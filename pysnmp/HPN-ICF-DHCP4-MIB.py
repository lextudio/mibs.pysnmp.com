# SNMP MIB module (HPN-ICF-DHCP4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DHCP4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:40 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfDhcp4 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122)
)
hpnicfDhcp4.setRevisions(
        ("2013-04-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDhcpServer2ScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfDhcpServer2ScalarObjects = _HpnicfDhcpServer2ScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1)
)
_HpnicfDhcpServer2ConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDhcpServer2ConfigGroup = _HpnicfDhcpServer2ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 1)
)


class _HpnicfDhcpServer2Enabled_Type(TruthValue):
    """Custom type hpnicfDhcpServer2Enabled based on TruthValue"""


_HpnicfDhcpServer2Enabled_Object = MibScalar
hpnicfDhcpServer2Enabled = _HpnicfDhcpServer2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 1, 1),
    _HpnicfDhcpServer2Enabled_Type()
)
hpnicfDhcpServer2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2Enabled.setStatus("current")


class _HpnicfDhcpServer2AlwaysBroadcast_Type(TruthValue):
    """Custom type hpnicfDhcpServer2AlwaysBroadcast based on TruthValue"""


_HpnicfDhcpServer2AlwaysBroadcast_Object = MibScalar
hpnicfDhcpServer2AlwaysBroadcast = _HpnicfDhcpServer2AlwaysBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 1, 2),
    _HpnicfDhcpServer2AlwaysBroadcast_Type()
)
hpnicfDhcpServer2AlwaysBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2AlwaysBroadcast.setStatus("current")


class _HpnicfDhcpServer2IgnoreBootp_Type(TruthValue):
    """Custom type hpnicfDhcpServer2IgnoreBootp based on TruthValue"""


_HpnicfDhcpServer2IgnoreBootp_Object = MibScalar
hpnicfDhcpServer2IgnoreBootp = _HpnicfDhcpServer2IgnoreBootp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 1, 3),
    _HpnicfDhcpServer2IgnoreBootp_Type()
)
hpnicfDhcpServer2IgnoreBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IgnoreBootp.setStatus("current")


class _HpnicfDhcpServer2BootpReplyRfc1048_Type(TruthValue):
    """Custom type hpnicfDhcpServer2BootpReplyRfc1048 based on TruthValue"""


_HpnicfDhcpServer2BootpReplyRfc1048_Object = MibScalar
hpnicfDhcpServer2BootpReplyRfc1048 = _HpnicfDhcpServer2BootpReplyRfc1048_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 1, 4),
    _HpnicfDhcpServer2BootpReplyRfc1048_Type()
)
hpnicfDhcpServer2BootpReplyRfc1048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2BootpReplyRfc1048.setStatus("current")


class _HpnicfDhcpServer2Opt82Enabled_Type(TruthValue):
    """Custom type hpnicfDhcpServer2Opt82Enabled based on TruthValue"""


_HpnicfDhcpServer2Opt82Enabled_Object = MibScalar
hpnicfDhcpServer2Opt82Enabled = _HpnicfDhcpServer2Opt82Enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 1, 5),
    _HpnicfDhcpServer2Opt82Enabled_Type()
)
hpnicfDhcpServer2Opt82Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2Opt82Enabled.setStatus("current")


class _HpnicfDhcpServer2PingNumber_Type(Unsigned32):
    """Custom type hpnicfDhcpServer2PingNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HpnicfDhcpServer2PingNumber_Type.__name__ = "Unsigned32"
_HpnicfDhcpServer2PingNumber_Object = MibScalar
hpnicfDhcpServer2PingNumber = _HpnicfDhcpServer2PingNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 1, 6),
    _HpnicfDhcpServer2PingNumber_Type()
)
hpnicfDhcpServer2PingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PingNumber.setStatus("current")


class _HpnicfDhcpServer2PingTimeout_Type(Unsigned32):
    """Custom type hpnicfDhcpServer2PingTimeout based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HpnicfDhcpServer2PingTimeout_Type.__name__ = "Unsigned32"
_HpnicfDhcpServer2PingTimeout_Object = MibScalar
hpnicfDhcpServer2PingTimeout = _HpnicfDhcpServer2PingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 1, 7),
    _HpnicfDhcpServer2PingTimeout_Type()
)
hpnicfDhcpServer2PingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PingTimeout.setStatus("current")
_HpnicfDhcpServer2StatGroup_ObjectIdentity = ObjectIdentity
hpnicfDhcpServer2StatGroup = _HpnicfDhcpServer2StatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2)
)
_HpnicfDhcpServer2BadNum_Type = Counter64
_HpnicfDhcpServer2BadNum_Object = MibScalar
hpnicfDhcpServer2BadNum = _HpnicfDhcpServer2BadNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 1),
    _HpnicfDhcpServer2BadNum_Type()
)
hpnicfDhcpServer2BadNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2BadNum.setStatus("current")
_HpnicfDhcpServer2BootpRequestNum_Type = Counter64
_HpnicfDhcpServer2BootpRequestNum_Object = MibScalar
hpnicfDhcpServer2BootpRequestNum = _HpnicfDhcpServer2BootpRequestNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 2),
    _HpnicfDhcpServer2BootpRequestNum_Type()
)
hpnicfDhcpServer2BootpRequestNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2BootpRequestNum.setStatus("current")
_HpnicfDhcpServer2DiscoverNum_Type = Counter64
_HpnicfDhcpServer2DiscoverNum_Object = MibScalar
hpnicfDhcpServer2DiscoverNum = _HpnicfDhcpServer2DiscoverNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 3),
    _HpnicfDhcpServer2DiscoverNum_Type()
)
hpnicfDhcpServer2DiscoverNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2DiscoverNum.setStatus("current")
_HpnicfDhcpServer2RequestNum_Type = Counter64
_HpnicfDhcpServer2RequestNum_Object = MibScalar
hpnicfDhcpServer2RequestNum = _HpnicfDhcpServer2RequestNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 4),
    _HpnicfDhcpServer2RequestNum_Type()
)
hpnicfDhcpServer2RequestNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RequestNum.setStatus("current")
_HpnicfDhcpServer2DeclineNum_Type = Counter64
_HpnicfDhcpServer2DeclineNum_Object = MibScalar
hpnicfDhcpServer2DeclineNum = _HpnicfDhcpServer2DeclineNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 5),
    _HpnicfDhcpServer2DeclineNum_Type()
)
hpnicfDhcpServer2DeclineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2DeclineNum.setStatus("current")
_HpnicfDhcpServer2ReleaseNum_Type = Counter64
_HpnicfDhcpServer2ReleaseNum_Object = MibScalar
hpnicfDhcpServer2ReleaseNum = _HpnicfDhcpServer2ReleaseNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 6),
    _HpnicfDhcpServer2ReleaseNum_Type()
)
hpnicfDhcpServer2ReleaseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ReleaseNum.setStatus("current")
_HpnicfDhcpServer2InformNum_Type = Counter64
_HpnicfDhcpServer2InformNum_Object = MibScalar
hpnicfDhcpServer2InformNum = _HpnicfDhcpServer2InformNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 7),
    _HpnicfDhcpServer2InformNum_Type()
)
hpnicfDhcpServer2InformNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2InformNum.setStatus("current")
_HpnicfDhcpServer2BootpReplyNum_Type = Counter64
_HpnicfDhcpServer2BootpReplyNum_Object = MibScalar
hpnicfDhcpServer2BootpReplyNum = _HpnicfDhcpServer2BootpReplyNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 8),
    _HpnicfDhcpServer2BootpReplyNum_Type()
)
hpnicfDhcpServer2BootpReplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2BootpReplyNum.setStatus("current")
_HpnicfDhcpServer2OfferNum_Type = Counter64
_HpnicfDhcpServer2OfferNum_Object = MibScalar
hpnicfDhcpServer2OfferNum = _HpnicfDhcpServer2OfferNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 9),
    _HpnicfDhcpServer2OfferNum_Type()
)
hpnicfDhcpServer2OfferNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OfferNum.setStatus("current")
_HpnicfDhcpServer2AckNum_Type = Counter64
_HpnicfDhcpServer2AckNum_Object = MibScalar
hpnicfDhcpServer2AckNum = _HpnicfDhcpServer2AckNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 10),
    _HpnicfDhcpServer2AckNum_Type()
)
hpnicfDhcpServer2AckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2AckNum.setStatus("current")
_HpnicfDhcpServer2NakNum_Type = Counter64
_HpnicfDhcpServer2NakNum_Object = MibScalar
hpnicfDhcpServer2NakNum = _HpnicfDhcpServer2NakNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 11),
    _HpnicfDhcpServer2NakNum_Type()
)
hpnicfDhcpServer2NakNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2NakNum.setStatus("current")


class _HpnicfDhcpServer2TotalPoolUsage_Type(Unsigned32):
    """Custom type hpnicfDhcpServer2TotalPoolUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDhcpServer2TotalPoolUsage_Type.__name__ = "Unsigned32"
_HpnicfDhcpServer2TotalPoolUsage_Object = MibScalar
hpnicfDhcpServer2TotalPoolUsage = _HpnicfDhcpServer2TotalPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 12),
    _HpnicfDhcpServer2TotalPoolUsage_Type()
)
hpnicfDhcpServer2TotalPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2TotalPoolUsage.setStatus("current")
_HpnicfDhcpServer2PoolNumber_Type = Unsigned32
_HpnicfDhcpServer2PoolNumber_Object = MibScalar
hpnicfDhcpServer2PoolNumber = _HpnicfDhcpServer2PoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 13),
    _HpnicfDhcpServer2PoolNumber_Type()
)
hpnicfDhcpServer2PoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolNumber.setStatus("current")
_HpnicfDhcpServer2ConflictNum_Type = Unsigned32
_HpnicfDhcpServer2ConflictNum_Object = MibScalar
hpnicfDhcpServer2ConflictNum = _HpnicfDhcpServer2ConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 14),
    _HpnicfDhcpServer2ConflictNum_Type()
)
hpnicfDhcpServer2ConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ConflictNum.setStatus("current")
_HpnicfDhcpServer2AutoBindNum_Type = Unsigned32
_HpnicfDhcpServer2AutoBindNum_Object = MibScalar
hpnicfDhcpServer2AutoBindNum = _HpnicfDhcpServer2AutoBindNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 15),
    _HpnicfDhcpServer2AutoBindNum_Type()
)
hpnicfDhcpServer2AutoBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2AutoBindNum.setStatus("current")
_HpnicfDhcpServer2ManualBindNum_Type = Unsigned32
_HpnicfDhcpServer2ManualBindNum_Object = MibScalar
hpnicfDhcpServer2ManualBindNum = _HpnicfDhcpServer2ManualBindNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 16),
    _HpnicfDhcpServer2ManualBindNum_Type()
)
hpnicfDhcpServer2ManualBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ManualBindNum.setStatus("current")
_HpnicfDhcpServer2ExpiredBindNum_Type = Unsigned32
_HpnicfDhcpServer2ExpiredBindNum_Object = MibScalar
hpnicfDhcpServer2ExpiredBindNum = _HpnicfDhcpServer2ExpiredBindNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 1, 2, 17),
    _HpnicfDhcpServer2ExpiredBindNum_Type()
)
hpnicfDhcpServer2ExpiredBindNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ExpiredBindNum.setStatus("current")
_HpnicfDhcpServer2Tables_ObjectIdentity = ObjectIdentity
hpnicfDhcpServer2Tables = _HpnicfDhcpServer2Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2)
)
_HpnicfDhcpServer2PoolTable_Object = MibTable
hpnicfDhcpServer2PoolTable = _HpnicfDhcpServer2PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolTable.setStatus("current")
_HpnicfDhcpServer2PoolEntry_Object = MibTableRow
hpnicfDhcpServer2PoolEntry = _HpnicfDhcpServer2PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1)
)
hpnicfDhcpServer2PoolEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolEntry.setStatus("current")


class _HpnicfDhcpServer2PoolIndex_Type(Unsigned32):
    """Custom type hpnicfDhcpServer2PoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfDhcpServer2PoolIndex_Type.__name__ = "Unsigned32"
_HpnicfDhcpServer2PoolIndex_Object = MibTableColumn
hpnicfDhcpServer2PoolIndex = _HpnicfDhcpServer2PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 1),
    _HpnicfDhcpServer2PoolIndex_Type()
)
hpnicfDhcpServer2PoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolIndex.setStatus("current")


class _HpnicfDhcpServer2PoolName_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfDhcpServer2PoolName_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolName_Object = MibTableColumn
hpnicfDhcpServer2PoolName = _HpnicfDhcpServer2PoolName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 2),
    _HpnicfDhcpServer2PoolName_Type()
)
hpnicfDhcpServer2PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolName.setStatus("current")


class _HpnicfDhcpServer2PoolVpnName_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfDhcpServer2PoolVpnName_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolVpnName_Object = MibTableColumn
hpnicfDhcpServer2PoolVpnName = _HpnicfDhcpServer2PoolVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 3),
    _HpnicfDhcpServer2PoolVpnName_Type()
)
hpnicfDhcpServer2PoolVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolVpnName.setStatus("current")
_HpnicfDhcpServer2PoolNetwork_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolNetwork_Object = MibTableColumn
hpnicfDhcpServer2PoolNetwork = _HpnicfDhcpServer2PoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 4),
    _HpnicfDhcpServer2PoolNetwork_Type()
)
hpnicfDhcpServer2PoolNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolNetwork.setStatus("current")
_HpnicfDhcpServer2PoolNetworkMask_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolNetworkMask_Object = MibTableColumn
hpnicfDhcpServer2PoolNetworkMask = _HpnicfDhcpServer2PoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 5),
    _HpnicfDhcpServer2PoolNetworkMask_Type()
)
hpnicfDhcpServer2PoolNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolNetworkMask.setStatus("current")
_HpnicfDhcpServer2PoolStartAddr_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolStartAddr_Object = MibTableColumn
hpnicfDhcpServer2PoolStartAddr = _HpnicfDhcpServer2PoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 6),
    _HpnicfDhcpServer2PoolStartAddr_Type()
)
hpnicfDhcpServer2PoolStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolStartAddr.setStatus("current")
_HpnicfDhcpServer2PoolEndAddr_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolEndAddr_Object = MibTableColumn
hpnicfDhcpServer2PoolEndAddr = _HpnicfDhcpServer2PoolEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 7),
    _HpnicfDhcpServer2PoolEndAddr_Type()
)
hpnicfDhcpServer2PoolEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolEndAddr.setStatus("current")


class _HpnicfDhcpServer2PoolLeaseDay_Type(Integer32):
    """Custom type hpnicfDhcpServer2PoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_HpnicfDhcpServer2PoolLeaseDay_Type.__name__ = "Integer32"
_HpnicfDhcpServer2PoolLeaseDay_Object = MibTableColumn
hpnicfDhcpServer2PoolLeaseDay = _HpnicfDhcpServer2PoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 8),
    _HpnicfDhcpServer2PoolLeaseDay_Type()
)
hpnicfDhcpServer2PoolLeaseDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolLeaseDay.setStatus("current")


class _HpnicfDhcpServer2PoolLeaseHour_Type(Integer32):
    """Custom type hpnicfDhcpServer2PoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_HpnicfDhcpServer2PoolLeaseHour_Type.__name__ = "Integer32"
