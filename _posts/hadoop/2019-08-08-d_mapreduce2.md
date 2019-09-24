---
layout: post
title: mapreduce2
category: hadoop
tags: [hadoop, mapreduce]
comments: false
---

# [mapreduce2]()

## 학습
* MapReduce 이해
* Flume 설치
* pig 설치

## 실습
* DelayCount
    - airline3.genericclass.DelayCount 생성
~~~java
package airline3.genericclass;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
//* extends Configured implements Tool
// Configured : 환경설정파일을 제어하기 위해
// Tool : 콘솔 설정 옵션을 지원하기 위해
public class DelayCount extends Configured implements Tool 
{	
    public static void main(String args[]) throws Exception
    {
        // ToolRunner : Tool 인터페이스의 실행을 도와주는 헬퍼 클래스 
        int res = ToolRunner.run(new Configuration(),new DelayCount(), args);
        System.out.println("Job Result : " + res);		
    } // end of main
    public int run(String[] args) throws Exception
    {
    String[] otherArgs = new GenericOptionsParser(getConf(), args).getRemainingArgs();        
        if(args.length != 2)
        { 
            System.err.println("Usage: DelayCount -D workType=departure <input> <output>");
            System.exit(2); 
        } // end of if
		// Configuration conf = new Configuration();
        // 기존에 있는 Conf를 가져온다.
        Job job = Job.getInstance(getConf(), "DelayCount");
        // 입력 파일 경로
        FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
        // 출력 디렉토리 경로
        FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
        job.setJarByClass(DelayCount.class);
        job.setMapperClass(DelayCountMapper.class); // 지연시간
        job.setReducerClass(DelayCountReducer.class);
        // 입력포맷과 출력포맷 지정
        job.setInputFormatClass(TextInputFormat.class);
        job.setOutputFormatClass(TextOutputFormat.class);
        // 입출력 자료형 지정
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        // mapreduce job 실행(끝날때까지 대기)
        job.waitForCompletion(true);
        return 0;
    } // end of run
} // end of DelayCount
~~~

    - airline3.genericclass.DelayCountMapper 생성
~~~java
package airline3.genericclass;
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import airline.common.AirlinePerformanceParser;
public class DelayCountMapper extends Mapper<LongWritable, Text, Text, IntWritable>
{
    private Text outputKey = new Text(); 
    private final static IntWritable outputValue = new IntWritable(1);       
    //* (1) 출발지연인지 도착지연인지 구별하는 변수
    private String workType;      
    //* (2) main 함수 실행시 지정한 workType 값을 얻어온다.
    public void setup(Context context) throws IOException, InterruptedException
    {	
        // workType값을 받아다 변수에 넣는다.
        workType = context.getConfiguration().get("workType");
    }       
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException 
    {
        AirlinePerformanceParser parser = new AirlinePerformanceParser(value);
        outputKey.set(parser.getYear() + "," + parser.getMonth());
        //* (3) 출발지연인지 도착지연인지 
        if(workType.equals("departure"))
        {
            if(parser.getDepartureDelayTime() > 0 )
            {
                context.write(outputKey, outputValue);
            } // end of if(getDepartureDelayTime)
        }else if(workType.equals("arrival")) 
        {
            if(parser.getArriveDelayTime() > 0 )
            {
                context.write(outputKey, outputValue);
            } // end of if(getArriveDelayTime)
        } // end of if(workType)
    } // end of map
} // end of DelayCountMapper
~~~

    - airline3.genericclass.DelayCountReducer 생성    
~~~java
package airline3.genericclass;
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
/*
    Reducer<입력Key, 입력Value, 출력Key, 출력Value)
    입력 : <1998,5> 1
    출력 : <1998,5> 10 (합산값)
*/
public class DelayCountReducer extends Reducer<Text, IntWritable, Text, IntWritable>
{
    private IntWritable result=new IntWritable();        
    // key, list(value)
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException 
    {
        // 계산 결과를 합치는 코드
        int sum=0;
        for(IntWritable value : values )
        {
            sum += value.get();
        } // end of for
        result.set(sum);
        context.write(key, result);  
    } // end of reduce
} // end of DelayCountReducer
~~~

    - WinCSP 업로드 후
