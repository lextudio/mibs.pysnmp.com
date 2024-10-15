# SNMP MIB module (CADANT-CMTS-DHCPRA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-DHCPRA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:25 2024
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

(cadIfUpChannelCardNumber,
 cadIfUpChannelId) = mibBuilder.importSymbols(
    "CADANT-CMTS-UPCHANNEL-MIB",
    "cadIfUpChannelCardNumber",
    "cadIfUpChannelId")

(cadLayer3,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadLayer3")

(CadBridgePortType,
 CadCpeDeviceTypes,
 InetAddressIPv4or6) = mibBuilder.importSymbols(
    "CADANT-TC",
    "CadBridgePortType",
    "CadCpeDeviceTypes",
    "InetAddressIPv4or6")

(cadVrInterfaceIfIndex,) = mibBuilder.importSymbols(
    "CADANT-VIRTUAL-ROUTER-MIB",
    "cadVrInterfaceIfIndex")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadDhcpRaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6)
)
cadDhcpRaMib.setRevisions(
        ("2015-04-22 00:00",
         "2014-09-16 00:00",
         "2013-10-17 00:00",
         "2011-11-16 00:00",
         "2011-10-27 00:00",
         "2011-07-05 00:00",
         "2010-11-01 00:00",
         "2010-10-19 00:00",
         "2010-04-22 00:00",
         "2010-04-15 00:00",
         "2010-03-09 00:00",
         "2010-03-05 00:00",
         "2009-11-04 00:00",
         "2009-10-01 00:00",
         "2009-09-21 00:00",
         "2009-09-17 00:00",
         "2009-08-27 00:00",
         "2006-12-06 00:00",
         "2006-11-22 00:00",
         "2006-10-18 00:00",
         "2006-08-22 00:00",
         "2006-01-27 00:00",
         "2004-01-18 00:00",
         "2003-08-18 00:00",
         "2003-07-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CadDhcpRelayAgentOptionType(Integer32, TextualConvention):
    status = "current"
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
        *(("mac-ifindex", 1),
          ("octet-string-hex", 4),
          ("octet-string-text", 3),
          ("us-ifindex", 2))
    )



class CadDhcpPDPreActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 0),
          ("restore", 2))
    )



class CadDhcpPDPreActionDataType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("cableMacInterface", 2),
          ("prefixOrIp", 1))
    )



class CadDhcpRaOptionMSOTextType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostname", 2),
          ("octet-string-text", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CadVrDhcpServerTable_Object = MibTable
cadVrDhcpServerTable = _CadVrDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4)
)
if mibBuilder.loadTexts:
    cadVrDhcpServerTable.setStatus("current")
_CadVrDhcpServerEntry_Object = MibTableRow
cadVrDhcpServerEntry = _CadVrDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4, 1)
)
cadVrDhcpServerEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrInterfaceIfIndex"),
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpServerIPAddress"),
)
if mibBuilder.loadTexts:
    cadVrDhcpServerEntry.setStatus("current")
_CadVrDhcpServerIPAddress_Type = InetAddressIPv4or6
_CadVrDhcpServerIPAddress_Object = MibTableColumn
cadVrDhcpServerIPAddress = _CadVrDhcpServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4, 1, 1),
    _CadVrDhcpServerIPAddress_Type()
)
cadVrDhcpServerIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpServerIPAddress.setStatus("current")
_CadVrDhcpServerRowStatus_Type = RowStatus
_CadVrDhcpServerRowStatus_Object = MibTableColumn
cadVrDhcpServerRowStatus = _CadVrDhcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4, 1, 3),
    _CadVrDhcpServerRowStatus_Type()
)
cadVrDhcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrDhcpServerRowStatus.setStatus("current")


class _CadVrDhcpServerIPAddressType_Type(InetAddressType):
    """Custom type cadVrDhcpServerIPAddressType based on InetAddressType"""


_CadVrDhcpServerIPAddressType_Object = MibTableColumn
cadVrDhcpServerIPAddressType = _CadVrDhcpServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4, 1, 4),
    _CadVrDhcpServerIPAddressType_Type()
)
cadVrDhcpServerIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrDhcpServerIPAddressType.setStatus("current")


class _CadVrDhcpServerTypes_Type(CadCpeDeviceTypes):
    """Custom type cadVrDhcpServerTypes based on CadCpeDeviceTypes"""
    defaultBinValue = "0"


_CadVrDhcpServerTypes_Object = MibTableColumn
cadVrDhcpServerTypes = _CadVrDhcpServerTypes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4, 1, 5),
    _CadVrDhcpServerTypes_Type()
)
cadVrDhcpServerTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrDhcpServerTypes.setStatus("current")
_CadDhcpThrottle_ObjectIdentity = ObjectIdentity
cadDhcpThrottle = _CadDhcpThrottle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5)
)


class _CadDhcpThrottleEnable_Type(TruthValue):
    """Custom type cadDhcpThrottleEnable based on TruthValue"""


_CadDhcpThrottleEnable_Object = MibScalar
cadDhcpThrottleEnable = _CadDhcpThrottleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 1),
    _CadDhcpThrottleEnable_Type()
)
cadDhcpThrottleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpThrottleEnable.setStatus("current")


class _CadDhcpThrottleBurstSize_Type(Unsigned32):
    """Custom type cadDhcpThrottleBurstSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CadDhcpThrottleBurstSize_Type.__name__ = "Unsigned32"
_CadDhcpThrottleBurstSize_Object = MibScalar
cadDhcpThrottleBurstSize = _CadDhcpThrottleBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 2),
    _CadDhcpThrottleBurstSize_Type()
)
cadDhcpThrottleBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpThrottleBurstSize.setStatus("current")


class _CadDhcpThrottleRate_Type(Unsigned32):
    """Custom type cadDhcpThrottleRate based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CadDhcpThrottleRate_Type.__name__ = "Unsigned32"
