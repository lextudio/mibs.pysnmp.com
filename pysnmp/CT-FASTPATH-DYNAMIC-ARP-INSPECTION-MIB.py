# SNMP MIB module (CT-FASTPATH-DYNAMIC-ARP-INSPECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-FASTPATH-DYNAMIC-ARP-INSPECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:13 2024
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

(ctDynamicArpInspectionExpMib,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctDynamicArpInspectionExpMib")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ctFastPathDynamicArpInspectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtAgentDaiConfigGroup_ObjectIdentity = ObjectIdentity
ctAgentDaiConfigGroup = _CtAgentDaiConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1)
)


class _CtAgentDaiSrcMacValidate_Type(TruthValue):
    """Custom type ctAgentDaiSrcMacValidate based on TruthValue"""


_CtAgentDaiSrcMacValidate_Object = MibScalar
ctAgentDaiSrcMacValidate = _CtAgentDaiSrcMacValidate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 1),
    _CtAgentDaiSrcMacValidate_Type()
)
ctAgentDaiSrcMacValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDaiSrcMacValidate.setStatus("current")


class _CtAgentDaiDstMacValidate_Type(TruthValue):
    """Custom type ctAgentDaiDstMacValidate based on TruthValue"""


_CtAgentDaiDstMacValidate_Object = MibScalar
ctAgentDaiDstMacValidate = _CtAgentDaiDstMacValidate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 2),
    _CtAgentDaiDstMacValidate_Type()
)
ctAgentDaiDstMacValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDaiDstMacValidate.setStatus("current")


class _CtAgentDaiIPValidate_Type(TruthValue):
    """Custom type ctAgentDaiIPValidate based on TruthValue"""


_CtAgentDaiIPValidate_Object = MibScalar
ctAgentDaiIPValidate = _CtAgentDaiIPValidate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 3),
    _CtAgentDaiIPValidate_Type()
)
ctAgentDaiIPValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDaiIPValidate.setStatus("current")
_CtAgentDaiVlanConfigTable_Object = MibTable
ctAgentDaiVlanConfigTable = _CtAgentDaiVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ctAgentDaiVlanConfigTable.setStatus("current")
_CtAgentDaiVlanConfigEntry_Object = MibTableRow
ctAgentDaiVlanConfigEntry = _CtAgentDaiVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 4, 1)
)
ctAgentDaiVlanConfigEntry.setIndexNames(
    (0, "CT-FASTPATH-DYNAMIC-ARP-INSPECTION-MIB", "ctAgentDaiVlanIndex"),
)
if mibBuilder.loadTexts:
    ctAgentDaiVlanConfigEntry.setStatus("current")
_CtAgentDaiVlanIndex_Type = VlanIndex
_CtAgentDaiVlanIndex_Object = MibTableColumn
ctAgentDaiVlanIndex = _CtAgentDaiVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 4, 1, 1),
    _CtAgentDaiVlanIndex_Type()
)
ctAgentDaiVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctAgentDaiVlanIndex.setStatus("current")


class _CtAgentDaiVlanDynArpInspEnable_Type(TruthValue):
    """Custom type ctAgentDaiVlanDynArpInspEnable based on TruthValue"""


_CtAgentDaiVlanDynArpInspEnable_Object = MibTableColumn
ctAgentDaiVlanDynArpInspEnable = _CtAgentDaiVlanDynArpInspEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 4, 1, 2),
    _CtAgentDaiVlanDynArpInspEnable_Type()
)
ctAgentDaiVlanDynArpInspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDaiVlanDynArpInspEnable.setStatus("current")


class _CtAgentDaiVlanLoggingEnable_Type(TruthValue):
    """Custom type ctAgentDaiVlanLoggingEnable based on TruthValue"""


_CtAgentDaiVlanLoggingEnable_Object = MibTableColumn
ctAgentDaiVlanLoggingEnable = _CtAgentDaiVlanLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 4, 1, 3),
    _CtAgentDaiVlanLoggingEnable_Type()
)
ctAgentDaiVlanLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDaiVlanLoggingEnable.setStatus("current")


class _CtAgentDaiVlanArpAclName_Type(DisplayString):
    """Custom type ctAgentDaiVlanArpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CtAgentDaiVlanArpAclName_Type.__name__ = "DisplayString"
_CtAgentDaiVlanArpAclName_Object = MibTableColumn
ctAgentDaiVlanArpAclName = _CtAgentDaiVlanArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 4, 1, 4),
    _CtAgentDaiVlanArpAclName_Type()
)
ctAgentDaiVlanArpAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDaiVlanArpAclName.setStatus("current")


class _CtAgentDaiVlanArpAclStaticFlag_Type(TruthValue):
    """Custom type ctAgentDaiVlanArpAclStaticFlag based on TruthValue"""


_CtAgentDaiVlanArpAclStaticFlag_Object = MibTableColumn
ctAgentDaiVlanArpAclStaticFlag = _CtAgentDaiVlanArpAclStaticFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 4, 1, 5),
    _CtAgentDaiVlanArpAclStaticFlag_Type()
)
ctAgentDaiVlanArpAclStaticFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDaiVlanArpAclStaticFlag.setStatus("current")


class _CtAagentDaiStatsReset_Type(Integer32):
    """Custom type ctAagentDaiStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_CtAagentDaiStatsReset_Type.__name__ = "Integer32"
