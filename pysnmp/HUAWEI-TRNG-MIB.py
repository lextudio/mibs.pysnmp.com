# SNMP MIB module (HUAWEI-TRNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TRNG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:16 2024
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

hwTRNG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13)
)
hwTRNG.setRevisions(
        ("2011-03-22 00:00",
         "2003-04-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwTRNGMibObjects_ObjectIdentity = ObjectIdentity
hwTRNGMibObjects = _HwTRNGMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1)
)
_HwTrngCreateTimerangeTable_Object = MibTable
hwTrngCreateTimerangeTable = _HwTrngCreateTimerangeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hwTrngCreateTimerangeTable.setStatus("current")
_HwTrngCreateTimerangeEntry_Object = MibTableRow
hwTrngCreateTimerangeEntry = _HwTrngCreateTimerangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 1, 1)
)
hwTrngCreateTimerangeEntry.setIndexNames(
    (0, "HUAWEI-TRNG-MIB", "hwTrngIndex"),
)
if mibBuilder.loadTexts:
    hwTrngCreateTimerangeEntry.setStatus("current")


class _HwTrngIndex_Type(Integer32):
    """Custom type hwTrngIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwTrngIndex_Type.__name__ = "Integer32"
_HwTrngIndex_Object = MibTableColumn
hwTrngIndex = _HwTrngIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 1, 1, 1),
    _HwTrngIndex_Type()
)
hwTrngIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTrngIndex.setStatus("current")


class _HwTrngName_Type(OctetString):
    """Custom type hwTrngName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwTrngName_Type.__name__ = "OctetString"
_HwTrngName_Object = MibTableColumn
hwTrngName = _HwTrngName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 1, 1, 2),
    _HwTrngName_Type()
)
hwTrngName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrngName.setStatus("current")
_HwTrngValidFlag_Type = TruthValue
_HwTrngValidFlag_Object = MibTableColumn
hwTrngValidFlag = _HwTrngValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 1, 1, 3),
    _HwTrngValidFlag_Type()
)
hwTrngValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTrngValidFlag.setStatus("current")
_HwTrngCreateRowStatus_Type = RowStatus
_HwTrngCreateRowStatus_Object = MibTableColumn
hwTrngCreateRowStatus = _HwTrngCreateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 1, 1, 4),
    _HwTrngCreateRowStatus_Type()
)
hwTrngCreateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrngCreateRowStatus.setStatus("current")
_HwTrngAbsoluteTable_Object = MibTable
hwTrngAbsoluteTable = _HwTrngAbsoluteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 2)
)
if mibBuilder.loadTexts:
    hwTrngAbsoluteTable.setStatus("current")
_HwTrngAbsoluteEntry_Object = MibTableRow
hwTrngAbsoluteEntry = _HwTrngAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 2, 1)
)
hwTrngAbsoluteEntry.setIndexNames(
    (0, "HUAWEI-TRNG-MIB", "hwTrngAbsoluteNameIndex"),
    (0, "HUAWEI-TRNG-MIB", "hwTrngAbsoluteSubIndex"),
)
if mibBuilder.loadTexts:
    hwTrngAbsoluteEntry.setStatus("current")


class _HwTrngAbsoluteNameIndex_Type(Integer32):
    """Custom type hwTrngAbsoluteNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwTrngAbsoluteNameIndex_Type.__name__ = "Integer32"
_HwTrngAbsoluteNameIndex_Object = MibTableColumn
hwTrngAbsoluteNameIndex = _HwTrngAbsoluteNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 2, 1, 1),
    _HwTrngAbsoluteNameIndex_Type()
)
hwTrngAbsoluteNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTrngAbsoluteNameIndex.setStatus("current")


class _HwTrngAbsoluteSubIndex_Type(Integer32):
    """Custom type hwTrngAbsoluteSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HwTrngAbsoluteSubIndex_Type.__name__ = "Integer32"
