from functools import lru_cache

from opwen_email_server import config
from opwen_email_server.constants import azure as constants
from opwen_email_server.services.auth import AzureAuth
from opwen_email_server.services.sendgrid import SendgridEmailSender
from opwen_email_server.services.storage import AzureFileStorage
from opwen_email_server.services.storage import AzureObjectStorage
from opwen_email_server.services.storage import AzureObjectsStorage
from opwen_email_server.services.storage import AzureTextStorage


@lru_cache(maxsize=1)
def get_auth() -> AzureAuth:
    return AzureAuth(
        storage=AzureTextStorage(
            account=config.TABLES_ACCOUNT,
            key=config.TABLES_KEY,
            container=constants.TABLE_AUTH,
            provider=config.STORAGE_PROVIDER))


@lru_cache(maxsize=1)
def get_client_storage() -> AzureObjectsStorage:
    return AzureObjectsStorage(
        file_storage=AzureFileStorage(
            account=config.CLIENT_STORAGE_ACCOUNT,
            key=config.CLIENT_STORAGE_KEY,
            container=constants.CONTAINER_CLIENT_PACKAGES,
            provider=config.STORAGE_PROVIDER))


@lru_cache(maxsize=1)
def get_raw_email_storage() -> AzureTextStorage:
    return AzureTextStorage(
        account=config.BLOBS_ACCOUNT,
        key=config.BLOBS_KEY,
        container=constants.CONTAINER_SENDGRID_MIME,
        provider=config.STORAGE_PROVIDER)


@lru_cache(maxsize=1)
def get_email_sender() -> SendgridEmailSender:
    return SendgridEmailSender(
        key=config.EMAIL_SENDER_KEY)


@lru_cache(maxsize=1)
def get_email_storage() -> AzureObjectStorage:
    return AzureObjectStorage(
        text_storage=AzureTextStorage(
            account=config.BLOBS_ACCOUNT,
            key=config.BLOBS_KEY,
            container=constants.CONTAINER_EMAILS,
            provider=config.STORAGE_PROVIDER))


@lru_cache(maxsize=128)
def get_pending_storage(domain: str) -> AzureTextStorage:
    return AzureTextStorage(
        account=config.TABLES_ACCOUNT,
        key=config.TABLES_KEY,
        container=domain,
        provider=config.STORAGE_PROVIDER)
