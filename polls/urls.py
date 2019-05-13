# from django.urls import path

# from . import views

# # Question: 
# # Su dung name de xac dinh url trong file html, tuy nhien mot project co the co rat nhieu app.
# # Neu moi app lai co cac url giong nhau. Vi du: app1/detail, app2/detail. Lam the nao de url trong file 
# # html co the xac dinh duoc la render detail cua app1 hay detail cua app2? 
# #
# # Answer: 
# # Su dung app_name, thay vi 'detail' chung ta se dung url 'app1:detail' hoac 'app2:detail'
# # Namespacing URL names

# app_name='polls' 
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# --------------------------------------------------------------------------------------------------------

# Use generic views: Less code is better

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]