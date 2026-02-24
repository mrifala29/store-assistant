from app.core.schema import ChatResponse

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

def build_agent(model, checkpointer):
    return create_agent(
        model=model,
        checkpointer=checkpointer,
        response_format=ToolStrategy(ChatResponse),
        # tools=[],
        # middleware=[],
        # context_schema=[],
    )