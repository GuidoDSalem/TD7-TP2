
  
    

  create  table "postgres"."public"."mpartidos__dbt_tmp"
  
  
    as
  
  (
    

with partido as (
    select *
    from partidos
)
select * 
from partido
  );
  