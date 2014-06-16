from django.http import (HttpResponseRedirect,
                         HttpResponse)
from user import forms as user_forms
from django.contrib.auth import (authenticate,
                                 login)
from django.shortcuts import render_to_response, render
from django.contrib.auth import logout

def home(request):
    return render_to_response('index.html')

# View for Register page
def register(request):
    """
    A boolean value for telling the template
    whether the registration was successful.
    Set to False initially. Code changes value
    to True when registration succeeds.
    """

    registered = False


    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = user_forms.UserForm(data=request.POST)
        profile_form = user_forms.UserLoginProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save(commit=False)

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            """
            Now sort out the UserProfile instance.
            Since we need to set the user attribute ourselves, we set
            commit=False.
            This delays saving the model until we're ready to avoid
            integrity problems.
            """
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            """
            Update our variable to tell the template registration
            was successful.
            """

            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = user_forms.UserForm()
        profile_form = user_forms.UserLoginProfileForm()

    # Render the template depending on the context.
    return render(request, 'register.html', {'user_form': user_form,
                                             'profile_form': profile_form,
                                             'registered': registered})


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')


def bye(request):
    return HttpResponse("bye bye")
