#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import time


def get_media_id_recent_feed(self):
    if self.login_status:
        now_time = datetime.datetime.now()
        log_string = "%s : Get media id on recent feed \n %s" % (
            self.user_login, now_time.strftime("%d.%m.%Y %H:%M"))
        self.write_log(log_string)
        #url = 'https://www.instagram.com/?__a=1'
        url = 'https://www.instagram.com/graphql/query/?query_hash=60b755363b5c230111347a7a4e242001&variables={}'
        try:
            r = self.s.get(url)
            all_data = json.loads(r.text)

            if 'data' not in all_data:
                print("rate limit reached")
                return 0
            self.media_on_feed = list(all_data['data']['user']['feed_reels_tray']['edge_reels_tray_to_reel']['edges'])
            log_string = "Media in recent feed = %i" % (
                len(self.media_on_feed))
            self.write_log(log_string)
        except Exception as err:
            print("Some message")
            print(err.__class__)
            print(err)
            self.media_on_feed = []
            self.write_log('Except on get media!!')
            time.sleep(20)
            return 0
    else:
        return 0
