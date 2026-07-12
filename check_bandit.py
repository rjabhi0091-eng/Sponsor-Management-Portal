import json
with open('bandit_report.json') as f:
    report = json.load(f)
for issue in report['results']:
    if issue['issue_severity'] in ['HIGH', 'MEDIUM']:
        print(f"{issue['issue_severity']}: {issue['issue_text']} at line {issue['line_number']}")
print(f"Total High/Medium: {sum(1 for i in report['results'] if i['issue_severity'] in ['HIGH', 'MEDIUM'])}")
