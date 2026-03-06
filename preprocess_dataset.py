import ast
import json

input_file = "qa_Appliances.json"
output_file = "cleaned_faq.json"

faqs = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = ast.literal_eval(line.strip())

            question = data.get("question")
            answer = data.get("answer")

            if question and answer and len(answer) > 15:
                faqs.append({
                    "question": question.strip(),
                    "answer": answer.strip()
                })

            if len(faqs) >= 5000:
                break

        except:
            continue

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(faqs, f, indent=4)

print("Total FAQs:", len(faqs))