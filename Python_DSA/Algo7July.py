# var = [ 1 ,5 ,100 , 55, 44, 8, 9, 60, 100,110 ]

# element = 44

# def search(var, element):
#     # step 1 : sorted structure ? 
#     sorted_var = var.sort()
    
#     # step 2 : finfthe mid value : 
#     mid_index = len(sorted_var)//2
    
#     # step 3 : check the conditon: 
#     if sorted_var[mid_index] < element:
#         # this is to check for the right structure 
#         search(sorted_var[mid_index : ], element)
        
#     elif sorted_var[mid_index] > element:
#         # this is to check for the left structure 
#         search(sorted_var[:mid_index+1 ], element)
        
#     else : 
#         print(f'{element} found on the index {mid_index}' )
        
        
        
var = [ 111 ,501 ,100 , 515, 424, 899, 991, 605, 103,1104 ]

# output_var =[]
# for i in var:
#     count =0 
#     for j in str(i):
#         count += int(j)
#         if count>10:
#             for a in str(count):
#                 count =0
#                 count += int(a)
#     output_var.append(count)


out_var = []
for i in var:
    while num > 9:
        num = sum(int(digit) for digit in str(num))
        for a in str(num):
            num = 0
            num += int(a)
            
    out_var.append(num) 
    print(out_var)
    
