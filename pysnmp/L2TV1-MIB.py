# SNMP MIB module (L2TV1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/L2TV1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:47 2024
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
 enterprises,
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
    "enterprises",
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

_IbmIROCroutingl2t_ObjectIdentity = ObjectIdentity
ibmIROCroutingl2t = _IbmIROCroutingl2t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7)
)
_L2tScalar_ObjectIdentity = ObjectIdentity
l2tScalar = _L2tScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1)
)
_L2tScalarConfig_ObjectIdentity = ObjectIdentity
l2tScalarConfig = _L2tScalarConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1)
)


class _L2tAdminState_Type(Integer32):
    """Custom type l2tAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_L2tAdminState_Type.__name__ = "Integer32"
_L2tAdminState_Object = MibScalar
l2tAdminState = _L2tAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1, 1),
    _L2tAdminState_Type()
)
l2tAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAdminState.setStatus("mandatory")


class _L2tAuthenticateIncomingTunnelSetupRequests_Type(Integer32):
    """Custom type l2tAuthenticateIncomingTunnelSetupRequests based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_L2tAuthenticateIncomingTunnelSetupRequests_Type.__name__ = "Integer32"
_L2tAuthenticateIncomingTunnelSetupRequests_Object = MibScalar
l2tAuthenticateIncomingTunnelSetupRequests = _L2tAuthenticateIncomingTunnelSetupRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1, 2),
    _L2tAuthenticateIncomingTunnelSetupRequests_Type()
)
l2tAuthenticateIncomingTunnelSetupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthenticateIncomingTunnelSetupRequests.setStatus("mandatory")


class _L2tTunnelDataFlowControl_Type(Integer32):
    """Custom type l2tTunnelDataFlowControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_L2tTunnelDataFlowControl_Type.__name__ = "Integer32"
_L2tTunnelDataFlowControl_Object = MibScalar
l2tTunnelDataFlowControl = _L2tTunnelDataFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1, 3),
    _L2tTunnelDataFlowControl_Type()
)
l2tTunnelDataFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelDataFlowControl.setStatus("mandatory")


class _L2tControlRecvPacketWindow_Type(Integer32):
    """Custom type l2tControlRecvPacketWindow based on Integer32"""
    defaultValue = 4


_L2tControlRecvPacketWindow_Object = MibScalar
l2tControlRecvPacketWindow = _L2tControlRecvPacketWindow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1, 4),
    _L2tControlRecvPacketWindow_Type()
)
l2tControlRecvPacketWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tControlRecvPacketWindow.setStatus("mandatory")


class _L2tDataRecvPacketWindow_Type(Integer32):
    """Custom type l2tDataRecvPacketWindow based on Integer32"""
    defaultValue = 6


_L2tDataRecvPacketWindow_Object = MibScalar
l2tDataRecvPacketWindow = _L2tDataRecvPacketWindow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1, 5),
    _L2tDataRecvPacketWindow_Type()
)
l2tDataRecvPacketWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tDataRecvPacketWindow.setStatus("mandatory")


class _L2tHelloTimer_Type(Integer32):
    """Custom type l2tHelloTimer based on Integer32"""
    defaultValue = 60


_L2tHelloTimer_Object = MibScalar
l2tHelloTimer = _L2tHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1, 6),
    _L2tHelloTimer_Type()
)
l2tHelloTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHelloTimer.setStatus("mandatory")


class _L2tControlRetransmissions_Type(Integer32):
    """Custom type l2tControlRetransmissions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tControlRetransmissions_Type.__name__ = "Integer32"
_L2tControlRetransmissions_Object = MibScalar
l2tControlRetransmissions = _L2tControlRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1, 7),
    _L2tControlRetransmissions_Type()
)
l2tControlRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tControlRetransmissions.setStatus("mandatory")


class _L2tSecurityExtensions_Type(Integer32):
    """Custom type l2tSecurityExtensions based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_L2tSecurityExtensions_Type.__name__ = "Integer32"
_L2tSecurityExtensions_Object = MibScalar
l2tSecurityExtensions = _L2tSecurityExtensions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1, 8),
    _L2tSecurityExtensions_Type()
)
l2tSecurityExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSecurityExtensions.setStatus("mandatory")
_L2tHistoryWindowSize_Type = Integer32
_L2tHistoryWindowSize_Object = MibScalar
l2tHistoryWindowSize = _L2tHistoryWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1, 9),
    _L2tHistoryWindowSize_Type()
)
l2tHistoryWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tHistoryWindowSize.setStatus("mandatory")
_L2tAuthFailWindowSize_Type = Integer32
_L2tAuthFailWindowSize_Object = MibScalar
l2tAuthFailWindowSize = _L2tAuthFailWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 1, 10),
    _L2tAuthFailWindowSize_Type()
)
l2tAuthFailWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tAuthFailWindowSize.setStatus("mandatory")
_L2tScalarStat_ObjectIdentity = ObjectIdentity
l2tScalarStat = _L2tScalarStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 2)
)
_L2tMibVersion_Type = Integer32
_L2tMibVersion_Object = MibScalar
l2tMibVersion = _L2tMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 2, 1),
    _L2tMibVersion_Type()
)
l2tMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tMibVersion.setStatus("mandatory")


class _L2tProtocolVersion_Type(OctetString):
    """Custom type l2tProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_L2tProtocolVersion_Type.__name__ = "OctetString"
_L2tProtocolVersion_Object = MibScalar
l2tProtocolVersion = _L2tProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 2, 2),
    _L2tProtocolVersion_Type()
)
l2tProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tProtocolVersion.setStatus("mandatory")
_L2tNumActiveTunnels_Type = Integer32
_L2tNumActiveTunnels_Object = MibScalar
l2tNumActiveTunnels = _L2tNumActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 2, 3),
    _L2tNumActiveTunnels_Type()
)
l2tNumActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tNumActiveTunnels.setStatus("mandatory")
_L2tStatsNumActiveSessions_Type = Integer32
_L2tStatsNumActiveSessions_Object = MibScalar
l2tStatsNumActiveSessions = _L2tStatsNumActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 1, 2, 4),
    _L2tStatsNumActiveSessions_Type()
)
l2tStatsNumActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tStatsNumActiveSessions.setStatus("mandatory")
_L2tStats_ObjectIdentity = ObjectIdentity
l2tStats = _L2tStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2)
)
_L2tTunnelStatsTable_Object = MibTable
l2tTunnelStatsTable = _L2tTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1)
)
if mibBuilder.loadTexts:
    l2tTunnelStatsTable.setStatus("mandatory")
_L2tTunnelStatsEntry_Object = MibTableRow
l2tTunnelStatsEntry = _L2tTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1)
)
l2tTunnelStatsEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tTunnelLocalTunnelControlId"),
)
if mibBuilder.loadTexts:
    l2tTunnelStatsEntry.setStatus("mandatory")
_L2tTunnelLocalTunnelControlId_Type = Integer32
_L2tTunnelLocalTunnelControlId_Object = MibTableColumn
l2tTunnelLocalTunnelControlId = _L2tTunnelLocalTunnelControlId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 1),
    _L2tTunnelLocalTunnelControlId_Type()
)
l2tTunnelLocalTunnelControlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelLocalTunnelControlId.setStatus("mandatory")
_L2tTunnelPeerTunnelControlId_Type = Integer32
_L2tTunnelPeerTunnelControlId_Object = MibTableColumn
l2tTunnelPeerTunnelControlId = _L2tTunnelPeerTunnelControlId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 2),
    _L2tTunnelPeerTunnelControlId_Type()
)
l2tTunnelPeerTunnelControlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelPeerTunnelControlId.setStatus("mandatory")


class _L2tTunnelControlState_Type(Integer32):
    """Custom type l2tTunnelControlState based on Integer32"""
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
        *(("l2ttunnelestablished", 4),
          ("l2ttunnelhold", 5),
          ("l2ttunnelidle", 1),
          ("l2ttunnelwaitctrlconn", 3),
          ("l2ttunnelwaitctrlreply", 2))
    )


_L2tTunnelControlState_Type.__name__ = "Integer32"
_L2tTunnelControlState_Object = MibTableColumn
l2tTunnelControlState = _L2tTunnelControlState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 3),
    _L2tTunnelControlState_Type()
)
l2tTunnelControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelControlState.setStatus("mandatory")


