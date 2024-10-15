# SNMP MIB module (HUAWEI-TAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:10 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwTAD = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWEnableValue(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_HwTADObjects_ObjectIdentity = ObjectIdentity
hwTADObjects = _HwTADObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1)
)
_HwTADInterfaceTable_Object = MibTable
hwTADInterfaceTable = _HwTADInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1)
)
if mibBuilder.loadTexts:
    hwTADInterfaceTable.setStatus("current")
_HwTADInterfaceEntry_Object = MibTableRow
hwTADInterfaceEntry = _HwTADInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1)
)
hwTADInterfaceEntry.setIndexNames(
    (0, "HUAWEI-TAD-MIB", "hwTADInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwTADInterfaceEntry.setStatus("current")
_HwTADInterfaceIndex_Type = InterfaceIndex
_HwTADInterfaceIndex_Object = MibTableColumn
hwTADInterfaceIndex = _HwTADInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 1),
    _HwTADInterfaceIndex_Type()
)
hwTADInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTADInterfaceIndex.setStatus("current")


class _HwTADFilterEnable_Type(HWEnableValue):
    """Custom type hwTADFilterEnable based on HWEnableValue"""


_HwTADFilterEnable_Object = MibTableColumn
hwTADFilterEnable = _HwTADFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 2),
    _HwTADFilterEnable_Type()
)
hwTADFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADFilterEnable.setStatus("current")


class _HwTADFilterExpireTime_Type(Integer32):
    """Custom type hwTADFilterExpireTime based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 10000),
    )


_HwTADFilterExpireTime_Type.__name__ = "Integer32"
_HwTADFilterExpireTime_Object = MibTableColumn
hwTADFilterExpireTime = _HwTADFilterExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 3),
    _HwTADFilterExpireTime_Type()
)
hwTADFilterExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADFilterExpireTime.setStatus("current")


class _HwTADDampingEnable_Type(HWEnableValue):
    """Custom type hwTADDampingEnable based on HWEnableValue"""


_HwTADDampingEnable_Object = MibTableColumn
hwTADDampingEnable = _HwTADDampingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 4),
    _HwTADDampingEnable_Type()
)
hwTADDampingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADDampingEnable.setStatus("current")


class _HwTADSuppress_Type(Integer32):
    """Custom type hwTADSuppress based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 19999),
    )


_HwTADSuppress_Type.__name__ = "Integer32"
_HwTADSuppress_Object = MibTableColumn
hwTADSuppress = _HwTADSuppress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 5),
    _HwTADSuppress_Type()
)
hwTADSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADSuppress.setStatus("current")


class _HwTADCeiling_Type(Integer32):
    """Custom type hwTADCeiling based on Integer32"""
    defaultValue = 6000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 20000),
    )


_HwTADCeiling_Type.__name__ = "Integer32"
_HwTADCeiling_Object = MibTableColumn
hwTADCeiling = _HwTADCeiling_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 6),
    _HwTADCeiling_Type()
)
hwTADCeiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADCeiling.setStatus("current")


class _HwTADReuse_Type(Integer32):
    """Custom type hwTADReuse based on Integer32"""
    defaultValue = 750

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19998),
    )


_HwTADReuse_Type.__name__ = "Integer32"
_HwTADReuse_Object = MibTableColumn
hwTADReuse = _HwTADReuse_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 7),
    _HwTADReuse_Type()
)
hwTADReuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADReuse.setStatus("current")


class _HwTADDecayOk_Type(Integer32):
    """Custom type hwTADDecayOk based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_HwTADDecayOk_Type.__name__ = "Integer32"
_HwTADDecayOk_Object = MibTableColumn
hwTADDecayOk = _HwTADDecayOk_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 8),
    _HwTADDecayOk_Type()
)
hwTADDecayOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADDecayOk.setStatus("current")


class _HwTADDecayNg_Type(Integer32):
    """Custom type hwTADDecayNg based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_HwTADDecayNg_Type.__name__ = "Integer32"
