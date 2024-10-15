# SNMP MIB module (HH3C-STORAGE-SNAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-STORAGE-SNAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:01 2024
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

(Hh3cExtendSelectPolicy,
 Hh3cLvIDType,
 Hh3cRaidIDType,
 Hh3cStorageActionType,
 Hh3cStorageEnableState,
 Hh3cStorageOnlineState,
 hh3cStorageRef) = mibBuilder.importSymbols(
    "HH3C-STORAGE-REF-MIB",
    "Hh3cExtendSelectPolicy",
    "Hh3cLvIDType",
    "Hh3cRaidIDType",
    "Hh3cStorageActionType",
    "Hh3cStorageEnableState",
    "Hh3cStorageOnlineState",
    "hh3cStorageRef")

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

hh3cStorageSnap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSnapMibObjects_ObjectIdentity = ObjectIdentity
hh3cSnapMibObjects = _Hh3cSnapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1)
)
_Hh3cGlobalSnapSettingsObject_ObjectIdentity = ObjectIdentity
hh3cGlobalSnapSettingsObject = _Hh3cGlobalSnapSettingsObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 1)
)
_Hh3cAddtionalSpaceMaxSize_Type = Integer32
_Hh3cAddtionalSpaceMaxSize_Object = MibScalar
hh3cAddtionalSpaceMaxSize = _Hh3cAddtionalSpaceMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 1, 1),
    _Hh3cAddtionalSpaceMaxSize_Type()
)
hh3cAddtionalSpaceMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAddtionalSpaceMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cAddtionalSpaceMaxSize.setUnits("TB")
_Hh3cSnapConfigTable_Object = MibTable
hh3cSnapConfigTable = _Hh3cSnapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cSnapConfigTable.setStatus("current")
_Hh3cSnapConfigEntry_Object = MibTableRow
hh3cSnapConfigEntry = _Hh3cSnapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1)
)
hh3cSnapConfigEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSnapLvIndex"),
)
if mibBuilder.loadTexts:
    hh3cSnapConfigEntry.setStatus("current")
_Hh3cSnapLvIndex_Type = Hh3cLvIDType
_Hh3cSnapLvIndex_Object = MibTableColumn
hh3cSnapLvIndex = _Hh3cSnapLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 1),
    _Hh3cSnapLvIndex_Type()
)
hh3cSnapLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSnapLvIndex.setStatus("current")
_Hh3cSnapAreaId_Type = Hh3cLvIDType
_Hh3cSnapAreaId_Object = MibTableColumn
hh3cSnapAreaId = _Hh3cSnapAreaId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 2),
    _Hh3cSnapAreaId_Type()
)
hh3cSnapAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnapAreaId.setStatus("current")


class _Hh3cSnapAreaAutoExpand_Type(Hh3cStorageEnableState):
    """Custom type hh3cSnapAreaAutoExpand based on Hh3cStorageEnableState"""


_Hh3cSnapAreaAutoExpand_Object = MibTableColumn
hh3cSnapAreaAutoExpand = _Hh3cSnapAreaAutoExpand_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 3),
    _Hh3cSnapAreaAutoExpand_Type()
)
hh3cSnapAreaAutoExpand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnapAreaAutoExpand.setStatus("current")


class _Hh3cSnapAreaThreshold_Type(Integer32):
    """Custom type hh3cSnapAreaThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cSnapAreaThreshold_Type.__name__ = "Integer32"
_Hh3cSnapAreaThreshold_Object = MibTableColumn
hh3cSnapAreaThreshold = _Hh3cSnapAreaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 4),
    _Hh3cSnapAreaThreshold_Type()
)
hh3cSnapAreaThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnapAreaThreshold.setStatus("current")
_Hh3cSnapAreaIncSize_Type = Integer32
_Hh3cSnapAreaIncSize_Object = MibTableColumn
hh3cSnapAreaIncSize = _Hh3cSnapAreaIncSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 5),
    _Hh3cSnapAreaIncSize_Type()
)
hh3cSnapAreaIncSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnapAreaIncSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSnapAreaIncSize.setUnits("MB")
_Hh3cSnapAreaMaxSize_Type = Integer32
_Hh3cSnapAreaMaxSize_Object = MibTableColumn
hh3cSnapAreaMaxSize = _Hh3cSnapAreaMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 6),
    _Hh3cSnapAreaMaxSize_Type()
)
hh3cSnapAreaMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnapAreaMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSnapAreaMaxSize.setUnits("MB")


class _Hh3cSnapAreaFullDeleteTM_Type(Integer32):
    """Custom type hh3cSnapAreaFullDeleteTM based on Integer32"""
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


_Hh3cSnapAreaFullDeleteTM_Type.__name__ = "Integer32"
_Hh3cSnapAreaFullDeleteTM_Object = MibTableColumn
hh3cSnapAreaFullDeleteTM = _Hh3cSnapAreaFullDeleteTM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 7),
    _Hh3cSnapAreaFullDeleteTM_Type()
)
hh3cSnapAreaFullDeleteTM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnapAreaFullDeleteTM.setStatus("current")
_Hh3cSnapAreaNotify_Type = Hh3cStorageEnableState
_Hh3cSnapAreaNotify_Object = MibTableColumn
hh3cSnapAreaNotify = _Hh3cSnapAreaNotify_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 8),
    _Hh3cSnapAreaNotify_Type()
)
hh3cSnapAreaNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnapAreaNotify.setStatus("current")
_Hh3cSnapAreaStatus_Type = Hh3cStorageOnlineState
_Hh3cSnapAreaStatus_Object = MibTableColumn
hh3cSnapAreaStatus = _Hh3cSnapAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 9),
    _Hh3cSnapAreaStatus_Type()
)
hh3cSnapAreaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnapAreaStatus.setStatus("current")
_Hh3cSnapRaidUuid_Type = Hh3cRaidIDType
_Hh3cSnapRaidUuid_Object = MibTableColumn
hh3cSnapRaidUuid = _Hh3cSnapRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 10),
    _Hh3cSnapRaidUuid_Type()
)
hh3cSnapRaidUuid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnapRaidUuid.setStatus("current")
_Hh3cSnapRaidSize_Type = Integer32
_Hh3cSnapRaidSize_Object = MibTableColumn
hh3cSnapRaidSize = _Hh3cSnapRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 11),
    _Hh3cSnapRaidSize_Type()
)
hh3cSnapRaidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnapRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSnapRaidSize.setUnits("MB")


class _Hh3cSnapRaidSelectPolicy_Type(Hh3cExtendSelectPolicy):
    """Custom type hh3cSnapRaidSelectPolicy based on Hh3cExtendSelectPolicy"""


_Hh3cSnapRaidSelectPolicy_Object = MibTableColumn
hh3cSnapRaidSelectPolicy = _Hh3cSnapRaidSelectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 12),
    _Hh3cSnapRaidSelectPolicy_Type()
)
hh3cSnapRaidSelectPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnapRaidSelectPolicy.setStatus("current")
_Hh3cSnapAreaTotalSize_Type = Integer32
_Hh3cSnapAreaTotalSize_Object = MibTableColumn
hh3cSnapAreaTotalSize = _Hh3cSnapAreaTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 13),
    _Hh3cSnapAreaTotalSize_Type()
)
hh3cSnapAreaTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnapAreaTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSnapAreaTotalSize.setUnits("MB")
_Hh3cSnapAreaFreeSize_Type = Integer32
_Hh3cSnapAreaFreeSize_Object = MibTableColumn
hh3cSnapAreaFreeSize = _Hh3cSnapAreaFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 14),
    _Hh3cSnapAreaFreeSize_Type()
)
hh3cSnapAreaFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnapAreaFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSnapAreaFreeSize.setUnits("MB")
_Hh3cSnapExtendTimes_Type = Integer32
_Hh3cSnapExtendTimes_Object = MibTableColumn
hh3cSnapExtendTimes = _Hh3cSnapExtendTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 15),
    _Hh3cSnapExtendTimes_Type()
)
hh3cSnapExtendTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnapExtendTimes.setStatus("current")
_Hh3cSnapRowStatus_Type = RowStatus
_Hh3cSnapRowStatus_Object = MibTableColumn
hh3cSnapRowStatus = _Hh3cSnapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 2, 1, 16),
    _Hh3cSnapRowStatus_Type()
)
hh3cSnapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnapRowStatus.setStatus("current")
_Hh3cSnapExpandTable_Object = MibTable
hh3cSnapExpandTable = _Hh3cSnapExpandTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cSnapExpandTable.setStatus("current")
_Hh3cSnapExpandEntry_Object = MibTableRow
hh3cSnapExpandEntry = _Hh3cSnapExpandEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 3, 1)
)
hh3cSnapExpandEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSnapLvIndex"),
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSAExpRaidUuid"),
)
if mibBuilder.loadTexts:
    hh3cSnapExpandEntry.setStatus("current")
_Hh3cSAExpRaidUuid_Type = Hh3cRaidIDType
_Hh3cSAExpRaidUuid_Object = MibTableColumn
hh3cSAExpRaidUuid = _Hh3cSAExpRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 3, 1, 1),
    _Hh3cSAExpRaidUuid_Type()
)
hh3cSAExpRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSAExpRaidUuid.setStatus("current")
_Hh3cSAExpSize_Type = Integer32
_Hh3cSAExpSize_Object = MibTableColumn
hh3cSAExpSize = _Hh3cSAExpSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 3, 1, 2),
    _Hh3cSAExpSize_Type()
)
hh3cSAExpSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSAExpSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSAExpSize.setUnits("MB")
_Hh3cSAExpRaidSize_Type = Integer32
_Hh3cSAExpRaidSize_Object = MibTableColumn
hh3cSAExpRaidSize = _Hh3cSAExpRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 3, 1, 3),
    _Hh3cSAExpRaidSize_Type()
)
hh3cSAExpRaidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSAExpRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSAExpRaidSize.setUnits("MB")
_Hh3cSnapAreaExpRowStatus_Type = RowStatus
_Hh3cSnapAreaExpRowStatus_Object = MibTableColumn
hh3cSnapAreaExpRowStatus = _Hh3cSnapAreaExpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 3, 1, 4),
    _Hh3cSnapAreaExpRowStatus_Type()
)
hh3cSnapAreaExpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnapAreaExpRowStatus.setStatus("current")
_Hh3cSnapCopyTable_Object = MibTable
hh3cSnapCopyTable = _Hh3cSnapCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cSnapCopyTable.setStatus("current")
_Hh3cSnapCopyEntry_Object = MibTableRow
hh3cSnapCopyEntry = _Hh3cSnapCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 4, 1)
)
hh3cSnapCopyEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSnapLvIndex"),
)
if mibBuilder.loadTexts:
    hh3cSnapCopyEntry.setStatus("current")
_Hh3cSnapCopyLvIndex_Type = Hh3cLvIDType
_Hh3cSnapCopyLvIndex_Object = MibTableColumn
hh3cSnapCopyLvIndex = _Hh3cSnapCopyLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 4, 1, 1),
    _Hh3cSnapCopyLvIndex_Type()
)
hh3cSnapCopyLvIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnapCopyLvIndex.setStatus("current")


class _Hh3cSnapCopyPercentage_Type(Integer32):
    """Custom type hh3cSnapCopyPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cSnapCopyPercentage_Type.__name__ = "Integer32"