class _L2tTunnelLocalInitConnection_Type(Integer32):
    """Custom type l2tTunnelLocalInitConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_L2tTunnelLocalInitConnection_Type.__name__ = "Integer32"
_L2tTunnelLocalInitConnection_Object = MibTableColumn
l2tTunnelLocalInitConnection = _L2tTunnelLocalInitConnection_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 4),
    _L2tTunnelLocalInitConnection_Type()
)
l2tTunnelLocalInitConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelLocalInitConnection.setStatus("mandatory")
_L2tTunnelLocalRecvPktWindow_Type = Integer32
_L2tTunnelLocalRecvPktWindow_Object = MibTableColumn
l2tTunnelLocalRecvPktWindow = _L2tTunnelLocalRecvPktWindow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 5),
    _L2tTunnelLocalRecvPktWindow_Type()
)
l2tTunnelLocalRecvPktWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelLocalRecvPktWindow.setStatus("mandatory")
_L2tTunnelRemoteRecvPktWindow_Type = Integer32
_L2tTunnelRemoteRecvPktWindow_Object = MibTableColumn
l2tTunnelRemoteRecvPktWindow = _L2tTunnelRemoteRecvPktWindow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 6),
    _L2tTunnelRemoteRecvPktWindow_Type()
)
l2tTunnelRemoteRecvPktWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelRemoteRecvPktWindow.setStatus("mandatory")
_L2tTunnelCtlTunnelFlwCtlTimeouts_Type = Counter32
_L2tTunnelCtlTunnelFlwCtlTimeouts_Object = MibTableColumn
l2tTunnelCtlTunnelFlwCtlTimeouts = _L2tTunnelCtlTunnelFlwCtlTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 7),
    _L2tTunnelCtlTunnelFlwCtlTimeouts_Type()
)
l2tTunnelCtlTunnelFlwCtlTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelCtlTunnelFlwCtlTimeouts.setStatus("mandatory")
_L2tTunnelRemoteHostName_Type = DisplayString
_L2tTunnelRemoteHostName_Object = MibTableColumn
l2tTunnelRemoteHostName = _L2tTunnelRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 8),
    _L2tTunnelRemoteHostName_Type()
)
l2tTunnelRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelRemoteHostName.setStatus("mandatory")
_L2tTunnelNextSendSeq_Type = Integer32
_L2tTunnelNextSendSeq_Object = MibTableColumn
l2tTunnelNextSendSeq = _L2tTunnelNextSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 9),
    _L2tTunnelNextSendSeq_Type()
)
l2tTunnelNextSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelNextSendSeq.setStatus("mandatory")
_L2tTunnelNextRecvSeq_Type = Integer32
_L2tTunnelNextRecvSeq_Object = MibTableColumn
l2tTunnelNextRecvSeq = _L2tTunnelNextRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 10),
    _L2tTunnelNextRecvSeq_Type()
)
l2tTunnelNextRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelNextRecvSeq.setStatus("mandatory")
_L2tTunnelRemoteVendorName_Type = DisplayString
_L2tTunnelRemoteVendorName_Object = MibTableColumn
l2tTunnelRemoteVendorName = _L2tTunnelRemoteVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 11),
    _L2tTunnelRemoteVendorName_Type()
)
l2tTunnelRemoteVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelRemoteVendorName.setStatus("mandatory")


class _L2tTunnelRemoteFirmwareRevision_Type(Integer32):
    """Custom type l2tTunnelRemoteFirmwareRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tTunnelRemoteFirmwareRevision_Type.__name__ = "Integer32"
_L2tTunnelRemoteFirmwareRevision_Object = MibTableColumn
l2tTunnelRemoteFirmwareRevision = _L2tTunnelRemoteFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 12),
    _L2tTunnelRemoteFirmwareRevision_Type()
)
l2tTunnelRemoteFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelRemoteFirmwareRevision.setStatus("mandatory")
_L2tTunnelRemoteProtocolVersion_Type = OctetString
_L2tTunnelRemoteProtocolVersion_Object = MibTableColumn
l2tTunnelRemoteProtocolVersion = _L2tTunnelRemoteProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 13),
    _L2tTunnelRemoteProtocolVersion_Type()
)
l2tTunnelRemoteProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelRemoteProtocolVersion.setStatus("mandatory")
_L2tTunnelActiveSessions_Type = Gauge32
_L2tTunnelActiveSessions_Object = MibTableColumn
l2tTunnelActiveSessions = _L2tTunnelActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 14),
    _L2tTunnelActiveSessions_Type()
)
l2tTunnelActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelActiveSessions.setStatus("mandatory")
_L2tTunnelPrevSessions_Type = Counter32
_L2tTunnelPrevSessions_Object = MibTableColumn
l2tTunnelPrevSessions = _L2tTunnelPrevSessions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 15),
    _L2tTunnelPrevSessions_Type()
)
l2tTunnelPrevSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelPrevSessions.setStatus("mandatory")
_L2tTunnelUpTime_Type = TimeTicks
_L2tTunnelUpTime_Object = MibTableColumn
l2tTunnelUpTime = _L2tTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 16),
    _L2tTunnelUpTime_Type()
)
l2tTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelUpTime.setStatus("mandatory")


class _L2tTunnelType_Type(Integer32):
    """Custom type l2tTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2fTunnel", 2),
          ("l2tpTunnel", 1),
          ("pptpTunnel", 3))
    )


_L2tTunnelType_Type.__name__ = "Integer32"
_L2tTunnelType_Object = MibTableColumn
l2tTunnelType = _L2tTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 17),
    _L2tTunnelType_Type()
)
l2tTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelType.setStatus("mandatory")
_L2tTunnelInOctets_Type = Counter32
_L2tTunnelInOctets_Object = MibTableColumn
l2tTunnelInOctets = _L2tTunnelInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 18),
    _L2tTunnelInOctets_Type()
)
l2tTunnelInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelInOctets.setStatus("mandatory")
_L2tTunnelInPkts_Type = Counter32
_L2tTunnelInPkts_Object = MibTableColumn
l2tTunnelInPkts = _L2tTunnelInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 19),
    _L2tTunnelInPkts_Type()
)
l2tTunnelInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelInPkts.setStatus("mandatory")
_L2tTunnelInDiscards_Type = Counter32
_L2tTunnelInDiscards_Object = MibTableColumn
l2tTunnelInDiscards = _L2tTunnelInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 20),
    _L2tTunnelInDiscards_Type()
)
l2tTunnelInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelInDiscards.setStatus("mandatory")
_L2tTunnelOutOctets_Type = Counter32
_L2tTunnelOutOctets_Object = MibTableColumn
l2tTunnelOutOctets = _L2tTunnelOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 21),
    _L2tTunnelOutOctets_Type()
)
l2tTunnelOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelOutOctets.setStatus("mandatory")
_L2tTunnelOutPkts_Type = Counter32
_L2tTunnelOutPkts_Object = MibTableColumn
l2tTunnelOutPkts = _L2tTunnelOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 22),
    _L2tTunnelOutPkts_Type()
)
l2tTunnelOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelOutPkts.setStatus("mandatory")
_L2tTunnelOutDiscards_Type = Counter32
_L2tTunnelOutDiscards_Object = MibTableColumn
l2tTunnelOutDiscards = _L2tTunnelOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 23),
    _L2tTunnelOutDiscards_Type()
)
l2tTunnelOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelOutDiscards.setStatus("mandatory")


class _L2tTunnelStatus_Type(Integer32):
    """Custom type l2tTunnelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 2))
    )


_L2tTunnelStatus_Type.__name__ = "Integer32"
_L2tTunnelStatus_Object = MibTableColumn
l2tTunnelStatus = _L2tTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 1, 1, 24),
    _L2tTunnelStatus_Type()
)
l2tTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tTunnelStatus.setStatus("mandatory")
_L2tSessionStatsTable_Object = MibTable
l2tSessionStatsTable = _L2tSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2)
)
if mibBuilder.loadTexts:
    l2tSessionStatsTable.setStatus("mandatory")
_L2tSessionStatsEntry_Object = MibTableRow
l2tSessionStatsEntry = _L2tSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1)
)
l2tSessionStatsEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tSessionLocalControlTunnelId"),
    (0, "L2TV1-MIB", "l2tSessionLocalCallId"),
)
if mibBuilder.loadTexts:
    l2tSessionStatsEntry.setStatus("mandatory")
_L2tSessionLocalControlTunnelId_Type = Integer32
_L2tSessionLocalControlTunnelId_Object = MibTableColumn
l2tSessionLocalControlTunnelId = _L2tSessionLocalControlTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 1),
    _L2tSessionLocalControlTunnelId_Type()
)
l2tSessionLocalControlTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionLocalControlTunnelId.setStatus("mandatory")
_L2tSessionLocalCallId_Type = Integer32
_L2tSessionLocalCallId_Object = MibTableColumn
l2tSessionLocalCallId = _L2tSessionLocalCallId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 2),
    _L2tSessionLocalCallId_Type()
)
l2tSessionLocalCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionLocalCallId.setStatus("mandatory")
_L2tSessionRemoteCallId_Type = Integer32
_L2tSessionRemoteCallId_Object = MibTableColumn
l2tSessionRemoteCallId = _L2tSessionRemoteCallId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 3),
    _L2tSessionRemoteCallId_Type()
)
l2tSessionRemoteCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionRemoteCallId.setStatus("mandatory")
_L2tSessionPeerName_Type = DisplayString
_L2tSessionPeerName_Object = MibTableColumn
l2tSessionPeerName = _L2tSessionPeerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 4),
    _L2tSessionPeerName_Type()
)
l2tSessionPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionPeerName.setStatus("mandatory")


