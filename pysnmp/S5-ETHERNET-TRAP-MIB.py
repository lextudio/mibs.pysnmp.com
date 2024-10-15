# SNMP MIB module (S5-ETHERNET-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-ETHERNET-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:08 2024
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

(s5EnRedPortCompanionBrdNum,
 s5EnRedPortCompanionPortNum,
 s5EnRedPortOperStatus,
 s5EnRedPortRedundMode,
 s5EnRedPortRemoteOperStatus) = mibBuilder.importSymbols(
    "S5-ETH-REDUNDANT-LINKS-MIB",
    "s5EnRedPortCompanionBrdNum",
    "s5EnRedPortCompanionPortNum",
    "s5EnRedPortOperStatus",
    "s5EnRedPortRedundMode",
    "s5EnRedPortRemoteOperStatus")

(s5EnPortJabberStatus,
 s5EnPortLinkStatus,
 s5EnPortPartStatus) = mibBuilder.importSymbols(
    "S5-ETHERNET-COMMON-MIB",
    "s5EnPortJabberStatus",
    "s5EnPortLinkStatus",
    "s5EnPortPartStatus")

(s5EthTrap,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5EthTrap")

(s5SbsMgmViolationIpAddress,
 s5SbsMgmViolationType,
 s5SbsViolationStatusBrdIndx,
 s5SbsViolationStatusMACAddress,
 s5SbsViolationStatusPortIndx) = mibBuilder.importSymbols(
    "S5-SWITCH-BAYSECURE-MIB",
    "s5SbsMgmViolationIpAddress",
    "s5SbsMgmViolationType",
    "s5SbsViolationStatusBrdIndx",
    "s5SbsViolationStatusMACAddress",
    "s5SbsViolationStatusPortIndx")

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

s5EthernetTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0)
)
s5EthernetTrapMib.setRevisions(
        ("2012-02-28 00:00",
         "2009-07-29 00:00",
         "2009-02-25 00:00",
         "2004-07-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

s5EtrSbsMacTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 1)
)
if mibBuilder.loadTexts:
    s5EtrSbsMacTableFull.setStatus(
        "current"
    )

s5EtrSbsMacTableClearedForPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 2)
)
s5EtrSbsMacTableClearedForPort.setObjects(
      *(("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusBrdIndx"),
        ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusPortIndx"))
)
if mibBuilder.loadTexts:
    s5EtrSbsMacTableClearedForPort.setStatus(
        "current"
    )

s5EtrSbsMacTableCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 3)
)
if mibBuilder.loadTexts:
    s5EtrSbsMacTableCleared.setStatus(
        "current"
    )

s5EtrSbsMacRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 4)
)
s5EtrSbsMacRemoved.setObjects(
      *(("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusBrdIndx"),
        ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusPortIndx"),
        ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusMACAddress"))
)
if mibBuilder.loadTexts:
    s5EtrSbsMacRemoved.setStatus(
        "current"
    )

s5EtrNewSbsMacAccessViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 5)
)
s5EtrNewSbsMacAccessViolation.setObjects(
      *(("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusBrdIndx"),
        ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusPortIndx"),
        ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusMACAddress"))
)
if mibBuilder.loadTexts:
    s5EtrNewSbsMacAccessViolation.setStatus(
        "current"
    )

s5EtrNewMgmAccessViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 6)
)
s5EtrNewMgmAccessViolation.setObjects(
      *(("S5-SWITCH-BAYSECURE-MIB", "s5SbsMgmViolationType"),
        ("S5-SWITCH-BAYSECURE-MIB", "s5SbsMgmViolationIpAddress"))
)
if mibBuilder.loadTexts:
    s5EtrNewMgmAccessViolation.setStatus(
        "current"
    )

s5EtrNewPortManualPart = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 7)
)
s5EtrNewPortManualPart.setObjects(
      *(("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"),
        ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
)
if mibBuilder.loadTexts:
    s5EtrNewPortManualPart.setStatus(
        "current"
    )

s5EtrNewPortAutoPart = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 8)
)
s5EtrNewPortAutoPart.setObjects(
      *(("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"),
        ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
)
if mibBuilder.loadTexts:
    s5EtrNewPortAutoPart.setStatus(
        "current"
    )

s5EtrNewPortDteJabbering = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 9)
)
s5EtrNewPortDteJabbering.setObjects(
    ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus")
)
if mibBuilder.loadTexts:
    s5EtrNewPortDteJabbering.setStatus(
        "current"
    )

