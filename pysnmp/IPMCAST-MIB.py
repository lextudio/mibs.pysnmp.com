# SNMP MIB module (IPMCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPMCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:55 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion",
    "InetZoneIndex")

(LangTag,) = mibBuilder.importSymbols(
    "LANGTAG-TC-MIB",
    "LangTag")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ipMcastMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 168)
)
ipMcastMIB.setRevisions(
        ("2007-11-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpMcast_ObjectIdentity = ObjectIdentity
ipMcast = _IpMcast_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 168, 1)
)
_IpMcastEnabled_Type = TruthValue
_IpMcastEnabled_Object = MibScalar
ipMcastEnabled = _IpMcastEnabled_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 1),
    _IpMcastEnabled_Type()
)
ipMcastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMcastEnabled.setStatus("current")
_IpMcastRouteEntryCount_Type = Gauge32
_IpMcastRouteEntryCount_Object = MibScalar
ipMcastRouteEntryCount = _IpMcastRouteEntryCount_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 2),
    _IpMcastRouteEntryCount_Type()
)
ipMcastRouteEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteEntryCount.setStatus("current")
_IpMcastInterfaceTable_Object = MibTable
ipMcastInterfaceTable = _IpMcastInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 3)
)
if mibBuilder.loadTexts:
    ipMcastInterfaceTable.setStatus("current")
_IpMcastInterfaceEntry_Object = MibTableRow
ipMcastInterfaceEntry = _IpMcastInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 3, 1)
)
ipMcastInterfaceEntry.setIndexNames(
    (0, "IPMCAST-MIB", "ipMcastInterfaceIPVersion"),
    (0, "IPMCAST-MIB", "ipMcastInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ipMcastInterfaceEntry.setStatus("current")
_IpMcastInterfaceIPVersion_Type = InetVersion
_IpMcastInterfaceIPVersion_Object = MibTableColumn
ipMcastInterfaceIPVersion = _IpMcastInterfaceIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 3, 1, 1),
    _IpMcastInterfaceIPVersion_Type()
)
ipMcastInterfaceIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastInterfaceIPVersion.setStatus("current")
_IpMcastInterfaceIfIndex_Type = InterfaceIndex
_IpMcastInterfaceIfIndex_Object = MibTableColumn
ipMcastInterfaceIfIndex = _IpMcastInterfaceIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 3, 1, 2),
    _IpMcastInterfaceIfIndex_Type()
)
ipMcastInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastInterfaceIfIndex.setStatus("current")


