---
layout: post
title: scrollMenu
category: jquery
tags: [java, jquery, scrollMenu]
comments: false
---

# [scrollMenu]()

## scrollMenu
~~~html
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8"/>
<title>scrollMenu</title>
<!-- js, css, jquery 지정 --> 
<link rel="stylesheet" href="css/base.css" type="text/css" media="screen"  /> 
<link rel="stylesheet" href="css/scroll.css" type="text/css" media="screen"  /> 

<script src="../lib/jquery-3.4.1.min.js" type="text/javascript"></script>
<script src="./js/jquery.js" type="text/javascript"></script>
</head>
<body>
  <div id="container">
    <div id="header">
      <h1>스타트래커!</h1>
    </div>
    <div id="content">
      <h2>
        환영합니다!
      </h2>
      <div id="navigation">
        <ul>
          <li><a href="#">처음으로</a></li>
          <li><a href="#">지금 구매!</a></li>
          <li><a href="#">스타트래커!란</a></li>
          <li><a href="#">선물 코너</a></li>
        </ul>
      </div>
      <p id="intro">		
		최고의 유명인을 추적하고 살펴볼 수 있는 <strong>스타파헤치기</strong>에 오신 것을 환영합니다. 
		최고의 유명인을 추적하고 살펴볼 수 있는 <strong>스타파헤치기</strong>에 오신 것을 환영합니다. 
		최고의 유명인을 추적하고 살펴볼 수 있는 <strong>스타파헤치기</strong>에 오신 것을 환영합니다. 
		최고의 유명인을 추적하고 살펴볼 수 있는 <strong>스타파헤치기</strong>에 오신 것을 환영합니다. 
		최고의 유명인을 추적하고 살펴볼 수 있는 <strong>스타파헤치기</strong>에 오신 것을 환영합니다. 
      </p>

      <div id="celebs">
        <h2 class="heading"> 우리 스타 보기</h2>
        <table class="data">
          <thead>
            <tr>
              <th>ID</th>
              <th>이름</th>
              <th>직업</th>
              <th>거주지</th>             
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>203A</td>
              <td>샤이니</td>
              <td>가수</td>
              <td>용인</td>
            </tr>
            <tr>
              <td>141B</td>
              <td>소녀시대</td>
              <td>가수</td>
              <td>부산</td>
            </tr>
            <tr>
              <td>2031</td>
              <td>김수현</td>
              <td>배우</td>
              <td>뉴욕</td>
            </tr>
            <tr>
              <td>007F</td>
              <td>국카스텐</td>
              <td>가수</td>
              <td>마산</td>
            </tr>
            <tr>
              <td>8A05</td>
              <td>김태희</td>
              <td>배우</td>
              <td>서울</td>
            </tr>
            <tr>
              <td>6636</td>
              <td>송혜교</td>
              <td>배우</td>
              <td>런던</td>
            </tr>
          </tbody>
        </table>
      </div>
      
    <div id="footer">
      <p>
        &copy; Copyright 2010 유명인추적 프로덕션
      </p>
    </div>

	<!-- 문서의 스크롤를 위한 '위로' 링크 -->
	<a href="#">위로</a>
    </div>
  </div>
</body>
</html>
~~~

## scrollMenu_js
~~~java
$(function(){
	$('#navigation>ul>li').hover(function(){
		$(this).animate({'paddingLeft' : '+=15px'}, 200);
	}, function(){
		$(this).animate({'paddingLeft' : '-=15px'}, 200);
	});
	
	// 퀵메뉴
	$(window).scroll(function(){
		$('#navigation').css('top', $(document).scrollTop());
	});
});
~~~

## Base_css
~~~css
body{
	font-family: "Lucida Sans Unicode","Lucida Grande",Sans-Serif;
	color: #3E3E3E;	
	font-size: 12px;
}

p{
	padding: 5px;
}

a{
	color: #3687AF;
}

h2{
	border-bottom:2px solid #015287;
	color: #D15600;
	padding-top: 10px;
	margin-top: 0;
}

#container{
	margin:0 auto;
	text-align: left;
	width: 650px;
}

#header{
	height: 60px;
	color: #172322;
	background: transparent url(../images/header-corners.png) no-repeat bottom left;
}

#header h1{
	padding:0;
	margin:0;
}

#content{
	background-color: #fff;
	padding: 0 15px 10px 15px;

} 

#intro{
	width: 450px;
}

#footer{
	background-color: #fff;
	padding:15px;
  clear: both;
}

table{
	border-collapse:collapse;
	font-size:12px;
	margin:0 20px 20px 20px;
	border-top:2px solid #015287;
	width:480px;
}

th{
	border-bottom: 2px solid #015287;
	color: #D15600;
	font-size: 14px;
	font-weight: normal;
	text-align: left;
	padding: 3px 8px;
}

td{
	padding: 6px;
}

/* li요소를 오른쪽으로 배치 */
#navigation{
	float: right;
	width: 150px;
}


/*-----------------------------------------------------*/
/* jquery로 클래스를 추가하기 위한 CSS 클래스 */
/*-----------------------------------------------------*/
/* 테이블에 줄바꿔 스타일 지정할 때 */
.table_striping{
	background-color : #dddddd;
	color : #666666
}	

/*-----------------------------------------------------*/
/* 테이블에 마우스 오르면 강조 */
tr.td_mouseover{
	background-color : #fffacd;
}
~~~

## Scroll_css
~~~css
/* intro 문단에 스크롤 만들기 */
#intro{
	height : 100px;
	width : 400px;
	overflow : scroll;
}

/* 내비게이션 메뉴를 움직이는 것처럼 보이게 */
#navigation{
	position : relative;
}


#content{
	height : 1000px;
}
~~~