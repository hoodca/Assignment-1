import pandas as pd

#Load our Excel (csv) file <3
file_path = "C:/Users/camjh/Downloads/extracted_files/us_states_covid19_daily.csv"
df = pd.read_csv(file_path) #adjust sheet name as needed :)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d', errors='coerce')


# Get the earliest and latest dates
start_date = df['date'].min()
end_date = df['date'].max()

# Print the result
print(f"Date range in Excel sheet: {start_date.date()} to {end_date.date()}")
