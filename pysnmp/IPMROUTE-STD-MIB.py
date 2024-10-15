# SNMP MIB module (IPMROUTE-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPMROUTE-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:27 2024
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

(IANAipMRouteProtocol,
 IANAipRouteProtocol) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol",
    "IANAipRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

ipMRouteStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 83)
)
ipMRouteStdMIB.setRevisions(
        ("2000-09-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LanguageTag(OctetString, TextualConvention):
    status = "current"
    displayHint = "100a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )



# MIB Managed Objects in the order of their OIDs

_IpMRouteMIBObjects_ObjectIdentity = ObjectIdentity
ipMRouteMIBObjects = _IpMRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 83, 1)
)
_IpMRoute_ObjectIdentity = ObjectIdentity
ipMRoute = _IpMRoute_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 83, 1, 1)
)


class _IpMRouteEnable_Type(Integer32):
    """Custom type ipMRouteEnable based on Integer32"""
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


_IpMRouteEnable_Type.__name__ = "Integer32"
_IpMRouteEnable_Object = MibScalar
ipMRouteEnable = _IpMRouteEnable_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 1),
    _IpMRouteEnable_Type()
)
ipMRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMRouteEnable.setStatus("current")
_IpMRouteTable_Object = MibTable
ipMRouteTable = _IpMRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipMRouteTable.setStatus("current")
_IpMRouteEntry_Object = MibTableRow
ipMRouteEntry = _IpMRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1)
)
ipMRouteEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    ipMRouteEntry.setStatus("current")
_IpMRouteGroup_Type = IpAddress
_IpMRouteGroup_Object = MibTableColumn
ipMRouteGroup = _IpMRouteGroup_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 1),
    _IpMRouteGroup_Type()
)
ipMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteGroup.setStatus("current")
_IpMRouteSource_Type = IpAddress
_IpMRouteSource_Object = MibTableColumn
ipMRouteSource = _IpMRouteSource_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 2),
    _IpMRouteSource_Type()
)
ipMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteSource.setStatus("current")
_IpMRouteSourceMask_Type = IpAddress
_IpMRouteSourceMask_Object = MibTableColumn
ipMRouteSourceMask = _IpMRouteSourceMask_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 3),
    _IpMRouteSourceMask_Type()
)
ipMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteSourceMask.setStatus("current")
_IpMRouteUpstreamNeighbor_Type = IpAddress
_IpMRouteUpstreamNeighbor_Object = MibTableColumn
ipMRouteUpstreamNeighbor = _IpMRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 4),
    _IpMRouteUpstreamNeighbor_Type()
)
ipMRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteUpstreamNeighbor.setStatus("current")
_IpMRouteInIfIndex_Type = InterfaceIndexOrZero
_IpMRouteInIfIndex_Object = MibTableColumn
ipMRouteInIfIndex = _IpMRouteInIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 5),
    _IpMRouteInIfIndex_Type()
)
ipMRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInIfIndex.setStatus("current")
_IpMRouteUpTime_Type = TimeTicks
_IpMRouteUpTime_Object = MibTableColumn
ipMRouteUpTime = _IpMRouteUpTime_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 6),
    _IpMRouteUpTime_Type()
)
ipMRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteUpTime.setStatus("current")
_IpMRouteExpiryTime_Type = TimeTicks
_IpMRouteExpiryTime_Object = MibTableColumn
ipMRouteExpiryTime = _IpMRouteExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 7),
    _IpMRouteExpiryTime_Type()
)
ipMRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteExpiryTime.setStatus("current")
_IpMRoutePkts_Type = Counter32
_IpMRoutePkts_Object = MibTableColumn
ipMRoutePkts = _IpMRoutePkts_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 8),
    _IpMRoutePkts_Type()
)
ipMRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoutePkts.setStatus("current")
_IpMRouteDifferentInIfPackets_Type = Counter32
_IpMRouteDifferentInIfPackets_Object = MibTableColumn
ipMRouteDifferentInIfPackets = _IpMRouteDifferentInIfPackets_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 9),
    _IpMRouteDifferentInIfPackets_Type()
)
ipMRouteDifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteDifferentInIfPackets.setStatus("current")
_IpMRouteOctets_Type = Counter32
_IpMRouteOctets_Object = MibTableColumn
ipMRouteOctets = _IpMRouteOctets_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 10),
    _IpMRouteOctets_Type()
)
ipMRouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteOctets.setStatus("current")
_IpMRouteProtocol_Type = IANAipMRouteProtocol
_IpMRouteProtocol_Object = MibTableColumn
ipMRouteProtocol = _IpMRouteProtocol_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 11),
    _IpMRouteProtocol_Type()
)
ipMRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteProtocol.setStatus("current")
_IpMRouteRtProto_Type = IANAipRouteProtocol
_IpMRouteRtProto_Object = MibTableColumn
ipMRouteRtProto = _IpMRouteRtProto_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 12),
    _IpMRouteRtProto_Type()
)
ipMRouteRtProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteRtProto.setStatus("current")
_IpMRouteRtAddress_Type = IpAddress
_IpMRouteRtAddress_Object = MibTableColumn
ipMRouteRtAddress = _IpMRouteRtAddress_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 13),
    _IpMRouteRtAddress_Type()
)
ipMRouteRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteRtAddress.setStatus("current")
_IpMRouteRtMask_Type = IpAddress
_IpMRouteRtMask_Object = MibTableColumn
ipMRouteRtMask = _IpMRouteRtMask_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 14),
    _IpMRouteRtMask_Type()
)
ipMRouteRtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteRtMask.setStatus("current")


