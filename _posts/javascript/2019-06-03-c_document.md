---
layout: post
title: document
category: javascript
tags: [java, javascript, document]
comments: false
---

# [document]()

## DocumentOpen
~~~html
<!DOCTYPE html>
<html>
<head>
<title>DocumentOpen</title>
<meta charset="UTF-8">
<style type="text/css">
</style>
<script type="text/Javascript">
	function show_document()
	{
// 		var irum = document.frm.userName.value;
// 		var irum = document.forms[0].userName.value;
		var irum = document.getElementById('userName').value;
// 		alert(irum);
		var result = document.getElementById('result');
		result.innerHTML = irum + '님 반갑습니다!!!';
	}
</script>
</head>
<body>
	<form name='frm'>
		당신의 이름은? <input type='text' id='userName' name='userName' size='20'>
		<input type='button' value='눌러봐' onclick='JavaScript:show_document()'>
	</form>
	<div id='result'></div>
</body>
</html>
~~~