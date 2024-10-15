# SNMP MIB module (BW-OpenClientServerFault) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-OpenClientServerFault
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:09 2024
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

(alarmName,
 alarmState,
 common,
 component,
 faultFields,
 identifier,
 problemText,
 recommendedActionsText,
 severity,
 subcomponent,
 systemName,
 timeStamp) = mibBuilder.importSymbols(
    "BroadworksFault",
    "alarmName",
    "alarmState",
    "common",
    "component",
    "faultFields",
    "identifier",
    "problemText",
    "recommendedActionsText",
    "severity",
    "subcomponent",
    "systemName",
    "timeStamp")

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


# MODULE-IDENTITY

systemFaults = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1)
)
systemFaults.setRevisions(
        ("2000-09-19 14:31",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

bwPMOpenClientServerLaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 501)
)
bwPMOpenClientServerLaunched.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMOpenClientServerLaunched.setStatus(
        "current"
    )

bwPMOpenClientServerShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 502)
)
bwPMOpenClientServerShutDown.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMOpenClientServerShutDown.setStatus(
        "current"
    )

bwPMOpenClientServerRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 503)
)
bwPMOpenClientServerRestarted.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMOpenClientServerRestarted.setStatus(
        "current"
    )

bwPMOpenClientServerDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 504)
)
bwPMOpenClientServerDeath.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMOpenClientServerDeath.setStatus(
        "current"
    )

bwPMOpenClientServerStartupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 505)
)
bwPMOpenClientServerStartupFailed.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMOpenClientServerStartupFailed.setStatus(
        "current"
    )

bwOpenClientServerNSConnFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 506)
)
bwOpenClientServerNSConnFailed.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwOpenClientServerNSConnFailed.setStatus(
        "current"
    )

bwOpenClientServerASConnFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 507)
)
bwOpenClientServerASConnFailed.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwOpenClientServerASConnFailed.setStatus(
        "current"
    )

bwOpenClientServerClientConnTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 508)
)
bwOpenClientServerClientConnTerminated.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwOpenClientServerClientConnTerminated.setStatus(
        "current"
    )

bwOpenClientServerASConnTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 509)
)
bwOpenClientServerASConnTerminated.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwOpenClientServerASConnTerminated.setStatus(
        "current"
    )

bwOpenClientServerNSConnTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 510)
)
bwOpenClientServerNSConnTerminated.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwOpenClientServerNSConnTerminated.setStatus(
        "current"
    )

bwOpenClientServerExtAuthConnFailedRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 511)
)
bwOpenClientServerExtAuthConnFailedRaise.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwOpenClientServerExtAuthConnFailedRaise.setStatus(
        "current"
    )

bwOpenClientServerExtAuthConnFailedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 512)
)
bwOpenClientServerExtAuthConnFailedClear.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwOpenClientServerExtAuthConnFailedClear.setStatus(
        "current"
    )

bwOpenClientServerExtAuthProcessingFailedRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 513)
)
bwOpenClientServerExtAuthProcessingFailedRaise.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwOpenClientServerExtAuthProcessingFailedRaise.setStatus(
        "current"
    )

bwOpenClientServerExtAuthProcessingFailedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 514)
)
bwOpenClientServerExtAuthProcessingFailedClear.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwOpenClientServerExtAuthProcessingFailedClear.setStatus(
        "current"
    )

bwOpenClientServerUserIdForceLoggedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 515)
)
bwOpenClientServerUserIdForceLoggedOut.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwOpenClientServerUserIdForceLoggedOut.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-OpenClientServerFault",
    **{"systemFaults": systemFaults,
       "bwPMOpenClientServerLaunched": bwPMOpenClientServerLaunched,
       "bwPMOpenClientServerShutDown": bwPMOpenClientServerShutDown,
       "bwPMOpenClientServerRestarted": bwPMOpenClientServerRestarted,
       "bwPMOpenClientServerDeath": bwPMOpenClientServerDeath,
       "bwPMOpenClientServerStartupFailed": bwPMOpenClientServerStartupFailed,
       "bwOpenClientServerNSConnFailed": bwOpenClientServerNSConnFailed,
       "bwOpenClientServerASConnFailed": bwOpenClientServerASConnFailed,
       "bwOpenClientServerClientConnTerminated": bwOpenClientServerClientConnTerminated,
       "bwOpenClientServerASConnTerminated": bwOpenClientServerASConnTerminated,
       "bwOpenClientServerNSConnTerminated": bwOpenClientServerNSConnTerminated,
       "bwOpenClientServerExtAuthConnFailedRaise": bwOpenClientServerExtAuthConnFailedRaise,
       "bwOpenClientServerExtAuthConnFailedClear": bwOpenClientServerExtAuthConnFailedClear,
       "bwOpenClientServerExtAuthProcessingFailedRaise": bwOpenClientServerExtAuthProcessingFailedRaise,
       "bwOpenClientServerExtAuthProcessingFailedClear": bwOpenClientServerExtAuthProcessingFailedClear,
       "bwOpenClientServerUserIdForceLoggedOut": bwOpenClientServerUserIdForceLoggedOut}
)
