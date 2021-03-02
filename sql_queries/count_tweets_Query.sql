select count(searchs), searchs
from tweets
where searchs = '@trezeguet'
group by searchs
order by count(searchs) desc;