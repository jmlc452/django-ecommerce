from app_carro.carro import Carro

def importe_total_carro(request):
    total=0
    if request.user.is_authenticated:
        
        carro = request.session.get("carro")
        if carro is not None:
            for key,value in request.session["carro"].items():
                total = total+(float(value["preciototal"]))
        else:
            carro=Carro(request)
    else:
        total="debes hacer login"    
    return {"importe_total_carro":total}        