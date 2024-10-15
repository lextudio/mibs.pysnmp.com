# SNMP MIB module (COLUBRIS-CLIENT-TRACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-CLIENT-TRACKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:12 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisNotificationEnable,) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisNotificationEnable")

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

colubrisClientTrackingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisClientTrackingMIBObjects_ObjectIdentity = ObjectIdentity
colubrisClientTrackingMIBObjects = _ColubrisClientTrackingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1)
)
_ClientTrackingConfig_ObjectIdentity = ObjectIdentity
clientTrackingConfig = _ClientTrackingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1)
)


class _ClientTrackingSuccessfulAssociationNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type clientTrackingSuccessfulAssociationNotificationEnabled based on ColubrisNotificationEnable"""


_ClientTrackingSuccessfulAssociationNotificationEnabled_Object = MibScalar
clientTrackingSuccessfulAssociationNotificationEnabled = _ClientTrackingSuccessfulAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 1),
    _ClientTrackingSuccessfulAssociationNotificationEnabled_Type()
)
clientTrackingSuccessfulAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingSuccessfulAssociationNotificationEnabled.setStatus("current")


class _ClientTrackingAssociationFailureNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type clientTrackingAssociationFailureNotificationEnabled based on ColubrisNotificationEnable"""


_ClientTrackingAssociationFailureNotificationEnabled_Object = MibScalar
clientTrackingAssociationFailureNotificationEnabled = _ClientTrackingAssociationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 2),
    _ClientTrackingAssociationFailureNotificationEnabled_Type()
)
clientTrackingAssociationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingAssociationFailureNotificationEnabled.setStatus("current")


class _ClientTrackingSuccessfulReAssociationNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type clientTrackingSuccessfulReAssociationNotificationEnabled based on ColubrisNotificationEnable"""


_ClientTrackingSuccessfulReAssociationNotificationEnabled_Object = MibScalar
clientTrackingSuccessfulReAssociationNotificationEnabled = _ClientTrackingSuccessfulReAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 3),
    _ClientTrackingSuccessfulReAssociationNotificationEnabled_Type()
)
clientTrackingSuccessfulReAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingSuccessfulReAssociationNotificationEnabled.setStatus("current")


class _ClientTrackingReAssociationFailureNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type clientTrackingReAssociationFailureNotificationEnabled based on ColubrisNotificationEnable"""


_ClientTrackingReAssociationFailureNotificationEnabled_Object = MibScalar
clientTrackingReAssociationFailureNotificationEnabled = _ClientTrackingReAssociationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 4),
    _ClientTrackingReAssociationFailureNotificationEnabled_Type()
)
clientTrackingReAssociationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingReAssociationFailureNotificationEnabled.setStatus("current")


class _ClientTrackingSuccessfulAuthenticationNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type clientTrackingSuccessfulAuthenticationNotificationEnabled based on ColubrisNotificationEnable"""


_ClientTrackingSuccessfulAuthenticationNotificationEnabled_Object = MibScalar
clientTrackingSuccessfulAuthenticationNotificationEnabled = _ClientTrackingSuccessfulAuthenticationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 5),
    _ClientTrackingSuccessfulAuthenticationNotificationEnabled_Type()
)
clientTrackingSuccessfulAuthenticationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingSuccessfulAuthenticationNotificationEnabled.setStatus("current")


class _ClientTrackingAuthenticationFailureNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type clientTrackingAuthenticationFailureNotificationEnabled based on ColubrisNotificationEnable"""


_ClientTrackingAuthenticationFailureNotificationEnabled_Object = MibScalar
clientTrackingAuthenticationFailureNotificationEnabled = _ClientTrackingAuthenticationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 6),
    _ClientTrackingAuthenticationFailureNotificationEnabled_Type()
)
clientTrackingAuthenticationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingAuthenticationFailureNotificationEnabled.setStatus("current")


class _ClientTrackingSuccessfulDisAssociationNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type clientTrackingSuccessfulDisAssociationNotificationEnabled based on ColubrisNotificationEnable"""


_ClientTrackingSuccessfulDisAssociationNotificationEnabled_Object = MibScalar
clientTrackingSuccessfulDisAssociationNotificationEnabled = _ClientTrackingSuccessfulDisAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 7),
    _ClientTrackingSuccessfulDisAssociationNotificationEnabled_Type()
)
clientTrackingSuccessfulDisAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingSuccessfulDisAssociationNotificationEnabled.setStatus("current")


class _ClientTrackingDisAssociationFailureNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type clientTrackingDisAssociationFailureNotificationEnabled based on ColubrisNotificationEnable"""


