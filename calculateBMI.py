
class CalculateBMI:
    def calBMI(self):
        for item in self.input:
            weight = item.get("WeightKg",0)
            height = item.get("HeightCm",0)

            mtr = height/100

            bmi = float(weight/(mtr*mtr))
            item["Bmi"] = bmi
            if bmi <= 18.4:
               item["Bmi Category"] = "Underweight"
               item["Health Risk"] = "Malnutrition risk"
            elif bmi >= 18.5 and bmi <= 24.9:
               item["Bmi Category"] = "Normal weight"
               item["Health Risk"] = "Low risk"
            elif bmi >= 25 and bmi <= 29.9:
               item["Bmi Category"] = "Overweight"
               item["Health Risk"] = "Enhanced risk"
            elif bmi >= 30 and bmi <= 34.9:
               item["Bmi Category"] = "Moderately obese"
               item["Health Risk"] = "Medium risk"
            elif bmi >= 35 and bmi <= 39.9:
               item["Bmi Category"] = "Severely obese"
               item["Health Risk"] = "High risk"
            else:
               item["Bmi Category"] = "Very severely obese"
               item["Health Risk"] = "Very high risk"   

        return (self.input)
    
    def countOverweight(self):
        count = 0

        for item in self.input:
           weight = item.get("WeightKg",0)
           height = item.get("HeightCm",0)

           mtr = height/100
           bmi = float(weight/(mtr*mtr))
           if bmi >= 25 and bmi <= 29.9:
             count +=1
        return count

    def __init__(self,input):
        self.input = input


if __name__ == "__main__":
  input_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

  calbmi = CalculateBMI(input_data)

  input_data = calbmi.calBMI()
  print("The modified output data is below:\n",input_data)
  count = calbmi.countOverweight()
  print("Total number of overweight people :",count)
  



          


  
