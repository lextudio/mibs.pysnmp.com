# SNMP MIB module (H3C-STORAGE-SNAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-STORAGE-SNAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:27 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(H3cExtendSelectPolicy,
 H3cLvIDType,
 H3cRaidIDType,
 H3cStorageActionType,
 H3cStorageEnableState,
 H3cStorageOnlineState,
 h3cStorageRef) = mibBuilder.importSymbols(
    "H3C-STORAGE-REF-MIB",
    "H3cExtendSelectPolicy",
    "H3cLvIDType",
    "H3cRaidIDType",
    "H3cStorageActionType",
    "H3cStorageEnableState",
    "H3cStorageOnlineState",
    "h3cStorageRef")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cStorageSnap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSnapMibObjects_ObjectIdentity = ObjectIdentity
h3cSnapMibObjects = _H3cSnapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1)
)
_H3cGlobalSnapSettingsObject_ObjectIdentity = ObjectIdentity
h3cGlobalSnapSettingsObject = _H3cGlobalSnapSettingsObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 1)
)
_H3cAddtionalSpaceMaxSize_Type = Integer32
_H3cAddtionalSpaceMaxSize_Object = MibScalar
h3cAddtionalSpaceMaxSize = _H3cAddtionalSpaceMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 1, 1),
    _H3cAddtionalSpaceMaxSize_Type()
)
h3cAddtionalSpaceMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAddtionalSpaceMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cAddtionalSpaceMaxSize.setUnits("TB")
_H3cSnapConfigTable_Object = MibTable
h3cSnapConfigTable = _H3cSnapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    h3cSnapConfigTable.setStatus("current")
_H3cSnapConfigEntry_Object = MibTableRow
h3cSnapConfigEntry = _H3cSnapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1)
)
h3cSnapConfigEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSnapLvIndex"),
)
if mibBuilder.loadTexts:
    h3cSnapConfigEntry.setStatus("current")
_H3cSnapLvIndex_Type = H3cLvIDType
_H3cSnapLvIndex_Object = MibTableColumn
h3cSnapLvIndex = _H3cSnapLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 1),
    _H3cSnapLvIndex_Type()
)
h3cSnapLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSnapLvIndex.setStatus("current")
_H3cSnapAreaId_Type = H3cLvIDType
_H3cSnapAreaId_Object = MibTableColumn
h3cSnapAreaId = _H3cSnapAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 2),
    _H3cSnapAreaId_Type()
)
h3cSnapAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSnapAreaId.setStatus("current")


class _H3cSnapAreaAutoExpand_Type(H3cStorageEnableState):
    """Custom type h3cSnapAreaAutoExpand based on H3cStorageEnableState"""


_H3cSnapAreaAutoExpand_Object = MibTableColumn
h3cSnapAreaAutoExpand = _H3cSnapAreaAutoExpand_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 3),
    _H3cSnapAreaAutoExpand_Type()
)
h3cSnapAreaAutoExpand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSnapAreaAutoExpand.setStatus("current")


class _H3cSnapAreaThreshold_Type(Integer32):
    """Custom type h3cSnapAreaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cSnapAreaThreshold_Type.__name__ = "Integer32"
_H3cSnapAreaThreshold_Object = MibTableColumn
h3cSnapAreaThreshold = _H3cSnapAreaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 4),
    _H3cSnapAreaThreshold_Type()
)
h3cSnapAreaThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSnapAreaThreshold.setStatus("current")
_H3cSnapAreaIncSize_Type = Integer32
_H3cSnapAreaIncSize_Object = MibTableColumn
h3cSnapAreaIncSize = _H3cSnapAreaIncSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 5),
    _H3cSnapAreaIncSize_Type()
)
h3cSnapAreaIncSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSnapAreaIncSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cSnapAreaIncSize.setUnits("MB")
_H3cSnapAreaMaxSize_Type = Integer32
_H3cSnapAreaMaxSize_Object = MibTableColumn
h3cSnapAreaMaxSize = _H3cSnapAreaMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 6),
    _H3cSnapAreaMaxSize_Type()
)
h3cSnapAreaMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSnapAreaMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cSnapAreaMaxSize.setUnits("MB")


class _H3cSnapAreaFullDeleteTM_Type(Integer32):
    """Custom type h3cSnapAreaFullDeleteTM based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("rotative", 1))
    )


_H3cSnapAreaFullDeleteTM_Type.__name__ = "Integer32"
_H3cSnapAreaFullDeleteTM_Object = MibTableColumn
h3cSnapAreaFullDeleteTM = _H3cSnapAreaFullDeleteTM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 7),
    _H3cSnapAreaFullDeleteTM_Type()
)
h3cSnapAreaFullDeleteTM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSnapAreaFullDeleteTM.setStatus("current")
_H3cSnapAreaNotify_Type = H3cStorageEnableState
_H3cSnapAreaNotify_Object = MibTableColumn
h3cSnapAreaNotify = _H3cSnapAreaNotify_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 8),
    _H3cSnapAreaNotify_Type()
)
h3cSnapAreaNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSnapAreaNotify.setStatus("current")
_H3cSnapAreaStatus_Type = H3cStorageOnlineState
_H3cSnapAreaStatus_Object = MibTableColumn
h3cSnapAreaStatus = _H3cSnapAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 9),
    _H3cSnapAreaStatus_Type()
)
h3cSnapAreaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSnapAreaStatus.setStatus("current")
_H3cSnapRaidUuid_Type = H3cRaidIDType
_H3cSnapRaidUuid_Object = MibTableColumn
h3cSnapRaidUuid = _H3cSnapRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 10),
    _H3cSnapRaidUuid_Type()
)
h3cSnapRaidUuid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSnapRaidUuid.setStatus("current")
_H3cSnapRaidSize_Type = Integer32
_H3cSnapRaidSize_Object = MibTableColumn
h3cSnapRaidSize = _H3cSnapRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 11),
    _H3cSnapRaidSize_Type()
)
h3cSnapRaidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSnapRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cSnapRaidSize.setUnits("MB")


class _H3cSnapRaidSelectPolicy_Type(H3cExtendSelectPolicy):
    """Custom type h3cSnapRaidSelectPolicy based on H3cExtendSelectPolicy"""


_H3cSnapRaidSelectPolicy_Object = MibTableColumn
h3cSnapRaidSelectPolicy = _H3cSnapRaidSelectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 12),
    _H3cSnapRaidSelectPolicy_Type()
)
h3cSnapRaidSelectPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSnapRaidSelectPolicy.setStatus("current")
_H3cSnapAreaTotalSize_Type = Integer32
_H3cSnapAreaTotalSize_Object = MibTableColumn
h3cSnapAreaTotalSize = _H3cSnapAreaTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 13),
    _H3cSnapAreaTotalSize_Type()
)
h3cSnapAreaTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSnapAreaTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cSnapAreaTotalSize.setUnits("MB")
_H3cSnapAreaFreeSize_Type = Integer32
_H3cSnapAreaFreeSize_Object = MibTableColumn
h3cSnapAreaFreeSize = _H3cSnapAreaFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 14),
    _H3cSnapAreaFreeSize_Type()
)
h3cSnapAreaFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSnapAreaFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cSnapAreaFreeSize.setUnits("MB")
_H3cSnapExtendTimes_Type = Integer32
_H3cSnapExtendTimes_Object = MibTableColumn
h3cSnapExtendTimes = _H3cSnapExtendTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 15),
    _H3cSnapExtendTimes_Type()
)
h3cSnapExtendTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSnapExtendTimes.setStatus("current")
_H3cSnapRowStatus_Type = RowStatus
_H3cSnapRowStatus_Object = MibTableColumn
h3cSnapRowStatus = _H3cSnapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 2, 1, 16),
    _H3cSnapRowStatus_Type()
)
h3cSnapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSnapRowStatus.setStatus("current")
_H3cSnapExpandTable_Object = MibTable
h3cSnapExpandTable = _H3cSnapExpandTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 3)
)
if mibBuilder.loadTexts:
    h3cSnapExpandTable.setStatus("current")
_H3cSnapExpandEntry_Object = MibTableRow
h3cSnapExpandEntry = _H3cSnapExpandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 3, 1)
)
h3cSnapExpandEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSnapLvIndex"),
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSAExpRaidUuid"),
)
if mibBuilder.loadTexts:
    h3cSnapExpandEntry.setStatus("current")
