# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('content_type_id', models.IntegerField()),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BasicDictionaryRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_weight', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'basic_dictionary_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
                ('content_type_id', models.IntegerField(null=True, blank=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmergencyDictionaryRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_weight', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'emergency_dictionary_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmergencyType',
            fields=[
                ('emergency_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('emergency_type_name', models.TextField()),
            ],
            options={
                'db_table': 'emergency_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmergencyTypeRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'emergency_type_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('emotion_id', models.AutoField(serialize=False, primary_key=True)),
                ('emotion_name', models.TextField()),
            ],
            options={
                'db_table': 'emotion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('event_name', models.TextField()),
                ('event_abstract', models.TextField(null=True, blank=True)),
                ('event_datetime', models.DateTimeField()),
                ('event_place', models.TextField(null=True, blank=True)),
                ('theme_not', models.IntegerField()),
            ],
            options={
                'db_table': 'event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventKeywordRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_weight', models.FloatField()),
            ],
            options={
                'db_table': 'event_keyword_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventNewsRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'event_news_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventPreparation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'event_preparation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventWeiboRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'event_weibo_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gdfan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=20)),
                ('gdfans_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'gdfan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gdfollow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=20)),
                ('gdfollows_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'gdfollow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'myuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('news_website_type', models.TextField()),
                ('news_url', models.TextField()),
                ('news_comment_url_args', models.TextField()),
                ('news_title', models.TextField()),
                ('news_abstract', models.TextField(null=True, blank=True)),
                ('news_content', models.TextField()),
                ('news_source', models.TextField(null=True, blank=True)),
                ('news_source_url', models.TextField(null=True, blank=True)),
                ('news_author', models.TextField(null=True, blank=True)),
                ('news_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('news_comment_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('news_comment_userid', models.TextField(null=True, blank=True)),
                ('news_comment_content', models.TextField()),
                ('news_comment_datetime', models.DateTimeField()),
                ('news_comment_user_place', models.TextField(null=True, blank=True)),
                ('news_comment_goodnumber', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'news_comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewsCommentEmotionRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'news_comment_emotion_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewsWebsite',
            fields=[
                ('news_website_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('index_url', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'news_website',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NormalEvent',
            fields=[
                ('normal_event_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('normal_event_type_name', models.TextField()),
            ],
            options={
                'db_table': 'normal_event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NormalEventDictionaryRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_weight', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'normal_event_dictionary_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NormalEventTypeRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'normal_event_type_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sinauser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'sinauser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SqlsecArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('published', models.IntegerField()),
                ('author_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sqlsec_article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SqlsecArticleColumn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_id', models.IntegerField()),
                ('column_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sqlsec_article_column',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SqlsecColumn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=256)),
                ('intro', models.TextField()),
            ],
            options={
                'db_table': 'sqlsec_column',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Weibo',
            fields=[
                ('weibo_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('weibo_content', models.TextField()),
                ('weibo_userid', models.TextField()),
                ('weibo_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'weibo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeiboComment',
            fields=[
                ('weibo_comment_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('weibo_comment_content', models.TextField()),
                ('weibo_comment_userid', models.TextField()),
                ('weibo_comment_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'weibo_comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeiboCommentEmotionRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'weibo_comment_emotion_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeiboCommentRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'weibo_comment_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeiboEmotionRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'weibo_emotion_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeiboHotspot',
            fields=[
                ('weibo_hotspot_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('weibo_hotspot_name', models.TextField()),
                ('weibo_hotspot_datetime', models.DateTimeField()),
                ('weibo_hotspot_type', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'weibo_hotspot',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeiboHotspotRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'weibo_hotspot_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeiboRepost',
            fields=[
                ('weibo_repost_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('weibo_repost_content', models.TextField()),
                ('weibo_repost_userid', models.TextField()),
                ('weibo_repost_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'weibo_repost',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeiboRepostEmotionRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'weibo_repost_emotion_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeiboRepostRelative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'weibo_repost_relative',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Weibotext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=20)),
                ('weibo', models.TextField()),
                ('time', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'weibotext',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('word_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('word_content', models.TextField()),
                ('attribute', models.IntegerField()),
            ],
            options={
                'db_table': 'word',
                'managed': False,
            },
        ),
    ]