_HpnicfDhcpServer2PoolLeaseHour_Object = MibTableColumn
hpnicfDhcpServer2PoolLeaseHour = _HpnicfDhcpServer2PoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 9),
    _HpnicfDhcpServer2PoolLeaseHour_Type()
)
hpnicfDhcpServer2PoolLeaseHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolLeaseHour.setStatus("current")


class _HpnicfDhcpServer2PoolLeaseMinute_Type(Integer32):
    """Custom type hpnicfDhcpServer2PoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_HpnicfDhcpServer2PoolLeaseMinute_Type.__name__ = "Integer32"
_HpnicfDhcpServer2PoolLeaseMinute_Object = MibTableColumn
hpnicfDhcpServer2PoolLeaseMinute = _HpnicfDhcpServer2PoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 10),
    _HpnicfDhcpServer2PoolLeaseMinute_Type()
)
hpnicfDhcpServer2PoolLeaseMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolLeaseMinute.setStatus("current")


class _HpnicfDhcpServer2PoolLeaseSecond_Type(Integer32):
    """Custom type hpnicfDhcpServer2PoolLeaseSecond based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_HpnicfDhcpServer2PoolLeaseSecond_Type.__name__ = "Integer32"
_HpnicfDhcpServer2PoolLeaseSecond_Object = MibTableColumn
hpnicfDhcpServer2PoolLeaseSecond = _HpnicfDhcpServer2PoolLeaseSecond_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 11),
    _HpnicfDhcpServer2PoolLeaseSecond_Type()
)
hpnicfDhcpServer2PoolLeaseSecond.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolLeaseSecond.setStatus("current")


class _HpnicfDhcpServer2PoolLeaseUnlimit_Type(TruthValue):
    """Custom type hpnicfDhcpServer2PoolLeaseUnlimit based on TruthValue"""


_HpnicfDhcpServer2PoolLeaseUnlimit_Object = MibTableColumn
hpnicfDhcpServer2PoolLeaseUnlimit = _HpnicfDhcpServer2PoolLeaseUnlimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 12),
    _HpnicfDhcpServer2PoolLeaseUnlimit_Type()
)
hpnicfDhcpServer2PoolLeaseUnlimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolLeaseUnlimit.setStatus("current")
_HpnicfDhcpServer2PoolLeaseTime_Type = TimeTicks
_HpnicfDhcpServer2PoolLeaseTime_Object = MibTableColumn
hpnicfDhcpServer2PoolLeaseTime = _HpnicfDhcpServer2PoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 13),
    _HpnicfDhcpServer2PoolLeaseTime_Type()
)
hpnicfDhcpServer2PoolLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolLeaseTime.setStatus("current")


class _HpnicfDhcpServer2PoolDomainName_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HpnicfDhcpServer2PoolDomainName_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolDomainName_Object = MibTableColumn
hpnicfDhcpServer2PoolDomainName = _HpnicfDhcpServer2PoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 14),
    _HpnicfDhcpServer2PoolDomainName_Type()
)
hpnicfDhcpServer2PoolDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolDomainName.setStatus("current")


class _HpnicfDhcpServer2PoolGatewayIP_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolGatewayIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDhcpServer2PoolGatewayIP_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolGatewayIP_Object = MibTableColumn
hpnicfDhcpServer2PoolGatewayIP = _HpnicfDhcpServer2PoolGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 15),
    _HpnicfDhcpServer2PoolGatewayIP_Type()
)
hpnicfDhcpServer2PoolGatewayIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolGatewayIP.setStatus("current")


class _HpnicfDhcpServer2PoolDNSIP_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolDNSIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDhcpServer2PoolDNSIP_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolDNSIP_Object = MibTableColumn
hpnicfDhcpServer2PoolDNSIP = _HpnicfDhcpServer2PoolDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 16),
    _HpnicfDhcpServer2PoolDNSIP_Type()
)
hpnicfDhcpServer2PoolDNSIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolDNSIP.setStatus("current")
_HpnicfDhcpServer2PoolPrimaryDNSIP_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolPrimaryDNSIP_Object = MibTableColumn
hpnicfDhcpServer2PoolPrimaryDNSIP = _HpnicfDhcpServer2PoolPrimaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 17),
    _HpnicfDhcpServer2PoolPrimaryDNSIP_Type()
)
hpnicfDhcpServer2PoolPrimaryDNSIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolPrimaryDNSIP.setStatus("current")
_HpnicfDhcpServer2PoolSecondDNSIP_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolSecondDNSIP_Object = MibTableColumn
hpnicfDhcpServer2PoolSecondDNSIP = _HpnicfDhcpServer2PoolSecondDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 18),
    _HpnicfDhcpServer2PoolSecondDNSIP_Type()
)
hpnicfDhcpServer2PoolSecondDNSIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolSecondDNSIP.setStatus("current")


class _HpnicfDhcpServer2PoolNetbiosType_Type(Integer32):
    """Custom type hpnicfDhcpServer2PoolNetbiosType based on Integer32"""
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


_HpnicfDhcpServer2PoolNetbiosType_Type.__name__ = "Integer32"
_HpnicfDhcpServer2PoolNetbiosType_Object = MibTableColumn
hpnicfDhcpServer2PoolNetbiosType = _HpnicfDhcpServer2PoolNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 19),
    _HpnicfDhcpServer2PoolNetbiosType_Type()
)
hpnicfDhcpServer2PoolNetbiosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolNetbiosType.setStatus("current")


class _HpnicfDhcpServer2PoolNbnsIP_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolNbnsIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDhcpServer2PoolNbnsIP_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolNbnsIP_Object = MibTableColumn
hpnicfDhcpServer2PoolNbnsIP = _HpnicfDhcpServer2PoolNbnsIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 20),
    _HpnicfDhcpServer2PoolNbnsIP_Type()
)
hpnicfDhcpServer2PoolNbnsIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolNbnsIP.setStatus("current")


class _HpnicfDhcpServer2PoolBootFileName_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolBootFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfDhcpServer2PoolBootFileName_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolBootFileName_Object = MibTableColumn
hpnicfDhcpServer2PoolBootFileName = _HpnicfDhcpServer2PoolBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 21),
    _HpnicfDhcpServer2PoolBootFileName_Type()
)
hpnicfDhcpServer2PoolBootFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolBootFileName.setStatus("current")
_HpnicfDhcpServer2PoolBimsIP_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolBimsIP_Object = MibTableColumn
hpnicfDhcpServer2PoolBimsIP = _HpnicfDhcpServer2PoolBimsIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 22),
    _HpnicfDhcpServer2PoolBimsIP_Type()
)
hpnicfDhcpServer2PoolBimsIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolBimsIP.setStatus("current")


class _HpnicfDhcpServer2PoolBimsPort_Type(Unsigned32):
    """Custom type hpnicfDhcpServer2PoolBimsPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfDhcpServer2PoolBimsPort_Type.__name__ = "Unsigned32"
_HpnicfDhcpServer2PoolBimsPort_Object = MibTableColumn
hpnicfDhcpServer2PoolBimsPort = _HpnicfDhcpServer2PoolBimsPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 23),
    _HpnicfDhcpServer2PoolBimsPort_Type()
)
hpnicfDhcpServer2PoolBimsPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolBimsPort.setStatus("current")


class _HpnicfDhcpServer2PoolBimsKeyStr_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolBimsKeyStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HpnicfDhcpServer2PoolBimsKeyStr_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolBimsKeyStr_Object = MibTableColumn
hpnicfDhcpServer2PoolBimsKeyStr = _HpnicfDhcpServer2PoolBimsKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 24),
    _HpnicfDhcpServer2PoolBimsKeyStr_Type()
)
hpnicfDhcpServer2PoolBimsKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolBimsKeyStr.setStatus("current")
_HpnicfDhcpServer2PoolNextServer_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolNextServer_Object = MibTableColumn
hpnicfDhcpServer2PoolNextServer = _HpnicfDhcpServer2PoolNextServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 25),
    _HpnicfDhcpServer2PoolNextServer_Type()
)
hpnicfDhcpServer2PoolNextServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolNextServer.setStatus("current")


class _HpnicfDhcpServer2PoolTftpDomName_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolTftpDomName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfDhcpServer2PoolTftpDomName_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolTftpDomName_Object = MibTableColumn
hpnicfDhcpServer2PoolTftpDomName = _HpnicfDhcpServer2PoolTftpDomName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 26),
    _HpnicfDhcpServer2PoolTftpDomName_Type()
)
hpnicfDhcpServer2PoolTftpDomName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolTftpDomName.setStatus("current")
_HpnicfDhcpServer2PoolTftpIP_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolTftpIP_Object = MibTableColumn
hpnicfDhcpServer2PoolTftpIP = _HpnicfDhcpServer2PoolTftpIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 27),
    _HpnicfDhcpServer2PoolTftpIP_Type()
)
hpnicfDhcpServer2PoolTftpIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolTftpIP.setStatus("current")
_HpnicfDhcpServer2PoolVoiceAsIP_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolVoiceAsIP_Object = MibTableColumn
hpnicfDhcpServer2PoolVoiceAsIP = _HpnicfDhcpServer2PoolVoiceAsIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 28),
    _HpnicfDhcpServer2PoolVoiceAsIP_Type()
)
hpnicfDhcpServer2PoolVoiceAsIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolVoiceAsIP.setStatus("current")
_HpnicfDhcpServer2PoolVoiceFailIP_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolVoiceFailIP_Object = MibTableColumn
hpnicfDhcpServer2PoolVoiceFailIP = _HpnicfDhcpServer2PoolVoiceFailIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 29),
    _HpnicfDhcpServer2PoolVoiceFailIP_Type()
)
hpnicfDhcpServer2PoolVoiceFailIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolVoiceFailIP.setStatus("current")


class _HpnicfDhcpServer2PoolVoiceFailStr_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolVoiceFailStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_HpnicfDhcpServer2PoolVoiceFailStr_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolVoiceFailStr_Object = MibTableColumn
hpnicfDhcpServer2PoolVoiceFailStr = _HpnicfDhcpServer2PoolVoiceFailStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 30),
    _HpnicfDhcpServer2PoolVoiceFailStr_Type()
)
hpnicfDhcpServer2PoolVoiceFailStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolVoiceFailStr.setStatus("current")
_HpnicfDhcpServer2PoolVoiceNCPIP_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolVoiceNCPIP_Object = MibTableColumn
hpnicfDhcpServer2PoolVoiceNCPIP = _HpnicfDhcpServer2PoolVoiceNCPIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 31),
    _HpnicfDhcpServer2PoolVoiceNCPIP_Type()
)
hpnicfDhcpServer2PoolVoiceNCPIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolVoiceNCPIP.setStatus("current")


class _HpnicfDhcpServer2PoolVoiceVlanId_Type(Unsigned32):
    """Custom type hpnicfDhcpServer2PoolVoiceVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfDhcpServer2PoolVoiceVlanId_Type.__name__ = "Unsigned32"
_HpnicfDhcpServer2PoolVoiceVlanId_Object = MibTableColumn
hpnicfDhcpServer2PoolVoiceVlanId = _HpnicfDhcpServer2PoolVoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 32),
    _HpnicfDhcpServer2PoolVoiceVlanId_Type()
)
hpnicfDhcpServer2PoolVoiceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolVoiceVlanId.setStatus("current")


class _HpnicfDhcpServer2PoolVoiceVlanEnbl_Type(TruthValue):
    """Custom type hpnicfDhcpServer2PoolVoiceVlanEnbl based on TruthValue"""


_HpnicfDhcpServer2PoolVoiceVlanEnbl_Object = MibTableColumn
hpnicfDhcpServer2PoolVoiceVlanEnbl = _HpnicfDhcpServer2PoolVoiceVlanEnbl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 33),
    _HpnicfDhcpServer2PoolVoiceVlanEnbl_Type()
)
hpnicfDhcpServer2PoolVoiceVlanEnbl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolVoiceVlanEnbl.setStatus("current")
_HpnicfDhcpServer2PoolRowStatus_Type = RowStatus
_HpnicfDhcpServer2PoolRowStatus_Object = MibTableColumn
hpnicfDhcpServer2PoolRowStatus = _HpnicfDhcpServer2PoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 34),
    _HpnicfDhcpServer2PoolRowStatus_Type()
)
hpnicfDhcpServer2PoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolRowStatus.setStatus("current")


class _HpnicfDhcpServer2PoolVerifyClass_Type(TruthValue):
    """Custom type hpnicfDhcpServer2PoolVerifyClass based on TruthValue"""


_HpnicfDhcpServer2PoolVerifyClass_Object = MibTableColumn
hpnicfDhcpServer2PoolVerifyClass = _HpnicfDhcpServer2PoolVerifyClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 1, 1, 35),
    _HpnicfDhcpServer2PoolVerifyClass_Type()
)
hpnicfDhcpServer2PoolVerifyClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolVerifyClass.setStatus("current")
_HpnicfDhcpServer2IfApplyPoolTable_Object = MibTable
hpnicfDhcpServer2IfApplyPoolTable = _HpnicfDhcpServer2IfApplyPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IfApplyPoolTable.setStatus("current")
_HpnicfDhcpServer2IfApplyPoolEntry_Object = MibTableRow
hpnicfDhcpServer2IfApplyPoolEntry = _HpnicfDhcpServer2IfApplyPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 2, 1)
)
hpnicfDhcpServer2IfApplyPoolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IfApplyPoolEntry.setStatus("current")


