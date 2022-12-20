# Regex using Python

import re

## Metacharacter

## search and findall function

str1 = "I am an Engineering student in Netaji Subhas University of Technology in Delhi."
str2 = "My email id is saibal123@gmail.com"
str3 = "I love to code in python but now focusing on C++ and Java"
str4 = "I love to solve problems using ML and DL and ofc using Logic."
str5 = "abc, aba, aca, acba, abca, abcbca, abbbbcccca, aaa, abbcaa, bbb, ccc, acb, cbc, cac, bac, cab"


match = re.search(r'@', str2)
findall = re.findall(r'c', str4)
print(match)


print(findall)match = re.search(r'a', str1)
print(match)


###matching special/meta character

match1 = re.search(r'.', str2)  ## treating it as meta character, but we want to know the location of '.' in gmail.com!
match2 = re.search(r'\.', str2)
print("Match1", match1)
print("Match2", match2)


## matching character class or set of character

match = re.search(r"[abc]", str5)
findall = re.findall(r"[abc]", str5)
print(match)
print(findall)


## matching character at the begining of the string

match1 = re.search(r"^abc", str5)
match2 = re.search(r"^acc", str5)
match3 = re.search(r"^my", str2)  #case sensitive
print(match1)
print(match2)
print(match3)



## matching character at the ending of the string

match1 = re.search(r"com$", str2)
match2 = re.search(r"Delhi.$", str1)
match3 = re.search(r"cab", str5)
findall = re.findall(r"cab", str5)



# print(match1)
# print(match2)
# print(match3)
# print(findall)


## method?attricutes and purpose
print(match1.group())
print(match2.span())
print(match3.start(), match3.end())




## matching character using '.'

findall1 = re.findall(r"c.c", str5)   
"""whenever it matches with anything, 
like 'c.c' means anything can be present in between two c, like for example cac, cbc, cccc, czzzcc.. etc"""

findall2 = re.findall(r"a.a", str5)

print(findall1)
print(findall2)



## matching character using OR operator

# findall = re.findall(r"bbb|b.b|^a", str5)

match = re.search(r"bbb|^a", str5) ## will find the matching position

# print(findall)
print(match)




## matching character using '?' operator

"""'?' id for zero or one occurance"""

f = re.findall(r"ab?c?a", str5)

print(f)


## matching character using '*' operator

"""'*' is used for matching, any number of occurance i.e. from 0 to ♾️ """

f = re.findall(r"ab*c*a", str5)

print(f)




## matching character using '+' operator

"""'+' is used for matching, positive number of occurance i.e. from 1 to ♾️ """

f = re.findall(r"ab+c+a", str5)
f_ = re.findall(r"ac+b*c*a", str5)


# print(f)
print(f_)



## matching character using '{}' operator

"""'{}' is used for matching the part of the string, where the pattern occurs for specified number of times"""

f = re.findall(r"abc{0,4}", str5) # no of times 'c' can be present for 0 and 4 times 
f_ = re.findall(r"a+b+c{0,2}", str5) # pattern means 'a' and 'b' should be present but presence of 'c' not necessary

print(f)
print(f_)



## matching character using '()' metacharacter

"""'()' is used for matching a specific string"""

f = re.findall(r"(a|b)bc", str5)   ## starting with either of a or b and bc should be present at the end
f_ = re.findall(r"(a|b)b*c*", str5)   ## starting with either of a or b and and no of b and c can be present after that

print(f)
print(f_)


