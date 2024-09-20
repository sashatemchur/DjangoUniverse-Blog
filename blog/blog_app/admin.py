from django.contrib import admin
from .models import UsersListRegisters, UsersListPhoto, LikesListPhoto
from .models import CommentListPhoto, UsersListTopics, CommentListTopics
from .models import UsersChat, NotesChat, Notification, UsersListPhotoGallery


class UsersListRegistersAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'username', 'password', 'discription', 'photo', 'csrftoken')


admin.site.register(UsersListRegisters, UsersListRegistersAdmin)


class UsersListPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'photo', 'id_photo', 'like')


admin.site.register(UsersListPhoto, UsersListPhotoAdmin)


class LikesListPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_photo', 'username_liked')


admin.site.register(LikesListPhoto, LikesListPhotoAdmin)



class CommentListPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_photo', 'username_comment', 'comment')


admin.site.register(CommentListPhoto, CommentListPhotoAdmin)



class UsersListTopicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discription', 'username', 'photo', 'id_topics')


admin.site.register(UsersListTopics, UsersListTopicsAdmin)


class CommentListTopicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_topics', 'username_comment', 'comment')


admin.site.register(CommentListTopics, CommentListTopicsAdmin)



class UsersChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_chat', 'name_chat_user1', 'name_chat_user2', 'photo_chat_user1', 'photo_chat_user2', 'notice_user1', \
    'notice_user2', 'notice_user_all', 'username_user1', 'username_user2')

admin.site.register(UsersChat, UsersChatAdmin)


class NotesChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_chat', 'name_chat', 'notice_user', 'username_user')

admin.site.register(NotesChat, NotesChatAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('is_read', 'message', 'timestamp', 'user', 'owner')

admin.site.register(Notification, NotificationAdmin)


class UsersListPhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'photo', 'id_photo', 'tag')


admin.site.register(UsersListPhotoGallery, UsersListPhotoGalleryAdmin)