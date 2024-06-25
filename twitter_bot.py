import os
import time
import random
from dotenv import load_dotenv
from openai import OpenAI
import tweepy

# .env dosyasındaki değişkenleri yükle
load_dotenv()

# OpenAI API anahtarını ayarla
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Twitter API anahtarlarını ayarla
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Twitter API ile bağlantı kurma
twitter_client = tweepy.Client(bearer_token=bearer_token, 
                               consumer_key=consumer_key, 
                               consumer_secret=consumer_secret, 
                               access_token=access_token, 
                               access_token_secret=access_token_secret)

# Rastgele bir prompt seçimi
def select_random_prompt():
    prompts = [
        "Bir Fenerbahçe taraftarı gibi kısa bir tweet at: Fenerbahçe başkanı ali koça güvendiğini ve fenerbahçe teknik direktörü mourinhoyu öven sözler söyle, mourinhonun başarılarından bahsedebilirsin",
        "Fenerbahçe taraftarı olarak fenerbahçe tarihindeki bir başarıdan ya da bir rekordan övünerek kısa bir tweet at:",
        "Galatasarayın TFF ve hakemler tarafından desteklendiğini ifade eden ve doğru karar veremeyen hakemlerin türk futboluna zarar verdiğini anlatan kısa bir tweet at:",
        "Fenerbahçe taraftarı olarak livakovicin ne kadar iyi kaleci olduğunu veya senin onu ne kadar sevdiğini anlatan kısa bir tweet at:",
        "Fenerbahçe taraftarı olarak dusan tadicin ne kadar iyi olduğunu veya senin onu ne kadar sevdiğini anlatan kısa bir tweet at:",
        "Fenerbahçe taraftarı olarak ferdinin ne kadar iyi olduğunu veya senin onu ne kadar sevdiğini veya avrupanın en büyük kulüplerinin onu transfer etmeyi ne kadar istediğini anlatan kısa bir tweet at:",
        "Fenerbahçe taraftarı olarak fredin ne kadar iyi olduğunu veya senin onu ne kadar sevdiğini veya brezilyanın en büyük orta saha oyuncularından olduğunu veya türkiyede oynayan en iyi oyuncu olduğunu veya sana appiahı hatırlattığını anlatan kısa bir tweet at:",
        "Fenerbahçe taraftarı olarak ismail yüksekin'in ne kadar iyi olduğunu veya senin onu ne kadar sevdiğini veya avrupanın en büyük kulüplerinin onu transfer etmeyi ne kadar istediğini anlatan kısa bir tweet at:",
        "Fenerbahçe taraftarı olarak galatasarayın kadrosunda sorunlu isimlerin olduğunu bazı oyuncuların çok formsuz olduğunu ziyech, ndombili gibi isimlerin katkı sağlayacağını düşünmediğini anlatan kısa bir tweet at:",
        "Fenerbahçe taraftarı olarak galatasaraylı icardinin eski günlerinden çok uzak olduğunu, türkiyede çok iyi idman yapamadığını anlatan kısa bir tweet at:",
        "Fenerbahçe taraftarı olarak galatasarayın batshuayiyi isteme sebebinin icardiye güvenmemesi olduğunu anlatan kısa bir tweet at:",
        "Fenerbahçe taraftarı olarak arda gülerin türkiyede yetişmiş en büyük oyuncu olduğunu ve fenerbahçenin bunun için verdiği büyük emeği anlatan kısa bir tweet at:"
    ]
    return random.choice(prompts)

# ChatGPT kullanarak rastgele seçilen prompta göre tweet oluşturma
def generate_tweet():
    prompt = select_random_prompt()
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sen Fenerbahçe taraftarı gibi tweet atan bir asistansın."},
            {"role": "user", "content": prompt+ " sadece tweeti ve hashtaglari yaz başka hiçbir şey yazma."}
        ]
    )

    tweet_text = response.choices[0].message.content.strip()
    if len(tweet_text) > 280:
        tweet_text = tweet_text[:277] + "..."
    return tweet_text

# Rastgele bir zaman diliminde tweet atma
# Tweet atma
def tweet():
    try:
        tweet_text = generate_tweet()
        response = twitter_client.create_tweet(text=tweet_text)
        print(f"Tweet atıldı! Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"Tweet atılırken hata oluştu: {e}")

# Rastgele zaman diliminde tweet atma fonksiyonunu çağır
tweet()