# SNMP MIB module (RBN-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:06 2024
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

(dsx3ConfigEntry,) = mibBuilder.importSymbols(
    "DS3-MIB",
    "dsx3ConfigEntry")

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

rbnDS3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38)
)
rbnDS3MIB.setRevisions(
        ("2005-05-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnDs3MIBObjects_ObjectIdentity = ObjectIdentity
rbnDs3MIBObjects = _RbnDs3MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38, 1)
)
_RbnDsx3ConfigTable_Object = MibTable
rbnDsx3ConfigTable = _RbnDsx3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1)
)
if mibBuilder.loadTexts:
    rbnDsx3ConfigTable.setStatus("current")
_RbnDsx3ConfigEntry_Object = MibTableRow
rbnDsx3ConfigEntry = _RbnDsx3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnDsx3ConfigEntry.setStatus("current")
_RbnDsx3AlarmSeverity_Type = RbnAlarmPerceivedSeverity
_RbnDsx3AlarmSeverity_Object = MibTableColumn
rbnDsx3AlarmSeverity = _RbnDsx3AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1, 1),
    _RbnDsx3AlarmSeverity_Type()
)
rbnDsx3AlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDsx3AlarmSeverity.setStatus("current")
_RbnDsx3AlarmServiceAffecting_Type = RbnAlarmServiceAffecting
_RbnDsx3AlarmServiceAffecting_Object = MibTableColumn
rbnDsx3AlarmServiceAffecting = _RbnDsx3AlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1, 2),
    _RbnDsx3AlarmServiceAffecting_Type()
)
rbnDsx3AlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDsx3AlarmServiceAffecting.setStatus("current")
_RbnDs3MIBConformance_ObjectIdentity = ObjectIdentity
rbnDs3MIBConformance = _RbnDs3MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38, 2)
)
_RbnDs3MIBGroups_ObjectIdentity = ObjectIdentity
rbnDs3MIBGroups = _RbnDs3MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 1)
)
_RbnDs3MIBCompliances_ObjectIdentity = ObjectIdentity
rbnDs3MIBCompliances = _RbnDs3MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 2)
)
dsx3ConfigEntry.registerAugmentions(
    ("RBN-DS3-MIB",
     "rbnDsx3ConfigEntry")
)
rbnDsx3ConfigEntry.setIndexNames(*dsx3ConfigEntry.getIndexNames())

# Managed Objects groups

rbnDs3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 1, 1)
)
rbnDs3Group.setObjects(
      *(("RBN-DS3-MIB", "rbnDsx3AlarmSeverity"),
        ("RBN-DS3-MIB", "rbnDsx3AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rbnDs3Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnDs3MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnDs3MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-DS3-MIB",
    **{"rbnDS3MIB": rbnDS3MIB,
       "rbnDs3MIBObjects": rbnDs3MIBObjects,
       "rbnDsx3ConfigTable": rbnDsx3ConfigTable,
       "rbnDsx3ConfigEntry": rbnDsx3ConfigEntry,
       "rbnDsx3AlarmSeverity": rbnDsx3AlarmSeverity,
       "rbnDsx3AlarmServiceAffecting": rbnDsx3AlarmServiceAffecting,
       "rbnDs3MIBConformance": rbnDs3MIBConformance,
       "rbnDs3MIBGroups": rbnDs3MIBGroups,
       "rbnDs3Group": rbnDs3Group,
       "rbnDs3MIBCompliances": rbnDs3MIBCompliances,
       "rbnDs3MIBCompliance": rbnDs3MIBCompliance}
)
