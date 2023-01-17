import os
homeDir = (r'\\').join(os.path.abspath(__file__).split('\\')[:-1])

admin_list = [1021524873, 828458879]
BOT_TOKEN = '5953176557:AAELkYdMdTWoR_2LZ74sisqCtaOFyVtLM64' #@Test_Products111_bot
db_path = f'{homeDir}\\db.db'

products = {
    'молоко':[
            'дом',
            'дом2']
    ,
    'сыр':[
            'дом3',
            'дом4'
    ],

}