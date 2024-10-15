# SNMP MIB module (FOUNDRY-SN-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:57 2024
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

(snIpx,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snIpx")

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



class RtrStatus(Integer32):
    """Custom type RtrStatus based on Integer32"""
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





class ClearStatus(Integer32):
    """Custom type ClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("normal", 0))
    )





class PortIndex(Integer32):
    """Custom type PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3900),
    )





class Action(Integer32):
    """Custom type Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )





class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnIpxGen_ObjectIdentity = ObjectIdentity
snIpxGen = _SnIpxGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1)
)
_SnIpxRoutingMode_Type = RtrStatus
_SnIpxRoutingMode_Object = MibScalar
snIpxRoutingMode = _SnIpxRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 1),
    _SnIpxRoutingMode_Type()
)
snIpxRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxRoutingMode.setStatus("mandatory")
_SnIpxNetBiosFilterMode_Type = RtrStatus
_SnIpxNetBiosFilterMode_Object = MibScalar
snIpxNetBiosFilterMode = _SnIpxNetBiosFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 2),
    _SnIpxNetBiosFilterMode_Type()
)
snIpxNetBiosFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxNetBiosFilterMode.setStatus("mandatory")
_SnIpxClearCache_Type = ClearStatus
_SnIpxClearCache_Object = MibScalar
snIpxClearCache = _SnIpxClearCache_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 3),
    _SnIpxClearCache_Type()
)
snIpxClearCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxClearCache.setStatus("mandatory")
_SnIpxClearRoute_Type = ClearStatus
_SnIpxClearRoute_Object = MibScalar
snIpxClearRoute = _SnIpxClearRoute_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 4),
    _SnIpxClearRoute_Type()
)
snIpxClearRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxClearRoute.setStatus("mandatory")
_SnIpxClearTrafficCnts_Type = ClearStatus
_SnIpxClearTrafficCnts_Object = MibScalar
snIpxClearTrafficCnts = _SnIpxClearTrafficCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 5),
    _SnIpxClearTrafficCnts_Type()
)
snIpxClearTrafficCnts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxClearTrafficCnts.setStatus("mandatory")
_SnIpxRcvPktsCnt_Type = Counter32
_SnIpxRcvPktsCnt_Object = MibScalar
snIpxRcvPktsCnt = _SnIpxRcvPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 6),
    _SnIpxRcvPktsCnt_Type()
)
snIpxRcvPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxRcvPktsCnt.setStatus("mandatory")
_SnIpxTxPktsCnt_Type = Counter32
_SnIpxTxPktsCnt_Object = MibScalar
snIpxTxPktsCnt = _SnIpxTxPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 7),
    _SnIpxTxPktsCnt_Type()
)
snIpxTxPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxTxPktsCnt.setStatus("mandatory")
_SnIpxFwdPktsCnt_Type = Counter32
_SnIpxFwdPktsCnt_Object = MibScalar
snIpxFwdPktsCnt = _SnIpxFwdPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 8),
    _SnIpxFwdPktsCnt_Type()
)
snIpxFwdPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxFwdPktsCnt.setStatus("mandatory")
_SnIpxRcvDropPktsCnt_Type = Counter32
_SnIpxRcvDropPktsCnt_Object = MibScalar
snIpxRcvDropPktsCnt = _SnIpxRcvDropPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 9),
    _SnIpxRcvDropPktsCnt_Type()
)
snIpxRcvDropPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxRcvDropPktsCnt.setStatus("mandatory")
_SnIpxRcvFiltPktsCnt_Type = Counter32
_SnIpxRcvFiltPktsCnt_Object = MibScalar
snIpxRcvFiltPktsCnt = _SnIpxRcvFiltPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 10),
    _SnIpxRcvFiltPktsCnt_Type()
)
snIpxRcvFiltPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxRcvFiltPktsCnt.setStatus("mandatory")


class _SnIpxRipGblFiltList_Type(OctetString):
    """Custom type snIpxRipGblFiltList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnIpxRipGblFiltList_Type.__name__ = "OctetString"
_SnIpxRipGblFiltList_Object = MibScalar
snIpxRipGblFiltList = _SnIpxRipGblFiltList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 11),
    _SnIpxRipGblFiltList_Type()
)
snIpxRipGblFiltList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxRipGblFiltList.setStatus("mandatory")


class _SnIpxRipFiltOnAllPort_Type(Integer32):
    """Custom type snIpxRipFiltOnAllPort based on Integer32"""
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
        *(("addAllInBound", 4),
          ("addAllOutBound", 5),
          ("deleteAllInBound", 2),
          ("deleteAllOutBound", 3),
          ("valid", 1))
    )


_SnIpxRipFiltOnAllPort_Type.__name__ = "Integer32"
_SnIpxRipFiltOnAllPort_Object = MibScalar
snIpxRipFiltOnAllPort = _SnIpxRipFiltOnAllPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 12),
    _SnIpxRipFiltOnAllPort_Type()
)
snIpxRipFiltOnAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxRipFiltOnAllPort.setStatus("mandatory")


