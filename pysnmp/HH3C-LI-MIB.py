# SNMP MIB module (HH3C-LI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:47 2024
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

hh3cLI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111)
)
hh3cLI.setRevisions(
        ("2009-08-25 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLICommon_ObjectIdentity = ObjectIdentity
hh3cLICommon = _Hh3cLICommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1)
)
_Hh3cLITrapBindObjects_ObjectIdentity = ObjectIdentity
hh3cLITrapBindObjects = _Hh3cLITrapBindObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 1)
)
_Hh3cLIBoardInformation_Type = Unsigned32
_Hh3cLIBoardInformation_Object = MibScalar
hh3cLIBoardInformation = _Hh3cLIBoardInformation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 1, 1),
    _Hh3cLIBoardInformation_Type()
)
hh3cLIBoardInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLIBoardInformation.setStatus("current")
_Hh3cLINotifications_ObjectIdentity = ObjectIdentity
hh3cLINotifications = _Hh3cLINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 2)
)
_Hh3cLINotificationsPrefix_ObjectIdentity = ObjectIdentity
hh3cLINotificationsPrefix = _Hh3cLINotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 2, 0)
)
_Hh3cLIObjects_ObjectIdentity = ObjectIdentity
hh3cLIObjects = _Hh3cLIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3)
)


class _Hh3cLINewIndex_Type(Integer32):
    """Custom type hh3cLINewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cLINewIndex_Type.__name__ = "Integer32"
_Hh3cLINewIndex_Object = MibScalar
hh3cLINewIndex = _Hh3cLINewIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 1),
    _Hh3cLINewIndex_Type()
)
hh3cLINewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLINewIndex.setStatus("current")
_Hh3cLIMediationTable_Object = MibTable
hh3cLIMediationTable = _Hh3cLIMediationTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cLIMediationTable.setStatus("current")
_Hh3cLIMediationEntry_Object = MibTableRow
hh3cLIMediationEntry = _Hh3cLIMediationEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1)
)
hh3cLIMediationEntry.setIndexNames(
    (0, "HH3C-LI-MIB", "hh3cLIMediationIndex"),
)
if mibBuilder.loadTexts:
    hh3cLIMediationEntry.setStatus("current")


class _Hh3cLIMediationIndex_Type(Integer32):
    """Custom type hh3cLIMediationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cLIMediationIndex_Type.__name__ = "Integer32"
_Hh3cLIMediationIndex_Object = MibTableColumn
hh3cLIMediationIndex = _Hh3cLIMediationIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 1),
    _Hh3cLIMediationIndex_Type()
)
hh3cLIMediationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cLIMediationIndex.setStatus("current")
_Hh3cLIMediationDestAddrType_Type = InetAddressType
_Hh3cLIMediationDestAddrType_Object = MibTableColumn
hh3cLIMediationDestAddrType = _Hh3cLIMediationDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 2),
    _Hh3cLIMediationDestAddrType_Type()
)
hh3cLIMediationDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMediationDestAddrType.setStatus("current")
_Hh3cLIMediationDestAddr_Type = InetAddress
_Hh3cLIMediationDestAddr_Object = MibTableColumn
hh3cLIMediationDestAddr = _Hh3cLIMediationDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 3),
    _Hh3cLIMediationDestAddr_Type()
)
hh3cLIMediationDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMediationDestAddr.setStatus("current")
_Hh3cLIMediationDestPort_Type = InetPortNumber
_Hh3cLIMediationDestPort_Object = MibTableColumn
hh3cLIMediationDestPort = _Hh3cLIMediationDestPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 4),
    _Hh3cLIMediationDestPort_Type()
)
hh3cLIMediationDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMediationDestPort.setStatus("current")
_Hh3cLIMediationSrcInterface_Type = InterfaceIndexOrZero
_Hh3cLIMediationSrcInterface_Object = MibTableColumn
hh3cLIMediationSrcInterface = _Hh3cLIMediationSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 5),
    _Hh3cLIMediationSrcInterface_Type()
)
hh3cLIMediationSrcInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMediationSrcInterface.setStatus("current")


