from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
import markdown
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from pure_pagination import PageNotAnInteger, Paginator
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from .service.tools import serach_key

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    # 这个地方后续优化要改一下

    article_num = 10   # 每页展示的博客数目

    # 分页
    page = request.GET.get('page', 1)
    p = Paginator(post_list, article_num, request=request)  
    post_list = p.page(page)

    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            # 'markdown.extensions.toc',
            TocExtension(slugify=slugify),
        ]
    )
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def search(request):
    q = request.GET.get('q')

    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')

    post_list = serach_key(q)
    # print(len(post_list))
    # print([x.title for x in post_list])
    # return render(request, 'blog/index.html', {'post_list': post_list})

    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })




