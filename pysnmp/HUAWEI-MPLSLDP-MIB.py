# SNMP MIB module (HUAWEI-MPLSLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MPLSLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:10 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(MplsLdpIdentifier,
 MplsLsrIdentifier) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLdpIdentifier",
    "MplsLsrIdentifier")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwMplsLdp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143)
)
hwMplsLdp.setRevisions(
        ("2014-11-06 16:40",
         "2014-08-22 11:26",
         "2014-05-28 11:26",
         "2014-01-15 16:00",
         "2013-07-15 16:00",
         "2013-06-14 10:00",
         "2013-01-15 10:00",
         "2013-01-07 10:00",
         "2012-07-14 10:00",
         "2011-11-16 10:00",
         "2011-09-28 10:00",
         "2011-09-07 10:00",
         "2011-05-10 10:00",
         "2010-08-11 16:00",
         "2010-07-12 16:00",
         "2009-03-10 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMplsLdpInfo_ObjectIdentity = ObjectIdentity
hwMplsLdpInfo = _HwMplsLdpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1)
)
_HwMplsLdpProcessName_Type = OctetString
_HwMplsLdpProcessName_Object = MibScalar
hwMplsLdpProcessName = _HwMplsLdpProcessName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 1),
    _HwMplsLdpProcessName_Type()
)
hwMplsLdpProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpProcessName.setStatus("current")
_HwMplsLdpLspFec_Type = InetAddress
_HwMplsLdpLspFec_Object = MibScalar
hwMplsLdpLspFec = _HwMplsLdpLspFec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 2),
    _HwMplsLdpLspFec_Type()
)
hwMplsLdpLspFec.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLdpLspFec.setStatus("current")
_HwMplsLdpLspInLabel_Type = Counter32
_HwMplsLdpLspInLabel_Object = MibScalar
hwMplsLdpLspInLabel = _HwMplsLdpLspInLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 3),
    _HwMplsLdpLspInLabel_Type()
)
hwMplsLdpLspInLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLdpLspInLabel.setStatus("current")
_HwMplsLdpLspOutLabel_Type = Counter32
_HwMplsLdpLspOutLabel_Object = MibScalar
hwMplsLdpLspOutLabel = _HwMplsLdpLspOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 4),
    _HwMplsLdpLspOutLabel_Type()
)
hwMplsLdpLspOutLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLdpLspOutLabel.setStatus("current")
_HwMplsLdpLspOutIfIndex_Type = InterfaceIndex
_HwMplsLdpLspOutIfIndex_Object = MibScalar
hwMplsLdpLspOutIfIndex = _HwMplsLdpLspOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 5),
    _HwMplsLdpLspOutIfIndex_Type()
)
hwMplsLdpLspOutIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLdpLspOutIfIndex.setStatus("current")


class _HwMplsLdpLspDownReason_Type(Integer32):
    """Custom type hwMplsLdpLspDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("canNotRecoveryFromGr", 3),
          ("downStreamLost", 7),
          ("lspmNotify", 2),
          ("otherReason", 8),
          ("recvReleaseMsg", 4),
          ("recvWithdrawMsg", 5),
          ("routeDelete", 1),
          ("upStreamLost", 6))
    )


_HwMplsLdpLspDownReason_Type.__name__ = "Integer32"
_HwMplsLdpLspDownReason_Object = MibScalar
hwMplsLdpLspDownReason = _HwMplsLdpLspDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 6),
    _HwMplsLdpLspDownReason_Type()
)
hwMplsLdpLspDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLdpLspDownReason.setStatus("current")
_HwMplsLdpSessionTable_Object = MibTable
hwMplsLdpSessionTable = _HwMplsLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 7)
)
if mibBuilder.loadTexts:
    hwMplsLdpSessionTable.setStatus("current")
_HwMplsLdpSessionEntry_Object = MibTableRow
hwMplsLdpSessionEntry = _HwMplsLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 7, 1)
)
hwMplsLdpSessionEntry.setIndexNames(
    (0, "HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionPeerLsrId"),
)
if mibBuilder.loadTexts:
    hwMplsLdpSessionEntry.setStatus("current")
_HwMplsLdpSessionPeerLsrId_Type = MplsLdpIdentifier
_HwMplsLdpSessionPeerLsrId_Object = MibTableColumn
hwMplsLdpSessionPeerLsrId = _HwMplsLdpSessionPeerLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 7, 1, 1),
    _HwMplsLdpSessionPeerLsrId_Type()
)
hwMplsLdpSessionPeerLsrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpSessionPeerLsrId.setStatus("current")
_HwMplsLdpSessionIfIndex_Type = Integer32
_HwMplsLdpSessionIfIndex_Object = MibTableColumn
hwMplsLdpSessionIfIndex = _HwMplsLdpSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 7, 1, 2),
    _HwMplsLdpSessionIfIndex_Type()
)
hwMplsLdpSessionIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLdpSessionIfIndex.setStatus("current")


class _HwMplsLdpSessionDownReason_Type(Integer32):
    """Custom type hwMplsLdpSessionDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("canntBuildSessionRelation", 22),
          ("helloHoldTimerExp", 1),
          ("ifStatusChanged", 18),
          ("modifyCapabilityAnnouncementConfig", 26),
          ("modifyGRConfig", 7),
          ("modifyGRTimer", 8),
          ("modifyKeepaliveTimer", 9),
          ("modifyLDPLsrID", 14),
          ("modifyLocalLsrID", 27),
          ("modifyMD5Config", 10),
          ("modifyMP2MP", 29),
          ("modifyMTUConfig", 12),
          ("modifyP2MP", 28),
          ("modifyTransportAddress", 13),
          ("otherReason", 20),
          ("protocolGR", 17),
          ("receiveErrorMessageFromPeer", 23),
          ("receiveSocketError", 24),
          ("recvNotification", 15),
          ("resetMplsLdp", 3),
          ("sentNotification", 21),
          ("sessionDelete", 25),
          ("sessionProtectTimerExp", 30),
          ("sessionUp", 0),
          ("ssnHoldTimerExp", 2),
          ("ssnRoleSwitch", 11),
          ("tcpDown", 19),
          ("transportAddressNotMatch", 16),
          ("undoMpls", 5),
          ("undoMplsLdp", 4),
          ("undoMplsLdpRemotePeer", 6))
    )


_HwMplsLdpSessionDownReason_Type.__name__ = "Integer32"
_HwMplsLdpSessionDownReason_Object = MibTableColumn
hwMplsLdpSessionDownReason = _HwMplsLdpSessionDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 7, 1, 3),
    _HwMplsLdpSessionDownReason_Type()
)
hwMplsLdpSessionDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsLdpSessionDownReason.setStatus("current")
_HwMplsLdpSessionAge_Type = TimeTicks
_HwMplsLdpSessionAge_Object = MibTableColumn
hwMplsLdpSessionAge = _HwMplsLdpSessionAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 7, 1, 4),
    _HwMplsLdpSessionAge_Type()
)
hwMplsLdpSessionAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionAge.setStatus("current")
_HwMplsLdpSessionStateTable_Object = MibTable
hwMplsLdpSessionStateTable = _HwMplsLdpSessionStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8)
)
if mibBuilder.loadTexts:
    hwMplsLdpSessionStateTable.setStatus("current")
_HwMplsLdpSessionStateEntry_Object = MibTableRow
hwMplsLdpSessionStateEntry = _HwMplsLdpSessionStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1)
)
hwMplsLdpSessionStateEntry.setIndexNames(
    (0, "HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionPeerId"),
)
if mibBuilder.loadTexts:
    hwMplsLdpSessionStateEntry.setStatus("current")
