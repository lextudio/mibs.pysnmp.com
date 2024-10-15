# SNMP MIB module (ALVARION-CLIENT-TRACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-CLIENT-TRACKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:31 2024
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionNotificationEnable,) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionNotificationEnable")

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

alvarionClientTrackingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionClientTrackingMIBObjects_ObjectIdentity = ObjectIdentity
alvarionClientTrackingMIBObjects = _AlvarionClientTrackingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1)
)
_ClientTrackingConfig_ObjectIdentity = ObjectIdentity
clientTrackingConfig = _ClientTrackingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1)
)


class _ClientTrackingSuccessfulAssociationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type clientTrackingSuccessfulAssociationNotificationEnabled based on AlvarionNotificationEnable"""


_ClientTrackingSuccessfulAssociationNotificationEnabled_Object = MibScalar
clientTrackingSuccessfulAssociationNotificationEnabled = _ClientTrackingSuccessfulAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 1),
    _ClientTrackingSuccessfulAssociationNotificationEnabled_Type()
)
clientTrackingSuccessfulAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingSuccessfulAssociationNotificationEnabled.setStatus("current")


class _ClientTrackingAssociationFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type clientTrackingAssociationFailureNotificationEnabled based on AlvarionNotificationEnable"""


_ClientTrackingAssociationFailureNotificationEnabled_Object = MibScalar
clientTrackingAssociationFailureNotificationEnabled = _ClientTrackingAssociationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 2),
    _ClientTrackingAssociationFailureNotificationEnabled_Type()
)
clientTrackingAssociationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingAssociationFailureNotificationEnabled.setStatus("current")


class _ClientTrackingSuccessfulReAssociationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type clientTrackingSuccessfulReAssociationNotificationEnabled based on AlvarionNotificationEnable"""


_ClientTrackingSuccessfulReAssociationNotificationEnabled_Object = MibScalar
clientTrackingSuccessfulReAssociationNotificationEnabled = _ClientTrackingSuccessfulReAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 3),
    _ClientTrackingSuccessfulReAssociationNotificationEnabled_Type()
)
clientTrackingSuccessfulReAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingSuccessfulReAssociationNotificationEnabled.setStatus("current")


class _ClientTrackingReAssociationFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type clientTrackingReAssociationFailureNotificationEnabled based on AlvarionNotificationEnable"""


_ClientTrackingReAssociationFailureNotificationEnabled_Object = MibScalar
clientTrackingReAssociationFailureNotificationEnabled = _ClientTrackingReAssociationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 4),
    _ClientTrackingReAssociationFailureNotificationEnabled_Type()
)
clientTrackingReAssociationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingReAssociationFailureNotificationEnabled.setStatus("current")


class _ClientTrackingSuccessfulAuthenticationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type clientTrackingSuccessfulAuthenticationNotificationEnabled based on AlvarionNotificationEnable"""


_ClientTrackingSuccessfulAuthenticationNotificationEnabled_Object = MibScalar
clientTrackingSuccessfulAuthenticationNotificationEnabled = _ClientTrackingSuccessfulAuthenticationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 5),
    _ClientTrackingSuccessfulAuthenticationNotificationEnabled_Type()
)
clientTrackingSuccessfulAuthenticationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingSuccessfulAuthenticationNotificationEnabled.setStatus("current")


class _ClientTrackingAuthenticationFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type clientTrackingAuthenticationFailureNotificationEnabled based on AlvarionNotificationEnable"""


_ClientTrackingAuthenticationFailureNotificationEnabled_Object = MibScalar
clientTrackingAuthenticationFailureNotificationEnabled = _ClientTrackingAuthenticationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 6),
    _ClientTrackingAuthenticationFailureNotificationEnabled_Type()
)
clientTrackingAuthenticationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingAuthenticationFailureNotificationEnabled.setStatus("current")


class _ClientTrackingSuccessfulDisAssociationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type clientTrackingSuccessfulDisAssociationNotificationEnabled based on AlvarionNotificationEnable"""


_ClientTrackingSuccessfulDisAssociationNotificationEnabled_Object = MibScalar
clientTrackingSuccessfulDisAssociationNotificationEnabled = _ClientTrackingSuccessfulDisAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 7),
    _ClientTrackingSuccessfulDisAssociationNotificationEnabled_Type()
)
clientTrackingSuccessfulDisAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingSuccessfulDisAssociationNotificationEnabled.setStatus("current")


class _ClientTrackingDisAssociationFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type clientTrackingDisAssociationFailureNotificationEnabled based on AlvarionNotificationEnable"""


_ClientTrackingDisAssociationFailureNotificationEnabled_Object = MibScalar
clientTrackingDisAssociationFailureNotificationEnabled = _ClientTrackingDisAssociationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 8),
    _ClientTrackingDisAssociationFailureNotificationEnabled_Type()
)
clientTrackingDisAssociationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingDisAssociationFailureNotificationEnabled.setStatus("current")


class _ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type clientTrackingSuccessfulDeAuthenticationNotificationEnabled based on AlvarionNotificationEnable"""


_ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Object = MibScalar
clientTrackingSuccessfulDeAuthenticationNotificationEnabled = _ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 9),
    _ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Type()
)
clientTrackingSuccessfulDeAuthenticationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingSuccessfulDeAuthenticationNotificationEnabled.setStatus("current")


class _ClientTrackingDeAuthenticationFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type clientTrackingDeAuthenticationFailureNotificationEnabled based on AlvarionNotificationEnable"""


