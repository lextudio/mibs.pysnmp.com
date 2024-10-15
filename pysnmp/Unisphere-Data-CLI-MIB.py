# SNMP MIB module (Unisphere-Data-CLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-CLI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:27 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdLogSeverity,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdLogSeverity")


# MODULE-IDENTITY

usdCliMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30)
)
usdCliMIB.setRevisions(
        ("2000-09-26 13:50",
         "1999-12-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdCliTrap_ObjectIdentity = ObjectIdentity
usdCliTrap = _UsdCliTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0)
)
_UsdCliObjects_ObjectIdentity = ObjectIdentity
usdCliObjects = _UsdCliObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1)
)
_UsdCliGeneral_ObjectIdentity = ObjectIdentity
usdCliGeneral = _UsdCliGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1)
)
_UsdCliSecurityTrapEnable_Type = TruthValue
_UsdCliSecurityTrapEnable_Object = MibScalar
usdCliSecurityTrapEnable = _UsdCliSecurityTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1, 1),
    _UsdCliSecurityTrapEnable_Type()
)
usdCliSecurityTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdCliSecurityTrapEnable.setStatus("current")
_UsdCliSecurity_ObjectIdentity = ObjectIdentity
usdCliSecurity = _UsdCliSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2)
)
_UsdCliSecurityAlertPriority_Type = UsdLogSeverity
_UsdCliSecurityAlertPriority_Object = MibScalar
usdCliSecurityAlertPriority = _UsdCliSecurityAlertPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 1),
    _UsdCliSecurityAlertPriority_Type()
)
usdCliSecurityAlertPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usdCliSecurityAlertPriority.setStatus("current")
_UsdCliSecurityAlertMessage_Type = DisplayString
_UsdCliSecurityAlertMessage_Object = MibScalar
usdCliSecurityAlertMessage = _UsdCliSecurityAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 2),
    _UsdCliSecurityAlertMessage_Type()
)
usdCliSecurityAlertMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usdCliSecurityAlertMessage.setStatus("current")
_UsdCliSecurityAlertTime_Type = DateAndTime
_UsdCliSecurityAlertTime_Object = MibScalar
usdCliSecurityAlertTime = _UsdCliSecurityAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 3),
    _UsdCliSecurityAlertTime_Type()
)
usdCliSecurityAlertTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usdCliSecurityAlertTime.setStatus("current")
_UsdCliConformance_ObjectIdentity = ObjectIdentity
usdCliConformance = _UsdCliConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2)
)
_UsdCliCompliances_ObjectIdentity = ObjectIdentity
usdCliCompliances = _UsdCliCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1)
)
_UsdCliGroups_ObjectIdentity = ObjectIdentity
usdCliGroups = _UsdCliGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2)
)

# Managed Objects groups

usdCliGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 1)
)
usdCliGroup.setObjects(
    ("Unisphere-Data-CLI-MIB", "usdCliSecurityTrapEnable")
)
if mibBuilder.loadTexts:
    usdCliGroup.setStatus("current")

usdCliSecurityAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 2)
)
usdCliSecurityAlertGroup.setObjects(
      *(("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertPriority"),
        ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertMessage"),
        ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertTime"))
)
if mibBuilder.loadTexts:
    usdCliSecurityAlertGroup.setStatus("current")


# Notification objects

usdCliSecurityAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0, 1)
)
usdCliSecurityAlert.setObjects(
      *(("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertPriority"),
        ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertMessage"),
        ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertTime"))
)
if mibBuilder.loadTexts:
    usdCliSecurityAlert.setStatus(
        "current"
    )


# Notifications groups

usdCliSecurityTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 3)
)
usdCliSecurityTrapGroup.setObjects(
    ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlert")
)
if mibBuilder.loadTexts:
    usdCliSecurityTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

usdCliCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdCliCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-CLI-MIB",
    **{"usdCliMIB": usdCliMIB,
       "usdCliTrap": usdCliTrap,
       "usdCliSecurityAlert": usdCliSecurityAlert,
       "usdCliObjects": usdCliObjects,
       "usdCliGeneral": usdCliGeneral,
       "usdCliSecurityTrapEnable": usdCliSecurityTrapEnable,
       "usdCliSecurity": usdCliSecurity,
       "usdCliSecurityAlertPriority": usdCliSecurityAlertPriority,
       "usdCliSecurityAlertMessage": usdCliSecurityAlertMessage,
       "usdCliSecurityAlertTime": usdCliSecurityAlertTime,
       "usdCliConformance": usdCliConformance,
       "usdCliCompliances": usdCliCompliances,
       "usdCliCompliance": usdCliCompliance,
       "usdCliGroups": usdCliGroups,
       "usdCliGroup": usdCliGroup,
       "usdCliSecurityAlertGroup": usdCliSecurityAlertGroup,
       "usdCliSecurityTrapGroup": usdCliSecurityTrapGroup}
)
