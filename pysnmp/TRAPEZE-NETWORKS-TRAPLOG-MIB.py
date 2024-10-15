# SNMP MIB module (TRAPEZE-NETWORKS-TRAPLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-TRAPLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:40 2024
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzTraplogMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13)
)
trpzTraplogMib.setRevisions(
        ("2009-03-22 00:09",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzTraplogTrapOccurrenceIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TrpzTraplogTrapOccurrenceIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_TrpzTraplogMibObjects_ObjectIdentity = ObjectIdentity
trpzTraplogMibObjects = _TrpzTraplogMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1)
)
_TrpzTraplogGuideObjects_ObjectIdentity = ObjectIdentity
trpzTraplogGuideObjects = _TrpzTraplogGuideObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 2)
)
_TrpzTraplogOldestTrapIndex_Type = TrpzTraplogTrapOccurrenceIndexOrZero
_TrpzTraplogOldestTrapIndex_Object = MibScalar
trpzTraplogOldestTrapIndex = _TrpzTraplogOldestTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 2, 1),
    _TrpzTraplogOldestTrapIndex_Type()
)
trpzTraplogOldestTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogOldestTrapIndex.setStatus("current")
_TrpzTraplogNewestTrapIndex_Type = TrpzTraplogTrapOccurrenceIndexOrZero
_TrpzTraplogNewestTrapIndex_Object = MibScalar
trpzTraplogNewestTrapIndex = _TrpzTraplogNewestTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 2, 2),
    _TrpzTraplogNewestTrapIndex_Type()
)
trpzTraplogNewestTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogNewestTrapIndex.setStatus("current")
_TrpzTraplogNewestTrapTime_Type = TimeStamp
_TrpzTraplogNewestTrapTime_Object = MibScalar
trpzTraplogNewestTrapTime = _TrpzTraplogNewestTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 2, 3),
    _TrpzTraplogNewestTrapTime_Type()
)
trpzTraplogNewestTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogNewestTrapTime.setStatus("current")


class _TrpzTraplogNewestTrapDateAndTime_Type(DateAndTime):
    """Custom type trpzTraplogNewestTrapDateAndTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_TrpzTraplogNewestTrapDateAndTime_Object = MibScalar
trpzTraplogNewestTrapDateAndTime = _TrpzTraplogNewestTrapDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 2, 4),
    _TrpzTraplogNewestTrapDateAndTime_Type()
)
trpzTraplogNewestTrapDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogNewestTrapDateAndTime.setStatus("current")
_TrpzTraplogTrapTable_Object = MibTable
trpzTraplogTrapTable = _TrpzTraplogTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3)
)
if mibBuilder.loadTexts:
    trpzTraplogTrapTable.setStatus("current")
_TrpzTraplogTrapEntry_Object = MibTableRow
trpzTraplogTrapEntry = _TrpzTraplogTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1)
)
trpzTraplogTrapEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapIndex"),
)
if mibBuilder.loadTexts:
    trpzTraplogTrapEntry.setStatus("current")
_TrpzTraplogTrapIndex_Type = TrpzTraplogTrapOccurrenceIndex
_TrpzTraplogTrapIndex_Object = MibTableColumn
trpzTraplogTrapIndex = _TrpzTraplogTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1, 1),
    _TrpzTraplogTrapIndex_Type()
)
trpzTraplogTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzTraplogTrapIndex.setStatus("current")
_TrpzTraplogTrapTime_Type = TimeStamp
_TrpzTraplogTrapTime_Object = MibTableColumn
trpzTraplogTrapTime = _TrpzTraplogTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1, 2),
    _TrpzTraplogTrapTime_Type()
)
trpzTraplogTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogTrapTime.setStatus("current")
_TrpzTraplogTrapDateAndTime_Type = DateAndTime
_TrpzTraplogTrapDateAndTime_Object = MibTableColumn
trpzTraplogTrapDateAndTime = _TrpzTraplogTrapDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1, 3),
    _TrpzTraplogTrapDateAndTime_Type()
)
trpzTraplogTrapDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogTrapDateAndTime.setStatus("current")
_TrpzTraplogTrapNotificationID_Type = ObjectIdentifier
_TrpzTraplogTrapNotificationID_Object = MibTableColumn
trpzTraplogTrapNotificationID = _TrpzTraplogTrapNotificationID_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1, 4),
    _TrpzTraplogTrapNotificationID_Type()
)
trpzTraplogTrapNotificationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogTrapNotificationID.setStatus("current")


class _TrpzTraplogTrapNumVars_Type(Unsigned32):
    """Custom type trpzTraplogTrapNumVars based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TrpzTraplogTrapNumVars_Type.__name__ = "Unsigned32"
