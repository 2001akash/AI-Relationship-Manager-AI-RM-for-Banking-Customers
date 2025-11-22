from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import ChatRequest, ChatResponse, ContextResponse
from config import PROFILE, TRANSACTIONS, INVESTMENTS
from utils.intent_utils import detect_intent
from handlers.transaction_handler import handle_transaction_insights
from handlers.investment_handler import handle_investment_overview
from handlers.recommendation_handler import handle_personalized_recommendation
from handlers.summary_handler import handle_smart_summary

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===========================
# GET /context
# ===========================
@app.get("/context", response_model=ContextResponse)
def get_context():
    return ContextResponse(
        profile=PROFILE,
        transactions=TRANSACTIONS,
        investments=INVESTMENTS
    )


# ===========================
# POST /chat
# ===========================
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    query = request.query.strip()
    intent = detect_intent(query)

    # -------------------------
    # SMALL TALK RESPONSES
    # -------------------------
    if intent == "greeting":
        return ChatResponse(
            reply="Hello! How can I assist you today? 😊",
            intent="small_talk",
            meta={}
        )

    if intent == "farewell":
        return ChatResponse(
            reply="Goodbye! Have a great day ahead 😊",
            intent="small_talk",
            meta={}
        )

    if intent == "thanks":
        return ChatResponse(
            reply="You're welcome! Happy to help anytime 😊",
            intent="small_talk",
            meta={}
        )

    # -------------------------
    # MAIN INTENTS
    # -------------------------
    if intent == "transaction_insights":
        return handle_transaction_insights(query)

    elif intent == "investment_overview":
        return handle_investment_overview(query)

    elif intent == "personalized_recommendation":
        return handle_personalized_recommendation(query)

    elif intent == "smart_summary":
        return handle_smart_summary(query)

    # -------------------------
    # FALLBACK
    # -------------------------
    return ChatResponse(
        reply="I'm here to assist with your financial questions!",
        intent="small_talk",
        meta={}
    )



# ===========================
# Run server (dev mode)
# ===========================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