class _L2tSessionLineState_Type(Integer32):
    """Custom type l2tSessionLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("callestablished", 6),
          ("callidle", 2),
          ("callwaitconnect", 4),
          ("callwaitcsanswer", 5),
          ("callwaitreply", 3),
          ("callwaittunnel", 1))
    )


_L2tSessionLineState_Type.__name__ = "Integer32"
_L2tSessionLineState_Object = MibTableColumn
l2tSessionLineState = _L2tSessionLineState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 5),
    _L2tSessionLineState_Type()
)
l2tSessionLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionLineState.setStatus("mandatory")
_L2tSessionCallDeviceNumber_Type = Integer32
_L2tSessionCallDeviceNumber_Object = MibTableColumn
l2tSessionCallDeviceNumber = _L2tSessionCallDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 6),
    _L2tSessionCallDeviceNumber_Type()
)
l2tSessionCallDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionCallDeviceNumber.setStatus("mandatory")
_L2tSessionCallSerialNumber_Type = DisplayString
_L2tSessionCallSerialNumber_Object = MibTableColumn
l2tSessionCallSerialNumber = _L2tSessionCallSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 7),
    _L2tSessionCallSerialNumber_Type()
)
l2tSessionCallSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionCallSerialNumber.setStatus("mandatory")
_L2tSessionConnectBps_Type = Integer32
_L2tSessionConnectBps_Object = MibTableColumn
l2tSessionConnectBps = _L2tSessionConnectBps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 8),
    _L2tSessionConnectBps_Type()
)
l2tSessionConnectBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionConnectBps.setStatus("mandatory")


class _L2tSessionCallBearerType_Type(Integer32):
    """Custom type l2tSessionCallBearerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("digital", 1))
    )


_L2tSessionCallBearerType_Type.__name__ = "Integer32"
_L2tSessionCallBearerType_Object = MibTableColumn
l2tSessionCallBearerType = _L2tSessionCallBearerType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 9),
    _L2tSessionCallBearerType_Type()
)
l2tSessionCallBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionCallBearerType.setStatus("mandatory")


class _L2tSessionFramingType_Type(Integer32):
    """Custom type l2tSessionFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 2),
          ("synchronous", 1))
    )


_L2tSessionFramingType_Type.__name__ = "Integer32"
_L2tSessionFramingType_Object = MibTableColumn
l2tSessionFramingType = _L2tSessionFramingType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 10),
    _L2tSessionFramingType_Type()
)
l2tSessionFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionFramingType.setStatus("mandatory")
_L2tSessionLocalRecvPacketWindow_Type = Integer32
_L2tSessionLocalRecvPacketWindow_Object = MibTableColumn
l2tSessionLocalRecvPacketWindow = _L2tSessionLocalRecvPacketWindow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 11),
    _L2tSessionLocalRecvPacketWindow_Type()
)
l2tSessionLocalRecvPacketWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionLocalRecvPacketWindow.setStatus("mandatory")
_L2tSessionRemoteRecvPacketWindow_Type = Integer32
_L2tSessionRemoteRecvPacketWindow_Object = MibTableColumn
l2tSessionRemoteRecvPacketWindow = _L2tSessionRemoteRecvPacketWindow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 12),
    _L2tSessionRemoteRecvPacketWindow_Type()
)
l2tSessionRemoteRecvPacketWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionRemoteRecvPacketWindow.setStatus("mandatory")
_L2tSessionDataRecvOctets_Type = Counter32
_L2tSessionDataRecvOctets_Object = MibTableColumn
l2tSessionDataRecvOctets = _L2tSessionDataRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 13),
    _L2tSessionDataRecvOctets_Type()
)
l2tSessionDataRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionDataRecvOctets.setStatus("mandatory")
_L2tSessionDataRecvDecompOctets_Type = Counter32
_L2tSessionDataRecvDecompOctets_Object = MibTableColumn
l2tSessionDataRecvDecompOctets = _L2tSessionDataRecvDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 14),
    _L2tSessionDataRecvDecompOctets_Type()
)
l2tSessionDataRecvDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionDataRecvDecompOctets.setStatus("mandatory")
_L2tSessionDataRecvPackets_Type = Counter32
_L2tSessionDataRecvPackets_Object = MibTableColumn
l2tSessionDataRecvPackets = _L2tSessionDataRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 15),
    _L2tSessionDataRecvPackets_Type()
)
l2tSessionDataRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionDataRecvPackets.setStatus("mandatory")
_L2tSessionDataRecvDiscards_Type = Counter32
_L2tSessionDataRecvDiscards_Object = MibTableColumn
l2tSessionDataRecvDiscards = _L2tSessionDataRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 16),
    _L2tSessionDataRecvDiscards_Type()
)
l2tSessionDataRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionDataRecvDiscards.setStatus("mandatory")
_L2tSessionDataSendOctets_Type = Counter32
_L2tSessionDataSendOctets_Object = MibTableColumn
l2tSessionDataSendOctets = _L2tSessionDataSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 17),
    _L2tSessionDataSendOctets_Type()
)
l2tSessionDataSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionDataSendOctets.setStatus("mandatory")
_L2tSessionDataSendUncompOctets_Type = Counter32
_L2tSessionDataSendUncompOctets_Object = MibTableColumn
l2tSessionDataSendUncompOctets = _L2tSessionDataSendUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 18),
    _L2tSessionDataSendUncompOctets_Type()
)
l2tSessionDataSendUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionDataSendUncompOctets.setStatus("mandatory")
_L2tSessionDataSendPackets_Type = Counter32
_L2tSessionDataSendPackets_Object = MibTableColumn
l2tSessionDataSendPackets = _L2tSessionDataSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 19),
    _L2tSessionDataSendPackets_Type()
)
l2tSessionDataSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionDataSendPackets.setStatus("mandatory")
_L2tSessionDataSendDiscards_Type = Counter32
_L2tSessionDataSendDiscards_Object = MibTableColumn
l2tSessionDataSendDiscards = _L2tSessionDataSendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 20),
    _L2tSessionDataSendDiscards_Type()
)
l2tSessionDataSendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionDataSendDiscards.setStatus("mandatory")
_L2tSessionDataFlowControlTimeouts_Type = Counter32
_L2tSessionDataFlowControlTimeouts_Object = MibTableColumn
l2tSessionDataFlowControlTimeouts = _L2tSessionDataFlowControlTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 21),
    _L2tSessionDataFlowControlTimeouts_Type()
)
l2tSessionDataFlowControlTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionDataFlowControlTimeouts.setStatus("mandatory")
_L2tSessionNextSendSeq_Type = Integer32
_L2tSessionNextSendSeq_Object = MibTableColumn
l2tSessionNextSendSeq = _L2tSessionNextSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 22),
    _L2tSessionNextSendSeq_Type()
)
l2tSessionNextSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionNextSendSeq.setStatus("mandatory")
_L2tSessionNextRecvSeq_Type = Integer32
_L2tSessionNextRecvSeq_Object = MibTableColumn
l2tSessionNextRecvSeq = _L2tSessionNextRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 23),
    _L2tSessionNextRecvSeq_Type()
)
l2tSessionNextRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionNextRecvSeq.setStatus("mandatory")
_L2tSessionRemotePPD_Type = Integer32
_L2tSessionRemotePPD_Object = MibTableColumn
l2tSessionRemotePPD = _L2tSessionRemotePPD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 24),
    _L2tSessionRemotePPD_Type()
)
l2tSessionRemotePPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionRemotePPD.setStatus("mandatory")


class _L2tSessionAuthMethod_Type(Integer32):
    """Custom type l2tSessionAuthMethod based on Integer32"""
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
        *(("none", 4),
          ("pppchap", 2),
          ("ppppap", 3),
          ("text", 1))
    )


_L2tSessionAuthMethod_Type.__name__ = "Integer32"
_L2tSessionAuthMethod_Object = MibTableColumn
l2tSessionAuthMethod = _L2tSessionAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 25),
    _L2tSessionAuthMethod_Type()
)
l2tSessionAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionAuthMethod.setStatus("mandatory")


class _L2tSessionEncryptDecrypt_Type(Integer32):
    """Custom type l2tSessionEncryptDecrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_L2tSessionEncryptDecrypt_Type.__name__ = "Integer32"
_L2tSessionEncryptDecrypt_Object = MibTableColumn
l2tSessionEncryptDecrypt = _L2tSessionEncryptDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 26),
    _L2tSessionEncryptDecrypt_Type()
)
l2tSessionEncryptDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionEncryptDecrypt.setStatus("mandatory")
_L2tSessionUpTime_Type = TimeTicks
_L2tSessionUpTime_Object = MibTableColumn
l2tSessionUpTime = _L2tSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 27),
    _L2tSessionUpTime_Type()
)
l2tSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tSessionUpTime.setStatus("mandatory")


