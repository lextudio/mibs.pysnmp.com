# SNMP MIB module (SUNSTORAGEAGENT-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUNSTORAGEAGENT-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:40 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

alertTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 0)
)
alertTrap.setRevisions(
        ("2002-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Storagent_ObjectIdentity = ObjectIdentity
storagent = _Storagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 95)
)
_Alert_ObjectIdentity = ObjectIdentity
alert = _Alert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1)
)
_AlertInfoGroup_ObjectIdentity = ObjectIdentity
alertInfoGroup = _AlertInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1, 3)
)
_DeviceName_Type = OctetString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1, 3, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")


class _AlertLevel_Type(Integer32):
    """Custom type alertLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("critical", 3),
          ("down", 4),
          ("major", 2),
          ("minor", 1))
    )


_AlertLevel_Type.__name__ = "Integer32"
_AlertLevel_Object = MibScalar
alertLevel = _AlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1, 3, 2),
    _AlertLevel_Type()
)
alertLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertLevel.setStatus("current")
_Message_Type = OctetString
_Message_Object = MibScalar
message = _Message_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1, 3, 3),
    _Message_Type()
)
message.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    message.setStatus("current")
_GridId_Type = OctetString
_GridId_Object = MibScalar
gridId = _GridId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1, 3, 4),
    _GridId_Type()
)
gridId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gridId.setStatus("current")
_DeviceId_Type = OctetString
_DeviceId_Object = MibScalar
deviceId = _DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1, 3, 5),
    _DeviceId_Type()
)
deviceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceId.setStatus("current")
_ComponentName_Type = OctetString
_ComponentName_Object = MibScalar
componentName = _ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1, 3, 6),
    _ComponentName_Type()
)
componentName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    componentName.setStatus("current")
_ComponentId_Type = OctetString
_ComponentId_Object = MibScalar
componentId = _ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1, 3, 7),
    _ComponentId_Type()
)
componentId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    componentId.setStatus("current")
_EventId_Type = OctetString
_EventId_Object = MibScalar
eventId = _EventId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1, 3, 8),
    _EventId_Type()
)
eventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventId.setStatus("current")
_EventName_Type = OctetString
_EventName_Object = MibScalar
eventName = _EventName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 1, 3, 9),
    _EventName_Type()
)
eventName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventName.setStatus("current")

# Managed Objects groups


# Notification objects

alertMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 95, 0, 6)
)
alertMessage.setObjects(
      *(("SUNSTORAGEAGENT-NOTIFICATION-MIB", "deviceName"),
        ("SUNSTORAGEAGENT-NOTIFICATION-MIB", "alertLevel"),
        ("SUNSTORAGEAGENT-NOTIFICATION-MIB", "message"),
        ("SUNSTORAGEAGENT-NOTIFICATION-MIB", "gridId"),
        ("SUNSTORAGEAGENT-NOTIFICATION-MIB", "deviceId"),
        ("SUNSTORAGEAGENT-NOTIFICATION-MIB", "componentName"),
        ("SUNSTORAGEAGENT-NOTIFICATION-MIB", "componentId"),
        ("SUNSTORAGEAGENT-NOTIFICATION-MIB", "eventId"),
        ("SUNSTORAGEAGENT-NOTIFICATION-MIB", "eventName"))
)
if mibBuilder.loadTexts:
    alertMessage.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUNSTORAGEAGENT-NOTIFICATION-MIB",
    **{"sun": sun,
       "prod": prod,
       "storagent": storagent,
       "alertTrap": alertTrap,
       "alertMessage": alertMessage,
       "alert": alert,
       "alertInfoGroup": alertInfoGroup,
       "deviceName": deviceName,
       "alertLevel": alertLevel,
       "message": message,
       "gridId": gridId,
       "deviceId": deviceId,
       "componentName": componentName,
       "componentId": componentId,
       "eventId": eventId,
       "eventName": eventName}
)
