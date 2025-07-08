{{
    config(
        catalog="gold",
        schema="marts"
     )
}}

SELECT
  customer_id,
  total_amount
FROM {{ source('lakehouse_gold', 'order_summary') }}
