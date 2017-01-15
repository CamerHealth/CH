"""
CH - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'CH.schema'
    flow_module   = 'CH.flow'
    javascripts   = [
        'js/CH/routes.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/CH/flow.js',
    ]