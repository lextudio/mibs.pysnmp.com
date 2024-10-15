# SNMP MIB module (CISCO-IP-ADDRESS-POOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-ADDRESS-POOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:33 2024
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

(IpAddrPoolInstanceIdentifier,
 IpAddrPoolInstanceIdentifierOrZero,
 IpAddressPoolGroupName,
 IpAddressPoolGroupNameOrNull,
 IpAddressPoolNameOrNull,
 IpAddressPoolThresholdUnits) = mibBuilder.importSymbols(
    "CISCO-IP-ADDRESS-POOL-TC-MIB",
    "IpAddrPoolInstanceIdentifier",
    "IpAddrPoolInstanceIdentifierOrZero",
    "IpAddressPoolGroupName",
    "IpAddressPoolGroupNameOrNull",
    "IpAddressPoolNameOrNull",
    "IpAddressPoolThresholdUnits")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIpAddressPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748)
)
ciscoIpAddressPoolMIB.setRevisions(
        ("2010-02-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpAddressPoolMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpAddressPoolMIBNotifs = _CiscoIpAddressPoolMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 0)
)
_CiscoIpAddressPoolMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpAddressPoolMIBObjects = _CiscoIpAddressPoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1)
)
_CiapGlobal_ObjectIdentity = ObjectIdentity
ciapGlobal = _CiapGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 1)
)


class _CiapGlobalNotifyEnable_Type(TruthValue):
    """Custom type ciapGlobalNotifyEnable based on TruthValue"""


_CiapGlobalNotifyEnable_Object = MibScalar
ciapGlobalNotifyEnable = _CiapGlobalNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 1, 1),
    _CiapGlobalNotifyEnable_Type()
)
ciapGlobalNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciapGlobalNotifyEnable.setStatus("current")


class _CiapGlobalThresholdUnits_Type(IpAddressPoolThresholdUnits):
    """Custom type ciapGlobalThresholdUnits based on IpAddressPoolThresholdUnits"""


_CiapGlobalThresholdUnits_Object = MibScalar
ciapGlobalThresholdUnits = _CiapGlobalThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 1, 2),
    _CiapGlobalThresholdUnits_Type()
)
ciapGlobalThresholdUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciapGlobalThresholdUnits.setStatus("current")


class _CiapGlobalThresholdRising_Type(Unsigned32):
    """Custom type ciapGlobalThresholdRising based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapGlobalThresholdRising_Type.__name__ = "Unsigned32"
_CiapGlobalThresholdRising_Object = MibScalar
ciapGlobalThresholdRising = _CiapGlobalThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 1, 3),
    _CiapGlobalThresholdRising_Type()
)
ciapGlobalThresholdRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciapGlobalThresholdRising.setStatus("current")


class _CiapGlobalThresholdFalling_Type(Unsigned32):
    """Custom type ciapGlobalThresholdFalling based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapGlobalThresholdFalling_Type.__name__ = "Unsigned32"
_CiapGlobalThresholdFalling_Object = MibScalar
ciapGlobalThresholdFalling = _CiapGlobalThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 1, 4),
    _CiapGlobalThresholdFalling_Type()
)
ciapGlobalThresholdFalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciapGlobalThresholdFalling.setStatus("current")
_CiapPools_ObjectIdentity = ObjectIdentity
ciapPools = _CiapPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2)
)
_CiapPoolIdNext_Type = IpAddrPoolInstanceIdentifierOrZero
_CiapPoolIdNext_Object = MibScalar
ciapPoolIdNext = _CiapPoolIdNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 1),
    _CiapPoolIdNext_Type()
)
ciapPoolIdNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapPoolIdNext.setStatus("current")
_CiapPoolTable_Object = MibTable
ciapPoolTable = _CiapPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ciapPoolTable.setStatus("current")
_CiapPoolEntry_Object = MibTableRow
ciapPoolEntry = _CiapPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1)
)
ciapPoolEntry.setIndexNames(
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolId"),
)
if mibBuilder.loadTexts:
    ciapPoolEntry.setStatus("current")
_CiapPoolId_Type = IpAddrPoolInstanceIdentifier
_CiapPoolId_Object = MibTableColumn
ciapPoolId = _CiapPoolId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 1),
    _CiapPoolId_Type()
)
ciapPoolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciapPoolId.setStatus("current")
_CiapPoolStatus_Type = RowStatus
_CiapPoolStatus_Object = MibTableColumn
ciapPoolStatus = _CiapPoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 2),
    _CiapPoolStatus_Type()
)
ciapPoolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPoolStatus.setStatus("current")


class _CiapPoolStorage_Type(StorageType):
    """Custom type ciapPoolStorage based on StorageType"""


_CiapPoolStorage_Object = MibTableColumn
ciapPoolStorage = _CiapPoolStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 3),
    _CiapPoolStorage_Type()
)
ciapPoolStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPoolStorage.setStatus("current")
_CiapPoolName_Type = IpAddressPoolNameOrNull
_CiapPoolName_Object = MibTableColumn
ciapPoolName = _CiapPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 4),
    _CiapPoolName_Type()
)
ciapPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPoolName.setStatus("current")


