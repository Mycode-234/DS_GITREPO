import numpy as np

def generate_3d_matrix(dim_x, dim_y, dim_z):  # Function to create a 3D matrix
    matrix = np.zeros((dim_x, dim_y, dim_z), dtype=int)

    for x in range(dim_x):
        for y in range(dim_y):
            for z in range(dim_z):
                sum_indices = x + y + z
                if (sum_indices % 10 == 2) or (sum_indices % 10 == 6):
                    matrix[x, y, z] = 0  # Assign 0 based on index sum rule
                else:
                    matrix[x, y, z] = 1  # Assign 1 otherwise

    return matrix

def locate_max_sequence(matrix_3d):
    dim_x, dim_y, dim_z = matrix_3d.shape
    longest_sequence = 0
    starting_point = None
    sequence_coordinates = []  # Store coordinates of longest sequence

    for x_idx in range(dim_x):
        for y_idx in range(dim_y):
            seq_length = 0
            temp_coordinates = []  # Temporarily store coordinates of current sequence

            for z_idx in range(dim_z):
                if matrix_3d[x_idx, y_idx, z_idx] == 1:
                    temp_coordinates.append((x_idx, y_idx, z_idx))  # Append coordinates for 1s
                    seq_length += 1

                    if seq_length > longest_sequence:
                        longest_sequence = seq_length
                        starting_point = (x_idx, y_idx, z_idx - seq_length + 1)
                        sequence_coordinates = temp_coordinates.copy()  # Copy current sequence
                else:
                    seq_length = 0
                    temp_coordinates = []  # Reset coordinates if 0 is encountered

    return longest_sequence, starting_point, sequence_coordinates

# Dimensions of the 3D matrix
size_x, size_y, size_z = 7, 5, 3
# Create the 3D matrix
matrix_3d = generate_3d_matrix(size_x, size_y, size_z)

# Print the 3D matrix
for x_idx in range(size_x):
    for y_idx in range(size_y):
        for z_idx in range(size_z):
            print(f"matrix[{x_idx}][{y_idx}][{z_idx}] = {matrix_3d[x_idx][y_idx][z_idx]}")
        print()
    print()

# Find the longest sequence of 1s
max_length, start_point, longest_sequence = locate_max_sequence(matrix_3d)
print(f"Length of the longest sequence of 1s: {max_length}")
print(f"Start position of the longest sequence: {start_point}")
print("Coordinates of the longest sequence:")
for coords in longest_sequence:
    print(coords)