~~~
1) [hadoop@nn01 ~]$ ls /home/hadoop/source
2) [hadoop@nn01 ~]$ yarn jar /home/hadoop/source/lab6.jar airline3.genericclass.DelayCount -D workType=departure /input/airline/1987.csv /output/delaycount_departure
3) [hadoop@nn01 ~]$ hdfs dfs -ls /output/delaycount_departure
4) [hadoop@nn01 ~]$ hdfs dfs -cat /output/delaycount_departure/part-r-00000
~~~

* 플럼 설치
    - dn01 노드의 root 계정에서 설치
~~~
1) [root@dn01 ~]# cd /tmp
2) [root@dn01 tmp]# wget http://apache.mirror.cdnetwors.com/flume/stable/apache-flume-1.9.0-bin.tar.gz
3) [root@dn01 tmp]# tar xzvf apache-flume-1.9.0-bin.tar.gz
4) [root@dn01 tmp]# mkdir -p /opt/flume/1.9.0
5) [root@dn01 tmp]# ls -l /opt/flume/1.9.0
6) [root@dn01 tmp]# mv apache-flume-1.9.0-bin/* /opt/flume/1.9.0
7) [root@dn01 tmp]# ln -s /opt/flume/1.9.0 /opt/flume/current
8) [root@dn01 tmp]# ls -l /opt/flume
9) [root@dn01 tmp]# chown -R hadoop:hadoop /opt/flume
10) [root@dn01 tmp]# ls -l /opt/flume
~~~

    - dn01 노드의 hadoop 계정에서 환경변수 설정
~~~
1) [root@dn01 ~]# su - hadoop
2) [hadoop@dn01 ~]$ vi ~/.bash_profile
#### FLUME 1.9.0 ####
export FLUME_HOME=/opt/flume/current
export PATH=$PATH:$FLUME_HOME/bin
#### FLUME 1.9.0 ####
3) [hadoop@dn01 ~]$ source ~/.bash_profile
~~~

    - dn01 노드의 hadoop 계정에서 Flume 설정
~~~
1) [hadoop@dn01 ~]$ cd $FLUME_HOME/conf
2) [hadoop@dn01 ~]$ cp flume-conf.properties.template flume-conf.properties
~~~

    - sodo 확인
~~~
1) [hadoop@dn01 ~]$ sudo tail -F /var/log/secure
2) [hadoop@dn01 ~]$ ls -l /var/log/secure
3) [hadoop@dn01 ~]$ su - root
4) [root@dn01 ~]$ chmod 666 /var/log/secure
5) [hadoop@dn02 ~]$ ssh dn01
~~~

    - Flume 확인
~~~shell
1) [hadoop@dn01 ~]$ cd $FLUME_HOME/conf
2) [hadoop@dn01 conf]$ vi flume-syslog.properties
########## flume-syslog.properties ##########
agent.sources = s1
agent.channels = c1
agent.sinks = k1
# For each one of the sources, the type is defined
agent.sources.s1.type = exec
agent.sources.s1.command = tail -F /var/log/secure
# The channel can be defined as follows.
agent.sources.s1.channels = c1
# Each sink's type must be defined
agent.sinks.k1.type = logger
#Specify the channel the sink should use
agent.sinks.k1.channel = c1
# Each channel's type is defined.
agent.channels.c1.type = memory
########## flume-syslog.properties ##########
3) [hadoop@dn01 conf]$ flume-ng agent --conf-file $FLUME_HOME/conf/flume-syslog.properties --name agent -Dflume.root.logger=INFO,console
4) [hadoop@dn02 ~]$ for((i=0;i<10;i++)); do ssh dn01; done
5) [hadoop@dn02 ~]$ for((i=0;i<10;i++)); do logout; done
~~~

* Bitcoin
    - 준비
