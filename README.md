#全字段md5
select md5(textin (record_out(foo))) from pg_class foo;

#表结构（字段顺序）
select attname,attnum from pg_attribute where attrelid::regclass::text = 'pg_class' and attnum > 0 order by attnum asc;
select attrelid::regclass::text,md5(string_agg(attname,',' order by attnum)) from pg_attribute where attrelid::regclass::text = 'pg_class' and attnum > 0 group by 1;

#表字段md5获取
select n.nspname||'.'||c.relname,md5(string_agg(attname,',' order by attnum)) 
from pg_attribute,pg_class c,pg_namespace n 
where attrelid::regclass = c.oid::regclass and (n.oid > 16384 or n.oid = 2200) 
		and c.oid::regclass::text !~ 'pg_toast' 
		and c.relname !~ 'gp_' 
		and c.oid > 16384 
		and attnum > 0  
group by 1;


#外部表md5获取
psql -qtAXF '^A' -c "select n.nspname||'.'||c.relname,md5(textin (record_out(pg_exttable)))
					 from pg_exttable,pg_class c,pg_namespace n
					 where c.relnamespace = n.oid 
					 		and c.oid::regclass = reloid::regclass 
					 		and n.nspname not in ('gp_toolkit','pg_toast')"

#分布键md5获取
select
        tbname,md5(string_agg(attname,','))
from
(
        select
                e.nspname||'.'||c.relname tbname,b.attname
        from ( select localoid ,unnest(attrnums) as attrnums from gp_distribution_policy) a
        join pg_attribute b on a.attrnums = b.attnum and a.localoid = b.attrelid
        join pg_class c on a.localoid = c.oid
        join pg_namespace e on c.relnamespace = e.oid
) t
group by tbname;