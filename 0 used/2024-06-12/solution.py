def req(arr1,arr2):
    if len(arr1) == 1:
        if arr2[0] == "": return 0
        return 4 if arr1[0] == arr2[0] else -1
    if arr2[0] == "": return 0 + req(arr1[1:], arr2[1:])
    return 4 + req(arr1[1:], arr2[1:]) if arr1[0] == arr2[0] else -1 + req(arr1[1:], arr2[1:])
    
def check_exam(arr1,arr2):
    result = req(arr1,arr2)
    return result if result >= 0 else 0
  
