# import cv2

# camera = cv2.VideoCapture(0)
# while camera.isOpened():
#     ret, frame = camera.read()

#     cv2.imshow("pop", frame)

#     if cv2.waitKey(1) & 0xFF == ord("1"):
#         break



# --- THE ARRAY (Python List) ---

# Di-Fan: We define the foundation (a list of 3 elements)
# Ren-He: The harmony of items sitting side-by-side in memory
my_array = ["Data1", "Data2", "Data3"]

# Tian-Yuan: Accessing the Origin (Index 0)
first_element = my_array[0] 

# Ren-He: Adding harmony by expanding the structure
# Python handles the memory "foundation" change automatically!
my_array.append("Data4") 

# Di-Fan: Checking the boundaries (The Length)
array_limit = len(my_array) 

print(f"Origin (Tian-Yuan): {first_element}")
print(f"Current Boundary (Di-Fan): {array_limit}")