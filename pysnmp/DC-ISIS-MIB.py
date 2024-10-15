# SNMP MIB module (DC-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DC-ISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:21 2024
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

(AuthUserDataString,
 EntityIndexOrZero,
 IfOperStatus,
 IgpShortcutMetricType,
 NumericIndex) = mibBuilder.importSymbols(
    "DC-MASTER-TC",
    "AuthUserDataString",
    "EntityIndexOrZero",
    "IfOperStatus",
    "IgpShortcutMetricType",
    "NumericIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
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

dcIsisMib = ModuleIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1)
)
dcIsisMib.setRevisions(
        ("2014-07-03 00:00",
         "2011-07-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OSINSAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class SystemID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class LinkStatePDUID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class AdminState(Integer32, TextualConvention):
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



class LSPBuffSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16000),
    )



class LevelState(Integer32, TextualConvention):
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



class SupportedProtocol(Integer32, TextualConvention):
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



class DefaultMetric(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class WideMetric(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )



class FullMetric(Unsigned32, TextualConvention):
    status = "current"


class MetricType(Integer32, TextualConvention):
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



class MetricStyle(Integer32, TextualConvention):
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



class ISLevel(Integer32, TextualConvention):
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



class IsisAdjLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("level1", 1),
          ("level1and2", 3),
          ("level2", 2),
          ("reserved", 0))
    )



class IsisPDUHeader(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CircuitID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
    )



class ISPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )



class Unsigned16TC(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Unsigned8TC(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class IsisAdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDown", 2),
          ("adminStatusUp", 1))
    )



class IsisOperStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )



class IsisMjStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("mjFailed", 10),
          ("mjFailedToRegister", 8),
          ("mjFailingOver", 9),
          ("mjJoinActive", 4),
          ("mjJoinGone", 7),
          ("mjNotJoined", 1),
          ("mjSentAddJoin", 2),
          ("mjSentDelJoin", 5),
          ("mjSentRegister", 3),
          ("mjSentUnregister", 6))
    )



class IsisSjStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sjFailed", 7),
          ("sjFailingOver", 6),
          ("sjJoinActive", 3),
          ("sjJoinGone", 5),
          ("sjJoinUnreg", 4),
          ("sjJoined", 2),
          ("sjNotJoined", 1))
    )



class IsisPmInterfaceId(Integer32, TextualConvention):
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
        *(("ifCSPF", 3),
          ("ifInterfaceInfo", 1),
          ("ifRtProtoInput", 2),
          ("ifSDC", 4))
    )



class IsisSdInterfaceId(Integer32, TextualConvention):
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
        *(("ifBidirectionalForwarding", 3),
          ("ifDataLink", 1),
          ("ifSubnetDependent", 2))
    )



class IsisSdEntityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifPDUInjectionTool", 2),
          ("ifProtocolManager", 1))
    )



class IsisAddrType(Integer32, TextualConvention):
    status = "current"
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipx", 4),
          ("none", 0),
          ("nsap", 3))
    )



class IsisAddrTypeBits(Bits, TextualConvention):
    status = "current"


class IsisSysRestartType(Integer32, TextualConvention):
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
        *(("none", 0),
          ("restart", 2),
          ("start", 1))
    )



# MIB Managed Objects in the order of their OIDs

_IsisObjects_ObjectIdentity = ObjectIdentity
isisObjects = _IsisObjects_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1)
)
_IsisSystem_ObjectIdentity = ObjectIdentity
isisSystem = _IsisSystem_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1)
)
_IsisSysTable_Object = MibTable
isisSysTable = _IsisSysTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    isisSysTable.setStatus("current")
_IsisSysEntry_Object = MibTableRow
isisSysEntry = _IsisSysEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1)
)
isisSysEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    isisSysEntry.setStatus("current")


class _IsisSysInstance_Type(Integer32):
    """Custom type isisSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsisSysInstance_Type.__name__ = "Integer32"
_IsisSysInstance_Object = MibTableColumn
isisSysInstance = _IsisSysInstance_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 1),
    _IsisSysInstance_Type()
)
isisSysInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSysInstance.setStatus("current")


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
_IsisSysVersion_Object = MibTableColumn
isisSysVersion = _IsisSysVersion_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 2),
    _IsisSysVersion_Type()
)
isisSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysVersion.setStatus("current")


class _IsisSysType_Type(Integer32):
    """Custom type isisSysType based on Integer32"""
    defaultValue = 3

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
        *(("level1IS", 1),
          ("level1L2IS", 3),
          ("level2IS", 2),
          ("reserved", 0))
    )


_IsisSysType_Type.__name__ = "Integer32"
_IsisSysType_Object = MibTableColumn
isisSysType = _IsisSysType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 3),
    _IsisSysType_Type()
)
isisSysType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysType.setStatus("current")
_IsisSysID_Type = SystemID
_IsisSysID_Object = MibTableColumn
isisSysID = _IsisSysID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 4),
    _IsisSysID_Type()
)
isisSysID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysID.setStatus("current")


class _IsisSysMaxPathSplits_Type(Integer32):
    """Custom type isisSysMaxPathSplits based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IsisSysMaxPathSplits_Type.__name__ = "Integer32"
_IsisSysMaxPathSplits_Object = MibTableColumn
isisSysMaxPathSplits = _IsisSysMaxPathSplits_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 5),
    _IsisSysMaxPathSplits_Type()
)
isisSysMaxPathSplits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxPathSplits.setStatus("current")


class _IsisSysMaxLSPGenInt_Type(Integer32):
    """Custom type isisSysMaxLSPGenInt based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65235),
    )


_IsisSysMaxLSPGenInt_Type.__name__ = "Integer32"
_IsisSysMaxLSPGenInt_Object = MibTableColumn
isisSysMaxLSPGenInt = _IsisSysMaxLSPGenInt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 6),
    _IsisSysMaxLSPGenInt_Type()
)
isisSysMaxLSPGenInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxLSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    isisSysMaxLSPGenInt.setUnits("seconds")


class _IsisSysPollESHelloRate_Type(Unsigned16TC):
    """Custom type isisSysPollESHelloRate based on Unsigned16TC"""
    defaultValue = 50

    subtypeSpec = Unsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysPollESHelloRate_Type.__name__ = "Unsigned16TC"
_IsisSysPollESHelloRate_Object = MibTableColumn
isisSysPollESHelloRate = _IsisSysPollESHelloRate_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 7),
    _IsisSysPollESHelloRate_Type()
)
isisSysPollESHelloRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysPollESHelloRate.setStatus("current")
if mibBuilder.loadTexts:
    isisSysPollESHelloRate.setUnits("seconds")


class _IsisSysWaitTime_Type(Unsigned16TC):
    """Custom type isisSysWaitTime based on Unsigned16TC"""
    defaultValue = 60

    subtypeSpec = Unsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysWaitTime_Type.__name__ = "Unsigned16TC"
_IsisSysWaitTime_Object = MibTableColumn
isisSysWaitTime = _IsisSysWaitTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 8),
    _IsisSysWaitTime_Type()
)
isisSysWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    isisSysWaitTime.setUnits("seconds")


class _IsisSysAdminState_Type(AdminState):
    """Custom type isisSysAdminState based on AdminState"""


_IsisSysAdminState_Object = MibTableColumn
isisSysAdminState = _IsisSysAdminState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 9),
    _IsisSysAdminState_Type()
)
isisSysAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysAdminState.setStatus("current")


class _IsisSysL2toL1Leaking_Type(TruthValue):
    """Custom type isisSysL2toL1Leaking based on TruthValue"""


_IsisSysL2toL1Leaking_Object = MibTableColumn
isisSysL2toL1Leaking = _IsisSysL2toL1Leaking_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 10),
    _IsisSysL2toL1Leaking_Type()
)
isisSysL2toL1Leaking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysL2toL1Leaking.setStatus("current")


class _IsisSysMaxAge_Type(Unsigned16TC):
    """Custom type isisSysMaxAge based on Unsigned16TC"""
    defaultValue = 1200

    subtypeSpec = Unsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 65535),
    )


_IsisSysMaxAge_Type.__name__ = "Unsigned16TC"
_IsisSysMaxAge_Object = MibTableColumn
isisSysMaxAge = _IsisSysMaxAge_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 11),
    _IsisSysMaxAge_Type()
)
isisSysMaxAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    isisSysMaxAge.setUnits("seconds")


class _IsisSysReceiveLSPBufferSize_Type(Unsigned16TC):
    """Custom type isisSysReceiveLSPBufferSize based on Unsigned16TC"""
    defaultValue = 1492

    subtypeSpec = Unsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1492, 16000),
    )


_IsisSysReceiveLSPBufferSize_Type.__name__ = "Unsigned16TC"
_IsisSysReceiveLSPBufferSize_Object = MibTableColumn
isisSysReceiveLSPBufferSize = _IsisSysReceiveLSPBufferSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 12),
    _IsisSysReceiveLSPBufferSize_Type()
)
isisSysReceiveLSPBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysReceiveLSPBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    isisSysReceiveLSPBufferSize.setUnits("bytes")
_IsisSysExistState_Type = RowStatus
_IsisSysExistState_Object = MibTableColumn
isisSysExistState = _IsisSysExistState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 13),
    _IsisSysExistState_Type()
)
isisSysExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysExistState.setStatus("current")


class _IsisSysOperStatus_Type(IsisOperStatus):
    """Custom type isisSysOperStatus based on IsisOperStatus"""


_IsisSysOperStatus_Object = MibTableColumn
isisSysOperStatus = _IsisSysOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 14),
    _IsisSysOperStatus_Type()
)
isisSysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysOperStatus.setStatus("current")


class _IsisSysAllowAutoI3Config_Type(TruthValue):
    """Custom type isisSysAllowAutoI3Config based on TruthValue"""


_IsisSysAllowAutoI3Config_Object = MibTableColumn
isisSysAllowAutoI3Config = _IsisSysAllowAutoI3Config_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 15),
    _IsisSysAllowAutoI3Config_Type()
)
isisSysAllowAutoI3Config.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysAllowAutoI3Config.setStatus("current")


class _IsisSysCalcMaxDelay_Type(Unsigned32):
    """Custom type isisSysCalcMaxDelay based on Unsigned32"""
    defaultValue = 5000


_IsisSysCalcMaxDelay_Object = MibTableColumn
isisSysCalcMaxDelay = _IsisSysCalcMaxDelay_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 16),
    _IsisSysCalcMaxDelay_Type()
)
isisSysCalcMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysCalcMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    isisSysCalcMaxDelay.setUnits("milliseconds")


class _IsisSysCalcThrshUpdStart_Type(Unsigned32):
    """Custom type isisSysCalcThrshUpdStart based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsisSysCalcThrshUpdStart_Type.__name__ = "Unsigned32"
_IsisSysCalcThrshUpdStart_Object = MibTableColumn
isisSysCalcThrshUpdStart = _IsisSysCalcThrshUpdStart_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 17),
    _IsisSysCalcThrshUpdStart_Type()
)
isisSysCalcThrshUpdStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysCalcThrshUpdStart.setStatus("current")


class _IsisSysCalcThrshUpdRestart_Type(Unsigned32):
    """Custom type isisSysCalcThrshUpdRestart based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsisSysCalcThrshUpdRestart_Type.__name__ = "Unsigned32"
_IsisSysCalcThrshUpdRestart_Object = MibTableColumn
isisSysCalcThrshUpdRestart = _IsisSysCalcThrshUpdRestart_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 18),
    _IsisSysCalcThrshUpdRestart_Type()
)
isisSysCalcThrshUpdRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysCalcThrshUpdRestart.setStatus("current")


class _IsisSysCalcThrshRestartLimit_Type(Unsigned32):
    """Custom type isisSysCalcThrshRestartLimit based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IsisSysCalcThrshRestartLimit_Type.__name__ = "Unsigned32"
_IsisSysCalcThrshRestartLimit_Object = MibTableColumn
isisSysCalcThrshRestartLimit = _IsisSysCalcThrshRestartLimit_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 19),
    _IsisSysCalcThrshRestartLimit_Type()
)
isisSysCalcThrshRestartLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysCalcThrshRestartLimit.setStatus("current")


class _IsisSysCalcPauseFreq_Type(Unsigned32):
    """Custom type isisSysCalcPauseFreq based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsisSysCalcPauseFreq_Type.__name__ = "Unsigned32"
_IsisSysCalcPauseFreq_Object = MibTableColumn
isisSysCalcPauseFreq = _IsisSysCalcPauseFreq_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 20),
    _IsisSysCalcPauseFreq_Type()
)
isisSysCalcPauseFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysCalcPauseFreq.setStatus("current")


class _IsisSysCheckChecksums_Type(Unsigned32):
    """Custom type isisSysCheckChecksums based on Unsigned32"""
    defaultValue = 900


_IsisSysCheckChecksums_Object = MibTableColumn
isisSysCheckChecksums = _IsisSysCheckChecksums_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 21),
    _IsisSysCheckChecksums_Type()
)
isisSysCheckChecksums.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysCheckChecksums.setStatus("current")
if mibBuilder.loadTexts:
    isisSysCheckChecksums.setUnits("seconds")


class _IsisSysZeroAgeLifetime_Type(Integer32):
    """Custom type isisSysZeroAgeLifetime based on Integer32"""
    defaultValue = 60


_IsisSysZeroAgeLifetime_Object = MibTableColumn
isisSysZeroAgeLifetime = _IsisSysZeroAgeLifetime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 22),
    _IsisSysZeroAgeLifetime_Type()
)
isisSysZeroAgeLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysZeroAgeLifetime.setStatus("current")
if mibBuilder.loadTexts:
    isisSysZeroAgeLifetime.setUnits("seconds")
_IsisSysNumUpdPending_Type = Gauge32
_IsisSysNumUpdPending_Object = MibTableColumn
isisSysNumUpdPending = _IsisSysNumUpdPending_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 23),
    _IsisSysNumUpdPending_Type()
)
isisSysNumUpdPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysNumUpdPending.setStatus("current")
_IsisSysNumUpdMerged_Type = Counter32
_IsisSysNumUpdMerged_Object = MibTableColumn
isisSysNumUpdMerged = _IsisSysNumUpdMerged_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 24),
    _IsisSysNumUpdMerged_Type()
)
isisSysNumUpdMerged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysNumUpdMerged.setStatus("current")
_IsisSysNumCksumsPending_Type = Gauge32
_IsisSysNumCksumsPending_Object = MibTableColumn
isisSysNumCksumsPending = _IsisSysNumCksumsPending_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 25),
    _IsisSysNumCksumsPending_Type()
)
isisSysNumCksumsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysNumCksumsPending.setStatus("current")


class _IsisSysTEMetricPcntge_Type(Integer32):
    """Custom type isisSysTEMetricPcntge based on Integer32"""
    defaultValue = 0


_IsisSysTEMetricPcntge_Object = MibTableColumn
isisSysTEMetricPcntge = _IsisSysTEMetricPcntge_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 26),
    _IsisSysTEMetricPcntge_Type()
)
isisSysTEMetricPcntge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysTEMetricPcntge.setStatus("current")


class _IsisSysMaxBwidthPcntge_Type(Integer32):
    """Custom type isisSysMaxBwidthPcntge based on Integer32"""
    defaultValue = 0


_IsisSysMaxBwidthPcntge_Object = MibTableColumn
isisSysMaxBwidthPcntge = _IsisSysMaxBwidthPcntge_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 27),
    _IsisSysMaxBwidthPcntge_Type()
)
isisSysMaxBwidthPcntge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxBwidthPcntge.setStatus("current")


class _IsisSysMaxResBwidthPcntge_Type(Integer32):
    """Custom type isisSysMaxResBwidthPcntge based on Integer32"""
    defaultValue = 0


_IsisSysMaxResBwidthPcntge_Object = MibTableColumn
isisSysMaxResBwidthPcntge = _IsisSysMaxResBwidthPcntge_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 28),
    _IsisSysMaxResBwidthPcntge_Type()
)
isisSysMaxResBwidthPcntge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxResBwidthPcntge.setStatus("current")


class _IsisSysUnresBwidthPcntge_Type(Integer32):
    """Custom type isisSysUnresBwidthPcntge based on Integer32"""
    defaultValue = 0


_IsisSysUnresBwidthPcntge_Object = MibTableColumn
isisSysUnresBwidthPcntge = _IsisSysUnresBwidthPcntge_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 29),
    _IsisSysUnresBwidthPcntge_Type()
)
isisSysUnresBwidthPcntge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysUnresBwidthPcntge.setStatus("current")


class _IsisSysMaxLSPBwidthPcntge_Type(Integer32):
    """Custom type isisSysMaxLSPBwidthPcntge based on Integer32"""
    defaultValue = 0


_IsisSysMaxLSPBwidthPcntge_Object = MibTableColumn
isisSysMaxLSPBwidthPcntge = _IsisSysMaxLSPBwidthPcntge_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 30),
    _IsisSysMaxLSPBwidthPcntge_Type()
)
isisSysMaxLSPBwidthPcntge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxLSPBwidthPcntge.setStatus("current")


class _IsisSysMinLSPBwidthPcntge_Type(Integer32):
    """Custom type isisSysMinLSPBwidthPcntge based on Integer32"""
    defaultValue = 0


_IsisSysMinLSPBwidthPcntge_Object = MibTableColumn
isisSysMinLSPBwidthPcntge = _IsisSysMinLSPBwidthPcntge_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 31),
    _IsisSysMinLSPBwidthPcntge_Type()
)
isisSysMinLSPBwidthPcntge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMinLSPBwidthPcntge.setStatus("current")


class _IsisSysMTUSizePcntge_Type(Integer32):
    """Custom type isisSysMTUSizePcntge based on Integer32"""
    defaultValue = 0


_IsisSysMTUSizePcntge_Object = MibTableColumn
isisSysMTUSizePcntge = _IsisSysMTUSizePcntge_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 32),
    _IsisSysMTUSizePcntge_Type()
)
isisSysMTUSizePcntge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMTUSizePcntge.setStatus("current")
_IsisSysTERouterID_Type = InetAddressIPv4
_IsisSysTERouterID_Object = MibTableColumn
isisSysTERouterID = _IsisSysTERouterID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 33),
    _IsisSysTERouterID_Type()
)
isisSysTERouterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysTERouterID.setStatus("current")
_IsisSysIPv6TERouterID_Type = InetAddressIPv6
_IsisSysIPv6TERouterID_Object = MibTableColumn
isisSysIPv6TERouterID = _IsisSysIPv6TERouterID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 34),
    _IsisSysIPv6TERouterID_Type()
)
isisSysIPv6TERouterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysIPv6TERouterID.setStatus("current")


class _IsisSysMaxExternalRoutes_Type(Unsigned32):
    """Custom type isisSysMaxExternalRoutes based on Unsigned32"""
    defaultValue = 4294967295


_IsisSysMaxExternalRoutes_Object = MibTableColumn
isisSysMaxExternalRoutes = _IsisSysMaxExternalRoutes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 35),
    _IsisSysMaxExternalRoutes_Type()
)
isisSysMaxExternalRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxExternalRoutes.setStatus("current")


class _IsisSysMaxExternalRoutesAction_Type(Integer32):
    """Custom type isisSysMaxExternalRoutesAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("suppressExternal", 2))
    )


_IsisSysMaxExternalRoutesAction_Type.__name__ = "Integer32"
_IsisSysMaxExternalRoutesAction_Object = MibTableColumn
isisSysMaxExternalRoutesAction = _IsisSysMaxExternalRoutesAction_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 36),
    _IsisSysMaxExternalRoutesAction_Type()
)
isisSysMaxExternalRoutesAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxExternalRoutesAction.setStatus("current")


class _IsisSysLspFullSuppress_Type(Integer32):
    """Custom type isisSysLspFullSuppress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("none", 2))
    )


_IsisSysLspFullSuppress_Type.__name__ = "Integer32"
_IsisSysLspFullSuppress_Object = MibTableColumn
isisSysLspFullSuppress = _IsisSysLspFullSuppress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 37),
    _IsisSysLspFullSuppress_Type()
)
isisSysLspFullSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLspFullSuppress.setStatus("current")


class _IsisSysLspFullSetDBOL_Type(TruthValue):
    """Custom type isisSysLspFullSetDBOL based on TruthValue"""


_IsisSysLspFullSetDBOL_Object = MibTableColumn
isisSysLspFullSetDBOL = _IsisSysLspFullSetDBOL_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 38),
    _IsisSysLspFullSetDBOL_Type()
)
isisSysLspFullSetDBOL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLspFullSetDBOL.setStatus("current")


class _IsisSysRestartHelpPeer_Type(TruthValue):
    """Custom type isisSysRestartHelpPeer based on TruthValue"""


_IsisSysRestartHelpPeer_Object = MibTableColumn
isisSysRestartHelpPeer = _IsisSysRestartHelpPeer_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 39),
    _IsisSysRestartHelpPeer_Type()
)
isisSysRestartHelpPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysRestartHelpPeer.setStatus("current")


class _IsisSysRestartActivationType_Type(IsisSysRestartType):
    """Custom type isisSysRestartActivationType based on IsisSysRestartType"""


_IsisSysRestartActivationType_Object = MibTableColumn
isisSysRestartActivationType = _IsisSysRestartActivationType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 40),
    _IsisSysRestartActivationType_Type()
)
isisSysRestartActivationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysRestartActivationType.setStatus("current")


class _IsisSysRestartAutoResetType_Type(IsisSysRestartType):
    """Custom type isisSysRestartAutoResetType based on IsisSysRestartType"""


_IsisSysRestartAutoResetType_Object = MibTableColumn
isisSysRestartAutoResetType = _IsisSysRestartAutoResetType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 41),
    _IsisSysRestartAutoResetType_Type()
)
isisSysRestartAutoResetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysRestartAutoResetType.setStatus("current")


class _IsisSysRestartAdjacencyWait_Type(Integer32):
    """Custom type isisSysRestartAdjacencyWait based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_IsisSysRestartAdjacencyWait_Type.__name__ = "Integer32"
_IsisSysRestartAdjacencyWait_Object = MibTableColumn
isisSysRestartAdjacencyWait = _IsisSysRestartAdjacencyWait_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 42),
    _IsisSysRestartAdjacencyWait_Type()
)
isisSysRestartAdjacencyWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysRestartAdjacencyWait.setStatus("current")
if mibBuilder.loadTexts:
    isisSysRestartAdjacencyWait.setUnits("seconds")


