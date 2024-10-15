# SNMP MIB module (Juniper-CLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-CLI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:52 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniLogSeverity,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniLogSeverity")

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


# MODULE-IDENTITY

juniCliMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30)
)
juniCliMIB.setRevisions(
        ("2007-12-10 13:25",
         "2002-09-16 21:44",
         "2000-09-26 13:50",
         "1999-12-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniCliTrap_ObjectIdentity = ObjectIdentity
juniCliTrap = _JuniCliTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0)
)
_JuniCliObjects_ObjectIdentity = ObjectIdentity
juniCliObjects = _JuniCliObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1)
)
_JuniCliGeneral_ObjectIdentity = ObjectIdentity
juniCliGeneral = _JuniCliGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1)
)
_JuniCliSecurityTrapEnable_Type = TruthValue
_JuniCliSecurityTrapEnable_Object = MibScalar
juniCliSecurityTrapEnable = _JuniCliSecurityTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1, 1),
    _JuniCliSecurityTrapEnable_Type()
)
juniCliSecurityTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniCliSecurityTrapEnable.setStatus("current")
_JuniCliSecurity_ObjectIdentity = ObjectIdentity
juniCliSecurity = _JuniCliSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2)
)
_JuniCliSecurityAlertPriority_Type = JuniLogSeverity
_JuniCliSecurityAlertPriority_Object = MibScalar
juniCliSecurityAlertPriority = _JuniCliSecurityAlertPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 1),
    _JuniCliSecurityAlertPriority_Type()
)
juniCliSecurityAlertPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniCliSecurityAlertPriority.setStatus("current")
_JuniCliSecurityAlertMessage_Type = DisplayString
_JuniCliSecurityAlertMessage_Object = MibScalar
juniCliSecurityAlertMessage = _JuniCliSecurityAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 2),
    _JuniCliSecurityAlertMessage_Type()
)
juniCliSecurityAlertMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniCliSecurityAlertMessage.setStatus("current")
_JuniCliSecurityAlertTime_Type = DateAndTime
_JuniCliSecurityAlertTime_Object = MibScalar
juniCliSecurityAlertTime = _JuniCliSecurityAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 3),
    _JuniCliSecurityAlertTime_Type()
)
juniCliSecurityAlertTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniCliSecurityAlertTime.setStatus("current")
_JuniCliConfigurationTable_Object = MibTable
juniCliConfigurationTable = _JuniCliConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3)
)
if mibBuilder.loadTexts:
    juniCliConfigurationTable.setStatus("current")
_JuniCliConfigurationEntry_Object = MibTableRow
juniCliConfigurationEntry = _JuniCliConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1)
)
juniCliConfigurationEntry.setIndexNames(
    (0, "Juniper-CLI-MIB", "juniCliConfigurationIndex"),
)
if mibBuilder.loadTexts:
    juniCliConfigurationEntry.setStatus("current")


class _JuniCliConfigurationIndex_Type(Integer32):
    """Custom type juniCliConfigurationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniCliConfigurationIndex_Type.__name__ = "Integer32"
_JuniCliConfigurationIndex_Object = MibTableColumn
juniCliConfigurationIndex = _JuniCliConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 1),
    _JuniCliConfigurationIndex_Type()
)
juniCliConfigurationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniCliConfigurationIndex.setStatus("current")


class _JuniCliConfigurationFileName_Type(DisplayString):
    """Custom type juniCliConfigurationFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniCliConfigurationFileName_Type.__name__ = "DisplayString"
_JuniCliConfigurationFileName_Object = MibTableColumn
juniCliConfigurationFileName = _JuniCliConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 2),
    _JuniCliConfigurationFileName_Type()
)
juniCliConfigurationFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCliConfigurationFileName.setStatus("current")


class _JuniCliConfigurationApply_Type(Integer32):
    """Custom type juniCliConfigurationApply based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("juniCliConfigurationApplyNow", 1),
          ("juniCliConfigurationReadyToApply", 0))
    )


_JuniCliConfigurationApply_Type.__name__ = "Integer32"
_JuniCliConfigurationApply_Object = MibTableColumn
juniCliConfigurationApply = _JuniCliConfigurationApply_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 3),
    _JuniCliConfigurationApply_Type()
)
juniCliConfigurationApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniCliConfigurationApply.setStatus("current")


class _JuniCliConfigurationOpStatus_Type(Integer32):
    """Custom type juniCliConfigurationOpStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("juniCliConfigurationFileIncompatible", 4),
          ("juniCliConfigurationFileNotFound", 3),
          ("juniCliConfigurationOpInProgress", 2),
          ("juniCliConfigurationOpNoOp", 0),
          ("juniCliConfigurationOpSuccessful", 1),
          ("juniCliConfigurationOperationFailed", 5))
    )


