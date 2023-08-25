from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateStripeCheckoutSessionView,StripeWebhookView

#app_name = "products"

urlpatterns = [
    path('',views.tienda,name='inicio'),
    path('detail/<int:id>/', views.producto_detail, name='detalles'),
    path('vercarro/',views.vercarro,name='vercarro'),
    path(
        "create-checkout-session/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path("success/", views.success, name="success"),
    path("webhooks/stripe/", StripeWebhookView.as_view(), name="stripe-webhook"),
    path("search/<str:search>/", views.search, name="search"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)