import argparse
import csv

def calculate_statistic(data, operation):
    if operation == 'min':
        return min(data)
    elif operation == 'max':
        return max(data)
    else:  # operation is 'avg'
        return sum(data) / len(data)

def filter_data(data, country, from_year, to_year):
    filtered_data = []
    for entry in data:
        if entry['Country'] == country:
            year = int(entry['Year'])
            if from_year <= year <= to_year:
                filtered_data.append(float(entry['UnemploymentRatio']))
    return filtered_data

def main():
    parser = argparse.ArgumentParser(description='Unemployment Statistics')
    parser.add_argument('input_file', type=str, help='Input CSV file')
    parser.add_argument('--country', type=str, required=True, help='Country to perform operation for')
    parser.add_argument('-o', choices=['min', 'max', 'avg'], default='avg', help='Operation to perform on unemployment rates (default: avg)')
    parser.add_argument('--from', dest='from_year', type=int, help='Starting year (inclusive)')
    parser.add_argument('--to', dest='to_year', type=int, help='Ending year (inclusive)')
    args = parser.parse_args()

    data = []
    with open(args.input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            entry = {
                'Country': row[0],
                'Symbol': row[1],
                'Year': row[2],
                'UnemploymentRatio': row[3]
            }
            data.append(entry)

    filtered_data = filter_data(data, args.country, args.from_year, args.to_year)
    statistic = calculate_statistic(filtered_data, args.o)
    print(statistic)

if __name__ == '__main__':
    main()



"""Save the code in a file called statistics.py and make it executable by running the command chmod +x statistics.py in your terminal or command prompt.

To use the program, you can run the following command:

css
Copy code
./statistics.py unemployment-rate.csv --country COUNTRY -o {avg,min,max} --from FROM_ --to TO
Replace COUNTRY with the desired country name, and {avg,min,max} with the desired operation (avg for average, min for minimum, max for maximum).

The --from and --to options are optional. If provided, they will restrict the operations to the specified date range. You can include both or either one of them.

Here are a few example usages:

To calculate the average unemployment ratio for Belgium from 2010 to 2018:

css
Copy code
./statistics.py unemployment-rate.csv --country Belgium -o avg --from 2010 --to 2018
To find the maximum unemployment ratio for Germany from 2000 to 2010:

css
Copy code
./statistics.py unemployment-rate.csv --country Germany -o max --from 2000 --to 2010
To calculate the minimum unemployment ratio for France without specifying a date range:

arduino
Copy code
./statistics.py unemployment-rate.csv --country France -o min"""
