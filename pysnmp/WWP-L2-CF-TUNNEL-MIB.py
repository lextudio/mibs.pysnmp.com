# SNMP MIB module (WWP-L2-CF-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-L2-CF-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:43 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpL2CFTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53)
)
wwpL2CFTunnelMIB.setRevisions(
        ("2005-03-08 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpL2CFTunnelMIBObjects_ObjectIdentity = ObjectIdentity
wwpL2CFTunnelMIBObjects = _WwpL2CFTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1)
)
_WwpL2CFTunnel_ObjectIdentity = ObjectIdentity
wwpL2CFTunnel = _WwpL2CFTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1)
)
_WwpL2CFTunnelTable_Object = MibTable
wwpL2CFTunnelTable = _WwpL2CFTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpL2CFTunnelTable.setStatus("current")
_WwpL2CFTunnelEntry_Object = MibTableRow
wwpL2CFTunnelEntry = _WwpL2CFTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 1, 1)
)
wwpL2CFTunnelEntry.setIndexNames(
    (0, "WWP-L2-CF-TUNNEL-MIB", "wwpL2CFTunnelVlanId"),
)
if mibBuilder.loadTexts:
    wwpL2CFTunnelEntry.setStatus("current")
_WwpL2CFTunnelVlanId_Type = VlanId
_WwpL2CFTunnelVlanId_Object = MibTableColumn
wwpL2CFTunnelVlanId = _WwpL2CFTunnelVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 1, 1, 1),
    _WwpL2CFTunnelVlanId_Type()
)
wwpL2CFTunnelVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTunnelVlanId.setStatus("current")


class _WwpL2CFTunnelOperStatus_Type(Integer32):
    """Custom type wwpL2CFTunnelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("operActive", 0),
          ("operDisabled", 5),
          ("operInvalidCfg", 4),
          ("operInvalidVlanNumPorts", 3),
          ("operInvalidVlanPortTag", 2),
          ("operVlanNotExist", 1))
    )


_WwpL2CFTunnelOperStatus_Type.__name__ = "Integer32"
_WwpL2CFTunnelOperStatus_Object = MibTableColumn
wwpL2CFTunnelOperStatus = _WwpL2CFTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 1, 1, 2),
    _WwpL2CFTunnelOperStatus_Type()
)
wwpL2CFTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTunnelOperStatus.setStatus("current")


class _WwpL2CFTunnelAdminStatus_Type(Integer32):
    """Custom type wwpL2CFTunnelAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WwpL2CFTunnelAdminStatus_Type.__name__ = "Integer32"
_WwpL2CFTunnelAdminStatus_Object = MibTableColumn
wwpL2CFTunnelAdminStatus = _WwpL2CFTunnelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 1, 1, 3),
    _WwpL2CFTunnelAdminStatus_Type()
)
wwpL2CFTunnelAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpL2CFTunnelAdminStatus.setStatus("current")


class _WwpL2CFTunnelPriority_Type(Integer32):
    """Custom type wwpL2CFTunnelPriority based on Integer32"""
    defaultValue = 6

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
              7)
        )
    )
    namedValues = NamedValues(
        *(("p0", 0),
          ("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("p5", 5),
          ("p6", 6),
          ("p7", 7))
    )


_WwpL2CFTunnelPriority_Type.__name__ = "Integer32"
_WwpL2CFTunnelPriority_Object = MibTableColumn
wwpL2CFTunnelPriority = _WwpL2CFTunnelPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 1, 1, 4),
    _WwpL2CFTunnelPriority_Type()
)
wwpL2CFTunnelPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpL2CFTunnelPriority.setStatus("current")
_WwpL2CFTunnelRowStatus_Type = RowStatus
_WwpL2CFTunnelRowStatus_Object = MibTableColumn
wwpL2CFTunnelRowStatus = _WwpL2CFTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 1, 1, 5),
    _WwpL2CFTunnelRowStatus_Type()
)
wwpL2CFTunnelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpL2CFTunnelRowStatus.setStatus("current")
_WwpL2CFTProtocolTable_Object = MibTable
wwpL2CFTProtocolTable = _WwpL2CFTProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpL2CFTProtocolTable.setStatus("current")
_WwpL2CFTProtocolEntry_Object = MibTableRow
wwpL2CFTProtocolEntry = _WwpL2CFTProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 2, 1)
)
wwpL2CFTProtocolEntry.setIndexNames(
    (0, "WWP-L2-CF-TUNNEL-MIB", "wwpL2CFTVlanId"),
    (0, "WWP-L2-CF-TUNNEL-MIB", "wwpL2CFTProtocolNum"),
)
if mibBuilder.loadTexts:
    wwpL2CFTProtocolEntry.setStatus("current")
