from django.shortcuts import render

# Create your views here.


def all_documents(request):
    # id_user  = request.session['entry_user']
    print("!!!!!!!!!!!!!!" , request.path)

    return render(request , 'all_document.html', {})