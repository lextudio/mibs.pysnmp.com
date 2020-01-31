#
# PySNMP MIB module CT-DARADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-DARADIUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:28:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, TimeTicks, Unsigned32, Gauge32, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, MibIdentifier, Bits, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "TimeTicks", "Unsigned32", "Gauge32", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "MibIdentifier", "Bits", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctSSA = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497))
daRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 24))
daRadiusConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1))
daRadiusGeneralConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1))
daRadiusStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2))
daRadiusGeneralStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 1))
daRadiusgcEnabled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: daRadiusgcEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: daRadiusgcEnabled.setDescription('Administrative status for the RADIUS client.')
daRadiusgcAuthNumRetries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: daRadiusgcAuthNumRetries.setStatus('mandatory')
if mibBuilder.loadTexts: daRadiusgcAuthNumRetries.setDescription('Number of times the RADIUS client will issue a request to a RADIUS Authentication Server if the server does not respond.')
daRadiusgcAuthSecsBtwnRetries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: daRadiusgcAuthSecsBtwnRetries.setStatus('mandatory')
if mibBuilder.loadTexts: daRadiusgcAuthSecsBtwnRetries.setDescription('Number of seconds a RADIUS Authentication Server has to respond to a request before the RADIUS client gives up waiting.')
daRadiusgcAcctNumRetries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: daRadiusgcAcctNumRetries.setStatus('mandatory')
if mibBuilder.loadTexts: daRadiusgcAcctNumRetries.setDescription('Number of times the RADIUS client will issue a request to a RADIUS Accounting Server attempting to solicit a response.')
gcAcctSecsBtwnRetries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gcAcctSecsBtwnRetries.setStatus('mandatory')
if mibBuilder.loadTexts: gcAcctSecsBtwnRetries.setDescription('Number of seconds a RADIUS Accounting Server has to respond to a request before the RADIUS client gives up waiting.')
daRadiusServerCfgTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2), )
if mibBuilder.loadTexts: daRadiusServerCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: daRadiusServerCfgTable.setDescription('This table contains RADIUS server configurations used by the RADIUS client.')
daRadiusServerCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1), ).setIndexNames((0, "CT-DARADIUS-MIB", "scIndex"))
if mibBuilder.loadTexts: daRadiusServerCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: daRadiusServerCfgEntry.setDescription('Each entry contains configuration information for a RADIUS server.')
scIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primaryAuthentication", 1), ("secondaryAuthentication", 2), ("primaryAccounting", 3), ("secondaryAccounting", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scIndex.setStatus('mandatory')
if mibBuilder.loadTexts: scIndex.setDescription('Type of RADIUS server.')
scStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scStatus.setStatus('mandatory')
if mibBuilder.loadTexts: scStatus.setDescription('RADIUS client administrative status for the RADIUS server, indicating if the server is enabled to be used by the RADIUS client.')
scIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: scIpAddress.setDescription('RADIUS server IP address.')
scSharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scSharedSecret.setStatus('mandatory')
if mibBuilder.loadTexts: scSharedSecret.setDescription('Shared secret used to authentication transactions between the RADIUS client and the RADIUS server.')
scUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: scUdpPort.setStatus('mandatory')
if mibBuilder.loadTexts: scUdpPort.setDescription('RADIUS server UDP port.')
gsInDiscards = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gsInDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: gsInDiscards.setDescription('The number of packets received from RADIUS servers which were chosen to be discarded even though no errors had been detected. The packets were chosen to be discarded before the source RADIUS server was identified. One possible reason for discarding a packet could be because the packet was received after the RADIUS client gave up waiting for it.')
gsInErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gsInErrors.setStatus('mandatory')
if mibBuilder.loadTexts: gsInErrors.setDescription('The number of packets received from RADIUS servers that contained errors preventing them from being processed. The packets were found to contain errors before the source RADIUS server was identified.')
daRadiusServerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2), )
if mibBuilder.loadTexts: daRadiusServerStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: daRadiusServerStatsTable.setDescription('This table contains RADIUS server statistics tallied by the RADIUS client.')
daRadiusServerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1), ).setIndexNames((0, "CT-DARADIUS-MIB", "ssIndex"))
if mibBuilder.loadTexts: daRadiusServerStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: daRadiusServerStatsEntry.setDescription('Each entry contains RADIUS server statistics tallied by the RADIUS client.')
ssIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primaryAuthentication", 1), ("secondaryAuthentication", 2), ("primaryAccounting", 3), ("secondaryAccounting", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ssIndex.setDescription('Type of RADIUS server.')
ssInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssInPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ssInPkts.setDescription('The number of packets received from the RADIUS server that were successfully handled by the RADIUS client.')
ssInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssInDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: ssInDiscards.setDescription('The number of packets received from the RADIUS server which were chosen to be discarded even though no errors had been detected. One possible reason for discarding a packet could be because the RADIUS code field of the packet was not recognized.')
ssInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssInErrors.setStatus('mandatory')
if mibBuilder.loadTexts: ssInErrors.setDescription('The number of packets received from the RADIUS server that contained errors preventing them from being processed.')
ssOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssOutPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ssOutPkts.setDescription('The number of packets transmitted to the RADIUS server.')
ssOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssOutErrors.setStatus('mandatory')
if mibBuilder.loadTexts: ssOutErrors.setDescription('The number of packets the RADIUS client was unable to transmit to the RADIUS server due to transmission errors.')
ssResponseTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssResponseTimeouts.setStatus('mandatory')
if mibBuilder.loadTexts: ssResponseTimeouts.setDescription('The number of times the RADIUS client did not receive a response from the RADIUS server within the expected time.')
mibBuilder.exportSymbols("CT-DARADIUS-MIB", gsInDiscards=gsInDiscards, scStatus=scStatus, ssOutPkts=ssOutPkts, daRadiusServerStatsTable=daRadiusServerStatsTable, daRadius=daRadius, ssInPkts=ssInPkts, daRadiusgcEnabled=daRadiusgcEnabled, gcAcctSecsBtwnRetries=gcAcctSecsBtwnRetries, scIndex=scIndex, ssInDiscards=ssInDiscards, ssIndex=ssIndex, daRadiusConfig=daRadiusConfig, gsInErrors=gsInErrors, ssOutErrors=ssOutErrors, ssInErrors=ssInErrors, daRadiusGeneralConfig=daRadiusGeneralConfig, daRadiusServerStatsEntry=daRadiusServerStatsEntry, daRadiusgcAuthNumRetries=daRadiusgcAuthNumRetries, scIpAddress=scIpAddress, ssResponseTimeouts=ssResponseTimeouts, daRadiusStats=daRadiusStats, daRadiusgcAuthSecsBtwnRetries=daRadiusgcAuthSecsBtwnRetries, scUdpPort=scUdpPort, daRadiusServerCfgEntry=daRadiusServerCfgEntry, scSharedSecret=scSharedSecret, ctSSA=ctSSA, daRadiusgcAcctNumRetries=daRadiusgcAcctNumRetries, daRadiusServerCfgTable=daRadiusServerCfgTable, daRadiusGeneralStats=daRadiusGeneralStats)