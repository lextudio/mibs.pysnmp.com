# SNMP MIB module (IPX-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPX-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:34 2024
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

(cjnProtocol,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnProtocol")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cjnIpx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3)
)


# Types definitions



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class NodeNumber(OctetString):
    """Custom type NodeNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class ServiceType(OctetString):
    """Custom type ServiceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )





class ServiceName(OctetString):
    """Custom type ServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )





class ServiceSocket(OctetString):
    """Custom type ServiceSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnIpxGlobalGroup_ObjectIdentity = ObjectIdentity
cjnIpxGlobalGroup = _CjnIpxGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 1)
)


class _CjnIpxEnabled_Type(Integer32):
    """Custom type cjnIpxEnabled based on Integer32"""
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


_CjnIpxEnabled_Type.__name__ = "Integer32"
_CjnIpxEnabled_Object = MibScalar
cjnIpxEnabled = _CjnIpxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 1, 1),
    _CjnIpxEnabled_Type()
)
cjnIpxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpxEnabled.setStatus("current")
_CjnIpxGlobalStatsGroup_ObjectIdentity = ObjectIdentity
cjnIpxGlobalStatsGroup = _CjnIpxGlobalStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4)
)
_CjnIpxInReceives_Type = Counter32
_CjnIpxInReceives_Object = MibScalar
cjnIpxInReceives = _CjnIpxInReceives_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 1),
    _CjnIpxInReceives_Type()
)
cjnIpxInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxInReceives.setStatus("current")
_CjnIpxInDelivers_Type = Counter32
_CjnIpxInDelivers_Object = MibScalar
cjnIpxInDelivers = _CjnIpxInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 2),
    _CjnIpxInDelivers_Type()
)
cjnIpxInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxInDelivers.setStatus("current")
_CjnIpxForwarded_Type = Counter32
_CjnIpxForwarded_Object = MibScalar
cjnIpxForwarded = _CjnIpxForwarded_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 3),
    _CjnIpxForwarded_Type()
)
cjnIpxForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxForwarded.setStatus("current")
_CjnIpxNetBIOSReceives_Type = Counter32
_CjnIpxNetBIOSReceives_Object = MibScalar
cjnIpxNetBIOSReceives = _CjnIpxNetBIOSReceives_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 4),
    _CjnIpxNetBIOSReceives_Type()
)
cjnIpxNetBIOSReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxNetBIOSReceives.setStatus("current")
_CjnIpxInDiscards_Type = Counter32
_CjnIpxInDiscards_Object = MibScalar
cjnIpxInDiscards = _CjnIpxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 5),
    _CjnIpxInDiscards_Type()
)
cjnIpxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxInDiscards.setStatus("current")
_CjnIpxInHdrErrors_Type = Counter32
_CjnIpxInHdrErrors_Object = MibScalar
cjnIpxInHdrErrors = _CjnIpxInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 6),
    _CjnIpxInHdrErrors_Type()
)
cjnIpxInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxInHdrErrors.setStatus("current")
_CjnIpxInUnknownSockets_Type = Counter32
_CjnIpxInUnknownSockets_Object = MibScalar
cjnIpxInUnknownSockets = _CjnIpxInUnknownSockets_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 7),
    _CjnIpxInUnknownSockets_Type()
)
cjnIpxInUnknownSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxInUnknownSockets.setStatus("current")
_CjnIpxInTooManyHops_Type = Counter32
_CjnIpxInTooManyHops_Object = MibScalar
cjnIpxInTooManyHops = _CjnIpxInTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 8),
    _CjnIpxInTooManyHops_Type()
)
cjnIpxInTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxInTooManyHops.setStatus("current")
_CjnIpxInBadChecksums_Type = Counter32
_CjnIpxInBadChecksums_Object = MibScalar
cjnIpxInBadChecksums = _CjnIpxInBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 9),
    _CjnIpxInBadChecksums_Type()
)
cjnIpxInBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxInBadChecksums.setStatus("current")
_CjnIpxOutRequests_Type = Counter32
_CjnIpxOutRequests_Object = MibScalar
cjnIpxOutRequests = _CjnIpxOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 10),
    _CjnIpxOutRequests_Type()
)
cjnIpxOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxOutRequests.setStatus("current")
_CjnIpxOutPackets_Type = Counter32
_CjnIpxOutPackets_Object = MibScalar
cjnIpxOutPackets = _CjnIpxOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 11),
    _CjnIpxOutPackets_Type()
)
cjnIpxOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxOutPackets.setStatus("current")
_CjnIpxOutDiscards_Type = Counter32
_CjnIpxOutDiscards_Object = MibScalar
cjnIpxOutDiscards = _CjnIpxOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 12),
    _CjnIpxOutDiscards_Type()
)
cjnIpxOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxOutDiscards.setStatus("current")
_CjnIpxOutNoRoutes_Type = Counter32
_CjnIpxOutNoRoutes_Object = MibScalar
cjnIpxOutNoRoutes = _CjnIpxOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 13),
    _CjnIpxOutNoRoutes_Type()
)
cjnIpxOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxOutNoRoutes.setStatus("current")
_CjnIpxInPingRequests_Type = Counter32
_CjnIpxInPingRequests_Object = MibScalar
cjnIpxInPingRequests = _CjnIpxInPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 14),
    _CjnIpxInPingRequests_Type()
)
cjnIpxInPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxInPingRequests.setStatus("current")
_CjnIpxInPingReplies_Type = Counter32
_CjnIpxInPingReplies_Object = MibScalar
cjnIpxInPingReplies = _CjnIpxInPingReplies_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 15),
    _CjnIpxInPingReplies_Type()
)
cjnIpxInPingReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxInPingReplies.setStatus("current")
_CjnIpxOutPingRequests_Type = Counter32
_CjnIpxOutPingRequests_Object = MibScalar
cjnIpxOutPingRequests = _CjnIpxOutPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 16),
    _CjnIpxOutPingRequests_Type()
)
cjnIpxOutPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxOutPingRequests.setStatus("current")
_CjnIpxOutPingReplies_Type = Counter32
_CjnIpxOutPingReplies_Object = MibScalar
cjnIpxOutPingReplies = _CjnIpxOutPingReplies_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 17),
    _CjnIpxOutPingReplies_Type()
)
cjnIpxOutPingReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxOutPingReplies.setStatus("current")


