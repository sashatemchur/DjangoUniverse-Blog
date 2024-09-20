from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from blog_app.models import UsersListRegisters
from blog_app.dborm import create_user, info_users, info_users_usernames, infoes_users, photo_change
from blog_app.dborm import name_discription_change, name_discription_photo_change, username_password_change
from blog_app.dborm import create_username_photo, photo_change_db2, take_photo, take_photo_id, take_photo_for_id, take_photo_likes
from blog_app.dborm import photo_like_plus, photo_like_minus, create_user_liked, add_csrftoken, take_csrftoken, delete_csrftoken_db
from blog_app.dborm import take_user_liked, delete_user_liked, delete_post, take_comment_username, create_comment, delete_comment
from blog_app.dborm import create_username_topics, take_topics, topics_change_db2, take_topics_id, take_topics_creating, take_topics_discroption
from blog_app.dborm import take_topics_name, create_comment_topics, take_comment_username_topics, delete_comment_topics, delete_topics, take_all_id_photo
from blog_app.dborm import take_username_for_id_photo, take_username_for_id_topics, take_name_for_id_topics, take_photo_for_id_topics, take_all_id_topics, take_photo_for_username
from blog_app.dborm import create_notes_chat, exists_notes_chat, message_chat_notes_change, take_message_chat_notes, message_chat_notes_delete
from blog_app.dborm import exists_notes_chat_users, create_notes_chat_users, take_notes_chat_users, take_all_info_chat_users, message_chat_notes_delete_users, message_chat_notes_change_users
from blog_app.dborm import take_message_chat_notes_users, take_name_chat_notes, create_notification, take_unread_notification, take_notification, take_message_chat_username_second, delete_notifications
from blog_app.dborm import create_username_photo_gallery, photo_change_gallery_db2, take_topics_gallery_tags, gallery_delete_photo, gallery_tag_photo
import json, re
import googlemaps
from django.http import JsonResponse



#aH7ds_278dO= MapBox password


def register(request):
    if 'username' not in request.COOKIES:
        return render(request, 'blog_app/register.html')
    else:
        return redirect('/')



def home(request):
    if 'username' in request.COOKIES:
        print(request.GET.get('posts'))
        if request.GET.get('posts') != None:
            posts_data = request.GET.get('posts')
            posts = []
            id_photo_list = []
            
            id_photo_list.append(posts_data[2:27])
            id_photo_list.append(posts_data[31:56])
            id_photo_list.append(posts_data[60:85])
            id_photo_list.append(posts_data[89:114])
            id_photo_list.append(posts_data[118:143])


            for id_photo in id_photo_list:
                username = take_username_for_id_photo(id_photo)
                photo = take_photo_for_id(username, id_photo)
                count_like = take_photo_likes(username, id_photo)
                user_liked = request.COOKIES.get('username') not in take_user_liked(id_photo)
                photo_username = take_photo_for_username(username)
                posts.append({
                    'username': username,
                    'photo': photo,
                    'count_like': count_like,
                    'user_liked': user_liked,
                    'id_photo': id_photo,
                    'photo_username': photo_username,
                })

            context = {
                'username_csrftoken': request.COOKIES.get('username'), 
                'user_profile_photo': str(infoes_users(request.COOKIES.get('username'))[4]), 
                'posts': posts,
                'id_photo_list': id_photo_list,
            }

            print('\n\n\n', posts, '\n\n\n')
            return render(request, 'blog_app/home.html', context)
        else:
            posts = []
            id_photo_list = take_all_id_photo()
            
            for id_photo in id_photo_list:
                username = take_username_for_id_photo(id_photo)
                photo = take_photo_for_id(username, id_photo)
                count_like = take_photo_likes(username, id_photo)
                user_liked = request.COOKIES.get('username') not in take_user_liked(id_photo)
                photo_username = take_photo_for_username(username)
                posts.append({
                    'username': username,
                    'photo': photo,
                    'count_like': count_like,
                    'user_liked': user_liked,
                    'id_photo': id_photo,
                    'photo_username': photo_username,
                })
            
            context = {
                'username_csrftoken': request.COOKIES.get('username'), 
                'user_profile_photo': str(infoes_users(request.COOKIES.get('username'))[4]), 
                'posts': posts,
                'id_photo_list': id_photo_list,
            }
            return render(request, 'blog_app/home.html', context)
    else:
        return redirect('/register/')


def login(request):
    if 'username' not in request.COOKIES:
        print(request.COOKIES)
        print(request.COOKIES.get('csrftoken'))
        return render(request, 'blog_app/login.html')
    else:
        return redirect('/')    

def nlogin(request):
    if 'username' not in request.COOKIES:
        return render(request, 'blog_app/nlogin.html')
    else:
        return redirect('/')


