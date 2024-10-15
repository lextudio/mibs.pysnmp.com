# SNMP MIB module (FOUNDRY-SN-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:01 2024
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

(brcdNPIndex,
 brcdNPLockupRecoveryCount) = mibBuilder.importSymbols(
    "BROCADE-NP-TM-STATS-MIB",
    "brcdNPIndex",
    "brcdNPLockupRecoveryCount")

(dot3OamLoopbackStatus,) = mibBuilder.importSymbols(
    "DOT3-OAM-MIB",
    "dot3OamLoopbackStatus")

(fdryLicenseType,
 snAgGblTrapMessage,
 snAgentBrdIndex,
 snAgentBrdModuleStatus,
 snChasFanDescription,
 snChasFanIndex,
 snChasPwrSupplyDescription,
 snChasPwrSupplyIndex,
 snChasPwrSupplyStatus,
 snChasUnitIndex) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "fdryLicenseType",
    "snAgGblTrapMessage",
    "snAgentBrdIndex",
    "snAgentBrdModuleStatus",
    "snChasFanDescription",
    "snChasFanIndex",
    "snChasPwrSupplyDescription",
    "snChasPwrSupplyIndex",
    "snChasPwrSupplyStatus",
    "snChasUnitIndex")

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

(snStackingGlobalMixedMode,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-STACKING-MIB",
    "snStackingGlobalMixedMode")

(snL4LinkVirtualInterface,
 snL4MaxSessionLimit,
 snL4TcpSynLimit,
 snL4TrapLinkName,
 snL4TrapRealServerCurConnections,
 snL4TrapRealServerIP,
 snL4TrapRealServerName,
 snL4TrapRealServerPort) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB",
    "snL4LinkVirtualInterface",
    "snL4MaxSessionLimit",
    "snL4TcpSynLimit",
    "snL4TrapLinkName",
    "snL4TrapRealServerCurConnections",
    "snL4TrapRealServerIP",
    "snL4TrapRealServerName",
    "snL4TrapRealServerPort")

(snSwViolatorMacAddress,
 snSwViolatorPortNumber,
 snVLanByPortCfgVLanId) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwViolatorMacAddress",
    "snSwViolatorPortNumber",
    "snVLanByPortCfgVLanId")

(wgPnPStatus,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-WIRELESS-GROUP-MIB",
    "wgPnPStatus")

(dot1agCfmMaNetName,
 dot1agCfmMdName,
 dot1agCfmMepDbRMepState) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaNetName",
    "dot1agCfmMdName",
    "dot1agCfmMepDbRMepState")

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

snTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 0)
)
snTraps.setRevisions(
        ("2012-05-18 00:00",
         "2010-06-02 00:00",
         "2009-09-30 00:00")
)


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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
    )

snTrapL4MaxSessionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 19)
)
snTrapL4MaxSessionLimitReached.setObjects(
    ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4MaxSessionLimit")
)
if mibBuilder.loadTexts:
    snTrapL4MaxSessionLimitReached.setStatus(
        "current"
    )

snTrapL4TcpSynLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 20)
)
snTrapL4TcpSynLimitReached.setObjects(
    ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TcpSynLimit")
)
if mibBuilder.loadTexts:
    snTrapL4TcpSynLimitReached.setStatus(
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
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
        "current"
    )

snTrapL4BecomeStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 26)
)
if mibBuilder.loadTexts:
    snTrapL4BecomeStandby.setStatus(
        "current"
    )

snTrapL4BecomeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 27)
)
if mibBuilder.loadTexts:
    snTrapL4BecomeActive.setStatus(
        "current"
    )

snTrapModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 28)
)
snTrapModuleInserted.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleInserted.setStatus(
        "current"
    )

snTrapModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 29)
)
snTrapModuleRemoved.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleRemoved.setStatus(
        "current"
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
        "current"
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
        "current"
    )

snTrapLockedAddressViolation2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 32)
)
snTrapLockedAddressViolation2.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLockedAddressViolation2.setStatus(
        "current"
    )

snTrapFsrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 33)
)
snTrapFsrpIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapFsrpIfStateChange.setStatus(
        "current"
    )

snTrapVrrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 34)
)
snTrapVrrpIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVrrpIfStateChange.setStatus(
        "current"
    )

snTrapMgmtModuleRedunStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 35)
)
snTrapMgmtModuleRedunStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMgmtModuleRedunStateChange.setStatus(
        "current"
    )

snTrapTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 36)
)
snTrapTemperatureWarning.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTemperatureWarning.setStatus(
        "current"
    )

snTrapAccessListDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 37)
)
snTrapAccessListDeny.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAccessListDeny.setStatus(
        "current"
    )

snTrapMacFilterDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 38)
)
snTrapMacFilterDeny.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacFilterDeny.setStatus(
        "current"
    )

snTrapL4GslbRemoteUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 39)
)
snTrapL4GslbRemoteUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteUp.setStatus(
        "current"
    )

snTrapL4GslbRemoteDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 40)
)
snTrapL4GslbRemoteDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteDown.setStatus(
        "current"
    )

snTrapL4GslbRemoteControllerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 41)
)
snTrapL4GslbRemoteControllerUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteControllerUp.setStatus(
        "current"
    )

snTrapL4GslbRemoteControllerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 42)
)
snTrapL4GslbRemoteControllerDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteControllerDown.setStatus(
        "current"
    )

snTrapL4GslbHealthCheckIpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 43)
)
snTrapL4GslbHealthCheckIpUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpUp.setStatus(
        "current"
    )

snTrapL4GslbHealthCheckIpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 44)
)
snTrapL4GslbHealthCheckIpDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpDown.setStatus(
        "current"
    )

snTrapL4GslbHealthCheckIpPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 45)
)
snTrapL4GslbHealthCheckIpPortUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpPortUp.setStatus(
        "current"
    )

snTrapL4GslbHealthCheckIpPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 46)
)
snTrapL4GslbHealthCheckIpPortDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpPortDown.setStatus(
        "current"
    )

snTrapL4FirewallBecomeStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 47)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallBecomeStandby.setStatus(
        "current"
    )

snTrapL4FirewallBecomeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 48)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallBecomeActive.setStatus(
        "current"
    )

snTrapL4FirewallPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 49)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallPathUp.setStatus(
        "current"
    )

snTrapL4FirewallPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 50)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallPathDown.setStatus(
        "current"
    )

snTrapIcmpLocalExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 51)
)
snTrapIcmpLocalExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIcmpLocalExceedBurst.setStatus(
        "current"
    )

snTrapIcmpTransitExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 52)
)
snTrapIcmpTransitExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIcmpTransitExceedBurst.setStatus(
        "current"
    )

snTrapTcpLocalExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 53)
)
snTrapTcpLocalExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTcpLocalExceedBurst.setStatus(
        "current"
    )

snTrapTcpTransitExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 54)
)
snTrapTcpTransitExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTcpTransitExceedBurst.setStatus(
        "current"
    )

snTrapL4ContentVerification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 55)
)
if mibBuilder.loadTexts:
    snTrapL4ContentVerification.setStatus(
        "current"
    )

snTrapDuplicateIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 56)
)
snTrapDuplicateIp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDuplicateIp.setStatus(
        "current"
    )

snTrapMplsProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 57)
)
if mibBuilder.loadTexts:
    snTrapMplsProblem.setStatus(
        "obsolete"
    )

snTrapMplsException = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 58)
)
if mibBuilder.loadTexts:
    snTrapMplsException.setStatus(
        "obsolete"
    )

snTrapMplsAudit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 59)
)
if mibBuilder.loadTexts:
    snTrapMplsAudit.setStatus(
        "obsolete"
    )

snTrapMplsDeveloper = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 60)
)
if mibBuilder.loadTexts:
    snTrapMplsDeveloper.setStatus(
        "obsolete"
    )

snTrapNoBmFreeQueue = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 61)
)
snTrapNoBmFreeQueue.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapNoBmFreeQueue.setStatus(
        "current"
    )

snTrapSmcDmaDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 62)
)
snTrapSmcDmaDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSmcDmaDrop.setStatus(
        "current"
    )

snTrapSmcBpDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 63)
)
snTrapSmcBpDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSmcBpDrop.setStatus(
        "current"
    )

snTrapBmWriteSeqDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 64)
)
snTrapBmWriteSeqDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBmWriteSeqDrop.setStatus(
        "current"
    )

snTrapBgpPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 65)
)
snTrapBgpPeerUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBgpPeerUp.setStatus(
        "current"
    )

snTrapBgpPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 66)
)
snTrapBgpPeerDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBgpPeerDown.setStatus(
        "current"
    )

snTrapL4RealServerResponseTimeLowerLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 67)
)
snTrapL4RealServerResponseTimeLowerLimit.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4RealServerResponseTimeLowerLimit.setStatus(
        "current"
    )

snTrapL4RealServerResponseTimeUpperLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 68)
)
snTrapL4RealServerResponseTimeUpperLimit.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4RealServerResponseTimeUpperLimit.setStatus(
        "current"
    )

snTrapL4TcpAttackRateExceedMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 69)
)
snTrapL4TcpAttackRateExceedMax.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4TcpAttackRateExceedMax.setStatus(
        "current"
    )

snTrapL4TcpAttackRateExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 70)
)
snTrapL4TcpAttackRateExceedThreshold.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4TcpAttackRateExceedThreshold.setStatus(
        "current"
    )

snTrapL4ConnectionRateExceedMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 71)
)
snTrapL4ConnectionRateExceedMax.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4ConnectionRateExceedMax.setStatus(
        "current"
    )

snTrapL4ConnectionRateExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 72)
)
snTrapL4ConnectionRateExceedThreshold.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4ConnectionRateExceedThreshold.setStatus(
        "current"
    )

snTrapRunningConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 73)
)
snTrapRunningConfigChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapRunningConfigChanged.setStatus(
        "current"
    )

snTrapStartupConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 74)
)
snTrapStartupConfigChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapStartupConfigChanged.setStatus(
        "current"
    )

snTrapUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 75)
)
snTrapUserLogin.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUserLogin.setStatus(
        "current"
    )

snTrapUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 76)
)
snTrapUserLogout.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUserLogout.setStatus(
        "current"
    )

snTrapPortSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 77)
)
snTrapPortSecurityViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortSecurityViolation.setStatus(
        "current"
    )

snTrapPortSecurityShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 78)
)
snTrapPortSecurityShutdown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortSecurityShutdown.setStatus(
        "current"
    )

snTrapMrpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 79)
)
snTrapMrpStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMrpStateChange.setStatus(
        "current"
    )

snTrapMrpCamError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 80)
)
snTrapMrpCamError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMrpCamError.setStatus(
        "current"
    )

snTrapChasPwrSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 81)
)
snTrapChasPwrSupplyOK.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupplyOK.setStatus(
        "current"
    )

snTrapVrrpeIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 82)
)
snTrapVrrpeIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVrrpeIfStateChange.setStatus(
        "current"
    )

snTrapVsrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 83)
)
snTrapVsrpIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVsrpIfStateChange.setStatus(
        "current"
    )

snTrapSrcIpAddressViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 84)
)
snTrapSrcIpAddressViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSrcIpAddressViolation.setStatus(
        "current"
    )

snTrapMacAuthEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 85)
)
snTrapMacAuthEnable.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthEnable.setStatus(
        "current"
    )

snTrapMacAuthDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 86)
)
snTrapMacAuthDisable.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthDisable.setStatus(
        "current"
    )

snTrapMacAuthMACAccepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 87)
)
snTrapMacAuthMACAccepted.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthMACAccepted.setStatus(
        "current"
    )

snTrapMacAuthMACRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 88)
)
snTrapMacAuthMACRejected.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthMACRejected.setStatus(
        "current"
    )

snTrapMacAuthPortDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 89)
)
snTrapMacAuthPortDisabled.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthPortDisabled.setStatus(
        "current"
    )

snTrapClientLoginReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 110)
)
snTrapClientLoginReject.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapClientLoginReject.setStatus(
        "current"
    )

snTrapLocalUserConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 111)
)
snTrapLocalUserConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLocalUserConfigChange.setStatus(
        "current"
    )

snTrapVlanConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 112)
)
snTrapVlanConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVlanConfigChange.setStatus(
        "current"
    )

snTrapAclConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 113)
)
snTrapAclConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAclConfigChange.setStatus(
        "current"
    )

snTrapMacFilterConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 114)
)
snTrapMacFilterConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacFilterConfigChange.setStatus(
        "current"
    )

snTrapSNMPConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 115)
)
snTrapSNMPConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSNMPConfigChange.setStatus(
        "current"
    )

snTrapSyslogConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 116)
)
snTrapSyslogConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSyslogConfigChange.setStatus(
        "current"
    )

snTrapPasswordConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 117)
)
snTrapPasswordConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPasswordConfigChange.setStatus(
        "current"
    )

snTrapServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 118)
)
snTrapServerStatusChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapServerStatusChange.setStatus(
        "current"
    )

snTrapL4RealServerPortMaxConnectionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 119)
)
snTrapL4RealServerPortMaxConnectionLimitReached.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4RealServerPortMaxConnectionLimitReached.setStatus(
        "current"
    )

snTrapL4LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 120)
)
snTrapL4LinkDown.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapLinkName"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4LinkVirtualInterface"))
)
if mibBuilder.loadTexts:
    snTrapL4LinkDown.setStatus(
        "current"
    )

snTrapL4LinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 121)
)
snTrapL4LinkUp.setObjects(
      *(("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapLinkName"),
        ("FOUNDRY-SN-SW-L4-SWITCH-GROUP-MIB", "snL4LinkVirtualInterface"))
)
if mibBuilder.loadTexts:
    snTrapL4LinkUp.setStatus(
        "current"
    )

snTrapPortPriorityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 122)
)
snTrapPortPriorityChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortPriorityChange.setStatus(
        "current"
    )

snTrapAutoPortDisableTrigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 123)
)
snTrapAutoPortDisableTrigger.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAutoPortDisableTrigger.setStatus(
        "current"
    )

snTrapAutoPortDisableRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 124)
)
snTrapAutoPortDisableRelease.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAutoPortDisableRelease.setStatus(
        "current"
    )

snTrapPnPStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 125)
)
snTrapPnPStatusChange.setObjects(
      *(("FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgPnPStatus"),
        ("FOUNDRY-SN-WIRELESS-GROUP-MIB", "wgPnPStatus"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapPnPStatusChange.setStatus(
        "current"
    )

snTrapWirelessIsrpPeerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 126)
)
snTrapWirelessIsrpPeerStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapWirelessIsrpPeerStateChange.setStatus(
        "current"
    )

snTrapWirelessStationStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 127)
)
snTrapWirelessStationStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapWirelessStationStateChange.setStatus(
        "current"
    )

snTrapWirelessStationRoamingEventTriggered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 128)
)
snTrapWirelessStationRoamingEventTriggered.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapWirelessStationRoamingEventTriggered.setStatus(
        "current"
    )

snTrapWirelessSappStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 129)
)
snTrapWirelessSappStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapWirelessSappStateChange.setStatus(
        "current"
    )

snTrapExternalPowerConnectionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 130)
)
snTrapExternalPowerConnectionStatus.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapExternalPowerConnectionStatus.setStatus(
        "current"
    )

snTrapDot1xSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 131)
)
snTrapDot1xSecurityViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xSecurityViolation.setStatus(
        "current"
    )

snTrapDot1xPortLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 132)
)
snTrapDot1xPortLinkChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xPortLinkChange.setStatus(
        "current"
    )

snTrapDot1xPortControlChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 133)
)
snTrapDot1xPortControlChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xPortControlChange.setStatus(
        "current"
    )

snTrapDot1xVlanIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 134)
)
snTrapDot1xVlanIdChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xVlanIdChange.setStatus(
        "current"
    )

snTrapDot1xFilterSetupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 135)
)
snTrapDot1xFilterSetupFailure.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xFilterSetupFailure.setStatus(
        "current"
    )

snTrapDot1xError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 136)
)
snTrapDot1xError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xError.setStatus(
        "current"
    )

snTrapPortConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 137)
)
snTrapPortConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortConfigChange.setStatus(
        "current"
    )

snTrapMacAuthVlanIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 138)
)
snTrapMacAuthVlanIdChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthVlanIdChange.setStatus(
        "current"
    )

snTrapWebAuthEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 139)
)
snTrapWebAuthEnabled.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapWebAuthEnabled.setStatus(
        "current"
    )

snTrapWebAuthDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 140)
)
snTrapWebAuthDisabled.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapWebAuthDisabled.setStatus(
        "current"
    )

snTrapIpConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 141)
)
snTrapIpConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIpConfigChange.setStatus(
        "current"
    )

snTrapIpv6ConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 142)
)
snTrapIpv6ConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIpv6ConfigChange.setStatus(
        "current"
    )

snTrapMacAuthRadiusTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 143)
)
snTrapMacAuthRadiusTimeout.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthRadiusTimeout.setStatus(
        "current"
    )

snTrapDot1xRadiusTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 144)
)
snTrapDot1xRadiusTimeout.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xRadiusTimeout.setStatus(
        "current"
    )

snTrapUDLDLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 145)
)
snTrapUDLDLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapUDLDLinkDown.setStatus(
        "current"
    )

snTrapUDLDLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 146)
)
snTrapUDLDLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapUDLDLinkUp.setStatus(
        "current"
    )

snTrapMacBasedVlanEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 147)
)
snTrapMacBasedVlanEnabled.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacBasedVlanEnabled.setStatus(
        "current"
    )

snTrapMacBasedVlanDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 148)
)
snTrapMacBasedVlanDisabled.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacBasedVlanDisabled.setStatus(
        "current"
    )

snTrapChasFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 149)
)
snTrapChasFanNormal.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasFanIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasFanDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasFanNormal.setStatus(
        "current"
    )

snTrapStpRootGuardDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 150)
)
snTrapStpRootGuardDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStpRootGuardDetect.setStatus(
        "current"
    )

snTrapStpRootGuardExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 151)
)
snTrapStpRootGuardExpire.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStpRootGuardExpire.setStatus(
        "current"
    )

snTrapStpBPDUGuardDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 152)
)
snTrapStpBPDUGuardDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStpBPDUGuardDetect.setStatus(
        "current"
    )

snTrapMstpBPDUGuardDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 153)
)
snTrapMstpBPDUGuardDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapMstpBPDUGuardDetect.setStatus(
        "current"
    )

snTrapErrorDisableAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 154)
)
snTrapErrorDisableAction.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapErrorDisableAction.setStatus(
        "current"
    )

snTrapLACPLinkStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 155)
)
snTrapLACPLinkStateChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLACPLinkStateChange.setStatus(
        "current"
    )

snTrapOpticalMonitoringNotFoundryOptics = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 156)
)
snTrapOpticalMonitoringNotFoundryOptics.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringNotFoundryOptics.setStatus(
        "current"
    )

