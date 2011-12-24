from django import forms

class LoginForm(forms.Form):
	name = forms.CharField()  
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class ComposeForm(forms.Form):
	to = forms.CharField()
	cc = forms.CharField()
	bcc = forms.CharField()
	subject = forms.CharField()
	message = forms.CharField(widget=forms.widgets.Textarea(attrs={'cols':'80', 'rows':'15'}))
	
