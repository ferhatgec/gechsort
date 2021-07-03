# MIT License
#
# Copyright (c) 2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
# Gechsort (library)
#
# github.com/ferhatgec/gechsort

def gech(elements):
    from itertools import permutations

    permutations_of = list(permutations(elements))
    data = []
    sort_it = elements.sort() # Huh
    get_min = min(elements)
    get_mid = elements[int(len(elements) / 2)]
    get_max = max(elements)

    if sort_it == None:
        sort_it = elements

    for arr in permutations_of:
        if arr[0] == get_min and arr[-1] == get_max and arr[int(len(arr) / 2)] == get_mid:
            data.append(arr)

    for ok in data:
        ok = list(ok)
        if ok == sort_it:
            return ok

# q = [2, 0, 0, 5, 0, 2, 0, 5]

# print(gech(q))