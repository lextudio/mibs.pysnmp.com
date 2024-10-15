# SNMP MIB module (CISCO-IETF-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-ISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:38 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(IndexIntegerNextFree,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
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

ciscoIetfIsisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118)
)
ciscoIetfIsisMIB.setRevisions(
        ("2005-08-16 12:00",
         "2005-02-08 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiiOSINSAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class CiiSystemID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class CiiLinkStatePDUID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )



class CiiAdminState(Integer32, TextualConvention):
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



class CiiLSPBuffSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16000),
    )



class CiiLevelState(Integer32, TextualConvention):
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



class CiiSupportedProtocol(Integer32, TextualConvention):
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



class CiiDefaultMetric(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class CiiWideMetric(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class CiiFullMetric(Unsigned32, TextualConvention):
    status = "current"


class CiiMetricType(Integer32, TextualConvention):
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



class CiiMetricStyle(Integer32, TextualConvention):
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



class CiiISLevel(Integer32, TextualConvention):
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
        *(("area", 1),
          ("domain", 2),
          ("none", 0))
    )



class CiiPDUHeader(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CiiCircuitID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
    )



class CiiISPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )



class CiiUnsigned16TC(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CiiUnsigned8TC(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIetfIsisMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIetfIsisMIBNotifs = _CiscoIetfIsisMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0)
)
_CiscoIetfIsisMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIetfIsisMIBObjects = _CiscoIetfIsisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1)
)
_CiiSystem_ObjectIdentity = ObjectIdentity
ciiSystem = _CiiSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1)
)
_CiiSysObject_ObjectIdentity = ObjectIdentity
ciiSysObject = _CiiSysObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1)
)


class _CiiSysVersion_Type(Integer32):
    """Custom type ciiSysVersion based on Integer32"""
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


_CiiSysVersion_Type.__name__ = "Integer32"
_CiiSysVersion_Object = MibScalar
ciiSysVersion = _CiiSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 1),
    _CiiSysVersion_Type()
)
ciiSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysVersion.setStatus("current")


class _CiiSysType_Type(Integer32):
    """Custom type ciiSysType based on Integer32"""
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
        *(("level1IS", 1),
          ("level1L2IS", 3),
          ("level2IS", 2))
    )


_CiiSysType_Type.__name__ = "Integer32"
_CiiSysType_Object = MibScalar
ciiSysType = _CiiSysType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 2),
    _CiiSysType_Type()
)
ciiSysType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysType.setStatus("current")
_CiiSysID_Type = CiiSystemID
_CiiSysID_Object = MibScalar
ciiSysID = _CiiSysID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 3),
    _CiiSysID_Type()
)
ciiSysID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysID.setStatus("current")


class _CiiSysMaxPathSplits_Type(Integer32):
    """Custom type ciiSysMaxPathSplits based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiiSysMaxPathSplits_Type.__name__ = "Integer32"
_CiiSysMaxPathSplits_Object = MibScalar
ciiSysMaxPathSplits = _CiiSysMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 4),
    _CiiSysMaxPathSplits_Type()
)
ciiSysMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysMaxPathSplits.setStatus("current")


class _CiiSysMaxLSPGenInt_Type(Integer32):
    """Custom type ciiSysMaxLSPGenInt based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65235),
    )


_CiiSysMaxLSPGenInt_Type.__name__ = "Integer32"
_CiiSysMaxLSPGenInt_Object = MibScalar
ciiSysMaxLSPGenInt = _CiiSysMaxLSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 5),
    _CiiSysMaxLSPGenInt_Type()
)
ciiSysMaxLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysMaxLSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysMaxLSPGenInt.setUnits("seconds")


class _CiiSysPollESHelloRate_Type(CiiUnsigned16TC):
    """Custom type ciiSysPollESHelloRate based on CiiUnsigned16TC"""
    defaultValue = 50

    subtypeSpec = CiiUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiiSysPollESHelloRate_Type.__name__ = "CiiUnsigned16TC"
_CiiSysPollESHelloRate_Object = MibScalar
ciiSysPollESHelloRate = _CiiSysPollESHelloRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 6),
    _CiiSysPollESHelloRate_Type()
)
ciiSysPollESHelloRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysPollESHelloRate.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysPollESHelloRate.setUnits("seconds")


class _CiiSysWaitTime_Type(CiiUnsigned16TC):
    """Custom type ciiSysWaitTime based on CiiUnsigned16TC"""
    defaultValue = 60

    subtypeSpec = CiiUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiiSysWaitTime_Type.__name__ = "CiiUnsigned16TC"
_CiiSysWaitTime_Object = MibScalar
ciiSysWaitTime = _CiiSysWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 7),
    _CiiSysWaitTime_Type()
)
ciiSysWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysWaitTime.setUnits("seconds")


class _CiiSysAdminState_Type(CiiAdminState):
    """Custom type ciiSysAdminState based on CiiAdminState"""


_CiiSysAdminState_Object = MibScalar
ciiSysAdminState = _CiiSysAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 8),
    _CiiSysAdminState_Type()
)
ciiSysAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysAdminState.setStatus("current")


class _CiiSysL2toL1Leaking_Type(TruthValue):
    """Custom type ciiSysL2toL1Leaking based on TruthValue"""


_CiiSysL2toL1Leaking_Object = MibScalar
ciiSysL2toL1Leaking = _CiiSysL2toL1Leaking_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 9),
    _CiiSysL2toL1Leaking_Type()
)
ciiSysL2toL1Leaking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysL2toL1Leaking.setStatus("current")


class _CiiSysMaxAge_Type(CiiUnsigned16TC):
    """Custom type ciiSysMaxAge based on CiiUnsigned16TC"""
    defaultValue = 1200

    subtypeSpec = CiiUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 65535),
    )


_CiiSysMaxAge_Type.__name__ = "CiiUnsigned16TC"
_CiiSysMaxAge_Object = MibScalar
ciiSysMaxAge = _CiiSysMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 10),
    _CiiSysMaxAge_Type()
)
ciiSysMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysMaxAge.setUnits("seconds")


class _CiiSysReceiveLSPBufferSize_Type(CiiUnsigned16TC):
    """Custom type ciiSysReceiveLSPBufferSize based on CiiUnsigned16TC"""
    defaultValue = 1492

    subtypeSpec = CiiUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1492, 16000),
    )


_CiiSysReceiveLSPBufferSize_Type.__name__ = "CiiUnsigned16TC"
_CiiSysReceiveLSPBufferSize_Object = MibScalar
ciiSysReceiveLSPBufferSize = _CiiSysReceiveLSPBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 1, 11),
    _CiiSysReceiveLSPBufferSize_Type()
)
ciiSysReceiveLSPBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysReceiveLSPBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysReceiveLSPBufferSize.setUnits("bytes")
_CiiManAreaAddrTable_Object = MibTable
ciiManAreaAddrTable = _CiiManAreaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciiManAreaAddrTable.setStatus("current")
_CiiManAreaAddrEntry_Object = MibTableRow
ciiManAreaAddrEntry = _CiiManAreaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 2, 1)
)
ciiManAreaAddrEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiManAreaAddr"),
)
if mibBuilder.loadTexts:
    ciiManAreaAddrEntry.setStatus("current")
_CiiManAreaAddr_Type = CiiOSINSAddress
_CiiManAreaAddr_Object = MibTableColumn
ciiManAreaAddr = _CiiManAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 2, 1, 1),
    _CiiManAreaAddr_Type()
)
ciiManAreaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiManAreaAddr.setStatus("current")
_CiiManAreaAddrExistState_Type = RowStatus
_CiiManAreaAddrExistState_Object = MibTableColumn
ciiManAreaAddrExistState = _CiiManAreaAddrExistState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 2, 1, 2),
    _CiiManAreaAddrExistState_Type()
)
ciiManAreaAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiManAreaAddrExistState.setStatus("current")
_CiiAreaAddrTable_Object = MibTable
ciiAreaAddrTable = _CiiAreaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ciiAreaAddrTable.setStatus("current")
_CiiAreaAddrEntry_Object = MibTableRow
ciiAreaAddrEntry = _CiiAreaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 3, 1)
)
ciiAreaAddrEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiAreaAddr"),
)
if mibBuilder.loadTexts:
    ciiAreaAddrEntry.setStatus("current")
_CiiAreaAddr_Type = CiiOSINSAddress
_CiiAreaAddr_Object = MibTableColumn
ciiAreaAddr = _CiiAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 3, 1, 1),
    _CiiAreaAddr_Type()
)
ciiAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiAreaAddr.setStatus("current")
_CiiSysProtSuppTable_Object = MibTable
ciiSysProtSuppTable = _CiiSysProtSuppTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ciiSysProtSuppTable.setStatus("current")
_CiiSysProtSuppEntry_Object = MibTableRow
ciiSysProtSuppEntry = _CiiSysProtSuppEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 4, 1)
)
ciiSysProtSuppEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiSysProtSuppProtocol"),
)
if mibBuilder.loadTexts:
    ciiSysProtSuppEntry.setStatus("current")
_CiiSysProtSuppProtocol_Type = CiiSupportedProtocol
_CiiSysProtSuppProtocol_Object = MibTableColumn
ciiSysProtSuppProtocol = _CiiSysProtSuppProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 4, 1, 1),
    _CiiSysProtSuppProtocol_Type()
)
ciiSysProtSuppProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiSysProtSuppProtocol.setStatus("current")
_CiiSysProtSuppExistState_Type = RowStatus
_CiiSysProtSuppExistState_Object = MibTableColumn
ciiSysProtSuppExistState = _CiiSysProtSuppExistState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 4, 1, 2),
    _CiiSysProtSuppExistState_Type()
)
ciiSysProtSuppExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiSysProtSuppExistState.setStatus("current")
_CiiSummAddrTable_Object = MibTable
ciiSummAddrTable = _CiiSummAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ciiSummAddrTable.setStatus("current")
_CiiSummAddrEntry_Object = MibTableRow
ciiSummAddrEntry = _CiiSummAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 5, 1)
)
ciiSummAddrEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiSummAddressType"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiSummAddress"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiSummAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    ciiSummAddrEntry.setStatus("current")
_CiiSummAddressType_Type = InetAddressType
_CiiSummAddressType_Object = MibTableColumn
ciiSummAddressType = _CiiSummAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 5, 1, 1),
    _CiiSummAddressType_Type()
)
ciiSummAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiSummAddressType.setStatus("current")


class _CiiSummAddress_Type(InetAddress):
    """Custom type ciiSummAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CiiSummAddress_Type.__name__ = "InetAddress"
_CiiSummAddress_Object = MibTableColumn
ciiSummAddress = _CiiSummAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 5, 1, 2),
    _CiiSummAddress_Type()
)
ciiSummAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiSummAddress.setStatus("current")


class _CiiSummAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type ciiSummAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CiiSummAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_CiiSummAddrPrefixLen_Object = MibTableColumn
ciiSummAddrPrefixLen = _CiiSummAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 5, 1, 3),
    _CiiSummAddrPrefixLen_Type()
)
ciiSummAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiSummAddrPrefixLen.setStatus("current")
_CiiSummAddrExistState_Type = RowStatus
_CiiSummAddrExistState_Object = MibTableColumn
ciiSummAddrExistState = _CiiSummAddrExistState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 5, 1, 4),
    _CiiSummAddrExistState_Type()
)
ciiSummAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiSummAddrExistState.setStatus("current")


class _CiiSummAddrMetric_Type(CiiDefaultMetric):
    """Custom type ciiSummAddrMetric based on CiiDefaultMetric"""
    defaultValue = 20


_CiiSummAddrMetric_Object = MibTableColumn
ciiSummAddrMetric = _CiiSummAddrMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 5, 1, 5),
    _CiiSummAddrMetric_Type()
)
ciiSummAddrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiSummAddrMetric.setStatus("current")


class _CiiSummAddrFullMetric_Type(CiiFullMetric):
    """Custom type ciiSummAddrFullMetric based on CiiFullMetric"""
    defaultValue = 20


_CiiSummAddrFullMetric_Object = MibTableColumn
ciiSummAddrFullMetric = _CiiSummAddrFullMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 5, 1, 6),
    _CiiSummAddrFullMetric_Type()
)
ciiSummAddrFullMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiSummAddrFullMetric.setStatus("current")
_CiiRedistributeAddrTable_Object = MibTable
ciiRedistributeAddrTable = _CiiRedistributeAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ciiRedistributeAddrTable.setStatus("current")
_CiiRedistributeAddrEntry_Object = MibTableRow
ciiRedistributeAddrEntry = _CiiRedistributeAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 6, 1)
)
ciiRedistributeAddrEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiRedistributeAddrType"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiRedistributeAddrAddress"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiRedistributeAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    ciiRedistributeAddrEntry.setStatus("current")
_CiiRedistributeAddrType_Type = InetAddressType
_CiiRedistributeAddrType_Object = MibTableColumn
ciiRedistributeAddrType = _CiiRedistributeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 6, 1, 1),
    _CiiRedistributeAddrType_Type()
)
ciiRedistributeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiRedistributeAddrType.setStatus("current")


class _CiiRedistributeAddrAddress_Type(InetAddress):
    """Custom type ciiRedistributeAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CiiRedistributeAddrAddress_Type.__name__ = "InetAddress"
_CiiRedistributeAddrAddress_Object = MibTableColumn
ciiRedistributeAddrAddress = _CiiRedistributeAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 6, 1, 2),
    _CiiRedistributeAddrAddress_Type()
)
ciiRedistributeAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiRedistributeAddrAddress.setStatus("current")


