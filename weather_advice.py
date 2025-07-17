weather = input ("What's the weather like today? (Sunny/rainy/cold): ").strip().lower()

if weather == "Sunny":
    print("Wear a t-shirt and sunglasses") 
elif weather == "rainy":
    print("Dont forget your umbrella and raincoat")
elif weather == "cold":
    print("Wear warm coat and gloves")
elif weather == "windy":
    print("Sorry, I don't have advice for windy weather")
else:
    print("Sorry, I don't understand that weather condition")
