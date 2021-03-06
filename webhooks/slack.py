from slacker import Slacker, Users

from django.conf import settings


def _invite(self, email, **kwargs):
    """
    There's only a private API to invite users to a slack team.
    This function will be monkeypatched onto slacker.User and it seems to work.
    """
    data = dict(email=email, **kwargs)
    channels = data.pop('channels', None)
    if channels is not None:
        data['channels'] = ','.join(channels)
    data['_attempts'] = 1  # required by slack for some reason
    return self.post('users.admin.invite', data=data)


def _monkeypatch_user_invite():
    Users.invite = _invite


def get_connection(slack_name):
    token = settings.SLACK_API_TOKENS[slack_name]
    return Slacker(token)


def _convert_channels(slack_team, channels):
    converted = []
    for channel in channels:
        if not channel.startswith('#'):
            converted.append(channel)
            continue
        channel = channel[1:]  # strip leading '#'
        converted.append(slack_team.channels.get_channel_id(channel))

    return converted