class _SnIpxSapGblFiltList_Type(OctetString):
    """Custom type snIpxSapGblFiltList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnIpxSapGblFiltList_Type.__name__ = "OctetString"
_SnIpxSapGblFiltList_Object = MibScalar
snIpxSapGblFiltList = _SnIpxSapGblFiltList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 13),
    _SnIpxSapGblFiltList_Type()
)
snIpxSapGblFiltList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxSapGblFiltList.setStatus("mandatory")


class _SnIpxSapFiltOnAllPort_Type(Integer32):
    """Custom type snIpxSapFiltOnAllPort based on Integer32"""
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
        *(("addAllInBound", 4),
          ("addAllOutBound", 5),
          ("deleteAllInBound", 2),
          ("deleteAllOutBound", 3),
          ("valid", 1))
    )


_SnIpxSapFiltOnAllPort_Type.__name__ = "Integer32"
_SnIpxSapFiltOnAllPort_Object = MibScalar
snIpxSapFiltOnAllPort = _SnIpxSapFiltOnAllPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 14),
    _SnIpxSapFiltOnAllPort_Type()
)
snIpxSapFiltOnAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxSapFiltOnAllPort.setStatus("mandatory")
_SnIpxTxDropPktsCnt_Type = Counter32
_SnIpxTxDropPktsCnt_Object = MibScalar
snIpxTxDropPktsCnt = _SnIpxTxDropPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 15),
    _SnIpxTxDropPktsCnt_Type()
)
snIpxTxDropPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxTxDropPktsCnt.setStatus("mandatory")
_SnIpxTxFiltPktsCnt_Type = Counter32
_SnIpxTxFiltPktsCnt_Object = MibScalar
snIpxTxFiltPktsCnt = _SnIpxTxFiltPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 16),
    _SnIpxTxFiltPktsCnt_Type()
)
snIpxTxFiltPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxTxFiltPktsCnt.setStatus("mandatory")
_SnIpxCache_ObjectIdentity = ObjectIdentity
snIpxCache = _SnIpxCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2)
)
_SnIpxCacheTable_Object = MibTable
snIpxCacheTable = _SnIpxCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    snIpxCacheTable.setStatus("mandatory")
_SnIpxCacheEntry_Object = MibTableRow
snIpxCacheEntry = _SnIpxCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1)
)
snIpxCacheEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxCacheIndex"),
)
if mibBuilder.loadTexts:
    snIpxCacheEntry.setStatus("mandatory")
_SnIpxCacheIndex_Type = Integer32
_SnIpxCacheIndex_Object = MibTableColumn
snIpxCacheIndex = _SnIpxCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 1),
    _SnIpxCacheIndex_Type()
)
snIpxCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxCacheIndex.setStatus("mandatory")
_SnIpxCacheNetNum_Type = NetNumber
_SnIpxCacheNetNum_Object = MibTableColumn
snIpxCacheNetNum = _SnIpxCacheNetNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 2),
    _SnIpxCacheNetNum_Type()
)
snIpxCacheNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxCacheNetNum.setStatus("mandatory")
_SnIpxCacheNode_Type = PhysAddress
_SnIpxCacheNode_Object = MibTableColumn
snIpxCacheNode = _SnIpxCacheNode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 3),
    _SnIpxCacheNode_Type()
)
snIpxCacheNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxCacheNode.setStatus("mandatory")
_SnIpxCacheOutFilter_Type = RtrStatus
_SnIpxCacheOutFilter_Object = MibTableColumn
snIpxCacheOutFilter = _SnIpxCacheOutFilter_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 4),
    _SnIpxCacheOutFilter_Type()
)
snIpxCacheOutFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxCacheOutFilter.setStatus("mandatory")


class _SnIpxCacheEncap_Type(Integer32):
    """Custom type snIpxCacheEncap based on Integer32"""
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
        *(("ethernet8022", 2),
          ("ethernet8023", 3),
          ("ethernetII", 1),
          ("ethernetSnap", 4))
    )


_SnIpxCacheEncap_Type.__name__ = "Integer32"
_SnIpxCacheEncap_Object = MibTableColumn
snIpxCacheEncap = _SnIpxCacheEncap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 5),
    _SnIpxCacheEncap_Type()
)
snIpxCacheEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxCacheEncap.setStatus("mandatory")
_SnIpxCachePort_Type = PortIndex
_SnIpxCachePort_Object = MibTableColumn
snIpxCachePort = _SnIpxCachePort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 6),
    _SnIpxCachePort_Type()
)
snIpxCachePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxCachePort.setStatus("mandatory")
_SnIpxRoute_ObjectIdentity = ObjectIdentity
snIpxRoute = _SnIpxRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3)
)
_SnIpxRouteTable_Object = MibTable
snIpxRouteTable = _SnIpxRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    snIpxRouteTable.setStatus("mandatory")
_SnIpxRouteEntry_Object = MibTableRow
snIpxRouteEntry = _SnIpxRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1)
)
snIpxRouteEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxRouteIndex"),
)
if mibBuilder.loadTexts:
    snIpxRouteEntry.setStatus("mandatory")
_SnIpxRouteIndex_Type = Integer32
_SnIpxRouteIndex_Object = MibTableColumn
snIpxRouteIndex = _SnIpxRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 1),
    _SnIpxRouteIndex_Type()
)
snIpxRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxRouteIndex.setStatus("mandatory")
_SnIpxDestNetNum_Type = NetNumber
_SnIpxDestNetNum_Object = MibTableColumn
snIpxDestNetNum = _SnIpxDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 2),
    _SnIpxDestNetNum_Type()
)
snIpxDestNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxDestNetNum.setStatus("mandatory")
_SnIpxFwdRouterNode_Type = PhysAddress
_SnIpxFwdRouterNode_Object = MibTableColumn
snIpxFwdRouterNode = _SnIpxFwdRouterNode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 3),
    _SnIpxFwdRouterNode_Type()
)
snIpxFwdRouterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxFwdRouterNode.setStatus("mandatory")
_SnIpxDestHopCnts_Type = Integer32
_SnIpxDestHopCnts_Object = MibTableColumn
snIpxDestHopCnts = _SnIpxDestHopCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 4),
    _SnIpxDestHopCnts_Type()
)
snIpxDestHopCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxDestHopCnts.setStatus("mandatory")
_SnIpxRouteMetric_Type = Integer32
_SnIpxRouteMetric_Object = MibTableColumn
snIpxRouteMetric = _SnIpxRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 5),
    _SnIpxRouteMetric_Type()
)
snIpxRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxRouteMetric.setStatus("mandatory")
_SnIpxDestPort_Type = Integer32
_SnIpxDestPort_Object = MibTableColumn
snIpxDestPort = _SnIpxDestPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 6),
    _SnIpxDestPort_Type()
)
snIpxDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxDestPort.setStatus("mandatory")
_SnIpxServer_ObjectIdentity = ObjectIdentity
snIpxServer = _SnIpxServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4)
)
_SnIpxServerTable_Object = MibTable
snIpxServerTable = _SnIpxServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    snIpxServerTable.setStatus("mandatory")
_SnIpxServerEntry_Object = MibTableRow
snIpxServerEntry = _SnIpxServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1)
)
snIpxServerEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxServerIndex"),
)
if mibBuilder.loadTexts:
    snIpxServerEntry.setStatus("mandatory")
_SnIpxServerIndex_Type = Integer32
_SnIpxServerIndex_Object = MibTableColumn
snIpxServerIndex = _SnIpxServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 1),
    _SnIpxServerIndex_Type()
)
snIpxServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxServerIndex.setStatus("mandatory")
_SnIpxServerType_Type = Integer32
_SnIpxServerType_Object = MibTableColumn
snIpxServerType = _SnIpxServerType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 2),
    _SnIpxServerType_Type()
)
snIpxServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxServerType.setStatus("mandatory")
_SnIpxServerNetNum_Type = NetNumber
_SnIpxServerNetNum_Object = MibTableColumn
snIpxServerNetNum = _SnIpxServerNetNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 3),
    _SnIpxServerNetNum_Type()
)
snIpxServerNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxServerNetNum.setStatus("mandatory")
_SnIpxServerNode_Type = PhysAddress
_SnIpxServerNode_Object = MibTableColumn
snIpxServerNode = _SnIpxServerNode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 4),
    _SnIpxServerNode_Type()
)
snIpxServerNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxServerNode.setStatus("mandatory")
_SnIpxServerSocket_Type = Integer32
_SnIpxServerSocket_Object = MibTableColumn
snIpxServerSocket = _SnIpxServerSocket_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 5),
    _SnIpxServerSocket_Type()
)
snIpxServerSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxServerSocket.setStatus("mandatory")
_SnIpxServerHopCnts_Type = Integer32
_SnIpxServerHopCnts_Object = MibTableColumn
snIpxServerHopCnts = _SnIpxServerHopCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 6),
    _SnIpxServerHopCnts_Type()
)
snIpxServerHopCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxServerHopCnts.setStatus("mandatory")


class _SnIpxServerName_Type(OctetString):
    """Custom type snIpxServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_SnIpxServerName_Type.__name__ = "OctetString"
