# SNMP MIB module (CISCO-ESC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ESC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:54 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoEscMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 844)
)
ciscoEscMIB.setRevisions(
        ("2017-03-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EscNotifs_ObjectIdentity = ObjectIdentity
escNotifs = _EscNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 0)
)
_EscMIBObjects_ObjectIdentity = ObjectIdentity
escMIBObjects = _EscMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 1)
)
_Vnfm_ObjectIdentity = ObjectIdentity
vnfm = _Vnfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 1, 1)
)
_EscStatusMessage_Type = OctetString
_EscStatusMessage_Object = MibScalar
escStatusMessage = _EscStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 1, 1, 1),
    _EscStatusMessage_Type()
)
escStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    escStatusMessage.setStatus("current")
_EscStatusCode_Type = OctetString
_EscStatusCode_Object = MibScalar
escStatusCode = _EscStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 1, 1, 2),
    _EscStatusCode_Type()
)
escStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    escStatusCode.setStatus("current")
_CiscoEscMIBConform_ObjectIdentity = ObjectIdentity
ciscoEscMIBConform = _CiscoEscMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 2)
)
_CiscoEscMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEscMIBCompliances = _CiscoEscMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 1)
)
_CiscoEscMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEscMIBGroups = _CiscoEscMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 2)
)

# Managed Objects groups

ciscoEscMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 2, 1)
)
ciscoEscMIBObjectGroup.setObjects(
      *(("CISCO-ESC-MIB", "escStatusCode"),
        ("CISCO-ESC-MIB", "escStatusMessage"))
)
if mibBuilder.loadTexts:
    ciscoEscMIBObjectGroup.setStatus("current")


# Notification objects

escStatusNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 0, 1)
)
escStatusNotif.setObjects(
      *(("CISCO-ESC-MIB", "escStatusCode"),
        ("CISCO-ESC-MIB", "escStatusMessage"))
)
if mibBuilder.loadTexts:
    escStatusNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoEscMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 2, 2)
)
ciscoEscMIBNotificationGroup.setObjects(
    ("CISCO-ESC-MIB", "escStatusNotif")
)
if mibBuilder.loadTexts:
    ciscoEscMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEscMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEscMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ESC-MIB",
    **{"ciscoEscMIB": ciscoEscMIB,
       "escNotifs": escNotifs,
       "escStatusNotif": escStatusNotif,
       "escMIBObjects": escMIBObjects,
       "vnfm": vnfm,
       "escStatusMessage": escStatusMessage,
       "escStatusCode": escStatusCode,
       "ciscoEscMIBConform": ciscoEscMIBConform,
       "ciscoEscMIBCompliances": ciscoEscMIBCompliances,
       "ciscoEscMIBCompliance": ciscoEscMIBCompliance,
       "ciscoEscMIBGroups": ciscoEscMIBGroups,
       "ciscoEscMIBObjectGroup": ciscoEscMIBObjectGroup,
       "ciscoEscMIBNotificationGroup": ciscoEscMIBNotificationGroup}
)
