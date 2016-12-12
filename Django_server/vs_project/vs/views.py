from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from vs.models import PointOfInterest
from vs.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from glob import glob
import commands, os, sys

def encode_url(str):
        return str.replace(' ', '_')

def decode_url(str):
        return str.replace('_', ' ')

def index(request):
        context = RequestContext(request)
	
        context_dict = { 'cam': request.session.get('camara'), 'gpsloc': request.session.get('gpslocalizado'), 'gps': request.session.get('gps'), 'ap' : request.session.get('ap') }

        #### NEW CODE ####
        if request.session.get('last_visit'):
                # The session has a value for the last visit
                last_visit_time = request.session.get('last_visit')
                visits = request.session.get('visits', 0)

                if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
                        request.session['visits'] = visits + 1
        else:
                # The get returns None, and the session does not have a value for the last visit.
                request.session['last_visit'] = str(datetime.now())
                request.session['visits'] = 1
        #### END NEW CODE ####
        # Render and return the rendered response back to the user.
        return render_to_response('vs/index.html', context_dict, context)

def about(request):
        # Request the contex.
        context = RequestContext(request)

        # If the visits session varible exists, take it and use it.
        # If it doesn't, we haven't visited the site so set the count to zero.
        if request.session['visits']:
                count = request.session['visits']
        else:
                count = 0

        # Return and render the response, ensuring the count is passed to the template engine.
        return render_to_response('vs/about.html', {'visit_count': count}, context)

