import pytest
import chispa

def test_compare_dataframes(spark):
    df1 = spark.createDataFrame(
        [
            ("Alice", 1500),
            ("Bob", 1000),
            ("Charlie", 150),
            ("Dexter", 100)
        ],
        ["name", "count"]
    )
    df2 = spark.createDataFrame(
        [
            ("Alice", 1500),
            ("Bob", 1000),
            ("Charlie", 150),
            ("Dexter", 100)
        ],
        ["name", "count"]
    )
    chispa.assert_df_equality(df1, df2)