class _IsisSysMaxRecoveryTime_Type(Integer32):
    """Custom type isisSysMaxRecoveryTime based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisSysMaxRecoveryTime_Type.__name__ = "Integer32"
_IsisSysMaxRecoveryTime_Object = MibTableColumn
isisSysMaxRecoveryTime = _IsisSysMaxRecoveryTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 43),
    _IsisSysMaxRecoveryTime_Type()
)
isisSysMaxRecoveryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysMaxRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    isisSysMaxRecoveryTime.setUnits("seconds")


class _IsisSysClearStats_Type(TruthValue):
    """Custom type isisSysClearStats based on TruthValue"""


_IsisSysClearStats_Object = MibTableColumn
isisSysClearStats = _IsisSysClearStats_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 44),
    _IsisSysClearStats_Type()
)
isisSysClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysClearStats.setStatus("current")


class _IsisSysSetAttached_Type(Integer32):
    """Custom type isisSysSetAttached based on Integer32"""
    defaultValue = 1

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
        *(("attachClear", 4),
          ("attachNoOverlapOnly", 2),
          ("attachNoOverlapOrRedist", 1),
          ("attachSet", 3))
    )


_IsisSysSetAttached_Type.__name__ = "Integer32"
_IsisSysSetAttached_Object = MibTableColumn
isisSysSetAttached = _IsisSysSetAttached_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 45),
    _IsisSysSetAttached_Type()
)
isisSysSetAttached.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysSetAttached.setStatus("current")


class _IsisSysProtSupported_Type(IsisAddrTypeBits):
    """Custom type isisSysProtSupported based on IsisAddrTypeBits"""
    defaultBinValue = "01"


_IsisSysProtSupported_Object = MibTableColumn
isisSysProtSupported = _IsisSysProtSupported_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 46),
    _IsisSysProtSupported_Type()
)
isisSysProtSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysProtSupported.setStatus("current")


class _IsisSysRestrictLanAdjsToSubnet_Type(TruthValue):
    """Custom type isisSysRestrictLanAdjsToSubnet based on TruthValue"""


_IsisSysRestrictLanAdjsToSubnet_Object = MibTableColumn
isisSysRestrictLanAdjsToSubnet = _IsisSysRestrictLanAdjsToSubnet_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 47),
    _IsisSysRestrictLanAdjsToSubnet_Type()
)
isisSysRestrictLanAdjsToSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysRestrictLanAdjsToSubnet.setStatus("current")
_IsisSysHostName_Type = SnmpAdminString
_IsisSysHostName_Object = MibTableColumn
isisSysHostName = _IsisSysHostName_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 48),
    _IsisSysHostName_Type()
)
isisSysHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysHostName.setStatus("current")


class _IsisSysCalcSoonAfterCircChange_Type(TruthValue):
    """Custom type isisSysCalcSoonAfterCircChange based on TruthValue"""


_IsisSysCalcSoonAfterCircChange_Object = MibTableColumn
isisSysCalcSoonAfterCircChange = _IsisSysCalcSoonAfterCircChange_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 49),
    _IsisSysCalcSoonAfterCircChange_Type()
)
isisSysCalcSoonAfterCircChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysCalcSoonAfterCircChange.setStatus("current")


class _IsisSysSendNotifications_Type(Bits):
    """Custom type isisSysSendNotifications based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("adjacencyChange", 8),
          ("areaMismatch", 6),
          ("attachStateChange", 17),
          ("attemptToExceedMaxSequence", 10),
          ("circuitIndication", 0),
          ("databaseOverload", 1),
          ("disChange", 14),
          ("extPassCircuitInd", 12),
          ("helloAuthFailure", 16),
          ("idLengthMismatch", 3),
          ("lspAuthFailure", 15),
          ("lspErrorDetected", 9),
          ("manualAreaAddressDrops", 2),
          ("maxAreaAddressMismatch", 4),
          ("operStateChange", 13),
          ("ownLspPurge", 5),
          ("rejectedAdjacency", 7),
          ("sequenceNumberSkip", 11))
    )

_IsisSysSendNotifications_Type.__name__ = "Bits"
_IsisSysSendNotifications_Object = MibTableColumn
isisSysSendNotifications = _IsisSysSendNotifications_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 50),
    _IsisSysSendNotifications_Type()
)
isisSysSendNotifications.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysSendNotifications.setStatus("current")


class _IsisSysEnableIgpShortcut_Type(TruthValue):
    """Custom type isisSysEnableIgpShortcut based on TruthValue"""


_IsisSysEnableIgpShortcut_Object = MibTableColumn
isisSysEnableIgpShortcut = _IsisSysEnableIgpShortcut_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 51),
    _IsisSysEnableIgpShortcut_Type()
)
isisSysEnableIgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysEnableIgpShortcut.setStatus("current")


class _IsisSysI3EntityIndex_Type(NumericIndex):
    """Custom type isisSysI3EntityIndex based on NumericIndex"""
    defaultValue = 1


_IsisSysI3EntityIndex_Object = MibTableColumn
isisSysI3EntityIndex = _IsisSysI3EntityIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 52),
    _IsisSysI3EntityIndex_Type()
)
isisSysI3EntityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysI3EntityIndex.setStatus("current")


class _IsisSysRtmPurgeTime_Type(Integer32):
    """Custom type isisSysRtmPurgeTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsisSysRtmPurgeTime_Type.__name__ = "Integer32"
_IsisSysRtmPurgeTime_Object = MibTableColumn
isisSysRtmPurgeTime = _IsisSysRtmPurgeTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 1, 1, 53),
    _IsisSysRtmPurgeTime_Type()
)
isisSysRtmPurgeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysRtmPurgeTime.setStatus("current")
if mibBuilder.loadTexts:
    isisSysRtmPurgeTime.setUnits("seconds")
_IsisManAreaAddrTable_Object = MibTable
isisManAreaAddrTable = _IsisManAreaAddrTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    isisManAreaAddrTable.setStatus("current")
_IsisManAreaAddrEntry_Object = MibTableRow
isisManAreaAddrEntry = _IsisManAreaAddrEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 2, 1)
)
isisManAreaAddrEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisManAreaAddr"),
)
if mibBuilder.loadTexts:
    isisManAreaAddrEntry.setStatus("current")
_IsisManAreaAddr_Type = OSINSAddress
_IsisManAreaAddr_Object = MibTableColumn
isisManAreaAddr = _IsisManAreaAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 2, 1, 1),
    _IsisManAreaAddr_Type()
)
isisManAreaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisManAreaAddr.setStatus("current")
_IsisManAreaAddrExistState_Type = RowStatus
_IsisManAreaAddrExistState_Object = MibTableColumn
isisManAreaAddrExistState = _IsisManAreaAddrExistState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 2, 1, 2),
    _IsisManAreaAddrExistState_Type()
)
isisManAreaAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisManAreaAddrExistState.setStatus("current")
_IsisAreaAddrTable_Object = MibTable
isisAreaAddrTable = _IsisAreaAddrTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    isisAreaAddrTable.setStatus("current")
_IsisAreaAddrEntry_Object = MibTableRow
isisAreaAddrEntry = _IsisAreaAddrEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 3, 1)
)
isisAreaAddrEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisAreaAddr"),
)
if mibBuilder.loadTexts:
    isisAreaAddrEntry.setStatus("current")
_IsisAreaAddr_Type = OSINSAddress
_IsisAreaAddr_Object = MibTableColumn
isisAreaAddr = _IsisAreaAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 3, 1, 1),
    _IsisAreaAddr_Type()
)
isisAreaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisAreaAddr.setStatus("current")
_IsisAreaAddrInLSP_Type = TruthValue
_IsisAreaAddrInLSP_Object = MibTableColumn
isisAreaAddrInLSP = _IsisAreaAddrInLSP_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 3, 1, 2),
    _IsisAreaAddrInLSP_Type()
)
isisAreaAddrInLSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisAreaAddrInLSP.setStatus("current")
_IsisSummAddrTable_Object = MibTable
isisSummAddrTable = _IsisSummAddrTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    isisSummAddrTable.setStatus("current")
_IsisSummAddrEntry_Object = MibTableRow
isisSummAddrEntry = _IsisSummAddrEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 5, 1)
)
isisSummAddrEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisSummAddrMtId"),
    (0, "DC-ISIS-MIB", "isisSummAddressType"),
    (0, "DC-ISIS-MIB", "isisSummAddress"),
    (0, "DC-ISIS-MIB", "isisSummAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    isisSummAddrEntry.setStatus("current")
_IsisSummAddressType_Type = InetAddressType
_IsisSummAddressType_Object = MibTableColumn
isisSummAddressType = _IsisSummAddressType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 5, 1, 1),
    _IsisSummAddressType_Type()
)
isisSummAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSummAddressType.setStatus("current")


class _IsisSummAddress_Type(InetAddress):
    """Custom type isisSummAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IsisSummAddress_Type.__name__ = "InetAddress"
_IsisSummAddress_Object = MibTableColumn
isisSummAddress = _IsisSummAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 5, 1, 2),
    _IsisSummAddress_Type()
)
isisSummAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSummAddress.setStatus("current")


class _IsisSummAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type isisSummAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IsisSummAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_IsisSummAddrPrefixLen_Object = MibTableColumn
isisSummAddrPrefixLen = _IsisSummAddrPrefixLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 5, 1, 3),
    _IsisSummAddrPrefixLen_Type()
)
isisSummAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSummAddrPrefixLen.setStatus("current")
_IsisSummAddrExistState_Type = RowStatus
_IsisSummAddrExistState_Object = MibTableColumn
isisSummAddrExistState = _IsisSummAddrExistState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 5, 1, 4),
    _IsisSummAddrExistState_Type()
)
isisSummAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSummAddrExistState.setStatus("current")


class _IsisSummAddrMetric_Type(Integer32):
    """Custom type isisSummAddrMetric based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_IsisSummAddrMetric_Type.__name__ = "Integer32"
_IsisSummAddrMetric_Object = MibTableColumn
isisSummAddrMetric = _IsisSummAddrMetric_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 5, 1, 5),
    _IsisSummAddrMetric_Type()
)
isisSummAddrMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSummAddrMetric.setStatus("current")


class _IsisSummAddrFullMetric_Type(FullMetric):
    """Custom type isisSummAddrFullMetric based on FullMetric"""
    defaultValue = 20


_IsisSummAddrFullMetric_Object = MibTableColumn
isisSummAddrFullMetric = _IsisSummAddrFullMetric_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 5, 1, 6),
    _IsisSummAddrFullMetric_Type()
)
isisSummAddrFullMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSummAddrFullMetric.setStatus("current")


class _IsisSummAddrMtId_Type(Integer32):
    """Custom type isisSummAddrMtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IsisSummAddrMtId_Type.__name__ = "Integer32"
_IsisSummAddrMtId_Object = MibTableColumn
isisSummAddrMtId = _IsisSummAddrMtId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 5, 1, 8),
    _IsisSummAddrMtId_Type()
)
isisSummAddrMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSummAddrMtId.setStatus("current")
_IsisRedistributeAddrTable_Object = MibTable
isisRedistributeAddrTable = _IsisRedistributeAddrTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    isisRedistributeAddrTable.setStatus("current")
_IsisRedistributeAddrEntry_Object = MibTableRow
isisRedistributeAddrEntry = _IsisRedistributeAddrEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 6, 1)
)
isisRedistributeAddrEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisRedistributeAddrMtId"),
    (0, "DC-ISIS-MIB", "isisRedistributeAddrType"),
    (0, "DC-ISIS-MIB", "isisRedistributeAddrAddress"),
    (0, "DC-ISIS-MIB", "isisRedistributeAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    isisRedistributeAddrEntry.setStatus("current")
_IsisRedistributeAddrType_Type = InetAddressType
_IsisRedistributeAddrType_Object = MibTableColumn
isisRedistributeAddrType = _IsisRedistributeAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 6, 1, 1),
    _IsisRedistributeAddrType_Type()
)
isisRedistributeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRedistributeAddrType.setStatus("current")


class _IsisRedistributeAddrAddress_Type(InetAddress):
    """Custom type isisRedistributeAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IsisRedistributeAddrAddress_Type.__name__ = "InetAddress"
_IsisRedistributeAddrAddress_Object = MibTableColumn
isisRedistributeAddrAddress = _IsisRedistributeAddrAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 6, 1, 2),
    _IsisRedistributeAddrAddress_Type()
)
isisRedistributeAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRedistributeAddrAddress.setStatus("current")


class _IsisRedistributeAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type isisRedistributeAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IsisRedistributeAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_IsisRedistributeAddrPrefixLen_Object = MibTableColumn
isisRedistributeAddrPrefixLen = _IsisRedistributeAddrPrefixLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 6, 1, 3),
    _IsisRedistributeAddrPrefixLen_Type()
)
isisRedistributeAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRedistributeAddrPrefixLen.setStatus("current")
_IsisRedistributeAddrExistState_Type = RowStatus
_IsisRedistributeAddrExistState_Object = MibTableColumn
isisRedistributeAddrExistState = _IsisRedistributeAddrExistState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 6, 1, 4),
    _IsisRedistributeAddrExistState_Type()
)
isisRedistributeAddrExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisRedistributeAddrExistState.setStatus("current")


class _IsisRedistributeAddrMtId_Type(Integer32):
    """Custom type isisRedistributeAddrMtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IsisRedistributeAddrMtId_Type.__name__ = "Integer32"
_IsisRedistributeAddrMtId_Object = MibTableColumn
isisRedistributeAddrMtId = _IsisRedistributeAddrMtId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 6, 1, 6),
    _IsisRedistributeAddrMtId_Type()
)
isisRedistributeAddrMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRedistributeAddrMtId.setStatus("current")
_IsisRouterTable_Object = MibTable
isisRouterTable = _IsisRouterTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    isisRouterTable.setStatus("current")
_IsisRouterEntry_Object = MibTableRow
isisRouterEntry = _IsisRouterEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 7, 1)
)
isisRouterEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisRouterSysID"),
    (0, "DC-ISIS-MIB", "isisRouterLevel"),
)
if mibBuilder.loadTexts:
    isisRouterEntry.setStatus("current")
_IsisRouterSysID_Type = SystemID
_IsisRouterSysID_Object = MibTableColumn
isisRouterSysID = _IsisRouterSysID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 7, 1, 1),
    _IsisRouterSysID_Type()
)
isisRouterSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRouterSysID.setStatus("current")
_IsisRouterLevel_Type = ISLevel
_IsisRouterLevel_Object = MibTableColumn
isisRouterLevel = _IsisRouterLevel_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 7, 1, 2),
    _IsisRouterLevel_Type()
)
isisRouterLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisRouterLevel.setStatus("current")
_IsisRouterHostName_Type = SnmpAdminString
_IsisRouterHostName_Object = MibTableColumn
isisRouterHostName = _IsisRouterHostName_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 7, 1, 3),
    _IsisRouterHostName_Type()
)
isisRouterHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisRouterHostName.setStatus("current")
_IsisRouterID_Type = Unsigned32
_IsisRouterID_Object = MibTableColumn
isisRouterID = _IsisRouterID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 7, 1, 4),
    _IsisRouterID_Type()
)
isisRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisRouterID.setStatus("current")
_IsisRouterIPv6ID_Type = InetAddressIPv6
_IsisRouterIPv6ID_Object = MibTableColumn
isisRouterIPv6ID = _IsisRouterIPv6ID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 7, 1, 5),
    _IsisRouterIPv6ID_Type()
)
isisRouterIPv6ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisRouterIPv6ID.setStatus("current")
_IsisMtSysTable_Object = MibTable
isisMtSysTable = _IsisMtSysTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    isisMtSysTable.setStatus("current")
_IsisMtSysEntry_Object = MibTableRow
isisMtSysEntry = _IsisMtSysEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 8, 1)
)
isisMtSysEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisMtSysMtId"),
)
if mibBuilder.loadTexts:
    isisMtSysEntry.setStatus("current")


class _IsisMtSysMtId_Type(Integer32):
    """Custom type isisMtSysMtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IsisMtSysMtId_Type.__name__ = "Integer32"
_IsisMtSysMtId_Object = MibTableColumn
isisMtSysMtId = _IsisMtSysMtId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 8, 1, 2),
    _IsisMtSysMtId_Type()
)
isisMtSysMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisMtSysMtId.setStatus("current")
_IsisMtSysExistState_Type = RowStatus
_IsisMtSysExistState_Object = MibTableColumn
isisMtSysExistState = _IsisMtSysExistState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 8, 1, 3),
    _IsisMtSysExistState_Type()
)
isisMtSysExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisMtSysExistState.setStatus("current")


class _IsisMtSysAdminState_Type(AdminState):
    """Custom type isisMtSysAdminState based on AdminState"""


_IsisMtSysAdminState_Object = MibTableColumn
isisMtSysAdminState = _IsisMtSysAdminState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 8, 1, 4),
    _IsisMtSysAdminState_Type()
)
isisMtSysAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisMtSysAdminState.setStatus("current")
_IsisMtSysOperState_Type = IsisOperStatus
_IsisMtSysOperState_Object = MibTableColumn
isisMtSysOperState = _IsisMtSysOperState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 8, 1, 5),
    _IsisMtSysOperState_Type()
)
isisMtSysOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisMtSysOperState.setStatus("current")


class _IsisMtSysProtSupported_Type(IsisAddrTypeBits):
    """Custom type isisMtSysProtSupported based on IsisAddrTypeBits"""
    defaultBinValue = "01"


_IsisMtSysProtSupported_Object = MibTableColumn
isisMtSysProtSupported = _IsisMtSysProtSupported_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 8, 1, 6),
    _IsisMtSysProtSupported_Type()
)
isisMtSysProtSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisMtSysProtSupported.setStatus("current")


class _IsisMtSysDefaultActive_Type(TruthValue):
    """Custom type isisMtSysDefaultActive based on TruthValue"""


_IsisMtSysDefaultActive_Object = MibTableColumn
isisMtSysDefaultActive = _IsisMtSysDefaultActive_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 1, 8, 1, 7),
    _IsisMtSysDefaultActive_Type()
)
isisMtSysDefaultActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisMtSysDefaultActive.setStatus("current")
_IsisSysLevel_ObjectIdentity = ObjectIdentity
isisSysLevel = _IsisSysLevel_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2)
)
_IsisSysLevelTable_Object = MibTable
isisSysLevelTable = _IsisSysLevelTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    isisSysLevelTable.setStatus("current")
_IsisSysLevelEntry_Object = MibTableRow
isisSysLevelEntry = _IsisSysLevelEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1)
)
isisSysLevelEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisSysLevelIndex"),
)
if mibBuilder.loadTexts:
    isisSysLevelEntry.setStatus("current")


class _IsisSysLevelIndex_Type(Integer32):
    """Custom type isisSysLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2),
          ("none", 0))
    )


_IsisSysLevelIndex_Type.__name__ = "Integer32"
_IsisSysLevelIndex_Object = MibTableColumn
isisSysLevelIndex = _IsisSysLevelIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 1),
    _IsisSysLevelIndex_Type()
)
isisSysLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSysLevelIndex.setStatus("current")


class _IsisSysLevelOrigLSPBuffSize_Type(LSPBuffSize):
    """Custom type isisSysLevelOrigLSPBuffSize based on LSPBuffSize"""
    defaultValue = 1492


_IsisSysLevelOrigLSPBuffSize_Object = MibTableColumn
isisSysLevelOrigLSPBuffSize = _IsisSysLevelOrigLSPBuffSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 2),
    _IsisSysLevelOrigLSPBuffSize_Type()
)
isisSysLevelOrigLSPBuffSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLevelOrigLSPBuffSize.setStatus("current")


class _IsisSysLevelMinLSPGenInt_Type(Unsigned32):
    """Custom type isisSysLevelMinLSPGenInt based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535000),
    )


_IsisSysLevelMinLSPGenInt_Type.__name__ = "Unsigned32"
_IsisSysLevelMinLSPGenInt_Object = MibTableColumn
isisSysLevelMinLSPGenInt = _IsisSysLevelMinLSPGenInt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 3),
    _IsisSysLevelMinLSPGenInt_Type()
)
isisSysLevelMinLSPGenInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLevelMinLSPGenInt.setStatus("current")
if mibBuilder.loadTexts:
    isisSysLevelMinLSPGenInt.setUnits("milliseconds")


class _IsisSysLevelOverloadState_Type(LevelState):
    """Custom type isisSysLevelOverloadState based on LevelState"""


_IsisSysLevelOverloadState_Object = MibTableColumn
isisSysLevelOverloadState = _IsisSysLevelOverloadState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 4),
    _IsisSysLevelOverloadState_Type()
)
isisSysLevelOverloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysLevelOverloadState.setStatus("current")


class _IsisSysLevelSetOverload_Type(TruthValue):
    """Custom type isisSysLevelSetOverload based on TruthValue"""


_IsisSysLevelSetOverload_Object = MibTableColumn
isisSysLevelSetOverload = _IsisSysLevelSetOverload_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 5),
    _IsisSysLevelSetOverload_Type()
)
isisSysLevelSetOverload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLevelSetOverload.setStatus("current")


class _IsisSysLevelSetOverloadUntil_Type(TimeTicks):
    """Custom type isisSysLevelSetOverloadUntil based on TimeTicks"""
    defaultValue = 0


_IsisSysLevelSetOverloadUntil_Object = MibTableColumn
isisSysLevelSetOverloadUntil = _IsisSysLevelSetOverloadUntil_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 6),
    _IsisSysLevelSetOverloadUntil_Type()
)
isisSysLevelSetOverloadUntil.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLevelSetOverloadUntil.setStatus("current")
if mibBuilder.loadTexts:
    isisSysLevelSetOverloadUntil.setUnits("seconds")


class _IsisSysLevelMetricStyle_Type(MetricStyle):
    """Custom type isisSysLevelMetricStyle based on MetricStyle"""


_IsisSysLevelMetricStyle_Object = MibTableColumn
isisSysLevelMetricStyle = _IsisSysLevelMetricStyle_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 7),
    _IsisSysLevelMetricStyle_Type()
)
isisSysLevelMetricStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLevelMetricStyle.setStatus("current")


class _IsisSysLevelSPFConsiders_Type(MetricStyle):
    """Custom type isisSysLevelSPFConsiders based on MetricStyle"""


_IsisSysLevelSPFConsiders_Object = MibTableColumn
isisSysLevelSPFConsiders = _IsisSysLevelSPFConsiders_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 8),
    _IsisSysLevelSPFConsiders_Type()
)
isisSysLevelSPFConsiders.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLevelSPFConsiders.setStatus("current")


class _IsisSysLevelTEEnabled_Type(TruthValue):
    """Custom type isisSysLevelTEEnabled based on TruthValue"""


_IsisSysLevelTEEnabled_Object = MibTableColumn
isisSysLevelTEEnabled = _IsisSysLevelTEEnabled_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 9),
    _IsisSysLevelTEEnabled_Type()
)
isisSysLevelTEEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLevelTEEnabled.setStatus("current")


class _IsisSysLevelIPv6TEEnabled_Type(TruthValue):
    """Custom type isisSysLevelIPv6TEEnabled based on TruthValue"""


_IsisSysLevelIPv6TEEnabled_Object = MibTableColumn
isisSysLevelIPv6TEEnabled = _IsisSysLevelIPv6TEEnabled_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 10),
    _IsisSysLevelIPv6TEEnabled_Type()
)
isisSysLevelIPv6TEEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLevelIPv6TEEnabled.setStatus("current")


class _IsisSysLevelRestartT2Duration_Type(Integer32):
    """Custom type isisSysLevelRestartT2Duration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_IsisSysLevelRestartT2Duration_Type.__name__ = "Integer32"
_IsisSysLevelRestartT2Duration_Object = MibTableColumn
isisSysLevelRestartT2Duration = _IsisSysLevelRestartT2Duration_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 11),
    _IsisSysLevelRestartT2Duration_Type()
)
isisSysLevelRestartT2Duration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLevelRestartT2Duration.setStatus("current")
if mibBuilder.loadTexts:
    isisSysLevelRestartT2Duration.setUnits("seconds")
_IsisSysLevelAuthUser_Type = AuthUserDataString
_IsisSysLevelAuthUser_Object = MibTableColumn
isisSysLevelAuthUser = _IsisSysLevelAuthUser_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 2, 1, 1, 12),
    _IsisSysLevelAuthUser_Type()
)
isisSysLevelAuthUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSysLevelAuthUser.setStatus("current")
_IsisCirc_ObjectIdentity = ObjectIdentity
isisCirc = _IsisCirc_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3)
)
_IsisCircTable_Object = MibTable
isisCircTable = _IsisCircTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    isisCircTable.setStatus("current")
_IsisCircEntry_Object = MibTableRow
isisCircEntry = _IsisCircEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1)
)
isisCircEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
)
if mibBuilder.loadTexts:
    isisCircEntry.setStatus("current")


