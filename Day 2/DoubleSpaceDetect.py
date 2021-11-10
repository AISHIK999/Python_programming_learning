# Python program to detect double spaces in a paragraph

par = input("Enter the paragraph(s):\n")

val = par.count("  ")   # Counts the number of '  ' (double spaces) present in the string 'par' and assigns the value to the variable val

print(val, "double spaces are present in the paragraph(s)")
