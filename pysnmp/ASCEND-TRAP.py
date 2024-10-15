# SNMP MIB module (ASCEND-TRAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-TRAP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:45 2024
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

(wanLineIfIndex,
 wanLineUsage) = mibBuilder.importSymbols(
    "ASCEND-ADVANCED-AGENT-MIB",
    "wanLineIfIndex",
    "wanLineUsage")

(atmpAgentRecvErrorFrom,
 atmpAgentSentErrorTo,
 atmpHNProfileName,
 atmpLastErrorGenerated,
 atmpLastErrorRecv) = mibBuilder.importSymbols(
    "ASCEND-ATMP-MIB",
    "atmpAgentRecvErrorFrom",
    "atmpAgentSentErrorTo",
    "atmpHNProfileName",
    "atmpLastErrorGenerated",
    "atmpLastErrorRecv")

(callLoggingDroppedPacketCount,
 callLoggingServerIPAddress,
 callLoggingServerIndex) = mibBuilder.importSymbols(
    "ASCEND-CALL-LOGGING-MIB",
    "callLoggingDroppedPacketCount",
    "callLoggingServerIPAddress",
    "callLoggingServerIndex")

(cntrReduAvailCurrState,
 cntrReduAvailLastTime,
 cntrReduAvailPrevState,
 cntrReduAvailSlotIndex,
 cntrReduCurrentIndex,
 cntrReduSwitchIndex,
 cntrReduSwitchLastTime,
 cntrReduSwitchReason,
 slotIndex,
 slotStatus) = mibBuilder.importSymbols(
    "ASCEND-CHASSIS-MIB",
    "cntrReduAvailCurrState",
    "cntrReduAvailLastTime",
    "cntrReduAvailPrevState",
    "cntrReduAvailSlotIndex",
    "cntrReduCurrentIndex",
    "cntrReduSwitchIndex",
    "cntrReduSwitchLastTime",
    "cntrReduSwitchReason",
    "slotIndex",
    "slotStatus")

(suspectLanModemBadCount,
 suspectLanModemLast32,
 suspectLanModemPortIndex,
 suspectLanModemSlotIndex,
 suspectLanModemUsedCount) = mibBuilder.importSymbols(
    "ASCEND-LANMODEM-MIB",
    "suspectLanModemBadCount",
    "suspectLanModemLast32",
    "suspectLanModemPortIndex",
    "suspectLanModemSlotIndex",
    "suspectLanModemUsedCount")

(heartBeatMulticastGroupAddress,
 heartBeatPacketCount,
 heartBeatSlotCount,
 heartBeatSlotTimeInterval,
 heartBeatSourceAddress) = mibBuilder.importSymbols(
    "ASCEND-MCAST-MIB",
    "heartBeatMulticastGroupAddress",
    "heartBeatPacketCount",
    "heartBeatSlotCount",
    "heartBeatSlotTimeInterval",
    "heartBeatSourceAddress")

(mgLinkName,
 mgOperStatus) = mibBuilder.importSymbols(
    "ASCEND-MGSTAT-MIB",
    "mgLinkName",
    "mgOperStatus")

(ascend,
 consoleIndex,
 fatalLogIndex,
 fatalLogReason,
 sysAbsoluteCurrentTime,
 sysConfigChange,
 sysLastRestartReason) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "ascend",
    "consoleIndex",
    "fatalLogIndex",
    "fatalLogReason",
    "sysAbsoluteCurrentTime",
    "sysConfigChange",
    "sysLastRestartReason")

(multiShelfState,) = mibBuilder.importSymbols(
    "ASCEND-MULTI-SHELF-MIB",
    "multiShelfState")

(powerSupplyOperationalState,
 powerSupplyState) = mibBuilder.importSymbols(
    "ASCEND-POWER-SUPPLY-MIB",
    "powerSupplyOperationalState",
    "powerSupplyState")

(radAuthHostIPAddress,
 radAuthServerIndex) = mibBuilder.importSymbols(
    "ASCEND-RADIUS-MIB",
    "radAuthHostIPAddress",
    "radAuthServerIndex")

(resourceBadCounts,
 resourceLast32,
 resourcePortIndex,
 resourceSlotIndex,
 resourceUsedCounts) = mibBuilder.importSymbols(
    "ASCEND-RESOURCES-MIB",
    "resourceBadCounts",
    "resourceLast32",
    "resourcePortIndex",
    "resourceSlotIndex",
    "resourceUsedCounts")

