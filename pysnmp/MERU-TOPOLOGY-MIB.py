# SNMP MIB module (MERU-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-TOPOLOGY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:16 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlApIfModeType,
 MwlApType,
 MwlAssociationState,
 MwlCapabilityModeBits,
 MwlEncryptionAlgorithm,
 MwlOnOffSwitch) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlApIfModeType",
    "MwlApType",
    "MwlAssociationState",
    "MwlCapabilityModeBits",
    "MwlEncryptionAlgorithm",
    "MwlOnOffSwitch")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwTopology = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwApAssignedTable_Object = MibTable
mwApAssignedTable = _MwApAssignedTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1)
)
if mibBuilder.loadTexts:
    mwApAssignedTable.setStatus("current")
_MwApAssignedEntry_Object = MibTableRow
mwApAssignedEntry = _MwApAssignedEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1)
)
mwApAssignedEntry.setIndexNames(
    (0, "MERU-TOPOLOGY-MIB", "mwApAssignedTableIndex"),
)
if mibBuilder.loadTexts:
    mwApAssignedEntry.setStatus("current")
_MwApAssignedTableIndex_Type = Integer32
_MwApAssignedTableIndex_Object = MibTableColumn
mwApAssignedTableIndex = _MwApAssignedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 1),
    _MwApAssignedTableIndex_Type()
)
mwApAssignedTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwApAssignedTableIndex.setStatus("current")
_MwApAssignedApMac_Type = MacAddress
_MwApAssignedApMac_Object = MibTableColumn
mwApAssignedApMac = _MwApAssignedApMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 2),
    _MwApAssignedApMac_Type()
)
mwApAssignedApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedApMac.setStatus("current")
_MwApAssignedEssid_Type = DisplayString
_MwApAssignedEssid_Object = MibTableColumn
mwApAssignedEssid = _MwApAssignedEssid_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 3),
    _MwApAssignedEssid_Type()
)
mwApAssignedEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedEssid.setStatus("current")
_MwApAssigneddbState_Type = MwlAssociationState
_MwApAssigneddbState_Object = MibTableColumn
mwApAssigneddbState = _MwApAssigneddbState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 4),
    _MwApAssigneddbState_Type()
)
mwApAssigneddbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssigneddbState.setStatus("current")
_MwApAssignedPrevRssi_Type = Integer32
_MwApAssignedPrevRssi_Object = MibTableColumn
mwApAssignedPrevRssi = _MwApAssignedPrevRssi_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 5),
    _MwApAssignedPrevRssi_Type()
)
mwApAssignedPrevRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedPrevRssi.setStatus("current")
_MwApAssignedRxPackets_Type = Unsigned32
_MwApAssignedRxPackets_Object = MibTableColumn
mwApAssignedRxPackets = _MwApAssignedRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 6),
    _MwApAssignedRxPackets_Type()
)
mwApAssignedRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedRxPackets.setStatus("current")
_MwApAssignedTxPackets_Type = Unsigned32
_MwApAssignedTxPackets_Object = MibTableColumn
mwApAssignedTxPackets = _MwApAssignedTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 7),
    _MwApAssignedTxPackets_Type()
)
mwApAssignedTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedTxPackets.setStatus("current")
_MwApAssignedRadioType_Type = MwlApIfModeType
_MwApAssignedRadioType_Object = MibTableColumn
mwApAssignedRadioType = _MwApAssignedRadioType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 8),
    _MwApAssignedRadioType_Type()
)
mwApAssignedRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedRadioType.setStatus("current")
_MwApAssignedAuthKeyType_Type = MwlEncryptionAlgorithm
_MwApAssignedAuthKeyType_Object = MibTableColumn
mwApAssignedAuthKeyType = _MwApAssignedAuthKeyType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 9),
    _MwApAssignedAuthKeyType_Type()
)
mwApAssignedAuthKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedAuthKeyType.setStatus("current")
_MwApAssignedCurrentRssi_Type = Integer32
_MwApAssignedCurrentRssi_Object = MibTableColumn
mwApAssignedCurrentRssi = _MwApAssignedCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 10),
    _MwApAssignedCurrentRssi_Type()
)
mwApAssignedCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedCurrentRssi.setStatus("current")
_MwApAssignedNmsApNodeId_Type = Integer32
_MwApAssignedNmsApNodeId_Object = MibTableColumn
mwApAssignedNmsApNodeId = _MwApAssignedNmsApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 11),
    _MwApAssignedNmsApNodeId_Type()
)
mwApAssignedNmsApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedNmsApNodeId.setStatus("current")
_MwApAssignedApDeviceType_Type = MwlApType
_MwApAssignedApDeviceType_Object = MibTableColumn
mwApAssignedApDeviceType = _MwApAssignedApDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 12),
    _MwApAssignedApDeviceType_Type()
)
mwApAssignedApDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedApDeviceType.setStatus("current")
_MwApAssignedLastActivity_Type = TimeTicks
_MwApAssignedLastActivity_Object = MibTableColumn
mwApAssignedLastActivity = _MwApAssignedLastActivity_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 13),
    _MwApAssignedLastActivity_Type()
)
mwApAssignedLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedLastActivity.setStatus("current")
_MwApAssignedNmsApNodeName_Type = DisplayString
_MwApAssignedNmsApNodeName_Object = MibTableColumn
mwApAssignedNmsApNodeName = _MwApAssignedNmsApNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 14),
    _MwApAssignedNmsApNodeName_Type()
)
mwApAssignedNmsApNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedNmsApNodeName.setStatus("current")
_MwApAssignedVirtualPort_Type = MacAddress
_MwApAssignedVirtualPort_Object = MibTableColumn
mwApAssignedVirtualPort = _MwApAssignedVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 15),
    _MwApAssignedVirtualPort_Type()
)
mwApAssignedVirtualPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedVirtualPort.setStatus("current")
_MwApAssignedCapabilities_Type = MwlCapabilityModeBits
_MwApAssignedCapabilities_Object = MibTableColumn
mwApAssignedCapabilities = _MwApAssignedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 1, 1, 16),
    _MwApAssignedCapabilities_Type()
)
mwApAssignedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApAssignedCapabilities.setStatus("current")
_MwApDiscoveredTable_Object = MibTable
mwApDiscoveredTable = _MwApDiscoveredTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2)
)
if mibBuilder.loadTexts:
    mwApDiscoveredTable.setStatus("current")
