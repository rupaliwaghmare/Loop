# User se ek n naam ke variable mein ek integer input lo.
#  Fir user se utni baar input baar ek integer ko input lo jitni n ki value hai. 
#  Finally unn saare integer jinko user ne input kara hai, sum karke print karo.
#   Example: Jaise agar n mein user ne ki 6 daala hai toh 6 baar input lo. n ki 
#   value Kitni baar input lein? waali line mein input li gai hai. Sum 179 isliye 
#   likha hai kyunki 10+1+56+89+11+12 ka result 179 hai. Example: Jaise agar user 
#   ne n ki value 10 di hai toh program kuch aisa chalega. Aap koi aur numbers bhi de 
#   sakte ho input mein. Sum 396 isliye hai kyunki 11+7+14+76+21+34+86+5+78+64 ka result
#    396 hai.
# Edit on Github


counter=0
sum=0
n=int(input("enter the number"))
while counter<n:
    a=int(input("enter a number"))
    sum=sum+a 
    counter=counter+1
print(sum)