_HwTADDecayNg_Object = MibTableColumn
hwTADDecayNg = _HwTADDecayNg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 9),
    _HwTADDecayNg_Type()
)
hwTADDecayNg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADDecayNg.setStatus("current")


class _HwTADResetStatistics_Type(Integer32):
    """Custom type hwTADResetStatistics based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unreset", 2))
    )


_HwTADResetStatistics_Type.__name__ = "Integer32"
_HwTADResetStatistics_Object = MibTableColumn
hwTADResetStatistics = _HwTADResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 10),
    _HwTADResetStatistics_Type()
)
hwTADResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADResetStatistics.setStatus("current")
_HwTADResetTime_Type = DateAndTime
_HwTADResetTime_Object = MibTableColumn
hwTADResetTime = _HwTADResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 11),
    _HwTADResetTime_Type()
)
hwTADResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTADResetTime.setStatus("current")


class _HwTADB3tcaThreshold_Type(Integer32):
    """Custom type hwTADB3tcaThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_HwTADB3tcaThreshold_Type.__name__ = "Integer32"
_HwTADB3tcaThreshold_Object = MibTableColumn
hwTADB3tcaThreshold = _HwTADB3tcaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 12),
    _HwTADB3tcaThreshold_Type()
)
hwTADB3tcaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADB3tcaThreshold.setStatus("current")


class _HwTADSdbereThreshold_Type(Integer32):
    """Custom type hwTADSdbereThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_HwTADSdbereThreshold_Type.__name__ = "Integer32"
_HwTADSdbereThreshold_Object = MibTableColumn
hwTADSdbereThreshold = _HwTADSdbereThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 13),
    _HwTADSdbereThreshold_Type()
)
hwTADSdbereThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADSdbereThreshold.setStatus("current")


class _HwTADSfbereThreshold_Type(Integer32):
    """Custom type hwTADSfbereThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_HwTADSfbereThreshold_Type.__name__ = "Integer32"
_HwTADSfbereThreshold_Object = MibTableColumn
hwTADSfbereThreshold = _HwTADSfbereThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 1, 1, 14),
    _HwTADSfbereThreshold_Type()
)
hwTADSfbereThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADSfbereThreshold.setStatus("current")
_HwTADAlarmTable_Object = MibTable
hwTADAlarmTable = _HwTADAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2)
)
if mibBuilder.loadTexts:
    hwTADAlarmTable.setStatus("current")
_HwTADAlarmEntry_Object = MibTableRow
hwTADAlarmEntry = _HwTADAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1)
)
hwTADAlarmEntry.setIndexNames(
    (0, "HUAWEI-TAD-MIB", "hwTADAlarmIfIndex"),
    (0, "HUAWEI-TAD-MIB", "hwTADAlarmType"),
)
if mibBuilder.loadTexts:
    hwTADAlarmEntry.setStatus("current")
_HwTADAlarmIfIndex_Type = InterfaceIndex
_HwTADAlarmIfIndex_Object = MibTableColumn
hwTADAlarmIfIndex = _HwTADAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1, 1),
    _HwTADAlarmIfIndex_Type()
)
hwTADAlarmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTADAlarmIfIndex.setStatus("current")


