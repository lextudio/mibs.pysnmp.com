# SNMP MIB module (ALTIGA-PPTP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-PPTP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:20 2024
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

(alPptpMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alPptpMibModule")

(alPptpGroup,
 alStatsPptp) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alPptpGroup",
    "alStatsPptp")

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

altigaPptpStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 10, 2)
)
altigaPptpStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaPptpStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaPptpStatsMibConformance = _AltigaPptpStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 10, 2, 1)
)
_AltigaPptpStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaPptpStatsMibCompliances = _AltigaPptpStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 10, 2, 1, 1)
)
_AlStatsPptpGlobal_ObjectIdentity = ObjectIdentity
alStatsPptpGlobal = _AlStatsPptpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1)
)


class _AlPptpStatsLocalProtVers_Type(OctetString):
    """Custom type alPptpStatsLocalProtVers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlPptpStatsLocalProtVers_Type.__name__ = "OctetString"
_AlPptpStatsLocalProtVers_Object = MibScalar
alPptpStatsLocalProtVers = _AlPptpStatsLocalProtVers_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 1),
    _AlPptpStatsLocalProtVers_Type()
)
alPptpStatsLocalProtVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsLocalProtVers.setStatus("current")


class _AlPptpStatsLocalFraming_Type(Integer32):
    """Custom type alPptpStatsLocalFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlPptpStatsLocalFraming_Type.__name__ = "Integer32"
_AlPptpStatsLocalFraming_Object = MibScalar
alPptpStatsLocalFraming = _AlPptpStatsLocalFraming_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 2),
    _AlPptpStatsLocalFraming_Type()
)
alPptpStatsLocalFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsLocalFraming.setStatus("current")


class _AlPptpStatsLocalBearer_Type(Integer32):
    """Custom type alPptpStatsLocalBearer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlPptpStatsLocalBearer_Type.__name__ = "Integer32"
_AlPptpStatsLocalBearer_Object = MibScalar
alPptpStatsLocalBearer = _AlPptpStatsLocalBearer_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 3),
    _AlPptpStatsLocalBearer_Type()
)
alPptpStatsLocalBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsLocalBearer.setStatus("current")


class _AlPptpStatsLocalFirmwareRev_Type(OctetString):
    """Custom type alPptpStatsLocalFirmwareRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlPptpStatsLocalFirmwareRev_Type.__name__ = "OctetString"
