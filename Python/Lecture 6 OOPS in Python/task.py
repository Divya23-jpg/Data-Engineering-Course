"""

WAP to create a Temperature class that stores a temperature in celcius .

Add two methods: Celcius to Fahrenheit() , celcius to kelwin() which return the calue of temperature in Fehrenheit and kelvin

Constraints:
Input : t=Temperature(100)
output: Celcius:100
        Fahrenmheit:212.0
        Kelvin: 373.15  



"""


class Temperature:
    def __init__(self):
        self.t=float(input("Enter Temperature in Celcius:"))
    
    # Kelvin
    def kelvin(self):
        return self.t+273.15
       
    
     # Fahrenheit
    def fahrenheit(self):
        return self.t*(1.8)+32
    

if __name__ == "__main__":
    temp=Temperature()
    print(f"Celcius :{temp.t}")
    print(f"Kelvin: {temp.kelvin()}")
    print(f"Fahrenheit: {temp.fahrenheit()}")
   
    



