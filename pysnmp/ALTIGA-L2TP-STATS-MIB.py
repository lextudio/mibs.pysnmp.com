# SNMP MIB module (ALTIGA-L2TP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-L2TP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:14 2024
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

(alL2tpMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alL2tpMibModule")

(alL2tpGroup,
 alStatsL2tp) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alL2tpGroup",
    "alStatsL2tp")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

altigaL2tpStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 21, 2)
)
altigaL2tpStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaL2tpStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaL2tpStatsMibConformance = _AltigaL2tpStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 21, 2, 1)
)
_AltigaL2tpStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaL2tpStatsMibCompliances = _AltigaL2tpStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 21, 2, 1, 1)
)
_AlStatsL2tpGlobal_ObjectIdentity = ObjectIdentity
alStatsL2tpGlobal = _AlStatsL2tpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1)
)


class _AlL2tpStatsLocalProtVers_Type(OctetString):
    """Custom type alL2tpStatsLocalProtVers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlL2tpStatsLocalProtVers_Type.__name__ = "OctetString"
_AlL2tpStatsLocalProtVers_Object = MibScalar
alL2tpStatsLocalProtVers = _AlL2tpStatsLocalProtVers_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 1),
    _AlL2tpStatsLocalProtVers_Type()
)
alL2tpStatsLocalProtVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsLocalProtVers.setStatus("current")
_AlL2tpStatsVendorName_Type = DisplayString
_AlL2tpStatsVendorName_Object = MibScalar
alL2tpStatsVendorName = _AlL2tpStatsVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 2),
    _AlL2tpStatsVendorName_Type()
)
alL2tpStatsVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsVendorName.setStatus("current")


class _AlL2tpStatsFirmwareRev_Type(OctetString):
    """Custom type alL2tpStatsFirmwareRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlL2tpStatsFirmwareRev_Type.__name__ = "OctetString"
_AlL2tpStatsFirmwareRev_Object = MibScalar
alL2tpStatsFirmwareRev = _AlL2tpStatsFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 3),
    _AlL2tpStatsFirmwareRev_Type()
)
alL2tpStatsFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsFirmwareRev.setStatus("current")
_AlL2tpStatsTotalTunnels_Type = Counter32
_AlL2tpStatsTotalTunnels_Object = MibScalar
alL2tpStatsTotalTunnels = _AlL2tpStatsTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 4),
    _AlL2tpStatsTotalTunnels_Type()
)
alL2tpStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTotalTunnels.setStatus("current")
_AlL2tpStatsFailedTunnels_Type = Counter32
_AlL2tpStatsFailedTunnels_Object = MibScalar
alL2tpStatsFailedTunnels = _AlL2tpStatsFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 5),
    _AlL2tpStatsFailedTunnels_Type()
)
alL2tpStatsFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsFailedTunnels.setStatus("current")
_AlL2tpStatsFailedAuthentications_Type = Counter32
_AlL2tpStatsFailedAuthentications_Object = MibScalar
alL2tpStatsFailedAuthentications = _AlL2tpStatsFailedAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 6),
    _AlL2tpStatsFailedAuthentications_Type()
)
alL2tpStatsFailedAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsFailedAuthentications.setStatus("current")
_AlL2tpStatsActiveTunnels_Type = Gauge32
_AlL2tpStatsActiveTunnels_Object = MibScalar
alL2tpStatsActiveTunnels = _AlL2tpStatsActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 7),
    _AlL2tpStatsActiveTunnels_Type()
)
alL2tpStatsActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsActiveTunnels.setStatus("current")
_AlL2tpStatsMaxTunnels_Type = Gauge32
_AlL2tpStatsMaxTunnels_Object = MibScalar
alL2tpStatsMaxTunnels = _AlL2tpStatsMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 8),
    _AlL2tpStatsMaxTunnels_Type()
)
alL2tpStatsMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsMaxTunnels.setStatus("current")
_AlL2tpStatsTotalSessions_Type = Counter32
_AlL2tpStatsTotalSessions_Object = MibScalar
alL2tpStatsTotalSessions = _AlL2tpStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 9),
    _AlL2tpStatsTotalSessions_Type()
)
alL2tpStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTotalSessions.setStatus("current")
_AlL2tpStatsFailedSessions_Type = Counter32
_AlL2tpStatsFailedSessions_Object = MibScalar
alL2tpStatsFailedSessions = _AlL2tpStatsFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 10),
    _AlL2tpStatsFailedSessions_Type()
)
alL2tpStatsFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsFailedSessions.setStatus("current")
_AlL2tpStatsActiveSessions_Type = Gauge32
_AlL2tpStatsActiveSessions_Object = MibScalar
alL2tpStatsActiveSessions = _AlL2tpStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 11),
    _AlL2tpStatsActiveSessions_Type()
)
alL2tpStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsActiveSessions.setStatus("current")
_AlL2tpStatsMaxSessions_Type = Gauge32
_AlL2tpStatsMaxSessions_Object = MibScalar
alL2tpStatsMaxSessions = _AlL2tpStatsMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 12),
    _AlL2tpStatsMaxSessions_Type()
)
alL2tpStatsMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsMaxSessions.setStatus("current")
_AlL2tpStatsControlRecvOctets_Type = Counter32
_AlL2tpStatsControlRecvOctets_Object = MibScalar
alL2tpStatsControlRecvOctets = _AlL2tpStatsControlRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 13),
    _AlL2tpStatsControlRecvOctets_Type()
)
alL2tpStatsControlRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsControlRecvOctets.setStatus("current")
_AlL2tpStatsControlRecvPackets_Type = Counter32
_AlL2tpStatsControlRecvPackets_Object = MibScalar
alL2tpStatsControlRecvPackets = _AlL2tpStatsControlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 14),
    _AlL2tpStatsControlRecvPackets_Type()
)
alL2tpStatsControlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsControlRecvPackets.setStatus("current")
_AlL2tpStatsControlRecvDiscards_Type = Counter32
_AlL2tpStatsControlRecvDiscards_Object = MibScalar
alL2tpStatsControlRecvDiscards = _AlL2tpStatsControlRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 15),
    _AlL2tpStatsControlRecvDiscards_Type()
)
alL2tpStatsControlRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsControlRecvDiscards.setStatus("current")
_AlL2tpStatsControlSendOctets_Type = Counter32
_AlL2tpStatsControlSendOctets_Object = MibScalar
alL2tpStatsControlSendOctets = _AlL2tpStatsControlSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 16),
    _AlL2tpStatsControlSendOctets_Type()
)
alL2tpStatsControlSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsControlSendOctets.setStatus("current")
_AlL2tpStatsControlSendPackets_Type = Counter32
_AlL2tpStatsControlSendPackets_Object = MibScalar
alL2tpStatsControlSendPackets = _AlL2tpStatsControlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 17),
    _AlL2tpStatsControlSendPackets_Type()
)
alL2tpStatsControlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsControlSendPackets.setStatus("current")
_AlL2tpStatsPayloadRecvOctets_Type = Counter32
_AlL2tpStatsPayloadRecvOctets_Object = MibScalar
alL2tpStatsPayloadRecvOctets = _AlL2tpStatsPayloadRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 18),
    _AlL2tpStatsPayloadRecvOctets_Type()
)
alL2tpStatsPayloadRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsPayloadRecvOctets.setStatus("current")
_AlL2tpStatsPayloadRecvPackets_Type = Counter32
_AlL2tpStatsPayloadRecvPackets_Object = MibScalar
alL2tpStatsPayloadRecvPackets = _AlL2tpStatsPayloadRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 19),
    _AlL2tpStatsPayloadRecvPackets_Type()
)
alL2tpStatsPayloadRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsPayloadRecvPackets.setStatus("current")
_AlL2tpStatsPayloadRecvDiscards_Type = Counter32
_AlL2tpStatsPayloadRecvDiscards_Object = MibScalar
alL2tpStatsPayloadRecvDiscards = _AlL2tpStatsPayloadRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 20),
    _AlL2tpStatsPayloadRecvDiscards_Type()
)
alL2tpStatsPayloadRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsPayloadRecvDiscards.setStatus("current")
_AlL2tpStatsPayloadSendOctets_Type = Counter32
_AlL2tpStatsPayloadSendOctets_Object = MibScalar
alL2tpStatsPayloadSendOctets = _AlL2tpStatsPayloadSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 21),
    _AlL2tpStatsPayloadSendOctets_Type()
)
alL2tpStatsPayloadSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsPayloadSendOctets.setStatus("current")
_AlL2tpStatsPayloadSendPackets_Type = Counter32
_AlL2tpStatsPayloadSendPackets_Object = MibScalar
alL2tpStatsPayloadSendPackets = _AlL2tpStatsPayloadSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 1, 22),
    _AlL2tpStatsPayloadSendPackets_Type()
)
alL2tpStatsPayloadSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsPayloadSendPackets.setStatus("current")
_AlL2tpStatsTunnelTable_Object = MibTable
alL2tpStatsTunnelTable = _AlL2tpStatsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2)
)
if mibBuilder.loadTexts:
    alL2tpStatsTunnelTable.setStatus("current")
