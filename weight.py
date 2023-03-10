#This function measures the weight of the waste according to wastetype
#The weight of the waste is in kgs

def measureWeight(wasteType):
    if wasteType == 1:
        weight = int(input("Please enter the weight of the organic waste (in kg): "))
    elif wasteType == 2:
        weight = int(input("Please enter the weight of the plastic waste (in kg): "))
    elif wasteType == 3:
        weight = int(input("Please enter the weight of the e-waste (in kg): "))
    elif wasteType == 4:
        weight = int(input("Please enter the weight of the glassware waste (in kg): "))
    else:
        weight = 0
    return weight

print(measureWeight(1)) # Prompts user to enter weight of organic waste
def measureWeight(wasteType):
    if wasteType == 1:
        weight = int(input("Please enter the weight of the organic waste (in kg): "))
    elif wasteType == 2:
        weight = int(input("Please enter the weight of the plastic waste (in kg): "))
    elif wasteType == 3:
        weight = int(input("Please enter the weight of the e-waste (in kg): "))
    elif wasteType == 4:
        weight = int(input("Please enter the weight of the glassware waste (in kg): "))
    else:
        weight = 0
    return weight

print(measureWeight(1)) # Prompts user to enter weight of organic waste

