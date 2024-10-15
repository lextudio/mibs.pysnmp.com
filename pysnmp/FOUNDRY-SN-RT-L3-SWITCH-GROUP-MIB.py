# SNMP MIB module (FOUNDRY-SN-RT-L3-SWITCH-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-RT-L3-SWITCH-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:05 2024
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

(snIp,
 snIpx) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snIp",
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



class RowSts(Integer32):
    """Custom type RowSts based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )





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
        ValueRangeConstraint(1, 34),
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
_SnIpxFwdPktsCnt_Type = Counter32
_SnIpxFwdPktsCnt_Object = MibScalar
snIpxFwdPktsCnt = _SnIpxFwdPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 8),
    _SnIpxFwdPktsCnt_Type()
)
snIpxFwdPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxFwdPktsCnt.setStatus("mandatory")
_SnIpxRcvFiltPktsCnt_Type = Counter32
_SnIpxRcvFiltPktsCnt_Object = MibScalar
snIpxRcvFiltPktsCnt = _SnIpxRcvFiltPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 10),
    _SnIpxRcvFiltPktsCnt_Type()
)
snIpxRcvFiltPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxRcvFiltPktsCnt.setStatus("mandatory")
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
    (0, "FOUNDRY-SN-RT-L3-SWITCH-GROUP-MIB", "snIpxCacheIndex"),
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


class _SnIpxCacheNetNum_Type(OctetString):
    """Custom type snIpxCacheNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_SnIpxCacheNetNum_Type.__name__ = "OctetString"
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
    (0, "FOUNDRY-SN-RT-L3-SWITCH-GROUP-MIB", "snIpxRouteIndex"),
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


class _SnIpxDestNetNum_Type(OctetString):
    """Custom type snIpxDestNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_SnIpxDestNetNum_Type.__name__ = "OctetString"
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
    (0, "FOUNDRY-SN-RT-L3-SWITCH-GROUP-MIB", "snIpxFwdFilterId"),
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
    (0, "FOUNDRY-SN-RT-L3-SWITCH-GROUP-MIB", "snIpxPortCountersPort"),
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
_SnIpxPortCountersFwdPktsCnt_Type = Counter32
_SnIpxPortCountersFwdPktsCnt_Object = MibTableColumn
snIpxPortCountersFwdPktsCnt = _SnIpxPortCountersFwdPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 4),
    _SnIpxPortCountersFwdPktsCnt_Type()
)
snIpxPortCountersFwdPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortCountersFwdPktsCnt.setStatus("mandatory")
_SnIpxPortCountersRcvFiltPktsCnt_Type = Counter32
_SnIpxPortCountersRcvFiltPktsCnt_Object = MibTableColumn
snIpxPortCountersRcvFiltPktsCnt = _SnIpxPortCountersRcvFiltPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 7),
    _SnIpxPortCountersRcvFiltPktsCnt_Type()
)
snIpxPortCountersRcvFiltPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpxPortCountersRcvFiltPktsCnt.setStatus("mandatory")
_SnRtIpGeneral_ObjectIdentity = ObjectIdentity
snRtIpGeneral = _SnRtIpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 1)
)
_SnRtClearArpCache_Type = ClearStatus
_SnRtClearArpCache_Object = MibScalar
snRtClearArpCache = _SnRtClearArpCache_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 1, 1),
    _SnRtClearArpCache_Type()
)
snRtClearArpCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtClearArpCache.setStatus("mandatory")
_SnRtClearIpCache_Type = ClearStatus
_SnRtClearIpCache_Object = MibScalar
snRtClearIpCache = _SnRtClearIpCache_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 1, 2),
    _SnRtClearIpCache_Type()
)
snRtClearIpCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtClearIpCache.setStatus("mandatory")
_SnRtIpFilterTable_Object = MibTable
snRtIpFilterTable = _SnRtIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    snRtIpFilterTable.setStatus("mandatory")
_SnRtIpFilterEntry_Object = MibTableRow
snRtIpFilterEntry = _SnRtIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1)
)
snRtIpFilterEntry.setIndexNames(
    (0, "FOUNDRY-SN-RT-L3-SWITCH-GROUP-MIB", "snRtIpFilterIndex"),
)
if mibBuilder.loadTexts:
    snRtIpFilterEntry.setStatus("mandatory")


class _SnRtIpFilterIndex_Type(Integer32):
    """Custom type snRtIpFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SnRtIpFilterIndex_Type.__name__ = "Integer32"
_SnRtIpFilterIndex_Object = MibTableColumn
snRtIpFilterIndex = _SnRtIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 1),
    _SnRtIpFilterIndex_Type()
)
snRtIpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFilterIndex.setStatus("mandatory")