class _L2tSessionStatus_Type(Integer32):
    """Custom type l2tSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 2))
    )


_L2tSessionStatus_Type.__name__ = "Integer32"
_L2tSessionStatus_Object = MibTableColumn
l2tSessionStatus = _L2tSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 2, 2, 1, 28),
    _L2tSessionStatus_Type()
)
l2tSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tSessionStatus.setStatus("mandatory")
_L2tUdp_ObjectIdentity = ObjectIdentity
l2tUdp = _L2tUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3)
)
_L2tUdpConfigTable_Object = MibTable
l2tUdpConfigTable = _L2tUdpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3, 1)
)
if mibBuilder.loadTexts:
    l2tUdpConfigTable.setStatus("mandatory")
_L2tUdpConfigEntry_Object = MibTableRow
l2tUdpConfigEntry = _L2tUdpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3, 1, 1)
)
l2tUdpConfigEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tTunnelLocalTunnelControlId"),
)
if mibBuilder.loadTexts:
    l2tUdpConfigEntry.setStatus("mandatory")
_L2tUdpPeerAddress_Type = IpAddress
_L2tUdpPeerAddress_Object = MibTableColumn
l2tUdpPeerAddress = _L2tUdpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3, 1, 1, 1),
    _L2tUdpPeerAddress_Type()
)
l2tUdpPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tUdpPeerAddress.setStatus("mandatory")


class _L2tUdpPeerPort_Type(Integer32):
    """Custom type l2tUdpPeerPort based on Integer32"""
    defaultValue = 1701


_L2tUdpPeerPort_Object = MibTableColumn
l2tUdpPeerPort = _L2tUdpPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3, 1, 1, 2),
    _L2tUdpPeerPort_Type()
)
l2tUdpPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tUdpPeerPort.setStatus("mandatory")
_L2tUdpStatsTable_Object = MibTable
l2tUdpStatsTable = _L2tUdpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3, 2)
)
if mibBuilder.loadTexts:
    l2tUdpStatsTable.setStatus("mandatory")
_L2tUdpStatsEntry_Object = MibTableRow
l2tUdpStatsEntry = _L2tUdpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3, 2, 1)
)
l2tUdpStatsEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tTunnelLocalTunnelControlId"),
)
if mibBuilder.loadTexts:
    l2tUdpStatsEntry.setStatus("mandatory")
_L2tUdpPeerIpAddress_Type = IpAddress
_L2tUdpPeerIpAddress_Object = MibTableColumn
l2tUdpPeerIpAddress = _L2tUdpPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3, 2, 1, 1),
    _L2tUdpPeerIpAddress_Type()
)
l2tUdpPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tUdpPeerIpAddress.setStatus("mandatory")
_L2tUdpLocalIpAddress_Type = IpAddress
_L2tUdpLocalIpAddress_Object = MibTableColumn
l2tUdpLocalIpAddress = _L2tUdpLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3, 2, 1, 2),
    _L2tUdpLocalIpAddress_Type()
)
l2tUdpLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tUdpLocalIpAddress.setStatus("mandatory")
_L2tUdpSrcPort_Type = Integer32
_L2tUdpSrcPort_Object = MibTableColumn
l2tUdpSrcPort = _L2tUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3, 2, 1, 3),
    _L2tUdpSrcPort_Type()
)
l2tUdpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tUdpSrcPort.setStatus("mandatory")
_L2tUdpDstPort_Type = Integer32
_L2tUdpDstPort_Object = MibTableColumn
l2tUdpDstPort = _L2tUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 3, 2, 1, 4),
    _L2tUdpDstPort_Type()
)
l2tUdpDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tUdpDstPort.setStatus("mandatory")
_L2tAuthentication_ObjectIdentity = ObjectIdentity
l2tAuthentication = _L2tAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4)
)
_L2tAuthStats_ObjectIdentity = ObjectIdentity
l2tAuthStats = _L2tAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 1)
)
_L2tAuthTunnelSuccesses_Type = Counter32
_L2tAuthTunnelSuccesses_Object = MibScalar
l2tAuthTunnelSuccesses = _L2tAuthTunnelSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 1, 1),
    _L2tAuthTunnelSuccesses_Type()
)
l2tAuthTunnelSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthTunnelSuccesses.setStatus("mandatory")
_L2tAuthTunnelFailures_Type = Counter32
_L2tAuthTunnelFailures_Object = MibScalar
l2tAuthTunnelFailures = _L2tAuthTunnelFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 1, 2),
    _L2tAuthTunnelFailures_Type()
)
l2tAuthTunnelFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthTunnelFailures.setStatus("mandatory")
_L2tAuthUserSuccesses_Type = Counter32
_L2tAuthUserSuccesses_Object = MibScalar
l2tAuthUserSuccesses = _L2tAuthUserSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 1, 3),
    _L2tAuthUserSuccesses_Type()
)
l2tAuthUserSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthUserSuccesses.setStatus("mandatory")
_L2tAuthUserFailures_Type = Counter32
_L2tAuthUserFailures_Object = MibScalar
l2tAuthUserFailures = _L2tAuthUserFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 1, 4),
    _L2tAuthUserFailures_Type()
)
l2tAuthUserFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthUserFailures.setStatus("mandatory")
_L2tAuthFailures_ObjectIdentity = ObjectIdentity
l2tAuthFailures = _L2tAuthFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2)
)
_L2tAuthFailTunnelTable_Object = MibTable
l2tAuthFailTunnelTable = _L2tAuthFailTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    l2tAuthFailTunnelTable.setStatus("mandatory")
_L2tAuthFailTunnelEntry_Object = MibTableRow
l2tAuthFailTunnelEntry = _L2tAuthFailTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 1, 1)
)
l2tAuthFailTunnelEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tAuthFailTunnelIndex"),
)
if mibBuilder.loadTexts:
    l2tAuthFailTunnelEntry.setStatus("mandatory")


class _L2tAuthFailTunnelIndex_Type(Integer32):
    """Custom type l2tAuthFailTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tAuthFailTunnelIndex_Type.__name__ = "Integer32"
_L2tAuthFailTunnelIndex_Object = MibTableColumn
l2tAuthFailTunnelIndex = _L2tAuthFailTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 1, 1, 1),
    _L2tAuthFailTunnelIndex_Type()
)
l2tAuthFailTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthFailTunnelIndex.setStatus("mandatory")
_L2tAuthFailTunnelHostName_Type = DisplayString
_L2tAuthFailTunnelHostName_Object = MibTableColumn
l2tAuthFailTunnelHostName = _L2tAuthFailTunnelHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 1, 1, 2),
    _L2tAuthFailTunnelHostName_Type()
)
l2tAuthFailTunnelHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthFailTunnelHostName.setStatus("mandatory")
_L2tAuthFailTunnelIpAddress_Type = IpAddress
_L2tAuthFailTunnelIpAddress_Object = MibTableColumn
l2tAuthFailTunnelIpAddress = _L2tAuthFailTunnelIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 1, 1, 3),
    _L2tAuthFailTunnelIpAddress_Type()
)
l2tAuthFailTunnelIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthFailTunnelIpAddress.setStatus("mandatory")
_L2tAuthFailTunnelTime_Type = TimeTicks
_L2tAuthFailTunnelTime_Object = MibTableColumn
l2tAuthFailTunnelTime = _L2tAuthFailTunnelTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 1, 1, 4),
    _L2tAuthFailTunnelTime_Type()
)
l2tAuthFailTunnelTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthFailTunnelTime.setStatus("mandatory")
_L2tAuthFailUserTable_Object = MibTable
l2tAuthFailUserTable = _L2tAuthFailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 2)
)
if mibBuilder.loadTexts:
    l2tAuthFailUserTable.setStatus("mandatory")
_L2tAuthFailUserEntry_Object = MibTableRow
l2tAuthFailUserEntry = _L2tAuthFailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 2, 1)
)
l2tAuthFailUserEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tAuthFailUserIndex"),
)
if mibBuilder.loadTexts:
    l2tAuthFailUserEntry.setStatus("mandatory")


class _L2tAuthFailUserIndex_Type(Integer32):
    """Custom type l2tAuthFailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tAuthFailUserIndex_Type.__name__ = "Integer32"
_L2tAuthFailUserIndex_Object = MibTableColumn
l2tAuthFailUserIndex = _L2tAuthFailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 2, 1, 1),
    _L2tAuthFailUserIndex_Type()
)
l2tAuthFailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthFailUserIndex.setStatus("mandatory")
_L2tAuthFailUserId_Type = DisplayString
_L2tAuthFailUserId_Object = MibTableColumn
l2tAuthFailUserId = _L2tAuthFailUserId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 2, 1, 2),
    _L2tAuthFailUserId_Type()
)
l2tAuthFailUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthFailUserId.setStatus("mandatory")
_L2tAuthFailUserTime_Type = TimeTicks
_L2tAuthFailUserTime_Object = MibTableColumn
l2tAuthFailUserTime = _L2tAuthFailUserTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 4, 2, 2, 1, 3),
    _L2tAuthFailUserTime_Type()
)
l2tAuthFailUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tAuthFailUserTime.setStatus("mandatory")
_L2tHistory_ObjectIdentity = ObjectIdentity
l2tHistory = _L2tHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5)
)
_L2tHistTunnelTable_Object = MibTable
l2tHistTunnelTable = _L2tHistTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1)
)
if mibBuilder.loadTexts:
    l2tHistTunnelTable.setStatus("mandatory")
_L2tHistTunnelEntry_Object = MibTableRow
l2tHistTunnelEntry = _L2tHistTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1)
)
l2tHistTunnelEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tHistTunnelIndex"),
)
if mibBuilder.loadTexts:
    l2tHistTunnelEntry.setStatus("mandatory")


class _L2tHistTunnelIndex_Type(Integer32):
    """Custom type l2tHistTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tHistTunnelIndex_Type.__name__ = "Integer32"
