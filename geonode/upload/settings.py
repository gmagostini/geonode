import os

"""
main settings to handle the celery rate
"""
IMPORTER_GLOBAL_RATE_LIMIT = os.getenv("IMPORTER_GLOBAL_RATE_LIMIT", 5)
IMPORTER_PUBLISHING_RATE_LIMIT = os.getenv("IMPORTER_PUBLISHING_RATE_LIMIT", 5)
IMPORTER_RESOURCE_CREATION_RATE_LIMIT = os.getenv("IMPORTER_RESOURCE_CREATION_RATE_LIMIT", 10)
IMPORTER_RESOURCE_COPY_RATE_LIMIT = os.getenv("IMPORTER_RESOURCE_COPY_RATE_LIMIT", 10)
