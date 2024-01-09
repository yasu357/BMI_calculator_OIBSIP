import tkinter as tk
from tkinter import messagebox

class BMICalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculator")
        self.geometry("300x200")

        self.label_weight = tk.Label(self, text="Enter Weight (kg):")
        self.entry_weight = tk.Entry(self)

        self.label_height = tk.Label(self, text="Enter Height (m):")
        self.entry_height = tk.Entry(self)

        self.btn_calculate = tk.Button(self, text="Calculate BMI", command=self.calculate_bmi)

        self.result_label = tk.Label(self, text="Result: ")

        self.label_weight.pack(pady=5)
        self.entry_weight.pack(pady=5)
        self.label_height.pack(pady=5)
        self.entry_height.pack(pady=5)
        self.btn_calculate.pack(pady=10)
        self.result_label.pack(pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())

            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")

            bmi = weight / (height ** 2)
            category = self.classify_bmi(bmi)

            self.result_label.config(text=f"Result: BMI = {bmi:.2f} - {category}")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

if __name__ == "__main__":
    app = BMICalculator()
    app.mainloop()
