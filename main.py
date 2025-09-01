import os
from ninjemail import Ninjemail

def main():
    # إعداد المفاتيح من environment variables
    captcha_keys = {}
    if os.getenv('CAPSOLVER_API_KEY'):
        captcha_keys['capsolver'] = os.getenv('CAPSOLVER_API_KEY')
    if os.getenv('NOPECHA_API_KEY'):
        captcha_keys['nopecha'] = os.getenv('NOPECHA_API_KEY')
    
    sms_keys = {}
    if os.getenv('SMS_USERNAME') and os.getenv('SMS_TOKEN'):
        sms_keys['getsmscode'] = {
            'user': os.getenv('SMS_USERNAME'),
            'token': os.getenv('SMS_TOKEN')
        }
    
    # إنشاء instance من Ninjemail
    ninja = Ninjemail(
        browser="firefox",  # أو "chrome" أو "undetected-chrome"
        captcha_keys=captcha_keys,
        sms_keys=sms_keys,
        auto_proxy=True  # استخدام free proxies تلقائياً
    )
    
    try:
        # إنشاء حساب Gmail
        email, password = ninja.create_gmail_account()
        print(f"Gmail Account Created: {email}")
        print(f"Password: {password}")
        
        # إنشاء حساب Outlook
        email2, password2 = ninja.create_outlook_account()
        print(f"Outlook Account Created: {email2}")
        print(f"Password: {password2}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
