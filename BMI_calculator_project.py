class BMI_Calculator:
    def __init__(self, weight, height, unit="m"):
        self.weight = weight
        self.unit = unit.lower()

        if self.unit == "in":
            self.height = height * 0.0254
        else:
            self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def interpret_bmi(self):
        bmi = self.calculate_bmi()
        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("You are Underweight.")
        elif bmi < 25:
            print("You have Normal weight.")
        elif bmi < 30:
            print("You are Overweight.")
        else:
            print("You are Obese.")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height: "))
unit = input("Enter the unit of height (m for meters, in for inches): ")

bmi_obj = BMI_Calculator(weight, height, unit)
bmi_obj.interpret_bmi()
