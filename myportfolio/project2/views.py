from django.shortcuts import render

# Create your views here.
def project2(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """

    context = {
        "key": 0,
    }
    return render(request, 'Project2\proyect2.html', context)