_CadDhcpThrottleRate_Object = MibScalar
cadDhcpThrottleRate = _CadDhcpThrottleRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 3),
    _CadDhcpThrottleRate_Type()
)
cadDhcpThrottleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpThrottleRate.setStatus("current")
if mibBuilder.loadTexts:
    cadDhcpThrottleRate.setUnits("seconds")


class _CadArpThrottleEnable_Type(TruthValue):
    """Custom type cadArpThrottleEnable based on TruthValue"""


_CadArpThrottleEnable_Object = MibScalar
cadArpThrottleEnable = _CadArpThrottleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 4),
    _CadArpThrottleEnable_Type()
)
cadArpThrottleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadArpThrottleEnable.setStatus("current")


class _CadDhcpV6ThrottleEnable_Type(TruthValue):
    """Custom type cadDhcpV6ThrottleEnable based on TruthValue"""


_CadDhcpV6ThrottleEnable_Object = MibScalar
cadDhcpV6ThrottleEnable = _CadDhcpV6ThrottleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 5),
    _CadDhcpV6ThrottleEnable_Type()
)
cadDhcpV6ThrottleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpV6ThrottleEnable.setStatus("current")


class _CadNdThrottleEnable_Type(TruthValue):
    """Custom type cadNdThrottleEnable based on TruthValue"""


_CadNdThrottleEnable_Object = MibScalar
cadNdThrottleEnable = _CadNdThrottleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 6),
    _CadNdThrottleEnable_Type()
)
cadNdThrottleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadNdThrottleEnable.setStatus("current")
_CadDhcpRaOption_ObjectIdentity = ObjectIdentity
cadDhcpRaOption = _CadDhcpRaOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6)
)


class _CadDhcpRaOptionType_Type(CadDhcpRelayAgentOptionType):
    """Custom type cadDhcpRaOptionType based on CadDhcpRelayAgentOptionType"""


_CadDhcpRaOptionType_Object = MibScalar
cadDhcpRaOptionType = _CadDhcpRaOptionType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 1),
    _CadDhcpRaOptionType_Type()
)
cadDhcpRaOptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpRaOptionType.setStatus("current")


class _CadDhcpRaOptionString_Type(OctetString):
    """Custom type cadDhcpRaOptionString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadDhcpRaOptionString_Type.__name__ = "OctetString"
_CadDhcpRaOptionString_Object = MibScalar
cadDhcpRaOptionString = _CadDhcpRaOptionString_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 2),
    _CadDhcpRaOptionString_Type()
)
cadDhcpRaOptionString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpRaOptionString.setStatus("current")
_CadDhcpRaOptionUpstreamChannelTable_Object = MibTable
cadDhcpRaOptionUpstreamChannelTable = _CadDhcpRaOptionUpstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 3)
)
if mibBuilder.loadTexts:
    cadDhcpRaOptionUpstreamChannelTable.setStatus("current")
_CadDhcpRaOptionUpstreamChannelEntry_Object = MibTableRow
cadDhcpRaOptionUpstreamChannelEntry = _CadDhcpRaOptionUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 3, 1)
)
cadDhcpRaOptionUpstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadDhcpRaOptionUpstreamChannelEntry.setStatus("current")


class _CadDhcpRaOptUpChannelOptionType_Type(CadDhcpRelayAgentOptionType):
    """Custom type cadDhcpRaOptUpChannelOptionType based on CadDhcpRelayAgentOptionType"""


_CadDhcpRaOptUpChannelOptionType_Object = MibTableColumn
cadDhcpRaOptUpChannelOptionType = _CadDhcpRaOptUpChannelOptionType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 3, 1, 1),
    _CadDhcpRaOptUpChannelOptionType_Type()
)
cadDhcpRaOptUpChannelOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDhcpRaOptUpChannelOptionType.setStatus("current")


class _CadDhcpRaOptUpChannelOptionString_Type(OctetString):
    """Custom type cadDhcpRaOptUpChannelOptionString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadDhcpRaOptUpChannelOptionString_Type.__name__ = "OctetString"
_CadDhcpRaOptUpChannelOptionString_Object = MibTableColumn
cadDhcpRaOptUpChannelOptionString = _CadDhcpRaOptUpChannelOptionString_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 3, 1, 2),
    _CadDhcpRaOptUpChannelOptionString_Type()
)
cadDhcpRaOptUpChannelOptionString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDhcpRaOptUpChannelOptionString.setStatus("current")
_CadDhcpRaOptUpChannelStatus_Type = RowStatus
_CadDhcpRaOptUpChannelStatus_Object = MibTableColumn
cadDhcpRaOptUpChannelStatus = _CadDhcpRaOptUpChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 3, 1, 3),
    _CadDhcpRaOptUpChannelStatus_Type()
)
cadDhcpRaOptUpChannelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDhcpRaOptUpChannelStatus.setStatus("current")