class _CiapPoolType_Type(Integer32):
    """Custom type ciapPoolType based on Integer32"""
    defaultValue = 2

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
        *(("dhcp", 4),
          ("local", 3),
          ("other", 1),
          ("shared", 2))
    )


_CiapPoolType_Type.__name__ = "Integer32"
_CiapPoolType_Object = MibTableColumn
ciapPoolType = _CiapPoolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 5),
    _CiapPoolType_Type()
)
ciapPoolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPoolType.setStatus("current")
_CiapPoolContainedIn_Type = IpAddressPoolGroupNameOrNull
_CiapPoolContainedIn_Object = MibTableColumn
ciapPoolContainedIn = _CiapPoolContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 6),
    _CiapPoolContainedIn_Type()
)
ciapPoolContainedIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPoolContainedIn.setStatus("current")
_CiapPoolThresholdUnits_Type = IpAddressPoolThresholdUnits
_CiapPoolThresholdUnits_Object = MibTableColumn
ciapPoolThresholdUnits = _CiapPoolThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 7),
    _CiapPoolThresholdUnits_Type()
)
ciapPoolThresholdUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPoolThresholdUnits.setStatus("current")
if mibBuilder.loadTexts:
    ciapPoolThresholdUnits.setUnits("IP addresses")


class _CiapPoolThresholdRising_Type(Unsigned32):
    """Custom type ciapPoolThresholdRising based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapPoolThresholdRising_Type.__name__ = "Unsigned32"
_CiapPoolThresholdRising_Object = MibTableColumn
ciapPoolThresholdRising = _CiapPoolThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 8),
    _CiapPoolThresholdRising_Type()
)
ciapPoolThresholdRising.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPoolThresholdRising.setStatus("current")


class _CiapPoolThresholdFalling_Type(Unsigned32):
    """Custom type ciapPoolThresholdFalling based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapPoolThresholdFalling_Type.__name__ = "Unsigned32"
_CiapPoolThresholdFalling_Object = MibTableColumn
ciapPoolThresholdFalling = _CiapPoolThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 9),
    _CiapPoolThresholdFalling_Type()
)
ciapPoolThresholdFalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPoolThresholdFalling.setStatus("current")
_CiapPoolAddressesInUse_Type = Gauge32
_CiapPoolAddressesInUse_Object = MibTableColumn
ciapPoolAddressesInUse = _CiapPoolAddressesInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 10),
    _CiapPoolAddressesInUse_Type()
)
ciapPoolAddressesInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPoolAddressesInUse.setStatus("current")
if mibBuilder.loadTexts:
    ciapPoolAddressesInUse.setUnits("IP addresses/prefixes")
_CiapPoolAddressesFree_Type = Gauge32
_CiapPoolAddressesFree_Object = MibTableColumn
ciapPoolAddressesFree = _CiapPoolAddressesFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 2, 1, 11),
    _CiapPoolAddressesFree_Type()
)
ciapPoolAddressesFree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPoolAddressesFree.setStatus("current")
if mibBuilder.loadTexts:
    ciapPoolAddressesFree.setUnits("IP addresses/prefixes")
_CiapPoolTableChanged_Type = TimeStamp
_CiapPoolTableChanged_Object = MibScalar
ciapPoolTableChanged = _CiapPoolTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 3),
    _CiapPoolTableChanged_Type()
)
ciapPoolTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapPoolTableChanged.setStatus("current")
_CiapRangeTable_Object = MibTable
ciapRangeTable = _CiapRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ciapRangeTable.setStatus("current")
_CiapRangeEntry_Object = MibTableRow
ciapRangeEntry = _CiapRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1)
)
ciapRangeEntry.setIndexNames(
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolId"),
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeAddressType"),
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeAddressLower"),
)
if mibBuilder.loadTexts:
    ciapRangeEntry.setStatus("current")
_CiapRangeAddressType_Type = InetAddressType
_CiapRangeAddressType_Object = MibTableColumn
ciapRangeAddressType = _CiapRangeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 1),
    _CiapRangeAddressType_Type()
)
ciapRangeAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciapRangeAddressType.setStatus("current")


class _CiapRangeAddressLower_Type(InetAddress):
    """Custom type ciapRangeAddressLower based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_CiapRangeAddressLower_Type.__name__ = "InetAddress"
_CiapRangeAddressLower_Object = MibTableColumn
ciapRangeAddressLower = _CiapRangeAddressLower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 2),
    _CiapRangeAddressLower_Type()
)
ciapRangeAddressLower.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciapRangeAddressLower.setStatus("current")
_CiapRangeStatus_Type = RowStatus
_CiapRangeStatus_Object = MibTableColumn
ciapRangeStatus = _CiapRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 3),
    _CiapRangeStatus_Type()
)
ciapRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapRangeStatus.setStatus("current")


class _CiapRangeStorage_Type(StorageType):
    """Custom type ciapRangeStorage based on StorageType"""


_CiapRangeStorage_Object = MibTableColumn
ciapRangeStorage = _CiapRangeStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 4),
    _CiapRangeStorage_Type()
)
ciapRangeStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapRangeStorage.setStatus("current")
_CiapRangeAddressUpper_Type = InetAddress
_CiapRangeAddressUpper_Object = MibTableColumn
ciapRangeAddressUpper = _CiapRangeAddressUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 5),
    _CiapRangeAddressUpper_Type()
)
ciapRangeAddressUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapRangeAddressUpper.setStatus("current")


class _CiapRangeCacheSize_Type(Unsigned32):
    """Custom type ciapRangeCacheSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapRangeCacheSize_Type.__name__ = "Unsigned32"