class _CiiRedistributeAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type ciiRedistributeAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CiiRedistributeAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_CiiRedistributeAddrPrefixLen_Object = MibTableColumn
ciiRedistributeAddrPrefixLen = _CiiRedistributeAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 6, 1, 3),
    _CiiRedistributeAddrPrefixLen_Type()
)
ciiRedistributeAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiRedistributeAddrPrefixLen.setStatus("current")
_CiiRedistributeAddrExistState_Type = RowStatus
_CiiRedistributeAddrExistState_Object = MibTableColumn
ciiRedistributeAddrExistState = _CiiRedistributeAddrExistState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 6, 1, 4),
    _CiiRedistributeAddrExistState_Type()
)
ciiRedistributeAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRedistributeAddrExistState.setStatus("current")
_CiiRouterTable_Object = MibTable
ciiRouterTable = _CiiRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ciiRouterTable.setStatus("current")
_CiiRouterEntry_Object = MibTableRow
ciiRouterEntry = _CiiRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 7, 1)
)
ciiRouterEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiRouterSysID"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiRouterLevel"),
)
if mibBuilder.loadTexts:
    ciiRouterEntry.setStatus("current")
_CiiRouterSysID_Type = CiiSystemID
_CiiRouterSysID_Object = MibTableColumn
ciiRouterSysID = _CiiRouterSysID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 7, 1, 1),
    _CiiRouterSysID_Type()
)
ciiRouterSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiRouterSysID.setStatus("current")
_CiiRouterLevel_Type = CiiISLevel
_CiiRouterLevel_Object = MibTableColumn
ciiRouterLevel = _CiiRouterLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 7, 1, 2),
    _CiiRouterLevel_Type()
)
ciiRouterLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiRouterLevel.setStatus("current")
_CiiRouterHostName_Type = SnmpAdminString
_CiiRouterHostName_Object = MibTableColumn
ciiRouterHostName = _CiiRouterHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 7, 1, 3),
    _CiiRouterHostName_Type()
)
ciiRouterHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiRouterHostName.setStatus("current")
_CiiRouterID_Type = Unsigned32
_CiiRouterID_Object = MibTableColumn
ciiRouterID = _CiiRouterID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 1, 7, 1, 4),
    _CiiRouterID_Type()
)
ciiRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiRouterID.setStatus("current")
_CiiSysLevel_ObjectIdentity = ObjectIdentity
ciiSysLevel = _CiiSysLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2)
)
_CiiSysLevelTable_Object = MibTable
ciiSysLevelTable = _CiiSysLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciiSysLevelTable.setStatus("current")
_CiiSysLevelEntry_Object = MibTableRow
ciiSysLevelEntry = _CiiSysLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1, 1)
)
ciiSysLevelEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiSysLevelIndex"),
)
if mibBuilder.loadTexts:
    ciiSysLevelEntry.setStatus("current")


class _CiiSysLevelIndex_Type(Integer32):
    """Custom type ciiSysLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_CiiSysLevelIndex_Type.__name__ = "Integer32"
_CiiSysLevelIndex_Object = MibTableColumn
ciiSysLevelIndex = _CiiSysLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1, 1, 1),
    _CiiSysLevelIndex_Type()
)
ciiSysLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiSysLevelIndex.setStatus("current")


class _CiiSysLevelOrigLSPBuffSize_Type(CiiLSPBuffSize):
    """Custom type ciiSysLevelOrigLSPBuffSize based on CiiLSPBuffSize"""
    defaultValue = 1492


_CiiSysLevelOrigLSPBuffSize_Object = MibTableColumn
ciiSysLevelOrigLSPBuffSize = _CiiSysLevelOrigLSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1, 1, 2),
    _CiiSysLevelOrigLSPBuffSize_Type()
)
ciiSysLevelOrigLSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysLevelOrigLSPBuffSize.setStatus("current")


class _CiiSysLevelMinLSPGenInt_Type(CiiUnsigned16TC):
    """Custom type ciiSysLevelMinLSPGenInt based on CiiUnsigned16TC"""
    defaultValue = 30

    subtypeSpec = CiiUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiiSysLevelMinLSPGenInt_Type.__name__ = "CiiUnsigned16TC"
_CiiSysLevelMinLSPGenInt_Object = MibTableColumn
ciiSysLevelMinLSPGenInt = _CiiSysLevelMinLSPGenInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1, 1, 3),
    _CiiSysLevelMinLSPGenInt_Type()
)
ciiSysLevelMinLSPGenInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysLevelMinLSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysLevelMinLSPGenInt.setUnits("seconds")
_CiiSysLevelOverloadState_Type = CiiLevelState
_CiiSysLevelOverloadState_Object = MibTableColumn
ciiSysLevelOverloadState = _CiiSysLevelOverloadState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1, 1, 4),
    _CiiSysLevelOverloadState_Type()
)
ciiSysLevelOverloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysLevelOverloadState.setStatus("current")


class _CiiSysLevelSetOverload_Type(TruthValue):
    """Custom type ciiSysLevelSetOverload based on TruthValue"""


_CiiSysLevelSetOverload_Object = MibTableColumn
ciiSysLevelSetOverload = _CiiSysLevelSetOverload_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1, 1, 5),
    _CiiSysLevelSetOverload_Type()
)
ciiSysLevelSetOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysLevelSetOverload.setStatus("current")


class _CiiSysLevelSetOverloadUntil_Type(TimeTicks):
    """Custom type ciiSysLevelSetOverloadUntil based on TimeTicks"""
    defaultValue = 0


_CiiSysLevelSetOverloadUntil_Object = MibTableColumn
ciiSysLevelSetOverloadUntil = _CiiSysLevelSetOverloadUntil_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1, 1, 6),
    _CiiSysLevelSetOverloadUntil_Type()
)
ciiSysLevelSetOverloadUntil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysLevelSetOverloadUntil.setStatus("current")


class _CiiSysLevelMetricStyle_Type(CiiMetricStyle):
    """Custom type ciiSysLevelMetricStyle based on CiiMetricStyle"""


_CiiSysLevelMetricStyle_Object = MibTableColumn
ciiSysLevelMetricStyle = _CiiSysLevelMetricStyle_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1, 1, 7),
    _CiiSysLevelMetricStyle_Type()
)
ciiSysLevelMetricStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysLevelMetricStyle.setStatus("current")


class _CiiSysLevelSPFConsiders_Type(CiiMetricStyle):
    """Custom type ciiSysLevelSPFConsiders based on CiiMetricStyle"""


_CiiSysLevelSPFConsiders_Object = MibTableColumn
ciiSysLevelSPFConsiders = _CiiSysLevelSPFConsiders_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1, 1, 8),
    _CiiSysLevelSPFConsiders_Type()
)
ciiSysLevelSPFConsiders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysLevelSPFConsiders.setStatus("current")


class _CiiSysLevelTEEnabled_Type(TruthValue):
    """Custom type ciiSysLevelTEEnabled based on TruthValue"""


_CiiSysLevelTEEnabled_Object = MibTableColumn
ciiSysLevelTEEnabled = _CiiSysLevelTEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 2, 1, 1, 9),
    _CiiSysLevelTEEnabled_Type()
)
ciiSysLevelTEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiSysLevelTEEnabled.setStatus("current")
_CiiCirc_ObjectIdentity = ObjectIdentity
ciiCirc = _CiiCirc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3)
)
_CiiNextCircIndex_Type = IndexIntegerNextFree
_CiiNextCircIndex_Object = MibScalar
ciiNextCircIndex = _CiiNextCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 1),
    _CiiNextCircIndex_Type()
)
ciiNextCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiNextCircIndex.setStatus("current")
_CiiCircTable_Object = MibTable
ciiCircTable = _CiiCircTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ciiCircTable.setStatus("current")
_CiiCircEntry_Object = MibTableRow
ciiCircEntry = _CiiCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1)
)
ciiCircEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircIndex"),
)
if mibBuilder.loadTexts:
    ciiCircEntry.setStatus("current")


class _CiiCircIndex_Type(Integer32):
    """Custom type ciiCircIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiiCircIndex_Type.__name__ = "Integer32"
_CiiCircIndex_Object = MibTableColumn
ciiCircIndex = _CiiCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 1),
    _CiiCircIndex_Type()
)
ciiCircIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiCircIndex.setStatus("current")
_CiiCircIfIndex_Type = InterfaceIndex
_CiiCircIfIndex_Object = MibTableColumn
ciiCircIfIndex = _CiiCircIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 2),
    _CiiCircIfIndex_Type()
)
ciiCircIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircIfIndex.setStatus("current")
_CiiCircIfSubIndex_Type = Integer32
_CiiCircIfSubIndex_Object = MibTableColumn
ciiCircIfSubIndex = _CiiCircIfSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 3),
    _CiiCircIfSubIndex_Type()
)
ciiCircIfSubIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircIfSubIndex.setStatus("current")


class _CiiCircAdminState_Type(CiiAdminState):
    """Custom type ciiCircAdminState based on CiiAdminState"""


_CiiCircAdminState_Object = MibTableColumn
ciiCircAdminState = _CiiCircAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 4),
    _CiiCircAdminState_Type()
)
ciiCircAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircAdminState.setStatus("current")
_CiiCircExistState_Type = RowStatus
_CiiCircExistState_Object = MibTableColumn
ciiCircExistState = _CiiCircExistState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 5),
    _CiiCircExistState_Type()
)
ciiCircExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircExistState.setStatus("current")


class _CiiCircType_Type(Integer32):
    """Custom type ciiCircType based on Integer32"""
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


_CiiCircType_Type.__name__ = "Integer32"
_CiiCircType_Object = MibTableColumn
ciiCircType = _CiiCircType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 6),
    _CiiCircType_Type()
)
ciiCircType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircType.setStatus("current")


class _CiiCircExtDomain_Type(TruthValue):
    """Custom type ciiCircExtDomain based on TruthValue"""


_CiiCircExtDomain_Object = MibTableColumn
ciiCircExtDomain = _CiiCircExtDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 7),
    _CiiCircExtDomain_Type()
)
ciiCircExtDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircExtDomain.setStatus("current")


class _CiiCircLevel_Type(Integer32):
    """Custom type ciiCircLevel based on Integer32"""
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
        *(("level1", 1),
          ("level1L2", 3),
          ("level2", 2))
    )


_CiiCircLevel_Type.__name__ = "Integer32"
_CiiCircLevel_Object = MibTableColumn
ciiCircLevel = _CiiCircLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 8),
    _CiiCircLevel_Type()
)
ciiCircLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircLevel.setStatus("current")


class _CiiCircPassiveCircuit_Type(TruthValue):
    """Custom type ciiCircPassiveCircuit based on TruthValue"""


_CiiCircPassiveCircuit_Object = MibTableColumn
ciiCircPassiveCircuit = _CiiCircPassiveCircuit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 9),
    _CiiCircPassiveCircuit_Type()
)
ciiCircPassiveCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircPassiveCircuit.setStatus("current")


class _CiiCircMeshGroupEnabled_Type(Integer32):
    """Custom type ciiCircMeshGroupEnabled based on Integer32"""
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


_CiiCircMeshGroupEnabled_Type.__name__ = "Integer32"
_CiiCircMeshGroupEnabled_Object = MibTableColumn
ciiCircMeshGroupEnabled = _CiiCircMeshGroupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 10),
    _CiiCircMeshGroupEnabled_Type()
)
ciiCircMeshGroupEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircMeshGroupEnabled.setStatus("current")
_CiiCircMeshGroup_Type = Unsigned32
_CiiCircMeshGroup_Object = MibTableColumn
ciiCircMeshGroup = _CiiCircMeshGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 11),
    _CiiCircMeshGroup_Type()
)
ciiCircMeshGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircMeshGroup.setStatus("current")


class _CiiCircSmallHellos_Type(TruthValue):
    """Custom type ciiCircSmallHellos based on TruthValue"""


_CiiCircSmallHellos_Object = MibTableColumn
ciiCircSmallHellos = _CiiCircSmallHellos_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 12),
    _CiiCircSmallHellos_Type()
)
ciiCircSmallHellos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircSmallHellos.setStatus("current")
_CiiCircLastUpTime_Type = TimeTicks
_CiiCircLastUpTime_Object = MibTableColumn
ciiCircLastUpTime = _CiiCircLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 13),
    _CiiCircLastUpTime_Type()
)
ciiCircLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircLastUpTime.setStatus("current")


class _CiiCirc3WayEnabled_Type(TruthValue):
    """Custom type ciiCirc3WayEnabled based on TruthValue"""


_CiiCirc3WayEnabled_Object = MibTableColumn
ciiCirc3WayEnabled = _CiiCirc3WayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 14),
    _CiiCirc3WayEnabled_Type()
)
ciiCirc3WayEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCirc3WayEnabled.setStatus("current")
_CiiCircExtendedCircID_Type = Unsigned32
_CiiCircExtendedCircID_Object = MibTableColumn
ciiCircExtendedCircID = _CiiCircExtendedCircID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 3, 2, 1, 15),
    _CiiCircExtendedCircID_Type()
)
ciiCircExtendedCircID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiCircExtendedCircID.setStatus("current")
_CiiCircLevelValues_ObjectIdentity = ObjectIdentity
ciiCircLevelValues = _CiiCircLevelValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4)
)
_CiiCircLevelTable_Object = MibTable
ciiCircLevelTable = _CiiCircLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ciiCircLevelTable.setStatus("current")
_CiiCircLevelEntry_Object = MibTableRow
ciiCircLevelEntry = _CiiCircLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1)
)
ciiCircLevelEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircLevelIndex"),
)
if mibBuilder.loadTexts:
    ciiCircLevelEntry.setStatus("current")


