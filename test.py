export ANDROIDNDK="$HOME$/admin/Downloads/android-ndk-r21e-linux-x86_64"
export ANDROIDAPI="27"  # Target API version of your application
export NDKAPI="21"  # Minimum supported API version of your application
export ANDROIDNDKVER="r10e"  # Version of the NDK you installed



from jnius import autoclass
# Для начала нам нужна ссылка на Java Activity, в которой
# запущено приложение, она хранится в загрузчике Kivy PythonActivity
PythonActivity = autoclass('org.renpy.android.PythonActivity')
activity = PythonActivity.mActivity
Context = autoclass('android.content.Context')
vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
vibrator.vibrate(10000)  # аргумент указывается в миллисекундах