class _CjnIpxGlobalStatsReset_Type(Integer32):
    """Custom type cjnIpxGlobalStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CjnIpxGlobalStatsReset_Type.__name__ = "Integer32"
_CjnIpxGlobalStatsReset_Object = MibScalar
cjnIpxGlobalStatsReset = _CjnIpxGlobalStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 18),
    _CjnIpxGlobalStatsReset_Type()
)
cjnIpxGlobalStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpxGlobalStatsReset.setStatus("current")
_CjnIpxRouteGroup_ObjectIdentity = ObjectIdentity
cjnIpxRouteGroup = _CjnIpxRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5)
)


class _CjnIpxMaxRoutes_Type(Integer32):
    """Custom type cjnIpxMaxRoutes based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240),
    )


_CjnIpxMaxRoutes_Type.__name__ = "Integer32"
_CjnIpxMaxRoutes_Object = MibScalar
cjnIpxMaxRoutes = _CjnIpxMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 1),
    _CjnIpxMaxRoutes_Type()
)
cjnIpxMaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpxMaxRoutes.setStatus("current")


class _CjnIpxDefaultRouteEnabled_Type(Integer32):
    """Custom type cjnIpxDefaultRouteEnabled based on Integer32"""
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


_CjnIpxDefaultRouteEnabled_Type.__name__ = "Integer32"
_CjnIpxDefaultRouteEnabled_Object = MibScalar
cjnIpxDefaultRouteEnabled = _CjnIpxDefaultRouteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 2),
    _CjnIpxDefaultRouteEnabled_Type()
)
cjnIpxDefaultRouteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpxDefaultRouteEnabled.setStatus("current")
_CjnIpxNumRoutes_Type = Counter32
_CjnIpxNumRoutes_Object = MibScalar
cjnIpxNumRoutes = _CjnIpxNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 3),
    _CjnIpxNumRoutes_Type()
)
cjnIpxNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxNumRoutes.setStatus("current")
_CjnIpxPeakNumRoutes_Type = Counter32
_CjnIpxPeakNumRoutes_Object = MibScalar
cjnIpxPeakNumRoutes = _CjnIpxPeakNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 4),
    _CjnIpxPeakNumRoutes_Type()
)
cjnIpxPeakNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxPeakNumRoutes.setStatus("current")
_CjnIpxRouteAddFailures_Type = Counter32
_CjnIpxRouteAddFailures_Object = MibScalar
cjnIpxRouteAddFailures = _CjnIpxRouteAddFailures_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 5),
    _CjnIpxRouteAddFailures_Type()
)
cjnIpxRouteAddFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRouteAddFailures.setStatus("current")
_CjnIpxStaticRouteGroup_ObjectIdentity = ObjectIdentity
cjnIpxStaticRouteGroup = _CjnIpxStaticRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6)
)
_CjnIpxStaticRouteTable_Object = MibTable
cjnIpxStaticRouteTable = _CjnIpxStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1)
)
if mibBuilder.loadTexts:
    cjnIpxStaticRouteTable.setStatus("current")
