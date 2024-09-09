import pandas as pd
from datetime import datetime

# Function to format dates to YYYY-MM-DD format
def format_date(date_str):
    """
    Formats a date string to 'YYYY-MM-DD'. If the input is NaN or 'N/A', returns 'N/A'.
    
    Parameters:
    date_str (str or NaN): The date string to format.
    
    Returns:
    str: The formatted date string or 'N/A' if the input is invalid or not a date.
    """
    if pd.isna(date_str) or date_str == "N/A":
        return "N/A"
    try:
        return datetime.strptime(str(date_str), "%d/%m/%Y").strftime("%Y-%m-%d")
    except ValueError:
        return "N/A"  # Returns 'N/A' if the date is missing or invalid

# Function to standardize job titles
def standardize_job_title(title):
    """
    Standardizes job titles to ensure consistency.
    
    Parameters:
    title (str): The job title to standardize.
    
    Returns:
    str: The standardized job title.
    """
    if pd.isna(title):
        return "N/A"
    title = title.strip().title()  # Capitalize and trim
    return title

# Function to normalize company names
def normalize_company_name(name):
    """
    Normalizes company names to ensure consistency.
    
    Parameters:
    name (str): The company name to normalize.
    
    Returns:
    str: The normalized company name.
    """
    if pd.isna(name):
        return "N/A"
    name = name.strip().title()  # Capitalize and trim
    return name

# Function to format locations
def format_location(location):
    """
    Formats location to ensure consistency.
    
    Parameters:
    location (str): The location to format.
    
    Returns:
    str: The formatted location.
    """
    if pd.isna(location):
        return "N/A"
    location = location.strip()
    return location

# Function to clean and format the CSV file
def clean_csv(input_path, output_path):
    """
    Cleans and formats a CSV file by:
    - Formatting the 'Posting Date' column to 'YYYY-MM-DD'.
    - Replacing empty cells and '-' with 'N/A'.
    - Standardizing job titles and company names.
    - Formatting location and other fields.
    
    Parameters:
    input_path (str): The path to the input CSV file.
    output_path (str): The path to save the cleaned CSV file.
    """
    # Reading data from CSV
    df = pd.read_csv(input_path)
    
    # Formatting dates in the 'Posting Date' column
    if 'Posting Date' in df.columns:
        df['Posting Date'] = df['Posting Date'].apply(format_date)
    
    # Replacing empty values and '-' with 'N/A'
    df.replace({"-": "N/A", "": "N/A"}, inplace=True)
    
    # Standardizing job titles
    if 'Job Title' in df.columns:
        df['Job Title'] = df['Job Title'].apply(standardize_job_title)
    
    # Normalizing company names
    if 'Company Name' in df.columns:
        df['Company Name'] = df['Company Name'].apply(normalize_company_name)
    
    # Formatting location
    if 'Location' in df.columns:
        df['Location'] = df['Location'].apply(format_location)
    
    # Additional cleaning tasks as needed (e.g., clarifying employment type)
    if 'Employment Type' in df.columns:
        df['Employment Type'].replace({"-": "N/A", "": "N/A"}, inplace=True)

    # Saving the cleaned CSV
    df.to_csv(output_path, index=False)

# File paths
input_path = 'Pet Project.csv'  
output_path = 'cleaned_data.csv'  

# Clean the CSV file
clean_csv(input_path, output_path)
