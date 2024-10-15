# SNMP MIB module (SYMMDATEANDTIME) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMDATEANDTIME
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:48 2024
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

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifNumber")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(symmClock,) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "symmClock")


# MODULE-IDENTITY

symmDateAndTime = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1)
)
symmDateAndTime.setRevisions(
        ("2011-07-18 13:17",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLatAndLon(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class TAntHeight(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TSsm(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_DateAndTimeStatus_ObjectIdentity = ObjectIdentity
dateAndTimeStatus = _DateAndTimeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1)
)
_SymmDateAndTimeTable_Object = MibTable
symmDateAndTimeTable = _SymmDateAndTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    symmDateAndTimeTable.setStatus("current")
_SymmDateAndTimeEntry_Object = MibTableRow
symmDateAndTimeEntry = _SymmDateAndTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 1, 1)
)
symmDateAndTimeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    symmDateAndTimeEntry.setStatus("current")
_SymmDateAndTimeInfo_Type = DisplayString
_SymmDateAndTimeInfo_Object = MibTableColumn
symmDateAndTimeInfo = _SymmDateAndTimeInfo_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 1, 1, 1),
    _SymmDateAndTimeInfo_Type()
)
symmDateAndTimeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symmDateAndTimeInfo.setStatus("current")
_SymmCurrentDateTime_Type = DisplayString
_SymmCurrentDateTime_Object = MibScalar
symmCurrentDateTime = _SymmCurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 2),
    _SymmCurrentDateTime_Type()
)
symmCurrentDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symmCurrentDateTime.setStatus("current")
_SymmLeapPendingAndSecond_Type = DisplayString
_SymmLeapPendingAndSecond_Object = MibScalar
symmLeapPendingAndSecond = _SymmLeapPendingAndSecond_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 1, 3),
    _SymmLeapPendingAndSecond_Type()
)
symmLeapPendingAndSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symmLeapPendingAndSecond.setStatus("current")
_DateAndTimeConfig_ObjectIdentity = ObjectIdentity
dateAndTimeConfig = _DateAndTimeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 2)
)
_SymmLeapSecondConfig_Type = Unsigned32
_SymmLeapSecondConfig_Object = MibScalar
symmLeapSecondConfig = _SymmLeapSecondConfig_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 2, 1),
    _SymmLeapSecondConfig_Type()
)
symmLeapSecondConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    symmLeapSecondConfig.setStatus("current")
if mibBuilder.loadTexts:
    symmLeapSecondConfig.setUnits("Second")
_SymmDateTimeConfig_Type = DisplayString
_SymmDateTimeConfig_Object = MibScalar
symmDateTimeConfig = _SymmDateTimeConfig_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 2, 2),
    _SymmDateTimeConfig_Type()
)
symmDateTimeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    symmDateTimeConfig.setStatus("current")
_DateAndTimeConformance_ObjectIdentity = ObjectIdentity
dateAndTimeConformance = _DateAndTimeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3)
)
if mibBuilder.loadTexts:
    dateAndTimeConformance.setStatus("current")
_DateAndTimeCompliances_ObjectIdentity = ObjectIdentity
dateAndTimeCompliances = _DateAndTimeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 1)
)
_DateAndTimeUocGroups_ObjectIdentity = ObjectIdentity
dateAndTimeUocGroups = _DateAndTimeUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 2)
)

# Managed Objects groups

dateTimeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 2, 1)
)
dateTimeStatusGroup.setObjects(
      *(("SYMMDATEANDTIME", "symmDateAndTimeInfo"),
        ("SYMMDATEANDTIME", "symmCurrentDateTime"),
        ("SYMMDATEANDTIME", "symmLeapPendingAndSecond"))
)
if mibBuilder.loadTexts:
    dateTimeStatusGroup.setStatus("current")

dateTimeConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 2, 2)
)
dateTimeConfigGroup.setObjects(
      *(("SYMMDATEANDTIME", "symmLeapSecondConfig"),
        ("SYMMDATEANDTIME", "symmDateTimeConfig"))
)
if mibBuilder.loadTexts:
    dateTimeConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dateTimeBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 3, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dateTimeBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMDATEANDTIME",
    **{"DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmDateAndTime": symmDateAndTime,
       "dateAndTimeStatus": dateAndTimeStatus,
       "symmDateAndTimeTable": symmDateAndTimeTable,
       "symmDateAndTimeEntry": symmDateAndTimeEntry,
       "symmDateAndTimeInfo": symmDateAndTimeInfo,
       "symmCurrentDateTime": symmCurrentDateTime,
       "symmLeapPendingAndSecond": symmLeapPendingAndSecond,
       "dateAndTimeConfig": dateAndTimeConfig,
       "symmLeapSecondConfig": symmLeapSecondConfig,
       "symmDateTimeConfig": symmDateTimeConfig,
       "dateAndTimeConformance": dateAndTimeConformance,
       "dateAndTimeCompliances": dateAndTimeCompliances,
       "dateTimeBasicCompliance": dateTimeBasicCompliance,
       "dateAndTimeUocGroups": dateAndTimeUocGroups,
       "dateTimeStatusGroup": dateTimeStatusGroup,
       "dateTimeConfigGroup": dateTimeConfigGroup}
)