_L2tHistTunnelIndex_Object = MibTableColumn
l2tHistTunnelIndex = _L2tHistTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 1),
    _L2tHistTunnelIndex_Type()
)
l2tHistTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelIndex.setStatus("mandatory")
_L2tHistTunnelTunnelIndex_Type = Integer32
_L2tHistTunnelTunnelIndex_Object = MibTableColumn
l2tHistTunnelTunnelIndex = _L2tHistTunnelTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 2),
    _L2tHistTunnelTunnelIndex_Type()
)
l2tHistTunnelTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelTunnelIndex.setStatus("mandatory")
_L2tHistTunnelRemoteHostName_Type = DisplayString
_L2tHistTunnelRemoteHostName_Object = MibTableColumn
l2tHistTunnelRemoteHostName = _L2tHistTunnelRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 3),
    _L2tHistTunnelRemoteHostName_Type()
)
l2tHistTunnelRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelRemoteHostName.setStatus("mandatory")
_L2tHistTunnelRemoteIpAddress_Type = IpAddress
_L2tHistTunnelRemoteIpAddress_Object = MibTableColumn
l2tHistTunnelRemoteIpAddress = _L2tHistTunnelRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 4),
    _L2tHistTunnelRemoteIpAddress_Type()
)
l2tHistTunnelRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelRemoteIpAddress.setStatus("mandatory")
_L2tHistTunnelRemotePort_Type = Integer32
_L2tHistTunnelRemotePort_Object = MibTableColumn
l2tHistTunnelRemotePort = _L2tHistTunnelRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 5),
    _L2tHistTunnelRemotePort_Type()
)
l2tHistTunnelRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelRemotePort.setStatus("mandatory")
_L2tHistTunnelLocalIpAddress_Type = IpAddress
_L2tHistTunnelLocalIpAddress_Object = MibTableColumn
l2tHistTunnelLocalIpAddress = _L2tHistTunnelLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 6),
    _L2tHistTunnelLocalIpAddress_Type()
)
l2tHistTunnelLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelLocalIpAddress.setStatus("mandatory")
_L2tHistTunnelLocalPort_Type = Integer32
_L2tHistTunnelLocalPort_Object = MibTableColumn
l2tHistTunnelLocalPort = _L2tHistTunnelLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 7),
    _L2tHistTunnelLocalPort_Type()
)
l2tHistTunnelLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelLocalPort.setStatus("mandatory")
_L2tHistTunnelUpTime_Type = TimeTicks
_L2tHistTunnelUpTime_Object = MibTableColumn
l2tHistTunnelUpTime = _L2tHistTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 8),
    _L2tHistTunnelUpTime_Type()
)
l2tHistTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelUpTime.setStatus("mandatory")
_L2tHistTunnelTotalSessions_Type = Counter32
_L2tHistTunnelTotalSessions_Object = MibTableColumn
l2tHistTunnelTotalSessions = _L2tHistTunnelTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 9),
    _L2tHistTunnelTotalSessions_Type()
)
l2tHistTunnelTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelTotalSessions.setStatus("mandatory")


class _L2tHistTunnelType_Type(Integer32):
    """Custom type l2tHistTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2fTunnel", 2),
          ("l2tpTunnel", 1),
          ("pptpTunnel", 3))
    )


_L2tHistTunnelType_Type.__name__ = "Integer32"
_L2tHistTunnelType_Object = MibTableColumn
l2tHistTunnelType = _L2tHistTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 10),
    _L2tHistTunnelType_Type()
)
l2tHistTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelType.setStatus("mandatory")
_L2tHistTunnelInOctets_Type = Counter32
_L2tHistTunnelInOctets_Object = MibTableColumn
l2tHistTunnelInOctets = _L2tHistTunnelInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 11),
    _L2tHistTunnelInOctets_Type()
)
l2tHistTunnelInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelInOctets.setStatus("mandatory")
_L2tHistTunnelInPkts_Type = Counter32
_L2tHistTunnelInPkts_Object = MibTableColumn
l2tHistTunnelInPkts = _L2tHistTunnelInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 12),
    _L2tHistTunnelInPkts_Type()
)
l2tHistTunnelInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelInPkts.setStatus("mandatory")
_L2tHistTunnelInDiscards_Type = Counter32
_L2tHistTunnelInDiscards_Object = MibTableColumn
l2tHistTunnelInDiscards = _L2tHistTunnelInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 13),
    _L2tHistTunnelInDiscards_Type()
)
l2tHistTunnelInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelInDiscards.setStatus("mandatory")
_L2tHistTunnelOutOctets_Type = Counter32
_L2tHistTunnelOutOctets_Object = MibTableColumn
l2tHistTunnelOutOctets = _L2tHistTunnelOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 14),
    _L2tHistTunnelOutOctets_Type()
)
l2tHistTunnelOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelOutOctets.setStatus("mandatory")
_L2tHistTunnelOutPkts_Type = Counter32
_L2tHistTunnelOutPkts_Object = MibTableColumn
l2tHistTunnelOutPkts = _L2tHistTunnelOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 15),
    _L2tHistTunnelOutPkts_Type()
)
l2tHistTunnelOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelOutPkts.setStatus("mandatory")
_L2tHistTunnelOutDiscards_Type = Counter32
_L2tHistTunnelOutDiscards_Object = MibTableColumn
l2tHistTunnelOutDiscards = _L2tHistTunnelOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 1, 1, 16),
    _L2tHistTunnelOutDiscards_Type()
)
l2tHistTunnelOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistTunnelOutDiscards.setStatus("mandatory")
_L2tHistSessTable_Object = MibTable
l2tHistSessTable = _L2tHistSessTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2)
)
if mibBuilder.loadTexts:
    l2tHistSessTable.setStatus("mandatory")
_L2tHistSessEntry_Object = MibTableRow
l2tHistSessEntry = _L2tHistSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1)
)
l2tHistSessEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tHistSessIndex"),
)
if mibBuilder.loadTexts:
    l2tHistSessEntry.setStatus("mandatory")


class _L2tHistSessIndex_Type(Integer32):
    """Custom type l2tHistSessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tHistSessIndex_Type.__name__ = "Integer32"
_L2tHistSessIndex_Object = MibTableColumn
l2tHistSessIndex = _L2tHistSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 1),
    _L2tHistSessIndex_Type()
)
l2tHistSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessIndex.setStatus("mandatory")
_L2tHistSessTunnelIndex_Type = Integer32
_L2tHistSessTunnelIndex_Object = MibTableColumn
l2tHistSessTunnelIndex = _L2tHistSessTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 2),
    _L2tHistSessTunnelIndex_Type()
)
l2tHistSessTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessTunnelIndex.setStatus("mandatory")
_L2tHistSessLocalCallId_Type = Integer32
_L2tHistSessLocalCallId_Object = MibTableColumn
l2tHistSessLocalCallId = _L2tHistSessLocalCallId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 3),
    _L2tHistSessLocalCallId_Type()
)
l2tHistSessLocalCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessLocalCallId.setStatus("mandatory")
_L2tHistSessRemoteIpAddress_Type = IpAddress
_L2tHistSessRemoteIpAddress_Object = MibTableColumn
l2tHistSessRemoteIpAddress = _L2tHistSessRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 4),
    _L2tHistSessRemoteIpAddress_Type()
)
l2tHistSessRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessRemoteIpAddress.setStatus("mandatory")
_L2tHistSessLocalIpAddress_Type = IpAddress
_L2tHistSessLocalIpAddress_Object = MibTableColumn
l2tHistSessLocalIpAddress = _L2tHistSessLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 5),
    _L2tHistSessLocalIpAddress_Type()
)
l2tHistSessLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessLocalIpAddress.setStatus("mandatory")
_L2tHistSessUpTime_Type = TimeTicks
_L2tHistSessUpTime_Object = MibTableColumn
l2tHistSessUpTime = _L2tHistSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 6),
    _L2tHistSessUpTime_Type()
)
l2tHistSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessUpTime.setStatus("mandatory")
_L2tHistSessDataRecvOctets_Type = Counter32
_L2tHistSessDataRecvOctets_Object = MibTableColumn
l2tHistSessDataRecvOctets = _L2tHistSessDataRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 7),
    _L2tHistSessDataRecvOctets_Type()
)
l2tHistSessDataRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessDataRecvOctets.setStatus("mandatory")
_L2tHistSessDataRecvPackets_Type = Counter32
_L2tHistSessDataRecvPackets_Object = MibTableColumn
l2tHistSessDataRecvPackets = _L2tHistSessDataRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 8),
    _L2tHistSessDataRecvPackets_Type()
)
l2tHistSessDataRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessDataRecvPackets.setStatus("mandatory")
_L2tHistSessDataRecvDiscards_Type = Counter32
_L2tHistSessDataRecvDiscards_Object = MibTableColumn
l2tHistSessDataRecvDiscards = _L2tHistSessDataRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 9),
    _L2tHistSessDataRecvDiscards_Type()
)
l2tHistSessDataRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessDataRecvDiscards.setStatus("mandatory")
_L2tHistSessDataSendOctets_Type = Counter32
_L2tHistSessDataSendOctets_Object = MibTableColumn
l2tHistSessDataSendOctets = _L2tHistSessDataSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 10),
    _L2tHistSessDataSendOctets_Type()
)
l2tHistSessDataSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessDataSendOctets.setStatus("mandatory")
_L2tHistSessDataSendPackets_Type = Counter32
_L2tHistSessDataSendPackets_Object = MibTableColumn
l2tHistSessDataSendPackets = _L2tHistSessDataSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 11),
    _L2tHistSessDataSendPackets_Type()
)
l2tHistSessDataSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessDataSendPackets.setStatus("mandatory")
_L2tHistSessDataSendDiscards_Type = Counter32
_L2tHistSessDataSendDiscards_Object = MibTableColumn
l2tHistSessDataSendDiscards = _L2tHistSessDataSendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 12),
    _L2tHistSessDataSendDiscards_Type()
)
l2tHistSessDataSendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessDataSendDiscards.setStatus("mandatory")


