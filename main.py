import asyncio
import dataclasses
import datetime

from pyrogram import Client

api_id = ""
api_hash = ""


@dataclasses.dataclass()
class FromDay:
    YEAR = 2023
    MONTH = 1
    DAY = 1


@dataclasses.dataclass()
class ToDay:
    YEAR = 2023
    MONTH = 4
    DAY = 1


async def printPosts(printf, app, group,
                     fromDay=datetime.datetime(year=FromDay.YEAR, month=FromDay.MONTH, day=FromDay.DAY),
                     toDay=datetime.datetime(year=ToDay.YEAR, month=ToDay.MONTH, day=ToDay.DAY)):
    async for message in app.get_chat_history(group, offset_date=toDay):
        printf(message.date.strftime("%d %B %Y %H:%M"))
        if message.date <= fromDay:
            break


async def getPosts(app, group):
    with open("posts.txt", "w") as file:
        def writeToFile(text):
            file.write(text + '\n')
        await printPosts(printf=writeToFile, app=app, group=group)


async def main():
    app = Client("gayAccount", api_id=api_id, api_hash=api_hash)
    group = input("Enter group")
    await app.start()
    await getPosts(app, group)
    await app.stop()


if __name__ == '__main__':
    asyncio.run(main())
