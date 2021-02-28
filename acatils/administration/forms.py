from django.forms import ModelForm


from core.models import News, Categories, get_file_path

from stdimage.models import StdImageField

class NewsRegisterForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'category', 'img', 'text', 'author']