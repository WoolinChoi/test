---
layout: post
title: bookSite
category: project
tags: [java, project, bookSite]
comments: false
---

# [bookSite]()

## BookSite
~~~html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="ko" xml:lang="ko">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta name="google-translate-customization" content="6f1073ba568f1202-9c8990a4b3025b3e-ga74e3ea243d3f01d-14"></meta> <!-- 세계 언어선택 메타 태그 -->
<title>BookSite</title>
<link rel="stylesheet" type="text/css" href="css/base.css" media="all" />
<link rel="stylesheet" type="text/css" href="css/main.css" media="all" />
<script type="text/javascript" src="js/jquery-1.10.2.min.js"></script> <!-- 제이쿼리 라이이브러리 연동 -->

<script type="text/javascript" src="js/jquery.bxslider.min.js"></script>  <!-- bxSlider 플러그인 연동 -->
<script type="text/javascript" src="js/jquery-ui-1.10.4.custom.min.js"></script> <!-- UI 플러그인 연동 -->
<script type="text/javascript" src="js/jquery.cookie.js"></script>  <!-- 쿠키 플러그인 연동 -->
<script type="text/javascript" src="js/scripts.js"></script>

</head>
<body>
<div id="wrap">
<dl class="hide">
 <dt>스킵메뉴</dt>
 <dd><a href="#container">본문바로가기</a></dd>
</dl>
<div id="header">
  <h1><a href="#"><img src="images/logo.gif" alt="이지스 퍼블리싱" /></a></h1>
  <dl id="util_menu">
     <dt class="hide">유틸메뉴</dt>
     <dd class="util_first">
        <ul>
           <li class="login_wrap">
           <a href="#">
           <img src="images/util_menu_1.gif" alt="로그인" />
           </a>
             <!-- #######				로그인 폼			 ########-->
             <form action="#" method="post" name="log_f" id="login_f">
               <fieldset>
                 <legend>로그인</legend>
                 <p class="user_id">
                    <label for="user_id">
                      <img src="images/login_title_id.gif" alt="아이디" />
                    </label>
                    <input type="text" name="user_id" id="user_id" />
                 </p>
                 <p class="user_pw">
                    <label for="user_pw">
                      <img src="images/login_title_pw.gif" alt="아이디" />
                    </label>
                    <input type="password" name="user_pw" id="user_pw" /></p>
                 <p>
                    <input type="checkbox" name="save_id" id="save_id" />
                    <label for="save_id"> 비밀번호 저장</label>
                 </p>
                 <p class="log_btn">
                    <input type="image" src="images/login_btn.gif" alt="로그인버튼" />
                 </p>
                 <p class="join_btn_wrap">
                     <a href="#">회원가입</a>
                     <a href="#" class="sch_id_btn">아이이디/비밀번호 찾기</a>
                 </p>
                 <p class="login_close_btn">
                     <a href="#">
                     <img src="images/login_close_btn.gif" alt="닫기버튼" />
                     </a>
                 </p>
               </fieldset>
             </form>
           </li>
           
           <li>
            <a href="#"><img src="images/util_menu_2.gif" alt="회원가입" /></a>
           </li>
           <li>
            <a href="#"><img src="images/util_menu_3.gif" alt="도서목록" /></a>
           </li>
           <li>
            <a href="#"><img src="images/util_menu_4.gif" alt="원고지원" /></a>
           </li>
           <li>
            <a href="#"><img src="images/util_menu_5.gif" alt="사이트맵" /></a>
           </li>
        </ul>
     </dd>
     <dd>
        <ul id="zoom">
           <li><img src="images/util_zoom_1.gif" alt="" /></li>
           <li>
            <a href="#" class="zoom_in"><img src="images/util_zoom_2.gif" alt="" /></a>
           </li>
           <li>
            <a href="#" class="zoom_return"><img src="images/util_zoom_3.gif" alt="" /></a>
           </li>
           <li>
            <a href="#" class="zoom_out"><img src="images/util_zoom_4.gif" alt="" /></a>
           </li>
        </ul>
     </dd>
     <dd>
      <a href="#" class="print_btn">
        <img src="images/util_print.gif" alt="" />
      </a>
     </dd>
     <dd>
        <div id="google_translate_element"></div>
     </dd>
  </dl>
  <form action="#" method="get" name="sch_f" id="sch_f">
     <fieldset>
        <legend>검색폼</legend>
        <p>
           <input type="text" name="keyword" id="keyword" title="검색어입력" />
           <input type="image" src="images/header_sch_btn.gif" alt="검색" />
        </p>
     </fieldset>
  </form>
  
  <!--  ######## 전체 메뉴 ########  -->
  <p id="total_btn">
      <a href="#">
        <img src="images/allmenu_btn_out.gif" alt="전체메뉴" />
      </a>
  </p>
  <div id="total_menu">
     <dl>
        <dt><img src="images/allmenu_title_1.gif" alt="홈" /></dt>
        <dd>
           <ul>
              <li><a href="#">홈으로이동</a></li>
           </ul>
        </dd>
     </dl>
     <dl>
        <dt><img src="images/allmenu_title_2.gif" alt="홈" /></dt>
        <dd>
           <ul>
              <li><a href="#">회사소개</a></li>
              <li><a href="#">출간분야</a></li>
              <li><a href="#">찾아오시는 길</a></li>
           </ul>
        </dd>
     </dl>
     <dl>
        <dt><img src="images/allmenu_title_1.gif" alt="홈" /></dt>
        <dd>
           <ul>
              <li><a href="#">신간도서</a></li>
              <li><a href="#">인기도서</a></li>
              <li><a href="#">추천도서</a></li>
           </ul>
        </dd>
     </dl>
     <dl>
        <dt><img src="images/allmenu_title_1.gif" alt="홈" /></dt>
        <dd>
           <ul>
              <li><a href="#">고객문의</a></li>
              <li><a href="#">저자문의</a></li>
              <li><a href="#">자료요청</a></li>
              <li><a href="#">자주묻는 질문</a></li>
           </ul>
        </dd>
     </dl>
     <p id="total_close">
        <a href="#">
            <img src="images/allmenu_close_btn.gif" alt="전체메뉴 닫기" />
        </a>
     </p>
  </div>
  
  <!-- ####### 날짜 출력 ########-->
  <p id="date_wrap">
      <span class="year">0000</span> 년
      <span class="month">00</span> 월
      <span class="date">00</span>일
   </p>
