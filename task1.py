f2 = open("output.txt", 'w+')
f1 = open("input.txt", 'r')
f2.writelines(f1.read())
f2.close()
f1.close()
f2 = open("output.txt","a")
f2.write(" today")
f2.close()
f2 = open("output.txt", 'r+')
print(f2.read())
f2.close()