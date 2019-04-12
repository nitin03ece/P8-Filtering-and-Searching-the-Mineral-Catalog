from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label=False)

    def clean_search(self):
        search = self.cleaned_data.get('search')
        if len(search) <= 0:
            raise forms.ValidationError("Please atleast one word is required")
        return search
