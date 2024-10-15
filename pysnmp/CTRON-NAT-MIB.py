# SNMP MIB module (CTRON-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:03 2024
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

(nwIpClientServices,
 nwIpComponents,
 nwIpMibs,
 nwIpRouter) = mibBuilder.importSymbols(
    "CTRON-IP-ROUTER-MIB",
    "nwIpClientServices",
    "nwIpComponents",
    "nwIpMibs",
    "nwIpRouter")

(nwRtrProtoSuites,) = mibBuilder.importSymbols(
    "ROUTER-OIDS",
    "nwRtrProtoSuites")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtNat_ObjectIdentity = ObjectIdentity
ctNat = _CtNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1)
)
_CtNatConfigGroup_ObjectIdentity = ObjectIdentity
ctNatConfigGroup = _CtNatConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1)
)
_CtNatPublicIfIndex_Type = Integer32
_CtNatPublicIfIndex_Object = MibScalar
ctNatPublicIfIndex = _CtNatPublicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 1),
    _CtNatPublicIfIndex_Type()
)
ctNatPublicIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctNatPublicIfIndex.setStatus("mandatory")
_CtNatPublicIP_Type = IpAddress
_CtNatPublicIP_Object = MibScalar
ctNatPublicIP = _CtNatPublicIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 2),
    _CtNatPublicIP_Type()
)
ctNatPublicIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatPublicIP.setStatus("mandatory")
_CtNatPublicMask_Type = IpAddress
_CtNatPublicMask_Object = MibScalar
ctNatPublicMask = _CtNatPublicMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 3),
    _CtNatPublicMask_Type()
)
ctNatPublicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatPublicMask.setStatus("mandatory")
_CtNatMaxConn_Type = Integer32
_CtNatMaxConn_Object = MibScalar
ctNatMaxConn = _CtNatMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 4),
    _CtNatMaxConn_Type()
)
ctNatMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctNatMaxConn.setStatus("mandatory")
_CtNatTcpTimeout_Type = Integer32
_CtNatTcpTimeout_Object = MibScalar
ctNatTcpTimeout = _CtNatTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 5),
    _CtNatTcpTimeout_Type()
)
ctNatTcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctNatTcpTimeout.setStatus("mandatory")
_CtNatUdpTimeout_Type = Integer32
_CtNatUdpTimeout_Object = MibScalar
ctNatUdpTimeout = _CtNatUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 6),
    _CtNatUdpTimeout_Type()
)
ctNatUdpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctNatUdpTimeout.setStatus("mandatory")
_CtNatPktsL2I_Type = Counter32
_CtNatPktsL2I_Object = MibScalar
ctNatPktsL2I = _CtNatPktsL2I_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 7),
    _CtNatPktsL2I_Type()
)
ctNatPktsL2I.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatPktsL2I.setStatus("mandatory")
_CtNatPktsI2L_Type = Counter32
_CtNatPktsI2L_Object = MibScalar
ctNatPktsI2L = _CtNatPktsI2L_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 8),
    _CtNatPktsI2L_Type()
)
ctNatPktsI2L.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatPktsI2L.setStatus("mandatory")
_CtNatBytesL2I_Type = Counter32
_CtNatBytesL2I_Object = MibScalar
ctNatBytesL2I = _CtNatBytesL2I_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 9),
    _CtNatBytesL2I_Type()
)
ctNatBytesL2I.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatBytesL2I.setStatus("mandatory")
_CtNatBytesI2L_Type = Counter32
_CtNatBytesI2L_Object = MibScalar
ctNatBytesI2L = _CtNatBytesI2L_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 10),
    _CtNatBytesI2L_Type()
)
ctNatBytesI2L.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatBytesI2L.setStatus("mandatory")
_CtNatTcpConn_Type = Integer32
_CtNatTcpConn_Object = MibScalar
ctNatTcpConn = _CtNatTcpConn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 11),
    _CtNatTcpConn_Type()
)
ctNatTcpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatTcpConn.setStatus("mandatory")
_CtNatUdpConn_Type = Integer32
_CtNatUdpConn_Object = MibScalar
ctNatUdpConn = _CtNatUdpConn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 12),
    _CtNatUdpConn_Type()
)
ctNatUdpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatUdpConn.setStatus("mandatory")
_CtNatIcmpConn_Type = Integer32
_CtNatIcmpConn_Object = MibScalar
ctNatIcmpConn = _CtNatIcmpConn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 13),
    _CtNatIcmpConn_Type()
)
ctNatIcmpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatIcmpConn.setStatus("mandatory")
_CtNatRetries_Type = Counter32
_CtNatRetries_Object = MibScalar
ctNatRetries = _CtNatRetries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 14),
    _CtNatRetries_Type()
)
ctNatRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatRetries.setStatus("mandatory")
_CtNatBadSums_Type = Counter32
_CtNatBadSums_Object = MibScalar
ctNatBadSums = _CtNatBadSums_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 15),
    _CtNatBadSums_Type()
)
ctNatBadSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatBadSums.setStatus("mandatory")
_CtNatTotalPkts_Type = Counter32
_CtNatTotalPkts_Object = MibScalar
ctNatTotalPkts = _CtNatTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 16),
    _CtNatTotalPkts_Type()
)
ctNatTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatTotalPkts.setStatus("mandatory")
_CtNatBadPkts_Type = Counter32
_CtNatBadPkts_Object = MibScalar
ctNatBadPkts = _CtNatBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 17),
    _CtNatBadPkts_Type()
)
ctNatBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatBadPkts.setStatus("mandatory")
_CtNatResPkts_Type = Counter32
_CtNatResPkts_Object = MibScalar
ctNatResPkts = _CtNatResPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 18),
    _CtNatResPkts_Type()
)
ctNatResPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatResPkts.setStatus("mandatory")
_CtNatTotTcpConn_Type = Counter32
_CtNatTotTcpConn_Object = MibScalar
ctNatTotTcpConn = _CtNatTotTcpConn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 19),
    _CtNatTotTcpConn_Type()
)
ctNatTotTcpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatTotTcpConn.setStatus("mandatory")
_CtNatTotUdpConn_Type = Counter32
_CtNatTotUdpConn_Object = MibScalar
ctNatTotUdpConn = _CtNatTotUdpConn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 20),
    _CtNatTotUdpConn_Type()
)
ctNatTotUdpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatTotUdpConn.setStatus("mandatory")
_CtNatTotIcmpConn_Type = Counter32
_CtNatTotIcmpConn_Object = MibScalar
ctNatTotIcmpConn = _CtNatTotIcmpConn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 21),
    _CtNatTotIcmpConn_Type()
)
ctNatTotIcmpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatTotIcmpConn.setStatus("mandatory")
_CtNatConfigTable_Object = MibTable
ctNatConfigTable = _CtNatConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22)
)
if mibBuilder.loadTexts:
    ctNatConfigTable.setStatus("mandatory")