class _CadVrDhcpRelaySrcInterfaceIndex_Type(InterfaceIndexOrZero):
    """Custom type cadVrDhcpRelaySrcInterfaceIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadVrDhcpRelaySrcInterfaceIndex_Object = MibScalar
cadVrDhcpRelaySrcInterfaceIndex = _CadVrDhcpRelaySrcInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 4),
    _CadVrDhcpRelaySrcInterfaceIndex_Type()
)
cadVrDhcpRelaySrcInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrDhcpRelaySrcInterfaceIndex.setStatus("current")


class _CadVrDhcpRelaySrcInterfaceLinkAddrEnabled_Type(TruthValue):
    """Custom type cadVrDhcpRelaySrcInterfaceLinkAddrEnabled based on TruthValue"""


_CadVrDhcpRelaySrcInterfaceLinkAddrEnabled_Object = MibScalar
cadVrDhcpRelaySrcInterfaceLinkAddrEnabled = _CadVrDhcpRelaySrcInterfaceLinkAddrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 5),
    _CadVrDhcpRelaySrcInterfaceLinkAddrEnabled_Type()
)
cadVrDhcpRelaySrcInterfaceLinkAddrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrDhcpRelaySrcInterfaceLinkAddrEnabled.setStatus("current")


class _CadVrDhcpRaOptionScnEnable_Type(TruthValue):
    """Custom type cadVrDhcpRaOptionScnEnable based on TruthValue"""


_CadVrDhcpRaOptionScnEnable_Object = MibScalar
cadVrDhcpRaOptionScnEnable = _CadVrDhcpRaOptionScnEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 6),
    _CadVrDhcpRaOptionScnEnable_Type()
)
cadVrDhcpRaOptionScnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrDhcpRaOptionScnEnable.setStatus("current")


class _CadDhcpRaOptionMSOTextType_Type(CadDhcpRaOptionMSOTextType):
    """Custom type cadDhcpRaOptionMSOTextType based on CadDhcpRaOptionMSOTextType"""


_CadDhcpRaOptionMSOTextType_Object = MibScalar
cadDhcpRaOptionMSOTextType = _CadDhcpRaOptionMSOTextType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 7),
    _CadDhcpRaOptionMSOTextType_Type()
)
cadDhcpRaOptionMSOTextType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpRaOptionMSOTextType.setStatus("current")


class _CadDhcpRaOptionMSOTextString_Type(OctetString):
    """Custom type cadDhcpRaOptionMSOTextString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadDhcpRaOptionMSOTextString_Type.__name__ = "OctetString"
_CadDhcpRaOptionMSOTextString_Object = MibScalar
cadDhcpRaOptionMSOTextString = _CadDhcpRaOptionMSOTextString_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 8),
    _CadDhcpRaOptionMSOTextString_Type()
)
cadDhcpRaOptionMSOTextString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpRaOptionMSOTextString.setStatus("current")
_CadDhcpRaOptionChannelMSOTextTable_Object = MibTable
cadDhcpRaOptionChannelMSOTextTable = _CadDhcpRaOptionChannelMSOTextTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 9)
)
if mibBuilder.loadTexts:
    cadDhcpRaOptionChannelMSOTextTable.setStatus("current")
_CadDhcpRaOptionChannelMSOTextEntry_Object = MibTableRow
cadDhcpRaOptionChannelMSOTextEntry = _CadDhcpRaOptionChannelMSOTextEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 9, 1)
)
cadDhcpRaOptionChannelMSOTextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadDhcpRaOptionChannelMSOTextEntry.setStatus("current")


class _CadDhcpRaOptionChannelMSOTextType_Type(CadDhcpRaOptionMSOTextType):
    """Custom type cadDhcpRaOptionChannelMSOTextType based on CadDhcpRaOptionMSOTextType"""


_CadDhcpRaOptionChannelMSOTextType_Object = MibTableColumn
cadDhcpRaOptionChannelMSOTextType = _CadDhcpRaOptionChannelMSOTextType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 9, 1, 1),
    _CadDhcpRaOptionChannelMSOTextType_Type()
)
cadDhcpRaOptionChannelMSOTextType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDhcpRaOptionChannelMSOTextType.setStatus("current")


class _CadDhcpRaOptionChannelMSOTextString_Type(OctetString):
    """Custom type cadDhcpRaOptionChannelMSOTextString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadDhcpRaOptionChannelMSOTextString_Type.__name__ = "OctetString"
_CadDhcpRaOptionChannelMSOTextString_Object = MibTableColumn
cadDhcpRaOptionChannelMSOTextString = _CadDhcpRaOptionChannelMSOTextString_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 9, 1, 2),
    _CadDhcpRaOptionChannelMSOTextString_Type()
)
cadDhcpRaOptionChannelMSOTextString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDhcpRaOptionChannelMSOTextString.setStatus("current")
_CadDhcpRaOptionChannelMSOTextStatus_Type = RowStatus
_CadDhcpRaOptionChannelMSOTextStatus_Object = MibTableColumn
cadDhcpRaOptionChannelMSOTextStatus = _CadDhcpRaOptionChannelMSOTextStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 9, 1, 3),
    _CadDhcpRaOptionChannelMSOTextStatus_Type()
)
cadDhcpRaOptionChannelMSOTextStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDhcpRaOptionChannelMSOTextStatus.setStatus("current")


class _CadVrDhcpRaOptionFanoutDisabled_Type(TruthValue):
    """Custom type cadVrDhcpRaOptionFanoutDisabled based on TruthValue"""


_CadVrDhcpRaOptionFanoutDisabled_Object = MibScalar
cadVrDhcpRaOptionFanoutDisabled = _CadVrDhcpRaOptionFanoutDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 10),
    _CadVrDhcpRaOptionFanoutDisabled_Type()
)
cadVrDhcpRaOptionFanoutDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrDhcpRaOptionFanoutDisabled.setStatus("current")
_CadDhcpRaLeaseQuery_ObjectIdentity = ObjectIdentity
cadDhcpRaLeaseQuery = _CadDhcpRaLeaseQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 7)
)


class _CadDhcpRaLeasequeryVersion_Type(Integer32):
    """Custom type cadDhcpRaLeasequeryVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              11)
        )
    )
    namedValues = NamedValues(
        *(("draft-0", 1),
          ("draft-2", 3),
          ("draft-4", 5),
          ("rfc-4388", 11))
    )