class _CiiCircLevelIndex_Type(Integer32):
    """Custom type ciiCircLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_CiiCircLevelIndex_Type.__name__ = "Integer32"
_CiiCircLevelIndex_Object = MibTableColumn
ciiCircLevelIndex = _CiiCircLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 1),
    _CiiCircLevelIndex_Type()
)
ciiCircLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiCircLevelIndex.setStatus("current")


class _CiiCircLevelMetric_Type(CiiDefaultMetric):
    """Custom type ciiCircLevelMetric based on CiiDefaultMetric"""
    defaultValue = 10


_CiiCircLevelMetric_Object = MibTableColumn
ciiCircLevelMetric = _CiiCircLevelMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 2),
    _CiiCircLevelMetric_Type()
)
ciiCircLevelMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelMetric.setStatus("current")


class _CiiCircLevelWideMetric_Type(CiiWideMetric):
    """Custom type ciiCircLevelWideMetric based on CiiWideMetric"""
    defaultValue = 10


_CiiCircLevelWideMetric_Object = MibTableColumn
ciiCircLevelWideMetric = _CiiCircLevelWideMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 3),
    _CiiCircLevelWideMetric_Type()
)
ciiCircLevelWideMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelWideMetric.setStatus("current")


class _CiiCircLevelISPriority_Type(CiiISPriority):
    """Custom type ciiCircLevelISPriority based on CiiISPriority"""
    defaultValue = 64


_CiiCircLevelISPriority_Object = MibTableColumn
ciiCircLevelISPriority = _CiiCircLevelISPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 4),
    _CiiCircLevelISPriority_Type()
)
ciiCircLevelISPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelISPriority.setStatus("current")


class _CiiCircLevelIDOctet_Type(Integer32):
    """Custom type ciiCircLevelIDOctet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiiCircLevelIDOctet_Type.__name__ = "Integer32"
_CiiCircLevelIDOctet_Object = MibTableColumn
ciiCircLevelIDOctet = _CiiCircLevelIDOctet_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 5),
    _CiiCircLevelIDOctet_Type()
)
ciiCircLevelIDOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelIDOctet.setStatus("current")
_CiiCircLevelID_Type = CiiCircuitID
_CiiCircLevelID_Object = MibTableColumn
ciiCircLevelID = _CiiCircLevelID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 6),
    _CiiCircLevelID_Type()
)
ciiCircLevelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircLevelID.setStatus("current")
_CiiCircLevelDesIS_Type = CiiCircuitID
_CiiCircLevelDesIS_Object = MibTableColumn
ciiCircLevelDesIS = _CiiCircLevelDesIS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 7),
    _CiiCircLevelDesIS_Type()
)
ciiCircLevelDesIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircLevelDesIS.setStatus("current")


class _CiiCircLevelHelloMultiplier_Type(Integer32):
    """Custom type ciiCircLevelHelloMultiplier based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_CiiCircLevelHelloMultiplier_Type.__name__ = "Integer32"
_CiiCircLevelHelloMultiplier_Object = MibTableColumn
ciiCircLevelHelloMultiplier = _CiiCircLevelHelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 8),
    _CiiCircLevelHelloMultiplier_Type()
)
ciiCircLevelHelloMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelHelloMultiplier.setStatus("current")


class _CiiCircLevelHelloTimer_Type(Integer32):
    """Custom type ciiCircLevelHelloTimer based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600000),
    )


_CiiCircLevelHelloTimer_Type.__name__ = "Integer32"
_CiiCircLevelHelloTimer_Object = MibTableColumn
ciiCircLevelHelloTimer = _CiiCircLevelHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 9),
    _CiiCircLevelHelloTimer_Type()
)
ciiCircLevelHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelHelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    ciiCircLevelHelloTimer.setUnits("milliseconds")


class _CiiCircLevelDRHelloTimer_Type(Integer32):
    """Custom type ciiCircLevelDRHelloTimer based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120000),
    )


_CiiCircLevelDRHelloTimer_Type.__name__ = "Integer32"
_CiiCircLevelDRHelloTimer_Object = MibTableColumn
ciiCircLevelDRHelloTimer = _CiiCircLevelDRHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 10),
    _CiiCircLevelDRHelloTimer_Type()
)
ciiCircLevelDRHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelDRHelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    ciiCircLevelDRHelloTimer.setUnits("milliseconds")


class _CiiCircLevelLSPThrottle_Type(CiiUnsigned16TC):
    """Custom type ciiCircLevelLSPThrottle based on CiiUnsigned16TC"""
    defaultValue = 30

    subtypeSpec = CiiUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiiCircLevelLSPThrottle_Type.__name__ = "CiiUnsigned16TC"
_CiiCircLevelLSPThrottle_Object = MibTableColumn
ciiCircLevelLSPThrottle = _CiiCircLevelLSPThrottle_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 11),
    _CiiCircLevelLSPThrottle_Type()
)
ciiCircLevelLSPThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelLSPThrottle.setStatus("current")
if mibBuilder.loadTexts:
    ciiCircLevelLSPThrottle.setUnits("milliseconds")


class _CiiCircLevelMinLSPRetransInt_Type(Integer32):
    """Custom type ciiCircLevelMinLSPRetransInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CiiCircLevelMinLSPRetransInt_Type.__name__ = "Integer32"
_CiiCircLevelMinLSPRetransInt_Object = MibTableColumn
ciiCircLevelMinLSPRetransInt = _CiiCircLevelMinLSPRetransInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 12),
    _CiiCircLevelMinLSPRetransInt_Type()
)
ciiCircLevelMinLSPRetransInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelMinLSPRetransInt.setStatus("current")
if mibBuilder.loadTexts:
    ciiCircLevelMinLSPRetransInt.setUnits("seconds")


class _CiiCircLevelCSNPInterval_Type(Integer32):
    """Custom type ciiCircLevelCSNPInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CiiCircLevelCSNPInterval_Type.__name__ = "Integer32"
_CiiCircLevelCSNPInterval_Object = MibTableColumn
ciiCircLevelCSNPInterval = _CiiCircLevelCSNPInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 13),
    _CiiCircLevelCSNPInterval_Type()
)
ciiCircLevelCSNPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelCSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciiCircLevelCSNPInterval.setUnits("seconds")


class _CiiCircLevelPartSNPInterval_Type(Integer32):
    """Custom type ciiCircLevelPartSNPInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CiiCircLevelPartSNPInterval_Type.__name__ = "Integer32"
_CiiCircLevelPartSNPInterval_Object = MibTableColumn
ciiCircLevelPartSNPInterval = _CiiCircLevelPartSNPInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 4, 1, 1, 14),
    _CiiCircLevelPartSNPInterval_Type()
)
ciiCircLevelPartSNPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciiCircLevelPartSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciiCircLevelPartSNPInterval.setUnits("seconds")
_CiiCounters_ObjectIdentity = ObjectIdentity
ciiCounters = _CiiCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5)
)
_CiiSystemCounterTable_Object = MibTable
ciiSystemCounterTable = _CiiSystemCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ciiSystemCounterTable.setStatus("current")
_CiiSystemCounterEntry_Object = MibTableRow
ciiSystemCounterEntry = _CiiSystemCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1)
)
ciiSystemCounterEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiSysStatLevel"),
)
if mibBuilder.loadTexts:
    ciiSystemCounterEntry.setStatus("current")


class _CiiSysStatLevel_Type(Integer32):
    """Custom type ciiSysStatLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_CiiSysStatLevel_Type.__name__ = "Integer32"
_CiiSysStatLevel_Object = MibTableColumn
ciiSysStatLevel = _CiiSysStatLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 1),
    _CiiSysStatLevel_Type()
)
ciiSysStatLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiSysStatLevel.setStatus("current")
_CiiSysStatCorrLSPs_Type = Counter32
_CiiSysStatCorrLSPs_Object = MibTableColumn
ciiSysStatCorrLSPs = _CiiSysStatCorrLSPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 2),
    _CiiSysStatCorrLSPs_Type()
)
ciiSysStatCorrLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatCorrLSPs.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysStatCorrLSPs.setUnits("frames")
_CiiSysStatAuthTypeFails_Type = Counter32
_CiiSysStatAuthTypeFails_Object = MibTableColumn
ciiSysStatAuthTypeFails = _CiiSysStatAuthTypeFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 3),
    _CiiSysStatAuthTypeFails_Type()
)
ciiSysStatAuthTypeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatAuthTypeFails.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysStatAuthTypeFails.setUnits("frames")
_CiiSysStatAuthFails_Type = Counter32
_CiiSysStatAuthFails_Object = MibTableColumn
ciiSysStatAuthFails = _CiiSysStatAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 4),
    _CiiSysStatAuthFails_Type()
)
ciiSysStatAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysStatAuthFails.setUnits("frames")
_CiiSysStatLSPDbaseOloads_Type = Counter32
_CiiSysStatLSPDbaseOloads_Object = MibTableColumn
ciiSysStatLSPDbaseOloads = _CiiSysStatLSPDbaseOloads_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 5),
    _CiiSysStatLSPDbaseOloads_Type()
)
ciiSysStatLSPDbaseOloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatLSPDbaseOloads.setStatus("current")
_CiiSysStatManAddrDropFromAreas_Type = Counter32
_CiiSysStatManAddrDropFromAreas_Object = MibTableColumn
ciiSysStatManAddrDropFromAreas = _CiiSysStatManAddrDropFromAreas_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 6),
    _CiiSysStatManAddrDropFromAreas_Type()
)
ciiSysStatManAddrDropFromAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatManAddrDropFromAreas.setStatus("current")
_CiiSysStatAttmptToExMaxSeqNums_Type = Counter32
_CiiSysStatAttmptToExMaxSeqNums_Object = MibTableColumn
ciiSysStatAttmptToExMaxSeqNums = _CiiSysStatAttmptToExMaxSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 7),
    _CiiSysStatAttmptToExMaxSeqNums_Type()
)
ciiSysStatAttmptToExMaxSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatAttmptToExMaxSeqNums.setStatus("current")
_CiiSysStatSeqNumSkips_Type = Counter32
_CiiSysStatSeqNumSkips_Object = MibTableColumn
ciiSysStatSeqNumSkips = _CiiSysStatSeqNumSkips_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 8),
    _CiiSysStatSeqNumSkips_Type()
)
ciiSysStatSeqNumSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatSeqNumSkips.setStatus("current")
_CiiSysStatOwnLSPPurges_Type = Counter32
_CiiSysStatOwnLSPPurges_Object = MibTableColumn
ciiSysStatOwnLSPPurges = _CiiSysStatOwnLSPPurges_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 9),
    _CiiSysStatOwnLSPPurges_Type()
)
ciiSysStatOwnLSPPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatOwnLSPPurges.setStatus("current")
_CiiSysStatIDFieldLenMismatches_Type = Counter32
_CiiSysStatIDFieldLenMismatches_Object = MibTableColumn
ciiSysStatIDFieldLenMismatches = _CiiSysStatIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 10),
    _CiiSysStatIDFieldLenMismatches_Type()
)
ciiSysStatIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatIDFieldLenMismatches.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysStatIDFieldLenMismatches.setUnits("frames")
_CiiSysStatPartChanges_Type = Counter32
_CiiSysStatPartChanges_Object = MibTableColumn
ciiSysStatPartChanges = _CiiSysStatPartChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 11),
    _CiiSysStatPartChanges_Type()
)
ciiSysStatPartChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatPartChanges.setStatus("current")
_CiiSysStatSPFRuns_Type = Counter32
_CiiSysStatSPFRuns_Object = MibTableColumn
ciiSysStatSPFRuns = _CiiSysStatSPFRuns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 12),
    _CiiSysStatSPFRuns_Type()
)
ciiSysStatSPFRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatSPFRuns.setStatus("current")
_CiiSysStatLSPErrors_Type = Counter32
_CiiSysStatLSPErrors_Object = MibTableColumn
ciiSysStatLSPErrors = _CiiSysStatLSPErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 1, 1, 13),
    _CiiSysStatLSPErrors_Type()
)
ciiSysStatLSPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiSysStatLSPErrors.setStatus("current")
if mibBuilder.loadTexts:
    ciiSysStatLSPErrors.setUnits("frames")
_CiiCircuitCounterTable_Object = MibTable
ciiCircuitCounterTable = _CiiCircuitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ciiCircuitCounterTable.setStatus("current")
_CiiCircuitCounterEntry_Object = MibTableRow
ciiCircuitCounterEntry = _CiiCircuitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1)
)
ciiCircuitCounterEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircuitType"),
)
if mibBuilder.loadTexts:
    ciiCircuitCounterEntry.setStatus("current")


class _CiiCircuitType_Type(Integer32):
    """Custom type ciiCircuitType based on Integer32"""
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


_CiiCircuitType_Type.__name__ = "Integer32"
_CiiCircuitType_Object = MibTableColumn
ciiCircuitType = _CiiCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1, 1),
    _CiiCircuitType_Type()
)
ciiCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiCircuitType.setStatus("current")
_CiiCircAdjChanges_Type = Counter32
_CiiCircAdjChanges_Object = MibTableColumn
ciiCircAdjChanges = _CiiCircAdjChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1, 2),
    _CiiCircAdjChanges_Type()
)
ciiCircAdjChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircAdjChanges.setStatus("current")
_CiiCircNumAdj_Type = Unsigned32
_CiiCircNumAdj_Object = MibTableColumn
ciiCircNumAdj = _CiiCircNumAdj_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1, 3),
    _CiiCircNumAdj_Type()
)
ciiCircNumAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircNumAdj.setStatus("current")
_CiiCircInitFails_Type = Counter32
_CiiCircInitFails_Object = MibTableColumn
ciiCircInitFails = _CiiCircInitFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1, 4),
    _CiiCircInitFails_Type()
)
ciiCircInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircInitFails.setStatus("current")
_CiiCircRejAdjs_Type = Counter32
_CiiCircRejAdjs_Object = MibTableColumn
ciiCircRejAdjs = _CiiCircRejAdjs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1, 5),
    _CiiCircRejAdjs_Type()
)
ciiCircRejAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircRejAdjs.setStatus("current")
_CiiCircIDFieldLenMismatches_Type = Counter32
_CiiCircIDFieldLenMismatches_Object = MibTableColumn
ciiCircIDFieldLenMismatches = _CiiCircIDFieldLenMismatches_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1, 6),
    _CiiCircIDFieldLenMismatches_Type()
)
ciiCircIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircIDFieldLenMismatches.setStatus("current")
if mibBuilder.loadTexts:
    ciiCircIDFieldLenMismatches.setUnits("frames")
_CiiCircMaxAreaAddrMismatches_Type = Counter32
_CiiCircMaxAreaAddrMismatches_Object = MibTableColumn
ciiCircMaxAreaAddrMismatches = _CiiCircMaxAreaAddrMismatches_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1, 7),
    _CiiCircMaxAreaAddrMismatches_Type()
)
ciiCircMaxAreaAddrMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircMaxAreaAddrMismatches.setStatus("current")
_CiiCircAuthTypeFails_Type = Counter32
_CiiCircAuthTypeFails_Object = MibTableColumn
ciiCircAuthTypeFails = _CiiCircAuthTypeFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1, 8),
    _CiiCircAuthTypeFails_Type()
)
ciiCircAuthTypeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircAuthTypeFails.setStatus("current")
_CiiCircAuthFails_Type = Counter32
_CiiCircAuthFails_Object = MibTableColumn
ciiCircAuthFails = _CiiCircAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1, 9),
    _CiiCircAuthFails_Type()
)
ciiCircAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircAuthFails.setStatus("current")
_CiiCircLANDesISChanges_Type = Counter32
_CiiCircLANDesISChanges_Object = MibTableColumn
ciiCircLANDesISChanges = _CiiCircLANDesISChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 2, 1, 10),
    _CiiCircLANDesISChanges_Type()
)
ciiCircLANDesISChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiCircLANDesISChanges.setStatus("current")
_CiiPacketCounterTable_Object = MibTable
ciiPacketCounterTable = _CiiPacketCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ciiPacketCounterTable.setStatus("current")
_CiiPacketCounterEntry_Object = MibTableRow
ciiPacketCounterEntry = _CiiPacketCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3, 1)
)
ciiPacketCounterEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiPacketCountLevel"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiPacketCountDirection"),
)
if mibBuilder.loadTexts:
    ciiPacketCounterEntry.setStatus("current")


class _CiiPacketCountLevel_Type(Integer32):
    """Custom type ciiPacketCountLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_CiiPacketCountLevel_Type.__name__ = "Integer32"
