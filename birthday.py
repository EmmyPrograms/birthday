from datetime import date
import time

print("Welcome.... :)")
name = input("What is your name.")

month = input("Enter your birth month: ")
day = input("Enter your birth day: ")
year = input("Enter your birth year ")

print("YOUR BIRTHDAY ISSSSSS : ", month, day, year)
for i in range(3):
    print("Happy birthday. To you.")
    time.sleep(1)

print("Happy birthday dear.", name)

td = str(date.today())
td_arr = td.split("-")
cy = td_arr[0]
cm = td_arr[1]
cd = td_arr[2]
print(type(cy), type(cm), type(cd))
print("Wyatt was here, ooga booga")
print("I wanted to print jinx here but I couldn't get it to work lol")
