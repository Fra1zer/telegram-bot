
welcome_message = "Привет! Пройди анкету и узнай свой тип мышления!"

questions = [
    ("Как вы относитесь к проблемам?",
     [("Боюсь проблем", {"growth mindset": 0, "fixed mindset": 1}),
      ("Принимаю проблемы", {"growth mindset": 1, "fixed mindset": 0}),
      ]),
    ("Как вы относитесь к своим недостаткам?",
     [("Принимаю их, не пытаюсь скрывать", {"growth mindset": 1, "fixed mindset": 0}),
      ("Пытаюсь скрыть их", {"growth mindset": 0, "fixed mindset": 1}),
      ]),
    ("Как вы относитесь к ошибкам?",
     [("Ошибки - двигателей прогресса", {"growth mindset": 1, "fixed mindset": 0}),
      ("Ошибки - что-то плохое, чего нужно избегать", {"growth mindset": 0, "fixed mindset": 1}),
      ]),
    ("Как вы относитесь к возможностям?",
     [("Пользуюсь ими, возможности - метод роста", {"growth mindset": 1, "fixed mindset": 0}),
      ("Избегаю новизну в своей жизни", {"growth mindset": 0, "fixed mindset": 1}),
      ]),
    ("Как вы оцениваете свои способности ?",
     [("При должном упорстве я способен на всё !", {"growth mindset": 1, "fixed mindset": 0}),
      ("Я способен лишь тому, чему меня научили в школе/университете", {"growth mindset": 0, "fixed mindset": 1}),
      ]),
]

characters = {
    "growth mindset": ("Бро, ты гигичад обладающий мышлением роста", "images/гигачад.png"),
    "fixed mindset": ("Бро... ты омежка обладающий фиксированным мышлением", "images/омежка.png"),
}