_AlL2tpStatsTunnelEntry_Object = MibTableRow
alL2tpStatsTunnelEntry = _AlL2tpStatsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1)
)
alL2tpStatsTunnelEntry.setIndexNames(
    (0, "ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelPeerIpAddr"),
)
if mibBuilder.loadTexts:
    alL2tpStatsTunnelEntry.setStatus("current")
_AlL2tpStatsTunnelRowStatus_Type = RowStatus
_AlL2tpStatsTunnelRowStatus_Object = MibTableColumn
alL2tpStatsTunnelRowStatus = _AlL2tpStatsTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 1),
    _AlL2tpStatsTunnelRowStatus_Type()
)
alL2tpStatsTunnelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelRowStatus.setStatus("current")
_AlL2tpStatsTunnelPeerIpAddr_Type = IpAddress
_AlL2tpStatsTunnelPeerIpAddr_Object = MibTableColumn
alL2tpStatsTunnelPeerIpAddr = _AlL2tpStatsTunnelPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 2),
    _AlL2tpStatsTunnelPeerIpAddr_Type()
)
alL2tpStatsTunnelPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelPeerIpAddr.setStatus("current")


class _AlL2tpStatsTunnelLocalTID_Type(Integer32):
    """Custom type alL2tpStatsTunnelLocalTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsTunnelLocalTID_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelLocalTID_Object = MibTableColumn
alL2tpStatsTunnelLocalTID = _AlL2tpStatsTunnelLocalTID_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 3),
    _AlL2tpStatsTunnelLocalTID_Type()
)
alL2tpStatsTunnelLocalTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelLocalTID.setStatus("current")


class _AlL2tpStatsTunnelRemoteTID_Type(Integer32):
    """Custom type alL2tpStatsTunnelRemoteTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsTunnelRemoteTID_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelRemoteTID_Object = MibTableColumn
alL2tpStatsTunnelRemoteTID = _AlL2tpStatsTunnelRemoteTID_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 4),
    _AlL2tpStatsTunnelRemoteTID_Type()
)
alL2tpStatsTunnelRemoteTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelRemoteTID.setStatus("current")


class _AlL2tpStatsTunnelState_Type(Integer32):
    """Custom type alL2tpStatsTunnelState based on Integer32"""
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
        *(("tunnelConnecting", 2),
          ("tunnelDisconnecting", 4),
          ("tunnelEstablished", 3),
          ("tunnelIdle", 1))
    )


_AlL2tpStatsTunnelState_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelState_Object = MibTableColumn
alL2tpStatsTunnelState = _AlL2tpStatsTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 5),
    _AlL2tpStatsTunnelState_Type()
)
alL2tpStatsTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelState.setStatus("current")


class _AlL2tpStatsTunnelInitiated_Type(Integer32):
    """Custom type alL2tpStatsTunnelInitiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locally", 1),
          ("remotely", 2))
    )


_AlL2tpStatsTunnelInitiated_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelInitiated_Object = MibTableColumn
alL2tpStatsTunnelInitiated = _AlL2tpStatsTunnelInitiated_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 6),
    _AlL2tpStatsTunnelInitiated_Type()
)
alL2tpStatsTunnelInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelInitiated.setStatus("current")
_AlL2tpStatsTunnelRemoteHostName_Type = DisplayString
_AlL2tpStatsTunnelRemoteHostName_Object = MibTableColumn
alL2tpStatsTunnelRemoteHostName = _AlL2tpStatsTunnelRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 7),
    _AlL2tpStatsTunnelRemoteHostName_Type()
)
alL2tpStatsTunnelRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelRemoteHostName.setStatus("current")
_AlL2tpStatsTunnelRemoteVendorName_Type = DisplayString
_AlL2tpStatsTunnelRemoteVendorName_Object = MibTableColumn
alL2tpStatsTunnelRemoteVendorName = _AlL2tpStatsTunnelRemoteVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 8),
    _AlL2tpStatsTunnelRemoteVendorName_Type()
)
alL2tpStatsTunnelRemoteVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelRemoteVendorName.setStatus("current")


class _AlL2tpStatsTunnelRemoteFirmwareRevision_Type(OctetString):
    """Custom type alL2tpStatsTunnelRemoteFirmwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlL2tpStatsTunnelRemoteFirmwareRevision_Type.__name__ = "OctetString"
_AlL2tpStatsTunnelRemoteFirmwareRevision_Object = MibTableColumn
alL2tpStatsTunnelRemoteFirmwareRevision = _AlL2tpStatsTunnelRemoteFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 9),
    _AlL2tpStatsTunnelRemoteFirmwareRevision_Type()
)
alL2tpStatsTunnelRemoteFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelRemoteFirmwareRevision.setStatus("current")


class _AlL2tpStatsTunnelRemoteProtocolVersion_Type(OctetString):
    """Custom type alL2tpStatsTunnelRemoteProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlL2tpStatsTunnelRemoteProtocolVersion_Type.__name__ = "OctetString"
_AlL2tpStatsTunnelRemoteProtocolVersion_Object = MibTableColumn
alL2tpStatsTunnelRemoteProtocolVersion = _AlL2tpStatsTunnelRemoteProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 10),
    _AlL2tpStatsTunnelRemoteProtocolVersion_Type()
)
alL2tpStatsTunnelRemoteProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelRemoteProtocolVersion.setStatus("current")


class _AlL2tpStatsTunnelInitialRemoteRWS_Type(Integer32):
    """Custom type alL2tpStatsTunnelInitialRemoteRWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsTunnelInitialRemoteRWS_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelInitialRemoteRWS_Object = MibTableColumn
