#
# PySNMP MIB module CISCO-WAN-FEEDER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-FEEDER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:20:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, IpAddress, Unsigned32, TimeTicks, Counter64, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, MibIdentifier, ModuleIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Unsigned32", "TimeTicks", "Counter64", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "MibIdentifier", "ModuleIdentity", "Bits", "Counter32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ciscoWanFeederMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 15))
ciscoWanFeederMIB.setRevisions(('2003-03-27 00:00', '2000-10-10 00:00', '2000-04-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanFeederMIB.setRevisionsDescriptions(('Fixed alignments and descriptions.', 'Added cwfLMIType object to distinguish feeder versus XLMI. Added enum fdrNON to cwfFeederType object.', 'Initial version of feeder MIB module.',))
if mibBuilder.loadTexts: ciscoWanFeederMIB.setLastUpdated('200303270000Z')
if mibBuilder.loadTexts: ciscoWanFeederMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanFeederMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanFeederMIB.setDescription('This MIB is used for configuring a port on an ATM switch module to be aware of feeder connection information. Terminology: AR - Auto Route, a CISCO proprietary feature, provides connection management for network with only CISCO nodes such as BPX or IGX. Feeder - An external ATM switch, which does not have PNNI feature, connected to an ATM switch that supports PNNI to provide LMI. LMI - Local Management Interface is an interface to provide a set of enhancements to Frame Relay specification for managing complex internetworks. LMI extensions include global addressing, virtual-circuit status messages, and multicasting. XLMI - The Extended LMI is a type of LMI which is implemented in an AR + PNNI network.')
cwfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 15, 1))
cwfFeeder = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1))
cwfFeederTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1), )
if mibBuilder.loadTexts: cwfFeederTable.setStatus('current')
if mibBuilder.loadTexts: cwfFeederTable.setDescription('This table contains the entries for the feeders. It is used for addition or deletion of feeders and to support LMI on the feeders. The information in these entries are advertised to LMI using a system dependent implementation when an entry is created/activated. This table can also be applicable to XLMI.')
cwfFeederEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-FEEDER-MIB", "cwfFeederIfNum"))
if mibBuilder.loadTexts: cwfFeederEntry.setStatus('current')
if mibBuilder.loadTexts: cwfFeederEntry.setDescription('An entry in cwfFeederTable.')
cwfFeederIfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cwfFeederIfNum.setStatus('current')
if mibBuilder.loadTexts: cwfFeederIfNum.setDescription('This is an unique interface number of an ATM virtual interface. The value of this object is equal to the ifIndex of the ATM virtual interface interface identified by ifType atmVirtual(149).')
cwfFeederName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwfFeederName.setStatus('current')
if mibBuilder.loadTexts: cwfFeederName.setDescription('This is the name of the feeder. It contains a string of length zero, if the feeder name is not available.')
cwfLanIP = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwfLanIP.setStatus('current')
if mibBuilder.loadTexts: cwfLanIP.setDescription('This is the LAN IP address of the feeder. This IP address is used for ethernet interface.')
cwfNetIP = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwfNetIP.setStatus('current')
if mibBuilder.loadTexts: cwfNetIP.setDescription('This is the network IP address of the feeder. This IP address is used for ATM interface.')
cwfRemoteShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwfRemoteShelf.setStatus('current')
if mibBuilder.loadTexts: cwfRemoteShelf.setDescription('This is the remote shelf number of the feeder module.')
cwfRemoteSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwfRemoteSlot.setStatus('current')
if mibBuilder.loadTexts: cwfRemoteSlot.setDescription('This is the remote slot number of the feeder module.')
cwfRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwfRemotePort.setStatus('current')
if mibBuilder.loadTexts: cwfRemotePort.setDescription('This is the remote physical port(line) number of the feeder module.')
cwfFeederType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("fdrIPX", 1), ("fdrBPX", 2), ("fdrIpxAF", 3), ("fdrBASIS", 4), ("fdrUNKNOWN", 5), ("fdrUNI", 6), ("fdrAPS", 7), ("fdrIGX", 8), ("fdrIgxAF", 9), ("fdrVSI", 10), ("fdrPAR", 11), ("fdrNON", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwfFeederType.setStatus('current')
if mibBuilder.loadTexts: cwfFeederType.setDescription('This identifies the feeeder type. fdrNON(12) is applicable when cwfLMIType is xLMI(2). Other values are applicable for cwfLMIType = feeder(1). The possible values are: fdrIPX -- Feeder is an IPX node in a routing network fdrBPX -- Feeder is an BPX node in a routing network fdrIpxAF -- Feeder is a stand-alone IPX node fdrBASIS -- Feeder is a stand-alone BASIS node fdrUNKNOWN -- Feeder is unknown fdrUNI -- Feeder is a UNI AIT (phase 0) fdrAPS -- Feeder is an APS (Adjunct Processor Shelf) fdrIGX -- Feeder is an IGX node in a routing network fdrIgxAF -- Feeder is a stand-alone IGX node fdrVSI -- Feeder is an VSI Controller fdrPAR -- Feeder is a PAR fdrNON -- Non-feeder type')
cwfModelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwfModelNumber.setStatus('current')
if mibBuilder.loadTexts: cwfModelNumber.setDescription('This identifies the feeder model number.')
cwfLMIAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwfLMIAdminStatus.setStatus('current')
if mibBuilder.loadTexts: cwfLMIAdminStatus.setDescription('This provides the feeder LMI admin state configuration capabilities for the desired state of interface. The value of this object is ignored during row creation.')
cwfLMIOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwfLMIOperStatus.setStatus('current')
if mibBuilder.loadTexts: cwfLMIOperStatus.setDescription('This provides the operational state of the LMI connection.')
cwfFeederNodeAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("clear", 1), ("minor", 2), ("major", 3), ("critical", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwfFeederNodeAlarm.setStatus('current')
if mibBuilder.loadTexts: cwfFeederNodeAlarm.setDescription('This identifies the feeder node alarm status. It provides the alarm status in hierarchical order where by if there are no feeder node alarms, it is signified by <clear>. If minor alarms, with no major alarms, it is signified by <minor>. If the node has one or more major alarms, irrespective of the minor alarm status, then it is signified by <major>.')
cwfFeederRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwfFeederRowStatus.setStatus('current')
if mibBuilder.loadTexts: cwfFeederRowStatus.setDescription("This is used for adding or deleting a feeder entry. The row can be created by setting this object to 'createAndGo(4)'. The row can be deleted by setting this object to 'destroy(6)'. No other values are supported.")
cwfLMIType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("feeder", 1), ("xLMI", 2))).clone('feeder')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwfLMIType.setStatus('current')
if mibBuilder.loadTexts: cwfLMIType.setDescription('This identifies the LMI type. It identifies the type of network to which the LMI port is connected to.')
cwfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 15, 3))
cwfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 1))
cwfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 2))
cwfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 1, 1)).setObjects(("CISCO-WAN-FEEDER-MIB", "cwfFeederGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwfMIBCompliance = cwfMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cwfMIBCompliance.setDescription('The compliance statement for feeder group.')
cwfMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 1, 2)).setObjects(("CISCO-WAN-FEEDER-MIB", "cwfFeederGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwfMIBCompliance2 = cwfMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: cwfMIBCompliance2.setDescription('The Compliance statement for feeder group.')
cwfFeederGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 2, 1)).setObjects(("CISCO-WAN-FEEDER-MIB", "cwfFeederName"), ("CISCO-WAN-FEEDER-MIB", "cwfLanIP"), ("CISCO-WAN-FEEDER-MIB", "cwfNetIP"), ("CISCO-WAN-FEEDER-MIB", "cwfRemoteShelf"), ("CISCO-WAN-FEEDER-MIB", "cwfRemoteSlot"), ("CISCO-WAN-FEEDER-MIB", "cwfRemotePort"), ("CISCO-WAN-FEEDER-MIB", "cwfFeederType"), ("CISCO-WAN-FEEDER-MIB", "cwfModelNumber"), ("CISCO-WAN-FEEDER-MIB", "cwfLMIAdminStatus"), ("CISCO-WAN-FEEDER-MIB", "cwfLMIOperStatus"), ("CISCO-WAN-FEEDER-MIB", "cwfFeederNodeAlarm"), ("CISCO-WAN-FEEDER-MIB", "cwfFeederRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwfFeederGroup = cwfFeederGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cwfFeederGroup.setDescription('The objects related to configuring a feeder.')
cwfFeederGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 2, 2)).setObjects(("CISCO-WAN-FEEDER-MIB", "cwfFeederName"), ("CISCO-WAN-FEEDER-MIB", "cwfLanIP"), ("CISCO-WAN-FEEDER-MIB", "cwfNetIP"), ("CISCO-WAN-FEEDER-MIB", "cwfRemoteShelf"), ("CISCO-WAN-FEEDER-MIB", "cwfRemoteSlot"), ("CISCO-WAN-FEEDER-MIB", "cwfRemotePort"), ("CISCO-WAN-FEEDER-MIB", "cwfFeederType"), ("CISCO-WAN-FEEDER-MIB", "cwfModelNumber"), ("CISCO-WAN-FEEDER-MIB", "cwfLMIAdminStatus"), ("CISCO-WAN-FEEDER-MIB", "cwfLMIOperStatus"), ("CISCO-WAN-FEEDER-MIB", "cwfFeederNodeAlarm"), ("CISCO-WAN-FEEDER-MIB", "cwfFeederRowStatus"), ("CISCO-WAN-FEEDER-MIB", "cwfLMIType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwfFeederGroup2 = cwfFeederGroup2.setStatus('current')
if mibBuilder.loadTexts: cwfFeederGroup2.setDescription('The objects related to configuring feeder and non-feeder(XLMI).')
mibBuilder.exportSymbols("CISCO-WAN-FEEDER-MIB", cwfFeederRowStatus=cwfFeederRowStatus, cwfMIBConformance=cwfMIBConformance, cwfFeederName=cwfFeederName, cwfRemoteSlot=cwfRemoteSlot, cwfFeederEntry=cwfFeederEntry, cwfRemotePort=cwfRemotePort, cwfMIBObjects=cwfMIBObjects, cwfFeederIfNum=cwfFeederIfNum, cwfNetIP=cwfNetIP, cwfMIBCompliance=cwfMIBCompliance, cwfMIBCompliances=cwfMIBCompliances, cwfMIBGroups=cwfMIBGroups, cwfFeeder=cwfFeeder, PYSNMP_MODULE_ID=ciscoWanFeederMIB, cwfLMIAdminStatus=cwfLMIAdminStatus, cwfFeederType=cwfFeederType, cwfMIBCompliance2=cwfMIBCompliance2, cwfRemoteShelf=cwfRemoteShelf, cwfFeederGroup=cwfFeederGroup, cwfFeederNodeAlarm=cwfFeederNodeAlarm, cwfLMIType=cwfLMIType, cwfLanIP=cwfLanIP, cwfLMIOperStatus=cwfLMIOperStatus, cwfFeederGroup2=cwfFeederGroup2, cwfFeederTable=cwfFeederTable, cwfModelNumber=cwfModelNumber, ciscoWanFeederMIB=ciscoWanFeederMIB)