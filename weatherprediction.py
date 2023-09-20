import time

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print() 

while True:
    city = input("Enter a city (or 'quit' to exit): ")
    
    if city.lower() == 'quit':
        slow_print("Goodbye!")
        break  # Exit the loop when 'quit' is entered
    
    slow_print(f"Checking the weather in {city}...")
    slow_print("Analyzing weather data...")
    slow_print("Running algorithms...")
    slow_print("Hmm omo...")
    slow_print("Check outside oga mi\n")
