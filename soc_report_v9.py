from datetime import datetime

print("SOC INCIDENT SUMMARY REPORT")
print("==========================")

# Read data from CSV
data = {}

with open("soc_data.csv", "r") as file:
    for line in file:
        key, value = line.strip().split(",")
        data[key] = int(value)

# Extract values
successful_logins = data["successful_logins"]
failed_logins = data["failed_logins"]
privileged_logins = data["privileged_logins"]
process_creations = data["process_creations"]
password_changes = data["password_changes"]

# Threat scoring
failed_score = failed_logins * 2
privileged_score = privileged_logins * 3
password_score = password_changes * 5
process_score = process_creations // 10

# Total risk score
risk_score = (
    failed_score +
    privileged_score +
    password_score +
    process_score
)

# Generate IDs
current_time = datetime.now()

incident_id = "SOC-" + current_time.strftime("%Y%m%d-%H%M%S")
case_id = "CASE-" + current_time.strftime("%Y%m%d-%H%M%S")

# Analyst information
analyst = "Zakaria"
assigned_team = "SOC Tier 1"

# Severity + Case Management
if risk_score >= 300:
    severity = "CRITICAL"
    status = "OPEN"
    priority = "P1"
    recommendation = "Activate Incident Response Team"
    assigned_team = "SOC Tier 3"

elif risk_score >= 150:
    severity = "HIGH"
    status = "OPEN"
    priority = "P2"
    recommendation = "Investigate Immediately"
    assigned_team = "SOC Tier 2"

elif risk_score >= 50:
    severity = "MEDIUM"
    status = "MONITORING"
    priority = "P3"
    recommendation = "Continue Monitoring"

else:
    severity = "LOW"
    status = "CLOSED"
    priority = "P4"
    recommendation = "No Action Required"

# Display Incident
print("\n========== INCIDENT ==========")

print("Incident ID      :", incident_id)
print("Case ID          :", case_id)
print("Date             :", current_time)

# Display Events
print("\n========== EVENTS ==========")

print("Successful Logins :", successful_logins)
print("Failed Logins     :", failed_logins)
print("Privileged Logins :", privileged_logins)
print("Process Creations :", process_creations)
print("Password Changes  :", password_changes)

# Threat Analysis
print("\n====== THREAT ANALYSIS ======")

print("Failed Login Score     :", failed_score)
print("Privileged Login Score :", privileged_score)
print("Password Change Score  :", password_score)
print("Process Creation Score :", process_score)

# Case Management
print("\n======= CASE MANAGEMENT =======")

print("Risk Score       :", risk_score)
print("Severity         :", severity)
print("Priority         :", priority)
print("Case Status      :", status)
print("Assigned Team    :", assigned_team)
print("Analyst          :", analyst)
print("Recommendation   :", recommendation)

print("\n================================")

# Export report
report = f"""
========== INCIDENT ==========

Incident ID      : {incident_id}
Case ID          : {case_id}
Date             : {current_time}

========== EVENTS ==========

Successful Logins : {successful_logins}
Failed Logins     : {failed_logins}
Privileged Logins : {privileged_logins}
Process Creations : {process_creations}
Password Changes  : {password_changes}

====== THREAT ANALYSIS ======

Failed Login Score     : {failed_score}
Privileged Login Score : {privileged_score}
Password Change Score  : {password_score}
Process Creation Score : {process_score}

======= CASE MANAGEMENT =======

Risk Score       : {risk_score}
Severity         : {severity}
Priority         : {priority}
Case Status      : {status}
Assigned Team    : {assigned_team}
Analyst          : {analyst}
Recommendation   : {recommendation}

================================
"""

with open("incident_report.txt", "w") as file:
    file.write(report)

print("\nCase exported successfully.")