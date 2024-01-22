from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random
import string

class WordGuessingApp(App):
    stages = [
        '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|\  |
         /   |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        '''
    ]

    def build(self):
        self.chosen_word = random.choice(word_list)
        self.word_length = len(self.chosen_word)
        self.display = ["_"] * self.word_length
        self.lives = 6
        self.current_stage = 0

        main_layout = BoxLayout(orientation='vertical', spacing=10)

        # BoxLayout for word-related components
        word_layout = BoxLayout(orientation='vertical', spacing=10)

        self.word_label = Label(text=' '.join(self.display), font_size=48)
        self.input_box = TextInput(hint_text="Hádej písmeno", font_size=48, multiline=False)
        self.input_box.bind(on_text_validate=self.check_guess)

        word_layout.add_widget(self.word_label)
        word_layout.add_widget(self.input_box)

        # BoxLayout for info_label
        info_layout = BoxLayout(orientation='vertical', spacing=10)
        self.info_label = Label(text='', font_size=30)
        info_layout.add_widget(self.info_label)

        # Add the word_layout and info_layout to the main_layout
        main_layout.add_widget(word_layout)
        main_layout.add_widget(info_layout)

        return main_layout

    def check_guess(self, instance):
        guess = instance.text.lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            self.info_label.text = "Hádej písmeno."
            instance.text = ""
            return

        if guess in self.display:
            self.info_label.text = f"\nUž jsi uhodl '{guess}'."
        elif guess in self.chosen_word:
            for position in range(self.word_length):
                letter = self.chosen_word[position]
                if letter == guess:
                    self.display[position] = letter
            self.info_label.text = ""
        else:
            self.lives -= 1
            self.info_label.text = f"\nHádal jsi '{guess}',což není písmeno ve slovu. \nMáš {self.lives} životů."
            self.current_stage += 1

        if self.lives == 0:
            self.info_label.text = f"Prohrál jsi! slovo bylo {self.chosen_word}"
            self.input_box.disabled = True
        elif "_" not in self.display:
            self.info_label.text = "Vyhrál jsi!"
            self.input_box.disabled = True
        elif self.current_stage < len(self.stages):
            self.info_label.text += self.stages[self.current_stage]

        self.word_label.text = ' '.join(self.display)
        instance.text = ""


word_list = [
    'kolo',
    'auto',
    'mobil',
    'stroj',
    'kvetinac',
    'kufor',
    'pero',
    'sklo',
    'karta',
    'traktor',
    'vitr',
    'kamen',
    'stan',
    'hranol',
    'list',
    'klic',
    'cihla',
    'most',
    'raketoplan',
    'prilba',
    'dum',
    'drak',
    'mrak',
    'klic',
    'krab',
    'slon',
    'krabice',
    'housle',
    'balon',
    'pocitac',
    'tank',
    'raketa',
    'parnik',
    'hrnicek',
    'zidle',
    'strom',
    'pingpongovy micek',
    'tenisova raketa',
    'vlak',
    'plachta',
    'sirka',
    'svicka',
    'destnik',
    'klapka',
    'trubka',
    'vodnik',
    'sykorka',
    'trenyrky',
    'lupa',
    'klubko',
    'banka',
    'karty',
    'cepice',
    'rukavice',
    'kolik',
    'orech',
    'klobouk',
    'baterka',
    'hracka',
    'diamant',
    'kometa',
    'cokolada',
    'gulas',
    'vystraha',
    'vzpominka',
    'sluchatko',
    'cas',
    'kridlo',
    'mys',
    'staveni',
    'nozik',
    'papir',
    'guma',
    'kostka',
    'zirafa',
    'boty',
    'klin',
    'svetr',
    'maska',
    'cil',
    'kolo',
    'peri',
    'oblak',
    'cesta',
    'plaz',
    'pocitac',
    'mobil',
    'ruze',
    'plamen',
    'okno',
    'dvere',
    'slunecnice',
    'pernik',
    'prsten',
    'darek',
    'casopis',
    'bublina',
    'klavesnice',
    'tabule',
    'kava',
    'hrnicek',
    'domek',
    'sukne',
    'cepice',
    'bryle',
    'kavovar',
    'polstar',
    'traktor',
    'zarovka',
    'carodej',
    'raketa',
    'cokolada',
    'kolo',
    'postel',
    'hudba',
    'zidle',
    'skala',
    'koberec',
    'ptak',
    'svetlo',
    'sklenice',
    'klic',
    'svicen',
    'plachta',
    'kloub',
    'banka',
    'vez',
    'plakat',
    'strom',
    'vitr',
    'klapka',
    'tank',
    'most',
    'ram',
    'ton',
    'kometa',
    'plavky',
    'zralok',
    'nozky',
    'socha',
    'syr',
    'zaba',
    'kresba',
    'vitrina',
    'houska',
    'gril',
    'dvur',
    'horko',
    'tisk',
    'truhla',
    'vino',
    'slon',
    'kladivo',
    'staveni',
    'boty',
    'kava',
    'svicka',
    'trouba',
    'krab',
    'kniha',
    'radio',
    'housle',
    'klubko',
    'sirka',
    'cervena ruze',
    'klavir',
    'destnik',
    'mys',
    'cepice',
    'dum',
    'kamera',
    'svetr',
    'tanec',
    'peri',
    'caj',
    'botnik',
    'oblak',
    'klic',
    'skala',
    'kostka',
    'trh',
    'bryle',
    'obraz',
    'plamen',
    'sklenka',
    'kohout',
    'prsten',
    'cajovna',
    'balon',
    'deka',
    'trava',
    'kloub',
    'koberec',
    'klapka',
    'pyramida',
    'panenka',
    'orech',
    'sacek',
    'mapa',
    'mobil',
    'stitek',
    'klubko',
    'boty',
    'kava',
    'kostka',
    'trikot',
    'skala',
    'plamen',
    'zarovka',
    'slunce',
    'casopis',
    'klavesnice',
    'polstar',
    'zidle',
    'zehlicka',
    'kabelka',
    'svicen',
    'kavovar',
    'kbelik',
    'zaba',
    'truhla',
    'pilulka',
    'hory',
    'klin',
    'praminek',
    'sklenka',
    'capka',
    'svetr',
    'trenyrky',
    'zebrik',
    'cokolada',
    'koupelna',
    'klobouk',
    'cesta',
    'zehlicka',
    'kapesnik',
    'plaz',
    'zidle',
    'houska',
    'staveni',
    'socha',
    'plachta',
    'plamen',
    'staveni',
    'botnik',
    'hudba',
    'naramenice'
]


if __name__ == '__main__':
    WordGuessingApp().run()