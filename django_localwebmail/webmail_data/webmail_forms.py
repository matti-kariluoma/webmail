from django import forms

class LoginForm(forms.Form):
	name = forms.CharField()  
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class ComposeForm(forms.Form):
	to = forms.CharField(attrs={'size': '80'})
	cc = forms.CharField(attrs={'size': '80'})
	bcc = forms.CharField(attrs={'size': '80'})
	subject = forms.CharField(attrs={'size': '80'})
	message = forms.CharField(widget=forms.widgets.Textarea(attrs={'cols':'80', 'rows':'15'}))
	