class _IpMcastInterfaceTtl_Type(Unsigned32):
    """Custom type ipMcastInterfaceTtl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpMcastInterfaceTtl_Type.__name__ = "Unsigned32"
_IpMcastInterfaceTtl_Object = MibTableColumn
ipMcastInterfaceTtl = _IpMcastInterfaceTtl_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 3, 1, 3),
    _IpMcastInterfaceTtl_Type()
)
ipMcastInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMcastInterfaceTtl.setStatus("current")


class _IpMcastInterfaceRateLimit_Type(Unsigned32):
    """Custom type ipMcastInterfaceRateLimit based on Unsigned32"""
    defaultValue = 0


_IpMcastInterfaceRateLimit_Object = MibTableColumn
ipMcastInterfaceRateLimit = _IpMcastInterfaceRateLimit_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 3, 1, 4),
    _IpMcastInterfaceRateLimit_Type()
)
ipMcastInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMcastInterfaceRateLimit.setStatus("current")


class _IpMcastInterfaceStorageType_Type(StorageType):
    """Custom type ipMcastInterfaceStorageType based on StorageType"""


_IpMcastInterfaceStorageType_Object = MibTableColumn
ipMcastInterfaceStorageType = _IpMcastInterfaceStorageType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 3, 1, 5),
    _IpMcastInterfaceStorageType_Type()
)
ipMcastInterfaceStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMcastInterfaceStorageType.setStatus("current")
_IpMcastSsmRangeTable_Object = MibTable
ipMcastSsmRangeTable = _IpMcastSsmRangeTable_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 4)
)
if mibBuilder.loadTexts:
    ipMcastSsmRangeTable.setStatus("current")
_IpMcastSsmRangeEntry_Object = MibTableRow
ipMcastSsmRangeEntry = _IpMcastSsmRangeEntry_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 4, 1)
)
ipMcastSsmRangeEntry.setIndexNames(
    (0, "IPMCAST-MIB", "ipMcastSsmRangeAddressType"),
    (0, "IPMCAST-MIB", "ipMcastSsmRangeAddress"),
    (0, "IPMCAST-MIB", "ipMcastSsmRangePrefixLength"),
)
if mibBuilder.loadTexts:
    ipMcastSsmRangeEntry.setStatus("current")
_IpMcastSsmRangeAddressType_Type = InetAddressType
_IpMcastSsmRangeAddressType_Object = MibTableColumn
ipMcastSsmRangeAddressType = _IpMcastSsmRangeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 4, 1, 1),
    _IpMcastSsmRangeAddressType_Type()
)
ipMcastSsmRangeAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastSsmRangeAddressType.setStatus("current")
_IpMcastSsmRangeAddress_Type = InetAddress
_IpMcastSsmRangeAddress_Object = MibTableColumn
ipMcastSsmRangeAddress = _IpMcastSsmRangeAddress_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 4, 1, 2),
    _IpMcastSsmRangeAddress_Type()
)
ipMcastSsmRangeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastSsmRangeAddress.setStatus("current")
_IpMcastSsmRangePrefixLength_Type = InetAddressPrefixLength
_IpMcastSsmRangePrefixLength_Object = MibTableColumn
ipMcastSsmRangePrefixLength = _IpMcastSsmRangePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 4, 1, 3),
    _IpMcastSsmRangePrefixLength_Type()
)
ipMcastSsmRangePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastSsmRangePrefixLength.setStatus("current")
_IpMcastSsmRangeRowStatus_Type = RowStatus
_IpMcastSsmRangeRowStatus_Object = MibTableColumn
ipMcastSsmRangeRowStatus = _IpMcastSsmRangeRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 4, 1, 4),
    _IpMcastSsmRangeRowStatus_Type()
)
ipMcastSsmRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMcastSsmRangeRowStatus.setStatus("current")


class _IpMcastSsmRangeStorageType_Type(StorageType):
    """Custom type ipMcastSsmRangeStorageType based on StorageType"""


_IpMcastSsmRangeStorageType_Object = MibTableColumn
ipMcastSsmRangeStorageType = _IpMcastSsmRangeStorageType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 4, 1, 5),
    _IpMcastSsmRangeStorageType_Type()
)
ipMcastSsmRangeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMcastSsmRangeStorageType.setStatus("current")
_IpMcastRouteTable_Object = MibTable
ipMcastRouteTable = _IpMcastRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5)
)
if mibBuilder.loadTexts:
    ipMcastRouteTable.setStatus("current")
_IpMcastRouteEntry_Object = MibTableRow
ipMcastRouteEntry = _IpMcastRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1)
)
ipMcastRouteEntry.setIndexNames(
    (0, "IPMCAST-MIB", "ipMcastRouteGroupAddressType"),
    (0, "IPMCAST-MIB", "ipMcastRouteGroup"),
    (0, "IPMCAST-MIB", "ipMcastRouteGroupPrefixLength"),
    (0, "IPMCAST-MIB", "ipMcastRouteSourceAddressType"),
    (0, "IPMCAST-MIB", "ipMcastRouteSource"),
    (0, "IPMCAST-MIB", "ipMcastRouteSourcePrefixLength"),
)
if mibBuilder.loadTexts:
    ipMcastRouteEntry.setStatus("current")
_IpMcastRouteGroupAddressType_Type = InetAddressType
_IpMcastRouteGroupAddressType_Object = MibTableColumn
ipMcastRouteGroupAddressType = _IpMcastRouteGroupAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 1),
    _IpMcastRouteGroupAddressType_Type()
)
ipMcastRouteGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteGroupAddressType.setStatus("current")
_IpMcastRouteGroup_Type = InetAddress
_IpMcastRouteGroup_Object = MibTableColumn
ipMcastRouteGroup = _IpMcastRouteGroup_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 2),
    _IpMcastRouteGroup_Type()
)
ipMcastRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteGroup.setStatus("current")
_IpMcastRouteGroupPrefixLength_Type = InetAddressPrefixLength
_IpMcastRouteGroupPrefixLength_Object = MibTableColumn
ipMcastRouteGroupPrefixLength = _IpMcastRouteGroupPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 3),
    _IpMcastRouteGroupPrefixLength_Type()
)
ipMcastRouteGroupPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteGroupPrefixLength.setStatus("current")
_IpMcastRouteSourceAddressType_Type = InetAddressType
_IpMcastRouteSourceAddressType_Object = MibTableColumn
ipMcastRouteSourceAddressType = _IpMcastRouteSourceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 4),
    _IpMcastRouteSourceAddressType_Type()
)
ipMcastRouteSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteSourceAddressType.setStatus("current")
_IpMcastRouteSource_Type = InetAddress
_IpMcastRouteSource_Object = MibTableColumn
ipMcastRouteSource = _IpMcastRouteSource_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 5),
    _IpMcastRouteSource_Type()
)
ipMcastRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteSource.setStatus("current")
_IpMcastRouteSourcePrefixLength_Type = InetAddressPrefixLength
_IpMcastRouteSourcePrefixLength_Object = MibTableColumn
ipMcastRouteSourcePrefixLength = _IpMcastRouteSourcePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 6),
    _IpMcastRouteSourcePrefixLength_Type()
)
ipMcastRouteSourcePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteSourcePrefixLength.setStatus("current")
_IpMcastRouteUpstreamNeighborType_Type = InetAddressType
_IpMcastRouteUpstreamNeighborType_Object = MibTableColumn
ipMcastRouteUpstreamNeighborType = _IpMcastRouteUpstreamNeighborType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 7),
    _IpMcastRouteUpstreamNeighborType_Type()
)
ipMcastRouteUpstreamNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteUpstreamNeighborType.setStatus("current")
_IpMcastRouteUpstreamNeighbor_Type = InetAddress
_IpMcastRouteUpstreamNeighbor_Object = MibTableColumn
ipMcastRouteUpstreamNeighbor = _IpMcastRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 8),
    _IpMcastRouteUpstreamNeighbor_Type()
)
ipMcastRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteUpstreamNeighbor.setStatus("current")
_IpMcastRouteInIfIndex_Type = InterfaceIndexOrZero
_IpMcastRouteInIfIndex_Object = MibTableColumn
ipMcastRouteInIfIndex = _IpMcastRouteInIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 9),
    _IpMcastRouteInIfIndex_Type()
)
ipMcastRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteInIfIndex.setStatus("current")
_IpMcastRouteTimeStamp_Type = TimeStamp
_IpMcastRouteTimeStamp_Object = MibTableColumn
ipMcastRouteTimeStamp = _IpMcastRouteTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 10),
    _IpMcastRouteTimeStamp_Type()
)
ipMcastRouteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteTimeStamp.setStatus("current")
_IpMcastRouteExpiryTime_Type = TimeTicks
_IpMcastRouteExpiryTime_Object = MibTableColumn
ipMcastRouteExpiryTime = _IpMcastRouteExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 11),
    _IpMcastRouteExpiryTime_Type()
)
ipMcastRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteExpiryTime.setStatus("current")
_IpMcastRouteProtocol_Type = IANAipMRouteProtocol
_IpMcastRouteProtocol_Object = MibTableColumn
ipMcastRouteProtocol = _IpMcastRouteProtocol_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 12),
    _IpMcastRouteProtocol_Type()
)
ipMcastRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteProtocol.setStatus("current")
_IpMcastRouteRtProtocol_Type = IANAipRouteProtocol
_IpMcastRouteRtProtocol_Object = MibTableColumn
ipMcastRouteRtProtocol = _IpMcastRouteRtProtocol_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 13),
    _IpMcastRouteRtProtocol_Type()
)
ipMcastRouteRtProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteRtProtocol.setStatus("current")
_IpMcastRouteRtAddressType_Type = InetAddressType
_IpMcastRouteRtAddressType_Object = MibTableColumn
ipMcastRouteRtAddressType = _IpMcastRouteRtAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 14),
    _IpMcastRouteRtAddressType_Type()
)
ipMcastRouteRtAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteRtAddressType.setStatus("current")
_IpMcastRouteRtAddress_Type = InetAddress
_IpMcastRouteRtAddress_Object = MibTableColumn
ipMcastRouteRtAddress = _IpMcastRouteRtAddress_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 15),
    _IpMcastRouteRtAddress_Type()
)
ipMcastRouteRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteRtAddress.setStatus("current")
_IpMcastRouteRtPrefixLength_Type = InetAddressPrefixLength
_IpMcastRouteRtPrefixLength_Object = MibTableColumn
ipMcastRouteRtPrefixLength = _IpMcastRouteRtPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 16),
    _IpMcastRouteRtPrefixLength_Type()
)
ipMcastRouteRtPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteRtPrefixLength.setStatus("current")


class _IpMcastRouteRtType_Type(Integer32):
    """Custom type ipMcastRouteRtType based on Integer32"""
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


_IpMcastRouteRtType_Type.__name__ = "Integer32"
_IpMcastRouteRtType_Object = MibTableColumn
ipMcastRouteRtType = _IpMcastRouteRtType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 17),
    _IpMcastRouteRtType_Type()
)
ipMcastRouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteRtType.setStatus("current")
_IpMcastRouteOctets_Type = Counter64
_IpMcastRouteOctets_Object = MibTableColumn
ipMcastRouteOctets = _IpMcastRouteOctets_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 18),
    _IpMcastRouteOctets_Type()
)
ipMcastRouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteOctets.setStatus("current")
_IpMcastRoutePkts_Type = Counter64
_IpMcastRoutePkts_Object = MibTableColumn
ipMcastRoutePkts = _IpMcastRoutePkts_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 19),
    _IpMcastRoutePkts_Type()
)
ipMcastRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRoutePkts.setStatus("current")
_IpMcastRouteTtlDropOctets_Type = Counter64
_IpMcastRouteTtlDropOctets_Object = MibTableColumn
ipMcastRouteTtlDropOctets = _IpMcastRouteTtlDropOctets_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 20),
    _IpMcastRouteTtlDropOctets_Type()
)
ipMcastRouteTtlDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteTtlDropOctets.setStatus("current")
_IpMcastRouteTtlDropPackets_Type = Counter64
_IpMcastRouteTtlDropPackets_Object = MibTableColumn
ipMcastRouteTtlDropPackets = _IpMcastRouteTtlDropPackets_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 21),
    _IpMcastRouteTtlDropPackets_Type()
)
ipMcastRouteTtlDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteTtlDropPackets.setStatus("current")
_IpMcastRouteDifferentInIfOctets_Type = Counter64
_IpMcastRouteDifferentInIfOctets_Object = MibTableColumn
ipMcastRouteDifferentInIfOctets = _IpMcastRouteDifferentInIfOctets_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 22),
    _IpMcastRouteDifferentInIfOctets_Type()
)
ipMcastRouteDifferentInIfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteDifferentInIfOctets.setStatus("current")
_IpMcastRouteDifferentInIfPackets_Type = Counter64
_IpMcastRouteDifferentInIfPackets_Object = MibTableColumn
ipMcastRouteDifferentInIfPackets = _IpMcastRouteDifferentInIfPackets_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 23),
    _IpMcastRouteDifferentInIfPackets_Type()
)
ipMcastRouteDifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteDifferentInIfPackets.setStatus("current")
_IpMcastRouteBps_Type = CounterBasedGauge64
_IpMcastRouteBps_Object = MibTableColumn
ipMcastRouteBps = _IpMcastRouteBps_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 5, 1, 24),
    _IpMcastRouteBps_Type()
)
ipMcastRouteBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteBps.setStatus("current")
if mibBuilder.loadTexts:
    ipMcastRouteBps.setUnits("bits per second")
_IpMcastRouteNextHopTable_Object = MibTable
ipMcastRouteNextHopTable = _IpMcastRouteNextHopTable_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6)
)
if mibBuilder.loadTexts:
    ipMcastRouteNextHopTable.setStatus("current")
_IpMcastRouteNextHopEntry_Object = MibTableRow
ipMcastRouteNextHopEntry = _IpMcastRouteNextHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1)
)
ipMcastRouteNextHopEntry.setIndexNames(
    (0, "IPMCAST-MIB", "ipMcastRouteNextHopGroupAddressType"),
    (0, "IPMCAST-MIB", "ipMcastRouteNextHopGroup"),
    (0, "IPMCAST-MIB", "ipMcastRouteNextHopGroupPrefixLength"),
    (0, "IPMCAST-MIB", "ipMcastRouteNextHopSourceAddressType"),
    (0, "IPMCAST-MIB", "ipMcastRouteNextHopSource"),
    (0, "IPMCAST-MIB", "ipMcastRouteNextHopSourcePrefixLength"),
    (0, "IPMCAST-MIB", "ipMcastRouteNextHopIfIndex"),
    (0, "IPMCAST-MIB", "ipMcastRouteNextHopAddressType"),
    (0, "IPMCAST-MIB", "ipMcastRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    ipMcastRouteNextHopEntry.setStatus("current")
_IpMcastRouteNextHopGroupAddressType_Type = InetAddressType
_IpMcastRouteNextHopGroupAddressType_Object = MibTableColumn
ipMcastRouteNextHopGroupAddressType = _IpMcastRouteNextHopGroupAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 1),
    _IpMcastRouteNextHopGroupAddressType_Type()
)
ipMcastRouteNextHopGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopGroupAddressType.setStatus("current")
_IpMcastRouteNextHopGroup_Type = InetAddress
_IpMcastRouteNextHopGroup_Object = MibTableColumn
ipMcastRouteNextHopGroup = _IpMcastRouteNextHopGroup_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 2),
    _IpMcastRouteNextHopGroup_Type()
)
ipMcastRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopGroup.setStatus("current")
_IpMcastRouteNextHopGroupPrefixLength_Type = InetAddressPrefixLength
_IpMcastRouteNextHopGroupPrefixLength_Object = MibTableColumn
ipMcastRouteNextHopGroupPrefixLength = _IpMcastRouteNextHopGroupPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 3),
    _IpMcastRouteNextHopGroupPrefixLength_Type()
)
ipMcastRouteNextHopGroupPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopGroupPrefixLength.setStatus("current")
_IpMcastRouteNextHopSourceAddressType_Type = InetAddressType
_IpMcastRouteNextHopSourceAddressType_Object = MibTableColumn
ipMcastRouteNextHopSourceAddressType = _IpMcastRouteNextHopSourceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 4),
    _IpMcastRouteNextHopSourceAddressType_Type()
)
ipMcastRouteNextHopSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopSourceAddressType.setStatus("current")
_IpMcastRouteNextHopSource_Type = InetAddress
_IpMcastRouteNextHopSource_Object = MibTableColumn
ipMcastRouteNextHopSource = _IpMcastRouteNextHopSource_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 5),
    _IpMcastRouteNextHopSource_Type()
)
ipMcastRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopSource.setStatus("current")
_IpMcastRouteNextHopSourcePrefixLength_Type = InetAddressPrefixLength
_IpMcastRouteNextHopSourcePrefixLength_Object = MibTableColumn
ipMcastRouteNextHopSourcePrefixLength = _IpMcastRouteNextHopSourcePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 6),
    _IpMcastRouteNextHopSourcePrefixLength_Type()
)
ipMcastRouteNextHopSourcePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopSourcePrefixLength.setStatus("current")
_IpMcastRouteNextHopIfIndex_Type = InterfaceIndex
_IpMcastRouteNextHopIfIndex_Object = MibTableColumn
ipMcastRouteNextHopIfIndex = _IpMcastRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 7),
    _IpMcastRouteNextHopIfIndex_Type()
)
ipMcastRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopIfIndex.setStatus("current")
_IpMcastRouteNextHopAddressType_Type = InetAddressType
_IpMcastRouteNextHopAddressType_Object = MibTableColumn
ipMcastRouteNextHopAddressType = _IpMcastRouteNextHopAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 8),
    _IpMcastRouteNextHopAddressType_Type()
)
ipMcastRouteNextHopAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopAddressType.setStatus("current")
_IpMcastRouteNextHopAddress_Type = InetAddress
_IpMcastRouteNextHopAddress_Object = MibTableColumn
ipMcastRouteNextHopAddress = _IpMcastRouteNextHopAddress_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 9),
    _IpMcastRouteNextHopAddress_Type()
)
ipMcastRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopAddress.setStatus("current")


class _IpMcastRouteNextHopState_Type(Integer32):
    """Custom type ipMcastRouteNextHopState based on Integer32"""
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


_IpMcastRouteNextHopState_Type.__name__ = "Integer32"
_IpMcastRouteNextHopState_Object = MibTableColumn
ipMcastRouteNextHopState = _IpMcastRouteNextHopState_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 10),
    _IpMcastRouteNextHopState_Type()
)
ipMcastRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopState.setStatus("current")
_IpMcastRouteNextHopTimeStamp_Type = TimeStamp
_IpMcastRouteNextHopTimeStamp_Object = MibTableColumn
ipMcastRouteNextHopTimeStamp = _IpMcastRouteNextHopTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 11),
    _IpMcastRouteNextHopTimeStamp_Type()
)
ipMcastRouteNextHopTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopTimeStamp.setStatus("current")
_IpMcastRouteNextHopExpiryTime_Type = TimeTicks
_IpMcastRouteNextHopExpiryTime_Object = MibTableColumn
ipMcastRouteNextHopExpiryTime = _IpMcastRouteNextHopExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 12),
    _IpMcastRouteNextHopExpiryTime_Type()
)
ipMcastRouteNextHopExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopExpiryTime.setStatus("current")


class _IpMcastRouteNextHopClosestMemberHops_Type(Unsigned32):
    """Custom type ipMcastRouteNextHopClosestMemberHops based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpMcastRouteNextHopClosestMemberHops_Type.__name__ = "Unsigned32"
