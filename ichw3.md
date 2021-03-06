**组成结构**
==
高速缓存存储器是存在于主存与CPU之间的一级存储器，由静态存储芯片(SRAM)组成，容量比较小但速度比主存高得多，接近于CPU。主要由三部分组成：  
*1.Cache存储体*：存放由主存调入的指令与数据块；  
*2.地址转换部件*：建立目录表以实现主存地址到缓存地址的转换；  
*3.替换部件*：在缓存已满时按一定策略进行数据块替换，并修改地址转换部件。

**工作原理**
==
高速缓冲存储器通常由高速存储器、联想存储器、替换逻辑电路和相应的控制线路组成。在有高速缓冲存储器的计算机系统中，中央处理器存取主存储器的地址划分为行号、列号和组内地址三个字段。于是，主存储器就在逻辑上划分为若干行；每行划分为若干的存储单元组；每组包含几个或几十个字。高速存储器也相应地划分为行和列的存储单元组。二者的列数相同，组的大小也相同，但高速存储器的行数却比主存储器的行数少得多。  
<br/>当中央处理器存取主存储器时，硬件首先自动对存取地址的列号字段进行译码，以便将联想存储器该列的全部行号与存取主存储器地址的行号字段进行比较：若有相同的，表明要存取的主存储器单元已在高速存储器中，称为命中，硬件就将存取主存储器的地址映射为高速存储器的地址并执行存取操作；若都不相同，表明该单元不在高速存储器中，称为脱靶，硬件将执行存取主存储器操作并自动将该单元所在的那一主存储器单元组调入高速存储器相同列中空着的存储单元组中，同时将该组在主存储器中的行号存入联想存储器对应位置的单元内。   

**CACHE-主存存储层次**   
--
在CPU与主存之间设置高速缓存存储器，构成Cache-主存层次，要求Cache在速度上能跟得上CPU的要求。Cache-主存间的地址映象和调度吸取了比它较早出现的主-辅存存储层次的技术，不同的是因其速度要求高，不是由软、硬件结合而完全由硬件来实现。  
![images](https://github.com/caijiahao2018/ichw/blob/master/baidu1.png)   

**地址映像与转换**
--  
地址映像是指某一数据在内存中地址与缓存中地址，两者之间对应关系。  

**1.全相联方式**  
地址映像规则：主存的任意一块可以映像到Cache中任意一块。  
(1)主存与缓存分成大小相同的数据块；
(2)主存的某一数据块可以装入缓存的任意一块空间中。  
全相联方式的对应关系如图，若Cache的块数为C，主存块数为M，则映像关系共有CM种。  
![images](https://github.com/caijiahao2018/ichw/blob/master/baidu2.png)  
**直接相联方式**  
地址映像规则：主存储器中一块只能映像到Cache的一个特定块中。    
(1)主存与缓存分成大小相同的数据块；    
(2)主存容量应是缓存的整数倍，将主存空间按缓存的容量分成区，主存中每一区块数与缓存的总块数相等；    
(3)主存中某区的一块存入缓存时只能存入缓存中块号相同的位置。  
![images](https://github.com/caijiahao2018/ichw/blob/master/baidu6.png)  
![images](https://github.com/caijiahao2018/ichw/blob/master/untitled.png)  
**组相联方式**  
组相联映像规则：  
(1)主存与Cache按同样大小划分成块；  
(2)主存与Cache按同样大小划分成组；  
(3)主存容量是缓存容量的整数倍，将主存空间按缓存区的大小分成区，主存中每一区的组数与缓存组数相同；  
(4)当主存的数据调入缓存时，主存与缓存的组号相等，也就是各区的某一块只能存入缓存的相同组号空间，但组内各块地址之间可以任意存放，即从主存的组到Cache的组之间采用直接映像方式；在两个对应的组内采用全相联映像方式。  
![images](https://github.com/caijiahao2018/ichw/blob/master/baidu5.png)   

**替换策略**
--
 根据程序局部性规律可知：程序在运行中，总是频繁地使用那些最近被使用过的指令和数据。这就提供了替换策略的理论依据。综合命中率、实现的难易及速度的快慢各种因素，替换策略可有随机法、先进先出法、最近最少使用法等。  
（1）随机法（RAND法）  
随机法是随机地确定替换的存储块。设置一个随机数产生器，依据所产生的随机数，确定替换块。这种方法简单、易于实现，但命中率比较低。  
（2）先进先出法（FIFO法）  
先进先出法是选择那个最先调入的那个块进行替换。当最先调入并被多次命中的块，很可能被优先替换，因而不符合局部性规律。这种方法的命中率比随机法好些，但还不满足要求。先进先出方法易于实现。  
（3）最近最少使用法（LRU法）  
LRU法是依据各块使用的情况， 总是选择那个最近最少使用的块被替换。这种方法比较好地反映了程序局部性规律。 实现LRU策略的方法有多种。



