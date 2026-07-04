from datetime import datetime

print("SOC INCIDENT SUMMARY REPORT")
print("==========================")

data = {}

with open("soc_data.csv", "r") as file:
    for line in file:
        key, value = line.strip().split(",")
        data[key] = int(value)

successful_logins = data["successful_logins"]
failed_logins = data["failed_logins"]
privileged_logins = data["privileged_logins"]
process_creations = data["process_creations"]
password_changes = data["password_changes"]

risk_score = failed_logins + privileged_logins

# Generate Incident ID
incident_id = "SOC-" + datetime.now().strftime("%Y%m%d-%H%M%S")

# Date
current_time = datetime.now()

# Severity + Recommendation
if risk_score >= 100:
    severity = "CRITICAL"
    status = "OPEN"
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