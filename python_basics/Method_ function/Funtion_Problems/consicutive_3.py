def has22(nums):
    for x in range(0,len(nums)-1):
        if nums[x] == 2 and nums[x+1] == 2:
            return True
        else:
            return False 
print(has22([2,2,1]))

def has_33(nums):
    for i in range(0, len(nums)-1):
      
        # nicer looking alternative in commented code
        #if nums[i] == 3 and nums[i+1] == 3:
    
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False
print(has_33([3,3,1]))