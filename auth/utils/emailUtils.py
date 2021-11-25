import smtplib
from email.mime.text import MIMEText
from dojot.module import Log

import conf

LOGGER = Log().color_log()


def send_mail(to, subject, html_msg):
    if conf.emailHost == 'NOEMAIL':
        return

    LOGGER.info("Starting service of sending email")

    # TODO: I think we should put this function in a worker thread
    msg = MIMEText(html_msg, 'html')

    msg['Subject'] = subject
    msg['From'] = conf.emailUsername
    msg['To'] = to

    try:
        s = smtplib.SMTP(conf.emailHost, conf.emailPort)
        if conf.emailTLS and conf.emailServerAuth:
            s.starttls()
        if conf.emailServerAuth:
            s.login(msg['From'], conf.emailPasswd)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        s.quit()
    except OSError as error:
        LOGGER.error(error)
        raise Exception('Failed to retrieve SMTP socket. Is the SMTP port closed?')
    except smtplib.SMTPAuthenticationError:
        raise Exception('SMTP authentication failed')
    except Exception as e:
        raise Exception(e)
