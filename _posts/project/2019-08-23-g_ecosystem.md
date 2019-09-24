---
layout: post
title: ecosystem
category: project
tags: [python, project, ecosystem]
comments: false
---

# [ecosystem]()

## zeppelin
* 설치
~~~
1) [root@dn01 ~]# cd /tmp
2) [root@dn01 tmp]# wget http://apache.mirror.cdnetworks.com/zeppelin/zeppelin-0.8.1/zeppelin-0.8.1-bin-all.tgz 
3) [root@dn01 tmp]# tar xzvf zeppelin-0.8.1-bin-all.tgz
4) [root@dn01 tmp]# mkdir -p /opt/zeppelin/0.8.1
5) [root@dn01 tmp]# mv zeppelin-0.8.1-bin-all/* /opt/zeppelin/0.8.1
6) [root@dn01 tmp]# ln -s /opt/zeppelin/0.8.1 /opt/zeppelin/current
7) [root@dn01 tmp]# chown -R hadoop:hadoop /opt/zeppelin/
8) [root@dn01 tmp]# su - hadoop
~~~

* 환경변수 설정
~~~shell
1) [hadoop@dn01 ~]$ vi ~/.bash_profile
########### zeppelin 0.8.1 ########
export ZEPPELIN_HOME=/opt/zeppelin/current
export PATH=$PATH:$ZEPPELIN_HOME/bin
########### zeppelin 0.8.1 ########
2) [hadoop@dn01 ~]$ source ~/.bash_profile
~~~

* zeppelin 환경변수 설정
~~~shell
1) [hadoop@dn01 ~] cd $ZEPPELIN_HOME/conf
2) [hadoop@dn01 conf] $ mv zeppelin-site.xml.template zeppelin-site.xml
3) [hadoop@dn01 conf] vi zeppelin-site.xml    # Value값만 변경
########### zeppelin-site.xml ############
# <property>
# <name>zeppelin.server.addr</name>
# <value>192.168.56.102</value>
# <description>Server address</description>
# </property>
# <property>
# <name>zeppelin.server.port</name>
# <value>8888</value>      # 8080이 사용중이면 다른 번호로 바꿈/8088 또는 6060 등
# <description>Server port.</description>
# </property>
########### zeppelin-site.xml ############
4) [hadoop@dn01 conf]$ mv zeppelin-env.sh.template zeppelin-env.sh
5) [hadoop@dn01 conf] $ vi zeppelin-env.sh
########### zeppelin-env.sh ###########
export ZEPPELIN_PORT=8888       # 밑에 추가 입력
export SPARK_HOME=/opt/spark/current
export JAVA_HOME=/opt/jdk/current
########### zeppelin-env.sh ###########
6) [hadoop@dn01 conf] $ mv shiro.ini.template shiro.ini
7) [hadoop@dn01 conf] vi shiro.ini  # 기존 추가
########### shiro.ini ###########
#/api/version = anon
#/** = anon
/** = authc
##################################
admin = admin, admin
#admin = password1
#user1 = password2, role1, role2
#user2 = password3, role3
#user3 = password4, role2
########### shiro.ini ###########
8) [hadoop@dn01 ~] cd $ZEPPELIN_HOME
9) [hadoop@dn01 current] ./bin/zeppelin-daemon.sh restart    # 설정변경 후 재시작
~~~

* 실행
~~~shell
1) [hadoop@dn01 ~] hive --servie hiveserver2    # hive 사용시 하이브서버킨 후 실행
1) [hadoop@dn01 ~] cd $ZEPPELIN_HOME
2) [hadoop@dn01 current] ./bin/zeppelin-daemon.sh start
3) http://192.168.56.102:8888
~~~

* zeppelin 정지
~~~
1) [hadoop@dn01 current] ./bin/zeppelin-daemon.sh stop
~~~

* Hive 인터프리터 Zeppelin 추가하기
    - http://192.168.56.102:8888 접속후
    - admin 권한의 유저로 로그인
    - admin > Interperter 메뉴 클릭
    - Create 클릭후 내용 입력
~~~
1) Interperter Name 
Interperter Name    hive
Interperter group   jdbc
2) Properties
default.driver	        org.apache.hive.jdbc.HiveDriver
default.url	            jdbc:hive2://localhost:10000
default.user	        hiveUser
default.password	    hivePassword
3) Dependencies
org.apache.hive:hive-jdbc:0.14.0	
org.apache.hadoop:hadoop-common:2.6.0
~~~
