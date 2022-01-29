"""
This code is for language translation
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('In-fbA4WYy1IE_4MNmT95BufsDrBRSXjho8BediZXoxi')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.\
    cloud.ibm.com/instances/18544d7e-4c7d-4fd9-9027-9eb7c426e677')

def english_to_french(english_text):
    """
    This function returns french translation
    """
    #write the code here
    french_text = language_translator.translate(
        text = english_text,
        model_id='en-fr'
    ).get_result()
    french_text = english_text['translations'][0]['translation']
    return json.dumps(french_text, indent=2, ensure_ascii=False)

def french_to_english(french_text):
    """
    This function returns english translation
    """
    #write the code here
    english_text = language_translator.translate(
        text = french_text,
        model_id='fr-en'
    ).get_result()
    english_text = french_text['translations'][0]['translation']
    return json.dumps(english_text, indent=2, ensure_ascii=False)
