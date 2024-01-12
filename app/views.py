from django.shortcuts import render

# Create your views here.
def prime(request):
    data = {'msg': ' '}
    if request.method == 'POST':
        value = request.POST.get("Prime")
        value = int(value)
        fcount=0
        for f in range (1, value+1):
            if (value %f == 0):
                fcount +=1
        if fcount == 2:
            data['msg'] = 'This is prime Number'
        else:
            data['msg'] = 'No, This is not a prime Number'

    return render(request, 'number.html', data)