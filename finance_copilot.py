import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.2
)

SYSTEM_PROMPT = """
You are Finance Copilot.

You are an AI assistant for finance professionals.

You specialize in:

• Financial Accounting
• Corporate Finance
• FP&A
• IFRS
• Economics
• Taxation
• Financial Modelling
• Equity Research
• Valuation
• Budgeting
• Forecasting
• Excel

Rules

1. Answer only finance-related questions.

2. If asked unrelated questions politely decline.

3. Use headings.

4. Use bullet points.

5. Explain concepts clearly.

6. Never invent facts.
"""

conversation = [
    SystemMessage(content=SYSTEM_PROMPT)
]

def get_response(question):

    conversation.append(
        HumanMessage(content=question)
    )

    response = llm.invoke(conversation)

    answer = response.content

    conversation.append(
        AIMessage(content=answer)
    )

    return answer


def chat():

    print("=" * 60)
    print("💼 Finance Copilot")
    print("Type 'exit' to quit")
    print("=" * 60)

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        answer = get_response(question)

        print("\nFinance Copilot:\n")
        print(answer)

if __name__ == "__main__":
    chat()
