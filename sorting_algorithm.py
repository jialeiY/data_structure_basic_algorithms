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
