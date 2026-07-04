successful_logins = 74
failed_logins = 10
privileged_logins = 69
process_creations = 98
password_changes = 2

risk_score = failed_logins + privileged_logins

print("================================")
print("SOC INCIDENT SUMMARY REPORT")
print("================================")

print("Successful Logins :", successful_logins)
print("Failed Logins     :", failed_logins)
print("Privileged Logins :", privileged_logins)
print("Process Creations :", process_creations)
print("Password Changes  :", password_changes)

print("\nRisk Score:", risk_score)

if risk_score >= 50:
    print("Alert Level: HIGH")
elif risk_score >= 20:
    print("Alert Level: MEDIUM")
else:
    print("Alert Level: LOW")

print("================================")