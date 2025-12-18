"""
LangChain-Amorce Integration

Secure LangChain agents with Ed25519 signatures and HITL approvals.
Now with agent discovery via Amorce ANS!
"""

from langchain_amorce.agent import AmorceAgent
from langchain_amorce.tools import AmorceToolWrapper
from langchain_amorce.discovery import (
    AmorceSearchAgentsTool,
    AmorceGetAgentTool,
    get_amorce_discovery_tools,
)

__version__ = "0.2.0"
__all__ = [
    "AmorceAgent",
    "AmorceToolWrapper",
    "AmorceSearchAgentsTool",
    "AmorceGetAgentTool",
    "get_amorce_discovery_tools",
]
