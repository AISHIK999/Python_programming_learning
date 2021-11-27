# Python program to convert celcius to farenheit

def tempConv(celc):
    
    fare = (celc * 1.8)+32
    return fare

celc = int (input("Enter the temperature in Celcius/Centigrade:\n"))
farenheit = str(tempConv(celc))
print(str(celc) + " degree celcius means " + farenheit + " degree farenheit")
