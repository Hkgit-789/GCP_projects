import requests
import pandas as pd

# API Endpoint
API_URL = "https://fakestoreapi.com/products"

try:
    # Call the API
    response = requests.get(API_URL, timeout=30)

    # Raise exception if request fails
    response.raise_for_status()

    # Convert JSON response to Python object
    products = response.json()

    # Convert JSON to DataFrame
    df = pd.DataFrame(products)

    # Display some information
    print("=" * 60)
    print("API Data Retrieved Successfully")
    print("=" * 60)

    print(f"\nTotal Records : {len(df)}")
    print(f"Total Columns : {len(df.columns)}")

    print("\nColumns Received:")
    print(df.columns.tolist())

    # Print entire dataframe
    print("\nComplete Data:")
    print(df.to_string(index=False))

    # Write all records and all columns to CSV
    output_file = "products.csv"

    df.to_csv(output_file, index=False)

    print(f"\nCSV file created successfully : {output_file}")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

except requests.exceptions.ConnectionError:
    print("Connection Error. Unable to connect to API.")

except requests.exceptions.Timeout:
    print("Request Timed Out.")

except Exception as e:
    print(f"Unexpected Error: {e}")