_IpMcastRouteNextHopClosestMemberHops_Object = MibTableColumn
ipMcastRouteNextHopClosestMemberHops = _IpMcastRouteNextHopClosestMemberHops_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 13),
    _IpMcastRouteNextHopClosestMemberHops_Type()
)
ipMcastRouteNextHopClosestMemberHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopClosestMemberHops.setStatus("current")
_IpMcastRouteNextHopProtocol_Type = IANAipMRouteProtocol
_IpMcastRouteNextHopProtocol_Object = MibTableColumn
ipMcastRouteNextHopProtocol = _IpMcastRouteNextHopProtocol_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 14),
    _IpMcastRouteNextHopProtocol_Type()
)
ipMcastRouteNextHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopProtocol.setStatus("current")
_IpMcastRouteNextHopOctets_Type = Counter64
_IpMcastRouteNextHopOctets_Object = MibTableColumn
ipMcastRouteNextHopOctets = _IpMcastRouteNextHopOctets_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 15),
    _IpMcastRouteNextHopOctets_Type()
)
ipMcastRouteNextHopOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopOctets.setStatus("current")
_IpMcastRouteNextHopPkts_Type = Counter64
_IpMcastRouteNextHopPkts_Object = MibTableColumn
ipMcastRouteNextHopPkts = _IpMcastRouteNextHopPkts_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 6, 1, 16),
    _IpMcastRouteNextHopPkts_Type()
)
ipMcastRouteNextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastRouteNextHopPkts.setStatus("current")
_IpMcastBoundaryTable_Object = MibTable
ipMcastBoundaryTable = _IpMcastBoundaryTable_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7)
)
if mibBuilder.loadTexts:
    ipMcastBoundaryTable.setStatus("current")