_CadDhcpRaLeasequeryVersion_Type.__name__ = "Integer32"
_CadDhcpRaLeasequeryVersion_Object = MibScalar
cadDhcpRaLeasequeryVersion = _CadDhcpRaLeasequeryVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 7, 1),
    _CadDhcpRaLeasequeryVersion_Type()
)
cadDhcpRaLeasequeryVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpRaLeasequeryVersion.setStatus("current")


class _CadDhcpRaLeasequeryMessageType_Type(Integer32):
    """Custom type cadDhcpRaLeasequeryMessageType based on Integer32"""
    defaultValue = 13

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 13),
    )


_CadDhcpRaLeasequeryMessageType_Type.__name__ = "Integer32"
_CadDhcpRaLeasequeryMessageType_Object = MibScalar
cadDhcpRaLeasequeryMessageType = _CadDhcpRaLeasequeryMessageType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 7, 2),
    _CadDhcpRaLeasequeryMessageType_Type()
)
cadDhcpRaLeasequeryMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpRaLeasequeryMessageType.setStatus("current")
_CadVrDhcpLinkAddressTable_Object = MibTable
cadVrDhcpLinkAddressTable = _CadVrDhcpLinkAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8)
)
if mibBuilder.loadTexts:
    cadVrDhcpLinkAddressTable.setStatus("current")
_CadVrDhcpLinkAddressEntry_Object = MibTableRow
cadVrDhcpLinkAddressEntry = _CadVrDhcpLinkAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8, 1)
)
cadVrDhcpLinkAddressEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrInterfaceIfIndex"),
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpLinkAddressType"),
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpLinkAddress"),
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpLinkType"),
)
if mibBuilder.loadTexts:
    cadVrDhcpLinkAddressEntry.setStatus("current")
_CadVrDhcpLinkAddressType_Type = InetAddressType
_CadVrDhcpLinkAddressType_Object = MibTableColumn
cadVrDhcpLinkAddressType = _CadVrDhcpLinkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8, 1, 1),
    _CadVrDhcpLinkAddressType_Type()
)
cadVrDhcpLinkAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpLinkAddressType.setStatus("current")
_CadVrDhcpLinkAddress_Type = InetAddressIPv4or6
_CadVrDhcpLinkAddress_Object = MibTableColumn
cadVrDhcpLinkAddress = _CadVrDhcpLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8, 1, 2),
    _CadVrDhcpLinkAddress_Type()
)
cadVrDhcpLinkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpLinkAddress.setStatus("current")
_CadVrDhcpLinkType_Type = CadBridgePortType
_CadVrDhcpLinkType_Object = MibTableColumn
cadVrDhcpLinkType = _CadVrDhcpLinkType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8, 1, 3),
    _CadVrDhcpLinkType_Type()
)
cadVrDhcpLinkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpLinkType.setStatus("current")
_CadVrDhcpLinkRowStatus_Type = RowStatus
_CadVrDhcpLinkRowStatus_Object = MibTableColumn
cadVrDhcpLinkRowStatus = _CadVrDhcpLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8, 1, 4),
    _CadVrDhcpLinkRowStatus_Type()
)
cadVrDhcpLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrDhcpLinkRowStatus.setStatus("current")
_CadDhcpPd_ObjectIdentity = ObjectIdentity
cadDhcpPd = _CadDhcpPd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 9)
)


class _CadDhcpPdRiEnabled_Type(TruthValue):
    """Custom type cadDhcpPdRiEnabled based on TruthValue"""


_CadDhcpPdRiEnabled_Object = MibScalar
cadDhcpPdRiEnabled = _CadDhcpPdRiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 9, 1),
    _CadDhcpPdRiEnabled_Type()
)
cadDhcpPdRiEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpPdRiEnabled.setStatus("current")


class _CadDhcpPdPrefixStabilityEnabled_Type(TruthValue):
    """Custom type cadDhcpPdPrefixStabilityEnabled based on TruthValue"""


_CadDhcpPdPrefixStabilityEnabled_Object = MibScalar
cadDhcpPdPrefixStabilityEnabled = _CadDhcpPdPrefixStabilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 9, 2),
    _CadDhcpPdPrefixStabilityEnabled_Type()
)
cadDhcpPdPrefixStabilityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpPdPrefixStabilityEnabled.setStatus("current")
_CadVrDhcpPdTable_Object = MibTable
cadVrDhcpPdTable = _CadVrDhcpPdTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10)
)
if mibBuilder.loadTexts:
    cadVrDhcpPdTable.setStatus("current")
_CadVrDhcpPdEntry_Object = MibTableRow
cadVrDhcpPdEntry = _CadVrDhcpPdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1)
)
cadVrDhcpPdEntry.setIndexNames(
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdClientIpv6Addr"),
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdClientIaid"),
)
if mibBuilder.loadTexts:
    cadVrDhcpPdEntry.setStatus("current")