_MwApDiscoveredEntry_Object = MibTableRow
mwApDiscoveredEntry = _MwApDiscoveredEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1)
)
mwApDiscoveredEntry.setIndexNames(
    (0, "MERU-TOPOLOGY-MIB", "mwApDiscoveredTableIndex"),
)
if mibBuilder.loadTexts:
    mwApDiscoveredEntry.setStatus("current")
_MwApDiscoveredTableIndex_Type = Integer32
_MwApDiscoveredTableIndex_Object = MibTableColumn
mwApDiscoveredTableIndex = _MwApDiscoveredTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 1),
    _MwApDiscoveredTableIndex_Type()
)
mwApDiscoveredTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwApDiscoveredTableIndex.setStatus("current")
_MwApDiscoveredApMac_Type = MacAddress
_MwApDiscoveredApMac_Object = MibTableColumn
mwApDiscoveredApMac = _MwApDiscoveredApMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 2),
    _MwApDiscoveredApMac_Type()
)
mwApDiscoveredApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredApMac.setStatus("current")
_MwApDiscoveredEssid_Type = DisplayString
_MwApDiscoveredEssid_Object = MibTableColumn
mwApDiscoveredEssid = _MwApDiscoveredEssid_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 3),
    _MwApDiscoveredEssid_Type()
)
mwApDiscoveredEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredEssid.setStatus("current")
_MwApDiscoveredBssid_Type = MacAddress
_MwApDiscoveredBssid_Object = MibTableColumn
mwApDiscoveredBssid = _MwApDiscoveredBssid_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 4),
    _MwApDiscoveredBssid_Type()
)
mwApDiscoveredBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredBssid.setStatus("current")
_MwApDiscoveredChannel_Type = Unsigned32
_MwApDiscoveredChannel_Object = MibTableColumn
mwApDiscoveredChannel = _MwApDiscoveredChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 5),
    _MwApDiscoveredChannel_Type()
)
mwApDiscoveredChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredChannel.setStatus("current")
_MwApDiscoveredPrevRssi_Type = Integer32
_MwApDiscoveredPrevRssi_Object = MibTableColumn
mwApDiscoveredPrevRssi = _MwApDiscoveredPrevRssi_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 6),
    _MwApDiscoveredPrevRssi_Type()
)
mwApDiscoveredPrevRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredPrevRssi.setStatus("current")
_MwApDiscoveredRxPackets_Type = Unsigned32
_MwApDiscoveredRxPackets_Object = MibTableColumn
mwApDiscoveredRxPackets = _MwApDiscoveredRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 7),
    _MwApDiscoveredRxPackets_Type()
)
mwApDiscoveredRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredRxPackets.setStatus("current")
_MwApDiscoveredRadioType_Type = MwlApIfModeType
_MwApDiscoveredRadioType_Object = MibTableColumn
mwApDiscoveredRadioType = _MwApDiscoveredRadioType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 8),
    _MwApDiscoveredRadioType_Type()
)
mwApDiscoveredRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredRadioType.setStatus("current")
_MwApDiscoveredWiredRogue_Type = MwlOnOffSwitch
_MwApDiscoveredWiredRogue_Object = MibTableColumn
mwApDiscoveredWiredRogue = _MwApDiscoveredWiredRogue_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 9),
    _MwApDiscoveredWiredRogue_Type()
)
mwApDiscoveredWiredRogue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredWiredRogue.setStatus("current")
_MwApDiscoveredCurrentRssi_Type = Integer32
_MwApDiscoveredCurrentRssi_Object = MibTableColumn
mwApDiscoveredCurrentRssi = _MwApDiscoveredCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 10),
    _MwApDiscoveredCurrentRssi_Type()
)
mwApDiscoveredCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredCurrentRssi.setStatus("current")
_MwApDiscoveredNmsApNodeId_Type = Integer32
_MwApDiscoveredNmsApNodeId_Object = MibTableColumn
mwApDiscoveredNmsApNodeId = _MwApDiscoveredNmsApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 11),
    _MwApDiscoveredNmsApNodeId_Type()
)
mwApDiscoveredNmsApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredNmsApNodeId.setStatus("current")
_MwApDiscoveredApDeviceType_Type = MwlApType
_MwApDiscoveredApDeviceType_Object = MibTableColumn
mwApDiscoveredApDeviceType = _MwApDiscoveredApDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 12),
    _MwApDiscoveredApDeviceType_Type()
)
mwApDiscoveredApDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredApDeviceType.setStatus("current")
_MwApDiscoveredLastActivity_Type = TimeTicks
_MwApDiscoveredLastActivity_Object = MibTableColumn
mwApDiscoveredLastActivity = _MwApDiscoveredLastActivity_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 13),
    _MwApDiscoveredLastActivity_Type()
)
mwApDiscoveredLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredLastActivity.setStatus("current")
_MwApDiscoveredNmsApNodeName_Type = DisplayString
_MwApDiscoveredNmsApNodeName_Object = MibTableColumn
mwApDiscoveredNmsApNodeName = _MwApDiscoveredNmsApNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 14),
    _MwApDiscoveredNmsApNodeName_Type()
)
mwApDiscoveredNmsApNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredNmsApNodeName.setStatus("current")
_MwApDiscoveredConfirmedChannel_Type = Unsigned32
_MwApDiscoveredConfirmedChannel_Object = MibTableColumn
mwApDiscoveredConfirmedChannel = _MwApDiscoveredConfirmedChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 2, 1, 15),
    _MwApDiscoveredConfirmedChannel_Type()
)
mwApDiscoveredConfirmedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApDiscoveredConfirmedChannel.setStatus("current")
_MwTopoApTable_Object = MibTable
mwTopoApTable = _MwTopoApTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 4)
)
if mibBuilder.loadTexts:
    mwTopoApTable.setStatus("current")
_MwTopoApEntry_Object = MibTableRow
mwTopoApEntry = _MwTopoApEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 4, 1)
)
mwTopoApEntry.setIndexNames(
    (0, "MERU-TOPOLOGY-MIB", "mwTopoApTableIndex"),
)
if mibBuilder.loadTexts:
    mwTopoApEntry.setStatus("current")
_MwTopoApTableIndex_Type = Integer32
_MwTopoApTableIndex_Object = MibTableColumn
mwTopoApTableIndex = _MwTopoApTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 4, 1, 1),
    _MwTopoApTableIndex_Type()
)
mwTopoApTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwTopoApTableIndex.setStatus("current")
_MwTopoApNodeId_Type = Unsigned32
_MwTopoApNodeId_Object = MibTableColumn
mwTopoApNodeId = _MwTopoApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 4, 1, 2),
    _MwTopoApNodeId_Type()
)
mwTopoApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApNodeId.setStatus("current")
_MwTopoApNodeName_Type = DisplayString
_MwTopoApNodeName_Object = MibTableColumn
mwTopoApNodeName = _MwTopoApNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 4, 1, 3),
    _MwTopoApNodeName_Type()
)
mwTopoApNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApNodeName.setStatus("current")
_MwTopoApAttachedCount_Type = Unsigned32
_MwTopoApAttachedCount_Object = MibTableColumn
mwTopoApAttachedCount = _MwTopoApAttachedCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 4, 1, 4),
    _MwTopoApAttachedCount_Type()
)
mwTopoApAttachedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApAttachedCount.setStatus("current")
_MwTopoApAssignedCount_Type = Unsigned32
_MwTopoApAssignedCount_Object = MibTableColumn
mwTopoApAssignedCount = _MwTopoApAssignedCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 4, 1, 5),
    _MwTopoApAssignedCount_Type()
)
mwTopoApAssignedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApAssignedCount.setStatus("current")
_MwTopoApNeighborsCount_Type = Unsigned32
_MwTopoApNeighborsCount_Object = MibTableColumn
mwTopoApNeighborsCount = _MwTopoApNeighborsCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 4, 1, 6),
    _MwTopoApNeighborsCount_Type()
)
mwTopoApNeighborsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApNeighborsCount.setStatus("current")
_MwTopoApResourceRequest_Type = Unsigned32
_MwTopoApResourceRequest_Object = MibTableColumn
mwTopoApResourceRequest = _MwTopoApResourceRequest_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 4, 1, 7),
    _MwTopoApResourceRequest_Type()
)
mwTopoApResourceRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApResourceRequest.setStatus("current")
_MwTopoApResourceAllocated_Type = Unsigned32
_MwTopoApResourceAllocated_Object = MibTableColumn
mwTopoApResourceAllocated = _MwTopoApResourceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 4, 1, 8),
    _MwTopoApResourceAllocated_Type()
)
mwTopoApResourceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApResourceAllocated.setStatus("current")
_MwTopoApapTable_Object = MibTable
mwTopoApapTable = _MwTopoApapTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 5)
)
if mibBuilder.loadTexts:
    mwTopoApapTable.setStatus("current")
