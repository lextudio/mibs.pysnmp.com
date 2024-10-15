# SNMP MIB module (CISCO-TAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:28 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 enterprises,
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
    "enterprises",
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

cTapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 252)
)
cTapMIB.setRevisions(
        ("2005-10-12 00:00",
         "2002-07-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dscp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



# MIB Managed Objects in the order of their OIDs

_CTapMIBNotifications_ObjectIdentity = ObjectIdentity
cTapMIBNotifications = _CTapMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 0)
)
_CTapMIBObjects_ObjectIdentity = ObjectIdentity
cTapMIBObjects = _CTapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1)
)
_CTapMediationGroup_ObjectIdentity = ObjectIdentity
cTapMediationGroup = _CTapMediationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1)
)


class _CTapMediationNewIndex_Type(Integer32):
    """Custom type cTapMediationNewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CTapMediationNewIndex_Type.__name__ = "Integer32"
_CTapMediationNewIndex_Object = MibScalar
cTapMediationNewIndex = _CTapMediationNewIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 1),
    _CTapMediationNewIndex_Type()
)
cTapMediationNewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTapMediationNewIndex.setStatus("current")
_CTapMediationTable_Object = MibTable
cTapMediationTable = _CTapMediationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cTapMediationTable.setStatus("current")
_CTapMediationEntry_Object = MibTableRow
cTapMediationEntry = _CTapMediationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1)
)
cTapMediationEntry.setIndexNames(
    (0, "CISCO-TAP-MIB", "cTapMediationContentId"),
)
if mibBuilder.loadTexts:
    cTapMediationEntry.setStatus("current")


class _CTapMediationContentId_Type(Integer32):
    """Custom type cTapMediationContentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CTapMediationContentId_Type.__name__ = "Integer32"
_CTapMediationContentId_Object = MibTableColumn
cTapMediationContentId = _CTapMediationContentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 1),
    _CTapMediationContentId_Type()
)
cTapMediationContentId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cTapMediationContentId.setStatus("current")
_CTapMediationDestAddressType_Type = InetAddressType
_CTapMediationDestAddressType_Object = MibTableColumn
cTapMediationDestAddressType = _CTapMediationDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 2),
    _CTapMediationDestAddressType_Type()
)
cTapMediationDestAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationDestAddressType.setStatus("current")
_CTapMediationDestAddress_Type = InetAddress
_CTapMediationDestAddress_Object = MibTableColumn
cTapMediationDestAddress = _CTapMediationDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 3),
    _CTapMediationDestAddress_Type()
)
cTapMediationDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationDestAddress.setStatus("current")
_CTapMediationDestPort_Type = InetPortNumber
_CTapMediationDestPort_Object = MibTableColumn
cTapMediationDestPort = _CTapMediationDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 4),
    _CTapMediationDestPort_Type()
)
cTapMediationDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationDestPort.setStatus("current")
_CTapMediationSrcInterface_Type = InterfaceIndexOrZero
_CTapMediationSrcInterface_Object = MibTableColumn
cTapMediationSrcInterface = _CTapMediationSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 5),
    _CTapMediationSrcInterface_Type()
)
cTapMediationSrcInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationSrcInterface.setStatus("current")
_CTapMediationRtcpPort_Type = InetPortNumber
_CTapMediationRtcpPort_Object = MibTableColumn
cTapMediationRtcpPort = _CTapMediationRtcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 6),
    _CTapMediationRtcpPort_Type()
)
cTapMediationRtcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTapMediationRtcpPort.setStatus("current")


class _CTapMediationDscp_Type(Dscp):
    """Custom type cTapMediationDscp based on Dscp"""
    defaultValue = 34


_CTapMediationDscp_Object = MibTableColumn
cTapMediationDscp = _CTapMediationDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 7),
    _CTapMediationDscp_Type()
)
cTapMediationDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationDscp.setStatus("current")


class _CTapMediationDataType_Type(Integer32):
    """Custom type cTapMediationDataType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CTapMediationDataType_Type.__name__ = "Integer32"
_CTapMediationDataType_Object = MibTableColumn
cTapMediationDataType = _CTapMediationDataType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 8),
    _CTapMediationDataType_Type()
)
cTapMediationDataType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationDataType.setStatus("current")


class _CTapMediationRetransmitType_Type(Integer32):
    """Custom type cTapMediationRetransmitType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CTapMediationRetransmitType_Type.__name__ = "Integer32"
