def flat(l):
    return[item for sublist in l for item in sublist]
l=[[1,2,3],[4,5,6],[7,8,9]]
flatten_list=flat(l)
print(flatten_list)
