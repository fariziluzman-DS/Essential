use football;
select * from result;

-- make colom baru tetapi hanya read only tanpa mengganti data asal
select *, home_score + away_score as totalgol, abs(home_score - away_score) as selisihgol from result;

-- sub query
select max(home_score) as max_goalhome from result;
select * from result where home_score = (select max(home_score) as max_goalhome from result);

-- selisi score terbesar
select *,abs(home_score - away_score) as selisih from result having selisih = (select max(abs(home_score - away_score)) as selisih from result);
select *,abs(home_score - away_score) as selisih from result having selisih = (select max(abs(home_score - away_score)) from result);

-- away dengan kemenangan terbesar
select *,(away_score - home_score) as selisih from result having selisih = (select max(away_score - home_score) from result);
select * from result having (away_score - home_score) = (select max(away_score - home_score) from result);

-- jumlah gol terbanyak
select *,(away_score + home_score) from result having (away_score + home_score) = (select max(away_score + home_score) from result);
select * from result order by (home_score + away_score) desc limit 5;

select *,abs(away_score - home_score) as selisih from result where home_team= 'Indonesia' or away_team = 'Indonesia';
select * from result where away_team = 'Indonesia' order by (away_score - Home_score) desc ;


-- pertandingan dgn gol terbanyak turnamen fifa world cup
select * from result where away_score + home_score = (select max(away_score + home_score) from result where tournament like 'FIFA%');
select * from result where away_score + home_score = (select max(away_score + home_score) from result where tournament like 'FIFA%');

-- rarata gol england di home
select avg(home_score) as rarata from result where home_team = 'england';

-- rarata gol england di away
select avg(away_score) as rarata from result where away_team = 'england';


-- ada berapa match di kuala lumpur
select count(*) from result where city = 'kuala lumpur';
select count(*) from result where city = 'jakarta';

-- 5 pertandingan friendly match dengan jumlah gol terbanyak
select * from result where tournament = 'friendly' order by (home_score + away_score) desc limit 5;

-- 5 pertandingan world cup match dengan jumlah gol terbanyak
select * from result where tournament like '%fifa world cup%' order by (home_score + away_score) desc limit 5;

-- 5 pertandingan dengan gol away terbanyak
select * from result order by (away_score) desc limit 5 ;


select * from result where (home_team= 'indonesia' or away_team = 'indonesia') and tournament like '%fifa world cup%';

select country,avg(home_score) as home_score_mean from result group by country;