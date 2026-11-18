import json
from typing import Literal 
from dotenv import load_dotenv 
from pydantic import BaseModel 
import anthropic 
import duckdb 

load_dotenv()
client = anthropic.Anthropic()


class TriageResult(BaseModel):
    issue_category: str
    urgency: Literal["low", "medium", "high"]
    reg_flag: Literal["Reg E", "Reg DD", "Reg Z", "UDAAP", "None"]
    route_to_human: bool
    next_step: str

con = duckdb.connect("complaints.db")
rows = con.execute("""  
    SELECT "Complaint ID", Company, Issue, "Sub-Issue"
    FROM complaints
    WHERE Company = 'WELLS FARGO & COMPANY'
    LIMIT 3
""").fetchall()

for cid, company, issue, sub_issue in rows:
    prompt = f"""
    Return ONLY valid JSON matching this schema:
    {json.dumps(TriageResult.model_json_schema())}

    Bank: {company}
    Issue: {issue}
    Sub-issue: {sub_issue}
    """

    msg = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = next(b.text for b in msg.content if hasattr(b, "text")).strip().removeprefix("```json").removesuffix("```").strip()
    result = TriageResult.model_validate_json(raw)
    print(cid, result.urgency, result.reg_flag, result.route_to_human)
    print("   ", result.next_step)
