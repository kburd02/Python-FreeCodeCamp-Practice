#KA'Pri Burden
#06/10/2022

print(2**3)

#use a for loop to create an exponent funciton

#multiply the base num by itself as many times as the pow num specifies

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result* base_num #keeps going through for the number pf base number
    return result
#keeps looping through the amount of instances given

print(raise_to_power(2,4))

