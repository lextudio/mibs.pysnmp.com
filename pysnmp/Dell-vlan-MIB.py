# SNMP MIB module (Dell-vlan-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dell-vlan-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:43 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(VlanList1,
 VlanList2,
 VlanList3,
 VlanList4) = mibBuilder.importSymbols(
    "Dell-BRIDGEMIBOBJECTS-MIB",
    "VlanList1",
    "VlanList2",
    "VlanList3",
    "VlanList4")

(rnd,) = mibBuilder.importSymbols(
    "Dell-MIB",
    "rnd")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

(PortList,
 VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qVlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

vlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 48)
)
vlan.setRevisions(
        ("2006-02-12 00:00",
         "2004-04-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VlanMibVersion_Type = Integer32
_VlanMibVersion_Object = MibScalar
vlanMibVersion = _VlanMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 1),
    _VlanMibVersion_Type()
)
vlanMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMibVersion.setStatus("current")
_VlanMaxTableNumber_Type = Integer32
_VlanMaxTableNumber_Object = MibScalar
vlanMaxTableNumber = _VlanMaxTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 2),
    _VlanMaxTableNumber_Type()
)
vlanMaxTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMaxTableNumber.setStatus("current")
_VlanNameTable_Object = MibTable
vlanNameTable = _VlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 21)
)
if mibBuilder.loadTexts:
    vlanNameTable.setStatus("current")
_VlanNameEntry_Object = MibTableRow
vlanNameEntry = _VlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 21, 1)
)
vlanNameEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanNameName"),
)
if mibBuilder.loadTexts:
    vlanNameEntry.setStatus("current")


class _VlanNameName_Type(DisplayString):
    """Custom type vlanNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VlanNameName_Type.__name__ = "DisplayString"
_VlanNameName_Object = MibTableColumn
vlanNameName = _VlanNameName_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 21, 1, 1),
    _VlanNameName_Type()
)
vlanNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameName.setStatus("current")
_VlanNameTag_Type = Integer32
_VlanNameTag_Object = MibTableColumn
vlanNameTag = _VlanNameTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 21, 1, 2),
    _VlanNameTag_Type()
)
vlanNameTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameTag.setStatus("current")
_VlanNameIfIndex_Type = Integer32
_VlanNameIfIndex_Object = MibTableColumn
vlanNameIfIndex = _VlanNameIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 21, 1, 3),
    _VlanNameIfIndex_Type()
)
vlanNameIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameIfIndex.setStatus("current")
_VlanPortModeTable_Object = MibTable
vlanPortModeTable = _VlanPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 22)
)
if mibBuilder.loadTexts:
    vlanPortModeTable.setStatus("current")
_VlanPortModeEntry_Object = MibTableRow
vlanPortModeEntry = _VlanPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 22, 1)
)
vlanPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanPortModeEntry.setStatus("current")
_VlanPortModeState_Type = Integer32
_VlanPortModeState_Object = MibTableColumn
vlanPortModeState = _VlanPortModeState_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 22, 1, 1),
    _VlanPortModeState_Type()
)
vlanPortModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortModeState.setStatus("current")


class _VlanSendUnknownToAllPorts_Type(TruthValue):
    """Custom type vlanSendUnknownToAllPorts based on TruthValue"""


_VlanSendUnknownToAllPorts_Object = MibScalar
vlanSendUnknownToAllPorts = _VlanSendUnknownToAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 27),
    _VlanSendUnknownToAllPorts_Type()
)
vlanSendUnknownToAllPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSendUnknownToAllPorts.setStatus("current")
_VlanDefaultSupported_Type = TruthValue
_VlanDefaultSupported_Object = MibScalar
vlanDefaultSupported = _VlanDefaultSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 29),
    _VlanDefaultSupported_Type()
)
vlanDefaultSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanDefaultSupported.setStatus("current")
_VlanDot1vSupported_Type = TruthValue
_VlanDot1vSupported_Object = MibScalar
vlanDot1vSupported = _VlanDot1vSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 31),
    _VlanDot1vSupported_Type()
)
vlanDot1vSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanDot1vSupported.setStatus("current")
_VlanDefaultEnabled_Type = TruthValue
_VlanDefaultEnabled_Object = MibScalar
vlanDefaultEnabled = _VlanDefaultEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 32),
    _VlanDefaultEnabled_Type()
)
vlanDefaultEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultEnabled.setStatus("current")
_VlanSpecialTagTable_Object = MibTable
vlanSpecialTagTable = _VlanSpecialTagTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 33)
)
if mibBuilder.loadTexts:
    vlanSpecialTagTable.setStatus("current")
_VlanSpecialTagEntry_Object = MibTableRow
vlanSpecialTagEntry = _VlanSpecialTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 33, 1)
)
vlanSpecialTagEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanSpecialTagEntry.setStatus("current")
_VlanSpecialTagVID_Type = VlanIndex
_VlanSpecialTagVID_Object = MibTableColumn
vlanSpecialTagVID = _VlanSpecialTagVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 33, 1, 1),
    _VlanSpecialTagVID_Type()
)
vlanSpecialTagVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSpecialTagVID.setStatus("current")
_VlanSpecialTagStatus_Type = RowStatus
_VlanSpecialTagStatus_Object = MibTableColumn
vlanSpecialTagStatus = _VlanSpecialTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 33, 1, 2),
    _VlanSpecialTagStatus_Type()
)
vlanSpecialTagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSpecialTagStatus.setStatus("current")
_VlanSpecialTagCurrentTable_Object = MibTable
vlanSpecialTagCurrentTable = _VlanSpecialTagCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 34)
)
if mibBuilder.loadTexts:
    vlanSpecialTagCurrentTable.setStatus("current")
_VlanSpecialTagCurrentEntry_Object = MibTableRow
vlanSpecialTagCurrentEntry = _VlanSpecialTagCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 34, 1)
)
vlanSpecialTagCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanSpecialTagCurrentEntry.setStatus("current")
_VlanSpecialTagCurrentVID_Type = VlanIndex
_VlanSpecialTagCurrentVID_Object = MibTableColumn
vlanSpecialTagCurrentVID = _VlanSpecialTagCurrentVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 34, 1, 1),
    _VlanSpecialTagCurrentVID_Type()
)
vlanSpecialTagCurrentVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpecialTagCurrentVID.setStatus("current")
_VlanSpecialTagCurrentReserved_Type = TruthValue
_VlanSpecialTagCurrentReserved_Object = MibTableColumn
vlanSpecialTagCurrentReserved = _VlanSpecialTagCurrentReserved_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 34, 1, 2),
    _VlanSpecialTagCurrentReserved_Type()
)
vlanSpecialTagCurrentReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpecialTagCurrentReserved.setStatus("current")
_VlanSpecialTagCurrentActive_Type = TruthValue
_VlanSpecialTagCurrentActive_Object = MibTableColumn
vlanSpecialTagCurrentActive = _VlanSpecialTagCurrentActive_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 34, 1, 3),
    _VlanSpecialTagCurrentActive_Type()
)
vlanSpecialTagCurrentActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSpecialTagCurrentActive.setStatus("current")
_VlanPrivateEdgeSupported_Type = TruthValue
_VlanPrivateEdgeSupported_Object = MibScalar
vlanPrivateEdgeSupported = _VlanPrivateEdgeSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 35),
    _VlanPrivateEdgeSupported_Type()
)
vlanPrivateEdgeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateEdgeSupported.setStatus("current")
_VlanPrivateEdgeVersion_Type = Integer32
_VlanPrivateEdgeVersion_Object = MibScalar
vlanPrivateEdgeVersion = _VlanPrivateEdgeVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 36),
    _VlanPrivateEdgeVersion_Type()
)
vlanPrivateEdgeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateEdgeVersion.setStatus("current")
_VlanPrivateEdgeTable_Object = MibTable
vlanPrivateEdgeTable = _VlanPrivateEdgeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 37)
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeTable.setStatus("current")
_VlanPrivateEdgeEntry_Object = MibTableRow
vlanPrivateEdgeEntry = _VlanPrivateEdgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 37, 1)
)
vlanPrivateEdgeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeEntry.setStatus("current")


class _VlanPrivateEdgeUplink_Type(Integer32):
    """Custom type vlanPrivateEdgeUplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPrivateEdgeUplink_Type.__name__ = "Integer32"
_VlanPrivateEdgeUplink_Object = MibTableColumn
vlanPrivateEdgeUplink = _VlanPrivateEdgeUplink_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 37, 1, 1),
    _VlanPrivateEdgeUplink_Type()
)
vlanPrivateEdgeUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateEdgeUplink.setStatus("current")
_VlanPrivateEdgeStatus_Type = RowStatus
_VlanPrivateEdgeStatus_Object = MibTableColumn
vlanPrivateEdgeStatus = _VlanPrivateEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 37, 1, 2),
    _VlanPrivateEdgeStatus_Type()
)
vlanPrivateEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateEdgeStatus.setStatus("current")
_VlanDynamicVlanSupported_Type = TruthValue
_VlanDynamicVlanSupported_Object = MibScalar
vlanDynamicVlanSupported = _VlanDynamicVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 38),
    _VlanDynamicVlanSupported_Type()
)
vlanDynamicVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanDynamicVlanSupported.setStatus("current")
_VlanDynamicVlanTable_Object = MibTable
vlanDynamicVlanTable = _VlanDynamicVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 39)
)
if mibBuilder.loadTexts:
    vlanDynamicVlanTable.setStatus("current")
_VlanDynamicVlanEntry_Object = MibTableRow
vlanDynamicVlanEntry = _VlanDynamicVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 39, 1)
)
vlanDynamicVlanEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanDynamicVlanMacAddress"),
)
if mibBuilder.loadTexts:
    vlanDynamicVlanEntry.setStatus("current")
_VlanDynamicVlanMacAddress_Type = MacAddress
_VlanDynamicVlanMacAddress_Object = MibTableColumn
vlanDynamicVlanMacAddress = _VlanDynamicVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 39, 1, 1),
    _VlanDynamicVlanMacAddress_Type()
)
vlanDynamicVlanMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanDynamicVlanMacAddress.setStatus("current")
_VlanDynamicVlanTag_Type = VlanIndex
_VlanDynamicVlanTag_Object = MibTableColumn
vlanDynamicVlanTag = _VlanDynamicVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 39, 1, 2),
    _VlanDynamicVlanTag_Type()
)
vlanDynamicVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDynamicVlanTag.setStatus("current")
_VlanDynamicVlanStatus_Type = RowStatus
_VlanDynamicVlanStatus_Object = MibTableColumn
vlanDynamicVlanStatus = _VlanDynamicVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 39, 1, 3),
    _VlanDynamicVlanStatus_Type()
)
vlanDynamicVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDynamicVlanStatus.setStatus("current")
_VlanPortModeExtTable_Object = MibTable
vlanPortModeExtTable = _VlanPortModeExtTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 40)
)
if mibBuilder.loadTexts:
    vlanPortModeExtTable.setStatus("current")
