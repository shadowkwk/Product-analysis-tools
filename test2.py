import re
text = ''' 
My son is in love!!! These headphones are just the perfect thing for my teenage son!!!! He uses them for a few different things…including school work while he’s at home! But he mainly uses them for his GAMING ADDICTION!!! HELP!!! These have really great sound quality!!!
In conclusion, I love the sound effect and the shining(on both sides) will I turn it on :) During the game, my teammates could hear me clearly, that's good. The sound effect is great and I love wearing it to watch movies.
The gaming headset is so far durable, my dog chews the cord and they still work.
The sound is clear, he is able to hear and be heard by others with no issue. He loves the look of it very cool. It transitions from gaming to movies effortlessly and he can use it both with his XBOX and his tablet with no issue. Highly recommend if you are looking for great quality at a great price. 10/10.
I bought these for my son for Christmas and let him use them for a little while before asking him how he likes them. He's very pleased. He said he especially likes how you can hear the sounds separately in each ear when gaming so you can tell where people or things are.
For each players, a good gaming headset is essential. What kind of headset we choose depends on what game we play. For example, if we are playing a game of PUBG type that we need enough surround sound to know where the enemy is at all times, and this gaming headset can well meet our needs.
My son's last gaming headset microphone broke. So I chose to buy this headset after reading the reviews. I waited about a month to make this review, so that I can give an accurate and honest one. My son is a game player and a live streamer. He said this headset are equivalent to or even better than the more expensive nearly $100 headset he used before. This headset is relatively light, and there will be no falling feeling when it is hung on the ear.
I'm very happy with these. Lightweight, comfortable and sound is very good for gaming.
I've purchased three pairs of this same headphone over the last 5 years. Two for use by us and the third as a gift for an Angle Tree gift. These are a solid option for a gaming headset at an affordable price. The audio quality has been good enough for both music and gaming where direction sound is important (think shooters).
3.5mm jack is defective, I tried it on a couple of device and if you hold it just right you get sound out of both ears, otherwise you only get sound out of the left ear.
'''

term = 'good'
b= re.search(term, text) # search method will go over all lines of text and report the first occurence
print(b, b.group())

term = 'head.'
b = re.findall(term, text)
print(b)

print(re.findall(r'\bon ?\b', text))