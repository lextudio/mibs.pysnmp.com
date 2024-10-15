# SNMP MIB module (HPN-ICF-LI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:47 2024
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

hpnicfLI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111)
)
hpnicfLI.setRevisions(
        ("2009-08-25 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfLICommon_ObjectIdentity = ObjectIdentity
hpnicfLICommon = _HpnicfLICommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1)
)
_HpnicfLITrapBindObjects_ObjectIdentity = ObjectIdentity
hpnicfLITrapBindObjects = _HpnicfLITrapBindObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 1)
)
_HpnicfLIBoardInformation_Type = Unsigned32
_HpnicfLIBoardInformation_Object = MibScalar
hpnicfLIBoardInformation = _HpnicfLIBoardInformation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 1, 1),
    _HpnicfLIBoardInformation_Type()
)
hpnicfLIBoardInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfLIBoardInformation.setStatus("current")
_HpnicfLINotifications_ObjectIdentity = ObjectIdentity
hpnicfLINotifications = _HpnicfLINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 2)
)
_HpnicfLINotificationsPrefix_ObjectIdentity = ObjectIdentity
hpnicfLINotificationsPrefix = _HpnicfLINotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 2, 0)
)
_HpnicfLIObjects_ObjectIdentity = ObjectIdentity
hpnicfLIObjects = _HpnicfLIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3)
)


class _HpnicfLINewIndex_Type(Integer32):
    """Custom type hpnicfLINewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfLINewIndex_Type.__name__ = "Integer32"
_HpnicfLINewIndex_Object = MibScalar
hpnicfLINewIndex = _HpnicfLINewIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 1),
    _HpnicfLINewIndex_Type()
)
hpnicfLINewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLINewIndex.setStatus("current")
_HpnicfLIMediationTable_Object = MibTable
hpnicfLIMediationTable = _HpnicfLIMediationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfLIMediationTable.setStatus("current")
_HpnicfLIMediationEntry_Object = MibTableRow
hpnicfLIMediationEntry = _HpnicfLIMediationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1)
)
hpnicfLIMediationEntry.setIndexNames(
    (0, "HPN-ICF-LI-MIB", "hpnicfLIMediationIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLIMediationEntry.setStatus("current")


class _HpnicfLIMediationIndex_Type(Integer32):
    """Custom type hpnicfLIMediationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfLIMediationIndex_Type.__name__ = "Integer32"
_HpnicfLIMediationIndex_Object = MibTableColumn
hpnicfLIMediationIndex = _HpnicfLIMediationIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1, 1),
    _HpnicfLIMediationIndex_Type()
)
hpnicfLIMediationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfLIMediationIndex.setStatus("current")
_HpnicfLIMediationDestAddrType_Type = InetAddressType
_HpnicfLIMediationDestAddrType_Object = MibTableColumn
hpnicfLIMediationDestAddrType = _HpnicfLIMediationDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1, 2),
    _HpnicfLIMediationDestAddrType_Type()
)
hpnicfLIMediationDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMediationDestAddrType.setStatus("current")
_HpnicfLIMediationDestAddr_Type = InetAddress
_HpnicfLIMediationDestAddr_Object = MibTableColumn
hpnicfLIMediationDestAddr = _HpnicfLIMediationDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1, 3),
    _HpnicfLIMediationDestAddr_Type()
)
hpnicfLIMediationDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMediationDestAddr.setStatus("current")
_HpnicfLIMediationDestPort_Type = InetPortNumber
_HpnicfLIMediationDestPort_Object = MibTableColumn
hpnicfLIMediationDestPort = _HpnicfLIMediationDestPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1, 4),
    _HpnicfLIMediationDestPort_Type()
)
hpnicfLIMediationDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMediationDestPort.setStatus("current")
_HpnicfLIMediationSrcInterface_Type = InterfaceIndexOrZero
_HpnicfLIMediationSrcInterface_Object = MibTableColumn
hpnicfLIMediationSrcInterface = _HpnicfLIMediationSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1, 5),
    _HpnicfLIMediationSrcInterface_Type()
)
hpnicfLIMediationSrcInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMediationSrcInterface.setStatus("current")


