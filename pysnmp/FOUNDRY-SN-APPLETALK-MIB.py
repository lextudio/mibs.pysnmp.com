# SNMP MIB module (FOUNDRY-SN-APPLETALK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-APPLETALK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:50 2024
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

(Action,
 ClearStatus,
 PortIndex,
 RowSts,
 RtrStatus) = mibBuilder.importSymbols(
    "FOUNDRY-SN-IP-MIB",
    "Action",
    "ClearStatus",
    "PortIndex",
    "RowSts",
    "RtrStatus")

(router,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "router")

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

snAppleTalk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10)
)
snAppleTalk.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00")
)


# Types definitions



class ATNetworkNumber(OctetString):
    """Custom type ATNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )





class DdpNodeAddress(OctetString):
    """Custom type DdpNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )





class ATName(OctetString):
    """Custom type ATName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnRtATGeneral_ObjectIdentity = ObjectIdentity
snRtATGeneral = _SnRtATGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1)
)
_SnRtATRoutingEnable_Type = RtrStatus
_SnRtATRoutingEnable_Object = MibScalar
snRtATRoutingEnable = _SnRtATRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 1),
    _SnRtATRoutingEnable_Type()
)
snRtATRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATRoutingEnable.setStatus("current")
_SnRtATClearArpCache_Type = ClearStatus
_SnRtATClearArpCache_Object = MibScalar
snRtATClearArpCache = _SnRtATClearArpCache_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 2),
    _SnRtATClearArpCache_Type()
)
snRtATClearArpCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATClearArpCache.setStatus("current")
_SnRtATClearFwdCache_Type = ClearStatus
_SnRtATClearFwdCache_Object = MibScalar
snRtATClearFwdCache = _SnRtATClearFwdCache_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 3),
    _SnRtATClearFwdCache_Type()
)
snRtATClearFwdCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATClearFwdCache.setStatus("current")
_SnRtATClearRoute_Type = ClearStatus
_SnRtATClearRoute_Object = MibScalar
snRtATClearRoute = _SnRtATClearRoute_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 4),
    _SnRtATClearRoute_Type()
)
snRtATClearRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATClearRoute.setStatus("current")
_SnRtATClearTrafficCounters_Type = ClearStatus
_SnRtATClearTrafficCounters_Object = MibScalar
snRtATClearTrafficCounters = _SnRtATClearTrafficCounters_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 5),
    _SnRtATClearTrafficCounters_Type()
)
snRtATClearTrafficCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATClearTrafficCounters.setStatus("current")


class _SnRtATArpRetransmitCount_Type(Integer32):
    """Custom type snRtATArpRetransmitCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SnRtATArpRetransmitCount_Type.__name__ = "Integer32"
_SnRtATArpRetransmitCount_Object = MibScalar
snRtATArpRetransmitCount = _SnRtATArpRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 6),
    _SnRtATArpRetransmitCount_Type()
)
snRtATArpRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATArpRetransmitCount.setStatus("current")


class _SnRtATArpRetransmitInterval_Type(Integer32):
    """Custom type snRtATArpRetransmitInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SnRtATArpRetransmitInterval_Type.__name__ = "Integer32"
_SnRtATArpRetransmitInterval_Object = MibScalar
snRtATArpRetransmitInterval = _SnRtATArpRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 7),
    _SnRtATArpRetransmitInterval_Type()
)
snRtATArpRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATArpRetransmitInterval.setStatus("current")


class _SnRtATGleanPacketsEnable_Type(RtrStatus):
    """Custom type snRtATGleanPacketsEnable based on RtrStatus"""


_SnRtATGleanPacketsEnable_Object = MibScalar
snRtATGleanPacketsEnable = _SnRtATGleanPacketsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 8),
    _SnRtATGleanPacketsEnable_Type()
)
snRtATGleanPacketsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATGleanPacketsEnable.setStatus("current")


class _SnRtATRtmpUpdateInterval_Type(Integer32):
    """Custom type snRtATRtmpUpdateInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SnRtATRtmpUpdateInterval_Type.__name__ = "Integer32"
