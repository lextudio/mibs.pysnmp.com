# SNMP MIB module (VPIEVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VPIEVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:06 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(software,
 voiceprint) = mibBuilder.importSymbols(
    "VPI-MIB",
    "software",
    "voiceprint")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eventcenter_ObjectIdentity = ObjectIdentity
eventcenter = _Eventcenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15191, 1, 1)
)


class _ApplicationId_Type(Integer32):
    """Custom type applicationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApplicationId_Type.__name__ = "Integer32"
_ApplicationId_Object = MibScalar
applicationId = _ApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 15191, 1, 1, 1),
    _ApplicationId_Type()
)
applicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationId.setStatus("mandatory")
_ApplicationName_Type = OctetString
_ApplicationName_Object = MibScalar
applicationName = _ApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 15191, 1, 1, 2),
    _ApplicationName_Type()
)
applicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationName.setStatus("mandatory")


class _ProcessName_Type(OctetString):
    """Custom type processName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_ProcessName_Type.__name__ = "OctetString"
_ProcessName_Object = MibScalar
processName = _ProcessName_Object(
    (1, 3, 6, 1, 4, 1, 15191, 1, 1, 3),
    _ProcessName_Type()
)
processName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processName.setStatus("mandatory")
_LogEventType_Type = Integer32
_LogEventType_Object = MibScalar
logEventType = _LogEventType_Object(
    (1, 3, 6, 1, 4, 1, 15191, 1, 1, 4),
    _LogEventType_Type()
)
logEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventType.setStatus("mandatory")
_LogEventName_Type = OctetString
_LogEventName_Object = MibScalar
logEventName = _LogEventName_Object(
    (1, 3, 6, 1, 4, 1, 15191, 1, 1, 5),
    _LogEventName_Type()
)
logEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventName.setStatus("mandatory")


class _LogEventMessage_Type(OctetString):
    """Custom type logEventMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_LogEventMessage_Type.__name__ = "OctetString"
_LogEventMessage_Object = MibScalar
logEventMessage = _LogEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 15191, 1, 1, 6),
    _LogEventMessage_Type()
)
logEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventMessage.setStatus("mandatory")

# Managed Objects groups


# Notification objects

eventNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 15191, 0, 0)
)
eventNotif.setObjects(
      *(("VPIEVENT-MIB", "applicationId"),
        ("VPIEVENT-MIB", "applicationName"),
        ("VPIEVENT-MIB", "processName"),
        ("VPIEVENT-MIB", "logEventType"),
        ("VPIEVENT-MIB", "logEventName"),
        ("VPIEVENT-MIB", "logEventMessage"))
)
if mibBuilder.loadTexts:
    eventNotif.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPIEVENT-MIB",
    **{"eventNotif": eventNotif,
       "eventcenter": eventcenter,
       "applicationId": applicationId,
       "applicationName": applicationName,
       "processName": processName,
       "logEventType": logEventType,
       "logEventName": logEventName,
       "logEventMessage": logEventMessage}
)
