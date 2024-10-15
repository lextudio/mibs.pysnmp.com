# SNMP MIB module (HH3C-TRNG2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-TRNG2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:08 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cTRNG2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121)
)
hh3cTRNG2.setRevisions(
        ("2013-03-08 00:00",
         "2012-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cTRNG2MibObjects_ObjectIdentity = ObjectIdentity
hh3cTRNG2MibObjects = _Hh3cTRNG2MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1)
)
_Hh3cTrangeCreateTimerangeTable_Object = MibTable
hh3cTrangeCreateTimerangeTable = _Hh3cTrangeCreateTimerangeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cTrangeCreateTimerangeTable.setStatus("current")
_Hh3cTrangeCreateTimerangeEntry_Object = MibTableRow
hh3cTrangeCreateTimerangeEntry = _Hh3cTrangeCreateTimerangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 1, 1)
)
hh3cTrangeCreateTimerangeEntry.setIndexNames(
    (0, "HH3C-TRNG2-MIB", "hh3cTrangeIndex"),
)
if mibBuilder.loadTexts:
    hh3cTrangeCreateTimerangeEntry.setStatus("current")


class _Hh3cTrangeIndex_Type(Integer32):
    """Custom type hh3cTrangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cTrangeIndex_Type.__name__ = "Integer32"
_Hh3cTrangeIndex_Object = MibTableColumn
hh3cTrangeIndex = _Hh3cTrangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 1, 1, 1),
    _Hh3cTrangeIndex_Type()
)
hh3cTrangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrangeIndex.setStatus("current")


class _Hh3cTrangeName_Type(OctetString):
    """Custom type hh3cTrangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cTrangeName_Type.__name__ = "OctetString"
_Hh3cTrangeName_Object = MibTableColumn
hh3cTrangeName = _Hh3cTrangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 1, 1, 2),
    _Hh3cTrangeName_Type()
)
hh3cTrangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrangeName.setStatus("current")
_Hh3cTrangeValidFlag_Type = TruthValue
_Hh3cTrangeValidFlag_Object = MibTableColumn
hh3cTrangeValidFlag = _Hh3cTrangeValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 1, 1, 3),
    _Hh3cTrangeValidFlag_Type()
)
hh3cTrangeValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTrangeValidFlag.setStatus("current")
_Hh3cTrangeCreateRowStatus_Type = RowStatus
_Hh3cTrangeCreateRowStatus_Object = MibTableColumn
hh3cTrangeCreateRowStatus = _Hh3cTrangeCreateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 1, 1, 4),
    _Hh3cTrangeCreateRowStatus_Type()
)
hh3cTrangeCreateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrangeCreateRowStatus.setStatus("current")
_Hh3cTrangeAbsoluteTable_Object = MibTable
hh3cTrangeAbsoluteTable = _Hh3cTrangeAbsoluteTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cTrangeAbsoluteTable.setStatus("current")
_Hh3cTrangeAbsoluteEntry_Object = MibTableRow
hh3cTrangeAbsoluteEntry = _Hh3cTrangeAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 2, 1)
)
hh3cTrangeAbsoluteEntry.setIndexNames(
    (0, "HH3C-TRNG2-MIB", "hh3cTrangeAbsoluteNameIndex"),
    (0, "HH3C-TRNG2-MIB", "hh3cTrangeAbsoluteSubIndex"),
)
if mibBuilder.loadTexts:
    hh3cTrangeAbsoluteEntry.setStatus("current")


class _Hh3cTrangeAbsoluteNameIndex_Type(Integer32):
    """Custom type hh3cTrangeAbsoluteNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cTrangeAbsoluteNameIndex_Type.__name__ = "Integer32"
_Hh3cTrangeAbsoluteNameIndex_Object = MibTableColumn
hh3cTrangeAbsoluteNameIndex = _Hh3cTrangeAbsoluteNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 2, 1, 1),
    _Hh3cTrangeAbsoluteNameIndex_Type()
)
hh3cTrangeAbsoluteNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrangeAbsoluteNameIndex.setStatus("current")


class _Hh3cTrangeAbsoluteSubIndex_Type(Integer32):
    """Custom type hh3cTrangeAbsoluteSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Hh3cTrangeAbsoluteSubIndex_Type.__name__ = "Integer32"