alL2tpStatsTunnelInitialRemoteRWS = _AlL2tpStatsTunnelInitialRemoteRWS_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 11),
    _AlL2tpStatsTunnelInitialRemoteRWS_Type()
)
alL2tpStatsTunnelInitialRemoteRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelInitialRemoteRWS.setStatus("current")


class _AlL2tpStatsTunnelBearerCapabilities_Type(Integer32):
    """Custom type alL2tpStatsTunnelBearerCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("sync", 1),
          ("syncAsync", 3))
    )


_AlL2tpStatsTunnelBearerCapabilities_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelBearerCapabilities_Object = MibTableColumn
alL2tpStatsTunnelBearerCapabilities = _AlL2tpStatsTunnelBearerCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 12),
    _AlL2tpStatsTunnelBearerCapabilities_Type()
)
alL2tpStatsTunnelBearerCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelBearerCapabilities.setStatus("current")


class _AlL2tpStatsTunnelFramingCapabilities_Type(Integer32):
    """Custom type alL2tpStatsTunnelFramingCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("digital", 1),
          ("digitalAnalog", 3))
    )


_AlL2tpStatsTunnelFramingCapabilities_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelFramingCapabilities_Object = MibTableColumn
alL2tpStatsTunnelFramingCapabilities = _AlL2tpStatsTunnelFramingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 13),
    _AlL2tpStatsTunnelFramingCapabilities_Type()
)
alL2tpStatsTunnelFramingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelFramingCapabilities.setStatus("current")
_AlL2tpStatsTunnelControlRecvPackets_Type = Counter32
_AlL2tpStatsTunnelControlRecvPackets_Object = MibTableColumn
alL2tpStatsTunnelControlRecvPackets = _AlL2tpStatsTunnelControlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 14),
    _AlL2tpStatsTunnelControlRecvPackets_Type()
)
alL2tpStatsTunnelControlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelControlRecvPackets.setStatus("current")
_AlL2tpStatsTunnelControlRecvDiscards_Type = Counter32
_AlL2tpStatsTunnelControlRecvDiscards_Object = MibTableColumn
alL2tpStatsTunnelControlRecvDiscards = _AlL2tpStatsTunnelControlRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 15),
    _AlL2tpStatsTunnelControlRecvDiscards_Type()
)
alL2tpStatsTunnelControlRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelControlRecvDiscards.setStatus("current")
_AlL2tpStatsTunnelControlRecvZLB_Type = Counter32
_AlL2tpStatsTunnelControlRecvZLB_Object = MibTableColumn
alL2tpStatsTunnelControlRecvZLB = _AlL2tpStatsTunnelControlRecvZLB_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 16),
    _AlL2tpStatsTunnelControlRecvZLB_Type()
)
alL2tpStatsTunnelControlRecvZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelControlRecvZLB.setStatus("current")
_AlL2tpStatsTunnelControlOutOfSequence_Type = Counter32
_AlL2tpStatsTunnelControlOutOfSequence_Object = MibTableColumn
alL2tpStatsTunnelControlOutOfSequence = _AlL2tpStatsTunnelControlOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 17),
    _AlL2tpStatsTunnelControlOutOfSequence_Type()
)
alL2tpStatsTunnelControlOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelControlOutOfSequence.setStatus("current")
_AlL2tpStatsTunnelControlOutOfWindow_Type = Counter32
_AlL2tpStatsTunnelControlOutOfWindow_Object = MibTableColumn
alL2tpStatsTunnelControlOutOfWindow = _AlL2tpStatsTunnelControlOutOfWindow_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 18),
    _AlL2tpStatsTunnelControlOutOfWindow_Type()
)
alL2tpStatsTunnelControlOutOfWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelControlOutOfWindow.setStatus("current")
_AlL2tpStatsTunnelControlSendPackets_Type = Counter32
_AlL2tpStatsTunnelControlSendPackets_Object = MibTableColumn
alL2tpStatsTunnelControlSendPackets = _AlL2tpStatsTunnelControlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 19),
    _AlL2tpStatsTunnelControlSendPackets_Type()
)
alL2tpStatsTunnelControlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelControlSendPackets.setStatus("current")
_AlL2tpStatsTunnelControlSendZLB_Type = Counter32
_AlL2tpStatsTunnelControlSendZLB_Object = MibTableColumn
alL2tpStatsTunnelControlSendZLB = _AlL2tpStatsTunnelControlSendZLB_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 20),
    _AlL2tpStatsTunnelControlSendZLB_Type()
)
alL2tpStatsTunnelControlSendZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelControlSendZLB.setStatus("current")
_AlL2tpStatsTunnelControlAckTimeouts_Type = Counter32
_AlL2tpStatsTunnelControlAckTimeouts_Object = MibTableColumn
alL2tpStatsTunnelControlAckTimeouts = _AlL2tpStatsTunnelControlAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 21),
    _AlL2tpStatsTunnelControlAckTimeouts_Type()
)
alL2tpStatsTunnelControlAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelControlAckTimeouts.setStatus("current")


class _AlL2tpStatsTunnelCurrentRemoteRWS_Type(Gauge32):
    """Custom type alL2tpStatsTunnelCurrentRemoteRWS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AlL2tpStatsTunnelCurrentRemoteRWS_Type.__name__ = "Gauge32"
_AlL2tpStatsTunnelCurrentRemoteRWS_Object = MibTableColumn
alL2tpStatsTunnelCurrentRemoteRWS = _AlL2tpStatsTunnelCurrentRemoteRWS_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 22),
    _AlL2tpStatsTunnelCurrentRemoteRWS_Type()
)
alL2tpStatsTunnelCurrentRemoteRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelCurrentRemoteRWS.setStatus("current")


class _AlL2tpStatsTunnelSendSeq_Type(Integer32):
    """Custom type alL2tpStatsTunnelSendSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsTunnelSendSeq_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelSendSeq_Object = MibTableColumn
alL2tpStatsTunnelSendSeq = _AlL2tpStatsTunnelSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 23),
    _AlL2tpStatsTunnelSendSeq_Type()
)
alL2tpStatsTunnelSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelSendSeq.setStatus("current")


class _AlL2tpStatsTunnelSendSeqAck_Type(Integer32):
    """Custom type alL2tpStatsTunnelSendSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsTunnelSendSeqAck_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelSendSeqAck_Object = MibTableColumn
alL2tpStatsTunnelSendSeqAck = _AlL2tpStatsTunnelSendSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 24),
    _AlL2tpStatsTunnelSendSeqAck_Type()
)
alL2tpStatsTunnelSendSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelSendSeqAck.setStatus("current")


class _AlL2tpStatsTunnelRecvSeq_Type(Integer32):
    """Custom type alL2tpStatsTunnelRecvSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsTunnelRecvSeq_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelRecvSeq_Object = MibTableColumn
alL2tpStatsTunnelRecvSeq = _AlL2tpStatsTunnelRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 25),
    _AlL2tpStatsTunnelRecvSeq_Type()
)
alL2tpStatsTunnelRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelRecvSeq.setStatus("current")