_HwMplsLdpSessionPeerId_Type = MplsLdpIdentifier
_HwMplsLdpSessionPeerId_Object = MibTableColumn
hwMplsLdpSessionPeerId = _HwMplsLdpSessionPeerId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 1),
    _HwMplsLdpSessionPeerId_Type()
)
hwMplsLdpSessionPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsLdpSessionPeerId.setStatus("current")
_HwMplsLdpSessionLsrId_Type = MplsLdpIdentifier
_HwMplsLdpSessionLsrId_Object = MibTableColumn
hwMplsLdpSessionLsrId = _HwMplsLdpSessionLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 2),
    _HwMplsLdpSessionLsrId_Type()
)
hwMplsLdpSessionLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionLsrId.setStatus("current")
_HwMplsLdpSessionTcpConnectionState_Type = OctetString
_HwMplsLdpSessionTcpConnectionState_Object = MibTableColumn
hwMplsLdpSessionTcpConnectionState = _HwMplsLdpSessionTcpConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 3),
    _HwMplsLdpSessionTcpConnectionState_Type()
)
hwMplsLdpSessionTcpConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionTcpConnectionState.setStatus("current")
_HwMplsLdpSessionState_Type = OctetString
_HwMplsLdpSessionState_Object = MibTableColumn
hwMplsLdpSessionState = _HwMplsLdpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 4),
    _HwMplsLdpSessionState_Type()
)
hwMplsLdpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionState.setStatus("current")
_HwMplsLdpSessionRole_Type = OctetString
_HwMplsLdpSessionRole_Object = MibTableColumn
hwMplsLdpSessionRole = _HwMplsLdpSessionRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 5),
    _HwMplsLdpSessionRole_Type()
)
hwMplsLdpSessionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionRole.setStatus("current")
_HwMplsLdpSessionFtFlag_Type = OctetString
_HwMplsLdpSessionFtFlag_Object = MibTableColumn
hwMplsLdpSessionFtFlag = _HwMplsLdpSessionFtFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 6),
    _HwMplsLdpSessionFtFlag_Type()
)
hwMplsLdpSessionFtFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionFtFlag.setStatus("current")
_HwMplsLdpSessionMd5Flag_Type = OctetString
_HwMplsLdpSessionMd5Flag_Object = MibTableColumn
hwMplsLdpSessionMd5Flag = _HwMplsLdpSessionMd5Flag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 7),
    _HwMplsLdpSessionMd5Flag_Type()
)
hwMplsLdpSessionMd5Flag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionMd5Flag.setStatus("current")
_HwMplsLdpSessionReconnectTimer_Type = Unsigned32
_HwMplsLdpSessionReconnectTimer_Object = MibTableColumn
hwMplsLdpSessionReconnectTimer = _HwMplsLdpSessionReconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 8),
    _HwMplsLdpSessionReconnectTimer_Type()
)
hwMplsLdpSessionReconnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionReconnectTimer.setStatus("current")
_HwMplsLdpSessionRecoveryTimer_Type = Unsigned32
_HwMplsLdpSessionRecoveryTimer_Object = MibTableColumn
hwMplsLdpSessionRecoveryTimer = _HwMplsLdpSessionRecoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 9),
    _HwMplsLdpSessionRecoveryTimer_Type()
)
hwMplsLdpSessionRecoveryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionRecoveryTimer.setStatus("current")
_HwMplsLdpSessionKeepAliveTimer_Type = Unsigned32
_HwMplsLdpSessionKeepAliveTimer_Object = MibTableColumn
hwMplsLdpSessionKeepAliveTimer = _HwMplsLdpSessionKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 10),
    _HwMplsLdpSessionKeepAliveTimer_Type()
)
hwMplsLdpSessionKeepAliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionKeepAliveTimer.setStatus("current")
_HwMplsLdpSessionKeepAliveMsgReceived_Type = Unsigned32
_HwMplsLdpSessionKeepAliveMsgReceived_Object = MibTableColumn
hwMplsLdpSessionKeepAliveMsgReceived = _HwMplsLdpSessionKeepAliveMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 11),
    _HwMplsLdpSessionKeepAliveMsgReceived_Type()
)
hwMplsLdpSessionKeepAliveMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionKeepAliveMsgReceived.setStatus("current")
_HwMplsLdpSessionKeepAliveMsgSent_Type = Unsigned32
_HwMplsLdpSessionKeepAliveMsgSent_Object = MibTableColumn
hwMplsLdpSessionKeepAliveMsgSent = _HwMplsLdpSessionKeepAliveMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 12),
    _HwMplsLdpSessionKeepAliveMsgSent_Type()
)
hwMplsLdpSessionKeepAliveMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionKeepAliveMsgSent.setStatus("current")
_HwMplsLdpSessionLabelAdvMode_Type = OctetString
_HwMplsLdpSessionLabelAdvMode_Object = MibTableColumn
hwMplsLdpSessionLabelAdvMode = _HwMplsLdpSessionLabelAdvMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 13),
    _HwMplsLdpSessionLabelAdvMode_Type()
)
hwMplsLdpSessionLabelAdvMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionLabelAdvMode.setStatus("current")
_HwMplsLdpSessionLocalLabelResourceStatus_Type = OctetString
_HwMplsLdpSessionLocalLabelResourceStatus_Object = MibTableColumn
hwMplsLdpSessionLocalLabelResourceStatus = _HwMplsLdpSessionLocalLabelResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 14),
    _HwMplsLdpSessionLocalLabelResourceStatus_Type()
)
hwMplsLdpSessionLocalLabelResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionLocalLabelResourceStatus.setStatus("current")
_HwMplsLdpSessionPeerLabelResourceStatus_Type = OctetString
_HwMplsLdpSessionPeerLabelResourceStatus_Object = MibTableColumn
hwMplsLdpSessionPeerLabelResourceStatus = _HwMplsLdpSessionPeerLabelResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 15),
    _HwMplsLdpSessionPeerLabelResourceStatus_Type()
)
hwMplsLdpSessionPeerLabelResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionPeerLabelResourceStatus.setStatus("current")
_HwMplsLdpSessionAgeStatus_Type = TimeTicks
_HwMplsLdpSessionAgeStatus_Object = MibTableColumn
hwMplsLdpSessionAgeStatus = _HwMplsLdpSessionAgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 8, 1, 16),
    _HwMplsLdpSessionAgeStatus_Type()
)
hwMplsLdpSessionAgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsLdpSessionAgeStatus.setStatus("current")
_HwLdpCapabilityConfig_Type = EnabledStatus
_HwLdpCapabilityConfig_Object = MibScalar
hwLdpCapabilityConfig = _HwLdpCapabilityConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 9),
    _HwLdpCapabilityConfig_Type()
)
hwLdpCapabilityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpCapabilityConfig.setStatus("current")
_HwLdpLsrId_Type = IpAddress
_HwLdpLsrId_Object = MibScalar
hwLdpLsrId = _HwLdpLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 10),
    _HwLdpLsrId_Type()
)
hwLdpLsrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpLsrId.setStatus("current")
_HwLdpPropagateIpPrefix_Type = OctetString
_HwLdpPropagateIpPrefix_Object = MibScalar
hwLdpPropagateIpPrefix = _HwLdpPropagateIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 11),
    _HwLdpPropagateIpPrefix_Type()
)
hwLdpPropagateIpPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpPropagateIpPrefix.setStatus("current")
_HwLdpGlobalRemotePwe3_Type = EnabledStatus
_HwLdpGlobalRemotePwe3_Object = MibScalar
hwLdpGlobalRemotePwe3 = _HwLdpGlobalRemotePwe3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 12),
    _HwLdpGlobalRemotePwe3_Type()
)
hwLdpGlobalRemotePwe3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpGlobalRemotePwe3.setStatus("current")
_HwLdpMtuSignaling_Type = EnabledStatus
_HwLdpMtuSignaling_Object = MibScalar
hwLdpMtuSignaling = _HwLdpMtuSignaling_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 13),
    _HwLdpMtuSignaling_Type()
)
hwLdpMtuSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpMtuSignaling.setStatus("current")
_HwLdpMtuApplyTlv_Type = EnabledStatus
_HwLdpMtuApplyTlv_Object = MibScalar
hwLdpMtuApplyTlv = _HwLdpMtuApplyTlv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 14),
    _HwLdpMtuApplyTlv_Type()
)
hwLdpMtuApplyTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpMtuApplyTlv.setStatus("current")
_HwLdpGrCapabilityConfig_Type = EnabledStatus
_HwLdpGrCapabilityConfig_Object = MibScalar
hwLdpGrCapabilityConfig = _HwLdpGrCapabilityConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 15),
    _HwLdpGrCapabilityConfig_Type()
)
hwLdpGrCapabilityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpGrCapabilityConfig.setStatus("current")
_HwLdpGrNeighborLivenessTimer_Type = Integer32
_HwLdpGrNeighborLivenessTimer_Object = MibScalar
hwLdpGrNeighborLivenessTimer = _HwLdpGrNeighborLivenessTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 16),
    _HwLdpGrNeighborLivenessTimer_Type()
)
hwLdpGrNeighborLivenessTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpGrNeighborLivenessTimer.setStatus("current")
_HwLdpGrReconnectTimer_Type = Integer32
_HwLdpGrReconnectTimer_Object = MibScalar
hwLdpGrReconnectTimer = _HwLdpGrReconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 17),
    _HwLdpGrReconnectTimer_Type()
)
hwLdpGrReconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpGrReconnectTimer.setStatus("current")
_HwLdpGrRecoveryTimer_Type = Integer32
_HwLdpGrRecoveryTimer_Object = MibScalar
hwLdpGrRecoveryTimer = _HwLdpGrRecoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 18),
    _HwLdpGrRecoveryTimer_Type()
)
hwLdpGrRecoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpGrRecoveryTimer.setStatus("current")


class _HwMplsLspTrigger_Type(Integer32):
    """Custom type hwMplsLspTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("host", 3),
          ("ipprefix", 4),
          ("none", 2))
    )


_HwMplsLspTrigger_Type.__name__ = "Integer32"
_HwMplsLspTrigger_Object = MibScalar
hwMplsLspTrigger = _HwMplsLspTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 19),
    _HwMplsLspTrigger_Type()
)
hwMplsLspTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLspTrigger.setStatus("current")
_HwMplsLspTriggerIpPrefix_Type = OctetString
_HwMplsLspTriggerIpPrefix_Object = MibScalar
hwMplsLspTriggerIpPrefix = _HwMplsLspTriggerIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 20),
    _HwMplsLspTriggerIpPrefix_Type()
)
hwMplsLspTriggerIpPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLspTriggerIpPrefix.setStatus("current")
_HwMplsLspTriggerBgpRoute_Type = EnabledStatus
_HwMplsLspTriggerBgpRoute_Object = MibScalar
hwMplsLspTriggerBgpRoute = _HwMplsLspTriggerBgpRoute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 21),
    _HwMplsLspTriggerBgpRoute_Type()
)
hwMplsLspTriggerBgpRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLspTriggerBgpRoute.setStatus("current")
_HwMplsLspTriggerBgpRouteIpPrefix_Type = OctetString
_HwMplsLspTriggerBgpRouteIpPrefix_Object = MibScalar
hwMplsLspTriggerBgpRouteIpPrefix = _HwMplsLspTriggerBgpRouteIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 22),
    _HwMplsLspTriggerBgpRouteIpPrefix_Type()
)
hwMplsLspTriggerBgpRouteIpPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsLspTriggerBgpRouteIpPrefix.setStatus("current")


class _HwLdpReset_Type(Integer32):
    """Custom type hwLdpReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 3),
          ("reset", 1),
          ("resetall", 2))
    )


_HwLdpReset_Type.__name__ = "Integer32"
_HwLdpReset_Object = MibScalar
hwLdpReset = _HwLdpReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 23),
    _HwLdpReset_Type()
)
hwLdpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpReset.setStatus("current")
_HwLdpOutBoundSplitHorizonAll_Type = EnabledStatus
_HwLdpOutBoundSplitHorizonAll_Object = MibScalar
hwLdpOutBoundSplitHorizonAll = _HwLdpOutBoundSplitHorizonAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 24),
    _HwLdpOutBoundSplitHorizonAll_Type()
)
hwLdpOutBoundSplitHorizonAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpOutBoundSplitHorizonAll.setStatus("current")


class _HwLdpDeleteGtsmAll_Type(Integer32):
    """Custom type hwLdpDeleteGtsmAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("ready", 2))
    )


_HwLdpDeleteGtsmAll_Type.__name__ = "Integer32"
_HwLdpDeleteGtsmAll_Object = MibScalar
hwLdpDeleteGtsmAll = _HwLdpDeleteGtsmAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 25),
    _HwLdpDeleteGtsmAll_Type()
)
hwLdpDeleteGtsmAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpDeleteGtsmAll.setStatus("current")


class _HwMplsFrrLspTrigger_Type(Integer32):
    """Custom type hwMplsFrrLspTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("host", 3),
          ("ipPrefix", 4),
          ("none", 2))
    )


_HwMplsFrrLspTrigger_Type.__name__ = "Integer32"
_HwMplsFrrLspTrigger_Object = MibScalar
hwMplsFrrLspTrigger = _HwMplsFrrLspTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 26),
    _HwMplsFrrLspTrigger_Type()
)
hwMplsFrrLspTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsFrrLspTrigger.setStatus("current")
_HwMplsFrrLspTriggerIpPrefix_Type = OctetString
_HwMplsFrrLspTriggerIpPrefix_Object = MibScalar
hwMplsFrrLspTriggerIpPrefix = _HwMplsFrrLspTriggerIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 27),
    _HwMplsFrrLspTriggerIpPrefix_Type()
)
hwMplsFrrLspTriggerIpPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsFrrLspTriggerIpPrefix.setStatus("current")


class _HwLdpBackOffTimerInit_Type(Integer32):
    """Custom type hwLdpBackOffTimerInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483),
    )


_HwLdpBackOffTimerInit_Type.__name__ = "Integer32"
_HwLdpBackOffTimerInit_Object = MibScalar
hwLdpBackOffTimerInit = _HwLdpBackOffTimerInit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 28),
    _HwLdpBackOffTimerInit_Type()
)
hwLdpBackOffTimerInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpBackOffTimerInit.setStatus("current")


class _HwLdpBackOffTimerMax_Type(Integer32):
    """Custom type hwLdpBackOffTimerMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483),
    )