class _SnRtIpFilterAction_Type(Integer32):
    """Custom type snRtIpFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1),
          ("qosEnabled", 2))
    )


_SnRtIpFilterAction_Type.__name__ = "Integer32"
_SnRtIpFilterAction_Object = MibTableColumn
snRtIpFilterAction = _SnRtIpFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 2),
    _SnRtIpFilterAction_Type()
)
snRtIpFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterAction.setStatus("mandatory")


class _SnRtIpFilterProtocol_Type(Integer32):
    """Custom type snRtIpFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnRtIpFilterProtocol_Type.__name__ = "Integer32"
_SnRtIpFilterProtocol_Object = MibTableColumn
snRtIpFilterProtocol = _SnRtIpFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 3),
    _SnRtIpFilterProtocol_Type()
)
snRtIpFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterProtocol.setStatus("mandatory")
_SnRtIpFilterSourceIp_Type = IpAddress
_SnRtIpFilterSourceIp_Object = MibTableColumn
snRtIpFilterSourceIp = _SnRtIpFilterSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 4),
    _SnRtIpFilterSourceIp_Type()
)
snRtIpFilterSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterSourceIp.setStatus("mandatory")
_SnRtIpFilterSourceMask_Type = IpAddress
_SnRtIpFilterSourceMask_Object = MibTableColumn
snRtIpFilterSourceMask = _SnRtIpFilterSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 5),
    _SnRtIpFilterSourceMask_Type()
)
snRtIpFilterSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterSourceMask.setStatus("mandatory")
_SnRtIpFilterDestIp_Type = IpAddress
_SnRtIpFilterDestIp_Object = MibTableColumn
snRtIpFilterDestIp = _SnRtIpFilterDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 6),
    _SnRtIpFilterDestIp_Type()
)
snRtIpFilterDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterDestIp.setStatus("mandatory")
_SnRtIpFilterDestMask_Type = IpAddress
_SnRtIpFilterDestMask_Object = MibTableColumn
snRtIpFilterDestMask = _SnRtIpFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 7),
    _SnRtIpFilterDestMask_Type()
)
snRtIpFilterDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterDestMask.setStatus("mandatory")


class _SnRtIpFilterOperator_Type(Integer32):
    """Custom type snRtIpFilterOperator based on Integer32"""
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
        *(("equal", 2),
          ("greater", 1),
          ("less", 3),
          ("notEqual", 4))
    )


_SnRtIpFilterOperator_Type.__name__ = "Integer32"
_SnRtIpFilterOperator_Object = MibTableColumn
snRtIpFilterOperator = _SnRtIpFilterOperator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 8),
    _SnRtIpFilterOperator_Type()
)
snRtIpFilterOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterOperator.setStatus("mandatory")


class _SnRtIpFilterOperand_Type(Integer32):
    """Custom type snRtIpFilterOperand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnRtIpFilterOperand_Type.__name__ = "Integer32"
_SnRtIpFilterOperand_Object = MibTableColumn
snRtIpFilterOperand = _SnRtIpFilterOperand_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 9),
    _SnRtIpFilterOperand_Type()
)
snRtIpFilterOperand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterOperand.setStatus("mandatory")
_SnRtIpFilterRowStatus_Type = RowSts
_SnRtIpFilterRowStatus_Object = MibTableColumn
snRtIpFilterRowStatus = _SnRtIpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 10),
    _SnRtIpFilterRowStatus_Type()
)
snRtIpFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterRowStatus.setStatus("mandatory")
_SnRtIpFilterEstablished_Type = RtrStatus
_SnRtIpFilterEstablished_Object = MibTableColumn
snRtIpFilterEstablished = _SnRtIpFilterEstablished_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 11),
    _SnRtIpFilterEstablished_Type()
)
snRtIpFilterEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterEstablished.setStatus("mandatory")


class _SnRtIpFilterQosPriority_Type(Integer32):
    """Custom type snRtIpFilterQosPriority based on Integer32"""
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
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )


_SnRtIpFilterQosPriority_Type.__name__ = "Integer32"
_SnRtIpFilterQosPriority_Object = MibTableColumn
snRtIpFilterQosPriority = _SnRtIpFilterQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 3, 1, 12),
    _SnRtIpFilterQosPriority_Type()
)
snRtIpFilterQosPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterQosPriority.setStatus("mandatory")
_SnRtIpTraceRoute_ObjectIdentity = ObjectIdentity
snRtIpTraceRoute = _SnRtIpTraceRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10)
)
_SnRtIpTraceRouteGeneral_ObjectIdentity = ObjectIdentity
snRtIpTraceRouteGeneral = _SnRtIpTraceRouteGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 1)
)
_SnRtIpTraceRouteTargetAddr_Type = IpAddress
_SnRtIpTraceRouteTargetAddr_Object = MibScalar
snRtIpTraceRouteTargetAddr = _SnRtIpTraceRouteTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 1, 1),
    _SnRtIpTraceRouteTargetAddr_Type()
)
snRtIpTraceRouteTargetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTraceRouteTargetAddr.setStatus("mandatory")


class _SnRtIpTraceRouteMinTtl_Type(Integer32):
    """Custom type snRtIpTraceRouteMinTtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnRtIpTraceRouteMinTtl_Type.__name__ = "Integer32"
