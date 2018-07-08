#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .new_unfollow import new_unfollow


def new_auto_mod_unfollow2(self):
    log_string = "Trying to unfollow: %s" % (self.current_user)
    whitelist_found = False
    self.write_log(log_string)
    for wluser in self.unfollow_whitelist:
        if wluser == self.current_user:
            log_string = (
                "found whitelist user, starting search again")
            self.write_log(log_string)
            whitelist_found = True
            break
    if whitelist_found is not True:
            new_unfollow(self, self.current_id, self.current_user)
