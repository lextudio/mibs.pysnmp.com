#
# PySNMP MIB module DC-MGMD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DC-MGMD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:45:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Gauge32, ObjectIdentity, Integer32, Counter64, NotificationType, Bits, IpAddress, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Gauge32", "ObjectIdentity", "Integer32", "Counter64", "NotificationType", "Bits", "IpAddress", "Counter32", "iso")
TruthValue, StorageType, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "StorageType", "RowStatus", "DisplayString", "TextualConvention")
dcMgmdMib = ModuleIdentity((1, 2, 826, 0, 1, 1578918, 5, 99, 1))
dcMgmdMib.setRevisions(('2014-11-19 00:00', '2011-03-09 00:00', '2005-08-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dcMgmdMib.setRevisionsDescriptions(('Added mgmdPmRouterInterfaceProxyAutoSwitchback IEQ SDV feature.', 'Added mgmdPmStaticGroupStorageType for MCAST FQDN feature', 'Added the mib',))
if mibBuilder.loadTexts: dcMgmdMib.setLastUpdated('201411190000Z')
if mibBuilder.loadTexts: dcMgmdMib.setOrganization('Arris')
if mibBuilder.loadTexts: dcMgmdMib.setContactInfo('Arris Technical Support')
if mibBuilder.loadTexts: dcMgmdMib.setDescription('The MIB module for management of the MGMD product.')
class NonZeroUnsigned8(TextualConvention, Unsigned32):
    description = 'An non-zero unsigned32 further restricted to 8 Bits.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class NonZeroInteger(TextualConvention, Unsigned32):
    description = 'A positive integer.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class AdminStatus(TextualConvention, Integer32):
    description = 'The desired administrative state of a MGMD entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("adminStatusUp", 1), ("adminStatusDown", 2))

class OperStatus(TextualConvention, Integer32):
    description = 'The current operational state of a MGMD entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5))

class PmIndex(TextualConvention, Unsigned32):
    description = 'The index value identifying a MGMD entity.'
    status = 'current'

class MjStatus(TextualConvention, Integer32):
    description = 'The status of a Master Join.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("mjNotJoined", 1), ("mjSentAddJoin", 2), ("mjSentRegister", 3), ("mjJoinActive", 4), ("mjSentDelJoin", 5), ("mjSentUnregister", 6), ("mjJoinGone", 7), ("mjFailedToRegister", 8), ("mjFailingOver", 9), ("mjFailed", 10))

class InterfaceType(TextualConvention, Integer32):
    description = 'The type of interface to which a join applies.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ifIpSockets", 1), ("ifIfInfo", 2), ("ifRteProtInput", 3))

class MgmdEntityType(TextualConvention, Integer32):
    description = 'The MGMD entity type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("host", 1), ("router", 2))

mgmdPmEntTable = MibTable((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1), )
if mibBuilder.loadTexts: mgmdPmEntTable.setStatus('current')
if mibBuilder.loadTexts: mgmdPmEntTable.setDescription('The table of MGMD entities.')
mgmdPmEntEntry = MibTableRow((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1, 1), ).setIndexNames((0, "DC-MGMD-MIB", "mgmdPmEntIndex"))
if mibBuilder.loadTexts: mgmdPmEntEntry.setStatus('current')
if mibBuilder.loadTexts: mgmdPmEntEntry.setDescription('Each entry represents an instance of the MGMD Protocol Manager entity.')
mgmdPmEntIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1, 1, 1), PmIndex())
if mibBuilder.loadTexts: mgmdPmEntIndex.setStatus('current')
if mibBuilder.loadTexts: mgmdPmEntIndex.setDescription('The index of this mgmdPmEntEntry. This is the HAF entity index passed on the entity create parameters.')
mgmdPmEntAdminStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1, 1, 2), AdminStatus().clone('adminStatusUp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmEntAdminStatus.setStatus('current')
if mibBuilder.loadTexts: mgmdPmEntAdminStatus.setDescription('The desired administrative state of the MGMD Protocol Manager entity.')
mgmdPmEntOperStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1, 1, 3), OperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmEntOperStatus.setStatus('current')
if mibBuilder.loadTexts: mgmdPmEntOperStatus.setDescription('The current operational state of the MGMD Protocol Manager entity.')
mgmdPmEntRowStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmEntRowStatus.setStatus('current')
if mibBuilder.loadTexts: mgmdPmEntRowStatus.setDescription('Used to create and delete an MGMD Protocol Manager Entity Table entry.')
mgmdPmMjTable = MibTable((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2), )
if mibBuilder.loadTexts: mgmdPmMjTable.setStatus('current')
if mibBuilder.loadTexts: mgmdPmMjTable.setDescription('This table controls which entities the MGMD Protocol Manager should join to as master. Each join is represented by a row in this table. The status of each join is represented by a read-only object within each row.')
mgmdPmMjEntry = MibTableRow((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1), ).setIndexNames((0, "DC-MGMD-MIB", "mgmdPmMjEntIndex"), (0, "DC-MGMD-MIB", "mgmdPmMjInterfaceId"), (0, "DC-MGMD-MIB", "mgmdPmMjPartnerIndex"))
if mibBuilder.loadTexts: mgmdPmMjEntry.setStatus('current')
if mibBuilder.loadTexts: mgmdPmMjEntry.setDescription('Represents a join for which the MGMD Protocol Manager is master.')
mgmdPmMjEntIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 1), PmIndex())
if mibBuilder.loadTexts: mgmdPmMjEntIndex.setStatus('current')
if mibBuilder.loadTexts: mgmdPmMjEntIndex.setDescription('Identifies a MGMD Protocol Manager entity.')
mgmdPmMjInterfaceId = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 2), InterfaceType())
if mibBuilder.loadTexts: mgmdPmMjInterfaceId.setStatus('current')
if mibBuilder.loadTexts: mgmdPmMjInterfaceId.setDescription('Identifies the interface required of this master join.')
mgmdPmMjPartnerIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: mgmdPmMjPartnerIndex.setStatus('current')
if mibBuilder.loadTexts: mgmdPmMjPartnerIndex.setDescription('Identifies the slave entity to join with. This index is used in the join user data, to enable FTI-specific code within System Manager to select a suitable slave entity.')
mgmdPmMjRowStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmMjRowStatus.setStatus('current')
if mibBuilder.loadTexts: mgmdPmMjRowStatus.setDescription('The row status for this MGMD Protocol Manager Master Join Table entry, used to create and destroy table entries.')
mgmdPmMjAdminStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 5), AdminStatus().clone('adminStatusUp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmMjAdminStatus.setStatus('current')
if mibBuilder.loadTexts: mgmdPmMjAdminStatus.setDescription('The administrative status of this master join, used to start and stop the join.')
mgmdPmMjOperStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 6), OperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmMjOperStatus.setStatus('current')
if mibBuilder.loadTexts: mgmdPmMjOperStatus.setDescription('The current operational status of this master join.')
mgmdPmMjJoinStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 7), MjStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmMjJoinStatus.setStatus('current')
if mibBuilder.loadTexts: mgmdPmMjJoinStatus.setDescription('The status of the master join.')
mgmdPmStaticGroupTable = MibTable((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3), )
if mibBuilder.loadTexts: mgmdPmStaticGroupTable.setStatus('current')
if mibBuilder.loadTexts: mgmdPmStaticGroupTable.setDescription('The list of multicast groups which are statically joined on an MGMD host or router.')
mgmdPmStaticGroupEntry = MibTableRow((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1), ).setIndexNames((0, "DC-MGMD-MIB", "mgmdPmStaticGroupEntityType"), (0, "DC-MGMD-MIB", "mgmdPmStaticGroupIfIndex"), (0, "DC-MGMD-MIB", "mgmdPmStaticGroupAddressType"), (0, "DC-MGMD-MIB", "mgmdPmStaticGroupAddress"), (0, "DC-MGMD-MIB", "mgmdPmStaticGroupSourceAddress"))
if mibBuilder.loadTexts: mgmdPmStaticGroupEntry.setStatus('current')
if mibBuilder.loadTexts: mgmdPmStaticGroupEntry.setDescription('An entry (conceptual row) in the mgmdPmStaticGroupTable.')
mgmdPmStaticGroupEntityType = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 1), MgmdEntityType())
if mibBuilder.loadTexts: mgmdPmStaticGroupEntityType.setStatus('current')
if mibBuilder.loadTexts: mgmdPmStaticGroupEntityType.setDescription('The entity type, host or router, that this static group will apply to.')
mgmdPmStaticGroupIfIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: mgmdPmStaticGroupIfIndex.setStatus('current')
if mibBuilder.loadTexts: mgmdPmStaticGroupIfIndex.setDescription('The interface that is a member of the group. The interface can be either a layer 2 or 3 interface.')
mgmdPmStaticGroupAddressType = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 3), InetAddressType())
if mibBuilder.loadTexts: mgmdPmStaticGroupAddressType.setStatus('current')
if mibBuilder.loadTexts: mgmdPmStaticGroupAddressType.setDescription('The address type of the InetAddress variables in this table. This value applies to the mgmdPmStaticGroupAddress and mgmdPmStaticGroupSourceAddress entries.')
mgmdPmStaticGroupAddress = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 4), InetAddress())
if mibBuilder.loadTexts: mgmdPmStaticGroupAddress.setStatus('current')
if mibBuilder.loadTexts: mgmdPmStaticGroupAddress.setDescription('The multicast group address to make static.')
mgmdPmStaticGroupSourceAddress = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 5), InetAddress())
if mibBuilder.loadTexts: mgmdPmStaticGroupSourceAddress.setStatus('current')
if mibBuilder.loadTexts: mgmdPmStaticGroupSourceAddress.setDescription('The source of the multicast group traffic for SSM. Set to 0.0.0.0 if not using SSM.')
mgmdPmStaticGroupStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmStaticGroupStatus.setStatus('current')
if mibBuilder.loadTexts: mgmdPmStaticGroupStatus.setDescription('The status of this row.')
mgmdPmStaticGroupStorageType = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 7), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmStaticGroupStorageType.setStatus('current')
if mibBuilder.loadTexts: mgmdPmStaticGroupStorageType.setDescription('The storage type for this conceptual row. Only the rows provisioned with nonVolatie(3) will be persistent.')
mgmdPmRouterInterfaceTable = MibTable((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4), )
if mibBuilder.loadTexts: mgmdPmRouterInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceTable.setDescription('The (conceptual) table listing the interfaces on which IGMP or MLD is enabled.')
mgmdPmRouterInterfaceEntry = MibTableRow((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1), ).setIndexNames((0, "DC-MGMD-MIB", "mgmdPmRouterInterfaceIfIndex"), (0, "DC-MGMD-MIB", "mgmdPmRouterInterfaceQuerierType"))
if mibBuilder.loadTexts: mgmdPmRouterInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceEntry.setDescription('An entry (conceptual row) representing an interface on which IGMP or MLD is enabled.')
mgmdPmRouterInterfaceIfIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: mgmdPmRouterInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceIfIndex.setDescription('The ifIndex value of the interface for which IGMP or MLD is enabled. The table is indexed by the ifIndex value and the InetAddressType to allow for interfaces which may be configured in both IPv4 and IPv6 modes.')
mgmdPmRouterInterfaceQuerierType = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 2), InetAddressType())
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQuerierType.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQuerierType.setDescription('The address type of this interface. This entry along with the ifIndex value acts as the index to the mgmdPmRouterInterface table. A physical interface may be configured in multiple modes concurrently, e.g. in IPv4 and IPv6 modes connected to the same interface, however the traffic is considered to be logically separate.')
mgmdPmRouterInterfaceQuerier = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQuerier.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQuerier.setDescription('The address of the IGMP or MLD Querier on the IP subnet to which this interface is attached. The InetAddressType, e.g. IPv4 or IPv6, is identified by the mgmdPmRouterInterfaceQuerierType variable in the mgmdPmRouterInterface table.')
mgmdPmRouterInterfaceQueryInterval = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 31744)).clone(125)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQueryInterval.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQueryInterval.setDescription('The frequency at which IGMP or MLD Host-Query packets are transmitted on this interface. This variable must be a non-zero value.')
mgmdPmRouterInterfaceStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceStatus.setDescription('The activation of a row enables the router side of IGMP or MLD on the interface. The destruction of a row disables the router side of IGMP or MLD on the interface.')
mgmdPmRouterInterfaceVersion = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceVersion.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceVersion.setDescription('The version of MGMD which is running on this interface. Value 1 applies to IGMPv1 routers only. Value 2 applies To IGMPv2 and MLDv1 routers, and value 3 applies to IGMPv3 and MLDv2 routers. This object can be used to configure a router capable of running either version. For IGMP and MLD to function correctly, all routers on a LAN must be configured to run the same version on that LAN.')
mgmdPmRouterInterfaceQueryMaxResponseTime = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 31744)).clone(100)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQueryMaxResponseTime.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQueryMaxResponseTime.setDescription('The maximum query response time advertised in MGMDv2 or v3 queries on this interface.')
mgmdPmRouterInterfaceQuerierUpTime = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQuerierUpTime.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQuerierUpTime.setDescription('The time since mgmdPmRouterInterfaceQuerier was last changed.')
mgmdPmRouterInterfaceQuerierExpiryTime = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQuerierExpiryTime.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceQuerierExpiryTime.setDescription('The amount of time remaining before the Other Querier Present Timer expires. If the local system is the querier, the value of this object is zero.')
mgmdPmRouterInterfaceWrongVersionQueries = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceWrongVersionQueries.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceWrongVersionQueries.setDescription('The number of queries received whose IGMP or MLD version does not match the equivalent mgmdPmRouterInterfaceVersion, over the lifetime of the row entry. Both IGMP and MLD require that all routers on a LAN be configured to run the same version. Thus, if any queries are received with the wrong version, this indicates a configuration error.')
mgmdPmRouterInterfaceJoins = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceJoins.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceJoins.setDescription('The number of times a group membership has been added on this interface; that is, the number of times an entry for this interface has been added to the Cache Table. This object gives an indication of the amount of IGMP or MLD activity over the lifetime of the row entry.')
mgmdPmRouterInterfaceProxyIfIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 12), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceProxyIfIndex.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceProxyIfIndex.setDescription('Some devices implement a form of IGMP or MLD proxying whereby memberships learned on the interface represented by this row, cause Host Membership Reports to be sent on the interface whose ifIndex value is given by this object. Such a device would implement the mgmdV2RouterMIBGroup only on its router interfaces (those interfaces with non-zero mgmdPmRouterInterfaceProxyIfIndex). Typically, the value of this object is 0, indicating that no proxying is being done.')
mgmdPmRouterInterfaceGroups = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceGroups.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceGroups.setDescription('The current number of entries for this interface in the RouterCache Table.')
mgmdPmRouterInterfaceRobustness = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceRobustness.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceRobustness.setDescription('The Robustness Variable allows tuning for the expected packet loss on a subnet. If a subnet is expected to be lossy, the Robustness Variable may be increased. IGMP and MLD is robust to (Robustness Variable-1) packet losses.')
mgmdPmRouterInterfaceLastMembQueryIntvl = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 31744)).clone(10)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceLastMembQueryIntvl.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceLastMembQueryIntvl.setDescription('The Last Member Query Interval is the Max Response Time inserted into Group-Specific Queries sent in response to Leave Group messages, and is also the amount of time Between Group-Specific Query messages. This value may be tuned to modify the leave latency of the network. A reduced value results in reduced time to detect the loss of the last member of a group. The value of this object is irrelevant if mgmdPmRouterInterfaceVersion is 1.')
mgmdPmRouterInterfaceLastMembQueryCount = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceLastMembQueryCount.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceLastMembQueryCount.setDescription('Represents the number of Group-specific and Group-and-Source-specific queries sent by the router before it assumes there are no local members.')
mgmdPmRouterInterfaceStartupQueryCount = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceStartupQueryCount.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceStartupQueryCount.setDescription('Represents the number of Queries sent out on startup separated by the Startup Query Interval.')
mgmdPmRouterInterfaceStartupQueryInterval = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 31744)).clone(31)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceStartupQueryInterval.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceStartupQueryInterval.setDescription('This variable represents the interval between General Queries sent by a Querier on startup.')
mgmdPmRouterInterfaceStaticMulticastMode = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 19), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceStaticMulticastMode.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceStaticMulticastMode.setDescription('If true then this interface will only be able to join groups statically. All querier and dynamic join functionality will be disabled.')
mgmdPmRouterInterfaceBackupProxyIfIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 20), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceBackupProxyIfIndex.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceBackupProxyIfIndex.setDescription('Some devices implement a form of IGMP or MLD proxying whereby memberships learned on the interface represented by this row, cause Host Membership Reports to be sent on the interface whose ifIndex value is given by this object. Such a device would implement the mgmdV2RouterMIBGroup only on its router interfaces (those interfaces with non-zero mgmdPmRouterInterfaceProxyIfIndex). If a proxy interface is defined for an interface a secondary backup proxy interface can be configured for failover operation.')
mgmdPmRouterInterfaceActiveProxyIfIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 21), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceActiveProxyIfIndex.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceActiveProxyIfIndex.setDescription('The active proxy interface.')
mgmdPmRouterInterfaceAccessList = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 22), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 199))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceAccessList.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceAccessList.setDescription('The access list number for filtering multicast group join requests by hosts. Set to 0 for no filtering. Only Standard ACLs (in the range 1-99) are supported.')
mgmdPmRouterInterfaceIgmpResetCounts = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 23), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceIgmpResetCounts.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceIgmpResetCounts.setDescription('Reset the send and receive counts and intervals')
mgmdPmRouterInterfaceIgmpCountIntvl = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 24), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceIgmpCountIntvl.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceIgmpCountIntvl.setDescription('The time interval in seconds that IGMP receive and send packets were counted')
mgmdPmRouterInterfaceIgmpRcvCount = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 25), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceIgmpRcvCount.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceIgmpRcvCount.setDescription('The number of IGMP packets received during the count interval')
mgmdPmRouterInterfaceIgmpSendCount = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 26), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceIgmpSendCount.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceIgmpSendCount.setDescription('The number of IGMP packets sent during the count interval')
mgmdPmRouterInterfaceProxyAutoSwitchback = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 27), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdPmRouterInterfaceProxyAutoSwitchback.setStatus('current')
if mibBuilder.loadTexts: mgmdPmRouterInterfaceProxyAutoSwitchback.setDescription('If set to true then auto-switchback mode is enabled. If set to false then auto-switchback mode is disabled.')
mibBuilder.exportSymbols("DC-MGMD-MIB", mgmdPmRouterInterfaceActiveProxyIfIndex=mgmdPmRouterInterfaceActiveProxyIfIndex, mgmdPmEntIndex=mgmdPmEntIndex, mgmdPmStaticGroupEntityType=mgmdPmStaticGroupEntityType, mgmdPmMjEntIndex=mgmdPmMjEntIndex, mgmdPmRouterInterfaceProxyAutoSwitchback=mgmdPmRouterInterfaceProxyAutoSwitchback, mgmdPmRouterInterfaceIgmpSendCount=mgmdPmRouterInterfaceIgmpSendCount, OperStatus=OperStatus, PYSNMP_MODULE_ID=dcMgmdMib, mgmdPmRouterInterfaceQueryInterval=mgmdPmRouterInterfaceQueryInterval, mgmdPmRouterInterfaceEntry=mgmdPmRouterInterfaceEntry, mgmdPmRouterInterfaceStatus=mgmdPmRouterInterfaceStatus, mgmdPmRouterInterfaceIgmpRcvCount=mgmdPmRouterInterfaceIgmpRcvCount, mgmdPmRouterInterfaceQuerierUpTime=mgmdPmRouterInterfaceQuerierUpTime, mgmdPmRouterInterfaceProxyIfIndex=mgmdPmRouterInterfaceProxyIfIndex, mgmdPmRouterInterfaceIgmpResetCounts=mgmdPmRouterInterfaceIgmpResetCounts, mgmdPmMjAdminStatus=mgmdPmMjAdminStatus, InterfaceType=InterfaceType, mgmdPmMjOperStatus=mgmdPmMjOperStatus, PmIndex=PmIndex, mgmdPmEntRowStatus=mgmdPmEntRowStatus, mgmdPmRouterInterfaceQueryMaxResponseTime=mgmdPmRouterInterfaceQueryMaxResponseTime, mgmdPmEntEntry=mgmdPmEntEntry, NonZeroUnsigned8=NonZeroUnsigned8, mgmdPmRouterInterfaceQuerier=mgmdPmRouterInterfaceQuerier, mgmdPmRouterInterfaceJoins=mgmdPmRouterInterfaceJoins, mgmdPmRouterInterfaceQuerierExpiryTime=mgmdPmRouterInterfaceQuerierExpiryTime, mgmdPmRouterInterfaceRobustness=mgmdPmRouterInterfaceRobustness, mgmdPmRouterInterfaceStaticMulticastMode=mgmdPmRouterInterfaceStaticMulticastMode, mgmdPmEntOperStatus=mgmdPmEntOperStatus, MjStatus=MjStatus, dcMgmdMib=dcMgmdMib, MgmdEntityType=MgmdEntityType, mgmdPmMjPartnerIndex=mgmdPmMjPartnerIndex, mgmdPmRouterInterfaceWrongVersionQueries=mgmdPmRouterInterfaceWrongVersionQueries, mgmdPmRouterInterfaceAccessList=mgmdPmRouterInterfaceAccessList, mgmdPmStaticGroupEntry=mgmdPmStaticGroupEntry, mgmdPmStaticGroupAddressType=mgmdPmStaticGroupAddressType, mgmdPmRouterInterfaceVersion=mgmdPmRouterInterfaceVersion, mgmdPmStaticGroupStatus=mgmdPmStaticGroupStatus, mgmdPmStaticGroupIfIndex=mgmdPmStaticGroupIfIndex, NonZeroInteger=NonZeroInteger, mgmdPmMjInterfaceId=mgmdPmMjInterfaceId, mgmdPmRouterInterfaceQuerierType=mgmdPmRouterInterfaceQuerierType, mgmdPmRouterInterfaceTable=mgmdPmRouterInterfaceTable, mgmdPmMjEntry=mgmdPmMjEntry, mgmdPmMjJoinStatus=mgmdPmMjJoinStatus, mgmdPmRouterInterfaceStartupQueryCount=mgmdPmRouterInterfaceStartupQueryCount, mgmdPmRouterInterfaceIgmpCountIntvl=mgmdPmRouterInterfaceIgmpCountIntvl, mgmdPmRouterInterfaceLastMembQueryIntvl=mgmdPmRouterInterfaceLastMembQueryIntvl, mgmdPmStaticGroupAddress=mgmdPmStaticGroupAddress, mgmdPmRouterInterfaceIfIndex=mgmdPmRouterInterfaceIfIndex, mgmdPmRouterInterfaceStartupQueryInterval=mgmdPmRouterInterfaceStartupQueryInterval, mgmdPmRouterInterfaceBackupProxyIfIndex=mgmdPmRouterInterfaceBackupProxyIfIndex, mgmdPmStaticGroupSourceAddress=mgmdPmStaticGroupSourceAddress, mgmdPmEntTable=mgmdPmEntTable, mgmdPmEntAdminStatus=mgmdPmEntAdminStatus, AdminStatus=AdminStatus, mgmdPmStaticGroupTable=mgmdPmStaticGroupTable, mgmdPmRouterInterfaceLastMembQueryCount=mgmdPmRouterInterfaceLastMembQueryCount, mgmdPmStaticGroupStorageType=mgmdPmStaticGroupStorageType, mgmdPmRouterInterfaceGroups=mgmdPmRouterInterfaceGroups, mgmdPmMjRowStatus=mgmdPmMjRowStatus, mgmdPmMjTable=mgmdPmMjTable)