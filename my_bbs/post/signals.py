from django.dispatch import Signal, receiver

register_signal = Signal(providing_args=['request', 'user'])

@receiver(register_signal, dispatch_uid='register_callback')
def register_callback(sender, **kwargs):
    print('remote addr: %s, send email to %s' % (
        kwargs['request'].META['REMOTE_ADDR'], kwargs['user'].email))