class _Hh3cLIMediationDscp_Type(Integer32):
    """Custom type hh3cLIMediationDscp based on Integer32"""
    defaultValue = 34


_Hh3cLIMediationDscp_Object = MibTableColumn
hh3cLIMediationDscp = _Hh3cLIMediationDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 6),
    _Hh3cLIMediationDscp_Type()
)
hh3cLIMediationDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMediationDscp.setStatus("current")
_Hh3cLIMediationTimeOut_Type = DateAndTime
_Hh3cLIMediationTimeOut_Object = MibTableColumn
hh3cLIMediationTimeOut = _Hh3cLIMediationTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 7),
    _Hh3cLIMediationTimeOut_Type()
)
hh3cLIMediationTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMediationTimeOut.setStatus("current")


class _Hh3cLIMediationTransport_Type(Integer32):
    """Custom type hh3cLIMediationTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("udp", 1)
    )


_Hh3cLIMediationTransport_Type.__name__ = "Integer32"
_Hh3cLIMediationTransport_Object = MibTableColumn
hh3cLIMediationTransport = _Hh3cLIMediationTransport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 8),
    _Hh3cLIMediationTransport_Type()
)
hh3cLIMediationTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMediationTransport.setStatus("current")


class _Hh3cLIMediationNotificationEnable_Type(TruthValue):
    """Custom type hh3cLIMediationNotificationEnable based on TruthValue"""


_Hh3cLIMediationNotificationEnable_Object = MibTableColumn
hh3cLIMediationNotificationEnable = _Hh3cLIMediationNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 9),
    _Hh3cLIMediationNotificationEnable_Type()
)
hh3cLIMediationNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMediationNotificationEnable.setStatus("current")
_Hh3cLIMediationRowStatus_Type = RowStatus
_Hh3cLIMediationRowStatus_Object = MibTableColumn
hh3cLIMediationRowStatus = _Hh3cLIMediationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 10),
    _Hh3cLIMediationRowStatus_Type()
)
hh3cLIMediationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLIMediationRowStatus.setStatus("current")
_Hh3cLIStreamTable_Object = MibTable
hh3cLIStreamTable = _Hh3cLIStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cLIStreamTable.setStatus("current")
_Hh3cLIStreamEntry_Object = MibTableRow
hh3cLIStreamEntry = _Hh3cLIStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1)
)
hh3cLIStreamEntry.setIndexNames(
    (0, "HH3C-LI-MIB", "hh3cLIMediationIndex"),
    (0, "HH3C-LI-MIB", "hh3cLIStreamIndex"),
)
if mibBuilder.loadTexts:
    hh3cLIStreamEntry.setStatus("current")


class _Hh3cLIStreamIndex_Type(Integer32):
    """Custom type hh3cLIStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cLIStreamIndex_Type.__name__ = "Integer32"
_Hh3cLIStreamIndex_Object = MibTableColumn
hh3cLIStreamIndex = _Hh3cLIStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 1),
    _Hh3cLIStreamIndex_Type()
)
hh3cLIStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cLIStreamIndex.setStatus("current")


class _Hh3cLIStreamtype_Type(Integer32):
    """Custom type hh3cLIStreamtype based on Integer32"""
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


_Hh3cLIStreamtype_Type.__name__ = "Integer32"
_Hh3cLIStreamtype_Object = MibTableColumn
hh3cLIStreamtype = _Hh3cLIStreamtype_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 2),
    _Hh3cLIStreamtype_Type()
)
hh3cLIStreamtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIStreamtype.setStatus("current")


class _Hh3cLIStreamEnable_Type(TruthValue):
    """Custom type hh3cLIStreamEnable based on TruthValue"""


