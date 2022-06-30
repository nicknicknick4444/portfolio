def make_lists(bure):
    bure_num = [(index, i)[1] for index, i in enumerate(bure) if index % 2 == 0]
    bure_sign = [(index, i)[1] for index, i in enumerate(bure[:-1]) if index % 2 == 1]
    return bure_num, bure_sign

def calcy(bure):
    bure_num, bure_sign = make_lists(bure)
    total = bure_num.pop(0)
    for index, i in enumerate(range(len(bure_num))):
        pair = [str(total), bure_sign[index], bure_num[index]]
        total = eval("".join(pair))
    return total

def main(bure):
    total = calcy(bure)
    return total
    
if __name__ == "__main__":
    main(bure)