_IpMcastBoundaryEntry_Object = MibTableRow
ipMcastBoundaryEntry = _IpMcastBoundaryEntry_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7, 1)
)
ipMcastBoundaryEntry.setIndexNames(
    (0, "IPMCAST-MIB", "ipMcastBoundaryIfIndex"),
    (0, "IPMCAST-MIB", "ipMcastBoundaryAddressType"),
    (0, "IPMCAST-MIB", "ipMcastBoundaryAddress"),
    (0, "IPMCAST-MIB", "ipMcastBoundaryAddressPrefixLength"),
)
if mibBuilder.loadTexts:
    ipMcastBoundaryEntry.setStatus("current")
_IpMcastBoundaryIfIndex_Type = InterfaceIndex
_IpMcastBoundaryIfIndex_Object = MibTableColumn
ipMcastBoundaryIfIndex = _IpMcastBoundaryIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7, 1, 1),
    _IpMcastBoundaryIfIndex_Type()
)
ipMcastBoundaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastBoundaryIfIndex.setStatus("current")
_IpMcastBoundaryAddressType_Type = InetAddressType
_IpMcastBoundaryAddressType_Object = MibTableColumn
ipMcastBoundaryAddressType = _IpMcastBoundaryAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7, 1, 2),
    _IpMcastBoundaryAddressType_Type()
)
ipMcastBoundaryAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastBoundaryAddressType.setStatus("current")
_IpMcastBoundaryAddress_Type = InetAddress
_IpMcastBoundaryAddress_Object = MibTableColumn
ipMcastBoundaryAddress = _IpMcastBoundaryAddress_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7, 1, 3),
    _IpMcastBoundaryAddress_Type()
)
ipMcastBoundaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastBoundaryAddress.setStatus("current")
_IpMcastBoundaryAddressPrefixLength_Type = InetAddressPrefixLength
_IpMcastBoundaryAddressPrefixLength_Object = MibTableColumn
ipMcastBoundaryAddressPrefixLength = _IpMcastBoundaryAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7, 1, 4),
    _IpMcastBoundaryAddressPrefixLength_Type()
)
ipMcastBoundaryAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastBoundaryAddressPrefixLength.setStatus("current")
_IpMcastBoundaryTimeStamp_Type = TimeStamp
_IpMcastBoundaryTimeStamp_Object = MibTableColumn
ipMcastBoundaryTimeStamp = _IpMcastBoundaryTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7, 1, 5),
    _IpMcastBoundaryTimeStamp_Type()
)
ipMcastBoundaryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastBoundaryTimeStamp.setStatus("current")
_IpMcastBoundaryDroppedMcastOctets_Type = Counter64
_IpMcastBoundaryDroppedMcastOctets_Object = MibTableColumn
ipMcastBoundaryDroppedMcastOctets = _IpMcastBoundaryDroppedMcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7, 1, 6),
    _IpMcastBoundaryDroppedMcastOctets_Type()
)
ipMcastBoundaryDroppedMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastBoundaryDroppedMcastOctets.setStatus("current")
_IpMcastBoundaryDroppedMcastPkts_Type = Counter64
_IpMcastBoundaryDroppedMcastPkts_Object = MibTableColumn
ipMcastBoundaryDroppedMcastPkts = _IpMcastBoundaryDroppedMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7, 1, 7),
    _IpMcastBoundaryDroppedMcastPkts_Type()
)
ipMcastBoundaryDroppedMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastBoundaryDroppedMcastPkts.setStatus("current")
_IpMcastBoundaryStatus_Type = RowStatus
_IpMcastBoundaryStatus_Object = MibTableColumn
ipMcastBoundaryStatus = _IpMcastBoundaryStatus_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7, 1, 8),
    _IpMcastBoundaryStatus_Type()
)
ipMcastBoundaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMcastBoundaryStatus.setStatus("current")


class _IpMcastBoundaryStorageType_Type(StorageType):
    """Custom type ipMcastBoundaryStorageType based on StorageType"""


_IpMcastBoundaryStorageType_Object = MibTableColumn
ipMcastBoundaryStorageType = _IpMcastBoundaryStorageType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 7, 1, 9),
    _IpMcastBoundaryStorageType_Type()
)
ipMcastBoundaryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMcastBoundaryStorageType.setStatus("current")
_IpMcastScopeNameTable_Object = MibTable
ipMcastScopeNameTable = _IpMcastScopeNameTable_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 8)
)
if mibBuilder.loadTexts:
    ipMcastScopeNameTable.setStatus("current")
_IpMcastScopeNameEntry_Object = MibTableRow
ipMcastScopeNameEntry = _IpMcastScopeNameEntry_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 8, 1)
)
ipMcastScopeNameEntry.setIndexNames(
    (0, "IPMCAST-MIB", "ipMcastScopeNameAddressType"),
    (0, "IPMCAST-MIB", "ipMcastScopeNameAddress"),
    (0, "IPMCAST-MIB", "ipMcastScopeNameAddressPrefixLength"),
    (0, "IPMCAST-MIB", "ipMcastScopeNameLanguage"),
)
if mibBuilder.loadTexts:
    ipMcastScopeNameEntry.setStatus("current")
