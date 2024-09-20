import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()
from django.core.management.base import BaseCommand
from blog_app.models import UsersListRegisters, UsersListPhoto, LikesListPhoto, CommentListPhoto, UsersListTopics, CommentListTopics, NotesChat, UsersChat, Notification, UsersListPhotoGallery
import random
import string


def generate_code(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))



def create_user(name_surname_db, username_db, password_db):
    user = UsersListRegisters(name_surname=name_surname_db, username=username_db, password=password_db)
    user.save()


def add_csrftoken(username_db, csrftoken_db):
    user = UsersListRegisters.objects.get(username=username_db)
    user.csrftoken = csrftoken_db
    user.save()


def take_csrftoken(username_db):
    user = UsersListRegisters.objects.get(username=username_db)
    csrftoken = user.csrftoken
    return csrftoken


def delete_csrftoken_db(username_db):
    user = UsersListRegisters.objects.get(username=username_db)
    user.csrftoken = ''
    user.save()

def info_users(username_db):
    products = UsersListRegisters.objects.get(username=username_db)
    product = products.password
    return product


def info_users_usernames():
    products = UsersListRegisters.objects.all()
    product = products.values_list('username', flat=True)
    return product

def photo_change(username_db):
    user = UsersListRegisters.objects.get(username=username_db)
    user_photo = str(user.photo).split('/')[-1]
    user.photo = user_photo
    user.save()


def infoes_users(username_db):
    products = UsersListRegisters.objects.get(username=username_db)
    product_name = products.name_surname
    product_username = products.username
    product_password = products.password
    product_discription = products.discription
    product_photo = products.photo
    product = [product_name, product_username, product_password, product_discription, product_photo]
    return product


def name_discription_change(username_db, user_name, user_discription):
    user = UsersListRegisters.objects.get(username=username_db)
    user.name_surname = user_name
    user.discription = user_discription
    user.save()


def name_discription_photo_change(username_db, user_name, user_discription, user_photo):
    user = UsersListRegisters.objects.get(username=username_db)
    user.name_surname = user_name
    user.discription = user_discription
    if user_photo:
        user.photo.save(user_photo.name, user_photo, save=True)
    user.save()


def username_password_change(username_db, user_username, user_password):
    user = UsersListRegisters.objects.get(username=username_db)
    user.username = user_username
    user.password = user_password
    user.save()


def photo_change_db2(username_db):
    users = UsersListPhoto.objects.all()
    id_list = users.values_list('id', flat=True)
    for i in range(len(id_list)):
        user = UsersListPhoto.objects.get(id=id_list[i])
        if '/' in str(user.photo): 
            user_photo = str(user.photo).split('/')[-1]
            user.photo = user_photo
            user.save()
        else:
            ...


def create_username_photo(username_db, user_photo):
    users = UsersListPhoto.objects.all()
    id_list = users.values_list('id', flat=True)
    photo_id_new = generate_code(25)
    for i in range(len(id_list)):
        user = UsersListPhoto.objects.get(id=id_list[i])
        print(user.id_photo, photo_id_new)
        if str(user.id_photo) != str(photo_id_new):
            _user = UsersListPhoto(username=username_db, photo=user_photo, id_photo=photo_id_new)
            if user_photo:
                _user.photo.save(user_photo.name, user_photo, save=True)
            _user.save()
            break
        else:
            ...
        

def take_photo(username_db):
    users = UsersListPhoto.objects.all()
    id_list = users.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        user = UsersListPhoto.objects.get(id=id_list[i])
        if str(user.username) == username_db:
            photo_cortege = user.photo
            cortege_list.append(photo_cortege)
        else:
            ...
    return cortege_list


def take_photo_id(username_db, photo):
    users = UsersListPhoto.objects.get(photo=photo)
    if username_db == users.username:
        photo_id = users.id_photo
        return photo_id
    else:
        ...


def take_photo_for_id(username_db, id_photo):
    users = UsersListPhoto.objects.get(id_photo=id_photo)
    if username_db == users.username:
        photo = users.photo
        return photo
    else:
        ...