(ssnStatusUserIPAddress,) = mibBuilder.importSymbols(
    "ASCEND-SESSION-MIB",
    "ssnStatusUserIPAddress")

(sparingIfLastChangeReason,
 sparingIfLastStatusChange,
 sparingIfPrimaryIndex,
 sparingIfSparingIndex,
 sparingIfStatus,
 sparingSlotLastChangeReason,
 sparingSlotLastStatusChange,
 sparingSlotPrimaryIndex,
 sparingSlotSparingIndex,
 sparingSlotStatus) = mibBuilder.importSymbols(
    "ASCEND-SPARING-MIB",
    "sparingIfLastChangeReason",
    "sparingIfLastStatusChange",
    "sparingIfPrimaryIndex",
    "sparingIfSparingIndex",
    "sparingIfStatus",
    "sparingSlotLastChangeReason",
    "sparingSlotLastStatusChange",
    "sparingSlotPrimaryIndex",
    "sparingSlotSparingIndex",
    "sparingSlotStatus")

(voipCfgGkIndex,
 voipCfgGkIpAddress) = mibBuilder.importSymbols(
    "ASCEND-VOIP-MIB",
    "voipCfgGkIndex",
    "voipCfgGkIpAddress")

(watchdogIndex,
 watchdogName,
 watchdogState) = mibBuilder.importSymbols(
    "ASCEND-WATCHDOG-MIB",
    "watchdogIndex",
    "watchdogName",
    "watchdogState")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName",
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

portInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 0)
)
portInactive.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portInactive.setStatus(
        ""
    )

portDualDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 1)
)
portDualDelay.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portDualDelay.setStatus(
        ""
    )

portWaitSerial = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 2)
)
portWaitSerial.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portWaitSerial.setStatus(
        ""
    )

portHaveSerial = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 3)
)
portHaveSerial.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portHaveSerial.setStatus(
        ""
    )

portRinging = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 4)
)
portRinging.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portRinging.setStatus(
        ""
    )

portCollectDigits = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 5)
)
portCollectDigits.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portCollectDigits.setStatus(
        ""
    )

portWaiting = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 6)
)
portWaiting.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portWaiting.setStatus(
        ""
    )

portConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 7)
)
portConnected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portConnected.setStatus(
        ""
    )

portCarrier = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 8)
)
portCarrier.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portCarrier.setStatus(
        ""
    )

portLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 9)
)
portLoopback.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portLoopback.setStatus(
        ""
    )

portAcrPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 10)
)
portAcrPending.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portAcrPending.setStatus(
        ""
    )

portDteNotReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 11)
)
portDteNotReady.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portDteNotReady.setStatus(
        ""
    )

consoleStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 12)
)
consoleStateChange.setObjects(
      *(("ASCEND-MIB", "consoleIndex"),
        ("ASCEND-SESSION-MIB", "ssnStatusUserIPAddress"))
)
if mibBuilder.loadTexts:
    consoleStateChange.setStatus(
        ""
    )

portUseExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 13)
)
portUseExceeded.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portUseExceeded.setStatus(
        ""
    )

systemUseExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 14)
)
if mibBuilder.loadTexts:
    systemUseExceeded.setStatus(
        ""
    )

maxTelnetAttempts = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 15)
)
maxTelnetAttempts.setObjects(
    ("ASCEND-SESSION-MIB", "ssnStatusUserIPAddress")
)
if mibBuilder.loadTexts:
    maxTelnetAttempts.setStatus(
        ""
    )

eventTableOverwrite = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 16)
)
if mibBuilder.loadTexts:
    eventTableOverwrite.setStatus(
        ""
    )

radiusServerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 18)
)
radiusServerChange.setObjects(
      *(("ASCEND-RADIUS-MIB", "radAuthServerIndex"),
        ("ASCEND-RADIUS-MIB", "radAuthHostIPAddress"))
)
if mibBuilder.loadTexts:
    radiusServerChange.setStatus(
        ""
    )