_VlanPortModeExtEntry_Object = MibTableRow
vlanPortModeExtEntry = _VlanPortModeExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 40, 1)
)
vlanPortModeExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanPortModeExtEntry.setStatus("current")
_VlanPortModeExtState_Type = Integer32
_VlanPortModeExtState_Object = MibTableColumn
vlanPortModeExtState = _VlanPortModeExtState_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 40, 1, 1),
    _VlanPortModeExtState_Type()
)
vlanPortModeExtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortModeExtState.setStatus("current")
_VlanPortModeExtStatus_Type = RowStatus
_VlanPortModeExtStatus_Object = MibTableColumn
vlanPortModeExtStatus = _VlanPortModeExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 40, 1, 2),
    _VlanPortModeExtStatus_Type()
)
vlanPortModeExtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortModeExtStatus.setStatus("current")
_VlanPrivateSupported_Type = TruthValue
_VlanPrivateSupported_Object = MibScalar
vlanPrivateSupported = _VlanPrivateSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 41),
    _VlanPrivateSupported_Type()
)
vlanPrivateSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateSupported.setStatus("current")
_VlanPrivateTableOld_Object = MibTable
vlanPrivateTableOld = _VlanPrivateTableOld_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 42)
)
if mibBuilder.loadTexts:
    vlanPrivateTableOld.setStatus("current")
_VlanPrivateEntryOld_Object = MibTableRow
vlanPrivateEntryOld = _VlanPrivateEntryOld_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 42, 1)
)
vlanPrivateEntryOld.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanPrivateEntryOld.setStatus("current")


class _VlanPrivateOldIsolatedVlanTag_Type(Integer32):
    """Custom type vlanPrivateOldIsolatedVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanPrivateOldIsolatedVlanTag_Type.__name__ = "Integer32"
_VlanPrivateOldIsolatedVlanTag_Object = MibTableColumn
vlanPrivateOldIsolatedVlanTag = _VlanPrivateOldIsolatedVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 42, 1, 1),
    _VlanPrivateOldIsolatedVlanTag_Type()
)
vlanPrivateOldIsolatedVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateOldIsolatedVlanTag.setStatus("current")
_VlanPrivateOldStatus_Type = RowStatus
_VlanPrivateOldStatus_Object = MibTableColumn
vlanPrivateOldStatus = _VlanPrivateOldStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 42, 1, 2),
    _VlanPrivateOldStatus_Type()
)
vlanPrivateOldStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateOldStatus.setStatus("current")
_VlanPrivateCommunityTable_Object = MibTable
vlanPrivateCommunityTable = _VlanPrivateCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 43)
)
if mibBuilder.loadTexts:
    vlanPrivateCommunityTable.setStatus("current")
_VlanPrivateCommunityEntry_Object = MibTableRow
vlanPrivateCommunityEntry = _VlanPrivateCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 43, 1)
)
vlanPrivateCommunityEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "Dell-vlan-MIB", "vlanPrivateCommunityVlanTag"),
)
if mibBuilder.loadTexts:
    vlanPrivateCommunityEntry.setStatus("current")
_VlanPrivateCommunityVlanTag_Type = VlanIndex
_VlanPrivateCommunityVlanTag_Object = MibTableColumn
vlanPrivateCommunityVlanTag = _VlanPrivateCommunityVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 43, 1, 1),
    _VlanPrivateCommunityVlanTag_Type()
)
vlanPrivateCommunityVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPrivateCommunityVlanTag.setStatus("current")
_VlanPrivateCommunityStatus_Type = RowStatus
_VlanPrivateCommunityStatus_Object = MibTableColumn
vlanPrivateCommunityStatus = _VlanPrivateCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 43, 1, 2),
    _VlanPrivateCommunityStatus_Type()
)
vlanPrivateCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateCommunityStatus.setStatus("current")
_VlanMulticastTvTable_Object = MibTable
vlanMulticastTvTable = _VlanMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 44)
)
if mibBuilder.loadTexts:
    vlanMulticastTvTable.setStatus("current")
_VlanMulticastTvEntry_Object = MibTableRow
vlanMulticastTvEntry = _VlanMulticastTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 44, 1)
)
vlanMulticastTvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanMulticastTvEntry.setStatus("current")
_VlanMulticastTvVID_Type = VlanIndex
_VlanMulticastTvVID_Object = MibTableColumn
vlanMulticastTvVID = _VlanMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 44, 1, 1),
    _VlanMulticastTvVID_Type()
)
vlanMulticastTvVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMulticastTvVID.setStatus("current")
_VlanMulticastTvStatus_Type = RowStatus
_VlanMulticastTvStatus_Object = MibTableColumn
vlanMulticastTvStatus = _VlanMulticastTvStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 44, 1, 2),
    _VlanMulticastTvStatus_Type()
)
vlanMulticastTvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMulticastTvStatus.setStatus("current")
_VlanMacBaseVlanGroupTable_Object = MibTable
vlanMacBaseVlanGroupTable = _VlanMacBaseVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45)
)
if mibBuilder.loadTexts:
    vlanMacBaseVlanGroupTable.setStatus("current")
_VlanMacBaseVlanGroupEntry_Object = MibTableRow
vlanMacBaseVlanGroupEntry = _VlanMacBaseVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45, 1)
)
vlanMacBaseVlanGroupEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanMacBaseVlanMacAddress"),
    (0, "Dell-vlan-MIB", "vlanMacBaseVlanMacMask"),
)
if mibBuilder.loadTexts:
    vlanMacBaseVlanGroupEntry.setStatus("current")
_VlanMacBaseVlanMacAddress_Type = MacAddress
_VlanMacBaseVlanMacAddress_Object = MibTableColumn
vlanMacBaseVlanMacAddress = _VlanMacBaseVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 1),
    _VlanMacBaseVlanMacAddress_Type()
)
vlanMacBaseVlanMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanMacBaseVlanMacAddress.setStatus("current")


class _VlanMacBaseVlanMacMask_Type(Integer32):
    """Custom type vlanMacBaseVlanMacMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 48),
    )


_VlanMacBaseVlanMacMask_Type.__name__ = "Integer32"
_VlanMacBaseVlanMacMask_Object = MibTableColumn
vlanMacBaseVlanMacMask = _VlanMacBaseVlanMacMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 2),
    _VlanMacBaseVlanMacMask_Type()
)
vlanMacBaseVlanMacMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanMacBaseVlanMacMask.setStatus("current")


class _VlanMacBaseVlanGroupId_Type(Integer32):
    """Custom type vlanMacBaseVlanGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VlanMacBaseVlanGroupId_Type.__name__ = "Integer32"
_VlanMacBaseVlanGroupId_Object = MibTableColumn
vlanMacBaseVlanGroupId = _VlanMacBaseVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 3),
    _VlanMacBaseVlanGroupId_Type()
)
vlanMacBaseVlanGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMacBaseVlanGroupId.setStatus("current")
_VlanMacBaseVlanGroupRowStatus_Type = RowStatus
_VlanMacBaseVlanGroupRowStatus_Object = MibTableColumn
vlanMacBaseVlanGroupRowStatus = _VlanMacBaseVlanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 4),
    _VlanMacBaseVlanGroupRowStatus_Type()
)
vlanMacBaseVlanGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMacBaseVlanGroupRowStatus.setStatus("current")
_VlanMacBaseVlanPortTable_Object = MibTable
vlanMacBaseVlanPortTable = _VlanMacBaseVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 46)
)
if mibBuilder.loadTexts:
    vlanMacBaseVlanPortTable.setStatus("current")
_VlanMacBaseVlanPortEntry_Object = MibTableRow
vlanMacBaseVlanPortEntry = _VlanMacBaseVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 46, 1)
)
vlanMacBaseVlanPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "Dell-vlan-MIB", "vlanMacBaseVlanPortGroupId"),
)
if mibBuilder.loadTexts:
    vlanMacBaseVlanPortEntry.setStatus("current")


class _VlanMacBaseVlanPortGroupId_Type(Integer32):
    """Custom type vlanMacBaseVlanPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VlanMacBaseVlanPortGroupId_Type.__name__ = "Integer32"
_VlanMacBaseVlanPortGroupId_Object = MibTableColumn
vlanMacBaseVlanPortGroupId = _VlanMacBaseVlanPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 46, 1, 1),
    _VlanMacBaseVlanPortGroupId_Type()
)
vlanMacBaseVlanPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanMacBaseVlanPortGroupId.setStatus("current")
_VlanMacBaseVlanPortGroupVid_Type = VlanIndex
_VlanMacBaseVlanPortGroupVid_Object = MibTableColumn
vlanMacBaseVlanPortGroupVid = _VlanMacBaseVlanPortGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 46, 1, 2),
    _VlanMacBaseVlanPortGroupVid_Type()
)
vlanMacBaseVlanPortGroupVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMacBaseVlanPortGroupVid.setStatus("current")
_VlanMacBaseVlanPortRowStatus_Type = RowStatus
_VlanMacBaseVlanPortRowStatus_Object = MibTableColumn
vlanMacBaseVlanPortRowStatus = _VlanMacBaseVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 46, 1, 3),
    _VlanMacBaseVlanPortRowStatus_Type()
)
vlanMacBaseVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMacBaseVlanPortRowStatus.setStatus("current")
_VlanPrivateEdgeGroupTable_Object = MibTable
vlanPrivateEdgeGroupTable = _VlanPrivateEdgeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 47)
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupTable.setStatus("current")
_VlanPrivateEdgeGroupEntry_Object = MibTableRow
vlanPrivateEdgeGroupEntry = _VlanPrivateEdgeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 47, 1)
)
vlanPrivateEdgeGroupEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanPrivateEdgeGroupSource"),
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupEntry.setStatus("current")


class _VlanPrivateEdgeGroupSource_Type(Integer32):
    """Custom type vlanPrivateEdgeGroupSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPrivateEdgeGroupSource_Type.__name__ = "Integer32"
_VlanPrivateEdgeGroupSource_Object = MibTableColumn
vlanPrivateEdgeGroupSource = _VlanPrivateEdgeGroupSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 47, 1, 1),
    _VlanPrivateEdgeGroupSource_Type()
)
vlanPrivateEdgeGroupSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupSource.setStatus("current")


class _VlanPrivateEdgeGroupUplink_Type(Integer32):
    """Custom type vlanPrivateEdgeGroupUplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPrivateEdgeGroupUplink_Type.__name__ = "Integer32"
_VlanPrivateEdgeGroupUplink_Object = MibTableColumn
vlanPrivateEdgeGroupUplink = _VlanPrivateEdgeGroupUplink_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 47, 1, 2),
    _VlanPrivateEdgeGroupUplink_Type()
)
vlanPrivateEdgeGroupUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupUplink.setStatus("current")
_VlanPrivateEdgeGroupStatus_Type = RowStatus
_VlanPrivateEdgeGroupStatus_Object = MibTableColumn
vlanPrivateEdgeGroupStatus = _VlanPrivateEdgeGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 47, 1, 3),
    _VlanPrivateEdgeGroupStatus_Type()
)
vlanPrivateEdgeGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupStatus.setStatus("current")
_VlanPrivateEdgeGroupIfIndexTable_Object = MibTable
vlanPrivateEdgeGroupIfIndexTable = _VlanPrivateEdgeGroupIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 48)
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupIfIndexTable.setStatus("current")
_VlanPrivateEdgeGroupIfIndexEntry_Object = MibTableRow
vlanPrivateEdgeGroupIfIndexEntry = _VlanPrivateEdgeGroupIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 48, 1)
)
vlanPrivateEdgeGroupIfIndexEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupIfIndexEntry.setStatus("current")


class _VlanPrivateEdgeGroupIfIndexID_Type(Integer32):
    """Custom type vlanPrivateEdgeGroupIfIndexID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPrivateEdgeGroupIfIndexID_Type.__name__ = "Integer32"
_VlanPrivateEdgeGroupIfIndexID_Object = MibTableColumn
vlanPrivateEdgeGroupIfIndexID = _VlanPrivateEdgeGroupIfIndexID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 48, 1, 1),
    _VlanPrivateEdgeGroupIfIndexID_Type()
)
vlanPrivateEdgeGroupIfIndexID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupIfIndexID.setStatus("current")


class _VlanPrivateEdgeGroupIfIndexDomainID_Type(Integer32):
    """Custom type vlanPrivateEdgeGroupIfIndexDomainID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanPrivateEdgeGroupIfIndexDomainID_Type.__name__ = "Integer32"
