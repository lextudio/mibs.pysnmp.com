# SNMP MIB module (A3COM-HUAWEI-LI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-LI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:18 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cLI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111)
)
h3cLI.setRevisions(
        ("2009-08-25 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cLICommon_ObjectIdentity = ObjectIdentity
h3cLICommon = _H3cLICommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1)
)
_H3cLITrapBindObjects_ObjectIdentity = ObjectIdentity
h3cLITrapBindObjects = _H3cLITrapBindObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 1)
)
_H3cLIBoardInformation_Type = Unsigned32
_H3cLIBoardInformation_Object = MibScalar
h3cLIBoardInformation = _H3cLIBoardInformation_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 1, 1),
    _H3cLIBoardInformation_Type()
)
h3cLIBoardInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLIBoardInformation.setStatus("current")
_H3cLINotifications_ObjectIdentity = ObjectIdentity
h3cLINotifications = _H3cLINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 2)
)
_H3cLINotificationsPrefix_ObjectIdentity = ObjectIdentity
h3cLINotificationsPrefix = _H3cLINotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 2, 0)
)
_H3cLIObjects_ObjectIdentity = ObjectIdentity
h3cLIObjects = _H3cLIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3)
)


class _H3cLINewIndex_Type(Integer32):
    """Custom type h3cLINewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cLINewIndex_Type.__name__ = "Integer32"
_H3cLINewIndex_Object = MibScalar
h3cLINewIndex = _H3cLINewIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 1),
    _H3cLINewIndex_Type()
)
h3cLINewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLINewIndex.setStatus("current")
_H3cLIMediationTable_Object = MibTable
h3cLIMediationTable = _H3cLIMediationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3cLIMediationTable.setStatus("current")
_H3cLIMediationEntry_Object = MibTableRow
h3cLIMediationEntry = _H3cLIMediationEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1)
)
h3cLIMediationEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LI-MIB", "h3cLIMediationIndex"),
)
if mibBuilder.loadTexts:
    h3cLIMediationEntry.setStatus("current")


class _H3cLIMediationIndex_Type(Integer32):
    """Custom type h3cLIMediationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cLIMediationIndex_Type.__name__ = "Integer32"
_H3cLIMediationIndex_Object = MibTableColumn
h3cLIMediationIndex = _H3cLIMediationIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 1),
    _H3cLIMediationIndex_Type()
)
h3cLIMediationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cLIMediationIndex.setStatus("current")
_H3cLIMediationDestAddrType_Type = InetAddressType
_H3cLIMediationDestAddrType_Object = MibTableColumn
h3cLIMediationDestAddrType = _H3cLIMediationDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 2),
    _H3cLIMediationDestAddrType_Type()
)
h3cLIMediationDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMediationDestAddrType.setStatus("current")
_H3cLIMediationDestAddr_Type = InetAddress
_H3cLIMediationDestAddr_Object = MibTableColumn
h3cLIMediationDestAddr = _H3cLIMediationDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 3),
    _H3cLIMediationDestAddr_Type()
)
h3cLIMediationDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMediationDestAddr.setStatus("current")
_H3cLIMediationDestPort_Type = InetPortNumber
_H3cLIMediationDestPort_Object = MibTableColumn
h3cLIMediationDestPort = _H3cLIMediationDestPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 4),
    _H3cLIMediationDestPort_Type()
)
h3cLIMediationDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMediationDestPort.setStatus("current")
_H3cLIMediationSrcInterface_Type = InterfaceIndexOrZero
_H3cLIMediationSrcInterface_Object = MibTableColumn
h3cLIMediationSrcInterface = _H3cLIMediationSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 5),
    _H3cLIMediationSrcInterface_Type()
)
h3cLIMediationSrcInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMediationSrcInterface.setStatus("current")


class _H3cLIMediationDscp_Type(Integer32):
    """Custom type h3cLIMediationDscp based on Integer32"""
    defaultValue = 34


_H3cLIMediationDscp_Object = MibTableColumn
h3cLIMediationDscp = _H3cLIMediationDscp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 6),
    _H3cLIMediationDscp_Type()
)
h3cLIMediationDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMediationDscp.setStatus("current")
_H3cLIMediationTimeOut_Type = DateAndTime
_H3cLIMediationTimeOut_Object = MibTableColumn
h3cLIMediationTimeOut = _H3cLIMediationTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 7),
    _H3cLIMediationTimeOut_Type()
)
h3cLIMediationTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMediationTimeOut.setStatus("current")


