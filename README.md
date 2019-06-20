# celery demo

看别人描述大概就是说win10上运行celery4.x就会出现这个问题，解决办法如下,原理未知：

先安装一个`eventlet
```bash
pip install eventlet
```

1
然后启动worker的时候加一个参数，如下：
```bash
celery -A <mymodule> worker -l info -P eventlet
```

#### 执行任务调度
```bash
celery beat  -A celery_demo -l INFO
```

#### 参考文献
- [Celery ValueError: not enough values to unpack (expected 3, got 0)的解决方案](https://blog.csdn.net/qq_30242609/article/details/79047660)