_Hh3cLIStreamEnable_Object = MibTableColumn
hh3cLIStreamEnable = _Hh3cLIStreamEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 3),
    _Hh3cLIStreamEnable_Type()
)
hh3cLIStreamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIStreamEnable.setStatus("current")
_Hh3cLIStreamPackets_Type = Counter32
_Hh3cLIStreamPackets_Object = MibTableColumn
hh3cLIStreamPackets = _Hh3cLIStreamPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 4),
    _Hh3cLIStreamPackets_Type()
)
hh3cLIStreamPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLIStreamPackets.setStatus("current")
_Hh3cLIStreamDrops_Type = Counter32
_Hh3cLIStreamDrops_Object = MibTableColumn
hh3cLIStreamDrops = _Hh3cLIStreamDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 5),
    _Hh3cLIStreamDrops_Type()
)
hh3cLIStreamDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLIStreamDrops.setStatus("current")
_Hh3cLIStreamHPackets_Type = Counter64
_Hh3cLIStreamHPackets_Object = MibTableColumn
hh3cLIStreamHPackets = _Hh3cLIStreamHPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 6),
    _Hh3cLIStreamHPackets_Type()
)
hh3cLIStreamHPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLIStreamHPackets.setStatus("current")
_Hh3cLIStreamHDrops_Type = Counter64
_Hh3cLIStreamHDrops_Object = MibTableColumn
hh3cLIStreamHDrops = _Hh3cLIStreamHDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 7),
    _Hh3cLIStreamHDrops_Type()
)
hh3cLIStreamHDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLIStreamHDrops.setStatus("current")
_Hh3cLIStreamRowStatus_Type = RowStatus
_Hh3cLIStreamRowStatus_Object = MibTableColumn
hh3cLIStreamRowStatus = _Hh3cLIStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 8),
    _Hh3cLIStreamRowStatus_Type()
)
hh3cLIStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLIStreamRowStatus.setStatus("current")
_Hh3cLIIPStream_ObjectIdentity = ObjectIdentity
hh3cLIIPStream = _Hh3cLIIPStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2)
)
_Hh3cLIIPStreamObjects_ObjectIdentity = ObjectIdentity
hh3cLIIPStreamObjects = _Hh3cLIIPStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1)
)
_Hh3cLIIPStreamTable_Object = MibTable
hh3cLIIPStreamTable = _Hh3cLIIPStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cLIIPStreamTable.setStatus("current")
_Hh3cLIIPStreamEntry_Object = MibTableRow
hh3cLIIPStreamEntry = _Hh3cLIIPStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1)
)
hh3cLIIPStreamEntry.setIndexNames(
    (0, "HH3C-LI-MIB", "hh3cLIMediationIndex"),
    (0, "HH3C-LI-MIB", "hh3cLIStreamIndex"),
)
if mibBuilder.loadTexts:
    hh3cLIIPStreamEntry.setStatus("current")
_Hh3cLIIPStreamInterface_Type = InterfaceIndexOrZero
_Hh3cLIIPStreamInterface_Object = MibTableColumn
hh3cLIIPStreamInterface = _Hh3cLIIPStreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 1),
    _Hh3cLIIPStreamInterface_Type()
)
hh3cLIIPStreamInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamInterface.setStatus("current")


class _Hh3cLIIPStreamAddrType_Type(InetAddressType):
    """Custom type hh3cLIIPStreamAddrType based on InetAddressType"""


_Hh3cLIIPStreamAddrType_Object = MibTableColumn
hh3cLIIPStreamAddrType = _Hh3cLIIPStreamAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 2),
    _Hh3cLIIPStreamAddrType_Type()
)
hh3cLIIPStreamAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamAddrType.setStatus("current")


