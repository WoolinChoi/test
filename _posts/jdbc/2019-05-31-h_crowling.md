---
layout: post
title: crowling
category: jdbc
tags: [java, jdbc, crowling]
comments: false
---

# [crowling]()

## Hanbit
~~~java
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
public class Hanbit {
	public static void main(String[] args) {
		try {
			// Jsoup으로 원하는 url을 가져온다
			String url = "http://www.hanbit.co.kr/media/";
			Document doc = Jsoup.connect(url).get();
//			System.out.println(doc);
			
			// 가져온 url에서 원하는 부분을 선택해서 가져온다
			Elements body = doc.select("div.sub_book_list_area .book_tit > a");
			for(Element title : body) {
				// a 함수안에 있는 책이름을 가져오기위해 text()를 사용한다
				System.out.println(title.text());
			}
			System.out.println(body);
		}catch(Exception ex) {
			System.out.println("예외발생");
			ex.printStackTrace();
		}
	}
}

~~~