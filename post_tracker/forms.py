from django import forms


class TrackForm(forms.Form):
    track_id = forms.CharField(max_length=20)