class _H3cLIMediationTransport_Type(Integer32):
    """Custom type h3cLIMediationTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("udp", 1)
    )


_H3cLIMediationTransport_Type.__name__ = "Integer32"
_H3cLIMediationTransport_Object = MibTableColumn
h3cLIMediationTransport = _H3cLIMediationTransport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 8),
    _H3cLIMediationTransport_Type()
)
h3cLIMediationTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMediationTransport.setStatus("current")


class _H3cLIMediationNotificationEnable_Type(TruthValue):
    """Custom type h3cLIMediationNotificationEnable based on TruthValue"""


_H3cLIMediationNotificationEnable_Object = MibTableColumn
h3cLIMediationNotificationEnable = _H3cLIMediationNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 9),
    _H3cLIMediationNotificationEnable_Type()
)
h3cLIMediationNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMediationNotificationEnable.setStatus("current")
_H3cLIMediationRowStatus_Type = RowStatus
_H3cLIMediationRowStatus_Object = MibTableColumn
h3cLIMediationRowStatus = _H3cLIMediationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 2, 1, 10),
    _H3cLIMediationRowStatus_Type()
)
h3cLIMediationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLIMediationRowStatus.setStatus("current")
_H3cLIStreamTable_Object = MibTable
h3cLIStreamTable = _H3cLIStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3)
)
if mibBuilder.loadTexts:
    h3cLIStreamTable.setStatus("current")
_H3cLIStreamEntry_Object = MibTableRow
h3cLIStreamEntry = _H3cLIStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1)
)
h3cLIStreamEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LI-MIB", "h3cLIMediationIndex"),
    (0, "A3COM-HUAWEI-LI-MIB", "h3cLIStreamIndex"),
)
if mibBuilder.loadTexts:
    h3cLIStreamEntry.setStatus("current")


class _H3cLIStreamIndex_Type(Integer32):
    """Custom type h3cLIStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cLIStreamIndex_Type.__name__ = "Integer32"
_H3cLIStreamIndex_Object = MibTableColumn
h3cLIStreamIndex = _H3cLIStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 1),
    _H3cLIStreamIndex_Type()
)
h3cLIStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cLIStreamIndex.setStatus("current")