_JuniCliConfigurationOpStatus_Type.__name__ = "Integer32"
_JuniCliConfigurationOpStatus_Object = MibTableColumn
juniCliConfigurationOpStatus = _JuniCliConfigurationOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 4),
    _JuniCliConfigurationOpStatus_Type()
)
juniCliConfigurationOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniCliConfigurationOpStatus.setStatus("current")
_JuniCliConformance_ObjectIdentity = ObjectIdentity
juniCliConformance = _JuniCliConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2)
)
_JuniCliCompliances_ObjectIdentity = ObjectIdentity
juniCliCompliances = _JuniCliCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1)
)
_JuniCliGroups_ObjectIdentity = ObjectIdentity
juniCliGroups = _JuniCliGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2)
)

# Managed Objects groups

juniCliGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 1)
)
juniCliGroup.setObjects(
    ("Juniper-CLI-MIB", "juniCliSecurityTrapEnable")
)
if mibBuilder.loadTexts:
    juniCliGroup.setStatus("current")

juniCliSecurityAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 2)
)
juniCliSecurityAlertGroup.setObjects(
      *(("Juniper-CLI-MIB", "juniCliSecurityAlertPriority"),
        ("Juniper-CLI-MIB", "juniCliSecurityAlertMessage"),
        ("Juniper-CLI-MIB", "juniCliSecurityAlertTime"))
)
if mibBuilder.loadTexts:
    juniCliSecurityAlertGroup.setStatus("current")

juniCliConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 4)
)
juniCliConfigurationGroup.setObjects(
      *(("Juniper-CLI-MIB", "juniCliConfigurationFileName"),
        ("Juniper-CLI-MIB", "juniCliConfigurationApply"),
        ("Juniper-CLI-MIB", "juniCliConfigurationOpStatus"))
)
if mibBuilder.loadTexts:
    juniCliConfigurationGroup.setStatus("current")


# Notification objects

juniCliSecurityAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0, 1)
)
juniCliSecurityAlert.setObjects(
      *(("Juniper-CLI-MIB", "juniCliSecurityAlertPriority"),
        ("Juniper-CLI-MIB", "juniCliSecurityAlertMessage"),
        ("Juniper-CLI-MIB", "juniCliSecurityAlertTime"))
)
if mibBuilder.loadTexts:
    juniCliSecurityAlert.setStatus(
        "current"
    )


# Notifications groups

juniCliSecurityTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 3)
)
juniCliSecurityTrapGroup.setObjects(
    ("Juniper-CLI-MIB", "juniCliSecurityAlert")
)
if mibBuilder.loadTexts:
    juniCliSecurityTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniCliCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniCliCompliance.setStatus(
        "obsolete"
    )

juniCliCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniCliCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-CLI-MIB",
    **{"juniCliMIB": juniCliMIB,
       "juniCliTrap": juniCliTrap,
       "juniCliSecurityAlert": juniCliSecurityAlert,
       "juniCliObjects": juniCliObjects,
       "juniCliGeneral": juniCliGeneral,
       "juniCliSecurityTrapEnable": juniCliSecurityTrapEnable,
       "juniCliSecurity": juniCliSecurity,
       "juniCliSecurityAlertPriority": juniCliSecurityAlertPriority,
       "juniCliSecurityAlertMessage": juniCliSecurityAlertMessage,
       "juniCliSecurityAlertTime": juniCliSecurityAlertTime,
       "juniCliConfigurationTable": juniCliConfigurationTable,
       "juniCliConfigurationEntry": juniCliConfigurationEntry,
       "juniCliConfigurationIndex": juniCliConfigurationIndex,
       "juniCliConfigurationFileName": juniCliConfigurationFileName,
       "juniCliConfigurationApply": juniCliConfigurationApply,
       "juniCliConfigurationOpStatus": juniCliConfigurationOpStatus,
       "juniCliConformance": juniCliConformance,
       "juniCliCompliances": juniCliCompliances,
       "juniCliCompliance": juniCliCompliance,
       "juniCliCompliance2": juniCliCompliance2,
       "juniCliGroups": juniCliGroups,
       "juniCliGroup": juniCliGroup,
       "juniCliSecurityAlertGroup": juniCliSecurityAlertGroup,
       "juniCliSecurityTrapGroup": juniCliSecurityTrapGroup,
       "juniCliConfigurationGroup": juniCliConfigurationGroup}
)
