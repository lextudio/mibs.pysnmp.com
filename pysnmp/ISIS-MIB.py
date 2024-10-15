# SNMP MIB module (ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:21 2024
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

(IndexInteger,
 IndexIntegerNextFree) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexInteger",
    "IndexIntegerNextFree")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

isisMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 138)
)
isisMIB.setRevisions(
        ("2006-04-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IsisOSINSAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class IsisSystemID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class IsisLinkStatePDUID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class IsisAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )



class IsisLSPBuffSize(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16000),
    )



class IsisLevelState(Integer32, TextualConvention):
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
        *(("off", 1),
          ("on", 2),
          ("overloaded", 4),
          ("waiting", 3))
    )



class IsisSupportedProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(129,
              142,
              204)
        )
    )
    namedValues = NamedValues(
        *(("ip", 204),
          ("ipV6", 142),
          ("iso8473", 129))
    )



class IsisDefaultMetric(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class IsisWideMetric(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class IsisFullMetric(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class IsisMetricType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )



class IsisMetricStyle(Integer32, TextualConvention):
    status = "current"
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
          ("narrow", 1),
          ("wide", 2))
    )



class IsisISLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("area", 1),
          ("domain", 2))
    )



class IsisLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level1and2", 3),
          ("level2", 2))
    )



class IsisPDUHeader(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class IsisCircuitID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
    )



class IsisISPriority(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )



class IsisUnsigned16TC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IsisUnsigned8TC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_IsisNotifications_ObjectIdentity = ObjectIdentity
isisNotifications = _IsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 0)
)
_IsisObjects_ObjectIdentity = ObjectIdentity
isisObjects = _IsisObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1)
)
_IsisSystem_ObjectIdentity = ObjectIdentity
isisSystem = _IsisSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 1)
)
_IsisSysObject_ObjectIdentity = ObjectIdentity
isisSysObject = _IsisSysObject_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1)
)


class _IsisSysVersion_Type(Integer32):
    """Custom type isisSysVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("unknown", 0))
    )


_IsisSysVersion_Type.__name__ = "Integer32"
_IsisSysVersion_Object = MibScalar
isisSysVersion = _IsisSysVersion_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 1),
    _IsisSysVersion_Type()
)
isisSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysVersion.setStatus("current")


class _IsisSysLevelType_Type(IsisLevel):
    """Custom type isisSysLevelType based on IsisLevel"""


_IsisSysLevelType_Object = MibScalar
isisSysLevelType = _IsisSysLevelType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 2),
    _IsisSysLevelType_Type()
)
isisSysLevelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysLevelType.setStatus("current")
_IsisSysID_Type = IsisSystemID
_IsisSysID_Object = MibScalar
isisSysID = _IsisSysID_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 3),
    _IsisSysID_Type()
)
isisSysID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysID.setStatus("current")


class _IsisSysMaxPathSplits_Type(Unsigned32):
    """Custom type isisSysMaxPathSplits based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IsisSysMaxPathSplits_Type.__name__ = "Unsigned32"
_IsisSysMaxPathSplits_Object = MibScalar
isisSysMaxPathSplits = _IsisSysMaxPathSplits_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 4),
    _IsisSysMaxPathSplits_Type()
)
isisSysMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysMaxPathSplits.setStatus("current")


