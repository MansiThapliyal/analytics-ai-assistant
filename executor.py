import sqlite3, pandas as pd

def run_sql(sql: str) -> pd.DataFrame:
    s = sql.strip().lower()
    banned = ["insert","update","delete","drop","alter","create",";--","pragma"]
    if not s.startswith("select") or any(b in s for b in banned):
        raise ValueError("Only single SELECT queries are allowed.")
    conn = sqlite3.connect("rental.db")
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df