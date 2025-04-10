kg = int(input("체중(kg): "))
cm = int(input("키(cm): "))

print("BMI " + str(round(kg / ((cm / 100) ** 2), 1)))
