# SNMP MIB module (CLNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CLNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:48 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class ClnpAddress(OctetString):
    """Custom type ClnpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 21),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Clns_ObjectIdentity = ObjectIdentity
clns = _Clns_ObjectIdentity(
    (1, 3, 6, 1, 3, 1)
)
_Clnp_ObjectIdentity = ObjectIdentity
clnp = _Clnp_ObjectIdentity(
    (1, 3, 6, 1, 3, 1, 1)
)


class _ClnpForwarding_Type(Integer32):
    """Custom type clnpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("es", 2),
          ("is", 1))
    )


_ClnpForwarding_Type.__name__ = "Integer32"
_ClnpForwarding_Object = MibScalar
clnpForwarding = _ClnpForwarding_Object(
    (1, 3, 6, 1, 3, 1, 1, 1),
    _ClnpForwarding_Type()
)
clnpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpForwarding.setStatus("mandatory")
_ClnpDefaultLifeTime_Type = Integer32
_ClnpDefaultLifeTime_Object = MibScalar
clnpDefaultLifeTime = _ClnpDefaultLifeTime_Object(
    (1, 3, 6, 1, 3, 1, 1, 2),
    _ClnpDefaultLifeTime_Type()
)
clnpDefaultLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpDefaultLifeTime.setStatus("mandatory")
_ClnpInReceives_Type = Counter32
_ClnpInReceives_Object = MibScalar
clnpInReceives = _ClnpInReceives_Object(
    (1, 3, 6, 1, 3, 1, 1, 3),
    _ClnpInReceives_Type()
)
clnpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInReceives.setStatus("mandatory")
_ClnpInHdrErrors_Type = Counter32
_ClnpInHdrErrors_Object = MibScalar
clnpInHdrErrors = _ClnpInHdrErrors_Object(
    (1, 3, 6, 1, 3, 1, 1, 4),
    _ClnpInHdrErrors_Type()
)
clnpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInHdrErrors.setStatus("mandatory")
_ClnpInAddrErrors_Type = Counter32
_ClnpInAddrErrors_Object = MibScalar
clnpInAddrErrors = _ClnpInAddrErrors_Object(
    (1, 3, 6, 1, 3, 1, 1, 5),
    _ClnpInAddrErrors_Type()
)
clnpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInAddrErrors.setStatus("mandatory")
_ClnpForwPDUs_Type = Counter32
_ClnpForwPDUs_Object = MibScalar
clnpForwPDUs = _ClnpForwPDUs_Object(
    (1, 3, 6, 1, 3, 1, 1, 6),
    _ClnpForwPDUs_Type()
)
clnpForwPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpForwPDUs.setStatus("mandatory")
_ClnpInUnknownNLPs_Type = Counter32
_ClnpInUnknownNLPs_Object = MibScalar
clnpInUnknownNLPs = _ClnpInUnknownNLPs_Object(
    (1, 3, 6, 1, 3, 1, 1, 7),
    _ClnpInUnknownNLPs_Type()
)
clnpInUnknownNLPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInUnknownNLPs.setStatus("mandatory")
_ClnpInUnknownULPs_Type = Counter32
_ClnpInUnknownULPs_Object = MibScalar
clnpInUnknownULPs = _ClnpInUnknownULPs_Object(
    (1, 3, 6, 1, 3, 1, 1, 8),
    _ClnpInUnknownULPs_Type()
)
clnpInUnknownULPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInUnknownULPs.setStatus("mandatory")
_ClnpInDiscards_Type = Counter32
_ClnpInDiscards_Object = MibScalar
clnpInDiscards = _ClnpInDiscards_Object(
    (1, 3, 6, 1, 3, 1, 1, 9),
    _ClnpInDiscards_Type()
)
clnpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInDiscards.setStatus("mandatory")
_ClnpInDelivers_Type = Counter32
_ClnpInDelivers_Object = MibScalar
clnpInDelivers = _ClnpInDelivers_Object(
    (1, 3, 6, 1, 3, 1, 1, 10),
    _ClnpInDelivers_Type()
)
clnpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInDelivers.setStatus("mandatory")
_ClnpOutRequests_Type = Counter32
_ClnpOutRequests_Object = MibScalar
clnpOutRequests = _ClnpOutRequests_Object(
    (1, 3, 6, 1, 3, 1, 1, 11),
    _ClnpOutRequests_Type()
)
clnpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutRequests.setStatus("mandatory")
_ClnpOutDiscards_Type = Counter32
_ClnpOutDiscards_Object = MibScalar
clnpOutDiscards = _ClnpOutDiscards_Object(
    (1, 3, 6, 1, 3, 1, 1, 12),
    _ClnpOutDiscards_Type()
)
clnpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutDiscards.setStatus("mandatory")
_ClnpOutNoRoutes_Type = Counter32
_ClnpOutNoRoutes_Object = MibScalar
clnpOutNoRoutes = _ClnpOutNoRoutes_Object(
    (1, 3, 6, 1, 3, 1, 1, 13),
    _ClnpOutNoRoutes_Type()
)
clnpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutNoRoutes.setStatus("mandatory")
_ClnpReasmTimeout_Type = Integer32
_ClnpReasmTimeout_Object = MibScalar
clnpReasmTimeout = _ClnpReasmTimeout_Object(
    (1, 3, 6, 1, 3, 1, 1, 14),
    _ClnpReasmTimeout_Type()
)
clnpReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpReasmTimeout.setStatus("mandatory")
_ClnpReasmReqds_Type = Counter32
_ClnpReasmReqds_Object = MibScalar
clnpReasmReqds = _ClnpReasmReqds_Object(
    (1, 3, 6, 1, 3, 1, 1, 15),
    _ClnpReasmReqds_Type()
)
clnpReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpReasmReqds.setStatus("mandatory")
_ClnpReasmOKs_Type = Counter32
_ClnpReasmOKs_Object = MibScalar
clnpReasmOKs = _ClnpReasmOKs_Object(
    (1, 3, 6, 1, 3, 1, 1, 16),
    _ClnpReasmOKs_Type()
)
clnpReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpReasmOKs.setStatus("mandatory")
_ClnpReasmFails_Type = Counter32
_ClnpReasmFails_Object = MibScalar
clnpReasmFails = _ClnpReasmFails_Object(
    (1, 3, 6, 1, 3, 1, 1, 17),
    _ClnpReasmFails_Type()
)
clnpReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpReasmFails.setStatus("mandatory")
_ClnpSegOKs_Type = Counter32
_ClnpSegOKs_Object = MibScalar
clnpSegOKs = _ClnpSegOKs_Object(
    (1, 3, 6, 1, 3, 1, 1, 18),
    _ClnpSegOKs_Type()
)
clnpSegOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpSegOKs.setStatus("mandatory")
_ClnpSegFails_Type = Counter32
_ClnpSegFails_Object = MibScalar
clnpSegFails = _ClnpSegFails_Object(
    (1, 3, 6, 1, 3, 1, 1, 19),
    _ClnpSegFails_Type()
)
clnpSegFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpSegFails.setStatus("mandatory")
_ClnpSegCreates_Type = Counter32
_ClnpSegCreates_Object = MibScalar
clnpSegCreates = _ClnpSegCreates_Object(
    (1, 3, 6, 1, 3, 1, 1, 20),
    _ClnpSegCreates_Type()
)
clnpSegCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpSegCreates.setStatus("mandatory")
_ClnpAddrTable_Object = MibTable
clnpAddrTable = _ClnpAddrTable_Object(
    (1, 3, 6, 1, 3, 1, 1, 21)
)
if mibBuilder.loadTexts:
    clnpAddrTable.setStatus("mandatory")
