# SNMP MIB module (HALCYON-PRIMEALERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HALCYON-PRIMEALERT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:00 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

primealert = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1242, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1242, 1, 0)
)
_Base_ObjectIdentity = ObjectIdentity
base = _Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1)
)
_TrapInfo_ObjectIdentity = ObjectIdentity
trapInfo = _TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1, 3)
)


class _EventHost_Type(DisplayString):
    """Custom type eventHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EventHost_Type.__name__ = "DisplayString"
_EventHost_Object = MibScalar
eventHost = _EventHost_Object(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 6),
    _EventHost_Type()
)
eventHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventHost.setStatus("current")
_EventPort_Type = Integer32
_EventPort_Object = MibScalar
eventPort = _EventPort_Object(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 7),
    _EventPort_Type()
)
eventPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventPort.setStatus("current")


class _EventModule_Type(DisplayString):
    """Custom type eventModule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EventModule_Type.__name__ = "DisplayString"
_EventModule_Object = MibScalar
eventModule = _EventModule_Object(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 8),
    _EventModule_Type()
)
eventModule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventModule.setStatus("current")


class _EventContext_Type(DisplayString):
    """Custom type eventContext based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EventContext_Type.__name__ = "DisplayString"
_EventContext_Object = MibScalar
eventContext = _EventContext_Object(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 9),
    _EventContext_Type()
)
eventContext.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventContext.setStatus("current")


class _EventSeverity_Type(DisplayString):
    """Custom type eventSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EventSeverity_Type.__name__ = "DisplayString"
_EventSeverity_Object = MibScalar
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 10),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")


class _EventMessage_Type(DisplayString):
    """Custom type eventMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EventMessage_Type.__name__ = "DisplayString"
_EventMessage_Object = MibScalar
eventMessage = _EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 11),
    _EventMessage_Type()
)
eventMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventMessage.setStatus("current")


class _EventUrl_Type(DisplayString):
    """Custom type eventUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EventUrl_Type.__name__ = "DisplayString"
_EventUrl_Object = MibScalar
eventUrl = _EventUrl_Object(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 12),
    _EventUrl_Type()
)
eventUrl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventUrl.setStatus("current")


class _EventOpenTime_Type(DisplayString):
    """Custom type eventOpenTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EventOpenTime_Type.__name__ = "DisplayString"
_EventOpenTime_Object = MibScalar
eventOpenTime = _EventOpenTime_Object(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 13),
    _EventOpenTime_Type()
)
eventOpenTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventOpenTime.setStatus("current")


class _EventCloseTime_Type(DisplayString):
    """Custom type eventCloseTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EventCloseTime_Type.__name__ = "DisplayString"
_EventCloseTime_Object = MibScalar
eventCloseTime = _EventCloseTime_Object(
    (1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 14),
    _EventCloseTime_Type()
)
eventCloseTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventCloseTime.setStatus("current")

# Managed Objects groups


# Notification objects

eventOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1242, 1, 0, 9)
)
eventOpenTrap.setObjects(
      *(("HALCYON-PRIMEALERT-MIB", "eventHost"),
        ("HALCYON-PRIMEALERT-MIB", "eventPort"),
        ("HALCYON-PRIMEALERT-MIB", "eventModule"),
        ("HALCYON-PRIMEALERT-MIB", "eventContext"),
        ("HALCYON-PRIMEALERT-MIB", "eventSeverity"),
        ("HALCYON-PRIMEALERT-MIB", "eventMessage"),
        ("HALCYON-PRIMEALERT-MIB", "eventUrl"),
        ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"),
        ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
)
if mibBuilder.loadTexts:
    eventOpenTrap.setStatus(
        "current"
    )

eventCloseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1242, 1, 0, 10)
)
eventCloseTrap.setObjects(
      *(("HALCYON-PRIMEALERT-MIB", "eventHost"),
        ("HALCYON-PRIMEALERT-MIB", "eventPort"),
        ("HALCYON-PRIMEALERT-MIB", "eventModule"),
        ("HALCYON-PRIMEALERT-MIB", "eventContext"),
        ("HALCYON-PRIMEALERT-MIB", "eventSeverity"),
        ("HALCYON-PRIMEALERT-MIB", "eventMessage"),
        ("HALCYON-PRIMEALERT-MIB", "eventUrl"),
        ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"),
        ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
)
if mibBuilder.loadTexts:
    eventCloseTrap.setStatus(
        "current"
    )

eventLogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1242, 1, 0, 11)
)
eventLogTrap.setObjects(
      *(("HALCYON-PRIMEALERT-MIB", "eventHost"),
        ("HALCYON-PRIMEALERT-MIB", "eventPort"),
        ("HALCYON-PRIMEALERT-MIB", "eventModule"),
        ("HALCYON-PRIMEALERT-MIB", "eventContext"),
        ("HALCYON-PRIMEALERT-MIB", "eventSeverity"),
        ("HALCYON-PRIMEALERT-MIB", "eventMessage"),
        ("HALCYON-PRIMEALERT-MIB", "eventUrl"),
        ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"),
        ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
)
if mibBuilder.loadTexts:
    eventLogTrap.setStatus(
        "current"
    )

eventColdstartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1242, 1, 0, 12)
)
eventColdstartTrap.setObjects(
      *(("HALCYON-PRIMEALERT-MIB", "eventHost"),
        ("HALCYON-PRIMEALERT-MIB", "eventPort"),
        ("HALCYON-PRIMEALERT-MIB", "eventModule"),
        ("HALCYON-PRIMEALERT-MIB", "eventContext"),
        ("HALCYON-PRIMEALERT-MIB", "eventSeverity"),
        ("HALCYON-PRIMEALERT-MIB", "eventMessage"),
        ("HALCYON-PRIMEALERT-MIB", "eventUrl"),
        ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"),
        ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
)
if mibBuilder.loadTexts:
    eventColdstartTrap.setStatus(
        "current"
    )

eventAcknowledgeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1242, 1, 0, 13)
)
eventAcknowledgeTrap.setObjects(
      *(("HALCYON-PRIMEALERT-MIB", "eventHost"),
        ("HALCYON-PRIMEALERT-MIB", "eventPort"),
        ("HALCYON-PRIMEALERT-MIB", "eventModule"),
        ("HALCYON-PRIMEALERT-MIB", "eventContext"),
        ("HALCYON-PRIMEALERT-MIB", "eventSeverity"),
        ("HALCYON-PRIMEALERT-MIB", "eventMessage"),
        ("HALCYON-PRIMEALERT-MIB", "eventUrl"),
        ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"),
        ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
)
if mibBuilder.loadTexts:
    eventAcknowledgeTrap.setStatus(
        "current"
    )

eventUnAcknowledgeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1242, 1, 0, 14)
)
eventUnAcknowledgeTrap.setObjects(
      *(("HALCYON-PRIMEALERT-MIB", "eventHost"),
        ("HALCYON-PRIMEALERT-MIB", "eventPort"),
        ("HALCYON-PRIMEALERT-MIB", "eventModule"),
        ("HALCYON-PRIMEALERT-MIB", "eventContext"),
        ("HALCYON-PRIMEALERT-MIB", "eventSeverity"),
        ("HALCYON-PRIMEALERT-MIB", "eventMessage"),
        ("HALCYON-PRIMEALERT-MIB", "eventUrl"),
        ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"),
        ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
)
if mibBuilder.loadTexts:
    eventUnAcknowledgeTrap.setStatus(
        "current"
    )

eventModuleUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1242, 1, 0, 15)
)
eventModuleUnavailableTrap.setObjects(
      *(("HALCYON-PRIMEALERT-MIB", "eventHost"),
        ("HALCYON-PRIMEALERT-MIB", "eventPort"),
        ("HALCYON-PRIMEALERT-MIB", "eventModule"),
        ("HALCYON-PRIMEALERT-MIB", "eventContext"),
        ("HALCYON-PRIMEALERT-MIB", "eventSeverity"),
        ("HALCYON-PRIMEALERT-MIB", "eventMessage"),
        ("HALCYON-PRIMEALERT-MIB", "eventUrl"),
        ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"),
        ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
)
if mibBuilder.loadTexts:
    eventModuleUnavailableTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HALCYON-PRIMEALERT-MIB",
    **{"primealert": primealert,
       "traps": traps,
       "eventOpenTrap": eventOpenTrap,
       "eventCloseTrap": eventCloseTrap,
       "eventLogTrap": eventLogTrap,
       "eventColdstartTrap": eventColdstartTrap,
       "eventAcknowledgeTrap": eventAcknowledgeTrap,
       "eventUnAcknowledgeTrap": eventUnAcknowledgeTrap,
       "eventModuleUnavailableTrap": eventModuleUnavailableTrap,
       "base": base,
       "trapInfo": trapInfo,
       "eventHost": eventHost,
       "eventPort": eventPort,
       "eventModule": eventModule,
       "eventContext": eventContext,
       "eventSeverity": eventSeverity,
       "eventMessage": eventMessage,
       "eventUrl": eventUrl,
       "eventOpenTime": eventOpenTime,
       "eventCloseTime": eventCloseTime}
)
