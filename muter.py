import dbus
import threading
import subprocess
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GObject as gobject


loop = None
count = 0
muted = False
spotify_main = 'spotify'
AD_ID = 'spotify:ad:'

mute_command = "amixer -q -D pulse sset Master mute"
unmute_command = "amixer -q -D pulse sset Master unmute"

def run_spotify():
    global loop
    process = subprocess.Popen(spotify_main.split()) # run bash command
    output, error = process.communicate()
    loop.quit()

def mute():
    global muted
    muted = True
    subprocess.Popen(mute_command.split())

def unmute():
    global muted
    muted = False
    subprocess.Popen(unmute_command.split())

def catchall_handler(*args, **kwargs):
    """ handles input signals and mute/unmute based on track ID
    """
    if len(args) < 2 or args[0] != 'org.mpris.MediaPlayer2.Player':
        return

    song_id = args[1]['Metadata']['mpris:trackid']

    if not muted and song_id.startswith(AD_ID):
        mute()
    elif muted and not song_id.startswith(AD_ID):
        unmute()

def main():
    """ Set up signal receiver and start spotify
    """
    global loop
    DBusGMainLoop(set_as_default=True)

    loop = gobject.MainLoop()
    bus = dbus.SessionBus()

    bus.add_signal_receiver(catchall_handler, 
        dbus_interface="org.freedesktop.DBus.Properties")

    threading.Thread(target=run_spotify).start()
    loop.run()


if __name__ == "__main__":
    main()