_MwTopoApapEntry_Object = MibTableRow
mwTopoApapEntry = _MwTopoApapEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 5, 1)
)
mwTopoApapEntry.setIndexNames(
    (0, "MERU-TOPOLOGY-MIB", "mwTopoApapTableIndex"),
)
if mibBuilder.loadTexts:
    mwTopoApapEntry.setStatus("current")
_MwTopoApapTableIndex_Type = Integer32
_MwTopoApapTableIndex_Object = MibTableColumn
mwTopoApapTableIndex = _MwTopoApapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 5, 1, 1),
    _MwTopoApapTableIndex_Type()
)
mwTopoApapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwTopoApapTableIndex.setStatus("current")
_MwTopoApapHeadId_Type = Unsigned32
_MwTopoApapHeadId_Object = MibTableColumn
mwTopoApapHeadId = _MwTopoApapHeadId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 5, 1, 2),
    _MwTopoApapHeadId_Type()
)
mwTopoApapHeadId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApapHeadId.setStatus("current")
_MwTopoApapTailId_Type = Unsigned32
_MwTopoApapTailId_Object = MibTableColumn
mwTopoApapTailId = _MwTopoApapTailId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 5, 1, 3),
    _MwTopoApapTailId_Type()
)
mwTopoApapTailId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApapTailId.setStatus("current")
_MwTopoApapHeadName_Type = DisplayString
_MwTopoApapHeadName_Object = MibTableColumn
mwTopoApapHeadName = _MwTopoApapHeadName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 5, 1, 4),
    _MwTopoApapHeadName_Type()
)
mwTopoApapHeadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApapHeadName.setStatus("current")
_MwTopoApapTailName_Type = DisplayString
_MwTopoApapTailName_Object = MibTableColumn
mwTopoApapTailName = _MwTopoApapTailName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 5, 1, 5),
    _MwTopoApapTailName_Type()
)
mwTopoApapTailName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoApapTailName.setStatus("current")
_MwTopoStaTable_Object = MibTable
mwTopoStaTable = _MwTopoStaTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6)
)
if mibBuilder.loadTexts:
    mwTopoStaTable.setStatus("current")
_MwTopoStaEntry_Object = MibTableRow
mwTopoStaEntry = _MwTopoStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6, 1)
)
mwTopoStaEntry.setIndexNames(
    (0, "MERU-TOPOLOGY-MIB", "mwTopoStaTableIndex"),
)
if mibBuilder.loadTexts:
    mwTopoStaEntry.setStatus("current")
_MwTopoStaTableIndex_Type = Integer32
_MwTopoStaTableIndex_Object = MibTableColumn
mwTopoStaTableIndex = _MwTopoStaTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6, 1, 1),
    _MwTopoStaTableIndex_Type()
)
mwTopoStaTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwTopoStaTableIndex.setStatus("current")
_MwTopoStaBssId_Type = MacAddress
_MwTopoStaBssId_Object = MibTableColumn
mwTopoStaBssId = _MwTopoStaBssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6, 1, 2),
    _MwTopoStaBssId_Type()
)
mwTopoStaBssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaBssId.setStatus("current")
_MwTopoStaMssId_Type = MacAddress
_MwTopoStaMssId_Object = MibTableColumn
mwTopoStaMssId = _MwTopoStaMssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6, 1, 3),
    _MwTopoStaMssId_Type()
)
mwTopoStaMssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaMssId.setStatus("current")
_MwTopoStaMacAddress_Type = MacAddress
_MwTopoStaMacAddress_Object = MibTableColumn
mwTopoStaMacAddress = _MwTopoStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6, 1, 4),
    _MwTopoStaMacAddress_Type()
)
mwTopoStaMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaMacAddress.setStatus("current")
_MwTopoStaAssocState_Type = MwlAssociationState
_MwTopoStaAssocState_Object = MibTableColumn
mwTopoStaAssocState = _MwTopoStaAssocState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6, 1, 5),
    _MwTopoStaAssocState_Type()
)
mwTopoStaAssocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaAssocState.setStatus("current")
_MwTopoStaAssignedAp_Type = Unsigned32
_MwTopoStaAssignedAp_Object = MibTableColumn
mwTopoStaAssignedAp = _MwTopoStaAssignedAp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6, 1, 6),
    _MwTopoStaAssignedAp_Type()
)
mwTopoStaAssignedAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaAssignedAp.setStatus("current")
_MwTopoStaHandoffTime_Type = DateAndTime
_MwTopoStaHandoffTime_Object = MibTableColumn
mwTopoStaHandoffTime = _MwTopoStaHandoffTime_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6, 1, 7),
    _MwTopoStaHandoffTime_Type()
)
mwTopoStaHandoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaHandoffTime.setStatus("current")
_MwTopoStaLastActiveTime_Type = DateAndTime
_MwTopoStaLastActiveTime_Object = MibTableColumn
mwTopoStaLastActiveTime = _MwTopoStaLastActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6, 1, 8),
    _MwTopoStaLastActiveTime_Type()
)
mwTopoStaLastActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaLastActiveTime.setStatus("current")
_MwTopoStaAssignedApName_Type = DisplayString
_MwTopoStaAssignedApName_Object = MibTableColumn
mwTopoStaAssignedApName = _MwTopoStaAssignedApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 6, 1, 9),
    _MwTopoStaAssignedApName_Type()
)
mwTopoStaAssignedApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaAssignedApName.setStatus("current")
_MwTopoStaapTable_Object = MibTable
mwTopoStaapTable = _MwTopoStaapTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 7)
)
if mibBuilder.loadTexts:
    mwTopoStaapTable.setStatus("current")
