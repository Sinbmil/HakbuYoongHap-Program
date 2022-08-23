# SizeLab
SizeLab은 AI를 활용한 체형 및 피부색별 적합 의류 추천 시스템입니다.
# 1) 개발 배경 및 목적   
## 1. 개발 배경   
* 매해 온라인 쇼핑 이용률이 증가하고 있으나, 환불율도 함께 증가
* 기존 의류 시스템 중 회원 가입 시 사용자의 신체 사이즈 및 선호 스타일을 입력 받았으나 이를 반영하지 않는 곳이 많았음<br>
**-> 환불 주 이유: 의류 사이즈 or 색상 불만족**

## 2. 개발 목적
* 입력받은 사용자의 신체 사이즈 및 선호 스타일을 AI를 활용하여 도출함으로써 사용자의 만족율 향상에 기여
* 이를 위해 남성 상의 8가지 종류를 대상으로 개발
<hr/>

# 2) 시스템 설계
## 1. System Structure
<p align="center">
 <img src="https://user-images.githubusercontent.com/83913056/170935275-108ee07f-1c97-4335-9569-4c1ab12a82eb.png">
</p>

* 시스템 구조는 [의류 정보 저장 모듈/피부톤 적합 색상 매칭 모듈/의류 추천 모듈/데이터베이스]로 구분
### [1] 의류 정보 저장 모듈(Clothing Information Storage Module)
* 외부 System Actor에서 제공하는 의류 정보를 개발 시스템에 등록
* 등록된 의류를 수정 및 삭제
### [2] 피부톤 적합 색상 매칭 모듈(Color Check Module Sutable for Skin Tone)
* 피부톤(봄 웜톤, 여름 쿨톤, 가을 웜톤, 겨울 쿨톤)에 적합한 의류 색상 매칭
### [3] 의류 추천 모듈(Clothing Recommendation Module)
* 사용자가 입력한 사이즈 정보 및 피부 톤을 고려 > 등록 의류 정보 중 사용자와 관련된 의류 추천
### [4] 데이터베이스 
* [사용자 정보/사이즈 정보/피부톤 정보/의류 정보] 저장

## 2. Usecase Diagram
<p align="center">
 <img src="https://user-images.githubusercontent.com/83913056/170938345-22efc10a-617b-478c-9be9-20b48747a4f7.png">
</p>

### [1] Actor
* [비회원/회원/관리자/쇼핑몰 시스템]으로 구분
### [2] Usecase
* 비회원 Usecase 역할 : 회원가입
* 회원 Usecase 역할 : 로그인, 회원 정보 조회/수정, 의류 추천, 의류 구매 사이트 이동, 사용자 인증
* 관리자 Usecase 역할 : 의류 등록/수정/의류 삭제, 회원 조회/삭제, 사용자 인증
* 쇼핑몰 시스템 Usecase 역할 : 의류 제공
### [3] Link
* 회원과 관리자는 사용자 인증 Usecase를 통해 연결
* 쇼핑몰 시스템과 회원은 의류 추천 Usecase를 통해 연결

## 3. E-R Diagram
<p align="center">
 <img src="https://user-images.githubusercontent.com/83913056/170939303-ae6dd4ee-ccec-4bac-9fed-d10673e1306f.png">
</p>

### [1] 사용자 정보(User Information) 테이블
* 사용자 이름, 닉네임, 이메일, 연락처, 성별 및 사이즈 정보 저장
* 피부톤 분류로 도출된 사용자 사이즈 및 사용자 피부톤 저장
### [2] 사이즈 정보(Size Information) 테이블
* 각 의류 사이즈에 해당되는 S, M, L, XL, XXL가 분류되어 저장
### [3] 피부톤 분류 테이블
* 사용자의 피부톤 종류인 [봄 웜톤, 여름 쿨톤, 가을 웜톤, 겨울 쿨톤] 중 1개의 정보가 저장
### [4] 의류 정보 테이블
* 의류 추천 위한 여러 의류 정보 저장
<hr/>

# 3) 시스템 구현
## 1. 개발 환경
<p align="center">
 <img src="https://user-images.githubusercontent.com/83913056/170942888-82788db3-e569-4846-a65f-9247434f6aac.png">
</p>

## 2. 주요 기능 구현
### [1] 사이즈 입력
<p align="center">
 <img src="https://user-images.githubusercontent.com/83913056/170944485-91a7e7b5-f729-4a45-b2d8-3a9d78d9b65c.png">
</p>