~~~shell
1) [hadoop@dn01 ~]$ mkdir -p /home/hadoop/source_data/bitthumbitCoin 
2) [hadoop@dn01 ~]$mkdir -p /home/hadoop/source_data/coinonebitCoin
3) mkdir -p /home/hadoop/source_data/upbitbitCoin
4) mkdir -p /home/hadoop/crawler
5) vi /home/hadoop/crawler/bitThumb_fileCount.txt
########## bitThumb_fileCount.txt ##########
0
########## bitThumb_fileCount.txt ##########
6) vi /home/hadoop/crawler/coinOne_fileCount.txt
########## coinOne_fileCount.txt ##########
0
########## coinOne_fileCount.txt ##########
7) vi /home/hadoop/crawler/upBit_fileCount.txt
########## upBit_fileCount.txt ##########
0
########## upBit_fileCount.txt ##########
8) hdfs dfs -mkdir -p /user/hadoop/testInput/bitThumb
9) vi flume-bitcoin.properties
########## flume-bitcoin.properties ##########
agent.sources = s1
agent.channels = m1
agent.sinks = h1
# For each one of the sources, the type is defined
agent.sources.s1.type = taildir
# The channel can be defined as follows.
agent.sources.s1.channels = m1
agent.sources.s1.filegroups = f1
agent.sources.s1.filegroups.f1 = /home/hadoop/source_data/bitthumbitCoin/bitthumbitCoin[0-9]{1,}.csv
# Each sink's type must be defined
agent.sinks.h1.type = hdfs
#Specify the channel the sink should use
agent.sinks.h1.channel = m1
agent.sinks.h1.hdfs.path = hdfs://nn01:9000/user/hadoop/testInput/bitThumb
agent.sinks.h1.hdfs.writeFormat = Text
agent.sinks.h1.hdfs.rollSize = 64000000
agent.sinks.h1.hdfs.rollInterval = 0
agent.sinks.h1.hdfs.rollCount = 0
agent.sinks.h1.hdfs.batchSize = 9900
agent.sinks.h1.hdfs.fileType = DataStream
# Each channel's type is defined.
agent.channels.m1.type = memory
# Other config values specific to each type of channel(sink or source)
# can be defined as well
# In this case, it specifies the capacity of the memory channel
agent.channels.m1.capacity = 10000
agent.channels.m1.transactionCapacity = 10000
########## flume-bitcoin.properties ##########
~~~
    
    - WinCSP 업로드 후
~~~
1) [hadoop@dn02 ~]$ ssh dno1
2) [hadoop@dn01 ~]$ ls /home/hadoop/source
3) [hadoop@dn01 ~]$ java -jar /home/hadoop/source/bitcoin.jar temp.MainApp 
~~~

* Pig 설치
    - 노드에서 root 계정에서 설치
~~~
1) [root@dn01 ~]$ cd /tmp 
2) [root@dn01 tmp]$ wget http://apache.tt.co.kr/pig/pig-0.17.0/pig-0.17.0.tar.gz
3) [root@dn01 tmp]$ tar zxvf pig-0.17.0.tar.gz
4) [root@dn01 tmp]$ mkdir -p /opt/pig/0.17.0
5) [root@dn01 tmp]$ ls -l /opt/pig/0.17.0
6) [root@dn01 tmp]$ mv pig-0.17.0/* /opt/pig/0.17.0
7) [root@dn01 tmp]$ ln -s /opt/pig/0.17.0 /opt/pig/current
8) [root@dn01 tmp]$ ls -l /opt/pig 
9) [root@dn01 tmp]$ chown -R hadoop:hadoop /opt/pig
10) [root@dn01 tmp]$ ls -l /opt/pig
~~~

    - dn01 노드의 hadoop 계정에서 환경변수 설정
~~~shell
2) [hadoop@dn01 ~]$ vi ~/.bash_profile
#### PIG 0.17.0 ######################
export PIG_HOME=/opt/pig/current
export PATH=$PATH:$PIG_HOME/bin
export PIG_CLASSPATH=$HADOOP_HOME/conf
#### PIG 0.17.0 ######################
2) [hadoop@dn01 ~]$ source ~/.bash_profile
~~~

    - Pig 실행
~~~
1) [hadoop@dn01 ~]$ mkdir pig_data
2) [hadoop@dn01 pig_data]$ cd pig_data
3) [hadoop@dn01 pig_data]$ pig -x local
~~~

    - pig_data
~~~
1) [hadoop@dn01 pig_data]$ hdfs dfs -mkdir -p /input/pig_data
2) [hadoop@dn01 pig_data]$ hdfs dfs -ls /input/pig_data
3) [hadoop@dn01 pig_data]$ hdfs dfs -put ./* /input/pig_data
4) [hadoop@dn01 pig_data]$ hdfs dfs -ls /input/pig_data
5) [hadoop@dn01 pig_data]$ pig -x local
6) grunt> groceries = load 'file:///home/hadoop/pig_data/data/groceries.csv' using PigStorage(',');
7) grunt> dump groceries
~~~

## 정리
* 행렬곱
    - 곱셈 결과 나오는 행렬의 크기는 (앞 행렬의 행의 수)×(뒤 행렬의 열의 수)가 됩니다. 즉, 앞 행렬이 m * n 크기이고 뒤 행렬이 n * r 크기인 경우 곱은 m * r 크기의 행렬이 된다.