class _AlL2tpStatsTunnelRecvSeqAck_Type(Integer32):
    """Custom type alL2tpStatsTunnelRecvSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsTunnelRecvSeqAck_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelRecvSeqAck_Object = MibTableColumn
alL2tpStatsTunnelRecvSeqAck = _AlL2tpStatsTunnelRecvSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 26),
    _AlL2tpStatsTunnelRecvSeqAck_Type()
)
alL2tpStatsTunnelRecvSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelRecvSeqAck.setStatus("current")
_AlL2tpStatsTunnelTotalSessions_Type = Counter32
_AlL2tpStatsTunnelTotalSessions_Object = MibTableColumn
alL2tpStatsTunnelTotalSessions = _AlL2tpStatsTunnelTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 27),
    _AlL2tpStatsTunnelTotalSessions_Type()
)
alL2tpStatsTunnelTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelTotalSessions.setStatus("current")
_AlL2tpStatsTunnelFailedSessions_Type = Counter32
_AlL2tpStatsTunnelFailedSessions_Object = MibTableColumn
alL2tpStatsTunnelFailedSessions = _AlL2tpStatsTunnelFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 28),
    _AlL2tpStatsTunnelFailedSessions_Type()
)
alL2tpStatsTunnelFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelFailedSessions.setStatus("current")
_AlL2tpStatsTunnelActiveSessions_Type = Gauge32
_AlL2tpStatsTunnelActiveSessions_Object = MibTableColumn
alL2tpStatsTunnelActiveSessions = _AlL2tpStatsTunnelActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 29),
    _AlL2tpStatsTunnelActiveSessions_Type()
)
alL2tpStatsTunnelActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelActiveSessions.setStatus("current")


class _AlL2tpStatsTunnelLastResultCode_Type(Integer32):
    """Custom type alL2tpStatsTunnelLastResultCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsTunnelLastResultCode_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelLastResultCode_Object = MibTableColumn
alL2tpStatsTunnelLastResultCode = _AlL2tpStatsTunnelLastResultCode_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 30),
    _AlL2tpStatsTunnelLastResultCode_Type()
)
alL2tpStatsTunnelLastResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelLastResultCode.setStatus("current")


class _AlL2tpStatsTunnelLastErrorCode_Type(Integer32):
    """Custom type alL2tpStatsTunnelLastErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsTunnelLastErrorCode_Type.__name__ = "Integer32"
_AlL2tpStatsTunnelLastErrorCode_Object = MibTableColumn
alL2tpStatsTunnelLastErrorCode = _AlL2tpStatsTunnelLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 31),
    _AlL2tpStatsTunnelLastErrorCode_Type()
)
alL2tpStatsTunnelLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelLastErrorCode.setStatus("current")
_AlL2tpStatsTunnelLastErrorMessage_Type = DisplayString
_AlL2tpStatsTunnelLastErrorMessage_Object = MibTableColumn
alL2tpStatsTunnelLastErrorMessage = _AlL2tpStatsTunnelLastErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 2, 1, 32),
    _AlL2tpStatsTunnelLastErrorMessage_Type()
)
alL2tpStatsTunnelLastErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsTunnelLastErrorMessage.setStatus("current")
_AlL2tpStatsSessionTable_Object = MibTable
alL2tpStatsSessionTable = _AlL2tpStatsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3)
)
if mibBuilder.loadTexts:
    alL2tpStatsSessionTable.setStatus("current")
_AlL2tpStatsSessionEntry_Object = MibTableRow
alL2tpStatsSessionEntry = _AlL2tpStatsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1)
)
alL2tpStatsSessionEntry.setIndexNames(
    (0, "ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionIfIndex"),
)
if mibBuilder.loadTexts:
    alL2tpStatsSessionEntry.setStatus("current")
_AlL2tpStatsSessionRowStatus_Type = RowStatus
_AlL2tpStatsSessionRowStatus_Object = MibTableColumn
alL2tpStatsSessionRowStatus = _AlL2tpStatsSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 1),
    _AlL2tpStatsSessionRowStatus_Type()
)
alL2tpStatsSessionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRowStatus.setStatus("current")
_AlL2tpStatsSessionIfIndex_Type = InterfaceIndex
_AlL2tpStatsSessionIfIndex_Object = MibTableColumn
alL2tpStatsSessionIfIndex = _AlL2tpStatsSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 2),
    _AlL2tpStatsSessionIfIndex_Type()
)
alL2tpStatsSessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionIfIndex.setStatus("current")


class _AlL2tpStatsSessionTID_Type(Integer32):
    """Custom type alL2tpStatsSessionTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsSessionTID_Type.__name__ = "Integer32"
_AlL2tpStatsSessionTID_Object = MibTableColumn
alL2tpStatsSessionTID = _AlL2tpStatsSessionTID_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 3),
    _AlL2tpStatsSessionTID_Type()
)
alL2tpStatsSessionTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionTID.setStatus("current")


class _AlL2tpStatsSessionLocalCID_Type(Integer32):
    """Custom type alL2tpStatsSessionLocalCID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsSessionLocalCID_Type.__name__ = "Integer32"
_AlL2tpStatsSessionLocalCID_Object = MibTableColumn
alL2tpStatsSessionLocalCID = _AlL2tpStatsSessionLocalCID_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 4),
    _AlL2tpStatsSessionLocalCID_Type()
)
alL2tpStatsSessionLocalCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionLocalCID.setStatus("current")


class _AlL2tpStatsSessionRemoteCID_Type(Integer32):
    """Custom type alL2tpStatsSessionRemoteCID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsSessionRemoteCID_Type.__name__ = "Integer32"
_AlL2tpStatsSessionRemoteCID_Object = MibTableColumn
alL2tpStatsSessionRemoteCID = _AlL2tpStatsSessionRemoteCID_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 5),
    _AlL2tpStatsSessionRemoteCID_Type()
)
alL2tpStatsSessionRemoteCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRemoteCID.setStatus("current")
_AlL2tpStatsSessionUserName_Type = DisplayString
_AlL2tpStatsSessionUserName_Object = MibTableColumn
alL2tpStatsSessionUserName = _AlL2tpStatsSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 6),
    _AlL2tpStatsSessionUserName_Type()
)
alL2tpStatsSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionUserName.setStatus("current")


class _AlL2tpStatsSessionState_Type(Integer32):
    """Custom type alL2tpStatsSessionState based on Integer32"""
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
        *(("sessionConnecting", 2),
          ("sessionDisconnecting", 4),
          ("sessionEstablished", 3),
          ("sessionIdle", 1))
    )


_AlL2tpStatsSessionState_Type.__name__ = "Integer32"
_AlL2tpStatsSessionState_Object = MibTableColumn
alL2tpStatsSessionState = _AlL2tpStatsSessionState_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 7),
    _AlL2tpStatsSessionState_Type()
)
alL2tpStatsSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionState.setStatus("current")


class _AlL2tpStatsSessionCallType_Type(Integer32):
    """Custom type alL2tpStatsSessionCallType based on Integer32"""
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
        *(("lacIncoming", 1),
          ("lacOutgoing", 3),
          ("lnsIncoming", 2),
          ("lnsOutgoing", 4))
    )