class _Hh3cLIIPStreamDestAddr_Type(InetAddress):
    """Custom type hh3cLIIPStreamDestAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hh3cLIIPStreamDestAddr_Object = MibTableColumn
hh3cLIIPStreamDestAddr = _Hh3cLIIPStreamDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 3),
    _Hh3cLIIPStreamDestAddr_Type()
)
hh3cLIIPStreamDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamDestAddr.setStatus("current")


class _Hh3cLIIPStreamDestAddrLength_Type(InetAddressPrefixLength):
    """Custom type hh3cLIIPStreamDestAddrLength based on InetAddressPrefixLength"""
    defaultValue = 0


_Hh3cLIIPStreamDestAddrLength_Object = MibTableColumn
hh3cLIIPStreamDestAddrLength = _Hh3cLIIPStreamDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 4),
    _Hh3cLIIPStreamDestAddrLength_Type()
)
hh3cLIIPStreamDestAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamDestAddrLength.setStatus("current")


class _Hh3cLIIPStreamSrcAddr_Type(InetAddress):
    """Custom type hh3cLIIPStreamSrcAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hh3cLIIPStreamSrcAddr_Object = MibTableColumn
hh3cLIIPStreamSrcAddr = _Hh3cLIIPStreamSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 5),
    _Hh3cLIIPStreamSrcAddr_Type()
)
hh3cLIIPStreamSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamSrcAddr.setStatus("current")


class _Hh3cLIIPStreamSrcAddrLength_Type(InetAddressPrefixLength):
    """Custom type hh3cLIIPStreamSrcAddrLength based on InetAddressPrefixLength"""
    defaultValue = 0


_Hh3cLIIPStreamSrcAddrLength_Object = MibTableColumn
hh3cLIIPStreamSrcAddrLength = _Hh3cLIIPStreamSrcAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 6),
    _Hh3cLIIPStreamSrcAddrLength_Type()
)
hh3cLIIPStreamSrcAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamSrcAddrLength.setStatus("current")


class _Hh3cLIIPStreamTosByte_Type(Integer32):
    """Custom type hh3cLIIPStreamTosByte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLIIPStreamTosByte_Type.__name__ = "Integer32"
_Hh3cLIIPStreamTosByte_Object = MibTableColumn
hh3cLIIPStreamTosByte = _Hh3cLIIPStreamTosByte_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 7),
    _Hh3cLIIPStreamTosByte_Type()
)
hh3cLIIPStreamTosByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamTosByte.setStatus("current")


class _Hh3cLIIPStreamTosByteMask_Type(Integer32):
    """Custom type hh3cLIIPStreamTosByteMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cLIIPStreamTosByteMask_Type.__name__ = "Integer32"
_Hh3cLIIPStreamTosByteMask_Object = MibTableColumn
hh3cLIIPStreamTosByteMask = _Hh3cLIIPStreamTosByteMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 8),
    _Hh3cLIIPStreamTosByteMask_Type()
)
hh3cLIIPStreamTosByteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamTosByteMask.setStatus("current")


class _Hh3cLIIPStreamFlowId_Type(Integer32):
    """Custom type hh3cLIIPStreamFlowId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_Hh3cLIIPStreamFlowId_Type.__name__ = "Integer32"
_Hh3cLIIPStreamFlowId_Object = MibTableColumn
hh3cLIIPStreamFlowId = _Hh3cLIIPStreamFlowId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 9),
    _Hh3cLIIPStreamFlowId_Type()
)
hh3cLIIPStreamFlowId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamFlowId.setStatus("current")


class _Hh3cLIIPStreamProtocol_Type(Integer32):
    """Custom type hh3cLIIPStreamProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_Hh3cLIIPStreamProtocol_Type.__name__ = "Integer32"
_Hh3cLIIPStreamProtocol_Object = MibTableColumn
hh3cLIIPStreamProtocol = _Hh3cLIIPStreamProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 10),
    _Hh3cLIIPStreamProtocol_Type()
)
hh3cLIIPStreamProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamProtocol.setStatus("current")


class _Hh3cLIIPStreamDestL4PortMin_Type(InetPortNumber):
    """Custom type hh3cLIIPStreamDestL4PortMin based on InetPortNumber"""
    defaultValue = 0


