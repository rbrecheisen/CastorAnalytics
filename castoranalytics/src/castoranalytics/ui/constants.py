from castoranalytics.ui_old.utils import is_macos


# Window settings
CASTOR_ANALYTICS_WINDOW_TITLE = 'Castor Analytics'
CASTOR_ANALYTICS_NAME = 'CastorAnalytics'
CASTOR_ANALYTICS_BUNDLE_IDENTIFIER = 'com.rbeesoft'
CASTOR_ANALYTICS_WINDOW_W = 1024
CASTOR_ANALYTICS_WINDOW_H = 600
CASTOR_ANALYTICS_WINDOW_GEOMETRY_KEY = 'window/geometry'
CASTOR_ANALYTICS_WINDOW_STATE_KEY = 'window/state'
CASTOR_ANALYTICS_STATUS_READY = 'Ready'

# Main panel
CASTOR_ANALYTICS_MAIN_TAB_DETAILS_TITLE = 'Details'
CASTOR_ANALYTICS_MAIN_TAB_STATISTICS_TITLE = 'Summary statistics'
CASTOR_ANALYTICS_MAIN_TAB_VISUALIZATIONS_TITLE = 'Advanced visualizations'

# Study tree dock widget
CASTOR_ANALYTICS_STUDIES_DOCK_WIDGET_TITLE = 'Studies and Sites'
CASTOR_ANALYTICS_STUDIES_DOCK_WIDGET_OBJECT_NAME = 'StudyTreeDockWidget'

# Logging dock widget
CASTOR_ANALYTICS_LOGS_DOCK_WIDGET_TITLE = 'Logs'
CASTOR_ANALYTICS_LOGS_DOCK_WIDGET_OBJECT_NAME = 'LoggingDockWidget'

# Toolbar
CASTOR_ANALYTICS_TOOLBAR_OBJECT_NAME = 'ToolBar'

# Status bar
CASTOR_ANALYTICS_STATUS_INDICATOR_OBJECT_NAME = 'StatusIndicator'

# Resources
CASTOR_ANALYTICS_RESOURCES_DIR = 'castoranalytics/resources'
CASTOR_ANALYTICS_RESOURCES_IMAGES_DIR = 'castoranalytics/resources/images'
CASTOR_ANALYTICS_RESOURCES_IMAGES_ICONS_DIR = 'castoranalytics/resources/images/icons'
CASTOR_ANALYTICS_RESOURCES_ICON = 'castoranalytics.icns' if is_macos() else 'castoranalytics.ico'
