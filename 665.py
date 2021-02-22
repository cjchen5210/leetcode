def checkPossibility(nums):
        #res = False
        count = 0
        index = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                index = i
        print(index)
        if count > 1:
            return False
        elif count == 0:
            return True
        elif count == 1:
            if index == 0:
                nums[index] = nums[index+1]
            elif nums[index-1] > nums[index+1]:
                nums[index+1] = nums[index]
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
        if count == 0:
            return True
        else:
            return False
nums = [-1,4,2,3]
print(checkPossibility(nums))