class _IsisSysMaxLSPGenInt_Type(Unsigned32):
    """Custom type isisSysMaxLSPGenInt based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65235),
    )


_IsisSysMaxLSPGenInt_Type.__name__ = "Unsigned32"
_IsisSysMaxLSPGenInt_Object = MibScalar
isisSysMaxLSPGenInt = _IsisSysMaxLSPGenInt_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 5),
    _IsisSysMaxLSPGenInt_Type()
)
isisSysMaxLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysMaxLSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    isisSysMaxLSPGenInt.setUnits("seconds")


class _IsisSysPollESHelloRate_Type(IsisUnsigned16TC):
    """Custom type isisSysPollESHelloRate based on IsisUnsigned16TC"""
    defaultValue = 50

    subtypeSpec = IsisUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysPollESHelloRate_Type.__name__ = "IsisUnsigned16TC"
_IsisSysPollESHelloRate_Object = MibScalar
isisSysPollESHelloRate = _IsisSysPollESHelloRate_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 6),
    _IsisSysPollESHelloRate_Type()
)
isisSysPollESHelloRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysPollESHelloRate.setStatus("current")
if mibBuilder.loadTexts:
    isisSysPollESHelloRate.setUnits("seconds")


class _IsisSysWaitTime_Type(IsisUnsigned16TC):
    """Custom type isisSysWaitTime based on IsisUnsigned16TC"""
    defaultValue = 60

    subtypeSpec = IsisUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysWaitTime_Type.__name__ = "IsisUnsigned16TC"
_IsisSysWaitTime_Object = MibScalar
isisSysWaitTime = _IsisSysWaitTime_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 7),
    _IsisSysWaitTime_Type()
)
isisSysWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    isisSysWaitTime.setUnits("seconds")


class _IsisSysAdminState_Type(IsisAdminState):
    """Custom type isisSysAdminState based on IsisAdminState"""


_IsisSysAdminState_Object = MibScalar
isisSysAdminState = _IsisSysAdminState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 8),
    _IsisSysAdminState_Type()
)
isisSysAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysAdminState.setStatus("current")


class _IsisSysL2toL1Leaking_Type(TruthValue):
    """Custom type isisSysL2toL1Leaking based on TruthValue"""


_IsisSysL2toL1Leaking_Object = MibScalar
isisSysL2toL1Leaking = _IsisSysL2toL1Leaking_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 9),
    _IsisSysL2toL1Leaking_Type()
)
isisSysL2toL1Leaking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysL2toL1Leaking.setStatus("current")


class _IsisSysMaxAge_Type(IsisUnsigned16TC):
    """Custom type isisSysMaxAge based on IsisUnsigned16TC"""
    defaultValue = 1200

    subtypeSpec = IsisUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 65535),
    )


_IsisSysMaxAge_Type.__name__ = "IsisUnsigned16TC"
_IsisSysMaxAge_Object = MibScalar
isisSysMaxAge = _IsisSysMaxAge_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 10),
    _IsisSysMaxAge_Type()
)
isisSysMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    isisSysMaxAge.setUnits("seconds")


class _IsisSysReceiveLSPBufferSize_Type(IsisUnsigned16TC):
    """Custom type isisSysReceiveLSPBufferSize based on IsisUnsigned16TC"""
    defaultValue = 1492

    subtypeSpec = IsisUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1492, 16000),
    )


_IsisSysReceiveLSPBufferSize_Type.__name__ = "IsisUnsigned16TC"
_IsisSysReceiveLSPBufferSize_Object = MibScalar
isisSysReceiveLSPBufferSize = _IsisSysReceiveLSPBufferSize_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 11),
    _IsisSysReceiveLSPBufferSize_Type()
)
isisSysReceiveLSPBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysReceiveLSPBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    isisSysReceiveLSPBufferSize.setUnits("bytes")


class _IsisSysProtSupported_Type(Bits):
    """Custom type isisSysProtSupported based on Bits"""
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("iso8473", 0))
    )

_IsisSysProtSupported_Type.__name__ = "Bits"
_IsisSysProtSupported_Object = MibScalar
isisSysProtSupported = _IsisSysProtSupported_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 12),
    _IsisSysProtSupported_Type()
)
isisSysProtSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysProtSupported.setStatus("current")


class _IsisSysNotificationEnable_Type(TruthValue):
    """Custom type isisSysNotificationEnable based on TruthValue"""


_IsisSysNotificationEnable_Object = MibScalar
isisSysNotificationEnable = _IsisSysNotificationEnable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 1, 13),
    _IsisSysNotificationEnable_Type()
)
isisSysNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysNotificationEnable.setStatus("current")
_IsisManAreaAddrTable_Object = MibTable
isisManAreaAddrTable = _IsisManAreaAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 2)
)
if mibBuilder.loadTexts:
    isisManAreaAddrTable.setStatus("current")
_IsisManAreaAddrEntry_Object = MibTableRow
isisManAreaAddrEntry = _IsisManAreaAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 2, 1)
)
isisManAreaAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisManAreaAddr"),
)
if mibBuilder.loadTexts:
    isisManAreaAddrEntry.setStatus("current")
_IsisManAreaAddr_Type = IsisOSINSAddress
_IsisManAreaAddr_Object = MibTableColumn
isisManAreaAddr = _IsisManAreaAddr_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 2, 1, 1),
    _IsisManAreaAddr_Type()
)
isisManAreaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisManAreaAddr.setStatus("current")
_IsisManAreaAddrExistState_Type = RowStatus
_IsisManAreaAddrExistState_Object = MibTableColumn
isisManAreaAddrExistState = _IsisManAreaAddrExistState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 2, 1, 2),
    _IsisManAreaAddrExistState_Type()
)
isisManAreaAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisManAreaAddrExistState.setStatus("current")
_IsisAreaAddrTable_Object = MibTable
isisAreaAddrTable = _IsisAreaAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 3)
)
if mibBuilder.loadTexts:
    isisAreaAddrTable.setStatus("current")
_IsisAreaAddrEntry_Object = MibTableRow
isisAreaAddrEntry = _IsisAreaAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 3, 1)
)
isisAreaAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisAreaAddr"),
)
if mibBuilder.loadTexts:
    isisAreaAddrEntry.setStatus("current")
_IsisAreaAddr_Type = IsisOSINSAddress
_IsisAreaAddr_Object = MibTableColumn
isisAreaAddr = _IsisAreaAddr_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 3, 1, 1),
    _IsisAreaAddr_Type()
)
isisAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisAreaAddr.setStatus("current")
_IsisSummAddrTable_Object = MibTable
isisSummAddrTable = _IsisSummAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 4)
)
if mibBuilder.loadTexts:
    isisSummAddrTable.setStatus("current")
_IsisSummAddrEntry_Object = MibTableRow
isisSummAddrEntry = _IsisSummAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 4, 1)
)
isisSummAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSummAddressType"),
    (0, "ISIS-MIB", "isisSummAddress"),
    (0, "ISIS-MIB", "isisSummAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    isisSummAddrEntry.setStatus("current")
_IsisSummAddressType_Type = InetAddressType
_IsisSummAddressType_Object = MibTableColumn
isisSummAddressType = _IsisSummAddressType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 4, 1, 1),
    _IsisSummAddressType_Type()
)
isisSummAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSummAddressType.setStatus("current")
_IsisSummAddress_Type = InetAddress
_IsisSummAddress_Object = MibTableColumn
isisSummAddress = _IsisSummAddress_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 4, 1, 2),
    _IsisSummAddress_Type()
)
isisSummAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSummAddress.setStatus("current")
_IsisSummAddrPrefixLen_Type = InetAddressPrefixLength
_IsisSummAddrPrefixLen_Object = MibTableColumn
isisSummAddrPrefixLen = _IsisSummAddrPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 4, 1, 3),
    _IsisSummAddrPrefixLen_Type()
)
isisSummAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSummAddrPrefixLen.setStatus("current")
_IsisSummAddrExistState_Type = RowStatus
_IsisSummAddrExistState_Object = MibTableColumn
isisSummAddrExistState = _IsisSummAddrExistState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 4, 1, 4),
    _IsisSummAddrExistState_Type()
)
isisSummAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSummAddrExistState.setStatus("current")


class _IsisSummAddrMetric_Type(IsisDefaultMetric):
    """Custom type isisSummAddrMetric based on IsisDefaultMetric"""
    defaultValue = 20


_IsisSummAddrMetric_Object = MibTableColumn
isisSummAddrMetric = _IsisSummAddrMetric_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 4, 1, 5),
    _IsisSummAddrMetric_Type()
)
isisSummAddrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSummAddrMetric.setStatus("current")


class _IsisSummAddrFullMetric_Type(IsisFullMetric):
    """Custom type isisSummAddrFullMetric based on IsisFullMetric"""
    defaultValue = 20


_IsisSummAddrFullMetric_Object = MibTableColumn
isisSummAddrFullMetric = _IsisSummAddrFullMetric_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 4, 1, 6),
    _IsisSummAddrFullMetric_Type()
)
isisSummAddrFullMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSummAddrFullMetric.setStatus("current")
_IsisRedistributeAddrTable_Object = MibTable
isisRedistributeAddrTable = _IsisRedistributeAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 5)
)
if mibBuilder.loadTexts:
    isisRedistributeAddrTable.setStatus("current")
_IsisRedistributeAddrEntry_Object = MibTableRow
isisRedistributeAddrEntry = _IsisRedistributeAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 5, 1)
)
isisRedistributeAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisRedistributeAddrType"),
    (0, "ISIS-MIB", "isisRedistributeAddrAddress"),
    (0, "ISIS-MIB", "isisRedistributeAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    isisRedistributeAddrEntry.setStatus("current")
_IsisRedistributeAddrType_Type = InetAddressType
_IsisRedistributeAddrType_Object = MibTableColumn
isisRedistributeAddrType = _IsisRedistributeAddrType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 5, 1, 1),
    _IsisRedistributeAddrType_Type()
)
isisRedistributeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRedistributeAddrType.setStatus("current")
_IsisRedistributeAddrAddress_Type = InetAddress
_IsisRedistributeAddrAddress_Object = MibTableColumn
isisRedistributeAddrAddress = _IsisRedistributeAddrAddress_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 5, 1, 2),
    _IsisRedistributeAddrAddress_Type()
)
isisRedistributeAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRedistributeAddrAddress.setStatus("current")
_IsisRedistributeAddrPrefixLen_Type = InetAddressPrefixLength
_IsisRedistributeAddrPrefixLen_Object = MibTableColumn
isisRedistributeAddrPrefixLen = _IsisRedistributeAddrPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 5, 1, 3),
    _IsisRedistributeAddrPrefixLen_Type()
)
isisRedistributeAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRedistributeAddrPrefixLen.setStatus("current")
_IsisRedistributeAddrExistState_Type = RowStatus
_IsisRedistributeAddrExistState_Object = MibTableColumn
isisRedistributeAddrExistState = _IsisRedistributeAddrExistState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 5, 1, 4),
    _IsisRedistributeAddrExistState_Type()
)
isisRedistributeAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRedistributeAddrExistState.setStatus("current")
_IsisRouterTable_Object = MibTable
isisRouterTable = _IsisRouterTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 6)
)
if mibBuilder.loadTexts:
    isisRouterTable.setStatus("current")
_IsisRouterEntry_Object = MibTableRow
isisRouterEntry = _IsisRouterEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 6, 1)
)
isisRouterEntry.setIndexNames(
    (0, "ISIS-MIB", "isisRouterSysID"),
    (0, "ISIS-MIB", "isisRouterLevel"),
)
if mibBuilder.loadTexts:
    isisRouterEntry.setStatus("current")
_IsisRouterSysID_Type = IsisSystemID
_IsisRouterSysID_Object = MibTableColumn
isisRouterSysID = _IsisRouterSysID_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 6, 1, 1),
    _IsisRouterSysID_Type()
)
isisRouterSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRouterSysID.setStatus("current")
_IsisRouterLevel_Type = IsisISLevel
_IsisRouterLevel_Object = MibTableColumn
isisRouterLevel = _IsisRouterLevel_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 6, 1, 2),
    _IsisRouterLevel_Type()
)
isisRouterLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRouterLevel.setStatus("current")
_IsisRouterHostName_Type = SnmpAdminString
_IsisRouterHostName_Object = MibTableColumn
isisRouterHostName = _IsisRouterHostName_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 6, 1, 3),
    _IsisRouterHostName_Type()
)
isisRouterHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisRouterHostName.setStatus("current")
_IsisRouterID_Type = Unsigned32
_IsisRouterID_Object = MibTableColumn
isisRouterID = _IsisRouterID_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 1, 6, 1, 4),
    _IsisRouterID_Type()
)
isisRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisRouterID.setStatus("current")
_IsisSysLevel_ObjectIdentity = ObjectIdentity
isisSysLevel = _IsisSysLevel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 2)
)
_IsisSysLevelTable_Object = MibTable
isisSysLevelTable = _IsisSysLevelTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1)
)
if mibBuilder.loadTexts:
    isisSysLevelTable.setStatus("current")
_IsisSysLevelEntry_Object = MibTableRow
isisSysLevelEntry = _IsisSysLevelEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1, 1)
)
isisSysLevelEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysLevelIndex"),
)
if mibBuilder.loadTexts:
    isisSysLevelEntry.setStatus("current")
_IsisSysLevelIndex_Type = IsisISLevel
_IsisSysLevelIndex_Object = MibTableColumn
isisSysLevelIndex = _IsisSysLevelIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1, 1, 1),
    _IsisSysLevelIndex_Type()
)
isisSysLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSysLevelIndex.setStatus("current")


class _IsisSysLevelOrigLSPBuffSize_Type(IsisLSPBuffSize):
    """Custom type isisSysLevelOrigLSPBuffSize based on IsisLSPBuffSize"""
    defaultValue = 1492


_IsisSysLevelOrigLSPBuffSize_Object = MibTableColumn
isisSysLevelOrigLSPBuffSize = _IsisSysLevelOrigLSPBuffSize_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1, 1, 2),
    _IsisSysLevelOrigLSPBuffSize_Type()
)
isisSysLevelOrigLSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysLevelOrigLSPBuffSize.setStatus("current")


class _IsisSysLevelMinLSPGenInt_Type(IsisUnsigned16TC):
    """Custom type isisSysLevelMinLSPGenInt based on IsisUnsigned16TC"""
    defaultValue = 30

    subtypeSpec = IsisUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysLevelMinLSPGenInt_Type.__name__ = "IsisUnsigned16TC"
_IsisSysLevelMinLSPGenInt_Object = MibTableColumn
isisSysLevelMinLSPGenInt = _IsisSysLevelMinLSPGenInt_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1, 1, 3),
    _IsisSysLevelMinLSPGenInt_Type()
)
isisSysLevelMinLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysLevelMinLSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    isisSysLevelMinLSPGenInt.setUnits("seconds")
_IsisSysLevelState_Type = IsisLevelState
_IsisSysLevelState_Object = MibTableColumn
isisSysLevelState = _IsisSysLevelState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1, 1, 4),
    _IsisSysLevelState_Type()
)
isisSysLevelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysLevelState.setStatus("current")


class _IsisSysLevelSetOverload_Type(TruthValue):
    """Custom type isisSysLevelSetOverload based on TruthValue"""


_IsisSysLevelSetOverload_Object = MibTableColumn
isisSysLevelSetOverload = _IsisSysLevelSetOverload_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1, 1, 5),
    _IsisSysLevelSetOverload_Type()
)
isisSysLevelSetOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysLevelSetOverload.setStatus("current")
_IsisSysLevelSetOverloadUntil_Type = Unsigned32
_IsisSysLevelSetOverloadUntil_Object = MibTableColumn
isisSysLevelSetOverloadUntil = _IsisSysLevelSetOverloadUntil_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1, 1, 6),
    _IsisSysLevelSetOverloadUntil_Type()
)
isisSysLevelSetOverloadUntil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysLevelSetOverloadUntil.setStatus("current")
if mibBuilder.loadTexts:
    isisSysLevelSetOverloadUntil.setUnits("Seconds until clearing manually set Overload Bit")


class _IsisSysLevelMetricStyle_Type(IsisMetricStyle):
    """Custom type isisSysLevelMetricStyle based on IsisMetricStyle"""


_IsisSysLevelMetricStyle_Object = MibTableColumn
isisSysLevelMetricStyle = _IsisSysLevelMetricStyle_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1, 1, 7),
    _IsisSysLevelMetricStyle_Type()
)
isisSysLevelMetricStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysLevelMetricStyle.setStatus("current")


class _IsisSysLevelSPFConsiders_Type(IsisMetricStyle):
    """Custom type isisSysLevelSPFConsiders based on IsisMetricStyle"""


_IsisSysLevelSPFConsiders_Object = MibTableColumn
isisSysLevelSPFConsiders = _IsisSysLevelSPFConsiders_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1, 1, 8),
    _IsisSysLevelSPFConsiders_Type()
)
isisSysLevelSPFConsiders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysLevelSPFConsiders.setStatus("current")


class _IsisSysLevelTEEnabled_Type(TruthValue):
    """Custom type isisSysLevelTEEnabled based on TruthValue"""


_IsisSysLevelTEEnabled_Object = MibTableColumn
isisSysLevelTEEnabled = _IsisSysLevelTEEnabled_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 2, 1, 1, 9),
    _IsisSysLevelTEEnabled_Type()
)
isisSysLevelTEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisSysLevelTEEnabled.setStatus("current")
_IsisCirc_ObjectIdentity = ObjectIdentity
isisCirc = _IsisCirc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 3)
)
_IsisNextCircIndex_Type = IndexIntegerNextFree
_IsisNextCircIndex_Object = MibScalar
isisNextCircIndex = _IsisNextCircIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 1),
    _IsisNextCircIndex_Type()
)
isisNextCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisNextCircIndex.setStatus("current")
_IsisCircTable_Object = MibTable
isisCircTable = _IsisCircTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2)
)
if mibBuilder.loadTexts:
    isisCircTable.setStatus("current")
_IsisCircEntry_Object = MibTableRow
isisCircEntry = _IsisCircEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1)
)
isisCircEntry.setIndexNames(
    (0, "ISIS-MIB", "isisCircIndex"),
)
if mibBuilder.loadTexts:
    isisCircEntry.setStatus("current")
_IsisCircIndex_Type = IndexInteger
_IsisCircIndex_Object = MibTableColumn
isisCircIndex = _IsisCircIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 1),
    _IsisCircIndex_Type()
)
isisCircIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisCircIndex.setStatus("current")
_IsisCircIfIndex_Type = InterfaceIndex
_IsisCircIfIndex_Object = MibTableColumn
isisCircIfIndex = _IsisCircIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 2),
    _IsisCircIfIndex_Type()
)
isisCircIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircIfIndex.setStatus("current")


class _IsisCircAdminState_Type(IsisAdminState):
    """Custom type isisCircAdminState based on IsisAdminState"""


_IsisCircAdminState_Object = MibTableColumn
isisCircAdminState = _IsisCircAdminState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 3),
    _IsisCircAdminState_Type()
)
isisCircAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircAdminState.setStatus("current")
_IsisCircExistState_Type = RowStatus
_IsisCircExistState_Object = MibTableColumn
isisCircExistState = _IsisCircExistState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 4),
    _IsisCircExistState_Type()
)
isisCircExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircExistState.setStatus("current")


class _IsisCircType_Type(Integer32):
    """Custom type isisCircType based on Integer32"""
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
        *(("broadcast", 1),
          ("dA", 5),
          ("ptToPt", 2),
          ("staticIn", 3),
          ("staticOut", 4))
    )


_IsisCircType_Type.__name__ = "Integer32"
_IsisCircType_Object = MibTableColumn
isisCircType = _IsisCircType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 5),
    _IsisCircType_Type()
)
isisCircType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircType.setStatus("current")


class _IsisCircExtDomain_Type(TruthValue):
    """Custom type isisCircExtDomain based on TruthValue"""


_IsisCircExtDomain_Object = MibTableColumn
isisCircExtDomain = _IsisCircExtDomain_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 6),
    _IsisCircExtDomain_Type()
)
isisCircExtDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircExtDomain.setStatus("current")


class _IsisCircLevelType_Type(IsisLevel):
    """Custom type isisCircLevelType based on IsisLevel"""


_IsisCircLevelType_Object = MibTableColumn
isisCircLevelType = _IsisCircLevelType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 7),
    _IsisCircLevelType_Type()
)
isisCircLevelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelType.setStatus("current")


class _IsisCircPassiveCircuit_Type(TruthValue):
    """Custom type isisCircPassiveCircuit based on TruthValue"""


_IsisCircPassiveCircuit_Object = MibTableColumn
isisCircPassiveCircuit = _IsisCircPassiveCircuit_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 8),
    _IsisCircPassiveCircuit_Type()
)
isisCircPassiveCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircPassiveCircuit.setStatus("current")


class _IsisCircMeshGroupEnabled_Type(Integer32):
    """Custom type isisCircMeshGroupEnabled based on Integer32"""
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
        *(("blocked", 2),
          ("inactive", 1),
          ("set", 3))
    )


_IsisCircMeshGroupEnabled_Type.__name__ = "Integer32"
_IsisCircMeshGroupEnabled_Object = MibTableColumn
isisCircMeshGroupEnabled = _IsisCircMeshGroupEnabled_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 9),
    _IsisCircMeshGroupEnabled_Type()
)
isisCircMeshGroupEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircMeshGroupEnabled.setStatus("current")
_IsisCircMeshGroup_Type = Unsigned32
_IsisCircMeshGroup_Object = MibTableColumn
isisCircMeshGroup = _IsisCircMeshGroup_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 10),
    _IsisCircMeshGroup_Type()
)
isisCircMeshGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircMeshGroup.setStatus("current")


class _IsisCircSmallHellos_Type(TruthValue):
    """Custom type isisCircSmallHellos based on TruthValue"""


_IsisCircSmallHellos_Object = MibTableColumn
isisCircSmallHellos = _IsisCircSmallHellos_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 11),
    _IsisCircSmallHellos_Type()
)
isisCircSmallHellos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircSmallHellos.setStatus("current")
_IsisCircLastUpTime_Type = TimeStamp
_IsisCircLastUpTime_Object = MibTableColumn
isisCircLastUpTime = _IsisCircLastUpTime_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 12),
    _IsisCircLastUpTime_Type()
)
isisCircLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLastUpTime.setStatus("current")


class _IsisCirc3WayEnabled_Type(TruthValue):
    """Custom type isisCirc3WayEnabled based on TruthValue"""


_IsisCirc3WayEnabled_Object = MibTableColumn
isisCirc3WayEnabled = _IsisCirc3WayEnabled_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 13),
    _IsisCirc3WayEnabled_Type()
)
isisCirc3WayEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCirc3WayEnabled.setStatus("current")
_IsisCircExtendedCircID_Type = Unsigned32
_IsisCircExtendedCircID_Object = MibTableColumn
isisCircExtendedCircID = _IsisCircExtendedCircID_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 3, 2, 1, 14),
    _IsisCircExtendedCircID_Type()
)
isisCircExtendedCircID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircExtendedCircID.setStatus("current")
_IsisCircLevelValues_ObjectIdentity = ObjectIdentity
isisCircLevelValues = _IsisCircLevelValues_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 4)
)
_IsisCircLevelTable_Object = MibTable
isisCircLevelTable = _IsisCircLevelTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1)
)
if mibBuilder.loadTexts:
    isisCircLevelTable.setStatus("current")
_IsisCircLevelEntry_Object = MibTableRow
isisCircLevelEntry = _IsisCircLevelEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1)
)
isisCircLevelEntry.setIndexNames(
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisCircLevelIndex"),
)
if mibBuilder.loadTexts:
    isisCircLevelEntry.setStatus("current")
_IsisCircLevelIndex_Type = IsisISLevel
_IsisCircLevelIndex_Object = MibTableColumn
isisCircLevelIndex = _IsisCircLevelIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 1),
    _IsisCircLevelIndex_Type()
)
isisCircLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisCircLevelIndex.setStatus("current")


class _IsisCircLevelMetric_Type(IsisDefaultMetric):
    """Custom type isisCircLevelMetric based on IsisDefaultMetric"""
    defaultValue = 10


_IsisCircLevelMetric_Object = MibTableColumn
isisCircLevelMetric = _IsisCircLevelMetric_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 2),
    _IsisCircLevelMetric_Type()
)
isisCircLevelMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisCircLevelMetric.setStatus("current")


class _IsisCircLevelWideMetric_Type(IsisWideMetric):
    """Custom type isisCircLevelWideMetric based on IsisWideMetric"""
    defaultValue = 10


_IsisCircLevelWideMetric_Object = MibTableColumn
isisCircLevelWideMetric = _IsisCircLevelWideMetric_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 3),
    _IsisCircLevelWideMetric_Type()
)
isisCircLevelWideMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisCircLevelWideMetric.setStatus("current")


class _IsisCircLevelISPriority_Type(IsisISPriority):
    """Custom type isisCircLevelISPriority based on IsisISPriority"""
    defaultValue = 64


_IsisCircLevelISPriority_Object = MibTableColumn
isisCircLevelISPriority = _IsisCircLevelISPriority_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 4),
    _IsisCircLevelISPriority_Type()
)
isisCircLevelISPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisCircLevelISPriority.setStatus("current")


class _IsisCircLevelIDOctet_Type(Unsigned32):
    """Custom type isisCircLevelIDOctet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsisCircLevelIDOctet_Type.__name__ = "Unsigned32"
