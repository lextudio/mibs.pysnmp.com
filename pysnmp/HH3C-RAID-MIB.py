# SNMP MIB module (HH3C-RAID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-RAID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:41 2024
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

(Hh3cRaidIDType,
 Hh3cStorageActionType,
 Hh3cStorageEnableState,
 Hh3cStorageOwnerType,
 hh3cStorageRef) = mibBuilder.importSymbols(
    "HH3C-STORAGE-REF-MIB",
    "Hh3cRaidIDType",
    "Hh3cStorageActionType",
    "Hh3cStorageEnableState",
    "Hh3cStorageOwnerType",
    "hh3cStorageRef")

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

hh3cRaid = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cRaidMibObjects_ObjectIdentity = ObjectIdentity
hh3cRaidMibObjects = _Hh3cRaidMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1)
)
_Hh3cRaidCapacityTable_ObjectIdentity = ObjectIdentity
hh3cRaidCapacityTable = _Hh3cRaidCapacityTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 1)
)
_Hh3cPrimaryRaidCount_Type = Integer32
_Hh3cPrimaryRaidCount_Object = MibScalar
hh3cPrimaryRaidCount = _Hh3cPrimaryRaidCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 1, 1),
    _Hh3cPrimaryRaidCount_Type()
)
hh3cPrimaryRaidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPrimaryRaidCount.setStatus("current")
_Hh3cRaidTable_Object = MibTable
hh3cRaidTable = _Hh3cRaidTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cRaidTable.setStatus("current")
_Hh3cRaidEntry_Object = MibTableRow
hh3cRaidEntry = _Hh3cRaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1)
)
hh3cRaidEntry.setIndexNames(
    (0, "HH3C-RAID-MIB", "hh3cRaidName"),
)
if mibBuilder.loadTexts:
    hh3cRaidEntry.setStatus("current")


class _Hh3cRaidName_Type(OctetString):
    """Custom type hh3cRaidName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cRaidName_Type.__name__ = "OctetString"
_Hh3cRaidName_Object = MibTableColumn
hh3cRaidName = _Hh3cRaidName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 1),
    _Hh3cRaidName_Type()
)
hh3cRaidName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRaidName.setStatus("current")
_Hh3cRaidId_Type = Integer32
_Hh3cRaidId_Object = MibTableColumn
hh3cRaidId = _Hh3cRaidId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 2),
    _Hh3cRaidId_Type()
)
hh3cRaidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidId.setStatus("current")
_Hh3cRaidUuid_Type = Hh3cRaidIDType
_Hh3cRaidUuid_Object = MibTableColumn
hh3cRaidUuid = _Hh3cRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 3),
    _Hh3cRaidUuid_Type()
)
hh3cRaidUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidUuid.setStatus("current")


class _Hh3cRaidLevel_Type(Integer32):
    """Custom type hh3cRaidLevel based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("jbod", 1),
          ("raid0", 2),
          ("raid1", 3),
          ("raid10", 9),
          ("raid2", 4),
          ("raid3", 5),
          ("raid4", 6),
          ("raid5", 7),
          ("raid50", 10),
          ("raid6", 8))
    )


_Hh3cRaidLevel_Type.__name__ = "Integer32"
_Hh3cRaidLevel_Object = MibTableColumn
hh3cRaidLevel = _Hh3cRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 4),
    _Hh3cRaidLevel_Type()
)
hh3cRaidLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRaidLevel.setStatus("current")
_Hh3cRaidTimestamp_Type = DateAndTime
_Hh3cRaidTimestamp_Object = MibTableColumn
hh3cRaidTimestamp = _Hh3cRaidTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 5),
    _Hh3cRaidTimestamp_Type()
)
hh3cRaidTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidTimestamp.setStatus("current")


