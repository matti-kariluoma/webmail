from django import forms

class LoginForm(forms.Form):
	name = forms.CharField()  
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class ComposeForm(forms.Form):
	to = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
	cc = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
	bcc = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
	message = forms.CharField(widget=forms.widgets.Textarea(attrs={'cols':'80', 'rows':'15'}))
	
