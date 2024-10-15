# SNMP MIB module (HUAWEI-LI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:33 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwLiMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131)
)
hwLiMib.setRevisions(
        ("2007-06-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWLiDscp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



# MIB Managed Objects in the order of their OIDs

_HwLiMibNotifs_ObjectIdentity = ObjectIdentity
hwLiMibNotifs = _HwLiMibNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 1)
)
_HwLiMibObjects_ObjectIdentity = ObjectIdentity
hwLiMibObjects = _HwLiMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2)
)
_HwLiAgentObjects_ObjectIdentity = ObjectIdentity
hwLiAgentObjects = _HwLiAgentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1)
)
_HwLiAgentTime_Type = DateAndTime
_HwLiAgentTime_Object = MibScalar
hwLiAgentTime = _HwLiAgentTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 1),
    _HwLiAgentTime_Type()
)
hwLiAgentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLiAgentTime.setStatus("current")


class _HwLiAgentEnable_Type(Integer32):
    """Custom type hwLiAgentEnable based on Integer32"""
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


_HwLiAgentEnable_Type.__name__ = "Integer32"
_HwLiAgentEnable_Object = MibScalar
hwLiAgentEnable = _HwLiAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 2),
    _HwLiAgentEnable_Type()
)
hwLiAgentEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLiAgentEnable.setStatus("current")
_HwLiAgentX2IpAddress_Type = InetAddress
_HwLiAgentX2IpAddress_Object = MibScalar
hwLiAgentX2IpAddress = _HwLiAgentX2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 3),
    _HwLiAgentX2IpAddress_Type()
)
hwLiAgentX2IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLiAgentX2IpAddress.setStatus("current")
_HwLiAgentX2Port_Type = InetPortNumber
_HwLiAgentX2Port_Object = MibScalar
hwLiAgentX2Port = _HwLiAgentX2Port_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 4),
    _HwLiAgentX2Port_Type()
)
hwLiAgentX2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLiAgentX2Port.setStatus("current")
_HwLiAgentX3IpAddress_Type = InetAddress
_HwLiAgentX3IpAddress_Object = MibScalar
hwLiAgentX3IpAddress = _HwLiAgentX3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 5),
    _HwLiAgentX3IpAddress_Type()
)
hwLiAgentX3IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLiAgentX3IpAddress.setStatus("current")
_HwLiAgentX3Port_Type = InetPortNumber
_HwLiAgentX3Port_Object = MibScalar
hwLiAgentX3Port = _HwLiAgentX3Port_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 1, 6),
    _HwLiAgentX3Port_Type()
)
hwLiAgentX3Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLiAgentX3Port.setStatus("current")
_HwLiGatewayGroup_ObjectIdentity = ObjectIdentity
hwLiGatewayGroup = _HwLiGatewayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3)
)


class _HwLiGatewayNewIndex_Type(Integer32):
    """Custom type hwLiGatewayNewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_HwLiGatewayNewIndex_Type.__name__ = "Integer32"
_HwLiGatewayNewIndex_Object = MibScalar
hwLiGatewayNewIndex = _HwLiGatewayNewIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 1),
    _HwLiGatewayNewIndex_Type()
)
hwLiGatewayNewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLiGatewayNewIndex.setStatus("current")
_HwLiGatewayTable_Object = MibTable
hwLiGatewayTable = _HwLiGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hwLiGatewayTable.setStatus("current")
_HwLiGatewayEntry_Object = MibTableRow
hwLiGatewayEntry = _HwLiGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1)
)
hwLiGatewayEntry.setIndexNames(
    (0, "HUAWEI-LI-MIB", "hwLiGatewayIndex"),
)
if mibBuilder.loadTexts:
    hwLiGatewayEntry.setStatus("current")


class _HwLiGatewayIndex_Type(Integer32):
    """Custom type hwLiGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwLiGatewayIndex_Type.__name__ = "Integer32"
_HwLiGatewayIndex_Object = MibTableColumn
hwLiGatewayIndex = _HwLiGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 1),
    _HwLiGatewayIndex_Type()
)
hwLiGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLiGatewayIndex.setStatus("current")