class _HpnicfLIMediationDscp_Type(Integer32):
    """Custom type hpnicfLIMediationDscp based on Integer32"""
    defaultValue = 34


_HpnicfLIMediationDscp_Object = MibTableColumn
hpnicfLIMediationDscp = _HpnicfLIMediationDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1, 6),
    _HpnicfLIMediationDscp_Type()
)
hpnicfLIMediationDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMediationDscp.setStatus("current")
_HpnicfLIMediationTimeOut_Type = DateAndTime
_HpnicfLIMediationTimeOut_Object = MibTableColumn
hpnicfLIMediationTimeOut = _HpnicfLIMediationTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1, 7),
    _HpnicfLIMediationTimeOut_Type()
)
hpnicfLIMediationTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMediationTimeOut.setStatus("current")


class _HpnicfLIMediationTransport_Type(Integer32):
    """Custom type hpnicfLIMediationTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("udp", 1)
    )


_HpnicfLIMediationTransport_Type.__name__ = "Integer32"
_HpnicfLIMediationTransport_Object = MibTableColumn
hpnicfLIMediationTransport = _HpnicfLIMediationTransport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1, 8),
    _HpnicfLIMediationTransport_Type()
)
hpnicfLIMediationTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMediationTransport.setStatus("current")


class _HpnicfLIMediationNotificationEnable_Type(TruthValue):
    """Custom type hpnicfLIMediationNotificationEnable based on TruthValue"""


_HpnicfLIMediationNotificationEnable_Object = MibTableColumn
hpnicfLIMediationNotificationEnable = _HpnicfLIMediationNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1, 9),
    _HpnicfLIMediationNotificationEnable_Type()
)
hpnicfLIMediationNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMediationNotificationEnable.setStatus("current")
_HpnicfLIMediationRowStatus_Type = RowStatus
_HpnicfLIMediationRowStatus_Object = MibTableColumn
hpnicfLIMediationRowStatus = _HpnicfLIMediationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 2, 1, 10),
    _HpnicfLIMediationRowStatus_Type()
)
hpnicfLIMediationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLIMediationRowStatus.setStatus("current")
_HpnicfLIStreamTable_Object = MibTable
hpnicfLIStreamTable = _HpnicfLIStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfLIStreamTable.setStatus("current")
_HpnicfLIStreamEntry_Object = MibTableRow
hpnicfLIStreamEntry = _HpnicfLIStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 3, 1)
)
hpnicfLIStreamEntry.setIndexNames(
    (0, "HPN-ICF-LI-MIB", "hpnicfLIMediationIndex"),
    (0, "HPN-ICF-LI-MIB", "hpnicfLIStreamIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLIStreamEntry.setStatus("current")


class _HpnicfLIStreamIndex_Type(Integer32):
    """Custom type hpnicfLIStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfLIStreamIndex_Type.__name__ = "Integer32"
_HpnicfLIStreamIndex_Object = MibTableColumn
hpnicfLIStreamIndex = _HpnicfLIStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 3, 1, 1),
    _HpnicfLIStreamIndex_Type()
)
hpnicfLIStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfLIStreamIndex.setStatus("current")


class _HpnicfLIStreamtype_Type(Integer32):
    """Custom type hpnicfLIStreamtype based on Integer32"""
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


_HpnicfLIStreamtype_Type.__name__ = "Integer32"
_HpnicfLIStreamtype_Object = MibTableColumn
hpnicfLIStreamtype = _HpnicfLIStreamtype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 3, 1, 2),
    _HpnicfLIStreamtype_Type()
)
hpnicfLIStreamtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIStreamtype.setStatus("current")


class _HpnicfLIStreamEnable_Type(TruthValue):
    """Custom type hpnicfLIStreamEnable based on TruthValue"""


