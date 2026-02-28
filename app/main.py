from fastapi import FastAPI
from app.core.model import get_model
from app.core.memory import get_checkpointer
from app.agents.agent import build_agent
from app.core.schema import ChatRequest, ChatResponse
from app.core.prompts import load_system_prompt

app = FastAPI()

agent = build_agent(
    model=get_model(),
    checkpointer=get_checkpointer(),
)


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    config = {"configurable": {"thread_id": request.session_id}}

    response = agent.invoke(
        {
            "messages": [
                {"role": "system", "content": load_system_prompt()},
                {"role": "user", "content": request.message},
            ]
        },
        config=config,
    )

    # ToolStrategy → structured_response
    if "structured_response" in response:
        return response["structured_response"]

    # Fallback (non-tool answer, e.g greeting or comparison)
    return ChatResponse(
        message=response["messages"][-1].content
    )