# SNMP MIB module (BAS-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:37 2024
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

(basTrapCardType,
 basTrapChassis,
 basTrapChassisNumber,
 basTrapCmtsCmGwAddress,
 basTrapCmtsCmIpAddress,
 basTrapCmtsCmMacAddress,
 basTrapCraftIpAddress,
 basTrapIclClass,
 basTrapIf,
 basTrapLPort,
 basTrapMgmtOneIpAddress,
 basTrapMgmtTwoIpAddress,
 basTrapSlot,
 basTrapSubnetType,
 basTraps) = mibBuilder.importSymbols(
    "BAS-MIB",
    "basTrapCardType",
    "basTrapChassis",
    "basTrapChassisNumber",
    "basTrapCmtsCmGwAddress",
    "basTrapCmtsCmIpAddress",
    "basTrapCmtsCmMacAddress",
    "basTrapCraftIpAddress",
    "basTrapIclClass",
    "basTrapIf",
    "basTrapLPort",
    "basTrapMgmtOneIpAddress",
    "basTrapMgmtTwoIpAddress",
    "basTrapSlot",
    "basTrapSubnetType",
    "basTraps")

(basTraceLogLevel,
 basTraceLogNotifyComponentId,
 basTraceLogNotifyString) = mibBuilder.importSymbols(
    "BAS-TRACE-MIB",
    "basTraceLogLevel",
    "basTraceLogNotifyComponentId",
    "basTraceLogNotifyString")

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

basTrapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

basCardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 1)
)
basCardDown.setObjects(
      *(("BAS-MIB", "basTrapChassis"),
        ("BAS-MIB", "basTrapSlot"),
        ("BAS-MIB", "basTrapIf"),
        ("BAS-MIB", "basTrapLPort"),
        ("BAS-MIB", "basTrapCardType"))
)
if mibBuilder.loadTexts:
    basCardDown.setStatus(
        "current"
    )

basCardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 2)
)
basCardUp.setObjects(
      *(("BAS-MIB", "basTrapChassis"),
        ("BAS-MIB", "basTrapSlot"),
        ("BAS-MIB", "basTrapIf"),
        ("BAS-MIB", "basTrapLPort"),
        ("BAS-MIB", "basTrapCardType"))
)
if mibBuilder.loadTexts:
    basCardUp.setStatus(
        "current"
    )

basTraceLogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 3)
)
basTraceLogTrap.setObjects(
      *(("BAS-MIB", "basTrapChassis"),
        ("BAS-MIB", "basTrapSlot"),
        ("BAS-MIB", "basTrapIf"),
        ("BAS-MIB", "basTrapLPort"),
        ("BAS-TRACE-MIB", "basTraceLogNotifyComponentId"),
        ("BAS-TRACE-MIB", "basTraceLogLevel"),
        ("BAS-TRACE-MIB", "basTraceLogNotifyString"))
)
if mibBuilder.loadTexts:
    basTraceLogTrap.setStatus(
        "current"
    )

basCmtsCmUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 4)
)
basCmtsCmUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BAS-MIB", "basTrapCmtsCmMacAddress"),
        ("BAS-MIB", "basTrapCmtsCmIpAddress"))
)
if mibBuilder.loadTexts:
    basCmtsCmUp.setStatus(
        "current"
    )

basCmtsCmDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 5)
)
basCmtsCmDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BAS-MIB", "basTrapCmtsCmMacAddress"),
        ("BAS-MIB", "basTrapCmtsCmIpAddress"))
)
if mibBuilder.loadTexts:
    basCmtsCmDown.setStatus(
        "current"
    )

basBcmStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 6)
)
basBcmStateChange.setObjects(
      *(("BAS-MIB", "basTrapChassis"),
        ("BAS-MIB", "basTrapSlot"),
        ("BAS-MIB", "basTrapIf"),
        ("BAS-MIB", "basTrapLPort"),
        ("BAS-MIB", "basTrapMgmtOneIpAddress"),
        ("BAS-MIB", "basTrapMgmtTwoIpAddress"),
        ("BAS-MIB", "basTrapCraftIpAddress"))
)
if mibBuilder.loadTexts:
    basBcmStateChange.setStatus(
        "current"
    )

basIclStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 7)
)
basIclStateChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BAS-MIB", "basTrapIclClass"),
        ("BAS-MIB", "basTrapChassisNumber"),
        ("BAS-MIB", "basTrapChassis"),
        ("BAS-MIB", "basTrapSlot"),
        ("BAS-MIB", "basTrapIf"),
        ("BAS-MIB", "basTrapLPort"))
)
if mibBuilder.loadTexts:
    basIclStateChange.setStatus(
        "current"
    )

basSoftwareComponentUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 8)
)
basSoftwareComponentUp.setObjects(
      *(("BAS-MIB", "basTrapChassis"),
        ("BAS-MIB", "basTrapSlot"),
        ("BAS-MIB", "basTrapIf"),
        ("BAS-MIB", "basTrapLPort"),
        ("BAS-TRACE-MIB", "basTraceLogNotifyComponentId"))
)
if mibBuilder.loadTexts:
    basSoftwareComponentUp.setStatus(
        "current"
    )

basSoftwareComponentDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 9)
)
basSoftwareComponentDown.setObjects(
      *(("BAS-MIB", "basTrapChassis"),
        ("BAS-MIB", "basTrapSlot"),
        ("BAS-MIB", "basTrapIf"),
        ("BAS-MIB", "basTrapLPort"),
        ("BAS-TRACE-MIB", "basTraceLogNotifyComponentId"))
)
if mibBuilder.loadTexts:
    basSoftwareComponentDown.setStatus(
        "current"
    )

basCmtsCmAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 10)
)
basCmtsCmAuthFailure.setObjects(
      *(("BAS-MIB", "basTrapCmtsCmMacAddress"),
        ("BAS-MIB", "basTrapCmtsCmGwAddress"))
)
if mibBuilder.loadTexts:
    basCmtsCmAuthFailure.setStatus(
        "current"
    )

basDhcpRelayNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 11)
)
basDhcpRelayNotConfigured.setObjects(
      *(("BAS-MIB", "basTrapChassis"),
        ("BAS-MIB", "basTrapSlot"),
        ("BAS-MIB", "basTrapIf"),
        ("BAS-MIB", "basTrapLPort"),
        ("BAS-MIB", "basTrapSubnetType"))
)
if mibBuilder.loadTexts:
    basDhcpRelayNotConfigured.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-TRAPS-MIB",
    **{"basTrapsMIB": basTrapsMIB,
       "basCardDown": basCardDown,
       "basCardUp": basCardUp,
       "basTraceLogTrap": basTraceLogTrap,
       "basCmtsCmUp": basCmtsCmUp,
       "basCmtsCmDown": basCmtsCmDown,
       "basBcmStateChange": basBcmStateChange,
       "basIclStateChange": basIclStateChange,
       "basSoftwareComponentUp": basSoftwareComponentUp,
       "basSoftwareComponentDown": basSoftwareComponentDown,
       "basCmtsCmAuthFailure": basCmtsCmAuthFailure,
       "basDhcpRelayNotConfigured": basDhcpRelayNotConfigured}
)
