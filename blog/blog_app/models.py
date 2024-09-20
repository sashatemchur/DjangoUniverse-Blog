from django.db import models

class UsersListRegisters(models.Model):
    name_surname = models.CharField('Name and Surname', max_length=100)
    username = models.CharField('Username', max_length=100)
    password = models.CharField('Passwords', max_length=50)    
    discription = models.CharField('Discription', max_length=250, blank=True)
    photo = models.ImageField('Photo', upload_to="blog_app/static/blog_app/img/")
    csrftoken = models.CharField('Token', max_length=250, blank=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural= "users"



class UsersListPhoto(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('Username', max_length=100)
    photo = models.ImageField('Users Photo', upload_to="blog_app/static/blog_app/img/")
    id_photo = models.CharField('Id Photo', max_length=100, unique=True)
    like = models.IntegerField('Like', default=0)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "user_photo"
        verbose_name_plural= "user_photos"



class LikesListPhoto(models.Model):
    id = models.AutoField(primary_key=True)
    id_photo = models.CharField('Id Photo', max_length=100)
    username_liked = models.CharField('Username', max_length=100)
    
    def __str__(self):
        return self.id_photo
    
    class Meta:
        verbose_name = "like_photo"
        verbose_name_plural= "like_photos"



class CommentListPhoto(models.Model):
    id = models.AutoField(primary_key=True)
    id_photo = models.CharField('Id Photo', max_length=100)
    username_comment = models.CharField('Username', max_length=100)
    comment = models.CharField('Comment', max_length=250)
    
    def __str__(self):
        return self.id_photo
    
    class Meta:
        verbose_name = "comment_photo"
        verbose_name_plural= "comment_photos"




class UsersListTopics(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name Topics', max_length=100)
    discription = models.CharField('Discription', max_length=10000)
    username = models.CharField('Username', max_length=100)
    photo = models.ImageField('Users Photo', upload_to="blog_app/static/blog_app/img/", blank=True)
    id_topics = models.CharField('Id Topics', max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "user_topic"
        verbose_name_plural= "user_topics"


class CommentListTopics(models.Model):
    id = models.AutoField(primary_key=True)
    id_topics = models.CharField('Id Topic', max_length=100)
    username_comment = models.CharField('Username', max_length=100)
    comment = models.CharField('Comment', max_length=250)
    
    def __str__(self):
        return self.id_photo
    
    class Meta:
        verbose_name = "comment_topic"
        verbose_name_plural= "comment_topics"


        

class UsersChat(models.Model):
    id = models.AutoField(primary_key=True)
    id_chat = models.CharField('Id Chat', max_length=200, unique=True)
    name_chat_user1 = models.CharField('Name Chat User First', max_length=100)
    name_chat_user2 = models.CharField('Name Chat User Second', max_length=100)
    photo_chat_user1 = models.ImageField('Photo User Chat First', upload_to="blog_app/static/blog_app/img/")
    photo_chat_user2 = models.ImageField('Photo User Chat Second', upload_to="blog_app/static/blog_app/img/")
    notice_user1 = models.JSONField('Notice User First', default=list, blank=True)
    notice_user2 = models.JSONField('Notice User Second', default=list, blank=True)    
    notice_user_all = models.JSONField('Notice User All', default=list, blank=True)  
    username_user1 = models.CharField('Username User First', max_length=50)
    username_user2 = models.CharField('Username User Second', max_length=50)

    def __str__(self):
        return self.id_chat
    
    class Meta:
        verbose_name = "chat"
        verbose_name_plural= "chats"


class NotesChat(models.Model):
    id = models.AutoField(primary_key=True)
    id_chat = models.CharField('Id Chat', max_length=200, unique=True)
    name_chat = models.CharField('Name Chat', max_length=100)
    notice_user = models.JSONField('Notice User', default=list, blank=True)
    username_user = models.CharField('Username User', max_length=100, unique=True)

    def __str__(self):
        return self.id_chat
    
    class Meta:
        verbose_name = "notes chat"
        verbose_name_plural= "notes chats"



class Notification(models.Model):
    is_read = models.BooleanField(default=False)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.CharField('Users', max_length=100)
    owner = models.CharField('Owner', max_length=100)

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = "notification"
        verbose_name_plural= "notifications"



class UsersListPhotoGallery(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('Username', max_length=100)
    photo = models.ImageField('Users Photo', upload_to="blog_app/static/blog_app/img/")
    id_photo = models.CharField('Id Photo', max_length=100, unique=True)
    tag = models.CharField('Tag', max_length=100, blank=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "user_photo_gallery"
        verbose_name_plural= "user_photos_gallery"