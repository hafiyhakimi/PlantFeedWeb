from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def payment(request):
        try:
            data=Payment.objects.all()
            return render(request,'Payment.html',{'data':data})
        except Payment.DoesNotExist:
            raise Http404('Data does not exist')

        market = Marketplace(request)
        total = float(market.price)

    stripe.api_key = 'pk_test_51M4MnSIMiEP0GJmrTjOFwVfxpZ5KRfUJfHYNTfiEHQ1TlwaQBJxclgibBE0VBYeRRJs85bnPAH0bAzytGUdeqB6i00TbB5FJ8Y'
    intent = stripe.PaymentIntent.create(
        amount=total,
    )