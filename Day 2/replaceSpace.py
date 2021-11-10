# Python program to replace double spaces in a paragraph with a single space

par = input("Enter the paragraph(s):\n")

par = par.replace("  ", " ")  # Replaces '  ' (double spaces) in a paragraph with a ' ' (single space)

print(par)
