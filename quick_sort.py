'''
Worst case :θ(n^2) , When the list is sorted ( T(n)=T(n-1)+n-1 )
zamani ke masale be 2 zir masale ba andaze haye 1 , n-1 taghsim shavad

'''
inp_str = input("Enter numbers:")
lst=[int(i) for i in inp_str.split(' ') ]
####################################################
def partition(lst,low,high):
    pivot=lst[low]
    i=low
    for j in range(i+1,high+1):
        if lst[j]<pivot:
            i+=1
            lst[i],lst[j]=lst[j],lst[i]
    lst[i],lst[low]=lst[low],lst[i]
    return i
    
def quick_sort(lst,low ,high):
    if len(lst)==1:
        return lst
    if low<high:    
        pivot_point=partition(lst,low,high)
        return quick_sort(lst,low,pivot_point-1)
        return quick_sort(lst,pivot_point+1,high)
#####################################################
quick_sort(lst,0,len(lst)-1)
print(lst)