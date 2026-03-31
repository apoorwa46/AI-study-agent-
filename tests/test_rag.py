from backend.services.rag_service import process_pdf, ask_question

# 🔹 Step 1: Process PDF
file_path = "data/uploads/sample.pdf"   # put your test pdf here

print("Processing PDF...")
process_pdf(file_path)
print("PDF processed successfully!\n")


# 🔹 Step 2: Ask Question
while True:
    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    answer = ask_question(query)

    print("\nAnswer:")
    print(answer)