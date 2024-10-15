# SNMP MIB module (HUAWEI-IPMCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-IPMCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:08 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

hwIpMcastMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1)
)
hwIpMcastMib.setRevisions(
        ("2014-07-01 00:00",
         "2014-06-20 00:00",
         "2013-08-28 00:00",
         "2007-04-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWChannelMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asm", 2),
          ("ssm", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwMcast_ObjectIdentity = ObjectIdentity
hwMcast = _HwMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149)
)
_HwIpMcastMibObjects_ObjectIdentity = ObjectIdentity
hwIpMcastMibObjects = _HwIpMcastMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1)
)
_HwIpMcast_ObjectIdentity = ObjectIdentity
hwIpMcast = _HwIpMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1)
)
_HwIpMcastEnable_Type = EnabledStatus
_HwIpMcastEnable_Object = MibScalar
hwIpMcastEnable = _HwIpMcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 1),
    _HwIpMcastEnable_Type()
)
hwIpMcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpMcastEnable.setStatus("current")
_HwIpMcastRouteEntryCount_Type = Gauge32
_HwIpMcastRouteEntryCount_Object = MibScalar
hwIpMcastRouteEntryCount = _HwIpMcastRouteEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 2),
    _HwIpMcastRouteEntryCount_Type()
)
hwIpMcastRouteEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteEntryCount.setStatus("current")
_HwIpMcastInterfaceTable_Object = MibTable
hwIpMcastInterfaceTable = _HwIpMcastInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwIpMcastInterfaceTable.setStatus("current")
_HwIpMcastInterfaceEntry_Object = MibTableRow
hwIpMcastInterfaceEntry = _HwIpMcastInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3, 1)
)
hwIpMcastInterfaceEntry.setIndexNames(
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastInterfaceIpVersion"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hwIpMcastInterfaceEntry.setStatus("current")
_HwIpMcastInterfaceIpVersion_Type = InetVersion
_HwIpMcastInterfaceIpVersion_Object = MibTableColumn
hwIpMcastInterfaceIpVersion = _HwIpMcastInterfaceIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3, 1, 1),
    _HwIpMcastInterfaceIpVersion_Type()
)
hwIpMcastInterfaceIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastInterfaceIpVersion.setStatus("current")
_HwIpMcastInterfaceIfIndex_Type = InterfaceIndex
_HwIpMcastInterfaceIfIndex_Object = MibTableColumn
hwIpMcastInterfaceIfIndex = _HwIpMcastInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3, 1, 2),
    _HwIpMcastInterfaceIfIndex_Type()
)
hwIpMcastInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastInterfaceIfIndex.setStatus("current")


class _HwIpMcastInterfaceTtl_Type(Unsigned32):
    """Custom type hwIpMcastInterfaceTtl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIpMcastInterfaceTtl_Type.__name__ = "Unsigned32"
_HwIpMcastInterfaceTtl_Object = MibTableColumn
hwIpMcastInterfaceTtl = _HwIpMcastInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3, 1, 3),
    _HwIpMcastInterfaceTtl_Type()
)
hwIpMcastInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpMcastInterfaceTtl.setStatus("current")


class _HwIpMcastInterfaceRateLimit_Type(Unsigned32):
    """Custom type hwIpMcastInterfaceRateLimit based on Unsigned32"""
    defaultValue = 0


_HwIpMcastInterfaceRateLimit_Object = MibTableColumn
hwIpMcastInterfaceRateLimit = _HwIpMcastInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3, 1, 4),
    _HwIpMcastInterfaceRateLimit_Type()
)
hwIpMcastInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpMcastInterfaceRateLimit.setStatus("current")
_HwIpMcastInterfaceInMcastOctets_Type = Counter64
_HwIpMcastInterfaceInMcastOctets_Object = MibTableColumn
hwIpMcastInterfaceInMcastOctets = _HwIpMcastInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3, 1, 5),
    _HwIpMcastInterfaceInMcastOctets_Type()
)
hwIpMcastInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastInterfaceInMcastOctets.setStatus("current")
_HwIpMcastInterfaceOutMcastOctets_Type = Counter64
_HwIpMcastInterfaceOutMcastOctets_Object = MibTableColumn
hwIpMcastInterfaceOutMcastOctets = _HwIpMcastInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3, 1, 6),
    _HwIpMcastInterfaceOutMcastOctets_Type()
)
hwIpMcastInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastInterfaceOutMcastOctets.setStatus("current")
_HwIpMcastInterfaceInMcastPkts_Type = Counter64
_HwIpMcastInterfaceInMcastPkts_Object = MibTableColumn
hwIpMcastInterfaceInMcastPkts = _HwIpMcastInterfaceInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3, 1, 7),
    _HwIpMcastInterfaceInMcastPkts_Type()
)
hwIpMcastInterfaceInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastInterfaceInMcastPkts.setStatus("current")
_HwIpMcastInterfaceOutMcastPkts_Type = Counter64
_HwIpMcastInterfaceOutMcastPkts_Object = MibTableColumn
hwIpMcastInterfaceOutMcastPkts = _HwIpMcastInterfaceOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3, 1, 8),
    _HwIpMcastInterfaceOutMcastPkts_Type()
)
hwIpMcastInterfaceOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastInterfaceOutMcastPkts.setStatus("current")
_HwIpMcastInterfaceDiscontinuityTime_Type = TimeStamp
_HwIpMcastInterfaceDiscontinuityTime_Object = MibTableColumn
hwIpMcastInterfaceDiscontinuityTime = _HwIpMcastInterfaceDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 3, 1, 9),
    _HwIpMcastInterfaceDiscontinuityTime_Type()
)
hwIpMcastInterfaceDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastInterfaceDiscontinuityTime.setStatus("current")
_HwIpMcastRouteTable_Object = MibTable
hwIpMcastRouteTable = _HwIpMcastRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwIpMcastRouteTable.setStatus("current")
_HwIpMcastRouteEntry_Object = MibTableRow
hwIpMcastRouteEntry = _HwIpMcastRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1)
)
hwIpMcastRouteEntry.setIndexNames(
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteGroupAddressType"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteGroup"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteGroupPrefixLength"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteSourceAddressType"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteSource"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteSourcePrefixLength"),
)
if mibBuilder.loadTexts:
    hwIpMcastRouteEntry.setStatus("current")
_HwIpMcastRouteGroupAddressType_Type = InetAddressType
_HwIpMcastRouteGroupAddressType_Object = MibTableColumn
hwIpMcastRouteGroupAddressType = _HwIpMcastRouteGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 1),
    _HwIpMcastRouteGroupAddressType_Type()
)
hwIpMcastRouteGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteGroupAddressType.setStatus("current")


class _HwIpMcastRouteGroup_Type(InetAddress):
    """Custom type hwIpMcastRouteGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwIpMcastRouteGroup_Type.__name__ = "InetAddress"
_HwIpMcastRouteGroup_Object = MibTableColumn
hwIpMcastRouteGroup = _HwIpMcastRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 2),
    _HwIpMcastRouteGroup_Type()
)
hwIpMcastRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteGroup.setStatus("current")


class _HwIpMcastRouteGroupPrefixLength_Type(InetAddressPrefixLength):
    """Custom type hwIpMcastRouteGroupPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_HwIpMcastRouteGroupPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_HwIpMcastRouteGroupPrefixLength_Object = MibTableColumn
hwIpMcastRouteGroupPrefixLength = _HwIpMcastRouteGroupPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 3),
    _HwIpMcastRouteGroupPrefixLength_Type()
)
hwIpMcastRouteGroupPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteGroupPrefixLength.setStatus("current")
_HwIpMcastRouteSourceAddressType_Type = InetAddressType
_HwIpMcastRouteSourceAddressType_Object = MibTableColumn
hwIpMcastRouteSourceAddressType = _HwIpMcastRouteSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 4),
    _HwIpMcastRouteSourceAddressType_Type()
)
hwIpMcastRouteSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteSourceAddressType.setStatus("current")


class _HwIpMcastRouteSource_Type(InetAddress):
    """Custom type hwIpMcastRouteSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwIpMcastRouteSource_Type.__name__ = "InetAddress"
_HwIpMcastRouteSource_Object = MibTableColumn
hwIpMcastRouteSource = _HwIpMcastRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 5),
    _HwIpMcastRouteSource_Type()
)
hwIpMcastRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteSource.setStatus("current")


class _HwIpMcastRouteSourcePrefixLength_Type(InetAddressPrefixLength):
    """Custom type hwIpMcastRouteSourcePrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_HwIpMcastRouteSourcePrefixLength_Type.__name__ = "InetAddressPrefixLength"
_HwIpMcastRouteSourcePrefixLength_Object = MibTableColumn
hwIpMcastRouteSourcePrefixLength = _HwIpMcastRouteSourcePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 6),
    _HwIpMcastRouteSourcePrefixLength_Type()
)
hwIpMcastRouteSourcePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteSourcePrefixLength.setStatus("current")
_HwIpMcastRouteUpstreamNeighborType_Type = InetAddressType
_HwIpMcastRouteUpstreamNeighborType_Object = MibTableColumn
hwIpMcastRouteUpstreamNeighborType = _HwIpMcastRouteUpstreamNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 7),
    _HwIpMcastRouteUpstreamNeighborType_Type()
)
hwIpMcastRouteUpstreamNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteUpstreamNeighborType.setStatus("current")


class _HwIpMcastRouteUpstreamNeighbor_Type(InetAddress):
    """Custom type hwIpMcastRouteUpstreamNeighbor based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwIpMcastRouteUpstreamNeighbor_Type.__name__ = "InetAddress"
