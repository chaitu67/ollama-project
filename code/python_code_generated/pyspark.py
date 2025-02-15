
# Import necessary libraries
import os
from pyspark.sql import SparkSession

def csv_to_df(csv_file_path):
    """
    This function takes a CSV file path as input and converts it into a PySpark DataFrame.

    Parameters:
    csv_file_path (str): The path to the CSV file.

    Returns:
    spark_df (pyspark.sql.DataFrame): The PySpark DataFrame representation of the CSV file.
    """
    # Initialize SparkSession
    spark = SparkSession.builder.getOrCreate()

    try:
        # Read the CSV file into a DataFrame
        df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

        return df

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


def df_to_parquet(spark_df, output_path):
    """
    This function takes the PySpark DataFrame from 'csv_to_df' and converts it into a Parquet file.

    Parameters:
    spark_df (pyspark.sql.DataFrame): The PySpark DataFrame.
    output_path (str): The path where the Parquet file will be written.

    Returns:
    None
    """
    try:
        # Write the DataFrame to a Parquet file
        spark_df.write.parquet(output_path)

        print(f"Parquet file written successfully at {output_path}")

    except Exception as e:
        print(f"Error writing Parquet file: {e}")


# Test the functions
if __name__ == "__main__":
    csv_file_path = "input.csv"
    output_path = "output.parquet"

    spark = SparkSession.builder.getOrCreate()

    # Get the CSV file path as input and convert it into a PySpark DataFrame
    df = csv_to_df(csv_file_path)

    if df is not None:
        # Convert the PySpark DataFrame into a Parquet file
        df_to_parquet(df, output_path)
