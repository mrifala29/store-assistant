from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from app.core.schema import ChatResponse
from app.tools.pricelist import search_pricelist


def build_agent(model, checkpointer):
    return create_agent(
        model=model,
        checkpointer=checkpointer,
        tools=[search_pricelist],
        response_format=ToolStrategy(ChatResponse),
    )