#
# PySNMP MIB module FDRY-DHCP-SNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDRY-DHCP-SNOOPING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ArpType, ArpState = mibBuilder.importSymbols("FDRY-DAI-MIB", "ArpType", "ArpState")
DisplayString, = mibBuilder.importSymbols("FOUNDRY-SN-AGENT-MIB", "DisplayString")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter32, IpAddress, MibIdentifier, ObjectIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Integer32, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Integer32", "Gauge32", "Unsigned32")
TruthValue, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "TextualConvention")
fdryDhcpSnoopMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36))
fdryDhcpSnoopMIB.setRevisions(('2010-07-26 00:00', '2010-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fdryDhcpSnoopMIB.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', '',))
if mibBuilder.loadTexts: fdryDhcpSnoopMIB.setLastUpdated('201007260000Z')
if mibBuilder.loadTexts: fdryDhcpSnoopMIB.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: fdryDhcpSnoopMIB.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: fdryDhcpSnoopMIB.setDescription("Management Information for configuration of DHCP Snooping feature. DHCP Snooping is a security feature which enables the device to filter untrusted DHCP packets in a subnet. It can also stop unauthorized DHCP serves and prevent errors due to user mis-configuration servers. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
class ClearAction(TextualConvention, Integer32):
    description = 'Represents action of Clear operation to be used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("valid", 0), ("clear", 1))

fdryDhcpSnoopGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 1))
fdryDhcpSnoopVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2))
fdryDhcpSnoopInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3))
fdryDhcpSnoopBind = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4))
fdryDhcpSnoopGlobalClearOper = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 1, 1), ClearAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryDhcpSnoopGlobalClearOper.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopGlobalClearOper.setDescription('valid(0) - this value is always returned when the variable is read. clear(1) - setting the variable to this value clears all entries in the DHCP binding database.')
fdryDhcpSnoopVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1), )
if mibBuilder.loadTexts: fdryDhcpSnoopVlanConfigTable.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopVlanConfigTable.setDescription('A table provides the mechanism to control DHCP Snooping per VLAN. When a VLAN is created in a device supporting this table, a corresponding entry of this table will be added.')
fdryDhcpSnoopVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1, 1), ).setIndexNames((0, "FDRY-DHCP-SNOOPING-MIB", "fdryDhcpSnoopVlanVLanId"))
if mibBuilder.loadTexts: fdryDhcpSnoopVlanConfigEntry.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopVlanConfigEntry.setDescription('A row instance contains the configuration to enable or disable DHCP Snooping at the existing VLAN.')
fdryDhcpSnoopVlanVLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1, 1, 1), VlanIndex())
if mibBuilder.loadTexts: fdryDhcpSnoopVlanVLanId.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopVlanVLanId.setDescription('This object indicates the VLAN number on which DHCP Snooping feature is configured.')
fdryDhcpSnoopVlanDhcpSnoopEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryDhcpSnoopVlanDhcpSnoopEnable.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopVlanDhcpSnoopEnable.setDescription("This object indicates whether DHCP Snooping is enabled in this VLAN. If this object is set to 'true', DHCP Snooping is enabled. If this object is set to 'false', DHCP Snooping is disabled.")
fdryDhcpSnoopIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3, 1), )
if mibBuilder.loadTexts: fdryDhcpSnoopIfConfigTable.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopIfConfigTable.setDescription('A table provides the mechanism to configure the trust state for DHCP Snooping purpose at each physical interface.')
fdryDhcpSnoopIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fdryDhcpSnoopIfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopIfConfigEntry.setDescription('A row instance contains the configuration to enable or disable trust state for DHCP Snooping at each physical interface capable of this feature.')
fdryDhcpSnoopIfTrustValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryDhcpSnoopIfTrustValue.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopIfTrustValue.setDescription("This object indicates whether the interface is trusted for DHCP Snooping. If this object is set to 'true', the interface is trusted. DHCP packets coming to this interface will be forwarded without checking. If this object is set to 'false', the interface is not trusted. DHCP packets received on this interface will be subjected to DHCP checks.")
fdryDhcpSnoopBindTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1), )
if mibBuilder.loadTexts: fdryDhcpSnoopBindTable.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopBindTable.setDescription('A table provides the information of DHCP snooping binding database learnt by the device')
fdryDhcpSnoopBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1), ).setIndexNames((0, "FDRY-DHCP-SNOOPING-MIB", "fdryDhcpSnoopBindIpAddr"))
if mibBuilder.loadTexts: fdryDhcpSnoopBindEntry.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopBindEntry.setDescription('A row instance contains the information of DHCP snoonping entry.')
fdryDhcpSnoopBindIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: fdryDhcpSnoopBindIpAddr.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopBindIpAddr.setDescription('The device IP address.')
fdryDhcpSnoopBindMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryDhcpSnoopBindMacAddr.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopBindMacAddr.setDescription('The device MAC address.')
fdryDhcpSnoopBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 3), ArpType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryDhcpSnoopBindType.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopBindType.setDescription('The type of the ARP entry')
fdryDhcpSnoopBindState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 4), ArpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryDhcpSnoopBindState.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopBindState.setDescription('The state of the ARP entry')
fdryDhcpSnoopBindPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryDhcpSnoopBindPort.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopBindPort.setDescription('The port of the ARP entry')
fdryDhcpSnoopBindVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 6), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryDhcpSnoopBindVlanId.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopBindVlanId.setDescription('This object indicates the VLAN number on which DHCP snooping feature is configured.')
fdryDhcpSnoopBindClearOper = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 7), ClearAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryDhcpSnoopBindClearOper.setStatus('current')
if mibBuilder.loadTexts: fdryDhcpSnoopBindClearOper.setDescription('valid(0) - this value is always returned when the variable is read. clear(1) - setting the variable to this value clears this entry in the DHCP binding database.')
mibBuilder.exportSymbols("FDRY-DHCP-SNOOPING-MIB", fdryDhcpSnoopVlanVLanId=fdryDhcpSnoopVlanVLanId, fdryDhcpSnoopBindMacAddr=fdryDhcpSnoopBindMacAddr, fdryDhcpSnoopIfConfigEntry=fdryDhcpSnoopIfConfigEntry, fdryDhcpSnoopBindVlanId=fdryDhcpSnoopBindVlanId, fdryDhcpSnoopBindType=fdryDhcpSnoopBindType, fdryDhcpSnoopBindState=fdryDhcpSnoopBindState, fdryDhcpSnoopBindIpAddr=fdryDhcpSnoopBindIpAddr, fdryDhcpSnoopBind=fdryDhcpSnoopBind, fdryDhcpSnoopMIB=fdryDhcpSnoopMIB, fdryDhcpSnoopGlobalObjects=fdryDhcpSnoopGlobalObjects, fdryDhcpSnoopBindEntry=fdryDhcpSnoopBindEntry, fdryDhcpSnoopBindClearOper=fdryDhcpSnoopBindClearOper, fdryDhcpSnoopBindTable=fdryDhcpSnoopBindTable, fdryDhcpSnoopInterface=fdryDhcpSnoopInterface, fdryDhcpSnoopVlanConfigTable=fdryDhcpSnoopVlanConfigTable, fdryDhcpSnoopGlobalClearOper=fdryDhcpSnoopGlobalClearOper, fdryDhcpSnoopVlanDhcpSnoopEnable=fdryDhcpSnoopVlanDhcpSnoopEnable, fdryDhcpSnoopVlan=fdryDhcpSnoopVlan, ClearAction=ClearAction, PYSNMP_MODULE_ID=fdryDhcpSnoopMIB, fdryDhcpSnoopIfConfigTable=fdryDhcpSnoopIfConfigTable, fdryDhcpSnoopBindPort=fdryDhcpSnoopBindPort, fdryDhcpSnoopVlanConfigEntry=fdryDhcpSnoopVlanConfigEntry, fdryDhcpSnoopIfTrustValue=fdryDhcpSnoopIfTrustValue)