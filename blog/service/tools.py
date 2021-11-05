from ..models import Post


# 手动匹配文章标题和内容，检索关键字
def serach_key(p):
    # print("进入serach_key函数")
    post_all = Post.objects.all()

    post_list = []
    for post in post_all:
        if (p in post.title) or (p in post.body):
            # print(post.title)
            post_list.append(post)
    
    return post_list


## 数据库增删改查练习




