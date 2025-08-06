from flask import Flask, render_template, request

app = Flask(__name__)

class BMI_Calculator:
    def __init__(self, weight, height, unit):
        self.weight = weight
        self.height = height
        self.unit = unit

    def convert_height_to_meters(self):
        if self.unit == 'in':
            return self.height * 0.0254
        return self.height

    def calculate_bmi(self):
        height_m = self.convert_height_to_meters()
        return self.weight / (height_m ** 2)

    def get_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight", bmi
        elif bmi < 25:
            return "Normal weight", bmi
        elif bmi < 30:
            return "Overweight", bmi
        else:
            return "Obese", bmi

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        unit = request.form['unit']

        person = BMI_Calculator(weight, height, unit)
        category, bmi_value = person.get_category()
        bmi_value = round(bmi_value, 2)

        return render_template('BMI_result.html', name=name, bmi=bmi_value, category=category)

    return render_template('BMI_input_form.html')

if __name__ == '__main__':
    app.run(debug=True)