_VlanPrivateEdgeGroupIfIndexDomainID_Object = MibTableColumn
vlanPrivateEdgeGroupIfIndexDomainID = _VlanPrivateEdgeGroupIfIndexDomainID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 48, 1, 2),
    _VlanPrivateEdgeGroupIfIndexDomainID_Type()
)
vlanPrivateEdgeGroupIfIndexDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateEdgeGroupIfIndexDomainID.setStatus("current")
_VlanSubnetRangeTable_Object = MibTable
vlanSubnetRangeTable = _VlanSubnetRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49)
)
if mibBuilder.loadTexts:
    vlanSubnetRangeTable.setStatus("current")
_VlanSubnetRangeEntry_Object = MibTableRow
vlanSubnetRangeEntry = _VlanSubnetRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49, 1)
)
vlanSubnetRangeEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanSubnetRangeAddr"),
    (0, "Dell-vlan-MIB", "vlanSubnetRangeMask"),
)
if mibBuilder.loadTexts:
    vlanSubnetRangeEntry.setStatus("current")
_VlanSubnetRangeAddr_Type = IpAddress
_VlanSubnetRangeAddr_Object = MibTableColumn
vlanSubnetRangeAddr = _VlanSubnetRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 1),
    _VlanSubnetRangeAddr_Type()
)
vlanSubnetRangeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSubnetRangeAddr.setStatus("current")


class _VlanSubnetRangeMask_Type(Integer32):
    """Custom type vlanSubnetRangeMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VlanSubnetRangeMask_Type.__name__ = "Integer32"
_VlanSubnetRangeMask_Object = MibTableColumn
vlanSubnetRangeMask = _VlanSubnetRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 2),
    _VlanSubnetRangeMask_Type()
)
vlanSubnetRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSubnetRangeMask.setStatus("current")


class _VlanSubnetRangeGroupId_Type(Integer32):
    """Custom type vlanSubnetRangeGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VlanSubnetRangeGroupId_Type.__name__ = "Integer32"
_VlanSubnetRangeGroupId_Object = MibTableColumn
vlanSubnetRangeGroupId = _VlanSubnetRangeGroupId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 3),
    _VlanSubnetRangeGroupId_Type()
)
vlanSubnetRangeGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanSubnetRangeGroupId.setStatus("current")
_VlanSubnetRangeRowStatus_Type = RowStatus
_VlanSubnetRangeRowStatus_Object = MibTableColumn
vlanSubnetRangeRowStatus = _VlanSubnetRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 4),
    _VlanSubnetRangeRowStatus_Type()
)
vlanSubnetRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanSubnetRangeRowStatus.setStatus("current")
_VlanSubnetPortTable_Object = MibTable
vlanSubnetPortTable = _VlanSubnetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 50)
)
if mibBuilder.loadTexts:
    vlanSubnetPortTable.setStatus("current")
_VlanSubnetPortEntry_Object = MibTableRow
vlanSubnetPortEntry = _VlanSubnetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 50, 1)
)
vlanSubnetPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "Dell-vlan-MIB", "vlanSubnetPortGroupId"),
)
if mibBuilder.loadTexts:
    vlanSubnetPortEntry.setStatus("current")


class _VlanSubnetPortGroupId_Type(Integer32):
    """Custom type vlanSubnetPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VlanSubnetPortGroupId_Type.__name__ = "Integer32"
_VlanSubnetPortGroupId_Object = MibTableColumn
vlanSubnetPortGroupId = _VlanSubnetPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 50, 1, 1),
    _VlanSubnetPortGroupId_Type()
)
vlanSubnetPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanSubnetPortGroupId.setStatus("current")


class _VlanSubnetPortGroupVid_Type(Integer32):
    """Custom type vlanSubnetPortGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanSubnetPortGroupVid_Type.__name__ = "Integer32"
_VlanSubnetPortGroupVid_Object = MibTableColumn
vlanSubnetPortGroupVid = _VlanSubnetPortGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 50, 1, 2),
    _VlanSubnetPortGroupVid_Type()
)
vlanSubnetPortGroupVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanSubnetPortGroupVid.setStatus("current")
_VlanSubnetPortRowStatus_Type = RowStatus
_VlanSubnetPortRowStatus_Object = MibTableColumn
vlanSubnetPortRowStatus = _VlanSubnetPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 50, 1, 3),
    _VlanSubnetPortRowStatus_Type()
)
vlanSubnetPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanSubnetPortRowStatus.setStatus("current")
_VlanTriplePlayTable_Object = MibTable
vlanTriplePlayTable = _VlanTriplePlayTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 51)
)
if mibBuilder.loadTexts:
    vlanTriplePlayTable.setStatus("current")
_VlanTriplePlayEntry_Object = MibTableRow
vlanTriplePlayEntry = _VlanTriplePlayEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 51, 1)
)
vlanTriplePlayEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanTriplePlayInnerVID"),
)
if mibBuilder.loadTexts:
    vlanTriplePlayEntry.setStatus("current")
_VlanTriplePlayInnerVID_Type = VlanIndex
_VlanTriplePlayInnerVID_Object = MibTableColumn
vlanTriplePlayInnerVID = _VlanTriplePlayInnerVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 51, 1, 1),
    _VlanTriplePlayInnerVID_Type()
)
vlanTriplePlayInnerVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanTriplePlayInnerVID.setStatus("current")
_VlanTriplePlayMulticastTvVID_Type = VlanIndex
_VlanTriplePlayMulticastTvVID_Object = MibTableColumn
vlanTriplePlayMulticastTvVID = _VlanTriplePlayMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 51, 1, 2),
    _VlanTriplePlayMulticastTvVID_Type()
)
vlanTriplePlayMulticastTvVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTriplePlayMulticastTvVID.setStatus("current")
_VlanTriplePlayRowStatus_Type = RowStatus
_VlanTriplePlayRowStatus_Object = MibTableColumn
vlanTriplePlayRowStatus = _VlanTriplePlayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 51, 1, 3),
    _VlanTriplePlayRowStatus_Type()
)
vlanTriplePlayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTriplePlayRowStatus.setStatus("current")
_VlanTriplePlayMulticastTvTable_Object = MibTable
vlanTriplePlayMulticastTvTable = _VlanTriplePlayMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 52)
)
if mibBuilder.loadTexts:
    vlanTriplePlayMulticastTvTable.setStatus("current")
_VlanTriplePlayMulticatTvEntry_Object = MibTableRow
vlanTriplePlayMulticatTvEntry = _VlanTriplePlayMulticatTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 52, 1)
)
vlanTriplePlayMulticatTvEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanTriplePlayMulticastTvMulticastTvVID"),
)
if mibBuilder.loadTexts:
    vlanTriplePlayMulticatTvEntry.setStatus("current")
_VlanTriplePlayMulticastTvMulticastTvVID_Type = VlanIndex
_VlanTriplePlayMulticastTvMulticastTvVID_Object = MibTableColumn
vlanTriplePlayMulticastTvMulticastTvVID = _VlanTriplePlayMulticastTvMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 52, 1, 1),
    _VlanTriplePlayMulticastTvMulticastTvVID_Type()
)
vlanTriplePlayMulticastTvMulticastTvVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTriplePlayMulticastTvMulticastTvVID.setStatus("current")
_VlanTriplePlayMulticastTvMulticastTvPortList_Type = PortList
_VlanTriplePlayMulticastTvMulticastTvPortList_Object = MibTableColumn
vlanTriplePlayMulticastTvMulticastTvPortList = _VlanTriplePlayMulticastTvMulticastTvPortList_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 52, 1, 2),
    _VlanTriplePlayMulticastTvMulticastTvPortList_Type()
)
vlanTriplePlayMulticastTvMulticastTvPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTriplePlayMulticastTvMulticastTvPortList.setStatus("current")
_VlanDefaultExtManagment_Type = TruthValue
_VlanDefaultExtManagment_Object = MibScalar
vlanDefaultExtManagment = _VlanDefaultExtManagment_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 53),
    _VlanDefaultExtManagment_Type()
)
vlanDefaultExtManagment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultExtManagment.setStatus("current")
_VlanVoice_ObjectIdentity = ObjectIdentity
vlanVoice = _VlanVoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 48, 54)
)


class _VlanVoiceAgingTimeout_Type(Integer32):
    """Custom type vlanVoiceAgingTimeout based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 43200),
    )


_VlanVoiceAgingTimeout_Type.__name__ = "Integer32"
_VlanVoiceAgingTimeout_Object = MibScalar
vlanVoiceAgingTimeout = _VlanVoiceAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 1),
    _VlanVoiceAgingTimeout_Type()
)
vlanVoiceAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceAgingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vlanVoiceAgingTimeout.setUnits("minutes")
_VlanVoiceTable_Object = MibTable
vlanVoiceTable = _VlanVoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 2)
)
if mibBuilder.loadTexts:
    vlanVoiceTable.setStatus("current")
_VlanVoiceEntry_Object = MibTableRow
vlanVoiceEntry = _VlanVoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 2, 1)
)
vlanVoiceEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanVoiceEntry.setStatus("current")


class _VlanVoicePriority_Type(Integer32):
    """Custom type vlanVoicePriority based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanVoicePriority_Type.__name__ = "Integer32"
_VlanVoicePriority_Object = MibTableColumn
vlanVoicePriority = _VlanVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 2, 1, 1),
    _VlanVoicePriority_Type()
)
vlanVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoicePriority.setStatus("current")


class _VlanVoicePriorityRemark_Type(TruthValue):
    """Custom type vlanVoicePriorityRemark based on TruthValue"""


_VlanVoicePriorityRemark_Object = MibTableColumn
vlanVoicePriorityRemark = _VlanVoicePriorityRemark_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 2, 1, 2),
    _VlanVoicePriorityRemark_Type()
)
vlanVoicePriorityRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanVoicePriorityRemark.setStatus("current")
_VlanVoiceRowStatus_Type = RowStatus
_VlanVoiceRowStatus_Object = MibTableColumn
vlanVoiceRowStatus = _VlanVoiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 2, 1, 3),
    _VlanVoiceRowStatus_Type()
)
vlanVoiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanVoiceRowStatus.setStatus("current")
_VlanVoiceOUITable_Object = MibTable
vlanVoiceOUITable = _VlanVoiceOUITable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 3)
)
if mibBuilder.loadTexts:
    vlanVoiceOUITable.setStatus("current")
_VlanVoiceOUIEntry_Object = MibTableRow
vlanVoiceOUIEntry = _VlanVoiceOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 3, 1)
)
vlanVoiceOUIEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanVoiceOUIPrefix"),
)
if mibBuilder.loadTexts:
    vlanVoiceOUIEntry.setStatus("current")


class _VlanVoiceOUIPrefix_Type(OctetString):
    """Custom type vlanVoiceOUIPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_VlanVoiceOUIPrefix_Type.__name__ = "OctetString"
_VlanVoiceOUIPrefix_Object = MibTableColumn
vlanVoiceOUIPrefix = _VlanVoiceOUIPrefix_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 3, 1, 1),
    _VlanVoiceOUIPrefix_Type()
)
vlanVoiceOUIPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanVoiceOUIPrefix.setStatus("current")


class _VlanVoiceOUIDescription_Type(DisplayString):
    """Custom type vlanVoiceOUIDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanVoiceOUIDescription_Type.__name__ = "DisplayString"