_AlPptpStatsLocalFirmwareRev_Object = MibScalar
alPptpStatsLocalFirmwareRev = _AlPptpStatsLocalFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 4),
    _AlPptpStatsLocalFirmwareRev_Type()
)
alPptpStatsLocalFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsLocalFirmwareRev.setStatus("current")
_AlPptpStatsTotalTunnels_Type = Gauge32
_AlPptpStatsTotalTunnels_Object = MibScalar
alPptpStatsTotalTunnels = _AlPptpStatsTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 5),
    _AlPptpStatsTotalTunnels_Type()
)
alPptpStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTotalTunnels.setStatus("current")
_AlPptpStatsActiveTunnels_Type = Gauge32
_AlPptpStatsActiveTunnels_Object = MibScalar
alPptpStatsActiveTunnels = _AlPptpStatsActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 6),
    _AlPptpStatsActiveTunnels_Type()
)
alPptpStatsActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsActiveTunnels.setStatus("current")
_AlPptpStatsMaxTunnels_Type = Gauge32
_AlPptpStatsMaxTunnels_Object = MibScalar
alPptpStatsMaxTunnels = _AlPptpStatsMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 7),
    _AlPptpStatsMaxTunnels_Type()
)
alPptpStatsMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsMaxTunnels.setStatus("current")
_AlPptpStatsTotalSessions_Type = Gauge32
_AlPptpStatsTotalSessions_Object = MibScalar
alPptpStatsTotalSessions = _AlPptpStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 8),
    _AlPptpStatsTotalSessions_Type()
)
alPptpStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTotalSessions.setStatus("current")
_AlPptpStatsActiveSessions_Type = Gauge32
_AlPptpStatsActiveSessions_Object = MibScalar
alPptpStatsActiveSessions = _AlPptpStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 9),
    _AlPptpStatsActiveSessions_Type()
)
alPptpStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsActiveSessions.setStatus("current")
_AlPptpStatsMaxSessions_Type = Gauge32
_AlPptpStatsMaxSessions_Object = MibScalar
alPptpStatsMaxSessions = _AlPptpStatsMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 10),
    _AlPptpStatsMaxSessions_Type()
)
alPptpStatsMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsMaxSessions.setStatus("current")
_AlPptpStatsControlRecvOctets_Type = Counter32
_AlPptpStatsControlRecvOctets_Object = MibScalar
alPptpStatsControlRecvOctets = _AlPptpStatsControlRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 11),
    _AlPptpStatsControlRecvOctets_Type()
)
alPptpStatsControlRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsControlRecvOctets.setStatus("current")
_AlPptpStatsControlRecvPackets_Type = Counter32
_AlPptpStatsControlRecvPackets_Object = MibScalar
alPptpStatsControlRecvPackets = _AlPptpStatsControlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 12),
    _AlPptpStatsControlRecvPackets_Type()
)
alPptpStatsControlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsControlRecvPackets.setStatus("current")
_AlPptpStatsControlRecvDiscards_Type = Counter32
_AlPptpStatsControlRecvDiscards_Object = MibScalar
alPptpStatsControlRecvDiscards = _AlPptpStatsControlRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 13),
    _AlPptpStatsControlRecvDiscards_Type()
)
alPptpStatsControlRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsControlRecvDiscards.setStatus("current")
_AlPptpStatsControlSendOctets_Type = Counter32
_AlPptpStatsControlSendOctets_Object = MibScalar
alPptpStatsControlSendOctets = _AlPptpStatsControlSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 14),
    _AlPptpStatsControlSendOctets_Type()
)
alPptpStatsControlSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsControlSendOctets.setStatus("current")
_AlPptpStatsControlSendPackets_Type = Counter32
_AlPptpStatsControlSendPackets_Object = MibScalar
alPptpStatsControlSendPackets = _AlPptpStatsControlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 15),
    _AlPptpStatsControlSendPackets_Type()
)
alPptpStatsControlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsControlSendPackets.setStatus("current")
_AlPptpStatsPayloadRecvOctets_Type = Counter32
_AlPptpStatsPayloadRecvOctets_Object = MibScalar
alPptpStatsPayloadRecvOctets = _AlPptpStatsPayloadRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 16),
    _AlPptpStatsPayloadRecvOctets_Type()
)
alPptpStatsPayloadRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsPayloadRecvOctets.setStatus("current")
_AlPptpStatsPayloadRecvPackets_Type = Counter32
_AlPptpStatsPayloadRecvPackets_Object = MibScalar
alPptpStatsPayloadRecvPackets = _AlPptpStatsPayloadRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 17),
    _AlPptpStatsPayloadRecvPackets_Type()
)
alPptpStatsPayloadRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsPayloadRecvPackets.setStatus("current")
_AlPptpStatsPayloadRecvDiscards_Type = Counter32
_AlPptpStatsPayloadRecvDiscards_Object = MibScalar
alPptpStatsPayloadRecvDiscards = _AlPptpStatsPayloadRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 18),
    _AlPptpStatsPayloadRecvDiscards_Type()
)
alPptpStatsPayloadRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsPayloadRecvDiscards.setStatus("current")
_AlPptpStatsPayloadSendOctets_Type = Counter32
_AlPptpStatsPayloadSendOctets_Object = MibScalar
alPptpStatsPayloadSendOctets = _AlPptpStatsPayloadSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 19),
    _AlPptpStatsPayloadSendOctets_Type()
)
alPptpStatsPayloadSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsPayloadSendOctets.setStatus("current")
_AlPptpStatsPayloadSendPackets_Type = Counter32
_AlPptpStatsPayloadSendPackets_Object = MibScalar
alPptpStatsPayloadSendPackets = _AlPptpStatsPayloadSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 20),
    _AlPptpStatsPayloadSendPackets_Type()
)
alPptpStatsPayloadSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsPayloadSendPackets.setStatus("current")
_AlPptpStatsTunnelTable_Object = MibTable
alPptpStatsTunnelTable = _AlPptpStatsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    alPptpStatsTunnelTable.setStatus("current")
_AlPptpStatsTunnelEntry_Object = MibTableRow
alPptpStatsTunnelEntry = _AlPptpStatsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1)
)
alPptpStatsTunnelEntry.setIndexNames(
    (0, "ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerIpAddr"),
)
if mibBuilder.loadTexts:
    alPptpStatsTunnelEntry.setStatus("current")
