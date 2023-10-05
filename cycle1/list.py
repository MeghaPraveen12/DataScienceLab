print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

List1 = [7, 5, 21, 18, 8]
List2 = [9, 15, 6, 1,11]
# printing original lists
print ("list1 : " + str(List1))
print ("list2 : " + str(List2))
newList = []
for n in range(0, len(List1)):
   newList.append(List1[n] + List2[n])
print(newList)