_H3cSAExpRaidUuid_Type = H3cRaidIDType
_H3cSAExpRaidUuid_Object = MibTableColumn
h3cSAExpRaidUuid = _H3cSAExpRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 3, 1, 1),
    _H3cSAExpRaidUuid_Type()
)
h3cSAExpRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSAExpRaidUuid.setStatus("current")
_H3cSAExpSize_Type = Integer32
_H3cSAExpSize_Object = MibTableColumn
h3cSAExpSize = _H3cSAExpSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 3, 1, 2),
    _H3cSAExpSize_Type()
)
h3cSAExpSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSAExpSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cSAExpSize.setUnits("MB")
_H3cSAExpRaidSize_Type = Integer32
_H3cSAExpRaidSize_Object = MibTableColumn
h3cSAExpRaidSize = _H3cSAExpRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 3, 1, 3),
    _H3cSAExpRaidSize_Type()
)
h3cSAExpRaidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSAExpRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cSAExpRaidSize.setUnits("MB")
_H3cSnapAreaExpRowStatus_Type = RowStatus
_H3cSnapAreaExpRowStatus_Object = MibTableColumn
h3cSnapAreaExpRowStatus = _H3cSnapAreaExpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 3, 1, 4),
    _H3cSnapAreaExpRowStatus_Type()
)
h3cSnapAreaExpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSnapAreaExpRowStatus.setStatus("current")
_H3cSnapCopyTable_Object = MibTable
h3cSnapCopyTable = _H3cSnapCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 4)
)
if mibBuilder.loadTexts:
    h3cSnapCopyTable.setStatus("current")
_H3cSnapCopyEntry_Object = MibTableRow
h3cSnapCopyEntry = _H3cSnapCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 4, 1)
)
h3cSnapCopyEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSnapLvIndex"),
)
if mibBuilder.loadTexts:
    h3cSnapCopyEntry.setStatus("current")
_H3cSnapCopyLvIndex_Type = H3cLvIDType
_H3cSnapCopyLvIndex_Object = MibTableColumn
h3cSnapCopyLvIndex = _H3cSnapCopyLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 4, 1, 1),
    _H3cSnapCopyLvIndex_Type()
)
h3cSnapCopyLvIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSnapCopyLvIndex.setStatus("current")


class _H3cSnapCopyPercentage_Type(Integer32):
    """Custom type h3cSnapCopyPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cSnapCopyPercentage_Type.__name__ = "Integer32"
_H3cSnapCopyPercentage_Object = MibTableColumn
h3cSnapCopyPercentage = _H3cSnapCopyPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 4, 1, 2),
    _H3cSnapCopyPercentage_Type()
)
h3cSnapCopyPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSnapCopyPercentage.setStatus("current")
_H3cSnapCopyStartTime_Type = DateAndTime
_H3cSnapCopyStartTime_Object = MibTableColumn
h3cSnapCopyStartTime = _H3cSnapCopyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 4, 1, 3),
    _H3cSnapCopyStartTime_Type()
)
h3cSnapCopyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSnapCopyStartTime.setStatus("current")


class _H3cSnapCopySwitch_Type(Integer32):
    """Custom type h3cSnapCopySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("start", 1),
          ("stop", 2))
    )


_H3cSnapCopySwitch_Type.__name__ = "Integer32"
_H3cSnapCopySwitch_Object = MibTableColumn
h3cSnapCopySwitch = _H3cSnapCopySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 4, 1, 4),
    _H3cSnapCopySwitch_Type()
)
h3cSnapCopySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSnapCopySwitch.setStatus("current")
_H3cTimeMarkConfigTable_Object = MibTable
h3cTimeMarkConfigTable = _H3cTimeMarkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 5)
)
if mibBuilder.loadTexts:
    h3cTimeMarkConfigTable.setStatus("current")
_H3cTimeMarkConfigEntry_Object = MibTableRow
h3cTimeMarkConfigEntry = _H3cTimeMarkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 5, 1)
)
h3cTimeMarkConfigEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSnapLvIndex"),
)
if mibBuilder.loadTexts:
    h3cTimeMarkConfigEntry.setStatus("current")


class _H3cTimeMarkCounts_Type(Integer32):
    """Custom type h3cTimeMarkCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cTimeMarkCounts_Type.__name__ = "Integer32"
_H3cTimeMarkCounts_Object = MibTableColumn
h3cTimeMarkCounts = _H3cTimeMarkCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 5, 1, 1),
    _H3cTimeMarkCounts_Type()
)
h3cTimeMarkCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTimeMarkCounts.setStatus("current")
_H3cTimeMarkInitializeTime_Type = DateAndTime
_H3cTimeMarkInitializeTime_Object = MibTableColumn
h3cTimeMarkInitializeTime = _H3cTimeMarkInitializeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 5, 1, 2),
    _H3cTimeMarkInitializeTime_Type()
)
h3cTimeMarkInitializeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTimeMarkInitializeTime.setStatus("current")
_H3cTimeMarkInterval_Type = Integer32
_H3cTimeMarkInterval_Object = MibTableColumn
h3cTimeMarkInterval = _H3cTimeMarkInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 5, 1, 3),
    _H3cTimeMarkInterval_Type()
)
h3cTimeMarkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTimeMarkInterval.setStatus("current")
_H3cTimeMarkLastTime_Type = DateAndTime
_H3cTimeMarkLastTime_Object = MibTableColumn
h3cTimeMarkLastTime = _H3cTimeMarkLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 5, 1, 4),
    _H3cTimeMarkLastTime_Type()
)
h3cTimeMarkLastTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTimeMarkLastTime.setStatus("current")
_H3cTimeMarkTotal_Type = Integer32
_H3cTimeMarkTotal_Object = MibTableColumn
h3cTimeMarkTotal = _H3cTimeMarkTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 5, 1, 5),
    _H3cTimeMarkTotal_Type()
)
h3cTimeMarkTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTimeMarkTotal.setStatus("current")
_H3cTimeMarkSwitch_Type = H3cStorageEnableState
_H3cTimeMarkSwitch_Object = MibTableColumn
h3cTimeMarkSwitch = _H3cTimeMarkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 5, 1, 6),
    _H3cTimeMarkSwitch_Type()
)
h3cTimeMarkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTimeMarkSwitch.setStatus("current")
_H3cTimeMarkCreateTable_Object = MibTable
h3cTimeMarkCreateTable = _H3cTimeMarkCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 6)
)
if mibBuilder.loadTexts:
    h3cTimeMarkCreateTable.setStatus("current")
_H3cTimeMarkCreateEntry_Object = MibTableRow
h3cTimeMarkCreateEntry = _H3cTimeMarkCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 6, 1)
)
h3cTimeMarkCreateEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSnapLvIndex"),
    (0, "H3C-STORAGE-SNAP-MIB", "h3cTimeMarkStamp"),
)
if mibBuilder.loadTexts:
    h3cTimeMarkCreateEntry.setStatus("current")
_H3cTimeMarkStamp_Type = DateAndTime
_H3cTimeMarkStamp_Object = MibTableColumn
h3cTimeMarkStamp = _H3cTimeMarkStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 6, 1, 1),
    _H3cTimeMarkStamp_Type()
)
h3cTimeMarkStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTimeMarkStamp.setStatus("current")
_H3cTimeMarkComment_Type = OctetString
_H3cTimeMarkComment_Object = MibTableColumn
h3cTimeMarkComment = _H3cTimeMarkComment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 6, 1, 2),
    _H3cTimeMarkComment_Type()
)
h3cTimeMarkComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTimeMarkComment.setStatus("current")
_H3cTimeMarkSize_Type = Integer32
_H3cTimeMarkSize_Object = MibTableColumn
h3cTimeMarkSize = _H3cTimeMarkSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 6, 1, 3),
    _H3cTimeMarkSize_Type()
)
h3cTimeMarkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTimeMarkSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cTimeMarkSize.setUnits("KB")
_H3cTimeMarkRowStatus_Type = RowStatus
_H3cTimeMarkRowStatus_Object = MibTableColumn
h3cTimeMarkRowStatus = _H3cTimeMarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 6, 1, 4),
    _H3cTimeMarkRowStatus_Type()
)
h3cTimeMarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTimeMarkRowStatus.setStatus("current")
_H3cTimeMarkCopyTable_Object = MibTable
h3cTimeMarkCopyTable = _H3cTimeMarkCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 7)
)
if mibBuilder.loadTexts:
    h3cTimeMarkCopyTable.setStatus("current")
_H3cTimeMarkCopyEntry_Object = MibTableRow
h3cTimeMarkCopyEntry = _H3cTimeMarkCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 7, 1)
)
h3cTimeMarkCopyEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSnapLvIndex"),
    (0, "H3C-STORAGE-SNAP-MIB", "h3cTimeMarkStamp"),
)
if mibBuilder.loadTexts:
    h3cTimeMarkCopyEntry.setStatus("current")
_H3cTMCopyDestLvId_Type = H3cLvIDType
_H3cTMCopyDestLvId_Object = MibTableColumn
h3cTMCopyDestLvId = _H3cTMCopyDestLvId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 7, 1, 1),
    _H3cTMCopyDestLvId_Type()
)
h3cTMCopyDestLvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTMCopyDestLvId.setStatus("current")


class _H3cTMCopyPercentage_Type(Integer32):
    """Custom type h3cTMCopyPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cTMCopyPercentage_Type.__name__ = "Integer32"
