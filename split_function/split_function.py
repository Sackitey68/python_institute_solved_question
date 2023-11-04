def mysplit(strng):
    #
    A = ""
    B = []
    for i in strng:
        if i != " ":
            A += i
        elif A != "":
            B.append(A)
            A = ""
    # Append last word
    if A != "":
        B.append(A)

    return(B)
    #


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