class _L2tHistSessAuthMethod_Type(Integer32):
    """Custom type l2tHistSessAuthMethod based on Integer32"""
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
        *(("none", 4),
          ("pppchap", 2),
          ("ppppap", 3),
          ("text", 1))
    )


_L2tHistSessAuthMethod_Type.__name__ = "Integer32"
_L2tHistSessAuthMethod_Object = MibTableColumn
l2tHistSessAuthMethod = _L2tHistSessAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 13),
    _L2tHistSessAuthMethod_Type()
)
l2tHistSessAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessAuthMethod.setStatus("mandatory")


class _L2tHistSessEncryptDecrypt_Type(Integer32):
    """Custom type l2tHistSessEncryptDecrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_L2tHistSessEncryptDecrypt_Type.__name__ = "Integer32"
_L2tHistSessEncryptDecrypt_Object = MibTableColumn
l2tHistSessEncryptDecrypt = _L2tHistSessEncryptDecrypt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 5, 2, 1, 14),
    _L2tHistSessEncryptDecrypt_Type()
)
l2tHistSessEncryptDecrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHistSessEncryptDecrypt.setStatus("mandatory")
_L2tHosts_ObjectIdentity = ObjectIdentity
l2tHosts = _L2tHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 6)
)
_L2tHostTable_Object = MibTable
l2tHostTable = _L2tHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 6, 1)
)
if mibBuilder.loadTexts:
    l2tHostTable.setStatus("mandatory")
_L2tHostEntry_Object = MibTableRow
l2tHostEntry = _L2tHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 6, 1, 1)
)
l2tHostEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tHostIndex"),
)
if mibBuilder.loadTexts:
    l2tHostEntry.setStatus("mandatory")


class _L2tHostIndex_Type(Integer32):
    """Custom type l2tHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tHostIndex_Type.__name__ = "Integer32"
_L2tHostIndex_Object = MibTableColumn
l2tHostIndex = _L2tHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 6, 1, 1, 1),
    _L2tHostIndex_Type()
)
l2tHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHostIndex.setStatus("mandatory")
_L2tHostName_Type = DisplayString
_L2tHostName_Object = MibTableColumn
l2tHostName = _L2tHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 6, 1, 1, 2),
    _L2tHostName_Type()
)
l2tHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHostName.setStatus("mandatory")
_L2tHostIpAddress_Type = IpAddress
_L2tHostIpAddress_Object = MibTableColumn
l2tHostIpAddress = _L2tHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 6, 1, 1, 3),
    _L2tHostIpAddress_Type()
)
l2tHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHostIpAddress.setStatus("mandatory")


class _L2tHostTunnelStatus_Type(Integer32):
    """Custom type l2tHostTunnelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_L2tHostTunnelStatus_Type.__name__ = "Integer32"
_L2tHostTunnelStatus_Object = MibTableColumn
l2tHostTunnelStatus = _L2tHostTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 6, 1, 1, 4),
    _L2tHostTunnelStatus_Type()
)
l2tHostTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tHostTunnelStatus.setStatus("mandatory")
_L2tTests_ObjectIdentity = ObjectIdentity
l2tTests = _L2tTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7)
)
_L2tTunnelConnectTestTable_Object = MibTable
l2tTunnelConnectTestTable = _L2tTunnelConnectTestTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 1)
)
if mibBuilder.loadTexts:
    l2tTunnelConnectTestTable.setStatus("mandatory")
_L2tTunnelConnectTestEntry_Object = MibTableRow
l2tTunnelConnectTestEntry = _L2tTunnelConnectTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 1, 1)
)
l2tTunnelConnectTestEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tTunnelConnectTestIndex"),
)
if mibBuilder.loadTexts:
    l2tTunnelConnectTestEntry.setStatus("mandatory")


class _L2tTunnelConnectTestIndex_Type(Integer32):
    """Custom type l2tTunnelConnectTestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tTunnelConnectTestIndex_Type.__name__ = "Integer32"
_L2tTunnelConnectTestIndex_Object = MibTableColumn
l2tTunnelConnectTestIndex = _L2tTunnelConnectTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 1, 1, 1),
    _L2tTunnelConnectTestIndex_Type()
)
l2tTunnelConnectTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelConnectTestIndex.setStatus("mandatory")
_L2tTunnelConnectTestHostName_Type = DisplayString
_L2tTunnelConnectTestHostName_Object = MibTableColumn
l2tTunnelConnectTestHostName = _L2tTunnelConnectTestHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 1, 1, 2),
    _L2tTunnelConnectTestHostName_Type()
)
l2tTunnelConnectTestHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tTunnelConnectTestHostName.setStatus("mandatory")


class _L2tTunnelConnectTestResult_Type(Integer32):
    """Custom type l2tTunnelConnectTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("hostNotResponding", 4),
          ("inProgress", 1),
          ("localAuthFailure", 5),
          ("remoteAuthFailure", 6),
          ("successful", 2),
          ("tunnelAlreadyUp", 3))
    )


_L2tTunnelConnectTestResult_Type.__name__ = "Integer32"
_L2tTunnelConnectTestResult_Object = MibTableColumn
l2tTunnelConnectTestResult = _L2tTunnelConnectTestResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 1, 1, 3),
    _L2tTunnelConnectTestResult_Type()
)
l2tTunnelConnectTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelConnectTestResult.setStatus("mandatory")


class _L2tTunnelConnectTestType_Type(Integer32):
    """Custom type l2tTunnelConnectTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("l2fTunnel", 2),
          ("l2tpTunnel", 1),
          ("none", 99),
          ("pptpTunnel", 3))
    )


_L2tTunnelConnectTestType_Type.__name__ = "Integer32"
_L2tTunnelConnectTestType_Object = MibTableColumn
l2tTunnelConnectTestType = _L2tTunnelConnectTestType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 1, 1, 4),
    _L2tTunnelConnectTestType_Type()
)
l2tTunnelConnectTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelConnectTestType.setStatus("mandatory")


class _L2tTunnelConnectTestStatus_Type(Integer32):
    """Custom type l2tTunnelConnectTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4))
    )


_L2tTunnelConnectTestStatus_Type.__name__ = "Integer32"
_L2tTunnelConnectTestStatus_Object = MibTableColumn
l2tTunnelConnectTestStatus = _L2tTunnelConnectTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 1, 1, 5),
    _L2tTunnelConnectTestStatus_Type()
)
l2tTunnelConnectTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tTunnelConnectTestStatus.setStatus("mandatory")
_L2tTunnelRspTimeTestTable_Object = MibTable
l2tTunnelRspTimeTestTable = _L2tTunnelRspTimeTestTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 2)
)
if mibBuilder.loadTexts:
    l2tTunnelRspTimeTestTable.setStatus("mandatory")
_L2tTunnelRspTimeTestEntry_Object = MibTableRow
l2tTunnelRspTimeTestEntry = _L2tTunnelRspTimeTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 2, 1)
)
l2tTunnelRspTimeTestEntry.setIndexNames(
    (0, "L2TV1-MIB", "l2tTunnelRspTimeTestIndex"),
)
if mibBuilder.loadTexts:
    l2tTunnelRspTimeTestEntry.setStatus("mandatory")


class _L2tTunnelRspTimeTestIndex_Type(Integer32):
    """Custom type l2tTunnelRspTimeTestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tTunnelRspTimeTestIndex_Type.__name__ = "Integer32"
_L2tTunnelRspTimeTestIndex_Object = MibTableColumn
l2tTunnelRspTimeTestIndex = _L2tTunnelRspTimeTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 2, 1, 1),
    _L2tTunnelRspTimeTestIndex_Type()
)
l2tTunnelRspTimeTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelRspTimeTestIndex.setStatus("mandatory")
_L2tTunnelRspTimeTestHostName_Type = DisplayString
_L2tTunnelRspTimeTestHostName_Object = MibTableColumn
l2tTunnelRspTimeTestHostName = _L2tTunnelRspTimeTestHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 2, 1, 2),
    _L2tTunnelRspTimeTestHostName_Type()
)
l2tTunnelRspTimeTestHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tTunnelRspTimeTestHostName.setStatus("mandatory")