_HpnicfLIStreamEnable_Object = MibTableColumn
hpnicfLIStreamEnable = _HpnicfLIStreamEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 3, 1, 3),
    _HpnicfLIStreamEnable_Type()
)
hpnicfLIStreamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIStreamEnable.setStatus("current")
_HpnicfLIStreamPackets_Type = Counter32
_HpnicfLIStreamPackets_Object = MibTableColumn
hpnicfLIStreamPackets = _HpnicfLIStreamPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 3, 1, 4),
    _HpnicfLIStreamPackets_Type()
)
hpnicfLIStreamPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLIStreamPackets.setStatus("current")
_HpnicfLIStreamDrops_Type = Counter32
_HpnicfLIStreamDrops_Object = MibTableColumn
hpnicfLIStreamDrops = _HpnicfLIStreamDrops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 3, 1, 5),
    _HpnicfLIStreamDrops_Type()
)
hpnicfLIStreamDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLIStreamDrops.setStatus("current")
_HpnicfLIStreamHPackets_Type = Counter64
_HpnicfLIStreamHPackets_Object = MibTableColumn
hpnicfLIStreamHPackets = _HpnicfLIStreamHPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 3, 1, 6),
    _HpnicfLIStreamHPackets_Type()
)
hpnicfLIStreamHPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLIStreamHPackets.setStatus("current")
_HpnicfLIStreamHDrops_Type = Counter64
_HpnicfLIStreamHDrops_Object = MibTableColumn
hpnicfLIStreamHDrops = _HpnicfLIStreamHDrops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 3, 1, 7),
    _HpnicfLIStreamHDrops_Type()
)
hpnicfLIStreamHDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLIStreamHDrops.setStatus("current")
_HpnicfLIStreamRowStatus_Type = RowStatus
_HpnicfLIStreamRowStatus_Object = MibTableColumn
hpnicfLIStreamRowStatus = _HpnicfLIStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 3, 3, 1, 8),
    _HpnicfLIStreamRowStatus_Type()
)
hpnicfLIStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLIStreamRowStatus.setStatus("current")
_HpnicfLIIPStream_ObjectIdentity = ObjectIdentity
hpnicfLIIPStream = _HpnicfLIIPStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2)
)
_HpnicfLIIPStreamObjects_ObjectIdentity = ObjectIdentity
hpnicfLIIPStreamObjects = _HpnicfLIIPStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1)
)
_HpnicfLIIPStreamTable_Object = MibTable
hpnicfLIIPStreamTable = _HpnicfLIIPStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfLIIPStreamTable.setStatus("current")
_HpnicfLIIPStreamEntry_Object = MibTableRow
hpnicfLIIPStreamEntry = _HpnicfLIIPStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1)
)
hpnicfLIIPStreamEntry.setIndexNames(
    (0, "HPN-ICF-LI-MIB", "hpnicfLIMediationIndex"),
    (0, "HPN-ICF-LI-MIB", "hpnicfLIStreamIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLIIPStreamEntry.setStatus("current")
_HpnicfLIIPStreamInterface_Type = InterfaceIndexOrZero
_HpnicfLIIPStreamInterface_Object = MibTableColumn
hpnicfLIIPStreamInterface = _HpnicfLIIPStreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 1),
    _HpnicfLIIPStreamInterface_Type()
)
hpnicfLIIPStreamInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamInterface.setStatus("current")


class _HpnicfLIIPStreamAddrType_Type(InetAddressType):
    """Custom type hpnicfLIIPStreamAddrType based on InetAddressType"""


_HpnicfLIIPStreamAddrType_Object = MibTableColumn
hpnicfLIIPStreamAddrType = _HpnicfLIIPStreamAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 2),
    _HpnicfLIIPStreamAddrType_Type()
)
hpnicfLIIPStreamAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamAddrType.setStatus("current")


class _HpnicfLIIPStreamDestAddr_Type(InetAddress):
    """Custom type hpnicfLIIPStreamDestAddr based on InetAddress"""
    defaultHexValue = "00000000"


_HpnicfLIIPStreamDestAddr_Object = MibTableColumn
hpnicfLIIPStreamDestAddr = _HpnicfLIIPStreamDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 3),
    _HpnicfLIIPStreamDestAddr_Type()
)
hpnicfLIIPStreamDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamDestAddr.setStatus("current")