_Hh3cLIIPStreamDestL4PortMin_Object = MibTableColumn
hh3cLIIPStreamDestL4PortMin = _Hh3cLIIPStreamDestL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 11),
    _Hh3cLIIPStreamDestL4PortMin_Type()
)
hh3cLIIPStreamDestL4PortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamDestL4PortMin.setStatus("current")


class _Hh3cLIIPStreamDestL4PortMax_Type(InetPortNumber):
    """Custom type hh3cLIIPStreamDestL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_Hh3cLIIPStreamDestL4PortMax_Object = MibTableColumn
hh3cLIIPStreamDestL4PortMax = _Hh3cLIIPStreamDestL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 12),
    _Hh3cLIIPStreamDestL4PortMax_Type()
)
hh3cLIIPStreamDestL4PortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamDestL4PortMax.setStatus("current")


class _Hh3cLIIPStreamSrcL4PortMin_Type(InetPortNumber):
    """Custom type hh3cLIIPStreamSrcL4PortMin based on InetPortNumber"""
    defaultValue = 0


_Hh3cLIIPStreamSrcL4PortMin_Object = MibTableColumn
hh3cLIIPStreamSrcL4PortMin = _Hh3cLIIPStreamSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 13),
    _Hh3cLIIPStreamSrcL4PortMin_Type()
)
hh3cLIIPStreamSrcL4PortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamSrcL4PortMin.setStatus("current")


class _Hh3cLIIPStreamSrcL4PortMax_Type(InetPortNumber):
    """Custom type hh3cLIIPStreamSrcL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_Hh3cLIIPStreamSrcL4PortMax_Object = MibTableColumn
hh3cLIIPStreamSrcL4PortMax = _Hh3cLIIPStreamSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 14),
    _Hh3cLIIPStreamSrcL4PortMax_Type()
)
hh3cLIIPStreamSrcL4PortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamSrcL4PortMax.setStatus("current")
_Hh3cLIIPStreamVRF_Type = SnmpAdminString
_Hh3cLIIPStreamVRF_Object = MibTableColumn
hh3cLIIPStreamVRF = _Hh3cLIIPStreamVRF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 15),
    _Hh3cLIIPStreamVRF_Type()
)
hh3cLIIPStreamVRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIIPStreamVRF.setStatus("current")
_Hh3cLIIPStreamRowStatus_Type = RowStatus
_Hh3cLIIPStreamRowStatus_Object = MibTableColumn
hh3cLIIPStreamRowStatus = _Hh3cLIIPStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 18),
    _Hh3cLIIPStreamRowStatus_Type()
)
hh3cLIIPStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLIIPStreamRowStatus.setStatus("current")
_Hh3cLIMACStream_ObjectIdentity = ObjectIdentity
hh3cLIMACStream = _Hh3cLIMACStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3)
)
_Hh3cLIMACStreamObjects_ObjectIdentity = ObjectIdentity
hh3cLIMACStreamObjects = _Hh3cLIMACStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1)
)
_Hh3cLIMACStreamTable_Object = MibTable
hh3cLIMACStreamTable = _Hh3cLIMACStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cLIMACStreamTable.setStatus("current")
_Hh3cLIMACStreamEntry_Object = MibTableRow
hh3cLIMACStreamEntry = _Hh3cLIMACStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1)
)
hh3cLIMACStreamEntry.setIndexNames(
    (0, "HH3C-LI-MIB", "hh3cLIMediationIndex"),
    (0, "HH3C-LI-MIB", "hh3cLIStreamIndex"),
)
if mibBuilder.loadTexts:
    hh3cLIMACStreamEntry.setStatus("current")


class _Hh3cLIMACStreamFields_Type(Bits):
    """Custom type hh3cLIMACStreamFields based on Bits"""
    namedValues = NamedValues(
        *(("dSap", 4),
          ("dstMacAddress", 1),
          ("ethernetPid", 3),
          ("interface", 0),
          ("sSap", 5),
          ("srcMacAddress", 2))
    )