_HwTrngAbsoluteSubIndex_Object = MibTableColumn
hwTrngAbsoluteSubIndex = _HwTrngAbsoluteSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 2, 1, 2),
    _HwTrngAbsoluteSubIndex_Type()
)
hwTrngAbsoluteSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTrngAbsoluteSubIndex.setStatus("current")
_HwTimerangeAbsoluteStartTime_Type = DateAndTime
_HwTimerangeAbsoluteStartTime_Object = MibTableColumn
hwTimerangeAbsoluteStartTime = _HwTimerangeAbsoluteStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 2, 1, 3),
    _HwTimerangeAbsoluteStartTime_Type()
)
hwTimerangeAbsoluteStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTimerangeAbsoluteStartTime.setStatus("current")
_HwTimerangeAbsoluteEndTime_Type = DateAndTime
_HwTimerangeAbsoluteEndTime_Object = MibTableColumn
hwTimerangeAbsoluteEndTime = _HwTimerangeAbsoluteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 2, 1, 4),
    _HwTimerangeAbsoluteEndTime_Type()
)
hwTimerangeAbsoluteEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTimerangeAbsoluteEndTime.setStatus("current")
_HwTimerangeAbsolueRowStatus_Type = RowStatus
_HwTimerangeAbsolueRowStatus_Object = MibTableColumn
hwTimerangeAbsolueRowStatus = _HwTimerangeAbsolueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 2, 1, 5),
    _HwTimerangeAbsolueRowStatus_Type()
)
hwTimerangeAbsolueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTimerangeAbsolueRowStatus.setStatus("current")
_HwTrngPeriodicTable_Object = MibTable
hwTrngPeriodicTable = _HwTrngPeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 3)
)
if mibBuilder.loadTexts:
    hwTrngPeriodicTable.setStatus("current")
_HwTrngPeriodicEntry_Object = MibTableRow
hwTrngPeriodicEntry = _HwTrngPeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 3, 1)
)
hwTrngPeriodicEntry.setIndexNames(
    (0, "HUAWEI-TRNG-MIB", "hwTrngPeriodicNameIndex"),
    (0, "HUAWEI-TRNG-MIB", "hwTrngPeriodicSubIndex"),
)
if mibBuilder.loadTexts:
    hwTrngPeriodicEntry.setStatus("current")


class _HwTrngPeriodicNameIndex_Type(Integer32):
    """Custom type hwTrngPeriodicNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwTrngPeriodicNameIndex_Type.__name__ = "Integer32"
_HwTrngPeriodicNameIndex_Object = MibTableColumn
hwTrngPeriodicNameIndex = _HwTrngPeriodicNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 3, 1, 1),
    _HwTrngPeriodicNameIndex_Type()
)
hwTrngPeriodicNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTrngPeriodicNameIndex.setStatus("current")


class _HwTrngPeriodicSubIndex_Type(Integer32):
    """Custom type hwTrngPeriodicSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwTrngPeriodicSubIndex_Type.__name__ = "Integer32"
_HwTrngPeriodicSubIndex_Object = MibTableColumn
hwTrngPeriodicSubIndex = _HwTrngPeriodicSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 3, 1, 2),
    _HwTrngPeriodicSubIndex_Type()
)
hwTrngPeriodicSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTrngPeriodicSubIndex.setStatus("current")