class _IsisCircIndex_Type(Integer32):
    """Custom type isisCircIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsisCircIndex_Type.__name__ = "Integer32"
_IsisCircIndex_Object = MibTableColumn
isisCircIndex = _IsisCircIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 1),
    _IsisCircIndex_Type()
)
isisCircIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisCircIndex.setStatus("current")
_IsisCircIfIndex_Type = InterfaceIndex
_IsisCircIfIndex_Object = MibTableColumn
isisCircIfIndex = _IsisCircIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 2),
    _IsisCircIfIndex_Type()
)
isisCircIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircIfIndex.setStatus("current")
_IsisCircIfSubIndex_Type = Integer32
_IsisCircIfSubIndex_Object = MibTableColumn
isisCircIfSubIndex = _IsisCircIfSubIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 3),
    _IsisCircIfSubIndex_Type()
)
isisCircIfSubIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircIfSubIndex.setStatus("current")


class _IsisCircAdminState_Type(AdminState):
    """Custom type isisCircAdminState based on AdminState"""


_IsisCircAdminState_Object = MibTableColumn
isisCircAdminState = _IsisCircAdminState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 4),
    _IsisCircAdminState_Type()
)
isisCircAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircAdminState.setStatus("current")
_IsisCircExistState_Type = RowStatus
_IsisCircExistState_Object = MibTableColumn
isisCircExistState = _IsisCircExistState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 5),
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
            *(0,
              1,
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
          ("staticOut", 4),
          ("unknown", 0))
    )


_IsisCircType_Type.__name__ = "Integer32"
_IsisCircType_Object = MibTableColumn
isisCircType = _IsisCircType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 6),
    _IsisCircType_Type()
)
isisCircType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircType.setStatus("current")


class _IsisCircExtDomain_Type(TruthValue):
    """Custom type isisCircExtDomain based on TruthValue"""


_IsisCircExtDomain_Object = MibTableColumn
isisCircExtDomain = _IsisCircExtDomain_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 7),
    _IsisCircExtDomain_Type()
)
isisCircExtDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircExtDomain.setStatus("current")


class _IsisCircLevel_Type(Integer32):
    """Custom type isisCircLevel based on Integer32"""
    defaultValue = 3

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
        *(("level1", 1),
          ("level1L2", 3),
          ("level2", 2),
          ("reserved", 0))
    )


_IsisCircLevel_Type.__name__ = "Integer32"
_IsisCircLevel_Object = MibTableColumn
isisCircLevel = _IsisCircLevel_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 8),
    _IsisCircLevel_Type()
)
isisCircLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevel.setStatus("current")


class _IsisCircPassiveCircuit_Type(TruthValue):
    """Custom type isisCircPassiveCircuit based on TruthValue"""


_IsisCircPassiveCircuit_Object = MibTableColumn
isisCircPassiveCircuit = _IsisCircPassiveCircuit_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 9),
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
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 10),
    _IsisCircMeshGroupEnabled_Type()
)
isisCircMeshGroupEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircMeshGroupEnabled.setStatus("current")
_IsisCircMeshGroup_Type = Unsigned32
_IsisCircMeshGroup_Object = MibTableColumn
isisCircMeshGroup = _IsisCircMeshGroup_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 11),
    _IsisCircMeshGroup_Type()
)
isisCircMeshGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircMeshGroup.setStatus("current")


class _IsisCircSmallHellos_Type(TruthValue):
    """Custom type isisCircSmallHellos based on TruthValue"""


_IsisCircSmallHellos_Object = MibTableColumn
isisCircSmallHellos = _IsisCircSmallHellos_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 12),
    _IsisCircSmallHellos_Type()
)
isisCircSmallHellos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircSmallHellos.setStatus("current")
_IsisCircLastUpTime_Type = TimeTicks
_IsisCircLastUpTime_Object = MibTableColumn
isisCircLastUpTime = _IsisCircLastUpTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 13),
    _IsisCircLastUpTime_Type()
)
isisCircLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLastUpTime.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLastUpTime.setUnits("seconds")
_IsisCirc3WayEnabled_Type = TruthValue
_IsisCirc3WayEnabled_Object = MibTableColumn
isisCirc3WayEnabled = _IsisCirc3WayEnabled_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 14),
    _IsisCirc3WayEnabled_Type()
)
isisCirc3WayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCirc3WayEnabled.setStatus("current")
_IsisCircExtendedCircID_Type = Unsigned32
_IsisCircExtendedCircID_Object = MibTableColumn
isisCircExtendedCircID = _IsisCircExtendedCircID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 15),
    _IsisCircExtendedCircID_Type()
)
isisCircExtendedCircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircExtendedCircID.setStatus("current")


class _IsisCircOperState_Type(IsisOperStatus):
    """Custom type isisCircOperState based on IsisOperStatus"""


_IsisCircOperState_Object = MibTableColumn
isisCircOperState = _IsisCircOperState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 16),
    _IsisCircOperState_Type()
)
isisCircOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircOperState.setStatus("current")


class _IsisCircSdEntityIndex_Type(Integer32):
    """Custom type isisCircSdEntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IsisCircSdEntityIndex_Type.__name__ = "Integer32"
_IsisCircSdEntityIndex_Object = MibTableColumn
isisCircSdEntityIndex = _IsisCircSdEntityIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 17),
    _IsisCircSdEntityIndex_Type()
)
isisCircSdEntityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircSdEntityIndex.setStatus("current")


class _IsisCircDlBuffPoolSize_Type(Unsigned32):
    """Custom type isisCircDlBuffPoolSize based on Unsigned32"""
    defaultValue = 150


_IsisCircDlBuffPoolSize_Object = MibTableColumn
isisCircDlBuffPoolSize = _IsisCircDlBuffPoolSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 18),
    _IsisCircDlBuffPoolSize_Type()
)
isisCircDlBuffPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircDlBuffPoolSize.setStatus("current")


class _IsisCircSdPDUBuffPoolSize_Type(Unsigned32):
    """Custom type isisCircSdPDUBuffPoolSize based on Unsigned32"""
    defaultValue = 200


_IsisCircSdPDUBuffPoolSize_Object = MibTableColumn
isisCircSdPDUBuffPoolSize = _IsisCircSdPDUBuffPoolSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 19),
    _IsisCircSdPDUBuffPoolSize_Type()
)
isisCircSdPDUBuffPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircSdPDUBuffPoolSize.setStatus("current")


class _IsisCircSdIndBuffPoolSize_Type(Unsigned32):
    """Custom type isisCircSdIndBuffPoolSize based on Unsigned32"""
    defaultValue = 20


_IsisCircSdIndBuffPoolSize_Object = MibTableColumn
isisCircSdIndBuffPoolSize = _IsisCircSdIndBuffPoolSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 20),
    _IsisCircSdIndBuffPoolSize_Type()
)
isisCircSdIndBuffPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircSdIndBuffPoolSize.setStatus("current")


class _IsisCircDataLinkBlockSize_Type(Unsigned32):
    """Custom type isisCircDataLinkBlockSize based on Unsigned32"""
    defaultValue = 1492


_IsisCircDataLinkBlockSize_Object = MibTableColumn
isisCircDataLinkBlockSize = _IsisCircDataLinkBlockSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 21),
    _IsisCircDataLinkBlockSize_Type()
)
isisCircDataLinkBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircDataLinkBlockSize.setStatus("current")


class _IsisCircPhysicalAddress_Type(OctetString):
    """Custom type isisCircPhysicalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IsisCircPhysicalAddress_Type.__name__ = "OctetString"
_IsisCircPhysicalAddress_Object = MibTableColumn
isisCircPhysicalAddress = _IsisCircPhysicalAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 22),
    _IsisCircPhysicalAddress_Type()
)
isisCircPhysicalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircPhysicalAddress.setStatus("current")


class _IsisCircManualOrAutomatic_Type(Integer32):
    """Custom type isisCircManualOrAutomatic based on Integer32"""
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
        *(("automatic", 2),
          ("both", 3),
          ("manual", 1))
    )


_IsisCircManualOrAutomatic_Type.__name__ = "Integer32"
_IsisCircManualOrAutomatic_Object = MibTableColumn
isisCircManualOrAutomatic = _IsisCircManualOrAutomatic_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 23),
    _IsisCircManualOrAutomatic_Type()
)
isisCircManualOrAutomatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircManualOrAutomatic.setStatus("current")
_IsisCircT1TimerRunning_Type = TruthValue
_IsisCircT1TimerRunning_Object = MibTableColumn
isisCircT1TimerRunning = _IsisCircT1TimerRunning_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 24),
    _IsisCircT1TimerRunning_Type()
)
isisCircT1TimerRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircT1TimerRunning.setStatus("current")


class _IsisCircProtSupported_Type(IsisAddrTypeBits):
    """Custom type isisCircProtSupported based on IsisAddrTypeBits"""
    defaultBinValue = "01"


_IsisCircProtSupported_Object = MibTableColumn
isisCircProtSupported = _IsisCircProtSupported_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 25),
    _IsisCircProtSupported_Type()
)
isisCircProtSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircProtSupported.setStatus("current")


class _IsisCircPtToPtOverLAN_Type(TruthValue):
    """Custom type isisCircPtToPtOverLAN based on TruthValue"""


_IsisCircPtToPtOverLAN_Object = MibTableColumn
isisCircPtToPtOverLAN = _IsisCircPtToPtOverLAN_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 26),
    _IsisCircPtToPtOverLAN_Type()
)
isisCircPtToPtOverLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircPtToPtOverLAN.setStatus("current")


class _IsisCircProtBfdDesired_Type(IsisAddrTypeBits):
    """Custom type isisCircProtBfdDesired based on IsisAddrTypeBits"""
    defaultBinValue = "0"


_IsisCircProtBfdDesired_Object = MibTableColumn
isisCircProtBfdDesired = _IsisCircProtBfdDesired_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 2, 1, 28),
    _IsisCircProtBfdDesired_Type()
)
isisCircProtBfdDesired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircProtBfdDesired.setStatus("current")
_IsisCircIPAddrTable_Object = MibTable
isisCircIPAddrTable = _IsisCircIPAddrTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    isisCircIPAddrTable.setStatus("current")
_IsisCircIPAddrEntry_Object = MibTableRow
isisCircIPAddrEntry = _IsisCircIPAddrEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 3, 1)
)
isisCircIPAddrEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisCircIPAddrManOrAuto"),
    (0, "DC-ISIS-MIB", "isisCircIPAddrIndex"),
)
if mibBuilder.loadTexts:
    isisCircIPAddrEntry.setStatus("current")


class _IsisCircIPAddrManOrAuto_Type(Integer32):
    """Custom type isisCircIPAddrManOrAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("both", 3),
          ("manual", 1))
    )


_IsisCircIPAddrManOrAuto_Type.__name__ = "Integer32"
_IsisCircIPAddrManOrAuto_Object = MibTableColumn
isisCircIPAddrManOrAuto = _IsisCircIPAddrManOrAuto_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 3, 1, 1),
    _IsisCircIPAddrManOrAuto_Type()
)
isisCircIPAddrManOrAuto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisCircIPAddrManOrAuto.setStatus("current")


class _IsisCircIPAddrIndex_Type(Integer32):
    """Custom type isisCircIPAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisCircIPAddrIndex_Type.__name__ = "Integer32"
_IsisCircIPAddrIndex_Object = MibTableColumn
isisCircIPAddrIndex = _IsisCircIPAddrIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 3, 1, 2),
    _IsisCircIPAddrIndex_Type()
)
isisCircIPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisCircIPAddrIndex.setStatus("current")
_IsisCircIPAddrRowStatus_Type = RowStatus
_IsisCircIPAddrRowStatus_Object = MibTableColumn
isisCircIPAddrRowStatus = _IsisCircIPAddrRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 3, 1, 3),
    _IsisCircIPAddrRowStatus_Type()
)
isisCircIPAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircIPAddrRowStatus.setStatus("current")


class _IsisCircIPAddrAdminState_Type(AdminState):
    """Custom type isisCircIPAddrAdminState based on AdminState"""


_IsisCircIPAddrAdminState_Object = MibTableColumn
isisCircIPAddrAdminState = _IsisCircIPAddrAdminState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 3, 1, 4),
    _IsisCircIPAddrAdminState_Type()
)
isisCircIPAddrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircIPAddrAdminState.setStatus("current")


class _IsisCircIPAddrAddressType_Type(InetAddressType):
    """Custom type isisCircIPAddrAddressType based on InetAddressType"""


_IsisCircIPAddrAddressType_Object = MibTableColumn
isisCircIPAddrAddressType = _IsisCircIPAddrAddressType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 3, 1, 5),
    _IsisCircIPAddrAddressType_Type()
)
isisCircIPAddrAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircIPAddrAddressType.setStatus("current")


class _IsisCircIPAddrAddress_Type(InetAddress):
    """Custom type isisCircIPAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IsisCircIPAddrAddress_Type.__name__ = "InetAddress"
_IsisCircIPAddrAddress_Object = MibTableColumn
isisCircIPAddrAddress = _IsisCircIPAddrAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 3, 1, 6),
    _IsisCircIPAddrAddress_Type()
)
isisCircIPAddrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircIPAddrAddress.setStatus("current")


class _IsisCircIPAddrInLSP_Type(TruthValue):
    """Custom type isisCircIPAddrInLSP based on TruthValue"""


_IsisCircIPAddrInLSP_Object = MibTableColumn
isisCircIPAddrInLSP = _IsisCircIPAddrInLSP_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 3, 1, 7),
    _IsisCircIPAddrInLSP_Type()
)
isisCircIPAddrInLSP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircIPAddrInLSP.setStatus("current")
_IsisMtCircManConfigTable_Object = MibTable
isisMtCircManConfigTable = _IsisMtCircManConfigTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    isisMtCircManConfigTable.setStatus("current")
_IsisMtCircManConfigEntry_Object = MibTableRow
isisMtCircManConfigEntry = _IsisMtCircManConfigEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 4, 1)
)
isisMtCircManConfigEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisMtCircManMtId"),
)
if mibBuilder.loadTexts:
    isisMtCircManConfigEntry.setStatus("current")


class _IsisMtCircManMtId_Type(Integer32):
    """Custom type isisMtCircManMtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IsisMtCircManMtId_Type.__name__ = "Integer32"
_IsisMtCircManMtId_Object = MibTableColumn
isisMtCircManMtId = _IsisMtCircManMtId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 4, 1, 3),
    _IsisMtCircManMtId_Type()
)
isisMtCircManMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisMtCircManMtId.setStatus("current")
_IsisMtCircManExistState_Type = RowStatus
_IsisMtCircManExistState_Object = MibTableColumn
isisMtCircManExistState = _IsisMtCircManExistState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 4, 1, 4),
    _IsisMtCircManExistState_Type()
)
isisMtCircManExistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisMtCircManExistState.setStatus("current")


class _IsisMtCircManAdminState_Type(AdminState):
    """Custom type isisMtCircManAdminState based on AdminState"""


_IsisMtCircManAdminState_Object = MibTableColumn
isisMtCircManAdminState = _IsisMtCircManAdminState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 4, 1, 5),
    _IsisMtCircManAdminState_Type()
)
isisMtCircManAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisMtCircManAdminState.setStatus("current")
_IsisMtCircManOperState_Type = IsisOperStatus
_IsisMtCircManOperState_Object = MibTableColumn
isisMtCircManOperState = _IsisMtCircManOperState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 4, 1, 6),
    _IsisMtCircManOperState_Type()
)
isisMtCircManOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisMtCircManOperState.setStatus("current")


class _IsisMtCircManL1WideMetric_Type(WideMetric):
    """Custom type isisMtCircManL1WideMetric based on WideMetric"""
    defaultValue = 10


_IsisMtCircManL1WideMetric_Object = MibTableColumn
isisMtCircManL1WideMetric = _IsisMtCircManL1WideMetric_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 4, 1, 7),
    _IsisMtCircManL1WideMetric_Type()
)
isisMtCircManL1WideMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisMtCircManL1WideMetric.setStatus("current")


class _IsisMtCircManL2WideMetric_Type(WideMetric):
    """Custom type isisMtCircManL2WideMetric based on WideMetric"""
    defaultValue = 10


_IsisMtCircManL2WideMetric_Object = MibTableColumn
isisMtCircManL2WideMetric = _IsisMtCircManL2WideMetric_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 4, 1, 8),
    _IsisMtCircManL2WideMetric_Type()
)
isisMtCircManL2WideMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisMtCircManL2WideMetric.setStatus("current")
_IsisMtCircStatusTable_Object = MibTable
isisMtCircStatusTable = _IsisMtCircStatusTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    isisMtCircStatusTable.setStatus("current")
_IsisMtCircStatusEntry_Object = MibTableRow
isisMtCircStatusEntry = _IsisMtCircStatusEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 5, 1)
)
isisMtCircStatusEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisMtCircStatusMtId"),
)
if mibBuilder.loadTexts:
    isisMtCircStatusEntry.setStatus("current")


class _IsisMtCircStatusMtId_Type(Integer32):
    """Custom type isisMtCircStatusMtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IsisMtCircStatusMtId_Type.__name__ = "Integer32"
_IsisMtCircStatusMtId_Object = MibTableColumn
isisMtCircStatusMtId = _IsisMtCircStatusMtId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 5, 1, 3),
    _IsisMtCircStatusMtId_Type()
)
isisMtCircStatusMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisMtCircStatusMtId.setStatus("current")
_IsisMtCircStatusOperState_Type = IsisOperStatus
_IsisMtCircStatusOperState_Object = MibTableColumn
isisMtCircStatusOperState = _IsisMtCircStatusOperState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 5, 1, 4),
    _IsisMtCircStatusOperState_Type()
)
isisMtCircStatusOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisMtCircStatusOperState.setStatus("current")
_IsisMtCircStatusL1WideMetric_Type = WideMetric
_IsisMtCircStatusL1WideMetric_Object = MibTableColumn
isisMtCircStatusL1WideMetric = _IsisMtCircStatusL1WideMetric_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 5, 1, 5),
    _IsisMtCircStatusL1WideMetric_Type()
)
isisMtCircStatusL1WideMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisMtCircStatusL1WideMetric.setStatus("current")
_IsisMtCircStatusL2WideMetric_Type = WideMetric
_IsisMtCircStatusL2WideMetric_Object = MibTableColumn
isisMtCircStatusL2WideMetric = _IsisMtCircStatusL2WideMetric_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 3, 5, 1, 6),
    _IsisMtCircStatusL2WideMetric_Type()
)
isisMtCircStatusL2WideMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisMtCircStatusL2WideMetric.setStatus("current")
_IsisCircLevelValues_ObjectIdentity = ObjectIdentity
isisCircLevelValues = _IsisCircLevelValues_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4)
)
_IsisCircLevelTable_Object = MibTable
isisCircLevelTable = _IsisCircLevelTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    isisCircLevelTable.setStatus("current")
_IsisCircLevelEntry_Object = MibTableRow
isisCircLevelEntry = _IsisCircLevelEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1)
)
isisCircLevelEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisCircLevelIndex"),
)
if mibBuilder.loadTexts:
    isisCircLevelEntry.setStatus("current")


class _IsisCircLevelIndex_Type(Integer32):
    """Custom type isisCircLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2),
          ("none", 0))
    )


_IsisCircLevelIndex_Type.__name__ = "Integer32"
_IsisCircLevelIndex_Object = MibTableColumn
isisCircLevelIndex = _IsisCircLevelIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 1),
    _IsisCircLevelIndex_Type()
)
isisCircLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisCircLevelIndex.setStatus("current")


class _IsisCircLevelMetric_Type(Integer32):
    """Custom type isisCircLevelMetric based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_IsisCircLevelMetric_Type.__name__ = "Integer32"
_IsisCircLevelMetric_Object = MibTableColumn
isisCircLevelMetric = _IsisCircLevelMetric_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 2),
    _IsisCircLevelMetric_Type()
)
isisCircLevelMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelMetric.setStatus("current")


class _IsisCircLevelWideMetric_Type(WideMetric):
    """Custom type isisCircLevelWideMetric based on WideMetric"""
    defaultValue = 10


_IsisCircLevelWideMetric_Object = MibTableColumn
isisCircLevelWideMetric = _IsisCircLevelWideMetric_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 3),
    _IsisCircLevelWideMetric_Type()
)
isisCircLevelWideMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelWideMetric.setStatus("current")


class _IsisCircLevelISPriority_Type(ISPriority):
    """Custom type isisCircLevelISPriority based on ISPriority"""
    defaultValue = 64


_IsisCircLevelISPriority_Object = MibTableColumn
isisCircLevelISPriority = _IsisCircLevelISPriority_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 4),
    _IsisCircLevelISPriority_Type()
)
isisCircLevelISPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelISPriority.setStatus("current")


class _IsisCircLevelIDOctet_Type(Integer32):
    """Custom type isisCircLevelIDOctet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsisCircLevelIDOctet_Type.__name__ = "Integer32"
_IsisCircLevelIDOctet_Object = MibTableColumn
isisCircLevelIDOctet = _IsisCircLevelIDOctet_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 5),
    _IsisCircLevelIDOctet_Type()
)
isisCircLevelIDOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLevelIDOctet.setStatus("current")
_IsisCircLevelID_Type = CircuitID
_IsisCircLevelID_Object = MibTableColumn
isisCircLevelID = _IsisCircLevelID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 6),
    _IsisCircLevelID_Type()
)
isisCircLevelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLevelID.setStatus("current")
_IsisCircLevelDesIS_Type = CircuitID
_IsisCircLevelDesIS_Object = MibTableColumn
isisCircLevelDesIS = _IsisCircLevelDesIS_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 7),
    _IsisCircLevelDesIS_Type()
)
isisCircLevelDesIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLevelDesIS.setStatus("current")


class _IsisCircLevelHelloMultiplier_Type(Integer32):
    """Custom type isisCircLevelHelloMultiplier based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_IsisCircLevelHelloMultiplier_Type.__name__ = "Integer32"
_IsisCircLevelHelloMultiplier_Object = MibTableColumn
isisCircLevelHelloMultiplier = _IsisCircLevelHelloMultiplier_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 8),
    _IsisCircLevelHelloMultiplier_Type()
)
isisCircLevelHelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelHelloMultiplier.setStatus("current")


class _IsisCircLevelHelloTimer_Type(Integer32):
    """Custom type isisCircLevelHelloTimer based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600000),
    )


_IsisCircLevelHelloTimer_Type.__name__ = "Integer32"
_IsisCircLevelHelloTimer_Object = MibTableColumn
isisCircLevelHelloTimer = _IsisCircLevelHelloTimer_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 9),
    _IsisCircLevelHelloTimer_Type()
)
isisCircLevelHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelHelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelHelloTimer.setUnits("milliseconds")


class _IsisCircLevelDRHelloTimer_Type(Integer32):
    """Custom type isisCircLevelDRHelloTimer based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120000),
    )


_IsisCircLevelDRHelloTimer_Type.__name__ = "Integer32"
_IsisCircLevelDRHelloTimer_Object = MibTableColumn
isisCircLevelDRHelloTimer = _IsisCircLevelDRHelloTimer_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 10),
    _IsisCircLevelDRHelloTimer_Type()
)
isisCircLevelDRHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelDRHelloTimer.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelDRHelloTimer.setUnits("milliseconds")


class _IsisCircLevelLSPThrottle_Type(Unsigned16TC):
    """Custom type isisCircLevelLSPThrottle based on Unsigned16TC"""
    defaultValue = 30

    subtypeSpec = Unsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisCircLevelLSPThrottle_Type.__name__ = "Unsigned16TC"
