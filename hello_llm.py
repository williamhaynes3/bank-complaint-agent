from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

msg = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=300,
    messages=[{"role": "user", "content": "A bank customer writes: 'You charged me a $35 overdraft fee twice.' Classify this complaint and suggest a next step."}],
)
print(msg.content[0].text)
