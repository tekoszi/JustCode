def removeShits(wyraz):
    shits = [
        " for ",
        " 2016 ",

    ]
    for shit in shits:
        if shit in wyraz:
            return wyraz[:wyraz.index(str(shit))+len(shit)]

print(removeShits("Microsoft for 203122313"))
print(removeShits("Microsoft  2016  203122313"))