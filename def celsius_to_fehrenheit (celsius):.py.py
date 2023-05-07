def celsius_to_fehrenheit (celsius):
    fehrenheit = celsius * 9/5 + 32
    return fehrenheit
celsius = float(input("add temrache: "))
fehrenheit = celsius_to_fehrenheit(celsius)
print ("in fehrenheit: ", fehrenheit)
