---
layout: post
title: jfreechart
category: jdbc
tags: [java, jdbc, jfreechart]
comments: false
---

# [jfreechart]()

## ChartA
~~~java
import java.awt.*;
import org.jfree.chart.*;
import org.jfree.chart.axis.*;
import org.jfree.chart.labels.*;
import org.jfree.chart.plot.*;
import org.jfree.chart.renderer.category.*;
import org.jfree.chart.title.*;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.ui.*;
public class ChartA {
    public JFreeChart getChart() {
        
        // 데이터 생성
        DefaultCategoryDataset dataset = new DefaultCategoryDataset(); 
 
        //------------------------------------------------------------------
        // 데이터 입력 ( 값, 범례, 카테고리 )
        dataset.addValue(1.0, "S1", "1월");
        dataset.addValue(4.0, "S1", "2월");
        dataset.addValue(3.0, "S1", "3월");
        dataset.addValue(5.0, "S1", "4월");
        dataset.addValue(5.0, "S1", "5월");
        dataset.addValue(7.0, "S1", "6월");
        dataset.addValue(7.0, "S1", "7월");
        dataset.addValue(8.0, "S1", "8월");
        dataset.addValue(5.0, "S1", "9월");
        dataset.addValue(0, "S1", "10월");
        dataset.addValue(6.0, "S1", "11월");
        dataset.addValue(3.0, "S1", "12월");
        // 위 부분을 반복문으로 만들었으면 좋겠다는 강한 느낌 ^^
        //------------------------------------------------------------------
        
        // 렌더링 생성 및 세팅
        // 렌더링 생성
        final BarRenderer renderer = new BarRenderer();
     
        // 공통 옵션 정의
        final CategoryItemLabelGenerator generator = new StandardCategoryItemLabelGenerator();
        final ItemLabelPosition p_center = new ItemLabelPosition(
                ItemLabelAnchor.CENTER, TextAnchor.CENTER
            );
        final ItemLabelPosition p_below = new ItemLabelPosition(
                     ItemLabelAnchor.OUTSIDE6, TextAnchor.TOP_LEFT
                     );
        Font f = new Font("Gulim", Font.BOLD, 14);
        Font axisF = new Font("Gulim", Font.PLAIN, 14);
       
        // 렌더링 세팅
        // 그래프 1
        renderer.setBaseItemLabelGenerator(generator);
        renderer.setBaseItemLabelsVisible(true);
        renderer.setBasePositiveItemLabelPosition(p_center);
        renderer.setBaseItemLabelFont(f);
        renderer.setSeriesPaint(0, new Color(0,162,255));
 
        // plot 생성
        final CategoryPlot plot = new CategoryPlot();
       
        // plot 에 데이터 적재
        plot.setDataset(dataset);
        plot.setRenderer(renderer);
 
        // plot 기본 설정
        plot.setOrientation(PlotOrientation.VERTICAL);       // 그래프 표시 방향
        plot.setRangeGridlinesVisible(true);                 // X축 가이드 라인 표시여부
        plot.setDomainGridlinesVisible(true);                // Y축 가이드 라인 표시여부
 
        // 렌더링 순서 정의 : dataset 등록 순서대로 렌더링 (즉, 먼저 등록한게 아래로 깔림 )
        plot.setDatasetRenderingOrder(DatasetRenderingOrder.FORWARD);
       
        // X축 세팅
        plot.setDomainAxis(new CategoryAxis());           // X축 종류 설정
        plot.getDomainAxis().setTickLabelFont(axisF); // X축 눈금라벨 폰트 조정
        plot.getDomainAxis().setCategoryLabelPositions(CategoryLabelPositions.STANDARD);       // 카테고리 라벨 위치 조정
 
        // Y축 세팅
        plot.setRangeAxis(new NumberAxis());              // Y축 종류 설정
        plot.getRangeAxis().setTickLabelFont(axisF);  // Y축 눈금라벨 폰트 조정
       
        // 세팅된 plot을 바탕으로 chart 생성
        final JFreeChart chart = new JFreeChart(plot);
        chart.setTitle(" 우리들의 차트 "); 
        TextTitle copyright = new TextTitle("월별 입사 현황 ", new Font("SansSerif", Font.PLAIN, 9));
        copyright.setHorizontalAlignment(HorizontalAlignment.RIGHT);
        chart.addSubtitle(copyright);  
        return chart;
    }
}
~~~