_WwpL2CFTVlanId_Type = VlanId
_WwpL2CFTVlanId_Object = MibTableColumn
wwpL2CFTVlanId = _WwpL2CFTVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 2, 1, 1),
    _WwpL2CFTVlanId_Type()
)
wwpL2CFTVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTVlanId.setStatus("current")


class _WwpL2CFTProtocolNum_Type(Integer32):
    """Custom type wwpL2CFTProtocolNum based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("bridge-grp-addr", 2),
          ("cdp", 3),
          ("dtp", 4),
          ("gvrp", 5),
          ("l28021x", 1),
          ("lacp", 6),
          ("lldp", 15),
          ("marker-protocol", 7),
          ("oam", 8),
          ("pagp", 9),
          ("pvst", 10),
          ("stp-uplink-fast", 11),
          ("udld", 12),
          ("vlanbridge", 13),
          ("vtp", 14))
    )


_WwpL2CFTProtocolNum_Type.__name__ = "Integer32"
_WwpL2CFTProtocolNum_Object = MibTableColumn
wwpL2CFTProtocolNum = _WwpL2CFTProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 2, 1, 2),
    _WwpL2CFTProtocolNum_Type()
)
wwpL2CFTProtocolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTProtocolNum.setStatus("current")


class _WwpL2CFTDispositionType_Type(Integer32):
    """Custom type wwpL2CFTDispositionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("peer", 1),
          ("tunnel", 2))
    )


_WwpL2CFTDispositionType_Type.__name__ = "Integer32"
_WwpL2CFTDispositionType_Object = MibTableColumn
wwpL2CFTDispositionType = _WwpL2CFTDispositionType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 2, 1, 3),
    _WwpL2CFTDispositionType_Type()
)
wwpL2CFTDispositionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpL2CFTDispositionType.setStatus("current")
_WwpL2CFTStatsTable_Object = MibTable
wwpL2CFTStatsTable = _WwpL2CFTStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpL2CFTStatsTable.setStatus("current")
_WwpL2CFTStatsEntry_Object = MibTableRow
wwpL2CFTStatsEntry = _WwpL2CFTStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3, 1)
)
wwpL2CFTStatsEntry.setIndexNames(
    (0, "WWP-L2-CF-TUNNEL-MIB", "wwpL2CFTStatsVlanId"),
    (0, "WWP-L2-CF-TUNNEL-MIB", "wwpL2CFTStatsProtocolNum"),
)
if mibBuilder.loadTexts:
    wwpL2CFTStatsEntry.setStatus("current")
_WwpL2CFTStatsVlanId_Type = VlanId
_WwpL2CFTStatsVlanId_Object = MibTableColumn
wwpL2CFTStatsVlanId = _WwpL2CFTStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3, 1, 1),
    _WwpL2CFTStatsVlanId_Type()
)
wwpL2CFTStatsVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTStatsVlanId.setStatus("current")