_CjnIpxStaticRouteEntry_Object = MibTableRow
cjnIpxStaticRouteEntry = _CjnIpxStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1)
)
cjnIpxStaticRouteEntry.setIndexNames(
    (0, "IPX-PRIVATE-MIB", "cjnIpxStaticRouteNet"),
)
if mibBuilder.loadTexts:
    cjnIpxStaticRouteEntry.setStatus("current")
_CjnIpxStaticRouteNet_Type = NetNumber
_CjnIpxStaticRouteNet_Object = MibTableColumn
cjnIpxStaticRouteNet = _CjnIpxStaticRouteNet_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 1),
    _CjnIpxStaticRouteNet_Type()
)
cjnIpxStaticRouteNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxStaticRouteNet.setStatus("current")
_CjnIpxStaticRouteRowStatus_Type = RowStatus
_CjnIpxStaticRouteRowStatus_Object = MibTableColumn
cjnIpxStaticRouteRowStatus = _CjnIpxStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 2),
    _CjnIpxStaticRouteRowStatus_Type()
)
cjnIpxStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticRouteRowStatus.setStatus("current")
_CjnIpxStaticRouteIfIndex_Type = Integer32
_CjnIpxStaticRouteIfIndex_Object = MibTableColumn
cjnIpxStaticRouteIfIndex = _CjnIpxStaticRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 3),
    _CjnIpxStaticRouteIfIndex_Type()
)
cjnIpxStaticRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticRouteIfIndex.setStatus("current")
_CjnIpxStaticRouteNextHopNode_Type = NodeNumber
_CjnIpxStaticRouteNextHopNode_Object = MibTableColumn
cjnIpxStaticRouteNextHopNode = _CjnIpxStaticRouteNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 4),
    _CjnIpxStaticRouteNextHopNode_Type()
)
cjnIpxStaticRouteNextHopNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticRouteNextHopNode.setStatus("current")
_CjnIpxStaticRouteTicks_Type = Integer32
_CjnIpxStaticRouteTicks_Object = MibTableColumn
cjnIpxStaticRouteTicks = _CjnIpxStaticRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 5),
    _CjnIpxStaticRouteTicks_Type()
)
cjnIpxStaticRouteTicks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticRouteTicks.setStatus("current")
_CjnIpxStaticRouteHops_Type = Integer32
_CjnIpxStaticRouteHops_Object = MibTableColumn
cjnIpxStaticRouteHops = _CjnIpxStaticRouteHops_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 6),
    _CjnIpxStaticRouteHops_Type()
)
cjnIpxStaticRouteHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticRouteHops.setStatus("current")
_CjnIpxRouteTable_Object = MibTable
cjnIpxRouteTable = _CjnIpxRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7)
)
if mibBuilder.loadTexts:
    cjnIpxRouteTable.setStatus("current")
_CjnIpxRouteEntry_Object = MibTableRow
cjnIpxRouteEntry = _CjnIpxRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1)
)
cjnIpxRouteEntry.setIndexNames(
    (0, "IPX-PRIVATE-MIB", "cjnIpxRouteNet"),
)
if mibBuilder.loadTexts:
    cjnIpxRouteEntry.setStatus("current")