_CiapRangeCacheSize_Object = MibTableColumn
ciapRangeCacheSize = _CiapRangeCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 6),
    _CiapRangeCacheSize_Type()
)
ciapRangeCacheSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapRangeCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    ciapRangeCacheSize.setUnits("IP addresses")


class _CiapRangeRecycleDelay_Type(Unsigned32):
    """Custom type ciapRangeRecycleDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapRangeRecycleDelay_Type.__name__ = "Unsigned32"
_CiapRangeRecycleDelay_Object = MibTableColumn
ciapRangeRecycleDelay = _CiapRangeRecycleDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 7),
    _CiapRangeRecycleDelay_Type()
)
ciapRangeRecycleDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapRangeRecycleDelay.setStatus("current")
if mibBuilder.loadTexts:
    ciapRangeRecycleDelay.setUnits("seconds")


class _CiapRangePriority_Type(Unsigned32):
    """Custom type ciapRangePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiapRangePriority_Type.__name__ = "Unsigned32"
_CiapRangePriority_Object = MibTableColumn
ciapRangePriority = _CiapRangePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 8),
    _CiapRangePriority_Type()
)
ciapRangePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapRangePriority.setStatus("current")
_CiapRangeThresholdUnits_Type = IpAddressPoolThresholdUnits
_CiapRangeThresholdUnits_Object = MibTableColumn
ciapRangeThresholdUnits = _CiapRangeThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 9),
    _CiapRangeThresholdUnits_Type()
)
ciapRangeThresholdUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapRangeThresholdUnits.setStatus("current")


class _CiapRangeThresholdRising_Type(Unsigned32):
    """Custom type ciapRangeThresholdRising based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapRangeThresholdRising_Type.__name__ = "Unsigned32"
_CiapRangeThresholdRising_Object = MibTableColumn
ciapRangeThresholdRising = _CiapRangeThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 10),
    _CiapRangeThresholdRising_Type()
)
ciapRangeThresholdRising.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapRangeThresholdRising.setStatus("current")


class _CiapRangeThresholdFalling_Type(Unsigned32):
    """Custom type ciapRangeThresholdFalling based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapRangeThresholdFalling_Type.__name__ = "Unsigned32"
_CiapRangeThresholdFalling_Object = MibTableColumn
ciapRangeThresholdFalling = _CiapRangeThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 11),
    _CiapRangeThresholdFalling_Type()
)
ciapRangeThresholdFalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapRangeThresholdFalling.setStatus("current")
_CiapRangeAddressesInUse_Type = Gauge32
_CiapRangeAddressesInUse_Object = MibTableColumn
ciapRangeAddressesInUse = _CiapRangeAddressesInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 12),
    _CiapRangeAddressesInUse_Type()
)
ciapRangeAddressesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapRangeAddressesInUse.setStatus("current")
if mibBuilder.loadTexts:
    ciapRangeAddressesInUse.setUnits("IP addresses")
_CiapRangeAddressesFree_Type = Gauge32
_CiapRangeAddressesFree_Object = MibTableColumn
ciapRangeAddressesFree = _CiapRangeAddressesFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 4, 1, 13),
    _CiapRangeAddressesFree_Type()
)
ciapRangeAddressesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapRangeAddressesFree.setStatus("current")
if mibBuilder.loadTexts:
    ciapRangeAddressesFree.setUnits("IP addresses")
_CiapRangeTableChanged_Type = TimeStamp
_CiapRangeTableChanged_Object = MibScalar
ciapRangeTableChanged = _CiapRangeTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 5),
    _CiapRangeTableChanged_Type()
)
ciapRangeTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapRangeTableChanged.setStatus("current")
_CiapPrefixTable_Object = MibTable
ciapPrefixTable = _CiapPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ciapPrefixTable.setStatus("current")
_CiapPrefixEntry_Object = MibTableRow
ciapPrefixEntry = _CiapPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1)
)
ciapPrefixEntry.setIndexNames(
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolId"),
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixType"),
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixAddress"),
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixAddressMask"),
)
if mibBuilder.loadTexts:
    ciapPrefixEntry.setStatus("current")
_CiapPrefixType_Type = InetAddressType
_CiapPrefixType_Object = MibTableColumn
ciapPrefixType = _CiapPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 1),
    _CiapPrefixType_Type()
)
ciapPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciapPrefixType.setStatus("current")


class _CiapPrefixAddress_Type(InetAddress):
    """Custom type ciapPrefixAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_CiapPrefixAddress_Type.__name__ = "InetAddress"
_CiapPrefixAddress_Object = MibTableColumn
ciapPrefixAddress = _CiapPrefixAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 2),
    _CiapPrefixAddress_Type()
)
ciapPrefixAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciapPrefixAddress.setStatus("current")


class _CiapPrefixAddressMask_Type(InetAddress):
    """Custom type ciapPrefixAddressMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_CiapPrefixAddressMask_Type.__name__ = "InetAddress"
