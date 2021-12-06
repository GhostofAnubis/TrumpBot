import re
import random
presidential_time = 0
notmypresident = True
remembered_name = ""
introduced = False


wall_responses = [">>It's a great idea despite what people say.  Millions of Americans want it.",
                  ">>Some bad hombres across the boarder.", "It will bring millions of jobs.",
                  "The Demoncrats don't like it.",
                  ">>Take a look at Israel. They're building another wall. Their wall is 99.9 percent effective, they told me -- 99.9 percent. That's what it would be with us, too. The only weakness is they go to a wall and then they go around the wall. They go around the wall and in. Okay?",
                  ">>Whether it's $8 billion or $2 billion or $1.5 billion, it's going to build a lot of wall. We're getting it done. We're right now in construction with wall in some of the most important areas.",
                  ">>I wish people would read or listen to my words on the Border Wall. This was in no way a concession. It was taking care of millions of people who were getting badly hurt by the Shutdown with the understanding that in 21 days, if no deal is done, it's off to the races!"]
china_responses = [">>Trade negotiators have just returned from China where the meetings on Trade were very productive. Now at meetings with me at Mar-a-Lago giving the details. In the meantime, Billions of Dollars are being paid to the United States by China in the form of Trade Tariffs!",
                ">>I'll put them in the room and let them speak up. Because any deal I make with China, if it's the great -- it's going to be better than any deal that anybody ever dreamt possible, or I'm not going to have a deal. It's a very simple.",
                ">>We've been losing, on average, $375 billion a year with China. A lot of people think it's $506 billion. Some people think it's much more than that. We're going to be leveling the playing field. The tariffs are hurting China very badly. They don't want them.",
                ">>We have a big team over in China right now, and they're working very hard, dealing with the Chinese...",
                ">>I don't blame China for taking advantage of us -- I blame our leaders and representatives for allowing this travesty to happen. I have great respect for President Xi, and we are now working on a new trade deal with China."]
deals_responses = [">>You know whats a bad deal? California now wants to scale back their already failed fast train project by substantially shortening the distance so that it no longer goes from L.A. to San Francisco. A different deal and record cost overruns. Send the Federal Government back the Billions of Dollars WASTED!",
                ">>I do know one of the Worst deals ever made, probably the worst trade deal ever done, although I happen to think that the WTO is not so good, either we're replacing NAFTA with a brand new U.S-Mexico-Canada agreement that everybody is loving, gonna get Congress to approve it. We've got to get Congress to approve it, we'll get it.",
                ">>Schumer and the Democrats are big fans of being weak and passive with Iran. They have no clue as to the danger they would be inflicting on our Country. Iran is in financial chaos now because of the sanctions and Iran Deal termination. Dems put us in a bad place.",
                ">>Well if we're talking bad trade deals, NAFTA was one of the worst trade deals ever made by a country. It killed our country. This landmark trade deal will increase exports of wheat from Montana, dairy from Wisconsin, chicken from Georgia, and products from farmers and ranchers all across our country."]
ivanka_responses = [">>I love Ivanka, if Ivanka weren't my daughter perhaps I'd be dating her.",
                    ">>She’s actually always been very voluptuous. She’s tall, she’s almost six feet tall and she’s been, she’s an amazing beauty.",
                    ">>You know who’s one of the great beauties of the world, according to everybody? And I helped create her. Ivanka. My daughter, Ivanka. She’s 6 feet tall; she’s got the best body.",
                    ">>Yeah, she’s really something, and what a beauty, that one. If I weren’t happily married and, ya know, her father…",
                    ">>Oh, Ivanka can handle herself. Ivanka can handle herself. These are all in the historical records. There was no deletion whatsoever, unlike Hillary Clinton, who deleted 33,000 emails; unlike Hillary Clinton, who had a server in the basement. Ivanka didn't."]
hillary_responses = [">>The fact is that the real collusion was between Hillary and the Democrats and the other side with Russia. That's where the collusion that's starting, to make a lot more sense. But that's where the collusion is with the Democrats and with Russia and with others, and by the way, there's also collusion between the Democrats and the fake news right here, and they know it better than anybody too.",
                    ">>Why didn't they go after Hillary Clinton for her emails? She had thirty three thousand emails that were deleted after receiving a subpoena from Congress.",
                    ">>I won't say whether she was a good candidate or not. I mean, the primary collusion was Hillary Clinton.",
                    ">>What about Hillary to FBI and her 33,000 deleted Emails? What about Lisa & Peter's deleted texts & Wiener's laptop? Much more!",
                    ">>Remember July 4th weekend when Crooked went before FBI & wasn't sworn in, no tape, nothing?"]
