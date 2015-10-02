def biggest_of_2(var1,var2):
    res = None
    if var1 > var2:
        res = var1
    else:
        res = var2
    return res

def biggest_of_4(var1,var2,var3,var4):
    big_12 = biggest_of_2(var1,var2)
    big_123 = biggest_of_2(big_12,var3)
    biggest = biggest_of_2(big_123,var4)
    return biggest

def smallest_of_2(var1,var2):
    if var1>var2:
        return var2
    return var1

def smallest_of_4(var1,var2,var3,var4):
    small_12 = smallest_of_2(var1,var2)
    small_123=smallest_of_2(small_12, var3)
    small_1234=smallest_of_2(small_123, var4)
    return small_1234

def biggest(l):
    big = None
    for elm in l:
        big = biggest_of_2(big, elm)
    return big

def smallest(lst):
    small=None
    for elm in lst:
        if small == None:
            small = elm
        else:
            small = smallest_of_2(small, elm)
    return small

def list_sum(lst):
    sum_res = 0
    for elm in lst:
        sum_res = sum_res + elm
    return sum_res

def num_elms(lst):
    counter = 0
    for elm in lst:
        counter = counter + 1.0
    return counter

def mean(lst):
    mean_res = list_sum(lst)/num_elms(lst)
    return mean_res
