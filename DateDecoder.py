# Create a dict suitable for decoding month names to numbers.
month_dict = {
    'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06',
    'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'
}

def decode_date(date_string):
    # Create a function which uses string operations to split the date into 3 items using the "-" character.
    day, month, year = date_string.split('-')
    
    # Translate the month
    month = month_dict[month.upper()]
    
    # Correct the year to include all of the digits.
    if int(year) < 50:
        year = '20' + year
    else:
        year = '19' + year
    
    return (year, month, day)

date = "8-MAR-85"
decoded_date = decode_date(date)
print("Decoded Date:", decoded_date)