_H3cTMCopyPercentage_Object = MibTableColumn
h3cTMCopyPercentage = _H3cTMCopyPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 7, 1, 2),
    _H3cTMCopyPercentage_Type()
)
h3cTMCopyPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTMCopyPercentage.setStatus("current")
_H3cTMCopyStartTime_Type = DateAndTime
_H3cTMCopyStartTime_Object = MibTableColumn
h3cTMCopyStartTime = _H3cTMCopyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 7, 1, 3),
    _H3cTMCopyStartTime_Type()
)
h3cTMCopyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTMCopyStartTime.setStatus("current")


class _H3cTMCopySwitch_Type(Integer32):
    """Custom type h3cTMCopySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("start", 1),
          ("stop", 2))
    )


_H3cTMCopySwitch_Type.__name__ = "Integer32"
_H3cTMCopySwitch_Object = MibTableColumn
h3cTMCopySwitch = _H3cTMCopySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 7, 1, 4),
    _H3cTMCopySwitch_Type()
)
h3cTMCopySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTMCopySwitch.setStatus("current")
_H3cTimeMarkRollbackTable_Object = MibTable
h3cTimeMarkRollbackTable = _H3cTimeMarkRollbackTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 8)
)
if mibBuilder.loadTexts:
    h3cTimeMarkRollbackTable.setStatus("current")
_H3cTimeMarkRollbackEntry_Object = MibTableRow
h3cTimeMarkRollbackEntry = _H3cTimeMarkRollbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 8, 1)
)
h3cTimeMarkRollbackEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSnapLvIndex"),
    (0, "H3C-STORAGE-SNAP-MIB", "h3cTimeMarkStamp"),
)
if mibBuilder.loadTexts:
    h3cTimeMarkRollbackEntry.setStatus("current")


class _H3cTMRollbackPercentage_Type(Integer32):
    """Custom type h3cTMRollbackPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cTMRollbackPercentage_Type.__name__ = "Integer32"
_H3cTMRollbackPercentage_Object = MibTableColumn
h3cTMRollbackPercentage = _H3cTMRollbackPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 8, 1, 1),
    _H3cTMRollbackPercentage_Type()
)
h3cTMRollbackPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTMRollbackPercentage.setStatus("current")
_H3cTMRollbackStartTime_Type = DateAndTime
_H3cTMRollbackStartTime_Object = MibTableColumn
h3cTMRollbackStartTime = _H3cTMRollbackStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 8, 1, 2),
    _H3cTMRollbackStartTime_Type()
)
h3cTMRollbackStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTMRollbackStartTime.setStatus("current")
_H3cTMRollbackSwitch_Type = H3cStorageActionType
_H3cTMRollbackSwitch_Object = MibTableColumn
h3cTMRollbackSwitch = _H3cTMRollbackSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 8, 1, 3),
    _H3cTMRollbackSwitch_Type()
)
h3cTMRollbackSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTMRollbackSwitch.setStatus("current")
_H3cTimeViewTable_Object = MibTable
h3cTimeViewTable = _H3cTimeViewTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 9)
)
if mibBuilder.loadTexts:
    h3cTimeViewTable.setStatus("current")
_H3cTimeViewEntry_Object = MibTableRow
h3cTimeViewEntry = _H3cTimeViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 9, 1)
)
h3cTimeViewEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSnapLvIndex"),
    (0, "H3C-STORAGE-SNAP-MIB", "h3cTimeViewStamp"),
)
if mibBuilder.loadTexts:
    h3cTimeViewEntry.setStatus("current")
_H3cTimeViewStamp_Type = DateAndTime
_H3cTimeViewStamp_Object = MibTableColumn
h3cTimeViewStamp = _H3cTimeViewStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 9, 1, 1),
    _H3cTimeViewStamp_Type()
)
h3cTimeViewStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTimeViewStamp.setStatus("current")
_H3cTimeViewID_Type = H3cLvIDType
_H3cTimeViewID_Object = MibTableColumn
h3cTimeViewID = _H3cTimeViewID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 9, 1, 2),
    _H3cTimeViewID_Type()
)
h3cTimeViewID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTimeViewID.setStatus("current")
_H3cTimeViewName_Type = OctetString
_H3cTimeViewName_Object = MibTableColumn
h3cTimeViewName = _H3cTimeViewName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 9, 1, 3),
    _H3cTimeViewName_Type()
)
h3cTimeViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTimeViewName.setStatus("current")
_H3cTimeViewRowStatus_Type = RowStatus
_H3cTimeViewRowStatus_Object = MibTableColumn
h3cTimeViewRowStatus = _H3cTimeViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 9, 1, 4),
    _H3cTimeViewRowStatus_Type()
)
h3cTimeViewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTimeViewRowStatus.setStatus("current")
_H3cReplicaConfigTable_Object = MibTable
h3cReplicaConfigTable = _H3cReplicaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10)
)
if mibBuilder.loadTexts:
    h3cReplicaConfigTable.setStatus("current")
_H3cReplicaConfigEntry_Object = MibTableRow
h3cReplicaConfigEntry = _H3cReplicaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1)
)
h3cReplicaConfigEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cRepLocalLvIndex"),
)
if mibBuilder.loadTexts:
    h3cReplicaConfigEntry.setStatus("current")
_H3cRepLocalLvIndex_Type = H3cLvIDType
_H3cRepLocalLvIndex_Object = MibTableColumn
h3cRepLocalLvIndex = _H3cRepLocalLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 1),
    _H3cRepLocalLvIndex_Type()
)
h3cRepLocalLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRepLocalLvIndex.setStatus("current")


class _H3cLvRepLocalWay_Type(Integer32):
    """Custom type h3cLvRepLocalWay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 2),
          ("outgoing", 1))
    )


_H3cLvRepLocalWay_Type.__name__ = "Integer32"
_H3cLvRepLocalWay_Object = MibTableColumn
h3cLvRepLocalWay = _H3cLvRepLocalWay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 2),
    _H3cLvRepLocalWay_Type()
)
h3cLvRepLocalWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvRepLocalWay.setStatus("current")
_H3cRepLocalServerIP_Type = InetAddress
_H3cRepLocalServerIP_Object = MibTableColumn
h3cRepLocalServerIP = _H3cRepLocalServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 3),
    _H3cRepLocalServerIP_Type()
)
h3cRepLocalServerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRepLocalServerIP.setStatus("current")
_H3cRepLocalServerIPType_Type = InetAddressType
_H3cRepLocalServerIPType_Object = MibTableColumn
h3cRepLocalServerIPType = _H3cRepLocalServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 4),
    _H3cRepLocalServerIPType_Type()
)
h3cRepLocalServerIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRepLocalServerIPType.setStatus("current")
_H3cRepLocalServerName_Type = OctetString
_H3cRepLocalServerName_Object = MibTableColumn
h3cRepLocalServerName = _H3cRepLocalServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 5),
    _H3cRepLocalServerName_Type()
)
h3cRepLocalServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRepLocalServerName.setStatus("current")


class _H3cRepLocalServerUsername_Type(OctetString):
    """Custom type h3cRepLocalServerUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cRepLocalServerUsername_Type.__name__ = "OctetString"
_H3cRepLocalServerUsername_Object = MibTableColumn
h3cRepLocalServerUsername = _H3cRepLocalServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 6),
    _H3cRepLocalServerUsername_Type()
)
h3cRepLocalServerUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRepLocalServerUsername.setStatus("current")