## ChartB
~~~java
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.CategoryAxis;
import org.jfree.chart.axis.CategoryLabelPositions;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.labels.CategoryItemLabelGenerator;
import org.jfree.chart.labels.ItemLabelAnchor;
import org.jfree.chart.labels.ItemLabelPosition;
import org.jfree.chart.labels.StandardCategoryItemLabelGenerator;
import org.jfree.chart.plot.CategoryPlot;
import org.jfree.chart.plot.DatasetRenderingOrder;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.renderer.category.BarRenderer;
import org.jfree.chart.title.TextTitle;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.ui.HorizontalAlignment;
import org.jfree.ui.TextAnchor;
public class ChartB {
    public JFreeChart getChart() {
        
        // 데이터 생성
        DefaultCategoryDataset dataset = new DefaultCategoryDataset(); 
 
        //------------------------------------------------------------------
        // 데이터 입력 ( 값, 범례, 카테고리 )
        Database db = new Database();
        ArrayList<ArrayList> data = db.getData();
        for(ArrayList temp : data) {
        	int value = (Integer) temp.get(0);
        	String cate = (String) temp.get(1);
        	dataset.addValue(value, "월별",  cate);
        }
        //------------------------------------------------------------------
        
        // 렌더링 생성 및 세팅
        // 렌더링 생성
        final BarRenderer renderer = new BarRenderer();
     
        // 공통 옵션 정의
        final CategoryItemLabelGenerator generator = new StandardCategoryItemLabelGenerator();
        final ItemLabelPosition p_center = new ItemLabelPosition(
                ItemLabelAnchor.CENTER, TextAnchor.CENTER
            );
        final ItemLabelPosition p_below = new ItemLabelPosition(
                     ItemLabelAnchor.OUTSIDE6, TextAnchor.TOP_LEFT
                     );
        Font f = new Font("Gulim", Font.BOLD, 14);
        Font axisF = new Font("Gulim", Font.PLAIN, 14);
       
        // 렌더링 세팅
        // 그래프 1
        renderer.setBaseItemLabelGenerator(generator);
        renderer.setBaseItemLabelsVisible(true);
        renderer.setBasePositiveItemLabelPosition(p_center);
        renderer.setBaseItemLabelFont(f);
        renderer.setSeriesPaint(0, new Color(0,162,255));
 
        // plot 생성
        final CategoryPlot plot = new CategoryPlot();
       
        // plot 에 데이터 적재
        plot.setDataset(dataset);
        plot.setRenderer(renderer);
 
        // plot 기본 설정
        plot.setOrientation(PlotOrientation.VERTICAL);       // 그래프 표시 방향
        plot.setRangeGridlinesVisible(true);                 // X축 가이드 라인 표시여부
        plot.setDomainGridlinesVisible(true);                // Y축 가이드 라인 표시여부
 
        // 렌더링 순서 정의 : dataset 등록 순서대로 렌더링 ( 즉, 먼저 등록한게 아래로 깔림 )
        plot.setDatasetRenderingOrder(DatasetRenderingOrder.FORWARD);
       
        // X축 세팅
        plot.setDomainAxis(new CategoryAxis());           // X축 종류 설정
        plot.getDomainAxis().setTickLabelFont(axisF); // X축 눈금라벨 폰트 조정
        plot.getDomainAxis().setCategoryLabelPositions(CategoryLabelPositions.STANDARD);       // 카테고리 라벨 위치 조정
 
        // Y축 세팅
        plot.setRangeAxis(new NumberAxis());              // Y축 종류 설정
        plot.getRangeAxis().setTickLabelFont(axisF);  // Y축 눈금라벨 폰트 조정
       
        // 세팅된 plot을 바탕으로 chart 생성
        final JFreeChart chart = new JFreeChart(plot);
        chart.setTitle(" 우리들의 차트 "); 
        TextTitle copyright = new TextTitle("월별 입사 현황 ", new Font("SansSerif", Font.PLAIN, 9));
        copyright.setHorizontalAlignment(HorizontalAlignment.RIGHT);
        chart.addSubtitle(copyright);  
        return chart;
    }
}
~~~

## Database
~~~java
import java.sql.*;
import java.util.*;
public class Database {
	String URL = "jdbc:oracle:thin:@127.0.0.1:1521:orcl";
	String USER ="scott";
	String PASS = "tiger";