class _HpnicfDhcpServer2IfApplyPoolName_Type(OctetString):
    """Custom type hpnicfDhcpServer2IfApplyPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfDhcpServer2IfApplyPoolName_Type.__name__ = "OctetString"
_HpnicfDhcpServer2IfApplyPoolName_Object = MibTableColumn
hpnicfDhcpServer2IfApplyPoolName = _HpnicfDhcpServer2IfApplyPoolName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 2, 1, 1),
    _HpnicfDhcpServer2IfApplyPoolName_Type()
)
hpnicfDhcpServer2IfApplyPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IfApplyPoolName.setStatus("current")
_HpnicfDhcpServer2PoolSecNwTable_Object = MibTable
hpnicfDhcpServer2PoolSecNwTable = _HpnicfDhcpServer2PoolSecNwTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolSecNwTable.setStatus("current")
_HpnicfDhcpServer2PoolSecNwEntry_Object = MibTableRow
hpnicfDhcpServer2PoolSecNwEntry = _HpnicfDhcpServer2PoolSecNwEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 3, 1)
)
hpnicfDhcpServer2PoolSecNwEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolSecNw"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolSecNwMask"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolSecNwEntry.setStatus("current")
_HpnicfDhcpServer2PoolSecNw_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolSecNw_Object = MibTableColumn
hpnicfDhcpServer2PoolSecNw = _HpnicfDhcpServer2PoolSecNw_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 3, 1, 1),
    _HpnicfDhcpServer2PoolSecNw_Type()
)
hpnicfDhcpServer2PoolSecNw.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolSecNw.setStatus("current")
_HpnicfDhcpServer2PoolSecNwMask_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolSecNwMask_Object = MibTableColumn
hpnicfDhcpServer2PoolSecNwMask = _HpnicfDhcpServer2PoolSecNwMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 3, 1, 2),
    _HpnicfDhcpServer2PoolSecNwMask_Type()
)
hpnicfDhcpServer2PoolSecNwMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolSecNwMask.setStatus("current")


class _HpnicfDhcpServer2PoolSecNwGwIP_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolSecNwGwIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDhcpServer2PoolSecNwGwIP_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolSecNwGwIP_Object = MibTableColumn
hpnicfDhcpServer2PoolSecNwGwIP = _HpnicfDhcpServer2PoolSecNwGwIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 3, 1, 3),
    _HpnicfDhcpServer2PoolSecNwGwIP_Type()
)
hpnicfDhcpServer2PoolSecNwGwIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolSecNwGwIP.setStatus("current")
_HpnicfDhcpServer2PoolSecNwStatus_Type = RowStatus
_HpnicfDhcpServer2PoolSecNwStatus_Object = MibTableColumn
hpnicfDhcpServer2PoolSecNwStatus = _HpnicfDhcpServer2PoolSecNwStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 3, 1, 4),
    _HpnicfDhcpServer2PoolSecNwStatus_Type()
)
hpnicfDhcpServer2PoolSecNwStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolSecNwStatus.setStatus("current")
_HpnicfDhcpServer2PoolClassTable_Object = MibTable
hpnicfDhcpServer2PoolClassTable = _HpnicfDhcpServer2PoolClassTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolClassTable.setStatus("current")
_HpnicfDhcpServer2PoolClassEntry_Object = MibTableRow
hpnicfDhcpServer2PoolClassEntry = _HpnicfDhcpServer2PoolClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 4, 1)
)
hpnicfDhcpServer2PoolClassEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolClassName"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolClassEntry.setStatus("current")


class _HpnicfDhcpServer2PoolClassName_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfDhcpServer2PoolClassName_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolClassName_Object = MibTableColumn
hpnicfDhcpServer2PoolClassName = _HpnicfDhcpServer2PoolClassName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 4, 1, 1),
    _HpnicfDhcpServer2PoolClassName_Type()
)
hpnicfDhcpServer2PoolClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolClassName.setStatus("current")
_HpnicfDhcpServer2PoolClassStart_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolClassStart_Object = MibTableColumn
hpnicfDhcpServer2PoolClassStart = _HpnicfDhcpServer2PoolClassStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 4, 1, 2),
    _HpnicfDhcpServer2PoolClassStart_Type()
)
hpnicfDhcpServer2PoolClassStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolClassStart.setStatus("current")
_HpnicfDhcpServer2PoolClassEnd_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolClassEnd_Object = MibTableColumn
hpnicfDhcpServer2PoolClassEnd = _HpnicfDhcpServer2PoolClassEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 4, 1, 3),
    _HpnicfDhcpServer2PoolClassEnd_Type()
)
hpnicfDhcpServer2PoolClassEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolClassEnd.setStatus("current")
_HpnicfDhcpServer2PoolClassStatus_Type = RowStatus
_HpnicfDhcpServer2PoolClassStatus_Object = MibTableColumn
hpnicfDhcpServer2PoolClassStatus = _HpnicfDhcpServer2PoolClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 4, 1, 4),
    _HpnicfDhcpServer2PoolClassStatus_Type()
)
hpnicfDhcpServer2PoolClassStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolClassStatus.setStatus("current")
_HpnicfDhcpServer2PoolStaticTable_Object = MibTable
hpnicfDhcpServer2PoolStaticTable = _HpnicfDhcpServer2PoolStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolStaticTable.setStatus("current")
_HpnicfDhcpServer2PoolStaticEntry_Object = MibTableRow
hpnicfDhcpServer2PoolStaticEntry = _HpnicfDhcpServer2PoolStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 5, 1)
)
hpnicfDhcpServer2PoolStaticEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolStaticIP"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolStaticEntry.setStatus("current")
_HpnicfDhcpServer2PoolStaticIP_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolStaticIP_Object = MibTableColumn
hpnicfDhcpServer2PoolStaticIP = _HpnicfDhcpServer2PoolStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 5, 1, 1),
    _HpnicfDhcpServer2PoolStaticIP_Type()
)
hpnicfDhcpServer2PoolStaticIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolStaticIP.setStatus("current")
_HpnicfDhcpServer2PoolStaticMask_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolStaticMask_Object = MibTableColumn
hpnicfDhcpServer2PoolStaticMask = _HpnicfDhcpServer2PoolStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 5, 1, 2),
    _HpnicfDhcpServer2PoolStaticMask_Type()
)
hpnicfDhcpServer2PoolStaticMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolStaticMask.setStatus("current")


class _HpnicfDhcpServer2PoolStaticCID_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolStaticCID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 254),
    )


_HpnicfDhcpServer2PoolStaticCID_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolStaticCID_Object = MibTableColumn
hpnicfDhcpServer2PoolStaticCID = _HpnicfDhcpServer2PoolStaticCID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 5, 1, 3),
    _HpnicfDhcpServer2PoolStaticCID_Type()
)
hpnicfDhcpServer2PoolStaticCID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolStaticCID.setStatus("current")


class _HpnicfDhcpServer2PoolStaticHAddr_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolStaticHAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 39),
    )


_HpnicfDhcpServer2PoolStaticHAddr_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolStaticHAddr_Object = MibTableColumn
hpnicfDhcpServer2PoolStaticHAddr = _HpnicfDhcpServer2PoolStaticHAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 5, 1, 4),
    _HpnicfDhcpServer2PoolStaticHAddr_Type()
)
hpnicfDhcpServer2PoolStaticHAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolStaticHAddr.setStatus("current")


class _HpnicfDhcpServer2PoolStaticHType_Type(Integer32):
    """Custom type hpnicfDhcpServer2PoolStaticHType based on Integer32"""
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


_HpnicfDhcpServer2PoolStaticHType_Type.__name__ = "Integer32"
_HpnicfDhcpServer2PoolStaticHType_Object = MibTableColumn
hpnicfDhcpServer2PoolStaticHType = _HpnicfDhcpServer2PoolStaticHType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 5, 1, 5),
    _HpnicfDhcpServer2PoolStaticHType_Type()
)
hpnicfDhcpServer2PoolStaticHType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolStaticHType.setStatus("current")
_HpnicfDhcpServer2PoolStaticStatus_Type = RowStatus
_HpnicfDhcpServer2PoolStaticStatus_Object = MibTableColumn
hpnicfDhcpServer2PoolStaticStatus = _HpnicfDhcpServer2PoolStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 5, 1, 6),
    _HpnicfDhcpServer2PoolStaticStatus_Type()
)
hpnicfDhcpServer2PoolStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolStaticStatus.setStatus("current")
_HpnicfDhcpServer2PoolOptionTable_Object = MibTable
hpnicfDhcpServer2PoolOptionTable = _HpnicfDhcpServer2PoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolOptionTable.setStatus("current")
_HpnicfDhcpServer2PoolOptionEntry_Object = MibTableRow
hpnicfDhcpServer2PoolOptionEntry = _HpnicfDhcpServer2PoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 6, 1)
)
hpnicfDhcpServer2PoolOptionEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolOptCode"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolOptionEntry.setStatus("current")


class _HpnicfDhcpServer2PoolOptCode_Type(Integer32):
    """Custom type hpnicfDhcpServer2PoolOptCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_HpnicfDhcpServer2PoolOptCode_Type.__name__ = "Integer32"
_HpnicfDhcpServer2PoolOptCode_Object = MibTableColumn
hpnicfDhcpServer2PoolOptCode = _HpnicfDhcpServer2PoolOptCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 6, 1, 1),
    _HpnicfDhcpServer2PoolOptCode_Type()
)
hpnicfDhcpServer2PoolOptCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolOptCode.setStatus("current")


class _HpnicfDhcpServer2PoolOptType_Type(Integer32):
    """Custom type hpnicfDhcpServer2PoolOptType based on Integer32"""
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


_HpnicfDhcpServer2PoolOptType_Type.__name__ = "Integer32"
_HpnicfDhcpServer2PoolOptType_Object = MibTableColumn
hpnicfDhcpServer2PoolOptType = _HpnicfDhcpServer2PoolOptType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 6, 1, 2),
    _HpnicfDhcpServer2PoolOptType_Type()
)
hpnicfDhcpServer2PoolOptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolOptType.setStatus("current")


class _HpnicfDhcpServer2PoolOptAscii_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolOptAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDhcpServer2PoolOptAscii_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolOptAscii_Object = MibTableColumn
hpnicfDhcpServer2PoolOptAscii = _HpnicfDhcpServer2PoolOptAscii_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 6, 1, 3),
    _HpnicfDhcpServer2PoolOptAscii_Type()
)
hpnicfDhcpServer2PoolOptAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolOptAscii.setStatus("current")


class _HpnicfDhcpServer2PoolOptHexStr_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolOptHexStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_HpnicfDhcpServer2PoolOptHexStr_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolOptHexStr_Object = MibTableColumn
hpnicfDhcpServer2PoolOptHexStr = _HpnicfDhcpServer2PoolOptHexStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 6, 1, 4),
    _HpnicfDhcpServer2PoolOptHexStr_Type()
)
hpnicfDhcpServer2PoolOptHexStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolOptHexStr.setStatus("current")


class _HpnicfDhcpServer2PoolOptIPStr_Type(OctetString):
    """Custom type hpnicfDhcpServer2PoolOptIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDhcpServer2PoolOptIPStr_Type.__name__ = "OctetString"
_HpnicfDhcpServer2PoolOptIPStr_Object = MibTableColumn
hpnicfDhcpServer2PoolOptIPStr = _HpnicfDhcpServer2PoolOptIPStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 6, 1, 5),
    _HpnicfDhcpServer2PoolOptIPStr_Type()
)
hpnicfDhcpServer2PoolOptIPStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolOptIPStr.setStatus("current")
_HpnicfDhcpServer2PoolOptRowStatus_Type = RowStatus
_HpnicfDhcpServer2PoolOptRowStatus_Object = MibTableColumn
hpnicfDhcpServer2PoolOptRowStatus = _HpnicfDhcpServer2PoolOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 6, 1, 6),
    _HpnicfDhcpServer2PoolOptRowStatus_Type()
)
hpnicfDhcpServer2PoolOptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolOptRowStatus.setStatus("current")
_HpnicfDhcpServer2PoolForbidTable_Object = MibTable
hpnicfDhcpServer2PoolForbidTable = _HpnicfDhcpServer2PoolForbidTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolForbidTable.setStatus("current")
_HpnicfDhcpServer2PoolForbidEntry_Object = MibTableRow
hpnicfDhcpServer2PoolForbidEntry = _HpnicfDhcpServer2PoolForbidEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 7, 1)
)
hpnicfDhcpServer2PoolForbidEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolForbidIP"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolForbidEntry.setStatus("current")
_HpnicfDhcpServer2PoolForbidIP_Type = InetAddressIPv4
_HpnicfDhcpServer2PoolForbidIP_Object = MibTableColumn
hpnicfDhcpServer2PoolForbidIP = _HpnicfDhcpServer2PoolForbidIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 7, 1, 1),
    _HpnicfDhcpServer2PoolForbidIP_Type()
)
hpnicfDhcpServer2PoolForbidIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolForbidIP.setStatus("current")
_HpnicfDhcpServer2PoolForbidStatus_Type = RowStatus
_HpnicfDhcpServer2PoolForbidStatus_Object = MibTableColumn
hpnicfDhcpServer2PoolForbidStatus = _HpnicfDhcpServer2PoolForbidStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 7, 1, 2),
    _HpnicfDhcpServer2PoolForbidStatus_Type()
)
hpnicfDhcpServer2PoolForbidStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2PoolForbidStatus.setStatus("current")
_HpnicfDhcpServer2ClassTable_Object = MibTable
hpnicfDhcpServer2ClassTable = _HpnicfDhcpServer2ClassTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ClassTable.setStatus("current")
_HpnicfDhcpServer2ClassEntry_Object = MibTableRow
hpnicfDhcpServer2ClassEntry = _HpnicfDhcpServer2ClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 8, 1)
)
hpnicfDhcpServer2ClassEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2ClassName"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ClassEntry.setStatus("current")


class _HpnicfDhcpServer2ClassName_Type(OctetString):
    """Custom type hpnicfDhcpServer2ClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfDhcpServer2ClassName_Type.__name__ = "OctetString"
_HpnicfDhcpServer2ClassName_Object = MibTableColumn
hpnicfDhcpServer2ClassName = _HpnicfDhcpServer2ClassName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 8, 1, 1),
    _HpnicfDhcpServer2ClassName_Type()
)
hpnicfDhcpServer2ClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ClassName.setStatus("current")
_HpnicfDhcpServer2ClassRowStatus_Type = RowStatus
_HpnicfDhcpServer2ClassRowStatus_Object = MibTableColumn
hpnicfDhcpServer2ClassRowStatus = _HpnicfDhcpServer2ClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 8, 1, 2),
    _HpnicfDhcpServer2ClassRowStatus_Type()
)
hpnicfDhcpServer2ClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ClassRowStatus.setStatus("current")
_HpnicfDhcpServer2RuleTable_Object = MibTable
hpnicfDhcpServer2RuleTable = _HpnicfDhcpServer2RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 9)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleTable.setStatus("current")
_HpnicfDhcpServer2RuleEntry_Object = MibTableRow
hpnicfDhcpServer2RuleEntry = _HpnicfDhcpServer2RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 9, 1)
)
hpnicfDhcpServer2RuleEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2ClassName"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2RuleNumber"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleEntry.setStatus("current")


class _HpnicfDhcpServer2RuleNumber_Type(Integer32):
    """Custom type hpnicfDhcpServer2RuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfDhcpServer2RuleNumber_Type.__name__ = "Integer32"
_HpnicfDhcpServer2RuleNumber_Object = MibTableColumn
hpnicfDhcpServer2RuleNumber = _HpnicfDhcpServer2RuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 9, 1, 1),
    _HpnicfDhcpServer2RuleNumber_Type()
)
hpnicfDhcpServer2RuleNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleNumber.setStatus("current")


class _HpnicfDhcpServer2RuleOptCode_Type(Integer32):
    """Custom type hpnicfDhcpServer2RuleOptCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HpnicfDhcpServer2RuleOptCode_Type.__name__ = "Integer32"
_HpnicfDhcpServer2RuleOptCode_Object = MibTableColumn
hpnicfDhcpServer2RuleOptCode = _HpnicfDhcpServer2RuleOptCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 9, 1, 2),
    _HpnicfDhcpServer2RuleOptCode_Type()
)
hpnicfDhcpServer2RuleOptCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleOptCode.setStatus("current")


class _HpnicfDhcpServer2RuleOptHexStr_Type(OctetString):
    """Custom type hpnicfDhcpServer2RuleOptHexStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_HpnicfDhcpServer2RuleOptHexStr_Type.__name__ = "OctetString"
_HpnicfDhcpServer2RuleOptHexStr_Object = MibTableColumn
hpnicfDhcpServer2RuleOptHexStr = _HpnicfDhcpServer2RuleOptHexStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 9, 1, 3),
    _HpnicfDhcpServer2RuleOptHexStr_Type()
)
hpnicfDhcpServer2RuleOptHexStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleOptHexStr.setStatus("current")


class _HpnicfDhcpServer2RuleOptMask_Type(OctetString):
    """Custom type hpnicfDhcpServer2RuleOptMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_HpnicfDhcpServer2RuleOptMask_Type.__name__ = "OctetString"