class _H3cLIStreamtype_Type(Integer32):
    """Custom type h3cLIStreamtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2),
          ("userConnection", 3))
    )


_H3cLIStreamtype_Type.__name__ = "Integer32"
_H3cLIStreamtype_Object = MibTableColumn
h3cLIStreamtype = _H3cLIStreamtype_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 2),
    _H3cLIStreamtype_Type()
)
h3cLIStreamtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIStreamtype.setStatus("current")


class _H3cLIStreamEnable_Type(TruthValue):
    """Custom type h3cLIStreamEnable based on TruthValue"""


_H3cLIStreamEnable_Object = MibTableColumn
h3cLIStreamEnable = _H3cLIStreamEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 3),
    _H3cLIStreamEnable_Type()
)
h3cLIStreamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIStreamEnable.setStatus("current")
_H3cLIStreamPackets_Type = Counter32
_H3cLIStreamPackets_Object = MibTableColumn
h3cLIStreamPackets = _H3cLIStreamPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 4),
    _H3cLIStreamPackets_Type()
)
h3cLIStreamPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLIStreamPackets.setStatus("current")
_H3cLIStreamDrops_Type = Counter32
_H3cLIStreamDrops_Object = MibTableColumn
h3cLIStreamDrops = _H3cLIStreamDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 5),
    _H3cLIStreamDrops_Type()
)
h3cLIStreamDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLIStreamDrops.setStatus("current")
_H3cLIStreamHPackets_Type = Counter64
_H3cLIStreamHPackets_Object = MibTableColumn
h3cLIStreamHPackets = _H3cLIStreamHPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 6),
    _H3cLIStreamHPackets_Type()
)
h3cLIStreamHPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLIStreamHPackets.setStatus("current")
_H3cLIStreamHDrops_Type = Counter64
_H3cLIStreamHDrops_Object = MibTableColumn
h3cLIStreamHDrops = _H3cLIStreamHDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 7),
    _H3cLIStreamHDrops_Type()
)
h3cLIStreamHDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLIStreamHDrops.setStatus("current")
_H3cLIStreamRowStatus_Type = RowStatus
_H3cLIStreamRowStatus_Object = MibTableColumn
h3cLIStreamRowStatus = _H3cLIStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 3, 3, 1, 8),
    _H3cLIStreamRowStatus_Type()
)
h3cLIStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLIStreamRowStatus.setStatus("current")
_H3cLIIPStream_ObjectIdentity = ObjectIdentity
h3cLIIPStream = _H3cLIIPStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2)
)
_H3cLIIPStreamObjects_ObjectIdentity = ObjectIdentity
h3cLIIPStreamObjects = _H3cLIIPStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1)
)
_H3cLIIPStreamTable_Object = MibTable
h3cLIIPStreamTable = _H3cLIIPStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cLIIPStreamTable.setStatus("current")
_H3cLIIPStreamEntry_Object = MibTableRow
h3cLIIPStreamEntry = _H3cLIIPStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1)
)
h3cLIIPStreamEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LI-MIB", "h3cLIMediationIndex"),
    (0, "A3COM-HUAWEI-LI-MIB", "h3cLIStreamIndex"),
)
if mibBuilder.loadTexts:
    h3cLIIPStreamEntry.setStatus("current")
_H3cLIIPStreamInterface_Type = InterfaceIndexOrZero
_H3cLIIPStreamInterface_Object = MibTableColumn
h3cLIIPStreamInterface = _H3cLIIPStreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 1),
    _H3cLIIPStreamInterface_Type()
)
h3cLIIPStreamInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamInterface.setStatus("current")


class _H3cLIIPStreamAddrType_Type(InetAddressType):
    """Custom type h3cLIIPStreamAddrType based on InetAddressType"""


_H3cLIIPStreamAddrType_Object = MibTableColumn
h3cLIIPStreamAddrType = _H3cLIIPStreamAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 2),
    _H3cLIIPStreamAddrType_Type()
)
h3cLIIPStreamAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamAddrType.setStatus("current")


class _H3cLIIPStreamDestAddr_Type(InetAddress):
    """Custom type h3cLIIPStreamDestAddr based on InetAddress"""
    defaultHexValue = "00000000"


_H3cLIIPStreamDestAddr_Object = MibTableColumn
h3cLIIPStreamDestAddr = _H3cLIIPStreamDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 3),
    _H3cLIIPStreamDestAddr_Type()
)
h3cLIIPStreamDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamDestAddr.setStatus("current")


class _H3cLIIPStreamDestAddrLength_Type(InetAddressPrefixLength):
    """Custom type h3cLIIPStreamDestAddrLength based on InetAddressPrefixLength"""
    defaultValue = 0


_H3cLIIPStreamDestAddrLength_Object = MibTableColumn
h3cLIIPStreamDestAddrLength = _H3cLIIPStreamDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 4),
    _H3cLIIPStreamDestAddrLength_Type()
)
h3cLIIPStreamDestAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamDestAddrLength.setStatus("current")


class _H3cLIIPStreamSrcAddr_Type(InetAddress):
    """Custom type h3cLIIPStreamSrcAddr based on InetAddress"""
    defaultHexValue = "00000000"


_H3cLIIPStreamSrcAddr_Object = MibTableColumn
h3cLIIPStreamSrcAddr = _H3cLIIPStreamSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 5),
    _H3cLIIPStreamSrcAddr_Type()
)
h3cLIIPStreamSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamSrcAddr.setStatus("current")


class _H3cLIIPStreamSrcAddrLength_Type(InetAddressPrefixLength):
    """Custom type h3cLIIPStreamSrcAddrLength based on InetAddressPrefixLength"""
    defaultValue = 0


_H3cLIIPStreamSrcAddrLength_Object = MibTableColumn
h3cLIIPStreamSrcAddrLength = _H3cLIIPStreamSrcAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 6),
    _H3cLIIPStreamSrcAddrLength_Type()
)
h3cLIIPStreamSrcAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamSrcAddrLength.setStatus("current")


class _H3cLIIPStreamTosByte_Type(Integer32):
    """Custom type h3cLIIPStreamTosByte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLIIPStreamTosByte_Type.__name__ = "Integer32"
