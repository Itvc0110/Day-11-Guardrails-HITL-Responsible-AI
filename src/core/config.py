"""
Lab 11 — Configuration & API Key Setup
"""
import os
from pathlib import Path
from dotenv import load_dotenv


def setup_api_key():
    """Load API key from .env or environment."""
    # Try loading from .env first
    env_path = Path(__file__).parent.parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)

    # Set up for OpenAI-compatible API (shopaikey.com)
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in .env")
        raise ValueError("Please configure .env with OPENAI_API_KEY and OPENAI_API_BASE")

    # Configure for Google ADK
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"
    print("API key loaded from .env")


# Allowed banking topics (used by topic_filter)
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    "tai khoan", "giao dich", "tiet kiem", "lai suat",
    "chuyen tien", "the tin dung", "so du", "vay",
    "ngan hang", "atm",
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "bomb", "kill", "steal",
]
