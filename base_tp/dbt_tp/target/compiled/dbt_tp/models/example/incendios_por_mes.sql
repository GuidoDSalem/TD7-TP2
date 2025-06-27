

with incendios_mes_partidos as (
    select p.nombre as partido, date_trunc('month', i.ts_inicio) as mes, count(*) as cantidad_incendios
    from "postgres"."public"."incendios" i inner join "postgres"."public"."bosquespartidos" bp on (i.nombre_bosque = bp.nombre_bosque)
     inner join "postgres"."public"."mpartidos" p on (bp.nombre_partido = p.nombre)
    group by p.nombre, date_trunc('month', i.ts_inicio)
)
select *
from incendios_mes_partidos