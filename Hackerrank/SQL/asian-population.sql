select sum(city.population) from city city inner join country country on CITY.CountryCode = COUNTRY.Code and country.CONTINENT = 'Asia';


select
    sum(city.population)
from city city
inner join country country
on CITY.CountryCode = COUNTRY.Code
and country.CONTINENT = 'Asia'
;
