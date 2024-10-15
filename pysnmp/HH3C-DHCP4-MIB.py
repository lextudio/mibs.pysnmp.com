# SNMP MIB module (HH3C-DHCP4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DHCP4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:40 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

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


# MODULE-IDENTITY

hh3cDhcp4 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122)
)
hh3cDhcp4.setRevisions(
        ("2013-04-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDhcpServer2ScalarObjects_ObjectIdentity = ObjectIdentity
hh3cDhcpServer2ScalarObjects = _Hh3cDhcpServer2ScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1)
)
_Hh3cDhcpServer2ConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDhcpServer2ConfigGroup = _Hh3cDhcpServer2ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 1)
)


class _Hh3cDhcpServer2Enabled_Type(TruthValue):
    """Custom type hh3cDhcpServer2Enabled based on TruthValue"""


_Hh3cDhcpServer2Enabled_Object = MibScalar
hh3cDhcpServer2Enabled = _Hh3cDhcpServer2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 1, 1),
    _Hh3cDhcpServer2Enabled_Type()
)
hh3cDhcpServer2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpServer2Enabled.setStatus("current")


class _Hh3cDhcpServer2AlwaysBroadcast_Type(TruthValue):
    """Custom type hh3cDhcpServer2AlwaysBroadcast based on TruthValue"""


_Hh3cDhcpServer2AlwaysBroadcast_Object = MibScalar
hh3cDhcpServer2AlwaysBroadcast = _Hh3cDhcpServer2AlwaysBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 1, 2),
    _Hh3cDhcpServer2AlwaysBroadcast_Type()
)
hh3cDhcpServer2AlwaysBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpServer2AlwaysBroadcast.setStatus("current")


class _Hh3cDhcpServer2IgnoreBootp_Type(TruthValue):
    """Custom type hh3cDhcpServer2IgnoreBootp based on TruthValue"""


_Hh3cDhcpServer2IgnoreBootp_Object = MibScalar
hh3cDhcpServer2IgnoreBootp = _Hh3cDhcpServer2IgnoreBootp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 1, 3),
    _Hh3cDhcpServer2IgnoreBootp_Type()
)
hh3cDhcpServer2IgnoreBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IgnoreBootp.setStatus("current")


class _Hh3cDhcpServer2BootpReplyRfc1048_Type(TruthValue):
    """Custom type hh3cDhcpServer2BootpReplyRfc1048 based on TruthValue"""


_Hh3cDhcpServer2BootpReplyRfc1048_Object = MibScalar
hh3cDhcpServer2BootpReplyRfc1048 = _Hh3cDhcpServer2BootpReplyRfc1048_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 1, 4),
    _Hh3cDhcpServer2BootpReplyRfc1048_Type()
)
hh3cDhcpServer2BootpReplyRfc1048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpServer2BootpReplyRfc1048.setStatus("current")


class _Hh3cDhcpServer2Opt82Enabled_Type(TruthValue):
    """Custom type hh3cDhcpServer2Opt82Enabled based on TruthValue"""


_Hh3cDhcpServer2Opt82Enabled_Object = MibScalar
hh3cDhcpServer2Opt82Enabled = _Hh3cDhcpServer2Opt82Enabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 1, 5),
    _Hh3cDhcpServer2Opt82Enabled_Type()
)
hh3cDhcpServer2Opt82Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpServer2Opt82Enabled.setStatus("current")


class _Hh3cDhcpServer2PingNumber_Type(Unsigned32):
    """Custom type hh3cDhcpServer2PingNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Hh3cDhcpServer2PingNumber_Type.__name__ = "Unsigned32"
_Hh3cDhcpServer2PingNumber_Object = MibScalar
hh3cDhcpServer2PingNumber = _Hh3cDhcpServer2PingNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 1, 6),
    _Hh3cDhcpServer2PingNumber_Type()
)
hh3cDhcpServer2PingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PingNumber.setStatus("current")


class _Hh3cDhcpServer2PingTimeout_Type(Unsigned32):
    """Custom type hh3cDhcpServer2PingTimeout based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Hh3cDhcpServer2PingTimeout_Type.__name__ = "Unsigned32"
_Hh3cDhcpServer2PingTimeout_Object = MibScalar
hh3cDhcpServer2PingTimeout = _Hh3cDhcpServer2PingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 1, 7),
    _Hh3cDhcpServer2PingTimeout_Type()
)
hh3cDhcpServer2PingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PingTimeout.setStatus("current")
_Hh3cDhcpServer2StatGroup_ObjectIdentity = ObjectIdentity
hh3cDhcpServer2StatGroup = _Hh3cDhcpServer2StatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2)
)
_Hh3cDhcpServer2BadNum_Type = Counter64
_Hh3cDhcpServer2BadNum_Object = MibScalar
hh3cDhcpServer2BadNum = _Hh3cDhcpServer2BadNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 1),
    _Hh3cDhcpServer2BadNum_Type()
)
hh3cDhcpServer2BadNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2BadNum.setStatus("current")
_Hh3cDhcpServer2BootpRequestNum_Type = Counter64
_Hh3cDhcpServer2BootpRequestNum_Object = MibScalar
hh3cDhcpServer2BootpRequestNum = _Hh3cDhcpServer2BootpRequestNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 2),
    _Hh3cDhcpServer2BootpRequestNum_Type()
)
hh3cDhcpServer2BootpRequestNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2BootpRequestNum.setStatus("current")
_Hh3cDhcpServer2DiscoverNum_Type = Counter64
_Hh3cDhcpServer2DiscoverNum_Object = MibScalar
hh3cDhcpServer2DiscoverNum = _Hh3cDhcpServer2DiscoverNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 3),
    _Hh3cDhcpServer2DiscoverNum_Type()
)
hh3cDhcpServer2DiscoverNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2DiscoverNum.setStatus("current")
_Hh3cDhcpServer2RequestNum_Type = Counter64
_Hh3cDhcpServer2RequestNum_Object = MibScalar
hh3cDhcpServer2RequestNum = _Hh3cDhcpServer2RequestNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 4),
    _Hh3cDhcpServer2RequestNum_Type()
)
hh3cDhcpServer2RequestNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RequestNum.setStatus("current")
_Hh3cDhcpServer2DeclineNum_Type = Counter64
_Hh3cDhcpServer2DeclineNum_Object = MibScalar
hh3cDhcpServer2DeclineNum = _Hh3cDhcpServer2DeclineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 5),
    _Hh3cDhcpServer2DeclineNum_Type()
)
hh3cDhcpServer2DeclineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2DeclineNum.setStatus("current")
_Hh3cDhcpServer2ReleaseNum_Type = Counter64
_Hh3cDhcpServer2ReleaseNum_Object = MibScalar
hh3cDhcpServer2ReleaseNum = _Hh3cDhcpServer2ReleaseNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 6),
    _Hh3cDhcpServer2ReleaseNum_Type()
)
hh3cDhcpServer2ReleaseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ReleaseNum.setStatus("current")
_Hh3cDhcpServer2InformNum_Type = Counter64
_Hh3cDhcpServer2InformNum_Object = MibScalar
hh3cDhcpServer2InformNum = _Hh3cDhcpServer2InformNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 7),
    _Hh3cDhcpServer2InformNum_Type()
)
hh3cDhcpServer2InformNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2InformNum.setStatus("current")
_Hh3cDhcpServer2BootpReplyNum_Type = Counter64
_Hh3cDhcpServer2BootpReplyNum_Object = MibScalar
hh3cDhcpServer2BootpReplyNum = _Hh3cDhcpServer2BootpReplyNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 8),
    _Hh3cDhcpServer2BootpReplyNum_Type()
)
hh3cDhcpServer2BootpReplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2BootpReplyNum.setStatus("current")
_Hh3cDhcpServer2OfferNum_Type = Counter64
_Hh3cDhcpServer2OfferNum_Object = MibScalar
hh3cDhcpServer2OfferNum = _Hh3cDhcpServer2OfferNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 9),
    _Hh3cDhcpServer2OfferNum_Type()
)
hh3cDhcpServer2OfferNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2OfferNum.setStatus("current")
_Hh3cDhcpServer2AckNum_Type = Counter64
_Hh3cDhcpServer2AckNum_Object = MibScalar
hh3cDhcpServer2AckNum = _Hh3cDhcpServer2AckNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 10),
    _Hh3cDhcpServer2AckNum_Type()
)
hh3cDhcpServer2AckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2AckNum.setStatus("current")
_Hh3cDhcpServer2NakNum_Type = Counter64
_Hh3cDhcpServer2NakNum_Object = MibScalar
hh3cDhcpServer2NakNum = _Hh3cDhcpServer2NakNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 11),
    _Hh3cDhcpServer2NakNum_Type()
)
hh3cDhcpServer2NakNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2NakNum.setStatus("current")


class _Hh3cDhcpServer2TotalPoolUsage_Type(Unsigned32):
    """Custom type hh3cDhcpServer2TotalPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDhcpServer2TotalPoolUsage_Type.__name__ = "Unsigned32"
_Hh3cDhcpServer2TotalPoolUsage_Object = MibScalar
hh3cDhcpServer2TotalPoolUsage = _Hh3cDhcpServer2TotalPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 12),
    _Hh3cDhcpServer2TotalPoolUsage_Type()
)
hh3cDhcpServer2TotalPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2TotalPoolUsage.setStatus("current")
_Hh3cDhcpServer2PoolNumber_Type = Unsigned32
_Hh3cDhcpServer2PoolNumber_Object = MibScalar
hh3cDhcpServer2PoolNumber = _Hh3cDhcpServer2PoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 13),
    _Hh3cDhcpServer2PoolNumber_Type()
)
hh3cDhcpServer2PoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolNumber.setStatus("current")
_Hh3cDhcpServer2ConflictNum_Type = Unsigned32
_Hh3cDhcpServer2ConflictNum_Object = MibScalar
hh3cDhcpServer2ConflictNum = _Hh3cDhcpServer2ConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 14),
    _Hh3cDhcpServer2ConflictNum_Type()
)
hh3cDhcpServer2ConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ConflictNum.setStatus("current")
_Hh3cDhcpServer2AutoBindNum_Type = Unsigned32
_Hh3cDhcpServer2AutoBindNum_Object = MibScalar
hh3cDhcpServer2AutoBindNum = _Hh3cDhcpServer2AutoBindNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 15),
    _Hh3cDhcpServer2AutoBindNum_Type()
)
hh3cDhcpServer2AutoBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2AutoBindNum.setStatus("current")
_Hh3cDhcpServer2ManualBindNum_Type = Unsigned32
_Hh3cDhcpServer2ManualBindNum_Object = MibScalar
hh3cDhcpServer2ManualBindNum = _Hh3cDhcpServer2ManualBindNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 16),
    _Hh3cDhcpServer2ManualBindNum_Type()
)
hh3cDhcpServer2ManualBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ManualBindNum.setStatus("current")
_Hh3cDhcpServer2ExpiredBindNum_Type = Unsigned32
_Hh3cDhcpServer2ExpiredBindNum_Object = MibScalar
hh3cDhcpServer2ExpiredBindNum = _Hh3cDhcpServer2ExpiredBindNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 1, 2, 17),
    _Hh3cDhcpServer2ExpiredBindNum_Type()
)
hh3cDhcpServer2ExpiredBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ExpiredBindNum.setStatus("current")
_Hh3cDhcpServer2Tables_ObjectIdentity = ObjectIdentity
hh3cDhcpServer2Tables = _Hh3cDhcpServer2Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2)
)
_Hh3cDhcpServer2PoolTable_Object = MibTable
hh3cDhcpServer2PoolTable = _Hh3cDhcpServer2PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolTable.setStatus("current")
_Hh3cDhcpServer2PoolEntry_Object = MibTableRow
hh3cDhcpServer2PoolEntry = _Hh3cDhcpServer2PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1)
)
hh3cDhcpServer2PoolEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolEntry.setStatus("current")


class _Hh3cDhcpServer2PoolIndex_Type(Unsigned32):
    """Custom type hh3cDhcpServer2PoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cDhcpServer2PoolIndex_Type.__name__ = "Unsigned32"
_Hh3cDhcpServer2PoolIndex_Object = MibTableColumn
hh3cDhcpServer2PoolIndex = _Hh3cDhcpServer2PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 1),
    _Hh3cDhcpServer2PoolIndex_Type()
)
hh3cDhcpServer2PoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolIndex.setStatus("current")


class _Hh3cDhcpServer2PoolName_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDhcpServer2PoolName_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolName_Object = MibTableColumn
hh3cDhcpServer2PoolName = _Hh3cDhcpServer2PoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 2),
    _Hh3cDhcpServer2PoolName_Type()
)
hh3cDhcpServer2PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolName.setStatus("current")


class _Hh3cDhcpServer2PoolVpnName_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cDhcpServer2PoolVpnName_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolVpnName_Object = MibTableColumn
hh3cDhcpServer2PoolVpnName = _Hh3cDhcpServer2PoolVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 3),
    _Hh3cDhcpServer2PoolVpnName_Type()
)
hh3cDhcpServer2PoolVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolVpnName.setStatus("current")
_Hh3cDhcpServer2PoolNetwork_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolNetwork_Object = MibTableColumn
hh3cDhcpServer2PoolNetwork = _Hh3cDhcpServer2PoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 4),
    _Hh3cDhcpServer2PoolNetwork_Type()
)
hh3cDhcpServer2PoolNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolNetwork.setStatus("current")
_Hh3cDhcpServer2PoolNetworkMask_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolNetworkMask_Object = MibTableColumn
hh3cDhcpServer2PoolNetworkMask = _Hh3cDhcpServer2PoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 5),
    _Hh3cDhcpServer2PoolNetworkMask_Type()
)
hh3cDhcpServer2PoolNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolNetworkMask.setStatus("current")
_Hh3cDhcpServer2PoolStartAddr_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolStartAddr_Object = MibTableColumn
hh3cDhcpServer2PoolStartAddr = _Hh3cDhcpServer2PoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 6),
    _Hh3cDhcpServer2PoolStartAddr_Type()
)
hh3cDhcpServer2PoolStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolStartAddr.setStatus("current")
_Hh3cDhcpServer2PoolEndAddr_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolEndAddr_Object = MibTableColumn
hh3cDhcpServer2PoolEndAddr = _Hh3cDhcpServer2PoolEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 7),
    _Hh3cDhcpServer2PoolEndAddr_Type()
)
hh3cDhcpServer2PoolEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolEndAddr.setStatus("current")


class _Hh3cDhcpServer2PoolLeaseDay_Type(Integer32):
    """Custom type hh3cDhcpServer2PoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_Hh3cDhcpServer2PoolLeaseDay_Type.__name__ = "Integer32"
_Hh3cDhcpServer2PoolLeaseDay_Object = MibTableColumn
hh3cDhcpServer2PoolLeaseDay = _Hh3cDhcpServer2PoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 8),
    _Hh3cDhcpServer2PoolLeaseDay_Type()
)
hh3cDhcpServer2PoolLeaseDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolLeaseDay.setStatus("current")


class _Hh3cDhcpServer2PoolLeaseHour_Type(Integer32):
    """Custom type hh3cDhcpServer2PoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh3cDhcpServer2PoolLeaseHour_Type.__name__ = "Integer32"
