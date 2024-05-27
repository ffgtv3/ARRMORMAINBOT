import discord
from discord.ext import commands

# Замените "YOUR_BOT_TOKEN" на ваш токен бота Discord
TOKEN = 'MTI0NDYyMzU3NDE2MjIxMDgyNw.GZcA7_.PmPlA6i2rl8MeGL3j7Bngh23_V2yo820vZexHQ'

# Замените "CATEGORY_ID" на ID категории, которую вы хотите проверять
CATEGORY_ID = 1244605060474863689

# Замените "ADMIN_USER_ID" на ID пользователя-администратора, которому будут отправляться сообщения
ADMIN_USER_ID = 881964256277459025

# Создаем экземпляр бота
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

# Событие, которое срабатывает при создании нового канала
@bot.event
async def on_guild_channel_create(channel):
    # Проверяем, является ли канал текстовым каналом
    if isinstance(channel, discord.TextChannel):
        # Проверяем, находится ли канал в нужной категории
        if channel.category_id == CATEGORY_ID:
            # Получаем информацию о создателе канала
            creator = channel.created_by
            # Отправляем сообщение администратору в личные сообщения
            admin = await bot.fetch_user(ADMIN_USER_ID)
            await admin.send(f'Канал "{channel.name}" был создан пользователем {creator.mention} в категории "{channel.category.name}"')

# Событие, которое срабатывает при удалении канала
@bot.event
async def on_guild_channel_delete(channel):
    # Проверяем, находился ли канал в нужной категории
    if channel.category_id == CATEGORY_ID:
        # Отправляем сообщение администратору в личные сообщения
        admin = await bot.fetch_user(ADMIN_USER_ID)
        await admin.send(f'Канал "{channel.name}" был удален из категории "{channel.category.name}"')

# Запуск бота
bot.run(TOKEN)
