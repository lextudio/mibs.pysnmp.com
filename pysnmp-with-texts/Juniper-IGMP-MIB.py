#
# PySNMP MIB module Juniper-IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IGMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:02:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniInterfaceLocationType, JuniInterfaceLocationValue = mibBuilder.importSymbols("Juniper-TC", "JuniInterfaceLocationType", "JuniInterfaceLocationValue")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, iso, Counter32, IpAddress, Gauge32, ObjectIdentity, NotificationType, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter32", "IpAddress", "Gauge32", "ObjectIdentity", "NotificationType", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Counter64", "ModuleIdentity")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
juniIgmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40))
juniIgmpMIB.setRevisions(('2006-08-25 05:40', '2003-09-29 18:39', '2002-10-28 14:55', '2000-09-26 18:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIgmpMIB.setRevisionsDescriptions(('Added juniIgmpIfLocationType for support on REX platform and deprecated juniIgmpGroupsTable.', 'Added IGMP administration state support.', 'Replaced Unisphere names with Juniper names. Added support for interface addresses and multicast group limits.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniIgmpMIB.setLastUpdated('200608250540Z')
if mibBuilder.loadTexts: juniIgmpMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniIgmpMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniIgmpMIB.setDescription('The IGMP MIB for Juniper Networks enterprise.')
class JuniIgmpProxyGroupState(TextualConvention, Integer32):
    description = 'IP multicast group state in respect to the host IGMP (IGMP proxy) behavior.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("juniIgmpProxyGroupUnknown", 0), ("juniIgmpProxyGroupIdleMember", 1), ("juniIgmpProxyGroupDelayingMember", 2))

class JuniIgmpProxyInterfaceState(TextualConvention, Integer32):
    description = 'IGMP proxy Interface state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("juniIgmpProxyInterfaceUnknown", 0), ("juniIgmpProxyInterfaceStateV1RouterPresent", 1), ("juniIgmpProxyInterfaceStateNonV1RouterPresent", 2))

juniIgmpMIBObject = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1))
juniIgmpProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1))
juniIgmpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2))
juniIgmpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3))
juniIgmpGroupsTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 1), )
if mibBuilder.loadTexts: juniIgmpGroupsTable.setStatus('deprecated')
if mibBuilder.loadTexts: juniIgmpGroupsTable.setDescription('Deprecated table of max multicast groups for each physical port. This has been replaced by juniIgmpGroupsTable2.')
juniIgmpGroupsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 1, 1), ).setIndexNames((0, "Juniper-IGMP-MIB", "juniIgmpGroupsSlot"), (0, "Juniper-IGMP-MIB", "juniIgmpGroupsPort"))
if mibBuilder.loadTexts: juniIgmpGroupsEntry.setStatus('deprecated')
if mibBuilder.loadTexts: juniIgmpGroupsEntry.setDescription('Deprecated entry representing per physical port max multicast groups configurations. This has been replaced by juniIgmpGroupsEntry2.')
juniIgmpGroupsSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: juniIgmpGroupsSlot.setStatus('deprecated')
if mibBuilder.loadTexts: juniIgmpGroupsSlot.setDescription('Deprecated physical slot position to configure the max multicast groups for any selected port. This has been replaced by juniIgmpIfLocationIndex.')
juniIgmpGroupsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: juniIgmpGroupsPort.setStatus('deprecated')
if mibBuilder.loadTexts: juniIgmpGroupsPort.setDescription('Deprecated physical port to configure max multicast groups. This has been replaced by juniIgmpIfLocationIndex.')
juniIgmpGroupsMaxGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniIgmpGroupsMaxGroups.setStatus('deprecated')
if mibBuilder.loadTexts: juniIgmpGroupsMaxGroups.setDescription('Deprecated max multicast groups limit value for each physical port. This has been replaced by juniIgmpGroupsMaxGroups2.')
juniIgmpIfLocationType = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 2), JuniInterfaceLocationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpIfLocationType.setStatus('current')
if mibBuilder.loadTexts: juniIgmpIfLocationType.setDescription("Describes the interpretation of JuniInterfaceLocationValue object values into platform-dependent interface location components, e.g., 'slot.port' on an ERX.")
juniIgmpGroupsTable2 = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 3), )
if mibBuilder.loadTexts: juniIgmpGroupsTable2.setStatus('current')
if mibBuilder.loadTexts: juniIgmpGroupsTable2.setDescription('The table of max multicast groups for each physical port.')
juniIgmpGroupsEntry2 = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 3, 1), ).setIndexNames((0, "Juniper-IGMP-MIB", "juniIgmpIfLocationIndex"))
if mibBuilder.loadTexts: juniIgmpGroupsEntry2.setStatus('current')
if mibBuilder.loadTexts: juniIgmpGroupsEntry2.setDescription('Each entry represents per physical port max multicast groups configurations.')
juniIgmpIfLocationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 3, 1, 1), JuniInterfaceLocationValue())
if mibBuilder.loadTexts: juniIgmpIfLocationIndex.setStatus('current')
if mibBuilder.loadTexts: juniIgmpIfLocationIndex.setDescription('The value of a platform interface location.')
juniIgmpGroupsMaxGroups2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniIgmpGroupsMaxGroups2.setStatus('current')
if mibBuilder.loadTexts: juniIgmpGroupsMaxGroups2.setDescription('Configure the max multicast groups limit for each physical port.')
juniIgmpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1), )
if mibBuilder.loadTexts: juniIgmpInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: juniIgmpInterfaceTable.setDescription('The table listing the interfaces on which IGMP is enabled.')
juniIgmpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-IGMP-MIB", "juniIgmpInterfaceIfIndex"))
if mibBuilder.loadTexts: juniIgmpInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: juniIgmpInterfaceEntry.setDescription('An entry representing an interface on which IGMP is enabled.')
juniIgmpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniIgmpInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniIgmpInterfaceIfIndex.setDescription('The ifIndex value of the interface for which IGMP is enabled.')
juniIgmpInterfaceQuerierTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 399))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniIgmpInterfaceQuerierTimeout.setStatus('current')
if mibBuilder.loadTexts: juniIgmpInterfaceQuerierTimeout.setDescription('Configure other-querier-present timeout on an interface.')
juniIgmpInterfaceImmediateLeave = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniIgmpInterfaceImmediateLeave.setStatus('current')
if mibBuilder.loadTexts: juniIgmpInterfaceImmediateLeave.setDescription('Enable/disable feature to stop traffic immediately after receive leave.')
juniIgmpInterfaceAccessGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniIgmpInterfaceAccessGroup.setStatus('current')
if mibBuilder.loadTexts: juniIgmpInterfaceAccessGroup.setDescription('Configure the access group list.')
juniIgmpInterfacePromiscuous = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniIgmpInterfacePromiscuous.setStatus('current')
if mibBuilder.loadTexts: juniIgmpInterfacePromiscuous.setDescription('Configure the promiscuous state.')
juniIgmpInterfaceMaxGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniIgmpInterfaceMaxGroups.setStatus('current')
if mibBuilder.loadTexts: juniIgmpInterfaceMaxGroups.setDescription('Configure the multicast groups limit.')
juniIgmpInterfaceIoaPacketReplIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 7), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniIgmpInterfaceIoaPacketReplIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniIgmpInterfaceIoaPacketReplIfIndex.setDescription('Configure the IOA packet replication interface.')
juniIgmpRouterPromiscuous = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniIgmpRouterPromiscuous.setStatus('current')
if mibBuilder.loadTexts: juniIgmpRouterPromiscuous.setDescription('Configure the promiscuous state of the router.')
juniIgmpAdminState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniIgmpAdminState.setStatus('current')
if mibBuilder.loadTexts: juniIgmpAdminState.setDescription('Adminstratively enable/disable the IGMP on the router.')
juniIgmpProxyInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1), )
if mibBuilder.loadTexts: juniIgmpProxyInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceTable.setDescription('The IGMP proxy interface table consists of interface on which the IGMP proxy is enabled.')
juniIgmpProxyInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1), ).setIndexNames((0, "Juniper-IGMP-MIB", "juniIgmpProxyInterfaceIfIndex"))
if mibBuilder.loadTexts: juniIgmpProxyInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceEntry.setDescription('An entry in the juniIgmpProxyInterfaceTable.')
juniIgmpProxyInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniIgmpProxyInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceIfIndex.setDescription('The ifIndex value of the interface for which the IGMP proxy is enabled.')
juniIgmpProxyInterfaceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceAddress.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceAddress.setDescription('The IP address of the interface for which the IGMP proxy is enabled.')
juniIgmpProxyInterfaceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceMask.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceMask.setDescription('The IP subnet mask of the interface for which the IGMP proxy is enabled.')
juniIgmpProxyInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 4), JuniIgmpProxyInterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceState.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceState.setDescription('When the IGMP proxy interface has v1 router present timeout running, it is in IgmpIntfStateV1RtPresent state. Otherwise, it is in IgmpIntfStateNonV1RtPresent states. While it is in IgmpIntfStateV1RtPresent, it only sends out version 1 group membership report(s). While it is in IgmpIntfStateNonV1RtPresent state, it sends out version 2 group membership report(s).')
juniIgmpProxyInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceStatus.setDescription('The state of the IGMP proxy interface. This object follows the RowStatus behavior. The destruction of the the row deletes the IGMP proxy inteface.')
juniIgmpProxyInterfaceVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceVersion.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceVersion.setDescription('The version of IGMP that this IGMP proxy interface is running.')
juniIgmpProxyInterfaceV1RoutePresentTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(400)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV1RoutePresentTimeout.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV1RoutePresentTimeout.setDescription('The IGMP version 1 router present timeout is the time between IGMP proxy receives a version 1 query and the time it assumes that there is no more IGMP version 1 router IGMP running. While before the V1 router present timeout expires, the IGMP proxy only sends out version 1 group membership report. When it expires, it sends out version 2 group membership report.')
juniIgmpProxyInterfaceUnsolicitedReportInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceUnsolicitedReportInterval.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceUnsolicitedReportInterval.setDescription('The unsolicited report interval specifies the time between the two initial group membership reports that the IGMP proxy sends.')
juniIgmpProxyInterfaceTotalGroupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceTotalGroupCount.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceTotalGroupCount.setDescription('Total number of multicast groups for this upstream interface (interface running IGMP proxy).')
juniIgmpProxyInterfaceWrongVersionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceWrongVersionCount.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceWrongVersionCount.setDescription('Total number of wrong version of IGMP packets received on this interface.')
juniIgmpProxyInterfaceV1QueryReceiveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV1QueryReceiveCount.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV1QueryReceiveCount.setDescription('Total number of version 1 IGMP queries received on this interface')
juniIgmpProxyInterfaceV2QueryReceiveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV2QueryReceiveCount.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV2QueryReceiveCount.setDescription('Total number of version 2 IGMP queries received on this interface.')
juniIgmpProxyInterfaceV1ReportReceiveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV1ReportReceiveCount.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV1ReportReceiveCount.setDescription('Total number of version 1 group membership reports received on this interface.')
juniIgmpProxyInterfaceV2ReportReceiveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV2ReportReceiveCount.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV2ReportReceiveCount.setDescription('Total number of version 2 group membership reports received on this interface.')
juniIgmpProxyInterfaceV1JoinReportCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV1JoinReportCount.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV1JoinReportCount.setDescription('Total number of version 1 group membership reports sent on this interface.')
juniIgmpProxyInterfaceV2JoinReportCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV2JoinReportCount.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceV2JoinReportCount.setDescription('Total number of version 2 group membership reports sent on this interface.')
juniIgmpProxyInterfaceLeaveReportCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyInterfaceLeaveReportCount.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceLeaveReportCount.setDescription('Total number of group leave reports sent on this interface.')
juniIgmpProxyCacheTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2), )
if mibBuilder.loadTexts: juniIgmpProxyCacheTable.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyCacheTable.setDescription('The IP multicast group table. The table is a union of multicast member groups from all its downstream interfaces and for which the IGMP proxy send group membership report.')
juniIgmpProxyCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1), ).setIndexNames((0, "Juniper-IGMP-MIB", "juniIgmpProxyIfIndex"), (0, "Juniper-IGMP-MIB", "juniIgmpProxyAddress"))
if mibBuilder.loadTexts: juniIgmpProxyCacheEntry.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyCacheEntry.setDescription('An entry in the juniIgmpProxyCacheTable.')
juniIgmpProxyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniIgmpProxyIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyIfIndex.setDescription('The ifIndex value of the interface for which IGMP proxy is enabled.')
juniIgmpProxyAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: juniIgmpProxyAddress.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyAddress.setDescription('The IP multicast group address that the IGMP proxy sends group membership for.')
juniIgmpProxyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 3), JuniIgmpProxyGroupState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIgmpProxyStatus.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyStatus.setDescription('The state of this entry. When the IGMP proxy has a delay time running for this multicast group, the state of this enry is in the juniIgmpDelayingMember state. When the delay time expires, the IGMP proxy sends an unsolicited report and the state of this group enters juniIgmpDelayMember state.')
juniIgmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4))
juniIgmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1))
juniIgmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2))
juniIgmpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1, 1)).setObjects(("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceGroup"), ("Juniper-IGMP-MIB", "juniIgmpProxyCacheGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpCompliance = juniIgmpCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: juniIgmpCompliance.setDescription('Obsolete compliance statement for entities that implement the Juniper IGMP MIB. This statement became obsolete when support was added for interface addresses and multicast group limits.')
juniIgmpCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1, 2)).setObjects(("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceGroup"), ("Juniper-IGMP-MIB", "juniIgmpProxyCacheGroup"), ("Juniper-IGMP-MIB", "juniIgmpInterfaceGroup"), ("Juniper-IGMP-MIB", "juniIgmpGroupsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpCompliance2 = juniIgmpCompliance2.setStatus('obsolete')
if mibBuilder.loadTexts: juniIgmpCompliance2.setDescription('Obsolete compliance statement for entities that implement the Juniper IGMP MIB. This statement became obsolete when support was added for the administrative state object.')
juniIgmpCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1, 3)).setObjects(("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceGroup"), ("Juniper-IGMP-MIB", "juniIgmpProxyCacheGroup"), ("Juniper-IGMP-MIB", "juniIgmpInterfaceGroup2"), ("Juniper-IGMP-MIB", "juniIgmpGroupsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpCompliance3 = juniIgmpCompliance3.setStatus('deprecated')
if mibBuilder.loadTexts: juniIgmpCompliance3.setDescription('Deprecated compliance statement for entities that implement the Juniper IGMP MIB. This statement was deprecated when support was added for the juniIgmpIfLocationType object.')
juniIgmpCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1, 4)).setObjects(("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceGroup"), ("Juniper-IGMP-MIB", "juniIgmpProxyCacheGroup"), ("Juniper-IGMP-MIB", "juniIgmpInterfaceGroup2"), ("Juniper-IGMP-MIB", "juniIgmpGroupsGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpCompliance4 = juniIgmpCompliance4.setStatus('current')
if mibBuilder.loadTexts: juniIgmpCompliance4.setDescription('The compliance statement for entities that implement the Juniper IGMP MIB.')
juniIgmpProxyInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 1)).setObjects(("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceAddress"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceMask"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceState"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceStatus"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceVersion"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV1RoutePresentTimeout"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceUnsolicitedReportInterval"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceTotalGroupCount"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceWrongVersionCount"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV1QueryReceiveCount"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV2QueryReceiveCount"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV1ReportReceiveCount"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV2ReportReceiveCount"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV1JoinReportCount"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV2JoinReportCount"), ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceLeaveReportCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpProxyInterfaceGroup = juniIgmpProxyInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyInterfaceGroup.setDescription('A collection of objects providing management of IGMP proxy interfaces in a Juniper product.')
juniIgmpProxyCacheGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 2)).setObjects(("Juniper-IGMP-MIB", "juniIgmpProxyStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpProxyCacheGroup = juniIgmpProxyCacheGroup.setStatus('current')
if mibBuilder.loadTexts: juniIgmpProxyCacheGroup.setDescription('An object providing management of IGMP proxy caches in a Juniper product.')
juniIgmpInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 3)).setObjects(("Juniper-IGMP-MIB", "juniIgmpInterfaceQuerierTimeout"), ("Juniper-IGMP-MIB", "juniIgmpInterfaceImmediateLeave"), ("Juniper-IGMP-MIB", "juniIgmpInterfaceAccessGroup"), ("Juniper-IGMP-MIB", "juniIgmpInterfacePromiscuous"), ("Juniper-IGMP-MIB", "juniIgmpInterfaceMaxGroups"), ("Juniper-IGMP-MIB", "juniIgmpRouterPromiscuous"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpInterfaceGroup = juniIgmpInterfaceGroup.setStatus('obsolete')
if mibBuilder.loadTexts: juniIgmpInterfaceGroup.setDescription('Obsolete collection of objects providing management of IGMP interfaces in a Juniper product. This group became obsolete when the administrative state object was added.')
juniIgmpGroupsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 4)).setObjects(("Juniper-IGMP-MIB", "juniIgmpGroupsMaxGroups"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpGroupsGroup = juniIgmpGroupsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: juniIgmpGroupsGroup.setDescription('Deprecated object providing management of IGMP global mCast groups in a Juniper product. This group was deprecated when support was added for juniIgmpIfLocationType.')
juniIgmpInterfaceGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 5)).setObjects(("Juniper-IGMP-MIB", "juniIgmpInterfaceQuerierTimeout"), ("Juniper-IGMP-MIB", "juniIgmpInterfaceImmediateLeave"), ("Juniper-IGMP-MIB", "juniIgmpInterfaceAccessGroup"), ("Juniper-IGMP-MIB", "juniIgmpInterfacePromiscuous"), ("Juniper-IGMP-MIB", "juniIgmpInterfaceMaxGroups"), ("Juniper-IGMP-MIB", "juniIgmpRouterPromiscuous"), ("Juniper-IGMP-MIB", "juniIgmpAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpInterfaceGroup2 = juniIgmpInterfaceGroup2.setStatus('current')
if mibBuilder.loadTexts: juniIgmpInterfaceGroup2.setDescription('A collection of objects providing management of IGMP interfaces in a Juniper product.')
juniIgmpGroupsGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 6)).setObjects(("Juniper-IGMP-MIB", "juniIgmpIfLocationType"), ("Juniper-IGMP-MIB", "juniIgmpGroupsMaxGroups2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpGroupsGroup2 = juniIgmpGroupsGroup2.setStatus('current')
if mibBuilder.loadTexts: juniIgmpGroupsGroup2.setDescription('A collection of objects providing management of IGMP global mCast groups in a Juniper product.')
mibBuilder.exportSymbols("Juniper-IGMP-MIB", JuniIgmpProxyInterfaceState=JuniIgmpProxyInterfaceState, juniIgmpConformance=juniIgmpConformance, juniIgmpProxyInterfaceMask=juniIgmpProxyInterfaceMask, juniIgmpProxyInterfaceGroup=juniIgmpProxyInterfaceGroup, juniIgmpProxyInterfaceStatus=juniIgmpProxyInterfaceStatus, juniIgmpInterfaceGroup=juniIgmpInterfaceGroup, juniIgmpGroupsTable2=juniIgmpGroupsTable2, juniIgmpProtocol=juniIgmpProtocol, juniIgmpInterfaceTable=juniIgmpInterfaceTable, juniIgmpInterfaceQuerierTimeout=juniIgmpInterfaceQuerierTimeout, juniIgmpIfLocationType=juniIgmpIfLocationType, juniIgmpInterfaceGroup2=juniIgmpInterfaceGroup2, juniIgmpInterfaceMaxGroups=juniIgmpInterfaceMaxGroups, juniIgmpProxyCacheTable=juniIgmpProxyCacheTable, juniIgmpProxyInterfaceV1QueryReceiveCount=juniIgmpProxyInterfaceV1QueryReceiveCount, juniIgmpProxyInterfaceState=juniIgmpProxyInterfaceState, juniIgmpGroupsMaxGroups=juniIgmpGroupsMaxGroups, juniIgmpInterfaceAccessGroup=juniIgmpInterfaceAccessGroup, juniIgmpInterfaceIoaPacketReplIfIndex=juniIgmpInterfaceIoaPacketReplIfIndex, juniIgmpProxyInterfaceUnsolicitedReportInterval=juniIgmpProxyInterfaceUnsolicitedReportInterval, juniIgmpGroupsSlot=juniIgmpGroupsSlot, juniIgmpProxyInterfaceWrongVersionCount=juniIgmpProxyInterfaceWrongVersionCount, juniIgmpProxyInterfaceLeaveReportCount=juniIgmpProxyInterfaceLeaveReportCount, juniIgmpProxyInterfaceEntry=juniIgmpProxyInterfaceEntry, juniIgmpGroupsEntry=juniIgmpGroupsEntry, juniIgmpInterfaceImmediateLeave=juniIgmpInterfaceImmediateLeave, juniIgmpGroupsMaxGroups2=juniIgmpGroupsMaxGroups2, juniIgmpProxyInterfaceV2ReportReceiveCount=juniIgmpProxyInterfaceV2ReportReceiveCount, juniIgmpProxy=juniIgmpProxy, juniIgmpGlobal=juniIgmpGlobal, juniIgmpProxyCacheEntry=juniIgmpProxyCacheEntry, juniIgmpGroupsPort=juniIgmpGroupsPort, juniIgmpProxyInterfaceAddress=juniIgmpProxyInterfaceAddress, juniIgmpCompliance=juniIgmpCompliance, juniIgmpProxyStatus=juniIgmpProxyStatus, juniIgmpInterfaceIfIndex=juniIgmpInterfaceIfIndex, juniIgmpProxyIfIndex=juniIgmpProxyIfIndex, juniIgmpProxyInterfaceTable=juniIgmpProxyInterfaceTable, juniIgmpProxyInterfaceV1JoinReportCount=juniIgmpProxyInterfaceV1JoinReportCount, juniIgmpInterfaceEntry=juniIgmpInterfaceEntry, juniIgmpProxyInterfaceV2JoinReportCount=juniIgmpProxyInterfaceV2JoinReportCount, juniIgmpRouterPromiscuous=juniIgmpRouterPromiscuous, juniIgmpProxyInterfaceTotalGroupCount=juniIgmpProxyInterfaceTotalGroupCount, juniIgmpProxyInterfaceV1RoutePresentTimeout=juniIgmpProxyInterfaceV1RoutePresentTimeout, juniIgmpProxyInterfaceV2QueryReceiveCount=juniIgmpProxyInterfaceV2QueryReceiveCount, juniIgmpAdminState=juniIgmpAdminState, juniIgmpProxyInterfaceVersion=juniIgmpProxyInterfaceVersion, juniIgmpProxyInterfaceV1ReportReceiveCount=juniIgmpProxyInterfaceV1ReportReceiveCount, juniIgmpProxyCacheGroup=juniIgmpProxyCacheGroup, juniIgmpGroupsTable=juniIgmpGroupsTable, juniIgmpCompliance4=juniIgmpCompliance4, juniIgmpCompliance3=juniIgmpCompliance3, juniIgmpCompliances=juniIgmpCompliances, juniIgmpProxyAddress=juniIgmpProxyAddress, juniIgmpCompliance2=juniIgmpCompliance2, juniIgmpGroupsGroup=juniIgmpGroupsGroup, juniIgmpGroupsEntry2=juniIgmpGroupsEntry2, JuniIgmpProxyGroupState=JuniIgmpProxyGroupState, juniIgmpInterfacePromiscuous=juniIgmpInterfacePromiscuous, juniIgmpGroups=juniIgmpGroups, juniIgmpGroupsGroup2=juniIgmpGroupsGroup2, PYSNMP_MODULE_ID=juniIgmpMIB, juniIgmpMIB=juniIgmpMIB, juniIgmpIfLocationIndex=juniIgmpIfLocationIndex, juniIgmpMIBObject=juniIgmpMIBObject, juniIgmpProxyInterfaceIfIndex=juniIgmpProxyInterfaceIfIndex)