## Question(?) character


*  Question Mark(?) is the option regex meaning 0 or 1 occurance

*  Question Mark(?) can also be used in combination with other special characters and means something else. 

*  asterisk, * means 0 or more occurance of the current element. 

*  By default, the engine returns more occurance(greedy), if you want to force the 0 occurance to be returned, after asterisk, * use question mark ?



string = 'amncghrbjab@nksnk'

re.findall('am.*', string)  # '.' matches any character except new line

## to get only the specified character as an output, use question mark after asterisk, *

re.findall('am.*?', string)

## new example

s = 'peter piper picked a peck of pickled peppers'

re.findall('p.*e.*r', s)   # 'p.*e.*r' means starts from 'p' then any character utill 'e' occurs and then all character except new line and finally end with 'r' occurs. 

## we want to get outputs like 'peter', 'piper' and rest in a single output

re.findall('p.*?e.*?r', s)
