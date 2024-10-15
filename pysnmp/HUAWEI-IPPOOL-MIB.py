# SNMP MIB module (HUAWEI-IPPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-IPPOOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:09 2024
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

(huaweiUtility,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiUtility")

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwIppool = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8)
)
hwIppool.setRevisions(
        ("2015-08-12 00:00",
         "2015-03-31 00:00",
         "2015-02-11 00:00",
         "2014-12-26 00:00",
         "2014-12-26 00:00",
         "2014-07-25 00:00",
         "2014-03-14 00:00",
         "2013-11-28 00:00",
         "2013-11-08 00:00",
         "2013-10-17 00:00",
         "2013-07-27 00:00",
         "2013-07-19 00:00",
         "2013-05-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwIPPoolMibObjects_ObjectIdentity = ObjectIdentity
hwIPPoolMibObjects = _HwIPPoolMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1)
)
_HwIPPoolTable_Object = MibTable
hwIPPoolTable = _HwIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hwIPPoolTable.setStatus("current")
_HwIPPoolEntry_Object = MibTableRow
hwIPPoolEntry = _HwIPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1)
)
hwIPPoolEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
)
if mibBuilder.loadTexts:
    hwIPPoolEntry.setStatus("current")


class _HwIPPoolIndex_Type(Integer32):
    """Custom type hwIPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwIPPoolIndex_Type.__name__ = "Integer32"
_HwIPPoolIndex_Object = MibTableColumn
hwIPPoolIndex = _HwIPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 1),
    _HwIPPoolIndex_Type()
)
hwIPPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolIndex.setStatus("current")


class _HwIPPoolName_Type(DisplayString):
    """Custom type hwIPPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_HwIPPoolName_Type.__name__ = "DisplayString"
_HwIPPoolName_Object = MibTableColumn
hwIPPoolName = _HwIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 2),
    _HwIPPoolName_Type()
)
hwIPPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolName.setStatus("current")
_HwIPPoolRouterIPAddr_Type = IpAddress
_HwIPPoolRouterIPAddr_Object = MibTableColumn
hwIPPoolRouterIPAddr = _HwIPPoolRouterIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 3),
    _HwIPPoolRouterIPAddr_Type()
)
hwIPPoolRouterIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolRouterIPAddr.setStatus("current")
_HwIPPoolRouterIPMask_Type = IpAddress
_HwIPPoolRouterIPMask_Object = MibTableColumn
hwIPPoolRouterIPMask = _HwIPPoolRouterIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 4),
    _HwIPPoolRouterIPMask_Type()
)
hwIPPoolRouterIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolRouterIPMask.setStatus("current")
_HwIPPoolPriDNSIPAddr_Type = IpAddress
_HwIPPoolPriDNSIPAddr_Object = MibTableColumn
hwIPPoolPriDNSIPAddr = _HwIPPoolPriDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 5),
    _HwIPPoolPriDNSIPAddr_Type()
)
hwIPPoolPriDNSIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolPriDNSIPAddr.setStatus("current")
_HwIPPoolSecDNSIPAddr_Type = IpAddress
_HwIPPoolSecDNSIPAddr_Object = MibTableColumn
hwIPPoolSecDNSIPAddr = _HwIPPoolSecDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 6),
    _HwIPPoolSecDNSIPAddr_Type()
)
hwIPPoolSecDNSIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolSecDNSIPAddr.setStatus("current")
_HwIPPoolPriNBNSIPAddr_Type = IpAddress
_HwIPPoolPriNBNSIPAddr_Object = MibTableColumn
hwIPPoolPriNBNSIPAddr = _HwIPPoolPriNBNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 7),
    _HwIPPoolPriNBNSIPAddr_Type()
)
hwIPPoolPriNBNSIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolPriNBNSIPAddr.setStatus("current")
_HwIPPoolSecNBNSIPAddr_Type = IpAddress
_HwIPPoolSecNBNSIPAddr_Object = MibTableColumn
hwIPPoolSecNBNSIPAddr = _HwIPPoolSecNBNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 8),
    _HwIPPoolSecNBNSIPAddr_Type()
)
hwIPPoolSecNBNSIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolSecNBNSIPAddr.setStatus("current")
_HwIPPoolIPAddrLease_Type = Integer32
_HwIPPoolIPAddrLease_Object = MibTableColumn
hwIPPoolIPAddrLease = _HwIPPoolIPAddrLease_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 9),
    _HwIPPoolIPAddrLease_Type()
)
hwIPPoolIPAddrLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolIPAddrLease.setStatus("current")
_HwIPPoolStatus_Type = RowStatus
_HwIPPoolStatus_Object = MibTableColumn
hwIPPoolStatus = _HwIPPoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 10),
    _HwIPPoolStatus_Type()
)
hwIPPoolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolStatus.setStatus("current")


class _HwIPPoolVPNInstance_Type(DisplayString):
    """Custom type hwIPPoolVPNInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwIPPoolVPNInstance_Type.__name__ = "DisplayString"
_HwIPPoolVPNInstance_Object = MibTableColumn
hwIPPoolVPNInstance = _HwIPPoolVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 11),
    _HwIPPoolVPNInstance_Type()
)
hwIPPoolVPNInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolVPNInstance.setStatus("current")


class _HwIPPoolType_Type(Integer32):
    """Custom type hwIPPoolType based on Integer32"""
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
        *(("local", 1),
          ("localRuiSlave", 4),
          ("relay", 2),
          ("server", 3))
    )


_HwIPPoolType_Type.__name__ = "Integer32"
_HwIPPoolType_Object = MibTableColumn
hwIPPoolType = _HwIPPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 12),
    _HwIPPoolType_Type()
)
hwIPPoolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolType.setStatus("current")
_HwIPPoolNetwork_Type = IpAddress
_HwIPPoolNetwork_Object = MibTableColumn
hwIPPoolNetwork = _HwIPPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 13),
    _HwIPPoolNetwork_Type()
)
hwIPPoolNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolNetwork.setStatus("current")
_HwIPPoolNetworkMask_Type = IpAddress
_HwIPPoolNetworkMask_Object = MibTableColumn
hwIPPoolNetworkMask = _HwIPPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 14),
    _HwIPPoolNetworkMask_Type()
)
hwIPPoolNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolNetworkMask.setStatus("current")
_HwIPPoolIPTotalNum_Type = Integer32
_HwIPPoolIPTotalNum_Object = MibTableColumn
hwIPPoolIPTotalNum = _HwIPPoolIPTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 15),
    _HwIPPoolIPTotalNum_Type()
)
hwIPPoolIPTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolIPTotalNum.setStatus("current")
_HwIPPoolIPUsedNum_Type = Integer32
_HwIPPoolIPUsedNum_Object = MibTableColumn
hwIPPoolIPUsedNum = _HwIPPoolIPUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 16),
    _HwIPPoolIPUsedNum_Type()
)
hwIPPoolIPUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolIPUsedNum.setStatus("current")
_HwIPPoolIPConflictNum_Type = Integer32
_HwIPPoolIPConflictNum_Object = MibTableColumn
hwIPPoolIPConflictNum = _HwIPPoolIPConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 17),
    _HwIPPoolIPConflictNum_Type()
)
hwIPPoolIPConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolIPConflictNum.setStatus("current")
_HwIPPoolIPExcludeNum_Type = Integer32
_HwIPPoolIPExcludeNum_Object = MibTableColumn
hwIPPoolIPExcludeNum = _HwIPPoolIPExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 18),
    _HwIPPoolIPExcludeNum_Type()
)
hwIPPoolIPExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolIPExcludeNum.setStatus("current")
_HwIPPoolIPIdleNum_Type = Integer32
_HwIPPoolIPIdleNum_Object = MibTableColumn
hwIPPoolIPIdleNum = _HwIPPoolIPIdleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 19),
    _HwIPPoolIPIdleNum_Type()
)
hwIPPoolIPIdleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolIPIdleNum.setStatus("current")


class _HwIPPoolIPUsedPercent_Type(Integer32):
    """Custom type hwIPPoolIPUsedPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwIPPoolIPUsedPercent_Type.__name__ = "Integer32"
_HwIPPoolIPUsedPercent_Object = MibTableColumn
hwIPPoolIPUsedPercent = _HwIPPoolIPUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 20),
    _HwIPPoolIPUsedPercent_Type()
)
hwIPPoolIPUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolIPUsedPercent.setStatus("current")


class _HwIPPoolDNSIPAddrString_Type(OctetString):
    """Custom type hwIPPoolDNSIPAddrString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwIPPoolDNSIPAddrString_Type.__name__ = "OctetString"
_HwIPPoolDNSIPAddrString_Object = MibTableColumn
hwIPPoolDNSIPAddrString = _HwIPPoolDNSIPAddrString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 21),
    _HwIPPoolDNSIPAddrString_Type()
)
hwIPPoolDNSIPAddrString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolDNSIPAddrString.setStatus("current")


class _HwIPPoolDNSIPAddrStringUndo_Type(OctetString):
    """Custom type hwIPPoolDNSIPAddrStringUndo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwIPPoolDNSIPAddrStringUndo_Type.__name__ = "OctetString"
_HwIPPoolDNSIPAddrStringUndo_Object = MibTableColumn
hwIPPoolDNSIPAddrStringUndo = _HwIPPoolDNSIPAddrStringUndo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 22),
    _HwIPPoolDNSIPAddrStringUndo_Type()
)
hwIPPoolDNSIPAddrStringUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolDNSIPAddrStringUndo.setStatus("current")


class _HwIPPoolNBNSIPAddrString_Type(OctetString):
    """Custom type hwIPPoolNBNSIPAddrString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwIPPoolNBNSIPAddrString_Type.__name__ = "OctetString"
_HwIPPoolNBNSIPAddrString_Object = MibTableColumn
hwIPPoolNBNSIPAddrString = _HwIPPoolNBNSIPAddrString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 23),
    _HwIPPoolNBNSIPAddrString_Type()
)
hwIPPoolNBNSIPAddrString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolNBNSIPAddrString.setStatus("current")


class _HwIPPoolNBNSIPAddrStringUndo_Type(OctetString):
    """Custom type hwIPPoolNBNSIPAddrStringUndo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwIPPoolNBNSIPAddrStringUndo_Type.__name__ = "OctetString"
_HwIPPoolNBNSIPAddrStringUndo_Object = MibTableColumn
hwIPPoolNBNSIPAddrStringUndo = _HwIPPoolNBNSIPAddrStringUndo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 24),
    _HwIPPoolNBNSIPAddrStringUndo_Type()
)
hwIPPoolNBNSIPAddrStringUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolNBNSIPAddrStringUndo.setStatus("current")


class _HwIPPoolRouterUnnumberedIfName_Type(OctetString):
    """Custom type hwIPPoolRouterUnnumberedIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIPPoolRouterUnnumberedIfName_Type.__name__ = "OctetString"
_HwIPPoolRouterUnnumberedIfName_Object = MibTableColumn
hwIPPoolRouterUnnumberedIfName = _HwIPPoolRouterUnnumberedIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 25),
    _HwIPPoolRouterUnnumberedIfName_Type()
)
hwIPPoolRouterUnnumberedIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolRouterUnnumberedIfName.setStatus("current")


class _HwIPPoolConflictAutoRecycleInterval_Type(Integer32):
    """Custom type hwIPPoolConflictAutoRecycleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 1440),
    )


_HwIPPoolConflictAutoRecycleInterval_Type.__name__ = "Integer32"
_HwIPPoolConflictAutoRecycleInterval_Object = MibTableColumn
hwIPPoolConflictAutoRecycleInterval = _HwIPPoolConflictAutoRecycleInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 26),
    _HwIPPoolConflictAutoRecycleInterval_Type()
)
hwIPPoolConflictAutoRecycleInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolConflictAutoRecycleInterval.setStatus("current")
_HwIPPoolLowAddr_Type = IpAddress
_HwIPPoolLowAddr_Object = MibTableColumn
hwIPPoolLowAddr = _HwIPPoolLowAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 27),
    _HwIPPoolLowAddr_Type()
)
hwIPPoolLowAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolLowAddr.setStatus("current")
_HwIPPoolHighAddr_Type = IpAddress
_HwIPPoolHighAddr_Object = MibTableColumn
hwIPPoolHighAddr = _HwIPPoolHighAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 28),
    _HwIPPoolHighAddr_Type()
)
hwIPPoolHighAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolHighAddr.setStatus("current")
_HwIPPoolReqNum_Type = Integer32
_HwIPPoolReqNum_Object = MibTableColumn
hwIPPoolReqNum = _HwIPPoolReqNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 29),
    _HwIPPoolReqNum_Type()
)
hwIPPoolReqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolReqNum.setStatus("current")
_HwIPPoolReqSucNum_Type = Integer32
_HwIPPoolReqSucNum_Object = MibTableColumn
hwIPPoolReqSucNum = _HwIPPoolReqSucNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 1, 1, 30),
    _HwIPPoolReqSucNum_Type()
)
hwIPPoolReqSucNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolReqSucNum.setStatus("current")
_HwIPSectionTable_Object = MibTable
hwIPSectionTable = _HwIPSectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hwIPSectionTable.setStatus("current")
_HwIPSectionEntry_Object = MibTableRow
hwIPSectionEntry = _HwIPSectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1)
)
hwIPSectionEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPSectionIndex"),
)
if mibBuilder.loadTexts:
    hwIPSectionEntry.setStatus("current")


class _HwIPSectionIndex_Type(Integer32):
    """Custom type hwIPSectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwIPSectionIndex_Type.__name__ = "Integer32"
_HwIPSectionIndex_Object = MibTableColumn
hwIPSectionIndex = _HwIPSectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1, 1),
    _HwIPSectionIndex_Type()
)
hwIPSectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSectionIndex.setStatus("current")


class _HwIPSectionDesc_Type(DisplayString):
    """Custom type hwIPSectionDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPSectionDesc_Type.__name__ = "DisplayString"
_HwIPSectionDesc_Object = MibTableColumn
hwIPSectionDesc = _HwIPSectionDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1, 2),
    _HwIPSectionDesc_Type()
)
hwIPSectionDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPSectionDesc.setStatus("current")
_HwIPSectionLowAddr_Type = IpAddress
_HwIPSectionLowAddr_Object = MibTableColumn
hwIPSectionLowAddr = _HwIPSectionLowAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1, 3),
    _HwIPSectionLowAddr_Type()
)
hwIPSectionLowAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPSectionLowAddr.setStatus("current")
_HwIPSectionHighAddr_Type = IpAddress
_HwIPSectionHighAddr_Object = MibTableColumn
hwIPSectionHighAddr = _HwIPSectionHighAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1, 4),
    _HwIPSectionHighAddr_Type()
)
hwIPSectionHighAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPSectionHighAddr.setStatus("current")


class _HwIPSectionLength_Type(Integer32):
    """Custom type hwIPSectionLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwIPSectionLength_Type.__name__ = "Integer32"
_HwIPSectionLength_Object = MibTableColumn
hwIPSectionLength = _HwIPSectionLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1, 5),
    _HwIPSectionLength_Type()
)
hwIPSectionLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSectionLength.setStatus("current")


class _HwIPSectionUsedNum_Type(Integer32):
    """Custom type hwIPSectionUsedNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwIPSectionUsedNum_Type.__name__ = "Integer32"
_HwIPSectionUsedNum_Object = MibTableColumn
hwIPSectionUsedNum = _HwIPSectionUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1, 6),
    _HwIPSectionUsedNum_Type()
)
hwIPSectionUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSectionUsedNum.setStatus("current")


class _HwIPSectionConflict_Type(Integer32):
    """Custom type hwIPSectionConflict based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwIPSectionConflict_Type.__name__ = "Integer32"
_HwIPSectionConflict_Object = MibTableColumn
hwIPSectionConflict = _HwIPSectionConflict_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1, 7),
    _HwIPSectionConflict_Type()
)
hwIPSectionConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSectionConflict.setStatus("current")


class _HwIPSectionInvalid_Type(Integer32):
    """Custom type hwIPSectionInvalid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwIPSectionInvalid_Type.__name__ = "Integer32"
_HwIPSectionInvalid_Object = MibTableColumn
hwIPSectionInvalid = _HwIPSectionInvalid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1, 8),
    _HwIPSectionInvalid_Type()
)
hwIPSectionInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSectionInvalid.setStatus("current")


class _HwIPSectionAvailableNum_Type(Integer32):
    """Custom type hwIPSectionAvailableNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwIPSectionAvailableNum_Type.__name__ = "Integer32"
_HwIPSectionAvailableNum_Object = MibTableColumn
hwIPSectionAvailableNum = _HwIPSectionAvailableNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1, 9),
    _HwIPSectionAvailableNum_Type()
)
hwIPSectionAvailableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPSectionAvailableNum.setStatus("current")
_HwIPSectionRowStatus_Type = RowStatus
_HwIPSectionRowStatus_Object = MibTableColumn
hwIPSectionRowStatus = _HwIPSectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 2, 1, 10),
    _HwIPSectionRowStatus_Type()
)
hwIPSectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPSectionRowStatus.setStatus("current")
_HwIPPoolExtTable_Object = MibTable
hwIPPoolExtTable = _HwIPPoolExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hwIPPoolExtTable.setStatus("current")
_HwIPPoolExtEntry_Object = MibTableRow
hwIPPoolExtEntry = _HwIPPoolExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1)
)
hwIPPoolExtEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
)
if mibBuilder.loadTexts:
    hwIPPoolExtEntry.setStatus("current")


class _HwIPPoolAvailableStatus_Type(Integer32):
    """Custom type hwIPPoolAvailableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwIPPoolAvailableStatus_Type.__name__ = "Integer32"
_HwIPPoolAvailableStatus_Object = MibTableColumn
hwIPPoolAvailableStatus = _HwIPPoolAvailableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 1),
    _HwIPPoolAvailableStatus_Type()
)
hwIPPoolAvailableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolAvailableStatus.setStatus("current")


class _HwIPDhcpOptionId1_Type(Integer32):
    """Custom type hwIPDhcpOptionId1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 255),
    )


_HwIPDhcpOptionId1_Type.__name__ = "Integer32"
_HwIPDhcpOptionId1_Object = MibTableColumn
hwIPDhcpOptionId1 = _HwIPDhcpOptionId1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 2),
    _HwIPDhcpOptionId1_Type()
)
hwIPDhcpOptionId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpOptionId1.setStatus("current")


class _HwIPDhcpOption1_Type(DisplayString):
    """Custom type hwIPDhcpOption1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIPDhcpOption1_Type.__name__ = "DisplayString"
_HwIPDhcpOption1_Object = MibTableColumn
hwIPDhcpOption1 = _HwIPDhcpOption1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 3),
    _HwIPDhcpOption1_Type()
)
hwIPDhcpOption1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpOption1.setStatus("current")


class _HwIPDhcpOptionId2_Type(Integer32):
    """Custom type hwIPDhcpOptionId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 255),
    )


_HwIPDhcpOptionId2_Type.__name__ = "Integer32"
_HwIPDhcpOptionId2_Object = MibTableColumn
hwIPDhcpOptionId2 = _HwIPDhcpOptionId2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 4),
    _HwIPDhcpOptionId2_Type()
)
hwIPDhcpOptionId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpOptionId2.setStatus("current")


class _HwIPDhcpOption2_Type(DisplayString):
    """Custom type hwIPDhcpOption2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIPDhcpOption2_Type.__name__ = "DisplayString"
_HwIPDhcpOption2_Object = MibTableColumn
hwIPDhcpOption2 = _HwIPDhcpOption2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 5),
    _HwIPDhcpOption2_Type()
)
hwIPDhcpOption2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpOption2.setStatus("current")


class _HwIPDhcpOptionId3_Type(Integer32):
    """Custom type hwIPDhcpOptionId3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 255),
    )


_HwIPDhcpOptionId3_Type.__name__ = "Integer32"
_HwIPDhcpOptionId3_Object = MibTableColumn
hwIPDhcpOptionId3 = _HwIPDhcpOptionId3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 6),
    _HwIPDhcpOptionId3_Type()
)
hwIPDhcpOptionId3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpOptionId3.setStatus("current")


class _HwIPDhcpOption3_Type(DisplayString):
    """Custom type hwIPDhcpOption3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIPDhcpOption3_Type.__name__ = "DisplayString"
_HwIPDhcpOption3_Object = MibTableColumn
hwIPDhcpOption3 = _HwIPDhcpOption3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 7),
    _HwIPDhcpOption3_Type()
)
hwIPDhcpOption3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpOption3.setStatus("current")


class _HwIPDhcpOptionId4_Type(Integer32):
    """Custom type hwIPDhcpOptionId4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 255),
    )


_HwIPDhcpOptionId4_Type.__name__ = "Integer32"
_HwIPDhcpOptionId4_Object = MibTableColumn
hwIPDhcpOptionId4 = _HwIPDhcpOptionId4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 8),
    _HwIPDhcpOptionId4_Type()
)
hwIPDhcpOptionId4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpOptionId4.setStatus("current")


class _HwIPDhcpOption4_Type(DisplayString):
    """Custom type hwIPDhcpOption4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIPDhcpOption4_Type.__name__ = "DisplayString"
_HwIPDhcpOption4_Object = MibTableColumn
hwIPDhcpOption4 = _HwIPDhcpOption4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 9),
    _HwIPDhcpOption4_Type()
)
hwIPDhcpOption4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpOption4.setStatus("current")


class _HwIPDnsSuffix_Type(DisplayString):
    """Custom type hwIPDnsSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HwIPDnsSuffix_Type.__name__ = "DisplayString"
_HwIPDnsSuffix_Object = MibTableColumn
hwIPDnsSuffix = _HwIPDnsSuffix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 10),
    _HwIPDnsSuffix_Type()
)
hwIPDnsSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDnsSuffix.setStatus("current")


class _HwIPDhcpSvrIPRsv_Type(Integer32):
    """Custom type hwIPDhcpSvrIPRsv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIPDhcpSvrIPRsv_Type.__name__ = "Integer32"
