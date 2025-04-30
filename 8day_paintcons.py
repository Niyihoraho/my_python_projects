

def paint(height,width):
    coverage=5
    Area_of_One_Unit=height*width
    num_cons=round(Area_of_One_Unit/coverage)
    return f"Number of cons: {num_cons}"

test_h=int(input("enter the height: "))
test_w=int(input("enter the with: "))
result=paint(test_h,test_w)
print(result)

   