class _L2tTunnelRspTimeTestResult_Type(Integer32):
    """Custom type l2tTunnelRspTimeTestResult based on Integer32"""
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
        *(("hostNotResponding", 3),
          ("inProgress", 1),
          ("successful", 2),
          ("tunnelDown", 4))
    )


_L2tTunnelRspTimeTestResult_Type.__name__ = "Integer32"
_L2tTunnelRspTimeTestResult_Object = MibTableColumn
l2tTunnelRspTimeTestResult = _L2tTunnelRspTimeTestResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 2, 1, 3),
    _L2tTunnelRspTimeTestResult_Type()
)
l2tTunnelRspTimeTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelRspTimeTestResult.setStatus("mandatory")
_L2tTunnelRspTimeTestRtripTime_Type = Integer32
_L2tTunnelRspTimeTestRtripTime_Object = MibTableColumn
l2tTunnelRspTimeTestRtripTime = _L2tTunnelRspTimeTestRtripTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 2, 1, 4),
    _L2tTunnelRspTimeTestRtripTime_Type()
)
l2tTunnelRspTimeTestRtripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tTunnelRspTimeTestRtripTime.setStatus("mandatory")


class _L2tTunnelRspTimeTestStatus_Type(Integer32):
    """Custom type l2tTunnelRspTimeTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4))
    )


_L2tTunnelRspTimeTestStatus_Type.__name__ = "Integer32"
_L2tTunnelRspTimeTestStatus_Object = MibTableColumn
l2tTunnelRspTimeTestStatus = _L2tTunnelRspTimeTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 7, 2, 1, 5),
    _L2tTunnelRspTimeTestStatus_Type()
)
l2tTunnelRspTimeTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tTunnelRspTimeTestStatus.setStatus("mandatory")
_L2tTrapCntl_ObjectIdentity = ObjectIdentity
l2tTrapCntl = _L2tTrapCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 8)
)


class _L2tTrapCntlTunnelStart_Type(Integer32):
    """Custom type l2tTrapCntlTunnelStart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_L2tTrapCntlTunnelStart_Type.__name__ = "Integer32"
_L2tTrapCntlTunnelStart_Object = MibScalar
l2tTrapCntlTunnelStart = _L2tTrapCntlTunnelStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 8, 1),
    _L2tTrapCntlTunnelStart_Type()
)
l2tTrapCntlTunnelStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tTrapCntlTunnelStart.setStatus("mandatory")


class _L2tTrapCntlTunnelStop_Type(Integer32):
    """Custom type l2tTrapCntlTunnelStop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_L2tTrapCntlTunnelStop_Type.__name__ = "Integer32"
_L2tTrapCntlTunnelStop_Object = MibScalar
l2tTrapCntlTunnelStop = _L2tTrapCntlTunnelStop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 8, 2),
    _L2tTrapCntlTunnelStop_Type()
)
l2tTrapCntlTunnelStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tTrapCntlTunnelStop.setStatus("mandatory")


class _L2tTrapCntlAuthFailTunnel_Type(Integer32):
    """Custom type l2tTrapCntlAuthFailTunnel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_L2tTrapCntlAuthFailTunnel_Type.__name__ = "Integer32"
_L2tTrapCntlAuthFailTunnel_Object = MibScalar
l2tTrapCntlAuthFailTunnel = _L2tTrapCntlAuthFailTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 8, 3),
    _L2tTrapCntlAuthFailTunnel_Type()
)
l2tTrapCntlAuthFailTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tTrapCntlAuthFailTunnel.setStatus("mandatory")


