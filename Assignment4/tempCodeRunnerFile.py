def read_name(file_path):
    """Read names from the CSV file and return as a list."""
    with open(file_path, 'r') as file:
        return file.read().strip('\n').splitlines()  # Read file content and split into lines

def load_matrix(data, mat):
    """Load data from the provided list into the matrix."""
    mat.extend(data)  # Extend the matrix with the data from the list
    print("Loaded matrix:", mat)

def convert_to_column_major(mat):
    """Convert the matrix to column-major order."""
    temp = []
    n = max(len(i) for i in mat)  # Get the maximum length of the rows
    for i in range(n):
        res = ""
        for j in range(len(mat)):
            try:
                res += mat[j][i]  # Concatenate characters column-wise
            except IndexError:  # Handle case when row length is less than n
                res += " "  # Add space if the row is shorter
        temp.append(res.rstrip().lstrip())  # Strip leading/trailing spaces
    mat.clear()  # Clear the original matrix
    mat.extend(temp)  # Update the matrix with the new column-major data
    print("Column major:", mat)

def calculate_character_length(mat):
    """Calculate the total character length excluding spaces."""
    res = sum(len(i.replace(" ", "")) for i in mat)  # Sum lengths of strings after removing spaces
    print("Character length:", res)

def store_list_as_string(mat, output_file):
    """Store the matrix data as a string in an output file."""
    with open(output_file, "wt") as file:  # Open the output file
        for i in mat:
            file.write(i + '\n')  # Write each row to the file

def main():
    """Main function to execute the workflow."""
    file_path = 'names.csv'  # Specify the path to your CSV file
    output_file = 'output.txt'  # Specify the output file name

    data = read_name(file_path)  # Read names from the CSV file
    mat = []  # Initialize matrix list
    load_matrix(data, mat)  # Load data into the matrix
    convert_to_column_major(mat)  # Convert matrix to column-major order
    calculate_character_length(mat)  # Calculate total character length
    store_list_as_string(mat, output_file)  # Store the matrix as a string in the output file

# Entry point of the script
if __name__ == "__main__":
    main()
