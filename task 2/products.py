from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_product_categories(spark, products_df, categories_df):

    products_df = products_df.withColumnRenamed("product_id", "category_id")
    product_category_join = products_df.join(categories_df, "category_id", "left_outer")

    # Отделяем продукты без категорий
    products_without_category = product_category_join.filter(col("category_id").isNull())
    products_without_category = products_without_category.select("product_name", col("category_name").alias("category_name"))

    # Выбираем только нужные столбцы для результирующего датафрейма
    result_df = product_category_join.select("product_name", "category_name")
    final_result = result_df.union(products_without_category)
    final_result = final_result.dropDuplicates()
    final_result = final_result.orderBy("product_name")

    return final_result

# Пример использования:
if __name__ == "__main__":

    spark = SparkSession.builder.appName("ProductCategories").getOrCreate()

    products_data = [("product1", 1), ("product1", 2), ("product2", 2), ("product3", None)]
    categories_data = [(1, "categoryA"), (2, "categoryB")]

    products_df = spark.createDataFrame(products_data, ["product_name", "product_id"])
    categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])

    result = get_product_categories(spark, products_df, categories_df)

    result.show()
    spark.stop()