_AlL2tpStatsSessionCallType_Type.__name__ = "Integer32"
_AlL2tpStatsSessionCallType_Object = MibTableColumn
alL2tpStatsSessionCallType = _AlL2tpStatsSessionCallType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 8),
    _AlL2tpStatsSessionCallType_Type()
)
alL2tpStatsSessionCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionCallType.setStatus("current")
_AlL2tpStatsSessionCallSerialNumber_Type = Unsigned32
_AlL2tpStatsSessionCallSerialNumber_Object = MibTableColumn
alL2tpStatsSessionCallSerialNumber = _AlL2tpStatsSessionCallSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 9),
    _AlL2tpStatsSessionCallSerialNumber_Type()
)
alL2tpStatsSessionCallSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionCallSerialNumber.setStatus("current")
_AlL2tpStatsSessionTxConnectSpeed_Type = Integer32
_AlL2tpStatsSessionTxConnectSpeed_Object = MibTableColumn
alL2tpStatsSessionTxConnectSpeed = _AlL2tpStatsSessionTxConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 10),
    _AlL2tpStatsSessionTxConnectSpeed_Type()
)
alL2tpStatsSessionTxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionTxConnectSpeed.setStatus("current")
_AlL2tpStatsSessionRxConnectSpeed_Type = Integer32
_AlL2tpStatsSessionRxConnectSpeed_Object = MibTableColumn
alL2tpStatsSessionRxConnectSpeed = _AlL2tpStatsSessionRxConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 11),
    _AlL2tpStatsSessionRxConnectSpeed_Type()
)
alL2tpStatsSessionRxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRxConnectSpeed.setStatus("current")


class _AlL2tpStatsSessionCallBearerType_Type(Integer32):
    """Custom type alL2tpStatsSessionCallBearerType based on Integer32"""
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


_AlL2tpStatsSessionCallBearerType_Type.__name__ = "Integer32"
_AlL2tpStatsSessionCallBearerType_Object = MibTableColumn
alL2tpStatsSessionCallBearerType = _AlL2tpStatsSessionCallBearerType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 12),
    _AlL2tpStatsSessionCallBearerType_Type()
)
alL2tpStatsSessionCallBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionCallBearerType.setStatus("current")


class _AlL2tpStatsSessionFramingType_Type(Integer32):
    """Custom type alL2tpStatsSessionFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("synchronous", 2))
    )


_AlL2tpStatsSessionFramingType_Type.__name__ = "Integer32"
_AlL2tpStatsSessionFramingType_Object = MibTableColumn
alL2tpStatsSessionFramingType = _AlL2tpStatsSessionFramingType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 13),
    _AlL2tpStatsSessionFramingType_Type()
)
alL2tpStatsSessionFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionFramingType.setStatus("current")
_AlL2tpStatsSessionPhysChanId_Type = Integer32
_AlL2tpStatsSessionPhysChanId_Object = MibTableColumn
alL2tpStatsSessionPhysChanId = _AlL2tpStatsSessionPhysChanId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 14),
    _AlL2tpStatsSessionPhysChanId_Type()
)
alL2tpStatsSessionPhysChanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionPhysChanId.setStatus("current")
_AlL2tpStatsSessionDNIS_Type = DisplayString
_AlL2tpStatsSessionDNIS_Object = MibTableColumn
alL2tpStatsSessionDNIS = _AlL2tpStatsSessionDNIS_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 15),
    _AlL2tpStatsSessionDNIS_Type()
)
alL2tpStatsSessionDNIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionDNIS.setStatus("current")
_AlL2tpStatsSessionCLID_Type = DisplayString
_AlL2tpStatsSessionCLID_Object = MibTableColumn
alL2tpStatsSessionCLID = _AlL2tpStatsSessionCLID_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 16),
    _AlL2tpStatsSessionCLID_Type()
)
alL2tpStatsSessionCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionCLID.setStatus("current")
_AlL2tpStatsSessionSubAddress_Type = DisplayString
_AlL2tpStatsSessionSubAddress_Object = MibTableColumn
alL2tpStatsSessionSubAddress = _AlL2tpStatsSessionSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 17),
    _AlL2tpStatsSessionSubAddress_Type()
)
alL2tpStatsSessionSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionSubAddress.setStatus("current")
_AlL2tpStatsSessionPrivateGroupID_Type = DisplayString
_AlL2tpStatsSessionPrivateGroupID_Object = MibTableColumn
alL2tpStatsSessionPrivateGroupID = _AlL2tpStatsSessionPrivateGroupID_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 18),
    _AlL2tpStatsSessionPrivateGroupID_Type()
)
alL2tpStatsSessionPrivateGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionPrivateGroupID.setStatus("current")
_AlL2tpStatsSessionProxyLcp_Type = TruthValue
_AlL2tpStatsSessionProxyLcp_Object = MibTableColumn
alL2tpStatsSessionProxyLcp = _AlL2tpStatsSessionProxyLcp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 19),
    _AlL2tpStatsSessionProxyLcp_Type()
)
alL2tpStatsSessionProxyLcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionProxyLcp.setStatus("current")


class _AlL2tpStatsSessionAuthMethod_Type(Integer32):
    """Custom type alL2tpStatsSessionAuthMethod based on Integer32"""
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
        *(("none", 1),
          ("pppChap", 3),
          ("pppPap", 4),
          ("text", 2))
    )


_AlL2tpStatsSessionAuthMethod_Type.__name__ = "Integer32"
_AlL2tpStatsSessionAuthMethod_Object = MibTableColumn
alL2tpStatsSessionAuthMethod = _AlL2tpStatsSessionAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 20),
    _AlL2tpStatsSessionAuthMethod_Type()
)
alL2tpStatsSessionAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionAuthMethod.setStatus("current")


class _AlL2tpStatsSessionLocalRWS_Type(Integer32):
    """Custom type alL2tpStatsSessionLocalRWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsSessionLocalRWS_Type.__name__ = "Integer32"
_AlL2tpStatsSessionLocalRWS_Object = MibTableColumn
alL2tpStatsSessionLocalRWS = _AlL2tpStatsSessionLocalRWS_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 21),
    _AlL2tpStatsSessionLocalRWS_Type()
)
alL2tpStatsSessionLocalRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionLocalRWS.setStatus("deprecated")