class _Hh3cRaidDiskList_Type(OctetString):
    """Custom type hh3cRaidDiskList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_Hh3cRaidDiskList_Type.__name__ = "OctetString"
_Hh3cRaidDiskList_Object = MibTableColumn
hh3cRaidDiskList = _Hh3cRaidDiskList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 6),
    _Hh3cRaidDiskList_Type()
)
hh3cRaidDiskList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRaidDiskList.setStatus("current")
_Hh3cRaidOwner_Type = Hh3cStorageOwnerType
_Hh3cRaidOwner_Object = MibTableColumn
hh3cRaidOwner = _Hh3cRaidOwner_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 7),
    _Hh3cRaidOwner_Type()
)
hh3cRaidOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRaidOwner.setStatus("current")
_Hh3cRaidSize_Type = Integer32
_Hh3cRaidSize_Object = MibTableColumn
hh3cRaidSize = _Hh3cRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 8),
    _Hh3cRaidSize_Type()
)
hh3cRaidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidSize.setStatus("current")
_Hh3cRaidFreeSize_Type = Integer32
_Hh3cRaidFreeSize_Object = MibTableColumn
hh3cRaidFreeSize = _Hh3cRaidFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 9),
    _Hh3cRaidFreeSize_Type()
)
hh3cRaidFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRaidFreeSize.setUnits("MB")
_Hh3cRaidAutoSync_Type = TruthValue
_Hh3cRaidAutoSync_Object = MibTableColumn
hh3cRaidAutoSync = _Hh3cRaidAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 10),
    _Hh3cRaidAutoSync_Type()
)
hh3cRaidAutoSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRaidAutoSync.setStatus("current")
_Hh3cRaidRowStatus_Type = RowStatus
_Hh3cRaidRowStatus_Object = MibTableColumn
hh3cRaidRowStatus = _Hh3cRaidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 2, 1, 11),
    _Hh3cRaidRowStatus_Type()
)
hh3cRaidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRaidRowStatus.setStatus("current")
_Hh3cRaidManageTable_Object = MibTable
hh3cRaidManageTable = _Hh3cRaidManageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cRaidManageTable.setStatus("current")
_Hh3cRaidManageEntry_Object = MibTableRow
hh3cRaidManageEntry = _Hh3cRaidManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 3, 1)
)
hh3cRaidManageEntry.setIndexNames(
    (0, "HH3C-RAID-MIB", "hh3cRaidUuid"),
)
if mibBuilder.loadTexts:
    hh3cRaidManageEntry.setStatus("current")


class _Hh3cRaidLocationState_Type(Hh3cStorageEnableState):
    """Custom type hh3cRaidLocationState based on Hh3cStorageEnableState"""


_Hh3cRaidLocationState_Object = MibTableColumn
hh3cRaidLocationState = _Hh3cRaidLocationState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 3, 1, 1),
    _Hh3cRaidLocationState_Type()
)
hh3cRaidLocationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidLocationState.setStatus("current")


class _Hh3cRaidAction_Type(Integer32):
    """Custom type hh3cRaidAction based on Integer32"""
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
        *(("invalid", 4),
          ("pause", 2),
          ("rebuild", 3),
          ("run", 1))
    )


_Hh3cRaidAction_Type.__name__ = "Integer32"
_Hh3cRaidAction_Object = MibTableColumn
hh3cRaidAction = _Hh3cRaidAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 3, 1, 2),
    _Hh3cRaidAction_Type()
)
hh3cRaidAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidAction.setStatus("current")


class _Hh3cRaidRunState_Type(Integer32):
    """Custom type hh3cRaidRunState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 2),
          ("failed", 3),
          ("normal", 1))
    )


_Hh3cRaidRunState_Type.__name__ = "Integer32"
_Hh3cRaidRunState_Object = MibTableColumn
hh3cRaidRunState = _Hh3cRaidRunState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 3, 1, 3),
    _Hh3cRaidRunState_Type()
)
hh3cRaidRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidRunState.setStatus("current")


class _Hh3cRaidAutoRebuild_Type(Hh3cStorageEnableState):
    """Custom type hh3cRaidAutoRebuild based on Hh3cStorageEnableState"""


_Hh3cRaidAutoRebuild_Object = MibTableColumn
hh3cRaidAutoRebuild = _Hh3cRaidAutoRebuild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 3, 1, 4),
    _Hh3cRaidAutoRebuild_Type()
)
hh3cRaidAutoRebuild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidAutoRebuild.setStatus("current")


