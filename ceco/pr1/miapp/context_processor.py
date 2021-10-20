
def total_invoice(request):
    total = 0

    if request.user.is_authenticated:
        if "trolley" in request.session.keys():
            for key, value in request.session['trolley'].items():
                total += float(value['price'])
    return{'total_invoice':total}