def nnlogin(request):
    if 'username' not in request.COOKIES:
        return render(request, 'blog_app/nnlogin.html')
    else:
        return redirect('/')



def post_photo(request, text=None, id_photo=None):
    if 'username' in request.COOKIES:
        if request.COOKIES.get('username') not in take_user_liked(id_photo):
            true_false =  True
        else:
            true_false = False
        if str(take_csrftoken(text))==str(request.COOKIES.get('csrftoken')):
            if request.GET != '':
                if request.GET.get('data') != None:
                    true_false_delete = request.GET.get('data')
                    username = request.GET.get('data2')
                    comment = request.GET.get('data3')
                    print(true_false_delete)
                    if str(true_false_delete) == 'True':
                        print("sdlhjlkds;kbsndjsndljsdlsnj")
                        product_name = {'username': infoes_users(text)[1], 'this_photo': take_photo_for_id(text, id_photo), \
                            'count_like': take_photo_likes(text, id_photo), 'id_photo': id_photo, 'true_false': true_false, \
                            'comment': take_comment_username(id_photo), 'true_false_delete': True, 'comment_delete': username+' '+comment}
                        return render(request, 'blog_app/photo.html', product_name)
                    else:
                        product_name = {'username': infoes_users(text)[1], 'this_photo': take_photo_for_id(text, id_photo), \
                            'count_like': take_photo_likes(text, id_photo), 'id_photo': id_photo, 'true_false': true_false, \
                            'comment': take_comment_username(id_photo), 'true_false_delete': False, 'comment_delete': username+' '+comment}
                        return render(request, 'blog_app/photo.html', product_name)
                else:
                    product_name = {'username': infoes_users(text)[1], 'this_photo': take_photo_for_id(text, id_photo), \
                        'count_like': take_photo_likes(text, id_photo), 'id_photo': id_photo, 'true_false': true_false, \
                        'comment': take_comment_username(id_photo), 'true_false_delete': None}
                    return render(request, 'blog_app/photo.html', product_name)                    
            else:
                ...
        else:
            print(request.GET)
            if request.GET != '':
                if request.GET.get('data') != None:
                    true_false_delete = request.GET.get('data')
                    username = request.GET.get('data2')
                    comment = request.GET.get('data3')
                    print(true_false_delete)
                    if str(true_false_delete) == 'True':
                        print("sdlhjlkds;kbsndjsndljsdlsnj")
                        product_name = {'username': infoes_users(text)[1], 'this_photo': take_photo_for_id(text, id_photo), \
                            'count_like': take_photo_likes(text, id_photo), 'id_photo': id_photo, 'true_false': true_false, \
                            'comment': take_comment_username(id_photo), 'true_false_delete': True, 'comment_delete': username+' '+comment}
                        return render(request, 'blog_app/photos.html', product_name)
                    else:
                        product_name = {'username': infoes_users(text)[1], 'this_photo': take_photo_for_id(text, id_photo), \
                            'count_like': take_photo_likes(text, id_photo), 'id_photo': id_photo, 'true_false': true_false, \
                            'comment': take_comment_username(id_photo), 'true_false_delete': False, 'comment_delete': username+' '+comment}
                        return render(request, 'blog_app/photos.html', product_name)
                else:
                    product_name = {'username': infoes_users(text)[1], 'this_photo': take_photo_for_id(text, id_photo), \
                        'count_like': take_photo_likes(text, id_photo), 'id_photo': id_photo, 'true_false': true_false, \
                        'comment': take_comment_username(id_photo), 'true_false_delete': None}
                    return render(request, 'blog_app/photos.html', product_name)                    
            else:
                ...
    else:
        return redirect('/register/')


@csrf_exempt 
def login_(request):
    if 'username' not in request.COOKIES:
        try:
            password = info_users(request.POST['username'])
            if request.method == 'POST' and str(request.POST['password']) == str(password):
                user_username = request.POST['username']
                add_csrftoken(user_username, request.COOKIES.get('csrftoken'))
                response = redirect(f'/{user_username}/')
                response.set_cookie('username', f'{user_username}')
                return response
            else:
                return redirect('/nnlogin/')
        except:
            return redirect('/nlogin/')
    else:
        return redirect('/')

def pregister(request):
    if 'username' not in request.COOKIES:
        return render(request, 'blog_app/pregister.html')
    else:
        return redirect('/')

def uregister(request):
    if 'username' not in request.COOKIES:
        return render(request, 'blog_app/uregister.html')
    else:
        return redirect('/')
    
