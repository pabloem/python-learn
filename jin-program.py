def smallest(var1, var2):
    if var1>var2:
        return var2
    return var1

def smallest_in_list(lst):
    sm = None
    for elm in lst:
        if sm == None:
            sm = elm
        else:
            sm = smallest(sm,elm)
    return sm

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def mean(somelist) :
    mean_res = sum(somelist)/len(somelist)
    return mean_res
