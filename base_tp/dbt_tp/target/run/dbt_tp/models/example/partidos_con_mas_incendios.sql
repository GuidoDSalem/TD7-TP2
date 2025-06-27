
  
    

  create  table "postgres"."public"."partidos_con_mas_incendios__dbt_tmp"
  
  
    as
  
  (
    

with total_incendios_partido as (
    select
        bp.nombre_partido,
        count(*) as cantidad_incendios
    from "postgres"."public"."incendios" i inner join "postgres"."public"."bosquespartidos" bp on (i.nombre_bosque = bp.nombre_bosque)
    group by bp.nombre_partido
)
select *
from total_incendios_partido
order by cantidad_incendios desc
  );
  