import pyspark.sql.functions as F
from pyspark.sql import DataFrame
import quinn
from typing import Callable


def with_greeting(df):
    return df.withColumn("greeting", F.lit("hello!"))


def with_greeting2(greeting_value: str) -> Callable[[DataFrame], DataFrame]:
    return lambda df: (
        df.withColumn("greeting", F.lit(greeting_value))
    )


def with_clean_first_name(df):
    return df.withColumn(
        "clean_first_name",
        quinn.remove_non_word_characters(F.col("first_name"))
    )