class _HwLiGatewayAddressType_Type(InetAddressType):
    """Custom type hwLiGatewayAddressType based on InetAddressType"""


_HwLiGatewayAddressType_Object = MibTableColumn
hwLiGatewayAddressType = _HwLiGatewayAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 2),
    _HwLiGatewayAddressType_Type()
)
hwLiGatewayAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayAddressType.setStatus("current")


class _HwLiGatewayX2Protocol_Type(Integer32):
    """Custom type hwLiGatewayX2Protocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )


_HwLiGatewayX2Protocol_Type.__name__ = "Integer32"
_HwLiGatewayX2Protocol_Object = MibTableColumn
hwLiGatewayX2Protocol = _HwLiGatewayX2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 3),
    _HwLiGatewayX2Protocol_Type()
)
hwLiGatewayX2Protocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX2Protocol.setStatus("current")
_HwLiGatewayX2Address_Type = InetAddress
_HwLiGatewayX2Address_Object = MibTableColumn
hwLiGatewayX2Address = _HwLiGatewayX2Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 4),
    _HwLiGatewayX2Address_Type()
)
hwLiGatewayX2Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX2Address.setStatus("current")
_HwLiGatewayX2Port_Type = InetPortNumber
_HwLiGatewayX2Port_Object = MibTableColumn
hwLiGatewayX2Port = _HwLiGatewayX2Port_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 5),
    _HwLiGatewayX2Port_Type()
)
hwLiGatewayX2Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX2Port.setStatus("current")


class _HwLiGatewayX3Protocol_Type(Integer32):
    """Custom type hwLiGatewayX3Protocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )


_HwLiGatewayX3Protocol_Type.__name__ = "Integer32"
_HwLiGatewayX3Protocol_Object = MibTableColumn
hwLiGatewayX3Protocol = _HwLiGatewayX3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 6),
    _HwLiGatewayX3Protocol_Type()
)
hwLiGatewayX3Protocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX3Protocol.setStatus("current")
_HwLiGatewayX3Address_Type = InetAddress
_HwLiGatewayX3Address_Object = MibTableColumn
hwLiGatewayX3Address = _HwLiGatewayX3Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 7),
    _HwLiGatewayX3Address_Type()
)
hwLiGatewayX3Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX3Address.setStatus("current")
_HwLiGatewayX3Port_Type = InetPortNumber
_HwLiGatewayX3Port_Object = MibTableColumn
hwLiGatewayX3Port = _HwLiGatewayX3Port_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 8),
    _HwLiGatewayX3Port_Type()
)
hwLiGatewayX3Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX3Port.setStatus("current")


class _HwLiGatewayX3HeartBeatTimer_Type(Integer32):
    """Custom type hwLiGatewayX3HeartBeatTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwLiGatewayX3HeartBeatTimer_Type.__name__ = "Integer32"
_HwLiGatewayX3HeartBeatTimer_Object = MibTableColumn
hwLiGatewayX3HeartBeatTimer = _HwLiGatewayX3HeartBeatTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 9),
    _HwLiGatewayX3HeartBeatTimer_Type()
)
hwLiGatewayX3HeartBeatTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX3HeartBeatTimer.setStatus("current")


class _HwLiGatewayX3NoResponseNum_Type(Integer32):
    """Custom type hwLiGatewayX3NoResponseNum based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_HwLiGatewayX3NoResponseNum_Type.__name__ = "Integer32"
_HwLiGatewayX3NoResponseNum_Object = MibTableColumn
hwLiGatewayX3NoResponseNum = _HwLiGatewayX3NoResponseNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 10),
    _HwLiGatewayX3NoResponseNum_Type()
)
hwLiGatewayX3NoResponseNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX3NoResponseNum.setStatus("current")


