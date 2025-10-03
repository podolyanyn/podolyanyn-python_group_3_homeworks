def in_range(start, end, step=1):

    if step == 0:
        raise ValueError("in_range() arg 3 must not be zero")

    curr = start
    if step > 0:
        while curr < end:
            yield curr
            curr += step
    else:
        while curr > end:
            yield curr
            curr += step

if __name__ == "__main__":
    print(list(in_range(1, 18, 2)))
    print(list(in_range(19, 0, -3)))