_SnRtIpTraceRouteMinTtl_Object = MibScalar
snRtIpTraceRouteMinTtl = _SnRtIpTraceRouteMinTtl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 1, 2),
    _SnRtIpTraceRouteMinTtl_Type()
)
snRtIpTraceRouteMinTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTraceRouteMinTtl.setStatus("mandatory")


class _SnRtIpTraceRouteMaxTtl_Type(Integer32):
    """Custom type snRtIpTraceRouteMaxTtl based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnRtIpTraceRouteMaxTtl_Type.__name__ = "Integer32"
_SnRtIpTraceRouteMaxTtl_Object = MibScalar
snRtIpTraceRouteMaxTtl = _SnRtIpTraceRouteMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 1, 3),
    _SnRtIpTraceRouteMaxTtl_Type()
)
snRtIpTraceRouteMaxTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTraceRouteMaxTtl.setStatus("mandatory")


class _SnRtIpTraceRouteTimeOut_Type(Integer32):
    """Custom type snRtIpTraceRouteTimeOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_SnRtIpTraceRouteTimeOut_Type.__name__ = "Integer32"
_SnRtIpTraceRouteTimeOut_Object = MibScalar
snRtIpTraceRouteTimeOut = _SnRtIpTraceRouteTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 1, 4),
    _SnRtIpTraceRouteTimeOut_Type()
)
snRtIpTraceRouteTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTraceRouteTimeOut.setStatus("mandatory")


class _SnRtIpTraceRouteControl_Type(Integer32):
    """Custom type snRtIpTraceRouteControl based on Integer32"""
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
        *(("abort", 2),
          ("failure", 4),
          ("inProgress", 5),
          ("start", 1),
          ("success", 3))
    )