class _Hh3cRaidSyncPercentage_Type(Integer32):
    """Custom type hh3cRaidSyncPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cRaidSyncPercentage_Type.__name__ = "Integer32"
_Hh3cRaidSyncPercentage_Object = MibTableColumn
hh3cRaidSyncPercentage = _Hh3cRaidSyncPercentage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 3, 1, 5),
    _Hh3cRaidSyncPercentage_Type()
)
hh3cRaidSyncPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidSyncPercentage.setStatus("current")


class _Hh3cRaidHideState_Type(Hh3cStorageEnableState):
    """Custom type hh3cRaidHideState based on Hh3cStorageEnableState"""


_Hh3cRaidHideState_Object = MibTableColumn
hh3cRaidHideState = _Hh3cRaidHideState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 3, 1, 6),
    _Hh3cRaidHideState_Type()
)
hh3cRaidHideState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidHideState.setStatus("current")
_Hh3cRaidLvRestore_Type = Hh3cStorageActionType
_Hh3cRaidLvRestore_Object = MibTableColumn
hh3cRaidLvRestore = _Hh3cRaidLvRestore_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 3, 1, 7),
    _Hh3cRaidLvRestore_Type()
)
hh3cRaidLvRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidLvRestore.setStatus("current")


class _Hh3cRaidType_Type(Integer32):
    """Custom type hh3cRaidType based on Integer32"""
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
        *(("directDevice", 2),
          ("serviceEnabledDevice", 3),
          ("unassigned", 4),
          ("virtualDevice", 1))
    )


_Hh3cRaidType_Type.__name__ = "Integer32"
_Hh3cRaidType_Object = MibTableColumn
hh3cRaidType = _Hh3cRaidType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 3, 1, 8),
    _Hh3cRaidType_Type()
)
hh3cRaidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidType.setStatus("current")
_Hh3cRaidCacheTable_Object = MibTable
hh3cRaidCacheTable = _Hh3cRaidCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cRaidCacheTable.setStatus("current")
_Hh3cRaidCacheEntry_Object = MibTableRow
hh3cRaidCacheEntry = _Hh3cRaidCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4, 1)
)
hh3cRaidCacheEntry.setIndexNames(
    (0, "HH3C-RAID-MIB", "hh3cRaidUuid"),
)
if mibBuilder.loadTexts:
    hh3cRaidCacheEntry.setStatus("current")


class _Hh3cRaidReadCache_Type(Hh3cStorageEnableState):
    """Custom type hh3cRaidReadCache based on Hh3cStorageEnableState"""


_Hh3cRaidReadCache_Object = MibTableColumn
hh3cRaidReadCache = _Hh3cRaidReadCache_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4, 1, 1),
    _Hh3cRaidReadCache_Type()
)
hh3cRaidReadCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidReadCache.setStatus("current")


class _Hh3cRaidReadCacheHitPeriod_Type(Integer32):
    """Custom type hh3cRaidReadCacheHitPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Hh3cRaidReadCacheHitPeriod_Type.__name__ = "Integer32"
_Hh3cRaidReadCacheHitPeriod_Object = MibTableColumn
hh3cRaidReadCacheHitPeriod = _Hh3cRaidReadCacheHitPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4, 1, 2),
    _Hh3cRaidReadCacheHitPeriod_Type()
)
hh3cRaidReadCacheHitPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidReadCacheHitPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRaidReadCacheHitPeriod.setUnits("minute")


class _Hh3cRaidReadCacheAverageRate_Type(Integer32):
    """Custom type hh3cRaidReadCacheAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cRaidReadCacheAverageRate_Type.__name__ = "Integer32"
_Hh3cRaidReadCacheAverageRate_Object = MibTableColumn
hh3cRaidReadCacheAverageRate = _Hh3cRaidReadCacheAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4, 1, 3),
    _Hh3cRaidReadCacheAverageRate_Type()
)
hh3cRaidReadCacheAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidReadCacheAverageRate.setStatus("current")


class _Hh3cRaidReadCachePhaseRate_Type(Integer32):
    """Custom type hh3cRaidReadCachePhaseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cRaidReadCachePhaseRate_Type.__name__ = "Integer32"
