# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:48:06 2015

@author: Marcus Therkildsen
"""
import facebook as fb
from time import sleep as slp

'''
Script for uploading a certain photo to facebook every day
'''


def get_api(cfg):
    graph = fb.GraphAPI(cfg['access_token'], version='2.2')

    # Get page token to post as the page. You can skip
    # the following if you want to post as yourself.
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
    graph = fb.GraphAPI(page_access_token)
    return graph


def main():

    # Enter your page id and access token
    cfg = {
        "page_id"       : "your_page_id",
        "access_token"  : "your_access_token"
        }

    api = get_api(cfg)

    '''
    Post a message
    '''
    # msg = "Here is my message"
    # status = api.put_wall_post(msg)

    '''
    Post an image
    '''
    status = api.put_photo(image=open("path_to/my_image.file_type", 'rb'), album_path=cfg['page_id'] + "/photos")
    return status


if __name__ == "__main__":

    uploaded = 0
    while uploaded is 0:
        try:
            status = main()
            print status
            if 'post_id' in status:
                # Succesfull upload, stop trying
                break

        except Exception:
            pass

        # If unsuccesfull upload, wait 10 seconds and try again
        slp(10)
