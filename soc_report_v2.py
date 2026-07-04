print("SOC INCIDENT SUMMARY REPORT")
print("==========================")

successful_logins = int(input("Enter successful logins: "))
failed_logins = int(input("Enter failed logins: "))
privileged_logins = int(input("Enter privileged logins: "))
process_creations = int(input("Enter process creations: "))
password_changes = int(input("Enter password changes: "))

risk_score = failed_logins + privileged_logins

print("\n========== REPORT ==========")
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