def take_photo_likes(username_db, id_photo):
    users = UsersListPhoto.objects.get(id_photo=id_photo)
    if username_db == users.username:
        like = users.like
        return like
    else:
        ...

def photo_like_plus(username_db, id_photo):
    users = UsersListPhoto.objects.get(id_photo=id_photo)
    if username_db == users.username:
        users.like = users.like+1
        users.save()
    else:
        ...



def photo_like_minus(username_db, id_photo):
    users = UsersListPhoto.objects.get(id_photo=id_photo)
    if username_db == users.username:
        users.like = users.like-1
        users.save()
    else:
        ...



def create_user_liked(id_photo_db, username_liked_db):
    user = LikesListPhoto(id_photo=id_photo_db, username_liked=username_liked_db)
    user.save()


def delete_user_liked(id_photo_db, username_liked_db):
    if str(take_user_liked(id_photo_db)) != '[]':
        users = LikesListPhoto.objects.all()
        id_list = users.values_list('id', flat=True)
        for i in range(len(id_list)):
            user = LikesListPhoto.objects.get(id=id_list[i])
            if str(user.id_photo) == id_photo_db and str(user.username_liked) == username_liked_db:
                like = LikesListPhoto.objects.get(id=user.id)
                like.delete()
    else:
        ...

def take_user_liked(id_photo_db):
    users = LikesListPhoto.objects.all()
    id_list = users.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        user = LikesListPhoto.objects.get(id=id_list[i])
        if str(user.id_photo) == id_photo_db:
            username_liked = user.username_liked
            cortege_list.append(username_liked)
        else:
            ...
    return cortege_list


def take_user_comment_post(id_photo_db):
    users = CommentListPhoto.objects.all()
    id_list = users.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        user = CommentListPhoto.objects.get(id=id_list[i])
        if str(user.id_photo) == id_photo_db:
            username = user.username_comment
            cortege_list.append(username)
        else:
            ...
    return cortege_list


def delete_post(id_photo_db):
    post = UsersListPhoto.objects.get(id_photo=id_photo_db)
    post.delete()
    if str(take_user_liked(id_photo_db)) != '[]':
        users = LikesListPhoto.objects.all()
        id_list = users.values_list('id', flat=True)
        for i in range(len(id_list)):
            user = LikesListPhoto.objects.get(id=id_list[i])
            if str(user.id_photo) == id_photo_db:
                like = LikesListPhoto.objects.get(id=user.id)
                like.delete()
    else:
        ...
    if str(take_user_comment_post(id_photo_db)) != '[]':
        users = CommentListPhoto.objects.all()
        id_list = users.values_list('id', flat=True)
        for i in range(len(id_list)):
            user = CommentListPhoto.objects.get(id=id_list[i])
            if str(user.id_photo) == id_photo_db:
                comment = CommentListPhoto.objects.get(id=user.id)
                comment.delete()
    else:
        ...



def take_comment_username(id_photo_db):
    comment = CommentListPhoto.objects.all()
    id_list = comment.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        comment_all = CommentListPhoto.objects.get(id=id_list[i])
        if str(comment_all.id_photo) == id_photo_db:
            username_cortege = str(comment_all.username_comment)
            comment_cortege = str(comment_all.comment)
            cortege = f"<b>{username_cortege}</b> {comment_cortege}"
            cortege_list.append(cortege)
        else:
            ...
    return cortege_list



def create_comment(id_photo_db, username_comment_db, comment_db):
    comment = CommentListPhoto(id_photo=id_photo_db, username_comment=username_comment_db, comment=comment_db)
    comment.save()


def delete_comment(id_photo_db, username_comment_db, comment_db):
    comment = CommentListPhoto.objects.all()
    id_list = comment.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        comment_all = CommentListPhoto.objects.get(id=id_list[i])
        if str(comment_all.id_photo) == id_photo_db and str(comment_all.username_comment) == username_comment_db and str(comment_all.comment) == comment_db:
            comment_all.delete()
        else:
            ...