_Hh3cTrangeAbsoluteSubIndex_Object = MibTableColumn
hh3cTrangeAbsoluteSubIndex = _Hh3cTrangeAbsoluteSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 2, 1, 2),
    _Hh3cTrangeAbsoluteSubIndex_Type()
)
hh3cTrangeAbsoluteSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrangeAbsoluteSubIndex.setStatus("current")
_Hh3cTrangeAbsoluteStartTime_Type = DateAndTime
_Hh3cTrangeAbsoluteStartTime_Object = MibTableColumn
hh3cTrangeAbsoluteStartTime = _Hh3cTrangeAbsoluteStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 2, 1, 3),
    _Hh3cTrangeAbsoluteStartTime_Type()
)
hh3cTrangeAbsoluteStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrangeAbsoluteStartTime.setStatus("current")
_Hh3cTrangeAbsoluteEndTime_Type = DateAndTime
_Hh3cTrangeAbsoluteEndTime_Object = MibTableColumn
hh3cTrangeAbsoluteEndTime = _Hh3cTrangeAbsoluteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 2, 1, 4),
    _Hh3cTrangeAbsoluteEndTime_Type()
)
hh3cTrangeAbsoluteEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrangeAbsoluteEndTime.setStatus("current")
_Hh3cTrangeAbsolueRowStatus_Type = RowStatus
_Hh3cTrangeAbsolueRowStatus_Object = MibTableColumn
hh3cTrangeAbsolueRowStatus = _Hh3cTrangeAbsolueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 2, 1, 5),
    _Hh3cTrangeAbsolueRowStatus_Type()
)
hh3cTrangeAbsolueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrangeAbsolueRowStatus.setStatus("current")
_Hh3cTrangePeriodicTable_Object = MibTable
hh3cTrangePeriodicTable = _Hh3cTrangePeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cTrangePeriodicTable.setStatus("current")
_Hh3cTrangePeriodicEntry_Object = MibTableRow
hh3cTrangePeriodicEntry = _Hh3cTrangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 3, 1)
)
hh3cTrangePeriodicEntry.setIndexNames(
    (0, "HH3C-TRNG2-MIB", "hh3cTrangePeriodicNameIndex"),
    (0, "HH3C-TRNG2-MIB", "hh3cTrangePeriodicSubIndex"),
)
if mibBuilder.loadTexts:
    hh3cTrangePeriodicEntry.setStatus("current")


class _Hh3cTrangePeriodicNameIndex_Type(Integer32):
    """Custom type hh3cTrangePeriodicNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cTrangePeriodicNameIndex_Type.__name__ = "Integer32"
_Hh3cTrangePeriodicNameIndex_Object = MibTableColumn
hh3cTrangePeriodicNameIndex = _Hh3cTrangePeriodicNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 3, 1, 1),
    _Hh3cTrangePeriodicNameIndex_Type()
)
hh3cTrangePeriodicNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrangePeriodicNameIndex.setStatus("current")


class _Hh3cTrangePeriodicSubIndex_Type(Integer32):
    """Custom type hh3cTrangePeriodicSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hh3cTrangePeriodicSubIndex_Type.__name__ = "Integer32"
_Hh3cTrangePeriodicSubIndex_Object = MibTableColumn
hh3cTrangePeriodicSubIndex = _Hh3cTrangePeriodicSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 3, 1, 2),
    _Hh3cTrangePeriodicSubIndex_Type()
)
hh3cTrangePeriodicSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrangePeriodicSubIndex.setStatus("current")