_HwIPDhcpSvrIPRsv_Object = MibTableColumn
hwIPDhcpSvrIPRsv = _HwIPDhcpSvrIPRsv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 11),
    _HwIPDhcpSvrIPRsv_Type()
)
hwIPDhcpSvrIPRsv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpSvrIPRsv.setStatus("current")
_HwIPPoolIpAddrRenewal_Type = Integer32
_HwIPPoolIpAddrRenewal_Object = MibTableColumn
hwIPPoolIpAddrRenewal = _HwIPPoolIpAddrRenewal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 12),
    _HwIPPoolIpAddrRenewal_Type()
)
hwIPPoolIpAddrRenewal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolIpAddrRenewal.setStatus("current")
_HwIPPoolIpAddrRebinding_Type = Integer32
_HwIPPoolIpAddrRebinding_Object = MibTableColumn
hwIPPoolIpAddrRebinding = _HwIPPoolIpAddrRebinding_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 13),
    _HwIPPoolIpAddrRebinding_Type()
)
hwIPPoolIpAddrRebinding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolIpAddrRebinding.setStatus("current")
_HwIPPoolSIPAddr1_Type = IpAddress
_HwIPPoolSIPAddr1_Object = MibTableColumn
hwIPPoolSIPAddr1 = _HwIPPoolSIPAddr1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 14),
    _HwIPPoolSIPAddr1_Type()
)
hwIPPoolSIPAddr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolSIPAddr1.setStatus("current")
_HwIPPoolSIPAddr2_Type = IpAddress
_HwIPPoolSIPAddr2_Object = MibTableColumn
hwIPPoolSIPAddr2 = _HwIPPoolSIPAddr2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 15),
    _HwIPPoolSIPAddr2_Type()
)
hwIPPoolSIPAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolSIPAddr2.setStatus("current")


class _HwIPPoolSIPName1_Type(DisplayString):
    """Custom type hwIPPoolSIPName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwIPPoolSIPName1_Type.__name__ = "DisplayString"
_HwIPPoolSIPName1_Object = MibTableColumn
hwIPPoolSIPName1 = _HwIPPoolSIPName1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 16),
    _HwIPPoolSIPName1_Type()
)
hwIPPoolSIPName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolSIPName1.setStatus("current")


class _HwIPPoolSIPName2_Type(DisplayString):
    """Custom type hwIPPoolSIPName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwIPPoolSIPName2_Type.__name__ = "DisplayString"
_HwIPPoolSIPName2_Object = MibTableColumn
hwIPPoolSIPName2 = _HwIPPoolSIPName2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 3, 1, 17),
    _HwIPPoolSIPName2_Type()
)
hwIPPoolSIPName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolSIPName2.setStatus("current")
_HwIPAddressStatusTable_Object = MibTable
hwIPAddressStatusTable = _HwIPAddressStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 4)
)
if mibBuilder.loadTexts:
    hwIPAddressStatusTable.setStatus("current")
_HwIPAddressStatusEntry_Object = MibTableRow
hwIPAddressStatusEntry = _HwIPAddressStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 4, 1)
)
hwIPAddressStatusEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPSectionIndex"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPAddress"),
)
if mibBuilder.loadTexts:
    hwIPAddressStatusEntry.setStatus("current")
_HwIPAddress_Type = IpAddress
_HwIPAddress_Object = MibTableColumn
hwIPAddress = _HwIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 4, 1, 1),
    _HwIPAddress_Type()
)
hwIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPAddress.setStatus("current")


class _HwIPAddressStatus_Type(Integer32):
    """Custom type hwIPAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("conflictive", 3),
          ("idle", 0),
          ("occupied", 1),
          ("prohibitive", 2))
    )


_HwIPAddressStatus_Type.__name__ = "Integer32"
_HwIPAddressStatus_Object = MibTableColumn
hwIPAddressStatus = _HwIPAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 4, 1, 2),
    _HwIPAddressStatus_Type()
)
hwIPAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPAddressStatus.setStatus("current")


class _HwPoolName_Type(DisplayString):
    """Custom type hwPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwPoolName_Type.__name__ = "DisplayString"
_HwPoolName_Object = MibTableColumn
hwPoolName = _HwPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 4, 1, 3),
    _HwPoolName_Type()
)
hwPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoolName.setStatus("current")
_HwDhcpSvrGroupTable_Object = MibTable
hwDhcpSvrGroupTable = _HwDhcpSvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5)
)
if mibBuilder.loadTexts:
    hwDhcpSvrGroupTable.setStatus("current")
_HwDhcpSvrGroupEntry_Object = MibTableRow
hwDhcpSvrGroupEntry = _HwDhcpSvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1)
)
hwDhcpSvrGroupEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpSvrGroupIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpSvrGroupEntry.setStatus("current")


class _HwIPPoolDhcpSvrGroupIndex_Type(Integer32):
    """Custom type hwIPPoolDhcpSvrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwIPPoolDhcpSvrGroupIndex_Type.__name__ = "Integer32"
_HwIPPoolDhcpSvrGroupIndex_Object = MibTableColumn
hwIPPoolDhcpSvrGroupIndex = _HwIPPoolDhcpSvrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 1),
    _HwIPPoolDhcpSvrGroupIndex_Type()
)
hwIPPoolDhcpSvrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolDhcpSvrGroupIndex.setStatus("current")


class _HwIPPoolDhcpSvrGroupName_Type(DisplayString):
    """Custom type hwIPPoolDhcpSvrGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPPoolDhcpSvrGroupName_Type.__name__ = "DisplayString"
_HwIPPoolDhcpSvrGroupName_Object = MibTableColumn
hwIPPoolDhcpSvrGroupName = _HwIPPoolDhcpSvrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 2),
    _HwIPPoolDhcpSvrGroupName_Type()
)
hwIPPoolDhcpSvrGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolDhcpSvrGroupName.setStatus("current")
_HwIPDhcpSvrPriAddr_Type = IpAddress
_HwIPDhcpSvrPriAddr_Object = MibTableColumn
hwIPDhcpSvrPriAddr = _HwIPDhcpSvrPriAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 3),
    _HwIPDhcpSvrPriAddr_Type()
)
hwIPDhcpSvrPriAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpSvrPriAddr.setStatus("current")
_HwIPDhcpSvrScdiAddr_Type = IpAddress
_HwIPDhcpSvrScdiAddr_Object = MibTableColumn
hwIPDhcpSvrScdiAddr = _HwIPDhcpSvrScdiAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 4),
    _HwIPDhcpSvrScdiAddr_Type()
)
hwIPDhcpSvrScdiAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpSvrScdiAddr.setStatus("current")


class _HwIPDhcpSvrPriState_Type(Integer32):
    """Custom type hwIPDhcpSvrPriState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stop", 0),
          ("use", 1))
    )


_HwIPDhcpSvrPriState_Type.__name__ = "Integer32"
_HwIPDhcpSvrPriState_Object = MibTableColumn
hwIPDhcpSvrPriState = _HwIPDhcpSvrPriState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 5),
    _HwIPDhcpSvrPriState_Type()
)
hwIPDhcpSvrPriState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpSvrPriState.setStatus("current")


class _HwIPDhcpScdPriState_Type(Integer32):
    """Custom type hwIPDhcpScdPriState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stop", 0),
          ("use", 1))
    )


_HwIPDhcpScdPriState_Type.__name__ = "Integer32"
_HwIPDhcpScdPriState_Object = MibTableColumn
hwIPDhcpScdPriState = _HwIPDhcpScdPriState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 6),
    _HwIPDhcpScdPriState_Type()
)
hwIPDhcpScdPriState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpScdPriState.setStatus("current")
_HwIPDhcpSvrAutoRelease_Type = TruthValue
_HwIPDhcpSvrAutoRelease_Object = MibTableColumn
hwIPDhcpSvrAutoRelease = _HwIPDhcpSvrAutoRelease_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 7),
    _HwIPDhcpSvrAutoRelease_Type()
)
hwIPDhcpSvrAutoRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpSvrAutoRelease.setStatus("current")


class _HwIPDhcpSvrRefCount_Type(Integer32):
    """Custom type hwIPDhcpSvrRefCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwIPDhcpSvrRefCount_Type.__name__ = "Integer32"
_HwIPDhcpSvrRefCount_Object = MibTableColumn
hwIPDhcpSvrRefCount = _HwIPDhcpSvrRefCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 8),
    _HwIPDhcpSvrRefCount_Type()
)
hwIPDhcpSvrRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpSvrRefCount.setStatus("current")
_HwIPDhcpSvrRowStatus_Type = RowStatus
_HwIPDhcpSvrRowStatus_Object = MibTableColumn
hwIPDhcpSvrRowStatus = _HwIPDhcpSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 9),
    _HwIPDhcpSvrRowStatus_Type()
)
hwIPDhcpSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpSvrRowStatus.setStatus("current")


class _HwIPDhcpSvrPriVpnInstance_Type(DisplayString):
    """Custom type hwIPDhcpSvrPriVpnInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwIPDhcpSvrPriVpnInstance_Type.__name__ = "DisplayString"
_HwIPDhcpSvrPriVpnInstance_Object = MibTableColumn
hwIPDhcpSvrPriVpnInstance = _HwIPDhcpSvrPriVpnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 10),
    _HwIPDhcpSvrPriVpnInstance_Type()
)
hwIPDhcpSvrPriVpnInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpSvrPriVpnInstance.setStatus("current")


class _HwIPDhcpSvrScdVpnInstance_Type(DisplayString):
    """Custom type hwIPDhcpSvrScdVpnInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwIPDhcpSvrScdVpnInstance_Type.__name__ = "DisplayString"
_HwIPDhcpSvrScdVpnInstance_Object = MibTableColumn
hwIPDhcpSvrScdVpnInstance = _HwIPDhcpSvrScdVpnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 11),
    _HwIPDhcpSvrScdVpnInstance_Type()
)
hwIPDhcpSvrScdVpnInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpSvrScdVpnInstance.setStatus("current")


class _HwIPDhcpSvrSouce_Type(OctetString):
    """Custom type hwIPDhcpSvrSouce based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwIPDhcpSvrSouce_Type.__name__ = "OctetString"
_HwIPDhcpSvrSouce_Object = MibTableColumn
hwIPDhcpSvrSouce = _HwIPDhcpSvrSouce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 5, 1, 12),
    _HwIPDhcpSvrSouce_Type()
)
hwIPDhcpSvrSouce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpSvrSouce.setStatus("current")
_HwRemotePoolTable_Object = MibTable
hwRemotePoolTable = _HwRemotePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6)
)
if mibBuilder.loadTexts:
    hwRemotePoolTable.setStatus("current")
_HwRemotePoolEntry_Object = MibTableRow
hwRemotePoolEntry = _HwRemotePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1)
)
hwRemotePoolEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolIndex"),
)
if mibBuilder.loadTexts:
    hwRemotePoolEntry.setStatus("current")


class _HwRemoteIPPoolIndex_Type(Integer32):
    """Custom type hwRemoteIPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwRemoteIPPoolIndex_Type.__name__ = "Integer32"
_HwRemoteIPPoolIndex_Object = MibTableColumn
hwRemoteIPPoolIndex = _HwRemoteIPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 1),
    _HwRemoteIPPoolIndex_Type()
)
hwRemoteIPPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRemoteIPPoolIndex.setStatus("current")


class _HwRemoteIPPoolName_Type(DisplayString):
    """Custom type hwRemoteIPPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwRemoteIPPoolName_Type.__name__ = "DisplayString"
_HwRemoteIPPoolName_Object = MibTableColumn
hwRemoteIPPoolName = _HwRemoteIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 2),
    _HwRemoteIPPoolName_Type()
)
hwRemoteIPPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteIPPoolName.setStatus("current")
_HwRemoteIPPoolRouterIPAddr_Type = IpAddress
_HwRemoteIPPoolRouterIPAddr_Object = MibTableColumn
hwRemoteIPPoolRouterIPAddr = _HwRemoteIPPoolRouterIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 3),
    _HwRemoteIPPoolRouterIPAddr_Type()
)
hwRemoteIPPoolRouterIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolRouterIPAddr.setStatus("current")
_HwRemoteIPPoolRouterIPMask_Type = IpAddress
_HwRemoteIPPoolRouterIPMask_Object = MibTableColumn
hwRemoteIPPoolRouterIPMask = _HwRemoteIPPoolRouterIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 4),
    _HwRemoteIPPoolRouterIPMask_Type()
)
hwRemoteIPPoolRouterIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolRouterIPMask.setStatus("current")


class _HwRemoteIPPoolDhcpSvrGroupID_Type(Integer32):
    """Custom type hwRemoteIPPoolDhcpSvrGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwRemoteIPPoolDhcpSvrGroupID_Type.__name__ = "Integer32"
_HwRemoteIPPoolDhcpSvrGroupID_Object = MibTableColumn
hwRemoteIPPoolDhcpSvrGroupID = _HwRemoteIPPoolDhcpSvrGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 5),
    _HwRemoteIPPoolDhcpSvrGroupID_Type()
)
hwRemoteIPPoolDhcpSvrGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolDhcpSvrGroupID.setStatus("current")


class _HwRemoteIPPoolAvailableStatus_Type(Integer32):
    """Custom type hwRemoteIPPoolAvailableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_HwRemoteIPPoolAvailableStatus_Type.__name__ = "Integer32"
_HwRemoteIPPoolAvailableStatus_Object = MibTableColumn
hwRemoteIPPoolAvailableStatus = _HwRemoteIPPoolAvailableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 6),
    _HwRemoteIPPoolAvailableStatus_Type()
)
hwRemoteIPPoolAvailableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolAvailableStatus.setStatus("current")
_HwRemoteIPPoolRowStatus_Type = RowStatus
_HwRemoteIPPoolRowStatus_Object = MibTableColumn
hwRemoteIPPoolRowStatus = _HwRemoteIPPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 7),
    _HwRemoteIPPoolRowStatus_Type()
)
hwRemoteIPPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteIPPoolRowStatus.setStatus("current")
_HwRemoteIPPoolPriDNSIPAddress_Type = IpAddress
_HwRemoteIPPoolPriDNSIPAddress_Object = MibTableColumn
hwRemoteIPPoolPriDNSIPAddress = _HwRemoteIPPoolPriDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 8),
    _HwRemoteIPPoolPriDNSIPAddress_Type()
)
hwRemoteIPPoolPriDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolPriDNSIPAddress.setStatus("current")
_HwRemoteIPPoolSecDNSIPAddress_Type = IpAddress
_HwRemoteIPPoolSecDNSIPAddress_Object = MibTableColumn
hwRemoteIPPoolSecDNSIPAddress = _HwRemoteIPPoolSecDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 9),
    _HwRemoteIPPoolSecDNSIPAddress_Type()
)
hwRemoteIPPoolSecDNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolSecDNSIPAddress.setStatus("current")
_HwRemoteIPPoolPriNBNSIPAddress_Type = IpAddress
_HwRemoteIPPoolPriNBNSIPAddress_Object = MibTableColumn
hwRemoteIPPoolPriNBNSIPAddress = _HwRemoteIPPoolPriNBNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 10),
    _HwRemoteIPPoolPriNBNSIPAddress_Type()
)
hwRemoteIPPoolPriNBNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolPriNBNSIPAddress.setStatus("current")
_HwRemoteIPPoolSecNBNSIPAddress_Type = IpAddress
_HwRemoteIPPoolSecNBNSIPAddress_Object = MibTableColumn
hwRemoteIPPoolSecNBNSIPAddress = _HwRemoteIPPoolSecNBNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 11),
    _HwRemoteIPPoolSecNBNSIPAddress_Type()
)
hwRemoteIPPoolSecNBNSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolSecNBNSIPAddress.setStatus("current")


class _HwRemoteIPPoolVPNInstance_Type(DisplayString):
    """Custom type hwRemoteIPPoolVPNInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRemoteIPPoolVPNInstance_Type.__name__ = "DisplayString"
_HwRemoteIPPoolVPNInstance_Object = MibTableColumn
hwRemoteIPPoolVPNInstance = _HwRemoteIPPoolVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 12),
    _HwRemoteIPPoolVPNInstance_Type()
)
hwRemoteIPPoolVPNInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolVPNInstance.setStatus("current")


class _HwRemoteIPPoolDhcpGroupName_Type(DisplayString):
    """Custom type hwRemoteIPPoolDhcpGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwRemoteIPPoolDhcpGroupName_Type.__name__ = "DisplayString"
_HwRemoteIPPoolDhcpGroupName_Object = MibTableColumn
hwRemoteIPPoolDhcpGroupName = _HwRemoteIPPoolDhcpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 13),
    _HwRemoteIPPoolDhcpGroupName_Type()
)
hwRemoteIPPoolDhcpGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRemoteIPPoolDhcpGroupName.setStatus("current")


class _HwRemoteIPPoolLeaseManageEnable_Type(Integer32):
    """Custom type hwRemoteIPPoolLeaseManageEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwRemoteIPPoolLeaseManageEnable_Type.__name__ = "Integer32"
_HwRemoteIPPoolLeaseManageEnable_Object = MibTableColumn
hwRemoteIPPoolLeaseManageEnable = _HwRemoteIPPoolLeaseManageEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 14),
    _HwRemoteIPPoolLeaseManageEnable_Type()
)
hwRemoteIPPoolLeaseManageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolLeaseManageEnable.setStatus("current")


class _HwRemoteIPPoolWeight_Type(Integer32):
    """Custom type hwRemoteIPPoolWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwRemoteIPPoolWeight_Type.__name__ = "Integer32"
_HwRemoteIPPoolWeight_Object = MibTableColumn
hwRemoteIPPoolWeight = _HwRemoteIPPoolWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 6, 1, 15),
    _HwRemoteIPPoolWeight_Type()
)
hwRemoteIPPoolWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRemoteIPPoolWeight.setStatus("current")
_HwIPPoolStatistic_ObjectIdentity = ObjectIdentity
hwIPPoolStatistic = _HwIPPoolStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 7)
)
_HwIPPoolNum_Type = Integer32
_HwIPPoolNum_Object = MibScalar
hwIPPoolNum = _HwIPPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 7, 1),
    _HwIPPoolNum_Type()
)
hwIPPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolNum.setStatus("current")
_HwIPIdleTotalNum_Type = Integer32
_HwIPIdleTotalNum_Object = MibScalar
hwIPIdleTotalNum = _HwIPIdleTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 7, 2),
    _HwIPIdleTotalNum_Type()
)
hwIPIdleTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPIdleTotalNum.setStatus("current")
_HwIPUsedTotalNum_Type = Integer32
_HwIPUsedTotalNum_Object = MibScalar
hwIPUsedTotalNum = _HwIPUsedTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 7, 3),
    _HwIPUsedTotalNum_Type()
)
hwIPUsedTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPUsedTotalNum.setStatus("current")
_HwIPConflictTotalNum_Type = Integer32
_HwIPConflictTotalNum_Object = MibScalar
hwIPConflictTotalNum = _HwIPConflictTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 7, 4),
    _HwIPConflictTotalNum_Type()
)
hwIPConflictTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPConflictTotalNum.setStatus("current")
_HwIPExcludeTotalNum_Type = Integer32
_HwIPExcludeTotalNum_Object = MibScalar
hwIPExcludeTotalNum = _HwIPExcludeTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 7, 5),
    _HwIPExcludeTotalNum_Type()
)
hwIPExcludeTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPExcludeTotalNum.setStatus("current")
_HwIPTotalNum_Type = Integer32
_HwIPTotalNum_Object = MibScalar
hwIPTotalNum = _HwIPTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 7, 6),
    _HwIPTotalNum_Type()
)
hwIPTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPTotalNum.setStatus("current")
_HwIPUsedPercent_Type = Integer32
_HwIPUsedPercent_Object = MibScalar
hwIPUsedPercent = _HwIPUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 7, 7),
    _HwIPUsedPercent_Type()
)
hwIPUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPUsedPercent.setStatus("current")
_HwDhcpServerTable_Object = MibTable
hwDhcpServerTable = _HwDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8)
)
if mibBuilder.loadTexts:
    hwDhcpServerTable.setStatus("current")
_HwDhcpServerEntry_Object = MibTableRow
hwDhcpServerEntry = _HwDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1)
)
hwDhcpServerEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwDhcpServerIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpServerEntry.setStatus("current")


class _HwDhcpServerIndex_Type(Integer32):
    """Custom type hwDhcpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwDhcpServerIndex_Type.__name__ = "Integer32"
_HwDhcpServerIndex_Object = MibTableColumn
hwDhcpServerIndex = _HwDhcpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1, 1),
    _HwDhcpServerIndex_Type()
)
hwDhcpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpServerIndex.setStatus("current")
_HwIPPoolDhcpServerIP_Type = IpAddress
_HwIPPoolDhcpServerIP_Object = MibTableColumn
hwIPPoolDhcpServerIP = _HwIPPoolDhcpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1, 2),
    _HwIPPoolDhcpServerIP_Type()
)
hwIPPoolDhcpServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolDhcpServerIP.setStatus("current")


class _HwIPPoolDhcpServerVRFName_Type(OctetString):
    """Custom type hwIPPoolDhcpServerVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwIPPoolDhcpServerVRFName_Type.__name__ = "OctetString"
_HwIPPoolDhcpServerVRFName_Object = MibTableColumn
hwIPPoolDhcpServerVRFName = _HwIPPoolDhcpServerVRFName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1, 3),
    _HwIPPoolDhcpServerVRFName_Type()
)
hwIPPoolDhcpServerVRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolDhcpServerVRFName.setStatus("current")


class _HwIPPoolDhcpServerState_Type(Integer32):
    """Custom type hwIPPoolDhcpServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HwIPPoolDhcpServerState_Type.__name__ = "Integer32"
_HwIPPoolDhcpServerState_Object = MibTableColumn
hwIPPoolDhcpServerState = _HwIPPoolDhcpServerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1, 4),
    _HwIPPoolDhcpServerState_Type()
)
hwIPPoolDhcpServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolDhcpServerState.setStatus("current")


class _HwIPPoolDhcpServerSendDisvSpdNum_Type(Integer32):
    """Custom type hwIPPoolDhcpServerSendDisvSpdNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIPPoolDhcpServerSendDisvSpdNum_Type.__name__ = "Integer32"
_HwIPPoolDhcpServerSendDisvSpdNum_Object = MibTableColumn
hwIPPoolDhcpServerSendDisvSpdNum = _HwIPPoolDhcpServerSendDisvSpdNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1, 5),
    _HwIPPoolDhcpServerSendDisvSpdNum_Type()
)
hwIPPoolDhcpServerSendDisvSpdNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolDhcpServerSendDisvSpdNum.setStatus("current")


