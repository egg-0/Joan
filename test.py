import numpy as np

def sampler(size_team, target_score, bottom_tier, top_tier):
    # https://stackoverflow.com/questions/40231094/generate-n-positive-integers-within-a-range-adding-up-to-a-total-in-python

    range_list = [bottom_tier,top_tier]

    assert range_list[0]<range_list[1], "Range should be a list, the first element of which is smaller than the second"
    arr = np.random.rand(size_team)
    sum_arr = sum(arr)

    new_arr = np.array([int((item/sum_arr) * target_score) if (int((item / sum_arr) * target_score) > range_list[0] and int((item / sum_arr) * target_score) < range_list[1]) \
                            else np.random.choice(range(range_list[0],range_list[1]+1)) for item in arr])
    difference = sum(new_arr) - target_score
    while difference != 0:
        if difference < 0 :
                for idx in np.random.choice(range(len(new_arr)),abs(difference)):
                    if new_arr[idx] != range_list[1] :
                        new_arr[idx] +=  1

        if difference > 0:
                for idx in np.random.choice(range(len(new_arr)), abs(difference)):
                    if new_arr[idx] != 0 and new_arr[idx] != range_list[0] :
                        new_arr[idx] -= 1
        difference = sum(new_arr) - target_score
    return new_arr

new_arr = sampler(4,8,1,5)
print("Generated random array is :")
print(new_arr)
print("Length of array:", len(new_arr))
print("Max of array: ", max(new_arr))
print("min of array: ", min(new_arr))
print("and it sums up to %d" %sum(new_arr))