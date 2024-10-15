# SNMP MIB module (RBN-MEDIA-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-MEDIA-GATEWAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:15 2024
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

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rbnMediaGatewayMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52)
)
rbnMediaGatewayMib.setRevisions(
        ("2010-04-19 00:00",
         "2009-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnMediaGatewayNotifications_ObjectIdentity = ObjectIdentity
rbnMediaGatewayNotifications = _RbnMediaGatewayNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 0)
)
_RbnMediaGatewayObjects_ObjectIdentity = ObjectIdentity
rbnMediaGatewayObjects = _RbnMediaGatewayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 1)
)
_RbnMediaGatewayNotify_ObjectIdentity = ObjectIdentity
rbnMediaGatewayNotify = _RbnMediaGatewayNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1)
)
_RbnMGEventDateAndTime_Type = DateAndTime
_RbnMGEventDateAndTime_Object = MibScalar
rbnMGEventDateAndTime = _RbnMGEventDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 1),
    _RbnMGEventDateAndTime_Type()
)
rbnMGEventDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnMGEventDateAndTime.setStatus("current")
_RbnMGEventSeverity_Type = ItuPerceivedSeverity
_RbnMGEventSeverity_Object = MibScalar
rbnMGEventSeverity = _RbnMGEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 2),
    _RbnMGEventSeverity_Type()
)
rbnMGEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnMGEventSeverity.setStatus("current")


class _RbnMGEventSender_Type(SnmpAdminString):
    """Custom type rbnMGEventSender based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RbnMGEventSender_Type.__name__ = "SnmpAdminString"
_RbnMGEventSender_Object = MibScalar
rbnMGEventSender = _RbnMGEventSender_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 3),
    _RbnMGEventSender_Type()
)
rbnMGEventSender.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnMGEventSender.setStatus("current")
_RbnMGEventType_Type = IANAItuEventType
_RbnMGEventType_Object = MibScalar
rbnMGEventType = _RbnMGEventType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 4),
    _RbnMGEventType_Type()
)
rbnMGEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnMGEventType.setStatus("current")
_RbnMGEventProbableCause_Type = IANAItuProbableCause
_RbnMGEventProbableCause_Object = MibScalar
rbnMGEventProbableCause = _RbnMGEventProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 5),
    _RbnMGEventProbableCause_Type()
)
rbnMGEventProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnMGEventProbableCause.setStatus("current")


class _RbnMGEventInformation_Type(SnmpAdminString):
    """Custom type rbnMGEventInformation based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RbnMGEventInformation_Type.__name__ = "SnmpAdminString"
_RbnMGEventInformation_Object = MibScalar
rbnMGEventInformation = _RbnMGEventInformation_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 6),
    _RbnMGEventInformation_Type()
)
rbnMGEventInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnMGEventInformation.setStatus("current")
_RbnMediaGatewayConformance_ObjectIdentity = ObjectIdentity
rbnMediaGatewayConformance = _RbnMediaGatewayConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 2)
)
_RbnMediaGatewayCompliances_ObjectIdentity = ObjectIdentity
rbnMediaGatewayCompliances = _RbnMediaGatewayCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 1)
)
_RbnMediaGatewayGroups_ObjectIdentity = ObjectIdentity
rbnMediaGatewayGroups = _RbnMediaGatewayGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 2)
)

# Managed Objects groups

rbnMGNotifyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 2, 1)
)
rbnMGNotifyObjectGroup.setObjects(
      *(("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventDateAndTime"),
        ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSeverity"),
        ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSender"),
        ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventType"),
        ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventProbableCause"),
        ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventInformation"))
)
if mibBuilder.loadTexts:
    rbnMGNotifyObjectGroup.setStatus("current")


# Notification objects

rbnH248LinkStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 0, 1)
)
rbnH248LinkStatusAlarm.setObjects(
      *(("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventDateAndTime"),
        ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSeverity"),
        ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSender"),
        ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventType"),
        ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventProbableCause"),
        ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventInformation"))
)
if mibBuilder.loadTexts:
    rbnH248LinkStatusAlarm.setStatus(
        "current"
    )


# Notifications groups

rbnMGLinkNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 2, 2)
)
rbnMGLinkNotifyGroup.setObjects(
    ("RBN-MEDIA-GATEWAY-MIB", "rbnH248LinkStatusAlarm")
)
if mibBuilder.loadTexts:
    rbnMGLinkNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnMGCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnMGCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-MEDIA-GATEWAY-MIB",
    **{"rbnMediaGatewayMib": rbnMediaGatewayMib,
       "rbnMediaGatewayNotifications": rbnMediaGatewayNotifications,
       "rbnH248LinkStatusAlarm": rbnH248LinkStatusAlarm,
       "rbnMediaGatewayObjects": rbnMediaGatewayObjects,
       "rbnMediaGatewayNotify": rbnMediaGatewayNotify,
       "rbnMGEventDateAndTime": rbnMGEventDateAndTime,
       "rbnMGEventSeverity": rbnMGEventSeverity,
       "rbnMGEventSender": rbnMGEventSender,
       "rbnMGEventType": rbnMGEventType,
       "rbnMGEventProbableCause": rbnMGEventProbableCause,
       "rbnMGEventInformation": rbnMGEventInformation,
       "rbnMediaGatewayConformance": rbnMediaGatewayConformance,
       "rbnMediaGatewayCompliances": rbnMediaGatewayCompliances,
       "rbnMGCompliance": rbnMGCompliance,
       "rbnMediaGatewayGroups": rbnMediaGatewayGroups,
       "rbnMGNotifyObjectGroup": rbnMGNotifyObjectGroup,
       "rbnMGLinkNotifyGroup": rbnMGLinkNotifyGroup}
)
