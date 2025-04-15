from transformers import pipeline

# FLAN-T5 ko text generation ke liye load karna
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

# Function jo ek question ka ek structured output dega
def ask_chatbot(prompt, max_length=100):
    response = chatbot(prompt, max_length=max_length, truncation=True)
    return response[0]['generated_text']

# Test prompts
questions = [
    "How do I stay motivated?",
    "What are the benefits of meditation?",
    "Tell me a productivity hack"
]

# Har question ka separate output
for idx, question in enumerate(questions, start=1):
    answer = ask_chatbot(question, max_length=100)
    print(f"🔹 **Question {idx}:** {question}")
    print(f"💡 **Answer:** {answer}\n" + "-"*50 + "\n")