class _AlL2tpStatsSessionRemoteInitialRWS_Type(Integer32):
    """Custom type alL2tpStatsSessionRemoteInitialRWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsSessionRemoteInitialRWS_Type.__name__ = "Integer32"
_AlL2tpStatsSessionRemoteInitialRWS_Object = MibTableColumn
alL2tpStatsSessionRemoteInitialRWS = _AlL2tpStatsSessionRemoteInitialRWS_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 22),
    _AlL2tpStatsSessionRemoteInitialRWS_Type()
)
alL2tpStatsSessionRemoteInitialRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRemoteInitialRWS.setStatus("deprecated")
_AlL2tpStatsSessionRemotePPD_Type = Integer32
_AlL2tpStatsSessionRemotePPD_Object = MibTableColumn
alL2tpStatsSessionRemotePPD = _AlL2tpStatsSessionRemotePPD_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 23),
    _AlL2tpStatsSessionRemotePPD_Type()
)
alL2tpStatsSessionRemotePPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRemotePPD.setStatus("current")


class _AlL2tpStatsSessionSequencingState_Type(Integer32):
    """Custom type alL2tpStatsSessionSequencingState based on Integer32"""
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
        *(("both", 4),
          ("local", 3),
          ("none", 1),
          ("remote", 2))
    )


_AlL2tpStatsSessionSequencingState_Type.__name__ = "Integer32"
_AlL2tpStatsSessionSequencingState_Object = MibTableColumn
alL2tpStatsSessionSequencingState = _AlL2tpStatsSessionSequencingState_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 24),
    _AlL2tpStatsSessionSequencingState_Type()
)
alL2tpStatsSessionSequencingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionSequencingState.setStatus("current")
_AlL2tpStatsSessionRecvOctets_Type = Counter32
_AlL2tpStatsSessionRecvOctets_Object = MibTableColumn
alL2tpStatsSessionRecvOctets = _AlL2tpStatsSessionRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 25),
    _AlL2tpStatsSessionRecvOctets_Type()
)
alL2tpStatsSessionRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRecvOctets.setStatus("current")
_AlL2tpStatsSessionRecvPackets_Type = Counter32
_AlL2tpStatsSessionRecvPackets_Object = MibTableColumn
alL2tpStatsSessionRecvPackets = _AlL2tpStatsSessionRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 26),
    _AlL2tpStatsSessionRecvPackets_Type()
)
alL2tpStatsSessionRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRecvPackets.setStatus("current")
_AlL2tpStatsSessionRecvDiscards_Type = Counter32
_AlL2tpStatsSessionRecvDiscards_Object = MibTableColumn
alL2tpStatsSessionRecvDiscards = _AlL2tpStatsSessionRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 27),
    _AlL2tpStatsSessionRecvDiscards_Type()
)
alL2tpStatsSessionRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRecvDiscards.setStatus("current")
_AlL2tpStatsSessionRecvZLB_Type = Counter32
_AlL2tpStatsSessionRecvZLB_Object = MibTableColumn
alL2tpStatsSessionRecvZLB = _AlL2tpStatsSessionRecvZLB_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 28),
    _AlL2tpStatsSessionRecvZLB_Type()
)
alL2tpStatsSessionRecvZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRecvZLB.setStatus("deprecated")
_AlL2tpStatsSessionOutSequence_Type = Counter32
_AlL2tpStatsSessionOutSequence_Object = MibTableColumn
alL2tpStatsSessionOutSequence = _AlL2tpStatsSessionOutSequence_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 29),
    _AlL2tpStatsSessionOutSequence_Type()
)
alL2tpStatsSessionOutSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionOutSequence.setStatus("current")
_AlL2tpStatsSessionOutOfWindow_Type = Counter32
_AlL2tpStatsSessionOutOfWindow_Object = MibTableColumn
alL2tpStatsSessionOutOfWindow = _AlL2tpStatsSessionOutOfWindow_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 30),
    _AlL2tpStatsSessionOutOfWindow_Type()
)
alL2tpStatsSessionOutOfWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionOutOfWindow.setStatus("deprecated")
_AlL2tpStatsSessionSendOctets_Type = Counter32
_AlL2tpStatsSessionSendOctets_Object = MibTableColumn
alL2tpStatsSessionSendOctets = _AlL2tpStatsSessionSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 31),
    _AlL2tpStatsSessionSendOctets_Type()
)
alL2tpStatsSessionSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionSendOctets.setStatus("current")
_AlL2tpStatsSessionSendPackets_Type = Counter32
_AlL2tpStatsSessionSendPackets_Object = MibTableColumn
alL2tpStatsSessionSendPackets = _AlL2tpStatsSessionSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 32),
    _AlL2tpStatsSessionSendPackets_Type()
)
alL2tpStatsSessionSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionSendPackets.setStatus("current")
_AlL2tpStatsSessionSendZLB_Type = Counter32
_AlL2tpStatsSessionSendZLB_Object = MibTableColumn
alL2tpStatsSessionSendZLB = _AlL2tpStatsSessionSendZLB_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 33),
    _AlL2tpStatsSessionSendZLB_Type()
)
alL2tpStatsSessionSendZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionSendZLB.setStatus("deprecated")
_AlL2tpStatsSessionAckTimeouts_Type = Counter32
_AlL2tpStatsSessionAckTimeouts_Object = MibTableColumn
alL2tpStatsSessionAckTimeouts = _AlL2tpStatsSessionAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 34),
    _AlL2tpStatsSessionAckTimeouts_Type()
)
alL2tpStatsSessionAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionAckTimeouts.setStatus("deprecated")
_AlL2tpStatsSessionReassemblyTimeouts_Type = Counter32
_AlL2tpStatsSessionReassemblyTimeouts_Object = MibTableColumn
alL2tpStatsSessionReassemblyTimeouts = _AlL2tpStatsSessionReassemblyTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 35),
    _AlL2tpStatsSessionReassemblyTimeouts_Type()
)
alL2tpStatsSessionReassemblyTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionReassemblyTimeouts.setStatus("current")


class _AlL2tpStatsSessionCurrentRemoteRWS_Type(Gauge32):
    """Custom type alL2tpStatsSessionCurrentRemoteRWS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsSessionCurrentRemoteRWS_Type.__name__ = "Gauge32"
_AlL2tpStatsSessionCurrentRemoteRWS_Object = MibTableColumn
alL2tpStatsSessionCurrentRemoteRWS = _AlL2tpStatsSessionCurrentRemoteRWS_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 36),
    _AlL2tpStatsSessionCurrentRemoteRWS_Type()
)
alL2tpStatsSessionCurrentRemoteRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionCurrentRemoteRWS.setStatus("deprecated")


class _AlL2tpStatsSessionSendSeq_Type(Integer32):
    """Custom type alL2tpStatsSessionSendSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsSessionSendSeq_Type.__name__ = "Integer32"
_AlL2tpStatsSessionSendSeq_Object = MibTableColumn
alL2tpStatsSessionSendSeq = _AlL2tpStatsSessionSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 37),
    _AlL2tpStatsSessionSendSeq_Type()
)
alL2tpStatsSessionSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionSendSeq.setStatus("current")


class _AlL2tpStatsSessionSendSeqAck_Type(Integer32):
    """Custom type alL2tpStatsSessionSendSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsSessionSendSeqAck_Type.__name__ = "Integer32"
_AlL2tpStatsSessionSendSeqAck_Object = MibTableColumn
alL2tpStatsSessionSendSeqAck = _AlL2tpStatsSessionSendSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 38),
    _AlL2tpStatsSessionSendSeqAck_Type()
)
alL2tpStatsSessionSendSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionSendSeqAck.setStatus("current")
_AlL2tpStatsSessionSendSeqResets_Type = Counter32
_AlL2tpStatsSessionSendSeqResets_Object = MibTableColumn
alL2tpStatsSessionSendSeqResets = _AlL2tpStatsSessionSendSeqResets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 39),
    _AlL2tpStatsSessionSendSeqResets_Type()
)
alL2tpStatsSessionSendSeqResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionSendSeqResets.setStatus("deprecated")


class _AlL2tpStatsSessionRecvSeq_Type(Integer32):
    """Custom type alL2tpStatsSessionRecvSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsSessionRecvSeq_Type.__name__ = "Integer32"
_AlL2tpStatsSessionRecvSeq_Object = MibTableColumn
alL2tpStatsSessionRecvSeq = _AlL2tpStatsSessionRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 40),
    _AlL2tpStatsSessionRecvSeq_Type()
)
alL2tpStatsSessionRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRecvSeq.setStatus("current")


class _AlL2tpStatsSessionRecvSeqAck_Type(Integer32):
    """Custom type alL2tpStatsSessionRecvSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlL2tpStatsSessionRecvSeqAck_Type.__name__ = "Integer32"
