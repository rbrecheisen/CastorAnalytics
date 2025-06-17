from castoranalytics.ui.utils import is_macos


# Window settings
CASTOR_ANALYTICS_WINDOW_TITLE = 'Castor Analytics'
CASTOR_ANALYTICS_NAME = 'CastorAnalytics'
CASTOR_ANALYTICS_BUNDLE_IDENTIFIER = 'com.rbeesoft'
CASTOR_ANALYTICS_WINDOW_W = 1024
CASTOR_ANALYTICS_WINDOW_H = 600

# Resources
CASTOR_ANALYTICS_RESOURCES_DIR = 'castoranalytics/resources'
CASTOR_ANALYTICS_RESOURCES_IMAGES_DIR = 'castoranalytics/resources/images'
CASTOR_ANALYTICS_RESOURCES_IMAGES_ICONS_DIR = 'castoranalytics/resources/images/icons'
CASTOR_ANALYTICS_RESOURCES_ICON = 'castoranalytics.icns' if is_macos() else 'castoranalytics.ico'