_IsisCircLevelIDOctet_Object = MibTableColumn
isisCircLevelIDOctet = _IsisCircLevelIDOctet_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 5),
    _IsisCircLevelIDOctet_Type()
)
isisCircLevelIDOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLevelIDOctet.setStatus("current")
_IsisCircLevelID_Type = IsisCircuitID
_IsisCircLevelID_Object = MibTableColumn
isisCircLevelID = _IsisCircLevelID_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 6),
    _IsisCircLevelID_Type()
)
isisCircLevelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLevelID.setStatus("current")
_IsisCircLevelDesIS_Type = IsisCircuitID
_IsisCircLevelDesIS_Object = MibTableColumn
isisCircLevelDesIS = _IsisCircLevelDesIS_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 7),
    _IsisCircLevelDesIS_Type()
)
isisCircLevelDesIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLevelDesIS.setStatus("current")


class _IsisCircLevelHelloMultiplier_Type(Unsigned32):
    """Custom type isisCircLevelHelloMultiplier based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_IsisCircLevelHelloMultiplier_Type.__name__ = "Unsigned32"
_IsisCircLevelHelloMultiplier_Object = MibTableColumn
isisCircLevelHelloMultiplier = _IsisCircLevelHelloMultiplier_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 8),
    _IsisCircLevelHelloMultiplier_Type()
)
isisCircLevelHelloMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisCircLevelHelloMultiplier.setStatus("current")


class _IsisCircLevelHelloTimer_Type(Unsigned32):
    """Custom type isisCircLevelHelloTimer based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600000),
    )


_IsisCircLevelHelloTimer_Type.__name__ = "Unsigned32"
_IsisCircLevelHelloTimer_Object = MibTableColumn
isisCircLevelHelloTimer = _IsisCircLevelHelloTimer_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 9),
    _IsisCircLevelHelloTimer_Type()
)
isisCircLevelHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisCircLevelHelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelHelloTimer.setUnits("milliseconds")


class _IsisCircLevelDRHelloTimer_Type(Unsigned32):
    """Custom type isisCircLevelDRHelloTimer based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120000),
    )


_IsisCircLevelDRHelloTimer_Type.__name__ = "Unsigned32"
_IsisCircLevelDRHelloTimer_Object = MibTableColumn
isisCircLevelDRHelloTimer = _IsisCircLevelDRHelloTimer_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 10),
    _IsisCircLevelDRHelloTimer_Type()
)
isisCircLevelDRHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisCircLevelDRHelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelDRHelloTimer.setUnits("milliseconds")


class _IsisCircLevelLSPThrottle_Type(IsisUnsigned16TC):
    """Custom type isisCircLevelLSPThrottle based on IsisUnsigned16TC"""
    defaultValue = 30

    subtypeSpec = IsisUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisCircLevelLSPThrottle_Type.__name__ = "IsisUnsigned16TC"
_IsisCircLevelLSPThrottle_Object = MibTableColumn
isisCircLevelLSPThrottle = _IsisCircLevelLSPThrottle_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 11),
    _IsisCircLevelLSPThrottle_Type()
)
isisCircLevelLSPThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisCircLevelLSPThrottle.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelLSPThrottle.setUnits("milliseconds")


class _IsisCircLevelMinLSPRetransInt_Type(Unsigned32):
    """Custom type isisCircLevelMinLSPRetransInt based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_IsisCircLevelMinLSPRetransInt_Type.__name__ = "Unsigned32"
_IsisCircLevelMinLSPRetransInt_Object = MibTableColumn
isisCircLevelMinLSPRetransInt = _IsisCircLevelMinLSPRetransInt_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 12),
    _IsisCircLevelMinLSPRetransInt_Type()
)
isisCircLevelMinLSPRetransInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisCircLevelMinLSPRetransInt.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelMinLSPRetransInt.setUnits("seconds")


class _IsisCircLevelCSNPInterval_Type(Unsigned32):
    """Custom type isisCircLevelCSNPInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_IsisCircLevelCSNPInterval_Type.__name__ = "Unsigned32"
_IsisCircLevelCSNPInterval_Object = MibTableColumn
isisCircLevelCSNPInterval = _IsisCircLevelCSNPInterval_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 13),
    _IsisCircLevelCSNPInterval_Type()
)
isisCircLevelCSNPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisCircLevelCSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelCSNPInterval.setUnits("seconds")


class _IsisCircLevelPartSNPInterval_Type(Unsigned32):
    """Custom type isisCircLevelPartSNPInterval based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_IsisCircLevelPartSNPInterval_Type.__name__ = "Unsigned32"
_IsisCircLevelPartSNPInterval_Object = MibTableColumn
isisCircLevelPartSNPInterval = _IsisCircLevelPartSNPInterval_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 4, 1, 1, 14),
    _IsisCircLevelPartSNPInterval_Type()
)
isisCircLevelPartSNPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isisCircLevelPartSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelPartSNPInterval.setUnits("seconds")
_IsisCounters_ObjectIdentity = ObjectIdentity
isisCounters = _IsisCounters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 5)
)
_IsisSystemCounterTable_Object = MibTable
isisSystemCounterTable = _IsisSystemCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1)
)
if mibBuilder.loadTexts:
    isisSystemCounterTable.setStatus("current")
_IsisSystemCounterEntry_Object = MibTableRow
isisSystemCounterEntry = _IsisSystemCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1)
)
isisSystemCounterEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysStatLevel"),
)
if mibBuilder.loadTexts:
    isisSystemCounterEntry.setStatus("current")
_IsisSysStatLevel_Type = IsisISLevel
_IsisSysStatLevel_Object = MibTableColumn
isisSysStatLevel = _IsisSysStatLevel_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 1),
    _IsisSysStatLevel_Type()
)
isisSysStatLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSysStatLevel.setStatus("current")
_IsisSysStatCorrLSPs_Type = Counter32
_IsisSysStatCorrLSPs_Object = MibTableColumn
isisSysStatCorrLSPs = _IsisSysStatCorrLSPs_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 2),
    _IsisSysStatCorrLSPs_Type()
)
isisSysStatCorrLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatCorrLSPs.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatCorrLSPs.setUnits("Number of corrupted in-memory frames")
_IsisSysStatAuthTypeFails_Type = Counter32
_IsisSysStatAuthTypeFails_Object = MibTableColumn
isisSysStatAuthTypeFails = _IsisSysStatAuthTypeFails_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 3),
    _IsisSysStatAuthTypeFails_Type()
)
isisSysStatAuthTypeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatAuthTypeFails.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatAuthTypeFails.setUnits("Number of frames with authentication type mismatches")
_IsisSysStatAuthFails_Type = Counter32
_IsisSysStatAuthFails_Object = MibTableColumn
isisSysStatAuthFails = _IsisSysStatAuthFails_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 4),
    _IsisSysStatAuthFails_Type()
)
isisSysStatAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatAuthFails.setUnits("Number of frames with authentication key failures")
_IsisSysStatLSPDbaseOloads_Type = Counter32
_IsisSysStatLSPDbaseOloads_Object = MibTableColumn
isisSysStatLSPDbaseOloads = _IsisSysStatLSPDbaseOloads_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 5),
    _IsisSysStatLSPDbaseOloads_Type()
)
isisSysStatLSPDbaseOloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatLSPDbaseOloads.setStatus("current")
_IsisSysStatManAddrDropFromAreas_Type = Counter32
_IsisSysStatManAddrDropFromAreas_Object = MibTableColumn
isisSysStatManAddrDropFromAreas = _IsisSysStatManAddrDropFromAreas_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 6),
    _IsisSysStatManAddrDropFromAreas_Type()
)
isisSysStatManAddrDropFromAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatManAddrDropFromAreas.setStatus("current")
_IsisSysStatAttmptToExMaxSeqNums_Type = Counter32
_IsisSysStatAttmptToExMaxSeqNums_Object = MibTableColumn
isisSysStatAttmptToExMaxSeqNums = _IsisSysStatAttmptToExMaxSeqNums_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 7),
    _IsisSysStatAttmptToExMaxSeqNums_Type()
)
isisSysStatAttmptToExMaxSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatAttmptToExMaxSeqNums.setStatus("current")
_IsisSysStatSeqNumSkips_Type = Counter32
_IsisSysStatSeqNumSkips_Object = MibTableColumn
isisSysStatSeqNumSkips = _IsisSysStatSeqNumSkips_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 8),
    _IsisSysStatSeqNumSkips_Type()
)
isisSysStatSeqNumSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatSeqNumSkips.setStatus("current")
_IsisSysStatOwnLSPPurges_Type = Counter32
_IsisSysStatOwnLSPPurges_Object = MibTableColumn
isisSysStatOwnLSPPurges = _IsisSysStatOwnLSPPurges_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 9),
    _IsisSysStatOwnLSPPurges_Type()
)
isisSysStatOwnLSPPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatOwnLSPPurges.setStatus("current")
_IsisSysStatIDFieldLenMismatches_Type = Counter32
_IsisSysStatIDFieldLenMismatches_Object = MibTableColumn
isisSysStatIDFieldLenMismatches = _IsisSysStatIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 10),
    _IsisSysStatIDFieldLenMismatches_Type()
)
isisSysStatIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatIDFieldLenMismatches.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatIDFieldLenMismatches.setUnits("Number of frames with ID length mismatches")
_IsisSysStatPartChanges_Type = Counter32
_IsisSysStatPartChanges_Object = MibTableColumn
isisSysStatPartChanges = _IsisSysStatPartChanges_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 11),
    _IsisSysStatPartChanges_Type()
)
isisSysStatPartChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatPartChanges.setStatus("current")
_IsisSysStatSPFRuns_Type = Counter32
_IsisSysStatSPFRuns_Object = MibTableColumn
isisSysStatSPFRuns = _IsisSysStatSPFRuns_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 12),
    _IsisSysStatSPFRuns_Type()
)
isisSysStatSPFRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatSPFRuns.setStatus("current")
_IsisSysStatLSPErrors_Type = Counter32
_IsisSysStatLSPErrors_Object = MibTableColumn
isisSysStatLSPErrors = _IsisSysStatLSPErrors_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 1, 1, 13),
    _IsisSysStatLSPErrors_Type()
)
isisSysStatLSPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatLSPErrors.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatLSPErrors.setUnits("Number of frames with errors that we have received")
_IsisCircuitCounterTable_Object = MibTable
isisCircuitCounterTable = _IsisCircuitCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2)
)
if mibBuilder.loadTexts:
    isisCircuitCounterTable.setStatus("current")
_IsisCircuitCounterEntry_Object = MibTableRow
isisCircuitCounterEntry = _IsisCircuitCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1)
)
isisCircuitCounterEntry.setIndexNames(
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisCircuitType"),
)
if mibBuilder.loadTexts:
    isisCircuitCounterEntry.setStatus("current")


class _IsisCircuitType_Type(Integer32):
    """Custom type isisCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lanlevel1", 1),
          ("lanlevel2", 2),
          ("p2pcircuit", 3))
    )


_IsisCircuitType_Type.__name__ = "Integer32"
_IsisCircuitType_Object = MibTableColumn
isisCircuitType = _IsisCircuitType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1, 1),
    _IsisCircuitType_Type()
)
isisCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisCircuitType.setStatus("current")
_IsisCircAdjChanges_Type = Counter32
_IsisCircAdjChanges_Object = MibTableColumn
isisCircAdjChanges = _IsisCircAdjChanges_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1, 2),
    _IsisCircAdjChanges_Type()
)
isisCircAdjChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircAdjChanges.setStatus("current")
_IsisCircNumAdj_Type = Unsigned32
_IsisCircNumAdj_Object = MibTableColumn
isisCircNumAdj = _IsisCircNumAdj_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1, 3),
    _IsisCircNumAdj_Type()
)
isisCircNumAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircNumAdj.setStatus("current")
_IsisCircInitFails_Type = Counter32
_IsisCircInitFails_Object = MibTableColumn
isisCircInitFails = _IsisCircInitFails_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1, 4),
    _IsisCircInitFails_Type()
)
isisCircInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircInitFails.setStatus("current")
_IsisCircRejAdjs_Type = Counter32
_IsisCircRejAdjs_Object = MibTableColumn
isisCircRejAdjs = _IsisCircRejAdjs_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1, 5),
    _IsisCircRejAdjs_Type()
)
isisCircRejAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircRejAdjs.setStatus("current")
_IsisCircIDFieldLenMismatches_Type = Counter32
_IsisCircIDFieldLenMismatches_Object = MibTableColumn
isisCircIDFieldLenMismatches = _IsisCircIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1, 6),
    _IsisCircIDFieldLenMismatches_Type()
)
isisCircIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircIDFieldLenMismatches.setStatus("current")
if mibBuilder.loadTexts:
    isisCircIDFieldLenMismatches.setUnits("Number of frames with ID field length mismatch")
_IsisCircMaxAreaAddrMismatches_Type = Counter32
_IsisCircMaxAreaAddrMismatches_Object = MibTableColumn
isisCircMaxAreaAddrMismatches = _IsisCircMaxAreaAddrMismatches_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1, 7),
    _IsisCircMaxAreaAddrMismatches_Type()
)
isisCircMaxAreaAddrMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircMaxAreaAddrMismatches.setStatus("current")
_IsisCircAuthTypeFails_Type = Counter32
_IsisCircAuthTypeFails_Object = MibTableColumn
isisCircAuthTypeFails = _IsisCircAuthTypeFails_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1, 8),
    _IsisCircAuthTypeFails_Type()
)
isisCircAuthTypeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircAuthTypeFails.setStatus("current")
_IsisCircAuthFails_Type = Counter32
_IsisCircAuthFails_Object = MibTableColumn
isisCircAuthFails = _IsisCircAuthFails_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1, 9),
    _IsisCircAuthFails_Type()
)
isisCircAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircAuthFails.setStatus("current")
_IsisCircLANDesISChanges_Type = Counter32
_IsisCircLANDesISChanges_Object = MibTableColumn
isisCircLANDesISChanges = _IsisCircLANDesISChanges_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 2, 1, 10),
    _IsisCircLANDesISChanges_Type()
)
isisCircLANDesISChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLANDesISChanges.setStatus("current")
_IsisPacketCounterTable_Object = MibTable
isisPacketCounterTable = _IsisPacketCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3)
)
if mibBuilder.loadTexts:
    isisPacketCounterTable.setStatus("current")
_IsisPacketCounterEntry_Object = MibTableRow
isisPacketCounterEntry = _IsisPacketCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3, 1)
)
isisPacketCounterEntry.setIndexNames(
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisPacketCountLevel"),
    (0, "ISIS-MIB", "isisPacketCountDirection"),
)
if mibBuilder.loadTexts:
    isisPacketCounterEntry.setStatus("current")
_IsisPacketCountLevel_Type = IsisISLevel
_IsisPacketCountLevel_Object = MibTableColumn
isisPacketCountLevel = _IsisPacketCountLevel_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3, 1, 1),
    _IsisPacketCountLevel_Type()
)
isisPacketCountLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPacketCountLevel.setStatus("current")


class _IsisPacketCountDirection_Type(Integer32):
    """Custom type isisPacketCountDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receiving", 2),
          ("sending", 1))
    )