_CTapMediationRetransmitType_Object = MibTableColumn
cTapMediationRetransmitType = _CTapMediationRetransmitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 9),
    _CTapMediationRetransmitType_Type()
)
cTapMediationRetransmitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationRetransmitType.setStatus("current")
_CTapMediationTimeout_Type = DateAndTime
_CTapMediationTimeout_Object = MibTableColumn
cTapMediationTimeout = _CTapMediationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 10),
    _CTapMediationTimeout_Type()
)
cTapMediationTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationTimeout.setStatus("current")


class _CTapMediationTransport_Type(Integer32):
    """Custom type cTapMediationTransport based on Integer32"""
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
        *(("rtpNack", 2),
          ("sctp", 4),
          ("tcp", 3),
          ("udp", 1))
    )


_CTapMediationTransport_Type.__name__ = "Integer32"
_CTapMediationTransport_Object = MibTableColumn
cTapMediationTransport = _CTapMediationTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 11),
    _CTapMediationTransport_Type()
)
cTapMediationTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationTransport.setStatus("current")


class _CTapMediationNotificationEnable_Type(TruthValue):
    """Custom type cTapMediationNotificationEnable based on TruthValue"""


_CTapMediationNotificationEnable_Object = MibTableColumn
cTapMediationNotificationEnable = _CTapMediationNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 12),
    _CTapMediationNotificationEnable_Type()
)
cTapMediationNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationNotificationEnable.setStatus("current")
_CTapMediationStatus_Type = RowStatus
_CTapMediationStatus_Object = MibTableColumn
cTapMediationStatus = _CTapMediationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 2, 1, 13),
    _CTapMediationStatus_Type()
)
cTapMediationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapMediationStatus.setStatus("current")


class _CTapMediationCapabilities_Type(Bits):
    """Custom type cTapMediationCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("ipV4SrcInterface", 0),
          ("ipV6SrcInterface", 1),
          ("rtpNack", 3),
          ("sctp", 5),
          ("tcp", 4),
          ("udp", 2))
    )

_CTapMediationCapabilities_Type.__name__ = "Bits"
_CTapMediationCapabilities_Object = MibScalar
cTapMediationCapabilities = _CTapMediationCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 1, 3),
    _CTapMediationCapabilities_Type()
)
cTapMediationCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTapMediationCapabilities.setStatus("current")
_CTapStreamGroup_ObjectIdentity = ObjectIdentity
cTapStreamGroup = _CTapStreamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2)
)


class _CTapStreamCapabilities_Type(Bits):
    """Custom type cTapStreamCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dscp", 5),
          ("dstLlcSap", 9),
          ("dstMacAddr", 6),
          ("ethernetPid", 8),
          ("interface", 1),
          ("ipV4", 2),
          ("ipV6", 3),
          ("l4Port", 4),
          ("srcLlcSap", 10),
          ("srcMacAddr", 7),
          ("tapEnable", 0))
    )

_CTapStreamCapabilities_Type.__name__ = "Bits"
_CTapStreamCapabilities_Object = MibScalar
cTapStreamCapabilities = _CTapStreamCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 1),
    _CTapStreamCapabilities_Type()
)
cTapStreamCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTapStreamCapabilities.setStatus("current")
_CTapStreamIpTable_Object = MibTable
cTapStreamIpTable = _CTapStreamIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cTapStreamIpTable.setStatus("current")
_CTapStreamIpEntry_Object = MibTableRow
cTapStreamIpEntry = _CTapStreamIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1)
)
cTapStreamIpEntry.setIndexNames(
    (0, "CISCO-TAP-MIB", "cTapMediationContentId"),
    (0, "CISCO-TAP-MIB", "cTapStreamIpIndex"),
)
if mibBuilder.loadTexts:
    cTapStreamIpEntry.setStatus("current")


class _CTapStreamIpIndex_Type(Integer32):
    """Custom type cTapStreamIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CTapStreamIpIndex_Type.__name__ = "Integer32"
_CTapStreamIpIndex_Object = MibTableColumn
cTapStreamIpIndex = _CTapStreamIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 1),
    _CTapStreamIpIndex_Type()
)
cTapStreamIpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cTapStreamIpIndex.setStatus("current")


class _CTapStreamIpInterface_Type(Integer32):
    """Custom type cTapStreamIpInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_CTapStreamIpInterface_Type.__name__ = "Integer32"
_CTapStreamIpInterface_Object = MibTableColumn
cTapStreamIpInterface = _CTapStreamIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 2),
    _CTapStreamIpInterface_Type()
)
cTapStreamIpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpInterface.setStatus("current")


