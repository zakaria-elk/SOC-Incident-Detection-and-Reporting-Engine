# 🛡️ SOC Incident Detection and Reporting Engine

## 📌 Project Overview

This project demonstrates the development of a Security Operations Center (SOC) Incident Detection and Reporting Engine using Splunk Enterprise and Python.

The objective of this project is to simulate a real SOC environment by collecting Windows Security Events, detecting suspicious activities using Splunk, calculating risk scores using Python, generating incidents, assigning priorities, and creating incident response recommendations.

---

# 🎯 Project Objectives

- Detect suspicious activities from Windows Event Logs.
- Analyze security events using Splunk Enterprise.
- Generate incidents automatically using Python.
- Calculate risk scores based on security indicators.
- Classify incidents by severity.
- Assign SOC teams and priorities.
- Export incident reports.
- Simulate a real SOC Incident Response workflow.

---

# 🛠️ Technologies Used

- Splunk Enterprise 10.4
- Python 3.14
- Windows Event Logs
- CSV Files
- Windows 10

---

# 🔍 Splunk Use Cases Implemented

## Authentication Monitoring

### Successful Logins
- Event ID: 4624
- Objective:
  - Monitor successful user authentications.

### Failed Logins (Brute Force Detection)
- Event ID: 4625
- Objective:
  - Detect brute-force attacks.
  - Monitor failed authentication attempts.

Search:

```spl
source="WinEventLog:Security" EventCode=4625
```

---

## Privileged Activity Detection

### Special Privileges Assigned
- Event ID: 4672

Objective:
- Detect privileged account activity.
- Monitor administrative actions.

Search:

```spl
source="WinEventLog:Security" EventCode=4672
```

---

## Process Creation Monitoring

### Process Creation Events
- Event ID: 4688

Objective:
- Detect process execution activity.
- Monitor suspicious processes.

Search:

```spl
source="WinEventLog:Security" EventCode=4688
```

---

## Password Change Monitoring

### Password Changes
- Event ID: 4723

Objective:
- Detect password modifications.

Search:

```spl
source="WinEventLog:Security" EventCode=4723
```

---

## User Added To Administrator Group

### Group Membership Changes
- Event ID: 4732

Objective:
- Detect privilege escalation attempts.

Search:

```spl
source="WinEventLog:Security" EventCode=4732
```

---

# 📊 Security Analytics

## Event Statistics

```spl
source="WinEventLog:Security"
| stats count by EventCode
| sort - count
```

Purpose:
- Identify the most frequent security events.

---

## Timeline Analysis

```spl
source="WinEventLog:Security" EventCode=4672
| timechart span=1h count
```

Purpose:
- Visualize security events over time.

---

# 📈 Splunk Dashboard Components

The SOC Dashboard contains:

- Successful Logins
- Failed Logins
- Privileged Activity
- Password Changes
- Process Creation Events
- Brute Force Detection
- Timeline Analysis
- Event Statistics
- Risk Indicators

---

# 🐍 Python Development

## Version 1
### File:
```
soc_report.py
```

Features:
- Variables
- Print Statements
- Basic Risk Calculation

---

## Version 2
### File:
```
soc_report_v2.py
```

Features:
- User Input
- Dynamic Values

---

## Version 3
### File:
```
soc_report_v3.py
```

Features:
- Conditional Statements
- Severity Classification

---

## Version 4
### File:
```
soc_report_v4.py
```

Features:
- CSV Processing
- Dictionaries

---

## Version 5
### File:
```
soc_report_v5.py
```

Features:
- Incident ID Generation
- Date and Time
- Incident Status

---

## Version 6
### File:
```
soc_report_v6.py
```

Features:
- Analyst Recommendations
- Incident Categorization

---

## Version 7
### File:
```
soc_report_v7.py
```

Features:
- Incident Report Export

---

## Version 8
### File:
```
soc_report_v8.py
```

Features:
- Weighted Risk Scoring
- Threat Analysis Engine

Risk Formula:

```python
risk_score = (
    failed_logins * 2 +
    privileged_logins * 3 +
    password_changes * 5 +
    process_creations // 10
)
```

---

## Version 9
### File:
```
soc_report_v9.py
```

Features:
- Case Management
- Priority Assignment
- Team Assignment
- Analyst Ownership
- Incident Response Workflow

---

# 🚨 Threat Scoring Engine

The project implements a weighted risk scoring engine:

| Indicator | Weight |
|-----------|---------|
| Failed Logins | x2 |
| Privileged Logins | x3 |
| Password Changes | x5 |
| Process Creation | /10 |

Example:

```
Failed Login Score      : 20
Privileged Login Score  : 207
Password Change Score   : 10
Process Creation Score  : 9

Risk Score              : 246
```

---

# 🎯 Incident Classification

| Risk Score | Severity | Priority |
|------------|----------|----------|
| 300+ | CRITICAL | P1 |
| 150+ | HIGH | P2 |
| 50+ | MEDIUM | P3 |
| <50 | LOW | P4 |

---

# 🗂️ Case Management

Example:

```
Incident ID      : SOC-20260704-043701
Case ID          : CASE-20260704-043701

Risk Score       : 246
Severity         : HIGH
Priority         : P2
Case Status      : OPEN
Assigned Team    : SOC Tier 2
Analyst          : Zakaria
Recommendation   : Investigate Immediately
```

---

# 📂 Project Structure

```
SOC-Incident-Detection-and-Reporting-Engine/

README.md
LICENSE

soc_report.py
soc_report_v2.py
soc_report_v3.py
soc_report_v4.py
soc_report_v5.py
soc_report_v6.py
soc_report_v7.py
soc_report_v8.py
soc_report_v9.py

soc_data.csv
incident_report.txt

SOC_Project.txt
```

---

# 🎓 Skills Demonstrated

## SOC Skills
- Security Monitoring
- Log Analysis
- Incident Detection
- Incident Response
- Threat Hunting
- Risk Assessment
- Case Management

## Splunk Skills
- Search Processing Language (SPL)
- Dashboard Creation
- Security Analytics
- Event Correlation
- Timeline Analysis
- Windows Event Monitoring

## Python Skills
- Variables
- Conditional Statements
- Dictionaries
- File Handling
- CSV Processing
- Datetime Module
- Automation

---

# 🏆 Project Status

```
STATUS: COMPLETED
VERSION: v9
TYPE: Portfolio Project
LEVEL: Junior SOC Analyst
```

---

Junior SOC Analyst | Splunk | Python | Cybersecurity