_Hh3cSnapCopyPercentage_Object = MibTableColumn
hh3cSnapCopyPercentage = _Hh3cSnapCopyPercentage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 4, 1, 2),
    _Hh3cSnapCopyPercentage_Type()
)
hh3cSnapCopyPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnapCopyPercentage.setStatus("current")
_Hh3cSnapCopyStartTime_Type = DateAndTime
_Hh3cSnapCopyStartTime_Object = MibTableColumn
hh3cSnapCopyStartTime = _Hh3cSnapCopyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 4, 1, 3),
    _Hh3cSnapCopyStartTime_Type()
)
hh3cSnapCopyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnapCopyStartTime.setStatus("current")


class _Hh3cSnapCopySwitch_Type(Integer32):
    """Custom type hh3cSnapCopySwitch based on Integer32"""
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


_Hh3cSnapCopySwitch_Type.__name__ = "Integer32"
_Hh3cSnapCopySwitch_Object = MibTableColumn
hh3cSnapCopySwitch = _Hh3cSnapCopySwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 4, 1, 4),
    _Hh3cSnapCopySwitch_Type()
)
hh3cSnapCopySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnapCopySwitch.setStatus("current")
_Hh3cTimeMarkConfigTable_Object = MibTable
hh3cTimeMarkConfigTable = _Hh3cTimeMarkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cTimeMarkConfigTable.setStatus("current")
_Hh3cTimeMarkConfigEntry_Object = MibTableRow
hh3cTimeMarkConfigEntry = _Hh3cTimeMarkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 5, 1)
)
hh3cTimeMarkConfigEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSnapLvIndex"),
)
if mibBuilder.loadTexts:
    hh3cTimeMarkConfigEntry.setStatus("current")


class _Hh3cTimeMarkCounts_Type(Integer32):
    """Custom type hh3cTimeMarkCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cTimeMarkCounts_Type.__name__ = "Integer32"
_Hh3cTimeMarkCounts_Object = MibTableColumn
hh3cTimeMarkCounts = _Hh3cTimeMarkCounts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 5, 1, 1),
    _Hh3cTimeMarkCounts_Type()
)
hh3cTimeMarkCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTimeMarkCounts.setStatus("current")
_Hh3cTimeMarkInitializeTime_Type = DateAndTime
_Hh3cTimeMarkInitializeTime_Object = MibTableColumn
hh3cTimeMarkInitializeTime = _Hh3cTimeMarkInitializeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 5, 1, 2),
    _Hh3cTimeMarkInitializeTime_Type()
)
hh3cTimeMarkInitializeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTimeMarkInitializeTime.setStatus("current")
_Hh3cTimeMarkInterval_Type = Integer32
_Hh3cTimeMarkInterval_Object = MibTableColumn
hh3cTimeMarkInterval = _Hh3cTimeMarkInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 5, 1, 3),
    _Hh3cTimeMarkInterval_Type()
)
hh3cTimeMarkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTimeMarkInterval.setStatus("current")
_Hh3cTimeMarkLastTime_Type = DateAndTime
_Hh3cTimeMarkLastTime_Object = MibTableColumn
hh3cTimeMarkLastTime = _Hh3cTimeMarkLastTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 5, 1, 4),
    _Hh3cTimeMarkLastTime_Type()
)
hh3cTimeMarkLastTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTimeMarkLastTime.setStatus("current")
_Hh3cTimeMarkTotal_Type = Integer32
_Hh3cTimeMarkTotal_Object = MibTableColumn
hh3cTimeMarkTotal = _Hh3cTimeMarkTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 5, 1, 5),
    _Hh3cTimeMarkTotal_Type()
)
hh3cTimeMarkTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTimeMarkTotal.setStatus("current")
_Hh3cTimeMarkSwitch_Type = Hh3cStorageEnableState
_Hh3cTimeMarkSwitch_Object = MibTableColumn
hh3cTimeMarkSwitch = _Hh3cTimeMarkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 5, 1, 6),
    _Hh3cTimeMarkSwitch_Type()
)
hh3cTimeMarkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTimeMarkSwitch.setStatus("current")
_Hh3cTimeMarkCreateTable_Object = MibTable
hh3cTimeMarkCreateTable = _Hh3cTimeMarkCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cTimeMarkCreateTable.setStatus("current")
_Hh3cTimeMarkCreateEntry_Object = MibTableRow
hh3cTimeMarkCreateEntry = _Hh3cTimeMarkCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 6, 1)
)
hh3cTimeMarkCreateEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSnapLvIndex"),
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cTimeMarkStamp"),
)
if mibBuilder.loadTexts:
    hh3cTimeMarkCreateEntry.setStatus("current")
_Hh3cTimeMarkStamp_Type = DateAndTime
_Hh3cTimeMarkStamp_Object = MibTableColumn
hh3cTimeMarkStamp = _Hh3cTimeMarkStamp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 6, 1, 1),
    _Hh3cTimeMarkStamp_Type()
)
hh3cTimeMarkStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTimeMarkStamp.setStatus("current")
_Hh3cTimeMarkComment_Type = OctetString
_Hh3cTimeMarkComment_Object = MibTableColumn
hh3cTimeMarkComment = _Hh3cTimeMarkComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 6, 1, 2),
    _Hh3cTimeMarkComment_Type()
)
hh3cTimeMarkComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTimeMarkComment.setStatus("current")
_Hh3cTimeMarkSize_Type = Integer32
_Hh3cTimeMarkSize_Object = MibTableColumn
hh3cTimeMarkSize = _Hh3cTimeMarkSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 6, 1, 3),
    _Hh3cTimeMarkSize_Type()
)
hh3cTimeMarkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTimeMarkSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cTimeMarkSize.setUnits("KB")
_Hh3cTimeMarkRowStatus_Type = RowStatus
_Hh3cTimeMarkRowStatus_Object = MibTableColumn
hh3cTimeMarkRowStatus = _Hh3cTimeMarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 6, 1, 4),
    _Hh3cTimeMarkRowStatus_Type()
)
hh3cTimeMarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTimeMarkRowStatus.setStatus("current")
_Hh3cTimeMarkCopyTable_Object = MibTable
hh3cTimeMarkCopyTable = _Hh3cTimeMarkCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cTimeMarkCopyTable.setStatus("current")
_Hh3cTimeMarkCopyEntry_Object = MibTableRow
hh3cTimeMarkCopyEntry = _Hh3cTimeMarkCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 7, 1)
)
hh3cTimeMarkCopyEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSnapLvIndex"),
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cTimeMarkStamp"),
)
if mibBuilder.loadTexts:
    hh3cTimeMarkCopyEntry.setStatus("current")
_Hh3cTMCopyDestLvId_Type = Hh3cLvIDType
_Hh3cTMCopyDestLvId_Object = MibTableColumn
hh3cTMCopyDestLvId = _Hh3cTMCopyDestLvId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 7, 1, 1),
    _Hh3cTMCopyDestLvId_Type()
)
hh3cTMCopyDestLvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTMCopyDestLvId.setStatus("current")


class _Hh3cTMCopyPercentage_Type(Integer32):
    """Custom type hh3cTMCopyPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cTMCopyPercentage_Type.__name__ = "Integer32"
