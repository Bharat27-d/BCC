phy = 50
chem = 60
math = 70
print("Physics={} Chemistry={} Mathematics={}".format(phy, chem, math))
print("Physics={0} Chemistry={1} Mathematics={2}".format(phy, chem, math))
print("Physics={x} Chemistry={y} Mathematics={z}".format(x=phy, y=chem, z=math))
total = phy + chem + math
print("Total Marks",f"{total}")
print("Roll No.","7".zfill(4))