class _HwTADAlarmType_Type(Integer32):
    """Custom type hwTADAlarmType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("auais", 1),
          ("b3tca", 2),
          ("lais", 3),
          ("lcd", 21),
          ("lof", 4),
          ("lom", 5),
          ("lop", 6),
          ("los", 7),
          ("lrdi", 8),
          ("lrei", 9),
          ("oof", 10),
          ("pais", 11),
          ("pplm", 14),
          ("prdi", 12),
          ("prei", 13),
          ("puneq", 20),
          ("rdool", 15),
          ("rrool", 16),
          ("sdbere", 17),
          ("sfbere", 18),
          ("trool", 19),
          ("wlnk", 22))
    )


_HwTADAlarmType_Type.__name__ = "Integer32"
_HwTADAlarmType_Object = MibTableColumn
hwTADAlarmType = _HwTADAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1, 2),
    _HwTADAlarmType_Type()
)
hwTADAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTADAlarmType.setStatus("current")
_HwTADAlarmIfDown_Type = HWEnableValue
_HwTADAlarmIfDown_Object = MibTableColumn
hwTADAlarmIfDown = _HwTADAlarmIfDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1, 3),
    _HwTADAlarmIfDown_Type()
)
hwTADAlarmIfDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADAlarmIfDown.setStatus("current")


class _HwTADAlarmLog_Type(HWEnableValue):
    """Custom type hwTADAlarmLog based on HWEnableValue"""


_HwTADAlarmLog_Object = MibTableColumn
hwTADAlarmLog = _HwTADAlarmLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1, 4),
    _HwTADAlarmLog_Type()
)
hwTADAlarmLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTADAlarmLog.setStatus("current")


class _HwTADAlarmStatus_Type(Integer32):
    """Custom type hwTADAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwTADAlarmStatus_Type.__name__ = "Integer32"
_HwTADAlarmStatus_Object = MibTableColumn
hwTADAlarmStatus = _HwTADAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1, 5),
    _HwTADAlarmStatus_Type()
)
hwTADAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTADAlarmStatus.setStatus("current")


class _HwTADAlarmInFilter_Type(Integer32):
    """Custom type hwTADAlarmInFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_HwTADAlarmInFilter_Type.__name__ = "Integer32"
_HwTADAlarmInFilter_Object = MibTableColumn
hwTADAlarmInFilter = _HwTADAlarmInFilter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1, 6),
    _HwTADAlarmInFilter_Type()
)
hwTADAlarmInFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTADAlarmInFilter.setStatus("current")
_HwTADAlarmFigure_Type = DisplayString
_HwTADAlarmFigure_Object = MibTableColumn
hwTADAlarmFigure = _HwTADAlarmFigure_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1, 7),
    _HwTADAlarmFigure_Type()
)
hwTADAlarmFigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTADAlarmFigure.setStatus("current")


class _HwTADAlarmInSuppress_Type(Integer32):
    """Custom type hwTADAlarmInSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("suppressed", 1),
          ("unsuppressed", 2))
    )


_HwTADAlarmInSuppress_Type.__name__ = "Integer32"
_HwTADAlarmInSuppress_Object = MibTableColumn
hwTADAlarmInSuppress = _HwTADAlarmInSuppress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1, 8),
    _HwTADAlarmInSuppress_Type()
)
hwTADAlarmInSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTADAlarmInSuppress.setStatus("current")
_HwTADAlarmFlappingCount_Type = Counter32
_HwTADAlarmFlappingCount_Object = MibTableColumn
hwTADAlarmFlappingCount = _HwTADAlarmFlappingCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1, 9),
    _HwTADAlarmFlappingCount_Type()
)
hwTADAlarmFlappingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTADAlarmFlappingCount.setStatus("current")
_HwTADAlarmSuppressCount_Type = Counter32
_HwTADAlarmSuppressCount_Object = MibTableColumn
hwTADAlarmSuppressCount = _HwTADAlarmSuppressCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 1, 2, 1, 10),
    _HwTADAlarmSuppressCount_Type()
)
hwTADAlarmSuppressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTADAlarmSuppressCount.setStatus("current")
_HwTADConformance_ObjectIdentity = ObjectIdentity
hwTADConformance = _HwTADConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 2)
)
_HwTADGroups_ObjectIdentity = ObjectIdentity
hwTADGroups = _HwTADGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 2, 1)
)

# Managed Objects groups

hwTADInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 2, 1, 1)
)
hwTADInterfaceGroup.setObjects(
      *(("HUAWEI-TAD-MIB", "hwTADFilterEnable"),
        ("HUAWEI-TAD-MIB", "hwTADFilterExpireTime"),
        ("HUAWEI-TAD-MIB", "hwTADDampingEnable"),
        ("HUAWEI-TAD-MIB", "hwTADSuppress"),
        ("HUAWEI-TAD-MIB", "hwTADCeiling"),
        ("HUAWEI-TAD-MIB", "hwTADReuse"),
        ("HUAWEI-TAD-MIB", "hwTADDecayOk"),
        ("HUAWEI-TAD-MIB", "hwTADDecayNg"),
        ("HUAWEI-TAD-MIB", "hwTADResetStatistics"),
        ("HUAWEI-TAD-MIB", "hwTADResetTime"),
        ("HUAWEI-TAD-MIB", "hwTADB3tcaThreshold"),
        ("HUAWEI-TAD-MIB", "hwTADSdbereThreshold"),
        ("HUAWEI-TAD-MIB", "hwTADSfbereThreshold"))
)
if mibBuilder.loadTexts:
    hwTADInterfaceGroup.setStatus("current")

hwTADAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 128, 2, 1, 2)
)
hwTADAlarmGroup.setObjects(
      *(("HUAWEI-TAD-MIB", "hwTADAlarmIfDown"),
        ("HUAWEI-TAD-MIB", "hwTADAlarmLog"),
        ("HUAWEI-TAD-MIB", "hwTADAlarmStatus"),
        ("HUAWEI-TAD-MIB", "hwTADAlarmInFilter"),
        ("HUAWEI-TAD-MIB", "hwTADAlarmFigure"),
        ("HUAWEI-TAD-MIB", "hwTADAlarmInSuppress"),
        ("HUAWEI-TAD-MIB", "hwTADAlarmFlappingCount"),
        ("HUAWEI-TAD-MIB", "hwTADAlarmSuppressCount"))
)
if mibBuilder.loadTexts:
    hwTADAlarmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TAD-MIB",
    **{"HWEnableValue": HWEnableValue,
       "hwTAD": hwTAD,
       "hwTADObjects": hwTADObjects,
       "hwTADInterfaceTable": hwTADInterfaceTable,
       "hwTADInterfaceEntry": hwTADInterfaceEntry,
       "hwTADInterfaceIndex": hwTADInterfaceIndex,
       "hwTADFilterEnable": hwTADFilterEnable,
       "hwTADFilterExpireTime": hwTADFilterExpireTime,
       "hwTADDampingEnable": hwTADDampingEnable,
       "hwTADSuppress": hwTADSuppress,
       "hwTADCeiling": hwTADCeiling,
       "hwTADReuse": hwTADReuse,
       "hwTADDecayOk": hwTADDecayOk,
       "hwTADDecayNg": hwTADDecayNg,
       "hwTADResetStatistics": hwTADResetStatistics,
       "hwTADResetTime": hwTADResetTime,
       "hwTADB3tcaThreshold": hwTADB3tcaThreshold,
       "hwTADSdbereThreshold": hwTADSdbereThreshold,
       "hwTADSfbereThreshold": hwTADSfbereThreshold,
       "hwTADAlarmTable": hwTADAlarmTable,
       "hwTADAlarmEntry": hwTADAlarmEntry,
       "hwTADAlarmIfIndex": hwTADAlarmIfIndex,
       "hwTADAlarmType": hwTADAlarmType,
       "hwTADAlarmIfDown": hwTADAlarmIfDown,
       "hwTADAlarmLog": hwTADAlarmLog,
       "hwTADAlarmStatus": hwTADAlarmStatus,
       "hwTADAlarmInFilter": hwTADAlarmInFilter,
       "hwTADAlarmFigure": hwTADAlarmFigure,
       "hwTADAlarmInSuppress": hwTADAlarmInSuppress,
       "hwTADAlarmFlappingCount": hwTADAlarmFlappingCount,
       "hwTADAlarmSuppressCount": hwTADAlarmSuppressCount,
       "hwTADConformance": hwTADConformance,
       "hwTADGroups": hwTADGroups,
       "hwTADInterfaceGroup": hwTADInterfaceGroup,
       "hwTADAlarmGroup": hwTADAlarmGroup}
)
