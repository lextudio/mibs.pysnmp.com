# SNMP MIB module (HPN-ICF-TRNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-TRNG-MIB
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

(hpnicfRhw,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw")

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

hpnicfTRNG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13)
)
hpnicfTRNG.setRevisions(
        ("2003-04-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfTRNGMibObjects_ObjectIdentity = ObjectIdentity
hpnicfTRNGMibObjects = _HpnicfTRNGMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1)
)
_HpnicfTrngCreateTimerangeTable_Object = MibTable
hpnicfTrngCreateTimerangeTable = _HpnicfTrngCreateTimerangeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfTrngCreateTimerangeTable.setStatus("current")
_HpnicfTrngCreateTimerangeEntry_Object = MibTableRow
hpnicfTrngCreateTimerangeEntry = _HpnicfTrngCreateTimerangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 1, 1)
)
hpnicfTrngCreateTimerangeEntry.setIndexNames(
    (0, "HPN-ICF-TRNG-MIB", "hpnicfTrngIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTrngCreateTimerangeEntry.setStatus("current")


class _HpnicfTrngIndex_Type(Integer32):
    """Custom type hpnicfTrngIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HpnicfTrngIndex_Type.__name__ = "Integer32"
_HpnicfTrngIndex_Object = MibTableColumn
hpnicfTrngIndex = _HpnicfTrngIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 1, 1, 1),
    _HpnicfTrngIndex_Type()
)
hpnicfTrngIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrngIndex.setStatus("current")


class _HpnicfTrngName_Type(OctetString):
    """Custom type hpnicfTrngName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfTrngName_Type.__name__ = "OctetString"
_HpnicfTrngName_Object = MibTableColumn
hpnicfTrngName = _HpnicfTrngName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 1, 1, 2),
    _HpnicfTrngName_Type()
)
hpnicfTrngName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrngName.setStatus("current")
_HpnicfTrngValidFlag_Type = TruthValue
_HpnicfTrngValidFlag_Object = MibTableColumn
hpnicfTrngValidFlag = _HpnicfTrngValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 1, 1, 3),
    _HpnicfTrngValidFlag_Type()
)
hpnicfTrngValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTrngValidFlag.setStatus("current")
_HpnicfTrngCreateRowStatus_Type = RowStatus
_HpnicfTrngCreateRowStatus_Object = MibTableColumn
hpnicfTrngCreateRowStatus = _HpnicfTrngCreateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 1, 1, 4),
    _HpnicfTrngCreateRowStatus_Type()
)
hpnicfTrngCreateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrngCreateRowStatus.setStatus("current")
_HpnicfTrngAbsoluteTable_Object = MibTable
hpnicfTrngAbsoluteTable = _HpnicfTrngAbsoluteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfTrngAbsoluteTable.setStatus("current")
_HpnicfTrngAbsoluteEntry_Object = MibTableRow
hpnicfTrngAbsoluteEntry = _HpnicfTrngAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 2, 1)
)
hpnicfTrngAbsoluteEntry.setIndexNames(
    (0, "HPN-ICF-TRNG-MIB", "hpnicfTrngAbsoluteNameIndex"),
    (0, "HPN-ICF-TRNG-MIB", "hpnicfTrngAbsoluteSubIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTrngAbsoluteEntry.setStatus("current")


class _HpnicfTrngAbsoluteNameIndex_Type(Integer32):
    """Custom type hpnicfTrngAbsoluteNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HpnicfTrngAbsoluteNameIndex_Type.__name__ = "Integer32"
_HpnicfTrngAbsoluteNameIndex_Object = MibTableColumn
hpnicfTrngAbsoluteNameIndex = _HpnicfTrngAbsoluteNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 2, 1, 1),
    _HpnicfTrngAbsoluteNameIndex_Type()
)
hpnicfTrngAbsoluteNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrngAbsoluteNameIndex.setStatus("current")


class _HpnicfTrngAbsoluteSubIndex_Type(Integer32):
    """Custom type hpnicfTrngAbsoluteSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HpnicfTrngAbsoluteSubIndex_Type.__name__ = "Integer32"
_HpnicfTrngAbsoluteSubIndex_Object = MibTableColumn
hpnicfTrngAbsoluteSubIndex = _HpnicfTrngAbsoluteSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 2, 1, 2),
    _HpnicfTrngAbsoluteSubIndex_Type()
)
hpnicfTrngAbsoluteSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrngAbsoluteSubIndex.setStatus("current")
_HpnicfTimerangeAbsoluteStartTime_Type = DateAndTime
_HpnicfTimerangeAbsoluteStartTime_Object = MibTableColumn
hpnicfTimerangeAbsoluteStartTime = _HpnicfTimerangeAbsoluteStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 2, 1, 3),
    _HpnicfTimerangeAbsoluteStartTime_Type()
)
hpnicfTimerangeAbsoluteStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTimerangeAbsoluteStartTime.setStatus("current")
_HpnicfTimerangeAbsoluteEndTime_Type = DateAndTime
_HpnicfTimerangeAbsoluteEndTime_Object = MibTableColumn
hpnicfTimerangeAbsoluteEndTime = _HpnicfTimerangeAbsoluteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 2, 1, 4),
    _HpnicfTimerangeAbsoluteEndTime_Type()
)
hpnicfTimerangeAbsoluteEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTimerangeAbsoluteEndTime.setStatus("current")
_HpnicfTimerangeAbsolueRowStatus_Type = RowStatus
_HpnicfTimerangeAbsolueRowStatus_Object = MibTableColumn
hpnicfTimerangeAbsolueRowStatus = _HpnicfTimerangeAbsolueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 2, 1, 5),
    _HpnicfTimerangeAbsolueRowStatus_Type()
)
hpnicfTimerangeAbsolueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTimerangeAbsolueRowStatus.setStatus("current")
_HpnicfTrngPeriodicTable_Object = MibTable
hpnicfTrngPeriodicTable = _HpnicfTrngPeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfTrngPeriodicTable.setStatus("current")
_HpnicfTrngPeriodicEntry_Object = MibTableRow
hpnicfTrngPeriodicEntry = _HpnicfTrngPeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 3, 1)
)
hpnicfTrngPeriodicEntry.setIndexNames(
    (0, "HPN-ICF-TRNG-MIB", "hpnicfTrngPeriodicNameIndex"),
    (0, "HPN-ICF-TRNG-MIB", "hpnicfTrngPeriodicSubIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTrngPeriodicEntry.setStatus("current")


class _HpnicfTrngPeriodicNameIndex_Type(Integer32):
    """Custom type hpnicfTrngPeriodicNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HpnicfTrngPeriodicNameIndex_Type.__name__ = "Integer32"
_HpnicfTrngPeriodicNameIndex_Object = MibTableColumn
hpnicfTrngPeriodicNameIndex = _HpnicfTrngPeriodicNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 3, 1, 1),
    _HpnicfTrngPeriodicNameIndex_Type()
)
hpnicfTrngPeriodicNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrngPeriodicNameIndex.setStatus("current")


class _HpnicfTrngPeriodicSubIndex_Type(Integer32):
    """Custom type hpnicfTrngPeriodicSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HpnicfTrngPeriodicSubIndex_Type.__name__ = "Integer32"
_HpnicfTrngPeriodicSubIndex_Object = MibTableColumn
hpnicfTrngPeriodicSubIndex = _HpnicfTrngPeriodicSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 3, 1, 2),
    _HpnicfTrngPeriodicSubIndex_Type()
)
hpnicfTrngPeriodicSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrngPeriodicSubIndex.setStatus("current")


