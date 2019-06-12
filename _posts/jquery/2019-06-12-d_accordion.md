---
layout: post
title: accordion
category: jquery
tags: [java, jquery, accordion]
comments: false
---

# [accordion]()

## Accordion
~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>jQuery test</title>
<link rel="stylesheet" type="text/css" href="css/styles.css" />
<script src="../lib/jquery-3.4.1.min.js"></script>
<script src="./js/jquery.js"></script>
</head>
<body>
	<dl class="accordion">
		<dt>하나</dt>
		<dd>당신은 전세계3%의 인간이다. 거리를 마음껏 걸어다닐 수 있으며, 국토에 바다가 있고, 초고속인터넷이 있으며,눈이있다. </dd>
		<dt>둘</dt>
		<dd>오늘걸으면 내일은 뛰어야 하지만 오늘뛰면 내일은 걷는다.일찍일어나는 새가 벌레를 잡지만, 일찍일어난 벌레는 새한테 죽는다.
		</dd>
		<dt>셋</dt>
		<dd>1. 포기란 김장할때 쓰는 말이다.   2. 남자는 얼굴보다 돈   3. 10분만 공부 더하면 남편얼굴 바뀐다.     4. 미쳐야 공부할맛 난다.     5. 부러질 지언정 굽히지는 않는다.      6. 인생 한방이다.       7. 원인을 밝혀라 (  , 좋은일이든 나쁜일이든 원인을 밝혀 내가 잘못된 것을 확인하는 차원 )      8. 잡초같은 인생 살자 ( , 잡초는 누가 심어주지 않아도 , 생명력이 강하여 혼자 살수 있기 때문에 )
		</dd>
	</dl>
	<dl class="accordion">
		<dt>하나</dt>
		<dd>당신은 전세계3%의 인간이다. 거리를 마음껏 걸어다닐 수 있으며, 국토에 바다가 있고, 초고속인터넷이 있으며,눈이있다. </dd>
		<dt>둘</dt>
		<dd>오늘걸으면 내일은 뛰어야 하지만 오늘뛰면 내일은 걷는다.일찍일어나는 새가 벌레를 잡지만, 일찍일어난 벌레는 새한테 죽는다.
		</dd>
		<dt>셋</dt>
		<dd>1. 포기란 김장할때 쓰는 말이다.   2. 남자는 얼굴보다 돈   3. 10분만 공부 더하면 남편얼굴 바뀐다.     4. 미쳐야 공부할맛 난다.     5. 부러질 지언정 굽히지는 않는다.      6. 인생 한방이다.       7. 원인을 밝혀라 (  , 좋은일이든 나쁜일이든 원인을 밝혀 내가 잘못된 것을 확인하는 차원 )      8. 잡초같은 인생 살자 ( , 잡초는 누가 심어주지 않아도 , 생명력이 강하여 혼자 살수 있기 때문에 )
		</dd>
	</dl>
</body>
</html>
~~~

## Accordion_Js
~~~java
$(function(){
	$('.accordion').each(function(){
		var allDt = $(this).find('dt');
		var allDd = $(this).find('dd');
		
		allDd.hide();
		allDt.css('cursor', 'pointer');
		
		allDt.click(function(){
//			allDd.hide();
//			$(this).next().show();
			$(this).next().toggle();
		});
	});
});
~~~

## Accordion_Css
~~~css
*{
	margin:0;
	padding:0;
	line-height:1.4;
}

body{
	padding:40px;
	font-family:Arial, Helvetica, sans-serif;
}

dl{
	width:320px;
	margin:0 0 20px;
}

    dt{
            padding:6px 10px 6px;
            background:#444 url('../imgs/bg.png') repeat-y 100% 0;
            color:#fff;
            margin:0 0 3px;
            font-weight:bold;
            border-radius:8px 0 0 0;
            border-left:2px solid #444;
            border-top:2px solid #444;
    }
        
    dd{
            padding:8px 10px 12px;
            width:298px;
            border-left:2px solid #444;
            background:#eee;
            margin:-3px 0 3px;
    }
~~~