class _Hh3cTrangePeriodicDayOfWeek_Type(Bits):
    """Custom type hh3cTrangePeriodicDayOfWeek based on Bits"""
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )

_Hh3cTrangePeriodicDayOfWeek_Type.__name__ = "Bits"
_Hh3cTrangePeriodicDayOfWeek_Object = MibTableColumn
hh3cTrangePeriodicDayOfWeek = _Hh3cTrangePeriodicDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 3, 1, 3),
    _Hh3cTrangePeriodicDayOfWeek_Type()
)
hh3cTrangePeriodicDayOfWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrangePeriodicDayOfWeek.setStatus("current")
_Hh3cTrangePeriodicStartTime_Type = DateAndTime
_Hh3cTrangePeriodicStartTime_Object = MibTableColumn
hh3cTrangePeriodicStartTime = _Hh3cTrangePeriodicStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 3, 1, 4),
    _Hh3cTrangePeriodicStartTime_Type()
)
hh3cTrangePeriodicStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrangePeriodicStartTime.setStatus("current")
_Hh3cTrangePeriodicEndTime_Type = DateAndTime
_Hh3cTrangePeriodicEndTime_Object = MibTableColumn
hh3cTrangePeriodicEndTime = _Hh3cTrangePeriodicEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 3, 1, 5),
    _Hh3cTrangePeriodicEndTime_Type()
)
hh3cTrangePeriodicEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrangePeriodicEndTime.setStatus("current")
_Hh3cTrangePeriodicRowStatus_Type = RowStatus
_Hh3cTrangePeriodicRowStatus_Object = MibTableColumn
hh3cTrangePeriodicRowStatus = _Hh3cTrangePeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121, 1, 3, 1, 6),
    _Hh3cTrangePeriodicRowStatus_Type()
)
hh3cTrangePeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrangePeriodicRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-TRNG2-MIB",
    **{"hh3cTRNG2": hh3cTRNG2,
       "hh3cTRNG2MibObjects": hh3cTRNG2MibObjects,
       "hh3cTrangeCreateTimerangeTable": hh3cTrangeCreateTimerangeTable,
       "hh3cTrangeCreateTimerangeEntry": hh3cTrangeCreateTimerangeEntry,
       "hh3cTrangeIndex": hh3cTrangeIndex,
       "hh3cTrangeName": hh3cTrangeName,
       "hh3cTrangeValidFlag": hh3cTrangeValidFlag,
       "hh3cTrangeCreateRowStatus": hh3cTrangeCreateRowStatus,
       "hh3cTrangeAbsoluteTable": hh3cTrangeAbsoluteTable,
       "hh3cTrangeAbsoluteEntry": hh3cTrangeAbsoluteEntry,
       "hh3cTrangeAbsoluteNameIndex": hh3cTrangeAbsoluteNameIndex,
       "hh3cTrangeAbsoluteSubIndex": hh3cTrangeAbsoluteSubIndex,
       "hh3cTrangeAbsoluteStartTime": hh3cTrangeAbsoluteStartTime,
       "hh3cTrangeAbsoluteEndTime": hh3cTrangeAbsoluteEndTime,
       "hh3cTrangeAbsolueRowStatus": hh3cTrangeAbsolueRowStatus,
       "hh3cTrangePeriodicTable": hh3cTrangePeriodicTable,
       "hh3cTrangePeriodicEntry": hh3cTrangePeriodicEntry,
       "hh3cTrangePeriodicNameIndex": hh3cTrangePeriodicNameIndex,
       "hh3cTrangePeriodicSubIndex": hh3cTrangePeriodicSubIndex,
       "hh3cTrangePeriodicDayOfWeek": hh3cTrangePeriodicDayOfWeek,
       "hh3cTrangePeriodicStartTime": hh3cTrangePeriodicStartTime,
       "hh3cTrangePeriodicEndTime": hh3cTrangePeriodicEndTime,
       "hh3cTrangePeriodicRowStatus": hh3cTrangePeriodicRowStatus}
)