@csrf_exempt
def register_(request):
    if 'username' not in request.COOKIES:
        users = UsersListRegisters.objects.all()
        usernames = users.values_list('username', flat=True)
        status1 = False
        status2 = False
        if request.method == 'POST' and request.POST['username'] not in usernames:
            status2 = True
            if status1 == True:
                create_user(request.POST['name_surname'], request.POST['username'], request.POST['password'])
                return HttpResponse(status=200)
            else:
                ...
        else:
            return redirect('/uregister/')
        if request.method == 'POST' and request.POST['password'] == request.POST['repeat_password'] and len(request.POST['password']) >= 8:
            status1 = True
            if status2 == True:
                create_user(request.POST['name_surname'], request.POST['username'], request.POST['password'])
                return HttpResponse(status=200)
            else:
                ...
        else:
            return redirect('/pregister/')
    else:
        return redirect('/')

def username(request, text=None):
    if 'username' in request.COOKIES:
        if text in info_users_usernames():
            if str(take_csrftoken(text))==str(request.COOKIES.get('csrftoken')):
                unread_notifications = take_unread_notification(text)
                photo_change(text)
                product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], \
                    'photo': '../../static/blog_app/img/'+str(infoes_users(text)[4]), 'photo_profile': take_photo(text), 'unread_notifications': unread_notifications}
                return render(request, 'blog_app/user.html', product_name)
            else:
                photo_change(text)
                product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], \
                    'photo': '../../static/blog_app/img/'+str(infoes_users(text)[4]), 'photo_profile': take_photo(text)}
                return render(request, 'blog_app/users.html', product_name)
        else:
            return redirect('/')
    else:
        return redirect('/register/')

def edit_profile(request, text=None):
    if 'username' in request.COOKIES:
        url = str(request)
        index = url[33:].index('/')
        username_url = url[33:][:index]
        if request.COOKIES.get('username')==username_url:
            if text in info_users_usernames():
                photo_change(text)
                product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], 'photo': '../../static/blog_app/img/'+str(infoes_users(text)[4])}
                return render(request, 'blog_app/edit_profile.html', product_name)
            else:
                return render(request, 'blog_app/home.html')
        else:
            return redirect('/')
    else:
        return redirect('/register/')

@csrf_exempt
def edit_profile_(request, text=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST':
            if text in info_users_usernames():
                try:
                    if request.FILES['photo'] == '':
                        ...
                except:
                    request.FILES['photo'] = infoes_users(text)[4]
                    photo_change(text)
                    name_discription_change(text, request.POST['names'], request.POST['discription'])
                    return redirect(f"/{text}/")
                else:
                    photo_change(text)
                    name_discription_photo_change(text, request.POST['names'], request.POST['discription'], request.FILES['photo'])
                    return redirect(f"/{text}/")
            else:
                return render(request, 'blog_app/home.html')
        else:
            return redirect(f'/edit-profile/{infoes_users(text)[1]}')
    else:
        return redirect('/register/')


@csrf_exempt
def _edit_profile_(request, text=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames():
            if request.POST['password'] == infoes_users(text)[2]:
                list_users = list(info_users_usernames())
                index_list_users = list(info_users_usernames()).index(text)
                list_users.pop(index_list_users)
                if request.POST['username'] not in list_users:
                    if request.POST['new_password'] == request.POST['repeat_new_password'] and len(request.POST['new_password']) >= 8:
                        photo_change(text)
                        username_password_change(text, request.POST['username'], request.POST['new_password'])
                        return redirect(f"/{request.POST['username']}/")
                    else:
                        product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], 'photo': '../../static/blog_app/img/'+str(infoes_users(text)[4])}
                        return render(request, 'blog_app/pedit_profile.html', product_name)
                else:
                    product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], 'photo': '../../static/blog_app/img/'+str(infoes_users(text)[4])}
                    return render(request, 'blog_app/uedit_profile.html', product_name)

            elif request.POST['username'] == text and request.POST['password'] == '' and request.POST['new_password'] == '' and request.POST['repeat_new_password'] == '':
                return redirect(f"/{text}/")

            elif request.POST['password'] == '' and request.POST['new_password'] == '' and request.POST['repeat_new_password'] == '':
                if request.POST['username'] not in info_users_usernames():
                    photo_change(text)
                    username_password_change(text, request.POST['username'], infoes_users(text)[2])
                    return redirect(f"/{request.POST['username']}/")
                else:
                    product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], 'photo': '../../static/blog_app/img/'+str(infoes_users(text)[4])}
                    return render(request, 'blog_app/uedit_profile.html', product_name)


            else:
                product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], 'photo': '../../static/blog_app/img/'+str(infoes_users(text)[4])}
                return render(request, 'blog_app/opedit_profile.html', product_name)
        else:
            return redirect(f'/edit-profile/{infoes_users(text)[1]}')
    else:
        return redirect('/register/')