_CtNatConfigEntry_Object = MibTableRow
ctNatConfigEntry = _CtNatConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1)
)
ctNatConfigEntry.setIndexNames(
    (0, "CTRON-NAT-MIB", "ctNatConfigId"),
)
if mibBuilder.loadTexts:
    ctNatConfigEntry.setStatus("mandatory")
_CtNatConfigId_Type = Integer32
_CtNatConfigId_Object = MibTableColumn
ctNatConfigId = _CtNatConfigId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 1),
    _CtNatConfigId_Type()
)
ctNatConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConfigId.setStatus("mandatory")


class _CtNatAdminStatus_Type(Integer32):
    """Custom type ctNatAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CtNatAdminStatus_Type.__name__ = "Integer32"
_CtNatAdminStatus_Object = MibTableColumn
ctNatAdminStatus = _CtNatAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 2),
    _CtNatAdminStatus_Type()
)
ctNatAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctNatAdminStatus.setStatus("mandatory")


class _CtNatOperStatus_Type(Integer32):
    """Custom type ctNatOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("invalid-config", 3))
    )


_CtNatOperStatus_Type.__name__ = "Integer32"
_CtNatOperStatus_Object = MibTableColumn
ctNatOperStatus = _CtNatOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 3),
    _CtNatOperStatus_Type()
)
ctNatOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatOperStatus.setStatus("mandatory")
_CtNatLocalIfIndex_Type = Integer32
_CtNatLocalIfIndex_Object = MibTableColumn
ctNatLocalIfIndex = _CtNatLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 4),
    _CtNatLocalIfIndex_Type()
)
ctNatLocalIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctNatLocalIfIndex.setStatus("mandatory")
_CtNatLocalIP_Type = IpAddress
_CtNatLocalIP_Object = MibTableColumn
ctNatLocalIP = _CtNatLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 5),
    _CtNatLocalIP_Type()
)
ctNatLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatLocalIP.setStatus("mandatory")
_CtNatLocalMask_Type = IpAddress
_CtNatLocalMask_Object = MibTableColumn
ctNatLocalMask = _CtNatLocalMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 6),
    _CtNatLocalMask_Type()
)
ctNatLocalMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatLocalMask.setStatus("mandatory")
_CtNatServerGroup_ObjectIdentity = ObjectIdentity
ctNatServerGroup = _CtNatServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2)
)
_CtNatTotServerEntries_Type = Integer32
_CtNatTotServerEntries_Object = MibScalar
ctNatTotServerEntries = _CtNatTotServerEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 1),
    _CtNatTotServerEntries_Type()
)
ctNatTotServerEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatTotServerEntries.setStatus("mandatory")
_CtNatServerListTable_Object = MibTable
ctNatServerListTable = _CtNatServerListTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ctNatServerListTable.setStatus("mandatory")
_CtNatServerListEntry_Object = MibTableRow
ctNatServerListEntry = _CtNatServerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2, 1)
)
ctNatServerListEntry.setIndexNames(
    (0, "CTRON-NAT-MIB", "ctNatServerId"),
)
if mibBuilder.loadTexts:
    ctNatServerListEntry.setStatus("mandatory")
