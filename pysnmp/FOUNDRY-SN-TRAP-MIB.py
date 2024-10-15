# SNMP MIB module (FOUNDRY-SN-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:10 2024
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

(snAgGblTrapMessage,
 snAgentBrdIndex,
 snChasFanDescription,
 snChasFanIndex,
 snChasPwrSupplyDescription,
 snChasPwrSupplyIndex,
 snChasPwrSupplyStatus) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "snAgGblTrapMessage",
    "snAgentBrdIndex",
    "snChasFanDescription",
    "snChasFanIndex",
    "snChasPwrSupplyDescription",
    "snChasPwrSupplyIndex",
    "snChasPwrSupplyStatus")

(snOspfConfigErrorType,
 snOspfExtLsdbLimit,
 snOspfIfStatusIpAddress,
 snOspfIfStatusState,
 snOspfLsdbAreaId,
 snOspfLsdbLsId,
 snOspfLsdbRouterId,
 snOspfLsdbType,
 snOspfNbrIpAddr,
 snOspfNbrRtrId,
 snOspfNbrState,
 snOspfPacketSrc,
 snOspfPacketType,
 snOspfRouterId,
 snOspfVirtIfStatusAreaID,
 snOspfVirtIfStatusNeighbor,
 snOspfVirtIfStatusState,
 snOspfVirtNbrArea,
 snOspfVirtNbrRtrId,
 snOspfVirtNbrState) = mibBuilder.importSymbols(
    "FOUNDRY-SN-OSPF-GROUP-MIB",
    "snOspfConfigErrorType",
    "snOspfExtLsdbLimit",
    "snOspfIfStatusIpAddress",
    "snOspfIfStatusState",
    "snOspfLsdbAreaId",
    "snOspfLsdbLsId",
    "snOspfLsdbRouterId",
    "snOspfLsdbType",
    "snOspfNbrIpAddr",
    "snOspfNbrRtrId",
    "snOspfNbrState",
    "snOspfPacketSrc",
    "snOspfPacketType",
    "snOspfRouterId",
    "snOspfVirtIfStatusAreaID",
    "snOspfVirtIfStatusNeighbor",
    "snOspfVirtIfStatusState",
    "snOspfVirtNbrArea",
    "snOspfVirtNbrRtrId",
    "snOspfVirtNbrState")

(foundry,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "foundry")

(snL4MaxSessionLimit,
 snL4TcpSynLimit,
 snL4TrapRealServerCurConnections,
 snL4TrapRealServerIP,
 snL4TrapRealServerName,
 snL4TrapRealServerPort) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB",
    "snL4MaxSessionLimit",
    "snL4TcpSynLimit",
    "snL4TrapRealServerCurConnections",
    "snL4TrapRealServerIP",
    "snL4TrapRealServerName",
    "snL4TrapRealServerPort")

(snSwViolatorMacAddress,
 snSwViolatorPortNumber) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwViolatorMacAddress",
    "snSwViolatorPortNumber")

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

snTrapChasPwrSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1)
)
snTrapChasPwrSupply.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyStatus")
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupply.setStatus(
        ""
    )

snTrapLockedAddressViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 2)
)
snTrapLockedAddressViolation.setObjects(
      *(("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwViolatorPortNumber"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwViolatorMacAddress"))
)
if mibBuilder.loadTexts:
    snTrapLockedAddressViolation.setStatus(
        ""
    )

snTrapOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 3)
)
snTrapOspfIfStateChange.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusState"))
)
if mibBuilder.loadTexts:
    snTrapOspfIfStateChange.setStatus(
        ""
    )

snTrapOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 4)
)
snTrapOspfVirtIfStateChange.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusState"))
)
if mibBuilder.loadTexts:
    snTrapOspfVirtIfStateChange.setStatus(
        ""
    )

snOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 5)
)
snOspfNbrStateChange.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrIpAddr"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrRtrId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrState"))
)
if mibBuilder.loadTexts:
    snOspfNbrStateChange.setStatus(
        ""
    )

snOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 6)
)
snOspfVirtNbrStateChange.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtNbrArea"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtNbrRtrId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    snOspfVirtNbrStateChange.setStatus(
        ""
    )

snOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 7)
)
snOspfIfConfigError.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfIfConfigError.setStatus(
        ""
    )

snOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 8)
)
snOspfVirtIfConfigError.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfVirtIfConfigError.setStatus(
        ""
    )

snOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 9)
)
snOspfIfAuthFailure.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfIfAuthFailure.setStatus(
        ""
    )

snOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 10)
)
snOspfVirtIfAuthFailure.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfVirtIfAuthFailure.setStatus(
        ""
    )

snOspfIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 11)
)
snOspfIfRxBadPacket.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfIfRxBadPacket.setStatus(
        ""
    )

snOspfVirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 12)
)
snOspfVirtIfRxBadPacket.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
)
if mibBuilder.loadTexts:
    snOspfVirtIfRxBadPacket.setStatus(
        ""
    )

snOspfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 13)
)
snOspfTxRetransmit.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrRtrId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    snOspfTxRetransmit.setStatus(
        ""
    )

ospfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 14)
)
ospfVirtIfTxRetransmit.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfPacketType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    ospfVirtIfTxRetransmit.setStatus(
        ""
    )

snOspfOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 15)
)
snOspfOriginateLsa.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbAreaId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    snOspfOriginateLsa.setStatus(
        ""
    )

snOspfMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 16)
)
snOspfMaxAgeLsa.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbAreaId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbType"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
)
if mibBuilder.loadTexts:
    snOspfMaxAgeLsa.setStatus(
        ""
    )

snOspfLsdbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 17)
)
snOspfLsdbOverflow.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    snOspfLsdbOverflow.setStatus(
        ""
    )

snOspfLsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 18)
)
snOspfLsdbApproachingOverflow.setObjects(
      *(("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRouterId"),
        ("FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    snOspfLsdbApproachingOverflow.setStatus(
        ""
    )

snTrapL4MaxSessionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 19)
)
snTrapL4MaxSessionLimitReached.setObjects(
    ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4MaxSessionLimit")
)
if mibBuilder.loadTexts:
    snTrapL4MaxSessionLimitReached.setStatus(
        ""
    )

snTrapL4TcpSynLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 20)
)
snTrapL4TcpSynLimitReached.setObjects(
    ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TcpSynLimit")
)
if mibBuilder.loadTexts:
    snTrapL4TcpSynLimitReached.setStatus(
        ""
    )

snTrapL4RealServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 21)
)
snTrapL4RealServerUp.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerUp.setStatus(
        ""
    )

snTrapL4RealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 22)
)
snTrapL4RealServerDown.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerDown.setStatus(
        ""
    )

snTrapL4RealServerPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 23)
)
snTrapL4RealServerPortUp.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerPortUp.setStatus(
        ""
    )

snTrapL4RealServerPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 24)
)
snTrapL4RealServerPortDown.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerPortDown.setStatus(
        ""
    )

snTrapL4RealServerMaxConnectionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 25)
)
snTrapL4RealServerMaxConnectionLimitReached.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerCurConnections"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerMaxConnectionLimitReached.setStatus(
        ""
    )

snTrapL4BecomeStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 26)
)
if mibBuilder.loadTexts:
    snTrapL4BecomeStandby.setStatus(
        ""
    )

snTrapL4BecomeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 27)
)
if mibBuilder.loadTexts:
    snTrapL4BecomeActive.setStatus(
        ""
    )

snTrapModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 28)
)
snTrapModuleInserted.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleInserted.setStatus(
        ""
    )

snTrapModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 29)
)
snTrapModuleRemoved.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleRemoved.setStatus(
        ""
    )

snTrapChasPwrSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 30)
)
snTrapChasPwrSupplyFailed.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupplyFailed.setStatus(
        ""
    )

snTrapChasFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 31)
)
snTrapChasFanFailed.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasFanIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasFanDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasFanFailed.setStatus(
        ""
    )

snTrapLockedAddressViolation2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 32)
)
snTrapLockedAddressViolation2.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLockedAddressViolation2.setStatus(
        ""
    )

snTrapFsrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 33)
)
snTrapFsrpIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapFsrpIfStateChange.setStatus(
        ""
    )

snTrapVrrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 34)
)
snTrapVrrpIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVrrpIfStateChange.setStatus(
        ""
    )

snTrapMgmtModuleRedunStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 35)
)
snTrapMgmtModuleRedunStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMgmtModuleRedunStateChange.setStatus(
        ""
    )

snTrapTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 36)
)
snTrapTemperatureWarning.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTemperatureWarning.setStatus(
        ""
    )

snTrapAccessListDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 37)
)
snTrapAccessListDeny.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAccessListDeny.setStatus(
        ""
    )

snTrapMacFilterDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 38)
)
snTrapMacFilterDeny.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacFilterDeny.setStatus(
        ""
    )

snTrapL4GslbRemoteUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 39)
)
snTrapL4GslbRemoteUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteUp.setStatus(
        ""
    )

snTrapL4GslbRemoteDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 40)
)
snTrapL4GslbRemoteDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteDown.setStatus(
        ""
    )

snTrapL4GslbRemoteControllerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 41)
)
snTrapL4GslbRemoteControllerUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteControllerUp.setStatus(
        ""
    )

snTrapL4GslbRemoteControllerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 42)
)
snTrapL4GslbRemoteControllerDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteControllerDown.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 43)
)
snTrapL4GslbHealthCheckIpUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpUp.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 44)
)
snTrapL4GslbHealthCheckIpDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpDown.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 45)
)
snTrapL4GslbHealthCheckIpPortUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpPortUp.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 46)
)
snTrapL4GslbHealthCheckIpPortDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpPortDown.setStatus(
        ""
    )

snTrapL4FirewallBecomeStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 47)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallBecomeStandby.setStatus(
        ""
    )

snTrapL4FirewallBecomeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 48)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallBecomeActive.setStatus(
        ""
    )

snTrapL4FirewallPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 49)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallPathUp.setStatus(
        ""
    )

snTrapL4FirewallPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 50)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallPathDown.setStatus(
        ""
    )

snTrapIcmpLocalExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 51)
)
snTrapIcmpLocalExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIcmpLocalExceedBurst.setStatus(
        ""
    )

snTrapIcmpTransitExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 52)
)
snTrapIcmpTransitExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIcmpTransitExceedBurst.setStatus(
        ""
    )

snTrapTcpLocalExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 53)
)
snTrapTcpLocalExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTcpLocalExceedBurst.setStatus(
        ""
    )

snTrapTcpTransitExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 54)
)
snTrapTcpTransitExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTcpTransitExceedBurst.setStatus(
        ""
    )

snTrapL4ContentVerification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 55)
)
if mibBuilder.loadTexts:
    snTrapL4ContentVerification.setStatus(
        ""
    )

snTrapDuplicateIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 56)
)
if mibBuilder.loadTexts:
    snTrapDuplicateIp.setStatus(
        ""
    )

snTrapMplsProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 57)
)
if mibBuilder.loadTexts:
    snTrapMplsProblem.setStatus(
        ""
    )

snTrapMplsException = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 58)
)
if mibBuilder.loadTexts:
    snTrapMplsException.setStatus(
        ""
    )

snTrapMplsAudit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 59)
)
if mibBuilder.loadTexts:
    snTrapMplsAudit.setStatus(
        ""
    )

snTrapMplsDeveloper = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 60)
)
if mibBuilder.loadTexts:
    snTrapMplsDeveloper.setStatus(
        ""
    )

snTrapNoBmFreeQueue = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 61)
)
snTrapNoBmFreeQueue.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapNoBmFreeQueue.setStatus(
        ""
    )

snTrapSmcDmaDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 62)
)
snTrapSmcDmaDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSmcDmaDrop.setStatus(
        ""
    )

snTrapSmcBpDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 63)
)
snTrapSmcBpDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSmcBpDrop.setStatus(
        ""
    )

snTrapBmWriteSeqDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 64)
)
snTrapBmWriteSeqDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBmWriteSeqDrop.setStatus(
        ""
    )

snTrapBgpPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 65)
)
snTrapBgpPeerUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBgpPeerUp.setStatus(
        ""
    )

snTrapBgpPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 66)
)
snTrapBgpPeerDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBgpPeerDown.setStatus(
        ""
    )

snTrapL4RealServerResponseTimeLowerLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 67)
)
snTrapL4RealServerResponseTimeLowerLimit.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4RealServerResponseTimeLowerLimit.setStatus(
        ""
    )

snTrapL4RealServerResponseTimeUpperLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 68)
)
snTrapL4RealServerResponseTimeUpperLimit.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4RealServerResponseTimeUpperLimit.setStatus(
        ""
    )

snTrapL4TcpAttackRateExceedMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 69)
)
snTrapL4TcpAttackRateExceedMax.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4TcpAttackRateExceedMax.setStatus(
        ""
    )

snTrapL4TcpAttackRateExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 70)
)
snTrapL4TcpAttackRateExceedThreshold.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4TcpAttackRateExceedThreshold.setStatus(
        ""
    )

snTrapL4ConnectionRateExceedMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 71)
)
snTrapL4ConnectionRateExceedMax.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4ConnectionRateExceedMax.setStatus(
        ""
    )

snTrapL4ConnectionRateExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 72)
)
snTrapL4ConnectionRateExceedThreshold.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4ConnectionRateExceedThreshold.setStatus(
        ""
    )

snTrapRunningConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 73)
)
snTrapRunningConfigChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapRunningConfigChanged.setStatus(
        ""
    )

snTrapStartupConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 74)
)
snTrapStartupConfigChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapStartupConfigChanged.setStatus(
        ""
    )

snTrapUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 75)
)
snTrapUserLogin.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUserLogin.setStatus(
        ""
    )

snTrapUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 76)
)
snTrapUserLogout.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUserLogout.setStatus(
        ""
    )

snTrapPortSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 77)
)
snTrapPortSecurityViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortSecurityViolation.setStatus(
        ""
    )

snTrapPortSecurityShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 78)
)
snTrapPortSecurityShutdown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortSecurityShutdown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-TRAP-MIB",
    **{"snTrapChasPwrSupply": snTrapChasPwrSupply,
       "snTrapLockedAddressViolation": snTrapLockedAddressViolation,
       "snTrapOspfIfStateChange": snTrapOspfIfStateChange,
       "snTrapOspfVirtIfStateChange": snTrapOspfVirtIfStateChange,
       "snOspfNbrStateChange": snOspfNbrStateChange,
       "snOspfVirtNbrStateChange": snOspfVirtNbrStateChange,
       "snOspfIfConfigError": snOspfIfConfigError,
       "snOspfVirtIfConfigError": snOspfVirtIfConfigError,
       "snOspfIfAuthFailure": snOspfIfAuthFailure,
       "snOspfVirtIfAuthFailure": snOspfVirtIfAuthFailure,
       "snOspfIfRxBadPacket": snOspfIfRxBadPacket,
       "snOspfVirtIfRxBadPacket": snOspfVirtIfRxBadPacket,
       "snOspfTxRetransmit": snOspfTxRetransmit,
       "ospfVirtIfTxRetransmit": ospfVirtIfTxRetransmit,
       "snOspfOriginateLsa": snOspfOriginateLsa,
       "snOspfMaxAgeLsa": snOspfMaxAgeLsa,
       "snOspfLsdbOverflow": snOspfLsdbOverflow,
       "snOspfLsdbApproachingOverflow": snOspfLsdbApproachingOverflow,
       "snTrapL4MaxSessionLimitReached": snTrapL4MaxSessionLimitReached,
       "snTrapL4TcpSynLimitReached": snTrapL4TcpSynLimitReached,
       "snTrapL4RealServerUp": snTrapL4RealServerUp,
       "snTrapL4RealServerDown": snTrapL4RealServerDown,
       "snTrapL4RealServerPortUp": snTrapL4RealServerPortUp,
       "snTrapL4RealServerPortDown": snTrapL4RealServerPortDown,
       "snTrapL4RealServerMaxConnectionLimitReached": snTrapL4RealServerMaxConnectionLimitReached,
       "snTrapL4BecomeStandby": snTrapL4BecomeStandby,
       "snTrapL4BecomeActive": snTrapL4BecomeActive,
       "snTrapModuleInserted": snTrapModuleInserted,
       "snTrapModuleRemoved": snTrapModuleRemoved,
       "snTrapChasPwrSupplyFailed": snTrapChasPwrSupplyFailed,
       "snTrapChasFanFailed": snTrapChasFanFailed,
       "snTrapLockedAddressViolation2": snTrapLockedAddressViolation2,
       "snTrapFsrpIfStateChange": snTrapFsrpIfStateChange,
       "snTrapVrrpIfStateChange": snTrapVrrpIfStateChange,
       "snTrapMgmtModuleRedunStateChange": snTrapMgmtModuleRedunStateChange,
       "snTrapTemperatureWarning": snTrapTemperatureWarning,
       "snTrapAccessListDeny": snTrapAccessListDeny,
       "snTrapMacFilterDeny": snTrapMacFilterDeny,
       "snTrapL4GslbRemoteUp": snTrapL4GslbRemoteUp,
       "snTrapL4GslbRemoteDown": snTrapL4GslbRemoteDown,
       "snTrapL4GslbRemoteControllerUp": snTrapL4GslbRemoteControllerUp,
       "snTrapL4GslbRemoteControllerDown": snTrapL4GslbRemoteControllerDown,
       "snTrapL4GslbHealthCheckIpUp": snTrapL4GslbHealthCheckIpUp,
       "snTrapL4GslbHealthCheckIpDown": snTrapL4GslbHealthCheckIpDown,
       "snTrapL4GslbHealthCheckIpPortUp": snTrapL4GslbHealthCheckIpPortUp,
       "snTrapL4GslbHealthCheckIpPortDown": snTrapL4GslbHealthCheckIpPortDown,
       "snTrapL4FirewallBecomeStandby": snTrapL4FirewallBecomeStandby,
       "snTrapL4FirewallBecomeActive": snTrapL4FirewallBecomeActive,
       "snTrapL4FirewallPathUp": snTrapL4FirewallPathUp,
       "snTrapL4FirewallPathDown": snTrapL4FirewallPathDown,
       "snTrapIcmpLocalExceedBurst": snTrapIcmpLocalExceedBurst,
       "snTrapIcmpTransitExceedBurst": snTrapIcmpTransitExceedBurst,
       "snTrapTcpLocalExceedBurst": snTrapTcpLocalExceedBurst,
       "snTrapTcpTransitExceedBurst": snTrapTcpTransitExceedBurst,
       "snTrapL4ContentVerification": snTrapL4ContentVerification,
       "snTrapDuplicateIp": snTrapDuplicateIp,
       "snTrapMplsProblem": snTrapMplsProblem,
       "snTrapMplsException": snTrapMplsException,
       "snTrapMplsAudit": snTrapMplsAudit,
       "snTrapMplsDeveloper": snTrapMplsDeveloper,
       "snTrapNoBmFreeQueue": snTrapNoBmFreeQueue,
       "snTrapSmcDmaDrop": snTrapSmcDmaDrop,
       "snTrapSmcBpDrop": snTrapSmcBpDrop,
       "snTrapBmWriteSeqDrop": snTrapBmWriteSeqDrop,
       "snTrapBgpPeerUp": snTrapBgpPeerUp,
       "snTrapBgpPeerDown": snTrapBgpPeerDown,
       "snTrapL4RealServerResponseTimeLowerLimit": snTrapL4RealServerResponseTimeLowerLimit,
       "snTrapL4RealServerResponseTimeUpperLimit": snTrapL4RealServerResponseTimeUpperLimit,
       "snTrapL4TcpAttackRateExceedMax": snTrapL4TcpAttackRateExceedMax,
       "snTrapL4TcpAttackRateExceedThreshold": snTrapL4TcpAttackRateExceedThreshold,
       "snTrapL4ConnectionRateExceedMax": snTrapL4ConnectionRateExceedMax,
       "snTrapL4ConnectionRateExceedThreshold": snTrapL4ConnectionRateExceedThreshold,
       "snTrapRunningConfigChanged": snTrapRunningConfigChanged,
       "snTrapStartupConfigChanged": snTrapStartupConfigChanged,
       "snTrapUserLogin": snTrapUserLogin,
       "snTrapUserLogout": snTrapUserLogout,
       "snTrapPortSecurityViolation": snTrapPortSecurityViolation,
       "snTrapPortSecurityShutdown": snTrapPortSecurityShutdown}
)