_CiapPrefixAddressMask_Object = MibTableColumn
ciapPrefixAddressMask = _CiapPrefixAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 3),
    _CiapPrefixAddressMask_Type()
)
ciapPrefixAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciapPrefixAddressMask.setStatus("current")
_CiapPrefixStatus_Type = RowStatus
_CiapPrefixStatus_Object = MibTableColumn
ciapPrefixStatus = _CiapPrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 4),
    _CiapPrefixStatus_Type()
)
ciapPrefixStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixStatus.setStatus("current")


class _CiapPrefixStorage_Type(StorageType):
    """Custom type ciapPrefixStorage based on StorageType"""


_CiapPrefixStorage_Object = MibTableColumn
ciapPrefixStorage = _CiapPrefixStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 5),
    _CiapPrefixStorage_Type()
)
ciapPrefixStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixStorage.setStatus("current")
_CiapPrefixAssignedLength_Type = InetAddressPrefixLength
_CiapPrefixAssignedLength_Object = MibTableColumn
ciapPrefixAssignedLength = _CiapPrefixAssignedLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 6),
    _CiapPrefixAssignedLength_Type()
)
ciapPrefixAssignedLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixAssignedLength.setStatus("current")


class _CiapPrefixCacheSize_Type(Unsigned32):
    """Custom type ciapPrefixCacheSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapPrefixCacheSize_Type.__name__ = "Unsigned32"
_CiapPrefixCacheSize_Object = MibTableColumn
ciapPrefixCacheSize = _CiapPrefixCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 7),
    _CiapPrefixCacheSize_Type()
)
ciapPrefixCacheSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    ciapPrefixCacheSize.setUnits("IP prefixes")


class _CiapPrefixRecycleDelay_Type(Unsigned32):
    """Custom type ciapPrefixRecycleDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapPrefixRecycleDelay_Type.__name__ = "Unsigned32"
_CiapPrefixRecycleDelay_Object = MibTableColumn
ciapPrefixRecycleDelay = _CiapPrefixRecycleDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 8),
    _CiapPrefixRecycleDelay_Type()
)
ciapPrefixRecycleDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixRecycleDelay.setStatus("current")
if mibBuilder.loadTexts:
    ciapPrefixRecycleDelay.setUnits("seconds")


class _CiapPrefixPriority_Type(Unsigned32):
    """Custom type ciapPrefixPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiapPrefixPriority_Type.__name__ = "Unsigned32"
_CiapPrefixPriority_Object = MibTableColumn
ciapPrefixPriority = _CiapPrefixPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 9),
    _CiapPrefixPriority_Type()
)
ciapPrefixPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixPriority.setStatus("current")
_CiapPrefixThresholdUnits_Type = IpAddressPoolThresholdUnits
_CiapPrefixThresholdUnits_Object = MibTableColumn
ciapPrefixThresholdUnits = _CiapPrefixThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 10),
    _CiapPrefixThresholdUnits_Type()
)
ciapPrefixThresholdUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixThresholdUnits.setStatus("current")


class _CiapPrefixThresholdRising_Type(Unsigned32):
    """Custom type ciapPrefixThresholdRising based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapPrefixThresholdRising_Type.__name__ = "Unsigned32"
_CiapPrefixThresholdRising_Object = MibTableColumn
ciapPrefixThresholdRising = _CiapPrefixThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 11),
    _CiapPrefixThresholdRising_Type()
)
ciapPrefixThresholdRising.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixThresholdRising.setStatus("current")