_HwIpMcastRouteUpstreamNeighbor_Object = MibTableColumn
hwIpMcastRouteUpstreamNeighbor = _HwIpMcastRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 8),
    _HwIpMcastRouteUpstreamNeighbor_Type()
)
hwIpMcastRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteUpstreamNeighbor.setStatus("current")
_HwIpMcastRouteInIfIndex_Type = InterfaceIndexOrZero
_HwIpMcastRouteInIfIndex_Object = MibTableColumn
hwIpMcastRouteInIfIndex = _HwIpMcastRouteInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 9),
    _HwIpMcastRouteInIfIndex_Type()
)
hwIpMcastRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteInIfIndex.setStatus("current")
_HwIpMcastRouteTimeStamp_Type = TimeStamp
_HwIpMcastRouteTimeStamp_Object = MibTableColumn
hwIpMcastRouteTimeStamp = _HwIpMcastRouteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 10),
    _HwIpMcastRouteTimeStamp_Type()
)
hwIpMcastRouteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteTimeStamp.setStatus("current")
_HwIpMcastRouteExpiryTime_Type = TimeTicks
_HwIpMcastRouteExpiryTime_Object = MibTableColumn
hwIpMcastRouteExpiryTime = _HwIpMcastRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 11),
    _HwIpMcastRouteExpiryTime_Type()
)
hwIpMcastRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteExpiryTime.setStatus("current")
_HwIpMcastRouteProtocol_Type = IANAipMRouteProtocol
_HwIpMcastRouteProtocol_Object = MibTableColumn
hwIpMcastRouteProtocol = _HwIpMcastRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 12),
    _HwIpMcastRouteProtocol_Type()
)
hwIpMcastRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteProtocol.setStatus("current")
_HwIpMcastRouteRtProtocol_Type = IANAipRouteProtocol
_HwIpMcastRouteRtProtocol_Object = MibTableColumn
hwIpMcastRouteRtProtocol = _HwIpMcastRouteRtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 13),
    _HwIpMcastRouteRtProtocol_Type()
)
hwIpMcastRouteRtProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteRtProtocol.setStatus("current")
_HwIpMcastRouteRtAddressType_Type = InetAddressType
_HwIpMcastRouteRtAddressType_Object = MibTableColumn
hwIpMcastRouteRtAddressType = _HwIpMcastRouteRtAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 14),
    _HwIpMcastRouteRtAddressType_Type()
)
hwIpMcastRouteRtAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteRtAddressType.setStatus("current")


class _HwIpMcastRouteRtAddress_Type(InetAddress):
    """Custom type hwIpMcastRouteRtAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwIpMcastRouteRtAddress_Type.__name__ = "InetAddress"
_HwIpMcastRouteRtAddress_Object = MibTableColumn
hwIpMcastRouteRtAddress = _HwIpMcastRouteRtAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 15),
    _HwIpMcastRouteRtAddress_Type()
)
hwIpMcastRouteRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteRtAddress.setStatus("current")


class _HwIpMcastRouteRtPrefixLength_Type(InetAddressPrefixLength):
    """Custom type hwIpMcastRouteRtPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_HwIpMcastRouteRtPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_HwIpMcastRouteRtPrefixLength_Object = MibTableColumn
hwIpMcastRouteRtPrefixLength = _HwIpMcastRouteRtPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 16),
    _HwIpMcastRouteRtPrefixLength_Type()
)
hwIpMcastRouteRtPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteRtPrefixLength.setStatus("current")


class _HwIpMcastRouteRtType_Type(Integer32):
    """Custom type hwIpMcastRouteRtType based on Integer32"""
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


_HwIpMcastRouteRtType_Type.__name__ = "Integer32"
_HwIpMcastRouteRtType_Object = MibTableColumn
hwIpMcastRouteRtType = _HwIpMcastRouteRtType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 17),
    _HwIpMcastRouteRtType_Type()
)
hwIpMcastRouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteRtType.setStatus("current")
_HwIpMcastRouteOctets_Type = Counter64
_HwIpMcastRouteOctets_Object = MibTableColumn
hwIpMcastRouteOctets = _HwIpMcastRouteOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 18),
    _HwIpMcastRouteOctets_Type()
)
hwIpMcastRouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteOctets.setStatus("current")
_HwIpMcastRoutePkts_Type = Counter64
_HwIpMcastRoutePkts_Object = MibTableColumn
hwIpMcastRoutePkts = _HwIpMcastRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 19),
    _HwIpMcastRoutePkts_Type()
)
hwIpMcastRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRoutePkts.setStatus("current")
_HwIpMcastRouteTtlDropOctets_Type = Counter64
_HwIpMcastRouteTtlDropOctets_Object = MibTableColumn
hwIpMcastRouteTtlDropOctets = _HwIpMcastRouteTtlDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 20),
    _HwIpMcastRouteTtlDropOctets_Type()
)
hwIpMcastRouteTtlDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteTtlDropOctets.setStatus("current")
_HwIpMcastRouteTtlDropPackets_Type = Counter64
_HwIpMcastRouteTtlDropPackets_Object = MibTableColumn
hwIpMcastRouteTtlDropPackets = _HwIpMcastRouteTtlDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 21),
    _HwIpMcastRouteTtlDropPackets_Type()
)
hwIpMcastRouteTtlDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteTtlDropPackets.setStatus("current")
_HwIpMcastRouteDifferentInIfOctets_Type = Counter64
_HwIpMcastRouteDifferentInIfOctets_Object = MibTableColumn
hwIpMcastRouteDifferentInIfOctets = _HwIpMcastRouteDifferentInIfOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 22),
    _HwIpMcastRouteDifferentInIfOctets_Type()
)
hwIpMcastRouteDifferentInIfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteDifferentInIfOctets.setStatus("current")
_HwIpMcastRouteDifferentInIfPackets_Type = Counter64
_HwIpMcastRouteDifferentInIfPackets_Object = MibTableColumn
hwIpMcastRouteDifferentInIfPackets = _HwIpMcastRouteDifferentInIfPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 5, 1, 23),
    _HwIpMcastRouteDifferentInIfPackets_Type()
)
hwIpMcastRouteDifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteDifferentInIfPackets.setStatus("current")
_HwIpMcastRouteNextHopTable_Object = MibTable
hwIpMcastRouteNextHopTable = _HwIpMcastRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopTable.setStatus("current")
_HwIpMcastRouteNextHopEntry_Object = MibTableRow
hwIpMcastRouteNextHopEntry = _HwIpMcastRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1)
)
hwIpMcastRouteNextHopEntry.setIndexNames(
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopGroupAddressType"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopGroup"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopGroupPrefixLength"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopSourceAddressType"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopSource"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopSourcePrefixLength"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopIfIndex"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopAddressType"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopEntry.setStatus("current")
_HwIpMcastRouteNextHopGroupAddressType_Type = InetAddressType
_HwIpMcastRouteNextHopGroupAddressType_Object = MibTableColumn
hwIpMcastRouteNextHopGroupAddressType = _HwIpMcastRouteNextHopGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 1),
    _HwIpMcastRouteNextHopGroupAddressType_Type()
)
hwIpMcastRouteNextHopGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopGroupAddressType.setStatus("current")


class _HwIpMcastRouteNextHopGroup_Type(InetAddress):
    """Custom type hwIpMcastRouteNextHopGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwIpMcastRouteNextHopGroup_Type.__name__ = "InetAddress"
_HwIpMcastRouteNextHopGroup_Object = MibTableColumn
hwIpMcastRouteNextHopGroup = _HwIpMcastRouteNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 2),
    _HwIpMcastRouteNextHopGroup_Type()
)
hwIpMcastRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopGroup.setStatus("current")


class _HwIpMcastRouteNextHopGroupPrefixLength_Type(InetAddressPrefixLength):
    """Custom type hwIpMcastRouteNextHopGroupPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_HwIpMcastRouteNextHopGroupPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_HwIpMcastRouteNextHopGroupPrefixLength_Object = MibTableColumn
hwIpMcastRouteNextHopGroupPrefixLength = _HwIpMcastRouteNextHopGroupPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 3),
    _HwIpMcastRouteNextHopGroupPrefixLength_Type()
)
hwIpMcastRouteNextHopGroupPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopGroupPrefixLength.setStatus("current")
_HwIpMcastRouteNextHopSourceAddressType_Type = InetAddressType
_HwIpMcastRouteNextHopSourceAddressType_Object = MibTableColumn
hwIpMcastRouteNextHopSourceAddressType = _HwIpMcastRouteNextHopSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 4),
    _HwIpMcastRouteNextHopSourceAddressType_Type()
)
hwIpMcastRouteNextHopSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopSourceAddressType.setStatus("current")


class _HwIpMcastRouteNextHopSource_Type(InetAddress):
    """Custom type hwIpMcastRouteNextHopSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwIpMcastRouteNextHopSource_Type.__name__ = "InetAddress"
_HwIpMcastRouteNextHopSource_Object = MibTableColumn
hwIpMcastRouteNextHopSource = _HwIpMcastRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 5),
    _HwIpMcastRouteNextHopSource_Type()
)
hwIpMcastRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopSource.setStatus("current")


class _HwIpMcastRouteNextHopSourcePrefixLength_Type(InetAddressPrefixLength):
    """Custom type hwIpMcastRouteNextHopSourcePrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_HwIpMcastRouteNextHopSourcePrefixLength_Type.__name__ = "InetAddressPrefixLength"
