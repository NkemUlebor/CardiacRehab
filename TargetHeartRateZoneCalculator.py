# For my cardiac rehab, we use 40-85% of intensity on a stress test to create a target HRR.
# Feel free to use it to match your cardiac rehab's procedures. :) - Nkem


#Prompt the user for their resting heart rate on their stress test
while True:
    try:
        resting_hr = int(input("Enter your resting heart rate (bpm): "))
        if resting_hr < 30:
            print("Please enter the correct heart rate.")
            continue
        break
    except ValueError:
        print("Please enter a numerical value.")

#Prompt the user for their maximum heart rate on their stress test
while True:
    try:
        maximum_hr = int(input("What was your maximal heart rate?: "))
        if maximum_hr < resting_hr:
            print("Please enter the correct heart rate.")
            continue
        break
    except ValueError:
        print("Please enter a numerical value.")


#Calculate the Heart Rate Reserve
heart_rate_reserve = maximum_hr - resting_hr

#Calculate the lower and higher range targets
lower_range_target = round(heart_rate_reserve * 0.4 + resting_hr)
higher_range_target = round(heart_rate_reserve * 0.85 + resting_hr)


#Display the Target Heart Rate Range
print(f"Your target heart rate range is {lower_range_target} - {higher_range_target} bpm")
