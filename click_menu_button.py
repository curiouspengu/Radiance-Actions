tap_ui_navigation()
for i in range(4):
    sleep(0.1)
    kc.tap(Key.left) 
for i in range(5 - button_num):
    sleep(0.1)
    kc.tap(Key.up)
sleep(0.1)
kc.tap(Key.enter)
tap_ui_navigation()