class _CTapStreamIpAddrType_Type(InetAddressType):
    """Custom type cTapStreamIpAddrType based on InetAddressType"""


_CTapStreamIpAddrType_Object = MibTableColumn
cTapStreamIpAddrType = _CTapStreamIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 3),
    _CTapStreamIpAddrType_Type()
)
cTapStreamIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpAddrType.setStatus("current")


class _CTapStreamIpDestinationAddress_Type(InetAddress):
    """Custom type cTapStreamIpDestinationAddress based on InetAddress"""
    defaultHexValue = "00000000"


_CTapStreamIpDestinationAddress_Object = MibTableColumn
cTapStreamIpDestinationAddress = _CTapStreamIpDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 4),
    _CTapStreamIpDestinationAddress_Type()
)
cTapStreamIpDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpDestinationAddress.setStatus("current")


class _CTapStreamIpDestinationLength_Type(InetAddressPrefixLength):
    """Custom type cTapStreamIpDestinationLength based on InetAddressPrefixLength"""
    defaultValue = 0


_CTapStreamIpDestinationLength_Object = MibTableColumn
cTapStreamIpDestinationLength = _CTapStreamIpDestinationLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 5),
    _CTapStreamIpDestinationLength_Type()
)
cTapStreamIpDestinationLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpDestinationLength.setStatus("current")


class _CTapStreamIpSourceAddress_Type(InetAddress):
    """Custom type cTapStreamIpSourceAddress based on InetAddress"""
    defaultHexValue = "00000000"


_CTapStreamIpSourceAddress_Object = MibTableColumn
cTapStreamIpSourceAddress = _CTapStreamIpSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 6),
    _CTapStreamIpSourceAddress_Type()
)
cTapStreamIpSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpSourceAddress.setStatus("current")


class _CTapStreamIpSourceLength_Type(InetAddressPrefixLength):
    """Custom type cTapStreamIpSourceLength based on InetAddressPrefixLength"""
    defaultValue = 0


_CTapStreamIpSourceLength_Object = MibTableColumn
cTapStreamIpSourceLength = _CTapStreamIpSourceLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 7),
    _CTapStreamIpSourceLength_Type()
)
cTapStreamIpSourceLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpSourceLength.setStatus("current")


class _CTapStreamIpTosByte_Type(Integer32):
    """Custom type cTapStreamIpTosByte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CTapStreamIpTosByte_Type.__name__ = "Integer32"
_CTapStreamIpTosByte_Object = MibTableColumn
cTapStreamIpTosByte = _CTapStreamIpTosByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 8),
    _CTapStreamIpTosByte_Type()
)
cTapStreamIpTosByte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpTosByte.setStatus("current")


class _CTapStreamIpTosByteMask_Type(Integer32):
    """Custom type cTapStreamIpTosByteMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CTapStreamIpTosByteMask_Type.__name__ = "Integer32"
_CTapStreamIpTosByteMask_Object = MibTableColumn
cTapStreamIpTosByteMask = _CTapStreamIpTosByteMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 9),
    _CTapStreamIpTosByteMask_Type()
)
cTapStreamIpTosByteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpTosByteMask.setStatus("current")


class _CTapStreamIpFlowId_Type(Integer32):
    """Custom type cTapStreamIpFlowId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_CTapStreamIpFlowId_Type.__name__ = "Integer32"
_CTapStreamIpFlowId_Object = MibTableColumn
cTapStreamIpFlowId = _CTapStreamIpFlowId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 10),
    _CTapStreamIpFlowId_Type()
)
cTapStreamIpFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpFlowId.setStatus("current")


class _CTapStreamIpProtocol_Type(Integer32):
    """Custom type cTapStreamIpProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_CTapStreamIpProtocol_Type.__name__ = "Integer32"
_CTapStreamIpProtocol_Object = MibTableColumn
cTapStreamIpProtocol = _CTapStreamIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 11),
    _CTapStreamIpProtocol_Type()
)
cTapStreamIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpProtocol.setStatus("current")


class _CTapStreamIpDestL4PortMin_Type(InetPortNumber):
    """Custom type cTapStreamIpDestL4PortMin based on InetPortNumber"""
    defaultValue = 0


_CTapStreamIpDestL4PortMin_Object = MibTableColumn
cTapStreamIpDestL4PortMin = _CTapStreamIpDestL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 12),
    _CTapStreamIpDestL4PortMin_Type()
)
cTapStreamIpDestL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpDestL4PortMin.setStatus("current")