class _WwpL2CFTStatsProtocolNum_Type(Integer32):
    """Custom type wwpL2CFTStatsProtocolNum based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bridge-grp-addr", 2),
          ("cdp", 3),
          ("dtp", 4),
          ("gvrp", 5),
          ("l28021x", 1),
          ("lacp", 6),
          ("marker-protocol", 7),
          ("oam", 8),
          ("pagp", 9),
          ("pvst", 10),
          ("stp-uplink-fast", 11),
          ("udld", 12),
          ("vlanbridge", 13),
          ("vtp", 14))
    )


_WwpL2CFTStatsProtocolNum_Type.__name__ = "Integer32"
_WwpL2CFTStatsProtocolNum_Object = MibTableColumn
wwpL2CFTStatsProtocolNum = _WwpL2CFTStatsProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3, 1, 2),
    _WwpL2CFTStatsProtocolNum_Type()
)
wwpL2CFTStatsProtocolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTStatsProtocolNum.setStatus("current")
_WwpL2CFTStatsPacketsRx_Type = Counter32
_WwpL2CFTStatsPacketsRx_Object = MibTableColumn
wwpL2CFTStatsPacketsRx = _WwpL2CFTStatsPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3, 1, 3),
    _WwpL2CFTStatsPacketsRx_Type()
)
wwpL2CFTStatsPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTStatsPacketsRx.setStatus("current")
_WwpL2CFTStatsTunneledFrames_Type = Counter32
_WwpL2CFTStatsTunneledFrames_Object = MibTableColumn
wwpL2CFTStatsTunneledFrames = _WwpL2CFTStatsTunneledFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3, 1, 4),
    _WwpL2CFTStatsTunneledFrames_Type()
)
wwpL2CFTStatsTunneledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTStatsTunneledFrames.setStatus("current")
_WwpL2CFTStatsDecodedFrames_Type = Counter32
_WwpL2CFTStatsDecodedFrames_Object = MibTableColumn
wwpL2CFTStatsDecodedFrames = _WwpL2CFTStatsDecodedFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3, 1, 5),
    _WwpL2CFTStatsDecodedFrames_Type()
)
wwpL2CFTStatsDecodedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTStatsDecodedFrames.setStatus("current")
_WwpL2CFTStatsDecodedFailed_Type = Counter32
_WwpL2CFTStatsDecodedFailed_Object = MibTableColumn
wwpL2CFTStatsDecodedFailed = _WwpL2CFTStatsDecodedFailed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3, 1, 6),
    _WwpL2CFTStatsDecodedFailed_Type()
)
wwpL2CFTStatsDecodedFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTStatsDecodedFailed.setStatus("current")
_WwpL2CFTStatsPeeredFrames_Type = Counter32
_WwpL2CFTStatsPeeredFrames_Object = MibTableColumn
wwpL2CFTStatsPeeredFrames = _WwpL2CFTStatsPeeredFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3, 1, 7),
    _WwpL2CFTStatsPeeredFrames_Type()
)
wwpL2CFTStatsPeeredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTStatsPeeredFrames.setStatus("current")
_WwpL2CFTStatsDiscardFrames_Type = Counter32
_WwpL2CFTStatsDiscardFrames_Object = MibTableColumn
wwpL2CFTStatsDiscardFrames = _WwpL2CFTStatsDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3, 1, 8),
    _WwpL2CFTStatsDiscardFrames_Type()
)
wwpL2CFTStatsDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTStatsDiscardFrames.setStatus("current")
_WwpL2CFTStatsTunFrameSubPort_Type = Counter32
_WwpL2CFTStatsTunFrameSubPort_Object = MibTableColumn
wwpL2CFTStatsTunFrameSubPort = _WwpL2CFTStatsTunFrameSubPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 3, 1, 9),
    _WwpL2CFTStatsTunFrameSubPort_Type()
)
wwpL2CFTStatsTunFrameSubPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTStatsTunFrameSubPort.setStatus("current")
_WwpL2CFTGlobalStats_ObjectIdentity = ObjectIdentity
wwpL2CFTGlobalStats = _WwpL2CFTGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 4)
)
_WwpL2CFTGlobalStatsPacketsRx_Type = Counter32
_WwpL2CFTGlobalStatsPacketsRx_Object = MibScalar
wwpL2CFTGlobalStatsPacketsRx = _WwpL2CFTGlobalStatsPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 4, 1),
    _WwpL2CFTGlobalStatsPacketsRx_Type()
)
wwpL2CFTGlobalStatsPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTGlobalStatsPacketsRx.setStatus("current")
_WwpL2CFTGlobalStatsTunneledFrames_Type = Counter32
_WwpL2CFTGlobalStatsTunneledFrames_Object = MibScalar
wwpL2CFTGlobalStatsTunneledFrames = _WwpL2CFTGlobalStatsTunneledFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 4, 2),
    _WwpL2CFTGlobalStatsTunneledFrames_Type()
)
wwpL2CFTGlobalStatsTunneledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTGlobalStatsTunneledFrames.setStatus("current")
_WwpL2CFTGlobalStatsDecodedFrames_Type = Counter32
_WwpL2CFTGlobalStatsDecodedFrames_Object = MibScalar
wwpL2CFTGlobalStatsDecodedFrames = _WwpL2CFTGlobalStatsDecodedFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 4, 3),
    _WwpL2CFTGlobalStatsDecodedFrames_Type()
)
wwpL2CFTGlobalStatsDecodedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTGlobalStatsDecodedFrames.setStatus("current")
_WwpL2CFTGlobalStatsDecodedFailed_Type = Counter32
_WwpL2CFTGlobalStatsDecodedFailed_Object = MibScalar
wwpL2CFTGlobalStatsDecodedFailed = _WwpL2CFTGlobalStatsDecodedFailed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 4, 4),
    _WwpL2CFTGlobalStatsDecodedFailed_Type()
)
wwpL2CFTGlobalStatsDecodedFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTGlobalStatsDecodedFailed.setStatus("current")
_WwpL2CFTGlobalStatsPeeredFrames_Type = Counter32
_WwpL2CFTGlobalStatsPeeredFrames_Object = MibScalar
wwpL2CFTGlobalStatsPeeredFrames = _WwpL2CFTGlobalStatsPeeredFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 4, 5),
    _WwpL2CFTGlobalStatsPeeredFrames_Type()
)
wwpL2CFTGlobalStatsPeeredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTGlobalStatsPeeredFrames.setStatus("current")
_WwpL2CFTGlobalStatsDiscardFrames_Type = Counter32
_WwpL2CFTGlobalStatsDiscardFrames_Object = MibScalar
wwpL2CFTGlobalStatsDiscardFrames = _WwpL2CFTGlobalStatsDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 4, 6),
    _WwpL2CFTGlobalStatsDiscardFrames_Type()
)
wwpL2CFTGlobalStatsDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTGlobalStatsDiscardFrames.setStatus("current")
_WwpL2CFTGlobalStatsTunFrameSubPort_Type = Counter32
_WwpL2CFTGlobalStatsTunFrameSubPort_Object = MibScalar
wwpL2CFTGlobalStatsTunFrameSubPort = _WwpL2CFTGlobalStatsTunFrameSubPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 4, 7),
    _WwpL2CFTGlobalStatsTunFrameSubPort_Type()
)
wwpL2CFTGlobalStatsTunFrameSubPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpL2CFTGlobalStatsTunFrameSubPort.setStatus("current")


class _WwpL2CFTResetStatCounters_Type(Integer32):
    """Custom type wwpL2CFTResetStatCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_WwpL2CFTResetStatCounters_Type.__name__ = "Integer32"