snTrapOpticalMonitoringFoundryOpticsNotCapable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 157)
)
snTrapOpticalMonitoringFoundryOpticsNotCapable.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringFoundryOpticsNotCapable.setStatus(
        "current"
    )

snTrapStaticMulticastMacConfigAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 158)
)
snTrapStaticMulticastMacConfigAdd.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapStaticMulticastMacConfigAdd.setStatus(
        "current"
    )

snTrapStaticMulticastMacConfigRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 159)
)
snTrapStaticMulticastMacConfigRemove.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapStaticMulticastMacConfigRemove.setStatus(
        "current"
    )

snTrapSTPBPDUGuardExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 160)
)
snTrapSTPBPDUGuardExpire.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapSTPBPDUGuardExpire.setStatus(
        "current"
    )

snTrapPortLoopDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 161)
)
snTrapPortLoopDetection.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapPortLoopDetection.setStatus(
        "current"
    )

snTrapNoFreeTcamEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 162)
)
snTrapNoFreeTcamEntry.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapNoFreeTcamEntry.setStatus(
        "current"
    )

snTrapStackingMasterElected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 163)
)
snTrapStackingMasterElected.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStackingMasterElected.setStatus(
        "current"
    )

snTrapStackingUnitAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 164)
)
snTrapStackingUnitAdded.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStackingUnitAdded.setStatus(
        "current"
    )

snTrapStackingUnitDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 165)
)
snTrapStackingUnitDeleted.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStackingUnitDeleted.setStatus(
        "current"
    )

snTrapStackingChasPwrSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 166)
)
snTrapStackingChasPwrSupplyOK.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStackingChasPwrSupplyOK.setStatus(
        "current"
    )

snTrapStackingChasPwrSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 167)
)
snTrapStackingChasPwrSupplyFailed.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStackingChasPwrSupplyFailed.setStatus(
        "current"
    )

snTrapStackingChasFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 168)
)
snTrapStackingChasFanNormal.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasFanIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasFanDescription"))
)
if mibBuilder.loadTexts:
    snTrapStackingChasFanNormal.setStatus(
        "current"
    )

snTrapStackingChasFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 169)
)
snTrapStackingChasFanFailed.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasFanIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasFanDescription"))
)
if mibBuilder.loadTexts:
    snTrapStackingChasFanFailed.setStatus(
        "current"
    )

snTrapStackingManagementMACChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 170)
)
snTrapStackingManagementMACChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapStackingManagementMACChanged.setStatus(
        "current"
    )

snTrapStackingTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 171)
)
snTrapStackingTemperatureWarning.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStackingTemperatureWarning.setStatus(
        "current"
    )

snTrapIfIndexAssignmentChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 172)
)
snTrapIfIndexAssignmentChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIfIndexAssignmentChanged.setStatus(
        "current"
    )

snTrapPBRConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 173)
)
snTrapPBRConfigChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPBRConfigChanged.setStatus(
        "current"
    )

snTrapChasPwrSupplyRPSAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 174)
)
snTrapChasPwrSupplyRPSAdd.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupplyRPSAdd.setStatus(
        "current"
    )

snTrapChasPwrSupplyRPSRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 175)
)
snTrapChasPwrSupplyRPSRemove.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupplyRPSRemove.setStatus(
        "current"
    )

snTrapModuleStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 176)
)
snTrapModuleStatusChange.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdModuleStatus"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapModuleStatusChange.setStatus(
        "current"
    )

snTrapChasHighSpeedFansNeeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 177)
)
snTrapChasHighSpeedFansNeeded.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapChasHighSpeedFansNeeded.setStatus(
        "current"
    )

snTrapSysmaxReverted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 178)
)
snTrapSysmaxReverted.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSysmaxReverted.setStatus(
        "current"
    )

snTrapSysmaxLeftLowMem = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 179)
)
snTrapSysmaxLeftLowMem.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSysmaxLeftLowMem.setStatus(
        "current"
    )

snTrapSysMemoryLowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 180)
)
snTrapSysMemoryLowThreshold.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSysMemoryLowThreshold.setStatus(
        "current"
    )

snTrapSysMemoryOutThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 181)
)
snTrapSysMemoryOutThreshold.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSysMemoryOutThreshold.setStatus(
        "current"
    )

snTrapLinkOAMLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 182)
)
snTrapLinkOAMLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLinkOAMLinkDown.setStatus(
        "current"
    )

snTrapLinkOAMLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 183)
)
snTrapLinkOAMLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLinkOAMLinkUp.setStatus(
        "current"
    )

snTrapI2CAccessLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 184)
)
snTrapI2CAccessLog.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapI2CAccessLog.setStatus(
        "current"
    )

snTrapLinkOAMLoopbackEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 185)
)
snTrapLinkOAMLoopbackEntered.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DOT3-OAM-MIB", "dot3OamLoopbackStatus"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLinkOAMLoopbackEntered.setStatus(
        "current"
    )

snTrapLinkOAMLoopbackCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 186)
)
snTrapLinkOAMLoopbackCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DOT3-OAM-MIB", "dot3OamLoopbackStatus"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLinkOAMLoopbackCleared.setStatus(
        "current"
    )

snTrapLicenseAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 187)
)
snTrapLicenseAdded.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "fdryLicenseType"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLicenseAdded.setStatus(
        "current"
    )

snTrapLicenseRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 188)
)
snTrapLicenseRemoved.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "fdryLicenseType"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLicenseRemoved.setStatus(
        "current"
    )

snTrapLicenseExpires = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 189)
)
snTrapLicenseExpires.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "fdryLicenseType"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLicenseExpires.setStatus(
        "current"
    )

snTrapLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 190)
)
snTrapLicenseExpired.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "fdryLicenseType"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLicenseExpired.setStatus(
        "current"
    )

snTrapUDLDCrcFailureDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 191)
)
snTrapUDLDCrcFailureDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapUDLDCrcFailureDetected.setStatus(
        "current"
    )

snTrapDot1agCfmRemoteMEPAgeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 192)
)
snTrapDot1agCfmRemoteMEPAgeOut.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepState"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapDot1agCfmRemoteMEPAgeOut.setStatus(
        "current"
    )

snTrapDot1agCfmRemoteMEPUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 193)
)
snTrapDot1agCfmRemoteMEPUp.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepState"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapDot1agCfmRemoteMEPUp.setStatus(
        "current"
    )

