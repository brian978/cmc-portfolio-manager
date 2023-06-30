from datetime import datetime
import pytz


def format_date(date_string):
    # Convert to datetime object
    date_object = datetime.strptime(date_string, "%d %b %Y %I:%M %p %Z")

    # Set the timezone to UTC
    utc = pytz.timezone('UTC')
    date_object = utc.localize(date_object)

    # Convert to desired format with fractional seconds
    formatted_date = date_object.isoformat(timespec='milliseconds')

    # Replace '+00:00' with 'Z'
    formatted_date = formatted_date.replace('+00:00', 'Z')

    return formatted_date