</div>
<hr/>

<!-- ####### 팝배너 ######## -->
<hr/>
<div id="container">
 <div id="contents_top">
   <div id="roll_banner_wrap">
     <h3><img src="images/pop_title.gif" alt="알림판" /></h3>
     <dt class="roll_btn1 roll" >
     	<a href="#" class="active"><img src="images/pop_btn_1_over.gif" alt="버튼1" /></a>
     </dt>
     <dt class="roll_btn2 roll">
     	<a href="#"><img src="images/pop_btn_2_out.gif" alt="버튼2" /></a>
     </dt>
     <dt class="roll_btn3 roll">
     	<a href="#"><img src="images/pop_btn_3_out.gif" alt="버튼3" /></a>
     </dt>
     <dt class="roll_btn4 roll">
     	<a href="#"><img src="images/pop_btn_4_out.gif" alt="버튼4" /></a>
     </dt>
     <dl>
       <dd>
          <a href="#"><img src="images/pop_banner_1.gif" alt="배너1" /></a>
       </dd>
       <dd>
          <a href="#"><img src="images/pop_banner_2.gif" alt="배너2" /></a>
       </dd>
       <dd>
          <a href="#"><img src="images/pop_banner_3.gif" alt="배너3" /></a>
       </dd>
       <dd>
          <a href="#"><img src="images/pop_banner_4.gif" alt="배너4" /></a>
       </dd>
     </dl>
     <p class="ctl_btn">
       <a href="#" class="playBtn">
        <img src="images/pop_btn_play_on.gif" alt="재생버튼" />
       </a> 
       <a href="#" class="stopBtn">
        <img src="images/pop_btn_stop_off.gif" alt="정지버튼" />
       </a>
     </p>
   </div>
   
   <!--  ########## 탭메뉴 ##########  -->
   <dl id="tabmenu">
     <dt class="tab_btn1">
        <a href="#"><img src="images/tab_btn_1_over.gif" alt="공지사항" /></a>
     </dt>
     <dd>
       <ul>
         <li>
         <a href="#">공지사항 관련된 내용입니다.</a><span>2014-03-01</span>
         </li>
         <li>
         <a href="#">공지사항 관련된 내용입니다.</a><span>2014-03-01</span>
         </li>
         <li>
         <a href="#">공지사항 관련된 내용입니다.</a><span>2014-03-01</span>
         </li>
         <li>
         <a href="#">공지사항 관련된 내용입니다.</a><span>2014-03-01</span>
         </li>
         <li>
         <a href="#">공지사항 관련된 내용입니다.</a><span>2014-03-01</span>
         </li>
       </ul>
       <p>
          <a href="#"><img src="images/tab_more_btn.gif" alt="더보기" /></a>
       </p>
     </dd>
     <dt class="tab_btn2">
        <a href="#"><img src="images/tab_btn_2_out.gif" alt="질문과답변" /></a>
     </dt>
     <dd>
       <ul>
         <li>
           <a href="#">질문과답변 관련된 내용입니다.</a>
           <span>2014-03-01</span>
         </li>
         <li>
           <a href="#">질문과답변 관련된 내용입니다.</a>
           <span>2014-03-01</span>
         </li>
         <li>
           <a href="#">질문과답변 관련된 내용입니다.</a>
           <span>2014-03-01</span>
         </li>
         <li>
           <a href="#">질문과답변 관련된 내용입니다.</a>
           <span>2014-03-01</span>
         </li>
         <li>
           <a href="#">질문과답변 관련된 내용입니다.</a>
           <span>2014-03-01</span>
         </li>
       </ul>
       <p>
          <a href="#"><img src="images/tab_more_btn.gif" alt="더보기" /></a>
       </p>
     </dd>
     <dt class="tab_btn3">
      <a href="#"><img src="images/tab_btn_3_out.gif" alt="저자문의" /></a>
     </dt>
     <dd>
       <ul>
         <li>
           <a href="#">저자문의 관련된 내용입니다.</a>
           <span>2014-03-01</span>
         </li>
         <li>
           <a href="#">저자문의 관련된 내용입니다.</a>
           <span>2014-03-01</span>
         </li>
         <li>
           <a href="#">저자문의 관련된 내용입니다.</a>
           <span>2014-03-01</span>
         </li>
         <li>
           <a href="#">저자문의 관련된 내용입니다.</a>
           <span>2014-03-01</span>
         </li>
         <li>
           <a href="#">저자문의 관련된 내용입니다.</a>
           <span>2014-03-01</span>
         </li>
       </ul>
       <p>
        <a href="#"><img src="images/tab_more_btn.gif" alt="더보기" /></a>
       </p>
     </dd>
   </dl>
   <ul id="consult_wrap">
     <li>
      <img src="images/banner_consult.gif" alt="출판상담문의 02-3235-1722" />
     </li>
     <li>
     <img src="images/banner_support.gif" alt="원고 양식 다운받기 및 지원 easy@easypub.co.kr" usemap="#support" />
       <map name="support" id="support">
         <area shape="rect" coords="9,29,126,53" href="#" alt="원고 양식 다운 받기" />
       </map>
     </li>
   </ul>
 </div>
 
 <!-- ########### 베스트북  슬라이더 #############  -->
 <div id="bestbook_zone">
   <h3>
      <img src="images/bestbook_title.gif" alt="이지스퍼블리싱 베스트 책" />
   </h3>
   <div id="best_bg">
      <ul>
        <li><a href="#"><img src="images/bestbook_list_1.png" alt="" /><span>
              <strong>책 제목</strong>책 저자
            </span></a></li>
        <li><a href="#"><img src="images/bestbook_list_2.png" alt="" />
              <span><strong>책 제목</strong>책 저자</span></a>
        </li>
        <li><a href="#"><img src="images/bestbook_list_3.png" alt="" />
              <span><strong>책 제목</strong>책 저자</span></a>
        </li>
        <li><a href="#"><img src="images/bestbook_list_4.png" alt="" />
              <span><strong>책 제목</strong>책 저자</span></a>
        </li>
        <li><a href="#"><img src="images/bestbook_list_5.png" alt="" />
              <span><strong>책 제목</strong>책 저자</span></a>
        </li>
        <li><a href="#"><img src="images/bestbook_list_6.png" alt="" />
              <span><strong>책 제목</strong>책 저자</span></a>
        </li>
        <li><a href="#"><img src="images/bestbook_list_7.png" alt="" />
              <span><strong>책 제목</strong>책 저자</span></a>
        </li>
        <li><a href="#"><img src="images/bestbook_list_8.png" alt="" />
              <span><strong>책 제목</strong>책 저자</span></a>
        </li>
        <li><a href="#"><img src="images/bestbook_list_9.png" alt="" />
              <span><strong>책 제목</strong>책 저자</span>
              </a>
       </li>
        <li><a href="#">
             <img src="images/bestbook_list_10.png" alt="" />
             <span><strong>책 제목</strong>책 저자</span></a>
        </li>
      </ul>
      <p class="prev_btn">
         <a href="#">
         <img src="images/bestbook_btn_left.png" alt="이전으로 이동" />
         </a>
      </p>
      <p class="next_btn">
         <a href="#">
         <img src="images/bestbook_btn_right.png" alt="다음으로 이동" />
         </a>
      </p>
   </div>
 </div> <!-- close of bestbook_zone -->
