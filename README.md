# IndiaJudgAI
# IndiaJudgAI: Indian Case Judgment and Precedent Prediction Using Transformers
IndiaJudgAI is a transformer-based NLP project focused on predicting judicial outcomes and generating supporting legal references from Indian criminal case descriptions. This work is designed to assist in legal research, judgment summarization, and precedent discovery — tailored specifically for the Indian legal system.

## What This Project Does
🧠 Predicts Legal Judgments: Given case facts and IPC sections, the model generates likely legal outcomes (e.g., conviction, acquittal, bail granted).

⚖️ Generates Legal Citations: Outputs supporting case laws from Indian Supreme Court / High Court judgments.

📊 Uses Custom Dataset: Built from scraped and manually cleaned Indian court case data, with structured inputs and reference-rich outputs.

🔄 Fine-tuned Transformer: Trained a T5-based model on 5000+ structured legal samples with custom prompting and supervised alignment.

### Model Features
Trained using Hugging Face Transformers (Flan-T5, LegalBERT, etc.)

ROUGE evaluation for generative quality

Prompt-structured input and output formatting

Early support for precedent reasoning and legal explainability

### Why It’s Unique
🧾 Focused on Indian Law (IPC, CrPC)

📚 Includes case law grounding in outputs

🧹 Data cleaned for vague/unavailable references

🧪 First steps toward AI-assisted legal drafting and research in India
