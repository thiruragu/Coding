'''Micorsoft Interview QUestion - Count distinct elements in every window of size k


Given an array of size n and an integer k, return the count of distinct numbers in all windows of size k.
Example:

Input: arr[] = {1, 2, 1, 3, 4, 2, 3};
       k = 4
Output: 3 4 4 3

Explanation:
First window is {1, 2, 1, 3}, count of distinct numbers is 3
Second window is {2, 1, 3, 4} count of distinct numbers is 4
Third window is {1, 3, 4, 2} count of distinct numbers is 4
Fourth window is {3, 4, 2, 3} count of distinct numbers is 3

Input: arr[] = {1, 2, 4, 4};
       k = 2
Output: 2 2 1

Explanation:
First window is {1, 2}, count of distinct numbers is 2
First window is {2, 4}, count of distinct numbers is 2
First window is {4, 4}, count of distinct numbers is 1


'''

import time

# def unique(list):
#     dict = {}
#     count = 0
#     for i in list:
#         if i not in dict.keys():
#             dict[i] = i
#             count += 1
#     return count

ls = list(map(int, input("Enter numbers (with space separated) = ").strip().split()))
k = int(input("Window size = "))

tic = time.time()

i = 0

while True:
    if i + k > len(ls):
        print("\nFinished")
        break
    ans = len(set(ls[i:i+k]))
    # ans = unique(ls[i:i + k])
    print(ans, end=" ")
    i += 1

toc = time.time()

print(int(round((toc-tic) * 1000000)),"Sec")