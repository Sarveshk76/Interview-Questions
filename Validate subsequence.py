arr = [1,2,3,4,5,9,7,8]
seq = [3,8,9]

def validate_subseq(arr,seq):
    ind=[0]
    for i in seq:
        if i in arr:
            if arr.index(i)>=ind[-1]:
                ind.append(arr.index(i))
            else:
                return ('Wrong subseq')
    if len(ind)==len(seq)+1:
        return ('Correct subseq')

print(validate_subseq(arr,seq))