from fanstatic import Library, Resource
import js.jquery
import js.jqueryui

library = Library('spiffform', 'resources')

spiffform = Resource(library, 'spiffform/spiffform.js',
        depends=[js.jquery.jquery, js.jqueryui.jqueryui, js.jqueryui.base])

spiffform_default_css = Resource(library, 'default.css',
        depends=[])

spiffform_css = Resource(library, 'spiffform/res/spiffform.css',
        depends=[])