class _HpnicfLIIPStreamDestAddrLength_Type(InetAddressPrefixLength):
    """Custom type hpnicfLIIPStreamDestAddrLength based on InetAddressPrefixLength"""
    defaultValue = 0


_HpnicfLIIPStreamDestAddrLength_Object = MibTableColumn
hpnicfLIIPStreamDestAddrLength = _HpnicfLIIPStreamDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 4),
    _HpnicfLIIPStreamDestAddrLength_Type()
)
hpnicfLIIPStreamDestAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamDestAddrLength.setStatus("current")


class _HpnicfLIIPStreamSrcAddr_Type(InetAddress):
    """Custom type hpnicfLIIPStreamSrcAddr based on InetAddress"""
    defaultHexValue = "00000000"


_HpnicfLIIPStreamSrcAddr_Object = MibTableColumn
hpnicfLIIPStreamSrcAddr = _HpnicfLIIPStreamSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 5),
    _HpnicfLIIPStreamSrcAddr_Type()
)
hpnicfLIIPStreamSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamSrcAddr.setStatus("current")


class _HpnicfLIIPStreamSrcAddrLength_Type(InetAddressPrefixLength):
    """Custom type hpnicfLIIPStreamSrcAddrLength based on InetAddressPrefixLength"""
    defaultValue = 0


_HpnicfLIIPStreamSrcAddrLength_Object = MibTableColumn
hpnicfLIIPStreamSrcAddrLength = _HpnicfLIIPStreamSrcAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 6),
    _HpnicfLIIPStreamSrcAddrLength_Type()
)
hpnicfLIIPStreamSrcAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamSrcAddrLength.setStatus("current")


class _HpnicfLIIPStreamTosByte_Type(Integer32):
    """Custom type hpnicfLIIPStreamTosByte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLIIPStreamTosByte_Type.__name__ = "Integer32"
_HpnicfLIIPStreamTosByte_Object = MibTableColumn
hpnicfLIIPStreamTosByte = _HpnicfLIIPStreamTosByte_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 7),
    _HpnicfLIIPStreamTosByte_Type()
)
hpnicfLIIPStreamTosByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamTosByte.setStatus("current")


class _HpnicfLIIPStreamTosByteMask_Type(Integer32):
    """Custom type hpnicfLIIPStreamTosByteMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfLIIPStreamTosByteMask_Type.__name__ = "Integer32"
_HpnicfLIIPStreamTosByteMask_Object = MibTableColumn
hpnicfLIIPStreamTosByteMask = _HpnicfLIIPStreamTosByteMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 8),
    _HpnicfLIIPStreamTosByteMask_Type()
)
hpnicfLIIPStreamTosByteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamTosByteMask.setStatus("current")


class _HpnicfLIIPStreamFlowId_Type(Integer32):
    """Custom type hpnicfLIIPStreamFlowId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_HpnicfLIIPStreamFlowId_Type.__name__ = "Integer32"
_HpnicfLIIPStreamFlowId_Object = MibTableColumn
hpnicfLIIPStreamFlowId = _HpnicfLIIPStreamFlowId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 9),
    _HpnicfLIIPStreamFlowId_Type()
)
hpnicfLIIPStreamFlowId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamFlowId.setStatus("current")


class _HpnicfLIIPStreamProtocol_Type(Integer32):
    """Custom type hpnicfLIIPStreamProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_HpnicfLIIPStreamProtocol_Type.__name__ = "Integer32"
_HpnicfLIIPStreamProtocol_Object = MibTableColumn
hpnicfLIIPStreamProtocol = _HpnicfLIIPStreamProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 10),
    _HpnicfLIIPStreamProtocol_Type()
)
hpnicfLIIPStreamProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamProtocol.setStatus("current")


class _HpnicfLIIPStreamDestL4PortMin_Type(InetPortNumber):
    """Custom type hpnicfLIIPStreamDestL4PortMin based on InetPortNumber"""
    defaultValue = 0


