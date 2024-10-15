# SNMP MIB module (EXTREME-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeV1Traps,
 extremenetworks) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeV1Traps",
    "extremenetworks")

(extremeEdpEntryAge,
 extremeEdpNeighborId,
 extremeEdpNeighborVlanIpAddress,
 extremeEdpNeighborVlanName,
 extremeEdpPortIfIndex) = mibBuilder.importSymbols(
    "EXTREME-EDP-MIB",
    "extremeEdpEntryAge",
    "extremeEdpNeighborId",
    "extremeEdpNeighborVlanIpAddress",
    "extremeEdpNeighborVlanName",
    "extremeEdpPortIfIndex")

(extremeEsrpActivePorts,
 extremeEsrpGroup,
 extremeEsrpInternalActivePorts,
 extremeEsrpNetAddress,
 extremeEsrpState,
 extremeEsrpTrackedActivePorts,
 extremeEsrpTrackedIpRoutes) = mibBuilder.importSymbols(
    "EXTREME-ESRP-MIB",
    "extremeEsrpActivePorts",
    "extremeEsrpGroup",
    "extremeEsrpInternalActivePorts",
    "extremeEsrpNetAddress",
    "extremeEsrpState",
    "extremeEsrpTrackedActivePorts",
    "extremeEsrpTrackedIpRoutes")

(extremeCurrentTemperature,
 extremeFanNumber,
 extremePowerSupplyNumber,
 extremeSlotModuleConfiguredType,
 extremeSlotModuleInsertedType,
 extremeSlotModuleState,
 extremeSlotNumber) = mibBuilder.importSymbols(
    "EXTREME-SYSTEM-MIB",
    "extremeCurrentTemperature",
    "extremeFanNumber",
    "extremePowerSupplyNumber",
    "extremeSlotModuleConfiguredType",
    "extremeSlotModuleInsertedType",
    "extremeSlotModuleState",
    "extremeSlotNumber")

(extremeVlanIfDescr,
 extremeVlanIfIndex) = mibBuilder.importSymbols(
    "EXTREME-VLAN-MIB",
    "extremeVlanIfDescr",
    "extremeVlanIfIndex")

(ifAlias,
 ifDescr,
 ifPhysAddress) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias",
    "ifDescr",
    "ifPhysAddress")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

extremeOverheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 6)
)
extremeOverheat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeCurrentTemperature"))
)
if mibBuilder.loadTexts:
    extremeOverheat.setStatus(
        "current"
    )

extremeFanfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 7)
)
extremeFanfailed.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeFanNumber"))
)
if mibBuilder.loadTexts:
    extremeFanfailed.setStatus(
        "current"
    )

extremeFanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 8)
)
extremeFanOK.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremeFanNumber"))
)
if mibBuilder.loadTexts:
    extremeFanOK.setStatus(
        "current"
    )

extremeInvalidLoginAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 9)
)
extremeInvalidLoginAttempt.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    extremeInvalidLoginAttempt.setStatus(
        "current"
    )

extremePowerSupplyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 10)
)
extremePowerSupplyFail.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremePowerSupplyNumber"))
)
if mibBuilder.loadTexts:
    extremePowerSupplyFail.setStatus(
        "current"
    )

extremePowerSupplyGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 11)
)
extremePowerSupplyGood.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-SYSTEM-MIB", "extremePowerSupplyNumber"))
)
if mibBuilder.loadTexts:
    extremePowerSupplyGood.setStatus(
        "current"
    )

extremeRpsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 12)
)
extremeRpsAlarm.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    extremeRpsAlarm.setStatus(
        "current"
    )

extremeRpsNoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 13)
)
extremeRpsNoAlarm.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    extremeRpsNoAlarm.setStatus(
        "current"
    )

extremeSmartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 14)
)
extremeSmartTrap.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    extremeSmartTrap.setStatus(
        "current"
    )

extremeModuleStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 15)
)
extremeModuleStateChanged.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotNumber"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotModuleConfiguredType"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotModuleInsertedType"),
        ("EXTREME-SYSTEM-MIB", "extremeSlotModuleState"))
)
if mibBuilder.loadTexts:
    extremeModuleStateChanged.setStatus(
        "current"
    )

extremeEsrpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 17)
)
extremeEsrpStateChange.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"),
        ("EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
        ("EXTREME-VLAN-MIB", "extremeVlanIfDescr"),
        ("EXTREME-ESRP-MIB", "extremeEsrpGroup"),
        ("EXTREME-ESRP-MIB", "extremeEsrpState"),
        ("EXTREME-ESRP-MIB", "extremeEsrpNetAddress"),
        ("IF-MIB", "ifPhysAddress"),
        ("EXTREME-ESRP-MIB", "extremeEsrpActivePorts"),
        ("EXTREME-ESRP-MIB", "extremeEsrpInternalActivePorts"),
        ("EXTREME-ESRP-MIB", "extremeEsrpTrackedActivePorts"),
        ("EXTREME-ESRP-MIB", "extremeEsrpTrackedIpRoutes"))
)
if mibBuilder.loadTexts:
    extremeEsrpStateChange.setStatus(
        "current"
    )

extremeSlbUnitAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 18)
)
if mibBuilder.loadTexts:
    extremeSlbUnitAdded.setStatus(
        "current"
    )

extremeSlbUnitRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 19)
)
if mibBuilder.loadTexts:
    extremeSlbUnitRemoved.setStatus(
        "current"
    )

extremeEdpNeighborAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 20)
)
extremeEdpNeighborAdded.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("EXTREME-EDP-MIB", "extremeEdpPortIfIndex"),
        ("EXTREME-EDP-MIB", "extremeEdpNeighborId"),
        ("EXTREME-EDP-MIB", "extremeEdpEntryAge"),
        ("IF-MIB", "ifAlias"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    extremeEdpNeighborAdded.setStatus(
        "current"
    )

extremeEdpNeighborRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 21)
)
extremeEdpNeighborRemoved.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("EXTREME-EDP-MIB", "extremeEdpPortIfIndex"),
        ("EXTREME-EDP-MIB", "extremeEdpNeighborId"),
        ("EXTREME-EDP-MIB", "extremeEdpEntryAge"),
        ("IF-MIB", "ifAlias"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    extremeEdpNeighborRemoved.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-TRAP-MIB",
    **{"extremeOverheat": extremeOverheat,
       "extremeFanfailed": extremeFanfailed,
       "extremeFanOK": extremeFanOK,
       "extremeInvalidLoginAttempt": extremeInvalidLoginAttempt,
       "extremePowerSupplyFail": extremePowerSupplyFail,
       "extremePowerSupplyGood": extremePowerSupplyGood,
       "extremeRpsAlarm": extremeRpsAlarm,
       "extremeRpsNoAlarm": extremeRpsNoAlarm,
       "extremeSmartTrap": extremeSmartTrap,
       "extremeModuleStateChanged": extremeModuleStateChanged,
       "extremeEsrpStateChange": extremeEsrpStateChange,
       "extremeSlbUnitAdded": extremeSlbUnitAdded,
       "extremeSlbUnitRemoved": extremeSlbUnitRemoved,
       "extremeEdpNeighborAdded": extremeEdpNeighborAdded,
       "extremeEdpNeighborRemoved": extremeEdpNeighborRemoved}
)