* 회원가입 및 개인 정보 수정 시 사용자의 사이즈 선택 및 변경 가능
* 선택된 사용자 사이즈가 추천 서비스 반영됨
* 대한민국 남성 가슴 둘레를 기준으로 사이즈를 구분하였음
* 인치의 치수를 토대로 사이즈를 S, M, L, XL, XXL로 구분
* S은 90 ~ 95인치, L은 100 ~ 105인치, XL은 105 ~ 110인치, XXL은 100인치 이상에 해당

### [2] 피부톤 선택
<p align="center">
 <img src="https://user-images.githubusercontent.com/83913056/170944893-11bd3097-bb09-486d-a212-485c0eac8706.png">
</p>

* 회원가입 및 개인 정보 수정 시 사용자의 피부톤 선택 및 변경 가능
* 피부톤은 기본적으로 웜톤과 쿨톤으로 구분됨
* 웜톤 피부는 따뜻한 느낌의 피부색 / 쿨톤 피부는 차갑고 창백한 느낌이 있는 피부색
* 웜톤 피부 및 쿨톤 피부 내에서 각각 2개로 구분됨
* 웜톤 피부 종류 : 봄톤, 가을톤 / 쿨톤 피부 종류 : 여름톤, 겨울톤
* 이 4가지 톤 중 사용자는 본인 피부톤과 가장 비슷한 톤 1개를 택함. 이 정보는 DB에 저장됨

### [3] 의류 추천
* 회원 정보와 의류 정보 수집을 통해 사용자별 사이즈와 피부톤이 데이터베이스에 저장되어 있음<br><br>
<p align="center">
 <img src="https://user-images.githubusercontent.com/83913056/170949045-091f4542-4924-41fc-b2d2-07764ce68b38.png">
</p>

* 의류 추천 위해 웹 크롤링 시행. 이를 통해 얻은 의류 정보는 주기적으로 엑셀로 변환 및 DB에 저장
* 위 이미지는 엑셀로 변환된 의류 정보에 해당<br><br>

```python
def getColorName(R,G,B): 
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
```
* 크롤링된 의류 이미지는 위 이미지처럼 색상 도출 AI 프로그램에 대입하여 이미지에서 도출되는 2가지 색상을 얻음<br><br>
<p align="center">
 <img src="https://user-images.githubusercontent.com/83913056/170965912-a78f3b61-a685-45d9-b806-0f6d4cf12746.png">
</p>

* 참고로 색상은 138개로 구분되며, 색상에 대한 정보는 별도의 엑셀 파일에 저장되어 있음 

### * 의류 추천 원리
* 색상 도출 AI 프로그램을 통해 가장 높게 나온 의류 이미지 내 2가지 색상 중 1개를 관리자 최종 선정
* 그 이유는 가장 높게 나온 2가지의 색상은 배경 색상 및 류의 색상에 해당되기 때문
* 의류 이미지마다 배경 색상의 비율이 더 높을 수 있고, 의류의 색상의 비율이 더 높을 수 있음
* 이에 따라 관리자가 1개의 색상만 최종적으로 선별
* 처음부터 가장 많이 차지하는 1가지 색상만 도출 시 의류 색상이 아닌 배경 색상을 얻는 문제가 생길 수 있음
* 최종 선정된 의류 색상이 DB에 반영
```python
for i in range(len(color_list)) :
        if((color_list[i] == "red") or (color_list[i] == "tomatto") or (color_list[i] == "Coral") 
            or (color_list[i] == "Dark orange") or (color_list[i] == "Orange") 
            or (color_list[i] == "a misty rose") or (color_list[i] == "Linen")): 
            # write() 함수를 통해 어울리는 tone을 넣어준다.
            f.write(color_list[i] + ',' + 'ws' + ',' + '' + ',' + '' + ',' + ''+ '\n')
```
* 위 이미지와 같이 DB에 저장된 의류 색상이 피부톤 종류 중 무엇에 적합한가를 매칭시켜 해당 색상에 어울리는 피부톤 종류의 결과를 DB에 저장<br><br>
<p align="center"> 
 <img src="https://user-images.githubusercontent.com/83913056/170969169-93061fa7-425a-4c9d-ab13-befd7a0d811e.png">
</p>

* 위와 같이 사용자의 사이즈와 피부톤을 DB에 저장되어 있는 각 의류의 사이즈와 의류 색상에 적합한 피부톤과 비교하여 일치한 것이 있다면 이를 사용자에게 추천

### * 시연 영상 및 기타 정보는 Wiki에서 확인 바랍니다.
-> https://github.com/Sinbmil/SizeLab/wiki/SizeLab-Wiki