class _H3cRepLocalServerPassword_Type(OctetString):
    """Custom type h3cRepLocalServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_H3cRepLocalServerPassword_Type.__name__ = "OctetString"
_H3cRepLocalServerPassword_Object = MibTableColumn
h3cRepLocalServerPassword = _H3cRepLocalServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 7),
    _H3cRepLocalServerPassword_Type()
)
h3cRepLocalServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRepLocalServerPassword.setStatus("current")
_H3cRepRemoteServerIP_Type = InetAddress
_H3cRepRemoteServerIP_Object = MibTableColumn
h3cRepRemoteServerIP = _H3cRepRemoteServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 8),
    _H3cRepRemoteServerIP_Type()
)
h3cRepRemoteServerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRepRemoteServerIP.setStatus("current")
_H3cRepRemoteServerIPType_Type = InetAddressType
_H3cRepRemoteServerIPType_Object = MibTableColumn
h3cRepRemoteServerIPType = _H3cRepRemoteServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 9),
    _H3cRepRemoteServerIPType_Type()
)
h3cRepRemoteServerIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRepRemoteServerIPType.setStatus("current")
_H3cRepRemoteServerName_Type = OctetString
_H3cRepRemoteServerName_Object = MibTableColumn
h3cRepRemoteServerName = _H3cRepRemoteServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 10),
    _H3cRepRemoteServerName_Type()
)
h3cRepRemoteServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRepRemoteServerName.setStatus("current")


class _H3cRepRemoteServerUsername_Type(OctetString):
    """Custom type h3cRepRemoteServerUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cRepRemoteServerUsername_Type.__name__ = "OctetString"
_H3cRepRemoteServerUsername_Object = MibTableColumn
h3cRepRemoteServerUsername = _H3cRepRemoteServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 11),
    _H3cRepRemoteServerUsername_Type()
)
h3cRepRemoteServerUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRepRemoteServerUsername.setStatus("current")


class _H3cRepRemoteServerPassword_Type(OctetString):
    """Custom type h3cRepRemoteServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_H3cRepRemoteServerPassword_Type.__name__ = "OctetString"
_H3cRepRemoteServerPassword_Object = MibTableColumn
h3cRepRemoteServerPassword = _H3cRepRemoteServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 12),
    _H3cRepRemoteServerPassword_Type()
)
h3cRepRemoteServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRepRemoteServerPassword.setStatus("current")
_H3cRepRemoteLvIndex_Type = H3cLvIDType
_H3cRepRemoteLvIndex_Object = MibTableColumn
h3cRepRemoteLvIndex = _H3cRepRemoteLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 13),
    _H3cRepRemoteLvIndex_Type()
)
h3cRepRemoteLvIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRepRemoteLvIndex.setStatus("current")


class _H3cReplicaMode_Type(Integer32):
    """Custom type h3cReplicaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("none", 3),
          ("remote", 2))
    )


_H3cReplicaMode_Type.__name__ = "Integer32"
_H3cReplicaMode_Object = MibTableColumn
h3cReplicaMode = _H3cReplicaMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 14),
    _H3cReplicaMode_Type()
)
h3cReplicaMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaMode.setStatus("current")
_H3cReplicaWatermark_Type = Integer32
_H3cReplicaWatermark_Object = MibTableColumn
h3cReplicaWatermark = _H3cReplicaWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 15),
    _H3cReplicaWatermark_Type()
)
h3cReplicaWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaWatermark.setStatus("current")
if mibBuilder.loadTexts:
    h3cReplicaWatermark.setUnits("MB")
_H3cReplicaWatermarkRetry_Type = Integer32
_H3cReplicaWatermarkRetry_Object = MibTableColumn
h3cReplicaWatermarkRetry = _H3cReplicaWatermarkRetry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 16),
    _H3cReplicaWatermarkRetry_Type()
)
h3cReplicaWatermarkRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaWatermarkRetry.setStatus("current")
_H3cReplicaInitializeTime_Type = DateAndTime
_H3cReplicaInitializeTime_Object = MibTableColumn
h3cReplicaInitializeTime = _H3cReplicaInitializeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 17),
    _H3cReplicaInitializeTime_Type()
)
h3cReplicaInitializeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaInitializeTime.setStatus("current")
_H3cReplicaInterval_Type = Integer32
_H3cReplicaInterval_Object = MibTableColumn
h3cReplicaInterval = _H3cReplicaInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 18),
    _H3cReplicaInterval_Type()
)
h3cReplicaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaInterval.setStatus("current")


class _H3cReplicaEncrypt_Type(H3cStorageEnableState):
    """Custom type h3cReplicaEncrypt based on H3cStorageEnableState"""


_H3cReplicaEncrypt_Object = MibTableColumn
h3cReplicaEncrypt = _H3cReplicaEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 19),
    _H3cReplicaEncrypt_Type()
)
h3cReplicaEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaEncrypt.setStatus("current")


class _H3cReplicaCompress_Type(H3cStorageEnableState):
    """Custom type h3cReplicaCompress based on H3cStorageEnableState"""


_H3cReplicaCompress_Object = MibTableColumn
h3cReplicaCompress = _H3cReplicaCompress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 20),
    _H3cReplicaCompress_Type()
)
h3cReplicaCompress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaCompress.setStatus("current")


class _H3cReplicaUseExistTM_Type(H3cStorageEnableState):
    """Custom type h3cReplicaUseExistTM based on H3cStorageEnableState"""


_H3cReplicaUseExistTM_Object = MibTableColumn
h3cReplicaUseExistTM = _H3cReplicaUseExistTM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 21),
    _H3cReplicaUseExistTM_Type()
)
h3cReplicaUseExistTM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaUseExistTM.setStatus("current")


class _H3cReplicaProtocol_Type(Integer32):
    """Custom type h3cReplicaProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rudp", 2),
          ("tcp", 1))
    )


_H3cReplicaProtocol_Type.__name__ = "Integer32"
_H3cReplicaProtocol_Object = MibTableColumn
h3cReplicaProtocol = _H3cReplicaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 22),
    _H3cReplicaProtocol_Type()
)
h3cReplicaProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaProtocol.setStatus("current")
_H3cReplicaScanDiff_Type = TruthValue
_H3cReplicaScanDiff_Object = MibTableColumn
h3cReplicaScanDiff = _H3cReplicaScanDiff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 23),
    _H3cReplicaScanDiff_Type()
)
h3cReplicaScanDiff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaScanDiff.setStatus("current")


class _H3cReplicaStatSwitch_Type(Integer32):
    """Custom type h3cReplicaStatSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 8),
          ("promte", 1),
          ("resume", 7),
          ("reversal", 4),
          ("scan", 3),
          ("stop", 5),
          ("suspend", 6),
          ("sync", 2))
    )


_H3cReplicaStatSwitch_Type.__name__ = "Integer32"
_H3cReplicaStatSwitch_Object = MibTableColumn
h3cReplicaStatSwitch = _H3cReplicaStatSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 24),
    _H3cReplicaStatSwitch_Type()
)
h3cReplicaStatSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaStatSwitch.setStatus("current")
_H3cReplicaRowStatus_Type = RowStatus
_H3cReplicaRowStatus_Object = MibTableColumn
h3cReplicaRowStatus = _H3cReplicaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 10, 1, 25),
    _H3cReplicaRowStatus_Type()
)
h3cReplicaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cReplicaRowStatus.setStatus("current")
_H3cReplicaStateTable_Object = MibTable
h3cReplicaStateTable = _H3cReplicaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 11)
)
if mibBuilder.loadTexts:
    h3cReplicaStateTable.setStatus("current")
_H3cReplicaStateEntry_Object = MibTableRow
h3cReplicaStateEntry = _H3cReplicaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 11, 1)
)
h3cReplicaStateEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cRepLocalLvIndex"),
)
if mibBuilder.loadTexts:
    h3cReplicaStateEntry.setStatus("current")
_H3cReplicaDelta_Type = Integer32
_H3cReplicaDelta_Object = MibTableColumn
h3cReplicaDelta = _H3cReplicaDelta_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 11, 1, 1),
    _H3cReplicaDelta_Type()
)
h3cReplicaDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cReplicaDelta.setStatus("current")
if mibBuilder.loadTexts:
    h3cReplicaDelta.setUnits("MB")
