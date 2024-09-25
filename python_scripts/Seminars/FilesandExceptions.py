f = open("testfile","w")
f.write("Test write to file.")
f.write(" Second test.")
f.close()

f = open("testfile","r")
s = f.read()
f.close()

print(s)
f = open("testfile","w")
f.write("This will delete what was written")
f.write(" earlier in the script.")
f.close()

f = open("testfile","r")
d = f.read()
print(d)
f.close()

f = open("testfile","w")
f.write(f"{d} But this way, we keep the old string as well as add a new one.")
f.close()

f = open("testfile","r")
e = f.read()
print(e)
f.close()

def copyFile(oFile, nFile):
    f1 = open(oFile, "r")
    f2 = open(nFile, "w")
    while True:
        text = f1.read(50)
        if text == "":
            break
        f2.write(text)
    # copyFile(oFile, nFile + 1) dont run this lol

    f1.close()
    f2.close()

copyFile("testfile", "copiedfile")