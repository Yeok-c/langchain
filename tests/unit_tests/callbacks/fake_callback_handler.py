"""A fake callback handler for testing purposes."""
from typing import Any, Dict, List

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish, LLMResult


class FakeCallbackHandler(BaseCallbackHandler):
    """Fake callback handler for testing."""

    def __init__(self) -> None:
        """Initialize the mock callback handler."""
        self.starts = 0
        self.ends = 0
        self.errors = 0

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when LLM starts running."""
        self.starts += 1

    def on_llm_end(
        self,
        response: LLMResult,
    ) -> None:
        """Run when LLM ends running."""
        self.ends += 1

    def on_llm_error(self, error: Exception) -> None:
        """Run when LLM errors."""
        self.errors += 1

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Run when chain starts running."""
        self.starts += 1

    def on_chain_end(self, outputs: Dict[str, Any]) -> None:
        """Run when chain ends running."""
        self.ends += 1

    def on_chain_error(self, error: Exception) -> None:
        """Run when chain errors."""
        self.errors += 1

    def on_tool_start(
        self, serialized: Dict[str, Any], action: AgentAction, **kwargs: Any
    ) -> None:
        """Run when tool starts running."""
        self.starts += 1

    def on_tool_end(self, output: str, **kwargs: Any) -> None:
        """Run when tool ends running."""
        self.ends += 1

    def on_tool_error(self, error: Exception) -> None:
        """Run when tool errors."""
        self.errors += 1

    def on_text(self, text: str, **kwargs: Any) -> None:
        """Run when agent is ending."""
        self.ends += 1

    def on_agent_end(self, finish: AgentFinish, **kwargs: Any) -> None:
        """Run when agent ends running."""
        self.ends += 1