class _CiapPrefixThresholdFalling_Type(Unsigned32):
    """Custom type ciapPrefixThresholdFalling based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapPrefixThresholdFalling_Type.__name__ = "Unsigned32"
_CiapPrefixThresholdFalling_Object = MibTableColumn
ciapPrefixThresholdFalling = _CiapPrefixThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 12),
    _CiapPrefixThresholdFalling_Type()
)
ciapPrefixThresholdFalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixThresholdFalling.setStatus("current")
_CiapPrefixPrefixesInUse_Type = Gauge32
_CiapPrefixPrefixesInUse_Object = MibTableColumn
ciapPrefixPrefixesInUse = _CiapPrefixPrefixesInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 13),
    _CiapPrefixPrefixesInUse_Type()
)
ciapPrefixPrefixesInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixPrefixesInUse.setStatus("current")
if mibBuilder.loadTexts:
    ciapPrefixPrefixesInUse.setUnits("IP prefixes")
_CiapPrefixPrefixesFree_Type = Gauge32
_CiapPrefixPrefixesFree_Object = MibTableColumn
ciapPrefixPrefixesFree = _CiapPrefixPrefixesFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 6, 1, 14),
    _CiapPrefixPrefixesFree_Type()
)
ciapPrefixPrefixesFree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciapPrefixPrefixesFree.setStatus("current")
if mibBuilder.loadTexts:
    ciapPrefixPrefixesFree.setUnits("IP prefixes")
_CiapPrefixTableChanged_Type = TimeStamp
_CiapPrefixTableChanged_Object = MibScalar
ciapPrefixTableChanged = _CiapPrefixTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 2, 7),
    _CiapPrefixTableChanged_Type()
)
ciapPrefixTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapPrefixTableChanged.setStatus("current")
_CiapPoolGroups_ObjectIdentity = ObjectIdentity
ciapPoolGroups = _CiapPoolGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3)
)
_CiapPoolGroupIdNext_Type = IpAddrPoolInstanceIdentifierOrZero
_CiapPoolGroupIdNext_Object = MibScalar
ciapPoolGroupIdNext = _CiapPoolGroupIdNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 1),
    _CiapPoolGroupIdNext_Type()
)
ciapPoolGroupIdNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapPoolGroupIdNext.setStatus("current")
_CiapPoolGroupTable_Object = MibTable
ciapPoolGroupTable = _CiapPoolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ciapPoolGroupTable.setStatus("current")
_CiapPoolGroupEntry_Object = MibTableRow
ciapPoolGroupEntry = _CiapPoolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 2, 1)
)
ciapPoolGroupEntry.setIndexNames(
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupId"),
)
if mibBuilder.loadTexts:
    ciapPoolGroupEntry.setStatus("current")
_CiapPoolGroupId_Type = IpAddrPoolInstanceIdentifier
_CiapPoolGroupId_Object = MibTableColumn
ciapPoolGroupId = _CiapPoolGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 2, 1, 1),
    _CiapPoolGroupId_Type()
)
ciapPoolGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciapPoolGroupId.setStatus("current")
_CiapPoolGroupName_Type = IpAddressPoolGroupName
_CiapPoolGroupName_Object = MibTableColumn
ciapPoolGroupName = _CiapPoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 2, 1, 2),
    _CiapPoolGroupName_Type()
)
ciapPoolGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapPoolGroupName.setStatus("current")
_CiapPoolGroupThresholdUnits_Type = IpAddressPoolThresholdUnits
_CiapPoolGroupThresholdUnits_Object = MibTableColumn
ciapPoolGroupThresholdUnits = _CiapPoolGroupThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 2, 1, 3),
    _CiapPoolGroupThresholdUnits_Type()
)
ciapPoolGroupThresholdUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciapPoolGroupThresholdUnits.setStatus("current")


class _CiapPoolGroupThresholdRising_Type(Unsigned32):
    """Custom type ciapPoolGroupThresholdRising based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapPoolGroupThresholdRising_Type.__name__ = "Unsigned32"
_CiapPoolGroupThresholdRising_Object = MibTableColumn
ciapPoolGroupThresholdRising = _CiapPoolGroupThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 2, 1, 4),
    _CiapPoolGroupThresholdRising_Type()
)
ciapPoolGroupThresholdRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciapPoolGroupThresholdRising.setStatus("current")


class _CiapPoolGroupThresholdFalling_Type(Unsigned32):
    """Custom type ciapPoolGroupThresholdFalling based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapPoolGroupThresholdFalling_Type.__name__ = "Unsigned32"
_CiapPoolGroupThresholdFalling_Object = MibTableColumn
ciapPoolGroupThresholdFalling = _CiapPoolGroupThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 2, 1, 5),
    _CiapPoolGroupThresholdFalling_Type()
)
ciapPoolGroupThresholdFalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciapPoolGroupThresholdFalling.setStatus("current")
_CiapPoolGroupAddressesInUse_Type = Gauge32
_CiapPoolGroupAddressesInUse_Object = MibTableColumn
ciapPoolGroupAddressesInUse = _CiapPoolGroupAddressesInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 2, 1, 6),
    _CiapPoolGroupAddressesInUse_Type()
)
ciapPoolGroupAddressesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapPoolGroupAddressesInUse.setStatus("current")
if mibBuilder.loadTexts:
    ciapPoolGroupAddressesInUse.setUnits("IP addresses/prefixes")
_CiapPoolGroupAddressesFree_Type = Gauge32
_CiapPoolGroupAddressesFree_Object = MibTableColumn
ciapPoolGroupAddressesFree = _CiapPoolGroupAddressesFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 2, 1, 7),
    _CiapPoolGroupAddressesFree_Type()
)
ciapPoolGroupAddressesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapPoolGroupAddressesFree.setStatus("current")
if mibBuilder.loadTexts:
    ciapPoolGroupAddressesFree.setUnits("IP addresses/prefixes")
_CiapPoolGroupContainsTable_Object = MibTable
ciapPoolGroupContainsTable = _CiapPoolGroupContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ciapPoolGroupContainsTable.setStatus("current")
_CiapPoolGroupContainsEntry_Object = MibTableRow
ciapPoolGroupContainsEntry = _CiapPoolGroupContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 3, 1)
)
ciapPoolGroupContainsEntry.setIndexNames(
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupId"),
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupContainsId"),
)
if mibBuilder.loadTexts:
    ciapPoolGroupContainsEntry.setStatus("current")
_CiapPoolGroupContainsId_Type = IpAddrPoolInstanceIdentifier
_CiapPoolGroupContainsId_Object = MibTableColumn
ciapPoolGroupContainsId = _CiapPoolGroupContainsId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 3, 3, 1, 1),
    _CiapPoolGroupContainsId_Type()
)
ciapPoolGroupContainsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapPoolGroupContainsId.setStatus("current")
_CiapAllocatedAddresses_ObjectIdentity = ObjectIdentity
ciapAllocatedAddresses = _CiapAllocatedAddresses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 4)
)
_CiapAllocatedAddressTable_Object = MibTable
ciapAllocatedAddressTable = _CiapAllocatedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ciapAllocatedAddressTable.setStatus("current")
_CiapAllocatedAddressEntry_Object = MibTableRow
ciapAllocatedAddressEntry = _CiapAllocatedAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 4, 1, 1)
)
ciapAllocatedAddressEntry.setIndexNames(
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolId"),
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapAllocatedAddressType"),
    (0, "CISCO-IP-ADDRESS-POOL-MIB", "ciapAllocatedAddress"),
)
if mibBuilder.loadTexts:
    ciapAllocatedAddressEntry.setStatus("current")
_CiapAllocatedAddressType_Type = InetAddressType
_CiapAllocatedAddressType_Object = MibTableColumn
ciapAllocatedAddressType = _CiapAllocatedAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 4, 1, 1, 1),
    _CiapAllocatedAddressType_Type()
)
ciapAllocatedAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciapAllocatedAddressType.setStatus("current")


class _CiapAllocatedAddress_Type(InetAddress):
    """Custom type ciapAllocatedAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_CiapAllocatedAddress_Type.__name__ = "InetAddress"