_HpnicfLIIPStreamDestL4PortMin_Object = MibTableColumn
hpnicfLIIPStreamDestL4PortMin = _HpnicfLIIPStreamDestL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 11),
    _HpnicfLIIPStreamDestL4PortMin_Type()
)
hpnicfLIIPStreamDestL4PortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamDestL4PortMin.setStatus("current")


class _HpnicfLIIPStreamDestL4PortMax_Type(InetPortNumber):
    """Custom type hpnicfLIIPStreamDestL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_HpnicfLIIPStreamDestL4PortMax_Object = MibTableColumn
hpnicfLIIPStreamDestL4PortMax = _HpnicfLIIPStreamDestL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 12),
    _HpnicfLIIPStreamDestL4PortMax_Type()
)
hpnicfLIIPStreamDestL4PortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamDestL4PortMax.setStatus("current")


class _HpnicfLIIPStreamSrcL4PortMin_Type(InetPortNumber):
    """Custom type hpnicfLIIPStreamSrcL4PortMin based on InetPortNumber"""
    defaultValue = 0


_HpnicfLIIPStreamSrcL4PortMin_Object = MibTableColumn
hpnicfLIIPStreamSrcL4PortMin = _HpnicfLIIPStreamSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 13),
    _HpnicfLIIPStreamSrcL4PortMin_Type()
)
hpnicfLIIPStreamSrcL4PortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamSrcL4PortMin.setStatus("current")


class _HpnicfLIIPStreamSrcL4PortMax_Type(InetPortNumber):
    """Custom type hpnicfLIIPStreamSrcL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_HpnicfLIIPStreamSrcL4PortMax_Object = MibTableColumn
