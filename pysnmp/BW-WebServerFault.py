# SNMP MIB module (BW-WebServerFault) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-WebServerFault
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:10 2024
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

bwApplicationServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2501)
)
bwApplicationServerUnreachable.setObjects(
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
    bwApplicationServerUnreachable.setStatus(
        "current"
    )

bwNetworkServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2502)
)
bwNetworkServerUnreachable.setObjects(
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
    bwNetworkServerUnreachable.setStatus(
        "current"
    )

bwNetworkServerRequestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2503)
)
bwNetworkServerRequestError.setObjects(
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
    bwNetworkServerRequestError.setStatus(
        "current"
    )

bwCMSConnectivityDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2504)
)
bwCMSConnectivityDown.setObjects(
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
    bwCMSConnectivityDown.setStatus(
        "current"
    )

bwCMSConnectivityUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2505)
)
bwCMSConnectivityUp.setObjects(
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
    bwCMSConnectivityUp.setStatus(
        "current"
    )

bwCMSDatabaseMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2506)
)
bwCMSDatabaseMismatch.setObjects(
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
    bwCMSDatabaseMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-WebServerFault",
    **{"systemFaults": systemFaults,
       "bwApplicationServerUnreachable": bwApplicationServerUnreachable,
       "bwNetworkServerUnreachable": bwNetworkServerUnreachable,
       "bwNetworkServerRequestError": bwNetworkServerRequestError,
       "bwCMSConnectivityDown": bwCMSConnectivityDown,
       "bwCMSConnectivityUp": bwCMSConnectivityUp,
       "bwCMSDatabaseMismatch": bwCMSDatabaseMismatch}
)
