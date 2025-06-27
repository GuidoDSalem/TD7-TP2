
  create view "postgres"."public"."my_first_dbt_model__dbt_tmp"
    
    
  as (
    

with bosques_data as (
    select *
    from "postgres"."public"."bosques"
)
select *
from bosques_data
  );