_CtNatServerId_Type = Integer32
_CtNatServerId_Object = MibTableColumn
ctNatServerId = _CtNatServerId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2, 1, 1),
    _CtNatServerId_Type()
)
ctNatServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatServerId.setStatus("mandatory")
_CtNatProxyServer_Type = OctetString
_CtNatProxyServer_Object = MibTableColumn
ctNatProxyServer = _CtNatProxyServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2, 1, 2),
    _CtNatProxyServer_Type()
)
ctNatProxyServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctNatProxyServer.setStatus("mandatory")
_CtNatConnStatsGroup_ObjectIdentity = ObjectIdentity
ctNatConnStatsGroup = _CtNatConnStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3)
)
_CtNatTotActiveConn_Type = Integer32
_CtNatTotActiveConn_Object = MibScalar
ctNatTotActiveConn = _CtNatTotActiveConn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 1),
    _CtNatTotActiveConn_Type()
)
ctNatTotActiveConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatTotActiveConn.setStatus("mandatory")
_CtNatConnStatsTable_Object = MibTable
ctNatConnStatsTable = _CtNatConnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ctNatConnStatsTable.setStatus("mandatory")
_CtNatConnStatsEntry_Object = MibTableRow
ctNatConnStatsEntry = _CtNatConnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1)
)
ctNatConnStatsEntry.setIndexNames(
    (0, "CTRON-NAT-MIB", "ctNatConnStatsID"),
)
if mibBuilder.loadTexts:
    ctNatConnStatsEntry.setStatus("mandatory")