_Hh3cTMCopyPercentage_Object = MibTableColumn
hh3cTMCopyPercentage = _Hh3cTMCopyPercentage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 7, 1, 2),
    _Hh3cTMCopyPercentage_Type()
)
hh3cTMCopyPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTMCopyPercentage.setStatus("current")
_Hh3cTMCopyStartTime_Type = DateAndTime
_Hh3cTMCopyStartTime_Object = MibTableColumn
hh3cTMCopyStartTime = _Hh3cTMCopyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 7, 1, 3),
    _Hh3cTMCopyStartTime_Type()
)
hh3cTMCopyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTMCopyStartTime.setStatus("current")


class _Hh3cTMCopySwitch_Type(Integer32):
    """Custom type hh3cTMCopySwitch based on Integer32"""
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


_Hh3cTMCopySwitch_Type.__name__ = "Integer32"
_Hh3cTMCopySwitch_Object = MibTableColumn
hh3cTMCopySwitch = _Hh3cTMCopySwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 7, 1, 4),
    _Hh3cTMCopySwitch_Type()
)
hh3cTMCopySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTMCopySwitch.setStatus("current")
_Hh3cTimeMarkRollbackTable_Object = MibTable
hh3cTimeMarkRollbackTable = _Hh3cTimeMarkRollbackTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cTimeMarkRollbackTable.setStatus("current")
_Hh3cTimeMarkRollbackEntry_Object = MibTableRow
hh3cTimeMarkRollbackEntry = _Hh3cTimeMarkRollbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 8, 1)
)
hh3cTimeMarkRollbackEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSnapLvIndex"),
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cTimeMarkStamp"),
)
if mibBuilder.loadTexts:
    hh3cTimeMarkRollbackEntry.setStatus("current")


class _Hh3cTMRollbackPercentage_Type(Integer32):
    """Custom type hh3cTMRollbackPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cTMRollbackPercentage_Type.__name__ = "Integer32"
_Hh3cTMRollbackPercentage_Object = MibTableColumn
hh3cTMRollbackPercentage = _Hh3cTMRollbackPercentage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 8, 1, 1),
    _Hh3cTMRollbackPercentage_Type()
)
hh3cTMRollbackPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTMRollbackPercentage.setStatus("current")
_Hh3cTMRollbackStartTime_Type = DateAndTime
_Hh3cTMRollbackStartTime_Object = MibTableColumn
hh3cTMRollbackStartTime = _Hh3cTMRollbackStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 8, 1, 2),
    _Hh3cTMRollbackStartTime_Type()
)
hh3cTMRollbackStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTMRollbackStartTime.setStatus("current")
_Hh3cTMRollbackSwitch_Type = Hh3cStorageActionType
_Hh3cTMRollbackSwitch_Object = MibTableColumn
hh3cTMRollbackSwitch = _Hh3cTMRollbackSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 8, 1, 3),
    _Hh3cTMRollbackSwitch_Type()
)
hh3cTMRollbackSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTMRollbackSwitch.setStatus("current")
_Hh3cTimeViewTable_Object = MibTable
hh3cTimeViewTable = _Hh3cTimeViewTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cTimeViewTable.setStatus("current")
_Hh3cTimeViewEntry_Object = MibTableRow
hh3cTimeViewEntry = _Hh3cTimeViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 9, 1)
)
hh3cTimeViewEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSnapLvIndex"),
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cTimeViewStamp"),
)
if mibBuilder.loadTexts:
    hh3cTimeViewEntry.setStatus("current")
_Hh3cTimeViewStamp_Type = DateAndTime
_Hh3cTimeViewStamp_Object = MibTableColumn
hh3cTimeViewStamp = _Hh3cTimeViewStamp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 9, 1, 1),
    _Hh3cTimeViewStamp_Type()
)
hh3cTimeViewStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTimeViewStamp.setStatus("current")
_Hh3cTimeViewID_Type = Hh3cLvIDType
_Hh3cTimeViewID_Object = MibTableColumn
hh3cTimeViewID = _Hh3cTimeViewID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 9, 1, 2),
    _Hh3cTimeViewID_Type()
)
hh3cTimeViewID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTimeViewID.setStatus("current")
_Hh3cTimeViewName_Type = OctetString
_Hh3cTimeViewName_Object = MibTableColumn
hh3cTimeViewName = _Hh3cTimeViewName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 9, 1, 3),
    _Hh3cTimeViewName_Type()
)
hh3cTimeViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTimeViewName.setStatus("current")
_Hh3cTimeViewRowStatus_Type = RowStatus
_Hh3cTimeViewRowStatus_Object = MibTableColumn
hh3cTimeViewRowStatus = _Hh3cTimeViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 9, 1, 4),
    _Hh3cTimeViewRowStatus_Type()
)
hh3cTimeViewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTimeViewRowStatus.setStatus("current")
_Hh3cReplicaConfigTable_Object = MibTable
hh3cReplicaConfigTable = _Hh3cReplicaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cReplicaConfigTable.setStatus("current")
_Hh3cReplicaConfigEntry_Object = MibTableRow
hh3cReplicaConfigEntry = _Hh3cReplicaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1)
)
hh3cReplicaConfigEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cRepLocalLvIndex"),
)
if mibBuilder.loadTexts:
    hh3cReplicaConfigEntry.setStatus("current")
_Hh3cRepLocalLvIndex_Type = Hh3cLvIDType
_Hh3cRepLocalLvIndex_Object = MibTableColumn
hh3cRepLocalLvIndex = _Hh3cRepLocalLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 1),
    _Hh3cRepLocalLvIndex_Type()
)
hh3cRepLocalLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRepLocalLvIndex.setStatus("current")


class _Hh3cLvRepLocalWay_Type(Integer32):
    """Custom type hh3cLvRepLocalWay based on Integer32"""
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


_Hh3cLvRepLocalWay_Type.__name__ = "Integer32"
_Hh3cLvRepLocalWay_Object = MibTableColumn
hh3cLvRepLocalWay = _Hh3cLvRepLocalWay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 2),
    _Hh3cLvRepLocalWay_Type()
)
hh3cLvRepLocalWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLvRepLocalWay.setStatus("current")
_Hh3cRepLocalServerIP_Type = InetAddress
_Hh3cRepLocalServerIP_Object = MibTableColumn
hh3cRepLocalServerIP = _Hh3cRepLocalServerIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 3),
    _Hh3cRepLocalServerIP_Type()
)
hh3cRepLocalServerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRepLocalServerIP.setStatus("current")
_Hh3cRepLocalServerIPType_Type = InetAddressType
_Hh3cRepLocalServerIPType_Object = MibTableColumn
hh3cRepLocalServerIPType = _Hh3cRepLocalServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 4),
    _Hh3cRepLocalServerIPType_Type()
)
hh3cRepLocalServerIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRepLocalServerIPType.setStatus("current")
_Hh3cRepLocalServerName_Type = OctetString
_Hh3cRepLocalServerName_Object = MibTableColumn
hh3cRepLocalServerName = _Hh3cRepLocalServerName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 5),
    _Hh3cRepLocalServerName_Type()
)
hh3cRepLocalServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRepLocalServerName.setStatus("current")


class _Hh3cRepLocalServerUsername_Type(OctetString):
    """Custom type hh3cRepLocalServerUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cRepLocalServerUsername_Type.__name__ = "OctetString"
_Hh3cRepLocalServerUsername_Object = MibTableColumn
hh3cRepLocalServerUsername = _Hh3cRepLocalServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 6),
    _Hh3cRepLocalServerUsername_Type()
)
hh3cRepLocalServerUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRepLocalServerUsername.setStatus("current")


