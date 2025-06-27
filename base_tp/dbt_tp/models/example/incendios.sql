{{ config(materialized='table') }}

with incendios as (
    select * from {{ source('data_incendios', 'incendiosforestales') }}
)
select *
from incendios