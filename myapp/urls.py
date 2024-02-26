from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index, name='my_index'),
    path('about/', views.about, name='my_about'),
    path('contact/', views.contact, name='my_contact'),
    path('product/', views.products, name='my_products'),
    path('testimonial/',views.testimonial,name='my_testimonial')

]



