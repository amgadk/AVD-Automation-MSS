"""
ANTA Custom Test Classes for multi-protocol data plane transport testing.
"""

from pydantic import Field, IPvAnyAddress
from typing import Literal
from anta.models import AntaTest, AntaCommand
from anta.tests.connectivity import VerifyReachability

class BaseLayer4Socket(AntaTest):
    """Base class providing transport socket connectivity validation logic via Netcat."""
    categories = ["connectivity"]
    commands = [AntaCommand(command="bash timeout 5 echo 'ANTA_L4_INIT'", ofmt="text")]

    class Input(AntaTest.Input):
        """Input schema validation for Layer 4 socket targets."""
        destination: IPvAnyAddress = Field(description="Target destination IP address to test.")
        port: int = Field(description="Layer 4 target destination port number (1-65535).", ge=1, le=65535)
        protocol: Literal["tcp", "udp"] = Field(default="tcp", description="Transport protocol layer type.")
        timeout: int = Field(default=2, description="Handshake timeout in seconds.")

    def render(self) -> list[AntaCommand]:
        """Dynamically builds the bash netcat command string using valid EOS constraints."""
        udp_flag = "-u " if self.inputs.protocol == "udp" else ""
        cmd_string = f"bash timeout {self.inputs.timeout + 2} nc -z{udp_flag}v -w {self.inputs.timeout} {self.inputs.destination} {self.inputs.port}"
        
        # Overwrite the command property on the instantiated elements array
        self.commands[0].command = cmd_string
        return self.commands

    @AntaTest.anta_test
    def test(self) -> None:
        """Evaluates the terminal output from the Arista eAPI engine."""
        # --- THE FIX FOR ATTRIBUTEERROR: Fetch explicitly from index 0 ---
        command_output = self.instance_commands[0].output
        
        if "succeeded" in command_output.lower() or "open" in command_output.lower():
            self.result.is_success()
        else:
            self.result.is_failure(
                f"Transport block failure. {self.name} Port {self.inputs.port} "
                f"to {self.inputs.destination} timed out or was dropped."
            )

# ====================================================================
#  DEDICATED STATIC ATTRIBUTE CLASSES FOR EXACT 'TEST' COLUMN MAPPING
# ====================================================================

class TCP(BaseLayer4Socket):
    """Validates active TCP transport socket connectivity."""
    # --- THE FIX FOR TEST COLUMN: Define name statically at the class level ---
    name = "TCP"
    description = "Validates active Layer 4 TCP transport path socket delivery parameters."

class UDP(BaseLayer4Socket):
    """Validates active UDP transport socket connectivity."""
    name = "UDP"
    description = "Validates active Layer 4 UDP transport path socket delivery parameters."

class Telnet(BaseLayer4Socket):
    """Validates active Telnet application layer transport connectivity."""
    name = "Telnet"
    description = "Validates active cleartext Telnet application layer delivery parameters."

class ICMP(VerifyReachability):
    """Natively executes VerifyReachability but maps 'ICMP' directly under the Test column."""
    name = "ICMP"
    description = "Test network reachability to one or many destination IP(s) via standard ICMP echo."