_MwTopoStaapEntry_Object = MibTableRow
mwTopoStaapEntry = _MwTopoStaapEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 7, 1)
)
mwTopoStaapEntry.setIndexNames(
    (0, "MERU-TOPOLOGY-MIB", "mwTopoStaapTableIndex"),
)
if mibBuilder.loadTexts:
    mwTopoStaapEntry.setStatus("current")
_MwTopoStaapTableIndex_Type = Integer32
_MwTopoStaapTableIndex_Object = MibTableColumn
mwTopoStaapTableIndex = _MwTopoStaapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 7, 1, 1),
    _MwTopoStaapTableIndex_Type()
)
mwTopoStaapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwTopoStaapTableIndex.setStatus("current")
_MwTopoStaapRssi_Type = Integer32
_MwTopoStaapRssi_Object = MibTableColumn
mwTopoStaapRssi = _MwTopoStaapRssi_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 7, 1, 2),
    _MwTopoStaapRssi_Type()
)
mwTopoStaapRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaapRssi.setStatus("current")
_MwTopoStaapStaId_Type = MacAddress
_MwTopoStaapStaId_Object = MibTableColumn
mwTopoStaapStaId = _MwTopoStaapStaId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 7, 1, 3),
    _MwTopoStaapStaId_Type()
)
mwTopoStaapStaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaapStaId.setStatus("current")
_MwTopoStaapApId_Type = Unsigned32
_MwTopoStaapApId_Object = MibTableColumn
mwTopoStaapApId = _MwTopoStaapApId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 7, 1, 4),
    _MwTopoStaapApId_Type()
)
mwTopoStaapApId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaapApId.setStatus("current")
_MwTopoStaapApName_Type = DisplayString
_MwTopoStaapApName_Object = MibTableColumn
mwTopoStaapApName = _MwTopoStaapApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 7, 1, 5),
    _MwTopoStaapApName_Type()
)
mwTopoStaapApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaapApName.setStatus("current")
_MwTopoStaapAssigned_Type = MwlOnOffSwitch
_MwTopoStaapAssigned_Object = MibTableColumn
mwTopoStaapAssigned = _MwTopoStaapAssigned_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 7, 1, 6),
    _MwTopoStaapAssigned_Type()
)
mwTopoStaapAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwTopoStaapAssigned.setStatus("current")
_MwApNeighborTable_Object = MibTable
mwApNeighborTable = _MwApNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8)
)
if mibBuilder.loadTexts:
    mwApNeighborTable.setStatus("current")
_MwApNeighborEntry_Object = MibTableRow
mwApNeighborEntry = _MwApNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8, 1)
)
mwApNeighborEntry.setIndexNames(
    (0, "MERU-TOPOLOGY-MIB", "mwApNeighborTableIndex"),
)
if mibBuilder.loadTexts:
    mwApNeighborEntry.setStatus("current")
