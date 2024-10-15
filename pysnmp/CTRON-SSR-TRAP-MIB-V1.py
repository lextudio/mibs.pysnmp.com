# SNMP MIB module (CTRON-SSR-TRAP-MIB-V1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SSR-TRAP-MIB-V1
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

(sysHwFan,
 sysHwModuleSlotNumber,
 sysHwPowerSupply,
 sysHwTemperature) = mibBuilder.importSymbols(
    "CTRON-SSR-HARDWARE-MIB",
    "sysHwFan",
    "sysHwModuleSlotNumber",
    "sysHwPowerSupply",
    "sysHwTemperature")

(ssrTraps,) = mibBuilder.importSymbols(
    "CTRON-SSR-SMI-MIB",
    "ssrTraps")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

envPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 0, 1)
)
envPowerSupplyFailed.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply")
)
if mibBuilder.loadTexts:
    envPowerSupplyFailed.setStatus(
        ""
    )

envPowerSupplyRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 0, 2)
)
envPowerSupplyRecovered.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply")
)
if mibBuilder.loadTexts:
    envPowerSupplyRecovered.setStatus(
        ""
    )

envFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 0, 3)
)
envFanFailed.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwFan")
)
if mibBuilder.loadTexts:
    envFanFailed.setStatus(
        ""
    )

envFanRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 0, 4)
)
envFanRecovered.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwFan")
)
if mibBuilder.loadTexts:
    envFanRecovered.setStatus(
        ""
    )

envTempExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 0, 5)
)
envTempExceeded.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature")
)
if mibBuilder.loadTexts:
    envTempExceeded.setStatus(
        ""
    )

envTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 0, 6)
)
envTempNormal.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature")
)
if mibBuilder.loadTexts:
    envTempNormal.setStatus(
        ""
    )

envHotSwapIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 0, 7)
)
envHotSwapIn.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber")
)
if mibBuilder.loadTexts:
    envHotSwapIn.setStatus(
        ""
    )

envHotSwapOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 0, 8)
)
envHotSwapOut.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber")
)
if mibBuilder.loadTexts:
    envHotSwapOut.setStatus(
        ""
    )

envBackupControlModuleOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 2501, 10, 0, 9)
)
envBackupControlModuleOnline.setObjects(
    ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber")
)
if mibBuilder.loadTexts:
    envBackupControlModuleOnline.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SSR-TRAP-MIB-V1",
    **{"envPowerSupplyFailed": envPowerSupplyFailed,
       "envPowerSupplyRecovered": envPowerSupplyRecovered,
       "envFanFailed": envFanFailed,
       "envFanRecovered": envFanRecovered,
       "envTempExceeded": envTempExceeded,
       "envTempNormal": envTempNormal,
       "envHotSwapIn": envHotSwapIn,
       "envHotSwapOut": envHotSwapOut,
       "envBackupControlModuleOnline": envBackupControlModuleOnline}
)