@csrf_exempt
def post(request, text=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames():
            create_username_photo(text, request.FILES.get('photo'))
            photo_change_db2(text)
            return redirect(f"/{text}/")
        else:
            return redirect(f"/{text}/")
    else:
        return redirect('/register/')

@csrf_exempt
def posts(request, text=None, id_photo=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames():
            delete_post(id_photo)
            return redirect(f"/{text}/")
        else:
            return redirect(f"/{text}/")
    else:
        return redirect('/register/')

@csrf_exempt
def post_apply(request, text=None, photo=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames() and photo in take_photo(text):
            id_photo = take_photo_id(text, photo)
            return redirect(f"/{text}/post/{id_photo}")
        else:
            redirect(f"/{text}/")
    else:
        return redirect('/register/')

@csrf_exempt
def post_photo_likes(request, text=None, id_photo=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames() and request.COOKIES.get('username') in info_users_usernames():
            if request.COOKIES.get('username') not in take_user_liked(id_photo):
                photo_like_plus(text, id_photo)
                create_user_liked(id_photo, request.COOKIES.get('username'))
                return redirect(f"/{text}/post/{id_photo}")
            else:
                photo_like_minus(text, id_photo)
                delete_user_liked(id_photo, request.COOKIES.get('username'))
                return redirect(f"/{text}/post/{id_photo}")
        else:
            return redirect(f"/{text}/post/{id_photo}")
    else:
        return redirect('/register/')

@csrf_exempt
def post_photo_comment(request, text=None, id_photo=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames() and request.COOKIES.get('username') in info_users_usernames():
            create_comment(id_photo, request.COOKIES.get('username'), request.POST['comment'])
            return redirect(f"/{text}/post/{id_photo}")
        else:
            return redirect(f"/{text}/post/{id_photo}")
    else:
        return redirect('/register/')

@csrf_exempt
def delete_csrftoken(request, text=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames():
            delete_csrftoken_db(text)
            response = redirect("/")
            response.delete_cookie('username')
            return response
        else:
            return redirect("/")
    else:
        return redirect('/register/')

@csrf_exempt
def post_photo_comment_delete_true_false(request, text=None, id_photo=None):
    if 'username' in request.COOKIES:
        print(request.COOKIES.get('username'), text)
        full_comment = request.POST['comment']
        username = full_comment[:full_comment.index(' ')]
        comment = full_comment[full_comment.index(' ')+1:]
        new_username = str(username).replace("<b>", '').replace("</b>", '')
        print(new_username)
        if request.method == 'POST' and text in info_users_usernames() and request.COOKIES.get('username') in info_users_usernames():
            print("s;kdlskdj")
            if new_username == request.COOKIES.get('username') or text == request.COOKIES.get('username'):
                true_false_delete = True
            else:
                true_false_delete = False
            print(true_false_delete)
            return redirect(f"/{text}/post/{id_photo}?data={true_false_delete}&data2={new_username}&data3={comment}")

        else:
            return redirect(f"/{text}/post/{id_photo}")

    else:
        return redirect('/register/')


@csrf_exempt
def post_photo_comment_delete(request, text=None, id_photo=None):
    if 'username' in request.COOKIES:
        print(request.COOKIES.get('username'), text)
        print(request.POST['comment'])
        full_comment = request.POST['comment']
        print(full_comment)
        index = full_comment.index(' ')
        username = full_comment[:index]
        new_username = str(username).replace("<b>", '').replace("</b>", '')
        print(new_username, 'jkjjkjlj')

        if request.method == 'POST' and text in info_users_usernames() and request.COOKIES.get('username') in info_users_usernames() and text == request.COOKIES.get('username'):
            full_comment = request.POST['comment']
            index = full_comment.index(' ')
            username = full_comment[:index]
            comment = full_comment[index+1:]
            new_username = str(username).replace("<b>", '').replace("</b>", '')
            print(comment)
            delete_comment(id_photo, new_username, comment)
            return redirect(f"/{text}/post/{id_photo}")

        elif request.method == 'POST' and text in info_users_usernames() and request.COOKIES.get('username') in info_users_usernames() and new_username == request.COOKIES.get('username'):
            full_comment = request.POST['comment']
            index = full_comment.index(' ')
            username = full_comment[:index]
            comment = full_comment[index+1:]
            new_username = str(username).replace("<b>", '').replace("</b>", '')
            delete_comment(id_photo, new_username, comment)
            return redirect(f"/{text}/post/{id_photo}")

        else:
            return redirect(f"/{text}/post/{id_photo}")

    else:
        return redirect('/register/')


def topics(request, text=None):
    if 'username' in request.COOKIES:
        if text in info_users_usernames():
            if str(take_csrftoken(text))==str(request.COOKIES.get('csrftoken')):
                photo_change(text)
                product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], \
                    'user_profile_photo': '../../static/blog_app/img/'+str(infoes_users(text)[4]), 'photo_profile': take_topics(text), 'username_csrftoken': request.COOKIES.get('username')}     
                return render(request, 'blog_app/topic.html', product_name)
            else:
                photo_change(text)
                product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], \
                    'user_profile_photo': '../../static/blog_app/img/'+str(infoes_users(request.COOKIES.get('username'))[4]), 'photo_profile': take_topics(text), 'username_csrftoken': request.COOKIES.get('username')}  
                return render(request, 'blog_app/topics.html', product_name)
        else:
            return render(request, 'blog_app/home.html')
    else:
        return redirect('/register/')


def topic(request):
    if 'username' in request.COOKIES:
        if request.GET.get('topics') != None:
            topics_data = request.GET.get('topics')
            topics = []
            id_topics_list = []
            
            id_topics_list.append(topics_data[2:27])
            id_topics_list.append(topics_data[31:56])
            id_topics_list.append(topics_data[60:85])
            id_topics_list.append(topics_data[89:114])
            id_topics_list.append(topics_data[118:143])


            for id_topics in id_topics_list:
                username = take_username_for_id_topics(id_topics)
                name = take_name_for_id_topics(id_topics)
                photo = take_photo_for_id_topics(username, id_topics)
                photo_username = take_photo_for_username(username)
                topics.append({
                    'username': username,
                    'name': name,
                    'photo': photo,
                    'id_topics': id_topics,
                    'photo_username': photo_username,
                })

            context = {
                'username_csrftoken': request.COOKIES.get('username'), 
                'user_profile_photo': str(infoes_users(request.COOKIES.get('username'))[4]), 
                'topics': topics,
                'id_topics_list': id_topics_list,
            }

            return render(request, 'blog_app/all_topics.html', context)

        else:
            topics = []
            id_topics_list = take_all_id_topics()
            
            for id_topics in id_topics_list:
                username = take_username_for_id_topics(id_topics)
                name = take_name_for_id_topics(id_topics)
                photo = take_photo_for_id_topics(username, id_topics)
                photo_username = take_photo_for_username(username)
                topics.append({
                    'username': username,
                    'name': name,
                    'photo': photo,
                    'id_topics': id_topics,
                    'photo_username': photo_username,
                })
            
            context = {
                'username_csrftoken': request.COOKIES.get('username'), 
                'user_profile_photo': str(infoes_users(request.COOKIES.get('username'))[4]), 
                'topics': topics,
                'id_topics_list': id_topics_list,
            }
            return render(request, 'blog_app/all_topics.html', context)
    else:
        return redirect('/register/')



def topics_create(request, text=None):
    if 'username' in request.COOKIES:
        if str(take_csrftoken(text))==str(request.COOKIES.get('csrftoken')):
            photo_change(text)
            product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], \
                'user_profile_photo': '../../static/blog_app/img/'+str(infoes_users(text)[4]), 'photo_profile': take_photo(text), 'username_csrftoken': request.COOKIES.get('username')}     
            return render(request, 'blog_app/topics_discription.html', product_name)
        else:
            return render(request, 'blog_app/home.html')
    else:
        return redirect('/register/')



