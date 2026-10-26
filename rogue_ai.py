
# ============================================================
# CMP 131 - ROGUE AI EMERGENCY DIAGNOSTIC SYSTEM
# Team members: Ryan, Andrew
# ============================================================

print("========================================")
print("     ROGUE AI DIAGNOSTIC SYSTEM")
print("========================================")

# LEVEL 1 - TEMPERATURE DIAGNOSTIC
# Ask for the system temperature and make the required decision.

system_temperature=input ("what is...")
print("temp",system_temperature)
if (system_temperature>100):
    print("warning system overheat")
else:
    print("safe")

# LEVEL 2 - POWER DIAGNOSTIC
# Ask for the battery percentage and make the required decision.
battery=int("What is the battery level")

if(battery<20):
    print("low power")
else:
    print("power normal")

# LEVEL 3 - SECURITY DIAGNOSTIC
# Ask for the security status and make the required decision.

security=input ("what is your security")
if security== "danger":
    print("shutdown required")
else:
    print("system secure")

print("========================================")
print("Diagnostic complete.")
print("========================================")
