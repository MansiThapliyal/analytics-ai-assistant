import os
from dotenv import load_dotenv
from openai import OpenAI
from schema import SCHEMA

load_dotenv()
client = OpenAI(api_key=os.environ["GROQ_API_KEY"],
                base_url="https://api.groq.com/openai/v1")

PROMPT = """You are an expert SQLite analyst.
{schema}
Write ONE valid SQLite SELECT query answering: {question}
Rules: return ONLY the SQL. No explanation. No markdown. No semicolon issues.
"""

def question_to_sql(question: str) -> str:
    r = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role":"user",
                   "content": PROMPT.format(schema=SCHEMA, question=question)}],
        temperature=0)
    sql = r.choices[0].message.content.strip()
    return sql.replace("```sql","").replace("```","").strip()

if __name__ == "__main__":
    q = input("Ask a question: ")
    print(question_to_sql(q))