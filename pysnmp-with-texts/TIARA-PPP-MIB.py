#
# PySNMP MIB module TIARA-PPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-PPP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, ModuleIdentity, TimeTicks, ObjectIdentity, Counter64, Unsigned32, Bits, Gauge32, MibIdentifier, iso, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Counter64", "Unsigned32", "Bits", "Gauge32", "MibIdentifier", "iso", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bundleId, = mibBuilder.importSymbols("TIARA-BUNDLE-MIB", "bundleId")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraPppMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 14))
tiaraPppMib.setRevisions(('1900-02-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tiaraPppMib.setRevisionsDescriptions(('Initial Revision.',))
if mibBuilder.loadTexts: tiaraPppMib.setLastUpdated('0002010000Z')
if mibBuilder.loadTexts: tiaraPppMib.setOrganization('Tiara Networks Inc.')
if mibBuilder.loadTexts: tiaraPppMib.setContactInfo(' Tiara Networks Customer Support 525 Race Street, Suite 100, San Jose, CA 95126 USA Tel: +1 408-216-4700 Fax: +1 408-216-4701 E-mail: support@tiaranetworks.com')
if mibBuilder.loadTexts: tiaraPppMib.setDescription('The MIB module defines the managed objects for Tiara enterrpise PPP/MLPPP. ')
pppTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 14, 1), )
if mibBuilder.loadTexts: pppTable.setStatus('current')
if mibBuilder.loadTexts: pppTable.setDescription('This table contains configurable parameters related to PPP/MLPPP bundle.')
pppTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1), ).setIndexNames((0, "TIARA-BUNDLE-MIB", "bundleId"))
if mibBuilder.loadTexts: pppTableEntry.setStatus('current')
if mibBuilder.loadTexts: pppTableEntry.setDescription('An entry in the PPP Table which contains the configuration for a particular bundle instance identified by the bundleId.')
pppMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 1), DisplayString().clone('64-1500-4096')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppMtu.setStatus('current')
if mibBuilder.loadTexts: pppMtu.setDescription('Minimum, default and maximum packet sizes to be sent separated by hyphens.')
pppMru = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 2), DisplayString().clone('46-1500-4096')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppMru.setStatus('current')
if mibBuilder.loadTexts: pppMru.setDescription('Minimum, default and maximum packet sizes to be received separated by hyphens.')
mlpppMrru = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 3), DisplayString().clone('1500-1524-8192')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mlpppMrru.setStatus('current')
if mibBuilder.loadTexts: mlpppMrru.setDescription('Maximum received reconstructed unit - maximum number of octets in the information fields of reassembled packets. This variable can be set only if the bundle is multi-link.')
mlpppSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("short", 1), ("long", 2))).clone('long')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mlpppSeq.setStatus('current')
if mibBuilder.loadTexts: mlpppSeq.setDescription('MLPPP sequence number length (short = 12 bits ; long = 24 bits. This variable can be set only if the bundle is multi-link.')
mlpppSegmentThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 5), Integer32().clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mlpppSegmentThreshold.setStatus('current')
if mibBuilder.loadTexts: mlpppSegmentThreshold.setDescription('Segmentation threshold - number of octets a packet must exceed before being fragmented for transmission. This variable can be set only if the bundle is multi-link.')
mlpppDiffDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mlpppDiffDelay.setStatus('current')
if mibBuilder.loadTexts: mlpppDiffDelay.setDescription('Tolerance, in milliseconds, to differential delay between links. If The differential delay exceeds this limit, the corresponding link will be removed from the bundle. This variable can be set only if the bundle is multi-link.')
mlpppDiscriminator = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mlpppDiscriminator.setStatus('current')
if mibBuilder.loadTexts: mlpppDiscriminator.setDescription('IP address of MLPPP discriminator. This variable can be set only if the bundle is multi-link.')
pppStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2), )
if mibBuilder.loadTexts: pppStatsTable.setStatus('current')
if mibBuilder.loadTexts: pppStatsTable.setDescription('This table contains the statistics for PPP/MLPPP bundles.')
pppStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1), ).setIndexNames((0, "TIARA-BUNDLE-MIB", "bundleId"))
if mibBuilder.loadTexts: pppStatsTableEntry.setStatus('current')
if mibBuilder.loadTexts: pppStatsTableEntry.setDescription('An entry in the PPP Statistics Table which contains the statistics for a particular bundle instance identified by the bundleId.')
pppStatsBytesRxLastBootOrClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsBytesRxLastBootOrClear.setStatus('current')
if mibBuilder.loadTexts: pppStatsBytesRxLastBootOrClear.setDescription('This counter has the number of bytes received on this bundle since it was last booted or cleared.')
pppStatsBytesTxLastBootOrClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsBytesTxLastBootOrClear.setStatus('current')
if mibBuilder.loadTexts: pppStatsBytesTxLastBootOrClear.setDescription('This counter has the number of bytes transmitted on this bundle since it was last booted or cleared.')
pppStatsPktsRxLastBootOrClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsPktsRxLastBootOrClear.setStatus('current')
if mibBuilder.loadTexts: pppStatsPktsRxLastBootOrClear.setDescription('This counter has the number of packets received on this bundle since it was last booted or cleared.')
pppStatsPktsTxLastBootOrClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsPktsTxLastBootOrClear.setStatus('current')
if mibBuilder.loadTexts: pppStatsPktsTxLastBootOrClear.setDescription('This counter has the number of packets transmitted on this bundle since it was last booted or cleared.')
pppStatsErrPktsRxLastBootOrClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsErrPktsRxLastBootOrClear.setStatus('current')
if mibBuilder.loadTexts: pppStatsErrPktsRxLastBootOrClear.setDescription('This counter has the number of error packets received on this bundle since it was last booted or cleared.')
pppStatsUpDownStatesLastBootOrClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsUpDownStatesLastBootOrClear.setStatus('current')
if mibBuilder.loadTexts: pppStatsUpDownStatesLastBootOrClear.setDescription("This variable has the count on the number of times this PPP/MLPPP bundle have made the 'Down' to 'Up' and 'Up' to 'Down' transitions since it was last booted or cleared.")
pppStatsBytesRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsBytesRxLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: pppStatsBytesRxLastFiveMins.setDescription('This counter has the number of bytes received on this bundle in the last 5 minutes.')
pppStatsBytesTxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsBytesTxLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: pppStatsBytesTxLastFiveMins.setDescription('This counter has the number of bytes transmitted on this bundle in the last 5 minutes.')
pppStatsPktsRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsPktsRxLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: pppStatsPktsRxLastFiveMins.setDescription('This counter has the number of packets received on this bundle in the last 5 minutes.')
pppStatsPktsTxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsPktsTxLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: pppStatsPktsTxLastFiveMins.setDescription('This counter has the number of packets transmitted on this bundle in the last 5 minutes.')
pppStatsErrPktsRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsErrPktsRxLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: pppStatsErrPktsRxLastFiveMins.setDescription('This counter has the number of error packets received on this bundle in the last 5 minutes.')
pppStatsUpDownStatesLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 14, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppStatsUpDownStatesLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: pppStatsUpDownStatesLastFiveMins.setDescription("This variable has the count on the number of times this PPP/MLPPP bundle have made the 'Down' to 'Up' and 'Up' to 'Down' transitions in the last 5 minutes.")
mibBuilder.exportSymbols("TIARA-PPP-MIB", pppMru=pppMru, mlpppSeq=mlpppSeq, pppStatsPktsRxLastBootOrClear=pppStatsPktsRxLastBootOrClear, pppStatsUpDownStatesLastBootOrClear=pppStatsUpDownStatesLastBootOrClear, pppStatsPktsTxLastBootOrClear=pppStatsPktsTxLastBootOrClear, pppTableEntry=pppTableEntry, pppStatsBytesRxLastBootOrClear=pppStatsBytesRxLastBootOrClear, pppTable=pppTable, pppStatsPktsRxLastFiveMins=pppStatsPktsRxLastFiveMins, mlpppDiffDelay=mlpppDiffDelay, pppMtu=pppMtu, pppStatsErrPktsRxLastFiveMins=pppStatsErrPktsRxLastFiveMins, pppStatsBytesTxLastFiveMins=pppStatsBytesTxLastFiveMins, pppStatsTableEntry=pppStatsTableEntry, pppStatsPktsTxLastFiveMins=pppStatsPktsTxLastFiveMins, pppStatsTable=pppStatsTable, pppStatsErrPktsRxLastBootOrClear=pppStatsErrPktsRxLastBootOrClear, tiaraPppMib=tiaraPppMib, mlpppSegmentThreshold=mlpppSegmentThreshold, pppStatsBytesRxLastFiveMins=pppStatsBytesRxLastFiveMins, mlpppDiscriminator=mlpppDiscriminator, mlpppMrru=mlpppMrru, pppStatsBytesTxLastBootOrClear=pppStatsBytesTxLastBootOrClear, PYSNMP_MODULE_ID=tiaraPppMib, pppStatsUpDownStatesLastFiveMins=pppStatsUpDownStatesLastFiveMins)