_H3cLIIPStreamTosByte_Object = MibTableColumn
h3cLIIPStreamTosByte = _H3cLIIPStreamTosByte_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 7),
    _H3cLIIPStreamTosByte_Type()
)
h3cLIIPStreamTosByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamTosByte.setStatus("current")


class _H3cLIIPStreamTosByteMask_Type(Integer32):
    """Custom type h3cLIIPStreamTosByteMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLIIPStreamTosByteMask_Type.__name__ = "Integer32"
_H3cLIIPStreamTosByteMask_Object = MibTableColumn
h3cLIIPStreamTosByteMask = _H3cLIIPStreamTosByteMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 8),
    _H3cLIIPStreamTosByteMask_Type()
)
h3cLIIPStreamTosByteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamTosByteMask.setStatus("current")


class _H3cLIIPStreamFlowId_Type(Integer32):
    """Custom type h3cLIIPStreamFlowId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_H3cLIIPStreamFlowId_Type.__name__ = "Integer32"
_H3cLIIPStreamFlowId_Object = MibTableColumn
h3cLIIPStreamFlowId = _H3cLIIPStreamFlowId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 9),
    _H3cLIIPStreamFlowId_Type()
)
h3cLIIPStreamFlowId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamFlowId.setStatus("current")


class _H3cLIIPStreamProtocol_Type(Integer32):
    """Custom type h3cLIIPStreamProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_H3cLIIPStreamProtocol_Type.__name__ = "Integer32"
_H3cLIIPStreamProtocol_Object = MibTableColumn
h3cLIIPStreamProtocol = _H3cLIIPStreamProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 10),
    _H3cLIIPStreamProtocol_Type()
)
h3cLIIPStreamProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamProtocol.setStatus("current")


class _H3cLIIPStreamDestL4PortMin_Type(InetPortNumber):
    """Custom type h3cLIIPStreamDestL4PortMin based on InetPortNumber"""
    defaultValue = 0


_H3cLIIPStreamDestL4PortMin_Object = MibTableColumn
h3cLIIPStreamDestL4PortMin = _H3cLIIPStreamDestL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 11),
    _H3cLIIPStreamDestL4PortMin_Type()
)
h3cLIIPStreamDestL4PortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamDestL4PortMin.setStatus("current")


class _H3cLIIPStreamDestL4PortMax_Type(InetPortNumber):
    """Custom type h3cLIIPStreamDestL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_H3cLIIPStreamDestL4PortMax_Object = MibTableColumn
h3cLIIPStreamDestL4PortMax = _H3cLIIPStreamDestL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 12),
    _H3cLIIPStreamDestL4PortMax_Type()
)
h3cLIIPStreamDestL4PortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamDestL4PortMax.setStatus("current")


class _H3cLIIPStreamSrcL4PortMin_Type(InetPortNumber):
    """Custom type h3cLIIPStreamSrcL4PortMin based on InetPortNumber"""
    defaultValue = 0


_H3cLIIPStreamSrcL4PortMin_Object = MibTableColumn
h3cLIIPStreamSrcL4PortMin = _H3cLIIPStreamSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 13),
    _H3cLIIPStreamSrcL4PortMin_Type()
)
h3cLIIPStreamSrcL4PortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamSrcL4PortMin.setStatus("current")