drink_responses = [">>My favorite drink is covfefe.",  ">>My favorite color, it's a very good color, has to be covfefe", ">>Covfefe with a little milk, Americans love it."]
russia_responses = [">>The fact is that the real collusion was between Hillary and the Democrats and the other side with Russia. That's where the collusion that's starting, to make a lot more sense.",
                    ">>After two years and interviewing more than two hundred witnesses, the Senate Intelligence Committee has NOT discovered any direct evidence of a conspiracy between the Trump Campaign and Russia. Get over it.",
                    ">>What's happened to me should never be allowed to happen to another president. With investigations on things that never took place, like Russia. You know, the Russia collusion, delusion we call it. I call it a hoax.",
                    ">>I am certain that, at some time in the future, President Xi and I, together with President Putin of Russia, will start talking about a meaningful halt to what has become a major and uncontrollable Arms Race.",
                    ">>I had a great meeting with Vladimir Putin. Great meeting. We got -- I talked about everything. We will do great."]
putin_responses = [">>Great guy. Born leader.", ">>I don't see why we can't be friends with Russia, with Putin.  Why not? They'd be great allies.", ">>I had a great meeting with Vladimir Putin. Great meeting. We got -- I talked about everything. We will do great.",
                    ">>when I was with Putin, they said, Trump was too nice. He was too nice. It was terrible. So one I was too tough, it's terrible. I'll cause war. The other one, I'm too nice, I'm too nice. I was nice. It's the first time I've ever been called too nice.",
                    ">>My Putin meeting was one of the best I've ever had."]
fa_responses = [">>But if you look at Idlib Province in Syria, I stopped the slaughter of perhaps 3 million people. Nobody talk about that.",
                ">>I mean look at the UK. So with the UK, we're continuing our trade, and we are going to actually be increasing it very substantially as time goes by. We expect that the UK will be very, very substantially increased as it relates to trade with the United States. The relationship there, also, is very good. We have a lot of great announcements having to do with Syria and our success with the eradication of the caliphate.",
                ">>Well if you look at ISIS, ISIS had a vast amount of territory in Syria and Iraq. When I became President, I said, 'I want to see what they have.' And I looked, and it was a mess. It was a lot. When I took office, one of my very first acts was to go to the Pentagon and ask them to produce and show me a plan to defeat ISIS. Under the new approach we developed, we empowered our commanders in the field, enabled our partners on the ground, and directly confronted ISIS’s wicked ideology.",
                ">>My administration has acted decisively to confront the world's leading state sponsor of terror: the radical regime in Iran. To ensure this corrupt dictatorship never acquires nuclear weapons, I withdrew the United States from the disastrous Iran nuclear deal.  How come we don't talk about that?"]
self_reference_responses = [">>Why would I care about that?", ">>I'm better than you.",  ">>Trump is something you should understand more.", ">>Less of that.  More of me."]

def introduction():
    global introduced

    if not introduced:
        global remembered_name

        print(">> No need for introductions. \n >>I'm the best POTUS that ever was and ever will be.  I know your name but say your first name anyway. ")
        yourname = input()
        remembered_name = yourname
        print(">> Wow," + " " + yourname + "." + " " + "Average name.")
        print(">>Remember to talk one setence at a time with punctuation.  I don't have good attention span.")
        introduced = True
    else:
        return None

def topics():
    print(">>These are things I like to talk about:")
    print(">>The Wall, China, Trade Deals, Ivanka, Hillary, My favorite drink, Russia, Foreign Affairs")

