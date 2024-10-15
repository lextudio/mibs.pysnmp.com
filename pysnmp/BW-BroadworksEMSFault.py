# SNMP MIB module (BW-BroadworksEMSFault) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-BroadworksEMSFault
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:03 2024
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

bwPMElementManagementSystemBELaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3001)
)
bwPMElementManagementSystemBELaunched.setObjects(
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
    bwPMElementManagementSystemBELaunched.setStatus(
        "current"
    )

bwPMElementManagementSystemBEShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3002)
)
bwPMElementManagementSystemBEShutDown.setObjects(
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
    bwPMElementManagementSystemBEShutDown.setStatus(
        "current"
    )

bwPMElementManagementSystemBERestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3003)
)
bwPMElementManagementSystemBERestarted.setObjects(
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
    bwPMElementManagementSystemBERestarted.setStatus(
        "current"
    )

bwPMElementManagementSystemBEDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3004)
)
bwPMElementManagementSystemBEDeath.setObjects(
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
    bwPMElementManagementSystemBEDeath.setStatus(
        "current"
    )

bwPMElementManagementSystemFELaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3005)
)
bwPMElementManagementSystemFELaunched.setObjects(
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
    bwPMElementManagementSystemFELaunched.setStatus(
        "current"
    )

bwPMElementManagementSystemFEShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3006)
)
bwPMElementManagementSystemFEShutDown.setObjects(
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
    bwPMElementManagementSystemFEShutDown.setStatus(
        "current"
    )

bwPMElementManagementSystemFERestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3007)
)
bwPMElementManagementSystemFERestarted.setObjects(
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
    bwPMElementManagementSystemFERestarted.setStatus(
        "current"
    )

bwPMElementManagementSystemFEDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3008)
)
bwPMElementManagementSystemFEDeath.setObjects(
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
    bwPMElementManagementSystemFEDeath.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-BroadworksEMSFault",
    **{"systemFaults": systemFaults,
       "bwPMElementManagementSystemBELaunched": bwPMElementManagementSystemBELaunched,
       "bwPMElementManagementSystemBEShutDown": bwPMElementManagementSystemBEShutDown,
       "bwPMElementManagementSystemBERestarted": bwPMElementManagementSystemBERestarted,
       "bwPMElementManagementSystemBEDeath": bwPMElementManagementSystemBEDeath,
       "bwPMElementManagementSystemFELaunched": bwPMElementManagementSystemFELaunched,
       "bwPMElementManagementSystemFEShutDown": bwPMElementManagementSystemFEShutDown,
       "bwPMElementManagementSystemFERestarted": bwPMElementManagementSystemFERestarted,
       "bwPMElementManagementSystemFEDeath": bwPMElementManagementSystemFEDeath}
)
