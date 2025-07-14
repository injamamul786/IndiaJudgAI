
import google.generativeai as genai
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("What is quantum computing?")
import os
import csv
import time
import json
import re

API = YOUR-GOOGLE-GEMINI-API-KEY
# 1. Configure Gemini API
genai.configure(api_key=API)
model = genai.GenerativeModel("gemini-1.5-flash")

# 2. Prompt builder
def build_prompt(case_text):
    return f"""
    You are a legal assistant. From the case text below, extract:

    1. input_text: Combine IPC sections and a summary of the case (max 100 words).
    2. outcome: State if bail was granted or not granted or judgment in favor of petitioner or against petitioner. Then list 3 case law references that support this outcome.

    If information is missing, use your legal knowledge. If still unavailable, return "Not available".

    Output as a JSON object.

    Case:
    \"\"\"{case_text}\"\"\"
    """

# 4. Summarize using Gemini
def summarize_case(case_text):
    try:
        prompt = build_prompt(case_text)
        response = model.generate_content(prompt)
        content = response.text.strip()

        # Remove ```json or ``` if present
        if content.startswith("```"):
            content = re.sub(r"^```(json)?", "", content.strip(), flags=re.IGNORECASE)
            content = content.strip().rstrip("```").strip()
        content = re.sub(r",\s*}", "}", content)
        content = re.sub(r",\s*]", "]", content)
        return content
    except Exception as e:
        print(f"Gemini error: {e}")
        return '{"input_text": "Not available", "outcome": "Not available"}'
# 5. Save output to CSV
def save_to_csv(data, filename="output.csv"):
    fieldnames = ["input_text", "outcome"]
    with open(filename, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        for row in data:
            writer.writerow(row)

# 6. Main pipeline
def main():
    all_results = []
    for i in range(2201, 2301):                                                                
        file_path = "link_to_text/" + str(i) + ".txt"
        # print(f"Processing: {file_path}")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                case_text = f.read()
                # print(case_text)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
        result_json = summarize_case(case_text)
        # print(result_json)
        try:
            result = json.loads(result_json)
            all_results.append({
                "input_text": result.get("input_text", "Not available"),
                "outcome": result.get("outcome", "Not available")
            })
        except Exception as e:
            print(f"Parsing error for {file_path}: {e}")

        time.sleep(2)  # Avoid API rate limits
    
    save_to_csv(all_results)
    print("✅ All done! Results saved to output.csv")

if __name__ == "__main__":
    main()
