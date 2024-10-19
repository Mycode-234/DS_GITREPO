import matplotlib.pyplot as plt

# Function to read CSV data without using any library
def read_csv_file(file_path):
    """Read a CSV file and return the header and data."""
    data = []
    with open(file_path, 'r') as file:
        # Read the header row
        header = file.readline().strip().split(',')

        # Read subsequent rows
        for line in file:
            fields = line.strip().split(',')  # Remove whitespace and split by comma
            data.append(fields)  # Append the processed fields to data list

    return header, data

# Function to calculate pass/fail status based on average marks
def calculate_pass_fail(csv_data, math_marks_index, english_marks_index):
    """Calculate the count of students passing and failing based on average marks."""
    pass_count = 0
    fail_count = 0

    for row in csv_data:
        # Extract Math and English marks from respective indices
        math_mark = float(row[math_marks_index])
        english_mark = float(row[english_marks_index])

        # Calculate average marks
        avg_marks = (math_mark + english_mark) / 2

        # Determine pass or fail
        if avg_marks >= 40:  # Adjusted to include students with exactly 40 marks as pass
            pass_count += 1
        else:
            fail_count += 1

    return pass_count, fail_count

# Example usage to read CSV file
file_path = 'marks.csv'  # Update with your actual file path
header, csv_data = read_csv_file(file_path)

# Find the indices of 'Math Marks' and 'English Marks' in header
math_marks_index = header.index('Math Marks')
english_marks_index = header.index('English Marks')

# Calculate pass/fail counts based on average marks
pass_count, fail_count = calculate_pass_fail(csv_data, math_marks_index, english_marks_index)

# Plotting the pie chart for pass/fail distribution
labels_pass_fail = ['Pass', 'Fail']
sizes_pass_fail = [pass_count, fail_count]
colors_pass_fail = ['lightgreen', 'lightcoral']
explode_pass_fail = (0.1, 0)  # Explode the 'Pass' slice

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)  # Create the first subplot for pass/fail distribution
plt.pie(sizes_pass_fail, labels=labels_pass_fail, colors=colors_pass_fail, explode=explode_pass_fail,
        autopct='%1.1f%%', startangle=140)
plt.title('Pass/Fail Distribution based on Average Marks')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Extract gender column data
gender_index = header.index('Gender')
genders = [row[gender_index] for row in csv_data]  # Collect gender data from each row

# Calculate counts for each gender
gender_counts = {}
for gender in genders:
    if gender in gender_counts:
        gender_counts[gender] += 1
    else:
        gender_counts[gender] = 1

# Plotting the pie chart for gender distribution
labels_gender = list(gender_counts.keys())
sizes_gender = list(gender_counts.values())
colors_gender = ['lightblue', 'pink']  # Adjust colors as needed

plt.subplot(1, 2, 2)  # Create the second subplot for gender distribution
plt.pie(sizes_gender, labels=labels_gender, colors=colors_gender,
        autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()  # Ensures spacing between subplots

plt.show()  # Display the plots
