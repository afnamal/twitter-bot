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
        "Galatasarayın TFF ve hakemler tarafından desteklendiğini ifade eden ve doğru karar veremeyen hakemlerin türk futboluna zarar verdiğini anlatan kısa bir tweet at:"
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
def tweet_at_random_time():
    while True:
        # 30 ile 60 dakika arasında rastgele bir zaman dilimi (saniye cinsinden)
        wait_time = random.randint(1800, 3600)
        print(f"{wait_time} saniye bekleniyor...")

        # Belirlenen zaman dilimini bekle
        time.sleep(wait_time)

        # Tweet atma
        try:
            tweet_text = generate_tweet()
            response = twitter_client.create_tweet(text=tweet_text)
            print(f"Tweet atıldı! Tweet ID: {response.data['id']}")
        except Exception as e:
            print(f"Tweet atılırken hata oluştu: {e}")
# Rastgele zaman diliminde tweet atma fonksiyonunu çağır
tweet_at_random_time()
