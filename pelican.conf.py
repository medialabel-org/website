AUTHOR = "International Labelling Authority"
SITENAME = "MediaLabel.org"
SITESUBTITLE = "Restoring Trust in Visual Media"
SITEURL = "https://medialabel.org"
TIMEZONE = "America/Vancouver"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False

GITHUB_URL = "http://github.com/medialabel-org/website/"
# DISQUS_SITENAME = "medialabel-website"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

LINKS = (
    ("White Paper", "https://docs.google.com/document/d/1C1mGqO52YeZhA7YV6tQ0yuPDE-qeyj0gcsiAbRjrF3k/edit#heading=h.kivdn6wkdpwz"),
    ("Filyb", "http://filyb.info/"),
    ("Libert-fr", "http://www.libert-fr.com"),
    ("N1k0", "http://prendreuncafe.com/blog/"),
    ("Zubin Mithra", "http://zubin71.wordpress.com/"),
)

SOCIAL = (
    ("mastodon", "https://techhub.social/medialabel"),
    ("github", "https://github.com/medialabel-org"),
)

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# global metadata to all the contents
DEFAULT_METADATA = {"yeah": "it is"}

# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "extra/robots.txt",
]

# custom page generated with a jinja2 template
# TEMPLATE_PAGES = {"pages/jinja2_template.html": "jinja2_template.html"}

# there is no other HTML content
READERS = {"html": None}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {"linenos": "table"}

THEME = 'themes/pelican-bootstrap3'
OUTPUT_PATH = 'output'
PATH = 'content'
PLUGIN_PATHS = ['./pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