class _Hh3cRepLocalServerPassword_Type(OctetString):
    """Custom type hh3cRepLocalServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Hh3cRepLocalServerPassword_Type.__name__ = "OctetString"
_Hh3cRepLocalServerPassword_Object = MibTableColumn
hh3cRepLocalServerPassword = _Hh3cRepLocalServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 7),
    _Hh3cRepLocalServerPassword_Type()
)
hh3cRepLocalServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRepLocalServerPassword.setStatus("current")
_Hh3cRepRemoteServerIP_Type = InetAddress
_Hh3cRepRemoteServerIP_Object = MibTableColumn
hh3cRepRemoteServerIP = _Hh3cRepRemoteServerIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 8),
    _Hh3cRepRemoteServerIP_Type()
)
hh3cRepRemoteServerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRepRemoteServerIP.setStatus("current")
_Hh3cRepRemoteServerIPType_Type = InetAddressType
_Hh3cRepRemoteServerIPType_Object = MibTableColumn
hh3cRepRemoteServerIPType = _Hh3cRepRemoteServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 9),
    _Hh3cRepRemoteServerIPType_Type()
)
hh3cRepRemoteServerIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRepRemoteServerIPType.setStatus("current")
_Hh3cRepRemoteServerName_Type = OctetString
_Hh3cRepRemoteServerName_Object = MibTableColumn
hh3cRepRemoteServerName = _Hh3cRepRemoteServerName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 10),
    _Hh3cRepRemoteServerName_Type()
)
hh3cRepRemoteServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRepRemoteServerName.setStatus("current")


class _Hh3cRepRemoteServerUsername_Type(OctetString):
    """Custom type hh3cRepRemoteServerUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cRepRemoteServerUsername_Type.__name__ = "OctetString"
_Hh3cRepRemoteServerUsername_Object = MibTableColumn
hh3cRepRemoteServerUsername = _Hh3cRepRemoteServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 11),
    _Hh3cRepRemoteServerUsername_Type()
)
hh3cRepRemoteServerUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRepRemoteServerUsername.setStatus("current")


