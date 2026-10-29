import duckdb

CSV_FILE = "complaints-2026-10-20_10_02.csv" 
con = duckdb.connect("complaints.db") 

con.execute(f"CREATE OR REPLACE TABLE complaints AS SELECT * FROM read_csv_auto('{CSV_FILE}')")
total = con.execute("SELECT COUNT (*) FROM complaints") . fetchone()[0]
print(f"Loaded {total} complaints into DuckDB.")

top_issues = con.execute("""
    SELECT Issue, COUNT(*) AS num_complaints
    FROM complaints
    GROUP BY Issue
    ORDER BY num_complaints DESC
    LIMIT 5
""").fetchall()

for issue, count in top_issues:
    print(f"{count:5d} | {issue}")

top_issues = con.execute('''
    SELECT Company, COUNT(*) AS num_complaints
    FROM complaints
    WHERE Issue = 'Problem caused by your funds being low'
    GROUP BY Company
    ORDER BY num_complaints DESC
    LIMIT 5
''').fetchall()

print("\nTop 5 banks for low-funds complaints:")
for company, count in top_issues:
    print(f"{count:5d} | {company}")