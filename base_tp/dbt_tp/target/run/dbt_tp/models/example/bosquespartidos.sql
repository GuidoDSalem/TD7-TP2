
  
    

  create  table "postgres"."public"."bosquespartidos__dbt_tmp"
  
  
    as
  
  (
    

with ubicacion as (
    select *
    from bosquesenpartidos
)
select *
from ubicacion
  );
  