class _CTapStreamIpDestL4PortMax_Type(InetPortNumber):
    """Custom type cTapStreamIpDestL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_CTapStreamIpDestL4PortMax_Object = MibTableColumn
cTapStreamIpDestL4PortMax = _CTapStreamIpDestL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 13),
    _CTapStreamIpDestL4PortMax_Type()
)
cTapStreamIpDestL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpDestL4PortMax.setStatus("current")


class _CTapStreamIpSourceL4PortMin_Type(InetPortNumber):
    """Custom type cTapStreamIpSourceL4PortMin based on InetPortNumber"""
    defaultValue = 0


_CTapStreamIpSourceL4PortMin_Object = MibTableColumn
cTapStreamIpSourceL4PortMin = _CTapStreamIpSourceL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 14),
    _CTapStreamIpSourceL4PortMin_Type()
)
cTapStreamIpSourceL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpSourceL4PortMin.setStatus("current")


class _CTapStreamIpSourceL4PortMax_Type(InetPortNumber):
    """Custom type cTapStreamIpSourceL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_CTapStreamIpSourceL4PortMax_Object = MibTableColumn
cTapStreamIpSourceL4PortMax = _CTapStreamIpSourceL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 15),
    _CTapStreamIpSourceL4PortMax_Type()
)
cTapStreamIpSourceL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpSourceL4PortMax.setStatus("current")


class _CTapStreamIpInterceptEnable_Type(TruthValue):
    """Custom type cTapStreamIpInterceptEnable based on TruthValue"""


_CTapStreamIpInterceptEnable_Object = MibTableColumn
cTapStreamIpInterceptEnable = _CTapStreamIpInterceptEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 16),
    _CTapStreamIpInterceptEnable_Type()
)
cTapStreamIpInterceptEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpInterceptEnable.setStatus("current")
_CTapStreamIpInterceptedPackets_Type = Counter32
_CTapStreamIpInterceptedPackets_Object = MibTableColumn
cTapStreamIpInterceptedPackets = _CTapStreamIpInterceptedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 17),
    _CTapStreamIpInterceptedPackets_Type()
)
cTapStreamIpInterceptedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTapStreamIpInterceptedPackets.setStatus("current")
_CTapStreamIpInterceptDrops_Type = Counter32
_CTapStreamIpInterceptDrops_Object = MibTableColumn
cTapStreamIpInterceptDrops = _CTapStreamIpInterceptDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 18),
    _CTapStreamIpInterceptDrops_Type()
)
cTapStreamIpInterceptDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTapStreamIpInterceptDrops.setStatus("current")
_CTapStreamIpStatus_Type = RowStatus
_CTapStreamIpStatus_Object = MibTableColumn
cTapStreamIpStatus = _CTapStreamIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 2, 1, 19),
    _CTapStreamIpStatus_Type()
)
cTapStreamIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStreamIpStatus.setStatus("current")
_CTapStream802Table_Object = MibTable
cTapStream802Table = _CTapStream802Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cTapStream802Table.setStatus("current")
_CTapStream802Entry_Object = MibTableRow
cTapStream802Entry = _CTapStream802Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1)
)
cTapStream802Entry.setIndexNames(
    (0, "CISCO-TAP-MIB", "cTapMediationContentId"),
    (0, "CISCO-TAP-MIB", "cTapStream802Index"),
)
if mibBuilder.loadTexts:
    cTapStream802Entry.setStatus("current")


class _CTapStream802Index_Type(Integer32):
    """Custom type cTapStream802Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CTapStream802Index_Type.__name__ = "Integer32"
_CTapStream802Index_Object = MibTableColumn
cTapStream802Index = _CTapStream802Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 1),
    _CTapStream802Index_Type()
)
cTapStream802Index.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cTapStream802Index.setStatus("current")


class _CTapStream802Fields_Type(Bits):
    """Custom type cTapStream802Fields based on Bits"""
    namedValues = NamedValues(
        *(("dstLlcSap", 4),
          ("dstMacAddress", 1),
          ("ethernetPid", 3),
          ("interface", 0),
          ("srcLlcSap", 5),
          ("srcMacAddress", 2))
    )

_CTapStream802Fields_Type.__name__ = "Bits"
_CTapStream802Fields_Object = MibTableColumn
cTapStream802Fields = _CTapStream802Fields_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 2),
    _CTapStream802Fields_Type()
)
cTapStream802Fields.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStream802Fields.setStatus("current")


class _CTapStream802Interface_Type(Integer32):
    """Custom type cTapStream802Interface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_CTapStream802Interface_Type.__name__ = "Integer32"
