'''
Write a program to determine the BMI Category based on user input.
Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal"
'''

height = input("Enter height in meters: ")
weight = input("Enter weight in kilograms: ")

if height.replace(".", "", 1).isdigit() and weight.replace(".", "", 1).isdigit():
    height = float(height)
    weight = float(weight)
    bmi = weight / (height ** 2)

    if bmi >= 30:
        category = "Obesity"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    else:
        category = "Underweight"

    print(f"Your BMI: {bmi:.2f}")
    print(f"Category: {category}")
else:
    print("Invalid input. Please enter valid numeric values.")

'''
Write a program to determine which country a city belongs to. Given
list of cities per country: Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
                                  UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
                                India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi"
Output: "Abu Dhabi is in UAE"
'''

city_country = {
    "Sydney": "Australia",
    "Melbourne": "Australia",
    "Brisbane": "Australia",
    "Perth": "Australia",
    "Dubai": "UAE",
    "Abu Dhabi": "UAE",
    "Sharjah": "UAE",
    "Ajman": "UAE",
    "Mumbai": "India",
    "Bangalore": "India",
    "Chennai": "India",
    "Delhi": "India"
}

city_name = input("Enter a city name: ")

if city_name in city_country:
    country = city_country[city_name]
    print(f"{city_name} is in {country}")
else:
    print("City not found in the database.")

'''
Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the same country or not.
Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"

Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"
'''


city_to_country = {
    "Mumbai": "India",
    "Chennai": "India",
    "Sydney": "Australia",
    "Dubai": "United Arab Emirates"
}

first_city = input("Enter the first city: ")
second_city = input("Enter the second city: ")

if first_city in city_to_country and second_city in city_to_country:
    if city_to_country[first_city] == city_to_country[second_city]:
        print("Both cities are in", city_to_country[first_city])
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the dictionary.")
