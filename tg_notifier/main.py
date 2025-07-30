import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message

from faststream.rabbit import RabbitBroker


TOKEN = "ВАШТОКЕНЗДЕСЬ"


dp = Dispatcher()
bot = Bot(token=TOKEN)

broker = RabbitBroker()


@broker.subscriber("orders")
async def handle_orders_and_send_message(data: str):
    await bot.send_message(
        chat_id=652261821,
        text=data,
    )

#
# @dp.message()
# async def handle_msg(msg: Message):
#     await msg.answer(f"Ваш chat_id: {msg.chat.id}")


async def main() -> None:
    async with broker:
        await broker.start()
        logging.info("Брокер стартовал")
        await dp.start_polling(bot)
    logging.info("Все закончилось...")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
