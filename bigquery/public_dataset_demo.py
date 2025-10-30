from google.cloud import bigquery


def query_public_datasets():
    client = bigquery.Client()

    query = """
        SELECT 
            ORDER_ITEMS.id, 
            order_id, 
            product_id, 
            PRODUCTS.name 
        FROM `bigquery-public-data.thelook_ecommerce.order_items` AS ORDER_ITEMS
        JOIN `bigquery-public-data.thelook_ecommerce.products` AS PRODUCTS
        ON ORDER_ITEMS.product_id = PRODUCTS.id
        LIMIT 10
    """

    results = client.query(query).to_dataframe()[:20]

    print(results)


if __name__ == "__main__":
    query_public_datasets()
