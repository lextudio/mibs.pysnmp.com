#
# PySNMP MIB module EMPIRE-SVCRSP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EMPIRE-SVCRSP
# Produced by pysmi-0.3.4 at Wed May  1 13:02:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Unsigned32, iso, Counter32, Bits, Gauge32, TimeTicks, Integer32, NotificationType, ModuleIdentity, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Unsigned32", "iso", "Counter32", "Bits", "Gauge32", "TimeTicks", "Integer32", "NotificationType", "ModuleIdentity", "IpAddress", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
empire = MibIdentifier((1, 3, 6, 1, 4, 1, 546))
applications = MibIdentifier((1, 3, 6, 1, 4, 1, 546, 16))
svcRsp = MibIdentifier((1, 3, 6, 1, 4, 1, 546, 16, 6))
svcRspVersion = MibScalar((1, 3, 6, 1, 4, 1, 546, 16, 6, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspVersion.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspVersion.setDescription('Description and version number of this module')
svcRspPID = MibScalar((1, 3, 6, 1, 4, 1, 546, 16, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspPID.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspPID.setDescription('Process ID of the svcrsp sub-program.')
svcRspModMode = MibScalar((1, 3, 6, 1, 4, 1, 546, 16, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fullMode", 1), ("restrictedMode", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspModMode.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspModMode.setDescription('This object indicates if the module is in full-mode or restricted-mode. Restricted-mode is entered, when SystemEDGE 4.0 and higher, fails to find a valid license. Once a valid license has been allocated and set, the module will then transition to fullMode(1)')
svcRspTable = MibTable((1, 3, 6, 1, 4, 1, 546, 16, 6, 10), )
if mibBuilder.loadTexts: svcRspTable.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTable.setDescription('This table describes the service response time measurements being conducted by this Application Management Moudle.')
svcRspTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1), ).setIndexNames((0, "EMPIRE-SVCRSP", "svcRspTableIndex"))
if mibBuilder.loadTexts: svcRspTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableEntry.setDescription('An entry in the service response measurement table.')
svcRspTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableIndex.setDescription('The index of this service response time table entry')
svcRspTableDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableDescr.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableDescr.setDescription('Description of this service-response monitoring entry. Limit of 256 characters.')
svcRspTableSvc = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("nntp", 1), ("dns", 2), ("pop3", 3), ("http", 4), ("ftp", 5), ("smtp", 6), ("ping", 7), ("tcpconnect", 8), ("custom", 9), ("https", 10), ("imap", 11), ("roundTripEmail", 12), ("virtualUserTest", 13), ("nis", 14), ("tftp", 15), ("dhcp", 16), ("mapi", 17), ("ldap", 18), ("activeDirectory", 19), ("sqlQuery", 20), ("snmp", 21), ("fileIO", 22)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableSvc.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableSvc.setDescription('The type of service being measured.')
svcRspTableArgs = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableArgs.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableArgs.setDescription('Service-specific arguments used for measuring purposes. Limit of 256 characters. Example service arguments are: dns: dns-server hostname http: URL [proxy-server] [username:user password:pass] ftp: ftp-server username passwd pop3: pop3-server username passwd nntp: nntp-server smtp: smtp-server ping: system-name packetsize tcpconnect: system-name port custom: script-name https: URL [proxy-server] [username:user password:pass] ')
svcRspTableInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableInterval.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableInterval.setDescription('The time interval between queries to the service.')
svcRspTableSamplesPerInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableSamplesPerInterval.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableSamplesPerInterval.setDescription('The number of samples taken at each query interval. For instance, if this value is set to 3 and svcRspTableInterval is set to 60 then after every 60 second interval, 3 sample transactions will be performed.')
svcRspTableTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTimeout.setDescription('The value (in seconds) after which service response time measurement should timeout for this particular service measurement.')
svcRspTableStatsWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableStatsWindow.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableStatsWindow.setDescription('The period (in seconds) over which response time statisics (e.g. mean, availability) for the particular service are calculated.')
svcRspTableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))).clone('createAndWait')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableStatus.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableStatus.setDescription('The status of this entry. This variable is equivalent in semantics to the SNMPv2 SMI RowStatus convention (see RFC 1443).')
svcRspTableLastUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableLastUpdate.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableLastUpdate.setDescription('The time (based on sysUpTime) that these counters and statistics were last updated.')
svcRspTableNumSamples = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableNumSamples.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableNumSamples.setDescription('The total number of samples taken since this row was initialized.')
svcRspTableTotalLastSample = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTotalLastSample.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTotalLastSample.setDescription('The total response time (in milliseconds) of the last sample.')
svcRspTableTotalMin = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTotalMin.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTotalMin.setDescription('The minimum total response time sample value over the statistics window.')
svcRspTableTotalMax = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTotalMax.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTotalMax.setDescription('The maximum total response time sample value over the statistics window.')
svcRspTableTotalMean = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTotalMean.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTotalMean.setDescription('The mean total response time value over the statistics window.')
svcRspTableTotalVariance = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTotalVariance.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTotalVariance.setDescription('The variance of the total response time values over the statistics window * 1000. A variance value of 1.337 would be returned by SA as 1337. The variance is calculated based on seconds, instead of milliseconds.')
svcRspTableTotalAvailability = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTotalAvailability.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTotalAvailability.setDescription('The availability of this service. This is calculated as the number of successful service queries divided by the number of service queries over the statistics window. A service query is successful if it succeeds within the timeout value specified for this entry.')
svcRspTableNameLastSample = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableNameLastSample.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableNameLastSample.setDescription('The name lookup (DNS) time (in milliseconds) of the last sample.')
svcRspTableNameMin = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableNameMin.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableNameMin.setDescription('The minimum name lookup time sample value over the statistics window.')
svcRspTableNameMax = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableNameMax.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableNameMax.setDescription('The maximum name lookup time sample value over the statistics window.')
svcRspTableNameMean = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableNameMean.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableNameMean.setDescription('The mean name lookup time value over the statistics window.')
svcRspTableNameVariance = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableNameVariance.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableNameVariance.setDescription('The variance of the name lookup time values over the statistics window. The variance is calculated based on seconds, instead of milliseconds.')
svcRspTableConnLastSample = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableConnLastSample.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableConnLastSample.setDescription('The connection time (in milliseconds) of the last sample.')
svcRspTableConnMin = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableConnMin.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableConnMin.setDescription('The minimum connection time sample value over the statistics window.')
svcRspTableConnMax = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableConnMax.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableConnMax.setDescription('The maximum connection time sample value over the statistics window.')
svcRspTableConnMean = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableConnMean.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableConnMean.setDescription('The mean connection time value over the statistics window.')
svcRspTableConnVariance = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableConnVariance.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableConnVariance.setDescription('The variance of the connection time values over the statistics window. The variance is calculated based on seconds, instead of milliseconds.')
svcRspTableTranLastSample = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTranLastSample.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTranLastSample.setDescription('The transaction time (in milliseconds) of the last sample.')
svcRspTableTranMin = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTranMin.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTranMin.setDescription('The minimum transaction time sample value over the statistics window.')
svcRspTableTranMax = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTranMax.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTranMax.setDescription('The maximum transaction time sample value over the statistics window.')
svcRspTableTranMean = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTranMean.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTranMean.setDescription('The mean transaction time value over the statistics window.')
svcRspTableTranVariance = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTranVariance.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTranVariance.setDescription('The variance of the transaction time values over the statistics window. The variance is calculated based on seconds, instead of milliseconds.')
svcRspTableBytesInLastSample = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableBytesInLastSample.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableBytesInLastSample.setDescription('The number of bytes received in the last sample.')
svcRspTableBytesOutLastSample = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableBytesOutLastSample.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableBytesOutLastSample.setDescription('The number of bytes sent in the last sample.')
svcRspTableTotalBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTotalBytesIn.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTotalBytesIn.setDescription('The total number of bytes received since SA was started. It should be noted that this counter will eventually wrap.')
svcRspTableTotalBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTotalBytesOut.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTotalBytesOut.setDescription('The total number of bytes sent since SA was started. It should be noted that this Counter will eventually wrap.')
svcRspTableThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableThroughput.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableThroughput.setDescription('The throughput, calculated over the statistics window, in bytes/sec. The BytesInLastSample and BytesOutLastSample will be added together for each sample. This number for each sample will be summed, and divided by the number of seconds in the sample.')
svcRspTableResults = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableResults.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableResults.setDescription('The results of the test. This field indicates non-error results, and the values are specific to each test type.')
svcRspTableErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableErrorCode.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableErrorCode.setDescription('The error code returned by the test. The values are specific to each test type. When possible, the standard numeric error codes for each test will be used (e.g. HTTP 404).')
svcRspTableTOSField = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 40), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTOSField.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTOSField.setDescription('This field allows the user to set the 8-bit TOS header in the IP header for each test. We will not enforce any particular RFC standard for the value of this field. It will be totally up to the user to decide an appropriate value.')
svcRspTableFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 41), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableFlags.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableFlags.setDescription('Reserved for future use as a bitmask field for toggle options')
svcRspTableLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 42), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableLimit.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableLimit.setDescription('This is the eHealth Response limit, used as a boundry for throwing exceptions')
svcRspTableUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 43), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableUsername.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableUsername.setDescription('For tests that require a login, the username is here instead of in the args field as in versions prior to 1.3')
svcRspTablePassword = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 44), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTablePassword.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTablePassword.setDescription('For tests that require a login, the password is here instead of in the args field as in versions prior to 1.3')
svcRspTableDest = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 45), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspTableDest.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableDest.setDescription('For all tests, the target / destination is now stored here instead of in the args field.')
svcRspTableTotalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableTotalErrors.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableTotalErrors.setDescription("This is the total number of errors, of all types, that this test has encountered over it's lifetime")
svcRspTableSamplesInWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableSamplesInWindow.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableSamplesInWindow.setDescription('This is the total number of samples represented by the status window. A 300 second window on a test with a 30 second interval would be 10, with the exception of during start up, and when a test is thrown out.')
svcRspTableSuccessesInWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 48), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspTableSuccessesInWindow.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspTableSuccessesInWindow.setDescription('This is the total number of successes within the status window for this test.')
svcRspUnusedIndex = MibScalar((1, 3, 6, 1, 4, 1, 546, 16, 6, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspUnusedIndex.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspUnusedIndex.setDescription('An SNMP Get of this MIB object returns an un-used svcrsp Table index number. It can be used for svcrsp table row creation optimization.')
svcRspMatchDescr = MibScalar((1, 3, 6, 1, 4, 1, 546, 16, 6, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspMatchDescr.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspMatchDescr.setDescription("This MIB object, when used in conjunction with svcRspEventMatchIndex can be used to quickly determine the index number corresponding to a particular entry description. SNMP Set'ing a description to this MIB object causes the agent to search through entries in the svcrsp table and place the index value of the last entry whose description matches, in the svcRspMatchIndex MIB object. If the description is not found, then 0 is placed in svcRspEventMatchIndex.")
svcRspMatchIndex = MibScalar((1, 3, 6, 1, 4, 1, 546, 16, 6, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspMatchIndex.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspMatchIndex.setDescription('See description for svcRspMatchDescr.')
svcRspNumTests = MibScalar((1, 3, 6, 1, 4, 1, 546, 16, 6, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspNumTests.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspNumTests.setDescription('This is the number of tests currently running on the agent. This may be greater than the number seen in eHealth, as it includes manually configured tests. This number should never be lower than the number of tests seen in eHealth.')
svcRspMaxThreads = MibScalar((1, 3, 6, 1, 4, 1, 546, 16, 6, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: svcRspMaxThreads.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspMaxThreads.setDescription('This is the maximum number of threads that the collector is allowed to run. Each thread executes a test, so multiple threads allows for tests to run concurrently.')
svcRspSecurityFlags = MibScalar((1, 3, 6, 1, 4, 1, 546, 16, 6, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: svcRspSecurityFlags.setStatus('mandatory')
if mibBuilder.loadTexts: svcRspSecurityFlags.setDescription('This is a bitmask for displaying various security settings: Bit 0: Security settings hidden. If this bit is set, all others will be set to 0 Bit 1: Allow Custom/Virtual User tests Bit 2: Allow File I/O tests Bit 3: Allow Untrusted SSL certificates in all SSL-based tests Bit 4-32 are currently unused')
mibBuilder.exportSymbols("EMPIRE-SVCRSP", svcRsp=svcRsp, svcRspVersion=svcRspVersion, svcRspPID=svcRspPID, svcRspTableTimeout=svcRspTableTimeout, svcRspTableBytesInLastSample=svcRspTableBytesInLastSample, svcRspTableSvc=svcRspTableSvc, svcRspModMode=svcRspModMode, svcRspTableTotalMin=svcRspTableTotalMin, svcRspTableNameMin=svcRspTableNameMin, svcRspTableDest=svcRspTableDest, svcRspTableArgs=svcRspTableArgs, svcRspUnusedIndex=svcRspUnusedIndex, svcRspSecurityFlags=svcRspSecurityFlags, svcRspTableTotalMax=svcRspTableTotalMax, svcRspTableTotalMean=svcRspTableTotalMean, svcRspTableFlags=svcRspTableFlags, svcRspTableDescr=svcRspTableDescr, svcRspTableIndex=svcRspTableIndex, svcRspTable=svcRspTable, svcRspTableNameMax=svcRspTableNameMax, svcRspTableBytesOutLastSample=svcRspTableBytesOutLastSample, svcRspTableConnLastSample=svcRspTableConnLastSample, svcRspTableUsername=svcRspTableUsername, empire=empire, svcRspTableTranMax=svcRspTableTranMax, svcRspTableSuccessesInWindow=svcRspTableSuccessesInWindow, svcRspMaxThreads=svcRspMaxThreads, svcRspTablePassword=svcRspTablePassword, svcRspTableLimit=svcRspTableLimit, svcRspTableStatsWindow=svcRspTableStatsWindow, svcRspTableLastUpdate=svcRspTableLastUpdate, svcRspTableNameLastSample=svcRspTableNameLastSample, svcRspTableTranLastSample=svcRspTableTranLastSample, svcRspTableSamplesInWindow=svcRspTableSamplesInWindow, svcRspTableEntry=svcRspTableEntry, svcRspTableStatus=svcRspTableStatus, svcRspTableTotalErrors=svcRspTableTotalErrors, svcRspTableTotalAvailability=svcRspTableTotalAvailability, svcRspMatchIndex=svcRspMatchIndex, svcRspTableTotalBytesOut=svcRspTableTotalBytesOut, svcRspMatchDescr=svcRspMatchDescr, svcRspTableSamplesPerInterval=svcRspTableSamplesPerInterval, svcRspTableErrorCode=svcRspTableErrorCode, svcRspTableConnMin=svcRspTableConnMin, svcRspTableConnMax=svcRspTableConnMax, svcRspTableConnVariance=svcRspTableConnVariance, svcRspTableTotalBytesIn=svcRspTableTotalBytesIn, svcRspTableTOSField=svcRspTableTOSField, applications=applications, svcRspTableTranMean=svcRspTableTranMean, svcRspTableNameVariance=svcRspTableNameVariance, svcRspTableConnMean=svcRspTableConnMean, svcRspTableInterval=svcRspTableInterval, svcRspTableTranVariance=svcRspTableTranVariance, svcRspTableNameMean=svcRspTableNameMean, svcRspTableResults=svcRspTableResults, svcRspNumTests=svcRspNumTests, svcRspTableNumSamples=svcRspTableNumSamples, svcRspTableTotalVariance=svcRspTableTotalVariance, svcRspTableTotalLastSample=svcRspTableTotalLastSample, svcRspTableTranMin=svcRspTableTranMin, svcRspTableThroughput=svcRspTableThroughput)