_SnRtATRtmpUpdateInterval_Object = MibScalar
snRtATRtmpUpdateInterval = _SnRtATRtmpUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 9),
    _SnRtATRtmpUpdateInterval_Type()
)
snRtATRtmpUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATRtmpUpdateInterval.setStatus("current")


class _SnRtATZipQueryInterval_Type(Integer32):
    """Custom type snRtATZipQueryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SnRtATZipQueryInterval_Type.__name__ = "Integer32"
_SnRtATZipQueryInterval_Object = MibScalar
snRtATZipQueryInterval = _SnRtATZipQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 10),
    _SnRtATZipQueryInterval_Type()
)
snRtATZipQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATZipQueryInterval.setStatus("current")
_SnRtATInRtmpPkts_Type = Counter32
_SnRtATInRtmpPkts_Object = MibScalar
snRtATInRtmpPkts = _SnRtATInRtmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 11),
    _SnRtATInRtmpPkts_Type()
)
snRtATInRtmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATInRtmpPkts.setStatus("current")
_SnRtATOutRtmpPkts_Type = Counter32
_SnRtATOutRtmpPkts_Object = MibScalar
snRtATOutRtmpPkts = _SnRtATOutRtmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 12),
    _SnRtATOutRtmpPkts_Type()
)
snRtATOutRtmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATOutRtmpPkts.setStatus("current")
_SnRtATFilteredRtmpPkts_Type = Counter32
_SnRtATFilteredRtmpPkts_Object = MibScalar
snRtATFilteredRtmpPkts = _SnRtATFilteredRtmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 13),
    _SnRtATFilteredRtmpPkts_Type()
)
snRtATFilteredRtmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATFilteredRtmpPkts.setStatus("current")
_SnRtATInZipPkts_Type = Counter32
_SnRtATInZipPkts_Object = MibScalar
snRtATInZipPkts = _SnRtATInZipPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 14),
    _SnRtATInZipPkts_Type()
)
snRtATInZipPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATInZipPkts.setStatus("current")
_SnRtATOutZipPkts_Type = Counter32
_SnRtATOutZipPkts_Object = MibScalar
snRtATOutZipPkts = _SnRtATOutZipPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 15),
    _SnRtATOutZipPkts_Type()
)
snRtATOutZipPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATOutZipPkts.setStatus("current")
_SnRtATInZipGZLPkts_Type = Counter32
_SnRtATInZipGZLPkts_Object = MibScalar
snRtATInZipGZLPkts = _SnRtATInZipGZLPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 16),
    _SnRtATInZipGZLPkts_Type()
)
snRtATInZipGZLPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATInZipGZLPkts.setStatus("current")
_SnRtATOutZipGZLPkts_Type = Counter32
_SnRtATOutZipGZLPkts_Object = MibScalar
snRtATOutZipGZLPkts = _SnRtATOutZipGZLPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 17),
    _SnRtATOutZipGZLPkts_Type()
)
snRtATOutZipGZLPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATOutZipGZLPkts.setStatus("current")
_SnRtATInZipNetInfoPkts_Type = Counter32
_SnRtATInZipNetInfoPkts_Object = MibScalar
snRtATInZipNetInfoPkts = _SnRtATInZipNetInfoPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 18),
    _SnRtATInZipNetInfoPkts_Type()
)
snRtATInZipNetInfoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATInZipNetInfoPkts.setStatus("current")
_SnRtATOutZipNetInfoPkts_Type = Counter32
_SnRtATOutZipNetInfoPkts_Object = MibScalar
snRtATOutZipNetInfoPkts = _SnRtATOutZipNetInfoPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 19),
    _SnRtATOutZipNetInfoPkts_Type()
)
snRtATOutZipNetInfoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATOutZipNetInfoPkts.setStatus("current")
_SnRtATInDdpPkts_Type = Counter32
_SnRtATInDdpPkts_Object = MibScalar
snRtATInDdpPkts = _SnRtATInDdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 20),
    _SnRtATInDdpPkts_Type()
)
snRtATInDdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATInDdpPkts.setStatus("current")
_SnRtATOutDdpPkts_Type = Counter32
_SnRtATOutDdpPkts_Object = MibScalar
snRtATOutDdpPkts = _SnRtATOutDdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 21),
    _SnRtATOutDdpPkts_Type()
)
snRtATOutDdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATOutDdpPkts.setStatus("current")
_SnRtATForwardedDdpPkts_Type = Counter32
_SnRtATForwardedDdpPkts_Object = MibScalar
snRtATForwardedDdpPkts = _SnRtATForwardedDdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 22),
    _SnRtATForwardedDdpPkts_Type()
)
snRtATForwardedDdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATForwardedDdpPkts.setStatus("current")
_SnRtATInDeliveredDdpPkts_Type = Counter32
_SnRtATInDeliveredDdpPkts_Object = MibScalar
snRtATInDeliveredDdpPkts = _SnRtATInDeliveredDdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 23),
    _SnRtATInDeliveredDdpPkts_Type()
)
snRtATInDeliveredDdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATInDeliveredDdpPkts.setStatus("current")
_SnRtATDroppedNoRouteDdpPkts_Type = Counter32
_SnRtATDroppedNoRouteDdpPkts_Object = MibScalar
snRtATDroppedNoRouteDdpPkts = _SnRtATDroppedNoRouteDdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 24),
    _SnRtATDroppedNoRouteDdpPkts_Type()
)
snRtATDroppedNoRouteDdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATDroppedNoRouteDdpPkts.setStatus("current")
_SnRtATDroppedBadHopCountsDdpPkts_Type = Counter32
_SnRtATDroppedBadHopCountsDdpPkts_Object = MibScalar
snRtATDroppedBadHopCountsDdpPkts = _SnRtATDroppedBadHopCountsDdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 25),
    _SnRtATDroppedBadHopCountsDdpPkts_Type()
)
snRtATDroppedBadHopCountsDdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATDroppedBadHopCountsDdpPkts.setStatus("current")
_SnRtATDroppedOtherReasonsDdpPkts_Type = Counter32
_SnRtATDroppedOtherReasonsDdpPkts_Object = MibScalar
snRtATDroppedOtherReasonsDdpPkts = _SnRtATDroppedOtherReasonsDdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 26),
    _SnRtATDroppedOtherReasonsDdpPkts_Type()
)
snRtATDroppedOtherReasonsDdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATDroppedOtherReasonsDdpPkts.setStatus("current")
_SnRtATInAarpPkts_Type = Counter32
_SnRtATInAarpPkts_Object = MibScalar
snRtATInAarpPkts = _SnRtATInAarpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 27),
    _SnRtATInAarpPkts_Type()
)
snRtATInAarpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATInAarpPkts.setStatus("current")
_SnRtATOutAarpPkts_Type = Counter32
_SnRtATOutAarpPkts_Object = MibScalar
snRtATOutAarpPkts = _SnRtATOutAarpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 1, 28),
    _SnRtATOutAarpPkts_Type()
)
snRtATOutAarpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATOutAarpPkts.setStatus("current")
_SnRtATSocketPriorityTable_Object = MibTable
snRtATSocketPriorityTable = _SnRtATSocketPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    snRtATSocketPriorityTable.setStatus("current")
_SnRtATSocketPriorityEntry_Object = MibTableRow
snRtATSocketPriorityEntry = _SnRtATSocketPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 2, 1)
)
snRtATSocketPriorityEntry.setIndexNames(
    (0, "FOUNDRY-SN-APPLETALK-MIB", "snRtATSocketPrioritySocket"),
)
if mibBuilder.loadTexts:
    snRtATSocketPriorityEntry.setStatus("current")


class _SnRtATSocketPrioritySocket_Type(Integer32):
    """Custom type snRtATSocketPrioritySocket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SnRtATSocketPrioritySocket_Type.__name__ = "Integer32"
