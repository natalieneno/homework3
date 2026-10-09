"""This code will convert a temperature and use weather 
conditions outside to tell the user what to wear on a specific day."""

celsius= float(input("What is the temperature outside (in celsuis)?"))
fahrenheit = (celsius * (9 / 5) + 32)


uv_index = input("What is the UV index?")
is_raining = input("Is it raining? Answer yes or no: ")
is_walking = input("Will you be walking a lot? Answer yes or no: ")

print ("Temperature:", round(fahrenheit, 1), "degrees Fahrenheit")

if fahrenheit > 100 or fahrenheit < 0:
    print ("The temperature is too low or too high")
elif fahrenheit <= 25:
    print ("You must wear a winter jacket.")
elif fahrenheit <= 50:
    print ("You must wear a sweatshirt.")
else: 
    print ("You don't need a jacket.")

if uv_index < 0 or uv_index > 11:
    print ("The uv index is too low or too high.")
elif uv_index < 0:
    print ("Invalid UV index.")
elif uv_index < 3:
    print ("Low UV: sunscreen is optional.")
elif uv_index < 6:
    print ("Moderate UV: wear sunscreen.")
elif uv_index < 8:
    print ("High UV: wear sunscreen and seek shade.")
elif uv_index < 11:
    print ("Very high UV: wear sunscreen, seek shade, and wear protective clothing.")
else:
    print ("Extreme UV: use strong sun protection and avoid prolonged sun exposure.")

if is_raining == "yes":
    print ("Bring an umbrella.")

if is_walking == "yes":
    print ("You must wear sneakers")
else:
    print ("Choose your shoes.")
