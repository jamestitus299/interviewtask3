import reflex as rx

class popState(rx.State):
    show : bool = False
    
    def set_show_false(self):
        self.show = False
    
    def set_show_true(self):
        self.show = True
        
