from django.shortcuts import render

# Create your views here.
def home_func(request):
    num = 0
    if request.method == 'POST':
        
        option = request.POST.get('options')
        if option == 'us':
            num += 109.71
            curr1= 'USD'
            curr2= 'BDT'
        elif option =='bd':
            num += 0.0091
            curr1= 'BDT'
            curr2 = 'USD'
    
        input_str = request.POST.get('usd')
        try: 
            input_int = int(input_str)
            total = input_int*num
        except ValueError:
            usd = None
            print('value error')
        
        
    return render(request,'index.html',locals())