class _IpMRouteRtType_Type(Integer32):
    """Custom type ipMRouteRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_IpMRouteRtType_Type.__name__ = "Integer32"
_IpMRouteRtType_Object = MibTableColumn
ipMRouteRtType = _IpMRouteRtType_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 15),
    _IpMRouteRtType_Type()
)
ipMRouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteRtType.setStatus("current")
_IpMRouteHCOctets_Type = Counter64
_IpMRouteHCOctets_Object = MibTableColumn
ipMRouteHCOctets = _IpMRouteHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 16),
    _IpMRouteHCOctets_Type()
)
ipMRouteHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteHCOctets.setStatus("current")
_IpMRouteNextHopTable_Object = MibTable
ipMRouteNextHopTable = _IpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipMRouteNextHopTable.setStatus("current")
_IpMRouteNextHopEntry_Object = MibTableRow
ipMRouteNextHopEntry = _IpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1)
)
ipMRouteNextHopEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    ipMRouteNextHopEntry.setStatus("current")
_IpMRouteNextHopGroup_Type = IpAddress
_IpMRouteNextHopGroup_Object = MibTableColumn
ipMRouteNextHopGroup = _IpMRouteNextHopGroup_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 1),
    _IpMRouteNextHopGroup_Type()
)
ipMRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopGroup.setStatus("current")
_IpMRouteNextHopSource_Type = IpAddress
_IpMRouteNextHopSource_Object = MibTableColumn
ipMRouteNextHopSource = _IpMRouteNextHopSource_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 2),
    _IpMRouteNextHopSource_Type()
)
ipMRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopSource.setStatus("current")
_IpMRouteNextHopSourceMask_Type = IpAddress
_IpMRouteNextHopSourceMask_Object = MibTableColumn
ipMRouteNextHopSourceMask = _IpMRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 3),
    _IpMRouteNextHopSourceMask_Type()
)
ipMRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopSourceMask.setStatus("current")
_IpMRouteNextHopIfIndex_Type = InterfaceIndex
_IpMRouteNextHopIfIndex_Object = MibTableColumn
ipMRouteNextHopIfIndex = _IpMRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 4),
    _IpMRouteNextHopIfIndex_Type()
)
ipMRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopIfIndex.setStatus("current")
_IpMRouteNextHopAddress_Type = IpAddress
_IpMRouteNextHopAddress_Object = MibTableColumn
ipMRouteNextHopAddress = _IpMRouteNextHopAddress_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 5),
    _IpMRouteNextHopAddress_Type()
)
ipMRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopAddress.setStatus("current")


class _IpMRouteNextHopState_Type(Integer32):
    """Custom type ipMRouteNextHopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 2),
          ("pruned", 1))
    )


