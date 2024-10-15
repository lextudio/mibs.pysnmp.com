# SNMP MIB module (HP-SN-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-MIBS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:48 2024
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
    "HP-SN-AGENT-MIB",
    "snAgGblTrapMessage",
    "snAgentBrdIndex",
    "snChasFanDescription",
    "snChasFanIndex",
    "snChasPwrSupplyDescription",
    "snChasPwrSupplyIndex",
    "snChasPwrSupplyStatus")

(hp,) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "hp")

(snL4MaxSessionLimit,
 snL4TcpSynLimit,
 snL4TrapRealServerCurConnections,
 snL4TrapRealServerIP,
 snL4TrapRealServerName,
 snL4TrapRealServerPort) = mibBuilder.importSymbols(
    "HP-SN-SW-L4-SWITCH-GROUP-MIB",
    "snL4MaxSessionLimit",
    "snL4TcpSynLimit",
    "snL4TrapRealServerCurConnections",
    "snL4TrapRealServerIP",
    "snL4TrapRealServerName",
    "snL4TrapRealServerPort")

(snSwViolatorMacAddress,
 snSwViolatorPortNumber) = mibBuilder.importSymbols(
    "HP-SN-SWITCH-GROUP-MIB",
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
    (1, 3, 6, 1, 4, 1, 11, 0, 1)
)
snTrapChasPwrSupply.setObjects(
    ("HP-SN-AGENT-MIB", "snChasPwrSupplyStatus")
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupply.setStatus(
        ""
    )

snTrapLockedAddressViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 2)
)
snTrapLockedAddressViolation.setObjects(
      *(("HP-SN-SWITCH-GROUP-MIB", "snSwViolatorPortNumber"),
        ("HP-SN-SWITCH-GROUP-MIB", "snSwViolatorMacAddress"))
)
if mibBuilder.loadTexts:
    snTrapLockedAddressViolation.setStatus(
        ""
    )

snTrapL4MaxSessionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 19)
)
snTrapL4MaxSessionLimitReached.setObjects(
    ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4MaxSessionLimit")
)
if mibBuilder.loadTexts:
    snTrapL4MaxSessionLimitReached.setStatus(
        ""
    )

snTrapL4TcpSynLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 20)
)
snTrapL4TcpSynLimitReached.setObjects(
    ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TcpSynLimit")
)
if mibBuilder.loadTexts:
    snTrapL4TcpSynLimitReached.setStatus(
        ""
    )

snTrapL4RealServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 21)
)
snTrapL4RealServerUp.setObjects(
      *(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerUp.setStatus(
        ""
    )

snTrapL4RealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 22)
)
snTrapL4RealServerDown.setObjects(
      *(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerDown.setStatus(
        ""
    )

snTrapL4RealServerPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 23)
)
snTrapL4RealServerPortUp.setObjects(
      *(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"),
        ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerPortUp.setStatus(
        ""
    )

snTrapL4RealServerPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 24)
)
snTrapL4RealServerPortDown.setObjects(
      *(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"),
        ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerPort"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerPortDown.setStatus(
        ""
    )

snTrapL4RealServerMaxConnectionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 25)
)
snTrapL4RealServerMaxConnectionLimitReached.setObjects(
      *(("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerIP"),
        ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerName"),
        ("HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4TrapRealServerCurConnections"))
)
if mibBuilder.loadTexts:
    snTrapL4RealServerMaxConnectionLimitReached.setStatus(
        ""
    )

snTrapL4BecomeStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 26)
)
if mibBuilder.loadTexts:
    snTrapL4BecomeStandby.setStatus(
        ""
    )

snTrapL4BecomeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 27)
)
if mibBuilder.loadTexts:
    snTrapL4BecomeActive.setStatus(
        ""
    )

snTrapModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 28)
)
snTrapModuleInserted.setObjects(
    ("HP-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleInserted.setStatus(
        ""
    )

snTrapModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 29)
)
snTrapModuleRemoved.setObjects(
    ("HP-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleRemoved.setStatus(
        ""
    )

snTrapChasPwrSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 30)
)
snTrapChasPwrSupplyFailed.setObjects(
      *(("HP-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("HP-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupplyFailed.setStatus(
        ""
    )

snTrapChasFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 31)
)
snTrapChasFanFailed.setObjects(
      *(("HP-SN-AGENT-MIB", "snChasFanIndex"),
        ("HP-SN-AGENT-MIB", "snChasFanDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasFanFailed.setStatus(
        ""
    )

snTrapLockedAddressViolation2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 32)
)
snTrapLockedAddressViolation2.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLockedAddressViolation2.setStatus(
        ""
    )

snTrapFsrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 33)
)
snTrapFsrpIfStateChange.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapFsrpIfStateChange.setStatus(
        ""
    )

snTrapVrrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 34)
)
snTrapVrrpIfStateChange.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVrrpIfStateChange.setStatus(
        ""
    )

snTrapMgmtModuleRedunStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 35)
)
snTrapMgmtModuleRedunStateChange.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMgmtModuleRedunStateChange.setStatus(
        ""
    )

snTrapTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 36)
)
snTrapTemperatureWarning.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTemperatureWarning.setStatus(
        ""
    )

snTrapAccessListDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 37)
)
snTrapAccessListDeny.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAccessListDeny.setStatus(
        ""
    )

snTrapMacFilterDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 38)
)
snTrapMacFilterDeny.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacFilterDeny.setStatus(
        ""
    )

snTrapL4GslbRemoteUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 39)
)
snTrapL4GslbRemoteUp.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteUp.setStatus(
        ""
    )

snTrapL4GslbRemoteDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 40)
)
snTrapL4GslbRemoteDown.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteDown.setStatus(
        ""
    )

snTrapL4GslbRemoteControllerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 41)
)
snTrapL4GslbRemoteControllerUp.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteControllerUp.setStatus(
        ""
    )

snTrapL4GslbRemoteControllerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 42)
)
snTrapL4GslbRemoteControllerDown.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbRemoteControllerDown.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 43)
)
snTrapL4GslbHealthCheckIpUp.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpUp.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 44)
)
snTrapL4GslbHealthCheckIpDown.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpDown.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 45)
)
snTrapL4GslbHealthCheckIpPortUp.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpPortUp.setStatus(
        ""
    )

snTrapL4GslbHealthCheckIpPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 46)
)
snTrapL4GslbHealthCheckIpPortDown.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4GslbHealthCheckIpPortDown.setStatus(
        ""
    )

snTrapL4FirewallBecomeStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 47)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallBecomeStandby.setStatus(
        ""
    )

snTrapL4FirewallBecomeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 48)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallBecomeActive.setStatus(
        ""
    )

snTrapL4FirewallPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 49)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallPathUp.setStatus(
        ""
    )

snTrapL4FirewallPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 50)
)
if mibBuilder.loadTexts:
    snTrapL4FirewallPathDown.setStatus(
        ""
    )

snTrapIcmpLocalExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 51)
)
snTrapIcmpLocalExceedBurst.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIcmpLocalExceedBurst.setStatus(
        ""
    )

snTrapIcmpTransitExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 52)
)
snTrapIcmpTransitExceedBurst.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIcmpTransitExceedBurst.setStatus(
        ""
    )

snTrapTcpLocalExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 53)
)
snTrapTcpLocalExceedBurst.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTcpLocalExceedBurst.setStatus(
        ""
    )

snTrapTcpTransitExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 54)
)
snTrapTcpTransitExceedBurst.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTcpTransitExceedBurst.setStatus(
        ""
    )

snTrapL4ContentVerification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 55)
)
if mibBuilder.loadTexts:
    snTrapL4ContentVerification.setStatus(
        ""
    )

snTrapDuplicateIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 56)
)
if mibBuilder.loadTexts:
    snTrapDuplicateIp.setStatus(
        ""
    )

snTrapMplsProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 57)
)
if mibBuilder.loadTexts:
    snTrapMplsProblem.setStatus(
        ""
    )

snTrapMplsException = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 58)
)
if mibBuilder.loadTexts:
    snTrapMplsException.setStatus(
        ""
    )