_IsisPacketCountDirection_Type.__name__ = "Integer32"
_IsisPacketCountDirection_Object = MibTableColumn
isisPacketCountDirection = _IsisPacketCountDirection_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3, 1, 2),
    _IsisPacketCountDirection_Type()
)
isisPacketCountDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPacketCountDirection.setStatus("current")
_IsisPacketCountIIHello_Type = Counter32
_IsisPacketCountIIHello_Object = MibTableColumn
isisPacketCountIIHello = _IsisPacketCountIIHello_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3, 1, 3),
    _IsisPacketCountIIHello_Type()
)
isisPacketCountIIHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountIIHello.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountIIHello.setUnits("Number of IS-IS Hellos frames seen in this direction at this level")
_IsisPacketCountISHello_Type = Counter32
_IsisPacketCountISHello_Object = MibTableColumn
isisPacketCountISHello = _IsisPacketCountISHello_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3, 1, 4),
    _IsisPacketCountISHello_Type()
)
isisPacketCountISHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountISHello.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountISHello.setUnits("Number of ES-IS frames seen in this direction at this level.")
_IsisPacketCountESHello_Type = Counter32
_IsisPacketCountESHello_Object = MibTableColumn
isisPacketCountESHello = _IsisPacketCountESHello_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3, 1, 5),
    _IsisPacketCountESHello_Type()
)
isisPacketCountESHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountESHello.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountESHello.setUnits("Number of ES Hello frames seen in this direction at this level")
_IsisPacketCountLSP_Type = Counter32
_IsisPacketCountLSP_Object = MibTableColumn
isisPacketCountLSP = _IsisPacketCountLSP_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3, 1, 6),
    _IsisPacketCountLSP_Type()
)
isisPacketCountLSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountLSP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountLSP.setUnits("Number of IS-IS LSP frames seen in this direction at this level")
_IsisPacketCountCSNP_Type = Counter32
_IsisPacketCountCSNP_Object = MibTableColumn
isisPacketCountCSNP = _IsisPacketCountCSNP_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3, 1, 7),
    _IsisPacketCountCSNP_Type()
)
isisPacketCountCSNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountCSNP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountCSNP.setUnits("Number of IS-IS CSNP frames seen in this direction at this level")
_IsisPacketCountPSNP_Type = Counter32
_IsisPacketCountPSNP_Object = MibTableColumn
isisPacketCountPSNP = _IsisPacketCountPSNP_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3, 1, 8),
    _IsisPacketCountPSNP_Type()
)
isisPacketCountPSNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountPSNP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountPSNP.setUnits("Number of IS-IS PSNP frames seen in this direction at this level")
_IsisPacketCountUnknown_Type = Counter32
_IsisPacketCountUnknown_Object = MibTableColumn
isisPacketCountUnknown = _IsisPacketCountUnknown_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 5, 3, 1, 9),
    _IsisPacketCountUnknown_Type()
)
isisPacketCountUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountUnknown.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountUnknown.setUnits("Number of unknown IS-IS frames seen at this level")
_IsisISAdj_ObjectIdentity = ObjectIdentity
isisISAdj = _IsisISAdj_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 6)
)
_IsisISAdjTable_Object = MibTable
isisISAdjTable = _IsisISAdjTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1)
)
if mibBuilder.loadTexts:
    isisISAdjTable.setStatus("current")
_IsisISAdjEntry_Object = MibTableRow
isisISAdjEntry = _IsisISAdjEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1)
)
isisISAdjEntry.setIndexNames(
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisISAdjIndex"),
)
if mibBuilder.loadTexts:
    isisISAdjEntry.setStatus("current")


class _IsisISAdjIndex_Type(Unsigned32):
    """Custom type isisISAdjIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IsisISAdjIndex_Type.__name__ = "Unsigned32"
_IsisISAdjIndex_Object = MibTableColumn
isisISAdjIndex = _IsisISAdjIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 1),
    _IsisISAdjIndex_Type()
)
isisISAdjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjIndex.setStatus("current")


class _IsisISAdjState_Type(Integer32):
    """Custom type isisISAdjState based on Integer32"""
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
        *(("down", 1),
          ("failed", 4),
          ("initializing", 2),
          ("up", 3))
    )


_IsisISAdjState_Type.__name__ = "Integer32"
_IsisISAdjState_Object = MibTableColumn
isisISAdjState = _IsisISAdjState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 2),
    _IsisISAdjState_Type()
)
isisISAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjState.setStatus("current")


class _IsisISAdj3WayState_Type(Integer32):
    """Custom type isisISAdj3WayState based on Integer32"""
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
        *(("down", 2),
          ("failed", 3),
          ("initializing", 1),
          ("up", 0))
    )


_IsisISAdj3WayState_Type.__name__ = "Integer32"
_IsisISAdj3WayState_Object = MibTableColumn
isisISAdj3WayState = _IsisISAdj3WayState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 3),
    _IsisISAdj3WayState_Type()
)
isisISAdj3WayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdj3WayState.setStatus("current")
_IsisISAdjNeighSNPAAddress_Type = IsisOSINSAddress
_IsisISAdjNeighSNPAAddress_Object = MibTableColumn
isisISAdjNeighSNPAAddress = _IsisISAdjNeighSNPAAddress_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 4),
    _IsisISAdjNeighSNPAAddress_Type()
)
isisISAdjNeighSNPAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighSNPAAddress.setStatus("current")


class _IsisISAdjNeighSysType_Type(Integer32):
    """Custom type isisISAdjNeighSysType based on Integer32"""
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
        *(("l1IntermediateSystem", 1),
          ("l1L2IntermediateSystem", 3),
          ("l2IntermediateSystem", 2),
          ("unknown", 4))
    )


_IsisISAdjNeighSysType_Type.__name__ = "Integer32"
_IsisISAdjNeighSysType_Object = MibTableColumn
isisISAdjNeighSysType = _IsisISAdjNeighSysType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 5),
    _IsisISAdjNeighSysType_Type()
)
isisISAdjNeighSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighSysType.setStatus("current")
_IsisISAdjNeighSysID_Type = IsisSystemID
_IsisISAdjNeighSysID_Object = MibTableColumn
isisISAdjNeighSysID = _IsisISAdjNeighSysID_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 6),
    _IsisISAdjNeighSysID_Type()
)
isisISAdjNeighSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighSysID.setStatus("current")
_IsisISAdjNbrExtendedCircID_Type = Unsigned32
_IsisISAdjNbrExtendedCircID_Object = MibTableColumn
isisISAdjNbrExtendedCircID = _IsisISAdjNbrExtendedCircID_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 7),
    _IsisISAdjNbrExtendedCircID_Type()
)
isisISAdjNbrExtendedCircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNbrExtendedCircID.setStatus("current")
_IsisISAdjUsage_Type = IsisLevel
_IsisISAdjUsage_Object = MibTableColumn
isisISAdjUsage = _IsisISAdjUsage_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 8),
    _IsisISAdjUsage_Type()
)
isisISAdjUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjUsage.setStatus("current")


class _IsisISAdjHoldTimer_Type(IsisUnsigned16TC):
    """Custom type isisISAdjHoldTimer based on IsisUnsigned16TC"""
    subtypeSpec = IsisUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisISAdjHoldTimer_Type.__name__ = "IsisUnsigned16TC"
_IsisISAdjHoldTimer_Object = MibTableColumn
isisISAdjHoldTimer = _IsisISAdjHoldTimer_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 9),
    _IsisISAdjHoldTimer_Type()
)
isisISAdjHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    isisISAdjHoldTimer.setUnits("seconds")
_IsisISAdjNeighPriority_Type = IsisISPriority
_IsisISAdjNeighPriority_Object = MibTableColumn
isisISAdjNeighPriority = _IsisISAdjNeighPriority_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 10),
    _IsisISAdjNeighPriority_Type()
)
isisISAdjNeighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighPriority.setStatus("current")
_IsisISAdjLastUpTime_Type = TimeStamp
_IsisISAdjLastUpTime_Object = MibTableColumn
isisISAdjLastUpTime = _IsisISAdjLastUpTime_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 1, 1, 11),
    _IsisISAdjLastUpTime_Type()
)
isisISAdjLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjLastUpTime.setStatus("current")
_IsisISAdjAreaAddrTable_Object = MibTable
isisISAdjAreaAddrTable = _IsisISAdjAreaAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 2)
)
if mibBuilder.loadTexts:
    isisISAdjAreaAddrTable.setStatus("current")
_IsisISAdjAreaAddrEntry_Object = MibTableRow
isisISAdjAreaAddrEntry = _IsisISAdjAreaAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 2, 1)
)
isisISAdjAreaAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisISAdjIndex"),
    (0, "ISIS-MIB", "isisISAdjAreaAddrIndex"),
)
if mibBuilder.loadTexts:
    isisISAdjAreaAddrEntry.setStatus("current")


class _IsisISAdjAreaAddrIndex_Type(Unsigned32):
    """Custom type isisISAdjAreaAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IsisISAdjAreaAddrIndex_Type.__name__ = "Unsigned32"
_IsisISAdjAreaAddrIndex_Object = MibTableColumn
isisISAdjAreaAddrIndex = _IsisISAdjAreaAddrIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 2, 1, 1),
    _IsisISAdjAreaAddrIndex_Type()
)
isisISAdjAreaAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjAreaAddrIndex.setStatus("current")
_IsisISAdjAreaAddress_Type = IsisOSINSAddress
_IsisISAdjAreaAddress_Object = MibTableColumn
isisISAdjAreaAddress = _IsisISAdjAreaAddress_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 2, 1, 2),
    _IsisISAdjAreaAddress_Type()
)
isisISAdjAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjAreaAddress.setStatus("current")
_IsisISAdjIPAddrTable_Object = MibTable
isisISAdjIPAddrTable = _IsisISAdjIPAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 3)
)
if mibBuilder.loadTexts:
    isisISAdjIPAddrTable.setStatus("current")
_IsisISAdjIPAddrEntry_Object = MibTableRow
isisISAdjIPAddrEntry = _IsisISAdjIPAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 3, 1)
)
isisISAdjIPAddrEntry.setIndexNames(
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisISAdjIndex"),
    (0, "ISIS-MIB", "isisISAdjIPAddrIndex"),
)
if mibBuilder.loadTexts:
    isisISAdjIPAddrEntry.setStatus("current")


class _IsisISAdjIPAddrIndex_Type(Unsigned32):
    """Custom type isisISAdjIPAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IsisISAdjIPAddrIndex_Type.__name__ = "Unsigned32"
_IsisISAdjIPAddrIndex_Object = MibTableColumn
isisISAdjIPAddrIndex = _IsisISAdjIPAddrIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 3, 1, 1),
    _IsisISAdjIPAddrIndex_Type()
)
isisISAdjIPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjIPAddrIndex.setStatus("current")
_IsisISAdjIPAddrType_Type = InetAddressType
_IsisISAdjIPAddrType_Object = MibTableColumn
isisISAdjIPAddrType = _IsisISAdjIPAddrType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 3, 1, 2),
    _IsisISAdjIPAddrType_Type()
)
isisISAdjIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjIPAddrType.setStatus("current")
_IsisISAdjIPAddrAddress_Type = InetAddress
_IsisISAdjIPAddrAddress_Object = MibTableColumn
isisISAdjIPAddrAddress = _IsisISAdjIPAddrAddress_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 3, 1, 3),
    _IsisISAdjIPAddrAddress_Type()
)
isisISAdjIPAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjIPAddrAddress.setStatus("current")
_IsisISAdjProtSuppTable_Object = MibTable
isisISAdjProtSuppTable = _IsisISAdjProtSuppTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 4)
)
if mibBuilder.loadTexts:
    isisISAdjProtSuppTable.setStatus("current")
_IsisISAdjProtSuppEntry_Object = MibTableRow
isisISAdjProtSuppEntry = _IsisISAdjProtSuppEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 4, 1)
)
isisISAdjProtSuppEntry.setIndexNames(
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisISAdjIndex"),
    (0, "ISIS-MIB", "isisISAdjProtSuppProtocol"),
)
if mibBuilder.loadTexts:
    isisISAdjProtSuppEntry.setStatus("current")
_IsisISAdjProtSuppProtocol_Type = IsisSupportedProtocol
_IsisISAdjProtSuppProtocol_Object = MibTableColumn
isisISAdjProtSuppProtocol = _IsisISAdjProtSuppProtocol_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 6, 4, 1, 1),
    _IsisISAdjProtSuppProtocol_Type()
)
isisISAdjProtSuppProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjProtSuppProtocol.setStatus("current")
_IsisReachAddr_ObjectIdentity = ObjectIdentity
isisReachAddr = _IsisReachAddr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 7)
)
_IsisRATable_Object = MibTable
isisRATable = _IsisRATable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1)
)
if mibBuilder.loadTexts:
    isisRATable.setStatus("current")
_IsisRAEntry_Object = MibTableRow
isisRAEntry = _IsisRAEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1)
)
isisRAEntry.setIndexNames(
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisRAIndex"),
)
if mibBuilder.loadTexts:
    isisRAEntry.setStatus("current")


class _IsisRAIndex_Type(Unsigned32):
    """Custom type isisRAIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IsisRAIndex_Type.__name__ = "Unsigned32"