_Hh3cDhcpServer2PoolLeaseHour_Object = MibTableColumn
hh3cDhcpServer2PoolLeaseHour = _Hh3cDhcpServer2PoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 9),
    _Hh3cDhcpServer2PoolLeaseHour_Type()
)
hh3cDhcpServer2PoolLeaseHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolLeaseHour.setStatus("current")


class _Hh3cDhcpServer2PoolLeaseMinute_Type(Integer32):
    """Custom type hh3cDhcpServer2PoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Hh3cDhcpServer2PoolLeaseMinute_Type.__name__ = "Integer32"
_Hh3cDhcpServer2PoolLeaseMinute_Object = MibTableColumn
hh3cDhcpServer2PoolLeaseMinute = _Hh3cDhcpServer2PoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 10),
    _Hh3cDhcpServer2PoolLeaseMinute_Type()
)
hh3cDhcpServer2PoolLeaseMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolLeaseMinute.setStatus("current")


class _Hh3cDhcpServer2PoolLeaseSecond_Type(Integer32):
    """Custom type hh3cDhcpServer2PoolLeaseSecond based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Hh3cDhcpServer2PoolLeaseSecond_Type.__name__ = "Integer32"
_Hh3cDhcpServer2PoolLeaseSecond_Object = MibTableColumn
hh3cDhcpServer2PoolLeaseSecond = _Hh3cDhcpServer2PoolLeaseSecond_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 11),
    _Hh3cDhcpServer2PoolLeaseSecond_Type()
)
hh3cDhcpServer2PoolLeaseSecond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolLeaseSecond.setStatus("current")


class _Hh3cDhcpServer2PoolLeaseUnlimit_Type(TruthValue):
    """Custom type hh3cDhcpServer2PoolLeaseUnlimit based on TruthValue"""


_Hh3cDhcpServer2PoolLeaseUnlimit_Object = MibTableColumn
hh3cDhcpServer2PoolLeaseUnlimit = _Hh3cDhcpServer2PoolLeaseUnlimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 12),
    _Hh3cDhcpServer2PoolLeaseUnlimit_Type()
)
hh3cDhcpServer2PoolLeaseUnlimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolLeaseUnlimit.setStatus("current")
_Hh3cDhcpServer2PoolLeaseTime_Type = TimeTicks
_Hh3cDhcpServer2PoolLeaseTime_Object = MibTableColumn
hh3cDhcpServer2PoolLeaseTime = _Hh3cDhcpServer2PoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 13),
    _Hh3cDhcpServer2PoolLeaseTime_Type()
)
hh3cDhcpServer2PoolLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolLeaseTime.setStatus("current")


class _Hh3cDhcpServer2PoolDomainName_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Hh3cDhcpServer2PoolDomainName_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolDomainName_Object = MibTableColumn
hh3cDhcpServer2PoolDomainName = _Hh3cDhcpServer2PoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 14),
    _Hh3cDhcpServer2PoolDomainName_Type()
)
hh3cDhcpServer2PoolDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolDomainName.setStatus("current")


class _Hh3cDhcpServer2PoolGatewayIP_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolGatewayIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDhcpServer2PoolGatewayIP_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolGatewayIP_Object = MibTableColumn
hh3cDhcpServer2PoolGatewayIP = _Hh3cDhcpServer2PoolGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 15),
    _Hh3cDhcpServer2PoolGatewayIP_Type()
)
hh3cDhcpServer2PoolGatewayIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolGatewayIP.setStatus("current")


class _Hh3cDhcpServer2PoolDNSIP_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolDNSIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDhcpServer2PoolDNSIP_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolDNSIP_Object = MibTableColumn
hh3cDhcpServer2PoolDNSIP = _Hh3cDhcpServer2PoolDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 16),
    _Hh3cDhcpServer2PoolDNSIP_Type()
)
hh3cDhcpServer2PoolDNSIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolDNSIP.setStatus("current")
_Hh3cDhcpServer2PoolPrimaryDNSIP_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolPrimaryDNSIP_Object = MibTableColumn
hh3cDhcpServer2PoolPrimaryDNSIP = _Hh3cDhcpServer2PoolPrimaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 17),
    _Hh3cDhcpServer2PoolPrimaryDNSIP_Type()
)
hh3cDhcpServer2PoolPrimaryDNSIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolPrimaryDNSIP.setStatus("current")
_Hh3cDhcpServer2PoolSecondDNSIP_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolSecondDNSIP_Object = MibTableColumn
hh3cDhcpServer2PoolSecondDNSIP = _Hh3cDhcpServer2PoolSecondDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 18),
    _Hh3cDhcpServer2PoolSecondDNSIP_Type()
)
hh3cDhcpServer2PoolSecondDNSIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolSecondDNSIP.setStatus("current")


class _Hh3cDhcpServer2PoolNetbiosType_Type(Integer32):
    """Custom type hh3cDhcpServer2PoolNetbiosType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bnode", 1),
          ("hnode", 8),
          ("mnode", 4),
          ("null", 0),
          ("pnode", 2))
    )


_Hh3cDhcpServer2PoolNetbiosType_Type.__name__ = "Integer32"
_Hh3cDhcpServer2PoolNetbiosType_Object = MibTableColumn
hh3cDhcpServer2PoolNetbiosType = _Hh3cDhcpServer2PoolNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 19),
    _Hh3cDhcpServer2PoolNetbiosType_Type()
)
hh3cDhcpServer2PoolNetbiosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolNetbiosType.setStatus("current")


class _Hh3cDhcpServer2PoolNbnsIP_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolNbnsIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDhcpServer2PoolNbnsIP_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolNbnsIP_Object = MibTableColumn
hh3cDhcpServer2PoolNbnsIP = _Hh3cDhcpServer2PoolNbnsIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 20),
    _Hh3cDhcpServer2PoolNbnsIP_Type()
)
hh3cDhcpServer2PoolNbnsIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolNbnsIP.setStatus("current")


class _Hh3cDhcpServer2PoolBootFileName_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolBootFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDhcpServer2PoolBootFileName_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolBootFileName_Object = MibTableColumn
hh3cDhcpServer2PoolBootFileName = _Hh3cDhcpServer2PoolBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 21),
    _Hh3cDhcpServer2PoolBootFileName_Type()
)
hh3cDhcpServer2PoolBootFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolBootFileName.setStatus("current")
_Hh3cDhcpServer2PoolBimsIP_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolBimsIP_Object = MibTableColumn
hh3cDhcpServer2PoolBimsIP = _Hh3cDhcpServer2PoolBimsIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 22),
    _Hh3cDhcpServer2PoolBimsIP_Type()
)
hh3cDhcpServer2PoolBimsIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolBimsIP.setStatus("current")


class _Hh3cDhcpServer2PoolBimsPort_Type(Unsigned32):
    """Custom type hh3cDhcpServer2PoolBimsPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cDhcpServer2PoolBimsPort_Type.__name__ = "Unsigned32"
_Hh3cDhcpServer2PoolBimsPort_Object = MibTableColumn
hh3cDhcpServer2PoolBimsPort = _Hh3cDhcpServer2PoolBimsPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 23),
    _Hh3cDhcpServer2PoolBimsPort_Type()
)
hh3cDhcpServer2PoolBimsPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolBimsPort.setStatus("current")


class _Hh3cDhcpServer2PoolBimsKeyStr_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolBimsKeyStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hh3cDhcpServer2PoolBimsKeyStr_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolBimsKeyStr_Object = MibTableColumn
hh3cDhcpServer2PoolBimsKeyStr = _Hh3cDhcpServer2PoolBimsKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 24),
    _Hh3cDhcpServer2PoolBimsKeyStr_Type()
)
hh3cDhcpServer2PoolBimsKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolBimsKeyStr.setStatus("current")
_Hh3cDhcpServer2PoolNextServer_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolNextServer_Object = MibTableColumn
hh3cDhcpServer2PoolNextServer = _Hh3cDhcpServer2PoolNextServer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 25),
    _Hh3cDhcpServer2PoolNextServer_Type()
)
hh3cDhcpServer2PoolNextServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolNextServer.setStatus("current")


class _Hh3cDhcpServer2PoolTftpDomName_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolTftpDomName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDhcpServer2PoolTftpDomName_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolTftpDomName_Object = MibTableColumn
hh3cDhcpServer2PoolTftpDomName = _Hh3cDhcpServer2PoolTftpDomName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 26),
    _Hh3cDhcpServer2PoolTftpDomName_Type()
)
hh3cDhcpServer2PoolTftpDomName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolTftpDomName.setStatus("current")
_Hh3cDhcpServer2PoolTftpIP_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolTftpIP_Object = MibTableColumn
hh3cDhcpServer2PoolTftpIP = _Hh3cDhcpServer2PoolTftpIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 27),
    _Hh3cDhcpServer2PoolTftpIP_Type()
)
hh3cDhcpServer2PoolTftpIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolTftpIP.setStatus("current")
_Hh3cDhcpServer2PoolVoiceAsIP_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolVoiceAsIP_Object = MibTableColumn
hh3cDhcpServer2PoolVoiceAsIP = _Hh3cDhcpServer2PoolVoiceAsIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 28),
    _Hh3cDhcpServer2PoolVoiceAsIP_Type()
)
hh3cDhcpServer2PoolVoiceAsIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolVoiceAsIP.setStatus("current")
_Hh3cDhcpServer2PoolVoiceFailIP_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolVoiceFailIP_Object = MibTableColumn
hh3cDhcpServer2PoolVoiceFailIP = _Hh3cDhcpServer2PoolVoiceFailIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 29),
    _Hh3cDhcpServer2PoolVoiceFailIP_Type()
)
hh3cDhcpServer2PoolVoiceFailIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolVoiceFailIP.setStatus("current")


class _Hh3cDhcpServer2PoolVoiceFailStr_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolVoiceFailStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_Hh3cDhcpServer2PoolVoiceFailStr_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolVoiceFailStr_Object = MibTableColumn
hh3cDhcpServer2PoolVoiceFailStr = _Hh3cDhcpServer2PoolVoiceFailStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 30),
    _Hh3cDhcpServer2PoolVoiceFailStr_Type()
)
hh3cDhcpServer2PoolVoiceFailStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolVoiceFailStr.setStatus("current")
_Hh3cDhcpServer2PoolVoiceNCPIP_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolVoiceNCPIP_Object = MibTableColumn
hh3cDhcpServer2PoolVoiceNCPIP = _Hh3cDhcpServer2PoolVoiceNCPIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 31),
    _Hh3cDhcpServer2PoolVoiceNCPIP_Type()
)
hh3cDhcpServer2PoolVoiceNCPIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolVoiceNCPIP.setStatus("current")


class _Hh3cDhcpServer2PoolVoiceVlanId_Type(Unsigned32):
    """Custom type hh3cDhcpServer2PoolVoiceVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cDhcpServer2PoolVoiceVlanId_Type.__name__ = "Unsigned32"
_Hh3cDhcpServer2PoolVoiceVlanId_Object = MibTableColumn
hh3cDhcpServer2PoolVoiceVlanId = _Hh3cDhcpServer2PoolVoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 32),
    _Hh3cDhcpServer2PoolVoiceVlanId_Type()
)
hh3cDhcpServer2PoolVoiceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolVoiceVlanId.setStatus("current")


class _Hh3cDhcpServer2PoolVoiceVlanEnbl_Type(TruthValue):
    """Custom type hh3cDhcpServer2PoolVoiceVlanEnbl based on TruthValue"""


_Hh3cDhcpServer2PoolVoiceVlanEnbl_Object = MibTableColumn
hh3cDhcpServer2PoolVoiceVlanEnbl = _Hh3cDhcpServer2PoolVoiceVlanEnbl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 33),
    _Hh3cDhcpServer2PoolVoiceVlanEnbl_Type()
)
hh3cDhcpServer2PoolVoiceVlanEnbl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolVoiceVlanEnbl.setStatus("current")
_Hh3cDhcpServer2PoolRowStatus_Type = RowStatus
_Hh3cDhcpServer2PoolRowStatus_Object = MibTableColumn
hh3cDhcpServer2PoolRowStatus = _Hh3cDhcpServer2PoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 34),
    _Hh3cDhcpServer2PoolRowStatus_Type()
)
hh3cDhcpServer2PoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolRowStatus.setStatus("current")


class _Hh3cDhcpServer2PoolVerifyClass_Type(TruthValue):
    """Custom type hh3cDhcpServer2PoolVerifyClass based on TruthValue"""


_Hh3cDhcpServer2PoolVerifyClass_Object = MibTableColumn
hh3cDhcpServer2PoolVerifyClass = _Hh3cDhcpServer2PoolVerifyClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 1, 1, 35),
    _Hh3cDhcpServer2PoolVerifyClass_Type()
)
hh3cDhcpServer2PoolVerifyClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolVerifyClass.setStatus("current")
_Hh3cDhcpServer2IfApplyPoolTable_Object = MibTable
hh3cDhcpServer2IfApplyPoolTable = _Hh3cDhcpServer2IfApplyPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2IfApplyPoolTable.setStatus("current")
_Hh3cDhcpServer2IfApplyPoolEntry_Object = MibTableRow
hh3cDhcpServer2IfApplyPoolEntry = _Hh3cDhcpServer2IfApplyPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 2, 1)
)
hh3cDhcpServer2IfApplyPoolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2IfApplyPoolEntry.setStatus("current")


class _Hh3cDhcpServer2IfApplyPoolName_Type(OctetString):
    """Custom type hh3cDhcpServer2IfApplyPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDhcpServer2IfApplyPoolName_Type.__name__ = "OctetString"
_Hh3cDhcpServer2IfApplyPoolName_Object = MibTableColumn
hh3cDhcpServer2IfApplyPoolName = _Hh3cDhcpServer2IfApplyPoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 2, 1, 1),
    _Hh3cDhcpServer2IfApplyPoolName_Type()
)
hh3cDhcpServer2IfApplyPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IfApplyPoolName.setStatus("current")
_Hh3cDhcpServer2PoolSecNwTable_Object = MibTable
hh3cDhcpServer2PoolSecNwTable = _Hh3cDhcpServer2PoolSecNwTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolSecNwTable.setStatus("current")
_Hh3cDhcpServer2PoolSecNwEntry_Object = MibTableRow
hh3cDhcpServer2PoolSecNwEntry = _Hh3cDhcpServer2PoolSecNwEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 3, 1)
)
hh3cDhcpServer2PoolSecNwEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolSecNw"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolSecNwMask"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolSecNwEntry.setStatus("current")
_Hh3cDhcpServer2PoolSecNw_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolSecNw_Object = MibTableColumn
hh3cDhcpServer2PoolSecNw = _Hh3cDhcpServer2PoolSecNw_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 3, 1, 1),
    _Hh3cDhcpServer2PoolSecNw_Type()
)
hh3cDhcpServer2PoolSecNw.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolSecNw.setStatus("current")
_Hh3cDhcpServer2PoolSecNwMask_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolSecNwMask_Object = MibTableColumn
hh3cDhcpServer2PoolSecNwMask = _Hh3cDhcpServer2PoolSecNwMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 3, 1, 2),
    _Hh3cDhcpServer2PoolSecNwMask_Type()
)
hh3cDhcpServer2PoolSecNwMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolSecNwMask.setStatus("current")