</div> <!-- close of container -->
</div> <!-- close of wrap -->
<hr/>
</body>
</html>
~~~

## BookSite_js
~~~java
$(function(){
	// #######[1] 날짜 출력 ########
	// 현재 날짜 가져오기
	var today = new Date();			// 현재 날짜
	var yyyy = today.getFullYear();	// 현재 년도
	var mm = today.getMonth()+1;	// 현재 월
	var dd = today.getDate();		// 현재 일
	// 가져온 날짜를 text에 붙히기
	$('.year').text(yyyy)
	$('.month').text(mm)
	$('.date').text(dd)
	
	// ########[2] 검색어폼 ########
	// 갖다대면 없어지고 마우스 때면 나타나게 한다.
	$('#keyword').mouseover(function(){
		$('#keyword').css('background-position', '0 -500px');
	}).mouseout(function(){
		$('#keyword').css('background-position', '0 0');
	});
	
	// ########[3] 탭메뉴 ########
	// 탭메뉴 지점
	var anchors = $('#tabmenu').find('dt');
	// 탭메뉴 지점의 내용
	var panelDivs = $('#tabmenu').find('dd');
	// 더보기
	var seeMore = panelDivs.children('p');
	
	// 탭메뉴 지점 첫번째 이름에 addClass를 통해 'on'붙혀준다.
	$('#tabmenu').find('dt:first').addClass('on');
	
	// 마지막지점 탭메뉴 지점에 on을 찾는다.
	var lastAnchors = anchors.filter('.on');
	// 마지막 지점의 내용의 다음꺼를 찾아준다.
	var lastPanelDivs = lastAnchors.next();

	var img_over = lastAnchors.find('img:first').attr('src');   // *_over
	var img_out = img_over.replace('_over', '_out');   // *_out
	
	// ####[*] 더보기가 눌려졌을 때 
	seeMore.click(function(){
		// 새창으로 띄우기
		var winObj = window.open(' ', 'widow-name', 'width=480, heigth=400');
		// 공지사항 더보기
		if($(this).is(seeMore.eq(0))){
			winObj.location.href = "http://www.easyspub.co.kr/12_Menu/BoardList/C200/PUB";
		// 질문과답변 더보기
		}else if($(this).is(seeMore.eq(1))){
			winObj.location.href = "http://www.easyspub.co.kr/40_Menu/QnaWrite/PUB";
		// 저자문의 더보기
		}else if($(this).is(seeMore.eq(2))){
			winObj.location.href = "http://www.easyspub.co.kr/20_Menu/BookList/PUB";
		}
	});

	// 지점을 클릭했을 때
	anchors.click(function(){
		// 마지막 지점의 removeClass를 통해 on을 지워준다.
		lastAnchors.removeClass('on');
		// 마지막 지점의 내용을 숨긴다.
		lastPanelDivs.hide();
		lastAnchors.find('img').attr('src', img_out);   // *_out 기존것.
		
		// 현재 지점에 addClass에 on을 붙혀준다.
		$(this).addClass('on');
		
		lastAnchors = $(this);
		
		img_out = lastAnchors.find('img').attr('src');   // *_out 바뀔것 원래.
		img_over = img_out.replace('_out', '_over');   // *_over 바뀔것
		lastAnchors.find('img').attr('src', img_over);
		lastPanelDivs = lastAnchors.next();
		lastPanelDivs.show();
	});

	// ########[4] 베스트북 이미지 슬라이더(bxSlider 이용) ########
    // 슬라이더 설정
    var slider = $('#best_bg > ul').bxSlider({
       minSlides : 5,    // 최소 노출 갯수
       maxSlides : 5,    // 최대 노출 갯수
       slideMargin : 10,    // 슬라이드의 간격
       slideWidth : 150,    // 슬라이드의 너비
       auto : true,    // 자동 실행 여부
       speed : 500,    // 이동 속도 설정
       moveSlides : 1,    // 슬라이드 이동 갯수
       pager: false    // 현재 위치 페이징 표시 여부 설정
    });
    // 이전버튼을 클릭하면 이전슬라이드로 전환
    $('.prev_btn').on('click', function(){
       slider.goToPrevSlide();    // 이전 슬라이드 배너로 이동
    });
    // 다음버튼을 클릭하면 다음슬라이드로 전환
    $('.next_btn').on('click', function(){
       slider.goToNextSlide();    // 다음 슬라이드 배너로 이동
    });
    // 슬라이더 왼쪽에 공간을 줌
    slider.css( 'margin-left', '10px' );
    
	// ########[5] 로그인 ########
	// 로그인  클릭
	$('.login_wrap>a').click(function(){
		// 폼의 animate() 이용하여 top 위치를 20px로 지정
		$('#login_f').animate({
			'top' : '20px'
		});
	});
	// 폼의 닫기 클릭 
	$('.login_close_btn>a').click(function(){
		// 폼의 animate() 이용하여 top 위치를 -500px로 지정
		$('#login_f').animate({
			'top' : '-500px'
		});
	});
	
	// ########[6] 전체메뉴 보이기 ########
	// 전체 메뉴 클릭
	$('#total_btn>a').click(function(){
		// 전체 메뉴 보여주기
		$('#total_menu').show(500);
	});
	// 전체 메뉴 닫기 클릭
	$('#total_close>a').click(function(){
		// 전체 메뉴 닫아주기
		$('#total_menu').hide();
	});
	
	// #######[7] 팝배너 ########
	// 팝배너 설정
	var popBanner = $('#roll_banner_wrap>dl').bxSlider({
	       minSlides : 1,	// 최소 노출 갯수
	       auto : true,		// 자동 실행 여부
	       speed : 500,		// 이동 속도 설정
	       moveSlides : 1	// 슬라이드 이동 갯수		
	});
	// 팝배너 버튼
	var bannerButton = $('#roll_banner_wrap>dt');
	var lastButtonImg = $('.roll:first').find('a');
	// 팝배너버튼을 클릭 했을 때 
	bannerButton.click(function(){
		// 숫자버튼 슬라이드부터 재생
		popBanner.goToSlide($(this).index() - 1);
		var buttonImg = $(this).find('img');
		// 지금 button _over을 _out로 변경
		buttonImg.attr('src', buttonImg.attr('src').replace('_out', '_over'));
		// 누른 button의 _out을 _over로 변경
		lastButtonImg.find('img').attr('src', lastButtonImg.find('img').attr('src').replace('_over', '_out'));
		lastButtonImg = $(this).find('a'); // 지금 버튼
	});
	// 재생버튼을 클릭할 떼
	$('.playBtn').on('click', function(){
		popBanner.startAuto();    // 슬라이드 재생
	});
	// 정지버튼을 클릭할 때
	$('.stopBtn').on('click', function(){
		popBanner.stopAuto();    // 슬라이드 정지
	});	
});
~~~