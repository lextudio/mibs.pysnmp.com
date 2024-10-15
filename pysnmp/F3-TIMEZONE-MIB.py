# SNMP MIB module (F3-TIMEZONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F3-TIMEZONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:32 2024
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

f3TimeZoneMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32)
)
f3TimeZoneMIB.setRevisions(
        ("2014-06-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MonthOfYear(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )



# MIB Managed Objects in the order of their OIDs

_F3TimeZoneConfigObjects_ObjectIdentity = ObjectIdentity
f3TimeZoneConfigObjects = _F3TimeZoneConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1)
)
_F3TimeZoneUtcOffset_Type = DisplayString
_F3TimeZoneUtcOffset_Object = MibScalar
f3TimeZoneUtcOffset = _F3TimeZoneUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 1),
    _F3TimeZoneUtcOffset_Type()
)
f3TimeZoneUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeZoneUtcOffset.setStatus("current")
_F3TimeZoneDstControlEnabled_Type = TruthValue
_F3TimeZoneDstControlEnabled_Object = MibScalar
f3TimeZoneDstControlEnabled = _F3TimeZoneDstControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 2),
    _F3TimeZoneDstControlEnabled_Type()
)
f3TimeZoneDstControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeZoneDstControlEnabled.setStatus("current")
_F3TimeZoneDstUtcOffset_Type = DisplayString
_F3TimeZoneDstUtcOffset_Object = MibScalar
f3TimeZoneDstUtcOffset = _F3TimeZoneDstUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 3),
    _F3TimeZoneDstUtcOffset_Type()
)
f3TimeZoneDstUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeZoneDstUtcOffset.setStatus("current")
_F3TimeZoneDstStartMonth_Type = MonthOfYear
_F3TimeZoneDstStartMonth_Object = MibScalar
f3TimeZoneDstStartMonth = _F3TimeZoneDstStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 4),
    _F3TimeZoneDstStartMonth_Type()
)
f3TimeZoneDstStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeZoneDstStartMonth.setStatus("current")
_F3TimeZoneDstStartDay_Type = DisplayString
_F3TimeZoneDstStartDay_Object = MibScalar
f3TimeZoneDstStartDay = _F3TimeZoneDstStartDay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 5),
    _F3TimeZoneDstStartDay_Type()
)
f3TimeZoneDstStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeZoneDstStartDay.setStatus("current")
_F3TimeZoneDstStartTime_Type = DisplayString
_F3TimeZoneDstStartTime_Object = MibScalar
f3TimeZoneDstStartTime = _F3TimeZoneDstStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 6),
    _F3TimeZoneDstStartTime_Type()
)
f3TimeZoneDstStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeZoneDstStartTime.setStatus("current")
_F3TimeZoneDstEndMonth_Type = MonthOfYear
_F3TimeZoneDstEndMonth_Object = MibScalar
f3TimeZoneDstEndMonth = _F3TimeZoneDstEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 7),
    _F3TimeZoneDstEndMonth_Type()
)
f3TimeZoneDstEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeZoneDstEndMonth.setStatus("current")
_F3TimeZoneDstEndDay_Type = DisplayString
_F3TimeZoneDstEndDay_Object = MibScalar
f3TimeZoneDstEndDay = _F3TimeZoneDstEndDay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 8),
    _F3TimeZoneDstEndDay_Type()
)
f3TimeZoneDstEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeZoneDstEndDay.setStatus("current")
_F3TimeZoneDstEndTime_Type = DisplayString
_F3TimeZoneDstEndTime_Object = MibScalar
f3TimeZoneDstEndTime = _F3TimeZoneDstEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 9),
    _F3TimeZoneDstEndTime_Type()
)
f3TimeZoneDstEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeZoneDstEndTime.setStatus("current")
_F3TimeZoneConformance_ObjectIdentity = ObjectIdentity
f3TimeZoneConformance = _F3TimeZoneConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2)
)
_F3TimeZoneCompliances_ObjectIdentity = ObjectIdentity
f3TimeZoneCompliances = _F3TimeZoneCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 1)
)
_F3TimeZoneGroups_ObjectIdentity = ObjectIdentity
f3TimeZoneGroups = _F3TimeZoneGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 2)
)

# Managed Objects groups

f3TimeZoneConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 2, 1)
)
f3TimeZoneConfigGroup.setObjects(
      *(("F3-TIMEZONE-MIB", "f3TimeZoneUtcOffset"),
        ("F3-TIMEZONE-MIB", "f3TimeZoneDstControlEnabled"),
        ("F3-TIMEZONE-MIB", "f3TimeZoneDstUtcOffset"),
        ("F3-TIMEZONE-MIB", "f3TimeZoneDstStartMonth"),
        ("F3-TIMEZONE-MIB", "f3TimeZoneDstStartDay"),
        ("F3-TIMEZONE-MIB", "f3TimeZoneDstStartTime"),
        ("F3-TIMEZONE-MIB", "f3TimeZoneDstEndMonth"),
        ("F3-TIMEZONE-MIB", "f3TimeZoneDstEndDay"),
        ("F3-TIMEZONE-MIB", "f3TimeZoneDstEndTime"))
)
if mibBuilder.loadTexts:
    f3TimeZoneConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3TimeZoneCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f3TimeZoneCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-TIMEZONE-MIB",
    **{"MonthOfYear": MonthOfYear,
       "f3TimeZoneMIB": f3TimeZoneMIB,
       "f3TimeZoneConfigObjects": f3TimeZoneConfigObjects,
       "f3TimeZoneUtcOffset": f3TimeZoneUtcOffset,
       "f3TimeZoneDstControlEnabled": f3TimeZoneDstControlEnabled,
       "f3TimeZoneDstUtcOffset": f3TimeZoneDstUtcOffset,
       "f3TimeZoneDstStartMonth": f3TimeZoneDstStartMonth,
       "f3TimeZoneDstStartDay": f3TimeZoneDstStartDay,
       "f3TimeZoneDstStartTime": f3TimeZoneDstStartTime,
       "f3TimeZoneDstEndMonth": f3TimeZoneDstEndMonth,
       "f3TimeZoneDstEndDay": f3TimeZoneDstEndDay,
       "f3TimeZoneDstEndTime": f3TimeZoneDstEndTime,
       "f3TimeZoneConformance": f3TimeZoneConformance,
       "f3TimeZoneCompliances": f3TimeZoneCompliances,
       "f3TimeZoneCompliance": f3TimeZoneCompliance,
       "f3TimeZoneGroups": f3TimeZoneGroups,
       "f3TimeZoneConfigGroup": f3TimeZoneConfigGroup}
)
