# SNMP MIB module (VISM-NONAXIPOP-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VISM-NONAXIPOP-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:41 2024
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

(functionModuleType,
 moduleSlotNumber,
 moduleTrapAlarmSeverity) = mibBuilder.importSymbols(
    "BASIS-GENERIC-MIB",
    "functionModuleType",
    "moduleSlotNumber",
    "moduleTrapAlarmSeverity")

(basis,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "basis")

(shelfNodeName,
 shelfNum) = mibBuilder.importSymbols(
    "BASIS-SHELF-MIB",
    "shelfNodeName",
    "shelfNum")

(cwAnnFileCodec,
 cwAnnFileName,
 cwAnnFileStatus) = mibBuilder.importSymbols(
    "CISCO-WAN-ANNOUNCEMENT-MIB",
    "cwAnnFileCodec",
    "cwAnnFileName",
    "cwAnnFileStatus")

(vismTrapIntIndex1,
 vismTrapIntIndex2) = mibBuilder.importSymbols(
    "CISCO-WAN-AXIPOP-MIB",
    "vismTrapIntIndex1",
    "vismTrapIntIndex2")

(vismLapdTrunkState,) = mibBuilder.importSymbols(
    "CISCO-WAN-LAPD-TRUNK-MIB",
    "vismLapdTrunkState")

(mgAdministrativeState,
 mgDnsResolutionType,
 mgDomainName,
 mgEndpointChannelMap,
 mgEndpointLineNumber,
 mgEndpointState,
 mgcAssociationState,
 mgcName,
 mgcResolutionCommState,
 mgcResolutionIpAddress,
 mgcResolutionName) = mibBuilder.importSymbols(
    "CISCO-WAN-MG-MIB",
    "mgAdministrativeState",
    "mgDnsResolutionType",
    "mgDomainName",
    "mgEndpointChannelMap",
    "mgEndpointLineNumber",
    "mgEndpointState",
    "mgcAssociationState",
    "mgcName",
    "mgcResolutionCommState",
    "mgcResolutionIpAddress",
    "mgcResolutionName")

(mgcRedundancyGrpActState,) = mibBuilder.importSymbols(
    "CISCO-WAN-MGC-REDUN-MIB",
    "mgcRedundancyGrpActState")

(persistentXgcpEventName,) = mibBuilder.importSymbols(
    "CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB",
    "persistentXgcpEventName")

(vismRtpConnAlarmState,
 vismRtpFailReason,
 vismRtpLcn) = mibBuilder.importSymbols(
    "CISCO-WAN-RTP-CONN-MIB",
    "vismRtpConnAlarmState",
    "vismRtpFailReason",
    "vismRtpLcn")

(srcpPeerGrpTimeSinceHeartbeat,
 srcpPeerTimeSinceHeartbeat) = mibBuilder.importSymbols(
    "CISCO-WAN-SRCP-MIB",
    "srcpPeerGrpTimeSinceHeartbeat",
    "srcpPeerTimeSinceHeartbeat")

(tonePlanFileName,
 tonePlanRegionName,
 tonePlanVersionNumber) = mibBuilder.importSymbols(
    "CISCO-WAN-VISM-TONE-PLAN-MIB",
    "tonePlanFileName",
    "tonePlanRegionName",
    "tonePlanVersionNumber")

(genericTimeStamp,) = mibBuilder.importSymbols(
    "GENERICOBJECT-MIB",
    "genericTimeStamp")

(intSrvFlowStatus,) = mibBuilder.importSymbols(
    "INT-SERV-MIB",
    "intSrvFlowStatus")

(rsvpResvFwdStatus,
 rsvpResvStatus,
 rsvpSenderStatus,
 rsvpSessionDestAddr) = mibBuilder.importSymbols(
    "RSVP-MIB",
    "rsvpResvFwdStatus",
    "rsvpResvStatus",
    "rsvpSenderStatus",
    "rsvpSessionDestAddr")

(lastSequenceNumber,) = mibBuilder.importSymbols(
    "RTM-MIB",
    "lastSequenceNumber")

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

