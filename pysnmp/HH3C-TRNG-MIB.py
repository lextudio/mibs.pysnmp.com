# SNMP MIB module (HH3C-TRNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-TRNG-MIB
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

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

hh3cTRNG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13)
)
hh3cTRNG.setRevisions(
        ("2003-04-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cTRNGMibObjects_ObjectIdentity = ObjectIdentity
hh3cTRNGMibObjects = _Hh3cTRNGMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1)
)
_Hh3cTrngCreateTimerangeTable_Object = MibTable
hh3cTrngCreateTimerangeTable = _Hh3cTrngCreateTimerangeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cTrngCreateTimerangeTable.setStatus("current")
_Hh3cTrngCreateTimerangeEntry_Object = MibTableRow
hh3cTrngCreateTimerangeEntry = _Hh3cTrngCreateTimerangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 1, 1)
)
hh3cTrngCreateTimerangeEntry.setIndexNames(
    (0, "HH3C-TRNG-MIB", "hh3cTrngIndex"),
)
if mibBuilder.loadTexts:
    hh3cTrngCreateTimerangeEntry.setStatus("current")


class _Hh3cTrngIndex_Type(Integer32):
    """Custom type hh3cTrngIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Hh3cTrngIndex_Type.__name__ = "Integer32"
_Hh3cTrngIndex_Object = MibTableColumn
hh3cTrngIndex = _Hh3cTrngIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 1, 1, 1),
    _Hh3cTrngIndex_Type()
)
hh3cTrngIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrngIndex.setStatus("current")


class _Hh3cTrngName_Type(OctetString):
    """Custom type hh3cTrngName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cTrngName_Type.__name__ = "OctetString"
_Hh3cTrngName_Object = MibTableColumn
hh3cTrngName = _Hh3cTrngName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 1, 1, 2),
    _Hh3cTrngName_Type()
)
hh3cTrngName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrngName.setStatus("current")
_Hh3cTrngValidFlag_Type = TruthValue
_Hh3cTrngValidFlag_Object = MibTableColumn
hh3cTrngValidFlag = _Hh3cTrngValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 1, 1, 3),
    _Hh3cTrngValidFlag_Type()
)
hh3cTrngValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTrngValidFlag.setStatus("current")
_Hh3cTrngCreateRowStatus_Type = RowStatus
_Hh3cTrngCreateRowStatus_Object = MibTableColumn
hh3cTrngCreateRowStatus = _Hh3cTrngCreateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 1, 1, 4),
    _Hh3cTrngCreateRowStatus_Type()
)
hh3cTrngCreateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrngCreateRowStatus.setStatus("current")
_Hh3cTrngAbsoluteTable_Object = MibTable
hh3cTrngAbsoluteTable = _Hh3cTrngAbsoluteTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cTrngAbsoluteTable.setStatus("current")
_Hh3cTrngAbsoluteEntry_Object = MibTableRow
hh3cTrngAbsoluteEntry = _Hh3cTrngAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 2, 1)
)
hh3cTrngAbsoluteEntry.setIndexNames(
    (0, "HH3C-TRNG-MIB", "hh3cTrngAbsoluteNameIndex"),
    (0, "HH3C-TRNG-MIB", "hh3cTrngAbsoluteSubIndex"),
)
if mibBuilder.loadTexts:
    hh3cTrngAbsoluteEntry.setStatus("current")


class _Hh3cTrngAbsoluteNameIndex_Type(Integer32):
    """Custom type hh3cTrngAbsoluteNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Hh3cTrngAbsoluteNameIndex_Type.__name__ = "Integer32"
_Hh3cTrngAbsoluteNameIndex_Object = MibTableColumn
hh3cTrngAbsoluteNameIndex = _Hh3cTrngAbsoluteNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 2, 1, 1),
    _Hh3cTrngAbsoluteNameIndex_Type()
)
hh3cTrngAbsoluteNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrngAbsoluteNameIndex.setStatus("current")


class _Hh3cTrngAbsoluteSubIndex_Type(Integer32):
    """Custom type hh3cTrngAbsoluteSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Hh3cTrngAbsoluteSubIndex_Type.__name__ = "Integer32"