_VlanVoiceOUIDescription_Object = MibTableColumn
vlanVoiceOUIDescription = _VlanVoiceOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 3, 1, 2),
    _VlanVoiceOUIDescription_Type()
)
vlanVoiceOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUIDescription.setStatus("current")
_VlanVoiceOUIEntryRowStatus_Type = RowStatus
_VlanVoiceOUIEntryRowStatus_Object = MibTableColumn
vlanVoiceOUIEntryRowStatus = _VlanVoiceOUIEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 3, 1, 3),
    _VlanVoiceOUIEntryRowStatus_Type()
)
vlanVoiceOUIEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanVoiceOUIEntryRowStatus.setStatus("current")
_VlanVoicePortTable_Object = MibTable
vlanVoicePortTable = _VlanVoicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 4)
)
if mibBuilder.loadTexts:
    vlanVoicePortTable.setStatus("current")
_VlanVoicePortEntry_Object = MibTableRow
vlanVoicePortEntry = _VlanVoicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 4, 1)
)
vlanVoicePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanVoicePortEntry.setStatus("current")


class _VlanVoicePortEnable_Type(TruthValue):
    """Custom type vlanVoicePortEnable based on TruthValue"""


_VlanVoicePortEnable_Object = MibTableColumn
vlanVoicePortEnable = _VlanVoicePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 4, 1, 1),
    _VlanVoicePortEnable_Type()
)
vlanVoicePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoicePortEnable.setStatus("current")


class _VlanVoicePortVlanIndex_Type(VlanIndex):
    """Custom type vlanVoicePortVlanIndex based on VlanIndex"""
    defaultValue = 4095


_VlanVoicePortVlanIndex_Object = MibTableColumn
vlanVoicePortVlanIndex = _VlanVoicePortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 4, 1, 2),
    _VlanVoicePortVlanIndex_Type()
)
vlanVoicePortVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoicePortVlanIndex.setStatus("current")


class _VlanVoicePortSecure_Type(TruthValue):
    """Custom type vlanVoicePortSecure based on TruthValue"""


_VlanVoicePortSecure_Object = MibTableColumn
vlanVoicePortSecure = _VlanVoicePortSecure_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 4, 1, 3),
    _VlanVoicePortSecure_Type()
)
vlanVoicePortSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoicePortSecure.setStatus("current")


class _VlanVoicePortCurrentMembership_Type(Integer32):
    """Custom type vlanVoicePortCurrentMembership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_VlanVoicePortCurrentMembership_Type.__name__ = "Integer32"
_VlanVoicePortCurrentMembership_Object = MibTableColumn
vlanVoicePortCurrentMembership = _VlanVoicePortCurrentMembership_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 4, 1, 4),
    _VlanVoicePortCurrentMembership_Type()
)
vlanVoicePortCurrentMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoicePortCurrentMembership.setStatus("current")


class _VlanVoicePortQosMode_Type(Integer32):
    """Custom type vlanVoicePortQosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("src", 1))
    )


_VlanVoicePortQosMode_Type.__name__ = "Integer32"
_VlanVoicePortQosMode_Object = MibTableColumn
vlanVoicePortQosMode = _VlanVoicePortQosMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 4, 1, 5),
    _VlanVoicePortQosMode_Type()
)
vlanVoicePortQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoicePortQosMode.setStatus("current")


class _VlanVoiceOUISetToDefault_Type(TruthValue):
    """Custom type vlanVoiceOUISetToDefault based on TruthValue"""


_VlanVoiceOUISetToDefault_Object = MibScalar
vlanVoiceOUISetToDefault = _VlanVoiceOUISetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 54, 5),
    _VlanVoiceOUISetToDefault_Type()
)
vlanVoiceOUISetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUISetToDefault.setStatus("current")
_VlanDefault_ObjectIdentity = ObjectIdentity
vlanDefault = _VlanDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 48, 55)
)
_VlanDefaultTaggedPorts_Type = PortList
_VlanDefaultTaggedPorts_Object = MibScalar
vlanDefaultTaggedPorts = _VlanDefaultTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 55, 1),
    _VlanDefaultTaggedPorts_Type()
)
vlanDefaultTaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultTaggedPorts.setStatus("current")
_VlanDefaultEnabledPorts_Type = PortList
_VlanDefaultEnabledPorts_Object = MibScalar
vlanDefaultEnabledPorts = _VlanDefaultEnabledPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 55, 2),
    _VlanDefaultEnabledPorts_Type()
)
vlanDefaultEnabledPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultEnabledPorts.setStatus("current")
_VlanInetTriplePlayTable_Object = MibTable
vlanInetTriplePlayTable = _VlanInetTriplePlayTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 56)
)
if mibBuilder.loadTexts:
    vlanInetTriplePlayTable.setStatus("current")
_VlanInetTriplePlayEntry_Object = MibTableRow
vlanInetTriplePlayEntry = _VlanInetTriplePlayEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 56, 1)
)
vlanInetTriplePlayEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanInetTriplePlayInetAddressType"),
    (0, "Dell-vlan-MIB", "vlanTriplePlayInnerVID"),
)
if mibBuilder.loadTexts:
    vlanInetTriplePlayEntry.setStatus("current")
_VlanInetTriplePlayInetAddressType_Type = InetAddressType
_VlanInetTriplePlayInetAddressType_Object = MibTableColumn
vlanInetTriplePlayInetAddressType = _VlanInetTriplePlayInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 56, 1, 1),
    _VlanInetTriplePlayInetAddressType_Type()
)
vlanInetTriplePlayInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInetTriplePlayInetAddressType.setStatus("current")
_VlanInetTriplePlayInnerVID_Type = VlanIndex
_VlanInetTriplePlayInnerVID_Object = MibTableColumn
vlanInetTriplePlayInnerVID = _VlanInetTriplePlayInnerVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 56, 1, 2),
    _VlanInetTriplePlayInnerVID_Type()
)
vlanInetTriplePlayInnerVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanInetTriplePlayInnerVID.setStatus("current")
_VlanInetTriplePlayMulticastTvVID_Type = VlanIndex
_VlanInetTriplePlayMulticastTvVID_Object = MibTableColumn
vlanInetTriplePlayMulticastTvVID = _VlanInetTriplePlayMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 56, 1, 3),
    _VlanInetTriplePlayMulticastTvVID_Type()
)
vlanInetTriplePlayMulticastTvVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInetTriplePlayMulticastTvVID.setStatus("current")
_VlanInetTriplePlayRowStatus_Type = RowStatus
_VlanInetTriplePlayRowStatus_Object = MibTableColumn
vlanInetTriplePlayRowStatus = _VlanInetTriplePlayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 56, 1, 4),
    _VlanInetTriplePlayRowStatus_Type()
)
vlanInetTriplePlayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInetTriplePlayRowStatus.setStatus("current")
_VlanInetTriplePlayMulticastTvTable_Object = MibTable
vlanInetTriplePlayMulticastTvTable = _VlanInetTriplePlayMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 57)
)
if mibBuilder.loadTexts:
    vlanInetTriplePlayMulticastTvTable.setStatus("current")
_VlanInetTriplePlayMulticatTvEntry_Object = MibTableRow
vlanInetTriplePlayMulticatTvEntry = _VlanInetTriplePlayMulticatTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 57, 1)
)
vlanInetTriplePlayMulticatTvEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanTriplePlayMulticastTvMulticastTvVID"),
)
if mibBuilder.loadTexts:
    vlanInetTriplePlayMulticatTvEntry.setStatus("current")
_VlanInetTriplePlayMulticastTvMulticastTvVID_Type = VlanIndex
_VlanInetTriplePlayMulticastTvMulticastTvVID_Object = MibTableColumn
vlanInetTriplePlayMulticastTvMulticastTvVID = _VlanInetTriplePlayMulticastTvMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 57, 1, 1),
    _VlanInetTriplePlayMulticastTvMulticastTvVID_Type()
)
vlanInetTriplePlayMulticastTvMulticastTvVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInetTriplePlayMulticastTvMulticastTvVID.setStatus("current")
_VlanInetTriplePlayMulticastTvMulticastTvPortList_Type = PortList
_VlanInetTriplePlayMulticastTvMulticastTvPortList_Object = MibTableColumn
vlanInetTriplePlayMulticastTvMulticastTvPortList = _VlanInetTriplePlayMulticastTvMulticastTvPortList_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 57, 1, 2),
    _VlanInetTriplePlayMulticastTvMulticastTvPortList_Type()
)
vlanInetTriplePlayMulticastTvMulticastTvPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanInetTriplePlayMulticastTvMulticastTvPortList.setStatus("current")
_VlanAsymmetricEnabled_Type = TruthValue
_VlanAsymmetricEnabled_Object = MibScalar
vlanAsymmetricEnabled = _VlanAsymmetricEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 58),
    _VlanAsymmetricEnabled_Type()
)
vlanAsymmetricEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAsymmetricEnabled.setStatus("current")
_VlanPrivateTable_Object = MibTable
vlanPrivateTable = _VlanPrivateTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 59)
)
if mibBuilder.loadTexts:
    vlanPrivateTable.setStatus("current")
_VlanPrivateEntry_Object = MibTableRow
vlanPrivateEntry = _VlanPrivateEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 59, 1)
)
vlanPrivateEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanPrivateVid"),
)
if mibBuilder.loadTexts:
    vlanPrivateEntry.setStatus("current")
_VlanPrivateVid_Type = VlanIndex
_VlanPrivateVid_Object = MibTableColumn
vlanPrivateVid = _VlanPrivateVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 59, 1, 1),
    _VlanPrivateVid_Type()
)
vlanPrivateVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPrivateVid.setStatus("current")