_IsisCircLevelLSPThrottle_Object = MibTableColumn
isisCircLevelLSPThrottle = _IsisCircLevelLSPThrottle_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 11),
    _IsisCircLevelLSPThrottle_Type()
)
isisCircLevelLSPThrottle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelLSPThrottle.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelLSPThrottle.setUnits("milliseconds")


class _IsisCircLevelMinLSPRetransInt_Type(Integer32):
    """Custom type isisCircLevelMinLSPRetransInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300000),
    )


_IsisCircLevelMinLSPRetransInt_Type.__name__ = "Integer32"
_IsisCircLevelMinLSPRetransInt_Object = MibTableColumn
isisCircLevelMinLSPRetransInt = _IsisCircLevelMinLSPRetransInt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 12),
    _IsisCircLevelMinLSPRetransInt_Type()
)
isisCircLevelMinLSPRetransInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelMinLSPRetransInt.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelMinLSPRetransInt.setUnits("milliseconds")


class _IsisCircLevelCSNPInterval_Type(Integer32):
    """Custom type isisCircLevelCSNPInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_IsisCircLevelCSNPInterval_Type.__name__ = "Integer32"
_IsisCircLevelCSNPInterval_Object = MibTableColumn
isisCircLevelCSNPInterval = _IsisCircLevelCSNPInterval_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 13),
    _IsisCircLevelCSNPInterval_Type()
)
isisCircLevelCSNPInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelCSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelCSNPInterval.setUnits("seconds")


class _IsisCircLevelPartSNPInterval_Type(Integer32):
    """Custom type isisCircLevelPartSNPInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_IsisCircLevelPartSNPInterval_Type.__name__ = "Integer32"
_IsisCircLevelPartSNPInterval_Object = MibTableColumn
isisCircLevelPartSNPInterval = _IsisCircLevelPartSNPInterval_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 14),
    _IsisCircLevelPartSNPInterval_Type()
)
isisCircLevelPartSNPInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelPartSNPInterval.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelPartSNPInterval.setUnits("seconds")


class _IsisCircLevelStickyDIS_Type(Integer32):
    """Custom type isisCircLevelStickyDIS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_IsisCircLevelStickyDIS_Type.__name__ = "Integer32"
_IsisCircLevelStickyDIS_Object = MibTableColumn
isisCircLevelStickyDIS = _IsisCircLevelStickyDIS_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 15),
    _IsisCircLevelStickyDIS_Type()
)
isisCircLevelStickyDIS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelStickyDIS.setStatus("current")
_IsisCircLevelAuthUser_Type = AuthUserDataString
_IsisCircLevelAuthUser_Object = MibTableColumn
isisCircLevelAuthUser = _IsisCircLevelAuthUser_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 16),
    _IsisCircLevelAuthUser_Type()
)
isisCircLevelAuthUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelAuthUser.setStatus("current")
_IsisCircLevelIDHostname_Type = SnmpAdminString
_IsisCircLevelIDHostname_Object = MibTableColumn
isisCircLevelIDHostname = _IsisCircLevelIDHostname_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 17),
    _IsisCircLevelIDHostname_Type()
)
isisCircLevelIDHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLevelIDHostname.setStatus("current")
_IsisCircLevelDesISHostname_Type = SnmpAdminString
_IsisCircLevelDesISHostname_Object = MibTableColumn
isisCircLevelDesISHostname = _IsisCircLevelDesISHostname_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 18),
    _IsisCircLevelDesISHostname_Type()
)
isisCircLevelDesISHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLevelDesISHostname.setStatus("current")


class _IsisCircLevelMinLSPArrivalInt_Type(Integer32):
    """Custom type isisCircLevelMinLSPArrivalInt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_IsisCircLevelMinLSPArrivalInt_Type.__name__ = "Integer32"
_IsisCircLevelMinLSPArrivalInt_Object = MibTableColumn
isisCircLevelMinLSPArrivalInt = _IsisCircLevelMinLSPArrivalInt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 4, 1, 1, 19),
    _IsisCircLevelMinLSPArrivalInt_Type()
)
isisCircLevelMinLSPArrivalInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisCircLevelMinLSPArrivalInt.setStatus("current")
if mibBuilder.loadTexts:
    isisCircLevelMinLSPArrivalInt.setUnits("milliseconds")
_IsisCounters_ObjectIdentity = ObjectIdentity
isisCounters = _IsisCounters_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5)
)
_IsisSystemCounterTable_Object = MibTable
isisSystemCounterTable = _IsisSystemCounterTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    isisSystemCounterTable.setStatus("current")
_IsisSystemCounterEntry_Object = MibTableRow
isisSystemCounterEntry = _IsisSystemCounterEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1)
)
isisSystemCounterEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisSysStatLevel"),
)
if mibBuilder.loadTexts:
    isisSystemCounterEntry.setStatus("current")


class _IsisSysStatLevel_Type(Integer32):
    """Custom type isisSysStatLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2),
          ("none", 0))
    )


_IsisSysStatLevel_Type.__name__ = "Integer32"
_IsisSysStatLevel_Object = MibTableColumn
isisSysStatLevel = _IsisSysStatLevel_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 1),
    _IsisSysStatLevel_Type()
)
isisSysStatLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSysStatLevel.setStatus("current")
_IsisSysStatCorrLSPs_Type = Counter32
_IsisSysStatCorrLSPs_Object = MibTableColumn
isisSysStatCorrLSPs = _IsisSysStatCorrLSPs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 2),
    _IsisSysStatCorrLSPs_Type()
)
isisSysStatCorrLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatCorrLSPs.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatCorrLSPs.setUnits("frames")
_IsisSysStatAuthTypeFails_Type = Counter32
_IsisSysStatAuthTypeFails_Object = MibTableColumn
isisSysStatAuthTypeFails = _IsisSysStatAuthTypeFails_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 3),
    _IsisSysStatAuthTypeFails_Type()
)
isisSysStatAuthTypeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatAuthTypeFails.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatAuthTypeFails.setUnits("frames")
_IsisSysStatAuthFails_Type = Counter32
_IsisSysStatAuthFails_Object = MibTableColumn
isisSysStatAuthFails = _IsisSysStatAuthFails_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 4),
    _IsisSysStatAuthFails_Type()
)
isisSysStatAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatAuthFails.setUnits("frames")
_IsisSysStatLSPDbaseOloads_Type = Counter32
_IsisSysStatLSPDbaseOloads_Object = MibTableColumn
isisSysStatLSPDbaseOloads = _IsisSysStatLSPDbaseOloads_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 5),
    _IsisSysStatLSPDbaseOloads_Type()
)
isisSysStatLSPDbaseOloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatLSPDbaseOloads.setStatus("current")
_IsisSysStatManAddrDropFromAreas_Type = Counter32
_IsisSysStatManAddrDropFromAreas_Object = MibTableColumn
isisSysStatManAddrDropFromAreas = _IsisSysStatManAddrDropFromAreas_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 6),
    _IsisSysStatManAddrDropFromAreas_Type()
)
isisSysStatManAddrDropFromAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatManAddrDropFromAreas.setStatus("current")
_IsisSysStatAttmptToExMaxSeqNums_Type = Counter32
_IsisSysStatAttmptToExMaxSeqNums_Object = MibTableColumn
isisSysStatAttmptToExMaxSeqNums = _IsisSysStatAttmptToExMaxSeqNums_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 7),
    _IsisSysStatAttmptToExMaxSeqNums_Type()
)
isisSysStatAttmptToExMaxSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatAttmptToExMaxSeqNums.setStatus("current")
_IsisSysStatSeqNumSkips_Type = Counter32
_IsisSysStatSeqNumSkips_Object = MibTableColumn
isisSysStatSeqNumSkips = _IsisSysStatSeqNumSkips_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 8),
    _IsisSysStatSeqNumSkips_Type()
)
isisSysStatSeqNumSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatSeqNumSkips.setStatus("current")
_IsisSysStatOwnLSPPurges_Type = Counter32
_IsisSysStatOwnLSPPurges_Object = MibTableColumn
isisSysStatOwnLSPPurges = _IsisSysStatOwnLSPPurges_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 9),
    _IsisSysStatOwnLSPPurges_Type()
)
isisSysStatOwnLSPPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatOwnLSPPurges.setStatus("current")
_IsisSysStatIDFieldLenMismatches_Type = Counter32
_IsisSysStatIDFieldLenMismatches_Object = MibTableColumn
isisSysStatIDFieldLenMismatches = _IsisSysStatIDFieldLenMismatches_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 10),
    _IsisSysStatIDFieldLenMismatches_Type()
)
isisSysStatIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatIDFieldLenMismatches.setStatus("current")
if mibBuilder.loadTexts:
    isisSysStatIDFieldLenMismatches.setUnits("frames")
_IsisSysStatPartChanges_Type = Counter32
_IsisSysStatPartChanges_Object = MibTableColumn
isisSysStatPartChanges = _IsisSysStatPartChanges_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 11),
    _IsisSysStatPartChanges_Type()
)
isisSysStatPartChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatPartChanges.setStatus("current")
_IsisSysStatSPFRuns_Type = Counter32
_IsisSysStatSPFRuns_Object = MibTableColumn
isisSysStatSPFRuns = _IsisSysStatSPFRuns_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 12),
    _IsisSysStatSPFRuns_Type()
)
isisSysStatSPFRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatSPFRuns.setStatus("current")
_IsisSysStatLSPError_Type = Counter32
_IsisSysStatLSPError_Object = MibTableColumn
isisSysStatLSPError = _IsisSysStatLSPError_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 13),
    _IsisSysStatLSPError_Type()
)
isisSysStatLSPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatLSPError.setStatus("current")
_IsisSysStatCSNPError_Type = Counter32
_IsisSysStatCSNPError_Object = MibTableColumn
isisSysStatCSNPError = _IsisSysStatCSNPError_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 14),
    _IsisSysStatCSNPError_Type()
)
isisSysStatCSNPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatCSNPError.setStatus("current")
_IsisSysStatPSNPError_Type = Counter32
_IsisSysStatPSNPError_Object = MibTableColumn
isisSysStatPSNPError = _IsisSysStatPSNPError_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 15),
    _IsisSysStatPSNPError_Type()
)
isisSysStatPSNPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatPSNPError.setStatus("current")
_IsisSysStatLSPQueueLen_Type = Counter32
_IsisSysStatLSPQueueLen_Object = MibTableColumn
isisSysStatLSPQueueLen = _IsisSysStatLSPQueueLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 16),
    _IsisSysStatLSPQueueLen_Type()
)
isisSysStatLSPQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatLSPQueueLen.setStatus("current")
_IsisSysStatFragsRebuilt_Type = Counter32
_IsisSysStatFragsRebuilt_Object = MibTableColumn
isisSysStatFragsRebuilt = _IsisSysStatFragsRebuilt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 17),
    _IsisSysStatFragsRebuilt_Type()
)
isisSysStatFragsRebuilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatFragsRebuilt.setStatus("current")
_IsisSysStatLSPRexmits_Type = Counter32
_IsisSysStatLSPRexmits_Object = MibTableColumn
isisSysStatLSPRexmits = _IsisSysStatLSPRexmits_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 18),
    _IsisSysStatLSPRexmits_Type()
)
isisSysStatLSPRexmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatLSPRexmits.setStatus("current")
_IsisSysStatLSPRegens_Type = Counter32
_IsisSysStatLSPRegens_Object = MibTableColumn
isisSysStatLSPRegens = _IsisSysStatLSPRegens_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 19),
    _IsisSysStatLSPRegens_Type()
)
isisSysStatLSPRegens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatLSPRegens.setStatus("current")
_IsisSysStatPurgesInitiated_Type = Counter32
_IsisSysStatPurgesInitiated_Object = MibTableColumn
isisSysStatPurgesInitiated = _IsisSysStatPurgesInitiated_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 20),
    _IsisSysStatPurgesInitiated_Type()
)
isisSysStatPurgesInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatPurgesInitiated.setStatus("current")
_IsisSysStatLSPCount_Type = Counter32
_IsisSysStatLSPCount_Object = MibTableColumn
isisSysStatLSPCount = _IsisSysStatLSPCount_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 21),
    _IsisSysStatLSPCount_Type()
)
isisSysStatLSPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatLSPCount.setStatus("current")
_IsisSysStatPurgesIniLocal_Type = Counter32
_IsisSysStatPurgesIniLocal_Object = MibTableColumn
isisSysStatPurgesIniLocal = _IsisSysStatPurgesIniLocal_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 23),
    _IsisSysStatPurgesIniLocal_Type()
)
isisSysStatPurgesIniLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatPurgesIniLocal.setStatus("current")
_IsisSysStatPurgesIniRemote_Type = Counter32
_IsisSysStatPurgesIniRemote_Object = MibTableColumn
isisSysStatPurgesIniRemote = _IsisSysStatPurgesIniRemote_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 24),
    _IsisSysStatPurgesIniRemote_Type()
)
isisSysStatPurgesIniRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatPurgesIniRemote.setStatus("current")
_IsisSysStatPurgesIniRemSNP_Type = Counter32
_IsisSysStatPurgesIniRemSNP_Object = MibTableColumn
isisSysStatPurgesIniRemSNP = _IsisSysStatPurgesIniRemSNP_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 25),
    _IsisSysStatPurgesIniRemSNP_Type()
)
isisSysStatPurgesIniRemSNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatPurgesIniRemSNP.setStatus("current")
_IsisSysStatPurgesIniRemExp_Type = Counter32
_IsisSysStatPurgesIniRemExp_Object = MibTableColumn
isisSysStatPurgesIniRemExp = _IsisSysStatPurgesIniRemExp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 26),
    _IsisSysStatPurgesIniRemExp_Type()
)
isisSysStatPurgesIniRemExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatPurgesIniRemExp.setStatus("current")
_IsisSysStatPurgesIniRemPrs_Type = Counter32
_IsisSysStatPurgesIniRemPrs_Object = MibTableColumn
isisSysStatPurgesIniRemPrs = _IsisSysStatPurgesIniRemPrs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 1, 1, 27),
    _IsisSysStatPurgesIniRemPrs_Type()
)
isisSysStatPurgesIniRemPrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSysStatPurgesIniRemPrs.setStatus("current")
_IsisCircuitCounterTable_Object = MibTable
isisCircuitCounterTable = _IsisCircuitCounterTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    isisCircuitCounterTable.setStatus("current")
_IsisCircuitCounterEntry_Object = MibTableRow
isisCircuitCounterEntry = _IsisCircuitCounterEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1)
)
isisCircuitCounterEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisCircuitType"),
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
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1, 1),
    _IsisCircuitType_Type()
)
isisCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisCircuitType.setStatus("current")
_IsisCircAdjChanges_Type = Counter32
_IsisCircAdjChanges_Object = MibTableColumn
isisCircAdjChanges = _IsisCircAdjChanges_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1, 2),
    _IsisCircAdjChanges_Type()
)
isisCircAdjChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircAdjChanges.setStatus("current")
_IsisCircNumAdj_Type = Unsigned32
_IsisCircNumAdj_Object = MibTableColumn
isisCircNumAdj = _IsisCircNumAdj_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1, 3),
    _IsisCircNumAdj_Type()
)
isisCircNumAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircNumAdj.setStatus("current")
_IsisCircInitFails_Type = Counter32
_IsisCircInitFails_Object = MibTableColumn
isisCircInitFails = _IsisCircInitFails_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1, 4),
    _IsisCircInitFails_Type()
)
isisCircInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircInitFails.setStatus("current")
_IsisCircRejAdjs_Type = Counter32
_IsisCircRejAdjs_Object = MibTableColumn
isisCircRejAdjs = _IsisCircRejAdjs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1, 5),
    _IsisCircRejAdjs_Type()
)
isisCircRejAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircRejAdjs.setStatus("current")
_IsisCircIDFieldLenMismatches_Type = Counter32
_IsisCircIDFieldLenMismatches_Object = MibTableColumn
isisCircIDFieldLenMismatches = _IsisCircIDFieldLenMismatches_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1, 6),
    _IsisCircIDFieldLenMismatches_Type()
)
isisCircIDFieldLenMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircIDFieldLenMismatches.setStatus("current")
if mibBuilder.loadTexts:
    isisCircIDFieldLenMismatches.setUnits("frames")
_IsisCircMaxAreaAddrMismatches_Type = Counter32
_IsisCircMaxAreaAddrMismatches_Object = MibTableColumn
isisCircMaxAreaAddrMismatches = _IsisCircMaxAreaAddrMismatches_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1, 7),
    _IsisCircMaxAreaAddrMismatches_Type()
)
isisCircMaxAreaAddrMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircMaxAreaAddrMismatches.setStatus("current")
_IsisCircAuthTypeFails_Type = Counter32
_IsisCircAuthTypeFails_Object = MibTableColumn
isisCircAuthTypeFails = _IsisCircAuthTypeFails_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1, 8),
    _IsisCircAuthTypeFails_Type()
)
isisCircAuthTypeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircAuthTypeFails.setStatus("current")
_IsisCircAuthFails_Type = Counter32
_IsisCircAuthFails_Object = MibTableColumn
isisCircAuthFails = _IsisCircAuthFails_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1, 9),
    _IsisCircAuthFails_Type()
)
isisCircAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircAuthFails.setStatus("current")
_IsisCircLANDesISChanges_Type = Counter32
_IsisCircLANDesISChanges_Object = MibTableColumn
isisCircLANDesISChanges = _IsisCircLANDesISChanges_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 2, 1, 10),
    _IsisCircLANDesISChanges_Type()
)
isisCircLANDesISChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisCircLANDesISChanges.setStatus("current")
_IsisPacketCounterTable_Object = MibTable
isisPacketCounterTable = _IsisPacketCounterTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    isisPacketCounterTable.setStatus("current")
_IsisPacketCounterEntry_Object = MibTableRow
isisPacketCounterEntry = _IsisPacketCounterEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1)
)
isisPacketCounterEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisPacketCountLevel"),
    (0, "DC-ISIS-MIB", "isisPacketCountDirection"),
)
if mibBuilder.loadTexts:
    isisPacketCounterEntry.setStatus("current")


class _IsisPacketCountLevel_Type(Integer32):
    """Custom type isisPacketCountLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("none", 0))
    )


_IsisPacketCountLevel_Type.__name__ = "Integer32"
_IsisPacketCountLevel_Object = MibTableColumn
isisPacketCountLevel = _IsisPacketCountLevel_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 1),
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
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 2),
    _IsisPacketCountDirection_Type()
)
isisPacketCountDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPacketCountDirection.setStatus("current")
_IsisPacketCountIIHello_Type = Counter32
_IsisPacketCountIIHello_Object = MibTableColumn
isisPacketCountIIHello = _IsisPacketCountIIHello_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 3),
    _IsisPacketCountIIHello_Type()
)
isisPacketCountIIHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountIIHello.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountIIHello.setUnits("frames")
_IsisPacketCountISHello_Type = Counter32
_IsisPacketCountISHello_Object = MibTableColumn
isisPacketCountISHello = _IsisPacketCountISHello_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 4),
    _IsisPacketCountISHello_Type()
)
isisPacketCountISHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountISHello.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountISHello.setUnits("frames")
_IsisPacketCountESHello_Type = Counter32
_IsisPacketCountESHello_Object = MibTableColumn
isisPacketCountESHello = _IsisPacketCountESHello_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 5),
    _IsisPacketCountESHello_Type()
)
isisPacketCountESHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountESHello.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountESHello.setUnits("frames")
_IsisPacketCountLSP_Type = Counter32
_IsisPacketCountLSP_Object = MibTableColumn
isisPacketCountLSP = _IsisPacketCountLSP_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 6),
    _IsisPacketCountLSP_Type()
)
isisPacketCountLSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountLSP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountLSP.setUnits("frames")
_IsisPacketCountCSNP_Type = Counter32
_IsisPacketCountCSNP_Object = MibTableColumn
isisPacketCountCSNP = _IsisPacketCountCSNP_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 7),
    _IsisPacketCountCSNP_Type()
)
isisPacketCountCSNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountCSNP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountCSNP.setUnits("frames")
_IsisPacketCountPSNP_Type = Counter32
_IsisPacketCountPSNP_Object = MibTableColumn
isisPacketCountPSNP = _IsisPacketCountPSNP_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 8),
    _IsisPacketCountPSNP_Type()
)
isisPacketCountPSNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountPSNP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountPSNP.setUnits("frames")
_IsisPacketCountUnknown_Type = Counter32
_IsisPacketCountUnknown_Object = MibTableColumn
isisPacketCountUnknown = _IsisPacketCountUnknown_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 9),
    _IsisPacketCountUnknown_Type()
)
isisPacketCountUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountUnknown.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountUnknown.setUnits("frames")
_IsisPacketCountDiscardedIIH_Type = Counter32
_IsisPacketCountDiscardedIIH_Object = MibTableColumn
isisPacketCountDiscardedIIH = _IsisPacketCountDiscardedIIH_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 10),
    _IsisPacketCountDiscardedIIH_Type()
)
isisPacketCountDiscardedIIH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountDiscardedIIH.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountDiscardedIIH.setUnits("frames")
_IsisPacketCountDiscardedLSP_Type = Counter32
_IsisPacketCountDiscardedLSP_Object = MibTableColumn
isisPacketCountDiscardedLSP = _IsisPacketCountDiscardedLSP_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 11),
    _IsisPacketCountDiscardedLSP_Type()
)
isisPacketCountDiscardedLSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountDiscardedLSP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountDiscardedLSP.setUnits("frames")
_IsisPacketCountDiscardedCSNP_Type = Counter32
_IsisPacketCountDiscardedCSNP_Object = MibTableColumn
isisPacketCountDiscardedCSNP = _IsisPacketCountDiscardedCSNP_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 12),
    _IsisPacketCountDiscardedCSNP_Type()
)
isisPacketCountDiscardedCSNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountDiscardedCSNP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountDiscardedCSNP.setUnits("frames")
_IsisPacketCountDiscardedPSNP_Type = Counter32
_IsisPacketCountDiscardedPSNP_Object = MibTableColumn
isisPacketCountDiscardedPSNP = _IsisPacketCountDiscardedPSNP_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 5, 3, 1, 13),
    _IsisPacketCountDiscardedPSNP_Type()
)
isisPacketCountDiscardedPSNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPacketCountDiscardedPSNP.setStatus("current")
if mibBuilder.loadTexts:
    isisPacketCountDiscardedPSNP.setUnits("frames")
_IsisISAdj_ObjectIdentity = ObjectIdentity
isisISAdj = _IsisISAdj_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6)
)
_IsisISAdjTable_Object = MibTable
isisISAdjTable = _IsisISAdjTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    isisISAdjTable.setStatus("current")
_IsisISAdjEntry_Object = MibTableRow
isisISAdjEntry = _IsisISAdjEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1)
)
isisISAdjEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisISAdjIndex"),
)
if mibBuilder.loadTexts:
    isisISAdjEntry.setStatus("current")


class _IsisISAdjIndex_Type(Integer32):
    """Custom type isisISAdjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisISAdjIndex_Type.__name__ = "Integer32"