_HwIpMcastRouteNextHopSourcePrefixLength_Object = MibTableColumn
hwIpMcastRouteNextHopSourcePrefixLength = _HwIpMcastRouteNextHopSourcePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 6),
    _HwIpMcastRouteNextHopSourcePrefixLength_Type()
)
hwIpMcastRouteNextHopSourcePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopSourcePrefixLength.setStatus("current")
_HwIpMcastRouteNextHopIfIndex_Type = InterfaceIndex
_HwIpMcastRouteNextHopIfIndex_Object = MibTableColumn
hwIpMcastRouteNextHopIfIndex = _HwIpMcastRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 7),
    _HwIpMcastRouteNextHopIfIndex_Type()
)
hwIpMcastRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopIfIndex.setStatus("current")
_HwIpMcastRouteNextHopAddressType_Type = InetAddressType
_HwIpMcastRouteNextHopAddressType_Object = MibTableColumn
hwIpMcastRouteNextHopAddressType = _HwIpMcastRouteNextHopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 8),
    _HwIpMcastRouteNextHopAddressType_Type()
)
hwIpMcastRouteNextHopAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopAddressType.setStatus("current")


class _HwIpMcastRouteNextHopAddress_Type(InetAddress):
    """Custom type hwIpMcastRouteNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwIpMcastRouteNextHopAddress_Type.__name__ = "InetAddress"
_HwIpMcastRouteNextHopAddress_Object = MibTableColumn
hwIpMcastRouteNextHopAddress = _HwIpMcastRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 9),
    _HwIpMcastRouteNextHopAddress_Type()
)
hwIpMcastRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopAddress.setStatus("current")


class _HwIpMcastRouteNextHopState_Type(Integer32):
    """Custom type hwIpMcastRouteNextHopState based on Integer32"""
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


_HwIpMcastRouteNextHopState_Type.__name__ = "Integer32"
_HwIpMcastRouteNextHopState_Object = MibTableColumn
hwIpMcastRouteNextHopState = _HwIpMcastRouteNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 10),
    _HwIpMcastRouteNextHopState_Type()
)
hwIpMcastRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopState.setStatus("current")
_HwIpMcastRouteNextHopTimeStamp_Type = TimeStamp
_HwIpMcastRouteNextHopTimeStamp_Object = MibTableColumn
hwIpMcastRouteNextHopTimeStamp = _HwIpMcastRouteNextHopTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 11),
    _HwIpMcastRouteNextHopTimeStamp_Type()
)
hwIpMcastRouteNextHopTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopTimeStamp.setStatus("current")
_HwIpMcastRouteNextHopExpiryTime_Type = TimeTicks
_HwIpMcastRouteNextHopExpiryTime_Object = MibTableColumn
hwIpMcastRouteNextHopExpiryTime = _HwIpMcastRouteNextHopExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 12),
    _HwIpMcastRouteNextHopExpiryTime_Type()
)
hwIpMcastRouteNextHopExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopExpiryTime.setStatus("current")


class _HwIpMcastRouteNextHopClosestMemberHops_Type(Unsigned32):
    """Custom type hwIpMcastRouteNextHopClosestMemberHops based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIpMcastRouteNextHopClosestMemberHops_Type.__name__ = "Unsigned32"
_HwIpMcastRouteNextHopClosestMemberHops_Object = MibTableColumn
hwIpMcastRouteNextHopClosestMemberHops = _HwIpMcastRouteNextHopClosestMemberHops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 13),
    _HwIpMcastRouteNextHopClosestMemberHops_Type()
)
hwIpMcastRouteNextHopClosestMemberHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopClosestMemberHops.setStatus("current")
_HwIpMcastRouteNextHopProtocol_Type = IANAipMRouteProtocol
_HwIpMcastRouteNextHopProtocol_Object = MibTableColumn
hwIpMcastRouteNextHopProtocol = _HwIpMcastRouteNextHopProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 14),
    _HwIpMcastRouteNextHopProtocol_Type()
)
hwIpMcastRouteNextHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopProtocol.setStatus("current")
_HwIpMcastRouteNextHopOctets_Type = Counter64
_HwIpMcastRouteNextHopOctets_Object = MibTableColumn
hwIpMcastRouteNextHopOctets = _HwIpMcastRouteNextHopOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 15),
    _HwIpMcastRouteNextHopOctets_Type()
)
hwIpMcastRouteNextHopOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopOctets.setStatus("current")
_HwIpMcastRouteNextHopPkts_Type = Counter64
_HwIpMcastRouteNextHopPkts_Object = MibTableColumn
hwIpMcastRouteNextHopPkts = _HwIpMcastRouteNextHopPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 6, 1, 16),
    _HwIpMcastRouteNextHopPkts_Type()
)
hwIpMcastRouteNextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastRouteNextHopPkts.setStatus("current")
_HwIpMcastBoundaryTable_Object = MibTable
hwIpMcastBoundaryTable = _HwIpMcastBoundaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwIpMcastBoundaryTable.setStatus("current")
_HwIpMcastBoundaryEntry_Object = MibTableRow
hwIpMcastBoundaryEntry = _HwIpMcastBoundaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7, 1)
)
hwIpMcastBoundaryEntry.setIndexNames(
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastBoundaryIfIndex"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastBoundaryAddressType"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastBoundaryAddress"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastBoundaryAddressPrefixLength"),
)
if mibBuilder.loadTexts:
    hwIpMcastBoundaryEntry.setStatus("current")
_HwIpMcastBoundaryIfIndex_Type = InterfaceIndex
_HwIpMcastBoundaryIfIndex_Object = MibTableColumn
hwIpMcastBoundaryIfIndex = _HwIpMcastBoundaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7, 1, 1),
    _HwIpMcastBoundaryIfIndex_Type()
)
hwIpMcastBoundaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastBoundaryIfIndex.setStatus("current")
_HwIpMcastBoundaryAddressType_Type = InetAddressType
_HwIpMcastBoundaryAddressType_Object = MibTableColumn
hwIpMcastBoundaryAddressType = _HwIpMcastBoundaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7, 1, 2),
    _HwIpMcastBoundaryAddressType_Type()
)
hwIpMcastBoundaryAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastBoundaryAddressType.setStatus("current")


class _HwIpMcastBoundaryAddress_Type(InetAddress):
    """Custom type hwIpMcastBoundaryAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwIpMcastBoundaryAddress_Type.__name__ = "InetAddress"
_HwIpMcastBoundaryAddress_Object = MibTableColumn
hwIpMcastBoundaryAddress = _HwIpMcastBoundaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7, 1, 3),
    _HwIpMcastBoundaryAddress_Type()
)
hwIpMcastBoundaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastBoundaryAddress.setStatus("current")


class _HwIpMcastBoundaryAddressPrefixLength_Type(InetAddressPrefixLength):
    """Custom type hwIpMcastBoundaryAddressPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_HwIpMcastBoundaryAddressPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_HwIpMcastBoundaryAddressPrefixLength_Object = MibTableColumn
hwIpMcastBoundaryAddressPrefixLength = _HwIpMcastBoundaryAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7, 1, 4),
    _HwIpMcastBoundaryAddressPrefixLength_Type()
)
hwIpMcastBoundaryAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastBoundaryAddressPrefixLength.setStatus("current")
_HwIpMcastBoundaryTimeStamp_Type = TimeStamp
_HwIpMcastBoundaryTimeStamp_Object = MibTableColumn
hwIpMcastBoundaryTimeStamp = _HwIpMcastBoundaryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7, 1, 5),
    _HwIpMcastBoundaryTimeStamp_Type()
)
hwIpMcastBoundaryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastBoundaryTimeStamp.setStatus("current")
_HwIpMcastBoundaryDroppedMcastOctets_Type = Counter64
_HwIpMcastBoundaryDroppedMcastOctets_Object = MibTableColumn
hwIpMcastBoundaryDroppedMcastOctets = _HwIpMcastBoundaryDroppedMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7, 1, 6),
    _HwIpMcastBoundaryDroppedMcastOctets_Type()
)
hwIpMcastBoundaryDroppedMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastBoundaryDroppedMcastOctets.setStatus("current")
_HwIpMcastBoundaryDroppedMcastPkts_Type = Counter64
_HwIpMcastBoundaryDroppedMcastPkts_Object = MibTableColumn
hwIpMcastBoundaryDroppedMcastPkts = _HwIpMcastBoundaryDroppedMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7, 1, 7),
    _HwIpMcastBoundaryDroppedMcastPkts_Type()
)
hwIpMcastBoundaryDroppedMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastBoundaryDroppedMcastPkts.setStatus("current")
_HwIpMcastBoundaryStatus_Type = RowStatus
_HwIpMcastBoundaryStatus_Object = MibTableColumn
hwIpMcastBoundaryStatus = _HwIpMcastBoundaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7, 1, 8),
    _HwIpMcastBoundaryStatus_Type()
)
hwIpMcastBoundaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpMcastBoundaryStatus.setStatus("current")


class _HwIpMcastBoundaryStorageType_Type(StorageType):
    """Custom type hwIpMcastBoundaryStorageType based on StorageType"""