_CjnIpxRouteNet_Type = NetNumber
_CjnIpxRouteNet_Object = MibTableColumn
cjnIpxRouteNet = _CjnIpxRouteNet_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 1),
    _CjnIpxRouteNet_Type()
)
cjnIpxRouteNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRouteNet.setStatus("current")
_CjnIpxRouteRowStatus_Type = RowStatus
_CjnIpxRouteRowStatus_Object = MibTableColumn
cjnIpxRouteRowStatus = _CjnIpxRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 2),
    _CjnIpxRouteRowStatus_Type()
)
cjnIpxRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRouteRowStatus.setStatus("current")
_CjnIpxRouteIfIndex_Type = Integer32
_CjnIpxRouteIfIndex_Object = MibTableColumn
cjnIpxRouteIfIndex = _CjnIpxRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 3),
    _CjnIpxRouteIfIndex_Type()
)
cjnIpxRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRouteIfIndex.setStatus("current")
_CjnIpxRouteNextHopNode_Type = NodeNumber
_CjnIpxRouteNextHopNode_Object = MibTableColumn
cjnIpxRouteNextHopNode = _CjnIpxRouteNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 4),
    _CjnIpxRouteNextHopNode_Type()
)
cjnIpxRouteNextHopNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRouteNextHopNode.setStatus("current")
_CjnIpxRouteTicks_Type = Integer32
_CjnIpxRouteTicks_Object = MibTableColumn
cjnIpxRouteTicks = _CjnIpxRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 5),
    _CjnIpxRouteTicks_Type()
)
cjnIpxRouteTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRouteTicks.setStatus("current")
_CjnIpxRouteHops_Type = Integer32
_CjnIpxRouteHops_Object = MibTableColumn
cjnIpxRouteHops = _CjnIpxRouteHops_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 6),
    _CjnIpxRouteHops_Type()
)
cjnIpxRouteHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRouteHops.setStatus("current")


class _CjnIpxRouteProtocol_Type(Integer32):
    """Custom type cjnIpxRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("rip", 2),
          ("static", 3))
    )


_CjnIpxRouteProtocol_Type.__name__ = "Integer32"
_CjnIpxRouteProtocol_Object = MibTableColumn
cjnIpxRouteProtocol = _CjnIpxRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 7),
    _CjnIpxRouteProtocol_Type()
)
cjnIpxRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRouteProtocol.setStatus("current")
_CjnIpxServicesGroup_ObjectIdentity = ObjectIdentity
cjnIpxServicesGroup = _CjnIpxServicesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6)
)


class _CjnIpxMaxServices_Type(Integer32):
    """Custom type cjnIpxMaxServices based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240),
    )


_CjnIpxMaxServices_Type.__name__ = "Integer32"
_CjnIpxMaxServices_Object = MibScalar
cjnIpxMaxServices = _CjnIpxMaxServices_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 1),
    _CjnIpxMaxServices_Type()
)
cjnIpxMaxServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpxMaxServices.setStatus("current")
_CjnIpxNumServices_Type = Counter32
_CjnIpxNumServices_Object = MibScalar
cjnIpxNumServices = _CjnIpxNumServices_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 2),
    _CjnIpxNumServices_Type()
)
cjnIpxNumServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxNumServices.setStatus("current")
_CjnIpxPeakNumServices_Type = Counter32
_CjnIpxPeakNumServices_Object = MibScalar
cjnIpxPeakNumServices = _CjnIpxPeakNumServices_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 3),
    _CjnIpxPeakNumServices_Type()
)
cjnIpxPeakNumServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxPeakNumServices.setStatus("current")
_CjnIpxServiceAddFailures_Type = Counter32
_CjnIpxServiceAddFailures_Object = MibScalar
cjnIpxServiceAddFailures = _CjnIpxServiceAddFailures_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 4),
    _CjnIpxServiceAddFailures_Type()
)
cjnIpxServiceAddFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxServiceAddFailures.setStatus("current")
_CjnIpxStaticServiceGroup_ObjectIdentity = ObjectIdentity
cjnIpxStaticServiceGroup = _CjnIpxStaticServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5)
)
_CjnIpxStaticServiceTable_Object = MibTable
cjnIpxStaticServiceTable = _CjnIpxStaticServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1)
)
if mibBuilder.loadTexts:
    cjnIpxStaticServiceTable.setStatus("current")
_CjnIpxStaticServiceEntry_Object = MibTableRow
cjnIpxStaticServiceEntry = _CjnIpxStaticServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1)
)
cjnIpxStaticServiceEntry.setIndexNames(
    (0, "IPX-PRIVATE-MIB", "cjnIpxStaticServiceType"),
    (0, "IPX-PRIVATE-MIB", "cjnIpxStaticServiceName"),
)
if mibBuilder.loadTexts:
    cjnIpxStaticServiceEntry.setStatus("current")