_SnRtATSocketPrioritySocket_Object = MibTableColumn
snRtATSocketPrioritySocket = _SnRtATSocketPrioritySocket_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 2, 1, 1),
    _SnRtATSocketPrioritySocket_Type()
)
snRtATSocketPrioritySocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATSocketPrioritySocket.setStatus("current")


class _SnRtATSocketPriorityPriority_Type(Integer32):
    """Custom type snRtATSocketPriorityPriority based on Integer32"""
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


_SnRtATSocketPriorityPriority_Type.__name__ = "Integer32"
_SnRtATSocketPriorityPriority_Object = MibTableColumn
snRtATSocketPriorityPriority = _SnRtATSocketPriorityPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 2, 1, 2),
    _SnRtATSocketPriorityPriority_Type()
)
snRtATSocketPriorityPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATSocketPriorityPriority.setStatus("current")
_SnRtATPortZoneFilterTable_Object = MibTable
snRtATPortZoneFilterTable = _SnRtATPortZoneFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 3)
)
if mibBuilder.loadTexts:
    snRtATPortZoneFilterTable.setStatus("current")
_SnRtATPortZoneFilterEntry_Object = MibTableRow
snRtATPortZoneFilterEntry = _SnRtATPortZoneFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 3, 1)
)
snRtATPortZoneFilterEntry.setIndexNames(
    (0, "FOUNDRY-SN-APPLETALK-MIB", "snRtATPortZoneFilterPortIndex"),
    (0, "FOUNDRY-SN-APPLETALK-MIB", "snRtATPortZoneFilterZone"),
)
if mibBuilder.loadTexts:
    snRtATPortZoneFilterEntry.setStatus("current")
