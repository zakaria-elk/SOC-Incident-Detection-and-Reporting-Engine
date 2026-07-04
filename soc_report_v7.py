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

# Calculate risk score
risk_score = failed_logins + privileged_logins

# Generate Incident ID
incident_id = "SOC-" + datetime.now().strftime("%Y%m%d-%H%M%S")

# Current date and time
current_time = datetime.now()

# Determine severity, status and recommendation
if risk_score >= 100:
    severity = "CRITICAL"
    status = "INCIDENT RESPONSE REQUIRED"
    recommendation = "Activate Incident Response Team"

elif risk_score >= 50:
    severity = "HIGH"
    status = "OPEN"
    recommendation = "Investigate Immediately"

elif risk_score >= 20:
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
print("Successful Logins :", successful_logins)
print("Failed Logins     :", failed_logins)
print("Privileged Logins :", privileged_logins)
print("Process Creations :", process_creations)
print("Password Changes  :", password_changes)

print("\nRisk Score        :", risk_score)
print("Severity          :", severity)
print("Status            :", status)
print("Recommendation    :", recommendation)

print("=====================================")

# Export report to file
report = f"""
========== INCIDENT REPORT ==========

Incident ID       : {incident_id}
Date              : {current_time}

Successful Logins : {successful_logins}
Failed Logins     : {failed_logins}
Privileged Logins : {privileged_logins}
Process Creations : {process_creations}
Password Changes  : {password_changes}

Risk Score        : {risk_score}
Severity          : {severity}
Status            : {status}
Recommendation    : {recommendation}

=====================================
"""

with open("incident_report.txt", "w") as file:
    file.write(report)

print("\nIncident report exported successfully.")