_ClientTrackingDeAuthenticationFailureNotificationEnabled_Object = MibScalar
clientTrackingDeAuthenticationFailureNotificationEnabled = _ClientTrackingDeAuthenticationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 10),
    _ClientTrackingDeAuthenticationFailureNotificationEnabled_Type()
)
clientTrackingDeAuthenticationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientTrackingDeAuthenticationFailureNotificationEnabled.setStatus("current")
_ClientTrackingInfo_ObjectIdentity = ObjectIdentity
clientTrackingInfo = _ClientTrackingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 2)
)
_ClientTrackingEventInformation_Type = DisplayString
_ClientTrackingEventInformation_Object = MibScalar
clientTrackingEventInformation = _ClientTrackingEventInformation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 2, 1),
    _ClientTrackingEventInformation_Type()
)
clientTrackingEventInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clientTrackingEventInformation.setStatus("current")
_AlvarionClientTrackingMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
alvarionClientTrackingMIBNotificationPrefix = _AlvarionClientTrackingMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2)
)
_AlvarionClientTrackingMIBNotifications_ObjectIdentity = ObjectIdentity
alvarionClientTrackingMIBNotifications = _AlvarionClientTrackingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0)
)
_AlvarionClientTrackingMIBConformance_ObjectIdentity = ObjectIdentity
alvarionClientTrackingMIBConformance = _AlvarionClientTrackingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3)
)
_AlvarionClientTrackingMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionClientTrackingMIBCompliances = _AlvarionClientTrackingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 1)
)
_AlvarionClientTrackingMIBGroups_ObjectIdentity = ObjectIdentity
alvarionClientTrackingMIBGroups = _AlvarionClientTrackingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 2)
)

# Managed Objects groups

alvarionClientTrackingConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 2, 1)
)
alvarionClientTrackingConfigMIBGroup.setObjects(
      *(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAssociationNotificationEnabled"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingAssociationFailureNotificationEnabled"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulReAssociationNotificationEnabled"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingReAssociationFailureNotificationEnabled"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAuthenticationNotificationEnabled"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingAuthenticationFailureNotificationEnabled"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDisAssociationNotificationEnabled"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingDisAssociationFailureNotificationEnabled"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDeAuthenticationNotificationEnabled"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingDeAuthenticationFailureNotificationEnabled"))
)
if mibBuilder.loadTexts:
    alvarionClientTrackingConfigMIBGroup.setStatus("current")

alvarionClientTrackingInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 2, 2)
)
alvarionClientTrackingInfoMIBGroup.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    alvarionClientTrackingInfoMIBGroup.setStatus("current")


# Notification objects

clientTrackingSuccessfulAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 1)
)
clientTrackingSuccessfulAssociation.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingSuccessfulAssociation.setStatus(
        "current"
    )

clientTrackingAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 2)
)
clientTrackingAssociationFailure.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingAssociationFailure.setStatus(
        "current"
    )

clientTrackingSuccessfulReAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 3)
)
clientTrackingSuccessfulReAssociation.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingSuccessfulReAssociation.setStatus(
        "current"
    )

clientTrackingReAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 4)
)
clientTrackingReAssociationFailure.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingReAssociationFailure.setStatus(
        "current"
    )

clientTrackingSuccessfulAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 5)
)
clientTrackingSuccessfulAuthentication.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingSuccessfulAuthentication.setStatus(
        "current"
    )

clientTrackingAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 6)
)
clientTrackingAuthenticationFailure.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingAuthenticationFailure.setStatus(
        "current"
    )

clientTrackingSuccessfulDisAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 7)
)
clientTrackingSuccessfulDisAssociation.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingSuccessfulDisAssociation.setStatus(
        "current"
    )

clientTrackingDisAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 8)
)
clientTrackingDisAssociationFailure.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingDisAssociationFailure.setStatus(
        "current"
    )

clientTrackingSuccessfulDeAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 9)
)
clientTrackingSuccessfulDeAuthentication.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingSuccessfulDeAuthentication.setStatus(
        "current"
    )

clientTrackingDeAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 10)
)
clientTrackingDeAuthenticationFailure.setObjects(
    ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation")
)
if mibBuilder.loadTexts:
    clientTrackingDeAuthenticationFailure.setStatus(
        "current"
    )


# Notifications groups

alvarionClientTrackingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 2, 3)
)
alvarionClientTrackingNotificationGroup.setObjects(
      *(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAssociation"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingAssociationFailure"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulReAssociation"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingReAssociationFailure"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAuthentication"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingAuthenticationFailure"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDisAssociation"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingDisAssociationFailure"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDeAuthentication"),
        ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingDeAuthenticationFailure"))
)
if mibBuilder.loadTexts:
    alvarionClientTrackingNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alvarionClientTrackingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionClientTrackingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-CLIENT-TRACKING-MIB",
    **{"alvarionClientTrackingMIB": alvarionClientTrackingMIB,
       "alvarionClientTrackingMIBObjects": alvarionClientTrackingMIBObjects,
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
       "alvarionClientTrackingMIBNotificationPrefix": alvarionClientTrackingMIBNotificationPrefix,
       "alvarionClientTrackingMIBNotifications": alvarionClientTrackingMIBNotifications,
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
       "alvarionClientTrackingMIBConformance": alvarionClientTrackingMIBConformance,
       "alvarionClientTrackingMIBCompliances": alvarionClientTrackingMIBCompliances,
       "alvarionClientTrackingMIBCompliance": alvarionClientTrackingMIBCompliance,
       "alvarionClientTrackingMIBGroups": alvarionClientTrackingMIBGroups,
       "alvarionClientTrackingConfigMIBGroup": alvarionClientTrackingConfigMIBGroup,
       "alvarionClientTrackingInfoMIBGroup": alvarionClientTrackingInfoMIBGroup,
       "alvarionClientTrackingNotificationGroup": alvarionClientTrackingNotificationGroup}
)