class _HwLiGatewayX3OperateStatus_Type(Integer32):
    """Custom type hwLiGatewayX3OperateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 3),
          ("noHeartBeat", 2),
          ("normal", 1))
    )


_HwLiGatewayX3OperateStatus_Type.__name__ = "Integer32"
_HwLiGatewayX3OperateStatus_Object = MibTableColumn
hwLiGatewayX3OperateStatus = _HwLiGatewayX3OperateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 11),
    _HwLiGatewayX3OperateStatus_Type()
)
hwLiGatewayX3OperateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLiGatewayX3OperateStatus.setStatus("current")


class _HwLiGatewayX3Dscp_Type(HWLiDscp):
    """Custom type hwLiGatewayX3Dscp based on HWLiDscp"""
    defaultValue = 0


_HwLiGatewayX3Dscp_Object = MibTableColumn
hwLiGatewayX3Dscp = _HwLiGatewayX3Dscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 12),
    _HwLiGatewayX3Dscp_Type()
)
hwLiGatewayX3Dscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX3Dscp.setStatus("current")
_HwLiGatewayRowStatus_Type = RowStatus
_HwLiGatewayRowStatus_Object = MibTableColumn
hwLiGatewayRowStatus = _HwLiGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 14),
    _HwLiGatewayRowStatus_Type()
)
hwLiGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayRowStatus.setStatus("current")


class _HwLiGatewayX3AddressType_Type(InetAddressType):
    """Custom type hwLiGatewayX3AddressType based on InetAddressType"""


_HwLiGatewayX3AddressType_Object = MibTableColumn
hwLiGatewayX3AddressType = _HwLiGatewayX3AddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 15),
    _HwLiGatewayX3AddressType_Type()
)
hwLiGatewayX3AddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX3AddressType.setStatus("current")


class _HwLiGatewayX2AddressType_Type(InetAddressType):
    """Custom type hwLiGatewayX2AddressType based on InetAddressType"""


_HwLiGatewayX2AddressType_Object = MibTableColumn
hwLiGatewayX2AddressType = _HwLiGatewayX2AddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 2, 1, 16),
    _HwLiGatewayX2AddressType_Type()
)
hwLiGatewayX2AddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiGatewayX2AddressType.setStatus("current")


class _HwLiGatewayCapabilities_Type(Bits):
    """Custom type hwLiGatewayCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("ipv4SrcInterface", 0),
          ("ipv6SrcInterface", 1),
          ("tcp", 3),
          ("udp", 2))
    )

_HwLiGatewayCapabilities_Type.__name__ = "Bits"
_HwLiGatewayCapabilities_Object = MibScalar
hwLiGatewayCapabilities = _HwLiGatewayCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 3, 3),
    _HwLiGatewayCapabilities_Type()
)
hwLiGatewayCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLiGatewayCapabilities.setStatus("current")
_HwLiStreamGroup_ObjectIdentity = ObjectIdentity
hwLiStreamGroup = _HwLiStreamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4)
)
_HwLiStreamTable_Object = MibTable
hwLiStreamTable = _HwLiStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2)
)
if mibBuilder.loadTexts:
    hwLiStreamTable.setStatus("current")
_HwLiStreamEntry_Object = MibTableRow
hwLiStreamEntry = _HwLiStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1)
)
hwLiStreamEntry.setIndexNames(
    (0, "HUAWEI-LI-MIB", "hwLiGatewayIndex"),
    (0, "HUAWEI-LI-MIB", "hwLiStreamIndex"),
)
if mibBuilder.loadTexts:
    hwLiStreamEntry.setStatus("current")


class _HwLiStreamIndex_Type(Integer32):
    """Custom type hwLiStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_HwLiStreamIndex_Type.__name__ = "Integer32"
_HwLiStreamIndex_Object = MibTableColumn
hwLiStreamIndex = _HwLiStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 1),
    _HwLiStreamIndex_Type()
)
hwLiStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLiStreamIndex.setStatus("current")
_HwLiStreamLiId_Type = Unsigned32
_HwLiStreamLiId_Object = MibTableColumn
hwLiStreamLiId = _HwLiStreamLiId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 2),
    _HwLiStreamLiId_Type()
)
hwLiStreamLiId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamLiId.setStatus("current")


class _HwLiStreamActivationType_Type(Integer32):
    """Custom type hwLiStreamActivationType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("cc", 2),
          ("iri", 1))
    )