class _Hh3cRepRemoteServerPassword_Type(OctetString):
    """Custom type hh3cRepRemoteServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Hh3cRepRemoteServerPassword_Type.__name__ = "OctetString"
_Hh3cRepRemoteServerPassword_Object = MibTableColumn
hh3cRepRemoteServerPassword = _Hh3cRepRemoteServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 12),
    _Hh3cRepRemoteServerPassword_Type()
)
hh3cRepRemoteServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRepRemoteServerPassword.setStatus("current")
_Hh3cRepRemoteLvIndex_Type = Hh3cLvIDType
_Hh3cRepRemoteLvIndex_Object = MibTableColumn
hh3cRepRemoteLvIndex = _Hh3cRepRemoteLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 13),
    _Hh3cRepRemoteLvIndex_Type()
)
hh3cRepRemoteLvIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRepRemoteLvIndex.setStatus("current")


class _Hh3cReplicaMode_Type(Integer32):
    """Custom type hh3cReplicaMode based on Integer32"""
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


_Hh3cReplicaMode_Type.__name__ = "Integer32"
_Hh3cReplicaMode_Object = MibTableColumn
hh3cReplicaMode = _Hh3cReplicaMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 14),
    _Hh3cReplicaMode_Type()
)
hh3cReplicaMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaMode.setStatus("current")
_Hh3cReplicaWatermark_Type = Integer32
_Hh3cReplicaWatermark_Object = MibTableColumn
hh3cReplicaWatermark = _Hh3cReplicaWatermark_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 15),
    _Hh3cReplicaWatermark_Type()
)
hh3cReplicaWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaWatermark.setStatus("current")
if mibBuilder.loadTexts:
    hh3cReplicaWatermark.setUnits("MB")
_Hh3cReplicaWatermarkRetry_Type = Integer32
_Hh3cReplicaWatermarkRetry_Object = MibTableColumn
hh3cReplicaWatermarkRetry = _Hh3cReplicaWatermarkRetry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 16),
    _Hh3cReplicaWatermarkRetry_Type()
)
hh3cReplicaWatermarkRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaWatermarkRetry.setStatus("current")
_Hh3cReplicaInitializeTime_Type = DateAndTime
_Hh3cReplicaInitializeTime_Object = MibTableColumn
hh3cReplicaInitializeTime = _Hh3cReplicaInitializeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 17),
    _Hh3cReplicaInitializeTime_Type()
)
hh3cReplicaInitializeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaInitializeTime.setStatus("current")
_Hh3cReplicaInterval_Type = Integer32
_Hh3cReplicaInterval_Object = MibTableColumn
hh3cReplicaInterval = _Hh3cReplicaInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 18),
    _Hh3cReplicaInterval_Type()
)
hh3cReplicaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaInterval.setStatus("current")


class _Hh3cReplicaEncrypt_Type(Hh3cStorageEnableState):
    """Custom type hh3cReplicaEncrypt based on Hh3cStorageEnableState"""


_Hh3cReplicaEncrypt_Object = MibTableColumn
hh3cReplicaEncrypt = _Hh3cReplicaEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 19),
    _Hh3cReplicaEncrypt_Type()
)
hh3cReplicaEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaEncrypt.setStatus("current")


class _Hh3cReplicaCompress_Type(Hh3cStorageEnableState):
    """Custom type hh3cReplicaCompress based on Hh3cStorageEnableState"""


_Hh3cReplicaCompress_Object = MibTableColumn
hh3cReplicaCompress = _Hh3cReplicaCompress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 20),
    _Hh3cReplicaCompress_Type()
)
hh3cReplicaCompress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaCompress.setStatus("current")


class _Hh3cReplicaUseExistTM_Type(Hh3cStorageEnableState):
    """Custom type hh3cReplicaUseExistTM based on Hh3cStorageEnableState"""


_Hh3cReplicaUseExistTM_Object = MibTableColumn
hh3cReplicaUseExistTM = _Hh3cReplicaUseExistTM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 21),
    _Hh3cReplicaUseExistTM_Type()
)
hh3cReplicaUseExistTM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaUseExistTM.setStatus("current")


class _Hh3cReplicaProtocol_Type(Integer32):
    """Custom type hh3cReplicaProtocol based on Integer32"""
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


_Hh3cReplicaProtocol_Type.__name__ = "Integer32"
_Hh3cReplicaProtocol_Object = MibTableColumn
hh3cReplicaProtocol = _Hh3cReplicaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 22),
    _Hh3cReplicaProtocol_Type()
)
hh3cReplicaProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaProtocol.setStatus("current")
_Hh3cReplicaScanDiff_Type = TruthValue
_Hh3cReplicaScanDiff_Object = MibTableColumn
hh3cReplicaScanDiff = _Hh3cReplicaScanDiff_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 23),
    _Hh3cReplicaScanDiff_Type()
)
hh3cReplicaScanDiff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaScanDiff.setStatus("current")


class _Hh3cReplicaStatSwitch_Type(Integer32):
    """Custom type hh3cReplicaStatSwitch based on Integer32"""
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


_Hh3cReplicaStatSwitch_Type.__name__ = "Integer32"
_Hh3cReplicaStatSwitch_Object = MibTableColumn
hh3cReplicaStatSwitch = _Hh3cReplicaStatSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 24),
    _Hh3cReplicaStatSwitch_Type()
)
hh3cReplicaStatSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaStatSwitch.setStatus("current")
_Hh3cReplicaRowStatus_Type = RowStatus
_Hh3cReplicaRowStatus_Object = MibTableColumn
hh3cReplicaRowStatus = _Hh3cReplicaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 10, 1, 25),
    _Hh3cReplicaRowStatus_Type()
)
hh3cReplicaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cReplicaRowStatus.setStatus("current")
_Hh3cReplicaStateTable_Object = MibTable
hh3cReplicaStateTable = _Hh3cReplicaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hh3cReplicaStateTable.setStatus("current")
_Hh3cReplicaStateEntry_Object = MibTableRow
hh3cReplicaStateEntry = _Hh3cReplicaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 11, 1)
)
hh3cReplicaStateEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cRepLocalLvIndex"),
)
if mibBuilder.loadTexts:
    hh3cReplicaStateEntry.setStatus("current")
_Hh3cReplicaDelta_Type = Integer32
_Hh3cReplicaDelta_Object = MibTableColumn
hh3cReplicaDelta = _Hh3cReplicaDelta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 11, 1, 1),
    _Hh3cReplicaDelta_Type()
)
hh3cReplicaDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cReplicaDelta.setStatus("current")
if mibBuilder.loadTexts:
    hh3cReplicaDelta.setUnits("MB")
_Hh3cReplicaLastSyncTime_Type = DateAndTime
_Hh3cReplicaLastSyncTime_Object = MibTableColumn
hh3cReplicaLastSyncTime = _Hh3cReplicaLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 11, 1, 2),
    _Hh3cReplicaLastSyncTime_Type()
)
hh3cReplicaLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cReplicaLastSyncTime.setStatus("current")
_Hh3cReplicaNextSyncTime_Type = DateAndTime
_Hh3cReplicaNextSyncTime_Object = MibTableColumn
hh3cReplicaNextSyncTime = _Hh3cReplicaNextSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 11, 1, 3),
    _Hh3cReplicaNextSyncTime_Type()
)
hh3cReplicaNextSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cReplicaNextSyncTime.setStatus("current")
_Hh3cReplicaSyncTotalSize_Type = Integer32
_Hh3cReplicaSyncTotalSize_Object = MibTableColumn
hh3cReplicaSyncTotalSize = _Hh3cReplicaSyncTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 11, 1, 4),
    _Hh3cReplicaSyncTotalSize_Type()
)
hh3cReplicaSyncTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cReplicaSyncTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cReplicaSyncTotalSize.setUnits("MB")
_Hh3cReplicaSyncCurPercentage_Type = Integer32
_Hh3cReplicaSyncCurPercentage_Object = MibTableColumn
hh3cReplicaSyncCurPercentage = _Hh3cReplicaSyncCurPercentage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 11, 1, 5),
    _Hh3cReplicaSyncCurPercentage_Type()
)
hh3cReplicaSyncCurPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cReplicaSyncCurPercentage.setStatus("current")
_Hh3cReplicaSyncPerformance_Type = Integer32
_Hh3cReplicaSyncPerformance_Object = MibTableColumn
hh3cReplicaSyncPerformance = _Hh3cReplicaSyncPerformance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 11, 1, 6),
    _Hh3cReplicaSyncPerformance_Type()
)
hh3cReplicaSyncPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cReplicaSyncPerformance.setStatus("current")


class _Hh3cReplicaRunStatus_Type(Integer32):
    """Custom type hh3cReplicaRunStatus based on Integer32"""
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


_Hh3cReplicaRunStatus_Type.__name__ = "Integer32"
_Hh3cReplicaRunStatus_Object = MibTableColumn
hh3cReplicaRunStatus = _Hh3cReplicaRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 11, 1, 7),
    _Hh3cReplicaRunStatus_Type()
)
hh3cReplicaRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cReplicaRunStatus.setStatus("current")
_Hh3cCDRConfigTable_Object = MibTable
hh3cCDRConfigTable = _Hh3cCDRConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 12)
)
if mibBuilder.loadTexts:
    hh3cCDRConfigTable.setStatus("current")
_Hh3cCDRConfigEntry_Object = MibTableRow
hh3cCDRConfigEntry = _Hh3cCDRConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 12, 1)
)
hh3cCDRConfigEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cCDRLvIndex"),
)
if mibBuilder.loadTexts:
    hh3cCDRConfigEntry.setStatus("current")
_Hh3cCDRLvIndex_Type = Hh3cLvIDType
_Hh3cCDRLvIndex_Object = MibTableColumn
hh3cCDRLvIndex = _Hh3cCDRLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 12, 1, 1),
    _Hh3cCDRLvIndex_Type()
)
hh3cCDRLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCDRLvIndex.setStatus("current")
_Hh3cCDRID_Type = Integer32
_Hh3cCDRID_Object = MibTableColumn
hh3cCDRID = _Hh3cCDRID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 12, 1, 2),
    _Hh3cCDRID_Type()
)
hh3cCDRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCDRID.setStatus("current")
_Hh3cCDRStatus_Type = Hh3cStorageOnlineState
_Hh3cCDRStatus_Object = MibTableColumn
hh3cCDRStatus = _Hh3cCDRStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 12, 1, 3),
    _Hh3cCDRStatus_Type()
)
hh3cCDRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCDRStatus.setStatus("current")
_Hh3cCDRTotalSize_Type = Integer32
_Hh3cCDRTotalSize_Object = MibTableColumn
hh3cCDRTotalSize = _Hh3cCDRTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 12, 1, 4),
    _Hh3cCDRTotalSize_Type()
)
hh3cCDRTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCDRTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCDRTotalSize.setUnits("MB")
_Hh3cCDRFreeSize_Type = Integer32
_Hh3cCDRFreeSize_Object = MibTableColumn
hh3cCDRFreeSize = _Hh3cCDRFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 12, 1, 5),
    _Hh3cCDRFreeSize_Type()
)
hh3cCDRFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCDRFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCDRFreeSize.setUnits("MB")


class _Hh3cCDRSelectPolicy_Type(Hh3cExtendSelectPolicy):
    """Custom type hh3cCDRSelectPolicy based on Hh3cExtendSelectPolicy"""


_Hh3cCDRSelectPolicy_Object = MibTableColumn
hh3cCDRSelectPolicy = _Hh3cCDRSelectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 12, 1, 6),
    _Hh3cCDRSelectPolicy_Type()
)
hh3cCDRSelectPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCDRSelectPolicy.setStatus("current")
_Hh3cCDRRowStatus_Type = RowStatus
_Hh3cCDRRowStatus_Object = MibTableColumn
hh3cCDRRowStatus = _Hh3cCDRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 12, 1, 7),
    _Hh3cCDRRowStatus_Type()
)
hh3cCDRRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCDRRowStatus.setStatus("current")
_Hh3cCDRDistributeTable_Object = MibTable
hh3cCDRDistributeTable = _Hh3cCDRDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 13)
)
if mibBuilder.loadTexts:
    hh3cCDRDistributeTable.setStatus("current")
_Hh3cCDRDistributeEntry_Object = MibTableRow
hh3cCDRDistributeEntry = _Hh3cCDRDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 13, 1)
)
hh3cCDRDistributeEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cCDRDistLvIndex"),
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cCDRRaidUuid"),
)
if mibBuilder.loadTexts:
    hh3cCDRDistributeEntry.setStatus("current")
_Hh3cCDRDistLvIndex_Type = Hh3cLvIDType
_Hh3cCDRDistLvIndex_Object = MibTableColumn
hh3cCDRDistLvIndex = _Hh3cCDRDistLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 13, 1, 1),
    _Hh3cCDRDistLvIndex_Type()
)
hh3cCDRDistLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCDRDistLvIndex.setStatus("current")
_Hh3cCDRRaidUuid_Type = Hh3cRaidIDType
_Hh3cCDRRaidUuid_Object = MibTableColumn
hh3cCDRRaidUuid = _Hh3cCDRRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 13, 1, 2),
    _Hh3cCDRRaidUuid_Type()
)
hh3cCDRRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCDRRaidUuid.setStatus("current")
_Hh3cCDRRaidSize_Type = Integer32
_Hh3cCDRRaidSize_Object = MibTableColumn
hh3cCDRRaidSize = _Hh3cCDRRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 13, 1, 3),
    _Hh3cCDRRaidSize_Type()
)
hh3cCDRRaidSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCDRRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCDRRaidSize.setUnits("MB")
_Hh3cCDRExtRowStatus_Type = RowStatus
_Hh3cCDRExtRowStatus_Object = MibTableColumn
hh3cCDRExtRowStatus = _Hh3cCDRExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 13, 1, 4),
    _Hh3cCDRExtRowStatus_Type()
)
hh3cCDRExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCDRExtRowStatus.setStatus("current")
_Hh3cSafeCacheConfigTable_Object = MibTable
hh3cSafeCacheConfigTable = _Hh3cSafeCacheConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14)
)
if mibBuilder.loadTexts:
    hh3cSafeCacheConfigTable.setStatus("current")
_Hh3cSafeCacheConfigEntry_Object = MibTableRow
hh3cSafeCacheConfigEntry = _Hh3cSafeCacheConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1)
)
hh3cSafeCacheConfigEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSafeCacheLvIndex"),
)
if mibBuilder.loadTexts:
    hh3cSafeCacheConfigEntry.setStatus("current")
_Hh3cSafeCacheLvIndex_Type = Hh3cLvIDType
_Hh3cSafeCacheLvIndex_Object = MibTableColumn
hh3cSafeCacheLvIndex = _Hh3cSafeCacheLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 1),
    _Hh3cSafeCacheLvIndex_Type()
)
hh3cSafeCacheLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSafeCacheLvIndex.setStatus("current")
_Hh3cSafeCacheID_Type = Integer32
_Hh3cSafeCacheID_Object = MibTableColumn
hh3cSafeCacheID = _Hh3cSafeCacheID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 2),
    _Hh3cSafeCacheID_Type()
)
hh3cSafeCacheID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSafeCacheID.setStatus("current")
_Hh3cSafeCacheStatus_Type = Hh3cStorageOnlineState
_Hh3cSafeCacheStatus_Object = MibTableColumn
hh3cSafeCacheStatus = _Hh3cSafeCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 3),
    _Hh3cSafeCacheStatus_Type()
)
hh3cSafeCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSafeCacheStatus.setStatus("current")
_Hh3cSafeCacheTotalSize_Type = Integer32
_Hh3cSafeCacheTotalSize_Object = MibTableColumn
hh3cSafeCacheTotalSize = _Hh3cSafeCacheTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 4),
    _Hh3cSafeCacheTotalSize_Type()
)
hh3cSafeCacheTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSafeCacheTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSafeCacheTotalSize.setUnits("MB")
_Hh3cSafeCacheFreeSize_Type = Integer32
_Hh3cSafeCacheFreeSize_Object = MibTableColumn
hh3cSafeCacheFreeSize = _Hh3cSafeCacheFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 5),
    _Hh3cSafeCacheFreeSize_Type()
)
hh3cSafeCacheFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSafeCacheFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSafeCacheFreeSize.setUnits("MB")


class _Hh3cSafeCacheSelectPolicy_Type(Hh3cExtendSelectPolicy):
    """Custom type hh3cSafeCacheSelectPolicy based on Hh3cExtendSelectPolicy"""


_Hh3cSafeCacheSelectPolicy_Object = MibTableColumn
hh3cSafeCacheSelectPolicy = _Hh3cSafeCacheSelectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 6),
    _Hh3cSafeCacheSelectPolicy_Type()
)
hh3cSafeCacheSelectPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSafeCacheSelectPolicy.setStatus("current")


class _Hh3cSafeCacheThreshold_Type(Integer32):
    """Custom type hh3cSafeCacheThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cSafeCacheThreshold_Type.__name__ = "Integer32"