class _HwIPPoolDhcpServerSendDisvSpdSec_Type(Integer32):
    """Custom type hwIPPoolDhcpServerSendDisvSpdSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIPPoolDhcpServerSendDisvSpdSec_Type.__name__ = "Integer32"
_HwIPPoolDhcpServerSendDisvSpdSec_Object = MibTableColumn
hwIPPoolDhcpServerSendDisvSpdSec = _HwIPPoolDhcpServerSendDisvSpdSec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1, 6),
    _HwIPPoolDhcpServerSendDisvSpdSec_Type()
)
hwIPPoolDhcpServerSendDisvSpdSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolDhcpServerSendDisvSpdSec.setStatus("current")


class _HwIPPoolDhcpServerDeadCount_Type(Integer32):
    """Custom type hwIPPoolDhcpServerDeadCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwIPPoolDhcpServerDeadCount_Type.__name__ = "Integer32"
_HwIPPoolDhcpServerDeadCount_Object = MibTableColumn
hwIPPoolDhcpServerDeadCount = _HwIPPoolDhcpServerDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1, 7),
    _HwIPPoolDhcpServerDeadCount_Type()
)
hwIPPoolDhcpServerDeadCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolDhcpServerDeadCount.setStatus("current")


class _HwIPPoolDhcpServerNakCount_Type(Integer32):
    """Custom type hwIPPoolDhcpServerNakCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIPPoolDhcpServerNakCount_Type.__name__ = "Integer32"
_HwIPPoolDhcpServerNakCount_Object = MibTableColumn
hwIPPoolDhcpServerNakCount = _HwIPPoolDhcpServerNakCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1, 8),
    _HwIPPoolDhcpServerNakCount_Type()
)
hwIPPoolDhcpServerNakCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolDhcpServerNakCount.setStatus("current")


class _HwIPPoolDhcpServerTimeout_Type(Integer32):
    """Custom type hwIPPoolDhcpServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HwIPPoolDhcpServerTimeout_Type.__name__ = "Integer32"
_HwIPPoolDhcpServerTimeout_Object = MibTableColumn
hwIPPoolDhcpServerTimeout = _HwIPPoolDhcpServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1, 9),
    _HwIPPoolDhcpServerTimeout_Type()
)
hwIPPoolDhcpServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolDhcpServerTimeout.setStatus("current")


class _HwIPPoolDhcpServerDeadTime_Type(Integer32):
    """Custom type hwIPPoolDhcpServerDeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIPPoolDhcpServerDeadTime_Type.__name__ = "Integer32"
_HwIPPoolDhcpServerDeadTime_Object = MibTableColumn
hwIPPoolDhcpServerDeadTime = _HwIPPoolDhcpServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 8, 1, 10),
    _HwIPPoolDhcpServerDeadTime_Type()
)
hwIPPoolDhcpServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolDhcpServerDeadTime.setStatus("current")
_HwIPPoolOptionTable_Object = MibTable
hwIPPoolOptionTable = _HwIPPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 9)
)
if mibBuilder.loadTexts:
    hwIPPoolOptionTable.setStatus("current")
_HwIPPoolOptionEntry_Object = MibTableRow
hwIPPoolOptionEntry = _HwIPPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 9, 1)
)
hwIPPoolOptionEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionId"),
)
if mibBuilder.loadTexts:
    hwIPPoolOptionEntry.setStatus("current")


class _HwIPDhcpOptionId_Type(Integer32):
    """Custom type hwIPDhcpOptionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_HwIPDhcpOptionId_Type.__name__ = "Integer32"
_HwIPDhcpOptionId_Object = MibTableColumn
hwIPDhcpOptionId = _HwIPDhcpOptionId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 9, 1, 1),
    _HwIPDhcpOptionId_Type()
)
hwIPDhcpOptionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpOptionId.setStatus("current")


class _HwIPDhcpOption_Type(OctetString):
    """Custom type hwIPDhcpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwIPDhcpOption_Type.__name__ = "OctetString"
_HwIPDhcpOption_Object = MibTableColumn
hwIPDhcpOption = _HwIPDhcpOption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 9, 1, 2),
    _HwIPDhcpOption_Type()
)
hwIPDhcpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPDhcpOption.setStatus("current")
_HwIPDhcpOptionRowStatus_Type = RowStatus
_HwIPDhcpOptionRowStatus_Object = MibTableColumn
hwIPDhcpOptionRowStatus = _HwIPDhcpOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 9, 1, 3),
    _HwIPDhcpOptionRowStatus_Type()
)
hwIPDhcpOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpOptionRowStatus.setStatus("current")
_HwIPPoolGroupTable_Object = MibTable
hwIPPoolGroupTable = _HwIPPoolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 10)
)
if mibBuilder.loadTexts:
    hwIPPoolGroupTable.setStatus("current")
_HwIPPoolGroupEntry_Object = MibTableRow
hwIPPoolGroupEntry = _HwIPPoolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 10, 1)
)
hwIPPoolGroupEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolGroupName"),
)
if mibBuilder.loadTexts:
    hwIPPoolGroupEntry.setStatus("current")


class _HwIPPoolGroupName_Type(OctetString):
    """Custom type hwIPPoolGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPPoolGroupName_Type.__name__ = "OctetString"
_HwIPPoolGroupName_Object = MibTableColumn
hwIPPoolGroupName = _HwIPPoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 10, 1, 1),
    _HwIPPoolGroupName_Type()
)
hwIPPoolGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupName.setStatus("current")


class _HwIPPoolGroupVPNInstance_Type(OctetString):
    """Custom type hwIPPoolGroupVPNInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwIPPoolGroupVPNInstance_Type.__name__ = "OctetString"
_HwIPPoolGroupVPNInstance_Object = MibTableColumn
hwIPPoolGroupVPNInstance = _HwIPPoolGroupVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 10, 1, 2),
    _HwIPPoolGroupVPNInstance_Type()
)
hwIPPoolGroupVPNInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolGroupVPNInstance.setStatus("current")
_HwIPPoolGroupIncludeUndo_Type = TruthValue
_HwIPPoolGroupIncludeUndo_Object = MibTableColumn
hwIPPoolGroupIncludeUndo = _HwIPPoolGroupIncludeUndo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 10, 1, 3),
    _HwIPPoolGroupIncludeUndo_Type()
)
hwIPPoolGroupIncludeUndo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolGroupIncludeUndo.setStatus("current")
_HwIPPoolGroupRowStatus_Type = RowStatus
_HwIPPoolGroupRowStatus_Object = MibTableColumn
hwIPPoolGroupRowStatus = _HwIPPoolGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 10, 1, 4),
    _HwIPPoolGroupRowStatus_Type()
)
hwIPPoolGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolGroupRowStatus.setStatus("current")
_HwIPPoolGroupExtTable_Object = MibTable
hwIPPoolGroupExtTable = _HwIPPoolGroupExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 11)
)
if mibBuilder.loadTexts:
    hwIPPoolGroupExtTable.setStatus("current")
_HwIPPoolGroupExtEntry_Object = MibTableRow
hwIPPoolGroupExtEntry = _HwIPPoolGroupExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 11, 1)
)
hwIPPoolGroupExtEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolGroupName"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolGroupExtIncludePoolName"),
)
if mibBuilder.loadTexts:
    hwIPPoolGroupExtEntry.setStatus("current")


class _HwIPPoolGroupExtIncludePoolName_Type(OctetString):
    """Custom type hwIPPoolGroupExtIncludePoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPPoolGroupExtIncludePoolName_Type.__name__ = "OctetString"
_HwIPPoolGroupExtIncludePoolName_Object = MibTableColumn
hwIPPoolGroupExtIncludePoolName = _HwIPPoolGroupExtIncludePoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 11, 1, 1),
    _HwIPPoolGroupExtIncludePoolName_Type()
)
hwIPPoolGroupExtIncludePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupExtIncludePoolName.setStatus("current")


class _HwIPPoolGroupExtIncludePoolMoveOrder_Type(Integer32):
    """Custom type hwIPPoolGroupExtIncludePoolMoveOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwIPPoolGroupExtIncludePoolMoveOrder_Type.__name__ = "Integer32"
_HwIPPoolGroupExtIncludePoolMoveOrder_Object = MibTableColumn
hwIPPoolGroupExtIncludePoolMoveOrder = _HwIPPoolGroupExtIncludePoolMoveOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 11, 1, 2),
    _HwIPPoolGroupExtIncludePoolMoveOrder_Type()
)
hwIPPoolGroupExtIncludePoolMoveOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolGroupExtIncludePoolMoveOrder.setStatus("current")
_HwIPPoolGroupExtRowStatus_Type = RowStatus
_HwIPPoolGroupExtRowStatus_Object = MibTableColumn
hwIPPoolGroupExtRowStatus = _HwIPPoolGroupExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 11, 1, 3),
    _HwIPPoolGroupExtRowStatus_Type()
)
hwIPPoolGroupExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolGroupExtRowStatus.setStatus("current")
_HwIPPoolGroupDisplayTable_Object = MibTable
hwIPPoolGroupDisplayTable = _HwIPPoolGroupDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12)
)
if mibBuilder.loadTexts:
    hwIPPoolGroupDisplayTable.setStatus("current")
_HwIPPoolGroupDisplayEntry_Object = MibTableRow
hwIPPoolGroupDisplayEntry = _HwIPPoolGroupDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12, 1)
)
hwIPPoolGroupDisplayEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolGroupName"),
)
if mibBuilder.loadTexts:
    hwIPPoolGroupDisplayEntry.setStatus("current")


class _HwIPPoolGroupIncludePoolNum_Type(Integer32):
    """Custom type hwIPPoolGroupIncludePoolNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HwIPPoolGroupIncludePoolNum_Type.__name__ = "Integer32"
_HwIPPoolGroupIncludePoolNum_Object = MibTableColumn
hwIPPoolGroupIncludePoolNum = _HwIPPoolGroupIncludePoolNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12, 1, 1),
    _HwIPPoolGroupIncludePoolNum_Type()
)
hwIPPoolGroupIncludePoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupIncludePoolNum.setStatus("current")


class _HwIPPoolGroupBoundByDomainNum_Type(Integer32):
    """Custom type hwIPPoolGroupBoundByDomainNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HwIPPoolGroupBoundByDomainNum_Type.__name__ = "Integer32"
_HwIPPoolGroupBoundByDomainNum_Object = MibTableColumn
hwIPPoolGroupBoundByDomainNum = _HwIPPoolGroupBoundByDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12, 1, 2),
    _HwIPPoolGroupBoundByDomainNum_Type()
)
hwIPPoolGroupBoundByDomainNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupBoundByDomainNum.setStatus("current")
_HwIPPoolGroupIPTotalNum_Type = Integer32
_HwIPPoolGroupIPTotalNum_Object = MibTableColumn
hwIPPoolGroupIPTotalNum = _HwIPPoolGroupIPTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12, 1, 3),
    _HwIPPoolGroupIPTotalNum_Type()
)
hwIPPoolGroupIPTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupIPTotalNum.setStatus("current")
_HwIPPoolGroupIPUsedNum_Type = Integer32
_HwIPPoolGroupIPUsedNum_Object = MibTableColumn
hwIPPoolGroupIPUsedNum = _HwIPPoolGroupIPUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12, 1, 4),
    _HwIPPoolGroupIPUsedNum_Type()
)
hwIPPoolGroupIPUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupIPUsedNum.setStatus("current")
_HwIPPoolGroupIPConflictedNum_Type = Integer32
_HwIPPoolGroupIPConflictedNum_Object = MibTableColumn
hwIPPoolGroupIPConflictedNum = _HwIPPoolGroupIPConflictedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12, 1, 5),
    _HwIPPoolGroupIPConflictedNum_Type()
)
hwIPPoolGroupIPConflictedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupIPConflictedNum.setStatus("current")
_HwIPPoolGroupIPDisableNum_Type = Integer32
_HwIPPoolGroupIPDisableNum_Object = MibTableColumn
hwIPPoolGroupIPDisableNum = _HwIPPoolGroupIPDisableNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12, 1, 6),
    _HwIPPoolGroupIPDisableNum_Type()
)
hwIPPoolGroupIPDisableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupIPDisableNum.setStatus("current")
_HwIPPoolGroupIPDesignatedNum_Type = Integer32
_HwIPPoolGroupIPDesignatedNum_Object = MibTableColumn
hwIPPoolGroupIPDesignatedNum = _HwIPPoolGroupIPDesignatedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12, 1, 7),
    _HwIPPoolGroupIPDesignatedNum_Type()
)
hwIPPoolGroupIPDesignatedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupIPDesignatedNum.setStatus("current")
_HwIPPoolGroupIPFreeNum_Type = Integer32
_HwIPPoolGroupIPFreeNum_Object = MibTableColumn
hwIPPoolGroupIPFreeNum = _HwIPPoolGroupIPFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12, 1, 8),
    _HwIPPoolGroupIPFreeNum_Type()
)
hwIPPoolGroupIPFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupIPFreeNum.setStatus("current")


class _HwIPPoolGroupIPUsedPercent_Type(Integer32):
    """Custom type hwIPPoolGroupIPUsedPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HwIPPoolGroupIPUsedPercent_Type.__name__ = "Integer32"
_HwIPPoolGroupIPUsedPercent_Object = MibTableColumn
hwIPPoolGroupIPUsedPercent = _HwIPPoolGroupIPUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 12, 1, 9),
    _HwIPPoolGroupIPUsedPercent_Type()
)
hwIPPoolGroupIPUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolGroupIPUsedPercent.setStatus("current")
_HwIPPoolDomainSearchListTable_Object = MibTable
hwIPPoolDomainSearchListTable = _HwIPPoolDomainSearchListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 13)
)
if mibBuilder.loadTexts:
    hwIPPoolDomainSearchListTable.setStatus("current")
_HwIPPoolDomainSearchListEntry_Object = MibTableRow
hwIPPoolDomainSearchListEntry = _HwIPPoolDomainSearchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 13, 1)
)
hwIPPoolDomainSearchListEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolDomainSearchList"),
)
if mibBuilder.loadTexts:
    hwIPPoolDomainSearchListEntry.setStatus("current")


class _HwIPPoolDomainSearchList_Type(OctetString):
    """Custom type hwIPPoolDomainSearchList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPPoolDomainSearchList_Type.__name__ = "OctetString"
_HwIPPoolDomainSearchList_Object = MibTableColumn
hwIPPoolDomainSearchList = _HwIPPoolDomainSearchList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 13, 1, 1),
    _HwIPPoolDomainSearchList_Type()
)
hwIPPoolDomainSearchList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPPoolDomainSearchList.setStatus("current")
_HwIPPoolDomainSearchListRowStatus_Type = RowStatus
_HwIPPoolDomainSearchListRowStatus_Object = MibTableColumn
hwIPPoolDomainSearchListRowStatus = _HwIPPoolDomainSearchListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 13, 1, 2),
    _HwIPPoolDomainSearchListRowStatus_Type()
)
hwIPPoolDomainSearchListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPPoolDomainSearchListRowStatus.setStatus("current")
_HwIPPoolOptionExtTable_Object = MibTable
hwIPPoolOptionExtTable = _HwIPPoolOptionExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 14)
)
if mibBuilder.loadTexts:
    hwIPPoolOptionExtTable.setStatus("current")
_HwIPPoolOptionExtEntry_Object = MibTableRow
hwIPPoolOptionExtEntry = _HwIPPoolOptionExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 14, 1)
)
hwIPPoolOptionExtEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionId"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionSubId"),
)
if mibBuilder.loadTexts:
    hwIPPoolOptionExtEntry.setStatus("current")


class _HwIPDhcpOptionSubId_Type(Integer32):
    """Custom type hwIPDhcpOptionSubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwIPDhcpOptionSubId_Type.__name__ = "Integer32"
_HwIPDhcpOptionSubId_Object = MibTableColumn
hwIPDhcpOptionSubId = _HwIPDhcpOptionSubId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 14, 1, 1),
    _HwIPDhcpOptionSubId_Type()
)
hwIPDhcpOptionSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpOptionSubId.setStatus("current")


class _HwIPDhcpOptionSubType_Type(Integer32):
    """Custom type hwIPDhcpOptionSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("string", 2))
    )


_HwIPDhcpOptionSubType_Type.__name__ = "Integer32"
_HwIPDhcpOptionSubType_Object = MibTableColumn
hwIPDhcpOptionSubType = _HwIPDhcpOptionSubType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 14, 1, 2),
    _HwIPDhcpOptionSubType_Type()
)
hwIPDhcpOptionSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpOptionSubType.setStatus("current")


class _HwIPDhcpOptionSubValue_Type(OctetString):
    """Custom type hwIPDhcpOptionSubValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIPDhcpOptionSubValue_Type.__name__ = "OctetString"
_HwIPDhcpOptionSubValue_Object = MibTableColumn
hwIPDhcpOptionSubValue = _HwIPDhcpOptionSubValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 14, 1, 3),
    _HwIPDhcpOptionSubValue_Type()
)
hwIPDhcpOptionSubValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpOptionSubValue.setStatus("current")
_HwIPDhcpOptionSubRowStatus_Type = RowStatus
_HwIPDhcpOptionSubRowStatus_Object = MibTableColumn
hwIPDhcpOptionSubRowStatus = _HwIPDhcpOptionSubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 14, 1, 50),
    _HwIPDhcpOptionSubRowStatus_Type()
)
hwIPDhcpOptionSubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpOptionSubRowStatus.setStatus("current")
_HwIPPoolReplyOptionTable_Object = MibTable
hwIPPoolReplyOptionTable = _HwIPPoolReplyOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 15)
)
if mibBuilder.loadTexts:
    hwIPPoolReplyOptionTable.setStatus("current")
_HwIPPoolReplyOptionEntry_Object = MibTableRow
hwIPPoolReplyOptionEntry = _HwIPPoolReplyOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 15, 1)
)
hwIPPoolReplyOptionEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPDhcpSpecOptionId"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPDhcpSpecOption"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPDhcpReplyOptionId"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPDhcpReplyOptionSubId"),
)
if mibBuilder.loadTexts:
    hwIPPoolReplyOptionEntry.setStatus("current")


class _HwIPDhcpSpecOptionId_Type(Integer32):
    """Custom type hwIPDhcpSpecOptionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 60),
    )


_HwIPDhcpSpecOptionId_Type.__name__ = "Integer32"
_HwIPDhcpSpecOptionId_Object = MibTableColumn
hwIPDhcpSpecOptionId = _HwIPDhcpSpecOptionId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 15, 1, 1),
    _HwIPDhcpSpecOptionId_Type()
)
hwIPDhcpSpecOptionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpSpecOptionId.setStatus("current")


class _HwIPDhcpSpecOption_Type(OctetString):
    """Custom type hwIPDhcpSpecOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIPDhcpSpecOption_Type.__name__ = "OctetString"
_HwIPDhcpSpecOption_Object = MibTableColumn
hwIPDhcpSpecOption = _HwIPDhcpSpecOption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 15, 1, 2),
    _HwIPDhcpSpecOption_Type()
)
hwIPDhcpSpecOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpSpecOption.setStatus("current")


class _HwIPDhcpReplyOptionId_Type(Integer32):
    """Custom type hwIPDhcpReplyOptionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_HwIPDhcpReplyOptionId_Type.__name__ = "Integer32"
_HwIPDhcpReplyOptionId_Object = MibTableColumn
hwIPDhcpReplyOptionId = _HwIPDhcpReplyOptionId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 15, 1, 3),
    _HwIPDhcpReplyOptionId_Type()
)
hwIPDhcpReplyOptionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpReplyOptionId.setStatus("current")


class _HwIPDhcpReplyOptionSubId_Type(Integer32):
    """Custom type hwIPDhcpReplyOptionSubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwIPDhcpReplyOptionSubId_Type.__name__ = "Integer32"
_HwIPDhcpReplyOptionSubId_Object = MibTableColumn
hwIPDhcpReplyOptionSubId = _HwIPDhcpReplyOptionSubId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 15, 1, 4),
    _HwIPDhcpReplyOptionSubId_Type()
)
hwIPDhcpReplyOptionSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpReplyOptionSubId.setStatus("current")


class _HwIPDhcpReplyOptionSubType_Type(Integer32):
    """Custom type hwIPDhcpReplyOptionSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hex", 3),
          ("ip", 1),
          ("string", 2))
    )


_HwIPDhcpReplyOptionSubType_Type.__name__ = "Integer32"
_HwIPDhcpReplyOptionSubType_Object = MibTableColumn
hwIPDhcpReplyOptionSubType = _HwIPDhcpReplyOptionSubType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 15, 1, 5),
    _HwIPDhcpReplyOptionSubType_Type()
)
hwIPDhcpReplyOptionSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpReplyOptionSubType.setStatus("current")


class _HwIPDhcpReplyOptionSub_Type(OctetString):
    """Custom type hwIPDhcpReplyOptionSub based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwIPDhcpReplyOptionSub_Type.__name__ = "OctetString"
_HwIPDhcpReplyOptionSub_Object = MibTableColumn
hwIPDhcpReplyOptionSub = _HwIPDhcpReplyOptionSub_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 15, 1, 6),
    _HwIPDhcpReplyOptionSub_Type()
)
hwIPDhcpReplyOptionSub.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpReplyOptionSub.setStatus("current")
_HwIPDhcpReplyOptionRowStatus_Type = RowStatus
_HwIPDhcpReplyOptionRowStatus_Object = MibTableColumn
hwIPDhcpReplyOptionRowStatus = _HwIPDhcpReplyOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 15, 1, 50),
    _HwIPDhcpReplyOptionRowStatus_Type()
)
hwIPDhcpReplyOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpReplyOptionRowStatus.setStatus("current")
_HwIPv6PrefixTable_Object = MibTable
hwIPv6PrefixTable = _HwIPv6PrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16)
)
if mibBuilder.loadTexts:
    hwIPv6PrefixTable.setStatus("current")
_HwIPv6PrefixEntry_Object = MibTableRow
hwIPv6PrefixEntry = _HwIPv6PrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1)
)
hwIPv6PrefixEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPv6PrefixIndex"),
)
if mibBuilder.loadTexts:
    hwIPv6PrefixEntry.setStatus("current")


