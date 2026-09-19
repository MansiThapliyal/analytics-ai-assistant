# 🚗 Analytics AI Assistant — English to SQL to Insights

Ask a business question in plain English. The app writes the SQL, runs it safely against a rental-car database, and returns a table and chart.

> \\\*\\\*"Top 3 cities by revenue in the last 90 days"\\\*\\\* → correct 3-table join, date filter, grouped result, bar chart — no SQL written by the user.

\---

## How it works

```
User question
     → LLM (Llama 3.3 via Groq) + database schema as context
     → generated SQL (shown to the user for transparency)
     → guardrail: single SELECT-only queries allowed, write/DDL statements blocked
     → executed on SQLite → results as table + auto-chart (Streamlit)
```

**Stack:** Python · OpenAI-compatible API (Groq / Llama 3.3 70B) · SQLite · Streamlit · Faker (synthetic data)

The database is fully synthetic (generated with Faker) — 6 Indian cities, 200 cars, 5,000 rentals over 12 months. No real data anywhere.

\---

## Run it yourself (\~4 minutes)

```bash
# 1. Clone
git clone https://github.com/MansiThapliyal/analytics-ai-assistant.git
cd analytics-ai-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your (free) API key
#    Get one at https://console.groq.com → API Keys
#    Then copy the template and paste your key inside:
cp .env.example .env

# 4. Build the database
python generate\\\_data.py

# 5. Launch
streamlit run app.py
```

\---

## Evaluation

The agent was tested against 10 analytical questions of increasing difficulty (aggregates → multi-table joins → date math → utilization metrics).

\---

## Guardrails

* Only single `SELECT` statements are executed — `INSERT / UPDATE / DELETE / DROP / ALTER / PRAGMA` are rejected before touching the database
* The generated SQL is always displayed before results, so the user can verify what was actually run
* LLM temperature set to 0 for deterministic query generation

\---

## Known limitations

* Date phrasing can be ambiguous ("last month" = calendar month vs. last 30 days)
* Hand-written schema description — works for 3 tables, wouldn't scale to a real 200-table warehouse without retrieval
* No conversation memory — each question is independent
* Accuracy is high but not guaranteed; production use would need confidence checks and human review for high-stakes queries

## Roadmap

* \[ ] Vector store (Chroma) over schema docs + business-metric definitions → true RAG at scale
* \[ ] Second tool: metric explainer ("what does utilization mean here?")
* \[ ] Retry-with-error-feedback loop for failed queries
* \[ ] Rebuild pipeline on Databricks with Delta tables (in progress — see roadmap)

\---

## About

Built by [Mansi Thapliyal](https://www.linkedin.com/in/mansi-thapliyal-21699617a) — Data Analyst exploring the AI-application layer on top of 4 years of SQL, ETL, and BI experience.

