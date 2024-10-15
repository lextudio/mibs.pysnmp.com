# SNMP MIB module (HPN-ICF-TRNG2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-TRNG2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:02 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfTRNG2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121)
)
hpnicfTRNG2.setRevisions(
        ("2013-03-08 00:00",
         "2012-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfTRNG2MibObjects_ObjectIdentity = ObjectIdentity
hpnicfTRNG2MibObjects = _HpnicfTRNG2MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1)
)
_HpnicfTrangeCreateTimerangeTable_Object = MibTable
hpnicfTrangeCreateTimerangeTable = _HpnicfTrangeCreateTimerangeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfTrangeCreateTimerangeTable.setStatus("current")
_HpnicfTrangeCreateTimerangeEntry_Object = MibTableRow
hpnicfTrangeCreateTimerangeEntry = _HpnicfTrangeCreateTimerangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 1, 1)
)
hpnicfTrangeCreateTimerangeEntry.setIndexNames(
    (0, "HPN-ICF-TRNG2-MIB", "hpnicfTrangeIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTrangeCreateTimerangeEntry.setStatus("current")


class _HpnicfTrangeIndex_Type(Integer32):
    """Custom type hpnicfTrangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfTrangeIndex_Type.__name__ = "Integer32"
_HpnicfTrangeIndex_Object = MibTableColumn
hpnicfTrangeIndex = _HpnicfTrangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 1, 1, 1),
    _HpnicfTrangeIndex_Type()
)
hpnicfTrangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrangeIndex.setStatus("current")


class _HpnicfTrangeName_Type(OctetString):
    """Custom type hpnicfTrangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfTrangeName_Type.__name__ = "OctetString"
_HpnicfTrangeName_Object = MibTableColumn
hpnicfTrangeName = _HpnicfTrangeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 1, 1, 2),
    _HpnicfTrangeName_Type()
)
hpnicfTrangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrangeName.setStatus("current")
_HpnicfTrangeValidFlag_Type = TruthValue
_HpnicfTrangeValidFlag_Object = MibTableColumn
hpnicfTrangeValidFlag = _HpnicfTrangeValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 1, 1, 3),
    _HpnicfTrangeValidFlag_Type()
)
hpnicfTrangeValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTrangeValidFlag.setStatus("current")
_HpnicfTrangeCreateRowStatus_Type = RowStatus
_HpnicfTrangeCreateRowStatus_Object = MibTableColumn
hpnicfTrangeCreateRowStatus = _HpnicfTrangeCreateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 1, 1, 4),
    _HpnicfTrangeCreateRowStatus_Type()
)
hpnicfTrangeCreateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrangeCreateRowStatus.setStatus("current")
_HpnicfTrangeAbsoluteTable_Object = MibTable
hpnicfTrangeAbsoluteTable = _HpnicfTrangeAbsoluteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfTrangeAbsoluteTable.setStatus("current")
_HpnicfTrangeAbsoluteEntry_Object = MibTableRow
hpnicfTrangeAbsoluteEntry = _HpnicfTrangeAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 2, 1)
)
hpnicfTrangeAbsoluteEntry.setIndexNames(
    (0, "HPN-ICF-TRNG2-MIB", "hpnicfTrangeAbsoluteNameIndex"),
    (0, "HPN-ICF-TRNG2-MIB", "hpnicfTrangeAbsoluteSubIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTrangeAbsoluteEntry.setStatus("current")


class _HpnicfTrangeAbsoluteNameIndex_Type(Integer32):
    """Custom type hpnicfTrangeAbsoluteNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfTrangeAbsoluteNameIndex_Type.__name__ = "Integer32"
_HpnicfTrangeAbsoluteNameIndex_Object = MibTableColumn
hpnicfTrangeAbsoluteNameIndex = _HpnicfTrangeAbsoluteNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 2, 1, 1),
    _HpnicfTrangeAbsoluteNameIndex_Type()
)
hpnicfTrangeAbsoluteNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrangeAbsoluteNameIndex.setStatus("current")


class _HpnicfTrangeAbsoluteSubIndex_Type(Integer32):
    """Custom type hpnicfTrangeAbsoluteSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HpnicfTrangeAbsoluteSubIndex_Type.__name__ = "Integer32"
_HpnicfTrangeAbsoluteSubIndex_Object = MibTableColumn
hpnicfTrangeAbsoluteSubIndex = _HpnicfTrangeAbsoluteSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 2, 1, 2),
    _HpnicfTrangeAbsoluteSubIndex_Type()
)
hpnicfTrangeAbsoluteSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrangeAbsoluteSubIndex.setStatus("current")
_HpnicfTrangeAbsoluteStartTime_Type = DateAndTime
_HpnicfTrangeAbsoluteStartTime_Object = MibTableColumn
hpnicfTrangeAbsoluteStartTime = _HpnicfTrangeAbsoluteStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 2, 1, 3),
    _HpnicfTrangeAbsoluteStartTime_Type()
)
hpnicfTrangeAbsoluteStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrangeAbsoluteStartTime.setStatus("current")
_HpnicfTrangeAbsoluteEndTime_Type = DateAndTime
_HpnicfTrangeAbsoluteEndTime_Object = MibTableColumn
hpnicfTrangeAbsoluteEndTime = _HpnicfTrangeAbsoluteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 2, 1, 4),
    _HpnicfTrangeAbsoluteEndTime_Type()
)
hpnicfTrangeAbsoluteEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrangeAbsoluteEndTime.setStatus("current")
_HpnicfTrangeAbsolueRowStatus_Type = RowStatus
_HpnicfTrangeAbsolueRowStatus_Object = MibTableColumn
hpnicfTrangeAbsolueRowStatus = _HpnicfTrangeAbsolueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 2, 1, 5),
    _HpnicfTrangeAbsolueRowStatus_Type()
)
hpnicfTrangeAbsolueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrangeAbsolueRowStatus.setStatus("current")
_HpnicfTrangePeriodicTable_Object = MibTable
hpnicfTrangePeriodicTable = _HpnicfTrangePeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfTrangePeriodicTable.setStatus("current")
_HpnicfTrangePeriodicEntry_Object = MibTableRow
hpnicfTrangePeriodicEntry = _HpnicfTrangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 3, 1)
)
hpnicfTrangePeriodicEntry.setIndexNames(
    (0, "HPN-ICF-TRNG2-MIB", "hpnicfTrangePeriodicNameIndex"),
    (0, "HPN-ICF-TRNG2-MIB", "hpnicfTrangePeriodicSubIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTrangePeriodicEntry.setStatus("current")


class _HpnicfTrangePeriodicNameIndex_Type(Integer32):
    """Custom type hpnicfTrangePeriodicNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfTrangePeriodicNameIndex_Type.__name__ = "Integer32"
_HpnicfTrangePeriodicNameIndex_Object = MibTableColumn
hpnicfTrangePeriodicNameIndex = _HpnicfTrangePeriodicNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 3, 1, 1),
    _HpnicfTrangePeriodicNameIndex_Type()
)
hpnicfTrangePeriodicNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrangePeriodicNameIndex.setStatus("current")


class _HpnicfTrangePeriodicSubIndex_Type(Integer32):
    """Custom type hpnicfTrangePeriodicSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HpnicfTrangePeriodicSubIndex_Type.__name__ = "Integer32"
_HpnicfTrangePeriodicSubIndex_Object = MibTableColumn
hpnicfTrangePeriodicSubIndex = _HpnicfTrangePeriodicSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 3, 1, 2),
    _HpnicfTrangePeriodicSubIndex_Type()
)
hpnicfTrangePeriodicSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrangePeriodicSubIndex.setStatus("current")


