def common_elements(list1,list2):
    common = []
    for ele1 in list1:
        for ele2 in list2:
            if ele1 == ele2:
                common.append(ele1)
    return common


def total(x):
    n = (input("Enter a integer from 0 to 9"))
    if n.isdigit() and int(n) > -1 and int(n) < 10:
        n = int(n) + x
        print(n)
    else:
        print("i tell u put integer from 0 to 9 already right?\n can put integer anot?")

list1 = [1,4,5,3,6,8]
list2 = [11,5,16,3,8] # Change the lists here for your test cases
total(len(common_elements(list1,list2)))#why you use len
