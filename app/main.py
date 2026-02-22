from fastapi import FastAPI

from app.core.model import get_model
from app.core.memory import get_checkpointer
from app.agents.agent import build_agent
from app.core.schema import ChatRequest, ChatResponse


app = FastAPI()
model = get_model()

agent = build_agent(
    model=get_model(),
    checkpointer=get_checkpointer(),
)


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    config = {"configurable": {"thread_id": request.session_id}}

    response = agent.invoke(
        {"messages": [{"role": "user", "content": request.message}]},
        config=config,
    )

    reply = response["messages"][-1].content

    return ChatResponse(reply=reply)