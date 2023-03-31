from pyspark.sql import SparkSession

spark = (SparkSession.builder
            .master("local")
            .appName("{{cookiecutter.project_name}}")
            .getOrCreate())