_HwLiStreamActivationType_Type.__name__ = "Integer32"
_HwLiStreamActivationType_Object = MibTableColumn
hwLiStreamActivationType = _HwLiStreamActivationType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 3),
    _HwLiStreamActivationType_Type()
)
hwLiStreamActivationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamActivationType.setStatus("current")


class _HwLiStreamSessionId_Type(Integer32):
    """Custom type hwLiStreamSessionId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwLiStreamSessionId_Type.__name__ = "Integer32"
_HwLiStreamSessionId_Object = MibTableColumn
hwLiStreamSessionId = _HwLiStreamSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 4),
    _HwLiStreamSessionId_Type()
)
hwLiStreamSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamSessionId.setStatus("current")


class _HwLiStreamTargetIdType_Type(Integer32):
    """Custom type hwLiStreamTargetIdType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biDirection", 2),
          ("oneDirection", 1))
    )


_HwLiStreamTargetIdType_Type.__name__ = "Integer32"
_HwLiStreamTargetIdType_Object = MibTableColumn
hwLiStreamTargetIdType = _HwLiStreamTargetIdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 5),
    _HwLiStreamTargetIdType_Type()
)
hwLiStreamTargetIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamTargetIdType.setStatus("current")
_HwLiStreamSrcMacAddress_Type = MacAddress
_HwLiStreamSrcMacAddress_Object = MibTableColumn
hwLiStreamSrcMacAddress = _HwLiStreamSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 7),
    _HwLiStreamSrcMacAddress_Type()
)
hwLiStreamSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamSrcMacAddress.setStatus("current")
_HwLiStreamDstMacAddress_Type = MacAddress
_HwLiStreamDstMacAddress_Object = MibTableColumn
hwLiStreamDstMacAddress = _HwLiStreamDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 8),
    _HwLiStreamDstMacAddress_Type()
)
hwLiStreamDstMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamDstMacAddress.setStatus("current")


class _HwLiStreamSrcIpAddress_Type(InetAddress):
    """Custom type hwLiStreamSrcIpAddress based on InetAddress"""
    defaultHexValue = "00000000"


_HwLiStreamSrcIpAddress_Object = MibTableColumn
hwLiStreamSrcIpAddress = _HwLiStreamSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 9),
    _HwLiStreamSrcIpAddress_Type()
)
hwLiStreamSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamSrcIpAddress.setStatus("current")


class _HwLiStreamSrcIpLength_Type(InetAddressPrefixLength):
    """Custom type hwLiStreamSrcIpLength based on InetAddressPrefixLength"""
    defaultValue = 32


_HwLiStreamSrcIpLength_Object = MibTableColumn
hwLiStreamSrcIpLength = _HwLiStreamSrcIpLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 10),
    _HwLiStreamSrcIpLength_Type()
)
hwLiStreamSrcIpLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamSrcIpLength.setStatus("current")


class _HwLiStreamDstIpAddress_Type(InetAddress):
    """Custom type hwLiStreamDstIpAddress based on InetAddress"""
    defaultHexValue = "00000000"


_HwLiStreamDstIpAddress_Object = MibTableColumn
hwLiStreamDstIpAddress = _HwLiStreamDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 11),
    _HwLiStreamDstIpAddress_Type()
)
hwLiStreamDstIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamDstIpAddress.setStatus("current")


class _HwLiStreamDstIpLength_Type(InetAddressPrefixLength):
    """Custom type hwLiStreamDstIpLength based on InetAddressPrefixLength"""
    defaultValue = 32


_HwLiStreamDstIpLength_Object = MibTableColumn
hwLiStreamDstIpLength = _HwLiStreamDstIpLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 12),
    _HwLiStreamDstIpLength_Type()
)
hwLiStreamDstIpLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamDstIpLength.setStatus("current")


