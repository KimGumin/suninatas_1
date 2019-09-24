str = input("str ")
if(str != ""):
    result = str.replace("a", "aad")
    result = result.replace("i", "in")
    result1 = result[1:3]
    result2 = result[3:9]
    result = result1 + result2
    print(result)
