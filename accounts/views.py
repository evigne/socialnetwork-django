from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash #to make sure that the user is still logged in after the password reset

def home(request):
	numbers=[1,2,3,4,5]
	name='Vigneshwaran'
	args = {'myName':name, 'numbers':numbers}
	return render(request,'accounts/home.html',args)

def register(request):
	"""Registration form"""
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('/account')
		else:
			print(form.errors)

	else:
		# for the first time its going to be a GET method, so just a empty form to handle that request
		#user need to register for the first time, so the form = UserCreationForm() and then passing the argument to the reg_form.html
		form = RegistrationForm()
		args={'form':form}
		return render(request,'accounts/reg_form.html',args)


def view_profile(request):
	args = {'user':request.user}
	return render(request,'accounts/profile.html',args)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/account/profile')
		else:
			redirect('account/profile/edit')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form':form}

		return render(request,'accounts/edit_profile.html',args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user) #not instance it should be user
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)  # user of the particular form 
			return redirect('/account/profile')
		else:
			return redirect('/account/change-password')
	else:
		form = PasswordChangeForm(user=request.user) #not instance it should be user
		args = {'form':form}

		return render(request,'accounts/change_password.html',args)