_IsisRAIndex_Object = MibTableColumn
isisRAIndex = _IsisRAIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 1),
    _IsisRAIndex_Type()
)
isisRAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRAIndex.setStatus("current")
_IsisRAExistState_Type = RowStatus
_IsisRAExistState_Object = MibTableColumn
isisRAExistState = _IsisRAExistState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 2),
    _IsisRAExistState_Type()
)
isisRAExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRAExistState.setStatus("current")


class _IsisRAAdminState_Type(IsisAdminState):
    """Custom type isisRAAdminState based on IsisAdminState"""


_IsisRAAdminState_Object = MibTableColumn
isisRAAdminState = _IsisRAAdminState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 3),
    _IsisRAAdminState_Type()
)
isisRAAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRAAdminState.setStatus("current")
_IsisRAAddrPrefix_Type = IsisOSINSAddress
_IsisRAAddrPrefix_Object = MibTableColumn
isisRAAddrPrefix = _IsisRAAddrPrefix_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 4),
    _IsisRAAddrPrefix_Type()
)
isisRAAddrPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRAAddrPrefix.setStatus("current")


class _IsisRAMapType_Type(Integer32):
    """Custom type isisRAMapType based on Integer32"""
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
        *(("explicit", 2),
          ("extractDSP", 4),
          ("extractIDI", 3),
          ("none", 1))
    )


_IsisRAMapType_Type.__name__ = "Integer32"
_IsisRAMapType_Object = MibTableColumn
isisRAMapType = _IsisRAMapType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 5),
    _IsisRAMapType_Type()
)
isisRAMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRAMapType.setStatus("current")


class _IsisRAMetric_Type(IsisDefaultMetric):
    """Custom type isisRAMetric based on IsisDefaultMetric"""
    defaultValue = 20


_IsisRAMetric_Object = MibTableColumn
isisRAMetric = _IsisRAMetric_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 6),
    _IsisRAMetric_Type()
)
isisRAMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRAMetric.setStatus("current")


class _IsisRAMetricType_Type(IsisMetricType):
    """Custom type isisRAMetricType based on IsisMetricType"""


_IsisRAMetricType_Object = MibTableColumn
isisRAMetricType = _IsisRAMetricType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 7),
    _IsisRAMetricType_Type()
)
isisRAMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRAMetricType.setStatus("current")


class _IsisRASNPAAddress_Type(IsisOSINSAddress):
    """Custom type isisRASNPAAddress based on IsisOSINSAddress"""
    defaultHexValue = ""


_IsisRASNPAAddress_Object = MibTableColumn
isisRASNPAAddress = _IsisRASNPAAddress_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 8),
    _IsisRASNPAAddress_Type()
)
isisRASNPAAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRASNPAAddress.setStatus("current")


class _IsisRASNPAMask_Type(IsisOSINSAddress):
    """Custom type isisRASNPAMask based on IsisOSINSAddress"""
    defaultHexValue = "00"


_IsisRASNPAMask_Object = MibTableColumn
isisRASNPAMask = _IsisRASNPAMask_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 9),
    _IsisRASNPAMask_Type()
)
isisRASNPAMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRASNPAMask.setStatus("current")


class _IsisRASNPAPrefix_Type(IsisOSINSAddress):
    """Custom type isisRASNPAPrefix based on IsisOSINSAddress"""
    defaultHexValue = "00"


_IsisRASNPAPrefix_Object = MibTableColumn
isisRASNPAPrefix = _IsisRASNPAPrefix_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 10),
    _IsisRASNPAPrefix_Type()
)
isisRASNPAPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRASNPAPrefix.setStatus("current")


class _IsisRAType_Type(Integer32):
    """Custom type isisRAType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )


_IsisRAType_Type.__name__ = "Integer32"
_IsisRAType_Object = MibTableColumn
isisRAType = _IsisRAType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 7, 1, 1, 11),
    _IsisRAType_Type()
)
isisRAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRAType.setStatus("current")
_IsisIPReachAddr_ObjectIdentity = ObjectIdentity
isisIPReachAddr = _IsisIPReachAddr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 8)
)
_IsisIPRATable_Object = MibTable
isisIPRATable = _IsisIPRATable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1)
)
if mibBuilder.loadTexts:
    isisIPRATable.setStatus("current")
_IsisIPRAEntry_Object = MibTableRow
isisIPRAEntry = _IsisIPRAEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1)
)
isisIPRAEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysLevelIndex"),
    (0, "ISIS-MIB", "isisIPRADestType"),
    (0, "ISIS-MIB", "isisIPRADest"),
    (0, "ISIS-MIB", "isisIPRADestPrefixLen"),
    (0, "ISIS-MIB", "isisIPRANextHopIndex"),
)
if mibBuilder.loadTexts:
    isisIPRAEntry.setStatus("current")
_IsisIPRADestType_Type = InetAddressType
_IsisIPRADestType_Object = MibTableColumn
isisIPRADestType = _IsisIPRADestType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 1),
    _IsisIPRADestType_Type()
)
isisIPRADestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisIPRADestType.setStatus("current")
_IsisIPRADest_Type = InetAddress
_IsisIPRADest_Object = MibTableColumn
isisIPRADest = _IsisIPRADest_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 2),
    _IsisIPRADest_Type()
)
isisIPRADest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisIPRADest.setStatus("current")
_IsisIPRADestPrefixLen_Type = InetAddressPrefixLength
_IsisIPRADestPrefixLen_Object = MibTableColumn
isisIPRADestPrefixLen = _IsisIPRADestPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 3),
    _IsisIPRADestPrefixLen_Type()
)
isisIPRADestPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisIPRADestPrefixLen.setStatus("current")


class _IsisIPRANextHopIndex_Type(Unsigned32):
    """Custom type isisIPRANextHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IsisIPRANextHopIndex_Type.__name__ = "Unsigned32"
_IsisIPRANextHopIndex_Object = MibTableColumn
isisIPRANextHopIndex = _IsisIPRANextHopIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 4),
    _IsisIPRANextHopIndex_Type()
)
isisIPRANextHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisIPRANextHopIndex.setStatus("current")
_IsisIPRANextHopType_Type = InetAddressType
_IsisIPRANextHopType_Object = MibTableColumn
isisIPRANextHopType = _IsisIPRANextHopType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 5),
    _IsisIPRANextHopType_Type()
)
isisIPRANextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRANextHopType.setStatus("current")
_IsisIPRANextHop_Type = InetAddress
_IsisIPRANextHop_Object = MibTableColumn
isisIPRANextHop = _IsisIPRANextHop_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 6),
    _IsisIPRANextHop_Type()
)
isisIPRANextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRANextHop.setStatus("current")


class _IsisIPRAType_Type(Integer32):
    """Custom type isisIPRAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )


_IsisIPRAType_Type.__name__ = "Integer32"
_IsisIPRAType_Object = MibTableColumn
isisIPRAType = _IsisIPRAType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 7),
    _IsisIPRAType_Type()
)
isisIPRAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRAType.setStatus("current")
_IsisIPRAExistState_Type = RowStatus
_IsisIPRAExistState_Object = MibTableColumn
isisIPRAExistState = _IsisIPRAExistState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 8),
    _IsisIPRAExistState_Type()
)
isisIPRAExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRAExistState.setStatus("current")


class _IsisIPRAAdminState_Type(IsisAdminState):
    """Custom type isisIPRAAdminState based on IsisAdminState"""


_IsisIPRAAdminState_Object = MibTableColumn
isisIPRAAdminState = _IsisIPRAAdminState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 9),
    _IsisIPRAAdminState_Type()
)
isisIPRAAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRAAdminState.setStatus("current")


class _IsisIPRAMetric_Type(IsisDefaultMetric):
    """Custom type isisIPRAMetric based on IsisDefaultMetric"""
    defaultValue = 10


_IsisIPRAMetric_Object = MibTableColumn
isisIPRAMetric = _IsisIPRAMetric_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 10),
    _IsisIPRAMetric_Type()
)
isisIPRAMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRAMetric.setStatus("current")


class _IsisIPRAMetricType_Type(IsisMetricType):
    """Custom type isisIPRAMetricType based on IsisMetricType"""


_IsisIPRAMetricType_Object = MibTableColumn
isisIPRAMetricType = _IsisIPRAMetricType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 11),
    _IsisIPRAMetricType_Type()
)
isisIPRAMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRAMetricType.setStatus("current")


class _IsisIPRAFullMetric_Type(IsisFullMetric):
    """Custom type isisIPRAFullMetric based on IsisFullMetric"""
    defaultValue = 10


_IsisIPRAFullMetric_Object = MibTableColumn
isisIPRAFullMetric = _IsisIPRAFullMetric_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 12),
    _IsisIPRAFullMetric_Type()
)
isisIPRAFullMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRAFullMetric.setStatus("current")


class _IsisIPRASNPAAddress_Type(IsisOSINSAddress):
    """Custom type isisIPRASNPAAddress based on IsisOSINSAddress"""
    defaultHexValue = ""


_IsisIPRASNPAAddress_Object = MibTableColumn
isisIPRASNPAAddress = _IsisIPRASNPAAddress_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 13),
    _IsisIPRASNPAAddress_Type()
)
isisIPRASNPAAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisIPRASNPAAddress.setStatus("current")


class _IsisIPRASourceType_Type(Integer32):
    """Custom type isisIPRASourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 9),
          ("direct", 2),
          ("eigrp", 8),
          ("igrp", 7),
          ("isis", 5),
          ("ospfv2", 3),
          ("ospfv3", 4),
          ("other", 10),
          ("rip", 6),
          ("static", 1))
    )


_IsisIPRASourceType_Type.__name__ = "Integer32"
_IsisIPRASourceType_Object = MibTableColumn
isisIPRASourceType = _IsisIPRASourceType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 8, 1, 1, 14),
    _IsisIPRASourceType_Type()
)
isisIPRASourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRASourceType.setStatus("current")
_IsisLSPDataBase_ObjectIdentity = ObjectIdentity
isisLSPDataBase = _IsisLSPDataBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 9)
)
_IsisLSPSummaryTable_Object = MibTable
isisLSPSummaryTable = _IsisLSPSummaryTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 1)
)
if mibBuilder.loadTexts:
    isisLSPSummaryTable.setStatus("current")
_IsisLSPSummaryEntry_Object = MibTableRow
isisLSPSummaryEntry = _IsisLSPSummaryEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 1, 1)
)
isisLSPSummaryEntry.setIndexNames(
    (0, "ISIS-MIB", "isisLSPLevel"),
    (0, "ISIS-MIB", "isisLSPID"),
)
if mibBuilder.loadTexts:
    isisLSPSummaryEntry.setStatus("current")
_IsisLSPLevel_Type = IsisISLevel
_IsisLSPLevel_Object = MibTableColumn
isisLSPLevel = _IsisLSPLevel_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 1, 1, 1),
    _IsisLSPLevel_Type()
)
isisLSPLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisLSPLevel.setStatus("current")
_IsisLSPID_Type = IsisLinkStatePDUID
_IsisLSPID_Object = MibTableColumn
isisLSPID = _IsisLSPID_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 1, 1, 2),
    _IsisLSPID_Type()
)
isisLSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisLSPID.setStatus("current")
_IsisLSPSeq_Type = Unsigned32
_IsisLSPSeq_Object = MibTableColumn
isisLSPSeq = _IsisLSPSeq_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 1, 1, 3),
    _IsisLSPSeq_Type()
)
isisLSPSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPSeq.setStatus("current")
_IsisLSPZeroLife_Type = TruthValue
_IsisLSPZeroLife_Object = MibTableColumn
isisLSPZeroLife = _IsisLSPZeroLife_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 1, 1, 4),
    _IsisLSPZeroLife_Type()
)
isisLSPZeroLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPZeroLife.setStatus("current")
_IsisLSPChecksum_Type = IsisUnsigned16TC
_IsisLSPChecksum_Object = MibTableColumn
isisLSPChecksum = _IsisLSPChecksum_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 1, 1, 5),
    _IsisLSPChecksum_Type()
)
isisLSPChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPChecksum.setStatus("current")
_IsisLSPLifetimeRemain_Type = IsisUnsigned16TC
_IsisLSPLifetimeRemain_Object = MibTableColumn
isisLSPLifetimeRemain = _IsisLSPLifetimeRemain_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 1, 1, 6),
    _IsisLSPLifetimeRemain_Type()
)
isisLSPLifetimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPLifetimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    isisLSPLifetimeRemain.setUnits("seconds")
_IsisLSPPDULength_Type = IsisUnsigned16TC
_IsisLSPPDULength_Object = MibTableColumn
isisLSPPDULength = _IsisLSPPDULength_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 1, 1, 7),
    _IsisLSPPDULength_Type()
)
isisLSPPDULength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPPDULength.setStatus("current")
_IsisLSPAttributes_Type = IsisUnsigned8TC
_IsisLSPAttributes_Object = MibTableColumn
isisLSPAttributes = _IsisLSPAttributes_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 1, 1, 8),
    _IsisLSPAttributes_Type()
)
isisLSPAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPAttributes.setStatus("current")
_IsisLSPTLVTable_Object = MibTable
isisLSPTLVTable = _IsisLSPTLVTable_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 2)
)
if mibBuilder.loadTexts:
    isisLSPTLVTable.setStatus("current")
_IsisLSPTLVEntry_Object = MibTableRow
isisLSPTLVEntry = _IsisLSPTLVEntry_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 2, 1)
)
isisLSPTLVEntry.setIndexNames(
    (0, "ISIS-MIB", "isisLSPLevel"),
    (0, "ISIS-MIB", "isisLSPID"),
    (0, "ISIS-MIB", "isisLSPTLVIndex"),
)
if mibBuilder.loadTexts:
    isisLSPTLVEntry.setStatus("current")


