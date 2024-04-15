-- 코드를 작성해주세요
select FISH_INFO.ID AS ID,
    FISH_NAME_INFO.FISH_NAME AS FISH_NAME,
    FISH_INFO.LENGTH AS LENGTH
    from 
    (
    select FISH_TYPE,max(LENGTH) as length
        from FISH_INFO
        where LENGTH > 10
        group by FISH_TYPE
    ) as max_lengths
    inner join FISH_INFO on max_lengths.FISH_TYPE = FISH_INFO.FISH_TYPE and max_lengths.length = FISH_INFO.LENGTH
    inner join FISH_NAME_INFO on FISH_NAME_INFO.FISH_TYPE = FISH_INFO.FISH_TYPE
    order by FISH_INFO.ID ASC