_CTapStream802Interface_Object = MibTableColumn
cTapStream802Interface = _CTapStream802Interface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 3),
    _CTapStream802Interface_Type()
)
cTapStream802Interface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStream802Interface.setStatus("current")
_CTapStream802DestinationAddress_Type = MacAddress
_CTapStream802DestinationAddress_Object = MibTableColumn
cTapStream802DestinationAddress = _CTapStream802DestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 4),
    _CTapStream802DestinationAddress_Type()
)
cTapStream802DestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStream802DestinationAddress.setStatus("current")
_CTapStream802SourceAddress_Type = MacAddress
_CTapStream802SourceAddress_Object = MibTableColumn
cTapStream802SourceAddress = _CTapStream802SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 5),
    _CTapStream802SourceAddress_Type()
)
cTapStream802SourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStream802SourceAddress.setStatus("current")


class _CTapStream802EthernetPid_Type(Integer32):
    """Custom type cTapStream802EthernetPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CTapStream802EthernetPid_Type.__name__ = "Integer32"
_CTapStream802EthernetPid_Object = MibTableColumn
cTapStream802EthernetPid = _CTapStream802EthernetPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 6),
    _CTapStream802EthernetPid_Type()
)
cTapStream802EthernetPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStream802EthernetPid.setStatus("current")


class _CTapStream802DestinationLlcSap_Type(Integer32):
    """Custom type cTapStream802DestinationLlcSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CTapStream802DestinationLlcSap_Type.__name__ = "Integer32"
_CTapStream802DestinationLlcSap_Object = MibTableColumn
cTapStream802DestinationLlcSap = _CTapStream802DestinationLlcSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 7),
    _CTapStream802DestinationLlcSap_Type()
)
cTapStream802DestinationLlcSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStream802DestinationLlcSap.setStatus("current")