_Hh3cRaidReadCachePhaseRate_Object = MibTableColumn
hh3cRaidReadCachePhaseRate = _Hh3cRaidReadCachePhaseRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4, 1, 4),
    _Hh3cRaidReadCachePhaseRate_Type()
)
hh3cRaidReadCachePhaseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidReadCachePhaseRate.setStatus("current")


class _Hh3cRaidWriteCache_Type(Hh3cStorageEnableState):
    """Custom type hh3cRaidWriteCache based on Hh3cStorageEnableState"""


_Hh3cRaidWriteCache_Object = MibTableColumn
hh3cRaidWriteCache = _Hh3cRaidWriteCache_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4, 1, 5),
    _Hh3cRaidWriteCache_Type()
)
hh3cRaidWriteCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidWriteCache.setStatus("current")


class _Hh3cRaidWriteCacheHitPeriod_Type(Integer32):
    """Custom type hh3cRaidWriteCacheHitPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Hh3cRaidWriteCacheHitPeriod_Type.__name__ = "Integer32"
_Hh3cRaidWriteCacheHitPeriod_Object = MibTableColumn
hh3cRaidWriteCacheHitPeriod = _Hh3cRaidWriteCacheHitPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4, 1, 6),
    _Hh3cRaidWriteCacheHitPeriod_Type()
)
hh3cRaidWriteCacheHitPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidWriteCacheHitPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRaidWriteCacheHitPeriod.setUnits("minute")


class _Hh3cRaidWriteCacheAverageRate_Type(Integer32):
    """Custom type hh3cRaidWriteCacheAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cRaidWriteCacheAverageRate_Type.__name__ = "Integer32"
_Hh3cRaidWriteCacheAverageRate_Object = MibTableColumn
hh3cRaidWriteCacheAverageRate = _Hh3cRaidWriteCacheAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4, 1, 7),
    _Hh3cRaidWriteCacheAverageRate_Type()
)
hh3cRaidWriteCacheAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidWriteCacheAverageRate.setStatus("current")


class _Hh3cRaidWriteCachePhaseRate_Type(Integer32):
    """Custom type hh3cRaidWriteCachePhaseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cRaidWriteCachePhaseRate_Type.__name__ = "Integer32"
_Hh3cRaidWriteCachePhaseRate_Object = MibTableColumn
hh3cRaidWriteCachePhaseRate = _Hh3cRaidWriteCachePhaseRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4, 1, 8),
    _Hh3cRaidWriteCachePhaseRate_Type()
)
hh3cRaidWriteCachePhaseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidWriteCachePhaseRate.setStatus("current")
_Hh3cRaidWriteCacheFlush_Type = Hh3cStorageActionType
_Hh3cRaidWriteCacheFlush_Object = MibTableColumn
hh3cRaidWriteCacheFlush = _Hh3cRaidWriteCacheFlush_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 4, 1, 9),
    _Hh3cRaidWriteCacheFlush_Type()
)
hh3cRaidWriteCacheFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRaidWriteCacheFlush.setStatus("current")
_Hh3cRaidSpareDiskTable_Object = MibTable
hh3cRaidSpareDiskTable = _Hh3cRaidSpareDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cRaidSpareDiskTable.setStatus("current")
_Hh3cRaidSpareDiskEntry_Object = MibTableRow
hh3cRaidSpareDiskEntry = _Hh3cRaidSpareDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 5, 1)
)
hh3cRaidSpareDiskEntry.setIndexNames(
    (0, "HH3C-RAID-MIB", "hh3cRaidUuid"),
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cRaidSpareDiskEntry.setStatus("current")
_Hh3cRaidSpareDiskRowStatus_Type = RowStatus
_Hh3cRaidSpareDiskRowStatus_Object = MibTableColumn
hh3cRaidSpareDiskRowStatus = _Hh3cRaidSpareDiskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 5, 1, 1),
    _Hh3cRaidSpareDiskRowStatus_Type()
)
hh3cRaidSpareDiskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRaidSpareDiskRowStatus.setStatus("current")
_Hh3cFreezeRaidTable_Object = MibTable
hh3cFreezeRaidTable = _Hh3cFreezeRaidTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cFreezeRaidTable.setStatus("current")
_Hh3cFreezeRaidEntry_Object = MibTableRow
hh3cFreezeRaidEntry = _Hh3cFreezeRaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 6, 1)
)
hh3cFreezeRaidEntry.setIndexNames(
    (0, "HH3C-RAID-MIB", "hh3cFreezeRaidUuid"),
)
if mibBuilder.loadTexts:
    hh3cFreezeRaidEntry.setStatus("current")
_Hh3cFreezeRaidUuid_Type = Hh3cRaidIDType
_Hh3cFreezeRaidUuid_Object = MibTableColumn
hh3cFreezeRaidUuid = _Hh3cFreezeRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 6, 1, 1),
    _Hh3cFreezeRaidUuid_Type()
)
hh3cFreezeRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFreezeRaidUuid.setStatus("current")


class _Hh3cFreezeRaidName_Type(OctetString):
    """Custom type hh3cFreezeRaidName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cFreezeRaidName_Type.__name__ = "OctetString"
