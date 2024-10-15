# SNMP MIB module (VERTICAL-EVENTLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERTICAL-EVENTLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:21 2024
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vertical_ObjectIdentity = ObjectIdentity
vertical = _Vertical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338)
)
_EventLog_ObjectIdentity = ObjectIdentity
eventLog = _EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 13)
)
_EventLogTrapInfoGroup_ObjectIdentity = ObjectIdentity
eventLogTrapInfoGroup = _EventLogTrapInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 13, 1)
)


class _LastTrapLogType_Type(Integer32):
    """Custom type lastTrapLogType based on Integer32"""
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
        *(("application", 3),
          ("security", 2),
          ("system", 1),
          ("unknown", 4))
    )


_LastTrapLogType_Type.__name__ = "Integer32"
_LastTrapLogType_Object = MibScalar
lastTrapLogType = _LastTrapLogType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 13, 1, 1),
    _LastTrapLogType_Type()
)
lastTrapLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTrapLogType.setStatus("mandatory")


class _LastTrapEventType_Type(Integer32):
    """Custom type lastTrapEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("audit-fail", 5),
          ("audit-success", 4),
          ("error", 1),
          ("information", 3),
          ("unknown", 6),
          ("warning", 2))
    )


_LastTrapEventType_Type.__name__ = "Integer32"
_LastTrapEventType_Object = MibScalar
lastTrapEventType = _LastTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 13, 1, 2),
    _LastTrapEventType_Type()
)
lastTrapEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTrapEventType.setStatus("mandatory")


class _LastTrapInfoString_Type(OctetString):
    """Custom type lastTrapInfoString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LastTrapInfoString_Type.__name__ = "OctetString"
_LastTrapInfoString_Object = MibScalar
lastTrapInfoString = _LastTrapInfoString_Object(
    (1, 3, 6, 1, 4, 1, 2338, 13, 1, 3),
    _LastTrapInfoString_Type()
)
lastTrapInfoString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTrapInfoString.setStatus("mandatory")

# Managed Objects groups


# Notification objects

eventLog_FailedToStartSTD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 53)
)
eventLog_FailedToStartSTD.setObjects(
      *(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
)
if mibBuilder.loadTexts:
    eventLog_FailedToStartSTD.setStatus(
        ""
    )

eventLog_FailedToStopSTD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 54)
)
eventLog_FailedToStopSTD.setObjects(
      *(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
)
if mibBuilder.loadTexts:
    eventLog_FailedToStopSTD.setStatus(
        ""
    )

eventLog_CannotCreateUserTracePipe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 55)
)
eventLog_CannotCreateUserTracePipe.setObjects(
      *(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
)
if mibBuilder.loadTexts:
    eventLog_CannotCreateUserTracePipe.setStatus(
        ""
    )

eventLog_CannotConnectUserTracePipe = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 56)
)
eventLog_CannotConnectUserTracePipe.setObjects(
      *(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
)
if mibBuilder.loadTexts:
    eventLog_CannotConnectUserTracePipe.setStatus(
        ""
    )

eventLog_VoiceMailDiskIsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 57)
)
eventLog_VoiceMailDiskIsFull.setObjects(
      *(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
)
if mibBuilder.loadTexts:
    eventLog_VoiceMailDiskIsFull.setStatus(
        ""
    )

eventLog_SystemDiskIsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 58)
)
eventLog_SystemDiskIsFull.setObjects(
      *(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
)
if mibBuilder.loadTexts:
    eventLog_SystemDiskIsFull.setStatus(
        ""
    )

eventLog_SecurityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 59)
)
eventLog_SecurityError.setObjects(
      *(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
)
if mibBuilder.loadTexts:
    eventLog_SecurityError.setStatus(
        ""
    )

eventLog_SecuritySuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 60)
)
eventLog_SecuritySuccess.setObjects(
      *(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
)
if mibBuilder.loadTexts:
    eventLog_SecuritySuccess.setStatus(
        ""
    )

eventLog_GenericEventLogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 61)
)
eventLog_GenericEventLogTrap.setObjects(
      *(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"),
        ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
)
if mibBuilder.loadTexts:
    eventLog_GenericEventLogTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTICAL-EVENTLOG-MIB",
    **{"vertical": vertical,
       "eventLog-FailedToStartSTD": eventLog_FailedToStartSTD,
       "eventLog-FailedToStopSTD": eventLog_FailedToStopSTD,
       "eventLog-CannotCreateUserTracePipe": eventLog_CannotCreateUserTracePipe,
       "eventLog-CannotConnectUserTracePipe": eventLog_CannotConnectUserTracePipe,
       "eventLog-VoiceMailDiskIsFull": eventLog_VoiceMailDiskIsFull,
       "eventLog-SystemDiskIsFull": eventLog_SystemDiskIsFull,
       "eventLog-SecurityError": eventLog_SecurityError,
       "eventLog-SecuritySuccess": eventLog_SecuritySuccess,
       "eventLog-GenericEventLogTrap": eventLog_GenericEventLogTrap,
       "eventLog": eventLog,
       "eventLogTrapInfoGroup": eventLogTrapInfoGroup,
       "lastTrapLogType": lastTrapLogType,
       "lastTrapEventType": lastTrapEventType,
       "lastTrapInfoString": lastTrapInfoString}
)