class _Hh3cDhcpServer2PoolSecNwGwIP_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolSecNwGwIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDhcpServer2PoolSecNwGwIP_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolSecNwGwIP_Object = MibTableColumn
hh3cDhcpServer2PoolSecNwGwIP = _Hh3cDhcpServer2PoolSecNwGwIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 3, 1, 3),
    _Hh3cDhcpServer2PoolSecNwGwIP_Type()
)
hh3cDhcpServer2PoolSecNwGwIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolSecNwGwIP.setStatus("current")
_Hh3cDhcpServer2PoolSecNwStatus_Type = RowStatus
_Hh3cDhcpServer2PoolSecNwStatus_Object = MibTableColumn
hh3cDhcpServer2PoolSecNwStatus = _Hh3cDhcpServer2PoolSecNwStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 3, 1, 4),
    _Hh3cDhcpServer2PoolSecNwStatus_Type()
)
hh3cDhcpServer2PoolSecNwStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolSecNwStatus.setStatus("current")
_Hh3cDhcpServer2PoolClassTable_Object = MibTable
hh3cDhcpServer2PoolClassTable = _Hh3cDhcpServer2PoolClassTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolClassTable.setStatus("current")
_Hh3cDhcpServer2PoolClassEntry_Object = MibTableRow
hh3cDhcpServer2PoolClassEntry = _Hh3cDhcpServer2PoolClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 4, 1)
)
hh3cDhcpServer2PoolClassEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolClassName"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolClassEntry.setStatus("current")


class _Hh3cDhcpServer2PoolClassName_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDhcpServer2PoolClassName_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolClassName_Object = MibTableColumn
hh3cDhcpServer2PoolClassName = _Hh3cDhcpServer2PoolClassName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 4, 1, 1),
    _Hh3cDhcpServer2PoolClassName_Type()
)
hh3cDhcpServer2PoolClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolClassName.setStatus("current")
_Hh3cDhcpServer2PoolClassStart_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolClassStart_Object = MibTableColumn
hh3cDhcpServer2PoolClassStart = _Hh3cDhcpServer2PoolClassStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 4, 1, 2),
    _Hh3cDhcpServer2PoolClassStart_Type()
)
hh3cDhcpServer2PoolClassStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolClassStart.setStatus("current")
_Hh3cDhcpServer2PoolClassEnd_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolClassEnd_Object = MibTableColumn
hh3cDhcpServer2PoolClassEnd = _Hh3cDhcpServer2PoolClassEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 4, 1, 3),
    _Hh3cDhcpServer2PoolClassEnd_Type()
)
hh3cDhcpServer2PoolClassEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolClassEnd.setStatus("current")
_Hh3cDhcpServer2PoolClassStatus_Type = RowStatus
_Hh3cDhcpServer2PoolClassStatus_Object = MibTableColumn
hh3cDhcpServer2PoolClassStatus = _Hh3cDhcpServer2PoolClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 4, 1, 4),
    _Hh3cDhcpServer2PoolClassStatus_Type()
)
hh3cDhcpServer2PoolClassStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolClassStatus.setStatus("current")
_Hh3cDhcpServer2PoolStaticTable_Object = MibTable
hh3cDhcpServer2PoolStaticTable = _Hh3cDhcpServer2PoolStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolStaticTable.setStatus("current")
_Hh3cDhcpServer2PoolStaticEntry_Object = MibTableRow
hh3cDhcpServer2PoolStaticEntry = _Hh3cDhcpServer2PoolStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 5, 1)
)
hh3cDhcpServer2PoolStaticEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolStaticIP"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolStaticEntry.setStatus("current")
_Hh3cDhcpServer2PoolStaticIP_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolStaticIP_Object = MibTableColumn
hh3cDhcpServer2PoolStaticIP = _Hh3cDhcpServer2PoolStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 5, 1, 1),
    _Hh3cDhcpServer2PoolStaticIP_Type()
)
hh3cDhcpServer2PoolStaticIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolStaticIP.setStatus("current")
_Hh3cDhcpServer2PoolStaticMask_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolStaticMask_Object = MibTableColumn
hh3cDhcpServer2PoolStaticMask = _Hh3cDhcpServer2PoolStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 5, 1, 2),
    _Hh3cDhcpServer2PoolStaticMask_Type()
)
hh3cDhcpServer2PoolStaticMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolStaticMask.setStatus("current")


class _Hh3cDhcpServer2PoolStaticCID_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolStaticCID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 254),
    )


_Hh3cDhcpServer2PoolStaticCID_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolStaticCID_Object = MibTableColumn
hh3cDhcpServer2PoolStaticCID = _Hh3cDhcpServer2PoolStaticCID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 5, 1, 3),
    _Hh3cDhcpServer2PoolStaticCID_Type()
)
hh3cDhcpServer2PoolStaticCID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolStaticCID.setStatus("current")


class _Hh3cDhcpServer2PoolStaticHAddr_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolStaticHAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 39),
    )


_Hh3cDhcpServer2PoolStaticHAddr_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolStaticHAddr_Object = MibTableColumn
hh3cDhcpServer2PoolStaticHAddr = _Hh3cDhcpServer2PoolStaticHAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 5, 1, 4),
    _Hh3cDhcpServer2PoolStaticHAddr_Type()
)
hh3cDhcpServer2PoolStaticHAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolStaticHAddr.setStatus("current")


class _Hh3cDhcpServer2PoolStaticHType_Type(Integer32):
    """Custom type hh3cDhcpServer2PoolStaticHType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("ethernet", 2),
          ("tokenRing", 3))
    )


_Hh3cDhcpServer2PoolStaticHType_Type.__name__ = "Integer32"
_Hh3cDhcpServer2PoolStaticHType_Object = MibTableColumn
hh3cDhcpServer2PoolStaticHType = _Hh3cDhcpServer2PoolStaticHType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 5, 1, 5),
    _Hh3cDhcpServer2PoolStaticHType_Type()
)
hh3cDhcpServer2PoolStaticHType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolStaticHType.setStatus("current")
_Hh3cDhcpServer2PoolStaticStatus_Type = RowStatus
_Hh3cDhcpServer2PoolStaticStatus_Object = MibTableColumn
hh3cDhcpServer2PoolStaticStatus = _Hh3cDhcpServer2PoolStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 5, 1, 6),
    _Hh3cDhcpServer2PoolStaticStatus_Type()
)
hh3cDhcpServer2PoolStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolStaticStatus.setStatus("current")
_Hh3cDhcpServer2PoolOptionTable_Object = MibTable
hh3cDhcpServer2PoolOptionTable = _Hh3cDhcpServer2PoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolOptionTable.setStatus("current")
_Hh3cDhcpServer2PoolOptionEntry_Object = MibTableRow
hh3cDhcpServer2PoolOptionEntry = _Hh3cDhcpServer2PoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 6, 1)
)
hh3cDhcpServer2PoolOptionEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolOptCode"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolOptionEntry.setStatus("current")


class _Hh3cDhcpServer2PoolOptCode_Type(Integer32):
    """Custom type hh3cDhcpServer2PoolOptCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_Hh3cDhcpServer2PoolOptCode_Type.__name__ = "Integer32"
_Hh3cDhcpServer2PoolOptCode_Object = MibTableColumn
hh3cDhcpServer2PoolOptCode = _Hh3cDhcpServer2PoolOptCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 6, 1, 1),
    _Hh3cDhcpServer2PoolOptCode_Type()
)
hh3cDhcpServer2PoolOptCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolOptCode.setStatus("current")


class _Hh3cDhcpServer2PoolOptType_Type(Integer32):
    """Custom type hh3cDhcpServer2PoolOptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2),
          ("ip", 3))
    )


_Hh3cDhcpServer2PoolOptType_Type.__name__ = "Integer32"
_Hh3cDhcpServer2PoolOptType_Object = MibTableColumn
hh3cDhcpServer2PoolOptType = _Hh3cDhcpServer2PoolOptType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 6, 1, 2),
    _Hh3cDhcpServer2PoolOptType_Type()
)
hh3cDhcpServer2PoolOptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolOptType.setStatus("current")


class _Hh3cDhcpServer2PoolOptAscii_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolOptAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDhcpServer2PoolOptAscii_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolOptAscii_Object = MibTableColumn
hh3cDhcpServer2PoolOptAscii = _Hh3cDhcpServer2PoolOptAscii_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 6, 1, 3),
    _Hh3cDhcpServer2PoolOptAscii_Type()
)
hh3cDhcpServer2PoolOptAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolOptAscii.setStatus("current")


class _Hh3cDhcpServer2PoolOptHexStr_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolOptHexStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_Hh3cDhcpServer2PoolOptHexStr_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolOptHexStr_Object = MibTableColumn
hh3cDhcpServer2PoolOptHexStr = _Hh3cDhcpServer2PoolOptHexStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 6, 1, 4),
    _Hh3cDhcpServer2PoolOptHexStr_Type()
)
hh3cDhcpServer2PoolOptHexStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolOptHexStr.setStatus("current")


class _Hh3cDhcpServer2PoolOptIPStr_Type(OctetString):
    """Custom type hh3cDhcpServer2PoolOptIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDhcpServer2PoolOptIPStr_Type.__name__ = "OctetString"
_Hh3cDhcpServer2PoolOptIPStr_Object = MibTableColumn
hh3cDhcpServer2PoolOptIPStr = _Hh3cDhcpServer2PoolOptIPStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 6, 1, 5),
    _Hh3cDhcpServer2PoolOptIPStr_Type()
)
hh3cDhcpServer2PoolOptIPStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolOptIPStr.setStatus("current")
_Hh3cDhcpServer2PoolOptRowStatus_Type = RowStatus
_Hh3cDhcpServer2PoolOptRowStatus_Object = MibTableColumn
hh3cDhcpServer2PoolOptRowStatus = _Hh3cDhcpServer2PoolOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 6, 1, 6),
    _Hh3cDhcpServer2PoolOptRowStatus_Type()
)
hh3cDhcpServer2PoolOptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolOptRowStatus.setStatus("current")
_Hh3cDhcpServer2PoolForbidTable_Object = MibTable
hh3cDhcpServer2PoolForbidTable = _Hh3cDhcpServer2PoolForbidTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolForbidTable.setStatus("current")
_Hh3cDhcpServer2PoolForbidEntry_Object = MibTableRow
hh3cDhcpServer2PoolForbidEntry = _Hh3cDhcpServer2PoolForbidEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 7, 1)
)
hh3cDhcpServer2PoolForbidEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolForbidIP"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolForbidEntry.setStatus("current")
_Hh3cDhcpServer2PoolForbidIP_Type = InetAddressIPv4
_Hh3cDhcpServer2PoolForbidIP_Object = MibTableColumn
hh3cDhcpServer2PoolForbidIP = _Hh3cDhcpServer2PoolForbidIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 7, 1, 1),
    _Hh3cDhcpServer2PoolForbidIP_Type()
)
hh3cDhcpServer2PoolForbidIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolForbidIP.setStatus("current")
_Hh3cDhcpServer2PoolForbidStatus_Type = RowStatus
_Hh3cDhcpServer2PoolForbidStatus_Object = MibTableColumn
hh3cDhcpServer2PoolForbidStatus = _Hh3cDhcpServer2PoolForbidStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 7, 1, 2),
    _Hh3cDhcpServer2PoolForbidStatus_Type()
)
hh3cDhcpServer2PoolForbidStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2PoolForbidStatus.setStatus("current")
_Hh3cDhcpServer2ClassTable_Object = MibTable
hh3cDhcpServer2ClassTable = _Hh3cDhcpServer2ClassTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2ClassTable.setStatus("current")
_Hh3cDhcpServer2ClassEntry_Object = MibTableRow
hh3cDhcpServer2ClassEntry = _Hh3cDhcpServer2ClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 8, 1)
)
hh3cDhcpServer2ClassEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2ClassName"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2ClassEntry.setStatus("current")


class _Hh3cDhcpServer2ClassName_Type(OctetString):
    """Custom type hh3cDhcpServer2ClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDhcpServer2ClassName_Type.__name__ = "OctetString"
_Hh3cDhcpServer2ClassName_Object = MibTableColumn
hh3cDhcpServer2ClassName = _Hh3cDhcpServer2ClassName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 8, 1, 1),
    _Hh3cDhcpServer2ClassName_Type()
)
hh3cDhcpServer2ClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ClassName.setStatus("current")
_Hh3cDhcpServer2ClassRowStatus_Type = RowStatus
_Hh3cDhcpServer2ClassRowStatus_Object = MibTableColumn
hh3cDhcpServer2ClassRowStatus = _Hh3cDhcpServer2ClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 8, 1, 2),
    _Hh3cDhcpServer2ClassRowStatus_Type()
)
hh3cDhcpServer2ClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ClassRowStatus.setStatus("current")
_Hh3cDhcpServer2RuleTable_Object = MibTable
hh3cDhcpServer2RuleTable = _Hh3cDhcpServer2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleTable.setStatus("current")
_Hh3cDhcpServer2RuleEntry_Object = MibTableRow
hh3cDhcpServer2RuleEntry = _Hh3cDhcpServer2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 9, 1)
)
hh3cDhcpServer2RuleEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2ClassName"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2RuleNumber"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleEntry.setStatus("current")


class _Hh3cDhcpServer2RuleNumber_Type(Integer32):
    """Custom type hh3cDhcpServer2RuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cDhcpServer2RuleNumber_Type.__name__ = "Integer32"
_Hh3cDhcpServer2RuleNumber_Object = MibTableColumn
hh3cDhcpServer2RuleNumber = _Hh3cDhcpServer2RuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 9, 1, 1),
    _Hh3cDhcpServer2RuleNumber_Type()
)
hh3cDhcpServer2RuleNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleNumber.setStatus("current")


class _Hh3cDhcpServer2RuleOptCode_Type(Integer32):
    """Custom type hh3cDhcpServer2RuleOptCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Hh3cDhcpServer2RuleOptCode_Type.__name__ = "Integer32"
_Hh3cDhcpServer2RuleOptCode_Object = MibTableColumn
hh3cDhcpServer2RuleOptCode = _Hh3cDhcpServer2RuleOptCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 9, 1, 2),
    _Hh3cDhcpServer2RuleOptCode_Type()
)
hh3cDhcpServer2RuleOptCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleOptCode.setStatus("current")


class _Hh3cDhcpServer2RuleOptHexStr_Type(OctetString):
    """Custom type hh3cDhcpServer2RuleOptHexStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_Hh3cDhcpServer2RuleOptHexStr_Type.__name__ = "OctetString"
