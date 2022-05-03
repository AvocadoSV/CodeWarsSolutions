def bingo(array): 
    count = 0
    l = [2,7,9,14,15]
    for i in l:
        if i in array: count +=1
    if count == 5 : return "WIN"
    else: return "LOSE"