_HpnicfDhcpServer2RuleOptMask_Object = MibTableColumn
hpnicfDhcpServer2RuleOptMask = _HpnicfDhcpServer2RuleOptMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 9, 1, 4),
    _HpnicfDhcpServer2RuleOptMask_Type()
)
hpnicfDhcpServer2RuleOptMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleOptMask.setStatus("current")


class _HpnicfDhcpServer2RuleOptOffset_Type(Integer32):
    """Custom type hpnicfDhcpServer2RuleOptOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_HpnicfDhcpServer2RuleOptOffset_Type.__name__ = "Integer32"
_HpnicfDhcpServer2RuleOptOffset_Object = MibTableColumn
hpnicfDhcpServer2RuleOptOffset = _HpnicfDhcpServer2RuleOptOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 9, 1, 5),
    _HpnicfDhcpServer2RuleOptOffset_Type()
)
hpnicfDhcpServer2RuleOptOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleOptOffset.setStatus("current")


class _HpnicfDhcpServer2RuleOptLength_Type(Integer32):
    """Custom type hpnicfDhcpServer2RuleOptLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfDhcpServer2RuleOptLength_Type.__name__ = "Integer32"
_HpnicfDhcpServer2RuleOptLength_Object = MibTableColumn
hpnicfDhcpServer2RuleOptLength = _HpnicfDhcpServer2RuleOptLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 9, 1, 6),
    _HpnicfDhcpServer2RuleOptLength_Type()
)
hpnicfDhcpServer2RuleOptLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleOptLength.setStatus("current")
_HpnicfDhcpServer2RuleRowStatus_Type = RowStatus
_HpnicfDhcpServer2RuleRowStatus_Object = MibTableColumn
hpnicfDhcpServer2RuleRowStatus = _HpnicfDhcpServer2RuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 9, 1, 7),
    _HpnicfDhcpServer2RuleRowStatus_Type()
)
hpnicfDhcpServer2RuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleRowStatus.setStatus("current")
_HpnicfDhcpServer2ForbidTable_Object = MibTable
hpnicfDhcpServer2ForbidTable = _HpnicfDhcpServer2ForbidTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 10)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ForbidTable.setStatus("current")
_HpnicfDhcpServer2ForbidEntry_Object = MibTableRow
hpnicfDhcpServer2ForbidEntry = _HpnicfDhcpServer2ForbidEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 10, 1)
)
hpnicfDhcpServer2ForbidEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2ForbidVpnName"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2ForbidStart"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2ForbidEnd"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ForbidEntry.setStatus("current")


class _HpnicfDhcpServer2ForbidVpnName_Type(OctetString):
    """Custom type hpnicfDhcpServer2ForbidVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfDhcpServer2ForbidVpnName_Type.__name__ = "OctetString"
_HpnicfDhcpServer2ForbidVpnName_Object = MibTableColumn
hpnicfDhcpServer2ForbidVpnName = _HpnicfDhcpServer2ForbidVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 10, 1, 1),
    _HpnicfDhcpServer2ForbidVpnName_Type()
)
hpnicfDhcpServer2ForbidVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ForbidVpnName.setStatus("current")
_HpnicfDhcpServer2ForbidStart_Type = InetAddressIPv4
_HpnicfDhcpServer2ForbidStart_Object = MibTableColumn
hpnicfDhcpServer2ForbidStart = _HpnicfDhcpServer2ForbidStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 10, 1, 2),
    _HpnicfDhcpServer2ForbidStart_Type()
)
hpnicfDhcpServer2ForbidStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ForbidStart.setStatus("current")
_HpnicfDhcpServer2ForbidEnd_Type = InetAddressIPv4
_HpnicfDhcpServer2ForbidEnd_Object = MibTableColumn
hpnicfDhcpServer2ForbidEnd = _HpnicfDhcpServer2ForbidEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 10, 1, 3),
    _HpnicfDhcpServer2ForbidEnd_Type()
)
hpnicfDhcpServer2ForbidEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ForbidEnd.setStatus("current")
_HpnicfDhcpServer2ForbidRowStatus_Type = RowStatus
_HpnicfDhcpServer2ForbidRowStatus_Object = MibTableColumn
hpnicfDhcpServer2ForbidRowStatus = _HpnicfDhcpServer2ForbidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 10, 1, 4),
    _HpnicfDhcpServer2ForbidRowStatus_Type()
)
hpnicfDhcpServer2ForbidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ForbidRowStatus.setStatus("current")
_HpnicfDhcpServer2FreeTable_Object = MibTable
hpnicfDhcpServer2FreeTable = _HpnicfDhcpServer2FreeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 11)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2FreeTable.setStatus("current")
_HpnicfDhcpServer2FreeEntry_Object = MibTableRow
hpnicfDhcpServer2FreeEntry = _HpnicfDhcpServer2FreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 11, 1)
)
hpnicfDhcpServer2FreeEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2FreeStart"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2FreeEntry.setStatus("current")
_HpnicfDhcpServer2FreeStart_Type = InetAddressIPv4
_HpnicfDhcpServer2FreeStart_Object = MibTableColumn
hpnicfDhcpServer2FreeStart = _HpnicfDhcpServer2FreeStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 11, 1, 1),
    _HpnicfDhcpServer2FreeStart_Type()
)
hpnicfDhcpServer2FreeStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2FreeStart.setStatus("current")
_HpnicfDhcpServer2FreeEnd_Type = InetAddressIPv4
_HpnicfDhcpServer2FreeEnd_Object = MibTableColumn
hpnicfDhcpServer2FreeEnd = _HpnicfDhcpServer2FreeEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 11, 1, 2),
    _HpnicfDhcpServer2FreeEnd_Type()
)
hpnicfDhcpServer2FreeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2FreeEnd.setStatus("current")
_HpnicfDhcpServer2ConflictTable_Object = MibTable
hpnicfDhcpServer2ConflictTable = _HpnicfDhcpServer2ConflictTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 12)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ConflictTable.setStatus("current")
_HpnicfDhcpServer2ConflictEntry_Object = MibTableRow
hpnicfDhcpServer2ConflictEntry = _HpnicfDhcpServer2ConflictEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 12, 1)
)
hpnicfDhcpServer2ConflictEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2ConflictIP"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ConflictEntry.setStatus("current")
_HpnicfDhcpServer2ConflictIP_Type = InetAddressIPv4
_HpnicfDhcpServer2ConflictIP_Object = MibTableColumn
hpnicfDhcpServer2ConflictIP = _HpnicfDhcpServer2ConflictIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 12, 1, 1),
    _HpnicfDhcpServer2ConflictIP_Type()
)
hpnicfDhcpServer2ConflictIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ConflictIP.setStatus("current")


class _HpnicfDhcpServer2ConflictType_Type(Integer32):
    """Custom type hpnicfDhcpServer2ConflictType based on Integer32"""
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


_HpnicfDhcpServer2ConflictType_Type.__name__ = "Integer32"
_HpnicfDhcpServer2ConflictType_Object = MibTableColumn
hpnicfDhcpServer2ConflictType = _HpnicfDhcpServer2ConflictType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 12, 1, 2),
    _HpnicfDhcpServer2ConflictType_Type()
)
hpnicfDhcpServer2ConflictType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ConflictType.setStatus("current")


class _HpnicfDhcpServer2ConflictTime_Type(OctetString):
    """Custom type hpnicfDhcpServer2ConflictTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HpnicfDhcpServer2ConflictTime_Type.__name__ = "OctetString"
_HpnicfDhcpServer2ConflictTime_Object = MibTableColumn
hpnicfDhcpServer2ConflictTime = _HpnicfDhcpServer2ConflictTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 12, 1, 3),
    _HpnicfDhcpServer2ConflictTime_Type()
)
hpnicfDhcpServer2ConflictTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ConflictTime.setStatus("current")
_HpnicfDhcpServer2ConflictRowStatus_Type = RowStatus
_HpnicfDhcpServer2ConflictRowStatus_Object = MibTableColumn
hpnicfDhcpServer2ConflictRowStatus = _HpnicfDhcpServer2ConflictRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 12, 1, 4),
    _HpnicfDhcpServer2ConflictRowStatus_Type()
)
hpnicfDhcpServer2ConflictRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ConflictRowStatus.setStatus("current")
_HpnicfDhcpServer2ExpiredTable_Object = MibTable
hpnicfDhcpServer2ExpiredTable = _HpnicfDhcpServer2ExpiredTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 13)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ExpiredTable.setStatus("current")
_HpnicfDhcpServer2ExpiredEntry_Object = MibTableRow
hpnicfDhcpServer2ExpiredEntry = _HpnicfDhcpServer2ExpiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 13, 1)
)
hpnicfDhcpServer2ExpiredEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2ExpiredIP"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ExpiredEntry.setStatus("current")
_HpnicfDhcpServer2ExpiredIP_Type = InetAddressIPv4
_HpnicfDhcpServer2ExpiredIP_Object = MibTableColumn
hpnicfDhcpServer2ExpiredIP = _HpnicfDhcpServer2ExpiredIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 13, 1, 1),
    _HpnicfDhcpServer2ExpiredIP_Type()
)
hpnicfDhcpServer2ExpiredIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ExpiredIP.setStatus("current")


class _HpnicfDhcpServer2ExpiredClientId_Type(OctetString):
    """Custom type hpnicfDhcpServer2ExpiredClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 254),
    )


_HpnicfDhcpServer2ExpiredClientId_Type.__name__ = "OctetString"
_HpnicfDhcpServer2ExpiredClientId_Object = MibTableColumn
hpnicfDhcpServer2ExpiredClientId = _HpnicfDhcpServer2ExpiredClientId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 13, 1, 2),
    _HpnicfDhcpServer2ExpiredClientId_Type()
)
hpnicfDhcpServer2ExpiredClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ExpiredClientId.setStatus("current")


class _HpnicfDhcpServer2ExpiredTime_Type(OctetString):
    """Custom type hpnicfDhcpServer2ExpiredTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HpnicfDhcpServer2ExpiredTime_Type.__name__ = "OctetString"
_HpnicfDhcpServer2ExpiredTime_Object = MibTableColumn
hpnicfDhcpServer2ExpiredTime = _HpnicfDhcpServer2ExpiredTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 13, 1, 3),
    _HpnicfDhcpServer2ExpiredTime_Type()
)
hpnicfDhcpServer2ExpiredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ExpiredTime.setStatus("current")
_HpnicfDhcpServer2ExpiredRowStatus_Type = RowStatus
_HpnicfDhcpServer2ExpiredRowStatus_Object = MibTableColumn
hpnicfDhcpServer2ExpiredRowStatus = _HpnicfDhcpServer2ExpiredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 13, 1, 4),
    _HpnicfDhcpServer2ExpiredRowStatus_Type()
)
hpnicfDhcpServer2ExpiredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ExpiredRowStatus.setStatus("current")
_HpnicfDhcpServer2IPInUseTable_Object = MibTable
hpnicfDhcpServer2IPInUseTable = _HpnicfDhcpServer2IPInUseTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseTable.setStatus("current")
_HpnicfDhcpServer2IPInUseEntry_Object = MibTableRow
hpnicfDhcpServer2IPInUseEntry = _HpnicfDhcpServer2IPInUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14, 1)
)
hpnicfDhcpServer2IPInUseEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2IPInUseIP"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseEntry.setStatus("current")
_HpnicfDhcpServer2IPInUseIP_Type = InetAddressIPv4
_HpnicfDhcpServer2IPInUseIP_Object = MibTableColumn
hpnicfDhcpServer2IPInUseIP = _HpnicfDhcpServer2IPInUseIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14, 1, 1),
    _HpnicfDhcpServer2IPInUseIP_Type()
)
hpnicfDhcpServer2IPInUseIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseIP.setStatus("current")


class _HpnicfDhcpServer2IPInUseClientId_Type(OctetString):
    """Custom type hpnicfDhcpServer2IPInUseClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 254),
    )


_HpnicfDhcpServer2IPInUseClientId_Type.__name__ = "OctetString"
_HpnicfDhcpServer2IPInUseClientId_Object = MibTableColumn
hpnicfDhcpServer2IPInUseClientId = _HpnicfDhcpServer2IPInUseClientId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14, 1, 2),
    _HpnicfDhcpServer2IPInUseClientId_Type()
)
hpnicfDhcpServer2IPInUseClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseClientId.setStatus("current")


class _HpnicfDhcpServer2IPInUseHardAddr_Type(OctetString):
    """Custom type hpnicfDhcpServer2IPInUseHardAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 39),
    )


_HpnicfDhcpServer2IPInUseHardAddr_Type.__name__ = "OctetString"
_HpnicfDhcpServer2IPInUseHardAddr_Object = MibTableColumn
hpnicfDhcpServer2IPInUseHardAddr = _HpnicfDhcpServer2IPInUseHardAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14, 1, 3),
    _HpnicfDhcpServer2IPInUseHardAddr_Type()
)
hpnicfDhcpServer2IPInUseHardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseHardAddr.setStatus("current")


class _HpnicfDhcpServer2IPInUseHardType_Type(Integer32):
    """Custom type hpnicfDhcpServer2IPInUseHardType based on Integer32"""
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


_HpnicfDhcpServer2IPInUseHardType_Type.__name__ = "Integer32"
_HpnicfDhcpServer2IPInUseHardType_Object = MibTableColumn
hpnicfDhcpServer2IPInUseHardType = _HpnicfDhcpServer2IPInUseHardType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14, 1, 4),
    _HpnicfDhcpServer2IPInUseHardType_Type()
)
hpnicfDhcpServer2IPInUseHardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseHardType.setStatus("current")


class _HpnicfDhcpServer2IPInUseVlanId_Type(Unsigned32):
    """Custom type hpnicfDhcpServer2IPInUseVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfDhcpServer2IPInUseVlanId_Type.__name__ = "Unsigned32"
_HpnicfDhcpServer2IPInUseVlanId_Object = MibTableColumn
hpnicfDhcpServer2IPInUseVlanId = _HpnicfDhcpServer2IPInUseVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14, 1, 5),
    _HpnicfDhcpServer2IPInUseVlanId_Type()
)
hpnicfDhcpServer2IPInUseVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseVlanId.setStatus("current")


class _HpnicfDhcpServer2IPInUseEndLease_Type(OctetString):
    """Custom type hpnicfDhcpServer2IPInUseEndLease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HpnicfDhcpServer2IPInUseEndLease_Type.__name__ = "OctetString"
_HpnicfDhcpServer2IPInUseEndLease_Object = MibTableColumn
hpnicfDhcpServer2IPInUseEndLease = _HpnicfDhcpServer2IPInUseEndLease_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14, 1, 6),
    _HpnicfDhcpServer2IPInUseEndLease_Type()
)
hpnicfDhcpServer2IPInUseEndLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseEndLease.setStatus("current")


class _HpnicfDhcpServer2IPInUseType_Type(Integer32):
    """Custom type hpnicfDhcpServer2IPInUseType based on Integer32"""
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