_MwApNeighborTableIndex_Type = Integer32
_MwApNeighborTableIndex_Object = MibTableColumn
mwApNeighborTableIndex = _MwApNeighborTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8, 1, 1),
    _MwApNeighborTableIndex_Type()
)
mwApNeighborTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwApNeighborTableIndex.setStatus("current")
_MwApNeighborNmsApNodeId_Type = Integer32
_MwApNeighborNmsApNodeId_Object = MibTableColumn
mwApNeighborNmsApNodeId = _MwApNeighborNmsApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8, 1, 2),
    _MwApNeighborNmsApNodeId_Type()
)
mwApNeighborNmsApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborNmsApNodeId.setStatus("current")
_MwApNeighborNmsApInterfaceId_Type = Integer32
_MwApNeighborNmsApInterfaceId_Object = MibTableColumn
mwApNeighborNmsApInterfaceId = _MwApNeighborNmsApInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8, 1, 3),
    _MwApNeighborNmsApInterfaceId_Type()
)
mwApNeighborNmsApInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborNmsApInterfaceId.setStatus("current")
_MwApNeighborApMac_Type = MacAddress
_MwApNeighborApMac_Object = MibTableColumn
mwApNeighborApMac = _MwApNeighborApMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8, 1, 4),
    _MwApNeighborApMac_Type()
)
mwApNeighborApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborApMac.setStatus("current")
_MwApNeighborChannel_Type = Unsigned32
_MwApNeighborChannel_Object = MibTableColumn
mwApNeighborChannel = _MwApNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8, 1, 5),
    _MwApNeighborChannel_Type()
)
mwApNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborChannel.setStatus("current")
_MwApNeighborNeighborApId_Type = Integer32
_MwApNeighborNeighborApId_Object = MibTableColumn
mwApNeighborNeighborApId = _MwApNeighborNeighborApId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8, 1, 6),
    _MwApNeighborNeighborApId_Type()
)
mwApNeighborNeighborApId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborNeighborApId.setStatus("current")
_MwApNeighborNeighborApMac_Type = MacAddress
_MwApNeighborNeighborApMac_Object = MibTableColumn
mwApNeighborNeighborApMac = _MwApNeighborNeighborApMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8, 1, 7),
    _MwApNeighborNeighborApMac_Type()
)
mwApNeighborNeighborApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborNeighborApMac.setStatus("current")
_MwApNeighborNeighborApControllerIndex_Type = Integer32
_MwApNeighborNeighborApControllerIndex_Object = MibTableColumn
mwApNeighborNeighborApControllerIndex = _MwApNeighborNeighborApControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8, 1, 8),
    _MwApNeighborNeighborApControllerIndex_Type()
)
mwApNeighborNeighborApControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborNeighborApControllerIndex.setStatus("current")
_MwApNeighborNeighborApCurrentRssi_Type = Integer32
_MwApNeighborNeighborApCurrentRssi_Object = MibTableColumn
mwApNeighborNeighborApCurrentRssi = _MwApNeighborNeighborApCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 8, 1, 9),
    _MwApNeighborNeighborApCurrentRssi_Type()
)
mwApNeighborNeighborApCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborNeighborApCurrentRssi.setStatus("current")
_MwApNeighborDetailsTable_Object = MibTable
mwApNeighborDetailsTable = _MwApNeighborDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9)
)
if mibBuilder.loadTexts:
    mwApNeighborDetailsTable.setStatus("current")
_MwApNeighborDetailsEntry_Object = MibTableRow
mwApNeighborDetailsEntry = _MwApNeighborDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1)
)
mwApNeighborDetailsEntry.setIndexNames(
    (0, "MERU-TOPOLOGY-MIB", "mwApNeighborDetailsTableIndex"),
)
if mibBuilder.loadTexts:
    mwApNeighborDetailsEntry.setStatus("current")