class _VlanPrivateType_Type(Integer32):
    """Custom type vlanPrivateType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("community", 3),
          ("isolated", 2),
          ("primary", 1))
    )


_VlanPrivateType_Type.__name__ = "Integer32"
_VlanPrivateType_Object = MibTableColumn
vlanPrivateType = _VlanPrivateType_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 59, 1, 2),
    _VlanPrivateType_Type()
)
vlanPrivateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateType.setStatus("current")
_VlanPrivatePrimaryVid_Type = VlanIndex
_VlanPrivatePrimaryVid_Object = MibTableColumn
vlanPrivatePrimaryVid = _VlanPrivatePrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 59, 1, 3),
    _VlanPrivatePrimaryVid_Type()
)
vlanPrivatePrimaryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivatePrimaryVid.setStatus("current")
_VlanPrivateStatus_Type = RowStatus
_VlanPrivateStatus_Object = MibTableColumn
vlanPrivateStatus = _VlanPrivateStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 59, 1, 4),
    _VlanPrivateStatus_Type()
)
vlanPrivateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateStatus.setStatus("current")
_VlanPrivateMapTable_Object = MibTable
vlanPrivateMapTable = _VlanPrivateMapTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 60)
)
if mibBuilder.loadTexts:
    vlanPrivateMapTable.setStatus("current")
_VlanPrivateMapEntry_Object = MibTableRow
vlanPrivateMapEntry = _VlanPrivateMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 60, 1)
)
vlanPrivateMapEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanPrivateMapPrimaryVid"),
    (0, "Dell-vlan-MIB", "vlanPrivateMapSecondaryVid"),
)
if mibBuilder.loadTexts:
    vlanPrivateMapEntry.setStatus("current")
_VlanPrivateMapPrimaryVid_Type = VlanIndex
_VlanPrivateMapPrimaryVid_Object = MibTableColumn
vlanPrivateMapPrimaryVid = _VlanPrivateMapPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 60, 1, 1),
    _VlanPrivateMapPrimaryVid_Type()
)
vlanPrivateMapPrimaryVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPrivateMapPrimaryVid.setStatus("current")
_VlanPrivateMapSecondaryVid_Type = VlanIndex
_VlanPrivateMapSecondaryVid_Object = MibTableColumn
vlanPrivateMapSecondaryVid = _VlanPrivateMapSecondaryVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 60, 1, 2),
    _VlanPrivateMapSecondaryVid_Type()
)
vlanPrivateMapSecondaryVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPrivateMapSecondaryVid.setStatus("current")
_VlanPrivateMapPrimaryPorts_Type = PortList
_VlanPrivateMapPrimaryPorts_Object = MibTableColumn
vlanPrivateMapPrimaryPorts = _VlanPrivateMapPrimaryPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 60, 1, 3),
    _VlanPrivateMapPrimaryPorts_Type()
)
vlanPrivateMapPrimaryPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateMapPrimaryPorts.setStatus("current")
_VlanPrivateMapSecondaryPorts_Type = PortList
_VlanPrivateMapSecondaryPorts_Object = MibTableColumn
vlanPrivateMapSecondaryPorts = _VlanPrivateMapSecondaryPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 60, 1, 4),
    _VlanPrivateMapSecondaryPorts_Type()
)
vlanPrivateMapSecondaryPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateMapSecondaryPorts.setStatus("current")
_VlanPrivateMapPrimaryOperPorts_Type = PortList
_VlanPrivateMapPrimaryOperPorts_Object = MibTableColumn
vlanPrivateMapPrimaryOperPorts = _VlanPrivateMapPrimaryOperPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 60, 1, 5),
    _VlanPrivateMapPrimaryOperPorts_Type()
)
vlanPrivateMapPrimaryOperPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateMapPrimaryOperPorts.setStatus("current")
_VlanPrivateMapSecondaryOperPorts_Type = PortList
_VlanPrivateMapSecondaryOperPorts_Object = MibTableColumn
vlanPrivateMapSecondaryOperPorts = _VlanPrivateMapSecondaryOperPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 60, 1, 6),
    _VlanPrivateMapSecondaryOperPorts_Type()
)
vlanPrivateMapSecondaryOperPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPrivateMapSecondaryOperPorts.setStatus("current")
_VlanPrivateMapStatus_Type = RowStatus
_VlanPrivateMapStatus_Object = MibTableColumn
vlanPrivateMapStatus = _VlanPrivateMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 60, 1, 7),
    _VlanPrivateMapStatus_Type()
)
vlanPrivateMapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrivateMapStatus.setStatus("current")
_VlanTrunkPortModeTable_Object = MibTable
vlanTrunkPortModeTable = _VlanTrunkPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 61)
)
if mibBuilder.loadTexts:
    vlanTrunkPortModeTable.setStatus("current")
_VlanTrunkPortModeEntry_Object = MibTableRow
vlanTrunkPortModeEntry = _VlanTrunkPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 61, 1)
)
vlanTrunkPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanTrunkPortModeEntry.setStatus("current")


class _VlanTrunkPortModeNativeVlanId_Type(VlanIndex):
    """Custom type vlanTrunkPortModeNativeVlanId based on VlanIndex"""
    defaultValue = 0


_VlanTrunkPortModeNativeVlanId_Object = MibTableColumn
vlanTrunkPortModeNativeVlanId = _VlanTrunkPortModeNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 61, 1, 1),
    _VlanTrunkPortModeNativeVlanId_Type()
)
vlanTrunkPortModeNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkPortModeNativeVlanId.setStatus("current")
_VlanTrunkModeList1to1024_Type = VlanList1
_VlanTrunkModeList1to1024_Object = MibTableColumn
vlanTrunkModeList1to1024 = _VlanTrunkModeList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 61, 1, 2),
    _VlanTrunkModeList1to1024_Type()
)
vlanTrunkModeList1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkModeList1to1024.setStatus("current")
_VlanTrunkModeList1025to2048_Type = VlanList2
_VlanTrunkModeList1025to2048_Object = MibTableColumn
vlanTrunkModeList1025to2048 = _VlanTrunkModeList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 61, 1, 3),
    _VlanTrunkModeList1025to2048_Type()
)
vlanTrunkModeList1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkModeList1025to2048.setStatus("current")
_VlanTrunkModeList2049to3072_Type = VlanList3
_VlanTrunkModeList2049to3072_Object = MibTableColumn
vlanTrunkModeList2049to3072 = _VlanTrunkModeList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 61, 1, 4),
    _VlanTrunkModeList2049to3072_Type()
)
vlanTrunkModeList2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkModeList2049to3072.setStatus("current")
_VlanTrunkModeList3073to4094_Type = VlanList4
_VlanTrunkModeList3073to4094_Object = MibTableColumn
vlanTrunkModeList3073to4094 = _VlanTrunkModeList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 61, 1, 5),
    _VlanTrunkModeList3073to4094_Type()
)
vlanTrunkModeList3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkModeList3073to4094.setStatus("current")
_VlanAccessPortModeTable_Object = MibTable
vlanAccessPortModeTable = _VlanAccessPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 62)
)
if mibBuilder.loadTexts:
    vlanAccessPortModeTable.setStatus("current")
_VlanAccessPortModeEntry_Object = MibTableRow
vlanAccessPortModeEntry = _VlanAccessPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 62, 1)
)
vlanAccessPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanAccessPortModeEntry.setStatus("current")


class _VlanAccessPortModeVlanId_Type(VlanIndex):
    """Custom type vlanAccessPortModeVlanId based on VlanIndex"""
    defaultValue = 0


_VlanAccessPortModeVlanId_Object = MibTableColumn
vlanAccessPortModeVlanId = _VlanAccessPortModeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 62, 1, 1),
    _VlanAccessPortModeVlanId_Type()
)
vlanAccessPortModeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAccessPortModeVlanId.setStatus("current")
_VlanAccessPortModeMcstTvVlanId_Type = VlanIndex
_VlanAccessPortModeMcstTvVlanId_Object = MibTableColumn
vlanAccessPortModeMcstTvVlanId = _VlanAccessPortModeMcstTvVlanId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 62, 1, 2),
    _VlanAccessPortModeMcstTvVlanId_Type()
)
vlanAccessPortModeMcstTvVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAccessPortModeMcstTvVlanId.setStatus("current")
_VlanCustomerPortModeTable_Object = MibTable
vlanCustomerPortModeTable = _VlanCustomerPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 63)
)
if mibBuilder.loadTexts:
    vlanCustomerPortModeTable.setStatus("current")
_VlanCustomerPortModeEntry_Object = MibTableRow
vlanCustomerPortModeEntry = _VlanCustomerPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 63, 1)
)
vlanCustomerPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanCustomerPortModeEntry.setStatus("current")


class _VlanCustomerPortModeVlanId_Type(VlanIndex):
    """Custom type vlanCustomerPortModeVlanId based on VlanIndex"""
    defaultValue = 0


_VlanCustomerPortModeVlanId_Object = MibTableColumn
vlanCustomerPortModeVlanId = _VlanCustomerPortModeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 63, 1, 1),
    _VlanCustomerPortModeVlanId_Type()
)
vlanCustomerPortModeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanCustomerPortModeVlanId.setStatus("current")
_VlanCustomerPortModeMtvList1to1024_Type = VlanList1
_VlanCustomerPortModeMtvList1to1024_Object = MibTableColumn
vlanCustomerPortModeMtvList1to1024 = _VlanCustomerPortModeMtvList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 63, 1, 2),
    _VlanCustomerPortModeMtvList1to1024_Type()
)
vlanCustomerPortModeMtvList1to1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCustomerPortModeMtvList1to1024.setStatus("current")
_VlanCustomerPortModeMtvList1025to2048_Type = VlanList2
_VlanCustomerPortModeMtvList1025to2048_Object = MibTableColumn
vlanCustomerPortModeMtvList1025to2048 = _VlanCustomerPortModeMtvList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 63, 1, 3),
    _VlanCustomerPortModeMtvList1025to2048_Type()
)
vlanCustomerPortModeMtvList1025to2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCustomerPortModeMtvList1025to2048.setStatus("current")
_VlanCustomerPortModeMtvList2049to3072_Type = VlanList3
_VlanCustomerPortModeMtvList2049to3072_Object = MibTableColumn
vlanCustomerPortModeMtvList2049to3072 = _VlanCustomerPortModeMtvList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 63, 1, 4),
    _VlanCustomerPortModeMtvList2049to3072_Type()
)
vlanCustomerPortModeMtvList2049to3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCustomerPortModeMtvList2049to3072.setStatus("current")
_VlanCustomerPortModeMtvList3073to4094_Type = VlanList4
_VlanCustomerPortModeMtvList3073to4094_Object = MibTableColumn
vlanCustomerPortModeMtvList3073to4094 = _VlanCustomerPortModeMtvList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 63, 1, 5),
    _VlanCustomerPortModeMtvList3073to4094_Type()
)
vlanCustomerPortModeMtvList3073to4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCustomerPortModeMtvList3073to4094.setStatus("current")
_VlanSwitchPortModeTable_Object = MibTable
vlanSwitchPortModeTable = _VlanSwitchPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 64)
)
if mibBuilder.loadTexts:
    vlanSwitchPortModeTable.setStatus("current")
_VlanSwitchPortModeEntry_Object = MibTableRow
vlanSwitchPortModeEntry = _VlanSwitchPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 64, 1)
)
vlanSwitchPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanSwitchPortModeEntry.setStatus("current")


class _VlanSwitchPortModeCategory_Type(Integer32):
    """Custom type vlanSwitchPortModeCategory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2", 1),
          ("l3", 2))
    )


_VlanSwitchPortModeCategory_Type.__name__ = "Integer32"
_VlanSwitchPortModeCategory_Object = MibTableColumn
vlanSwitchPortModeCategory = _VlanSwitchPortModeCategory_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 64, 1, 1),
    _VlanSwitchPortModeCategory_Type()
)
vlanSwitchPortModeCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSwitchPortModeCategory.setStatus("current")
_VlanPortModeContextTable_Object = MibTable
vlanPortModeContextTable = _VlanPortModeContextTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 65)
)
if mibBuilder.loadTexts:
    vlanPortModeContextTable.setStatus("current")
_VlanPortModeContextEntry_Object = MibTableRow
vlanPortModeContextEntry = _VlanPortModeContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 65, 1)
)
vlanPortModeContextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanPortModeContextEntry.setStatus("current")
_VlanPortModeContextValue_Type = Integer32
_VlanPortModeContextValue_Object = MibTableColumn
vlanPortModeContextValue = _VlanPortModeContextValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 65, 1, 1),
    _VlanPortModeContextValue_Type()
)
vlanPortModeContextValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortModeContextValue.setStatus("current")


