from langchain_google_genai import ChatGoogleGenerativeAI

from trip_x.config.settings import settings


def get_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=settings.model_name,
        google_api_key=settings.google_api_key,
        max_retries=2,
        timeout=60
    )
