# Problem 1: Object Types (Weight 2).
# Consider the number 17. Construct multiple variables
# (y1, y2, y3, and y4) in Python that represent the number 17 in the various forms of objects
# (integer, float, string, and Boolean, respectively).
# Hint: For creation of the Boolean, set a value for 17 to be compared against another number.
# 1. Print the value of y1, y2, y3, and y4 and their types
# (Hint: you can use function type() to get a type of an object or variable).

y = 17
print('Setting x =', y)
#y1 = integer
y1 = int(y)

#y2 = float
y2 = float(y)

#y3 = string
y3 = str(y)

#y4 = Boolean
y4 = bool(17)
print(y4 == 18)

print(type(y1))
print(type(y2))
print(type(y3))
print(type(y4))

#2. Use y1, y2, or y3 to create a variable named text such that print(text) prints 'The value of x is 17.'

text = ('The value of x is', y1)
print(text)

echo "# HPM573S18_Pokutnaya_HW1"
git init
git add README.md
git commit
git remote add origin https://github.com/dasha-pokutnaya/HPM573S18_Pokutnaya_HW1.git
git push
