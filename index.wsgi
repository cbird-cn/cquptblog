import sae
from cquptblog_project import wsgi

application = sae.create_wsgi_app(wsgi.application)