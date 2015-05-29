This sample is intended to show how to develop custom JDBC export hook which takes completed releases, extracts some data and puts it into a 3rd-party database. It has been tested with MySQL 5.6.

Requirements: XL Release 4.7.0+.

There are 2 ways to load this export hook into XL Release:

## As a jar

1. From the root folder do: `./gradlew clean :mysql-jdbc-export-hook:jar`;
2. Copy generated jar (`./mysql-jdbc-export-hook/build/libs/mysql-jdbc-export-hook-*.jar`) into `XLRELEASE_SERVER_HOME/plugins`;
3. Restart the server.

## Add files to the the classpath

1. Copy contents of `mysql-jdbc-export-hook/src/main/resources` into `XLRELEASE_SERVER_HOME/ext`;
2. Restart the server.

# Pre-requisites

1. Install MySQL 5;
2. Create some database which name will be used in JDBC URL;
3. Download [the latest version of MySQL connector/J](http://dev.mysql.com/downloads/connector/j/) and put into `XLRELEASE_SERVER_HOME/plugins`.

After doing so you can go to `Settings -> Configuration` in XL Release and choose newly appeared option `Acme: Mysql reporting export hook`.

![Add Elastic search export hook](./images/mysql_acme.png)

## Tips and tricks

* Enable frequent archivation to test the script easier. You can do that by setting `xlrelease.ArchivingSettings.archivingJobCronSchedule=*/10 * * * * *` at `conf/deployit-defaults.properties` and selecting '0 Days' at `Settings -> General settings`;
* You don't need to restart the server if you change main python script;
* You do need to restart the server if you change `synthetic.xml`
* JDBC URL for this example should always start with `jdbc:mysql:`.

## Related articles

* <a href="https://docs.xebialabs.com/xl-deploy/how-to/writing-jython-scripts-for-xl-deploy.html">Writing Jython scripts for XL Deploy</a>
