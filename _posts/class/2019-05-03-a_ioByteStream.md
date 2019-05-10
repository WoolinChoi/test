---
layout: post
title: ioByteStream
category: git
tags: [java, class, ioByteStream]
comments: false
---

# [ioByteStream]()

## 오늘의 학습
~~~shell
1. 자바 입출력 - 파일관리

* java IO(Input Output) - 자바입출력

	입출력 - Stream
		- java.io 패키지
		
	1. byte 스트림
		- InputStream - FileInputStream
		- OutputStream - FileOutputStream

        + 필터 스트림
            - DataOutputStream - DataInputStream
            - ObjectOutputStream - ObjectInputStream(*직렬화필수)
		
	2. char 스트림
		- Reader - FileReader
		- Writer - FileWriter
		
	cf. ReandomAccessFile : 입출력스트림
~~~

## InputTestFirst
~~~java
/*
 *	======================================================
 *	InputStream을 구현한 FileInputStream을 이용한 예
 *	======================================================
 *	
 *	@ int read()
 *		` 한 바이트를 읽고 이를 0-255사이의 값을 리턴하지만4byte의 int 형으로 리턴
 *		` 리턴되는 값은 0-255 부호없는 바이트이지만 형변환 과정에서 -128 ~127의 부호 있는 바이트가 된다
 *		
 *		
 *		` 데이타를 읽어들이기 전까지 기다리므로 다른 부분을 실행할 수가 없다
 *			-> 쓰레드 적용 필요
 *			
 *		` 더이상 읽을 바이트가 없으면 -1 리턴
 *		
 *		
 *		
 *		[ 참고 ]
 *			int i =  b >= 0 ? b : 256 + b;
 */
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
public class InputTestFirst {
	public static  void main(String args[]) {
		try {
			FileInputStream fos = new FileInputStream("a.txt");
			while(true) {
				int data = fos.read(); // EOF = -1
				if(data == -1) break;
				System.out.print((char)data);
			}
			fos.close();
		}catch(IOException ex) {
			System.out.println("파일전송실패 :" + ex.toString());
		}
	}		
}
/*
 *	======================================
 *		결과 출력
 *	======================================
 *
 *	` 숫자만 나오는데, 우선 열개만 읽어서 숫자 자체로 출력하고
 *	나머지는 읽어서 (char) 형변환 하면 문자로 출력될 것이
 */
~~~

## OutputTestFirst
~~~java
/*
 *	===========================================================
 *	OuputStream을 구현한 FileOutputStream을 이용한 예제
 *	===========================================================
 *	
 *	@ write( int )
 *		` 0-255 사이의 정수를 인자로 받아 해당하는 바이트를 출력스트림에 쓴다
 *		` 인자로 정수형을 받지만, 실제로는 부호없는 바이트로 전송
 *		  ( 자바에서 정수형은 32bit이지만 그 중 8bit만 사용 )
 *	
 *	
 *	
 */
import java.io.FileOutputStream;
import java.io.IOException;
public class OutputTestFirst {
	public static void main(String args[]) {
		try {
			FileOutputStream fos = new FileOutputStream("a.txt");
			for(int ch = 'A'; ch <= 'Z'; ch++) {
				fos.write(ch);
			}		
			fos.close();
		}catch(IOException ex) {
			System.out.println("파일전송실패 :" + ex.toString());
		}
	}	
}
/*
 *	a.txt 를 노트패드와 워드패드로 읽어보기
 */
~~~