_SnIpxServerName_Object = MibTableColumn
snIpxServerName = _SnIpxServerName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 7),
    _SnIpxServerName_Type()
)
snIpxServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxServerName.setStatus("mandatory")
_SnIpxFwdFilter_ObjectIdentity = ObjectIdentity
snIpxFwdFilter = _SnIpxFwdFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5)
)
_SnIpxFwdFilterTable_Object = MibTable
snIpxFwdFilterTable = _SnIpxFwdFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    snIpxFwdFilterTable.setStatus("mandatory")
_SnIpxFwdFilterEntry_Object = MibTableRow
snIpxFwdFilterEntry = _SnIpxFwdFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1)
)
snIpxFwdFilterEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxFwdFilterId"),
)
if mibBuilder.loadTexts:
    snIpxFwdFilterEntry.setStatus("mandatory")
_SnIpxFwdFilterId_Type = Integer32
_SnIpxFwdFilterId_Object = MibTableColumn
snIpxFwdFilterId = _SnIpxFwdFilterId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 1),
    _SnIpxFwdFilterId_Type()
)
snIpxFwdFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxFwdFilterId.setStatus("mandatory")
_SnIpxFwdFilterAction_Type = Action
_SnIpxFwdFilterAction_Object = MibTableColumn
snIpxFwdFilterAction = _SnIpxFwdFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 2),
    _SnIpxFwdFilterAction_Type()
)
snIpxFwdFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxFwdFilterAction.setStatus("mandatory")
_SnIpxFwdFilterSocket_Type = Integer32
_SnIpxFwdFilterSocket_Object = MibTableColumn
snIpxFwdFilterSocket = _SnIpxFwdFilterSocket_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 3),
    _SnIpxFwdFilterSocket_Type()
)
snIpxFwdFilterSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxFwdFilterSocket.setStatus("mandatory")
_SnIpxFwdFilterSrcNet_Type = NetNumber
_SnIpxFwdFilterSrcNet_Object = MibTableColumn
snIpxFwdFilterSrcNet = _SnIpxFwdFilterSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 4),
    _SnIpxFwdFilterSrcNet_Type()
)
snIpxFwdFilterSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxFwdFilterSrcNet.setStatus("mandatory")
_SnIpxFwdFilterSrcNode_Type = PhysAddress
_SnIpxFwdFilterSrcNode_Object = MibTableColumn
snIpxFwdFilterSrcNode = _SnIpxFwdFilterSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 5),
    _SnIpxFwdFilterSrcNode_Type()
)
snIpxFwdFilterSrcNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxFwdFilterSrcNode.setStatus("mandatory")
_SnIpxFwdFilterDestNet_Type = NetNumber
_SnIpxFwdFilterDestNet_Object = MibTableColumn
snIpxFwdFilterDestNet = _SnIpxFwdFilterDestNet_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 6),
    _SnIpxFwdFilterDestNet_Type()
)
snIpxFwdFilterDestNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxFwdFilterDestNet.setStatus("mandatory")
_SnIpxFwdFilterDestNode_Type = PhysAddress
_SnIpxFwdFilterDestNode_Object = MibTableColumn
snIpxFwdFilterDestNode = _SnIpxFwdFilterDestNode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 7),
    _SnIpxFwdFilterDestNode_Type()
)
snIpxFwdFilterDestNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxFwdFilterDestNode.setStatus("mandatory")