_H3cReplicaLastSyncTime_Type = DateAndTime
_H3cReplicaLastSyncTime_Object = MibTableColumn
h3cReplicaLastSyncTime = _H3cReplicaLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 11, 1, 2),
    _H3cReplicaLastSyncTime_Type()
)
h3cReplicaLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cReplicaLastSyncTime.setStatus("current")
_H3cReplicaNextSyncTime_Type = DateAndTime
_H3cReplicaNextSyncTime_Object = MibTableColumn
h3cReplicaNextSyncTime = _H3cReplicaNextSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 11, 1, 3),
    _H3cReplicaNextSyncTime_Type()
)
h3cReplicaNextSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cReplicaNextSyncTime.setStatus("current")
_H3cReplicaSyncTotalSize_Type = Integer32
_H3cReplicaSyncTotalSize_Object = MibTableColumn
h3cReplicaSyncTotalSize = _H3cReplicaSyncTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 11, 1, 4),
    _H3cReplicaSyncTotalSize_Type()
)
h3cReplicaSyncTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cReplicaSyncTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cReplicaSyncTotalSize.setUnits("MB")
_H3cReplicaSyncCurPercentage_Type = Integer32
_H3cReplicaSyncCurPercentage_Object = MibTableColumn
h3cReplicaSyncCurPercentage = _H3cReplicaSyncCurPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 11, 1, 5),
    _H3cReplicaSyncCurPercentage_Type()
)
h3cReplicaSyncCurPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cReplicaSyncCurPercentage.setStatus("current")
_H3cReplicaSyncPerformance_Type = Integer32
_H3cReplicaSyncPerformance_Object = MibTableColumn
h3cReplicaSyncPerformance = _H3cReplicaSyncPerformance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 11, 1, 6),
    _H3cReplicaSyncPerformance_Type()
)
h3cReplicaSyncPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cReplicaSyncPerformance.setStatus("current")


class _H3cReplicaRunStatus_Type(Integer32):
    """Custom type h3cReplicaRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("scan", 5),
          ("stop", 3),
          ("suspend", 1),
          ("sync", 4))
    )


_H3cReplicaRunStatus_Type.__name__ = "Integer32"
_H3cReplicaRunStatus_Object = MibTableColumn
h3cReplicaRunStatus = _H3cReplicaRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 11, 1, 7),
    _H3cReplicaRunStatus_Type()
)
h3cReplicaRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cReplicaRunStatus.setStatus("current")
_H3cCDRConfigTable_Object = MibTable
h3cCDRConfigTable = _H3cCDRConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 12)
)
if mibBuilder.loadTexts:
    h3cCDRConfigTable.setStatus("current")
_H3cCDRConfigEntry_Object = MibTableRow
h3cCDRConfigEntry = _H3cCDRConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 12, 1)
)
h3cCDRConfigEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cCDRLvIndex"),
)
if mibBuilder.loadTexts:
    h3cCDRConfigEntry.setStatus("current")
_H3cCDRLvIndex_Type = H3cLvIDType
_H3cCDRLvIndex_Object = MibTableColumn
h3cCDRLvIndex = _H3cCDRLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 12, 1, 1),
    _H3cCDRLvIndex_Type()
)
h3cCDRLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCDRLvIndex.setStatus("current")
_H3cCDRID_Type = Integer32
_H3cCDRID_Object = MibTableColumn
h3cCDRID = _H3cCDRID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 12, 1, 2),
    _H3cCDRID_Type()
)
h3cCDRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCDRID.setStatus("current")
_H3cCDRStatus_Type = H3cStorageOnlineState
_H3cCDRStatus_Object = MibTableColumn
h3cCDRStatus = _H3cCDRStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 12, 1, 3),
    _H3cCDRStatus_Type()
)
h3cCDRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCDRStatus.setStatus("current")
_H3cCDRTotalSize_Type = Integer32
_H3cCDRTotalSize_Object = MibTableColumn
h3cCDRTotalSize = _H3cCDRTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 12, 1, 4),
    _H3cCDRTotalSize_Type()
)
h3cCDRTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCDRTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cCDRTotalSize.setUnits("MB")
_H3cCDRFreeSize_Type = Integer32
_H3cCDRFreeSize_Object = MibTableColumn
h3cCDRFreeSize = _H3cCDRFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 12, 1, 5),
    _H3cCDRFreeSize_Type()
)
h3cCDRFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCDRFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cCDRFreeSize.setUnits("MB")


class _H3cCDRSelectPolicy_Type(H3cExtendSelectPolicy):
    """Custom type h3cCDRSelectPolicy based on H3cExtendSelectPolicy"""


_H3cCDRSelectPolicy_Object = MibTableColumn
h3cCDRSelectPolicy = _H3cCDRSelectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 12, 1, 6),
    _H3cCDRSelectPolicy_Type()
)
h3cCDRSelectPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCDRSelectPolicy.setStatus("current")
_H3cCDRRowStatus_Type = RowStatus
_H3cCDRRowStatus_Object = MibTableColumn
h3cCDRRowStatus = _H3cCDRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 12, 1, 7),
    _H3cCDRRowStatus_Type()
)
h3cCDRRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCDRRowStatus.setStatus("current")
_H3cCDRDistributeTable_Object = MibTable
h3cCDRDistributeTable = _H3cCDRDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 13)
)
if mibBuilder.loadTexts:
    h3cCDRDistributeTable.setStatus("current")
_H3cCDRDistributeEntry_Object = MibTableRow
h3cCDRDistributeEntry = _H3cCDRDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 13, 1)
)
h3cCDRDistributeEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cCDRDistLvIndex"),
    (0, "H3C-STORAGE-SNAP-MIB", "h3cCDRRaidUuid"),
)
if mibBuilder.loadTexts:
    h3cCDRDistributeEntry.setStatus("current")
_H3cCDRDistLvIndex_Type = H3cLvIDType
_H3cCDRDistLvIndex_Object = MibTableColumn
h3cCDRDistLvIndex = _H3cCDRDistLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 13, 1, 1),
    _H3cCDRDistLvIndex_Type()
)
h3cCDRDistLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCDRDistLvIndex.setStatus("current")
_H3cCDRRaidUuid_Type = H3cRaidIDType
_H3cCDRRaidUuid_Object = MibTableColumn
h3cCDRRaidUuid = _H3cCDRRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 13, 1, 2),
    _H3cCDRRaidUuid_Type()
)
h3cCDRRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCDRRaidUuid.setStatus("current")
_H3cCDRRaidSize_Type = Integer32
_H3cCDRRaidSize_Object = MibTableColumn
h3cCDRRaidSize = _H3cCDRRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 13, 1, 3),
    _H3cCDRRaidSize_Type()
)
h3cCDRRaidSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCDRRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cCDRRaidSize.setUnits("MB")
_H3cCDRExtRowStatus_Type = RowStatus
_H3cCDRExtRowStatus_Object = MibTableColumn
h3cCDRExtRowStatus = _H3cCDRExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 13, 1, 4),
    _H3cCDRExtRowStatus_Type()
)
h3cCDRExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCDRExtRowStatus.setStatus("current")
_H3cSafeCacheConfigTable_Object = MibTable
h3cSafeCacheConfigTable = _H3cSafeCacheConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14)
)
if mibBuilder.loadTexts:
    h3cSafeCacheConfigTable.setStatus("current")
_H3cSafeCacheConfigEntry_Object = MibTableRow
h3cSafeCacheConfigEntry = _H3cSafeCacheConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1)
)
h3cSafeCacheConfigEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSafeCacheLvIndex"),
)
if mibBuilder.loadTexts:
    h3cSafeCacheConfigEntry.setStatus("current")
_H3cSafeCacheLvIndex_Type = H3cLvIDType
_H3cSafeCacheLvIndex_Object = MibTableColumn
h3cSafeCacheLvIndex = _H3cSafeCacheLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 1),
    _H3cSafeCacheLvIndex_Type()
)
h3cSafeCacheLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSafeCacheLvIndex.setStatus("current")
_H3cSafeCacheID_Type = Integer32
_H3cSafeCacheID_Object = MibTableColumn
h3cSafeCacheID = _H3cSafeCacheID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 2),
    _H3cSafeCacheID_Type()
)
h3cSafeCacheID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSafeCacheID.setStatus("current")
_H3cSafeCacheStatus_Type = H3cStorageOnlineState
_H3cSafeCacheStatus_Object = MibTableColumn
h3cSafeCacheStatus = _H3cSafeCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 3),
    _H3cSafeCacheStatus_Type()
)
h3cSafeCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSafeCacheStatus.setStatus("current")
_H3cSafeCacheTotalSize_Type = Integer32
_H3cSafeCacheTotalSize_Object = MibTableColumn
h3cSafeCacheTotalSize = _H3cSafeCacheTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 4),
    _H3cSafeCacheTotalSize_Type()
)
h3cSafeCacheTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSafeCacheTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cSafeCacheTotalSize.setUnits("MB")
_H3cSafeCacheFreeSize_Type = Integer32
_H3cSafeCacheFreeSize_Object = MibTableColumn
h3cSafeCacheFreeSize = _H3cSafeCacheFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 5),
    _H3cSafeCacheFreeSize_Type()
)
h3cSafeCacheFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSafeCacheFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cSafeCacheFreeSize.setUnits("MB")


class _H3cSafeCacheSelectPolicy_Type(H3cExtendSelectPolicy):
    """Custom type h3cSafeCacheSelectPolicy based on H3cExtendSelectPolicy"""


_H3cSafeCacheSelectPolicy_Object = MibTableColumn
h3cSafeCacheSelectPolicy = _H3cSafeCacheSelectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 6),
    _H3cSafeCacheSelectPolicy_Type()
)
h3cSafeCacheSelectPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSafeCacheSelectPolicy.setStatus("current")


class _H3cSafeCacheThreshold_Type(Integer32):
    """Custom type h3cSafeCacheThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cSafeCacheThreshold_Type.__name__ = "Integer32"
