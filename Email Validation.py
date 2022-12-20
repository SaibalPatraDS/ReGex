## Email Validation


-------------------

inputs = ['google123@gmail.com', 'mahima_123@gmail.com', 'pooja_y091@gmail.com', 'benes_james@outlook.com', 'ed_start@iitbhu.ac.in']

regex = '(\w|\.|\_|\-)+[@][a-z]+[.]\w{2,3}[.]?[a-z]?[a-z]?$'

## two parts of the regex, 
# """ist part before '@' and second part after '@'
# for ist part, any number of alphanumeric character can exists with that dot[.], underscore[_] and hyphen[-] 
# and for second part, any numer of alphabets can occur, then a dot[.] next to it again {2,3} alphabets and then optional dot[.] and optional alphabets."""

## testing

[re.fullmatch(regex, x) for x in inputs]

### Username Validation


*  Allowing aplhanumeric character, underscore(_) and dor[.] only

inputs = ['rakima_123', 'huges_salt', 'peterbrake.123', 'jeus@1230', 'navin._56']

regex = '^[a-zA-Z0-9._]+$'

# regex = '^[.]?\w+[.}?$'   #---> this will not work cause \w doesn't allow dot[.] and all combinations can't be covered.


## anynumber of aplhanumeric character and special characters like dot[.] and underscore[_] are allowed. 

[re.fullmatch(regex, x) for x in inputs]
