def load_data(filepath):
    data_entries = []
    with open(filepath, 'r') as f:
        next(f)  # Skipping header
        for row in f:
            data_fields = row.strip().split(',')
            data_entries.append(data_fields)
    return data_entries

def split_date(date_str):
    y, m, d = map(int, date_str.strip().split('-'))  # Decompose the date
    return (y, m, d)

def filter_records_by_date(data_entries, from_date, to_date):
    result_records = []
    from_date_tuple = split_date(from_date)
    to_date_tuple = split_date(to_date)

    for record in data_entries:
        date_str = record[0].strip()  # Clean date string
        record_date_tuple = split_date(date_str)

        if from_date_tuple <= record_date_tuple <= to_date_tuple:
            result_records.append(record)

    return result_records

def avg_calories_per_day(filtered_entries):
    day_avg = {}
    for record in filtered_entries:
        date_str = record[0].strip()
        cal_value = int(record[2].strip())  # Use index 2 for calories

        if date_str in day_avg:
            day_avg[date_str].append(cal_value)
        else:
            day_avg[date_str] = [cal_value]

    # Compute the average calories per day
    avg_daily = {date: sum(cals) / len(cals) for date, cals in day_avg.items()}
    return avg_daily

def max_calories_per_day(filtered_entries):
    day_max = {}
    for record in filtered_entries:
        date_str = record[0].strip()
        cal_value = int(record[2].strip())  # Use index 2 for calories

        if date_str in day_max:
            day_max[date_str] = max(day_max[date_str], cal_value)
        else:
            day_max[date_str] = cal_value
            
    return day_max

def standard_deviation_calories(filtered_entries):
    cal_values = [int(record[2].strip()) for record in filtered_entries]  # Use index 2 for calories
    if len(cal_values) <= 1:
        return None
    avg_value = sum(cal_values) / len(cal_values)
    variance = sum((x - avg_value) ** 2 for x in cal_values) / len(cal_values)
    return variance ** 0.5

def highest_calories_in_range(filtered_entries):
    return max(int(record[2].strip()) for record in filtered_entries) if filtered_entries else 0  # Use index 2 for calories

def avg_calories_in_range(filtered_entries):
    total_cals = sum(int(record[2].strip()) for record in filtered_entries)  # Use index 2 for calories
    return total_cals / len(filtered_entries) if filtered_entries else None

def get_date_input(prompt_text):
    while True:
        date_str = input(f"{prompt_text} (YYYY-MM-DD): ")
        # Ensuring proper format
        if len(date_str) == 10 and date_str[4] == '-' and date_str[7] == '-':
            return date_str
        else:
            print("Invalid input format. Please use YYYY-MM-DD.")

def run_program():
    filepath = 'calorie_log.csv'  # Modify path if necessary
    data_entries = load_data(filepath)

    from_date = get_date_input("Start Date")
    to_date = get_date_input("End Date")

    selected_records = filter_records_by_date(data_entries, from_date, to_date)

    avg_per_day = avg_calories_per_day(selected_records)
    max_per_meal = max_calories_per_day(selected_records)
    std_dev = standard_deviation_calories(selected_records)
    max_calories = highest_calories_in_range(selected_records)
    avg_calories = avg_calories_in_range(selected_records)

    print(f"Records from {from_date} to {to_date}:")
    for date, avg_cal in avg_per_day.items():
        print(f"Date: {date}, Avg Calories: {avg_cal:.2f}")

    for date, max_cal in max_per_meal.items():
        print(f"Date: {date}, Max Calories in Meal: {max_cal}")

    if std_dev is not None:
        print(f'Standard deviation of calories between {from_date} and {to_date}: {std_dev:.2f}')

    if max_calories is not None:
        print(f'Max Calories consumed between {from_date} and {to_date}: {max_calories}')

    if avg_calories is not None:
        print(f'Avg Calories consumed between {from_date} and {to_date}: {avg_calories:.2f}')
    else:
        print("No available records.")

if __name__ == "__main__":
    run_program()