_CiapAllocatedAddress_Object = MibTableColumn
ciapAllocatedAddress = _CiapAllocatedAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 4, 1, 1, 2),
    _CiapAllocatedAddress_Type()
)
ciapAllocatedAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciapAllocatedAddress.setStatus("current")


class _CiapAllocatedAddressMask_Type(InetAddress):
    """Custom type ciapAllocatedAddressMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_CiapAllocatedAddressMask_Type.__name__ = "InetAddress"
_CiapAllocatedAddressMask_Object = MibTableColumn
ciapAllocatedAddressMask = _CiapAllocatedAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 4, 1, 1, 3),
    _CiapAllocatedAddressMask_Type()
)
ciapAllocatedAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciapAllocatedAddressMask.setStatus("current")
_CiapNotifyData_ObjectIdentity = ObjectIdentity
ciapNotifyData = _CiapNotifyData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 5)
)
_CiapNotifyResource_Type = RowPointer
_CiapNotifyResource_Object = MibScalar
ciapNotifyResource = _CiapNotifyResource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 5, 1),
    _CiapNotifyResource_Type()
)
ciapNotifyResource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciapNotifyResource.setStatus("current")
_CiapNotifyThresholdUnits_Type = IpAddressPoolThresholdUnits
_CiapNotifyThresholdUnits_Object = MibScalar
ciapNotifyThresholdUnits = _CiapNotifyThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 5, 2),
    _CiapNotifyThresholdUnits_Type()
)
ciapNotifyThresholdUnits.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciapNotifyThresholdUnits.setStatus("current")


class _CiapNotifyThresholdRising_Type(Unsigned32):
    """Custom type ciapNotifyThresholdRising based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapNotifyThresholdRising_Type.__name__ = "Unsigned32"
_CiapNotifyThresholdRising_Object = MibScalar
ciapNotifyThresholdRising = _CiapNotifyThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 5, 3),
    _CiapNotifyThresholdRising_Type()
)
ciapNotifyThresholdRising.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciapNotifyThresholdRising.setStatus("current")


