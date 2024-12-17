def histogram(str):
    dict = {}
    str = str.strip(' .')
    for i in str:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict

def histogram2(str):
    lst = []
    str = str.strip(' .')
    for i in str:
        if i in lst:
            index = lst.index(i)
            lst[index+1] = lst[index+1]+1
        else:
            lst.append(i)
            lst.append(1)
    return lst

def printHist(hist):
    print(f" Bokstav | Antal ")
    if isinstance(hist, dict):
        for i in hist:
            num = hist[i]
            print(f" {i} | {num} ")
    elif isinstance(hist, list):
        for i in hist:
            if isinstance(i, str):
                index = hist.index(i)
                num = hist[index + 1]
                print(f" {i} | {num} ")
            else:
                pass

s = "VINGUMMIN"
printHist(histogram2(s))