_CtNatConnStatsID_Type = Integer32
_CtNatConnStatsID_Object = MibTableColumn
ctNatConnStatsID = _CtNatConnStatsID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 1),
    _CtNatConnStatsID_Type()
)
ctNatConnStatsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsID.setStatus("mandatory")
_CtNatConnStatsForeignIP_Type = IpAddress
_CtNatConnStatsForeignIP_Object = MibTableColumn
ctNatConnStatsForeignIP = _CtNatConnStatsForeignIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 2),
    _CtNatConnStatsForeignIP_Type()
)
ctNatConnStatsForeignIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsForeignIP.setStatus("mandatory")
_CtNatConnStatsLocalIP_Type = IpAddress
_CtNatConnStatsLocalIP_Object = MibTableColumn
ctNatConnStatsLocalIP = _CtNatConnStatsLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 3),
    _CtNatConnStatsLocalIP_Type()
)
ctNatConnStatsLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsLocalIP.setStatus("mandatory")
_CtNatConnStatsPublicPort_Type = Integer32
_CtNatConnStatsPublicPort_Object = MibTableColumn
ctNatConnStatsPublicPort = _CtNatConnStatsPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 4),
    _CtNatConnStatsPublicPort_Type()
)
ctNatConnStatsPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsPublicPort.setStatus("mandatory")
_CtNatConnStatsLocalPort_Type = Integer32
_CtNatConnStatsLocalPort_Object = MibTableColumn
ctNatConnStatsLocalPort = _CtNatConnStatsLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 5),
    _CtNatConnStatsLocalPort_Type()
)
ctNatConnStatsLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsLocalPort.setStatus("mandatory")
_CtNatConnStatsForeignPort_Type = Integer32
_CtNatConnStatsForeignPort_Object = MibTableColumn
ctNatConnStatsForeignPort = _CtNatConnStatsForeignPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 6),
    _CtNatConnStatsForeignPort_Type()
)
ctNatConnStatsForeignPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsForeignPort.setStatus("mandatory")
_CtNatConnStatsOutgoingPkts_Type = Counter32
_CtNatConnStatsOutgoingPkts_Object = MibTableColumn
ctNatConnStatsOutgoingPkts = _CtNatConnStatsOutgoingPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 7),
    _CtNatConnStatsOutgoingPkts_Type()
)
ctNatConnStatsOutgoingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsOutgoingPkts.setStatus("mandatory")
_CtNatConnStatsOutgoingBytes_Type = Counter32
_CtNatConnStatsOutgoingBytes_Object = MibTableColumn
ctNatConnStatsOutgoingBytes = _CtNatConnStatsOutgoingBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 8),
    _CtNatConnStatsOutgoingBytes_Type()
)
ctNatConnStatsOutgoingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsOutgoingBytes.setStatus("mandatory")
_CtNatConnStatsIncomingPkts_Type = Counter32
_CtNatConnStatsIncomingPkts_Object = MibTableColumn
ctNatConnStatsIncomingPkts = _CtNatConnStatsIncomingPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 9),
    _CtNatConnStatsIncomingPkts_Type()
)
ctNatConnStatsIncomingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsIncomingPkts.setStatus("mandatory")
_CtNatConnStatsIncomingBytes_Type = Counter32
_CtNatConnStatsIncomingBytes_Object = MibTableColumn
ctNatConnStatsIncomingBytes = _CtNatConnStatsIncomingBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 10),
    _CtNatConnStatsIncomingBytes_Type()
)
ctNatConnStatsIncomingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsIncomingBytes.setStatus("mandatory")
_CtNatConnStatsTimeSinceUse_Type = Integer32
_CtNatConnStatsTimeSinceUse_Object = MibTableColumn
ctNatConnStatsTimeSinceUse = _CtNatConnStatsTimeSinceUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 11),
    _CtNatConnStatsTimeSinceUse_Type()
)
ctNatConnStatsTimeSinceUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsTimeSinceUse.setStatus("mandatory")
_CtNatConnStatsProtocol_Type = Integer32
_CtNatConnStatsProtocol_Object = MibTableColumn
ctNatConnStatsProtocol = _CtNatConnStatsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 12),
    _CtNatConnStatsProtocol_Type()
)
ctNatConnStatsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsProtocol.setStatus("mandatory")
_CtNatConnStatsTCPSeq_Type = Integer32
_CtNatConnStatsTCPSeq_Object = MibTableColumn
ctNatConnStatsTCPSeq = _CtNatConnStatsTCPSeq_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 13),
    _CtNatConnStatsTCPSeq_Type()
)
ctNatConnStatsTCPSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsTCPSeq.setStatus("mandatory")
_CtNatConnStatsTCPAck_Type = Integer32
_CtNatConnStatsTCPAck_Object = MibTableColumn
ctNatConnStatsTCPAck = _CtNatConnStatsTCPAck_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 14),
    _CtNatConnStatsTCPAck_Type()
)
ctNatConnStatsTCPAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsTCPAck.setStatus("mandatory")
_CtNatConnStatsTCPState_Type = Integer32
_CtNatConnStatsTCPState_Object = MibTableColumn
ctNatConnStatsTCPState = _CtNatConnStatsTCPState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 15),
    _CtNatConnStatsTCPState_Type()
)
ctNatConnStatsTCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsTCPState.setStatus("mandatory")
_CtNatConnStatsLocalRetrys_Type = Counter32
_CtNatConnStatsLocalRetrys_Object = MibTableColumn
ctNatConnStatsLocalRetrys = _CtNatConnStatsLocalRetrys_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 16),
    _CtNatConnStatsLocalRetrys_Type()
)
ctNatConnStatsLocalRetrys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsLocalRetrys.setStatus("mandatory")
_CtNatConnStatsForeignRetrys_Type = Counter32
_CtNatConnStatsForeignRetrys_Object = MibTableColumn
ctNatConnStatsForeignRetrys = _CtNatConnStatsForeignRetrys_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 17),
    _CtNatConnStatsForeignRetrys_Type()
)
ctNatConnStatsForeignRetrys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsForeignRetrys.setStatus("mandatory")
_CtNatConnStatsLocalChecksum_Type = Counter32
_CtNatConnStatsLocalChecksum_Object = MibTableColumn
ctNatConnStatsLocalChecksum = _CtNatConnStatsLocalChecksum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 18),
    _CtNatConnStatsLocalChecksum_Type()
)
ctNatConnStatsLocalChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsLocalChecksum.setStatus("mandatory")
_CtNatConnStatsForeignChecksum_Type = Counter32
_CtNatConnStatsForeignChecksum_Object = MibTableColumn
ctNatConnStatsForeignChecksum = _CtNatConnStatsForeignChecksum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 19),
    _CtNatConnStatsForeignChecksum_Type()
)
ctNatConnStatsForeignChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctNatConnStatsForeignChecksum.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-NAT-MIB",
    **{"ctNat": ctNat,
       "ctNatConfigGroup": ctNatConfigGroup,
       "ctNatPublicIfIndex": ctNatPublicIfIndex,
       "ctNatPublicIP": ctNatPublicIP,
       "ctNatPublicMask": ctNatPublicMask,
       "ctNatMaxConn": ctNatMaxConn,
       "ctNatTcpTimeout": ctNatTcpTimeout,
       "ctNatUdpTimeout": ctNatUdpTimeout,
       "ctNatPktsL2I": ctNatPktsL2I,
       "ctNatPktsI2L": ctNatPktsI2L,
       "ctNatBytesL2I": ctNatBytesL2I,
       "ctNatBytesI2L": ctNatBytesI2L,
       "ctNatTcpConn": ctNatTcpConn,
       "ctNatUdpConn": ctNatUdpConn,
       "ctNatIcmpConn": ctNatIcmpConn,
       "ctNatRetries": ctNatRetries,
       "ctNatBadSums": ctNatBadSums,
       "ctNatTotalPkts": ctNatTotalPkts,
       "ctNatBadPkts": ctNatBadPkts,
       "ctNatResPkts": ctNatResPkts,
       "ctNatTotTcpConn": ctNatTotTcpConn,
       "ctNatTotUdpConn": ctNatTotUdpConn,
       "ctNatTotIcmpConn": ctNatTotIcmpConn,
       "ctNatConfigTable": ctNatConfigTable,
       "ctNatConfigEntry": ctNatConfigEntry,
       "ctNatConfigId": ctNatConfigId,
       "ctNatAdminStatus": ctNatAdminStatus,
       "ctNatOperStatus": ctNatOperStatus,
       "ctNatLocalIfIndex": ctNatLocalIfIndex,
       "ctNatLocalIP": ctNatLocalIP,
       "ctNatLocalMask": ctNatLocalMask,
       "ctNatServerGroup": ctNatServerGroup,
       "ctNatTotServerEntries": ctNatTotServerEntries,
       "ctNatServerListTable": ctNatServerListTable,
       "ctNatServerListEntry": ctNatServerListEntry,
       "ctNatServerId": ctNatServerId,
       "ctNatProxyServer": ctNatProxyServer,
       "ctNatConnStatsGroup": ctNatConnStatsGroup,
       "ctNatTotActiveConn": ctNatTotActiveConn,
       "ctNatConnStatsTable": ctNatConnStatsTable,
       "ctNatConnStatsEntry": ctNatConnStatsEntry,
       "ctNatConnStatsID": ctNatConnStatsID,
       "ctNatConnStatsForeignIP": ctNatConnStatsForeignIP,
       "ctNatConnStatsLocalIP": ctNatConnStatsLocalIP,
       "ctNatConnStatsPublicPort": ctNatConnStatsPublicPort,
       "ctNatConnStatsLocalPort": ctNatConnStatsLocalPort,
       "ctNatConnStatsForeignPort": ctNatConnStatsForeignPort,
       "ctNatConnStatsOutgoingPkts": ctNatConnStatsOutgoingPkts,
       "ctNatConnStatsOutgoingBytes": ctNatConnStatsOutgoingBytes,
       "ctNatConnStatsIncomingPkts": ctNatConnStatsIncomingPkts,
       "ctNatConnStatsIncomingBytes": ctNatConnStatsIncomingBytes,
       "ctNatConnStatsTimeSinceUse": ctNatConnStatsTimeSinceUse,
       "ctNatConnStatsProtocol": ctNatConnStatsProtocol,
       "ctNatConnStatsTCPSeq": ctNatConnStatsTCPSeq,
       "ctNatConnStatsTCPAck": ctNatConnStatsTCPAck,
       "ctNatConnStatsTCPState": ctNatConnStatsTCPState,
       "ctNatConnStatsLocalRetrys": ctNatConnStatsLocalRetrys,
       "ctNatConnStatsForeignRetrys": ctNatConnStatsForeignRetrys,
       "ctNatConnStatsLocalChecksum": ctNatConnStatsLocalChecksum,
       "ctNatConnStatsForeignChecksum": ctNatConnStatsForeignChecksum}
)
