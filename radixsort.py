def radix_sort(u):
    radix = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        buckets = [list() for _ in range(radix)]
        for h in u:
            tmp = h // placement
            buckets[tmp % radix].append(h)
            if max_length and tmp > 0:
                max_length = False

        a = 0
        for b in range(radix):
            buck = buckets[b]
            for h in buck:
                u[a] = h
                a += 1
        # move to next digit
        placement *= radix
    return u