_MwApNeighborDetailsTableIndex_Type = Integer32
_MwApNeighborDetailsTableIndex_Object = MibTableColumn
mwApNeighborDetailsTableIndex = _MwApNeighborDetailsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1, 1),
    _MwApNeighborDetailsTableIndex_Type()
)
mwApNeighborDetailsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwApNeighborDetailsTableIndex.setStatus("current")
_MwApNeighborDetailsNmsApNodeId_Type = Integer32
_MwApNeighborDetailsNmsApNodeId_Object = MibTableColumn
mwApNeighborDetailsNmsApNodeId = _MwApNeighborDetailsNmsApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1, 2),
    _MwApNeighborDetailsNmsApNodeId_Type()
)
mwApNeighborDetailsNmsApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborDetailsNmsApNodeId.setStatus("current")
_MwApNeighborDetailsNmsApInterfaceId_Type = Integer32
_MwApNeighborDetailsNmsApInterfaceId_Object = MibTableColumn
mwApNeighborDetailsNmsApInterfaceId = _MwApNeighborDetailsNmsApInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1, 3),
    _MwApNeighborDetailsNmsApInterfaceId_Type()
)
mwApNeighborDetailsNmsApInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborDetailsNmsApInterfaceId.setStatus("current")
_MwApNeighborDetailsChannel_Type = Unsigned32
_MwApNeighborDetailsChannel_Object = MibTableColumn
mwApNeighborDetailsChannel = _MwApNeighborDetailsChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1, 4),
    _MwApNeighborDetailsChannel_Type()
)
mwApNeighborDetailsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborDetailsChannel.setStatus("current")
_MwApNeighborDetailsLocalAp_Type = Integer32
_MwApNeighborDetailsLocalAp_Object = MibTableColumn
mwApNeighborDetailsLocalAp = _MwApNeighborDetailsLocalAp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1, 5),
    _MwApNeighborDetailsLocalAp_Type()
)
mwApNeighborDetailsLocalAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborDetailsLocalAp.setStatus("current")
_MwApNeighborDetailsRemoteAp_Type = Integer32
_MwApNeighborDetailsRemoteAp_Object = MibTableColumn
mwApNeighborDetailsRemoteAp = _MwApNeighborDetailsRemoteAp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1, 6),
    _MwApNeighborDetailsRemoteAp_Type()
)
mwApNeighborDetailsRemoteAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborDetailsRemoteAp.setStatus("current")
_MwApNeighborDetailsRssiLevel1_Type = Integer32
_MwApNeighborDetailsRssiLevel1_Object = MibTableColumn
mwApNeighborDetailsRssiLevel1 = _MwApNeighborDetailsRssiLevel1_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1, 7),
    _MwApNeighborDetailsRssiLevel1_Type()
)
mwApNeighborDetailsRssiLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborDetailsRssiLevel1.setStatus("current")
_MwApNeighborDetailsRssiLevel2_Type = Integer32
_MwApNeighborDetailsRssiLevel2_Object = MibTableColumn
mwApNeighborDetailsRssiLevel2 = _MwApNeighborDetailsRssiLevel2_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1, 8),
    _MwApNeighborDetailsRssiLevel2_Type()
)
mwApNeighborDetailsRssiLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborDetailsRssiLevel2.setStatus("current")
_MwApNeighborDetailsRssiLevel3_Type = Integer32
_MwApNeighborDetailsRssiLevel3_Object = MibTableColumn
mwApNeighborDetailsRssiLevel3 = _MwApNeighborDetailsRssiLevel3_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1, 9),
    _MwApNeighborDetailsRssiLevel3_Type()
)
mwApNeighborDetailsRssiLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborDetailsRssiLevel3.setStatus("current")
_MwApNeighborDetailsRssiLevel4_Type = Integer32
_MwApNeighborDetailsRssiLevel4_Object = MibTableColumn
mwApNeighborDetailsRssiLevel4 = _MwApNeighborDetailsRssiLevel4_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 13, 9, 1, 10),
    _MwApNeighborDetailsRssiLevel4_Type()
)
mwApNeighborDetailsRssiLevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApNeighborDetailsRssiLevel4.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-TOPOLOGY-MIB",
    **{"mwTopology": mwTopology,
       "mwApAssignedTable": mwApAssignedTable,
       "mwApAssignedEntry": mwApAssignedEntry,
       "mwApAssignedTableIndex": mwApAssignedTableIndex,
       "mwApAssignedApMac": mwApAssignedApMac,
       "mwApAssignedEssid": mwApAssignedEssid,
       "mwApAssigneddbState": mwApAssigneddbState,
       "mwApAssignedPrevRssi": mwApAssignedPrevRssi,
       "mwApAssignedRxPackets": mwApAssignedRxPackets,
       "mwApAssignedTxPackets": mwApAssignedTxPackets,
       "mwApAssignedRadioType": mwApAssignedRadioType,
       "mwApAssignedAuthKeyType": mwApAssignedAuthKeyType,
       "mwApAssignedCurrentRssi": mwApAssignedCurrentRssi,
       "mwApAssignedNmsApNodeId": mwApAssignedNmsApNodeId,
       "mwApAssignedApDeviceType": mwApAssignedApDeviceType,
       "mwApAssignedLastActivity": mwApAssignedLastActivity,
       "mwApAssignedNmsApNodeName": mwApAssignedNmsApNodeName,
       "mwApAssignedVirtualPort": mwApAssignedVirtualPort,
       "mwApAssignedCapabilities": mwApAssignedCapabilities,
       "mwApDiscoveredTable": mwApDiscoveredTable,
       "mwApDiscoveredEntry": mwApDiscoveredEntry,
       "mwApDiscoveredTableIndex": mwApDiscoveredTableIndex,
       "mwApDiscoveredApMac": mwApDiscoveredApMac,
       "mwApDiscoveredEssid": mwApDiscoveredEssid,
       "mwApDiscoveredBssid": mwApDiscoveredBssid,
       "mwApDiscoveredChannel": mwApDiscoveredChannel,
       "mwApDiscoveredPrevRssi": mwApDiscoveredPrevRssi,
       "mwApDiscoveredRxPackets": mwApDiscoveredRxPackets,
       "mwApDiscoveredRadioType": mwApDiscoveredRadioType,
       "mwApDiscoveredWiredRogue": mwApDiscoveredWiredRogue,
       "mwApDiscoveredCurrentRssi": mwApDiscoveredCurrentRssi,
       "mwApDiscoveredNmsApNodeId": mwApDiscoveredNmsApNodeId,
       "mwApDiscoveredApDeviceType": mwApDiscoveredApDeviceType,
       "mwApDiscoveredLastActivity": mwApDiscoveredLastActivity,
       "mwApDiscoveredNmsApNodeName": mwApDiscoveredNmsApNodeName,
       "mwApDiscoveredConfirmedChannel": mwApDiscoveredConfirmedChannel,
       "mwTopoApTable": mwTopoApTable,
       "mwTopoApEntry": mwTopoApEntry,
       "mwTopoApTableIndex": mwTopoApTableIndex,
       "mwTopoApNodeId": mwTopoApNodeId,
       "mwTopoApNodeName": mwTopoApNodeName,
       "mwTopoApAttachedCount": mwTopoApAttachedCount,
       "mwTopoApAssignedCount": mwTopoApAssignedCount,
       "mwTopoApNeighborsCount": mwTopoApNeighborsCount,
       "mwTopoApResourceRequest": mwTopoApResourceRequest,
       "mwTopoApResourceAllocated": mwTopoApResourceAllocated,
       "mwTopoApapTable": mwTopoApapTable,
       "mwTopoApapEntry": mwTopoApapEntry,
       "mwTopoApapTableIndex": mwTopoApapTableIndex,
       "mwTopoApapHeadId": mwTopoApapHeadId,
       "mwTopoApapTailId": mwTopoApapTailId,
       "mwTopoApapHeadName": mwTopoApapHeadName,
       "mwTopoApapTailName": mwTopoApapTailName,
       "mwTopoStaTable": mwTopoStaTable,
       "mwTopoStaEntry": mwTopoStaEntry,
       "mwTopoStaTableIndex": mwTopoStaTableIndex,
       "mwTopoStaBssId": mwTopoStaBssId,
       "mwTopoStaMssId": mwTopoStaMssId,
       "mwTopoStaMacAddress": mwTopoStaMacAddress,
       "mwTopoStaAssocState": mwTopoStaAssocState,
       "mwTopoStaAssignedAp": mwTopoStaAssignedAp,
       "mwTopoStaHandoffTime": mwTopoStaHandoffTime,
       "mwTopoStaLastActiveTime": mwTopoStaLastActiveTime,
       "mwTopoStaAssignedApName": mwTopoStaAssignedApName,
       "mwTopoStaapTable": mwTopoStaapTable,
       "mwTopoStaapEntry": mwTopoStaapEntry,
       "mwTopoStaapTableIndex": mwTopoStaapTableIndex,
       "mwTopoStaapRssi": mwTopoStaapRssi,
       "mwTopoStaapStaId": mwTopoStaapStaId,
       "mwTopoStaapApId": mwTopoStaapApId,
       "mwTopoStaapApName": mwTopoStaapApName,
       "mwTopoStaapAssigned": mwTopoStaapAssigned,
       "mwApNeighborTable": mwApNeighborTable,
       "mwApNeighborEntry": mwApNeighborEntry,
       "mwApNeighborTableIndex": mwApNeighborTableIndex,
       "mwApNeighborNmsApNodeId": mwApNeighborNmsApNodeId,
       "mwApNeighborNmsApInterfaceId": mwApNeighborNmsApInterfaceId,
       "mwApNeighborApMac": mwApNeighborApMac,
       "mwApNeighborChannel": mwApNeighborChannel,
       "mwApNeighborNeighborApId": mwApNeighborNeighborApId,
       "mwApNeighborNeighborApMac": mwApNeighborNeighborApMac,
       "mwApNeighborNeighborApControllerIndex": mwApNeighborNeighborApControllerIndex,
       "mwApNeighborNeighborApCurrentRssi": mwApNeighborNeighborApCurrentRssi,
       "mwApNeighborDetailsTable": mwApNeighborDetailsTable,
       "mwApNeighborDetailsEntry": mwApNeighborDetailsEntry,
       "mwApNeighborDetailsTableIndex": mwApNeighborDetailsTableIndex,
       "mwApNeighborDetailsNmsApNodeId": mwApNeighborDetailsNmsApNodeId,
       "mwApNeighborDetailsNmsApInterfaceId": mwApNeighborDetailsNmsApInterfaceId,
       "mwApNeighborDetailsChannel": mwApNeighborDetailsChannel,
       "mwApNeighborDetailsLocalAp": mwApNeighborDetailsLocalAp,
       "mwApNeighborDetailsRemoteAp": mwApNeighborDetailsRemoteAp,
       "mwApNeighborDetailsRssiLevel1": mwApNeighborDetailsRssiLevel1,
       "mwApNeighborDetailsRssiLevel2": mwApNeighborDetailsRssiLevel2,
       "mwApNeighborDetailsRssiLevel3": mwApNeighborDetailsRssiLevel3,
       "mwApNeighborDetailsRssiLevel4": mwApNeighborDetailsRssiLevel4}
)