class _SnIpxFwdFilterRowStatus_Type(Integer32):
    """Custom type snIpxFwdFilterRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnIpxFwdFilterRowStatus_Type.__name__ = "Integer32"
_SnIpxFwdFilterRowStatus_Object = MibTableColumn
snIpxFwdFilterRowStatus = _SnIpxFwdFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 8),
    _SnIpxFwdFilterRowStatus_Type()
)
snIpxFwdFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxFwdFilterRowStatus.setStatus("mandatory")
_SnIpxRipFilter_ObjectIdentity = ObjectIdentity
snIpxRipFilter = _SnIpxRipFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6)
)
_SnIpxRipFilterTable_Object = MibTable
snIpxRipFilterTable = _SnIpxRipFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    snIpxRipFilterTable.setStatus("mandatory")
_SnIpxRipFilterEntry_Object = MibTableRow
snIpxRipFilterEntry = _SnIpxRipFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1)
)
snIpxRipFilterEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxRipFilterId"),
)
if mibBuilder.loadTexts:
    snIpxRipFilterEntry.setStatus("mandatory")
_SnIpxRipFilterId_Type = Integer32
_SnIpxRipFilterId_Object = MibTableColumn
snIpxRipFilterId = _SnIpxRipFilterId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1, 1),
    _SnIpxRipFilterId_Type()
)
snIpxRipFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxRipFilterId.setStatus("mandatory")
_SnIpxRipFilterAction_Type = Action
_SnIpxRipFilterAction_Object = MibTableColumn
snIpxRipFilterAction = _SnIpxRipFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1, 2),
    _SnIpxRipFilterAction_Type()
)
snIpxRipFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxRipFilterAction.setStatus("mandatory")
_SnIpxRipFilterNet_Type = NetNumber
_SnIpxRipFilterNet_Object = MibTableColumn
snIpxRipFilterNet = _SnIpxRipFilterNet_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1, 3),
    _SnIpxRipFilterNet_Type()
)
snIpxRipFilterNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxRipFilterNet.setStatus("mandatory")
_SnIpxRipFilterMask_Type = NetNumber
_SnIpxRipFilterMask_Object = MibTableColumn
snIpxRipFilterMask = _SnIpxRipFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1, 4),
    _SnIpxRipFilterMask_Type()
)
snIpxRipFilterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxRipFilterMask.setStatus("mandatory")


class _SnIpxRipFilterRowStatus_Type(Integer32):
    """Custom type snIpxRipFilterRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnIpxRipFilterRowStatus_Type.__name__ = "Integer32"
_SnIpxRipFilterRowStatus_Object = MibTableColumn
snIpxRipFilterRowStatus = _SnIpxRipFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1, 5),
    _SnIpxRipFilterRowStatus_Type()
)
snIpxRipFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxRipFilterRowStatus.setStatus("mandatory")
_SnIpxSapFilter_ObjectIdentity = ObjectIdentity
snIpxSapFilter = _SnIpxSapFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7)
)
_SnIpxSapFilterTable_Object = MibTable
snIpxSapFilterTable = _SnIpxSapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    snIpxSapFilterTable.setStatus("mandatory")
_SnIpxSapFilterEntry_Object = MibTableRow
snIpxSapFilterEntry = _SnIpxSapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1)
)
snIpxSapFilterEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxSapFilterId"),
)
if mibBuilder.loadTexts:
    snIpxSapFilterEntry.setStatus("mandatory")
_SnIpxSapFilterId_Type = Integer32
_SnIpxSapFilterId_Object = MibTableColumn
snIpxSapFilterId = _SnIpxSapFilterId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1, 1),
    _SnIpxSapFilterId_Type()
)
snIpxSapFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxSapFilterId.setStatus("mandatory")
_SnIpxSapFilterAction_Type = Action
_SnIpxSapFilterAction_Object = MibTableColumn
snIpxSapFilterAction = _SnIpxSapFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1, 2),
    _SnIpxSapFilterAction_Type()
)
snIpxSapFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxSapFilterAction.setStatus("mandatory")
_SnIpxSapFilterType_Type = Integer32
_SnIpxSapFilterType_Object = MibTableColumn
snIpxSapFilterType = _SnIpxSapFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1, 3),
    _SnIpxSapFilterType_Type()
)
snIpxSapFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxSapFilterType.setStatus("mandatory")


class _SnIpxSapFilterName_Type(OctetString):
    """Custom type snIpxSapFilterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_SnIpxSapFilterName_Type.__name__ = "OctetString"
_SnIpxSapFilterName_Object = MibTableColumn
snIpxSapFilterName = _SnIpxSapFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1, 4),
    _SnIpxSapFilterName_Type()
)
snIpxSapFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxSapFilterName.setStatus("mandatory")


class _SnIpxSapFilterRowStatus_Type(Integer32):
    """Custom type snIpxSapFilterRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnIpxSapFilterRowStatus_Type.__name__ = "Integer32"
_SnIpxSapFilterRowStatus_Object = MibTableColumn
snIpxSapFilterRowStatus = _SnIpxSapFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1, 5),
    _SnIpxSapFilterRowStatus_Type()
)
snIpxSapFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxSapFilterRowStatus.setStatus("mandatory")
_SnIpxIfFwdAccess_ObjectIdentity = ObjectIdentity
snIpxIfFwdAccess = _SnIpxIfFwdAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8)
)
_SnIpxIfFwdAccessTable_Object = MibTable
snIpxIfFwdAccessTable = _SnIpxIfFwdAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    snIpxIfFwdAccessTable.setStatus("mandatory")
_SnIpxIfFwdAccessEntry_Object = MibTableRow
snIpxIfFwdAccessEntry = _SnIpxIfFwdAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1, 1)
)
snIpxIfFwdAccessEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxIfFwdAccessPort"),
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxIfFwdAccessDir"),
)
if mibBuilder.loadTexts:
    snIpxIfFwdAccessEntry.setStatus("mandatory")