_HwLdpBackOffTimerMax_Type.__name__ = "Integer32"
_HwLdpBackOffTimerMax_Object = MibScalar
hwLdpBackOffTimerMax = _HwLdpBackOffTimerMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 29),
    _HwLdpBackOffTimerMax_Type()
)
hwLdpBackOffTimerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpBackOffTimerMax.setStatus("current")
_HwLdpLongestMatch_Type = EnabledStatus
_HwLdpLongestMatch_Object = MibScalar
hwLdpLongestMatch = _HwLdpLongestMatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 30),
    _HwLdpLongestMatch_Type()
)
hwLdpLongestMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpLongestMatch.setStatus("current")
_HwLdpRemotePeerAutoDodRequest_Type = EnabledStatus
_HwLdpRemotePeerAutoDodRequest_Object = MibScalar
hwLdpRemotePeerAutoDodRequest = _HwLdpRemotePeerAutoDodRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 37),
    _HwLdpRemotePeerAutoDodRequest_Type()
)
hwLdpRemotePeerAutoDodRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpRemotePeerAutoDodRequest.setStatus("current")
_HwLdpCapabilityAnnouncementConfig_Type = EnabledStatus
_HwLdpCapabilityAnnouncementConfig_Object = MibScalar
hwLdpCapabilityAnnouncementConfig = _HwLdpCapabilityAnnouncementConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 38),
    _HwLdpCapabilityAnnouncementConfig_Type()
)
hwLdpCapabilityAnnouncementConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpCapabilityAnnouncementConfig.setStatus("current")
_HwLdpVpnTable_Object = MibTable
hwLdpVpnTable = _HwLdpVpnTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50)
)
if mibBuilder.loadTexts:
    hwLdpVpnTable.setStatus("current")
_HwLdpVpnEntry_Object = MibTableRow
hwLdpVpnEntry = _HwLdpVpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50, 1)
)
hwLdpVpnEntry.setIndexNames(
    (0, "HUAWEI-MPLSLDP-MIB", "hwLdpVpnInstanceId"),
)
if mibBuilder.loadTexts:
    hwLdpVpnEntry.setStatus("current")
_HwLdpVpnInstanceId_Type = Unsigned32
_HwLdpVpnInstanceId_Object = MibTableColumn
hwLdpVpnInstanceId = _HwLdpVpnInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50, 1, 1),
    _HwLdpVpnInstanceId_Type()
)
hwLdpVpnInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLdpVpnInstanceId.setStatus("current")
_HwLdpVpnLsrId_Type = IpAddress
_HwLdpVpnLsrId_Object = MibTableColumn
hwLdpVpnLsrId = _HwLdpVpnLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50, 1, 11),
    _HwLdpVpnLsrId_Type()
)
hwLdpVpnLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnLsrId.setStatus("current")


class _HwLdpVpnSplitHorizonAll_Type(EnabledStatus):
    """Custom type hwLdpVpnSplitHorizonAll based on EnabledStatus"""


_HwLdpVpnSplitHorizonAll_Object = MibTableColumn
hwLdpVpnSplitHorizonAll = _HwLdpVpnSplitHorizonAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50, 1, 12),
    _HwLdpVpnSplitHorizonAll_Type()
)
hwLdpVpnSplitHorizonAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnSplitHorizonAll.setStatus("current")


class _HwLdpVpnReset_Type(Integer32):
    """Custom type hwLdpVpnReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 2),
          ("reset", 1))
    )


_HwLdpVpnReset_Type.__name__ = "Integer32"
_HwLdpVpnReset_Object = MibTableColumn
hwLdpVpnReset = _HwLdpVpnReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50, 1, 13),
    _HwLdpVpnReset_Type()
)
hwLdpVpnReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnReset.setStatus("current")


class _HwMplsVpnFrrLspTrigger_Type(Integer32):
    """Custom type hwMplsVpnFrrLspTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("host", 3),
          ("ipPrefix", 4),
          ("none", 2))
    )


_HwMplsVpnFrrLspTrigger_Type.__name__ = "Integer32"
_HwMplsVpnFrrLspTrigger_Object = MibTableColumn
hwMplsVpnFrrLspTrigger = _HwMplsVpnFrrLspTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50, 1, 14),
    _HwMplsVpnFrrLspTrigger_Type()
)
hwMplsVpnFrrLspTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsVpnFrrLspTrigger.setStatus("current")
_HwMplsVpnFrrLspTriggerIpPrefix_Type = OctetString
_HwMplsVpnFrrLspTriggerIpPrefix_Object = MibTableColumn
hwMplsVpnFrrLspTriggerIpPrefix = _HwMplsVpnFrrLspTriggerIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50, 1, 15),
    _HwMplsVpnFrrLspTriggerIpPrefix_Type()
)
hwMplsVpnFrrLspTriggerIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsVpnFrrLspTriggerIpPrefix.setStatus("current")
_HwLdpVpnGracefulDeleteCapability_Type = EnabledStatus
_HwLdpVpnGracefulDeleteCapability_Object = MibTableColumn
hwLdpVpnGracefulDeleteCapability = _HwLdpVpnGracefulDeleteCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50, 1, 16),
    _HwLdpVpnGracefulDeleteCapability_Type()
)
hwLdpVpnGracefulDeleteCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnGracefulDeleteCapability.setStatus("current")


class _HwLdpVpnGracefulDeleteTimer_Type(Integer32):
    """Custom type hwLdpVpnGracefulDeleteTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwLdpVpnGracefulDeleteTimer_Type.__name__ = "Integer32"
_HwLdpVpnGracefulDeleteTimer_Object = MibTableColumn
hwLdpVpnGracefulDeleteTimer = _HwLdpVpnGracefulDeleteTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50, 1, 17),
    _HwLdpVpnGracefulDeleteTimer_Type()
)
hwLdpVpnGracefulDeleteTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnGracefulDeleteTimer.setStatus("current")
_HwLdpVpnRowStatus_Type = RowStatus
_HwLdpVpnRowStatus_Object = MibTableColumn
hwLdpVpnRowStatus = _HwLdpVpnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 50, 1, 51),
    _HwLdpVpnRowStatus_Type()
)
hwLdpVpnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnRowStatus.setStatus("current")
_HwLdpRemoteEntityTable_Object = MibTable
hwLdpRemoteEntityTable = _HwLdpRemoteEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51)
)
if mibBuilder.loadTexts:
    hwLdpRemoteEntityTable.setStatus("current")
_HwLdpRemoteEntityEntry_Object = MibTableRow
hwLdpRemoteEntityEntry = _HwLdpRemoteEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1)
)
hwLdpRemoteEntityEntry.setIndexNames(
    (0, "HUAWEI-MPLSLDP-MIB", "hwLdpRemoteName"),
)
if mibBuilder.loadTexts:
    hwLdpRemoteEntityEntry.setStatus("current")
_HwLdpRemoteName_Type = DisplayString
_HwLdpRemoteName_Object = MibTableColumn
hwLdpRemoteName = _HwLdpRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 1),
    _HwLdpRemoteName_Type()
)
hwLdpRemoteName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLdpRemoteName.setStatus("current")
_HwLdpRemoteIp_Type = IpAddress
_HwLdpRemoteIp_Object = MibTableColumn
hwLdpRemoteIp = _HwLdpRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 11),
    _HwLdpRemoteIp_Type()
)
hwLdpRemoteIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteIp.setStatus("current")


class _HwLdpRemotePwe3_Type(EnabledStatus):
    """Custom type hwLdpRemotePwe3 based on EnabledStatus"""


_HwLdpRemotePwe3_Object = MibTableColumn
hwLdpRemotePwe3 = _HwLdpRemotePwe3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 12),
    _HwLdpRemotePwe3_Type()
)
hwLdpRemotePwe3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemotePwe3.setStatus("current")


class _HwLdpRemoteKeepaliveTimer_Type(Integer32):
    """Custom type hwLdpRemoteKeepaliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_HwLdpRemoteKeepaliveTimer_Type.__name__ = "Integer32"
_HwLdpRemoteKeepaliveTimer_Object = MibTableColumn
hwLdpRemoteKeepaliveTimer = _HwLdpRemoteKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 13),
    _HwLdpRemoteKeepaliveTimer_Type()
)
hwLdpRemoteKeepaliveTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteKeepaliveTimer.setStatus("current")


class _HwLdpRemoteHelloTimer_Type(Integer32):
    """Custom type hwLdpRemoteHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_HwLdpRemoteHelloTimer_Type.__name__ = "Integer32"
_HwLdpRemoteHelloTimer_Object = MibTableColumn
hwLdpRemoteHelloTimer = _HwLdpRemoteHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 14),
    _HwLdpRemoteHelloTimer_Type()
)
hwLdpRemoteHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteHelloTimer.setStatus("current")


class _HwLdpRemoteKeepaliveSendTimer_Type(Integer32):
    """Custom type hwLdpRemoteKeepaliveSendTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwLdpRemoteKeepaliveSendTimer_Type.__name__ = "Integer32"
_HwLdpRemoteKeepaliveSendTimer_Object = MibTableColumn
hwLdpRemoteKeepaliveSendTimer = _HwLdpRemoteKeepaliveSendTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 15),
    _HwLdpRemoteKeepaliveSendTimer_Type()
)
hwLdpRemoteKeepaliveSendTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteKeepaliveSendTimer.setStatus("current")


class _HwLdpRemoteHelloSendTimer_Type(Integer32):
    """Custom type hwLdpRemoteHelloSendTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwLdpRemoteHelloSendTimer_Type.__name__ = "Integer32"
_HwLdpRemoteHelloSendTimer_Object = MibTableColumn
hwLdpRemoteHelloSendTimer = _HwLdpRemoteHelloSendTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 16),
    _HwLdpRemoteHelloSendTimer_Type()
)
hwLdpRemoteHelloSendTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteHelloSendTimer.setStatus("current")


class _HwLdpRemoteIgpSyncTimer_Type(Integer32):
    """Custom type hwLdpRemoteIgpSyncTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwLdpRemoteIgpSyncTimer_Type.__name__ = "Integer32"
_HwLdpRemoteIgpSyncTimer_Object = MibTableColumn
hwLdpRemoteIgpSyncTimer = _HwLdpRemoteIgpSyncTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 17),
    _HwLdpRemoteIgpSyncTimer_Type()
)
hwLdpRemoteIgpSyncTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteIgpSyncTimer.setStatus("current")


class _HwLdpRemoteIpAutoDoDRequest_Type(EnabledStatus):
    """Custom type hwLdpRemoteIpAutoDoDRequest based on EnabledStatus"""


_HwLdpRemoteIpAutoDoDRequest_Object = MibTableColumn
hwLdpRemoteIpAutoDoDRequest = _HwLdpRemoteIpAutoDoDRequest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 18),
    _HwLdpRemoteIpAutoDoDRequest_Type()
)
hwLdpRemoteIpAutoDoDRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteIpAutoDoDRequest.setStatus("current")
_HwLdpRemoteIpAutoDoDRequestBlock_Type = EnabledStatus
_HwLdpRemoteIpAutoDoDRequestBlock_Object = MibTableColumn
hwLdpRemoteIpAutoDoDRequestBlock = _HwLdpRemoteIpAutoDoDRequestBlock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 19),
    _HwLdpRemoteIpAutoDoDRequestBlock_Type()
)
hwLdpRemoteIpAutoDoDRequestBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteIpAutoDoDRequestBlock.setStatus("current")


