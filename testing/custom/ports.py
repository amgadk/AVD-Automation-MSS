"""
ports.py
ANTA Custom Test Classes using native AntaTemplate to bypass command caching bugs.
"""

from pydantic import Field, IPvAnyAddress
from typing import Literal, Optional
from anta.models import AntaTest, AntaCommand, AntaTemplate
from anta.tests.connectivity import VerifyReachability

class BaseLayer4Socket(AntaTest):
    """Base class providing transport path validation via native switch iperf utility templates."""
    categories = ["connectivity"]
    
    # --- THE CORE FIX: Define an AntaTemplate token instead of a static AntaCommand ---
    commands = [AntaTemplate(template="bash timeout {timeout} iperf -c {destination} -p {port} {udp_flag} -t 2", ofmt="text")]

    class Input(AntaTest.Input):
        """Input schema validation for Layer 4 socket targets."""
        destination: IPvAnyAddress = Field(description="Target destination IP address to test.")
        port: int = Field(description="Layer 4 target destination port number (1-65535).", ge=1, le=65535)
        timeout: int = Field(default=4, description="Handshake timeout in seconds.")

class TCP(BaseLayer4Socket):
    """Validates active Layer 4 transport path parameters by rendering an iperf TCP client."""
    name = "TCP"
    description = "Validates active Layer 4 TCP transport path connectivity parameters using iperf."

    def render(self, template: AntaTemplate) -> list[AntaCommand]:
        """Dynamically renders the AntaTemplate into a pristine execution instance command."""
        # --- THE FIX: Leverage the framework template engine to build the command ---
        return [
            template.render(
                timeout=self.inputs.timeout + 3,
                destination=str(self.inputs.destination),
                port=self.inputs.port,
                udp_flag=""  # Plain TCP mode execution
            )
        ]

    @AntaTest.anta_test
    def test(self) -> None:
        """Evaluates the structural text output from the template execution context."""
        command_output = self.instance_commands[0].output.lower()
        
        if "connected" in command_output:
            self.result.is_success()
        else:
            self.result.is_failure(
                f"iperf transport test failed to connect. Raw output stream returned: {command_output.strip()}"
            )

class Telnet(BaseLayer4Socket):
    """Validates cleartext Telnet path connectivity using native iperf templates."""
    name = "Telnet"
    description = "Validates active cleartext Telnet application layer delivery parameters."
    
    class Input(BaseLayer4Socket.Input):
        port: int = Field(default=23, description="Telnet transport port.", ge=1, le=65535)
        timeout: int = Field(default=4, description="Handshake timeout in seconds.")

    def render(self, template: AntaTemplate) -> list[AntaCommand]:
        """Renders an isolated template mapping for port 23."""
        return [
            template.render(
                timeout=self.inputs.timeout + 3,
                destination=str(self.inputs.destination),
                port=self.inputs.port,
                udp_flag=""
            )
        ]

    @AntaTest.anta_test
    def test(self) -> None:
        """Evaluates the Telnet connection results."""
        command_output = self.instance_commands[0].output.lower()
        
        if "connected" in command_output:
            self.result.is_success()
        else:
            self.result.is_failure(
                f"iperf transport test failed to connect. Raw output stream returned: {command_output.strip()}"
            )

class UDP(BaseLayer4Socket):
    """Validates active UDP transport path parameters by rendering an iperf UDP client."""
    name = "UDP"
    description = "Validates active Layer 4 UDP transport path connectivity parameters using iperf."

    def render(self, template: AntaTemplate) -> list[AntaCommand]:
        """Renders the template with the -u UDP flag active."""
        return [
            template.render(
                timeout=self.inputs.timeout + 3,
                destination=str(self.inputs.destination),
                port=self.inputs.port,
                udp_flag="-u"  # Pass the UDP flag to the binary template
            )
        ]

    @AntaTest.anta_test
    def test(self) -> None:
        """Evaluates the UDP transaction logs."""
        command_output = self.instance_commands[0].output.lower()
        
        if "connected" in command_output or "connected with" in command_output:
            self.result.is_success()
        else:
            self.result.is_failure(f"UDP iperf test failed: {command_output.strip()}")

class ICMP(VerifyReachability):
    """Natively executes VerifyReachability but maps 'ICMP' directly under the Test column."""
    name = "ICMP"
    description = "Test network reachability to one or many destination IP(s) via standard ICMP echo."