_SnIpxIfFwdAccessPort_Type = Integer32
_SnIpxIfFwdAccessPort_Object = MibTableColumn
snIpxIfFwdAccessPort = _SnIpxIfFwdAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1, 1, 1),
    _SnIpxIfFwdAccessPort_Type()
)
snIpxIfFwdAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxIfFwdAccessPort.setStatus("mandatory")


class _SnIpxIfFwdAccessDir_Type(Integer32):
    """Custom type snIpxIfFwdAccessDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_SnIpxIfFwdAccessDir_Type.__name__ = "Integer32"
_SnIpxIfFwdAccessDir_Object = MibTableColumn
snIpxIfFwdAccessDir = _SnIpxIfFwdAccessDir_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1, 1, 2),
    _SnIpxIfFwdAccessDir_Type()
)
snIpxIfFwdAccessDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxIfFwdAccessDir.setStatus("mandatory")


class _SnIpxIfFwdAccessFilterList_Type(OctetString):
    """Custom type snIpxIfFwdAccessFilterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnIpxIfFwdAccessFilterList_Type.__name__ = "OctetString"
_SnIpxIfFwdAccessFilterList_Object = MibTableColumn
snIpxIfFwdAccessFilterList = _SnIpxIfFwdAccessFilterList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1, 1, 3),
    _SnIpxIfFwdAccessFilterList_Type()
)
snIpxIfFwdAccessFilterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxIfFwdAccessFilterList.setStatus("mandatory")


class _SnIpxIfFwdAccessRowStatus_Type(Integer32):
    """Custom type snIpxIfFwdAccessRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnIpxIfFwdAccessRowStatus_Type.__name__ = "Integer32"
_SnIpxIfFwdAccessRowStatus_Object = MibTableColumn
snIpxIfFwdAccessRowStatus = _SnIpxIfFwdAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1, 1, 4),
    _SnIpxIfFwdAccessRowStatus_Type()
)
snIpxIfFwdAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxIfFwdAccessRowStatus.setStatus("mandatory")
_SnIpxIfRipAccess_ObjectIdentity = ObjectIdentity
snIpxIfRipAccess = _SnIpxIfRipAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9)
)
_SnIpxIfRipAccessTable_Object = MibTable
snIpxIfRipAccessTable = _SnIpxIfRipAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    snIpxIfRipAccessTable.setStatus("mandatory")
_SnIpxIfRipAccessEntry_Object = MibTableRow
snIpxIfRipAccessEntry = _SnIpxIfRipAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1, 1)
)
snIpxIfRipAccessEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxIfRipAccessPort"),
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxIfRipAccessDir"),
)
if mibBuilder.loadTexts:
    snIpxIfRipAccessEntry.setStatus("mandatory")
_SnIpxIfRipAccessPort_Type = Integer32
_SnIpxIfRipAccessPort_Object = MibTableColumn
snIpxIfRipAccessPort = _SnIpxIfRipAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1, 1, 1),
    _SnIpxIfRipAccessPort_Type()
)
snIpxIfRipAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxIfRipAccessPort.setStatus("mandatory")


class _SnIpxIfRipAccessDir_Type(Integer32):
    """Custom type snIpxIfRipAccessDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_SnIpxIfRipAccessDir_Type.__name__ = "Integer32"
_SnIpxIfRipAccessDir_Object = MibTableColumn
snIpxIfRipAccessDir = _SnIpxIfRipAccessDir_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1, 1, 2),
    _SnIpxIfRipAccessDir_Type()
)
snIpxIfRipAccessDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxIfRipAccessDir.setStatus("mandatory")


class _SnIpxIfRipAccessFilterList_Type(OctetString):
    """Custom type snIpxIfRipAccessFilterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnIpxIfRipAccessFilterList_Type.__name__ = "OctetString"
_SnIpxIfRipAccessFilterList_Object = MibTableColumn
snIpxIfRipAccessFilterList = _SnIpxIfRipAccessFilterList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1, 1, 3),
    _SnIpxIfRipAccessFilterList_Type()
)
snIpxIfRipAccessFilterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxIfRipAccessFilterList.setStatus("mandatory")


class _SnIpxIfRipAccessRowStatus_Type(Integer32):
    """Custom type snIpxIfRipAccessRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnIpxIfRipAccessRowStatus_Type.__name__ = "Integer32"
_SnIpxIfRipAccessRowStatus_Object = MibTableColumn
snIpxIfRipAccessRowStatus = _SnIpxIfRipAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1, 1, 4),
    _SnIpxIfRipAccessRowStatus_Type()
)
snIpxIfRipAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxIfRipAccessRowStatus.setStatus("mandatory")
_SnIpxIfSapAccess_ObjectIdentity = ObjectIdentity
snIpxIfSapAccess = _SnIpxIfSapAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10)
)
_SnIpxIfSapAccessTable_Object = MibTable
snIpxIfSapAccessTable = _SnIpxIfSapAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    snIpxIfSapAccessTable.setStatus("mandatory")
_SnIpxIfSapAccessEntry_Object = MibTableRow
snIpxIfSapAccessEntry = _SnIpxIfSapAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1, 1)
)
snIpxIfSapAccessEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxIfSapAccessPort"),
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxIfSapAccessDir"),
)
if mibBuilder.loadTexts:
    snIpxIfSapAccessEntry.setStatus("mandatory")