_Hh3cTrngAbsoluteSubIndex_Object = MibTableColumn
hh3cTrngAbsoluteSubIndex = _Hh3cTrngAbsoluteSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 2, 1, 2),
    _Hh3cTrngAbsoluteSubIndex_Type()
)
hh3cTrngAbsoluteSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrngAbsoluteSubIndex.setStatus("current")
_Hh3cTimerangeAbsoluteStartTime_Type = DateAndTime
_Hh3cTimerangeAbsoluteStartTime_Object = MibTableColumn
hh3cTimerangeAbsoluteStartTime = _Hh3cTimerangeAbsoluteStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 2, 1, 3),
    _Hh3cTimerangeAbsoluteStartTime_Type()
)
hh3cTimerangeAbsoluteStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTimerangeAbsoluteStartTime.setStatus("current")
_Hh3cTimerangeAbsoluteEndTime_Type = DateAndTime
_Hh3cTimerangeAbsoluteEndTime_Object = MibTableColumn
hh3cTimerangeAbsoluteEndTime = _Hh3cTimerangeAbsoluteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 2, 1, 4),
    _Hh3cTimerangeAbsoluteEndTime_Type()
)
hh3cTimerangeAbsoluteEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTimerangeAbsoluteEndTime.setStatus("current")
_Hh3cTimerangeAbsolueRowStatus_Type = RowStatus
_Hh3cTimerangeAbsolueRowStatus_Object = MibTableColumn
hh3cTimerangeAbsolueRowStatus = _Hh3cTimerangeAbsolueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 2, 1, 5),
    _Hh3cTimerangeAbsolueRowStatus_Type()
)
hh3cTimerangeAbsolueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTimerangeAbsolueRowStatus.setStatus("current")
_Hh3cTrngPeriodicTable_Object = MibTable
hh3cTrngPeriodicTable = _Hh3cTrngPeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cTrngPeriodicTable.setStatus("current")
_Hh3cTrngPeriodicEntry_Object = MibTableRow
hh3cTrngPeriodicEntry = _Hh3cTrngPeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 3, 1)
)
hh3cTrngPeriodicEntry.setIndexNames(
    (0, "HH3C-TRNG-MIB", "hh3cTrngPeriodicNameIndex"),
    (0, "HH3C-TRNG-MIB", "hh3cTrngPeriodicSubIndex"),
)
if mibBuilder.loadTexts:
    hh3cTrngPeriodicEntry.setStatus("current")


class _Hh3cTrngPeriodicNameIndex_Type(Integer32):
    """Custom type hh3cTrngPeriodicNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Hh3cTrngPeriodicNameIndex_Type.__name__ = "Integer32"
_Hh3cTrngPeriodicNameIndex_Object = MibTableColumn
hh3cTrngPeriodicNameIndex = _Hh3cTrngPeriodicNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 3, 1, 1),
    _Hh3cTrngPeriodicNameIndex_Type()
)
hh3cTrngPeriodicNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrngPeriodicNameIndex.setStatus("current")


class _Hh3cTrngPeriodicSubIndex_Type(Integer32):
    """Custom type hh3cTrngPeriodicSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hh3cTrngPeriodicSubIndex_Type.__name__ = "Integer32"
_Hh3cTrngPeriodicSubIndex_Object = MibTableColumn
hh3cTrngPeriodicSubIndex = _Hh3cTrngPeriodicSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 3, 1, 2),
    _Hh3cTrngPeriodicSubIndex_Type()
)
hh3cTrngPeriodicSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrngPeriodicSubIndex.setStatus("current")


class _Hh3cTrngPeriodicDayOfWeek_Type(Bits):
    """Custom type hh3cTrngPeriodicDayOfWeek based on Bits"""
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )

_Hh3cTrngPeriodicDayOfWeek_Type.__name__ = "Bits"
_Hh3cTrngPeriodicDayOfWeek_Object = MibTableColumn
hh3cTrngPeriodicDayOfWeek = _Hh3cTrngPeriodicDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 3, 1, 3),
    _Hh3cTrngPeriodicDayOfWeek_Type()
)
hh3cTrngPeriodicDayOfWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrngPeriodicDayOfWeek.setStatus("current")
_Hh3cTimerangePeriodicStartTime_Type = DateAndTime
_Hh3cTimerangePeriodicStartTime_Object = MibTableColumn
hh3cTimerangePeriodicStartTime = _Hh3cTimerangePeriodicStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 3, 1, 4),
    _Hh3cTimerangePeriodicStartTime_Type()
)
hh3cTimerangePeriodicStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTimerangePeriodicStartTime.setStatus("current")
_Hh3cTimerangePeriodicEndTime_Type = DateAndTime
_Hh3cTimerangePeriodicEndTime_Object = MibTableColumn
hh3cTimerangePeriodicEndTime = _Hh3cTimerangePeriodicEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 3, 1, 5),
    _Hh3cTimerangePeriodicEndTime_Type()
)
hh3cTimerangePeriodicEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTimerangePeriodicEndTime.setStatus("current")
_Hh3cTimerangePeriodicRowStatus_Type = RowStatus
_Hh3cTimerangePeriodicRowStatus_Object = MibTableColumn
hh3cTimerangePeriodicRowStatus = _Hh3cTimerangePeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 1, 3, 1, 6),
    _Hh3cTimerangePeriodicRowStatus_Type()
)
hh3cTimerangePeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTimerangePeriodicRowStatus.setStatus("current")
_Hh3cTRNGMibConformance_ObjectIdentity = ObjectIdentity
hh3cTRNGMibConformance = _Hh3cTRNGMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 3)
)
_Hh3cTRNGMibCompliances_ObjectIdentity = ObjectIdentity
hh3cTRNGMibCompliances = _Hh3cTRNGMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 3, 1)
)
_Hh3cTRNGMibGroups_ObjectIdentity = ObjectIdentity
hh3cTRNGMibGroups = _Hh3cTRNGMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 3, 2)
)

