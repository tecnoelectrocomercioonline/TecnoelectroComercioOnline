

def HomeForm(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
    if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado con exito')
            return redirect('index')
    else:
        form = HomeForm()
    return render(request, 'shop/body.html', {'form': form})