_AlL2tpStatsSessionRecvSeqAck_Object = MibTableColumn
alL2tpStatsSessionRecvSeqAck = _AlL2tpStatsSessionRecvSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 41),
    _AlL2tpStatsSessionRecvSeqAck_Type()
)
alL2tpStatsSessionRecvSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRecvSeqAck.setStatus("current")
_AlL2tpStatsSessionRecvSeqResets_Type = Counter32
_AlL2tpStatsSessionRecvSeqResets_Object = MibTableColumn
alL2tpStatsSessionRecvSeqResets = _AlL2tpStatsSessionRecvSeqResets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 42),
    _AlL2tpStatsSessionRecvSeqResets_Type()
)
alL2tpStatsSessionRecvSeqResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionRecvSeqResets.setStatus("deprecated")
_AlL2tpStatsSessionTunnelPeerIpAddr_Type = IpAddress
_AlL2tpStatsSessionTunnelPeerIpAddr_Object = MibTableColumn
alL2tpStatsSessionTunnelPeerIpAddr = _AlL2tpStatsSessionTunnelPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 16, 3, 1, 43),
    _AlL2tpStatsSessionTunnelPeerIpAddr_Type()
)
alL2tpStatsSessionTunnelPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alL2tpStatsSessionTunnelPeerIpAddr.setStatus("current")

# Managed Objects groups