_Hh3cFreezeRaidName_Object = MibTableColumn
hh3cFreezeRaidName = _Hh3cFreezeRaidName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 6, 1, 2),
    _Hh3cFreezeRaidName_Type()
)
hh3cFreezeRaidName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFreezeRaidName.setStatus("current")
_Hh3cFreezeRaidRowStatus_Type = RowStatus
_Hh3cFreezeRaidRowStatus_Object = MibTableColumn
hh3cFreezeRaidRowStatus = _Hh3cFreezeRaidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 6, 1, 3),
    _Hh3cFreezeRaidRowStatus_Type()
)
hh3cFreezeRaidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFreezeRaidRowStatus.setStatus("current")
_Hh3c3rdRaidTable_Object = MibTable
hh3c3rdRaidTable = _Hh3c3rdRaidTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 7)
)
if mibBuilder.loadTexts:
    hh3c3rdRaidTable.setStatus("current")
_Hh3c3rdRaidEntry_Object = MibTableRow
hh3c3rdRaidEntry = _Hh3c3rdRaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 7, 1)
)
hh3c3rdRaidEntry.setIndexNames(
    (0, "HH3C-RAID-MIB", "hh3c3rdRaidUuid"),
)
if mibBuilder.loadTexts:
    hh3c3rdRaidEntry.setStatus("current")
_Hh3c3rdRaidUuid_Type = Hh3cRaidIDType
_Hh3c3rdRaidUuid_Object = MibTableColumn
hh3c3rdRaidUuid = _Hh3c3rdRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 7, 1, 1),
    _Hh3c3rdRaidUuid_Type()
)
hh3c3rdRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3c3rdRaidUuid.setStatus("current")