class _L2tTrapCntlAuthFailUser_Type(Integer32):
    """Custom type l2tTrapCntlAuthFailUser based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_L2tTrapCntlAuthFailUser_Type.__name__ = "Integer32"
_L2tTrapCntlAuthFailUser_Object = MibScalar
l2tTrapCntlAuthFailUser = _L2tTrapCntlAuthFailUser_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 8, 4),
    _L2tTrapCntlAuthFailUser_Type()
)
l2tTrapCntlAuthFailUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tTrapCntlAuthFailUser.setStatus("mandatory")

# Managed Objects groups


# Notification objects

l2tTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 0, 1)
)
l2tTunnelStart.setObjects(
      *(("L2TV1-MIB", "l2tTunnelLocalTunnelControlId"),
        ("L2TV1-MIB", "l2tTunnelType"))
)
if mibBuilder.loadTexts:
    l2tTunnelStart.setStatus(
        ""
    )

l2tTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 0, 2)
)
l2tTunnelStop.setObjects(
      *(("L2TV1-MIB", "l2tTunnelLocalTunnelControlId"),
        ("L2TV1-MIB", "l2tTunnelType"),
        ("L2TV1-MIB", "l2tTunnelUpTime"))
)
if mibBuilder.loadTexts:
    l2tTunnelStop.setStatus(
        ""
    )

l2tAuthFailTunnel = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 0, 3)
)
l2tAuthFailTunnel.setObjects(
      *(("L2TV1-MIB", "l2tAuthFailTunnelHostName"),
        ("L2TV1-MIB", "l2tAuthFailTunnelIpAddress"))
)
if mibBuilder.loadTexts:
    l2tAuthFailTunnel.setStatus(
        ""
    )

l2tAuthFailUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 7, 0, 4)
)
l2tAuthFailUser.setObjects(
    ("L2TV1-MIB", "l2tAuthFailUserId")
)
if mibBuilder.loadTexts:
    l2tAuthFailUser.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "L2TV1-MIB",
    **{"ibmIROCroutingl2t": ibmIROCroutingl2t,
       "l2tTunnelStart": l2tTunnelStart,
       "l2tTunnelStop": l2tTunnelStop,
       "l2tAuthFailTunnel": l2tAuthFailTunnel,
       "l2tAuthFailUser": l2tAuthFailUser,
       "l2tScalar": l2tScalar,
       "l2tScalarConfig": l2tScalarConfig,
       "l2tAdminState": l2tAdminState,
       "l2tAuthenticateIncomingTunnelSetupRequests": l2tAuthenticateIncomingTunnelSetupRequests,
       "l2tTunnelDataFlowControl": l2tTunnelDataFlowControl,
       "l2tControlRecvPacketWindow": l2tControlRecvPacketWindow,
       "l2tDataRecvPacketWindow": l2tDataRecvPacketWindow,
       "l2tHelloTimer": l2tHelloTimer,
       "l2tControlRetransmissions": l2tControlRetransmissions,
       "l2tSecurityExtensions": l2tSecurityExtensions,
       "l2tHistoryWindowSize": l2tHistoryWindowSize,
       "l2tAuthFailWindowSize": l2tAuthFailWindowSize,
       "l2tScalarStat": l2tScalarStat,
       "l2tMibVersion": l2tMibVersion,
       "l2tProtocolVersion": l2tProtocolVersion,
       "l2tNumActiveTunnels": l2tNumActiveTunnels,
       "l2tStatsNumActiveSessions": l2tStatsNumActiveSessions,
       "l2tStats": l2tStats,
       "l2tTunnelStatsTable": l2tTunnelStatsTable,
       "l2tTunnelStatsEntry": l2tTunnelStatsEntry,
       "l2tTunnelLocalTunnelControlId": l2tTunnelLocalTunnelControlId,
       "l2tTunnelPeerTunnelControlId": l2tTunnelPeerTunnelControlId,
       "l2tTunnelControlState": l2tTunnelControlState,
       "l2tTunnelLocalInitConnection": l2tTunnelLocalInitConnection,
       "l2tTunnelLocalRecvPktWindow": l2tTunnelLocalRecvPktWindow,
       "l2tTunnelRemoteRecvPktWindow": l2tTunnelRemoteRecvPktWindow,
       "l2tTunnelCtlTunnelFlwCtlTimeouts": l2tTunnelCtlTunnelFlwCtlTimeouts,
       "l2tTunnelRemoteHostName": l2tTunnelRemoteHostName,
       "l2tTunnelNextSendSeq": l2tTunnelNextSendSeq,
       "l2tTunnelNextRecvSeq": l2tTunnelNextRecvSeq,
       "l2tTunnelRemoteVendorName": l2tTunnelRemoteVendorName,
       "l2tTunnelRemoteFirmwareRevision": l2tTunnelRemoteFirmwareRevision,
       "l2tTunnelRemoteProtocolVersion": l2tTunnelRemoteProtocolVersion,
       "l2tTunnelActiveSessions": l2tTunnelActiveSessions,
       "l2tTunnelPrevSessions": l2tTunnelPrevSessions,
       "l2tTunnelUpTime": l2tTunnelUpTime,
       "l2tTunnelType": l2tTunnelType,
       "l2tTunnelInOctets": l2tTunnelInOctets,
       "l2tTunnelInPkts": l2tTunnelInPkts,
       "l2tTunnelInDiscards": l2tTunnelInDiscards,
       "l2tTunnelOutOctets": l2tTunnelOutOctets,
       "l2tTunnelOutPkts": l2tTunnelOutPkts,
       "l2tTunnelOutDiscards": l2tTunnelOutDiscards,
       "l2tTunnelStatus": l2tTunnelStatus,
       "l2tSessionStatsTable": l2tSessionStatsTable,
       "l2tSessionStatsEntry": l2tSessionStatsEntry,
       "l2tSessionLocalControlTunnelId": l2tSessionLocalControlTunnelId,
       "l2tSessionLocalCallId": l2tSessionLocalCallId,
       "l2tSessionRemoteCallId": l2tSessionRemoteCallId,
       "l2tSessionPeerName": l2tSessionPeerName,
       "l2tSessionLineState": l2tSessionLineState,
       "l2tSessionCallDeviceNumber": l2tSessionCallDeviceNumber,
       "l2tSessionCallSerialNumber": l2tSessionCallSerialNumber,
       "l2tSessionConnectBps": l2tSessionConnectBps,
       "l2tSessionCallBearerType": l2tSessionCallBearerType,
       "l2tSessionFramingType": l2tSessionFramingType,
       "l2tSessionLocalRecvPacketWindow": l2tSessionLocalRecvPacketWindow,
       "l2tSessionRemoteRecvPacketWindow": l2tSessionRemoteRecvPacketWindow,
       "l2tSessionDataRecvOctets": l2tSessionDataRecvOctets,
       "l2tSessionDataRecvDecompOctets": l2tSessionDataRecvDecompOctets,
       "l2tSessionDataRecvPackets": l2tSessionDataRecvPackets,
       "l2tSessionDataRecvDiscards": l2tSessionDataRecvDiscards,
       "l2tSessionDataSendOctets": l2tSessionDataSendOctets,
       "l2tSessionDataSendUncompOctets": l2tSessionDataSendUncompOctets,
       "l2tSessionDataSendPackets": l2tSessionDataSendPackets,
       "l2tSessionDataSendDiscards": l2tSessionDataSendDiscards,
       "l2tSessionDataFlowControlTimeouts": l2tSessionDataFlowControlTimeouts,
       "l2tSessionNextSendSeq": l2tSessionNextSendSeq,
       "l2tSessionNextRecvSeq": l2tSessionNextRecvSeq,
       "l2tSessionRemotePPD": l2tSessionRemotePPD,
       "l2tSessionAuthMethod": l2tSessionAuthMethod,
       "l2tSessionEncryptDecrypt": l2tSessionEncryptDecrypt,
       "l2tSessionUpTime": l2tSessionUpTime,
       "l2tSessionStatus": l2tSessionStatus,
       "l2tUdp": l2tUdp,
       "l2tUdpConfigTable": l2tUdpConfigTable,
       "l2tUdpConfigEntry": l2tUdpConfigEntry,
       "l2tUdpPeerAddress": l2tUdpPeerAddress,
       "l2tUdpPeerPort": l2tUdpPeerPort,
       "l2tUdpStatsTable": l2tUdpStatsTable,
       "l2tUdpStatsEntry": l2tUdpStatsEntry,
       "l2tUdpPeerIpAddress": l2tUdpPeerIpAddress,
       "l2tUdpLocalIpAddress": l2tUdpLocalIpAddress,
       "l2tUdpSrcPort": l2tUdpSrcPort,
       "l2tUdpDstPort": l2tUdpDstPort,
       "l2tAuthentication": l2tAuthentication,
       "l2tAuthStats": l2tAuthStats,
       "l2tAuthTunnelSuccesses": l2tAuthTunnelSuccesses,
       "l2tAuthTunnelFailures": l2tAuthTunnelFailures,
       "l2tAuthUserSuccesses": l2tAuthUserSuccesses,
       "l2tAuthUserFailures": l2tAuthUserFailures,
       "l2tAuthFailures": l2tAuthFailures,
       "l2tAuthFailTunnelTable": l2tAuthFailTunnelTable,
       "l2tAuthFailTunnelEntry": l2tAuthFailTunnelEntry,
       "l2tAuthFailTunnelIndex": l2tAuthFailTunnelIndex,
       "l2tAuthFailTunnelHostName": l2tAuthFailTunnelHostName,
       "l2tAuthFailTunnelIpAddress": l2tAuthFailTunnelIpAddress,
       "l2tAuthFailTunnelTime": l2tAuthFailTunnelTime,
       "l2tAuthFailUserTable": l2tAuthFailUserTable,
       "l2tAuthFailUserEntry": l2tAuthFailUserEntry,
       "l2tAuthFailUserIndex": l2tAuthFailUserIndex,
       "l2tAuthFailUserId": l2tAuthFailUserId,
       "l2tAuthFailUserTime": l2tAuthFailUserTime,
       "l2tHistory": l2tHistory,
       "l2tHistTunnelTable": l2tHistTunnelTable,
       "l2tHistTunnelEntry": l2tHistTunnelEntry,
       "l2tHistTunnelIndex": l2tHistTunnelIndex,
       "l2tHistTunnelTunnelIndex": l2tHistTunnelTunnelIndex,
       "l2tHistTunnelRemoteHostName": l2tHistTunnelRemoteHostName,
       "l2tHistTunnelRemoteIpAddress": l2tHistTunnelRemoteIpAddress,
       "l2tHistTunnelRemotePort": l2tHistTunnelRemotePort,
       "l2tHistTunnelLocalIpAddress": l2tHistTunnelLocalIpAddress,
       "l2tHistTunnelLocalPort": l2tHistTunnelLocalPort,
       "l2tHistTunnelUpTime": l2tHistTunnelUpTime,
       "l2tHistTunnelTotalSessions": l2tHistTunnelTotalSessions,
       "l2tHistTunnelType": l2tHistTunnelType,
       "l2tHistTunnelInOctets": l2tHistTunnelInOctets,
       "l2tHistTunnelInPkts": l2tHistTunnelInPkts,
       "l2tHistTunnelInDiscards": l2tHistTunnelInDiscards,
       "l2tHistTunnelOutOctets": l2tHistTunnelOutOctets,
       "l2tHistTunnelOutPkts": l2tHistTunnelOutPkts,
       "l2tHistTunnelOutDiscards": l2tHistTunnelOutDiscards,
       "l2tHistSessTable": l2tHistSessTable,
       "l2tHistSessEntry": l2tHistSessEntry,
       "l2tHistSessIndex": l2tHistSessIndex,
       "l2tHistSessTunnelIndex": l2tHistSessTunnelIndex,
       "l2tHistSessLocalCallId": l2tHistSessLocalCallId,
       "l2tHistSessRemoteIpAddress": l2tHistSessRemoteIpAddress,
       "l2tHistSessLocalIpAddress": l2tHistSessLocalIpAddress,
       "l2tHistSessUpTime": l2tHistSessUpTime,
       "l2tHistSessDataRecvOctets": l2tHistSessDataRecvOctets,
       "l2tHistSessDataRecvPackets": l2tHistSessDataRecvPackets,
       "l2tHistSessDataRecvDiscards": l2tHistSessDataRecvDiscards,
       "l2tHistSessDataSendOctets": l2tHistSessDataSendOctets,
       "l2tHistSessDataSendPackets": l2tHistSessDataSendPackets,
       "l2tHistSessDataSendDiscards": l2tHistSessDataSendDiscards,
       "l2tHistSessAuthMethod": l2tHistSessAuthMethod,
       "l2tHistSessEncryptDecrypt": l2tHistSessEncryptDecrypt,
       "l2tHosts": l2tHosts,
       "l2tHostTable": l2tHostTable,
       "l2tHostEntry": l2tHostEntry,
       "l2tHostIndex": l2tHostIndex,
       "l2tHostName": l2tHostName,
       "l2tHostIpAddress": l2tHostIpAddress,
       "l2tHostTunnelStatus": l2tHostTunnelStatus,
       "l2tTests": l2tTests,
       "l2tTunnelConnectTestTable": l2tTunnelConnectTestTable,
       "l2tTunnelConnectTestEntry": l2tTunnelConnectTestEntry,
       "l2tTunnelConnectTestIndex": l2tTunnelConnectTestIndex,
       "l2tTunnelConnectTestHostName": l2tTunnelConnectTestHostName,
       "l2tTunnelConnectTestResult": l2tTunnelConnectTestResult,
       "l2tTunnelConnectTestType": l2tTunnelConnectTestType,
       "l2tTunnelConnectTestStatus": l2tTunnelConnectTestStatus,
       "l2tTunnelRspTimeTestTable": l2tTunnelRspTimeTestTable,
       "l2tTunnelRspTimeTestEntry": l2tTunnelRspTimeTestEntry,
       "l2tTunnelRspTimeTestIndex": l2tTunnelRspTimeTestIndex,
       "l2tTunnelRspTimeTestHostName": l2tTunnelRspTimeTestHostName,
       "l2tTunnelRspTimeTestResult": l2tTunnelRspTimeTestResult,
       "l2tTunnelRspTimeTestRtripTime": l2tTunnelRspTimeTestRtripTime,
       "l2tTunnelRspTimeTestStatus": l2tTunnelRspTimeTestStatus,
       "l2tTrapCntl": l2tTrapCntl,
       "l2tTrapCntlTunnelStart": l2tTrapCntlTunnelStart,
       "l2tTrapCntlTunnelStop": l2tTrapCntlTunnelStop,
       "l2tTrapCntlAuthFailTunnel": l2tTrapCntlAuthFailTunnel,
       "l2tTrapCntlAuthFailUser": l2tTrapCntlAuthFailUser}
)
