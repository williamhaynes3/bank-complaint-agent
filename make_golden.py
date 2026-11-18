import duckdb

con = duckdb.connect("complaints.db")
con.execute("""
    COPY (
        SELECT "Complaint ID", Company, Issue, "Sub-issue"
        FROM complaints
        USING SAMPLE 50 ROWS (reservoir, 42)
    ) TO 'golden_set.csv' (HEADER)
""")
print("Saved 50 complaints to golden_set.csv")