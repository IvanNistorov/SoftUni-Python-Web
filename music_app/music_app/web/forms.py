from django import forms

from music_app.web.models import Profile, Album


class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Age'
            })
        }


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        labels = {
            'image': 'Image URL',
        }

        widgets = {
            'album_name': forms.TextInput(attrs={
                'placeholder': 'Album Name'
            }),
            'artist': forms.TextInput(attrs={
                'placeholder': 'Artist'
            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'Description'
            }),
            'image': forms.URLInput(attrs={
                'placeholder': 'Image URL'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price'
            }),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