_IsisISAdjIndex_Object = MibTableColumn
isisISAdjIndex = _IsisISAdjIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 1),
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
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 2),
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
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 3),
    _IsisISAdj3WayState_Type()
)
isisISAdj3WayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdj3WayState.setStatus("current")
_IsisISAdjNeighSNPAAddress_Type = OSINSAddress
_IsisISAdjNeighSNPAAddress_Object = MibTableColumn
isisISAdjNeighSNPAAddress = _IsisISAdjNeighSNPAAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 4),
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
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 5),
    _IsisISAdjNeighSysType_Type()
)
isisISAdjNeighSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighSysType.setStatus("current")
_IsisISAdjNeighSysID_Type = SystemID
_IsisISAdjNeighSysID_Object = MibTableColumn
isisISAdjNeighSysID = _IsisISAdjNeighSysID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 6),
    _IsisISAdjNeighSysID_Type()
)
isisISAdjNeighSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighSysID.setStatus("current")
_IsisISAdjNbrExtendedCircID_Type = Unsigned32
_IsisISAdjNbrExtendedCircID_Object = MibTableColumn
isisISAdjNbrExtendedCircID = _IsisISAdjNbrExtendedCircID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 7),
    _IsisISAdjNbrExtendedCircID_Type()
)
isisISAdjNbrExtendedCircID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNbrExtendedCircID.setStatus("current")


class _IsisISAdjUsage_Type(Integer32):
    """Custom type isisISAdjUsage based on Integer32"""
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
        *(("level1", 1),
          ("level1and2", 3),
          ("level2", 2),
          ("reserved", 0))
    )


_IsisISAdjUsage_Type.__name__ = "Integer32"
_IsisISAdjUsage_Object = MibTableColumn
isisISAdjUsage = _IsisISAdjUsage_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 8),
    _IsisISAdjUsage_Type()
)
isisISAdjUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjUsage.setStatus("current")


class _IsisISAdjHoldTimer_Type(Unsigned16TC):
    """Custom type isisISAdjHoldTimer based on Unsigned16TC"""
    subtypeSpec = Unsigned16TC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisISAdjHoldTimer_Type.__name__ = "Unsigned16TC"
_IsisISAdjHoldTimer_Object = MibTableColumn
isisISAdjHoldTimer = _IsisISAdjHoldTimer_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 9),
    _IsisISAdjHoldTimer_Type()
)
isisISAdjHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    isisISAdjHoldTimer.setUnits("seconds")
_IsisISAdjNeighPriority_Type = ISPriority
_IsisISAdjNeighPriority_Object = MibTableColumn
isisISAdjNeighPriority = _IsisISAdjNeighPriority_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 10),
    _IsisISAdjNeighPriority_Type()
)
isisISAdjNeighPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighPriority.setStatus("current")
_IsisISAdjLastUpTime_Type = TimeTicks
_IsisISAdjLastUpTime_Object = MibTableColumn
isisISAdjLastUpTime = _IsisISAdjLastUpTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 11),
    _IsisISAdjLastUpTime_Type()
)
isisISAdjLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjLastUpTime.setStatus("current")
if mibBuilder.loadTexts:
    isisISAdjLastUpTime.setUnits("seconds")
_IsisISAdjRestartCapable_Type = TruthValue
_IsisISAdjRestartCapable_Object = MibTableColumn
isisISAdjRestartCapable = _IsisISAdjRestartCapable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 12),
    _IsisISAdjRestartCapable_Type()
)
isisISAdjRestartCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjRestartCapable.setStatus("current")


class _IsisISAdjPeerRestartState_Type(Integer32):
    """Custom type isisISAdjPeerRestartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("helpingRestart", 3),
          ("notRestarting", 1),
          ("restartingNoHelp", 2))
    )


_IsisISAdjPeerRestartState_Type.__name__ = "Integer32"
_IsisISAdjPeerRestartState_Object = MibTableColumn
isisISAdjPeerRestartState = _IsisISAdjPeerRestartState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 13),
    _IsisISAdjPeerRestartState_Type()
)
isisISAdjPeerRestartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjPeerRestartState.setStatus("current")
_IsisISAdjSuppressed_Type = TruthValue
_IsisISAdjSuppressed_Object = MibTableColumn
isisISAdjSuppressed = _IsisISAdjSuppressed_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 14),
    _IsisISAdjSuppressed_Type()
)
isisISAdjSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjSuppressed.setStatus("current")


class _IsisISAdjNeighLanID_Type(OctetString):
    """Custom type isisISAdjNeighLanID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_IsisISAdjNeighLanID_Type.__name__ = "OctetString"
_IsisISAdjNeighLanID_Object = MibTableColumn
isisISAdjNeighLanID = _IsisISAdjNeighLanID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 15),
    _IsisISAdjNeighLanID_Type()
)
isisISAdjNeighLanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighLanID.setStatus("current")
_IsisISAdjNeighHostname_Type = SnmpAdminString
_IsisISAdjNeighHostname_Object = MibTableColumn
isisISAdjNeighHostname = _IsisISAdjNeighHostname_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 16),
    _IsisISAdjNeighHostname_Type()
)
isisISAdjNeighHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighHostname.setStatus("current")
_IsisISAdjNeighLanIDHostname_Type = SnmpAdminString
_IsisISAdjNeighLanIDHostname_Object = MibTableColumn
isisISAdjNeighLanIDHostname = _IsisISAdjNeighLanIDHostname_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 1, 1, 17),
    _IsisISAdjNeighLanIDHostname_Type()
)
isisISAdjNeighLanIDHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjNeighLanIDHostname.setStatus("current")
_IsisISAdjAreaAddrTable_Object = MibTable
isisISAdjAreaAddrTable = _IsisISAdjAreaAddrTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    isisISAdjAreaAddrTable.setStatus("current")
_IsisISAdjAreaAddrEntry_Object = MibTableRow
isisISAdjAreaAddrEntry = _IsisISAdjAreaAddrEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 2, 1)
)
isisISAdjAreaAddrEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisISAdjIndex"),
    (0, "DC-ISIS-MIB", "isisISAdjAreaAddrIndex"),
)
if mibBuilder.loadTexts:
    isisISAdjAreaAddrEntry.setStatus("current")


class _IsisISAdjAreaAddrIndex_Type(Integer32):
    """Custom type isisISAdjAreaAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisISAdjAreaAddrIndex_Type.__name__ = "Integer32"
_IsisISAdjAreaAddrIndex_Object = MibTableColumn
isisISAdjAreaAddrIndex = _IsisISAdjAreaAddrIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 2, 1, 1),
    _IsisISAdjAreaAddrIndex_Type()
)
isisISAdjAreaAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjAreaAddrIndex.setStatus("current")
_IsisISAdjAreaAddress_Type = OSINSAddress
_IsisISAdjAreaAddress_Object = MibTableColumn
isisISAdjAreaAddress = _IsisISAdjAreaAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 2, 1, 2),
    _IsisISAdjAreaAddress_Type()
)
isisISAdjAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjAreaAddress.setStatus("current")
_IsisISAdjIPAddrTable_Object = MibTable
isisISAdjIPAddrTable = _IsisISAdjIPAddrTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    isisISAdjIPAddrTable.setStatus("current")
_IsisISAdjIPAddrEntry_Object = MibTableRow
isisISAdjIPAddrEntry = _IsisISAdjIPAddrEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 3, 1)
)
isisISAdjIPAddrEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisISAdjIndex"),
    (0, "DC-ISIS-MIB", "isisISAdjIPAddrIndex"),
)
if mibBuilder.loadTexts:
    isisISAdjIPAddrEntry.setStatus("current")


class _IsisISAdjIPAddrIndex_Type(Integer32):
    """Custom type isisISAdjIPAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisISAdjIPAddrIndex_Type.__name__ = "Integer32"
_IsisISAdjIPAddrIndex_Object = MibTableColumn
isisISAdjIPAddrIndex = _IsisISAdjIPAddrIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 3, 1, 1),
    _IsisISAdjIPAddrIndex_Type()
)
isisISAdjIPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjIPAddrIndex.setStatus("current")
_IsisISAdjIPAddrType_Type = InetAddressType
_IsisISAdjIPAddrType_Object = MibTableColumn
isisISAdjIPAddrType = _IsisISAdjIPAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 3, 1, 2),
    _IsisISAdjIPAddrType_Type()
)
isisISAdjIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjIPAddrType.setStatus("current")


class _IsisISAdjIPAddrAddress_Type(InetAddress):
    """Custom type isisISAdjIPAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IsisISAdjIPAddrAddress_Type.__name__ = "InetAddress"
_IsisISAdjIPAddrAddress_Object = MibTableColumn
isisISAdjIPAddrAddress = _IsisISAdjIPAddrAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 3, 1, 3),
    _IsisISAdjIPAddrAddress_Type()
)
isisISAdjIPAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjIPAddrAddress.setStatus("current")
_IsisISAdjProtSuppTable_Object = MibTable
isisISAdjProtSuppTable = _IsisISAdjProtSuppTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    isisISAdjProtSuppTable.setStatus("current")
_IsisISAdjProtSuppEntry_Object = MibTableRow
isisISAdjProtSuppEntry = _IsisISAdjProtSuppEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 4, 1)
)
isisISAdjProtSuppEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisISAdjIndex"),
    (0, "DC-ISIS-MIB", "isisISAdjProtSuppProtocol"),
)
if mibBuilder.loadTexts:
    isisISAdjProtSuppEntry.setStatus("current")
_IsisISAdjProtSuppProtocol_Type = SupportedProtocol
_IsisISAdjProtSuppProtocol_Object = MibTableColumn
isisISAdjProtSuppProtocol = _IsisISAdjProtSuppProtocol_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 4, 1, 1),
    _IsisISAdjProtSuppProtocol_Type()
)
isisISAdjProtSuppProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjProtSuppProtocol.setStatus("current")
_IsisISAdjProtSuppLocalSupport_Type = TruthValue
_IsisISAdjProtSuppLocalSupport_Object = MibTableColumn
isisISAdjProtSuppLocalSupport = _IsisISAdjProtSuppLocalSupport_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 4, 1, 5),
    _IsisISAdjProtSuppLocalSupport_Type()
)
isisISAdjProtSuppLocalSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjProtSuppLocalSupport.setStatus("current")


class _IsisISAdjProtSuppBfdStatus_Type(Integer32):
    """Custom type isisISAdjProtSuppBfdStatus based on Integer32"""
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
        *(("active", 1),
          ("adminDown", 3),
          ("inactive", 2),
          ("noContact", 4),
          ("notRequired", 0))
    )


_IsisISAdjProtSuppBfdStatus_Type.__name__ = "Integer32"
_IsisISAdjProtSuppBfdStatus_Object = MibTableColumn
isisISAdjProtSuppBfdStatus = _IsisISAdjProtSuppBfdStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 4, 1, 6),
    _IsisISAdjProtSuppBfdStatus_Type()
)
isisISAdjProtSuppBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjProtSuppBfdStatus.setStatus("current")
_IsisISAdjMtSupportedTable_Object = MibTable
isisISAdjMtSupportedTable = _IsisISAdjMtSupportedTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    isisISAdjMtSupportedTable.setStatus("current")
_IsisISAdjMtSupportedEntry_Object = MibTableRow
isisISAdjMtSupportedEntry = _IsisISAdjMtSupportedEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 5, 1)
)
isisISAdjMtSupportedEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisCircIndex"),
    (0, "DC-ISIS-MIB", "isisISAdjIndex"),
    (0, "DC-ISIS-MIB", "isisISAdjMtSuppMtId"),
)
if mibBuilder.loadTexts:
    isisISAdjMtSupportedEntry.setStatus("current")


class _IsisISAdjMtSuppMtId_Type(Integer32):
    """Custom type isisISAdjMtSuppMtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IsisISAdjMtSuppMtId_Type.__name__ = "Integer32"
_IsisISAdjMtSuppMtId_Object = MibTableColumn
isisISAdjMtSuppMtId = _IsisISAdjMtSuppMtId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 5, 1, 4),
    _IsisISAdjMtSuppMtId_Type()
)
isisISAdjMtSuppMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisISAdjMtSuppMtId.setStatus("current")
_IsisISAdjMtSuppLocalSupport_Type = TruthValue
_IsisISAdjMtSuppLocalSupport_Object = MibTableColumn
isisISAdjMtSuppLocalSupport = _IsisISAdjMtSuppLocalSupport_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 6, 5, 1, 5),
    _IsisISAdjMtSuppLocalSupport_Type()
)
isisISAdjMtSuppLocalSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisISAdjMtSuppLocalSupport.setStatus("current")
_IsisReachAddr_ObjectIdentity = ObjectIdentity
isisReachAddr = _IsisReachAddr_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 7)
)
_IsisIPReachAddr_ObjectIdentity = ObjectIdentity
isisIPReachAddr = _IsisIPReachAddr_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8)
)
_IsisIPRATable_Object = MibTable
isisIPRATable = _IsisIPRATable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    isisIPRATable.setStatus("current")
_IsisIPRAEntry_Object = MibTableRow
isisIPRAEntry = _IsisIPRAEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1)
)
isisIPRAEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisIPRADestType"),
    (0, "DC-ISIS-MIB", "isisIPRADest"),
    (0, "DC-ISIS-MIB", "isisIPRADestPrefixLen"),
    (0, "DC-ISIS-MIB", "isisIPRANextHopIndex"),
)
if mibBuilder.loadTexts:
    isisIPRAEntry.setStatus("current")
_IsisIPRADestType_Type = InetAddressType
_IsisIPRADestType_Object = MibTableColumn
isisIPRADestType = _IsisIPRADestType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 1),
    _IsisIPRADestType_Type()
)
isisIPRADestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisIPRADestType.setStatus("current")


class _IsisIPRADest_Type(InetAddress):
    """Custom type isisIPRADest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IsisIPRADest_Type.__name__ = "InetAddress"
_IsisIPRADest_Object = MibTableColumn
isisIPRADest = _IsisIPRADest_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 2),
    _IsisIPRADest_Type()
)
isisIPRADest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisIPRADest.setStatus("current")


class _IsisIPRADestPrefixLen_Type(InetAddressPrefixLength):
    """Custom type isisIPRADestPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IsisIPRADestPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_IsisIPRADestPrefixLen_Object = MibTableColumn
isisIPRADestPrefixLen = _IsisIPRADestPrefixLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 3),
    _IsisIPRADestPrefixLen_Type()
)
isisIPRADestPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisIPRADestPrefixLen.setStatus("current")


class _IsisIPRANextHopIndex_Type(Integer32):
    """Custom type isisIPRANextHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsisIPRANextHopIndex_Type.__name__ = "Integer32"
_IsisIPRANextHopIndex_Object = MibTableColumn
isisIPRANextHopIndex = _IsisIPRANextHopIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 4),
    _IsisIPRANextHopIndex_Type()
)
isisIPRANextHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisIPRANextHopIndex.setStatus("current")
_IsisIPRANextHopType_Type = InetAddressType
_IsisIPRANextHopType_Object = MibTableColumn
isisIPRANextHopType = _IsisIPRANextHopType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 5),
    _IsisIPRANextHopType_Type()
)
isisIPRANextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRANextHopType.setStatus("current")


class _IsisIPRANextHop_Type(InetAddress):
    """Custom type isisIPRANextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IsisIPRANextHop_Type.__name__ = "InetAddress"
_IsisIPRANextHop_Object = MibTableColumn
isisIPRANextHop = _IsisIPRANextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 6),
    _IsisIPRANextHop_Type()
)
isisIPRANextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRANextHop.setStatus("current")


class _IsisIPRAType_Type(Integer32):
    """Custom type isisIPRAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("both", 3),
          ("manual", 1))
    )


_IsisIPRAType_Type.__name__ = "Integer32"
_IsisIPRAType_Object = MibTableColumn
isisIPRAType = _IsisIPRAType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 7),
    _IsisIPRAType_Type()
)
isisIPRAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRAType.setStatus("current")
_IsisIPRAExistState_Type = RowStatus
_IsisIPRAExistState_Object = MibTableColumn
isisIPRAExistState = _IsisIPRAExistState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 8),
    _IsisIPRAExistState_Type()
)
isisIPRAExistState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRAExistState.setStatus("current")
_IsisIPRAAdminState_Type = AdminState
_IsisIPRAAdminState_Object = MibTableColumn
isisIPRAAdminState = _IsisIPRAAdminState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 9),
    _IsisIPRAAdminState_Type()
)
isisIPRAAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRAAdminState.setStatus("current")
_IsisIPRAMetric_Type = DefaultMetric
_IsisIPRAMetric_Object = MibTableColumn
isisIPRAMetric = _IsisIPRAMetric_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 10),
    _IsisIPRAMetric_Type()
)
isisIPRAMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRAMetric.setStatus("current")
_IsisIPRAMetricType_Type = MetricType
_IsisIPRAMetricType_Object = MibTableColumn
isisIPRAMetricType = _IsisIPRAMetricType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 11),
    _IsisIPRAMetricType_Type()
)
isisIPRAMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRAMetricType.setStatus("current")
_IsisIPRAFullMetric_Type = FullMetric
_IsisIPRAFullMetric_Object = MibTableColumn
isisIPRAFullMetric = _IsisIPRAFullMetric_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 12),
    _IsisIPRAFullMetric_Type()
)
isisIPRAFullMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRAFullMetric.setStatus("current")
_IsisIPRASNPAAddress_Type = OSINSAddress
_IsisIPRASNPAAddress_Object = MibTableColumn
isisIPRASNPAAddress = _IsisIPRASNPAAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 13),
    _IsisIPRASNPAAddress_Type()
)
isisIPRASNPAAddress.setMaxAccess("read-only")
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
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 14),
    _IsisIPRASourceType_Type()
)
isisIPRASourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRASourceType.setStatus("current")


class _IsisIPRAMtId_Type(Integer32):
    """Custom type isisIPRAMtId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IsisIPRAMtId_Type.__name__ = "Integer32"
_IsisIPRAMtId_Object = MibTableColumn
isisIPRAMtId = _IsisIPRAMtId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 8, 1, 1, 16),
    _IsisIPRAMtId_Type()
)
isisIPRAMtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisIPRAMtId.setStatus("current")
_IsisLSPDataBase_ObjectIdentity = ObjectIdentity
isisLSPDataBase = _IsisLSPDataBase_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9)
)
_IsisLSPSummaryTable_Object = MibTable
isisLSPSummaryTable = _IsisLSPSummaryTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    isisLSPSummaryTable.setStatus("current")
_IsisLSPSummaryEntry_Object = MibTableRow
isisLSPSummaryEntry = _IsisLSPSummaryEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1, 1)
)
isisLSPSummaryEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisLSPLevel"),
    (0, "DC-ISIS-MIB", "isisLSPID"),
)
if mibBuilder.loadTexts:
    isisLSPSummaryEntry.setStatus("current")
_IsisLSPLevel_Type = ISLevel
_IsisLSPLevel_Object = MibTableColumn
isisLSPLevel = _IsisLSPLevel_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1, 1, 1),
    _IsisLSPLevel_Type()
)
isisLSPLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisLSPLevel.setStatus("current")
_IsisLSPID_Type = LinkStatePDUID
_IsisLSPID_Object = MibTableColumn
isisLSPID = _IsisLSPID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1, 1, 2),
    _IsisLSPID_Type()
)
isisLSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisLSPID.setStatus("current")
_IsisLSPSeq_Type = Unsigned32
_IsisLSPSeq_Object = MibTableColumn
isisLSPSeq = _IsisLSPSeq_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1, 1, 3),
    _IsisLSPSeq_Type()
)
isisLSPSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPSeq.setStatus("current")
_IsisLSPZeroLife_Type = TruthValue
_IsisLSPZeroLife_Object = MibTableColumn
isisLSPZeroLife = _IsisLSPZeroLife_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1, 1, 4),
    _IsisLSPZeroLife_Type()
)
isisLSPZeroLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPZeroLife.setStatus("current")
_IsisLSPChecksum_Type = Unsigned16TC
_IsisLSPChecksum_Object = MibTableColumn
isisLSPChecksum = _IsisLSPChecksum_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1, 1, 5),
    _IsisLSPChecksum_Type()
)
isisLSPChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPChecksum.setStatus("current")
_IsisLSPLifetimeRemain_Type = Unsigned16TC
_IsisLSPLifetimeRemain_Object = MibTableColumn
isisLSPLifetimeRemain = _IsisLSPLifetimeRemain_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1, 1, 6),
    _IsisLSPLifetimeRemain_Type()
)
isisLSPLifetimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPLifetimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    isisLSPLifetimeRemain.setUnits("seconds")
_IsisLSPPDULength_Type = Unsigned16TC
_IsisLSPPDULength_Object = MibTableColumn
isisLSPPDULength = _IsisLSPPDULength_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1, 1, 7),
    _IsisLSPPDULength_Type()
)
isisLSPPDULength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPPDULength.setStatus("current")
_IsisLSPAttributes_Type = Unsigned8TC
_IsisLSPAttributes_Object = MibTableColumn
isisLSPAttributes = _IsisLSPAttributes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1, 1, 8),
    _IsisLSPAttributes_Type()
)
isisLSPAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPAttributes.setStatus("current")
_IsisLSPIDHostname_Type = SnmpAdminString
_IsisLSPIDHostname_Object = MibTableColumn
isisLSPIDHostname = _IsisLSPIDHostname_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 1, 1, 9),
    _IsisLSPIDHostname_Type()
)
isisLSPIDHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPIDHostname.setStatus("current")
_IsisLSPTLVTable_Object = MibTable
isisLSPTLVTable = _IsisLSPTLVTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    isisLSPTLVTable.setStatus("current")
_IsisLSPTLVEntry_Object = MibTableRow
isisLSPTLVEntry = _IsisLSPTLVEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 2, 1)
)
isisLSPTLVEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisLSPLevel"),
    (0, "DC-ISIS-MIB", "isisLSPID"),
    (0, "DC-ISIS-MIB", "isisLSPTLVIndex"),
)
if mibBuilder.loadTexts:
    isisLSPTLVEntry.setStatus("current")
_IsisLSPTLVIndex_Type = Unsigned32
_IsisLSPTLVIndex_Object = MibTableColumn
isisLSPTLVIndex = _IsisLSPTLVIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 2, 1, 1),
    _IsisLSPTLVIndex_Type()
)
isisLSPTLVIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisLSPTLVIndex.setStatus("current")
_IsisLSPTLVSeq_Type = Unsigned32
_IsisLSPTLVSeq_Object = MibTableColumn
isisLSPTLVSeq = _IsisLSPTLVSeq_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 2, 1, 2),
    _IsisLSPTLVSeq_Type()
)
isisLSPTLVSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPTLVSeq.setStatus("current")
_IsisLSPTLVChecksum_Type = Unsigned16TC
_IsisLSPTLVChecksum_Object = MibTableColumn
isisLSPTLVChecksum = _IsisLSPTLVChecksum_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 2, 1, 3),
    _IsisLSPTLVChecksum_Type()
)
isisLSPTLVChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPTLVChecksum.setStatus("current")
_IsisLSPTLVType_Type = Unsigned8TC
_IsisLSPTLVType_Object = MibTableColumn
isisLSPTLVType = _IsisLSPTLVType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 2, 1, 4),
    _IsisLSPTLVType_Type()
)
isisLSPTLVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPTLVType.setStatus("current")
_IsisLSPTLVLen_Type = Unsigned8TC
_IsisLSPTLVLen_Object = MibTableColumn
isisLSPTLVLen = _IsisLSPTLVLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 2, 1, 5),
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
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 2, 1, 6),
    _IsisLSPTLVValue_Type()
)
isisLSPTLVValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPTLVValue.setStatus("current")
_IsisLSPTLVHostname_Type = SnmpAdminString
_IsisLSPTLVHostname_Object = MibTableColumn
isisLSPTLVHostname = _IsisLSPTLVHostname_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 9, 2, 1, 7),
    _IsisLSPTLVHostname_Type()
)
isisLSPTLVHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisLSPTLVHostname.setStatus("current")
_IsisNotification_ObjectIdentity = ObjectIdentity
isisNotification = _IsisNotification_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10)
)
_IsisNotificationEntry_ObjectIdentity = ObjectIdentity
isisNotificationEntry = _IsisNotificationEntry_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1)
)
_IsisPduLspId_Type = LinkStatePDUID
_IsisPduLspId_Object = MibScalar
isisPduLspId = _IsisPduLspId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 1),
    _IsisPduLspId_Type()
)
isisPduLspId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduLspId.setStatus("current")
_IsisPduFragment_Type = IsisPDUHeader
_IsisPduFragment_Object = MibScalar
isisPduFragment = _IsisPduFragment_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 2),
    _IsisPduFragment_Type()
)
isisPduFragment.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduFragment.setStatus("current")
_IsisPduFieldLen_Type = Unsigned8TC
_IsisPduFieldLen_Object = MibScalar
isisPduFieldLen = _IsisPduFieldLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 3),
    _IsisPduFieldLen_Type()
)
isisPduFieldLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduFieldLen.setStatus("current")
_IsisPduMaxAreaAddress_Type = Unsigned8TC
_IsisPduMaxAreaAddress_Object = MibScalar
isisPduMaxAreaAddress = _IsisPduMaxAreaAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 4),
    _IsisPduMaxAreaAddress_Type()
)
isisPduMaxAreaAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisPduMaxAreaAddress.setStatus("current")


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
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 5),
    _IsisAdjState_Type()
)
isisAdjState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisAdjState.setStatus("current")
_IsisErrorOffset_Type = Unsigned32
_IsisErrorOffset_Object = MibScalar
isisErrorOffset = _IsisErrorOffset_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 6),
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
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 7),
    _IsisErrorTLVType_Type()
)
isisErrorTLVType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisErrorTLVType.setStatus("current")


