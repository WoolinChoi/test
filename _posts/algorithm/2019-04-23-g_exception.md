---
layout: post
title: exception
category: javabasic
tags: [java][exception]
comments: false
---

# [exception]()

## TryCatch
~~~java
/*
 * 오류
 *  - 에러 : 심각 오류
 *  - 예외 : 심각하지 않은 오류
 * 
 * 예외처리 - 프로그램을 정상적으로 종료하기 위해
 * 
 * (1) 예외를 잡자 - try ~ catch 구문
 * 		try{
 * 			예외발생할 구문
 * 		}catch(){
 * 			예외가 발생한 후의 구문
 * 		}finally{
 * 			예외발생여부 상관없이 무조건 실행구문
 * 		}
 */
public class Ex01_TryCatch {
	public static void main(String[] args) {	
		String[] str = {"맛점", "우산", "즐거운화요일"};
		try{
			for(int i=0; i<=str.length; i++) {
				System.out.println(str[i]);
			}
			System.out.println("예외가 발생할 여지가 있는 구문");
			return;
		}catch(Exception ex) {								  
			System.out.println("예외발생: "+ex.getMessage());   // ex.toString()
			ex.printStackTrace();							   // 예외 발생 문구를 모두 보여준다.
			
		}finally {											   // return을 해도 finally는 무조건 실행 
			System.out.println("무조건 실행하는 구문");		    // 커넥션을 닫을 때 많이 쓰인다.
		}
		System.out.println("프로그램 정상 종료");
	}	
}
/* 
 * 정상적인 구문일 때 return이 있을 경우에 catch로 안가고 예외발생구문과 프로그램 정상 종료구문은 안나온다.  finally는 항상출력
 * 비정상적인 구문일 때 return 전에 예외가 발생함으로 catch로 넘어가 예외발생구문이 나오고 프로그램 정상 종료구문이 나온다. finally는 항상출력  
 */	
~~~

## File
~~~java
import java.io.FileInputStream;
import java.io.FileNotFoundException;
public class Ex02_File {
	public static void main(String[] args) {
		try{
			FileInputStream fis = new FileInputStream("abc.txt");
			System.out.println("파일연결");
			fis.read();
		}catch(Exception e) {
			// e.printStackTrace();
			System.out.println("파일없는 예외: "+e.getMessage());
		}
	}
}
~~~

## TryCatch2
~~~java
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
public class Ex02_TryCatch2 {
	public static void main(String[] args) {
		FileInputStream  fis = null;
		try{
			fis = new FileInputStream("abc.txt");
			System.out.println("파일연결");
			fis.read();		
//		}catch(FileNotFoundException e) {
//			// e.printStackTrace();
//			System.out.println("파일없는 예외: "+e.getMessage());
//		}catch(IOException e) {
//			System.out.println("입출력 예외: "+e.getMessage()); // 일일이 Exception을 받을 수 있지만 Exception범용으로 받아줘도 된다.
		}catch(Exception e) {
			System.out.println("그 외 예외처리");
		}finally {
			try{ fis.close(); }catch(Exception e) {}
		}
	}
}
~~~

## throws
~~~java
import java.io.FileInputStream;
public class Ex03_throws {
	public static void main(String[] args) {
		try {
			readFile();
			System.out.println("파일처리");
		}catch(Exception ex) {
			System.out.println("예외발생");
		}
	}
	static void readFile() throws Exception {
		FileInputStream fis = new FileInputStream("xxx.txt");
		System.out.println("파일연결");
	}
}
~~~

## MyException
~~~java
public class MyException extends Exception {
	public String getMessge() {
		return "우리가 자주 실수하는 예외";
	}
}
~~~

## throw
~~~java
public class Ex04_throw {
	public static void main(String[] args) {
		try {
		readArrey();
		}catch(Exception ex) {
			System.out.println("예외발생: "+ex.getMessage());
		}
		System.out.println("정상종료");
	}
	static void readArrey() throws Exception {
		String[] str = {"우리는한배", "공부즐기시기", "스터디"};
		try{
			for(int i=0; i<=str.length; i++) {
				System.out.println(str[i]);
			}
		}catch(Exception ex) {
			throw new MyException();
		}
	}
}
// 5 6 7 13 14 15 16 17 18 19 20 8 9 10 11
~~~

## 문제
~~~java
[문제1] 다음 문장들 중에서 올바른 메소드 정의는?
(1) void method () throw MyException {throws MyException(); }
(2) void method () throw MyException {throws new MyException(); }
(3) void method () throws MyException {throw MyException(); }
(4) void method () throws MyException {throw new MyException(); }

