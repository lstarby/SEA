#coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        # unique_together = (('user_id', 'permission_id'),)


class BasicDictionaryRelative(models.Model):
    word = models.ForeignKey('Word')
    emotion = models.ForeignKey('Emotion')
    word_weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basic_dictionary_relative'
        # unique_together = (('word_id', 'emotion_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmergencyDictionaryRelative(models.Model):
    word = models.ForeignKey('Word')
    emergency_type = models.ForeignKey('EmergencyType')
    word_weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_dictionary_relative'
        # unique_together = (('word_id', 'emergency_type_id'),)


class EmergencyType(models.Model):
    emergency_type_id = models.AutoField(primary_key=True)
    emergency_type_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'emergency_type'


class EmergencyTypeRelative(models.Model):
    event = models.ForeignKey('Event')
    emergency_type = models.ForeignKey(EmergencyType)

    class Meta:
        managed = False
        db_table = 'emergency_type_relative'
        # unique_together = (('event_id', 'emergency_type_id'),)


class Emotion(models.Model):
    emotion_id = models.AutoField(primary_key=True)
    emotion_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'emotion'


class Event(models.Model):
    event_id = models.BigIntegerField(primary_key=True)
    event_name = models.TextField()
    event_abstract = models.TextField(blank=True, null=True)
    event_datetime = models.DateTimeField()
    event_place = models.TextField(blank=True, null=True)
    theme_not = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event'

    def toDICT(self):
        a = dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])
        a['image']=None
        totalnum =0
        b = News.objects.filter(eventnewsrelative__event_id=self.event_id)
        c = b.filter(news_image__isnull=False)
        if c.count()!=0:
            a['image']=c[0].news_image

        #根据事件的id获取其所有新闻评论数
        for ns in b:
            news_comment_set_sub = ns.newscomment_set.all()
            num_sub = news_comment_set_sub.count()
            totalnum+=num_sub

        a['comment_num']=totalnum
        #如果事件有父事件，返回父事件的event_id
        # event = Event.objects.get(event_id=)
        eventpreparation = EventPreparation.objects.filter(later_event_id=self.event_id)
        if eventpreparation:
            a['parent_event_id']=eventpreparation[0].pre_event_id
            a['parent_event_name']=eventpreparation[0].pre_event.event_name
        return a

class EventKeywordRelative(models.Model):
    event = models.ForeignKey(Event,primary_key=True)
    word = models.ForeignKey('Word')
    word_weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'event_keyword_relative'
        # unique_together = (('event_id', 'word_id'),)


class EventNewsRelative(models.Model):
    event = models.ForeignKey(Event,primary_key=True)
    news = models.ForeignKey('News')

    class Meta:
        managed = False
        db_table = 'event_news_relative'
        # unique_together = (('event_id', 'news_id'),)


class EventPreparation(models.Model):
    pre_event = models.ForeignKey(Event,related_name='pre_event',primary_key=True)
    later_event = models.ForeignKey(Event,related_name='later_event')

    class Meta:
        managed = False
        db_table = 'event_preparation'
        # unique_together = (('pre_event_id', 'later_event_id'),)


class EventWeiboRelative(models.Model):
    event = models.ForeignKey(Event,primary_key=True)
    weibo_hotspot = models.ForeignKey('WeiboHotspot')

    class Meta:
        managed = False
        db_table = 'event_weibo_relative'
        # unique_together = (('event_id', 'weibo_hotspot_id'),)


class Gdfan(models.Model):
    user_id = models.CharField(max_length=20)
    gdfans_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'gdfan'
        unique_together = (('user_id', 'gdfans_id'),)


class Gdfollow(models.Model):
    user_id = models.CharField(max_length=20)
    gdfollows_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'gdfollow'
        unique_together = (('user_id', 'gdfollows_id'),)


class Myuser(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'myuser'

@python_2_unicode_compatible
class News(models.Model):
    news_id = models.BigIntegerField(primary_key=True)
    news_website = models.ForeignKey('NewsWebsite')
    news_website_type = models.TextField()
    news_url = models.TextField()
    news_comment_url_args = models.TextField()
    news_title = models.TextField()
    news_abstract = models.TextField(blank=True, null=True)
    news_content = models.TextField()
    news_source = models.TextField(blank=True, null=True)
    news_source_url = models.TextField(blank=True, null=True)
    news_author = models.TextField(blank=True, null=True)
    news_datetime = models.DateTimeField()
    news_image = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'news'
    def __str__(self):
        return str(self.news_id)
@python_2_unicode_compatible
class NewsComment(models.Model):
    news_comment_id = models.BigIntegerField(primary_key=True)
    news = models.ForeignKey(News)
    news_comment_userid = models.TextField(blank=True, null=True)
    news_comment_content = models.TextField()
    news_comment_datetime = models.DateTimeField()
    news_comment_user_place = models.TextField(blank=True, null=True)
    news_comment_goodnumber = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_comment'
        # unique_together = (('news_comment_id', 'news_id'),)
    def __str__(self):
        return self.news_comment_content

    def toDICT(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])

