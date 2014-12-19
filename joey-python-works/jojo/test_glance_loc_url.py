import re
import urlparse


pattern = re.compile(r'^https?://\S+/v2/images/\S+$')


def create_ep_by_loc_url(loc_url):
    if not is_glance_location(loc_url):
        return None
    piece = urlparse.urlparse(loc_url)
    return piece.scheme + '://' + piece.netloc + '/'


def is_glance_location(loc_url):
    return pattern.match(loc_url)


def get_id_from_glance_loc_url(loc_url):
    if not is_glance_location(loc_url):
        return ''
    _index = loc_url.find('/v2/images/') + len('/v2/images/')
    return loc_url[_index:]


url = 'http://162.2.110.189:9292/v2/images/4bc0a818-7661-449f-8281-e045d844c2cf'
s = get_id_from_glance_loc_url(url)
ep = create_ep_by_loc_url(url)
print s
print ep