class _HwLdpRemoteLabelAdvertisementMode_Type(Integer32):
    """Custom type hwLdpRemoteLabelAdvertisementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dod", 1),
          ("du", 2))
    )


_HwLdpRemoteLabelAdvertisementMode_Type.__name__ = "Integer32"
_HwLdpRemoteLabelAdvertisementMode_Object = MibTableColumn
hwLdpRemoteLabelAdvertisementMode = _HwLdpRemoteLabelAdvertisementMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 20),
    _HwLdpRemoteLabelAdvertisementMode_Type()
)
hwLdpRemoteLabelAdvertisementMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteLabelAdvertisementMode.setStatus("current")
_HwLdpRemoteLocalLsrIdIfIndex_Type = InterfaceIndexOrZero
_HwLdpRemoteLocalLsrIdIfIndex_Object = MibTableColumn
hwLdpRemoteLocalLsrIdIfIndex = _HwLdpRemoteLocalLsrIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 21),
    _HwLdpRemoteLocalLsrIdIfIndex_Type()
)
hwLdpRemoteLocalLsrIdIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteLocalLsrIdIfIndex.setStatus("current")
_HwLdpRemoteRowStatus_Type = RowStatus
_HwLdpRemoteRowStatus_Object = MibTableColumn
hwLdpRemoteRowStatus = _HwLdpRemoteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 51, 1, 51),
    _HwLdpRemoteRowStatus_Type()
)
hwLdpRemoteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpRemoteRowStatus.setStatus("current")
_HwLdpPeerTable_Object = MibTable
hwLdpPeerTable = _HwLdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52)
)
if mibBuilder.loadTexts:
    hwLdpPeerTable.setStatus("current")
_HwLdpPeerEntry_Object = MibTableRow
hwLdpPeerEntry = _HwLdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1)
)
hwLdpPeerEntry.setIndexNames(
    (0, "HUAWEI-MPLSLDP-MIB", "hwLdpPeerLsrId"),
)
if mibBuilder.loadTexts:
    hwLdpPeerEntry.setStatus("current")
_HwLdpPeerLsrId_Type = IpAddress
_HwLdpPeerLsrId_Object = MibTableColumn
hwLdpPeerLsrId = _HwLdpPeerLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 1),
    _HwLdpPeerLsrId_Type()
)
hwLdpPeerLsrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLdpPeerLsrId.setStatus("current")


class _HwLdpPeerMd5Type_Type(Integer32):
    """Custom type hwLdpPeerMd5Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 1),
          ("null", 3),
          ("plain", 2))
    )


_HwLdpPeerMd5Type_Type.__name__ = "Integer32"
_HwLdpPeerMd5Type_Object = MibTableColumn
hwLdpPeerMd5Type = _HwLdpPeerMd5Type_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 11),
    _HwLdpPeerMd5Type_Type()
)
hwLdpPeerMd5Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerMd5Type.setStatus("current")
_HwLdpPeerMd5Password_Type = OctetString
_HwLdpPeerMd5Password_Object = MibTableColumn
hwLdpPeerMd5Password = _HwLdpPeerMd5Password_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 12),
    _HwLdpPeerMd5Password_Type()
)
hwLdpPeerMd5Password.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerMd5Password.setStatus("current")


class _HwLdpPeerGtsmHops_Type(Integer32):
    """Custom type hwLdpPeerGtsmHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwLdpPeerGtsmHops_Type.__name__ = "Integer32"
_HwLdpPeerGtsmHops_Object = MibTableColumn
hwLdpPeerGtsmHops = _HwLdpPeerGtsmHops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 13),
    _HwLdpPeerGtsmHops_Type()
)
hwLdpPeerGtsmHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerGtsmHops.setStatus("current")


class _HwLdpPeerSplitHorizon_Type(EnabledStatus):
    """Custom type hwLdpPeerSplitHorizon based on EnabledStatus"""


_HwLdpPeerSplitHorizon_Object = MibTableColumn
hwLdpPeerSplitHorizon = _HwLdpPeerSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 14),
    _HwLdpPeerSplitHorizon_Type()
)
hwLdpPeerSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerSplitHorizon.setStatus("current")


class _HwLdpPeerReset_Type(Integer32):
    """Custom type hwLdpPeerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 2),
          ("reset", 1))
    )


_HwLdpPeerReset_Type.__name__ = "Integer32"
_HwLdpPeerReset_Object = MibTableColumn
hwLdpPeerReset = _HwLdpPeerReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 15),
    _HwLdpPeerReset_Type()
)
hwLdpPeerReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerReset.setStatus("current")
_HwLdpPeerKeychainName_Type = OctetString
_HwLdpPeerKeychainName_Object = MibTableColumn
hwLdpPeerKeychainName = _HwLdpPeerKeychainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 18),
    _HwLdpPeerKeychainName_Type()
)
hwLdpPeerKeychainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerKeychainName.setStatus("current")


class _HwLdpPeerOutBoundPolicyRange_Type(Integer32):
    """Custom type hwLdpPeerOutBoundPolicyRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("host", 4),
          ("ipprefix", 3),
          ("none", 2))
    )


_HwLdpPeerOutBoundPolicyRange_Type.__name__ = "Integer32"
_HwLdpPeerOutBoundPolicyRange_Object = MibTableColumn
hwLdpPeerOutBoundPolicyRange = _HwLdpPeerOutBoundPolicyRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 19),
    _HwLdpPeerOutBoundPolicyRange_Type()
)
hwLdpPeerOutBoundPolicyRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerOutBoundPolicyRange.setStatus("current")
_HwLdpPeerOutBoundPolicyFecIpPrefix_Type = OctetString
_HwLdpPeerOutBoundPolicyFecIpPrefix_Object = MibTableColumn
hwLdpPeerOutBoundPolicyFecIpPrefix = _HwLdpPeerOutBoundPolicyFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 20),
    _HwLdpPeerOutBoundPolicyFecIpPrefix_Type()
)
hwLdpPeerOutBoundPolicyFecIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerOutBoundPolicyFecIpPrefix.setStatus("current")


class _HwLdpPeerOutBoundPolicyBgpRange_Type(Integer32):
    """Custom type hwLdpPeerOutBoundPolicyBgpRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ipprefix", 3),
          ("none", 2))
    )


_HwLdpPeerOutBoundPolicyBgpRange_Type.__name__ = "Integer32"
_HwLdpPeerOutBoundPolicyBgpRange_Object = MibTableColumn
hwLdpPeerOutBoundPolicyBgpRange = _HwLdpPeerOutBoundPolicyBgpRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 21),
    _HwLdpPeerOutBoundPolicyBgpRange_Type()
)
hwLdpPeerOutBoundPolicyBgpRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerOutBoundPolicyBgpRange.setStatus("current")
_HwLdpPeerOutBoundPolicyBgpIpPrefix_Type = OctetString
_HwLdpPeerOutBoundPolicyBgpIpPrefix_Object = MibTableColumn
hwLdpPeerOutBoundPolicyBgpIpPrefix = _HwLdpPeerOutBoundPolicyBgpIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 22),
    _HwLdpPeerOutBoundPolicyBgpIpPrefix_Type()
)
hwLdpPeerOutBoundPolicyBgpIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerOutBoundPolicyBgpIpPrefix.setStatus("current")


class _HwLdpPeerInBoundPolicyRange_Type(Integer32):
    """Custom type hwLdpPeerInBoundPolicyRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("host", 4),
          ("ipprefix", 3),
          ("none", 2))
    )


_HwLdpPeerInBoundPolicyRange_Type.__name__ = "Integer32"
_HwLdpPeerInBoundPolicyRange_Object = MibTableColumn
hwLdpPeerInBoundPolicyRange = _HwLdpPeerInBoundPolicyRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 23),
    _HwLdpPeerInBoundPolicyRange_Type()
)
hwLdpPeerInBoundPolicyRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerInBoundPolicyRange.setStatus("current")
_HwLdpPeerInBoundPolicyFecIpPrefix_Type = OctetString
_HwLdpPeerInBoundPolicyFecIpPrefix_Object = MibTableColumn
hwLdpPeerInBoundPolicyFecIpPrefix = _HwLdpPeerInBoundPolicyFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 24),
    _HwLdpPeerInBoundPolicyFecIpPrefix_Type()
)
hwLdpPeerInBoundPolicyFecIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerInBoundPolicyFecIpPrefix.setStatus("current")
_HwLdpPeerRowStatus_Type = RowStatus
_HwLdpPeerRowStatus_Object = MibTableColumn
hwLdpPeerRowStatus = _HwLdpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 52, 1, 51),
    _HwLdpPeerRowStatus_Type()
)
hwLdpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerRowStatus.setStatus("current")
_HwLdpVpnPeerTable_Object = MibTable
hwLdpVpnPeerTable = _HwLdpVpnPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 53)
)
if mibBuilder.loadTexts:
    hwLdpVpnPeerTable.setStatus("current")
_HwLdpVpnPeerEntry_Object = MibTableRow
hwLdpVpnPeerEntry = _HwLdpVpnPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 53, 1)
)
hwLdpVpnPeerEntry.setIndexNames(
    (0, "HUAWEI-MPLSLDP-MIB", "hwLdpVpnInstanceId"),
    (0, "HUAWEI-MPLSLDP-MIB", "hwLdpVpnPeerLsrId"),
)
if mibBuilder.loadTexts:
    hwLdpVpnPeerEntry.setStatus("current")
_HwLdpVpnPeerLsrId_Type = IpAddress
_HwLdpVpnPeerLsrId_Object = MibTableColumn
hwLdpVpnPeerLsrId = _HwLdpVpnPeerLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 53, 1, 1),
    _HwLdpVpnPeerLsrId_Type()
)
hwLdpVpnPeerLsrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLdpVpnPeerLsrId.setStatus("current")


class _HwLdpVpnPeerMd5Type_Type(Integer32):
    """Custom type hwLdpVpnPeerMd5Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 1),
          ("null", 3),
          ("plain", 2))
    )


_HwLdpVpnPeerMd5Type_Type.__name__ = "Integer32"
_HwLdpVpnPeerMd5Type_Object = MibTableColumn
hwLdpVpnPeerMd5Type = _HwLdpVpnPeerMd5Type_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 53, 1, 11),
    _HwLdpVpnPeerMd5Type_Type()
)
hwLdpVpnPeerMd5Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnPeerMd5Type.setStatus("current")
_HwLdpVpnPeerMd5Password_Type = OctetString
_HwLdpVpnPeerMd5Password_Object = MibTableColumn
hwLdpVpnPeerMd5Password = _HwLdpVpnPeerMd5Password_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 53, 1, 12),
    _HwLdpVpnPeerMd5Password_Type()
)
hwLdpVpnPeerMd5Password.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnPeerMd5Password.setStatus("current")


class _HwLdpVpnPeerSplitHorizon_Type(EnabledStatus):
    """Custom type hwLdpVpnPeerSplitHorizon based on EnabledStatus"""


_HwLdpVpnPeerSplitHorizon_Object = MibTableColumn
hwLdpVpnPeerSplitHorizon = _HwLdpVpnPeerSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 53, 1, 13),
    _HwLdpVpnPeerSplitHorizon_Type()
)
hwLdpVpnPeerSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnPeerSplitHorizon.setStatus("current")


