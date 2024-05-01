from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_func(request):
    if request.method == 'POST':
        # Retrieve the selected option from the form
        option = request.POST.get('options')
        
        # Check if option is 'option1' and print a message
        if option == 'option1':
            print('all are okay')

        # Retrieve the value of 'usd' from the form
        usd_str = request.POST.get('usd')
        
        try:
            # Convert 'usd_str' to an integer
            usd = int(usd_str)
            
            # Calculate 'bdt' based on the converted 'usd'
            bdt = usd * 109.67
        except ValueError:
            # If 'usd_str' cannot be converted to an integer, set 'usd' to None
            usd = None
            print('value error')

    # Render the 'index.html' template and pass local variables to the template
    return render(request, 'index.html', locals())