_H3cSafeCacheThreshold_Object = MibTableColumn
h3cSafeCacheThreshold = _H3cSafeCacheThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 7),
    _H3cSafeCacheThreshold_Type()
)
h3cSafeCacheThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSafeCacheThreshold.setStatus("current")
_H3cSafeCacheFlushTime_Type = Integer32
_H3cSafeCacheFlushTime_Object = MibTableColumn
h3cSafeCacheFlushTime = _H3cSafeCacheFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 8),
    _H3cSafeCacheFlushTime_Type()
)
h3cSafeCacheFlushTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSafeCacheFlushTime.setStatus("current")


class _H3cSafeCacheFlushCommand_Type(Integer32):
    """Custom type h3cSafeCacheFlushCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cSafeCacheFlushCommand_Type.__name__ = "Integer32"
_H3cSafeCacheFlushCommand_Object = MibTableColumn
h3cSafeCacheFlushCommand = _H3cSafeCacheFlushCommand_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 9),
    _H3cSafeCacheFlushCommand_Type()
)
h3cSafeCacheFlushCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSafeCacheFlushCommand.setStatus("current")


class _H3cSafeCacheSkipDupWrite_Type(Integer32):
    """Custom type h3cSafeCacheSkipDupWrite based on Integer32"""
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


_H3cSafeCacheSkipDupWrite_Type.__name__ = "Integer32"
_H3cSafeCacheSkipDupWrite_Object = MibTableColumn
h3cSafeCacheSkipDupWrite = _H3cSafeCacheSkipDupWrite_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 10),
    _H3cSafeCacheSkipDupWrite_Type()
)
h3cSafeCacheSkipDupWrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSafeCacheSkipDupWrite.setStatus("current")


class _H3cSafeCacheRunStatus_Type(Integer32):
    """Custom type h3cSafeCacheRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("run", 1),
          ("suspend", 2))
    )


_H3cSafeCacheRunStatus_Type.__name__ = "Integer32"
_H3cSafeCacheRunStatus_Object = MibTableColumn
h3cSafeCacheRunStatus = _H3cSafeCacheRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 11),
    _H3cSafeCacheRunStatus_Type()
)
h3cSafeCacheRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSafeCacheRunStatus.setStatus("current")


class _H3cSafeCacheSwitch_Type(Integer32):
    """Custom type h3cSafeCacheSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("resume", 2),
          ("suspend", 1))
    )


_H3cSafeCacheSwitch_Type.__name__ = "Integer32"
_H3cSafeCacheSwitch_Object = MibTableColumn
h3cSafeCacheSwitch = _H3cSafeCacheSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 12),
    _H3cSafeCacheSwitch_Type()
)
h3cSafeCacheSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSafeCacheSwitch.setStatus("current")
_H3cSafeCacheRowStatus_Type = RowStatus
_H3cSafeCacheRowStatus_Object = MibTableColumn
h3cSafeCacheRowStatus = _H3cSafeCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 14, 1, 13),
    _H3cSafeCacheRowStatus_Type()
)
h3cSafeCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSafeCacheRowStatus.setStatus("current")
_H3cSafeCacheDistributeTable_Object = MibTable
h3cSafeCacheDistributeTable = _H3cSafeCacheDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 15)
)
if mibBuilder.loadTexts:
    h3cSafeCacheDistributeTable.setStatus("current")
_H3cSafeCacheDistributeEntry_Object = MibTableRow
h3cSafeCacheDistributeEntry = _H3cSafeCacheDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 15, 1)
)
h3cSafeCacheDistributeEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSafeCacheDistLvIndex"),
    (0, "H3C-STORAGE-SNAP-MIB", "h3cSafeCacheRaidUuid"),
)
if mibBuilder.loadTexts:
    h3cSafeCacheDistributeEntry.setStatus("current")
_H3cSafeCacheDistLvIndex_Type = H3cLvIDType
_H3cSafeCacheDistLvIndex_Object = MibTableColumn
h3cSafeCacheDistLvIndex = _H3cSafeCacheDistLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 15, 1, 1),
    _H3cSafeCacheDistLvIndex_Type()
)
h3cSafeCacheDistLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSafeCacheDistLvIndex.setStatus("current")
_H3cSafeCacheRaidUuid_Type = H3cRaidIDType
_H3cSafeCacheRaidUuid_Object = MibTableColumn
h3cSafeCacheRaidUuid = _H3cSafeCacheRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 15, 1, 2),
    _H3cSafeCacheRaidUuid_Type()
)
h3cSafeCacheRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSafeCacheRaidUuid.setStatus("current")
_H3cSafeCacheRaidSize_Type = Integer32
_H3cSafeCacheRaidSize_Object = MibTableColumn
h3cSafeCacheRaidSize = _H3cSafeCacheRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 15, 1, 3),
    _H3cSafeCacheRaidSize_Type()
)
h3cSafeCacheRaidSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSafeCacheRaidSize.setStatus("current")
_H3cSafeCacheExtRowStatus_Type = RowStatus
_H3cSafeCacheExtRowStatus_Object = MibTableColumn
h3cSafeCacheExtRowStatus = _H3cSafeCacheExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 15, 1, 4),
    _H3cSafeCacheExtRowStatus_Type()
)
h3cSafeCacheExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSafeCacheExtRowStatus.setStatus("current")
_H3cMirrorConfigTable_Object = MibTable
h3cMirrorConfigTable = _H3cMirrorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16)
)
if mibBuilder.loadTexts:
    h3cMirrorConfigTable.setStatus("current")
_H3cMirrorConfigEntry_Object = MibTableRow
h3cMirrorConfigEntry = _H3cMirrorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1)
)
h3cMirrorConfigEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cMirrorLvIndex"),
)
if mibBuilder.loadTexts:
    h3cMirrorConfigEntry.setStatus("current")
_H3cMirrorLvIndex_Type = H3cLvIDType
_H3cMirrorLvIndex_Object = MibTableColumn
h3cMirrorLvIndex = _H3cMirrorLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 1),
    _H3cMirrorLvIndex_Type()
)
h3cMirrorLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMirrorLvIndex.setStatus("current")


class _H3cMirrorType_Type(Integer32):
    """Custom type h3cMirrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("none", 3),
          ("sync", 1))
    )


_H3cMirrorType_Type.__name__ = "Integer32"
_H3cMirrorType_Object = MibTableColumn
h3cMirrorType = _H3cMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 2),
    _H3cMirrorType_Type()
)
h3cMirrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMirrorType.setStatus("current")
_H3cMirrorStatus_Type = H3cStorageOnlineState
_H3cMirrorStatus_Object = MibTableColumn
h3cMirrorStatus = _H3cMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 3),
    _H3cMirrorStatus_Type()
)
h3cMirrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMirrorStatus.setStatus("current")
_H3cMirrorName_Type = OctetString
_H3cMirrorName_Object = MibTableColumn
h3cMirrorName = _H3cMirrorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 4),
    _H3cMirrorName_Type()
)
h3cMirrorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMirrorName.setStatus("current")


class _H3cMirrorSyncPercentage_Type(Integer32):
    """Custom type h3cMirrorSyncPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cMirrorSyncPercentage_Type.__name__ = "Integer32"
_H3cMirrorSyncPercentage_Object = MibTableColumn
h3cMirrorSyncPercentage = _H3cMirrorSyncPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 5),
    _H3cMirrorSyncPercentage_Type()
)
h3cMirrorSyncPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMirrorSyncPercentage.setStatus("current")


class _H3cMirrorSyncPerformance_Type(Integer32):
    """Custom type h3cMirrorSyncPerformance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cMirrorSyncPerformance_Type.__name__ = "Integer32"
