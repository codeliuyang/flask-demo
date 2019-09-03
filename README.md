# Flask Demo

> 项目旨在使用Flask作为API微服务的开发框架

Python版本如下
```
$ python --version
Python 3.6.1
```


## Develop

以下为开发中常见的说明

#### 1.切换pip的源
建议使用国内的镜像源


#### 2.编码风格指南
严格遵循PEP8，以下列举常见规范
- 文件名：全小写,可使用下划线
- 类名称：采用骆驼拼写法
- 方法与函数名：小写_以及_下划线
- 私有方法与函数名：以 __ 开头（2个下划线），其他和普通函数一样
- 变量名：小写_以及_下划线
- 私有变量名称：以 __开头（2个下划线），其他和普通变量一样
- 常量：大写_以及_下划线
- 缩进：4个空格，不能使用Tab制表符，没有例外

## Install

1. 手动添加的依赖脚本如下
```
$ pip install flask
$ pip install flask-restful
$ pip install Flask-SQLAlchemy
$ pip install PyMySQL
```

2. 如何自动生成依赖清单

使用```pipreqs```会在项目根目录生成requirements.txt，不过实际下来差了一个```PyMySQL==0.9.3```需要手动补上。
```
$ pip install pipreqs
$ cd [项目根目录]
// 如果是windows环境下，需要加上编码
$ pipreqs ./ --encoding=utf8
```

一键下载所有的包
```
pip install -r requirements.txt
```

## Usage

```
```

## Common Questions
- ```__name__``` 代表什么意思？

```__name__``` 是当前模块名，当模块被直接运行时模块名为 ```__main__``` 。

- python中的模块怎么理解？

在Python中，一个.py文件就是一个模块，一般情况下，模块的名字就是文件名(不包括扩展名.py)。
全局变量__name__存放的就是模块的名字。


## Contributing

PRs accepted.

## License

MIT © Richard McRichface