_Hh3cDhcpServer2RuleOptHexStr_Object = MibTableColumn
hh3cDhcpServer2RuleOptHexStr = _Hh3cDhcpServer2RuleOptHexStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 9, 1, 3),
    _Hh3cDhcpServer2RuleOptHexStr_Type()
)
hh3cDhcpServer2RuleOptHexStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleOptHexStr.setStatus("current")


class _Hh3cDhcpServer2RuleOptMask_Type(OctetString):
    """Custom type hh3cDhcpServer2RuleOptMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_Hh3cDhcpServer2RuleOptMask_Type.__name__ = "OctetString"
_Hh3cDhcpServer2RuleOptMask_Object = MibTableColumn
hh3cDhcpServer2RuleOptMask = _Hh3cDhcpServer2RuleOptMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 9, 1, 4),
    _Hh3cDhcpServer2RuleOptMask_Type()
)
hh3cDhcpServer2RuleOptMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleOptMask.setStatus("current")


class _Hh3cDhcpServer2RuleOptOffset_Type(Integer32):
    """Custom type hh3cDhcpServer2RuleOptOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_Hh3cDhcpServer2RuleOptOffset_Type.__name__ = "Integer32"
_Hh3cDhcpServer2RuleOptOffset_Object = MibTableColumn
hh3cDhcpServer2RuleOptOffset = _Hh3cDhcpServer2RuleOptOffset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 9, 1, 5),
    _Hh3cDhcpServer2RuleOptOffset_Type()
)
hh3cDhcpServer2RuleOptOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleOptOffset.setStatus("current")


class _Hh3cDhcpServer2RuleOptLength_Type(Integer32):
    """Custom type hh3cDhcpServer2RuleOptLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cDhcpServer2RuleOptLength_Type.__name__ = "Integer32"
_Hh3cDhcpServer2RuleOptLength_Object = MibTableColumn
hh3cDhcpServer2RuleOptLength = _Hh3cDhcpServer2RuleOptLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 9, 1, 6),
    _Hh3cDhcpServer2RuleOptLength_Type()
)
hh3cDhcpServer2RuleOptLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleOptLength.setStatus("current")
_Hh3cDhcpServer2RuleRowStatus_Type = RowStatus
_Hh3cDhcpServer2RuleRowStatus_Object = MibTableColumn
hh3cDhcpServer2RuleRowStatus = _Hh3cDhcpServer2RuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 9, 1, 7),
    _Hh3cDhcpServer2RuleRowStatus_Type()
)
hh3cDhcpServer2RuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleRowStatus.setStatus("current")
_Hh3cDhcpServer2ForbidTable_Object = MibTable
hh3cDhcpServer2ForbidTable = _Hh3cDhcpServer2ForbidTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 10)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2ForbidTable.setStatus("current")
_Hh3cDhcpServer2ForbidEntry_Object = MibTableRow
hh3cDhcpServer2ForbidEntry = _Hh3cDhcpServer2ForbidEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 10, 1)
)
hh3cDhcpServer2ForbidEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2ForbidVpnName"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2ForbidStart"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2ForbidEnd"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2ForbidEntry.setStatus("current")


class _Hh3cDhcpServer2ForbidVpnName_Type(OctetString):
    """Custom type hh3cDhcpServer2ForbidVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cDhcpServer2ForbidVpnName_Type.__name__ = "OctetString"
_Hh3cDhcpServer2ForbidVpnName_Object = MibTableColumn
hh3cDhcpServer2ForbidVpnName = _Hh3cDhcpServer2ForbidVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 10, 1, 1),
    _Hh3cDhcpServer2ForbidVpnName_Type()
)
hh3cDhcpServer2ForbidVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ForbidVpnName.setStatus("current")
_Hh3cDhcpServer2ForbidStart_Type = InetAddressIPv4
_Hh3cDhcpServer2ForbidStart_Object = MibTableColumn
hh3cDhcpServer2ForbidStart = _Hh3cDhcpServer2ForbidStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 10, 1, 2),
    _Hh3cDhcpServer2ForbidStart_Type()
)
hh3cDhcpServer2ForbidStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ForbidStart.setStatus("current")
_Hh3cDhcpServer2ForbidEnd_Type = InetAddressIPv4
_Hh3cDhcpServer2ForbidEnd_Object = MibTableColumn
hh3cDhcpServer2ForbidEnd = _Hh3cDhcpServer2ForbidEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 10, 1, 3),
    _Hh3cDhcpServer2ForbidEnd_Type()
)
hh3cDhcpServer2ForbidEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ForbidEnd.setStatus("current")
_Hh3cDhcpServer2ForbidRowStatus_Type = RowStatus
_Hh3cDhcpServer2ForbidRowStatus_Object = MibTableColumn
hh3cDhcpServer2ForbidRowStatus = _Hh3cDhcpServer2ForbidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 10, 1, 4),
    _Hh3cDhcpServer2ForbidRowStatus_Type()
)
hh3cDhcpServer2ForbidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ForbidRowStatus.setStatus("current")
_Hh3cDhcpServer2FreeTable_Object = MibTable
hh3cDhcpServer2FreeTable = _Hh3cDhcpServer2FreeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 11)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2FreeTable.setStatus("current")
_Hh3cDhcpServer2FreeEntry_Object = MibTableRow
hh3cDhcpServer2FreeEntry = _Hh3cDhcpServer2FreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 11, 1)
)
hh3cDhcpServer2FreeEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2FreeStart"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2FreeEntry.setStatus("current")
_Hh3cDhcpServer2FreeStart_Type = InetAddressIPv4
_Hh3cDhcpServer2FreeStart_Object = MibTableColumn
hh3cDhcpServer2FreeStart = _Hh3cDhcpServer2FreeStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 11, 1, 1),
    _Hh3cDhcpServer2FreeStart_Type()
)
hh3cDhcpServer2FreeStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2FreeStart.setStatus("current")
_Hh3cDhcpServer2FreeEnd_Type = InetAddressIPv4
_Hh3cDhcpServer2FreeEnd_Object = MibTableColumn
hh3cDhcpServer2FreeEnd = _Hh3cDhcpServer2FreeEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 11, 1, 2),
    _Hh3cDhcpServer2FreeEnd_Type()
)
hh3cDhcpServer2FreeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2FreeEnd.setStatus("current")
_Hh3cDhcpServer2ConflictTable_Object = MibTable
hh3cDhcpServer2ConflictTable = _Hh3cDhcpServer2ConflictTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 12)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2ConflictTable.setStatus("current")
_Hh3cDhcpServer2ConflictEntry_Object = MibTableRow
hh3cDhcpServer2ConflictEntry = _Hh3cDhcpServer2ConflictEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 12, 1)
)
hh3cDhcpServer2ConflictEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2ConflictIP"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2ConflictEntry.setStatus("current")
_Hh3cDhcpServer2ConflictIP_Type = InetAddressIPv4
_Hh3cDhcpServer2ConflictIP_Object = MibTableColumn
hh3cDhcpServer2ConflictIP = _Hh3cDhcpServer2ConflictIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 12, 1, 1),
    _Hh3cDhcpServer2ConflictIP_Type()
)
hh3cDhcpServer2ConflictIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ConflictIP.setStatus("current")


class _Hh3cDhcpServer2ConflictType_Type(Integer32):
    """Custom type hh3cDhcpServer2ConflictType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detectByClient", 2),
          ("detectByServer", 1))
    )


_Hh3cDhcpServer2ConflictType_Type.__name__ = "Integer32"
_Hh3cDhcpServer2ConflictType_Object = MibTableColumn
hh3cDhcpServer2ConflictType = _Hh3cDhcpServer2ConflictType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 12, 1, 2),
    _Hh3cDhcpServer2ConflictType_Type()
)
hh3cDhcpServer2ConflictType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ConflictType.setStatus("current")


class _Hh3cDhcpServer2ConflictTime_Type(OctetString):
    """Custom type hh3cDhcpServer2ConflictTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cDhcpServer2ConflictTime_Type.__name__ = "OctetString"
_Hh3cDhcpServer2ConflictTime_Object = MibTableColumn
hh3cDhcpServer2ConflictTime = _Hh3cDhcpServer2ConflictTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 12, 1, 3),
    _Hh3cDhcpServer2ConflictTime_Type()
)
hh3cDhcpServer2ConflictTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ConflictTime.setStatus("current")
_Hh3cDhcpServer2ConflictRowStatus_Type = RowStatus
_Hh3cDhcpServer2ConflictRowStatus_Object = MibTableColumn
hh3cDhcpServer2ConflictRowStatus = _Hh3cDhcpServer2ConflictRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 12, 1, 4),
    _Hh3cDhcpServer2ConflictRowStatus_Type()
)
hh3cDhcpServer2ConflictRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ConflictRowStatus.setStatus("current")
_Hh3cDhcpServer2ExpiredTable_Object = MibTable
hh3cDhcpServer2ExpiredTable = _Hh3cDhcpServer2ExpiredTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 13)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2ExpiredTable.setStatus("current")
_Hh3cDhcpServer2ExpiredEntry_Object = MibTableRow
hh3cDhcpServer2ExpiredEntry = _Hh3cDhcpServer2ExpiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 13, 1)
)
hh3cDhcpServer2ExpiredEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2ExpiredIP"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2ExpiredEntry.setStatus("current")
_Hh3cDhcpServer2ExpiredIP_Type = InetAddressIPv4
_Hh3cDhcpServer2ExpiredIP_Object = MibTableColumn
hh3cDhcpServer2ExpiredIP = _Hh3cDhcpServer2ExpiredIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 13, 1, 1),
    _Hh3cDhcpServer2ExpiredIP_Type()
)
hh3cDhcpServer2ExpiredIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ExpiredIP.setStatus("current")


class _Hh3cDhcpServer2ExpiredClientId_Type(OctetString):
    """Custom type hh3cDhcpServer2ExpiredClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 254),
    )


_Hh3cDhcpServer2ExpiredClientId_Type.__name__ = "OctetString"
_Hh3cDhcpServer2ExpiredClientId_Object = MibTableColumn
hh3cDhcpServer2ExpiredClientId = _Hh3cDhcpServer2ExpiredClientId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 13, 1, 2),
    _Hh3cDhcpServer2ExpiredClientId_Type()
)
hh3cDhcpServer2ExpiredClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ExpiredClientId.setStatus("current")


class _Hh3cDhcpServer2ExpiredTime_Type(OctetString):
    """Custom type hh3cDhcpServer2ExpiredTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cDhcpServer2ExpiredTime_Type.__name__ = "OctetString"
_Hh3cDhcpServer2ExpiredTime_Object = MibTableColumn
hh3cDhcpServer2ExpiredTime = _Hh3cDhcpServer2ExpiredTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 13, 1, 3),
    _Hh3cDhcpServer2ExpiredTime_Type()
)
hh3cDhcpServer2ExpiredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ExpiredTime.setStatus("current")
_Hh3cDhcpServer2ExpiredRowStatus_Type = RowStatus
_Hh3cDhcpServer2ExpiredRowStatus_Object = MibTableColumn
hh3cDhcpServer2ExpiredRowStatus = _Hh3cDhcpServer2ExpiredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 13, 1, 4),
    _Hh3cDhcpServer2ExpiredRowStatus_Type()
)
hh3cDhcpServer2ExpiredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ExpiredRowStatus.setStatus("current")
_Hh3cDhcpServer2IPInUseTable_Object = MibTable
hh3cDhcpServer2IPInUseTable = _Hh3cDhcpServer2IPInUseTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseTable.setStatus("current")
_Hh3cDhcpServer2IPInUseEntry_Object = MibTableRow
hh3cDhcpServer2IPInUseEntry = _Hh3cDhcpServer2IPInUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14, 1)
)
hh3cDhcpServer2IPInUseEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2IPInUseIP"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseEntry.setStatus("current")
_Hh3cDhcpServer2IPInUseIP_Type = InetAddressIPv4
_Hh3cDhcpServer2IPInUseIP_Object = MibTableColumn
hh3cDhcpServer2IPInUseIP = _Hh3cDhcpServer2IPInUseIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14, 1, 1),
    _Hh3cDhcpServer2IPInUseIP_Type()
)
hh3cDhcpServer2IPInUseIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseIP.setStatus("current")


class _Hh3cDhcpServer2IPInUseClientId_Type(OctetString):
    """Custom type hh3cDhcpServer2IPInUseClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 254),
    )


_Hh3cDhcpServer2IPInUseClientId_Type.__name__ = "OctetString"
_Hh3cDhcpServer2IPInUseClientId_Object = MibTableColumn
hh3cDhcpServer2IPInUseClientId = _Hh3cDhcpServer2IPInUseClientId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14, 1, 2),
    _Hh3cDhcpServer2IPInUseClientId_Type()
)
hh3cDhcpServer2IPInUseClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseClientId.setStatus("current")


class _Hh3cDhcpServer2IPInUseHardAddr_Type(OctetString):
    """Custom type hh3cDhcpServer2IPInUseHardAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 39),
    )


_Hh3cDhcpServer2IPInUseHardAddr_Type.__name__ = "OctetString"
_Hh3cDhcpServer2IPInUseHardAddr_Object = MibTableColumn
hh3cDhcpServer2IPInUseHardAddr = _Hh3cDhcpServer2IPInUseHardAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14, 1, 3),
    _Hh3cDhcpServer2IPInUseHardAddr_Type()
)
hh3cDhcpServer2IPInUseHardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseHardAddr.setStatus("current")


class _Hh3cDhcpServer2IPInUseHardType_Type(Integer32):
    """Custom type hh3cDhcpServer2IPInUseHardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("ethernet", 2),
          ("tokenRing", 3))
    )


_Hh3cDhcpServer2IPInUseHardType_Type.__name__ = "Integer32"
_Hh3cDhcpServer2IPInUseHardType_Object = MibTableColumn
hh3cDhcpServer2IPInUseHardType = _Hh3cDhcpServer2IPInUseHardType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14, 1, 4),
    _Hh3cDhcpServer2IPInUseHardType_Type()
)
hh3cDhcpServer2IPInUseHardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseHardType.setStatus("current")


class _Hh3cDhcpServer2IPInUseVlanId_Type(Unsigned32):
    """Custom type hh3cDhcpServer2IPInUseVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cDhcpServer2IPInUseVlanId_Type.__name__ = "Unsigned32"
_Hh3cDhcpServer2IPInUseVlanId_Object = MibTableColumn
hh3cDhcpServer2IPInUseVlanId = _Hh3cDhcpServer2IPInUseVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14, 1, 5),
    _Hh3cDhcpServer2IPInUseVlanId_Type()
)
hh3cDhcpServer2IPInUseVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseVlanId.setStatus("current")