_IpMRouteNextHopState_Type.__name__ = "Integer32"
_IpMRouteNextHopState_Object = MibTableColumn
ipMRouteNextHopState = _IpMRouteNextHopState_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 6),
    _IpMRouteNextHopState_Type()
)
ipMRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteNextHopState.setStatus("current")
_IpMRouteNextHopUpTime_Type = TimeTicks
_IpMRouteNextHopUpTime_Object = MibTableColumn
ipMRouteNextHopUpTime = _IpMRouteNextHopUpTime_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 7),
    _IpMRouteNextHopUpTime_Type()
)
ipMRouteNextHopUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteNextHopUpTime.setStatus("current")
_IpMRouteNextHopExpiryTime_Type = TimeTicks
_IpMRouteNextHopExpiryTime_Object = MibTableColumn
ipMRouteNextHopExpiryTime = _IpMRouteNextHopExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 8),
    _IpMRouteNextHopExpiryTime_Type()
)
ipMRouteNextHopExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteNextHopExpiryTime.setStatus("current")
_IpMRouteNextHopClosestMemberHops_Type = Integer32
_IpMRouteNextHopClosestMemberHops_Object = MibTableColumn
ipMRouteNextHopClosestMemberHops = _IpMRouteNextHopClosestMemberHops_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 9),
    _IpMRouteNextHopClosestMemberHops_Type()
)
ipMRouteNextHopClosestMemberHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteNextHopClosestMemberHops.setStatus("current")
_IpMRouteNextHopProtocol_Type = IANAipMRouteProtocol
_IpMRouteNextHopProtocol_Object = MibTableColumn
ipMRouteNextHopProtocol = _IpMRouteNextHopProtocol_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 10),
    _IpMRouteNextHopProtocol_Type()
)
ipMRouteNextHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteNextHopProtocol.setStatus("current")
_IpMRouteNextHopPkts_Type = Counter32
_IpMRouteNextHopPkts_Object = MibTableColumn
ipMRouteNextHopPkts = _IpMRouteNextHopPkts_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 11),
    _IpMRouteNextHopPkts_Type()
)
ipMRouteNextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteNextHopPkts.setStatus("current")
_IpMRouteInterfaceTable_Object = MibTable
ipMRouteInterfaceTable = _IpMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipMRouteInterfaceTable.setStatus("current")
_IpMRouteInterfaceEntry_Object = MibTableRow
ipMRouteInterfaceEntry = _IpMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1)
)
ipMRouteInterfaceEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ipMRouteInterfaceEntry.setStatus("current")
_IpMRouteInterfaceIfIndex_Type = InterfaceIndex
_IpMRouteInterfaceIfIndex_Object = MibTableColumn
ipMRouteInterfaceIfIndex = _IpMRouteInterfaceIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 1),
    _IpMRouteInterfaceIfIndex_Type()
)
ipMRouteInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteInterfaceIfIndex.setStatus("current")


