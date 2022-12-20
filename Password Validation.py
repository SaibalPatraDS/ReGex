## Password Valdation with ReGex

--------------------------

<h3>Task 1 : Need to write a regex that will validate a password to make sure it meets the following criteria. </h3>



1.   At least 8 characters
2.   upper case characters: A-Z
3.   lowercase characters: a-z
4.   numbers:0-9
5.   any of the special characters:@#$%^&+=

Letters/numbers/special characters are optional.



regex = '[A-Za-z0-9@#$^&+=]{8,}'

## {8,} will make sure no of characters are greater of equal to 8
## [A-Z] to make sure Capital letters are included
## [a-z] to make sure lower case characters are included
## [0-9] to make sure numeric characters are included
## and everyone is merge as letters, numbers and special characters are optional

password = input("Enter Password:")

def setpassword(regex, password):
    if re.fullmatch(regex, password):
        print("Congratulation!Your password is set.")
    else:
        print("Please enter correcr password") 
    # print("Your password")
    return password       

setpassword(regex, password)



<h3>Task 2 : Need to write a regex that will validate a password to make sure it meets the following criteria. </h3>



1.   At least 6 characters
2.   upper case characters: A-Z
3.   lowercase characters: a-z
4.   numbers:0-9
5.   any of the special characters:@#$%^&+=

Letters/numbers/special characters are must.



## creating regex

regex1 = '(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{6,}'

## positive lookahead, used to match atleast the condition
## pattern --> (?=.*[here, write the pattern])

setpassword(regex, password)

