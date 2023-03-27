ice_cream: dict [str,int]={'chocolate':12,'vanilla':8,'strawberry':5}
#Adding
ice_cream["mint"]=3
print(ice_cream)

#Removing
ice_cream.pop("mint")
print(ice_cream)

#Accessing
print(f"Number of vanilla orders:{ice_cream['vanilla']}")

#Modifying
ice_cream["vanilla"]+=1
print(ice_cream)
print(f"Number of vanilla orders:{ice_cream['vanilla']}")

#Checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)