_ClnpAddrEntry_Object = MibTableRow
clnpAddrEntry = _ClnpAddrEntry_Object(
    (1, 3, 6, 1, 3, 1, 1, 21, 1)
)
clnpAddrEntry.setIndexNames(
    (0, "CLNS-MIB", "clnpAdEntAddr"),
)
if mibBuilder.loadTexts:
    clnpAddrEntry.setStatus("mandatory")
_ClnpAdEntAddr_Type = ClnpAddress
_ClnpAdEntAddr_Object = MibTableColumn
clnpAdEntAddr = _ClnpAdEntAddr_Object(
    (1, 3, 6, 1, 3, 1, 1, 21, 1, 1),
    _ClnpAdEntAddr_Type()
)
clnpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpAdEntAddr.setStatus("mandatory")
_ClnpAdEntIfIndex_Type = Integer32
_ClnpAdEntIfIndex_Object = MibTableColumn
clnpAdEntIfIndex = _ClnpAdEntIfIndex_Object(
    (1, 3, 6, 1, 3, 1, 1, 21, 1, 2),
    _ClnpAdEntIfIndex_Type()
)
clnpAdEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpAdEntIfIndex.setStatus("mandatory")


class _ClnpAdEntReasmMaxSize_Type(Integer32):
    """Custom type clnpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClnpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_ClnpAdEntReasmMaxSize_Object = MibTableColumn
clnpAdEntReasmMaxSize = _ClnpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 3, 1, 1, 21, 1, 3),
    _ClnpAdEntReasmMaxSize_Type()
)
clnpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpAdEntReasmMaxSize.setStatus("mandatory")
_ClnpRoutingTable_Object = MibTable
clnpRoutingTable = _ClnpRoutingTable_Object(
    (1, 3, 6, 1, 3, 1, 1, 22)
)
if mibBuilder.loadTexts:
    clnpRoutingTable.setStatus("mandatory")
_ClnpRouteEntry_Object = MibTableRow
clnpRouteEntry = _ClnpRouteEntry_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1)
)
clnpRouteEntry.setIndexNames(
    (0, "CLNS-MIB", "clnpRouteDest"),
)
if mibBuilder.loadTexts:
    clnpRouteEntry.setStatus("mandatory")
_ClnpRouteDest_Type = ClnpAddress
_ClnpRouteDest_Object = MibTableColumn
clnpRouteDest = _ClnpRouteDest_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 1),
    _ClnpRouteDest_Type()
)
clnpRouteDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpRouteDest.setStatus("mandatory")
_ClnpRouteIfIndex_Type = Integer32
_ClnpRouteIfIndex_Object = MibTableColumn
clnpRouteIfIndex = _ClnpRouteIfIndex_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 2),
    _ClnpRouteIfIndex_Type()
)
clnpRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpRouteIfIndex.setStatus("mandatory")
_ClnpRouteMetric1_Type = Integer32
_ClnpRouteMetric1_Object = MibTableColumn
clnpRouteMetric1 = _ClnpRouteMetric1_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 3),
    _ClnpRouteMetric1_Type()
)
clnpRouteMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpRouteMetric1.setStatus("mandatory")
_ClnpRouteMetric2_Type = Integer32
_ClnpRouteMetric2_Object = MibTableColumn
clnpRouteMetric2 = _ClnpRouteMetric2_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 4),
    _ClnpRouteMetric2_Type()
)
clnpRouteMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpRouteMetric2.setStatus("mandatory")
_ClnpRouteMetric3_Type = Integer32
_ClnpRouteMetric3_Object = MibTableColumn
clnpRouteMetric3 = _ClnpRouteMetric3_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 5),
    _ClnpRouteMetric3_Type()
)
clnpRouteMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpRouteMetric3.setStatus("mandatory")
_ClnpRouteMetric4_Type = Integer32
_ClnpRouteMetric4_Object = MibTableColumn
clnpRouteMetric4 = _ClnpRouteMetric4_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 6),
    _ClnpRouteMetric4_Type()
)
clnpRouteMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpRouteMetric4.setStatus("mandatory")
_ClnpRouteNextHop_Type = ClnpAddress
_ClnpRouteNextHop_Object = MibTableColumn
clnpRouteNextHop = _ClnpRouteNextHop_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 7),
    _ClnpRouteNextHop_Type()
)
clnpRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpRouteNextHop.setStatus("mandatory")


class _ClnpRouteType_Type(Integer32):
    """Custom type clnpRouteType based on Integer32"""
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
        *(("direct", 3),
          ("invalid", 2),
          ("other", 1),
          ("remote", 4))
    )


_ClnpRouteType_Type.__name__ = "Integer32"
_ClnpRouteType_Object = MibTableColumn
clnpRouteType = _ClnpRouteType_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 8),
    _ClnpRouteType_Type()
)
clnpRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpRouteType.setStatus("mandatory")


class _ClnpRouteProto_Type(Integer32):
    """Custom type clnpRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("is-is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1))
    )