_HwIpMcastBoundaryStorageType_Object = MibTableColumn
hwIpMcastBoundaryStorageType = _HwIpMcastBoundaryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 7, 1, 9),
    _HwIpMcastBoundaryStorageType_Type()
)
hwIpMcastBoundaryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpMcastBoundaryStorageType.setStatus("current")


class _HwIpMcastChannelName_Type(DisplayString):
    """Custom type hwIpMcastChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpMcastChannelName_Type.__name__ = "DisplayString"
_HwIpMcastChannelName_Object = MibScalar
hwIpMcastChannelName = _HwIpMcastChannelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 8),
    _HwIpMcastChannelName_Type()
)
hwIpMcastChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelName.setStatus("current")
_HwIpMcastChannelGroup_Type = IpAddress
_HwIpMcastChannelGroup_Object = MibScalar
hwIpMcastChannelGroup = _HwIpMcastChannelGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 9),
    _HwIpMcastChannelGroup_Type()
)
hwIpMcastChannelGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelGroup.setStatus("current")
_HwIpMcastChannelSource_Type = IpAddress
_HwIpMcastChannelSource_Object = MibScalar
hwIpMcastChannelSource = _HwIpMcastChannelSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 10),
    _HwIpMcastChannelSource_Type()
)
hwIpMcastChannelSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelSource.setStatus("current")


class _HwIpMcastChannelDownstreamEntries_Type(Unsigned32):
    """Custom type hwIpMcastChannelDownstreamEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpMcastChannelDownstreamEntries_Type.__name__ = "Unsigned32"
_HwIpMcastChannelDownstreamEntries_Object = MibScalar
hwIpMcastChannelDownstreamEntries = _HwIpMcastChannelDownstreamEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 11),
    _HwIpMcastChannelDownstreamEntries_Type()
)
hwIpMcastChannelDownstreamEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelDownstreamEntries.setStatus("current")


class _HwIpMcastChannelDownstreamBandWidth_Type(DisplayString):
    """Custom type hwIpMcastChannelDownstreamBandWidth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpMcastChannelDownstreamBandWidth_Type.__name__ = "DisplayString"
_HwIpMcastChannelDownstreamBandWidth_Object = MibScalar
hwIpMcastChannelDownstreamBandWidth = _HwIpMcastChannelDownstreamBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 12),
    _HwIpMcastChannelDownstreamBandWidth_Type()
)
hwIpMcastChannelDownstreamBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelDownstreamBandWidth.setStatus("current")


class _HwIpMcastChannelGlobalEntries_Type(Unsigned32):
    """Custom type hwIpMcastChannelGlobalEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpMcastChannelGlobalEntries_Type.__name__ = "Unsigned32"
_HwIpMcastChannelGlobalEntries_Object = MibScalar
hwIpMcastChannelGlobalEntries = _HwIpMcastChannelGlobalEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 13),
    _HwIpMcastChannelGlobalEntries_Type()
)
hwIpMcastChannelGlobalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelGlobalEntries.setStatus("current")


class _HwIpMcastChannelDownstreamLimitBandWidth_Type(DisplayString):
    """Custom type hwIpMcastChannelDownstreamLimitBandWidth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpMcastChannelDownstreamLimitBandWidth_Type.__name__ = "DisplayString"
_HwIpMcastChannelDownstreamLimitBandWidth_Object = MibScalar
hwIpMcastChannelDownstreamLimitBandWidth = _HwIpMcastChannelDownstreamLimitBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 14),
    _HwIpMcastChannelDownstreamLimitBandWidth_Type()
)
hwIpMcastChannelDownstreamLimitBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelDownstreamLimitBandWidth.setStatus("obsolete")


class _HwIpMcastChannelDownstreamLimitEntries_Type(Unsigned32):
    """Custom type hwIpMcastChannelDownstreamLimitEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpMcastChannelDownstreamLimitEntries_Type.__name__ = "Unsigned32"
_HwIpMcastChannelDownstreamLimitEntries_Object = MibScalar
hwIpMcastChannelDownstreamLimitEntries = _HwIpMcastChannelDownstreamLimitEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 15),
    _HwIpMcastChannelDownstreamLimitEntries_Type()
)
hwIpMcastChannelDownstreamLimitEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelDownstreamLimitEntries.setStatus("obsolete")


class _HwIpMcastChannelGlobalLimitEntries_Type(Unsigned32):
    """Custom type hwIpMcastChannelGlobalLimitEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpMcastChannelGlobalLimitEntries_Type.__name__ = "Unsigned32"
_HwIpMcastChannelGlobalLimitEntries_Object = MibScalar
hwIpMcastChannelGlobalLimitEntries = _HwIpMcastChannelGlobalLimitEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 16),
    _HwIpMcastChannelGlobalLimitEntries_Type()
)
hwIpMcastChannelGlobalLimitEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelGlobalLimitEntries.setStatus("obsolete")
_HwIpMcastChannelInterfaceIfIndex_Type = InterfaceIndexOrZero
_HwIpMcastChannelInterfaceIfIndex_Object = MibScalar
hwIpMcastChannelInterfaceIfIndex = _HwIpMcastChannelInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 17),
    _HwIpMcastChannelInterfaceIfIndex_Type()
)
hwIpMcastChannelInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelInterfaceIfIndex.setStatus("current")


class _HwIpMcastChannelInterfaceName_Type(DisplayString):
    """Custom type hwIpMcastChannelInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpMcastChannelInterfaceName_Type.__name__ = "DisplayString"
_HwIpMcastChannelInterfaceName_Object = MibScalar
hwIpMcastChannelInterfaceName = _HwIpMcastChannelInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 18),
    _HwIpMcastChannelInterfaceName_Type()
)
hwIpMcastChannelInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpMcastChannelInterfaceName.setStatus("current")


class _HwIpMcastCfgTotalLimit_Type(Unsigned32):
    """Custom type hwIpMcastCfgTotalLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIpMcastCfgTotalLimit_Type.__name__ = "Unsigned32"
_HwIpMcastCfgTotalLimit_Object = MibScalar
hwIpMcastCfgTotalLimit = _HwIpMcastCfgTotalLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 19),
    _HwIpMcastCfgTotalLimit_Type()
)
hwIpMcastCfgTotalLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastCfgTotalLimit.setStatus("current")


class _HwIpMcastCfgTotalThreshold_Type(Unsigned32):
    """Custom type hwIpMcastCfgTotalThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIpMcastCfgTotalThreshold_Type.__name__ = "Unsigned32"
_HwIpMcastCfgTotalThreshold_Object = MibScalar
hwIpMcastCfgTotalThreshold = _HwIpMcastCfgTotalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 20),
    _HwIpMcastCfgTotalThreshold_Type()
)
hwIpMcastCfgTotalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastCfgTotalThreshold.setStatus("current")


class _HwIpMcastTotalStat_Type(Unsigned32):
    """Custom type hwIpMcastTotalStat based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpMcastTotalStat_Type.__name__ = "Unsigned32"
_HwIpMcastTotalStat_Object = MibScalar
hwIpMcastTotalStat = _HwIpMcastTotalStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 21),
    _HwIpMcastTotalStat_Type()
)
hwIpMcastTotalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastTotalStat.setStatus("current")
_HwIpMcastDownstreamTotalTable_Object = MibTable
hwIpMcastDownstreamTotalTable = _HwIpMcastDownstreamTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    hwIpMcastDownstreamTotalTable.setStatus("current")
_HwIpMcastDownstreamTotalEntry_Object = MibTableRow
hwIpMcastDownstreamTotalEntry = _HwIpMcastDownstreamTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 22, 1)
)
hwIpMcastDownstreamTotalEntry.setIndexNames(
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastDownstreamTotalIpVersion"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastDownstreamTotalIfIndex"),
)
if mibBuilder.loadTexts:
    hwIpMcastDownstreamTotalEntry.setStatus("current")
_HwIpMcastDownstreamTotalIpVersion_Type = InetVersion
_HwIpMcastDownstreamTotalIpVersion_Object = MibTableColumn
hwIpMcastDownstreamTotalIpVersion = _HwIpMcastDownstreamTotalIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 22, 1, 1),
    _HwIpMcastDownstreamTotalIpVersion_Type()
)
hwIpMcastDownstreamTotalIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamTotalIpVersion.setStatus("current")
_HwIpMcastDownstreamTotalIfIndex_Type = InterfaceIndex
_HwIpMcastDownstreamTotalIfIndex_Object = MibTableColumn
hwIpMcastDownstreamTotalIfIndex = _HwIpMcastDownstreamTotalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 22, 1, 2),
    _HwIpMcastDownstreamTotalIfIndex_Type()
)
hwIpMcastDownstreamTotalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamTotalIfIndex.setStatus("current")


class _HwIpMcastDownstreamTotalEntriesLimit_Type(Unsigned32):
    """Custom type hwIpMcastDownstreamTotalEntriesLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIpMcastDownstreamTotalEntriesLimit_Type.__name__ = "Unsigned32"
_HwIpMcastDownstreamTotalEntriesLimit_Object = MibTableColumn
hwIpMcastDownstreamTotalEntriesLimit = _HwIpMcastDownstreamTotalEntriesLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 22, 1, 3),
    _HwIpMcastDownstreamTotalEntriesLimit_Type()
)
hwIpMcastDownstreamTotalEntriesLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamTotalEntriesLimit.setStatus("current")