class _HwIPv6PrefixIndex_Type(Integer32):
    """Custom type hwIPv6PrefixIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwIPv6PrefixIndex_Type.__name__ = "Integer32"
_HwIPv6PrefixIndex_Object = MibTableColumn
hwIPv6PrefixIndex = _HwIPv6PrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 1),
    _HwIPv6PrefixIndex_Type()
)
hwIPv6PrefixIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6PrefixIndex.setStatus("current")


class _HwIPv6PrefixName_Type(OctetString):
    """Custom type hwIPv6PrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPv6PrefixName_Type.__name__ = "OctetString"
_HwIPv6PrefixName_Object = MibTableColumn
hwIPv6PrefixName = _HwIPv6PrefixName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 2),
    _HwIPv6PrefixName_Type()
)
hwIPv6PrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PrefixName.setStatus("current")


class _HwIPv6PrefixType_Type(Integer32):
    """Custom type hwIPv6PrefixType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delegation", 2),
          ("local", 1),
          ("remote", 3))
    )


_HwIPv6PrefixType_Type.__name__ = "Integer32"
_HwIPv6PrefixType_Object = MibTableColumn
hwIPv6PrefixType = _HwIPv6PrefixType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 3),
    _HwIPv6PrefixType_Type()
)
hwIPv6PrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PrefixType.setStatus("current")
_HwIPv6Prefix_Type = Ipv6AddressPrefix
_HwIPv6Prefix_Object = MibTableColumn
hwIPv6Prefix = _HwIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 4),
    _HwIPv6Prefix_Type()
)
hwIPv6Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6Prefix.setStatus("current")


class _HwIPv6PrefixLen_Type(Integer32):
    """Custom type hwIPv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwIPv6PrefixLen_Type.__name__ = "Integer32"
_HwIPv6PrefixLen_Object = MibTableColumn
hwIPv6PrefixLen = _HwIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 5),
    _HwIPv6PrefixLen_Type()
)
hwIPv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PrefixLen.setStatus("current")


class _HwIPv6PrefixDelegatingLen_Type(Integer32):
    """Custom type hwIPv6PrefixDelegatingLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwIPv6PrefixDelegatingLen_Type.__name__ = "Integer32"
_HwIPv6PrefixDelegatingLen_Object = MibTableColumn
hwIPv6PrefixDelegatingLen = _HwIPv6PrefixDelegatingLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 6),
    _HwIPv6PrefixDelegatingLen_Type()
)
hwIPv6PrefixDelegatingLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PrefixDelegatingLen.setStatus("current")
_HwIPv6PrefixAdvPreferredLifetime_Type = Integer32
_HwIPv6PrefixAdvPreferredLifetime_Object = MibTableColumn
hwIPv6PrefixAdvPreferredLifetime = _HwIPv6PrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 7),
    _HwIPv6PrefixAdvPreferredLifetime_Type()
)
hwIPv6PrefixAdvPreferredLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PrefixAdvPreferredLifetime.setStatus("current")
_HwIPv6PrefixAdvValidLifetime_Type = Integer32
_HwIPv6PrefixAdvValidLifetime_Object = MibTableColumn
hwIPv6PrefixAdvValidLifetime = _HwIPv6PrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 8),
    _HwIPv6PrefixAdvValidLifetime_Type()
)
hwIPv6PrefixAdvValidLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PrefixAdvValidLifetime.setStatus("current")
_HwIPv6PrefixAvailableStatus_Type = TruthValue
_HwIPv6PrefixAvailableStatus_Object = MibTableColumn
hwIPv6PrefixAvailableStatus = _HwIPv6PrefixAvailableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 9),
    _HwIPv6PrefixAvailableStatus_Type()
)
hwIPv6PrefixAvailableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PrefixAvailableStatus.setStatus("current")


class _HwIPv6VPNInstance_Type(OctetString):
    """Custom type hwIPv6VPNInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwIPv6VPNInstance_Type.__name__ = "OctetString"
_HwIPv6VPNInstance_Object = MibTableColumn
hwIPv6VPNInstance = _HwIPv6VPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 10),
    _HwIPv6VPNInstance_Type()
)
hwIPv6VPNInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6VPNInstance.setStatus("current")


class _HwIPv6PrefixReservedFlag_Type(Integer32):
    """Custom type hwIPv6PrefixReservedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("duidPlusLeaseReserved", 4),
          ("duidReserved", 3),
          ("macPlusLeaseReserved", 2),
          ("macReserved", 1),
          ("noneReserved", 0))
    )


_HwIPv6PrefixReservedFlag_Type.__name__ = "Integer32"
_HwIPv6PrefixReservedFlag_Object = MibTableColumn
hwIPv6PrefixReservedFlag = _HwIPv6PrefixReservedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 11),
    _HwIPv6PrefixReservedFlag_Type()
)
hwIPv6PrefixReservedFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PrefixReservedFlag.setStatus("current")
_HwIPv6LinkAddress_Type = Ipv6Address
_HwIPv6LinkAddress_Object = MibTableColumn
hwIPv6LinkAddress = _HwIPv6LinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 12),
    _HwIPv6LinkAddress_Type()
)
hwIPv6LinkAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6LinkAddress.setStatus("current")
_HwIPv6SlaacUnsharedFlag_Type = TruthValue
_HwIPv6SlaacUnsharedFlag_Object = MibTableColumn
hwIPv6SlaacUnsharedFlag = _HwIPv6SlaacUnsharedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 13),
    _HwIPv6SlaacUnsharedFlag_Type()
)
hwIPv6SlaacUnsharedFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6SlaacUnsharedFlag.setStatus("current")
_HwIPv6PrefixRowStatus_Type = RowStatus
_HwIPv6PrefixRowStatus_Object = MibTableColumn
hwIPv6PrefixRowStatus = _HwIPv6PrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 14),
    _HwIPv6PrefixRowStatus_Type()
)
hwIPv6PrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PrefixRowStatus.setStatus("current")
_HwIPPoolPDUnshareOnly_Type = TruthValue
_HwIPPoolPDUnshareOnly_Object = MibTableColumn
hwIPPoolPDUnshareOnly = _HwIPPoolPDUnshareOnly_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 16, 1, 15),
    _HwIPPoolPDUnshareOnly_Type()
)
hwIPPoolPDUnshareOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolPDUnshareOnly.setStatus("current")
_HwIPv6PoolTable_Object = MibTable
hwIPv6PoolTable = _HwIPv6PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17)
)
if mibBuilder.loadTexts:
    hwIPv6PoolTable.setStatus("current")
_HwIPv6PoolEntry_Object = MibTableRow
hwIPv6PoolEntry = _HwIPv6PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1)
)
hwIPv6PoolEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPv6PoolIndex"),
)
if mibBuilder.loadTexts:
    hwIPv6PoolEntry.setStatus("current")


class _HwIPv6PoolIndex_Type(Integer32):
    """Custom type hwIPv6PoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwIPv6PoolIndex_Type.__name__ = "Integer32"
_HwIPv6PoolIndex_Object = MibTableColumn
hwIPv6PoolIndex = _HwIPv6PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 1),
    _HwIPv6PoolIndex_Type()
)
hwIPv6PoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6PoolIndex.setStatus("current")


class _HwIPv6PoolName_Type(OctetString):
    """Custom type hwIPv6PoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPv6PoolName_Type.__name__ = "OctetString"
_HwIPv6PoolName_Object = MibTableColumn
hwIPv6PoolName = _HwIPv6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 2),
    _HwIPv6PoolName_Type()
)
hwIPv6PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolName.setStatus("current")


class _HwIPv6PoolType_Type(Integer32):
    """Custom type hwIPv6PoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delegation", 2),
          ("local", 1),
          ("relay", 3))
    )


_HwIPv6PoolType_Type.__name__ = "Integer32"
_HwIPv6PoolType_Object = MibTableColumn
hwIPv6PoolType = _HwIPv6PoolType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 3),
    _HwIPv6PoolType_Type()
)
hwIPv6PoolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolType.setStatus("current")


class _HwIPv6PoolPrefixName_Type(OctetString):
    """Custom type hwIPv6PoolPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPv6PoolPrefixName_Type.__name__ = "OctetString"
_HwIPv6PoolPrefixName_Object = MibTableColumn
hwIPv6PoolPrefixName = _HwIPv6PoolPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 4),
    _HwIPv6PoolPrefixName_Type()
)
hwIPv6PoolPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolPrefixName.setStatus("current")


class _HwIPv6PoolDnsIPAddr_Type(OctetString):
    """Custom type hwIPv6PoolDnsIPAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 81),
    )


_HwIPv6PoolDnsIPAddr_Type.__name__ = "OctetString"
_HwIPv6PoolDnsIPAddr_Object = MibTableColumn
hwIPv6PoolDnsIPAddr = _HwIPv6PoolDnsIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 5),
    _HwIPv6PoolDnsIPAddr_Type()
)
hwIPv6PoolDnsIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolDnsIPAddr.setStatus("current")


class _HwIPv6PoolDnsSearchList_Type(OctetString):
    """Custom type hwIPv6PoolDnsSearchList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPv6PoolDnsSearchList_Type.__name__ = "OctetString"
_HwIPv6PoolDnsSearchList_Object = MibTableColumn
hwIPv6PoolDnsSearchList = _HwIPv6PoolDnsSearchList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 6),
    _HwIPv6PoolDnsSearchList_Type()
)
hwIPv6PoolDnsSearchList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolDnsSearchList.setStatus("current")


class _HwIPv6PoolPreference_Type(Integer32):
    """Custom type hwIPv6PoolPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIPv6PoolPreference_Type.__name__ = "Integer32"
_HwIPv6PoolPreference_Object = MibTableColumn
hwIPv6PoolPreference = _HwIPv6PoolPreference_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 7),
    _HwIPv6PoolPreference_Type()
)
hwIPv6PoolPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolPreference.setStatus("current")
_HwIPv6PoolAvailableStatus_Type = TruthValue
_HwIPv6PoolAvailableStatus_Object = MibTableColumn
hwIPv6PoolAvailableStatus = _HwIPv6PoolAvailableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 8),
    _HwIPv6PoolAvailableStatus_Type()
)
hwIPv6PoolAvailableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolAvailableStatus.setStatus("current")


class _HwIPv6PoolRenewPercent_Type(Integer32):
    """Custom type hwIPv6PoolRenewPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 99),
    )


_HwIPv6PoolRenewPercent_Type.__name__ = "Integer32"
_HwIPv6PoolRenewPercent_Object = MibTableColumn
hwIPv6PoolRenewPercent = _HwIPv6PoolRenewPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 9),
    _HwIPv6PoolRenewPercent_Type()
)
hwIPv6PoolRenewPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolRenewPercent.setStatus("current")


class _HwIPv6PoolRebindingPercent_Type(Integer32):
    """Custom type hwIPv6PoolRebindingPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 99),
    )


_HwIPv6PoolRebindingPercent_Type.__name__ = "Integer32"
_HwIPv6PoolRebindingPercent_Object = MibTableColumn
hwIPv6PoolRebindingPercent = _HwIPv6PoolRebindingPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 10),
    _HwIPv6PoolRebindingPercent_Type()
)
hwIPv6PoolRebindingPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolRebindingPercent.setStatus("current")
_HwIPv6PoolRapidCommitFlag_Type = TruthValue
_HwIPv6PoolRapidCommitFlag_Object = MibTableColumn
hwIPv6PoolRapidCommitFlag = _HwIPv6PoolRapidCommitFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 11),
    _HwIPv6PoolRapidCommitFlag_Type()
)
hwIPv6PoolRapidCommitFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolRapidCommitFlag.setStatus("current")
_HwIPv6PoolUnicastOption_Type = TruthValue
_HwIPv6PoolUnicastOption_Object = MibTableColumn
hwIPv6PoolUnicastOption = _HwIPv6PoolUnicastOption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 12),
    _HwIPv6PoolUnicastOption_Type()
)
hwIPv6PoolUnicastOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolUnicastOption.setStatus("current")


class _HwIPv6PoolAFTRName_Type(OctetString):
    """Custom type hwIPv6PoolAFTRName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwIPv6PoolAFTRName_Type.__name__ = "OctetString"
_HwIPv6PoolAFTRName_Object = MibTableColumn
hwIPv6PoolAFTRName = _HwIPv6PoolAFTRName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 13),
    _HwIPv6PoolAFTRName_Type()
)
hwIPv6PoolAFTRName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolAFTRName.setStatus("current")
_HwIPv6PoolRowStatus_Type = RowStatus
_HwIPv6PoolRowStatus_Object = MibTableColumn
hwIPv6PoolRowStatus = _HwIPv6PoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 17, 1, 14),
    _HwIPv6PoolRowStatus_Type()
)
hwIPv6PoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6PoolRowStatus.setStatus("current")
_HwIPv6PoolStatusTable_Object = MibTable
hwIPv6PoolStatusTable = _HwIPv6PoolStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18)
)
if mibBuilder.loadTexts:
    hwIPv6PoolStatusTable.setStatus("current")
_HwIPv6PoolStatusEntry_Object = MibTableRow
hwIPv6PoolStatusEntry = _HwIPv6PoolStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1)
)
hwIPv6PoolStatusEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPv6PoolIndex"),
)
if mibBuilder.loadTexts:
    hwIPv6PoolStatusEntry.setStatus("current")
_HwIPv6FreeAddressNum_Type = Integer32
_HwIPv6FreeAddressNum_Object = MibTableColumn
hwIPv6FreeAddressNum = _HwIPv6FreeAddressNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 1),
    _HwIPv6FreeAddressNum_Type()
)
hwIPv6FreeAddressNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6FreeAddressNum.setStatus("current")
_HwIPv6UsedAddressNum_Type = Integer32
_HwIPv6UsedAddressNum_Object = MibTableColumn
hwIPv6UsedAddressNum = _HwIPv6UsedAddressNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 2),
    _HwIPv6UsedAddressNum_Type()
)
hwIPv6UsedAddressNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6UsedAddressNum.setStatus("current")
_HwIPv6FreePrefixNum_Type = Integer32
_HwIPv6FreePrefixNum_Object = MibTableColumn
hwIPv6FreePrefixNum = _HwIPv6FreePrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 3),
    _HwIPv6FreePrefixNum_Type()
)
hwIPv6FreePrefixNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6FreePrefixNum.setStatus("current")
_HwIPv6UsedPrefixNum_Type = Integer32
_HwIPv6UsedPrefixNum_Object = MibTableColumn
hwIPv6UsedPrefixNum = _HwIPv6UsedPrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 4),
    _HwIPv6UsedPrefixNum_Type()
)
hwIPv6UsedPrefixNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6UsedPrefixNum.setStatus("current")
_HwIPv6AddressTotalNum_Type = Integer32
_HwIPv6AddressTotalNum_Object = MibTableColumn
hwIPv6AddressTotalNum = _HwIPv6AddressTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 5),
    _HwIPv6AddressTotalNum_Type()
)
hwIPv6AddressTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6AddressTotalNum.setStatus("current")
_HwIPv6AddressUsedNum_Type = Integer32
_HwIPv6AddressUsedNum_Object = MibTableColumn
hwIPv6AddressUsedNum = _HwIPv6AddressUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 6),
    _HwIPv6AddressUsedNum_Type()
)
hwIPv6AddressUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6AddressUsedNum.setStatus("current")
_HwIPv6AddressFreeNum_Type = Integer32
_HwIPv6AddressFreeNum_Object = MibTableColumn
hwIPv6AddressFreeNum = _HwIPv6AddressFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 7),
    _HwIPv6AddressFreeNum_Type()
)
hwIPv6AddressFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6AddressFreeNum.setStatus("current")
_HwIPv6AddressConflictNum_Type = Integer32
_HwIPv6AddressConflictNum_Object = MibTableColumn
hwIPv6AddressConflictNum = _HwIPv6AddressConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 8),
    _HwIPv6AddressConflictNum_Type()
)
hwIPv6AddressConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6AddressConflictNum.setStatus("current")
_HwIPv6AddressExcludeNum_Type = Integer32
_HwIPv6AddressExcludeNum_Object = MibTableColumn
hwIPv6AddressExcludeNum = _HwIPv6AddressExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 9),
    _HwIPv6AddressExcludeNum_Type()
)
hwIPv6AddressExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6AddressExcludeNum.setStatus("current")
_HwIPv6AddressUsedPercent_Type = Integer32
_HwIPv6AddressUsedPercent_Object = MibTableColumn
hwIPv6AddressUsedPercent = _HwIPv6AddressUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 10),
    _HwIPv6AddressUsedPercent_Type()
)
hwIPv6AddressUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6AddressUsedPercent.setStatus("current")
_HwIPv6NDRAPrefixTotalNum_Type = Integer32
_HwIPv6NDRAPrefixTotalNum_Object = MibTableColumn
hwIPv6NDRAPrefixTotalNum = _HwIPv6NDRAPrefixTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 11),
    _HwIPv6NDRAPrefixTotalNum_Type()
)
hwIPv6NDRAPrefixTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6NDRAPrefixTotalNum.setStatus("current")
_HwIPv6NDRAPrefixUsedNum_Type = Integer32
_HwIPv6NDRAPrefixUsedNum_Object = MibTableColumn
hwIPv6NDRAPrefixUsedNum = _HwIPv6NDRAPrefixUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 12),
    _HwIPv6NDRAPrefixUsedNum_Type()
)
hwIPv6NDRAPrefixUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6NDRAPrefixUsedNum.setStatus("current")
_HwIPv6NDRAPrefixFreeNum_Type = Integer32
_HwIPv6NDRAPrefixFreeNum_Object = MibTableColumn
hwIPv6NDRAPrefixFreeNum = _HwIPv6NDRAPrefixFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 13),
    _HwIPv6NDRAPrefixFreeNum_Type()
)
hwIPv6NDRAPrefixFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6NDRAPrefixFreeNum.setStatus("current")
_HwIPv6NDRAPrefixConflictNum_Type = Integer32
_HwIPv6NDRAPrefixConflictNum_Object = MibTableColumn
hwIPv6NDRAPrefixConflictNum = _HwIPv6NDRAPrefixConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 14),
    _HwIPv6NDRAPrefixConflictNum_Type()
)
hwIPv6NDRAPrefixConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6NDRAPrefixConflictNum.setStatus("current")
_HwIPv6NDRAPrefixExcludeNum_Type = Integer32
_HwIPv6NDRAPrefixExcludeNum_Object = MibTableColumn
hwIPv6NDRAPrefixExcludeNum = _HwIPv6NDRAPrefixExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 15),
    _HwIPv6NDRAPrefixExcludeNum_Type()
)
hwIPv6NDRAPrefixExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6NDRAPrefixExcludeNum.setStatus("current")
_HwIPv6NDRAPrefixUsedPercent_Type = Integer32
_HwIPv6NDRAPrefixUsedPercent_Object = MibTableColumn
hwIPv6NDRAPrefixUsedPercent = _HwIPv6NDRAPrefixUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 16),
    _HwIPv6NDRAPrefixUsedPercent_Type()
)
hwIPv6NDRAPrefixUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6NDRAPrefixUsedPercent.setStatus("current")
_HwIPv6PDPrefixTotalNum_Type = Integer32
_HwIPv6PDPrefixTotalNum_Object = MibTableColumn
hwIPv6PDPrefixTotalNum = _HwIPv6PDPrefixTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 17),
    _HwIPv6PDPrefixTotalNum_Type()
)
hwIPv6PDPrefixTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6PDPrefixTotalNum.setStatus("current")
_HwIPv6PDPrefixUsedNum_Type = Integer32
_HwIPv6PDPrefixUsedNum_Object = MibTableColumn
hwIPv6PDPrefixUsedNum = _HwIPv6PDPrefixUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 18),
    _HwIPv6PDPrefixUsedNum_Type()
)
hwIPv6PDPrefixUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6PDPrefixUsedNum.setStatus("current")
_HwIPv6PDPrefixFreeNum_Type = Integer32
_HwIPv6PDPrefixFreeNum_Object = MibTableColumn
hwIPv6PDPrefixFreeNum = _HwIPv6PDPrefixFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 19),
    _HwIPv6PDPrefixFreeNum_Type()
)
hwIPv6PDPrefixFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6PDPrefixFreeNum.setStatus("current")
_HwIPv6PDPrefixConflictNum_Type = Integer32
_HwIPv6PDPrefixConflictNum_Object = MibTableColumn
hwIPv6PDPrefixConflictNum = _HwIPv6PDPrefixConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 20),
    _HwIPv6PDPrefixConflictNum_Type()
)
hwIPv6PDPrefixConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6PDPrefixConflictNum.setStatus("current")
_HwIPv6PDPrefixExcludeNum_Type = Integer32
_HwIPv6PDPrefixExcludeNum_Object = MibTableColumn
hwIPv6PDPrefixExcludeNum = _HwIPv6PDPrefixExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 21),
    _HwIPv6PDPrefixExcludeNum_Type()
)
hwIPv6PDPrefixExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6PDPrefixExcludeNum.setStatus("current")
_HwIPv6PDPrefixUsedPercent_Type = Integer32
_HwIPv6PDPrefixUsedPercent_Object = MibTableColumn
hwIPv6PDPrefixUsedPercent = _HwIPv6PDPrefixUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 18, 1, 22),
    _HwIPv6PDPrefixUsedPercent_Type()
)
hwIPv6PDPrefixUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6PDPrefixUsedPercent.setStatus("current")
_HwIPv6DuidBindPrefixTable_Object = MibTable
hwIPv6DuidBindPrefixTable = _HwIPv6DuidBindPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 19)
)
if mibBuilder.loadTexts:
    hwIPv6DuidBindPrefixTable.setStatus("current")
_HwIPv6DuidBindPrefixEntry_Object = MibTableRow
hwIPv6DuidBindPrefixEntry = _HwIPv6DuidBindPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 19, 1)
)
hwIPv6DuidBindPrefixEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPv6PrefixIndex"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPv6ClientDuid"),
)
if mibBuilder.loadTexts:
    hwIPv6DuidBindPrefixEntry.setStatus("current")


class _HwIPv6ClientDuid_Type(OctetString):
    """Custom type hwIPv6ClientDuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 28),
    )


