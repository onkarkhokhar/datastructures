a = [1,2,3,4,5]
sum_segment_tree = [0 for i in range(4*len(a))]
min_segment_tree = [float('inf') for i in range(4*len(a))]
def construct_sum_segment_tree(segment_tree,a,tree_index,low,high):

    if low >= high:
        segment_tree[tree_index] = a[high]
        return

    mid = (low + high)//2
    construct_sum_segment_tree(segment_tree,a,2*tree_index+1,low,mid)
    construct_sum_segment_tree(segment_tree,a,2*tree_index+2,mid+1,high)

    segment_tree[tree_index] = segment_tree[2*tree_index+1] + segment_tree[2*tree_index+2]


def construct_min_segment_tree(segment_tree,a,tree_index,low,high):

    if low >= high:
        segment_tree[tree_index] = a[high]
        return

    mid = (low + high)//2
    construct_min_segment_tree(segment_tree,a,2*tree_index+1,low,mid)
    construct_min_segment_tree(segment_tree,a,2*tree_index+2,mid+1,high)

    segment_tree[tree_index] = min(segment_tree[2*tree_index+1],segment_tree[2*tree_index+2])

def sum_query(segment_tree,tree_index,low,high,i,j):
    #full over lap
    if i <= low and j >= high:
        return segment_tree[tree_index]
    #no over lap
    if low > j or high < i:
        return 0

    #partial overlap
    mid = (low + high) // 2
    # go to left and right side now to find over laps
    # below if condition is to reduce some recursion calls
    if i > mid:
        return sum_query(segment_tree, 2*tree_index+2,mid+1,high,i,j)
    elif j <= mid:
        return sum_query(segment_tree, 2*tree_index+1,low,mid,i,j)

    left_query = sum_query(segment_tree,2*tree_index +1,low,mid,i,j)
    right_query = sum_query(segment_tree,2*tree_index +2,mid+1,high,i,j)

    return left_query + right_query


def min_query(segment_tree,tree_index,low,high,i,j):
    #full over lap
    if i <= low and j >= high:
        return segment_tree[tree_index]
    #no over lap
    if low > j or high < i:
        return float('inf')

    #partial overlap
    mid = (low + high) // 2
    # go to left and right side now to find over laps
    # below if condition is to reduce some recursion calls
    if i > mid:
        return min_query(segment_tree, 2*tree_index+2,mid+1,high,i,j)
    elif j <= mid:
        return min_query(segment_tree, 2*tree_index+1,low,mid,i,j)

    left_query = min_query(segment_tree,2*tree_index +1,low,mid,i,j)
    right_query = min_query(segment_tree,2*tree_index +2,mid+1,high,i,j)

    return min(left_query,right_query)

def update_sum_segment_tree(segment_tree,val,arr_index,low,high,tree_index):
    if low == high:
        segment_tree[tree_index] = val
        return
    mid = (high + low ) // 2

    if arr_index > mid:
        update_sum_segment_tree(segment_tree,val,arr_index,mid+1,high,2*tree_index+2)
    else:
        update_sum_segment_tree(segment_tree,val,arr_index,low,mid,2*tree_index +1)

    segment_tree[tree_index] = segment_tree[2*tree_index +2] + segment_tree[2*tree_index +1]


construct_sum_segment_tree(sum_segment_tree,a,0,0,len(a)-1)
construct_min_segment_tree(min_segment_tree,a,0,0,len(a)-1)

update_sum_segment_tree(sum_segment_tree,10,3,0,len(a)-1,0)
# print(min_query(min_segment_tree,0,0,len(a)-1,2,4))
# print(min_segment_tree)

print( sum_query(sum_segment_tree,0,0,len(a)-1,2,3))
print( sum_segment_tree)