_Hh3cSafeCacheThreshold_Object = MibTableColumn
hh3cSafeCacheThreshold = _Hh3cSafeCacheThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 7),
    _Hh3cSafeCacheThreshold_Type()
)
hh3cSafeCacheThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSafeCacheThreshold.setStatus("current")
_Hh3cSafeCacheFlushTime_Type = Integer32
_Hh3cSafeCacheFlushTime_Object = MibTableColumn
hh3cSafeCacheFlushTime = _Hh3cSafeCacheFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 8),
    _Hh3cSafeCacheFlushTime_Type()
)
hh3cSafeCacheFlushTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSafeCacheFlushTime.setStatus("current")


class _Hh3cSafeCacheFlushCommand_Type(Integer32):
    """Custom type hh3cSafeCacheFlushCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cSafeCacheFlushCommand_Type.__name__ = "Integer32"
_Hh3cSafeCacheFlushCommand_Object = MibTableColumn
hh3cSafeCacheFlushCommand = _Hh3cSafeCacheFlushCommand_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 9),
    _Hh3cSafeCacheFlushCommand_Type()
)
hh3cSafeCacheFlushCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSafeCacheFlushCommand.setStatus("current")


class _Hh3cSafeCacheSkipDupWrite_Type(Integer32):
    """Custom type hh3cSafeCacheSkipDupWrite based on Integer32"""
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


_Hh3cSafeCacheSkipDupWrite_Type.__name__ = "Integer32"
_Hh3cSafeCacheSkipDupWrite_Object = MibTableColumn
hh3cSafeCacheSkipDupWrite = _Hh3cSafeCacheSkipDupWrite_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 10),
    _Hh3cSafeCacheSkipDupWrite_Type()
)
hh3cSafeCacheSkipDupWrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSafeCacheSkipDupWrite.setStatus("current")


class _Hh3cSafeCacheRunStatus_Type(Integer32):
    """Custom type hh3cSafeCacheRunStatus based on Integer32"""
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


_Hh3cSafeCacheRunStatus_Type.__name__ = "Integer32"
_Hh3cSafeCacheRunStatus_Object = MibTableColumn
hh3cSafeCacheRunStatus = _Hh3cSafeCacheRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 11),
    _Hh3cSafeCacheRunStatus_Type()
)
hh3cSafeCacheRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSafeCacheRunStatus.setStatus("current")


class _Hh3cSafeCacheSwitch_Type(Integer32):
    """Custom type hh3cSafeCacheSwitch based on Integer32"""
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


_Hh3cSafeCacheSwitch_Type.__name__ = "Integer32"
_Hh3cSafeCacheSwitch_Object = MibTableColumn
hh3cSafeCacheSwitch = _Hh3cSafeCacheSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 12),
    _Hh3cSafeCacheSwitch_Type()
)
hh3cSafeCacheSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSafeCacheSwitch.setStatus("current")
_Hh3cSafeCacheRowStatus_Type = RowStatus
_Hh3cSafeCacheRowStatus_Object = MibTableColumn
hh3cSafeCacheRowStatus = _Hh3cSafeCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 14, 1, 13),
    _Hh3cSafeCacheRowStatus_Type()
)
hh3cSafeCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSafeCacheRowStatus.setStatus("current")
_Hh3cSafeCacheDistributeTable_Object = MibTable
hh3cSafeCacheDistributeTable = _Hh3cSafeCacheDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 15)
)
if mibBuilder.loadTexts:
    hh3cSafeCacheDistributeTable.setStatus("current")
_Hh3cSafeCacheDistributeEntry_Object = MibTableRow
hh3cSafeCacheDistributeEntry = _Hh3cSafeCacheDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 15, 1)
)
hh3cSafeCacheDistributeEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSafeCacheDistLvIndex"),
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cSafeCacheRaidUuid"),
)
if mibBuilder.loadTexts:
    hh3cSafeCacheDistributeEntry.setStatus("current")
_Hh3cSafeCacheDistLvIndex_Type = Hh3cLvIDType
_Hh3cSafeCacheDistLvIndex_Object = MibTableColumn
hh3cSafeCacheDistLvIndex = _Hh3cSafeCacheDistLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 15, 1, 1),
    _Hh3cSafeCacheDistLvIndex_Type()
)
hh3cSafeCacheDistLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSafeCacheDistLvIndex.setStatus("current")
_Hh3cSafeCacheRaidUuid_Type = Hh3cRaidIDType
_Hh3cSafeCacheRaidUuid_Object = MibTableColumn
hh3cSafeCacheRaidUuid = _Hh3cSafeCacheRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 15, 1, 2),
    _Hh3cSafeCacheRaidUuid_Type()
)
hh3cSafeCacheRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSafeCacheRaidUuid.setStatus("current")
_Hh3cSafeCacheRaidSize_Type = Integer32
_Hh3cSafeCacheRaidSize_Object = MibTableColumn
hh3cSafeCacheRaidSize = _Hh3cSafeCacheRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 15, 1, 3),
    _Hh3cSafeCacheRaidSize_Type()
)
hh3cSafeCacheRaidSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSafeCacheRaidSize.setStatus("current")
_Hh3cSafeCacheExtRowStatus_Type = RowStatus
_Hh3cSafeCacheExtRowStatus_Object = MibTableColumn
hh3cSafeCacheExtRowStatus = _Hh3cSafeCacheExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 15, 1, 4),
    _Hh3cSafeCacheExtRowStatus_Type()
)
hh3cSafeCacheExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSafeCacheExtRowStatus.setStatus("current")
_Hh3cMirrorConfigTable_Object = MibTable
hh3cMirrorConfigTable = _Hh3cMirrorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16)
)
if mibBuilder.loadTexts:
    hh3cMirrorConfigTable.setStatus("current")
_Hh3cMirrorConfigEntry_Object = MibTableRow
hh3cMirrorConfigEntry = _Hh3cMirrorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1)
)
hh3cMirrorConfigEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cMirrorLvIndex"),
)
if mibBuilder.loadTexts:
    hh3cMirrorConfigEntry.setStatus("current")
_Hh3cMirrorLvIndex_Type = Hh3cLvIDType
_Hh3cMirrorLvIndex_Object = MibTableColumn
hh3cMirrorLvIndex = _Hh3cMirrorLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 1),
    _Hh3cMirrorLvIndex_Type()
)
hh3cMirrorLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMirrorLvIndex.setStatus("current")


class _Hh3cMirrorType_Type(Integer32):
    """Custom type hh3cMirrorType based on Integer32"""
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


_Hh3cMirrorType_Type.__name__ = "Integer32"
_Hh3cMirrorType_Object = MibTableColumn
hh3cMirrorType = _Hh3cMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 2),
    _Hh3cMirrorType_Type()
)
hh3cMirrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMirrorType.setStatus("current")
_Hh3cMirrorStatus_Type = Hh3cStorageOnlineState
_Hh3cMirrorStatus_Object = MibTableColumn
hh3cMirrorStatus = _Hh3cMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 3),
    _Hh3cMirrorStatus_Type()
)
hh3cMirrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMirrorStatus.setStatus("current")
_Hh3cMirrorName_Type = OctetString
_Hh3cMirrorName_Object = MibTableColumn
hh3cMirrorName = _Hh3cMirrorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 4),
    _Hh3cMirrorName_Type()
)
hh3cMirrorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorName.setStatus("current")


class _Hh3cMirrorSyncPercentage_Type(Integer32):
    """Custom type hh3cMirrorSyncPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cMirrorSyncPercentage_Type.__name__ = "Integer32"
_Hh3cMirrorSyncPercentage_Object = MibTableColumn
hh3cMirrorSyncPercentage = _Hh3cMirrorSyncPercentage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 5),
    _Hh3cMirrorSyncPercentage_Type()
)
hh3cMirrorSyncPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMirrorSyncPercentage.setStatus("current")