class _CiapNotifyThresholdFalling_Type(Unsigned32):
    """Custom type ciapNotifyThresholdFalling based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CiapNotifyThresholdFalling_Type.__name__ = "Unsigned32"
_CiapNotifyThresholdFalling_Object = MibScalar
ciapNotifyThresholdFalling = _CiapNotifyThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 5, 4),
    _CiapNotifyThresholdFalling_Type()
)
ciapNotifyThresholdFalling.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciapNotifyThresholdFalling.setStatus("current")
_CiapNotifyInUse_Type = Gauge32
_CiapNotifyInUse_Object = MibScalar
ciapNotifyInUse = _CiapNotifyInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 5, 5),
    _CiapNotifyInUse_Type()
)
ciapNotifyInUse.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciapNotifyInUse.setStatus("current")
if mibBuilder.loadTexts:
    ciapNotifyInUse.setUnits("IP addresses/prefixes")
_CiapNotifyFree_Type = Gauge32
_CiapNotifyFree_Object = MibScalar
ciapNotifyFree = _CiapNotifyFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 1, 5, 6),
    _CiapNotifyFree_Type()
)
ciapNotifyFree.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciapNotifyFree.setStatus("current")
if mibBuilder.loadTexts:
    ciapNotifyFree.setUnits("IP addresses/prefixes")
_CiscoIpAddressPoolMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpAddressPoolMIBConform = _CiscoIpAddressPoolMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2)
)
_CiscoIpAddressPoolMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpAddressPoolMIBCompliances = _CiscoIpAddressPoolMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2, 1)
)
_CiscoIpAddressPoolMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpAddressPoolMIBGroups = _CiscoIpAddressPoolMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2, 2)
)

# Managed Objects groups

ciapGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2, 2, 1)
)
ciapGlobalGroup.setObjects(
      *(("CISCO-IP-ADDRESS-POOL-MIB", "ciapGlobalNotifyEnable"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapGlobalThresholdUnits"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapGlobalThresholdRising"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapGlobalThresholdFalling"))
)
if mibBuilder.loadTexts:
    ciapGlobalGroup.setStatus("current")

ciapPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2, 2, 2)
)
ciapPoolGroup.setObjects(
      *(("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolIdNext"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolName"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolStatus"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolStorage"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolType"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolContainedIn"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolThresholdUnits"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolThresholdRising"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolThresholdFalling"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolAddressesInUse"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolAddressesFree"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolTableChanged"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapAllocatedAddressMask"))
)
if mibBuilder.loadTexts:
    ciapPoolGroup.setStatus("current")

ciapRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2, 2, 3)
)
ciapRangeGroup.setObjects(
      *(("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeStatus"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeStorage"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeAddressUpper"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeCacheSize"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeRecycleDelay"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangePriority"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeThresholdUnits"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeThresholdRising"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeThresholdFalling"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeAddressesInUse"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeAddressesFree"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapRangeTableChanged"))
)
if mibBuilder.loadTexts:
    ciapRangeGroup.setStatus("current")

ciapPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2, 2, 4)
)
ciapPrefixGroup.setObjects(
      *(("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixStatus"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixStorage"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixAssignedLength"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixCacheSize"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixRecycleDelay"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixPriority"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixThresholdUnits"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixThresholdRising"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixThresholdFalling"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixPrefixesInUse"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixPrefixesFree"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPrefixTableChanged"))
)
if mibBuilder.loadTexts:
    ciapPrefixGroup.setStatus("current")

ciapPoolGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2, 2, 5)
)
ciapPoolGroupGroup.setObjects(
      *(("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupIdNext"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupName"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupThresholdUnits"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupThresholdRising"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupThresholdFalling"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupAddressesInUse"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupAddressesFree"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapPoolGroupContainsId"))
)
if mibBuilder.loadTexts:
    ciapPoolGroupGroup.setStatus("current")

ciapNotifDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2, 2, 6)
)
ciapNotifDataGroup.setObjects(
      *(("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyResource"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyThresholdUnits"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyThresholdRising"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyThresholdFalling"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyInUse"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyFree"))
)
if mibBuilder.loadTexts:
    ciapNotifDataGroup.setStatus("current")


# Notification objects

ciapEventThresholdRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 0, 1)
)
ciapEventThresholdRising.setObjects(
      *(("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyResource"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyThresholdUnits"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyThresholdRising"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyInUse"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyFree"))
)
if mibBuilder.loadTexts:
    ciapEventThresholdRising.setStatus(
        "current"
    )

ciapEventThresholdFalling = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 0, 2)
)
ciapEventThresholdFalling.setObjects(
      *(("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyResource"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyThresholdUnits"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyThresholdFalling"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyInUse"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapNotifyFree"))
)
if mibBuilder.loadTexts:
    ciapEventThresholdFalling.setStatus(
        "current"
    )


# Notifications groups

ciapNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2, 2, 7)
)
ciapNotifsGroup.setObjects(
      *(("CISCO-IP-ADDRESS-POOL-MIB", "ciapEventThresholdRising"),
        ("CISCO-IP-ADDRESS-POOL-MIB", "ciapEventThresholdFalling"))
)
if mibBuilder.loadTexts:
    ciapNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIpAddressPoolCompliance01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 748, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpAddressPoolCompliance01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-ADDRESS-POOL-MIB",
    **{"ciscoIpAddressPoolMIB": ciscoIpAddressPoolMIB,
       "ciscoIpAddressPoolMIBNotifs": ciscoIpAddressPoolMIBNotifs,
       "ciapEventThresholdRising": ciapEventThresholdRising,
       "ciapEventThresholdFalling": ciapEventThresholdFalling,
       "ciscoIpAddressPoolMIBObjects": ciscoIpAddressPoolMIBObjects,
       "ciapGlobal": ciapGlobal,
       "ciapGlobalNotifyEnable": ciapGlobalNotifyEnable,
       "ciapGlobalThresholdUnits": ciapGlobalThresholdUnits,
       "ciapGlobalThresholdRising": ciapGlobalThresholdRising,
       "ciapGlobalThresholdFalling": ciapGlobalThresholdFalling,
       "ciapPools": ciapPools,
       "ciapPoolIdNext": ciapPoolIdNext,
       "ciapPoolTable": ciapPoolTable,
       "ciapPoolEntry": ciapPoolEntry,
       "ciapPoolId": ciapPoolId,
       "ciapPoolStatus": ciapPoolStatus,
       "ciapPoolStorage": ciapPoolStorage,
       "ciapPoolName": ciapPoolName,
       "ciapPoolType": ciapPoolType,
       "ciapPoolContainedIn": ciapPoolContainedIn,
       "ciapPoolThresholdUnits": ciapPoolThresholdUnits,
       "ciapPoolThresholdRising": ciapPoolThresholdRising,
       "ciapPoolThresholdFalling": ciapPoolThresholdFalling,
       "ciapPoolAddressesInUse": ciapPoolAddressesInUse,
       "ciapPoolAddressesFree": ciapPoolAddressesFree,
       "ciapPoolTableChanged": ciapPoolTableChanged,
       "ciapRangeTable": ciapRangeTable,
       "ciapRangeEntry": ciapRangeEntry,
       "ciapRangeAddressType": ciapRangeAddressType,
       "ciapRangeAddressLower": ciapRangeAddressLower,
       "ciapRangeStatus": ciapRangeStatus,
       "ciapRangeStorage": ciapRangeStorage,
       "ciapRangeAddressUpper": ciapRangeAddressUpper,
       "ciapRangeCacheSize": ciapRangeCacheSize,
       "ciapRangeRecycleDelay": ciapRangeRecycleDelay,
       "ciapRangePriority": ciapRangePriority,
       "ciapRangeThresholdUnits": ciapRangeThresholdUnits,
       "ciapRangeThresholdRising": ciapRangeThresholdRising,
       "ciapRangeThresholdFalling": ciapRangeThresholdFalling,
       "ciapRangeAddressesInUse": ciapRangeAddressesInUse,
       "ciapRangeAddressesFree": ciapRangeAddressesFree,
       "ciapRangeTableChanged": ciapRangeTableChanged,
       "ciapPrefixTable": ciapPrefixTable,
       "ciapPrefixEntry": ciapPrefixEntry,
       "ciapPrefixType": ciapPrefixType,
       "ciapPrefixAddress": ciapPrefixAddress,
       "ciapPrefixAddressMask": ciapPrefixAddressMask,
       "ciapPrefixStatus": ciapPrefixStatus,
       "ciapPrefixStorage": ciapPrefixStorage,
       "ciapPrefixAssignedLength": ciapPrefixAssignedLength,
       "ciapPrefixCacheSize": ciapPrefixCacheSize,
       "ciapPrefixRecycleDelay": ciapPrefixRecycleDelay,
       "ciapPrefixPriority": ciapPrefixPriority,
       "ciapPrefixThresholdUnits": ciapPrefixThresholdUnits,
       "ciapPrefixThresholdRising": ciapPrefixThresholdRising,
       "ciapPrefixThresholdFalling": ciapPrefixThresholdFalling,
       "ciapPrefixPrefixesInUse": ciapPrefixPrefixesInUse,
       "ciapPrefixPrefixesFree": ciapPrefixPrefixesFree,
       "ciapPrefixTableChanged": ciapPrefixTableChanged,
       "ciapPoolGroups": ciapPoolGroups,
       "ciapPoolGroupIdNext": ciapPoolGroupIdNext,
       "ciapPoolGroupTable": ciapPoolGroupTable,
       "ciapPoolGroupEntry": ciapPoolGroupEntry,
       "ciapPoolGroupId": ciapPoolGroupId,
       "ciapPoolGroupName": ciapPoolGroupName,
       "ciapPoolGroupThresholdUnits": ciapPoolGroupThresholdUnits,
       "ciapPoolGroupThresholdRising": ciapPoolGroupThresholdRising,
       "ciapPoolGroupThresholdFalling": ciapPoolGroupThresholdFalling,
       "ciapPoolGroupAddressesInUse": ciapPoolGroupAddressesInUse,
       "ciapPoolGroupAddressesFree": ciapPoolGroupAddressesFree,
       "ciapPoolGroupContainsTable": ciapPoolGroupContainsTable,
       "ciapPoolGroupContainsEntry": ciapPoolGroupContainsEntry,
       "ciapPoolGroupContainsId": ciapPoolGroupContainsId,
       "ciapAllocatedAddresses": ciapAllocatedAddresses,
       "ciapAllocatedAddressTable": ciapAllocatedAddressTable,
       "ciapAllocatedAddressEntry": ciapAllocatedAddressEntry,
       "ciapAllocatedAddressType": ciapAllocatedAddressType,
       "ciapAllocatedAddress": ciapAllocatedAddress,
       "ciapAllocatedAddressMask": ciapAllocatedAddressMask,
       "ciapNotifyData": ciapNotifyData,
       "ciapNotifyResource": ciapNotifyResource,
       "ciapNotifyThresholdUnits": ciapNotifyThresholdUnits,
       "ciapNotifyThresholdRising": ciapNotifyThresholdRising,
       "ciapNotifyThresholdFalling": ciapNotifyThresholdFalling,
       "ciapNotifyInUse": ciapNotifyInUse,
       "ciapNotifyFree": ciapNotifyFree,
       "ciscoIpAddressPoolMIBConform": ciscoIpAddressPoolMIBConform,
       "ciscoIpAddressPoolMIBCompliances": ciscoIpAddressPoolMIBCompliances,
       "ciscoIpAddressPoolCompliance01": ciscoIpAddressPoolCompliance01,
       "ciscoIpAddressPoolMIBGroups": ciscoIpAddressPoolMIBGroups,
       "ciapGlobalGroup": ciapGlobalGroup,
       "ciapPoolGroup": ciapPoolGroup,
       "ciapRangeGroup": ciapRangeGroup,
       "ciapPrefixGroup": ciapPrefixGroup,
       "ciapPoolGroupGroup": ciapPoolGroupGroup,
       "ciapNotifDataGroup": ciapNotifDataGroup,
       "ciapNotifsGroup": ciapNotifsGroup}
)
