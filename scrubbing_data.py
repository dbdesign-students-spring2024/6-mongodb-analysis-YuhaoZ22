import csv

# Define the input and output file paths
input_file = 'data/listings.csv'
output_file = 'data/listings_clean.csv'

# Open the input CSV file and create a CSV reader object
with open(input_file, 'r', newline='') as f:
    reader = csv.DictReader(f)
    
    # Define the fieldnames for the output CSV file
    fieldnames = [field for field in reader.fieldnames if field not in ['bedrooms', 'calendar_updated', 'neighbourhood_group_cleansed', 'description']]

    # Open the output CSV file and create a CSV writer object
    with open(output_file, 'w', newline='') as out_f:
        writer = csv.DictWriter(out_f, fieldnames=fieldnames)
        
        # Write the header to the output file
        writer.writeheader()
        
        # Iterate over each row in the input CSV file
        for row in reader:
            # Replace "t" and "f" values with "YES" and "NO" respectively
            for key, value in row.items():
                if value == 't':
                    row[key] = 'YES'
                elif value == 'f':
                    row[key] = 'NO'
            
            # Write the scrubbed row to the output CSV file
            writer.writerow({key: row[key] for key in fieldnames})


