def sum_seq(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list,tuple)):
            result += sum_seq(item)
        else:
            result += item

    return result


seq = [1, 2, [1, 2], [2, 1, 8]]
print(seq)
print("suma: {}".format(sum_seq(seq)))