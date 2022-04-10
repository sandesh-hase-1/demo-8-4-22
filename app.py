def fun1(input1:str):
    print("input1 is: ",input1)

fun1("Git tutorial chapter 1")

def fun2(input:str):
    lst=["a","i","e","o","u"]
    lst_final=[]
    [lst_final.append(char) for char in input if char in lst]
    return lst_final

result=fun2("Last_character")
print(result)
