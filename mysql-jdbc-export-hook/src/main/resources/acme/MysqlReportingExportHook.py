connection = exportHook.getJdbcConnection()

try:
  statement = connection.createStatement()

  # CREATE TABLE is done here for simplicity of the example, but it makes sense to execute it manually once for various reasons.
  sql = "CREATE TABLE IF NOT EXISTS releases_report (id VARCHAR(255), title TEXT, status VARCHAR(255));"
  logger.debug("Executing SQL statement: %s" % sql)
  statement.executeUpdate(sql)

  releaseId = release.id
  title = release.title
  status = release.status.toString()

  sql = "INSERT INTO releases_report VALUES ('%s', '%s', '%s')" % (releaseId, title, status)
  logger.debug("Executing SQL statement: %s" % sql)
  statement.executeUpdate(sql)
finally:
  connection.close()
