# Requirements Analysis

## Purpose
List what we need to clean the data.

## Requirements
1. **Standardize Job Titles**:
   - Ensure consistency in job titles (e.g., "Business-oriented BI and Data Analyst" vs. "Data Analyst/Power BI specialist within Marketing Operations").
   - Capitalize and format titles uniformly.

2. **Normalize Company Names**:
   - Standardize company names to ensure consistency (e.g., "Bunzl Nordic" and "Universal Robots").

3. **Uniform Location Format**:
   - Ensure location formats are consistent. For example, use "City, Country" format if applicable.
   - Remove any unnecessary information, such as extra spaces or abbreviations.

4. **Clarify Employment Type**:
   - Specify employment types clearly (e.g., Full-Time, Part-Time, Hybrid Work). Remove any ambiguous terms or extra punctuation.

5. **Fill Missing Salary Range**:
   - If the salary range is missing, it should be filled or marked as "Not Disclosed".

6. **Consistent Job Description Formatting**:
   - Ensure job descriptions are free of inconsistent punctuation or formatting issues.
   - Break down lengthy descriptions into bullet points for better readability.

7. **Extract Key Skills**:
   - Identify and list key skills clearly (e.g., "Power BI", "DAX", "SQL").
   - Ensure consistency in naming and avoid duplicates.

8. **Remove Redundant Columns**:
   - If "Key Skills" and "Required Skills" overlap significantly, consider merging them or making sure there are no duplicates.

9. **Experience Level and Experience Required**:
   - Ensure experience levels and requirements are clearly stated and in a uniform format (e.g., "1-2 years" vs. "5-8 years").

10. **Language Consistency**:
    - Ensure language fields are consistently formatted (e.g., "English", "Danish"). Check for any missing or inconsistent entries.

11. **Education and Application Link**:
    - Ensure that education requirements and application links are correctly formatted and complete.
    - Verify that all application links are functional and direct to the correct page.

12. **Posting Date and Deadline**:
    - Verify date formats are consistent (e.g., "MM/DD/YYYY").
    - Fill in or standardize any missing dates.

## Summary
- **Cleaning needs**:
  - Standardize job titles and company names.
  - Ensure consistent location and employment type formats.
  - Fill in missing salary information and ensure job descriptions are well-formatted.
  - Extract and standardize key skills, handle redundant columns, and clarify experience levels.
  - Ensure consistency in language fields and verify education and application links.
  - Standardize date formats and fill in missing posting and deadline dates.

- **CSV format**:
  - Ensure uniform column formats and consistency across rows.
  - Verify that all URLs and contact details are accurate and functional.
  - Mark any missing information appropriately, e.g., "Not Disclosed" for salary ranges.
