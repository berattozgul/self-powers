def self_power(a):
    x=0
    for i in range(1,a):
        x=i**i+x
    return x
print(self_power(1001)%10000000000)
