---
layout: post
title: dragndrop
category: javascript
tags: [java, javascript, dragndrop]
comments: false
---

# [dragndrop]()

## ChristmasView
~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>ChristmasView</title>
<link href="./css/view.css" rel="stylesheet" type="text/css">
<!-- 이벤트 확인 -->
<script src="./js/1_events.js"></script>
<script src="./js/2_events.js"></script>
<!-- 전송데이타들을 객체로 만들고 json 변환 -->
<script src="./js/3_events.js"></script>
</head>
<body>
	<div>
		<h3> 트리를 예쁘게 </h3>
		<div id="total" class='gifts'>
			<img src="./images/1.PNG" class="item" id='gift1'>
			<img src="./images/2.PNG" class="item" id='gift2' >
			<img src="./images/3.PNG" class="item" id='gift3'>
			<img src="./images/4.PNG" class="item" id='gift4' >
			<img src="./images/5.PNG" class="item"  id='gift5'>
			<img src="./images/6.PNG" class="item" id='gift6'>
			<img src="./images/7.PNG" class="item"  id='gift7'>
			<img src="./images/8.PNG" class="item" id='gift8'>
			<img src="./images/9.PNG" class="item"  id='gift9'> <!--  draggable="false" -->
		</div>
	</div>

	<div id="myPan" >
		<canvas id="tree" class="dropTarget" width='450' height='500'></canvas>
		<img id='img' src='./images/christmastree.png' width='450' height='500'/>
	</div>
</body>
</html>
~~~

## events_js
~~~java
window.onload = function(){
	// 캔버스에 트리 이미지 삽입
	var tree =  document.querySelector("#tree");
	var img = document.querySelector('#img');
	img.style.display = 'none';
	var ctx = tree.getContext("2d");
	ctx.drawImage(img, 0, 0);

	var lis = document.querySelectorAll(".item");
	var targets = document.querySelectorAll(".dropTarget");

	for(var i = 0; i < lis.length; i++){
		lis[i].addEventListener("dragstart", function(){
			console.log("drag start event");
		});
		lis[i].addEventListener("drag", function(){
			console.log("drag  event");
		});
		lis[i].addEventListener("dragend", function(){
			console.log("drag end  event");
		});
	}

	for(var i = 0; i < targets.length; i++){
		targets[i].addEventListener("dragenter", function(e){
			console.log("drag enter event");
		});
		targets[i].addEventListener("dragleave", function(){
			console.log("drag leave event");
		});
		targets[i].addEventListener("dragover", function(e){
			e.preventDefault();
			console.log("drag over event");
		});
		targets[i].addEventListener("drop", function(e){
			e.preventDefault();
			console.log("drop event");
		});
	}
}
~~~

## events_js2
~~~java
window.onload = function(){
	// 캔버스에 트리 이미지 삽입
	var tree = document.querySelector("#tree");
	var img = document.querySelector('#img');
	img.style.display = 'none';
	var ctx = tree.getContext("2d");
	ctx.drawImage(img, 0, 0);
	
	var lis = document.querySelectorAll(".item");
	for(var i = 0; i < lis.length; i++){
		lis[i].addEventListener("dragstart", function(e){
			//---------------------------------------------------
			// 전송할 데이타들을 지정한다.
			e.dataTransfer.setData("id", e.target.id);
			e.dataTransfer.setData("offsetX", e.offsetX);
			e.dataTransfer.setData("offsetY", e.offsetY);
			
			e.dataTransfer.effectAllowed = "move";
		});
	}
	
	tree.addEventListener("dragover", function(e){
		e.preventDefault();
		e.dataTransfer.dropEffect = "move";
	});
	tree.addEventListener("drop", function(e){
		e.preventDefault();
		//---------------------------------------------------
		// 전송한 데이타들을 얻어온다.
		var id = e.dataTransfer.getData("id");		
		var x = e.offsetX - e.dataTransfer.getData("offsetX");
		var y = e.offsetY - e.dataTransfer.getData("offsetY");
		
		// 전송받은 데이타를 다시 그린다.
		ctx.drawImage(document.getElementById(id), x, y);
		
		//---------------------------------------------------
		// 해당 요소를 지운다.
		document.getElementById(id).remove()
	});
}
~~~

## events_js3
~~~java
window.onload = function(){
	// 캔버스에 트리 이미지 삽입
	var tree =  document.querySelector("#tree");
	var img = document.querySelector('#img');
	img.style.display = 'none';
	var ctx = tree.getContext("2d");
	ctx.drawImage(img, 0, 0);
	
	var lis = document.querySelectorAll(".item");
	for (var i = 0; i < lis.length; i++) {
		lis[i].addEventListener("dragstart", function(e) {
			//---------------------------------------------------
			// 전송할 데이타를 객체로 만들고 Json 으로 변환하여 지정
			var dragSourceObj = {
				"id" : e.target.id,
				"offsetX" : e.offsetX,
				"offsetY" : e.offsetY
			};
			e.dataTransfer.setData("dragSource", JSON.stringify(dragSourceObj));
			e.dataTransfer.effectAllowed = "move";
		});
	}
	
	tree.addEventListener("dragover", function(e) {
		e.preventDefault();
		e.dataTransfer.dropEffect = "move";
	});
	
	tree.addEventListener("drop", function(e) {
		e.preventDefault();
		//---------------------------------------------------
		// json 데이타를 다시 객체로 파싱
		var dragSrcObj = JSON.parse(e.dataTransfer.getData("dragSource"));
		var id = dragSrcObj.id;
		var x = e.offsetX - dragSrcObj.offsetX;
		var y = e.offsetY - dragSrcObj.offsetY;
		
		ctx.drawImage(document.getElementById(id), x, y);
	});
}
~~~

## view_css
~~~css
@charset "utf-8";

#myPan {
/* 	float : right; */
}


.gifts {
	float : left;
	width : 400px;
	height : 300px;
	border: 1px solid blue;
	margin: 20px;
}

.item {
	width: 60px;
	height: 60px;
}
~~~