class _Hh3cDhcpServer2IPInUseEndLease_Type(OctetString):
    """Custom type hh3cDhcpServer2IPInUseEndLease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_Hh3cDhcpServer2IPInUseEndLease_Type.__name__ = "OctetString"
_Hh3cDhcpServer2IPInUseEndLease_Object = MibTableColumn
hh3cDhcpServer2IPInUseEndLease = _Hh3cDhcpServer2IPInUseEndLease_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14, 1, 6),
    _Hh3cDhcpServer2IPInUseEndLease_Type()
)
hh3cDhcpServer2IPInUseEndLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseEndLease.setStatus("current")


class _Hh3cDhcpServer2IPInUseType_Type(Integer32):
    """Custom type hh3cDhcpServer2IPInUseType based on Integer32"""
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
        *(("autoCommitted", 5),
          ("autoOffered", 4),
          ("staticCommitted", 3),
          ("staticOffered", 2),
          ("staticUnallocated", 1))
    )


_Hh3cDhcpServer2IPInUseType_Type.__name__ = "Integer32"
_Hh3cDhcpServer2IPInUseType_Object = MibTableColumn
hh3cDhcpServer2IPInUseType = _Hh3cDhcpServer2IPInUseType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14, 1, 7),
    _Hh3cDhcpServer2IPInUseType_Type()
)
hh3cDhcpServer2IPInUseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseType.setStatus("current")
_Hh3cDhcpServer2IPInUseIfIndex_Type = InterfaceIndexOrZero
_Hh3cDhcpServer2IPInUseIfIndex_Object = MibTableColumn
hh3cDhcpServer2IPInUseIfIndex = _Hh3cDhcpServer2IPInUseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14, 1, 8),
    _Hh3cDhcpServer2IPInUseIfIndex_Type()
)
hh3cDhcpServer2IPInUseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseIfIndex.setStatus("current")
_Hh3cDhcpServer2IPInUseRowStatus_Type = RowStatus
_Hh3cDhcpServer2IPInUseRowStatus_Object = MibTableColumn
hh3cDhcpServer2IPInUseRowStatus = _Hh3cDhcpServer2IPInUseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 14, 1, 9),
    _Hh3cDhcpServer2IPInUseRowStatus_Type()
)
hh3cDhcpServer2IPInUseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2IPInUseRowStatus.setStatus("current")
_Hh3cDhcpServer2DefOptGrpTable_Object = MibTable
hh3cDhcpServer2DefOptGrpTable = _Hh3cDhcpServer2DefOptGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 15)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2DefOptGrpTable.setStatus("current")
_Hh3cDhcpServer2DefOptGrpEntry_Object = MibTableRow
hh3cDhcpServer2DefOptGrpEntry = _Hh3cDhcpServer2DefOptGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 15, 1)
)
hh3cDhcpServer2DefOptGrpEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2DefOptGrpClass"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2DefOptGrpEntry.setStatus("current")


class _Hh3cDhcpServer2DefOptGrpClass_Type(OctetString):
    """Custom type hh3cDhcpServer2DefOptGrpClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDhcpServer2DefOptGrpClass_Type.__name__ = "OctetString"
_Hh3cDhcpServer2DefOptGrpClass_Object = MibTableColumn
hh3cDhcpServer2DefOptGrpClass = _Hh3cDhcpServer2DefOptGrpClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 15, 1, 1),
    _Hh3cDhcpServer2DefOptGrpClass_Type()
)
hh3cDhcpServer2DefOptGrpClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2DefOptGrpClass.setStatus("current")


class _Hh3cDhcpServer2DefOptGrpId_Type(Integer32):
    """Custom type hh3cDhcpServer2DefOptGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_Hh3cDhcpServer2DefOptGrpId_Type.__name__ = "Integer32"
_Hh3cDhcpServer2DefOptGrpId_Object = MibTableColumn
hh3cDhcpServer2DefOptGrpId = _Hh3cDhcpServer2DefOptGrpId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 15, 1, 2),
    _Hh3cDhcpServer2DefOptGrpId_Type()
)
hh3cDhcpServer2DefOptGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2DefOptGrpId.setStatus("current")
_Hh3cDhcpServer2DefOptGrpStatus_Type = RowStatus
_Hh3cDhcpServer2DefOptGrpStatus_Object = MibTableColumn
hh3cDhcpServer2DefOptGrpStatus = _Hh3cDhcpServer2DefOptGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 15, 1, 3),
    _Hh3cDhcpServer2DefOptGrpStatus_Type()
)
hh3cDhcpServer2DefOptGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2DefOptGrpStatus.setStatus("current")
_Hh3cDhcpServer2ValidClassTable_Object = MibTable
hh3cDhcpServer2ValidClassTable = _Hh3cDhcpServer2ValidClassTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 16)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2ValidClassTable.setStatus("current")
_Hh3cDhcpServer2ValidClassEntry_Object = MibTableRow
hh3cDhcpServer2ValidClassEntry = _Hh3cDhcpServer2ValidClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 16, 1)
)
hh3cDhcpServer2ValidClassEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2PoolIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2ValidClassName"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2ValidClassEntry.setStatus("current")


class _Hh3cDhcpServer2ValidClassName_Type(OctetString):
    """Custom type hh3cDhcpServer2ValidClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDhcpServer2ValidClassName_Type.__name__ = "OctetString"
_Hh3cDhcpServer2ValidClassName_Object = MibTableColumn
hh3cDhcpServer2ValidClassName = _Hh3cDhcpServer2ValidClassName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 16, 1, 1),
    _Hh3cDhcpServer2ValidClassName_Type()
)
hh3cDhcpServer2ValidClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ValidClassName.setStatus("current")
_Hh3cDhcpServer2ValidClassStatus_Type = RowStatus
_Hh3cDhcpServer2ValidClassStatus_Object = MibTableColumn
hh3cDhcpServer2ValidClassStatus = _Hh3cDhcpServer2ValidClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 16, 1, 2),
    _Hh3cDhcpServer2ValidClassStatus_Type()
)
hh3cDhcpServer2ValidClassStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2ValidClassStatus.setStatus("current")
_Hh3cDhcpServer2RuleHwAddrTable_Object = MibTable
hh3cDhcpServer2RuleHwAddrTable = _Hh3cDhcpServer2RuleHwAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 17)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleHwAddrTable.setStatus("current")
_Hh3cDhcpServer2RuleHwAddrEntry_Object = MibTableRow
hh3cDhcpServer2RuleHwAddrEntry = _Hh3cDhcpServer2RuleHwAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 17, 1)
)
hh3cDhcpServer2RuleHwAddrEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2ClassName"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2RuleHwAddrNumber"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleHwAddrEntry.setStatus("current")


class _Hh3cDhcpServer2RuleHwAddrNumber_Type(Integer32):
    """Custom type hh3cDhcpServer2RuleHwAddrNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cDhcpServer2RuleHwAddrNumber_Type.__name__ = "Integer32"
_Hh3cDhcpServer2RuleHwAddrNumber_Object = MibTableColumn
hh3cDhcpServer2RuleHwAddrNumber = _Hh3cDhcpServer2RuleHwAddrNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 17, 1, 1),
    _Hh3cDhcpServer2RuleHwAddrNumber_Type()
)
hh3cDhcpServer2RuleHwAddrNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleHwAddrNumber.setStatus("current")


class _Hh3cDhcpServer2RuleHwAddress_Type(OctetString):
    """Custom type hh3cDhcpServer2RuleHwAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 39),
    )


_Hh3cDhcpServer2RuleHwAddress_Type.__name__ = "OctetString"
_Hh3cDhcpServer2RuleHwAddress_Object = MibTableColumn
hh3cDhcpServer2RuleHwAddress = _Hh3cDhcpServer2RuleHwAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 17, 1, 2),
    _Hh3cDhcpServer2RuleHwAddress_Type()
)
hh3cDhcpServer2RuleHwAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleHwAddress.setStatus("current")


class _Hh3cDhcpServer2RuleHwAddrMask_Type(OctetString):
    """Custom type hh3cDhcpServer2RuleHwAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 39),
    )


_Hh3cDhcpServer2RuleHwAddrMask_Type.__name__ = "OctetString"
_Hh3cDhcpServer2RuleHwAddrMask_Object = MibTableColumn
hh3cDhcpServer2RuleHwAddrMask = _Hh3cDhcpServer2RuleHwAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 17, 1, 3),
    _Hh3cDhcpServer2RuleHwAddrMask_Type()
)
hh3cDhcpServer2RuleHwAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleHwAddrMask.setStatus("current")


class _Hh3cDhcpServer2RuleHwAddrType_Type(Integer32):
    """Custom type hh3cDhcpServer2RuleHwAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cDhcpServer2RuleHwAddrType_Type.__name__ = "Integer32"
_Hh3cDhcpServer2RuleHwAddrType_Object = MibTableColumn
hh3cDhcpServer2RuleHwAddrType = _Hh3cDhcpServer2RuleHwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 17, 1, 4),
    _Hh3cDhcpServer2RuleHwAddrType_Type()
)
hh3cDhcpServer2RuleHwAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleHwAddrType.setStatus("current")
_Hh3cDhcpServer2RuleHwAddrStatus_Type = RowStatus
_Hh3cDhcpServer2RuleHwAddrStatus_Object = MibTableColumn
hh3cDhcpServer2RuleHwAddrStatus = _Hh3cDhcpServer2RuleHwAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 17, 1, 5),
    _Hh3cDhcpServer2RuleHwAddrStatus_Type()
)
hh3cDhcpServer2RuleHwAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2RuleHwAddrStatus.setStatus("current")
_Hh3cDhcpServer2OptionGroupTable_Object = MibTable
hh3cDhcpServer2OptionGroupTable = _Hh3cDhcpServer2OptionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 18)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionGroupTable.setStatus("current")
_Hh3cDhcpServer2OptionGroupEntry_Object = MibTableRow
hh3cDhcpServer2OptionGroupEntry = _Hh3cDhcpServer2OptionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 18, 1)
)
hh3cDhcpServer2OptionGroupEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2OptionGroupId"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionGroupEntry.setStatus("current")


class _Hh3cDhcpServer2OptionGroupId_Type(Integer32):
    """Custom type hh3cDhcpServer2OptionGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_Hh3cDhcpServer2OptionGroupId_Type.__name__ = "Integer32"
_Hh3cDhcpServer2OptionGroupId_Object = MibTableColumn
hh3cDhcpServer2OptionGroupId = _Hh3cDhcpServer2OptionGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 18, 1, 1),
    _Hh3cDhcpServer2OptionGroupId_Type()
)
hh3cDhcpServer2OptionGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionGroupId.setStatus("current")
_Hh3cDhcpServer2OptionGroupStatus_Type = RowStatus
_Hh3cDhcpServer2OptionGroupStatus_Object = MibTableColumn
hh3cDhcpServer2OptionGroupStatus = _Hh3cDhcpServer2OptionGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 18, 1, 2),
    _Hh3cDhcpServer2OptionGroupStatus_Type()
)
hh3cDhcpServer2OptionGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionGroupStatus.setStatus("current")
_Hh3cDhcpServer2OptionTable_Object = MibTable
hh3cDhcpServer2OptionTable = _Hh3cDhcpServer2OptionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 19)
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionTable.setStatus("current")
_Hh3cDhcpServer2OptionEntry_Object = MibTableRow
hh3cDhcpServer2OptionEntry = _Hh3cDhcpServer2OptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 19, 1)
)
hh3cDhcpServer2OptionEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2OptionGroupId"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpServer2OptionCode"),
)
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionEntry.setStatus("current")


class _Hh3cDhcpServer2OptionCode_Type(Integer32):
    """Custom type hh3cDhcpServer2OptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_Hh3cDhcpServer2OptionCode_Type.__name__ = "Integer32"
_Hh3cDhcpServer2OptionCode_Object = MibTableColumn
hh3cDhcpServer2OptionCode = _Hh3cDhcpServer2OptionCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 19, 1, 1),
    _Hh3cDhcpServer2OptionCode_Type()
)
hh3cDhcpServer2OptionCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionCode.setStatus("current")


class _Hh3cDhcpServer2OptionType_Type(Integer32):
    """Custom type hh3cDhcpServer2OptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2),
          ("ip", 3))
    )


_Hh3cDhcpServer2OptionType_Type.__name__ = "Integer32"
_Hh3cDhcpServer2OptionType_Object = MibTableColumn
hh3cDhcpServer2OptionType = _Hh3cDhcpServer2OptionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 19, 1, 2),
    _Hh3cDhcpServer2OptionType_Type()
)
hh3cDhcpServer2OptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionType.setStatus("current")


class _Hh3cDhcpServer2OptionAscii_Type(OctetString):
    """Custom type hh3cDhcpServer2OptionAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDhcpServer2OptionAscii_Type.__name__ = "OctetString"
_Hh3cDhcpServer2OptionAscii_Object = MibTableColumn
hh3cDhcpServer2OptionAscii = _Hh3cDhcpServer2OptionAscii_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 19, 1, 3),
    _Hh3cDhcpServer2OptionAscii_Type()
)
hh3cDhcpServer2OptionAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionAscii.setStatus("current")


class _Hh3cDhcpServer2OptionHexStr_Type(OctetString):
    """Custom type hh3cDhcpServer2OptionHexStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_Hh3cDhcpServer2OptionHexStr_Type.__name__ = "OctetString"
_Hh3cDhcpServer2OptionHexStr_Object = MibTableColumn
hh3cDhcpServer2OptionHexStr = _Hh3cDhcpServer2OptionHexStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 19, 1, 4),
    _Hh3cDhcpServer2OptionHexStr_Type()
)
hh3cDhcpServer2OptionHexStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionHexStr.setStatus("current")


class _Hh3cDhcpServer2OptionIPStr_Type(OctetString):
    """Custom type hh3cDhcpServer2OptionIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDhcpServer2OptionIPStr_Type.__name__ = "OctetString"
_Hh3cDhcpServer2OptionIPStr_Object = MibTableColumn
hh3cDhcpServer2OptionIPStr = _Hh3cDhcpServer2OptionIPStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 19, 1, 5),
    _Hh3cDhcpServer2OptionIPStr_Type()
)
hh3cDhcpServer2OptionIPStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionIPStr.setStatus("current")
_Hh3cDhcpServer2OptionRowStatus_Type = RowStatus
_Hh3cDhcpServer2OptionRowStatus_Object = MibTableColumn
hh3cDhcpServer2OptionRowStatus = _Hh3cDhcpServer2OptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 2, 19, 1, 6),
    _Hh3cDhcpServer2OptionRowStatus_Type()
)
hh3cDhcpServer2OptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpServer2OptionRowStatus.setStatus("current")
_Hh3cDhcpRelay2ScalarObjects_ObjectIdentity = ObjectIdentity
hh3cDhcpRelay2ScalarObjects = _Hh3cDhcpRelay2ScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3)
)
_Hh3cDhcpRelay2ConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDhcpRelay2ConfigGroup = _Hh3cDhcpRelay2ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 1)
)


class _Hh3cDhcpRelay2UserInfoRecord_Type(TruthValue):
    """Custom type hh3cDhcpRelay2UserInfoRecord based on TruthValue"""


_Hh3cDhcpRelay2UserInfoRecord_Object = MibScalar
hh3cDhcpRelay2UserInfoRecord = _Hh3cDhcpRelay2UserInfoRecord_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 1, 1),
    _Hh3cDhcpRelay2UserInfoRecord_Type()
)
hh3cDhcpRelay2UserInfoRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2UserInfoRecord.setStatus("current")


