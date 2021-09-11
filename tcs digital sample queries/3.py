s=input()
rs=s[0]
la=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ua=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','^','&','*','(',')','{','}','[',']',':','"',',','.','/','>','<','?','~']
if rs in la:
    print("lower alphabet")
elif rs in ua:
    print("UPPER ALPHABET")
elif rs in symbols:
    print("Symbol")
else:
    print("Number")