class _Hh3c3rdRaidName_Type(OctetString):
    """Custom type hh3c3rdRaidName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3c3rdRaidName_Type.__name__ = "OctetString"
_Hh3c3rdRaidName_Object = MibTableColumn
hh3c3rdRaidName = _Hh3c3rdRaidName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 7, 1, 2),
    _Hh3c3rdRaidName_Type()
)
hh3c3rdRaidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3rdRaidName.setStatus("current")
_Hh3c3rdRaidOwner_Type = OctetString
_Hh3c3rdRaidOwner_Object = MibTableColumn
hh3c3rdRaidOwner = _Hh3c3rdRaidOwner_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 7, 1, 3),
    _Hh3c3rdRaidOwner_Type()
)
hh3c3rdRaidOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3rdRaidOwner.setStatus("current")
_Hh3c3rdRaidImport_Type = Hh3cStorageOwnerType
_Hh3c3rdRaidImport_Object = MibTableColumn
hh3c3rdRaidImport = _Hh3c3rdRaidImport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 7, 1, 4),
    _Hh3c3rdRaidImport_Type()
)
hh3c3rdRaidImport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3c3rdRaidImport.setStatus("current")
_Hh3c3rdRaidRowStatus_Type = RowStatus
_Hh3c3rdRaidRowStatus_Object = MibTableColumn
hh3c3rdRaidRowStatus = _Hh3c3rdRaidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4, 1, 7, 1, 5),
    _Hh3c3rdRaidRowStatus_Type()
)
hh3c3rdRaidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3c3rdRaidRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RAID-MIB",
    **{"hh3cRaid": hh3cRaid,
       "hh3cRaidMibObjects": hh3cRaidMibObjects,
       "hh3cRaidCapacityTable": hh3cRaidCapacityTable,
       "hh3cPrimaryRaidCount": hh3cPrimaryRaidCount,
       "hh3cRaidTable": hh3cRaidTable,
       "hh3cRaidEntry": hh3cRaidEntry,
       "hh3cRaidName": hh3cRaidName,
       "hh3cRaidId": hh3cRaidId,
       "hh3cRaidUuid": hh3cRaidUuid,
       "hh3cRaidLevel": hh3cRaidLevel,
       "hh3cRaidTimestamp": hh3cRaidTimestamp,
       "hh3cRaidDiskList": hh3cRaidDiskList,
       "hh3cRaidOwner": hh3cRaidOwner,
       "hh3cRaidSize": hh3cRaidSize,
       "hh3cRaidFreeSize": hh3cRaidFreeSize,
       "hh3cRaidAutoSync": hh3cRaidAutoSync,
       "hh3cRaidRowStatus": hh3cRaidRowStatus,
       "hh3cRaidManageTable": hh3cRaidManageTable,
       "hh3cRaidManageEntry": hh3cRaidManageEntry,
       "hh3cRaidLocationState": hh3cRaidLocationState,
       "hh3cRaidAction": hh3cRaidAction,
       "hh3cRaidRunState": hh3cRaidRunState,
       "hh3cRaidAutoRebuild": hh3cRaidAutoRebuild,
       "hh3cRaidSyncPercentage": hh3cRaidSyncPercentage,
       "hh3cRaidHideState": hh3cRaidHideState,
       "hh3cRaidLvRestore": hh3cRaidLvRestore,
       "hh3cRaidType": hh3cRaidType,
       "hh3cRaidCacheTable": hh3cRaidCacheTable,
       "hh3cRaidCacheEntry": hh3cRaidCacheEntry,
       "hh3cRaidReadCache": hh3cRaidReadCache,
       "hh3cRaidReadCacheHitPeriod": hh3cRaidReadCacheHitPeriod,
       "hh3cRaidReadCacheAverageRate": hh3cRaidReadCacheAverageRate,
       "hh3cRaidReadCachePhaseRate": hh3cRaidReadCachePhaseRate,
       "hh3cRaidWriteCache": hh3cRaidWriteCache,
       "hh3cRaidWriteCacheHitPeriod": hh3cRaidWriteCacheHitPeriod,
       "hh3cRaidWriteCacheAverageRate": hh3cRaidWriteCacheAverageRate,
       "hh3cRaidWriteCachePhaseRate": hh3cRaidWriteCachePhaseRate,
       "hh3cRaidWriteCacheFlush": hh3cRaidWriteCacheFlush,
       "hh3cRaidSpareDiskTable": hh3cRaidSpareDiskTable,
       "hh3cRaidSpareDiskEntry": hh3cRaidSpareDiskEntry,
       "hh3cRaidSpareDiskRowStatus": hh3cRaidSpareDiskRowStatus,
       "hh3cFreezeRaidTable": hh3cFreezeRaidTable,
       "hh3cFreezeRaidEntry": hh3cFreezeRaidEntry,
       "hh3cFreezeRaidUuid": hh3cFreezeRaidUuid,
       "hh3cFreezeRaidName": hh3cFreezeRaidName,
       "hh3cFreezeRaidRowStatus": hh3cFreezeRaidRowStatus,
       "hh3c3rdRaidTable": hh3c3rdRaidTable,
       "hh3c3rdRaidEntry": hh3c3rdRaidEntry,
       "hh3c3rdRaidUuid": hh3c3rdRaidUuid,
       "hh3c3rdRaidName": hh3c3rdRaidName,
       "hh3c3rdRaidOwner": hh3c3rdRaidOwner,
       "hh3c3rdRaidImport": hh3c3rdRaidImport,
       "hh3c3rdRaidRowStatus": hh3c3rdRaidRowStatus}
)