class _Hh3cMirrorSyncPerformance_Type(Integer32):
    """Custom type hh3cMirrorSyncPerformance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cMirrorSyncPerformance_Type.__name__ = "Integer32"
_Hh3cMirrorSyncPerformance_Object = MibTableColumn
hh3cMirrorSyncPerformance = _Hh3cMirrorSyncPerformance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 6),
    _Hh3cMirrorSyncPerformance_Type()
)
hh3cMirrorSyncPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMirrorSyncPerformance.setStatus("current")
_Hh3cMirrorDelta_Type = Integer32
_Hh3cMirrorDelta_Object = MibTableColumn
hh3cMirrorDelta = _Hh3cMirrorDelta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 7),
    _Hh3cMirrorDelta_Type()
)
hh3cMirrorDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMirrorDelta.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMirrorDelta.setUnits("MB")


class _Hh3cMirrorRaidType_Type(Integer32):
    """Custom type hh3cMirrorRaidType based on Integer32"""
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


_Hh3cMirrorRaidType_Type.__name__ = "Integer32"
_Hh3cMirrorRaidType_Object = MibTableColumn
hh3cMirrorRaidType = _Hh3cMirrorRaidType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 8),
    _Hh3cMirrorRaidType_Type()
)
hh3cMirrorRaidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorRaidType.setStatus("current")


class _Hh3cMirrorSelectPolicy_Type(Hh3cExtendSelectPolicy):
    """Custom type hh3cMirrorSelectPolicy based on Hh3cExtendSelectPolicy"""


_Hh3cMirrorSelectPolicy_Object = MibTableColumn
hh3cMirrorSelectPolicy = _Hh3cMirrorSelectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 9),
    _Hh3cMirrorSelectPolicy_Type()
)
hh3cMirrorSelectPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorSelectPolicy.setStatus("current")


class _Hh3cMirrorSwitch_Type(Integer32):
    """Custom type hh3cMirrorSwitch based on Integer32"""
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


_Hh3cMirrorSwitch_Type.__name__ = "Integer32"
_Hh3cMirrorSwitch_Object = MibTableColumn
hh3cMirrorSwitch = _Hh3cMirrorSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 10),
    _Hh3cMirrorSwitch_Type()
)
hh3cMirrorSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorSwitch.setStatus("current")
_Hh3cMirrorExtendRaidUuid_Type = Hh3cRaidIDType
_Hh3cMirrorExtendRaidUuid_Object = MibTableColumn
hh3cMirrorExtendRaidUuid = _Hh3cMirrorExtendRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 11),
    _Hh3cMirrorExtendRaidUuid_Type()
)
hh3cMirrorExtendRaidUuid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorExtendRaidUuid.setStatus("current")
_Hh3cMirrorRowStatus_Type = RowStatus
_Hh3cMirrorRowStatus_Object = MibTableColumn
hh3cMirrorRowStatus = _Hh3cMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 16, 1, 12),
    _Hh3cMirrorRowStatus_Type()
)
hh3cMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorRowStatus.setStatus("current")
_Hh3cMirrorDistributeTable_Object = MibTable
hh3cMirrorDistributeTable = _Hh3cMirrorDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 17)
)
if mibBuilder.loadTexts:
    hh3cMirrorDistributeTable.setStatus("current")
_Hh3cMirrorDistributeEntry_Object = MibTableRow
hh3cMirrorDistributeEntry = _Hh3cMirrorDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 17, 1)
)
hh3cMirrorDistributeEntry.setIndexNames(
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cMirrorDistLvIndex"),
    (0, "HH3C-STORAGE-SNAP-MIB", "hh3cMirrorRaidUuid"),
)
if mibBuilder.loadTexts:
    hh3cMirrorDistributeEntry.setStatus("current")
_Hh3cMirrorDistLvIndex_Type = Hh3cLvIDType
_Hh3cMirrorDistLvIndex_Object = MibTableColumn
hh3cMirrorDistLvIndex = _Hh3cMirrorDistLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 17, 1, 1),
    _Hh3cMirrorDistLvIndex_Type()
)
hh3cMirrorDistLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMirrorDistLvIndex.setStatus("current")
_Hh3cMirrorRaidUuid_Type = Hh3cRaidIDType
_Hh3cMirrorRaidUuid_Object = MibTableColumn
hh3cMirrorRaidUuid = _Hh3cMirrorRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 17, 1, 2),
    _Hh3cMirrorRaidUuid_Type()
)
hh3cMirrorRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMirrorRaidUuid.setStatus("current")
_Hh3cMirrorRaidSize_Type = Integer32
_Hh3cMirrorRaidSize_Object = MibTableColumn
hh3cMirrorRaidSize = _Hh3cMirrorRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 17, 1, 3),
    _Hh3cMirrorRaidSize_Type()
)
hh3cMirrorRaidSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorRaidSize.setStatus("current")
_Hh3cMirrorExtRowStatus_Type = RowStatus
_Hh3cMirrorExtRowStatus_Object = MibTableColumn
hh3cMirrorExtRowStatus = _Hh3cMirrorExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2, 1, 17, 1, 4),
    _Hh3cMirrorExtRowStatus_Type()
)
hh3cMirrorExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorExtRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-STORAGE-SNAP-MIB",
    **{"hh3cStorageSnap": hh3cStorageSnap,
       "hh3cSnapMibObjects": hh3cSnapMibObjects,
       "hh3cGlobalSnapSettingsObject": hh3cGlobalSnapSettingsObject,
       "hh3cAddtionalSpaceMaxSize": hh3cAddtionalSpaceMaxSize,
       "hh3cSnapConfigTable": hh3cSnapConfigTable,
       "hh3cSnapConfigEntry": hh3cSnapConfigEntry,
       "hh3cSnapLvIndex": hh3cSnapLvIndex,
       "hh3cSnapAreaId": hh3cSnapAreaId,
       "hh3cSnapAreaAutoExpand": hh3cSnapAreaAutoExpand,
       "hh3cSnapAreaThreshold": hh3cSnapAreaThreshold,
       "hh3cSnapAreaIncSize": hh3cSnapAreaIncSize,
       "hh3cSnapAreaMaxSize": hh3cSnapAreaMaxSize,
       "hh3cSnapAreaFullDeleteTM": hh3cSnapAreaFullDeleteTM,
       "hh3cSnapAreaNotify": hh3cSnapAreaNotify,
       "hh3cSnapAreaStatus": hh3cSnapAreaStatus,
       "hh3cSnapRaidUuid": hh3cSnapRaidUuid,
       "hh3cSnapRaidSize": hh3cSnapRaidSize,
       "hh3cSnapRaidSelectPolicy": hh3cSnapRaidSelectPolicy,
       "hh3cSnapAreaTotalSize": hh3cSnapAreaTotalSize,
       "hh3cSnapAreaFreeSize": hh3cSnapAreaFreeSize,
       "hh3cSnapExtendTimes": hh3cSnapExtendTimes,
       "hh3cSnapRowStatus": hh3cSnapRowStatus,
       "hh3cSnapExpandTable": hh3cSnapExpandTable,
       "hh3cSnapExpandEntry": hh3cSnapExpandEntry,
       "hh3cSAExpRaidUuid": hh3cSAExpRaidUuid,
       "hh3cSAExpSize": hh3cSAExpSize,
       "hh3cSAExpRaidSize": hh3cSAExpRaidSize,
       "hh3cSnapAreaExpRowStatus": hh3cSnapAreaExpRowStatus,
       "hh3cSnapCopyTable": hh3cSnapCopyTable,
       "hh3cSnapCopyEntry": hh3cSnapCopyEntry,
       "hh3cSnapCopyLvIndex": hh3cSnapCopyLvIndex,
       "hh3cSnapCopyPercentage": hh3cSnapCopyPercentage,
       "hh3cSnapCopyStartTime": hh3cSnapCopyStartTime,
       "hh3cSnapCopySwitch": hh3cSnapCopySwitch,
       "hh3cTimeMarkConfigTable": hh3cTimeMarkConfigTable,
       "hh3cTimeMarkConfigEntry": hh3cTimeMarkConfigEntry,
       "hh3cTimeMarkCounts": hh3cTimeMarkCounts,
       "hh3cTimeMarkInitializeTime": hh3cTimeMarkInitializeTime,
       "hh3cTimeMarkInterval": hh3cTimeMarkInterval,
       "hh3cTimeMarkLastTime": hh3cTimeMarkLastTime,
       "hh3cTimeMarkTotal": hh3cTimeMarkTotal,
       "hh3cTimeMarkSwitch": hh3cTimeMarkSwitch,
       "hh3cTimeMarkCreateTable": hh3cTimeMarkCreateTable,
       "hh3cTimeMarkCreateEntry": hh3cTimeMarkCreateEntry,
       "hh3cTimeMarkStamp": hh3cTimeMarkStamp,
       "hh3cTimeMarkComment": hh3cTimeMarkComment,
       "hh3cTimeMarkSize": hh3cTimeMarkSize,
       "hh3cTimeMarkRowStatus": hh3cTimeMarkRowStatus,
       "hh3cTimeMarkCopyTable": hh3cTimeMarkCopyTable,
       "hh3cTimeMarkCopyEntry": hh3cTimeMarkCopyEntry,
       "hh3cTMCopyDestLvId": hh3cTMCopyDestLvId,
       "hh3cTMCopyPercentage": hh3cTMCopyPercentage,
       "hh3cTMCopyStartTime": hh3cTMCopyStartTime,
       "hh3cTMCopySwitch": hh3cTMCopySwitch,
       "hh3cTimeMarkRollbackTable": hh3cTimeMarkRollbackTable,
       "hh3cTimeMarkRollbackEntry": hh3cTimeMarkRollbackEntry,
       "hh3cTMRollbackPercentage": hh3cTMRollbackPercentage,
       "hh3cTMRollbackStartTime": hh3cTMRollbackStartTime,
       "hh3cTMRollbackSwitch": hh3cTMRollbackSwitch,
       "hh3cTimeViewTable": hh3cTimeViewTable,
       "hh3cTimeViewEntry": hh3cTimeViewEntry,
       "hh3cTimeViewStamp": hh3cTimeViewStamp,
       "hh3cTimeViewID": hh3cTimeViewID,
       "hh3cTimeViewName": hh3cTimeViewName,
       "hh3cTimeViewRowStatus": hh3cTimeViewRowStatus,
       "hh3cReplicaConfigTable": hh3cReplicaConfigTable,
       "hh3cReplicaConfigEntry": hh3cReplicaConfigEntry,
       "hh3cRepLocalLvIndex": hh3cRepLocalLvIndex,
       "hh3cLvRepLocalWay": hh3cLvRepLocalWay,
       "hh3cRepLocalServerIP": hh3cRepLocalServerIP,
       "hh3cRepLocalServerIPType": hh3cRepLocalServerIPType,
       "hh3cRepLocalServerName": hh3cRepLocalServerName,
       "hh3cRepLocalServerUsername": hh3cRepLocalServerUsername,
       "hh3cRepLocalServerPassword": hh3cRepLocalServerPassword,
       "hh3cRepRemoteServerIP": hh3cRepRemoteServerIP,
       "hh3cRepRemoteServerIPType": hh3cRepRemoteServerIPType,
       "hh3cRepRemoteServerName": hh3cRepRemoteServerName,
       "hh3cRepRemoteServerUsername": hh3cRepRemoteServerUsername,
       "hh3cRepRemoteServerPassword": hh3cRepRemoteServerPassword,
       "hh3cRepRemoteLvIndex": hh3cRepRemoteLvIndex,
       "hh3cReplicaMode": hh3cReplicaMode,
       "hh3cReplicaWatermark": hh3cReplicaWatermark,
       "hh3cReplicaWatermarkRetry": hh3cReplicaWatermarkRetry,
       "hh3cReplicaInitializeTime": hh3cReplicaInitializeTime,
       "hh3cReplicaInterval": hh3cReplicaInterval,
       "hh3cReplicaEncrypt": hh3cReplicaEncrypt,
       "hh3cReplicaCompress": hh3cReplicaCompress,
       "hh3cReplicaUseExistTM": hh3cReplicaUseExistTM,
       "hh3cReplicaProtocol": hh3cReplicaProtocol,
       "hh3cReplicaScanDiff": hh3cReplicaScanDiff,
       "hh3cReplicaStatSwitch": hh3cReplicaStatSwitch,
       "hh3cReplicaRowStatus": hh3cReplicaRowStatus,
       "hh3cReplicaStateTable": hh3cReplicaStateTable,
       "hh3cReplicaStateEntry": hh3cReplicaStateEntry,
       "hh3cReplicaDelta": hh3cReplicaDelta,
       "hh3cReplicaLastSyncTime": hh3cReplicaLastSyncTime,
       "hh3cReplicaNextSyncTime": hh3cReplicaNextSyncTime,
       "hh3cReplicaSyncTotalSize": hh3cReplicaSyncTotalSize,
       "hh3cReplicaSyncCurPercentage": hh3cReplicaSyncCurPercentage,
       "hh3cReplicaSyncPerformance": hh3cReplicaSyncPerformance,
       "hh3cReplicaRunStatus": hh3cReplicaRunStatus,
       "hh3cCDRConfigTable": hh3cCDRConfigTable,
       "hh3cCDRConfigEntry": hh3cCDRConfigEntry,
       "hh3cCDRLvIndex": hh3cCDRLvIndex,
       "hh3cCDRID": hh3cCDRID,
       "hh3cCDRStatus": hh3cCDRStatus,
       "hh3cCDRTotalSize": hh3cCDRTotalSize,
       "hh3cCDRFreeSize": hh3cCDRFreeSize,
       "hh3cCDRSelectPolicy": hh3cCDRSelectPolicy,
       "hh3cCDRRowStatus": hh3cCDRRowStatus,
       "hh3cCDRDistributeTable": hh3cCDRDistributeTable,
       "hh3cCDRDistributeEntry": hh3cCDRDistributeEntry,
       "hh3cCDRDistLvIndex": hh3cCDRDistLvIndex,
       "hh3cCDRRaidUuid": hh3cCDRRaidUuid,
       "hh3cCDRRaidSize": hh3cCDRRaidSize,
       "hh3cCDRExtRowStatus": hh3cCDRExtRowStatus,
       "hh3cSafeCacheConfigTable": hh3cSafeCacheConfigTable,
       "hh3cSafeCacheConfigEntry": hh3cSafeCacheConfigEntry,
       "hh3cSafeCacheLvIndex": hh3cSafeCacheLvIndex,
       "hh3cSafeCacheID": hh3cSafeCacheID,
       "hh3cSafeCacheStatus": hh3cSafeCacheStatus,
       "hh3cSafeCacheTotalSize": hh3cSafeCacheTotalSize,
       "hh3cSafeCacheFreeSize": hh3cSafeCacheFreeSize,
       "hh3cSafeCacheSelectPolicy": hh3cSafeCacheSelectPolicy,
       "hh3cSafeCacheThreshold": hh3cSafeCacheThreshold,
       "hh3cSafeCacheFlushTime": hh3cSafeCacheFlushTime,
       "hh3cSafeCacheFlushCommand": hh3cSafeCacheFlushCommand,
       "hh3cSafeCacheSkipDupWrite": hh3cSafeCacheSkipDupWrite,
       "hh3cSafeCacheRunStatus": hh3cSafeCacheRunStatus,
       "hh3cSafeCacheSwitch": hh3cSafeCacheSwitch,
       "hh3cSafeCacheRowStatus": hh3cSafeCacheRowStatus,
       "hh3cSafeCacheDistributeTable": hh3cSafeCacheDistributeTable,
       "hh3cSafeCacheDistributeEntry": hh3cSafeCacheDistributeEntry,
       "hh3cSafeCacheDistLvIndex": hh3cSafeCacheDistLvIndex,
       "hh3cSafeCacheRaidUuid": hh3cSafeCacheRaidUuid,
       "hh3cSafeCacheRaidSize": hh3cSafeCacheRaidSize,
       "hh3cSafeCacheExtRowStatus": hh3cSafeCacheExtRowStatus,
       "hh3cMirrorConfigTable": hh3cMirrorConfigTable,
       "hh3cMirrorConfigEntry": hh3cMirrorConfigEntry,
       "hh3cMirrorLvIndex": hh3cMirrorLvIndex,
       "hh3cMirrorType": hh3cMirrorType,
       "hh3cMirrorStatus": hh3cMirrorStatus,
       "hh3cMirrorName": hh3cMirrorName,
       "hh3cMirrorSyncPercentage": hh3cMirrorSyncPercentage,
       "hh3cMirrorSyncPerformance": hh3cMirrorSyncPerformance,
       "hh3cMirrorDelta": hh3cMirrorDelta,
       "hh3cMirrorRaidType": hh3cMirrorRaidType,
       "hh3cMirrorSelectPolicy": hh3cMirrorSelectPolicy,
       "hh3cMirrorSwitch": hh3cMirrorSwitch,
       "hh3cMirrorExtendRaidUuid": hh3cMirrorExtendRaidUuid,
       "hh3cMirrorRowStatus": hh3cMirrorRowStatus,
       "hh3cMirrorDistributeTable": hh3cMirrorDistributeTable,
       "hh3cMirrorDistributeEntry": hh3cMirrorDistributeEntry,
       "hh3cMirrorDistLvIndex": hh3cMirrorDistLvIndex,
       "hh3cMirrorRaidUuid": hh3cMirrorRaidUuid,
       "hh3cMirrorRaidSize": hh3cMirrorRaidSize,
       "hh3cMirrorExtRowStatus": hh3cMirrorExtRowStatus}
)
