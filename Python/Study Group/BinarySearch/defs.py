class BinarySearch():
    def b_search(self,list1,left,right,val):
        while left <= right:
            mid = left + (right - left) // 2
            if list1[mid] == val:
                return mid
            elif list1[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        return -1
if __name__ == '__main__':
    obj=BinarySearch()
    lis=input("Enter the List items: ")
    val=input("Enter the element to find: ")
    finding = obj.b_search(lis, 0, len(lis) - 1, val)
    if finding != -1:
        print("Element is present at index % d" % finding)
    else:
        print("Element is not present in array")