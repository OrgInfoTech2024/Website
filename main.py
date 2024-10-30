from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from language import langDict
import sys
import os
import time
import pyautogui

class MediaCenter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Center")
        self.resize(800, 600)
        self.setStyleSheet("background-color: black;")
        self.setWindowIcon(QIcon('images/icon/icon.png'))
        
        
        # LANGUAGE
        
        self.lang = langDict
        self.syslang = QLocale.system().name()
        if self.syslang not in self.lang:
            self.syslang = "en_US"
            
            
            
            

        self.display_width, self.display_height = pyautogui.size()

        # "STARTUP" SOUND
        self.startup_sound = QMediaPlayer()
        sound_path = os.path.abspath("sounds/startup.mp3")
        self.startup_sound.setMedia(QMediaContent(QUrl.fromLocalFile(sound_path)))

        # SPLASH SCREEN
        self.splash_movie = QMovie('images/animations/splash.gif')
        self.splash_label = QLabel(self)
        self.splash_label.setMovie(self.splash_movie)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.showFullScreen()
        layout = QVBoxLayout()
        layout.addWidget(self.splash_label, alignment=Qt.AlignCenter)
        container = QWidget(self)
        container.setLayout(layout)
        container.setStyleSheet('background-color: black')
        self.setLayout(layout)
        self.timer = QTimer()
        self.splash_label.hide()
        
        # "MAIN" PAGE
        
        # "HOME" BUTTON
        self.home_button = QPushButton(self)
        self.home_button.setIcon(QIcon('images/buttons/back-to-home.png'))
        self.home_button.setIconSize(QSize(45, 45))
        self.home_button.setGeometry(5, 5, 45, 45)
        self.home_button.setStyleSheet('border-radius: 5px')
        self.home_button.enterEvent = self.select_home_button
        self.home_button.leaveEvent = self.reset_home_button
        self.home_button.clicked.connect(self.goHome)
        self.home_button.hide()
        
        # "MINIMAZE" BUTTON
        self.minimaze_button = QPushButton(self)
        self.minimaze_button.setIcon(QIcon('images/buttons/hide.png'))
        self.minimaze_button.setIconSize(QSize(45, 45))
        minimaze_button_from_width_end = self.display_width - 100
        self.minimaze_button.setGeometry(minimaze_button_from_width_end, 5, 45, 45)
        self.minimaze_button.setStyleSheet('border-radius: 5px')
        self.minimaze_button.enterEvent = self.select_minimaze_button
        self.minimaze_button.leaveEvent = self.reset_minimaze_button
        self.minimaze_button.clicked.connect(self.minimaze_window)
        self.minimaze_button.hide()
        
        # "EXIT" BUTTON
        self.exit_button = QPushButton(self)
        self.exit_button.setIcon(QIcon('images/buttons/exit.png'))
        self.exit_button.setIconSize(QSize(45, 45))
        exit_button_from_width_end = self.display_width - 50
        self.exit_button.setGeometry(exit_button_from_width_end, 5, 45, 45)
        self.exit_button.setStyleSheet('border-radius: 5px')
        self.exit_button.enterEvent = self.select_exit_button
        self.exit_button.leaveEvent = self.reset_exit_button
        self.exit_button.clicked.connect(self.exit)
        self.exit_button.hide()
        
        
        # "HOME" PAGE
        
        # "FAVORITES" BUTTON
        self.favorite_button = QPushButton(self)
        self.favorite_button.setIcon(QIcon('images/buttons/favorities.png'))
        self.favorite_button.setIconSize(QSize(140, 90))
        self.favorite_button.setGeometry(5, 60, 150, 100)
        self.favorite_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.favorite_button.enterEvent = self.select_favorite_button
        self.favorite_button.leaveEvent = self.reset_favorite_button
        self.favorite_button.clicked.connect(self.favorites_page)
        self.favorite_button.hide()
                
        # "PLAYER" BUTTON
        self.player_button = QPushButton(self)
        self.player_button.setIcon(QIcon('images/buttons/player.png'))
        self.player_button.setIconSize(QSize(140, 90))
        self.player_button.setGeometry(160, 60, 150, 100)
        self.player_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.player_button.enterEvent = self.select_player_button
        self.player_button.leaveEvent = self.reset_player_button
        self.player_button.clicked.connect(self.player_page)
        self.player_button.hide()
                
        # "RADIO" BUTTON
        self.radio_button = QPushButton(self)
        self.radio_button.setIcon(QIcon('images/buttons/radio.png'))
        self.radio_button.setIconSize(QSize(140, 90))
        self.radio_button.setGeometry(315, 60, 150, 100)
        self.radio_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.radio_button.enterEvent = self.select_radio_button
        self.radio_button.leaveEvent = self.reset_radio_button
        self.radio_button.clicked.connect(self.radio_page)
        self.radio_button.hide()
                
        # "TV" BUTTON
        self.tv_button = QPushButton(self)
        self.tv_button.setIcon(QIcon('images/buttons/tv.png'))
        self.tv_button.setIconSize(QSize(140, 90))
        self.tv_button.setGeometry(470, 60, 150, 100)
        self.tv_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.tv_button.enterEvent = self.select_tv_button
        self.tv_button.leaveEvent = self.reset_tv_button
        self.tv_button.clicked.connect(self.tv_page)
        self.tv_button.hide()
        
        
        # "FAVORITES" PAGE
        
        self.favorites_list = []
        try:
            home_directory = os.path.expanduser("~")
            file_path = os.path.join(home_directory, '.programdates', 'favorites_media.txt')
            with open(file_path, 'r') as f:
                self.favorites_list = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            pass

        # "ADD" BUTTON
        self.add_favorites_button = QPushButton(self.lang[self.syslang]["Add"], self)
        self.add_favorites_button.setGeometry(5, 60, 70, 30)
        self.add_favorites_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.add_favorites_button.enterEvent = self.select_add_favorites_button
        self.add_favorites_button.leaveEvent = self.reset_add_favorites_button
        self.add_favorites_button.clicked.connect(self.add_favorites)
        self.add_favorites_button.hide()
        
        # "REMOVE" BUTTON
        self.remove_favorites_button = QPushButton(self.lang[self.syslang]["Remove"], self)
        self.remove_favorites_button.setGeometry(5, 95, 70, 30)
        self.remove_favorites_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.remove_favorites_button.enterEvent = self.select_remove_favorites_button
        self.remove_favorites_button.leaveEvent = self.reset_remove_favorites_button
        self.remove_favorites_button.clicked.connect(self.remove_favorites)
        self.remove_favorites_button.hide()
        
        # "FAVORITES" LISTBOX
        self.favorites_listbox = QListWidget(self)
        favorites_listbox_to_width_end = self.display_width - 85
        favorites_listbox_to_height_end = self.display_height - 65
        self.favorites_listbox.setGeometry(80, 60, favorites_listbox_to_width_end, favorites_listbox_to_height_end)
        self.favorites_listbox.hide()
        self.favorites_listbox.doubleClicked.connect(self.double_click_favorites)
        self.favorites_listbox.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px;')
        self.favorites_listbox.addItems(self.favorites_list)
        
        
        # "PLAYER" PAGE

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget(self)
        videoWidget_to_width_end = self.display_width - 10
        videoWidget_to_height_end = self.display_height - 160
        self.videoWidget.setGeometry(5, 60, videoWidget_to_width_end, videoWidget_to_height_end)
        self.videoWidget.hide()

        self.playerTimer = QTimer(self)
        self.playerTimer.timeout.connect(self.updatePlayerTime)

        self.openButton = QPushButton(self.lang[self.syslang]["Open"], self)
        self.openButton.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px;')
        self.openButton.enterEvent = self.select_openButton
        self.openButton.leaveEvent = self.reset_openButton
        self.openButton.clicked.connect(self.openFileFromButton)
        openButton_from_height_end = self.display_height - 90
        self.openButton.setGeometry(5, openButton_from_height_end, 55, 35)
        self.openButton.hide()

        self.playButton = QPushButton(self.lang[self.syslang]["Play"], self)
        self.playButton.setEnabled(False)
        self.playButton.clicked.connect(self.playVideo)
        self.playButton.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px;')
        self.playButton.enterEvent = self.select_playButton
        self.playButton.leaveEvent = self.reset_playButton
        playButton_from_height_end = self.display_height - 90
        self.playButton.setGeometry(65, playButton_from_height_end, 55, 35)
        self.playButton.hide()

        self.stopButton = QPushButton(self.lang[self.syslang]["Stop"], self)
        self.stopButton.clicked.connect(self.stopVideo)
        self.stopButton.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px;')
        self.stopButton.enterEvent = self.select_stopButton
        self.stopButton.leaveEvent = self.reset_stopButton
        stopButton_from_height_end = self.display_height - 90
        self.stopButton.setGeometry(125, stopButton_from_height_end, 55, 35)
        self.stopButton.hide()

        self.lastMediaButton = QPushButton("<", self)
        self.lastMediaButton.clicked.connect(self.lastMedia)
        self.lastMediaButton.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px;')
        self.lastMediaButton.enterEvent = self.select_lastMediaButton
        self.lastMediaButton.leaveEvent = self.reset_lastMediaButton
        lastMediaButton_from_height_end = self.display_height - 90
        self.lastMediaButton.setGeometry(185, lastMediaButton_from_height_end, 55, 35)
        self.lastMediaButton.hide()

        self.nextMediaButton = QPushButton(">", self)
        self.nextMediaButton.clicked.connect(self.nextMedia)
        self.nextMediaButton.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px;')
        self.nextMediaButton.enterEvent = self.select_nextMediaButton
        self.nextMediaButton.leaveEvent = self.reset_nextMediaButton
        nextMediaButton_from_height_end = self.display_height - 90
        self.nextMediaButton.setGeometry(245, nextMediaButton_from_height_end, 55, 35)
        self.nextMediaButton.hide()

        self.positionSlider = QSlider(Qt.Horizontal, self)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        positionSlider_from_height_end = self.display_height - 90
        positionSlider_to_width_height_end = self.display_width - 310
        self.positionSlider.setGeometry(305, positionSlider_from_height_end, positionSlider_to_width_height_end, 35)
        self.positionSlider.hide()

        self.currentMedia = 0
        self.folderMedia = []

        self.timeLabel = QLabel(self)
        timeLabel_from_height_end = self.display_height - 55
        self.timeLabel.setGeometry(5, timeLabel_from_height_end, 790, 20)
        self.timeLabel.setStyleSheet('color: white')
        self.timeLabel.hide()

        self.errorLabel = QLabel(self)
        errorLabel_from_height_end = self.display_height - 30
        self.errorLabel.setGeometry(5, errorLabel_from_height_end, 790, 20)
        self.errorLabel.setStyleSheet('color: white')
        self.errorLabel.hide()

        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        
        # "RADIO" PAGE

        self.radio_chanels = []
        try:
            home_directory = os.path.expanduser("~")
            file_path = os.path.join(home_directory, '.programdates', 'radio.txt')

            with open(file_path, 'r') as f:
                self.radio_chanels = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            self.radio_chanels = ['http://91.218.213.49:8000/ur1-mp3', 
                                  'http://91.218.213.49:8000/ur3-mp3', 
                                  'http://193.53.83.3:8000/fresh-fm_mp3', 
                                  'http://radio.ukr.radio:8000/ur1-rv-mp3']

        # RADIO PLAYER
        self.radio_player = QMediaPlayer()
        self.radio_player.setVolume(50)
        
        # "LINK RADIO-CHANNEL" INPUT
        self.radio_channel_input = QLineEdit(self)
        self.radio_channel_input.setGeometry(5, 60, 125, 35)
        self.radio_channel_input.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.radio_channel_input.returnPressed.connect(self.list_radio)
        self.radio_channel_input.hide()
        
        # "LIST" BUTTON
        self.list_radio_button = QPushButton(self.lang[self.syslang]["List"], self)
        self.list_radio_button.setGeometry(5, 100, 125, 35)
        self.list_radio_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.list_radio_button.enterEvent = self.select_list_radio_button
        self.list_radio_button.leaveEvent = self.reset_list_radio_button
        self.list_radio_button.clicked.connect(self.list_radio)
        self.list_radio_button.hide()
        
        # "STOP" BUTTON
        self.stop_radio_button = QPushButton(self.lang[self.syslang]["Stop"], self)
        self.stop_radio_button.setGeometry(5, 140, 125, 35)
        self.stop_radio_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.stop_radio_button.enterEvent = self.select_stop_radio_button
        self.stop_radio_button.leaveEvent = self.reset_stop_radio_button
        self.stop_radio_button.clicked.connect(self.stop_radio)
        self.stop_radio_button.hide()
        
        # "ADD" BUTTON
        self.add_radio_channel_button = QPushButton(self.lang[self.syslang]["Add"], self)
        self.add_radio_channel_button.setGeometry(5, 190, 125, 35)
        self.add_radio_channel_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.add_radio_channel_button.enterEvent = self.select_add_radio_channel_button
        self.add_radio_channel_button.leaveEvent = self.reset_add_radio_channel_button
        self.add_radio_channel_button.clicked.connect(self.add_radio_channel)
        self.add_radio_channel_button.hide()
        
        # "REMOVE" BUTTON
        self.remove_radio_channel_button = QPushButton(self.lang[self.syslang]["Remove"], self)
        self.remove_radio_channel_button.setGeometry(5, 230, 125, 35)
        self.remove_radio_channel_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
        self.remove_radio_channel_button.enterEvent = self.select_remove_radio_channel_button
        self.remove_radio_channel_button.leaveEvent = self.reset_remove_radio_channel_button
        self.remove_radio_channel_button.clicked.connect(self.remove_radio_channel)
        self.remove_radio_channel_button.hide()
        
        # "RADIO-CHANNELS" LISTBOX
        self.radio_channels_listbox = QListWidget(self)
        radio_channels_listbox_to_width_end = self.display_width - 140
        radio_channels_listbox_to_height_end = self.display_height - 65
        self.radio_channels_listbox.setGeometry(135, 60, radio_channels_listbox_to_width_end, radio_channels_listbox_to_height_end)
        self.radio_channels_listbox.hide()
        self.radio_channels_listbox.addItems(self.radio_chanels)
        self.radio_channels_listbox.doubleClicked.connect(self.double_click_radio)
        self.radio_channels_listbox.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px;')

    def select_sound_function(self):
        self.select_sound = QMediaPlayer()
        sound_path = os.path.abspath("sounds/select.mp3")
        self.select_sound.setMedia(QMediaContent(QUrl.fromLocalFile(sound_path)))
        self.select_sound.play()

    def click_sound_function(self):
        self.click_sound = QMediaPlayer()
        sound_path = os.path.abspath("sounds/click.mp3")
        self.click_sound.setMedia(QMediaContent(QUrl.fromLocalFile(sound_path)))
        self.click_sound.play()

    # "EXIT" CLICKED
    def exit(self):
        self.click_sound_function()
        time.sleep(1)
        self.close()

    # "MINIMAZE WINDOW" CLICKED
    def minimaze_window(self):
        self.click_sound_function()
        time.sleep(1)
        self.showMinimized()

    # "HOME" SELECT
    def select_home_button(self, event):
        self.select_sound_function()
        
        self.home_button.setIcon(QIcon('images/buttons-selected/back-to-home.png'))

    def reset_home_button(self, event):
        self.home_button.setIcon(QIcon('images/buttons/back-to-home.png'))

    # "HIDE WINDOW" SELECT
    def select_minimaze_button(self, event):
        self.select_sound_function()
        
        self.minimaze_button.setIcon(QIcon('images/buttons-selected/hide.png'))

    def reset_minimaze_button(self, event):
        self.minimaze_button.setIcon(QIcon('images/buttons/hide.png'))

    # "EXIT" SELECT
    def select_exit_button(self, event):
        self.select_sound_function()
        
        self.exit_button.setIcon(QIcon('images/buttons-selected/exit.png'))

    def reset_exit_button(self, event):
        self.exit_button.setIcon(QIcon('images/buttons/exit.png'))

    # "ADD FAVORITES" SELECT
    def select_add_favorites_button(self, event):
        self.select_sound_function()
        
        self.add_favorites_button.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_add_favorites_button(self, event):
        self.add_favorites_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # "PLAY BUTTON" SELECT
    def select_playButton(self, event):
        self.select_sound_function()
        
        self.playButton.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_playButton(self, event):
        self.playButton.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # "OPEN BUTTON" SELECT
    def select_openButton(self, event):
        self.select_sound_function()
        
        self.openButton.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_openButton(self, event):
        self.openButton.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # "STOP BUTTON" SELECT
    def select_stopButton(self, event):
        self.select_sound_function()
        
        self.stopButton.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_stopButton(self, event):
        self.stopButton.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # "<" SELECT
    def select_lastMediaButton(self, event):
        self.select_sound_function()
        
        self.lastMediaButton.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_lastMediaButton(self, event):
        self.lastMediaButton.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # ">" SELECT
    def select_nextMediaButton(self, event):
        self.select_sound_function()
        
        self.nextMediaButton.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_nextMediaButton(self, event):
        self.nextMediaButton.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # "REMOVE FAVORITES" SELECT
    def select_remove_favorites_button(self, event):
        self.select_sound_function()
        
        self.remove_favorites_button.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_remove_favorites_button(self, event):
        self.remove_favorites_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # "ADD RADIO-CHANNEL" SELECT
    def select_add_radio_channel_button(self, event):
        self.select_sound_function()
        
        self.add_radio_channel_button.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_add_radio_channel_button(self, event):
        self.add_radio_channel_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # "REMOVE RADIO-CHANNEL" SELECT
    def select_remove_radio_channel_button(self, event):
        self.select_sound_function()
        
        self.remove_radio_channel_button.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_remove_radio_channel_button(self, event):
        self.remove_radio_channel_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # "LIST RADIO" SELECT
    def select_list_radio_button(self, event):
        self.select_sound_function()
        
        self.list_radio_button.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_list_radio_button(self, event):
        self.list_radio_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # "STOP RADIO" SELECT
    def select_stop_radio_button(self, event):
        self.select_sound_function()
        
        self.stop_radio_button.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_stop_radio_button(self, event):
        self.stop_radio_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    # "FAVORITES" SELECT
    def select_favorite_button(self, event):
        self.select_sound_function()
        
        self.favorite_button.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')

    def reset_favorite_button(self, event):
        self.favorite_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
    
    # "PLAYER" SELECT
    def select_player_button(self, event):
        self.select_sound_function()
        
        self.player_button.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
    
    def reset_player_button(self, event):
        self.player_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
    
    # "RADIO" SELECT
    def select_radio_button(self, event):
        self.select_sound_function()
        
        self.radio_button.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
    
    def reset_radio_button(self, event):
        self.radio_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
    
    # "TV" SELECT
    def select_tv_button(self, event):
        self.select_sound_function()
        
        self.tv_button.setStyleSheet('background-color: #002387; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
    
    def reset_tv_button(self, event):
        self.tv_button.setStyleSheet('background-color: #003153; color: white; border: 2px solid white; border-radius: 5px; padding: 8px;')
    
    # "OPEN GALLERY" FUNCTION
    def open_sound_player(self):
        return
    
    # "OPEN SOUND-PLAYER" FUNCTION
    def open_sound_player(self):
        return
    
    # "OPEN VIDEO-PLAYER" FUNCTION
    def open_video_player(self):
        return
    
    # "OPEN FAVORITE LIST" FUNCTION
    def open_sound_player(self):
        return
    
    # "HIDE ALL OBJECT" FUNCTION
    def hide_all(self):
        self.splash_label.hide()
        self.favorite_button.hide()
        self.player_button.hide()
        self.radio_button.hide()
        self.tv_button.hide()
        self.timeLabel.hide()
        self.add_radio_channel_button.hide()
        self.remove_radio_channel_button.hide()
        self.list_radio_button.hide()
        self.videoWidget.hide()
        self.openButton.hide()
        self.playButton.hide()
        self.positionSlider.hide()
        self.errorLabel.hide()
        self.stopButton.hide()
        self.lastMediaButton.hide()
        self.nextMediaButton.hide()
        self.add_favorites_button.hide()
        self.remove_favorites_button.hide()
        self.favorites_listbox.hide()
        self.stop_radio_button.hide()
        self.errorLabel.hide()

    # "HIDE SPLASH" FUNCTION
    def hideSplash(self):
        # HIDING OF OBJECTS
        self.hide_all()
        
        # CHANGING OF COLOR
        self.setStyleSheet('background-color: rgb(0, 49, 83)')
        
        # SHOWING OF OBJECTS
        self.favorite_button.show()
        self.player_button.show()
        self.radio_button.show()
        #self.tv_button.show()
        self.home_button.show()
        self.minimaze_button.show()
        self.exit_button.show()
        self.remove_radio_channel_button.hide()
        self.radio_channel_input.hide()
        self.radio_channels_listbox.hide()
        self.timeLabel.hide()
        self.label.hide()

    def goHome(self):
        self.stopVideo()
        self.hide_all()
        
        if hasattr(self, 'label') and self.label.isVisible():
            self.label.hide()
            self.label.clear()
        self.favorite_button.show()
        self.player_button.show()
        self.radio_button.show()
        self.home_button.show()
        self.minimaze_button.show()
        self.exit_button.show()
        self.setStyleSheet('background-color: rgb(0, 49, 83)')

    # "OPEN FAVORITES PAGE" FUNCTION
    def favorites_page(self):
        self.hide_all()
        
        # SHOWING OF OBJECTS
        self.add_favorites_button.show()
        self.remove_favorites_button.show()
        self.favorites_listbox.show()

        # "CLICKED" SOUND
        self.click_sound_function()

    # "ADD TO FAVORITES" FUNCTION
    def add_favorites(self):
        # "CLICKED" SOUND
        self.click_sound_function()
        
        fileName, _ = QFileDialog.getOpenFileName(self, "Add Media", "", "All files (*.*)")
        if fileName != '':
            text = fileName
            self.favorites_list.append(str(text))
            self.favorites_listbox.clear()
            self.favorites_listbox.addItems(self.favorites_list)

    # "REMOVE TO FAVORITES" FUNCTION
    def remove_favorites(self):
        # "CLICKED" SOUND
        self.click_sound_function()
        
        selected_item = self.favorites_listbox.currentItem()
        if selected_item:
            text = selected_item.text()
            self.favorites_list.remove(text)
            self.favorites_listbox.clear()
            self.favorites_listbox.addItems(self.favorites_list)

    # "DOUBLE CLICK IN FAVORITES" FUNCTION
    def double_click_favorites(self):
        self.hide_all()

        current_item = self.favorites_listbox.currentItem()
        file_Name = current_item.text()
        
        # SHOWING OF OBJECTS
        self.videoWidget.show()
        self.openButton.show()
        self.playButton.show()
        self.positionSlider.show()
        self.errorLabel.show()
        self.timeLabel.show()
        self.stopButton.show()
        self.timeLabel.show()

        position = self.mediaPlayer.position() / 1000
        self.timeLabel.setText("{:02}:{:02}".format(int(position // 60), int(position % 60)))

        self.openFile(file_Name)

    # "OPEN RADIO PAGE" FUNCTION
    def player_page(self):
        self.hide_all()
        
        # SHOWING OF OBJECTS
        self.videoWidget.show()
        self.openButton.show()
        self.playButton.show()
        self.positionSlider.show()
        self.errorLabel.show()
        self.timeLabel.show()
        self.stopButton.show()
        self.timeLabel.show()
        self.lastMediaButton.show()
        self.nextMediaButton.show()

        position = self.mediaPlayer.position() / 1000
        self.timeLabel.setText("{:02}:{:02}".format(int(position // 60), int(position % 60)))

        # "CLICKED" SOUND
        self.click_sound_function()

    def openFileFromButton(self, fileName):
        self.stopVideo()
        self.updatePlayerTime()
        self.click_sound_function()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Media", "", "All files (*.*)")
        self.openFile(fileName)

    def openFile(self, fileName):
        folder = os.path.dirname(fileName)
        all_files = os.listdir(folder)

        self.folderMedia = [os.path.join(folder, f) for f in all_files 
                            if f.lower().endswith(('.png', '.bmp', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.svgz', '.webp', '.mp4', '.avi', '.mkv', '.wav', '.mp3'))]
        if fileName in self.folderMedia:
            self.currentMedia = self.folderMedia.index(fileName)

        if hasattr(self, 'label'):
            self.label.clear()
            self.label.deleteLater()
            del self.label

        self.mediaPlayer.stop()
        self.mediaPlayer.setMedia(QMediaContent())
        self.videoWidget.hide()

        if fileName.lower().endswith(('.png', '.bmp', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.svgz' '.webp')):
            self.label = QLabel(self)
            pixmap = QPixmap(fileName)
            scaled_pixmap = pixmap.scaled(self.display_width, self.display_height - 160, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.updatePixmap()
            self.label.setPixmap(scaled_pixmap)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setGeometry(0, 60, self.display_width, self.display_height - 160)
            self.label.show()
            self.playButton.setEnabled(False)
        else:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.videoWidget.show()
            self.playButton.setEnabled(True)


    def playVideo(self):
        self.updatePlayerTime()
        self.click_sound_function()
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def hideSplash(self):
        self.splash_label.hide()
        self.setStyleSheet('background-color: rgb(0, 49, 83)')
        self.favorite_button.show()
        self.player_button.show()
        self.radio_button.show()
        self.home_button.show()
        self.minimaze_button.show()
        self.exit_button.show()

    def stopVideo(self):
        self.click_sound_function()
        self.mediaPlayer.stop()
        self.mediaPlayer.setMedia(QMediaContent())
        self.positionSlider.setValue(0)
        self.timeLabel.setText("00:00")


    def updatePlayerTime(self):
        position = self.mediaPlayer.position() / 1000
        self.timeLabel.setText("{:02}:{:02}".format(int(position // 60), int(position % 60)))

    def mediaStateChanged(self, state):
        self.updatePlayerTime()
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setText("Pause")
        else:
            self.playButton.setText("Play")

    def positionChanged(self, position):
        self.updatePlayerTime()
        self.positionSlider.setValue(position)

    def lastMedia(self):
        self.click_sound_function()
        if self.folderMedia:
            self.currentMedia = (self.currentMedia - 1) % len(self.folderMedia)
            self.openFile(self.folderMedia[self.currentMedia])

    def nextMedia(self):
        self.click_sound_function()
        if self.folderMedia:
            self.currentMedia = (self.currentMedia + 1) % len(self.folderMedia)
            self.openFile(self.folderMedia[self.currentMedia])

    def durationChanged(self, duration):
        self.updatePlayerTime()
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.updatePlayerTime()
        self.mediaPlayer.setPosition(position)

    def displayErrorMessage(self, error):
        self.updatePlayerTime()
        self.errorLabel.setText("Error: " + error)

    # "OPEN RADIO PAGE" FUNCTION
    def radio_page(self):
        self.hide_all()
        
        # SHOWING OF OBJECTS
        self.add_radio_channel_button.show()
        self.remove_radio_channel_button.show()
        self.radio_channel_input.show()
        self.radio_channels_listbox.show()
        self.list_radio_button.show()
        self.stop_radio_button.show()

        # "CLICKED" SOUND
        self.click_sound_function()
    
    def list_radio(self):
        self.stop_radio()
        url = self.radio_channel_input.text()
        media_content = QMediaContent(QUrl(url))
        self.radio_player.setMedia(media_content)
        self.radio_player.play()

        # "CLICKED" SOUND
        self.click_sound_function()

    def stop_radio(self):
        self.radio_player.stop()

    def add_radio_channel(self):
        # "CLICKED" SOUND
        self.click_sound_function()
        
        text = self.radio_channel_input.text()
        self.radio_chanels.append(str(text))
        self.radio_channels_listbox.clear()
        self.radio_channels_listbox.addItems(self.radio_chanels)

    def remove_radio_channel(self):
        # "CLICKED" SOUND
        self.click_sound_function()
        
        selected_item = self.radio_channels_listbox.currentItem()
        if selected_item:
            text = selected_item.text()
            self.radio_chanels.remove(text)
            self.radio_channels_listbox.clear()
            self.radio_channels_listbox.addItems(self.radio_chanels)

    def double_click_radio(self):
        self.stop_radio()
        url = self.radio_channels_listbox.currentItem().text()
        media_content = QMediaContent(QUrl(url))
        self.radio_player.setMedia(media_content)
        self.radio_player.play()

        # "CLICKED" SOUND
        self.click_sound_function()

    # "OPEN TV PAGE" FUNCTION
    def tv_page(self):
        # SOUND
        self.click_sound_function()

        # HIDING OF OBJECTS
        self.hide_all()
        
        # SHOWING OF OBJECTS

    
    
    def closeEvent(self, event):
        home_directory = os.path.expanduser("~")
        file_path_favorites = os.path.join(home_directory, '.programdates', 'favorites_media.txt')

        with open(file_path_favorites, 'w') as f:
            for item in self.favorites_list:
                f.write(f'{item}\n')
        event.accept()

        file_path_radio = os.path.join(home_directory, '.programdates', 'radio.txt')

        with open(file_path_radio, 'w') as f:
            for item in self.radio_chanels:
                f.write(f'{item}\n')
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MediaCenter()

    if len(sys.argv) > 1:
        window.setStyleSheet("background-color: rgb(0, 49, 83);")
        file_path = sys.argv[1]
        window.openFile(file_path)

        window.home_button.show()
        window.minimaze_button.show()
        window.exit_button.show()
        window.openButton.show()
        window.playButton.show()
        window.positionSlider.show()
        window.stopButton.show()
        window.timeLabel.show()
        window.errorLabel.show()

    else:
        window.splash_label.show()
        window.startup_sound.play()
        window.splash_movie.start()
        window.timer.singleShot(1000, window.hideSplash)

    # Показываем приложение на весь экран
    window.showFullScreen()
    sys.exit(app.exec_())