_HwIPv6ClientDuid_Type.__name__ = "OctetString"
_HwIPv6ClientDuid_Object = MibTableColumn
hwIPv6ClientDuid = _HwIPv6ClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 19, 1, 1),
    _HwIPv6ClientDuid_Type()
)
hwIPv6ClientDuid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6ClientDuid.setStatus("current")
_HwIPv6BindPrefix_Type = Ipv6AddressPrefix
_HwIPv6BindPrefix_Object = MibTableColumn
hwIPv6BindPrefix = _HwIPv6BindPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 19, 1, 2),
    _HwIPv6BindPrefix_Type()
)
hwIPv6BindPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6BindPrefix.setStatus("current")
_HwIPv6DuidBindPrefixRowStatus_Type = RowStatus
_HwIPv6DuidBindPrefixRowStatus_Object = MibTableColumn
hwIPv6DuidBindPrefixRowStatus = _HwIPv6DuidBindPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 19, 1, 3),
    _HwIPv6DuidBindPrefixRowStatus_Type()
)
hwIPv6DuidBindPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6DuidBindPrefixRowStatus.setStatus("current")
_HwDhcpv6SvrGroupTable_Object = MibTable
hwDhcpv6SvrGroupTable = _HwDhcpv6SvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20)
)
if mibBuilder.loadTexts:
    hwDhcpv6SvrGroupTable.setStatus("current")
_HwDhcpv6SvrGroupEntry_Object = MibTableRow
hwDhcpv6SvrGroupEntry = _HwDhcpv6SvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1)
)
hwDhcpv6SvrGroupEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrGroupIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpv6SvrGroupEntry.setStatus("current")


class _HwDhcpv6SvrGroupIndex_Type(Integer32):
    """Custom type hwDhcpv6SvrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwDhcpv6SvrGroupIndex_Type.__name__ = "Integer32"
_HwDhcpv6SvrGroupIndex_Object = MibTableColumn
hwDhcpv6SvrGroupIndex = _HwDhcpv6SvrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 1),
    _HwDhcpv6SvrGroupIndex_Type()
)
hwDhcpv6SvrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpv6SvrGroupIndex.setStatus("current")


class _HwDhcpv6SvrGroupName_Type(OctetString):
    """Custom type hwDhcpv6SvrGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDhcpv6SvrGroupName_Type.__name__ = "OctetString"
_HwDhcpv6SvrGroupName_Object = MibTableColumn
hwDhcpv6SvrGroupName = _HwDhcpv6SvrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 2),
    _HwDhcpv6SvrGroupName_Type()
)
hwDhcpv6SvrGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpv6SvrGroupName.setStatus("current")
_HwIPDhcpv6SvrAddr1_Type = Ipv6Address
_HwIPDhcpv6SvrAddr1_Object = MibTableColumn
hwIPDhcpv6SvrAddr1 = _HwIPDhcpv6SvrAddr1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 3),
    _HwIPDhcpv6SvrAddr1_Type()
)
hwIPDhcpv6SvrAddr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpv6SvrAddr1.setStatus("current")
_HwIPDhcpv6SvrAddr2_Type = Ipv6Address
_HwIPDhcpv6SvrAddr2_Object = MibTableColumn
hwIPDhcpv6SvrAddr2 = _HwIPDhcpv6SvrAddr2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 4),
    _HwIPDhcpv6SvrAddr2_Type()
)
hwIPDhcpv6SvrAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpv6SvrAddr2.setStatus("current")


class _HwIPDhcpv6PriSvrState_Type(Integer32):
    """Custom type hwIPDhcpv6PriSvrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HwIPDhcpv6PriSvrState_Type.__name__ = "Integer32"
_HwIPDhcpv6PriSvrState_Object = MibTableColumn
hwIPDhcpv6PriSvrState = _HwIPDhcpv6PriSvrState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 5),
    _HwIPDhcpv6PriSvrState_Type()
)
hwIPDhcpv6PriSvrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpv6PriSvrState.setStatus("current")


class _HwIPDhcpv6ScdSvrState_Type(Integer32):
    """Custom type hwIPDhcpv6ScdSvrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HwIPDhcpv6ScdSvrState_Type.__name__ = "Integer32"
_HwIPDhcpv6ScdSvrState_Object = MibTableColumn
hwIPDhcpv6ScdSvrState = _HwIPDhcpv6ScdSvrState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 6),
    _HwIPDhcpv6ScdSvrState_Type()
)
hwIPDhcpv6ScdSvrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpv6ScdSvrState.setStatus("current")
_HwIPDhcpv6SvrAutoRelease_Type = TruthValue
_HwIPDhcpv6SvrAutoRelease_Object = MibTableColumn
hwIPDhcpv6SvrAutoRelease = _HwIPDhcpv6SvrAutoRelease_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 7),
    _HwIPDhcpv6SvrAutoRelease_Type()
)
hwIPDhcpv6SvrAutoRelease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpv6SvrAutoRelease.setStatus("current")


class _HwIPDhcpv6SvrGroupRefCount_Type(Integer32):
    """Custom type hwIPDhcpv6SvrGroupRefCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwIPDhcpv6SvrGroupRefCount_Type.__name__ = "Integer32"
_HwIPDhcpv6SvrGroupRefCount_Object = MibTableColumn
hwIPDhcpv6SvrGroupRefCount = _HwIPDhcpv6SvrGroupRefCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 8),
    _HwIPDhcpv6SvrGroupRefCount_Type()
)
hwIPDhcpv6SvrGroupRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPDhcpv6SvrGroupRefCount.setStatus("current")
_HwDhcpv6SvrInterface1_Type = DisplayString
_HwDhcpv6SvrInterface1_Object = MibTableColumn
hwDhcpv6SvrInterface1 = _HwDhcpv6SvrInterface1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 9),
    _HwDhcpv6SvrInterface1_Type()
)
hwDhcpv6SvrInterface1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpv6SvrInterface1.setStatus("current")
_HwDhcpv6SvrInterface2_Type = DisplayString
_HwDhcpv6SvrInterface2_Object = MibTableColumn
hwDhcpv6SvrInterface2 = _HwDhcpv6SvrInterface2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 10),
    _HwDhcpv6SvrInterface2_Type()
)
hwDhcpv6SvrInterface2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpv6SvrInterface2.setStatus("current")


class _HwDhcpv6SvrAlgorithm_Type(Integer32):
    """Custom type hwDhcpv6SvrAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loadingshare", 2),
          ("masterbackup", 1),
          ("polling", 3))
    )


_HwDhcpv6SvrAlgorithm_Type.__name__ = "Integer32"
_HwDhcpv6SvrAlgorithm_Object = MibTableColumn
hwDhcpv6SvrAlgorithm = _HwDhcpv6SvrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 11),
    _HwDhcpv6SvrAlgorithm_Type()
)
hwDhcpv6SvrAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpv6SvrAlgorithm.setStatus("current")


class _HwDhcpv6SvrWeight1_Type(Integer32):
    """Custom type hwDhcpv6SvrWeight1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwDhcpv6SvrWeight1_Type.__name__ = "Integer32"
_HwDhcpv6SvrWeight1_Object = MibTableColumn
hwDhcpv6SvrWeight1 = _HwDhcpv6SvrWeight1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 12),
    _HwDhcpv6SvrWeight1_Type()
)
hwDhcpv6SvrWeight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpv6SvrWeight1.setStatus("current")


class _HwDhcpv6SvrWeight2_Type(Integer32):
    """Custom type hwDhcpv6SvrWeight2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwDhcpv6SvrWeight2_Type.__name__ = "Integer32"
_HwDhcpv6SvrWeight2_Object = MibTableColumn
hwDhcpv6SvrWeight2 = _HwDhcpv6SvrWeight2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 13),
    _HwDhcpv6SvrWeight2_Type()
)
hwDhcpv6SvrWeight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpv6SvrWeight2.setStatus("current")


class _HwIPDhcpv6Svr1VrfName_Type(OctetString):
    """Custom type hwIPDhcpv6Svr1VrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwIPDhcpv6Svr1VrfName_Type.__name__ = "OctetString"
_HwIPDhcpv6Svr1VrfName_Object = MibTableColumn
hwIPDhcpv6Svr1VrfName = _HwIPDhcpv6Svr1VrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 14),
    _HwIPDhcpv6Svr1VrfName_Type()
)
hwIPDhcpv6Svr1VrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpv6Svr1VrfName.setStatus("current")


class _HwIPDhcpv6Svr2VrfName_Type(OctetString):
    """Custom type hwIPDhcpv6Svr2VrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwIPDhcpv6Svr2VrfName_Type.__name__ = "OctetString"
_HwIPDhcpv6Svr2VrfName_Object = MibTableColumn
hwIPDhcpv6Svr2VrfName = _HwIPDhcpv6Svr2VrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 15),
    _HwIPDhcpv6Svr2VrfName_Type()
)
hwIPDhcpv6Svr2VrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPDhcpv6Svr2VrfName.setStatus("current")
_HwDhcpv6SvrGroupRowStatus_Type = RowStatus
_HwDhcpv6SvrGroupRowStatus_Object = MibTableColumn
hwDhcpv6SvrGroupRowStatus = _HwDhcpv6SvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 16),
    _HwDhcpv6SvrGroupRowStatus_Type()
)
hwDhcpv6SvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpv6SvrGroupRowStatus.setStatus("current")


class _HwDhcpv6SvrSourceInterface_Type(OctetString):
    """Custom type hwDhcpv6SvrSourceInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwDhcpv6SvrSourceInterface_Type.__name__ = "OctetString"
_HwDhcpv6SvrSourceInterface_Object = MibTableColumn
hwDhcpv6SvrSourceInterface = _HwDhcpv6SvrSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 20, 1, 17),
    _HwDhcpv6SvrSourceInterface_Type()
)
hwDhcpv6SvrSourceInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpv6SvrSourceInterface.setStatus("current")
_HwIPv6RemotePoolTable_Object = MibTable
hwIPv6RemotePoolTable = _HwIPv6RemotePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21)
)
if mibBuilder.loadTexts:
    hwIPv6RemotePoolTable.setStatus("current")
_HwIPv6RemotePoolEntry_Object = MibTableRow
hwIPv6RemotePoolEntry = _HwIPv6RemotePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1)
)
hwIPv6RemotePoolEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolIndex"),
)
if mibBuilder.loadTexts:
    hwIPv6RemotePoolEntry.setStatus("current")


class _HwIPv6RemotePoolIndex_Type(Integer32):
    """Custom type hwIPv6RemotePoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwIPv6RemotePoolIndex_Type.__name__ = "Integer32"
_HwIPv6RemotePoolIndex_Object = MibTableColumn
hwIPv6RemotePoolIndex = _HwIPv6RemotePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 1),
    _HwIPv6RemotePoolIndex_Type()
)
hwIPv6RemotePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolIndex.setStatus("current")


class _HwIPv6RemotePoolName_Type(OctetString):
    """Custom type hwIPv6RemotePoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPv6RemotePoolName_Type.__name__ = "OctetString"
_HwIPv6RemotePoolName_Object = MibTableColumn
hwIPv6RemotePoolName = _HwIPv6RemotePoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 2),
    _HwIPv6RemotePoolName_Type()
)
hwIPv6RemotePoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolName.setStatus("current")


class _HwIPv6RemotePoolPrefixName_Type(OctetString):
    """Custom type hwIPv6RemotePoolPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPv6RemotePoolPrefixName_Type.__name__ = "OctetString"
_HwIPv6RemotePoolPrefixName_Object = MibTableColumn
hwIPv6RemotePoolPrefixName = _HwIPv6RemotePoolPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 3),
    _HwIPv6RemotePoolPrefixName_Type()
)
hwIPv6RemotePoolPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolPrefixName.setStatus("current")


class _HwIPv6RemotePoolDhcpv6SvrGroupName_Type(OctetString):
    """Custom type hwIPv6RemotePoolDhcpv6SvrGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPv6RemotePoolDhcpv6SvrGroupName_Type.__name__ = "OctetString"
_HwIPv6RemotePoolDhcpv6SvrGroupName_Object = MibTableColumn
hwIPv6RemotePoolDhcpv6SvrGroupName = _HwIPv6RemotePoolDhcpv6SvrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 4),
    _HwIPv6RemotePoolDhcpv6SvrGroupName_Type()
)
hwIPv6RemotePoolDhcpv6SvrGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolDhcpv6SvrGroupName.setStatus("current")
_HwIPv6RemotePoolAvailableStatus_Type = TruthValue
_HwIPv6RemotePoolAvailableStatus_Object = MibTableColumn
hwIPv6RemotePoolAvailableStatus = _HwIPv6RemotePoolAvailableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 5),
    _HwIPv6RemotePoolAvailableStatus_Type()
)
hwIPv6RemotePoolAvailableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolAvailableStatus.setStatus("current")
_HwIPv6RemotePoolExportHostRouteFlag_Type = TruthValue
_HwIPv6RemotePoolExportHostRouteFlag_Object = MibTableColumn
hwIPv6RemotePoolExportHostRouteFlag = _HwIPv6RemotePoolExportHostRouteFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 6),
    _HwIPv6RemotePoolExportHostRouteFlag_Type()
)
hwIPv6RemotePoolExportHostRouteFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolExportHostRouteFlag.setStatus("current")
_HwIPv6RemotePoolRowStatus_Type = RowStatus
_HwIPv6RemotePoolRowStatus_Object = MibTableColumn
hwIPv6RemotePoolRowStatus = _HwIPv6RemotePoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 7),
    _HwIPv6RemotePoolRowStatus_Type()
)
hwIPv6RemotePoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolRowStatus.setStatus("current")
_HwIPv6RemotePoolExportHostRouteIPv6Address_Type = TruthValue
_HwIPv6RemotePoolExportHostRouteIPv6Address_Object = MibTableColumn
hwIPv6RemotePoolExportHostRouteIPv6Address = _HwIPv6RemotePoolExportHostRouteIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 8),
    _HwIPv6RemotePoolExportHostRouteIPv6Address_Type()
)
hwIPv6RemotePoolExportHostRouteIPv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolExportHostRouteIPv6Address.setStatus("current")
_HwIPv6RemotePoolExportHostRoutePDPrefix_Type = TruthValue
_HwIPv6RemotePoolExportHostRoutePDPrefix_Object = MibTableColumn
hwIPv6RemotePoolExportHostRoutePDPrefix = _HwIPv6RemotePoolExportHostRoutePDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 9),
    _HwIPv6RemotePoolExportHostRoutePDPrefix_Type()
)
hwIPv6RemotePoolExportHostRoutePDPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolExportHostRoutePDPrefix.setStatus("current")
_HwIPv6RemotePoolExportHostRouteNDPrefix_Type = TruthValue
_HwIPv6RemotePoolExportHostRouteNDPrefix_Object = MibTableColumn
hwIPv6RemotePoolExportHostRouteNDPrefix = _HwIPv6RemotePoolExportHostRouteNDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 10),
    _HwIPv6RemotePoolExportHostRouteNDPrefix_Type()
)
hwIPv6RemotePoolExportHostRouteNDPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolExportHostRouteNDPrefix.setStatus("current")


class _HwIPv6RemotePoolWeight_Type(Integer32):
    """Custom type hwIPv6RemotePoolWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwIPv6RemotePoolWeight_Type.__name__ = "Integer32"
_HwIPv6RemotePoolWeight_Object = MibTableColumn
hwIPv6RemotePoolWeight = _HwIPv6RemotePoolWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 21, 1, 11),
    _HwIPv6RemotePoolWeight_Type()
)
hwIPv6RemotePoolWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPv6RemotePoolWeight.setStatus("current")
_HwIPv6PoolStatistic_ObjectIdentity = ObjectIdentity
hwIPv6PoolStatistic = _HwIPv6PoolStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22)
)
_HwIpv6PoolNum_Type = Integer32
_HwIpv6PoolNum_Object = MibScalar
hwIpv6PoolNum = _HwIpv6PoolNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 1),
    _HwIpv6PoolNum_Type()
)
hwIpv6PoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6PoolNum.setStatus("current")
_HwIpv6AddressIdleTotalNum_Type = Integer32
_HwIpv6AddressIdleTotalNum_Object = MibScalar
hwIpv6AddressIdleTotalNum = _HwIpv6AddressIdleTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 2),
    _HwIpv6AddressIdleTotalNum_Type()
)
hwIpv6AddressIdleTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6AddressIdleTotalNum.setStatus("current")
_HwIpv6PrefixIdleTotalNum_Type = Integer32
_HwIpv6PrefixIdleTotalNum_Object = MibScalar
hwIpv6PrefixIdleTotalNum = _HwIpv6PrefixIdleTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 3),
    _HwIpv6PrefixIdleTotalNum_Type()
)
hwIpv6PrefixIdleTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6PrefixIdleTotalNum.setStatus("current")
_HwIpv6AddressUsedTotalNum_Type = Integer32
_HwIpv6AddressUsedTotalNum_Object = MibScalar
hwIpv6AddressUsedTotalNum = _HwIpv6AddressUsedTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 4),
    _HwIpv6AddressUsedTotalNum_Type()
)
hwIpv6AddressUsedTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6AddressUsedTotalNum.setStatus("current")
_HwIpv6PrefixUsedTotalNum_Type = Integer32
_HwIpv6PrefixUsedTotalNum_Object = MibScalar
hwIpv6PrefixUsedTotalNum = _HwIpv6PrefixUsedTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 5),
    _HwIpv6PrefixUsedTotalNum_Type()
)
hwIpv6PrefixUsedTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6PrefixUsedTotalNum.setStatus("current")
_HwAllIPv6AddressTotalNum_Type = Integer32
_HwAllIPv6AddressTotalNum_Object = MibScalar
hwAllIPv6AddressTotalNum = _HwAllIPv6AddressTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 6),
    _HwAllIPv6AddressTotalNum_Type()
)
hwAllIPv6AddressTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllIPv6AddressTotalNum.setStatus("current")
_HwAllIPv6AddressUsedNum_Type = Integer32
_HwAllIPv6AddressUsedNum_Object = MibScalar
hwAllIPv6AddressUsedNum = _HwAllIPv6AddressUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 7),
    _HwAllIPv6AddressUsedNum_Type()
)
hwAllIPv6AddressUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllIPv6AddressUsedNum.setStatus("current")
_HwAllIPv6AddressIdleNum_Type = Integer32
_HwAllIPv6AddressIdleNum_Object = MibScalar
hwAllIPv6AddressIdleNum = _HwAllIPv6AddressIdleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 8),
    _HwAllIPv6AddressIdleNum_Type()
)
hwAllIPv6AddressIdleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllIPv6AddressIdleNum.setStatus("current")
_HwAllIPv6ConflictAddressNum_Type = Integer32
_HwAllIPv6ConflictAddressNum_Object = MibScalar
hwAllIPv6ConflictAddressNum = _HwAllIPv6ConflictAddressNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 9),
    _HwAllIPv6ConflictAddressNum_Type()
)
hwAllIPv6ConflictAddressNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllIPv6ConflictAddressNum.setStatus("current")
_HwAllIPv6ExcludeAddressNum_Type = Integer32
_HwAllIPv6ExcludeAddressNum_Object = MibScalar
hwAllIPv6ExcludeAddressNum = _HwAllIPv6ExcludeAddressNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 10),
    _HwAllIPv6ExcludeAddressNum_Type()
)
hwAllIPv6ExcludeAddressNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllIPv6ExcludeAddressNum.setStatus("current")
_HwAllIPv6AddressUsedPercent_Type = Integer32
_HwAllIPv6AddressUsedPercent_Object = MibScalar
hwAllIPv6AddressUsedPercent = _HwAllIPv6AddressUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 11),
    _HwAllIPv6AddressUsedPercent_Type()
)
hwAllIPv6AddressUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllIPv6AddressUsedPercent.setStatus("current")
_HwAllNDRAPrefixTotalNum_Type = Integer32
_HwAllNDRAPrefixTotalNum_Object = MibScalar
hwAllNDRAPrefixTotalNum = _HwAllNDRAPrefixTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 12),
    _HwAllNDRAPrefixTotalNum_Type()
)
hwAllNDRAPrefixTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllNDRAPrefixTotalNum.setStatus("current")
_HwAllNDRAPrefixUsedNum_Type = Integer32
_HwAllNDRAPrefixUsedNum_Object = MibScalar
hwAllNDRAPrefixUsedNum = _HwAllNDRAPrefixUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 13),
    _HwAllNDRAPrefixUsedNum_Type()
)
hwAllNDRAPrefixUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllNDRAPrefixUsedNum.setStatus("current")
_HwAllNDRAPrefixFreeNum_Type = Integer32
_HwAllNDRAPrefixFreeNum_Object = MibScalar
hwAllNDRAPrefixFreeNum = _HwAllNDRAPrefixFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 14),
    _HwAllNDRAPrefixFreeNum_Type()
)
hwAllNDRAPrefixFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllNDRAPrefixFreeNum.setStatus("current")
_HwAllNDRAPrefixConflictNum_Type = Integer32
_HwAllNDRAPrefixConflictNum_Object = MibScalar
hwAllNDRAPrefixConflictNum = _HwAllNDRAPrefixConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 15),
    _HwAllNDRAPrefixConflictNum_Type()
)
hwAllNDRAPrefixConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllNDRAPrefixConflictNum.setStatus("current")
_HwAllNDRAPrefixExcludeNum_Type = Integer32
_HwAllNDRAPrefixExcludeNum_Object = MibScalar
hwAllNDRAPrefixExcludeNum = _HwAllNDRAPrefixExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 16),
    _HwAllNDRAPrefixExcludeNum_Type()
)
hwAllNDRAPrefixExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllNDRAPrefixExcludeNum.setStatus("current")
_HwAllNDRAPrefixUsedPercent_Type = Integer32
_HwAllNDRAPrefixUsedPercent_Object = MibScalar
hwAllNDRAPrefixUsedPercent = _HwAllNDRAPrefixUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 17),
    _HwAllNDRAPrefixUsedPercent_Type()
)
hwAllNDRAPrefixUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllNDRAPrefixUsedPercent.setStatus("current")
_HwAllPDPrefixTotalNum_Type = Integer32
_HwAllPDPrefixTotalNum_Object = MibScalar
hwAllPDPrefixTotalNum = _HwAllPDPrefixTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 18),
    _HwAllPDPrefixTotalNum_Type()
)
hwAllPDPrefixTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllPDPrefixTotalNum.setStatus("current")
_HwAllPDPrefixUsedNum_Type = Integer32
_HwAllPDPrefixUsedNum_Object = MibScalar
hwAllPDPrefixUsedNum = _HwAllPDPrefixUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 19),
    _HwAllPDPrefixUsedNum_Type()
)
hwAllPDPrefixUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllPDPrefixUsedNum.setStatus("current")
_HwAllPDPrefixFreeNum_Type = Integer32
_HwAllPDPrefixFreeNum_Object = MibScalar
hwAllPDPrefixFreeNum = _HwAllPDPrefixFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 20),
    _HwAllPDPrefixFreeNum_Type()
)
hwAllPDPrefixFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllPDPrefixFreeNum.setStatus("current")
_HwAllPDPrefixConflictNum_Type = Integer32
_HwAllPDPrefixConflictNum_Object = MibScalar
hwAllPDPrefixConflictNum = _HwAllPDPrefixConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 21),
    _HwAllPDPrefixConflictNum_Type()
)
hwAllPDPrefixConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllPDPrefixConflictNum.setStatus("current")
_HwAllPDPrefixExcludeNum_Type = Integer32
_HwAllPDPrefixExcludeNum_Object = MibScalar
hwAllPDPrefixExcludeNum = _HwAllPDPrefixExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 22),
    _HwAllPDPrefixExcludeNum_Type()
)
hwAllPDPrefixExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllPDPrefixExcludeNum.setStatus("current")
_HwAllPDPrefixUsedPercent_Type = Integer32
_HwAllPDPrefixUsedPercent_Object = MibScalar
hwAllPDPrefixUsedPercent = _HwAllPDPrefixUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 22, 23),
    _HwAllPDPrefixUsedPercent_Type()
)
hwAllPDPrefixUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAllPDPrefixUsedPercent.setStatus("current")
_HwDhcpv6ServerTable_Object = MibTable
hwDhcpv6ServerTable = _HwDhcpv6ServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 23)
)
if mibBuilder.loadTexts:
    hwDhcpv6ServerTable.setStatus("current")