class _HwLdpVpnPeerReset_Type(Integer32):
    """Custom type hwLdpVpnPeerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 2),
          ("reset", 1))
    )


_HwLdpVpnPeerReset_Type.__name__ = "Integer32"
_HwLdpVpnPeerReset_Object = MibTableColumn
hwLdpVpnPeerReset = _HwLdpVpnPeerReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 53, 1, 14),
    _HwLdpVpnPeerReset_Type()
)
hwLdpVpnPeerReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnPeerReset.setStatus("current")
_HwLdpVpnPeerKeychainName_Type = OctetString
_HwLdpVpnPeerKeychainName_Object = MibTableColumn
hwLdpVpnPeerKeychainName = _HwLdpVpnPeerKeychainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 53, 1, 17),
    _HwLdpVpnPeerKeychainName_Type()
)
hwLdpVpnPeerKeychainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnPeerKeychainName.setStatus("current")
_HwLdpVpnPeerRowStatus_Type = RowStatus
_HwLdpVpnPeerRowStatus_Object = MibTableColumn
hwLdpVpnPeerRowStatus = _HwLdpVpnPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 53, 1, 51),
    _HwLdpVpnPeerRowStatus_Type()
)
hwLdpVpnPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpVpnPeerRowStatus.setStatus("current")
_HwLdpInterfaceTable_Object = MibTable
hwLdpInterfaceTable = _HwLdpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54)
)
if mibBuilder.loadTexts:
    hwLdpInterfaceTable.setStatus("current")
_HwLdpInterfaceEntry_Object = MibTableRow
hwLdpInterfaceEntry = _HwLdpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1)
)
hwLdpInterfaceEntry.setIndexNames(
    (0, "HUAWEI-MPLSLDP-MIB", "hwLdpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwLdpInterfaceEntry.setStatus("current")
_HwLdpInterfaceIndex_Type = InterfaceIndex
_HwLdpInterfaceIndex_Object = MibTableColumn
hwLdpInterfaceIndex = _HwLdpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 1),
    _HwLdpInterfaceIndex_Type()
)
hwLdpInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLdpInterfaceIndex.setStatus("current")


class _HwLdpStaticFrrProtectTimer_Type(Integer32):
    """Custom type hwLdpStaticFrrProtectTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_HwLdpStaticFrrProtectTimer_Type.__name__ = "Integer32"
_HwLdpStaticFrrProtectTimer_Object = MibTableColumn
hwLdpStaticFrrProtectTimer = _HwLdpStaticFrrProtectTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 11),
    _HwLdpStaticFrrProtectTimer_Type()
)
hwLdpStaticFrrProtectTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpStaticFrrProtectTimer.setStatus("obsolete")


class _HwLdpKeepAliveTimer_Type(Integer32):
    """Custom type hwLdpKeepAliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_HwLdpKeepAliveTimer_Type.__name__ = "Integer32"
_HwLdpKeepAliveTimer_Object = MibTableColumn
hwLdpKeepAliveTimer = _HwLdpKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 12),
    _HwLdpKeepAliveTimer_Type()
)
hwLdpKeepAliveTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpKeepAliveTimer.setStatus("current")


class _HwLdpIgpSyncTimer_Type(Integer32):
    """Custom type hwLdpIgpSyncTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwLdpIgpSyncTimer_Type.__name__ = "Integer32"
_HwLdpIgpSyncTimer_Object = MibTableColumn
hwLdpIgpSyncTimer = _HwLdpIgpSyncTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 13),
    _HwLdpIgpSyncTimer_Type()
)
hwLdpIgpSyncTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpIgpSyncTimer.setStatus("current")


class _HwLdpHelloTimer_Type(Integer32):
    """Custom type hwLdpHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_HwLdpHelloTimer_Type.__name__ = "Integer32"
_HwLdpHelloTimer_Object = MibTableColumn
hwLdpHelloTimer = _HwLdpHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 14),
    _HwLdpHelloTimer_Type()
)
hwLdpHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpHelloTimer.setStatus("current")
_HwLdpTransportAddressIfIndex_Type = InterfaceIndexOrZero
_HwLdpTransportAddressIfIndex_Object = MibTableColumn
hwLdpTransportAddressIfIndex = _HwLdpTransportAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 15),
    _HwLdpTransportAddressIfIndex_Type()
)
hwLdpTransportAddressIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpTransportAddressIfIndex.setStatus("current")


class _HwLdpKeepAliveSendTimer_Type(Integer32):
    """Custom type hwLdpKeepAliveSendTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwLdpKeepAliveSendTimer_Type.__name__ = "Integer32"
_HwLdpKeepAliveSendTimer_Object = MibTableColumn
hwLdpKeepAliveSendTimer = _HwLdpKeepAliveSendTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 16),
    _HwLdpKeepAliveSendTimer_Type()
)
hwLdpKeepAliveSendTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpKeepAliveSendTimer.setStatus("current")


class _HwLdpHelloSendTimer_Type(Integer32):
    """Custom type hwLdpHelloSendTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwLdpHelloSendTimer_Type.__name__ = "Integer32"
_HwLdpHelloSendTimer_Object = MibTableColumn
hwLdpHelloSendTimer = _HwLdpHelloSendTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 17),
    _HwLdpHelloSendTimer_Type()
)
hwLdpHelloSendTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpHelloSendTimer.setStatus("current")


class _HwLdpInterfaceLabelAdvertisementMode_Type(Integer32):
    """Custom type hwLdpInterfaceLabelAdvertisementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dod", 1),
          ("du", 2))
    )


_HwLdpInterfaceLabelAdvertisementMode_Type.__name__ = "Integer32"
_HwLdpInterfaceLabelAdvertisementMode_Object = MibTableColumn
hwLdpInterfaceLabelAdvertisementMode = _HwLdpInterfaceLabelAdvertisementMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 18),
    _HwLdpInterfaceLabelAdvertisementMode_Type()
)
hwLdpInterfaceLabelAdvertisementMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpInterfaceLabelAdvertisementMode.setStatus("current")
_HwLdpInterfaceLocalLsrIdIfIndex_Type = InterfaceIndexOrZero
_HwLdpInterfaceLocalLsrIdIfIndex_Object = MibTableColumn
hwLdpInterfaceLocalLsrIdIfIndex = _HwLdpInterfaceLocalLsrIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 19),
    _HwLdpInterfaceLocalLsrIdIfIndex_Type()
)
hwLdpInterfaceLocalLsrIdIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpInterfaceLocalLsrIdIfIndex.setStatus("current")
_HwLdpInterfaceRowStatus_Type = RowStatus
_HwLdpInterfaceRowStatus_Object = MibTableColumn
hwLdpInterfaceRowStatus = _HwLdpInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 54, 1, 51),
    _HwLdpInterfaceRowStatus_Type()
)
hwLdpInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpInterfaceRowStatus.setStatus("current")
_HwLdpPeerGroupTable_Object = MibTable
hwLdpPeerGroupTable = _HwLdpPeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 58)
)
if mibBuilder.loadTexts:
    hwLdpPeerGroupTable.setStatus("current")
_HwLdpPeerGroupEntry_Object = MibTableRow
hwLdpPeerGroupEntry = _HwLdpPeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 58, 1)
)
hwLdpPeerGroupEntry.setIndexNames(
    (0, "HUAWEI-MPLSLDP-MIB", "hwLdpPeerGroupName"),
)
if mibBuilder.loadTexts:
    hwLdpPeerGroupEntry.setStatus("current")


class _HwLdpPeerGroupName_Type(OctetString):
    """Custom type hwLdpPeerGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 110),
    )


_HwLdpPeerGroupName_Type.__name__ = "OctetString"
_HwLdpPeerGroupName_Object = MibTableColumn
hwLdpPeerGroupName = _HwLdpPeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 58, 1, 1),
    _HwLdpPeerGroupName_Type()
)
hwLdpPeerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLdpPeerGroupName.setStatus("current")


class _HwLdpPeerGroupOutBoundRange_Type(Integer32):
    """Custom type hwLdpPeerGroupOutBoundRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("host", 4),
          ("ipprefix", 3),
          ("none", 2))
    )


_HwLdpPeerGroupOutBoundRange_Type.__name__ = "Integer32"
_HwLdpPeerGroupOutBoundRange_Object = MibTableColumn
hwLdpPeerGroupOutBoundRange = _HwLdpPeerGroupOutBoundRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 58, 1, 11),
    _HwLdpPeerGroupOutBoundRange_Type()
)
hwLdpPeerGroupOutBoundRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerGroupOutBoundRange.setStatus("current")
_HwLdpPeerGroupOutBoundFecIpPrefix_Type = OctetString
_HwLdpPeerGroupOutBoundFecIpPrefix_Object = MibTableColumn
hwLdpPeerGroupOutBoundFecIpPrefix = _HwLdpPeerGroupOutBoundFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 58, 1, 12),
    _HwLdpPeerGroupOutBoundFecIpPrefix_Type()
)
hwLdpPeerGroupOutBoundFecIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerGroupOutBoundFecIpPrefix.setStatus("current")


class _HwLdpPeerGroupOutBoundBgpRange_Type(Integer32):
    """Custom type hwLdpPeerGroupOutBoundBgpRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ipprefix", 3),
          ("none", 2))
    )


_HwLdpPeerGroupOutBoundBgpRange_Type.__name__ = "Integer32"
_HwLdpPeerGroupOutBoundBgpRange_Object = MibTableColumn
hwLdpPeerGroupOutBoundBgpRange = _HwLdpPeerGroupOutBoundBgpRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 58, 1, 13),
    _HwLdpPeerGroupOutBoundBgpRange_Type()
)
hwLdpPeerGroupOutBoundBgpRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerGroupOutBoundBgpRange.setStatus("current")
_HwLdpPeerGroupOutBoundBgpIpPrefix_Type = OctetString
_HwLdpPeerGroupOutBoundBgpIpPrefix_Object = MibTableColumn
hwLdpPeerGroupOutBoundBgpIpPrefix = _HwLdpPeerGroupOutBoundBgpIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 58, 1, 14),
    _HwLdpPeerGroupOutBoundBgpIpPrefix_Type()
)
hwLdpPeerGroupOutBoundBgpIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerGroupOutBoundBgpIpPrefix.setStatus("current")


class _HwLdpPeerGroupInBoundRange_Type(Integer32):
    """Custom type hwLdpPeerGroupInBoundRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("host", 4),
          ("ipprefix", 3),
          ("none", 2))
    )


_HwLdpPeerGroupInBoundRange_Type.__name__ = "Integer32"
_HwLdpPeerGroupInBoundRange_Object = MibTableColumn
hwLdpPeerGroupInBoundRange = _HwLdpPeerGroupInBoundRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 58, 1, 15),
    _HwLdpPeerGroupInBoundRange_Type()
)
hwLdpPeerGroupInBoundRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerGroupInBoundRange.setStatus("current")
_HwLdpPeerGroupInBoundIpPrefix_Type = OctetString
_HwLdpPeerGroupInBoundIpPrefix_Object = MibTableColumn
hwLdpPeerGroupInBoundIpPrefix = _HwLdpPeerGroupInBoundIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 58, 1, 16),
    _HwLdpPeerGroupInBoundIpPrefix_Type()
)
hwLdpPeerGroupInBoundIpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerGroupInBoundIpPrefix.setStatus("current")
_HwLdpPeerGroupRowStatus_Type = RowStatus
_HwLdpPeerGroupRowStatus_Object = MibTableColumn
hwLdpPeerGroupRowStatus = _HwLdpPeerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 58, 1, 51),
    _HwLdpPeerGroupRowStatus_Type()
)
hwLdpPeerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLdpPeerGroupRowStatus.setStatus("current")