_SnRtATPortZoneFilterPortIndex_Type = PortIndex
_SnRtATPortZoneFilterPortIndex_Object = MibTableColumn
snRtATPortZoneFilterPortIndex = _SnRtATPortZoneFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 3, 1, 1),
    _SnRtATPortZoneFilterPortIndex_Type()
)
snRtATPortZoneFilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATPortZoneFilterPortIndex.setStatus("current")
_SnRtATPortZoneFilterZone_Type = ATName
_SnRtATPortZoneFilterZone_Object = MibTableColumn
snRtATPortZoneFilterZone = _SnRtATPortZoneFilterZone_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 3, 1, 2),
    _SnRtATPortZoneFilterZone_Type()
)
snRtATPortZoneFilterZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATPortZoneFilterZone.setStatus("current")
_SnRtATPortZoneFilterAction_Type = Action
_SnRtATPortZoneFilterAction_Object = MibTableColumn
snRtATPortZoneFilterAction = _SnRtATPortZoneFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 3, 1, 3),
    _SnRtATPortZoneFilterAction_Type()
)
snRtATPortZoneFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATPortZoneFilterAction.setStatus("current")
_SnRtATPortZoneFilterRtmpEnable_Type = RtrStatus
_SnRtATPortZoneFilterRtmpEnable_Object = MibTableColumn
snRtATPortZoneFilterRtmpEnable = _SnRtATPortZoneFilterRtmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 3, 1, 4),
    _SnRtATPortZoneFilterRtmpEnable_Type()
)
snRtATPortZoneFilterRtmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATPortZoneFilterRtmpEnable.setStatus("current")
_SnRtATPortZoneFilterRowStatus_Type = RowSts
_SnRtATPortZoneFilterRowStatus_Object = MibTableColumn
snRtATPortZoneFilterRowStatus = _SnRtATPortZoneFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 3, 1, 5),
    _SnRtATPortZoneFilterRowStatus_Type()
)
snRtATPortZoneFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATPortZoneFilterRowStatus.setStatus("current")
_SnRtATPortTable_Object = MibTable
snRtATPortTable = _SnRtATPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 4)
)
if mibBuilder.loadTexts:
    snRtATPortTable.setStatus("current")