_AlPptpStatsTunnelRowStatus_Type = RowStatus
_AlPptpStatsTunnelRowStatus_Object = MibTableColumn
alPptpStatsTunnelRowStatus = _AlPptpStatsTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 1),
    _AlPptpStatsTunnelRowStatus_Type()
)
alPptpStatsTunnelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPptpStatsTunnelRowStatus.setStatus("current")
_AlPptpStatsTunnelPeerIpAddr_Type = IpAddress
_AlPptpStatsTunnelPeerIpAddr_Object = MibTableColumn
alPptpStatsTunnelPeerIpAddr = _AlPptpStatsTunnelPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 2),
    _AlPptpStatsTunnelPeerIpAddr_Type()
)
alPptpStatsTunnelPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelPeerIpAddr.setStatus("current")
_AlPptpStatsTunnelDatastreamId_Type = Integer32
_AlPptpStatsTunnelDatastreamId_Object = MibTableColumn
alPptpStatsTunnelDatastreamId = _AlPptpStatsTunnelDatastreamId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 3),
    _AlPptpStatsTunnelDatastreamId_Type()
)
alPptpStatsTunnelDatastreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelDatastreamId.setStatus("current")
_AlPptpStatsTunnelLocalIpAddr_Type = IpAddress
_AlPptpStatsTunnelLocalIpAddr_Object = MibTableColumn
alPptpStatsTunnelLocalIpAddr = _AlPptpStatsTunnelLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 4),
    _AlPptpStatsTunnelLocalIpAddr_Type()
)
alPptpStatsTunnelLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelLocalIpAddr.setStatus("current")
_AlPptpStatsTunnelPeerHostName_Type = DisplayString
_AlPptpStatsTunnelPeerHostName_Object = MibTableColumn
alPptpStatsTunnelPeerHostName = _AlPptpStatsTunnelPeerHostName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 5),
    _AlPptpStatsTunnelPeerHostName_Type()
)
alPptpStatsTunnelPeerHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelPeerHostName.setStatus("current")
_AlPptpStatsTunnelPeerVendorName_Type = DisplayString
_AlPptpStatsTunnelPeerVendorName_Object = MibTableColumn
alPptpStatsTunnelPeerVendorName = _AlPptpStatsTunnelPeerVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 6),
    _AlPptpStatsTunnelPeerVendorName_Type()
)
alPptpStatsTunnelPeerVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelPeerVendorName.setStatus("current")


class _AlPptpStatsTunnelPeerFirmwareRev_Type(OctetString):
    """Custom type alPptpStatsTunnelPeerFirmwareRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlPptpStatsTunnelPeerFirmwareRev_Type.__name__ = "OctetString"
_AlPptpStatsTunnelPeerFirmwareRev_Object = MibTableColumn
alPptpStatsTunnelPeerFirmwareRev = _AlPptpStatsTunnelPeerFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 7),
    _AlPptpStatsTunnelPeerFirmwareRev_Type()
)
alPptpStatsTunnelPeerFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelPeerFirmwareRev.setStatus("current")


class _AlPptpStatsTunnelPeerProtVers_Type(OctetString):
    """Custom type alPptpStatsTunnelPeerProtVers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlPptpStatsTunnelPeerProtVers_Type.__name__ = "OctetString"
_AlPptpStatsTunnelPeerProtVers_Object = MibTableColumn
alPptpStatsTunnelPeerProtVers = _AlPptpStatsTunnelPeerProtVers_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 8),
    _AlPptpStatsTunnelPeerProtVers_Type()
)
alPptpStatsTunnelPeerProtVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelPeerProtVers.setStatus("current")


class _AlPptpStatsTunnelPeerFramingCap_Type(Integer32):
    """Custom type alPptpStatsTunnelPeerFramingCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlPptpStatsTunnelPeerFramingCap_Type.__name__ = "Integer32"
_AlPptpStatsTunnelPeerFramingCap_Object = MibTableColumn
alPptpStatsTunnelPeerFramingCap = _AlPptpStatsTunnelPeerFramingCap_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 9),
    _AlPptpStatsTunnelPeerFramingCap_Type()
)
alPptpStatsTunnelPeerFramingCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelPeerFramingCap.setStatus("current")


class _AlPptpStatsTunnelPeerBearerCap_Type(Integer32):
    """Custom type alPptpStatsTunnelPeerBearerCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlPptpStatsTunnelPeerBearerCap_Type.__name__ = "Integer32"