class _VlanRsvlEnable_Type(Integer32):
    """Custom type vlanRsvlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VlanRsvlEnable_Type.__name__ = "Integer32"
_VlanRsvlEnable_Object = MibScalar
vlanRsvlEnable = _VlanRsvlEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 66),
    _VlanRsvlEnable_Type()
)
vlanRsvlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanRsvlEnable.setStatus("current")
_VlanRsvlMapTable_Object = MibTable
vlanRsvlMapTable = _VlanRsvlMapTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 67)
)
if mibBuilder.loadTexts:
    vlanRsvlMapTable.setStatus("current")
_VlanRsvlMapEntry_Object = MibTableRow
vlanRsvlMapEntry = _VlanRsvlMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 67, 1)
)
vlanRsvlMapEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "vlanRsvlMapPrimaryVid"),
    (0, "Dell-vlan-MIB", "vlanRsvlMapSecondaryVid"),
)
if mibBuilder.loadTexts:
    vlanRsvlMapEntry.setStatus("current")
_VlanRsvlMapPrimaryVid_Type = VlanIndex
_VlanRsvlMapPrimaryVid_Object = MibTableColumn
vlanRsvlMapPrimaryVid = _VlanRsvlMapPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 67, 1, 1),
    _VlanRsvlMapPrimaryVid_Type()
)
vlanRsvlMapPrimaryVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanRsvlMapPrimaryVid.setStatus("current")
_VlanRsvlMapSecondaryVid_Type = VlanIndex
_VlanRsvlMapSecondaryVid_Object = MibTableColumn
vlanRsvlMapSecondaryVid = _VlanRsvlMapSecondaryVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 67, 1, 2),
    _VlanRsvlMapSecondaryVid_Type()
)
vlanRsvlMapSecondaryVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanRsvlMapSecondaryVid.setStatus("current")
_VlanRsvlMapStatus_Type = RowStatus
_VlanRsvlMapStatus_Object = MibTableColumn
vlanRsvlMapStatus = _VlanRsvlMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 67, 1, 3),
    _VlanRsvlMapStatus_Type()
)
vlanRsvlMapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanRsvlMapStatus.setStatus("current")
_Rldot1qPortVlanStaticTable_Object = MibTable
rldot1qPortVlanStaticTable = _Rldot1qPortVlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68)
)
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticTable.setStatus("current")
_Rldot1qPortVlanStaticEntry_Object = MibTableRow
rldot1qPortVlanStaticEntry = _Rldot1qPortVlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1)
)
rldot1qPortVlanStaticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticEntry.setStatus("current")


class _Rldot1qPortVlanStaticEgressList1to1024_Type(VlanList1):
    """Custom type rldot1qPortVlanStaticEgressList1to1024 based on VlanList1"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticEgressList1to1024_Object = MibTableColumn
rldot1qPortVlanStaticEgressList1to1024 = _Rldot1qPortVlanStaticEgressList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 1),
    _Rldot1qPortVlanStaticEgressList1to1024_Type()
)
rldot1qPortVlanStaticEgressList1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticEgressList1to1024.setStatus("current")


class _Rldot1qPortVlanStaticEgressList1025to2048_Type(VlanList2):
    """Custom type rldot1qPortVlanStaticEgressList1025to2048 based on VlanList2"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticEgressList1025to2048_Object = MibTableColumn
rldot1qPortVlanStaticEgressList1025to2048 = _Rldot1qPortVlanStaticEgressList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 2),
    _Rldot1qPortVlanStaticEgressList1025to2048_Type()
)
rldot1qPortVlanStaticEgressList1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticEgressList1025to2048.setStatus("current")


class _Rldot1qPortVlanStaticEgressList2049to3072_Type(VlanList3):
    """Custom type rldot1qPortVlanStaticEgressList2049to3072 based on VlanList3"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticEgressList2049to3072_Object = MibTableColumn
rldot1qPortVlanStaticEgressList2049to3072 = _Rldot1qPortVlanStaticEgressList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 3),
    _Rldot1qPortVlanStaticEgressList2049to3072_Type()
)
rldot1qPortVlanStaticEgressList2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticEgressList2049to3072.setStatus("current")


class _Rldot1qPortVlanStaticEgressList3073to4094_Type(VlanList4):
    """Custom type rldot1qPortVlanStaticEgressList3073to4094 based on VlanList4"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticEgressList3073to4094_Object = MibTableColumn
rldot1qPortVlanStaticEgressList3073to4094 = _Rldot1qPortVlanStaticEgressList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 4),
    _Rldot1qPortVlanStaticEgressList3073to4094_Type()
)
rldot1qPortVlanStaticEgressList3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticEgressList3073to4094.setStatus("current")


class _Rldot1qPortVlanStaticUntaggedEgressList1to1024_Type(VlanList1):
    """Custom type rldot1qPortVlanStaticUntaggedEgressList1to1024 based on VlanList1"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticUntaggedEgressList1to1024_Object = MibTableColumn
rldot1qPortVlanStaticUntaggedEgressList1to1024 = _Rldot1qPortVlanStaticUntaggedEgressList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 5),
    _Rldot1qPortVlanStaticUntaggedEgressList1to1024_Type()
)
rldot1qPortVlanStaticUntaggedEgressList1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticUntaggedEgressList1to1024.setStatus("current")


class _Rldot1qPortVlanStaticUntaggedEgressList1025to2048_Type(VlanList2):
    """Custom type rldot1qPortVlanStaticUntaggedEgressList1025to2048 based on VlanList2"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticUntaggedEgressList1025to2048_Object = MibTableColumn
rldot1qPortVlanStaticUntaggedEgressList1025to2048 = _Rldot1qPortVlanStaticUntaggedEgressList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 6),
    _Rldot1qPortVlanStaticUntaggedEgressList1025to2048_Type()
)
rldot1qPortVlanStaticUntaggedEgressList1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticUntaggedEgressList1025to2048.setStatus("current")


class _Rldot1qPortVlanStaticUntaggedEgressList2049to3072_Type(VlanList3):
    """Custom type rldot1qPortVlanStaticUntaggedEgressList2049to3072 based on VlanList3"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticUntaggedEgressList2049to3072_Object = MibTableColumn
rldot1qPortVlanStaticUntaggedEgressList2049to3072 = _Rldot1qPortVlanStaticUntaggedEgressList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 7),
    _Rldot1qPortVlanStaticUntaggedEgressList2049to3072_Type()
)
rldot1qPortVlanStaticUntaggedEgressList2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticUntaggedEgressList2049to3072.setStatus("current")


class _Rldot1qPortVlanStaticUntaggedEgressList3073to4094_Type(VlanList4):
    """Custom type rldot1qPortVlanStaticUntaggedEgressList3073to4094 based on VlanList4"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticUntaggedEgressList3073to4094_Object = MibTableColumn
rldot1qPortVlanStaticUntaggedEgressList3073to4094 = _Rldot1qPortVlanStaticUntaggedEgressList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 8),
    _Rldot1qPortVlanStaticUntaggedEgressList3073to4094_Type()
)
rldot1qPortVlanStaticUntaggedEgressList3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticUntaggedEgressList3073to4094.setStatus("current")


class _Rldot1qPortVlanStaticForbiddenList1to1024_Type(VlanList1):
    """Custom type rldot1qPortVlanStaticForbiddenList1to1024 based on VlanList1"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticForbiddenList1to1024_Object = MibTableColumn
rldot1qPortVlanStaticForbiddenList1to1024 = _Rldot1qPortVlanStaticForbiddenList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 9),
    _Rldot1qPortVlanStaticForbiddenList1to1024_Type()
)
rldot1qPortVlanStaticForbiddenList1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticForbiddenList1to1024.setStatus("current")


class _Rldot1qPortVlanStaticForbiddenList1025to2048_Type(VlanList2):
    """Custom type rldot1qPortVlanStaticForbiddenList1025to2048 based on VlanList2"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticForbiddenList1025to2048_Object = MibTableColumn
rldot1qPortVlanStaticForbiddenList1025to2048 = _Rldot1qPortVlanStaticForbiddenList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 10),
    _Rldot1qPortVlanStaticForbiddenList1025to2048_Type()
)
rldot1qPortVlanStaticForbiddenList1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticForbiddenList1025to2048.setStatus("current")


class _Rldot1qPortVlanStaticForbiddenList2049to3072_Type(VlanList3):
    """Custom type rldot1qPortVlanStaticForbiddenList2049to3072 based on VlanList3"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticForbiddenList2049to3072_Object = MibTableColumn
rldot1qPortVlanStaticForbiddenList2049to3072 = _Rldot1qPortVlanStaticForbiddenList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 11),
    _Rldot1qPortVlanStaticForbiddenList2049to3072_Type()
)
rldot1qPortVlanStaticForbiddenList2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticForbiddenList2049to3072.setStatus("current")


class _Rldot1qPortVlanStaticForbiddenList3073to4094_Type(VlanList4):
    """Custom type rldot1qPortVlanStaticForbiddenList3073to4094 based on VlanList4"""
    defaultHexValue = "00"


_Rldot1qPortVlanStaticForbiddenList3073to4094_Object = MibTableColumn
rldot1qPortVlanStaticForbiddenList3073to4094 = _Rldot1qPortVlanStaticForbiddenList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 68, 1, 12),
    _Rldot1qPortVlanStaticForbiddenList3073to4094_Type()
)
rldot1qPortVlanStaticForbiddenList3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qPortVlanStaticForbiddenList3073to4094.setStatus("current")
_Rldot1qVlanStaticListTable_Object = MibTable
rldot1qVlanStaticListTable = _Rldot1qVlanStaticListTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 69)
)
if mibBuilder.loadTexts:
    rldot1qVlanStaticListTable.setStatus("current")
_Rldot1qVlanStaticListEntry_Object = MibTableRow
rldot1qVlanStaticListEntry = _Rldot1qVlanStaticListEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 69, 1)
)
rldot1qVlanStaticListEntry.setIndexNames(
    (0, "Dell-vlan-MIB", "rldot1qVlanStaticListIndex"),
)
if mibBuilder.loadTexts:
    rldot1qVlanStaticListEntry.setStatus("current")


class _Rldot1qVlanStaticListIndex_Type(Integer32):
    """Custom type rldot1qVlanStaticListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicGvrp", 1),
          ("dynamicRava", 2),
          ("static", 0))
    )


_Rldot1qVlanStaticListIndex_Type.__name__ = "Integer32"
_Rldot1qVlanStaticListIndex_Object = MibTableColumn
rldot1qVlanStaticListIndex = _Rldot1qVlanStaticListIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 69, 1, 1),
    _Rldot1qVlanStaticListIndex_Type()
)
rldot1qVlanStaticListIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qVlanStaticListIndex.setStatus("current")
_Rldot1qVlanStaticList1to1024_Type = VlanList1
_Rldot1qVlanStaticList1to1024_Object = MibTableColumn
rldot1qVlanStaticList1to1024 = _Rldot1qVlanStaticList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 69, 1, 2),
    _Rldot1qVlanStaticList1to1024_Type()
)
rldot1qVlanStaticList1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qVlanStaticList1to1024.setStatus("current")


class _Rldot1qVlanStaticList1025to2048_Type(VlanList2):
    """Custom type rldot1qVlanStaticList1025to2048 based on VlanList2"""
    defaultHexValue = "00"


_Rldot1qVlanStaticList1025to2048_Object = MibTableColumn
rldot1qVlanStaticList1025to2048 = _Rldot1qVlanStaticList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 69, 1, 3),
    _Rldot1qVlanStaticList1025to2048_Type()
)
rldot1qVlanStaticList1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qVlanStaticList1025to2048.setStatus("current")


class _Rldot1qVlanStaticList2049to3072_Type(VlanList3):
    """Custom type rldot1qVlanStaticList2049to3072 based on VlanList3"""
    defaultHexValue = "00"


_Rldot1qVlanStaticList2049to3072_Object = MibTableColumn
rldot1qVlanStaticList2049to3072 = _Rldot1qVlanStaticList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 69, 1, 4),
    _Rldot1qVlanStaticList2049to3072_Type()
)
rldot1qVlanStaticList2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qVlanStaticList2049to3072.setStatus("current")


class _Rldot1qVlanStaticList3073to4094_Type(VlanList4):
    """Custom type rldot1qVlanStaticList3073to4094 based on VlanList4"""
    defaultHexValue = "00"


_Rldot1qVlanStaticList3073to4094_Object = MibTableColumn
rldot1qVlanStaticList3073to4094 = _Rldot1qVlanStaticList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 69, 1, 5),
    _Rldot1qVlanStaticList3073to4094_Type()
)
rldot1qVlanStaticList3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qVlanStaticList3073to4094.setStatus("current")
_Rldot1qVlanStaticNameTable_Object = MibTable
rldot1qVlanStaticNameTable = _Rldot1qVlanStaticNameTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 70)
)
if mibBuilder.loadTexts:
    rldot1qVlanStaticNameTable.setStatus("current")
_Rldot1qVlanStaticNameEntry_Object = MibTableRow
rldot1qVlanStaticNameEntry = _Rldot1qVlanStaticNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 70, 1)
)
rldot1qVlanStaticNameEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    rldot1qVlanStaticNameEntry.setStatus("current")


class _Rldot1qVlanStaticName_Type(SnmpAdminString):
    """Custom type rldot1qVlanStaticName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Rldot1qVlanStaticName_Type.__name__ = "SnmpAdminString"
