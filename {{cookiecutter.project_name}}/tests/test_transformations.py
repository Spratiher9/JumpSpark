import pytest

from pyspark.sql.types import *
from quinn.extensions import *

import {{cookiecutter.project_name}}.sparksession as S
import {{cookiecutter.project_name}}.transformations as T

import chispa


class TestTransformations(object):

    def test_with_greeting(self):
        source_data = [
            ("jose", 1),
            ("li", 2)
        ]
        source_df = S.spark.createDataFrame(
            source_data,
            ["name", "age"]
        )
        actual_df = T.with_greeting(source_df)
        expected_data = [
            ("jose", 1, "hello!"),
            ("li", 2, "hello!")
        ]
        expected_df = S.spark.createDataFrame(
            expected_data,
            ["name", "age", "greeting"]
        )
        chispa.assert_df_equality(actual_df, expected_df, ignore_nullable = True)


    def test_with_greeting2(self):
        source_data = [
            ("jose", 1),
            ("li", 2)
        ]
        source_df = S.spark.createDataFrame(
            source_data,
            ["name", "age"]
        )
        actual_df = source_df.transform(T.with_greeting2("hi"))
        expected_data = [
            ("jose", 1, "hi"),
            ("li", 2, "hi")
        ]
        expected_df = S.spark.createDataFrame(
            expected_data,
            ["name", "age", "greeting"]
        )
        chispa.assert_df_equality(actual_df, expected_df, ignore_nullable = True)



    def test_with_clean_first_name(self):
        source_df = S.spark.create_df(
            [("jo&&se", "a"), ("##li", "b"), ("!!sam**", "c")],
            [("first_name", StringType(), True), ("letter", StringType(), True)]
        )
        actual_df = T.with_clean_first_name(source_df)
        expected_df = S.spark.create_df(
            [("jo&&se", "a", "jose"), ("##li", "b", "li"), ("!!sam**", "c", "sam")],
            [("first_name", StringType(), True), ("letter", StringType(), True), ("clean_first_name", StringType(), True)]
        )
        chispa.assert_df_equality(actual_df, expected_df, ignore_nullable = True)