_SnRtIpTraceRouteControl_Type.__name__ = "Integer32"
_SnRtIpTraceRouteControl_Object = MibScalar
snRtIpTraceRouteControl = _SnRtIpTraceRouteControl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 1, 5),
    _SnRtIpTraceRouteControl_Type()
)
snRtIpTraceRouteControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTraceRouteControl.setStatus("mandatory")
_SnRtIpTraceRouteResult_ObjectIdentity = ObjectIdentity
snRtIpTraceRouteResult = _SnRtIpTraceRouteResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 2)
)
_SnRtIpTraceRouteResultTable_Object = MibTable
snRtIpTraceRouteResultTable = _SnRtIpTraceRouteResultTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultTable.setStatus("mandatory")
_SnRtIpTraceRouteResultEntry_Object = MibTableRow
snRtIpTraceRouteResultEntry = _SnRtIpTraceRouteResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 2, 1, 1)
)
snRtIpTraceRouteResultEntry.setIndexNames(
    (0, "FOUNDRY-SN-RT-L3-SWITCH-GROUP-MIB", "snRtIpTraceRouteResultIndex"),
)
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultEntry.setStatus("mandatory")
_SnRtIpTraceRouteResultIndex_Type = Integer32
_SnRtIpTraceRouteResultIndex_Object = MibTableColumn
snRtIpTraceRouteResultIndex = _SnRtIpTraceRouteResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 2, 1, 1, 1),
    _SnRtIpTraceRouteResultIndex_Type()
)
snRtIpTraceRouteResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultIndex.setStatus("mandatory")
_SnRtIpTraceRouteResultAddr_Type = IpAddress
_SnRtIpTraceRouteResultAddr_Object = MibTableColumn
snRtIpTraceRouteResultAddr = _SnRtIpTraceRouteResultAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 2, 1, 1, 2),
    _SnRtIpTraceRouteResultAddr_Type()
)
snRtIpTraceRouteResultAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultAddr.setStatus("mandatory")
_SnRtIpTraceRouteResultRoundTripTime1_Type = TimeTicks
_SnRtIpTraceRouteResultRoundTripTime1_Object = MibTableColumn
snRtIpTraceRouteResultRoundTripTime1 = _SnRtIpTraceRouteResultRoundTripTime1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 2, 1, 1, 3),
    _SnRtIpTraceRouteResultRoundTripTime1_Type()
)
snRtIpTraceRouteResultRoundTripTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultRoundTripTime1.setStatus("mandatory")
_SnRtIpTraceRouteResultRoundTripTime2_Type = TimeTicks
_SnRtIpTraceRouteResultRoundTripTime2_Object = MibTableColumn
snRtIpTraceRouteResultRoundTripTime2 = _SnRtIpTraceRouteResultRoundTripTime2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 2, 10, 2, 1, 1, 4),
    _SnRtIpTraceRouteResultRoundTripTime2_Type()
)
snRtIpTraceRouteResultRoundTripTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultRoundTripTime2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-RT-L3-SWITCH-GROUP-MIB",
    **{"RowSts": RowSts,
       "RtrStatus": RtrStatus,
       "ClearStatus": ClearStatus,
       "PortIndex": PortIndex,
       "Action": Action,
       "PhysAddress": PhysAddress,
       "NetNumber": NetNumber,
       "snIpxGen": snIpxGen,
       "snIpxClearCache": snIpxClearCache,
       "snIpxClearRoute": snIpxClearRoute,
       "snIpxClearTrafficCnts": snIpxClearTrafficCnts,
       "snIpxRcvPktsCnt": snIpxRcvPktsCnt,
       "snIpxFwdPktsCnt": snIpxFwdPktsCnt,
       "snIpxRcvFiltPktsCnt": snIpxRcvFiltPktsCnt,
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
       "snIpxPortCounters": snIpxPortCounters,
       "snIpxPortCountersTable": snIpxPortCountersTable,
       "snIpxPortCountersEntry": snIpxPortCountersEntry,
       "snIpxPortCountersPort": snIpxPortCountersPort,
       "snIpxPortCountersRcvPktsCnt": snIpxPortCountersRcvPktsCnt,
       "snIpxPortCountersFwdPktsCnt": snIpxPortCountersFwdPktsCnt,
       "snIpxPortCountersRcvFiltPktsCnt": snIpxPortCountersRcvFiltPktsCnt,
       "snRtIpGeneral": snRtIpGeneral,
       "snRtClearArpCache": snRtClearArpCache,
       "snRtClearIpCache": snRtClearIpCache,
       "snRtIpFilterTable": snRtIpFilterTable,
       "snRtIpFilterEntry": snRtIpFilterEntry,
       "snRtIpFilterIndex": snRtIpFilterIndex,
       "snRtIpFilterAction": snRtIpFilterAction,
       "snRtIpFilterProtocol": snRtIpFilterProtocol,
       "snRtIpFilterSourceIp": snRtIpFilterSourceIp,
       "snRtIpFilterSourceMask": snRtIpFilterSourceMask,
       "snRtIpFilterDestIp": snRtIpFilterDestIp,
       "snRtIpFilterDestMask": snRtIpFilterDestMask,
       "snRtIpFilterOperator": snRtIpFilterOperator,
       "snRtIpFilterOperand": snRtIpFilterOperand,
       "snRtIpFilterRowStatus": snRtIpFilterRowStatus,
       "snRtIpFilterEstablished": snRtIpFilterEstablished,
       "snRtIpFilterQosPriority": snRtIpFilterQosPriority,
       "snRtIpTraceRoute": snRtIpTraceRoute,
       "snRtIpTraceRouteGeneral": snRtIpTraceRouteGeneral,
       "snRtIpTraceRouteTargetAddr": snRtIpTraceRouteTargetAddr,
       "snRtIpTraceRouteMinTtl": snRtIpTraceRouteMinTtl,
       "snRtIpTraceRouteMaxTtl": snRtIpTraceRouteMaxTtl,
       "snRtIpTraceRouteTimeOut": snRtIpTraceRouteTimeOut,
       "snRtIpTraceRouteControl": snRtIpTraceRouteControl,
       "snRtIpTraceRouteResult": snRtIpTraceRouteResult,
       "snRtIpTraceRouteResultTable": snRtIpTraceRouteResultTable,
       "snRtIpTraceRouteResultEntry": snRtIpTraceRouteResultEntry,
       "snRtIpTraceRouteResultIndex": snRtIpTraceRouteResultIndex,
       "snRtIpTraceRouteResultAddr": snRtIpTraceRouteResultAddr,
       "snRtIpTraceRouteResultRoundTripTime1": snRtIpTraceRouteResultRoundTripTime1,
       "snRtIpTraceRouteResultRoundTripTime2": snRtIpTraceRouteResultRoundTripTime2}
)