class _HpnicfTrngPeriodicDayOfWeek_Type(Bits):
    """Custom type hpnicfTrngPeriodicDayOfWeek based on Bits"""
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )

_HpnicfTrngPeriodicDayOfWeek_Type.__name__ = "Bits"
_HpnicfTrngPeriodicDayOfWeek_Object = MibTableColumn
hpnicfTrngPeriodicDayOfWeek = _HpnicfTrngPeriodicDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 3, 1, 3),
    _HpnicfTrngPeriodicDayOfWeek_Type()
)
hpnicfTrngPeriodicDayOfWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrngPeriodicDayOfWeek.setStatus("current")
_HpnicfTimerangePeriodicStartTime_Type = DateAndTime
_HpnicfTimerangePeriodicStartTime_Object = MibTableColumn
hpnicfTimerangePeriodicStartTime = _HpnicfTimerangePeriodicStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 3, 1, 4),
    _HpnicfTimerangePeriodicStartTime_Type()
)
hpnicfTimerangePeriodicStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTimerangePeriodicStartTime.setStatus("current")
_HpnicfTimerangePeriodicEndTime_Type = DateAndTime
_HpnicfTimerangePeriodicEndTime_Object = MibTableColumn
hpnicfTimerangePeriodicEndTime = _HpnicfTimerangePeriodicEndTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 3, 1, 5),
    _HpnicfTimerangePeriodicEndTime_Type()
)
hpnicfTimerangePeriodicEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTimerangePeriodicEndTime.setStatus("current")
_HpnicfTimerangePeriodicRowStatus_Type = RowStatus
_HpnicfTimerangePeriodicRowStatus_Object = MibTableColumn
hpnicfTimerangePeriodicRowStatus = _HpnicfTimerangePeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 1, 3, 1, 6),
    _HpnicfTimerangePeriodicRowStatus_Type()
)
hpnicfTimerangePeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTimerangePeriodicRowStatus.setStatus("current")
_HpnicfTRNGMibConformance_ObjectIdentity = ObjectIdentity
hpnicfTRNGMibConformance = _HpnicfTRNGMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 3)
)
_HpnicfTRNGMibCompliances_ObjectIdentity = ObjectIdentity
hpnicfTRNGMibCompliances = _HpnicfTRNGMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 3, 1)
)
_HpnicfTRNGMibGroups_ObjectIdentity = ObjectIdentity
hpnicfTRNGMibGroups = _HpnicfTRNGMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 3, 2)
)

