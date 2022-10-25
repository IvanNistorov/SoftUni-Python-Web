from django import forms

from games.profiles.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')

        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        labels = {
            'image': 'Image URL',
        }


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        labels = {
            'image': 'Image URL',
        }


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Game
        fields = '__all__'

        labels = {
            'image': 'Image URL',
        }
