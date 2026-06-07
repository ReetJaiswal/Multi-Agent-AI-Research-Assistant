print("AI Research Assistant Started")
from services.llm_service import ask_llm

answer = ask_llm(
    "Explain Artificial Intelligence in simple terms."
)

print(answer)