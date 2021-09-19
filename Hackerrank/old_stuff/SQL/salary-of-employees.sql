select name from employee where salary > 2000 and months < 10 order by employee_id;
-- african-cities/
select cty.name from city cty inner join country ctry on ctry.code = cty.countrycode and ctry.CONTINENT = 'Africa';

-- average-population-of-each-continent
select ctry.continent, floor(avg(cty.population)) from city cty inner join country ctry on ctry.code = cty.countrycode group by ctry.continent;
;

-- the-report
select case when gr.grade >= 8 then st.name end as name, gr.grade, st.marks from students st inner join grades gr on st.marks between gr.min_mark and gr.max_mark order by gr.grade desc, st.name, decode(st.name,NULL,st.marks);

-- full-score
select

    h.hacker_id,
    h.name

from hackers h
;