# Managed Objects groups

hh3cTRNGGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 3, 2, 1)
)
hh3cTRNGGroup.setObjects(
      *(("HH3C-TRNG-MIB", "hh3cTrngName"),
        ("HH3C-TRNG-MIB", "hh3cTrngValidFlag"),
        ("HH3C-TRNG-MIB", "hh3cTrngCreateRowStatus"),
        ("HH3C-TRNG-MIB", "hh3cTimerangeAbsoluteStartTime"),
        ("HH3C-TRNG-MIB", "hh3cTimerangeAbsoluteEndTime"),
        ("HH3C-TRNG-MIB", "hh3cTimerangeAbsolueRowStatus"),
        ("HH3C-TRNG-MIB", "hh3cTrngPeriodicDayOfWeek"),
        ("HH3C-TRNG-MIB", "hh3cTimerangePeriodicStartTime"),
        ("HH3C-TRNG-MIB", "hh3cTimerangePeriodicEndTime"),
        ("HH3C-TRNG-MIB", "hh3cTimerangePeriodicRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cTRNGGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cTRNGMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cTRNGMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-TRNG-MIB",
    **{"hh3cTRNG": hh3cTRNG,
       "hh3cTRNGMibObjects": hh3cTRNGMibObjects,
       "hh3cTrngCreateTimerangeTable": hh3cTrngCreateTimerangeTable,
       "hh3cTrngCreateTimerangeEntry": hh3cTrngCreateTimerangeEntry,
       "hh3cTrngIndex": hh3cTrngIndex,
       "hh3cTrngName": hh3cTrngName,
       "hh3cTrngValidFlag": hh3cTrngValidFlag,
       "hh3cTrngCreateRowStatus": hh3cTrngCreateRowStatus,
       "hh3cTrngAbsoluteTable": hh3cTrngAbsoluteTable,
       "hh3cTrngAbsoluteEntry": hh3cTrngAbsoluteEntry,
       "hh3cTrngAbsoluteNameIndex": hh3cTrngAbsoluteNameIndex,
       "hh3cTrngAbsoluteSubIndex": hh3cTrngAbsoluteSubIndex,
       "hh3cTimerangeAbsoluteStartTime": hh3cTimerangeAbsoluteStartTime,
       "hh3cTimerangeAbsoluteEndTime": hh3cTimerangeAbsoluteEndTime,
       "hh3cTimerangeAbsolueRowStatus": hh3cTimerangeAbsolueRowStatus,
       "hh3cTrngPeriodicTable": hh3cTrngPeriodicTable,
       "hh3cTrngPeriodicEntry": hh3cTrngPeriodicEntry,
       "hh3cTrngPeriodicNameIndex": hh3cTrngPeriodicNameIndex,
       "hh3cTrngPeriodicSubIndex": hh3cTrngPeriodicSubIndex,
       "hh3cTrngPeriodicDayOfWeek": hh3cTrngPeriodicDayOfWeek,
       "hh3cTimerangePeriodicStartTime": hh3cTimerangePeriodicStartTime,
       "hh3cTimerangePeriodicEndTime": hh3cTimerangePeriodicEndTime,
       "hh3cTimerangePeriodicRowStatus": hh3cTimerangePeriodicRowStatus,
       "hh3cTRNGMibConformance": hh3cTRNGMibConformance,
       "hh3cTRNGMibCompliances": hh3cTRNGMibCompliances,
       "hh3cTRNGMibCompliance": hh3cTRNGMibCompliance,
       "hh3cTRNGMibGroups": hh3cTRNGMibGroups,
       "hh3cTRNGGroup": hh3cTRNGGroup}
)