@csrf_exempt
def topics_created(request, text=None):
    if 'username' in request.COOKIES:
        if str(take_csrftoken(text))==str(request.COOKIES.get('csrftoken')):
            if request.FILES:
                print('\n\n\n\n\n')
                create_username_topics(request.POST['name'], request.POST['discription'], text, request.FILES['photo'])
                topics_change_db2(text)
                return redirect(f'/topics/{text}')
            else:
                if take_topics_creating(text, request.POST['name']) == True:
                    print("djk;slkdj;sdjk123iu12iuiewuqi")
                    create_username_topics(request.POST['name'], request.POST['discription'], text, request.POST['name'])
                    return redirect(f'/topics/{text}')
                else:
                    print("djk;slkdj;sdjk")
                    photo_change(text)
                    product_name = {'name': infoes_users(text)[0], 'username': infoes_users(text)[1], 'discription': infoes_users(text)[3], \
                        'user_profile_photo': '../../static/blog_app/img/'+str(infoes_users(text)[4]), 'photo_profile': take_photo(text), 'username_csrftoken': request.COOKIES.get('username'), 'error': "Це ім'я теми зайнято"}     
                    return render(request, 'blog_app/topics_discription.html', product_name) 
        else:
            return render(request, 'blog_app/home.html')
    else:
        return redirect('/register/')