	public ArrayList<ArrayList> getData() {
		ArrayList<ArrayList> data = new ArrayList<ArrayList>();
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con = DriverManager.getConnection(URL, USER , PASS);	
			
			//***************************************************************
			// 1. 월별 입사한 인원
//			String sql = "SELECT count(*) cnt, to_char(hiredate, 'MM') mm FROM emp GROUP BY to_char(hiredate, 'MM') "
//					+ "ORDER BY to_char(hiredate, 'MM')";
			
			// 2. 업무별 평균 월급
//			String sql = "SELECT job job, round(avg(sal)) sal FROM emp GROUP BY job ORDER BY job";
			
			// 3. 월급을 많이 받는 10명
			String sql = "SELECT rownum, s.ename name, s.sal sal FROM (SELECT ename, sal FROM emp ORDER BY sal DESC) s " 
					+ "WHERE rownum <= 10";
			
			//***************************************************************
			
			PreparedStatement stmt = con.prepareStatement(sql);	

			ResultSet rset = stmt.executeQuery();

			
			while(rset.next()) {
				ArrayList temp = new ArrayList();
//				temp.add(rset.getInt("CNT"));
//				temp.add(rset.getString("MM"));
//				temp.add(rset.getInt("SAL"));
//				temp.add(rset.getString("JOB"));
				temp.add(rset.getInt("SAL"));
				temp.add(rset.getString("NAME"));
				data.add(temp);
			}
			rset.close();
			stmt.close();
			con.close();
		}catch(Exception ex) {
			System.out.println("에러 : " + ex.getMessage());
		}
		return data;
	}
}
~~~