class _CTapStream802SourceLlcSap_Type(Integer32):
    """Custom type cTapStream802SourceLlcSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CTapStream802SourceLlcSap_Type.__name__ = "Integer32"
_CTapStream802SourceLlcSap_Object = MibTableColumn
cTapStream802SourceLlcSap = _CTapStream802SourceLlcSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 8),
    _CTapStream802SourceLlcSap_Type()
)
cTapStream802SourceLlcSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStream802SourceLlcSap.setStatus("current")


class _CTapStream802InterceptEnable_Type(TruthValue):
    """Custom type cTapStream802InterceptEnable based on TruthValue"""


_CTapStream802InterceptEnable_Object = MibTableColumn
cTapStream802InterceptEnable = _CTapStream802InterceptEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 9),
    _CTapStream802InterceptEnable_Type()
)
cTapStream802InterceptEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStream802InterceptEnable.setStatus("current")
_CTapStream802InterceptedPackets_Type = Counter32
_CTapStream802InterceptedPackets_Object = MibTableColumn
cTapStream802InterceptedPackets = _CTapStream802InterceptedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 10),
    _CTapStream802InterceptedPackets_Type()
)
cTapStream802InterceptedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTapStream802InterceptedPackets.setStatus("current")
_CTapStream802InterceptDrops_Type = Counter32
_CTapStream802InterceptDrops_Object = MibTableColumn
cTapStream802InterceptDrops = _CTapStream802InterceptDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 11),
    _CTapStream802InterceptDrops_Type()
)
cTapStream802InterceptDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTapStream802InterceptDrops.setStatus("current")
_CTapStream802Status_Type = RowStatus
_CTapStream802Status_Object = MibTableColumn
cTapStream802Status = _CTapStream802Status_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 2, 3, 1, 12),
    _CTapStream802Status_Type()
)
cTapStream802Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTapStream802Status.setStatus("current")
_CTapDebugGroup_ObjectIdentity = ObjectIdentity
cTapDebugGroup = _CTapDebugGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 3)
)
_CTapDebugTable_Object = MibTable
cTapDebugTable = _CTapDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cTapDebugTable.setStatus("current")
_CTapDebugEntry_Object = MibTableRow
cTapDebugEntry = _CTapDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 3, 1, 1)
)
cTapDebugEntry.setIndexNames(
    (0, "CISCO-TAP-MIB", "cTapDebugIndex"),
)
if mibBuilder.loadTexts:
    cTapDebugEntry.setStatus("current")
_CTapDebugIndex_Type = Unsigned32
_CTapDebugIndex_Object = MibTableColumn
cTapDebugIndex = _CTapDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 3, 1, 1, 1),
    _CTapDebugIndex_Type()
)
cTapDebugIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cTapDebugIndex.setStatus("current")
_CTapDebugMessage_Type = SnmpAdminString
_CTapDebugMessage_Object = MibTableColumn
cTapDebugMessage = _CTapDebugMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 1, 3, 1, 1, 2),
    _CTapDebugMessage_Type()
)
cTapDebugMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTapDebugMessage.setStatus("current")
_CTapMIBConformance_ObjectIdentity = ObjectIdentity
cTapMIBConformance = _CTapMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2)
)
_CTapMIBCompliances_ObjectIdentity = ObjectIdentity
cTapMIBCompliances = _CTapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 1)
)
_CTapMIBGroups_ObjectIdentity = ObjectIdentity
cTapMIBGroups = _CTapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2)
)

# Managed Objects groups

cTapMediationComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 1)
)
cTapMediationComplianceGroup.setObjects(
      *(("CISCO-TAP-MIB", "cTapMediationNewIndex"),
        ("CISCO-TAP-MIB", "cTapMediationDestAddressType"),
        ("CISCO-TAP-MIB", "cTapMediationDestAddress"),
        ("CISCO-TAP-MIB", "cTapMediationDestPort"),
        ("CISCO-TAP-MIB", "cTapMediationSrcInterface"),
        ("CISCO-TAP-MIB", "cTapMediationRtcpPort"),
        ("CISCO-TAP-MIB", "cTapMediationDscp"),
        ("CISCO-TAP-MIB", "cTapMediationDataType"),
        ("CISCO-TAP-MIB", "cTapMediationRetransmitType"),
        ("CISCO-TAP-MIB", "cTapMediationTimeout"),
        ("CISCO-TAP-MIB", "cTapMediationTransport"),
        ("CISCO-TAP-MIB", "cTapMediationNotificationEnable"),
        ("CISCO-TAP-MIB", "cTapMediationStatus"))
)
if mibBuilder.loadTexts:
    cTapMediationComplianceGroup.setStatus("current")

cTapStreamComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 2)
)
cTapStreamComplianceGroup.setObjects(
    ("CISCO-TAP-MIB", "cTapStreamCapabilities")
)
if mibBuilder.loadTexts:
    cTapStreamComplianceGroup.setStatus("current")

cTapStreamIpComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 3)
)
cTapStreamIpComplianceGroup.setObjects(
      *(("CISCO-TAP-MIB", "cTapStreamIpInterface"),
        ("CISCO-TAP-MIB", "cTapStreamIpAddrType"),
        ("CISCO-TAP-MIB", "cTapStreamIpDestinationAddress"),
        ("CISCO-TAP-MIB", "cTapStreamIpDestinationLength"),
        ("CISCO-TAP-MIB", "cTapStreamIpSourceAddress"),
        ("CISCO-TAP-MIB", "cTapStreamIpSourceLength"),
        ("CISCO-TAP-MIB", "cTapStreamIpTosByte"),
        ("CISCO-TAP-MIB", "cTapStreamIpTosByteMask"),
        ("CISCO-TAP-MIB", "cTapStreamIpFlowId"),
        ("CISCO-TAP-MIB", "cTapStreamIpProtocol"),
        ("CISCO-TAP-MIB", "cTapStreamIpDestL4PortMin"),
        ("CISCO-TAP-MIB", "cTapStreamIpDestL4PortMax"),
        ("CISCO-TAP-MIB", "cTapStreamIpSourceL4PortMin"),
        ("CISCO-TAP-MIB", "cTapStreamIpSourceL4PortMax"),
        ("CISCO-TAP-MIB", "cTapStreamIpInterceptEnable"),
        ("CISCO-TAP-MIB", "cTapStreamIpInterceptedPackets"),
        ("CISCO-TAP-MIB", "cTapStreamIpInterceptDrops"),
        ("CISCO-TAP-MIB", "cTapStreamIpStatus"))
)
if mibBuilder.loadTexts:
    cTapStreamIpComplianceGroup.setStatus("current")

cTapStream802ComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 4)
)
cTapStream802ComplianceGroup.setObjects(
      *(("CISCO-TAP-MIB", "cTapStream802Fields"),
        ("CISCO-TAP-MIB", "cTapStream802Interface"),
        ("CISCO-TAP-MIB", "cTapStream802DestinationAddress"),
        ("CISCO-TAP-MIB", "cTapStream802SourceAddress"),
        ("CISCO-TAP-MIB", "cTapStream802EthernetPid"),
        ("CISCO-TAP-MIB", "cTapStream802SourceLlcSap"),
        ("CISCO-TAP-MIB", "cTapStream802DestinationLlcSap"),
        ("CISCO-TAP-MIB", "cTapStream802InterceptEnable"),
        ("CISCO-TAP-MIB", "cTapStream802InterceptedPackets"),
        ("CISCO-TAP-MIB", "cTapStream802InterceptDrops"),
        ("CISCO-TAP-MIB", "cTapStream802Status"))
)
if mibBuilder.loadTexts:
    cTapStream802ComplianceGroup.setStatus("current")

cTapMediationCpbComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 6)
)
cTapMediationCpbComplianceGroup.setObjects(
    ("CISCO-TAP-MIB", "cTapMediationCapabilities")
)
if mibBuilder.loadTexts:
    cTapMediationCpbComplianceGroup.setStatus("current")

cTapDebugComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 7)
)
cTapDebugComplianceGroup.setObjects(
    ("CISCO-TAP-MIB", "cTapDebugMessage")
)
if mibBuilder.loadTexts:
    cTapDebugComplianceGroup.setStatus("current")


# Notification objects

cTapMIBActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 0, 1)
)
cTapMIBActive.setObjects(
    ("CISCO-TAP-MIB", "cTapStream802Status")
)
if mibBuilder.loadTexts:
    cTapMIBActive.setStatus(
        "current"
    )

cTapMediationTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 0, 2)
)
cTapMediationTimedOut.setObjects(
    ("CISCO-TAP-MIB", "cTapMediationStatus")
)
if mibBuilder.loadTexts:
    cTapMediationTimedOut.setStatus(
        "current"
    )

cTapMediationDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 0, 3)
)
cTapMediationDebug.setObjects(
      *(("CISCO-TAP-MIB", "cTapMediationContentId"),
        ("CISCO-TAP-MIB", "cTapDebugIndex"))
)
if mibBuilder.loadTexts:
    cTapMediationDebug.setStatus(
        "current"
    )

cTapStreamIpDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 0, 4)
)
cTapStreamIpDebug.setObjects(
      *(("CISCO-TAP-MIB", "cTapMediationContentId"),
        ("CISCO-TAP-MIB", "cTapStreamIpIndex"),
        ("CISCO-TAP-MIB", "cTapDebugIndex"))
)
if mibBuilder.loadTexts:
    cTapStreamIpDebug.setStatus(
        "current"
    )

cTapStream802Debug = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 0, 5)
)
cTapStream802Debug.setObjects(
      *(("CISCO-TAP-MIB", "cTapMediationContentId"),
        ("CISCO-TAP-MIB", "cTapStream802Index"),
        ("CISCO-TAP-MIB", "cTapDebugIndex"))
)
if mibBuilder.loadTexts:
    cTapStream802Debug.setStatus(
        "current"
    )


# Notifications groups

cTapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 2, 5)
)
cTapNotificationGroup.setObjects(
      *(("CISCO-TAP-MIB", "cTapMIBActive"),
        ("CISCO-TAP-MIB", "cTapMediationTimedOut"),
        ("CISCO-TAP-MIB", "cTapMediationDebug"),
        ("CISCO-TAP-MIB", "cTapStreamIpDebug"))
)
if mibBuilder.loadTexts:
    cTapNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cTapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 252, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cTapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TAP-MIB",
    **{"Dscp": Dscp,
       "cTapMIB": cTapMIB,
       "cTapMIBNotifications": cTapMIBNotifications,
       "cTapMIBActive": cTapMIBActive,
       "cTapMediationTimedOut": cTapMediationTimedOut,
       "cTapMediationDebug": cTapMediationDebug,
       "cTapStreamIpDebug": cTapStreamIpDebug,
       "cTapStream802Debug": cTapStream802Debug,
       "cTapMIBObjects": cTapMIBObjects,
       "cTapMediationGroup": cTapMediationGroup,
       "cTapMediationNewIndex": cTapMediationNewIndex,
       "cTapMediationTable": cTapMediationTable,
       "cTapMediationEntry": cTapMediationEntry,
       "cTapMediationContentId": cTapMediationContentId,
       "cTapMediationDestAddressType": cTapMediationDestAddressType,
       "cTapMediationDestAddress": cTapMediationDestAddress,
       "cTapMediationDestPort": cTapMediationDestPort,
       "cTapMediationSrcInterface": cTapMediationSrcInterface,
       "cTapMediationRtcpPort": cTapMediationRtcpPort,
       "cTapMediationDscp": cTapMediationDscp,
       "cTapMediationDataType": cTapMediationDataType,
       "cTapMediationRetransmitType": cTapMediationRetransmitType,
       "cTapMediationTimeout": cTapMediationTimeout,
       "cTapMediationTransport": cTapMediationTransport,
       "cTapMediationNotificationEnable": cTapMediationNotificationEnable,
       "cTapMediationStatus": cTapMediationStatus,
       "cTapMediationCapabilities": cTapMediationCapabilities,
       "cTapStreamGroup": cTapStreamGroup,
       "cTapStreamCapabilities": cTapStreamCapabilities,
       "cTapStreamIpTable": cTapStreamIpTable,
       "cTapStreamIpEntry": cTapStreamIpEntry,
       "cTapStreamIpIndex": cTapStreamIpIndex,
       "cTapStreamIpInterface": cTapStreamIpInterface,
       "cTapStreamIpAddrType": cTapStreamIpAddrType,
       "cTapStreamIpDestinationAddress": cTapStreamIpDestinationAddress,
       "cTapStreamIpDestinationLength": cTapStreamIpDestinationLength,
       "cTapStreamIpSourceAddress": cTapStreamIpSourceAddress,
       "cTapStreamIpSourceLength": cTapStreamIpSourceLength,
       "cTapStreamIpTosByte": cTapStreamIpTosByte,
       "cTapStreamIpTosByteMask": cTapStreamIpTosByteMask,
       "cTapStreamIpFlowId": cTapStreamIpFlowId,
       "cTapStreamIpProtocol": cTapStreamIpProtocol,
       "cTapStreamIpDestL4PortMin": cTapStreamIpDestL4PortMin,
       "cTapStreamIpDestL4PortMax": cTapStreamIpDestL4PortMax,
       "cTapStreamIpSourceL4PortMin": cTapStreamIpSourceL4PortMin,
       "cTapStreamIpSourceL4PortMax": cTapStreamIpSourceL4PortMax,
       "cTapStreamIpInterceptEnable": cTapStreamIpInterceptEnable,
       "cTapStreamIpInterceptedPackets": cTapStreamIpInterceptedPackets,
       "cTapStreamIpInterceptDrops": cTapStreamIpInterceptDrops,
       "cTapStreamIpStatus": cTapStreamIpStatus,
       "cTapStream802Table": cTapStream802Table,
       "cTapStream802Entry": cTapStream802Entry,
       "cTapStream802Index": cTapStream802Index,
       "cTapStream802Fields": cTapStream802Fields,
       "cTapStream802Interface": cTapStream802Interface,
       "cTapStream802DestinationAddress": cTapStream802DestinationAddress,
       "cTapStream802SourceAddress": cTapStream802SourceAddress,
       "cTapStream802EthernetPid": cTapStream802EthernetPid,
       "cTapStream802DestinationLlcSap": cTapStream802DestinationLlcSap,
       "cTapStream802SourceLlcSap": cTapStream802SourceLlcSap,
       "cTapStream802InterceptEnable": cTapStream802InterceptEnable,
       "cTapStream802InterceptedPackets": cTapStream802InterceptedPackets,
       "cTapStream802InterceptDrops": cTapStream802InterceptDrops,
       "cTapStream802Status": cTapStream802Status,
       "cTapDebugGroup": cTapDebugGroup,
       "cTapDebugTable": cTapDebugTable,
       "cTapDebugEntry": cTapDebugEntry,
       "cTapDebugIndex": cTapDebugIndex,
       "cTapDebugMessage": cTapDebugMessage,
       "cTapMIBConformance": cTapMIBConformance,
       "cTapMIBCompliances": cTapMIBCompliances,
       "cTapMIBCompliance": cTapMIBCompliance,
       "cTapMIBGroups": cTapMIBGroups,
       "cTapMediationComplianceGroup": cTapMediationComplianceGroup,
       "cTapStreamComplianceGroup": cTapStreamComplianceGroup,
       "cTapStreamIpComplianceGroup": cTapStreamIpComplianceGroup,
       "cTapStream802ComplianceGroup": cTapStream802ComplianceGroup,
       "cTapNotificationGroup": cTapNotificationGroup,
       "cTapMediationCpbComplianceGroup": cTapMediationCpbComplianceGroup,
       "cTapDebugComplianceGroup": cTapDebugComplianceGroup}
)