_SnRtATPortEntry_Object = MibTableRow
snRtATPortEntry = _SnRtATPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 4, 1)
)
snRtATPortEntry.setIndexNames(
    (0, "FOUNDRY-SN-APPLETALK-MIB", "snRtATPortIndex"),
)
if mibBuilder.loadTexts:
    snRtATPortEntry.setStatus("current")
_SnRtATPortIndex_Type = PortIndex
_SnRtATPortIndex_Object = MibTableColumn
snRtATPortIndex = _SnRtATPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 4, 1, 1),
    _SnRtATPortIndex_Type()
)
snRtATPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATPortIndex.setStatus("current")


class _SnRtATPortArpAge_Type(Integer32):
    """Custom type snRtATPortArpAge based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SnRtATPortArpAge_Type.__name__ = "Integer32"
_SnRtATPortArpAge_Object = MibTableColumn
snRtATPortArpAge = _SnRtATPortArpAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 4, 1, 2),
    _SnRtATPortArpAge_Type()
)
snRtATPortArpAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATPortArpAge.setStatus("current")


class _SnRtATPortState_Type(Integer32):
    """Custom type snRtATPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("other", 1),
          ("up", 3))
    )


_SnRtATPortState_Type.__name__ = "Integer32"
_SnRtATPortState_Object = MibTableColumn
snRtATPortState = _SnRtATPortState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 4, 1, 3),
    _SnRtATPortState_Type()
)
snRtATPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATPortState.setStatus("current")


class _SnRtATPortSeedRouter_Type(Integer32):
    """Custom type snRtATPortSeedRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonSeedRouter", 3),
          ("other", 1),
          ("seedRouter", 2))
    )


_SnRtATPortSeedRouter_Type.__name__ = "Integer32"
_SnRtATPortSeedRouter_Object = MibTableColumn
snRtATPortSeedRouter = _SnRtATPortSeedRouter_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 4, 1, 4),
    _SnRtATPortSeedRouter_Type()
)
snRtATPortSeedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATPortSeedRouter.setStatus("current")


class _SnRtATPortOperationMode_Type(Integer32):
    """Custom type snRtATPortOperationMode based on Integer32"""
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
        *(("nonSeedRouter", 3),
          ("notOperational", 4),
          ("other", 1),
          ("routingDisabled", 5),
          ("seedRouter", 2))
    )


_SnRtATPortOperationMode_Type.__name__ = "Integer32"
_SnRtATPortOperationMode_Object = MibTableColumn
snRtATPortOperationMode = _SnRtATPortOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 4, 1, 5),
    _SnRtATPortOperationMode_Type()
)
snRtATPortOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATPortOperationMode.setStatus("current")
_SnRtATFwdCacheTable_Object = MibTable
snRtATFwdCacheTable = _SnRtATFwdCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 5)
)
if mibBuilder.loadTexts:
    snRtATFwdCacheTable.setStatus("current")
_SnRtATFwdCacheEntry_Object = MibTableRow
snRtATFwdCacheEntry = _SnRtATFwdCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 5, 1)
)
snRtATFwdCacheEntry.setIndexNames(
    (0, "FOUNDRY-SN-APPLETALK-MIB", "snRtATFwdCacheIndex"),
)
if mibBuilder.loadTexts:
    snRtATFwdCacheEntry.setStatus("current")
_SnRtATFwdCacheIndex_Type = Integer32
_SnRtATFwdCacheIndex_Object = MibTableColumn
snRtATFwdCacheIndex = _SnRtATFwdCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 5, 1, 1),
    _SnRtATFwdCacheIndex_Type()
)
snRtATFwdCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATFwdCacheIndex.setStatus("current")
_SnRtATFwdCacheNetAddr_Type = DdpNodeAddress
_SnRtATFwdCacheNetAddr_Object = MibTableColumn
snRtATFwdCacheNetAddr = _SnRtATFwdCacheNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 5, 1, 2),
    _SnRtATFwdCacheNetAddr_Type()
)
snRtATFwdCacheNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATFwdCacheNetAddr.setStatus("current")


class _SnRtATFwdCacheMacAddr_Type(OctetString):
    """Custom type snRtATFwdCacheMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SnRtATFwdCacheMacAddr_Type.__name__ = "OctetString"