_WwpL2CFTResetStatCounters_Object = MibScalar
wwpL2CFTResetStatCounters = _WwpL2CFTResetStatCounters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 1, 1, 5),
    _WwpL2CFTResetStatCounters_Type()
)
wwpL2CFTResetStatCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpL2CFTResetStatCounters.setStatus("current")
_WwpL2CFTunnelMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpL2CFTunnelMIBNotificationPrefix = _WwpL2CFTunnelMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 2)
)
_WwpL2CFTunnelMIBNotifications_ObjectIdentity = ObjectIdentity
wwpL2CFTunnelMIBNotifications = _WwpL2CFTunnelMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 2, 0)
)
_WwpL2CFTunnelMIBConformance_ObjectIdentity = ObjectIdentity
wwpL2CFTunnelMIBConformance = _WwpL2CFTunnelMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 3)
)
_WwpL2CFTunnelMIBCompliances_ObjectIdentity = ObjectIdentity
wwpL2CFTunnelMIBCompliances = _WwpL2CFTunnelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 3, 1)
)
_WwpL2CFTunnelMIBGroups_ObjectIdentity = ObjectIdentity
wwpL2CFTunnelMIBGroups = _WwpL2CFTunnelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 53, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-L2-CF-TUNNEL-MIB",
    **{"VlanId": VlanId,
       "wwpL2CFTunnelMIB": wwpL2CFTunnelMIB,
       "wwpL2CFTunnelMIBObjects": wwpL2CFTunnelMIBObjects,
       "wwpL2CFTunnel": wwpL2CFTunnel,
       "wwpL2CFTunnelTable": wwpL2CFTunnelTable,
       "wwpL2CFTunnelEntry": wwpL2CFTunnelEntry,
       "wwpL2CFTunnelVlanId": wwpL2CFTunnelVlanId,
       "wwpL2CFTunnelOperStatus": wwpL2CFTunnelOperStatus,
       "wwpL2CFTunnelAdminStatus": wwpL2CFTunnelAdminStatus,
       "wwpL2CFTunnelPriority": wwpL2CFTunnelPriority,
       "wwpL2CFTunnelRowStatus": wwpL2CFTunnelRowStatus,
       "wwpL2CFTProtocolTable": wwpL2CFTProtocolTable,
       "wwpL2CFTProtocolEntry": wwpL2CFTProtocolEntry,
       "wwpL2CFTVlanId": wwpL2CFTVlanId,
       "wwpL2CFTProtocolNum": wwpL2CFTProtocolNum,
       "wwpL2CFTDispositionType": wwpL2CFTDispositionType,
       "wwpL2CFTStatsTable": wwpL2CFTStatsTable,
       "wwpL2CFTStatsEntry": wwpL2CFTStatsEntry,
       "wwpL2CFTStatsVlanId": wwpL2CFTStatsVlanId,
       "wwpL2CFTStatsProtocolNum": wwpL2CFTStatsProtocolNum,
       "wwpL2CFTStatsPacketsRx": wwpL2CFTStatsPacketsRx,
       "wwpL2CFTStatsTunneledFrames": wwpL2CFTStatsTunneledFrames,
       "wwpL2CFTStatsDecodedFrames": wwpL2CFTStatsDecodedFrames,
       "wwpL2CFTStatsDecodedFailed": wwpL2CFTStatsDecodedFailed,
       "wwpL2CFTStatsPeeredFrames": wwpL2CFTStatsPeeredFrames,
       "wwpL2CFTStatsDiscardFrames": wwpL2CFTStatsDiscardFrames,
       "wwpL2CFTStatsTunFrameSubPort": wwpL2CFTStatsTunFrameSubPort,
       "wwpL2CFTGlobalStats": wwpL2CFTGlobalStats,
       "wwpL2CFTGlobalStatsPacketsRx": wwpL2CFTGlobalStatsPacketsRx,
       "wwpL2CFTGlobalStatsTunneledFrames": wwpL2CFTGlobalStatsTunneledFrames,
       "wwpL2CFTGlobalStatsDecodedFrames": wwpL2CFTGlobalStatsDecodedFrames,
       "wwpL2CFTGlobalStatsDecodedFailed": wwpL2CFTGlobalStatsDecodedFailed,
       "wwpL2CFTGlobalStatsPeeredFrames": wwpL2CFTGlobalStatsPeeredFrames,
       "wwpL2CFTGlobalStatsDiscardFrames": wwpL2CFTGlobalStatsDiscardFrames,
       "wwpL2CFTGlobalStatsTunFrameSubPort": wwpL2CFTGlobalStatsTunFrameSubPort,
       "wwpL2CFTResetStatCounters": wwpL2CFTResetStatCounters,
       "wwpL2CFTunnelMIBNotificationPrefix": wwpL2CFTunnelMIBNotificationPrefix,
       "wwpL2CFTunnelMIBNotifications": wwpL2CFTunnelMIBNotifications,
       "wwpL2CFTunnelMIBConformance": wwpL2CFTunnelMIBConformance,
       "wwpL2CFTunnelMIBCompliances": wwpL2CFTunnelMIBCompliances,
       "wwpL2CFTunnelMIBGroups": wwpL2CFTunnelMIBGroups}
)
