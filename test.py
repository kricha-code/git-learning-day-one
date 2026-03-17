# # # # import cv2

# # # # camera = cv2.VideoCapture(0)
# # # # while camera.isOpened():
# # # #     ret, frame = camera.read()

# # # #     cv2.imshow("pop", frame)

# # # #     if cv2.waitKey(1) & 0xFF == ord("1"):
# # # #         break



# # # # --- THE ARRAY (Python List) ---

# # # # Di-Fan: We define the foundation (a list of 3 elements)
# # # # Ren-He: The harmony of items sitting side-by-side in memory
# # # my_array = ["Data1", "Data2", "Data3"]

# # # # Tian-Yuan: Accessing the Origin (Index 0)
# # # first_element = my_array[0] 

# # # # Ren-He: Adding harmony by expanding the structure
# # # # Python handles the memory "foundation" change automatically!
# # # my_array.append("Data4") 

# # # # Di-Fan: Checking the boundaries (The Length)
# # # array_limit = len(my_array) 

# # # print(f"Origin (Tian-Yuan): {first_element}")
# # # print(f"Current Boundary (Di-Fan): {array_limit}")







# # # --- THE ARRAY TRINITY ---

# # # 1. Di-Fan (The Foundation): We pre-allocate 5 slots of "land".
# # # In Python, this list has fixed boundaries for now.
# # array_foundation = [None] * 5 

# # # 2. Tian-Yuan (The Origin): The variable 'array_foundation' 
# # # points to the very first slot (Index 0).
# # tian_yuan = array_foundation[0]

# # # 3. Ren-He (The Harmony): Accessing data via offsets.
# # # We use the index to find the 'Harmony' between the origin and the target.
# # for i in range(len(array_foundation)):
# #     # Placing data into the foundation
# #     array_foundation[i] = f"Spirit_{i}" # Mapping data to the land
    
# #     # Inline Mapping:
# #     # array_foundation -> The Di-Fan (The memory block)
# #     # [i]              -> The Ren-He (The relationship/offset)
# #     # [0]              -> The Tian-Yuan (The starting point)

# # print(f"The Array is complete: {array_foundation}")





# # THE SEARCH ALGORITHM (线性搜索)

# def find_element(data_list, target):
#     # Tian-Yuan: Our 'Heavenly' goal is to find 'target'
    
#     # Di-Fan: Our 'Earthly' boundary is the length of the list
#     n = len(data_list) 
    
#     # Ren-He: The 'Harmony' of the loop checking each element one-by-one
#     for i in range(n):
#         # Comparing the current element to our goal
#         if data_list[i] == target:
#             # Harmony achieved! Goal found.
#             return f"Found at index {i}"
            
#     # If we reach the edge of the Di-Fan without finding it:
#     return "0 idndex found."

# # --- Usage ---
# my_foundation = [10, 20, 30, 40, 50, 60, 70, 80] # Di-Fan
# my_goal = 60                    # Tian-Yuan
# result = find_element(my_foundation, my_goal) # Ren-He
# print(result)


# --- VERSION A: Linear Search (Ren-He: O(n)) ---
# Good for small "Di-Fan" (Foundations)
def linear_harmony(data, target):
    # Tian-Yuan: n = len(data)
    for item in data: # The loop scales exactly with n
        if item == target:
            return True
    return False

# --- VERSION B: Nested Loop (Ren-He: O(n^2)) ---
# Dangerous! The "Earthly" limits will be reached very quickly.
def chaotic_harmony(data):
    # Tian-Yuan: n = len(data)
    for i in data:         # First loop (n)
        for j in data:     # Nested loop (n)
            print(i, j)    # Total operations: n * n