_CiiPacketCountLevel_Object = MibTableColumn
ciiPacketCountLevel = _CiiPacketCountLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3, 1, 1),
    _CiiPacketCountLevel_Type()
)
ciiPacketCountLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiPacketCountLevel.setStatus("current")


class _CiiPacketCountDirection_Type(Integer32):
    """Custom type ciiPacketCountDirection based on Integer32"""
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


_CiiPacketCountDirection_Type.__name__ = "Integer32"
_CiiPacketCountDirection_Object = MibTableColumn
ciiPacketCountDirection = _CiiPacketCountDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3, 1, 2),
    _CiiPacketCountDirection_Type()
)
ciiPacketCountDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiPacketCountDirection.setStatus("current")
_CiiPacketCountIIHellos_Type = Counter32
_CiiPacketCountIIHellos_Object = MibTableColumn
ciiPacketCountIIHellos = _CiiPacketCountIIHellos_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3, 1, 3),
    _CiiPacketCountIIHellos_Type()
)
ciiPacketCountIIHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiPacketCountIIHellos.setStatus("current")
if mibBuilder.loadTexts:
    ciiPacketCountIIHellos.setUnits("frames")
_CiiPacketCountISHellos_Type = Counter32
_CiiPacketCountISHellos_Object = MibTableColumn
ciiPacketCountISHellos = _CiiPacketCountISHellos_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3, 1, 4),
    _CiiPacketCountISHellos_Type()
)
ciiPacketCountISHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiPacketCountISHellos.setStatus("current")
if mibBuilder.loadTexts:
    ciiPacketCountISHellos.setUnits("frames")
_CiiPacketCountESHellos_Type = Counter32
_CiiPacketCountESHellos_Object = MibTableColumn
ciiPacketCountESHellos = _CiiPacketCountESHellos_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3, 1, 5),
    _CiiPacketCountESHellos_Type()
)
ciiPacketCountESHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiPacketCountESHellos.setStatus("current")
if mibBuilder.loadTexts:
    ciiPacketCountESHellos.setUnits("frames")
_CiiPacketCountLSPs_Type = Counter32
_CiiPacketCountLSPs_Object = MibTableColumn
ciiPacketCountLSPs = _CiiPacketCountLSPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3, 1, 6),
    _CiiPacketCountLSPs_Type()
)
ciiPacketCountLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiPacketCountLSPs.setStatus("current")
if mibBuilder.loadTexts:
    ciiPacketCountLSPs.setUnits("frames")
_CiiPacketCountCSNPs_Type = Counter32
_CiiPacketCountCSNPs_Object = MibTableColumn
ciiPacketCountCSNPs = _CiiPacketCountCSNPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3, 1, 7),
    _CiiPacketCountCSNPs_Type()
)
ciiPacketCountCSNPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiPacketCountCSNPs.setStatus("current")
if mibBuilder.loadTexts:
    ciiPacketCountCSNPs.setUnits("frames")
_CiiPacketCountPSNPs_Type = Counter32
_CiiPacketCountPSNPs_Object = MibTableColumn
ciiPacketCountPSNPs = _CiiPacketCountPSNPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3, 1, 8),
    _CiiPacketCountPSNPs_Type()
)
ciiPacketCountPSNPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiPacketCountPSNPs.setStatus("current")
if mibBuilder.loadTexts:
    ciiPacketCountPSNPs.setUnits("frames")
_CiiPacketCountUnknowns_Type = Counter32
_CiiPacketCountUnknowns_Object = MibTableColumn
ciiPacketCountUnknowns = _CiiPacketCountUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 5, 3, 1, 9),
    _CiiPacketCountUnknowns_Type()
)
ciiPacketCountUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiPacketCountUnknowns.setStatus("current")
if mibBuilder.loadTexts:
    ciiPacketCountUnknowns.setUnits("frames")
_CiiISAdj_ObjectIdentity = ObjectIdentity
ciiISAdj = _CiiISAdj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6)
)
_CiiISAdjTable_Object = MibTable
ciiISAdjTable = _CiiISAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ciiISAdjTable.setStatus("current")
_CiiISAdjEntry_Object = MibTableRow
ciiISAdjEntry = _CiiISAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1)
)
ciiISAdjEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiISAdjIndex"),
)
if mibBuilder.loadTexts:
    ciiISAdjEntry.setStatus("current")


class _CiiISAdjIndex_Type(Integer32):
    """Custom type ciiISAdjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_CiiISAdjIndex_Type.__name__ = "Integer32"
_CiiISAdjIndex_Object = MibTableColumn
ciiISAdjIndex = _CiiISAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 1),
    _CiiISAdjIndex_Type()
)
ciiISAdjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiISAdjIndex.setStatus("current")


class _CiiISAdjState_Type(Integer32):
    """Custom type ciiISAdjState based on Integer32"""
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


_CiiISAdjState_Type.__name__ = "Integer32"
_CiiISAdjState_Object = MibTableColumn
ciiISAdjState = _CiiISAdjState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 2),
    _CiiISAdjState_Type()
)
ciiISAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjState.setStatus("current")


class _CiiISAdj3WayState_Type(Integer32):
    """Custom type ciiISAdj3WayState based on Integer32"""
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


_CiiISAdj3WayState_Type.__name__ = "Integer32"
_CiiISAdj3WayState_Object = MibTableColumn
ciiISAdj3WayState = _CiiISAdj3WayState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 3),
    _CiiISAdj3WayState_Type()
)
ciiISAdj3WayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdj3WayState.setStatus("current")
_CiiISAdjNeighSNPAAddress_Type = CiiOSINSAddress
_CiiISAdjNeighSNPAAddress_Object = MibTableColumn
ciiISAdjNeighSNPAAddress = _CiiISAdjNeighSNPAAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 4),
    _CiiISAdjNeighSNPAAddress_Type()
)
ciiISAdjNeighSNPAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjNeighSNPAAddress.setStatus("current")


class _CiiISAdjNeighSysType_Type(Integer32):
    """Custom type ciiISAdjNeighSysType based on Integer32"""
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


_CiiISAdjNeighSysType_Type.__name__ = "Integer32"
_CiiISAdjNeighSysType_Object = MibTableColumn
ciiISAdjNeighSysType = _CiiISAdjNeighSysType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 5),
    _CiiISAdjNeighSysType_Type()
)
ciiISAdjNeighSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjNeighSysType.setStatus("current")
_CiiISAdjNeighSysID_Type = CiiSystemID
_CiiISAdjNeighSysID_Object = MibTableColumn
ciiISAdjNeighSysID = _CiiISAdjNeighSysID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 6),
    _CiiISAdjNeighSysID_Type()
)
ciiISAdjNeighSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjNeighSysID.setStatus("current")
_CiiISAdjNbrExtendedCircID_Type = Unsigned32
_CiiISAdjNbrExtendedCircID_Object = MibTableColumn
ciiISAdjNbrExtendedCircID = _CiiISAdjNbrExtendedCircID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 7),
    _CiiISAdjNbrExtendedCircID_Type()
)
ciiISAdjNbrExtendedCircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjNbrExtendedCircID.setStatus("current")


class _CiiISAdjUsage_Type(Integer32):
    """Custom type ciiISAdjUsage based on Integer32"""
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


_CiiISAdjUsage_Type.__name__ = "Integer32"
_CiiISAdjUsage_Object = MibTableColumn
ciiISAdjUsage = _CiiISAdjUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 8),
    _CiiISAdjUsage_Type()
)
ciiISAdjUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjUsage.setStatus("current")


class _CiiISAdjHoldTimer_Type(CiiUnsigned16TC):
    """Custom type ciiISAdjHoldTimer based on CiiUnsigned16TC"""
    subtypeSpec = CiiUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiiISAdjHoldTimer_Type.__name__ = "CiiUnsigned16TC"
_CiiISAdjHoldTimer_Object = MibTableColumn
ciiISAdjHoldTimer = _CiiISAdjHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 9),
    _CiiISAdjHoldTimer_Type()
)
ciiISAdjHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    ciiISAdjHoldTimer.setUnits("seconds")
_CiiISAdjNeighPriority_Type = CiiISPriority
_CiiISAdjNeighPriority_Object = MibTableColumn
ciiISAdjNeighPriority = _CiiISAdjNeighPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 10),
    _CiiISAdjNeighPriority_Type()
)
ciiISAdjNeighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjNeighPriority.setStatus("current")
_CiiISAdjLastUpTime_Type = TimeTicks
_CiiISAdjLastUpTime_Object = MibTableColumn
ciiISAdjLastUpTime = _CiiISAdjLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 1, 1, 11),
    _CiiISAdjLastUpTime_Type()
)
ciiISAdjLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjLastUpTime.setStatus("current")
if mibBuilder.loadTexts:
    ciiISAdjLastUpTime.setUnits("hundredths of a second")
_CiiISAdjAreaAddrTable_Object = MibTable
ciiISAdjAreaAddrTable = _CiiISAdjAreaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ciiISAdjAreaAddrTable.setStatus("current")
_CiiISAdjAreaAddrEntry_Object = MibTableRow
ciiISAdjAreaAddrEntry = _CiiISAdjAreaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 2, 1)
)
ciiISAdjAreaAddrEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiISAdjIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiISAdjAreaAddrIndex"),
)
if mibBuilder.loadTexts:
    ciiISAdjAreaAddrEntry.setStatus("current")


class _CiiISAdjAreaAddrIndex_Type(Integer32):
    """Custom type ciiISAdjAreaAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_CiiISAdjAreaAddrIndex_Type.__name__ = "Integer32"
_CiiISAdjAreaAddrIndex_Object = MibTableColumn
ciiISAdjAreaAddrIndex = _CiiISAdjAreaAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 2, 1, 1),
    _CiiISAdjAreaAddrIndex_Type()
)
ciiISAdjAreaAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiISAdjAreaAddrIndex.setStatus("current")
_CiiISAdjAreaAddress_Type = CiiOSINSAddress
_CiiISAdjAreaAddress_Object = MibTableColumn
ciiISAdjAreaAddress = _CiiISAdjAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 2, 1, 2),
    _CiiISAdjAreaAddress_Type()
)
ciiISAdjAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjAreaAddress.setStatus("current")
_CiiISAdjIPAddrTable_Object = MibTable
ciiISAdjIPAddrTable = _CiiISAdjIPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 3)
)
if mibBuilder.loadTexts:
    ciiISAdjIPAddrTable.setStatus("current")
_CiiISAdjIPAddrEntry_Object = MibTableRow
ciiISAdjIPAddrEntry = _CiiISAdjIPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 3, 1)
)
ciiISAdjIPAddrEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiISAdjIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiISAdjIPAddrIndex"),
)
if mibBuilder.loadTexts:
    ciiISAdjIPAddrEntry.setStatus("current")


class _CiiISAdjIPAddrIndex_Type(Integer32):
    """Custom type ciiISAdjIPAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_CiiISAdjIPAddrIndex_Type.__name__ = "Integer32"
_CiiISAdjIPAddrIndex_Object = MibTableColumn
ciiISAdjIPAddrIndex = _CiiISAdjIPAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 3, 1, 1),
    _CiiISAdjIPAddrIndex_Type()
)
ciiISAdjIPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiISAdjIPAddrIndex.setStatus("current")
_CiiISAdjIPAddrType_Type = InetAddressType
_CiiISAdjIPAddrType_Object = MibTableColumn
ciiISAdjIPAddrType = _CiiISAdjIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 3, 1, 2),
    _CiiISAdjIPAddrType_Type()
)
ciiISAdjIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjIPAddrType.setStatus("current")


class _CiiISAdjIPAddrAddress_Type(InetAddress):
    """Custom type ciiISAdjIPAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CiiISAdjIPAddrAddress_Type.__name__ = "InetAddress"
_CiiISAdjIPAddrAddress_Object = MibTableColumn
ciiISAdjIPAddrAddress = _CiiISAdjIPAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 3, 1, 3),
    _CiiISAdjIPAddrAddress_Type()
)
ciiISAdjIPAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjIPAddrAddress.setStatus("current")
_CiiISAdjProtSuppTable_Object = MibTable
ciiISAdjProtSuppTable = _CiiISAdjProtSuppTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 4)
)
if mibBuilder.loadTexts:
    ciiISAdjProtSuppTable.setStatus("current")
