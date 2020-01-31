#
# PySNMP MIB module F10-VIRTUAL-LINK-TRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/F10-VIRTUAL-LINK-TRUNK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:11:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
f10Mgmt, = mibBuilder.importSymbols("FORCE10-SMI", "f10Mgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, Bits, MibIdentifier, IpAddress, Integer32, TimeTicks, ModuleIdentity, Gauge32, ObjectIdentity, NotificationType, Counter64, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "MibIdentifier", "IpAddress", "Integer32", "TimeTicks", "ModuleIdentity", "Gauge32", "ObjectIdentity", "NotificationType", "Counter64", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, MacAddress, TimeInterval, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "TimeInterval", "DisplayString")
f10VirtualLinkTrunkMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 17))
f10VirtualLinkTrunkMib.setRevisions(('2012-11-28 00:00', '2012-05-21 00:00', '2012-05-14 00:00', '2012-04-02 00:00', '2011-05-06 00:00', '2011-03-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f10VirtualLinkTrunkMib.setRevisionsDescriptions((' - Added new objects f10VLTPeerRouting, f10VLTPeerRoutingTimeout,f10VLTRemotePeerRouting in f10VirtualLinkTrunkTable - Added additional error reason peerRoutMismatch in f10VltErrorReason object', 'Added new object f10VLTCfgSysMacAddr in f10VirtualLinkTrunkTable', 'Re arranged MIB objects in the f10VirtualLinkTrunkTable to make it compatible with older version. Moved the newly added objects at the bottom', 'Re arrenged the f10VirtualLinkTrunkTable, additional objects are added. - f10VirtualLinkTrunkNotifications added to make notifications separate subtree from f10VirtualLinkTrunkMib. - f10VirtualLinkDetailsTable is added for VLT details. - f10VLTIclBwUsageExceed, f10VLTDomainConfigError new notifications are added. - Updated the corresponding conformance groups - Some indentation change', 'Modified MIB OID from 13 to 16.', 'Initial draft of VLT MIB.',))
if mibBuilder.loadTexts: f10VirtualLinkTrunkMib.setLastUpdated('201211280000Z')
if mibBuilder.loadTexts: f10VirtualLinkTrunkMib.setOrganization('Dell Inc')
if mibBuilder.loadTexts: f10VirtualLinkTrunkMib.setContactInfo('http://www.force10networks.com/support')
if mibBuilder.loadTexts: f10VirtualLinkTrunkMib.setDescription('This MIB module provides information on Dual Brain Virtual Link Trunk(VLT) feature which is a control plane mechanism to provide Layer2 multipathing between access network devices (switches or servers) and the core network. VLT represents a single logical layer 2 domain from the view of downstream devices that have LAG bundles terminating on separate chassis in the virtual link trunk domain. However, the two VLT chassis are independent L2/L3 switches for devices in the upstream network. A sample of VLT scenario: --------------------------------------------------------------- | _______________ | | | Edge router | | | |_______________| | | / \\ | | / \\ | | VLT / \\ | | ____________/_______________________\\____________ . | | | _______/ Back Up Link \\_______ | /|\\| | | | |-------------------------| | | | | | | | | ------- | | | L3| | | | | S4810 |________| Inter |________| S4810 | |_____| | | | |________|Chassis|________| | | L2| | | | | | | Link | | | | | | | VLT port \\_____\\ ------- /____/VLT port\\|/| | |_____\\_____\\_________________________/____/_____| . | | \\ \\ -----------------/ / | | \\ \\----/------------ / | | \\ / \\ / | | \\ / \\ / | |Lag(active)<--- \\ / \\ /--->Lag(active) | | ___\\__/___________________\\_/______ | | | _______ Stacking ______ | | | | | S60 |--------------| S60 | | | | | |__\\____| |____/_| | | | |_____\\______________________/______| | | \\ /-->Nic teaming | | \\__________________/ | | | Nic1 Nic2 | | | | Server | | | |____________________| | --------------------------------------------------------------- Benefits of VLT are as follows: > Allows a single device to use LAG across two upstream devices > Eliminates Spanning Tree Protocol (STP) blocked ports > Provides a loop-free topology > Uses all available uplink bandwidth > Provides fast convergence if either the link or a device fails > Provides link-level resiliency > Assures high availability GLOSSARY AND ABBREVIATIONS VLT - Virtual Link Trunk The combined port channel between the VLT peer devices and the downstream device. VLT Peer device One of a pair of devices that are connected with the special port channel known as the chassis interconnect trunk. VLT Chassis Interconnect Trunk The link used to synchronize states between the VLT peer devices. VLT domain This domain includes both VLT peer devices, the VLT chassis interconnect trunk, and all of the port channels in the VLT connected to the downstream devices. VLT Backup link The backup link monitors the vitality of a VLT peer device. The backup trunk sends configurable, periodic heart beat messages between VLT peer devices. ICL Abbreviation for Chassis InterConnect Link.')
f10VirtualLinkTrunkObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1))
f10VirtualLinkTrunkNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2))
class F10VLTMemberLinkStatus(TextualConvention, Integer32):
    description = 'This defines the status of the link. The states are: linkNotEstablished - Initial State. linkUp - Link is established and the VLT operations specific to this link are up. linkDown - Communication with Peer is lost. linkError - Configuration incompatible.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("linkNotEstablished", 0), ("linkUp", 1), ("linkDown", 2), ("linkError", 3))

