from django import forms
from .models import Category, Post
from django.core.exceptions import ValidationError


# class CategoryForm(forms.ModelForm):
    
#     class Meta:
#         model = Category
#         fields = '__all__'

class PostForm(forms.ModelForm):
    category_choice = forms.ModelChoiceField(queryset=Category.objects.all(),
                                             required = False,
                                             label="choose an category")
    
    category_name = forms.CharField(max_length=50,required=False,label='create new category')
    class Meta:
        model = Post
        fields = ['post_title','post_text']

    def clean(self):
        cleaned_data = super().clean()
        category_choice = cleaned_data.get('category_choice')
        category_name = cleaned_data.get('category_name')
        
        if not category_choice and not category_name:
            raise ValidationError('category_choice or category_name neccessary')

        if category_choice and category_name:
            raise ValidationError('Please choose one Not Both')

        return cleaned_data
        

    def save(self, commit = True):
        category_choice = self.cleaned_data.get('category_choice')
        category_name = self.cleaned_data.get('category_name')

        # setting the instance's category field
        if category_choice:
            self.instance.post_category = category_choice 
        elif category_name:
            category, created = Category.objects.get_or_create(category_name = category_name)

            self.instance.post_category = category 

        
        return super().save(commit)