[답]
4
~~~

## 문제
~~~java
[문제2] 다음 프로그램의 출력결과는?
class Test{
    static void method() {
        throw new Exception();
    }
    public static void main( String [] args ) { 
        try{
            method();
        }catch( Exception ex ) {
            System.out.println(“예외처리”);
        }
    }
}
(1) 컴파일 에러가 발생한다
(2) “예외처리”가출력된다
(3) 실행은 성공하나 아무것도 출력되지 않는다.
(4) 실행시 예외가 발생하여 프로그램이 비정상적으로 종료한다.

[답]
1
~~~

## 문제
~~~java
[문제3] 다음 프로그램의 출력결과는?
class Test{
    public static void main( String [] args ) { 
        try{
            return;
        }finally {
            System.out.println(“FINALLY”);
        }
    }
}
(1) 컴파일 에러가 발생한다
(2) 컴파일 에러는 없으나 실행시 예외가 발생한다.
(3) 실행은 성공하나 아무것도 출력되지 않는다.
(4) “FINALLY”라는 문장이 출력된다.

[답]
4
~~~

## 문제
~~~java
[문제4] 다음 프로그램의출력 결과는?
class Test{
    public static void main( String [] args ) { 
        try{
            System.exit(0);
        }finally {
            System.out.println(“FINALLY”);
        }
    }
}
(1) 컴파일 에러가 발생한다
(2) 컴파일 에러는 없으나 실행시 예외가 발생한다.
(3) 실행은 성공하나 아무것도 출력되지 않는다.
(4) “FINALLY”라는 문장이 출력된다.

[답]
3
~~~

## 문제
~~~java
[문제5] 다음 프로그램에서 출력 결과로 “try”라는 단어가 몇 번 출력되나?
class Test{
    static void method( int i ) throws Exception {
        if ( i % 2 == 0 ) throw new Exception();
    }
    public static void main( String [] args ) {
        for( int i=0; i <= 4 ; i++ ) {
            try{
                method( i );
                System.out.println(“try”);
            }catch( Exception ex ) {
                System.out.println(“catch”);
            }
        }
    }
}

[답]
2
~~~

## 문제
~~~java
[문제6] 다음 프로그램의출력 결과는?
import java.io.IOException;
class Test{
    static void method() throws IOException {
        throw new IOException();
    }
    public static void main( String [] args ) {  
        try{
            method();
            System.out.println(“TRY”);
        }catch( IOException ex ) {
            System.out.println(“IOEXCEPTION”);
        }catch( Exception ex ) {
            System.out.println(“EXCEPTION”);
        }finally {
            System.out.println(“FINALLY”);
        }
        System.out.println(“END”);
    }
}
(1) 컴파일 에러
(2) 실행시 예외발생으로 프로그램 비정상 종료
(3) IOEXCEPTION – FINALLY – END
(4) EXCEPTION – FINALLY – END
(5) TRY – IOEXCEPTION – END

[답]
3
~~~

## 문제
~~~java
[문제7] 다음 프로그램의출력 결과는?
import java.io.IOException;
class Test{
    static void method() throws IOException {
        throw new IOException();
    }
    public static void main( String [] args ) {  
        try{
            method();
            System.out.println(“TRY”);
        } catch( Exception ex ) {               // Exception으로 컴파일 에러
            System.out.println(“EXCEPTION”);
        } catch( IOException ex ) {
            System.out.println(“IOEXCEPTION”);
        } finally {
            System.out.println(“FINALLY”);
        }
        System.out.println(“END”);
    }
}
(1) 컴파일 에러
(2) 실행시 예외발생으로 프로그램 비정상 종료
(3) IOEXCEPTION – FINALLY – END
(4) EXCEPTION – FINALLY – END
(5) TRY – IOEXCEPTION – END

[답]
1
~~~

## 문제
~~~java
[문제8] 다음 프로그램의출력 결과는?
class Test{
    static String str = “”;
    static void method( int i ){
        try{
            if ( i == 10 ) throw new Exception();
            str += “A”;
        }catch( Exception ex ) {
            str += “B”;
            return;
        } finally {
            str += “C”;
        }
        str += “D”;
    }
    public static void main( String [] args ) {  
        method( 5 );
        method( 10);
        System.out.println(str);
    }
}

[답]
A C D B C
~~~