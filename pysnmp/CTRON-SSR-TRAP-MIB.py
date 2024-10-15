# SNMP MIB module (CTRON-SSR-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SSR-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:46 2024
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

(capCPUCurrentUtilization,) = mibBuilder.importSymbols(
    "CTRON-SSR-CAPACITY-MIB",
    "capCPUCurrentUtilization")

(sysHwFan,
 sysHwModuleSlotNumber,
 sysHwPowerSupply,
 sysHwTemperature) = mibBuilder.importSymbols(
    "CTRON-SSR-HARDWARE-MIB",
    "sysHwFan",
    "sysHwModuleSlotNumber",
    "sysHwPowerSupply",
    "sysHwTemperature")

(polAclItem,
 polAclName) = mibBuilder.importSymbols(
    "CTRON-SSR-POLICY-MIB",
    "polAclItem",
    "polAclName")

(ssrMibs,
 ssrTraps) = mibBuilder.importSymbols(
    "CTRON-SSR-SMI-MIB",
    "ssrMibs",
    "ssrTraps")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ssrTrapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300)
)
ssrTrapsMIB.setRevisions(
        ("2002-07-23 17:20",
         "2001-02-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SsrTrapsConformance_ObjectIdentity = ObjectIdentity
ssrTrapsConformance = _SsrTrapsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2)
)
_SsrTrapsCompliances_ObjectIdentity = ObjectIdentity
ssrTrapsCompliances = _SsrTrapsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 1)
)
_SsrTrapsGroups_ObjectIdentity = ObjectIdentity
ssrTrapsGroups = _SsrTrapsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2)
)
_TrapControl_ObjectIdentity = ObjectIdentity
trapControl = _TrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 1)
)
_EnvTrapGroup_ObjectIdentity = ObjectIdentity
envTrapGroup = _EnvTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2)
)
_PolTrapGroup_ObjectIdentity = ObjectIdentity
polTrapGroup = _PolTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 3)
)
_PolNotifications_ObjectIdentity = ObjectIdentity
polNotifications = _PolNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 3, 0)
)

# Managed Objects groups


# Notification objects

envPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 1)
)
envPowerSupplyFailed.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply")
)
if mibBuilder.loadTexts:
    envPowerSupplyFailed.setStatus(
        "current"
    )

envPowerSupplyRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 2)
)
envPowerSupplyRecovered.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply")
)
if mibBuilder.loadTexts:
    envPowerSupplyRecovered.setStatus(
        "current"
    )

envFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 3)
)
envFanFailed.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwFan")
)
if mibBuilder.loadTexts:
    envFanFailed.setStatus(
        "current"
    )

envFanRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 4)
)
envFanRecovered.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwFan")
)
if mibBuilder.loadTexts:
    envFanRecovered.setStatus(
        "current"
    )

envTempExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 5)
)
envTempExceeded.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature")
)
if mibBuilder.loadTexts:
    envTempExceeded.setStatus(
        "current"
    )

envTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 6)
)
envTempNormal.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature")
)
if mibBuilder.loadTexts:
    envTempNormal.setStatus(
        "current"
    )

envHotSwapIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 7)
)
envHotSwapIn.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber")
)
if mibBuilder.loadTexts:
    envHotSwapIn.setStatus(
        "current"
    )

envHotSwapOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 8)
)
envHotSwapOut.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber")
)
if mibBuilder.loadTexts:
    envHotSwapOut.setStatus(
        "current"
    )

envBackupControlModuleOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 9)
)
envBackupControlModuleOnline.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber")
)
if mibBuilder.loadTexts:
    envBackupControlModuleOnline.setStatus(
        "current"
    )

envBackupControlModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 10)
)
envBackupControlModuleFailure.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber")
)
if mibBuilder.loadTexts:
    envBackupControlModuleFailure.setStatus(
        "current"
    )

envLineModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 11)
)
envLineModuleFailure.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber")
)
if mibBuilder.loadTexts:
    envLineModuleFailure.setStatus(
        "current"
    )

envCPUThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 2, 12)
)
envCPUThresholdExceeded.setObjects(
      *(("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"),
        ("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization"))
)
if mibBuilder.loadTexts:
    envCPUThresholdExceeded.setStatus(
        "current"
    )

polAclDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 3, 0, 1)
)
polAclDenied.setObjects(
      *(("CTRON-SSR-POLICY-MIB", "polAclName"),
        ("CTRON-SSR-POLICY-MIB", "polAclItem"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    polAclDenied.setStatus(
        "current"
    )


# Notifications groups

ssrTrapsConfGroupV10 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 1)
)
ssrTrapsConfGroupV10.setObjects(
      *(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"),
        ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"))
)
if mibBuilder.loadTexts:
    ssrTrapsConfGroupV10.setStatus(
        "obsolete"
    )

ssrTrapsConfGroupV20 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 2)
)
ssrTrapsConfGroupV20.setObjects(
      *(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"),
        ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"),
        ("CTRON-SSR-TRAP-MIB", "envFanFailed"),
        ("CTRON-SSR-TRAP-MIB", "envFanRecovered"),
        ("CTRON-SSR-TRAP-MIB", "envTempExceeded"),
        ("CTRON-SSR-TRAP-MIB", "envTempNormal"))
)
if mibBuilder.loadTexts:
    ssrTrapsConfGroupV20.setStatus(
        "deprecated"
    )