_ClnpRouteProto_Type.__name__ = "Integer32"
_ClnpRouteProto_Object = MibTableColumn
clnpRouteProto = _ClnpRouteProto_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 9),
    _ClnpRouteProto_Type()
)
clnpRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpRouteProto.setStatus("mandatory")
_ClnpRouteAge_Type = Integer32
_ClnpRouteAge_Object = MibTableColumn
clnpRouteAge = _ClnpRouteAge_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 10),
    _ClnpRouteAge_Type()
)
clnpRouteAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpRouteAge.setStatus("mandatory")
_ClnpRouteMetric5_Type = Integer32
_ClnpRouteMetric5_Object = MibTableColumn
clnpRouteMetric5 = _ClnpRouteMetric5_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 11),
    _ClnpRouteMetric5_Type()
)
clnpRouteMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpRouteMetric5.setStatus("mandatory")
_ClnpRouteInfo_Type = ObjectIdentifier
_ClnpRouteInfo_Object = MibTableColumn
clnpRouteInfo = _ClnpRouteInfo_Object(
    (1, 3, 6, 1, 3, 1, 1, 22, 1, 12),
    _ClnpRouteInfo_Type()
)
clnpRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpRouteInfo.setStatus("mandatory")
_ClnpNetToMediaTable_Object = MibTable
clnpNetToMediaTable = _ClnpNetToMediaTable_Object(
    (1, 3, 6, 1, 3, 1, 1, 23)
)
if mibBuilder.loadTexts:
    clnpNetToMediaTable.setStatus("mandatory")
_ClnpNetToMediaEntry_Object = MibTableRow
clnpNetToMediaEntry = _ClnpNetToMediaEntry_Object(
    (1, 3, 6, 1, 3, 1, 1, 23, 1)
)
clnpNetToMediaEntry.setIndexNames(
    (0, "CLNS-MIB", "clnpNetToMediaIfIndex"),
    (0, "CLNS-MIB", "clnpNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    clnpNetToMediaEntry.setStatus("mandatory")
_ClnpNetToMediaIfIndex_Type = Integer32
_ClnpNetToMediaIfIndex_Object = MibTableColumn
clnpNetToMediaIfIndex = _ClnpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 3, 1, 1, 23, 1, 1),
    _ClnpNetToMediaIfIndex_Type()
)
clnpNetToMediaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpNetToMediaIfIndex.setStatus("mandatory")
_ClnpNetToMediaPhysAddress_Type = PhysAddress
_ClnpNetToMediaPhysAddress_Object = MibTableColumn
clnpNetToMediaPhysAddress = _ClnpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 3, 1, 1, 23, 1, 2),
    _ClnpNetToMediaPhysAddress_Type()
)
clnpNetToMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpNetToMediaPhysAddress.setStatus("mandatory")
_ClnpNetToMediaNetAddress_Type = ClnpAddress
_ClnpNetToMediaNetAddress_Object = MibTableColumn
clnpNetToMediaNetAddress = _ClnpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 3, 1, 1, 23, 1, 3),
    _ClnpNetToMediaNetAddress_Type()
)
clnpNetToMediaNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpNetToMediaNetAddress.setStatus("mandatory")


class _ClnpNetToMediaType_Type(Integer32):
    """Custom type clnpNetToMediaType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_ClnpNetToMediaType_Type.__name__ = "Integer32"
_ClnpNetToMediaType_Object = MibTableColumn
clnpNetToMediaType = _ClnpNetToMediaType_Object(
    (1, 3, 6, 1, 3, 1, 1, 23, 1, 4),
    _ClnpNetToMediaType_Type()
)
clnpNetToMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpNetToMediaType.setStatus("mandatory")
_ClnpNetToMediaAge_Type = Integer32
_ClnpNetToMediaAge_Object = MibTableColumn
clnpNetToMediaAge = _ClnpNetToMediaAge_Object(
    (1, 3, 6, 1, 3, 1, 1, 23, 1, 5),
    _ClnpNetToMediaAge_Type()
)
clnpNetToMediaAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpNetToMediaAge.setStatus("mandatory")
_ClnpNetToMediaHoldTime_Type = Integer32
_ClnpNetToMediaHoldTime_Object = MibTableColumn
clnpNetToMediaHoldTime = _ClnpNetToMediaHoldTime_Object(
    (1, 3, 6, 1, 3, 1, 1, 23, 1, 6),
    _ClnpNetToMediaHoldTime_Type()
)
clnpNetToMediaHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpNetToMediaHoldTime.setStatus("mandatory")
_ClnpMediaToNetTable_Object = MibTable
clnpMediaToNetTable = _ClnpMediaToNetTable_Object(
    (1, 3, 6, 1, 3, 1, 1, 24)
)
if mibBuilder.loadTexts:
    clnpMediaToNetTable.setStatus("mandatory")
_ClnpMediaToNetEntry_Object = MibTableRow
clnpMediaToNetEntry = _ClnpMediaToNetEntry_Object(
    (1, 3, 6, 1, 3, 1, 1, 24, 1)
)
clnpMediaToNetEntry.setIndexNames(
    (0, "CLNS-MIB", "clnpMediaToNetIfIndex"),
    (0, "CLNS-MIB", "clnpMediaToNetPhysAddress"),
)
if mibBuilder.loadTexts:
    clnpMediaToNetEntry.setStatus("mandatory")
_ClnpMediaToNetIfIndex_Type = Integer32
_ClnpMediaToNetIfIndex_Object = MibTableColumn
clnpMediaToNetIfIndex = _ClnpMediaToNetIfIndex_Object(
    (1, 3, 6, 1, 3, 1, 1, 24, 1, 1),
    _ClnpMediaToNetIfIndex_Type()
)
clnpMediaToNetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpMediaToNetIfIndex.setStatus("mandatory")
_ClnpMediaToNetAddress_Type = ClnpAddress
_ClnpMediaToNetAddress_Object = MibScalar
clnpMediaToNetAddress = _ClnpMediaToNetAddress_Object(
    (1, 3, 6, 1, 3, 1, 1, 24, 1, 2),
    _ClnpMediaToNetAddress_Type()
)
clnpMediaToNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpMediaToNetAddress.setStatus("mandatory")
_ClnpMediaToNetPhysAddress_Type = PhysAddress
_ClnpMediaToNetPhysAddress_Object = MibTableColumn
clnpMediaToNetPhysAddress = _ClnpMediaToNetPhysAddress_Object(
    (1, 3, 6, 1, 3, 1, 1, 24, 1, 3),
    _ClnpMediaToNetPhysAddress_Type()
)
clnpMediaToNetPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpMediaToNetPhysAddress.setStatus("mandatory")


class _ClnpMediaToNetType_Type(Integer32):
    """Custom type clnpMediaToNetType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_ClnpMediaToNetType_Type.__name__ = "Integer32"