class _HwIpMcastDownstreamTotalBandwidthLimit_Type(DisplayString):
    """Custom type hwIpMcastDownstreamTotalBandwidthLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpMcastDownstreamTotalBandwidthLimit_Type.__name__ = "DisplayString"
_HwIpMcastDownstreamTotalBandwidthLimit_Object = MibTableColumn
hwIpMcastDownstreamTotalBandwidthLimit = _HwIpMcastDownstreamTotalBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 22, 1, 4),
    _HwIpMcastDownstreamTotalBandwidthLimit_Type()
)
hwIpMcastDownstreamTotalBandwidthLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamTotalBandwidthLimit.setStatus("current")


class _HwIpMcastDownstreamTotalEntriesStat_Type(Unsigned32):
    """Custom type hwIpMcastDownstreamTotalEntriesStat based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpMcastDownstreamTotalEntriesStat_Type.__name__ = "Unsigned32"
_HwIpMcastDownstreamTotalEntriesStat_Object = MibTableColumn
hwIpMcastDownstreamTotalEntriesStat = _HwIpMcastDownstreamTotalEntriesStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 22, 1, 5),
    _HwIpMcastDownstreamTotalEntriesStat_Type()
)
hwIpMcastDownstreamTotalEntriesStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamTotalEntriesStat.setStatus("current")


class _HwIpMcastDownstreamTotalBandwidthStat_Type(DisplayString):
    """Custom type hwIpMcastDownstreamTotalBandwidthStat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpMcastDownstreamTotalBandwidthStat_Type.__name__ = "DisplayString"
_HwIpMcastDownstreamTotalBandwidthStat_Object = MibTableColumn
hwIpMcastDownstreamTotalBandwidthStat = _HwIpMcastDownstreamTotalBandwidthStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 22, 1, 6),
    _HwIpMcastDownstreamTotalBandwidthStat_Type()
)
hwIpMcastDownstreamTotalBandwidthStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamTotalBandwidthStat.setStatus("current")
_HwIpMcastDownstreamChannelTable_Object = MibTable
hwIpMcastDownstreamChannelTable = _HwIpMcastDownstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 23)
)
if mibBuilder.loadTexts:
    hwIpMcastDownstreamChannelTable.setStatus("current")
_HwIpMcastDownstreamChannelEntry_Object = MibTableRow
hwIpMcastDownstreamChannelEntry = _HwIpMcastDownstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 23, 1)
)
hwIpMcastDownstreamChannelEntry.setIndexNames(
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastDownstreamChannelIpVersion"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastDownstreamChannelIfIndex"),
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastDownstreamChannelName"),
)
if mibBuilder.loadTexts:
    hwIpMcastDownstreamChannelEntry.setStatus("current")
_HwIpMcastDownstreamChannelIpVersion_Type = InetVersion
_HwIpMcastDownstreamChannelIpVersion_Object = MibTableColumn
hwIpMcastDownstreamChannelIpVersion = _HwIpMcastDownstreamChannelIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 23, 1, 1),
    _HwIpMcastDownstreamChannelIpVersion_Type()
)
hwIpMcastDownstreamChannelIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamChannelIpVersion.setStatus("current")
_HwIpMcastDownstreamChannelIfIndex_Type = InterfaceIndex
_HwIpMcastDownstreamChannelIfIndex_Object = MibTableColumn
hwIpMcastDownstreamChannelIfIndex = _HwIpMcastDownstreamChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 23, 1, 2),
    _HwIpMcastDownstreamChannelIfIndex_Type()
)
hwIpMcastDownstreamChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamChannelIfIndex.setStatus("current")


class _HwIpMcastDownstreamChannelName_Type(DisplayString):
    """Custom type hwIpMcastDownstreamChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpMcastDownstreamChannelName_Type.__name__ = "DisplayString"
_HwIpMcastDownstreamChannelName_Object = MibTableColumn
hwIpMcastDownstreamChannelName = _HwIpMcastDownstreamChannelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 23, 1, 3),
    _HwIpMcastDownstreamChannelName_Type()
)
hwIpMcastDownstreamChannelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamChannelName.setStatus("current")


class _HwIpMcastDownstreamChannelEntryLimit_Type(Unsigned32):
    """Custom type hwIpMcastDownstreamChannelEntryLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIpMcastDownstreamChannelEntryLimit_Type.__name__ = "Unsigned32"
_HwIpMcastDownstreamChannelEntryLimit_Object = MibTableColumn
hwIpMcastDownstreamChannelEntryLimit = _HwIpMcastDownstreamChannelEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 23, 1, 4),
    _HwIpMcastDownstreamChannelEntryLimit_Type()
)
hwIpMcastDownstreamChannelEntryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamChannelEntryLimit.setStatus("current")


class _HwIpMcastDownstreamChannelBandwidthLimit_Type(DisplayString):
    """Custom type hwIpMcastDownstreamChannelBandwidthLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpMcastDownstreamChannelBandwidthLimit_Type.__name__ = "DisplayString"
_HwIpMcastDownstreamChannelBandwidthLimit_Object = MibTableColumn
hwIpMcastDownstreamChannelBandwidthLimit = _HwIpMcastDownstreamChannelBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 23, 1, 5),
    _HwIpMcastDownstreamChannelBandwidthLimit_Type()
)
hwIpMcastDownstreamChannelBandwidthLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamChannelBandwidthLimit.setStatus("current")


class _HwIpMcastDownstreamChannelEntryStat_Type(Unsigned32):
    """Custom type hwIpMcastDownstreamChannelEntryStat based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpMcastDownstreamChannelEntryStat_Type.__name__ = "Unsigned32"
_HwIpMcastDownstreamChannelEntryStat_Object = MibTableColumn
hwIpMcastDownstreamChannelEntryStat = _HwIpMcastDownstreamChannelEntryStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 23, 1, 6),
    _HwIpMcastDownstreamChannelEntryStat_Type()
)
hwIpMcastDownstreamChannelEntryStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamChannelEntryStat.setStatus("current")


class _HwIpMcastDownstreamChannelBandwidthStat_Type(DisplayString):
    """Custom type hwIpMcastDownstreamChannelBandwidthStat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpMcastDownstreamChannelBandwidthStat_Type.__name__ = "DisplayString"
_HwIpMcastDownstreamChannelBandwidthStat_Object = MibTableColumn
hwIpMcastDownstreamChannelBandwidthStat = _HwIpMcastDownstreamChannelBandwidthStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 23, 1, 7),
    _HwIpMcastDownstreamChannelBandwidthStat_Type()
)
hwIpMcastDownstreamChannelBandwidthStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastDownstreamChannelBandwidthStat.setStatus("current")
_HwIpMcastChannelTable_Object = MibTable
hwIpMcastChannelTable = _HwIpMcastChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 24)
)
if mibBuilder.loadTexts:
    hwIpMcastChannelTable.setStatus("current")
_HwIpMcastChannelEntry_Object = MibTableRow
hwIpMcastChannelEntry = _HwIpMcastChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 24, 1)
)
hwIpMcastChannelEntry.setIndexNames(
    (0, "HUAWEI-IPMCAST-MIB", "hwIpMcastChannelChnName"),
)
if mibBuilder.loadTexts:
    hwIpMcastChannelEntry.setStatus("current")


class _HwIpMcastChannelChnName_Type(DisplayString):
    """Custom type hwIpMcastChannelChnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpMcastChannelChnName_Type.__name__ = "DisplayString"
_HwIpMcastChannelChnName_Object = MibTableColumn
hwIpMcastChannelChnName = _HwIpMcastChannelChnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 24, 1, 1),
    _HwIpMcastChannelChnName_Type()
)
hwIpMcastChannelChnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpMcastChannelChnName.setStatus("current")


class _HwIpMcastChannelLimit_Type(Unsigned32):
    """Custom type hwIpMcastChannelLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIpMcastChannelLimit_Type.__name__ = "Unsigned32"
_HwIpMcastChannelLimit_Object = MibTableColumn
hwIpMcastChannelLimit = _HwIpMcastChannelLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 24, 1, 2),
    _HwIpMcastChannelLimit_Type()
)
hwIpMcastChannelLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelLimit.setStatus("current")


class _HwIpMcastChannelThreshold_Type(Unsigned32):
    """Custom type hwIpMcastChannelThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIpMcastChannelThreshold_Type.__name__ = "Unsigned32"
_HwIpMcastChannelThreshold_Object = MibTableColumn
hwIpMcastChannelThreshold = _HwIpMcastChannelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 24, 1, 3),
    _HwIpMcastChannelThreshold_Type()
)
hwIpMcastChannelThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelThreshold.setStatus("current")


class _HwIpMcastChannelStat_Type(Unsigned32):
    """Custom type hwIpMcastChannelStat based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpMcastChannelStat_Type.__name__ = "Unsigned32"
