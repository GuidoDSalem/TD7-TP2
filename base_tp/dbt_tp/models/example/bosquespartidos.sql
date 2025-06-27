{{ config(materialized='table') }}

with ubicacion as (
    select *
    from bosquesenpartidos
)
select *
from ubicacion