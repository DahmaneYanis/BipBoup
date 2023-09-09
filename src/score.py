import pygame as py 



class ScoreText:
    def __init__(self, current_score : int) -> None:
        self.current_score = current_score
        
        self.font = py.font.SysFont("Comic Sans MS", 50)
        
    
    def update(self, window : py.Surface) -> None:
        self.draw(window)
        
    
    def draw(self, window : py.Surface) -> None:
        text = self.font.render(str(self.current_score), True, (0, 0, 0))
        window.blit(text, (window.get_width() // 2 - text.get_width() // 2, 0))
    
    
    def increment(self) -> None:
        self.current_score += 1