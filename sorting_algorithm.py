def bubble_sort(the_list):
    for k in xrange(1,len(the_list)):
        for i in xrange(len(the_list)-k):
            if the_list[i]>the_list[i+1]:
                the_list[i],the_list[i+1]=the_list[i+1],the_list[i]
        print the_list
    return the_list
#bubble_sort([19, 1, 9, 7, 3, 10, 13, 15, 8, 12])

def selection_sort(the_list):
    for k in xrange(len(the_list)-1):
        the_max=None
        the_max_pos=None        
        for i in xrange(len(the_list)-k):       
            if the_list[i]>the_max:
                the_max=the_list[i]
                the_max_pos=i
        the_list[-k-1],the_list[the_max_pos]=the_list[the_max_pos],the_list[-k-1]
        print the_list
    return the_list
#selection_sort([11, 7, 12, 14, 19, 1, 6, 18, 8, 20])

def insertion_sort(the_list):
    for k in xrange(1,len(the_list)):
        this_value=the_list[k]
        i=k-1
        while the_list[i]>this_value and i>=0:      
            the_list[i+1]=the_list[i]
            i-=1
        the_list[i+1]=this_value        
        print the_list
    return the_list
#insertion_sort([15, 5, 4, 18, 12, 19, 14, 10, 8, 20])

def merge_sort(the_list):
    def merge(lo,mid,hi):
        left=the_list[lo:mid+1]
        right=the_list[mid+1:hi+1]        
        i=j=0

        for k in xrange(lo,hi+1):
            if j>=len(right):
                the_list[k]=left[i]
                i+=1    
            elif i>=len(left):
                the_list[k]=right[j]
                j+=1
            elif left[i]<right[j]:
                the_list[k]=left[i]
                i+=1
            else:
                the_list[k]=right[j]
                j+=1
                
    def split(lo,hi):
        if lo<hi:
            mid=lo+(hi-lo)/2
            split(lo,mid)
            split(mid+1,hi)
            merge(lo,mid,hi)
            
    split(0,len(the_list)-1)
    print the_list
    return the_list
#merge_sort([21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40])

def shell_sort(the_list):
    l=len(the_list)    
    h=1
    while h<l/3:
        h=3*h+1
    while h>=1:
        for i in xrange(h,l):
            k=i-h
            this_value=the_list[i]
            while the_list[k]>this_value and k>=0:
                the_list[k+h]=the_list[k]
                k-=h
            the_list[k+h]=this_value
            print the_list 
        h/=3
    return the_list
#shell_sort([5, 16, 20, 12, 3, 8, 9, 17, 19, 7])