@csrf_exempt
def topics_apply(request, text=None, topics=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames(): # photo in take_photo(text) замінить 
            id_topics = take_topics_id(text, topics)
            return redirect(f"/{text}/topic/{id_topics}")
        else:
            return render(request, 'blog_app/home.html')
    else:
        return redirect('/register/')



def topics_post(request, text=None, id_topics=None):
    if 'username' in request.COOKIES:
        if str(take_csrftoken(text))==str(request.COOKIES.get('csrftoken')):
            if request.GET != '':
                if request.GET.get('data') != None:
                    true_false_delete = request.GET.get('data')
                    username = request.GET.get('data2')
                    comment = request.GET.get('data3')
                    if str(true_false_delete) == 'True':
                        product_name = {'name': take_topics_name(text, id_topics), 'username': infoes_users(text)[1], 'discription': take_topics_discroption(text, id_topics), \
                            'username_csrftoken': request.COOKIES.get('username'), 'id_topics': id_topics, \
                            'comment': take_comment_username_topics(id_topics), 'true_false_delete': True, 'comment_delete': username+' '+comment} 
                        return render(request, 'blog_app/topics_post.html', product_name)   
                    else:
                        product_name = {'name': take_topics_name(text, id_topics), 'username': infoes_users(text)[1], 'discription': take_topics_discroption(text, id_topics), \
                            'username_csrftoken': request.COOKIES.get('username'), 'id_topics': id_topics, \
                            'comment': take_comment_username_topics(id_topics), 'true_false_delete': False, 'comment_delete': username+' '+comment} 
                        return render(request, 'blog_app/topics_post.html', product_name)   
                else:
                    product_name = {'name': take_topics_name(text, id_topics), 'username': infoes_users(text)[1], 'discription': take_topics_discroption(text, id_topics), \
                        'username_csrftoken': request.COOKIES.get('username'), 'id_topics': id_topics, \
                        'comment': take_comment_username_topics(id_topics), 'true_false_delete': None} 
                    return render(request, 'blog_app/topics_post.html', product_name)   
            else:
                ...
        else:
            if request.GET != '':
                if request.GET.get('data') != None:
                    true_false_delete = request.GET.get('data')
                    username = request.GET.get('data2')
                    comment = request.GET.get('data3')
                    if str(true_false_delete) == 'True':
                        product_name = {'name': take_topics_name(text, id_topics), 'username': infoes_users(text)[1], 'discription': take_topics_discroption(text, id_topics), \
                            'username_csrftoken': request.COOKIES.get('username'), 'id_topics': id_topics, \
                            'comment': take_comment_username_topics(id_topics), 'true_false_delete': True, 'comment_delete': username+' '+comment} 
                        return render(request, 'blog_app/topics_posts.html', product_name)   
                    else:
                        product_name = {'name': take_topics_name(text, id_topics), 'username': infoes_users(text)[1], 'discription': take_topics_discroption(text, id_topics), \
                            'username_csrftoken': request.COOKIES.get('username'), 'id_topics': id_topics, \
                            'comment': take_comment_username_topics(id_topics), 'true_false_delete': False, 'comment_delete': username+' '+comment} 
                        return render(request, 'blog_app/topics_posts.html', product_name) 
                else:
                    product_name = {'name': take_topics_name(text, id_topics), 'username': infoes_users(text)[1], 'discription': take_topics_discroption(text, id_topics), \
                        'username_csrftoken': request.COOKIES.get('username'), 'id_topics': id_topics, \
                        'comment': take_comment_username_topics(id_topics), 'true_false_delete': None} 
                    return render(request, 'blog_app/topics_posts.html', product_name)                   
            else:
                ...
    else:
        return redirect('/register/')



@csrf_exempt
def topics_comment(request, text=None, id_topics=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames() and request.COOKIES.get('username') in info_users_usernames():
            create_comment_topics(id_topics, request.COOKIES.get('username'), request.POST['comment'])
            return redirect(f"/{text}/topic/{id_topics}")
        else:
            return redirect(f"/{text}/topic/{id_topics}")
    else:
        return redirect('/register/')



@csrf_exempt
def topics_photo_comment_delete_true_false(request, text=None, id_topics=None):
    if 'username' in request.COOKIES:
        print(request.COOKIES.get('username'), text)
        full_comment = request.POST['comment']
        username = full_comment[:full_comment.index(' ')]
        comment = full_comment[full_comment.index(' ')+1:]
        new_username = str(username).replace("<b>", '').replace("</b>", '')
        print(new_username)
        if request.method == 'POST' and text in info_users_usernames() and request.COOKIES.get('username') in info_users_usernames():
            print("s;kdlskdj")
            if new_username == request.COOKIES.get('username') or text == request.COOKIES.get('username'):
                true_false_delete = True
            else:
                true_false_delete = False
            print(true_false_delete)
            return redirect(f"/{text}/topic/{id_topics}?data={true_false_delete}&data2={new_username}&data3={comment}")

        else:
            return redirect(f"/{text}/topic/{id_topics}")

    else:
        return redirect('/register/')



@csrf_exempt
def topics_photo_comment_delete(request, text=None, id_topics=None):
    if 'username' in request.COOKIES:
        print(request.COOKIES.get('username'), text)
        print(request.POST['comment'])
        full_comment = request.POST['comment']
        print(full_comment)
        index = full_comment.index(' ')
        username = full_comment[:index]
        new_username = str(username).replace("<b>", '').replace("</b>", '')
        print(new_username, 'jkjjkjlj')

        if request.method == 'POST' and text in info_users_usernames() and request.COOKIES.get('username') in info_users_usernames() and text == request.COOKIES.get('username'):
            full_comment = request.POST['comment']
            index = full_comment.index(' ')
            username = full_comment[:index]
            comment = full_comment[index+1:]
            new_username = str(username).replace("<b>", '').replace("</b>", '')
            print(comment)
            delete_comment_topics(id_topics, new_username, comment)
            return redirect(f"/{text}/topic/{id_topics}")

        elif request.method == 'POST' and text in info_users_usernames() and request.COOKIES.get('username') in info_users_usernames() and new_username == request.COOKIES.get('username'):
            full_comment = request.POST['comment']
            index = full_comment.index(' ')
            username = full_comment[:index]
            comment = full_comment[index+1:]
            new_username = str(username).replace("<b>", '').replace("</b>", '')
            delete_comment_topics(id_topics, new_username, comment)
            return redirect(f"/{text}/topic/{id_topics}")

        else:
            return redirect(f"/{text}/topic/{id_topics}")

    else:
        return redirect('/register/')


@csrf_exempt
def topics_delete(request, text=None, id_topics=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames():
            delete_topics(id_topics)
            return redirect(f"/topics/{text}/")
        else:
            return redirect(f"/topics/{text}/")
    else:
        return redirect('/register/')


@csrf_exempt
def post_photo_likes_home(request, text=None, id_photo=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames() and request.COOKIES.get('username') in info_users_usernames():
            if request.COOKIES.get('username') not in take_user_liked(id_photo):
                photo_like_plus(text, id_photo)
                create_user_liked(id_photo, request.COOKIES.get('username'))
                return redirect(f"/?posts={request.POST['posts']}")
            else:
                photo_like_minus(text, id_photo)
                delete_user_liked(id_photo, request.COOKIES.get('username'))
                return redirect(f"/?posts={request.POST['posts']}")
        else:
            return redirect("/")
    else:
        return redirect('/register/')



def chats_user(request, text=None):
    if 'username' in request.COOKIES:
        if exists_notes_chat(text) == False:
            create_notes_chat([], text)
        else:
            ...
        
        messages = take_message_chat_notes(request.COOKIES.get('username'))
        if str(messages) != '[]':
            last_message = messages[-1]
        else:
            last_message = ''
        last_message_chat = 's'
        product_name = {'username': text, 'messages': messages, 'last_message': last_message, 'users_messages': take_all_info_chat_users(text), 'last_message_chat': last_message_chat}
        return render(request, 'blog_app/chats_user.html', product_name)   
    else:
        return redirect('/register/')

@csrf_exempt
def message_change(request, text=None):
    if 'username' in request.COOKIES:
        notes = request.POST['notes']
        message_chat_notes_change(request.COOKIES.get('username'), notes)
        return redirect(f'/chats/{text}/')
    else:
        return redirect('/register/')



@csrf_exempt
def message_delete(request, text=None):
    if 'username' in request.COOKIES:
        message = request.POST['message']
        message_chat_notes_delete(request.COOKIES.get('username'), message)
        return redirect(f'/chats/{text}/')
    else:
        return redirect('/register/')


@csrf_exempt
def chats_users_check(request, text=None):
    if 'username' in request.COOKIES:
        if exists_notes_chat_users(text, request.COOKIES.get('username')) == True:
            id_chat = take_notes_chat_users(text, request.COOKIES.get('username'))
            username = request.COOKIES.get('username')
            return redirect(f'/chats/{username}/{id_chat}')
        else:
            photo_chat_user1 = str(infoes_users(request.COOKIES.get('username'))[4])
            photo_chat_user2 = str(infoes_users(text)[4])
            create_notes_chat_users(request.COOKIES.get('username'), text, photo_chat_user1, photo_chat_user2, [], [], [], text, request.COOKIES.get('username'))
            id_chat = take_notes_chat_users(text, request.COOKIES.get('username'))
            username = request.COOKIES.get('username')
            return redirect(f'/chats/{username}/{id_chat}')
    else:
        return redirect('/register/')



def chats_users(request, text=None, id_chat=None):
    if 'username' in request.COOKIES:
        if request.GET.get('data') != None:
            posts_data = request.GET.get('data')
            if str(posts_data) == 'True':
                messages = take_message_chat_notes(text)
                if str(messages) != '[]':
                    last_message_notes = messages[-1]
                else:
                    last_message_notes = ''
                product_name = {'username': text, 'id_chat': id_chat, 'last_message_notes': last_message_notes, \
                    'users_messages': take_all_info_chat_users(text), 'messages': take_message_chat_notes_users(text, id_chat), 'name_chat_for_id_chat': take_name_chat_notes(text, id_chat), \
                    'mapbox_token': 'pk.eyJ1Ijoic2FzaGF0ZW1jaHVyIiwiYSI6ImNtMTEzbWFyejBrd3oybHNnczFiYzFwcngifQ.KQA26hgWeVb_8aNXO2XtRQ', 'true_false_map': True}
                return render(request, 'blog_app/chats_users.html', product_name)
            else:
                ...
        else: 
            messages = take_message_chat_notes(text)
            if str(messages) != '[]':
                last_message_notes = messages[-1]
            else:
                last_message_notes = ''
            product_name = {'username': text, 'id_chat': id_chat, 'last_message_notes': last_message_notes, \
                'users_messages': take_all_info_chat_users(text), 'messages': take_message_chat_notes_users(text, id_chat), 'name_chat_for_id_chat': take_name_chat_notes(text, id_chat), \
                'mapbox_token': 'pk.eyJ1Ijoic2FzaGF0ZW1jaHVyIiwiYSI6ImNtMTEzbWFyejBrd3oybHNnczFiYzFwcngifQ.KQA26hgWeVb_8aNXO2XtRQ'}
            return render(request, 'blog_app/chats_users.html', product_name)
    else:
        return redirect('/register/')




@csrf_exempt
def message_change_users(request, text=None, id_chat=None):
    if 'username' in request.COOKIES:
        username_second = take_message_chat_username_second(text, id_chat)
        notes = request.POST['notes']
        message_chat_notes_change_users(text, id_chat, notes)
        create_notification(text, notes, username_second)
        return redirect(f'/chats/{text}/{id_chat}')
    else:
        return redirect('/register/')



@csrf_exempt
def message_delete_users(request, text=None, id_chat=None):
    if 'username' in request.COOKIES:
        message = request.POST['message']
        message_chat_notes_delete_users(text, id_chat, message)
        return redirect(f'/chats/{text}/{id_chat}')
    else:
        return redirect('/register/')


@csrf_exempt
def notification(request, text=None):
    if 'username' in request.COOKIES:
        product_name = {'username': text, 'notifications': take_notification(text)}
        return render(request, 'blog_app/notification.html', product_name)
    else:
        return redirect('/register/')



@csrf_exempt
def delete_notification(request, text=None):
    if 'username' in request.COOKIES:
        delete_notifications(text)
        return redirect(f'/{text}/notification')
    else:
        return redirect('/register/')

@csrf_exempt
def gallery(request, text=None):
    if 'username' in request.COOKIES:
        product_name = {'username': text, "photo_profile_tags": take_topics_gallery_tags(text)}
        return render(request, 'blog_app/gallery.html', product_name)
    else:
        return redirect('/register/')


@csrf_exempt
def post_gallery(request, text=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames():
            create_username_photo_gallery(text, request.FILES.get('photo'))
            photo_change_gallery_db2(text)
            return redirect(f"/{text}/gallery/")
        else:
            return redirect(f"/{text}/")
    else:
        return redirect('/register/')



@csrf_exempt
def gallery_delete(request, text=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames():
            photo = request.POST['photo']
            gallery_delete_photo(text, photo)
            return redirect(f"/{text}/gallery/")
        else:
            return redirect(f"/{text}/")
    else:
        return redirect('/register/')



@csrf_exempt
def gallery_tag(request, text=None):
    if 'username' in request.COOKIES:
        if request.method == 'POST' and text in info_users_usernames():
            photo = request.POST['photo']
            gallery_tag_photo(text, photo, request.POST['tag'])
            return redirect(f"/{text}/gallery/")
        else:
            return redirect(f"/{text}/")
    else:
        return redirect('/register/')


def chats_users_map(request, text=None, id_chat=None):
    if 'username' in request.COOKIES:
        true_false_map = True
        return redirect(f'/chats/{text}/{id_chat}?data={true_false_map}')
    else:
        return redirect('/register/')

