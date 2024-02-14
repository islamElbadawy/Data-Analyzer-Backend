# utils.py
import pandas as pd

def analyze(data_list):
    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(data_list)


    # Convert columns to appropriate data types
    df["Founded"] = df["Founded"].astype(int)
    df["Number of employees"] = df["Number of employees"].astype(int)

    # Descriptive statistics
    stats = df.describe()

    # Correlation matrix
    # correlation_matrix = df.corr()

    # Group by Country and calculate mean Number of employees
    average_employees_by_country = df.groupby("Country")["Number of employees"].mean()

    return {
        'descriptive_statistics': stats.to_dict(),
        # 'correlation_matrix': correlation_matrix.to_dict(),
        'average_employees_by_country': average_employees_by_country.to_dict()
    }