_CadVrDhcpPdClientIpv6Addr_Type = InetAddressIPv6
_CadVrDhcpPdClientIpv6Addr_Object = MibTableColumn
cadVrDhcpPdClientIpv6Addr = _CadVrDhcpPdClientIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 1),
    _CadVrDhcpPdClientIpv6Addr_Type()
)
cadVrDhcpPdClientIpv6Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpPdClientIpv6Addr.setStatus("current")
_CadVrDhcpPdClientIaid_Type = Unsigned32
_CadVrDhcpPdClientIaid_Object = MibTableColumn
cadVrDhcpPdClientIaid = _CadVrDhcpPdClientIaid_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 2),
    _CadVrDhcpPdClientIaid_Type()
)
cadVrDhcpPdClientIaid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpPdClientIaid.setStatus("current")


class _CadVrDhcpPdIfIndex_Type(Integer32):
    """Custom type cadVrDhcpPdIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CadVrDhcpPdIfIndex_Type.__name__ = "Integer32"
_CadVrDhcpPdIfIndex_Object = MibTableColumn
cadVrDhcpPdIfIndex = _CadVrDhcpPdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 3),
    _CadVrDhcpPdIfIndex_Type()
)
cadVrDhcpPdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrDhcpPdIfIndex.setStatus("current")
_CadVrDhcpPdClientDuid_Type = OctetString
_CadVrDhcpPdClientDuid_Object = MibTableColumn
cadVrDhcpPdClientDuid = _CadVrDhcpPdClientDuid_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 4),
    _CadVrDhcpPdClientDuid_Type()
)
cadVrDhcpPdClientDuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrDhcpPdClientDuid.setStatus("current")
_CadVrDhcpPdCmMacAddress_Type = MacAddress
_CadVrDhcpPdCmMacAddress_Object = MibTableColumn
cadVrDhcpPdCmMacAddress = _CadVrDhcpPdCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 5),
    _CadVrDhcpPdCmMacAddress_Type()
)
cadVrDhcpPdCmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrDhcpPdCmMacAddress.setStatus("current")


class _CadVrDhcpPdT1_Type(Unsigned32):
    """Custom type cadVrDhcpPdT1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CadVrDhcpPdT1_Type.__name__ = "Unsigned32"
_CadVrDhcpPdT1_Object = MibTableColumn
cadVrDhcpPdT1 = _CadVrDhcpPdT1_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 6),
    _CadVrDhcpPdT1_Type()
)
cadVrDhcpPdT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrDhcpPdT1.setStatus("current")


class _CadVrDhcpPdT2_Type(Unsigned32):
    """Custom type cadVrDhcpPdT2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CadVrDhcpPdT2_Type.__name__ = "Unsigned32"
_CadVrDhcpPdT2_Object = MibTableColumn
cadVrDhcpPdT2 = _CadVrDhcpPdT2_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 7),
    _CadVrDhcpPdT2_Type()
)
cadVrDhcpPdT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrDhcpPdT2.setStatus("current")
_CadVrDhcpPdPrefixTable_Object = MibTable
cadVrDhcpPdPrefixTable = _CadVrDhcpPdPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11)
)
if mibBuilder.loadTexts:
    cadVrDhcpPdPrefixTable.setStatus("current")
_CadVrDhcpPdPrefixEntry_Object = MibTableRow
cadVrDhcpPdPrefixEntry = _CadVrDhcpPdPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1)
)
cadVrDhcpPdPrefixEntry.setIndexNames(
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdPreClientIpv6Addr"),
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdPreClientIaid"),
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdPrePrefix"),
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdPrePrefixLength"),
)
if mibBuilder.loadTexts:
    cadVrDhcpPdPrefixEntry.setStatus("current")
_CadVrDhcpPdPreClientIpv6Addr_Type = InetAddressIPv6
_CadVrDhcpPdPreClientIpv6Addr_Object = MibTableColumn
cadVrDhcpPdPreClientIpv6Addr = _CadVrDhcpPdPreClientIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 1),
    _CadVrDhcpPdPreClientIpv6Addr_Type()
)
cadVrDhcpPdPreClientIpv6Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpPdPreClientIpv6Addr.setStatus("current")
_CadVrDhcpPdPreClientIaid_Type = Unsigned32
_CadVrDhcpPdPreClientIaid_Object = MibTableColumn
cadVrDhcpPdPreClientIaid = _CadVrDhcpPdPreClientIaid_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 2),
    _CadVrDhcpPdPreClientIaid_Type()
)
cadVrDhcpPdPreClientIaid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpPdPreClientIaid.setStatus("current")
_CadVrDhcpPdPrePrefix_Type = InetAddressIPv6
_CadVrDhcpPdPrePrefix_Object = MibTableColumn
cadVrDhcpPdPrePrefix = _CadVrDhcpPdPrePrefix_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 3),
    _CadVrDhcpPdPrePrefix_Type()
)
cadVrDhcpPdPrePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpPdPrePrefix.setStatus("current")


class _CadVrDhcpPdPrePrefixLength_Type(Integer32):
    """Custom type cadVrDhcpPdPrePrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CadVrDhcpPdPrePrefixLength_Type.__name__ = "Integer32"
_CadVrDhcpPdPrePrefixLength_Object = MibTableColumn
cadVrDhcpPdPrePrefixLength = _CadVrDhcpPdPrePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 4),
    _CadVrDhcpPdPrePrefixLength_Type()
)
cadVrDhcpPdPrePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpPdPrePrefixLength.setStatus("current")


