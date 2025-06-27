
  
    

  create  table "postgres"."public"."incendios__dbt_tmp"
  
  
    as
  
  (
    

with incendios as (
    select * from "postgres"."public"."incendiosforestales"
)
select *
from incendios
  );
  