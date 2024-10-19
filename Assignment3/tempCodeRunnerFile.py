# Function to read a matrix from a CSV file
def read_matrix(filename):
    """Read a matrix from a specified CSV file."""
    matrix = []
    with open(filename, "r", encoding='utf-8-sig') as file:  # Open filename for reading (handling BOM error)
        for line in file:
            row = list(map(int, line.strip().split(',')))  # Strip whitespace & split lines by comma
            matrix.append(row)  # Append processed row to matrix list
    return matrix

def multiply_matrices(matrix1, matrix2):
    """Multiply two 3x3 matrices."""
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Initialize a 3x3 result matrix
    for i in range(3):  # Iterate over the rows of matrix1
        for j in range(3):  # Iterate over the columns of matrix2
            for k in range(3):  # Iterate over the elements of the current row of matrix1 and column of matrix2
                result[i][j] += matrix1[i][k] * matrix2[k][j]  # Fixed the indexing
    return result

# Function to write the matrix to a CSV file
def write_matrix(matrix, filename):
    """Write the specified matrix to a CSV file."""
    with open(filename, "w") as file:  # Open filename for writing
        for row in matrix:
            file.write(','.join(map(str, row)) + '\n')  # Convert each element to a string, join elements with a comma

# Read matrices from the specified CSV files
matrix1 = read_matrix('/content/drive/MyDrive/Data_Science_Data/matrix1.csv')
matrix2 = read_matrix('/content/drive/MyDrive/Data_Science_Data/matrix2.csv')
print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)

# Multiply the matrices
result_matrix = multiply_matrices(matrix1, matrix2)

# Write the result to a new CSV file
write_matrix(result_matrix, 'result_matrix.csv')  # Save the output in result_matrix.csv
print("Resulting Matrix saved in 'result_matrix.csv'")

# Read and print the resulting matrix from the CSV file
result_matrix = read_matrix('result_matrix.csv')
print("Resulting Matrix:", result_matrix)
