
import pygame

SCREEN_SIZE = (1200, 700)

class TextPrint(object):
    def __init__(self):
       self._startX = 10
       self._startY = 10
       self._indent = 10
       self.reset()
       self._lineHeight = 15
       self._lineWidth = 300
       self._font = pygame.font.Font("PressStart2P.ttf", 8)
       
    
    def renderJoy(self, joy, screen):
        # Get the joystick of the given number
              
        self.joystick = pygame.joystick.Joystick(joy)
        if not self.joystick.get_init():
            self.joystick.init()
        
  
        # Display the joystick's number
        self.renderText(screen, f"Joystick {joy}")
        self.indent()
    
        # Get the name from the OS for the controller/joystick
        name = self.joystick.get_name()
        self.renderText(screen, f"Joystick name: {name}")
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = self.joystick.get_numaxes()
        self.renderText(screen, f"Number of axes: {axes}")
        self.indent()
        
        for i in range( axes ):
            axis = self.joystick.get_axis(i)
            self.renderText(screen, f"Axis {i} value: {axis:>6.3f}")
        self.unindent()
            
        # Display buttons
        buttons = self.joystick.get_numbuttons()
        self.renderText(screen, f"Number of buttons: {buttons}")
        self.indent()
  
        for i in range( buttons ):
            button = self.joystick.get_button(i)
            self.renderText(screen, f"Button {i:>2} value: {button}")
        self.unindent()
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = self.joystick.get_numhats()
        self.renderText(screen, f"Number of hats: {hats}")
        self.indent()
  
        for i in range( hats ):
            hat = self.joystick.get_hat( i )
            self.renderText(screen, f"Hat {i} value: {hat}")
        self.unindent()
        
        self.unindent()
 
    def renderText(self, screen, textString):
        # Render some text at the current location and move down a line
        textBitmap = self._font.render(textString, True, (0,0,0))
        screen.blit(textBitmap, [self._x, self._y])
        self._y += self._lineHeight
        
    def reset(self):
        # Go back to the top left
        self._x = self._startX
        self._y = self._startY
        
    def indent(self):
        # "tab" over
        self._x += self._indent
        
    def unindent(self):
        # undo tab
        self._x -= self._indent
       
    def nextJoy(self):
        # Return to the top and move to the right
        self._x += self._lineWidth
        self._y = self._startY + self._lineHeight
       
   
def main():
    
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    
    pygame.display.set_caption("Joystick Controls")
    
    screen = pygame.display.set_mode(SCREEN_SIZE)
    
    
    textPrint = TextPrint()
    
    # define a variable to control the main loop
    RUNNING = True
    
    # main loop
    while RUNNING:
          
        
        # Draw everything
        screen.fill((255,255,255))
        textPrint.reset()
        
        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()
        
        
        textPrint.renderText(screen, f"Number of joysticks: {joystick_count}")
        textPrint.indent()
      
        # For each joystick:
        for i in range(joystick_count):
            textPrint.renderJoy(i, screen)
            textPrint.nextJoy()
    
        # Flip the display to the monitor
        pygame.display.flip()
        
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
           # only do something if the event is of type QUIT or ESCAPE is pressed
           if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
              # change the value to False, to exit the main loop
              RUNNING = False
           
              
        
        # Update everything
       
if __name__ == "__main__":
    main()