_Hh3cLIMACStreamFields_Type.__name__ = "Bits"
_Hh3cLIMACStreamFields_Object = MibTableColumn
hh3cLIMACStreamFields = _Hh3cLIMACStreamFields_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 1),
    _Hh3cLIMACStreamFields_Type()
)
hh3cLIMACStreamFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMACStreamFields.setStatus("current")
_Hh3cLIMACStreamInterface_Type = InterfaceIndexOrZero
_Hh3cLIMACStreamInterface_Object = MibTableColumn
hh3cLIMACStreamInterface = _Hh3cLIMACStreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 2),
    _Hh3cLIMACStreamInterface_Type()
)
hh3cLIMACStreamInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMACStreamInterface.setStatus("current")
_Hh3cLIMACStreamDestAddr_Type = MacAddress
_Hh3cLIMACStreamDestAddr_Object = MibTableColumn
hh3cLIMACStreamDestAddr = _Hh3cLIMACStreamDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 3),
    _Hh3cLIMACStreamDestAddr_Type()
)
hh3cLIMACStreamDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMACStreamDestAddr.setStatus("current")
_Hh3cLIMACStreamSrcAddr_Type = MacAddress
_Hh3cLIMACStreamSrcAddr_Object = MibTableColumn
hh3cLIMACStreamSrcAddr = _Hh3cLIMACStreamSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 4),
    _Hh3cLIMACStreamSrcAddr_Type()
)
hh3cLIMACStreamSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMACStreamSrcAddr.setStatus("current")
_Hh3cLIMACStreamEthPid_Type = Unsigned32
_Hh3cLIMACStreamEthPid_Object = MibTableColumn
hh3cLIMACStreamEthPid = _Hh3cLIMACStreamEthPid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 5),
    _Hh3cLIMACStreamEthPid_Type()
)
hh3cLIMACStreamEthPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMACStreamEthPid.setStatus("current")
_Hh3cLIMACStreamDSap_Type = Unsigned32
_Hh3cLIMACStreamDSap_Object = MibTableColumn
hh3cLIMACStreamDSap = _Hh3cLIMACStreamDSap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 6),
    _Hh3cLIMACStreamDSap_Type()
)
hh3cLIMACStreamDSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMACStreamDSap.setStatus("current")
_Hh3cLIMACStreamSSap_Type = Unsigned32
_Hh3cLIMACStreamSSap_Object = MibTableColumn
hh3cLIMACStreamSSap = _Hh3cLIMACStreamSSap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 7),
    _Hh3cLIMACStreamSSap_Type()
)
hh3cLIMACStreamSSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIMACStreamSSap.setStatus("current")
_Hh3cLIMACStreamRowStatus_Type = RowStatus
_Hh3cLIMACStreamRowStatus_Object = MibTableColumn
hh3cLIMACStreamRowStatus = _Hh3cLIMACStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 8),
    _Hh3cLIMACStreamRowStatus_Type()
)
hh3cLIMACStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLIMACStreamRowStatus.setStatus("current")
_Hh3cLIUserStream_ObjectIdentity = ObjectIdentity
hh3cLIUserStream = _Hh3cLIUserStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 4)
)
_Hh3cLIUserStreamObjects_ObjectIdentity = ObjectIdentity
hh3cLIUserStreamObjects = _Hh3cLIUserStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 4, 1)
)
_Hh3cLIUserStreamTable_Object = MibTable
hh3cLIUserStreamTable = _Hh3cLIUserStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cLIUserStreamTable.setStatus("current")
_Hh3cLIUserStreamEntry_Object = MibTableRow
hh3cLIUserStreamEntry = _Hh3cLIUserStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 4, 1, 1, 1)
)
hh3cLIUserStreamEntry.setIndexNames(
    (0, "HH3C-LI-MIB", "hh3cLIMediationIndex"),
    (0, "HH3C-LI-MIB", "hh3cLIStreamIndex"),
)
if mibBuilder.loadTexts:
    hh3cLIUserStreamEntry.setStatus("current")


