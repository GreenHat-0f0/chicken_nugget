def inteligencia_orc(orc: "Orc"):
    # MEXER APENAS AQUI
    # Sensores: orc.EIXO_X, orc.EIXO_Y, orc.ESTA_TOCANDO, orc.PLAYER_A_FRENTE, orc.PAREDE_A_FRENTE
    # Acoes: orc.mover_frente(), orc.virar_esquerda(), orc.virar_direita(), orc.atacar()
    from pynput import keyboard
    if orc.ESTA_TOCANDO:
        if orc.PLAYER_A_FRENTE:
            orc.atacar()
        elif orc.PLAYER_A_ESQUERDA:
            orc.virar_esquerda()
            orc.atacar()
        elif orc.PLAYER_A_DIREITA:
            orc.virar_direita()
            orc.atacar()
        else:
            orc.virar_esquerda()
            orc.virar_esquerda()
            orc.atacar()
    elif not orc.PAREDE_A_FRENTE:
        orc.mover_frente()
    else:
        orc.virar_direita()


    import sys
    import tty
    import termios
    import select
    import time

    def is_key_pressed():
        """Checks if there is a key waiting in the input buffer."""
        # select.select([file_descriptors], [outputs], [exceptions], timeout)
        # A timeout of 0 makes it completely non-blocking
        ready_to_read, _, _ = select.select([sys.stdin], [], [], 0)
        return ready_to_read

    # Save the original terminal settings
    original_settings = termios.tcgetattr(sys.stdin)

    try:
        # Switch the terminal to raw (non-canonical) mode
        tty.setcbreak(sys.stdin.fileno())

        counter = 0
        while True:
            # 1. This simulates your main code running continuously
            counter += 1
            print(f"\rBackground loop iteration: {counter}", end="", flush=True)
            time.sleep(0.1) # Small delay just to keep output readable

            # 2. Check for keyboard input without stalling the loop
            if is_key_pressed():
                key = sys.stdin.read(1)
                
                # 3. Execute actions instantly based on the key
                if key == 'a':
                    orc.virar_esquerda()
                elif key == 'd':
                    orc.virar_direita()
                elif key == 's':
                    orc.virar_esquerda()
                    orc.virar_esquerda()

    finally:
        # CRITICAL: Always restore terminal settings, even if code crashes
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_settings)

    # def on_press(key):
    #     print(f'\rKey pressed: {key}', end='')

    #     # Collect events until released
    #     with keyboard.Listener(on_press=on_press) as listener:
    #         listener.join()



    # def mover_frente(self) -> None: ...
    # def virar_esquerda(self) -> None: ...
    # def virar_direita(self) -> None: ...
    # def atacar(self) -> None: ...






















from _motor.tipos import Orc

if __name__ == "__main__":
    from _motor import executar_simulacao

    executar_simulacao(inteligencia_orc)
