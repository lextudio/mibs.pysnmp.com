#
# PySNMP MIB module CISCO-FABRICPATH-TOPOLOGY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FABRICPATH-TOPOLOGY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:57:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Cisco2KVlanList, = mibBuilder.importSymbols("CISCO-TC", "Cisco2KVlanList")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Bits, ModuleIdentity, Counter32, Counter64, IpAddress, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ModuleIdentity", "Counter32", "Counter64", "IpAddress", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Gauge32")
TextualConvention, DisplayString, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "StorageType")
ciscoFabricPathTopologyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 801))
ciscoFabricPathTopologyMIB.setRevisions(('2013-03-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFabricPathTopologyMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFabricPathTopologyMIB.setLastUpdated('201303110000Z')
if mibBuilder.loadTexts: ciscoFabricPathTopologyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFabricPathTopologyMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoFabricPathTopologyMIB.setDescription("This MIB module defines managed objects that facilitate the management of Cisco's FabricPath Topology technology.")
ciscoFabricPathTopologyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 801, 0))
ciscoFabricPathTopologyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 801, 1))
ciscoFabricPathTopologyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 801, 2))
cfptTopologyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1), )
if mibBuilder.loadTexts: cfptTopologyTable.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyTable.setDescription('A table containing a list of FabricPath topology information.')
cfptTopologyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1), ).setIndexNames((0, "CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIndex"))
if mibBuilder.loadTexts: cfptTopologyEntry.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyEntry.setDescription('An entry containing management information of a particular FabricPath topology. An entry is created for each FabricPath topology that is managed by the system.')
cfptTopologyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfptTopologyIndex.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIndex.setDescription('An identifier that uniquely identifies a FabricPath topology.')
cfptTopologyDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfptTopologyDescr.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyDescr.setDescription('This object specifies the description of the FabricPath topology.')
cfptTopologyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyState.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyState.setDescription('This object indicates the state of the FabricPath topology. other - none of the followings up - topology is up down - topology is down')
cfptTopologyStateChangeReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyStateChangeReason.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyStateChangeReason.setDescription('This object indicates the reason of the current topology state that cfptTopologyState provides.')
cfptTopologyVlansFirst2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 5), Cisco2KVlanList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfptTopologyVlansFirst2K.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyVlansFirst2K.setDescription("A string of octets containing one bit per VLAN for VLANs 0 to 2047 that are configured for this FabricPath topology entry. If the bit corresponding to a VLAN is set to '1', then the VLAN is configured in this FabricPath topology. If the bit is set to '0', then the VLAN is not configured in this FabricPath topology.")
cfptTopologyVlansSecond2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 6), Cisco2KVlanList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfptTopologyVlansSecond2K.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyVlansSecond2K.setDescription("A string of octets containing one bit per VLAN for VLANs 2048 to 4095 that are configured for this FabricPath topology entry. If the bit corresponding to a VLAN is set to '1', then the VLAN is configured in this FabricPath topology. If the bit is set to '0', then the VLAN is not configured in this FabricPath topology.")
cfptTopologyActiveVlansFirst2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 7), Cisco2KVlanList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyActiveVlansFirst2K.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyActiveVlansFirst2K.setDescription("A string of octets containing one bit per VLAN for VLANs 0 to 2047 that are active in this FabricPath topology entry. If the bit corresponding to a VLAN is set to '1', then the VLAN is active in this FabricPath topology. If the bit is set to '0', then the VLAN is not configured in this FabricPath topology.")
cfptTopologyActiveVlansSecond2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 8), Cisco2KVlanList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyActiveVlansSecond2K.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyActiveVlansSecond2K.setDescription("A string of octets containing one bit per VLAN for VLANs 2048 to 4095 that are active in this FabricPath topology entry. If the bit corresponding to a VLAN is set to '1', then the VLAN is active in this FabricPath topology. If the bit is set to '0', then the VLAN is not active in this FabricPath topology.")
cfptTopologyStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 9), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfptTopologyStorageType.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyStorageType.setDescription('This object specifies the storage type for this conceptual row.')
cfptTopologyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfptTopologyRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyRowStatus.setDescription("The status of this conceptual row entry. This object is used to manage creation and deletion of rows in this table. When this object value is 'active', other writable objects in the same row may be modified.")
cfptTopologyIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2), )
if mibBuilder.loadTexts: cfptTopologyIfTable.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfTable.setDescription('A table containing a list of all FabricPath topology interfaces.')
cfptTopologyIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2, 1), ).setIndexNames((0, "CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfTopoIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cfptTopologyIfEntry.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfEntry.setDescription('An entry containing information of one interface in a FabricPath topology. An entry is created for a FabricPath capable interface that is a member of a particular FabricPath topology.')
cfptTopologyIfTopoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfptTopologyIfTopoIndex.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfTopoIndex.setDescription('An identifier that uniquely identifies a FabricPath topology interface.')
cfptTopologyIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyIfState.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfState.setDescription('This object indicates the state of a given FabricPath topology interface. other - none of the followings up - interface is up down - interface is down')
cfptTopologyIfStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfptTopologyIfStorageType.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfStorageType.setDescription('The objects specifies the storage type for this conceptual row.')
cfptTopologyIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfptTopologyIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfRowStatus.setDescription('The status of this conceptual row entry. This object is used to manage creation and deletion of rows in this table.')
cfptTopologyIfVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3), )
if mibBuilder.loadTexts: cfptTopologyIfVlanTable.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfVlanTable.setDescription('A table containing a list of FabricPath interfaces and their VLAN information.')
cfptTopologyIfVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cfptTopologyIfVlanEntry.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfVlanEntry.setDescription('An entry containing VLAN information for each FabricPath interface. An entry is created for each FabricPath topology interface.')
cfptTopologyIfVlansFirst2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3, 1, 1), Cisco2KVlanList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyIfVlansFirst2K.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfVlansFirst2K.setDescription("A string of octets containing one bit per VLAN for VLANs 0 through 2047 that are configured for the FabricPath interface specified by ifIndex in this entry. If the bit corresponding to a VLAN is set to '1', then the VLAN is configured for the interface, it is not otherwise.")
cfptTopologyIfVlansSecond2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3, 1, 2), Cisco2KVlanList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyIfVlansSecond2K.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfVlansSecond2K.setDescription("A string of octets containing one bit per VLAN for VLANs 2048 through 4095 that are configured for the FabricPath interface specified by ifIndex in this entry. If the bit corresponding to a VLAN is set to '1', then the VLAN is configured for the interface, it is not otherwise.")
cfptTopologyIfActiveVlansFirst2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3, 1, 3), Cisco2KVlanList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyIfActiveVlansFirst2K.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfActiveVlansFirst2K.setDescription("A string of octets containing one bit per VLAN for VLANs 0 through 2047 that are operational on the FabricPath interface specified by ifIndex in this entry. If the bit corresponding to a VLAN is set to '1', then the VLAN is active on the interface, it is not otherwise.")
cfptTopologyIfActiveVlansSecond2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3, 1, 4), Cisco2KVlanList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyIfActiveVlansSecond2K.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfActiveVlansSecond2K.setDescription("A string of octets containing one bit per VLAN for VLANs 2048 through 4095 that are operational on the FabricPath interface specified by ifIndex in this entry. If the bit corresponding to a VLAN is set to '1', then the VLAN is active on the interface, it is not otherwise.")
cfptTopologyTreeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4), )
if mibBuilder.loadTexts: cfptTopologyTreeTable.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyTreeTable.setDescription('A table containing a list of forwarding tree information of the FabricPath topologies.')
cfptTopologyTreeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4, 1), ).setIndexNames((0, "CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIndex"), (0, "CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyTreeId"))
if mibBuilder.loadTexts: cfptTopologyTreeEntry.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyTreeEntry.setDescription('An entry containing one forwarding tree information in a particular FabricPath topology.')
cfptTopologyTreeId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfptTopologyTreeId.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyTreeId.setDescription('An index number that uniquely identifies forwarding tree of a particular FabricPath topology.')
cfptTopologyTreeFtag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyTreeFtag.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyTreeFtag.setDescription("This object indicates the tree's forwarding tag.")
cfptTopologyTreeState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyTreeState.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyTreeState.setDescription('This object indicates the state of the tree. other - none of the followings active - the tree is active inactive - the tree is inactive.')
cfptTopologyTreeType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("mixed", 2), ("multicast", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfptTopologyTreeType.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyTreeType.setDescription('This object indicates the type of the tree. other - none of the followings mixed - unknown unicast, broadcast and multicast tree multicast - multicast tree')
cfptFabricPathTopologyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 1))
cfptFabricPathTopologyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 2))
cfptFabricPathTopologyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 1, 1)).setObjects(("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyGroup"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfGroup"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfVlanGroup"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyTreeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfptFabricPathTopologyMIBCompliance = cfptFabricPathTopologyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cfptFabricPathTopologyMIBCompliance.setDescription('Describes the requirements for conformance to the CISCO-FABRICPATH-TOPOLOGY-MIB.')
cfptTopologyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 2, 1)).setObjects(("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyDescr"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyState"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyStateChangeReason"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyVlansFirst2K"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyVlansSecond2K"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyActiveVlansFirst2K"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyActiveVlansSecond2K"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyStorageType"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfptTopologyGroup = cfptTopologyGroup.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyGroup.setDescription('A collection of objects providing FabricPath topology information.')
cfptTopologyIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 2, 2)).setObjects(("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfState"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfStorageType"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfptTopologyIfGroup = cfptTopologyIfGroup.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfGroup.setDescription('A collection of objects providing per interface FabricPath topology information.')
cfptTopologyIfVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 2, 3)).setObjects(("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfVlansFirst2K"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfVlansSecond2K"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfActiveVlansFirst2K"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfActiveVlansSecond2K"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfptTopologyIfVlanGroup = cfptTopologyIfVlanGroup.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyIfVlanGroup.setDescription('A collection of objects providing VLAN information for each FabricPath interface.')
cfptTopologyTreeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 2, 4)).setObjects(("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyTreeFtag"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyTreeState"), ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyTreeType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfptTopologyTreeGroup = cfptTopologyTreeGroup.setStatus('current')
if mibBuilder.loadTexts: cfptTopologyTreeGroup.setDescription('A collection of objects providing FabricPath topology forwarding tree information.')
mibBuilder.exportSymbols("CISCO-FABRICPATH-TOPOLOGY-MIB", cfptTopologyTreeTable=cfptTopologyTreeTable, cfptTopologyRowStatus=cfptTopologyRowStatus, cfptTopologyTreeType=cfptTopologyTreeType, cfptTopologyIfGroup=cfptTopologyIfGroup, cfptTopologyEntry=cfptTopologyEntry, cfptFabricPathTopologyMIBGroups=cfptFabricPathTopologyMIBGroups, cfptTopologyDescr=cfptTopologyDescr, cfptTopologyActiveVlansFirst2K=cfptTopologyActiveVlansFirst2K, cfptTopologyActiveVlansSecond2K=cfptTopologyActiveVlansSecond2K, cfptTopologyVlansFirst2K=cfptTopologyVlansFirst2K, ciscoFabricPathTopologyMIBConformance=ciscoFabricPathTopologyMIBConformance, cfptTopologyTreeId=cfptTopologyTreeId, cfptTopologyIfVlanEntry=cfptTopologyIfVlanEntry, cfptTopologyTable=cfptTopologyTable, cfptTopologyIndex=cfptTopologyIndex, cfptTopologyIfEntry=cfptTopologyIfEntry, cfptTopologyTreeFtag=cfptTopologyTreeFtag, cfptFabricPathTopologyMIBCompliances=cfptFabricPathTopologyMIBCompliances, cfptTopologyIfVlanTable=cfptTopologyIfVlanTable, cfptTopologyIfTopoIndex=cfptTopologyIfTopoIndex, cfptTopologyIfVlansSecond2K=cfptTopologyIfVlansSecond2K, cfptTopologyStateChangeReason=cfptTopologyStateChangeReason, cfptTopologyTreeGroup=cfptTopologyTreeGroup, cfptTopologyIfTable=cfptTopologyIfTable, ciscoFabricPathTopologyMIB=ciscoFabricPathTopologyMIB, cfptFabricPathTopologyMIBCompliance=cfptFabricPathTopologyMIBCompliance, cfptTopologyGroup=cfptTopologyGroup, cfptTopologyTreeEntry=cfptTopologyTreeEntry, cfptTopologyIfState=cfptTopologyIfState, ciscoFabricPathTopologyMIBObjects=ciscoFabricPathTopologyMIBObjects, cfptTopologyTreeState=cfptTopologyTreeState, cfptTopologyIfVlanGroup=cfptTopologyIfVlanGroup, cfptTopologyIfActiveVlansSecond2K=cfptTopologyIfActiveVlansSecond2K, ciscoFabricPathTopologyMIBNotifs=ciscoFabricPathTopologyMIBNotifs, cfptTopologyIfRowStatus=cfptTopologyIfRowStatus, cfptTopologyIfActiveVlansFirst2K=cfptTopologyIfActiveVlansFirst2K, cfptTopologyIfStorageType=cfptTopologyIfStorageType, PYSNMP_MODULE_ID=ciscoFabricPathTopologyMIB, cfptTopologyVlansSecond2K=cfptTopologyVlansSecond2K, cfptTopologyState=cfptTopologyState, cfptTopologyIfVlansFirst2K=cfptTopologyIfVlansFirst2K, cfptTopologyStorageType=cfptTopologyStorageType)