_HpnicfDhcpServer2IPInUseType_Type.__name__ = "Integer32"
_HpnicfDhcpServer2IPInUseType_Object = MibTableColumn
hpnicfDhcpServer2IPInUseType = _HpnicfDhcpServer2IPInUseType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14, 1, 7),
    _HpnicfDhcpServer2IPInUseType_Type()
)
hpnicfDhcpServer2IPInUseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseType.setStatus("current")
_HpnicfDhcpServer2IPInUseIfIndex_Type = InterfaceIndexOrZero
_HpnicfDhcpServer2IPInUseIfIndex_Object = MibTableColumn
hpnicfDhcpServer2IPInUseIfIndex = _HpnicfDhcpServer2IPInUseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14, 1, 8),
    _HpnicfDhcpServer2IPInUseIfIndex_Type()
)
hpnicfDhcpServer2IPInUseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseIfIndex.setStatus("current")
_HpnicfDhcpServer2IPInUseRowStatus_Type = RowStatus
_HpnicfDhcpServer2IPInUseRowStatus_Object = MibTableColumn
hpnicfDhcpServer2IPInUseRowStatus = _HpnicfDhcpServer2IPInUseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 14, 1, 9),
    _HpnicfDhcpServer2IPInUseRowStatus_Type()
)
hpnicfDhcpServer2IPInUseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2IPInUseRowStatus.setStatus("current")
_HpnicfDhcpServer2DefOptGrpTable_Object = MibTable
hpnicfDhcpServer2DefOptGrpTable = _HpnicfDhcpServer2DefOptGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 15)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2DefOptGrpTable.setStatus("current")
_HpnicfDhcpServer2DefOptGrpEntry_Object = MibTableRow
hpnicfDhcpServer2DefOptGrpEntry = _HpnicfDhcpServer2DefOptGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 15, 1)
)
hpnicfDhcpServer2DefOptGrpEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2DefOptGrpClass"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2DefOptGrpEntry.setStatus("current")


class _HpnicfDhcpServer2DefOptGrpClass_Type(OctetString):
    """Custom type hpnicfDhcpServer2DefOptGrpClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfDhcpServer2DefOptGrpClass_Type.__name__ = "OctetString"
_HpnicfDhcpServer2DefOptGrpClass_Object = MibTableColumn
hpnicfDhcpServer2DefOptGrpClass = _HpnicfDhcpServer2DefOptGrpClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 15, 1, 1),
    _HpnicfDhcpServer2DefOptGrpClass_Type()
)
hpnicfDhcpServer2DefOptGrpClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2DefOptGrpClass.setStatus("current")


class _HpnicfDhcpServer2DefOptGrpId_Type(Integer32):
    """Custom type hpnicfDhcpServer2DefOptGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_HpnicfDhcpServer2DefOptGrpId_Type.__name__ = "Integer32"
_HpnicfDhcpServer2DefOptGrpId_Object = MibTableColumn
hpnicfDhcpServer2DefOptGrpId = _HpnicfDhcpServer2DefOptGrpId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 15, 1, 2),
    _HpnicfDhcpServer2DefOptGrpId_Type()
)
hpnicfDhcpServer2DefOptGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2DefOptGrpId.setStatus("current")
_HpnicfDhcpServer2DefOptGrpStatus_Type = RowStatus
_HpnicfDhcpServer2DefOptGrpStatus_Object = MibTableColumn
hpnicfDhcpServer2DefOptGrpStatus = _HpnicfDhcpServer2DefOptGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 15, 1, 3),
    _HpnicfDhcpServer2DefOptGrpStatus_Type()
)
hpnicfDhcpServer2DefOptGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2DefOptGrpStatus.setStatus("current")
_HpnicfDhcpServer2ValidClassTable_Object = MibTable
hpnicfDhcpServer2ValidClassTable = _HpnicfDhcpServer2ValidClassTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 16)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ValidClassTable.setStatus("current")
_HpnicfDhcpServer2ValidClassEntry_Object = MibTableRow
hpnicfDhcpServer2ValidClassEntry = _HpnicfDhcpServer2ValidClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 16, 1)
)
hpnicfDhcpServer2ValidClassEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2PoolIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2ValidClassName"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ValidClassEntry.setStatus("current")


class _HpnicfDhcpServer2ValidClassName_Type(OctetString):
    """Custom type hpnicfDhcpServer2ValidClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HpnicfDhcpServer2ValidClassName_Type.__name__ = "OctetString"
_HpnicfDhcpServer2ValidClassName_Object = MibTableColumn
hpnicfDhcpServer2ValidClassName = _HpnicfDhcpServer2ValidClassName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 16, 1, 1),
    _HpnicfDhcpServer2ValidClassName_Type()
)
hpnicfDhcpServer2ValidClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ValidClassName.setStatus("current")
_HpnicfDhcpServer2ValidClassStatus_Type = RowStatus
_HpnicfDhcpServer2ValidClassStatus_Object = MibTableColumn
hpnicfDhcpServer2ValidClassStatus = _HpnicfDhcpServer2ValidClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 16, 1, 2),
    _HpnicfDhcpServer2ValidClassStatus_Type()
)
hpnicfDhcpServer2ValidClassStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2ValidClassStatus.setStatus("current")
_HpnicfDhcpServer2RuleHwAddrTable_Object = MibTable
hpnicfDhcpServer2RuleHwAddrTable = _HpnicfDhcpServer2RuleHwAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 17)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleHwAddrTable.setStatus("current")
_HpnicfDhcpServer2RuleHwAddrEntry_Object = MibTableRow
hpnicfDhcpServer2RuleHwAddrEntry = _HpnicfDhcpServer2RuleHwAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 17, 1)
)
hpnicfDhcpServer2RuleHwAddrEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2ClassName"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2RuleHwAddrNumber"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleHwAddrEntry.setStatus("current")


class _HpnicfDhcpServer2RuleHwAddrNumber_Type(Integer32):
    """Custom type hpnicfDhcpServer2RuleHwAddrNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfDhcpServer2RuleHwAddrNumber_Type.__name__ = "Integer32"
_HpnicfDhcpServer2RuleHwAddrNumber_Object = MibTableColumn
hpnicfDhcpServer2RuleHwAddrNumber = _HpnicfDhcpServer2RuleHwAddrNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 17, 1, 1),
    _HpnicfDhcpServer2RuleHwAddrNumber_Type()
)
hpnicfDhcpServer2RuleHwAddrNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleHwAddrNumber.setStatus("current")


class _HpnicfDhcpServer2RuleHwAddress_Type(OctetString):
    """Custom type hpnicfDhcpServer2RuleHwAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 39),
    )


_HpnicfDhcpServer2RuleHwAddress_Type.__name__ = "OctetString"
_HpnicfDhcpServer2RuleHwAddress_Object = MibTableColumn
hpnicfDhcpServer2RuleHwAddress = _HpnicfDhcpServer2RuleHwAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 17, 1, 2),
    _HpnicfDhcpServer2RuleHwAddress_Type()
)
hpnicfDhcpServer2RuleHwAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleHwAddress.setStatus("current")


class _HpnicfDhcpServer2RuleHwAddrMask_Type(OctetString):
    """Custom type hpnicfDhcpServer2RuleHwAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 39),
    )


_HpnicfDhcpServer2RuleHwAddrMask_Type.__name__ = "OctetString"
_HpnicfDhcpServer2RuleHwAddrMask_Object = MibTableColumn
hpnicfDhcpServer2RuleHwAddrMask = _HpnicfDhcpServer2RuleHwAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 17, 1, 3),
    _HpnicfDhcpServer2RuleHwAddrMask_Type()
)
hpnicfDhcpServer2RuleHwAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleHwAddrMask.setStatus("current")


class _HpnicfDhcpServer2RuleHwAddrType_Type(Integer32):
    """Custom type hpnicfDhcpServer2RuleHwAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfDhcpServer2RuleHwAddrType_Type.__name__ = "Integer32"
_HpnicfDhcpServer2RuleHwAddrType_Object = MibTableColumn
hpnicfDhcpServer2RuleHwAddrType = _HpnicfDhcpServer2RuleHwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 17, 1, 4),
    _HpnicfDhcpServer2RuleHwAddrType_Type()
)
hpnicfDhcpServer2RuleHwAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleHwAddrType.setStatus("current")
_HpnicfDhcpServer2RuleHwAddrStatus_Type = RowStatus
_HpnicfDhcpServer2RuleHwAddrStatus_Object = MibTableColumn
hpnicfDhcpServer2RuleHwAddrStatus = _HpnicfDhcpServer2RuleHwAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 17, 1, 5),
    _HpnicfDhcpServer2RuleHwAddrStatus_Type()
)
hpnicfDhcpServer2RuleHwAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2RuleHwAddrStatus.setStatus("current")
_HpnicfDhcpServer2OptionGroupTable_Object = MibTable
hpnicfDhcpServer2OptionGroupTable = _HpnicfDhcpServer2OptionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 18)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionGroupTable.setStatus("current")
_HpnicfDhcpServer2OptionGroupEntry_Object = MibTableRow
hpnicfDhcpServer2OptionGroupEntry = _HpnicfDhcpServer2OptionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 18, 1)
)
hpnicfDhcpServer2OptionGroupEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2OptionGroupId"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionGroupEntry.setStatus("current")


class _HpnicfDhcpServer2OptionGroupId_Type(Integer32):
    """Custom type hpnicfDhcpServer2OptionGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_HpnicfDhcpServer2OptionGroupId_Type.__name__ = "Integer32"
_HpnicfDhcpServer2OptionGroupId_Object = MibTableColumn
hpnicfDhcpServer2OptionGroupId = _HpnicfDhcpServer2OptionGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 18, 1, 1),
    _HpnicfDhcpServer2OptionGroupId_Type()
)
hpnicfDhcpServer2OptionGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionGroupId.setStatus("current")
_HpnicfDhcpServer2OptionGroupStatus_Type = RowStatus
_HpnicfDhcpServer2OptionGroupStatus_Object = MibTableColumn
hpnicfDhcpServer2OptionGroupStatus = _HpnicfDhcpServer2OptionGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 18, 1, 2),
    _HpnicfDhcpServer2OptionGroupStatus_Type()
)
hpnicfDhcpServer2OptionGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionGroupStatus.setStatus("current")
_HpnicfDhcpServer2OptionTable_Object = MibTable
hpnicfDhcpServer2OptionTable = _HpnicfDhcpServer2OptionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 19)
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionTable.setStatus("current")
_HpnicfDhcpServer2OptionEntry_Object = MibTableRow
hpnicfDhcpServer2OptionEntry = _HpnicfDhcpServer2OptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 19, 1)
)
hpnicfDhcpServer2OptionEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2OptionGroupId"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpServer2OptionCode"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionEntry.setStatus("current")


class _HpnicfDhcpServer2OptionCode_Type(Integer32):
    """Custom type hpnicfDhcpServer2OptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_HpnicfDhcpServer2OptionCode_Type.__name__ = "Integer32"
_HpnicfDhcpServer2OptionCode_Object = MibTableColumn
hpnicfDhcpServer2OptionCode = _HpnicfDhcpServer2OptionCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 19, 1, 1),
    _HpnicfDhcpServer2OptionCode_Type()
)
hpnicfDhcpServer2OptionCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionCode.setStatus("current")


class _HpnicfDhcpServer2OptionType_Type(Integer32):
    """Custom type hpnicfDhcpServer2OptionType based on Integer32"""
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


_HpnicfDhcpServer2OptionType_Type.__name__ = "Integer32"
_HpnicfDhcpServer2OptionType_Object = MibTableColumn
hpnicfDhcpServer2OptionType = _HpnicfDhcpServer2OptionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 19, 1, 2),
    _HpnicfDhcpServer2OptionType_Type()
)
hpnicfDhcpServer2OptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionType.setStatus("current")


class _HpnicfDhcpServer2OptionAscii_Type(OctetString):
    """Custom type hpnicfDhcpServer2OptionAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDhcpServer2OptionAscii_Type.__name__ = "OctetString"
_HpnicfDhcpServer2OptionAscii_Object = MibTableColumn
hpnicfDhcpServer2OptionAscii = _HpnicfDhcpServer2OptionAscii_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 19, 1, 3),
    _HpnicfDhcpServer2OptionAscii_Type()
)
hpnicfDhcpServer2OptionAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionAscii.setStatus("current")


class _HpnicfDhcpServer2OptionHexStr_Type(OctetString):
    """Custom type hpnicfDhcpServer2OptionHexStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_HpnicfDhcpServer2OptionHexStr_Type.__name__ = "OctetString"
_HpnicfDhcpServer2OptionHexStr_Object = MibTableColumn
hpnicfDhcpServer2OptionHexStr = _HpnicfDhcpServer2OptionHexStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 19, 1, 4),
    _HpnicfDhcpServer2OptionHexStr_Type()
)
hpnicfDhcpServer2OptionHexStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionHexStr.setStatus("current")


class _HpnicfDhcpServer2OptionIPStr_Type(OctetString):
    """Custom type hpnicfDhcpServer2OptionIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDhcpServer2OptionIPStr_Type.__name__ = "OctetString"
_HpnicfDhcpServer2OptionIPStr_Object = MibTableColumn
hpnicfDhcpServer2OptionIPStr = _HpnicfDhcpServer2OptionIPStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 19, 1, 5),
    _HpnicfDhcpServer2OptionIPStr_Type()
)
hpnicfDhcpServer2OptionIPStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionIPStr.setStatus("current")
_HpnicfDhcpServer2OptionRowStatus_Type = RowStatus
_HpnicfDhcpServer2OptionRowStatus_Object = MibTableColumn
hpnicfDhcpServer2OptionRowStatus = _HpnicfDhcpServer2OptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 2, 19, 1, 6),
    _HpnicfDhcpServer2OptionRowStatus_Type()
)
hpnicfDhcpServer2OptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpServer2OptionRowStatus.setStatus("current")
_HpnicfDhcpRelay2ScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfDhcpRelay2ScalarObjects = _HpnicfDhcpRelay2ScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3)
)
_HpnicfDhcpRelay2ConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDhcpRelay2ConfigGroup = _HpnicfDhcpRelay2ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 1)
)


class _HpnicfDhcpRelay2UserInfoRecord_Type(TruthValue):
    """Custom type hpnicfDhcpRelay2UserInfoRecord based on TruthValue"""


_HpnicfDhcpRelay2UserInfoRecord_Object = MibScalar
hpnicfDhcpRelay2UserInfoRecord = _HpnicfDhcpRelay2UserInfoRecord_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 1, 1),
    _HpnicfDhcpRelay2UserInfoRecord_Type()
)
hpnicfDhcpRelay2UserInfoRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2UserInfoRecord.setStatus("current")


class _HpnicfDhcpRelay2UserInfoRefresh_Type(TruthValue):
    """Custom type hpnicfDhcpRelay2UserInfoRefresh based on TruthValue"""


_HpnicfDhcpRelay2UserInfoRefresh_Object = MibScalar
hpnicfDhcpRelay2UserInfoRefresh = _HpnicfDhcpRelay2UserInfoRefresh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 1, 2),
    _HpnicfDhcpRelay2UserInfoRefresh_Type()
)
hpnicfDhcpRelay2UserInfoRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2UserInfoRefresh.setStatus("current")