snTrapMplsAudit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 59)
)
if mibBuilder.loadTexts:
    snTrapMplsAudit.setStatus(
        ""
    )

snTrapMplsDeveloper = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 60)
)
if mibBuilder.loadTexts:
    snTrapMplsDeveloper.setStatus(
        ""
    )

snTrapNoBmFreeQueue = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 61)
)
snTrapNoBmFreeQueue.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapNoBmFreeQueue.setStatus(
        ""
    )

snTrapSmcDmaDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 62)
)
snTrapSmcDmaDrop.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSmcDmaDrop.setStatus(
        ""
    )

snTrapSmcBpDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 63)
)
snTrapSmcBpDrop.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSmcBpDrop.setStatus(
        ""
    )

snTrapBmWriteSeqDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 64)
)
snTrapBmWriteSeqDrop.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBmWriteSeqDrop.setStatus(
        ""
    )

snTrapBgpPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 65)
)
snTrapBgpPeerUp.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBgpPeerUp.setStatus(
        ""
    )

snTrapBgpPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 66)
)
snTrapBgpPeerDown.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBgpPeerDown.setStatus(
        ""
    )

snTrapL4RealServerResponseTimeLowerLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 67)
)
snTrapL4RealServerResponseTimeLowerLimit.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4RealServerResponseTimeLowerLimit.setStatus(
        ""
    )

snTrapL4RealServerResponseTimeUpperLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 68)
)
snTrapL4RealServerResponseTimeUpperLimit.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4RealServerResponseTimeUpperLimit.setStatus(
        ""
    )

snTrapL4TcpAttackRateExceedMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 69)
)
snTrapL4TcpAttackRateExceedMax.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4TcpAttackRateExceedMax.setStatus(
        ""
    )

snTrapL4TcpAttackRateExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 70)
)
snTrapL4TcpAttackRateExceedThreshold.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4TcpAttackRateExceedThreshold.setStatus(
        ""
    )

snTrapL4ConnectionRateExceedMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 71)
)
snTrapL4ConnectionRateExceedMax.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4ConnectionRateExceedMax.setStatus(
        ""
    )

snTrapL4ConnectionRateExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 72)
)
snTrapL4ConnectionRateExceedThreshold.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapL4ConnectionRateExceedThreshold.setStatus(
        ""
    )

snTrapRunningConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 73)
)
snTrapRunningConfigChanged.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapRunningConfigChanged.setStatus(
        ""
    )

snTrapStartupConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 74)
)
snTrapStartupConfigChanged.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapStartupConfigChanged.setStatus(
        ""
    )

snTrapUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 75)
)
snTrapUserLogin.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUserLogin.setStatus(
        ""
    )

snTrapUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 76)
)
snTrapUserLogout.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUserLogout.setStatus(
        ""
    )

snTrapPortSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 77)
)
snTrapPortSecurityViolation.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortSecurityViolation.setStatus(
        ""
    )

snTrapPortSecurityShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 78)
)
snTrapPortSecurityShutdown.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortSecurityShutdown.setStatus(
        ""
    )

snTrapMrpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 79)
)
snTrapMrpStateChange.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMrpStateChange.setStatus(
        ""
    )

snTrapMrpCamError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 80)
)
snTrapMrpCamError.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMrpCamError.setStatus(
        ""
    )

snTrapChasPwrSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 81)
)
snTrapChasPwrSupplyOK.setObjects(
      *(("HP-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("HP-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupplyOK.setStatus(
        ""
    )

snTrapVrrpeIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 82)
)
snTrapVrrpeIfStateChange.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVrrpeIfStateChange.setStatus(
        ""
    )

snTrapVsrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 0, 83)
)
snTrapVsrpIfStateChange.setObjects(
    ("HP-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVsrpIfStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-TRAP-MIB",
    **{"snTrapChasPwrSupply": snTrapChasPwrSupply,
       "snTrapLockedAddressViolation": snTrapLockedAddressViolation,
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
       "snTrapVsrpIfStateChange": snTrapVsrpIfStateChange}
)
