from os import environ

CONTAINER_CLIENT_PACKAGES = 'compressedpackages'
CONTAINER_EMAILS = 'emails'
CONTAINER_SENDGRID_MIME = 'sendgridinboundemails'
TABLE_DOMAIN = 'emaildomain'
TABLE_TO = 'emailto'
TABLE_CC = 'emailcc'
TABLE_BCC = 'emailbcc'
TABLE_FROM = 'emailfrom'
TABLE_DOMAIN_X_DELIVERED = 'emaildomainxdelivered'
TABLE_AUTH = 'clientsauth'
QUEUE_CLIENT_PACKAGE = 'lokoleinboundemails'
QUEUE_EMAIL_SEND = 'sengridoutboundemails'
QUEUE_SENDGRID_MIME = 'sengridinboundemails'
QUEUE_POLL_INTERVAL = float(environ.get('LOKOLE_QUEUE_POLL_SECONDS', '10'))