class _IpMRouteInterfaceTtl_Type(Integer32):
    """Custom type ipMRouteInterfaceTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpMRouteInterfaceTtl_Type.__name__ = "Integer32"
_IpMRouteInterfaceTtl_Object = MibTableColumn
ipMRouteInterfaceTtl = _IpMRouteInterfaceTtl_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 2),
    _IpMRouteInterfaceTtl_Type()
)
ipMRouteInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMRouteInterfaceTtl.setStatus("current")
_IpMRouteInterfaceProtocol_Type = IANAipMRouteProtocol
_IpMRouteInterfaceProtocol_Object = MibTableColumn
ipMRouteInterfaceProtocol = _IpMRouteInterfaceProtocol_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 3),
    _IpMRouteInterfaceProtocol_Type()
)
ipMRouteInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceProtocol.setStatus("current")


class _IpMRouteInterfaceRateLimit_Type(Integer32):
    """Custom type ipMRouteInterfaceRateLimit based on Integer32"""
    defaultValue = 0


_IpMRouteInterfaceRateLimit_Object = MibTableColumn
ipMRouteInterfaceRateLimit = _IpMRouteInterfaceRateLimit_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 4),
    _IpMRouteInterfaceRateLimit_Type()
)
ipMRouteInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMRouteInterfaceRateLimit.setStatus("current")
_IpMRouteInterfaceInMcastOctets_Type = Counter32
_IpMRouteInterfaceInMcastOctets_Object = MibTableColumn
ipMRouteInterfaceInMcastOctets = _IpMRouteInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 5),
    _IpMRouteInterfaceInMcastOctets_Type()
)
ipMRouteInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceInMcastOctets.setStatus("current")
_IpMRouteInterfaceOutMcastOctets_Type = Counter32
_IpMRouteInterfaceOutMcastOctets_Object = MibTableColumn
ipMRouteInterfaceOutMcastOctets = _IpMRouteInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 6),
    _IpMRouteInterfaceOutMcastOctets_Type()
)
ipMRouteInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceOutMcastOctets.setStatus("current")
_IpMRouteInterfaceHCInMcastOctets_Type = Counter64
_IpMRouteInterfaceHCInMcastOctets_Object = MibTableColumn
ipMRouteInterfaceHCInMcastOctets = _IpMRouteInterfaceHCInMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 7),
    _IpMRouteInterfaceHCInMcastOctets_Type()
)
ipMRouteInterfaceHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceHCInMcastOctets.setStatus("current")
_IpMRouteInterfaceHCOutMcastOctets_Type = Counter64
_IpMRouteInterfaceHCOutMcastOctets_Object = MibTableColumn
ipMRouteInterfaceHCOutMcastOctets = _IpMRouteInterfaceHCOutMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 8),
    _IpMRouteInterfaceHCOutMcastOctets_Type()
)
ipMRouteInterfaceHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceHCOutMcastOctets.setStatus("current")
_IpMRouteBoundaryTable_Object = MibTable
ipMRouteBoundaryTable = _IpMRouteBoundaryTable_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ipMRouteBoundaryTable.setStatus("current")
_IpMRouteBoundaryEntry_Object = MibTableRow
ipMRouteBoundaryEntry = _IpMRouteBoundaryEntry_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1)
)
ipMRouteBoundaryEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteBoundaryIfIndex"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteBoundaryAddress"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteBoundaryAddressMask"),
)
if mibBuilder.loadTexts:
    ipMRouteBoundaryEntry.setStatus("current")
_IpMRouteBoundaryIfIndex_Type = InterfaceIndex
_IpMRouteBoundaryIfIndex_Object = MibTableColumn
ipMRouteBoundaryIfIndex = _IpMRouteBoundaryIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 1),
    _IpMRouteBoundaryIfIndex_Type()
)
ipMRouteBoundaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteBoundaryIfIndex.setStatus("current")
_IpMRouteBoundaryAddress_Type = IpAddress
_IpMRouteBoundaryAddress_Object = MibTableColumn
ipMRouteBoundaryAddress = _IpMRouteBoundaryAddress_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 2),
    _IpMRouteBoundaryAddress_Type()
)
ipMRouteBoundaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteBoundaryAddress.setStatus("current")
_IpMRouteBoundaryAddressMask_Type = IpAddress
_IpMRouteBoundaryAddressMask_Object = MibTableColumn
ipMRouteBoundaryAddressMask = _IpMRouteBoundaryAddressMask_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 3),
    _IpMRouteBoundaryAddressMask_Type()
)
ipMRouteBoundaryAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteBoundaryAddressMask.setStatus("current")
_IpMRouteBoundaryStatus_Type = RowStatus
_IpMRouteBoundaryStatus_Object = MibTableColumn
ipMRouteBoundaryStatus = _IpMRouteBoundaryStatus_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 4),
    _IpMRouteBoundaryStatus_Type()
)
ipMRouteBoundaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMRouteBoundaryStatus.setStatus("current")
_IpMRouteScopeNameTable_Object = MibTable
ipMRouteScopeNameTable = _IpMRouteScopeNameTable_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipMRouteScopeNameTable.setStatus("current")
_IpMRouteScopeNameEntry_Object = MibTableRow
ipMRouteScopeNameEntry = _IpMRouteScopeNameEntry_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1)
)
ipMRouteScopeNameEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteScopeNameAddress"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteScopeNameAddressMask"),
    (1, "IPMROUTE-STD-MIB", "ipMRouteScopeNameLanguage"),
)
if mibBuilder.loadTexts:
    ipMRouteScopeNameEntry.setStatus("current")
_IpMRouteScopeNameAddress_Type = IpAddress
_IpMRouteScopeNameAddress_Object = MibTableColumn
ipMRouteScopeNameAddress = _IpMRouteScopeNameAddress_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 1),
    _IpMRouteScopeNameAddress_Type()
)
ipMRouteScopeNameAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteScopeNameAddress.setStatus("current")
_IpMRouteScopeNameAddressMask_Type = IpAddress
_IpMRouteScopeNameAddressMask_Object = MibTableColumn
ipMRouteScopeNameAddressMask = _IpMRouteScopeNameAddressMask_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 2),
    _IpMRouteScopeNameAddressMask_Type()
)
ipMRouteScopeNameAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteScopeNameAddressMask.setStatus("current")
_IpMRouteScopeNameLanguage_Type = LanguageTag
_IpMRouteScopeNameLanguage_Object = MibTableColumn
ipMRouteScopeNameLanguage = _IpMRouteScopeNameLanguage_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 3),
    _IpMRouteScopeNameLanguage_Type()
)
ipMRouteScopeNameLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteScopeNameLanguage.setStatus("current")
_IpMRouteScopeNameString_Type = SnmpAdminString
_IpMRouteScopeNameString_Object = MibTableColumn
ipMRouteScopeNameString = _IpMRouteScopeNameString_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 4),
    _IpMRouteScopeNameString_Type()
)
ipMRouteScopeNameString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMRouteScopeNameString.setStatus("current")


class _IpMRouteScopeNameDefault_Type(TruthValue):
    """Custom type ipMRouteScopeNameDefault based on TruthValue"""


_IpMRouteScopeNameDefault_Object = MibTableColumn
ipMRouteScopeNameDefault = _IpMRouteScopeNameDefault_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 5),
    _IpMRouteScopeNameDefault_Type()
)
ipMRouteScopeNameDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMRouteScopeNameDefault.setStatus("current")
_IpMRouteScopeNameStatus_Type = RowStatus
_IpMRouteScopeNameStatus_Object = MibTableColumn
ipMRouteScopeNameStatus = _IpMRouteScopeNameStatus_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 6),
    _IpMRouteScopeNameStatus_Type()
)
ipMRouteScopeNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMRouteScopeNameStatus.setStatus("current")
_IpMRouteEntryCount_Type = Gauge32
_IpMRouteEntryCount_Object = MibScalar
ipMRouteEntryCount = _IpMRouteEntryCount_Object(
    (1, 3, 6, 1, 2, 1, 83, 1, 1, 7),
    _IpMRouteEntryCount_Type()
)
ipMRouteEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteEntryCount.setStatus("current")
_IpMRouteMIBConformance_ObjectIdentity = ObjectIdentity
ipMRouteMIBConformance = _IpMRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 83, 2)
)
_IpMRouteMIBCompliances_ObjectIdentity = ObjectIdentity
ipMRouteMIBCompliances = _IpMRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 83, 2, 1)
)
_IpMRouteMIBGroups_ObjectIdentity = ObjectIdentity
ipMRouteMIBGroups = _IpMRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 83, 2, 2)
)

# Managed Objects groups

ipMRouteMIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 83, 2, 2, 1)
)
ipMRouteMIBBasicGroup.setObjects(
      *(("IPMROUTE-STD-MIB", "ipMRouteEnable"),
        ("IPMROUTE-STD-MIB", "ipMRouteEntryCount"),
        ("IPMROUTE-STD-MIB", "ipMRouteUpstreamNeighbor"),
        ("IPMROUTE-STD-MIB", "ipMRouteInIfIndex"),
        ("IPMROUTE-STD-MIB", "ipMRouteUpTime"),
        ("IPMROUTE-STD-MIB", "ipMRouteExpiryTime"),
        ("IPMROUTE-STD-MIB", "ipMRouteNextHopState"),
        ("IPMROUTE-STD-MIB", "ipMRouteNextHopUpTime"),
        ("IPMROUTE-STD-MIB", "ipMRouteNextHopExpiryTime"),
        ("IPMROUTE-STD-MIB", "ipMRouteNextHopProtocol"),
        ("IPMROUTE-STD-MIB", "ipMRouteNextHopPkts"),
        ("IPMROUTE-STD-MIB", "ipMRouteInterfaceTtl"),
        ("IPMROUTE-STD-MIB", "ipMRouteInterfaceProtocol"),
        ("IPMROUTE-STD-MIB", "ipMRouteInterfaceRateLimit"),
        ("IPMROUTE-STD-MIB", "ipMRouteInterfaceInMcastOctets"),
        ("IPMROUTE-STD-MIB", "ipMRouteInterfaceOutMcastOctets"),
        ("IPMROUTE-STD-MIB", "ipMRouteProtocol"))
)
if mibBuilder.loadTexts:
    ipMRouteMIBBasicGroup.setStatus("current")

ipMRouteMIBHopCountGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 83, 2, 2, 2)
)
ipMRouteMIBHopCountGroup.setObjects(
    ("IPMROUTE-STD-MIB", "ipMRouteNextHopClosestMemberHops")
)
if mibBuilder.loadTexts:
    ipMRouteMIBHopCountGroup.setStatus("current")

ipMRouteMIBBoundaryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 83, 2, 2, 3)
)
ipMRouteMIBBoundaryGroup.setObjects(
      *(("IPMROUTE-STD-MIB", "ipMRouteBoundaryStatus"),
        ("IPMROUTE-STD-MIB", "ipMRouteScopeNameString"),
        ("IPMROUTE-STD-MIB", "ipMRouteScopeNameDefault"),
        ("IPMROUTE-STD-MIB", "ipMRouteScopeNameStatus"))
)
if mibBuilder.loadTexts:
    ipMRouteMIBBoundaryGroup.setStatus("current")

ipMRouteMIBPktsOutGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 83, 2, 2, 4)
)
ipMRouteMIBPktsOutGroup.setObjects(
    ("IPMROUTE-STD-MIB", "ipMRouteNextHopPkts")
)
if mibBuilder.loadTexts:
    ipMRouteMIBPktsOutGroup.setStatus("current")

ipMRouteMIBHCInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 83, 2, 2, 5)
)
ipMRouteMIBHCInterfaceGroup.setObjects(
      *(("IPMROUTE-STD-MIB", "ipMRouteInterfaceHCInMcastOctets"),
        ("IPMROUTE-STD-MIB", "ipMRouteInterfaceHCOutMcastOctets"),
        ("IPMROUTE-STD-MIB", "ipMRouteHCOctets"))
)
if mibBuilder.loadTexts:
    ipMRouteMIBHCInterfaceGroup.setStatus("current")

ipMRouteMIBRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 83, 2, 2, 6)
)
ipMRouteMIBRouteGroup.setObjects(
      *(("IPMROUTE-STD-MIB", "ipMRouteRtProto"),
        ("IPMROUTE-STD-MIB", "ipMRouteRtAddress"),
        ("IPMROUTE-STD-MIB", "ipMRouteRtMask"),
        ("IPMROUTE-STD-MIB", "ipMRouteRtType"))
)
if mibBuilder.loadTexts:
    ipMRouteMIBRouteGroup.setStatus("current")

ipMRouteMIBPktsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 83, 2, 2, 7)
)
ipMRouteMIBPktsGroup.setObjects(
      *(("IPMROUTE-STD-MIB", "ipMRoutePkts"),
        ("IPMROUTE-STD-MIB", "ipMRouteDifferentInIfPackets"),
        ("IPMROUTE-STD-MIB", "ipMRouteOctets"))
)
if mibBuilder.loadTexts:
    ipMRouteMIBPktsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipMRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 83, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipMRouteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPMROUTE-STD-MIB",
    **{"LanguageTag": LanguageTag,
       "ipMRouteStdMIB": ipMRouteStdMIB,
       "ipMRouteMIBObjects": ipMRouteMIBObjects,
       "ipMRoute": ipMRoute,
       "ipMRouteEnable": ipMRouteEnable,
       "ipMRouteTable": ipMRouteTable,
       "ipMRouteEntry": ipMRouteEntry,
       "ipMRouteGroup": ipMRouteGroup,
       "ipMRouteSource": ipMRouteSource,
       "ipMRouteSourceMask": ipMRouteSourceMask,
       "ipMRouteUpstreamNeighbor": ipMRouteUpstreamNeighbor,
       "ipMRouteInIfIndex": ipMRouteInIfIndex,
       "ipMRouteUpTime": ipMRouteUpTime,
       "ipMRouteExpiryTime": ipMRouteExpiryTime,
       "ipMRoutePkts": ipMRoutePkts,
       "ipMRouteDifferentInIfPackets": ipMRouteDifferentInIfPackets,
       "ipMRouteOctets": ipMRouteOctets,
       "ipMRouteProtocol": ipMRouteProtocol,
       "ipMRouteRtProto": ipMRouteRtProto,
       "ipMRouteRtAddress": ipMRouteRtAddress,
       "ipMRouteRtMask": ipMRouteRtMask,
       "ipMRouteRtType": ipMRouteRtType,
       "ipMRouteHCOctets": ipMRouteHCOctets,
       "ipMRouteNextHopTable": ipMRouteNextHopTable,
       "ipMRouteNextHopEntry": ipMRouteNextHopEntry,
       "ipMRouteNextHopGroup": ipMRouteNextHopGroup,
       "ipMRouteNextHopSource": ipMRouteNextHopSource,
       "ipMRouteNextHopSourceMask": ipMRouteNextHopSourceMask,
       "ipMRouteNextHopIfIndex": ipMRouteNextHopIfIndex,
       "ipMRouteNextHopAddress": ipMRouteNextHopAddress,
       "ipMRouteNextHopState": ipMRouteNextHopState,
       "ipMRouteNextHopUpTime": ipMRouteNextHopUpTime,
       "ipMRouteNextHopExpiryTime": ipMRouteNextHopExpiryTime,
       "ipMRouteNextHopClosestMemberHops": ipMRouteNextHopClosestMemberHops,
       "ipMRouteNextHopProtocol": ipMRouteNextHopProtocol,
       "ipMRouteNextHopPkts": ipMRouteNextHopPkts,
       "ipMRouteInterfaceTable": ipMRouteInterfaceTable,
       "ipMRouteInterfaceEntry": ipMRouteInterfaceEntry,
       "ipMRouteInterfaceIfIndex": ipMRouteInterfaceIfIndex,
       "ipMRouteInterfaceTtl": ipMRouteInterfaceTtl,
       "ipMRouteInterfaceProtocol": ipMRouteInterfaceProtocol,
       "ipMRouteInterfaceRateLimit": ipMRouteInterfaceRateLimit,
       "ipMRouteInterfaceInMcastOctets": ipMRouteInterfaceInMcastOctets,
       "ipMRouteInterfaceOutMcastOctets": ipMRouteInterfaceOutMcastOctets,
       "ipMRouteInterfaceHCInMcastOctets": ipMRouteInterfaceHCInMcastOctets,
       "ipMRouteInterfaceHCOutMcastOctets": ipMRouteInterfaceHCOutMcastOctets,
       "ipMRouteBoundaryTable": ipMRouteBoundaryTable,
       "ipMRouteBoundaryEntry": ipMRouteBoundaryEntry,
       "ipMRouteBoundaryIfIndex": ipMRouteBoundaryIfIndex,
       "ipMRouteBoundaryAddress": ipMRouteBoundaryAddress,
       "ipMRouteBoundaryAddressMask": ipMRouteBoundaryAddressMask,
       "ipMRouteBoundaryStatus": ipMRouteBoundaryStatus,
       "ipMRouteScopeNameTable": ipMRouteScopeNameTable,
       "ipMRouteScopeNameEntry": ipMRouteScopeNameEntry,
       "ipMRouteScopeNameAddress": ipMRouteScopeNameAddress,
       "ipMRouteScopeNameAddressMask": ipMRouteScopeNameAddressMask,
       "ipMRouteScopeNameLanguage": ipMRouteScopeNameLanguage,
       "ipMRouteScopeNameString": ipMRouteScopeNameString,
       "ipMRouteScopeNameDefault": ipMRouteScopeNameDefault,
       "ipMRouteScopeNameStatus": ipMRouteScopeNameStatus,
       "ipMRouteEntryCount": ipMRouteEntryCount,
       "ipMRouteMIBConformance": ipMRouteMIBConformance,
       "ipMRouteMIBCompliances": ipMRouteMIBCompliances,
       "ipMRouteMIBCompliance": ipMRouteMIBCompliance,
       "ipMRouteMIBGroups": ipMRouteMIBGroups,
       "ipMRouteMIBBasicGroup": ipMRouteMIBBasicGroup,
       "ipMRouteMIBHopCountGroup": ipMRouteMIBHopCountGroup,
       "ipMRouteMIBBoundaryGroup": ipMRouteMIBBoundaryGroup,
       "ipMRouteMIBPktsOutGroup": ipMRouteMIBPktsOutGroup,
       "ipMRouteMIBHCInterfaceGroup": ipMRouteMIBHCInterfaceGroup,
       "ipMRouteMIBRouteGroup": ipMRouteMIBRouteGroup,
       "ipMRouteMIBPktsGroup": ipMRouteMIBPktsGroup}
)
