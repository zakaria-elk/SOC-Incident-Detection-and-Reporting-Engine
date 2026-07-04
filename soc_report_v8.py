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

# Generate Incident ID
incident_id = "SOC-" + datetime.now().strftime("%Y%m%d-%H%M%S")

# Current date and time
current_time = datetime.now()

# Severity + Status + Recommendation
if risk_score >= 300:
    severity = "CRITICAL"
    status = "INCIDENT RESPONSE REQUIRED"
    recommendation = "Activate Incident Response Team"

elif risk_score >= 150:
    severity = "HIGH"
    status = "OPEN"
    recommendation = "Investigate Immediately"

elif risk_score >= 50:
    severity = "MEDIUM"
    status = "MONITORING"
    recommendation = "Continue Monitoring"

else:
    severity = "LOW"
    status = "CLOSED"
    recommendation = "No Action Required"

# Display report
print("\n========== INCIDENT REPORT ==========")

print("Incident ID       :", incident_id)
print("Date              :", current_time)

print("\n========== EVENTS ==========")

print("Successful Logins :", successful_logins)
print("Failed Logins     :", failed_logins)
print("Privileged Logins :", privileged_logins)
print("Process Creations :", process_creations)
print("Password Changes  :", password_changes)

print("\n========== THREAT ANALYSIS ==========")

print("Failed Login Score     :", failed_score)
print("Privileged Login Score :", privileged_score)
print("Password Change Score  :", password_score)
print("Process Creation Score :", process_score)

print("\n========== FINAL ASSESSMENT ==========")

print("Risk Score        :", risk_score)
print("Severity          :", severity)
print("Status            :", status)
print("Recommendation    :", recommendation)

print("======================================")

# Export report
report = f"""
========== INCIDENT REPORT ==========

Incident ID       : {incident_id}
Date              : {current_time}

========== EVENTS ==========

Successful Logins : {successful_logins}
Failed Logins     : {failed_logins}
Privileged Logins : {privileged_logins}
Process Creations : {process_creations}
Password Changes  : {password_changes}

========== THREAT ANALYSIS ==========

Failed Login Score     : {failed_score}
Privileged Login Score : {privileged_score}
Password Change Score  : {password_score}
Process Creation Score : {process_score}

========== FINAL ASSESSMENT ==========

Risk Score        : {risk_score}
Severity          : {severity}
Status            : {status}
Recommendation    : {recommendation}

======================================
"""

with open("incident_report.txt", "w") as file:
    file.write(report)

print("\nIncident report exported successfully.")