class _HpnicfDhcpRelay2UserInfoFlushTime_Type(Unsigned32):
    """Custom type hpnicfDhcpRelay2UserInfoFlushTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HpnicfDhcpRelay2UserInfoFlushTime_Type.__name__ = "Unsigned32"
_HpnicfDhcpRelay2UserInfoFlushTime_Object = MibScalar
hpnicfDhcpRelay2UserInfoFlushTime = _HpnicfDhcpRelay2UserInfoFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 1, 3),
    _HpnicfDhcpRelay2UserInfoFlushTime_Type()
)
hpnicfDhcpRelay2UserInfoFlushTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2UserInfoFlushTime.setStatus("current")


class _HpnicfDhcpRelay2ReleaseAddr_Type(OctetString):
    """Custom type hpnicfDhcpRelay2ReleaseAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HpnicfDhcpRelay2ReleaseAddr_Type.__name__ = "OctetString"
_HpnicfDhcpRelay2ReleaseAddr_Object = MibScalar
hpnicfDhcpRelay2ReleaseAddr = _HpnicfDhcpRelay2ReleaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 1, 4),
    _HpnicfDhcpRelay2ReleaseAddr_Type()
)
hpnicfDhcpRelay2ReleaseAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2ReleaseAddr.setStatus("current")
_HpnicfDhcpRelay2StatisticsGroup_ObjectIdentity = ObjectIdentity
hpnicfDhcpRelay2StatisticsGroup = _HpnicfDhcpRelay2StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2)
)
_HpnicfDhcpRelay2RxClientNum_Type = Counter64
_HpnicfDhcpRelay2RxClientNum_Object = MibScalar
hpnicfDhcpRelay2RxClientNum = _HpnicfDhcpRelay2RxClientNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 1),
    _HpnicfDhcpRelay2RxClientNum_Type()
)
hpnicfDhcpRelay2RxClientNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2RxClientNum.setStatus("current")
_HpnicfDhcpRelay2TxClientNum_Type = Counter64
_HpnicfDhcpRelay2TxClientNum_Object = MibScalar
hpnicfDhcpRelay2TxClientNum = _HpnicfDhcpRelay2TxClientNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 2),
    _HpnicfDhcpRelay2TxClientNum_Type()
)
hpnicfDhcpRelay2TxClientNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2TxClientNum.setStatus("current")
_HpnicfDhcpRelay2RxServerNum_Type = Counter64
_HpnicfDhcpRelay2RxServerNum_Object = MibScalar
hpnicfDhcpRelay2RxServerNum = _HpnicfDhcpRelay2RxServerNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 3),
    _HpnicfDhcpRelay2RxServerNum_Type()
)
hpnicfDhcpRelay2RxServerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2RxServerNum.setStatus("current")
_HpnicfDhcpRelay2TxServerNum_Type = Counter64
_HpnicfDhcpRelay2TxServerNum_Object = MibScalar
hpnicfDhcpRelay2TxServerNum = _HpnicfDhcpRelay2TxServerNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 4),
    _HpnicfDhcpRelay2TxServerNum_Type()
)
hpnicfDhcpRelay2TxServerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2TxServerNum.setStatus("current")
_HpnicfDhcpRelay2BadNum_Type = Counter64
_HpnicfDhcpRelay2BadNum_Object = MibScalar
hpnicfDhcpRelay2BadNum = _HpnicfDhcpRelay2BadNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 5),
    _HpnicfDhcpRelay2BadNum_Type()
)
hpnicfDhcpRelay2BadNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2BadNum.setStatus("current")
_HpnicfDhcpRelay2BootpRequestNum_Type = Counter64
_HpnicfDhcpRelay2BootpRequestNum_Object = MibScalar
hpnicfDhcpRelay2BootpRequestNum = _HpnicfDhcpRelay2BootpRequestNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 6),
    _HpnicfDhcpRelay2BootpRequestNum_Type()
)
hpnicfDhcpRelay2BootpRequestNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2BootpRequestNum.setStatus("current")
_HpnicfDhcpRelay2DiscoverNum_Type = Counter64
_HpnicfDhcpRelay2DiscoverNum_Object = MibScalar
hpnicfDhcpRelay2DiscoverNum = _HpnicfDhcpRelay2DiscoverNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 7),
    _HpnicfDhcpRelay2DiscoverNum_Type()
)
hpnicfDhcpRelay2DiscoverNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2DiscoverNum.setStatus("current")
_HpnicfDhcpRelay2RequestNum_Type = Counter64
_HpnicfDhcpRelay2RequestNum_Object = MibScalar
hpnicfDhcpRelay2RequestNum = _HpnicfDhcpRelay2RequestNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 8),
    _HpnicfDhcpRelay2RequestNum_Type()
)
hpnicfDhcpRelay2RequestNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2RequestNum.setStatus("current")
_HpnicfDhcpRelay2DeclineNum_Type = Counter64
_HpnicfDhcpRelay2DeclineNum_Object = MibScalar
hpnicfDhcpRelay2DeclineNum = _HpnicfDhcpRelay2DeclineNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 9),
    _HpnicfDhcpRelay2DeclineNum_Type()
)
hpnicfDhcpRelay2DeclineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2DeclineNum.setStatus("current")
_HpnicfDhcpRelay2ReleaseNum_Type = Counter64
_HpnicfDhcpRelay2ReleaseNum_Object = MibScalar
hpnicfDhcpRelay2ReleaseNum = _HpnicfDhcpRelay2ReleaseNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 10),
    _HpnicfDhcpRelay2ReleaseNum_Type()
)
hpnicfDhcpRelay2ReleaseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2ReleaseNum.setStatus("current")
_HpnicfDhcpRelay2InformNum_Type = Counter64
_HpnicfDhcpRelay2InformNum_Object = MibScalar
hpnicfDhcpRelay2InformNum = _HpnicfDhcpRelay2InformNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 11),
    _HpnicfDhcpRelay2InformNum_Type()
)
hpnicfDhcpRelay2InformNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2InformNum.setStatus("current")
_HpnicfDhcpRelay2BootpReplyNum_Type = Counter64
_HpnicfDhcpRelay2BootpReplyNum_Object = MibScalar
hpnicfDhcpRelay2BootpReplyNum = _HpnicfDhcpRelay2BootpReplyNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 12),
    _HpnicfDhcpRelay2BootpReplyNum_Type()
)
hpnicfDhcpRelay2BootpReplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2BootpReplyNum.setStatus("current")
_HpnicfDhcpRelay2OfferNum_Type = Counter64
_HpnicfDhcpRelay2OfferNum_Object = MibScalar
hpnicfDhcpRelay2OfferNum = _HpnicfDhcpRelay2OfferNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 13),
    _HpnicfDhcpRelay2OfferNum_Type()
)
hpnicfDhcpRelay2OfferNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2OfferNum.setStatus("current")
_HpnicfDhcpRelay2AckNum_Type = Counter64
_HpnicfDhcpRelay2AckNum_Object = MibScalar
hpnicfDhcpRelay2AckNum = _HpnicfDhcpRelay2AckNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 14),
    _HpnicfDhcpRelay2AckNum_Type()
)
hpnicfDhcpRelay2AckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2AckNum.setStatus("current")
_HpnicfDhcpRelay2NakNum_Type = Counter64
_HpnicfDhcpRelay2NakNum_Object = MibScalar
hpnicfDhcpRelay2NakNum = _HpnicfDhcpRelay2NakNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 3, 2, 15),
    _HpnicfDhcpRelay2NakNum_Type()
)
hpnicfDhcpRelay2NakNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2NakNum.setStatus("current")
_HpnicfDhcpRelay2Tables_ObjectIdentity = ObjectIdentity
hpnicfDhcpRelay2Tables = _HpnicfDhcpRelay2Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4)
)
_HpnicfDhcpRelay2IfConfigTable_Object = MibTable
hpnicfDhcpRelay2IfConfigTable = _HpnicfDhcpRelay2IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfConfigTable.setStatus("current")
_HpnicfDhcpRelay2IfConfigEntry_Object = MibTableRow
hpnicfDhcpRelay2IfConfigEntry = _HpnicfDhcpRelay2IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1)
)
hpnicfDhcpRelay2IfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfConfigEntry.setStatus("current")


class _HpnicfDhcpRelay2IfSelectRelay_Type(TruthValue):
    """Custom type hpnicfDhcpRelay2IfSelectRelay based on TruthValue"""


_HpnicfDhcpRelay2IfSelectRelay_Object = MibTableColumn
hpnicfDhcpRelay2IfSelectRelay = _HpnicfDhcpRelay2IfSelectRelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 1),
    _HpnicfDhcpRelay2IfSelectRelay_Type()
)
hpnicfDhcpRelay2IfSelectRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfSelectRelay.setStatus("current")


class _HpnicfDhcpRelay2IfCheckMac_Type(TruthValue):
    """Custom type hpnicfDhcpRelay2IfCheckMac based on TruthValue"""


_HpnicfDhcpRelay2IfCheckMac_Object = MibTableColumn
hpnicfDhcpRelay2IfCheckMac = _HpnicfDhcpRelay2IfCheckMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 2),
    _HpnicfDhcpRelay2IfCheckMac_Type()
)
hpnicfDhcpRelay2IfCheckMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfCheckMac.setStatus("current")


class _HpnicfDhcpRelay2IfOpt82Enable_Type(TruthValue):
    """Custom type hpnicfDhcpRelay2IfOpt82Enable based on TruthValue"""


_HpnicfDhcpRelay2IfOpt82Enable_Object = MibTableColumn
hpnicfDhcpRelay2IfOpt82Enable = _HpnicfDhcpRelay2IfOpt82Enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 3),
    _HpnicfDhcpRelay2IfOpt82Enable_Type()
)
hpnicfDhcpRelay2IfOpt82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfOpt82Enable.setStatus("current")


class _HpnicfDhcpRelay2IfOpt82Strategy_Type(Integer32):
    """Custom type hpnicfDhcpRelay2IfOpt82Strategy based on Integer32"""
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


_HpnicfDhcpRelay2IfOpt82Strategy_Type.__name__ = "Integer32"
_HpnicfDhcpRelay2IfOpt82Strategy_Object = MibTableColumn
hpnicfDhcpRelay2IfOpt82Strategy = _HpnicfDhcpRelay2IfOpt82Strategy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 4),
    _HpnicfDhcpRelay2IfOpt82Strategy_Type()
)
hpnicfDhcpRelay2IfOpt82Strategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfOpt82Strategy.setStatus("current")


class _HpnicfDhcpRelay2IfOpt82CIDMode_Type(Integer32):
    """Custom type hpnicfDhcpRelay2IfOpt82CIDMode based on Integer32"""
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


_HpnicfDhcpRelay2IfOpt82CIDMode_Type.__name__ = "Integer32"
_HpnicfDhcpRelay2IfOpt82CIDMode_Object = MibTableColumn
hpnicfDhcpRelay2IfOpt82CIDMode = _HpnicfDhcpRelay2IfOpt82CIDMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 5),
    _HpnicfDhcpRelay2IfOpt82CIDMode_Type()
)
hpnicfDhcpRelay2IfOpt82CIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfOpt82CIDMode.setStatus("current")


class _HpnicfDhcpRelay2IfOpt82CIDNodeType_Type(Integer32):
    """Custom type hpnicfDhcpRelay2IfOpt82CIDNodeType based on Integer32"""
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


_HpnicfDhcpRelay2IfOpt82CIDNodeType_Type.__name__ = "Integer32"
_HpnicfDhcpRelay2IfOpt82CIDNodeType_Object = MibTableColumn
hpnicfDhcpRelay2IfOpt82CIDNodeType = _HpnicfDhcpRelay2IfOpt82CIDNodeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 6),
    _HpnicfDhcpRelay2IfOpt82CIDNodeType_Type()
)
hpnicfDhcpRelay2IfOpt82CIDNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfOpt82CIDNodeType.setStatus("current")


class _HpnicfDhcpRelay2IfOpt82CIDNodeStr_Type(OctetString):
    """Custom type hpnicfDhcpRelay2IfOpt82CIDNodeStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HpnicfDhcpRelay2IfOpt82CIDNodeStr_Type.__name__ = "OctetString"
_HpnicfDhcpRelay2IfOpt82CIDNodeStr_Object = MibTableColumn
hpnicfDhcpRelay2IfOpt82CIDNodeStr = _HpnicfDhcpRelay2IfOpt82CIDNodeStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 7),
    _HpnicfDhcpRelay2IfOpt82CIDNodeStr_Type()
)
hpnicfDhcpRelay2IfOpt82CIDNodeStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfOpt82CIDNodeStr.setStatus("current")


class _HpnicfDhcpRelay2IfOpt82CIDStr_Type(OctetString):
    """Custom type hpnicfDhcpRelay2IfOpt82CIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 63),
    )


_HpnicfDhcpRelay2IfOpt82CIDStr_Type.__name__ = "OctetString"
_HpnicfDhcpRelay2IfOpt82CIDStr_Object = MibTableColumn
hpnicfDhcpRelay2IfOpt82CIDStr = _HpnicfDhcpRelay2IfOpt82CIDStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 8),
    _HpnicfDhcpRelay2IfOpt82CIDStr_Type()
)
hpnicfDhcpRelay2IfOpt82CIDStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfOpt82CIDStr.setStatus("current")


class _HpnicfDhcpRelay2IfOpt82CIDFormat_Type(Integer32):
    """Custom type hpnicfDhcpRelay2IfOpt82CIDFormat based on Integer32"""
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


_HpnicfDhcpRelay2IfOpt82CIDFormat_Type.__name__ = "Integer32"
_HpnicfDhcpRelay2IfOpt82CIDFormat_Object = MibTableColumn
hpnicfDhcpRelay2IfOpt82CIDFormat = _HpnicfDhcpRelay2IfOpt82CIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 9),
    _HpnicfDhcpRelay2IfOpt82CIDFormat_Type()
)
hpnicfDhcpRelay2IfOpt82CIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfOpt82CIDFormat.setStatus("current")


class _HpnicfDhcpRelay2IfOpt82RIDMode_Type(Integer32):
    """Custom type hpnicfDhcpRelay2IfOpt82RIDMode based on Integer32"""
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


_HpnicfDhcpRelay2IfOpt82RIDMode_Type.__name__ = "Integer32"
_HpnicfDhcpRelay2IfOpt82RIDMode_Object = MibTableColumn
hpnicfDhcpRelay2IfOpt82RIDMode = _HpnicfDhcpRelay2IfOpt82RIDMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 10),
    _HpnicfDhcpRelay2IfOpt82RIDMode_Type()
)
hpnicfDhcpRelay2IfOpt82RIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfOpt82RIDMode.setStatus("current")


