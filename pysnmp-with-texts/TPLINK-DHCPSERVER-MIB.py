#
# PySNMP MIB module TPLINK-DHCPSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-DHCPSERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, IpAddress, TimeTicks, Counter64, ModuleIdentity, Bits, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "IpAddress", "TimeTicks", "Counter64", "ModuleIdentity", "Bits", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tplinkDhcpServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 38))
tplinkDhcpServerMIB.setRevisions(('2012-11-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkDhcpServerMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkDhcpServerMIB.setLastUpdated('201211290000Z')
if mibBuilder.loadTexts: tplinkDhcpServerMIB.setOrganization('TP-LINK')
if mibBuilder.loadTexts: tplinkDhcpServerMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkDhcpServerMIB.setDescription('This MIB module contain a collection of managed objects that apply to network devices with Dhcp Server function.')
tplinkDhcpServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1))
tplinkDhcpServerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 38, 2))
tpDhcpServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerEnable.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerEnable.setDescription('Select Enable/Disable DHCP server function globally on the Switch.')
tpDhcpServerVendorClassId = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerVendorClassId.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerVendorClassId.setDescription('Configure DHCP option 60 field.')
tpDhcpServerCapwapAcIp = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerCapwapAcIp.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerCapwapAcIp.setDescription('Configure DHCP option 138 field.')
tpDhcpServerUnusedIpTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4), )
if mibBuilder.loadTexts: tpDhcpServerUnusedIpTable.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerUnusedIpTable.setDescription('A list of distributed IP entries by the DHCP server.')
tpDhcpServerUnusedIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1), ).setIndexNames((0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerUnusedStartIp"))
if mibBuilder.loadTexts: tpDhcpServerUnusedIpEntry.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerUnusedIpEntry.setDescription(' A group of IP entries.')
tpDhcpServerUnusedStartIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerUnusedStartIp.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerUnusedStartIp.setDescription('Every DHCP Server own a lot of ip address ,here is the start unused ip address.')
tpDhcpServerUnusedEndIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerUnusedEndIp.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerUnusedEndIp.setDescription('The end unused ip address of the DHCP server.')
tpDhcpServerUnusedIpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 4, 1, 3), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerUnusedIpStatus.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerUnusedIpStatus.setDescription(' The following values are states: these values may be used as follow: active(1),if the entry is being used. createAndGo(4),not being used. destroy(6),destory the entry.')
tpDhcpServerAddrPoolTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5), )
if mibBuilder.loadTexts: tpDhcpServerAddrPoolTable.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolTable.setDescription('A list of entries in DHCP server address pool.')
tpDhcpServerAddrPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1), ).setIndexNames((0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerAddrPoolNetwork"))
if mibBuilder.loadTexts: tpDhcpServerAddrPoolEntry.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolEntry.setDescription(' A group of IP entries.')
tpDhcpServerAddrPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolName.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolName.setDescription('The entry name.')
tpDhcpServerAddrPoolNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNetwork.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNetwork.setDescription('The address of network.')
tpDhcpServerAddrPoolSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolSubnetMask.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolSubnetMask.setDescription('The address of subnet mask.')
tpDhcpServerAddrPoolRentTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolRentTime.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolRentTime.setDescription('The rent time.')
tpDhcpServerAddrPoolGateWayA = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayA.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayA.setDescription('The address of gateway.')
tpDhcpServerAddrPoolGateWayB = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayB.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayB.setDescription('The address of gateway.')
tpDhcpServerAddrPoolGateWayC = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayC.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayC.setDescription('The address of gateway.')
tpDhcpServerAddrPoolGateWayD = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayD.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayD.setDescription('The address of gateway.')
tpDhcpServerAddrPoolGateWayE = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayE.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayE.setDescription('The address of gateway.')
tpDhcpServerAddrPoolGateWayF = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayF.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayF.setDescription('The address of gateway.')
tpDhcpServerAddrPoolGateWayG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 11), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayG.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayG.setDescription('The address of gateway.')
tpDhcpServerAddrPoolGateWayH = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 12), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayH.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolGateWayH.setDescription('The address of gateway.')
tpDhcpServerAddrPoolDnsA = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 13), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsA.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsA.setDescription('The address of dns.')
tpDhcpServerAddrPoolDnsB = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 14), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsB.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsB.setDescription('The address of dns.')
tpDhcpServerAddrPoolDnsC = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 15), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsC.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsC.setDescription('The address of dns.')
tpDhcpServerAddrPoolDnsD = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 16), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsD.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsD.setDescription('The address of dns.')
tpDhcpServerAddrPoolDnsE = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 17), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsE.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsE.setDescription('The address of dns.')
tpDhcpServerAddrPoolDnsF = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsF.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsF.setDescription('The address of dns.')
tpDhcpServerAddrPoolDnsG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 19), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsG.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsG.setDescription('The address of dns.')
tpDhcpServerAddrPoolDnsH = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 20), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsH.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDnsH.setDescription('The address of dns.')
tpDhcpServerAddrPoolNBNServerA = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 21), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerA.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerA.setDescription('The address of nebios server.')
tpDhcpServerAddrPoolNBNServerB = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 22), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerB.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerB.setDescription('The address of nebios server.')
tpDhcpServerAddrPoolNBNServerC = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 23), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerC.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerC.setDescription('The address of nebios server.')
tpDhcpServerAddrPoolNBNServerD = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 24), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerD.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerD.setDescription('The address of nebios server.')
tpDhcpServerAddrPoolNBNServerE = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 25), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerE.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerE.setDescription('The address of nebios server.')
tpDhcpServerAddrPoolNBNServerF = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 26), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerF.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerF.setDescription('The address of nebios server.')
tpDhcpServerAddrPoolNBNServerG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 27), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerG.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerG.setDescription('The address of nebios server.')
tpDhcpServerAddrPoolNBNServerH = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 28), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerH.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNBNServerH.setDescription('The address of nebios server.')
tpDhcpServerAddrPoolNetbiosNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))).clone(namedValues=NamedValues(("none", 0), ("broadcast", 1), ("peer-to-peer", 2), ("mixed", 4), ("hybrid", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNetbiosNodeType.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNetbiosNodeType.setDescription('The Netbios node type. ')
tpDhcpServerAddrPoolNextServer = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 30), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNextServer.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolNextServer.setDescription('The address of next server.')
tpDhcpServerAddrPoolDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 31), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDomainName.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolDomainName.setDescription('The domain name of client.')
tpDhcpServerAddrPoolBootfile = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 32), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolBootfile.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolBootfile.setDescription('The domain name of client.')
tpDhcpServerAddrPoolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 5, 1, 33), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerAddrPoolStatus.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerAddrPoolStatus.setDescription(' The following values are states: these values may be used as follow: active(1),if the entry is being used. createAndGo(4),not being used. destroy(6),destory the entry.')
tpDhcpServerStaticBindTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6), )
if mibBuilder.loadTexts: tpDhcpServerStaticBindTable.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStaticBindTable.setDescription('A list of entries in DHCP server static bind table.')
tpDhcpServerStaticBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1), ).setIndexNames((0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerBindIpAddr"))
if mibBuilder.loadTexts: tpDhcpServerStaticBindEntry.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStaticBindEntry.setDescription(' A group of IP entries.')
tpDhcpServerStaticAddrPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerStaticAddrPoolName.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStaticAddrPoolName.setDescription('The entry name.')
tpDhcpServerBindIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerBindIpAddr.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerBindIpAddr.setDescription('The static binding ip address.')
tpDhcpServerStaticClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerStaticClientId.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStaticClientId.setDescription('The identifier of the client.')
tpDhcpServerMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerMacAddr.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerMacAddr.setDescription('The mac address of network.')
tpDhcpServerHardwareType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-2, -1, 1, 6))).clone(namedValues=NamedValues(("ascii", -2), ("hex", -1), ("ethernet", 1), ("ieee802", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerHardwareType.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerHardwareType.setDescription('The hardware type. -2 stands for ascii clientid, -1 stands for hex clientid ETHERNET_BIND v stands for mac type ethernet and 6 stands for mac type ieee802.')
tpDhcpServerStaticBindStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 6, 1, 6), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerStaticBindStatus.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStaticBindStatus.setDescription(' The following values are states: these values may be used as follow: active(1),if the entry is being used. createAndGo(4),not being used. destroy(6),destory the entry.')
tpDhcpServerBindingTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7), )
if mibBuilder.loadTexts: tpDhcpServerBindingTable.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerBindingTable.setDescription('A list of entries in DHCP server bindings.')
tpDhcpServerBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1), ).setIndexNames((0, "TPLINK-DHCPSERVER-MIB", "tpDhcpServerBindingIp"))
if mibBuilder.loadTexts: tpDhcpServerBindingEntry.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerBindingEntry.setDescription(' A group of IP entries.')
tpDhcpServerBindingIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerBindingIp.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerBindingIp.setDescription('The address of subnet mask.')
tpDhcpServerBindingClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerBindingClientId.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerBindingClientId.setDescription('The identifier of the client.')
tpDhcpServerBindingMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerBindingMac.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerBindingMac.setDescription('The address of network.')
tpDhcpServerBindingType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("automatic", 0), ("manual", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerBindingType.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerBindingType.setDescription('The binding type.')
tpDhcpServerBindingRemainTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerBindingRemainTime.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerBindingRemainTime.setDescription('The rent time.')
tpDhcpServerBindingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 7, 1, 6), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpDhcpServerBindingStatus.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerBindingStatus.setDescription(' The following values are states: these values may be used as follow: active(1),if the entry is being used. createAndGo(4),not being used. destroy(6),destory the entry.')
tpDhcpServerBindingClear = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("remain", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerBindingClear.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerBindingClear.setDescription('Clear the DHCP bindings.')
tpDhcpServerStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9))
tpDhcpServerStatisticsBootRequest = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsBootRequest.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsBootRequest.setDescription('Displays the Bootp Request packets received.')
tpDhcpServerStatisticsDiscover = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsDiscover.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsDiscover.setDescription('Displays the Discover packets received.')
tpDhcpServerStatisticsRequest = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsRequest.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsRequest.setDescription('Displays the Request packets received.')
tpDhcpServerStatisticsDecline = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsDecline.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsDecline.setDescription('Displays the Decline packets received.')
tpDhcpServerStatisticsRelease = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsRelease.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsRelease.setDescription('Displays the Release packets received.')
tpDhcpServerStatisticsInform = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsInform.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsInform.setDescription('Displays the Inform packets received.')
tpDhcpServerStatisticsBootReply = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsBootReply.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsBootReply.setDescription('Displays the Bootp reply packets sent.')
tpDhcpServerStatisticsOffer = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsOffer.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsOffer.setDescription('Displays the Offer packets sent.')
tpDhcpServerStatisticsAck = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsAck.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsAck.setDescription('Displays the Ack packets sent.')
tpDhcpServerStatisticsNak = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpDhcpServerStatisticsNak.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsNak.setDescription('Displays the Nak packets sent.')
tpDhcpServerStatisticsClear = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 9, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("remain", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerStatisticsClear.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerStatisticsClear.setDescription('Clear the packet statistics.')
tpDhcpServerPingPackets = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerPingPackets.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerPingPackets.setDescription('The number of packets to be sent.')
tpDhcpServerPingTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 38, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpDhcpServerPingTimeout.setStatus('current')
if mibBuilder.loadTexts: tpDhcpServerPingTimeout.setDescription('The time it takes to determine the specific IP not exist.')
mibBuilder.exportSymbols("TPLINK-DHCPSERVER-MIB", tpDhcpServerUnusedStartIp=tpDhcpServerUnusedStartIp, tpDhcpServerBindingRemainTime=tpDhcpServerBindingRemainTime, tpDhcpServerAddrPoolGateWayC=tpDhcpServerAddrPoolGateWayC, tpDhcpServerAddrPoolBootfile=tpDhcpServerAddrPoolBootfile, tpDhcpServerAddrPoolDnsG=tpDhcpServerAddrPoolDnsG, tpDhcpServerVendorClassId=tpDhcpServerVendorClassId, tpDhcpServerBindIpAddr=tpDhcpServerBindIpAddr, tpDhcpServerStatisticsBootRequest=tpDhcpServerStatisticsBootRequest, tpDhcpServerUnusedEndIp=tpDhcpServerUnusedEndIp, tpDhcpServerAddrPoolGateWayH=tpDhcpServerAddrPoolGateWayH, tpDhcpServerAddrPoolStatus=tpDhcpServerAddrPoolStatus, tpDhcpServerAddrPoolRentTime=tpDhcpServerAddrPoolRentTime, tpDhcpServerCapwapAcIp=tpDhcpServerCapwapAcIp, tpDhcpServerAddrPoolNextServer=tpDhcpServerAddrPoolNextServer, tpDhcpServerStaticBindStatus=tpDhcpServerStaticBindStatus, tpDhcpServerUnusedIpEntry=tpDhcpServerUnusedIpEntry, tpDhcpServerPingTimeout=tpDhcpServerPingTimeout, tpDhcpServerAddrPoolGateWayA=tpDhcpServerAddrPoolGateWayA, tpDhcpServerAddrPoolNetwork=tpDhcpServerAddrPoolNetwork, tpDhcpServerBindingClear=tpDhcpServerBindingClear, tpDhcpServerStaticClientId=tpDhcpServerStaticClientId, tpDhcpServerAddrPoolNBNServerA=tpDhcpServerAddrPoolNBNServerA, tpDhcpServerAddrPoolDnsE=tpDhcpServerAddrPoolDnsE, tpDhcpServerAddrPoolNBNServerC=tpDhcpServerAddrPoolNBNServerC, tpDhcpServerStatisticsInform=tpDhcpServerStatisticsInform, tplinkDhcpServerMIB=tplinkDhcpServerMIB, tpDhcpServerAddrPoolNBNServerG=tpDhcpServerAddrPoolNBNServerG, tpDhcpServerAddrPoolDnsA=tpDhcpServerAddrPoolDnsA, tpDhcpServerStatistics=tpDhcpServerStatistics, tpDhcpServerAddrPoolGateWayD=tpDhcpServerAddrPoolGateWayD, tpDhcpServerAddrPoolGateWayE=tpDhcpServerAddrPoolGateWayE, tpDhcpServerBindingTable=tpDhcpServerBindingTable, tpDhcpServerStatisticsNak=tpDhcpServerStatisticsNak, tpDhcpServerPingPackets=tpDhcpServerPingPackets, tpDhcpServerAddrPoolDnsH=tpDhcpServerAddrPoolDnsH, tpDhcpServerAddrPoolSubnetMask=tpDhcpServerAddrPoolSubnetMask, tpDhcpServerAddrPoolNetbiosNodeType=tpDhcpServerAddrPoolNetbiosNodeType, tplinkDhcpServerNotifications=tplinkDhcpServerNotifications, tpDhcpServerAddrPoolNBNServerH=tpDhcpServerAddrPoolNBNServerH, tpDhcpServerAddrPoolTable=tpDhcpServerAddrPoolTable, tplinkDhcpServerMIBObjects=tplinkDhcpServerMIBObjects, tpDhcpServerAddrPoolName=tpDhcpServerAddrPoolName, tpDhcpServerAddrPoolNBNServerD=tpDhcpServerAddrPoolNBNServerD, tpDhcpServerStatisticsDiscover=tpDhcpServerStatisticsDiscover, tpDhcpServerStatisticsOffer=tpDhcpServerStatisticsOffer, tpDhcpServerAddrPoolDnsF=tpDhcpServerAddrPoolDnsF, tpDhcpServerStaticAddrPoolName=tpDhcpServerStaticAddrPoolName, tpDhcpServerStatisticsDecline=tpDhcpServerStatisticsDecline, tpDhcpServerStaticBindEntry=tpDhcpServerStaticBindEntry, tpDhcpServerStaticBindTable=tpDhcpServerStaticBindTable, PYSNMP_MODULE_ID=tplinkDhcpServerMIB, tpDhcpServerBindingClientId=tpDhcpServerBindingClientId, tpDhcpServerAddrPoolGateWayG=tpDhcpServerAddrPoolGateWayG, tpDhcpServerStatisticsAck=tpDhcpServerStatisticsAck, tpDhcpServerAddrPoolDnsB=tpDhcpServerAddrPoolDnsB, tpDhcpServerStatisticsClear=tpDhcpServerStatisticsClear, tpDhcpServerAddrPoolDnsD=tpDhcpServerAddrPoolDnsD, tpDhcpServerAddrPoolDomainName=tpDhcpServerAddrPoolDomainName, tpDhcpServerUnusedIpStatus=tpDhcpServerUnusedIpStatus, tpDhcpServerStatisticsBootReply=tpDhcpServerStatisticsBootReply, tpDhcpServerAddrPoolNBNServerE=tpDhcpServerAddrPoolNBNServerE, tpDhcpServerMacAddr=tpDhcpServerMacAddr, tpDhcpServerBindingIp=tpDhcpServerBindingIp, tpDhcpServerAddrPoolGateWayB=tpDhcpServerAddrPoolGateWayB, tpDhcpServerEnable=tpDhcpServerEnable, tpDhcpServerUnusedIpTable=tpDhcpServerUnusedIpTable, tpDhcpServerAddrPoolNBNServerF=tpDhcpServerAddrPoolNBNServerF, tpDhcpServerStatisticsRequest=tpDhcpServerStatisticsRequest, tpDhcpServerBindingEntry=tpDhcpServerBindingEntry, tpDhcpServerAddrPoolGateWayF=tpDhcpServerAddrPoolGateWayF, tpDhcpServerAddrPoolEntry=tpDhcpServerAddrPoolEntry, tpDhcpServerBindingType=tpDhcpServerBindingType, tpDhcpServerHardwareType=tpDhcpServerHardwareType, tpDhcpServerBindingStatus=tpDhcpServerBindingStatus, tpDhcpServerAddrPoolNBNServerB=tpDhcpServerAddrPoolNBNServerB, tpDhcpServerStatisticsRelease=tpDhcpServerStatisticsRelease, tpDhcpServerAddrPoolDnsC=tpDhcpServerAddrPoolDnsC, tpDhcpServerBindingMac=tpDhcpServerBindingMac)