_CjnIpxStaticServiceType_Type = ServiceType
_CjnIpxStaticServiceType_Object = MibTableColumn
cjnIpxStaticServiceType = _CjnIpxStaticServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 1),
    _CjnIpxStaticServiceType_Type()
)
cjnIpxStaticServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxStaticServiceType.setStatus("current")
_CjnIpxStaticServiceName_Type = ServiceName
_CjnIpxStaticServiceName_Object = MibTableColumn
cjnIpxStaticServiceName = _CjnIpxStaticServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 2),
    _CjnIpxStaticServiceName_Type()
)
cjnIpxStaticServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxStaticServiceName.setStatus("current")
_CjnIpxStaticServiceRowStatus_Type = RowStatus
_CjnIpxStaticServiceRowStatus_Object = MibTableColumn
cjnIpxStaticServiceRowStatus = _CjnIpxStaticServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 3),
    _CjnIpxStaticServiceRowStatus_Type()
)
cjnIpxStaticServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticServiceRowStatus.setStatus("current")
_CjnIpxStaticServiceNet_Type = NetNumber
_CjnIpxStaticServiceNet_Object = MibTableColumn
cjnIpxStaticServiceNet = _CjnIpxStaticServiceNet_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 4),
    _CjnIpxStaticServiceNet_Type()
)
cjnIpxStaticServiceNet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticServiceNet.setStatus("current")
_CjnIpxStaticServiceNode_Type = NodeNumber
_CjnIpxStaticServiceNode_Object = MibTableColumn
cjnIpxStaticServiceNode = _CjnIpxStaticServiceNode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 5),
    _CjnIpxStaticServiceNode_Type()
)
cjnIpxStaticServiceNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticServiceNode.setStatus("current")
_CjnIpxStaticServiceSocket_Type = ServiceSocket
_CjnIpxStaticServiceSocket_Object = MibTableColumn
cjnIpxStaticServiceSocket = _CjnIpxStaticServiceSocket_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 6),
    _CjnIpxStaticServiceSocket_Type()
)
cjnIpxStaticServiceSocket.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticServiceSocket.setStatus("current")
_CjnIpxStaticServiceIfIndex_Type = Integer32
_CjnIpxStaticServiceIfIndex_Object = MibTableColumn
cjnIpxStaticServiceIfIndex = _CjnIpxStaticServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 7),
    _CjnIpxStaticServiceIfIndex_Type()
)
cjnIpxStaticServiceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticServiceIfIndex.setStatus("current")
_CjnIpxStaticServiceNextHopNode_Type = NodeNumber
_CjnIpxStaticServiceNextHopNode_Object = MibTableColumn
cjnIpxStaticServiceNextHopNode = _CjnIpxStaticServiceNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 8),
    _CjnIpxStaticServiceNextHopNode_Type()
)
cjnIpxStaticServiceNextHopNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticServiceNextHopNode.setStatus("current")
_CjnIpxStaticServiceHops_Type = Integer32
_CjnIpxStaticServiceHops_Object = MibTableColumn
cjnIpxStaticServiceHops = _CjnIpxStaticServiceHops_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 9),
    _CjnIpxStaticServiceHops_Type()
)
cjnIpxStaticServiceHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxStaticServiceHops.setStatus("current")
_CjnIpxServiceTable_Object = MibTable
cjnIpxServiceTable = _CjnIpxServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6)
)
if mibBuilder.loadTexts:
    cjnIpxServiceTable.setStatus("current")
_CjnIpxServiceEntry_Object = MibTableRow
cjnIpxServiceEntry = _CjnIpxServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1)
)
cjnIpxServiceEntry.setIndexNames(
    (0, "IPX-PRIVATE-MIB", "cjnIpxServiceType"),
    (0, "IPX-PRIVATE-MIB", "cjnIpxServiceName"),
)
if mibBuilder.loadTexts:
    cjnIpxServiceEntry.setStatus("current")
