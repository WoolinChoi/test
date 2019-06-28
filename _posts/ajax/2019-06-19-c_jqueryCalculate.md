---
layout: post
title: jqueryCalculate
category: ajax
tags: [java, ajax, jqueryCalculate]
comments: false
---

# [jqueryCalculate]()

## CalcFormJson
~~~html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>ACalcFormJson</title>
	<script type="text/javascript" src="../02_jquery_ajax_basic/libs/jquery-1.9.1.min.js"></script>
	<script type="text/javascript">
		$(function(){
			// #### javascript
/*
			document.forms[0].onsubmit = function(){
				alert("ok");
				return false; // 기존의 submit 이벤트 기능 막음
			}
*/			
			// ##### jquery
			$("form").submit(function(){
				$.ajax({
					type : "GET",
					url : "./jsp/calc-action.jsp",
					data : {
						"op1" : $("#op1").val(),
						"op2" : $("#op2").val(),
						"opr" : $("#opr").val() 
					},
					dataType : "text",
					success : function(data){
						$("#result").text(data);
					},
					error : function(e){
						alert("error" + e);
					}
				});
				return false;
			});
		});
	</script>
</head>

<body>
	<form action="./jsp/calc-action.jsp" method="get">
	<input name="op1" id="op1" size="3">
	<select name="opr" id="opr" >
		<option>+</option>
		<option>-</option>
		<option>*</option>
		<option>/</option>
		<option>%</option>
	</select>
	<input name="op2" id="op2" size="3">
	<input type="submit" value="=">
	</form>
	<fieldset>
		<legend>실행결과</legend>
		<div id="result"></div>
	</fieldset>
</body>
</html>
~~~

## CalcFormJson_jsp
~~~jsp
<%@ page language="java" contentType="application/json; charset=UTF-8"
    pageEncoding="UTF-8"%>
    {
    	"op1" : ${param.op1},
    	"op2" : ${param.op2},
    	"opr" : "${param.opr}",
    	"result" : ${param.op1 + param.op2}
    }
~~~

## CalcFormXml
~~~html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>CalcFormXml</title>
	<script type="text/javascript" src="../02_jquery_ajax_basic/libs/jquery-1.9.1.min.js"></script>
	<script type="text/javascript">
		$(function(){
			// ##### jquery
			$("form").submit(function(){
				$.ajax({
					type : "GET",
					url : "./jsp/calc-action-xml.jsp",
					data : {
						"op1" : $("#op1").val(),
						"op2" : $("#op2").val(),
						"opr" : $("#opr").val() 
					},
					dataType : "xml",
					success : function(data){
						var res = $(data).find("result").text();
						$("#result").text(res);
					},
					error : function(e){
						alert("error" + e);
					}
				});
				return false;
			});
		});
	</script>
</head>

<body>
	<form action="./jsp/calc-action.jsp" method="get">
	<input name="op1" id="op1" size="3">
	<select name="opr" id="opr">
		<option>+</option>
		<option>-</option>
		<option>*</option>
		<option>/</option>
		<option>%</option>
	</select>
	<input name="op2" id="op2" size="3">
	<input type="submit" value="=">
	</form>
	<fieldset>
		<legend>실행결과</legend>
		<div id="result"></div>
	</fieldset>
</body>
</html>
~~~

## CalcFormXml_jsp
~~~jsp
<?xml version='1.0' encoding='UTF-8' ?>
<%@ page language="java" contentType="text/xml; charset=UTF-8"
    pageEncoding="UTF-8"%>
<response>
	<op1>${param.op1}</op1>
	<opr>${param.opr}</opr>
	<op2>${param.op2}</op2>
	<result>${param.op1 + param.op2}</result>
</response>
~~~

## CalcForm
~~~html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>CalcForm</title>
	<script type="text/javascript" src="../02_jquery_ajax_basic/libs/jquery-1.9.1.min.js"></script>
	<script type="text/javascript">
		$(function(){
			// ##### jquery
			$("form").submit(function(){
				$.ajax({
					type : "GET",
					url : "./jsp/calc-action-json.jsp",
					data : {
						"op1" : $("#op1").val(),
						"op2" : $("#op2").val(),
						"opr" : $("#opr").val() 
					},
					dataType : "json",
					success : function(data){
						$("#result").text(data.result);
					},
					error : function(e){
						alert("error" + e);
					}
				});
				return false;
			});
		});
	</script>
</head>

<body>
	<form action="./jsp/calc-action.jsp" method="get">
	<input name="op1" id='op1' size="3">
	<select name="opr" id='opr'>
		<option>+</option>
		<option>-</option>
		<option>*</option>
		<option>/</option>
		<option>%</option>
	</select>
	<input name="op2" id='op2' size="3">
	<input type="submit" value="=">
	</form>
	<fieldset>
		<legend>실행결과</legend>
		<div id="result"></div>
	</fieldset>
</body>
</html>
~~~

## CalcForm_jsp
~~~jsp
<%@ page language="java" contentType="application/json; charset=UTF-8"
    pageEncoding="UTF-8"%>
    {
    	"op1" : ${param.op1},
    	"op2" : ${param.op2},
    	"opr" : "${param.opr}",
    	"result" : ${param.op1 + param.op2}
    }
~~~