@login_required
def register(request):
        # Request the context.
        context = RequestContext(request)

        # Boolean telling us whether registration was successful or not.
        # Initially False; presume it was a failure until proven otherwise!
        registered = False

        # If HTTP POST, we wish to process form data and create an account.
        if request.method == 'POST':
                # Grab raw form data - making use of both FormModels.
                user_form = UserForm(data=request.POST)
                profile_form = UserProfileForm(data=request.POST)

                # Two valid forms?
                if user_form.is_valid() and profile_form.is_valid():
                        # Save the user's form data. That one is easy.
                        user = user_form.save()

                        # Now a user account exists, we hash the password with the set_password() method.
                        # Then we can update the account with .save().
                        user.set_password(user.password)
                        user.save()

                        # Now we can sort out the UserProfile instance.
                        # We'll be setting values for the instance ourselves, so commit=False prevents Django from saving the instance automatically.
                        profile = profile_form.save(commit=False)
                        profile.user = user

                        # Profile picture supplied? If so, we put it in the new UserProfile.
                        if 'picture' in request.FILES:
                                profile.picture = request.FILES['picture']

                        # Now we save the model instance!
                        profile.save()

                        # We can say registration was successful.
                        registered = True

                # Invalid form(s) - just print errors to the terminal.
                else:
                        print user_form.errors, profile_form.errors

        # Not a HTTP POST, so we render the two ModelForms to allow a user to input their data.
        else:
                user_form = UserForm()
                profile_form = UserProfileForm()

        # Render and return!
        return render_to_response(
                'vs/register.html',
                {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
                context)

def user_login(request):
        # Obtain our request's context.
        context = RequestContext(request)

        # If HTTP POST, pull out form data and process it.
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                # Attempt to log the user in with the supplied credentials.
                # A User object is returned if correct - None if not.
                user = authenticate(username=username, password=password)

                # A valid user logged in?
                if user is not None:
                        # Check if the account is active (can be used).
                        # If so, log the user in and redirect them to the homepage.
			request.session['camara'] = '0'
			request.session['gps'] = '0'
			request.session['gpslocalizado'] = '0'
			request.session['ap'] = '0'
                        if user.is_active:
                                login(request, user)
                                return HttpResponseRedirect('/vs/')
                        # The account is inactive; tell by adding variable to the template context.
                        else:
                                return render_to_response('vs/login.html', {'disabled_account': True}, context)
                # Invalid login details supplied!
                else:
                        print "Invalid login details: {0}, {1}".format(username, password)
                        return render_to_response('vs/login.html', {'bad_details': True}, context)

        # Not a HTTP POST - most likely a HTTP GET. In this case, we render the login form for the user.
        else:
                return render_to_response('vs/login.html', {}, context)


# Only allow logged in users to logout - add the @login_required decorator!
@login_required
def user_logout(request):
        # Get the request's context
        context = RequestContext(request)

        # As we can assume the user is logged in, we can just log them out.
        logout(request)

        # Take the user back to the homepage.
        return HttpResponseRedirect('/vs/')

@login_required
def camera(request):
    	#return HttpResponseRedirect('/vs/camera_view/')
	return render_to_response('vs/camera.html')

@login_required
def desactivarcamara(request):
	request.session['camara'] = '0'
	res = commands.getstatusoutput('killall mjpg_streamer')
        print(res)
	
        return HttpResponseRedirect('/vs/')

@login_required
def activarcamara(request):
	request.session['camara'] = '1'
        res = commands.getstatusoutput('sudo LD_LIBRARY_PATH=/usr/src/mjpg-streamer/mjpg-streamer-experimental/ /usr/src/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 640 -y 480 -fps 3 -ex night" -b')
	print(res)
	
        return HttpResponseRedirect('/vs/')




@login_required
def desactivarlocalizacion(request):
	res = commands.getstatusoutput('python /home/userpro/Project/Programas/GPS/desactivargps.py')
        print(res)
	request.session['gps'] = '0'
	request.session['gpslocalizado'] = '0'
        return HttpResponseRedirect('/vs/')

@login_required
def activarlocalizacion(request):
        res = commands.getstatusoutput('python /home/userpro/Project/Programas/GPS/activargps.py')
        print(res)
	request.session['gps'] = '1'
        return HttpResponseRedirect('/vs/')

@login_required
def borrarhistorialub(request):
        res = commands.getstatusoutput('sqlite3 /home/userpro/Project/Django/vs_project/vs.db "delete from vs_pointofinterest"')
        print(res)
        return HttpResponseRedirect('/vs/')


@login_required
def introducirlocalizacion(request):
	if request.session.get('gps') == '0':
		res = commands.getstatusoutput('python /home/userpro/Project/Programas/GPS/activargps.py')
		print(res)
		request.session['gps'] = '1'
	res = commands.getstatusoutput('python /home/userpro/Project/Programas/GPS/estadogps.py')
	#proc = subprocess.Popen("sudo python localizargps.py --alpha=arg1 -b arg2 arg3" ,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	#posactual = proc.communicate()[0]
	print(res)
	if(res[1] == '1'):
		request.session['gpslocalizado'] = '1'
		res = commands.getstatusoutput('python /home/userpro/Project/Programas/GPS/localizargps.py')
		PointOfInterest.objects.get_or_create(name=res[1][20:34], position=res[1][0:19])
		#PointOfInterest.objects.get_or_create(name='20161121193721', position='37.209750,-3.638673')
		print(res)
		lastpoint = PointOfInterest.objects.get(name=res[1][20:34])
		return render(request, 'vs/posicionactual.html', {'lastpoint': lastpoint})
	else:
		request.session['gpslocalizado'] = '0'
		return HttpResponseRedirect('/vs/')

@login_required
def poi_list(request):
    pois = PointOfInterest.objects.all()
    return render(request, 'vs/poi_list.html', {'pois': pois})



@login_required
def desactivarAP(request):
	request.session['ap'] = '0'
	res = commands.getstatusoutput('sudo service hostapd stop')
        print(res)
	res = commands.getstatusoutput('sudo service udhcpd stop')
	print(res)
	res = commands.getstatusoutput('sudo iptables --flush')
        print(res)
        return HttpResponseRedirect('/vs/')

@login_required
def activarAP(request):
	request.session['ap'] = '1'
	res = commands.getstatusoutput('sudo iptables --flush')
        print(res)
	res = commands.getstatusoutput('sudo iptables -t nat -A POSTROUTING -o ppp0 -j MASQUERADE')
        print(res)
        res = commands.getstatusoutput('sudo iptables -A FORWARD -i ppp0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT')
        print(res)
	res = commands.getstatusoutput('sudo iptables -A FORWARD -i wlan0 -o ppp0 -j ACCEPT')
        print(res)
        res = commands.getstatusoutput('sudo service hostapd start')
        print(res)
	res = commands.getstatusoutput('sudo service udhcpd start')
	print(res)
        return HttpResponseRedirect('/vs/')





import os
from django.conf import settings
from django.core.exceptions import PermissionDenied, ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.http import StreamingHttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

try:
    from django.utils.module_loading import import_string as import_module
except ImportError:
    from django.utils.module_loading import import_by_path as import_module

#utils functions
def check_access(request):
    """Returns true if user has access to the directory"""
    access_mode = getattr(settings, 'DIRECTORY_ACCESS_MODE', 'public')
    if access_mode == 'public':
        return True
    elif access_mode == 'use-perms':
        if request.user.is_anonymous():
            return False
        else:
            return request.user.has_perm('directory.read')
    elif access_mode == 'custom':
        check_perm = settings.DIRECTORY_ACCESS_FUNCTION
        if isinstance(check_perm, basestring):
            check_perm = import_module(check_perm)
        elif not hasattr(check_perm, '__call__'):
            raise ImproperlyConfigured('DIRECTORY_ACCESS_FUNCTION must either be a function or python path')
        return check_perm(request)
    else:
        raise ImproperlyConfigured(
            "Invalid setting DIRECTORY_ACCESS_MODE: only values "
            "'public', 'use-perms', and 'custom' are allowed"
        )



def get_file_names(directory):
    """Returns list of file names within directory"""
    contents = os.listdir(directory)
    files = list()
    for item in contents:
        if os.path.isfile(os.path.join(directory, item)):
            files.append(item)
    return files


def read_file_chunkwise(file_obj):
    """Reads file in 32Kb chunks"""
    while True:
        data = file_obj.read(32768)
        if not data:
            break
        yield data

#view functions below
@login_required
def directorio(request):
    return HttpResponseRedirect(reverse('directory_list'))

@login_required
def borrarhistorialint(request):
        res = commands.getstatusoutput('sudo rm -rf /home/userpro/Project/Multimedia/Fotos/*')
        print(res)
	res = commands.getstatusoutput('sudo rm -rf /home/userpro/Project/Multimedia/Videos/*')
        print(res)
        return HttpResponseRedirect('/vs/')

@login_required
def list_directory(request):
    """default view - listing of the directory"""
    if check_access(request):
        directory = settings.DIRECTORY_DIRECTORY
        data = {
            #'directory_name': os.path.basename(directory),
	    'directory_name': 'Intrusiones',
            'directory_files': get_file_names(directory),
	    'directory_dirs': [ name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name)) ],
	    'dire': directory
        }
        template = getattr(settings, 'DIRECTORY_TEMPLATE', 'vs/list.html')
        return render(request, template, data)
        
    else:
        raise PermissionDenied()