snTrapDot1agCfmDomainCrossConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 194)
)
snTrapDot1agCfmDomainCrossConnection.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapDot1agCfmDomainCrossConnection.setStatus(
        "current"
    )

snTrapDot1agCfmDuplicateMEPId = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 195)
)
snTrapDot1agCfmDuplicateMEPId.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepState"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapDot1agCfmDuplicateMEPId.setStatus(
        "current"
    )

snTrapStackingStandbyElected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 196)
)
snTrapStackingStandbyElected.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStackingStandbyElected.setStatus(
        "current"
    )

snTrapMacMoveThresholdRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 197)
)
snTrapMacMoveThresholdRate.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacMoveThresholdRate.setStatus(
        "current"
    )

snTrapMacMoveIntervalHistory = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 198)
)
snTrapMacMoveIntervalHistory.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacMoveIntervalHistory.setStatus(
        "current"
    )

snTrapStackingMixedModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 199)
)
snTrapStackingMixedModeChanged.setObjects(
      *(("FOUNDRY-SN-STACKING-MIB", "snStackingGlobalMixedMode"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStackingMixedModeChanged.setStatus(
        "current"
    )

snTrapSysMonErrorDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 200)
)
snTrapSysMonErrorDetect.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSysMonErrorDetect.setStatus(
        "current"
    )

snTrapMacNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 201)
)
snTrapMacNotification.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacNotification.setStatus(
        "current"
    )

snTrapMacEventBufferFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 202)
)
snTrapMacEventBufferFull.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacEventBufferFull.setStatus(
        "current"
    )

snTrapStpDesignatedGuardDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 203)
)
snTrapStpDesignatedGuardDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStpDesignatedGuardDetect.setStatus(
        "current"
    )

snTrapStpDesignatedGuardDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 204)
)
snTrapStpDesignatedGuardDisable.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStpDesignatedGuardDisable.setStatus(
        "current"
    )

snTrapLicenseNNLLTrialNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 205)
)
snTrapLicenseNNLLTrialNotify.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLicenseNNLLTrialNotify.setStatus(
        "current"
    )

snTrapLicenseNNLLTrialExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 206)
)
snTrapLicenseNNLLTrialExpiry.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLicenseNNLLTrialExpiry.setStatus(
        "current"
    )

snTrapLicenseNNLLNonCompliant = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 207)
)
snTrapLicenseNNLLNonCompliant.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLicenseNNLLNonCompliant.setStatus(
        "current"
    )

snTrapLicenseNNLLDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 208)
)
snTrapLicenseNNLLDelete.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLicenseNNLLDelete.setStatus(
        "current"
    )

snTrapStackingShowStackConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 209)
)
snTrapStackingShowStackConnect.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapStackingShowStackConnect.setStatus(
        "current"
    )

snTrapChasFanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1000)
)
snTrapChasFanOK.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasFanIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasFanDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasFanOK.setStatus(
        "current"
    )

snTrapTemperatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1001)
)
snTrapTemperatureOK.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTemperatureOK.setStatus(
        "current"
    )

snTrapCAMOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1002)
)
snTrapCAMOverflow.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapCAMOverflow.setStatus(
        "current"
    )

snTrapOpticalMonitoringWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1003)
)
snTrapOpticalMonitoringWarning.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringWarning.setStatus(
        "current"
    )

snTrapOpticalMonitoringAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1004)
)
snTrapOpticalMonitoringAlarm.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringAlarm.setStatus(
        "current"
    )

snTrapOpticalMonitoringError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1005)
)
snTrapOpticalMonitoringError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringError.setStatus(
        "current"
    )

snTrapPosMonitoringWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1006)
)
snTrapPosMonitoringWarning.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPosMonitoringWarning.setStatus(
        "current"
    )

snTrapPosMonitoringAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1007)
)
snTrapPosMonitoringAlarm.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPosMonitoringAlarm.setStatus(
        "current"
    )

snTrapPosMonitoringError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1008)
)
snTrapPosMonitoringError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPosMonitoringError.setStatus(
        "current"
    )

snTrapXfpSfpIncompatibleOptics = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1009)
)
snTrapXfpSfpIncompatibleOptics.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapXfpSfpIncompatibleOptics.setStatus(
        "current"
    )

snTrapTMLoggingStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1015)
)
snTrapTMLoggingStart.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMLoggingStart.setStatus(
        "current"
    )

snTrapTMLoggingStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1016)
)
snTrapTMLoggingStop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMLoggingStop.setStatus(
        "current"
    )

snTrapTMLoggingRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1017)
)
snTrapTMLoggingRestart.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMLoggingRestart.setStatus(
        "current"
    )

snTrapXfpSfpNotFoundryOptics = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1018)
)
snTrapXfpSfpNotFoundryOptics.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapXfpSfpNotFoundryOptics.setStatus(
        "current"
    )

snTrapTMRecoverySlotReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1019)
)
snTrapTMRecoverySlotReset.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMRecoverySlotReset.setStatus(
        "current"
    )

snTrapTMEgressDataError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1020)
)
snTrapTMEgressDataError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMEgressDataError.setStatus(
        "current"
    )

snTrapSFMLoggingRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1021)
)
snTrapSFMLoggingRestart.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSFMLoggingRestart.setStatus(
        "current"
    )

snTrapNotEnoughFapLinks = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1035)
)
snTrapNotEnoughFapLinks.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapNotEnoughFapLinks.setStatus(
        "current"
    )

snTrapSFMLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1100)
)
snTrapSFMLinkDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSFMLinkDown.setStatus(
        "current"
    )

snTrapSFMLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1101)
)
snTrapSFMLinkUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSFMLinkUp.setStatus(
        "current"
    )

snTrapSFMAccessError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1102)
)
snTrapSFMAccessError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSFMAccessError.setStatus(
        "current"
    )

snTrapSFMStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1103)
)
snTrapSFMStatusChange.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdModuleStatus"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapSFMStatusChange.setStatus(
        "current"
    )

snTrapLPFabricStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1104)
)
snTrapLPFabricStatusChange.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdModuleStatus"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLPFabricStatusChange.setStatus(
        "current"
    )

snTrapModuleNPLockupIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1105)
)
snTrapModuleNPLockupIndication.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"),
        ("BROCADE-NP-TM-STATS-MIB", "brcdNPIndex"),
        ("BROCADE-NP-TM-STATS-MIB", "brcdNPLockupRecoveryCount"))
)
if mibBuilder.loadTexts:
    snTrapModuleNPLockupIndication.setStatus(
        "current"
    )

snTrapModuleNPLockupThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1106)
)
snTrapModuleNPLockupThresholdExceeded.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleNPLockupThresholdExceeded.setStatus(
        "current"
    )

snTrapSFMAutoTuneStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1107)
)
snTrapSFMAutoTuneStart.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSFMAutoTuneStart.setStatus(
        "current"
    )

snTrapSFMAutoTuneFails = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1108)
)
snTrapSFMAutoTuneFails.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSFMAutoTuneFails.setStatus(
        "current"
    )

snTrapSFMAutoTuneComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1109)
)
snTrapSFMAutoTuneComplete.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSFMAutoTuneComplete.setStatus(
        "current"
    )

snTrapTMAutoTuneStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1110)
)
snTrapTMAutoTuneStart.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMAutoTuneStart.setStatus(
        "current"
    )

snTrapTMAutoTuneFails = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1111)
)
snTrapTMAutoTuneFails.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMAutoTuneFails.setStatus(
        "current"
    )

snTrapTMAutoTuneComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1112)
)
snTrapTMAutoTuneComplete.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMAutoTuneComplete.setStatus(
        "current"
    )

snTrapNPILKNCRCError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1113)
)
snTrapNPILKNCRCError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapNPILKNCRCError.setStatus(
        "current"
    )

snTrapARPMACMovement = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1114)
)
snTrapARPMACMovement.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapARPMACMovement.setStatus(
        "current"
    )

snTrapChassisFanSpeedLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1200)
)
snTrapChassisFanSpeedLow.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapChassisFanSpeedLow.setStatus(
        "current"
    )

snTrapChassisFanSpeedMedium = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1201)
)
snTrapChassisFanSpeedMedium.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapChassisFanSpeedMedium.setStatus(
        "current"
    )

snTrapChassisFanSpeedMedHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1202)
)
snTrapChassisFanSpeedMedHigh.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapChassisFanSpeedMedHigh.setStatus(
        "current"
    )

snTrapChassisFanSpeedHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1203)
)
snTrapChassisFanSpeedHigh.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapChassisFanSpeedHigh.setStatus(
        "current"
    )

snTrapFIPSModeEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1207)
)
snTrapFIPSModeEnable.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapFIPSModeEnable.setStatus(
        "current"
    )

snTrapFIPSModeDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1208)
)
snTrapFIPSModeDisable.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapFIPSModeDisable.setStatus(
        "current"
    )

snTrapFIPSHostZeroized = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1209)
)
snTrapFIPSHostZeroized.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapFIPSHostZeroized.setStatus(
        "current"
    )

snTrapFIPSSharedSecretZeroized = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1210)
)
snTrapFIPSSharedSecretZeroized.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapFIPSSharedSecretZeroized.setStatus(
        "current"
    )

snTrapFIPSPOSTStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1211)
)
snTrapFIPSPOSTStatus.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapFIPSPOSTStatus.setStatus(
        "current"
    )

snTrapFIPSCryptoModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1212)
)
snTrapFIPSCryptoModuleFailure.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapFIPSCryptoModuleFailure.setStatus(
        "current"
    )

snTrapLicense2PortNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1213)
)
snTrapLicense2PortNotSupported.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLicense2PortNotSupported.setStatus(
        "current"
    )

snTrapOpticalMonitoringOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1214)
)
snTrapOpticalMonitoringOK.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringOK.setStatus(
        "current"
    )

snTrapSFMAccessOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1215)
)
snTrapSFMAccessOK.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSFMAccessOK.setStatus(
        "current"
    )

snTrapUpgradeSingleCmdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1216)
)
if mibBuilder.loadTexts:
    snTrapUpgradeSingleCmdStart.setStatus(
        "current"
    )

snTrapUpgradeSingleCmdDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1217)
)
snTrapUpgradeSingleCmdDone.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUpgradeSingleCmdDone.setStatus(
        "current"
    )

snTrapAutoUpgradeStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1218)
)
snTrapAutoUpgradeStart.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapAutoUpgradeStart.setStatus(
        "current"
    )

snTrapAutoUpgradeDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1219)
)
snTrapAutoUpgradeDone.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapAutoUpgradeDone.setStatus(
        "current"
    )

snTrapTcamParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1220)
)
snTrapTcamParityError.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapTcamParityError.setStatus(
        "current"
    )

snTrapLPResetOnTcamError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1221)
)
snTrapLPResetOnTcamError.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLPResetOnTcamError.setStatus(
        "current"
    )

snTrapSTPRootGuardViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1230)
)
snTrapSTPRootGuardViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSTPRootGuardViolation.setStatus(
        "current"
    )

snTrapRSTPRootGuardViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1231)
)
snTrapRSTPRootGuardViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapRSTPRootGuardViolation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-NOTIFICATION-MIB",
    **{"snTraps": snTraps,
       "snTrapChasPwrSupply": snTrapChasPwrSupply,
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
       "snTrapPortSecurityShutdown": snTrapPortSecurityShutdown,
       "snTrapMrpStateChange": snTrapMrpStateChange,
       "snTrapMrpCamError": snTrapMrpCamError,
       "snTrapChasPwrSupplyOK": snTrapChasPwrSupplyOK,
       "snTrapVrrpeIfStateChange": snTrapVrrpeIfStateChange,
       "snTrapVsrpIfStateChange": snTrapVsrpIfStateChange,
       "snTrapSrcIpAddressViolation": snTrapSrcIpAddressViolation,
       "snTrapMacAuthEnable": snTrapMacAuthEnable,
       "snTrapMacAuthDisable": snTrapMacAuthDisable,
       "snTrapMacAuthMACAccepted": snTrapMacAuthMACAccepted,
       "snTrapMacAuthMACRejected": snTrapMacAuthMACRejected,
       "snTrapMacAuthPortDisabled": snTrapMacAuthPortDisabled,
       "snTrapClientLoginReject": snTrapClientLoginReject,
       "snTrapLocalUserConfigChange": snTrapLocalUserConfigChange,
       "snTrapVlanConfigChange": snTrapVlanConfigChange,
       "snTrapAclConfigChange": snTrapAclConfigChange,
       "snTrapMacFilterConfigChange": snTrapMacFilterConfigChange,
       "snTrapSNMPConfigChange": snTrapSNMPConfigChange,
       "snTrapSyslogConfigChange": snTrapSyslogConfigChange,
       "snTrapPasswordConfigChange": snTrapPasswordConfigChange,
       "snTrapServerStatusChange": snTrapServerStatusChange,
       "snTrapL4RealServerPortMaxConnectionLimitReached": snTrapL4RealServerPortMaxConnectionLimitReached,
       "snTrapL4LinkDown": snTrapL4LinkDown,
       "snTrapL4LinkUp": snTrapL4LinkUp,
       "snTrapPortPriorityChange": snTrapPortPriorityChange,
       "snTrapAutoPortDisableTrigger": snTrapAutoPortDisableTrigger,
       "snTrapAutoPortDisableRelease": snTrapAutoPortDisableRelease,
       "snTrapPnPStatusChange": snTrapPnPStatusChange,
       "snTrapWirelessIsrpPeerStateChange": snTrapWirelessIsrpPeerStateChange,
       "snTrapWirelessStationStateChange": snTrapWirelessStationStateChange,
       "snTrapWirelessStationRoamingEventTriggered": snTrapWirelessStationRoamingEventTriggered,
       "snTrapWirelessSappStateChange": snTrapWirelessSappStateChange,
       "snTrapExternalPowerConnectionStatus": snTrapExternalPowerConnectionStatus,
       "snTrapDot1xSecurityViolation": snTrapDot1xSecurityViolation,
       "snTrapDot1xPortLinkChange": snTrapDot1xPortLinkChange,
       "snTrapDot1xPortControlChange": snTrapDot1xPortControlChange,
       "snTrapDot1xVlanIdChange": snTrapDot1xVlanIdChange,
       "snTrapDot1xFilterSetupFailure": snTrapDot1xFilterSetupFailure,
       "snTrapDot1xError": snTrapDot1xError,
       "snTrapPortConfigChange": snTrapPortConfigChange,
       "snTrapMacAuthVlanIdChange": snTrapMacAuthVlanIdChange,
       "snTrapWebAuthEnabled": snTrapWebAuthEnabled,
       "snTrapWebAuthDisabled": snTrapWebAuthDisabled,
       "snTrapIpConfigChange": snTrapIpConfigChange,
       "snTrapIpv6ConfigChange": snTrapIpv6ConfigChange,
       "snTrapMacAuthRadiusTimeout": snTrapMacAuthRadiusTimeout,
       "snTrapDot1xRadiusTimeout": snTrapDot1xRadiusTimeout,
       "snTrapUDLDLinkDown": snTrapUDLDLinkDown,
       "snTrapUDLDLinkUp": snTrapUDLDLinkUp,
       "snTrapMacBasedVlanEnabled": snTrapMacBasedVlanEnabled,
       "snTrapMacBasedVlanDisabled": snTrapMacBasedVlanDisabled,
       "snTrapChasFanNormal": snTrapChasFanNormal,
       "snTrapStpRootGuardDetect": snTrapStpRootGuardDetect,
       "snTrapStpRootGuardExpire": snTrapStpRootGuardExpire,
       "snTrapStpBPDUGuardDetect": snTrapStpBPDUGuardDetect,
       "snTrapMstpBPDUGuardDetect": snTrapMstpBPDUGuardDetect,
       "snTrapErrorDisableAction": snTrapErrorDisableAction,
       "snTrapLACPLinkStateChange": snTrapLACPLinkStateChange,
       "snTrapOpticalMonitoringNotFoundryOptics": snTrapOpticalMonitoringNotFoundryOptics,
       "snTrapOpticalMonitoringFoundryOpticsNotCapable": snTrapOpticalMonitoringFoundryOpticsNotCapable,
       "snTrapStaticMulticastMacConfigAdd": snTrapStaticMulticastMacConfigAdd,
       "snTrapStaticMulticastMacConfigRemove": snTrapStaticMulticastMacConfigRemove,
       "snTrapSTPBPDUGuardExpire": snTrapSTPBPDUGuardExpire,
       "snTrapPortLoopDetection": snTrapPortLoopDetection,
       "snTrapNoFreeTcamEntry": snTrapNoFreeTcamEntry,
       "snTrapStackingMasterElected": snTrapStackingMasterElected,
       "snTrapStackingUnitAdded": snTrapStackingUnitAdded,
       "snTrapStackingUnitDeleted": snTrapStackingUnitDeleted,
       "snTrapStackingChasPwrSupplyOK": snTrapStackingChasPwrSupplyOK,
       "snTrapStackingChasPwrSupplyFailed": snTrapStackingChasPwrSupplyFailed,
       "snTrapStackingChasFanNormal": snTrapStackingChasFanNormal,
       "snTrapStackingChasFanFailed": snTrapStackingChasFanFailed,
       "snTrapStackingManagementMACChanged": snTrapStackingManagementMACChanged,
       "snTrapStackingTemperatureWarning": snTrapStackingTemperatureWarning,
       "snTrapIfIndexAssignmentChanged": snTrapIfIndexAssignmentChanged,
       "snTrapPBRConfigChanged": snTrapPBRConfigChanged,
       "snTrapChasPwrSupplyRPSAdd": snTrapChasPwrSupplyRPSAdd,
       "snTrapChasPwrSupplyRPSRemove": snTrapChasPwrSupplyRPSRemove,
       "snTrapModuleStatusChange": snTrapModuleStatusChange,
       "snTrapChasHighSpeedFansNeeded": snTrapChasHighSpeedFansNeeded,
       "snTrapSysmaxReverted": snTrapSysmaxReverted,
       "snTrapSysmaxLeftLowMem": snTrapSysmaxLeftLowMem,
       "snTrapSysMemoryLowThreshold": snTrapSysMemoryLowThreshold,
       "snTrapSysMemoryOutThreshold": snTrapSysMemoryOutThreshold,
       "snTrapLinkOAMLinkDown": snTrapLinkOAMLinkDown,
       "snTrapLinkOAMLinkUp": snTrapLinkOAMLinkUp,
       "snTrapI2CAccessLog": snTrapI2CAccessLog,
       "snTrapLinkOAMLoopbackEntered": snTrapLinkOAMLoopbackEntered,
       "snTrapLinkOAMLoopbackCleared": snTrapLinkOAMLoopbackCleared,
       "snTrapLicenseAdded": snTrapLicenseAdded,
       "snTrapLicenseRemoved": snTrapLicenseRemoved,
       "snTrapLicenseExpires": snTrapLicenseExpires,
       "snTrapLicenseExpired": snTrapLicenseExpired,
       "snTrapUDLDCrcFailureDetected": snTrapUDLDCrcFailureDetected,
       "snTrapDot1agCfmRemoteMEPAgeOut": snTrapDot1agCfmRemoteMEPAgeOut,
       "snTrapDot1agCfmRemoteMEPUp": snTrapDot1agCfmRemoteMEPUp,
       "snTrapDot1agCfmDomainCrossConnection": snTrapDot1agCfmDomainCrossConnection,
       "snTrapDot1agCfmDuplicateMEPId": snTrapDot1agCfmDuplicateMEPId,
       "snTrapStackingStandbyElected": snTrapStackingStandbyElected,
       "snTrapMacMoveThresholdRate": snTrapMacMoveThresholdRate,
       "snTrapMacMoveIntervalHistory": snTrapMacMoveIntervalHistory,
       "snTrapStackingMixedModeChanged": snTrapStackingMixedModeChanged,
       "snTrapSysMonErrorDetect": snTrapSysMonErrorDetect,
       "snTrapMacNotification": snTrapMacNotification,
       "snTrapMacEventBufferFull": snTrapMacEventBufferFull,
       "snTrapStpDesignatedGuardDetect": snTrapStpDesignatedGuardDetect,
       "snTrapStpDesignatedGuardDisable": snTrapStpDesignatedGuardDisable,
       "snTrapLicenseNNLLTrialNotify": snTrapLicenseNNLLTrialNotify,
       "snTrapLicenseNNLLTrialExpiry": snTrapLicenseNNLLTrialExpiry,
       "snTrapLicenseNNLLNonCompliant": snTrapLicenseNNLLNonCompliant,
       "snTrapLicenseNNLLDelete": snTrapLicenseNNLLDelete,
       "snTrapStackingShowStackConnect": snTrapStackingShowStackConnect,
       "snTrapChasFanOK": snTrapChasFanOK,
       "snTrapTemperatureOK": snTrapTemperatureOK,
       "snTrapCAMOverflow": snTrapCAMOverflow,
       "snTrapOpticalMonitoringWarning": snTrapOpticalMonitoringWarning,
       "snTrapOpticalMonitoringAlarm": snTrapOpticalMonitoringAlarm,
       "snTrapOpticalMonitoringError": snTrapOpticalMonitoringError,
       "snTrapPosMonitoringWarning": snTrapPosMonitoringWarning,
       "snTrapPosMonitoringAlarm": snTrapPosMonitoringAlarm,
       "snTrapPosMonitoringError": snTrapPosMonitoringError,
       "snTrapXfpSfpIncompatibleOptics": snTrapXfpSfpIncompatibleOptics,
       "snTrapTMLoggingStart": snTrapTMLoggingStart,
       "snTrapTMLoggingStop": snTrapTMLoggingStop,
       "snTrapTMLoggingRestart": snTrapTMLoggingRestart,
       "snTrapXfpSfpNotFoundryOptics": snTrapXfpSfpNotFoundryOptics,
       "snTrapTMRecoverySlotReset": snTrapTMRecoverySlotReset,
       "snTrapTMEgressDataError": snTrapTMEgressDataError,
       "snTrapSFMLoggingRestart": snTrapSFMLoggingRestart,
       "snTrapNotEnoughFapLinks": snTrapNotEnoughFapLinks,
       "snTrapSFMLinkDown": snTrapSFMLinkDown,
       "snTrapSFMLinkUp": snTrapSFMLinkUp,
       "snTrapSFMAccessError": snTrapSFMAccessError,
       "snTrapSFMStatusChange": snTrapSFMStatusChange,
       "snTrapLPFabricStatusChange": snTrapLPFabricStatusChange,
       "snTrapModuleNPLockupIndication": snTrapModuleNPLockupIndication,
       "snTrapModuleNPLockupThresholdExceeded": snTrapModuleNPLockupThresholdExceeded,
       "snTrapSFMAutoTuneStart": snTrapSFMAutoTuneStart,
       "snTrapSFMAutoTuneFails": snTrapSFMAutoTuneFails,
       "snTrapSFMAutoTuneComplete": snTrapSFMAutoTuneComplete,
       "snTrapTMAutoTuneStart": snTrapTMAutoTuneStart,
       "snTrapTMAutoTuneFails": snTrapTMAutoTuneFails,
       "snTrapTMAutoTuneComplete": snTrapTMAutoTuneComplete,
       "snTrapNPILKNCRCError": snTrapNPILKNCRCError,
       "snTrapARPMACMovement": snTrapARPMACMovement,
       "snTrapChassisFanSpeedLow": snTrapChassisFanSpeedLow,
       "snTrapChassisFanSpeedMedium": snTrapChassisFanSpeedMedium,
       "snTrapChassisFanSpeedMedHigh": snTrapChassisFanSpeedMedHigh,
       "snTrapChassisFanSpeedHigh": snTrapChassisFanSpeedHigh,
       "snTrapFIPSModeEnable": snTrapFIPSModeEnable,
       "snTrapFIPSModeDisable": snTrapFIPSModeDisable,
       "snTrapFIPSHostZeroized": snTrapFIPSHostZeroized,
       "snTrapFIPSSharedSecretZeroized": snTrapFIPSSharedSecretZeroized,
       "snTrapFIPSPOSTStatus": snTrapFIPSPOSTStatus,
       "snTrapFIPSCryptoModuleFailure": snTrapFIPSCryptoModuleFailure,
       "snTrapLicense2PortNotSupported": snTrapLicense2PortNotSupported,
       "snTrapOpticalMonitoringOK": snTrapOpticalMonitoringOK,
       "snTrapSFMAccessOK": snTrapSFMAccessOK,
       "snTrapUpgradeSingleCmdStart": snTrapUpgradeSingleCmdStart,
       "snTrapUpgradeSingleCmdDone": snTrapUpgradeSingleCmdDone,
       "snTrapAutoUpgradeStart": snTrapAutoUpgradeStart,
       "snTrapAutoUpgradeDone": snTrapAutoUpgradeDone,
       "snTrapTcamParityError": snTrapTcamParityError,
       "snTrapLPResetOnTcamError": snTrapLPResetOnTcamError,
       "snTrapSTPRootGuardViolation": snTrapSTPRootGuardViolation,
       "snTrapRSTPRootGuardViolation": snTrapRSTPRootGuardViolation}
)