class _HpnicfDhcpRelay2IfOpt82RIDStr_Type(OctetString):
    """Custom type hpnicfDhcpRelay2IfOpt82RIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfDhcpRelay2IfOpt82RIDStr_Type.__name__ = "OctetString"
_HpnicfDhcpRelay2IfOpt82RIDStr_Object = MibTableColumn
hpnicfDhcpRelay2IfOpt82RIDStr = _HpnicfDhcpRelay2IfOpt82RIDStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 11),
    _HpnicfDhcpRelay2IfOpt82RIDStr_Type()
)
hpnicfDhcpRelay2IfOpt82RIDStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfOpt82RIDStr.setStatus("current")


class _HpnicfDhcpRelay2IfOpt82RIDFormat_Type(Integer32):
    """Custom type hpnicfDhcpRelay2IfOpt82RIDFormat based on Integer32"""
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


_HpnicfDhcpRelay2IfOpt82RIDFormat_Type.__name__ = "Integer32"
_HpnicfDhcpRelay2IfOpt82RIDFormat_Object = MibTableColumn
hpnicfDhcpRelay2IfOpt82RIDFormat = _HpnicfDhcpRelay2IfOpt82RIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 1, 1, 12),
    _HpnicfDhcpRelay2IfOpt82RIDFormat_Type()
)
hpnicfDhcpRelay2IfOpt82RIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2IfOpt82RIDFormat.setStatus("current")
_HpnicfDhcpRelay2SrvAddrTable_Object = MibTable
hpnicfDhcpRelay2SrvAddrTable = _HpnicfDhcpRelay2SrvAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2SrvAddrTable.setStatus("current")
_HpnicfDhcpRelay2SrvAddrEntry_Object = MibTableRow
hpnicfDhcpRelay2SrvAddrEntry = _HpnicfDhcpRelay2SrvAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 2, 1)
)
hpnicfDhcpRelay2SrvAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpRelay2SrvAddrIP"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2SrvAddrEntry.setStatus("current")
_HpnicfDhcpRelay2SrvAddrIP_Type = InetAddressIPv4
_HpnicfDhcpRelay2SrvAddrIP_Object = MibTableColumn
hpnicfDhcpRelay2SrvAddrIP = _HpnicfDhcpRelay2SrvAddrIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 2, 1, 1),
    _HpnicfDhcpRelay2SrvAddrIP_Type()
)
hpnicfDhcpRelay2SrvAddrIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2SrvAddrIP.setStatus("current")
_HpnicfDhcpRelay2SrvAddrRowStatus_Type = RowStatus
_HpnicfDhcpRelay2SrvAddrRowStatus_Object = MibTableColumn
hpnicfDhcpRelay2SrvAddrRowStatus = _HpnicfDhcpRelay2SrvAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 2, 1, 2),
    _HpnicfDhcpRelay2SrvAddrRowStatus_Type()
)
hpnicfDhcpRelay2SrvAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2SrvAddrRowStatus.setStatus("current")
_HpnicfDhcpRelay2UserInfoTable_Object = MibTable
hpnicfDhcpRelay2UserInfoTable = _HpnicfDhcpRelay2UserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 3)
)
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2UserInfoTable.setStatus("current")
_HpnicfDhcpRelay2UserInfoEntry_Object = MibTableRow
hpnicfDhcpRelay2UserInfoEntry = _HpnicfDhcpRelay2UserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 3, 1)
)
hpnicfDhcpRelay2UserInfoEntry.setIndexNames(
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpRelay2UserInfoVpnIndex"),
    (0, "HPN-ICF-DHCP4-MIB", "hpnicfDhcpRelay2UserInfoIpAddr"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2UserInfoEntry.setStatus("current")


class _HpnicfDhcpRelay2UserInfoVpnIndex_Type(Unsigned32):
    """Custom type hpnicfDhcpRelay2UserInfoVpnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfDhcpRelay2UserInfoVpnIndex_Type.__name__ = "Unsigned32"
