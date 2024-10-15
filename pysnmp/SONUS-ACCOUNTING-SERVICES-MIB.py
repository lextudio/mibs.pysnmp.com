# SNMP MIB module (SONUS-ACCOUNTING-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-ACCOUNTING-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:49 2024
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

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusServicesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusServicesMIBs")

(SonusAdminState,) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminState")


# MODULE-IDENTITY

sonusAccountingServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusAccountingServicesMIBObjects_ObjectIdentity = ObjectIdentity
sonusAccountingServicesMIBObjects = _SonusAccountingServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1)
)
_SonusCallAccountingObjects_ObjectIdentity = ObjectIdentity
sonusCallAccountingObjects = _SonusCallAccountingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1)
)
_SonusCallAccountingConfigObjects_ObjectIdentity = ObjectIdentity
sonusCallAccountingConfigObjects = _SonusCallAccountingConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 1)
)


class _SonusAcctGenerationMode_Type(Integer32):
    """Custom type sonusAcctGenerationMode based on Integer32"""
    defaultValue = 1

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
        *(("allcalls", 3),
          ("destination", 2),
          ("none", 4),
          ("origination", 1))
    )


_SonusAcctGenerationMode_Type.__name__ = "Integer32"
_SonusAcctGenerationMode_Object = MibScalar
sonusAcctGenerationMode = _SonusAcctGenerationMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 1, 1),
    _SonusAcctGenerationMode_Type()
)
sonusAcctGenerationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAcctGenerationMode.setStatus("current")


class _SonusAcctLogDestination_Type(Integer32):
    """Custom type sonusAcctLogDestination based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eventlog", 1)
    )


_SonusAcctLogDestination_Type.__name__ = "Integer32"
_SonusAcctLogDestination_Object = MibScalar
sonusAcctLogDestination = _SonusAcctLogDestination_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 1, 2),
    _SonusAcctLogDestination_Type()
)
sonusAcctLogDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAcctLogDestination.setStatus("current")


class _SonusAcctIntAcctState_Type(SonusAdminState):
    """Custom type sonusAcctIntAcctState based on SonusAdminState"""


_SonusAcctIntAcctState_Object = MibScalar
sonusAcctIntAcctState = _SonusAcctIntAcctState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 1, 3),
    _SonusAcctIntAcctState_Type()
)
sonusAcctIntAcctState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAcctIntAcctState.setStatus("current")


class _SonusAcctIntAcctInterval_Type(Integer32):
    """Custom type sonusAcctIntAcctInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_SonusAcctIntAcctInterval_Type.__name__ = "Integer32"
_SonusAcctIntAcctInterval_Object = MibScalar
sonusAcctIntAcctInterval = _SonusAcctIntAcctInterval_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 1, 4),
    _SonusAcctIntAcctInterval_Type()
)
sonusAcctIntAcctInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAcctIntAcctInterval.setStatus("current")
_SonusCallAccountingStatusObjects_ObjectIdentity = ObjectIdentity
sonusCallAccountingStatusObjects = _SonusCallAccountingStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 2)
)
_SonusAcctNumCallAttempts_Type = Counter64
_SonusAcctNumCallAttempts_Object = MibScalar
sonusAcctNumCallAttempts = _SonusAcctNumCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 2, 1),
    _SonusAcctNumCallAttempts_Type()
)
sonusAcctNumCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAcctNumCallAttempts.setStatus("current")
_SonusAcctNumCallCompletions_Type = Counter64
_SonusAcctNumCallCompletions_Object = MibScalar
sonusAcctNumCallCompletions = _SonusAcctNumCallCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 2, 2),
    _SonusAcctNumCallCompletions_Type()
)
sonusAcctNumCallCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAcctNumCallCompletions.setStatus("current")
_SonusAcctNumCallAttemptFailures_Type = Counter64
_SonusAcctNumCallAttemptFailures_Object = MibScalar
sonusAcctNumCallAttemptFailures = _SonusAcctNumCallAttemptFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 2, 3),
    _SonusAcctNumCallAttemptFailures_Type()
)
sonusAcctNumCallAttemptFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAcctNumCallAttemptFailures.setStatus("current")
_SonusAcctBusyHourAttempts_Type = Integer32
_SonusAcctBusyHourAttempts_Object = MibScalar
sonusAcctBusyHourAttempts = _SonusAcctBusyHourAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 2, 4),
    _SonusAcctBusyHourAttempts_Type()
)
sonusAcctBusyHourAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAcctBusyHourAttempts.setStatus("current")
_SonusAcctCallAttemptRate_Type = Integer32
_SonusAcctCallAttemptRate_Object = MibScalar
sonusAcctCallAttemptRate = _SonusAcctCallAttemptRate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 2, 5),
    _SonusAcctCallAttemptRate_Type()
)
sonusAcctCallAttemptRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAcctCallAttemptRate.setStatus("current")
_SonusAcctAvgCallDuration_Type = Integer32
_SonusAcctAvgCallDuration_Object = MibScalar
sonusAcctAvgCallDuration = _SonusAcctAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 2, 6),
    _SonusAcctAvgCallDuration_Type()
)
sonusAcctAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAcctAvgCallDuration.setStatus("current")
_SonusAcctNumCallAttemptBlocked_Type = Counter64
_SonusAcctNumCallAttemptBlocked_Object = MibScalar
sonusAcctNumCallAttemptBlocked = _SonusAcctNumCallAttemptBlocked_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 1, 1, 2, 7),
    _SonusAcctNumCallAttemptBlocked_Type()
)
sonusAcctNumCallAttemptBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAcctNumCallAttemptBlocked.setStatus("current")
_SonusAccountingMIBNotifications_ObjectIdentity = ObjectIdentity
sonusAccountingMIBNotifications = _SonusAccountingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 2)
)
_SonusAccountingMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusAccountingMIBNotificationsPrefix = _SonusAccountingMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 2, 0)
)
_SonusAccountingMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusAccountingMIBNotificationsObjects = _SonusAccountingMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 2, 1)
)


