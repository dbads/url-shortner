# system/builtin libraries
import re
import json
from json import dumps
import random, string
from datetime import datetime, date

# django libraries
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# custom modules
from .models import Url
from .serializers import UrlSerializer


#1 Create Short URL /shorten
@csrf_exempt
def shorten(request):
    """_summary_

    Args:
        request: request with shortcode and url in body

    Returns:
        if url:
            not Null
            if shortcode 
                not null: 
                    shortcode:
                        is valid: {shortcode: shortcode, status: 201}
                        not valid: {ERROR: sortcode is not valid}
                null:
                    {shortcode: shortcode, status: 201}
        else:
            {ERROR: url must be provided for shotening}
    """
    # shorten the url and return expected response
    if request.method == 'POST':
        request_body = json.loads(request.body)
        url = request_body.get('url', None)
        shortcode = request_body.get('shortcode', None)

        response = {}
        status = 200
        if url:
            matched = False
            if shortcode is not None:
                exsitng_shortcodes = Url.objects.filter(shortcode=shortcode)
                if len(exsitng_shortcodes) > 0:
                    print('${shortcode}: shortcode already in use')
                    response["ERROR"] = 'shortcode already in use'
                    status = 409
                else:
                    matched = bool(re.match('[0-9a-zA-Z_]{4,}', shortcode))
                    if matched:
                        response["shortcode"] = shortcode
                        status = 201
                    else:
                        print('shortcode requested doesn\t meet the requirements')
                        response['ERROR'] = 'shortcode requested doesn\t meet the requirements'
                        status = 422
            else:
                shortcode = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                response["shortcode"] = shortcode
                status = 201

            if status == 201:
                print(f'Creating new shortcode ${shortcode} for ${url}')
                new_url_shorcode = Url()
                new_url_shorcode.actual = url
                new_url_shorcode.shortcode = shortcode
                new_url_shorcode.start_date = date.today()
                new_url_shorcode.save()

            return HttpResponse(dumps(response), status=status)
        else:
            response = {
                'ERROR': 'url must be provided for shortening'
            }
            return HttpResponse(dumps(response), status=400)


#2 Get URL /<shortcode>
def get_url(request, shortcode):
    # shorten the url and return expected response
    try:
        url = Url.objects.get(shortcode=shortcode)
    except Url.DoesNotExist:
        url = None
    
    status = 200
    response = {}
    if url:
        status = 302 
        response["location"] = url.actual

        # update url metadata
        url.redirect_count += 1
        url.last_seen_date = date.today()
        url.save()
    else:
        print('${shortcode}: shortcode does not exist')
        status = 404
        response["ERROR"] = 'shortcode does not exist'
    
    return HttpResponse(dumps(response), status=status)


#3 Get Stats of Shortened URL /<shortcode>/stats
def stats(request, shortcode):
    # shorten the url and return expected response
    urls = Url.objects.filter(shortcode=shortcode)
    
    status = 200
    response = {}
    if len(urls) > 0:
        status = 200
        url_data = UrlSerializer(urls[0]).data
        response["startDate"] = url_data["start_date"]
        response["lastSeenDate"] = url_data["last_seen_date"]
        response["redirectCount"] = url_data["redirect_count"]
    else:
        print('${shortcode}: shortcode does not exist')
        status = 404
        response["ERROR"] = 'shortcode does not exist'
    
    return HttpResponse(dumps(response), status=status)


# we can write job to delete shorturl where today - last_seen_date  >= n, n can be decided whcih can be 30 days eg