_ClientTrackingDisAssociationFailureNotificationEnabled_Object = MibScalar
clientTrackingDisAssociationFailureNotificationEnabled = _ClientTrackingDisAssociationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 8),
    _ClientTrackingDisAssociationFailureNotificationEnabled_Type()
)
clientTrackingDisAssociationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingDisAssociationFailureNotificationEnabled.setStatus("current")


class _ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type clientTrackingSuccessfulDeAuthenticationNotificationEnabled based on ColubrisNotificationEnable"""


_ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Object = MibScalar
clientTrackingSuccessfulDeAuthenticationNotificationEnabled = _ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 9),
    _ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Type()
)
clientTrackingSuccessfulDeAuthenticationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingSuccessfulDeAuthenticationNotificationEnabled.setStatus("current")


class _ClientTrackingDeAuthenticationFailureNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type clientTrackingDeAuthenticationFailureNotificationEnabled based on ColubrisNotificationEnable"""


_ClientTrackingDeAuthenticationFailureNotificationEnabled_Object = MibScalar
clientTrackingDeAuthenticationFailureNotificationEnabled = _ClientTrackingDeAuthenticationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 1, 10),
    _ClientTrackingDeAuthenticationFailureNotificationEnabled_Type()
)
clientTrackingDeAuthenticationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingDeAuthenticationFailureNotificationEnabled.setStatus("current")
_ClientTrackingInfo_ObjectIdentity = ObjectIdentity
clientTrackingInfo = _ClientTrackingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 2)
)
_ClientTrackingEventInformation_Type = DisplayString
_ClientTrackingEventInformation_Object = MibScalar
clientTrackingEventInformation = _ClientTrackingEventInformation_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 1, 2, 1),
    _ClientTrackingEventInformation_Type()
)
clientTrackingEventInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clientTrackingEventInformation.setStatus("current")
_ColubrisClientTrackingMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisClientTrackingMIBNotificationPrefix = _ColubrisClientTrackingMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2)
)
_ColubrisClientTrackingMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisClientTrackingMIBNotifications = _ColubrisClientTrackingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0)
)
_ColubrisClientTrackingMIBConformance_ObjectIdentity = ObjectIdentity
colubrisClientTrackingMIBConformance = _ColubrisClientTrackingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 3)
)
_ColubrisClientTrackingMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisClientTrackingMIBCompliances = _ColubrisClientTrackingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 1)
)
_ColubrisClientTrackingMIBGroups_ObjectIdentity = ObjectIdentity
colubrisClientTrackingMIBGroups = _ColubrisClientTrackingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 2)
)

# Managed Objects groups

colubrisClientTrackingConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 2, 1)
)
colubrisClientTrackingConfigMIBGroup.setObjects(
      *(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAssociationNotificationEnabled"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingAssociationFailureNotificationEnabled"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulReAssociationNotificationEnabled"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingReAssociationFailureNotificationEnabled"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAuthenticationNotificationEnabled"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingAuthenticationFailureNotificationEnabled"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDisAssociationNotificationEnabled"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingDisAssociationFailureNotificationEnabled"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDeAuthenticationNotificationEnabled"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingDeAuthenticationFailureNotificationEnabled"))
)
if mibBuilder.loadTexts:
    colubrisClientTrackingConfigMIBGroup.setStatus("current")

colubrisClientTrackingInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 2, 2)
)
colubrisClientTrackingInfoMIBGroup.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    colubrisClientTrackingInfoMIBGroup.setStatus("current")


# Notification objects

clientTrackingSuccessfulAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 1)
)
clientTrackingSuccessfulAssociation.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingSuccessfulAssociation.setStatus(
        "current"
    )

clientTrackingAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 2)
)
clientTrackingAssociationFailure.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingAssociationFailure.setStatus(
        "current"
    )

clientTrackingSuccessfulReAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 3)
)
clientTrackingSuccessfulReAssociation.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingSuccessfulReAssociation.setStatus(
        "current"
    )

clientTrackingReAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 4)
)
clientTrackingReAssociationFailure.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingReAssociationFailure.setStatus(
        "current"
    )

clientTrackingSuccessfulAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 5)
)
clientTrackingSuccessfulAuthentication.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingSuccessfulAuthentication.setStatus(
        "current"
    )

clientTrackingAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 6)
)
clientTrackingAuthenticationFailure.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingAuthenticationFailure.setStatus(
        "current"
    )

clientTrackingSuccessfulDisAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 7)
)
clientTrackingSuccessfulDisAssociation.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingSuccessfulDisAssociation.setStatus(
        "current"
    )

clientTrackingDisAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 8)
)
clientTrackingDisAssociationFailure.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingDisAssociationFailure.setStatus(
        "current"
    )

clientTrackingSuccessfulDeAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 9)
)
clientTrackingSuccessfulDeAuthentication.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingSuccessfulDeAuthentication.setStatus(
        "current"
    )

clientTrackingDeAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 2, 0, 10)
)
clientTrackingDeAuthenticationFailure.setObjects(
    ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingDeAuthenticationFailure.setStatus(
        "current"
    )


# Notifications groups

colubrisClientTrackingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 2, 3)
)
colubrisClientTrackingNotificationGroup.setObjects(
      *(("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAssociation"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingAssociationFailure"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulReAssociation"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingReAssociationFailure"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAuthentication"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingAuthenticationFailure"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDisAssociation"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingDisAssociationFailure"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDeAuthentication"),
        ("COLUBRIS-CLIENT-TRACKING-MIB", "clientTrackingDeAuthenticationFailure"))
)
if mibBuilder.loadTexts:
    colubrisClientTrackingNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisClientTrackingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 19, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisClientTrackingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-CLIENT-TRACKING-MIB",
    **{"colubrisClientTrackingMIB": colubrisClientTrackingMIB,
       "colubrisClientTrackingMIBObjects": colubrisClientTrackingMIBObjects,
       "clientTrackingConfig": clientTrackingConfig,
       "clientTrackingSuccessfulAssociationNotificationEnabled": clientTrackingSuccessfulAssociationNotificationEnabled,
       "clientTrackingAssociationFailureNotificationEnabled": clientTrackingAssociationFailureNotificationEnabled,
       "clientTrackingSuccessfulReAssociationNotificationEnabled": clientTrackingSuccessfulReAssociationNotificationEnabled,
       "clientTrackingReAssociationFailureNotificationEnabled": clientTrackingReAssociationFailureNotificationEnabled,
       "clientTrackingSuccessfulAuthenticationNotificationEnabled": clientTrackingSuccessfulAuthenticationNotificationEnabled,
       "clientTrackingAuthenticationFailureNotificationEnabled": clientTrackingAuthenticationFailureNotificationEnabled,
       "clientTrackingSuccessfulDisAssociationNotificationEnabled": clientTrackingSuccessfulDisAssociationNotificationEnabled,
       "clientTrackingDisAssociationFailureNotificationEnabled": clientTrackingDisAssociationFailureNotificationEnabled,
       "clientTrackingSuccessfulDeAuthenticationNotificationEnabled": clientTrackingSuccessfulDeAuthenticationNotificationEnabled,
       "clientTrackingDeAuthenticationFailureNotificationEnabled": clientTrackingDeAuthenticationFailureNotificationEnabled,
       "clientTrackingInfo": clientTrackingInfo,
       "clientTrackingEventInformation": clientTrackingEventInformation,
       "colubrisClientTrackingMIBNotificationPrefix": colubrisClientTrackingMIBNotificationPrefix,
       "colubrisClientTrackingMIBNotifications": colubrisClientTrackingMIBNotifications,
       "clientTrackingSuccessfulAssociation": clientTrackingSuccessfulAssociation,
       "clientTrackingAssociationFailure": clientTrackingAssociationFailure,
       "clientTrackingSuccessfulReAssociation": clientTrackingSuccessfulReAssociation,
       "clientTrackingReAssociationFailure": clientTrackingReAssociationFailure,
       "clientTrackingSuccessfulAuthentication": clientTrackingSuccessfulAuthentication,
       "clientTrackingAuthenticationFailure": clientTrackingAuthenticationFailure,
       "clientTrackingSuccessfulDisAssociation": clientTrackingSuccessfulDisAssociation,
       "clientTrackingDisAssociationFailure": clientTrackingDisAssociationFailure,
       "clientTrackingSuccessfulDeAuthentication": clientTrackingSuccessfulDeAuthentication,
       "clientTrackingDeAuthenticationFailure": clientTrackingDeAuthenticationFailure,
       "colubrisClientTrackingMIBConformance": colubrisClientTrackingMIBConformance,
       "colubrisClientTrackingMIBCompliances": colubrisClientTrackingMIBCompliances,
       "colubrisClientTrackingMIBCompliance": colubrisClientTrackingMIBCompliance,
       "colubrisClientTrackingMIBGroups": colubrisClientTrackingMIBGroups,
       "colubrisClientTrackingConfigMIBGroup": colubrisClientTrackingConfigMIBGroup,
       "colubrisClientTrackingInfoMIBGroup": colubrisClientTrackingInfoMIBGroup,
       "colubrisClientTrackingNotificationGroup": colubrisClientTrackingNotificationGroup}
)
