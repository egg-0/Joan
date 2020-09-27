# https://stackoverflow.com/questions/39192777/how-to-split-a-list-into-n-groups-in-all-possible-combinations-of-group-length-a

import more_itertools

A = [1,2,3,4]

print(list(more_itertools.set_partitions(A, k=2)))