_IpMcastScopeNameAddressType_Type = InetAddressType
_IpMcastScopeNameAddressType_Object = MibTableColumn
ipMcastScopeNameAddressType = _IpMcastScopeNameAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 8, 1, 1),
    _IpMcastScopeNameAddressType_Type()
)
ipMcastScopeNameAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastScopeNameAddressType.setStatus("current")
_IpMcastScopeNameAddress_Type = InetAddress
_IpMcastScopeNameAddress_Object = MibTableColumn
ipMcastScopeNameAddress = _IpMcastScopeNameAddress_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 8, 1, 2),
    _IpMcastScopeNameAddress_Type()
)
ipMcastScopeNameAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastScopeNameAddress.setStatus("current")
_IpMcastScopeNameAddressPrefixLength_Type = InetAddressPrefixLength
_IpMcastScopeNameAddressPrefixLength_Object = MibTableColumn
ipMcastScopeNameAddressPrefixLength = _IpMcastScopeNameAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 8, 1, 3),
    _IpMcastScopeNameAddressPrefixLength_Type()
)
ipMcastScopeNameAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastScopeNameAddressPrefixLength.setStatus("current")
_IpMcastScopeNameLanguage_Type = LangTag
_IpMcastScopeNameLanguage_Object = MibTableColumn
ipMcastScopeNameLanguage = _IpMcastScopeNameLanguage_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 8, 1, 4),
    _IpMcastScopeNameLanguage_Type()
)
ipMcastScopeNameLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastScopeNameLanguage.setStatus("current")
_IpMcastScopeNameString_Type = SnmpAdminString
_IpMcastScopeNameString_Object = MibTableColumn
ipMcastScopeNameString = _IpMcastScopeNameString_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 8, 1, 5),
    _IpMcastScopeNameString_Type()
)
ipMcastScopeNameString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMcastScopeNameString.setStatus("current")


class _IpMcastScopeNameDefault_Type(TruthValue):
    """Custom type ipMcastScopeNameDefault based on TruthValue"""


_IpMcastScopeNameDefault_Object = MibTableColumn
ipMcastScopeNameDefault = _IpMcastScopeNameDefault_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 8, 1, 6),
    _IpMcastScopeNameDefault_Type()
)
ipMcastScopeNameDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMcastScopeNameDefault.setStatus("current")
_IpMcastScopeNameStatus_Type = RowStatus
_IpMcastScopeNameStatus_Object = MibTableColumn
ipMcastScopeNameStatus = _IpMcastScopeNameStatus_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 8, 1, 7),
    _IpMcastScopeNameStatus_Type()
)
ipMcastScopeNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMcastScopeNameStatus.setStatus("current")


class _IpMcastScopeNameStorageType_Type(StorageType):
    """Custom type ipMcastScopeNameStorageType based on StorageType"""


_IpMcastScopeNameStorageType_Object = MibTableColumn
ipMcastScopeNameStorageType = _IpMcastScopeNameStorageType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 8, 1, 8),
    _IpMcastScopeNameStorageType_Type()
)
ipMcastScopeNameStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipMcastScopeNameStorageType.setStatus("current")
_IpMcastLocalListenerTable_Object = MibTable
ipMcastLocalListenerTable = _IpMcastLocalListenerTable_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 9)
)
if mibBuilder.loadTexts:
    ipMcastLocalListenerTable.setStatus("current")
_IpMcastLocalListenerEntry_Object = MibTableRow
ipMcastLocalListenerEntry = _IpMcastLocalListenerEntry_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 9, 1)
)
ipMcastLocalListenerEntry.setIndexNames(
    (0, "IPMCAST-MIB", "ipMcastLocalListenerGroupAddressType"),
    (0, "IPMCAST-MIB", "ipMcastLocalListenerGroupAddress"),
    (0, "IPMCAST-MIB", "ipMcastLocalListenerSourceAddressType"),
    (0, "IPMCAST-MIB", "ipMcastLocalListenerSourceAddress"),
    (0, "IPMCAST-MIB", "ipMcastLocalListenerSourcePrefixLength"),
    (0, "IPMCAST-MIB", "ipMcastLocalListenerIfIndex"),
    (0, "IPMCAST-MIB", "ipMcastLocalListenerRunIndex"),
)
if mibBuilder.loadTexts:
    ipMcastLocalListenerEntry.setStatus("current")
_IpMcastLocalListenerGroupAddressType_Type = InetAddressType
_IpMcastLocalListenerGroupAddressType_Object = MibTableColumn
ipMcastLocalListenerGroupAddressType = _IpMcastLocalListenerGroupAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 9, 1, 1),
    _IpMcastLocalListenerGroupAddressType_Type()
)
ipMcastLocalListenerGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastLocalListenerGroupAddressType.setStatus("current")
_IpMcastLocalListenerGroupAddress_Type = InetAddress
_IpMcastLocalListenerGroupAddress_Object = MibTableColumn
ipMcastLocalListenerGroupAddress = _IpMcastLocalListenerGroupAddress_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 9, 1, 2),
    _IpMcastLocalListenerGroupAddress_Type()
)
ipMcastLocalListenerGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastLocalListenerGroupAddress.setStatus("current")
_IpMcastLocalListenerSourceAddressType_Type = InetAddressType
_IpMcastLocalListenerSourceAddressType_Object = MibTableColumn
ipMcastLocalListenerSourceAddressType = _IpMcastLocalListenerSourceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 9, 1, 3),
    _IpMcastLocalListenerSourceAddressType_Type()
)
ipMcastLocalListenerSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastLocalListenerSourceAddressType.setStatus("current")
_IpMcastLocalListenerSourceAddress_Type = InetAddress
_IpMcastLocalListenerSourceAddress_Object = MibTableColumn
ipMcastLocalListenerSourceAddress = _IpMcastLocalListenerSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 9, 1, 4),
    _IpMcastLocalListenerSourceAddress_Type()
)
ipMcastLocalListenerSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastLocalListenerSourceAddress.setStatus("current")
_IpMcastLocalListenerSourcePrefixLength_Type = InetAddressPrefixLength
_IpMcastLocalListenerSourcePrefixLength_Object = MibTableColumn
ipMcastLocalListenerSourcePrefixLength = _IpMcastLocalListenerSourcePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 9, 1, 5),
    _IpMcastLocalListenerSourcePrefixLength_Type()
)
ipMcastLocalListenerSourcePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastLocalListenerSourcePrefixLength.setStatus("current")
_IpMcastLocalListenerIfIndex_Type = InterfaceIndex
_IpMcastLocalListenerIfIndex_Object = MibTableColumn
ipMcastLocalListenerIfIndex = _IpMcastLocalListenerIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 9, 1, 6),
    _IpMcastLocalListenerIfIndex_Type()
)
ipMcastLocalListenerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastLocalListenerIfIndex.setStatus("current")


