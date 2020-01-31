#
# PySNMP MIB module A3COM-BRIDGE-R3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/A3COM-BRIDGE-R3-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:29:17 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
MacAddress, = mibBuilder.importSymbols("RFC1286-MIB", "MacAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, ObjectIdentity, IpAddress, enterprises, Counter64, Gauge32, iso, NotificationType, Unsigned32, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "ObjectIdentity", "IpAddress", "enterprises", "Counter64", "Gauge32", "iso", "NotificationType", "Unsigned32", "Counter32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 9))
class SMDSAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3ComBrgGen = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 9, 1))
a3ComBrgStp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 9, 2))
a3ComBrgSr = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 9, 3))
class X121Address(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 17)

a3ComBrgCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bridging", 1), ("noBridging", 2))).clone('noBridging')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgCtl.setStatus('mandatory')
a3ComBrgAgeCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aging", 1), ("noAging", 2))).clone('aging')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgAgeCtl.setStatus('mandatory')
a3ComBrgFwallCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("firewall", 1), ("noFirewall", 2))).clone('firewall')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgFwallCtl.setStatus('mandatory')
a3ComBrgLearnCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("learn", 1), ("noLearn", 2))).clone('learn')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgLearnCtl.setStatus('mandatory')
a3ComBrgForwardCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forward", 1), ("noForward", 2))).clone('forward')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgForwardCtl.setStatus('mandatory')
a3ComBrgAppleCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgAppleCtl.setStatus('mandatory')
a3ComBrgFwTblCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("dynToStatic", 2), ("delStatic", 3), ("delDyn", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgFwTblCtl.setStatus('mandatory')
a3ComBrgFwTblSize = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgFwTblSize.setStatus('mandatory')
a3ComBrgBLimitTimer = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("timer400ms", 2), ("timer600ms", 3), ("timer800ms", 4), ("timer1000ms", 5))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgBLimitTimer.setStatus('mandatory')
a3ComBrgStExtTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 10), )
if mibBuilder.loadTexts: a3ComBrgStExtTable.setStatus('mandatory')
a3ComBrgStExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 10, 1), ).setIndexNames((0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgStExtAdd"), (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgStExtRcvPort"))
if mibBuilder.loadTexts: a3ComBrgStExtEntry.setStatus('mandatory')
a3ComBrgStExtAdd = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 10, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgStExtAdd.setStatus('mandatory')
a3ComBrgStExtRcvPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 10, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgStExtRcvPort.setStatus('mandatory')
a3ComBrgStExtWaAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 10, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgStExtWaAddress.setStatus('mandatory')
a3ComBrgFdbExtTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 11), )
if mibBuilder.loadTexts: a3ComBrgFdbExtTable.setStatus('mandatory')
a3ComBrgFdbExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 11, 1), ).setIndexNames((0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgFdbExtAdd"))
if mibBuilder.loadTexts: a3ComBrgFdbExtEntry.setStatus('mandatory')
a3ComBrgFdbExtAdd = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 11, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgFdbExtAdd.setStatus('mandatory')
a3ComBrgFdbExtWaAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 11, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgFdbExtWaAddress.setStatus('mandatory')
a3ComBrgPortTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12), )
if mibBuilder.loadTexts: a3ComBrgPortTable.setStatus('mandatory')
a3ComBrgPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1), ).setIndexNames((0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgPortIndex"))
if mibBuilder.loadTexts: a3ComBrgPortEntry.setStatus('mandatory')
a3ComBrgPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgPortIndex.setStatus('mandatory')
a3ComBrgPortCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("transparent", 1), ("sourceRoute", 2), ("srtEnabled", 3), ("noBridging", 4))).clone('noBridging')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgPortCtl.setStatus('mandatory')
a3ComBrgDstSecCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("forward", 2), ("block", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgDstSecCtl.setStatus('mandatory')
a3ComBrgSrcSecCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("forward", 2), ("block", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrcSecCtl.setStatus('mandatory')
a3ComBrgX25Pid = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(221)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgX25Pid.setStatus('mandatory')
a3ComBrgX25Qsize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgX25Qsize.setStatus('deprecated')
a3ComBrgX25VcLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgX25VcLimit.setStatus('deprecated')
a3ComBrgX25VcTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgX25VcTimer.setStatus('deprecated')
a3ComBrgBroadCastLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgBroadCastLimit.setStatus('mandatory')
a3ComBrgSmdsGroupAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 10), SMDSAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSmdsGroupAddr.setStatus('mandatory')
a3ComBrgX25ProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 12, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgX25ProfId.setStatus('mandatory')
a3ComBrgX25NbrTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 13), )
if mibBuilder.loadTexts: a3ComBrgX25NbrTable.setStatus('mandatory')
a3ComBrgX25NbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 13, 1), ).setIndexNames((0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgX25NbrPort"), (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgX25NbrDTE"))
if mibBuilder.loadTexts: a3ComBrgX25NbrEntry.setStatus('mandatory')
a3ComBrgX25NbrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 13, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgX25NbrPort.setStatus('mandatory')
a3ComBrgX25NbrDTE = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 13, 1, 2), X121Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgX25NbrDTE.setStatus('mandatory')
a3ComBrgX25NbrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 1, 13, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgX25NbrStatus.setStatus('mandatory')
a3ComBrgStpMultAdd = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 2, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgStpMultAdd.setStatus('mandatory')
a3ComBrgStpCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgStpCtl.setStatus('mandatory')
a3ComBrgStpHopCtl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hopReduce", 1), ("noHopReduce", 2))).clone('noHopReduce')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgStpHopCtl.setStatus('mandatory')
a3ComBrgSrMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ieee", 1), ("passiveBridging", 2))).clone('ieee')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrMode.setStatus('mandatory')
a3ComBrgSrPortTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2), )
if mibBuilder.loadTexts: a3ComBrgSrPortTable.setStatus('mandatory')
a3ComBrgSrPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1), ).setIndexNames((0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrPort"))
if mibBuilder.loadTexts: a3ComBrgSrPortEntry.setStatus('mandatory')
a3ComBrgSrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgSrPort.setStatus('mandatory')
a3ComBrgSrPortSTEHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrPortSTEHopCount.setStatus('mandatory')
a3ComBrgSrPortAREHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrPortAREHopCount.setStatus('mandatory')
a3ComBrgSrPortHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrPortHoldTime.setStatus('mandatory')
a3ComBrgSrPortMinAccessPrior = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrPortMinAccessPrior.setStatus('mandatory')
a3ComBrgSrWanAddrTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3), )
if mibBuilder.loadTexts: a3ComBrgSrWanAddrTable.setStatus('mandatory')
a3ComBrgSrWanAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3, 1), ).setIndexNames((0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrWAportIndex"), (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrWAringNum"), (0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrWAbrgNum"))
if mibBuilder.loadTexts: a3ComBrgSrWanAddrEntry.setStatus('mandatory')
a3ComBrgSrWAportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgSrWAportIndex.setStatus('mandatory')
a3ComBrgSrWAringNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgSrWAringNum.setStatus('mandatory')
a3ComBrgSrWAbrgNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgSrWAbrgNum.setStatus('mandatory')
a3ComBrgSrWAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 3, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgSrWAddress.setStatus('mandatory')
a3ComBrgSrGwVirRing = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrGwVirRing.setStatus('mandatory')
a3ComBrgSrGwContTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5), )
if mibBuilder.loadTexts: a3ComBrgSrGwContTable.setStatus('mandatory')
a3ComBrgSrGwContEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5, 1), ).setIndexNames((0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrGwContPort"))
if mibBuilder.loadTexts: a3ComBrgSrGwContEntry.setStatus('mandatory')
a3ComBrgSrGwContPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgSrGwContPort.setStatus('mandatory')
a3ComBrgSrGwCont = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrGwCont.setStatus('mandatory')
a3ComBrgSrGwContEncapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ieeeMode", 1), ("etherMode", 2))).clone('ieeeMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrGwContEncapMode.setStatus('mandatory')
a3ComBrgSrGwContAutoMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("autoMode", 1), ("noAutoMode", 2))).clone('autoMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrGwContAutoMode.setStatus('mandatory')
a3ComBrgSrRDTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6), )
if mibBuilder.loadTexts: a3ComBrgSrRDTable.setStatus('mandatory')
a3ComBrgSrRDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1), ).setIndexNames((0, "A3COM-BRIDGE-R3-MIB", "a3ComBrgSrRDPort"))
if mibBuilder.loadTexts: a3ComBrgSrRDEntry.setStatus('mandatory')
a3ComBrgSrRDPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgSrRDPort.setStatus('mandatory')
a3ComBrgSrRDAppleTalk = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("appleTalk", 1), ("noAppleTalk", 2))).clone('noAppleTalk')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrRDAppleTalk.setStatus('mandatory')
a3ComBrgSrRDClnp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clnp", 1), ("noClnp", 2))).clone('noClnp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrRDClnp.setStatus('mandatory')
a3ComBrgSrRDDecNet = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("decNet", 1), ("noDecNet", 2))).clone('noDecNet')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrRDDecNet.setStatus('mandatory')
a3ComBrgSrRDDlTest = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dlTest", 1), ("noDlTest", 2))).clone('noDlTest')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrRDDlTest.setStatus('mandatory')
a3ComBrgSrRDIp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ip", 1), ("noIp", 2))).clone('noIp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrRDIp.setStatus('mandatory')
a3ComBrgSrRDIpx = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipx", 1), ("noIpx", 2))).clone('noIpx')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrRDIpx.setStatus('mandatory')
a3ComBrgSrRDLlc2 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("llc2", 1), ("noLlc2", 2))).clone('noLlc2')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrRDLlc2.setStatus('mandatory')
a3ComBrgSrRDVines = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vines", 1), ("noVines", 2))).clone('noVines')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrgSrRDVines.setStatus('mandatory')
a3ComBrgSrTunVRing = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgSrTunVRing.setStatus('deprecated')
a3ComBrgSrCNodeAddr = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 9, 3, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBrgSrCNodeAddr.setStatus('deprecated')
mibBuilder.exportSymbols("A3COM-BRIDGE-R3-MIB", a3ComBrgX25NbrPort=a3ComBrgX25NbrPort, a3ComBrgSrGwContEncapMode=a3ComBrgSrGwContEncapMode, SMDSAddress=SMDSAddress, a3ComBrgSrPortSTEHopCount=a3ComBrgSrPortSTEHopCount, a3ComBrgFwTblSize=a3ComBrgFwTblSize, a3ComBrgSr=a3ComBrgSr, a3ComBrgSrRDAppleTalk=a3ComBrgSrRDAppleTalk, a3ComBrgLearnCtl=a3ComBrgLearnCtl, a3ComBrgStExtWaAddress=a3ComBrgStExtWaAddress, a3ComBrgPortIndex=a3ComBrgPortIndex, a3ComBrgGen=a3ComBrgGen, a3ComBrgSrCNodeAddr=a3ComBrgSrCNodeAddr, a3ComBrgStExtAdd=a3ComBrgStExtAdd, a3ComBrgSrRDDecNet=a3ComBrgSrRDDecNet, a3ComBrgFdbExtTable=a3ComBrgFdbExtTable, a3ComBrgSrPortHoldTime=a3ComBrgSrPortHoldTime, a3ComBrgStExtTable=a3ComBrgStExtTable, a3ComBrgSrRDIpx=a3ComBrgSrRDIpx, a3ComBrgCtl=a3ComBrgCtl, a3ComBrgFwTblCtl=a3ComBrgFwTblCtl, a3ComBrgStpCtl=a3ComBrgStpCtl, a3ComBrgStpMultAdd=a3ComBrgStpMultAdd, a3ComBrgSmdsGroupAddr=a3ComBrgSmdsGroupAddr, a3ComBrgSrRDClnp=a3ComBrgSrRDClnp, a3ComBrgForwardCtl=a3ComBrgForwardCtl, a3ComBrgX25VcTimer=a3ComBrgX25VcTimer, a3ComBrgSrGwContAutoMode=a3ComBrgSrGwContAutoMode, a3ComBrgSrRDLlc2=a3ComBrgSrRDLlc2, a3ComBrgSrRDEntry=a3ComBrgSrRDEntry, a3ComBrgSrWAportIndex=a3ComBrgSrWAportIndex, a3ComBrgSrGwVirRing=a3ComBrgSrGwVirRing, a3ComBrgBroadCastLimit=a3ComBrgBroadCastLimit, a3ComBrgSrGwContEntry=a3ComBrgSrGwContEntry, RowStatus=RowStatus, a3ComBrgSrPortEntry=a3ComBrgSrPortEntry, a3ComBrgSrPort=a3ComBrgSrPort, a3ComBrgSrGwContTable=a3ComBrgSrGwContTable, a3ComBrgStExtEntry=a3ComBrgStExtEntry, a3ComBrgFdbExtWaAddress=a3ComBrgFdbExtWaAddress, a3ComBrgFdbExtAdd=a3ComBrgFdbExtAdd, a3ComBrgSrRDIp=a3ComBrgSrRDIp, a3ComBrgSrGwCont=a3ComBrgSrGwCont, a3ComBrgStExtRcvPort=a3ComBrgStExtRcvPort, a3ComBridge=a3ComBridge, a3ComBrgX25VcLimit=a3ComBrgX25VcLimit, a3ComBrgPortTable=a3ComBrgPortTable, a3ComBrgAgeCtl=a3ComBrgAgeCtl, a3ComBrgSrRDPort=a3ComBrgSrRDPort, a3ComBrgStpHopCtl=a3ComBrgStpHopCtl, a3ComBrgSrPortMinAccessPrior=a3ComBrgSrPortMinAccessPrior, a3ComBrgSrRDTable=a3ComBrgSrRDTable, a3ComBrgX25ProfId=a3ComBrgX25ProfId, a3Com=a3Com, a3ComBrgPortEntry=a3ComBrgPortEntry, a3ComBrgSrMode=a3ComBrgSrMode, a3ComBrgFwallCtl=a3ComBrgFwallCtl, a3ComBrgAppleCtl=a3ComBrgAppleCtl, a3ComBrgX25NbrTable=a3ComBrgX25NbrTable, a3ComBrgSrWanAddrEntry=a3ComBrgSrWanAddrEntry, a3ComBrgX25NbrEntry=a3ComBrgX25NbrEntry, a3ComBrgX25NbrDTE=a3ComBrgX25NbrDTE, a3ComBrgSrWanAddrTable=a3ComBrgSrWanAddrTable, a3ComBrgStp=a3ComBrgStp, a3ComBrgSrGwContPort=a3ComBrgSrGwContPort, a3ComBrgSrTunVRing=a3ComBrgSrTunVRing, X121Address=X121Address, a3ComBrgSrWAbrgNum=a3ComBrgSrWAbrgNum, a3ComBrgDstSecCtl=a3ComBrgDstSecCtl, a3ComBrgSrPortTable=a3ComBrgSrPortTable, a3ComBrgSrRDVines=a3ComBrgSrRDVines, a3ComBrgX25Qsize=a3ComBrgX25Qsize, a3ComBrgSrcSecCtl=a3ComBrgSrcSecCtl, a3ComBrgFdbExtEntry=a3ComBrgFdbExtEntry, a3ComBrgSrRDDlTest=a3ComBrgSrRDDlTest, a3ComBrgSrWAddress=a3ComBrgSrWAddress, a3ComBrgX25NbrStatus=a3ComBrgX25NbrStatus, a3ComBrgPortCtl=a3ComBrgPortCtl, brouterMIB=brouterMIB, a3ComBrgBLimitTimer=a3ComBrgBLimitTimer, a3ComBrgSrWAringNum=a3ComBrgSrWAringNum, a3ComBrgX25Pid=a3ComBrgX25Pid, a3ComBrgSrPortAREHopCount=a3ComBrgSrPortAREHopCount)