# Managed Objects groups

hpnicfTRNGGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 3, 2, 1)
)
hpnicfTRNGGroup.setObjects(
      *(("HPN-ICF-TRNG-MIB", "hpnicfTrngName"),
        ("HPN-ICF-TRNG-MIB", "hpnicfTrngValidFlag"),
        ("HPN-ICF-TRNG-MIB", "hpnicfTrngCreateRowStatus"),
        ("HPN-ICF-TRNG-MIB", "hpnicfTimerangeAbsoluteStartTime"),
        ("HPN-ICF-TRNG-MIB", "hpnicfTimerangeAbsoluteEndTime"),
        ("HPN-ICF-TRNG-MIB", "hpnicfTimerangeAbsolueRowStatus"),
        ("HPN-ICF-TRNG-MIB", "hpnicfTrngPeriodicDayOfWeek"),
        ("HPN-ICF-TRNG-MIB", "hpnicfTimerangePeriodicStartTime"),
        ("HPN-ICF-TRNG-MIB", "hpnicfTimerangePeriodicEndTime"),
        ("HPN-ICF-TRNG-MIB", "hpnicfTimerangePeriodicRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfTRNGGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfTRNGMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfTRNGMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-TRNG-MIB",
    **{"hpnicfTRNG": hpnicfTRNG,
       "hpnicfTRNGMibObjects": hpnicfTRNGMibObjects,
       "hpnicfTrngCreateTimerangeTable": hpnicfTrngCreateTimerangeTable,
       "hpnicfTrngCreateTimerangeEntry": hpnicfTrngCreateTimerangeEntry,
       "hpnicfTrngIndex": hpnicfTrngIndex,
       "hpnicfTrngName": hpnicfTrngName,
       "hpnicfTrngValidFlag": hpnicfTrngValidFlag,
       "hpnicfTrngCreateRowStatus": hpnicfTrngCreateRowStatus,
       "hpnicfTrngAbsoluteTable": hpnicfTrngAbsoluteTable,
       "hpnicfTrngAbsoluteEntry": hpnicfTrngAbsoluteEntry,
       "hpnicfTrngAbsoluteNameIndex": hpnicfTrngAbsoluteNameIndex,
       "hpnicfTrngAbsoluteSubIndex": hpnicfTrngAbsoluteSubIndex,
       "hpnicfTimerangeAbsoluteStartTime": hpnicfTimerangeAbsoluteStartTime,
       "hpnicfTimerangeAbsoluteEndTime": hpnicfTimerangeAbsoluteEndTime,
       "hpnicfTimerangeAbsolueRowStatus": hpnicfTimerangeAbsolueRowStatus,
       "hpnicfTrngPeriodicTable": hpnicfTrngPeriodicTable,
       "hpnicfTrngPeriodicEntry": hpnicfTrngPeriodicEntry,
       "hpnicfTrngPeriodicNameIndex": hpnicfTrngPeriodicNameIndex,
       "hpnicfTrngPeriodicSubIndex": hpnicfTrngPeriodicSubIndex,
       "hpnicfTrngPeriodicDayOfWeek": hpnicfTrngPeriodicDayOfWeek,
       "hpnicfTimerangePeriodicStartTime": hpnicfTimerangePeriodicStartTime,
       "hpnicfTimerangePeriodicEndTime": hpnicfTimerangePeriodicEndTime,
       "hpnicfTimerangePeriodicRowStatus": hpnicfTimerangePeriodicRowStatus,
       "hpnicfTRNGMibConformance": hpnicfTRNGMibConformance,
       "hpnicfTRNGMibCompliances": hpnicfTRNGMibCompliances,
       "hpnicfTRNGMibCompliance": hpnicfTRNGMibCompliance,
       "hpnicfTRNGMibGroups": hpnicfTRNGMibGroups,
       "hpnicfTRNGGroup": hpnicfTRNGGroup}
)
