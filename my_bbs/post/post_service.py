from post.models import Comment, Topic


def build_topic_base_info(topic):
    """
    构造 Topic 基本信息
    :param topic:
    :return:
    """
    return {
        'id': topic.id,
        'title': topic.title,
        'user': topic.user.username,
        'created_time': topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
    }


def build_comment_info(comment):
    """
    构造 Comment 信息
    :param comment:
    :return:
    """
    return {
        'id': comment.id,
        'content': comment.content,
        'up': comment.up,
        'down': comment.down,
        'created_time': comment.created_time.strftime('%Y-%m-%d %H:%M:%S'),
        'last_modified': comment.last_modified.strftime('%Y-%m-%d %H:%M:%S'),
    }


def build_topic_detail_info(topic):
    """
    构造 Topic 详细信息
    :param topic:
    :return:
    """
    comment_qs = Comment.objects.filter(topic=topic)
    return {
        'id': topic.id,
        'title': topic.title,
        'content': topic.content,
        'user': topic.user.username,
        'created_time': topic.created_time.strftime('%Y-%m-%d %H:%M:%S'),
        'last_modified': topic.last_modified.strftime('%Y-%m-%d %H:%M:%S'),
        'comments': [build_comment_info(comment) for comment in comment_qs],
    }


def add_comment_to_topic(topic, comment):
    """
    给话题添加评论
    :param topic:
    :param content:
    :return:
    """
    return Comment.objects.create(topic=topic, content=content)
