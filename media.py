import webbrowser
import os
class Movie():
    def __init__(self,m_title,m_storyline,m_posterimage,m_trailer):
        self.m_title = m_title
        self.m_storyline = m_storyline
        self.m_posterimage = m_posterimage
        self.m_trailer = m_trailer

    def show_trailer(self):
        webbrowser.open(self.m_trailer)
    def __str__(self):
        return f'Movie name is {self.m_title}, Title is {self.m_storyline}'

bahubali = Movie("BAHUBALI","ACTION DRAMA","C:\\Users\\Anurag Singhal\\Pictures\\Screenshots","https://youtu.be/G62HrubdD6o")  #\\ dena padega
bahubali.show_trailer()
