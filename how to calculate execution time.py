from time import time
start = time()
strs = "Calculate Execution Time"
word = strs.split()
a = " "
for i in word:
    a = a+str(i[0]).upper()
print(a)
end = time()
exection_time = end - start
print("Execution Time",exection_time)