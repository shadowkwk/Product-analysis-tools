##The product is Gaming Headset for PS4 PS5 Xbox One Switch PC with Noise Canceling Mic, Deep Bass Stereo Sound
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
##text = "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
text="My son is in love!!! These headphones are just the perfect thing for my teenage son!!!! He uses them for a few different things…including school work while he’s at home! But he mainly uses them for his GAMING ADDICTION!!! HELP!!! These have really great sound quality!!!"
text1="In conclusion, I love the sound effect and the shining(on both sides) will I turn it on :) During the game, my teammates could hear me clearly, that's good. The sound effect is great and I love wearing it to watch movies."
text2="The gaming headset is so far durable, my dog chews the cord and they still work."
text3="The sound is clear, he is able to hear and be heard by others with no issue. He loves the look of it very cool. It transitions from gaming to movies effortlessly and he can use it both with his XBOX and his tablet with no issue. Highly recommend if you are looking for great quality at a great price. 10/10."
text4="I bought these for my son for Christmas and let him use them for a little while before asking him how he likes them. He's very pleased. He said he especially likes how you can hear the sounds separately in each ear when gaming so you can tell where people or things are."
text5="For each players, a good gaming headset is essential. What kind of headset we choose depends on what game we play. For example, if we are playing a game of PUBG type that we need enough surround sound to know where the enemy is at all times, and this gaming headset can well meet our needs."
text6="My son's last gaming headset microphone broke. So I chose to buy this headset after reading the reviews. I waited about a month to make this review, so that I can give an accurate and honest one. My son is a game player and a live streamer. He said this headset are equivalent to or even better than the more expensive nearly $100 headset he used before. This headset is relatively light, and there will be no falling feeling when it is hung on the ear."
text7="I'm very happy with these. Lightweight, comfortable and sound is very good for gaming."
text8="I've purchased three pairs of this same headphone over the last 5 years. Two for use by us and the third as a gift for an Angle Tree gift. These are a solid option for a gaming headset at an affordable price. The audio quality has been good enough for both music and gaming where direction sound is important (think shooters)."
text9="3.5mm jack is defective, I tried it on a couple of device and if you hold it just right you get sound out of both ears, otherwise you only get sound out of the left ear."
text = text.lower()
text1 = text1.lower()
text2 = text2.lower()
text3 = text3.lower()
text4 = text4.lower()
text5 = text5.lower()
text6 = text6.lower()
text7 = text7.lower()
text8 = text8.lower()
text9 = text9.lower()

#print(text)

import string
#print(string.punctuation)

text_p = "".join([char for char in text if char not in string.punctuation])
text_p1 = "".join([char for char in text1 if char not in string.punctuation])
text_p2 = "".join([char for char in text2 if char not in string.punctuation])
text_p3 = "".join([char for char in text3 if char not in string.punctuation])
text_p4 = "".join([char for char in text4 if char not in string.punctuation])
text_p5 = "".join([char for char in text5 if char not in string.punctuation])
text_p6 = "".join([char for char in text6 if char not in string.punctuation])
text_p7 = "".join([char for char in text7 if char not in string.punctuation])
text_p8 = "".join([char for char in text8 if char not in string.punctuation])
text_p9 = "".join([char for char in text9 if char not in string.punctuation])

from nltk import word_tokenize
words = word_tokenize(text_p)
words1 = word_tokenize(text_p1)
words2 = word_tokenize(text_p2)
words3 = word_tokenize(text_p3)
words4 = word_tokenize(text_p4)
words5 = word_tokenize(text_p5)
words6 = word_tokenize(text_p6)
words7 = word_tokenize(text_p7)
words8 = word_tokenize(text_p8)
words9 = word_tokenize(text_p9)


from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words1 = stopwords.words('english')
stop_words2 = stopwords.words('english')
stop_words3 = stopwords.words('english')
stop_words4 = stopwords.words('english')
stop_words5 = stopwords.words('english')
stop_words6 = stopwords.words('english')
stop_words7 = stopwords.words('english')
stop_words8 = stopwords.words('english')
stop_words9 = stopwords.words('english')
## print(stop_words)

filtered_words = [word for word in words if word not in stop_words]
filtered_words1 = [word for word in words1 if word not in stop_words1]
filtered_words2 = [word for word in words2 if word not in stop_words2]
filtered_words3 = [word for word in words3 if word not in stop_words3]
filtered_words4 = [word for word in words4 if word not in stop_words4]
filtered_words5 = [word for word in words5 if word not in stop_words5]
filtered_words6 = [word for word in words6 if word not in stop_words6]
filtered_words7 = [word for word in words7 if word not in stop_words7]
filtered_words8 = [word for word in words8 if word not in stop_words8]
filtered_words9 = [word for word in words9 if word not in stop_words9]

#print(filtered_words)

from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in filtered_words]
stemmed1 = [porter.stem(word) for word in filtered_words1]
stemmed2= [porter.stem(word) for word in filtered_words2]
stemmed3 = [porter.stem(word) for word in filtered_words3]
stemmed4 = [porter.stem(word) for word in filtered_words4]
stemmed5 = [porter.stem(word) for word in filtered_words5]
stemmed6 = [porter.stem(word) for word in filtered_words6]
stemmed7 = [porter.stem(word) for word in filtered_words7]
stemmed8 = [porter.stem(word) for word in filtered_words8]
stemmed9 = [porter.stem(word) for word in filtered_words9]


print(stemmed)
print(stemmed1)
print(stemmed2)
print(stemmed3)
print(stemmed4)
print(stemmed5)
print(stemmed6)
print(stemmed7)
print(stemmed8)
print(stemmed9)



from nltk import pos_tag
pos = pos_tag(filtered_words)
#print(pos)