import requests

def get_phone_number_info(phone_number):
    try:
        # Make a request to the NumVerify API to get information about the phone number
        response = requests.get(f'http://apilayer.net/api/validate?access_key=b92ed61d1c1757f6f53196ca1594a404&number={phone_number}&country_code=&format=1')
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200 and data.get('valid'):
            return data
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

def main():
    # Prompt the user to enter a phone number
    phone_number = input("Enter a phone number (including country code): ")

    # Get information about the phone number
    phone_info = get_phone_number_info(phone_number)
    if phone_info:
        print("Phone number:", phone_number)
        print("Country name:", phone_info.get('country_name'))
        print("Location:", phone_info.get('location'))
        print("Carrier:", phone_info.get('carrier'))
        print("Line type:", phone_info.get('line_type'))
    else:
        print("Unable to retrieve information for the phone number.")

if __name__ == "__main__":
    main()
