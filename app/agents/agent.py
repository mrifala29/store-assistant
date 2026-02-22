from langchain.agents import create_agent

def build_agent(model, checkpointer):
    return create_agent(
        model=model,
        checkpointer=checkpointer,
        # tools=[],
        # middleware=[],
        # context_schema=[],
        # response_format=[],
    )