class _Hh3cDhcpRelay2UserInfoRefresh_Type(TruthValue):
    """Custom type hh3cDhcpRelay2UserInfoRefresh based on TruthValue"""


_Hh3cDhcpRelay2UserInfoRefresh_Object = MibScalar
hh3cDhcpRelay2UserInfoRefresh = _Hh3cDhcpRelay2UserInfoRefresh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 1, 2),
    _Hh3cDhcpRelay2UserInfoRefresh_Type()
)
hh3cDhcpRelay2UserInfoRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2UserInfoRefresh.setStatus("current")


class _Hh3cDhcpRelay2UserInfoFlushTime_Type(Unsigned32):
    """Custom type hh3cDhcpRelay2UserInfoFlushTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Hh3cDhcpRelay2UserInfoFlushTime_Type.__name__ = "Unsigned32"
_Hh3cDhcpRelay2UserInfoFlushTime_Object = MibScalar
hh3cDhcpRelay2UserInfoFlushTime = _Hh3cDhcpRelay2UserInfoFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 1, 3),
    _Hh3cDhcpRelay2UserInfoFlushTime_Type()
)
hh3cDhcpRelay2UserInfoFlushTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2UserInfoFlushTime.setStatus("current")


class _Hh3cDhcpRelay2ReleaseAddr_Type(OctetString):
    """Custom type hh3cDhcpRelay2ReleaseAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_Hh3cDhcpRelay2ReleaseAddr_Type.__name__ = "OctetString"
_Hh3cDhcpRelay2ReleaseAddr_Object = MibScalar
hh3cDhcpRelay2ReleaseAddr = _Hh3cDhcpRelay2ReleaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 1, 4),
    _Hh3cDhcpRelay2ReleaseAddr_Type()
)
hh3cDhcpRelay2ReleaseAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2ReleaseAddr.setStatus("current")
_Hh3cDhcpRelay2StatisticsGroup_ObjectIdentity = ObjectIdentity
hh3cDhcpRelay2StatisticsGroup = _Hh3cDhcpRelay2StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2)
)
_Hh3cDhcpRelay2RxClientNum_Type = Counter64
_Hh3cDhcpRelay2RxClientNum_Object = MibScalar
hh3cDhcpRelay2RxClientNum = _Hh3cDhcpRelay2RxClientNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 1),
    _Hh3cDhcpRelay2RxClientNum_Type()
)
hh3cDhcpRelay2RxClientNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2RxClientNum.setStatus("current")
_Hh3cDhcpRelay2TxClientNum_Type = Counter64
_Hh3cDhcpRelay2TxClientNum_Object = MibScalar
hh3cDhcpRelay2TxClientNum = _Hh3cDhcpRelay2TxClientNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 2),
    _Hh3cDhcpRelay2TxClientNum_Type()
)
hh3cDhcpRelay2TxClientNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2TxClientNum.setStatus("current")
_Hh3cDhcpRelay2RxServerNum_Type = Counter64
_Hh3cDhcpRelay2RxServerNum_Object = MibScalar
hh3cDhcpRelay2RxServerNum = _Hh3cDhcpRelay2RxServerNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 3),
    _Hh3cDhcpRelay2RxServerNum_Type()
)
hh3cDhcpRelay2RxServerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2RxServerNum.setStatus("current")
_Hh3cDhcpRelay2TxServerNum_Type = Counter64
_Hh3cDhcpRelay2TxServerNum_Object = MibScalar
hh3cDhcpRelay2TxServerNum = _Hh3cDhcpRelay2TxServerNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 4),
    _Hh3cDhcpRelay2TxServerNum_Type()
)
hh3cDhcpRelay2TxServerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2TxServerNum.setStatus("current")
_Hh3cDhcpRelay2BadNum_Type = Counter64
_Hh3cDhcpRelay2BadNum_Object = MibScalar
hh3cDhcpRelay2BadNum = _Hh3cDhcpRelay2BadNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 5),
    _Hh3cDhcpRelay2BadNum_Type()
)
hh3cDhcpRelay2BadNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2BadNum.setStatus("current")
_Hh3cDhcpRelay2BootpRequestNum_Type = Counter64
_Hh3cDhcpRelay2BootpRequestNum_Object = MibScalar
hh3cDhcpRelay2BootpRequestNum = _Hh3cDhcpRelay2BootpRequestNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 6),
    _Hh3cDhcpRelay2BootpRequestNum_Type()
)
hh3cDhcpRelay2BootpRequestNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2BootpRequestNum.setStatus("current")
_Hh3cDhcpRelay2DiscoverNum_Type = Counter64
_Hh3cDhcpRelay2DiscoverNum_Object = MibScalar
hh3cDhcpRelay2DiscoverNum = _Hh3cDhcpRelay2DiscoverNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 7),
    _Hh3cDhcpRelay2DiscoverNum_Type()
)
hh3cDhcpRelay2DiscoverNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2DiscoverNum.setStatus("current")
_Hh3cDhcpRelay2RequestNum_Type = Counter64
_Hh3cDhcpRelay2RequestNum_Object = MibScalar
hh3cDhcpRelay2RequestNum = _Hh3cDhcpRelay2RequestNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 8),
    _Hh3cDhcpRelay2RequestNum_Type()
)
hh3cDhcpRelay2RequestNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2RequestNum.setStatus("current")
_Hh3cDhcpRelay2DeclineNum_Type = Counter64
_Hh3cDhcpRelay2DeclineNum_Object = MibScalar
hh3cDhcpRelay2DeclineNum = _Hh3cDhcpRelay2DeclineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 9),
    _Hh3cDhcpRelay2DeclineNum_Type()
)
hh3cDhcpRelay2DeclineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2DeclineNum.setStatus("current")
_Hh3cDhcpRelay2ReleaseNum_Type = Counter64
_Hh3cDhcpRelay2ReleaseNum_Object = MibScalar
hh3cDhcpRelay2ReleaseNum = _Hh3cDhcpRelay2ReleaseNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 10),
    _Hh3cDhcpRelay2ReleaseNum_Type()
)
hh3cDhcpRelay2ReleaseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2ReleaseNum.setStatus("current")
_Hh3cDhcpRelay2InformNum_Type = Counter64
_Hh3cDhcpRelay2InformNum_Object = MibScalar
hh3cDhcpRelay2InformNum = _Hh3cDhcpRelay2InformNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 11),
    _Hh3cDhcpRelay2InformNum_Type()
)
hh3cDhcpRelay2InformNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2InformNum.setStatus("current")
_Hh3cDhcpRelay2BootpReplyNum_Type = Counter64
_Hh3cDhcpRelay2BootpReplyNum_Object = MibScalar
hh3cDhcpRelay2BootpReplyNum = _Hh3cDhcpRelay2BootpReplyNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 12),
    _Hh3cDhcpRelay2BootpReplyNum_Type()
)
hh3cDhcpRelay2BootpReplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2BootpReplyNum.setStatus("current")
_Hh3cDhcpRelay2OfferNum_Type = Counter64
_Hh3cDhcpRelay2OfferNum_Object = MibScalar
hh3cDhcpRelay2OfferNum = _Hh3cDhcpRelay2OfferNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 13),
    _Hh3cDhcpRelay2OfferNum_Type()
)
hh3cDhcpRelay2OfferNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2OfferNum.setStatus("current")
_Hh3cDhcpRelay2AckNum_Type = Counter64
_Hh3cDhcpRelay2AckNum_Object = MibScalar
hh3cDhcpRelay2AckNum = _Hh3cDhcpRelay2AckNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 14),
    _Hh3cDhcpRelay2AckNum_Type()
)
hh3cDhcpRelay2AckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2AckNum.setStatus("current")
_Hh3cDhcpRelay2NakNum_Type = Counter64
_Hh3cDhcpRelay2NakNum_Object = MibScalar
hh3cDhcpRelay2NakNum = _Hh3cDhcpRelay2NakNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 3, 2, 15),
    _Hh3cDhcpRelay2NakNum_Type()
)
hh3cDhcpRelay2NakNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2NakNum.setStatus("current")
_Hh3cDhcpRelay2Tables_ObjectIdentity = ObjectIdentity
hh3cDhcpRelay2Tables = _Hh3cDhcpRelay2Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4)
)
_Hh3cDhcpRelay2IfConfigTable_Object = MibTable
hh3cDhcpRelay2IfConfigTable = _Hh3cDhcpRelay2IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfConfigTable.setStatus("current")
_Hh3cDhcpRelay2IfConfigEntry_Object = MibTableRow
hh3cDhcpRelay2IfConfigEntry = _Hh3cDhcpRelay2IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1)
)
hh3cDhcpRelay2IfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfConfigEntry.setStatus("current")


class _Hh3cDhcpRelay2IfSelectRelay_Type(TruthValue):
    """Custom type hh3cDhcpRelay2IfSelectRelay based on TruthValue"""


_Hh3cDhcpRelay2IfSelectRelay_Object = MibTableColumn
hh3cDhcpRelay2IfSelectRelay = _Hh3cDhcpRelay2IfSelectRelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 1),
    _Hh3cDhcpRelay2IfSelectRelay_Type()
)
hh3cDhcpRelay2IfSelectRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfSelectRelay.setStatus("current")


class _Hh3cDhcpRelay2IfCheckMac_Type(TruthValue):
    """Custom type hh3cDhcpRelay2IfCheckMac based on TruthValue"""


_Hh3cDhcpRelay2IfCheckMac_Object = MibTableColumn
hh3cDhcpRelay2IfCheckMac = _Hh3cDhcpRelay2IfCheckMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 2),
    _Hh3cDhcpRelay2IfCheckMac_Type()
)
hh3cDhcpRelay2IfCheckMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfCheckMac.setStatus("current")


class _Hh3cDhcpRelay2IfOpt82Enable_Type(TruthValue):
    """Custom type hh3cDhcpRelay2IfOpt82Enable based on TruthValue"""


_Hh3cDhcpRelay2IfOpt82Enable_Object = MibTableColumn
hh3cDhcpRelay2IfOpt82Enable = _Hh3cDhcpRelay2IfOpt82Enable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 3),
    _Hh3cDhcpRelay2IfOpt82Enable_Type()
)
hh3cDhcpRelay2IfOpt82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfOpt82Enable.setStatus("current")


class _Hh3cDhcpRelay2IfOpt82Strategy_Type(Integer32):
    """Custom type hh3cDhcpRelay2IfOpt82Strategy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_Hh3cDhcpRelay2IfOpt82Strategy_Type.__name__ = "Integer32"
_Hh3cDhcpRelay2IfOpt82Strategy_Object = MibTableColumn
hh3cDhcpRelay2IfOpt82Strategy = _Hh3cDhcpRelay2IfOpt82Strategy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 4),
    _Hh3cDhcpRelay2IfOpt82Strategy_Type()
)
hh3cDhcpRelay2IfOpt82Strategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfOpt82Strategy.setStatus("current")


class _Hh3cDhcpRelay2IfOpt82CIDMode_Type(Integer32):
    """Custom type hh3cDhcpRelay2IfOpt82CIDMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("userDefine", 3),
          ("verbose", 2))
    )


_Hh3cDhcpRelay2IfOpt82CIDMode_Type.__name__ = "Integer32"
_Hh3cDhcpRelay2IfOpt82CIDMode_Object = MibTableColumn
hh3cDhcpRelay2IfOpt82CIDMode = _Hh3cDhcpRelay2IfOpt82CIDMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 5),
    _Hh3cDhcpRelay2IfOpt82CIDMode_Type()
)
hh3cDhcpRelay2IfOpt82CIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfOpt82CIDMode.setStatus("current")


class _Hh3cDhcpRelay2IfOpt82CIDNodeType_Type(Integer32):
    """Custom type hh3cDhcpRelay2IfOpt82CIDNodeType based on Integer32"""
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
        *(("invalid", 1),
          ("mac", 2),
          ("sysname", 3),
          ("userDefine", 4))
    )


_Hh3cDhcpRelay2IfOpt82CIDNodeType_Type.__name__ = "Integer32"
_Hh3cDhcpRelay2IfOpt82CIDNodeType_Object = MibTableColumn
hh3cDhcpRelay2IfOpt82CIDNodeType = _Hh3cDhcpRelay2IfOpt82CIDNodeType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 6),
    _Hh3cDhcpRelay2IfOpt82CIDNodeType_Type()
)
hh3cDhcpRelay2IfOpt82CIDNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfOpt82CIDNodeType.setStatus("current")


class _Hh3cDhcpRelay2IfOpt82CIDNodeStr_Type(OctetString):
    """Custom type hh3cDhcpRelay2IfOpt82CIDNodeStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Hh3cDhcpRelay2IfOpt82CIDNodeStr_Type.__name__ = "OctetString"
_Hh3cDhcpRelay2IfOpt82CIDNodeStr_Object = MibTableColumn
hh3cDhcpRelay2IfOpt82CIDNodeStr = _Hh3cDhcpRelay2IfOpt82CIDNodeStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 7),
    _Hh3cDhcpRelay2IfOpt82CIDNodeStr_Type()
)
hh3cDhcpRelay2IfOpt82CIDNodeStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfOpt82CIDNodeStr.setStatus("current")


class _Hh3cDhcpRelay2IfOpt82CIDStr_Type(OctetString):
    """Custom type hh3cDhcpRelay2IfOpt82CIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 63),
    )


_Hh3cDhcpRelay2IfOpt82CIDStr_Type.__name__ = "OctetString"
_Hh3cDhcpRelay2IfOpt82CIDStr_Object = MibTableColumn
hh3cDhcpRelay2IfOpt82CIDStr = _Hh3cDhcpRelay2IfOpt82CIDStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 8),
    _Hh3cDhcpRelay2IfOpt82CIDStr_Type()
)
hh3cDhcpRelay2IfOpt82CIDStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfOpt82CIDStr.setStatus("current")


class _Hh3cDhcpRelay2IfOpt82CIDFormat_Type(Integer32):
    """Custom type hh3cDhcpRelay2IfOpt82CIDFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 1),
          ("undefine", 3))
    )


_Hh3cDhcpRelay2IfOpt82CIDFormat_Type.__name__ = "Integer32"
_Hh3cDhcpRelay2IfOpt82CIDFormat_Object = MibTableColumn
hh3cDhcpRelay2IfOpt82CIDFormat = _Hh3cDhcpRelay2IfOpt82CIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 9),
    _Hh3cDhcpRelay2IfOpt82CIDFormat_Type()
)
hh3cDhcpRelay2IfOpt82CIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfOpt82CIDFormat.setStatus("current")


class _Hh3cDhcpRelay2IfOpt82RIDMode_Type(Integer32):
    """Custom type hh3cDhcpRelay2IfOpt82RIDMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("sysname", 2),
          ("userDefine", 3))
    )


_Hh3cDhcpRelay2IfOpt82RIDMode_Type.__name__ = "Integer32"
_Hh3cDhcpRelay2IfOpt82RIDMode_Object = MibTableColumn
hh3cDhcpRelay2IfOpt82RIDMode = _Hh3cDhcpRelay2IfOpt82RIDMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 10),
    _Hh3cDhcpRelay2IfOpt82RIDMode_Type()
)
hh3cDhcpRelay2IfOpt82RIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfOpt82RIDMode.setStatus("current")


