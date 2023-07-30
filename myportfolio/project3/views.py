from django.shortcuts import render
from .forms import fileForm
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse

def project3(request):


    if request.method == "POST":
        
        # create a form instance and populate it with data from the request:
        form = fileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            file = form.cleaned_data.get('file')
            with open(file, encoding="utf8") as f:
                lines = f.readlines()
            msgs = []
            for mss in lines:
                 x = re.findall("\: (.*)$", mss)
                 if len(x)>0:
                    if x[0] != '<Multimedia omitido>':
                        msgs.append(x[0])
            #convert list to string and generate
            unique_string=(" ").join(msgs).replace('y','').replace('que','')
            wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
            plt.figure(figsize=(15,8))
            plt.imshow(wordcloud)
            plt.axis("off")
            fig = plt.figure()

            response = HttpResponse(content_type = 'image/png')
            canvas = FigureCanvasAgg(fig)
            canvas.print_png(response)
            print('yes')
            return render(request, 'Project2\proyect2.html',  {"form": form})
        
    form = fileForm()
    context = {
        "key": 0,
    }
    print('no')
    return render(request, 'Project3\proyect3.html',  {"form": form})