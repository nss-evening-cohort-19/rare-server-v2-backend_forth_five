from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rarev2api.views import register_user, check_user
from rarev2api.views import UserView, PostView, CommentView, CategoryView, ReactionView, PostReactionView, TagView, PostTagView, SubscriptionView
"""rarev2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'posts', PostView, 'post')
router.register(r'comments', CommentView, 'comment')
router.register(r'categories', CategoryView, 'category')
router.register(r'reactions', ReactionView, 'reaction')
router.register(r'post_reactions', PostReactionView, 'post_reaction')
router.register(r'tags', TagView, 'tag')
router.register(r'post_tags', PostTagView, 'post_tag')
router.register(r'subscriptions', SubscriptionView, 'subscription')

urlpatterns = [
# Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
# Requests to http://localhost:8000/checkuser will be routed to the login_user function
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
