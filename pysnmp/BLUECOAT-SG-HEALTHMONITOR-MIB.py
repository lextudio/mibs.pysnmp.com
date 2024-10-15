# SNMP MIB module (BLUECOAT-SG-HEALTHMONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUECOAT-SG-HEALTHMONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:20 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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

bluecoatSGHealthMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12)
)
bluecoatSGHealthMonMIB.setRevisions(
        ("2013-06-10 03:00",
         "2007-11-05 03:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HealthMonMessageString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class HealthMonStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("ok", 1),
          ("unknown", 4),
          ("warning", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DeviceHealthMonMIBObjects_ObjectIdentity = ObjectIdentity
deviceHealthMonMIBObjects = _DeviceHealthMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 1)
)
_DeviceHealthMonValues_ObjectIdentity = ObjectIdentity
deviceHealthMonValues = _DeviceHealthMonValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 1, 1)
)
_DeviceHealthMonMessage_Type = HealthMonMessageString
_DeviceHealthMonMessage_Object = MibScalar
deviceHealthMonMessage = _DeviceHealthMonMessage_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 1, 1, 1),
    _DeviceHealthMonMessage_Type()
)
deviceHealthMonMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHealthMonMessage.setStatus("current")
_DeviceHealthMonStatus_Type = HealthMonStatus
_DeviceHealthMonStatus_Object = MibScalar
deviceHealthMonStatus = _DeviceHealthMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 1, 1, 2),
    _DeviceHealthMonStatus_Type()
)
deviceHealthMonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHealthMonStatus.setStatus("current")
_DeviceHealthMonMIBNotification_ObjectIdentity = ObjectIdentity
deviceHealthMonMIBNotification = _DeviceHealthMonMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 2)
)
_DeviceHealthMonMIBNotifPrefix_ObjectIdentity = ObjectIdentity
deviceHealthMonMIBNotifPrefix = _DeviceHealthMonMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0)
)
_DeviceHealthMonMIBConformance_ObjectIdentity = ObjectIdentity
deviceHealthMonMIBConformance = _DeviceHealthMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 3)
)
_DeviceHealthMonMIBCompliances_ObjectIdentity = ObjectIdentity
deviceHealthMonMIBCompliances = _DeviceHealthMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 1)
)
_DeviceHealthMonMIBGroups_ObjectIdentity = ObjectIdentity
deviceHealthMonMIBGroups = _DeviceHealthMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 2)
)
_DeviceHealthMonMIBNotifGroups_ObjectIdentity = ObjectIdentity
deviceHealthMonMIBNotifGroups = _DeviceHealthMonMIBNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 3)
)

# Managed Objects groups

deviceHealthMonMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 2, 1)
)
deviceHealthMonMIBGroup.setObjects(
      *(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonStatus"),
        ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage"))
)
if mibBuilder.loadTexts:
    deviceHealthMonMIBGroup.setStatus("current")


# Notification objects

deviceHealthMonOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0, 1)
)
deviceHealthMonOkTrap.setObjects(
    ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage")
)
if mibBuilder.loadTexts:
    deviceHealthMonOkTrap.setStatus(
        "current"
    )

deviceHealthMonWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0, 2)
)
deviceHealthMonWarningTrap.setObjects(
    ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage")
)
if mibBuilder.loadTexts:
    deviceHealthMonWarningTrap.setStatus(
        "current"
    )

deviceHealthMonCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0, 3)
)
deviceHealthMonCriticalTrap.setObjects(
    ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage")
)
if mibBuilder.loadTexts:
    deviceHealthMonCriticalTrap.setStatus(
        "current"
    )


# Notifications groups

deviceHealthMonMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 3, 1)
)
deviceHealthMonMIBNotifGroup.setObjects(
      *(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonOkTrap"),
        ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonWarningTrap"),
        ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonCriticalTrap"))
)
if mibBuilder.loadTexts:
    deviceHealthMonMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

deviceHealthMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 1, 1)
)
if mibBuilder.loadTexts:
    deviceHealthMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-HEALTHMONITOR-MIB",
    **{"HealthMonMessageString": HealthMonMessageString,
       "HealthMonStatus": HealthMonStatus,
       "bluecoatSGHealthMonMIB": bluecoatSGHealthMonMIB,
       "deviceHealthMonMIBObjects": deviceHealthMonMIBObjects,
       "deviceHealthMonValues": deviceHealthMonValues,
       "deviceHealthMonMessage": deviceHealthMonMessage,
       "deviceHealthMonStatus": deviceHealthMonStatus,
       "deviceHealthMonMIBNotification": deviceHealthMonMIBNotification,
       "deviceHealthMonMIBNotifPrefix": deviceHealthMonMIBNotifPrefix,
       "deviceHealthMonOkTrap": deviceHealthMonOkTrap,
       "deviceHealthMonWarningTrap": deviceHealthMonWarningTrap,
       "deviceHealthMonCriticalTrap": deviceHealthMonCriticalTrap,
       "deviceHealthMonMIBConformance": deviceHealthMonMIBConformance,
       "deviceHealthMonMIBCompliances": deviceHealthMonMIBCompliances,
       "deviceHealthMonMIBCompliance": deviceHealthMonMIBCompliance,
       "deviceHealthMonMIBGroups": deviceHealthMonMIBGroups,
       "deviceHealthMonMIBGroup": deviceHealthMonMIBGroup,
       "deviceHealthMonMIBNotifGroups": deviceHealthMonMIBNotifGroups,
       "deviceHealthMonMIBNotifGroup": deviceHealthMonMIBNotifGroup}
)
