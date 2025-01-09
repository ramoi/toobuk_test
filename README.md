
toobuk_test는 Toobuk를 사용하면서 사용할 수 있는 다양한 예제를 모았습니다.

## 차례
1. [설치](#설치)
1. [Get 방식으로 크롤링하기](#Get-방식으로-크롤링하기)
1. [Post 방식으로 크롤링하기](#Get-방식으로-크롤링하기)
1. [Parameter 설정하기](#Parameter-설정하기)
1. [Output 설정하기](#Output-설정하기)
   1. [Output 설정하기](#Output-설정하기)
   1. [Output 하나만 가져오기](#Output-하나만-가져오기)
   1. [Output 여러개 가져오기](#Output-여러개-가져오기)
   1. [Output 전체 가져오기](#Output-전체-가져오기)
1. [Output List/Single 데이타 추출](#Output-List/Single-데이타-추출)
   1. [List로 추출하기](#List로-추출하기)
   1. [Single로 추출하기](#Single로-추출하기)
1. [Output 추출 패턴 적용하기](#Output-추출-패턴-적용하기)
   1. [text값 가져오기](#text값 가져오기)
   1. [속성값 가져오기](#속성값 가져오기)
1. [읽어온 데이타 skip 하기](#읽어온-데이타-skip-하기)
   1. [미리 정의된 skip](#미리-정의된-skip)
      1. [slice](#slice)
      1. [white 공백문자 skip](#white-공백문자-skip)
   1. [skip 함수 추가](#skip-함수-추가)
   1. [skip 사용자 정의 함수 사용](#skip-사용자-정의-함수-사용)
   1. [여러 skip을 같이 사용하기](#여러-skip을-같이-사용하기)
1. [변환하기](#변환하기)
   1. [미리 정의된 변환기](#미리-정의된-변환기)
      1. [currency](#currency)
      1. [콤마제거](#remove.comma)
      1. [int](#int)
      1. [float](#float)
      1. [정규식](#정규식)
   1. [변환기 추가](#변환기-추가)
   1. [변환기 사용자 정의 함수 사용](#변환기-사용자-정의-함수-사용)
   1. [변환기 여러개 사용하기](#변환기-여러개-사용하기)
1. [크롤링 여러번 하기:페이징처리 크롤링](#크롤링-여러번-하기:페이징처리 크롤링)
   1. [파라메터 설정 후, 페이징처리하기](#파라메터-설정-후,-페이징처리하기)
1. [Connector](#Connector)
   1. [Connector 생명주기](#Connector 생명주기)
   1. [미리 정의된 Connector](#미리 정의된 Connector)
   1. [사용자 정의 Connector](#사용자 정의 Connector)
   1. [Connector 추가](#Connector-추가)
   1. [Selenium을 Connector로 추가하기](#Selenium을 Connector로 추가하기)
1. [xml 다루기](#xml-다루기)

## 개요
toobuk는 크롤링을 해 온 데이타를 쉽게 추출할 수 있는 도구입니다.  
1. 이미 html을  긁어올 수 있는 여러 라이브러리가 있구요.
2. html에서 의미있는 데이터를 뽑아내는 라이브러리가 존재합니다.

핵심은 데이타를 추출할 때, 로직이나 패턴이 소스에 잘 정리가 안되어 있는 경우가 많다는 거죠  
그 부분을 따로 설정 파일로 분리하는게 핵심입니다.  
경험 많은 개발자분들은 아마 mybatis를 생각하실 수도 있겠네요.  

데이타 추출은 beautifulsoup를 사용했습니다. 아래를 참조하세요.  
https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/#

## 설치
toobuk은 기본적으로 beautifulsoup4, requests 를 이용합니다.   
pip install beautifulsoup4  
pip install requests

toobuk을 설치합니다.
pip install toobuk

설치 여부 확인  
pip list  

## Get 방식으로 크롤링하기
01_get 패키지를 확인하세요.

1. 설정 파일을 만듭니다.
   파일명은 getTest.json입니다.


    {
    "housetrade" : {
                "url" : "https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=124001&idx_cd=1240&freq=Y&period=N",
                "output" : {
                            "date" : {    "type" : "list",
                                       "pattern" : [ 
                                                    {
                                                        "selector" : "#t_Table_124001 thead > tr:nth-of-type(1) > th",
                                                        "name" : "DATE"
                                                    }
                                                   ]
                                         }
                            }
                    }
    }
2.  아래 설정 파일을 읽어들여 크롤링을 합니다.  


    from toobuk import Toobuk

    htb = Toobuk('getTest') #설정 파일 getTest.json, .json은 생략
    print( htb.grumble('housetrade') ) 

단지, 크롤링할 사이트와 어떤 데이타를 읽어들일지 selector를 통해서 설정만 해주었습니다.  
아래 post 방식과 비교해보세요.


## Post 방식으로 크롤링하기
02_post 패키지를 확인하세요.

1. 설정 파일을 만듭니다.
   파일명은 post.json입니다.


    {
     "qa" : {
            "url" : "https://kosis.kr/civilComplaint/qnaList.do",
            "conn.type" : "post",
            "bs.type" : "html.parser",
            "output" : {
                        "date" : {    "type" : "list",
                                   "pattern" : [
                                                {
                                                    "selector" : ".bd_lst_tit a",
                                                    "name" : "TITLE"
                                                }
                                               ]
                                     }
                        }
                }
      }

2.  아래 설정 파일을 읽어들여 크롤링을 합니다.


    from toobuk import Toobuk
    import util as ut

    htb = Toobuk('post') #설정 파일 post.json, .json은 생략
    ut.pprint( htb.grumble('qa') )

위에 get 방식과  차이를 느끼시나요? 소스에서는 차이가 없습니다. 
단지 설정 파일에서 **conn.type**이 post로 되어 있습니다.

## Parameter 설정하기
1. 설정파일을 통해서 파라메터 정의  
   크롤링을 하면서 파라메터를 설정할 수 있습니다. 설정파일에서 parameter로 넘길 값을 설정해 주세요  
   03_parameter를 확인하세요.  

         "parameter": [
            {
            "searchKeyword": "지방",
            "searchCondition": "subject"
            },
         ]

   파라메터가 다른 값으로 하고 싶을 때가 있죠? 예를  들면 "지방" 했으니 "수도" 로도 하고 싶어요.

       "parameter": [
         {
           "searchKeyword": "지방",
           "searchCondition": "subject"
         },
         {
           "searchKeyword": "수도",
           "searchCondition": "subject"
         }
       ],

   위처럼, 파라메터가 2가지로 설정이 되어 있다면 실제로 크롤링을 하기 위해서 2번 사이트에 접속을 하게 됩니다.  
   파라메터가 n개라면 n번 되겠죠.
   parameter.py를 실행해보시면 차이를 느끼실 수 있을겁니다.

1. 소스에서 파라메터 정의
   소스에서 파라메터를 넘기고 싶은 경우도 있습니다. 웹에서 select 를 통해 값을 넘겨 받거나, 
   크롤링을 해온 값을 읽어서 다시 다른 페이지를 크롤링하면서 파라메터를 넘길 수 있죠. 그럴 때는 소스에서 파라메터를 넘기면 됩니다.

   
      parameter = {
          "searchKeyword": "주택",
          "searchCondition": "subject"
      }
      ut.pprint( htb.grumble('empty.param', parameter) )

   위를 표현할때 get방식과 post 방식에서 약간 차이가 있습니다. get 방식에서는 url에서 해당값을 알려줘야 해요.
   ### get
   아래 url 부분을 유심히 보시죠.

        "get" : {
          "url" : "https://kosis.kr/civilComplaint/qnaList.do?searchKeyword=#searchKeyword#&searchCondition=#searchCondition#",
          "conn.type" : "get",
          "bs.type" : "html.parser",
          "parameter": [
            {
              "searchKeyword": "지방",
              "searchCondition": "subject"
            },
            {
              "searchKeyword": "수도",
              "searchCondition": "subject"
            }
   ### post
   반면 post는 url만 적으면 됩니다.

        "post" : {
          "url": "https://kosis.kr/civilComplaint/qnaList.do",
          "conn.type": "post",
          "bs.type": "html.parser",
          "parameter": [
            {
              "searchKeyword": "지방",
              "searchCondition": "subject"
            },
            {
              "searchKeyword": "수도",
              "searchCondition": "subject"
            }
          ],

   ### output 구성
   parameter를 설정한 경우와 설정하지 않은 경우 output 구성에서 차이가 있습니다.  
   parameter 설정한 경우, 아래처럼 parameter에서 설정한 key, value가 output에 그대로 실려 있습니다.  
   반면, parameter가 없는 경우 'data' 값만 있습니다.

      {   'search': [   {   'data': [   {   'CNT': '111',
                                      'TITLE': '행정안전부 지방자치단체 외국인주민 현황 관련 문의'},
                                  {'CNT': '104', 'TITLE': '2016년 시군구별 지방교부세'},
                                  ...
                                   ],
                      'searchCondition': 'subject',
                      'searchKeyword': '지방'},

## Output 설정하기
   크롤링 한 데이타(html 소스)에서 의미있는 데이타를 추출행 합니다. 어떤 상세 정보일 경우 **단일건**으로 읽어들여야 하고, 리스트 형식인 경우 **배열**로 읽어들여야 합니다.
   ([List/Single 데이타 추출](#List/Single-데이타-추출) 참조)
   그리고  읽어온 데이타에서 가공을 해야 하는 경우도 있겠죠. (  [읽어온 데이타 skip 하기](#읽어온-데이타-skip-하기) / [변환하기](#변환하기) 참조)  

   ### Output 설정하기
   04_output을 보세요.  
   보시는 것처럼 output key값으로 output을 정의해 나가면 됩니다. 
   소스에서는 date와 changeRate 2개가 output으로 설정이되어 있습니다. 

    {
    "housetrade" : {
                "url" : "https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=124001&idx_cd=1240&freq=Y&period=N",
                "bs.type" : "html.parser",
                "output" : {
                            "date" : {    "type" : "list",
                                       "pattern" : [
                                                    {
                                                      "selector" : "#t_Table_124001 thead > tr:nth-of-type(1) > th",
                                                      "name" : "DATE",
                                                      "skip": "white",
                                                      "converter" : "regx(regx=\"(?P<YYYY>\\d{4})(?P<MM>\\d{2}).\", replace=\"\\g<YYYY>-\\g<MM>\")"
                                                    }
                                                   ]
                                         },
                    "changeRate" : {     "type" : "list",
                                        "pattern" : [
                                                     {
                                                        "selector" : "#t_Table_124001 thead > tr:nth-of-type(1) > th",
                                                        "name" : "DATE",
                                                       "skip": "slice(sa={ 'start': 1})",
                                                       "converter" : "regx(regx=\"(?P<YYYY>\\d{4})(?P<MM>\\d{2}).\", replace=\"\\g<YYYY>-\\g<MM>\")"
                                                    }, {
                                                        "selector" : "#t_Table_124001 tbody > tr:nth-of-type(1) > td",
                                                        "name" : "COUNTRY",
                                                        "converter" : "float"
                                                    }, {
                                                        "selector" : "#t_Table_124001 tbody > tr:nth-of-type(2) > td",
                                                        "name" : "CAPATIAL",
                                                        "converter" : "float"
                                                    }, {
                                                        "selector" : "#t_Table_124001 tbody > tr:nth-of-type(3) > td",
                                                        "name" : "SEOUL",
                                                        "converter" : "float"
                                                    }, {
                                                        "selector" : "#t_Table_124001 tbody > tr:nth-of-type(4) > td",
                                                        "name" : "SOUTH",
                                                        "converter" : "float"
                                                    }, {
                                                        "selector" : "#t_Table_124001 tbody > tr:nth-of-type(5) > td",
                                                        "name" : "NORTH",
                                                        "converter" : "float"
                                                    }
                                                    ]

                                    }
                            }
                }
        }

   ### Output 전체 가져오기
   output에 정의된 모든 값을 추출하는 방법은 간단합니다. 우리가 그 동안 해왔죠.

      htb = Toobuk('output')
      htb.grumble('housetrade')
   ### Output 하나만 가져오기     
   output 에서 단 하나만 가져오려면. /를 하고 output명을 적어주시면 됩니다.
      
      htb.grumble('housetrade/date')
   ### Output 여러개 가져오기
   output 에서 단 하나만 가져오려면. /를 하고 output명을 &로 적어주시면 됩니다.

      htb.grumble('housetrade/date&changeRate') 
  
위 설정 파일에서 skip, converter 같은 좀 생소한 key명은 아래서 확인하실 수 있습니다.
   

## List/Single 데이타 추출
   output을 설정하면서 일어온 값을 List(배열)로 읽어올지, Single(단일건)으로 읽어올지 설정해야 합니다.  
   05_list_single 를 보세요  

### List로 추출하기
   output 설정시, type을 list로 하시면 됩니다.

      "qaList": {
        "type": "list",
        "pattern": [
          {
            "selector": ".bd_lst_tit a",
            "name": "TITLE"
          }
        ]
      }
      
   ### Single로 추출하기
   output 설정시, type을 single 로 설정하시면 됩니다.

      "qaInfo": {
        "type": "single",
        "pattern": [
          {
            "selector": ".totals",
            "name": "totle"
          },
          {
            "selector": ".counts",
            "name": "count"
          }
        ]
      }
## Output 추출 패턴 적용하기
   ### text값 가져오기
   아래처럼 선언된 태그 안에서 사용된 text 문자열입니다. 아래를 보시면 text 가 text 값이되며 01_get 소스를 보시면 
     
      <p>text</p>

   01_get 소스르 보시면, 아래와 같이 selector오 name이 있습니다. 이와 같이 되면 text값을 가져올 수 있습니다. 
   그리고 아래  [속성값 가져오기](#속성값-가져오기) 사용할 수 있는 방법이 있숩니다.

                  "output" : {
                        "date" : {    "type" : "list",
                                   "pattern" : [
                                                {
                                                    "selector" : "#t_Table_124001 thead > tr:nth-of-type(1) > th",
                                                    "name" : "DATE"
                                                }
                                               ]
                                     }
                        }
                }
   ### 속성값 가져오기
   속성값을 가져올 수도 있겠죠. 아래 태그에서 data-index 값을 가져오고 싶다면 어떻게 해야 하까요?  
            
      <th data-id="t124001_h_0" item-id="202312M" data-index="0" data-name="td_124001_cc_0" class="tc" data-headers="td_124001_cc_0" rowspan="1">2023<br>12월</th>

   04_output 에서 other로 선언된 output을 보시기 바랍니다.  
   target 이라는 이름으로 배열을 요소로 attr으 태그에서 가져오려는 속성명을 name은 뽑아온 후, 사용할 명을 선언하고 있습니다.
   attr이 __text__인 경우는 위에 [text값 가져오기](#text값-가져오기)와 같습니다. 즉, text도 가져오고 속성도 가져오고 싶은 경우 사용하면 되는 거죠.

                                  "other" : {    "type" : "list",
                                       "pattern" : [
                                                    {
                                                      "selector" : "#t_Table_124001 thead > tr:nth-of-type(1) > th",
                                                      "target" : [ {
                                                        "attr" :  "__text__",
                                                        "name": "date",
                                                        "converter" : "regx(regx=\"(?P<YYYY>\\d{4})(?P<MM>\\d{2}).\", replace=\"\\g<YYYY>-\\g<MM>\")"
                                                      },  {
                                                        "attr" :  "data-index",
                                                        "name": "index"
                                                      }


## 읽어온 데이타 skip 하기
위 내용을 보며 눈치채셨지요. 사실, 소스 수정은 최소한이며 대부분은 설정 파일을 통해 제어됩니다.   
이번 단락에서는 읽어온 데이타 중 일부는 skip 하는 기능에 대하여 알아보겠습니다.  
skip은 [List로-추출하기](#List로-추출하기)에서만 가능합니다. 사실 Single 에서는 단일 row이기에 skip이 의미가 없습니다.  
06_skip를 보시기 바랍니다.

일단, 아래 주소를 확인해보시죠.
https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=124001&idx_cd=1240&freq=Y&period=N

   ### 미리 정의된 skip
   저는 지금 해당 html에서 날짜를 가져오려 합니다. YYYYMM월 형식이군요. selecor를 아래처럼 하겠습니다.

      "pattern": [
					{
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE"
					}
				]
   저렇게 하니, 맨 앞에 공백이 있는 th까지 가져오네요. 이를 보완하기 위한 여러가지 방법이 있겠지만, 저는 미리 skip 기능을 사용하겠습니다.

   #### slice
   slice는 가져올 부분을 잘라냅니다. start는 시작을 end는 끝을. start만 적으면 start부터 끝까지, end만 적는다면 시작부터 end까지입니다.
      
   start만  

      "pattern": [
					{
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE",
						"skip": "slice(sa={ 'start': 1})"
					}

   end만

      "pattern": [
					{
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE",
						"skip": "slice(sa={ 'end': 3})"
					}
				]
   start, end

      "pattern": [
					{
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE",
						"skip": "slice(sa={ 'start':1, 'end': 3})"
					}
				]

   start, end를 여러개 적을 수도 있습니다.

      "pattern": [
					{
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE",
						"skip": "slice(sa=[{'start': 1, 'end': 2}, {'start': 11, 'end': 13} ])"
					}
				]

#### white 공백문자 skip 
   하지만 white 공백문자는 미리 정의된 skip 함수가 있습니다.

				"pattern": [
					{
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE",
						"skip": "white"
					}
				]

### skip 함수 추가
   미리 정의된 skip 함수는 여러가지로 부족할 수 있습니다. 그리고 그걸 다 만들어놓을 수도 없죠. 
   사용자 skip 함수를 만들 수도 있습니다. 그리고 그걸 재사용이 많다면 미리 등록해 놓고 쓸 수 있죠.

				"pattern": [
					{
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE",
						"skip": "skipJan"
					}
				]

   소스에서 skipJan을 미리 등록합니다.

      import func as fn

      Skipper.addSkipper('skipJan', fn.skipJan )
      htb = Toobuk('skip1')
      ut.pprint(htb.get('trade'))

   skipJan 함수는 아래와 같습니다. 그냥 1월은 skip 하네요.
      
      def skipJan(text, r) :
         return text[4:6] == "01";

### skip 사용자 정의 함수 사용
   재사용까지는 필요없는 경우 아래처럼 사용하셔도 됩니다. 물론, 미리 등록해놓고 쓰는게 더 낫긴하죠.

				"pattern": [
					{
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE",
						"skip": "func.skipFunc1"
					}
				]

  위에 정의한 skipFunc1 내용은 아래와 같습니다.

      def skipFunc1(text, r) :
         return text == '\xa0'

   간단하죠. text는 읽어온 selector text 내용이고 r은 결과물입니다. r은 거의 신경쓰시지 않아도 됩니다.

   06_skip를 확인해주세요.


### 여러 skip을 같이 사용하기
   여러 skipper를 같이 사용할 수 있습니다.

				"pattern": [
					{
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE",
						"skip": "slice(sa={ 'start': 0, 'end':5 }),white,skipJan"
					}
   slice를 skipJan 뒤로 옮기면 결과는 달라집니다.



## 변환하기
이번 단락에서는 읽어온 데이타를 변환하는 기능에 대해서 알아보겠습니다.  
사실, 사용법은 [읽어온 데이타 skip 하기](#읽어온-데이타-skip-하기)와 대동소이합니다.  
07_converter 를 보시기 바랍니다.

일단, 아래 주소를 확인해보시죠.
https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=124001&idx_cd=1240&freq=Y&period=N

### 미리 정의된 변환기
저는 지금 해당 html에서 날짜를 가져오려 합니다. YYYYMM월 형식이군요. selecor를 아래처럼 하겠습니다.

      "pattern": [
					{
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE",
						"skip": "white"
					}
				]

결과는 아래와 같습니다.
      
        [{'DATE': '202312월'}, {'DATE': '202401월'},....

설정 파일에 converter 옵션을 추가했습니다.

           {
               "selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
               "name": "DATE",
               "skip": "white",
               "converter" : "regx(regx=\"(?P<YYYY>\\d{4})(?P<MM>\\d{2}).\", replace=\"\\g<YYYY>-\\g<MM>\")"
           }
결과는 아래와 같습니다.

      [   {   'DATE': '2023-12',...

#### currency
세자리 숫자마다 ,(콤마)를 찍어줍니다.

#### remove.comma
, 제거

#### int
int로 변환

#### float
float로 변환

#### 정규식
정규식을 사용해서 변환합니다. 아래 예제를 보면 두가지 옵션이 있습니다. regx와 replace

           {
               "selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
               "name": "DATE",
               "skip": "white",
               "converter" : "regx(regx=\"(?P<YYYY>\\d{4})(?P<MM>\\d{2}).\", replace=\"\\g<YYYY>-\\g<MM>\")"
           }


### 변환기 추가
미리 정의된 converter 함수는 여러가지로 부족할 수 있습니다. 그리고 그걸 다 만들어놓을 수도 없죠.
사용자 converter 함수를 만들 수도 있습니다. 그리고 그걸 재사용이 많다면 미리 등록해 놓고 쓸 수 있죠.

            {
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE4",
						"skip": "white",
						"converter": "dateformat"
					}

소스에서 dateformat을 미리 등록합니다.

      import func as fn

      Converter.addConverter("dateformat", fn.dateformat)

      htb = Toobuk('converter')
      ut.pprint(htb.get('trade'))

dateformat 함수는 아래와 같습니다. 위에서 본 정규식과 차이는 없지만, 다른 방식으로 유용할 듯 합니다.

      def dateformat(text, r) :
          regx = re.compile(r"(?P<YYYY>\d{4})(?P<MM>\d{2}).")
          replace = "\\g<YYYY>-\\g<MM>"

          return regx.sub(replace, text)

### 변환기 사용자 정의 함수 사용
재사용까지는 필요없는 경우 아래처럼 사용하셔도 됩니다. 물론, 미리 등록해놓고 쓰는게 더 낫긴하죠.

       {
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE3",
						"skip": "white",
						"converter": "func.dateformat"
					}

위에 정의한 dateformat 내용은 아래와 같습니다.

      def dateformat(text, r) :
          regx = re.compile(r"(?P<YYYY>\d{4})(?P<MM>\d{2}).")
          replace = "\\g<YYYY>-\\g<MM>"

          return regx.sub(replace, text)

간단하죠. text는 읽어온 selector text 내용이고 r은 결과물입니다. r은 거의 신경쓰시지 않아도 됩니다.

07_converter 확인해주세요.


### 변환기 여러개 사용하기
여러 converter를 같이 사용할 수 있습니다.
skip을 이용하여 whitespace 문자열은 건너띄고, 
1. 처음 regx는 숫자가 아닌 문자는 모두 지우고
2. 두번째 regx는 문자 맨 끝에 .을 추가하였으며
3. float를 이용하여 float로 변환하였습니다.


       {
						"selector": "#t_Table_124001 thead > tr:nth-of-type(1) > th",
						"name": "DATE2",
						"skip": "white",
						"converter" : "regx(regx='\\D', replace=''), regx(regx='$', replace='.'), float"
					}

## 크롤링 여러번 하기:페이징처리 크롤링
페이징 처리는 어떻게 할까요? 여러 페이지에 걸쳐서 페이징처리를 해야 하는 경우,  
toobuk에서는 페이지 번호를 지정할 수 있습니다.  
크롤링하고자 하는 페이징 정보를 줄 수 있죠. 
아래 내용을 보시죠.  
소스는 08_for_loop를 확인하세요


      "paging" : {
            "url" : "https://kosis.kr/civilComplaint/qnaList.do",
            "conn.type" : "post",
            "bs.type" : "html.parser",
            "for" : { "type" :  "number", "name" : "pageIndex","start": 1, "end": 2},

output을 설정해서 뽑아낼 데이타를 지정할 수 있습니다.

                  "output" : {
                        "qaList" : {    
                            "type" : "list",
                            "pattern" : [
                                        {
                                            "selector" : ".bd_lst_tit a",
                                            "name" : "TITLE"
                                        }, 
                                        {
                                           "selector" : ".bd_lst_tbl > tbody td:nth-of-type(6)",
                                           "name" : "CNT"
                                         }
                                        ]
                                    }
                        }
그리하여 아래는 전체 설정입니다.

      "paging" : {
            "url" : "https://kosis.kr/civilComplaint/qnaList.do",
            "conn.type" : "post",
            "bs.type" : "html.parser",
            "for" : { "type" :  "number", "name" : "pageIndex","start": 1, "end": 2},
            "output" : {
                        "qaList" : {
                            "type" : "list",
                            "pattern" : [
                                        {
                                            "selector" : ".bd_lst_tit a",
                                            "name" : "TITLE"
                                        },
                                        {
                                           "selector" : ".bd_lst_tbl > tbody td:nth-of-type(6)",
                                           "name" : "CNT"
                                         }
                                        ]
                                    }
                        }
                },
결과를 확인해볼까요?

      {   'qaList': [   
               {'CNT': '13', 'TITLE': '세대별 주민등록인구'},
               {'CNT': '228', 'TITLE': '보건> 건강 보험 2023, 2024 통계 자료'},
               {   'CNT': '236',
               'TITLE': '성/활동상태별 비경제활동인구 통계 자료에 사라진 구간이 있습니다.'},
               {'CNT': '272', 'TITLE': '2025년 중위소득에 따른 건강보험료 금액문의'},
               .... ]

   ### 파라메터 설정 후, 페이징처리하기
   위 설정에서 파라메터 설정을 추가해주면 됩니다.
   
          "parameter" :  [{"searchKeyword": "도시", "searchCondition": "subject"}, {"searchKeyword": "수도", "searchCondition": "subject"}],
          "for" : { "type" :  "number", "name" : "pageIndex","start": 1, "end": 2},

### Connector
   Connector는 실제로 사이트에 접속을 해서 html을 읽어옵니다.  
   보통 get방식으로 읽어오지만, post로도 접속이 가능합니다.  
   혹시, put이나 delete 도 가능한지 물어보신다면, [사용자 정의 Connector](#사용자-정의-Connector)로 직접 구현할 수 있습니다.
   그리고 Selenium 역시 Connector로 구현할 수 있습니다.

   아래 코드를 봐주세요.
   https://github.com/ramoi/toobuk/blob/master/toobuk/connector_v1.py

   AbstractConnector 가 Connector 에서 사용하는 추상클래스입니다.  
   여러분이 Connector를 직접 구현하시려면 해당 클래스를 상속받아야 합니다.

   Toobuk에서는 AbstractConnector를 상속받는 2개의 Connector가 있습니다.
   GetConnector, PostConnector

### Connector 생명주기
   Connector는 3단계로 진행이 됩니다.
   1. beforeConnect(self, headers, parameter)
      connect 이전 단계이며, 해당 함수에서 headers나 parameter를 수정하거나 db에 로그를 남기는 작업등을 할 수 있습니다.
   2. connect(self, url, headers, parameter)
      해당  메소드에서 실제로 html을 읽어옵니다.  
      그리고 꼭, BeautifulSoup 객체를 리턴해야 합니다.
   3. afterConnect(self, bs)  
      해당 메소드에서 실제로 읽어온 후, 로깅작업등을 할 수 있습니다.
      그리고 꼭, BeautifulSoup 객체를 리턴해야 합니다.( 이 말은, BeautifulSoup 객체를 조작해서 리턴시켜도 된다는 말이죠.)

   AbstractConnector 클래스 get함수를 보시면 아래와 같습니다.

      def get(self, headers, parameter):
        url = self.getUrl(parameter)
        logger.debug('connect url=======>' + url)

        self.beforeConnect(headers, parameter)
        bs = self.connect(url, headers, parameter)
        bs = self.afterConnect(bs)

        return {'source': bs, 'parameter': parameter}

   getUrl 인자로 parameter를 넘기고 있습니다. 실제로 AbstractConnector 에서는 해당 메소드에서 설정 파일에 기술된, url에서 변수 처리 된 값을 parameter에서 읽어들여 매핑 시키고 있습니다.
   예를 들어 아래와 같이 url이 기술된다면.
      
      https://xxxx.xx?searchKeyword=#searchKeyword#

   #searchKeyword# 부분에서 parameter에 정의된 searchKeyword를 읽어서 치환해주는 것이죠.
   AbstractConnector에서는 beforeConnect는 선언만 되어 있으며
   connect는 GetConnector에서는 get 방식으로 PostConnector에서는 post로 접속을 합니다.
   afterConnecgt에서는 인자로 받은 bs(connect 함수에서 생성된 BeautifulSoup 객체)를 그대로 리턴합니다

   ### 미리 정의된 Connector
   1. GetConnector  
      get 방식
   2. PostConnector  
      post 방식

   ### 사용자 정의 Connector
   09_connector 소스를 봐주세요
   connectorTest.py 소스를 그대로 옮기면 아래와 같습니다.

      class CustomGetConnector(AbstractConnector):
          def beforeConnect(self, headers, parameter):
              logger.debug(parameter)

          def afterConnect(self, bs):
              logger.debug(bs)
              return bs

          def connect(self, url, headers, parameter):
              html = urlopen(url)
              logger.debug(html)

              bs = BeautifulSoup(html, self._bsType_, from_encoding=self._encoding_ )

              return bs

   AbstractConnector를 상속받고 있습니다  
   beforeConnect, afterConnect 에서는 로깅처리를 하고 있으며(Toobuk에서는 그냥 pass처리 하고 있습니다.)  
   connect에서 사이트에 접속 후, html을 읽어와서 BeautifulSoup로 리턴하고 있습니다.
   Connector를 만드는 방법은 이게 끝입니다. 설정은 아래

      "housetrade" : {
            "url" : "https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=124001&idx_cd=1240&freq=Y&period=N",
            "bs.type" : "html.parser",
            "conn.type" : "connectorTest.CustomGetConnector",

   ### Selenium을 Connector로 추가하기
   10_selenium을 봐주세요.  
   우리가 selenium을 사용하기 위해선 Connector를 상속받아서 구현해야 합니다.  
   그리고 07_connector에서 기술한 메소드 중에서 connect 메소드를 구현해 주시면 됩니다.  
   seleniumTest.py룰 보시면, Connector 2개를 구현했습니다.  
   SeleniumConnector는 그냥 페이지에 접속해서 html을 얻어오고 있구요. 사실, 그냥 Get을 사용하는 것과 차이가 없숩니다.
   
   SeleniumLoopConnector 를 보시면 더보기 버튼을 2번더 클릭 후, 전체 내용을 가져오고 있습니다.
   소스에서 아래 부분울 유심히 봐주세요.
   * driver.find_element(By.CSS_SELECTOR, '#newsListMore').click() *
   
      class SeleniumLoopConnector(AbstractConnector):

          def connect(self, url, headers, parameter):

              # 이게 pc에 설치되어있는 chrome을 제어하는거라서 그냥 실행시키면 창이 나오고
              # 입력되고 하는게 다 보인다.
              # headless option을 주어서 background에서 실행이 되도록 하자
              driver_options = webdriver.ChromeOptions()
              driver_options.add_argument("headless")
              driver = webdriver.Chrome()
              driver.get(url)

              # while True :
              for i in range(10):
                  print('idx==================>>', i)
                  bs = BeautifulSoup(driver.page_source,  self._bsType_, from_encoding=self._encoding_ )
                  dateList = bs.select('.newsContents  .tit_section')

                  if len(dateList) > 3:
                      # driver.execute_script("""
                      # document.querySelector('.newsContents .head_section:nth-child(n+2) + .list_newsinfo').remove();
                      # """)
                      # bs = BeautifulSoup(driver.page_source, self._json_['bs.type'],
                      #                    from_encoding='utf-8' if self._json_.get('encoding') is None else self._json_[
                      #                        'encoding'])

                      return bs
                  driver.find_element(By.CSS_SELECTOR, '#newsListMore').click()

              # 잊지말고 동작이 끝나면 driver을 종료할것!
              driver.quit()
              return bs


## xml 다루기
형식이 html이 아닌 xml인 경우도 역시 크롤링을 하여 데이타를 추출할 수 있는데요. 이 부분 역시 beautifulsoup 을 참조하시면 됩니다
https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/#

      pip install lxml


11_xml 소스를 참조하세요.  
bs.type이 xml로 설정되어 있습니다. 그리고 outout pattern에서 뽑아내고자 하는 값을 적용하면 됩니다.


      {
      "euroDaily" : {
                  "url" : "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml",
                  "bs.type" : "xml",
                  "output" : {
                              "curr" : {    "type" : "list",
                                         "pattern" : [
                                                      {
                                                          "selector" : "Cube Cube Cube",
                                                          "target": [
                                                            "currency,
                                                            { "name" : "rate", attr:"rate", converter:
                                                            ]
                                                      }
                                                     ]
                                           }
                              }
                      }
      }

