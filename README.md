
之前博客崩辽，想着扩展和开发也都不简单，不如干脆自己写一个，
正好明天就十一假期，趁这个假期看看能不能开发完成  --> 假期没有完成~

-V
Python==3.6.4
django==2.2.3

# 一级标题
## 二级标题
### 三级标题
#### 四级标题

#### 无序列表
* 1
* 2
* 3

#### 有序列表
1. 1
2. 2
3. 3

> 这里是引用的一段话

要注意符号和文本之间的空格

#### 插入链接
[陈小陌博客](http://www.mylwx.cn)



#### 插入图片
![图片](https://cdn.sspai.com/attachment/origin/2014/04/15/69495.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

#### 粗体和斜体
**这是粗体**
*这是斜体*

#### 代码块
``` python
for i in range(6):
        print(666)
```

#### 另一个代码块

``` python
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})
```