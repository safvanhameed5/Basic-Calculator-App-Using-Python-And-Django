from django.shortcuts import render
from django.http import HttpResponse
from .forms import HomeForm

def homepage(request):

    if request.method == "GET":
        form = HomeForm()
        return render(request, 'main/home.html', {'form': form})

    elif request.method == "POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            
            num1 = form.cleaned_data.get('number1')
            num2 = form.cleaned_data.get('number2')
            num3 = form.cleaned_data.get('number3')
            num4 = form.cleaned_data.get('number4')

        
            result = None

            try:
                if 'add' in request.POST:
                    
                    result = sum(x for x in [num1, num2, num3, num4] if x is not None)
                elif 'sub' in request.POST:
                    
                    numbers = [x for x in [num1, num2, num3, num4] if x is not None]
                    if numbers:
                        result = numbers[0] - sum(numbers[1:])
                    else:
                        result = 0
                elif 'mul' in request.POST:
                    
                    numbers = [x for x in [num1, num2, num3, num4] if x is not None]
                    if numbers:
                        result = 1
                        for number in numbers:
                            result *= number
                    else:
                        result = 0
                elif 'div' in request.POST:
                    
                    numbers = [x for x in [num1, num2, num3, num4] if x is not None]
                    if numbers:
                        result = numbers[0]
                        for number in numbers[1:]:
                            if number == 0:
                                return HttpResponse("<h1>Error: Division by zero is not allowed!</h1><a href='/'>Back To Calculator</a>")
                            result /= number
                    else:
                        result = 0

            except Exception as e:
                return HttpResponse(f"<h1>Error: {e}</h1>")

            
            form = HomeForm()
            args = {'form': form, 'result': result}
            return render(request, 'main/home.html', args)

    return HttpResponse("<h1>Invalid Request</h1><a href='/'>Back To Calculator</a>")
