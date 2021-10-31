def multiple(number):
    if number>10: return int(number/10)
    else: return 0

def div(number):
    if number>10: return int(number%10)
    else: return number

n_p=5
k=5
ans=(pow(10,k-1)+1) * (multiple(n_p)+1)

if (k%2==0):
    ans+=int( ((div(n_p)-1)*11) * pow(10, ((k)/2)-1))
else:
    ans+=int( ((div(n_p)-1)*101) * pow(10, ((k+1)/2)-2))
print(ans)