select ceil(avg(salary) - avg(to_number(regexp_replace(to_char(salary),'0')))) from EMPLOYEES ;