_CjnIpxServiceType_Type = ServiceType
_CjnIpxServiceType_Object = MibTableColumn
cjnIpxServiceType = _CjnIpxServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 1),
    _CjnIpxServiceType_Type()
)
cjnIpxServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxServiceType.setStatus("current")
_CjnIpxServiceName_Type = ServiceName
_CjnIpxServiceName_Object = MibTableColumn
cjnIpxServiceName = _CjnIpxServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 2),
    _CjnIpxServiceName_Type()
)
cjnIpxServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxServiceName.setStatus("current")
_CjnIpxServiceRowStatus_Type = RowStatus
_CjnIpxServiceRowStatus_Object = MibTableColumn
cjnIpxServiceRowStatus = _CjnIpxServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 3),
    _CjnIpxServiceRowStatus_Type()
)
cjnIpxServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxServiceRowStatus.setStatus("current")
_CjnIpxServiceNet_Type = NetNumber
_CjnIpxServiceNet_Object = MibTableColumn
cjnIpxServiceNet = _CjnIpxServiceNet_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 4),
    _CjnIpxServiceNet_Type()
)
cjnIpxServiceNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxServiceNet.setStatus("current")
_CjnIpxServiceNode_Type = NodeNumber
_CjnIpxServiceNode_Object = MibTableColumn
cjnIpxServiceNode = _CjnIpxServiceNode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 5),
    _CjnIpxServiceNode_Type()
)
cjnIpxServiceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxServiceNode.setStatus("current")
_CjnIpxServiceSocket_Type = ServiceSocket
_CjnIpxServiceSocket_Object = MibTableColumn
cjnIpxServiceSocket = _CjnIpxServiceSocket_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 6),
    _CjnIpxServiceSocket_Type()
)
cjnIpxServiceSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxServiceSocket.setStatus("current")
_CjnIpxServiceIfIndex_Type = Integer32
_CjnIpxServiceIfIndex_Object = MibTableColumn
cjnIpxServiceIfIndex = _CjnIpxServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 7),
    _CjnIpxServiceIfIndex_Type()
)
cjnIpxServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxServiceIfIndex.setStatus("current")
_CjnIpxServiceNextHopNode_Type = NodeNumber
_CjnIpxServiceNextHopNode_Object = MibTableColumn
cjnIpxServiceNextHopNode = _CjnIpxServiceNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 8),
    _CjnIpxServiceNextHopNode_Type()
)
cjnIpxServiceNextHopNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxServiceNextHopNode.setStatus("current")
_CjnIpxServiceHops_Type = Integer32
_CjnIpxServiceHops_Object = MibTableColumn
cjnIpxServiceHops = _CjnIpxServiceHops_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 9),
    _CjnIpxServiceHops_Type()
)
cjnIpxServiceHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxServiceHops.setStatus("current")