_HwDhcpv6ServerEntry_Object = MibTableRow
hwDhcpv6ServerEntry = _HwDhcpv6ServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 23, 1)
)
hwDhcpv6ServerEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpv6ServerEntry.setStatus("current")


class _HwDhcpv6SvrIndex_Type(Integer32):
    """Custom type hwDhcpv6SvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwDhcpv6SvrIndex_Type.__name__ = "Integer32"
_HwDhcpv6SvrIndex_Object = MibTableColumn
hwDhcpv6SvrIndex = _HwDhcpv6SvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 23, 1, 1),
    _HwDhcpv6SvrIndex_Type()
)
hwDhcpv6SvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpv6SvrIndex.setStatus("current")
_HwDhcpv6ServerIP_Type = Ipv6Address
_HwDhcpv6ServerIP_Object = MibTableColumn
hwDhcpv6ServerIP = _HwDhcpv6ServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 23, 1, 2),
    _HwDhcpv6ServerIP_Type()
)
hwDhcpv6ServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpv6ServerIP.setStatus("current")


class _HwDhcpv6ServerVRFName_Type(OctetString):
    """Custom type hwDhcpv6ServerVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwDhcpv6ServerVRFName_Type.__name__ = "OctetString"
_HwDhcpv6ServerVRFName_Object = MibTableColumn
hwDhcpv6ServerVRFName = _HwDhcpv6ServerVRFName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 23, 1, 3),
    _HwDhcpv6ServerVRFName_Type()
)
hwDhcpv6ServerVRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpv6ServerVRFName.setStatus("current")
_HwDhcpv6ServerIfIndex_Type = Integer32
_HwDhcpv6ServerIfIndex_Object = MibTableColumn
hwDhcpv6ServerIfIndex = _HwDhcpv6ServerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 23, 1, 4),
    _HwDhcpv6ServerIfIndex_Type()
)
hwDhcpv6ServerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpv6ServerIfIndex.setStatus("current")


class _HwDhcpv6ServerState_Type(Integer32):
    """Custom type hwDhcpv6ServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HwDhcpv6ServerState_Type.__name__ = "Integer32"
_HwDhcpv6ServerState_Object = MibTableColumn
hwDhcpv6ServerState = _HwDhcpv6ServerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 23, 1, 5),
    _HwDhcpv6ServerState_Type()
)
hwDhcpv6ServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpv6ServerState.setStatus("current")


class _HwDhcpv6ServerSendSolicitSpeedNum_Type(Integer32):
    """Custom type hwDhcpv6ServerSendSolicitSpeedNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwDhcpv6ServerSendSolicitSpeedNum_Type.__name__ = "Integer32"
_HwDhcpv6ServerSendSolicitSpeedNum_Object = MibTableColumn
hwDhcpv6ServerSendSolicitSpeedNum = _HwDhcpv6ServerSendSolicitSpeedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 23, 1, 6),
    _HwDhcpv6ServerSendSolicitSpeedNum_Type()
)
hwDhcpv6ServerSendSolicitSpeedNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpv6ServerSendSolicitSpeedNum.setStatus("current")


class _HwDhcpv6ServerSendSolicitSpeedSec_Type(Integer32):
    """Custom type hwDhcpv6ServerSendSolicitSpeedSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HwDhcpv6ServerSendSolicitSpeedSec_Type.__name__ = "Integer32"
_HwDhcpv6ServerSendSolicitSpeedSec_Object = MibTableColumn
hwDhcpv6ServerSendSolicitSpeedSec = _HwDhcpv6ServerSendSolicitSpeedSec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 23, 1, 7),
    _HwDhcpv6ServerSendSolicitSpeedSec_Type()
)
hwDhcpv6ServerSendSolicitSpeedSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpv6ServerSendSolicitSpeedSec.setStatus("current")
_HwIPV6AddressStatusTable_Object = MibTable
hwIPV6AddressStatusTable = _HwIPV6AddressStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 24)
)
if mibBuilder.loadTexts:
    hwIPV6AddressStatusTable.setStatus("current")
_HwIPV6AddressStatusEntry_Object = MibTableRow
hwIPV6AddressStatusEntry = _HwIPV6AddressStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 24, 1)
)
hwIPV6AddressStatusEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPv6PrefixIndex"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIPv6Address"),
)
if mibBuilder.loadTexts:
    hwIPV6AddressStatusEntry.setStatus("current")
_HwIPv6Address_Type = Ipv6Address
_HwIPv6Address_Object = MibTableColumn
hwIPv6Address = _HwIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 24, 1, 1),
    _HwIPv6Address_Type()
)
hwIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6Address.setStatus("current")


class _HwIPv6AddressStatus_Type(Integer32):
    """Custom type hwIPv6AddressStatus based on Integer32"""
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
        *(("conflictive", 3),
          ("flex", 4),
          ("idle", 0),
          ("occupied", 1),
          ("prohibitive", 2),
          ("radius", 6),
          ("reserved", 7),
          ("static", 5))
    )


_HwIPv6AddressStatus_Type.__name__ = "Integer32"
_HwIPv6AddressStatus_Object = MibTableColumn
hwIPv6AddressStatus = _HwIPv6AddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 24, 1, 2),
    _HwIPv6AddressStatus_Type()
)
hwIPv6AddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPv6AddressStatus.setStatus("current")


class _HwIPv6LocalPrefixName_Type(DisplayString):
    """Custom type hwIPv6LocalPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPv6LocalPrefixName_Type.__name__ = "DisplayString"
_HwIPv6LocalPrefixName_Object = MibTableColumn
hwIPv6LocalPrefixName = _HwIPv6LocalPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 24, 1, 3),
    _HwIPv6LocalPrefixName_Type()
)
hwIPv6LocalPrefixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6LocalPrefixName.setStatus("current")
_HwIPV6PrefixStatusTable_Object = MibTable
hwIPV6PrefixStatusTable = _HwIPV6PrefixStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 25)
)
if mibBuilder.loadTexts:
    hwIPV6PrefixStatusTable.setStatus("current")
_HwIPV6PrefixStatusEntry_Object = MibTableRow
hwIPV6PrefixStatusEntry = _HwIPV6PrefixStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 25, 1)
)
hwIPV6PrefixStatusEntry.setIndexNames(
    (0, "HUAWEI-IPPOOL-MIB", "hwIPv6PrefixIndex"),
    (0, "HUAWEI-IPPOOL-MIB", "hwIpv6Prefix"),
)
if mibBuilder.loadTexts:
    hwIPV6PrefixStatusEntry.setStatus("current")
_HwIpv6Prefix_Type = Ipv6AddressPrefix
_HwIpv6Prefix_Object = MibTableColumn
hwIpv6Prefix = _HwIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 25, 1, 1),
    _HwIpv6Prefix_Type()
)
hwIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6Prefix.setStatus("current")


class _HwIpv6PrefixLen_Type(Integer32):
    """Custom type hwIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwIpv6PrefixLen_Type.__name__ = "Integer32"
_HwIpv6PrefixLen_Object = MibTableColumn
hwIpv6PrefixLen = _HwIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 25, 1, 2),
    _HwIpv6PrefixLen_Type()
)
hwIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6PrefixLen.setStatus("current")


class _HwIPv6PrefixStatus_Type(Integer32):
    """Custom type hwIPv6PrefixStatus based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("binded", 8),
          ("conflictive", 3),
          ("flex", 4),
          ("idle", 0),
          ("occupied", 1),
          ("prohibitive", 2),
          ("radius", 6),
          ("reserved", 7),
          ("static", 5))
    )


_HwIPv6PrefixStatus_Type.__name__ = "Integer32"
_HwIPv6PrefixStatus_Object = MibTableColumn
hwIPv6PrefixStatus = _HwIPv6PrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 25, 1, 3),
    _HwIPv6PrefixStatus_Type()
)
hwIPv6PrefixStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPv6PrefixStatus.setStatus("current")


class _HwIPv6DelegationPrefixName_Type(DisplayString):
    """Custom type hwIPv6DelegationPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIPv6DelegationPrefixName_Type.__name__ = "DisplayString"
_HwIPv6DelegationPrefixName_Object = MibTableColumn
hwIPv6DelegationPrefixName = _HwIPv6DelegationPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 25, 1, 4),
    _HwIPv6DelegationPrefixName_Type()
)
hwIPv6DelegationPrefixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPv6DelegationPrefixName.setStatus("current")
_HwIPPoolConstantIndex_ObjectIdentity = ObjectIdentity
hwIPPoolConstantIndex = _HwIPPoolConstantIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 26)
)


class _HwIPPoolConstantIndexEnable_Type(Integer32):
    """Custom type hwIPPoolConstantIndexEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwIPPoolConstantIndexEnable_Type.__name__ = "Integer32"
_HwIPPoolConstantIndexEnable_Object = MibScalar
hwIPPoolConstantIndexEnable = _HwIPPoolConstantIndexEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 26, 1),
    _HwIPPoolConstantIndexEnable_Type()
)
hwIPPoolConstantIndexEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolConstantIndexEnable.setStatus("current")
_HwIPPoolSetting_ObjectIdentity = ObjectIdentity
hwIPPoolSetting = _HwIPPoolSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 27)
)


class _HwIPPoolAlgorithm_Type(Integer32):
    """Custom type hwIPPoolAlgorithm based on Integer32"""
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


_HwIPPoolAlgorithm_Type.__name__ = "Integer32"
_HwIPPoolAlgorithm_Object = MibScalar
hwIPPoolAlgorithm = _HwIPPoolAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 27, 1),
    _HwIPPoolAlgorithm_Type()
)
hwIPPoolAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPPoolAlgorithm.setStatus("current")


class _HwIPv6PoolAlgorithm_Type(Integer32):
    """Custom type hwIPv6PoolAlgorithm based on Integer32"""
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


_HwIPv6PoolAlgorithm_Type.__name__ = "Integer32"
_HwIPv6PoolAlgorithm_Object = MibScalar
hwIPv6PoolAlgorithm = _HwIPv6PoolAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 1, 27, 2),
    _HwIPv6PoolAlgorithm_Type()
)
hwIPv6PoolAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPv6PoolAlgorithm.setStatus("current")
_HwIPPoolMibTrap_ObjectIdentity = ObjectIdentity
hwIPPoolMibTrap = _HwIPPoolMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2)
)
_HwIPPoolTrapOid_ObjectIdentity = ObjectIdentity
hwIPPoolTrapOid = _HwIPPoolTrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 1)
)
_HwUserIPAddress_Type = IpAddress
_HwUserIPAddress_Object = MibScalar
hwUserIPAddress = _HwUserIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 1, 1),
    _HwUserIPAddress_Type()
)
hwUserIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUserIPAddress.setStatus("current")
_HwDHCPServerAddr_Type = IpAddress
_HwDHCPServerAddr_Object = MibScalar
hwDHCPServerAddr = _HwDHCPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 1, 2),
    _HwDHCPServerAddr_Type()
)
hwDHCPServerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDHCPServerAddr.setStatus("current")


class _HwDhcpSvrVrfName_Type(DisplayString):
    """Custom type hwDhcpSvrVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwDhcpSvrVrfName_Type.__name__ = "DisplayString"
_HwDhcpSvrVrfName_Object = MibScalar
hwDhcpSvrVrfName = _HwDhcpSvrVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 1, 3),
    _HwDhcpSvrVrfName_Type()
)
hwDhcpSvrVrfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDhcpSvrVrfName.setStatus("current")


class _HwIPPoolGroupIndex_Type(Integer32):
    """Custom type hwIPPoolGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIPPoolGroupIndex_Type.__name__ = "Integer32"
_HwIPPoolGroupIndex_Object = MibScalar
hwIPPoolGroupIndex = _HwIPPoolGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 1, 4),
    _HwIPPoolGroupIndex_Type()
)
hwIPPoolGroupIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPPoolGroupIndex.setStatus("current")


class _HwDhcpSvrDownReason_Type(DisplayString):
    """Custom type hwDhcpSvrDownReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwDhcpSvrDownReason_Type.__name__ = "DisplayString"
_HwDhcpSvrDownReason_Object = MibScalar
hwDhcpSvrDownReason = _HwDhcpSvrDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 1, 5),
    _HwDhcpSvrDownReason_Type()
)
hwDhcpSvrDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDhcpSvrDownReason.setStatus("current")


class _HwIPPoolDAPName_Type(DisplayString):
    """Custom type hwIPPoolDAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_HwIPPoolDAPName_Type.__name__ = "DisplayString"
_HwIPPoolDAPName_Object = MibScalar
hwIPPoolDAPName = _HwIPPoolDAPName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 1, 7),
    _HwIPPoolDAPName_Type()
)
hwIPPoolDAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPPoolDAPName.setStatus("current")


