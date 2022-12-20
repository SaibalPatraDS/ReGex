## Time Format Validation

-----------------------

<h3>Task 3 : Time Format Validation.</h3>

----------------------

Write a format checker that determines whether the input is worth processing further with your backend application.


* Time Format must be valid and in between 00:00 to 23:59






inputs = ['10:26', '25:36', '44:56', '99:99', '100:32', '45:999',  '01:25']

regex = '[0-9]{2}:[0-9]{2}' ## max numerical that can be matched 99:99 and minimum 00:00

print(re.fullmatch(regex, inputs[0]))
print(re.fullmatch(regex, '00:00'))
print(re.fullmatch(regex, '99:99'))
print(re.fullmatch(regex, '100:99'))


## list comprehension

[re.fullmatch(regex, x) for x in inputs]

Project Work

---------------------

max_time = '23:59'
min_time = '00:00'

regex = '([01][0-9]|2[0-3]):([0-5][0-9])'  # max numerical can be matched 23:59 and minimum 00:00

def timematch(regex, time):
    if re.fullmatch(regex, time):
        print("Time is saved")
    else:
        print("Invalid Time")
    return time    

## dry run

timematch(regex, max_time), timematch(regex, min_time)

## testing

time = ['10:26', '15:59', '23:60', '10:10', '17:54', '21:45', '33:45', '12:12']

#testing results

for x in time:
    timematch(regex, x)
    print("Time is:", x)
    print('\n')
