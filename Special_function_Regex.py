## Special Sequences


-----------------------------------

 1. '\d' -----> matches any numeric character i.e. [0-9]

 2. '\w' -----> matches any alphanumeric character i.e. [a-Z][0-9]




re.search(r'\d', "abc!@#2005@gmail.com")  #return the first occurace place of the numeric digit


re.search(r'\d+', "abc!@#2005@gmail.com")  # return the position of all numeric digits on one go


re.search(r'\d+', "abc!@#2005xyz123@gmail.com") # didn't return all position of numeric digits


re.search(r'\d\d\d\d', "abc!@#2005@gmail.com") # can be used to return the pos of numeric digits


re.search(r'\d\d\d\d', "abc!@#2005xyz123@gmail.com") # didn't return all position of numeric digits


re.search(r'\d+\D+\d+', "abc!@#2005xyz123@gmail.com")


re.findall(r'\d', "abc!@#2005xyz123@gmail.com")
