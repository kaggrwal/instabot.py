#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login="secluded_nomad",
    password="dob2919",
    like_per_day=500,
    comments_per_day=0,
    tag_list=['wanderlust', '_soi', 'nikonindia','bnwphotography','incredibleindia','travelislife','photographers_of_india','travelgram','storiesofindia','_woi','visionofpictures','shots_of_india','newphotographers','instawriters','writersofindia','igwriters','poetry','shayri','instawriters','writersofinstagram'],
    tag_blacklist=['porn', 'sex','hotgirl','instaporn','deals','sexy'],
    user_blacklist={},
    max_like_for_one_tag=25,
    follow_per_day=2,
    follow_time=1 * 60 * 30,
    unfollow_per_day=20,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["this", "the", "your"],
                  ["photo", "picture", "pic", "shot", "snapshot"],
                  ["is", "looks", "feels", "is really"],
                  ["great", "super", "good", "very good", "good", "wow",
                   "WOW", "cool", "GREAT","magnificent", "magical",
                   "very cool", "stylish", "beautiful", "so beautiful",
                   "so stylish", "so professional", "lovely",
                   "so lovely", "very lovely", "glorious","so glorious",
                   "very glorious", "adorable", "excellent", "amazing"],
                  [".", "..", "...", "!", "!!", "!!!"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['9gag', 'shots_of_india','unheard_shayri','villainquote','nteetie','photowalkdelhi','ghietauelena','loeshoekstra','thegameoflaughs','people_who_rise','apextvofficial','stereoindia','sakshimalik','dlf_cyberhub','meenakshichaudhary006','anunaysood','thescientistfacts','h4pp1e','clone_collection','latest_one.in','technicalbaba_','mishti.and.meat','corporate.bytes','pruvichowdary','trendfilms','ixigo','artistsadda','oneplus','thelocaltrain','kailash.kumar11','famehazel','ankita_narayan_','sassy_thoughts','__funny__chats__','6amsuccess','adventure_nation_outdoor_tribe','kriti.kharbanda','akaushal2945','time4knowledge','divinebucketlist','iamtarunjit','markvelasquez101','thinkandcode','codechef','usabilla','ode_to_travel','shootguru','wandering_dreamcatcher','workoutsofficial','monkey__shanti','mrwhosetheboss','lalitshokeen1515','horrorphiles','fairwarningcareers','vision_of_india','asabhyak','sumeetvyas','instagram','selenagomez','natgeo','kajalaggarwaloffical','akshita.chhabra','deepikapadukone','aliaabhatt','priyankachopra','sunnnyleone','ileana_official','jacquelinef143','naruto','nina','chan.singh7','evelyn_sharma','sarcasm_only','thegoodquote','barked','pu_chd','prachidesai','heenasihag','theawkwardyeti','chandigarhians__','factbolt','asapscience','tvfqtiyapa','allindiabakchod','narendramodi','navagg79','historytv18','the.realshit.gyan','namelsspc','akshaykumar','streets.of.india','500px','humansofchandigarh','the.ramukaka','virat.kohli','photgraphers_of_india','delhigram','stories.of.india','indianshutterbugs','indiatravelgram','jitendrak1','rajography','spacex','colours.of.india','nikonindiaofficial','yourstory_co','desi_diaries','simrankaur9492','troll_punjabi','sciencejoke.s','chemistryjokes','curiositydotcom','futurism','ethereal.colours','hiswriteups','longexpo_shotz','developerjobs4you','monikaspeaks','geekspin','wevolverapp','elonmusk','scrawledstories','thescribbledstories','ttt_official','scoopwhoop','thewashroomstories','amandacerny','ishivyas18','garbagebinofficial','bosplanet','natalie.dormer','emilia_clarke','roycebairphoto','singh_nikita','dslrofficial','theunrulytravler','streetphotographyindia','indian.photography','india.clicks','yourshot_india','indiapictures','igersofindia','photographers_hub_india'])
while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 2

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")