_SnIpxIfSapAccessPort_Type = Integer32
_SnIpxIfSapAccessPort_Object = MibTableColumn
snIpxIfSapAccessPort = _SnIpxIfSapAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1, 1, 1),
    _SnIpxIfSapAccessPort_Type()
)
snIpxIfSapAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxIfSapAccessPort.setStatus("mandatory")


class _SnIpxIfSapAccessDir_Type(Integer32):
    """Custom type snIpxIfSapAccessDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_SnIpxIfSapAccessDir_Type.__name__ = "Integer32"
_SnIpxIfSapAccessDir_Object = MibTableColumn
snIpxIfSapAccessDir = _SnIpxIfSapAccessDir_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1, 1, 2),
    _SnIpxIfSapAccessDir_Type()
)
snIpxIfSapAccessDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxIfSapAccessDir.setStatus("mandatory")


class _SnIpxIfSapAccessFilterList_Type(OctetString):
    """Custom type snIpxIfSapAccessFilterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnIpxIfSapAccessFilterList_Type.__name__ = "OctetString"
_SnIpxIfSapAccessFilterList_Object = MibTableColumn
snIpxIfSapAccessFilterList = _SnIpxIfSapAccessFilterList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1, 1, 3),
    _SnIpxIfSapAccessFilterList_Type()
)
snIpxIfSapAccessFilterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxIfSapAccessFilterList.setStatus("mandatory")


class _SnIpxIfSapAccessRowStatus_Type(Integer32):
    """Custom type snIpxIfSapAccessRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnIpxIfSapAccessRowStatus_Type.__name__ = "Integer32"
_SnIpxIfSapAccessRowStatus_Object = MibTableColumn
snIpxIfSapAccessRowStatus = _SnIpxIfSapAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1, 1, 4),
    _SnIpxIfSapAccessRowStatus_Type()
)
snIpxIfSapAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxIfSapAccessRowStatus.setStatus("mandatory")
_SnIpxPortAddr_ObjectIdentity = ObjectIdentity
snIpxPortAddr = _SnIpxPortAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11)
)
_SnIpxPortAddrTable_Object = MibTable
snIpxPortAddrTable = _SnIpxPortAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    snIpxPortAddrTable.setStatus("mandatory")
_SnIpxPortAddrEntry_Object = MibTableRow
snIpxPortAddrEntry = _SnIpxPortAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1)
)
snIpxPortAddrEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxPortAddrPort"),
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxPortAddrEncap"),
)
if mibBuilder.loadTexts:
    snIpxPortAddrEntry.setStatus("mandatory")
_SnIpxPortAddrPort_Type = PortIndex
_SnIpxPortAddrPort_Object = MibTableColumn
snIpxPortAddrPort = _SnIpxPortAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1, 1),
    _SnIpxPortAddrPort_Type()
)
snIpxPortAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortAddrPort.setStatus("mandatory")


class _SnIpxPortAddrEncap_Type(Integer32):
    """Custom type snIpxPortAddrEncap based on Integer32"""
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
        *(("ethernet8022", 1),
          ("ethernet8023", 2),
          ("ethernetII", 3),
          ("ethernetSnap", 4))
    )


_SnIpxPortAddrEncap_Type.__name__ = "Integer32"
_SnIpxPortAddrEncap_Object = MibTableColumn
snIpxPortAddrEncap = _SnIpxPortAddrEncap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1, 2),
    _SnIpxPortAddrEncap_Type()
)
snIpxPortAddrEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortAddrEncap.setStatus("mandatory")
_SnIpxPortAddrNetNum_Type = NetNumber
_SnIpxPortAddrNetNum_Object = MibTableColumn
snIpxPortAddrNetNum = _SnIpxPortAddrNetNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1, 3),
    _SnIpxPortAddrNetNum_Type()
)
snIpxPortAddrNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxPortAddrNetNum.setStatus("mandatory")


class _SnIpxPortAddrRowStatus_Type(Integer32):
    """Custom type snIpxPortAddrRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnIpxPortAddrRowStatus_Type.__name__ = "Integer32"
_SnIpxPortAddrRowStatus_Object = MibTableColumn
snIpxPortAddrRowStatus = _SnIpxPortAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1, 4),
    _SnIpxPortAddrRowStatus_Type()
)
snIpxPortAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxPortAddrRowStatus.setStatus("mandatory")
_SnIpxPortAddrNetBiosFilterMode_Type = RtrStatus
_SnIpxPortAddrNetBiosFilterMode_Object = MibTableColumn
snIpxPortAddrNetBiosFilterMode = _SnIpxPortAddrNetBiosFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1, 5),
    _SnIpxPortAddrNetBiosFilterMode_Type()
)
snIpxPortAddrNetBiosFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpxPortAddrNetBiosFilterMode.setStatus("mandatory")
_SnIpxPortCounters_ObjectIdentity = ObjectIdentity
snIpxPortCounters = _SnIpxPortCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12)
)
_SnIpxPortCountersTable_Object = MibTable
snIpxPortCountersTable = _SnIpxPortCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    snIpxPortCountersTable.setStatus("mandatory")
_SnIpxPortCountersEntry_Object = MibTableRow
snIpxPortCountersEntry = _SnIpxPortCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1)
)
snIpxPortCountersEntry.setIndexNames(
    (0, "FOUNDRY-SN-IPX-MIB", "snIpxPortCountersPort"),
)
if mibBuilder.loadTexts:
    snIpxPortCountersEntry.setStatus("mandatory")
