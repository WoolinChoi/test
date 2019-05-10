---
layout: post
title: ioOthers
category: git
tags: [java, class, ioOthers]
comments: false
---

# [ioOthers]()

## FileEx
~~~java
import java.io.File;
public class FileEx {
	public static void main(String[] args) {
		File f= new File("src\\io\\others");
		System.out.println(f.getPath());
		System.out.println(f.getAbsolutePath());
		if(f.isFile()) {
			System.out.println("파일입니다");
		}else if(f.isDirectory()) {
			System.out.println("디렉토리입니다");
			String[] sub = f.list();
			for(String m : sub) {
				System.out.println(m);
			}
		}
		File f2 = new File("src\\io\\others\\파일.txt");
		f2.delete();
	}
}
~~~