select earning, cnt from (select months*salary as earning, count(*) as cnt from employee group by months*salary order by 2 desc) where rownum = 1;