s5EtrNewRedPortFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 10)
)
s5EtrNewRedPortFailure.setObjects(
      *(("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortOperStatus"),
        ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortCompanionBrdNum"),
        ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortCompanionPortNum"),
        ("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"),
        ("S5-ETHERNET-COMMON-MIB", "s5EnPortLinkStatus"),
        ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
)
if mibBuilder.loadTexts:
    s5EtrNewRedPortFailure.setStatus(
        "current"
    )

s5EtrNewRedBadRemCfgDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 11)
)
s5EtrNewRedBadRemCfgDetected.setObjects(
      *(("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortRemoteOperStatus"),
        ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortRedundMode"))
)
if mibBuilder.loadTexts:
    s5EtrNewRedBadRemCfgDetected.setStatus(
        "current"
    )

s5EtrMacAddressTablesThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 12)
)
if mibBuilder.loadTexts:
    s5EtrMacAddressTablesThresholdReached.setStatus(
        "current"
    )

s5EtrPortAutoPart = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 1)
)
s5EtrPortAutoPart.setObjects(
      *(("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"),
        ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
)
if mibBuilder.loadTexts:
    s5EtrPortAutoPart.setStatus(
        "current"
    )

s5EtrPortDteJabbering = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 2)
)
s5EtrPortDteJabbering.setObjects(
    ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus")
)
if mibBuilder.loadTexts:
    s5EtrPortDteJabbering.setStatus(
        "current"
    )

s5EtrRedPortFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 3)
)
s5EtrRedPortFailure.setObjects(
      *(("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortOperStatus"),
        ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortCompanionBrdNum"),
        ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortCompanionPortNum"),
        ("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"),
        ("S5-ETHERNET-COMMON-MIB", "s5EnPortLinkStatus"),
        ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
)
if mibBuilder.loadTexts:
    s5EtrRedPortFailure.setStatus(
        "current"
    )

s5EtrRedBadRemCfgDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 4)
)
s5EtrRedBadRemCfgDetected.setObjects(
      *(("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortRemoteOperStatus"),
        ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortRedundMode"))
)
if mibBuilder.loadTexts:
    s5EtrRedBadRemCfgDetected.setStatus(
        "current"
    )

s5EtrSbsMacAccessViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 5)
)
s5EtrSbsMacAccessViolation.setObjects(
      *(("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusBrdIndx"),
        ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusPortIndx"),
        ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusMACAddress"))
)
if mibBuilder.loadTexts:
    s5EtrSbsMacAccessViolation.setStatus(
        "current"
    )

s5EtrMgmAccessViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 6)
)
s5EtrMgmAccessViolation.setObjects(
      *(("S5-SWITCH-BAYSECURE-MIB", "s5SbsMgmViolationType"),
        ("S5-SWITCH-BAYSECURE-MIB", "s5SbsMgmViolationIpAddress"))
)
if mibBuilder.loadTexts:
    s5EtrMgmAccessViolation.setStatus(
        "current"
    )

s5EtrPortManualPart = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 7)
)
s5EtrPortManualPart.setObjects(
      *(("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"),
        ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
)
if mibBuilder.loadTexts:
    s5EtrPortManualPart.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-ETHERNET-TRAP-MIB",
    **{"s5EthernetTrapMib": s5EthernetTrapMib,
       "s5EtrSbsMacTableFull": s5EtrSbsMacTableFull,
       "s5EtrSbsMacTableClearedForPort": s5EtrSbsMacTableClearedForPort,
       "s5EtrSbsMacTableCleared": s5EtrSbsMacTableCleared,
       "s5EtrSbsMacRemoved": s5EtrSbsMacRemoved,
       "s5EtrNewSbsMacAccessViolation": s5EtrNewSbsMacAccessViolation,
       "s5EtrNewMgmAccessViolation": s5EtrNewMgmAccessViolation,
       "s5EtrNewPortManualPart": s5EtrNewPortManualPart,
       "s5EtrNewPortAutoPart": s5EtrNewPortAutoPart,
       "s5EtrNewPortDteJabbering": s5EtrNewPortDteJabbering,
       "s5EtrNewRedPortFailure": s5EtrNewRedPortFailure,
       "s5EtrNewRedBadRemCfgDetected": s5EtrNewRedBadRemCfgDetected,
       "s5EtrMacAddressTablesThresholdReached": s5EtrMacAddressTablesThresholdReached,
       "s5EtrPortAutoPart": s5EtrPortAutoPart,
       "s5EtrPortDteJabbering": s5EtrPortDteJabbering,
       "s5EtrRedPortFailure": s5EtrRedPortFailure,
       "s5EtrRedBadRemCfgDetected": s5EtrRedBadRemCfgDetected,
       "s5EtrSbsMacAccessViolation": s5EtrSbsMacAccessViolation,
       "s5EtrMgmAccessViolation": s5EtrMgmAccessViolation,
       "s5EtrPortManualPart": s5EtrPortManualPart}
)