_HwIpMcastChannelStat_Object = MibTableColumn
hwIpMcastChannelStat = _HwIpMcastChannelStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 24, 1, 4),
    _HwIpMcastChannelStat_Type()
)
hwIpMcastChannelStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelStat.setStatus("current")
_HwIpMcastChannelMode_Type = HWChannelMode
_HwIpMcastChannelMode_Object = MibTableColumn
hwIpMcastChannelMode = _HwIpMcastChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 24, 1, 5),
    _HwIpMcastChannelMode_Type()
)
hwIpMcastChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpMcastChannelMode.setStatus("current")
_HwIpMcastInstanceName_Type = DisplayString
_HwIpMcastInstanceName_Object = MibScalar
hwIpMcastInstanceName = _HwIpMcastInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 25),
    _HwIpMcastInstanceName_Type()
)
hwIpMcastInstanceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpMcastInstanceName.setStatus("current")
_HwBoardIndex_Type = Integer32
_HwBoardIndex_Object = MibScalar
hwBoardIndex = _HwBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 26),
    _HwBoardIndex_Type()
)
hwBoardIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBoardIndex.setStatus("current")
_HwIpMcastOverloadAddressType_Type = Integer32
_HwIpMcastOverloadAddressType_Object = MibScalar
hwIpMcastOverloadAddressType = _HwIpMcastOverloadAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 27),
    _HwIpMcastOverloadAddressType_Type()
)
hwIpMcastOverloadAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpMcastOverloadAddressType.setStatus("current")
_HwIpMcastOverloadSource_Type = InetAddress
_HwIpMcastOverloadSource_Object = MibScalar
hwIpMcastOverloadSource = _HwIpMcastOverloadSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 28),
    _HwIpMcastOverloadSource_Type()
)
hwIpMcastOverloadSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpMcastOverloadSource.setStatus("current")
_HwIpMcastOverloadGroup_Type = InetAddress
_HwIpMcastOverloadGroup_Object = MibScalar
hwIpMcastOverloadGroup = _HwIpMcastOverloadGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 29),
    _HwIpMcastOverloadGroup_Type()
)
hwIpMcastOverloadGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpMcastOverloadGroup.setStatus("current")


class _HwIpMcastSGCurrentCount_Type(Unsigned32):
    """Custom type hwIpMcastSGCurrentCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_HwIpMcastSGCurrentCount_Type.__name__ = "Unsigned32"
_HwIpMcastSGCurrentCount_Object = MibScalar
hwIpMcastSGCurrentCount = _HwIpMcastSGCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 30),
    _HwIpMcastSGCurrentCount_Type()
)
hwIpMcastSGCurrentCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpMcastSGCurrentCount.setStatus("current")


class _HwIpMcastSGThreshold_Type(Unsigned32):
    """Custom type hwIpMcastSGThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwIpMcastSGThreshold_Type.__name__ = "Unsigned32"
_HwIpMcastSGThreshold_Object = MibScalar
hwIpMcastSGThreshold = _HwIpMcastSGThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 31),
    _HwIpMcastSGThreshold_Type()
)
hwIpMcastSGThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpMcastSGThreshold.setStatus("current")