class _HwIPPoolDAPReason_Type(DisplayString):
    """Custom type hwIPPoolDAPReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwIPPoolDAPReason_Type.__name__ = "DisplayString"
_HwIPPoolDAPReason_Object = MibScalar
hwIPPoolDAPReason = _HwIPPoolDAPReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 1, 8),
    _HwIPPoolDAPReason_Type()
)
hwIPPoolDAPReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIPPoolDAPReason.setStatus("current")
_HwIPPoolTrapsDefine_ObjectIdentity = ObjectIdentity
hwIPPoolTrapsDefine = _HwIPPoolTrapsDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2)
)
_HwIPPoolTraps_ObjectIdentity = ObjectIdentity
hwIPPoolTraps = _HwIPPoolTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0)
)
_HwIpPoolMIBConformance_ObjectIdentity = ObjectIdentity
hwIpPoolMIBConformance = _HwIpPoolMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3)
)
_HwIpPoolCompliances_ObjectIdentity = ObjectIdentity
hwIpPoolCompliances = _HwIpPoolCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 1)
)
_HwIpPoolObjectGroups_ObjectIdentity = ObjectIdentity
hwIpPoolObjectGroups = _HwIpPoolObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2)
)

# Managed Objects groups

hwIpPoolTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 1)
)
hwIpPoolTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolRouterIPAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolRouterIPMask"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolPriDNSIPAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolSecDNSIPAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolPriNBNSIPAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolSecNBNSIPAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolIPAddrLease"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolVPNInstance"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolType"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolNetwork"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolNetworkMask"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolIPTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolIPUsedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolIPConflictNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolIPExcludeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolIPIdleNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolIPUsedPercent"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDNSIPAddrString"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDNSIPAddrStringUndo"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolNBNSIPAddrString"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolNBNSIPAddrStringUndo"))
)
if mibBuilder.loadTexts:
    hwIpPoolTableGroup.setStatus("current")

hwIpSectionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 2)
)
hwIpSectionTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPSectionIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPSectionDesc"),
        ("HUAWEI-IPPOOL-MIB", "hwIPSectionLowAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPSectionHighAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPSectionLength"),
        ("HUAWEI-IPPOOL-MIB", "hwIPSectionUsedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPSectionConflict"),
        ("HUAWEI-IPPOOL-MIB", "hwIPSectionInvalid"),
        ("HUAWEI-IPPOOL-MIB", "hwIPSectionAvailableNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPSectionRowStatus"))
)
if mibBuilder.loadTexts:
    hwIpSectionTableGroup.setStatus("current")

hwIpPoolExtTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 3)
)
hwIpPoolExtTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolAvailableStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionId1"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOption1"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionId2"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOption2"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionId3"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOption3"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionId4"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOption4"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDnsSuffix"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSvrIPRsv"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolIpAddrRenewal"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolIpAddrRebinding"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolSIPAddr1"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolSIPAddr2"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolSIPName1"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolSIPName2"))
)
if mibBuilder.loadTexts:
    hwIpPoolExtTableGroup.setStatus("current")

hwIpAddressStatusTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 4)
)
hwIpAddressStatusTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPAddress"),
        ("HUAWEI-IPPOOL-MIB", "hwIPAddressStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwPoolName"))
)
if mibBuilder.loadTexts:
    hwIpAddressStatusTableGroup.setStatus("current")

hwDhcpSvrGroupTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 5)
)
hwDhcpSvrGroupTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpSvrGroupIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpSvrGroupName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSvrPriAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSvrScdiAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSvrPriState"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpScdPriState"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSvrAutoRelease"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSvrRefCount"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSvrRowStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSvrPriVpnInstance"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSvrScdVpnInstance"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSvrSouce"))
)
if mibBuilder.loadTexts:
    hwDhcpSvrGroupTableGroup.setStatus("current")

hwRemotePoolTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 6)
)
hwRemotePoolTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolName"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolRouterIPAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolRouterIPMask"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolDhcpSvrGroupID"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolAvailableStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolRowStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolPriDNSIPAddress"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolSecDNSIPAddress"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolPriNBNSIPAddress"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolSecNBNSIPAddress"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolVPNInstance"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolDhcpGroupName"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolLeaseManageEnable"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolWeight"))
)
if mibBuilder.loadTexts:
    hwRemotePoolTableGroup.setStatus("current")

hwIpPoolStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 7)
)
hwIpPoolStatisticGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPIdleTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPUsedTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPConflictTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPExcludeTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPUsedPercent"))
)
if mibBuilder.loadTexts:
    hwIpPoolStatisticGroup.setStatus("current")

hwIpPoolTrapOidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 8)
)
hwIpPoolTrapOidGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwUserIPAddress"),
        ("HUAWEI-IPPOOL-MIB", "hwDHCPServerAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpSvrVrfName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpSvrDownReason"))
)
if mibBuilder.loadTexts:
    hwIpPoolTrapOidGroup.setStatus("current")

hwDhcpServerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 10)
)
hwDhcpServerTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwDhcpServerIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpServerIP"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpServerVRFName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpServerState"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpServerSendDisvSpdNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpServerSendDisvSpdSec"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpServerDeadCount"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpServerNakCount"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpServerTimeout"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDhcpServerDeadTime"))
)
if mibBuilder.loadTexts:
    hwDhcpServerTableGroup.setStatus("current")

hwIPPoolOptionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 11)
)
hwIPPoolOptionTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionId"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOption"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionRowStatus"))
)
if mibBuilder.loadTexts:
    hwIPPoolOptionTableGroup.setStatus("current")

hwIPPoolGroupTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 12)
)
hwIPPoolGroupTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupVPNInstance"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIncludeUndo"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwIPPoolGroupTableGroup.setStatus("current")

hwIPPoolGroupExtTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 13)
)
hwIPPoolGroupExtTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupExtIncludePoolName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupExtIncludePoolMoveOrder"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupExtRowStatus"))
)
if mibBuilder.loadTexts:
    hwIPPoolGroupExtTableGroup.setStatus("current")

hwIPPoolGroupDisplayTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 14)
)
hwIPPoolGroupDisplayTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIncludePoolNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupBoundByDomainNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIPTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIPUsedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIPConflictedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIPDisableNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIPDesignatedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIPFreeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIPUsedPercent"))
)
if mibBuilder.loadTexts:
    hwIPPoolGroupDisplayTableGroup.setStatus("current")

hwIPPoolDomainSearchListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 15)
)
hwIPPoolDomainSearchListGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolDomainSearchList"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDomainSearchListRowStatus"))
)
if mibBuilder.loadTexts:
    hwIPPoolDomainSearchListGroup.setStatus("current")

hwIPPoolOptionExtTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 16)
)
hwIPPoolOptionExtTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionSubId"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionSubType"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionSubValue"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpOptionSubRowStatus"))
)
if mibBuilder.loadTexts:
    hwIPPoolOptionExtTableGroup.setStatus("current")

hwIPPoolReplyOptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 17)
)
hwIPPoolReplyOptionGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPDhcpSpecOptionId"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpSpecOption"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpReplyOptionId"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpReplyOptionSubId"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpReplyOptionSubType"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpReplyOptionSub"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpReplyOptionRowStatus"))
)
if mibBuilder.loadTexts:
    hwIPPoolReplyOptionGroup.setStatus("current")

hwIPv6PrefixTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 18)
)
hwIPv6PrefixTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixType"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6Prefix"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixLen"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixDelegatingLen"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixAdvPreferredLifetime"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixAdvValidLifetime"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixAvailableStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6VPNInstance"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixReservedFlag"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6LinkAddress"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6SlaacUnsharedFlag"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixRowStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolPDUnshareOnly"))
)
if mibBuilder.loadTexts:
    hwIPv6PrefixTableGroup.setStatus("current")

hwIPv6PoolTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 19)
)
hwIPv6PoolTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPv6PoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolType"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolPrefixName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolDnsIPAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolDnsSearchList"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolPreference"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolAvailableStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolRenewPercent"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolRebindingPercent"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolRapidCommitFlag"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolUnicastOption"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolAFTRName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolRowStatus"))
)
if mibBuilder.loadTexts:
    hwIPv6PoolTableGroup.setStatus("current")

hwIPv6PoolStatusTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 20)
)
hwIPv6PoolStatusTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPv6FreeAddressNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6UsedAddressNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6FreePrefixNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6UsedPrefixNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6AddressTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6AddressUsedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6AddressFreeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6AddressConflictNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6AddressExcludeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6AddressUsedPercent"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6NDRAPrefixTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6NDRAPrefixUsedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6NDRAPrefixFreeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6NDRAPrefixConflictNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6NDRAPrefixExcludeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6NDRAPrefixUsedPercent"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PDPrefixTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PDPrefixUsedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PDPrefixFreeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PDPrefixConflictNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PDPrefixExcludeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PDPrefixUsedPercent"))
)
if mibBuilder.loadTexts:
    hwIPv6PoolStatusTableGroup.setStatus("current")

hwIPv6DuidBindPrefixTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 21)
)
hwIPv6DuidBindPrefixTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPv6ClientDuid"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6BindPrefix"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6DuidBindPrefixRowStatus"))
)
if mibBuilder.loadTexts:
    hwIPv6DuidBindPrefixTableGroup.setStatus("current")

hwDhcpv6SvrGroupTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 22)
)
hwDhcpv6SvrGroupTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrGroupIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrGroupName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpv6SvrAddr1"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpv6SvrAddr2"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpv6PriSvrState"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpv6ScdSvrState"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpv6SvrAutoRelease"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpv6SvrGroupRefCount"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrInterface1"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrInterface2"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrAlgorithm"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrWeight1"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrWeight2"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpv6Svr1VrfName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPDhcpv6Svr2VrfName"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrGroupRowStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpv6SvrSourceInterface"))
)
if mibBuilder.loadTexts:
    hwDhcpv6SvrGroupTableGroup.setStatus("current")

hwIPv6RemotePoolTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 23)
)
hwIPv6RemotePoolTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolPrefixName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolDhcpv6SvrGroupName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolAvailableStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolExportHostRouteFlag"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolRowStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolExportHostRouteIPv6Address"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolExportHostRoutePDPrefix"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolExportHostRouteNDPrefix"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6RemotePoolWeight"))
)
if mibBuilder.loadTexts:
    hwIPv6RemotePoolTableGroup.setStatus("current")

hwIPv6PoolStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 24)
)
hwIPv6PoolStatisticGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIpv6PoolNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIpv6AddressIdleTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIpv6PrefixIdleTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIpv6AddressUsedTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwIpv6PrefixUsedTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllIPv6AddressTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllIPv6AddressUsedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllIPv6AddressIdleNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllIPv6ConflictAddressNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllIPv6ExcludeAddressNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllIPv6AddressUsedPercent"),
        ("HUAWEI-IPPOOL-MIB", "hwAllNDRAPrefixTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllNDRAPrefixUsedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllNDRAPrefixFreeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllNDRAPrefixConflictNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllNDRAPrefixExcludeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllNDRAPrefixUsedPercent"),
        ("HUAWEI-IPPOOL-MIB", "hwAllPDPrefixTotalNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllPDPrefixUsedNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllPDPrefixFreeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllPDPrefixConflictNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllPDPrefixExcludeNum"),
        ("HUAWEI-IPPOOL-MIB", "hwAllPDPrefixUsedPercent"))
)
if mibBuilder.loadTexts:
    hwIPv6PoolStatisticGroup.setStatus("current")

hwIPV6AddressStatusTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 25)
)
hwIPV6AddressStatusTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPv6Address"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6AddressStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6LocalPrefixName"))
)
if mibBuilder.loadTexts:
    hwIPV6AddressStatusTableGroup.setStatus("current")

hwIPV6PrefixStatusTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 26)
)
hwIPV6PrefixStatusTableGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIpv6Prefix"),
        ("HUAWEI-IPPOOL-MIB", "hwIpv6PrefixLen"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixStatus"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6DelegationPrefixName"))
)
if mibBuilder.loadTexts:
    hwIPV6PrefixStatusTableGroup.setStatus("current")

hwIPPoolConstantIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 27)
)
hwIPPoolConstantIndexGroup.setObjects(
    ("HUAWEI-IPPOOL-MIB", "hwIPPoolConstantIndexEnable")
)
if mibBuilder.loadTexts:
    hwIPPoolConstantIndexGroup.setStatus("current")


# Notification objects

hwUserIPConflictAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 1)
)
hwUserIPConflictAlarm.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwUserIPAddress"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolName"))
)
if mibBuilder.loadTexts:
    hwUserIPConflictAlarm.setStatus(
        "current"
    )

hwUserIPLeaseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 2)
)
hwUserIPLeaseAlarm.setObjects(
    ("HUAWEI-IPPOOL-MIB", "hwUserIPAddress")
)
if mibBuilder.loadTexts:
    hwUserIPLeaseAlarm.setStatus(
        "current"
    )

hwAllocUserIPFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 3)
)
hwAllocUserIPFailAlarm.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolName"))
)
if mibBuilder.loadTexts:
    hwAllocUserIPFailAlarm.setStatus(
        "current"
    )

hwDhcpServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 4)
)
hwDhcpServerDown.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwDHCPServerAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolRouterIPAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpSvrVrfName"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpSvrDownReason"))
)
if mibBuilder.loadTexts:
    hwDhcpServerDown.setStatus(
        "current"
    )

hwLocalIPPoolDifferWithServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 5)
)
hwLocalIPPoolDifferWithServer.setObjects(
    ("HUAWEI-IPPOOL-MIB", "hwRemoteIPPoolName")
)
if mibBuilder.loadTexts:
    hwLocalIPPoolDifferWithServer.setStatus(
        "current"
    )

hwUsedIPReachThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 6)
)
hwUsedIPReachThreshold.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolName"))
)
if mibBuilder.loadTexts:
    hwUsedIPReachThreshold.setStatus(
        "current"
    )

hwUsedIPReachThresholdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 7)
)
hwUsedIPReachThresholdResume.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolName"))
)
if mibBuilder.loadTexts:
    hwUsedIPReachThresholdResume.setStatus(
        "current"
    )

hwUsedDeleteUnnumberedRouter = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 8)
)
hwUsedDeleteUnnumberedRouter.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolName"))
)
if mibBuilder.loadTexts:
    hwUsedDeleteUnnumberedRouter.setStatus(
        "current"
    )

hwPoolGroupUsedIPReachThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 9)
)
hwPoolGroupUsedIPReachThreshold.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupName"))
)
if mibBuilder.loadTexts:
    hwPoolGroupUsedIPReachThreshold.setStatus(
        "current"
    )

hwPoolGroupUsedIPReachThresholdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 10)
)
hwPoolGroupUsedIPReachThresholdResume.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupName"))
)
if mibBuilder.loadTexts:
    hwPoolGroupUsedIPReachThresholdResume.setStatus(
        "current"
    )

hwIPPoolConstantIndexFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 11)
)
if mibBuilder.loadTexts:
    hwIPPoolConstantIndexFail.setStatus(
        "current"
    )

hwIPv6PrefixConstantIndexFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 12)
)
if mibBuilder.loadTexts:
    hwIPv6PrefixConstantIndexFail.setStatus(
        "current"
    )

hwIPv6PoolConstantIndexFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 13)
)
if mibBuilder.loadTexts:
    hwIPv6PoolConstantIndexFail.setStatus(
        "current"
    )

hwUsedIPExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 14)
)
hwUsedIPExhaust.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolName"))
)
if mibBuilder.loadTexts:
    hwUsedIPExhaust.setStatus(
        "current"
    )

hwUsedIPExhaustResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 15)
)
hwUsedIPExhaustResume.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolName"))
)
if mibBuilder.loadTexts:
    hwUsedIPExhaustResume.setStatus(
        "current"
    )

hwPoolGroupUsedIPExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 16)
)
hwPoolGroupUsedIPExhaust.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupName"))
)
if mibBuilder.loadTexts:
    hwPoolGroupUsedIPExhaust.setStatus(
        "current"
    )

hwPoolGroupUsedIPExhaustResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 17)
)
hwPoolGroupUsedIPExhaustResume.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolGroupName"))
)
if mibBuilder.loadTexts:
    hwPoolGroupUsedIPExhaustResume.setStatus(
        "current"
    )

hwUsedIPv6AddressAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 18)
)
hwUsedIPv6AddressAlarm.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPv6PoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolName"))
)
if mibBuilder.loadTexts:
    hwUsedIPv6AddressAlarm.setStatus(
        "current"
    )

hwUsedIPv6AddressAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 19)
)
hwUsedIPv6AddressAlarmResume.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPv6PoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolName"))
)
if mibBuilder.loadTexts:
    hwUsedIPv6AddressAlarmResume.setStatus(
        "current"
    )

hwIPv6AddressExhaustAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 20)
)
hwIPv6AddressExhaustAlarm.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPv6PoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolName"))
)
if mibBuilder.loadTexts:
    hwIPv6AddressExhaustAlarm.setStatus(
        "current"
    )

hwIPv6AddressExhaustAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 21)
)
hwIPv6AddressExhaustAlarmResume.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPv6PoolIndex"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolName"))
)
if mibBuilder.loadTexts:
    hwIPv6AddressExhaustAlarmResume.setStatus(
        "current"
    )

hwIPPoolDAPApplyUnsuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 22)
)
hwIPPoolDAPApplyUnsuccessful.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolRouterIPAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolRouterIPMask"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDAPReason"))
)
if mibBuilder.loadTexts:
    hwIPPoolDAPApplyUnsuccessful.setStatus(
        "current"
    )

hwIPPoolDAPReleaseUnsuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 23)
)
hwIPPoolDAPReleaseUnsuccessful.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolRouterIPAddr"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolRouterIPMask"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDAPReason"))
)
if mibBuilder.loadTexts:
    hwIPPoolDAPReleaseUnsuccessful.setStatus(
        "current"
    )

hwIPPoolDAPSubnetFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 24)
)
hwIPPoolDAPSubnetFull.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwIPPoolName"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolDAPName"))
)
if mibBuilder.loadTexts:
    hwIPPoolDAPSubnetFull.setStatus(
        "current"
    )

hwIPPoolDAPDeviceSubnetFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 2, 2, 0, 25)
)
if mibBuilder.loadTexts:
    hwIPPoolDAPDeviceSubnetFull.setStatus(
        "current"
    )


# Notifications groups

hwIpPoolTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 2, 9)
)
hwIpPoolTrapsGroup.setObjects(
      *(("HUAWEI-IPPOOL-MIB", "hwUserIPConflictAlarm"),
        ("HUAWEI-IPPOOL-MIB", "hwUserIPLeaseAlarm"),
        ("HUAWEI-IPPOOL-MIB", "hwAllocUserIPFailAlarm"),
        ("HUAWEI-IPPOOL-MIB", "hwDhcpServerDown"),
        ("HUAWEI-IPPOOL-MIB", "hwLocalIPPoolDifferWithServer"),
        ("HUAWEI-IPPOOL-MIB", "hwUsedIPReachThreshold"),
        ("HUAWEI-IPPOOL-MIB", "hwUsedIPReachThresholdResume"),
        ("HUAWEI-IPPOOL-MIB", "hwUsedDeleteUnnumberedRouter"),
        ("HUAWEI-IPPOOL-MIB", "hwPoolGroupUsedIPReachThreshold"),
        ("HUAWEI-IPPOOL-MIB", "hwPoolGroupUsedIPReachThresholdResume"),
        ("HUAWEI-IPPOOL-MIB", "hwIPPoolConstantIndexFail"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PrefixConstantIndexFail"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6PoolConstantIndexFail"),
        ("HUAWEI-IPPOOL-MIB", "hwUsedIPExhaust"),
        ("HUAWEI-IPPOOL-MIB", "hwUsedIPExhaustResume"),
        ("HUAWEI-IPPOOL-MIB", "hwPoolGroupUsedIPExhaust"),
        ("HUAWEI-IPPOOL-MIB", "hwPoolGroupUsedIPExhaustResume"),
        ("HUAWEI-IPPOOL-MIB", "hwUsedIPv6AddressAlarm"),
        ("HUAWEI-IPPOOL-MIB", "hwUsedIPv6AddressAlarmResume"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6AddressExhaustAlarm"),
        ("HUAWEI-IPPOOL-MIB", "hwIPv6AddressExhaustAlarmResume"))
)
if mibBuilder.loadTexts:
    hwIpPoolTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIpPoolCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwIpPoolCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-IPPOOL-MIB",
    **{"hwIppool": hwIppool,
       "hwIPPoolMibObjects": hwIPPoolMibObjects,
       "hwIPPoolTable": hwIPPoolTable,
       "hwIPPoolEntry": hwIPPoolEntry,
       "hwIPPoolIndex": hwIPPoolIndex,
       "hwIPPoolName": hwIPPoolName,
       "hwIPPoolRouterIPAddr": hwIPPoolRouterIPAddr,
       "hwIPPoolRouterIPMask": hwIPPoolRouterIPMask,
       "hwIPPoolPriDNSIPAddr": hwIPPoolPriDNSIPAddr,
       "hwIPPoolSecDNSIPAddr": hwIPPoolSecDNSIPAddr,
       "hwIPPoolPriNBNSIPAddr": hwIPPoolPriNBNSIPAddr,
       "hwIPPoolSecNBNSIPAddr": hwIPPoolSecNBNSIPAddr,
       "hwIPPoolIPAddrLease": hwIPPoolIPAddrLease,
       "hwIPPoolStatus": hwIPPoolStatus,
       "hwIPPoolVPNInstance": hwIPPoolVPNInstance,
       "hwIPPoolType": hwIPPoolType,
       "hwIPPoolNetwork": hwIPPoolNetwork,
       "hwIPPoolNetworkMask": hwIPPoolNetworkMask,
       "hwIPPoolIPTotalNum": hwIPPoolIPTotalNum,
       "hwIPPoolIPUsedNum": hwIPPoolIPUsedNum,
       "hwIPPoolIPConflictNum": hwIPPoolIPConflictNum,
       "hwIPPoolIPExcludeNum": hwIPPoolIPExcludeNum,
       "hwIPPoolIPIdleNum": hwIPPoolIPIdleNum,
       "hwIPPoolIPUsedPercent": hwIPPoolIPUsedPercent,
       "hwIPPoolDNSIPAddrString": hwIPPoolDNSIPAddrString,
       "hwIPPoolDNSIPAddrStringUndo": hwIPPoolDNSIPAddrStringUndo,
       "hwIPPoolNBNSIPAddrString": hwIPPoolNBNSIPAddrString,
       "hwIPPoolNBNSIPAddrStringUndo": hwIPPoolNBNSIPAddrStringUndo,
       "hwIPPoolRouterUnnumberedIfName": hwIPPoolRouterUnnumberedIfName,
       "hwIPPoolConflictAutoRecycleInterval": hwIPPoolConflictAutoRecycleInterval,
       "hwIPPoolLowAddr": hwIPPoolLowAddr,
       "hwIPPoolHighAddr": hwIPPoolHighAddr,
       "hwIPPoolReqNum": hwIPPoolReqNum,
       "hwIPPoolReqSucNum": hwIPPoolReqSucNum,
       "hwIPSectionTable": hwIPSectionTable,
       "hwIPSectionEntry": hwIPSectionEntry,
       "hwIPSectionIndex": hwIPSectionIndex,
       "hwIPSectionDesc": hwIPSectionDesc,
       "hwIPSectionLowAddr": hwIPSectionLowAddr,
       "hwIPSectionHighAddr": hwIPSectionHighAddr,
       "hwIPSectionLength": hwIPSectionLength,
       "hwIPSectionUsedNum": hwIPSectionUsedNum,
       "hwIPSectionConflict": hwIPSectionConflict,
       "hwIPSectionInvalid": hwIPSectionInvalid,
       "hwIPSectionAvailableNum": hwIPSectionAvailableNum,
       "hwIPSectionRowStatus": hwIPSectionRowStatus,
       "hwIPPoolExtTable": hwIPPoolExtTable,
       "hwIPPoolExtEntry": hwIPPoolExtEntry,
       "hwIPPoolAvailableStatus": hwIPPoolAvailableStatus,
       "hwIPDhcpOptionId1": hwIPDhcpOptionId1,
       "hwIPDhcpOption1": hwIPDhcpOption1,
       "hwIPDhcpOptionId2": hwIPDhcpOptionId2,
       "hwIPDhcpOption2": hwIPDhcpOption2,
       "hwIPDhcpOptionId3": hwIPDhcpOptionId3,
       "hwIPDhcpOption3": hwIPDhcpOption3,
       "hwIPDhcpOptionId4": hwIPDhcpOptionId4,
       "hwIPDhcpOption4": hwIPDhcpOption4,
       "hwIPDnsSuffix": hwIPDnsSuffix,
       "hwIPDhcpSvrIPRsv": hwIPDhcpSvrIPRsv,
       "hwIPPoolIpAddrRenewal": hwIPPoolIpAddrRenewal,
       "hwIPPoolIpAddrRebinding": hwIPPoolIpAddrRebinding,
       "hwIPPoolSIPAddr1": hwIPPoolSIPAddr1,
       "hwIPPoolSIPAddr2": hwIPPoolSIPAddr2,
       "hwIPPoolSIPName1": hwIPPoolSIPName1,
       "hwIPPoolSIPName2": hwIPPoolSIPName2,
       "hwIPAddressStatusTable": hwIPAddressStatusTable,
       "hwIPAddressStatusEntry": hwIPAddressStatusEntry,
       "hwIPAddress": hwIPAddress,
       "hwIPAddressStatus": hwIPAddressStatus,
       "hwPoolName": hwPoolName,
       "hwDhcpSvrGroupTable": hwDhcpSvrGroupTable,
       "hwDhcpSvrGroupEntry": hwDhcpSvrGroupEntry,
       "hwIPPoolDhcpSvrGroupIndex": hwIPPoolDhcpSvrGroupIndex,
       "hwIPPoolDhcpSvrGroupName": hwIPPoolDhcpSvrGroupName,
       "hwIPDhcpSvrPriAddr": hwIPDhcpSvrPriAddr,
       "hwIPDhcpSvrScdiAddr": hwIPDhcpSvrScdiAddr,
       "hwIPDhcpSvrPriState": hwIPDhcpSvrPriState,
       "hwIPDhcpScdPriState": hwIPDhcpScdPriState,
       "hwIPDhcpSvrAutoRelease": hwIPDhcpSvrAutoRelease,
       "hwIPDhcpSvrRefCount": hwIPDhcpSvrRefCount,
       "hwIPDhcpSvrRowStatus": hwIPDhcpSvrRowStatus,
       "hwIPDhcpSvrPriVpnInstance": hwIPDhcpSvrPriVpnInstance,
       "hwIPDhcpSvrScdVpnInstance": hwIPDhcpSvrScdVpnInstance,
       "hwIPDhcpSvrSouce": hwIPDhcpSvrSouce,
       "hwRemotePoolTable": hwRemotePoolTable,
       "hwRemotePoolEntry": hwRemotePoolEntry,
       "hwRemoteIPPoolIndex": hwRemoteIPPoolIndex,
       "hwRemoteIPPoolName": hwRemoteIPPoolName,
       "hwRemoteIPPoolRouterIPAddr": hwRemoteIPPoolRouterIPAddr,
       "hwRemoteIPPoolRouterIPMask": hwRemoteIPPoolRouterIPMask,
       "hwRemoteIPPoolDhcpSvrGroupID": hwRemoteIPPoolDhcpSvrGroupID,
       "hwRemoteIPPoolAvailableStatus": hwRemoteIPPoolAvailableStatus,
       "hwRemoteIPPoolRowStatus": hwRemoteIPPoolRowStatus,
       "hwRemoteIPPoolPriDNSIPAddress": hwRemoteIPPoolPriDNSIPAddress,
       "hwRemoteIPPoolSecDNSIPAddress": hwRemoteIPPoolSecDNSIPAddress,
       "hwRemoteIPPoolPriNBNSIPAddress": hwRemoteIPPoolPriNBNSIPAddress,
       "hwRemoteIPPoolSecNBNSIPAddress": hwRemoteIPPoolSecNBNSIPAddress,
       "hwRemoteIPPoolVPNInstance": hwRemoteIPPoolVPNInstance,
       "hwRemoteIPPoolDhcpGroupName": hwRemoteIPPoolDhcpGroupName,
       "hwRemoteIPPoolLeaseManageEnable": hwRemoteIPPoolLeaseManageEnable,
       "hwRemoteIPPoolWeight": hwRemoteIPPoolWeight,
       "hwIPPoolStatistic": hwIPPoolStatistic,
       "hwIPPoolNum": hwIPPoolNum,
       "hwIPIdleTotalNum": hwIPIdleTotalNum,
       "hwIPUsedTotalNum": hwIPUsedTotalNum,
       "hwIPConflictTotalNum": hwIPConflictTotalNum,
       "hwIPExcludeTotalNum": hwIPExcludeTotalNum,
       "hwIPTotalNum": hwIPTotalNum,
       "hwIPUsedPercent": hwIPUsedPercent,
       "hwDhcpServerTable": hwDhcpServerTable,
       "hwDhcpServerEntry": hwDhcpServerEntry,
       "hwDhcpServerIndex": hwDhcpServerIndex,
       "hwIPPoolDhcpServerIP": hwIPPoolDhcpServerIP,
       "hwIPPoolDhcpServerVRFName": hwIPPoolDhcpServerVRFName,
       "hwIPPoolDhcpServerState": hwIPPoolDhcpServerState,
       "hwIPPoolDhcpServerSendDisvSpdNum": hwIPPoolDhcpServerSendDisvSpdNum,
       "hwIPPoolDhcpServerSendDisvSpdSec": hwIPPoolDhcpServerSendDisvSpdSec,
       "hwIPPoolDhcpServerDeadCount": hwIPPoolDhcpServerDeadCount,
       "hwIPPoolDhcpServerNakCount": hwIPPoolDhcpServerNakCount,
       "hwIPPoolDhcpServerTimeout": hwIPPoolDhcpServerTimeout,
       "hwIPPoolDhcpServerDeadTime": hwIPPoolDhcpServerDeadTime,
       "hwIPPoolOptionTable": hwIPPoolOptionTable,
       "hwIPPoolOptionEntry": hwIPPoolOptionEntry,
       "hwIPDhcpOptionId": hwIPDhcpOptionId,
       "hwIPDhcpOption": hwIPDhcpOption,
       "hwIPDhcpOptionRowStatus": hwIPDhcpOptionRowStatus,
       "hwIPPoolGroupTable": hwIPPoolGroupTable,
       "hwIPPoolGroupEntry": hwIPPoolGroupEntry,
       "hwIPPoolGroupName": hwIPPoolGroupName,
       "hwIPPoolGroupVPNInstance": hwIPPoolGroupVPNInstance,
       "hwIPPoolGroupIncludeUndo": hwIPPoolGroupIncludeUndo,
       "hwIPPoolGroupRowStatus": hwIPPoolGroupRowStatus,
       "hwIPPoolGroupExtTable": hwIPPoolGroupExtTable,
       "hwIPPoolGroupExtEntry": hwIPPoolGroupExtEntry,
       "hwIPPoolGroupExtIncludePoolName": hwIPPoolGroupExtIncludePoolName,
       "hwIPPoolGroupExtIncludePoolMoveOrder": hwIPPoolGroupExtIncludePoolMoveOrder,
       "hwIPPoolGroupExtRowStatus": hwIPPoolGroupExtRowStatus,
       "hwIPPoolGroupDisplayTable": hwIPPoolGroupDisplayTable,
       "hwIPPoolGroupDisplayEntry": hwIPPoolGroupDisplayEntry,
       "hwIPPoolGroupIncludePoolNum": hwIPPoolGroupIncludePoolNum,
       "hwIPPoolGroupBoundByDomainNum": hwIPPoolGroupBoundByDomainNum,
       "hwIPPoolGroupIPTotalNum": hwIPPoolGroupIPTotalNum,
       "hwIPPoolGroupIPUsedNum": hwIPPoolGroupIPUsedNum,
       "hwIPPoolGroupIPConflictedNum": hwIPPoolGroupIPConflictedNum,
       "hwIPPoolGroupIPDisableNum": hwIPPoolGroupIPDisableNum,
       "hwIPPoolGroupIPDesignatedNum": hwIPPoolGroupIPDesignatedNum,
       "hwIPPoolGroupIPFreeNum": hwIPPoolGroupIPFreeNum,
       "hwIPPoolGroupIPUsedPercent": hwIPPoolGroupIPUsedPercent,
       "hwIPPoolDomainSearchListTable": hwIPPoolDomainSearchListTable,
       "hwIPPoolDomainSearchListEntry": hwIPPoolDomainSearchListEntry,
       "hwIPPoolDomainSearchList": hwIPPoolDomainSearchList,
       "hwIPPoolDomainSearchListRowStatus": hwIPPoolDomainSearchListRowStatus,
       "hwIPPoolOptionExtTable": hwIPPoolOptionExtTable,
       "hwIPPoolOptionExtEntry": hwIPPoolOptionExtEntry,
       "hwIPDhcpOptionSubId": hwIPDhcpOptionSubId,
       "hwIPDhcpOptionSubType": hwIPDhcpOptionSubType,
       "hwIPDhcpOptionSubValue": hwIPDhcpOptionSubValue,
       "hwIPDhcpOptionSubRowStatus": hwIPDhcpOptionSubRowStatus,
       "hwIPPoolReplyOptionTable": hwIPPoolReplyOptionTable,
       "hwIPPoolReplyOptionEntry": hwIPPoolReplyOptionEntry,
       "hwIPDhcpSpecOptionId": hwIPDhcpSpecOptionId,
       "hwIPDhcpSpecOption": hwIPDhcpSpecOption,
       "hwIPDhcpReplyOptionId": hwIPDhcpReplyOptionId,
       "hwIPDhcpReplyOptionSubId": hwIPDhcpReplyOptionSubId,
       "hwIPDhcpReplyOptionSubType": hwIPDhcpReplyOptionSubType,
       "hwIPDhcpReplyOptionSub": hwIPDhcpReplyOptionSub,
       "hwIPDhcpReplyOptionRowStatus": hwIPDhcpReplyOptionRowStatus,
       "hwIPv6PrefixTable": hwIPv6PrefixTable,
       "hwIPv6PrefixEntry": hwIPv6PrefixEntry,
       "hwIPv6PrefixIndex": hwIPv6PrefixIndex,
       "hwIPv6PrefixName": hwIPv6PrefixName,
       "hwIPv6PrefixType": hwIPv6PrefixType,
       "hwIPv6Prefix": hwIPv6Prefix,
       "hwIPv6PrefixLen": hwIPv6PrefixLen,
       "hwIPv6PrefixDelegatingLen": hwIPv6PrefixDelegatingLen,
       "hwIPv6PrefixAdvPreferredLifetime": hwIPv6PrefixAdvPreferredLifetime,
       "hwIPv6PrefixAdvValidLifetime": hwIPv6PrefixAdvValidLifetime,
       "hwIPv6PrefixAvailableStatus": hwIPv6PrefixAvailableStatus,
       "hwIPv6VPNInstance": hwIPv6VPNInstance,
       "hwIPv6PrefixReservedFlag": hwIPv6PrefixReservedFlag,
       "hwIPv6LinkAddress": hwIPv6LinkAddress,
       "hwIPv6SlaacUnsharedFlag": hwIPv6SlaacUnsharedFlag,
       "hwIPv6PrefixRowStatus": hwIPv6PrefixRowStatus,
       "hwIPPoolPDUnshareOnly": hwIPPoolPDUnshareOnly,
       "hwIPv6PoolTable": hwIPv6PoolTable,
       "hwIPv6PoolEntry": hwIPv6PoolEntry,
       "hwIPv6PoolIndex": hwIPv6PoolIndex,
       "hwIPv6PoolName": hwIPv6PoolName,
       "hwIPv6PoolType": hwIPv6PoolType,
       "hwIPv6PoolPrefixName": hwIPv6PoolPrefixName,
       "hwIPv6PoolDnsIPAddr": hwIPv6PoolDnsIPAddr,
       "hwIPv6PoolDnsSearchList": hwIPv6PoolDnsSearchList,
       "hwIPv6PoolPreference": hwIPv6PoolPreference,
       "hwIPv6PoolAvailableStatus": hwIPv6PoolAvailableStatus,
       "hwIPv6PoolRenewPercent": hwIPv6PoolRenewPercent,
       "hwIPv6PoolRebindingPercent": hwIPv6PoolRebindingPercent,
       "hwIPv6PoolRapidCommitFlag": hwIPv6PoolRapidCommitFlag,
       "hwIPv6PoolUnicastOption": hwIPv6PoolUnicastOption,
       "hwIPv6PoolAFTRName": hwIPv6PoolAFTRName,
       "hwIPv6PoolRowStatus": hwIPv6PoolRowStatus,
       "hwIPv6PoolStatusTable": hwIPv6PoolStatusTable,
       "hwIPv6PoolStatusEntry": hwIPv6PoolStatusEntry,
       "hwIPv6FreeAddressNum": hwIPv6FreeAddressNum,
       "hwIPv6UsedAddressNum": hwIPv6UsedAddressNum,
       "hwIPv6FreePrefixNum": hwIPv6FreePrefixNum,
       "hwIPv6UsedPrefixNum": hwIPv6UsedPrefixNum,
       "hwIPv6AddressTotalNum": hwIPv6AddressTotalNum,
       "hwIPv6AddressUsedNum": hwIPv6AddressUsedNum,
       "hwIPv6AddressFreeNum": hwIPv6AddressFreeNum,
       "hwIPv6AddressConflictNum": hwIPv6AddressConflictNum,
       "hwIPv6AddressExcludeNum": hwIPv6AddressExcludeNum,
       "hwIPv6AddressUsedPercent": hwIPv6AddressUsedPercent,
       "hwIPv6NDRAPrefixTotalNum": hwIPv6NDRAPrefixTotalNum,
       "hwIPv6NDRAPrefixUsedNum": hwIPv6NDRAPrefixUsedNum,
       "hwIPv6NDRAPrefixFreeNum": hwIPv6NDRAPrefixFreeNum,
       "hwIPv6NDRAPrefixConflictNum": hwIPv6NDRAPrefixConflictNum,
       "hwIPv6NDRAPrefixExcludeNum": hwIPv6NDRAPrefixExcludeNum,
       "hwIPv6NDRAPrefixUsedPercent": hwIPv6NDRAPrefixUsedPercent,
       "hwIPv6PDPrefixTotalNum": hwIPv6PDPrefixTotalNum,
       "hwIPv6PDPrefixUsedNum": hwIPv6PDPrefixUsedNum,
       "hwIPv6PDPrefixFreeNum": hwIPv6PDPrefixFreeNum,
       "hwIPv6PDPrefixConflictNum": hwIPv6PDPrefixConflictNum,
       "hwIPv6PDPrefixExcludeNum": hwIPv6PDPrefixExcludeNum,
       "hwIPv6PDPrefixUsedPercent": hwIPv6PDPrefixUsedPercent,
       "hwIPv6DuidBindPrefixTable": hwIPv6DuidBindPrefixTable,
       "hwIPv6DuidBindPrefixEntry": hwIPv6DuidBindPrefixEntry,
       "hwIPv6ClientDuid": hwIPv6ClientDuid,
       "hwIPv6BindPrefix": hwIPv6BindPrefix,
       "hwIPv6DuidBindPrefixRowStatus": hwIPv6DuidBindPrefixRowStatus,
       "hwDhcpv6SvrGroupTable": hwDhcpv6SvrGroupTable,
       "hwDhcpv6SvrGroupEntry": hwDhcpv6SvrGroupEntry,
       "hwDhcpv6SvrGroupIndex": hwDhcpv6SvrGroupIndex,
       "hwDhcpv6SvrGroupName": hwDhcpv6SvrGroupName,
       "hwIPDhcpv6SvrAddr1": hwIPDhcpv6SvrAddr1,
       "hwIPDhcpv6SvrAddr2": hwIPDhcpv6SvrAddr2,
       "hwIPDhcpv6PriSvrState": hwIPDhcpv6PriSvrState,
       "hwIPDhcpv6ScdSvrState": hwIPDhcpv6ScdSvrState,
       "hwIPDhcpv6SvrAutoRelease": hwIPDhcpv6SvrAutoRelease,
       "hwIPDhcpv6SvrGroupRefCount": hwIPDhcpv6SvrGroupRefCount,
       "hwDhcpv6SvrInterface1": hwDhcpv6SvrInterface1,
       "hwDhcpv6SvrInterface2": hwDhcpv6SvrInterface2,
       "hwDhcpv6SvrAlgorithm": hwDhcpv6SvrAlgorithm,
       "hwDhcpv6SvrWeight1": hwDhcpv6SvrWeight1,
       "hwDhcpv6SvrWeight2": hwDhcpv6SvrWeight2,
       "hwIPDhcpv6Svr1VrfName": hwIPDhcpv6Svr1VrfName,
       "hwIPDhcpv6Svr2VrfName": hwIPDhcpv6Svr2VrfName,
       "hwDhcpv6SvrGroupRowStatus": hwDhcpv6SvrGroupRowStatus,
       "hwDhcpv6SvrSourceInterface": hwDhcpv6SvrSourceInterface,
       "hwIPv6RemotePoolTable": hwIPv6RemotePoolTable,
       "hwIPv6RemotePoolEntry": hwIPv6RemotePoolEntry,
       "hwIPv6RemotePoolIndex": hwIPv6RemotePoolIndex,
       "hwIPv6RemotePoolName": hwIPv6RemotePoolName,
       "hwIPv6RemotePoolPrefixName": hwIPv6RemotePoolPrefixName,
       "hwIPv6RemotePoolDhcpv6SvrGroupName": hwIPv6RemotePoolDhcpv6SvrGroupName,
       "hwIPv6RemotePoolAvailableStatus": hwIPv6RemotePoolAvailableStatus,
       "hwIPv6RemotePoolExportHostRouteFlag": hwIPv6RemotePoolExportHostRouteFlag,
       "hwIPv6RemotePoolRowStatus": hwIPv6RemotePoolRowStatus,
       "hwIPv6RemotePoolExportHostRouteIPv6Address": hwIPv6RemotePoolExportHostRouteIPv6Address,
       "hwIPv6RemotePoolExportHostRoutePDPrefix": hwIPv6RemotePoolExportHostRoutePDPrefix,
       "hwIPv6RemotePoolExportHostRouteNDPrefix": hwIPv6RemotePoolExportHostRouteNDPrefix,
       "hwIPv6RemotePoolWeight": hwIPv6RemotePoolWeight,
       "hwIPv6PoolStatistic": hwIPv6PoolStatistic,
       "hwIpv6PoolNum": hwIpv6PoolNum,
       "hwIpv6AddressIdleTotalNum": hwIpv6AddressIdleTotalNum,
       "hwIpv6PrefixIdleTotalNum": hwIpv6PrefixIdleTotalNum,
       "hwIpv6AddressUsedTotalNum": hwIpv6AddressUsedTotalNum,
       "hwIpv6PrefixUsedTotalNum": hwIpv6PrefixUsedTotalNum,
       "hwAllIPv6AddressTotalNum": hwAllIPv6AddressTotalNum,
       "hwAllIPv6AddressUsedNum": hwAllIPv6AddressUsedNum,
       "hwAllIPv6AddressIdleNum": hwAllIPv6AddressIdleNum,
       "hwAllIPv6ConflictAddressNum": hwAllIPv6ConflictAddressNum,
       "hwAllIPv6ExcludeAddressNum": hwAllIPv6ExcludeAddressNum,
       "hwAllIPv6AddressUsedPercent": hwAllIPv6AddressUsedPercent,
       "hwAllNDRAPrefixTotalNum": hwAllNDRAPrefixTotalNum,
       "hwAllNDRAPrefixUsedNum": hwAllNDRAPrefixUsedNum,
       "hwAllNDRAPrefixFreeNum": hwAllNDRAPrefixFreeNum,
       "hwAllNDRAPrefixConflictNum": hwAllNDRAPrefixConflictNum,
       "hwAllNDRAPrefixExcludeNum": hwAllNDRAPrefixExcludeNum,
       "hwAllNDRAPrefixUsedPercent": hwAllNDRAPrefixUsedPercent,
       "hwAllPDPrefixTotalNum": hwAllPDPrefixTotalNum,
       "hwAllPDPrefixUsedNum": hwAllPDPrefixUsedNum,
       "hwAllPDPrefixFreeNum": hwAllPDPrefixFreeNum,
       "hwAllPDPrefixConflictNum": hwAllPDPrefixConflictNum,
       "hwAllPDPrefixExcludeNum": hwAllPDPrefixExcludeNum,
       "hwAllPDPrefixUsedPercent": hwAllPDPrefixUsedPercent,
       "hwDhcpv6ServerTable": hwDhcpv6ServerTable,
       "hwDhcpv6ServerEntry": hwDhcpv6ServerEntry,
       "hwDhcpv6SvrIndex": hwDhcpv6SvrIndex,
       "hwDhcpv6ServerIP": hwDhcpv6ServerIP,
       "hwDhcpv6ServerVRFName": hwDhcpv6ServerVRFName,
       "hwDhcpv6ServerIfIndex": hwDhcpv6ServerIfIndex,
       "hwDhcpv6ServerState": hwDhcpv6ServerState,
       "hwDhcpv6ServerSendSolicitSpeedNum": hwDhcpv6ServerSendSolicitSpeedNum,
       "hwDhcpv6ServerSendSolicitSpeedSec": hwDhcpv6ServerSendSolicitSpeedSec,
       "hwIPV6AddressStatusTable": hwIPV6AddressStatusTable,
       "hwIPV6AddressStatusEntry": hwIPV6AddressStatusEntry,
       "hwIPv6Address": hwIPv6Address,
       "hwIPv6AddressStatus": hwIPv6AddressStatus,
       "hwIPv6LocalPrefixName": hwIPv6LocalPrefixName,
       "hwIPV6PrefixStatusTable": hwIPV6PrefixStatusTable,
       "hwIPV6PrefixStatusEntry": hwIPV6PrefixStatusEntry,
       "hwIpv6Prefix": hwIpv6Prefix,
       "hwIpv6PrefixLen": hwIpv6PrefixLen,
       "hwIPv6PrefixStatus": hwIPv6PrefixStatus,
       "hwIPv6DelegationPrefixName": hwIPv6DelegationPrefixName,
       "hwIPPoolConstantIndex": hwIPPoolConstantIndex,
       "hwIPPoolConstantIndexEnable": hwIPPoolConstantIndexEnable,
       "hwIPPoolSetting": hwIPPoolSetting,
       "hwIPPoolAlgorithm": hwIPPoolAlgorithm,
       "hwIPv6PoolAlgorithm": hwIPv6PoolAlgorithm,
       "hwIPPoolMibTrap": hwIPPoolMibTrap,
       "hwIPPoolTrapOid": hwIPPoolTrapOid,
       "hwUserIPAddress": hwUserIPAddress,
       "hwDHCPServerAddr": hwDHCPServerAddr,
       "hwDhcpSvrVrfName": hwDhcpSvrVrfName,
       "hwIPPoolGroupIndex": hwIPPoolGroupIndex,
       "hwDhcpSvrDownReason": hwDhcpSvrDownReason,
       "hwIPPoolDAPName": hwIPPoolDAPName,
       "hwIPPoolDAPReason": hwIPPoolDAPReason,
       "hwIPPoolTrapsDefine": hwIPPoolTrapsDefine,
       "hwIPPoolTraps": hwIPPoolTraps,
       "hwUserIPConflictAlarm": hwUserIPConflictAlarm,
       "hwUserIPLeaseAlarm": hwUserIPLeaseAlarm,
       "hwAllocUserIPFailAlarm": hwAllocUserIPFailAlarm,
       "hwDhcpServerDown": hwDhcpServerDown,
       "hwLocalIPPoolDifferWithServer": hwLocalIPPoolDifferWithServer,
       "hwUsedIPReachThreshold": hwUsedIPReachThreshold,
       "hwUsedIPReachThresholdResume": hwUsedIPReachThresholdResume,
       "hwUsedDeleteUnnumberedRouter": hwUsedDeleteUnnumberedRouter,
       "hwPoolGroupUsedIPReachThreshold": hwPoolGroupUsedIPReachThreshold,
       "hwPoolGroupUsedIPReachThresholdResume": hwPoolGroupUsedIPReachThresholdResume,
       "hwIPPoolConstantIndexFail": hwIPPoolConstantIndexFail,
       "hwIPv6PrefixConstantIndexFail": hwIPv6PrefixConstantIndexFail,
       "hwIPv6PoolConstantIndexFail": hwIPv6PoolConstantIndexFail,
       "hwUsedIPExhaust": hwUsedIPExhaust,
       "hwUsedIPExhaustResume": hwUsedIPExhaustResume,
       "hwPoolGroupUsedIPExhaust": hwPoolGroupUsedIPExhaust,
       "hwPoolGroupUsedIPExhaustResume": hwPoolGroupUsedIPExhaustResume,
       "hwUsedIPv6AddressAlarm": hwUsedIPv6AddressAlarm,
       "hwUsedIPv6AddressAlarmResume": hwUsedIPv6AddressAlarmResume,
       "hwIPv6AddressExhaustAlarm": hwIPv6AddressExhaustAlarm,
       "hwIPv6AddressExhaustAlarmResume": hwIPv6AddressExhaustAlarmResume,
       "hwIPPoolDAPApplyUnsuccessful": hwIPPoolDAPApplyUnsuccessful,
       "hwIPPoolDAPReleaseUnsuccessful": hwIPPoolDAPReleaseUnsuccessful,
       "hwIPPoolDAPSubnetFull": hwIPPoolDAPSubnetFull,
       "hwIPPoolDAPDeviceSubnetFull": hwIPPoolDAPDeviceSubnetFull,
       "hwIpPoolMIBConformance": hwIpPoolMIBConformance,
       "hwIpPoolCompliances": hwIpPoolCompliances,
       "hwIpPoolCompliance": hwIpPoolCompliance,
       "hwIpPoolObjectGroups": hwIpPoolObjectGroups,
       "hwIpPoolTableGroup": hwIpPoolTableGroup,
       "hwIpSectionTableGroup": hwIpSectionTableGroup,
       "hwIpPoolExtTableGroup": hwIpPoolExtTableGroup,
       "hwIpAddressStatusTableGroup": hwIpAddressStatusTableGroup,
       "hwDhcpSvrGroupTableGroup": hwDhcpSvrGroupTableGroup,
       "hwRemotePoolTableGroup": hwRemotePoolTableGroup,
       "hwIpPoolStatisticGroup": hwIpPoolStatisticGroup,
       "hwIpPoolTrapOidGroup": hwIpPoolTrapOidGroup,
       "hwIpPoolTrapsGroup": hwIpPoolTrapsGroup,
       "hwDhcpServerTableGroup": hwDhcpServerTableGroup,
       "hwIPPoolOptionTableGroup": hwIPPoolOptionTableGroup,
       "hwIPPoolGroupTableGroup": hwIPPoolGroupTableGroup,
       "hwIPPoolGroupExtTableGroup": hwIPPoolGroupExtTableGroup,
       "hwIPPoolGroupDisplayTableGroup": hwIPPoolGroupDisplayTableGroup,
       "hwIPPoolDomainSearchListGroup": hwIPPoolDomainSearchListGroup,
       "hwIPPoolOptionExtTableGroup": hwIPPoolOptionExtTableGroup,
       "hwIPPoolReplyOptionGroup": hwIPPoolReplyOptionGroup,
       "hwIPv6PrefixTableGroup": hwIPv6PrefixTableGroup,
       "hwIPv6PoolTableGroup": hwIPv6PoolTableGroup,
       "hwIPv6PoolStatusTableGroup": hwIPv6PoolStatusTableGroup,
       "hwIPv6DuidBindPrefixTableGroup": hwIPv6DuidBindPrefixTableGroup,
       "hwDhcpv6SvrGroupTableGroup": hwDhcpv6SvrGroupTableGroup,
       "hwIPv6RemotePoolTableGroup": hwIPv6RemotePoolTableGroup,
       "hwIPv6PoolStatisticGroup": hwIPv6PoolStatisticGroup,
       "hwIPV6AddressStatusTableGroup": hwIPV6AddressStatusTableGroup,
       "hwIPV6PrefixStatusTableGroup": hwIPV6PrefixStatusTableGroup,
       "hwIPPoolConstantIndexGroup": hwIPPoolConstantIndexGroup}
)