_Rldot1qVlanStaticName_Object = MibTableColumn
rldot1qVlanStaticName = _Rldot1qVlanStaticName_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 70, 1, 1),
    _Rldot1qVlanStaticName_Type()
)
rldot1qVlanStaticName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1qVlanStaticName.setStatus("current")
_RlPortVlanTriplePlayMulticastTvTable_Object = MibTable
rlPortVlanTriplePlayMulticastTvTable = _RlPortVlanTriplePlayMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 71)
)
if mibBuilder.loadTexts:
    rlPortVlanTriplePlayMulticastTvTable.setStatus("current")
_RlPortVlanTriplePlayMulticastTvEntry_Object = MibTableRow
rlPortVlanTriplePlayMulticastTvEntry = _RlPortVlanTriplePlayMulticastTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 71, 1)
)
rlPortVlanTriplePlayMulticastTvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlPortVlanTriplePlayMulticastTvEntry.setStatus("current")
_RlPortVlanTriplePlayMulticastTvList1to1024_Type = VlanList1
_RlPortVlanTriplePlayMulticastTvList1to1024_Object = MibTableColumn
rlPortVlanTriplePlayMulticastTvList1to1024 = _RlPortVlanTriplePlayMulticastTvList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 71, 1, 1),
    _RlPortVlanTriplePlayMulticastTvList1to1024_Type()
)
rlPortVlanTriplePlayMulticastTvList1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortVlanTriplePlayMulticastTvList1to1024.setStatus("current")
_RlPortVlanTriplePlayMulticastTvList1025to2048_Type = VlanList2
_RlPortVlanTriplePlayMulticastTvList1025to2048_Object = MibTableColumn
rlPortVlanTriplePlayMulticastTvList1025to2048 = _RlPortVlanTriplePlayMulticastTvList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 71, 1, 2),
    _RlPortVlanTriplePlayMulticastTvList1025to2048_Type()
)
rlPortVlanTriplePlayMulticastTvList1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortVlanTriplePlayMulticastTvList1025to2048.setStatus("current")
_RlPortVlanTriplePlayMulticastTvList2049to3072_Type = VlanList3
_RlPortVlanTriplePlayMulticastTvList2049to3072_Object = MibTableColumn
rlPortVlanTriplePlayMulticastTvList2049to3072 = _RlPortVlanTriplePlayMulticastTvList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 71, 1, 3),
    _RlPortVlanTriplePlayMulticastTvList2049to3072_Type()
)
rlPortVlanTriplePlayMulticastTvList2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortVlanTriplePlayMulticastTvList2049to3072.setStatus("current")
_RlPortVlanTriplePlayMulticastTvList3073to4094_Type = VlanList4
_RlPortVlanTriplePlayMulticastTvList3073to4094_Object = MibTableColumn
rlPortVlanTriplePlayMulticastTvList3073to4094 = _RlPortVlanTriplePlayMulticastTvList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 71, 1, 4),
    _RlPortVlanTriplePlayMulticastTvList3073to4094_Type()
)
rlPortVlanTriplePlayMulticastTvList3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortVlanTriplePlayMulticastTvList3073to4094.setStatus("current")
_Rldot1qVlanMembershipTypeTable_Object = MibTable
rldot1qVlanMembershipTypeTable = _Rldot1qVlanMembershipTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 72)
)
if mibBuilder.loadTexts:
    rldot1qVlanMembershipTypeTable.setStatus("current")
