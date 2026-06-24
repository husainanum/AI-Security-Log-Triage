import ollama


def read_logs():

    with open("logs/sample_logs.txt", "r") as file:
        return file.read()


def analyze_logs(logs):

    prompt = f"""

You are a cybersecurity SOC analyst.

Analyze these logs.


Provide:

1. Incident Summary
2. Severity Level (Low/Medium/High/Critical)
3. Attack Type
4. MITRE ATT&CK Technique Mapping
5. Indicators of Compromise
6. Recommended Response Actions


Logs:

{logs}

"""


    response = ollama.chat(
        model="llama3.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    return response["message"]["content"]



logs = read_logs()

report = analyze_logs(logs)


print("\n===== AI INCIDENT REPORT =====\n")

print(report)
