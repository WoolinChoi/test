---
layout: post
title: ioReaderWriter
category: git
tags: [java, class, ioReaderWriter]
comments: false
---

# [ioReaderWriter]()

## ReaderWriterTest
~~~java
/*
 * 메모장 만들기
 */
import java.io.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class ReaderWriterTest {
	public static void main(String args[]) {
		UIForm3 ui = new UIForm3();
		ui.addLayout();
		ui.eventProc();	
	}	
}
//========================================
//	화면을 관리하는 클래스 
//----------------------------------------
class UIForm3 extends JFrame {
	JTextArea ta;
	JButton bSave, bLoad, bClear;
	UIForm3() {
		ta = new JTextArea();		
		bSave = new JButton("파일저장");
		bLoad = new JButton("파일읽기");
		bClear = new JButton("화면지우기");
	}
	void addLayout() {
		JPanel pCenter = new JPanel();
		pCenter.setLayout(new BorderLayout());
		pCenter.add("Center", new JScrollPane(ta));
		JPanel pSouth = new JPanel();
		pSouth.add(bSave);
		pSouth.add(bLoad);
		pSouth.add(bClear);
		getContentPane().add("Center", pCenter);
		getContentPane().add("South",  pSouth);
		setSize( 400, 350 );
		setVisible( true );
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	void eventProc() {
		EventHandler hdlr = new EventHandler();
		bSave.addActionListener(hdlr);
		bLoad.addActionListener(hdlr);
	}
	class EventHandler implements ActionListener{
		public void actionPerformed(ActionEvent ev){
			Object evt = ev.getSource();
			// "화일저장" 버튼이 눌렸을 때 
			if(evt == bSave){
				JFileChooser fd = new JFileChooser();
				int returnValue = fd.showSaveDialog(null);
				if(returnValue == JFileChooser.APPROVE_OPTION) {
					File f = fd.getSelectedFile();
					try {
						FileWriter fw = new FileWriter(f);
						String content = ta.getText();
						fw.write(content);
						fw.close();
						ta.setText(null);
					}catch(Exception ex){
						System.out.println("저장 실패");
					}	
				}
			}else if(evt == bLoad) {
			// "화일읽기" 버튼이 눌렸을 때 
				JFileChooser fd = new JFileChooser();
				int returnValue = fd.showOpenDialog(null);
				if(returnValue == JFileChooser.APPROVE_OPTION) {
					File f = fd.getSelectedFile();
					try {
						FileReader fr = new FileReader(f);
						char[] data = new char[10 * 1024];
						fr.read(data);
						ta.setText(String.valueOf(data));
						fr.close();
					}catch(Exception ex){
						System.out.println("읽기 실패");
					}	
				}
			}	
		}
	}
}
~~~