_H3cMirrorSyncPerformance_Object = MibTableColumn
h3cMirrorSyncPerformance = _H3cMirrorSyncPerformance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 6),
    _H3cMirrorSyncPerformance_Type()
)
h3cMirrorSyncPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMirrorSyncPerformance.setStatus("current")
_H3cMirrorDelta_Type = Integer32
_H3cMirrorDelta_Object = MibTableColumn
h3cMirrorDelta = _H3cMirrorDelta_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 7),
    _H3cMirrorDelta_Type()
)
h3cMirrorDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMirrorDelta.setStatus("current")
if mibBuilder.loadTexts:
    h3cMirrorDelta.setUnits("MB")


class _H3cMirrorRaidType_Type(Integer32):
    """Custom type h3cMirrorRaidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("serviceEnable", 2),
          ("virtual", 1))
    )


_H3cMirrorRaidType_Type.__name__ = "Integer32"
_H3cMirrorRaidType_Object = MibTableColumn
h3cMirrorRaidType = _H3cMirrorRaidType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 8),
    _H3cMirrorRaidType_Type()
)
h3cMirrorRaidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMirrorRaidType.setStatus("current")


class _H3cMirrorSelectPolicy_Type(H3cExtendSelectPolicy):
    """Custom type h3cMirrorSelectPolicy based on H3cExtendSelectPolicy"""


_H3cMirrorSelectPolicy_Object = MibTableColumn
h3cMirrorSelectPolicy = _H3cMirrorSelectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 9),
    _H3cMirrorSelectPolicy_Type()
)
h3cMirrorSelectPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMirrorSelectPolicy.setStatus("current")


class _H3cMirrorSwitch_Type(Integer32):
    """Custom type h3cMirrorSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 4),
          ("promote", 3),
          ("swap", 2),
          ("sync", 1))
    )


_H3cMirrorSwitch_Type.__name__ = "Integer32"
_H3cMirrorSwitch_Object = MibTableColumn
h3cMirrorSwitch = _H3cMirrorSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 10),
    _H3cMirrorSwitch_Type()
)
h3cMirrorSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMirrorSwitch.setStatus("current")
_H3cMirrorExtendRaidUuid_Type = H3cRaidIDType
_H3cMirrorExtendRaidUuid_Object = MibTableColumn
h3cMirrorExtendRaidUuid = _H3cMirrorExtendRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 11),
    _H3cMirrorExtendRaidUuid_Type()
)
h3cMirrorExtendRaidUuid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMirrorExtendRaidUuid.setStatus("current")
_H3cMirrorRowStatus_Type = RowStatus
_H3cMirrorRowStatus_Object = MibTableColumn
h3cMirrorRowStatus = _H3cMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 16, 1, 12),
    _H3cMirrorRowStatus_Type()
)
h3cMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMirrorRowStatus.setStatus("current")
_H3cMirrorDistributeTable_Object = MibTable
h3cMirrorDistributeTable = _H3cMirrorDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 17)
)
if mibBuilder.loadTexts:
    h3cMirrorDistributeTable.setStatus("current")
_H3cMirrorDistributeEntry_Object = MibTableRow
h3cMirrorDistributeEntry = _H3cMirrorDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 17, 1)
)
h3cMirrorDistributeEntry.setIndexNames(
    (0, "H3C-STORAGE-SNAP-MIB", "h3cMirrorDistLvIndex"),
    (0, "H3C-STORAGE-SNAP-MIB", "h3cMirrorRaidUuid"),
)
if mibBuilder.loadTexts:
    h3cMirrorDistributeEntry.setStatus("current")
