# SNMP MIB module (RBN-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:05 2024
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

(dsx1ConfigEntry,) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1ConfigEntry")

(RbnAlarmPerceivedSeverity,
 RbnAlarmServiceAffecting) = mibBuilder.importSymbols(
    "RBN-ALARM-TC",
    "RbnAlarmPerceivedSeverity",
    "RbnAlarmServiceAffecting")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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


# MODULE-IDENTITY

rbnDS1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37)
)
rbnDS1MIB.setRevisions(
        ("2005-05-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnDs1MIBObjects_ObjectIdentity = ObjectIdentity
rbnDs1MIBObjects = _RbnDs1MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37, 1)
)
_RbnDsx1ConfigTable_Object = MibTable
rbnDsx1ConfigTable = _RbnDsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1)
)
if mibBuilder.loadTexts:
    rbnDsx1ConfigTable.setStatus("current")
_RbnDsx1ConfigEntry_Object = MibTableRow
rbnDsx1ConfigEntry = _RbnDsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnDsx1ConfigEntry.setStatus("current")
_RbnDsx1AlarmSeverity_Type = RbnAlarmPerceivedSeverity
_RbnDsx1AlarmSeverity_Object = MibTableColumn
rbnDsx1AlarmSeverity = _RbnDsx1AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1, 1),
    _RbnDsx1AlarmSeverity_Type()
)
rbnDsx1AlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDsx1AlarmSeverity.setStatus("current")
_RbnDsx1AlarmServiceAffecting_Type = RbnAlarmServiceAffecting
_RbnDsx1AlarmServiceAffecting_Object = MibTableColumn
rbnDsx1AlarmServiceAffecting = _RbnDsx1AlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1, 2),
    _RbnDsx1AlarmServiceAffecting_Type()
)
rbnDsx1AlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDsx1AlarmServiceAffecting.setStatus("current")
_RbnDs1MIBConformance_ObjectIdentity = ObjectIdentity
rbnDs1MIBConformance = _RbnDs1MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37, 2)
)
_RbnDs1MIBGroups_ObjectIdentity = ObjectIdentity
rbnDs1MIBGroups = _RbnDs1MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 1)
)
_RbnDs1MIBCompliances_ObjectIdentity = ObjectIdentity
rbnDs1MIBCompliances = _RbnDs1MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 2)
)
dsx1ConfigEntry.registerAugmentions(
    ("RBN-DS1-MIB",
     "rbnDsx1ConfigEntry")
)
rbnDsx1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())

# Managed Objects groups

rbnDs1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 1, 1)
)
rbnDs1Group.setObjects(
      *(("RBN-DS1-MIB", "rbnDsx1AlarmSeverity"),
        ("RBN-DS1-MIB", "rbnDsx1AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rbnDs1Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnDs1MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnDs1MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-DS1-MIB",
    **{"rbnDS1MIB": rbnDS1MIB,
       "rbnDs1MIBObjects": rbnDs1MIBObjects,
       "rbnDsx1ConfigTable": rbnDsx1ConfigTable,
       "rbnDsx1ConfigEntry": rbnDsx1ConfigEntry,
       "rbnDsx1AlarmSeverity": rbnDsx1AlarmSeverity,
       "rbnDsx1AlarmServiceAffecting": rbnDsx1AlarmServiceAffecting,
       "rbnDs1MIBConformance": rbnDs1MIBConformance,
       "rbnDs1MIBGroups": rbnDs1MIBGroups,
       "rbnDs1Group": rbnDs1Group,
       "rbnDs1MIBCompliances": rbnDs1MIBCompliances,
       "rbnDs1MIBCompliance": rbnDs1MIBCompliance}
)