class _HwLiStreamProtocol_Type(Integer32):
    """Custom type hwLiStreamProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwLiStreamProtocol_Type.__name__ = "Integer32"
_HwLiStreamProtocol_Object = MibTableColumn
hwLiStreamProtocol = _HwLiStreamProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 13),
    _HwLiStreamProtocol_Type()
)
hwLiStreamProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamProtocol.setStatus("current")


class _HwLiStreamSrcPort_Type(InetPortNumber):
    """Custom type hwLiStreamSrcPort based on InetPortNumber"""
    defaultValue = 0


_HwLiStreamSrcPort_Object = MibTableColumn
hwLiStreamSrcPort = _HwLiStreamSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 14),
    _HwLiStreamSrcPort_Type()
)
hwLiStreamSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamSrcPort.setStatus("current")


class _HwLiStreamDstPort_Type(InetPortNumber):
    """Custom type hwLiStreamDstPort based on InetPortNumber"""
    defaultValue = 0


_HwLiStreamDstPort_Object = MibTableColumn
hwLiStreamDstPort = _HwLiStreamDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 15),
    _HwLiStreamDstPort_Type()
)
hwLiStreamDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamDstPort.setStatus("current")


class _HwLiStreamIfIndex_Type(Integer32):
    """Custom type hwLiStreamIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwLiStreamIfIndex_Type.__name__ = "Integer32"
_HwLiStreamIfIndex_Object = MibTableColumn
hwLiStreamIfIndex = _HwLiStreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 16),
    _HwLiStreamIfIndex_Type()
)
hwLiStreamIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamIfIndex.setStatus("current")
_HwLiStreamUserName_Type = OctetString
_HwLiStreamUserName_Object = MibTableColumn
hwLiStreamUserName = _HwLiStreamUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 17),
    _HwLiStreamUserName_Type()
)
hwLiStreamUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamUserName.setStatus("current")
_HwLiStreamRowStatus_Type = RowStatus
_HwLiStreamRowStatus_Object = MibTableColumn
hwLiStreamRowStatus = _HwLiStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 18),
    _HwLiStreamRowStatus_Type()
)
hwLiStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamRowStatus.setStatus("current")


class _HwLiStreamSrcIpAddressType_Type(InetAddressType):
    """Custom type hwLiStreamSrcIpAddressType based on InetAddressType"""


_HwLiStreamSrcIpAddressType_Object = MibTableColumn
hwLiStreamSrcIpAddressType = _HwLiStreamSrcIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 19),
    _HwLiStreamSrcIpAddressType_Type()
)
hwLiStreamSrcIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamSrcIpAddressType.setStatus("current")


class _HwLiStreamDstIpAddressType_Type(InetAddressType):
    """Custom type hwLiStreamDstIpAddressType based on InetAddressType"""


_HwLiStreamDstIpAddressType_Object = MibTableColumn
hwLiStreamDstIpAddressType = _HwLiStreamDstIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 20),
    _HwLiStreamDstIpAddressType_Type()
)
hwLiStreamDstIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamDstIpAddressType.setStatus("current")
_HwLiStreamSrcVpnName_Type = OctetString
_HwLiStreamSrcVpnName_Object = MibTableColumn
hwLiStreamSrcVpnName = _HwLiStreamSrcVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 21),
    _HwLiStreamSrcVpnName_Type()
)
hwLiStreamSrcVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamSrcVpnName.setStatus("current")
_HwLiStreamDstVpnName_Type = OctetString
_HwLiStreamDstVpnName_Object = MibTableColumn
hwLiStreamDstVpnName = _HwLiStreamDstVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 22),
    _HwLiStreamDstVpnName_Type()
)
hwLiStreamDstVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamDstVpnName.setStatus("current")


