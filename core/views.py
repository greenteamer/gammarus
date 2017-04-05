# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from core import models
from django.core.mail import send_mail
from project.settings import ADMIN_EMAIL
# Create your views here.


def index_view(request, template_name='core/index.html'):
    title = "Главная | товары народной медицины gammarus.ru"
    description = "Магазин товаров народной медецины gammarus.ru. Бобровая струя, медвежий жир и другие товары у нас."
    products = models.Product.objects.all()
    popularProducts = models.Product.objects.filter(isPopular=True)
    about = get_object_or_404(models.Page, slug="about")
    return render(request, template_name, {
        "title": title,
        "description": description,
        "about": about,
        "products": products,
        "popularProducts": popularProducts,
    })


def catalog_view(request, slug, template_name='core/index.html'):
    category = get_object_or_404(models.Category, slug=slug)
    title = u"{}".format(category.meta_title)
    description = u"{}".format(category.meta_description)
    request.breadcrumbs([(category.name, category.absoluteUrl)])
    products = models.Product.objects.filter(category=category)
    return render(request, template_name, {
        "title": title,
        "description": description,
        "title": title,
        "description": description,
        "products": products,
    })


def product_view(request, categorySlug, slug, template_name='core/product.html'):
    category = get_object_or_404(models.Category, slug=categorySlug)
    product = get_object_or_404(models.Product, category=category, slug=slug)
    title = u"{}".format(product.meta_title)
    description = u"{}".format(product.meta_description)
    reviews = models.Review.objects.filter(product=product)
    attachedProducts = models.Product.objects.filter(attached=product)
    popularProducts = models.Product.objects.filter(isPopular=True)
    request.breadcrumbs([(category.name, category.absoluteUrl), (product.name, product.absoluteUrl)])
    return render(request, template_name, {
        "title": title,
        "description": description,
        "category": category,
        "product": product,
        "reviews": reviews,
        "attachedProducts": attachedProducts,
        "popularProducts": popularProducts,
    })


def page_view(request, slug, template_name='core/page.html'):
    page = get_object_or_404(models.Page, slug=slug)
    title = u"{}".format(page.meta_title)
    description = u"{}".format(page.meta_description)
    request.breadcrumbs([(page.name, page.get_absolute_url)])
    return render(request, template_name, {
        "title": title,
        "description": description,
        "page": page,
    })


def article_view(request, slug, template_name='core/article.html'):
    article = get_object_or_404(models.Article, slug=slug)
    title = u"{}".format(article.meta_title)
    description = u"{}".format(article.meta_description)
    request.breadcrumbs([(u"Статьи", '/articles/'), (article.name, article.get_absolute_url)])
    return render(request, template_name, {
        "title": title,
        "description": description,
        "article": article,
    })


def article_list_view(request, template_name='core/article_list.html'):
    articles = models.Article.objects.all()
    title = u"Статьи | товары народной медицины gammarus.ru"
    description = u"Статьи на тему здоровья"
    request.breadcrumbs([(u"Статьи", '/articles/')])
    return render(request, template_name, {
        "title": title,
        "description": description,
        "articles": articles,
    })


def news_view(request, slug, template_name='core/news.html'):
    news = get_object_or_404(models.News, slug=slug)
    title = u"{}".format(news.meta_title)
    description = u"{}".format(news.meta_description)
    request.breadcrumbs([(u"Новости", '/news/'), (news.name, news.get_absolute_url)])
    return render(request, template_name, {
        "title": title,
        "description": description,
        "news": news,
    })


def news_list_view(request, template_name='core/news_list.html'):
    news = models.News.objects.all()
    title = u"Новости | товары народной медицины gammarus.ru"
    description = u"Наши новости"
    request.breadcrumbs([(u"Новости", '/news/')])
    return render(request, template_name, {
        "title": title,
        "description": description,
        "news": news,
    })


def reivew_view(request, slug, template_name='core/review.html'):
    review = get_object_or_404(models.Review, slug=slug)
    title = u"{}".format(review.meta_title)
    description = u"{}".format(review.meta_description)
    request.breadcrumbs([(u"Отзывы", '/reviews/'), (review.name, review.get_absolute_url)])
    return render(request, template_name, {
        "title": title,
        "description": description,
        "review": review,
    })


def review_list_view(request, template_name='core/review_list.html'):
    reviews = models.Review.objects.all()
    title = u"Отзывы | товары народной медицины gammarus.ru"
    description = u"Отзывы о наших продуктах"
    request.breadcrumbs([(u"Отзывы", '/reviews/')])
    return render(request, template_name, {
        "title": title,
        "description": description,
        "reviews": reviews,
    })


def contact_form(request, template_name='core/contact_form.html'):
    if request.method == 'POST':
        print "**** request.POST: %s" % request.POST
        send_mail(
            u'Заявка на звонок',
            u'Телефон: %s' % request.POST['phone'],
            'teamer777@example.com',
            [ADMIN_EMAIL, ],
            fail_silently=False,
        )
    return render(request, template_name, {})
