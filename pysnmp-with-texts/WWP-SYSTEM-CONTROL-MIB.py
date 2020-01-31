#
# PySNMP MIB module WWP-SYSTEM-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-SYSTEM-CONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
dot1dStpPort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPort")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter64, Integer32, Counter32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, ModuleIdentity, Bits, iso, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Integer32", "Counter32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "ModuleIdentity", "Bits", "iso", "NotificationType", "IpAddress")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpSysCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 30))
wwpSysCtrlMIB.setRevisions(('2001-04-03 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpSysCtrlMIB.setRevisionsDescriptions(('Initial creation.',))
if mibBuilder.loadTexts: wwpSysCtrlMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpSysCtrlMIB.setOrganization('World Wide Packets, Inc')
if mibBuilder.loadTexts: wwpSysCtrlMIB.setContactInfo(' Mib Meister Postal: World Wide Packets P.O. Box 950 Veradale, WA 99037 USA Phone: +1 509 242 9000 Email: mib.meister@worldwidepackets.com')
if mibBuilder.loadTexts: wwpSysCtrlMIB.setDescription('The MIB module for the WWP SysCtrl specific information.')
wwpSysCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1))
wwpSysCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1))
wwpSysCtrlMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 2))
wwpSysCtrlMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 2, 0))
wwpSysCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 3))
wwpSysCtrlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 3, 1))
wwpSysCtrlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 3, 2))
wwpSysCtrlBridgeRSTPEnable = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpSysCtrlBridgeRSTPEnable.setStatus('current')
if mibBuilder.loadTexts: wwpSysCtrlBridgeRSTPEnable.setDescription("when this object is set to 'true' the rstp operation for the bridge is enabled. Setting this object to 'false' disable bridge rstp operations.")
wwpSysCtrlLacpEnable = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpSysCtrlLacpEnable.setStatus('current')
if mibBuilder.loadTexts: wwpSysCtrlLacpEnable.setDescription("when this object is set to 'true' the Lacp operation for the device is enabled. Setting this object to 'false' disable the Lacp operations.")
wwpPvstBpduReceived = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 30, 2, 0, 1)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: wwpPvstBpduReceived.setStatus('current')
if mibBuilder.loadTexts: wwpPvstBpduReceived.setDescription('A wwpPvstBpduReceived trap signifies that the SNMP entity, acting in an agent role, has detected that a Per Vlan Spanning Tree (PVST) BPDU was received on one of the ports sepcified by dot1dStpPort.')
mibBuilder.exportSymbols("WWP-SYSTEM-CONTROL-MIB", wwpSysCtrlMIBNotifications=wwpSysCtrlMIBNotifications, wwpSysCtrl=wwpSysCtrl, wwpSysCtrlMIBCompliances=wwpSysCtrlMIBCompliances, wwpSysCtrlMIB=wwpSysCtrlMIB, wwpPvstBpduReceived=wwpPvstBpduReceived, wwpSysCtrlMIBObjects=wwpSysCtrlMIBObjects, PYSNMP_MODULE_ID=wwpSysCtrlMIB, wwpSysCtrlLacpEnable=wwpSysCtrlLacpEnable, wwpSysCtrlMIBConformance=wwpSysCtrlMIBConformance, wwpSysCtrlMIBGroups=wwpSysCtrlMIBGroups, wwpSysCtrlMIBNotificationPrefix=wwpSysCtrlMIBNotificationPrefix, wwpSysCtrlBridgeRSTPEnable=wwpSysCtrlBridgeRSTPEnable)