import urllib2

# Small helper to make a POST request
def publish_to_elastic_search(uri, payload):
    logger.debug('Posting to URI %s' % uri)
    req = urllib2.Request(uri, payload)
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        if e.code == 201:
            logger.debug('The release has been pushed into ES')
        else:
            logger.error('Could not push release into ES', e)
            raise e


# Logger object of type `org.slf4j.Logger` is available.
# Check http://www.slf4j.org/apidocs/org/slf4j/Logger.html for more details.
# You can set custom logging level by using referring to the name: `com.xebialabs.platform.script.Logging`.
logger.info("Starting export of the release %s v2" % release.id)

publish_to_elastic_search(
    # `exportHook` object provides access to properties defined at `acme.ElasticSearchExportHook` synthetic type.
    uri = '%s/%s/%s' % (exportHook.url, exportHook.typeName, exportHook.indexName),
    # `releaseJson` contains a string with serialized release.
    payload = releaseJson
)