_HpnicfDhcpRelay2UserInfoVpnIndex_Object = MibTableColumn
hpnicfDhcpRelay2UserInfoVpnIndex = _HpnicfDhcpRelay2UserInfoVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 3, 1, 1),
    _HpnicfDhcpRelay2UserInfoVpnIndex_Type()
)
hpnicfDhcpRelay2UserInfoVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2UserInfoVpnIndex.setStatus("current")
_HpnicfDhcpRelay2UserInfoIpAddr_Type = InetAddressIPv4
_HpnicfDhcpRelay2UserInfoIpAddr_Object = MibTableColumn
hpnicfDhcpRelay2UserInfoIpAddr = _HpnicfDhcpRelay2UserInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 3, 1, 2),
    _HpnicfDhcpRelay2UserInfoIpAddr_Type()
)
hpnicfDhcpRelay2UserInfoIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2UserInfoIpAddr.setStatus("current")
_HpnicfDhcpRelay2UserInfoMacAddr_Type = MacAddress
_HpnicfDhcpRelay2UserInfoMacAddr_Object = MibTableColumn
hpnicfDhcpRelay2UserInfoMacAddr = _HpnicfDhcpRelay2UserInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 3, 1, 3),
    _HpnicfDhcpRelay2UserInfoMacAddr_Type()
)
hpnicfDhcpRelay2UserInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2UserInfoMacAddr.setStatus("current")
_HpnicfDhcpRelay2UserInfoIfIndex_Type = InterfaceIndexOrZero
_HpnicfDhcpRelay2UserInfoIfIndex_Object = MibTableColumn
hpnicfDhcpRelay2UserInfoIfIndex = _HpnicfDhcpRelay2UserInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 3, 1, 4),
    _HpnicfDhcpRelay2UserInfoIfIndex_Type()
)
hpnicfDhcpRelay2UserInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2UserInfoIfIndex.setStatus("current")
_HpnicfDhcpRelay2UserInfoRowStatus_Type = RowStatus
_HpnicfDhcpRelay2UserInfoRowStatus_Object = MibTableColumn
hpnicfDhcpRelay2UserInfoRowStatus = _HpnicfDhcpRelay2UserInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122, 4, 3, 1, 5),
    _HpnicfDhcpRelay2UserInfoRowStatus_Type()
)
hpnicfDhcpRelay2UserInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpRelay2UserInfoRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DHCP4-MIB",
    **{"hpnicfDhcp4": hpnicfDhcp4,
       "hpnicfDhcpServer2ScalarObjects": hpnicfDhcpServer2ScalarObjects,
       "hpnicfDhcpServer2ConfigGroup": hpnicfDhcpServer2ConfigGroup,
       "hpnicfDhcpServer2Enabled": hpnicfDhcpServer2Enabled,
       "hpnicfDhcpServer2AlwaysBroadcast": hpnicfDhcpServer2AlwaysBroadcast,
       "hpnicfDhcpServer2IgnoreBootp": hpnicfDhcpServer2IgnoreBootp,
       "hpnicfDhcpServer2BootpReplyRfc1048": hpnicfDhcpServer2BootpReplyRfc1048,
       "hpnicfDhcpServer2Opt82Enabled": hpnicfDhcpServer2Opt82Enabled,
       "hpnicfDhcpServer2PingNumber": hpnicfDhcpServer2PingNumber,
       "hpnicfDhcpServer2PingTimeout": hpnicfDhcpServer2PingTimeout,
       "hpnicfDhcpServer2StatGroup": hpnicfDhcpServer2StatGroup,
       "hpnicfDhcpServer2BadNum": hpnicfDhcpServer2BadNum,
       "hpnicfDhcpServer2BootpRequestNum": hpnicfDhcpServer2BootpRequestNum,
       "hpnicfDhcpServer2DiscoverNum": hpnicfDhcpServer2DiscoverNum,
       "hpnicfDhcpServer2RequestNum": hpnicfDhcpServer2RequestNum,
       "hpnicfDhcpServer2DeclineNum": hpnicfDhcpServer2DeclineNum,
       "hpnicfDhcpServer2ReleaseNum": hpnicfDhcpServer2ReleaseNum,
       "hpnicfDhcpServer2InformNum": hpnicfDhcpServer2InformNum,
       "hpnicfDhcpServer2BootpReplyNum": hpnicfDhcpServer2BootpReplyNum,
       "hpnicfDhcpServer2OfferNum": hpnicfDhcpServer2OfferNum,
       "hpnicfDhcpServer2AckNum": hpnicfDhcpServer2AckNum,
       "hpnicfDhcpServer2NakNum": hpnicfDhcpServer2NakNum,
       "hpnicfDhcpServer2TotalPoolUsage": hpnicfDhcpServer2TotalPoolUsage,
       "hpnicfDhcpServer2PoolNumber": hpnicfDhcpServer2PoolNumber,
       "hpnicfDhcpServer2ConflictNum": hpnicfDhcpServer2ConflictNum,
       "hpnicfDhcpServer2AutoBindNum": hpnicfDhcpServer2AutoBindNum,
       "hpnicfDhcpServer2ManualBindNum": hpnicfDhcpServer2ManualBindNum,
       "hpnicfDhcpServer2ExpiredBindNum": hpnicfDhcpServer2ExpiredBindNum,
       "hpnicfDhcpServer2Tables": hpnicfDhcpServer2Tables,
       "hpnicfDhcpServer2PoolTable": hpnicfDhcpServer2PoolTable,
       "hpnicfDhcpServer2PoolEntry": hpnicfDhcpServer2PoolEntry,
       "hpnicfDhcpServer2PoolIndex": hpnicfDhcpServer2PoolIndex,
       "hpnicfDhcpServer2PoolName": hpnicfDhcpServer2PoolName,
       "hpnicfDhcpServer2PoolVpnName": hpnicfDhcpServer2PoolVpnName,
       "hpnicfDhcpServer2PoolNetwork": hpnicfDhcpServer2PoolNetwork,
       "hpnicfDhcpServer2PoolNetworkMask": hpnicfDhcpServer2PoolNetworkMask,
       "hpnicfDhcpServer2PoolStartAddr": hpnicfDhcpServer2PoolStartAddr,
       "hpnicfDhcpServer2PoolEndAddr": hpnicfDhcpServer2PoolEndAddr,
       "hpnicfDhcpServer2PoolLeaseDay": hpnicfDhcpServer2PoolLeaseDay,
       "hpnicfDhcpServer2PoolLeaseHour": hpnicfDhcpServer2PoolLeaseHour,
       "hpnicfDhcpServer2PoolLeaseMinute": hpnicfDhcpServer2PoolLeaseMinute,
       "hpnicfDhcpServer2PoolLeaseSecond": hpnicfDhcpServer2PoolLeaseSecond,
       "hpnicfDhcpServer2PoolLeaseUnlimit": hpnicfDhcpServer2PoolLeaseUnlimit,
       "hpnicfDhcpServer2PoolLeaseTime": hpnicfDhcpServer2PoolLeaseTime,
       "hpnicfDhcpServer2PoolDomainName": hpnicfDhcpServer2PoolDomainName,
       "hpnicfDhcpServer2PoolGatewayIP": hpnicfDhcpServer2PoolGatewayIP,
       "hpnicfDhcpServer2PoolDNSIP": hpnicfDhcpServer2PoolDNSIP,
       "hpnicfDhcpServer2PoolPrimaryDNSIP": hpnicfDhcpServer2PoolPrimaryDNSIP,
       "hpnicfDhcpServer2PoolSecondDNSIP": hpnicfDhcpServer2PoolSecondDNSIP,
       "hpnicfDhcpServer2PoolNetbiosType": hpnicfDhcpServer2PoolNetbiosType,
       "hpnicfDhcpServer2PoolNbnsIP": hpnicfDhcpServer2PoolNbnsIP,
       "hpnicfDhcpServer2PoolBootFileName": hpnicfDhcpServer2PoolBootFileName,
       "hpnicfDhcpServer2PoolBimsIP": hpnicfDhcpServer2PoolBimsIP,
       "hpnicfDhcpServer2PoolBimsPort": hpnicfDhcpServer2PoolBimsPort,
       "hpnicfDhcpServer2PoolBimsKeyStr": hpnicfDhcpServer2PoolBimsKeyStr,
       "hpnicfDhcpServer2PoolNextServer": hpnicfDhcpServer2PoolNextServer,
       "hpnicfDhcpServer2PoolTftpDomName": hpnicfDhcpServer2PoolTftpDomName,
       "hpnicfDhcpServer2PoolTftpIP": hpnicfDhcpServer2PoolTftpIP,
       "hpnicfDhcpServer2PoolVoiceAsIP": hpnicfDhcpServer2PoolVoiceAsIP,
       "hpnicfDhcpServer2PoolVoiceFailIP": hpnicfDhcpServer2PoolVoiceFailIP,
       "hpnicfDhcpServer2PoolVoiceFailStr": hpnicfDhcpServer2PoolVoiceFailStr,
       "hpnicfDhcpServer2PoolVoiceNCPIP": hpnicfDhcpServer2PoolVoiceNCPIP,
       "hpnicfDhcpServer2PoolVoiceVlanId": hpnicfDhcpServer2PoolVoiceVlanId,
       "hpnicfDhcpServer2PoolVoiceVlanEnbl": hpnicfDhcpServer2PoolVoiceVlanEnbl,
       "hpnicfDhcpServer2PoolRowStatus": hpnicfDhcpServer2PoolRowStatus,
       "hpnicfDhcpServer2PoolVerifyClass": hpnicfDhcpServer2PoolVerifyClass,
       "hpnicfDhcpServer2IfApplyPoolTable": hpnicfDhcpServer2IfApplyPoolTable,
       "hpnicfDhcpServer2IfApplyPoolEntry": hpnicfDhcpServer2IfApplyPoolEntry,
       "hpnicfDhcpServer2IfApplyPoolName": hpnicfDhcpServer2IfApplyPoolName,
       "hpnicfDhcpServer2PoolSecNwTable": hpnicfDhcpServer2PoolSecNwTable,
       "hpnicfDhcpServer2PoolSecNwEntry": hpnicfDhcpServer2PoolSecNwEntry,
       "hpnicfDhcpServer2PoolSecNw": hpnicfDhcpServer2PoolSecNw,
       "hpnicfDhcpServer2PoolSecNwMask": hpnicfDhcpServer2PoolSecNwMask,
       "hpnicfDhcpServer2PoolSecNwGwIP": hpnicfDhcpServer2PoolSecNwGwIP,
       "hpnicfDhcpServer2PoolSecNwStatus": hpnicfDhcpServer2PoolSecNwStatus,
       "hpnicfDhcpServer2PoolClassTable": hpnicfDhcpServer2PoolClassTable,
       "hpnicfDhcpServer2PoolClassEntry": hpnicfDhcpServer2PoolClassEntry,
       "hpnicfDhcpServer2PoolClassName": hpnicfDhcpServer2PoolClassName,
       "hpnicfDhcpServer2PoolClassStart": hpnicfDhcpServer2PoolClassStart,
       "hpnicfDhcpServer2PoolClassEnd": hpnicfDhcpServer2PoolClassEnd,
       "hpnicfDhcpServer2PoolClassStatus": hpnicfDhcpServer2PoolClassStatus,
       "hpnicfDhcpServer2PoolStaticTable": hpnicfDhcpServer2PoolStaticTable,
       "hpnicfDhcpServer2PoolStaticEntry": hpnicfDhcpServer2PoolStaticEntry,
       "hpnicfDhcpServer2PoolStaticIP": hpnicfDhcpServer2PoolStaticIP,
       "hpnicfDhcpServer2PoolStaticMask": hpnicfDhcpServer2PoolStaticMask,
       "hpnicfDhcpServer2PoolStaticCID": hpnicfDhcpServer2PoolStaticCID,
       "hpnicfDhcpServer2PoolStaticHAddr": hpnicfDhcpServer2PoolStaticHAddr,
       "hpnicfDhcpServer2PoolStaticHType": hpnicfDhcpServer2PoolStaticHType,
       "hpnicfDhcpServer2PoolStaticStatus": hpnicfDhcpServer2PoolStaticStatus,
       "hpnicfDhcpServer2PoolOptionTable": hpnicfDhcpServer2PoolOptionTable,
       "hpnicfDhcpServer2PoolOptionEntry": hpnicfDhcpServer2PoolOptionEntry,
       "hpnicfDhcpServer2PoolOptCode": hpnicfDhcpServer2PoolOptCode,
       "hpnicfDhcpServer2PoolOptType": hpnicfDhcpServer2PoolOptType,
       "hpnicfDhcpServer2PoolOptAscii": hpnicfDhcpServer2PoolOptAscii,
       "hpnicfDhcpServer2PoolOptHexStr": hpnicfDhcpServer2PoolOptHexStr,
       "hpnicfDhcpServer2PoolOptIPStr": hpnicfDhcpServer2PoolOptIPStr,
       "hpnicfDhcpServer2PoolOptRowStatus": hpnicfDhcpServer2PoolOptRowStatus,
       "hpnicfDhcpServer2PoolForbidTable": hpnicfDhcpServer2PoolForbidTable,
       "hpnicfDhcpServer2PoolForbidEntry": hpnicfDhcpServer2PoolForbidEntry,
       "hpnicfDhcpServer2PoolForbidIP": hpnicfDhcpServer2PoolForbidIP,
       "hpnicfDhcpServer2PoolForbidStatus": hpnicfDhcpServer2PoolForbidStatus,
       "hpnicfDhcpServer2ClassTable": hpnicfDhcpServer2ClassTable,
       "hpnicfDhcpServer2ClassEntry": hpnicfDhcpServer2ClassEntry,
       "hpnicfDhcpServer2ClassName": hpnicfDhcpServer2ClassName,
       "hpnicfDhcpServer2ClassRowStatus": hpnicfDhcpServer2ClassRowStatus,
       "hpnicfDhcpServer2RuleTable": hpnicfDhcpServer2RuleTable,
       "hpnicfDhcpServer2RuleEntry": hpnicfDhcpServer2RuleEntry,
       "hpnicfDhcpServer2RuleNumber": hpnicfDhcpServer2RuleNumber,
       "hpnicfDhcpServer2RuleOptCode": hpnicfDhcpServer2RuleOptCode,
       "hpnicfDhcpServer2RuleOptHexStr": hpnicfDhcpServer2RuleOptHexStr,
       "hpnicfDhcpServer2RuleOptMask": hpnicfDhcpServer2RuleOptMask,
       "hpnicfDhcpServer2RuleOptOffset": hpnicfDhcpServer2RuleOptOffset,
       "hpnicfDhcpServer2RuleOptLength": hpnicfDhcpServer2RuleOptLength,
       "hpnicfDhcpServer2RuleRowStatus": hpnicfDhcpServer2RuleRowStatus,
       "hpnicfDhcpServer2ForbidTable": hpnicfDhcpServer2ForbidTable,
       "hpnicfDhcpServer2ForbidEntry": hpnicfDhcpServer2ForbidEntry,
       "hpnicfDhcpServer2ForbidVpnName": hpnicfDhcpServer2ForbidVpnName,
       "hpnicfDhcpServer2ForbidStart": hpnicfDhcpServer2ForbidStart,
       "hpnicfDhcpServer2ForbidEnd": hpnicfDhcpServer2ForbidEnd,
       "hpnicfDhcpServer2ForbidRowStatus": hpnicfDhcpServer2ForbidRowStatus,
       "hpnicfDhcpServer2FreeTable": hpnicfDhcpServer2FreeTable,
       "hpnicfDhcpServer2FreeEntry": hpnicfDhcpServer2FreeEntry,
       "hpnicfDhcpServer2FreeStart": hpnicfDhcpServer2FreeStart,
       "hpnicfDhcpServer2FreeEnd": hpnicfDhcpServer2FreeEnd,
       "hpnicfDhcpServer2ConflictTable": hpnicfDhcpServer2ConflictTable,
       "hpnicfDhcpServer2ConflictEntry": hpnicfDhcpServer2ConflictEntry,
       "hpnicfDhcpServer2ConflictIP": hpnicfDhcpServer2ConflictIP,
       "hpnicfDhcpServer2ConflictType": hpnicfDhcpServer2ConflictType,
       "hpnicfDhcpServer2ConflictTime": hpnicfDhcpServer2ConflictTime,
       "hpnicfDhcpServer2ConflictRowStatus": hpnicfDhcpServer2ConflictRowStatus,
       "hpnicfDhcpServer2ExpiredTable": hpnicfDhcpServer2ExpiredTable,
       "hpnicfDhcpServer2ExpiredEntry": hpnicfDhcpServer2ExpiredEntry,
       "hpnicfDhcpServer2ExpiredIP": hpnicfDhcpServer2ExpiredIP,
       "hpnicfDhcpServer2ExpiredClientId": hpnicfDhcpServer2ExpiredClientId,
       "hpnicfDhcpServer2ExpiredTime": hpnicfDhcpServer2ExpiredTime,
       "hpnicfDhcpServer2ExpiredRowStatus": hpnicfDhcpServer2ExpiredRowStatus,
       "hpnicfDhcpServer2IPInUseTable": hpnicfDhcpServer2IPInUseTable,
       "hpnicfDhcpServer2IPInUseEntry": hpnicfDhcpServer2IPInUseEntry,
       "hpnicfDhcpServer2IPInUseIP": hpnicfDhcpServer2IPInUseIP,
       "hpnicfDhcpServer2IPInUseClientId": hpnicfDhcpServer2IPInUseClientId,
       "hpnicfDhcpServer2IPInUseHardAddr": hpnicfDhcpServer2IPInUseHardAddr,
       "hpnicfDhcpServer2IPInUseHardType": hpnicfDhcpServer2IPInUseHardType,
       "hpnicfDhcpServer2IPInUseVlanId": hpnicfDhcpServer2IPInUseVlanId,
       "hpnicfDhcpServer2IPInUseEndLease": hpnicfDhcpServer2IPInUseEndLease,
       "hpnicfDhcpServer2IPInUseType": hpnicfDhcpServer2IPInUseType,
       "hpnicfDhcpServer2IPInUseIfIndex": hpnicfDhcpServer2IPInUseIfIndex,
       "hpnicfDhcpServer2IPInUseRowStatus": hpnicfDhcpServer2IPInUseRowStatus,
       "hpnicfDhcpServer2DefOptGrpTable": hpnicfDhcpServer2DefOptGrpTable,
       "hpnicfDhcpServer2DefOptGrpEntry": hpnicfDhcpServer2DefOptGrpEntry,
       "hpnicfDhcpServer2DefOptGrpClass": hpnicfDhcpServer2DefOptGrpClass,
       "hpnicfDhcpServer2DefOptGrpId": hpnicfDhcpServer2DefOptGrpId,
       "hpnicfDhcpServer2DefOptGrpStatus": hpnicfDhcpServer2DefOptGrpStatus,
       "hpnicfDhcpServer2ValidClassTable": hpnicfDhcpServer2ValidClassTable,
       "hpnicfDhcpServer2ValidClassEntry": hpnicfDhcpServer2ValidClassEntry,
       "hpnicfDhcpServer2ValidClassName": hpnicfDhcpServer2ValidClassName,
       "hpnicfDhcpServer2ValidClassStatus": hpnicfDhcpServer2ValidClassStatus,
       "hpnicfDhcpServer2RuleHwAddrTable": hpnicfDhcpServer2RuleHwAddrTable,
       "hpnicfDhcpServer2RuleHwAddrEntry": hpnicfDhcpServer2RuleHwAddrEntry,
       "hpnicfDhcpServer2RuleHwAddrNumber": hpnicfDhcpServer2RuleHwAddrNumber,
       "hpnicfDhcpServer2RuleHwAddress": hpnicfDhcpServer2RuleHwAddress,
       "hpnicfDhcpServer2RuleHwAddrMask": hpnicfDhcpServer2RuleHwAddrMask,
       "hpnicfDhcpServer2RuleHwAddrType": hpnicfDhcpServer2RuleHwAddrType,
       "hpnicfDhcpServer2RuleHwAddrStatus": hpnicfDhcpServer2RuleHwAddrStatus,
       "hpnicfDhcpServer2OptionGroupTable": hpnicfDhcpServer2OptionGroupTable,
       "hpnicfDhcpServer2OptionGroupEntry": hpnicfDhcpServer2OptionGroupEntry,
       "hpnicfDhcpServer2OptionGroupId": hpnicfDhcpServer2OptionGroupId,
       "hpnicfDhcpServer2OptionGroupStatus": hpnicfDhcpServer2OptionGroupStatus,
       "hpnicfDhcpServer2OptionTable": hpnicfDhcpServer2OptionTable,
       "hpnicfDhcpServer2OptionEntry": hpnicfDhcpServer2OptionEntry,
       "hpnicfDhcpServer2OptionCode": hpnicfDhcpServer2OptionCode,
       "hpnicfDhcpServer2OptionType": hpnicfDhcpServer2OptionType,
       "hpnicfDhcpServer2OptionAscii": hpnicfDhcpServer2OptionAscii,
       "hpnicfDhcpServer2OptionHexStr": hpnicfDhcpServer2OptionHexStr,
       "hpnicfDhcpServer2OptionIPStr": hpnicfDhcpServer2OptionIPStr,
       "hpnicfDhcpServer2OptionRowStatus": hpnicfDhcpServer2OptionRowStatus,
       "hpnicfDhcpRelay2ScalarObjects": hpnicfDhcpRelay2ScalarObjects,
       "hpnicfDhcpRelay2ConfigGroup": hpnicfDhcpRelay2ConfigGroup,
       "hpnicfDhcpRelay2UserInfoRecord": hpnicfDhcpRelay2UserInfoRecord,
       "hpnicfDhcpRelay2UserInfoRefresh": hpnicfDhcpRelay2UserInfoRefresh,
       "hpnicfDhcpRelay2UserInfoFlushTime": hpnicfDhcpRelay2UserInfoFlushTime,
       "hpnicfDhcpRelay2ReleaseAddr": hpnicfDhcpRelay2ReleaseAddr,
       "hpnicfDhcpRelay2StatisticsGroup": hpnicfDhcpRelay2StatisticsGroup,
       "hpnicfDhcpRelay2RxClientNum": hpnicfDhcpRelay2RxClientNum,
       "hpnicfDhcpRelay2TxClientNum": hpnicfDhcpRelay2TxClientNum,
       "hpnicfDhcpRelay2RxServerNum": hpnicfDhcpRelay2RxServerNum,
       "hpnicfDhcpRelay2TxServerNum": hpnicfDhcpRelay2TxServerNum,
       "hpnicfDhcpRelay2BadNum": hpnicfDhcpRelay2BadNum,
       "hpnicfDhcpRelay2BootpRequestNum": hpnicfDhcpRelay2BootpRequestNum,
       "hpnicfDhcpRelay2DiscoverNum": hpnicfDhcpRelay2DiscoverNum,
       "hpnicfDhcpRelay2RequestNum": hpnicfDhcpRelay2RequestNum,
       "hpnicfDhcpRelay2DeclineNum": hpnicfDhcpRelay2DeclineNum,
       "hpnicfDhcpRelay2ReleaseNum": hpnicfDhcpRelay2ReleaseNum,
       "hpnicfDhcpRelay2InformNum": hpnicfDhcpRelay2InformNum,
       "hpnicfDhcpRelay2BootpReplyNum": hpnicfDhcpRelay2BootpReplyNum,
       "hpnicfDhcpRelay2OfferNum": hpnicfDhcpRelay2OfferNum,
       "hpnicfDhcpRelay2AckNum": hpnicfDhcpRelay2AckNum,
       "hpnicfDhcpRelay2NakNum": hpnicfDhcpRelay2NakNum,
       "hpnicfDhcpRelay2Tables": hpnicfDhcpRelay2Tables,
       "hpnicfDhcpRelay2IfConfigTable": hpnicfDhcpRelay2IfConfigTable,
       "hpnicfDhcpRelay2IfConfigEntry": hpnicfDhcpRelay2IfConfigEntry,
       "hpnicfDhcpRelay2IfSelectRelay": hpnicfDhcpRelay2IfSelectRelay,
       "hpnicfDhcpRelay2IfCheckMac": hpnicfDhcpRelay2IfCheckMac,
       "hpnicfDhcpRelay2IfOpt82Enable": hpnicfDhcpRelay2IfOpt82Enable,
       "hpnicfDhcpRelay2IfOpt82Strategy": hpnicfDhcpRelay2IfOpt82Strategy,
       "hpnicfDhcpRelay2IfOpt82CIDMode": hpnicfDhcpRelay2IfOpt82CIDMode,
       "hpnicfDhcpRelay2IfOpt82CIDNodeType": hpnicfDhcpRelay2IfOpt82CIDNodeType,
       "hpnicfDhcpRelay2IfOpt82CIDNodeStr": hpnicfDhcpRelay2IfOpt82CIDNodeStr,
       "hpnicfDhcpRelay2IfOpt82CIDStr": hpnicfDhcpRelay2IfOpt82CIDStr,
       "hpnicfDhcpRelay2IfOpt82CIDFormat": hpnicfDhcpRelay2IfOpt82CIDFormat,
       "hpnicfDhcpRelay2IfOpt82RIDMode": hpnicfDhcpRelay2IfOpt82RIDMode,
       "hpnicfDhcpRelay2IfOpt82RIDStr": hpnicfDhcpRelay2IfOpt82RIDStr,
       "hpnicfDhcpRelay2IfOpt82RIDFormat": hpnicfDhcpRelay2IfOpt82RIDFormat,
       "hpnicfDhcpRelay2SrvAddrTable": hpnicfDhcpRelay2SrvAddrTable,
       "hpnicfDhcpRelay2SrvAddrEntry": hpnicfDhcpRelay2SrvAddrEntry,
       "hpnicfDhcpRelay2SrvAddrIP": hpnicfDhcpRelay2SrvAddrIP,
       "hpnicfDhcpRelay2SrvAddrRowStatus": hpnicfDhcpRelay2SrvAddrRowStatus,
       "hpnicfDhcpRelay2UserInfoTable": hpnicfDhcpRelay2UserInfoTable,
       "hpnicfDhcpRelay2UserInfoEntry": hpnicfDhcpRelay2UserInfoEntry,
       "hpnicfDhcpRelay2UserInfoVpnIndex": hpnicfDhcpRelay2UserInfoVpnIndex,
       "hpnicfDhcpRelay2UserInfoIpAddr": hpnicfDhcpRelay2UserInfoIpAddr,
       "hpnicfDhcpRelay2UserInfoMacAddr": hpnicfDhcpRelay2UserInfoMacAddr,
       "hpnicfDhcpRelay2UserInfoIfIndex": hpnicfDhcpRelay2UserInfoIfIndex,
       "hpnicfDhcpRelay2UserInfoRowStatus": hpnicfDhcpRelay2UserInfoRowStatus}
)