_Rldot1qVlanMembershipTypeEntry_Object = MibTableRow
rldot1qVlanMembershipTypeEntry = _Rldot1qVlanMembershipTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 72, 1)
)
rldot1qVlanMembershipTypeEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    rldot1qVlanMembershipTypeEntry.setStatus("current")
_Rldot1qVlanMembershipTypeBitmap_Type = Integer32
_Rldot1qVlanMembershipTypeBitmap_Object = MibTableColumn
rldot1qVlanMembershipTypeBitmap = _Rldot1qVlanMembershipTypeBitmap_Object(
    (1, 3, 6, 1, 4, 1, 89, 48, 72, 1, 1),
    _Rldot1qVlanMembershipTypeBitmap_Type()
)
rldot1qVlanMembershipTypeBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1qVlanMembershipTypeBitmap.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dell-vlan-MIB",
    **{"vlan": vlan,
       "vlanMibVersion": vlanMibVersion,
       "vlanMaxTableNumber": vlanMaxTableNumber,
       "vlanNameTable": vlanNameTable,
       "vlanNameEntry": vlanNameEntry,
       "vlanNameName": vlanNameName,
       "vlanNameTag": vlanNameTag,
       "vlanNameIfIndex": vlanNameIfIndex,
       "vlanPortModeTable": vlanPortModeTable,
       "vlanPortModeEntry": vlanPortModeEntry,
       "vlanPortModeState": vlanPortModeState,
       "vlanSendUnknownToAllPorts": vlanSendUnknownToAllPorts,
       "vlanDefaultSupported": vlanDefaultSupported,
       "vlanDot1vSupported": vlanDot1vSupported,
       "vlanDefaultEnabled": vlanDefaultEnabled,
       "vlanSpecialTagTable": vlanSpecialTagTable,
       "vlanSpecialTagEntry": vlanSpecialTagEntry,
       "vlanSpecialTagVID": vlanSpecialTagVID,
       "vlanSpecialTagStatus": vlanSpecialTagStatus,
       "vlanSpecialTagCurrentTable": vlanSpecialTagCurrentTable,
       "vlanSpecialTagCurrentEntry": vlanSpecialTagCurrentEntry,
       "vlanSpecialTagCurrentVID": vlanSpecialTagCurrentVID,
       "vlanSpecialTagCurrentReserved": vlanSpecialTagCurrentReserved,
       "vlanSpecialTagCurrentActive": vlanSpecialTagCurrentActive,
       "vlanPrivateEdgeSupported": vlanPrivateEdgeSupported,
       "vlanPrivateEdgeVersion": vlanPrivateEdgeVersion,
       "vlanPrivateEdgeTable": vlanPrivateEdgeTable,
       "vlanPrivateEdgeEntry": vlanPrivateEdgeEntry,
       "vlanPrivateEdgeUplink": vlanPrivateEdgeUplink,
       "vlanPrivateEdgeStatus": vlanPrivateEdgeStatus,
       "vlanDynamicVlanSupported": vlanDynamicVlanSupported,
       "vlanDynamicVlanTable": vlanDynamicVlanTable,
       "vlanDynamicVlanEntry": vlanDynamicVlanEntry,
       "vlanDynamicVlanMacAddress": vlanDynamicVlanMacAddress,
       "vlanDynamicVlanTag": vlanDynamicVlanTag,
       "vlanDynamicVlanStatus": vlanDynamicVlanStatus,
       "vlanPortModeExtTable": vlanPortModeExtTable,
       "vlanPortModeExtEntry": vlanPortModeExtEntry,
       "vlanPortModeExtState": vlanPortModeExtState,
       "vlanPortModeExtStatus": vlanPortModeExtStatus,
       "vlanPrivateSupported": vlanPrivateSupported,
       "vlanPrivateTableOld": vlanPrivateTableOld,
       "vlanPrivateEntryOld": vlanPrivateEntryOld,
       "vlanPrivateOldIsolatedVlanTag": vlanPrivateOldIsolatedVlanTag,
       "vlanPrivateOldStatus": vlanPrivateOldStatus,
       "vlanPrivateCommunityTable": vlanPrivateCommunityTable,
       "vlanPrivateCommunityEntry": vlanPrivateCommunityEntry,
       "vlanPrivateCommunityVlanTag": vlanPrivateCommunityVlanTag,
       "vlanPrivateCommunityStatus": vlanPrivateCommunityStatus,
       "vlanMulticastTvTable": vlanMulticastTvTable,
       "vlanMulticastTvEntry": vlanMulticastTvEntry,
       "vlanMulticastTvVID": vlanMulticastTvVID,
       "vlanMulticastTvStatus": vlanMulticastTvStatus,
       "vlanMacBaseVlanGroupTable": vlanMacBaseVlanGroupTable,
       "vlanMacBaseVlanGroupEntry": vlanMacBaseVlanGroupEntry,
       "vlanMacBaseVlanMacAddress": vlanMacBaseVlanMacAddress,
       "vlanMacBaseVlanMacMask": vlanMacBaseVlanMacMask,
       "vlanMacBaseVlanGroupId": vlanMacBaseVlanGroupId,
       "vlanMacBaseVlanGroupRowStatus": vlanMacBaseVlanGroupRowStatus,
       "vlanMacBaseVlanPortTable": vlanMacBaseVlanPortTable,
       "vlanMacBaseVlanPortEntry": vlanMacBaseVlanPortEntry,
       "vlanMacBaseVlanPortGroupId": vlanMacBaseVlanPortGroupId,
       "vlanMacBaseVlanPortGroupVid": vlanMacBaseVlanPortGroupVid,
       "vlanMacBaseVlanPortRowStatus": vlanMacBaseVlanPortRowStatus,
       "vlanPrivateEdgeGroupTable": vlanPrivateEdgeGroupTable,
       "vlanPrivateEdgeGroupEntry": vlanPrivateEdgeGroupEntry,
       "vlanPrivateEdgeGroupSource": vlanPrivateEdgeGroupSource,
       "vlanPrivateEdgeGroupUplink": vlanPrivateEdgeGroupUplink,
       "vlanPrivateEdgeGroupStatus": vlanPrivateEdgeGroupStatus,
       "vlanPrivateEdgeGroupIfIndexTable": vlanPrivateEdgeGroupIfIndexTable,
       "vlanPrivateEdgeGroupIfIndexEntry": vlanPrivateEdgeGroupIfIndexEntry,
       "vlanPrivateEdgeGroupIfIndexID": vlanPrivateEdgeGroupIfIndexID,
       "vlanPrivateEdgeGroupIfIndexDomainID": vlanPrivateEdgeGroupIfIndexDomainID,
       "vlanSubnetRangeTable": vlanSubnetRangeTable,
       "vlanSubnetRangeEntry": vlanSubnetRangeEntry,
       "vlanSubnetRangeAddr": vlanSubnetRangeAddr,
       "vlanSubnetRangeMask": vlanSubnetRangeMask,
       "vlanSubnetRangeGroupId": vlanSubnetRangeGroupId,
       "vlanSubnetRangeRowStatus": vlanSubnetRangeRowStatus,
       "vlanSubnetPortTable": vlanSubnetPortTable,
       "vlanSubnetPortEntry": vlanSubnetPortEntry,
       "vlanSubnetPortGroupId": vlanSubnetPortGroupId,
       "vlanSubnetPortGroupVid": vlanSubnetPortGroupVid,
       "vlanSubnetPortRowStatus": vlanSubnetPortRowStatus,
       "vlanTriplePlayTable": vlanTriplePlayTable,
       "vlanTriplePlayEntry": vlanTriplePlayEntry,
       "vlanTriplePlayInnerVID": vlanTriplePlayInnerVID,
       "vlanTriplePlayMulticastTvVID": vlanTriplePlayMulticastTvVID,
       "vlanTriplePlayRowStatus": vlanTriplePlayRowStatus,
       "vlanTriplePlayMulticastTvTable": vlanTriplePlayMulticastTvTable,
       "vlanTriplePlayMulticatTvEntry": vlanTriplePlayMulticatTvEntry,
       "vlanTriplePlayMulticastTvMulticastTvVID": vlanTriplePlayMulticastTvMulticastTvVID,
       "vlanTriplePlayMulticastTvMulticastTvPortList": vlanTriplePlayMulticastTvMulticastTvPortList,
       "vlanDefaultExtManagment": vlanDefaultExtManagment,
       "vlanVoice": vlanVoice,
       "vlanVoiceAgingTimeout": vlanVoiceAgingTimeout,
       "vlanVoiceTable": vlanVoiceTable,
       "vlanVoiceEntry": vlanVoiceEntry,
       "vlanVoicePriority": vlanVoicePriority,
       "vlanVoicePriorityRemark": vlanVoicePriorityRemark,
       "vlanVoiceRowStatus": vlanVoiceRowStatus,
       "vlanVoiceOUITable": vlanVoiceOUITable,
       "vlanVoiceOUIEntry": vlanVoiceOUIEntry,
       "vlanVoiceOUIPrefix": vlanVoiceOUIPrefix,
       "vlanVoiceOUIDescription": vlanVoiceOUIDescription,
       "vlanVoiceOUIEntryRowStatus": vlanVoiceOUIEntryRowStatus,
       "vlanVoicePortTable": vlanVoicePortTable,
       "vlanVoicePortEntry": vlanVoicePortEntry,
       "vlanVoicePortEnable": vlanVoicePortEnable,
       "vlanVoicePortVlanIndex": vlanVoicePortVlanIndex,
       "vlanVoicePortSecure": vlanVoicePortSecure,
       "vlanVoicePortCurrentMembership": vlanVoicePortCurrentMembership,
       "vlanVoicePortQosMode": vlanVoicePortQosMode,
       "vlanVoiceOUISetToDefault": vlanVoiceOUISetToDefault,
       "vlanDefault": vlanDefault,
       "vlanDefaultTaggedPorts": vlanDefaultTaggedPorts,
       "vlanDefaultEnabledPorts": vlanDefaultEnabledPorts,
       "vlanInetTriplePlayTable": vlanInetTriplePlayTable,
       "vlanInetTriplePlayEntry": vlanInetTriplePlayEntry,
       "vlanInetTriplePlayInetAddressType": vlanInetTriplePlayInetAddressType,
       "vlanInetTriplePlayInnerVID": vlanInetTriplePlayInnerVID,
       "vlanInetTriplePlayMulticastTvVID": vlanInetTriplePlayMulticastTvVID,
       "vlanInetTriplePlayRowStatus": vlanInetTriplePlayRowStatus,
       "vlanInetTriplePlayMulticastTvTable": vlanInetTriplePlayMulticastTvTable,
       "vlanInetTriplePlayMulticatTvEntry": vlanInetTriplePlayMulticatTvEntry,
       "vlanInetTriplePlayMulticastTvMulticastTvVID": vlanInetTriplePlayMulticastTvMulticastTvVID,
       "vlanInetTriplePlayMulticastTvMulticastTvPortList": vlanInetTriplePlayMulticastTvMulticastTvPortList,
       "vlanAsymmetricEnabled": vlanAsymmetricEnabled,
       "vlanPrivateTable": vlanPrivateTable,
       "vlanPrivateEntry": vlanPrivateEntry,
       "vlanPrivateVid": vlanPrivateVid,
       "vlanPrivateType": vlanPrivateType,
       "vlanPrivatePrimaryVid": vlanPrivatePrimaryVid,
       "vlanPrivateStatus": vlanPrivateStatus,
       "vlanPrivateMapTable": vlanPrivateMapTable,
       "vlanPrivateMapEntry": vlanPrivateMapEntry,
       "vlanPrivateMapPrimaryVid": vlanPrivateMapPrimaryVid,
       "vlanPrivateMapSecondaryVid": vlanPrivateMapSecondaryVid,
       "vlanPrivateMapPrimaryPorts": vlanPrivateMapPrimaryPorts,
       "vlanPrivateMapSecondaryPorts": vlanPrivateMapSecondaryPorts,
       "vlanPrivateMapPrimaryOperPorts": vlanPrivateMapPrimaryOperPorts,
       "vlanPrivateMapSecondaryOperPorts": vlanPrivateMapSecondaryOperPorts,
       "vlanPrivateMapStatus": vlanPrivateMapStatus,
       "vlanTrunkPortModeTable": vlanTrunkPortModeTable,
       "vlanTrunkPortModeEntry": vlanTrunkPortModeEntry,
       "vlanTrunkPortModeNativeVlanId": vlanTrunkPortModeNativeVlanId,
       "vlanTrunkModeList1to1024": vlanTrunkModeList1to1024,
       "vlanTrunkModeList1025to2048": vlanTrunkModeList1025to2048,
       "vlanTrunkModeList2049to3072": vlanTrunkModeList2049to3072,
       "vlanTrunkModeList3073to4094": vlanTrunkModeList3073to4094,
       "vlanAccessPortModeTable": vlanAccessPortModeTable,
       "vlanAccessPortModeEntry": vlanAccessPortModeEntry,
       "vlanAccessPortModeVlanId": vlanAccessPortModeVlanId,
       "vlanAccessPortModeMcstTvVlanId": vlanAccessPortModeMcstTvVlanId,
       "vlanCustomerPortModeTable": vlanCustomerPortModeTable,
       "vlanCustomerPortModeEntry": vlanCustomerPortModeEntry,
       "vlanCustomerPortModeVlanId": vlanCustomerPortModeVlanId,
       "vlanCustomerPortModeMtvList1to1024": vlanCustomerPortModeMtvList1to1024,
       "vlanCustomerPortModeMtvList1025to2048": vlanCustomerPortModeMtvList1025to2048,
       "vlanCustomerPortModeMtvList2049to3072": vlanCustomerPortModeMtvList2049to3072,
       "vlanCustomerPortModeMtvList3073to4094": vlanCustomerPortModeMtvList3073to4094,
       "vlanSwitchPortModeTable": vlanSwitchPortModeTable,
       "vlanSwitchPortModeEntry": vlanSwitchPortModeEntry,
       "vlanSwitchPortModeCategory": vlanSwitchPortModeCategory,
       "vlanPortModeContextTable": vlanPortModeContextTable,
       "vlanPortModeContextEntry": vlanPortModeContextEntry,
       "vlanPortModeContextValue": vlanPortModeContextValue,
       "vlanRsvlEnable": vlanRsvlEnable,
       "vlanRsvlMapTable": vlanRsvlMapTable,
       "vlanRsvlMapEntry": vlanRsvlMapEntry,
       "vlanRsvlMapPrimaryVid": vlanRsvlMapPrimaryVid,
       "vlanRsvlMapSecondaryVid": vlanRsvlMapSecondaryVid,
       "vlanRsvlMapStatus": vlanRsvlMapStatus,
       "rldot1qPortVlanStaticTable": rldot1qPortVlanStaticTable,
       "rldot1qPortVlanStaticEntry": rldot1qPortVlanStaticEntry,
       "rldot1qPortVlanStaticEgressList1to1024": rldot1qPortVlanStaticEgressList1to1024,
       "rldot1qPortVlanStaticEgressList1025to2048": rldot1qPortVlanStaticEgressList1025to2048,
       "rldot1qPortVlanStaticEgressList2049to3072": rldot1qPortVlanStaticEgressList2049to3072,
       "rldot1qPortVlanStaticEgressList3073to4094": rldot1qPortVlanStaticEgressList3073to4094,
       "rldot1qPortVlanStaticUntaggedEgressList1to1024": rldot1qPortVlanStaticUntaggedEgressList1to1024,
       "rldot1qPortVlanStaticUntaggedEgressList1025to2048": rldot1qPortVlanStaticUntaggedEgressList1025to2048,
       "rldot1qPortVlanStaticUntaggedEgressList2049to3072": rldot1qPortVlanStaticUntaggedEgressList2049to3072,
       "rldot1qPortVlanStaticUntaggedEgressList3073to4094": rldot1qPortVlanStaticUntaggedEgressList3073to4094,
       "rldot1qPortVlanStaticForbiddenList1to1024": rldot1qPortVlanStaticForbiddenList1to1024,
       "rldot1qPortVlanStaticForbiddenList1025to2048": rldot1qPortVlanStaticForbiddenList1025to2048,
       "rldot1qPortVlanStaticForbiddenList2049to3072": rldot1qPortVlanStaticForbiddenList2049to3072,
       "rldot1qPortVlanStaticForbiddenList3073to4094": rldot1qPortVlanStaticForbiddenList3073to4094,
       "rldot1qVlanStaticListTable": rldot1qVlanStaticListTable,
       "rldot1qVlanStaticListEntry": rldot1qVlanStaticListEntry,
       "rldot1qVlanStaticListIndex": rldot1qVlanStaticListIndex,
       "rldot1qVlanStaticList1to1024": rldot1qVlanStaticList1to1024,
       "rldot1qVlanStaticList1025to2048": rldot1qVlanStaticList1025to2048,
       "rldot1qVlanStaticList2049to3072": rldot1qVlanStaticList2049to3072,
       "rldot1qVlanStaticList3073to4094": rldot1qVlanStaticList3073to4094,
       "rldot1qVlanStaticNameTable": rldot1qVlanStaticNameTable,
       "rldot1qVlanStaticNameEntry": rldot1qVlanStaticNameEntry,
       "rldot1qVlanStaticName": rldot1qVlanStaticName,
       "rlPortVlanTriplePlayMulticastTvTable": rlPortVlanTriplePlayMulticastTvTable,
       "rlPortVlanTriplePlayMulticastTvEntry": rlPortVlanTriplePlayMulticastTvEntry,
       "rlPortVlanTriplePlayMulticastTvList1to1024": rlPortVlanTriplePlayMulticastTvList1to1024,
       "rlPortVlanTriplePlayMulticastTvList1025to2048": rlPortVlanTriplePlayMulticastTvList1025to2048,
       "rlPortVlanTriplePlayMulticastTvList2049to3072": rlPortVlanTriplePlayMulticastTvList2049to3072,
       "rlPortVlanTriplePlayMulticastTvList3073to4094": rlPortVlanTriplePlayMulticastTvList3073to4094,
       "rldot1qVlanMembershipTypeTable": rldot1qVlanMembershipTypeTable,
       "rldot1qVlanMembershipTypeEntry": rldot1qVlanMembershipTypeEntry,
       "rldot1qVlanMembershipTypeBitmap": rldot1qVlanMembershipTypeBitmap}
)