class _CadVrDhcpPdPrePreferredLifetime_Type(Unsigned32):
    """Custom type cadVrDhcpPdPrePreferredLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CadVrDhcpPdPrePreferredLifetime_Type.__name__ = "Unsigned32"
_CadVrDhcpPdPrePreferredLifetime_Object = MibTableColumn
cadVrDhcpPdPrePreferredLifetime = _CadVrDhcpPdPrePreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 5),
    _CadVrDhcpPdPrePreferredLifetime_Type()
)
cadVrDhcpPdPrePreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrDhcpPdPrePreferredLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cadVrDhcpPdPrePreferredLifetime.setUnits("seconds")


class _CadVrDhcpPdPreValidLifetime_Type(Unsigned32):
    """Custom type cadVrDhcpPdPreValidLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CadVrDhcpPdPreValidLifetime_Type.__name__ = "Unsigned32"
_CadVrDhcpPdPreValidLifetime_Object = MibTableColumn
cadVrDhcpPdPreValidLifetime = _CadVrDhcpPdPreValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 6),
    _CadVrDhcpPdPreValidLifetime_Type()
)
cadVrDhcpPdPreValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrDhcpPdPreValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cadVrDhcpPdPreValidLifetime.setUnits("seconds")
_CadVrDhcpPdPreRouteInject_Type = TruthValue
_CadVrDhcpPdPreRouteInject_Object = MibTableColumn
cadVrDhcpPdPreRouteInject = _CadVrDhcpPdPreRouteInject_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 7),
    _CadVrDhcpPdPreRouteInject_Type()
)
cadVrDhcpPdPreRouteInject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrDhcpPdPreRouteInject.setStatus("current")


class _CadVrDhcpPdPreExpirytime_Type(Unsigned32):
    """Custom type cadVrDhcpPdPreExpirytime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CadVrDhcpPdPreExpirytime_Type.__name__ = "Unsigned32"
_CadVrDhcpPdPreExpirytime_Object = MibTableColumn
cadVrDhcpPdPreExpirytime = _CadVrDhcpPdPreExpirytime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 8),
    _CadVrDhcpPdPreExpirytime_Type()
)
cadVrDhcpPdPreExpirytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrDhcpPdPreExpirytime.setStatus("current")
if mibBuilder.loadTexts:
    cadVrDhcpPdPreExpirytime.setUnits("seconds")
_CadVrDhcpRelayEgressIfTable_Object = MibTable
cadVrDhcpRelayEgressIfTable = _CadVrDhcpRelayEgressIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 12)
)
if mibBuilder.loadTexts:
    cadVrDhcpRelayEgressIfTable.setStatus("current")
_CadVrDhcpRelayEgressIfEntry_Object = MibTableRow
cadVrDhcpRelayEgressIfEntry = _CadVrDhcpRelayEgressIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 12, 1)
)
cadVrDhcpRelayEgressIfEntry.setIndexNames(
    (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpRelayEgressIfIndex"),
)
if mibBuilder.loadTexts:
    cadVrDhcpRelayEgressIfEntry.setStatus("current")
_CadVrDhcpRelayEgressIfIndex_Type = InterfaceIndex
_CadVrDhcpRelayEgressIfIndex_Object = MibTableColumn
cadVrDhcpRelayEgressIfIndex = _CadVrDhcpRelayEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 12, 1, 1),
    _CadVrDhcpRelayEgressIfIndex_Type()
)
cadVrDhcpRelayEgressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrDhcpRelayEgressIfIndex.setStatus("current")
_CadVrDhcpRelayEgressIfRowStatus_Type = RowStatus
_CadVrDhcpRelayEgressIfRowStatus_Object = MibTableColumn
cadVrDhcpRelayEgressIfRowStatus = _CadVrDhcpRelayEgressIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 12, 1, 2),
    _CadVrDhcpRelayEgressIfRowStatus_Type()
)
cadVrDhcpRelayEgressIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrDhcpRelayEgressIfRowStatus.setStatus("current")
_CadDhcpPdPrefixAction_ObjectIdentity = ObjectIdentity
cadDhcpPdPrefixAction = _CadDhcpPdPrefixAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13)
)


class _CadDhcpPdPrefixActionType_Type(CadDhcpPDPreActionType):
    """Custom type cadDhcpPdPrefixActionType based on CadDhcpPDPreActionType"""


_CadDhcpPdPrefixActionType_Object = MibScalar
cadDhcpPdPrefixActionType = _CadDhcpPdPrefixActionType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13, 1),
    _CadDhcpPdPrefixActionType_Type()
)
cadDhcpPdPrefixActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpPdPrefixActionType.setStatus("current")


class _CadDhcpPdPrefixActionDataType_Type(CadDhcpPDPreActionDataType):
    """Custom type cadDhcpPdPrefixActionDataType based on CadDhcpPDPreActionDataType"""


_CadDhcpPdPrefixActionDataType_Object = MibScalar
cadDhcpPdPrefixActionDataType = _CadDhcpPdPrefixActionDataType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13, 2),
    _CadDhcpPdPrefixActionDataType_Type()
)
cadDhcpPdPrefixActionDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpPdPrefixActionDataType.setStatus("current")


class _CadDhcpPdPrefixActionDataIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cadDhcpPdPrefixActionDataIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadDhcpPdPrefixActionDataIfIndex_Object = MibScalar
cadDhcpPdPrefixActionDataIfIndex = _CadDhcpPdPrefixActionDataIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13, 3),
    _CadDhcpPdPrefixActionDataIfIndex_Type()
)
cadDhcpPdPrefixActionDataIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpPdPrefixActionDataIfIndex.setStatus("current")
_CadDhcpPdPrefixActionDataPrefixOrIp_Type = InetAddressIPv6
_CadDhcpPdPrefixActionDataPrefixOrIp_Object = MibScalar
cadDhcpPdPrefixActionDataPrefixOrIp = _CadDhcpPdPrefixActionDataPrefixOrIp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13, 4),
    _CadDhcpPdPrefixActionDataPrefixOrIp_Type()
)
cadDhcpPdPrefixActionDataPrefixOrIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpPdPrefixActionDataPrefixOrIp.setStatus("current")


class _CadDhcpPdPrefixActionDataPrefixOrIpLen_Type(Integer32):
    """Custom type cadDhcpPdPrefixActionDataPrefixOrIpLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CadDhcpPdPrefixActionDataPrefixOrIpLen_Type.__name__ = "Integer32"