_SnRtATFwdCacheMacAddr_Object = MibTableColumn
snRtATFwdCacheMacAddr = _SnRtATFwdCacheMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 5, 1, 3),
    _SnRtATFwdCacheMacAddr_Type()
)
snRtATFwdCacheMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATFwdCacheMacAddr.setStatus("current")
_SnRtATFwdCacheNextHop_Type = DdpNodeAddress
_SnRtATFwdCacheNextHop_Object = MibTableColumn
snRtATFwdCacheNextHop = _SnRtATFwdCacheNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 5, 1, 4),
    _SnRtATFwdCacheNextHop_Type()
)
snRtATFwdCacheNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATFwdCacheNextHop.setStatus("current")
_SnRtATFwdCacheOutgoingPort_Type = Integer32
_SnRtATFwdCacheOutgoingPort_Object = MibTableColumn
snRtATFwdCacheOutgoingPort = _SnRtATFwdCacheOutgoingPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 5, 1, 5),
    _SnRtATFwdCacheOutgoingPort_Type()
)
snRtATFwdCacheOutgoingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATFwdCacheOutgoingPort.setStatus("current")


class _SnRtATFwdCacheType_Type(Integer32):
    """Custom type snRtATFwdCacheType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_SnRtATFwdCacheType_Type.__name__ = "Integer32"
_SnRtATFwdCacheType_Object = MibTableColumn
snRtATFwdCacheType = _SnRtATFwdCacheType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 5, 1, 6),
    _SnRtATFwdCacheType_Type()
)
snRtATFwdCacheType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATFwdCacheType.setStatus("current")


class _SnRtATFwdCacheAction_Type(Integer32):
    """Custom type snRtATFwdCacheAction based on Integer32"""
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
        *(("dropPacket", 5),
          ("forUs", 3),
          ("forward", 2),
          ("other", 1),
          ("waitForArp", 4))
    )


_SnRtATFwdCacheAction_Type.__name__ = "Integer32"
_SnRtATFwdCacheAction_Object = MibTableColumn
snRtATFwdCacheAction = _SnRtATFwdCacheAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 5, 1, 7),
    _SnRtATFwdCacheAction_Type()
)
snRtATFwdCacheAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATFwdCacheAction.setStatus("current")
_SnRtATFwdCacheVLanId_Type = Integer32
_SnRtATFwdCacheVLanId_Object = MibTableColumn
snRtATFwdCacheVLanId = _SnRtATFwdCacheVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 5, 1, 8),
    _SnRtATFwdCacheVLanId_Type()
)
snRtATFwdCacheVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATFwdCacheVLanId.setStatus("current")
_SnRtATZoneTable_Object = MibTable
snRtATZoneTable = _SnRtATZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 6)
)
if mibBuilder.loadTexts:
    snRtATZoneTable.setStatus("current")
_SnRtATZoneEntry_Object = MibTableRow
snRtATZoneEntry = _SnRtATZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 6, 1)
)
snRtATZoneEntry.setIndexNames(
    (0, "FOUNDRY-SN-APPLETALK-MIB", "snRtATZoneIndex"),
)
if mibBuilder.loadTexts:
    snRtATZoneEntry.setStatus("current")
_SnRtATZoneIndex_Type = Integer32
_SnRtATZoneIndex_Object = MibTableColumn
snRtATZoneIndex = _SnRtATZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 6, 1, 1),
    _SnRtATZoneIndex_Type()
)
snRtATZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATZoneIndex.setStatus("current")
_SnRtATZoneNetStart_Type = ATNetworkNumber
_SnRtATZoneNetStart_Object = MibTableColumn
snRtATZoneNetStart = _SnRtATZoneNetStart_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 6, 1, 2),
    _SnRtATZoneNetStart_Type()
)
snRtATZoneNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATZoneNetStart.setStatus("current")
_SnRtATZoneNetEnd_Type = ATNetworkNumber
_SnRtATZoneNetEnd_Object = MibTableColumn
snRtATZoneNetEnd = _SnRtATZoneNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 6, 1, 3),
    _SnRtATZoneNetEnd_Type()
)
snRtATZoneNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATZoneNetEnd.setStatus("current")
_SnRtATZoneName_Type = ATName
_SnRtATZoneName_Object = MibTableColumn
snRtATZoneName = _SnRtATZoneName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 6, 1, 4),
    _SnRtATZoneName_Type()
)
snRtATZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATZoneName.setStatus("current")
_SnRtATAddZoneFilterTable_Object = MibTable
snRtATAddZoneFilterTable = _SnRtATAddZoneFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 7)
)
if mibBuilder.loadTexts:
    snRtATAddZoneFilterTable.setStatus("current")
_SnRtATAddZoneFilterEntry_Object = MibTableRow
snRtATAddZoneFilterEntry = _SnRtATAddZoneFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 7, 1)
)
snRtATAddZoneFilterEntry.setIndexNames(
    (0, "FOUNDRY-SN-APPLETALK-MIB", "snRtATAddZoneFilterPortIndex"),
)
if mibBuilder.loadTexts:
    snRtATAddZoneFilterEntry.setStatus("current")
_SnRtATAddZoneFilterPortIndex_Type = PortIndex
_SnRtATAddZoneFilterPortIndex_Object = MibTableColumn
snRtATAddZoneFilterPortIndex = _SnRtATAddZoneFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 7, 1, 1),
    _SnRtATAddZoneFilterPortIndex_Type()
)
snRtATAddZoneFilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtATAddZoneFilterPortIndex.setStatus("current")
_SnRtATAddZoneFilterAction_Type = Action
_SnRtATAddZoneFilterAction_Object = MibTableColumn
snRtATAddZoneFilterAction = _SnRtATAddZoneFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 7, 1, 2),
    _SnRtATAddZoneFilterAction_Type()
)
snRtATAddZoneFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATAddZoneFilterAction.setStatus("current")
_SnRtATAddZoneFilterRtmpEnable_Type = RtrStatus
_SnRtATAddZoneFilterRtmpEnable_Object = MibTableColumn
snRtATAddZoneFilterRtmpEnable = _SnRtATAddZoneFilterRtmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 10, 7, 1, 3),
    _SnRtATAddZoneFilterRtmpEnable_Type()
)
snRtATAddZoneFilterRtmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtATAddZoneFilterRtmpEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-APPLETALK-MIB",
    **{"ATNetworkNumber": ATNetworkNumber,
       "DdpNodeAddress": DdpNodeAddress,
       "ATName": ATName,
       "snAppleTalk": snAppleTalk,
       "snRtATGeneral": snRtATGeneral,
       "snRtATRoutingEnable": snRtATRoutingEnable,
       "snRtATClearArpCache": snRtATClearArpCache,
       "snRtATClearFwdCache": snRtATClearFwdCache,
       "snRtATClearRoute": snRtATClearRoute,
       "snRtATClearTrafficCounters": snRtATClearTrafficCounters,
       "snRtATArpRetransmitCount": snRtATArpRetransmitCount,
       "snRtATArpRetransmitInterval": snRtATArpRetransmitInterval,
       "snRtATGleanPacketsEnable": snRtATGleanPacketsEnable,
       "snRtATRtmpUpdateInterval": snRtATRtmpUpdateInterval,
       "snRtATZipQueryInterval": snRtATZipQueryInterval,
       "snRtATInRtmpPkts": snRtATInRtmpPkts,
       "snRtATOutRtmpPkts": snRtATOutRtmpPkts,
       "snRtATFilteredRtmpPkts": snRtATFilteredRtmpPkts,
       "snRtATInZipPkts": snRtATInZipPkts,
       "snRtATOutZipPkts": snRtATOutZipPkts,
       "snRtATInZipGZLPkts": snRtATInZipGZLPkts,
       "snRtATOutZipGZLPkts": snRtATOutZipGZLPkts,
       "snRtATInZipNetInfoPkts": snRtATInZipNetInfoPkts,
       "snRtATOutZipNetInfoPkts": snRtATOutZipNetInfoPkts,
       "snRtATInDdpPkts": snRtATInDdpPkts,
       "snRtATOutDdpPkts": snRtATOutDdpPkts,
       "snRtATForwardedDdpPkts": snRtATForwardedDdpPkts,
       "snRtATInDeliveredDdpPkts": snRtATInDeliveredDdpPkts,
       "snRtATDroppedNoRouteDdpPkts": snRtATDroppedNoRouteDdpPkts,
       "snRtATDroppedBadHopCountsDdpPkts": snRtATDroppedBadHopCountsDdpPkts,
       "snRtATDroppedOtherReasonsDdpPkts": snRtATDroppedOtherReasonsDdpPkts,
       "snRtATInAarpPkts": snRtATInAarpPkts,
       "snRtATOutAarpPkts": snRtATOutAarpPkts,
       "snRtATSocketPriorityTable": snRtATSocketPriorityTable,
       "snRtATSocketPriorityEntry": snRtATSocketPriorityEntry,
       "snRtATSocketPrioritySocket": snRtATSocketPrioritySocket,
       "snRtATSocketPriorityPriority": snRtATSocketPriorityPriority,
       "snRtATPortZoneFilterTable": snRtATPortZoneFilterTable,
       "snRtATPortZoneFilterEntry": snRtATPortZoneFilterEntry,
       "snRtATPortZoneFilterPortIndex": snRtATPortZoneFilterPortIndex,
       "snRtATPortZoneFilterZone": snRtATPortZoneFilterZone,
       "snRtATPortZoneFilterAction": snRtATPortZoneFilterAction,
       "snRtATPortZoneFilterRtmpEnable": snRtATPortZoneFilterRtmpEnable,
       "snRtATPortZoneFilterRowStatus": snRtATPortZoneFilterRowStatus,
       "snRtATPortTable": snRtATPortTable,
       "snRtATPortEntry": snRtATPortEntry,
       "snRtATPortIndex": snRtATPortIndex,
       "snRtATPortArpAge": snRtATPortArpAge,
       "snRtATPortState": snRtATPortState,
       "snRtATPortSeedRouter": snRtATPortSeedRouter,
       "snRtATPortOperationMode": snRtATPortOperationMode,
       "snRtATFwdCacheTable": snRtATFwdCacheTable,
       "snRtATFwdCacheEntry": snRtATFwdCacheEntry,
       "snRtATFwdCacheIndex": snRtATFwdCacheIndex,
       "snRtATFwdCacheNetAddr": snRtATFwdCacheNetAddr,
       "snRtATFwdCacheMacAddr": snRtATFwdCacheMacAddr,
       "snRtATFwdCacheNextHop": snRtATFwdCacheNextHop,
       "snRtATFwdCacheOutgoingPort": snRtATFwdCacheOutgoingPort,
       "snRtATFwdCacheType": snRtATFwdCacheType,
       "snRtATFwdCacheAction": snRtATFwdCacheAction,
       "snRtATFwdCacheVLanId": snRtATFwdCacheVLanId,
       "snRtATZoneTable": snRtATZoneTable,
       "snRtATZoneEntry": snRtATZoneEntry,
       "snRtATZoneIndex": snRtATZoneIndex,
       "snRtATZoneNetStart": snRtATZoneNetStart,
       "snRtATZoneNetEnd": snRtATZoneNetEnd,
       "snRtATZoneName": snRtATZoneName,
       "snRtATAddZoneFilterTable": snRtATAddZoneFilterTable,
       "snRtATAddZoneFilterEntry": snRtATAddZoneFilterEntry,
       "snRtATAddZoneFilterPortIndex": snRtATAddZoneFilterPortIndex,
       "snRtATAddZoneFilterAction": snRtATAddZoneFilterAction,
       "snRtATAddZoneFilterRtmpEnable": snRtATAddZoneFilterRtmpEnable}
)