class _HwLiStreamL2tpIfIndex_Type(Integer32):
    """Custom type hwLiStreamL2tpIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwLiStreamL2tpIfIndex_Type.__name__ = "Integer32"
_HwLiStreamL2tpIfIndex_Object = MibTableColumn
hwLiStreamL2tpIfIndex = _HwLiStreamL2tpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 23),
    _HwLiStreamL2tpIfIndex_Type()
)
hwLiStreamL2tpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamL2tpIfIndex.setStatus("current")


class _HwLiStreamL2tpVlanId_Type(Integer32):
    """Custom type hwLiStreamL2tpVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwLiStreamL2tpVlanId_Type.__name__ = "Integer32"
_HwLiStreamL2tpVlanId_Object = MibTableColumn
hwLiStreamL2tpVlanId = _HwLiStreamL2tpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 24),
    _HwLiStreamL2tpVlanId_Type()
)
hwLiStreamL2tpVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamL2tpVlanId.setStatus("current")
_HwLiStreamAcctSessionId_Type = OctetString
_HwLiStreamAcctSessionId_Object = MibTableColumn
hwLiStreamAcctSessionId = _HwLiStreamAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 2, 4, 2, 1, 25),
    _HwLiStreamAcctSessionId_Type()
)
hwLiStreamAcctSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLiStreamAcctSessionId.setStatus("current")
_HwLiMibConform_ObjectIdentity = ObjectIdentity
hwLiMibConform = _HwLiMibConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3)
)
_HwLiMibCompliances_ObjectIdentity = ObjectIdentity
hwLiMibCompliances = _HwLiMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 2)
)
_HwLiMibGroups_ObjectIdentity = ObjectIdentity
hwLiMibGroups = _HwLiMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3)
)

# Managed Objects groups

hwLiAgentComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3, 1)
)
hwLiAgentComplianceGroup.setObjects(
      *(("HUAWEI-LI-MIB", "hwLiAgentTime"),
        ("HUAWEI-LI-MIB", "hwLiAgentEnable"),
        ("HUAWEI-LI-MIB", "hwLiAgentX2IpAddress"),
        ("HUAWEI-LI-MIB", "hwLiAgentX2Port"),
        ("HUAWEI-LI-MIB", "hwLiAgentX3IpAddress"),
        ("HUAWEI-LI-MIB", "hwLiAgentX3Port"))
)
if mibBuilder.loadTexts:
    hwLiAgentComplianceGroup.setStatus("current")

hwLiGatewayComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3, 2)
)
hwLiGatewayComplianceGroup.setObjects(
      *(("HUAWEI-LI-MIB", "hwLiGatewayNewIndex"),
        ("HUAWEI-LI-MIB", "hwLiGatewayAddressType"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX2Protocol"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX2Address"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX2Port"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX3Protocol"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX3Address"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX3Port"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX3HeartBeatTimer"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX3NoResponseNum"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX3OperateStatus"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX3Dscp"),
        ("HUAWEI-LI-MIB", "hwLiGatewayRowStatus"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX3AddressType"),
        ("HUAWEI-LI-MIB", "hwLiGatewayX2AddressType"))
)
if mibBuilder.loadTexts:
    hwLiGatewayComplianceGroup.setStatus("current")

hwLiStreamComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3, 3)
)
hwLiStreamComplianceGroup.setObjects(
      *(("HUAWEI-LI-MIB", "hwLiStreamLiId"),
        ("HUAWEI-LI-MIB", "hwLiStreamActivationType"),
        ("HUAWEI-LI-MIB", "hwLiStreamSessionId"),
        ("HUAWEI-LI-MIB", "hwLiStreamTargetIdType"),
        ("HUAWEI-LI-MIB", "hwLiStreamProtocol"),
        ("HUAWEI-LI-MIB", "hwLiStreamSrcPort"),
        ("HUAWEI-LI-MIB", "hwLiStreamDstPort"),
        ("HUAWEI-LI-MIB", "hwLiStreamSrcMacAddress"),
        ("HUAWEI-LI-MIB", "hwLiStreamDstMacAddress"),
        ("HUAWEI-LI-MIB", "hwLiStreamSrcIpAddress"),
        ("HUAWEI-LI-MIB", "hwLiStreamSrcIpLength"),
        ("HUAWEI-LI-MIB", "hwLiStreamDstIpAddress"),
        ("HUAWEI-LI-MIB", "hwLiStreamDstIpLength"),
        ("HUAWEI-LI-MIB", "hwLiStreamIfIndex"),
        ("HUAWEI-LI-MIB", "hwLiStreamUserName"),
        ("HUAWEI-LI-MIB", "hwLiStreamRowStatus"),
        ("HUAWEI-LI-MIB", "hwLiStreamSrcIpAddressType"),
        ("HUAWEI-LI-MIB", "hwLiStreamDstIpAddressType"),
        ("HUAWEI-LI-MIB", "hwLiStreamSrcVpnName"),
        ("HUAWEI-LI-MIB", "hwLiStreamDstVpnName"),
        ("HUAWEI-LI-MIB", "hwLiStreamL2tpIfIndex"),
        ("HUAWEI-LI-MIB", "hwLiStreamL2tpVlanId"),
        ("HUAWEI-LI-MIB", "hwLiStreamAcctSessionId"))
)
if mibBuilder.loadTexts:
    hwLiStreamComplianceGroup.setStatus("current")

hwLiGatewayCpbComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3, 5)
)
hwLiGatewayCpbComplianceGroup.setObjects(
    ("HUAWEI-LI-MIB", "hwLiGatewayCapabilities")
)
if mibBuilder.loadTexts:
    hwLiGatewayCpbComplianceGroup.setStatus("current")


# Notification objects

hwLiMibActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 1, 1)
)
if mibBuilder.loadTexts:
    hwLiMibActive.setStatus(
        "current"
    )

hwLiX3HeartBeatAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 1, 2)
)
hwLiX3HeartBeatAlarm.setObjects(
    ("HUAWEI-LI-MIB", "hwLiGatewayX3Address")
)
if mibBuilder.loadTexts:
    hwLiX3HeartBeatAlarm.setStatus(
        "current"
    )

hwLiX3HeartBeatRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 1, 3)
)
hwLiX3HeartBeatRecover.setObjects(
    ("HUAWEI-LI-MIB", "hwLiGatewayX3Address")
)
if mibBuilder.loadTexts:
    hwLiX3HeartBeatRecover.setStatus(
        "current"
    )


# Notifications groups

hwLiNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 3, 4)
)
hwLiNotificationGroup.setObjects(
      *(("HUAWEI-LI-MIB", "hwLiMibActive"),
        ("HUAWEI-LI-MIB", "hwLiX3HeartBeatAlarm"),
        ("HUAWEI-LI-MIB", "hwLiX3HeartBeatRecover"))
)
if mibBuilder.loadTexts:
    hwLiNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwLiMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 131, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwLiMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LI-MIB",
    **{"HWLiDscp": HWLiDscp,
       "hwLiMib": hwLiMib,
       "hwLiMibNotifs": hwLiMibNotifs,
       "hwLiMibActive": hwLiMibActive,
       "hwLiX3HeartBeatAlarm": hwLiX3HeartBeatAlarm,
       "hwLiX3HeartBeatRecover": hwLiX3HeartBeatRecover,
       "hwLiMibObjects": hwLiMibObjects,
       "hwLiAgentObjects": hwLiAgentObjects,
       "hwLiAgentTime": hwLiAgentTime,
       "hwLiAgentEnable": hwLiAgentEnable,
       "hwLiAgentX2IpAddress": hwLiAgentX2IpAddress,
       "hwLiAgentX2Port": hwLiAgentX2Port,
       "hwLiAgentX3IpAddress": hwLiAgentX3IpAddress,
       "hwLiAgentX3Port": hwLiAgentX3Port,
       "hwLiGatewayGroup": hwLiGatewayGroup,
       "hwLiGatewayNewIndex": hwLiGatewayNewIndex,
       "hwLiGatewayTable": hwLiGatewayTable,
       "hwLiGatewayEntry": hwLiGatewayEntry,
       "hwLiGatewayIndex": hwLiGatewayIndex,
       "hwLiGatewayAddressType": hwLiGatewayAddressType,
       "hwLiGatewayX2Protocol": hwLiGatewayX2Protocol,
       "hwLiGatewayX2Address": hwLiGatewayX2Address,
       "hwLiGatewayX2Port": hwLiGatewayX2Port,
       "hwLiGatewayX3Protocol": hwLiGatewayX3Protocol,
       "hwLiGatewayX3Address": hwLiGatewayX3Address,
       "hwLiGatewayX3Port": hwLiGatewayX3Port,
       "hwLiGatewayX3HeartBeatTimer": hwLiGatewayX3HeartBeatTimer,
       "hwLiGatewayX3NoResponseNum": hwLiGatewayX3NoResponseNum,
       "hwLiGatewayX3OperateStatus": hwLiGatewayX3OperateStatus,
       "hwLiGatewayX3Dscp": hwLiGatewayX3Dscp,
       "hwLiGatewayRowStatus": hwLiGatewayRowStatus,
       "hwLiGatewayX3AddressType": hwLiGatewayX3AddressType,
       "hwLiGatewayX2AddressType": hwLiGatewayX2AddressType,
       "hwLiGatewayCapabilities": hwLiGatewayCapabilities,
       "hwLiStreamGroup": hwLiStreamGroup,
       "hwLiStreamTable": hwLiStreamTable,
       "hwLiStreamEntry": hwLiStreamEntry,
       "hwLiStreamIndex": hwLiStreamIndex,
       "hwLiStreamLiId": hwLiStreamLiId,
       "hwLiStreamActivationType": hwLiStreamActivationType,
       "hwLiStreamSessionId": hwLiStreamSessionId,
       "hwLiStreamTargetIdType": hwLiStreamTargetIdType,
       "hwLiStreamSrcMacAddress": hwLiStreamSrcMacAddress,
       "hwLiStreamDstMacAddress": hwLiStreamDstMacAddress,
       "hwLiStreamSrcIpAddress": hwLiStreamSrcIpAddress,
       "hwLiStreamSrcIpLength": hwLiStreamSrcIpLength,
       "hwLiStreamDstIpAddress": hwLiStreamDstIpAddress,
       "hwLiStreamDstIpLength": hwLiStreamDstIpLength,
       "hwLiStreamProtocol": hwLiStreamProtocol,
       "hwLiStreamSrcPort": hwLiStreamSrcPort,
       "hwLiStreamDstPort": hwLiStreamDstPort,
       "hwLiStreamIfIndex": hwLiStreamIfIndex,
       "hwLiStreamUserName": hwLiStreamUserName,
       "hwLiStreamRowStatus": hwLiStreamRowStatus,
       "hwLiStreamSrcIpAddressType": hwLiStreamSrcIpAddressType,
       "hwLiStreamDstIpAddressType": hwLiStreamDstIpAddressType,
       "hwLiStreamSrcVpnName": hwLiStreamSrcVpnName,
       "hwLiStreamDstVpnName": hwLiStreamDstVpnName,
       "hwLiStreamL2tpIfIndex": hwLiStreamL2tpIfIndex,
       "hwLiStreamL2tpVlanId": hwLiStreamL2tpVlanId,
       "hwLiStreamAcctSessionId": hwLiStreamAcctSessionId,
       "hwLiMibConform": hwLiMibConform,
       "hwLiMibCompliances": hwLiMibCompliances,
       "hwLiMibCompliance": hwLiMibCompliance,
       "hwLiMibGroups": hwLiMibGroups,
       "hwLiAgentComplianceGroup": hwLiAgentComplianceGroup,
       "hwLiGatewayComplianceGroup": hwLiGatewayComplianceGroup,
       "hwLiStreamComplianceGroup": hwLiStreamComplianceGroup,
       "hwLiNotificationGroup": hwLiNotificationGroup,
       "hwLiGatewayCpbComplianceGroup": hwLiGatewayCpbComplianceGroup}
)
