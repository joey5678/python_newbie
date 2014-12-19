GLOBAL_MAP = {}


def remove_invalid_loc(id, url):
    global GLOBAL_MAP
    image_map = GLOBAL_MAP[id]
    if not image_map:
        return
    locs = image_map['locations'] or []
    if not locs:
        return
    del_locs = [loc for loc in locs if loc['url'] == url]
    if not del_locs:
        return
    locs.remove(del_locs[0])


def get_copy_location_url(image):
    global GLOBAL_MAP
    image_id = image.get('id')
    locations = image.get('locations', [])
    if not locations:
        return ''
    if image_id not in GLOBAL_MAP.keys():
        GLOBAL_MAP[image_id] = {'locations':
                                    [{'url': locations[0]['url'],
                                      'count': 1,
                                      'is_using':1
                                     }]
        }
        return locations[0]['url']
    else:
        recorded_locs = GLOBAL_MAP[image_id]['locations']
        record_urls = [loc['url'] for loc in recorded_locs]
        for location in locations:
            if location['url'] not in record_urls:
                recorded_locs.append({
                    'url': location['url'],
                    'count':1,
                    'is_using':1
                })
                return location['url']
        not_used_locs = [loc for loc in recorded_locs
                         if not loc['is_using']]
        if not_used_locs:
            _loc = not_used_locs[0]
            _loc['is_using'] = 1
            _loc['count'] += 1
            return _loc['url']
        _my_loc = sorted(recorded_locs, key=lambda my_loc: my_loc['count'])[0]
        _my_loc['count'] += 1
        return _my_loc['url']

# _url = get_copy_location_url(my_image)
# print _url
#
# _url = get_copy_location_url(my_image)
# print _url
#
# _url = get_copy_location_url(my_image)
# print _url
#
# _url = get_copy_location_url(my_image)
# print _url
#
# _url = get_copy_location_url(my_image)
# print _url
#
# _url = get_copy_location_url(my_image)
# print _url


def choose_location(f):

    def wrapper(*args, **kwargs):
        print args[0]
        _image = kwargs.get('image')
        _id = _image['id']
        _url0 = get_copy_location_url(_image)
        kwargs['url'] = _url0
        r_code = -1 #f(*args, **kwargs)
        error_urls = []
        while r_code != 0:
            r_code = f(*args, **kwargs)
            if r_code == 0:
                break
            error_urls.append(_url0)
            _url0 = get_copy_location_url(_image)
            if not _url0:
                break
            kwargs['url'] = _url0

        for e_url in error_urls:
            remove_invalid_loc(_id, e_url)
        return r_code
    return wrapper



@choose_location
def do_business(id, image=None, **kwargs):
    url = kwargs['url']
    if not url or url.startswith('swift'):
        print 'the url is not valid, or not exists. %s' %url
        return -1
    print 'the url is ok, %s' %url
    return 0


my_image = dict()
my_image['id'] = 1
my_image['locations'] = [{'url': 'file:///'}, {'url': 'http://'}, {'url': 'swift://'}]

do_business(1, image=my_image)
do_business(2, image=my_image)