class _IpMcastLocalListenerRunIndex_Type(Unsigned32):
    """Custom type ipMcastLocalListenerRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpMcastLocalListenerRunIndex_Type.__name__ = "Unsigned32"
_IpMcastLocalListenerRunIndex_Object = MibTableColumn
ipMcastLocalListenerRunIndex = _IpMcastLocalListenerRunIndex_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 9, 1, 7),
    _IpMcastLocalListenerRunIndex_Type()
)
ipMcastLocalListenerRunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastLocalListenerRunIndex.setStatus("current")
_IpMcastZoneTable_Object = MibTable
ipMcastZoneTable = _IpMcastZoneTable_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 10)
)
if mibBuilder.loadTexts:
    ipMcastZoneTable.setStatus("current")
_IpMcastZoneEntry_Object = MibTableRow
ipMcastZoneEntry = _IpMcastZoneEntry_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 10, 1)
)
ipMcastZoneEntry.setIndexNames(
    (0, "IPMCAST-MIB", "ipMcastZoneIndex"),
)
if mibBuilder.loadTexts:
    ipMcastZoneEntry.setStatus("current")


class _IpMcastZoneIndex_Type(InetZoneIndex):
    """Custom type ipMcastZoneIndex based on InetZoneIndex"""
    subtypeSpec = InetZoneIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpMcastZoneIndex_Type.__name__ = "InetZoneIndex"
_IpMcastZoneIndex_Object = MibTableColumn
ipMcastZoneIndex = _IpMcastZoneIndex_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 10, 1, 1),
    _IpMcastZoneIndex_Type()
)
ipMcastZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMcastZoneIndex.setStatus("current")


class _IpMcastZoneScopeDefaultZoneIndex_Type(InetZoneIndex):
    """Custom type ipMcastZoneScopeDefaultZoneIndex based on InetZoneIndex"""
    subtypeSpec = InetZoneIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpMcastZoneScopeDefaultZoneIndex_Type.__name__ = "InetZoneIndex"
_IpMcastZoneScopeDefaultZoneIndex_Object = MibTableColumn
ipMcastZoneScopeDefaultZoneIndex = _IpMcastZoneScopeDefaultZoneIndex_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 10, 1, 2),
    _IpMcastZoneScopeDefaultZoneIndex_Type()
)
ipMcastZoneScopeDefaultZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastZoneScopeDefaultZoneIndex.setStatus("current")
_IpMcastZoneScopeAddressType_Type = InetAddressType
_IpMcastZoneScopeAddressType_Object = MibTableColumn
ipMcastZoneScopeAddressType = _IpMcastZoneScopeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 10, 1, 3),
    _IpMcastZoneScopeAddressType_Type()
)
ipMcastZoneScopeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastZoneScopeAddressType.setStatus("current")
_IpMcastZoneScopeAddress_Type = InetAddress
_IpMcastZoneScopeAddress_Object = MibTableColumn
ipMcastZoneScopeAddress = _IpMcastZoneScopeAddress_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 10, 1, 4),
    _IpMcastZoneScopeAddress_Type()
)
ipMcastZoneScopeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastZoneScopeAddress.setStatus("current")
_IpMcastZoneScopeAddressPrefixLength_Type = InetAddressPrefixLength
_IpMcastZoneScopeAddressPrefixLength_Object = MibTableColumn
ipMcastZoneScopeAddressPrefixLength = _IpMcastZoneScopeAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 10, 1, 5),
    _IpMcastZoneScopeAddressPrefixLength_Type()
)
ipMcastZoneScopeAddressPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMcastZoneScopeAddressPrefixLength.setStatus("current")


class _IpMcastDeviceConfigStorageType_Type(StorageType):
    """Custom type ipMcastDeviceConfigStorageType based on StorageType"""


_IpMcastDeviceConfigStorageType_Object = MibScalar
ipMcastDeviceConfigStorageType = _IpMcastDeviceConfigStorageType_Object(
    (1, 3, 6, 1, 2, 1, 168, 1, 11),
    _IpMcastDeviceConfigStorageType_Type()
)
ipMcastDeviceConfigStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMcastDeviceConfigStorageType.setStatus("current")
_IpMcastMIBConformance_ObjectIdentity = ObjectIdentity
ipMcastMIBConformance = _IpMcastMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 168, 2)
)
_IpMcastMIBCompliances_ObjectIdentity = ObjectIdentity
ipMcastMIBCompliances = _IpMcastMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 168, 2, 1)
)
_IpMcastMIBGroups_ObjectIdentity = ObjectIdentity
ipMcastMIBGroups = _IpMcastMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 168, 2, 2)
)

# Managed Objects groups

ipMcastMIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 1)
)
ipMcastMIBBasicGroup.setObjects(
      *(("IPMCAST-MIB", "ipMcastEnabled"),
        ("IPMCAST-MIB", "ipMcastRouteEntryCount"),
        ("IPMCAST-MIB", "ipMcastDeviceConfigStorageType"))
)
if mibBuilder.loadTexts:
    ipMcastMIBBasicGroup.setStatus("current")

ipMcastMIBSsmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 2)
)
ipMcastMIBSsmGroup.setObjects(
      *(("IPMCAST-MIB", "ipMcastSsmRangeRowStatus"),
        ("IPMCAST-MIB", "ipMcastSsmRangeStorageType"))
)
if mibBuilder.loadTexts:
    ipMcastMIBSsmGroup.setStatus("current")

ipMcastMIBRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 3)
)
ipMcastMIBRouteGroup.setObjects(
      *(("IPMCAST-MIB", "ipMcastInterfaceTtl"),
        ("IPMCAST-MIB", "ipMcastInterfaceRateLimit"),
        ("IPMCAST-MIB", "ipMcastInterfaceStorageType"),
        ("IPMCAST-MIB", "ipMcastRouteUpstreamNeighborType"),
        ("IPMCAST-MIB", "ipMcastRouteUpstreamNeighbor"),
        ("IPMCAST-MIB", "ipMcastRouteInIfIndex"),
        ("IPMCAST-MIB", "ipMcastRouteTimeStamp"),
        ("IPMCAST-MIB", "ipMcastRouteExpiryTime"),
        ("IPMCAST-MIB", "ipMcastRouteNextHopState"),
        ("IPMCAST-MIB", "ipMcastRouteNextHopTimeStamp"),
        ("IPMCAST-MIB", "ipMcastRouteNextHopExpiryTime"))
)
if mibBuilder.loadTexts:
    ipMcastMIBRouteGroup.setStatus("current")

ipMcastMIBRouteDiagnosticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 4)
)
ipMcastMIBRouteDiagnosticsGroup.setObjects(
      *(("IPMCAST-MIB", "ipMcastRoutePkts"),
        ("IPMCAST-MIB", "ipMcastRouteTtlDropPackets"),
        ("IPMCAST-MIB", "ipMcastRouteDifferentInIfPackets"))
)
if mibBuilder.loadTexts:
    ipMcastMIBRouteDiagnosticsGroup.setStatus("current")

ipMcastMIBPktsOutGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 5)
)
ipMcastMIBPktsOutGroup.setObjects(
      *(("IPMCAST-MIB", "ipMcastRouteNextHopTimeStamp"),
        ("IPMCAST-MIB", "ipMcastRouteNextHopPkts"))
)
if mibBuilder.loadTexts:
    ipMcastMIBPktsOutGroup.setStatus("current")

ipMcastMIBHopCountGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 6)
)
ipMcastMIBHopCountGroup.setObjects(
    ("IPMCAST-MIB", "ipMcastRouteNextHopClosestMemberHops")
)
if mibBuilder.loadTexts:
    ipMcastMIBHopCountGroup.setStatus("current")

ipMcastMIBRouteOctetsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 7)
)
ipMcastMIBRouteOctetsGroup.setObjects(
      *(("IPMCAST-MIB", "ipMcastRouteTimeStamp"),
        ("IPMCAST-MIB", "ipMcastRouteOctets"),
        ("IPMCAST-MIB", "ipMcastRouteTtlDropOctets"),
        ("IPMCAST-MIB", "ipMcastRouteDifferentInIfOctets"),
        ("IPMCAST-MIB", "ipMcastRouteNextHopTimeStamp"),
        ("IPMCAST-MIB", "ipMcastRouteNextHopOctets"))
)
if mibBuilder.loadTexts:
    ipMcastMIBRouteOctetsGroup.setStatus("current")

ipMcastMIBRouteBpsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 8)
)
ipMcastMIBRouteBpsGroup.setObjects(
    ("IPMCAST-MIB", "ipMcastRouteBps")
)
if mibBuilder.loadTexts:
    ipMcastMIBRouteBpsGroup.setStatus("current")

ipMcastMIBRouteProtoGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 9)
)
ipMcastMIBRouteProtoGroup.setObjects(
      *(("IPMCAST-MIB", "ipMcastRouteProtocol"),
        ("IPMCAST-MIB", "ipMcastRouteRtProtocol"),
        ("IPMCAST-MIB", "ipMcastRouteRtAddressType"),
        ("IPMCAST-MIB", "ipMcastRouteRtAddress"),
        ("IPMCAST-MIB", "ipMcastRouteRtPrefixLength"),
        ("IPMCAST-MIB", "ipMcastRouteRtType"),
        ("IPMCAST-MIB", "ipMcastRouteNextHopProtocol"))
)
if mibBuilder.loadTexts:
    ipMcastMIBRouteProtoGroup.setStatus("current")

ipMcastMIBLocalListenerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 10)
)
ipMcastMIBLocalListenerGroup.setObjects(
    ("IPMCAST-MIB", "ipMcastLocalListenerRunIndex")
)
if mibBuilder.loadTexts:
    ipMcastMIBLocalListenerGroup.setStatus("current")

ipMcastMIBBoundaryIfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 11)
)
ipMcastMIBBoundaryIfGroup.setObjects(
      *(("IPMCAST-MIB", "ipMcastBoundaryTimeStamp"),
        ("IPMCAST-MIB", "ipMcastBoundaryDroppedMcastOctets"),
        ("IPMCAST-MIB", "ipMcastBoundaryDroppedMcastPkts"),
        ("IPMCAST-MIB", "ipMcastBoundaryStatus"),
        ("IPMCAST-MIB", "ipMcastBoundaryStorageType"),
        ("IPMCAST-MIB", "ipMcastZoneScopeDefaultZoneIndex"),
        ("IPMCAST-MIB", "ipMcastZoneScopeAddressType"),
        ("IPMCAST-MIB", "ipMcastZoneScopeAddress"),
        ("IPMCAST-MIB", "ipMcastZoneScopeAddressPrefixLength"))
)
if mibBuilder.loadTexts:
    ipMcastMIBBoundaryIfGroup.setStatus("current")

ipMcastMIBScopeNameGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 168, 2, 2, 12)
)
ipMcastMIBScopeNameGroup.setObjects(
      *(("IPMCAST-MIB", "ipMcastScopeNameString"),
        ("IPMCAST-MIB", "ipMcastScopeNameDefault"),
        ("IPMCAST-MIB", "ipMcastScopeNameStatus"),
        ("IPMCAST-MIB", "ipMcastScopeNameStorageType"))
)
if mibBuilder.loadTexts:
    ipMcastMIBScopeNameGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipMcastMIBComplianceHost = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 168, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipMcastMIBComplianceHost.setStatus(
        "current"
    )

ipMcastMIBComplianceRouter = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 168, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ipMcastMIBComplianceRouter.setStatus(
        "current"
    )

ipMcastMIBComplianceBorderRouter = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 168, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ipMcastMIBComplianceBorderRouter.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPMCAST-MIB",
    **{"ipMcastMIB": ipMcastMIB,
       "ipMcast": ipMcast,
       "ipMcastEnabled": ipMcastEnabled,
       "ipMcastRouteEntryCount": ipMcastRouteEntryCount,
       "ipMcastInterfaceTable": ipMcastInterfaceTable,
       "ipMcastInterfaceEntry": ipMcastInterfaceEntry,
       "ipMcastInterfaceIPVersion": ipMcastInterfaceIPVersion,
       "ipMcastInterfaceIfIndex": ipMcastInterfaceIfIndex,
       "ipMcastInterfaceTtl": ipMcastInterfaceTtl,
       "ipMcastInterfaceRateLimit": ipMcastInterfaceRateLimit,
       "ipMcastInterfaceStorageType": ipMcastInterfaceStorageType,
       "ipMcastSsmRangeTable": ipMcastSsmRangeTable,
       "ipMcastSsmRangeEntry": ipMcastSsmRangeEntry,
       "ipMcastSsmRangeAddressType": ipMcastSsmRangeAddressType,
       "ipMcastSsmRangeAddress": ipMcastSsmRangeAddress,
       "ipMcastSsmRangePrefixLength": ipMcastSsmRangePrefixLength,
       "ipMcastSsmRangeRowStatus": ipMcastSsmRangeRowStatus,
       "ipMcastSsmRangeStorageType": ipMcastSsmRangeStorageType,
       "ipMcastRouteTable": ipMcastRouteTable,
       "ipMcastRouteEntry": ipMcastRouteEntry,
       "ipMcastRouteGroupAddressType": ipMcastRouteGroupAddressType,
       "ipMcastRouteGroup": ipMcastRouteGroup,
       "ipMcastRouteGroupPrefixLength": ipMcastRouteGroupPrefixLength,
       "ipMcastRouteSourceAddressType": ipMcastRouteSourceAddressType,
       "ipMcastRouteSource": ipMcastRouteSource,
       "ipMcastRouteSourcePrefixLength": ipMcastRouteSourcePrefixLength,
       "ipMcastRouteUpstreamNeighborType": ipMcastRouteUpstreamNeighborType,
       "ipMcastRouteUpstreamNeighbor": ipMcastRouteUpstreamNeighbor,
       "ipMcastRouteInIfIndex": ipMcastRouteInIfIndex,
       "ipMcastRouteTimeStamp": ipMcastRouteTimeStamp,
       "ipMcastRouteExpiryTime": ipMcastRouteExpiryTime,
       "ipMcastRouteProtocol": ipMcastRouteProtocol,
       "ipMcastRouteRtProtocol": ipMcastRouteRtProtocol,
       "ipMcastRouteRtAddressType": ipMcastRouteRtAddressType,
       "ipMcastRouteRtAddress": ipMcastRouteRtAddress,
       "ipMcastRouteRtPrefixLength": ipMcastRouteRtPrefixLength,
       "ipMcastRouteRtType": ipMcastRouteRtType,
       "ipMcastRouteOctets": ipMcastRouteOctets,
       "ipMcastRoutePkts": ipMcastRoutePkts,
       "ipMcastRouteTtlDropOctets": ipMcastRouteTtlDropOctets,
       "ipMcastRouteTtlDropPackets": ipMcastRouteTtlDropPackets,
       "ipMcastRouteDifferentInIfOctets": ipMcastRouteDifferentInIfOctets,
       "ipMcastRouteDifferentInIfPackets": ipMcastRouteDifferentInIfPackets,
       "ipMcastRouteBps": ipMcastRouteBps,
       "ipMcastRouteNextHopTable": ipMcastRouteNextHopTable,
       "ipMcastRouteNextHopEntry": ipMcastRouteNextHopEntry,
       "ipMcastRouteNextHopGroupAddressType": ipMcastRouteNextHopGroupAddressType,
       "ipMcastRouteNextHopGroup": ipMcastRouteNextHopGroup,
       "ipMcastRouteNextHopGroupPrefixLength": ipMcastRouteNextHopGroupPrefixLength,
       "ipMcastRouteNextHopSourceAddressType": ipMcastRouteNextHopSourceAddressType,
       "ipMcastRouteNextHopSource": ipMcastRouteNextHopSource,
       "ipMcastRouteNextHopSourcePrefixLength": ipMcastRouteNextHopSourcePrefixLength,
       "ipMcastRouteNextHopIfIndex": ipMcastRouteNextHopIfIndex,
       "ipMcastRouteNextHopAddressType": ipMcastRouteNextHopAddressType,
       "ipMcastRouteNextHopAddress": ipMcastRouteNextHopAddress,
       "ipMcastRouteNextHopState": ipMcastRouteNextHopState,
       "ipMcastRouteNextHopTimeStamp": ipMcastRouteNextHopTimeStamp,
       "ipMcastRouteNextHopExpiryTime": ipMcastRouteNextHopExpiryTime,
       "ipMcastRouteNextHopClosestMemberHops": ipMcastRouteNextHopClosestMemberHops,
       "ipMcastRouteNextHopProtocol": ipMcastRouteNextHopProtocol,
       "ipMcastRouteNextHopOctets": ipMcastRouteNextHopOctets,
       "ipMcastRouteNextHopPkts": ipMcastRouteNextHopPkts,
       "ipMcastBoundaryTable": ipMcastBoundaryTable,
       "ipMcastBoundaryEntry": ipMcastBoundaryEntry,
       "ipMcastBoundaryIfIndex": ipMcastBoundaryIfIndex,
       "ipMcastBoundaryAddressType": ipMcastBoundaryAddressType,
       "ipMcastBoundaryAddress": ipMcastBoundaryAddress,
       "ipMcastBoundaryAddressPrefixLength": ipMcastBoundaryAddressPrefixLength,
       "ipMcastBoundaryTimeStamp": ipMcastBoundaryTimeStamp,
       "ipMcastBoundaryDroppedMcastOctets": ipMcastBoundaryDroppedMcastOctets,
       "ipMcastBoundaryDroppedMcastPkts": ipMcastBoundaryDroppedMcastPkts,
       "ipMcastBoundaryStatus": ipMcastBoundaryStatus,
       "ipMcastBoundaryStorageType": ipMcastBoundaryStorageType,
       "ipMcastScopeNameTable": ipMcastScopeNameTable,
       "ipMcastScopeNameEntry": ipMcastScopeNameEntry,
       "ipMcastScopeNameAddressType": ipMcastScopeNameAddressType,
       "ipMcastScopeNameAddress": ipMcastScopeNameAddress,
       "ipMcastScopeNameAddressPrefixLength": ipMcastScopeNameAddressPrefixLength,
       "ipMcastScopeNameLanguage": ipMcastScopeNameLanguage,
       "ipMcastScopeNameString": ipMcastScopeNameString,
       "ipMcastScopeNameDefault": ipMcastScopeNameDefault,
       "ipMcastScopeNameStatus": ipMcastScopeNameStatus,
       "ipMcastScopeNameStorageType": ipMcastScopeNameStorageType,
       "ipMcastLocalListenerTable": ipMcastLocalListenerTable,
       "ipMcastLocalListenerEntry": ipMcastLocalListenerEntry,
       "ipMcastLocalListenerGroupAddressType": ipMcastLocalListenerGroupAddressType,
       "ipMcastLocalListenerGroupAddress": ipMcastLocalListenerGroupAddress,
       "ipMcastLocalListenerSourceAddressType": ipMcastLocalListenerSourceAddressType,
       "ipMcastLocalListenerSourceAddress": ipMcastLocalListenerSourceAddress,
       "ipMcastLocalListenerSourcePrefixLength": ipMcastLocalListenerSourcePrefixLength,
       "ipMcastLocalListenerIfIndex": ipMcastLocalListenerIfIndex,
       "ipMcastLocalListenerRunIndex": ipMcastLocalListenerRunIndex,
       "ipMcastZoneTable": ipMcastZoneTable,
       "ipMcastZoneEntry": ipMcastZoneEntry,
       "ipMcastZoneIndex": ipMcastZoneIndex,
       "ipMcastZoneScopeDefaultZoneIndex": ipMcastZoneScopeDefaultZoneIndex,
       "ipMcastZoneScopeAddressType": ipMcastZoneScopeAddressType,
       "ipMcastZoneScopeAddress": ipMcastZoneScopeAddress,
       "ipMcastZoneScopeAddressPrefixLength": ipMcastZoneScopeAddressPrefixLength,
       "ipMcastDeviceConfigStorageType": ipMcastDeviceConfigStorageType,
       "ipMcastMIBConformance": ipMcastMIBConformance,
       "ipMcastMIBCompliances": ipMcastMIBCompliances,
       "ipMcastMIBComplianceHost": ipMcastMIBComplianceHost,
       "ipMcastMIBComplianceRouter": ipMcastMIBComplianceRouter,
       "ipMcastMIBComplianceBorderRouter": ipMcastMIBComplianceBorderRouter,
       "ipMcastMIBGroups": ipMcastMIBGroups,
       "ipMcastMIBBasicGroup": ipMcastMIBBasicGroup,
       "ipMcastMIBSsmGroup": ipMcastMIBSsmGroup,
       "ipMcastMIBRouteGroup": ipMcastMIBRouteGroup,
       "ipMcastMIBRouteDiagnosticsGroup": ipMcastMIBRouteDiagnosticsGroup,
       "ipMcastMIBPktsOutGroup": ipMcastMIBPktsOutGroup,
       "ipMcastMIBHopCountGroup": ipMcastMIBHopCountGroup,
       "ipMcastMIBRouteOctetsGroup": ipMcastMIBRouteOctetsGroup,
       "ipMcastMIBRouteBpsGroup": ipMcastMIBRouteBpsGroup,
       "ipMcastMIBRouteProtoGroup": ipMcastMIBRouteProtoGroup,
       "ipMcastMIBLocalListenerGroup": ipMcastMIBLocalListenerGroup,
       "ipMcastMIBBoundaryIfGroup": ipMcastMIBBoundaryIfGroup,
       "ipMcastMIBScopeNameGroup": ipMcastMIBScopeNameGroup}
)
