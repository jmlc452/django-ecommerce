from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import producto,categoria_producto
from app_carro.carro import Carro
import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from app_carro.context_processor import importe_total_carro
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import re


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """
    def post(self, request, *args, **kwargs):
        data = importe_total_carro(request)

        importe_total = data['importe_total_carro']
        lista_productos = "--".join(item[1]['nombre'] for item in request.session["carro"].items())
        
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(importe_total) * 100,
                        "product_data": {
                            "name": "Compra en EShopper",
                            "description": lista_productos,
                            
                        },
                    },
                    "quantity": 1,
                }
            ],
            metadata={"product_id": 1},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)


# Create your views here.
def tienda(request):
    carro=Carro(request)
    is_logout = request.GET.get('is_logout')
    
    if is_logout:
        messages.success(request, "You have been successfully logged out.")
    
    prod = producto.objects.all()
    query = request.GET.get('barrabusqueda')
    if query:
        resultados = producto.objects.filter(nombre__icontains=query)
        return render(request, 'tienda/resultados.html', {'mostrar_resultados': resultados})
    
    return render(request, 'tienda/tienda.html',{
        'prod':prod,
    }) 
    
def search(request,search):
    #filtro = re.compile(rf'\b{search}\b', re.IGNORECASE)
    resultados = producto.objects.filter(nombre__icontains=search)
    print(resultados)
    return render(request, 'tienda/resultados.html', {'mostrar_resultados': resultados})
    
def producto_detail(request,id):
    obj = get_object_or_404(producto, id=id)
    prod = producto.objects.all()
    
    return render(request,'tienda/detalles.html',{
        'producto':obj,
        'productos':prod
        
    })
    
    
def vercarro(request):
    return render(request,'carro/carro.html')

def success(request):
    return render(request,'success.html')

@method_decorator(csrf_exempt, name="dispatch")
class StripeWebhookView(View):
    """
    Stripe webhook view to handle checkout session completed event.
    """

    def post(self, request, format=None):
        payload = request.body
        endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
        sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
        event = None

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)

        if event["type"] == "checkout.session.completed":
            print("Payment successful")

        # Can handle other events here.

        return HttpResponse(status=200)