_CiiISAdjProtSuppEntry_Object = MibTableRow
ciiISAdjProtSuppEntry = _CiiISAdjProtSuppEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 4, 1)
)
ciiISAdjProtSuppEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiISAdjIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiISAdjProtSuppProtocol"),
)
if mibBuilder.loadTexts:
    ciiISAdjProtSuppEntry.setStatus("current")
_CiiISAdjProtSuppProtocol_Type = CiiSupportedProtocol
_CiiISAdjProtSuppProtocol_Object = MibTableColumn
ciiISAdjProtSuppProtocol = _CiiISAdjProtSuppProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 6, 4, 1, 1),
    _CiiISAdjProtSuppProtocol_Type()
)
ciiISAdjProtSuppProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiISAdjProtSuppProtocol.setStatus("current")
_CiiReachAddr_ObjectIdentity = ObjectIdentity
ciiReachAddr = _CiiReachAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7)
)
_CiiRATable_Object = MibTable
ciiRATable = _CiiRATable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ciiRATable.setStatus("current")
_CiiRAEntry_Object = MibTableRow
ciiRAEntry = _CiiRAEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1)
)
ciiRAEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiCircIndex"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiRAIndex"),
)
if mibBuilder.loadTexts:
    ciiRAEntry.setStatus("current")


class _CiiRAIndex_Type(Integer32):
    """Custom type ciiRAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_CiiRAIndex_Type.__name__ = "Integer32"
_CiiRAIndex_Object = MibTableColumn
ciiRAIndex = _CiiRAIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 1),
    _CiiRAIndex_Type()
)
ciiRAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiRAIndex.setStatus("current")
_CiiRAExistState_Type = RowStatus
_CiiRAExistState_Object = MibTableColumn
ciiRAExistState = _CiiRAExistState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 2),
    _CiiRAExistState_Type()
)
ciiRAExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRAExistState.setStatus("current")


class _CiiRAAdminState_Type(CiiAdminState):
    """Custom type ciiRAAdminState based on CiiAdminState"""


_CiiRAAdminState_Object = MibTableColumn
ciiRAAdminState = _CiiRAAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 3),
    _CiiRAAdminState_Type()
)
ciiRAAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRAAdminState.setStatus("current")
_CiiRAAddrPrefix_Type = CiiOSINSAddress
_CiiRAAddrPrefix_Object = MibTableColumn
ciiRAAddrPrefix = _CiiRAAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 4),
    _CiiRAAddrPrefix_Type()
)
ciiRAAddrPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRAAddrPrefix.setStatus("current")


class _CiiRAMapType_Type(Integer32):
    """Custom type ciiRAMapType based on Integer32"""
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


_CiiRAMapType_Type.__name__ = "Integer32"
_CiiRAMapType_Object = MibTableColumn
ciiRAMapType = _CiiRAMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 5),
    _CiiRAMapType_Type()
)
ciiRAMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRAMapType.setStatus("current")


class _CiiRAMetric_Type(CiiDefaultMetric):
    """Custom type ciiRAMetric based on CiiDefaultMetric"""
    defaultValue = 20


_CiiRAMetric_Object = MibTableColumn
ciiRAMetric = _CiiRAMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 6),
    _CiiRAMetric_Type()
)
ciiRAMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRAMetric.setStatus("current")


class _CiiRAMetricType_Type(CiiMetricType):
    """Custom type ciiRAMetricType based on CiiMetricType"""


_CiiRAMetricType_Object = MibTableColumn
ciiRAMetricType = _CiiRAMetricType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 7),
    _CiiRAMetricType_Type()
)
ciiRAMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRAMetricType.setStatus("current")


class _CiiRASNPAAddress_Type(CiiOSINSAddress):
    """Custom type ciiRASNPAAddress based on CiiOSINSAddress"""
    defaultHexValue = ""


_CiiRASNPAAddress_Object = MibTableColumn
ciiRASNPAAddress = _CiiRASNPAAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 8),
    _CiiRASNPAAddress_Type()
)
ciiRASNPAAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRASNPAAddress.setStatus("current")


class _CiiRASNPAMask_Type(CiiOSINSAddress):
    """Custom type ciiRASNPAMask based on CiiOSINSAddress"""
    defaultHexValue = "00"


_CiiRASNPAMask_Object = MibTableColumn
ciiRASNPAMask = _CiiRASNPAMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 9),
    _CiiRASNPAMask_Type()
)
ciiRASNPAMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRASNPAMask.setStatus("current")


class _CiiRASNPAPrefix_Type(CiiOSINSAddress):
    """Custom type ciiRASNPAPrefix based on CiiOSINSAddress"""
    defaultHexValue = "00"


_CiiRASNPAPrefix_Object = MibTableColumn
ciiRASNPAPrefix = _CiiRASNPAPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 10),
    _CiiRASNPAPrefix_Type()
)
ciiRASNPAPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRASNPAPrefix.setStatus("current")


class _CiiRAType_Type(Integer32):
    """Custom type ciiRAType based on Integer32"""
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


_CiiRAType_Type.__name__ = "Integer32"
_CiiRAType_Object = MibTableColumn
ciiRAType = _CiiRAType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 7, 1, 1, 11),
    _CiiRAType_Type()
)
ciiRAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiRAType.setStatus("current")
_CiiIPReachAddr_ObjectIdentity = ObjectIdentity
ciiIPReachAddr = _CiiIPReachAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8)
)
_CiiIPRATable_Object = MibTable
ciiIPRATable = _CiiIPRATable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ciiIPRATable.setStatus("current")
_CiiIPRAEntry_Object = MibTableRow
ciiIPRAEntry = _CiiIPRAEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1)
)
ciiIPRAEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiIPRADestType"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiIPRADest"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiIPRADestPrefixLen"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiIPRANextHopIndex"),
)
if mibBuilder.loadTexts:
    ciiIPRAEntry.setStatus("current")
_CiiIPRADestType_Type = InetAddressType
_CiiIPRADestType_Object = MibTableColumn
ciiIPRADestType = _CiiIPRADestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 1),
    _CiiIPRADestType_Type()
)
ciiIPRADestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiIPRADestType.setStatus("current")


class _CiiIPRADest_Type(InetAddress):
    """Custom type ciiIPRADest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CiiIPRADest_Type.__name__ = "InetAddress"
_CiiIPRADest_Object = MibTableColumn
ciiIPRADest = _CiiIPRADest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 2),
    _CiiIPRADest_Type()
)
ciiIPRADest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiIPRADest.setStatus("current")


class _CiiIPRADestPrefixLen_Type(InetAddressPrefixLength):
    """Custom type ciiIPRADestPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CiiIPRADestPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_CiiIPRADestPrefixLen_Object = MibTableColumn
ciiIPRADestPrefixLen = _CiiIPRADestPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 3),
    _CiiIPRADestPrefixLen_Type()
)
ciiIPRADestPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiIPRADestPrefixLen.setStatus("current")


class _CiiIPRANextHopIndex_Type(Integer32):
    """Custom type ciiIPRANextHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiiIPRANextHopIndex_Type.__name__ = "Integer32"
_CiiIPRANextHopIndex_Object = MibTableColumn
ciiIPRANextHopIndex = _CiiIPRANextHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 4),
    _CiiIPRANextHopIndex_Type()
)
ciiIPRANextHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiIPRANextHopIndex.setStatus("current")
_CiiIPRANextHopType_Type = InetAddressType
_CiiIPRANextHopType_Object = MibTableColumn
ciiIPRANextHopType = _CiiIPRANextHopType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 5),
    _CiiIPRANextHopType_Type()
)
ciiIPRANextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPRANextHopType.setStatus("current")


class _CiiIPRANextHop_Type(InetAddress):
    """Custom type ciiIPRANextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CiiIPRANextHop_Type.__name__ = "InetAddress"
_CiiIPRANextHop_Object = MibTableColumn
ciiIPRANextHop = _CiiIPRANextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 6),
    _CiiIPRANextHop_Type()
)
ciiIPRANextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPRANextHop.setStatus("current")


class _CiiIPRAType_Type(Integer32):
    """Custom type ciiIPRAType based on Integer32"""
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


_CiiIPRAType_Type.__name__ = "Integer32"
_CiiIPRAType_Object = MibTableColumn
ciiIPRAType = _CiiIPRAType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 7),
    _CiiIPRAType_Type()
)
ciiIPRAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPRAType.setStatus("current")
_CiiIPRAExistState_Type = RowStatus
_CiiIPRAExistState_Object = MibTableColumn
ciiIPRAExistState = _CiiIPRAExistState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 8),
    _CiiIPRAExistState_Type()
)
ciiIPRAExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPRAExistState.setStatus("current")


class _CiiIPRAAdminState_Type(CiiAdminState):
    """Custom type ciiIPRAAdminState based on CiiAdminState"""


_CiiIPRAAdminState_Object = MibTableColumn
ciiIPRAAdminState = _CiiIPRAAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 9),
    _CiiIPRAAdminState_Type()
)
ciiIPRAAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPRAAdminState.setStatus("current")


class _CiiIPRAMetric_Type(CiiDefaultMetric):
    """Custom type ciiIPRAMetric based on CiiDefaultMetric"""
    defaultValue = 10


_CiiIPRAMetric_Object = MibTableColumn
ciiIPRAMetric = _CiiIPRAMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 10),
    _CiiIPRAMetric_Type()
)
ciiIPRAMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPRAMetric.setStatus("current")


class _CiiIPRAMetricType_Type(CiiMetricType):
    """Custom type ciiIPRAMetricType based on CiiMetricType"""


_CiiIPRAMetricType_Object = MibTableColumn
ciiIPRAMetricType = _CiiIPRAMetricType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 11),
    _CiiIPRAMetricType_Type()
)
ciiIPRAMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPRAMetricType.setStatus("current")


class _CiiIPRAFullMetric_Type(CiiFullMetric):
    """Custom type ciiIPRAFullMetric based on CiiFullMetric"""
    defaultValue = 10


_CiiIPRAFullMetric_Object = MibTableColumn
ciiIPRAFullMetric = _CiiIPRAFullMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 12),
    _CiiIPRAFullMetric_Type()
)
ciiIPRAFullMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPRAFullMetric.setStatus("current")


class _CiiIPRASNPAAddress_Type(CiiOSINSAddress):
    """Custom type ciiIPRASNPAAddress based on CiiOSINSAddress"""
    defaultHexValue = ""


_CiiIPRASNPAAddress_Object = MibTableColumn
ciiIPRASNPAAddress = _CiiIPRASNPAAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 13),
    _CiiIPRASNPAAddress_Type()
)
ciiIPRASNPAAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPRASNPAAddress.setStatus("current")


class _CiiIPRASourceType_Type(Integer32):
    """Custom type ciiIPRASourceType based on Integer32"""
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


_CiiIPRASourceType_Type.__name__ = "Integer32"
_CiiIPRASourceType_Object = MibTableColumn
ciiIPRASourceType = _CiiIPRASourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 8, 1, 1, 14),
    _CiiIPRASourceType_Type()
)
ciiIPRASourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiIPRASourceType.setStatus("current")
_CiiLSPDataBase_ObjectIdentity = ObjectIdentity
ciiLSPDataBase = _CiiLSPDataBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9)
)
_CiiLSPSummaryTable_Object = MibTable
ciiLSPSummaryTable = _CiiLSPSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ciiLSPSummaryTable.setStatus("current")
_CiiLSPSummaryEntry_Object = MibTableRow
ciiLSPSummaryEntry = _CiiLSPSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 1, 1)
)
ciiLSPSummaryEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiLSPLevel"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiLSPID"),
)
if mibBuilder.loadTexts:
    ciiLSPSummaryEntry.setStatus("current")
_CiiLSPLevel_Type = CiiISLevel
_CiiLSPLevel_Object = MibTableColumn
ciiLSPLevel = _CiiLSPLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 1, 1, 1),
    _CiiLSPLevel_Type()
)
ciiLSPLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiLSPLevel.setStatus("current")
_CiiLSPID_Type = CiiLinkStatePDUID
_CiiLSPID_Object = MibTableColumn
ciiLSPID = _CiiLSPID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 1, 1, 2),
    _CiiLSPID_Type()
)
ciiLSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiLSPID.setStatus("current")
_CiiLSPSeq_Type = Unsigned32
_CiiLSPSeq_Object = MibTableColumn
ciiLSPSeq = _CiiLSPSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 1, 1, 3),
    _CiiLSPSeq_Type()
)
ciiLSPSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPSeq.setStatus("current")
_CiiLSPZeroLife_Type = TruthValue
_CiiLSPZeroLife_Object = MibTableColumn
ciiLSPZeroLife = _CiiLSPZeroLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 1, 1, 4),
    _CiiLSPZeroLife_Type()
)
ciiLSPZeroLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPZeroLife.setStatus("current")
_CiiLSPChecksum_Type = CiiUnsigned16TC
_CiiLSPChecksum_Object = MibTableColumn
ciiLSPChecksum = _CiiLSPChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 1, 1, 5),
    _CiiLSPChecksum_Type()
)
ciiLSPChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPChecksum.setStatus("current")
_CiiLSPLifetimeRemain_Type = CiiUnsigned16TC
_CiiLSPLifetimeRemain_Object = MibTableColumn
ciiLSPLifetimeRemain = _CiiLSPLifetimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 1, 1, 6),
    _CiiLSPLifetimeRemain_Type()
)
ciiLSPLifetimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPLifetimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    ciiLSPLifetimeRemain.setUnits("seconds")
_CiiLSPPDULength_Type = CiiUnsigned16TC
_CiiLSPPDULength_Object = MibTableColumn
ciiLSPPDULength = _CiiLSPPDULength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 1, 1, 7),
    _CiiLSPPDULength_Type()
)
ciiLSPPDULength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPPDULength.setStatus("current")
_CiiLSPAttributes_Type = CiiUnsigned8TC
_CiiLSPAttributes_Object = MibTableColumn
ciiLSPAttributes = _CiiLSPAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 1, 1, 8),
    _CiiLSPAttributes_Type()
)
ciiLSPAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPAttributes.setStatus("current")
_CiiLSPTLVTable_Object = MibTable
ciiLSPTLVTable = _CiiLSPTLVTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ciiLSPTLVTable.setStatus("current")
_CiiLSPTLVEntry_Object = MibTableRow
ciiLSPTLVEntry = _CiiLSPTLVEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 2, 1)
)
ciiLSPTLVEntry.setIndexNames(
    (0, "CISCO-IETF-ISIS-MIB", "ciiLSPLevel"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiLSPID"),
    (0, "CISCO-IETF-ISIS-MIB", "ciiLSPTLVIndex"),
)
if mibBuilder.loadTexts:
    ciiLSPTLVEntry.setStatus("current")
_CiiLSPTLVIndex_Type = Unsigned32
_CiiLSPTLVIndex_Object = MibTableColumn
ciiLSPTLVIndex = _CiiLSPTLVIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 2, 1, 1),
    _CiiLSPTLVIndex_Type()
)
ciiLSPTLVIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiLSPTLVIndex.setStatus("current")
_CiiLSPTLVSeq_Type = Unsigned32
_CiiLSPTLVSeq_Object = MibTableColumn
ciiLSPTLVSeq = _CiiLSPTLVSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 2, 1, 2),
    _CiiLSPTLVSeq_Type()
)
ciiLSPTLVSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPTLVSeq.setStatus("current")
_CiiLSPTLVChecksum_Type = CiiUnsigned16TC
_CiiLSPTLVChecksum_Object = MibTableColumn
ciiLSPTLVChecksum = _CiiLSPTLVChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 2, 1, 3),
    _CiiLSPTLVChecksum_Type()
)
ciiLSPTLVChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPTLVChecksum.setStatus("current")
_CiiLSPTLVType_Type = CiiUnsigned8TC
_CiiLSPTLVType_Object = MibTableColumn
ciiLSPTLVType = _CiiLSPTLVType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 2, 1, 4),
    _CiiLSPTLVType_Type()
)
ciiLSPTLVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPTLVType.setStatus("current")
_CiiLSPTLVLen_Type = CiiUnsigned8TC
_CiiLSPTLVLen_Object = MibTableColumn
ciiLSPTLVLen = _CiiLSPTLVLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 2, 1, 5),
    _CiiLSPTLVLen_Type()
)
ciiLSPTLVLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPTLVLen.setStatus("current")


class _CiiLSPTLVValue_Type(OctetString):
    """Custom type ciiLSPTLVValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiiLSPTLVValue_Type.__name__ = "OctetString"