class _HpnicfTrangePeriodicDayOfWeek_Type(Bits):
    """Custom type hpnicfTrangePeriodicDayOfWeek based on Bits"""
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )

_HpnicfTrangePeriodicDayOfWeek_Type.__name__ = "Bits"
_HpnicfTrangePeriodicDayOfWeek_Object = MibTableColumn
hpnicfTrangePeriodicDayOfWeek = _HpnicfTrangePeriodicDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 3, 1, 3),
    _HpnicfTrangePeriodicDayOfWeek_Type()
)
hpnicfTrangePeriodicDayOfWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrangePeriodicDayOfWeek.setStatus("current")
_HpnicfTrangePeriodicStartTime_Type = DateAndTime
_HpnicfTrangePeriodicStartTime_Object = MibTableColumn
hpnicfTrangePeriodicStartTime = _HpnicfTrangePeriodicStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 3, 1, 4),
    _HpnicfTrangePeriodicStartTime_Type()
)
hpnicfTrangePeriodicStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrangePeriodicStartTime.setStatus("current")
_HpnicfTrangePeriodicEndTime_Type = DateAndTime
_HpnicfTrangePeriodicEndTime_Object = MibTableColumn
hpnicfTrangePeriodicEndTime = _HpnicfTrangePeriodicEndTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 3, 1, 5),
    _HpnicfTrangePeriodicEndTime_Type()
)
hpnicfTrangePeriodicEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrangePeriodicEndTime.setStatus("current")
_HpnicfTrangePeriodicRowStatus_Type = RowStatus
_HpnicfTrangePeriodicRowStatus_Object = MibTableColumn
hpnicfTrangePeriodicRowStatus = _HpnicfTrangePeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121, 1, 3, 1, 6),
    _HpnicfTrangePeriodicRowStatus_Type()
)
hpnicfTrangePeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrangePeriodicRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-TRNG2-MIB",
    **{"hpnicfTRNG2": hpnicfTRNG2,
       "hpnicfTRNG2MibObjects": hpnicfTRNG2MibObjects,
       "hpnicfTrangeCreateTimerangeTable": hpnicfTrangeCreateTimerangeTable,
       "hpnicfTrangeCreateTimerangeEntry": hpnicfTrangeCreateTimerangeEntry,
       "hpnicfTrangeIndex": hpnicfTrangeIndex,
       "hpnicfTrangeName": hpnicfTrangeName,
       "hpnicfTrangeValidFlag": hpnicfTrangeValidFlag,
       "hpnicfTrangeCreateRowStatus": hpnicfTrangeCreateRowStatus,
       "hpnicfTrangeAbsoluteTable": hpnicfTrangeAbsoluteTable,
       "hpnicfTrangeAbsoluteEntry": hpnicfTrangeAbsoluteEntry,
       "hpnicfTrangeAbsoluteNameIndex": hpnicfTrangeAbsoluteNameIndex,
       "hpnicfTrangeAbsoluteSubIndex": hpnicfTrangeAbsoluteSubIndex,
       "hpnicfTrangeAbsoluteStartTime": hpnicfTrangeAbsoluteStartTime,
       "hpnicfTrangeAbsoluteEndTime": hpnicfTrangeAbsoluteEndTime,
       "hpnicfTrangeAbsolueRowStatus": hpnicfTrangeAbsolueRowStatus,
       "hpnicfTrangePeriodicTable": hpnicfTrangePeriodicTable,
       "hpnicfTrangePeriodicEntry": hpnicfTrangePeriodicEntry,
       "hpnicfTrangePeriodicNameIndex": hpnicfTrangePeriodicNameIndex,
       "hpnicfTrangePeriodicSubIndex": hpnicfTrangePeriodicSubIndex,
       "hpnicfTrangePeriodicDayOfWeek": hpnicfTrangePeriodicDayOfWeek,
       "hpnicfTrangePeriodicStartTime": hpnicfTrangePeriodicStartTime,
       "hpnicfTrangePeriodicEndTime": hpnicfTrangePeriodicEndTime,
       "hpnicfTrangePeriodicRowStatus": hpnicfTrangePeriodicRowStatus}
)