class _HwTrngPeriodicDayofWeek_Type(Integer32):
    """Custom type hwTrngPeriodicDayofWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwTrngPeriodicDayofWeek_Type.__name__ = "Integer32"
_HwTrngPeriodicDayofWeek_Object = MibTableColumn
hwTrngPeriodicDayofWeek = _HwTrngPeriodicDayofWeek_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 3, 1, 3),
    _HwTrngPeriodicDayofWeek_Type()
)
hwTrngPeriodicDayofWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrngPeriodicDayofWeek.setStatus("current")
_HwTimerangePeriodicStartTime_Type = DateAndTime
_HwTimerangePeriodicStartTime_Object = MibTableColumn
hwTimerangePeriodicStartTime = _HwTimerangePeriodicStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 3, 1, 4),
    _HwTimerangePeriodicStartTime_Type()
)
hwTimerangePeriodicStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTimerangePeriodicStartTime.setStatus("current")
_HwTimerangePeriodicEndTime_Type = DateAndTime
_HwTimerangePeriodicEndTime_Object = MibTableColumn
hwTimerangePeriodicEndTime = _HwTimerangePeriodicEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 3, 1, 5),
    _HwTimerangePeriodicEndTime_Type()
)
hwTimerangePeriodicEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTimerangePeriodicEndTime.setStatus("current")
_HwTimerangePeriodicRowStatus_Type = RowStatus
_HwTimerangePeriodicRowStatus_Object = MibTableColumn
hwTimerangePeriodicRowStatus = _HwTimerangePeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 1, 3, 1, 6),
    _HwTimerangePeriodicRowStatus_Type()
)
hwTimerangePeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTimerangePeriodicRowStatus.setStatus("current")
_HwTRNGMibConformance_ObjectIdentity = ObjectIdentity
hwTRNGMibConformance = _HwTRNGMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 3)
)
_HwTRNGMibCompliances_ObjectIdentity = ObjectIdentity
hwTRNGMibCompliances = _HwTRNGMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 3, 1)
)
_HwTRNGMibGroups_ObjectIdentity = ObjectIdentity
hwTRNGMibGroups = _HwTRNGMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 3, 2)
)

# Managed Objects groups

hwTRNGGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 3, 2, 1)
)
hwTRNGGroup.setObjects(
      *(("HUAWEI-TRNG-MIB", "hwTrngName"),
        ("HUAWEI-TRNG-MIB", "hwTrngValidFlag"),
        ("HUAWEI-TRNG-MIB", "hwTrngCreateRowStatus"),
        ("HUAWEI-TRNG-MIB", "hwTimerangeAbsoluteStartTime"),
        ("HUAWEI-TRNG-MIB", "hwTimerangeAbsoluteEndTime"),
        ("HUAWEI-TRNG-MIB", "hwTimerangeAbsolueRowStatus"),
        ("HUAWEI-TRNG-MIB", "hwTrngPeriodicDayofWeek"),
        ("HUAWEI-TRNG-MIB", "hwTimerangePeriodicStartTime"),
        ("HUAWEI-TRNG-MIB", "hwTimerangePeriodicEndTime"),
        ("HUAWEI-TRNG-MIB", "hwTimerangePeriodicRowStatus"))
)
if mibBuilder.loadTexts:
    hwTRNGGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwTRNGMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 13, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwTRNGMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TRNG-MIB",
    **{"hwTRNG": hwTRNG,
       "hwTRNGMibObjects": hwTRNGMibObjects,
       "hwTrngCreateTimerangeTable": hwTrngCreateTimerangeTable,
       "hwTrngCreateTimerangeEntry": hwTrngCreateTimerangeEntry,
       "hwTrngIndex": hwTrngIndex,
       "hwTrngName": hwTrngName,
       "hwTrngValidFlag": hwTrngValidFlag,
       "hwTrngCreateRowStatus": hwTrngCreateRowStatus,
       "hwTrngAbsoluteTable": hwTrngAbsoluteTable,
       "hwTrngAbsoluteEntry": hwTrngAbsoluteEntry,
       "hwTrngAbsoluteNameIndex": hwTrngAbsoluteNameIndex,
       "hwTrngAbsoluteSubIndex": hwTrngAbsoluteSubIndex,
       "hwTimerangeAbsoluteStartTime": hwTimerangeAbsoluteStartTime,
       "hwTimerangeAbsoluteEndTime": hwTimerangeAbsoluteEndTime,
       "hwTimerangeAbsolueRowStatus": hwTimerangeAbsolueRowStatus,
       "hwTrngPeriodicTable": hwTrngPeriodicTable,
       "hwTrngPeriodicEntry": hwTrngPeriodicEntry,
       "hwTrngPeriodicNameIndex": hwTrngPeriodicNameIndex,
       "hwTrngPeriodicSubIndex": hwTrngPeriodicSubIndex,
       "hwTrngPeriodicDayofWeek": hwTrngPeriodicDayofWeek,
       "hwTimerangePeriodicStartTime": hwTimerangePeriodicStartTime,
       "hwTimerangePeriodicEndTime": hwTimerangePeriodicEndTime,
       "hwTimerangePeriodicRowStatus": hwTimerangePeriodicRowStatus,
       "hwTRNGMibConformance": hwTRNGMibConformance,
       "hwTRNGMibCompliances": hwTRNGMibCompliances,
       "hwTRNGMibCompliance": hwTRNGMibCompliance,
       "hwTRNGMibGroups": hwTRNGMibGroups,
       "hwTRNGGroup": hwTRNGGroup}
)
