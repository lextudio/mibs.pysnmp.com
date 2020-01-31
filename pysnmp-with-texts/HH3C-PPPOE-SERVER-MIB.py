#
# PySNMP MIB module HH3C-PPPOE-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-PPPOE-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:29:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, NotificationType, IpAddress, TimeTicks, Gauge32, MibIdentifier, Integer32, Unsigned32, ModuleIdentity, iso, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "MibIdentifier", "Integer32", "Unsigned32", "ModuleIdentity", "iso", "Bits", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cPPPoEServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 102))
hh3cPPPoEServer.setRevisions(('2009-05-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cPPPoEServer.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: hh3cPPPoEServer.setLastUpdated('200905060000Z')
if mibBuilder.loadTexts: hh3cPPPoEServer.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cPPPoEServer.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: hh3cPPPoEServer.setDescription('The MIB module is used for PPPoE server.')
hh3cPPPoEServerObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 102, 1))
hh3cPPPoEServerMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPPPoEServerMaxSessions.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoEServerMaxSessions.setDescription('The maximum sessions supported by PPPoE server.')
hh3cPPPoEServerCurrSessions = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPPPoEServerCurrSessions.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoEServerCurrSessions.setDescription('The number of current sessions on the PPPoE server.')
hh3cPPPoEServerAuthRequests = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPPPoEServerAuthRequests.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoEServerAuthRequests.setDescription('The number of authentication requests.')
hh3cPPPoEServerAuthSuccesses = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPPPoEServerAuthSuccesses.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoEServerAuthSuccesses.setDescription('The number of authentication succeses.')
hh3cPPPoEServerAuthFailures = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPPPoEServerAuthFailures.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoEServerAuthFailures.setDescription('The number of authentication failure.')
hh3cPPPoESAbnormOffsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPPPoESAbnormOffsThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoESAbnormOffsThreshold.setDescription('The threshold of abnormal offline count.')
hh3cPPPoESAbnormOffPerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPPPoESAbnormOffPerThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoESAbnormOffPerThreshold.setDescription('The threshold of abnormal offline percent.')
hh3cPPPoESNormOffPerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPPPoESNormOffPerThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoESNormOffPerThreshold.setDescription('The threshold of normal offline percent.')
hh3cPPPoEServerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 102, 2))
hh3cPPPoeServerTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 102, 2, 0))
hh3cPPPoESAbnormOffsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 102, 2, 0, 1))
if mibBuilder.loadTexts: hh3cPPPoESAbnormOffsAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoESAbnormOffsAlarm.setDescription('This trap is generated when the PPPoE server abnormal offline counts over threshold in five minutes.')
hh3cPPPoESAbnormOffPerAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 102, 2, 0, 2))
if mibBuilder.loadTexts: hh3cPPPoESAbnormOffPerAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoESAbnormOffPerAlarm.setDescription('This trap is generated when the PPPoE server abnormal offline percent over threshold in five minutes.')
hh3cPPPoESNormOffPerAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 102, 2, 0, 3))
if mibBuilder.loadTexts: hh3cPPPoESNormOffPerAlarm.setStatus('current')
if mibBuilder.loadTexts: hh3cPPPoESNormOffPerAlarm.setDescription('This trap is generated when the PPPoE server normal offline percent under threshold in five minutes.')
mibBuilder.exportSymbols("HH3C-PPPOE-SERVER-MIB", hh3cPPPoEServer=hh3cPPPoEServer, hh3cPPPoEServerTraps=hh3cPPPoEServerTraps, hh3cPPPoeServerTrapPrefix=hh3cPPPoeServerTrapPrefix, PYSNMP_MODULE_ID=hh3cPPPoEServer, hh3cPPPoEServerAuthRequests=hh3cPPPoEServerAuthRequests, hh3cPPPoESNormOffPerThreshold=hh3cPPPoESNormOffPerThreshold, hh3cPPPoESNormOffPerAlarm=hh3cPPPoESNormOffPerAlarm, hh3cPPPoESAbnormOffPerAlarm=hh3cPPPoESAbnormOffPerAlarm, hh3cPPPoEServerObject=hh3cPPPoEServerObject, hh3cPPPoEServerAuthSuccesses=hh3cPPPoEServerAuthSuccesses, hh3cPPPoESAbnormOffPerThreshold=hh3cPPPoESAbnormOffPerThreshold, hh3cPPPoESAbnormOffsAlarm=hh3cPPPoESAbnormOffsAlarm, hh3cPPPoEServerAuthFailures=hh3cPPPoEServerAuthFailures, hh3cPPPoEServerMaxSessions=hh3cPPPoEServerMaxSessions, hh3cPPPoESAbnormOffsThreshold=hh3cPPPoESAbnormOffsThreshold, hh3cPPPoEServerCurrSessions=hh3cPPPoEServerCurrSessions)