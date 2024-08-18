from deep_translator import GoogleTranslator
codes = {
    'english': 'en',
    'persian': 'fa',
    'french': 'fr',
    'germany': 'de',
    'spanish': 'es',
    'italian': 'it',
    'russian': 'ru',
    'arrabic': 'ar',
}
print ('wellcome to translator\n')
while True:
    text = input("enter text to translate: ")
    TargetLanguage = input("enter the language that you want to translate to : ").strip()
    if TargetLanguage in codes:
        TargetLanguageCode = codes[TargetLanguage]
        break
    else:
        print("somethimthing went wrong please try again")
try:
    TranslatedText = GoogleTranslator(source='auto', target=TargetLanguageCode).translate(text)
    print(f"translating : {TranslatedText}")
except Exception as e:
    print(f"you got this error: {e}")