class _IsisNotificationSysInstance_Type(Integer32):
    """Custom type isisNotificationSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsisNotificationSysInstance_Type.__name__ = "Integer32"
_IsisNotificationSysInstance_Object = MibScalar
isisNotificationSysInstance = _IsisNotificationSysInstance_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 8),
    _IsisNotificationSysInstance_Type()
)
isisNotificationSysInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationSysInstance.setStatus("current")
_IsisNotificationSysLevelIndex_Type = IsisAdjLevel
_IsisNotificationSysLevelIndex_Object = MibScalar
isisNotificationSysLevelIndex = _IsisNotificationSysLevelIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 9),
    _IsisNotificationSysLevelIndex_Type()
)
isisNotificationSysLevelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationSysLevelIndex.setStatus("current")
_IsisNotificationAreaAddress_Type = OSINSAddress
_IsisNotificationAreaAddress_Object = MibScalar
isisNotificationAreaAddress = _IsisNotificationAreaAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 10),
    _IsisNotificationAreaAddress_Type()
)
isisNotificationAreaAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationAreaAddress.setStatus("current")


class _IsisNotificationISAdjIndex_Type(Integer32):
    """Custom type isisNotificationISAdjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_IsisNotificationISAdjIndex_Type.__name__ = "Integer32"
_IsisNotificationISAdjIndex_Object = MibScalar
isisNotificationISAdjIndex = _IsisNotificationISAdjIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 11),
    _IsisNotificationISAdjIndex_Type()
)
isisNotificationISAdjIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationISAdjIndex.setStatus("current")


class _IsisNotificationDisState_Type(Integer32):
    """Custom type isisNotificationDisState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("none", 3),
          ("remote", 2))
    )


_IsisNotificationDisState_Type.__name__ = "Integer32"
_IsisNotificationDisState_Object = MibScalar
isisNotificationDisState = _IsisNotificationDisState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 12),
    _IsisNotificationDisState_Type()
)
isisNotificationDisState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationDisState.setStatus("current")


class _IsisNotificationAttachedState_Type(Integer32):
    """Custom type isisNotificationAttachedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 1),
          ("notAttached", 2))
    )


_IsisNotificationAttachedState_Type.__name__ = "Integer32"
_IsisNotificationAttachedState_Object = MibScalar
isisNotificationAttachedState = _IsisNotificationAttachedState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 13),
    _IsisNotificationAttachedState_Type()
)
isisNotificationAttachedState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationAttachedState.setStatus("current")
_IsisNotificationNeighSysID_Type = SystemID
_IsisNotificationNeighSysID_Object = MibScalar
isisNotificationNeighSysID = _IsisNotificationNeighSysID_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 14),
    _IsisNotificationNeighSysID_Type()
)
isisNotificationNeighSysID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationNeighSysID.setStatus("current")


class _IsisNotificationMtId_Type(Integer32):
    """Custom type isisNotificationMtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IsisNotificationMtId_Type.__name__ = "Integer32"
_IsisNotificationMtId_Object = MibScalar
isisNotificationMtId = _IsisNotificationMtId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 10, 1, 15),
    _IsisNotificationMtId_Type()
)
isisNotificationMtId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isisNotificationMtId.setStatus("current")
_IsisPmObjects_ObjectIdentity = ObjectIdentity
isisPmObjects = _IsisPmObjects_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11)
)
_IsisPmSjTable_Object = MibTable
isisPmSjTable = _IsisPmSjTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    isisPmSjTable.setStatus("current")
_IsisPmSjEntry_Object = MibTableRow
isisPmSjEntry = _IsisPmSjEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 1, 1)
)
isisPmSjEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisPmSjInterface"),
    (0, "DC-ISIS-MIB", "isisPmSjMasterEntity"),
)
if mibBuilder.loadTexts:
    isisPmSjEntry.setStatus("current")
_IsisPmSjInterface_Type = IsisPmInterfaceId
_IsisPmSjInterface_Object = MibTableColumn
isisPmSjInterface = _IsisPmSjInterface_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 1, 1, 1),
    _IsisPmSjInterface_Type()
)
isisPmSjInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPmSjInterface.setStatus("current")
_IsisPmSjMasterEntity_Type = Unsigned32
_IsisPmSjMasterEntity_Object = MibTableColumn
isisPmSjMasterEntity = _IsisPmSjMasterEntity_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 1, 1, 2),
    _IsisPmSjMasterEntity_Type()
)
isisPmSjMasterEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPmSjMasterEntity.setStatus("current")
_IsisPmSjJoinStatus_Type = IsisSjStatus
_IsisPmSjJoinStatus_Object = MibTableColumn
isisPmSjJoinStatus = _IsisPmSjJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 1, 1, 3),
    _IsisPmSjJoinStatus_Type()
)
isisPmSjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPmSjJoinStatus.setStatus("current")
_IsisPmMjTable_Object = MibTable
isisPmMjTable = _IsisPmMjTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    isisPmMjTable.setStatus("current")
_IsisPmMjEntry_Object = MibTableRow
isisPmMjEntry = _IsisPmMjEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2, 1)
)
isisPmMjEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisPmMjInterface"),
    (0, "DC-ISIS-MIB", "isisPmMjSlaveEntity"),
    (0, "DC-ISIS-MIB", "isisPmMjAddrType"),
    (0, "DC-ISIS-MIB", "isisPmMjMtId"),
)
if mibBuilder.loadTexts:
    isisPmMjEntry.setStatus("current")
_IsisPmMjInterface_Type = IsisPmInterfaceId
_IsisPmMjInterface_Object = MibTableColumn
isisPmMjInterface = _IsisPmMjInterface_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2, 1, 1),
    _IsisPmMjInterface_Type()
)
isisPmMjInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPmMjInterface.setStatus("current")
_IsisPmMjSlaveEntity_Type = Unsigned32
_IsisPmMjSlaveEntity_Object = MibTableColumn
isisPmMjSlaveEntity = _IsisPmMjSlaveEntity_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2, 1, 2),
    _IsisPmMjSlaveEntity_Type()
)
isisPmMjSlaveEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPmMjSlaveEntity.setStatus("current")
_IsisPmMjAddrType_Type = IsisAddrType
_IsisPmMjAddrType_Object = MibTableColumn
isisPmMjAddrType = _IsisPmMjAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2, 1, 3),
    _IsisPmMjAddrType_Type()
)
isisPmMjAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPmMjAddrType.setStatus("current")
_IsisPmMjRowStatus_Type = RowStatus
_IsisPmMjRowStatus_Object = MibTableColumn
isisPmMjRowStatus = _IsisPmMjRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2, 1, 4),
    _IsisPmMjRowStatus_Type()
)
isisPmMjRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisPmMjRowStatus.setStatus("current")


class _IsisPmMjAdminStatus_Type(IsisAdminStatus):
    """Custom type isisPmMjAdminStatus based on IsisAdminStatus"""


_IsisPmMjAdminStatus_Object = MibTableColumn
isisPmMjAdminStatus = _IsisPmMjAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2, 1, 5),
    _IsisPmMjAdminStatus_Type()
)
isisPmMjAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisPmMjAdminStatus.setStatus("current")
_IsisPmMjOperStatus_Type = IsisOperStatus
_IsisPmMjOperStatus_Object = MibTableColumn
isisPmMjOperStatus = _IsisPmMjOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2, 1, 6),
    _IsisPmMjOperStatus_Type()
)
isisPmMjOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPmMjOperStatus.setStatus("current")
_IsisPmMjJoinStatus_Type = IsisMjStatus
_IsisPmMjJoinStatus_Object = MibTableColumn
isisPmMjJoinStatus = _IsisPmMjJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2, 1, 7),
    _IsisPmMjJoinStatus_Type()
)
isisPmMjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisPmMjJoinStatus.setStatus("current")


class _IsisPmMjMtId_Type(Integer32):
    """Custom type isisPmMjMtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IsisPmMjMtId_Type.__name__ = "Integer32"
_IsisPmMjMtId_Object = MibTableColumn
isisPmMjMtId = _IsisPmMjMtId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2, 1, 9),
    _IsisPmMjMtId_Type()
)
isisPmMjMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisPmMjMtId.setStatus("current")


class _IsisPmMjSubAddrFamily_Type(Integer32):
    """Custom type isisPmMjSubAddrFamily based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IsisPmMjSubAddrFamily_Type.__name__ = "Integer32"
_IsisPmMjSubAddrFamily_Object = MibTableColumn
isisPmMjSubAddrFamily = _IsisPmMjSubAddrFamily_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 2, 1, 10),
    _IsisPmMjSubAddrFamily_Type()
)
isisPmMjSubAddrFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisPmMjSubAddrFamily.setStatus("current")
_IsisIgpShortcutTable_Object = MibTable
isisIgpShortcutTable = _IsisIgpShortcutTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 3)
)
if mibBuilder.loadTexts:
    isisIgpShortcutTable.setStatus("current")
_IsisIgpShortcutEntry_Object = MibTableRow
isisIgpShortcutEntry = _IsisIgpShortcutEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 3, 1)
)
isisIgpShortcutEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSysInstance"),
    (0, "DC-ISIS-MIB", "isisShortcutIfIndex"),
)
if mibBuilder.loadTexts:
    isisIgpShortcutEntry.setStatus("current")
_IsisShortcutIfIndex_Type = InterfaceIndex
_IsisShortcutIfIndex_Object = MibTableColumn
isisShortcutIfIndex = _IsisShortcutIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 3, 1, 1),
    _IsisShortcutIfIndex_Type()
)
isisShortcutIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisShortcutIfIndex.setStatus("current")
_IsisShortcutRemoteAddressType_Type = InetAddressType
_IsisShortcutRemoteAddressType_Object = MibTableColumn
isisShortcutRemoteAddressType = _IsisShortcutRemoteAddressType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 3, 1, 2),
    _IsisShortcutRemoteAddressType_Type()
)
isisShortcutRemoteAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisShortcutRemoteAddressType.setStatus("current")


class _IsisShortcutRemoteAddress_Type(InetAddress):
    """Custom type isisShortcutRemoteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IsisShortcutRemoteAddress_Type.__name__ = "InetAddress"
_IsisShortcutRemoteAddress_Object = MibTableColumn
isisShortcutRemoteAddress = _IsisShortcutRemoteAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 3, 1, 3),
    _IsisShortcutRemoteAddress_Type()
)
isisShortcutRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisShortcutRemoteAddress.setStatus("current")
_IsisShortcutMetricType_Type = IgpShortcutMetricType
_IsisShortcutMetricType_Object = MibTableColumn
isisShortcutMetricType = _IsisShortcutMetricType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 3, 1, 4),
    _IsisShortcutMetricType_Type()
)
isisShortcutMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisShortcutMetricType.setStatus("current")
_IsisShortcutMetricValue_Type = Integer32
_IsisShortcutMetricValue_Object = MibTableColumn
isisShortcutMetricValue = _IsisShortcutMetricValue_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 3, 1, 5),
    _IsisShortcutMetricValue_Type()
)
isisShortcutMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisShortcutMetricValue.setStatus("current")
_IsisShortcutOperStatus_Type = IfOperStatus
_IsisShortcutOperStatus_Object = MibTableColumn
isisShortcutOperStatus = _IsisShortcutOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 3, 1, 6),
    _IsisShortcutOperStatus_Type()
)
isisShortcutOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisShortcutOperStatus.setStatus("current")
_IsisShortcutPendingDeletion_Type = TruthValue
_IsisShortcutPendingDeletion_Object = MibTableColumn
isisShortcutPendingDeletion = _IsisShortcutPendingDeletion_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 11, 3, 1, 7),
    _IsisShortcutPendingDeletion_Type()
)
isisShortcutPendingDeletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisShortcutPendingDeletion.setStatus("current")
_IsisSdObjects_ObjectIdentity = ObjectIdentity
isisSdObjects = _IsisSdObjects_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12)
)
_IsisSdEntTable_Object = MibTable
isisSdEntTable = _IsisSdEntTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    isisSdEntTable.setStatus("current")
_IsisSdEntEntry_Object = MibTableRow
isisSdEntEntry = _IsisSdEntEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 1, 1)
)
isisSdEntEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSdEntIndex"),
)
if mibBuilder.loadTexts:
    isisSdEntEntry.setStatus("current")