class _CjnIpxServiceProtocol_Type(Integer32):
    """Custom type cjnIpxServiceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("static", 2))
    )


_CjnIpxServiceProtocol_Type.__name__ = "Integer32"
_CjnIpxServiceProtocol_Object = MibTableColumn
cjnIpxServiceProtocol = _CjnIpxServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 10),
    _CjnIpxServiceProtocol_Type()
)
cjnIpxServiceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxServiceProtocol.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPX-PRIVATE-MIB",
    **{"NetNumber": NetNumber,
       "NodeNumber": NodeNumber,
       "ServiceType": ServiceType,
       "ServiceName": ServiceName,
       "ServiceSocket": ServiceSocket,
       "cjnIpx": cjnIpx,
       "cjnIpxGlobalGroup": cjnIpxGlobalGroup,
       "cjnIpxEnabled": cjnIpxEnabled,
       "cjnIpxGlobalStatsGroup": cjnIpxGlobalStatsGroup,
       "cjnIpxInReceives": cjnIpxInReceives,
       "cjnIpxInDelivers": cjnIpxInDelivers,
       "cjnIpxForwarded": cjnIpxForwarded,
       "cjnIpxNetBIOSReceives": cjnIpxNetBIOSReceives,
       "cjnIpxInDiscards": cjnIpxInDiscards,
       "cjnIpxInHdrErrors": cjnIpxInHdrErrors,
       "cjnIpxInUnknownSockets": cjnIpxInUnknownSockets,
       "cjnIpxInTooManyHops": cjnIpxInTooManyHops,
       "cjnIpxInBadChecksums": cjnIpxInBadChecksums,
       "cjnIpxOutRequests": cjnIpxOutRequests,
       "cjnIpxOutPackets": cjnIpxOutPackets,
       "cjnIpxOutDiscards": cjnIpxOutDiscards,
       "cjnIpxOutNoRoutes": cjnIpxOutNoRoutes,
       "cjnIpxInPingRequests": cjnIpxInPingRequests,
       "cjnIpxInPingReplies": cjnIpxInPingReplies,
       "cjnIpxOutPingRequests": cjnIpxOutPingRequests,
       "cjnIpxOutPingReplies": cjnIpxOutPingReplies,
       "cjnIpxGlobalStatsReset": cjnIpxGlobalStatsReset,
       "cjnIpxRouteGroup": cjnIpxRouteGroup,
       "cjnIpxMaxRoutes": cjnIpxMaxRoutes,
       "cjnIpxDefaultRouteEnabled": cjnIpxDefaultRouteEnabled,
       "cjnIpxNumRoutes": cjnIpxNumRoutes,
       "cjnIpxPeakNumRoutes": cjnIpxPeakNumRoutes,
       "cjnIpxRouteAddFailures": cjnIpxRouteAddFailures,
       "cjnIpxStaticRouteGroup": cjnIpxStaticRouteGroup,
       "cjnIpxStaticRouteTable": cjnIpxStaticRouteTable,
       "cjnIpxStaticRouteEntry": cjnIpxStaticRouteEntry,
       "cjnIpxStaticRouteNet": cjnIpxStaticRouteNet,
       "cjnIpxStaticRouteRowStatus": cjnIpxStaticRouteRowStatus,
       "cjnIpxStaticRouteIfIndex": cjnIpxStaticRouteIfIndex,
       "cjnIpxStaticRouteNextHopNode": cjnIpxStaticRouteNextHopNode,
       "cjnIpxStaticRouteTicks": cjnIpxStaticRouteTicks,
       "cjnIpxStaticRouteHops": cjnIpxStaticRouteHops,
       "cjnIpxRouteTable": cjnIpxRouteTable,
       "cjnIpxRouteEntry": cjnIpxRouteEntry,
       "cjnIpxRouteNet": cjnIpxRouteNet,
       "cjnIpxRouteRowStatus": cjnIpxRouteRowStatus,
       "cjnIpxRouteIfIndex": cjnIpxRouteIfIndex,
       "cjnIpxRouteNextHopNode": cjnIpxRouteNextHopNode,
       "cjnIpxRouteTicks": cjnIpxRouteTicks,
       "cjnIpxRouteHops": cjnIpxRouteHops,
       "cjnIpxRouteProtocol": cjnIpxRouteProtocol,
       "cjnIpxServicesGroup": cjnIpxServicesGroup,
       "cjnIpxMaxServices": cjnIpxMaxServices,
       "cjnIpxNumServices": cjnIpxNumServices,
       "cjnIpxPeakNumServices": cjnIpxPeakNumServices,
       "cjnIpxServiceAddFailures": cjnIpxServiceAddFailures,
       "cjnIpxStaticServiceGroup": cjnIpxStaticServiceGroup,
       "cjnIpxStaticServiceTable": cjnIpxStaticServiceTable,
       "cjnIpxStaticServiceEntry": cjnIpxStaticServiceEntry,
       "cjnIpxStaticServiceType": cjnIpxStaticServiceType,
       "cjnIpxStaticServiceName": cjnIpxStaticServiceName,
       "cjnIpxStaticServiceRowStatus": cjnIpxStaticServiceRowStatus,
       "cjnIpxStaticServiceNet": cjnIpxStaticServiceNet,
       "cjnIpxStaticServiceNode": cjnIpxStaticServiceNode,
       "cjnIpxStaticServiceSocket": cjnIpxStaticServiceSocket,
       "cjnIpxStaticServiceIfIndex": cjnIpxStaticServiceIfIndex,
       "cjnIpxStaticServiceNextHopNode": cjnIpxStaticServiceNextHopNode,
       "cjnIpxStaticServiceHops": cjnIpxStaticServiceHops,
       "cjnIpxServiceTable": cjnIpxServiceTable,
       "cjnIpxServiceEntry": cjnIpxServiceEntry,
       "cjnIpxServiceType": cjnIpxServiceType,
       "cjnIpxServiceName": cjnIpxServiceName,
       "cjnIpxServiceRowStatus": cjnIpxServiceRowStatus,
       "cjnIpxServiceNet": cjnIpxServiceNet,
       "cjnIpxServiceNode": cjnIpxServiceNode,
       "cjnIpxServiceSocket": cjnIpxServiceSocket,
       "cjnIpxServiceIfIndex": cjnIpxServiceIfIndex,
       "cjnIpxServiceNextHopNode": cjnIpxServiceNextHopNode,
       "cjnIpxServiceHops": cjnIpxServiceHops,
       "cjnIpxServiceProtocol": cjnIpxServiceProtocol}
)