hpnicfLIIPStreamSrcL4PortMax = _HpnicfLIIPStreamSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 14),
    _HpnicfLIIPStreamSrcL4PortMax_Type()
)
hpnicfLIIPStreamSrcL4PortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamSrcL4PortMax.setStatus("current")
_HpnicfLIIPStreamVRF_Type = SnmpAdminString
_HpnicfLIIPStreamVRF_Object = MibTableColumn
hpnicfLIIPStreamVRF = _HpnicfLIIPStreamVRF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 15),
    _HpnicfLIIPStreamVRF_Type()
)
hpnicfLIIPStreamVRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamVRF.setStatus("current")
_HpnicfLIIPStreamRowStatus_Type = RowStatus
_HpnicfLIIPStreamRowStatus_Object = MibTableColumn
hpnicfLIIPStreamRowStatus = _HpnicfLIIPStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 2, 1, 1, 1, 18),
    _HpnicfLIIPStreamRowStatus_Type()
)
hpnicfLIIPStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLIIPStreamRowStatus.setStatus("current")
_HpnicfLIMACStream_ObjectIdentity = ObjectIdentity
hpnicfLIMACStream = _HpnicfLIMACStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3)
)
_HpnicfLIMACStreamObjects_ObjectIdentity = ObjectIdentity
hpnicfLIMACStreamObjects = _HpnicfLIMACStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1)
)
_HpnicfLIMACStreamTable_Object = MibTable
hpnicfLIMACStreamTable = _HpnicfLIMACStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfLIMACStreamTable.setStatus("current")
_HpnicfLIMACStreamEntry_Object = MibTableRow
hpnicfLIMACStreamEntry = _HpnicfLIMACStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1, 1, 1)
)
hpnicfLIMACStreamEntry.setIndexNames(
    (0, "HPN-ICF-LI-MIB", "hpnicfLIMediationIndex"),
    (0, "HPN-ICF-LI-MIB", "hpnicfLIStreamIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLIMACStreamEntry.setStatus("current")


class _HpnicfLIMACStreamFields_Type(Bits):
    """Custom type hpnicfLIMACStreamFields based on Bits"""
    namedValues = NamedValues(
        *(("dSap", 4),
          ("dstMacAddress", 1),
          ("ethernetPid", 3),
          ("interface", 0),
          ("sSap", 5),
          ("srcMacAddress", 2))
    )

_HpnicfLIMACStreamFields_Type.__name__ = "Bits"
_HpnicfLIMACStreamFields_Object = MibTableColumn
hpnicfLIMACStreamFields = _HpnicfLIMACStreamFields_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1, 1, 1, 1),
    _HpnicfLIMACStreamFields_Type()
)
hpnicfLIMACStreamFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMACStreamFields.setStatus("current")
_HpnicfLIMACStreamInterface_Type = InterfaceIndexOrZero
_HpnicfLIMACStreamInterface_Object = MibTableColumn
hpnicfLIMACStreamInterface = _HpnicfLIMACStreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1, 1, 1, 2),
    _HpnicfLIMACStreamInterface_Type()
)
hpnicfLIMACStreamInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMACStreamInterface.setStatus("current")
_HpnicfLIMACStreamDestAddr_Type = MacAddress
_HpnicfLIMACStreamDestAddr_Object = MibTableColumn
hpnicfLIMACStreamDestAddr = _HpnicfLIMACStreamDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1, 1, 1, 3),
    _HpnicfLIMACStreamDestAddr_Type()
)
hpnicfLIMACStreamDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMACStreamDestAddr.setStatus("current")
_HpnicfLIMACStreamSrcAddr_Type = MacAddress
_HpnicfLIMACStreamSrcAddr_Object = MibTableColumn
hpnicfLIMACStreamSrcAddr = _HpnicfLIMACStreamSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1, 1, 1, 4),
    _HpnicfLIMACStreamSrcAddr_Type()
)
hpnicfLIMACStreamSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMACStreamSrcAddr.setStatus("current")
_HpnicfLIMACStreamEthPid_Type = Unsigned32
_HpnicfLIMACStreamEthPid_Object = MibTableColumn
hpnicfLIMACStreamEthPid = _HpnicfLIMACStreamEthPid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1, 1, 1, 5),
    _HpnicfLIMACStreamEthPid_Type()
)
hpnicfLIMACStreamEthPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMACStreamEthPid.setStatus("current")
_HpnicfLIMACStreamDSap_Type = Unsigned32
_HpnicfLIMACStreamDSap_Object = MibTableColumn
hpnicfLIMACStreamDSap = _HpnicfLIMACStreamDSap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1, 1, 1, 6),
    _HpnicfLIMACStreamDSap_Type()
)
hpnicfLIMACStreamDSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMACStreamDSap.setStatus("current")
_HpnicfLIMACStreamSSap_Type = Unsigned32
_HpnicfLIMACStreamSSap_Object = MibTableColumn
hpnicfLIMACStreamSSap = _HpnicfLIMACStreamSSap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1, 1, 1, 7),
    _HpnicfLIMACStreamSSap_Type()
)
hpnicfLIMACStreamSSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIMACStreamSSap.setStatus("current")
_HpnicfLIMACStreamRowStatus_Type = RowStatus
_HpnicfLIMACStreamRowStatus_Object = MibTableColumn
hpnicfLIMACStreamRowStatus = _HpnicfLIMACStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 3, 1, 1, 1, 8),
    _HpnicfLIMACStreamRowStatus_Type()
)
hpnicfLIMACStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLIMACStreamRowStatus.setStatus("current")
_HpnicfLIUserStream_ObjectIdentity = ObjectIdentity
hpnicfLIUserStream = _HpnicfLIUserStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 4)
)
_HpnicfLIUserStreamObjects_ObjectIdentity = ObjectIdentity
hpnicfLIUserStreamObjects = _HpnicfLIUserStreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 4, 1)
)
_HpnicfLIUserStreamTable_Object = MibTable
hpnicfLIUserStreamTable = _HpnicfLIUserStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfLIUserStreamTable.setStatus("current")
_HpnicfLIUserStreamEntry_Object = MibTableRow
hpnicfLIUserStreamEntry = _HpnicfLIUserStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 4, 1, 1, 1)
)
hpnicfLIUserStreamEntry.setIndexNames(
    (0, "HPN-ICF-LI-MIB", "hpnicfLIMediationIndex"),
    (0, "HPN-ICF-LI-MIB", "hpnicfLIStreamIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLIUserStreamEntry.setStatus("current")


class _HpnicfLIUserStreamAcctSessID_Type(OctetString):
    """Custom type hpnicfLIUserStreamAcctSessID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_HpnicfLIUserStreamAcctSessID_Type.__name__ = "OctetString"
_HpnicfLIUserStreamAcctSessID_Object = MibTableColumn
hpnicfLIUserStreamAcctSessID = _HpnicfLIUserStreamAcctSessID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 4, 1, 1, 1, 1),
    _HpnicfLIUserStreamAcctSessID_Type()
)
hpnicfLIUserStreamAcctSessID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLIUserStreamAcctSessID.setStatus("current")
_HpnicfLIUserStreamRowStatus_Type = RowStatus
_HpnicfLIUserStreamRowStatus_Object = MibTableColumn
hpnicfLIUserStreamRowStatus = _HpnicfLIUserStreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 4, 1, 1, 1, 2),
    _HpnicfLIUserStreamRowStatus_Type()
)
hpnicfLIUserStreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLIUserStreamRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfLIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 2, 0, 1)
)
hpnicfLIActive.setObjects(
    ("HPN-ICF-LI-MIB", "hpnicfLIStreamtype")
)
if mibBuilder.loadTexts:
    hpnicfLIActive.setStatus(
        "current"
    )

hpnicfLITimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 2, 0, 2)
)
hpnicfLITimeOut.setObjects(
    ("HPN-ICF-LI-MIB", "hpnicfLIMediationRowStatus")
)
if mibBuilder.loadTexts:
    hpnicfLITimeOut.setStatus(
        "current"
    )

hpnicfLIFailureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111, 1, 2, 0, 3)
)
hpnicfLIFailureInformation.setObjects(
      *(("HPN-ICF-LI-MIB", "hpnicfLIStreamtype"),
        ("HPN-ICF-LI-MIB", "hpnicfLIBoardInformation"))
)
if mibBuilder.loadTexts:
    hpnicfLIFailureInformation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LI-MIB",
    **{"hpnicfLI": hpnicfLI,
       "hpnicfLICommon": hpnicfLICommon,
       "hpnicfLITrapBindObjects": hpnicfLITrapBindObjects,
       "hpnicfLIBoardInformation": hpnicfLIBoardInformation,
       "hpnicfLINotifications": hpnicfLINotifications,
       "hpnicfLINotificationsPrefix": hpnicfLINotificationsPrefix,
       "hpnicfLIActive": hpnicfLIActive,
       "hpnicfLITimeOut": hpnicfLITimeOut,
       "hpnicfLIFailureInformation": hpnicfLIFailureInformation,
       "hpnicfLIObjects": hpnicfLIObjects,
       "hpnicfLINewIndex": hpnicfLINewIndex,
       "hpnicfLIMediationTable": hpnicfLIMediationTable,
       "hpnicfLIMediationEntry": hpnicfLIMediationEntry,
       "hpnicfLIMediationIndex": hpnicfLIMediationIndex,
       "hpnicfLIMediationDestAddrType": hpnicfLIMediationDestAddrType,
       "hpnicfLIMediationDestAddr": hpnicfLIMediationDestAddr,
       "hpnicfLIMediationDestPort": hpnicfLIMediationDestPort,
       "hpnicfLIMediationSrcInterface": hpnicfLIMediationSrcInterface,
       "hpnicfLIMediationDscp": hpnicfLIMediationDscp,
       "hpnicfLIMediationTimeOut": hpnicfLIMediationTimeOut,
       "hpnicfLIMediationTransport": hpnicfLIMediationTransport,
       "hpnicfLIMediationNotificationEnable": hpnicfLIMediationNotificationEnable,
       "hpnicfLIMediationRowStatus": hpnicfLIMediationRowStatus,
       "hpnicfLIStreamTable": hpnicfLIStreamTable,
       "hpnicfLIStreamEntry": hpnicfLIStreamEntry,
       "hpnicfLIStreamIndex": hpnicfLIStreamIndex,
       "hpnicfLIStreamtype": hpnicfLIStreamtype,
       "hpnicfLIStreamEnable": hpnicfLIStreamEnable,
       "hpnicfLIStreamPackets": hpnicfLIStreamPackets,
       "hpnicfLIStreamDrops": hpnicfLIStreamDrops,
       "hpnicfLIStreamHPackets": hpnicfLIStreamHPackets,
       "hpnicfLIStreamHDrops": hpnicfLIStreamHDrops,
       "hpnicfLIStreamRowStatus": hpnicfLIStreamRowStatus,
       "hpnicfLIIPStream": hpnicfLIIPStream,
       "hpnicfLIIPStreamObjects": hpnicfLIIPStreamObjects,
       "hpnicfLIIPStreamTable": hpnicfLIIPStreamTable,
       "hpnicfLIIPStreamEntry": hpnicfLIIPStreamEntry,
       "hpnicfLIIPStreamInterface": hpnicfLIIPStreamInterface,
       "hpnicfLIIPStreamAddrType": hpnicfLIIPStreamAddrType,
       "hpnicfLIIPStreamDestAddr": hpnicfLIIPStreamDestAddr,
       "hpnicfLIIPStreamDestAddrLength": hpnicfLIIPStreamDestAddrLength,
       "hpnicfLIIPStreamSrcAddr": hpnicfLIIPStreamSrcAddr,
       "hpnicfLIIPStreamSrcAddrLength": hpnicfLIIPStreamSrcAddrLength,
       "hpnicfLIIPStreamTosByte": hpnicfLIIPStreamTosByte,
       "hpnicfLIIPStreamTosByteMask": hpnicfLIIPStreamTosByteMask,
       "hpnicfLIIPStreamFlowId": hpnicfLIIPStreamFlowId,
       "hpnicfLIIPStreamProtocol": hpnicfLIIPStreamProtocol,
       "hpnicfLIIPStreamDestL4PortMin": hpnicfLIIPStreamDestL4PortMin,
       "hpnicfLIIPStreamDestL4PortMax": hpnicfLIIPStreamDestL4PortMax,
       "hpnicfLIIPStreamSrcL4PortMin": hpnicfLIIPStreamSrcL4PortMin,
       "hpnicfLIIPStreamSrcL4PortMax": hpnicfLIIPStreamSrcL4PortMax,
       "hpnicfLIIPStreamVRF": hpnicfLIIPStreamVRF,
       "hpnicfLIIPStreamRowStatus": hpnicfLIIPStreamRowStatus,
       "hpnicfLIMACStream": hpnicfLIMACStream,
       "hpnicfLIMACStreamObjects": hpnicfLIMACStreamObjects,
       "hpnicfLIMACStreamTable": hpnicfLIMACStreamTable,
       "hpnicfLIMACStreamEntry": hpnicfLIMACStreamEntry,
       "hpnicfLIMACStreamFields": hpnicfLIMACStreamFields,
       "hpnicfLIMACStreamInterface": hpnicfLIMACStreamInterface,
       "hpnicfLIMACStreamDestAddr": hpnicfLIMACStreamDestAddr,
       "hpnicfLIMACStreamSrcAddr": hpnicfLIMACStreamSrcAddr,
       "hpnicfLIMACStreamEthPid": hpnicfLIMACStreamEthPid,
       "hpnicfLIMACStreamDSap": hpnicfLIMACStreamDSap,
       "hpnicfLIMACStreamSSap": hpnicfLIMACStreamSSap,
       "hpnicfLIMACStreamRowStatus": hpnicfLIMACStreamRowStatus,
       "hpnicfLIUserStream": hpnicfLIUserStream,
       "hpnicfLIUserStreamObjects": hpnicfLIUserStreamObjects,
       "hpnicfLIUserStreamTable": hpnicfLIUserStreamTable,
       "hpnicfLIUserStreamEntry": hpnicfLIUserStreamEntry,
       "hpnicfLIUserStreamAcctSessID": hpnicfLIUserStreamAcctSessID,
       "hpnicfLIUserStreamRowStatus": hpnicfLIUserStreamRowStatus}
)