class _SonusAcctOutOfServiceReason_Type(Integer32):
    """Custom type sonusAcctOutOfServiceReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configChange", 1),
          ("eventLoggingError", 2))
    )


_SonusAcctOutOfServiceReason_Type.__name__ = "Integer32"
_SonusAcctOutOfServiceReason_Object = MibScalar
sonusAcctOutOfServiceReason = _SonusAcctOutOfServiceReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 2, 1, 1),
    _SonusAcctOutOfServiceReason_Type()
)
sonusAcctOutOfServiceReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAcctOutOfServiceReason.setStatus("current")

# Managed Objects groups


# Notification objects

sonusCallAccountingInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 2, 0, 1)
)
sonusCallAccountingInServiceNotification.setObjects(
      *(("SONUS-ACCOUNTING-SERVICES-MIB", "sonusAcctGenerationMode"),
        ("SONUS-ACCOUNTING-SERVICES-MIB", "sonusAcctLogDestination"),
        ("SONUS-ACCOUNTING-SERVICES-MIB", "sonusAcctIntAcctState"),
        ("SONUS-ACCOUNTING-SERVICES-MIB", "sonusAcctIntAcctInterval"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusCallAccountingInServiceNotification.setStatus(
        "current"
    )

sonusCallAccountingOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 5, 2, 0, 2)
)
sonusCallAccountingOutOfServiceNotification.setObjects(
      *(("SONUS-ACCOUNTING-SERVICES-MIB", "sonusAcctOutOfServiceReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusCallAccountingOutOfServiceNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-ACCOUNTING-SERVICES-MIB",
    **{"sonusAccountingServicesMIB": sonusAccountingServicesMIB,
       "sonusAccountingServicesMIBObjects": sonusAccountingServicesMIBObjects,
       "sonusCallAccountingObjects": sonusCallAccountingObjects,
       "sonusCallAccountingConfigObjects": sonusCallAccountingConfigObjects,
       "sonusAcctGenerationMode": sonusAcctGenerationMode,
       "sonusAcctLogDestination": sonusAcctLogDestination,
       "sonusAcctIntAcctState": sonusAcctIntAcctState,
       "sonusAcctIntAcctInterval": sonusAcctIntAcctInterval,
       "sonusCallAccountingStatusObjects": sonusCallAccountingStatusObjects,
       "sonusAcctNumCallAttempts": sonusAcctNumCallAttempts,
       "sonusAcctNumCallCompletions": sonusAcctNumCallCompletions,
       "sonusAcctNumCallAttemptFailures": sonusAcctNumCallAttemptFailures,
       "sonusAcctBusyHourAttempts": sonusAcctBusyHourAttempts,
       "sonusAcctCallAttemptRate": sonusAcctCallAttemptRate,
       "sonusAcctAvgCallDuration": sonusAcctAvgCallDuration,
       "sonusAcctNumCallAttemptBlocked": sonusAcctNumCallAttemptBlocked,
       "sonusAccountingMIBNotifications": sonusAccountingMIBNotifications,
       "sonusAccountingMIBNotificationsPrefix": sonusAccountingMIBNotificationsPrefix,
       "sonusCallAccountingInServiceNotification": sonusCallAccountingInServiceNotification,
       "sonusCallAccountingOutOfServiceNotification": sonusCallAccountingOutOfServiceNotification,
       "sonusAccountingMIBNotificationsObjects": sonusAccountingMIBNotificationsObjects,
       "sonusAcctOutOfServiceReason": sonusAcctOutOfServiceReason}
)