_SnIpxPortCountersPort_Type = PortIndex
_SnIpxPortCountersPort_Object = MibTableColumn
snIpxPortCountersPort = _SnIpxPortCountersPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 1),
    _SnIpxPortCountersPort_Type()
)
snIpxPortCountersPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortCountersPort.setStatus("mandatory")
_SnIpxPortCountersRcvPktsCnt_Type = Counter32
_SnIpxPortCountersRcvPktsCnt_Object = MibTableColumn
snIpxPortCountersRcvPktsCnt = _SnIpxPortCountersRcvPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 2),
    _SnIpxPortCountersRcvPktsCnt_Type()
)
snIpxPortCountersRcvPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortCountersRcvPktsCnt.setStatus("mandatory")
_SnIpxPortCountersTxPktsCnt_Type = Counter32
_SnIpxPortCountersTxPktsCnt_Object = MibTableColumn
snIpxPortCountersTxPktsCnt = _SnIpxPortCountersTxPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 3),
    _SnIpxPortCountersTxPktsCnt_Type()
)
snIpxPortCountersTxPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortCountersTxPktsCnt.setStatus("mandatory")
_SnIpxPortCountersFwdPktsCnt_Type = Counter32
_SnIpxPortCountersFwdPktsCnt_Object = MibTableColumn
snIpxPortCountersFwdPktsCnt = _SnIpxPortCountersFwdPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 4),
    _SnIpxPortCountersFwdPktsCnt_Type()
)
snIpxPortCountersFwdPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortCountersFwdPktsCnt.setStatus("mandatory")
_SnIpxPortCountersRcvDropPktsCnt_Type = Counter32
_SnIpxPortCountersRcvDropPktsCnt_Object = MibTableColumn
snIpxPortCountersRcvDropPktsCnt = _SnIpxPortCountersRcvDropPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 5),
    _SnIpxPortCountersRcvDropPktsCnt_Type()
)
snIpxPortCountersRcvDropPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortCountersRcvDropPktsCnt.setStatus("mandatory")
_SnIpxPortCountersTxDropPktsCnt_Type = Counter32
_SnIpxPortCountersTxDropPktsCnt_Object = MibTableColumn
snIpxPortCountersTxDropPktsCnt = _SnIpxPortCountersTxDropPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 6),
    _SnIpxPortCountersTxDropPktsCnt_Type()
)
snIpxPortCountersTxDropPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortCountersTxDropPktsCnt.setStatus("mandatory")
_SnIpxPortCountersRcvFiltPktsCnt_Type = Counter32
_SnIpxPortCountersRcvFiltPktsCnt_Object = MibTableColumn
snIpxPortCountersRcvFiltPktsCnt = _SnIpxPortCountersRcvFiltPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 7),
    _SnIpxPortCountersRcvFiltPktsCnt_Type()
)
snIpxPortCountersRcvFiltPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortCountersRcvFiltPktsCnt.setStatus("mandatory")
_SnIpxPortCountersTxFiltPktsCnt_Type = Counter32
_SnIpxPortCountersTxFiltPktsCnt_Object = MibTableColumn
snIpxPortCountersTxFiltPktsCnt = _SnIpxPortCountersTxFiltPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 8),
    _SnIpxPortCountersTxFiltPktsCnt_Type()
)
snIpxPortCountersTxFiltPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortCountersTxFiltPktsCnt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-IPX-MIB",
    **{"RtrStatus": RtrStatus,
       "ClearStatus": ClearStatus,
       "PortIndex": PortIndex,
       "Action": Action,
       "PhysAddress": PhysAddress,
       "NetNumber": NetNumber,
       "snIpxGen": snIpxGen,
       "snIpxRoutingMode": snIpxRoutingMode,
       "snIpxNetBiosFilterMode": snIpxNetBiosFilterMode,
       "snIpxClearCache": snIpxClearCache,
       "snIpxClearRoute": snIpxClearRoute,
       "snIpxClearTrafficCnts": snIpxClearTrafficCnts,
       "snIpxRcvPktsCnt": snIpxRcvPktsCnt,
       "snIpxTxPktsCnt": snIpxTxPktsCnt,
       "snIpxFwdPktsCnt": snIpxFwdPktsCnt,
       "snIpxRcvDropPktsCnt": snIpxRcvDropPktsCnt,
       "snIpxRcvFiltPktsCnt": snIpxRcvFiltPktsCnt,
       "snIpxRipGblFiltList": snIpxRipGblFiltList,
       "snIpxRipFiltOnAllPort": snIpxRipFiltOnAllPort,
       "snIpxSapGblFiltList": snIpxSapGblFiltList,
       "snIpxSapFiltOnAllPort": snIpxSapFiltOnAllPort,
       "snIpxTxDropPktsCnt": snIpxTxDropPktsCnt,
       "snIpxTxFiltPktsCnt": snIpxTxFiltPktsCnt,
       "snIpxCache": snIpxCache,
       "snIpxCacheTable": snIpxCacheTable,
       "snIpxCacheEntry": snIpxCacheEntry,
       "snIpxCacheIndex": snIpxCacheIndex,
       "snIpxCacheNetNum": snIpxCacheNetNum,
       "snIpxCacheNode": snIpxCacheNode,
       "snIpxCacheOutFilter": snIpxCacheOutFilter,
       "snIpxCacheEncap": snIpxCacheEncap,
       "snIpxCachePort": snIpxCachePort,
       "snIpxRoute": snIpxRoute,
       "snIpxRouteTable": snIpxRouteTable,
       "snIpxRouteEntry": snIpxRouteEntry,
       "snIpxRouteIndex": snIpxRouteIndex,
       "snIpxDestNetNum": snIpxDestNetNum,
       "snIpxFwdRouterNode": snIpxFwdRouterNode,
       "snIpxDestHopCnts": snIpxDestHopCnts,
       "snIpxRouteMetric": snIpxRouteMetric,
       "snIpxDestPort": snIpxDestPort,
       "snIpxServer": snIpxServer,
       "snIpxServerTable": snIpxServerTable,
       "snIpxServerEntry": snIpxServerEntry,
       "snIpxServerIndex": snIpxServerIndex,
       "snIpxServerType": snIpxServerType,
       "snIpxServerNetNum": snIpxServerNetNum,
       "snIpxServerNode": snIpxServerNode,
       "snIpxServerSocket": snIpxServerSocket,
       "snIpxServerHopCnts": snIpxServerHopCnts,
       "snIpxServerName": snIpxServerName,
       "snIpxFwdFilter": snIpxFwdFilter,
       "snIpxFwdFilterTable": snIpxFwdFilterTable,
       "snIpxFwdFilterEntry": snIpxFwdFilterEntry,
       "snIpxFwdFilterId": snIpxFwdFilterId,
       "snIpxFwdFilterAction": snIpxFwdFilterAction,
       "snIpxFwdFilterSocket": snIpxFwdFilterSocket,
       "snIpxFwdFilterSrcNet": snIpxFwdFilterSrcNet,
       "snIpxFwdFilterSrcNode": snIpxFwdFilterSrcNode,
       "snIpxFwdFilterDestNet": snIpxFwdFilterDestNet,
       "snIpxFwdFilterDestNode": snIpxFwdFilterDestNode,
       "snIpxFwdFilterRowStatus": snIpxFwdFilterRowStatus,
       "snIpxRipFilter": snIpxRipFilter,
       "snIpxRipFilterTable": snIpxRipFilterTable,
       "snIpxRipFilterEntry": snIpxRipFilterEntry,
       "snIpxRipFilterId": snIpxRipFilterId,
       "snIpxRipFilterAction": snIpxRipFilterAction,
       "snIpxRipFilterNet": snIpxRipFilterNet,
       "snIpxRipFilterMask": snIpxRipFilterMask,
       "snIpxRipFilterRowStatus": snIpxRipFilterRowStatus,
       "snIpxSapFilter": snIpxSapFilter,
       "snIpxSapFilterTable": snIpxSapFilterTable,
       "snIpxSapFilterEntry": snIpxSapFilterEntry,
       "snIpxSapFilterId": snIpxSapFilterId,
       "snIpxSapFilterAction": snIpxSapFilterAction,
       "snIpxSapFilterType": snIpxSapFilterType,
       "snIpxSapFilterName": snIpxSapFilterName,
       "snIpxSapFilterRowStatus": snIpxSapFilterRowStatus,
       "snIpxIfFwdAccess": snIpxIfFwdAccess,
       "snIpxIfFwdAccessTable": snIpxIfFwdAccessTable,
       "snIpxIfFwdAccessEntry": snIpxIfFwdAccessEntry,
       "snIpxIfFwdAccessPort": snIpxIfFwdAccessPort,
       "snIpxIfFwdAccessDir": snIpxIfFwdAccessDir,
       "snIpxIfFwdAccessFilterList": snIpxIfFwdAccessFilterList,
       "snIpxIfFwdAccessRowStatus": snIpxIfFwdAccessRowStatus,
       "snIpxIfRipAccess": snIpxIfRipAccess,
       "snIpxIfRipAccessTable": snIpxIfRipAccessTable,
       "snIpxIfRipAccessEntry": snIpxIfRipAccessEntry,
       "snIpxIfRipAccessPort": snIpxIfRipAccessPort,
       "snIpxIfRipAccessDir": snIpxIfRipAccessDir,
       "snIpxIfRipAccessFilterList": snIpxIfRipAccessFilterList,
       "snIpxIfRipAccessRowStatus": snIpxIfRipAccessRowStatus,
       "snIpxIfSapAccess": snIpxIfSapAccess,
       "snIpxIfSapAccessTable": snIpxIfSapAccessTable,
       "snIpxIfSapAccessEntry": snIpxIfSapAccessEntry,
       "snIpxIfSapAccessPort": snIpxIfSapAccessPort,
       "snIpxIfSapAccessDir": snIpxIfSapAccessDir,
       "snIpxIfSapAccessFilterList": snIpxIfSapAccessFilterList,
       "snIpxIfSapAccessRowStatus": snIpxIfSapAccessRowStatus,
       "snIpxPortAddr": snIpxPortAddr,
       "snIpxPortAddrTable": snIpxPortAddrTable,
       "snIpxPortAddrEntry": snIpxPortAddrEntry,
       "snIpxPortAddrPort": snIpxPortAddrPort,
       "snIpxPortAddrEncap": snIpxPortAddrEncap,
       "snIpxPortAddrNetNum": snIpxPortAddrNetNum,
       "snIpxPortAddrRowStatus": snIpxPortAddrRowStatus,
       "snIpxPortAddrNetBiosFilterMode": snIpxPortAddrNetBiosFilterMode,
       "snIpxPortCounters": snIpxPortCounters,
       "snIpxPortCountersTable": snIpxPortCountersTable,
       "snIpxPortCountersEntry": snIpxPortCountersEntry,
       "snIpxPortCountersPort": snIpxPortCountersPort,
       "snIpxPortCountersRcvPktsCnt": snIpxPortCountersRcvPktsCnt,
       "snIpxPortCountersTxPktsCnt": snIpxPortCountersTxPktsCnt,
       "snIpxPortCountersFwdPktsCnt": snIpxPortCountersFwdPktsCnt,
       "snIpxPortCountersRcvDropPktsCnt": snIpxPortCountersRcvDropPktsCnt,
       "snIpxPortCountersTxDropPktsCnt": snIpxPortCountersTxDropPktsCnt,
       "snIpxPortCountersRcvFiltPktsCnt": snIpxPortCountersRcvFiltPktsCnt,
       "snIpxPortCountersTxFiltPktsCnt": snIpxPortCountersTxFiltPktsCnt}
)
