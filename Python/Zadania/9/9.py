h = float(input("Podaj swoją wysokość [m]: "))
w = float(input("Podaj swoją wagę [kg]: "))*10000

bmiE = w/(h*h)
bmi = round(bmiE,2)

if bmi < 20:
    print(f"Twoje BMI wynosi {bmi}. Masz niedowagę.")
elif bmi >= 20 and bmi < 25:
    print(f"Twoje BMI wynosi {bmi}. Masz prawidłową wagę.")
elif bmi >= 25 and bmi < 30:
    print(f"Twoje BMI wynosi {bmi}. Masz nadwagę.")
else:
    print(f"Twoje BMI wynosi {bmi}. Cierpisz na otyłość.")