_AlPptpStatsTunnelPeerBearerCap_Object = MibTableColumn
alPptpStatsTunnelPeerBearerCap = _AlPptpStatsTunnelPeerBearerCap_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 10),
    _AlPptpStatsTunnelPeerBearerCap_Type()
)
alPptpStatsTunnelPeerBearerCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelPeerBearerCap.setStatus("current")
_AlPptpStatsTunnelPeerMaxChan_Type = Integer32
_AlPptpStatsTunnelPeerMaxChan_Object = MibTableColumn
alPptpStatsTunnelPeerMaxChan = _AlPptpStatsTunnelPeerMaxChan_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 11),
    _AlPptpStatsTunnelPeerMaxChan_Type()
)
alPptpStatsTunnelPeerMaxChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelPeerMaxChan.setStatus("current")
_AlPptpStatsTunnelActiveSessions_Type = Counter32
_AlPptpStatsTunnelActiveSessions_Object = MibTableColumn
alPptpStatsTunnelActiveSessions = _AlPptpStatsTunnelActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 12),
    _AlPptpStatsTunnelActiveSessions_Type()
)
alPptpStatsTunnelActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsTunnelActiveSessions.setStatus("current")
_AlPptpStatsSessionTable_Object = MibTable
alPptpStatsSessionTable = _AlPptpStatsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    alPptpStatsSessionTable.setStatus("current")
_AlPptpStatsSessionEntry_Object = MibTableRow
alPptpStatsSessionEntry = _AlPptpStatsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1)
)
alPptpStatsSessionEntry.setIndexNames(
    (0, "ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionDatastreamId"),
)
if mibBuilder.loadTexts:
    alPptpStatsSessionEntry.setStatus("current")
_AlPptpStatsSessionRowStatus_Type = RowStatus
_AlPptpStatsSessionRowStatus_Object = MibTableColumn
alPptpStatsSessionRowStatus = _AlPptpStatsSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 1),
    _AlPptpStatsSessionRowStatus_Type()
)
alPptpStatsSessionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPptpStatsSessionRowStatus.setStatus("current")
_AlPptpStatsSessionDatastreamId_Type = Integer32
_AlPptpStatsSessionDatastreamId_Object = MibTableColumn
alPptpStatsSessionDatastreamId = _AlPptpStatsSessionDatastreamId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 2),
    _AlPptpStatsSessionDatastreamId_Type()
)
alPptpStatsSessionDatastreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionDatastreamId.setStatus("current")


class _AlPptpStatsSessionLocalCallId_Type(Integer32):
    """Custom type alPptpStatsSessionLocalCallId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlPptpStatsSessionLocalCallId_Type.__name__ = "Integer32"
_AlPptpStatsSessionLocalCallId_Object = MibTableColumn
alPptpStatsSessionLocalCallId = _AlPptpStatsSessionLocalCallId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 3),
    _AlPptpStatsSessionLocalCallId_Type()
)
alPptpStatsSessionLocalCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionLocalCallId.setStatus("current")


class _AlPptpStatsSessionPeerCallId_Type(Integer32):
    """Custom type alPptpStatsSessionPeerCallId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlPptpStatsSessionPeerCallId_Type.__name__ = "Integer32"
_AlPptpStatsSessionPeerCallId_Object = MibTableColumn
alPptpStatsSessionPeerCallId = _AlPptpStatsSessionPeerCallId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 4),
    _AlPptpStatsSessionPeerCallId_Type()
)
alPptpStatsSessionPeerCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionPeerCallId.setStatus("current")
_AlPptpStatsSessionUserName_Type = DisplayString
_AlPptpStatsSessionUserName_Object = MibTableColumn
alPptpStatsSessionUserName = _AlPptpStatsSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 5),
    _AlPptpStatsSessionUserName_Type()
)
alPptpStatsSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionUserName.setStatus("current")


