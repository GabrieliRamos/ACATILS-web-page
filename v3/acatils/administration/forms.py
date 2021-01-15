from django import forms


from core.models import News, Categories

from stdimage.models import StdImageField

class NewsRegisterForm(forms.Form):
    title = forms.CharField(label='Título', max_length=300)
    category = forms.CharField(label='core.Categories')
    img = forms.ImageField(label='Imagem', required=False)
    author = forms.CharField(label='Autor', max_length=200)
    text = forms.CharField(label='Texto', widget=forms.Textarea())

    def save_news(self):
        title = self.cleaned_data['title']
        category = self.cleaned_data['category']
        if category == 'op1':
            category = Categories.objects.get(id=3)
        else:
            category = Categories.objects.get(id=4)

        img = self.cleaned_data['img']
        author = self.cleaned_data['author']
        text = self.cleaned_data['text']

        new_news = News(title=title, category=category, img=img, author=author, text=text)
        new_news.save()


    