class _IsisLSPTLVIndex_Type(Unsigned32):
    """Custom type isisLSPTLVIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IsisLSPTLVIndex_Type.__name__ = "Unsigned32"
_IsisLSPTLVIndex_Object = MibTableColumn
isisLSPTLVIndex = _IsisLSPTLVIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 2, 1, 1),
    _IsisLSPTLVIndex_Type()
)
isisLSPTLVIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisLSPTLVIndex.setStatus("current")
_IsisLSPTLVSeq_Type = Unsigned32
_IsisLSPTLVSeq_Object = MibTableColumn
isisLSPTLVSeq = _IsisLSPTLVSeq_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 2, 1, 2),
    _IsisLSPTLVSeq_Type()
)
isisLSPTLVSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPTLVSeq.setStatus("current")
_IsisLSPTLVChecksum_Type = IsisUnsigned16TC
_IsisLSPTLVChecksum_Object = MibTableColumn
isisLSPTLVChecksum = _IsisLSPTLVChecksum_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 2, 1, 3),
    _IsisLSPTLVChecksum_Type()
)
isisLSPTLVChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPTLVChecksum.setStatus("current")
_IsisLSPTLVType_Type = IsisUnsigned8TC
_IsisLSPTLVType_Object = MibTableColumn
isisLSPTLVType = _IsisLSPTLVType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 2, 1, 4),
    _IsisLSPTLVType_Type()
)
isisLSPTLVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPTLVType.setStatus("current")
_IsisLSPTLVLen_Type = IsisUnsigned8TC
_IsisLSPTLVLen_Object = MibTableColumn
isisLSPTLVLen = _IsisLSPTLVLen_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 2, 1, 5),
    _IsisLSPTLVLen_Type()
)
isisLSPTLVLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPTLVLen.setStatus("current")


class _IsisLSPTLVValue_Type(OctetString):
    """Custom type isisLSPTLVValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IsisLSPTLVValue_Type.__name__ = "OctetString"
_IsisLSPTLVValue_Object = MibTableColumn
isisLSPTLVValue = _IsisLSPTLVValue_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 9, 2, 1, 6),
    _IsisLSPTLVValue_Type()
)
isisLSPTLVValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPTLVValue.setStatus("current")
_IsisNotification_ObjectIdentity = ObjectIdentity
isisNotification = _IsisNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 10)
)
_IsisNotificationEntry_ObjectIdentity = ObjectIdentity
isisNotificationEntry = _IsisNotificationEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1)
)
_IsisNotificationSysLevelIndex_Type = IsisLevel
_IsisNotificationSysLevelIndex_Object = MibScalar
isisNotificationSysLevelIndex = _IsisNotificationSysLevelIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 1),
    _IsisNotificationSysLevelIndex_Type()
)
isisNotificationSysLevelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationSysLevelIndex.setStatus("current")


class _IsisNotificationCircIfIndex_Type(Unsigned32):
    """Custom type isisNotificationCircIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsisNotificationCircIfIndex_Type.__name__ = "Unsigned32"
_IsisNotificationCircIfIndex_Object = MibScalar
isisNotificationCircIfIndex = _IsisNotificationCircIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 2),
    _IsisNotificationCircIfIndex_Type()
)
isisNotificationCircIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationCircIfIndex.setStatus("current")
_IsisPduLspId_Type = IsisLinkStatePDUID
_IsisPduLspId_Object = MibScalar
isisPduLspId = _IsisPduLspId_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 3),
    _IsisPduLspId_Type()
)
isisPduLspId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduLspId.setStatus("current")
_IsisPduFragment_Type = IsisPDUHeader
_IsisPduFragment_Object = MibScalar
isisPduFragment = _IsisPduFragment_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 4),
    _IsisPduFragment_Type()
)
isisPduFragment.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduFragment.setStatus("current")
_IsisPduFieldLen_Type = IsisUnsigned8TC
_IsisPduFieldLen_Object = MibScalar
isisPduFieldLen = _IsisPduFieldLen_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 5),
    _IsisPduFieldLen_Type()
)
isisPduFieldLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduFieldLen.setStatus("current")
_IsisPduMaxAreaAddress_Type = IsisUnsigned8TC
_IsisPduMaxAreaAddress_Object = MibScalar
isisPduMaxAreaAddress = _IsisPduMaxAreaAddress_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 6),
    _IsisPduMaxAreaAddress_Type()
)
isisPduMaxAreaAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduMaxAreaAddress.setStatus("current")
_IsisPduProtocolVersion_Type = IsisUnsigned8TC
_IsisPduProtocolVersion_Object = MibScalar
isisPduProtocolVersion = _IsisPduProtocolVersion_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 7),
    _IsisPduProtocolVersion_Type()
)
isisPduProtocolVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduProtocolVersion.setStatus("current")


class _IsisPduLspSize_Type(Unsigned32):
    """Custom type isisPduLspSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IsisPduLspSize_Type.__name__ = "Unsigned32"
_IsisPduLspSize_Object = MibScalar
isisPduLspSize = _IsisPduLspSize_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 8),
    _IsisPduLspSize_Type()
)
isisPduLspSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduLspSize.setStatus("current")


class _IsisPduOriginatingBufferSize_Type(IsisUnsigned16TC):
    """Custom type isisPduOriginatingBufferSize based on IsisUnsigned16TC"""
    subtypeSpec = IsisUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_IsisPduOriginatingBufferSize_Type.__name__ = "IsisUnsigned16TC"
_IsisPduOriginatingBufferSize_Object = MibScalar
isisPduOriginatingBufferSize = _IsisPduOriginatingBufferSize_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 9),
    _IsisPduOriginatingBufferSize_Type()
)
isisPduOriginatingBufferSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduOriginatingBufferSize.setStatus("current")


class _IsisPduBufferSize_Type(IsisUnsigned16TC):
    """Custom type isisPduBufferSize based on IsisUnsigned16TC"""
    subtypeSpec = IsisUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_IsisPduBufferSize_Type.__name__ = "IsisUnsigned16TC"
_IsisPduBufferSize_Object = MibScalar
isisPduBufferSize = _IsisPduBufferSize_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 10),
    _IsisPduBufferSize_Type()
)
isisPduBufferSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduBufferSize.setStatus("current")


class _IsisPduProtocolsSupported_Type(OctetString):
    """Custom type isisPduProtocolsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IsisPduProtocolsSupported_Type.__name__ = "OctetString"
_IsisPduProtocolsSupported_Object = MibScalar
isisPduProtocolsSupported = _IsisPduProtocolsSupported_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 11),
    _IsisPduProtocolsSupported_Type()
)
isisPduProtocolsSupported.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduProtocolsSupported.setStatus("current")


class _IsisAdjState_Type(Integer32):
    """Custom type isisAdjState based on Integer32"""
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
        *(("down", 1),
          ("failed", 4),
          ("initializing", 2),
          ("up", 3))
    )


_IsisAdjState_Type.__name__ = "Integer32"
_IsisAdjState_Object = MibScalar
isisAdjState = _IsisAdjState_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 12),
    _IsisAdjState_Type()
)
isisAdjState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisAdjState.setStatus("current")
_IsisErrorOffset_Type = Unsigned32
_IsisErrorOffset_Object = MibScalar
isisErrorOffset = _IsisErrorOffset_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 13),
    _IsisErrorOffset_Type()
)
isisErrorOffset.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisErrorOffset.setStatus("current")


class _IsisErrorTLVType_Type(Unsigned32):
    """Custom type isisErrorTLVType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsisErrorTLVType_Type.__name__ = "Unsigned32"
_IsisErrorTLVType_Object = MibScalar
isisErrorTLVType = _IsisErrorTLVType_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 14),
    _IsisErrorTLVType_Type()
)
isisErrorTLVType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisErrorTLVType.setStatus("current")
_IsisNotificationAreaAddress_Type = IsisOSINSAddress
_IsisNotificationAreaAddress_Object = MibScalar
isisNotificationAreaAddress = _IsisNotificationAreaAddress_Object(
    (1, 3, 6, 1, 2, 1, 138, 1, 10, 1, 15),
    _IsisNotificationAreaAddress_Type()
)
isisNotificationAreaAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationAreaAddress.setStatus("current")
_IsisConformance_ObjectIdentity = ObjectIdentity
isisConformance = _IsisConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 2)
)
_IsisCompliances_ObjectIdentity = ObjectIdentity
isisCompliances = _IsisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 2, 1)
)
_IsisGroups_ObjectIdentity = ObjectIdentity
isisGroups = _IsisGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 138, 2, 2)
)

# Managed Objects groups

isisSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 138, 2, 2, 1)
)
isisSystemGroup.setObjects(
      *(("ISIS-MIB", "isisSysVersion"),
        ("ISIS-MIB", "isisSysLevelType"),
        ("ISIS-MIB", "isisSysID"),
        ("ISIS-MIB", "isisSysMaxPathSplits"),
        ("ISIS-MIB", "isisSysMaxLSPGenInt"),
        ("ISIS-MIB", "isisSysPollESHelloRate"),
        ("ISIS-MIB", "isisSysWaitTime"),
        ("ISIS-MIB", "isisSysAdminState"),
        ("ISIS-MIB", "isisSysL2toL1Leaking"),
        ("ISIS-MIB", "isisSysMaxAge"),
        ("ISIS-MIB", "isisSysProtSupported"),
        ("ISIS-MIB", "isisSysNotificationEnable"),
        ("ISIS-MIB", "isisManAreaAddrExistState"),
        ("ISIS-MIB", "isisSysLevelOrigLSPBuffSize"),
        ("ISIS-MIB", "isisSysLevelMinLSPGenInt"),
        ("ISIS-MIB", "isisSysLevelState"),
        ("ISIS-MIB", "isisSysLevelSetOverload"),
        ("ISIS-MIB", "isisSysLevelSetOverloadUntil"),
        ("ISIS-MIB", "isisSysLevelMetricStyle"),
        ("ISIS-MIB", "isisSysLevelSPFConsiders"),
        ("ISIS-MIB", "isisSysLevelTEEnabled"),
        ("ISIS-MIB", "isisSysReceiveLSPBufferSize"),
        ("ISIS-MIB", "isisSummAddrExistState"),
        ("ISIS-MIB", "isisSummAddrMetric"),
        ("ISIS-MIB", "isisAreaAddr"),
        ("ISIS-MIB", "isisSummAddrFullMetric"),
        ("ISIS-MIB", "isisRedistributeAddrExistState"),
        ("ISIS-MIB", "isisRouterHostName"),
        ("ISIS-MIB", "isisRouterID"),
        ("ISIS-MIB", "isisSysStatCorrLSPs"),
        ("ISIS-MIB", "isisSysStatLSPDbaseOloads"),
        ("ISIS-MIB", "isisSysStatManAddrDropFromAreas"),
        ("ISIS-MIB", "isisSysStatAttmptToExMaxSeqNums"),
        ("ISIS-MIB", "isisSysStatSeqNumSkips"),
        ("ISIS-MIB", "isisSysStatOwnLSPPurges"),
        ("ISIS-MIB", "isisSysStatIDFieldLenMismatches"),
        ("ISIS-MIB", "isisSysStatPartChanges"),
        ("ISIS-MIB", "isisSysStatSPFRuns"),
        ("ISIS-MIB", "isisSysStatAuthTypeFails"),
        ("ISIS-MIB", "isisSysStatAuthFails"),
        ("ISIS-MIB", "isisSysStatLSPErrors"))
)
if mibBuilder.loadTexts:
    isisSystemGroup.setStatus("current")

isisCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 138, 2, 2, 2)
)
isisCircuitGroup.setObjects(
      *(("ISIS-MIB", "isisNextCircIndex"),
        ("ISIS-MIB", "isisCircAdminState"),
        ("ISIS-MIB", "isisCircExistState"),
        ("ISIS-MIB", "isisCircType"),
        ("ISIS-MIB", "isisCircExtDomain"),
        ("ISIS-MIB", "isisCircLevelType"),
        ("ISIS-MIB", "isisCircAdjChanges"),
        ("ISIS-MIB", "isisCircNumAdj"),
        ("ISIS-MIB", "isisCircInitFails"),
        ("ISIS-MIB", "isisCircRejAdjs"),
        ("ISIS-MIB", "isisCircIDFieldLenMismatches"),
        ("ISIS-MIB", "isisCircMaxAreaAddrMismatches"),
        ("ISIS-MIB", "isisCircAuthTypeFails"),
        ("ISIS-MIB", "isisCircAuthFails"),
        ("ISIS-MIB", "isisCircLANDesISChanges"),
        ("ISIS-MIB", "isisCircPassiveCircuit"),
        ("ISIS-MIB", "isisCircMeshGroupEnabled"),
        ("ISIS-MIB", "isisCircMeshGroup"),
        ("ISIS-MIB", "isisCircSmallHellos"),
        ("ISIS-MIB", "isisCircLastUpTime"),
        ("ISIS-MIB", "isisCirc3WayEnabled"),
        ("ISIS-MIB", "isisCircExtendedCircID"),
        ("ISIS-MIB", "isisCircIfIndex"),
        ("ISIS-MIB", "isisCircLevelMetric"),
        ("ISIS-MIB", "isisCircLevelWideMetric"),
        ("ISIS-MIB", "isisCircLevelISPriority"),
        ("ISIS-MIB", "isisCircLevelIDOctet"),
        ("ISIS-MIB", "isisCircLevelID"),
        ("ISIS-MIB", "isisCircLevelDesIS"),
        ("ISIS-MIB", "isisCircLevelHelloMultiplier"),
        ("ISIS-MIB", "isisCircLevelHelloTimer"),
        ("ISIS-MIB", "isisCircLevelDRHelloTimer"),
        ("ISIS-MIB", "isisCircLevelLSPThrottle"),
        ("ISIS-MIB", "isisCircLevelMinLSPRetransInt"),
        ("ISIS-MIB", "isisCircLevelCSNPInterval"),
        ("ISIS-MIB", "isisCircLevelPartSNPInterval"))
)
if mibBuilder.loadTexts:
    isisCircuitGroup.setStatus("current")

isisISAdjGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 138, 2, 2, 3)
)
isisISAdjGroup.setObjects(
      *(("ISIS-MIB", "isisISAdjState"),
        ("ISIS-MIB", "isisISAdj3WayState"),
        ("ISIS-MIB", "isisISAdjNeighSNPAAddress"),
        ("ISIS-MIB", "isisISAdjNeighSysType"),
        ("ISIS-MIB", "isisISAdjNeighSysID"),
        ("ISIS-MIB", "isisISAdjNbrExtendedCircID"),
        ("ISIS-MIB", "isisISAdjUsage"),
        ("ISIS-MIB", "isisISAdjHoldTimer"),
        ("ISIS-MIB", "isisISAdjNeighPriority"),
        ("ISIS-MIB", "isisISAdjLastUpTime"),
        ("ISIS-MIB", "isisISAdjAreaAddress"),
        ("ISIS-MIB", "isisISAdjIPAddrType"),
        ("ISIS-MIB", "isisISAdjIPAddrAddress"),
        ("ISIS-MIB", "isisISAdjProtSuppProtocol"))
)
if mibBuilder.loadTexts:
    isisISAdjGroup.setStatus("current")

isisNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 138, 2, 2, 4)
)
isisNotificationObjectGroup.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduLspId"),
        ("ISIS-MIB", "isisPduFragment"),
        ("ISIS-MIB", "isisPduFieldLen"),
        ("ISIS-MIB", "isisPduMaxAreaAddress"),
        ("ISIS-MIB", "isisPduProtocolVersion"),
        ("ISIS-MIB", "isisPduLspSize"),
        ("ISIS-MIB", "isisPduOriginatingBufferSize"),
        ("ISIS-MIB", "isisPduBufferSize"),
        ("ISIS-MIB", "isisPduProtocolsSupported"),
        ("ISIS-MIB", "isisAdjState"),
        ("ISIS-MIB", "isisErrorOffset"),
        ("ISIS-MIB", "isisErrorTLVType"),
        ("ISIS-MIB", "isisNotificationAreaAddress"))
)
if mibBuilder.loadTexts:
    isisNotificationObjectGroup.setStatus("current")

isisISPDUCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 138, 2, 2, 6)
)
isisISPDUCounterGroup.setObjects(
      *(("ISIS-MIB", "isisPacketCountIIHello"),
        ("ISIS-MIB", "isisPacketCountISHello"),
        ("ISIS-MIB", "isisPacketCountESHello"),
        ("ISIS-MIB", "isisPacketCountLSP"),
        ("ISIS-MIB", "isisPacketCountCSNP"),
        ("ISIS-MIB", "isisPacketCountPSNP"),
        ("ISIS-MIB", "isisPacketCountUnknown"))
)
if mibBuilder.loadTexts:
    isisISPDUCounterGroup.setStatus("current")

isisRATableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 138, 2, 2, 7)
)
isisRATableGroup.setObjects(
      *(("ISIS-MIB", "isisRAExistState"),
        ("ISIS-MIB", "isisRAAdminState"),
        ("ISIS-MIB", "isisRAAddrPrefix"),
        ("ISIS-MIB", "isisRAMapType"),
        ("ISIS-MIB", "isisRAMetric"),
        ("ISIS-MIB", "isisRAMetricType"),
        ("ISIS-MIB", "isisRASNPAAddress"),
        ("ISIS-MIB", "isisRASNPAMask"),
        ("ISIS-MIB", "isisRASNPAPrefix"),
        ("ISIS-MIB", "isisRAType"))
)
if mibBuilder.loadTexts:
    isisRATableGroup.setStatus("current")

isisISIPRADestGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 138, 2, 2, 8)
)
isisISIPRADestGroup.setObjects(
      *(("ISIS-MIB", "isisIPRANextHopType"),
        ("ISIS-MIB", "isisIPRANextHop"),
        ("ISIS-MIB", "isisIPRAType"),
        ("ISIS-MIB", "isisIPRAExistState"),
        ("ISIS-MIB", "isisIPRAAdminState"),
        ("ISIS-MIB", "isisIPRAMetric"),
        ("ISIS-MIB", "isisIPRAFullMetric"),
        ("ISIS-MIB", "isisIPRAMetricType"),
        ("ISIS-MIB", "isisIPRASNPAAddress"),
        ("ISIS-MIB", "isisIPRASourceType"))
)
if mibBuilder.loadTexts:
    isisISIPRADestGroup.setStatus("current")

isisLSPGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 138, 2, 2, 9)
)
isisLSPGroup.setObjects(
      *(("ISIS-MIB", "isisLSPSeq"),
        ("ISIS-MIB", "isisLSPZeroLife"),
        ("ISIS-MIB", "isisLSPChecksum"),
        ("ISIS-MIB", "isisLSPLifetimeRemain"),
        ("ISIS-MIB", "isisLSPPDULength"),
        ("ISIS-MIB", "isisLSPAttributes"),
        ("ISIS-MIB", "isisLSPTLVSeq"),
        ("ISIS-MIB", "isisLSPTLVChecksum"),
        ("ISIS-MIB", "isisLSPTLVType"),
        ("ISIS-MIB", "isisLSPTLVLen"),
        ("ISIS-MIB", "isisLSPTLVValue"))
)
if mibBuilder.loadTexts:
    isisLSPGroup.setStatus("current")


# Notification objects

isisDatabaseOverload = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 1)
)
isisDatabaseOverload.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisSysLevelState"))
)
if mibBuilder.loadTexts:
    isisDatabaseOverload.setStatus(
        "current"
    )

isisManualAddressDrops = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 2)
)
isisManualAddressDrops.setObjects(
    ("ISIS-MIB", "isisNotificationAreaAddress")
)
if mibBuilder.loadTexts:
    isisManualAddressDrops.setStatus(
        "current"
    )

isisCorruptedLSPDetected = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 3)
)
isisCorruptedLSPDetected.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisPduLspId"))
)
if mibBuilder.loadTexts:
    isisCorruptedLSPDetected.setStatus(
        "current"
    )

isisAttemptToExceedMaxSequence = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 4)
)
isisAttemptToExceedMaxSequence.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisPduLspId"))
)
if mibBuilder.loadTexts:
    isisAttemptToExceedMaxSequence.setStatus(
        "current"
    )

isisIDLenMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 5)
)
isisIDLenMismatch.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisPduFieldLen"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisIDLenMismatch.setStatus(
        "current"
    )

isisMaxAreaAddressesMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 6)
)
isisMaxAreaAddressesMismatch.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisPduMaxAreaAddress"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisMaxAreaAddressesMismatch.setStatus(
        "current"
    )

isisOwnLSPPurge = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 7)
)
isisOwnLSPPurge.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduLspId"))
)
if mibBuilder.loadTexts:
    isisOwnLSPPurge.setStatus(
        "current"
    )

isisSequenceNumberSkip = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 8)
)
isisSequenceNumberSkip.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduLspId"))
)
if mibBuilder.loadTexts:
    isisSequenceNumberSkip.setStatus(
        "current"
    )

isisAuthenticationTypeFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 9)
)
isisAuthenticationTypeFailure.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisAuthenticationTypeFailure.setStatus(
        "current"
    )

isisAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 10)
)
isisAuthenticationFailure.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisAuthenticationFailure.setStatus(
        "current"
    )

isisVersionSkew = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 11)
)
isisVersionSkew.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduProtocolVersion"),
        ("ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisVersionSkew.setStatus(
        "current"
    )

isisAreaMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 12)
)
isisAreaMismatch.setObjects(
      *(("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisAreaMismatch.setStatus(
        "current"
    )

isisRejectedAdjacency = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 13)
)
isisRejectedAdjacency.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisRejectedAdjacency.setStatus(
        "current"
    )

isisLSPTooLargeToPropagate = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 14)
)
isisLSPTooLargeToPropagate.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduLspSize"),
        ("ISIS-MIB", "isisPduLspId"))
)
if mibBuilder.loadTexts:
    isisLSPTooLargeToPropagate.setStatus(
        "current"
    )

isisOrigLSPBuffSizeMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 15)
)
isisOrigLSPBuffSizeMismatch.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduLspId"),
        ("ISIS-MIB", "isisPduOriginatingBufferSize"),
        ("ISIS-MIB", "isisPduBufferSize"))
)
if mibBuilder.loadTexts:
    isisOrigLSPBuffSizeMismatch.setStatus(
        "current"
    )

isisProtocolsSupportedMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 16)
)
isisProtocolsSupportedMismatch.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduProtocolsSupported"),
        ("ISIS-MIB", "isisPduLspId"),
        ("ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisProtocolsSupportedMismatch.setStatus(
        "current"
    )

isisAdjacencyChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 17)
)
isisAdjacencyChange.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduLspId"),
        ("ISIS-MIB", "isisAdjState"))
)
if mibBuilder.loadTexts:
    isisAdjacencyChange.setStatus(
        "current"
    )

isisLSPErrorDetected = NotificationType(
    (1, 3, 6, 1, 2, 1, 138, 0, 18)
)
isisLSPErrorDetected.setObjects(
      *(("ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("ISIS-MIB", "isisPduLspId"),
        ("ISIS-MIB", "isisNotificationCircIfIndex"),
        ("ISIS-MIB", "isisPduFragment"),
        ("ISIS-MIB", "isisErrorOffset"),
        ("ISIS-MIB", "isisErrorTLVType"))
)
if mibBuilder.loadTexts:
    isisLSPErrorDetected.setStatus(
        "current"
    )


# Notifications groups

isisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 138, 2, 2, 5)
)
isisNotificationGroup.setObjects(
      *(("ISIS-MIB", "isisDatabaseOverload"),
        ("ISIS-MIB", "isisManualAddressDrops"),
        ("ISIS-MIB", "isisCorruptedLSPDetected"),
        ("ISIS-MIB", "isisAttemptToExceedMaxSequence"),
        ("ISIS-MIB", "isisIDLenMismatch"),
        ("ISIS-MIB", "isisMaxAreaAddressesMismatch"),
        ("ISIS-MIB", "isisOwnLSPPurge"),
        ("ISIS-MIB", "isisSequenceNumberSkip"),
        ("ISIS-MIB", "isisAuthenticationTypeFailure"),
        ("ISIS-MIB", "isisAuthenticationFailure"),
        ("ISIS-MIB", "isisVersionSkew"),
        ("ISIS-MIB", "isisAreaMismatch"),
        ("ISIS-MIB", "isisRejectedAdjacency"),
        ("ISIS-MIB", "isisLSPTooLargeToPropagate"),
        ("ISIS-MIB", "isisOrigLSPBuffSizeMismatch"),
        ("ISIS-MIB", "isisProtocolsSupportedMismatch"),
        ("ISIS-MIB", "isisAdjacencyChange"),
        ("ISIS-MIB", "isisLSPErrorDetected"))
)
if mibBuilder.loadTexts:
    isisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

isisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 138, 2, 1, 1)
)
if mibBuilder.loadTexts:
    isisCompliance.setStatus(
        "current"
    )

isisAdvancedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 138, 2, 1, 2)
)
if mibBuilder.loadTexts:
    isisAdvancedCompliance.setStatus(
        "current"
    )

isisReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 138, 2, 1, 3)
)
if mibBuilder.loadTexts:
    isisReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISIS-MIB",
    **{"IsisOSINSAddress": IsisOSINSAddress,
       "IsisSystemID": IsisSystemID,
       "IsisLinkStatePDUID": IsisLinkStatePDUID,
       "IsisAdminState": IsisAdminState,
       "IsisLSPBuffSize": IsisLSPBuffSize,
       "IsisLevelState": IsisLevelState,
       "IsisSupportedProtocol": IsisSupportedProtocol,
       "IsisDefaultMetric": IsisDefaultMetric,
       "IsisWideMetric": IsisWideMetric,
       "IsisFullMetric": IsisFullMetric,
       "IsisMetricType": IsisMetricType,
       "IsisMetricStyle": IsisMetricStyle,
       "IsisISLevel": IsisISLevel,
       "IsisLevel": IsisLevel,
       "IsisPDUHeader": IsisPDUHeader,
       "IsisCircuitID": IsisCircuitID,
       "IsisISPriority": IsisISPriority,
       "IsisUnsigned16TC": IsisUnsigned16TC,
       "IsisUnsigned8TC": IsisUnsigned8TC,
       "isisMIB": isisMIB,
       "isisNotifications": isisNotifications,
       "isisDatabaseOverload": isisDatabaseOverload,
       "isisManualAddressDrops": isisManualAddressDrops,
       "isisCorruptedLSPDetected": isisCorruptedLSPDetected,
       "isisAttemptToExceedMaxSequence": isisAttemptToExceedMaxSequence,
       "isisIDLenMismatch": isisIDLenMismatch,
       "isisMaxAreaAddressesMismatch": isisMaxAreaAddressesMismatch,
       "isisOwnLSPPurge": isisOwnLSPPurge,
       "isisSequenceNumberSkip": isisSequenceNumberSkip,
       "isisAuthenticationTypeFailure": isisAuthenticationTypeFailure,
       "isisAuthenticationFailure": isisAuthenticationFailure,
       "isisVersionSkew": isisVersionSkew,
       "isisAreaMismatch": isisAreaMismatch,
       "isisRejectedAdjacency": isisRejectedAdjacency,
       "isisLSPTooLargeToPropagate": isisLSPTooLargeToPropagate,
       "isisOrigLSPBuffSizeMismatch": isisOrigLSPBuffSizeMismatch,
       "isisProtocolsSupportedMismatch": isisProtocolsSupportedMismatch,
       "isisAdjacencyChange": isisAdjacencyChange,
       "isisLSPErrorDetected": isisLSPErrorDetected,
       "isisObjects": isisObjects,
       "isisSystem": isisSystem,
       "isisSysObject": isisSysObject,
       "isisSysVersion": isisSysVersion,
       "isisSysLevelType": isisSysLevelType,
       "isisSysID": isisSysID,
       "isisSysMaxPathSplits": isisSysMaxPathSplits,
       "isisSysMaxLSPGenInt": isisSysMaxLSPGenInt,
       "isisSysPollESHelloRate": isisSysPollESHelloRate,
       "isisSysWaitTime": isisSysWaitTime,
       "isisSysAdminState": isisSysAdminState,
       "isisSysL2toL1Leaking": isisSysL2toL1Leaking,
       "isisSysMaxAge": isisSysMaxAge,
       "isisSysReceiveLSPBufferSize": isisSysReceiveLSPBufferSize,
       "isisSysProtSupported": isisSysProtSupported,
       "isisSysNotificationEnable": isisSysNotificationEnable,
       "isisManAreaAddrTable": isisManAreaAddrTable,
       "isisManAreaAddrEntry": isisManAreaAddrEntry,
       "isisManAreaAddr": isisManAreaAddr,
       "isisManAreaAddrExistState": isisManAreaAddrExistState,
       "isisAreaAddrTable": isisAreaAddrTable,
       "isisAreaAddrEntry": isisAreaAddrEntry,
       "isisAreaAddr": isisAreaAddr,
       "isisSummAddrTable": isisSummAddrTable,
       "isisSummAddrEntry": isisSummAddrEntry,
       "isisSummAddressType": isisSummAddressType,
       "isisSummAddress": isisSummAddress,
       "isisSummAddrPrefixLen": isisSummAddrPrefixLen,
       "isisSummAddrExistState": isisSummAddrExistState,
       "isisSummAddrMetric": isisSummAddrMetric,
       "isisSummAddrFullMetric": isisSummAddrFullMetric,
       "isisRedistributeAddrTable": isisRedistributeAddrTable,
       "isisRedistributeAddrEntry": isisRedistributeAddrEntry,
       "isisRedistributeAddrType": isisRedistributeAddrType,
       "isisRedistributeAddrAddress": isisRedistributeAddrAddress,
       "isisRedistributeAddrPrefixLen": isisRedistributeAddrPrefixLen,
       "isisRedistributeAddrExistState": isisRedistributeAddrExistState,
       "isisRouterTable": isisRouterTable,
       "isisRouterEntry": isisRouterEntry,
       "isisRouterSysID": isisRouterSysID,
       "isisRouterLevel": isisRouterLevel,
       "isisRouterHostName": isisRouterHostName,
       "isisRouterID": isisRouterID,
       "isisSysLevel": isisSysLevel,
       "isisSysLevelTable": isisSysLevelTable,
       "isisSysLevelEntry": isisSysLevelEntry,
       "isisSysLevelIndex": isisSysLevelIndex,
       "isisSysLevelOrigLSPBuffSize": isisSysLevelOrigLSPBuffSize,
       "isisSysLevelMinLSPGenInt": isisSysLevelMinLSPGenInt,
       "isisSysLevelState": isisSysLevelState,
       "isisSysLevelSetOverload": isisSysLevelSetOverload,
       "isisSysLevelSetOverloadUntil": isisSysLevelSetOverloadUntil,
       "isisSysLevelMetricStyle": isisSysLevelMetricStyle,
       "isisSysLevelSPFConsiders": isisSysLevelSPFConsiders,
       "isisSysLevelTEEnabled": isisSysLevelTEEnabled,
       "isisCirc": isisCirc,
       "isisNextCircIndex": isisNextCircIndex,
       "isisCircTable": isisCircTable,
       "isisCircEntry": isisCircEntry,
       "isisCircIndex": isisCircIndex,
       "isisCircIfIndex": isisCircIfIndex,
       "isisCircAdminState": isisCircAdminState,
       "isisCircExistState": isisCircExistState,
       "isisCircType": isisCircType,
       "isisCircExtDomain": isisCircExtDomain,
       "isisCircLevelType": isisCircLevelType,
       "isisCircPassiveCircuit": isisCircPassiveCircuit,
       "isisCircMeshGroupEnabled": isisCircMeshGroupEnabled,
       "isisCircMeshGroup": isisCircMeshGroup,
       "isisCircSmallHellos": isisCircSmallHellos,
       "isisCircLastUpTime": isisCircLastUpTime,
       "isisCirc3WayEnabled": isisCirc3WayEnabled,
       "isisCircExtendedCircID": isisCircExtendedCircID,
       "isisCircLevelValues": isisCircLevelValues,
       "isisCircLevelTable": isisCircLevelTable,
       "isisCircLevelEntry": isisCircLevelEntry,
       "isisCircLevelIndex": isisCircLevelIndex,
       "isisCircLevelMetric": isisCircLevelMetric,
       "isisCircLevelWideMetric": isisCircLevelWideMetric,
       "isisCircLevelISPriority": isisCircLevelISPriority,
       "isisCircLevelIDOctet": isisCircLevelIDOctet,
       "isisCircLevelID": isisCircLevelID,
       "isisCircLevelDesIS": isisCircLevelDesIS,
       "isisCircLevelHelloMultiplier": isisCircLevelHelloMultiplier,
       "isisCircLevelHelloTimer": isisCircLevelHelloTimer,
       "isisCircLevelDRHelloTimer": isisCircLevelDRHelloTimer,
       "isisCircLevelLSPThrottle": isisCircLevelLSPThrottle,
       "isisCircLevelMinLSPRetransInt": isisCircLevelMinLSPRetransInt,
       "isisCircLevelCSNPInterval": isisCircLevelCSNPInterval,
       "isisCircLevelPartSNPInterval": isisCircLevelPartSNPInterval,
       "isisCounters": isisCounters,
       "isisSystemCounterTable": isisSystemCounterTable,
       "isisSystemCounterEntry": isisSystemCounterEntry,
       "isisSysStatLevel": isisSysStatLevel,
       "isisSysStatCorrLSPs": isisSysStatCorrLSPs,
       "isisSysStatAuthTypeFails": isisSysStatAuthTypeFails,
       "isisSysStatAuthFails": isisSysStatAuthFails,
       "isisSysStatLSPDbaseOloads": isisSysStatLSPDbaseOloads,
       "isisSysStatManAddrDropFromAreas": isisSysStatManAddrDropFromAreas,
       "isisSysStatAttmptToExMaxSeqNums": isisSysStatAttmptToExMaxSeqNums,
       "isisSysStatSeqNumSkips": isisSysStatSeqNumSkips,
       "isisSysStatOwnLSPPurges": isisSysStatOwnLSPPurges,
       "isisSysStatIDFieldLenMismatches": isisSysStatIDFieldLenMismatches,
       "isisSysStatPartChanges": isisSysStatPartChanges,
       "isisSysStatSPFRuns": isisSysStatSPFRuns,
       "isisSysStatLSPErrors": isisSysStatLSPErrors,
       "isisCircuitCounterTable": isisCircuitCounterTable,
       "isisCircuitCounterEntry": isisCircuitCounterEntry,
       "isisCircuitType": isisCircuitType,
       "isisCircAdjChanges": isisCircAdjChanges,
       "isisCircNumAdj": isisCircNumAdj,
       "isisCircInitFails": isisCircInitFails,
       "isisCircRejAdjs": isisCircRejAdjs,
       "isisCircIDFieldLenMismatches": isisCircIDFieldLenMismatches,
       "isisCircMaxAreaAddrMismatches": isisCircMaxAreaAddrMismatches,
       "isisCircAuthTypeFails": isisCircAuthTypeFails,
       "isisCircAuthFails": isisCircAuthFails,
       "isisCircLANDesISChanges": isisCircLANDesISChanges,
       "isisPacketCounterTable": isisPacketCounterTable,
       "isisPacketCounterEntry": isisPacketCounterEntry,
       "isisPacketCountLevel": isisPacketCountLevel,
       "isisPacketCountDirection": isisPacketCountDirection,
       "isisPacketCountIIHello": isisPacketCountIIHello,
       "isisPacketCountISHello": isisPacketCountISHello,
       "isisPacketCountESHello": isisPacketCountESHello,
       "isisPacketCountLSP": isisPacketCountLSP,
       "isisPacketCountCSNP": isisPacketCountCSNP,
       "isisPacketCountPSNP": isisPacketCountPSNP,
       "isisPacketCountUnknown": isisPacketCountUnknown,
       "isisISAdj": isisISAdj,
       "isisISAdjTable": isisISAdjTable,
       "isisISAdjEntry": isisISAdjEntry,
       "isisISAdjIndex": isisISAdjIndex,
       "isisISAdjState": isisISAdjState,
       "isisISAdj3WayState": isisISAdj3WayState,
       "isisISAdjNeighSNPAAddress": isisISAdjNeighSNPAAddress,
       "isisISAdjNeighSysType": isisISAdjNeighSysType,
       "isisISAdjNeighSysID": isisISAdjNeighSysID,
       "isisISAdjNbrExtendedCircID": isisISAdjNbrExtendedCircID,
       "isisISAdjUsage": isisISAdjUsage,
       "isisISAdjHoldTimer": isisISAdjHoldTimer,
       "isisISAdjNeighPriority": isisISAdjNeighPriority,
       "isisISAdjLastUpTime": isisISAdjLastUpTime,
       "isisISAdjAreaAddrTable": isisISAdjAreaAddrTable,
       "isisISAdjAreaAddrEntry": isisISAdjAreaAddrEntry,
       "isisISAdjAreaAddrIndex": isisISAdjAreaAddrIndex,
       "isisISAdjAreaAddress": isisISAdjAreaAddress,
       "isisISAdjIPAddrTable": isisISAdjIPAddrTable,
       "isisISAdjIPAddrEntry": isisISAdjIPAddrEntry,
       "isisISAdjIPAddrIndex": isisISAdjIPAddrIndex,
       "isisISAdjIPAddrType": isisISAdjIPAddrType,
       "isisISAdjIPAddrAddress": isisISAdjIPAddrAddress,
       "isisISAdjProtSuppTable": isisISAdjProtSuppTable,
       "isisISAdjProtSuppEntry": isisISAdjProtSuppEntry,
       "isisISAdjProtSuppProtocol": isisISAdjProtSuppProtocol,
       "isisReachAddr": isisReachAddr,
       "isisRATable": isisRATable,
       "isisRAEntry": isisRAEntry,
       "isisRAIndex": isisRAIndex,
       "isisRAExistState": isisRAExistState,
       "isisRAAdminState": isisRAAdminState,
       "isisRAAddrPrefix": isisRAAddrPrefix,
       "isisRAMapType": isisRAMapType,
       "isisRAMetric": isisRAMetric,
       "isisRAMetricType": isisRAMetricType,
       "isisRASNPAAddress": isisRASNPAAddress,
       "isisRASNPAMask": isisRASNPAMask,
       "isisRASNPAPrefix": isisRASNPAPrefix,
       "isisRAType": isisRAType,
       "isisIPReachAddr": isisIPReachAddr,
       "isisIPRATable": isisIPRATable,
       "isisIPRAEntry": isisIPRAEntry,
       "isisIPRADestType": isisIPRADestType,
       "isisIPRADest": isisIPRADest,
       "isisIPRADestPrefixLen": isisIPRADestPrefixLen,
       "isisIPRANextHopIndex": isisIPRANextHopIndex,
       "isisIPRANextHopType": isisIPRANextHopType,
       "isisIPRANextHop": isisIPRANextHop,
       "isisIPRAType": isisIPRAType,
       "isisIPRAExistState": isisIPRAExistState,
       "isisIPRAAdminState": isisIPRAAdminState,
       "isisIPRAMetric": isisIPRAMetric,
       "isisIPRAMetricType": isisIPRAMetricType,
       "isisIPRAFullMetric": isisIPRAFullMetric,
       "isisIPRASNPAAddress": isisIPRASNPAAddress,
       "isisIPRASourceType": isisIPRASourceType,
       "isisLSPDataBase": isisLSPDataBase,
       "isisLSPSummaryTable": isisLSPSummaryTable,
       "isisLSPSummaryEntry": isisLSPSummaryEntry,
       "isisLSPLevel": isisLSPLevel,
       "isisLSPID": isisLSPID,
       "isisLSPSeq": isisLSPSeq,
       "isisLSPZeroLife": isisLSPZeroLife,
       "isisLSPChecksum": isisLSPChecksum,
       "isisLSPLifetimeRemain": isisLSPLifetimeRemain,
       "isisLSPPDULength": isisLSPPDULength,
       "isisLSPAttributes": isisLSPAttributes,
       "isisLSPTLVTable": isisLSPTLVTable,
       "isisLSPTLVEntry": isisLSPTLVEntry,
       "isisLSPTLVIndex": isisLSPTLVIndex,
       "isisLSPTLVSeq": isisLSPTLVSeq,
       "isisLSPTLVChecksum": isisLSPTLVChecksum,
       "isisLSPTLVType": isisLSPTLVType,
       "isisLSPTLVLen": isisLSPTLVLen,
       "isisLSPTLVValue": isisLSPTLVValue,
       "isisNotification": isisNotification,
       "isisNotificationEntry": isisNotificationEntry,
       "isisNotificationSysLevelIndex": isisNotificationSysLevelIndex,
       "isisNotificationCircIfIndex": isisNotificationCircIfIndex,
       "isisPduLspId": isisPduLspId,
       "isisPduFragment": isisPduFragment,
       "isisPduFieldLen": isisPduFieldLen,
       "isisPduMaxAreaAddress": isisPduMaxAreaAddress,
       "isisPduProtocolVersion": isisPduProtocolVersion,
       "isisPduLspSize": isisPduLspSize,
       "isisPduOriginatingBufferSize": isisPduOriginatingBufferSize,
       "isisPduBufferSize": isisPduBufferSize,
       "isisPduProtocolsSupported": isisPduProtocolsSupported,
       "isisAdjState": isisAdjState,
       "isisErrorOffset": isisErrorOffset,
       "isisErrorTLVType": isisErrorTLVType,
       "isisNotificationAreaAddress": isisNotificationAreaAddress,
       "isisConformance": isisConformance,
       "isisCompliances": isisCompliances,
       "isisCompliance": isisCompliance,
       "isisAdvancedCompliance": isisAdvancedCompliance,
       "isisReadOnlyCompliance": isisReadOnlyCompliance,
       "isisGroups": isisGroups,
       "isisSystemGroup": isisSystemGroup,
       "isisCircuitGroup": isisCircuitGroup,
       "isisISAdjGroup": isisISAdjGroup,
       "isisNotificationObjectGroup": isisNotificationObjectGroup,
       "isisNotificationGroup": isisNotificationGroup,
       "isisISPDUCounterGroup": isisISPDUCounterGroup,
       "isisRATableGroup": isisRATableGroup,
       "isisISIPRADestGroup": isisISIPRADestGroup,
       "isisLSPGroup": isisLSPGroup}
)