_CadDhcpPdPrefixActionDataPrefixOrIpLen_Object = MibScalar
cadDhcpPdPrefixActionDataPrefixOrIpLen = _CadDhcpPdPrefixActionDataPrefixOrIpLen_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13, 5),
    _CadDhcpPdPrefixActionDataPrefixOrIpLen_Type()
)
cadDhcpPdPrefixActionDataPrefixOrIpLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDhcpPdPrefixActionDataPrefixOrIpLen.setStatus("current")
_CadDhcpPdBLQFailedGrp_ObjectIdentity = ObjectIdentity
cadDhcpPdBLQFailedGrp = _CadDhcpPdBLQFailedGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 14)
)
_CadDhcpPdBLQFailedTCPSIP_Type = InetAddressIPv6
_CadDhcpPdBLQFailedTCPSIP_Object = MibScalar
cadDhcpPdBLQFailedTCPSIP = _CadDhcpPdBLQFailedTCPSIP_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 14, 1),
    _CadDhcpPdBLQFailedTCPSIP_Type()
)
cadDhcpPdBLQFailedTCPSIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDhcpPdBLQFailedTCPSIP.setStatus("current")
_CadDhcpPdBLQFailedTCPDIP_Type = InetAddressIPv6
_CadDhcpPdBLQFailedTCPDIP_Object = MibScalar
cadDhcpPdBLQFailedTCPDIP = _CadDhcpPdBLQFailedTCPDIP_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 14, 2),
    _CadDhcpPdBLQFailedTCPDIP_Type()
)
cadDhcpPdBLQFailedTCPDIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDhcpPdBLQFailedTCPDIP.setStatus("current")
_CadDhcpPdBLQFailedTCPTime_Type = DateAndTime
_CadDhcpPdBLQFailedTCPTime_Object = MibScalar
cadDhcpPdBLQFailedTCPTime = _CadDhcpPdBLQFailedTCPTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 14, 3),
    _CadDhcpPdBLQFailedTCPTime_Type()
)
cadDhcpPdBLQFailedTCPTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDhcpPdBLQFailedTCPTime.setStatus("current")
_CadDhcpPdBLQFailedTCPNum_Type = Unsigned32
_CadDhcpPdBLQFailedTCPNum_Object = MibScalar
cadDhcpPdBLQFailedTCPNum = _CadDhcpPdBLQFailedTCPNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 14, 4),
    _CadDhcpPdBLQFailedTCPNum_Type()
)
cadDhcpPdBLQFailedTCPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDhcpPdBLQFailedTCPNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-DHCPRA-MIB",
    **{"CadDhcpRelayAgentOptionType": CadDhcpRelayAgentOptionType,
       "CadDhcpPDPreActionType": CadDhcpPDPreActionType,
       "CadDhcpPDPreActionDataType": CadDhcpPDPreActionDataType,
       "CadDhcpRaOptionMSOTextType": CadDhcpRaOptionMSOTextType,
       "cadDhcpRaMib": cadDhcpRaMib,
       "cadVrDhcpServerTable": cadVrDhcpServerTable,
       "cadVrDhcpServerEntry": cadVrDhcpServerEntry,
       "cadVrDhcpServerIPAddress": cadVrDhcpServerIPAddress,
       "cadVrDhcpServerRowStatus": cadVrDhcpServerRowStatus,
       "cadVrDhcpServerIPAddressType": cadVrDhcpServerIPAddressType,
       "cadVrDhcpServerTypes": cadVrDhcpServerTypes,
       "cadDhcpThrottle": cadDhcpThrottle,
       "cadDhcpThrottleEnable": cadDhcpThrottleEnable,
       "cadDhcpThrottleBurstSize": cadDhcpThrottleBurstSize,
       "cadDhcpThrottleRate": cadDhcpThrottleRate,
       "cadArpThrottleEnable": cadArpThrottleEnable,
       "cadDhcpV6ThrottleEnable": cadDhcpV6ThrottleEnable,
       "cadNdThrottleEnable": cadNdThrottleEnable,
       "cadDhcpRaOption": cadDhcpRaOption,
       "cadDhcpRaOptionType": cadDhcpRaOptionType,
       "cadDhcpRaOptionString": cadDhcpRaOptionString,
       "cadDhcpRaOptionUpstreamChannelTable": cadDhcpRaOptionUpstreamChannelTable,
       "cadDhcpRaOptionUpstreamChannelEntry": cadDhcpRaOptionUpstreamChannelEntry,
       "cadDhcpRaOptUpChannelOptionType": cadDhcpRaOptUpChannelOptionType,
       "cadDhcpRaOptUpChannelOptionString": cadDhcpRaOptUpChannelOptionString,
       "cadDhcpRaOptUpChannelStatus": cadDhcpRaOptUpChannelStatus,
       "cadVrDhcpRelaySrcInterfaceIndex": cadVrDhcpRelaySrcInterfaceIndex,
       "cadVrDhcpRelaySrcInterfaceLinkAddrEnabled": cadVrDhcpRelaySrcInterfaceLinkAddrEnabled,
       "cadVrDhcpRaOptionScnEnable": cadVrDhcpRaOptionScnEnable,
       "cadDhcpRaOptionMSOTextType": cadDhcpRaOptionMSOTextType,
       "cadDhcpRaOptionMSOTextString": cadDhcpRaOptionMSOTextString,
       "cadDhcpRaOptionChannelMSOTextTable": cadDhcpRaOptionChannelMSOTextTable,
       "cadDhcpRaOptionChannelMSOTextEntry": cadDhcpRaOptionChannelMSOTextEntry,
       "cadDhcpRaOptionChannelMSOTextType": cadDhcpRaOptionChannelMSOTextType,
       "cadDhcpRaOptionChannelMSOTextString": cadDhcpRaOptionChannelMSOTextString,
       "cadDhcpRaOptionChannelMSOTextStatus": cadDhcpRaOptionChannelMSOTextStatus,
       "cadVrDhcpRaOptionFanoutDisabled": cadVrDhcpRaOptionFanoutDisabled,
       "cadDhcpRaLeaseQuery": cadDhcpRaLeaseQuery,
       "cadDhcpRaLeasequeryVersion": cadDhcpRaLeasequeryVersion,
       "cadDhcpRaLeasequeryMessageType": cadDhcpRaLeasequeryMessageType,
       "cadVrDhcpLinkAddressTable": cadVrDhcpLinkAddressTable,
       "cadVrDhcpLinkAddressEntry": cadVrDhcpLinkAddressEntry,
       "cadVrDhcpLinkAddressType": cadVrDhcpLinkAddressType,
       "cadVrDhcpLinkAddress": cadVrDhcpLinkAddress,
       "cadVrDhcpLinkType": cadVrDhcpLinkType,
       "cadVrDhcpLinkRowStatus": cadVrDhcpLinkRowStatus,
       "cadDhcpPd": cadDhcpPd,
       "cadDhcpPdRiEnabled": cadDhcpPdRiEnabled,
       "cadDhcpPdPrefixStabilityEnabled": cadDhcpPdPrefixStabilityEnabled,
       "cadVrDhcpPdTable": cadVrDhcpPdTable,
       "cadVrDhcpPdEntry": cadVrDhcpPdEntry,
       "cadVrDhcpPdClientIpv6Addr": cadVrDhcpPdClientIpv6Addr,
       "cadVrDhcpPdClientIaid": cadVrDhcpPdClientIaid,
       "cadVrDhcpPdIfIndex": cadVrDhcpPdIfIndex,
       "cadVrDhcpPdClientDuid": cadVrDhcpPdClientDuid,
       "cadVrDhcpPdCmMacAddress": cadVrDhcpPdCmMacAddress,
       "cadVrDhcpPdT1": cadVrDhcpPdT1,
       "cadVrDhcpPdT2": cadVrDhcpPdT2,
       "cadVrDhcpPdPrefixTable": cadVrDhcpPdPrefixTable,
       "cadVrDhcpPdPrefixEntry": cadVrDhcpPdPrefixEntry,
       "cadVrDhcpPdPreClientIpv6Addr": cadVrDhcpPdPreClientIpv6Addr,
       "cadVrDhcpPdPreClientIaid": cadVrDhcpPdPreClientIaid,
       "cadVrDhcpPdPrePrefix": cadVrDhcpPdPrePrefix,
       "cadVrDhcpPdPrePrefixLength": cadVrDhcpPdPrePrefixLength,
       "cadVrDhcpPdPrePreferredLifetime": cadVrDhcpPdPrePreferredLifetime,
       "cadVrDhcpPdPreValidLifetime": cadVrDhcpPdPreValidLifetime,
       "cadVrDhcpPdPreRouteInject": cadVrDhcpPdPreRouteInject,
       "cadVrDhcpPdPreExpirytime": cadVrDhcpPdPreExpirytime,
       "cadVrDhcpRelayEgressIfTable": cadVrDhcpRelayEgressIfTable,
       "cadVrDhcpRelayEgressIfEntry": cadVrDhcpRelayEgressIfEntry,
       "cadVrDhcpRelayEgressIfIndex": cadVrDhcpRelayEgressIfIndex,
       "cadVrDhcpRelayEgressIfRowStatus": cadVrDhcpRelayEgressIfRowStatus,
       "cadDhcpPdPrefixAction": cadDhcpPdPrefixAction,
       "cadDhcpPdPrefixActionType": cadDhcpPdPrefixActionType,
       "cadDhcpPdPrefixActionDataType": cadDhcpPdPrefixActionDataType,
       "cadDhcpPdPrefixActionDataIfIndex": cadDhcpPdPrefixActionDataIfIndex,
       "cadDhcpPdPrefixActionDataPrefixOrIp": cadDhcpPdPrefixActionDataPrefixOrIp,
       "cadDhcpPdPrefixActionDataPrefixOrIpLen": cadDhcpPdPrefixActionDataPrefixOrIpLen,
       "cadDhcpPdBLQFailedGrp": cadDhcpPdBLQFailedGrp,
       "cadDhcpPdBLQFailedTCPSIP": cadDhcpPdBLQFailedTCPSIP,
       "cadDhcpPdBLQFailedTCPDIP": cadDhcpPdBLQFailedTCPDIP,
       "cadDhcpPdBLQFailedTCPTime": cadDhcpPdBLQFailedTCPTime,
       "cadDhcpPdBLQFailedTCPNum": cadDhcpPdBLQFailedTCPNum}
)