multicastHeartBeatMonitor = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 19)
)
multicastHeartBeatMonitor.setObjects(
      *(("ASCEND-MCAST-MIB", "heartBeatMulticastGroupAddress"),
        ("ASCEND-MCAST-MIB", "heartBeatSourceAddress"),
        ("ASCEND-MCAST-MIB", "heartBeatSlotTimeInterval"),
        ("ASCEND-MCAST-MIB", "heartBeatSlotCount"),
        ("ASCEND-MCAST-MIB", "heartBeatPacketCount"))
)
if mibBuilder.loadTexts:
    multicastHeartBeatMonitor.setStatus(
        ""
    )

lanModemMovedToSuspectList = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 20)
)
lanModemMovedToSuspectList.setObjects(
      *(("ASCEND-LANMODEM-MIB", "suspectLanModemSlotIndex"),
        ("ASCEND-LANMODEM-MIB", "suspectLanModemPortIndex"),
        ("ASCEND-LANMODEM-MIB", "suspectLanModemUsedCount"),
        ("ASCEND-LANMODEM-MIB", "suspectLanModemBadCount"),
        ("ASCEND-LANMODEM-MIB", "suspectLanModemLast32"))
)
if mibBuilder.loadTexts:
    lanModemMovedToSuspectList.setStatus(
        ""
    )

dirdoListFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 21)
)
dirdoListFailure.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    dirdoListFailure.setStatus(
        ""
    )

sysSlotStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 22)
)
sysSlotStateChange.setObjects(
      *(("ASCEND-CHASSIS-MIB", "slotIndex"),
        ("ASCEND-CHASSIS-MIB", "slotStatus"))
)
if mibBuilder.loadTexts:
    sysSlotStateChange.setStatus(
        ""
    )

powerSupplyStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 23)
)
powerSupplyStateChange.setObjects(
    ("ASCEND-POWER-SUPPLY-MIB", "powerSupplyState")
)
if mibBuilder.loadTexts:
    powerSupplyStateChange.setStatus(
        ""
    )

powerSupplyOperationalStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 24)
)
powerSupplyOperationalStateChange.setObjects(
    ("ASCEND-POWER-SUPPLY-MIB", "powerSupplyOperationalState")
)
if mibBuilder.loadTexts:
    powerSupplyOperationalStateChange.setStatus(
        ""
    )

multiShelfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 25)
)
multiShelfStateChange.setObjects(
    ("ASCEND-MULTI-SHELF-MIB", "multiShelfState")
)
if mibBuilder.loadTexts:
    multiShelfStateChange.setStatus(
        ""
    )

sysLastRestartReasonTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 26)
)
sysLastRestartReasonTrap.setObjects(
      *(("ASCEND-MIB", "sysLastRestartReason"),
        ("ASCEND-MIB", "fatalLogIndex"),
        ("ASCEND-MIB", "sysAbsoluteCurrentTime"))
)
if mibBuilder.loadTexts:
    sysLastRestartReasonTrap.setStatus(
        ""
    )

atmpMaxTunnelExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 27)
)
atmpMaxTunnelExceeded.setObjects(
    ("ASCEND-ATMP-MIB", "atmpHNProfileName")
)
if mibBuilder.loadTexts:
    atmpMaxTunnelExceeded.setStatus(
        ""
    )

atmpAgentErrorSentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 28)
)
atmpAgentErrorSentTrap.setObjects(
      *(("ASCEND-ATMP-MIB", "atmpLastErrorGenerated"),
        ("ASCEND-ATMP-MIB", "atmpAgentSentErrorTo"))
)
if mibBuilder.loadTexts:
    atmpAgentErrorSentTrap.setStatus(
        ""
    )

atmpAgentErrorRecvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 29)
)
atmpAgentErrorRecvTrap.setObjects(
      *(("ASCEND-ATMP-MIB", "atmpLastErrorRecv"),
        ("ASCEND-ATMP-MIB", "atmpAgentRecvErrorFrom"))
)
if mibBuilder.loadTexts:
    atmpAgentErrorRecvTrap.setStatus(
        ""
    )

sysConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 30)
)
sysConfigChangeTrap.setObjects(
    ("ASCEND-MIB", "sysConfigChange")
)
if mibBuilder.loadTexts:
    sysConfigChangeTrap.setStatus(
        ""
    )

sdtnPrimaryListEmptyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 31)
)
if mibBuilder.loadTexts:
    sdtnPrimaryListEmptyTrap.setStatus(
        ""
    )

sdtnSecondaryListEmptyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 32)
)
if mibBuilder.loadTexts:
    sdtnSecondaryListEmptyTrap.setStatus(
        ""
    )

systemClockDrifted = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 33)
)
if mibBuilder.loadTexts:
    systemClockDrifted.setStatus(
        ""
    )

suspectAccessResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 34)
)
suspectAccessResource.setObjects(
      *(("ASCEND-RESOURCES-MIB", "resourceSlotIndex"),
        ("ASCEND-RESOURCES-MIB", "resourcePortIndex"),
        ("ASCEND-RESOURCES-MIB", "resourceUsedCounts"),
        ("ASCEND-RESOURCES-MIB", "resourceBadCounts"),
        ("ASCEND-RESOURCES-MIB", "resourceLast32"))
)
if mibBuilder.loadTexts:
    suspectAccessResource.setStatus(
        ""
    )

watchdogWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 35)
)
watchdogWarningTrap.setObjects(
      *(("ASCEND-WATCHDOG-MIB", "watchdogIndex"),
        ("ASCEND-WATCHDOG-MIB", "watchdogName"),
        ("ASCEND-WATCHDOG-MIB", "watchdogState"),
        ("ASCEND-MIB", "sysAbsoluteCurrentTime"))
)
if mibBuilder.loadTexts:
    watchdogWarningTrap.setStatus(
        ""
    )

slotCardResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 36)
)
slotCardResetTrap.setObjects(
      *(("ASCEND-MIB", "fatalLogIndex"),
        ("ASCEND-MIB", "fatalLogReason"),
        ("ASCEND-MIB", "sysAbsoluteCurrentTime"),
        ("ASCEND-CHASSIS-MIB", "slotIndex"))
)
if mibBuilder.loadTexts:
    slotCardResetTrap.setStatus(
        ""
    )

controllerSwitchoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 37)
)
controllerSwitchoverTrap.setObjects(
      *(("ASCEND-MIB", "sysAbsoluteCurrentTime"),
        ("ASCEND-CHASSIS-MIB", "cntrReduSwitchReason"),
        ("ASCEND-CHASSIS-MIB", "cntrReduSwitchIndex"),
        ("ASCEND-CHASSIS-MIB", "cntrReduCurrentIndex"))
)
if mibBuilder.loadTexts:
    controllerSwitchoverTrap.setStatus(
        ""
    )

callLogServChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 38)
)
callLogServChange.setObjects(
      *(("ASCEND-CALL-LOGGING-MIB", "callLoggingServerIndex"),
        ("ASCEND-CALL-LOGGING-MIB", "callLoggingServerIPAddress"),
        ("ASCEND-MIB", "sysAbsoluteCurrentTime"))
)
if mibBuilder.loadTexts:
    callLogServChange.setStatus(
        ""
    )

voipGkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 39)
)
voipGkChange.setObjects(
      *(("ASCEND-VOIP-MIB", "voipCfgGkIndex"),
        ("ASCEND-VOIP-MIB", "voipCfgGkIpAddress"),
        ("ASCEND-MIB", "sysAbsoluteCurrentTime"))
)
if mibBuilder.loadTexts:
    voipGkChange.setStatus(
        ""
    )

wanLineStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 40)
)
wanLineStateChange.setObjects(
      *(("ASCEND-ADVANCED-AGENT-MIB", "wanLineIfIndex"),
        ("ASCEND-ADVANCED-AGENT-MIB", "wanLineUsage"),
        ("ASCEND-MIB", "sysAbsoluteCurrentTime"))
)
if mibBuilder.loadTexts:
    wanLineStateChange.setStatus(
        ""
    )

callLogDroppedPkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 41)
)
callLogDroppedPkt.setObjects(
    ("ASCEND-CALL-LOGGING-MIB", "callLoggingDroppedPacketCount")
)
if mibBuilder.loadTexts:
    callLogDroppedPkt.setStatus(
        ""
    )

megacoLinkStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 42)
)
megacoLinkStatusTrap.setObjects(
      *(("ASCEND-MGSTAT-MIB", "mgLinkName"),
        ("ASCEND-MGSTAT-MIB", "mgOperStatus"))
)
if mibBuilder.loadTexts:
    megacoLinkStatusTrap.setStatus(
        ""
    )

sparingSlotStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 43)
)
sparingSlotStatusChange.setObjects(
      *(("ASCEND-SPARING-MIB", "sparingSlotPrimaryIndex"),
        ("ASCEND-SPARING-MIB", "sparingSlotSparingIndex"),
        ("ASCEND-SPARING-MIB", "sparingSlotStatus"),
        ("ASCEND-SPARING-MIB", "sparingSlotLastStatusChange"),
        ("ASCEND-SPARING-MIB", "sparingSlotLastChangeReason"))
)
if mibBuilder.loadTexts:
    sparingSlotStatusChange.setStatus(
        ""
    )

sparingIfStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 44)
)
sparingIfStatusChange.setObjects(
      *(("ASCEND-SPARING-MIB", "sparingIfPrimaryIndex"),
        ("ASCEND-SPARING-MIB", "sparingIfSparingIndex"),
        ("ASCEND-SPARING-MIB", "sparingIfStatus"),
        ("ASCEND-SPARING-MIB", "sparingIfLastStatusChange"),
        ("ASCEND-SPARING-MIB", "sparingIfLastChangeReason"))
)
if mibBuilder.loadTexts:
    sparingIfStatusChange.setStatus(
        ""
    )

cntrReduAvailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 529, 0, 45)
)
cntrReduAvailTrap.setObjects(
      *(("ASCEND-CHASSIS-MIB", "cntrReduAvailLastTime"),
        ("ASCEND-CHASSIS-MIB", "cntrReduAvailSlotIndex"),
        ("ASCEND-CHASSIS-MIB", "cntrReduAvailPrevState"),
        ("ASCEND-CHASSIS-MIB", "cntrReduAvailCurrState"))
)
if mibBuilder.loadTexts:
    cntrReduAvailTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-TRAP",
    **{"portInactive": portInactive,
       "portDualDelay": portDualDelay,
       "portWaitSerial": portWaitSerial,
       "portHaveSerial": portHaveSerial,
       "portRinging": portRinging,
       "portCollectDigits": portCollectDigits,
       "portWaiting": portWaiting,
       "portConnected": portConnected,
       "portCarrier": portCarrier,
       "portLoopback": portLoopback,
       "portAcrPending": portAcrPending,
       "portDteNotReady": portDteNotReady,
       "consoleStateChange": consoleStateChange,
       "portUseExceeded": portUseExceeded,
       "systemUseExceeded": systemUseExceeded,
       "maxTelnetAttempts": maxTelnetAttempts,
       "eventTableOverwrite": eventTableOverwrite,
       "radiusServerChange": radiusServerChange,
       "multicastHeartBeatMonitor": multicastHeartBeatMonitor,
       "lanModemMovedToSuspectList": lanModemMovedToSuspectList,
       "dirdoListFailure": dirdoListFailure,
       "sysSlotStateChange": sysSlotStateChange,
       "powerSupplyStateChange": powerSupplyStateChange,
       "powerSupplyOperationalStateChange": powerSupplyOperationalStateChange,
       "multiShelfStateChange": multiShelfStateChange,
       "sysLastRestartReasonTrap": sysLastRestartReasonTrap,
       "atmpMaxTunnelExceeded": atmpMaxTunnelExceeded,
       "atmpAgentErrorSentTrap": atmpAgentErrorSentTrap,
       "atmpAgentErrorRecvTrap": atmpAgentErrorRecvTrap,
       "sysConfigChangeTrap": sysConfigChangeTrap,
       "sdtnPrimaryListEmptyTrap": sdtnPrimaryListEmptyTrap,
       "sdtnSecondaryListEmptyTrap": sdtnSecondaryListEmptyTrap,
       "systemClockDrifted": systemClockDrifted,
       "suspectAccessResource": suspectAccessResource,
       "watchdogWarningTrap": watchdogWarningTrap,
       "slotCardResetTrap": slotCardResetTrap,
       "controllerSwitchoverTrap": controllerSwitchoverTrap,
       "callLogServChange": callLogServChange,
       "voipGkChange": voipGkChange,
       "wanLineStateChange": wanLineStateChange,
       "callLogDroppedPkt": callLogDroppedPkt,
       "megacoLinkStatusTrap": megacoLinkStatusTrap,
       "sparingSlotStatusChange": sparingSlotStatusChange,
       "sparingIfStatusChange": sparingIfStatusChange,
       "cntrReduAvailTrap": cntrReduAvailTrap}
)