@login_required
def list_directories(request, path, directorio):
    """default view - listing of the directory"""
    if check_access(request):
        #directory = settings.DIRECTORY_DIRECTORY
	#directory = path + '/' + directorio
	directory = os.path.join(path, directorio)
        data = {
            'directory_name': os.path.basename(directory),
            'directory_files': get_file_names(directory),
	    #'directory_dirsandfiles': os.listdir(directory),
	    'directory_dirs': [ name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name)) ],
	    'dire': directory
        }
        template = getattr(settings, 'DIRECTORY_TEMPLATE', 'vs/list.html')
        return render(request, template, data)
        
    else:
        raise PermissionDenied()


def download_file(request, path, file_name):
    """allows authorized user to download a given file"""

    if os.path.sep in file_name:
        raise PermissionDenied()

    if check_access(request):
        directory = path

        #make sure that file exists within current directory
        files = get_file_names(directory)
	#files = os.listdir(directory)
        if file_name in files:
            file_path = os.path.join(directory, file_name)
            response = StreamingHttpResponse(content_type='vs/force-download')
            response['Content-Disposition'] = 'attachment; filename=%s' % file_name
            file_obj = open(os.path.join(directory, file_name))
            response.streaming_content = read_file_chunkwise(file_obj)
            return response
        else:
            raise Http404