def take_topics_creating(username_db, photo_db):
    users = UsersListTopics.objects.all()
    id_list = users.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        user = UsersListTopics.objects.get(id=id_list[i])
        if str(user.username) == username_db:
            cortege_list.append(user.photo)
        else:
            ...
    if photo_db not in cortege_list:
        return True


def create_username_topics(name_db, discription_db, username_db, photo_db):
    users = UsersListTopics.objects.all()
    id_list = users.values_list('id', flat=True)
    topics_id_new = generate_code(30)
    for i in range(len(id_list)):
        user = UsersListTopics.objects.get(id=id_list[i])
        if str(user.id_topics) != str(topics_id_new):
            if photo_db != name_db:
                _user = UsersListTopics(name=name_db, discription=discription_db, username=username_db, photo=photo_db, id_topics=topics_id_new)
                if photo_db:
                    _user.photo.save(photo_db.name, photo_db, save=True)
                _user.save()
                break
            else:
                if take_topics_creating(username_db, photo_db) == True:
                    _user = UsersListTopics(name=name_db, discription=discription_db, username=username_db, photo=photo_db, id_topics=topics_id_new)
                    _user.save()
                    break
                else:
                    ...
        else:
            ...

def topics_change_db2(username_db):
    users = UsersListTopics.objects.all()
    id_list = users.values_list('id', flat=True)
    for i in range(len(id_list)):
        user = UsersListTopics.objects.get(id=id_list[i])
        if '/' in str(user.photo): 
            user_photo = str(user.photo).split('/')[-1]
            user.photo = user_photo
            user.save()
        else:
            ...



def delete_topics(id_topics_db):
    topics = UsersListTopics.objects.get(id_topics=id_topics_db)
    topics.delete()


def take_topics(username_db):
    users = UsersListTopics.objects.all()
    id_list = users.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        user = UsersListTopics.objects.get(id=id_list[i])
        if str(user.username) == username_db:
            topics_cortege = user.photo
            cortege_list.append(topics_cortege)
        else:
            ...
    return cortege_list



def take_topics_id(username_db, photo_db):
    users = UsersListTopics.objects.all()
    id_list = users.values_list('id', flat=True)
    for i in range(len(id_list)):
        user = UsersListTopics.objects.get(id=id_list[i])
        if str(user.username) == username_db and str(user.photo) == photo_db:
            if '.png' in str(photo_db) or '.jpg' in str(photo_db):
                photo_id = user.id_topics
                return photo_id
            else:
                photo_id = user.id_topics
                return photo_id
        else:
            ...



def take_topics_discroption(username_db, id_topics):
    users = UsersListTopics.objects.get(id_topics=id_topics)
    if username_db == users.username:
        discription = users.discription
        return discription
    else:
        ...


def take_topics_name(username_db, id_topics):
    users = UsersListTopics.objects.get(id_topics=id_topics)
    if username_db == users.username:
        name = users.name
        return name
    else:
        ...



def create_comment_topics(id_topics_db, username_comment_db, comment_db):
    comment = CommentListTopics(id_topics=id_topics_db, username_comment=username_comment_db, comment=comment_db)
    comment.save()


def take_comment_username_topics(id_topics_db):
    comment = CommentListTopics.objects.all()
    id_list = comment.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        comment_all = CommentListTopics.objects.get(id=id_list[i])
        if str(comment_all.id_topics) == id_topics_db:
            username_cortege = str(comment_all.username_comment)
            comment_cortege = str(comment_all.comment)
            cortege = f"<b>{username_cortege}</b> {comment_cortege}"
            cortege_list.append(cortege)
        else:
            ...
    return cortege_list



def delete_comment_topics(id_topics_db, username_comment_db, comment_db):
    comment = CommentListTopics.objects.all()
    id_list = comment.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        comment_all = CommentListTopics.objects.get(id=id_list[i])
        if str(comment_all.id_topics) == id_topics_db and str(comment_all.username_comment) == username_comment_db and str(comment_all.comment) == comment_db:
            comment_all.delete()
        else:
            ...





def take_user_comment_topics(id_topics_db):
    users = CommentListTopics.objects.all()
    id_list = users.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        user = CommentListTopics.objects.get(id=id_list[i])
        if str(user.id_topics) == id_topics_db:
            username = user.username_comment
            cortege_list.append(username)
        else:
            ...
    return cortege_list





