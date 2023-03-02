# Toy_Project2
Toy Project2는 Fastapi를 이용한 웹 서비스 프로젝트입니다.

## 목차
1. [FastAPI 프로젝트 구조](#fastapi-프로젝트-구조)
2. [프로젝트를 설정하는 main.py 파일](#프로젝트를-설정하는-mainpy-파일)
3. [데이터베이스를 설정하는 database 디렉터리](#데이터베이스를-설정하는-Database-디렉터리)
4. [모델을 관리하는 Models 디렉터리](#모델을-관리하는-models-디렉터리)
5. [API를 구성하는 Domain 디렉터리](#api를-구성하는-Domain-디렉터리)
6. [frontend](#frontend)
7. [기타(https/tutorials 디렉토리)](#기타httpstutorials-디렉토리)


## FastAPI 프로젝트 구조
Toy Project2 프로젝트의 전체 구조는 다음과 같습니다. 
```
Toy_Project2
├── backend
│   ├── app
│   ├── db  
│   │   └── database.py
│   ├── models 
│   │   └── models.py
│   ├── domain
│   │   ├── answer
│   │   ├── question
│   │   └── user
│   └── main.py
├── frontend
├── https
└── tutorials
```
## 프로젝트를 설정하는 main.py 파일
main.py 파일에 생성한 app 객체는 FastAPI의 핵심 객체이다. app 객체를 통해 FastAPI의 설정을 할 수 있다. main.py는 FastAPI 프로젝트의 전체적인 환경을 설정하는 파일이다.
## 데이터베이스를 설정하는 Database 디렉터리
database.py 파일은 데이터베이스와 관련된 설정을 하는 파일이다. 이 파일에는 데이터베이스를 사용하기 위한 변수, 함수등을 정의하고 접속할 데이터베이스의 주소와 사용자, 비밀번호등을 관리한다.
## 모델을 관리하는 models 디렉터리
프로젝트는 ORM(object relational mapping)을 지원하는 파이썬 데이터베이스 도구인 SQLAlchemy를 사용한다. SQLAlchemy는 모델 기반으로 데이터베이스를 처리한다. 지금은 모델 기반으로 데이터베이스를 처리한다는 말이 이해되지 않겠지만, 이후 프로젝트를 진행하면 잘 알 수 있을 것이다. 아무튼 지금 여러분이 알아야 할 내용은 프로젝트에는 "모델 클래스들을 정의할 models.py 파일이 필요하다"는 것이다.

## API를 구성하는 Domain 디렉터리
질문과 답변을 작성하는 게시판을 만드는 것을 최종 목표로 하고 있다. 이에 "질문", "답변", "사용자" 라는 총 3개의 도메인을 두어 그 하위에 관련된 파일을 작성하고자 한다.

```
도메인은 "질문", "답변", "사용자" 처럼 굵직한 요구사항 또는 문제 영역을 대표하는 말이다.
```

- 질문 (question)
- 답변 (answer)
- 사용자 (user)

그리고 각 도메인은 API를 생성하기 위해서 다음과 같은 파일들이 필요하다.

- 라우터 파일 - URL과 API의 전체적인 동작을 관리
- 데이터베이스 처리 파일 - 데이터의 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)를 처리 (CRUD)
- 입출력 관리 파일 - 입력 데이터와 출력 데이터의 스펙 정의 및 검증

예를 들어 질문(domain/question) 도메인이라면 다음의 3개 파일이 필요하다.

- question_router.py - 라우터 파일
- question_crud.py - 데이터베이스 처리 파일
- question_schema.py - 입출력 관리 파일

## frontend
Svelte 프레임워크를 설치한 디렉터리이다. Svelte의 소스 및 빌드 파일들을 저장할 프론트엔드의 루트 디렉터리이다. 최종적으로 frontend/dist 디렉터리에 생성된 빌드 파일들을 배포시에 사용할 것이다.

## 기타(https/tutorials 디렉토리)
https 디렉토리 - VSCode의 Rest Client 요청 정리
tutorials 디렉토리 - Fastapi의 Doc문서 정리 및 Test