## MyFrame extends JFrame
~~~java
import javax.swing.JFrame;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
public class MyFrame extends JFrame {
	// 우리가 만드는 화면 
	MyFrame(){
		 // *******************************************************
//		 ChartA demo = new ChartA();   		 // (1) 정해진 값으로 차트
		 ChartB demo = new ChartB();		 // (2) DB에서 가져온 값으로 차트 
         JFreeChart chart = demo.getChart();     
         ChartPanel chartPanel=new ChartPanel(chart); 
         				// JFreeChart는 ChartPanel이나 ChartFrame에만 붙일 수 있다.
         				// 차트만 출력하려면 ChartFrame에 붙여서 바로 출력하거나
         				// 기존의 화면에 보이게 하려면 ChartPanel에 붙이고 다시 우리 화면 JPanel에 붙인다. 
         add(chartPanel);
         setSize(800,400); 
         setVisible(true);
         setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public static void main(String[] args) {
		MyFrame my = new MyFrame();
	}
}
~~~

## PolylineBarChart
~~~java
import java.awt.*;
import org.jfree.chart.*;
import org.jfree.chart.axis.*;
import org.jfree.chart.labels.*;
import org.jfree.chart.plot.*;
import org.jfree.chart.renderer.category.*;
import org.jfree.chart.title.TextTitle;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.ui.*;
public class PolylineBarChart {
    public JFreeChart getChart() {
      
        // 데이터 생성
        DefaultCategoryDataset dataset1 = new DefaultCategoryDataset();                // bar chart 1
        DefaultCategoryDataset dataset12 = new DefaultCategoryDataset();        		 // bar chart 2
        DefaultCategoryDataset dataset2 = new DefaultCategoryDataset();                // line chart 1
 
        // 데이터 입력 ( 값, 범례, 카테고리 )
        // 그래프 1       
        dataset1.addValue(1.0, "S1", "1월");
        dataset1.addValue(4.0, "S1", "2월");
        dataset1.addValue(3.0, "S1", "3월");
        dataset1.addValue(5.0, "S1", "4월");
        dataset1.addValue(5.0, "S1", "5월");
        dataset1.addValue(7.0, "S1", "6월");
        dataset1.addValue(7.0, "S1", "7월");
        dataset1.addValue(8.0, "S1", "8월");
        dataset1.addValue(0, "S1", "9월");
        dataset1.addValue(0, "S1", "10월");
        dataset1.addValue(0, "S1", "11월");
        dataset1.addValue(0, "S1", "12월");
 
        // 그래프 2       
        dataset12.addValue(0, "S2", "1월");
        dataset12.addValue(0, "S2", "2월");
        dataset12.addValue(0, "S2", "3월");
        dataset12.addValue(0, "S2", "4월");
        dataset12.addValue(0, "S2", "5월");
        dataset12.addValue(0, "S2", "6월");
        dataset12.addValue(0, "S2", "7월");
        dataset12.addValue(0, "S2", "8월");
        dataset12.addValue(6.0, "S2", "9월");
        dataset12.addValue(4.0, "S2", "10월");
        dataset12.addValue(8.0, "S2", "11월");
        dataset12.addValue(7.0, "S2", "12월");

 
        // 그래프 3       
        dataset2.addValue(9.0, "T1", "1월");
        dataset2.addValue(7.0, "T1", "2월");
        dataset2.addValue(2.0, "T1", "3월");
        dataset2.addValue(6.0, "T1", "4월");
        dataset2.addValue(6.0, "T1", "5월");
        dataset2.addValue(9.0, "T1", "6월");
        dataset2.addValue(5.0, "T1", "7월");
        dataset2.addValue(4.0, "T1", "8월");
        dataset2.addValue(8.0, "T1", "9월");
        dataset2.addValue(8.0, "T1", "10월");
        dataset2.addValue(8.0, "T1", "11월");
        dataset2.addValue(8.0, "T1", "12월");
 
        // 렌더링 생성 및 세팅
        // 렌더링 생성
        final BarRenderer renderer = new BarRenderer();
        final BarRenderer renderer12 = new BarRenderer();
        final LineAndShapeRenderer renderer2 = new LineAndShapeRenderer();
       
        // 공통 옵션 정의
        final CategoryItemLabelGenerator generator = new StandardCategoryItemLabelGenerator();
        final ItemLabelPosition p_center = new ItemLabelPosition(
                ItemLabelAnchor.CENTER, TextAnchor.CENTER
            );
        final ItemLabelPosition p_below = new ItemLabelPosition(
                     ItemLabelAnchor.OUTSIDE6, TextAnchor.TOP_LEFT
                     );
        Font f = new Font("Gulim", Font.BOLD, 14);
        Font axisF = new Font("Gulim", Font.PLAIN, 14);
       
        // 렌더링 세팅
        // 그래프 1
        renderer.setBaseItemLabelGenerator(generator);
        renderer.setBaseItemLabelsVisible(true);
        renderer.setBasePositiveItemLabelPosition(p_center);
        renderer.setBaseItemLabelFont(f);
        renderer.setSeriesPaint(0, new Color(0,162,255));
 
        // 그래프 2       
        renderer12.setSeriesPaint(0, new Color(232,168,255));
        renderer12.setBaseItemLabelFont(f);
        renderer12.setBasePositiveItemLabelPosition(p_center);
        renderer12.setBaseItemLabelGenerator(generator);
        renderer12.setBaseItemLabelsVisible(true);
       
        // 그래프 3       
        renderer2.setBaseItemLabelGenerator(generator);
        renderer2.setBaseItemLabelsVisible(true);
        renderer2.setBaseShapesVisible(true);
        renderer2.setDrawOutlines(true);
        renderer2.setUseFillPaint(true);
        renderer2.setBaseFillPaint(Color.WHITE);
        renderer2.setBaseItemLabelFont(f);
        renderer2.setBasePositiveItemLabelPosition(p_below);
        renderer2.setSeriesPaint(0,new Color(219,121,22));
        renderer2.setSeriesStroke(0,new BasicStroke(
                                               2.0f,
                                               BasicStroke.CAP_ROUND,
                                               BasicStroke.JOIN_ROUND,
                                               3.0f)
        );
       
        // plot 생성
        final CategoryPlot plot = new CategoryPlot();
       
        // plot 에 데이터 적재
        plot.setDataset(dataset1);
        plot.setRenderer(renderer);
        plot.setDataset(1,dataset12);
        plot.setRenderer(1,renderer12);
        plot.setDataset(2, dataset2);
        plot.setRenderer(2, renderer2);
 
        // plot 기본 설정
        plot.setOrientation(PlotOrientation.VERTICAL);       // 그래프 표시 방향
        plot.setRangeGridlinesVisible(true);                 // X축 가이드 라인 표시여부
        plot.setDomainGridlinesVisible(true);                // Y축 가이드 라인 표시여부
 
        // 렌더링 순서 정의 : dataset 등록 순서대로 렌더링 (즉, 먼저 등록한게 아래로 깔림 )
        plot.setDatasetRenderingOrder(DatasetRenderingOrder.FORWARD);
       
        // X축 세팅
        plot.setDomainAxis(new CategoryAxis());           // X축 종류 설정
        plot.getDomainAxis().setTickLabelFont(axisF); // X축 눈금라벨 폰트 조정
        plot.getDomainAxis().setCategoryLabelPositions(CategoryLabelPositions.STANDARD);       // 카테고리 라벨 위치 조정
 
        // Y축 세팅
        plot.setRangeAxis(new NumberAxis());              // Y축 종류 설정
        plot.getRangeAxis().setTickLabelFont(axisF);  // Y축 눈금라벨 폰트 조정
       
        // 세팅된 plot을 바탕으로 chart 생성
        final JFreeChart chart = new JFreeChart(plot);
        chart.setTitle("Overlaid Bar Chart"); // 차트 타이틀
        TextTitle copyright = new TextTitle("JFreeChart WaferMapPlot", new Font("SansSerif", Font.PLAIN, 9));
        copyright.setHorizontalAlignment(HorizontalAlignment.RIGHT);
        chart.addSubtitle(copyright);  // 차트 서브 타이틀
        return chart;
    }
    
    public static void main(final String[] args) {
        	  PolylineBarChart demo = new PolylineBarChart();
              JFreeChart chart = demo.getChart();
              ChartFrame frame1=new ChartFrame("Bar Chart",chart);
              frame1.setSize(800,400); 
              frame1.setVisible(true);
     }
}
~~~