def delete_topics(id_topics_db):
    post = UsersListTopics.objects.get(id_topics=id_topics_db)
    post.delete()
    if str(take_user_comment_topics(id_topics_db)) != '[]':
        users = CommentListTopics.objects.all()
        id_list = users.values_list('id', flat=True)
        for i in range(len(id_list)):
            user = CommentListTopics.objects.get(id=id_list[i])
            if str(user.id_topics) == id_topics_db:
                comment = CommentListTopics.objects.get(id=user.id)
                comment.delete()
    else:
        ...
    
    

def take_all_id_photo():
    id_photo = UsersListPhoto.objects.all()
    all_id = id_photo.values_list('id_photo', flat=True)
    id_list = []
    while len(id_list) != 5:  
        id_photo_ = random.choice(all_id)
        if id_photo_ not in id_list:
            id_list.append(id_photo_)
    return id_list


def take_username_for_id_photo(id_photo):
    users = UsersListPhoto.objects.get(id_photo=id_photo)
    username = users.username
    return username


def take_username_for_id_topics(id_topics):
    users = UsersListTopics.objects.get(id_topics=id_topics)
    username = users.username
    return username


def take_name_for_id_topics(id_topics):
    users = UsersListTopics.objects.get(id_topics=id_topics)
    name = users.name
    return name



def take_photo_for_id_topics(username_db, id_topics):
    users = UsersListTopics.objects.get(id_topics=id_topics)
    if username_db == users.username:
        photo = users.photo
        return photo
    else:
        ...


def take_all_id_topics():
    id_photo = UsersListTopics.objects.all()
    all_id = id_photo.values_list('id_topics', flat=True)
    id_list = []
    while len(id_list) != 5:  
        id_topics_ = random.choice(all_id)
        if id_topics_ not in id_list:
            id_list.append(id_topics_)
    return id_list


def take_photo_for_username(username):
    users = UsersListRegisters.objects.get(username=username)
    photo = users.photo
    return photo





def create_notes_chat(notice_user_db, username_db):
    id_chat_db = generate_code(50)
    comment = NotesChat(id_chat=id_chat_db, name_chat="Збережене", notice_user=notice_user_db, username_user=username_db)
    comment.save()


def exists_notes_chat(username_db):
    notes = NotesChat.objects.filter(username_user=username_db).exists()
    return notes
    


def message_chat_notes_change(username_db, message_db):
    message = NotesChat.objects.get(username_user=username_db)
    message.notice_user.append(message_db)
    message.save()


def take_message_chat_notes(username_db):
    message = NotesChat.objects.get(username_user=username_db)
    notes = message.notice_user
    return notes



def message_chat_notes_delete(username_db, message_db):
    message = NotesChat.objects.get(username_user=username_db)
    index = message.notice_user.index(message_db)
    message.notice_user.pop(index)
    message.save()






def create_notes_chat_users(name_chat_user1_db, name_chat_user2_db, photo_chat_user1_db, photo_chat_user2_db, notice_user1_db, notice_user2_db, notice_user_all_db, username1_db, username2_db):
    id_chat_db = generate_code(100)
    comment = UsersChat(id_chat=id_chat_db, name_chat_user1=name_chat_user1_db, name_chat_user2=name_chat_user2_db, \
        photo_chat_user1=photo_chat_user1_db, photo_chat_user2=photo_chat_user2_db, notice_user1=notice_user1_db, notice_user2=notice_user2_db, \
        notice_user_all=notice_user_all_db, username_user1=username1_db, username_user2=username2_db)
    comment.save()


def exists_notes_chat_users(username_db1, username_db2):
    notes = UsersChat.objects.all()
    id_list = notes.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        notes = UsersChat.objects.get(id=id_list[i])
        if notes.username_user1 == username_db1 and notes.username_user2 == username_db2:
            return True 
        elif notes.username_user1 == username_db2 and notes.username_user2 == username_db1:
            return True   
        else:
            return False 



