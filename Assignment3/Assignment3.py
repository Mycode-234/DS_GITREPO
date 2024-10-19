import csv

def read_matrix(filename):
    """Read a matrix from a specified CSV file."""
    matrix = []
    with open(filename, "r", encoding='utf-8-sig') as file:
        for line in file:
            row = list(map(int, line.strip().split(',')))  # Convert each line to a list of integers
            matrix.append(row)  # Append the row to the matrix
    return matrix

def multiply_matrices(matrix1, matrix2):
    """Multiply two 3x3 matrices."""
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Initialize a 3x3 result matrix
    for i in range(3):  # Iterate over the rows of matrix1
        for j in range(3):  # Iterate over the columns of matrix2
            for k in range(3):  # Iterate over the elements
                result[i][j] += matrix1[i][k] * matrix2[k][j]  # Perform multiplication
    return result

def write_matrix(matrix, filename):
    """Write the specified matrix to a CSV file."""
    with open(filename, "w") as file:
        for row in matrix:
            file.write(','.join(map(str, row)) + '\n')  # Convert row elements to string and write to file

# Read matrices from the specified CSV files
matrix1 = read_matrix('matrix1.csv')  # Update the file path as needed
matrix2 = read_matrix('matrix2.csv')  # Update the file path as needed

# Multiply the matrices
result_matrix = multiply_matrices(matrix1, matrix2)

# Write the result to a new CSV file
write_matrix(result_matrix, 'result_matrix.csv')
print("Resulting Matrix saved in 'result_matrix.csv'")

# Read and print the resulting matrix from the CSV file
result_matrix = read_matrix('result_matrix.csv')
print("Resulting Matrix:", result_matrix)