class _H3cLIIPStreamSrcL4PortMax_Type(InetPortNumber):
    """Custom type h3cLIIPStreamSrcL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_H3cLIIPStreamSrcL4PortMax_Object = MibTableColumn
h3cLIIPStreamSrcL4PortMax = _H3cLIIPStreamSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 14),
    _H3cLIIPStreamSrcL4PortMax_Type()
)
h3cLIIPStreamSrcL4PortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamSrcL4PortMax.setStatus("current")
_H3cLIIPStreamVRF_Type = SnmpAdminString
_H3cLIIPStreamVRF_Object = MibTableColumn
h3cLIIPStreamVRF = _H3cLIIPStreamVRF_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 15),
    _H3cLIIPStreamVRF_Type()
)
h3cLIIPStreamVRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIIPStreamVRF.setStatus("current")
_H3cLIIPStreamRowStatus_Type = RowStatus
_H3cLIIPStreamRowStatus_Object = MibTableColumn
h3cLIIPStreamRowStatus = _H3cLIIPStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 2, 1, 1, 1, 18),
    _H3cLIIPStreamRowStatus_Type()
)
h3cLIIPStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLIIPStreamRowStatus.setStatus("current")
_H3cLIMACStream_ObjectIdentity = ObjectIdentity
h3cLIMACStream = _H3cLIMACStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3)
)
_H3cLIMACStreamObjects_ObjectIdentity = ObjectIdentity
h3cLIMACStreamObjects = _H3cLIMACStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1)
)
_H3cLIMACStreamTable_Object = MibTable
h3cLIMACStreamTable = _H3cLIMACStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cLIMACStreamTable.setStatus("current")
_H3cLIMACStreamEntry_Object = MibTableRow
h3cLIMACStreamEntry = _H3cLIMACStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1)
)
h3cLIMACStreamEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LI-MIB", "h3cLIMediationIndex"),
    (0, "A3COM-HUAWEI-LI-MIB", "h3cLIStreamIndex"),
)
if mibBuilder.loadTexts:
    h3cLIMACStreamEntry.setStatus("current")


class _H3cLIMACStreamFields_Type(Bits):
    """Custom type h3cLIMACStreamFields based on Bits"""
    namedValues = NamedValues(
        *(("dSap", 4),
          ("dstMacAddress", 1),
          ("ethernetPid", 3),
          ("interface", 0),
          ("sSap", 5),
          ("srcMacAddress", 2))
    )

_H3cLIMACStreamFields_Type.__name__ = "Bits"
_H3cLIMACStreamFields_Object = MibTableColumn
h3cLIMACStreamFields = _H3cLIMACStreamFields_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 1),
    _H3cLIMACStreamFields_Type()
)
h3cLIMACStreamFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMACStreamFields.setStatus("current")
_H3cLIMACStreamInterface_Type = InterfaceIndexOrZero
_H3cLIMACStreamInterface_Object = MibTableColumn
h3cLIMACStreamInterface = _H3cLIMACStreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 2),
    _H3cLIMACStreamInterface_Type()
)
h3cLIMACStreamInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMACStreamInterface.setStatus("current")
_H3cLIMACStreamDestAddr_Type = MacAddress
_H3cLIMACStreamDestAddr_Object = MibTableColumn
h3cLIMACStreamDestAddr = _H3cLIMACStreamDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 3),
    _H3cLIMACStreamDestAddr_Type()
)
h3cLIMACStreamDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMACStreamDestAddr.setStatus("current")
_H3cLIMACStreamSrcAddr_Type = MacAddress
_H3cLIMACStreamSrcAddr_Object = MibTableColumn
h3cLIMACStreamSrcAddr = _H3cLIMACStreamSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 4),
    _H3cLIMACStreamSrcAddr_Type()
)
h3cLIMACStreamSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMACStreamSrcAddr.setStatus("current")
_H3cLIMACStreamEthPid_Type = Unsigned32
_H3cLIMACStreamEthPid_Object = MibTableColumn
h3cLIMACStreamEthPid = _H3cLIMACStreamEthPid_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 5),
    _H3cLIMACStreamEthPid_Type()
)
h3cLIMACStreamEthPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMACStreamEthPid.setStatus("current")
_H3cLIMACStreamDSap_Type = Unsigned32
_H3cLIMACStreamDSap_Object = MibTableColumn
h3cLIMACStreamDSap = _H3cLIMACStreamDSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 6),
    _H3cLIMACStreamDSap_Type()
)
h3cLIMACStreamDSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMACStreamDSap.setStatus("current")
_H3cLIMACStreamSSap_Type = Unsigned32
_H3cLIMACStreamSSap_Object = MibTableColumn
h3cLIMACStreamSSap = _H3cLIMACStreamSSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 7),
    _H3cLIMACStreamSSap_Type()
)
h3cLIMACStreamSSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIMACStreamSSap.setStatus("current")
_H3cLIMACStreamRowStatus_Type = RowStatus
_H3cLIMACStreamRowStatus_Object = MibTableColumn
h3cLIMACStreamRowStatus = _H3cLIMACStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 3, 1, 1, 1, 8),
    _H3cLIMACStreamRowStatus_Type()
)
h3cLIMACStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLIMACStreamRowStatus.setStatus("current")
_H3cLIUserStream_ObjectIdentity = ObjectIdentity
h3cLIUserStream = _H3cLIUserStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4)
)
_H3cLIUserStreamObjects_ObjectIdentity = ObjectIdentity
h3cLIUserStreamObjects = _H3cLIUserStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4, 1)
)
_H3cLIUserStreamTable_Object = MibTable
h3cLIUserStreamTable = _H3cLIUserStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4, 1, 1)
)
if mibBuilder.loadTexts:
    h3cLIUserStreamTable.setStatus("current")
_H3cLIUserStreamEntry_Object = MibTableRow
h3cLIUserStreamEntry = _H3cLIUserStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4, 1, 1, 1)
)
h3cLIUserStreamEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LI-MIB", "h3cLIMediationIndex"),
    (0, "A3COM-HUAWEI-LI-MIB", "h3cLIStreamIndex"),
)
if mibBuilder.loadTexts:
    h3cLIUserStreamEntry.setStatus("current")


class _H3cLIUserStreamAcctSessID_Type(OctetString):
    """Custom type h3cLIUserStreamAcctSessID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_H3cLIUserStreamAcctSessID_Type.__name__ = "OctetString"