class _AlPptpStatsSessionSerial_Type(Integer32):
    """Custom type alPptpStatsSessionSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlPptpStatsSessionSerial_Type.__name__ = "Integer32"
_AlPptpStatsSessionSerial_Object = MibTableColumn
alPptpStatsSessionSerial = _AlPptpStatsSessionSerial_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 6),
    _AlPptpStatsSessionSerial_Type()
)
alPptpStatsSessionSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionSerial.setStatus("current")
_AlPptpStatsSessionMinimumSpeed_Type = Integer32
_AlPptpStatsSessionMinimumSpeed_Object = MibTableColumn
alPptpStatsSessionMinimumSpeed = _AlPptpStatsSessionMinimumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 7),
    _AlPptpStatsSessionMinimumSpeed_Type()
)
alPptpStatsSessionMinimumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionMinimumSpeed.setStatus("current")
_AlPptpStatsSessionMaximumSpeed_Type = Integer32
_AlPptpStatsSessionMaximumSpeed_Object = MibTableColumn
alPptpStatsSessionMaximumSpeed = _AlPptpStatsSessionMaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 8),
    _AlPptpStatsSessionMaximumSpeed_Type()
)
alPptpStatsSessionMaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionMaximumSpeed.setStatus("current")
_AlPptpStatsSessionConnectSpeed_Type = Integer32
_AlPptpStatsSessionConnectSpeed_Object = MibTableColumn
alPptpStatsSessionConnectSpeed = _AlPptpStatsSessionConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 9),
    _AlPptpStatsSessionConnectSpeed_Type()
)
alPptpStatsSessionConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionConnectSpeed.setStatus("current")


class _AlPptpStatsSessionBearerType_Type(Integer32):
    """Custom type alPptpStatsSessionBearerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 1),
          ("any", 3),
          ("digital", 2))
    )


_AlPptpStatsSessionBearerType_Type.__name__ = "Integer32"
_AlPptpStatsSessionBearerType_Object = MibTableColumn
alPptpStatsSessionBearerType = _AlPptpStatsSessionBearerType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 10),
    _AlPptpStatsSessionBearerType_Type()
)
alPptpStatsSessionBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionBearerType.setStatus("current")


