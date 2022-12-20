## Sets

------------------


1.  [0-9] -----> matches any number between 0 and 9

2.  [a-Z] -----> matches any character in small 'a' to capital 'Z'(not a good practice)

3.  [^a-n] ----> Do not match any character between small 'a' and 'n'

4.  [0-8][0-9] ----> matches any number between 00 to 89



string = 'Gmail ID is goglex1029@gmail.com'


re.search(r'[0-9]', string)

re.findall(r'[0-9]', string)

re.search(r'[0-9][0-9][0-9][0-9]', string)

re.search(r'[a-m]', string)

re.search(r'[A-Z]', string)

re.search(r'[A-Z][a-z]', string)

re.search(r'[A-Z][a-z]+', string)