ssrTrapsConfGroupV30 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 3)
)
ssrTrapsConfGroupV30.setObjects(
      *(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"),
        ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"),
        ("CTRON-SSR-TRAP-MIB", "envFanFailed"),
        ("CTRON-SSR-TRAP-MIB", "envFanRecovered"),
        ("CTRON-SSR-TRAP-MIB", "envTempExceeded"),
        ("CTRON-SSR-TRAP-MIB", "envTempNormal"),
        ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"),
        ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"))
)
if mibBuilder.loadTexts:
    ssrTrapsConfGroupV30.setStatus(
        "deprecated"
    )

ssrTrapsConfGroupV40 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 4)
)
ssrTrapsConfGroupV40.setObjects(
      *(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"),
        ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"),
        ("CTRON-SSR-TRAP-MIB", "envFanFailed"),
        ("CTRON-SSR-TRAP-MIB", "envFanRecovered"),
        ("CTRON-SSR-TRAP-MIB", "envTempExceeded"),
        ("CTRON-SSR-TRAP-MIB", "envTempNormal"),
        ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"),
        ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"),
        ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleOnline"),
        ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleFailure"),
        ("CTRON-SSR-TRAP-MIB", "envLineModuleFailure"),
        ("CTRON-SSR-TRAP-MIB", "envCPUThresholdExceeded"))
)
if mibBuilder.loadTexts:
    ssrTrapsConfGroupV40.setStatus(
        "deprecated"
    )

ssrTrapsConfGroupV50 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 5)
)
ssrTrapsConfGroupV50.setObjects(
      *(("CTRON-SSR-TRAP-MIB", "envPowerSupplyFailed"),
        ("CTRON-SSR-TRAP-MIB", "envPowerSupplyRecovered"),
        ("CTRON-SSR-TRAP-MIB", "envFanFailed"),
        ("CTRON-SSR-TRAP-MIB", "envFanRecovered"),
        ("CTRON-SSR-TRAP-MIB", "envTempExceeded"),
        ("CTRON-SSR-TRAP-MIB", "envTempNormal"),
        ("CTRON-SSR-TRAP-MIB", "envHotSwapIn"),
        ("CTRON-SSR-TRAP-MIB", "envHotSwapOut"),
        ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleOnline"),
        ("CTRON-SSR-TRAP-MIB", "envBackupControlModuleFailure"),
        ("CTRON-SSR-TRAP-MIB", "envLineModuleFailure"),
        ("CTRON-SSR-TRAP-MIB", "envCPUThresholdExceeded"),
        ("CTRON-SSR-TRAP-MIB", "polAclDenied"))
)
if mibBuilder.loadTexts:
    ssrTrapsConfGroupV50.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ssrTrapsComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ssrTrapsComplianceV10.setStatus(
        "obsolete"
    )

ssrTrapsComplianceV20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ssrTrapsComplianceV20.setStatus(
        "deprecated"
    )

ssrTrapsComplianceV30 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ssrTrapsComplianceV30.setStatus(
        "deprecated"
    )

ssrTrapsComplianceV40 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ssrTrapsComplianceV40.setStatus(
        "current"
    )

ssrTrapsComplianceV50 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 300, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ssrTrapsComplianceV50.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SSR-TRAP-MIB",
    **{"ssrTrapsMIB": ssrTrapsMIB,
       "ssrTrapsConformance": ssrTrapsConformance,
       "ssrTrapsCompliances": ssrTrapsCompliances,
       "ssrTrapsGroups": ssrTrapsGroups,
       "ssrTrapsConfGroupV10": ssrTrapsConfGroupV10,
       "ssrTrapsComplianceV10": ssrTrapsComplianceV10,
       "ssrTrapsConfGroupV20": ssrTrapsConfGroupV20,
       "ssrTrapsComplianceV20": ssrTrapsComplianceV20,
       "ssrTrapsConfGroupV30": ssrTrapsConfGroupV30,
       "ssrTrapsComplianceV30": ssrTrapsComplianceV30,
       "ssrTrapsConfGroupV40": ssrTrapsConfGroupV40,
       "ssrTrapsComplianceV40": ssrTrapsComplianceV40,
       "ssrTrapsConfGroupV50": ssrTrapsConfGroupV50,
       "ssrTrapsComplianceV50": ssrTrapsComplianceV50,
       "trapControl": trapControl,
       "envTrapGroup": envTrapGroup,
       "envPowerSupplyFailed": envPowerSupplyFailed,
       "envPowerSupplyRecovered": envPowerSupplyRecovered,
       "envFanFailed": envFanFailed,
       "envFanRecovered": envFanRecovered,
       "envTempExceeded": envTempExceeded,
       "envTempNormal": envTempNormal,
       "envHotSwapIn": envHotSwapIn,
       "envHotSwapOut": envHotSwapOut,
       "envBackupControlModuleOnline": envBackupControlModuleOnline,
       "envBackupControlModuleFailure": envBackupControlModuleFailure,
       "envLineModuleFailure": envLineModuleFailure,
       "envCPUThresholdExceeded": envCPUThresholdExceeded,
       "polTrapGroup": polTrapGroup,
       "polNotifications": polNotifications,
       "polAclDenied": polAclDenied}
)
