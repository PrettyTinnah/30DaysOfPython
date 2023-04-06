#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("Enter the number of years lived: "))

#there are 3.154**7 seconds in a year so 
seclived = 31536000 * years
print("You have lived for", seclived, "seconds")

#Write a Python script that displays the following table
# ```py
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1,6):
    print(i, end = " ")
    for j in range (1,4):
        print(i**j, end = " ")
    print(" ")
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

# ```py
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
# ```

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour"))

earn = hours * rate

print("Your weekly earn is: ", earn)
