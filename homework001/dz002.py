# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
import random
x = random.randrange (2)
y = random.randrange (2)
z = random.randrange (2)
print(not((x) or (y) or (z)) == (not((x) and not(y) and not(z)))) 
print (x, y, z)