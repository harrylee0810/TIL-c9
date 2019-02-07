# 3. DB

## 1. 목표

- 영진위 API를 활용하여 수집한 데이터를 데이터베이스에 반영하기
- SQL을 통한 데이터베이스 조작
- 단일 테이블에서의 데이터 조작
- 영화추천서비스와 관련된 다양한 검색 쿼리 작성하기

## 2. 준비 사항

1. (필수) SQL 활용 환경 설정

2. (필수) 영화 데이터 베이스

  100주간 박스오피스 TOP10에 들어간 적이 있었던 영화 총 360개의 정보가 포함된
  boxoffice.csv 가 있습니다.

## 3. 요구 사항


아래의 조건에 맞는 정보를 찾는 쿼리를 만들고 각각의 파일명에 따른 sql 파일을 만들어 제출하세요. DB이름은 pjt 입니다



### 제출 코드

----

```sqlite
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
-- 데이터베이스를 잘 보기 위해 headers와 column을 추가하였음.

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
-- 중복을 제거하기 위해 DISTINCT를 추가로 넣었음.

-- 4. Expression 활용하기
-- 4.1번
SELECT SUM(누적관객수) FROM movies;

-- 4.2번
SELECT 영화이름, MAX(누적관객수) FROM movies;

-- 4.3번
SELECT 장르, MIN(상영시간) FROM movies;

-- 4.4번
SELECT AVG(누적관객수) FROM movies WHERE 제작국가='한국';

-- 4.5번
SELECT COUNT(영화이름) FROM movies WHERE 관람등급='청소년관람불가';

-- 4.6번
SELECT COUNT(영화이름) FROM movies WHERE 상영시간>=100 AND 장르='애니메이션';

-- 5. 정렬하기
-- 5.1번
SELECT * FROM movies ORDER BY 누적관객수 DESC LIMIT 5;

-- 5.2번
SELECT * FROM movies WHERE 장르='애니메이션' ORDER BY 제작국가 ASC, 누적관객수 DESC LIMIT 10;

-- 5.3번
SELECT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10;
```