class NewsCommentEmotionRelative(models.Model):
    news_comment = models.ForeignKey(NewsComment,primary_key=True)
    news = models.ForeignKey(News)
    emotion = models.ForeignKey(Emotion)

    class Meta:
        managed = False
        db_table = 'news_comment_emotion_relative'
        unique_together = (('news_comment', 'news', 'emotion'),)

@python_2_unicode_compatible
class NewsWebsite(models.Model):
    news_website_id = models.AutoField(primary_key=True)
    name = models.TextField()
    index_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_website'
    def __str__(self):
        return self.name

class NormalEvent(models.Model):
    normal_event_type_id = models.AutoField(primary_key=True)
    normal_event_type_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'normal_event'


class NormalEventDictionaryRelative(models.Model):
    word = models.ForeignKey('Word')
    normal_event_type = models.ForeignKey(NormalEvent,primary_key=True)
    word_weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normal_event_dictionary_relative'
        # unique_together = (('word_id', 'normal_event_type_id'),)


class NormalEventTypeRelative(models.Model):
    event = models.ForeignKey(Event,primary_key=True)
    normal_event_type = models.ForeignKey(NormalEvent)

    class Meta:
        managed = False
        db_table = 'normal_event_type_relative'
        # unique_together = (('event_id', 'normal_event_type_id'),)


class Sinauser(models.Model):
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinauser'
        unique_together = (('user_id', 'user_name'),)


class SqlsecArticle(models.Model):
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    content = models.TextField()
    published = models.IntegerField()
    author_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sqlsec_article'


class SqlsecArticleColumn(models.Model):
    article_id = models.IntegerField()
    column_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sqlsec_article_column'
        unique_together = (('article_id', 'column_id'),)


class SqlsecColumn(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    intro = models.TextField()

    class Meta:
        managed = False
        db_table = 'sqlsec_column'


class Weibo(models.Model):
    weibo_id = models.BigIntegerField(primary_key=True)
    weibo_content = models.TextField()
    weibo_userid = models.TextField()
    weibo_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'weibo'


class WeiboComment(models.Model):
    weibo_comment_id = models.BigIntegerField(primary_key=True)
    weibo_comment_content = models.TextField()
    weibo_comment_userid = models.TextField()
    weibo_comment_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'weibo_comment'


class WeiboCommentEmotionRelative(models.Model):
    weibo_comment = models.ForeignKey(WeiboComment)
    emotion = models.ForeignKey(Emotion,primary_key=True)

    class Meta:
        managed = False
        db_table = 'weibo_comment_emotion_relative'
        # unique_together = (('weibo_comment_id', 'emotion_id'),)


class WeiboCommentRelative(models.Model):
    weibo = models.ForeignKey(Weibo,primary_key=True)
    weibo_comment = models.ForeignKey(WeiboComment)

    class Meta:
        managed = False
        db_table = 'weibo_comment_relative'
        # unique_together = (('weibo_id', 'weibo_comment_id'),)


class WeiboEmotionRelative(models.Model):
    weibo = models.ForeignKey(Weibo)
    emotion = models.ForeignKey(Emotion,primary_key=True)

    class Meta:
        managed = False
        db_table = 'weibo_emotion_relative'
        # unique_together = (('weibo_id', 'emotion_id'),)


class WeiboHotspot(models.Model):
    weibo_hotspot_id = models.BigIntegerField(primary_key=True)
    weibo_hotspot_name = models.TextField()
    weibo_hotspot_datetime = models.DateTimeField()
    weibo_hotspot_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weibo_hotspot'


class WeiboHotspotRelative(models.Model):
    weibo = models.ForeignKey(Weibo,primary_key=True)
    weibo_hotspot = models.ForeignKey(WeiboHotspot)

    class Meta:
        managed = False
        db_table = 'weibo_hotspot_relative'
        # unique_together = (('weibo_id', 'weibo_hotspot_id'),)


class WeiboRepost(models.Model):
    weibo_repost_id = models.BigIntegerField(primary_key=True)
    weibo_repost_content = models.TextField()
    weibo_repost_userid = models.TextField()
    weibo_repost_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'weibo_repost'


class WeiboRepostEmotionRelative(models.Model):
    weibo_repost = models.ForeignKey(WeiboRepost,)
    emotion = models.ForeignKey(Emotion,primary_key=True)

    class Meta:
        managed = False
        db_table = 'weibo_repost_emotion_relative'
        # unique_together = (('weibo_repost_id', 'emotion_id'),)


class WeiboRepostRelative(models.Model):
    weibo = models.ForeignKey(Weibo,primary_key=True)
    weibo_repost = models.ForeignKey(WeiboRepost)

    class Meta:
        managed = False
        db_table = 'weibo_repost_relative'
        # unique_together = (('weibo_id', 'weibo_repost_id'),)


class Weibotext(models.Model):
    user_id = models.CharField(max_length=20)
    weibo = models.TextField()
    time = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'weibotext'


class Word(models.Model):
    word_id = models.BigIntegerField(primary_key=True)
    word_content = models.TextField()
    attribute = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'word'

