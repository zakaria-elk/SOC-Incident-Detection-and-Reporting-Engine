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

print("\n========== REPORT ==========")
print("Successful Logins :", successful_logins)
print("Failed Logins     :", failed_logins)
print("Privileged Logins :", privileged_logins)
print("Process Creations :", process_creations)
print("Password Changes  :", password_changes)

print("\nRisk Score:", risk_score)

if risk_score >= 100:
    print("Alert Level: CRITICAL")
    print("SOC ALERT: INCIDENT RESPONSE REQUIRED")
elif risk_score >= 50:
    print("Alert Level: HIGH")
elif risk_score >= 20:
    print("Alert Level: MEDIUM")
else:
    print("Alert Level: LOW")