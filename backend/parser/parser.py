from datetime import datetime
from parser.models import News, Tag

from asgiref.sync import sync_to_async
from django.db import IntegrityError
from news.settings import API_HASH, API_ID
from telethon.sync import TelegramClient


@sync_to_async
def save_news(title: str, text: str, link: str, pub_date: datetime, tag: Tag) -> None:
    News.objects.create(
        title=title,
        text=text,
        link=link,
        pub_date=pub_date,
        tags=tag,
    )


async def telegram_parser(tag: Tag, count: int = 0) -> None:
    """
    Парсит последние 10 постов и записывает их в бд если их нет.
    При первом запуске запросит номер телефона и код из телеграмма.
    """
    async with TelegramClient('parser', API_ID, API_HASH) as client:
        async for message in client.iter_messages(tag.link):
            if message.text:
                if count > 9:
                    break
                count += 1
                text = message.text.split('\n', 1)

                try:
                    await save_news(
                        title=text[0],
                        text=text[1],
                        link=f'{tag.link}/{message.id}',
                        pub_date=message.date,
                        tag=tag,
                    )
                except IntegrityError:
                    continue