class _HwIpMcastSGTotalCount_Type(Unsigned32):
    """Custom type hwIpMcastSGTotalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_HwIpMcastSGTotalCount_Type.__name__ = "Unsigned32"
_HwIpMcastSGTotalCount_Object = MibScalar
hwIpMcastSGTotalCount = _HwIpMcastSGTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 1, 1, 32),
    _HwIpMcastSGTotalCount_Type()
)
hwIpMcastSGTotalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpMcastSGTotalCount.setStatus("current")
_HwIpMcastNotifications_ObjectIdentity = ObjectIdentity
hwIpMcastNotifications = _HwIpMcastNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2)
)
_HwIpMcastMibConformance_ObjectIdentity = ObjectIdentity
hwIpMcastMibConformance = _HwIpMcastMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3)
)
_HwIpMcastMibCompliances_ObjectIdentity = ObjectIdentity
hwIpMcastMibCompliances = _HwIpMcastMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 1)
)
_HwIpMcastMibGroups_ObjectIdentity = ObjectIdentity
hwIpMcastMibGroups = _HwIpMcastMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2)
)

# Managed Objects groups

hwIpMcastMibBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2, 1)
)
hwIpMcastMibBasicGroup.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastEnable"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteEntryCount"))
)
if mibBuilder.loadTexts:
    hwIpMcastMibBasicGroup.setStatus("current")

hwIpMcastMibRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2, 2)
)
hwIpMcastMibRouteGroup.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastInterfaceTtl"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInterfaceRateLimit"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInterfaceInMcastOctets"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInterfaceOutMcastOctets"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInterfaceDiscontinuityTime"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteUpstreamNeighborType"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteUpstreamNeighbor"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteInIfIndex"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteTimeStamp"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteExpiryTime"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRoutePkts"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteTtlDropPackets"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteDifferentInIfPackets"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopState"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopTimeStamp"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopExpiryTime"))
)
if mibBuilder.loadTexts:
    hwIpMcastMibRouteGroup.setStatus("current")

hwIpMcastMibIfPktsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2, 3)
)
hwIpMcastMibIfPktsGroup.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastInterfaceInMcastPkts"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInterfaceOutMcastPkts"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInterfaceDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    hwIpMcastMibIfPktsGroup.setStatus("current")

hwIpMcastMibPktsOutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2, 4)
)
hwIpMcastMibPktsOutGroup.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopTimeStamp"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopPkts"))
)
if mibBuilder.loadTexts:
    hwIpMcastMibPktsOutGroup.setStatus("current")

hwIpMcastMibHopCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2, 5)
)
hwIpMcastMibHopCountGroup.setObjects(
    ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopClosestMemberHops")
)
if mibBuilder.loadTexts:
    hwIpMcastMibHopCountGroup.setStatus("current")

hwIpMcastMibRouteOctetsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2, 6)
)
hwIpMcastMibRouteOctetsGroup.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteTimeStamp"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteOctets"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteTtlDropOctets"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteDifferentInIfOctets"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopTimeStamp"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopOctets"))
)
if mibBuilder.loadTexts:
    hwIpMcastMibRouteOctetsGroup.setStatus("current")

hwIpMcastMibRouteProtoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2, 7)
)
hwIpMcastMibRouteProtoGroup.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteProtocol"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteRtProtocol"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteRtAddressType"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteRtAddress"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteRtPrefixLength"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteRtType"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastRouteNextHopProtocol"))
)
if mibBuilder.loadTexts:
    hwIpMcastMibRouteProtoGroup.setStatus("current")

hwIpMcastMibBoundaryIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2, 8)
)
hwIpMcastMibBoundaryIfGroup.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastBoundaryTimeStamp"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastBoundaryDroppedMcastOctets"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastBoundaryDroppedMcastPkts"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastBoundaryStatus"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastBoundaryStorageType"))
)
if mibBuilder.loadTexts:
    hwIpMcastMibBoundaryIfGroup.setStatus("current")

hwIpMcastMibNotificationObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2, 9)
)
hwIpMcastMibNotificationObjects.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelName"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGroup"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelSource"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamBandWidth"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGlobalEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamLimitBandWidth"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamLimitEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGlobalLimitEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelInterfaceIfIndex"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelInterfaceName"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastCfgTotalLimit"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastCfgTotalThreshold"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastTotalStat"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInstanceName"),
        ("HUAWEI-IPMCAST-MIB", "hwBoardIndex"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadAddressType"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadSource"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadGroup"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGCurrentCount"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGThreshold"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGTotalCount"))
)
if mibBuilder.loadTexts:
    hwIpMcastMibNotificationObjects.setStatus("current")


# Notification objects

hwIpMcastDownstreamChannelLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 1)
)
hwIpMcastDownstreamChannelLimit.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelSource"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGroup"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelInterfaceIfIndex"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelName"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamBandWidth"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelInterfaceName"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInstanceName"))
)
if mibBuilder.loadTexts:
    hwIpMcastDownstreamChannelLimit.setStatus(
        "current"
    )

hwIpMcastDownstreamTotalLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 2)
)
hwIpMcastDownstreamTotalLimit.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelSource"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGroup"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelInterfaceIfIndex"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamBandWidth"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelInterfaceName"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInstanceName"))
)
if mibBuilder.loadTexts:
    hwIpMcastDownstreamTotalLimit.setStatus(
        "current"
    )

hwIpMcastGlobalChannelLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 3)
)
hwIpMcastGlobalChannelLimit.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelSource"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGroup"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelName"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGlobalEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInstanceName"))
)
if mibBuilder.loadTexts:
    hwIpMcastGlobalChannelLimit.setStatus(
        "current"
    )

hwIpMcastGlobalTotalLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 4)
)
hwIpMcastGlobalTotalLimit.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelSource"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGroup"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGlobalEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInstanceName"))
)
if mibBuilder.loadTexts:
    hwIpMcastGlobalTotalLimit.setStatus(
        "current"
    )

hwIpMcastOutChannelExceededLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 5)
)
hwIpMcastOutChannelExceededLimit.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelName"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelInterfaceIfIndex"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamBandWidth"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamLimitEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamLimitBandWidth"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelInterfaceName"))
)
if mibBuilder.loadTexts:
    hwIpMcastOutChannelExceededLimit.setStatus(
        "obsolete"
    )

hwIpMcastOutTotalExceededLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 6)
)
hwIpMcastOutTotalExceededLimit.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelInterfaceIfIndex"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamBandWidth"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamLimitEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelDownstreamLimitBandWidth"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelInterfaceName"))
)
if mibBuilder.loadTexts:
    hwIpMcastOutTotalExceededLimit.setStatus(
        "obsolete"
    )

hwIpMcastGlobalChannelExceededLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 7)
)
hwIpMcastGlobalChannelExceededLimit.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelName"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGlobalEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGlobalLimitEntries"))
)
if mibBuilder.loadTexts:
    hwIpMcastGlobalChannelExceededLimit.setStatus(
        "obsolete"
    )

hwIpMcastGlobalTotalExceededLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 8)
)
hwIpMcastGlobalTotalExceededLimit.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGlobalEntries"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastChannelGlobalLimitEntries"))
)
if mibBuilder.loadTexts:
    hwIpMcastGlobalTotalExceededLimit.setStatus(
        "obsolete"
    )

hwMFIBEntryOverloadSuspend = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 9)
)
hwMFIBEntryOverloadSuspend.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadAddressType"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInstanceName"),
        ("HUAWEI-IPMCAST-MIB", "hwBoardIndex"))
)
if mibBuilder.loadTexts:
    hwMFIBEntryOverloadSuspend.setStatus(
        "current"
    )

hwMFIBEntryOverloadSusResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 10)
)
hwMFIBEntryOverloadSusResume.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadAddressType"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInstanceName"),
        ("HUAWEI-IPMCAST-MIB", "hwBoardIndex"))
)
if mibBuilder.loadTexts:
    hwMFIBEntryOverloadSusResume.setStatus(
        "current"
    )

hwMFIBEntryOifOverloadSuspend = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 11)
)
hwMFIBEntryOifOverloadSuspend.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadAddressType"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadSource"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadGroup"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInstanceName"),
        ("HUAWEI-IPMCAST-MIB", "hwBoardIndex"))
)
if mibBuilder.loadTexts:
    hwMFIBEntryOifOverloadSuspend.setStatus(
        "current"
    )

hwMFIBEntryOifOverloadSusResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 12)
)
hwMFIBEntryOifOverloadSusResume.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadAddressType"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadSource"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastOverloadGroup"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastInstanceName"),
        ("HUAWEI-IPMCAST-MIB", "hwBoardIndex"))
)
if mibBuilder.loadTexts:
    hwMFIBEntryOifOverloadSusResume.setStatus(
        "current"
    )

hwIpMcastSGThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 13)
)
hwIpMcastSGThresholdExceed.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastSGCurrentCount"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGThreshold"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGTotalCount"))
)
if mibBuilder.loadTexts:
    hwIpMcastSGThresholdExceed.setStatus(
        "current"
    )

hwIpMcastSGThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 14)
)
hwIpMcastSGThresholdExceedClear.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastSGCurrentCount"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGThreshold"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGTotalCount"))
)
if mibBuilder.loadTexts:
    hwIpMcastSGThresholdExceedClear.setStatus(
        "current"
    )

hwIpMcastSGExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 15)
)
hwIpMcastSGExceed.setObjects(
    ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGTotalCount")
)
if mibBuilder.loadTexts:
    hwIpMcastSGExceed.setStatus(
        "current"
    )

hwIpMcastSGExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 2, 16)
)
hwIpMcastSGExceedClear.setObjects(
    ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGTotalCount")
)
if mibBuilder.loadTexts:
    hwIpMcastSGExceedClear.setStatus(
        "current"
    )


# Notifications groups

hwIpMcastMibNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 2, 10)
)
hwIpMcastMibNotificationGroup.setObjects(
      *(("HUAWEI-IPMCAST-MIB", "hwIpMcastDownstreamChannelLimit"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastDownstreamTotalLimit"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastGlobalChannelLimit"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastGlobalTotalLimit"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastOutChannelExceededLimit"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastOutTotalExceededLimit"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastGlobalChannelExceededLimit"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastGlobalTotalExceededLimit"),
        ("HUAWEI-IPMCAST-MIB", "hwMFIBEntryOverloadSuspend"),
        ("HUAWEI-IPMCAST-MIB", "hwMFIBEntryOverloadSusResume"),
        ("HUAWEI-IPMCAST-MIB", "hwMFIBEntryOifOverloadSuspend"),
        ("HUAWEI-IPMCAST-MIB", "hwMFIBEntryOifOverloadSusResume"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGThresholdExceed"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGThresholdExceedClear"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGExceed"),
        ("HUAWEI-IPMCAST-MIB", "hwIpMcastSGExceedClear"))
)
if mibBuilder.loadTexts:
    hwIpMcastMibNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIpMcastMibComplianceHost = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwIpMcastMibComplianceHost.setStatus(
        "current"
    )

hwIpMcastMibComplianceRouter = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hwIpMcastMibComplianceRouter.setStatus(
        "current"
    )

hwIpMcastMibComplianceBorderRouter = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hwIpMcastMibComplianceBorderRouter.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-IPMCAST-MIB",
    **{"HWChannelMode": HWChannelMode,
       "hwMcast": hwMcast,
       "hwIpMcastMib": hwIpMcastMib,
       "hwIpMcastMibObjects": hwIpMcastMibObjects,
       "hwIpMcast": hwIpMcast,
       "hwIpMcastEnable": hwIpMcastEnable,
       "hwIpMcastRouteEntryCount": hwIpMcastRouteEntryCount,
       "hwIpMcastInterfaceTable": hwIpMcastInterfaceTable,
       "hwIpMcastInterfaceEntry": hwIpMcastInterfaceEntry,
       "hwIpMcastInterfaceIpVersion": hwIpMcastInterfaceIpVersion,
       "hwIpMcastInterfaceIfIndex": hwIpMcastInterfaceIfIndex,
       "hwIpMcastInterfaceTtl": hwIpMcastInterfaceTtl,
       "hwIpMcastInterfaceRateLimit": hwIpMcastInterfaceRateLimit,
       "hwIpMcastInterfaceInMcastOctets": hwIpMcastInterfaceInMcastOctets,
       "hwIpMcastInterfaceOutMcastOctets": hwIpMcastInterfaceOutMcastOctets,
       "hwIpMcastInterfaceInMcastPkts": hwIpMcastInterfaceInMcastPkts,
       "hwIpMcastInterfaceOutMcastPkts": hwIpMcastInterfaceOutMcastPkts,
       "hwIpMcastInterfaceDiscontinuityTime": hwIpMcastInterfaceDiscontinuityTime,
       "hwIpMcastRouteTable": hwIpMcastRouteTable,
       "hwIpMcastRouteEntry": hwIpMcastRouteEntry,
       "hwIpMcastRouteGroupAddressType": hwIpMcastRouteGroupAddressType,
       "hwIpMcastRouteGroup": hwIpMcastRouteGroup,
       "hwIpMcastRouteGroupPrefixLength": hwIpMcastRouteGroupPrefixLength,
       "hwIpMcastRouteSourceAddressType": hwIpMcastRouteSourceAddressType,
       "hwIpMcastRouteSource": hwIpMcastRouteSource,
       "hwIpMcastRouteSourcePrefixLength": hwIpMcastRouteSourcePrefixLength,
       "hwIpMcastRouteUpstreamNeighborType": hwIpMcastRouteUpstreamNeighborType,
       "hwIpMcastRouteUpstreamNeighbor": hwIpMcastRouteUpstreamNeighbor,
       "hwIpMcastRouteInIfIndex": hwIpMcastRouteInIfIndex,
       "hwIpMcastRouteTimeStamp": hwIpMcastRouteTimeStamp,
       "hwIpMcastRouteExpiryTime": hwIpMcastRouteExpiryTime,
       "hwIpMcastRouteProtocol": hwIpMcastRouteProtocol,
       "hwIpMcastRouteRtProtocol": hwIpMcastRouteRtProtocol,
       "hwIpMcastRouteRtAddressType": hwIpMcastRouteRtAddressType,
       "hwIpMcastRouteRtAddress": hwIpMcastRouteRtAddress,
       "hwIpMcastRouteRtPrefixLength": hwIpMcastRouteRtPrefixLength,
       "hwIpMcastRouteRtType": hwIpMcastRouteRtType,
       "hwIpMcastRouteOctets": hwIpMcastRouteOctets,
       "hwIpMcastRoutePkts": hwIpMcastRoutePkts,
       "hwIpMcastRouteTtlDropOctets": hwIpMcastRouteTtlDropOctets,
       "hwIpMcastRouteTtlDropPackets": hwIpMcastRouteTtlDropPackets,
       "hwIpMcastRouteDifferentInIfOctets": hwIpMcastRouteDifferentInIfOctets,
       "hwIpMcastRouteDifferentInIfPackets": hwIpMcastRouteDifferentInIfPackets,
       "hwIpMcastRouteNextHopTable": hwIpMcastRouteNextHopTable,
       "hwIpMcastRouteNextHopEntry": hwIpMcastRouteNextHopEntry,
       "hwIpMcastRouteNextHopGroupAddressType": hwIpMcastRouteNextHopGroupAddressType,
       "hwIpMcastRouteNextHopGroup": hwIpMcastRouteNextHopGroup,
       "hwIpMcastRouteNextHopGroupPrefixLength": hwIpMcastRouteNextHopGroupPrefixLength,
       "hwIpMcastRouteNextHopSourceAddressType": hwIpMcastRouteNextHopSourceAddressType,
       "hwIpMcastRouteNextHopSource": hwIpMcastRouteNextHopSource,
       "hwIpMcastRouteNextHopSourcePrefixLength": hwIpMcastRouteNextHopSourcePrefixLength,
       "hwIpMcastRouteNextHopIfIndex": hwIpMcastRouteNextHopIfIndex,
       "hwIpMcastRouteNextHopAddressType": hwIpMcastRouteNextHopAddressType,
       "hwIpMcastRouteNextHopAddress": hwIpMcastRouteNextHopAddress,
       "hwIpMcastRouteNextHopState": hwIpMcastRouteNextHopState,
       "hwIpMcastRouteNextHopTimeStamp": hwIpMcastRouteNextHopTimeStamp,
       "hwIpMcastRouteNextHopExpiryTime": hwIpMcastRouteNextHopExpiryTime,
       "hwIpMcastRouteNextHopClosestMemberHops": hwIpMcastRouteNextHopClosestMemberHops,
       "hwIpMcastRouteNextHopProtocol": hwIpMcastRouteNextHopProtocol,
       "hwIpMcastRouteNextHopOctets": hwIpMcastRouteNextHopOctets,
       "hwIpMcastRouteNextHopPkts": hwIpMcastRouteNextHopPkts,
       "hwIpMcastBoundaryTable": hwIpMcastBoundaryTable,
       "hwIpMcastBoundaryEntry": hwIpMcastBoundaryEntry,
       "hwIpMcastBoundaryIfIndex": hwIpMcastBoundaryIfIndex,
       "hwIpMcastBoundaryAddressType": hwIpMcastBoundaryAddressType,
       "hwIpMcastBoundaryAddress": hwIpMcastBoundaryAddress,
       "hwIpMcastBoundaryAddressPrefixLength": hwIpMcastBoundaryAddressPrefixLength,
       "hwIpMcastBoundaryTimeStamp": hwIpMcastBoundaryTimeStamp,
       "hwIpMcastBoundaryDroppedMcastOctets": hwIpMcastBoundaryDroppedMcastOctets,
       "hwIpMcastBoundaryDroppedMcastPkts": hwIpMcastBoundaryDroppedMcastPkts,
       "hwIpMcastBoundaryStatus": hwIpMcastBoundaryStatus,
       "hwIpMcastBoundaryStorageType": hwIpMcastBoundaryStorageType,
       "hwIpMcastChannelName": hwIpMcastChannelName,
       "hwIpMcastChannelGroup": hwIpMcastChannelGroup,
       "hwIpMcastChannelSource": hwIpMcastChannelSource,
       "hwIpMcastChannelDownstreamEntries": hwIpMcastChannelDownstreamEntries,
       "hwIpMcastChannelDownstreamBandWidth": hwIpMcastChannelDownstreamBandWidth,
       "hwIpMcastChannelGlobalEntries": hwIpMcastChannelGlobalEntries,
       "hwIpMcastChannelDownstreamLimitBandWidth": hwIpMcastChannelDownstreamLimitBandWidth,
       "hwIpMcastChannelDownstreamLimitEntries": hwIpMcastChannelDownstreamLimitEntries,
       "hwIpMcastChannelGlobalLimitEntries": hwIpMcastChannelGlobalLimitEntries,
       "hwIpMcastChannelInterfaceIfIndex": hwIpMcastChannelInterfaceIfIndex,
       "hwIpMcastChannelInterfaceName": hwIpMcastChannelInterfaceName,
       "hwIpMcastCfgTotalLimit": hwIpMcastCfgTotalLimit,
       "hwIpMcastCfgTotalThreshold": hwIpMcastCfgTotalThreshold,
       "hwIpMcastTotalStat": hwIpMcastTotalStat,
       "hwIpMcastDownstreamTotalTable": hwIpMcastDownstreamTotalTable,
       "hwIpMcastDownstreamTotalEntry": hwIpMcastDownstreamTotalEntry,
       "hwIpMcastDownstreamTotalIpVersion": hwIpMcastDownstreamTotalIpVersion,
       "hwIpMcastDownstreamTotalIfIndex": hwIpMcastDownstreamTotalIfIndex,
       "hwIpMcastDownstreamTotalEntriesLimit": hwIpMcastDownstreamTotalEntriesLimit,
       "hwIpMcastDownstreamTotalBandwidthLimit": hwIpMcastDownstreamTotalBandwidthLimit,
       "hwIpMcastDownstreamTotalEntriesStat": hwIpMcastDownstreamTotalEntriesStat,
       "hwIpMcastDownstreamTotalBandwidthStat": hwIpMcastDownstreamTotalBandwidthStat,
       "hwIpMcastDownstreamChannelTable": hwIpMcastDownstreamChannelTable,
       "hwIpMcastDownstreamChannelEntry": hwIpMcastDownstreamChannelEntry,
       "hwIpMcastDownstreamChannelIpVersion": hwIpMcastDownstreamChannelIpVersion,
       "hwIpMcastDownstreamChannelIfIndex": hwIpMcastDownstreamChannelIfIndex,
       "hwIpMcastDownstreamChannelName": hwIpMcastDownstreamChannelName,
       "hwIpMcastDownstreamChannelEntryLimit": hwIpMcastDownstreamChannelEntryLimit,
       "hwIpMcastDownstreamChannelBandwidthLimit": hwIpMcastDownstreamChannelBandwidthLimit,
       "hwIpMcastDownstreamChannelEntryStat": hwIpMcastDownstreamChannelEntryStat,
       "hwIpMcastDownstreamChannelBandwidthStat": hwIpMcastDownstreamChannelBandwidthStat,
       "hwIpMcastChannelTable": hwIpMcastChannelTable,
       "hwIpMcastChannelEntry": hwIpMcastChannelEntry,
       "hwIpMcastChannelChnName": hwIpMcastChannelChnName,
       "hwIpMcastChannelLimit": hwIpMcastChannelLimit,
       "hwIpMcastChannelThreshold": hwIpMcastChannelThreshold,
       "hwIpMcastChannelStat": hwIpMcastChannelStat,
       "hwIpMcastChannelMode": hwIpMcastChannelMode,
       "hwIpMcastInstanceName": hwIpMcastInstanceName,
       "hwBoardIndex": hwBoardIndex,
       "hwIpMcastOverloadAddressType": hwIpMcastOverloadAddressType,
       "hwIpMcastOverloadSource": hwIpMcastOverloadSource,
       "hwIpMcastOverloadGroup": hwIpMcastOverloadGroup,
       "hwIpMcastSGCurrentCount": hwIpMcastSGCurrentCount,
       "hwIpMcastSGThreshold": hwIpMcastSGThreshold,
       "hwIpMcastSGTotalCount": hwIpMcastSGTotalCount,
       "hwIpMcastNotifications": hwIpMcastNotifications,
       "hwIpMcastDownstreamChannelLimit": hwIpMcastDownstreamChannelLimit,
       "hwIpMcastDownstreamTotalLimit": hwIpMcastDownstreamTotalLimit,
       "hwIpMcastGlobalChannelLimit": hwIpMcastGlobalChannelLimit,
       "hwIpMcastGlobalTotalLimit": hwIpMcastGlobalTotalLimit,
       "hwIpMcastOutChannelExceededLimit": hwIpMcastOutChannelExceededLimit,
       "hwIpMcastOutTotalExceededLimit": hwIpMcastOutTotalExceededLimit,
       "hwIpMcastGlobalChannelExceededLimit": hwIpMcastGlobalChannelExceededLimit,
       "hwIpMcastGlobalTotalExceededLimit": hwIpMcastGlobalTotalExceededLimit,
       "hwMFIBEntryOverloadSuspend": hwMFIBEntryOverloadSuspend,
       "hwMFIBEntryOverloadSusResume": hwMFIBEntryOverloadSusResume,
       "hwMFIBEntryOifOverloadSuspend": hwMFIBEntryOifOverloadSuspend,
       "hwMFIBEntryOifOverloadSusResume": hwMFIBEntryOifOverloadSusResume,
       "hwIpMcastSGThresholdExceed": hwIpMcastSGThresholdExceed,
       "hwIpMcastSGThresholdExceedClear": hwIpMcastSGThresholdExceedClear,
       "hwIpMcastSGExceed": hwIpMcastSGExceed,
       "hwIpMcastSGExceedClear": hwIpMcastSGExceedClear,
       "hwIpMcastMibConformance": hwIpMcastMibConformance,
       "hwIpMcastMibCompliances": hwIpMcastMibCompliances,
       "hwIpMcastMibComplianceHost": hwIpMcastMibComplianceHost,
       "hwIpMcastMibComplianceRouter": hwIpMcastMibComplianceRouter,
       "hwIpMcastMibComplianceBorderRouter": hwIpMcastMibComplianceBorderRouter,
       "hwIpMcastMibGroups": hwIpMcastMibGroups,
       "hwIpMcastMibBasicGroup": hwIpMcastMibBasicGroup,
       "hwIpMcastMibRouteGroup": hwIpMcastMibRouteGroup,
       "hwIpMcastMibIfPktsGroup": hwIpMcastMibIfPktsGroup,
       "hwIpMcastMibPktsOutGroup": hwIpMcastMibPktsOutGroup,
       "hwIpMcastMibHopCountGroup": hwIpMcastMibHopCountGroup,
       "hwIpMcastMibRouteOctetsGroup": hwIpMcastMibRouteOctetsGroup,
       "hwIpMcastMibRouteProtoGroup": hwIpMcastMibRouteProtoGroup,
       "hwIpMcastMibBoundaryIfGroup": hwIpMcastMibBoundaryIfGroup,
       "hwIpMcastMibNotificationObjects": hwIpMcastMibNotificationObjects,
       "hwIpMcastMibNotificationGroup": hwIpMcastMibNotificationGroup}
)
