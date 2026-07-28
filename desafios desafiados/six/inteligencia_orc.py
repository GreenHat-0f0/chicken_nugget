def inteligencia_orc(orc: "Orc"):
    # MEXER APENAS AQUI
    # Sensores: orc.EIXO_X, orc.EIXO_Y, orc.ESTA_TOCANDO, orc.PLAYER_A_FRENTE, orc.PAREDE_A_FRENTE
    # Acoes: orc.mover_frente(), orc.virar_esquerda(), orc.virar_direita(), orc.atacar()
    from pynput import keyboard
    
    import pygame  
    
    # Capture state of all keys on the keyboard
    keys = pygame.key.get_pressed()
    # map keys
    orc.mover_frente()
    orc.atacar()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        orc.virar_esquerda()
        
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        orc.virar_direita()
        
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        orc.virar_esquerda()
        orc.virar_esquerda()
    
    if orc.ESTA_TOCANDO:
        if not orc.PLAYER_A_FRENTE:
            orc.virar_direita
            if not orc.PLAYER_A_FRENTE:
                orc.virar_direita 
                if not orc.PLAYER_A_FRENTE:
                    orc.virar_direita
    
    
    
    
    # if orc.ESTA_TOCANDO:
    #     if orc.PLAYER_A_FRENTE:
    #         orc.atacar()
    #     elif orc.PLAYER_A_ESQUERDA:
    #         orc.virar_esquerda()
    #         orc.atacar()
    #     elif orc.PLAYER_A_DIREITA:
    #         orc.virar_direita()
    #         orc.atacar()
    #     else:
    #         orc.virar_esquerda()
    #         orc.virar_esquerda()
    #         if orc.PLAYER_A_FRENTE:
    #             orc.atacar()                     
    # elif not orc.PAREDE_A_FRENTE:
    #     orc.mover_frente()
    # else:
    #     orc.virar_esquerda()
    # else:
    #     orc.virar_direita()
    #     orc.virar_direita()


    # def mover_frente(self) -> None: ...
    # def virar_esquerda(self) -> None: ...
    # def virar_direita(self) -> None: ...
    # def atacar(self) -> None: ...
























# NAO MEXER
from _motor.tipos import Orc

if __name__ == "__main__":
    from _motor import executar_simulacao

    executar_simulacao(inteligencia_orc)