def take_notes_chat_users(username_db1, username_db2):
    notes = UsersChat.objects.all()
    id_list = notes.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        notes = UsersChat.objects.get(id=id_list[i])
        if notes.username_user1 == username_db1 and notes.username_user2 == username_db2:
            id_chat_db = notes.id_chat
            return id_chat_db 
        elif notes.username_user1 == username_db2 and notes.username_user2 == username_db1:
            id_chat_db = notes.id_chat
            return id_chat_db   
        else: 
            ...





def take_all_info_chat_users(username_db):
    notes = UsersChat.objects.all()
    id_list = notes.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        notes = UsersChat.objects.get(id=id_list[i])
        if notes.username_user1 == username_db or notes.username_user2 == username_db:
            if notes.name_chat_user1 != username_db:
                if str(notes.notice_user_all) != '[]':
                    last_message_chat = notes.notice_user_all[-1]
                else:
                    last_message_chat = ''
                cortege = {'id_chat': notes.id_chat, 'name_chat_user': notes.name_chat_user1, 'photo_chat_user': notes.photo_chat_user1, 'notice_user1': notes.notice_user1, 'notice_user2': notes.notice_user2, 'notice_user_all': notes.notice_user_all, 'username_user1': notes.username_user1, 'username_user2': notes.username_user2, 'last_message_chat': last_message_chat}
                cortege_list.append(cortege)
            else:
                if str(notes.notice_user_all) != '[]':
                    last_message_chat = notes.notice_user_all[-1]
                else:
                    last_message_chat = ''
                cortege = {'id_chat': notes.id_chat, 'name_chat_user': notes.name_chat_user2, 'photo_chat_user': notes.photo_chat_user2, 'notice_user1': notes.notice_user1, 'notice_user2': notes.notice_user2, 'notice_user_all': notes.notice_user_all, 'username_user1': notes.username_user1, 'username_user2': notes.username_user2, 'last_message_chat': last_message_chat}
                cortege_list.append(cortege)
        else:
            ...
    return cortege_list





def message_chat_notes_change_users(username_db, id_chat_db, message_db):
    message = UsersChat.objects.get(id_chat=id_chat_db)
    if message.username_user1 == username_db:
        message.notice_user1.append(message_db)
        message.notice_user_all.append(message_db)
        message.save()
    elif message.username_user2 == username_db:
        message.notice_user2.append(message_db)
        message.notice_user_all.append(message_db)
        message.save()
    else:
        ...





def message_chat_notes_delete_users(username_db, id_chat_db, message_db):
    message = UsersChat.objects.get(id_chat=id_chat_db)
    if message.username_user1 == username_db:
        try:
            index = message.notice_user1.index(message_db)
            index_all = message.notice_user_all.index(message_db)
            message.notice_user1.pop(index)
            message.notice_user_all.pop(index_all)
            message.save()
        except:
            ...
    elif message.username_user2 == username_db:
        try:
            index = message.notice_user2.index(message_db)
            index_all = message.notice_user_all.index(message_db)
            message.notice_user2.pop(index)
            message.notice_user_all.pop(index_all)
            message.save()
        except:
            ...
    else:
        ...


def take_message_chat_notes_users(username_db, id_chat_db):
    message = UsersChat.objects.get(id_chat=id_chat_db)
    notes = []
    if message.username_user1 == username_db:
        all_message = message.notice_user_all[:]
        message_user = message.notice_user1
        message_user2 = message.notice_user2
        for msg in all_message:
            if msg in message_user:
                cortege = {'username': message.username_user1, 'photo_user': message.photo_chat_user2, 'message': msg}
                notes.append(cortege)
                message_user.remove(msg)
                message.notice_user_all.remove(msg)
            elif msg in message_user2:
                cortege = {'username': message.username_user2, 'photo_user': message.photo_chat_user1, 'message': msg}
                notes.append(cortege)
                message.notice_user_all.remove(msg)
                message_user2.remove(msg)

    elif message.username_user2 == username_db:
        all_message = message.notice_user_all[:]
        message_user = message.notice_user2
        message_user2 = message.notice_user1
        for msg in all_message:
            if msg in message_user:
                cortege = {'username': message.username_user2, 'photo_user': message.photo_chat_user1, 'message': msg}
                notes.append(cortege)
                message_user.remove(msg)
                message.notice_user_all.remove(msg)
            elif msg in message_user2:
                cortege = {'username': message.username_user1, 'photo_user': message.photo_chat_user2, 'message': msg}
                notes.append(cortege)
                message.notice_user_all.remove(msg)
                message_user2.remove(msg)

    else:
        ...
    return notes




