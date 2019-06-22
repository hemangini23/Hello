import random
pattern = "1234567890"
len = 4
otp = "".join(random.sample(pattern,len))
print (otp)