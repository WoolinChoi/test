---
layout: post
title: jqueryProxy
category: ajax
tags: [java, ajax, jqueryProxy]
comments: false
---

# [jqueryProxy]()

## Page
~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Page</title>
	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
	<script type="text/javascript">
		$(function(){
			// 네이버 버튼을 눌렸을 때
			$("#naver").click(function(){
				// 축약형
// 				$.post("./jsp/ProxyNaver.jsp", function(data){
// 				});
				
				$.ajax({
					type : "POST",
					url : "./jsp/ProxyNaver.jsp",
					success : function(data){
						// $("xxxx", data) data에서 xxxx를 찾기
						var rank = $(".PM_CL_realtimeKeyword_rolling", data);
						$("#result").empty();
						$("#result").append(rank);
					} // success-end
				}); // ajax-end	
			}); // click-end
			
			// 멜론 버튼을 눌렀을 때
			$("#melon").click(function(){
				$.ajax({
					type : "POST",
					url : "./jsp/ProxyMelon.jsp",
					success : function(data){
						var chart = $(".typeRealtime>ul>li", data);
						// rsult부분을 empty로 지워준다.
						$("#result").empty();
						chart.each(function(){
							// 태그와 태그 사이에 있는 글자는 text로 얻어오고 이미지는 html로 얻어온다. 내 위치에서 찾기위해 this를 쓴다.
							var rank = $(".rank", this).text();
							var title = $(".song", this).text();
							var img = $(".mlog", this).html();
							// result부분에 append로 붙혀 준다.
							$("#result").append(img + rank + "위" + title + "<br/>");
						});	// each-end
					} // success-end
				}); // ajax-end
			}); // click-end
			
			// 다음 버튼을 눌렀을 때
			$("#daum").click(function(){
				$.ajax({
					type : "POST",
					url : "./jsp/ProxyDaum.jsp",
					success : function(data){
						$("#result").empty();
						var rank = $(".realtime_part .rank_cont:even", data);
						$("#result").append(rank);
					} // success-end
				}); // ajax-end	
			}); // click-end
			
			// 날씨 버튼을 눌렀을 때
			$('#kma').click(function(){      
				$.ajax({
					type : 'POST',
					url : './jsp/ProxyKma.jsp',
					success : drawBasic 
				}) // ajax-end
			   
				// 구글 차트
				google.charts.load('current', {packages: ['corechart', 'line']});
				google.charts.setOnLoadCallback(drawBasic);
	
				// success가 됬을 때
				function drawBasic(content) {
					var array = new Array();
					// alert($('category',content).text());
		            var data = $('data', content)
		            // alert($(data[0]).html());
		            $('#result').empty();
		            for(var i = 0; i < data.length; i++ ) {
						var hour = $(data[i]).find('hour').html();
						var temp = $(data[i]).find('temp').html();
		            	var array_sub = new Array(hour,parseInt(temp));   
						array.push(array_sub);
//							$('#result').append(hour+"시"+temp+"도"+'<br/>');   
					} // for-end 
				
					var data = new google.visualization.DataTable();
					data.addColumn('string', 'hour');
					data.addColumn('number', 'temp');
				      
					data.addRows(array);
					var options = {'title':'서초구 시간별 온도',
						'width':1000,
						'height':400,
						'hAxis' : {
							'title': 'Hour'
						},
						'vAxis' : {
							'title' : 'Temp'
						}
					};
					var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
					chart.draw(data, options);
				} // drawBasic-end
			}); // click-end
		}); // function-end
	</script>
</head>

<body>
	<h1>선택</h1>
	<button id="naver">네이버</button>
	<button id="melon">멜론</button>
	<button id="daum">다음</button>
	<button id="kma">날씨</button>
	<div id="result"></div>
	<div id="chart_div"></div>
</body>
</html>
~~~

## ProxyNaver
~~~jsp
<%@ page contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:import url="https://www.naver.com/"></c:import>
~~~

## ProxyMelon
~~~jsp
<%@ page contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:import url="https://www.melon.com/"></c:import>
~~~

## ProxyDaum
~~~jsp
<%@ page contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:import url="https://www.daum.net/"></c:import>
~~~

## ProxyKma
~~~jsp
<%@ page contentType="text/xml; charset=UTF-8"
    pageEncoding="UTF-8"%><%@ taglib uri="http://java.sun.com/jsp/jstl/core" 
    prefix="c" %><c:import url="http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1165066000"></c:import>
~~~