def take_name_chat_notes(username_db, id_chat_db):
    message = UsersChat.objects.get(id_chat=id_chat_db)
    if message.username_user1 == username_db:
        name = message.name_chat_user1
        return name
    elif message.username_user2 == username_db:
        name = message.name_chat_user2
        return name
    else:
        ...


def create_notification(username_db, text_db, owner_db):
    notification = Notification.objects.create(user=username_db, message=text_db, owner=owner_db)
    notification.save()


def take_notification(username_db):
    notification = Notification.objects.all()
    id_list = notification.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        notification = Notification.objects.get(id=id_list[i])
        if notification.is_read == False and notification.owner == username_db:
            cortege = {'username': notification.user, 'message': notification.message, 'time': notification.timestamp}
            cortege_list.append(cortege)
        else:
            ...
    return cortege_list



def take_unread_notification(username_db):
    unread_notification = Notification.objects.filter(owner=username_db, is_read=False).count()
    return unread_notification



def take_message_chat_username_second(username_db, id_chat_db):
    message = UsersChat.objects.get(id_chat=id_chat_db)
    if message.username_user1 == username_db:
        return message.username_user2
    else:
        return message.username_user1



def delete_notifications(username_db):
    notification = Notification.objects.all()
    id_list = notification.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        notification = Notification.objects.get(id=id_list[i])
        if notification.owner == username_db:
            notification.delete()
        else:
            ...


def create_username_photo_gallery(username_db, user_photo):
    users = UsersListPhotoGallery.objects.all()
    id_list = users.values_list('id', flat=True)
    photo_id_new = generate_code(15)
    for i in range(len(id_list)):
        user = UsersListPhotoGallery.objects.get(id=id_list[i])
        if str(user.id_photo) != str(photo_id_new):
            _user = UsersListPhotoGallery(username=username_db, photo=user_photo, id_photo=photo_id_new)
            if user_photo:
                _user.photo.save(user_photo.name, user_photo, save=True)
            _user.save()
            break
        else:
            ...


def photo_change_gallery_db2(username_db):
    users = UsersListPhotoGallery.objects.all()
    id_list = users.values_list('id', flat=True)
    for i in range(len(id_list)):
        user = UsersListPhotoGallery.objects.get(id=id_list[i])
        if '/' in str(user.photo): 
            user_photo = str(user.photo).split('/')[-1]
            user.photo = user_photo
            user.save()
        else:
            ...



def take_topics_gallery_tags(username_db):
    users = UsersListPhotoGallery.objects.all()
    id_list = users.values_list('id', flat=True)
    cortege_list = []
    for i in range(len(id_list)):
        user = UsersListPhotoGallery.objects.get(id=id_list[i])
        if str(user.username) == username_db:
            topics_cortege = {'photo': user.photo, 'tag': user.tag}
            cortege_list.append(topics_cortege)
        else:
            ...
    return cortege_list


def gallery_delete_photo(username_db, photo):
    users = UsersListPhotoGallery.objects.all()
    id_list = users.values_list('id', flat=True)
    for i in range(len(id_list)):
        user = UsersListPhotoGallery.objects.get(id=id_list[i])
        if str(user.username) == username_db and str(user.photo) == photo:
            user.delete()
        else:
            ...



def gallery_tag_photo(username_db, photo, tag_db):
    users = UsersListPhotoGallery.objects.all()
    id_list = users.values_list('id', flat=True)
    for i in range(len(id_list)):
        user = UsersListPhotoGallery.objects.get(id=id_list[i])
        if str(user.username) == username_db and str(user.photo) == photo:
            user.tag = tag_db
            user.save()
        else:
            ...


