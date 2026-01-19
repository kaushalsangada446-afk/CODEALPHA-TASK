faqs = {
    "what is ai":
        "Artificial Intelligence (AI) is the simulation of human intelligence in machines.",

    "what is machine learning":
        "Machine Learning is a subset of AI that enables systems to learn from data without being explicitly programmed.",

    "what is deep learning":
        "Deep Learning is a branch of Machine Learning that uses multi-layer neural networks.",

    "what is python":
        "Python is a high-level programming language widely used in AI, data science, and web development.",

    "what is codealpha":
        "CodeAlpha is a platform that provides internships and real-world technical projects to students.",

    "what is data science":
        "Data Science is the field of analyzing data to extract meaningful insights.",

    "what is chatbot":
        "A chatbot is a computer program that simulates human conversation.",

    "what is nlp":
        "Natural Language Processing (NLP) helps machines understand human language.",

    "what is computer":
        "A computer is an electronic device that processes data and performs calculations."
}

print("\n🤖 ======= FAQ CHATBOT =======")
print("Type your question or type 'exit' to quit.\n")

while True:
    user = input("You: ").lower().strip()

    if user == "exit":
        print("Chatbot: Goodbye! Have a great day 👋")
        break

    found = False

    for question, answer in faqs.items():
        if question in user:
            print("Chatbot:", answer, "\n")
            found = True
            break

    if not found:
        print("Chatbot: Sorry, I don't have an answer for that. Try asking differently.\n")