_ClnpMediaToNetType_Object = MibTableColumn
clnpMediaToNetType = _ClnpMediaToNetType_Object(
    (1, 3, 6, 1, 3, 1, 1, 24, 1, 4),
    _ClnpMediaToNetType_Type()
)
clnpMediaToNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpMediaToNetType.setStatus("mandatory")
_ClnpMediaToNetAge_Type = Integer32
_ClnpMediaToNetAge_Object = MibTableColumn
clnpMediaToNetAge = _ClnpMediaToNetAge_Object(
    (1, 3, 6, 1, 3, 1, 1, 24, 1, 5),
    _ClnpMediaToNetAge_Type()
)
clnpMediaToNetAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpMediaToNetAge.setStatus("mandatory")
_ClnpMediaToNetHoldTime_Type = Integer32
_ClnpMediaToNetHoldTime_Object = MibTableColumn
clnpMediaToNetHoldTime = _ClnpMediaToNetHoldTime_Object(
    (1, 3, 6, 1, 3, 1, 1, 24, 1, 6),
    _ClnpMediaToNetHoldTime_Type()
)
clnpMediaToNetHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clnpMediaToNetHoldTime.setStatus("mandatory")
_ClnpInOpts_Type = Counter32
_ClnpInOpts_Object = MibScalar
clnpInOpts = _ClnpInOpts_Object(
    (1, 3, 6, 1, 3, 1, 1, 25),
    _ClnpInOpts_Type()
)
clnpInOpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInOpts.setStatus("mandatory")
_ClnpOutOpts_Type = Counter32
_ClnpOutOpts_Object = MibScalar
clnpOutOpts = _ClnpOutOpts_Object(
    (1, 3, 6, 1, 3, 1, 1, 26),
    _ClnpOutOpts_Type()
)
clnpOutOpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutOpts.setStatus("mandatory")
_ClnpRoutingDiscards_Type = Counter32
_ClnpRoutingDiscards_Object = MibScalar
clnpRoutingDiscards = _ClnpRoutingDiscards_Object(
    (1, 3, 6, 1, 3, 1, 1, 27),
    _ClnpRoutingDiscards_Type()
)
clnpRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpRoutingDiscards.setStatus("mandatory")
_Error_ObjectIdentity = ObjectIdentity
error = _Error_ObjectIdentity(
    (1, 3, 6, 1, 3, 1, 2)
)
_ClnpInErrors_Type = Counter32
_ClnpInErrors_Object = MibScalar
clnpInErrors = _ClnpInErrors_Object(
    (1, 3, 6, 1, 3, 1, 2, 1),
    _ClnpInErrors_Type()
)
clnpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrors.setStatus("mandatory")
_ClnpOutErrors_Type = Counter32
_ClnpOutErrors_Object = MibScalar
clnpOutErrors = _ClnpOutErrors_Object(
    (1, 3, 6, 1, 3, 1, 2, 2),
    _ClnpOutErrors_Type()
)
clnpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrors.setStatus("mandatory")
_ClnpInErrUnspecs_Type = Counter32
_ClnpInErrUnspecs_Object = MibScalar
clnpInErrUnspecs = _ClnpInErrUnspecs_Object(
    (1, 3, 6, 1, 3, 1, 2, 3),
    _ClnpInErrUnspecs_Type()
)
clnpInErrUnspecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrUnspecs.setStatus("mandatory")
_ClnpInErrProcs_Type = Counter32
_ClnpInErrProcs_Object = MibScalar
clnpInErrProcs = _ClnpInErrProcs_Object(
    (1, 3, 6, 1, 3, 1, 2, 4),
    _ClnpInErrProcs_Type()
)
clnpInErrProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrProcs.setStatus("mandatory")
_ClnpInErrCksums_Type = Counter32
_ClnpInErrCksums_Object = MibScalar
clnpInErrCksums = _ClnpInErrCksums_Object(
    (1, 3, 6, 1, 3, 1, 2, 5),
    _ClnpInErrCksums_Type()
)
clnpInErrCksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrCksums.setStatus("mandatory")
_ClnpInErrCongests_Type = Counter32
_ClnpInErrCongests_Object = MibScalar
clnpInErrCongests = _ClnpInErrCongests_Object(
    (1, 3, 6, 1, 3, 1, 2, 6),
    _ClnpInErrCongests_Type()
)
clnpInErrCongests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrCongests.setStatus("mandatory")
_ClnpInErrHdrs_Type = Counter32
_ClnpInErrHdrs_Object = MibScalar
clnpInErrHdrs = _ClnpInErrHdrs_Object(
    (1, 3, 6, 1, 3, 1, 2, 7),
    _ClnpInErrHdrs_Type()
)
clnpInErrHdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrHdrs.setStatus("mandatory")
_ClnpInErrSegs_Type = Counter32
_ClnpInErrSegs_Object = MibScalar
clnpInErrSegs = _ClnpInErrSegs_Object(
    (1, 3, 6, 1, 3, 1, 2, 8),
    _ClnpInErrSegs_Type()
)
clnpInErrSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrSegs.setStatus("mandatory")
_ClnpInErrIncomps_Type = Counter32
_ClnpInErrIncomps_Object = MibScalar
clnpInErrIncomps = _ClnpInErrIncomps_Object(
    (1, 3, 6, 1, 3, 1, 2, 9),
    _ClnpInErrIncomps_Type()
)
clnpInErrIncomps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrIncomps.setStatus("mandatory")
_ClnpInErrDups_Type = Counter32
_ClnpInErrDups_Object = MibScalar
clnpInErrDups = _ClnpInErrDups_Object(
    (1, 3, 6, 1, 3, 1, 2, 10),
    _ClnpInErrDups_Type()
)
clnpInErrDups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrDups.setStatus("mandatory")
_ClnpInErrUnreachDsts_Type = Counter32
_ClnpInErrUnreachDsts_Object = MibScalar
clnpInErrUnreachDsts = _ClnpInErrUnreachDsts_Object(
    (1, 3, 6, 1, 3, 1, 2, 11),
    _ClnpInErrUnreachDsts_Type()
)
clnpInErrUnreachDsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrUnreachDsts.setStatus("mandatory")
_ClnpInErrUnknownDsts_Type = Counter32
_ClnpInErrUnknownDsts_Object = MibScalar
clnpInErrUnknownDsts = _ClnpInErrUnknownDsts_Object(
    (1, 3, 6, 1, 3, 1, 2, 12),
    _ClnpInErrUnknownDsts_Type()
)
clnpInErrUnknownDsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrUnknownDsts.setStatus("mandatory")
_ClnpInErrSRUnspecs_Type = Counter32
_ClnpInErrSRUnspecs_Object = MibScalar
clnpInErrSRUnspecs = _ClnpInErrSRUnspecs_Object(
    (1, 3, 6, 1, 3, 1, 2, 13),
    _ClnpInErrSRUnspecs_Type()
)
clnpInErrSRUnspecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrSRUnspecs.setStatus("mandatory")
_ClnpInErrSRSyntaxes_Type = Counter32
_ClnpInErrSRSyntaxes_Object = MibScalar
clnpInErrSRSyntaxes = _ClnpInErrSRSyntaxes_Object(
    (1, 3, 6, 1, 3, 1, 2, 14),
    _ClnpInErrSRSyntaxes_Type()
)
clnpInErrSRSyntaxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrSRSyntaxes.setStatus("mandatory")
_ClnpInErrSRUnkAddrs_Type = Counter32
_ClnpInErrSRUnkAddrs_Object = MibScalar
clnpInErrSRUnkAddrs = _ClnpInErrSRUnkAddrs_Object(
    (1, 3, 6, 1, 3, 1, 2, 15),
    _ClnpInErrSRUnkAddrs_Type()
)
clnpInErrSRUnkAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrSRUnkAddrs.setStatus("mandatory")
_ClnpInErrSRBadPaths_Type = Counter32
_ClnpInErrSRBadPaths_Object = MibScalar
clnpInErrSRBadPaths = _ClnpInErrSRBadPaths_Object(
    (1, 3, 6, 1, 3, 1, 2, 16),
    _ClnpInErrSRBadPaths_Type()
)
clnpInErrSRBadPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrSRBadPaths.setStatus("mandatory")
_ClnpInErrHops_Type = Counter32
_ClnpInErrHops_Object = MibScalar
clnpInErrHops = _ClnpInErrHops_Object(
    (1, 3, 6, 1, 3, 1, 2, 17),
    _ClnpInErrHops_Type()
)
clnpInErrHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrHops.setStatus("mandatory")
_ClnpInErrHopReassms_Type = Counter32
_ClnpInErrHopReassms_Object = MibScalar
clnpInErrHopReassms = _ClnpInErrHopReassms_Object(
    (1, 3, 6, 1, 3, 1, 2, 18),
    _ClnpInErrHopReassms_Type()
)
clnpInErrHopReassms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrHopReassms.setStatus("mandatory")
_ClnpInErrUnsOptions_Type = Counter32
_ClnpInErrUnsOptions_Object = MibScalar
clnpInErrUnsOptions = _ClnpInErrUnsOptions_Object(
    (1, 3, 6, 1, 3, 1, 2, 19),
    _ClnpInErrUnsOptions_Type()
)
clnpInErrUnsOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrUnsOptions.setStatus("mandatory")
_ClnpInErrUnsVersions_Type = Counter32
_ClnpInErrUnsVersions_Object = MibScalar
clnpInErrUnsVersions = _ClnpInErrUnsVersions_Object(
    (1, 3, 6, 1, 3, 1, 2, 20),
    _ClnpInErrUnsVersions_Type()
)
clnpInErrUnsVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrUnsVersions.setStatus("mandatory")
_ClnpInErrUnsSecurities_Type = Counter32
_ClnpInErrUnsSecurities_Object = MibScalar
clnpInErrUnsSecurities = _ClnpInErrUnsSecurities_Object(
    (1, 3, 6, 1, 3, 1, 2, 21),
    _ClnpInErrUnsSecurities_Type()
)
clnpInErrUnsSecurities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrUnsSecurities.setStatus("mandatory")
_ClnpInErrUnsSRs_Type = Counter32
_ClnpInErrUnsSRs_Object = MibScalar
clnpInErrUnsSRs = _ClnpInErrUnsSRs_Object(
    (1, 3, 6, 1, 3, 1, 2, 22),
    _ClnpInErrUnsSRs_Type()
)
clnpInErrUnsSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrUnsSRs.setStatus("mandatory")
_ClnpInErrUnsRRs_Type = Counter32
_ClnpInErrUnsRRs_Object = MibScalar
clnpInErrUnsRRs = _ClnpInErrUnsRRs_Object(
    (1, 3, 6, 1, 3, 1, 2, 23),
    _ClnpInErrUnsRRs_Type()
)
clnpInErrUnsRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrUnsRRs.setStatus("mandatory")
_ClnpInErrInterferences_Type = Counter32
_ClnpInErrInterferences_Object = MibScalar
clnpInErrInterferences = _ClnpInErrInterferences_Object(
    (1, 3, 6, 1, 3, 1, 2, 24),
    _ClnpInErrInterferences_Type()
)
clnpInErrInterferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpInErrInterferences.setStatus("mandatory")
_ClnpOutErrUnspecs_Type = Counter32
_ClnpOutErrUnspecs_Object = MibScalar
clnpOutErrUnspecs = _ClnpOutErrUnspecs_Object(
    (1, 3, 6, 1, 3, 1, 2, 25),
    _ClnpOutErrUnspecs_Type()
)
clnpOutErrUnspecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrUnspecs.setStatus("mandatory")
_ClnpOutErrProcs_Type = Counter32
_ClnpOutErrProcs_Object = MibScalar
clnpOutErrProcs = _ClnpOutErrProcs_Object(
    (1, 3, 6, 1, 3, 1, 2, 26),
    _ClnpOutErrProcs_Type()
)
clnpOutErrProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrProcs.setStatus("mandatory")
_ClnpOutErrCksums_Type = Counter32
_ClnpOutErrCksums_Object = MibScalar
clnpOutErrCksums = _ClnpOutErrCksums_Object(
    (1, 3, 6, 1, 3, 1, 2, 27),
    _ClnpOutErrCksums_Type()
)
clnpOutErrCksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrCksums.setStatus("mandatory")
_ClnpOutErrCongests_Type = Counter32
_ClnpOutErrCongests_Object = MibScalar
clnpOutErrCongests = _ClnpOutErrCongests_Object(
    (1, 3, 6, 1, 3, 1, 2, 28),
    _ClnpOutErrCongests_Type()
)
clnpOutErrCongests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrCongests.setStatus("mandatory")
_ClnpOutErrHdrs_Type = Counter32
_ClnpOutErrHdrs_Object = MibScalar
clnpOutErrHdrs = _ClnpOutErrHdrs_Object(
    (1, 3, 6, 1, 3, 1, 2, 29),
    _ClnpOutErrHdrs_Type()
)
clnpOutErrHdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrHdrs.setStatus("mandatory")
_ClnpOutErrSegs_Type = Counter32
_ClnpOutErrSegs_Object = MibScalar
clnpOutErrSegs = _ClnpOutErrSegs_Object(
    (1, 3, 6, 1, 3, 1, 2, 30),
    _ClnpOutErrSegs_Type()
)
clnpOutErrSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrSegs.setStatus("mandatory")
_ClnpOutErrIncomps_Type = Counter32
_ClnpOutErrIncomps_Object = MibScalar
clnpOutErrIncomps = _ClnpOutErrIncomps_Object(
    (1, 3, 6, 1, 3, 1, 2, 31),
    _ClnpOutErrIncomps_Type()
)
clnpOutErrIncomps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrIncomps.setStatus("mandatory")
_ClnpOutErrDups_Type = Counter32
_ClnpOutErrDups_Object = MibScalar
clnpOutErrDups = _ClnpOutErrDups_Object(
    (1, 3, 6, 1, 3, 1, 2, 32),
    _ClnpOutErrDups_Type()
)
clnpOutErrDups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrDups.setStatus("mandatory")
_ClnpOutErrUnreachDsts_Type = Counter32
_ClnpOutErrUnreachDsts_Object = MibScalar
clnpOutErrUnreachDsts = _ClnpOutErrUnreachDsts_Object(
    (1, 3, 6, 1, 3, 1, 2, 33),
    _ClnpOutErrUnreachDsts_Type()
)
clnpOutErrUnreachDsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrUnreachDsts.setStatus("mandatory")
_ClnpOutErrUnknownDsts_Type = Counter32
_ClnpOutErrUnknownDsts_Object = MibScalar
clnpOutErrUnknownDsts = _ClnpOutErrUnknownDsts_Object(
    (1, 3, 6, 1, 3, 1, 2, 34),
    _ClnpOutErrUnknownDsts_Type()
)
clnpOutErrUnknownDsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrUnknownDsts.setStatus("mandatory")
_ClnpOutErrSRUnspecs_Type = Counter32
_ClnpOutErrSRUnspecs_Object = MibScalar
clnpOutErrSRUnspecs = _ClnpOutErrSRUnspecs_Object(
    (1, 3, 6, 1, 3, 1, 2, 35),
    _ClnpOutErrSRUnspecs_Type()
)
clnpOutErrSRUnspecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrSRUnspecs.setStatus("mandatory")
_ClnpOutErrSRSyntaxes_Type = Counter32
_ClnpOutErrSRSyntaxes_Object = MibScalar
clnpOutErrSRSyntaxes = _ClnpOutErrSRSyntaxes_Object(
    (1, 3, 6, 1, 3, 1, 2, 36),
    _ClnpOutErrSRSyntaxes_Type()
)
clnpOutErrSRSyntaxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrSRSyntaxes.setStatus("mandatory")
_ClnpOutErrSRUnkAddrs_Type = Counter32
_ClnpOutErrSRUnkAddrs_Object = MibScalar
clnpOutErrSRUnkAddrs = _ClnpOutErrSRUnkAddrs_Object(
    (1, 3, 6, 1, 3, 1, 2, 37),
    _ClnpOutErrSRUnkAddrs_Type()
)
clnpOutErrSRUnkAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrSRUnkAddrs.setStatus("mandatory")
_ClnpOutErrSRBadPaths_Type = Counter32
_ClnpOutErrSRBadPaths_Object = MibScalar
clnpOutErrSRBadPaths = _ClnpOutErrSRBadPaths_Object(
    (1, 3, 6, 1, 3, 1, 2, 38),
    _ClnpOutErrSRBadPaths_Type()
)
clnpOutErrSRBadPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrSRBadPaths.setStatus("mandatory")
_ClnpOutErrHops_Type = Counter32
_ClnpOutErrHops_Object = MibScalar
clnpOutErrHops = _ClnpOutErrHops_Object(
    (1, 3, 6, 1, 3, 1, 2, 39),
    _ClnpOutErrHops_Type()
)
clnpOutErrHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrHops.setStatus("mandatory")
_ClnpOutErrHopReassms_Type = Counter32
_ClnpOutErrHopReassms_Object = MibScalar
clnpOutErrHopReassms = _ClnpOutErrHopReassms_Object(
    (1, 3, 6, 1, 3, 1, 2, 40),
    _ClnpOutErrHopReassms_Type()
)
clnpOutErrHopReassms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrHopReassms.setStatus("mandatory")
_ClnpOutErrUnsOptions_Type = Counter32
_ClnpOutErrUnsOptions_Object = MibScalar
clnpOutErrUnsOptions = _ClnpOutErrUnsOptions_Object(
    (1, 3, 6, 1, 3, 1, 2, 41),
    _ClnpOutErrUnsOptions_Type()
)
clnpOutErrUnsOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrUnsOptions.setStatus("mandatory")
_ClnpOutErrUnsVersions_Type = Counter32
_ClnpOutErrUnsVersions_Object = MibScalar
clnpOutErrUnsVersions = _ClnpOutErrUnsVersions_Object(
    (1, 3, 6, 1, 3, 1, 2, 42),
    _ClnpOutErrUnsVersions_Type()
)
clnpOutErrUnsVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrUnsVersions.setStatus("mandatory")
_ClnpOutErrUnsSecurities_Type = Counter32
_ClnpOutErrUnsSecurities_Object = MibScalar
clnpOutErrUnsSecurities = _ClnpOutErrUnsSecurities_Object(
    (1, 3, 6, 1, 3, 1, 2, 43),
    _ClnpOutErrUnsSecurities_Type()
)
clnpOutErrUnsSecurities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrUnsSecurities.setStatus("mandatory")
_ClnpOutErrUnsSRs_Type = Counter32
_ClnpOutErrUnsSRs_Object = MibScalar
clnpOutErrUnsSRs = _ClnpOutErrUnsSRs_Object(
    (1, 3, 6, 1, 3, 1, 2, 44),
    _ClnpOutErrUnsSRs_Type()
)
clnpOutErrUnsSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrUnsSRs.setStatus("mandatory")
_ClnpOutErrUnsRRs_Type = Counter32
_ClnpOutErrUnsRRs_Object = MibScalar
clnpOutErrUnsRRs = _ClnpOutErrUnsRRs_Object(
    (1, 3, 6, 1, 3, 1, 2, 45),
    _ClnpOutErrUnsRRs_Type()
)
clnpOutErrUnsRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrUnsRRs.setStatus("mandatory")
_ClnpOutErrInterferences_Type = Counter32
_ClnpOutErrInterferences_Object = MibScalar
clnpOutErrInterferences = _ClnpOutErrInterferences_Object(
    (1, 3, 6, 1, 3, 1, 2, 46),
    _ClnpOutErrInterferences_Type()
)
clnpOutErrInterferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clnpOutErrInterferences.setStatus("mandatory")
_Echo_ObjectIdentity = ObjectIdentity
echo = _Echo_ObjectIdentity(
    (1, 3, 6, 1, 3, 1, 3)
)
_Es_is_ObjectIdentity = ObjectIdentity
es_is = _Es_is_ObjectIdentity(
    (1, 3, 6, 1, 3, 1, 4)
)
_EsisESHins_Type = Counter32
_EsisESHins_Object = MibScalar
esisESHins = _EsisESHins_Object(
    (1, 3, 6, 1, 3, 1, 4, 1),
    _EsisESHins_Type()
)
esisESHins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esisESHins.setStatus("mandatory")
_EsisESHouts_Type = Counter32
_EsisESHouts_Object = MibScalar
esisESHouts = _EsisESHouts_Object(
    (1, 3, 6, 1, 3, 1, 4, 2),
    _EsisESHouts_Type()
)
esisESHouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esisESHouts.setStatus("mandatory")
_EsisISHins_Type = Counter32
_EsisISHins_Object = MibScalar
esisISHins = _EsisISHins_Object(
    (1, 3, 6, 1, 3, 1, 4, 3),
    _EsisISHins_Type()
)
esisISHins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esisISHins.setStatus("mandatory")
_EsisISHouts_Type = Counter32
_EsisISHouts_Object = MibScalar
esisISHouts = _EsisISHouts_Object(
    (1, 3, 6, 1, 3, 1, 4, 4),
    _EsisISHouts_Type()
)
esisISHouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esisISHouts.setStatus("mandatory")
_EsisRDUins_Type = Counter32
_EsisRDUins_Object = MibScalar
esisRDUins = _EsisRDUins_Object(
    (1, 3, 6, 1, 3, 1, 4, 5),
    _EsisRDUins_Type()
)
esisRDUins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esisRDUins.setStatus("mandatory")
_EsisRDUouts_Type = Counter32
_EsisRDUouts_Object = MibScalar
esisRDUouts = _EsisRDUouts_Object(
    (1, 3, 6, 1, 3, 1, 4, 6),
    _EsisRDUouts_Type()
)
esisRDUouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esisRDUouts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLNS-MIB",
    **{"ClnpAddress": ClnpAddress,
       "clns": clns,
       "clnp": clnp,
       "clnpForwarding": clnpForwarding,
       "clnpDefaultLifeTime": clnpDefaultLifeTime,
       "clnpInReceives": clnpInReceives,
       "clnpInHdrErrors": clnpInHdrErrors,
       "clnpInAddrErrors": clnpInAddrErrors,
       "clnpForwPDUs": clnpForwPDUs,
       "clnpInUnknownNLPs": clnpInUnknownNLPs,
       "clnpInUnknownULPs": clnpInUnknownULPs,
       "clnpInDiscards": clnpInDiscards,
       "clnpInDelivers": clnpInDelivers,
       "clnpOutRequests": clnpOutRequests,
       "clnpOutDiscards": clnpOutDiscards,
       "clnpOutNoRoutes": clnpOutNoRoutes,
       "clnpReasmTimeout": clnpReasmTimeout,
       "clnpReasmReqds": clnpReasmReqds,
       "clnpReasmOKs": clnpReasmOKs,
       "clnpReasmFails": clnpReasmFails,
       "clnpSegOKs": clnpSegOKs,
       "clnpSegFails": clnpSegFails,
       "clnpSegCreates": clnpSegCreates,
       "clnpAddrTable": clnpAddrTable,
       "clnpAddrEntry": clnpAddrEntry,
       "clnpAdEntAddr": clnpAdEntAddr,
       "clnpAdEntIfIndex": clnpAdEntIfIndex,
       "clnpAdEntReasmMaxSize": clnpAdEntReasmMaxSize,
       "clnpRoutingTable": clnpRoutingTable,
       "clnpRouteEntry": clnpRouteEntry,
       "clnpRouteDest": clnpRouteDest,
       "clnpRouteIfIndex": clnpRouteIfIndex,
       "clnpRouteMetric1": clnpRouteMetric1,
       "clnpRouteMetric2": clnpRouteMetric2,
       "clnpRouteMetric3": clnpRouteMetric3,
       "clnpRouteMetric4": clnpRouteMetric4,
       "clnpRouteNextHop": clnpRouteNextHop,
       "clnpRouteType": clnpRouteType,
       "clnpRouteProto": clnpRouteProto,
       "clnpRouteAge": clnpRouteAge,
       "clnpRouteMetric5": clnpRouteMetric5,
       "clnpRouteInfo": clnpRouteInfo,
       "clnpNetToMediaTable": clnpNetToMediaTable,
       "clnpNetToMediaEntry": clnpNetToMediaEntry,
       "clnpNetToMediaIfIndex": clnpNetToMediaIfIndex,
       "clnpNetToMediaPhysAddress": clnpNetToMediaPhysAddress,
       "clnpNetToMediaNetAddress": clnpNetToMediaNetAddress,
       "clnpNetToMediaType": clnpNetToMediaType,
       "clnpNetToMediaAge": clnpNetToMediaAge,
       "clnpNetToMediaHoldTime": clnpNetToMediaHoldTime,
       "clnpMediaToNetTable": clnpMediaToNetTable,
       "clnpMediaToNetEntry": clnpMediaToNetEntry,
       "clnpMediaToNetIfIndex": clnpMediaToNetIfIndex,
       "clnpMediaToNetAddress": clnpMediaToNetAddress,
       "clnpMediaToNetPhysAddress": clnpMediaToNetPhysAddress,
       "clnpMediaToNetType": clnpMediaToNetType,
       "clnpMediaToNetAge": clnpMediaToNetAge,
       "clnpMediaToNetHoldTime": clnpMediaToNetHoldTime,
       "clnpInOpts": clnpInOpts,
       "clnpOutOpts": clnpOutOpts,
       "clnpRoutingDiscards": clnpRoutingDiscards,
       "error": error,
       "clnpInErrors": clnpInErrors,
       "clnpOutErrors": clnpOutErrors,
       "clnpInErrUnspecs": clnpInErrUnspecs,
       "clnpInErrProcs": clnpInErrProcs,
       "clnpInErrCksums": clnpInErrCksums,
       "clnpInErrCongests": clnpInErrCongests,
       "clnpInErrHdrs": clnpInErrHdrs,
       "clnpInErrSegs": clnpInErrSegs,
       "clnpInErrIncomps": clnpInErrIncomps,
       "clnpInErrDups": clnpInErrDups,
       "clnpInErrUnreachDsts": clnpInErrUnreachDsts,
       "clnpInErrUnknownDsts": clnpInErrUnknownDsts,
       "clnpInErrSRUnspecs": clnpInErrSRUnspecs,
       "clnpInErrSRSyntaxes": clnpInErrSRSyntaxes,
       "clnpInErrSRUnkAddrs": clnpInErrSRUnkAddrs,
       "clnpInErrSRBadPaths": clnpInErrSRBadPaths,
       "clnpInErrHops": clnpInErrHops,
       "clnpInErrHopReassms": clnpInErrHopReassms,
       "clnpInErrUnsOptions": clnpInErrUnsOptions,
       "clnpInErrUnsVersions": clnpInErrUnsVersions,
       "clnpInErrUnsSecurities": clnpInErrUnsSecurities,
       "clnpInErrUnsSRs": clnpInErrUnsSRs,
       "clnpInErrUnsRRs": clnpInErrUnsRRs,
       "clnpInErrInterferences": clnpInErrInterferences,
       "clnpOutErrUnspecs": clnpOutErrUnspecs,
       "clnpOutErrProcs": clnpOutErrProcs,
       "clnpOutErrCksums": clnpOutErrCksums,
       "clnpOutErrCongests": clnpOutErrCongests,
       "clnpOutErrHdrs": clnpOutErrHdrs,
       "clnpOutErrSegs": clnpOutErrSegs,
       "clnpOutErrIncomps": clnpOutErrIncomps,
       "clnpOutErrDups": clnpOutErrDups,
       "clnpOutErrUnreachDsts": clnpOutErrUnreachDsts,
       "clnpOutErrUnknownDsts": clnpOutErrUnknownDsts,
       "clnpOutErrSRUnspecs": clnpOutErrSRUnspecs,
       "clnpOutErrSRSyntaxes": clnpOutErrSRSyntaxes,
       "clnpOutErrSRUnkAddrs": clnpOutErrSRUnkAddrs,
       "clnpOutErrSRBadPaths": clnpOutErrSRBadPaths,
       "clnpOutErrHops": clnpOutErrHops,
       "clnpOutErrHopReassms": clnpOutErrHopReassms,
       "clnpOutErrUnsOptions": clnpOutErrUnsOptions,
       "clnpOutErrUnsVersions": clnpOutErrUnsVersions,
       "clnpOutErrUnsSecurities": clnpOutErrUnsSecurities,
       "clnpOutErrUnsSRs": clnpOutErrUnsSRs,
       "clnpOutErrUnsRRs": clnpOutErrUnsRRs,
       "clnpOutErrInterferences": clnpOutErrInterferences,
       "echo": echo,
       "es-is": es_is,
       "esisESHins": esisESHins,
       "esisESHouts": esisESHouts,
       "esisISHins": esisISHins,
       "esisISHouts": esisISHouts,
       "esisRDUins": esisRDUins,
       "esisRDUouts": esisRDUouts}
)