class _Hh3cDhcpRelay2IfOpt82RIDStr_Type(OctetString):
    """Custom type hh3cDhcpRelay2IfOpt82RIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDhcpRelay2IfOpt82RIDStr_Type.__name__ = "OctetString"
_Hh3cDhcpRelay2IfOpt82RIDStr_Object = MibTableColumn
hh3cDhcpRelay2IfOpt82RIDStr = _Hh3cDhcpRelay2IfOpt82RIDStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 11),
    _Hh3cDhcpRelay2IfOpt82RIDStr_Type()
)
hh3cDhcpRelay2IfOpt82RIDStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfOpt82RIDStr.setStatus("current")


class _Hh3cDhcpRelay2IfOpt82RIDFormat_Type(Integer32):
    """Custom type hh3cDhcpRelay2IfOpt82RIDFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 1))
    )


_Hh3cDhcpRelay2IfOpt82RIDFormat_Type.__name__ = "Integer32"
_Hh3cDhcpRelay2IfOpt82RIDFormat_Object = MibTableColumn
hh3cDhcpRelay2IfOpt82RIDFormat = _Hh3cDhcpRelay2IfOpt82RIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 1, 1, 12),
    _Hh3cDhcpRelay2IfOpt82RIDFormat_Type()
)
hh3cDhcpRelay2IfOpt82RIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2IfOpt82RIDFormat.setStatus("current")
_Hh3cDhcpRelay2SrvAddrTable_Object = MibTable
hh3cDhcpRelay2SrvAddrTable = _Hh3cDhcpRelay2SrvAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cDhcpRelay2SrvAddrTable.setStatus("current")
_Hh3cDhcpRelay2SrvAddrEntry_Object = MibTableRow
hh3cDhcpRelay2SrvAddrEntry = _Hh3cDhcpRelay2SrvAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 2, 1)
)
hh3cDhcpRelay2SrvAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpRelay2SrvAddrIP"),
)
if mibBuilder.loadTexts:
    hh3cDhcpRelay2SrvAddrEntry.setStatus("current")
_Hh3cDhcpRelay2SrvAddrIP_Type = InetAddressIPv4
_Hh3cDhcpRelay2SrvAddrIP_Object = MibTableColumn
hh3cDhcpRelay2SrvAddrIP = _Hh3cDhcpRelay2SrvAddrIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 2, 1, 1),
    _Hh3cDhcpRelay2SrvAddrIP_Type()
)
hh3cDhcpRelay2SrvAddrIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2SrvAddrIP.setStatus("current")
_Hh3cDhcpRelay2SrvAddrRowStatus_Type = RowStatus
_Hh3cDhcpRelay2SrvAddrRowStatus_Object = MibTableColumn
hh3cDhcpRelay2SrvAddrRowStatus = _Hh3cDhcpRelay2SrvAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 2, 1, 2),
    _Hh3cDhcpRelay2SrvAddrRowStatus_Type()
)
hh3cDhcpRelay2SrvAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2SrvAddrRowStatus.setStatus("current")
_Hh3cDhcpRelay2UserInfoTable_Object = MibTable
hh3cDhcpRelay2UserInfoTable = _Hh3cDhcpRelay2UserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 3)
)
if mibBuilder.loadTexts:
    hh3cDhcpRelay2UserInfoTable.setStatus("current")
_Hh3cDhcpRelay2UserInfoEntry_Object = MibTableRow
hh3cDhcpRelay2UserInfoEntry = _Hh3cDhcpRelay2UserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 3, 1)
)
hh3cDhcpRelay2UserInfoEntry.setIndexNames(
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpRelay2UserInfoVpnIndex"),
    (0, "HH3C-DHCP4-MIB", "hh3cDhcpRelay2UserInfoIpAddr"),
)
if mibBuilder.loadTexts:
    hh3cDhcpRelay2UserInfoEntry.setStatus("current")