class _IsisSdEntIndex_Type(Integer32):
    """Custom type isisSdEntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsisSdEntIndex_Type.__name__ = "Integer32"
_IsisSdEntIndex_Object = MibTableColumn
isisSdEntIndex = _IsisSdEntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 1, 1, 1),
    _IsisSdEntIndex_Type()
)
isisSdEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSdEntIndex.setStatus("current")
_IsisSdEntRowStatus_Type = RowStatus
_IsisSdEntRowStatus_Object = MibTableColumn
isisSdEntRowStatus = _IsisSdEntRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 1, 1, 2),
    _IsisSdEntRowStatus_Type()
)
isisSdEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSdEntRowStatus.setStatus("current")


class _IsisSdEntAdminStatus_Type(IsisAdminStatus):
    """Custom type isisSdEntAdminStatus based on IsisAdminStatus"""


_IsisSdEntAdminStatus_Object = MibTableColumn
isisSdEntAdminStatus = _IsisSdEntAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 1, 1, 3),
    _IsisSdEntAdminStatus_Type()
)
isisSdEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSdEntAdminStatus.setStatus("current")
_IsisSdEntOperStatus_Type = IsisOperStatus
_IsisSdEntOperStatus_Object = MibTableColumn
isisSdEntOperStatus = _IsisSdEntOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 1, 1, 4),
    _IsisSdEntOperStatus_Type()
)
isisSdEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSdEntOperStatus.setStatus("current")


class _IsisSdEntMapHostnames_Type(TruthValue):
    """Custom type isisSdEntMapHostnames based on TruthValue"""


_IsisSdEntMapHostnames_Object = MibTableColumn
isisSdEntMapHostnames = _IsisSdEntMapHostnames_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 1, 1, 5),
    _IsisSdEntMapHostnames_Type()
)
isisSdEntMapHostnames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSdEntMapHostnames.setStatus("current")


class _IsisSdEntAuthSNPs_Type(TruthValue):
    """Custom type isisSdEntAuthSNPs based on TruthValue"""


_IsisSdEntAuthSNPs_Object = MibTableColumn
isisSdEntAuthSNPs = _IsisSdEntAuthSNPs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 1, 1, 6),
    _IsisSdEntAuthSNPs_Type()
)
isisSdEntAuthSNPs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSdEntAuthSNPs.setStatus("current")


class _IsisSdEntBfdProviderIndex_Type(EntityIndexOrZero):
    """Custom type isisSdEntBfdProviderIndex based on EntityIndexOrZero"""
    defaultValue = 0


_IsisSdEntBfdProviderIndex_Object = MibTableColumn
isisSdEntBfdProviderIndex = _IsisSdEntBfdProviderIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 1, 1, 7),
    _IsisSdEntBfdProviderIndex_Type()
)
isisSdEntBfdProviderIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSdEntBfdProviderIndex.setStatus("current")


class _IsisSdEntStopAdjDuplIDs_Type(TruthValue):
    """Custom type isisSdEntStopAdjDuplIDs based on TruthValue"""


_IsisSdEntStopAdjDuplIDs_Object = MibTableColumn
isisSdEntStopAdjDuplIDs = _IsisSdEntStopAdjDuplIDs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 1, 1, 8),
    _IsisSdEntStopAdjDuplIDs_Type()
)
isisSdEntStopAdjDuplIDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSdEntStopAdjDuplIDs.setStatus("current")
_IsisSdMjTable_Object = MibTable
isisSdMjTable = _IsisSdMjTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    isisSdMjTable.setStatus("current")
_IsisSdMjEntry_Object = MibTableRow
isisSdMjEntry = _IsisSdMjEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 2, 1)
)
isisSdMjEntry.setIndexNames(
    (0, "DC-ISIS-MIB", "isisSdEntIndex"),
    (0, "DC-ISIS-MIB", "isisSdMjInterface"),
)
if mibBuilder.loadTexts:
    isisSdMjEntry.setStatus("current")
_IsisSdMjInterface_Type = IsisSdInterfaceId
_IsisSdMjInterface_Object = MibTableColumn
isisSdMjInterface = _IsisSdMjInterface_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 2, 1, 1),
    _IsisSdMjInterface_Type()
)
isisSdMjInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isisSdMjInterface.setStatus("current")
_IsisSdMjRowStatus_Type = RowStatus
_IsisSdMjRowStatus_Object = MibTableColumn
isisSdMjRowStatus = _IsisSdMjRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 2, 1, 2),
    _IsisSdMjRowStatus_Type()
)
isisSdMjRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSdMjRowStatus.setStatus("current")


class _IsisSdMjAdminStatus_Type(IsisAdminStatus):
    """Custom type isisSdMjAdminStatus based on IsisAdminStatus"""


_IsisSdMjAdminStatus_Object = MibTableColumn
isisSdMjAdminStatus = _IsisSdMjAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 2, 1, 3),
    _IsisSdMjAdminStatus_Type()
)
isisSdMjAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSdMjAdminStatus.setStatus("current")
_IsisSdMjOperStatus_Type = IsisOperStatus
_IsisSdMjOperStatus_Object = MibTableColumn
isisSdMjOperStatus = _IsisSdMjOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 2, 1, 4),
    _IsisSdMjOperStatus_Type()
)
isisSdMjOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSdMjOperStatus.setStatus("current")
_IsisSdMjEntityIndex_Type = Unsigned32
_IsisSdMjEntityIndex_Object = MibTableColumn
isisSdMjEntityIndex = _IsisSdMjEntityIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 2, 1, 5),
    _IsisSdMjEntityIndex_Type()
)
isisSdMjEntityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSdMjEntityIndex.setStatus("current")


class _IsisSdMjEntityType_Type(IsisSdEntityType):
    """Custom type isisSdMjEntityType based on IsisSdEntityType"""


_IsisSdMjEntityType_Object = MibTableColumn
isisSdMjEntityType = _IsisSdMjEntityType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 2, 1, 6),
    _IsisSdMjEntityType_Type()
)
isisSdMjEntityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isisSdMjEntityType.setStatus("current")
_IsisSdMjJoinStatus_Type = IsisMjStatus
_IsisSdMjJoinStatus_Object = MibTableColumn
isisSdMjJoinStatus = _IsisSdMjJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 1, 12, 2, 1, 7),
    _IsisSdMjJoinStatus_Type()
)
isisSdMjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isisSdMjJoinStatus.setStatus("current")
_IsisNotifications_ObjectIdentity = ObjectIdentity
isisNotifications = _IsisNotifications_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2)
)
_IsisTrapPrefix_ObjectIdentity = ObjectIdentity
isisTrapPrefix = _IsisTrapPrefix_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0)
)
_IsisConformance_ObjectIdentity = ObjectIdentity
isisConformance = _IsisConformance_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3)
)
_IsisGroups_ObjectIdentity = ObjectIdentity
isisGroups = _IsisGroups_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 1)
)
_IsisCompliances_ObjectIdentity = ObjectIdentity
isisCompliances = _IsisCompliances_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 2)
)

# Managed Objects groups

isisSystemGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 1, 1)
)
isisSystemGroup.setObjects(
      *(("DC-ISIS-MIB", "isisSysVersion"),
        ("DC-ISIS-MIB", "isisSysType"),
        ("DC-ISIS-MIB", "isisSysID"),
        ("DC-ISIS-MIB", "isisSysMaxPathSplits"),
        ("DC-ISIS-MIB", "isisSysMaxLSPGenInt"),
        ("DC-ISIS-MIB", "isisSysPollESHelloRate"),
        ("DC-ISIS-MIB", "isisSysWaitTime"),
        ("DC-ISIS-MIB", "isisSysAdminState"),
        ("DC-ISIS-MIB", "isisSysL2toL1Leaking"),
        ("DC-ISIS-MIB", "isisSysMaxAge"),
        ("DC-ISIS-MIB", "isisSysLevelOrigLSPBuffSize"),
        ("DC-ISIS-MIB", "isisSysLevelMinLSPGenInt"),
        ("DC-ISIS-MIB", "isisSysLevelOverloadState"),
        ("DC-ISIS-MIB", "isisSysLevelSetOverload"),
        ("DC-ISIS-MIB", "isisSysLevelSetOverloadUntil"),
        ("DC-ISIS-MIB", "isisSysLevelMetricStyle"),
        ("DC-ISIS-MIB", "isisSysLevelSPFConsiders"),
        ("DC-ISIS-MIB", "isisSysLevelTEEnabled"),
        ("DC-ISIS-MIB", "isisSysReceiveLSPBufferSize"),
        ("DC-ISIS-MIB", "isisManAreaAddrExistState"),
        ("DC-ISIS-MIB", "isisAreaAddrInLSP"),
        ("DC-ISIS-MIB", "isisSummAddrExistState"),
        ("DC-ISIS-MIB", "isisSummAddrMetric"),
        ("DC-ISIS-MIB", "isisSummAddrFullMetric"),
        ("DC-ISIS-MIB", "isisRedistributeAddrExistState"),
        ("DC-ISIS-MIB", "isisRouterHostName"),
        ("DC-ISIS-MIB", "isisRouterID"),
        ("DC-ISIS-MIB", "isisSysStatCorrLSPs"),
        ("DC-ISIS-MIB", "isisSysStatLSPDbaseOloads"),
        ("DC-ISIS-MIB", "isisSysStatManAddrDropFromAreas"),
        ("DC-ISIS-MIB", "isisSysStatAttmptToExMaxSeqNums"),
        ("DC-ISIS-MIB", "isisSysStatSeqNumSkips"),
        ("DC-ISIS-MIB", "isisSysStatOwnLSPPurges"),
        ("DC-ISIS-MIB", "isisSysStatIDFieldLenMismatches"),
        ("DC-ISIS-MIB", "isisSysStatPartChanges"),
        ("DC-ISIS-MIB", "isisSysStatSPFRuns"),
        ("DC-ISIS-MIB", "isisSysStatAuthTypeFails"),
        ("DC-ISIS-MIB", "isisSysStatAuthFails"),
        ("DC-ISIS-MIB", "isisSysStatLSPError"))
)
if mibBuilder.loadTexts:
    isisSystemGroup.setStatus("current")

isisCircuitGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 1, 2)
)
isisCircuitGroup.setObjects(
      *(("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisCircIfSubIndex"),
        ("DC-ISIS-MIB", "isisCircAdminState"),
        ("DC-ISIS-MIB", "isisCircExistState"),
        ("DC-ISIS-MIB", "isisCircType"),
        ("DC-ISIS-MIB", "isisCircExtDomain"),
        ("DC-ISIS-MIB", "isisCircAdjChanges"),
        ("DC-ISIS-MIB", "isisCircNumAdj"),
        ("DC-ISIS-MIB", "isisCircInitFails"),
        ("DC-ISIS-MIB", "isisCircRejAdjs"),
        ("DC-ISIS-MIB", "isisCircIDFieldLenMismatches"),
        ("DC-ISIS-MIB", "isisCircMaxAreaAddrMismatches"),
        ("DC-ISIS-MIB", "isisCircAuthTypeFails"),
        ("DC-ISIS-MIB", "isisCircAuthFails"),
        ("DC-ISIS-MIB", "isisCircLANDesISChanges"),
        ("DC-ISIS-MIB", "isisCircLevel"),
        ("DC-ISIS-MIB", "isisCircPassiveCircuit"),
        ("DC-ISIS-MIB", "isisCircMeshGroupEnabled"),
        ("DC-ISIS-MIB", "isisCircMeshGroup"),
        ("DC-ISIS-MIB", "isisCircSmallHellos"),
        ("DC-ISIS-MIB", "isisCircLastUpTime"),
        ("DC-ISIS-MIB", "isisCirc3WayEnabled"),
        ("DC-ISIS-MIB", "isisCircExtendedCircID"),
        ("DC-ISIS-MIB", "isisCircLevelMetric"),
        ("DC-ISIS-MIB", "isisCircLevelWideMetric"),
        ("DC-ISIS-MIB", "isisCircLevelISPriority"),
        ("DC-ISIS-MIB", "isisCircLevelIDOctet"),
        ("DC-ISIS-MIB", "isisCircLevelID"),
        ("DC-ISIS-MIB", "isisCircLevelDesIS"),
        ("DC-ISIS-MIB", "isisCircLevelHelloMultiplier"),
        ("DC-ISIS-MIB", "isisCircLevelHelloTimer"),
        ("DC-ISIS-MIB", "isisCircLevelDRHelloTimer"),
        ("DC-ISIS-MIB", "isisCircLevelLSPThrottle"),
        ("DC-ISIS-MIB", "isisCircLevelMinLSPRetransInt"),
        ("DC-ISIS-MIB", "isisCircLevelCSNPInterval"),
        ("DC-ISIS-MIB", "isisCircLevelPartSNPInterval"),
        ("DC-ISIS-MIB", "isisCircIPAddrRowStatus"),
        ("DC-ISIS-MIB", "isisCircIPAddrAdminState"),
        ("DC-ISIS-MIB", "isisCircIPAddrAddressType"),
        ("DC-ISIS-MIB", "isisCircIPAddrAddress"),
        ("DC-ISIS-MIB", "isisCircIPAddrInLSP"))
)
if mibBuilder.loadTexts:
    isisCircuitGroup.setStatus("current")

isisISAdjGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 1, 3)
)
isisISAdjGroup.setObjects(
      *(("DC-ISIS-MIB", "isisISAdjState"),
        ("DC-ISIS-MIB", "isisISAdj3WayState"),
        ("DC-ISIS-MIB", "isisISAdjNeighSNPAAddress"),
        ("DC-ISIS-MIB", "isisISAdjNeighSysType"),
        ("DC-ISIS-MIB", "isisISAdjNeighSysID"),
        ("DC-ISIS-MIB", "isisISAdjNbrExtendedCircID"),
        ("DC-ISIS-MIB", "isisISAdjUsage"),
        ("DC-ISIS-MIB", "isisISAdjHoldTimer"),
        ("DC-ISIS-MIB", "isisISAdjNeighPriority"),
        ("DC-ISIS-MIB", "isisISAdjLastUpTime"),
        ("DC-ISIS-MIB", "isisISAdjAreaAddress"),
        ("DC-ISIS-MIB", "isisISAdjIPAddrType"),
        ("DC-ISIS-MIB", "isisISAdjIPAddrAddress"),
        ("DC-ISIS-MIB", "isisISAdjProtSuppLocalSupport"),
        ("DC-ISIS-MIB", "isisISAdjProtSuppBfdStatus"))
)
if mibBuilder.loadTexts:
    isisISAdjGroup.setStatus("current")

isisNotificationObjectGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 1, 4)
)
isisNotificationObjectGroup.setObjects(
      *(("DC-ISIS-MIB", "isisPduLspId"),
        ("DC-ISIS-MIB", "isisPduFragment"),
        ("DC-ISIS-MIB", "isisPduFieldLen"),
        ("DC-ISIS-MIB", "isisPduMaxAreaAddress"),
        ("DC-ISIS-MIB", "isisAdjState"),
        ("DC-ISIS-MIB", "isisErrorOffset"),
        ("DC-ISIS-MIB", "isisErrorTLVType"),
        ("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisNotificationAreaAddress"),
        ("DC-ISIS-MIB", "isisNotificationISAdjIndex"),
        ("DC-ISIS-MIB", "isisNotificationDisState"),
        ("DC-ISIS-MIB", "isisNotificationAttachedState"),
        ("DC-ISIS-MIB", "isisNotificationNeighSysID"),
        ("DC-ISIS-MIB", "isisNotificationMtId"))
)
if mibBuilder.loadTexts:
    isisNotificationObjectGroup.setStatus("current")

isisISPDUCounterGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 1, 6)
)
isisISPDUCounterGroup.setObjects(
      *(("DC-ISIS-MIB", "isisPacketCountIIHello"),
        ("DC-ISIS-MIB", "isisPacketCountISHello"),
        ("DC-ISIS-MIB", "isisPacketCountESHello"),
        ("DC-ISIS-MIB", "isisPacketCountLSP"),
        ("DC-ISIS-MIB", "isisPacketCountCSNP"),
        ("DC-ISIS-MIB", "isisPacketCountPSNP"),
        ("DC-ISIS-MIB", "isisPacketCountUnknown"))
)
if mibBuilder.loadTexts:
    isisISPDUCounterGroup.setStatus("current")

isisISIPRADestGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 1, 8)
)
isisISIPRADestGroup.setObjects(
      *(("DC-ISIS-MIB", "isisIPRANextHopType"),
        ("DC-ISIS-MIB", "isisIPRANextHop"),
        ("DC-ISIS-MIB", "isisIPRAType"),
        ("DC-ISIS-MIB", "isisIPRAExistState"),
        ("DC-ISIS-MIB", "isisIPRAAdminState"),
        ("DC-ISIS-MIB", "isisIPRAMetric"),
        ("DC-ISIS-MIB", "isisIPRAFullMetric"),
        ("DC-ISIS-MIB", "isisIPRAMetricType"),
        ("DC-ISIS-MIB", "isisIPRASNPAAddress"),
        ("DC-ISIS-MIB", "isisIPRASourceType"))
)
if mibBuilder.loadTexts:
    isisISIPRADestGroup.setStatus("current")

isisLSPGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 1, 9)
)
isisLSPGroup.setObjects(
      *(("DC-ISIS-MIB", "isisLSPSeq"),
        ("DC-ISIS-MIB", "isisLSPZeroLife"),
        ("DC-ISIS-MIB", "isisLSPChecksum"),
        ("DC-ISIS-MIB", "isisLSPLifetimeRemain"),
        ("DC-ISIS-MIB", "isisLSPPDULength"),
        ("DC-ISIS-MIB", "isisLSPAttributes"),
        ("DC-ISIS-MIB", "isisLSPTLVSeq"),
        ("DC-ISIS-MIB", "isisLSPTLVChecksum"),
        ("DC-ISIS-MIB", "isisLSPTLVType"),
        ("DC-ISIS-MIB", "isisLSPTLVLen"),
        ("DC-ISIS-MIB", "isisLSPTLVValue"))
)
if mibBuilder.loadTexts:
    isisLSPGroup.setStatus("current")

isisDCAdditionGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 1, 10)
)
isisDCAdditionGroup.setObjects(
      *(("DC-ISIS-MIB", "isisSysExistState"),
        ("DC-ISIS-MIB", "isisSysOperStatus"),
        ("DC-ISIS-MIB", "isisSysAllowAutoI3Config"),
        ("DC-ISIS-MIB", "isisSysCalcMaxDelay"),
        ("DC-ISIS-MIB", "isisSysCalcThrshUpdStart"),
        ("DC-ISIS-MIB", "isisSysCalcThrshUpdRestart"),
        ("DC-ISIS-MIB", "isisSysCalcThrshRestartLimit"),
        ("DC-ISIS-MIB", "isisSysCalcPauseFreq"),
        ("DC-ISIS-MIB", "isisSysCheckChecksums"),
        ("DC-ISIS-MIB", "isisSysZeroAgeLifetime"),
        ("DC-ISIS-MIB", "isisSysNumUpdPending"),
        ("DC-ISIS-MIB", "isisSysNumUpdMerged"),
        ("DC-ISIS-MIB", "isisSysNumCksumsPending"),
        ("DC-ISIS-MIB", "isisSysTEMetricPcntge"),
        ("DC-ISIS-MIB", "isisSysMaxBwidthPcntge"),
        ("DC-ISIS-MIB", "isisSysMaxResBwidthPcntge"),
        ("DC-ISIS-MIB", "isisSysUnresBwidthPcntge"),
        ("DC-ISIS-MIB", "isisSysMaxLSPBwidthPcntge"),
        ("DC-ISIS-MIB", "isisSysMinLSPBwidthPcntge"),
        ("DC-ISIS-MIB", "isisSysMTUSizePcntge"),
        ("DC-ISIS-MIB", "isisSysTERouterID"),
        ("DC-ISIS-MIB", "isisSysIPv6TERouterID"),
        ("DC-ISIS-MIB", "isisSysMaxExternalRoutes"),
        ("DC-ISIS-MIB", "isisSysMaxExternalRoutesAction"),
        ("DC-ISIS-MIB", "isisSysLspFullSuppress"),
        ("DC-ISIS-MIB", "isisSysLspFullSetDBOL"),
        ("DC-ISIS-MIB", "isisSysRestartHelpPeer"),
        ("DC-ISIS-MIB", "isisSysRestartActivationType"),
        ("DC-ISIS-MIB", "isisSysRestartAutoResetType"),
        ("DC-ISIS-MIB", "isisSysRestartAdjacencyWait"),
        ("DC-ISIS-MIB", "isisSysMaxRecoveryTime"),
        ("DC-ISIS-MIB", "isisSysClearStats"),
        ("DC-ISIS-MIB", "isisSysSetAttached"),
        ("DC-ISIS-MIB", "isisSysProtSupported"),
        ("DC-ISIS-MIB", "isisSysRestrictLanAdjsToSubnet"),
        ("DC-ISIS-MIB", "isisSysHostName"),
        ("DC-ISIS-MIB", "isisSysCalcSoonAfterCircChange"),
        ("DC-ISIS-MIB", "isisSysSendNotifications"),
        ("DC-ISIS-MIB", "isisSysEnableIgpShortcut"),
        ("DC-ISIS-MIB", "isisSysI3EntityIndex"),
        ("DC-ISIS-MIB", "isisSysRtmPurgeTime"),
        ("DC-ISIS-MIB", "isisRouterIPv6ID"),
        ("DC-ISIS-MIB", "isisSysLevelIPv6TEEnabled"),
        ("DC-ISIS-MIB", "isisSysLevelRestartT2Duration"),
        ("DC-ISIS-MIB", "isisSysLevelAuthUser"),
        ("DC-ISIS-MIB", "isisCircOperState"),
        ("DC-ISIS-MIB", "isisCircSdEntityIndex"),
        ("DC-ISIS-MIB", "isisCircDlBuffPoolSize"),
        ("DC-ISIS-MIB", "isisCircSdPDUBuffPoolSize"),
        ("DC-ISIS-MIB", "isisCircSdIndBuffPoolSize"),
        ("DC-ISIS-MIB", "isisCircDataLinkBlockSize"),
        ("DC-ISIS-MIB", "isisCircPhysicalAddress"),
        ("DC-ISIS-MIB", "isisCircManualOrAutomatic"),
        ("DC-ISIS-MIB", "isisCircT1TimerRunning"),
        ("DC-ISIS-MIB", "isisCircProtSupported"),
        ("DC-ISIS-MIB", "isisCircPtToPtOverLAN"),
        ("DC-ISIS-MIB", "isisCircProtBfdDesired"),
        ("DC-ISIS-MIB", "isisCircLevelStickyDIS"),
        ("DC-ISIS-MIB", "isisCircLevelAuthUser"),
        ("DC-ISIS-MIB", "isisCircLevelIDHostname"),
        ("DC-ISIS-MIB", "isisCircLevelDesISHostname"),
        ("DC-ISIS-MIB", "isisCircLevelMinLSPArrivalInt"),
        ("DC-ISIS-MIB", "isisSysStatPSNPError"),
        ("DC-ISIS-MIB", "isisSysStatCSNPError"),
        ("DC-ISIS-MIB", "isisSysStatLSPQueueLen"),
        ("DC-ISIS-MIB", "isisSysStatFragsRebuilt"),
        ("DC-ISIS-MIB", "isisSysStatLSPRexmits"),
        ("DC-ISIS-MIB", "isisSysStatLSPRegens"),
        ("DC-ISIS-MIB", "isisSysStatPurgesInitiated"),
        ("DC-ISIS-MIB", "isisSysStatLSPCount"),
        ("DC-ISIS-MIB", "isisSysStatPurgesIniLocal"),
        ("DC-ISIS-MIB", "isisSysStatPurgesIniRemote"),
        ("DC-ISIS-MIB", "isisSysStatPurgesIniRemSNP"),
        ("DC-ISIS-MIB", "isisSysStatPurgesIniRemExp"),
        ("DC-ISIS-MIB", "isisSysStatPurgesIniRemPrs"),
        ("DC-ISIS-MIB", "isisPacketCountDiscardedIIH"),
        ("DC-ISIS-MIB", "isisPacketCountDiscardedLSP"),
        ("DC-ISIS-MIB", "isisPacketCountDiscardedCSNP"),
        ("DC-ISIS-MIB", "isisPacketCountDiscardedPSNP"),
        ("DC-ISIS-MIB", "isisISAdjRestartCapable"),
        ("DC-ISIS-MIB", "isisISAdjPeerRestartState"),
        ("DC-ISIS-MIB", "isisISAdjSuppressed"),
        ("DC-ISIS-MIB", "isisISAdjNeighLanID"),
        ("DC-ISIS-MIB", "isisISAdjNeighHostname"),
        ("DC-ISIS-MIB", "isisISAdjNeighLanIDHostname"),
        ("DC-ISIS-MIB", "isisLSPIDHostname"),
        ("DC-ISIS-MIB", "isisLSPTLVHostname"),
        ("DC-ISIS-MIB", "isisPmSjJoinStatus"),
        ("DC-ISIS-MIB", "isisPmMjRowStatus"),
        ("DC-ISIS-MIB", "isisPmMjAdminStatus"),
        ("DC-ISIS-MIB", "isisPmMjOperStatus"),
        ("DC-ISIS-MIB", "isisPmMjJoinStatus"),
        ("DC-ISIS-MIB", "isisSdEntRowStatus"),
        ("DC-ISIS-MIB", "isisSdEntAdminStatus"),
        ("DC-ISIS-MIB", "isisSdEntOperStatus"),
        ("DC-ISIS-MIB", "isisSdEntMapHostnames"),
        ("DC-ISIS-MIB", "isisSdEntAuthSNPs"),
        ("DC-ISIS-MIB", "isisSdEntBfdProviderIndex"),
        ("DC-ISIS-MIB", "isisSdEntStopAdjDuplIDs"),
        ("DC-ISIS-MIB", "isisSdMjRowStatus"),
        ("DC-ISIS-MIB", "isisSdMjAdminStatus"),
        ("DC-ISIS-MIB", "isisSdMjOperStatus"),
        ("DC-ISIS-MIB", "isisSdMjEntityIndex"),
        ("DC-ISIS-MIB", "isisSdMjEntityType"),
        ("DC-ISIS-MIB", "isisSdMjJoinStatus"),
        ("DC-ISIS-MIB", "isisMtSysExistState"),
        ("DC-ISIS-MIB", "isisMtSysAdminState"),
        ("DC-ISIS-MIB", "isisMtSysOperState"),
        ("DC-ISIS-MIB", "isisMtSysProtSupported"),
        ("DC-ISIS-MIB", "isisMtSysDefaultActive"),
        ("DC-ISIS-MIB", "isisMtCircManExistState"),
        ("DC-ISIS-MIB", "isisMtCircManAdminState"),
        ("DC-ISIS-MIB", "isisMtCircManOperState"),
        ("DC-ISIS-MIB", "isisMtCircManL1WideMetric"),
        ("DC-ISIS-MIB", "isisMtCircManL2WideMetric"),
        ("DC-ISIS-MIB", "isisMtCircStatusOperState"),
        ("DC-ISIS-MIB", "isisMtCircStatusL1WideMetric"),
        ("DC-ISIS-MIB", "isisMtCircStatusL2WideMetric"),
        ("DC-ISIS-MIB", "isisISAdjMtSuppLocalSupport"),
        ("DC-ISIS-MIB", "isisIPRAMtId"),
        ("DC-ISIS-MIB", "isisPmMjSubAddrFamily"),
        ("DC-ISIS-MIB", "isisShortcutRemoteAddressType"),
        ("DC-ISIS-MIB", "isisShortcutRemoteAddress"),
        ("DC-ISIS-MIB", "isisShortcutMetricType"),
        ("DC-ISIS-MIB", "isisShortcutMetricValue"),
        ("DC-ISIS-MIB", "isisShortcutOperStatus"),
        ("DC-ISIS-MIB", "isisShortcutPendingDeletion"))
)
if mibBuilder.loadTexts:
    isisDCAdditionGroup.setStatus("current")


# Notification objects

isisDatabaseOverload = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 1)
)
isisDatabaseOverload.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisSysLevelOverloadState"))
)
if mibBuilder.loadTexts:
    isisDatabaseOverload.setStatus(
        "current"
    )

isisManualAddressDrops = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 2)
)
isisManualAddressDrops.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationAreaAddress"))
)
if mibBuilder.loadTexts:
    isisManualAddressDrops.setStatus(
        "current"
    )

isisIDLenMismatch = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 3)
)
isisIDLenMismatch.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisPduFieldLen"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisIDLenMismatch.setStatus(
        "current"
    )

isisMaxAreaAddressesMismatch = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 4)
)
isisMaxAreaAddressesMismatch.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisPduMaxAreaAddress"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisMaxAreaAddressesMismatch.setStatus(
        "current"
    )

isisOwnLSPPurge = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 5)
)
isisOwnLSPPurge.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisPduLspId"))
)
if mibBuilder.loadTexts:
    isisOwnLSPPurge.setStatus(
        "current"
    )

isisAreaMismatch = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 6)
)
isisAreaMismatch.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisAreaMismatch.setStatus(
        "current"
    )

isisRejectedAdjacency = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 7)
)
isisRejectedAdjacency.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisPduFragment"))
)
if mibBuilder.loadTexts:
    isisRejectedAdjacency.setStatus(
        "current"
    )

isisAdjacencyChange = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 8)
)
isisAdjacencyChange.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisPduLspId"),
        ("DC-ISIS-MIB", "isisAdjState"),
        ("DC-ISIS-MIB", "isisNotificationISAdjIndex"),
        ("DC-ISIS-MIB", "isisISAdjNeighSNPAAddress"))
)
if mibBuilder.loadTexts:
    isisAdjacencyChange.setStatus(
        "current"
    )

isisLSPErrorDetected = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 9)
)
isisLSPErrorDetected.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisPduLspId"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisPduFragment"),
        ("DC-ISIS-MIB", "isisErrorOffset"),
        ("DC-ISIS-MIB", "isisErrorTLVType"))
)
if mibBuilder.loadTexts:
    isisLSPErrorDetected.setStatus(
        "current"
    )

isisAttemptToExceedMaxSequence = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 10)
)
isisAttemptToExceedMaxSequence.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisPduLspId"))
)
if mibBuilder.loadTexts:
    isisAttemptToExceedMaxSequence.setStatus(
        "current"
    )

isisSequenceNumberSkip = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 11)
)
isisSequenceNumberSkip.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisPduLspId"))
)
if mibBuilder.loadTexts:
    isisSequenceNumberSkip.setStatus(
        "current"
    )

isisCircIndTable = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 12)
)
isisCircIndTable.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisCircExistState"),
        ("DC-ISIS-MIB", "isisCircAdminState"),
        ("DC-ISIS-MIB", "isisCircOperState"),
        ("DC-ISIS-MIB", "isisCircT1TimerRunning"),
        ("DC-ISIS-MIB", "isisCircLevel"))
)
if mibBuilder.loadTexts:
    isisCircIndTable.setStatus(
        "current"
    )

isisExtPassCircuitInd = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 13)
)
isisExtPassCircuitInd.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisCircExistState"),
        ("DC-ISIS-MIB", "isisCircAdminState"),
        ("DC-ISIS-MIB", "isisCircOperState"),
        ("DC-ISIS-MIB", "isisCircLevel"))
)
if mibBuilder.loadTexts:
    isisExtPassCircuitInd.setStatus(
        "current"
    )

isisOperStateChange = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 14)
)
isisOperStateChange.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisSysOperStatus"))
)
if mibBuilder.loadTexts:
    isisOperStateChange.setStatus(
        "current"
    )

isisLspAuthFailure = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 15)
)
isisLspAuthFailure.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisPduLspId"))
)
if mibBuilder.loadTexts:
    isisLspAuthFailure.setStatus(
        "current"
    )

isisHelloAuthFailure = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 16)
)
isisHelloAuthFailure.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisNotificationNeighSysID"))
)
if mibBuilder.loadTexts:
    isisHelloAuthFailure.setStatus(
        "current"
    )

isisAttachedStateChange = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 17)
)
isisAttachedStateChange.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationMtId"),
        ("DC-ISIS-MIB", "isisNotificationAttachedState"))
)
if mibBuilder.loadTexts:
    isisAttachedStateChange.setStatus(
        "current"
    )

isisDisChange = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 2, 0, 18)
)
isisDisChange.setObjects(
      *(("DC-ISIS-MIB", "isisNotificationSysInstance"),
        ("DC-ISIS-MIB", "isisNotificationSysLevelIndex"),
        ("DC-ISIS-MIB", "isisCircIfIndex"),
        ("DC-ISIS-MIB", "isisNotificationDisState"),
        ("DC-ISIS-MIB", "isisCircLevelDesIS"))
)
if mibBuilder.loadTexts:
    isisDisChange.setStatus(
        "current"
    )


# Notifications groups

isisNotificationGroup = NotificationGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 1, 5)
)
isisNotificationGroup.setObjects(
      *(("DC-ISIS-MIB", "isisDatabaseOverload"),
        ("DC-ISIS-MIB", "isisManualAddressDrops"),
        ("DC-ISIS-MIB", "isisIDLenMismatch"),
        ("DC-ISIS-MIB", "isisMaxAreaAddressesMismatch"),
        ("DC-ISIS-MIB", "isisOwnLSPPurge"),
        ("DC-ISIS-MIB", "isisAreaMismatch"),
        ("DC-ISIS-MIB", "isisRejectedAdjacency"),
        ("DC-ISIS-MIB", "isisAdjacencyChange"),
        ("DC-ISIS-MIB", "isisLSPErrorDetected"),
        ("DC-ISIS-MIB", "isisAttemptToExceedMaxSequence"),
        ("DC-ISIS-MIB", "isisSequenceNumberSkip"),
        ("DC-ISIS-MIB", "isisCircIndTable"),
        ("DC-ISIS-MIB", "isisExtPassCircuitInd"),
        ("DC-ISIS-MIB", "isisDisChange"),
        ("DC-ISIS-MIB", "isisOperStateChange"),
        ("DC-ISIS-MIB", "isisHelloAuthFailure"),
        ("DC-ISIS-MIB", "isisLspAuthFailure"),
        ("DC-ISIS-MIB", "isisAttachedStateChange"))
)
if mibBuilder.loadTexts:
    isisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

isisCompliance = ModuleCompliance(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    isisCompliance.setStatus(
        "current"
    )

isisAdvancedCompliance = ModuleCompliance(
    (1, 2, 826, 0, 1, 1578918, 5, 63, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    isisAdvancedCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-ISIS-MIB",
    **{"OSINSAddress": OSINSAddress,
       "SystemID": SystemID,
       "LinkStatePDUID": LinkStatePDUID,
       "AdminState": AdminState,
       "LSPBuffSize": LSPBuffSize,
       "LevelState": LevelState,
       "SupportedProtocol": SupportedProtocol,
       "DefaultMetric": DefaultMetric,
       "WideMetric": WideMetric,
       "FullMetric": FullMetric,
       "MetricType": MetricType,
       "MetricStyle": MetricStyle,
       "ISLevel": ISLevel,
       "IsisAdjLevel": IsisAdjLevel,
       "IsisPDUHeader": IsisPDUHeader,
       "CircuitID": CircuitID,
       "ISPriority": ISPriority,
       "Unsigned16TC": Unsigned16TC,
       "Unsigned8TC": Unsigned8TC,
       "IsisAdminStatus": IsisAdminStatus,
       "IsisOperStatus": IsisOperStatus,
       "IsisMjStatus": IsisMjStatus,
       "IsisSjStatus": IsisSjStatus,
       "IsisPmInterfaceId": IsisPmInterfaceId,
       "IsisSdInterfaceId": IsisSdInterfaceId,
       "IsisSdEntityType": IsisSdEntityType,
       "IsisAddrType": IsisAddrType,
       "IsisAddrTypeBits": IsisAddrTypeBits,
       "IsisSysRestartType": IsisSysRestartType,
       "dcIsisMib": dcIsisMib,
       "isisObjects": isisObjects,
       "isisSystem": isisSystem,
       "isisSysTable": isisSysTable,
       "isisSysEntry": isisSysEntry,
       "isisSysInstance": isisSysInstance,
       "isisSysVersion": isisSysVersion,
       "isisSysType": isisSysType,
       "isisSysID": isisSysID,
       "isisSysMaxPathSplits": isisSysMaxPathSplits,
       "isisSysMaxLSPGenInt": isisSysMaxLSPGenInt,
       "isisSysPollESHelloRate": isisSysPollESHelloRate,
       "isisSysWaitTime": isisSysWaitTime,
       "isisSysAdminState": isisSysAdminState,
       "isisSysL2toL1Leaking": isisSysL2toL1Leaking,
       "isisSysMaxAge": isisSysMaxAge,
       "isisSysReceiveLSPBufferSize": isisSysReceiveLSPBufferSize,
       "isisSysExistState": isisSysExistState,
       "isisSysOperStatus": isisSysOperStatus,
       "isisSysAllowAutoI3Config": isisSysAllowAutoI3Config,
       "isisSysCalcMaxDelay": isisSysCalcMaxDelay,
       "isisSysCalcThrshUpdStart": isisSysCalcThrshUpdStart,
       "isisSysCalcThrshUpdRestart": isisSysCalcThrshUpdRestart,
       "isisSysCalcThrshRestartLimit": isisSysCalcThrshRestartLimit,
       "isisSysCalcPauseFreq": isisSysCalcPauseFreq,
       "isisSysCheckChecksums": isisSysCheckChecksums,
       "isisSysZeroAgeLifetime": isisSysZeroAgeLifetime,
       "isisSysNumUpdPending": isisSysNumUpdPending,
       "isisSysNumUpdMerged": isisSysNumUpdMerged,
       "isisSysNumCksumsPending": isisSysNumCksumsPending,
       "isisSysTEMetricPcntge": isisSysTEMetricPcntge,
       "isisSysMaxBwidthPcntge": isisSysMaxBwidthPcntge,
       "isisSysMaxResBwidthPcntge": isisSysMaxResBwidthPcntge,
       "isisSysUnresBwidthPcntge": isisSysUnresBwidthPcntge,
       "isisSysMaxLSPBwidthPcntge": isisSysMaxLSPBwidthPcntge,
       "isisSysMinLSPBwidthPcntge": isisSysMinLSPBwidthPcntge,
       "isisSysMTUSizePcntge": isisSysMTUSizePcntge,
       "isisSysTERouterID": isisSysTERouterID,
       "isisSysIPv6TERouterID": isisSysIPv6TERouterID,
       "isisSysMaxExternalRoutes": isisSysMaxExternalRoutes,
       "isisSysMaxExternalRoutesAction": isisSysMaxExternalRoutesAction,
       "isisSysLspFullSuppress": isisSysLspFullSuppress,
       "isisSysLspFullSetDBOL": isisSysLspFullSetDBOL,
       "isisSysRestartHelpPeer": isisSysRestartHelpPeer,
       "isisSysRestartActivationType": isisSysRestartActivationType,
       "isisSysRestartAutoResetType": isisSysRestartAutoResetType,
       "isisSysRestartAdjacencyWait": isisSysRestartAdjacencyWait,
       "isisSysMaxRecoveryTime": isisSysMaxRecoveryTime,
       "isisSysClearStats": isisSysClearStats,
       "isisSysSetAttached": isisSysSetAttached,
       "isisSysProtSupported": isisSysProtSupported,
       "isisSysRestrictLanAdjsToSubnet": isisSysRestrictLanAdjsToSubnet,
       "isisSysHostName": isisSysHostName,
       "isisSysCalcSoonAfterCircChange": isisSysCalcSoonAfterCircChange,
       "isisSysSendNotifications": isisSysSendNotifications,
       "isisSysEnableIgpShortcut": isisSysEnableIgpShortcut,
       "isisSysI3EntityIndex": isisSysI3EntityIndex,
       "isisSysRtmPurgeTime": isisSysRtmPurgeTime,
       "isisManAreaAddrTable": isisManAreaAddrTable,
       "isisManAreaAddrEntry": isisManAreaAddrEntry,
       "isisManAreaAddr": isisManAreaAddr,
       "isisManAreaAddrExistState": isisManAreaAddrExistState,
       "isisAreaAddrTable": isisAreaAddrTable,
       "isisAreaAddrEntry": isisAreaAddrEntry,
       "isisAreaAddr": isisAreaAddr,
       "isisAreaAddrInLSP": isisAreaAddrInLSP,
       "isisSummAddrTable": isisSummAddrTable,
       "isisSummAddrEntry": isisSummAddrEntry,
       "isisSummAddressType": isisSummAddressType,
       "isisSummAddress": isisSummAddress,
       "isisSummAddrPrefixLen": isisSummAddrPrefixLen,
       "isisSummAddrExistState": isisSummAddrExistState,
       "isisSummAddrMetric": isisSummAddrMetric,
       "isisSummAddrFullMetric": isisSummAddrFullMetric,
       "isisSummAddrMtId": isisSummAddrMtId,
       "isisRedistributeAddrTable": isisRedistributeAddrTable,
       "isisRedistributeAddrEntry": isisRedistributeAddrEntry,
       "isisRedistributeAddrType": isisRedistributeAddrType,
       "isisRedistributeAddrAddress": isisRedistributeAddrAddress,
       "isisRedistributeAddrPrefixLen": isisRedistributeAddrPrefixLen,
       "isisRedistributeAddrExistState": isisRedistributeAddrExistState,
       "isisRedistributeAddrMtId": isisRedistributeAddrMtId,
       "isisRouterTable": isisRouterTable,
       "isisRouterEntry": isisRouterEntry,
       "isisRouterSysID": isisRouterSysID,
       "isisRouterLevel": isisRouterLevel,
       "isisRouterHostName": isisRouterHostName,
       "isisRouterID": isisRouterID,
       "isisRouterIPv6ID": isisRouterIPv6ID,
       "isisMtSysTable": isisMtSysTable,
       "isisMtSysEntry": isisMtSysEntry,
       "isisMtSysMtId": isisMtSysMtId,
       "isisMtSysExistState": isisMtSysExistState,
       "isisMtSysAdminState": isisMtSysAdminState,
       "isisMtSysOperState": isisMtSysOperState,
       "isisMtSysProtSupported": isisMtSysProtSupported,
       "isisMtSysDefaultActive": isisMtSysDefaultActive,
       "isisSysLevel": isisSysLevel,
       "isisSysLevelTable": isisSysLevelTable,
       "isisSysLevelEntry": isisSysLevelEntry,
       "isisSysLevelIndex": isisSysLevelIndex,
       "isisSysLevelOrigLSPBuffSize": isisSysLevelOrigLSPBuffSize,
       "isisSysLevelMinLSPGenInt": isisSysLevelMinLSPGenInt,
       "isisSysLevelOverloadState": isisSysLevelOverloadState,
       "isisSysLevelSetOverload": isisSysLevelSetOverload,
       "isisSysLevelSetOverloadUntil": isisSysLevelSetOverloadUntil,
       "isisSysLevelMetricStyle": isisSysLevelMetricStyle,
       "isisSysLevelSPFConsiders": isisSysLevelSPFConsiders,
       "isisSysLevelTEEnabled": isisSysLevelTEEnabled,
       "isisSysLevelIPv6TEEnabled": isisSysLevelIPv6TEEnabled,
       "isisSysLevelRestartT2Duration": isisSysLevelRestartT2Duration,
       "isisSysLevelAuthUser": isisSysLevelAuthUser,
       "isisCirc": isisCirc,
       "isisCircTable": isisCircTable,
       "isisCircEntry": isisCircEntry,
       "isisCircIndex": isisCircIndex,
       "isisCircIfIndex": isisCircIfIndex,
       "isisCircIfSubIndex": isisCircIfSubIndex,
       "isisCircAdminState": isisCircAdminState,
       "isisCircExistState": isisCircExistState,
       "isisCircType": isisCircType,
       "isisCircExtDomain": isisCircExtDomain,
       "isisCircLevel": isisCircLevel,
       "isisCircPassiveCircuit": isisCircPassiveCircuit,
       "isisCircMeshGroupEnabled": isisCircMeshGroupEnabled,
       "isisCircMeshGroup": isisCircMeshGroup,
       "isisCircSmallHellos": isisCircSmallHellos,
       "isisCircLastUpTime": isisCircLastUpTime,
       "isisCirc3WayEnabled": isisCirc3WayEnabled,
       "isisCircExtendedCircID": isisCircExtendedCircID,
       "isisCircOperState": isisCircOperState,
       "isisCircSdEntityIndex": isisCircSdEntityIndex,
       "isisCircDlBuffPoolSize": isisCircDlBuffPoolSize,
       "isisCircSdPDUBuffPoolSize": isisCircSdPDUBuffPoolSize,
       "isisCircSdIndBuffPoolSize": isisCircSdIndBuffPoolSize,
       "isisCircDataLinkBlockSize": isisCircDataLinkBlockSize,
       "isisCircPhysicalAddress": isisCircPhysicalAddress,
       "isisCircManualOrAutomatic": isisCircManualOrAutomatic,
       "isisCircT1TimerRunning": isisCircT1TimerRunning,
       "isisCircProtSupported": isisCircProtSupported,
       "isisCircPtToPtOverLAN": isisCircPtToPtOverLAN,
       "isisCircProtBfdDesired": isisCircProtBfdDesired,
       "isisCircIPAddrTable": isisCircIPAddrTable,
       "isisCircIPAddrEntry": isisCircIPAddrEntry,
       "isisCircIPAddrManOrAuto": isisCircIPAddrManOrAuto,
       "isisCircIPAddrIndex": isisCircIPAddrIndex,
       "isisCircIPAddrRowStatus": isisCircIPAddrRowStatus,
       "isisCircIPAddrAdminState": isisCircIPAddrAdminState,
       "isisCircIPAddrAddressType": isisCircIPAddrAddressType,
       "isisCircIPAddrAddress": isisCircIPAddrAddress,
       "isisCircIPAddrInLSP": isisCircIPAddrInLSP,
       "isisMtCircManConfigTable": isisMtCircManConfigTable,
       "isisMtCircManConfigEntry": isisMtCircManConfigEntry,
       "isisMtCircManMtId": isisMtCircManMtId,
       "isisMtCircManExistState": isisMtCircManExistState,
       "isisMtCircManAdminState": isisMtCircManAdminState,
       "isisMtCircManOperState": isisMtCircManOperState,
       "isisMtCircManL1WideMetric": isisMtCircManL1WideMetric,
       "isisMtCircManL2WideMetric": isisMtCircManL2WideMetric,
       "isisMtCircStatusTable": isisMtCircStatusTable,
       "isisMtCircStatusEntry": isisMtCircStatusEntry,
       "isisMtCircStatusMtId": isisMtCircStatusMtId,
       "isisMtCircStatusOperState": isisMtCircStatusOperState,
       "isisMtCircStatusL1WideMetric": isisMtCircStatusL1WideMetric,
       "isisMtCircStatusL2WideMetric": isisMtCircStatusL2WideMetric,
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
       "isisCircLevelStickyDIS": isisCircLevelStickyDIS,
       "isisCircLevelAuthUser": isisCircLevelAuthUser,
       "isisCircLevelIDHostname": isisCircLevelIDHostname,
       "isisCircLevelDesISHostname": isisCircLevelDesISHostname,
       "isisCircLevelMinLSPArrivalInt": isisCircLevelMinLSPArrivalInt,
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
       "isisSysStatLSPError": isisSysStatLSPError,
       "isisSysStatCSNPError": isisSysStatCSNPError,
       "isisSysStatPSNPError": isisSysStatPSNPError,
       "isisSysStatLSPQueueLen": isisSysStatLSPQueueLen,
       "isisSysStatFragsRebuilt": isisSysStatFragsRebuilt,
       "isisSysStatLSPRexmits": isisSysStatLSPRexmits,
       "isisSysStatLSPRegens": isisSysStatLSPRegens,
       "isisSysStatPurgesInitiated": isisSysStatPurgesInitiated,
       "isisSysStatLSPCount": isisSysStatLSPCount,
       "isisSysStatPurgesIniLocal": isisSysStatPurgesIniLocal,
       "isisSysStatPurgesIniRemote": isisSysStatPurgesIniRemote,
       "isisSysStatPurgesIniRemSNP": isisSysStatPurgesIniRemSNP,
       "isisSysStatPurgesIniRemExp": isisSysStatPurgesIniRemExp,
       "isisSysStatPurgesIniRemPrs": isisSysStatPurgesIniRemPrs,
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
       "isisPacketCountDiscardedIIH": isisPacketCountDiscardedIIH,
       "isisPacketCountDiscardedLSP": isisPacketCountDiscardedLSP,
       "isisPacketCountDiscardedCSNP": isisPacketCountDiscardedCSNP,
       "isisPacketCountDiscardedPSNP": isisPacketCountDiscardedPSNP,
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
       "isisISAdjRestartCapable": isisISAdjRestartCapable,
       "isisISAdjPeerRestartState": isisISAdjPeerRestartState,
       "isisISAdjSuppressed": isisISAdjSuppressed,
       "isisISAdjNeighLanID": isisISAdjNeighLanID,
       "isisISAdjNeighHostname": isisISAdjNeighHostname,
       "isisISAdjNeighLanIDHostname": isisISAdjNeighLanIDHostname,
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
       "isisISAdjProtSuppLocalSupport": isisISAdjProtSuppLocalSupport,
       "isisISAdjProtSuppBfdStatus": isisISAdjProtSuppBfdStatus,
       "isisISAdjMtSupportedTable": isisISAdjMtSupportedTable,
       "isisISAdjMtSupportedEntry": isisISAdjMtSupportedEntry,
       "isisISAdjMtSuppMtId": isisISAdjMtSuppMtId,
       "isisISAdjMtSuppLocalSupport": isisISAdjMtSuppLocalSupport,
       "isisReachAddr": isisReachAddr,
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
       "isisIPRAMtId": isisIPRAMtId,
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
       "isisLSPIDHostname": isisLSPIDHostname,
       "isisLSPTLVTable": isisLSPTLVTable,
       "isisLSPTLVEntry": isisLSPTLVEntry,
       "isisLSPTLVIndex": isisLSPTLVIndex,
       "isisLSPTLVSeq": isisLSPTLVSeq,
       "isisLSPTLVChecksum": isisLSPTLVChecksum,
       "isisLSPTLVType": isisLSPTLVType,
       "isisLSPTLVLen": isisLSPTLVLen,
       "isisLSPTLVValue": isisLSPTLVValue,
       "isisLSPTLVHostname": isisLSPTLVHostname,
       "isisNotification": isisNotification,
       "isisNotificationEntry": isisNotificationEntry,
       "isisPduLspId": isisPduLspId,
       "isisPduFragment": isisPduFragment,
       "isisPduFieldLen": isisPduFieldLen,
       "isisPduMaxAreaAddress": isisPduMaxAreaAddress,
       "isisAdjState": isisAdjState,
       "isisErrorOffset": isisErrorOffset,
       "isisErrorTLVType": isisErrorTLVType,
       "isisNotificationSysInstance": isisNotificationSysInstance,
       "isisNotificationSysLevelIndex": isisNotificationSysLevelIndex,
       "isisNotificationAreaAddress": isisNotificationAreaAddress,
       "isisNotificationISAdjIndex": isisNotificationISAdjIndex,
       "isisNotificationDisState": isisNotificationDisState,
       "isisNotificationAttachedState": isisNotificationAttachedState,
       "isisNotificationNeighSysID": isisNotificationNeighSysID,
       "isisNotificationMtId": isisNotificationMtId,
       "isisPmObjects": isisPmObjects,
       "isisPmSjTable": isisPmSjTable,
       "isisPmSjEntry": isisPmSjEntry,
       "isisPmSjInterface": isisPmSjInterface,
       "isisPmSjMasterEntity": isisPmSjMasterEntity,
       "isisPmSjJoinStatus": isisPmSjJoinStatus,
       "isisPmMjTable": isisPmMjTable,
       "isisPmMjEntry": isisPmMjEntry,
       "isisPmMjInterface": isisPmMjInterface,
       "isisPmMjSlaveEntity": isisPmMjSlaveEntity,
       "isisPmMjAddrType": isisPmMjAddrType,
       "isisPmMjRowStatus": isisPmMjRowStatus,
       "isisPmMjAdminStatus": isisPmMjAdminStatus,
       "isisPmMjOperStatus": isisPmMjOperStatus,
       "isisPmMjJoinStatus": isisPmMjJoinStatus,
       "isisPmMjMtId": isisPmMjMtId,
       "isisPmMjSubAddrFamily": isisPmMjSubAddrFamily,
       "isisIgpShortcutTable": isisIgpShortcutTable,
       "isisIgpShortcutEntry": isisIgpShortcutEntry,
       "isisShortcutIfIndex": isisShortcutIfIndex,
       "isisShortcutRemoteAddressType": isisShortcutRemoteAddressType,
       "isisShortcutRemoteAddress": isisShortcutRemoteAddress,
       "isisShortcutMetricType": isisShortcutMetricType,
       "isisShortcutMetricValue": isisShortcutMetricValue,
       "isisShortcutOperStatus": isisShortcutOperStatus,
       "isisShortcutPendingDeletion": isisShortcutPendingDeletion,
       "isisSdObjects": isisSdObjects,
       "isisSdEntTable": isisSdEntTable,
       "isisSdEntEntry": isisSdEntEntry,
       "isisSdEntIndex": isisSdEntIndex,
       "isisSdEntRowStatus": isisSdEntRowStatus,
       "isisSdEntAdminStatus": isisSdEntAdminStatus,
       "isisSdEntOperStatus": isisSdEntOperStatus,
       "isisSdEntMapHostnames": isisSdEntMapHostnames,
       "isisSdEntAuthSNPs": isisSdEntAuthSNPs,
       "isisSdEntBfdProviderIndex": isisSdEntBfdProviderIndex,
       "isisSdEntStopAdjDuplIDs": isisSdEntStopAdjDuplIDs,
       "isisSdMjTable": isisSdMjTable,
       "isisSdMjEntry": isisSdMjEntry,
       "isisSdMjInterface": isisSdMjInterface,
       "isisSdMjRowStatus": isisSdMjRowStatus,
       "isisSdMjAdminStatus": isisSdMjAdminStatus,
       "isisSdMjOperStatus": isisSdMjOperStatus,
       "isisSdMjEntityIndex": isisSdMjEntityIndex,
       "isisSdMjEntityType": isisSdMjEntityType,
       "isisSdMjJoinStatus": isisSdMjJoinStatus,
       "isisNotifications": isisNotifications,
       "isisTrapPrefix": isisTrapPrefix,
       "isisDatabaseOverload": isisDatabaseOverload,
       "isisManualAddressDrops": isisManualAddressDrops,
       "isisIDLenMismatch": isisIDLenMismatch,
       "isisMaxAreaAddressesMismatch": isisMaxAreaAddressesMismatch,
       "isisOwnLSPPurge": isisOwnLSPPurge,
       "isisAreaMismatch": isisAreaMismatch,
       "isisRejectedAdjacency": isisRejectedAdjacency,
       "isisAdjacencyChange": isisAdjacencyChange,
       "isisLSPErrorDetected": isisLSPErrorDetected,
       "isisAttemptToExceedMaxSequence": isisAttemptToExceedMaxSequence,
       "isisSequenceNumberSkip": isisSequenceNumberSkip,
       "isisCircIndTable": isisCircIndTable,
       "isisExtPassCircuitInd": isisExtPassCircuitInd,
       "isisOperStateChange": isisOperStateChange,
       "isisLspAuthFailure": isisLspAuthFailure,
       "isisHelloAuthFailure": isisHelloAuthFailure,
       "isisAttachedStateChange": isisAttachedStateChange,
       "isisDisChange": isisDisChange,
       "isisConformance": isisConformance,
       "isisGroups": isisGroups,
       "isisSystemGroup": isisSystemGroup,
       "isisCircuitGroup": isisCircuitGroup,
       "isisISAdjGroup": isisISAdjGroup,
       "isisNotificationObjectGroup": isisNotificationObjectGroup,
       "isisNotificationGroup": isisNotificationGroup,
       "isisISPDUCounterGroup": isisISPDUCounterGroup,
       "isisISIPRADestGroup": isisISIPRADestGroup,
       "isisLSPGroup": isisLSPGroup,
       "isisDCAdditionGroup": isisDCAdditionGroup,
       "isisCompliances": isisCompliances,
       "isisCompliance": isisCompliance,
       "isisAdvancedCompliance": isisAdvancedCompliance}
)
