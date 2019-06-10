---
layout: post
title: integratedClass
category: javascript
tags: [java, javascript, integratedClass]
comments: false
---

# [integratedClass]()

## Audio
~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Audio</title>
<style type="text/css">
	input{
		width:100px;
	}
</style>
<script type="text/javascript">
	var audio = new Audio('/WebUI/media/mymusic.mp3');
	var togglePlay = function(){
		var control = document.getElementById('control');
		if(audio.paused || audio.ended){
			audio.play();
			control.innerHTML = '일시정지';
		}else{
			audio.pause();
			control.innerHTML = '재생';
		}
	}
</script>
</head>
<body>
	<!-- <audio controls> -->
	<!-- 	<source src="/WebUI/media/mymusic.mp3" type="audio/mpeg"/> -->
	<!-- </audio> -->
	
	<div id="player">
		<img src="../../images/sample/sensitive.jpg" id="img"/><br/>
		<button id="control" onclick="togglePlay()">play</button>
		<button id="mute" onclick="toggleMute()">mute</button>
	</div>
</body>
</html>
~~~

## Video
~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Video</title>
<style type="text/css">
	canvas{
			border: 1px solid #000;
	}
</style>
<script type="text/javascript">
	window.onload = function(){
		var video = document.getElementById('video');
		var canvas = document.getElementById('canvas');
		
		canvas.addEventListener('click', function(){
			var ctx = canvas.getContext('2d');
			ctx.drawImage(video, 0, 0, 320, 240)
		});
	}
</script>
</head>
<body>
	<video width="320" height="240" controls="controls"  id="video">
		<source src="../../media/myvedio.mp4" type="video/mp4"></source>
	</video>
	
	<canvas id="canvas" width="320" height="240"></canvas>
</body>
</html>
~~~

## GoogleMap
~~~html
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>GoogleMap</title>
<script type="text/javascript"
	src="http://maps.googleapis.com/maps/api/js?sensor=true"></script>
<script type="text/javascript">
	var map = null;
	window.onload = function(){
		getLocation();
		var opt = {
			center : new google.maps.LatLng(37.518877, 126.732002),
			zoom : 15,
			mapTypeId : google.maps.MapTypeId.ROADMAP
		};
		map = new google.maps.Map(document.getElementById("map"), opt);
	}

	function showLocation(position){
		var latitude = position.coords.latitude;
		var longitude = position.coords.longitude;
		alert("Latitude : " + latitude + " Longitude: " + longitude);
		var hear = new google.maps.LatLng(latitude, longitude);
		map.panTo(new google.maps.LatLng(latitude, longitude));
		var marker = new google.maps.Marker({
		    position : hear,
		    title : "I'm hear!"
		});
		marker.setMap(map);
	}

	function errorHandler(err){
		if (err.code == 1){
			alert("Error: Access is denied!");
		} else if (err.code == 2){
			alert("Error: Position is unavailable!");
		}else if(err.code == 3){
			alert("Erro : Time out");
		}
	}
	
	function getLocation(){
		if(navigator.geolocation){
			var Options = {
				timeout : 60000,
				enabledHighAccuracy : true
			};
			navigator.geolocation.getCurrentPosition(showLocation,
					errorHandler, options);
		}else{
			alert("Sorry, browser does not support geolocation!");
		}
	}
</script>
</head>
<body>
	<div id="map" style="width: 800px; height: 600px"></div>
</body>
</html>
~~~