class _Hh3cLIUserStreamAcctSessID_Type(OctetString):
    """Custom type hh3cLIUserStreamAcctSessID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_Hh3cLIUserStreamAcctSessID_Type.__name__ = "OctetString"
_Hh3cLIUserStreamAcctSessID_Object = MibTableColumn
hh3cLIUserStreamAcctSessID = _Hh3cLIUserStreamAcctSessID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 4, 1, 1, 1, 1),
    _Hh3cLIUserStreamAcctSessID_Type()
)
hh3cLIUserStreamAcctSessID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLIUserStreamAcctSessID.setStatus("current")
_Hh3cLIUserStreamRowStatus_Type = RowStatus
_Hh3cLIUserStreamRowStatus_Object = MibTableColumn
hh3cLIUserStreamRowStatus = _Hh3cLIUserStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 4, 1, 1, 1, 2),
    _Hh3cLIUserStreamRowStatus_Type()
)
hh3cLIUserStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLIUserStreamRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cLIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 2, 0, 1)
)
hh3cLIActive.setObjects(
    ("HH3C-LI-MIB", "hh3cLIStreamtype")
)
if mibBuilder.loadTexts:
    hh3cLIActive.setStatus(
        "current"
    )

hh3cLITimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 2, 0, 2)
)
hh3cLITimeOut.setObjects(
    ("HH3C-LI-MIB", "hh3cLIMediationRowStatus")
)
if mibBuilder.loadTexts:
    hh3cLITimeOut.setStatus(
        "current"
    )

hh3cLIFailureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 2, 0, 3)
)
hh3cLIFailureInformation.setObjects(
      *(("HH3C-LI-MIB", "hh3cLIStreamtype"),
        ("HH3C-LI-MIB", "hh3cLIBoardInformation"))
)
if mibBuilder.loadTexts:
    hh3cLIFailureInformation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LI-MIB",
    **{"hh3cLI": hh3cLI,
       "hh3cLICommon": hh3cLICommon,
       "hh3cLITrapBindObjects": hh3cLITrapBindObjects,
       "hh3cLIBoardInformation": hh3cLIBoardInformation,
       "hh3cLINotifications": hh3cLINotifications,
       "hh3cLINotificationsPrefix": hh3cLINotificationsPrefix,
       "hh3cLIActive": hh3cLIActive,
       "hh3cLITimeOut": hh3cLITimeOut,
       "hh3cLIFailureInformation": hh3cLIFailureInformation,
       "hh3cLIObjects": hh3cLIObjects,
       "hh3cLINewIndex": hh3cLINewIndex,
       "hh3cLIMediationTable": hh3cLIMediationTable,
       "hh3cLIMediationEntry": hh3cLIMediationEntry,
       "hh3cLIMediationIndex": hh3cLIMediationIndex,
       "hh3cLIMediationDestAddrType": hh3cLIMediationDestAddrType,
       "hh3cLIMediationDestAddr": hh3cLIMediationDestAddr,
       "hh3cLIMediationDestPort": hh3cLIMediationDestPort,
       "hh3cLIMediationSrcInterface": hh3cLIMediationSrcInterface,
       "hh3cLIMediationDscp": hh3cLIMediationDscp,
       "hh3cLIMediationTimeOut": hh3cLIMediationTimeOut,
       "hh3cLIMediationTransport": hh3cLIMediationTransport,
       "hh3cLIMediationNotificationEnable": hh3cLIMediationNotificationEnable,
       "hh3cLIMediationRowStatus": hh3cLIMediationRowStatus,
       "hh3cLIStreamTable": hh3cLIStreamTable,
       "hh3cLIStreamEntry": hh3cLIStreamEntry,
       "hh3cLIStreamIndex": hh3cLIStreamIndex,
       "hh3cLIStreamtype": hh3cLIStreamtype,
       "hh3cLIStreamEnable": hh3cLIStreamEnable,
       "hh3cLIStreamPackets": hh3cLIStreamPackets,
       "hh3cLIStreamDrops": hh3cLIStreamDrops,
       "hh3cLIStreamHPackets": hh3cLIStreamHPackets,
       "hh3cLIStreamHDrops": hh3cLIStreamHDrops,
       "hh3cLIStreamRowStatus": hh3cLIStreamRowStatus,
       "hh3cLIIPStream": hh3cLIIPStream,
       "hh3cLIIPStreamObjects": hh3cLIIPStreamObjects,
       "hh3cLIIPStreamTable": hh3cLIIPStreamTable,
       "hh3cLIIPStreamEntry": hh3cLIIPStreamEntry,
       "hh3cLIIPStreamInterface": hh3cLIIPStreamInterface,
       "hh3cLIIPStreamAddrType": hh3cLIIPStreamAddrType,
       "hh3cLIIPStreamDestAddr": hh3cLIIPStreamDestAddr,
       "hh3cLIIPStreamDestAddrLength": hh3cLIIPStreamDestAddrLength,
       "hh3cLIIPStreamSrcAddr": hh3cLIIPStreamSrcAddr,
       "hh3cLIIPStreamSrcAddrLength": hh3cLIIPStreamSrcAddrLength,
       "hh3cLIIPStreamTosByte": hh3cLIIPStreamTosByte,
       "hh3cLIIPStreamTosByteMask": hh3cLIIPStreamTosByteMask,
       "hh3cLIIPStreamFlowId": hh3cLIIPStreamFlowId,
       "hh3cLIIPStreamProtocol": hh3cLIIPStreamProtocol,
       "hh3cLIIPStreamDestL4PortMin": hh3cLIIPStreamDestL4PortMin,
       "hh3cLIIPStreamDestL4PortMax": hh3cLIIPStreamDestL4PortMax,
       "hh3cLIIPStreamSrcL4PortMin": hh3cLIIPStreamSrcL4PortMin,
       "hh3cLIIPStreamSrcL4PortMax": hh3cLIIPStreamSrcL4PortMax,
       "hh3cLIIPStreamVRF": hh3cLIIPStreamVRF,
       "hh3cLIIPStreamRowStatus": hh3cLIIPStreamRowStatus,
       "hh3cLIMACStream": hh3cLIMACStream,
       "hh3cLIMACStreamObjects": hh3cLIMACStreamObjects,
       "hh3cLIMACStreamTable": hh3cLIMACStreamTable,
       "hh3cLIMACStreamEntry": hh3cLIMACStreamEntry,
       "hh3cLIMACStreamFields": hh3cLIMACStreamFields,
       "hh3cLIMACStreamInterface": hh3cLIMACStreamInterface,
       "hh3cLIMACStreamDestAddr": hh3cLIMACStreamDestAddr,
       "hh3cLIMACStreamSrcAddr": hh3cLIMACStreamSrcAddr,
       "hh3cLIMACStreamEthPid": hh3cLIMACStreamEthPid,
       "hh3cLIMACStreamDSap": hh3cLIMACStreamDSap,
       "hh3cLIMACStreamSSap": hh3cLIMACStreamSSap,
       "hh3cLIMACStreamRowStatus": hh3cLIMACStreamRowStatus,
       "hh3cLIUserStream": hh3cLIUserStream,
       "hh3cLIUserStreamObjects": hh3cLIUserStreamObjects,
       "hh3cLIUserStreamTable": hh3cLIUserStreamTable,
       "hh3cLIUserStreamEntry": hh3cLIUserStreamEntry,
       "hh3cLIUserStreamAcctSessID": hh3cLIUserStreamAcctSessID,
       "hh3cLIUserStreamRowStatus": hh3cLIUserStreamRowStatus}
)