(vismLapdDlcIndex,
 vismLapdDlcLinkState,
 vismLapdDlcSapi,
 vismLapdDlcTei,
 vismLapdIndex) = mibBuilder.importSymbols(
    "VISM-LAPD-MIB",
    "vismLapdDlcIndex",
    "vismLapdDlcLinkState",
    "vismLapdDlcSapi",
    "vismLapdDlcTei",
    "vismLapdIndex")

(vismRudpSessionNum,
 vismRudpSessionState,
 vismSessionGrpNum,
 vismSessionGrpState,
 vismSessionSetNum,
 vismSessionSetState) = mibBuilder.importSymbols(
    "VISM-SESSION-MIB",
    "vismRudpSessionNum",
    "vismRudpSessionState",
    "vismSessionGrpNum",
    "vismSessionGrpState",
    "vismSessionSetNum",
    "vismSessionSetState")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

vismRtpConnAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50650)
)
vismRtpConnAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpLcn"))
)
if mibBuilder.loadTexts:
    vismRtpConnAdded.setStatus(
        ""
    )

vismRtpConnDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50651)
)
vismRtpConnDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpLcn"))
)
if mibBuilder.loadTexts:
    vismRtpConnDeleted.setStatus(
        ""
    )

vismRtpConnStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50652)
)
vismRtpConnStateChg.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpConnAlarmState"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpLcn"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpFailReason"))
)
if mibBuilder.loadTexts:
    vismRtpConnStateChg.setStatus(
        ""
    )

vismLapdTrStateIs = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50653)
)
vismLapdTrStateIs.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTrunkState"))
)
if mibBuilder.loadTexts:
    vismLapdTrStateIs.setStatus(
        ""
    )

vismLapdTrStateOos = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50654)
)
vismLapdTrStateOos.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTrunkState"))
)
if mibBuilder.loadTexts:
    vismLapdTrStateOos.setStatus(
        ""
    )

vismLapdTrunkAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50655)
)
vismLapdTrunkAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"))
)
if mibBuilder.loadTexts:
    vismLapdTrunkAdded.setStatus(
        ""
    )

vismLapdTrunkDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50656)
)
vismLapdTrunkDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"))
)
if mibBuilder.loadTexts:
    vismLapdTrunkDeleted.setStatus(
        ""
    )

mgcRedundancyGrpAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50657)
)
mgcRedundancyGrpAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex2"))
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpAdded.setStatus(
        ""
    )

mgcRedundancyGrpDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50658)
)
mgcRedundancyGrpDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex2"))
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpDeleted.setStatus(
        ""
    )

mgcRedundancyGrpCommOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50659)
)
mgcRedundancyGrpCommOk.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"))
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpCommOk.setStatus(
        ""
    )

mgcRedundancyGrpCommLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50660)
)
mgcRedundancyGrpCommLoss.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"))
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpCommLoss.setStatus(
        ""
    )

mgcRedundancyGrpProtocolAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50661)
)
mgcRedundancyGrpProtocolAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex2"))
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpProtocolAdded.setStatus(
        ""
    )

mgcRedundancyGrpProtocolDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50662)
)
mgcRedundancyGrpProtocolDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex2"))
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpProtocolDeleted.setStatus(
        ""
    )

peerGrpHeartbeatLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50663)
)
peerGrpHeartbeatLost.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerGrpTimeSinceHeartbeat"))
)
if mibBuilder.loadTexts:
    peerGrpHeartbeatLost.setStatus(
        ""
    )

peerGrpHeartbeatDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50664)
)
peerGrpHeartbeatDetected.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerGrpTimeSinceHeartbeat"))
)
if mibBuilder.loadTexts:
    peerGrpHeartbeatDetected.setStatus(
        ""
    )

mgcActiveInGrp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50665)
)
mgcActiveInGrp.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex2"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpActState"))
)
if mibBuilder.loadTexts:
    mgcActiveInGrp.setStatus(
        ""
    )

mgcInactiveInGrp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50666)
)
mgcInactiveInGrp.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex2"),
        ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpActState"))
)
if mibBuilder.loadTexts:
    mgcInactiveInGrp.setStatus(
        ""
    )

mgcRedundancyGrpParamEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50668)
)
mgcRedundancyGrpParamEntryAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"))
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpParamEntryAdded.setStatus(
        ""
    )

mgcRedundancyGrpParamEntryDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50669)
)
mgcRedundancyGrpParamEntryDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"))
)
if mibBuilder.loadTexts:
    mgcRedundancyGrpParamEntryDeleted.setStatus(
        ""
    )

srcpPeerGrpParamEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50670)
)
srcpPeerGrpParamEntryAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"))
)
if mibBuilder.loadTexts:
    srcpPeerGrpParamEntryAdded.setStatus(
        ""
    )

srcpPeerGrpParamEntryDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50671)
)
srcpPeerGrpParamEntryDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"))
)
if mibBuilder.loadTexts:
    srcpPeerGrpParamEntryDeleted.setStatus(
        ""
    )

newFlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50672)
)
newFlow.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("INT-SERV-MIB", "intSrvFlowStatus"),
        ("RSVP-MIB", "rsvpSessionDestAddr"),
        ("RSVP-MIB", "rsvpResvFwdStatus"),
        ("RSVP-MIB", "rsvpResvStatus"),
        ("RSVP-MIB", "rsvpSenderStatus"))
)
if mibBuilder.loadTexts:
    newFlow.setStatus(
        ""
    )

lostFlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50673)
)
lostFlow.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("INT-SERV-MIB", "intSrvFlowStatus"),
        ("RSVP-MIB", "rsvpSessionDestAddr"),
        ("RSVP-MIB", "rsvpResvFwdStatus"),
        ("RSVP-MIB", "rsvpResvStatus"),
        ("RSVP-MIB", "rsvpSenderStatus"))
)
if mibBuilder.loadTexts:
    lostFlow.setStatus(
        ""
    )

cwAnnFileAddStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50674)
)
cwAnnFileAddStarted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileName"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileCodec"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileStatus"))
)
if mibBuilder.loadTexts:
    cwAnnFileAddStarted.setStatus(
        ""
    )

cwAnnFileLoadComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50675)
)
cwAnnFileLoadComplete.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileName"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileCodec"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileStatus"))
)
if mibBuilder.loadTexts:
    cwAnnFileLoadComplete.setStatus(
        ""
    )

cwAnnFileLoadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50676)
)
cwAnnFileLoadFailed.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileName"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileCodec"),
        ("CISCO-WAN-ANNOUNCEMENT-MIB", "cwAnnFileStatus"))
)
if mibBuilder.loadTexts:
    cwAnnFileLoadFailed.setStatus(
        ""
    )

cwAnnFileDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50677)
)
cwAnnFileDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"))
)
if mibBuilder.loadTexts:
    cwAnnFileDeleted.setStatus(
        ""
    )

mgAdministrativeStateLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50719)
)
mgAdministrativeStateLocked.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-MG-MIB", "mgAdministrativeState"))
)
if mibBuilder.loadTexts:
    mgAdministrativeStateLocked.setStatus(
        ""
    )

mgAdministrativeStateUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50720)
)
mgAdministrativeStateUnlocked.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-MG-MIB", "mgAdministrativeState"))
)
if mibBuilder.loadTexts:
    mgAdministrativeStateUnlocked.setStatus(
        ""
    )

mgAdministrativeStateShuttingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50721)
)
mgAdministrativeStateShuttingDown.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-MG-MIB", "mgAdministrativeState"))
)
if mibBuilder.loadTexts:
    mgAdministrativeStateShuttingDown.setStatus(
        ""
    )

mgcAssociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50722)
)
mgcAssociated.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgcName"),
        ("CISCO-WAN-MG-MIB", "mgcAssociationState"))
)
if mibBuilder.loadTexts:
    mgcAssociated.setStatus(
        ""
    )

mgcUnassociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50723)
)
mgcUnassociated.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgcName"),
        ("CISCO-WAN-MG-MIB", "mgcAssociationState"))
)
if mibBuilder.loadTexts:
    mgcUnassociated.setStatus(
        ""
    )

mgcAssociatedCommLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50724)
)
mgcAssociatedCommLoss.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgcName"),
        ("CISCO-WAN-MG-MIB", "mgcAssociationState"))
)
if mibBuilder.loadTexts:
    mgcAssociatedCommLoss.setStatus(
        ""
    )

mgcCommStateActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50725)
)
mgcCommStateActive.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionIpAddress"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionCommState"))
)
if mibBuilder.loadTexts:
    mgcCommStateActive.setStatus(
        ""
    )

mgcCommStateInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50726)
)
mgcCommStateInactive.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionIpAddress"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionCommState"))
)
if mibBuilder.loadTexts:
    mgcCommStateInactive.setStatus(
        ""
    )

mgEndpointCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50727)
)
mgEndpointCreated.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgEndpointLineNumber"),
        ("CISCO-WAN-MG-MIB", "mgEndpointChannelMap"))
)
if mibBuilder.loadTexts:
    mgEndpointCreated.setStatus(
        ""
    )

mgEndpointDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50728)
)
mgEndpointDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgEndpointLineNumber"),
        ("CISCO-WAN-MG-MIB", "mgEndpointChannelMap"))
)
if mibBuilder.loadTexts:
    mgEndpointDeleted.setStatus(
        ""
    )

mgEndpointActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50729)
)
mgEndpointActive.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgEndpointLineNumber"),
        ("CISCO-WAN-MG-MIB", "mgEndpointChannelMap"),
        ("CISCO-WAN-MG-MIB", "mgEndpointState"))
)
if mibBuilder.loadTexts:
    mgEndpointActive.setStatus(
        ""
    )

mgEndpointFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50730)
)
mgEndpointFailed.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgEndpointLineNumber"),
        ("CISCO-WAN-MG-MIB", "mgEndpointChannelMap"),
        ("CISCO-WAN-MG-MIB", "mgEndpointState"))
)
if mibBuilder.loadTexts:
    mgEndpointFailed.setStatus(
        ""
    )

mgcAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50731)
)
mgcAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgcName"))
)
if mibBuilder.loadTexts:
    mgcAdded.setStatus(
        ""
    )

mgcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50732)
)
mgcDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgcName"))
)
if mibBuilder.loadTexts:
    mgcDeleted.setStatus(
        ""
    )

mgcProtocolAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50733)
)
mgcProtocolAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex2"))
)
if mibBuilder.loadTexts:
    mgcProtocolAdded.setStatus(
        ""
    )

mgcProtocolDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50734)
)
mgcProtocolDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex2"))
)
if mibBuilder.loadTexts:
    mgcProtocolDeleted.setStatus(
        ""
    )

mgcResolutionAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50735)
)
mgcResolutionAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionName"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionIpAddress"))
)
if mibBuilder.loadTexts:
    mgcResolutionAdded.setStatus(
        ""
    )

mgcResolutionDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50736)
)
mgcResolutionDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionName"),
        ("CISCO-WAN-MG-MIB", "mgcResolutionIpAddress"))
)
if mibBuilder.loadTexts:
    mgcResolutionDeleted.setStatus(
        ""
    )

peerHeartbeatLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50737)
)
peerHeartbeatLost.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerTimeSinceHeartbeat"))
)
if mibBuilder.loadTexts:
    peerHeartbeatLost.setStatus(
        ""
    )

peerHeartbeatDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50738)
)
peerHeartbeatDetected.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerTimeSinceHeartbeat"))
)
if mibBuilder.loadTexts:
    peerHeartbeatDetected.setStatus(
        ""
    )

trapLapdAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50761)
)
trapLapdAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-LAPD-MIB", "vismLapdIndex"))
)
if mibBuilder.loadTexts:
    trapLapdAdded.setStatus(
        ""
    )

trapLapdDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50762)
)
trapLapdDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-LAPD-MIB", "vismLapdIndex"))
)
if mibBuilder.loadTexts:
    trapLapdDeleted.setStatus(
        ""
    )

trapSessionSetAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50763)
)
trapSessionSetAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismSessionSetNum"))
)
if mibBuilder.loadTexts:
    trapSessionSetAdded.setStatus(
        ""
    )

trapSessionSetDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50764)
)
trapSessionSetDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismSessionSetNum"))
)
if mibBuilder.loadTexts:
    trapSessionSetDeleted.setStatus(
        ""
    )

trapSessionGrpAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50765)
)
trapSessionGrpAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismSessionGrpNum"))
)
if mibBuilder.loadTexts:
    trapSessionGrpAdded.setStatus(
        ""
    )

trapSessionGrpDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50766)
)
trapSessionGrpDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismSessionGrpNum"))
)
if mibBuilder.loadTexts:
    trapSessionGrpDeleted.setStatus(
        ""
    )

trapRudpSessionAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50767)
)
trapRudpSessionAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismRudpSessionNum"))
)
if mibBuilder.loadTexts:
    trapRudpSessionAdded.setStatus(
        ""
    )

trapRudpSessionDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50768)
)
trapRudpSessionDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismRudpSessionNum"))
)
if mibBuilder.loadTexts:
    trapRudpSessionDeleted.setStatus(
        ""
    )

trapRudpSessionOos = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50769)
)
trapRudpSessionOos.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismRudpSessionNum"),
        ("VISM-SESSION-MIB", "vismRudpSessionState"))
)
if mibBuilder.loadTexts:
    trapRudpSessionOos.setStatus(
        ""
    )

trapRudpSessionIs = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50770)
)
trapRudpSessionIs.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismRudpSessionNum"),
        ("VISM-SESSION-MIB", "vismRudpSessionState"))
)
if mibBuilder.loadTexts:
    trapRudpSessionIs.setStatus(
        ""
    )

trapRudpSessionPrimaryIs = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50771)
)
trapRudpSessionPrimaryIs.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismRudpSessionNum"),
        ("VISM-SESSION-MIB", "vismRudpSessionState"))
)
if mibBuilder.loadTexts:
    trapRudpSessionPrimaryIs.setStatus(
        ""
    )

trapRudpSessionActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50772)
)
trapRudpSessionActive.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismRudpSessionNum"),
        ("VISM-SESSION-MIB", "vismRudpSessionState"))
)
if mibBuilder.loadTexts:
    trapRudpSessionActive.setStatus(
        ""
    )

trapSessionGrpOos = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50773)
)
trapSessionGrpOos.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismSessionGrpNum"),
        ("VISM-SESSION-MIB", "vismSessionGrpState"))
)
if mibBuilder.loadTexts:
    trapSessionGrpOos.setStatus(
        ""
    )

trapSessionGrpIs = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50774)
)
trapSessionGrpIs.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismSessionGrpNum"),
        ("VISM-SESSION-MIB", "vismSessionGrpState"))
)
if mibBuilder.loadTexts:
    trapSessionGrpIs.setStatus(
        ""
    )

trapSessionSetOos = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50775)
)
trapSessionSetOos.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismSessionSetNum"),
        ("VISM-SESSION-MIB", "vismSessionSetState"))
)
if mibBuilder.loadTexts:
    trapSessionSetOos.setStatus(
        ""
    )

trapSessionSetActiveIs = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50776)
)
trapSessionSetActiveIs.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismSessionSetNum"),
        ("VISM-SESSION-MIB", "vismSessionSetState"))
)
if mibBuilder.loadTexts:
    trapSessionSetActiveIs.setStatus(
        ""
    )

trapSessionSetStandbyIs = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50777)
)
trapSessionSetStandbyIs.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismSessionSetNum"),
        ("VISM-SESSION-MIB", "vismSessionSetState"))
)
if mibBuilder.loadTexts:
    trapSessionSetStandbyIs.setStatus(
        ""
    )

trapSessionSetFullIs = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50778)
)
trapSessionSetFullIs.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-SESSION-MIB", "vismSessionSetNum"),
        ("VISM-SESSION-MIB", "vismSessionSetState"))
)
if mibBuilder.loadTexts:
    trapSessionSetFullIs.setStatus(
        ""
    )

trapLapdDlcAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50779)
)
trapLapdDlcAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-LAPD-MIB", "vismLapdDlcIndex"),
        ("VISM-LAPD-MIB", "vismLapdDlcSapi"),
        ("VISM-LAPD-MIB", "vismLapdDlcTei"))
)
if mibBuilder.loadTexts:
    trapLapdDlcAdded.setStatus(
        ""
    )

trapLapdDlcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50780)
)
trapLapdDlcDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-LAPD-MIB", "vismLapdDlcIndex"),
        ("VISM-LAPD-MIB", "vismLapdDlcSapi"),
        ("VISM-LAPD-MIB", "vismLapdDlcTei"))
)
if mibBuilder.loadTexts:
    trapLapdDlcDeleted.setStatus(
        ""
    )

trapLapdDlcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50781)
)
trapLapdDlcUp.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-LAPD-MIB", "vismLapdDlcIndex"),
        ("VISM-LAPD-MIB", "vismLapdDlcSapi"),
        ("VISM-LAPD-MIB", "vismLapdDlcTei"),
        ("VISM-LAPD-MIB", "vismLapdDlcLinkState"))
)
if mibBuilder.loadTexts:
    trapLapdDlcUp.setStatus(
        ""
    )

trapLapdDlcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50782)
)
trapLapdDlcDown.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("VISM-LAPD-MIB", "vismLapdDlcIndex"),
        ("VISM-LAPD-MIB", "vismLapdDlcSapi"),
        ("VISM-LAPD-MIB", "vismLapdDlcTei"),
        ("VISM-LAPD-MIB", "vismLapdDlcLinkState"))
)
if mibBuilder.loadTexts:
    trapLapdDlcDown.setStatus(
        ""
    )

persistentXgcpEventCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50786)
)
persistentXgcpEventCreated.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventName"))
)
if mibBuilder.loadTexts:
    persistentXgcpEventCreated.setStatus(
        ""
    )

persistentXgcpEventDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50787)
)
persistentXgcpEventDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventName"))
)
if mibBuilder.loadTexts:
    persistentXgcpEventDeleted.setStatus(
        ""
    )

mgDomainNameDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50789)
)
mgDomainNameDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"))
)
if mibBuilder.loadTexts:
    mgDomainNameDeleted.setStatus(
        ""
    )

mgDomainNameAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50791)
)
mgDomainNameAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-MG-MIB", "mgDomainName"),
        ("CISCO-WAN-MG-MIB", "mgDnsResolutionType"))
)
if mibBuilder.loadTexts:
    mgDomainNameAdded.setStatus(
        ""
    )

vismTonePlanAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50798)
)
vismTonePlanAdded.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanRegionName"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanVersionNumber"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanFileName"))
)
if mibBuilder.loadTexts:
    vismTonePlanAdded.setStatus(
        ""
    )

vismTonePlanDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 351, 110, 0, 50799)
)
vismTonePlanDeleted.setObjects(
      *(("RTM-MIB", "lastSequenceNumber"),
        ("BASIS-SHELF-MIB", "shelfNodeName"),
        ("BASIS-SHELF-MIB", "shelfNum"),
        ("BASIS-GENERIC-MIB", "moduleSlotNumber"),
        ("BASIS-GENERIC-MIB", "moduleTrapAlarmSeverity"),
        ("BASIS-GENERIC-MIB", "functionModuleType"),
        ("GENERICOBJECT-MIB", "genericTimeStamp"),
        ("CISCO-WAN-AXIPOP-MIB", "vismTrapIntIndex1"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanRegionName"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanVersionNumber"),
        ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanFileName"))
)
if mibBuilder.loadTexts:
    vismTonePlanDeleted.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VISM-NONAXIPOP-TRAPS-MIB",
    **{"vismRtpConnAdded": vismRtpConnAdded,
       "vismRtpConnDeleted": vismRtpConnDeleted,
       "vismRtpConnStateChg": vismRtpConnStateChg,
       "vismLapdTrStateIs": vismLapdTrStateIs,
       "vismLapdTrStateOos": vismLapdTrStateOos,
       "vismLapdTrunkAdded": vismLapdTrunkAdded,
       "vismLapdTrunkDeleted": vismLapdTrunkDeleted,
       "mgcRedundancyGrpAdded": mgcRedundancyGrpAdded,
       "mgcRedundancyGrpDeleted": mgcRedundancyGrpDeleted,
       "mgcRedundancyGrpCommOk": mgcRedundancyGrpCommOk,
       "mgcRedundancyGrpCommLoss": mgcRedundancyGrpCommLoss,
       "mgcRedundancyGrpProtocolAdded": mgcRedundancyGrpProtocolAdded,
       "mgcRedundancyGrpProtocolDeleted": mgcRedundancyGrpProtocolDeleted,
       "peerGrpHeartbeatLost": peerGrpHeartbeatLost,
       "peerGrpHeartbeatDetected": peerGrpHeartbeatDetected,
       "mgcActiveInGrp": mgcActiveInGrp,
       "mgcInactiveInGrp": mgcInactiveInGrp,
       "mgcRedundancyGrpParamEntryAdded": mgcRedundancyGrpParamEntryAdded,
       "mgcRedundancyGrpParamEntryDeleted": mgcRedundancyGrpParamEntryDeleted,
       "srcpPeerGrpParamEntryAdded": srcpPeerGrpParamEntryAdded,
       "srcpPeerGrpParamEntryDeleted": srcpPeerGrpParamEntryDeleted,
       "newFlow": newFlow,
       "lostFlow": lostFlow,
       "cwAnnFileAddStarted": cwAnnFileAddStarted,
       "cwAnnFileLoadComplete": cwAnnFileLoadComplete,
       "cwAnnFileLoadFailed": cwAnnFileLoadFailed,
       "cwAnnFileDeleted": cwAnnFileDeleted,
       "mgAdministrativeStateLocked": mgAdministrativeStateLocked,
       "mgAdministrativeStateUnlocked": mgAdministrativeStateUnlocked,
       "mgAdministrativeStateShuttingDown": mgAdministrativeStateShuttingDown,
       "mgcAssociated": mgcAssociated,
       "mgcUnassociated": mgcUnassociated,
       "mgcAssociatedCommLoss": mgcAssociatedCommLoss,
       "mgcCommStateActive": mgcCommStateActive,
       "mgcCommStateInactive": mgcCommStateInactive,
       "mgEndpointCreated": mgEndpointCreated,
       "mgEndpointDeleted": mgEndpointDeleted,
       "mgEndpointActive": mgEndpointActive,
       "mgEndpointFailed": mgEndpointFailed,
       "mgcAdded": mgcAdded,
       "mgcDeleted": mgcDeleted,
       "mgcProtocolAdded": mgcProtocolAdded,
       "mgcProtocolDeleted": mgcProtocolDeleted,
       "mgcResolutionAdded": mgcResolutionAdded,
       "mgcResolutionDeleted": mgcResolutionDeleted,
       "peerHeartbeatLost": peerHeartbeatLost,
       "peerHeartbeatDetected": peerHeartbeatDetected,
       "trapLapdAdded": trapLapdAdded,
       "trapLapdDeleted": trapLapdDeleted,
       "trapSessionSetAdded": trapSessionSetAdded,
       "trapSessionSetDeleted": trapSessionSetDeleted,
       "trapSessionGrpAdded": trapSessionGrpAdded,
       "trapSessionGrpDeleted": trapSessionGrpDeleted,
       "trapRudpSessionAdded": trapRudpSessionAdded,
       "trapRudpSessionDeleted": trapRudpSessionDeleted,
       "trapRudpSessionOos": trapRudpSessionOos,
       "trapRudpSessionIs": trapRudpSessionIs,
       "trapRudpSessionPrimaryIs": trapRudpSessionPrimaryIs,
       "trapRudpSessionActive": trapRudpSessionActive,
       "trapSessionGrpOos": trapSessionGrpOos,
       "trapSessionGrpIs": trapSessionGrpIs,
       "trapSessionSetOos": trapSessionSetOos,
       "trapSessionSetActiveIs": trapSessionSetActiveIs,
       "trapSessionSetStandbyIs": trapSessionSetStandbyIs,
       "trapSessionSetFullIs": trapSessionSetFullIs,
       "trapLapdDlcAdded": trapLapdDlcAdded,
       "trapLapdDlcDeleted": trapLapdDlcDeleted,
       "trapLapdDlcUp": trapLapdDlcUp,
       "trapLapdDlcDown": trapLapdDlcDown,
       "persistentXgcpEventCreated": persistentXgcpEventCreated,
       "persistentXgcpEventDeleted": persistentXgcpEventDeleted,
       "mgDomainNameDeleted": mgDomainNameDeleted,
       "mgDomainNameAdded": mgDomainNameAdded,
       "vismTonePlanAdded": vismTonePlanAdded,
       "vismTonePlanDeleted": vismTonePlanDeleted}
)