class _HwLdpOutBoundPolicyPeerAllRange_Type(Integer32):
    """Custom type hwLdpOutBoundPolicyPeerAllRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("host", 4),
          ("ipprefix", 3),
          ("none", 2))
    )


_HwLdpOutBoundPolicyPeerAllRange_Type.__name__ = "Integer32"
_HwLdpOutBoundPolicyPeerAllRange_Object = MibScalar
hwLdpOutBoundPolicyPeerAllRange = _HwLdpOutBoundPolicyPeerAllRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 59),
    _HwLdpOutBoundPolicyPeerAllRange_Type()
)
hwLdpOutBoundPolicyPeerAllRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpOutBoundPolicyPeerAllRange.setStatus("current")
_HwLdpOutBoundPolicyPeerAllFecIpPrefix_Type = OctetString
_HwLdpOutBoundPolicyPeerAllFecIpPrefix_Object = MibScalar
hwLdpOutBoundPolicyPeerAllFecIpPrefix = _HwLdpOutBoundPolicyPeerAllFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 60),
    _HwLdpOutBoundPolicyPeerAllFecIpPrefix_Type()
)
hwLdpOutBoundPolicyPeerAllFecIpPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpOutBoundPolicyPeerAllFecIpPrefix.setStatus("current")


class _HwLdpOutBoundPolicyPeerAllBgpRange_Type(Integer32):
    """Custom type hwLdpOutBoundPolicyPeerAllBgpRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("ipprefix", 3),
          ("none", 2))
    )


_HwLdpOutBoundPolicyPeerAllBgpRange_Type.__name__ = "Integer32"
_HwLdpOutBoundPolicyPeerAllBgpRange_Object = MibScalar
hwLdpOutBoundPolicyPeerAllBgpRange = _HwLdpOutBoundPolicyPeerAllBgpRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 61),
    _HwLdpOutBoundPolicyPeerAllBgpRange_Type()
)
hwLdpOutBoundPolicyPeerAllBgpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpOutBoundPolicyPeerAllBgpRange.setStatus("current")
_HwLdpOutBoundPolicyPeerAllBgpIpPrefix_Type = OctetString
_HwLdpOutBoundPolicyPeerAllBgpIpPrefix_Object = MibScalar
hwLdpOutBoundPolicyPeerAllBgpIpPrefix = _HwLdpOutBoundPolicyPeerAllBgpIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 62),
    _HwLdpOutBoundPolicyPeerAllBgpIpPrefix_Type()
)
hwLdpOutBoundPolicyPeerAllBgpIpPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpOutBoundPolicyPeerAllBgpIpPrefix.setStatus("current")


class _HwLdpInBoundPolicyPeerAllRange_Type(Integer32):
    """Custom type hwLdpInBoundPolicyPeerAllRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("host", 4),
          ("ipprefix", 3),
          ("none", 2))
    )


_HwLdpInBoundPolicyPeerAllRange_Type.__name__ = "Integer32"
_HwLdpInBoundPolicyPeerAllRange_Object = MibScalar
hwLdpInBoundPolicyPeerAllRange = _HwLdpInBoundPolicyPeerAllRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 63),
    _HwLdpInBoundPolicyPeerAllRange_Type()
)
hwLdpInBoundPolicyPeerAllRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpInBoundPolicyPeerAllRange.setStatus("current")
_HwLdpInBoundPolicyPeerAllIpPrefix_Type = OctetString
_HwLdpInBoundPolicyPeerAllIpPrefix_Object = MibScalar
hwLdpInBoundPolicyPeerAllIpPrefix = _HwLdpInBoundPolicyPeerAllIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 64),
    _HwLdpInBoundPolicyPeerAllIpPrefix_Type()
)
hwLdpInBoundPolicyPeerAllIpPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpInBoundPolicyPeerAllIpPrefix.setStatus("current")
_HwLdpGracefulDeleteCapability_Type = EnabledStatus
_HwLdpGracefulDeleteCapability_Object = MibScalar
hwLdpGracefulDeleteCapability = _HwLdpGracefulDeleteCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 65),
    _HwLdpGracefulDeleteCapability_Type()
)
hwLdpGracefulDeleteCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpGracefulDeleteCapability.setStatus("current")


class _HwLdpGracefulDeleteTimer_Type(Integer32):
    """Custom type hwLdpGracefulDeleteTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwLdpGracefulDeleteTimer_Type.__name__ = "Integer32"
_HwLdpGracefulDeleteTimer_Object = MibScalar
hwLdpGracefulDeleteTimer = _HwLdpGracefulDeleteTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 66),
    _HwLdpGracefulDeleteTimer_Type()
)
hwLdpGracefulDeleteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLdpGracefulDeleteTimer.setStatus("current")


class _HwLdpLspDownReason_Type(Integer32):
    """Custom type hwLdpLspDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("canNotRecoveryFromGr", 4),
          ("other", 1),
          ("policyChange", 5),
          ("routeChange", 3),
          ("sessionDown", 2))
    )


_HwLdpLspDownReason_Type.__name__ = "Integer32"
_HwLdpLspDownReason_Object = MibScalar
hwLdpLspDownReason = _HwLdpLspDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 67),
    _HwLdpLspDownReason_Type()
)
hwLdpLspDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdpLspDownReason.setStatus("current")
_HwLdpLspDownMplsLsrId_Type = MplsLsrIdentifier
_HwLdpLspDownMplsLsrId_Object = MibScalar
hwLdpLspDownMplsLsrId = _HwLdpLspDownMplsLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 68),
    _HwLdpLspDownMplsLsrId_Type()
)
hwLdpLspDownMplsLsrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdpLspDownMplsLsrId.setStatus("current")
_HwLdpLspDownOutIfIndex_Type = InterfaceIndex
_HwLdpLspDownOutIfIndex_Object = MibScalar
hwLdpLspDownOutIfIndex = _HwLdpLspDownOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 69),
    _HwLdpLspDownOutIfIndex_Type()
)
hwLdpLspDownOutIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdpLspDownOutIfIndex.setStatus("current")
_HwLdpLspDownOutIfMainIp_Type = IpAddress
_HwLdpLspDownOutIfMainIp_Object = MibScalar
hwLdpLspDownOutIfMainIp = _HwLdpLspDownOutIfMainIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 70),
    _HwLdpLspDownOutIfMainIp_Type()
)
hwLdpLspDownOutIfMainIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdpLspDownOutIfMainIp.setStatus("current")


class _HwLdpLspDownOutIfState_Type(Integer32):
    """Custom type hwLdpLspDownOutIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwLdpLspDownOutIfState_Type.__name__ = "Integer32"
_HwLdpLspDownOutIfState_Object = MibScalar
hwLdpLspDownOutIfState = _HwLdpLspDownOutIfState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 71),
    _HwLdpLspDownOutIfState_Type()
)
hwLdpLspDownOutIfState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdpLspDownOutIfState.setStatus("current")
_HwLdpLspDownDownstreamPeerLsrId_Type = MplsLdpIdentifier
_HwLdpLspDownDownstreamPeerLsrId_Object = MibScalar
hwLdpLspDownDownstreamPeerLsrId = _HwLdpLspDownDownstreamPeerLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 72),
    _HwLdpLspDownDownstreamPeerLsrId_Type()
)
hwLdpLspDownDownstreamPeerLsrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLdpLspDownDownstreamPeerLsrId.setStatus("current")
_HwLdpSessionStatistics_ObjectIdentity = ObjectIdentity
hwLdpSessionStatistics = _HwLdpSessionStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 73)
)
_HwLdpLocalOperationalSessionNumber_Type = Integer32
_HwLdpLocalOperationalSessionNumber_Object = MibScalar
hwLdpLocalOperationalSessionNumber = _HwLdpLocalOperationalSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 73, 1),
    _HwLdpLocalOperationalSessionNumber_Type()
)
hwLdpLocalOperationalSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLdpLocalOperationalSessionNumber.setStatus("current")
_HwLdpRemoteOperationalSessionNumber_Type = Integer32
_HwLdpRemoteOperationalSessionNumber_Object = MibScalar
hwLdpRemoteOperationalSessionNumber = _HwLdpRemoteOperationalSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 73, 2),
    _HwLdpRemoteOperationalSessionNumber_Type()
)
hwLdpRemoteOperationalSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLdpRemoteOperationalSessionNumber.setStatus("current")
_HwLdpLocalAndRemoteOperationalSessionNumber_Type = Integer32
_HwLdpLocalAndRemoteOperationalSessionNumber_Object = MibScalar
hwLdpLocalAndRemoteOperationalSessionNumber = _HwLdpLocalAndRemoteOperationalSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 73, 3),
    _HwLdpLocalAndRemoteOperationalSessionNumber_Type()
)
hwLdpLocalAndRemoteOperationalSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLdpLocalAndRemoteOperationalSessionNumber.setStatus("current")
_HwLdpTotalOperationalSessionNumber_Type = Integer32
_HwLdpTotalOperationalSessionNumber_Object = MibScalar
hwLdpTotalOperationalSessionNumber = _HwLdpTotalOperationalSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 1, 73, 4),
    _HwLdpTotalOperationalSessionNumber_Type()
)
hwLdpTotalOperationalSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLdpTotalOperationalSessionNumber.setStatus("current")
_HwMplsLdpTrap_ObjectIdentity = ObjectIdentity
hwMplsLdpTrap = _HwMplsLdpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 2)
)
_HwMplsLdpConformance_ObjectIdentity = ObjectIdentity
hwMplsLdpConformance = _HwMplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3)
)
_HwMplsLdpGroup_ObjectIdentity = ObjectIdentity
hwMplsLdpGroup = _HwMplsLdpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2)
)

# Managed Objects groups

hwMplsLdpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 1)
)
hwMplsLdpInfoGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspDownReason"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspFec"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspInLabel"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspOutLabel"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionAge"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionIfIndex"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionAgeStatus"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionPeerLabelResourceStatus"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionLocalLabelResourceStatus"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionLabelAdvMode"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionKeepAliveMsgSent"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionKeepAliveMsgReceived"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionKeepAliveTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionRecoveryTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionReconnectTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionMd5Flag"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionFtFlag"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionRole"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionState"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionTcpConnectionState"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionLsrId"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemotePeerAutoDodRequest"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpCapabilityAnnouncementConfig"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionDownReason"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpProcessName"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspOutIfIndex"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpOutBoundPolicyPeerAllRange"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpOutBoundPolicyPeerAllFecIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpOutBoundPolicyPeerAllBgpRange"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpOutBoundPolicyPeerAllBgpIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpInBoundPolicyPeerAllRange"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpInBoundPolicyPeerAllIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpGracefulDeleteCapability"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpGracefulDeleteTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownReason"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownMplsLsrId"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownOutIfIndex"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownOutIfMainIp"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownOutIfState"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownDownstreamPeerLsrId"))
)
if mibBuilder.loadTexts:
    hwMplsLdpInfoGroup.setStatus("current")

hwMplsLdpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 4)
)
hwMplsLdpGlobalGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwLdpCapabilityConfig"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLsrId"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPropagateIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpGlobalRemotePwe3"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpMtuSignaling"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpMtuApplyTlv"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpGrCapabilityConfig"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpGrNeighborLivenessTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpGrReconnectTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpGrRecoveryTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLspTrigger"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLspTriggerIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLspTriggerBgpRoute"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLspTriggerBgpRouteIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpReset"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpOutBoundSplitHorizonAll"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpDeleteGtsmAll"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsFrrLspTrigger"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsFrrLspTriggerIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpBackOffTimerInit"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpBackOffTimerMax"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLongestMatch"))
)
if mibBuilder.loadTexts:
    hwMplsLdpGlobalGroup.setStatus("current")

hwMplsLdpVpnGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 5)
)
hwMplsLdpVpnGlobalGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwLdpVpnLsrId"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpVpnSplitHorizonAll"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpVpnReset"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsVpnFrrLspTrigger"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsVpnFrrLspTriggerIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpVpnGracefulDeleteCapability"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpVpnGracefulDeleteTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpVpnRowStatus"))
)
if mibBuilder.loadTexts:
    hwMplsLdpVpnGlobalGroup.setStatus("current")

hwMplsLdpRemoteEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 6)
)
hwMplsLdpRemoteEntityGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteIp"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemotePwe3"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteKeepaliveTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteHelloTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteKeepaliveSendTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteHelloSendTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteIgpSyncTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteIpAutoDoDRequest"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteIpAutoDoDRequestBlock"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteLabelAdvertisementMode"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteLocalLsrIdIfIndex"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteRowStatus"))
)
if mibBuilder.loadTexts:
    hwMplsLdpRemoteEntityGroup.setStatus("current")

hwMplsLdpPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 7)
)
hwMplsLdpPeerGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwLdpPeerMd5Type"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerMd5Password"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerGtsmHops"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerSplitHorizon"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerReset"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerKeychainName"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerOutBoundPolicyRange"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerOutBoundPolicyFecIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerOutBoundPolicyBgpRange"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerOutBoundPolicyBgpIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerInBoundPolicyRange"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerInBoundPolicyFecIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerRowStatus"))
)
if mibBuilder.loadTexts:
    hwMplsLdpPeerGroup.setStatus("current")

hwMplsLdpVpnPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 8)
)
hwMplsLdpVpnPeerGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwLdpVpnPeerMd5Type"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpVpnPeerMd5Password"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpVpnPeerSplitHorizon"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpVpnPeerReset"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpVpnPeerKeychainName"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpVpnPeerRowStatus"))
)
if mibBuilder.loadTexts:
    hwMplsLdpVpnPeerGroup.setStatus("current")

hwMplsLdpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 9)
)
hwMplsLdpInterfaceGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwLdpKeepAliveTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpIgpSyncTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpHelloTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpTransportAddressIfIndex"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpKeepAliveSendTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpHelloSendTimer"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpInterfaceLabelAdvertisementMode"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpInterfaceLocalLsrIdIfIndex"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpInterfaceRowStatus"))
)
if mibBuilder.loadTexts:
    hwMplsLdpInterfaceGroup.setStatus("current")

hwLdpLspDownReasonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 10)
)
hwLdpLspDownReasonGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownReason"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownMplsLsrId"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownOutIfIndex"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownOutIfMainIp"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownOutIfState"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownDownstreamPeerLsrId"))
)
if mibBuilder.loadTexts:
    hwLdpLspDownReasonGroup.setStatus("current")

hwLdpPolicyPeerGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 15)
)
hwLdpPolicyPeerGroupGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwLdpPeerGroupOutBoundRange"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerGroupOutBoundFecIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerGroupOutBoundBgpRange"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerGroupOutBoundBgpIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerGroupInBoundRange"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerGroupInBoundIpPrefix"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpPeerGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwLdpPolicyPeerGroupGroup.setStatus("current")

hwMplsLdpFrrProtectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 16)
)
hwMplsLdpFrrProtectGroup.setObjects(
    ("HUAWEI-MPLSLDP-MIB", "hwLdpStaticFrrProtectTimer")
)
if mibBuilder.loadTexts:
    hwMplsLdpFrrProtectGroup.setStatus("obsolete")

hwMplsLdpSessionStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 17)
)
hwMplsLdpSessionStatisticsGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwLdpLocalOperationalSessionNumber"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpRemoteOperationalSessionNumber"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLocalAndRemoteOperationalSessionNumber"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpTotalOperationalSessionNumber"))
)
if mibBuilder.loadTexts:
    hwMplsLdpSessionStatisticsGroup.setStatus("current")


# Notification objects

hwMplsLdpSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 2, 1)
)
hwMplsLdpSessionDown.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionDownReason"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionIfIndex"))
)
if mibBuilder.loadTexts:
    hwMplsLdpSessionDown.setStatus(
        "obsolete"
    )

hwMplsLdpLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 2, 2)
)
hwMplsLdpLspDown.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspFec"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspInLabel"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspOutLabel"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspOutIfIndex"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspDownReason"))
)
if mibBuilder.loadTexts:
    hwMplsLdpLspDown.setStatus(
        "obsolete"
    )

hwMplsLdpHostIngressLspDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 2, 3)
)
hwMplsLdpHostIngressLspDownClear.setObjects(
    ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspFec")
)
if mibBuilder.loadTexts:
    hwMplsLdpHostIngressLspDownClear.setStatus(
        "current"
    )

hwMplsLdpHostIngressLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 2, 4)
)
hwMplsLdpHostIngressLspDown.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspFec"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownReason"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownMplsLsrId"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownOutIfIndex"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownOutIfMainIp"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownOutIfState"),
        ("HUAWEI-MPLSLDP-MIB", "hwLdpLspDownDownstreamPeerLsrId"))
)
if mibBuilder.loadTexts:
    hwMplsLdpHostIngressLspDown.setStatus(
        "current"
    )


# Notifications groups

hwMplsLdpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 2)
)
hwMplsLdpNotificationGroup.setObjects(
    ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpSessionDown")
)
if mibBuilder.loadTexts:
    hwMplsLdpNotificationGroup.setStatus(
        "obsolete"
    )

hwMplsLdpLspDownNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 3)
)
hwMplsLdpLspDownNotificationGroup.setObjects(
    ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpLspDown")
)
if mibBuilder.loadTexts:
    hwMplsLdpLspDownNotificationGroup.setStatus(
        "obsolete"
    )

hwMplsLdpHostIngressLspDownNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 2, 11)
)
hwMplsLdpHostIngressLspDownNotificationGroup.setObjects(
      *(("HUAWEI-MPLSLDP-MIB", "hwMplsLdpHostIngressLspDownClear"),
        ("HUAWEI-MPLSLDP-MIB", "hwMplsLdpHostIngressLspDown"))
)
if mibBuilder.loadTexts:
    hwMplsLdpHostIngressLspDownNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMplsLdpCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 143, 3, 1)
)
if mibBuilder.loadTexts:
    hwMplsLdpCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MPLSLDP-MIB",
    **{"hwMplsLdp": hwMplsLdp,
       "hwMplsLdpInfo": hwMplsLdpInfo,
       "hwMplsLdpProcessName": hwMplsLdpProcessName,
       "hwMplsLdpLspFec": hwMplsLdpLspFec,
       "hwMplsLdpLspInLabel": hwMplsLdpLspInLabel,
       "hwMplsLdpLspOutLabel": hwMplsLdpLspOutLabel,
       "hwMplsLdpLspOutIfIndex": hwMplsLdpLspOutIfIndex,
       "hwMplsLdpLspDownReason": hwMplsLdpLspDownReason,
       "hwMplsLdpSessionTable": hwMplsLdpSessionTable,
       "hwMplsLdpSessionEntry": hwMplsLdpSessionEntry,
       "hwMplsLdpSessionPeerLsrId": hwMplsLdpSessionPeerLsrId,
       "hwMplsLdpSessionIfIndex": hwMplsLdpSessionIfIndex,
       "hwMplsLdpSessionDownReason": hwMplsLdpSessionDownReason,
       "hwMplsLdpSessionAge": hwMplsLdpSessionAge,
       "hwMplsLdpSessionStateTable": hwMplsLdpSessionStateTable,
       "hwMplsLdpSessionStateEntry": hwMplsLdpSessionStateEntry,
       "hwMplsLdpSessionPeerId": hwMplsLdpSessionPeerId,
       "hwMplsLdpSessionLsrId": hwMplsLdpSessionLsrId,
       "hwMplsLdpSessionTcpConnectionState": hwMplsLdpSessionTcpConnectionState,
       "hwMplsLdpSessionState": hwMplsLdpSessionState,
       "hwMplsLdpSessionRole": hwMplsLdpSessionRole,
       "hwMplsLdpSessionFtFlag": hwMplsLdpSessionFtFlag,
       "hwMplsLdpSessionMd5Flag": hwMplsLdpSessionMd5Flag,
       "hwMplsLdpSessionReconnectTimer": hwMplsLdpSessionReconnectTimer,
       "hwMplsLdpSessionRecoveryTimer": hwMplsLdpSessionRecoveryTimer,
       "hwMplsLdpSessionKeepAliveTimer": hwMplsLdpSessionKeepAliveTimer,
       "hwMplsLdpSessionKeepAliveMsgReceived": hwMplsLdpSessionKeepAliveMsgReceived,
       "hwMplsLdpSessionKeepAliveMsgSent": hwMplsLdpSessionKeepAliveMsgSent,
       "hwMplsLdpSessionLabelAdvMode": hwMplsLdpSessionLabelAdvMode,
       "hwMplsLdpSessionLocalLabelResourceStatus": hwMplsLdpSessionLocalLabelResourceStatus,
       "hwMplsLdpSessionPeerLabelResourceStatus": hwMplsLdpSessionPeerLabelResourceStatus,
       "hwMplsLdpSessionAgeStatus": hwMplsLdpSessionAgeStatus,
       "hwLdpCapabilityConfig": hwLdpCapabilityConfig,
       "hwLdpLsrId": hwLdpLsrId,
       "hwLdpPropagateIpPrefix": hwLdpPropagateIpPrefix,
       "hwLdpGlobalRemotePwe3": hwLdpGlobalRemotePwe3,
       "hwLdpMtuSignaling": hwLdpMtuSignaling,
       "hwLdpMtuApplyTlv": hwLdpMtuApplyTlv,
       "hwLdpGrCapabilityConfig": hwLdpGrCapabilityConfig,
       "hwLdpGrNeighborLivenessTimer": hwLdpGrNeighborLivenessTimer,
       "hwLdpGrReconnectTimer": hwLdpGrReconnectTimer,
       "hwLdpGrRecoveryTimer": hwLdpGrRecoveryTimer,
       "hwMplsLspTrigger": hwMplsLspTrigger,
       "hwMplsLspTriggerIpPrefix": hwMplsLspTriggerIpPrefix,
       "hwMplsLspTriggerBgpRoute": hwMplsLspTriggerBgpRoute,
       "hwMplsLspTriggerBgpRouteIpPrefix": hwMplsLspTriggerBgpRouteIpPrefix,
       "hwLdpReset": hwLdpReset,
       "hwLdpOutBoundSplitHorizonAll": hwLdpOutBoundSplitHorizonAll,
       "hwLdpDeleteGtsmAll": hwLdpDeleteGtsmAll,
       "hwMplsFrrLspTrigger": hwMplsFrrLspTrigger,
       "hwMplsFrrLspTriggerIpPrefix": hwMplsFrrLspTriggerIpPrefix,
       "hwLdpBackOffTimerInit": hwLdpBackOffTimerInit,
       "hwLdpBackOffTimerMax": hwLdpBackOffTimerMax,
       "hwLdpLongestMatch": hwLdpLongestMatch,
       "hwLdpRemotePeerAutoDodRequest": hwLdpRemotePeerAutoDodRequest,
       "hwLdpCapabilityAnnouncementConfig": hwLdpCapabilityAnnouncementConfig,
       "hwLdpVpnTable": hwLdpVpnTable,
       "hwLdpVpnEntry": hwLdpVpnEntry,
       "hwLdpVpnInstanceId": hwLdpVpnInstanceId,
       "hwLdpVpnLsrId": hwLdpVpnLsrId,
       "hwLdpVpnSplitHorizonAll": hwLdpVpnSplitHorizonAll,
       "hwLdpVpnReset": hwLdpVpnReset,
       "hwMplsVpnFrrLspTrigger": hwMplsVpnFrrLspTrigger,
       "hwMplsVpnFrrLspTriggerIpPrefix": hwMplsVpnFrrLspTriggerIpPrefix,
       "hwLdpVpnGracefulDeleteCapability": hwLdpVpnGracefulDeleteCapability,
       "hwLdpVpnGracefulDeleteTimer": hwLdpVpnGracefulDeleteTimer,
       "hwLdpVpnRowStatus": hwLdpVpnRowStatus,
       "hwLdpRemoteEntityTable": hwLdpRemoteEntityTable,
       "hwLdpRemoteEntityEntry": hwLdpRemoteEntityEntry,
       "hwLdpRemoteName": hwLdpRemoteName,
       "hwLdpRemoteIp": hwLdpRemoteIp,
       "hwLdpRemotePwe3": hwLdpRemotePwe3,
       "hwLdpRemoteKeepaliveTimer": hwLdpRemoteKeepaliveTimer,
       "hwLdpRemoteHelloTimer": hwLdpRemoteHelloTimer,
       "hwLdpRemoteKeepaliveSendTimer": hwLdpRemoteKeepaliveSendTimer,
       "hwLdpRemoteHelloSendTimer": hwLdpRemoteHelloSendTimer,
       "hwLdpRemoteIgpSyncTimer": hwLdpRemoteIgpSyncTimer,
       "hwLdpRemoteIpAutoDoDRequest": hwLdpRemoteIpAutoDoDRequest,
       "hwLdpRemoteIpAutoDoDRequestBlock": hwLdpRemoteIpAutoDoDRequestBlock,
       "hwLdpRemoteLabelAdvertisementMode": hwLdpRemoteLabelAdvertisementMode,
       "hwLdpRemoteLocalLsrIdIfIndex": hwLdpRemoteLocalLsrIdIfIndex,
       "hwLdpRemoteRowStatus": hwLdpRemoteRowStatus,
       "hwLdpPeerTable": hwLdpPeerTable,
       "hwLdpPeerEntry": hwLdpPeerEntry,
       "hwLdpPeerLsrId": hwLdpPeerLsrId,
       "hwLdpPeerMd5Type": hwLdpPeerMd5Type,
       "hwLdpPeerMd5Password": hwLdpPeerMd5Password,
       "hwLdpPeerGtsmHops": hwLdpPeerGtsmHops,
       "hwLdpPeerSplitHorizon": hwLdpPeerSplitHorizon,
       "hwLdpPeerReset": hwLdpPeerReset,
       "hwLdpPeerKeychainName": hwLdpPeerKeychainName,
       "hwLdpPeerOutBoundPolicyRange": hwLdpPeerOutBoundPolicyRange,
       "hwLdpPeerOutBoundPolicyFecIpPrefix": hwLdpPeerOutBoundPolicyFecIpPrefix,
       "hwLdpPeerOutBoundPolicyBgpRange": hwLdpPeerOutBoundPolicyBgpRange,
       "hwLdpPeerOutBoundPolicyBgpIpPrefix": hwLdpPeerOutBoundPolicyBgpIpPrefix,
       "hwLdpPeerInBoundPolicyRange": hwLdpPeerInBoundPolicyRange,
       "hwLdpPeerInBoundPolicyFecIpPrefix": hwLdpPeerInBoundPolicyFecIpPrefix,
       "hwLdpPeerRowStatus": hwLdpPeerRowStatus,
       "hwLdpVpnPeerTable": hwLdpVpnPeerTable,
       "hwLdpVpnPeerEntry": hwLdpVpnPeerEntry,
       "hwLdpVpnPeerLsrId": hwLdpVpnPeerLsrId,
       "hwLdpVpnPeerMd5Type": hwLdpVpnPeerMd5Type,
       "hwLdpVpnPeerMd5Password": hwLdpVpnPeerMd5Password,
       "hwLdpVpnPeerSplitHorizon": hwLdpVpnPeerSplitHorizon,
       "hwLdpVpnPeerReset": hwLdpVpnPeerReset,
       "hwLdpVpnPeerKeychainName": hwLdpVpnPeerKeychainName,
       "hwLdpVpnPeerRowStatus": hwLdpVpnPeerRowStatus,
       "hwLdpInterfaceTable": hwLdpInterfaceTable,
       "hwLdpInterfaceEntry": hwLdpInterfaceEntry,
       "hwLdpInterfaceIndex": hwLdpInterfaceIndex,
       "hwLdpStaticFrrProtectTimer": hwLdpStaticFrrProtectTimer,
       "hwLdpKeepAliveTimer": hwLdpKeepAliveTimer,
       "hwLdpIgpSyncTimer": hwLdpIgpSyncTimer,
       "hwLdpHelloTimer": hwLdpHelloTimer,
       "hwLdpTransportAddressIfIndex": hwLdpTransportAddressIfIndex,
       "hwLdpKeepAliveSendTimer": hwLdpKeepAliveSendTimer,
       "hwLdpHelloSendTimer": hwLdpHelloSendTimer,
       "hwLdpInterfaceLabelAdvertisementMode": hwLdpInterfaceLabelAdvertisementMode,
       "hwLdpInterfaceLocalLsrIdIfIndex": hwLdpInterfaceLocalLsrIdIfIndex,
       "hwLdpInterfaceRowStatus": hwLdpInterfaceRowStatus,
       "hwLdpPeerGroupTable": hwLdpPeerGroupTable,
       "hwLdpPeerGroupEntry": hwLdpPeerGroupEntry,
       "hwLdpPeerGroupName": hwLdpPeerGroupName,
       "hwLdpPeerGroupOutBoundRange": hwLdpPeerGroupOutBoundRange,
       "hwLdpPeerGroupOutBoundFecIpPrefix": hwLdpPeerGroupOutBoundFecIpPrefix,
       "hwLdpPeerGroupOutBoundBgpRange": hwLdpPeerGroupOutBoundBgpRange,
       "hwLdpPeerGroupOutBoundBgpIpPrefix": hwLdpPeerGroupOutBoundBgpIpPrefix,
       "hwLdpPeerGroupInBoundRange": hwLdpPeerGroupInBoundRange,
       "hwLdpPeerGroupInBoundIpPrefix": hwLdpPeerGroupInBoundIpPrefix,
       "hwLdpPeerGroupRowStatus": hwLdpPeerGroupRowStatus,
       "hwLdpOutBoundPolicyPeerAllRange": hwLdpOutBoundPolicyPeerAllRange,
       "hwLdpOutBoundPolicyPeerAllFecIpPrefix": hwLdpOutBoundPolicyPeerAllFecIpPrefix,
       "hwLdpOutBoundPolicyPeerAllBgpRange": hwLdpOutBoundPolicyPeerAllBgpRange,
       "hwLdpOutBoundPolicyPeerAllBgpIpPrefix": hwLdpOutBoundPolicyPeerAllBgpIpPrefix,
       "hwLdpInBoundPolicyPeerAllRange": hwLdpInBoundPolicyPeerAllRange,
       "hwLdpInBoundPolicyPeerAllIpPrefix": hwLdpInBoundPolicyPeerAllIpPrefix,
       "hwLdpGracefulDeleteCapability": hwLdpGracefulDeleteCapability,
       "hwLdpGracefulDeleteTimer": hwLdpGracefulDeleteTimer,
       "hwLdpLspDownReason": hwLdpLspDownReason,
       "hwLdpLspDownMplsLsrId": hwLdpLspDownMplsLsrId,
       "hwLdpLspDownOutIfIndex": hwLdpLspDownOutIfIndex,
       "hwLdpLspDownOutIfMainIp": hwLdpLspDownOutIfMainIp,
       "hwLdpLspDownOutIfState": hwLdpLspDownOutIfState,
       "hwLdpLspDownDownstreamPeerLsrId": hwLdpLspDownDownstreamPeerLsrId,
       "hwLdpSessionStatistics": hwLdpSessionStatistics,
       "hwLdpLocalOperationalSessionNumber": hwLdpLocalOperationalSessionNumber,
       "hwLdpRemoteOperationalSessionNumber": hwLdpRemoteOperationalSessionNumber,
       "hwLdpLocalAndRemoteOperationalSessionNumber": hwLdpLocalAndRemoteOperationalSessionNumber,
       "hwLdpTotalOperationalSessionNumber": hwLdpTotalOperationalSessionNumber,
       "hwMplsLdpTrap": hwMplsLdpTrap,
       "hwMplsLdpSessionDown": hwMplsLdpSessionDown,
       "hwMplsLdpLspDown": hwMplsLdpLspDown,
       "hwMplsLdpHostIngressLspDownClear": hwMplsLdpHostIngressLspDownClear,
       "hwMplsLdpHostIngressLspDown": hwMplsLdpHostIngressLspDown,
       "hwMplsLdpConformance": hwMplsLdpConformance,
       "hwMplsLdpCompliances": hwMplsLdpCompliances,
       "hwMplsLdpGroup": hwMplsLdpGroup,
       "hwMplsLdpInfoGroup": hwMplsLdpInfoGroup,
       "hwMplsLdpNotificationGroup": hwMplsLdpNotificationGroup,
       "hwMplsLdpLspDownNotificationGroup": hwMplsLdpLspDownNotificationGroup,
       "hwMplsLdpGlobalGroup": hwMplsLdpGlobalGroup,
       "hwMplsLdpVpnGlobalGroup": hwMplsLdpVpnGlobalGroup,
       "hwMplsLdpRemoteEntityGroup": hwMplsLdpRemoteEntityGroup,
       "hwMplsLdpPeerGroup": hwMplsLdpPeerGroup,
       "hwMplsLdpVpnPeerGroup": hwMplsLdpVpnPeerGroup,
       "hwMplsLdpInterfaceGroup": hwMplsLdpInterfaceGroup,
       "hwLdpLspDownReasonGroup": hwLdpLspDownReasonGroup,
       "hwMplsLdpHostIngressLspDownNotificationGroup": hwMplsLdpHostIngressLspDownNotificationGroup,
       "hwLdpPolicyPeerGroupGroup": hwLdpPolicyPeerGroupGroup,
       "hwMplsLdpFrrProtectGroup": hwMplsLdpFrrProtectGroup,
       "hwMplsLdpSessionStatisticsGroup": hwMplsLdpSessionStatisticsGroup}
)
