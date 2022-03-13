import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION_LT='2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """Translates the text to french"""
    try:
        translation_response = language_translator.translate(\
         text=english_text, model_id='en-fr')
        translation=translation_response.get_result()
        french_text=translation['translations'][0]['translation'] 
    except:
        french_text='The input is empty'    
    return french_text

def french_to_english(french_text):
    """Translates the text to english"""
    try:
        translation_response = language_translator.translate(\
        text=french_text, model_id='fr-en')
        translation=translation_response.get_result()
        english_text =translation['translations'][0]['translation'] 
    except:
        english_text='The input is empty' 
    return english_text
