import pandas as pd
from datetime import datetime
import re

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

# Function to clean key skills by copying from required column
def clean_key_skills(row):
    """
    Extracts the key skills from the 'required' column and applies them to the 'key_skills' column.
    
    Parameters:
    row (pd.Series): The row of the dataframe containing both 'required' and 'key_skills' columns.
    
    Returns:
    str: The value for 'key_skills' based on the 'required' column if 'key_skills' is missing.
    """
    required_skills = row.get('required_skills', '')
    key_skills = row.get('key_skills', '')
    
    # If key_skills is NaN or empty, copy from required
    if pd.isna(key_skills) or key_skills == 'N/A':
        return required_skills
    return key_skills

# Function to replace all variations of 'Power BI' with 'PowerBI'
def replace_power_bi(text):
    """
    Replaces all case-insensitive occurrences of 'Power BI' with 'PowerBI'.
    
    Parameters:
    text (str): The text to search and replace.
    
    Returns:
    str: The updated text.
    """
    if pd.isna(text):
        return "N/A"
    # Using regex to replace all variations of "Power BI" case-insensitively
    return re.sub(r'\bpower\s*bi\b', 'PowerBI', text, flags=re.IGNORECASE)

# Function to clean and format the CSV file
def clean_csv(input_path, output_path):
    """
    Cleans and formats a CSV file by:
    - Formatting the 'Posting Date' column to 'YYYY-MM-DD'.
    - Replacing empty cells and '-' with 'N/A'.
    - Standardizing job titles and company names.
    - Formatting location and other fields.
    - Copying main key skills from 'required' to 'key_skills' if necessary.
    - Renaming columns: lowercase and underscores instead of spaces.
    - Replacing all occurrences of 'Power BI' (in any case) with 'PowerBI'.
    
    Parameters:
    input_path (str): The path to the input CSV file.
    output_path (str): The path to save the cleaned CSV file.
    """
    # Reading data from CSV
    df = pd.read_csv(input_path)
    
    # Renaming columns: lowercase and replacing spaces with underscores
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    
    # Specifically renaming the 'key_skills (copy the main ones from required)' column to just 'key_skills'
    df.rename(columns={'key_skills_(copy_the_main_ones_from_required)': 'key_skills'}, inplace=True)
    
    # Formatting dates in the 'posting_date' column
    if 'posting_date' in df.columns:
        df['posting_date'] = df['posting_date'].apply(format_date)
    
    # Replacing empty values and '-' with 'N/A'
    df.replace({"-": "N/A", "": "N/A"}, inplace=True)
    
    # Standardizing job titles
    if 'job_title' in df.columns:
        df['job_title'] = df['job_title'].apply(standardize_job_title)
    
    # Normalizing company names
    if 'company_name' in df.columns:
        df['company_name'] = df['company_name'].apply(normalize_company_name)
    
    # Formatting location
    if 'location' in df.columns:
        df['location'] = df['location'].apply(format_location)
    
    # Copying required skills to key_skills if necessary
    if 'key_skills' in df.columns and 'required_skills' in df.columns:
        df['key_skills'] = df.apply(clean_key_skills, axis=1)
    
    # Replacing all variations of 'Power BI' in 'job_description' and 'key_skills' with 'PowerBI'
    if 'job_description' in df.columns:
        df['job_description'] = df['job_description'].apply(replace_power_bi)
    if 'key_skills' in df.columns:
        df['key_skills'] = df['key_skills'].apply(replace_power_bi)
    
    # Additional cleaning tasks as needed (e.g., clarifying employment type)
    if 'employment_type' in df.columns:
        df['employment_type'].replace({"-": "N/A", "": "N/A"}, inplace=True)

    # Saving the cleaned CSV
    df.to_csv(output_path, index=False)

# File paths
input_path = 'data_cleaning_script/Pet_Project.csv'  
output_path = 'data_cleaning_script/cleaned_data.csv'  

# Clean the CSV file
clean_csv(input_path, output_path)