def input_check():
    topic_responses = [ ">>Let's change subject " + remembered_name, ">>Boring. Next:", ">>What about you " + remembered_name, ">>You know what's important? Not this, try again " + remembered_name, ">>Let's continue with a non waste of time.", ">>Done. Done. and Done. Next?:", ">>Oh please, how about something else, huh" + remembered_name, "Obviously, we should move on."]
    global presidential_time
    presidential_time +=1
    topic = input()
    #keys
    wall_key = r"wall|Wall|boarder|crossing|aliens|illegal aliens|job|jobs"
    wall_people_key = r"Mexico|mexico|mexicans|Mexicans|people|crossers"
    china_key = r"china|China|asia|Asia|Asian|asian"
    deals_key = r"deal|deals|Deals|Deal|Business|business|company|Towers|towers|trade"
    ivanka_key = r"Ivanka|daughter|ivanka|family|beautiful"
    hillary_key = r"Hillary|hillary|Clinton|clinton|secretary"
    drink_key = r"drink|Drink|favorite beverage"
    russia_key = r"Putin|putin|Russia|russia|investigation|collusion|elections|election|campaign"
    fa_key = r"Saudi|Middle|East|east|middle|EU|European|Union|Brexit|england|uk|UK|Syria|syria|ISIS|isis|ISIL|foreign|Foreign|affairs|Affairs"
    self_reference_key = r"me|myself|my|mine"
    self_like_key = r"I like|i like|I love|I think|I believe"
    trump_gen = r"tan|America great|america|America|great|again"
    trump_key = r"Trump|you|your"
    trump_key_like = r"you like|your favorite"
    trump_key_talk = r"talk|about|else|can you talk|can you do|else"
    trump_key_love = r"love"

    #searches
    try_wall = re.search(wall_key, topic)
    try_china = re.search(china_key, topic)
    try_deals = re.search(deals_key, topic)
    try_ivanka = re.search(ivanka_key, topic)
    try_hillary = re.search(hillary_key, topic)
    try_drink = re.search(drink_key, topic)
    try_russia = re.search(russia_key, topic)
    try_fa = re.search(fa_key, topic)
    try_self = re.search(self_reference_key, topic)
    try_trump = re.search(trump_key, topic)
    try_self_like = re.search(self_like_key, topic)
    try_trumpgen = re.search(trump_gen, topic)


    if try_wall:
        m = re.search(r"jobs|job", topic)
        if m:
            print(">>The wall will provide jobs. Millions.")
        if re.search(wall_people_key, topic):
            print(random.choice(wall_people_key))
            conversationflow()
        else:
            print(random.choice(wall_responses))
            print(random.choice(topic_responses))
            conversationflow()
    elif try_china:
        print(random.choice(china_responses))
        print(random.choice(topic_responses))
        conversationflow()
    elif try_deals:
        print(random.choice(deals_responses))
        print(random.choice(topic_responses))
        conversationflow()
    elif try_ivanka:
        print(random.choice(ivanka_responses))
        print(random.choice(topic_responses))
        conversationflow()
    elif try_hillary:
        print(random.choice(hillary_responses))
        print(random.choice(topic_responses))
        conversationflow()
    elif try_drink:
        print(random.choice(drink_responses))
        print(random.choice(topic_responses))
        conversationflow()
    elif try_russia:
        m = re.search(r"Putin|putin", topic)
        if m:
            print(random.choice(putin_responses))
            print(random.choice(russia_responses))
            print(random.choice(topic_responses))
            conversationflow()
        else:
            print(random.choice(russia_responses))
            print(random.choice(topic_responses))
            conversationflow()
    elif try_trumpgen:
        m = re.search(r"tan", topic)
        l = re.search(r"america great|America great|again|america|America", topic)
        if m:
            list = [">>All natural baby", ">>Its perfect, I'm perfect, don't even have a tan"]
            print(random.choice(list))
        elif l:
            print(">>I will make it great.  I'm great, we're great. America.")

    elif try_fa:
        print(random.choice(fa_responses))
        print(random.choice(topic_responses))
        conversationflow()
    elif try_self:
        print((random.choice(self_reference_responses)))
        print(random.choice(topic_responses))
        conversationflow()
    elif try_self_like:
        m = re.search(r"I like|love (\w+)", topic)
        l = re.search(r"I think|believe (\w+)", topic)
        if m:
            list = [">>Why do you think I care about " + m.groups()[0] + "?", ">>If I dont love " + m.groups()[0] + ", why should you?", ">>Some people love em, great people dont."]
            print(random.choice(list))
        elif l:
            list = [">>I don't care about what you think", ">>I believe that China made that up to get us out of a good deal" ]
            print(random.choice(list))
        conversationflow()
    elif try_trump:
        l = re.search(r"you think|believe|feel", topic)
        m = re.search(r"are you (\w+)", topic)
        n = re.search(r"I (\w+) you", topic)
        if l:
            list = [">>Made up by China.  Bad idea.", ">>No such thing, just like Global Waming."]
            print(random.choice(list))
            conversationflow()
        elif m:
            list = [">>No you.", ">>You're " + m.groups()[0]]
            print(random.choice(list))
            conversationflow()
        elif n:
            list = [">>You know what I hate? Mexicans stealing jobs.", ">>I " + n.groups()[0] + " you too.", ">>I hate lazy people."]
            print(random.choice(list))
            conversationflow()

        if re.search(trump_key_like, topic):
            print(">>What I like is everything Trump.  My favorite anything is my Presidency and anything to do with me.")
            print(random.choice(topic_responses))
            conversationflow()

        elif re.search(trump_key_love, topic):
            print(random.choice(ivanka_responses))
            conversationflow()
        elif re.search(trump_key_talk, topic):
            topics()
            conversationflow()

        else:
            print(random.choice(self_reference_responses))
            print(random.choice(topic_responses))
            conversationflow()
    else:
        topics()
        conversationflow()


def conversationflow():
    global presidential_time
    if presidential_time > 20:
        print(">>You're fired")
        print(">>Secret service, get " + remembered_name + " out of here!")
        exit()
    else:
        input_check()



while notmypresident:
    introduction()
    topics()
    conversationflow()