altigaL2tpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 16, 2)
)
altigaL2tpStatsGroup.setObjects(
      *(("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsLocalProtVers"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsVendorName"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsFirmwareRev"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTotalTunnels"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsFailedTunnels"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsFailedAuthentications"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsActiveTunnels"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsMaxTunnels"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTotalSessions"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsFailedSessions"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsActiveSessions"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsMaxSessions"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsControlRecvOctets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsControlRecvPackets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsControlRecvDiscards"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsControlSendOctets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsControlSendPackets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsPayloadRecvOctets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsPayloadRecvPackets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsPayloadRecvDiscards"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsPayloadSendOctets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsPayloadSendPackets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelRowStatus"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelPeerIpAddr"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelLocalTID"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelRemoteTID"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelState"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelInitiated"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelRemoteHostName"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelRemoteVendorName"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelRemoteFirmwareRevision"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelRemoteProtocolVersion"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelInitialRemoteRWS"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelBearerCapabilities"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelFramingCapabilities"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelControlRecvPackets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelControlRecvDiscards"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelControlRecvZLB"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelControlOutOfSequence"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelControlOutOfWindow"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelControlSendPackets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelControlSendZLB"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelControlAckTimeouts"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelCurrentRemoteRWS"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelSendSeq"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelSendSeqAck"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelRecvSeq"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelRecvSeqAck"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelTotalSessions"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelFailedSessions"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelActiveSessions"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelLastResultCode"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelLastErrorCode"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsTunnelLastErrorMessage"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRowStatus"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionIfIndex"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionTID"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionLocalCID"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRemoteCID"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionUserName"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionState"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionCallType"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionCallSerialNumber"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionTxConnectSpeed"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRxConnectSpeed"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionCallBearerType"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionFramingType"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionPhysChanId"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionDNIS"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionCLID"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionSubAddress"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionPrivateGroupID"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionProxyLcp"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionAuthMethod"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRemotePPD"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionSequencingState"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRecvOctets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRecvPackets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRecvDiscards"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionOutSequence"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionSendOctets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionSendPackets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionReassemblyTimeouts"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionSendSeq"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionSendSeqAck"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRecvSeq"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRecvSeqAck"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionTunnelPeerIpAddr"))
)
if mibBuilder.loadTexts:
    altigaL2tpStatsGroup.setStatus("current")

altigaL2tpStatsDepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 16, 3)
)
altigaL2tpStatsDepGroup.setObjects(
      *(("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionLocalRWS"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRemoteInitialRWS"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRecvZLB"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionSendZLB"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionOutOfWindow"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionAckTimeouts"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionCurrentRemoteRWS"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionSendSeqResets"),
        ("ALTIGA-L2TP-STATS-MIB", "alL2tpStatsSessionRecvSeqResets"))
)
if mibBuilder.loadTexts:
    altigaL2tpStatsDepGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaL2tpStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 21, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaL2tpStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-L2TP-STATS-MIB",
    **{"altigaL2tpStatsMibModule": altigaL2tpStatsMibModule,
       "altigaL2tpStatsMibConformance": altigaL2tpStatsMibConformance,
       "altigaL2tpStatsMibCompliances": altigaL2tpStatsMibCompliances,
       "altigaL2tpStatsMibCompliance": altigaL2tpStatsMibCompliance,
       "altigaL2tpStatsGroup": altigaL2tpStatsGroup,
       "altigaL2tpStatsDepGroup": altigaL2tpStatsDepGroup,
       "alStatsL2tpGlobal": alStatsL2tpGlobal,
       "alL2tpStatsLocalProtVers": alL2tpStatsLocalProtVers,
       "alL2tpStatsVendorName": alL2tpStatsVendorName,
       "alL2tpStatsFirmwareRev": alL2tpStatsFirmwareRev,
       "alL2tpStatsTotalTunnels": alL2tpStatsTotalTunnels,
       "alL2tpStatsFailedTunnels": alL2tpStatsFailedTunnels,
       "alL2tpStatsFailedAuthentications": alL2tpStatsFailedAuthentications,
       "alL2tpStatsActiveTunnels": alL2tpStatsActiveTunnels,
       "alL2tpStatsMaxTunnels": alL2tpStatsMaxTunnels,
       "alL2tpStatsTotalSessions": alL2tpStatsTotalSessions,
       "alL2tpStatsFailedSessions": alL2tpStatsFailedSessions,
       "alL2tpStatsActiveSessions": alL2tpStatsActiveSessions,
       "alL2tpStatsMaxSessions": alL2tpStatsMaxSessions,
       "alL2tpStatsControlRecvOctets": alL2tpStatsControlRecvOctets,
       "alL2tpStatsControlRecvPackets": alL2tpStatsControlRecvPackets,
       "alL2tpStatsControlRecvDiscards": alL2tpStatsControlRecvDiscards,
       "alL2tpStatsControlSendOctets": alL2tpStatsControlSendOctets,
       "alL2tpStatsControlSendPackets": alL2tpStatsControlSendPackets,
       "alL2tpStatsPayloadRecvOctets": alL2tpStatsPayloadRecvOctets,
       "alL2tpStatsPayloadRecvPackets": alL2tpStatsPayloadRecvPackets,
       "alL2tpStatsPayloadRecvDiscards": alL2tpStatsPayloadRecvDiscards,
       "alL2tpStatsPayloadSendOctets": alL2tpStatsPayloadSendOctets,
       "alL2tpStatsPayloadSendPackets": alL2tpStatsPayloadSendPackets,
       "alL2tpStatsTunnelTable": alL2tpStatsTunnelTable,
       "alL2tpStatsTunnelEntry": alL2tpStatsTunnelEntry,
       "alL2tpStatsTunnelRowStatus": alL2tpStatsTunnelRowStatus,
       "alL2tpStatsTunnelPeerIpAddr": alL2tpStatsTunnelPeerIpAddr,
       "alL2tpStatsTunnelLocalTID": alL2tpStatsTunnelLocalTID,
       "alL2tpStatsTunnelRemoteTID": alL2tpStatsTunnelRemoteTID,
       "alL2tpStatsTunnelState": alL2tpStatsTunnelState,
       "alL2tpStatsTunnelInitiated": alL2tpStatsTunnelInitiated,
       "alL2tpStatsTunnelRemoteHostName": alL2tpStatsTunnelRemoteHostName,
       "alL2tpStatsTunnelRemoteVendorName": alL2tpStatsTunnelRemoteVendorName,
       "alL2tpStatsTunnelRemoteFirmwareRevision": alL2tpStatsTunnelRemoteFirmwareRevision,
       "alL2tpStatsTunnelRemoteProtocolVersion": alL2tpStatsTunnelRemoteProtocolVersion,
       "alL2tpStatsTunnelInitialRemoteRWS": alL2tpStatsTunnelInitialRemoteRWS,
       "alL2tpStatsTunnelBearerCapabilities": alL2tpStatsTunnelBearerCapabilities,
       "alL2tpStatsTunnelFramingCapabilities": alL2tpStatsTunnelFramingCapabilities,
       "alL2tpStatsTunnelControlRecvPackets": alL2tpStatsTunnelControlRecvPackets,
       "alL2tpStatsTunnelControlRecvDiscards": alL2tpStatsTunnelControlRecvDiscards,
       "alL2tpStatsTunnelControlRecvZLB": alL2tpStatsTunnelControlRecvZLB,
       "alL2tpStatsTunnelControlOutOfSequence": alL2tpStatsTunnelControlOutOfSequence,
       "alL2tpStatsTunnelControlOutOfWindow": alL2tpStatsTunnelControlOutOfWindow,
       "alL2tpStatsTunnelControlSendPackets": alL2tpStatsTunnelControlSendPackets,
       "alL2tpStatsTunnelControlSendZLB": alL2tpStatsTunnelControlSendZLB,
       "alL2tpStatsTunnelControlAckTimeouts": alL2tpStatsTunnelControlAckTimeouts,
       "alL2tpStatsTunnelCurrentRemoteRWS": alL2tpStatsTunnelCurrentRemoteRWS,
       "alL2tpStatsTunnelSendSeq": alL2tpStatsTunnelSendSeq,
       "alL2tpStatsTunnelSendSeqAck": alL2tpStatsTunnelSendSeqAck,
       "alL2tpStatsTunnelRecvSeq": alL2tpStatsTunnelRecvSeq,
       "alL2tpStatsTunnelRecvSeqAck": alL2tpStatsTunnelRecvSeqAck,
       "alL2tpStatsTunnelTotalSessions": alL2tpStatsTunnelTotalSessions,
       "alL2tpStatsTunnelFailedSessions": alL2tpStatsTunnelFailedSessions,
       "alL2tpStatsTunnelActiveSessions": alL2tpStatsTunnelActiveSessions,
       "alL2tpStatsTunnelLastResultCode": alL2tpStatsTunnelLastResultCode,
       "alL2tpStatsTunnelLastErrorCode": alL2tpStatsTunnelLastErrorCode,
       "alL2tpStatsTunnelLastErrorMessage": alL2tpStatsTunnelLastErrorMessage,
       "alL2tpStatsSessionTable": alL2tpStatsSessionTable,
       "alL2tpStatsSessionEntry": alL2tpStatsSessionEntry,
       "alL2tpStatsSessionRowStatus": alL2tpStatsSessionRowStatus,
       "alL2tpStatsSessionIfIndex": alL2tpStatsSessionIfIndex,
       "alL2tpStatsSessionTID": alL2tpStatsSessionTID,
       "alL2tpStatsSessionLocalCID": alL2tpStatsSessionLocalCID,
       "alL2tpStatsSessionRemoteCID": alL2tpStatsSessionRemoteCID,
       "alL2tpStatsSessionUserName": alL2tpStatsSessionUserName,
       "alL2tpStatsSessionState": alL2tpStatsSessionState,
       "alL2tpStatsSessionCallType": alL2tpStatsSessionCallType,
       "alL2tpStatsSessionCallSerialNumber": alL2tpStatsSessionCallSerialNumber,
       "alL2tpStatsSessionTxConnectSpeed": alL2tpStatsSessionTxConnectSpeed,
       "alL2tpStatsSessionRxConnectSpeed": alL2tpStatsSessionRxConnectSpeed,
       "alL2tpStatsSessionCallBearerType": alL2tpStatsSessionCallBearerType,
       "alL2tpStatsSessionFramingType": alL2tpStatsSessionFramingType,
       "alL2tpStatsSessionPhysChanId": alL2tpStatsSessionPhysChanId,
       "alL2tpStatsSessionDNIS": alL2tpStatsSessionDNIS,
       "alL2tpStatsSessionCLID": alL2tpStatsSessionCLID,
       "alL2tpStatsSessionSubAddress": alL2tpStatsSessionSubAddress,
       "alL2tpStatsSessionPrivateGroupID": alL2tpStatsSessionPrivateGroupID,
       "alL2tpStatsSessionProxyLcp": alL2tpStatsSessionProxyLcp,
       "alL2tpStatsSessionAuthMethod": alL2tpStatsSessionAuthMethod,
       "alL2tpStatsSessionLocalRWS": alL2tpStatsSessionLocalRWS,
       "alL2tpStatsSessionRemoteInitialRWS": alL2tpStatsSessionRemoteInitialRWS,
       "alL2tpStatsSessionRemotePPD": alL2tpStatsSessionRemotePPD,
       "alL2tpStatsSessionSequencingState": alL2tpStatsSessionSequencingState,
       "alL2tpStatsSessionRecvOctets": alL2tpStatsSessionRecvOctets,
       "alL2tpStatsSessionRecvPackets": alL2tpStatsSessionRecvPackets,
       "alL2tpStatsSessionRecvDiscards": alL2tpStatsSessionRecvDiscards,
       "alL2tpStatsSessionRecvZLB": alL2tpStatsSessionRecvZLB,
       "alL2tpStatsSessionOutSequence": alL2tpStatsSessionOutSequence,
       "alL2tpStatsSessionOutOfWindow": alL2tpStatsSessionOutOfWindow,
       "alL2tpStatsSessionSendOctets": alL2tpStatsSessionSendOctets,
       "alL2tpStatsSessionSendPackets": alL2tpStatsSessionSendPackets,
       "alL2tpStatsSessionSendZLB": alL2tpStatsSessionSendZLB,
       "alL2tpStatsSessionAckTimeouts": alL2tpStatsSessionAckTimeouts,
       "alL2tpStatsSessionReassemblyTimeouts": alL2tpStatsSessionReassemblyTimeouts,
       "alL2tpStatsSessionCurrentRemoteRWS": alL2tpStatsSessionCurrentRemoteRWS,
       "alL2tpStatsSessionSendSeq": alL2tpStatsSessionSendSeq,
       "alL2tpStatsSessionSendSeqAck": alL2tpStatsSessionSendSeqAck,
       "alL2tpStatsSessionSendSeqResets": alL2tpStatsSessionSendSeqResets,
       "alL2tpStatsSessionRecvSeq": alL2tpStatsSessionRecvSeq,
       "alL2tpStatsSessionRecvSeqAck": alL2tpStatsSessionRecvSeqAck,
       "alL2tpStatsSessionRecvSeqResets": alL2tpStatsSessionRecvSeqResets,
       "alL2tpStatsSessionTunnelPeerIpAddr": alL2tpStatsSessionTunnelPeerIpAddr}
)