_CiiLSPTLVValue_Object = MibTableColumn
ciiLSPTLVValue = _CiiLSPTLVValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 9, 2, 1, 6),
    _CiiLSPTLVValue_Type()
)
ciiLSPTLVValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiLSPTLVValue.setStatus("current")
_CiiNotification_ObjectIdentity = ObjectIdentity
ciiNotification = _CiiNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10)
)
_CiiNotificationEntry_ObjectIdentity = ObjectIdentity
ciiNotificationEntry = _CiiNotificationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1)
)
_CiiPduLspId_Type = CiiLinkStatePDUID
_CiiPduLspId_Object = MibScalar
ciiPduLspId = _CiiPduLspId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 1),
    _CiiPduLspId_Type()
)
ciiPduLspId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiPduLspId.setStatus("current")
_CiiPduFragment_Type = CiiPDUHeader
_CiiPduFragment_Object = MibScalar
ciiPduFragment = _CiiPduFragment_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 2),
    _CiiPduFragment_Type()
)
ciiPduFragment.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiPduFragment.setStatus("current")
_CiiPduFieldLen_Type = CiiUnsigned8TC
_CiiPduFieldLen_Object = MibScalar
ciiPduFieldLen = _CiiPduFieldLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 3),
    _CiiPduFieldLen_Type()
)
ciiPduFieldLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiPduFieldLen.setStatus("current")
_CiiPduMaxAreaAddress_Type = CiiUnsigned8TC
_CiiPduMaxAreaAddress_Object = MibScalar
ciiPduMaxAreaAddress = _CiiPduMaxAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 4),
    _CiiPduMaxAreaAddress_Type()
)
ciiPduMaxAreaAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiPduMaxAreaAddress.setStatus("current")
_CiiPduProtocolVersion_Type = CiiUnsigned8TC
_CiiPduProtocolVersion_Object = MibScalar
ciiPduProtocolVersion = _CiiPduProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 5),
    _CiiPduProtocolVersion_Type()
)
ciiPduProtocolVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiPduProtocolVersion.setStatus("current")


class _CiiPduLspSize_Type(Integer32):
    """Custom type ciiPduLspSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiiPduLspSize_Type.__name__ = "Integer32"
_CiiPduLspSize_Object = MibScalar
ciiPduLspSize = _CiiPduLspSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 6),
    _CiiPduLspSize_Type()
)
ciiPduLspSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiPduLspSize.setStatus("current")


class _CiiPduOriginatingBufferSize_Type(CiiUnsigned16TC):
    """Custom type ciiPduOriginatingBufferSize based on CiiUnsigned16TC"""
    subtypeSpec = CiiUnsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_CiiPduOriginatingBufferSize_Type.__name__ = "CiiUnsigned16TC"
_CiiPduOriginatingBufferSize_Object = MibScalar
ciiPduOriginatingBufferSize = _CiiPduOriginatingBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 7),
    _CiiPduOriginatingBufferSize_Type()
)
ciiPduOriginatingBufferSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiPduOriginatingBufferSize.setStatus("current")


class _CiiPduProtocolsSupported_Type(OctetString):
    """Custom type ciiPduProtocolsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiiPduProtocolsSupported_Type.__name__ = "OctetString"
_CiiPduProtocolsSupported_Object = MibScalar
ciiPduProtocolsSupported = _CiiPduProtocolsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 8),
    _CiiPduProtocolsSupported_Type()
)
ciiPduProtocolsSupported.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiPduProtocolsSupported.setStatus("current")


class _CiiAdjState_Type(Integer32):
    """Custom type ciiAdjState based on Integer32"""
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


_CiiAdjState_Type.__name__ = "Integer32"
_CiiAdjState_Object = MibScalar
ciiAdjState = _CiiAdjState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 9),
    _CiiAdjState_Type()
)
ciiAdjState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiAdjState.setStatus("current")
_CiiErrorOffset_Type = Unsigned32
_CiiErrorOffset_Object = MibScalar
ciiErrorOffset = _CiiErrorOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 10),
    _CiiErrorOffset_Type()
)
ciiErrorOffset.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiErrorOffset.setStatus("current")


class _CiiErrorTLVType_Type(Unsigned32):
    """Custom type ciiErrorTLVType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiiErrorTLVType_Type.__name__ = "Unsigned32"
_CiiErrorTLVType_Object = MibScalar
ciiErrorTLVType = _CiiErrorTLVType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 11),
    _CiiErrorTLVType_Type()
)
ciiErrorTLVType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiErrorTLVType.setStatus("current")
_CiiNotifManualAddress_Type = CiiOSINSAddress
_CiiNotifManualAddress_Object = MibScalar
ciiNotifManualAddress = _CiiNotifManualAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 12),
    _CiiNotifManualAddress_Type()
)
ciiNotifManualAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiNotifManualAddress.setStatus("current")


class _CiiNotifIsLevelIndex_Type(Integer32):
    """Custom type ciiNotifIsLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_CiiNotifIsLevelIndex_Type.__name__ = "Integer32"
_CiiNotifIsLevelIndex_Object = MibScalar
ciiNotifIsLevelIndex = _CiiNotifIsLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 1, 10, 1, 13),
    _CiiNotifIsLevelIndex_Type()
)
ciiNotifIsLevelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciiNotifIsLevelIndex.setStatus("current")
_CiscoIetfIsisMIBConform_ObjectIdentity = ObjectIdentity
ciscoIetfIsisMIBConform = _CiscoIetfIsisMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2)
)
_CiscoIetfIsisMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIetfIsisMIBGroups = _CiscoIetfIsisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 1)
)
_CiscoIetfIsisMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIetfIsisMIBCompliances = _CiscoIetfIsisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 2)
)

# Managed Objects groups

ciscoIetfIsisSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 1, 1)
)
ciscoIetfIsisSystemGroup.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiSysVersion"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysType"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysID"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysMaxPathSplits"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysMaxLSPGenInt"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysPollESHelloRate"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysWaitTime"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysAdminState"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysL2toL1Leaking"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysMaxAge"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysLevelOrigLSPBuffSize"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysLevelMinLSPGenInt"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysLevelOverloadState"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysLevelSetOverload"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysLevelSetOverloadUntil"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysLevelMetricStyle"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysLevelSPFConsiders"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysLevelTEEnabled"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysReceiveLSPBufferSize"),
        ("CISCO-IETF-ISIS-MIB", "ciiManAreaAddrExistState"),
        ("CISCO-IETF-ISIS-MIB", "ciiAreaAddr"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysProtSuppExistState"),
        ("CISCO-IETF-ISIS-MIB", "ciiSummAddrExistState"),
        ("CISCO-IETF-ISIS-MIB", "ciiSummAddrMetric"),
        ("CISCO-IETF-ISIS-MIB", "ciiSummAddrFullMetric"),
        ("CISCO-IETF-ISIS-MIB", "ciiRedistributeAddrExistState"),
        ("CISCO-IETF-ISIS-MIB", "ciiRouterHostName"),
        ("CISCO-IETF-ISIS-MIB", "ciiRouterID"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatCorrLSPs"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatLSPDbaseOloads"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatManAddrDropFromAreas"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatAttmptToExMaxSeqNums"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatSeqNumSkips"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatOwnLSPPurges"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatIDFieldLenMismatches"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatPartChanges"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatSPFRuns"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatAuthTypeFails"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatAuthFails"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysStatLSPErrors"))
)
if mibBuilder.loadTexts:
    ciscoIetfIsisSystemGroup.setStatus("current")

ciscoIetfIsisCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 1, 2)
)
ciscoIetfIsisCircuitGroup.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNextCircIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfSubIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircAdminState"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircExistState"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircType"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircExtDomain"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircAdjChanges"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircNumAdj"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircInitFails"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircRejAdjs"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIDFieldLenMismatches"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircMaxAreaAddrMismatches"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircAuthTypeFails"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircAuthFails"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLANDesISChanges"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevel"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircPassiveCircuit"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircMeshGroupEnabled"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircMeshGroup"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircSmallHellos"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLastUpTime"),
        ("CISCO-IETF-ISIS-MIB", "ciiCirc3WayEnabled"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircExtendedCircID"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelMetric"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelWideMetric"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelISPriority"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelIDOctet"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelID"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelDesIS"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelHelloMultiplier"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelHelloTimer"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelDRHelloTimer"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelLSPThrottle"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelMinLSPRetransInt"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelCSNPInterval"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircLevelPartSNPInterval"))
)
if mibBuilder.loadTexts:
    ciscoIetfIsisCircuitGroup.setStatus("current")

ciscoIetfIsisISAdjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 1, 3)
)
ciscoIetfIsisISAdjGroup.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiISAdjState"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdj3WayState"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjNeighSNPAAddress"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjNeighSysType"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjNeighSysID"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjNbrExtendedCircID"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjUsage"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjHoldTimer"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjNeighPriority"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjLastUpTime"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjAreaAddress"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjIPAddrType"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjIPAddrAddress"),
        ("CISCO-IETF-ISIS-MIB", "ciiISAdjProtSuppProtocol"))
)
if mibBuilder.loadTexts:
    ciscoIetfIsisISAdjGroup.setStatus("current")

ciscoIetfIsisNotifObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 1, 4)
)
ciscoIetfIsisNotifObjectGroup.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiPduLspId"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFragment"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFieldLen"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduMaxAreaAddress"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduProtocolVersion"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspSize"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduOriginatingBufferSize"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduProtocolsSupported"),
        ("CISCO-IETF-ISIS-MIB", "ciiAdjState"),
        ("CISCO-IETF-ISIS-MIB", "ciiErrorOffset"),
        ("CISCO-IETF-ISIS-MIB", "ciiErrorTLVType"),
        ("CISCO-IETF-ISIS-MIB", "ciiNotifManualAddress"),
        ("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"))
)
if mibBuilder.loadTexts:
    ciscoIetfIsisNotifObjectGroup.setStatus("current")

ciscoIetfIsisISPDUCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 1, 6)
)
ciscoIetfIsisISPDUCounterGroup.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiPacketCountIIHellos"),
        ("CISCO-IETF-ISIS-MIB", "ciiPacketCountISHellos"),
        ("CISCO-IETF-ISIS-MIB", "ciiPacketCountESHellos"),
        ("CISCO-IETF-ISIS-MIB", "ciiPacketCountLSPs"),
        ("CISCO-IETF-ISIS-MIB", "ciiPacketCountCSNPs"),
        ("CISCO-IETF-ISIS-MIB", "ciiPacketCountPSNPs"),
        ("CISCO-IETF-ISIS-MIB", "ciiPacketCountUnknowns"))
)
if mibBuilder.loadTexts:
    ciscoIetfIsisISPDUCounterGroup.setStatus("current")

ciscoIetfIsisRATableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 1, 7)
)
ciscoIetfIsisRATableGroup.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiRAExistState"),
        ("CISCO-IETF-ISIS-MIB", "ciiRAAdminState"),
        ("CISCO-IETF-ISIS-MIB", "ciiRAAddrPrefix"),
        ("CISCO-IETF-ISIS-MIB", "ciiRAMapType"),
        ("CISCO-IETF-ISIS-MIB", "ciiRAMetric"),
        ("CISCO-IETF-ISIS-MIB", "ciiRAMetricType"),
        ("CISCO-IETF-ISIS-MIB", "ciiRASNPAAddress"),
        ("CISCO-IETF-ISIS-MIB", "ciiRASNPAMask"),
        ("CISCO-IETF-ISIS-MIB", "ciiRASNPAPrefix"),
        ("CISCO-IETF-ISIS-MIB", "ciiRAType"))
)
if mibBuilder.loadTexts:
    ciscoIetfIsisRATableGroup.setStatus("current")

ciscoIetfIsisISIPRADestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 1, 8)
)
ciscoIetfIsisISIPRADestGroup.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiIPRANextHopType"),
        ("CISCO-IETF-ISIS-MIB", "ciiIPRANextHop"),
        ("CISCO-IETF-ISIS-MIB", "ciiIPRAType"),
        ("CISCO-IETF-ISIS-MIB", "ciiIPRAExistState"),
        ("CISCO-IETF-ISIS-MIB", "ciiIPRAAdminState"),
        ("CISCO-IETF-ISIS-MIB", "ciiIPRAMetric"),
        ("CISCO-IETF-ISIS-MIB", "ciiIPRAFullMetric"),
        ("CISCO-IETF-ISIS-MIB", "ciiIPRAMetricType"),
        ("CISCO-IETF-ISIS-MIB", "ciiIPRASNPAAddress"),
        ("CISCO-IETF-ISIS-MIB", "ciiIPRASourceType"))
)
if mibBuilder.loadTexts:
    ciscoIetfIsisISIPRADestGroup.setStatus("current")

ciscoIetfIsisLSPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 1, 9)
)
ciscoIetfIsisLSPGroup.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiLSPSeq"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPZeroLife"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPChecksum"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPLifetimeRemain"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPPDULength"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPAttributes"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPTLVSeq"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPTLVChecksum"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPTLVType"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPTLVLen"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPTLVValue"))
)
if mibBuilder.loadTexts:
    ciscoIetfIsisLSPGroup.setStatus("current")


# Notification objects

ciiDatabaseOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 1)
)
ciiDatabaseOverload.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiSysLevelOverloadState"))
)
if mibBuilder.loadTexts:
    ciiDatabaseOverload.setStatus(
        "current"
    )

ciiManualAddressDrops = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 2)
)
ciiManualAddressDrops.setObjects(
    ("CISCO-IETF-ISIS-MIB", "ciiNotifManualAddress")
)
if mibBuilder.loadTexts:
    ciiManualAddressDrops.setStatus(
        "current"
    )

ciiCorruptedLSPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 3)
)
ciiCorruptedLSPDetected.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspId"))
)
if mibBuilder.loadTexts:
    ciiCorruptedLSPDetected.setStatus(
        "current"
    )

ciiAttemptToExceedMaxSequence = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 4)
)
ciiAttemptToExceedMaxSequence.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspId"))
)
if mibBuilder.loadTexts:
    ciiAttemptToExceedMaxSequence.setStatus(
        "current"
    )

ciiIDLenMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 5)
)
ciiIDLenMismatch.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFieldLen"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFragment"))
)
if mibBuilder.loadTexts:
    ciiIDLenMismatch.setStatus(
        "current"
    )

ciiMaxAreaAddressesMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 6)
)
ciiMaxAreaAddressesMismatch.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduMaxAreaAddress"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFragment"))
)
if mibBuilder.loadTexts:
    ciiMaxAreaAddressesMismatch.setStatus(
        "current"
    )

ciiOwnLSPPurge = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 7)
)
ciiOwnLSPPurge.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspId"))
)
if mibBuilder.loadTexts:
    ciiOwnLSPPurge.setStatus(
        "current"
    )

ciiSequenceNumberSkip = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 8)
)
ciiSequenceNumberSkip.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspId"))
)
if mibBuilder.loadTexts:
    ciiSequenceNumberSkip.setStatus(
        "current"
    )

ciiAuthenticationTypeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 9)
)
ciiAuthenticationTypeFailure.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFragment"))
)
if mibBuilder.loadTexts:
    ciiAuthenticationTypeFailure.setStatus(
        "current"
    )

ciiAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 10)
)
ciiAuthenticationFailure.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFragment"))
)
if mibBuilder.loadTexts:
    ciiAuthenticationFailure.setStatus(
        "current"
    )

ciiVersionSkew = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 11)
)
ciiVersionSkew.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduProtocolVersion"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFragment"))
)
if mibBuilder.loadTexts:
    ciiVersionSkew.setStatus(
        "current"
    )

ciiAreaMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 12)
)
ciiAreaMismatch.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFragment"))
)
if mibBuilder.loadTexts:
    ciiAreaMismatch.setStatus(
        "current"
    )

ciiRejectedAdjacency = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 13)
)
ciiRejectedAdjacency.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFragment"))
)
if mibBuilder.loadTexts:
    ciiRejectedAdjacency.setStatus(
        "current"
    )

ciiLSPTooLargeToPropagate = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 14)
)
ciiLSPTooLargeToPropagate.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspSize"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspId"))
)
if mibBuilder.loadTexts:
    ciiLSPTooLargeToPropagate.setStatus(
        "current"
    )

ciiOrigLSPBuffSizeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 15)
)
ciiOrigLSPBuffSizeMismatch.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspId"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduOriginatingBufferSize"))
)
if mibBuilder.loadTexts:
    ciiOrigLSPBuffSizeMismatch.setStatus(
        "current"
    )

ciiProtocolsSupportedMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 16)
)
ciiProtocolsSupportedMismatch.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduProtocolsSupported"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspId"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFragment"))
)
if mibBuilder.loadTexts:
    ciiProtocolsSupportedMismatch.setStatus(
        "current"
    )

ciiAdjacencyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 17)
)
ciiAdjacencyChange.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspId"),
        ("CISCO-IETF-ISIS-MIB", "ciiAdjState"))
)
if mibBuilder.loadTexts:
    ciiAdjacencyChange.setStatus(
        "current"
    )

ciiLSPErrorDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 0, 18)
)
ciiLSPErrorDetected.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiNotifIsLevelIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduLspId"),
        ("CISCO-IETF-ISIS-MIB", "ciiCircIfIndex"),
        ("CISCO-IETF-ISIS-MIB", "ciiPduFragment"),
        ("CISCO-IETF-ISIS-MIB", "ciiErrorOffset"),
        ("CISCO-IETF-ISIS-MIB", "ciiErrorTLVType"))
)
if mibBuilder.loadTexts:
    ciiLSPErrorDetected.setStatus(
        "current"
    )


# Notifications groups

ciscoIetfIsisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 1, 5)
)
ciscoIetfIsisNotificationGroup.setObjects(
      *(("CISCO-IETF-ISIS-MIB", "ciiDatabaseOverload"),
        ("CISCO-IETF-ISIS-MIB", "ciiManualAddressDrops"),
        ("CISCO-IETF-ISIS-MIB", "ciiCorruptedLSPDetected"),
        ("CISCO-IETF-ISIS-MIB", "ciiAttemptToExceedMaxSequence"),
        ("CISCO-IETF-ISIS-MIB", "ciiIDLenMismatch"),
        ("CISCO-IETF-ISIS-MIB", "ciiMaxAreaAddressesMismatch"),
        ("CISCO-IETF-ISIS-MIB", "ciiOwnLSPPurge"),
        ("CISCO-IETF-ISIS-MIB", "ciiSequenceNumberSkip"),
        ("CISCO-IETF-ISIS-MIB", "ciiAuthenticationTypeFailure"),
        ("CISCO-IETF-ISIS-MIB", "ciiAuthenticationFailure"),
        ("CISCO-IETF-ISIS-MIB", "ciiVersionSkew"),
        ("CISCO-IETF-ISIS-MIB", "ciiAreaMismatch"),
        ("CISCO-IETF-ISIS-MIB", "ciiRejectedAdjacency"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPTooLargeToPropagate"),
        ("CISCO-IETF-ISIS-MIB", "ciiOrigLSPBuffSizeMismatch"),
        ("CISCO-IETF-ISIS-MIB", "ciiProtocolsSupportedMismatch"),
        ("CISCO-IETF-ISIS-MIB", "ciiAdjacencyChange"),
        ("CISCO-IETF-ISIS-MIB", "ciiLSPErrorDetected"))
)
if mibBuilder.loadTexts:
    ciscoIetfIsisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIetfIsisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoIetfIsisMIBCompliance.setStatus(
        "current"
    )

ciscoIetfIsisMIBAdvCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 118, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoIetfIsisMIBAdvCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-ISIS-MIB",
    **{"CiiOSINSAddress": CiiOSINSAddress,
       "CiiSystemID": CiiSystemID,
       "CiiLinkStatePDUID": CiiLinkStatePDUID,
       "CiiAdminState": CiiAdminState,
       "CiiLSPBuffSize": CiiLSPBuffSize,
       "CiiLevelState": CiiLevelState,
       "CiiSupportedProtocol": CiiSupportedProtocol,
       "CiiDefaultMetric": CiiDefaultMetric,
       "CiiWideMetric": CiiWideMetric,
       "CiiFullMetric": CiiFullMetric,
       "CiiMetricType": CiiMetricType,
       "CiiMetricStyle": CiiMetricStyle,
       "CiiISLevel": CiiISLevel,
       "CiiPDUHeader": CiiPDUHeader,
       "CiiCircuitID": CiiCircuitID,
       "CiiISPriority": CiiISPriority,
       "CiiUnsigned16TC": CiiUnsigned16TC,
       "CiiUnsigned8TC": CiiUnsigned8TC,
       "ciscoIetfIsisMIB": ciscoIetfIsisMIB,
       "ciscoIetfIsisMIBNotifs": ciscoIetfIsisMIBNotifs,
       "ciiDatabaseOverload": ciiDatabaseOverload,
       "ciiManualAddressDrops": ciiManualAddressDrops,
       "ciiCorruptedLSPDetected": ciiCorruptedLSPDetected,
       "ciiAttemptToExceedMaxSequence": ciiAttemptToExceedMaxSequence,
       "ciiIDLenMismatch": ciiIDLenMismatch,
       "ciiMaxAreaAddressesMismatch": ciiMaxAreaAddressesMismatch,
       "ciiOwnLSPPurge": ciiOwnLSPPurge,
       "ciiSequenceNumberSkip": ciiSequenceNumberSkip,
       "ciiAuthenticationTypeFailure": ciiAuthenticationTypeFailure,
       "ciiAuthenticationFailure": ciiAuthenticationFailure,
       "ciiVersionSkew": ciiVersionSkew,
       "ciiAreaMismatch": ciiAreaMismatch,
       "ciiRejectedAdjacency": ciiRejectedAdjacency,
       "ciiLSPTooLargeToPropagate": ciiLSPTooLargeToPropagate,
       "ciiOrigLSPBuffSizeMismatch": ciiOrigLSPBuffSizeMismatch,
       "ciiProtocolsSupportedMismatch": ciiProtocolsSupportedMismatch,
       "ciiAdjacencyChange": ciiAdjacencyChange,
       "ciiLSPErrorDetected": ciiLSPErrorDetected,
       "ciscoIetfIsisMIBObjects": ciscoIetfIsisMIBObjects,
       "ciiSystem": ciiSystem,
       "ciiSysObject": ciiSysObject,
       "ciiSysVersion": ciiSysVersion,
       "ciiSysType": ciiSysType,
       "ciiSysID": ciiSysID,
       "ciiSysMaxPathSplits": ciiSysMaxPathSplits,
       "ciiSysMaxLSPGenInt": ciiSysMaxLSPGenInt,
       "ciiSysPollESHelloRate": ciiSysPollESHelloRate,
       "ciiSysWaitTime": ciiSysWaitTime,
       "ciiSysAdminState": ciiSysAdminState,
       "ciiSysL2toL1Leaking": ciiSysL2toL1Leaking,
       "ciiSysMaxAge": ciiSysMaxAge,
       "ciiSysReceiveLSPBufferSize": ciiSysReceiveLSPBufferSize,
       "ciiManAreaAddrTable": ciiManAreaAddrTable,
       "ciiManAreaAddrEntry": ciiManAreaAddrEntry,
       "ciiManAreaAddr": ciiManAreaAddr,
       "ciiManAreaAddrExistState": ciiManAreaAddrExistState,
       "ciiAreaAddrTable": ciiAreaAddrTable,
       "ciiAreaAddrEntry": ciiAreaAddrEntry,
       "ciiAreaAddr": ciiAreaAddr,
       "ciiSysProtSuppTable": ciiSysProtSuppTable,
       "ciiSysProtSuppEntry": ciiSysProtSuppEntry,
       "ciiSysProtSuppProtocol": ciiSysProtSuppProtocol,
       "ciiSysProtSuppExistState": ciiSysProtSuppExistState,
       "ciiSummAddrTable": ciiSummAddrTable,
       "ciiSummAddrEntry": ciiSummAddrEntry,
       "ciiSummAddressType": ciiSummAddressType,
       "ciiSummAddress": ciiSummAddress,
       "ciiSummAddrPrefixLen": ciiSummAddrPrefixLen,
       "ciiSummAddrExistState": ciiSummAddrExistState,
       "ciiSummAddrMetric": ciiSummAddrMetric,
       "ciiSummAddrFullMetric": ciiSummAddrFullMetric,
       "ciiRedistributeAddrTable": ciiRedistributeAddrTable,
       "ciiRedistributeAddrEntry": ciiRedistributeAddrEntry,
       "ciiRedistributeAddrType": ciiRedistributeAddrType,
       "ciiRedistributeAddrAddress": ciiRedistributeAddrAddress,
       "ciiRedistributeAddrPrefixLen": ciiRedistributeAddrPrefixLen,
       "ciiRedistributeAddrExistState": ciiRedistributeAddrExistState,
       "ciiRouterTable": ciiRouterTable,
       "ciiRouterEntry": ciiRouterEntry,
       "ciiRouterSysID": ciiRouterSysID,
       "ciiRouterLevel": ciiRouterLevel,
       "ciiRouterHostName": ciiRouterHostName,
       "ciiRouterID": ciiRouterID,
       "ciiSysLevel": ciiSysLevel,
       "ciiSysLevelTable": ciiSysLevelTable,
       "ciiSysLevelEntry": ciiSysLevelEntry,
       "ciiSysLevelIndex": ciiSysLevelIndex,
       "ciiSysLevelOrigLSPBuffSize": ciiSysLevelOrigLSPBuffSize,
       "ciiSysLevelMinLSPGenInt": ciiSysLevelMinLSPGenInt,
       "ciiSysLevelOverloadState": ciiSysLevelOverloadState,
       "ciiSysLevelSetOverload": ciiSysLevelSetOverload,
       "ciiSysLevelSetOverloadUntil": ciiSysLevelSetOverloadUntil,
       "ciiSysLevelMetricStyle": ciiSysLevelMetricStyle,
       "ciiSysLevelSPFConsiders": ciiSysLevelSPFConsiders,
       "ciiSysLevelTEEnabled": ciiSysLevelTEEnabled,
       "ciiCirc": ciiCirc,
       "ciiNextCircIndex": ciiNextCircIndex,
       "ciiCircTable": ciiCircTable,
       "ciiCircEntry": ciiCircEntry,
       "ciiCircIndex": ciiCircIndex,
       "ciiCircIfIndex": ciiCircIfIndex,
       "ciiCircIfSubIndex": ciiCircIfSubIndex,
       "ciiCircAdminState": ciiCircAdminState,
       "ciiCircExistState": ciiCircExistState,
       "ciiCircType": ciiCircType,
       "ciiCircExtDomain": ciiCircExtDomain,
       "ciiCircLevel": ciiCircLevel,
       "ciiCircPassiveCircuit": ciiCircPassiveCircuit,
       "ciiCircMeshGroupEnabled": ciiCircMeshGroupEnabled,
       "ciiCircMeshGroup": ciiCircMeshGroup,
       "ciiCircSmallHellos": ciiCircSmallHellos,
       "ciiCircLastUpTime": ciiCircLastUpTime,
       "ciiCirc3WayEnabled": ciiCirc3WayEnabled,
       "ciiCircExtendedCircID": ciiCircExtendedCircID,
       "ciiCircLevelValues": ciiCircLevelValues,
       "ciiCircLevelTable": ciiCircLevelTable,
       "ciiCircLevelEntry": ciiCircLevelEntry,
       "ciiCircLevelIndex": ciiCircLevelIndex,
       "ciiCircLevelMetric": ciiCircLevelMetric,
       "ciiCircLevelWideMetric": ciiCircLevelWideMetric,
       "ciiCircLevelISPriority": ciiCircLevelISPriority,
       "ciiCircLevelIDOctet": ciiCircLevelIDOctet,
       "ciiCircLevelID": ciiCircLevelID,
       "ciiCircLevelDesIS": ciiCircLevelDesIS,
       "ciiCircLevelHelloMultiplier": ciiCircLevelHelloMultiplier,
       "ciiCircLevelHelloTimer": ciiCircLevelHelloTimer,
       "ciiCircLevelDRHelloTimer": ciiCircLevelDRHelloTimer,
       "ciiCircLevelLSPThrottle": ciiCircLevelLSPThrottle,
       "ciiCircLevelMinLSPRetransInt": ciiCircLevelMinLSPRetransInt,
       "ciiCircLevelCSNPInterval": ciiCircLevelCSNPInterval,
       "ciiCircLevelPartSNPInterval": ciiCircLevelPartSNPInterval,
       "ciiCounters": ciiCounters,
       "ciiSystemCounterTable": ciiSystemCounterTable,
       "ciiSystemCounterEntry": ciiSystemCounterEntry,
       "ciiSysStatLevel": ciiSysStatLevel,
       "ciiSysStatCorrLSPs": ciiSysStatCorrLSPs,
       "ciiSysStatAuthTypeFails": ciiSysStatAuthTypeFails,
       "ciiSysStatAuthFails": ciiSysStatAuthFails,
       "ciiSysStatLSPDbaseOloads": ciiSysStatLSPDbaseOloads,
       "ciiSysStatManAddrDropFromAreas": ciiSysStatManAddrDropFromAreas,
       "ciiSysStatAttmptToExMaxSeqNums": ciiSysStatAttmptToExMaxSeqNums,
       "ciiSysStatSeqNumSkips": ciiSysStatSeqNumSkips,
       "ciiSysStatOwnLSPPurges": ciiSysStatOwnLSPPurges,
       "ciiSysStatIDFieldLenMismatches": ciiSysStatIDFieldLenMismatches,
       "ciiSysStatPartChanges": ciiSysStatPartChanges,
       "ciiSysStatSPFRuns": ciiSysStatSPFRuns,
       "ciiSysStatLSPErrors": ciiSysStatLSPErrors,
       "ciiCircuitCounterTable": ciiCircuitCounterTable,
       "ciiCircuitCounterEntry": ciiCircuitCounterEntry,
       "ciiCircuitType": ciiCircuitType,
       "ciiCircAdjChanges": ciiCircAdjChanges,
       "ciiCircNumAdj": ciiCircNumAdj,
       "ciiCircInitFails": ciiCircInitFails,
       "ciiCircRejAdjs": ciiCircRejAdjs,
       "ciiCircIDFieldLenMismatches": ciiCircIDFieldLenMismatches,
       "ciiCircMaxAreaAddrMismatches": ciiCircMaxAreaAddrMismatches,
       "ciiCircAuthTypeFails": ciiCircAuthTypeFails,
       "ciiCircAuthFails": ciiCircAuthFails,
       "ciiCircLANDesISChanges": ciiCircLANDesISChanges,
       "ciiPacketCounterTable": ciiPacketCounterTable,
       "ciiPacketCounterEntry": ciiPacketCounterEntry,
       "ciiPacketCountLevel": ciiPacketCountLevel,
       "ciiPacketCountDirection": ciiPacketCountDirection,
       "ciiPacketCountIIHellos": ciiPacketCountIIHellos,
       "ciiPacketCountISHellos": ciiPacketCountISHellos,
       "ciiPacketCountESHellos": ciiPacketCountESHellos,
       "ciiPacketCountLSPs": ciiPacketCountLSPs,
       "ciiPacketCountCSNPs": ciiPacketCountCSNPs,
       "ciiPacketCountPSNPs": ciiPacketCountPSNPs,
       "ciiPacketCountUnknowns": ciiPacketCountUnknowns,
       "ciiISAdj": ciiISAdj,
       "ciiISAdjTable": ciiISAdjTable,
       "ciiISAdjEntry": ciiISAdjEntry,
       "ciiISAdjIndex": ciiISAdjIndex,
       "ciiISAdjState": ciiISAdjState,
       "ciiISAdj3WayState": ciiISAdj3WayState,
       "ciiISAdjNeighSNPAAddress": ciiISAdjNeighSNPAAddress,
       "ciiISAdjNeighSysType": ciiISAdjNeighSysType,
       "ciiISAdjNeighSysID": ciiISAdjNeighSysID,
       "ciiISAdjNbrExtendedCircID": ciiISAdjNbrExtendedCircID,
       "ciiISAdjUsage": ciiISAdjUsage,
       "ciiISAdjHoldTimer": ciiISAdjHoldTimer,
       "ciiISAdjNeighPriority": ciiISAdjNeighPriority,
       "ciiISAdjLastUpTime": ciiISAdjLastUpTime,
       "ciiISAdjAreaAddrTable": ciiISAdjAreaAddrTable,
       "ciiISAdjAreaAddrEntry": ciiISAdjAreaAddrEntry,
       "ciiISAdjAreaAddrIndex": ciiISAdjAreaAddrIndex,
       "ciiISAdjAreaAddress": ciiISAdjAreaAddress,
       "ciiISAdjIPAddrTable": ciiISAdjIPAddrTable,
       "ciiISAdjIPAddrEntry": ciiISAdjIPAddrEntry,
       "ciiISAdjIPAddrIndex": ciiISAdjIPAddrIndex,
       "ciiISAdjIPAddrType": ciiISAdjIPAddrType,
       "ciiISAdjIPAddrAddress": ciiISAdjIPAddrAddress,
       "ciiISAdjProtSuppTable": ciiISAdjProtSuppTable,
       "ciiISAdjProtSuppEntry": ciiISAdjProtSuppEntry,
       "ciiISAdjProtSuppProtocol": ciiISAdjProtSuppProtocol,
       "ciiReachAddr": ciiReachAddr,
       "ciiRATable": ciiRATable,
       "ciiRAEntry": ciiRAEntry,
       "ciiRAIndex": ciiRAIndex,
       "ciiRAExistState": ciiRAExistState,
       "ciiRAAdminState": ciiRAAdminState,
       "ciiRAAddrPrefix": ciiRAAddrPrefix,
       "ciiRAMapType": ciiRAMapType,
       "ciiRAMetric": ciiRAMetric,
       "ciiRAMetricType": ciiRAMetricType,
       "ciiRASNPAAddress": ciiRASNPAAddress,
       "ciiRASNPAMask": ciiRASNPAMask,
       "ciiRASNPAPrefix": ciiRASNPAPrefix,
       "ciiRAType": ciiRAType,
       "ciiIPReachAddr": ciiIPReachAddr,
       "ciiIPRATable": ciiIPRATable,
       "ciiIPRAEntry": ciiIPRAEntry,
       "ciiIPRADestType": ciiIPRADestType,
       "ciiIPRADest": ciiIPRADest,
       "ciiIPRADestPrefixLen": ciiIPRADestPrefixLen,
       "ciiIPRANextHopIndex": ciiIPRANextHopIndex,
       "ciiIPRANextHopType": ciiIPRANextHopType,
       "ciiIPRANextHop": ciiIPRANextHop,
       "ciiIPRAType": ciiIPRAType,
       "ciiIPRAExistState": ciiIPRAExistState,
       "ciiIPRAAdminState": ciiIPRAAdminState,
       "ciiIPRAMetric": ciiIPRAMetric,
       "ciiIPRAMetricType": ciiIPRAMetricType,
       "ciiIPRAFullMetric": ciiIPRAFullMetric,
       "ciiIPRASNPAAddress": ciiIPRASNPAAddress,
       "ciiIPRASourceType": ciiIPRASourceType,
       "ciiLSPDataBase": ciiLSPDataBase,
       "ciiLSPSummaryTable": ciiLSPSummaryTable,
       "ciiLSPSummaryEntry": ciiLSPSummaryEntry,
       "ciiLSPLevel": ciiLSPLevel,
       "ciiLSPID": ciiLSPID,
       "ciiLSPSeq": ciiLSPSeq,
       "ciiLSPZeroLife": ciiLSPZeroLife,
       "ciiLSPChecksum": ciiLSPChecksum,
       "ciiLSPLifetimeRemain": ciiLSPLifetimeRemain,
       "ciiLSPPDULength": ciiLSPPDULength,
       "ciiLSPAttributes": ciiLSPAttributes,
       "ciiLSPTLVTable": ciiLSPTLVTable,
       "ciiLSPTLVEntry": ciiLSPTLVEntry,
       "ciiLSPTLVIndex": ciiLSPTLVIndex,
       "ciiLSPTLVSeq": ciiLSPTLVSeq,
       "ciiLSPTLVChecksum": ciiLSPTLVChecksum,
       "ciiLSPTLVType": ciiLSPTLVType,
       "ciiLSPTLVLen": ciiLSPTLVLen,
       "ciiLSPTLVValue": ciiLSPTLVValue,
       "ciiNotification": ciiNotification,
       "ciiNotificationEntry": ciiNotificationEntry,
       "ciiPduLspId": ciiPduLspId,
       "ciiPduFragment": ciiPduFragment,
       "ciiPduFieldLen": ciiPduFieldLen,
       "ciiPduMaxAreaAddress": ciiPduMaxAreaAddress,
       "ciiPduProtocolVersion": ciiPduProtocolVersion,
       "ciiPduLspSize": ciiPduLspSize,
       "ciiPduOriginatingBufferSize": ciiPduOriginatingBufferSize,
       "ciiPduProtocolsSupported": ciiPduProtocolsSupported,
       "ciiAdjState": ciiAdjState,
       "ciiErrorOffset": ciiErrorOffset,
       "ciiErrorTLVType": ciiErrorTLVType,
       "ciiNotifManualAddress": ciiNotifManualAddress,
       "ciiNotifIsLevelIndex": ciiNotifIsLevelIndex,
       "ciscoIetfIsisMIBConform": ciscoIetfIsisMIBConform,
       "ciscoIetfIsisMIBGroups": ciscoIetfIsisMIBGroups,
       "ciscoIetfIsisSystemGroup": ciscoIetfIsisSystemGroup,
       "ciscoIetfIsisCircuitGroup": ciscoIetfIsisCircuitGroup,
       "ciscoIetfIsisISAdjGroup": ciscoIetfIsisISAdjGroup,
       "ciscoIetfIsisNotifObjectGroup": ciscoIetfIsisNotifObjectGroup,
       "ciscoIetfIsisNotificationGroup": ciscoIetfIsisNotificationGroup,
       "ciscoIetfIsisISPDUCounterGroup": ciscoIetfIsisISPDUCounterGroup,
       "ciscoIetfIsisRATableGroup": ciscoIetfIsisRATableGroup,
       "ciscoIetfIsisISIPRADestGroup": ciscoIetfIsisISIPRADestGroup,
       "ciscoIetfIsisLSPGroup": ciscoIetfIsisLSPGroup,
       "ciscoIetfIsisMIBCompliances": ciscoIetfIsisMIBCompliances,
       "ciscoIetfIsisMIBCompliance": ciscoIetfIsisMIBCompliance,
       "ciscoIetfIsisMIBAdvCompliance": ciscoIetfIsisMIBAdvCompliance}
)
