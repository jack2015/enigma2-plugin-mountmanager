from distutils.core import setup
import setup_translate

setup(name = 'enigma2-plugin-systemplugins-mountmanager',
		version='1.9',
		author='Dimitrij',
		author_email='dima-73@inbox.lv',
		package_dir = {'SystemPlugins.MountManager': 'src'},
		packages=['SystemPlugins.MountManager'],
		package_data={'SystemPlugins.MountManager': ['*.sh', 'icons/*.png']},
		description = 'Mount devices at your decision (label,uuid)',
		cmdclass = setup_translate.cmdclass,
	)