class _AlPptpStatsSessionFramingType_Type(Integer32):
    """Custom type alPptpStatsSessionFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("either", 3),
          ("synchronous", 2))
    )


_AlPptpStatsSessionFramingType_Type.__name__ = "Integer32"
_AlPptpStatsSessionFramingType_Object = MibTableColumn
alPptpStatsSessionFramingType = _AlPptpStatsSessionFramingType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 11),
    _AlPptpStatsSessionFramingType_Type()
)
alPptpStatsSessionFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionFramingType.setStatus("current")
_AlPptpStatsSessionPhysicalChannel_Type = Integer32
_AlPptpStatsSessionPhysicalChannel_Object = MibTableColumn
alPptpStatsSessionPhysicalChannel = _AlPptpStatsSessionPhysicalChannel_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 12),
    _AlPptpStatsSessionPhysicalChannel_Type()
)
alPptpStatsSessionPhysicalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionPhysicalChannel.setStatus("current")
_AlPptpStatsSessionLocalWindowSize_Type = Integer32
_AlPptpStatsSessionLocalWindowSize_Object = MibTableColumn
alPptpStatsSessionLocalWindowSize = _AlPptpStatsSessionLocalWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 13),
    _AlPptpStatsSessionLocalWindowSize_Type()
)
alPptpStatsSessionLocalWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionLocalWindowSize.setStatus("current")
_AlPptpStatsSessionPeerWindowSize_Type = Integer32
_AlPptpStatsSessionPeerWindowSize_Object = MibTableColumn
alPptpStatsSessionPeerWindowSize = _AlPptpStatsSessionPeerWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 14),
    _AlPptpStatsSessionPeerWindowSize_Type()
)
alPptpStatsSessionPeerWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionPeerWindowSize.setStatus("current")
_AlPptpStatsSessionLocalPpd_Type = Integer32
_AlPptpStatsSessionLocalPpd_Object = MibTableColumn
alPptpStatsSessionLocalPpd = _AlPptpStatsSessionLocalPpd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 15),
    _AlPptpStatsSessionLocalPpd_Type()
)
alPptpStatsSessionLocalPpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionLocalPpd.setStatus("current")
_AlPptpStatsSessionPeerPpd_Type = Integer32
_AlPptpStatsSessionPeerPpd_Object = MibTableColumn
alPptpStatsSessionPeerPpd = _AlPptpStatsSessionPeerPpd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 16),
    _AlPptpStatsSessionPeerPpd_Type()
)
alPptpStatsSessionPeerPpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionPeerPpd.setStatus("current")
_AlPptpStatsSessionRecvOctets_Type = Counter32
_AlPptpStatsSessionRecvOctets_Object = MibTableColumn
alPptpStatsSessionRecvOctets = _AlPptpStatsSessionRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 17),
    _AlPptpStatsSessionRecvOctets_Type()
)
alPptpStatsSessionRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionRecvOctets.setStatus("current")
_AlPptpStatsSessionRecvPackets_Type = Counter32
_AlPptpStatsSessionRecvPackets_Object = MibTableColumn
alPptpStatsSessionRecvPackets = _AlPptpStatsSessionRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 18),
    _AlPptpStatsSessionRecvPackets_Type()
)
alPptpStatsSessionRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionRecvPackets.setStatus("current")
_AlPptpStatsSessionRecvDiscards_Type = Counter32
_AlPptpStatsSessionRecvDiscards_Object = MibTableColumn
alPptpStatsSessionRecvDiscards = _AlPptpStatsSessionRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 19),
    _AlPptpStatsSessionRecvDiscards_Type()
)
alPptpStatsSessionRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionRecvDiscards.setStatus("current")
_AlPptpStatsSessionRecvZLB_Type = Counter32
_AlPptpStatsSessionRecvZLB_Object = MibTableColumn
alPptpStatsSessionRecvZLB = _AlPptpStatsSessionRecvZLB_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 20),
    _AlPptpStatsSessionRecvZLB_Type()
)
alPptpStatsSessionRecvZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionRecvZLB.setStatus("current")
_AlPptpStatsSessionSendOctets_Type = Counter32
_AlPptpStatsSessionSendOctets_Object = MibTableColumn
alPptpStatsSessionSendOctets = _AlPptpStatsSessionSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 21),
    _AlPptpStatsSessionSendOctets_Type()
)
alPptpStatsSessionSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionSendOctets.setStatus("current")
_AlPptpStatsSessionSendPackets_Type = Counter32
_AlPptpStatsSessionSendPackets_Object = MibTableColumn
alPptpStatsSessionSendPackets = _AlPptpStatsSessionSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 22),
    _AlPptpStatsSessionSendPackets_Type()
)
alPptpStatsSessionSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionSendPackets.setStatus("current")
_AlPptpStatsSessionSendZLB_Type = Counter32
_AlPptpStatsSessionSendZLB_Object = MibTableColumn
alPptpStatsSessionSendZLB = _AlPptpStatsSessionSendZLB_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 23),
    _AlPptpStatsSessionSendZLB_Type()
)
alPptpStatsSessionSendZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionSendZLB.setStatus("current")
_AlPptpStatsSessionAckTimeouts_Type = Counter32
_AlPptpStatsSessionAckTimeouts_Object = MibTableColumn
alPptpStatsSessionAckTimeouts = _AlPptpStatsSessionAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 24),
    _AlPptpStatsSessionAckTimeouts_Type()
)
alPptpStatsSessionAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionAckTimeouts.setStatus("current")
_AlPptpStatsSessionLocalFlowOff_Type = TruthValue
_AlPptpStatsSessionLocalFlowOff_Object = MibTableColumn
alPptpStatsSessionLocalFlowOff = _AlPptpStatsSessionLocalFlowOff_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 25),
    _AlPptpStatsSessionLocalFlowOff_Type()
)
alPptpStatsSessionLocalFlowOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionLocalFlowOff.setStatus("current")
_AlPptpStatsSessionPeerFlowOff_Type = TruthValue
_AlPptpStatsSessionPeerFlowOff_Object = MibTableColumn
alPptpStatsSessionPeerFlowOff = _AlPptpStatsSessionPeerFlowOff_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 26),
    _AlPptpStatsSessionPeerFlowOff_Type()
)
alPptpStatsSessionPeerFlowOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionPeerFlowOff.setStatus("current")
_AlPptpStatsSessionOutOfWindow_Type = Counter32
_AlPptpStatsSessionOutOfWindow_Object = MibTableColumn
alPptpStatsSessionOutOfWindow = _AlPptpStatsSessionOutOfWindow_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 27),
    _AlPptpStatsSessionOutOfWindow_Type()
)
alPptpStatsSessionOutOfWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionOutOfWindow.setStatus("current")
_AlPptpStatsSessionOutOfSequence_Type = Counter32
_AlPptpStatsSessionOutOfSequence_Object = MibTableColumn
alPptpStatsSessionOutOfSequence = _AlPptpStatsSessionOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 28),
    _AlPptpStatsSessionOutOfSequence_Type()
)
alPptpStatsSessionOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionOutOfSequence.setStatus("current")
_AlPptpStatsSessionTunnelPeerIpAddr_Type = IpAddress
_AlPptpStatsSessionTunnelPeerIpAddr_Object = MibTableColumn
alPptpStatsSessionTunnelPeerIpAddr = _AlPptpStatsSessionTunnelPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 29),
    _AlPptpStatsSessionTunnelPeerIpAddr_Type()
)
alPptpStatsSessionTunnelPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPptpStatsSessionTunnelPeerIpAddr.setStatus("current")

# Managed Objects groups

altigaPptpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 3, 2)
)
altigaPptpStatsGroup.setObjects(
      *(("ALTIGA-PPTP-STATS-MIB", "alPptpStatsLocalProtVers"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsLocalFraming"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsLocalBearer"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsLocalFirmwareRev"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTotalTunnels"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsActiveTunnels"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsMaxTunnels"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTotalSessions"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsActiveSessions"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsMaxSessions"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsControlRecvOctets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsControlRecvPackets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsControlRecvDiscards"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsControlSendOctets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsControlSendPackets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsPayloadRecvOctets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsPayloadRecvPackets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsPayloadRecvDiscards"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsPayloadSendOctets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsPayloadSendPackets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelRowStatus"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelDatastreamId"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelLocalIpAddr"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerIpAddr"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerHostName"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerVendorName"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerFirmwareRev"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerProtVers"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerFramingCap"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerBearerCap"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerMaxChan"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelActiveSessions"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionRowStatus"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionDatastreamId"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionLocalCallId"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionPeerCallId"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionUserName"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionSerial"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionMinimumSpeed"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionMaximumSpeed"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionConnectSpeed"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionBearerType"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionFramingType"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionPhysicalChannel"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionLocalWindowSize"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionPeerWindowSize"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionLocalPpd"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionPeerPpd"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionRecvOctets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionRecvPackets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionRecvDiscards"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionRecvZLB"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionSendOctets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionSendPackets"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionSendZLB"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionAckTimeouts"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionLocalFlowOff"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionPeerFlowOff"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionOutOfWindow"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionOutOfSequence"),
        ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionTunnelPeerIpAddr"))
)
if mibBuilder.loadTexts:
    altigaPptpStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaPptpStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 10, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaPptpStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-PPTP-STATS-MIB",
    **{"altigaPptpStatsMibModule": altigaPptpStatsMibModule,
       "altigaPptpStatsMibConformance": altigaPptpStatsMibConformance,
       "altigaPptpStatsMibCompliances": altigaPptpStatsMibCompliances,
       "altigaPptpStatsMibCompliance": altigaPptpStatsMibCompliance,
       "altigaPptpStatsGroup": altigaPptpStatsGroup,
       "alStatsPptpGlobal": alStatsPptpGlobal,
       "alPptpStatsLocalProtVers": alPptpStatsLocalProtVers,
       "alPptpStatsLocalFraming": alPptpStatsLocalFraming,
       "alPptpStatsLocalBearer": alPptpStatsLocalBearer,
       "alPptpStatsLocalFirmwareRev": alPptpStatsLocalFirmwareRev,
       "alPptpStatsTotalTunnels": alPptpStatsTotalTunnels,
       "alPptpStatsActiveTunnels": alPptpStatsActiveTunnels,
       "alPptpStatsMaxTunnels": alPptpStatsMaxTunnels,
       "alPptpStatsTotalSessions": alPptpStatsTotalSessions,
       "alPptpStatsActiveSessions": alPptpStatsActiveSessions,
       "alPptpStatsMaxSessions": alPptpStatsMaxSessions,
       "alPptpStatsControlRecvOctets": alPptpStatsControlRecvOctets,
       "alPptpStatsControlRecvPackets": alPptpStatsControlRecvPackets,
       "alPptpStatsControlRecvDiscards": alPptpStatsControlRecvDiscards,
       "alPptpStatsControlSendOctets": alPptpStatsControlSendOctets,
       "alPptpStatsControlSendPackets": alPptpStatsControlSendPackets,
       "alPptpStatsPayloadRecvOctets": alPptpStatsPayloadRecvOctets,
       "alPptpStatsPayloadRecvPackets": alPptpStatsPayloadRecvPackets,
       "alPptpStatsPayloadRecvDiscards": alPptpStatsPayloadRecvDiscards,
       "alPptpStatsPayloadSendOctets": alPptpStatsPayloadSendOctets,
       "alPptpStatsPayloadSendPackets": alPptpStatsPayloadSendPackets,
       "alPptpStatsTunnelTable": alPptpStatsTunnelTable,
       "alPptpStatsTunnelEntry": alPptpStatsTunnelEntry,
       "alPptpStatsTunnelRowStatus": alPptpStatsTunnelRowStatus,
       "alPptpStatsTunnelPeerIpAddr": alPptpStatsTunnelPeerIpAddr,
       "alPptpStatsTunnelDatastreamId": alPptpStatsTunnelDatastreamId,
       "alPptpStatsTunnelLocalIpAddr": alPptpStatsTunnelLocalIpAddr,
       "alPptpStatsTunnelPeerHostName": alPptpStatsTunnelPeerHostName,
       "alPptpStatsTunnelPeerVendorName": alPptpStatsTunnelPeerVendorName,
       "alPptpStatsTunnelPeerFirmwareRev": alPptpStatsTunnelPeerFirmwareRev,
       "alPptpStatsTunnelPeerProtVers": alPptpStatsTunnelPeerProtVers,
       "alPptpStatsTunnelPeerFramingCap": alPptpStatsTunnelPeerFramingCap,
       "alPptpStatsTunnelPeerBearerCap": alPptpStatsTunnelPeerBearerCap,
       "alPptpStatsTunnelPeerMaxChan": alPptpStatsTunnelPeerMaxChan,
       "alPptpStatsTunnelActiveSessions": alPptpStatsTunnelActiveSessions,
       "alPptpStatsSessionTable": alPptpStatsSessionTable,
       "alPptpStatsSessionEntry": alPptpStatsSessionEntry,
       "alPptpStatsSessionRowStatus": alPptpStatsSessionRowStatus,
       "alPptpStatsSessionDatastreamId": alPptpStatsSessionDatastreamId,
       "alPptpStatsSessionLocalCallId": alPptpStatsSessionLocalCallId,
       "alPptpStatsSessionPeerCallId": alPptpStatsSessionPeerCallId,
       "alPptpStatsSessionUserName": alPptpStatsSessionUserName,
       "alPptpStatsSessionSerial": alPptpStatsSessionSerial,
       "alPptpStatsSessionMinimumSpeed": alPptpStatsSessionMinimumSpeed,
       "alPptpStatsSessionMaximumSpeed": alPptpStatsSessionMaximumSpeed,
       "alPptpStatsSessionConnectSpeed": alPptpStatsSessionConnectSpeed,
       "alPptpStatsSessionBearerType": alPptpStatsSessionBearerType,
       "alPptpStatsSessionFramingType": alPptpStatsSessionFramingType,
       "alPptpStatsSessionPhysicalChannel": alPptpStatsSessionPhysicalChannel,
       "alPptpStatsSessionLocalWindowSize": alPptpStatsSessionLocalWindowSize,
       "alPptpStatsSessionPeerWindowSize": alPptpStatsSessionPeerWindowSize,
       "alPptpStatsSessionLocalPpd": alPptpStatsSessionLocalPpd,
       "alPptpStatsSessionPeerPpd": alPptpStatsSessionPeerPpd,
       "alPptpStatsSessionRecvOctets": alPptpStatsSessionRecvOctets,
       "alPptpStatsSessionRecvPackets": alPptpStatsSessionRecvPackets,
       "alPptpStatsSessionRecvDiscards": alPptpStatsSessionRecvDiscards,
       "alPptpStatsSessionRecvZLB": alPptpStatsSessionRecvZLB,
       "alPptpStatsSessionSendOctets": alPptpStatsSessionSendOctets,
       "alPptpStatsSessionSendPackets": alPptpStatsSessionSendPackets,
       "alPptpStatsSessionSendZLB": alPptpStatsSessionSendZLB,
       "alPptpStatsSessionAckTimeouts": alPptpStatsSessionAckTimeouts,
       "alPptpStatsSessionLocalFlowOff": alPptpStatsSessionLocalFlowOff,
       "alPptpStatsSessionPeerFlowOff": alPptpStatsSessionPeerFlowOff,
       "alPptpStatsSessionOutOfWindow": alPptpStatsSessionOutOfWindow,
       "alPptpStatsSessionOutOfSequence": alPptpStatsSessionOutOfSequence,
       "alPptpStatsSessionTunnelPeerIpAddr": alPptpStatsSessionTunnelPeerIpAddr}
)