_CtAagentDaiStatsReset_Object = MibScalar
ctAagentDaiStatsReset = _CtAagentDaiStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 5),
    _CtAagentDaiStatsReset_Type()
)
ctAagentDaiStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAagentDaiStatsReset.setStatus("current")
_CtAgentDaiVlanStatsTable_Object = MibTable
ctAgentDaiVlanStatsTable = _CtAgentDaiVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ctAgentDaiVlanStatsTable.setStatus("current")
_CtAgentDaiVlanStatsEntry_Object = MibTableRow
ctAgentDaiVlanStatsEntry = _CtAgentDaiVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1)
)
ctAgentDaiVlanStatsEntry.setIndexNames(
    (0, "CT-FASTPATH-DYNAMIC-ARP-INSPECTION-MIB", "ctAgentDaiVlanStatsIndex"),
)
if mibBuilder.loadTexts:
    ctAgentDaiVlanStatsEntry.setStatus("current")
_CtAgentDaiVlanStatsIndex_Type = VlanIndex
_CtAgentDaiVlanStatsIndex_Object = MibTableColumn
ctAgentDaiVlanStatsIndex = _CtAgentDaiVlanStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1, 1),
    _CtAgentDaiVlanStatsIndex_Type()
)
ctAgentDaiVlanStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctAgentDaiVlanStatsIndex.setStatus("current")
_CtAgentDaiVlanPktsForwarded_Type = Counter32
_CtAgentDaiVlanPktsForwarded_Object = MibTableColumn
ctAgentDaiVlanPktsForwarded = _CtAgentDaiVlanPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1, 2),
    _CtAgentDaiVlanPktsForwarded_Type()
)
ctAgentDaiVlanPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDaiVlanPktsForwarded.setStatus("current")
_CtAgentDaiVlanPktsDropped_Type = Counter32
_CtAgentDaiVlanPktsDropped_Object = MibTableColumn
ctAgentDaiVlanPktsDropped = _CtAgentDaiVlanPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1, 3),
    _CtAgentDaiVlanPktsDropped_Type()
)
ctAgentDaiVlanPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDaiVlanPktsDropped.setStatus("current")
_CtAgentDaiVlanDhcpDrops_Type = Counter32
_CtAgentDaiVlanDhcpDrops_Object = MibTableColumn
ctAgentDaiVlanDhcpDrops = _CtAgentDaiVlanDhcpDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1, 4),
    _CtAgentDaiVlanDhcpDrops_Type()
)
ctAgentDaiVlanDhcpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDaiVlanDhcpDrops.setStatus("current")
_CtAgentDaiVlanDhcpPermits_Type = Counter32
_CtAgentDaiVlanDhcpPermits_Object = MibTableColumn
ctAgentDaiVlanDhcpPermits = _CtAgentDaiVlanDhcpPermits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1, 5),
    _CtAgentDaiVlanDhcpPermits_Type()
)
ctAgentDaiVlanDhcpPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDaiVlanDhcpPermits.setStatus("current")
_CtAgentDaiVlanAclDrops_Type = Counter32
_CtAgentDaiVlanAclDrops_Object = MibTableColumn
ctAgentDaiVlanAclDrops = _CtAgentDaiVlanAclDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1, 6),
    _CtAgentDaiVlanAclDrops_Type()
)
ctAgentDaiVlanAclDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDaiVlanAclDrops.setStatus("current")
_CtAgentDaiVlanAclPermits_Type = Counter32
_CtAgentDaiVlanAclPermits_Object = MibTableColumn
ctAgentDaiVlanAclPermits = _CtAgentDaiVlanAclPermits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1, 7),
    _CtAgentDaiVlanAclPermits_Type()
)
ctAgentDaiVlanAclPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDaiVlanAclPermits.setStatus("current")
_CtAgentDaiVlanSrcMacFailures_Type = Counter32
_CtAgentDaiVlanSrcMacFailures_Object = MibTableColumn
ctAgentDaiVlanSrcMacFailures = _CtAgentDaiVlanSrcMacFailures_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1, 8),
    _CtAgentDaiVlanSrcMacFailures_Type()
)
ctAgentDaiVlanSrcMacFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDaiVlanSrcMacFailures.setStatus("current")
_CtAgentDaiVlanDstMacFailures_Type = Counter32
_CtAgentDaiVlanDstMacFailures_Object = MibTableColumn
ctAgentDaiVlanDstMacFailures = _CtAgentDaiVlanDstMacFailures_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1, 9),
    _CtAgentDaiVlanDstMacFailures_Type()
)
ctAgentDaiVlanDstMacFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDaiVlanDstMacFailures.setStatus("current")
_CtAgentDaiVlanIpValidFailures_Type = Counter32
_CtAgentDaiVlanIpValidFailures_Object = MibTableColumn
ctAgentDaiVlanIpValidFailures = _CtAgentDaiVlanIpValidFailures_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 6, 1, 10),
    _CtAgentDaiVlanIpValidFailures_Type()
)
ctAgentDaiVlanIpValidFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAgentDaiVlanIpValidFailures.setStatus("current")
_CtAgentDaiIfConfigTable_Object = MibTable
ctAgentDaiIfConfigTable = _CtAgentDaiIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ctAgentDaiIfConfigTable.setStatus("current")
_CtAgentDaiIfConfigEntry_Object = MibTableRow
ctAgentDaiIfConfigEntry = _CtAgentDaiIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 7, 1)
)
ctAgentDaiIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctAgentDaiIfConfigEntry.setStatus("current")


