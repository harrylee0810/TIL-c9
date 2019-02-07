-- 1. 테이블 구성하기
-- 1.1번
CREATE TABLE movies (
    '영화코드' INTEGER PRIMARY KEY,
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' DATE,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);

-- 1.2번
.mode csv
.import boxoffice.csv movies
.headers on
.mode column

-- 1.3번
SELECT * FROM movies;

-- 2. 기본 CRUD 조작하기
-- 2.1번
INSERT INTO movies('영화코드','영화이름','관람등급','감독','개봉연도','누적관객수','상영시간','제작국가','장르')
VALUES(20182530,'극한직업','15세이상관람가','이병현',20190123,3138467,111,'한국','코미디');

-- 2.2번
SELECT *  FROM movies WHERE 영화코드=20040521 ;  
DELETE FROM movies WHERE 영화코드=20040521 ;

-- 2.3번
UPDATE movies SET 감독='없음' WHERE 영화코드=20185124 AND 감독="";

-- 3. 원하는 데이터 찾기
-- 3.1번
SELECT 영화이름 FROM movies WHERE 상영시간 >= 150;

-- 3.2번
SELECT 영화코드, 영화이름 FROM movies WHERE 장르='애니메이션';

-- 3.3번
SELECT 영화이름 FROM movies WHERE 장르='애니메이션' AND 제작국가='덴마크';

-- 3.4번
SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수 >= 1000000 AND 관람등급='청소년관람불가';

-- 3.5번
SELECT * FROM movies WHERE 개봉연도 >= 20000101 AND 개봉연도 <= 20091231;

-- 3.6번
SELECT DISTINCT 장르 FROM movies;