class _Hh3cDhcpRelay2UserInfoVpnIndex_Type(Unsigned32):
    """Custom type hh3cDhcpRelay2UserInfoVpnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cDhcpRelay2UserInfoVpnIndex_Type.__name__ = "Unsigned32"
_Hh3cDhcpRelay2UserInfoVpnIndex_Object = MibTableColumn
hh3cDhcpRelay2UserInfoVpnIndex = _Hh3cDhcpRelay2UserInfoVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 3, 1, 1),
    _Hh3cDhcpRelay2UserInfoVpnIndex_Type()
)
hh3cDhcpRelay2UserInfoVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2UserInfoVpnIndex.setStatus("current")
_Hh3cDhcpRelay2UserInfoIpAddr_Type = InetAddressIPv4
_Hh3cDhcpRelay2UserInfoIpAddr_Object = MibTableColumn
hh3cDhcpRelay2UserInfoIpAddr = _Hh3cDhcpRelay2UserInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 3, 1, 2),
    _Hh3cDhcpRelay2UserInfoIpAddr_Type()
)
hh3cDhcpRelay2UserInfoIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2UserInfoIpAddr.setStatus("current")
_Hh3cDhcpRelay2UserInfoMacAddr_Type = MacAddress
_Hh3cDhcpRelay2UserInfoMacAddr_Object = MibTableColumn
hh3cDhcpRelay2UserInfoMacAddr = _Hh3cDhcpRelay2UserInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 3, 1, 3),
    _Hh3cDhcpRelay2UserInfoMacAddr_Type()
)
hh3cDhcpRelay2UserInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2UserInfoMacAddr.setStatus("current")
_Hh3cDhcpRelay2UserInfoIfIndex_Type = InterfaceIndexOrZero
_Hh3cDhcpRelay2UserInfoIfIndex_Object = MibTableColumn
hh3cDhcpRelay2UserInfoIfIndex = _Hh3cDhcpRelay2UserInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 3, 1, 4),
    _Hh3cDhcpRelay2UserInfoIfIndex_Type()
)
hh3cDhcpRelay2UserInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2UserInfoIfIndex.setStatus("current")
_Hh3cDhcpRelay2UserInfoRowStatus_Type = RowStatus
_Hh3cDhcpRelay2UserInfoRowStatus_Object = MibTableColumn
hh3cDhcpRelay2UserInfoRowStatus = _Hh3cDhcpRelay2UserInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122, 4, 3, 1, 5),
    _Hh3cDhcpRelay2UserInfoRowStatus_Type()
)
hh3cDhcpRelay2UserInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpRelay2UserInfoRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DHCP4-MIB",
    **{"hh3cDhcp4": hh3cDhcp4,
       "hh3cDhcpServer2ScalarObjects": hh3cDhcpServer2ScalarObjects,
       "hh3cDhcpServer2ConfigGroup": hh3cDhcpServer2ConfigGroup,
       "hh3cDhcpServer2Enabled": hh3cDhcpServer2Enabled,
       "hh3cDhcpServer2AlwaysBroadcast": hh3cDhcpServer2AlwaysBroadcast,
       "hh3cDhcpServer2IgnoreBootp": hh3cDhcpServer2IgnoreBootp,
       "hh3cDhcpServer2BootpReplyRfc1048": hh3cDhcpServer2BootpReplyRfc1048,
       "hh3cDhcpServer2Opt82Enabled": hh3cDhcpServer2Opt82Enabled,
       "hh3cDhcpServer2PingNumber": hh3cDhcpServer2PingNumber,
       "hh3cDhcpServer2PingTimeout": hh3cDhcpServer2PingTimeout,
       "hh3cDhcpServer2StatGroup": hh3cDhcpServer2StatGroup,
       "hh3cDhcpServer2BadNum": hh3cDhcpServer2BadNum,
       "hh3cDhcpServer2BootpRequestNum": hh3cDhcpServer2BootpRequestNum,
       "hh3cDhcpServer2DiscoverNum": hh3cDhcpServer2DiscoverNum,
       "hh3cDhcpServer2RequestNum": hh3cDhcpServer2RequestNum,
       "hh3cDhcpServer2DeclineNum": hh3cDhcpServer2DeclineNum,
       "hh3cDhcpServer2ReleaseNum": hh3cDhcpServer2ReleaseNum,
       "hh3cDhcpServer2InformNum": hh3cDhcpServer2InformNum,
       "hh3cDhcpServer2BootpReplyNum": hh3cDhcpServer2BootpReplyNum,
       "hh3cDhcpServer2OfferNum": hh3cDhcpServer2OfferNum,
       "hh3cDhcpServer2AckNum": hh3cDhcpServer2AckNum,
       "hh3cDhcpServer2NakNum": hh3cDhcpServer2NakNum,
       "hh3cDhcpServer2TotalPoolUsage": hh3cDhcpServer2TotalPoolUsage,
       "hh3cDhcpServer2PoolNumber": hh3cDhcpServer2PoolNumber,
       "hh3cDhcpServer2ConflictNum": hh3cDhcpServer2ConflictNum,
       "hh3cDhcpServer2AutoBindNum": hh3cDhcpServer2AutoBindNum,
       "hh3cDhcpServer2ManualBindNum": hh3cDhcpServer2ManualBindNum,
       "hh3cDhcpServer2ExpiredBindNum": hh3cDhcpServer2ExpiredBindNum,
       "hh3cDhcpServer2Tables": hh3cDhcpServer2Tables,
       "hh3cDhcpServer2PoolTable": hh3cDhcpServer2PoolTable,
       "hh3cDhcpServer2PoolEntry": hh3cDhcpServer2PoolEntry,
       "hh3cDhcpServer2PoolIndex": hh3cDhcpServer2PoolIndex,
       "hh3cDhcpServer2PoolName": hh3cDhcpServer2PoolName,
       "hh3cDhcpServer2PoolVpnName": hh3cDhcpServer2PoolVpnName,
       "hh3cDhcpServer2PoolNetwork": hh3cDhcpServer2PoolNetwork,
       "hh3cDhcpServer2PoolNetworkMask": hh3cDhcpServer2PoolNetworkMask,
       "hh3cDhcpServer2PoolStartAddr": hh3cDhcpServer2PoolStartAddr,
       "hh3cDhcpServer2PoolEndAddr": hh3cDhcpServer2PoolEndAddr,
       "hh3cDhcpServer2PoolLeaseDay": hh3cDhcpServer2PoolLeaseDay,
       "hh3cDhcpServer2PoolLeaseHour": hh3cDhcpServer2PoolLeaseHour,
       "hh3cDhcpServer2PoolLeaseMinute": hh3cDhcpServer2PoolLeaseMinute,
       "hh3cDhcpServer2PoolLeaseSecond": hh3cDhcpServer2PoolLeaseSecond,
       "hh3cDhcpServer2PoolLeaseUnlimit": hh3cDhcpServer2PoolLeaseUnlimit,
       "hh3cDhcpServer2PoolLeaseTime": hh3cDhcpServer2PoolLeaseTime,
       "hh3cDhcpServer2PoolDomainName": hh3cDhcpServer2PoolDomainName,
       "hh3cDhcpServer2PoolGatewayIP": hh3cDhcpServer2PoolGatewayIP,
       "hh3cDhcpServer2PoolDNSIP": hh3cDhcpServer2PoolDNSIP,
       "hh3cDhcpServer2PoolPrimaryDNSIP": hh3cDhcpServer2PoolPrimaryDNSIP,
       "hh3cDhcpServer2PoolSecondDNSIP": hh3cDhcpServer2PoolSecondDNSIP,
       "hh3cDhcpServer2PoolNetbiosType": hh3cDhcpServer2PoolNetbiosType,
       "hh3cDhcpServer2PoolNbnsIP": hh3cDhcpServer2PoolNbnsIP,
       "hh3cDhcpServer2PoolBootFileName": hh3cDhcpServer2PoolBootFileName,
       "hh3cDhcpServer2PoolBimsIP": hh3cDhcpServer2PoolBimsIP,
       "hh3cDhcpServer2PoolBimsPort": hh3cDhcpServer2PoolBimsPort,
       "hh3cDhcpServer2PoolBimsKeyStr": hh3cDhcpServer2PoolBimsKeyStr,
       "hh3cDhcpServer2PoolNextServer": hh3cDhcpServer2PoolNextServer,
       "hh3cDhcpServer2PoolTftpDomName": hh3cDhcpServer2PoolTftpDomName,
       "hh3cDhcpServer2PoolTftpIP": hh3cDhcpServer2PoolTftpIP,
       "hh3cDhcpServer2PoolVoiceAsIP": hh3cDhcpServer2PoolVoiceAsIP,
       "hh3cDhcpServer2PoolVoiceFailIP": hh3cDhcpServer2PoolVoiceFailIP,
       "hh3cDhcpServer2PoolVoiceFailStr": hh3cDhcpServer2PoolVoiceFailStr,
       "hh3cDhcpServer2PoolVoiceNCPIP": hh3cDhcpServer2PoolVoiceNCPIP,
       "hh3cDhcpServer2PoolVoiceVlanId": hh3cDhcpServer2PoolVoiceVlanId,
       "hh3cDhcpServer2PoolVoiceVlanEnbl": hh3cDhcpServer2PoolVoiceVlanEnbl,
       "hh3cDhcpServer2PoolRowStatus": hh3cDhcpServer2PoolRowStatus,
       "hh3cDhcpServer2PoolVerifyClass": hh3cDhcpServer2PoolVerifyClass,
       "hh3cDhcpServer2IfApplyPoolTable": hh3cDhcpServer2IfApplyPoolTable,
       "hh3cDhcpServer2IfApplyPoolEntry": hh3cDhcpServer2IfApplyPoolEntry,
       "hh3cDhcpServer2IfApplyPoolName": hh3cDhcpServer2IfApplyPoolName,
       "hh3cDhcpServer2PoolSecNwTable": hh3cDhcpServer2PoolSecNwTable,
       "hh3cDhcpServer2PoolSecNwEntry": hh3cDhcpServer2PoolSecNwEntry,
       "hh3cDhcpServer2PoolSecNw": hh3cDhcpServer2PoolSecNw,
       "hh3cDhcpServer2PoolSecNwMask": hh3cDhcpServer2PoolSecNwMask,
       "hh3cDhcpServer2PoolSecNwGwIP": hh3cDhcpServer2PoolSecNwGwIP,
       "hh3cDhcpServer2PoolSecNwStatus": hh3cDhcpServer2PoolSecNwStatus,
       "hh3cDhcpServer2PoolClassTable": hh3cDhcpServer2PoolClassTable,
       "hh3cDhcpServer2PoolClassEntry": hh3cDhcpServer2PoolClassEntry,
       "hh3cDhcpServer2PoolClassName": hh3cDhcpServer2PoolClassName,
       "hh3cDhcpServer2PoolClassStart": hh3cDhcpServer2PoolClassStart,
       "hh3cDhcpServer2PoolClassEnd": hh3cDhcpServer2PoolClassEnd,
       "hh3cDhcpServer2PoolClassStatus": hh3cDhcpServer2PoolClassStatus,
       "hh3cDhcpServer2PoolStaticTable": hh3cDhcpServer2PoolStaticTable,
       "hh3cDhcpServer2PoolStaticEntry": hh3cDhcpServer2PoolStaticEntry,
       "hh3cDhcpServer2PoolStaticIP": hh3cDhcpServer2PoolStaticIP,
       "hh3cDhcpServer2PoolStaticMask": hh3cDhcpServer2PoolStaticMask,
       "hh3cDhcpServer2PoolStaticCID": hh3cDhcpServer2PoolStaticCID,
       "hh3cDhcpServer2PoolStaticHAddr": hh3cDhcpServer2PoolStaticHAddr,
       "hh3cDhcpServer2PoolStaticHType": hh3cDhcpServer2PoolStaticHType,
       "hh3cDhcpServer2PoolStaticStatus": hh3cDhcpServer2PoolStaticStatus,
       "hh3cDhcpServer2PoolOptionTable": hh3cDhcpServer2PoolOptionTable,
       "hh3cDhcpServer2PoolOptionEntry": hh3cDhcpServer2PoolOptionEntry,
       "hh3cDhcpServer2PoolOptCode": hh3cDhcpServer2PoolOptCode,
       "hh3cDhcpServer2PoolOptType": hh3cDhcpServer2PoolOptType,
       "hh3cDhcpServer2PoolOptAscii": hh3cDhcpServer2PoolOptAscii,
       "hh3cDhcpServer2PoolOptHexStr": hh3cDhcpServer2PoolOptHexStr,
       "hh3cDhcpServer2PoolOptIPStr": hh3cDhcpServer2PoolOptIPStr,
       "hh3cDhcpServer2PoolOptRowStatus": hh3cDhcpServer2PoolOptRowStatus,
       "hh3cDhcpServer2PoolForbidTable": hh3cDhcpServer2PoolForbidTable,
       "hh3cDhcpServer2PoolForbidEntry": hh3cDhcpServer2PoolForbidEntry,
       "hh3cDhcpServer2PoolForbidIP": hh3cDhcpServer2PoolForbidIP,
       "hh3cDhcpServer2PoolForbidStatus": hh3cDhcpServer2PoolForbidStatus,
       "hh3cDhcpServer2ClassTable": hh3cDhcpServer2ClassTable,
       "hh3cDhcpServer2ClassEntry": hh3cDhcpServer2ClassEntry,
       "hh3cDhcpServer2ClassName": hh3cDhcpServer2ClassName,
       "hh3cDhcpServer2ClassRowStatus": hh3cDhcpServer2ClassRowStatus,
       "hh3cDhcpServer2RuleTable": hh3cDhcpServer2RuleTable,
       "hh3cDhcpServer2RuleEntry": hh3cDhcpServer2RuleEntry,
       "hh3cDhcpServer2RuleNumber": hh3cDhcpServer2RuleNumber,
       "hh3cDhcpServer2RuleOptCode": hh3cDhcpServer2RuleOptCode,
       "hh3cDhcpServer2RuleOptHexStr": hh3cDhcpServer2RuleOptHexStr,
       "hh3cDhcpServer2RuleOptMask": hh3cDhcpServer2RuleOptMask,
       "hh3cDhcpServer2RuleOptOffset": hh3cDhcpServer2RuleOptOffset,
       "hh3cDhcpServer2RuleOptLength": hh3cDhcpServer2RuleOptLength,
       "hh3cDhcpServer2RuleRowStatus": hh3cDhcpServer2RuleRowStatus,
       "hh3cDhcpServer2ForbidTable": hh3cDhcpServer2ForbidTable,
       "hh3cDhcpServer2ForbidEntry": hh3cDhcpServer2ForbidEntry,
       "hh3cDhcpServer2ForbidVpnName": hh3cDhcpServer2ForbidVpnName,
       "hh3cDhcpServer2ForbidStart": hh3cDhcpServer2ForbidStart,
       "hh3cDhcpServer2ForbidEnd": hh3cDhcpServer2ForbidEnd,
       "hh3cDhcpServer2ForbidRowStatus": hh3cDhcpServer2ForbidRowStatus,
       "hh3cDhcpServer2FreeTable": hh3cDhcpServer2FreeTable,
       "hh3cDhcpServer2FreeEntry": hh3cDhcpServer2FreeEntry,
       "hh3cDhcpServer2FreeStart": hh3cDhcpServer2FreeStart,
       "hh3cDhcpServer2FreeEnd": hh3cDhcpServer2FreeEnd,
       "hh3cDhcpServer2ConflictTable": hh3cDhcpServer2ConflictTable,
       "hh3cDhcpServer2ConflictEntry": hh3cDhcpServer2ConflictEntry,
       "hh3cDhcpServer2ConflictIP": hh3cDhcpServer2ConflictIP,
       "hh3cDhcpServer2ConflictType": hh3cDhcpServer2ConflictType,
       "hh3cDhcpServer2ConflictTime": hh3cDhcpServer2ConflictTime,
       "hh3cDhcpServer2ConflictRowStatus": hh3cDhcpServer2ConflictRowStatus,
       "hh3cDhcpServer2ExpiredTable": hh3cDhcpServer2ExpiredTable,
       "hh3cDhcpServer2ExpiredEntry": hh3cDhcpServer2ExpiredEntry,
       "hh3cDhcpServer2ExpiredIP": hh3cDhcpServer2ExpiredIP,
       "hh3cDhcpServer2ExpiredClientId": hh3cDhcpServer2ExpiredClientId,
       "hh3cDhcpServer2ExpiredTime": hh3cDhcpServer2ExpiredTime,
       "hh3cDhcpServer2ExpiredRowStatus": hh3cDhcpServer2ExpiredRowStatus,
       "hh3cDhcpServer2IPInUseTable": hh3cDhcpServer2IPInUseTable,
       "hh3cDhcpServer2IPInUseEntry": hh3cDhcpServer2IPInUseEntry,
       "hh3cDhcpServer2IPInUseIP": hh3cDhcpServer2IPInUseIP,
       "hh3cDhcpServer2IPInUseClientId": hh3cDhcpServer2IPInUseClientId,
       "hh3cDhcpServer2IPInUseHardAddr": hh3cDhcpServer2IPInUseHardAddr,
       "hh3cDhcpServer2IPInUseHardType": hh3cDhcpServer2IPInUseHardType,
       "hh3cDhcpServer2IPInUseVlanId": hh3cDhcpServer2IPInUseVlanId,
       "hh3cDhcpServer2IPInUseEndLease": hh3cDhcpServer2IPInUseEndLease,
       "hh3cDhcpServer2IPInUseType": hh3cDhcpServer2IPInUseType,
       "hh3cDhcpServer2IPInUseIfIndex": hh3cDhcpServer2IPInUseIfIndex,
       "hh3cDhcpServer2IPInUseRowStatus": hh3cDhcpServer2IPInUseRowStatus,
       "hh3cDhcpServer2DefOptGrpTable": hh3cDhcpServer2DefOptGrpTable,
       "hh3cDhcpServer2DefOptGrpEntry": hh3cDhcpServer2DefOptGrpEntry,
       "hh3cDhcpServer2DefOptGrpClass": hh3cDhcpServer2DefOptGrpClass,
       "hh3cDhcpServer2DefOptGrpId": hh3cDhcpServer2DefOptGrpId,
       "hh3cDhcpServer2DefOptGrpStatus": hh3cDhcpServer2DefOptGrpStatus,
       "hh3cDhcpServer2ValidClassTable": hh3cDhcpServer2ValidClassTable,
       "hh3cDhcpServer2ValidClassEntry": hh3cDhcpServer2ValidClassEntry,
       "hh3cDhcpServer2ValidClassName": hh3cDhcpServer2ValidClassName,
       "hh3cDhcpServer2ValidClassStatus": hh3cDhcpServer2ValidClassStatus,
       "hh3cDhcpServer2RuleHwAddrTable": hh3cDhcpServer2RuleHwAddrTable,
       "hh3cDhcpServer2RuleHwAddrEntry": hh3cDhcpServer2RuleHwAddrEntry,
       "hh3cDhcpServer2RuleHwAddrNumber": hh3cDhcpServer2RuleHwAddrNumber,
       "hh3cDhcpServer2RuleHwAddress": hh3cDhcpServer2RuleHwAddress,
       "hh3cDhcpServer2RuleHwAddrMask": hh3cDhcpServer2RuleHwAddrMask,
       "hh3cDhcpServer2RuleHwAddrType": hh3cDhcpServer2RuleHwAddrType,
       "hh3cDhcpServer2RuleHwAddrStatus": hh3cDhcpServer2RuleHwAddrStatus,
       "hh3cDhcpServer2OptionGroupTable": hh3cDhcpServer2OptionGroupTable,
       "hh3cDhcpServer2OptionGroupEntry": hh3cDhcpServer2OptionGroupEntry,
       "hh3cDhcpServer2OptionGroupId": hh3cDhcpServer2OptionGroupId,
       "hh3cDhcpServer2OptionGroupStatus": hh3cDhcpServer2OptionGroupStatus,
       "hh3cDhcpServer2OptionTable": hh3cDhcpServer2OptionTable,
       "hh3cDhcpServer2OptionEntry": hh3cDhcpServer2OptionEntry,
       "hh3cDhcpServer2OptionCode": hh3cDhcpServer2OptionCode,
       "hh3cDhcpServer2OptionType": hh3cDhcpServer2OptionType,
       "hh3cDhcpServer2OptionAscii": hh3cDhcpServer2OptionAscii,
       "hh3cDhcpServer2OptionHexStr": hh3cDhcpServer2OptionHexStr,
       "hh3cDhcpServer2OptionIPStr": hh3cDhcpServer2OptionIPStr,
       "hh3cDhcpServer2OptionRowStatus": hh3cDhcpServer2OptionRowStatus,
       "hh3cDhcpRelay2ScalarObjects": hh3cDhcpRelay2ScalarObjects,
       "hh3cDhcpRelay2ConfigGroup": hh3cDhcpRelay2ConfigGroup,
       "hh3cDhcpRelay2UserInfoRecord": hh3cDhcpRelay2UserInfoRecord,
       "hh3cDhcpRelay2UserInfoRefresh": hh3cDhcpRelay2UserInfoRefresh,
       "hh3cDhcpRelay2UserInfoFlushTime": hh3cDhcpRelay2UserInfoFlushTime,
       "hh3cDhcpRelay2ReleaseAddr": hh3cDhcpRelay2ReleaseAddr,
       "hh3cDhcpRelay2StatisticsGroup": hh3cDhcpRelay2StatisticsGroup,
       "hh3cDhcpRelay2RxClientNum": hh3cDhcpRelay2RxClientNum,
       "hh3cDhcpRelay2TxClientNum": hh3cDhcpRelay2TxClientNum,
       "hh3cDhcpRelay2RxServerNum": hh3cDhcpRelay2RxServerNum,
       "hh3cDhcpRelay2TxServerNum": hh3cDhcpRelay2TxServerNum,
       "hh3cDhcpRelay2BadNum": hh3cDhcpRelay2BadNum,
       "hh3cDhcpRelay2BootpRequestNum": hh3cDhcpRelay2BootpRequestNum,
       "hh3cDhcpRelay2DiscoverNum": hh3cDhcpRelay2DiscoverNum,
       "hh3cDhcpRelay2RequestNum": hh3cDhcpRelay2RequestNum,
       "hh3cDhcpRelay2DeclineNum": hh3cDhcpRelay2DeclineNum,
       "hh3cDhcpRelay2ReleaseNum": hh3cDhcpRelay2ReleaseNum,
       "hh3cDhcpRelay2InformNum": hh3cDhcpRelay2InformNum,
       "hh3cDhcpRelay2BootpReplyNum": hh3cDhcpRelay2BootpReplyNum,
       "hh3cDhcpRelay2OfferNum": hh3cDhcpRelay2OfferNum,
       "hh3cDhcpRelay2AckNum": hh3cDhcpRelay2AckNum,
       "hh3cDhcpRelay2NakNum": hh3cDhcpRelay2NakNum,
       "hh3cDhcpRelay2Tables": hh3cDhcpRelay2Tables,
       "hh3cDhcpRelay2IfConfigTable": hh3cDhcpRelay2IfConfigTable,
       "hh3cDhcpRelay2IfConfigEntry": hh3cDhcpRelay2IfConfigEntry,
       "hh3cDhcpRelay2IfSelectRelay": hh3cDhcpRelay2IfSelectRelay,
       "hh3cDhcpRelay2IfCheckMac": hh3cDhcpRelay2IfCheckMac,
       "hh3cDhcpRelay2IfOpt82Enable": hh3cDhcpRelay2IfOpt82Enable,
       "hh3cDhcpRelay2IfOpt82Strategy": hh3cDhcpRelay2IfOpt82Strategy,
       "hh3cDhcpRelay2IfOpt82CIDMode": hh3cDhcpRelay2IfOpt82CIDMode,
       "hh3cDhcpRelay2IfOpt82CIDNodeType": hh3cDhcpRelay2IfOpt82CIDNodeType,
       "hh3cDhcpRelay2IfOpt82CIDNodeStr": hh3cDhcpRelay2IfOpt82CIDNodeStr,
       "hh3cDhcpRelay2IfOpt82CIDStr": hh3cDhcpRelay2IfOpt82CIDStr,
       "hh3cDhcpRelay2IfOpt82CIDFormat": hh3cDhcpRelay2IfOpt82CIDFormat,
       "hh3cDhcpRelay2IfOpt82RIDMode": hh3cDhcpRelay2IfOpt82RIDMode,
       "hh3cDhcpRelay2IfOpt82RIDStr": hh3cDhcpRelay2IfOpt82RIDStr,
       "hh3cDhcpRelay2IfOpt82RIDFormat": hh3cDhcpRelay2IfOpt82RIDFormat,
       "hh3cDhcpRelay2SrvAddrTable": hh3cDhcpRelay2SrvAddrTable,
       "hh3cDhcpRelay2SrvAddrEntry": hh3cDhcpRelay2SrvAddrEntry,
       "hh3cDhcpRelay2SrvAddrIP": hh3cDhcpRelay2SrvAddrIP,
       "hh3cDhcpRelay2SrvAddrRowStatus": hh3cDhcpRelay2SrvAddrRowStatus,
       "hh3cDhcpRelay2UserInfoTable": hh3cDhcpRelay2UserInfoTable,
       "hh3cDhcpRelay2UserInfoEntry": hh3cDhcpRelay2UserInfoEntry,
       "hh3cDhcpRelay2UserInfoVpnIndex": hh3cDhcpRelay2UserInfoVpnIndex,
       "hh3cDhcpRelay2UserInfoIpAddr": hh3cDhcpRelay2UserInfoIpAddr,
       "hh3cDhcpRelay2UserInfoMacAddr": hh3cDhcpRelay2UserInfoMacAddr,
       "hh3cDhcpRelay2UserInfoIfIndex": hh3cDhcpRelay2UserInfoIfIndex,
       "hh3cDhcpRelay2UserInfoRowStatus": hh3cDhcpRelay2UserInfoRowStatus}
)