class _CtAgentDaiIfTrustEnable_Type(TruthValue):
    """Custom type ctAgentDaiIfTrustEnable based on TruthValue"""


_CtAgentDaiIfTrustEnable_Object = MibTableColumn
ctAgentDaiIfTrustEnable = _CtAgentDaiIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 7, 1, 1),
    _CtAgentDaiIfTrustEnable_Type()
)
ctAgentDaiIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDaiIfTrustEnable.setStatus("current")


class _CtAgentDaiIfRateLimit_Type(Unsigned32):
    """Custom type ctAgentDaiIfRateLimit based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CtAgentDaiIfRateLimit_Type.__name__ = "Unsigned32"
_CtAgentDaiIfRateLimit_Object = MibTableColumn
ctAgentDaiIfRateLimit = _CtAgentDaiIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 7, 1, 2),
    _CtAgentDaiIfRateLimit_Type()
)
ctAgentDaiIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDaiIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    ctAgentDaiIfRateLimit.setUnits("packets per second")


class _CtAgentDaiIfBurstInterval_Type(Unsigned32):
    """Custom type ctAgentDaiIfBurstInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CtAgentDaiIfBurstInterval_Type.__name__ = "Unsigned32"
_CtAgentDaiIfBurstInterval_Object = MibTableColumn
ctAgentDaiIfBurstInterval = _CtAgentDaiIfBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 36, 1, 1, 7, 1, 3),
    _CtAgentDaiIfBurstInterval_Type()
)
ctAgentDaiIfBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAgentDaiIfBurstInterval.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-FASTPATH-DYNAMIC-ARP-INSPECTION-MIB",
    **{"ctFastPathDynamicArpInspectionMIB": ctFastPathDynamicArpInspectionMIB,
       "ctAgentDaiConfigGroup": ctAgentDaiConfigGroup,
       "ctAgentDaiSrcMacValidate": ctAgentDaiSrcMacValidate,
       "ctAgentDaiDstMacValidate": ctAgentDaiDstMacValidate,
       "ctAgentDaiIPValidate": ctAgentDaiIPValidate,
       "ctAgentDaiVlanConfigTable": ctAgentDaiVlanConfigTable,
       "ctAgentDaiVlanConfigEntry": ctAgentDaiVlanConfigEntry,
       "ctAgentDaiVlanIndex": ctAgentDaiVlanIndex,
       "ctAgentDaiVlanDynArpInspEnable": ctAgentDaiVlanDynArpInspEnable,
       "ctAgentDaiVlanLoggingEnable": ctAgentDaiVlanLoggingEnable,
       "ctAgentDaiVlanArpAclName": ctAgentDaiVlanArpAclName,
       "ctAgentDaiVlanArpAclStaticFlag": ctAgentDaiVlanArpAclStaticFlag,
       "ctAagentDaiStatsReset": ctAagentDaiStatsReset,
       "ctAgentDaiVlanStatsTable": ctAgentDaiVlanStatsTable,
       "ctAgentDaiVlanStatsEntry": ctAgentDaiVlanStatsEntry,
       "ctAgentDaiVlanStatsIndex": ctAgentDaiVlanStatsIndex,
       "ctAgentDaiVlanPktsForwarded": ctAgentDaiVlanPktsForwarded,
       "ctAgentDaiVlanPktsDropped": ctAgentDaiVlanPktsDropped,
       "ctAgentDaiVlanDhcpDrops": ctAgentDaiVlanDhcpDrops,
       "ctAgentDaiVlanDhcpPermits": ctAgentDaiVlanDhcpPermits,
       "ctAgentDaiVlanAclDrops": ctAgentDaiVlanAclDrops,
       "ctAgentDaiVlanAclPermits": ctAgentDaiVlanAclPermits,
       "ctAgentDaiVlanSrcMacFailures": ctAgentDaiVlanSrcMacFailures,
       "ctAgentDaiVlanDstMacFailures": ctAgentDaiVlanDstMacFailures,
       "ctAgentDaiVlanIpValidFailures": ctAgentDaiVlanIpValidFailures,
       "ctAgentDaiIfConfigTable": ctAgentDaiIfConfigTable,
       "ctAgentDaiIfConfigEntry": ctAgentDaiIfConfigEntry,
       "ctAgentDaiIfTrustEnable": ctAgentDaiIfTrustEnable,
       "ctAgentDaiIfRateLimit": ctAgentDaiIfRateLimit,
       "ctAgentDaiIfBurstInterval": ctAgentDaiIfBurstInterval}
)
