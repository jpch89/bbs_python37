from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from post.models import Comment, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    class TitleFilter(admin.SimpleListFilter):
        title = _('标题过滤')
        parameter_name = 'tf'

        def lookups(self, request, model_admin):
            return (
                ('first', _('包含first')),
                ('!first', _('不包含first')),
            )
        
        def queryset(self, request, queryset):
            if self.value() == 'first':
                return queryset.filter(title__contains=self.value())
            elif self.value() == '!first':
                return queryset.exclude(title__contains=self.value()[1:])
            else:
                return queryset
    
    def get_ordering(self, request):
        if request.user.is_superuser:
            return ['id']
        else:
            return self.ordering
    """
    def get_queryset(self, request):
        return self.model._default_manager.filter(title__contains='third')
    """

    # list_display = ('title', 'content', 'is_online', 'user', 'created_time')
    # search_fields = ['title', 'user__username']
    search_fields = ['title', '=user__username']
    list_display = ('title', 'topic_content', 'topic_is_online', 'user')
    # list_filter = ['title', 'user__username']
    list_filter = [TitleFilter, 'user__username']
    ordering = ['id']
    list_per_page = 1
    list_max_show_all = 2
    # fields = ['user', 'title', 'is_online']
    # exclude = ['content']
    """
    fields = [
        ('user', 'title'),
        'content',
        'is_online'
    ]
    """
    """
    fieldsets = (
        ('Topic Part A', {
            'fields': ('title', 'user'),
            'description': 'Topic的title和user',
        }),
        ('Topic Part B', {
            'fields': ('content', 'is_online'),
            'classes': ['collapse', 'wide'],
            'description': 'Topic的content的is_online'
        })
    )
    """
    """
    fields = [('user', 'title'), 'is_online', 'content_length']
    readonly_fields = ('user', 'content', 'content_length')
    """
    # raw_id_fields = ('user', )

    def content_length(self, obj):
        return len(obj.content)
    content_length.short_description = u'话题长度内容'

    def topic_is_online(self, obj):
        return u'是' if obj.is_online else u'否'
    topic_is_online.short_description = u'话题是否在线'

    def topic_content(self, obj):
        return obj.content[:30]
    topic_content.short_description = u'话题内容'

    actions = ['topic_online', 'topic_offline']

    def topic_online(self, request, queryset):
        rows_updated = queryset.update(is_online=True)
        self.message_user(request, '%s topics online' % rows_updated)
    topic_online.short_description = u'上线所选的 %s' % Topic._meta.verbose_name

    def topic_offline(self, request, queryset):
        rows_updated = queryset.udpate(is_online=False)
        self.message_user(request, '%s topics offline' % rows_updated)
    topic_offline.short_description = u'下线所选的 %s' % Topic._meta.verbose_name

    def save_model(self, request, obj, form, change):
        if change and 'is_online' in form.changed_data and not obj.is_online:
            self.message_user(request, 'Topic(%s)被管理员删除了' % obj.id)
            obj.title = '%s(%s)' % (obj.title, '管理员删除')
        super(TopicAdmin, self).save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
