from django import forms
from django.core.exceptions import ValidationError  # 校验错误

from post.models import Topic


class TopicSearchForm(forms.Form):
    title = forms.CharField(
        label='话题标题', initial='Django BBS', help_text='帮助信息')


class TopicField(forms.Field):
    default_error_messages = {
        'invalid': '输入一个整数',
        'not_exist': '模型不存在',
    }

    def to_python(self, value):
        try:
            value = int(str(value).strip())
            return Topic.objects.get(pk=value)
        except (ValueError, TypeError):
            # 团子注：ValidationError 的第一个参数是错误信息，第二个参数是通过关键字指定的错误代码
            raise ValidationError(
                self.error_messages['invalid'], code='invalid')
        except Topic.DoesNotExist:
            raise ValidationError(
                self.error_messages['not_exist'], code='not_exist')


class SignField(forms.CharField):
    def clean(self, value):
        return 'django %s' % super().clean(value)

def even_validator(value):
    if value % 2 != 0:
        raise ValidationError('%d is not a even number' % value)


class EvenField(forms.IntegerField):
    def __init__(self, **kwargs):
        super().__init__(validators=[even_validator], **kwargs)


class TopicSearchForm(forms.Form):
    title = forms.CharField(label='Topic title')

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError('字符串长度太短')
        return title
    

class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ('is_online', 'user')
        labels = {
            'title': '标题label',
            'content': '内容label',
        }