f10VirtualLinkTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1), )
if mibBuilder.loadTexts: f10VirtualLinkTrunkTable.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkTrunkTable.setDescription('This table provides the information about Virtual Link Trunks. A row is added to the table when a VLT domain is configured in the device. A row is deleted from the table when the configured VLT domain is removed.')
f10VirtualLinkTrunkTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1), ).setIndexNames((0, "F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDomainId"))
if mibBuilder.loadTexts: f10VirtualLinkTrunkTableEntry.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkTrunkTableEntry.setDescription('Each entry represents information about the specific VLT domain.')
f10VLTDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTDomainId.setStatus('current')
if mibBuilder.loadTexts: f10VLTDomainId.setDescription("This oject represents the Virtual Link Trunk Domain's id.")
f10VLTMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTMacAddr.setStatus('current')
if mibBuilder.loadTexts: f10VLTMacAddr.setDescription(' This object represents the MAC Address value assigned to this Virtual Link Trunk domain.')
f10VLTPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(32768)).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTPriority.setStatus('current')
if mibBuilder.loadTexts: f10VLTPriority.setDescription("This object represents the Virtual Link Trunk domain's System Priority value.")
f10VLTIclIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTIclIfIndex.setStatus('current')
if mibBuilder.loadTexts: f10VLTIclIfIndex.setDescription('This object represents the interface index of the link configured as the Inter Chassis Link for the Virtual Link Trunk domain.')
f10VLTRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("standAlone", 0), ("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRole.setStatus('current')
if mibBuilder.loadTexts: f10VLTRole.setDescription('This object represents the role of the device in the Virtual Link Trunk domain configured.')
f10VLTPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notEstablished", 0), ("peerUp", 1), ("peerDown", 2), ("linkDown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTPeerStatus.setStatus('current')
if mibBuilder.loadTexts: f10VLTPeerStatus.setDescription('This object represents the status of the VLT Peer i.e whether it is active, or in disabled/errored state. notEstablished - set if ICL Link is either in notEstablished status or error status. peerUp - set if ICL Link is up. peerDown - set if both ICL link and Backup link are down linkDown - set if ICL link down and Backup link is up. ')
f10VLTIclStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 7), F10VLTMemberLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTIclStatus.setStatus('current')
if mibBuilder.loadTexts: f10VLTIclStatus.setDescription('This object represents the state of the IC link aggregation. linkNotEstablished - ICL Hello has not yet started.Initial State. linkUp - Hello protocol is established and the VLT operations are up. linkDown - Communication with Peer is lost. linkError - Communication with Peer is established but configuration incompatible.')
f10VLTHBeatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 8), F10VLTMemberLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTHBeatStatus.setStatus('current')
if mibBuilder.loadTexts: f10VLTHBeatStatus.setDescription('This object represents the status of the heart beat link/backup link. linkNotEstablished - Heartbeat has not yet started. Initial stage. linkUp - Heartbeat started and Remote is Up. linkDown - Heartbeat lost. linkError - This indicates a configuration error.')
f10VLTBkUpIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTBkUpIpAddrType.setStatus('current')
if mibBuilder.loadTexts: f10VLTBkUpIpAddrType.setDescription('This object represents the address family of the Backup link designated for the Virtual Link Trunk Domain.')
f10VLTBkUpIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTBkUpIpAddr.setStatus('current')
if mibBuilder.loadTexts: f10VLTBkUpIpAddr.setDescription('This object represents the Ip address of the backup link.')
f10VLTBkUpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 11), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(100, 500)).clone(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTBkUpInterval.setStatus('current')
if mibBuilder.loadTexts: f10VLTBkUpInterval.setDescription('This object represents the time interval for the VLT heart-beat timer. ')
f10VLTRemoteMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemoteMacAddr.setStatus('current')
if mibBuilder.loadTexts: f10VLTRemoteMacAddr.setDescription('This object represents the MAC Address of the Remote system that is part of the VLT Domain.')
f10VLTRemoteRolePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(32768)).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemoteRolePriority.setStatus('current')
if mibBuilder.loadTexts: f10VLTRemoteRolePriority.setDescription('This object represents the role priority of the Remote System that is part of the Virtual Link Trunk Domain.')
f10VLTUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTUnitId.setStatus('current')
if mibBuilder.loadTexts: f10VLTUnitId.setDescription('This object represents the configured unit ID for the Virtual Link Trunk domain.')
f10VLTVersionMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTVersionMajor.setStatus('current')
if mibBuilder.loadTexts: f10VLTVersionMajor.setDescription('This object represents the major version of for the Virtual Link Trunk domain protocol running.')
f10VLTVersionMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTVersionMinor.setStatus('current')
if mibBuilder.loadTexts: f10VLTVersionMinor.setDescription('This object represents the minor version of for the Virtual Link Trunk domain protocol running.')
f10VLTRemoteUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemoteUnitId.setStatus('current')
if mibBuilder.loadTexts: f10VLTRemoteUnitId.setDescription('This object represents the configured unit ID for the Virtual Link Trunk domain on the remote node.')
f10VLTRemoteVersionMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemoteVersionMajor.setStatus('current')
if mibBuilder.loadTexts: f10VLTRemoteVersionMajor.setDescription('This object represents the major version of for the Virtual Link Trunk domain protocol running on the remote node.')
f10VLTRemoteVersionMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemoteVersionMinor.setStatus('current')
if mibBuilder.loadTexts: f10VLTRemoteVersionMinor.setDescription('This object represents the minor version of for the Virtual Link Trunk domain protocol running on the remote node.')
f10VLTIclBwStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("belowthreshold", 0), ("abovethreshold", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTIclBwStatus.setStatus('current')
if mibBuilder.loadTexts: f10VLTIclBwStatus.setDescription('This object represents the status of the VLT ICL Bandwidth usage i.e whether it crosses threshold, or below threshold state. below-threshold - set if ICL Link BW usage is below 80% above-threshold - set if ICL link BW usage is above 80%. ')
f10VLTCfgSysMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 21), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTCfgSysMacAddr.setStatus('current')
if mibBuilder.loadTexts: f10VLTCfgSysMacAddr.setDescription(' This object represents the System MAC Address value configured the Virtual Link Trunk domain.')
f10VLTPeerRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTPeerRouting.setStatus('current')
if mibBuilder.loadTexts: f10VLTPeerRouting.setDescription('This object represents the state of the VLT Peer routing i.e whether it is enabled or disabled.')
f10VLTPeerRoutingTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 23), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTPeerRoutingTimeout.setStatus('current')
if mibBuilder.loadTexts: f10VLTPeerRoutingTimeout.setDescription('This object represents the time interval for VLT peer-routing timer, which is configured for removing the local-da of the other peer in case of peer failure.')
f10VLTRemotePeerRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemotePeerRouting.setStatus('current')
if mibBuilder.loadTexts: f10VLTRemotePeerRouting.setDescription('This object represents the state of the VLT Peer routing configured on the remote peer node i.e whether it is enabled or disabled.')
f10VirtualLinkStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2), )
if mibBuilder.loadTexts: f10VirtualLinkStatsTable.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkStatsTable.setDescription('This table provides the details of the statistical information on traffic traversing port channels to attached devices, Interchassis link, and backup link.')
f10VirtualLinkStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1), )
f10VirtualLinkTrunkTableEntry.registerAugmentions(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VirtualLinkStatsTableEntry"))
f10VirtualLinkStatsTableEntry.setIndexNames(*f10VirtualLinkTrunkTableEntry.getIndexNames())
if mibBuilder.loadTexts: f10VirtualLinkStatsTableEntry.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkStatsTableEntry.setDescription('Each entry is the device specific statistical information on traffic in the links in VLT domain.')
f10VLTStatNumHelloSent = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumHelloSent.setStatus('current')
if mibBuilder.loadTexts: f10VLTStatNumHelloSent.setDescription('The count of Hello Packets sent across the ICL for synchronization.')
f10VLTStatNumHelloRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumHelloRcvd.setStatus('current')
if mibBuilder.loadTexts: f10VLTStatNumHelloRcvd.setDescription('The count of Hello Packets received from the remote VLT through the ICL.')
f10VLTStatNumHbeatSent = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumHbeatSent.setStatus('current')
if mibBuilder.loadTexts: f10VLTStatNumHbeatSent.setDescription('The count of periodic Keepalive messages sent by the VLT device to the peer.')
f10VLTStatNumHbeatRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumHbeatRcvd.setStatus('current')
if mibBuilder.loadTexts: f10VLTStatNumHbeatRcvd.setDescription('The count of periodic Keepalive messages received by the VLT device from the peer.')
f10VLTStatNumDomainErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumDomainErrors.setStatus('current')
if mibBuilder.loadTexts: f10VLTStatNumDomainErrors.setDescription("The count of hello/heartbeat packets dropped by the VLT device which failed to match the device's VLT domain Id.")
f10VLTStatNumVersionErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumVersionErrors.setStatus('current')
if mibBuilder.loadTexts: f10VLTStatNumVersionErrors.setDescription("The count of hello/heartbeat packets dropped by the VLT device which failed to match the device's VLT message's version.")
f10VirtualLinkDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3), )
if mibBuilder.loadTexts: f10VirtualLinkDetailsTable.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkDetailsTable.setDescription('This table provides the details of port channel information by traversing port channels to attached devices, peer port-channel ID, status and Active Vlans')
f10VirtualLinkDetailsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1), ).setIndexNames((0, "F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailLocalLagID"))
if mibBuilder.loadTexts: f10VirtualLinkDetailsTableEntry.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkDetailsTableEntry.setDescription('Each entry is the port channel specific information on links between TOR and VLT domain.')
f10VLTDetailLocalLagID = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTDetailLocalLagID.setStatus('current')
if mibBuilder.loadTexts: f10VLTDetailLocalLagID.setDescription('The Detail of the vlt local lag ID.')
f10VLTDetailPeerLagID = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTDetailPeerLagID.setStatus('current')
if mibBuilder.loadTexts: f10VLTDetailPeerLagID.setDescription('The Detail of the vlt peer lag ID')
f10VLTDetailLocalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTDetailLocalStatus.setStatus('current')
if mibBuilder.loadTexts: f10VLTDetailLocalStatus.setDescription('The interface operational status of the vlt local LAG ID')
f10VLTDetailPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTDetailPeerStatus.setStatus('current')
if mibBuilder.loadTexts: f10VLTDetailPeerStatus.setDescription('The interface operational status of the vlt peer LAG ID.')
f10VLTErrorReason = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noError", 1), ("domainIdMismatch", 2), ("unitIdMismatch", 3), ("versionMismatch", 4), ("sysMacMismatch", 5), ("peerRoutingMismatch", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: f10VLTErrorReason.setStatus('current')
if mibBuilder.loadTexts: f10VLTErrorReason.setDescription('This object represents the VLT domain config error,the possible errors are: noError - No Error. domainIdMismatch - local and remote vlt domain Id mismatch. unitIdMismatch - local or remote vlt Unit Id is Identical or not configured. versionMismatch - local and remote vlt version does not meet criteria for peer UP. sysMacMismatch - local and remote vlt system MAC mismatch. peerRoutingMismatch - local and remote vlt peer-routing config mismatch')
f10VirtualLinkTrunkNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0))
f10VLTRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 1)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRole"))
if mibBuilder.loadTexts: f10VLTRoleChange.setStatus('current')
if mibBuilder.loadTexts: f10VLTRoleChange.setDescription('The agent generates this norification to denote the change in role of the VLT device in the VLT domain. This notification carries the information about the new role. The possible roles are as follows: 1. StandAlone 2. Primary 3. Secondary')
f10VLTIclStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 2)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclStatus"))
if mibBuilder.loadTexts: f10VLTIclStatusChange.setStatus('current')
if mibBuilder.loadTexts: f10VLTIclStatusChange.setDescription('The agent generates this notification to denote the change in InterConnect Link Status.The notification contains information on the new ICL status. The possible states are as follows: 1. NotEstabished 2. LinkUp 3. LinkDown 4. LinkError')
f10VLTPeerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 3)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerStatus"))
if mibBuilder.loadTexts: f10VLTPeerStatusChange.setStatus('current')
if mibBuilder.loadTexts: f10VLTPeerStatusChange.setDescription('The agent generates this notification to denote the change in Status of the Peer in the VLT domain. This notification contains information on the new status of the peer device. The possible states are as follows: 1. NotEstablished 2. PeerUp 3. PeerDown 4. LinkDown')
f10VLTHBeatStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 4)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTHBeatStatus"))
if mibBuilder.loadTexts: f10VLTHBeatStatusChange.setStatus('current')
if mibBuilder.loadTexts: f10VLTHBeatStatusChange.setDescription('The agent generates this notification to denote the change in Backup Link Status. The notification contains information on the new BackupLink Status. The possible states are as follows: 1. NotEstabished 2. LinkUp 3. LinkDown 4. LinkError')
f10VLTIclBwUsageExceed = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 5)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclIfIndex"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclBwStatus"))
if mibBuilder.loadTexts: f10VLTIclBwUsageExceed.setStatus('current')
if mibBuilder.loadTexts: f10VLTIclBwUsageExceed.setDescription('The IFM agent generates this notification to denote the change in Bandwidth usage of ICL Link, when it crosses the threshold above 80 %. The possible states are as follows: 0. Below threshold 1. Above threshold')
f10VLTDomainConfigError = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 6)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTErrorReason"))
if mibBuilder.loadTexts: f10VLTDomainConfigError.setStatus('current')
if mibBuilder.loadTexts: f10VLTDomainConfigError.setDescription('The agent generates this notification to denote there is a error/conflict in the VLT domain config parameters (either locally or in remote node which prevent the peer up. The mismatch can be domain Id, unitId,version or system MAC. The notification contains information on the error/mismatch type.')
f10VirtualLinkTrunkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3))
f10VirtualLinkTrunkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 1))
f10VirtualLinkTrunkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2))
f10VirtualLinkTrunkCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 1, 1)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VirtualLinkTrunkGroup"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VirtualLinkStatisticsGroup"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VirtualLinkNotificationGroup"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VirtualLinkDetailsTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10VirtualLinkTrunkCompliance = f10VirtualLinkTrunkCompliance.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkTrunkCompliance.setDescription('The compliance statement for the Dell Networking OS Virtual Link Trunk MIB.')
f10VirtualLinkTrunkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 1)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDomainId"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTMacAddr"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPriority"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclIfIndex"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRole"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerStatus"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclStatus"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTHBeatStatus"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTBkUpIpAddrType"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTBkUpIpAddr"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTBkUpInterval"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteMacAddr"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteRolePriority"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTUnitId"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTVersionMajor"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTVersionMinor"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteUnitId"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteVersionMajor"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteVersionMinor"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclBwStatus"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTCfgSysMacAddr"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerRouting"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerRoutingTimeout"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemotePeerRouting"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTErrorReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10VirtualLinkTrunkGroup = f10VirtualLinkTrunkGroup.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkTrunkGroup.setDescription('This group represents a collection of objects providing the overall VLT information.')
f10VirtualLinkStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 2)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHelloSent"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHelloRcvd"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHbeatSent"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHbeatRcvd"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumDomainErrors"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumVersionErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10VirtualLinkStatisticsGroup = f10VirtualLinkStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkStatisticsGroup.setDescription('This group represents a collection of objects providing the overall statistical information on the VLT.')
f10VirtualLinkNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 3)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRoleChange"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclStatusChange"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerStatusChange"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTHBeatStatusChange"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclBwUsageExceed"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDomainConfigError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10VirtualLinkNotificationGroup = f10VirtualLinkNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkNotificationGroup.setDescription('A collection of notification objects for the Dell Networking OS VLT mib')
f10VirtualLinkDetailsTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 4)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailLocalLagID"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailPeerLagID"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailLocalStatus"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailPeerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10VirtualLinkDetailsTableGroup = f10VirtualLinkDetailsTableGroup.setStatus('current')
if mibBuilder.loadTexts: f10VirtualLinkDetailsTableGroup.setDescription('This group represents a collection of objects providing the LAG details on the VLT.')
mibBuilder.exportSymbols("F10-VIRTUAL-LINK-TRUNK-MIB", f10VirtualLinkTrunkConformance=f10VirtualLinkTrunkConformance, f10VirtualLinkTrunkMib=f10VirtualLinkTrunkMib, f10VLTPeerRouting=f10VLTPeerRouting, f10VLTStatNumHbeatSent=f10VLTStatNumHbeatSent, f10VLTCfgSysMacAddr=f10VLTCfgSysMacAddr, f10VLTRemoteUnitId=f10VLTRemoteUnitId, f10VLTPeerStatusChange=f10VLTPeerStatusChange, f10VirtualLinkStatsTableEntry=f10VirtualLinkStatsTableEntry, f10VirtualLinkStatsTable=f10VirtualLinkStatsTable, f10VLTRoleChange=f10VLTRoleChange, f10VirtualLinkDetailsTable=f10VirtualLinkDetailsTable, f10VirtualLinkDetailsTableGroup=f10VirtualLinkDetailsTableGroup, f10VLTVersionMinor=f10VLTVersionMinor, f10VLTErrorReason=f10VLTErrorReason, f10VirtualLinkTrunkCompliance=f10VirtualLinkTrunkCompliance, f10VLTDetailPeerLagID=f10VLTDetailPeerLagID, PYSNMP_MODULE_ID=f10VirtualLinkTrunkMib, f10VirtualLinkTrunkTable=f10VirtualLinkTrunkTable, f10VLTRole=f10VLTRole, f10VLTIclStatus=f10VLTIclStatus, f10VLTHBeatStatusChange=f10VLTHBeatStatusChange, f10VLTRemoteRolePriority=f10VLTRemoteRolePriority, f10VLTDetailLocalStatus=f10VLTDetailLocalStatus, f10VLTDetailPeerStatus=f10VLTDetailPeerStatus, f10VLTStatNumVersionErrors=f10VLTStatNumVersionErrors, f10VLTBkUpIpAddr=f10VLTBkUpIpAddr, f10VLTVersionMajor=f10VLTVersionMajor, f10VLTStatNumDomainErrors=f10VLTStatNumDomainErrors, f10VLTBkUpInterval=f10VLTBkUpInterval, f10VLTPeerStatus=f10VLTPeerStatus, f10VLTUnitId=f10VLTUnitId, f10VirtualLinkNotificationGroup=f10VirtualLinkNotificationGroup, F10VLTMemberLinkStatus=F10VLTMemberLinkStatus, f10VLTBkUpIpAddrType=f10VLTBkUpIpAddrType, f10VirtualLinkTrunkGroup=f10VirtualLinkTrunkGroup, f10VirtualLinkDetailsTableEntry=f10VirtualLinkDetailsTableEntry, f10VLTHBeatStatus=f10VLTHBeatStatus, f10VLTRemoteVersionMajor=f10VLTRemoteVersionMajor, f10VLTIclBwStatus=f10VLTIclBwStatus, f10VirtualLinkTrunkNotifObjects=f10VirtualLinkTrunkNotifObjects, f10VLTIclIfIndex=f10VLTIclIfIndex, f10VLTRemoteMacAddr=f10VLTRemoteMacAddr, f10VLTIclBwUsageExceed=f10VLTIclBwUsageExceed, f10VirtualLinkTrunkNotifications=f10VirtualLinkTrunkNotifications, f10VirtualLinkTrunkTableEntry=f10VirtualLinkTrunkTableEntry, f10VLTMacAddr=f10VLTMacAddr, f10VLTStatNumHbeatRcvd=f10VLTStatNumHbeatRcvd, f10VLTPeerRoutingTimeout=f10VLTPeerRoutingTimeout, f10VirtualLinkTrunkObjects=f10VirtualLinkTrunkObjects, f10VLTRemotePeerRouting=f10VLTRemotePeerRouting, f10VLTDomainId=f10VLTDomainId, f10VLTRemoteVersionMinor=f10VLTRemoteVersionMinor, f10VLTStatNumHelloSent=f10VLTStatNumHelloSent, f10VirtualLinkTrunkCompliances=f10VirtualLinkTrunkCompliances, f10VirtualLinkTrunkGroups=f10VirtualLinkTrunkGroups, f10VLTStatNumHelloRcvd=f10VLTStatNumHelloRcvd, f10VLTDomainConfigError=f10VLTDomainConfigError, f10VLTPriority=f10VLTPriority, f10VirtualLinkStatisticsGroup=f10VirtualLinkStatisticsGroup, f10VLTDetailLocalLagID=f10VLTDetailLocalLagID, f10VLTIclStatusChange=f10VLTIclStatusChange)