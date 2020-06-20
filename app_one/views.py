from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print("got here on redirect")
    return render(request,'index.html')
    

def results(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'loc': request.POST['location'],
            'lang': request.POST['language']
        }
        
        return render(request, 'results.html', context)
    return redirect("/")
    # return render(request, 'results.html')
   
def some_function(request):
    request.session['name'] = request.POST['name']
    request.session['lang'] = request.POST['lang']
