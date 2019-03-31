django startproject projectname
django-admin startapp appname

= app.views.py

 ->appname.views has several view methods which get triggered with different urls-mapping!
    generally, this .view methods takes parametere request and return HttpResponse('')!
    view methods also make view from a html page using --
        return render(request, 'UserServiceApp/register.html')
            @ directory should be -- appname/templates/appname/index.html
            @ enter appname.apps.appnameConfig in INSTALLED_APPS in projectname.settings
            --> this entry ensures correct template & model recognization from the app!
    remember::
        view method render diye html page reutrn kore!
        render thake view method er vitore, return render(request, 'blog/haha.html')!

    views along with showing html page, they can also send data to the html page!
    return render(request, 'blog/home.html', {'posts':'posts'})

    <a href="{% url 'blog-home' %}">Django Blog</a>  --->  {% load static %}
    we can refer to a different {{ url-mapping + view-method }} by {% url 'name_in_path_urls.py'%}

    template inherritance == {% extends "blog/base.html" %}


= app.urls.py

    from django.urls import path,include
    project.urls e, path('blog/', include('blog.urls'))
        from . import views
        appname.urls e path('home/', views.method_name, name="django-view-name")

projectname.urls is generally the url-mapping get the main apps!
appname.urls defines subdirectory url-mapping which directs to from appname.views methods!















# appname.urls gives the subdirectory to the app's different view methods & services!

#


SQL::: 