_H3cLIUserStreamAcctSessID_Object = MibTableColumn
h3cLIUserStreamAcctSessID = _H3cLIUserStreamAcctSessID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4, 1, 1, 1, 1),
    _H3cLIUserStreamAcctSessID_Type()
)
h3cLIUserStreamAcctSessID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLIUserStreamAcctSessID.setStatus("current")
_H3cLIUserStreamRowStatus_Type = RowStatus
_H3cLIUserStreamRowStatus_Object = MibTableColumn
h3cLIUserStreamRowStatus = _H3cLIUserStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 4, 1, 1, 1, 2),
    _H3cLIUserStreamRowStatus_Type()
)
h3cLIUserStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLIUserStreamRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

h3cLIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 2, 0, 1)
)
h3cLIActive.setObjects(
    ("A3COM-HUAWEI-LI-MIB", "h3cLIStreamtype")
)
if mibBuilder.loadTexts:
    h3cLIActive.setStatus(
        "current"
    )

h3cLITimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 2, 0, 2)
)
h3cLITimeOut.setObjects(
    ("A3COM-HUAWEI-LI-MIB", "h3cLIMediationRowStatus")
)
if mibBuilder.loadTexts:
    h3cLITimeOut.setStatus(
        "current"
    )

h3cLIFailureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 111, 1, 2, 0, 3)
)
h3cLIFailureInformation.setObjects(
      *(("A3COM-HUAWEI-LI-MIB", "h3cLIStreamtype"),
        ("A3COM-HUAWEI-LI-MIB", "h3cLIBoardInformation"))
)
if mibBuilder.loadTexts:
    h3cLIFailureInformation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LI-MIB",
    **{"h3cLI": h3cLI,
       "h3cLICommon": h3cLICommon,
       "h3cLITrapBindObjects": h3cLITrapBindObjects,
       "h3cLIBoardInformation": h3cLIBoardInformation,
       "h3cLINotifications": h3cLINotifications,
       "h3cLINotificationsPrefix": h3cLINotificationsPrefix,
       "h3cLIActive": h3cLIActive,
       "h3cLITimeOut": h3cLITimeOut,
       "h3cLIFailureInformation": h3cLIFailureInformation,
       "h3cLIObjects": h3cLIObjects,
       "h3cLINewIndex": h3cLINewIndex,
       "h3cLIMediationTable": h3cLIMediationTable,
       "h3cLIMediationEntry": h3cLIMediationEntry,
       "h3cLIMediationIndex": h3cLIMediationIndex,
       "h3cLIMediationDestAddrType": h3cLIMediationDestAddrType,
       "h3cLIMediationDestAddr": h3cLIMediationDestAddr,
       "h3cLIMediationDestPort": h3cLIMediationDestPort,
       "h3cLIMediationSrcInterface": h3cLIMediationSrcInterface,
       "h3cLIMediationDscp": h3cLIMediationDscp,
       "h3cLIMediationTimeOut": h3cLIMediationTimeOut,
       "h3cLIMediationTransport": h3cLIMediationTransport,
       "h3cLIMediationNotificationEnable": h3cLIMediationNotificationEnable,
       "h3cLIMediationRowStatus": h3cLIMediationRowStatus,
       "h3cLIStreamTable": h3cLIStreamTable,
       "h3cLIStreamEntry": h3cLIStreamEntry,
       "h3cLIStreamIndex": h3cLIStreamIndex,
       "h3cLIStreamtype": h3cLIStreamtype,
       "h3cLIStreamEnable": h3cLIStreamEnable,
       "h3cLIStreamPackets": h3cLIStreamPackets,
       "h3cLIStreamDrops": h3cLIStreamDrops,
       "h3cLIStreamHPackets": h3cLIStreamHPackets,
       "h3cLIStreamHDrops": h3cLIStreamHDrops,
       "h3cLIStreamRowStatus": h3cLIStreamRowStatus,
       "h3cLIIPStream": h3cLIIPStream,
       "h3cLIIPStreamObjects": h3cLIIPStreamObjects,
       "h3cLIIPStreamTable": h3cLIIPStreamTable,
       "h3cLIIPStreamEntry": h3cLIIPStreamEntry,
       "h3cLIIPStreamInterface": h3cLIIPStreamInterface,
       "h3cLIIPStreamAddrType": h3cLIIPStreamAddrType,
       "h3cLIIPStreamDestAddr": h3cLIIPStreamDestAddr,
       "h3cLIIPStreamDestAddrLength": h3cLIIPStreamDestAddrLength,
       "h3cLIIPStreamSrcAddr": h3cLIIPStreamSrcAddr,
       "h3cLIIPStreamSrcAddrLength": h3cLIIPStreamSrcAddrLength,
       "h3cLIIPStreamTosByte": h3cLIIPStreamTosByte,
       "h3cLIIPStreamTosByteMask": h3cLIIPStreamTosByteMask,
       "h3cLIIPStreamFlowId": h3cLIIPStreamFlowId,
       "h3cLIIPStreamProtocol": h3cLIIPStreamProtocol,
       "h3cLIIPStreamDestL4PortMin": h3cLIIPStreamDestL4PortMin,
       "h3cLIIPStreamDestL4PortMax": h3cLIIPStreamDestL4PortMax,
       "h3cLIIPStreamSrcL4PortMin": h3cLIIPStreamSrcL4PortMin,
       "h3cLIIPStreamSrcL4PortMax": h3cLIIPStreamSrcL4PortMax,
       "h3cLIIPStreamVRF": h3cLIIPStreamVRF,
       "h3cLIIPStreamRowStatus": h3cLIIPStreamRowStatus,
       "h3cLIMACStream": h3cLIMACStream,
       "h3cLIMACStreamObjects": h3cLIMACStreamObjects,
       "h3cLIMACStreamTable": h3cLIMACStreamTable,
       "h3cLIMACStreamEntry": h3cLIMACStreamEntry,
       "h3cLIMACStreamFields": h3cLIMACStreamFields,
       "h3cLIMACStreamInterface": h3cLIMACStreamInterface,
       "h3cLIMACStreamDestAddr": h3cLIMACStreamDestAddr,
       "h3cLIMACStreamSrcAddr": h3cLIMACStreamSrcAddr,
       "h3cLIMACStreamEthPid": h3cLIMACStreamEthPid,
       "h3cLIMACStreamDSap": h3cLIMACStreamDSap,
       "h3cLIMACStreamSSap": h3cLIMACStreamSSap,
       "h3cLIMACStreamRowStatus": h3cLIMACStreamRowStatus,
       "h3cLIUserStream": h3cLIUserStream,
       "h3cLIUserStreamObjects": h3cLIUserStreamObjects,
       "h3cLIUserStreamTable": h3cLIUserStreamTable,
       "h3cLIUserStreamEntry": h3cLIUserStreamEntry,
       "h3cLIUserStreamAcctSessID": h3cLIUserStreamAcctSessID,
       "h3cLIUserStreamRowStatus": h3cLIUserStreamRowStatus}
)