_H3cMirrorDistLvIndex_Type = H3cLvIDType
_H3cMirrorDistLvIndex_Object = MibTableColumn
h3cMirrorDistLvIndex = _H3cMirrorDistLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 17, 1, 1),
    _H3cMirrorDistLvIndex_Type()
)
h3cMirrorDistLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMirrorDistLvIndex.setStatus("current")
_H3cMirrorRaidUuid_Type = H3cRaidIDType
_H3cMirrorRaidUuid_Object = MibTableColumn
h3cMirrorRaidUuid = _H3cMirrorRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 17, 1, 2),
    _H3cMirrorRaidUuid_Type()
)
h3cMirrorRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMirrorRaidUuid.setStatus("current")
_H3cMirrorRaidSize_Type = Integer32
_H3cMirrorRaidSize_Object = MibTableColumn
h3cMirrorRaidSize = _H3cMirrorRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 17, 1, 3),
    _H3cMirrorRaidSize_Type()
)
h3cMirrorRaidSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMirrorRaidSize.setStatus("current")
_H3cMirrorExtRowStatus_Type = RowStatus
_H3cMirrorExtRowStatus_Object = MibTableColumn
h3cMirrorExtRowStatus = _H3cMirrorExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 2, 1, 17, 1, 4),
    _H3cMirrorExtRowStatus_Type()
)
h3cMirrorExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMirrorExtRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-STORAGE-SNAP-MIB",
    **{"h3cStorageSnap": h3cStorageSnap,
       "h3cSnapMibObjects": h3cSnapMibObjects,
       "h3cGlobalSnapSettingsObject": h3cGlobalSnapSettingsObject,
       "h3cAddtionalSpaceMaxSize": h3cAddtionalSpaceMaxSize,
       "h3cSnapConfigTable": h3cSnapConfigTable,
       "h3cSnapConfigEntry": h3cSnapConfigEntry,
       "h3cSnapLvIndex": h3cSnapLvIndex,
       "h3cSnapAreaId": h3cSnapAreaId,
       "h3cSnapAreaAutoExpand": h3cSnapAreaAutoExpand,
       "h3cSnapAreaThreshold": h3cSnapAreaThreshold,
       "h3cSnapAreaIncSize": h3cSnapAreaIncSize,
       "h3cSnapAreaMaxSize": h3cSnapAreaMaxSize,
       "h3cSnapAreaFullDeleteTM": h3cSnapAreaFullDeleteTM,
       "h3cSnapAreaNotify": h3cSnapAreaNotify,
       "h3cSnapAreaStatus": h3cSnapAreaStatus,
       "h3cSnapRaidUuid": h3cSnapRaidUuid,
       "h3cSnapRaidSize": h3cSnapRaidSize,
       "h3cSnapRaidSelectPolicy": h3cSnapRaidSelectPolicy,
       "h3cSnapAreaTotalSize": h3cSnapAreaTotalSize,
       "h3cSnapAreaFreeSize": h3cSnapAreaFreeSize,
       "h3cSnapExtendTimes": h3cSnapExtendTimes,
       "h3cSnapRowStatus": h3cSnapRowStatus,
       "h3cSnapExpandTable": h3cSnapExpandTable,
       "h3cSnapExpandEntry": h3cSnapExpandEntry,
       "h3cSAExpRaidUuid": h3cSAExpRaidUuid,
       "h3cSAExpSize": h3cSAExpSize,
       "h3cSAExpRaidSize": h3cSAExpRaidSize,
       "h3cSnapAreaExpRowStatus": h3cSnapAreaExpRowStatus,
       "h3cSnapCopyTable": h3cSnapCopyTable,
       "h3cSnapCopyEntry": h3cSnapCopyEntry,
       "h3cSnapCopyLvIndex": h3cSnapCopyLvIndex,
       "h3cSnapCopyPercentage": h3cSnapCopyPercentage,
       "h3cSnapCopyStartTime": h3cSnapCopyStartTime,
       "h3cSnapCopySwitch": h3cSnapCopySwitch,
       "h3cTimeMarkConfigTable": h3cTimeMarkConfigTable,
       "h3cTimeMarkConfigEntry": h3cTimeMarkConfigEntry,
       "h3cTimeMarkCounts": h3cTimeMarkCounts,
       "h3cTimeMarkInitializeTime": h3cTimeMarkInitializeTime,
       "h3cTimeMarkInterval": h3cTimeMarkInterval,
       "h3cTimeMarkLastTime": h3cTimeMarkLastTime,
       "h3cTimeMarkTotal": h3cTimeMarkTotal,
       "h3cTimeMarkSwitch": h3cTimeMarkSwitch,
       "h3cTimeMarkCreateTable": h3cTimeMarkCreateTable,
       "h3cTimeMarkCreateEntry": h3cTimeMarkCreateEntry,
       "h3cTimeMarkStamp": h3cTimeMarkStamp,
       "h3cTimeMarkComment": h3cTimeMarkComment,
       "h3cTimeMarkSize": h3cTimeMarkSize,
       "h3cTimeMarkRowStatus": h3cTimeMarkRowStatus,
       "h3cTimeMarkCopyTable": h3cTimeMarkCopyTable,
       "h3cTimeMarkCopyEntry": h3cTimeMarkCopyEntry,
       "h3cTMCopyDestLvId": h3cTMCopyDestLvId,
       "h3cTMCopyPercentage": h3cTMCopyPercentage,
       "h3cTMCopyStartTime": h3cTMCopyStartTime,
       "h3cTMCopySwitch": h3cTMCopySwitch,
       "h3cTimeMarkRollbackTable": h3cTimeMarkRollbackTable,
       "h3cTimeMarkRollbackEntry": h3cTimeMarkRollbackEntry,
       "h3cTMRollbackPercentage": h3cTMRollbackPercentage,
       "h3cTMRollbackStartTime": h3cTMRollbackStartTime,
       "h3cTMRollbackSwitch": h3cTMRollbackSwitch,
       "h3cTimeViewTable": h3cTimeViewTable,
       "h3cTimeViewEntry": h3cTimeViewEntry,
       "h3cTimeViewStamp": h3cTimeViewStamp,
       "h3cTimeViewID": h3cTimeViewID,
       "h3cTimeViewName": h3cTimeViewName,
       "h3cTimeViewRowStatus": h3cTimeViewRowStatus,
       "h3cReplicaConfigTable": h3cReplicaConfigTable,
       "h3cReplicaConfigEntry": h3cReplicaConfigEntry,
       "h3cRepLocalLvIndex": h3cRepLocalLvIndex,
       "h3cLvRepLocalWay": h3cLvRepLocalWay,
       "h3cRepLocalServerIP": h3cRepLocalServerIP,
       "h3cRepLocalServerIPType": h3cRepLocalServerIPType,
       "h3cRepLocalServerName": h3cRepLocalServerName,
       "h3cRepLocalServerUsername": h3cRepLocalServerUsername,
       "h3cRepLocalServerPassword": h3cRepLocalServerPassword,
       "h3cRepRemoteServerIP": h3cRepRemoteServerIP,
       "h3cRepRemoteServerIPType": h3cRepRemoteServerIPType,
       "h3cRepRemoteServerName": h3cRepRemoteServerName,
       "h3cRepRemoteServerUsername": h3cRepRemoteServerUsername,
       "h3cRepRemoteServerPassword": h3cRepRemoteServerPassword,
       "h3cRepRemoteLvIndex": h3cRepRemoteLvIndex,
       "h3cReplicaMode": h3cReplicaMode,
       "h3cReplicaWatermark": h3cReplicaWatermark,
       "h3cReplicaWatermarkRetry": h3cReplicaWatermarkRetry,
       "h3cReplicaInitializeTime": h3cReplicaInitializeTime,
       "h3cReplicaInterval": h3cReplicaInterval,
       "h3cReplicaEncrypt": h3cReplicaEncrypt,
       "h3cReplicaCompress": h3cReplicaCompress,
       "h3cReplicaUseExistTM": h3cReplicaUseExistTM,
       "h3cReplicaProtocol": h3cReplicaProtocol,
       "h3cReplicaScanDiff": h3cReplicaScanDiff,
       "h3cReplicaStatSwitch": h3cReplicaStatSwitch,
       "h3cReplicaRowStatus": h3cReplicaRowStatus,
       "h3cReplicaStateTable": h3cReplicaStateTable,
       "h3cReplicaStateEntry": h3cReplicaStateEntry,
       "h3cReplicaDelta": h3cReplicaDelta,
       "h3cReplicaLastSyncTime": h3cReplicaLastSyncTime,
       "h3cReplicaNextSyncTime": h3cReplicaNextSyncTime,
       "h3cReplicaSyncTotalSize": h3cReplicaSyncTotalSize,
       "h3cReplicaSyncCurPercentage": h3cReplicaSyncCurPercentage,
       "h3cReplicaSyncPerformance": h3cReplicaSyncPerformance,
       "h3cReplicaRunStatus": h3cReplicaRunStatus,
       "h3cCDRConfigTable": h3cCDRConfigTable,
       "h3cCDRConfigEntry": h3cCDRConfigEntry,
       "h3cCDRLvIndex": h3cCDRLvIndex,
       "h3cCDRID": h3cCDRID,
       "h3cCDRStatus": h3cCDRStatus,
       "h3cCDRTotalSize": h3cCDRTotalSize,
       "h3cCDRFreeSize": h3cCDRFreeSize,
       "h3cCDRSelectPolicy": h3cCDRSelectPolicy,
       "h3cCDRRowStatus": h3cCDRRowStatus,
       "h3cCDRDistributeTable": h3cCDRDistributeTable,
       "h3cCDRDistributeEntry": h3cCDRDistributeEntry,
       "h3cCDRDistLvIndex": h3cCDRDistLvIndex,
       "h3cCDRRaidUuid": h3cCDRRaidUuid,
       "h3cCDRRaidSize": h3cCDRRaidSize,
       "h3cCDRExtRowStatus": h3cCDRExtRowStatus,
       "h3cSafeCacheConfigTable": h3cSafeCacheConfigTable,
       "h3cSafeCacheConfigEntry": h3cSafeCacheConfigEntry,
       "h3cSafeCacheLvIndex": h3cSafeCacheLvIndex,
       "h3cSafeCacheID": h3cSafeCacheID,
       "h3cSafeCacheStatus": h3cSafeCacheStatus,
       "h3cSafeCacheTotalSize": h3cSafeCacheTotalSize,
       "h3cSafeCacheFreeSize": h3cSafeCacheFreeSize,
       "h3cSafeCacheSelectPolicy": h3cSafeCacheSelectPolicy,
       "h3cSafeCacheThreshold": h3cSafeCacheThreshold,
       "h3cSafeCacheFlushTime": h3cSafeCacheFlushTime,
       "h3cSafeCacheFlushCommand": h3cSafeCacheFlushCommand,
       "h3cSafeCacheSkipDupWrite": h3cSafeCacheSkipDupWrite,
       "h3cSafeCacheRunStatus": h3cSafeCacheRunStatus,
       "h3cSafeCacheSwitch": h3cSafeCacheSwitch,
       "h3cSafeCacheRowStatus": h3cSafeCacheRowStatus,
       "h3cSafeCacheDistributeTable": h3cSafeCacheDistributeTable,
       "h3cSafeCacheDistributeEntry": h3cSafeCacheDistributeEntry,
       "h3cSafeCacheDistLvIndex": h3cSafeCacheDistLvIndex,
       "h3cSafeCacheRaidUuid": h3cSafeCacheRaidUuid,
       "h3cSafeCacheRaidSize": h3cSafeCacheRaidSize,
       "h3cSafeCacheExtRowStatus": h3cSafeCacheExtRowStatus,
       "h3cMirrorConfigTable": h3cMirrorConfigTable,
       "h3cMirrorConfigEntry": h3cMirrorConfigEntry,
       "h3cMirrorLvIndex": h3cMirrorLvIndex,
       "h3cMirrorType": h3cMirrorType,
       "h3cMirrorStatus": h3cMirrorStatus,
       "h3cMirrorName": h3cMirrorName,
       "h3cMirrorSyncPercentage": h3cMirrorSyncPercentage,
       "h3cMirrorSyncPerformance": h3cMirrorSyncPerformance,
       "h3cMirrorDelta": h3cMirrorDelta,
       "h3cMirrorRaidType": h3cMirrorRaidType,
       "h3cMirrorSelectPolicy": h3cMirrorSelectPolicy,
       "h3cMirrorSwitch": h3cMirrorSwitch,
       "h3cMirrorExtendRaidUuid": h3cMirrorExtendRaidUuid,
       "h3cMirrorRowStatus": h3cMirrorRowStatus,
       "h3cMirrorDistributeTable": h3cMirrorDistributeTable,
       "h3cMirrorDistributeEntry": h3cMirrorDistributeEntry,
       "h3cMirrorDistLvIndex": h3cMirrorDistLvIndex,
       "h3cMirrorRaidUuid": h3cMirrorRaidUuid,
       "h3cMirrorRaidSize": h3cMirrorRaidSize,
       "h3cMirrorExtRowStatus": h3cMirrorExtRowStatus}
)
