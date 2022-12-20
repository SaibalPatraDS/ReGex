## Execution and Word Replacement from Server Logs

------------------

**Problem 1** :    
Find a match that starts with 'crypto', then matches at the most 30 arbitary characters and match ends when the last word is 'coin'.



text1 = 'crypto-bot that is trading Bitcoin and other currencies.'

## regex making and finding the match

re.match('crypto(.{1,30})coin', text1)


Explanation --

Match starts with 'crypto' and ends with 'coin' in between anything can be there, only condition is that max length can 30. 
We will solve it by grouping things, (.{1,30}), dot[.] matches with anything except new line. 



**Problem 2**:

Find the occurances of dollar amounts with optional Regular Expressions decimal values. 



text2 = '''
If you invested $1 in the year 1801, you would have $18087791.41 today.
This is a 7.6967% return on investment. 
But if you only invested $0.25 in 1801, you would end up with $4521947.667'''

## regex making and finding the match

regex = "(\$[0-9]+(\.[0-9]*)?)"

amount = re.findall(regex, text2)

for i in amount:
    print("Decimal Amount", i[1])

Explanation --

Regex will start with dollar sign[\$], but dollar sign[\$] has another meaning in regex, so we will use bakslash(\) and same for decimal(.) and rest of the things any number of numeric characters, [0-9]+. To make sure regex to be not greddy, we will use question mark, '?' after decimal matching.



**Problem 3**:

Replace Alice Wonderland with 'Alice Doe' but do not replace occurances of 'Alice Wonderland' when you see single quotes.

text3 = '''
Alice Wonderland married John Doe.
The new name of former 'Alice Wonderland' is Alice Doe.
Alice Wonderland replaces her old name 'Wonderland' with her new name 'Doe'
Alice's sister Jane Wonderland still keeps her old name.'''

## Regex making and replacing the match

regex = "Alice Wonderland(?!')"   ## regex to be used

re.sub(regex, 'Alice Doe', text3)   # sub for replacing, regex -- > what to be replaced, next item with what to be replaced

Explanation --

Negative Lookahead, (?!the character want to avoid) .

Alice Wonderland will be replaced but if quotation occurs, no replacement.  

[Regex-Lookaronds](https://www.rexegg.com/regex-lookarounds.html)