_TrpzTraplogTrapNumVars_Object = MibTableColumn
trpzTraplogTrapNumVars = _TrpzTraplogTrapNumVars_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1, 5),
    _TrpzTraplogTrapNumVars_Type()
)
trpzTraplogTrapNumVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogTrapNumVars.setStatus("current")
_TrpzTraplogVarTable_Object = MibTable
trpzTraplogVarTable = _TrpzTraplogVarTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4)
)
if mibBuilder.loadTexts:
    trpzTraplogVarTable.setStatus("current")
_TrpzTraplogVarEntry_Object = MibTableRow
trpzTraplogVarEntry = _TrpzTraplogVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1)
)
trpzTraplogVarEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarTrapIndex"),
    (0, "TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarIndex"),
)
if mibBuilder.loadTexts:
    trpzTraplogVarEntry.setStatus("current")
_TrpzTraplogVarTrapIndex_Type = TrpzTraplogTrapOccurrenceIndex
_TrpzTraplogVarTrapIndex_Object = MibTableColumn
trpzTraplogVarTrapIndex = _TrpzTraplogVarTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 1),
    _TrpzTraplogVarTrapIndex_Type()
)
trpzTraplogVarTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzTraplogVarTrapIndex.setStatus("current")


class _TrpzTraplogVarIndex_Type(Unsigned32):
    """Custom type trpzTraplogVarIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TrpzTraplogVarIndex_Type.__name__ = "Unsigned32"
_TrpzTraplogVarIndex_Object = MibTableColumn
trpzTraplogVarIndex = _TrpzTraplogVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 2),
    _TrpzTraplogVarIndex_Type()
)
trpzTraplogVarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzTraplogVarIndex.setStatus("current")
_TrpzTraplogVarID_Type = ObjectIdentifier
_TrpzTraplogVarID_Object = MibTableColumn
trpzTraplogVarID = _TrpzTraplogVarID_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 3),
    _TrpzTraplogVarID_Type()
)
trpzTraplogVarID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogVarID.setStatus("current")


class _TrpzTraplogVarValueType_Type(Integer32):
    """Custom type trpzTraplogVarValueType based on Integer32"""
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
        *(("counter32", 1),
          ("counter64", 8),
          ("integer32", 4),
          ("ipAddress", 5),
          ("objectId", 7),
          ("octetString", 6),
          ("timeTicks", 3),
          ("unsigned32", 2))
    )


_TrpzTraplogVarValueType_Type.__name__ = "Integer32"
_TrpzTraplogVarValueType_Object = MibTableColumn
trpzTraplogVarValueType = _TrpzTraplogVarValueType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 4),
    _TrpzTraplogVarValueType_Type()
)
trpzTraplogVarValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogVarValueType.setStatus("current")
_TrpzTraplogVarCounter32Val_Type = Counter32
_TrpzTraplogVarCounter32Val_Object = MibTableColumn
trpzTraplogVarCounter32Val = _TrpzTraplogVarCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 5),
    _TrpzTraplogVarCounter32Val_Type()
)
trpzTraplogVarCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogVarCounter32Val.setStatus("current")
_TrpzTraplogVarUnsigned32Val_Type = Unsigned32
_TrpzTraplogVarUnsigned32Val_Object = MibTableColumn
trpzTraplogVarUnsigned32Val = _TrpzTraplogVarUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 6),
    _TrpzTraplogVarUnsigned32Val_Type()
)
trpzTraplogVarUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogVarUnsigned32Val.setStatus("current")
_TrpzTraplogVarTimeTicksVal_Type = TimeTicks
_TrpzTraplogVarTimeTicksVal_Object = MibTableColumn
trpzTraplogVarTimeTicksVal = _TrpzTraplogVarTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 7),
    _TrpzTraplogVarTimeTicksVal_Type()
)
trpzTraplogVarTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogVarTimeTicksVal.setStatus("current")
_TrpzTraplogVarInteger32Val_Type = Integer32
_TrpzTraplogVarInteger32Val_Object = MibTableColumn
trpzTraplogVarInteger32Val = _TrpzTraplogVarInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 8),
    _TrpzTraplogVarInteger32Val_Type()
)
trpzTraplogVarInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogVarInteger32Val.setStatus("current")
_TrpzTraplogVarOctetStringVal_Type = OctetString
_TrpzTraplogVarOctetStringVal_Object = MibTableColumn
trpzTraplogVarOctetStringVal = _TrpzTraplogVarOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 9),
    _TrpzTraplogVarOctetStringVal_Type()
)
trpzTraplogVarOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogVarOctetStringVal.setStatus("current")
_TrpzTraplogVarIpAddressVal_Type = IpAddress
_TrpzTraplogVarIpAddressVal_Object = MibTableColumn
trpzTraplogVarIpAddressVal = _TrpzTraplogVarIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 10),
    _TrpzTraplogVarIpAddressVal_Type()
)
trpzTraplogVarIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogVarIpAddressVal.setStatus("current")
_TrpzTraplogVarOidVal_Type = ObjectIdentifier
_TrpzTraplogVarOidVal_Object = MibTableColumn
trpzTraplogVarOidVal = _TrpzTraplogVarOidVal_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 11),
    _TrpzTraplogVarOidVal_Type()
)
trpzTraplogVarOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogVarOidVal.setStatus("current")
_TrpzTraplogVarCounter64Val_Type = Counter64
_TrpzTraplogVarCounter64Val_Object = MibTableColumn
trpzTraplogVarCounter64Val = _TrpzTraplogVarCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 12),
    _TrpzTraplogVarCounter64Val_Type()
)
trpzTraplogVarCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzTraplogVarCounter64Val.setStatus("current")
_TrpzTraplogConformance_ObjectIdentity = ObjectIdentity
trpzTraplogConformance = _TrpzTraplogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 2)
)
_TrpzTraplogCompliances_ObjectIdentity = ObjectIdentity
trpzTraplogCompliances = _TrpzTraplogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 1)
)
_TrpzTraplogGroups_ObjectIdentity = ObjectIdentity
trpzTraplogGroups = _TrpzTraplogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2)
)

# Managed Objects groups

trpzTraplogGuideGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2, 1)
)
trpzTraplogGuideGroup.setObjects(
      *(("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogOldestTrapIndex"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogNewestTrapIndex"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogNewestTrapTime"))
)
if mibBuilder.loadTexts:
    trpzTraplogGuideGroup.setStatus("current")

trpzTraplogGuideDateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2, 2)
)
trpzTraplogGuideDateGroup.setObjects(
    ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogNewestTrapDateAndTime")
)
if mibBuilder.loadTexts:
    trpzTraplogGuideDateGroup.setStatus("current")

trpzTraplogTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2, 3)
)
trpzTraplogTrapGroup.setObjects(
      *(("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapTime"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapNotificationID"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapNumVars"))
)
if mibBuilder.loadTexts:
    trpzTraplogTrapGroup.setStatus("current")

trpzTraplogTrapDateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2, 4)
)
trpzTraplogTrapDateGroup.setObjects(
    ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapDateAndTime")
)
if mibBuilder.loadTexts:
    trpzTraplogTrapDateGroup.setStatus("current")

trpzTraplogVarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2, 5)
)
trpzTraplogVarGroup.setObjects(
      *(("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarID"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarValueType"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarCounter32Val"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarUnsigned32Val"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarTimeTicksVal"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarInteger32Val"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarOctetStringVal"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarIpAddressVal"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarOidVal"),
        ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarCounter64Val"))
)
if mibBuilder.loadTexts:
    trpzTraplogVarGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzTraplogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzTraplogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-TRAPLOG-MIB",
    **{"TrpzTraplogTrapOccurrenceIndex": TrpzTraplogTrapOccurrenceIndex,
       "TrpzTraplogTrapOccurrenceIndexOrZero": TrpzTraplogTrapOccurrenceIndexOrZero,
       "trpzTraplogMib": trpzTraplogMib,
       "trpzTraplogMibObjects": trpzTraplogMibObjects,
       "trpzTraplogGuideObjects": trpzTraplogGuideObjects,
       "trpzTraplogOldestTrapIndex": trpzTraplogOldestTrapIndex,
       "trpzTraplogNewestTrapIndex": trpzTraplogNewestTrapIndex,
       "trpzTraplogNewestTrapTime": trpzTraplogNewestTrapTime,
       "trpzTraplogNewestTrapDateAndTime": trpzTraplogNewestTrapDateAndTime,
       "trpzTraplogTrapTable": trpzTraplogTrapTable,
       "trpzTraplogTrapEntry": trpzTraplogTrapEntry,
       "trpzTraplogTrapIndex": trpzTraplogTrapIndex,
       "trpzTraplogTrapTime": trpzTraplogTrapTime,
       "trpzTraplogTrapDateAndTime": trpzTraplogTrapDateAndTime,
       "trpzTraplogTrapNotificationID": trpzTraplogTrapNotificationID,
       "trpzTraplogTrapNumVars": trpzTraplogTrapNumVars,
       "trpzTraplogVarTable": trpzTraplogVarTable,
       "trpzTraplogVarEntry": trpzTraplogVarEntry,
       "trpzTraplogVarTrapIndex": trpzTraplogVarTrapIndex,
       "trpzTraplogVarIndex": trpzTraplogVarIndex,
       "trpzTraplogVarID": trpzTraplogVarID,
       "trpzTraplogVarValueType": trpzTraplogVarValueType,
       "trpzTraplogVarCounter32Val": trpzTraplogVarCounter32Val,
       "trpzTraplogVarUnsigned32Val": trpzTraplogVarUnsigned32Val,
       "trpzTraplogVarTimeTicksVal": trpzTraplogVarTimeTicksVal,
       "trpzTraplogVarInteger32Val": trpzTraplogVarInteger32Val,
       "trpzTraplogVarOctetStringVal": trpzTraplogVarOctetStringVal,
       "trpzTraplogVarIpAddressVal": trpzTraplogVarIpAddressVal,
       "trpzTraplogVarOidVal": trpzTraplogVarOidVal,
       "trpzTraplogVarCounter64Val": trpzTraplogVarCounter64Val,
       "trpzTraplogConformance": trpzTraplogConformance,
       "trpzTraplogCompliances": trpzTraplogCompliances,
       "trpzTraplogCompliance": trpzTraplogCompliance,
       "trpzTraplogGroups": trpzTraplogGroups,
       "trpzTraplogGuideGroup": trpzTraplogGuideGroup,
       "trpzTraplogGuideDateGroup": trpzTraplogGuideDateGroup,
       "trpzTraplogTrapGroup": trpzTraplogTrapGroup,
       "trpzTraplogTrapDateGroup": trpzTraplogTrapDateGroup,
       "trpzTraplogVarGroup": trpzTraplogVarGroup}
)
