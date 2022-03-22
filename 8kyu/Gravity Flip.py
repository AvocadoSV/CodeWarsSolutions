def flip(d, a):
    if d == 'R':
        a.sort(reverse = False)
        return a
    else:
        a.sort(reverse = True)
        return a
