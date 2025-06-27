{{ config(materialized='table') }}

with partido as (
    select *
    from partidos
)
select * 
from partido