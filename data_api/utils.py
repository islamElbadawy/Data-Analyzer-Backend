# utils.py
import pandas as pd

def analyze(data_list):
    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(data_list)

    # Drop unnecessary columns if needed
    df = df.drop(["Reference USEEIO Code"], axis=1, errors='ignore')

    # Convert numeric columns to appropriate data types
    numeric_columns = ["Supply Chain Emission Factors without Margins", 
                        "Margins of Supply Chain Emission Factors", 
                        "Supply Chain Emission Factors with Margins"]

    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # Descriptive statistics for numeric columns
    numeric_stats = df[numeric_columns].describe()

    # Correlation matrix for numeric columns
    correlation_matrix = df[numeric_columns].corr()

    # Group by NAICS Title and calculate mean of numeric columns
    averages_by_title = df.groupby("2017 NAICS Title")[numeric_columns].mean()

    return {
        'numeric_statistics': numeric_stats.to_dict(),
        'correlation_matrix': correlation_matrix.to_dict(),
        'averages_by_title': averages_by_title.to_dict()
    }
