from math import ceil
# Read an integer:
a = int(input("Gr. a: "))
b = int(input("Gr. b: "))
c = int(input("Gr. c: "))
# Math 
#   ceil = возвращает предельное значение х, т.е. наименьшее целое число не меньше, чем х

classa=ceil(a/2)
classb=ceil(b/2)
classc=ceil(c/2)
classall=(classa+classb+classc)

print("%s" % classall)