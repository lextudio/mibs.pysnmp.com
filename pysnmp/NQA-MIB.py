# SNMP MIB module (NQA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NQA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:20 2024
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

(HWDot1agCfmEgressActionFieldValue,
 HWDot1agCfmIngressActionFieldValue,
 HWDot1agCfmRelayActionFieldValue) = mibBuilder.importSymbols(
    "HUAWEI-ETHOAM-MIB",
    "HWDot1agCfmEgressActionFieldValue",
    "HWDot1agCfmIngressActionFieldValue",
    "HWDot1agCfmRelayActionFieldValue")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(Dot1agCfmMaintAssocName,
 Dot1agCfmMaintDomainName,
 Dot1agCfmMepIdOrZero) = mibBuilder.importSymbols(
    "IEEE802171-CFM-MIB",
    "Dot1agCfmMaintAssocName",
    "Dot1agCfmMaintDomainName",
    "Dot1agCfmMepIdOrZero")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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
 NotificationGroup,
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
    "NotificationGroup",
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

nqa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NqaType(Integer32, TextualConvention):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("dhcpAppl", 12),
          ("dlswAppl", 13),
          ("dnsAppl", 11),
          ("ftpAppl", 4),
          ("gmacping", 29),
          ("gmactrace", 30),
          ("httpAppl", 3),
          ("icmpAppl", 6),
          ("icmpJitter", 22),
          ("jitterAppl", 5),
          ("lspJitter", 20),
          ("lspPing", 9),
          ("lspTraceRoute", 10),
          ("mPing", 16),
          ("mTracert", 17),
          ("macPing", 18),
          ("macTunnelPing", 19),
          ("mactrace", 31),
          ("pathJitter", 23),
          ("pathMtu", 21),
          ("pppoe", 24),
          ("pwe3Ping", 14),
          ("pwe3Tracert", 15),
          ("snmpAppl", 7),
          ("tcpConnect", 1),
          ("traceRoute", 8),
          ("udpEcho", 2),
          ("unknown", 0),
          ("vplsMTrace", 28),
          ("vplsmPing", 25),
          ("vplsmacPing", 26),
          ("vplsmacTrace", 27),
          ("vplspwping", 32),
          ("vplspwtrace", 33))
    )



class EnableValue(Integer32, TextualConvention):
    status = "current"
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



class NqaDistanceNodeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 1),
          ("mepID", 2))
    )



class HWLldpPortIdSubtype(Integer32, TextualConvention):
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
        *(("agentCircuitId", 6),
          ("interfaceAlias", 1),
          ("interfaceName", 5),
          ("local", 7),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("portComponent", 2))
    )



class HWLldpPortId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class NqaOperation(Integer32, TextualConvention):
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
        *(("ftpGet", 4),
          ("ftpPut", 5),
          ("httpGet", 2),
          ("httpPost", 3),
          ("noOperation", 1))
    )



# MIB Managed Objects in the order of their OIDs

_NqaBase_ObjectIdentity = ObjectIdentity
nqaBase = _NqaBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1)
)
_NqaVersion_Type = DisplayString
_NqaVersion_Object = MibScalar
nqaVersion = _NqaVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 1),
    _NqaVersion_Type()
)
nqaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVersion.setStatus("current")
_NqaEnable_Type = EnableValue
_NqaEnable_Object = MibScalar
nqaEnable = _NqaEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 2),
    _NqaEnable_Type()
)
nqaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaEnable.setStatus("current")
_NqaReset_Type = EnableValue
_NqaReset_Object = MibScalar
nqaReset = _NqaReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 3),
    _NqaReset_Type()
)
nqaReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaReset.setStatus("current")
_NqaTimeOfLastSetError_Type = DateAndTime
_NqaTimeOfLastSetError_Object = MibScalar
nqaTimeOfLastSetError = _NqaTimeOfLastSetError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 4),
    _NqaTimeOfLastSetError_Type()
)
nqaTimeOfLastSetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaTimeOfLastSetError.setStatus("current")
_NqaLastSetError_Type = DisplayString
_NqaLastSetError_Object = MibScalar
nqaLastSetError = _NqaLastSetError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 5),
    _NqaLastSetError_Type()
)
nqaLastSetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaLastSetError.setStatus("current")
_NqaNumOfCurrentCtrlEntry_Type = Integer32
_NqaNumOfCurrentCtrlEntry_Object = MibScalar
nqaNumOfCurrentCtrlEntry = _NqaNumOfCurrentCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 6),
    _NqaNumOfCurrentCtrlEntry_Type()
)
nqaNumOfCurrentCtrlEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaNumOfCurrentCtrlEntry.setStatus("current")
_NqaMaxConcurrentRequests_Type = Unsigned32
_NqaMaxConcurrentRequests_Object = MibScalar
nqaMaxConcurrentRequests = _NqaMaxConcurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 7),
    _NqaMaxConcurrentRequests_Type()
)
nqaMaxConcurrentRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaMaxConcurrentRequests.setStatus("current")
if mibBuilder.loadTexts:
    nqaMaxConcurrentRequests.setUnits("requests")
_NqaMaxNumOfRequests_Type = Unsigned32
_NqaMaxNumOfRequests_Object = MibScalar
nqaMaxNumOfRequests = _NqaMaxNumOfRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 8),
    _NqaMaxNumOfRequests_Type()
)
nqaMaxNumOfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMaxNumOfRequests.setStatus("current")
if mibBuilder.loadTexts:
    nqaMaxNumOfRequests.setUnits("requests")
_NqaJitterVersion_Type = Integer32
_NqaJitterVersion_Object = MibScalar
nqaJitterVersion = _NqaJitterVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 9),
    _NqaJitterVersion_Type()
)
nqaJitterVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaJitterVersion.setStatus("current")


class _NqaSupportTestType_Type(Bits):
    """Custom type nqaSupportTestType based on Bits"""
    namedValues = NamedValues(
        *(("dhcp", 11),
          ("dlsw", 12),
          ("dns", 10),
          ("ftp", 4),
          ("gmacping", 28),
          ("gmactrace", 29),
          ("http", 3),
          ("icmp", 0),
          ("icmpJitter", 20),
          ("jitter", 5),
          ("lspJitter", 19),
          ("lspPing", 8),
          ("lspTrace", 9),
          ("mPing", 15),
          ("mTrace", 16),
          ("macPing", 17),
          ("macTunnelPing", 18),
          ("mactrace", 30),
          ("pathJitter", 21),
          ("pathMtu", 22),
          ("pppoe", 23),
          ("pwe3Ping", 13),
          ("pwe3Trace", 14),
          ("snmp", 6),
          ("tcp", 1),
          ("trace", 7),
          ("udp", 2),
          ("vplsMTrace", 27),
          ("vplsmPing", 24),
          ("vplsmacPing", 25),
          ("vplsmacTrace", 26),
          ("vplspwping", 31),
          ("vplspwtrace", 32))
    )

_NqaSupportTestType_Type.__name__ = "Bits"
_NqaSupportTestType_Object = MibScalar
nqaSupportTestType = _NqaSupportTestType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 10),
    _NqaSupportTestType_Type()
)
nqaSupportTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaSupportTestType.setStatus("current")


class _NqaSupportServerType_Type(Bits):
    """Custom type nqaSupportServerType based on Bits"""
    namedValues = NamedValues(
        *(("icmpServer", 2),
          ("tcpServer", 0),
          ("udpServer", 1))
    )

_NqaSupportServerType_Type.__name__ = "Bits"
_NqaSupportServerType_Object = MibScalar
nqaSupportServerType = _NqaSupportServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 1, 11),
    _NqaSupportServerType_Type()
)
nqaSupportServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaSupportServerType.setStatus("current")
_NqaCtrl_ObjectIdentity = ObjectIdentity
nqaCtrl = _NqaCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2)
)
_NqaAdminCtrlTable_Object = MibTable
nqaAdminCtrlTable = _NqaAdminCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1)
)
if mibBuilder.loadTexts:
    nqaAdminCtrlTable.setStatus("current")
_NqaAdminCtrlEntry_Object = MibTableRow
nqaAdminCtrlEntry = _NqaAdminCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1)
)
nqaAdminCtrlEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
)
if mibBuilder.loadTexts:
    nqaAdminCtrlEntry.setStatus("current")


class _NqaAdminCtrlOwnerIndex_Type(SnmpAdminString):
    """Custom type nqaAdminCtrlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NqaAdminCtrlOwnerIndex_Type.__name__ = "SnmpAdminString"
_NqaAdminCtrlOwnerIndex_Object = MibTableColumn
nqaAdminCtrlOwnerIndex = _NqaAdminCtrlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1, 1),
    _NqaAdminCtrlOwnerIndex_Type()
)
nqaAdminCtrlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaAdminCtrlOwnerIndex.setStatus("current")


class _NqaAdminCtrlTestName_Type(SnmpAdminString):
    """Custom type nqaAdminCtrlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NqaAdminCtrlTestName_Type.__name__ = "SnmpAdminString"
_NqaAdminCtrlTestName_Object = MibTableColumn
nqaAdminCtrlTestName = _NqaAdminCtrlTestName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1, 2),
    _NqaAdminCtrlTestName_Type()
)
nqaAdminCtrlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaAdminCtrlTestName.setStatus("current")
_NqaAdminCtrlTag_Type = DisplayString
_NqaAdminCtrlTag_Object = MibTableColumn
nqaAdminCtrlTag = _NqaAdminCtrlTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1, 3),
    _NqaAdminCtrlTag_Type()
)
nqaAdminCtrlTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAdminCtrlTag.setStatus("current")
_NqaAdminCtrlType_Type = NqaType
_NqaAdminCtrlType_Object = MibTableColumn
nqaAdminCtrlType = _NqaAdminCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1, 4),
    _NqaAdminCtrlType_Type()
)
nqaAdminCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAdminCtrlType.setStatus("current")


class _NqaAdminCtrlFrequency_Type(Integer32):
    """Custom type nqaAdminCtrlFrequency based on Integer32"""
    defaultValue = 0


_NqaAdminCtrlFrequency_Object = MibTableColumn
nqaAdminCtrlFrequency = _NqaAdminCtrlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1, 5),
    _NqaAdminCtrlFrequency_Type()
)
nqaAdminCtrlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAdminCtrlFrequency.setStatus("current")
if mibBuilder.loadTexts:
    nqaAdminCtrlFrequency.setUnits("seconds")


class _NqaAdminCtrlTimeOut_Type(Integer32):
    """Custom type nqaAdminCtrlTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_NqaAdminCtrlTimeOut_Type.__name__ = "Integer32"
_NqaAdminCtrlTimeOut_Object = MibTableColumn
nqaAdminCtrlTimeOut = _NqaAdminCtrlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1, 6),
    _NqaAdminCtrlTimeOut_Type()
)
nqaAdminCtrlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAdminCtrlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    nqaAdminCtrlTimeOut.setUnits("seconds")


class _NqaAdminCtrlThreshold1_Type(Integer32):
    """Custom type nqaAdminCtrlThreshold1 based on Integer32"""
    defaultValue = 0


_NqaAdminCtrlThreshold1_Object = MibTableColumn
nqaAdminCtrlThreshold1 = _NqaAdminCtrlThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1, 7),
    _NqaAdminCtrlThreshold1_Type()
)
nqaAdminCtrlThreshold1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAdminCtrlThreshold1.setStatus("current")
if mibBuilder.loadTexts:
    nqaAdminCtrlThreshold1.setUnits("milliseconds")


class _NqaAdminCtrlThreshold2_Type(Integer32):
    """Custom type nqaAdminCtrlThreshold2 based on Integer32"""
    defaultValue = 0


_NqaAdminCtrlThreshold2_Object = MibTableColumn
nqaAdminCtrlThreshold2 = _NqaAdminCtrlThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1, 8),
    _NqaAdminCtrlThreshold2_Type()
)
nqaAdminCtrlThreshold2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAdminCtrlThreshold2.setStatus("current")
if mibBuilder.loadTexts:
    nqaAdminCtrlThreshold2.setUnits("milliseconds")


class _NqaAdminCtrlThreshold3_Type(Integer32):
    """Custom type nqaAdminCtrlThreshold3 based on Integer32"""
    defaultValue = 0


_NqaAdminCtrlThreshold3_Object = MibTableColumn
nqaAdminCtrlThreshold3 = _NqaAdminCtrlThreshold3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1, 9),
    _NqaAdminCtrlThreshold3_Type()
)
nqaAdminCtrlThreshold3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAdminCtrlThreshold3.setStatus("current")
if mibBuilder.loadTexts:
    nqaAdminCtrlThreshold3.setUnits("milliseconds")
_NqaAdminCtrlStatus_Type = RowStatus
_NqaAdminCtrlStatus_Object = MibTableColumn
nqaAdminCtrlStatus = _NqaAdminCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 1, 1, 10),
    _NqaAdminCtrlStatus_Type()
)
nqaAdminCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAdminCtrlStatus.setStatus("current")
_NqaAdminParaTable_Object = MibTable
nqaAdminParaTable = _NqaAdminParaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2)
)
if mibBuilder.loadTexts:
    nqaAdminParaTable.setStatus("current")
_NqaAdminParaEntry_Object = MibTableRow
nqaAdminParaEntry = _NqaAdminParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1)
)
nqaAdminParaEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
)
if mibBuilder.loadTexts:
    nqaAdminParaEntry.setStatus("current")


class _NqaAdminParaTargetAddressType_Type(InetAddressType):
    """Custom type nqaAdminParaTargetAddressType based on InetAddressType"""


_NqaAdminParaTargetAddressType_Object = MibTableColumn
nqaAdminParaTargetAddressType = _NqaAdminParaTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 1),
    _NqaAdminParaTargetAddressType_Type()
)
nqaAdminParaTargetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaTargetAddressType.setStatus("current")
_NqaAdminParaTargetAddress_Type = InetAddress
_NqaAdminParaTargetAddress_Object = MibTableColumn
nqaAdminParaTargetAddress = _NqaAdminParaTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 2),
    _NqaAdminParaTargetAddress_Type()
)
nqaAdminParaTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaTargetAddress.setStatus("current")
_NqaAdminParaTargetPort_Type = InetPortNumber
_NqaAdminParaTargetPort_Object = MibTableColumn
nqaAdminParaTargetPort = _NqaAdminParaTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 3),
    _NqaAdminParaTargetPort_Type()
)
nqaAdminParaTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaTargetPort.setStatus("current")


class _NqaAdminParaSourceAddressType_Type(InetAddressType):
    """Custom type nqaAdminParaSourceAddressType based on InetAddressType"""


_NqaAdminParaSourceAddressType_Object = MibTableColumn
nqaAdminParaSourceAddressType = _NqaAdminParaSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 4),
    _NqaAdminParaSourceAddressType_Type()
)
nqaAdminParaSourceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaSourceAddressType.setStatus("current")
_NqaAdminParaSourceAddress_Type = InetAddress
_NqaAdminParaSourceAddress_Object = MibTableColumn
nqaAdminParaSourceAddress = _NqaAdminParaSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 5),
    _NqaAdminParaSourceAddress_Type()
)
nqaAdminParaSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaSourceAddress.setStatus("current")
_NqaAdminParaSourcePort_Type = InetPortNumber
_NqaAdminParaSourcePort_Object = MibTableColumn
nqaAdminParaSourcePort = _NqaAdminParaSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 6),
    _NqaAdminParaSourcePort_Type()
)
nqaAdminParaSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaSourcePort.setStatus("current")


class _NqaAdminParaMaxTtl_Type(Unsigned32):
    """Custom type nqaAdminParaMaxTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NqaAdminParaMaxTtl_Type.__name__ = "Unsigned32"
_NqaAdminParaMaxTtl_Object = MibTableColumn
nqaAdminParaMaxTtl = _NqaAdminParaMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 7),
    _NqaAdminParaMaxTtl_Type()
)
nqaAdminParaMaxTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMaxTtl.setStatus("current")
if mibBuilder.loadTexts:
    nqaAdminParaMaxTtl.setUnits("time-to-live value")


class _NqaAdminParaInitialTtl_Type(Unsigned32):
    """Custom type nqaAdminParaInitialTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaAdminParaInitialTtl_Type.__name__ = "Unsigned32"
_NqaAdminParaInitialTtl_Object = MibTableColumn
nqaAdminParaInitialTtl = _NqaAdminParaInitialTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 8),
    _NqaAdminParaInitialTtl_Type()
)
nqaAdminParaInitialTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaInitialTtl.setStatus("current")


class _NqaAdminParaStorageType_Type(StorageType):
    """Custom type nqaAdminParaStorageType based on StorageType"""


_NqaAdminParaStorageType_Object = MibTableColumn
nqaAdminParaStorageType = _NqaAdminParaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 9),
    _NqaAdminParaStorageType_Type()
)
nqaAdminParaStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaStorageType.setStatus("current")


class _NqaAdminParaMaxFailures_Type(Unsigned32):
    """Custom type nqaAdminParaMaxFailures based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaAdminParaMaxFailures_Type.__name__ = "Unsigned32"
_NqaAdminParaMaxFailures_Object = MibTableColumn
nqaAdminParaMaxFailures = _NqaAdminParaMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 10),
    _NqaAdminParaMaxFailures_Type()
)
nqaAdminParaMaxFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    nqaAdminParaMaxFailures.setUnits("timeouts")


class _NqaAdminParaDontFragment_Type(TruthValue):
    """Custom type nqaAdminParaDontFragment based on TruthValue"""


_NqaAdminParaDontFragment_Object = MibTableColumn
nqaAdminParaDontFragment = _NqaAdminParaDontFragment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 11),
    _NqaAdminParaDontFragment_Type()
)
nqaAdminParaDontFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaDontFragment.setStatus("current")


class _NqaAdminParaDataSize_Type(Unsigned32):
    """Custom type nqaAdminParaDataSize based on Unsigned32"""
    defaultValue = 0


_NqaAdminParaDataSize_Object = MibTableColumn
nqaAdminParaDataSize = _NqaAdminParaDataSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 12),
    _NqaAdminParaDataSize_Type()
)
nqaAdminParaDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaDataSize.setStatus("current")
if mibBuilder.loadTexts:
    nqaAdminParaDataSize.setUnits("octets")


class _NqaAdminParaDataFill_Type(OctetString):
    """Custom type nqaAdminParaDataFill based on OctetString"""
    defaultHexValue = "00"


_NqaAdminParaDataFill_Object = MibTableColumn
nqaAdminParaDataFill = _NqaAdminParaDataFill_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 13),
    _NqaAdminParaDataFill_Type()
)
nqaAdminParaDataFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaDataFill.setStatus("current")


class _NqaAdminParaIfIndex_Type(InterfaceIndexOrZero):
    """Custom type nqaAdminParaIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_NqaAdminParaIfIndex_Object = MibTableColumn
nqaAdminParaIfIndex = _NqaAdminParaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 14),
    _NqaAdminParaIfIndex_Type()
)
nqaAdminParaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaIfIndex.setStatus("current")


class _NqaAdminParaByPassRouteTable_Type(TruthValue):
    """Custom type nqaAdminParaByPassRouteTable based on TruthValue"""


_NqaAdminParaByPassRouteTable_Object = MibTableColumn
nqaAdminParaByPassRouteTable = _NqaAdminParaByPassRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 15),
    _NqaAdminParaByPassRouteTable_Type()
)
nqaAdminParaByPassRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaByPassRouteTable.setStatus("current")


class _NqaAdminParaMiscOptions_Type(SnmpAdminString):
    """Custom type nqaAdminParaMiscOptions based on SnmpAdminString"""
    defaultHexValue = ""


_NqaAdminParaMiscOptions_Object = MibTableColumn
nqaAdminParaMiscOptions = _NqaAdminParaMiscOptions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 16),
    _NqaAdminParaMiscOptions_Type()
)
nqaAdminParaMiscOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMiscOptions.setStatus("current")


class _NqaAdminParaProbeCount_Type(Unsigned32):
    """Custom type nqaAdminParaProbeCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_NqaAdminParaProbeCount_Type.__name__ = "Unsigned32"
_NqaAdminParaProbeCount_Object = MibTableColumn
nqaAdminParaProbeCount = _NqaAdminParaProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 17),
    _NqaAdminParaProbeCount_Type()
)
nqaAdminParaProbeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    nqaAdminParaProbeCount.setUnits("probes")


class _NqaAdminParaTrapGeneration_Type(Bits):
    """Custom type nqaAdminParaTrapGeneration based on Bits"""
    namedValues = NamedValues(
        *(("overOwdThresholdDs", 5),
          ("overOwdThresholdSd", 4),
          ("overRtdThreshold", 3),
          ("probeFailure", 0),
          ("testCompletion", 2),
          ("testFailure", 1))
    )

_NqaAdminParaTrapGeneration_Type.__name__ = "Bits"
_NqaAdminParaTrapGeneration_Object = MibTableColumn
nqaAdminParaTrapGeneration = _NqaAdminParaTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 18),
    _NqaAdminParaTrapGeneration_Type()
)
nqaAdminParaTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaTrapGeneration.setStatus("current")


class _NqaAdminParaTrapProbeFailureFilter_Type(Unsigned32):
    """Custom type nqaAdminParaTrapProbeFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_NqaAdminParaTrapProbeFailureFilter_Type.__name__ = "Unsigned32"
_NqaAdminParaTrapProbeFailureFilter_Object = MibTableColumn
nqaAdminParaTrapProbeFailureFilter = _NqaAdminParaTrapProbeFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 19),
    _NqaAdminParaTrapProbeFailureFilter_Type()
)
nqaAdminParaTrapProbeFailureFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaTrapProbeFailureFilter.setStatus("current")


class _NqaAdminParaTrapTestFailureFilter_Type(Unsigned32):
    """Custom type nqaAdminParaTrapTestFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_NqaAdminParaTrapTestFailureFilter_Type.__name__ = "Unsigned32"
_NqaAdminParaTrapTestFailureFilter_Object = MibTableColumn
nqaAdminParaTrapTestFailureFilter = _NqaAdminParaTrapTestFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 20),
    _NqaAdminParaTrapTestFailureFilter_Type()
)
nqaAdminParaTrapTestFailureFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaTrapTestFailureFilter.setStatus("current")


class _NqaAdminParaDSField_Type(Integer32):
    """Custom type nqaAdminParaDSField based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NqaAdminParaDSField_Type.__name__ = "Integer32"
_NqaAdminParaDSField_Object = MibTableColumn
nqaAdminParaDSField = _NqaAdminParaDSField_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 21),
    _NqaAdminParaDSField_Type()
)
nqaAdminParaDSField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaDSField.setStatus("current")


class _NqaAdminParaDnsServerAddressType_Type(InetAddressType):
    """Custom type nqaAdminParaDnsServerAddressType based on InetAddressType"""


_NqaAdminParaDnsServerAddressType_Object = MibTableColumn
nqaAdminParaDnsServerAddressType = _NqaAdminParaDnsServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 22),
    _NqaAdminParaDnsServerAddressType_Type()
)
nqaAdminParaDnsServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaDnsServerAddressType.setStatus("current")
_NqaAdminParaDnsServerAddress_Type = InetAddress
_NqaAdminParaDnsServerAddress_Object = MibTableColumn
nqaAdminParaDnsServerAddress = _NqaAdminParaDnsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 23),
    _NqaAdminParaDnsServerAddress_Type()
)
nqaAdminParaDnsServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaDnsServerAddress.setStatus("current")


class _NqaAdminParaOperation_Type(NqaOperation):
    """Custom type nqaAdminParaOperation based on NqaOperation"""


_NqaAdminParaOperation_Object = MibTableColumn
nqaAdminParaOperation = _NqaAdminParaOperation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 24),
    _NqaAdminParaOperation_Type()
)
nqaAdminParaOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaOperation.setStatus("current")
_NqaAdminParaHttpVersion_Type = DisplayString
_NqaAdminParaHttpVersion_Object = MibTableColumn
nqaAdminParaHttpVersion = _NqaAdminParaHttpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 25),
    _NqaAdminParaHttpVersion_Type()
)
nqaAdminParaHttpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaHttpVersion.setStatus("current")
_NqaAdminParaHttpOperationString_Type = DisplayString
_NqaAdminParaHttpOperationString_Object = MibTableColumn
nqaAdminParaHttpOperationString = _NqaAdminParaHttpOperationString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 26),
    _NqaAdminParaHttpOperationString_Type()
)
nqaAdminParaHttpOperationString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaHttpOperationString.setStatus("current")


class _NqaAdminParaTestFailurePercent_Type(Unsigned32):
    """Custom type nqaAdminParaTestFailurePercent based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NqaAdminParaTestFailurePercent_Type.__name__ = "Unsigned32"
_NqaAdminParaTestFailurePercent_Object = MibTableColumn
nqaAdminParaTestFailurePercent = _NqaAdminParaTestFailurePercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 27),
    _NqaAdminParaTestFailurePercent_Type()
)
nqaAdminParaTestFailurePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaTestFailurePercent.setStatus("current")
_NqaAdminParaFtpUserName_Type = DisplayString
_NqaAdminParaFtpUserName_Object = MibTableColumn
nqaAdminParaFtpUserName = _NqaAdminParaFtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 28),
    _NqaAdminParaFtpUserName_Type()
)
nqaAdminParaFtpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaFtpUserName.setStatus("current")
_NqaAdminParaFtpPassword_Type = DisplayString
_NqaAdminParaFtpPassword_Object = MibTableColumn
nqaAdminParaFtpPassword = _NqaAdminParaFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 29),
    _NqaAdminParaFtpPassword_Type()
)
nqaAdminParaFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaFtpPassword.setStatus("current")
_NqaAdminParaFtpFilePath_Type = DisplayString
_NqaAdminParaFtpFilePath_Object = MibTableColumn
nqaAdminParaFtpFilePath = _NqaAdminParaFtpFilePath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 30),
    _NqaAdminParaFtpFilePath_Type()
)
nqaAdminParaFtpFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaFtpFilePath.setStatus("current")


class _NqaAdminParaFtpFileSize_Type(Integer32):
    """Custom type nqaAdminParaFtpFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_NqaAdminParaFtpFileSize_Type.__name__ = "Integer32"
_NqaAdminParaFtpFileSize_Object = MibTableColumn
nqaAdminParaFtpFileSize = _NqaAdminParaFtpFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 31),
    _NqaAdminParaFtpFileSize_Type()
)
nqaAdminParaFtpFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaFtpFileSize.setStatus("current")


class _NqaAdminParaInterval_Type(Integer32):
    """Custom type nqaAdminParaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_NqaAdminParaInterval_Type.__name__ = "Integer32"
_NqaAdminParaInterval_Object = MibTableColumn
nqaAdminParaInterval = _NqaAdminParaInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 32),
    _NqaAdminParaInterval_Type()
)
nqaAdminParaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaInterval.setStatus("current")
if mibBuilder.loadTexts:
    nqaAdminParaInterval.setUnits("millseconds")


class _NqaAdminParaNumPackets_Type(Integer32):
    """Custom type nqaAdminParaNumPackets based on Integer32"""
    defaultValue = 20


_NqaAdminParaNumPackets_Object = MibTableColumn
nqaAdminParaNumPackets = _NqaAdminParaNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 33),
    _NqaAdminParaNumPackets_Type()
)
nqaAdminParaNumPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaNumPackets.setStatus("current")
_NqaAdminParaVrfName_Type = DisplayString
_NqaAdminParaVrfName_Object = MibTableColumn
nqaAdminParaVrfName = _NqaAdminParaVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 34),
    _NqaAdminParaVrfName_Type()
)
nqaAdminParaVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaVrfName.setStatus("current")


class _NqaAdminParaLspAddressType_Type(Integer32):
    """Custom type nqaAdminParaLspAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ring", 255),
          ("te", 3))
    )


_NqaAdminParaLspAddressType_Type.__name__ = "Integer32"
_NqaAdminParaLspAddressType_Object = MibTableColumn
nqaAdminParaLspAddressType = _NqaAdminParaLspAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 35),
    _NqaAdminParaLspAddressType_Type()
)
nqaAdminParaLspAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspAddressType.setStatus("current")
_NqaAdminParaLspAddressMask_Type = Integer32
_NqaAdminParaLspAddressMask_Object = MibTableColumn
nqaAdminParaLspAddressMask = _NqaAdminParaLspAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 36),
    _NqaAdminParaLspAddressMask_Type()
)
nqaAdminParaLspAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspAddressMask.setStatus("current")
_NqaAdminParaLspIpAddress_Type = InetAddress
_NqaAdminParaLspIpAddress_Object = MibTableColumn
nqaAdminParaLspIpAddress = _NqaAdminParaLspIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 37),
    _NqaAdminParaLspIpAddress_Type()
)
nqaAdminParaLspIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspIpAddress.setStatus("current")
_NqaAdminParaLspPWE3VcId_Type = Unsigned32
_NqaAdminParaLspPWE3VcId_Object = MibTableColumn
nqaAdminParaLspPWE3VcId = _NqaAdminParaLspPWE3VcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 38),
    _NqaAdminParaLspPWE3VcId_Type()
)
nqaAdminParaLspPWE3VcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspPWE3VcId.setStatus("current")


class _NqaAdminParaLspPWE3Type_Type(Integer32):
    """Custom type nqaAdminParaLspPWE3Type based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              17,
              18,
              19,
              21,
              64)
        )
    )
    namedValues = NamedValues(
        *(("atm-1to1-vcc", 12),
          ("atm-1to1-vpc", 13),
          ("atm-cell-transport", 3),
          ("atm-nto1-vcc", 9),
          ("atm-nto1-vpc", 10),
          ("atmAal5Sdu", 2),
          ("cesopsn-basic", 21),
          ("ethernet", 5),
          ("fr", 1),
          ("hdlc", 6),
          ("ip-layer2", 11),
          ("ipInterworking", 64),
          ("ppp", 7),
          ("satop-e1", 17),
          ("satop-e3", 19),
          ("satop-t1", 18),
          ("vlan", 4))
    )


_NqaAdminParaLspPWE3Type_Type.__name__ = "Integer32"
_NqaAdminParaLspPWE3Type_Object = MibTableColumn
nqaAdminParaLspPWE3Type = _NqaAdminParaLspPWE3Type_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 39),
    _NqaAdminParaLspPWE3Type_Type()
)
nqaAdminParaLspPWE3Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspPWE3Type.setStatus("current")


class _NqaAdminParaLspPWE3Option_Type(Integer32):
    """Custom type nqaAdminParaLspPWE3Option based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlWord", 2),
          ("labelAlert", 1),
          ("normal", 3))
    )


_NqaAdminParaLspPWE3Option_Type.__name__ = "Integer32"
_NqaAdminParaLspPWE3Option_Object = MibTableColumn
nqaAdminParaLspPWE3Option = _NqaAdminParaLspPWE3Option_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 40),
    _NqaAdminParaLspPWE3Option_Type()
)
nqaAdminParaLspPWE3Option.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspPWE3Option.setStatus("current")
_NqaAdminParaLspPWE3RemoteVcId_Type = Unsigned32
_NqaAdminParaLspPWE3RemoteVcId_Object = MibTableColumn
nqaAdminParaLspPWE3RemoteVcId = _NqaAdminParaLspPWE3RemoteVcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 41),
    _NqaAdminParaLspPWE3RemoteVcId_Type()
)
nqaAdminParaLspPWE3RemoteVcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspPWE3RemoteVcId.setStatus("current")
_NqaAdminParaLspPWE3RemoteAddress_Type = InetAddress
_NqaAdminParaLspPWE3RemoteAddress_Object = MibTableColumn
nqaAdminParaLspPWE3RemoteAddress = _NqaAdminParaLspPWE3RemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 42),
    _NqaAdminParaLspPWE3RemoteAddress_Type()
)
nqaAdminParaLspPWE3RemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspPWE3RemoteAddress.setStatus("current")


class _NqaAdminParaLspExp_Type(Unsigned32):
    """Custom type nqaAdminParaLspExp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NqaAdminParaLspExp_Type.__name__ = "Unsigned32"
_NqaAdminParaLspExp_Object = MibTableColumn
nqaAdminParaLspExp = _NqaAdminParaLspExp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 43),
    _NqaAdminParaLspExp_Type()
)
nqaAdminParaLspExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspExp.setStatus("current")


class _NqaAdminParaLspReplyMode_Type(Integer32):
    """Custom type nqaAdminParaLspReplyMode based on Integer32"""
    defaultValue = 2

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
        *(("levelControlChannel", 4),
          ("noReply", 1),
          ("udp", 2),
          ("udpRouterAlert", 3),
          ("udpviaVPLS", 5))
    )


_NqaAdminParaLspReplyMode_Type.__name__ = "Integer32"
_NqaAdminParaLspReplyMode_Object = MibTableColumn
nqaAdminParaLspReplyMode = _NqaAdminParaLspReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 44),
    _NqaAdminParaLspReplyMode_Type()
)
nqaAdminParaLspReplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspReplyMode.setStatus("current")


class _NqaAdminParaResultRowMax_Type(Integer32):
    """Custom type nqaAdminParaResultRowMax based on Integer32"""
    defaultValue = 5


_NqaAdminParaResultRowMax_Object = MibTableColumn
nqaAdminParaResultRowMax = _NqaAdminParaResultRowMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 45),
    _NqaAdminParaResultRowMax_Type()
)
nqaAdminParaResultRowMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaResultRowMax.setStatus("current")


class _NqaAdminParaHistoryRowMax_Type(Integer32):
    """Custom type nqaAdminParaHistoryRowMax based on Integer32"""
    defaultValue = 50


_NqaAdminParaHistoryRowMax_Object = MibTableColumn
nqaAdminParaHistoryRowMax = _NqaAdminParaHistoryRowMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 46),
    _NqaAdminParaHistoryRowMax_Type()
)
nqaAdminParaHistoryRowMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaHistoryRowMax.setStatus("current")


class _NqaAdminParaCreateHopsEntries_Type(EnableValue):
    """Custom type nqaAdminParaCreateHopsEntries based on EnableValue"""


_NqaAdminParaCreateHopsEntries_Object = MibTableColumn
nqaAdminParaCreateHopsEntries = _NqaAdminParaCreateHopsEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 47),
    _NqaAdminParaCreateHopsEntries_Type()
)
nqaAdminParaCreateHopsEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaCreateHopsEntries.setStatus("current")


class _NqaAdminParaLspVCType_Type(Integer32):
    """Custom type nqaAdminParaLspVCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 2),
          ("bgpad", 3),
          ("ldp", 1))
    )


_NqaAdminParaLspVCType_Type.__name__ = "Integer32"
_NqaAdminParaLspVCType_Object = MibTableColumn
nqaAdminParaLspVCType = _NqaAdminParaLspVCType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 48),
    _NqaAdminParaLspVCType_Type()
)
nqaAdminParaLspVCType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspVCType.setStatus("current")
_NqaAdminParaMTraceLastHopAddress_Type = InetAddress
_NqaAdminParaMTraceLastHopAddress_Object = MibTableColumn
nqaAdminParaMTraceLastHopAddress = _NqaAdminParaMTraceLastHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 49),
    _NqaAdminParaMTraceLastHopAddress_Type()
)
nqaAdminParaMTraceLastHopAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMTraceLastHopAddress.setStatus("current")
_NqaAdminParaMTraceSourceAddress_Type = InetAddress
_NqaAdminParaMTraceSourceAddress_Object = MibTableColumn
nqaAdminParaMTraceSourceAddress = _NqaAdminParaMTraceSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 50),
    _NqaAdminParaMTraceSourceAddress_Type()
)
nqaAdminParaMTraceSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMTraceSourceAddress.setStatus("current")
_NqaAdminParaMTraceGroupAddress_Type = InetAddress
_NqaAdminParaMTraceGroupAddress_Object = MibTableColumn
nqaAdminParaMTraceGroupAddress = _NqaAdminParaMTraceGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 51),
    _NqaAdminParaMTraceGroupAddress_Type()
)
nqaAdminParaMTraceGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMTraceGroupAddress.setStatus("current")


class _NqaAdminParaMTraceMaxTtl_Type(Unsigned32):
    """Custom type nqaAdminParaMTraceMaxTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaAdminParaMTraceMaxTtl_Type.__name__ = "Unsigned32"
_NqaAdminParaMTraceMaxTtl_Object = MibTableColumn
nqaAdminParaMTraceMaxTtl = _NqaAdminParaMTraceMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 52),
    _NqaAdminParaMTraceMaxTtl_Type()
)
nqaAdminParaMTraceMaxTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMTraceMaxTtl.setStatus("current")


class _NqaAdminParaMTraceSendMode_Type(Integer32):
    """Custom type nqaAdminParaMTraceSendMode based on Integer32"""
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
        *(("allRouter", 2),
          ("destination", 3),
          ("lastHop", 4),
          ("multicastTree", 1))
    )


_NqaAdminParaMTraceSendMode_Type.__name__ = "Integer32"
_NqaAdminParaMTraceSendMode_Object = MibTableColumn
nqaAdminParaMTraceSendMode = _NqaAdminParaMTraceSendMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 53),
    _NqaAdminParaMTraceSendMode_Type()
)
nqaAdminParaMTraceSendMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMTraceSendMode.setStatus("current")


class _NqaAdminParaMTraceResponseTtl_Type(Unsigned32):
    """Custom type nqaAdminParaMTraceResponseTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaAdminParaMTraceResponseTtl_Type.__name__ = "Unsigned32"
_NqaAdminParaMTraceResponseTtl_Object = MibTableColumn
nqaAdminParaMTraceResponseTtl = _NqaAdminParaMTraceResponseTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 54),
    _NqaAdminParaMTraceResponseTtl_Type()
)
nqaAdminParaMTraceResponseTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMTraceResponseTtl.setStatus("current")


class _NqaAdminParaMTraceResponseAddressType_Type(InetAddressType):
    """Custom type nqaAdminParaMTraceResponseAddressType based on InetAddressType"""


_NqaAdminParaMTraceResponseAddressType_Object = MibTableColumn
nqaAdminParaMTraceResponseAddressType = _NqaAdminParaMTraceResponseAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 55),
    _NqaAdminParaMTraceResponseAddressType_Type()
)
nqaAdminParaMTraceResponseAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMTraceResponseAddressType.setStatus("current")
_NqaAdminParaMTraceResponseAddress_Type = InetAddress
_NqaAdminParaMTraceResponseAddress_Object = MibTableColumn
nqaAdminParaMTraceResponseAddress = _NqaAdminParaMTraceResponseAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 56),
    _NqaAdminParaMTraceResponseAddress_Type()
)
nqaAdminParaMTraceResponseAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMTraceResponseAddress.setStatus("current")
_NqaAdminParaDistanceNodeType_Type = NqaDistanceNodeType
_NqaAdminParaDistanceNodeType_Object = MibTableColumn
nqaAdminParaDistanceNodeType = _NqaAdminParaDistanceNodeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 57),
    _NqaAdminParaDistanceNodeType_Type()
)
nqaAdminParaDistanceNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaDistanceNodeType.setStatus("current")
_NqaAdminParaMacAddress_Type = MacAddress
_NqaAdminParaMacAddress_Object = MibTableColumn
nqaAdminParaMacAddress = _NqaAdminParaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 58),
    _NqaAdminParaMacAddress_Type()
)
nqaAdminParaMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMacAddress.setStatus("current")
_NqaAdminParaRMepID_Type = Dot1agCfmMepIdOrZero
_NqaAdminParaRMepID_Object = MibTableColumn
nqaAdminParaRMepID = _NqaAdminParaRMepID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 59),
    _NqaAdminParaRMepID_Type()
)
nqaAdminParaRMepID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaRMepID.setStatus("current")


class _NqaAdminParaMDName_Type(OctetString):
    """Custom type nqaAdminParaMDName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 43),
    )


_NqaAdminParaMDName_Type.__name__ = "OctetString"
_NqaAdminParaMDName_Object = MibTableColumn
nqaAdminParaMDName = _NqaAdminParaMDName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 60),
    _NqaAdminParaMDName_Type()
)
nqaAdminParaMDName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMDName.setStatus("current")


class _NqaAdminParaMAName_Type(OctetString):
    """Custom type nqaAdminParaMAName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_NqaAdminParaMAName_Type.__name__ = "OctetString"
_NqaAdminParaMAName_Object = MibTableColumn
nqaAdminParaMAName = _NqaAdminParaMAName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 61),
    _NqaAdminParaMAName_Type()
)
nqaAdminParaMAName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMAName.setStatus("current")
_NqaAdminParaMacTunnelName_Type = OctetString
_NqaAdminParaMacTunnelName_Object = MibTableColumn
nqaAdminParaMacTunnelName = _NqaAdminParaMacTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 62),
    _NqaAdminParaMacTunnelName_Type()
)
nqaAdminParaMacTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaMacTunnelName.setStatus("current")


class _NqaAdminParaPathMtuStep_Type(Integer32):
    """Custom type nqaAdminParaPathMtuStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_NqaAdminParaPathMtuStep_Type.__name__ = "Integer32"
_NqaAdminParaPathMtuStep_Object = MibTableColumn
nqaAdminParaPathMtuStep = _NqaAdminParaPathMtuStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 63),
    _NqaAdminParaPathMtuStep_Type()
)
nqaAdminParaPathMtuStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaPathMtuStep.setStatus("current")


class _NqaAdminParaPathMtuDiscoveryPathMtuMax_Type(Integer32):
    """Custom type nqaAdminParaPathMtuDiscoveryPathMtuMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48, 9198),
    )


_NqaAdminParaPathMtuDiscoveryPathMtuMax_Type.__name__ = "Integer32"
_NqaAdminParaPathMtuDiscoveryPathMtuMax_Object = MibTableColumn
nqaAdminParaPathMtuDiscoveryPathMtuMax = _NqaAdminParaPathMtuDiscoveryPathMtuMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 64),
    _NqaAdminParaPathMtuDiscoveryPathMtuMax_Type()
)
nqaAdminParaPathMtuDiscoveryPathMtuMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaPathMtuDiscoveryPathMtuMax.setStatus("current")


class _NqaAdminParaIcmpJitterMode_Type(Integer32):
    """Custom type nqaAdminParaIcmpJitterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("icmpEcho", 2),
          ("icmpTimestamp", 1))
    )


_NqaAdminParaIcmpJitterMode_Type.__name__ = "Integer32"
_NqaAdminParaIcmpJitterMode_Object = MibTableColumn
nqaAdminParaIcmpJitterMode = _NqaAdminParaIcmpJitterMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 65),
    _NqaAdminParaIcmpJitterMode_Type()
)
nqaAdminParaIcmpJitterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaIcmpJitterMode.setStatus("current")


class _NqaAdminParaCodecType_Type(Integer32):
    """Custom type nqaAdminParaCodecType based on Integer32"""
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
        *(("g711Alaw", 2),
          ("g711Ulaw", 3),
          ("g729A", 4),
          ("notDefined", 1))
    )


_NqaAdminParaCodecType_Type.__name__ = "Integer32"
_NqaAdminParaCodecType_Object = MibTableColumn
nqaAdminParaCodecType = _NqaAdminParaCodecType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 66),
    _NqaAdminParaCodecType_Type()
)
nqaAdminParaCodecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaCodecType.setStatus("current")


class _NqaAdminParaIcpifAdvFactor_Type(Integer32):
    """Custom type nqaAdminParaIcpifAdvFactor based on Integer32"""
    defaultValue = 0


_NqaAdminParaIcpifAdvFactor_Object = MibTableColumn
nqaAdminParaIcpifAdvFactor = _NqaAdminParaIcpifAdvFactor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 67),
    _NqaAdminParaIcpifAdvFactor_Type()
)
nqaAdminParaIcpifAdvFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaIcpifAdvFactor.setStatus("current")


class _NqaAdminParaFtpMode_Type(Integer32):
    """Custom type nqaAdminParaFtpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_NqaAdminParaFtpMode_Type.__name__ = "Integer32"
_NqaAdminParaFtpMode_Object = MibTableColumn
nqaAdminParaFtpMode = _NqaAdminParaFtpMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 68),
    _NqaAdminParaFtpMode_Type()
)
nqaAdminParaFtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaFtpMode.setStatus("current")
_NqaAdminParaHardwareBased_Type = EnabledStatus
_NqaAdminParaHardwareBased_Object = MibTableColumn
nqaAdminParaHardwareBased = _NqaAdminParaHardwareBased_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 69),
    _NqaAdminParaHardwareBased_Type()
)
nqaAdminParaHardwareBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaHardwareBased.setStatus("current")


class _NqaAdminParaPppoeUserName_Type(OctetString):
    """Custom type nqaAdminParaPppoeUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NqaAdminParaPppoeUserName_Type.__name__ = "OctetString"
_NqaAdminParaPppoeUserName_Object = MibTableColumn
nqaAdminParaPppoeUserName = _NqaAdminParaPppoeUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 70),
    _NqaAdminParaPppoeUserName_Type()
)
nqaAdminParaPppoeUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaPppoeUserName.setStatus("current")


class _NqaAdminParaPppoePassword_Type(OctetString):
    """Custom type nqaAdminParaPppoePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NqaAdminParaPppoePassword_Type.__name__ = "OctetString"
_NqaAdminParaPppoePassword_Object = MibTableColumn
nqaAdminParaPppoePassword = _NqaAdminParaPppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 71),
    _NqaAdminParaPppoePassword_Type()
)
nqaAdminParaPppoePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaPppoePassword.setStatus("current")


class _NqaAdminParaPppoeVlanIf_Type(Integer32):
    """Custom type nqaAdminParaPppoeVlanIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_NqaAdminParaPppoeVlanIf_Type.__name__ = "Integer32"
_NqaAdminParaPppoeVlanIf_Object = MibTableColumn
nqaAdminParaPppoeVlanIf = _NqaAdminParaPppoeVlanIf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 72),
    _NqaAdminParaPppoeVlanIf_Type()
)
nqaAdminParaPppoeVlanIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaPppoeVlanIf.setStatus("current")


class _NqaAdminParaPppoeAuthenticationMode_Type(Integer32):
    """Custom type nqaAdminParaPppoeAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("pap", 2))
    )


_NqaAdminParaPppoeAuthenticationMode_Type.__name__ = "Integer32"
_NqaAdminParaPppoeAuthenticationMode_Object = MibTableColumn
nqaAdminParaPppoeAuthenticationMode = _NqaAdminParaPppoeAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 73),
    _NqaAdminParaPppoeAuthenticationMode_Type()
)
nqaAdminParaPppoeAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaPppoeAuthenticationMode.setStatus("current")


class _NqaAdminParaPppoeRedialUpTimes_Type(Integer32):
    """Custom type nqaAdminParaPppoeRedialUpTimes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_NqaAdminParaPppoeRedialUpTimes_Type.__name__ = "Integer32"
_NqaAdminParaPppoeRedialUpTimes_Object = MibTableColumn
nqaAdminParaPppoeRedialUpTimes = _NqaAdminParaPppoeRedialUpTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 74),
    _NqaAdminParaPppoeRedialUpTimes_Type()
)
nqaAdminParaPppoeRedialUpTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaPppoeRedialUpTimes.setStatus("current")


class _NqaAdminParaPppoeInterval_Type(Integer32):
    """Custom type nqaAdminParaPppoeInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_NqaAdminParaPppoeInterval_Type.__name__ = "Integer32"
_NqaAdminParaPppoeInterval_Object = MibTableColumn
nqaAdminParaPppoeInterval = _NqaAdminParaPppoeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 75),
    _NqaAdminParaPppoeInterval_Type()
)
nqaAdminParaPppoeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaPppoeInterval.setStatus("current")


class _NqaAdminParaVsiName_Type(OctetString):
    """Custom type nqaAdminParaVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NqaAdminParaVsiName_Type.__name__ = "OctetString"
_NqaAdminParaVsiName_Object = MibTableColumn
nqaAdminParaVsiName = _NqaAdminParaVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 76),
    _NqaAdminParaVsiName_Type()
)
nqaAdminParaVsiName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaVsiName.setStatus("current")
_NqaAdminParaVlanId_Type = VlanIdOrNone
_NqaAdminParaVlanId_Object = MibTableColumn
nqaAdminParaVlanId = _NqaAdminParaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 77),
    _NqaAdminParaVlanId_Type()
)
nqaAdminParaVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaVlanId.setStatus("current")


class _NqaAdminParaLspTunnelType_Type(Integer32):
    """Custom type nqaAdminParaLspTunnelType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hotstandby", 1),
          ("main", 0))
    )


_NqaAdminParaLspTunnelType_Type.__name__ = "Integer32"
_NqaAdminParaLspTunnelType_Object = MibTableColumn
nqaAdminParaLspTunnelType = _NqaAdminParaLspTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 78),
    _NqaAdminParaLspTunnelType_Type()
)
nqaAdminParaLspTunnelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspTunnelType.setStatus("current")
_NqaAdminParaLspNextHopAddress_Type = InetAddress
_NqaAdminParaLspNextHopAddress_Object = MibTableColumn
nqaAdminParaLspNextHopAddress = _NqaAdminParaLspNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 79),
    _NqaAdminParaLspNextHopAddress_Type()
)
nqaAdminParaLspNextHopAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspNextHopAddress.setStatus("current")


class _NqaAdminParaLspVersion_Type(Integer32):
    """Custom type nqaAdminParaLspVersion based on Integer32"""
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
        *(("draft6", 1),
          ("ptnmode", 3),
          ("rfc4379", 2))
    )


_NqaAdminParaLspVersion_Type.__name__ = "Integer32"
_NqaAdminParaLspVersion_Object = MibTableColumn
nqaAdminParaLspVersion = _NqaAdminParaLspVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 80),
    _NqaAdminParaLspVersion_Type()
)
nqaAdminParaLspVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaLspVersion.setStatus("current")


class _NqaAdminParaRemoteAddressType_Type(InetAddressType):
    """Custom type nqaAdminParaRemoteAddressType based on InetAddressType"""


_NqaAdminParaRemoteAddressType_Object = MibTableColumn
nqaAdminParaRemoteAddressType = _NqaAdminParaRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 81),
    _NqaAdminParaRemoteAddressType_Type()
)
nqaAdminParaRemoteAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaRemoteAddressType.setStatus("current")
_NqaAdminParaRemoteAddress_Type = InetAddress
_NqaAdminParaRemoteAddress_Object = MibTableColumn
nqaAdminParaRemoteAddress = _NqaAdminParaRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 82),
    _NqaAdminParaRemoteAddress_Type()
)
nqaAdminParaRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaRemoteAddress.setStatus("current")


class _NqaAdminParaTimeUnit_Type(Integer32):
    """Custom type nqaAdminParaTimeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ms", 2),
          ("us", 1))
    )


_NqaAdminParaTimeUnit_Type.__name__ = "Integer32"
_NqaAdminParaTimeUnit_Object = MibTableColumn
nqaAdminParaTimeUnit = _NqaAdminParaTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 2, 1, 83),
    _NqaAdminParaTimeUnit_Type()
)
nqaAdminParaTimeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminParaTimeUnit.setStatus("current")
_NqaScheduleTable_Object = MibTable
nqaScheduleTable = _NqaScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3)
)
if mibBuilder.loadTexts:
    nqaScheduleTable.setStatus("current")
_NqaScheduleEntry_Object = MibTableRow
nqaScheduleEntry = _NqaScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1)
)
nqaScheduleEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
)
if mibBuilder.loadTexts:
    nqaScheduleEntry.setStatus("current")


class _NqaScheduleStartType_Type(Integer32):
    """Custom type nqaScheduleStartType based on Integer32"""
    defaultValue = 0

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
        *(("default", 0),
          ("startAfter", 3),
          ("startAt", 2),
          ("startNow", 1))
    )


_NqaScheduleStartType_Type.__name__ = "Integer32"
_NqaScheduleStartType_Object = MibTableColumn
nqaScheduleStartType = _NqaScheduleStartType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1, 1),
    _NqaScheduleStartType_Type()
)
nqaScheduleStartType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaScheduleStartType.setStatus("current")
_NqaScheduleStartTime_Type = Unsigned32
_NqaScheduleStartTime_Object = MibTableColumn
nqaScheduleStartTime = _NqaScheduleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1, 2),
    _NqaScheduleStartTime_Type()
)
nqaScheduleStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaScheduleStartTime.setStatus("current")


class _NqaScheduleEndType_Type(Integer32):
    """Custom type nqaScheduleEndType based on Integer32"""
    defaultValue = 0

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
        *(("default", 0),
          ("endAfter", 2),
          ("endAt", 1),
          ("endLifetime", 3))
    )


_NqaScheduleEndType_Type.__name__ = "Integer32"
_NqaScheduleEndType_Object = MibTableColumn
nqaScheduleEndType = _NqaScheduleEndType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1, 3),
    _NqaScheduleEndType_Type()
)
nqaScheduleEndType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaScheduleEndType.setStatus("current")
_NqaScheduleEndTime_Type = Unsigned32
_NqaScheduleEndTime_Object = MibTableColumn
nqaScheduleEndTime = _NqaScheduleEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1, 4),
    _NqaScheduleEndTime_Type()
)
nqaScheduleEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaScheduleEndTime.setStatus("current")
_NqaScheduleAgeTime_Type = Integer32
_NqaScheduleAgeTime_Object = MibTableColumn
nqaScheduleAgeTime = _NqaScheduleAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1, 5),
    _NqaScheduleAgeTime_Type()
)
nqaScheduleAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaScheduleAgeTime.setStatus("current")
_NqaScheduleElapsedTime_Type = TimeInterval
_NqaScheduleElapsedTime_Object = MibTableColumn
nqaScheduleElapsedTime = _NqaScheduleElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1, 6),
    _NqaScheduleElapsedTime_Type()
)
nqaScheduleElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaScheduleElapsedTime.setStatus("current")
_NqaScheduleNumOfInitiations_Type = Integer32
_NqaScheduleNumOfInitiations_Object = MibTableColumn
nqaScheduleNumOfInitiations = _NqaScheduleNumOfInitiations_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1, 7),
    _NqaScheduleNumOfInitiations_Type()
)
nqaScheduleNumOfInitiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaScheduleNumOfInitiations.setStatus("current")
_NqaScheduleLastFinishIndex_Type = Integer32
_NqaScheduleLastFinishIndex_Object = MibTableColumn
nqaScheduleLastFinishIndex = _NqaScheduleLastFinishIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1, 8),
    _NqaScheduleLastFinishIndex_Type()
)
nqaScheduleLastFinishIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaScheduleLastFinishIndex.setStatus("current")


class _NqaScheduleOperStatus_Type(Integer32):
    """Custom type nqaScheduleOperStatus based on Integer32"""
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
        *(("active", 4),
          ("inactive", 5),
          ("reset", 1),
          ("restart", 3),
          ("stop", 2))
    )


_NqaScheduleOperStatus_Type.__name__ = "Integer32"
_NqaScheduleOperStatus_Object = MibTableColumn
nqaScheduleOperStatus = _NqaScheduleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1, 9),
    _NqaScheduleOperStatus_Type()
)
nqaScheduleOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaScheduleOperStatus.setStatus("current")
_NqaScheduleLastCollectIndex_Type = Integer32
_NqaScheduleLastCollectIndex_Object = MibTableColumn
nqaScheduleLastCollectIndex = _NqaScheduleLastCollectIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 3, 1, 10),
    _NqaScheduleLastCollectIndex_Type()
)
nqaScheduleLastCollectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaScheduleLastCollectIndex.setStatus("current")
_NqaGroupTable_Object = MibTable
nqaGroupTable = _NqaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 4)
)
if mibBuilder.loadTexts:
    nqaGroupTable.setStatus("current")
_NqaGroupEntry_Object = MibTableRow
nqaGroupEntry = _NqaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 4, 1)
)
nqaGroupEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
)
if mibBuilder.loadTexts:
    nqaGroupEntry.setStatus("current")


class _NqaGroupStatusType_Type(Integer32):
    """Custom type nqaGroupStatusType based on Integer32"""
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
        *(("leader", 2),
          ("member", 3),
          ("normal", 1))
    )


_NqaGroupStatusType_Type.__name__ = "Integer32"
_NqaGroupStatusType_Object = MibTableColumn
nqaGroupStatusType = _NqaGroupStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 4, 1, 1),
    _NqaGroupStatusType_Type()
)
nqaGroupStatusType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaGroupStatusType.setStatus("current")


class _NqaGroupPeriod_Type(Integer32):
    """Custom type nqaGroupPeriod based on Integer32"""
    defaultValue = 60


_NqaGroupPeriod_Object = MibTableColumn
nqaGroupPeriod = _NqaGroupPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 4, 1, 2),
    _NqaGroupPeriod_Type()
)
nqaGroupPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaGroupPeriod.setStatus("current")
if mibBuilder.loadTexts:
    nqaGroupPeriod.setUnits("seconds")
_NqaGroupLeaderOwnerIndex_Type = SnmpAdminString
_NqaGroupLeaderOwnerIndex_Object = MibTableColumn
nqaGroupLeaderOwnerIndex = _NqaGroupLeaderOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 4, 1, 3),
    _NqaGroupLeaderOwnerIndex_Type()
)
nqaGroupLeaderOwnerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaGroupLeaderOwnerIndex.setStatus("current")
_NqaGroupLeaderTestName_Type = SnmpAdminString
_NqaGroupLeaderTestName_Object = MibTableColumn
nqaGroupLeaderTestName = _NqaGroupLeaderTestName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 4, 1, 4),
    _NqaGroupLeaderTestName_Type()
)
nqaGroupLeaderTestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaGroupLeaderTestName.setStatus("current")
_NqaGroupMemberNum_Type = Integer32
_NqaGroupMemberNum_Object = MibTableColumn
nqaGroupMemberNum = _NqaGroupMemberNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 4, 1, 5),
    _NqaGroupMemberNum_Type()
)
nqaGroupMemberNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaGroupMemberNum.setStatus("current")
_NqaGroupMemberFree_Type = EnableValue
_NqaGroupMemberFree_Object = MibTableColumn
nqaGroupMemberFree = _NqaGroupMemberFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 4, 1, 6),
    _NqaGroupMemberFree_Type()
)
nqaGroupMemberFree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaGroupMemberFree.setStatus("current")
_NqaAdminParaExtTable_Object = MibTable
nqaAdminParaExtTable = _NqaAdminParaExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5)
)
if mibBuilder.loadTexts:
    nqaAdminParaExtTable.setStatus("current")
_NqaAdminParaExtEntry_Object = MibTableRow
nqaAdminParaExtEntry = _NqaAdminParaExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1)
)
nqaAdminParaExtEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
)
if mibBuilder.loadTexts:
    nqaAdminParaExtEntry.setStatus("current")
_NqaAdminExtPara1_Type = OctetString
_NqaAdminExtPara1_Object = MibTableColumn
nqaAdminExtPara1 = _NqaAdminExtPara1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 1),
    _NqaAdminExtPara1_Type()
)
nqaAdminExtPara1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara1.setStatus("current")


class _NqaAdminExtPara2_Type(Integer32):
    """Custom type nqaAdminExtPara2 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara2_Object = MibTableColumn
nqaAdminExtPara2 = _NqaAdminExtPara2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 2),
    _NqaAdminExtPara2_Type()
)
nqaAdminExtPara2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara2.setStatus("current")
_NqaAdminExtPara3_Type = OctetString
_NqaAdminExtPara3_Object = MibTableColumn
nqaAdminExtPara3 = _NqaAdminExtPara3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 3),
    _NqaAdminExtPara3_Type()
)
nqaAdminExtPara3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara3.setStatus("current")


class _NqaAdminExtPara4_Type(Integer32):
    """Custom type nqaAdminExtPara4 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara4_Object = MibTableColumn
nqaAdminExtPara4 = _NqaAdminExtPara4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 4),
    _NqaAdminExtPara4_Type()
)
nqaAdminExtPara4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara4.setStatus("current")
_NqaAdminExtPara5_Type = OctetString
_NqaAdminExtPara5_Object = MibTableColumn
nqaAdminExtPara5 = _NqaAdminExtPara5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 5),
    _NqaAdminExtPara5_Type()
)
nqaAdminExtPara5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara5.setStatus("current")


class _NqaAdminExtPara6_Type(Integer32):
    """Custom type nqaAdminExtPara6 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara6_Object = MibTableColumn
nqaAdminExtPara6 = _NqaAdminExtPara6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 6),
    _NqaAdminExtPara6_Type()
)
nqaAdminExtPara6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara6.setStatus("current")
_NqaAdminExtPara7_Type = OctetString
_NqaAdminExtPara7_Object = MibTableColumn
nqaAdminExtPara7 = _NqaAdminExtPara7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 7),
    _NqaAdminExtPara7_Type()
)
nqaAdminExtPara7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara7.setStatus("current")


class _NqaAdminExtPara8_Type(Integer32):
    """Custom type nqaAdminExtPara8 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara8_Object = MibTableColumn
nqaAdminExtPara8 = _NqaAdminExtPara8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 8),
    _NqaAdminExtPara8_Type()
)
nqaAdminExtPara8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara8.setStatus("current")
_NqaAdminExtPara9_Type = OctetString
_NqaAdminExtPara9_Object = MibTableColumn
nqaAdminExtPara9 = _NqaAdminExtPara9_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 9),
    _NqaAdminExtPara9_Type()
)
nqaAdminExtPara9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara9.setStatus("current")


class _NqaAdminExtPara10_Type(Integer32):
    """Custom type nqaAdminExtPara10 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara10_Object = MibTableColumn
nqaAdminExtPara10 = _NqaAdminExtPara10_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 10),
    _NqaAdminExtPara10_Type()
)
nqaAdminExtPara10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara10.setStatus("current")
_NqaAdminExtPara11_Type = OctetString
_NqaAdminExtPara11_Object = MibTableColumn
nqaAdminExtPara11 = _NqaAdminExtPara11_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 11),
    _NqaAdminExtPara11_Type()
)
nqaAdminExtPara11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara11.setStatus("current")


class _NqaAdminExtPara12_Type(Integer32):
    """Custom type nqaAdminExtPara12 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara12_Object = MibTableColumn
nqaAdminExtPara12 = _NqaAdminExtPara12_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 12),
    _NqaAdminExtPara12_Type()
)
nqaAdminExtPara12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara12.setStatus("current")
_NqaAdminExtPara13_Type = OctetString
_NqaAdminExtPara13_Object = MibTableColumn
nqaAdminExtPara13 = _NqaAdminExtPara13_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 13),
    _NqaAdminExtPara13_Type()
)
nqaAdminExtPara13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara13.setStatus("current")


class _NqaAdminExtPara14_Type(Integer32):
    """Custom type nqaAdminExtPara14 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara14_Object = MibTableColumn
nqaAdminExtPara14 = _NqaAdminExtPara14_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 14),
    _NqaAdminExtPara14_Type()
)
nqaAdminExtPara14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara14.setStatus("current")
_NqaAdminExtPara15_Type = OctetString
_NqaAdminExtPara15_Object = MibTableColumn
nqaAdminExtPara15 = _NqaAdminExtPara15_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 15),
    _NqaAdminExtPara15_Type()
)
nqaAdminExtPara15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara15.setStatus("current")


class _NqaAdminExtPara16_Type(Integer32):
    """Custom type nqaAdminExtPara16 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara16_Object = MibTableColumn
nqaAdminExtPara16 = _NqaAdminExtPara16_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 16),
    _NqaAdminExtPara16_Type()
)
nqaAdminExtPara16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara16.setStatus("current")
_NqaAdminExtPara17_Type = OctetString
_NqaAdminExtPara17_Object = MibTableColumn
nqaAdminExtPara17 = _NqaAdminExtPara17_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 17),
    _NqaAdminExtPara17_Type()
)
nqaAdminExtPara17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara17.setStatus("current")


class _NqaAdminExtPara18_Type(Integer32):
    """Custom type nqaAdminExtPara18 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara18_Object = MibTableColumn
nqaAdminExtPara18 = _NqaAdminExtPara18_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 18),
    _NqaAdminExtPara18_Type()
)
nqaAdminExtPara18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara18.setStatus("current")
_NqaAdminExtPara19_Type = OctetString
_NqaAdminExtPara19_Object = MibTableColumn
nqaAdminExtPara19 = _NqaAdminExtPara19_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 19),
    _NqaAdminExtPara19_Type()
)
nqaAdminExtPara19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara19.setStatus("current")


class _NqaAdminExtPara20_Type(Integer32):
    """Custom type nqaAdminExtPara20 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara20_Object = MibTableColumn
nqaAdminExtPara20 = _NqaAdminExtPara20_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 20),
    _NqaAdminExtPara20_Type()
)
nqaAdminExtPara20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara20.setStatus("current")
_NqaAdminExtPara21_Type = OctetString
_NqaAdminExtPara21_Object = MibTableColumn
nqaAdminExtPara21 = _NqaAdminExtPara21_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 21),
    _NqaAdminExtPara21_Type()
)
nqaAdminExtPara21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara21.setStatus("current")


class _NqaAdminExtPara22_Type(Integer32):
    """Custom type nqaAdminExtPara22 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara22_Object = MibTableColumn
nqaAdminExtPara22 = _NqaAdminExtPara22_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 22),
    _NqaAdminExtPara22_Type()
)
nqaAdminExtPara22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara22.setStatus("current")
_NqaAdminExtPara23_Type = OctetString
_NqaAdminExtPara23_Object = MibTableColumn
nqaAdminExtPara23 = _NqaAdminExtPara23_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 23),
    _NqaAdminExtPara23_Type()
)
nqaAdminExtPara23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara23.setStatus("current")


class _NqaAdminExtPara24_Type(Integer32):
    """Custom type nqaAdminExtPara24 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara24_Object = MibTableColumn
nqaAdminExtPara24 = _NqaAdminExtPara24_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 24),
    _NqaAdminExtPara24_Type()
)
nqaAdminExtPara24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara24.setStatus("current")
_NqaAdminExtPara25_Type = OctetString
_NqaAdminExtPara25_Object = MibTableColumn
nqaAdminExtPara25 = _NqaAdminExtPara25_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 25),
    _NqaAdminExtPara25_Type()
)
nqaAdminExtPara25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara25.setStatus("current")


class _NqaAdminExtPara26_Type(Integer32):
    """Custom type nqaAdminExtPara26 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara26_Object = MibTableColumn
nqaAdminExtPara26 = _NqaAdminExtPara26_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 26),
    _NqaAdminExtPara26_Type()
)
nqaAdminExtPara26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara26.setStatus("current")
_NqaAdminExtPara27_Type = OctetString
_NqaAdminExtPara27_Object = MibTableColumn
nqaAdminExtPara27 = _NqaAdminExtPara27_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 27),
    _NqaAdminExtPara27_Type()
)
nqaAdminExtPara27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara27.setStatus("current")


class _NqaAdminExtPara28_Type(Integer32):
    """Custom type nqaAdminExtPara28 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara28_Object = MibTableColumn
nqaAdminExtPara28 = _NqaAdminExtPara28_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 28),
    _NqaAdminExtPara28_Type()
)
nqaAdminExtPara28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara28.setStatus("current")
_NqaAdminExtPara29_Type = OctetString
_NqaAdminExtPara29_Object = MibTableColumn
nqaAdminExtPara29 = _NqaAdminExtPara29_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 29),
    _NqaAdminExtPara29_Type()
)
nqaAdminExtPara29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara29.setStatus("current")


class _NqaAdminExtPara30_Type(Integer32):
    """Custom type nqaAdminExtPara30 based on Integer32"""
    defaultValue = 0


_NqaAdminExtPara30_Object = MibTableColumn
nqaAdminExtPara30 = _NqaAdminExtPara30_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 30),
    _NqaAdminExtPara30_Type()
)
nqaAdminExtPara30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara30.setStatus("current")
_NqaAdminExtPara31_Type = OctetString
_NqaAdminExtPara31_Object = MibTableColumn
nqaAdminExtPara31 = _NqaAdminExtPara31_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 31),
    _NqaAdminExtPara31_Type()
)
nqaAdminExtPara31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara31.setStatus("current")


class _NqaAdminExtPara32_Type(OctetString):
    """Custom type nqaAdminExtPara32 based on OctetString"""
    defaultValue = 0


_NqaAdminExtPara32_Object = MibTableColumn
nqaAdminExtPara32 = _NqaAdminExtPara32_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 32),
    _NqaAdminExtPara32_Type()
)
nqaAdminExtPara32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara32.setStatus("current")
_NqaAdminExtPara33_Type = OctetString
_NqaAdminExtPara33_Object = MibTableColumn
nqaAdminExtPara33 = _NqaAdminExtPara33_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 33),
    _NqaAdminExtPara33_Type()
)
nqaAdminExtPara33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara33.setStatus("current")


class _NqaAdminExtPara34_Type(OctetString):
    """Custom type nqaAdminExtPara34 based on OctetString"""
    defaultValue = 0


_NqaAdminExtPara34_Object = MibTableColumn
nqaAdminExtPara34 = _NqaAdminExtPara34_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 34),
    _NqaAdminExtPara34_Type()
)
nqaAdminExtPara34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara34.setStatus("current")
_NqaAdminExtPara35_Type = OctetString
_NqaAdminExtPara35_Object = MibTableColumn
nqaAdminExtPara35 = _NqaAdminExtPara35_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 35),
    _NqaAdminExtPara35_Type()
)
nqaAdminExtPara35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara35.setStatus("current")


class _NqaAdminExtPara36_Type(OctetString):
    """Custom type nqaAdminExtPara36 based on OctetString"""
    defaultValue = 0


_NqaAdminExtPara36_Object = MibTableColumn
nqaAdminExtPara36 = _NqaAdminExtPara36_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 36),
    _NqaAdminExtPara36_Type()
)
nqaAdminExtPara36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara36.setStatus("current")
_NqaAdminExtPara37_Type = OctetString
_NqaAdminExtPara37_Object = MibTableColumn
nqaAdminExtPara37 = _NqaAdminExtPara37_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 37),
    _NqaAdminExtPara37_Type()
)
nqaAdminExtPara37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara37.setStatus("current")


class _NqaAdminExtPara38_Type(OctetString):
    """Custom type nqaAdminExtPara38 based on OctetString"""
    defaultValue = 0


_NqaAdminExtPara38_Object = MibTableColumn
nqaAdminExtPara38 = _NqaAdminExtPara38_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 38),
    _NqaAdminExtPara38_Type()
)
nqaAdminExtPara38.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara38.setStatus("current")
_NqaAdminExtPara39_Type = OctetString
_NqaAdminExtPara39_Object = MibTableColumn
nqaAdminExtPara39 = _NqaAdminExtPara39_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 39),
    _NqaAdminExtPara39_Type()
)
nqaAdminExtPara39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara39.setStatus("current")


class _NqaAdminExtPara40_Type(OctetString):
    """Custom type nqaAdminExtPara40 based on OctetString"""
    defaultValue = 0


_NqaAdminExtPara40_Object = MibTableColumn
nqaAdminExtPara40 = _NqaAdminExtPara40_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 40),
    _NqaAdminExtPara40_Type()
)
nqaAdminExtPara40.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara40.setStatus("current")
_NqaAdminExtPara41_Type = OctetString
_NqaAdminExtPara41_Object = MibTableColumn
nqaAdminExtPara41 = _NqaAdminExtPara41_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 41),
    _NqaAdminExtPara41_Type()
)
nqaAdminExtPara41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara41.setStatus("current")


class _NqaAdminExtPara42_Type(OctetString):
    """Custom type nqaAdminExtPara42 based on OctetString"""
    defaultValue = 0


_NqaAdminExtPara42_Object = MibTableColumn
nqaAdminExtPara42 = _NqaAdminExtPara42_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 42),
    _NqaAdminExtPara42_Type()
)
nqaAdminExtPara42.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara42.setStatus("current")
_NqaAdminExtPara43_Type = OctetString
_NqaAdminExtPara43_Object = MibTableColumn
nqaAdminExtPara43 = _NqaAdminExtPara43_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 43),
    _NqaAdminExtPara43_Type()
)
nqaAdminExtPara43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara43.setStatus("current")


class _NqaAdminExtPara44_Type(OctetString):
    """Custom type nqaAdminExtPara44 based on OctetString"""
    defaultValue = 0


_NqaAdminExtPara44_Object = MibTableColumn
nqaAdminExtPara44 = _NqaAdminExtPara44_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 44),
    _NqaAdminExtPara44_Type()
)
nqaAdminExtPara44.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara44.setStatus("current")
_NqaAdminExtPara45_Type = OctetString
_NqaAdminExtPara45_Object = MibTableColumn
nqaAdminExtPara45 = _NqaAdminExtPara45_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 45),
    _NqaAdminExtPara45_Type()
)
nqaAdminExtPara45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara45.setStatus("current")


class _NqaAdminExtPara46_Type(OctetString):
    """Custom type nqaAdminExtPara46 based on OctetString"""
    defaultValue = 0


_NqaAdminExtPara46_Object = MibTableColumn
nqaAdminExtPara46 = _NqaAdminExtPara46_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 46),
    _NqaAdminExtPara46_Type()
)
nqaAdminExtPara46.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara46.setStatus("current")
_NqaAdminExtPara47_Type = OctetString
_NqaAdminExtPara47_Object = MibTableColumn
nqaAdminExtPara47 = _NqaAdminExtPara47_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 47),
    _NqaAdminExtPara47_Type()
)
nqaAdminExtPara47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara47.setStatus("current")


class _NqaAdminExtPara48_Type(OctetString):
    """Custom type nqaAdminExtPara48 based on OctetString"""
    defaultValue = 0


_NqaAdminExtPara48_Object = MibTableColumn
nqaAdminExtPara48 = _NqaAdminExtPara48_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 48),
    _NqaAdminExtPara48_Type()
)
nqaAdminExtPara48.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara48.setStatus("current")
_NqaAdminExtPara49_Type = OctetString
_NqaAdminExtPara49_Object = MibTableColumn
nqaAdminExtPara49 = _NqaAdminExtPara49_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 49),
    _NqaAdminExtPara49_Type()
)
nqaAdminExtPara49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAdminExtPara49.setStatus("current")


class _NqaAdminExtPara50_Type(OctetString):
    """Custom type nqaAdminExtPara50 based on OctetString"""
    defaultValue = 0


_NqaAdminExtPara50_Object = MibTableColumn
nqaAdminExtPara50 = _NqaAdminExtPara50_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 2, 5, 1, 50),
    _NqaAdminExtPara50_Type()
)
nqaAdminExtPara50.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaAdminExtPara50.setStatus("current")
_NqaServer_ObjectIdentity = ObjectIdentity
nqaServer = _NqaServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3)
)
_NqaServerEnable_Type = EnableValue
_NqaServerEnable_Object = MibScalar
nqaServerEnable = _NqaServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 1),
    _NqaServerEnable_Type()
)
nqaServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaServerEnable.setStatus("current")
_NqaTcpServerTable_Object = MibTable
nqaTcpServerTable = _NqaTcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 2)
)
if mibBuilder.loadTexts:
    nqaTcpServerTable.setStatus("current")
_NqaTcpServerEntry_Object = MibTableRow
nqaTcpServerEntry = _NqaTcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 2, 1)
)
nqaTcpServerEntry.setIndexNames(
    (0, "NQA-MIB", "nqaTcpServerAddress"),
    (0, "NQA-MIB", "nqaTcpServerPort"),
    (0, "NQA-MIB", "nqaTcpServerVrfName"),
)
if mibBuilder.loadTexts:
    nqaTcpServerEntry.setStatus("current")


class _NqaTcpServerAddressType_Type(InetAddressType):
    """Custom type nqaTcpServerAddressType based on InetAddressType"""


_NqaTcpServerAddressType_Object = MibTableColumn
nqaTcpServerAddressType = _NqaTcpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 2, 1, 1),
    _NqaTcpServerAddressType_Type()
)
nqaTcpServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaTcpServerAddressType.setStatus("current")
_NqaTcpServerAddress_Type = InetAddress
_NqaTcpServerAddress_Object = MibTableColumn
nqaTcpServerAddress = _NqaTcpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 2, 1, 2),
    _NqaTcpServerAddress_Type()
)
nqaTcpServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaTcpServerAddress.setStatus("current")
_NqaTcpServerPort_Type = InetPortNumber
_NqaTcpServerPort_Object = MibTableColumn
nqaTcpServerPort = _NqaTcpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 2, 1, 3),
    _NqaTcpServerPort_Type()
)
nqaTcpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaTcpServerPort.setStatus("current")


class _NqaTcpServerVrfName_Type(DisplayString):
    """Custom type nqaTcpServerVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_NqaTcpServerVrfName_Type.__name__ = "DisplayString"
_NqaTcpServerVrfName_Object = MibTableColumn
nqaTcpServerVrfName = _NqaTcpServerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 2, 1, 4),
    _NqaTcpServerVrfName_Type()
)
nqaTcpServerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaTcpServerVrfName.setStatus("current")
_NqaTcpServerStatus_Type = RowStatus
_NqaTcpServerStatus_Object = MibTableColumn
nqaTcpServerStatus = _NqaTcpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 2, 1, 5),
    _NqaTcpServerStatus_Type()
)
nqaTcpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaTcpServerStatus.setStatus("current")
_NqaUdpServerTable_Object = MibTable
nqaUdpServerTable = _NqaUdpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 3)
)
if mibBuilder.loadTexts:
    nqaUdpServerTable.setStatus("current")
_NqaUdpServerEntry_Object = MibTableRow
nqaUdpServerEntry = _NqaUdpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 3, 1)
)
nqaUdpServerEntry.setIndexNames(
    (0, "NQA-MIB", "nqaUdpServerAddress"),
    (0, "NQA-MIB", "nqaUdpServerPort"),
    (0, "NQA-MIB", "nqaUdpServerVrfName"),
)
if mibBuilder.loadTexts:
    nqaUdpServerEntry.setStatus("current")


class _NqaUdpServerAddressType_Type(InetAddressType):
    """Custom type nqaUdpServerAddressType based on InetAddressType"""


_NqaUdpServerAddressType_Object = MibTableColumn
nqaUdpServerAddressType = _NqaUdpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 3, 1, 1),
    _NqaUdpServerAddressType_Type()
)
nqaUdpServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaUdpServerAddressType.setStatus("current")
_NqaUdpServerAddress_Type = InetAddress
_NqaUdpServerAddress_Object = MibTableColumn
nqaUdpServerAddress = _NqaUdpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 3, 1, 2),
    _NqaUdpServerAddress_Type()
)
nqaUdpServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaUdpServerAddress.setStatus("current")
_NqaUdpServerPort_Type = InetPortNumber
_NqaUdpServerPort_Object = MibTableColumn
nqaUdpServerPort = _NqaUdpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 3, 1, 3),
    _NqaUdpServerPort_Type()
)
nqaUdpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaUdpServerPort.setStatus("current")


class _NqaUdpServerVrfName_Type(DisplayString):
    """Custom type nqaUdpServerVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_NqaUdpServerVrfName_Type.__name__ = "DisplayString"
_NqaUdpServerVrfName_Object = MibTableColumn
nqaUdpServerVrfName = _NqaUdpServerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 3, 1, 4),
    _NqaUdpServerVrfName_Type()
)
nqaUdpServerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaUdpServerVrfName.setStatus("current")
_NqaUdpServerStatus_Type = RowStatus
_NqaUdpServerStatus_Object = MibTableColumn
nqaUdpServerStatus = _NqaUdpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 3, 1, 5),
    _NqaUdpServerStatus_Type()
)
nqaUdpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaUdpServerStatus.setStatus("current")
_NqaIcmpServerTable_Object = MibTable
nqaIcmpServerTable = _NqaIcmpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 4)
)
if mibBuilder.loadTexts:
    nqaIcmpServerTable.setStatus("current")
_NqaIcmpServerEntry_Object = MibTableRow
nqaIcmpServerEntry = _NqaIcmpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 4, 1)
)
nqaIcmpServerEntry.setIndexNames(
    (0, "NQA-MIB", "nqaIcmpServerAddress"),
    (0, "NQA-MIB", "nqaIcmpServerVrfName"),
)
if mibBuilder.loadTexts:
    nqaIcmpServerEntry.setStatus("current")
_NqaIcmpServerAddress_Type = InetAddress
_NqaIcmpServerAddress_Object = MibTableColumn
nqaIcmpServerAddress = _NqaIcmpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 4, 1, 1),
    _NqaIcmpServerAddress_Type()
)
nqaIcmpServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaIcmpServerAddress.setStatus("current")


class _NqaIcmpServerVrfName_Type(DisplayString):
    """Custom type nqaIcmpServerVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_NqaIcmpServerVrfName_Type.__name__ = "DisplayString"
_NqaIcmpServerVrfName_Object = MibTableColumn
nqaIcmpServerVrfName = _NqaIcmpServerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 4, 1, 2),
    _NqaIcmpServerVrfName_Type()
)
nqaIcmpServerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaIcmpServerVrfName.setStatus("current")


class _NqaIcmpServerAddressType_Type(InetAddressType):
    """Custom type nqaIcmpServerAddressType based on InetAddressType"""


_NqaIcmpServerAddressType_Object = MibTableColumn
nqaIcmpServerAddressType = _NqaIcmpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 4, 1, 3),
    _NqaIcmpServerAddressType_Type()
)
nqaIcmpServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaIcmpServerAddressType.setStatus("current")
_NqaIcmpServerStatus_Type = RowStatus
_NqaIcmpServerStatus_Object = MibTableColumn
nqaIcmpServerStatus = _NqaIcmpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 3, 4, 1, 51),
    _NqaIcmpServerStatus_Type()
)
nqaIcmpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaIcmpServerStatus.setStatus("current")
_NqaStats_ObjectIdentity = ObjectIdentity
nqaStats = _NqaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4)
)
_NqaResultsTable_Object = MibTable
nqaResultsTable = _NqaResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1)
)
if mibBuilder.loadTexts:
    nqaResultsTable.setStatus("current")
_NqaResultsEntry_Object = MibTableRow
nqaResultsEntry = _NqaResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1)
)
nqaResultsEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaResultsIndex"),
    (0, "NQA-MIB", "nqaResultsHopIndex"),
)
if mibBuilder.loadTexts:
    nqaResultsEntry.setStatus("current")


class _NqaResultsIndex_Type(Integer32):
    """Custom type nqaResultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaResultsIndex_Type.__name__ = "Integer32"
_NqaResultsIndex_Object = MibTableColumn
nqaResultsIndex = _NqaResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 1),
    _NqaResultsIndex_Type()
)
nqaResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaResultsIndex.setStatus("current")


class _NqaResultsHopIndex_Type(Integer32):
    """Custom type nqaResultsHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaResultsHopIndex_Type.__name__ = "Integer32"
_NqaResultsHopIndex_Object = MibTableColumn
nqaResultsHopIndex = _NqaResultsHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 2),
    _NqaResultsHopIndex_Type()
)
nqaResultsHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaResultsHopIndex.setStatus("current")


class _NqaResultsCompletions_Type(Integer32):
    """Custom type nqaResultsCompletions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("noResult", 0),
          ("success", 1))
    )


_NqaResultsCompletions_Type.__name__ = "Integer32"
_NqaResultsCompletions_Object = MibTableColumn
nqaResultsCompletions = _NqaResultsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 3),
    _NqaResultsCompletions_Type()
)
nqaResultsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsCompletions.setStatus("current")
_NqaResultsTestAttempts_Type = Counter32
_NqaResultsTestAttempts_Object = MibTableColumn
nqaResultsTestAttempts = _NqaResultsTestAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 4),
    _NqaResultsTestAttempts_Type()
)
nqaResultsTestAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsTestAttempts.setStatus("current")
if mibBuilder.loadTexts:
    nqaResultsTestAttempts.setUnits("tests")
_NqaResultsCurHopCount_Type = Gauge32
_NqaResultsCurHopCount_Object = MibTableColumn
nqaResultsCurHopCount = _NqaResultsCurHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 5),
    _NqaResultsCurHopCount_Type()
)
nqaResultsCurHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsCurHopCount.setStatus("current")
if mibBuilder.loadTexts:
    nqaResultsCurHopCount.setUnits("hops")
_NqaResultsCurProbeCount_Type = Gauge32
_NqaResultsCurProbeCount_Object = MibTableColumn
nqaResultsCurProbeCount = _NqaResultsCurProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 6),
    _NqaResultsCurProbeCount_Type()
)
nqaResultsCurProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsCurProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    nqaResultsCurProbeCount.setUnits("probes")
_NqaResultsRTDOverThresholds_Type = Counter32
_NqaResultsRTDOverThresholds_Object = MibTableColumn
nqaResultsRTDOverThresholds = _NqaResultsRTDOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 7),
    _NqaResultsRTDOverThresholds_Type()
)
nqaResultsRTDOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsRTDOverThresholds.setStatus("current")
_NqaResultsSumCompletionTime_Type = Counter32
_NqaResultsSumCompletionTime_Object = MibTableColumn
nqaResultsSumCompletionTime = _NqaResultsSumCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 8),
    _NqaResultsSumCompletionTime_Type()
)
nqaResultsSumCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsSumCompletionTime.setStatus("current")
_NqaResultsSumCompletionTime2Low_Type = Counter32
_NqaResultsSumCompletionTime2Low_Object = MibTableColumn
nqaResultsSumCompletionTime2Low = _NqaResultsSumCompletionTime2Low_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 9),
    _NqaResultsSumCompletionTime2Low_Type()
)
nqaResultsSumCompletionTime2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsSumCompletionTime2Low.setStatus("current")
_NqaResultsSumCompletionTime2High_Type = Counter32
_NqaResultsSumCompletionTime2High_Object = MibTableColumn
nqaResultsSumCompletionTime2High = _NqaResultsSumCompletionTime2High_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 10),
    _NqaResultsSumCompletionTime2High_Type()
)
nqaResultsSumCompletionTime2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsSumCompletionTime2High.setStatus("current")
_NqaResultsCompletionTimeMin_Type = Gauge32
_NqaResultsCompletionTimeMin_Object = MibTableColumn
nqaResultsCompletionTimeMin = _NqaResultsCompletionTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 11),
    _NqaResultsCompletionTimeMin_Type()
)
nqaResultsCompletionTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsCompletionTimeMin.setStatus("current")
_NqaResultsCompletionTimeMax_Type = Gauge32
_NqaResultsCompletionTimeMax_Object = MibTableColumn
nqaResultsCompletionTimeMax = _NqaResultsCompletionTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 12),
    _NqaResultsCompletionTimeMax_Type()
)
nqaResultsCompletionTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsCompletionTimeMax.setStatus("current")
_NqaResultsDisconnects_Type = Counter32
_NqaResultsDisconnects_Object = MibTableColumn
nqaResultsDisconnects = _NqaResultsDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 13),
    _NqaResultsDisconnects_Type()
)
nqaResultsDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsDisconnects.setStatus("current")
_NqaResultsTimeouts_Type = Counter32
_NqaResultsTimeouts_Object = MibTableColumn
nqaResultsTimeouts = _NqaResultsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 14),
    _NqaResultsTimeouts_Type()
)
nqaResultsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsTimeouts.setStatus("current")
_NqaResultsBusies_Type = Counter32
_NqaResultsBusies_Object = MibTableColumn
nqaResultsBusies = _NqaResultsBusies_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 15),
    _NqaResultsBusies_Type()
)
nqaResultsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsBusies.setStatus("current")
_NqaResultsNoConnections_Type = Counter32
_NqaResultsNoConnections_Object = MibTableColumn
nqaResultsNoConnections = _NqaResultsNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 16),
    _NqaResultsNoConnections_Type()
)
nqaResultsNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsNoConnections.setStatus("current")
_NqaResultsSequenceErrors_Type = Counter32
_NqaResultsSequenceErrors_Object = MibTableColumn
nqaResultsSequenceErrors = _NqaResultsSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 17),
    _NqaResultsSequenceErrors_Type()
)
nqaResultsSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsSequenceErrors.setStatus("current")
_NqaResultsDrops_Type = Counter32
_NqaResultsDrops_Object = MibTableColumn
nqaResultsDrops = _NqaResultsDrops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 18),
    _NqaResultsDrops_Type()
)
nqaResultsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsDrops.setStatus("current")
_NqaResultsAddressType_Type = InetAddressType
_NqaResultsAddressType_Object = MibTableColumn
nqaResultsAddressType = _NqaResultsAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 19),
    _NqaResultsAddressType_Type()
)
nqaResultsAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsAddressType.setStatus("current")
_NqaResultsAddress_Type = InetAddress
_NqaResultsAddress_Object = MibTableColumn
nqaResultsAddress = _NqaResultsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 20),
    _NqaResultsAddress_Type()
)
nqaResultsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsAddress.setStatus("current")
_NqaResultsProbeResponses_Type = Counter32
_NqaResultsProbeResponses_Object = MibTableColumn
nqaResultsProbeResponses = _NqaResultsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 21),
    _NqaResultsProbeResponses_Type()
)
nqaResultsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    nqaResultsProbeResponses.setUnits("responses")
_NqaResultsSentProbes_Type = Counter32
_NqaResultsSentProbes_Object = MibTableColumn
nqaResultsSentProbes = _NqaResultsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 22),
    _NqaResultsSentProbes_Type()
)
nqaResultsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    nqaResultsSentProbes.setUnits("probes")
_NqaResultsLastGoodProbe_Type = DateAndTime
_NqaResultsLastGoodProbe_Object = MibTableColumn
nqaResultsLastGoodProbe = _NqaResultsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 23),
    _NqaResultsLastGoodProbe_Type()
)
nqaResultsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsLastGoodProbe.setStatus("current")
_NqaResultsLastGoodPath_Type = DateAndTime
_NqaResultsLastGoodPath_Object = MibTableColumn
nqaResultsLastGoodPath = _NqaResultsLastGoodPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 24),
    _NqaResultsLastGoodPath_Type()
)
nqaResultsLastGoodPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsLastGoodPath.setStatus("current")


class _NqaResultsTestFinished_Type(Integer32):
    """Custom type nqaResultsTestFinished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finish", 1),
          ("noFinish", 0))
    )


_NqaResultsTestFinished_Type.__name__ = "Integer32"
_NqaResultsTestFinished_Object = MibTableColumn
nqaResultsTestFinished = _NqaResultsTestFinished_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 25),
    _NqaResultsTestFinished_Type()
)
nqaResultsTestFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsTestFinished.setStatus("current")
_NqaResultsRttAvg_Type = Gauge32
_NqaResultsRttAvg_Object = MibTableColumn
nqaResultsRttAvg = _NqaResultsRttAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 26),
    _NqaResultsRttAvg_Type()
)
nqaResultsRttAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsRttAvg.setStatus("current")
_NqaResultsLostPacketRatio_Type = Gauge32
_NqaResultsLostPacketRatio_Object = MibTableColumn
nqaResultsLostPacketRatio = _NqaResultsLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 1, 1, 27),
    _NqaResultsLostPacketRatio_Type()
)
nqaResultsLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaResultsLostPacketRatio.setStatus("current")
_NqaHTTPStatsTable_Object = MibTable
nqaHTTPStatsTable = _NqaHTTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2)
)
if mibBuilder.loadTexts:
    nqaHTTPStatsTable.setStatus("current")
_NqaHTTPStatsEntry_Object = MibTableRow
nqaHTTPStatsEntry = _NqaHTTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1)
)
nqaHTTPStatsEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaHTTPStatsIndex"),
)
if mibBuilder.loadTexts:
    nqaHTTPStatsEntry.setStatus("current")


class _NqaHTTPStatsIndex_Type(Integer32):
    """Custom type nqaHTTPStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaHTTPStatsIndex_Type.__name__ = "Integer32"
_NqaHTTPStatsIndex_Object = MibTableColumn
nqaHTTPStatsIndex = _NqaHTTPStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 1),
    _NqaHTTPStatsIndex_Type()
)
nqaHTTPStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaHTTPStatsIndex.setStatus("current")


class _NqaHTTPStatsCompletions_Type(Integer32):
    """Custom type nqaHTTPStatsCompletions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("noResult", 0),
          ("success", 1))
    )


_NqaHTTPStatsCompletions_Type.__name__ = "Integer32"
_NqaHTTPStatsCompletions_Object = MibTableColumn
nqaHTTPStatsCompletions = _NqaHTTPStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 2),
    _NqaHTTPStatsCompletions_Type()
)
nqaHTTPStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsCompletions.setStatus("current")
_NqaHTTPStatsRTDOverThresholds_Type = Counter32
_NqaHTTPStatsRTDOverThresholds_Object = MibTableColumn
nqaHTTPStatsRTDOverThresholds = _NqaHTTPStatsRTDOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 3),
    _NqaHTTPStatsRTDOverThresholds_Type()
)
nqaHTTPStatsRTDOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsRTDOverThresholds.setStatus("current")
_NqaHTTPStatsRTTSum_Type = Counter32
_NqaHTTPStatsRTTSum_Object = MibTableColumn
nqaHTTPStatsRTTSum = _NqaHTTPStatsRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 4),
    _NqaHTTPStatsRTTSum_Type()
)
nqaHTTPStatsRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsRTTSum.setStatus("current")
_NqaHTTPStatsRTTMin_Type = Gauge32
_NqaHTTPStatsRTTMin_Object = MibTableColumn
nqaHTTPStatsRTTMin = _NqaHTTPStatsRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 5),
    _NqaHTTPStatsRTTMin_Type()
)
nqaHTTPStatsRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsRTTMin.setStatus("current")
_NqaHTTPStatsRTTMax_Type = Gauge32
_NqaHTTPStatsRTTMax_Object = MibTableColumn
nqaHTTPStatsRTTMax = _NqaHTTPStatsRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 6),
    _NqaHTTPStatsRTTMax_Type()
)
nqaHTTPStatsRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsRTTMax.setStatus("current")
_NqaHTTPStatsDNSRTTSum_Type = Counter32
_NqaHTTPStatsDNSRTTSum_Object = MibTableColumn
nqaHTTPStatsDNSRTTSum = _NqaHTTPStatsDNSRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 7),
    _NqaHTTPStatsDNSRTTSum_Type()
)
nqaHTTPStatsDNSRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsDNSRTTSum.setStatus("current")
_NqaHTTPStatsDNSRTTMin_Type = Gauge32
_NqaHTTPStatsDNSRTTMin_Object = MibTableColumn
nqaHTTPStatsDNSRTTMin = _NqaHTTPStatsDNSRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 8),
    _NqaHTTPStatsDNSRTTMin_Type()
)
nqaHTTPStatsDNSRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsDNSRTTMin.setStatus("current")
_NqaHTTPStatsDNSRTTMax_Type = Gauge32
_NqaHTTPStatsDNSRTTMax_Object = MibTableColumn
nqaHTTPStatsDNSRTTMax = _NqaHTTPStatsDNSRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 9),
    _NqaHTTPStatsDNSRTTMax_Type()
)
nqaHTTPStatsDNSRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsDNSRTTMax.setStatus("current")
_NqaHTTPStatsTCPConnectRTTSum_Type = Counter32
_NqaHTTPStatsTCPConnectRTTSum_Object = MibTableColumn
nqaHTTPStatsTCPConnectRTTSum = _NqaHTTPStatsTCPConnectRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 10),
    _NqaHTTPStatsTCPConnectRTTSum_Type()
)
nqaHTTPStatsTCPConnectRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsTCPConnectRTTSum.setStatus("current")
_NqaHTTPStatsTCPConnectRTTMin_Type = Gauge32
_NqaHTTPStatsTCPConnectRTTMin_Object = MibTableColumn
nqaHTTPStatsTCPConnectRTTMin = _NqaHTTPStatsTCPConnectRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 11),
    _NqaHTTPStatsTCPConnectRTTMin_Type()
)
nqaHTTPStatsTCPConnectRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsTCPConnectRTTMin.setStatus("current")
_NqaHTTPStatsTCPConnectRTTMax_Type = Gauge32
_NqaHTTPStatsTCPConnectRTTMax_Object = MibTableColumn
nqaHTTPStatsTCPConnectRTTMax = _NqaHTTPStatsTCPConnectRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 12),
    _NqaHTTPStatsTCPConnectRTTMax_Type()
)
nqaHTTPStatsTCPConnectRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsTCPConnectRTTMax.setStatus("current")
_NqaHTTPStatsTransactionRTTSum_Type = Counter32
_NqaHTTPStatsTransactionRTTSum_Object = MibTableColumn
nqaHTTPStatsTransactionRTTSum = _NqaHTTPStatsTransactionRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 13),
    _NqaHTTPStatsTransactionRTTSum_Type()
)
nqaHTTPStatsTransactionRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsTransactionRTTSum.setStatus("current")
_NqaHTTPStatsTransactionRTTMin_Type = Gauge32
_NqaHTTPStatsTransactionRTTMin_Object = MibTableColumn
nqaHTTPStatsTransactionRTTMin = _NqaHTTPStatsTransactionRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 14),
    _NqaHTTPStatsTransactionRTTMin_Type()
)
nqaHTTPStatsTransactionRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsTransactionRTTMin.setStatus("current")
_NqaHTTPStatsTransactionRTTMax_Type = Gauge32
_NqaHTTPStatsTransactionRTTMax_Object = MibTableColumn
nqaHTTPStatsTransactionRTTMax = _NqaHTTPStatsTransactionRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 15),
    _NqaHTTPStatsTransactionRTTMax_Type()
)
nqaHTTPStatsTransactionRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsTransactionRTTMax.setStatus("current")
_NqaHTTPStatsMessageBodyOctetsSum_Type = Counter32
_NqaHTTPStatsMessageBodyOctetsSum_Object = MibTableColumn
nqaHTTPStatsMessageBodyOctetsSum = _NqaHTTPStatsMessageBodyOctetsSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 16),
    _NqaHTTPStatsMessageBodyOctetsSum_Type()
)
nqaHTTPStatsMessageBodyOctetsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsMessageBodyOctetsSum.setStatus("current")
_NqaHTTPStatsDNSServerTimeouts_Type = Counter32
_NqaHTTPStatsDNSServerTimeouts_Object = MibTableColumn
nqaHTTPStatsDNSServerTimeouts = _NqaHTTPStatsDNSServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 17),
    _NqaHTTPStatsDNSServerTimeouts_Type()
)
nqaHTTPStatsDNSServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsDNSServerTimeouts.setStatus("current")
_NqaHTTPStatsTCPConnectTimeouts_Type = Counter32
_NqaHTTPStatsTCPConnectTimeouts_Object = MibTableColumn
nqaHTTPStatsTCPConnectTimeouts = _NqaHTTPStatsTCPConnectTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 18),
    _NqaHTTPStatsTCPConnectTimeouts_Type()
)
nqaHTTPStatsTCPConnectTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsTCPConnectTimeouts.setStatus("current")
_NqaHTTPStatsTransactionTimeouts_Type = Counter32
_NqaHTTPStatsTransactionTimeouts_Object = MibTableColumn
nqaHTTPStatsTransactionTimeouts = _NqaHTTPStatsTransactionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 19),
    _NqaHTTPStatsTransactionTimeouts_Type()
)
nqaHTTPStatsTransactionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsTransactionTimeouts.setStatus("current")
_NqaHTTPStatsDNSQueryErrors_Type = Counter32
_NqaHTTPStatsDNSQueryErrors_Object = MibTableColumn
nqaHTTPStatsDNSQueryErrors = _NqaHTTPStatsDNSQueryErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 20),
    _NqaHTTPStatsDNSQueryErrors_Type()
)
nqaHTTPStatsDNSQueryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsDNSQueryErrors.setStatus("current")
_NqaHTTPStatsErrors_Type = Counter32
_NqaHTTPStatsErrors_Object = MibTableColumn
nqaHTTPStatsErrors = _NqaHTTPStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 21),
    _NqaHTTPStatsErrors_Type()
)
nqaHTTPStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsErrors.setStatus("current")
_NqaHTTPStatsTcpConnErrors_Type = Counter32
_NqaHTTPStatsTcpConnErrors_Object = MibTableColumn
nqaHTTPStatsTcpConnErrors = _NqaHTTPStatsTcpConnErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 22),
    _NqaHTTPStatsTcpConnErrors_Type()
)
nqaHTTPStatsTcpConnErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsTcpConnErrors.setStatus("current")
_NqaHTTPStatsProbeResponses_Type = Counter32
_NqaHTTPStatsProbeResponses_Object = MibTableColumn
nqaHTTPStatsProbeResponses = _NqaHTTPStatsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 23),
    _NqaHTTPStatsProbeResponses_Type()
)
nqaHTTPStatsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsProbeResponses.setStatus("current")
_NqaHTTPStatsSendProbes_Type = Counter32
_NqaHTTPStatsSendProbes_Object = MibTableColumn
nqaHTTPStatsSendProbes = _NqaHTTPStatsSendProbes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 24),
    _NqaHTTPStatsSendProbes_Type()
)
nqaHTTPStatsSendProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsSendProbes.setStatus("current")
_NqaHTTPStatsBusies_Type = Counter32
_NqaHTTPStatsBusies_Object = MibTableColumn
nqaHTTPStatsBusies = _NqaHTTPStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 25),
    _NqaHTTPStatsBusies_Type()
)
nqaHTTPStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsBusies.setStatus("current")


class _NqaHTTPStatsTestFinished_Type(Integer32):
    """Custom type nqaHTTPStatsTestFinished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finish", 1),
          ("noFinish", 0))
    )


_NqaHTTPStatsTestFinished_Type.__name__ = "Integer32"
_NqaHTTPStatsTestFinished_Object = MibTableColumn
nqaHTTPStatsTestFinished = _NqaHTTPStatsTestFinished_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 26),
    _NqaHTTPStatsTestFinished_Type()
)
nqaHTTPStatsTestFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsTestFinished.setStatus("current")
_NqaHTTPStatsRttAvg_Type = Gauge32
_NqaHTTPStatsRttAvg_Object = MibTableColumn
nqaHTTPStatsRttAvg = _NqaHTTPStatsRttAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 27),
    _NqaHTTPStatsRttAvg_Type()
)
nqaHTTPStatsRttAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsRttAvg.setStatus("current")
_NqaHTTPStatsLostPacketRatio_Type = Gauge32
_NqaHTTPStatsLostPacketRatio_Object = MibTableColumn
nqaHTTPStatsLostPacketRatio = _NqaHTTPStatsLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 2, 1, 28),
    _NqaHTTPStatsLostPacketRatio_Type()
)
nqaHTTPStatsLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHTTPStatsLostPacketRatio.setStatus("current")
_NqaJitterStatsTable_Object = MibTable
nqaJitterStatsTable = _NqaJitterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3)
)
if mibBuilder.loadTexts:
    nqaJitterStatsTable.setStatus("current")
_NqaJitterStatsEntry_Object = MibTableRow
nqaJitterStatsEntry = _NqaJitterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1)
)
nqaJitterStatsEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaJitterStatsIndex"),
)
if mibBuilder.loadTexts:
    nqaJitterStatsEntry.setStatus("current")


class _NqaJitterStatsIndex_Type(Integer32):
    """Custom type nqaJitterStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaJitterStatsIndex_Type.__name__ = "Integer32"
_NqaJitterStatsIndex_Object = MibTableColumn
nqaJitterStatsIndex = _NqaJitterStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 1),
    _NqaJitterStatsIndex_Type()
)
nqaJitterStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaJitterStatsIndex.setStatus("current")


class _NqaJitterStatsCompletions_Type(Integer32):
    """Custom type nqaJitterStatsCompletions based on Integer32"""
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
        *(("failure", 2),
          ("negotiateFailed", 3),
          ("noResult", 0),
          ("success", 1))
    )


_NqaJitterStatsCompletions_Type.__name__ = "Integer32"
_NqaJitterStatsCompletions_Object = MibTableColumn
nqaJitterStatsCompletions = _NqaJitterStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 2),
    _NqaJitterStatsCompletions_Type()
)
nqaJitterStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsCompletions.setStatus("current")
_NqaJitterStatsRTDOverThresholds_Type = Counter32
_NqaJitterStatsRTDOverThresholds_Object = MibTableColumn
nqaJitterStatsRTDOverThresholds = _NqaJitterStatsRTDOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 3),
    _NqaJitterStatsRTDOverThresholds_Type()
)
nqaJitterStatsRTDOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsRTDOverThresholds.setStatus("current")
_NqaJitterStatsNumOfRTT_Type = Counter32
_NqaJitterStatsNumOfRTT_Object = MibTableColumn
nqaJitterStatsNumOfRTT = _NqaJitterStatsNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 4),
    _NqaJitterStatsNumOfRTT_Type()
)
nqaJitterStatsNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsNumOfRTT.setStatus("current")
_NqaJitterStatsRTTSum_Type = Counter32
_NqaJitterStatsRTTSum_Object = MibTableColumn
nqaJitterStatsRTTSum = _NqaJitterStatsRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 5),
    _NqaJitterStatsRTTSum_Type()
)
nqaJitterStatsRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsRTTSum.setStatus("current")
_NqaJitterStatsRTTSum2Low_Type = Counter32
_NqaJitterStatsRTTSum2Low_Object = MibTableColumn
nqaJitterStatsRTTSum2Low = _NqaJitterStatsRTTSum2Low_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 6),
    _NqaJitterStatsRTTSum2Low_Type()
)
nqaJitterStatsRTTSum2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsRTTSum2Low.setStatus("current")
_NqaJitterStatsRTTSum2High_Type = Counter32
_NqaJitterStatsRTTSum2High_Object = MibTableColumn
nqaJitterStatsRTTSum2High = _NqaJitterStatsRTTSum2High_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 7),
    _NqaJitterStatsRTTSum2High_Type()
)
nqaJitterStatsRTTSum2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsRTTSum2High.setStatus("current")
_NqaJitterStatsRTTMin_Type = Gauge32
_NqaJitterStatsRTTMin_Object = MibTableColumn
nqaJitterStatsRTTMin = _NqaJitterStatsRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 8),
    _NqaJitterStatsRTTMin_Type()
)
nqaJitterStatsRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsRTTMin.setStatus("current")
_NqaJitterStatsRTTMax_Type = Gauge32
_NqaJitterStatsRTTMax_Object = MibTableColumn
nqaJitterStatsRTTMax = _NqaJitterStatsRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 9),
    _NqaJitterStatsRTTMax_Type()
)
nqaJitterStatsRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsRTTMax.setStatus("current")
_NqaJitterStatsMinOfPositivesSD_Type = Gauge32
_NqaJitterStatsMinOfPositivesSD_Object = MibTableColumn
nqaJitterStatsMinOfPositivesSD = _NqaJitterStatsMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 10),
    _NqaJitterStatsMinOfPositivesSD_Type()
)
nqaJitterStatsMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMinOfPositivesSD.setStatus("current")
_NqaJitterStatsMaxOfPositivesSD_Type = Gauge32
_NqaJitterStatsMaxOfPositivesSD_Object = MibTableColumn
nqaJitterStatsMaxOfPositivesSD = _NqaJitterStatsMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 11),
    _NqaJitterStatsMaxOfPositivesSD_Type()
)
nqaJitterStatsMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMaxOfPositivesSD.setStatus("current")
_NqaJitterStatsNumOfPositivesSD_Type = Counter32
_NqaJitterStatsNumOfPositivesSD_Object = MibTableColumn
nqaJitterStatsNumOfPositivesSD = _NqaJitterStatsNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 12),
    _NqaJitterStatsNumOfPositivesSD_Type()
)
nqaJitterStatsNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsNumOfPositivesSD.setStatus("current")
_NqaJitterStatsSumOfPositivesSD_Type = Counter32
_NqaJitterStatsSumOfPositivesSD_Object = MibTableColumn
nqaJitterStatsSumOfPositivesSD = _NqaJitterStatsSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 13),
    _NqaJitterStatsSumOfPositivesSD_Type()
)
nqaJitterStatsSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSumOfPositivesSD.setStatus("current")
_NqaJitterStatsSum2OfPositivesSDLow_Type = Counter32
_NqaJitterStatsSum2OfPositivesSDLow_Object = MibTableColumn
nqaJitterStatsSum2OfPositivesSDLow = _NqaJitterStatsSum2OfPositivesSDLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 14),
    _NqaJitterStatsSum2OfPositivesSDLow_Type()
)
nqaJitterStatsSum2OfPositivesSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2OfPositivesSDLow.setStatus("current")
_NqaJitterStatsSum2OfPositivesSDHigh_Type = Counter32
_NqaJitterStatsSum2OfPositivesSDHigh_Object = MibTableColumn
nqaJitterStatsSum2OfPositivesSDHigh = _NqaJitterStatsSum2OfPositivesSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 15),
    _NqaJitterStatsSum2OfPositivesSDHigh_Type()
)
nqaJitterStatsSum2OfPositivesSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2OfPositivesSDHigh.setStatus("current")
_NqaJitterStatsMinOfNegativesSD_Type = Gauge32
_NqaJitterStatsMinOfNegativesSD_Object = MibTableColumn
nqaJitterStatsMinOfNegativesSD = _NqaJitterStatsMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 16),
    _NqaJitterStatsMinOfNegativesSD_Type()
)
nqaJitterStatsMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMinOfNegativesSD.setStatus("current")
_NqaJitterStatsMaxOfNegativesSD_Type = Gauge32
_NqaJitterStatsMaxOfNegativesSD_Object = MibTableColumn
nqaJitterStatsMaxOfNegativesSD = _NqaJitterStatsMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 17),
    _NqaJitterStatsMaxOfNegativesSD_Type()
)
nqaJitterStatsMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMaxOfNegativesSD.setStatus("current")
_NqaJitterStatsNumOfNegativesSD_Type = Counter32
_NqaJitterStatsNumOfNegativesSD_Object = MibTableColumn
nqaJitterStatsNumOfNegativesSD = _NqaJitterStatsNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 18),
    _NqaJitterStatsNumOfNegativesSD_Type()
)
nqaJitterStatsNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsNumOfNegativesSD.setStatus("current")
_NqaJitterStatsSumOfNegativesSD_Type = Counter32
_NqaJitterStatsSumOfNegativesSD_Object = MibTableColumn
nqaJitterStatsSumOfNegativesSD = _NqaJitterStatsSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 19),
    _NqaJitterStatsSumOfNegativesSD_Type()
)
nqaJitterStatsSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSumOfNegativesSD.setStatus("current")
_NqaJitterStatsSum2OfNegativesSDLow_Type = Counter32
_NqaJitterStatsSum2OfNegativesSDLow_Object = MibTableColumn
nqaJitterStatsSum2OfNegativesSDLow = _NqaJitterStatsSum2OfNegativesSDLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 20),
    _NqaJitterStatsSum2OfNegativesSDLow_Type()
)
nqaJitterStatsSum2OfNegativesSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2OfNegativesSDLow.setStatus("current")
_NqaJitterStatsSum2OfNegativesSDHigh_Type = Counter32
_NqaJitterStatsSum2OfNegativesSDHigh_Object = MibTableColumn
nqaJitterStatsSum2OfNegativesSDHigh = _NqaJitterStatsSum2OfNegativesSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 21),
    _NqaJitterStatsSum2OfNegativesSDHigh_Type()
)
nqaJitterStatsSum2OfNegativesSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2OfNegativesSDHigh.setStatus("current")
_NqaJitterStatsMinOfPositivesDS_Type = Gauge32
_NqaJitterStatsMinOfPositivesDS_Object = MibTableColumn
nqaJitterStatsMinOfPositivesDS = _NqaJitterStatsMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 22),
    _NqaJitterStatsMinOfPositivesDS_Type()
)
nqaJitterStatsMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMinOfPositivesDS.setStatus("current")
_NqaJitterStatsMaxOfPositivesDS_Type = Gauge32
_NqaJitterStatsMaxOfPositivesDS_Object = MibTableColumn
nqaJitterStatsMaxOfPositivesDS = _NqaJitterStatsMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 23),
    _NqaJitterStatsMaxOfPositivesDS_Type()
)
nqaJitterStatsMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMaxOfPositivesDS.setStatus("current")
_NqaJitterStatsNumOfPositivesDS_Type = Counter32
_NqaJitterStatsNumOfPositivesDS_Object = MibTableColumn
nqaJitterStatsNumOfPositivesDS = _NqaJitterStatsNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 24),
    _NqaJitterStatsNumOfPositivesDS_Type()
)
nqaJitterStatsNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsNumOfPositivesDS.setStatus("current")
_NqaJitterStatsSumOfPositivesDS_Type = Counter32
_NqaJitterStatsSumOfPositivesDS_Object = MibTableColumn
nqaJitterStatsSumOfPositivesDS = _NqaJitterStatsSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 25),
    _NqaJitterStatsSumOfPositivesDS_Type()
)
nqaJitterStatsSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSumOfPositivesDS.setStatus("current")
_NqaJitterStatsSum2OfPositivesDSLow_Type = Counter32
_NqaJitterStatsSum2OfPositivesDSLow_Object = MibTableColumn
nqaJitterStatsSum2OfPositivesDSLow = _NqaJitterStatsSum2OfPositivesDSLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 26),
    _NqaJitterStatsSum2OfPositivesDSLow_Type()
)
nqaJitterStatsSum2OfPositivesDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2OfPositivesDSLow.setStatus("current")
_NqaJitterStatsSum2OfPositivesDSHigh_Type = Counter32
_NqaJitterStatsSum2OfPositivesDSHigh_Object = MibTableColumn
nqaJitterStatsSum2OfPositivesDSHigh = _NqaJitterStatsSum2OfPositivesDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 27),
    _NqaJitterStatsSum2OfPositivesDSHigh_Type()
)
nqaJitterStatsSum2OfPositivesDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2OfPositivesDSHigh.setStatus("current")
_NqaJitterStatsMinOfNegativesDS_Type = Gauge32
_NqaJitterStatsMinOfNegativesDS_Object = MibTableColumn
nqaJitterStatsMinOfNegativesDS = _NqaJitterStatsMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 28),
    _NqaJitterStatsMinOfNegativesDS_Type()
)
nqaJitterStatsMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMinOfNegativesDS.setStatus("current")
_NqaJitterStatsMaxOfNegativesDS_Type = Gauge32
_NqaJitterStatsMaxOfNegativesDS_Object = MibTableColumn
nqaJitterStatsMaxOfNegativesDS = _NqaJitterStatsMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 29),
    _NqaJitterStatsMaxOfNegativesDS_Type()
)
nqaJitterStatsMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMaxOfNegativesDS.setStatus("current")
_NqaJitterStatsNumOfNegativesDS_Type = Counter32
_NqaJitterStatsNumOfNegativesDS_Object = MibTableColumn
nqaJitterStatsNumOfNegativesDS = _NqaJitterStatsNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 30),
    _NqaJitterStatsNumOfNegativesDS_Type()
)
nqaJitterStatsNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsNumOfNegativesDS.setStatus("current")
_NqaJitterStatsSumOfNegativesDS_Type = Counter32
_NqaJitterStatsSumOfNegativesDS_Object = MibTableColumn
nqaJitterStatsSumOfNegativesDS = _NqaJitterStatsSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 31),
    _NqaJitterStatsSumOfNegativesDS_Type()
)
nqaJitterStatsSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSumOfNegativesDS.setStatus("current")
_NqaJitterStatsSum2OfNegativesDSLow_Type = Counter32
_NqaJitterStatsSum2OfNegativesDSLow_Object = MibTableColumn
nqaJitterStatsSum2OfNegativesDSLow = _NqaJitterStatsSum2OfNegativesDSLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 32),
    _NqaJitterStatsSum2OfNegativesDSLow_Type()
)
nqaJitterStatsSum2OfNegativesDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2OfNegativesDSLow.setStatus("current")
_NqaJitterStatsSum2OfNegativesDSHigh_Type = Counter32
_NqaJitterStatsSum2OfNegativesDSHigh_Object = MibTableColumn
nqaJitterStatsSum2OfNegativesDSHigh = _NqaJitterStatsSum2OfNegativesDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 33),
    _NqaJitterStatsSum2OfNegativesDSHigh_Type()
)
nqaJitterStatsSum2OfNegativesDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2OfNegativesDSHigh.setStatus("current")
_NqaJitterStatsPacketLossSD_Type = Counter32
_NqaJitterStatsPacketLossSD_Object = MibTableColumn
nqaJitterStatsPacketLossSD = _NqaJitterStatsPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 34),
    _NqaJitterStatsPacketLossSD_Type()
)
nqaJitterStatsPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsPacketLossSD.setStatus("current")
_NqaJitterStatsPacketLossDS_Type = Counter32
_NqaJitterStatsPacketLossDS_Object = MibTableColumn
nqaJitterStatsPacketLossDS = _NqaJitterStatsPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 35),
    _NqaJitterStatsPacketLossDS_Type()
)
nqaJitterStatsPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsPacketLossDS.setStatus("current")
_NqaJitterStatsPacketOutOfSequences_Type = Counter32
_NqaJitterStatsPacketOutOfSequences_Object = MibTableColumn
nqaJitterStatsPacketOutOfSequences = _NqaJitterStatsPacketOutOfSequences_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 36),
    _NqaJitterStatsPacketOutOfSequences_Type()
)
nqaJitterStatsPacketOutOfSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsPacketOutOfSequences.setStatus("current")
_NqaJitterStatsErrors_Type = Counter32
_NqaJitterStatsErrors_Object = MibTableColumn
nqaJitterStatsErrors = _NqaJitterStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 37),
    _NqaJitterStatsErrors_Type()
)
nqaJitterStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsErrors.setStatus("current")
_NqaJitterStatsBusies_Type = Counter32
_NqaJitterStatsBusies_Object = MibTableColumn
nqaJitterStatsBusies = _NqaJitterStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 38),
    _NqaJitterStatsBusies_Type()
)
nqaJitterStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsBusies.setStatus("current")
_NqaJitterStatsTimeouts_Type = Counter32
_NqaJitterStatsTimeouts_Object = MibTableColumn
nqaJitterStatsTimeouts = _NqaJitterStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 39),
    _NqaJitterStatsTimeouts_Type()
)
nqaJitterStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsTimeouts.setStatus("current")
_NqaJitterStatsProbeResponses_Type = Counter32
_NqaJitterStatsProbeResponses_Object = MibTableColumn
nqaJitterStatsProbeResponses = _NqaJitterStatsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 40),
    _NqaJitterStatsProbeResponses_Type()
)
nqaJitterStatsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsProbeResponses.setStatus("current")
_NqaJitterStatsSentProbes_Type = Counter32
_NqaJitterStatsSentProbes_Object = MibTableColumn
nqaJitterStatsSentProbes = _NqaJitterStatsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 41),
    _NqaJitterStatsSentProbes_Type()
)
nqaJitterStatsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSentProbes.setStatus("current")
_NqaJitterStatsDrops_Type = Counter32
_NqaJitterStatsDrops_Object = MibTableColumn
nqaJitterStatsDrops = _NqaJitterStatsDrops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 42),
    _NqaJitterStatsDrops_Type()
)
nqaJitterStatsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsDrops.setStatus("current")


class _NqaJitterStatsTestFinished_Type(Integer32):
    """Custom type nqaJitterStatsTestFinished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finish", 1),
          ("noFinish", 0))
    )


_NqaJitterStatsTestFinished_Type.__name__ = "Integer32"
_NqaJitterStatsTestFinished_Object = MibTableColumn
nqaJitterStatsTestFinished = _NqaJitterStatsTestFinished_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 43),
    _NqaJitterStatsTestFinished_Type()
)
nqaJitterStatsTestFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsTestFinished.setStatus("current")
_NqaJitterStatsMaxDelaySD_Type = Gauge32
_NqaJitterStatsMaxDelaySD_Object = MibTableColumn
nqaJitterStatsMaxDelaySD = _NqaJitterStatsMaxDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 44),
    _NqaJitterStatsMaxDelaySD_Type()
)
nqaJitterStatsMaxDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMaxDelaySD.setStatus("current")
if mibBuilder.loadTexts:
    nqaJitterStatsMaxDelaySD.setUnits("milliseconds")
_NqaJitterStatsMaxDelayDS_Type = Gauge32
_NqaJitterStatsMaxDelayDS_Object = MibTableColumn
nqaJitterStatsMaxDelayDS = _NqaJitterStatsMaxDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 45),
    _NqaJitterStatsMaxDelayDS_Type()
)
nqaJitterStatsMaxDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMaxDelayDS.setStatus("current")
if mibBuilder.loadTexts:
    nqaJitterStatsMaxDelayDS.setUnits("milliseconds")
_NqaJitterStatsRTTAvg_Type = Gauge32
_NqaJitterStatsRTTAvg_Object = MibTableColumn
nqaJitterStatsRTTAvg = _NqaJitterStatsRTTAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 46),
    _NqaJitterStatsRTTAvg_Type()
)
nqaJitterStatsRTTAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsRTTAvg.setStatus("current")
_NqaJitterStatsPacketLossRatio_Type = Gauge32
_NqaJitterStatsPacketLossRatio_Object = MibTableColumn
nqaJitterStatsPacketLossRatio = _NqaJitterStatsPacketLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 47),
    _NqaJitterStatsPacketLossRatio_Type()
)
nqaJitterStatsPacketLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsPacketLossRatio.setStatus("current")
_NqaJitterStatsAvgJitter_Type = Gauge32
_NqaJitterStatsAvgJitter_Object = MibTableColumn
nqaJitterStatsAvgJitter = _NqaJitterStatsAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 48),
    _NqaJitterStatsAvgJitter_Type()
)
nqaJitterStatsAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsAvgJitter.setStatus("current")
_NqaJitterStatsAvgJitterSD_Type = Gauge32
_NqaJitterStatsAvgJitterSD_Object = MibTableColumn
nqaJitterStatsAvgJitterSD = _NqaJitterStatsAvgJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 49),
    _NqaJitterStatsAvgJitterSD_Type()
)
nqaJitterStatsAvgJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsAvgJitterSD.setStatus("current")
_NqaJitterStatsAvgJitterDS_Type = Gauge32
_NqaJitterStatsAvgJitterDS_Object = MibTableColumn
nqaJitterStatsAvgJitterDS = _NqaJitterStatsAvgJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 50),
    _NqaJitterStatsAvgJitterDS_Type()
)
nqaJitterStatsAvgJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsAvgJitterDS.setStatus("current")
_NqaJitterStatsJitterOut_Type = OctetString
_NqaJitterStatsJitterOut_Object = MibTableColumn
nqaJitterStatsJitterOut = _NqaJitterStatsJitterOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 51),
    _NqaJitterStatsJitterOut_Type()
)
nqaJitterStatsJitterOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsJitterOut.setStatus("current")
_NqaJitterStatsJitterIn_Type = OctetString
_NqaJitterStatsJitterIn_Object = MibTableColumn
nqaJitterStatsJitterIn = _NqaJitterStatsJitterIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 52),
    _NqaJitterStatsJitterIn_Type()
)
nqaJitterStatsJitterIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsJitterIn.setStatus("current")
_NqaJitterStatsOWDOverThresholdsSD_Type = Counter32
_NqaJitterStatsOWDOverThresholdsSD_Object = MibTableColumn
nqaJitterStatsOWDOverThresholdsSD = _NqaJitterStatsOWDOverThresholdsSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 53),
    _NqaJitterStatsOWDOverThresholdsSD_Type()
)
nqaJitterStatsOWDOverThresholdsSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsOWDOverThresholdsSD.setStatus("current")
_NqaJitterStatsPktLossUnknown_Type = Counter32
_NqaJitterStatsPktLossUnknown_Object = MibTableColumn
nqaJitterStatsPktLossUnknown = _NqaJitterStatsPktLossUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 54),
    _NqaJitterStatsPktLossUnknown_Type()
)
nqaJitterStatsPktLossUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsPktLossUnknown.setStatus("current")
_NqaJitterStatsNumOfOWD_Type = Counter32
_NqaJitterStatsNumOfOWD_Object = MibTableColumn
nqaJitterStatsNumOfOWD = _NqaJitterStatsNumOfOWD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 55),
    _NqaJitterStatsNumOfOWD_Type()
)
nqaJitterStatsNumOfOWD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsNumOfOWD.setStatus("current")
_NqaJitterStatsOWSumSD_Type = Counter32
_NqaJitterStatsOWSumSD_Object = MibTableColumn
nqaJitterStatsOWSumSD = _NqaJitterStatsOWSumSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 56),
    _NqaJitterStatsOWSumSD_Type()
)
nqaJitterStatsOWSumSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsOWSumSD.setStatus("current")
_NqaJitterStatsOWSumDS_Type = Counter32
_NqaJitterStatsOWSumDS_Object = MibTableColumn
nqaJitterStatsOWSumDS = _NqaJitterStatsOWSumDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 57),
    _NqaJitterStatsOWSumDS_Type()
)
nqaJitterStatsOWSumDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsOWSumDS.setStatus("current")
_NqaJitterStatsOWDOverThresholdsDS_Type = Counter32
_NqaJitterStatsOWDOverThresholdsDS_Object = MibTableColumn
nqaJitterStatsOWDOverThresholdsDS = _NqaJitterStatsOWDOverThresholdsDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 58),
    _NqaJitterStatsOWDOverThresholdsDS_Type()
)
nqaJitterStatsOWDOverThresholdsDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsOWDOverThresholdsDS.setStatus("current")
_NqaJitterStatsOperOfIcpif_Type = Gauge32
_NqaJitterStatsOperOfIcpif_Object = MibTableColumn
nqaJitterStatsOperOfIcpif = _NqaJitterStatsOperOfIcpif_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 59),
    _NqaJitterStatsOperOfIcpif_Type()
)
nqaJitterStatsOperOfIcpif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsOperOfIcpif.setStatus("current")
_NqaJitterStatsOperOfMos_Type = Gauge32
_NqaJitterStatsOperOfMos_Object = MibTableColumn
nqaJitterStatsOperOfMos = _NqaJitterStatsOperOfMos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 60),
    _NqaJitterStatsOperOfMos_Type()
)
nqaJitterStatsOperOfMos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsOperOfMos.setStatus("current")
_NqaJitterStatsMinDelaySD_Type = Gauge32
_NqaJitterStatsMinDelaySD_Object = MibTableColumn
nqaJitterStatsMinDelaySD = _NqaJitterStatsMinDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 61),
    _NqaJitterStatsMinDelaySD_Type()
)
nqaJitterStatsMinDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMinDelaySD.setStatus("current")
_NqaJitterStatsSum2DelaySDLow_Type = Gauge32
_NqaJitterStatsSum2DelaySDLow_Object = MibTableColumn
nqaJitterStatsSum2DelaySDLow = _NqaJitterStatsSum2DelaySDLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 62),
    _NqaJitterStatsSum2DelaySDLow_Type()
)
nqaJitterStatsSum2DelaySDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2DelaySDLow.setStatus("current")
_NqaJitterStatsSum2DelaySDHigh_Type = Counter32
_NqaJitterStatsSum2DelaySDHigh_Object = MibTableColumn
nqaJitterStatsSum2DelaySDHigh = _NqaJitterStatsSum2DelaySDHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 63),
    _NqaJitterStatsSum2DelaySDHigh_Type()
)
nqaJitterStatsSum2DelaySDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2DelaySDHigh.setStatus("current")
_NqaJitterStatsMinDelayDS_Type = Gauge32
_NqaJitterStatsMinDelayDS_Object = MibTableColumn
nqaJitterStatsMinDelayDS = _NqaJitterStatsMinDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 64),
    _NqaJitterStatsMinDelayDS_Type()
)
nqaJitterStatsMinDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsMinDelayDS.setStatus("current")
_NqaJitterStatsSum2DelayDSLow_Type = Gauge32
_NqaJitterStatsSum2DelayDSLow_Object = MibTableColumn
nqaJitterStatsSum2DelayDSLow = _NqaJitterStatsSum2DelayDSLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 65),
    _NqaJitterStatsSum2DelayDSLow_Type()
)
nqaJitterStatsSum2DelayDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2DelayDSLow.setStatus("current")
_NqaJitterStatsSum2DelayDSHigh_Type = Counter32
_NqaJitterStatsSum2DelayDSHigh_Object = MibTableColumn
nqaJitterStatsSum2DelayDSHigh = _NqaJitterStatsSum2DelayDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 66),
    _NqaJitterStatsSum2DelayDSHigh_Type()
)
nqaJitterStatsSum2DelayDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsSum2DelayDSHigh.setStatus("current")


class _NqaJitterStatsTimeUnit_Type(Integer32):
    """Custom type nqaJitterStatsTimeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ms", 2),
          ("us", 1))
    )


_NqaJitterStatsTimeUnit_Type.__name__ = "Integer32"
_NqaJitterStatsTimeUnit_Object = MibTableColumn
nqaJitterStatsTimeUnit = _NqaJitterStatsTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 67),
    _NqaJitterStatsTimeUnit_Type()
)
nqaJitterStatsTimeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsTimeUnit.setStatus("current")
_NqaJitterStatsAvgDelaySD_Type = Gauge32
_NqaJitterStatsAvgDelaySD_Object = MibTableColumn
nqaJitterStatsAvgDelaySD = _NqaJitterStatsAvgDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 68),
    _NqaJitterStatsAvgDelaySD_Type()
)
nqaJitterStatsAvgDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsAvgDelaySD.setStatus("current")
_NqaJitterStatsAvgDelayDS_Type = Gauge32
_NqaJitterStatsAvgDelayDS_Object = MibTableColumn
nqaJitterStatsAvgDelayDS = _NqaJitterStatsAvgDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 69),
    _NqaJitterStatsAvgDelayDS_Type()
)
nqaJitterStatsAvgDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsAvgDelayDS.setStatus("current")
_NqaJitterStatsPktRewriteNum_Type = Counter32
_NqaJitterStatsPktRewriteNum_Object = MibTableColumn
nqaJitterStatsPktRewriteNum = _NqaJitterStatsPktRewriteNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 70),
    _NqaJitterStatsPktRewriteNum_Type()
)
nqaJitterStatsPktRewriteNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsPktRewriteNum.setStatus("current")
_NqaJitterStatsPktRewriteRatio_Type = Gauge32
_NqaJitterStatsPktRewriteRatio_Object = MibTableColumn
nqaJitterStatsPktRewriteRatio = _NqaJitterStatsPktRewriteRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 71),
    _NqaJitterStatsPktRewriteRatio_Type()
)
nqaJitterStatsPktRewriteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsPktRewriteRatio.setStatus("current")
_NqaJitterStatsPktDisorderNum_Type = Counter32
_NqaJitterStatsPktDisorderNum_Object = MibTableColumn
nqaJitterStatsPktDisorderNum = _NqaJitterStatsPktDisorderNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 72),
    _NqaJitterStatsPktDisorderNum_Type()
)
nqaJitterStatsPktDisorderNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsPktDisorderNum.setStatus("current")
_NqaJitterStatsPktDisorderRatio_Type = Gauge32
_NqaJitterStatsPktDisorderRatio_Object = MibTableColumn
nqaJitterStatsPktDisorderRatio = _NqaJitterStatsPktDisorderRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 73),
    _NqaJitterStatsPktDisorderRatio_Type()
)
nqaJitterStatsPktDisorderRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsPktDisorderRatio.setStatus("current")
_NqaJitterStatsFragPktDisorderNum_Type = Counter32
_NqaJitterStatsFragPktDisorderNum_Object = MibTableColumn
nqaJitterStatsFragPktDisorderNum = _NqaJitterStatsFragPktDisorderNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 74),
    _NqaJitterStatsFragPktDisorderNum_Type()
)
nqaJitterStatsFragPktDisorderNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsFragPktDisorderNum.setStatus("current")
_NqaJitterStatsFragPktDisorderRatio_Type = Gauge32
_NqaJitterStatsFragPktDisorderRatio_Object = MibTableColumn
nqaJitterStatsFragPktDisorderRatio = _NqaJitterStatsFragPktDisorderRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 3, 1, 75),
    _NqaJitterStatsFragPktDisorderRatio_Type()
)
nqaJitterStatsFragPktDisorderRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterStatsFragPktDisorderRatio.setStatus("current")
_NqaFTPStatsTable_Object = MibTable
nqaFTPStatsTable = _NqaFTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4)
)
if mibBuilder.loadTexts:
    nqaFTPStatsTable.setStatus("current")
_NqaFTPStatsEntry_Object = MibTableRow
nqaFTPStatsEntry = _NqaFTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1)
)
nqaFTPStatsEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaFTPStatsIndex"),
)
if mibBuilder.loadTexts:
    nqaFTPStatsEntry.setStatus("current")


class _NqaFTPStatsIndex_Type(Integer32):
    """Custom type nqaFTPStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaFTPStatsIndex_Type.__name__ = "Integer32"
_NqaFTPStatsIndex_Object = MibTableColumn
nqaFTPStatsIndex = _NqaFTPStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 1),
    _NqaFTPStatsIndex_Type()
)
nqaFTPStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaFTPStatsIndex.setStatus("current")


class _NqaFTPStatsCompletions_Type(Integer32):
    """Custom type nqaFTPStatsCompletions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("noResult", 0),
          ("success", 1))
    )


_NqaFTPStatsCompletions_Type.__name__ = "Integer32"
_NqaFTPStatsCompletions_Object = MibTableColumn
nqaFTPStatsCompletions = _NqaFTPStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 2),
    _NqaFTPStatsCompletions_Type()
)
nqaFTPStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsCompletions.setStatus("current")
_NqaFTPStatsRTDOverThresholds_Type = Counter32
_NqaFTPStatsRTDOverThresholds_Object = MibTableColumn
nqaFTPStatsRTDOverThresholds = _NqaFTPStatsRTDOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 3),
    _NqaFTPStatsRTDOverThresholds_Type()
)
nqaFTPStatsRTDOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsRTDOverThresholds.setStatus("current")
_NqaFTPStatsCtrlConnMaxTime_Type = Gauge32
_NqaFTPStatsCtrlConnMaxTime_Object = MibTableColumn
nqaFTPStatsCtrlConnMaxTime = _NqaFTPStatsCtrlConnMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 4),
    _NqaFTPStatsCtrlConnMaxTime_Type()
)
nqaFTPStatsCtrlConnMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsCtrlConnMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaFTPStatsCtrlConnMaxTime.setUnits("milliseconds")
_NqaFTPStatsCtrlConnMinTime_Type = Gauge32
_NqaFTPStatsCtrlConnMinTime_Object = MibTableColumn
nqaFTPStatsCtrlConnMinTime = _NqaFTPStatsCtrlConnMinTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 5),
    _NqaFTPStatsCtrlConnMinTime_Type()
)
nqaFTPStatsCtrlConnMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsCtrlConnMinTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaFTPStatsCtrlConnMinTime.setUnits("milliseconds")
_NqaFTPStatsCtrlConnAveTime_Type = Gauge32
_NqaFTPStatsCtrlConnAveTime_Object = MibTableColumn
nqaFTPStatsCtrlConnAveTime = _NqaFTPStatsCtrlConnAveTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 6),
    _NqaFTPStatsCtrlConnAveTime_Type()
)
nqaFTPStatsCtrlConnAveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsCtrlConnAveTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaFTPStatsCtrlConnAveTime.setUnits("milliseconds")
_NqaFTPStatsDataConnMaxTime_Type = Gauge32
_NqaFTPStatsDataConnMaxTime_Object = MibTableColumn
nqaFTPStatsDataConnMaxTime = _NqaFTPStatsDataConnMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 7),
    _NqaFTPStatsDataConnMaxTime_Type()
)
nqaFTPStatsDataConnMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsDataConnMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaFTPStatsDataConnMaxTime.setUnits("milliseconds")
_NqaFTPStatsDataConnMinTime_Type = Gauge32
_NqaFTPStatsDataConnMinTime_Object = MibTableColumn
nqaFTPStatsDataConnMinTime = _NqaFTPStatsDataConnMinTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 8),
    _NqaFTPStatsDataConnMinTime_Type()
)
nqaFTPStatsDataConnMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsDataConnMinTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaFTPStatsDataConnMinTime.setUnits("milliseconds")
_NqaFTPStatsDataConnAveTime_Type = Gauge32
_NqaFTPStatsDataConnAveTime_Object = MibTableColumn
nqaFTPStatsDataConnAveTime = _NqaFTPStatsDataConnAveTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 9),
    _NqaFTPStatsDataConnAveTime_Type()
)
nqaFTPStatsDataConnAveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsDataConnAveTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaFTPStatsDataConnAveTime.setUnits("milliseconds")
_NqaFTPStatsConnectSumTimeMax_Type = Gauge32
_NqaFTPStatsConnectSumTimeMax_Object = MibTableColumn
nqaFTPStatsConnectSumTimeMax = _NqaFTPStatsConnectSumTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 10),
    _NqaFTPStatsConnectSumTimeMax_Type()
)
nqaFTPStatsConnectSumTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsConnectSumTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    nqaFTPStatsConnectSumTimeMax.setUnits("milliseconds")
_NqaFTPStatsConnectSumTimeMin_Type = Gauge32
_NqaFTPStatsConnectSumTimeMin_Object = MibTableColumn
nqaFTPStatsConnectSumTimeMin = _NqaFTPStatsConnectSumTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 11),
    _NqaFTPStatsConnectSumTimeMin_Type()
)
nqaFTPStatsConnectSumTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsConnectSumTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    nqaFTPStatsConnectSumTimeMin.setUnits("milliseconds")
_NqaFTPStatsConnectSumTimeAve_Type = Gauge32
_NqaFTPStatsConnectSumTimeAve_Object = MibTableColumn
nqaFTPStatsConnectSumTimeAve = _NqaFTPStatsConnectSumTimeAve_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 12),
    _NqaFTPStatsConnectSumTimeAve_Type()
)
nqaFTPStatsConnectSumTimeAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsConnectSumTimeAve.setStatus("current")
if mibBuilder.loadTexts:
    nqaFTPStatsConnectSumTimeAve.setUnits("milliseconds")
_NqaFTPStatsMessageBodyOctetsSum_Type = Counter32
_NqaFTPStatsMessageBodyOctetsSum_Object = MibTableColumn
nqaFTPStatsMessageBodyOctetsSum = _NqaFTPStatsMessageBodyOctetsSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 13),
    _NqaFTPStatsMessageBodyOctetsSum_Type()
)
nqaFTPStatsMessageBodyOctetsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsMessageBodyOctetsSum.setStatus("current")
_NqaFTPStatsErrors_Type = Counter32
_NqaFTPStatsErrors_Object = MibTableColumn
nqaFTPStatsErrors = _NqaFTPStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 14),
    _NqaFTPStatsErrors_Type()
)
nqaFTPStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsErrors.setStatus("current")
_NqaFTPStatsTimeouts_Type = Counter32
_NqaFTPStatsTimeouts_Object = MibTableColumn
nqaFTPStatsTimeouts = _NqaFTPStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 15),
    _NqaFTPStatsTimeouts_Type()
)
nqaFTPStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsTimeouts.setStatus("current")
_NqaFTPStatsDiscontinued_Type = Counter32
_NqaFTPStatsDiscontinued_Object = MibTableColumn
nqaFTPStatsDiscontinued = _NqaFTPStatsDiscontinued_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 16),
    _NqaFTPStatsDiscontinued_Type()
)
nqaFTPStatsDiscontinued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsDiscontinued.setStatus("current")
_NqaFTPStatsProbeResponses_Type = Counter32
_NqaFTPStatsProbeResponses_Object = MibTableColumn
nqaFTPStatsProbeResponses = _NqaFTPStatsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 17),
    _NqaFTPStatsProbeResponses_Type()
)
nqaFTPStatsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsProbeResponses.setStatus("current")
_NqaFTPStatsSendProbes_Type = Counter32
_NqaFTPStatsSendProbes_Object = MibTableColumn
nqaFTPStatsSendProbes = _NqaFTPStatsSendProbes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 18),
    _NqaFTPStatsSendProbes_Type()
)
nqaFTPStatsSendProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsSendProbes.setStatus("current")


class _NqaFTPStatsTestFinished_Type(Integer32):
    """Custom type nqaFTPStatsTestFinished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finish", 1),
          ("noFinish", 0))
    )


_NqaFTPStatsTestFinished_Type.__name__ = "Integer32"
_NqaFTPStatsTestFinished_Object = MibTableColumn
nqaFTPStatsTestFinished = _NqaFTPStatsTestFinished_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 19),
    _NqaFTPStatsTestFinished_Type()
)
nqaFTPStatsTestFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsTestFinished.setStatus("current")
_NqaFTPStatsRttAvg_Type = Gauge32
_NqaFTPStatsRttAvg_Object = MibTableColumn
nqaFTPStatsRttAvg = _NqaFTPStatsRttAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 20),
    _NqaFTPStatsRttAvg_Type()
)
nqaFTPStatsRttAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsRttAvg.setStatus("current")
_NqaFTPStatsLostPacketRatio_Type = Gauge32
_NqaFTPStatsLostPacketRatio_Object = MibTableColumn
nqaFTPStatsLostPacketRatio = _NqaFTPStatsLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 4, 1, 21),
    _NqaFTPStatsLostPacketRatio_Type()
)
nqaFTPStatsLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFTPStatsLostPacketRatio.setStatus("current")
_NqaMpingStatsTable_Object = MibTable
nqaMpingStatsTable = _NqaMpingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5)
)
if mibBuilder.loadTexts:
    nqaMpingStatsTable.setStatus("current")
_NqaMpingStatsEntry_Object = MibTableRow
nqaMpingStatsEntry = _NqaMpingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1)
)
nqaMpingStatsEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaMpingStatsIndex"),
    (0, "NQA-MIB", "nqaMpingStatsReceiverIndex"),
)
if mibBuilder.loadTexts:
    nqaMpingStatsEntry.setStatus("current")


class _NqaMpingStatsIndex_Type(Integer32):
    """Custom type nqaMpingStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMpingStatsIndex_Type.__name__ = "Integer32"
_NqaMpingStatsIndex_Object = MibTableColumn
nqaMpingStatsIndex = _NqaMpingStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 1),
    _NqaMpingStatsIndex_Type()
)
nqaMpingStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMpingStatsIndex.setStatus("current")


class _NqaMpingStatsReceiverIndex_Type(Integer32):
    """Custom type nqaMpingStatsReceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMpingStatsReceiverIndex_Type.__name__ = "Integer32"
_NqaMpingStatsReceiverIndex_Object = MibTableColumn
nqaMpingStatsReceiverIndex = _NqaMpingStatsReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 2),
    _NqaMpingStatsReceiverIndex_Type()
)
nqaMpingStatsReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMpingStatsReceiverIndex.setStatus("current")
_NqaMpingStatsTargetAddressType_Type = InetAddressType
_NqaMpingStatsTargetAddressType_Object = MibTableColumn
nqaMpingStatsTargetAddressType = _NqaMpingStatsTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 3),
    _NqaMpingStatsTargetAddressType_Type()
)
nqaMpingStatsTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsTargetAddressType.setStatus("current")
_NqaMpingStatsTargetAddress_Type = InetAddress
_NqaMpingStatsTargetAddress_Object = MibTableColumn
nqaMpingStatsTargetAddress = _NqaMpingStatsTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 4),
    _NqaMpingStatsTargetAddress_Type()
)
nqaMpingStatsTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsTargetAddress.setStatus("current")
_NqaMpingStatsReceiverAddress_Type = InetAddress
_NqaMpingStatsReceiverAddress_Object = MibTableColumn
nqaMpingStatsReceiverAddress = _NqaMpingStatsReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 5),
    _NqaMpingStatsReceiverAddress_Type()
)
nqaMpingStatsReceiverAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsReceiverAddress.setStatus("current")


class _NqaMpingStatsCompletions_Type(Integer32):
    """Custom type nqaMpingStatsCompletions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("noResult", 1),
          ("success", 2))
    )


_NqaMpingStatsCompletions_Type.__name__ = "Integer32"
_NqaMpingStatsCompletions_Object = MibTableColumn
nqaMpingStatsCompletions = _NqaMpingStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 6),
    _NqaMpingStatsCompletions_Type()
)
nqaMpingStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsCompletions.setStatus("current")
_NqaMpingStatsRTDOverThresholds_Type = Counter32
_NqaMpingStatsRTDOverThresholds_Object = MibTableColumn
nqaMpingStatsRTDOverThresholds = _NqaMpingStatsRTDOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 7),
    _NqaMpingStatsRTDOverThresholds_Type()
)
nqaMpingStatsRTDOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsRTDOverThresholds.setStatus("current")
_NqaMpingStatsSumCompletionTime_Type = Counter32
_NqaMpingStatsSumCompletionTime_Object = MibTableColumn
nqaMpingStatsSumCompletionTime = _NqaMpingStatsSumCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 8),
    _NqaMpingStatsSumCompletionTime_Type()
)
nqaMpingStatsSumCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsSumCompletionTime.setStatus("current")
_NqaMpingStatsSumCompletionTime2Low_Type = Counter32
_NqaMpingStatsSumCompletionTime2Low_Object = MibTableColumn
nqaMpingStatsSumCompletionTime2Low = _NqaMpingStatsSumCompletionTime2Low_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 9),
    _NqaMpingStatsSumCompletionTime2Low_Type()
)
nqaMpingStatsSumCompletionTime2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsSumCompletionTime2Low.setStatus("current")
_NqaMpingStatsSumCompletionTime2High_Type = Counter32
_NqaMpingStatsSumCompletionTime2High_Object = MibTableColumn
nqaMpingStatsSumCompletionTime2High = _NqaMpingStatsSumCompletionTime2High_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 10),
    _NqaMpingStatsSumCompletionTime2High_Type()
)
nqaMpingStatsSumCompletionTime2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsSumCompletionTime2High.setStatus("current")
_NqaMpingStatsCompletionTimeMin_Type = Gauge32
_NqaMpingStatsCompletionTimeMin_Object = MibTableColumn
nqaMpingStatsCompletionTimeMin = _NqaMpingStatsCompletionTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 11),
    _NqaMpingStatsCompletionTimeMin_Type()
)
nqaMpingStatsCompletionTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsCompletionTimeMin.setStatus("current")
_NqaMpingStatsCompletionTimeMax_Type = Gauge32
_NqaMpingStatsCompletionTimeMax_Object = MibTableColumn
nqaMpingStatsCompletionTimeMax = _NqaMpingStatsCompletionTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 12),
    _NqaMpingStatsCompletionTimeMax_Type()
)
nqaMpingStatsCompletionTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsCompletionTimeMax.setStatus("current")
_NqaMpingStatsTimeouts_Type = Counter32
_NqaMpingStatsTimeouts_Object = MibTableColumn
nqaMpingStatsTimeouts = _NqaMpingStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 13),
    _NqaMpingStatsTimeouts_Type()
)
nqaMpingStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsTimeouts.setStatus("current")
_NqaMpingStatsBusies_Type = Counter32
_NqaMpingStatsBusies_Object = MibTableColumn
nqaMpingStatsBusies = _NqaMpingStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 14),
    _NqaMpingStatsBusies_Type()
)
nqaMpingStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsBusies.setStatus("current")
_NqaMpingStatsSequenceErrors_Type = Counter32
_NqaMpingStatsSequenceErrors_Object = MibTableColumn
nqaMpingStatsSequenceErrors = _NqaMpingStatsSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 15),
    _NqaMpingStatsSequenceErrors_Type()
)
nqaMpingStatsSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsSequenceErrors.setStatus("current")
_NqaMpingStatsDrops_Type = Counter32
_NqaMpingStatsDrops_Object = MibTableColumn
nqaMpingStatsDrops = _NqaMpingStatsDrops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 16),
    _NqaMpingStatsDrops_Type()
)
nqaMpingStatsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsDrops.setStatus("current")
_NqaMpingStatsProbeResponses_Type = Counter32
_NqaMpingStatsProbeResponses_Object = MibTableColumn
nqaMpingStatsProbeResponses = _NqaMpingStatsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 17),
    _NqaMpingStatsProbeResponses_Type()
)
nqaMpingStatsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsProbeResponses.setStatus("current")
_NqaMpingStatsSentProbes_Type = Counter32
_NqaMpingStatsSentProbes_Object = MibTableColumn
nqaMpingStatsSentProbes = _NqaMpingStatsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 18),
    _NqaMpingStatsSentProbes_Type()
)
nqaMpingStatsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsSentProbes.setStatus("current")
_NqaMpingStatsLastGoodProbe_Type = DateAndTime
_NqaMpingStatsLastGoodProbe_Object = MibTableColumn
nqaMpingStatsLastGoodProbe = _NqaMpingStatsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 19),
    _NqaMpingStatsLastGoodProbe_Type()
)
nqaMpingStatsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsLastGoodProbe.setStatus("current")


class _NqaMpingStatsTestFinished_Type(Integer32):
    """Custom type nqaMpingStatsTestFinished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("finish", 2),
          ("noFinish", 1))
    )


_NqaMpingStatsTestFinished_Type.__name__ = "Integer32"
_NqaMpingStatsTestFinished_Object = MibTableColumn
nqaMpingStatsTestFinished = _NqaMpingStatsTestFinished_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 20),
    _NqaMpingStatsTestFinished_Type()
)
nqaMpingStatsTestFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsTestFinished.setStatus("current")
_NqaMpingStatsReceiverCount_Type = Gauge32
_NqaMpingStatsReceiverCount_Object = MibTableColumn
nqaMpingStatsReceiverCount = _NqaMpingStatsReceiverCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 21),
    _NqaMpingStatsReceiverCount_Type()
)
nqaMpingStatsReceiverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsReceiverCount.setStatus("current")
_NqaMpingStatsLastFibHit_Type = TruthValue
_NqaMpingStatsLastFibHit_Object = MibTableColumn
nqaMpingStatsLastFibHit = _NqaMpingStatsLastFibHit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 22),
    _NqaMpingStatsLastFibHit_Type()
)
nqaMpingStatsLastFibHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsLastFibHit.setStatus("current")
_NqaMpingStatsRttAvg_Type = Gauge32
_NqaMpingStatsRttAvg_Object = MibTableColumn
nqaMpingStatsRttAvg = _NqaMpingStatsRttAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 23),
    _NqaMpingStatsRttAvg_Type()
)
nqaMpingStatsRttAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsRttAvg.setStatus("current")
_NqaMpingStatsLostPacketRatio_Type = Gauge32
_NqaMpingStatsLostPacketRatio_Object = MibTableColumn
nqaMpingStatsLostPacketRatio = _NqaMpingStatsLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 5, 1, 24),
    _NqaMpingStatsLostPacketRatio_Type()
)
nqaMpingStatsLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingStatsLostPacketRatio.setStatus("current")
_NqaMtracertStatsTable_Object = MibTable
nqaMtracertStatsTable = _NqaMtracertStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6)
)
if mibBuilder.loadTexts:
    nqaMtracertStatsTable.setStatus("current")
_NqaMtracertStatsEntry_Object = MibTableRow
nqaMtracertStatsEntry = _NqaMtracertStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1)
)
nqaMtracertStatsEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaMtracertStatsIndex"),
    (0, "NQA-MIB", "nqaMtracertStatsHopIndex"),
)
if mibBuilder.loadTexts:
    nqaMtracertStatsEntry.setStatus("current")


class _NqaMtracertStatsIndex_Type(Integer32):
    """Custom type nqaMtracertStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMtracertStatsIndex_Type.__name__ = "Integer32"
_NqaMtracertStatsIndex_Object = MibTableColumn
nqaMtracertStatsIndex = _NqaMtracertStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 1),
    _NqaMtracertStatsIndex_Type()
)
nqaMtracertStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMtracertStatsIndex.setStatus("current")


class _NqaMtracertStatsHopIndex_Type(Integer32):
    """Custom type nqaMtracertStatsHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaMtracertStatsHopIndex_Type.__name__ = "Integer32"
_NqaMtracertStatsHopIndex_Object = MibTableColumn
nqaMtracertStatsHopIndex = _NqaMtracertStatsHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 2),
    _NqaMtracertStatsHopIndex_Type()
)
nqaMtracertStatsHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMtracertStatsHopIndex.setStatus("current")
_NqaMtracertStatsAddressType_Type = InetAddressType
_NqaMtracertStatsAddressType_Object = MibTableColumn
nqaMtracertStatsAddressType = _NqaMtracertStatsAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 3),
    _NqaMtracertStatsAddressType_Type()
)
nqaMtracertStatsAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsAddressType.setStatus("current")
_NqaMtracertStatsAddress_Type = InetAddress
_NqaMtracertStatsAddress_Object = MibTableColumn
nqaMtracertStatsAddress = _NqaMtracertStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 4),
    _NqaMtracertStatsAddress_Type()
)
nqaMtracertStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsAddress.setStatus("current")


class _NqaMtracertStatsCompletions_Type(Integer32):
    """Custom type nqaMtracertStatsCompletions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("noResult", 1),
          ("success", 2))
    )


_NqaMtracertStatsCompletions_Type.__name__ = "Integer32"
_NqaMtracertStatsCompletions_Object = MibTableColumn
nqaMtracertStatsCompletions = _NqaMtracertStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 5),
    _NqaMtracertStatsCompletions_Type()
)
nqaMtracertStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsCompletions.setStatus("current")
_NqaMtracertStatsCurHopCount_Type = Gauge32
_NqaMtracertStatsCurHopCount_Object = MibTableColumn
nqaMtracertStatsCurHopCount = _NqaMtracertStatsCurHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 6),
    _NqaMtracertStatsCurHopCount_Type()
)
nqaMtracertStatsCurHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsCurHopCount.setStatus("current")
_NqaMtracertStatsCurProbeCount_Type = Gauge32
_NqaMtracertStatsCurProbeCount_Object = MibTableColumn
nqaMtracertStatsCurProbeCount = _NqaMtracertStatsCurProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 7),
    _NqaMtracertStatsCurProbeCount_Type()
)
nqaMtracertStatsCurProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsCurProbeCount.setStatus("current")
_NqaMtracertStatsRTDOverThresholds_Type = Counter32
_NqaMtracertStatsRTDOverThresholds_Object = MibTableColumn
nqaMtracertStatsRTDOverThresholds = _NqaMtracertStatsRTDOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 8),
    _NqaMtracertStatsRTDOverThresholds_Type()
)
nqaMtracertStatsRTDOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsRTDOverThresholds.setStatus("current")
_NqaMtracertStatsTimeouts_Type = Counter32
_NqaMtracertStatsTimeouts_Object = MibTableColumn
nqaMtracertStatsTimeouts = _NqaMtracertStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 9),
    _NqaMtracertStatsTimeouts_Type()
)
nqaMtracertStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsTimeouts.setStatus("current")
_NqaMtracertStatsBusies_Type = Counter32
_NqaMtracertStatsBusies_Object = MibTableColumn
nqaMtracertStatsBusies = _NqaMtracertStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 10),
    _NqaMtracertStatsBusies_Type()
)
nqaMtracertStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsBusies.setStatus("current")
_NqaMtracertStatsSequenceErrors_Type = Counter32
_NqaMtracertStatsSequenceErrors_Object = MibTableColumn
nqaMtracertStatsSequenceErrors = _NqaMtracertStatsSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 11),
    _NqaMtracertStatsSequenceErrors_Type()
)
nqaMtracertStatsSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsSequenceErrors.setStatus("current")
_NqaMtracertStatsDrops_Type = Counter32
_NqaMtracertStatsDrops_Object = MibTableColumn
nqaMtracertStatsDrops = _NqaMtracertStatsDrops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 12),
    _NqaMtracertStatsDrops_Type()
)
nqaMtracertStatsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsDrops.setStatus("current")
_NqaMtracertStatsProbeResponses_Type = Counter32
_NqaMtracertStatsProbeResponses_Object = MibTableColumn
nqaMtracertStatsProbeResponses = _NqaMtracertStatsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 13),
    _NqaMtracertStatsProbeResponses_Type()
)
nqaMtracertStatsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsProbeResponses.setStatus("current")
_NqaMtracertStatsSentProbes_Type = Counter32
_NqaMtracertStatsSentProbes_Object = MibTableColumn
nqaMtracertStatsSentProbes = _NqaMtracertStatsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 14),
    _NqaMtracertStatsSentProbes_Type()
)
nqaMtracertStatsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsSentProbes.setStatus("current")
_NqaMtracertStatsLastGoodProbe_Type = DateAndTime
_NqaMtracertStatsLastGoodProbe_Object = MibTableColumn
nqaMtracertStatsLastGoodProbe = _NqaMtracertStatsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 15),
    _NqaMtracertStatsLastGoodProbe_Type()
)
nqaMtracertStatsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsLastGoodProbe.setStatus("current")
_NqaMtracertStatsLastGoodPath_Type = DateAndTime
_NqaMtracertStatsLastGoodPath_Object = MibTableColumn
nqaMtracertStatsLastGoodPath = _NqaMtracertStatsLastGoodPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 16),
    _NqaMtracertStatsLastGoodPath_Type()
)
nqaMtracertStatsLastGoodPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsLastGoodPath.setStatus("current")


class _NqaMtracertStatsTestFinished_Type(Integer32):
    """Custom type nqaMtracertStatsTestFinished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("finish", 2),
          ("noFinish", 1))
    )


_NqaMtracertStatsTestFinished_Type.__name__ = "Integer32"
_NqaMtracertStatsTestFinished_Object = MibTableColumn
nqaMtracertStatsTestFinished = _NqaMtracertStatsTestFinished_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 17),
    _NqaMtracertStatsTestFinished_Type()
)
nqaMtracertStatsTestFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsTestFinished.setStatus("current")
_NqaMtracertStatsCurPathTTL_Type = Gauge32
_NqaMtracertStatsCurPathTTL_Object = MibTableColumn
nqaMtracertStatsCurPathTTL = _NqaMtracertStatsCurPathTTL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 18),
    _NqaMtracertStatsCurPathTTL_Type()
)
nqaMtracertStatsCurPathTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsCurPathTTL.setStatus("current")
_NqaMtracertStatsMaxPathTTL_Type = Gauge32
_NqaMtracertStatsMaxPathTTL_Object = MibTableColumn
nqaMtracertStatsMaxPathTTL = _NqaMtracertStatsMaxPathTTL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 19),
    _NqaMtracertStatsMaxPathTTL_Type()
)
nqaMtracertStatsMaxPathTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsMaxPathTTL.setStatus("current")
_NqaMtracertStatsInPkgLossRate_Type = Gauge32
_NqaMtracertStatsInPkgLossRate_Object = MibTableColumn
nqaMtracertStatsInPkgLossRate = _NqaMtracertStatsInPkgLossRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 20),
    _NqaMtracertStatsInPkgLossRate_Type()
)
nqaMtracertStatsInPkgLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsInPkgLossRate.setStatus("current")
_NqaMtracertStatsSGPkgLossRate_Type = Gauge32
_NqaMtracertStatsSGPkgLossRate_Object = MibTableColumn
nqaMtracertStatsSGPkgLossRate = _NqaMtracertStatsSGPkgLossRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 21),
    _NqaMtracertStatsSGPkgLossRate_Type()
)
nqaMtracertStatsSGPkgLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsSGPkgLossRate.setStatus("current")
_NqaMtracertStatsInPkgRate_Type = Gauge32
_NqaMtracertStatsInPkgRate_Object = MibTableColumn
nqaMtracertStatsInPkgRate = _NqaMtracertStatsInPkgRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 22),
    _NqaMtracertStatsInPkgRate_Type()
)
nqaMtracertStatsInPkgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsInPkgRate.setStatus("current")
_NqaMtracertStatsOutPkgRate_Type = Gauge32
_NqaMtracertStatsOutPkgRate_Object = MibTableColumn
nqaMtracertStatsOutPkgRate = _NqaMtracertStatsOutPkgRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 23),
    _NqaMtracertStatsOutPkgRate_Type()
)
nqaMtracertStatsOutPkgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsOutPkgRate.setStatus("current")
_NqaMtracertStatsTimeDelay_Type = Gauge32
_NqaMtracertStatsTimeDelay_Object = MibTableColumn
nqaMtracertStatsTimeDelay = _NqaMtracertStatsTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 6, 1, 24),
    _NqaMtracertStatsTimeDelay_Type()
)
nqaMtracertStatsTimeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertStatsTimeDelay.setStatus("current")
_NqaPathMtuStatsTable_Object = MibTable
nqaPathMtuStatsTable = _NqaPathMtuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7)
)
if mibBuilder.loadTexts:
    nqaPathMtuStatsTable.setStatus("current")
_NqaPathMtuStatsEntry_Object = MibTableRow
nqaPathMtuStatsEntry = _NqaPathMtuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1)
)
nqaPathMtuStatsEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaPathMtuStatsIndex"),
)
if mibBuilder.loadTexts:
    nqaPathMtuStatsEntry.setStatus("current")


class _NqaPathMtuStatsIndex_Type(Integer32):
    """Custom type nqaPathMtuStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaPathMtuStatsIndex_Type.__name__ = "Integer32"
_NqaPathMtuStatsIndex_Object = MibTableColumn
nqaPathMtuStatsIndex = _NqaPathMtuStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 1),
    _NqaPathMtuStatsIndex_Type()
)
nqaPathMtuStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaPathMtuStatsIndex.setStatus("current")
_NqaPathMtuStatsAddressType_Type = InetAddressType
_NqaPathMtuStatsAddressType_Object = MibTableColumn
nqaPathMtuStatsAddressType = _NqaPathMtuStatsAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 2),
    _NqaPathMtuStatsAddressType_Type()
)
nqaPathMtuStatsAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsAddressType.setStatus("current")
_NqaPathMtuStatsAddress_Type = InetAddress
_NqaPathMtuStatsAddress_Object = MibTableColumn
nqaPathMtuStatsAddress = _NqaPathMtuStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 3),
    _NqaPathMtuStatsAddress_Type()
)
nqaPathMtuStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsAddress.setStatus("current")


class _NqaPathMtuStatsCompletions_Type(Integer32):
    """Custom type nqaPathMtuStatsCompletions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("noResult", 0),
          ("success", 1))
    )


_NqaPathMtuStatsCompletions_Type.__name__ = "Integer32"
_NqaPathMtuStatsCompletions_Object = MibTableColumn
nqaPathMtuStatsCompletions = _NqaPathMtuStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 4),
    _NqaPathMtuStatsCompletions_Type()
)
nqaPathMtuStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsCompletions.setStatus("current")
_NqaPathMtuStatsSentProbes_Type = Counter32
_NqaPathMtuStatsSentProbes_Object = MibTableColumn
nqaPathMtuStatsSentProbes = _NqaPathMtuStatsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 5),
    _NqaPathMtuStatsSentProbes_Type()
)
nqaPathMtuStatsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsSentProbes.setStatus("current")
_NqaPathMtuStatsProbeResponses_Type = Counter32
_NqaPathMtuStatsProbeResponses_Object = MibTableColumn
nqaPathMtuStatsProbeResponses = _NqaPathMtuStatsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 6),
    _NqaPathMtuStatsProbeResponses_Type()
)
nqaPathMtuStatsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsProbeResponses.setStatus("current")
_NqaPathMtuStatsDiscoveryPathMtuMin_Type = Gauge32
_NqaPathMtuStatsDiscoveryPathMtuMin_Object = MibTableColumn
nqaPathMtuStatsDiscoveryPathMtuMin = _NqaPathMtuStatsDiscoveryPathMtuMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 7),
    _NqaPathMtuStatsDiscoveryPathMtuMin_Type()
)
nqaPathMtuStatsDiscoveryPathMtuMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsDiscoveryPathMtuMin.setStatus("current")
_NqaPathMtuStatsDiscoveryPathMtuMax_Type = Gauge32
_NqaPathMtuStatsDiscoveryPathMtuMax_Object = MibTableColumn
nqaPathMtuStatsDiscoveryPathMtuMax = _NqaPathMtuStatsDiscoveryPathMtuMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 8),
    _NqaPathMtuStatsDiscoveryPathMtuMax_Type()
)
nqaPathMtuStatsDiscoveryPathMtuMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsDiscoveryPathMtuMax.setStatus("current")
_NqaPathMtuStatsOptimumFirstStep_Type = Gauge32
_NqaPathMtuStatsOptimumFirstStep_Object = MibTableColumn
nqaPathMtuStatsOptimumFirstStep = _NqaPathMtuStatsOptimumFirstStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 9),
    _NqaPathMtuStatsOptimumFirstStep_Type()
)
nqaPathMtuStatsOptimumFirstStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsOptimumFirstStep.setStatus("current")
_NqaPathMtuStatsBusies_Type = Counter32
_NqaPathMtuStatsBusies_Object = MibTableColumn
nqaPathMtuStatsBusies = _NqaPathMtuStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 10),
    _NqaPathMtuStatsBusies_Type()
)
nqaPathMtuStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsBusies.setStatus("current")
_NqaPathMtuStatsTimeouts_Type = Counter32
_NqaPathMtuStatsTimeouts_Object = MibTableColumn
nqaPathMtuStatsTimeouts = _NqaPathMtuStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 11),
    _NqaPathMtuStatsTimeouts_Type()
)
nqaPathMtuStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsTimeouts.setStatus("current")
_NqaPathMtuStatsDrops_Type = Counter32
_NqaPathMtuStatsDrops_Object = MibTableColumn
nqaPathMtuStatsDrops = _NqaPathMtuStatsDrops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 12),
    _NqaPathMtuStatsDrops_Type()
)
nqaPathMtuStatsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsDrops.setStatus("current")
_NqaPathMtuStatsPathMtu_Type = Gauge32
_NqaPathMtuStatsPathMtu_Object = MibTableColumn
nqaPathMtuStatsPathMtu = _NqaPathMtuStatsPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 13),
    _NqaPathMtuStatsPathMtu_Type()
)
nqaPathMtuStatsPathMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsPathMtu.setStatus("current")


class _NqaPathMtuStatsTestFinished_Type(Integer32):
    """Custom type nqaPathMtuStatsTestFinished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finish", 1),
          ("nofinish", 0))
    )


_NqaPathMtuStatsTestFinished_Type.__name__ = "Integer32"
_NqaPathMtuStatsTestFinished_Object = MibTableColumn
nqaPathMtuStatsTestFinished = _NqaPathMtuStatsTestFinished_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 7, 1, 14),
    _NqaPathMtuStatsTestFinished_Type()
)
nqaPathMtuStatsTestFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathMtuStatsTestFinished.setStatus("current")
_NqaPathJitterStatsTable_Object = MibTable
nqaPathJitterStatsTable = _NqaPathJitterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8)
)
if mibBuilder.loadTexts:
    nqaPathJitterStatsTable.setStatus("current")
_NqaPathJitterStatsEntry_Object = MibTableRow
nqaPathJitterStatsEntry = _NqaPathJitterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1)
)
nqaPathJitterStatsEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaPathJitterStatsIndex"),
    (0, "NQA-MIB", "nqaPathJitterStatsHopIndex"),
)
if mibBuilder.loadTexts:
    nqaPathJitterStatsEntry.setStatus("current")


class _NqaPathJitterStatsIndex_Type(Integer32):
    """Custom type nqaPathJitterStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaPathJitterStatsIndex_Type.__name__ = "Integer32"
_NqaPathJitterStatsIndex_Object = MibTableColumn
nqaPathJitterStatsIndex = _NqaPathJitterStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 1),
    _NqaPathJitterStatsIndex_Type()
)
nqaPathJitterStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaPathJitterStatsIndex.setStatus("current")


class _NqaPathJitterStatsHopIndex_Type(Integer32):
    """Custom type nqaPathJitterStatsHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaPathJitterStatsHopIndex_Type.__name__ = "Integer32"
_NqaPathJitterStatsHopIndex_Object = MibTableColumn
nqaPathJitterStatsHopIndex = _NqaPathJitterStatsHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 2),
    _NqaPathJitterStatsHopIndex_Type()
)
nqaPathJitterStatsHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaPathJitterStatsHopIndex.setStatus("current")


class _NqaPathJitterStatsCompletions_Type(Integer32):
    """Custom type nqaPathJitterStatsCompletions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("noResult", 0),
          ("success", 1))
    )


_NqaPathJitterStatsCompletions_Type.__name__ = "Integer32"
_NqaPathJitterStatsCompletions_Object = MibTableColumn
nqaPathJitterStatsCompletions = _NqaPathJitterStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 3),
    _NqaPathJitterStatsCompletions_Type()
)
nqaPathJitterStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsCompletions.setStatus("current")
_NqaPathJitterStatsAddressType_Type = InetAddressType
_NqaPathJitterStatsAddressType_Object = MibTableColumn
nqaPathJitterStatsAddressType = _NqaPathJitterStatsAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 4),
    _NqaPathJitterStatsAddressType_Type()
)
nqaPathJitterStatsAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsAddressType.setStatus("current")
_NqaPathJitterStatsAddress_Type = InetAddress
_NqaPathJitterStatsAddress_Object = MibTableColumn
nqaPathJitterStatsAddress = _NqaPathJitterStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 5),
    _NqaPathJitterStatsAddress_Type()
)
nqaPathJitterStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsAddress.setStatus("current")
_NqaPathJitterStatsRtdOverThresholds_Type = Counter32
_NqaPathJitterStatsRtdOverThresholds_Object = MibTableColumn
nqaPathJitterStatsRtdOverThresholds = _NqaPathJitterStatsRtdOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 6),
    _NqaPathJitterStatsRtdOverThresholds_Type()
)
nqaPathJitterStatsRtdOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsRtdOverThresholds.setStatus("current")
_NqaPathJitterStatsNumOfRtt_Type = Counter32
_NqaPathJitterStatsNumOfRtt_Object = MibTableColumn
nqaPathJitterStatsNumOfRtt = _NqaPathJitterStatsNumOfRtt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 7),
    _NqaPathJitterStatsNumOfRtt_Type()
)
nqaPathJitterStatsNumOfRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsNumOfRtt.setStatus("current")
_NqaPathJitterStatsRttSum_Type = Counter32
_NqaPathJitterStatsRttSum_Object = MibTableColumn
nqaPathJitterStatsRttSum = _NqaPathJitterStatsRttSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 8),
    _NqaPathJitterStatsRttSum_Type()
)
nqaPathJitterStatsRttSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsRttSum.setStatus("current")
_NqaPathJitterStatsRttSum2Low_Type = Counter32
_NqaPathJitterStatsRttSum2Low_Object = MibTableColumn
nqaPathJitterStatsRttSum2Low = _NqaPathJitterStatsRttSum2Low_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 9),
    _NqaPathJitterStatsRttSum2Low_Type()
)
nqaPathJitterStatsRttSum2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsRttSum2Low.setStatus("current")
_NqaPathJitterStatsRttSum2High_Type = Counter32
_NqaPathJitterStatsRttSum2High_Object = MibTableColumn
nqaPathJitterStatsRttSum2High = _NqaPathJitterStatsRttSum2High_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 10),
    _NqaPathJitterStatsRttSum2High_Type()
)
nqaPathJitterStatsRttSum2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsRttSum2High.setStatus("current")
_NqaPathJitterStatsRttMin_Type = Gauge32
_NqaPathJitterStatsRttMin_Object = MibTableColumn
nqaPathJitterStatsRttMin = _NqaPathJitterStatsRttMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 11),
    _NqaPathJitterStatsRttMin_Type()
)
nqaPathJitterStatsRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsRttMin.setStatus("current")
_NqaPathJitterStatsRttMax_Type = Gauge32
_NqaPathJitterStatsRttMax_Object = MibTableColumn
nqaPathJitterStatsRttMax = _NqaPathJitterStatsRttMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 12),
    _NqaPathJitterStatsRttMax_Type()
)
nqaPathJitterStatsRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsRttMax.setStatus("current")
_NqaPathJitterStatsMinOfPositivesSD_Type = Gauge32
_NqaPathJitterStatsMinOfPositivesSD_Object = MibTableColumn
nqaPathJitterStatsMinOfPositivesSD = _NqaPathJitterStatsMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 13),
    _NqaPathJitterStatsMinOfPositivesSD_Type()
)
nqaPathJitterStatsMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMinOfPositivesSD.setStatus("current")
_NqaPathJitterStatsMaxOfPositivesSD_Type = Gauge32
_NqaPathJitterStatsMaxOfPositivesSD_Object = MibTableColumn
nqaPathJitterStatsMaxOfPositivesSD = _NqaPathJitterStatsMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 14),
    _NqaPathJitterStatsMaxOfPositivesSD_Type()
)
nqaPathJitterStatsMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMaxOfPositivesSD.setStatus("current")
_NqaPathJitterStatsNumOfPositivesSD_Type = Counter32
_NqaPathJitterStatsNumOfPositivesSD_Object = MibTableColumn
nqaPathJitterStatsNumOfPositivesSD = _NqaPathJitterStatsNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 15),
    _NqaPathJitterStatsNumOfPositivesSD_Type()
)
nqaPathJitterStatsNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsNumOfPositivesSD.setStatus("current")
_NqaPathJitterStatsSumOfPositivesSD_Type = Counter32
_NqaPathJitterStatsSumOfPositivesSD_Object = MibTableColumn
nqaPathJitterStatsSumOfPositivesSD = _NqaPathJitterStatsSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 16),
    _NqaPathJitterStatsSumOfPositivesSD_Type()
)
nqaPathJitterStatsSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSumOfPositivesSD.setStatus("current")
_NqaPathJitterStatsSum2OfPositivesSDLow_Type = Counter32
_NqaPathJitterStatsSum2OfPositivesSDLow_Object = MibTableColumn
nqaPathJitterStatsSum2OfPositivesSDLow = _NqaPathJitterStatsSum2OfPositivesSDLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 17),
    _NqaPathJitterStatsSum2OfPositivesSDLow_Type()
)
nqaPathJitterStatsSum2OfPositivesSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSum2OfPositivesSDLow.setStatus("current")
_NqaPathJitterStatsSum2OfPositivesSDHigh_Type = Counter32
_NqaPathJitterStatsSum2OfPositivesSDHigh_Object = MibTableColumn
nqaPathJitterStatsSum2OfPositivesSDHigh = _NqaPathJitterStatsSum2OfPositivesSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 18),
    _NqaPathJitterStatsSum2OfPositivesSDHigh_Type()
)
nqaPathJitterStatsSum2OfPositivesSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSum2OfPositivesSDHigh.setStatus("current")
_NqaPathJitterStatsMinOfNegativesSD_Type = Gauge32
_NqaPathJitterStatsMinOfNegativesSD_Object = MibTableColumn
nqaPathJitterStatsMinOfNegativesSD = _NqaPathJitterStatsMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 19),
    _NqaPathJitterStatsMinOfNegativesSD_Type()
)
nqaPathJitterStatsMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMinOfNegativesSD.setStatus("current")
_NqaPathJitterStatsMaxOfNegativesSD_Type = Gauge32
_NqaPathJitterStatsMaxOfNegativesSD_Object = MibTableColumn
nqaPathJitterStatsMaxOfNegativesSD = _NqaPathJitterStatsMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 20),
    _NqaPathJitterStatsMaxOfNegativesSD_Type()
)
nqaPathJitterStatsMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMaxOfNegativesSD.setStatus("current")
_NqaPathJitterStatsNumOfNegativesSD_Type = Counter32
_NqaPathJitterStatsNumOfNegativesSD_Object = MibTableColumn
nqaPathJitterStatsNumOfNegativesSD = _NqaPathJitterStatsNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 21),
    _NqaPathJitterStatsNumOfNegativesSD_Type()
)
nqaPathJitterStatsNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsNumOfNegativesSD.setStatus("current")
_NqaPathJitterStatsSumOfNegativesSD_Type = Counter32
_NqaPathJitterStatsSumOfNegativesSD_Object = MibTableColumn
nqaPathJitterStatsSumOfNegativesSD = _NqaPathJitterStatsSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 22),
    _NqaPathJitterStatsSumOfNegativesSD_Type()
)
nqaPathJitterStatsSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSumOfNegativesSD.setStatus("current")
_NqaPathJitterStatsSum2OfNegativesSDLow_Type = Counter32
_NqaPathJitterStatsSum2OfNegativesSDLow_Object = MibTableColumn
nqaPathJitterStatsSum2OfNegativesSDLow = _NqaPathJitterStatsSum2OfNegativesSDLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 23),
    _NqaPathJitterStatsSum2OfNegativesSDLow_Type()
)
nqaPathJitterStatsSum2OfNegativesSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSum2OfNegativesSDLow.setStatus("current")
_NqaPathJitterStatsSum2OfNegativesSDHigh_Type = Counter32
_NqaPathJitterStatsSum2OfNegativesSDHigh_Object = MibTableColumn
nqaPathJitterStatsSum2OfNegativesSDHigh = _NqaPathJitterStatsSum2OfNegativesSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 24),
    _NqaPathJitterStatsSum2OfNegativesSDHigh_Type()
)
nqaPathJitterStatsSum2OfNegativesSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSum2OfNegativesSDHigh.setStatus("current")
_NqaPathJitterStatsMinOfPositivesDS_Type = Gauge32
_NqaPathJitterStatsMinOfPositivesDS_Object = MibTableColumn
nqaPathJitterStatsMinOfPositivesDS = _NqaPathJitterStatsMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 25),
    _NqaPathJitterStatsMinOfPositivesDS_Type()
)
nqaPathJitterStatsMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMinOfPositivesDS.setStatus("current")
_NqaPathJitterStatsMaxOfPositivesDS_Type = Gauge32
_NqaPathJitterStatsMaxOfPositivesDS_Object = MibTableColumn
nqaPathJitterStatsMaxOfPositivesDS = _NqaPathJitterStatsMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 26),
    _NqaPathJitterStatsMaxOfPositivesDS_Type()
)
nqaPathJitterStatsMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMaxOfPositivesDS.setStatus("current")
_NqaPathJitterStatsNumOfPositivesDS_Type = Counter32
_NqaPathJitterStatsNumOfPositivesDS_Object = MibTableColumn
nqaPathJitterStatsNumOfPositivesDS = _NqaPathJitterStatsNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 27),
    _NqaPathJitterStatsNumOfPositivesDS_Type()
)
nqaPathJitterStatsNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsNumOfPositivesDS.setStatus("current")
_NqaPathJitterStatsSumOfPositivesDS_Type = Counter32
_NqaPathJitterStatsSumOfPositivesDS_Object = MibTableColumn
nqaPathJitterStatsSumOfPositivesDS = _NqaPathJitterStatsSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 28),
    _NqaPathJitterStatsSumOfPositivesDS_Type()
)
nqaPathJitterStatsSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSumOfPositivesDS.setStatus("current")
_NqaPathJitterStatsSum2OfPositivesDSLow_Type = Counter32
_NqaPathJitterStatsSum2OfPositivesDSLow_Object = MibTableColumn
nqaPathJitterStatsSum2OfPositivesDSLow = _NqaPathJitterStatsSum2OfPositivesDSLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 29),
    _NqaPathJitterStatsSum2OfPositivesDSLow_Type()
)
nqaPathJitterStatsSum2OfPositivesDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSum2OfPositivesDSLow.setStatus("current")
_NqaPathJitterStatsSum2OfPositivesDSHigh_Type = Counter32
_NqaPathJitterStatsSum2OfPositivesDSHigh_Object = MibTableColumn
nqaPathJitterStatsSum2OfPositivesDSHigh = _NqaPathJitterStatsSum2OfPositivesDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 30),
    _NqaPathJitterStatsSum2OfPositivesDSHigh_Type()
)
nqaPathJitterStatsSum2OfPositivesDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSum2OfPositivesDSHigh.setStatus("current")
_NqaPathJitterStatsMinOfNegativesDS_Type = Gauge32
_NqaPathJitterStatsMinOfNegativesDS_Object = MibTableColumn
nqaPathJitterStatsMinOfNegativesDS = _NqaPathJitterStatsMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 31),
    _NqaPathJitterStatsMinOfNegativesDS_Type()
)
nqaPathJitterStatsMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMinOfNegativesDS.setStatus("current")
_NqaPathJitterStatsMaxOfNegativesDS_Type = Gauge32
_NqaPathJitterStatsMaxOfNegativesDS_Object = MibTableColumn
nqaPathJitterStatsMaxOfNegativesDS = _NqaPathJitterStatsMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 32),
    _NqaPathJitterStatsMaxOfNegativesDS_Type()
)
nqaPathJitterStatsMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMaxOfNegativesDS.setStatus("current")
_NqaPathJitterStatsNumOfNegativesDS_Type = Counter32
_NqaPathJitterStatsNumOfNegativesDS_Object = MibTableColumn
nqaPathJitterStatsNumOfNegativesDS = _NqaPathJitterStatsNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 33),
    _NqaPathJitterStatsNumOfNegativesDS_Type()
)
nqaPathJitterStatsNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsNumOfNegativesDS.setStatus("current")
_NqaPathJitterStatsSumOfNegativesDS_Type = Counter32
_NqaPathJitterStatsSumOfNegativesDS_Object = MibTableColumn
nqaPathJitterStatsSumOfNegativesDS = _NqaPathJitterStatsSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 34),
    _NqaPathJitterStatsSumOfNegativesDS_Type()
)
nqaPathJitterStatsSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSumOfNegativesDS.setStatus("current")
_NqaPathJitterStatsSum2OfNegativesDSLow_Type = Counter32
_NqaPathJitterStatsSum2OfNegativesDSLow_Object = MibTableColumn
nqaPathJitterStatsSum2OfNegativesDSLow = _NqaPathJitterStatsSum2OfNegativesDSLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 35),
    _NqaPathJitterStatsSum2OfNegativesDSLow_Type()
)
nqaPathJitterStatsSum2OfNegativesDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSum2OfNegativesDSLow.setStatus("current")
_NqaPathJitterStatsSum2OfNegativesDSHigh_Type = Counter32
_NqaPathJitterStatsSum2OfNegativesDSHigh_Object = MibTableColumn
nqaPathJitterStatsSum2OfNegativesDSHigh = _NqaPathJitterStatsSum2OfNegativesDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 36),
    _NqaPathJitterStatsSum2OfNegativesDSHigh_Type()
)
nqaPathJitterStatsSum2OfNegativesDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSum2OfNegativesDSHigh.setStatus("current")
_NqaPathJitterStatsPacketLossSD_Type = Counter32
_NqaPathJitterStatsPacketLossSD_Object = MibTableColumn
nqaPathJitterStatsPacketLossSD = _NqaPathJitterStatsPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 37),
    _NqaPathJitterStatsPacketLossSD_Type()
)
nqaPathJitterStatsPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsPacketLossSD.setStatus("current")
_NqaPathJitterStatsPacketLossDS_Type = Counter32
_NqaPathJitterStatsPacketLossDS_Object = MibTableColumn
nqaPathJitterStatsPacketLossDS = _NqaPathJitterStatsPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 38),
    _NqaPathJitterStatsPacketLossDS_Type()
)
nqaPathJitterStatsPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsPacketLossDS.setStatus("current")
_NqaPathJitterStatsPacketOutOfSequences_Type = Counter32
_NqaPathJitterStatsPacketOutOfSequences_Object = MibTableColumn
nqaPathJitterStatsPacketOutOfSequences = _NqaPathJitterStatsPacketOutOfSequences_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 39),
    _NqaPathJitterStatsPacketOutOfSequences_Type()
)
nqaPathJitterStatsPacketOutOfSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsPacketOutOfSequences.setStatus("current")
_NqaPathJitterStatsErrors_Type = Counter32
_NqaPathJitterStatsErrors_Object = MibTableColumn
nqaPathJitterStatsErrors = _NqaPathJitterStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 40),
    _NqaPathJitterStatsErrors_Type()
)
nqaPathJitterStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsErrors.setStatus("current")
_NqaPathJitterStatsBusies_Type = Counter32
_NqaPathJitterStatsBusies_Object = MibTableColumn
nqaPathJitterStatsBusies = _NqaPathJitterStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 41),
    _NqaPathJitterStatsBusies_Type()
)
nqaPathJitterStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsBusies.setStatus("current")
_NqaPathJitterStatsTimeouts_Type = Counter32
_NqaPathJitterStatsTimeouts_Object = MibTableColumn
nqaPathJitterStatsTimeouts = _NqaPathJitterStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 42),
    _NqaPathJitterStatsTimeouts_Type()
)
nqaPathJitterStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsTimeouts.setStatus("current")
_NqaPathJitterStatsProbeResponses_Type = Counter32
_NqaPathJitterStatsProbeResponses_Object = MibTableColumn
nqaPathJitterStatsProbeResponses = _NqaPathJitterStatsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 43),
    _NqaPathJitterStatsProbeResponses_Type()
)
nqaPathJitterStatsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsProbeResponses.setStatus("current")
_NqaPathJitterStatsSentProbes_Type = Counter32
_NqaPathJitterStatsSentProbes_Object = MibTableColumn
nqaPathJitterStatsSentProbes = _NqaPathJitterStatsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 44),
    _NqaPathJitterStatsSentProbes_Type()
)
nqaPathJitterStatsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsSentProbes.setStatus("current")
_NqaPathJitterStatsDrops_Type = Counter32
_NqaPathJitterStatsDrops_Object = MibTableColumn
nqaPathJitterStatsDrops = _NqaPathJitterStatsDrops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 45),
    _NqaPathJitterStatsDrops_Type()
)
nqaPathJitterStatsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsDrops.setStatus("current")


class _NqaPathJitterStatsTestFinished_Type(Integer32):
    """Custom type nqaPathJitterStatsTestFinished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finish", 1),
          ("noFinish", 0))
    )


_NqaPathJitterStatsTestFinished_Type.__name__ = "Integer32"
_NqaPathJitterStatsTestFinished_Object = MibTableColumn
nqaPathJitterStatsTestFinished = _NqaPathJitterStatsTestFinished_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 46),
    _NqaPathJitterStatsTestFinished_Type()
)
nqaPathJitterStatsTestFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsTestFinished.setStatus("current")
_NqaPathJitterStatsMaxDelaySD_Type = Gauge32
_NqaPathJitterStatsMaxDelaySD_Object = MibTableColumn
nqaPathJitterStatsMaxDelaySD = _NqaPathJitterStatsMaxDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 47),
    _NqaPathJitterStatsMaxDelaySD_Type()
)
nqaPathJitterStatsMaxDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMaxDelaySD.setStatus("current")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMaxDelaySD.setUnits("milliseconds")
_NqaPathJitterStatsMaxDelayDS_Type = Gauge32
_NqaPathJitterStatsMaxDelayDS_Object = MibTableColumn
nqaPathJitterStatsMaxDelayDS = _NqaPathJitterStatsMaxDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 48),
    _NqaPathJitterStatsMaxDelayDS_Type()
)
nqaPathJitterStatsMaxDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMaxDelayDS.setStatus("current")
if mibBuilder.loadTexts:
    nqaPathJitterStatsMaxDelayDS.setUnits("milliseconds")
_NqaPathJitterStatsRttAvg_Type = Gauge32
_NqaPathJitterStatsRttAvg_Object = MibTableColumn
nqaPathJitterStatsRttAvg = _NqaPathJitterStatsRttAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 49),
    _NqaPathJitterStatsRttAvg_Type()
)
nqaPathJitterStatsRttAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsRttAvg.setStatus("current")
_NqaPathJitterStatsPacketLossRatio_Type = Gauge32
_NqaPathJitterStatsPacketLossRatio_Object = MibTableColumn
nqaPathJitterStatsPacketLossRatio = _NqaPathJitterStatsPacketLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 50),
    _NqaPathJitterStatsPacketLossRatio_Type()
)
nqaPathJitterStatsPacketLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsPacketLossRatio.setStatus("current")
_NqaPathJitterStatsAvgJitter_Type = Gauge32
_NqaPathJitterStatsAvgJitter_Object = MibTableColumn
nqaPathJitterStatsAvgJitter = _NqaPathJitterStatsAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 51),
    _NqaPathJitterStatsAvgJitter_Type()
)
nqaPathJitterStatsAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsAvgJitter.setStatus("current")
_NqaPathJitterStatsAvgJitterSD_Type = Gauge32
_NqaPathJitterStatsAvgJitterSD_Object = MibTableColumn
nqaPathJitterStatsAvgJitterSD = _NqaPathJitterStatsAvgJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 52),
    _NqaPathJitterStatsAvgJitterSD_Type()
)
nqaPathJitterStatsAvgJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsAvgJitterSD.setStatus("current")
_NqaPathJitterStatsAvgJitterDS_Type = Gauge32
_NqaPathJitterStatsAvgJitterDS_Object = MibTableColumn
nqaPathJitterStatsAvgJitterDS = _NqaPathJitterStatsAvgJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 53),
    _NqaPathJitterStatsAvgJitterDS_Type()
)
nqaPathJitterStatsAvgJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsAvgJitterDS.setStatus("current")
_NqaPathJitterStatsJitterOut_Type = OctetString
_NqaPathJitterStatsJitterOut_Object = MibTableColumn
nqaPathJitterStatsJitterOut = _NqaPathJitterStatsJitterOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 54),
    _NqaPathJitterStatsJitterOut_Type()
)
nqaPathJitterStatsJitterOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsJitterOut.setStatus("current")
_NqaPathJitterStatsJitterIn_Type = OctetString
_NqaPathJitterStatsJitterIn_Object = MibTableColumn
nqaPathJitterStatsJitterIn = _NqaPathJitterStatsJitterIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 55),
    _NqaPathJitterStatsJitterIn_Type()
)
nqaPathJitterStatsJitterIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsJitterIn.setStatus("current")
_NqaPathJitterStatsOwdOverThresholdsSD_Type = Counter32
_NqaPathJitterStatsOwdOverThresholdsSD_Object = MibTableColumn
nqaPathJitterStatsOwdOverThresholdsSD = _NqaPathJitterStatsOwdOverThresholdsSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 56),
    _NqaPathJitterStatsOwdOverThresholdsSD_Type()
)
nqaPathJitterStatsOwdOverThresholdsSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsOwdOverThresholdsSD.setStatus("current")
_NqaPathJitterStatsPktLossUnknown_Type = Counter32
_NqaPathJitterStatsPktLossUnknown_Object = MibTableColumn
nqaPathJitterStatsPktLossUnknown = _NqaPathJitterStatsPktLossUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 57),
    _NqaPathJitterStatsPktLossUnknown_Type()
)
nqaPathJitterStatsPktLossUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsPktLossUnknown.setStatus("current")
_NqaPathJitterStatsNumOfOwd_Type = Counter32
_NqaPathJitterStatsNumOfOwd_Object = MibTableColumn
nqaPathJitterStatsNumOfOwd = _NqaPathJitterStatsNumOfOwd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 58),
    _NqaPathJitterStatsNumOfOwd_Type()
)
nqaPathJitterStatsNumOfOwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsNumOfOwd.setStatus("current")
_NqaPathJitterStatsOwdSumSD_Type = Counter32
_NqaPathJitterStatsOwdSumSD_Object = MibTableColumn
nqaPathJitterStatsOwdSumSD = _NqaPathJitterStatsOwdSumSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 59),
    _NqaPathJitterStatsOwdSumSD_Type()
)
nqaPathJitterStatsOwdSumSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsOwdSumSD.setStatus("current")
_NqaPathJitterStatsOwdSumDS_Type = Counter32
_NqaPathJitterStatsOwdSumDS_Object = MibTableColumn
nqaPathJitterStatsOwdSumDS = _NqaPathJitterStatsOwdSumDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 60),
    _NqaPathJitterStatsOwdSumDS_Type()
)
nqaPathJitterStatsOwdSumDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsOwdSumDS.setStatus("current")
_NqaPathJitterStatsOwdOverThresholdsDS_Type = Counter32
_NqaPathJitterStatsOwdOverThresholdsDS_Object = MibTableColumn
nqaPathJitterStatsOwdOverThresholdsDS = _NqaPathJitterStatsOwdOverThresholdsDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 8, 1, 61),
    _NqaPathJitterStatsOwdOverThresholdsDS_Type()
)
nqaPathJitterStatsOwdOverThresholdsDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPathJitterStatsOwdOverThresholdsDS.setStatus("current")
_NqaPppoeStatsTable_Object = MibTable
nqaPppoeStatsTable = _NqaPppoeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9)
)
if mibBuilder.loadTexts:
    nqaPppoeStatsTable.setStatus("current")
_NqaPppoeStatsEntry_Object = MibTableRow
nqaPppoeStatsEntry = _NqaPppoeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1)
)
nqaPppoeStatsEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaPppoeStatsIndex"),
    (0, "NQA-MIB", "nqaPppoeRedialIndex"),
)
if mibBuilder.loadTexts:
    nqaPppoeStatsEntry.setStatus("current")


class _NqaPppoeStatsIndex_Type(Integer32):
    """Custom type nqaPppoeStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaPppoeStatsIndex_Type.__name__ = "Integer32"
_NqaPppoeStatsIndex_Object = MibTableColumn
nqaPppoeStatsIndex = _NqaPppoeStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 1),
    _NqaPppoeStatsIndex_Type()
)
nqaPppoeStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaPppoeStatsIndex.setStatus("current")


class _NqaPppoeRedialIndex_Type(Integer32):
    """Custom type nqaPppoeRedialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaPppoeRedialIndex_Type.__name__ = "Integer32"
_NqaPppoeRedialIndex_Object = MibTableColumn
nqaPppoeRedialIndex = _NqaPppoeRedialIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 2),
    _NqaPppoeRedialIndex_Type()
)
nqaPppoeRedialIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaPppoeRedialIndex.setStatus("current")


class _NqaPppoeStatsCompletions_Type(Integer32):
    """Custom type nqaPppoeStatsCompletions based on Integer32"""
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
        *(("dialupFail", 2),
          ("dialupSuccess", 1),
          ("exceptionStop", 4),
          ("stop", 3))
    )


_NqaPppoeStatsCompletions_Type.__name__ = "Integer32"
_NqaPppoeStatsCompletions_Object = MibTableColumn
nqaPppoeStatsCompletions = _NqaPppoeStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 3),
    _NqaPppoeStatsCompletions_Type()
)
nqaPppoeStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeStatsCompletions.setStatus("current")


class _NqaPppoeStatsCurrentPhase_Type(Integer32):
    """Custom type nqaPppoeStatsCurrentPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("authorization", 3),
          ("discovery", 1),
          ("lcp", 2),
          ("ncp", 4),
          ("online", 5),
          ("stop", 6))
    )


_NqaPppoeStatsCurrentPhase_Type.__name__ = "Integer32"
_NqaPppoeStatsCurrentPhase_Object = MibTableColumn
nqaPppoeStatsCurrentPhase = _NqaPppoeStatsCurrentPhase_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 4),
    _NqaPppoeStatsCurrentPhase_Type()
)
nqaPppoeStatsCurrentPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeStatsCurrentPhase.setStatus("current")


class _NqaPppoeStatsErrorMessage_Type(Integer32):
    """Custom type nqaPppoeStatsErrorMessage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 255),
          ("other", 1),
          ("paramNegotiateFail", 3),
          ("peerDownRequest", 5),
          ("timeout", 2),
          ("userAuthenticationFail", 4))
    )


_NqaPppoeStatsErrorMessage_Type.__name__ = "Integer32"
_NqaPppoeStatsErrorMessage_Object = MibTableColumn
nqaPppoeStatsErrorMessage = _NqaPppoeStatsErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 5),
    _NqaPppoeStatsErrorMessage_Type()
)
nqaPppoeStatsErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeStatsErrorMessage.setStatus("current")
_NqaPppoeDiscoveryTimeout_Type = Gauge32
_NqaPppoeDiscoveryTimeout_Object = MibTableColumn
nqaPppoeDiscoveryTimeout = _NqaPppoeDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 6),
    _NqaPppoeDiscoveryTimeout_Type()
)
nqaPppoeDiscoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeDiscoveryTimeout.setStatus("current")
_NqaPppoeLcpTimeout_Type = Gauge32
_NqaPppoeLcpTimeout_Object = MibTableColumn
nqaPppoeLcpTimeout = _NqaPppoeLcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 7),
    _NqaPppoeLcpTimeout_Type()
)
nqaPppoeLcpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeLcpTimeout.setStatus("current")
_NqaPppoeAuthorizationTimeout_Type = Gauge32
_NqaPppoeAuthorizationTimeout_Object = MibTableColumn
nqaPppoeAuthorizationTimeout = _NqaPppoeAuthorizationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 8),
    _NqaPppoeAuthorizationTimeout_Type()
)
nqaPppoeAuthorizationTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeAuthorizationTimeout.setStatus("current")
_NqaPppoeNcpTimeout_Type = Gauge32
_NqaPppoeNcpTimeout_Object = MibTableColumn
nqaPppoeNcpTimeout = _NqaPppoeNcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 9),
    _NqaPppoeNcpTimeout_Type()
)
nqaPppoeNcpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeNcpTimeout.setStatus("current")
_NqaPppoeConnectionTime_Type = Gauge32
_NqaPppoeConnectionTime_Object = MibTableColumn
nqaPppoeConnectionTime = _NqaPppoeConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 10),
    _NqaPppoeConnectionTime_Type()
)
nqaPppoeConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeConnectionTime.setStatus("current")
_NqaPppoeClientSessionId_Type = Gauge32
_NqaPppoeClientSessionId_Object = MibTableColumn
nqaPppoeClientSessionId = _NqaPppoeClientSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 11),
    _NqaPppoeClientSessionId_Type()
)
nqaPppoeClientSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeClientSessionId.setStatus("current")
_NqaPppoeClientIpAddress_Type = InetAddress
_NqaPppoeClientIpAddress_Object = MibTableColumn
nqaPppoeClientIpAddress = _NqaPppoeClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 12),
    _NqaPppoeClientIpAddress_Type()
)
nqaPppoeClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeClientIpAddress.setStatus("current")
_NqaPppoeGatewayIpAddress_Type = InetAddress
_NqaPppoeGatewayIpAddress_Object = MibTableColumn
nqaPppoeGatewayIpAddress = _NqaPppoeGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 4, 9, 1, 13),
    _NqaPppoeGatewayIpAddress_Type()
)
nqaPppoeGatewayIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaPppoeGatewayIpAddress.setStatus("current")
_NqaHistory_ObjectIdentity = ObjectIdentity
nqaHistory = _NqaHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5)
)
_NqaHistoryTable_Object = MibTable
nqaHistoryTable = _NqaHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1)
)
if mibBuilder.loadTexts:
    nqaHistoryTable.setStatus("current")
_NqaHistoryEntry_Object = MibTableRow
nqaHistoryEntry = _NqaHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1, 1)
)
nqaHistoryEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaHistoryIndex"),
    (0, "NQA-MIB", "nqaHistoryHopIndex"),
    (0, "NQA-MIB", "nqaHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    nqaHistoryEntry.setStatus("current")


class _NqaHistoryIndex_Type(Integer32):
    """Custom type nqaHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaHistoryIndex_Type.__name__ = "Integer32"
_NqaHistoryIndex_Object = MibTableColumn
nqaHistoryIndex = _NqaHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1, 1, 1),
    _NqaHistoryIndex_Type()
)
nqaHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaHistoryIndex.setStatus("current")


class _NqaHistoryHopIndex_Type(Integer32):
    """Custom type nqaHistoryHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaHistoryHopIndex_Type.__name__ = "Integer32"
_NqaHistoryHopIndex_Object = MibTableColumn
nqaHistoryHopIndex = _NqaHistoryHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1, 1, 2),
    _NqaHistoryHopIndex_Type()
)
nqaHistoryHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaHistoryHopIndex.setStatus("current")


class _NqaHistoryProbeIndex_Type(Integer32):
    """Custom type nqaHistoryProbeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaHistoryProbeIndex_Type.__name__ = "Integer32"
_NqaHistoryProbeIndex_Object = MibTableColumn
nqaHistoryProbeIndex = _NqaHistoryProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1, 1, 3),
    _NqaHistoryProbeIndex_Type()
)
nqaHistoryProbeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaHistoryProbeIndex.setStatus("current")
_NqaHistoryTimeStamp_Type = DateAndTime
_NqaHistoryTimeStamp_Object = MibTableColumn
nqaHistoryTimeStamp = _NqaHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1, 1, 4),
    _NqaHistoryTimeStamp_Type()
)
nqaHistoryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHistoryTimeStamp.setStatus("current")
_NqaHistoryAddressType_Type = InetAddressType
_NqaHistoryAddressType_Object = MibTableColumn
nqaHistoryAddressType = _NqaHistoryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1, 1, 5),
    _NqaHistoryAddressType_Type()
)
nqaHistoryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHistoryAddressType.setStatus("current")
_NqaHistoryAddress_Type = InetAddress
_NqaHistoryAddress_Object = MibTableColumn
nqaHistoryAddress = _NqaHistoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1, 1, 6),
    _NqaHistoryAddress_Type()
)
nqaHistoryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHistoryAddress.setStatus("current")
_NqaHistoryCompletionTime_Type = Integer32
_NqaHistoryCompletionTime_Object = MibTableColumn
nqaHistoryCompletionTime = _NqaHistoryCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1, 1, 7),
    _NqaHistoryCompletionTime_Type()
)
nqaHistoryCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHistoryCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaHistoryCompletionTime.setUnits("milliseconds")


class _NqaHistoryFinishState_Type(Integer32):
    """Custom type nqaHistoryFinishState based on Integer32"""
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
        *(("busy", 4),
          ("disconnected", 6),
          ("drop", 3),
          ("noConnected", 7),
          ("overThreshold", 5),
          ("success", 1),
          ("timeout", 2))
    )


_NqaHistoryFinishState_Type.__name__ = "Integer32"
_NqaHistoryFinishState_Object = MibTableColumn
nqaHistoryFinishState = _NqaHistoryFinishState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1, 1, 8),
    _NqaHistoryFinishState_Type()
)
nqaHistoryFinishState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHistoryFinishState.setStatus("current")
_NqaHistoryLastRC_Type = Integer32
_NqaHistoryLastRC_Object = MibTableColumn
nqaHistoryLastRC = _NqaHistoryLastRC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 1, 1, 9),
    _NqaHistoryLastRC_Type()
)
nqaHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaHistoryLastRC.setStatus("current")
_NqaMpingHistoryTable_Object = MibTable
nqaMpingHistoryTable = _NqaMpingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2)
)
if mibBuilder.loadTexts:
    nqaMpingHistoryTable.setStatus("current")
_NqaMpingHistoryEntry_Object = MibTableRow
nqaMpingHistoryEntry = _NqaMpingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1)
)
nqaMpingHistoryEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaMpingHistoryIndex"),
    (0, "NQA-MIB", "nqaMpingHistoryReceiverIndex"),
    (0, "NQA-MIB", "nqaMpingHistoryResponseIndex"),
)
if mibBuilder.loadTexts:
    nqaMpingHistoryEntry.setStatus("current")


class _NqaMpingHistoryIndex_Type(Integer32):
    """Custom type nqaMpingHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMpingHistoryIndex_Type.__name__ = "Integer32"
_NqaMpingHistoryIndex_Object = MibTableColumn
nqaMpingHistoryIndex = _NqaMpingHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 1),
    _NqaMpingHistoryIndex_Type()
)
nqaMpingHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMpingHistoryIndex.setStatus("current")


class _NqaMpingHistoryReceiverIndex_Type(Integer32):
    """Custom type nqaMpingHistoryReceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMpingHistoryReceiverIndex_Type.__name__ = "Integer32"
_NqaMpingHistoryReceiverIndex_Object = MibTableColumn
nqaMpingHistoryReceiverIndex = _NqaMpingHistoryReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 2),
    _NqaMpingHistoryReceiverIndex_Type()
)
nqaMpingHistoryReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMpingHistoryReceiverIndex.setStatus("current")


class _NqaMpingHistoryResponseIndex_Type(Integer32):
    """Custom type nqaMpingHistoryResponseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMpingHistoryResponseIndex_Type.__name__ = "Integer32"
_NqaMpingHistoryResponseIndex_Object = MibTableColumn
nqaMpingHistoryResponseIndex = _NqaMpingHistoryResponseIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 3),
    _NqaMpingHistoryResponseIndex_Type()
)
nqaMpingHistoryResponseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMpingHistoryResponseIndex.setStatus("current")
_NqaMpingHistoryAddressType_Type = InetAddressType
_NqaMpingHistoryAddressType_Object = MibTableColumn
nqaMpingHistoryAddressType = _NqaMpingHistoryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 4),
    _NqaMpingHistoryAddressType_Type()
)
nqaMpingHistoryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingHistoryAddressType.setStatus("current")
_NqaMpingHistoryAddress_Type = InetAddress
_NqaMpingHistoryAddress_Object = MibTableColumn
nqaMpingHistoryAddress = _NqaMpingHistoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 5),
    _NqaMpingHistoryAddress_Type()
)
nqaMpingHistoryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingHistoryAddress.setStatus("current")
_NqaMpingHistoryReceiverAddress_Type = InetAddress
_NqaMpingHistoryReceiverAddress_Object = MibTableColumn
nqaMpingHistoryReceiverAddress = _NqaMpingHistoryReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 6),
    _NqaMpingHistoryReceiverAddress_Type()
)
nqaMpingHistoryReceiverAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingHistoryReceiverAddress.setStatus("current")
_NqaMpingHistoryTimeStamp_Type = DateAndTime
_NqaMpingHistoryTimeStamp_Object = MibTableColumn
nqaMpingHistoryTimeStamp = _NqaMpingHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 7),
    _NqaMpingHistoryTimeStamp_Type()
)
nqaMpingHistoryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingHistoryTimeStamp.setStatus("current")
_NqaMpingHistoryCompletionTime_Type = Integer32
_NqaMpingHistoryCompletionTime_Object = MibTableColumn
nqaMpingHistoryCompletionTime = _NqaMpingHistoryCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 8),
    _NqaMpingHistoryCompletionTime_Type()
)
nqaMpingHistoryCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingHistoryCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaMpingHistoryCompletionTime.setUnits("milliseconds")


class _NqaMpingHistoryFinishState_Type(Integer32):
    """Custom type nqaMpingHistoryFinishState based on Integer32"""
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
        *(("busy", 4),
          ("disconnected", 6),
          ("drop", 3),
          ("noConnected", 7),
          ("overThreshold", 5),
          ("success", 1),
          ("timeout", 2))
    )


_NqaMpingHistoryFinishState_Type.__name__ = "Integer32"
_NqaMpingHistoryFinishState_Object = MibTableColumn
nqaMpingHistoryFinishState = _NqaMpingHistoryFinishState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 9),
    _NqaMpingHistoryFinishState_Type()
)
nqaMpingHistoryFinishState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingHistoryFinishState.setStatus("current")
_NqaMpingHistoryLastRC_Type = Integer32
_NqaMpingHistoryLastRC_Object = MibTableColumn
nqaMpingHistoryLastRC = _NqaMpingHistoryLastRC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 10),
    _NqaMpingHistoryLastRC_Type()
)
nqaMpingHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingHistoryLastRC.setStatus("current")
_NqaMpingHistoryFibHit_Type = TruthValue
_NqaMpingHistoryFibHit_Object = MibTableColumn
nqaMpingHistoryFibHit = _NqaMpingHistoryFibHit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 2, 1, 11),
    _NqaMpingHistoryFibHit_Type()
)
nqaMpingHistoryFibHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMpingHistoryFibHit.setStatus("current")
_NqaMtracertHistoryTable_Object = MibTable
nqaMtracertHistoryTable = _NqaMtracertHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3)
)
if mibBuilder.loadTexts:
    nqaMtracertHistoryTable.setStatus("current")
_NqaMtracertHistoryEntry_Object = MibTableRow
nqaMtracertHistoryEntry = _NqaMtracertHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1)
)
nqaMtracertHistoryEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaMtracertHistoryIndex"),
    (0, "NQA-MIB", "nqaMtracertHistoryHopIndex"),
)
if mibBuilder.loadTexts:
    nqaMtracertHistoryEntry.setStatus("current")


class _NqaMtracertHistoryIndex_Type(Integer32):
    """Custom type nqaMtracertHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMtracertHistoryIndex_Type.__name__ = "Integer32"
_NqaMtracertHistoryIndex_Object = MibTableColumn
nqaMtracertHistoryIndex = _NqaMtracertHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 1),
    _NqaMtracertHistoryIndex_Type()
)
nqaMtracertHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMtracertHistoryIndex.setStatus("current")


class _NqaMtracertHistoryHopIndex_Type(Integer32):
    """Custom type nqaMtracertHistoryHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaMtracertHistoryHopIndex_Type.__name__ = "Integer32"
_NqaMtracertHistoryHopIndex_Object = MibTableColumn
nqaMtracertHistoryHopIndex = _NqaMtracertHistoryHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 2),
    _NqaMtracertHistoryHopIndex_Type()
)
nqaMtracertHistoryHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMtracertHistoryHopIndex.setStatus("current")
_NqaMtracertHistoryAddressType_Type = InetAddressType
_NqaMtracertHistoryAddressType_Object = MibTableColumn
nqaMtracertHistoryAddressType = _NqaMtracertHistoryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 3),
    _NqaMtracertHistoryAddressType_Type()
)
nqaMtracertHistoryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryAddressType.setStatus("current")
_NqaMtracertHistoryAddress_Type = InetAddress
_NqaMtracertHistoryAddress_Object = MibTableColumn
nqaMtracertHistoryAddress = _NqaMtracertHistoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 4),
    _NqaMtracertHistoryAddress_Type()
)
nqaMtracertHistoryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryAddress.setStatus("current")
_NqaMtracertHistoryTimeStamp_Type = DateAndTime
_NqaMtracertHistoryTimeStamp_Object = MibTableColumn
nqaMtracertHistoryTimeStamp = _NqaMtracertHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 5),
    _NqaMtracertHistoryTimeStamp_Type()
)
nqaMtracertHistoryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryTimeStamp.setStatus("current")
_NqaMtracertHistoryCompletionTime_Type = Integer32
_NqaMtracertHistoryCompletionTime_Object = MibTableColumn
nqaMtracertHistoryCompletionTime = _NqaMtracertHistoryCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 6),
    _NqaMtracertHistoryCompletionTime_Type()
)
nqaMtracertHistoryCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaMtracertHistoryCompletionTime.setUnits("milliseconds")
_NqaMtracertHistoryLastRC_Type = Integer32
_NqaMtracertHistoryLastRC_Object = MibTableColumn
nqaMtracertHistoryLastRC = _NqaMtracertHistoryLastRC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 7),
    _NqaMtracertHistoryLastRC_Type()
)
nqaMtracertHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryLastRC.setStatus("current")


class _NqaMtracertHistoryCurQueryMode_Type(Integer32):
    """Custom type nqaMtracertHistoryCurQueryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hopByHop", 2),
          ("maxHops", 1))
    )


_NqaMtracertHistoryCurQueryMode_Type.__name__ = "Integer32"
_NqaMtracertHistoryCurQueryMode_Object = MibTableColumn
nqaMtracertHistoryCurQueryMode = _NqaMtracertHistoryCurQueryMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 8),
    _NqaMtracertHistoryCurQueryMode_Type()
)
nqaMtracertHistoryCurQueryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryCurQueryMode.setStatus("current")
_NqaMtracertHistoryQueryArrivalTime_Type = Unsigned32
_NqaMtracertHistoryQueryArrivalTime_Object = MibTableColumn
nqaMtracertHistoryQueryArrivalTime = _NqaMtracertHistoryQueryArrivalTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 9),
    _NqaMtracertHistoryQueryArrivalTime_Type()
)
nqaMtracertHistoryQueryArrivalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryQueryArrivalTime.setStatus("current")
_NqaMtracertHistoryIncomingIfAddress_Type = InetAddress
_NqaMtracertHistoryIncomingIfAddress_Object = MibTableColumn
nqaMtracertHistoryIncomingIfAddress = _NqaMtracertHistoryIncomingIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 10),
    _NqaMtracertHistoryIncomingIfAddress_Type()
)
nqaMtracertHistoryIncomingIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryIncomingIfAddress.setStatus("current")
_NqaMtracertHistoryOutgoingIfAddress_Type = InetAddress
_NqaMtracertHistoryOutgoingIfAddress_Object = MibTableColumn
nqaMtracertHistoryOutgoingIfAddress = _NqaMtracertHistoryOutgoingIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 11),
    _NqaMtracertHistoryOutgoingIfAddress_Type()
)
nqaMtracertHistoryOutgoingIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryOutgoingIfAddress.setStatus("current")
_NqaMtracertHistoryPreHopRouterAddress_Type = InetAddress
_NqaMtracertHistoryPreHopRouterAddress_Object = MibTableColumn
nqaMtracertHistoryPreHopRouterAddress = _NqaMtracertHistoryPreHopRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 12),
    _NqaMtracertHistoryPreHopRouterAddress_Type()
)
nqaMtracertHistoryPreHopRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryPreHopRouterAddress.setStatus("current")
_NqaMtracertHistoryInputPacketCount_Type = Gauge32
_NqaMtracertHistoryInputPacketCount_Object = MibTableColumn
nqaMtracertHistoryInputPacketCount = _NqaMtracertHistoryInputPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 13),
    _NqaMtracertHistoryInputPacketCount_Type()
)
nqaMtracertHistoryInputPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryInputPacketCount.setStatus("current")
_NqaMtracertHistoryOutputPacketCount_Type = Gauge32
_NqaMtracertHistoryOutputPacketCount_Object = MibTableColumn
nqaMtracertHistoryOutputPacketCount = _NqaMtracertHistoryOutputPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 14),
    _NqaMtracertHistoryOutputPacketCount_Type()
)
nqaMtracertHistoryOutputPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryOutputPacketCount.setStatus("current")
_NqaMtracertHistoryTotalSGPacketCount_Type = Gauge32
_NqaMtracertHistoryTotalSGPacketCount_Object = MibTableColumn
nqaMtracertHistoryTotalSGPacketCount = _NqaMtracertHistoryTotalSGPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 15),
    _NqaMtracertHistoryTotalSGPacketCount_Type()
)
nqaMtracertHistoryTotalSGPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryTotalSGPacketCount.setStatus("current")


class _NqaMtracertHistoryRtgProtocol_Type(Integer32):
    """Custom type nqaMtracertHistoryRtgProtocol based on Integer32"""
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
              10,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cbt", 4),
          ("cbtUsingSpecRteTab", 9),
          ("cbtUsingStaticRte", 10),
          ("dvmrp", 1),
          ("dvmrpUsingStaticRte", 7),
          ("mospf", 2),
          ("pim", 3),
          ("pimUsingMBGPRte", 8),
          ("pimUsingSpecRteTab", 5),
          ("pimUsingState", 11),
          ("pimUsingStaticRte", 6),
          ("unknownProtocol", 255))
    )


_NqaMtracertHistoryRtgProtocol_Type.__name__ = "Integer32"
_NqaMtracertHistoryRtgProtocol_Object = MibTableColumn
nqaMtracertHistoryRtgProtocol = _NqaMtracertHistoryRtgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 16),
    _NqaMtracertHistoryRtgProtocol_Type()
)
nqaMtracertHistoryRtgProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryRtgProtocol.setStatus("current")
_NqaMtracertHistoryFwdTTL_Type = Gauge32
_NqaMtracertHistoryFwdTTL_Object = MibTableColumn
nqaMtracertHistoryFwdTTL = _NqaMtracertHistoryFwdTTL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 17),
    _NqaMtracertHistoryFwdTTL_Type()
)
nqaMtracertHistoryFwdTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryFwdTTL.setStatus("current")


class _NqaMtracertHistoryFwdCode_Type(Integer32):
    """Custom type nqaMtracertHistoryFwdCode based on Integer32"""
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
              11,
              12,
              130,
              131,
              132,
              255)
        )
    )
    namedValues = NamedValues(
        *(("adminProhib", 132),
          ("infoHidden", 12),
          ("noError", 1),
          ("noMulticast", 11),
          ("noRoute", 6),
          ("noSpace", 130),
          ("notForwarding", 8),
          ("oldRouter", 131),
          ("pruneRCVD", 4),
          ("pruneSent", 3),
          ("reachedRP", 9),
          ("scoped", 5),
          ("unknownError", 255),
          ("wrongIf", 2),
          ("wrongLastHop", 7))
    )


_NqaMtracertHistoryFwdCode_Type.__name__ = "Integer32"
_NqaMtracertHistoryFwdCode_Object = MibTableColumn
nqaMtracertHistoryFwdCode = _NqaMtracertHistoryFwdCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 18),
    _NqaMtracertHistoryFwdCode_Type()
)
nqaMtracertHistoryFwdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistoryFwdCode.setStatus("current")


class _NqaMtracertHistroyFinishState_Type(Integer32):
    """Custom type nqaMtracertHistroyFinishState based on Integer32"""
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
        *(("busy", 3),
          ("disconnected", 6),
          ("drop", 4),
          ("noConnected", 7),
          ("overThreshold", 5),
          ("success", 1),
          ("timeout", 2))
    )


_NqaMtracertHistroyFinishState_Type.__name__ = "Integer32"
_NqaMtracertHistroyFinishState_Object = MibTableColumn
nqaMtracertHistroyFinishState = _NqaMtracertHistroyFinishState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 3, 1, 19),
    _NqaMtracertHistroyFinishState_Type()
)
nqaMtracertHistroyFinishState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMtracertHistroyFinishState.setStatus("current")
_NqaVplsMacTracertHistoryTable_Object = MibTable
nqaVplsMacTracertHistoryTable = _NqaVplsMacTracertHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4)
)
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryTable.setStatus("current")
_NqaVplsMacTracertHistoryEntry_Object = MibTableRow
nqaVplsMacTracertHistoryEntry = _NqaVplsMacTracertHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1)
)
nqaVplsMacTracertHistoryEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaVplsMacTracertHistoryIndex"),
    (0, "NQA-MIB", "nqaVplsMacTracertHistoryHopIndex"),
    (0, "NQA-MIB", "nqaVplsMacTracertHistoryResponseIndex"),
)
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryEntry.setStatus("current")


class _NqaVplsMacTracertHistoryIndex_Type(Integer32):
    """Custom type nqaVplsMacTracertHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaVplsMacTracertHistoryIndex_Type.__name__ = "Integer32"
_NqaVplsMacTracertHistoryIndex_Object = MibTableColumn
nqaVplsMacTracertHistoryIndex = _NqaVplsMacTracertHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 1),
    _NqaVplsMacTracertHistoryIndex_Type()
)
nqaVplsMacTracertHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryIndex.setStatus("current")


class _NqaVplsMacTracertHistoryHopIndex_Type(Integer32):
    """Custom type nqaVplsMacTracertHistoryHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaVplsMacTracertHistoryHopIndex_Type.__name__ = "Integer32"
_NqaVplsMacTracertHistoryHopIndex_Object = MibTableColumn
nqaVplsMacTracertHistoryHopIndex = _NqaVplsMacTracertHistoryHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 2),
    _NqaVplsMacTracertHistoryHopIndex_Type()
)
nqaVplsMacTracertHistoryHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryHopIndex.setStatus("current")


class _NqaVplsMacTracertHistoryResponseIndex_Type(Integer32):
    """Custom type nqaVplsMacTracertHistoryResponseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaVplsMacTracertHistoryResponseIndex_Type.__name__ = "Integer32"
_NqaVplsMacTracertHistoryResponseIndex_Object = MibTableColumn
nqaVplsMacTracertHistoryResponseIndex = _NqaVplsMacTracertHistoryResponseIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 3),
    _NqaVplsMacTracertHistoryResponseIndex_Type()
)
nqaVplsMacTracertHistoryResponseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryResponseIndex.setStatus("current")
_NqaVplsMacTracertHistoryTimeStamp_Type = DateAndTime
_NqaVplsMacTracertHistoryTimeStamp_Object = MibTableColumn
nqaVplsMacTracertHistoryTimeStamp = _NqaVplsMacTracertHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 4),
    _NqaVplsMacTracertHistoryTimeStamp_Type()
)
nqaVplsMacTracertHistoryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryTimeStamp.setStatus("current")
_NqaVplsMacTracertHistoryAddressType_Type = InetAddressType
_NqaVplsMacTracertHistoryAddressType_Object = MibTableColumn
nqaVplsMacTracertHistoryAddressType = _NqaVplsMacTracertHistoryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 5),
    _NqaVplsMacTracertHistoryAddressType_Type()
)
nqaVplsMacTracertHistoryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryAddressType.setStatus("current")
_NqaVplsMacTracertHistoryAddress_Type = InetAddress
_NqaVplsMacTracertHistoryAddress_Object = MibTableColumn
nqaVplsMacTracertHistoryAddress = _NqaVplsMacTracertHistoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 6),
    _NqaVplsMacTracertHistoryAddress_Type()
)
nqaVplsMacTracertHistoryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryAddress.setStatus("current")
_NqaVplsMacTracertHistoryCompletionTime_Type = Integer32
_NqaVplsMacTracertHistoryCompletionTime_Object = MibTableColumn
nqaVplsMacTracertHistoryCompletionTime = _NqaVplsMacTracertHistoryCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 7),
    _NqaVplsMacTracertHistoryCompletionTime_Type()
)
nqaVplsMacTracertHistoryCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryCompletionTime.setUnits("milliseconds")


class _NqaVplsMacTracertHistoryFinishState_Type(Integer32):
    """Custom type nqaVplsMacTracertHistoryFinishState based on Integer32"""
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
        *(("busy", 4),
          ("disconnected", 6),
          ("drop", 3),
          ("noConnected", 7),
          ("overThreshold", 5),
          ("success", 1),
          ("timeout", 2))
    )


_NqaVplsMacTracertHistoryFinishState_Type.__name__ = "Integer32"
_NqaVplsMacTracertHistoryFinishState_Object = MibTableColumn
nqaVplsMacTracertHistoryFinishState = _NqaVplsMacTracertHistoryFinishState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 8),
    _NqaVplsMacTracertHistoryFinishState_Type()
)
nqaVplsMacTracertHistoryFinishState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryFinishState.setStatus("current")
_NqaVplsMacTracertHistoryHitFlag_Type = TruthValue
_NqaVplsMacTracertHistoryHitFlag_Object = MibTableColumn
nqaVplsMacTracertHistoryHitFlag = _NqaVplsMacTracertHistoryHitFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 9),
    _NqaVplsMacTracertHistoryHitFlag_Type()
)
nqaVplsMacTracertHistoryHitFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryHitFlag.setStatus("current")


class _NqaVplsMacTracertHistoryDSCount_Type(Integer32):
    """Custom type nqaVplsMacTracertHistoryDSCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NqaVplsMacTracertHistoryDSCount_Type.__name__ = "Integer32"
_NqaVplsMacTracertHistoryDSCount_Object = MibTableColumn
nqaVplsMacTracertHistoryDSCount = _NqaVplsMacTracertHistoryDSCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 10),
    _NqaVplsMacTracertHistoryDSCount_Type()
)
nqaVplsMacTracertHistoryDSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryDSCount.setStatus("current")
_NqaVplsMacTracertHistorySuccessPathNode_Type = TruthValue
_NqaVplsMacTracertHistorySuccessPathNode_Object = MibTableColumn
nqaVplsMacTracertHistorySuccessPathNode = _NqaVplsMacTracertHistorySuccessPathNode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 4, 1, 11),
    _NqaVplsMacTracertHistorySuccessPathNode_Type()
)
nqaVplsMacTracertHistorySuccessPathNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistorySuccessPathNode.setStatus("current")
_NqaVplsMacTracertHistoryDSTable_Object = MibTable
nqaVplsMacTracertHistoryDSTable = _NqaVplsMacTracertHistoryDSTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 5)
)
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryDSTable.setStatus("current")
_NqaVplsMacTracertHistoryDSEntry_Object = MibTableRow
nqaVplsMacTracertHistoryDSEntry = _NqaVplsMacTracertHistoryDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 5, 1)
)
nqaVplsMacTracertHistoryDSEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaVplsMacTracertHistoryIndex"),
    (0, "NQA-MIB", "nqaVplsMacTracertHistoryHopIndex"),
    (0, "NQA-MIB", "nqaVplsMacTracertHistoryResponseIndex"),
    (0, "NQA-MIB", "nqaVplsMacTracertHistoryDSIndex"),
)
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryDSEntry.setStatus("current")


class _NqaVplsMacTracertHistoryDSIndex_Type(Integer32):
    """Custom type nqaVplsMacTracertHistoryDSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaVplsMacTracertHistoryDSIndex_Type.__name__ = "Integer32"
_NqaVplsMacTracertHistoryDSIndex_Object = MibTableColumn
nqaVplsMacTracertHistoryDSIndex = _NqaVplsMacTracertHistoryDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 5, 1, 1),
    _NqaVplsMacTracertHistoryDSIndex_Type()
)
nqaVplsMacTracertHistoryDSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryDSIndex.setStatus("current")
_NqaVplsMacTracertHistoryDSAddress_Type = InetAddress
_NqaVplsMacTracertHistoryDSAddress_Object = MibTableColumn
nqaVplsMacTracertHistoryDSAddress = _NqaVplsMacTracertHistoryDSAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 5, 1, 2),
    _NqaVplsMacTracertHistoryDSAddress_Type()
)
nqaVplsMacTracertHistoryDSAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMacTracertHistoryDSAddress.setStatus("current")
_NqaVplsMTraceHistoryTable_Object = MibTable
nqaVplsMTraceHistoryTable = _NqaVplsMTraceHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6)
)
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryTable.setStatus("current")
_NqaVplsMTraceHistoryEntry_Object = MibTableRow
nqaVplsMTraceHistoryEntry = _NqaVplsMTraceHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1)
)
nqaVplsMTraceHistoryEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaVplsMTraceHistoryIndex"),
    (0, "NQA-MIB", "nqaVplsMTraceHistoryHopIndex"),
    (0, "NQA-MIB", "nqaVplsMTraceHistoryResponseIndex"),
)
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryEntry.setStatus("current")


class _NqaVplsMTraceHistoryIndex_Type(Integer32):
    """Custom type nqaVplsMTraceHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaVplsMTraceHistoryIndex_Type.__name__ = "Integer32"
_NqaVplsMTraceHistoryIndex_Object = MibTableColumn
nqaVplsMTraceHistoryIndex = _NqaVplsMTraceHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 1),
    _NqaVplsMTraceHistoryIndex_Type()
)
nqaVplsMTraceHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryIndex.setStatus("current")


class _NqaVplsMTraceHistoryHopIndex_Type(Integer32):
    """Custom type nqaVplsMTraceHistoryHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaVplsMTraceHistoryHopIndex_Type.__name__ = "Integer32"
_NqaVplsMTraceHistoryHopIndex_Object = MibTableColumn
nqaVplsMTraceHistoryHopIndex = _NqaVplsMTraceHistoryHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 2),
    _NqaVplsMTraceHistoryHopIndex_Type()
)
nqaVplsMTraceHistoryHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryHopIndex.setStatus("current")


class _NqaVplsMTraceHistoryResponseIndex_Type(Integer32):
    """Custom type nqaVplsMTraceHistoryResponseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaVplsMTraceHistoryResponseIndex_Type.__name__ = "Integer32"
_NqaVplsMTraceHistoryResponseIndex_Object = MibTableColumn
nqaVplsMTraceHistoryResponseIndex = _NqaVplsMTraceHistoryResponseIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 3),
    _NqaVplsMTraceHistoryResponseIndex_Type()
)
nqaVplsMTraceHistoryResponseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryResponseIndex.setStatus("current")
_NqaVplsMTraceHistoryResponserAddressType_Type = InetAddressType
_NqaVplsMTraceHistoryResponserAddressType_Object = MibTableColumn
nqaVplsMTraceHistoryResponserAddressType = _NqaVplsMTraceHistoryResponserAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 4),
    _NqaVplsMTraceHistoryResponserAddressType_Type()
)
nqaVplsMTraceHistoryResponserAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryResponserAddressType.setStatus("current")
_NqaVplsMTraceHistoryResponserAddress_Type = InetAddress
_NqaVplsMTraceHistoryResponserAddress_Object = MibTableColumn
nqaVplsMTraceHistoryResponserAddress = _NqaVplsMTraceHistoryResponserAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 5),
    _NqaVplsMTraceHistoryResponserAddress_Type()
)
nqaVplsMTraceHistoryResponserAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryResponserAddress.setStatus("current")
_NqaVplsMTraceHistoryUpStreamAddressType_Type = InetAddressType
_NqaVplsMTraceHistoryUpStreamAddressType_Object = MibTableColumn
nqaVplsMTraceHistoryUpStreamAddressType = _NqaVplsMTraceHistoryUpStreamAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 6),
    _NqaVplsMTraceHistoryUpStreamAddressType_Type()
)
nqaVplsMTraceHistoryUpStreamAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryUpStreamAddressType.setStatus("current")
_NqaVplsMTraceHistoryUpStreamAddress_Type = InetAddress
_NqaVplsMTraceHistoryUpStreamAddress_Object = MibTableColumn
nqaVplsMTraceHistoryUpStreamAddress = _NqaVplsMTraceHistoryUpStreamAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 7),
    _NqaVplsMTraceHistoryUpStreamAddress_Type()
)
nqaVplsMTraceHistoryUpStreamAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryUpStreamAddress.setStatus("current")


class _NqaVplsMTraceHistoryReceivedTtl_Type(Unsigned32):
    """Custom type nqaVplsMTraceHistoryReceivedTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaVplsMTraceHistoryReceivedTtl_Type.__name__ = "Unsigned32"
_NqaVplsMTraceHistoryReceivedTtl_Object = MibTableColumn
nqaVplsMTraceHistoryReceivedTtl = _NqaVplsMTraceHistoryReceivedTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 8),
    _NqaVplsMTraceHistoryReceivedTtl_Type()
)
nqaVplsMTraceHistoryReceivedTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryReceivedTtl.setStatus("current")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryReceivedTtl.setUnits("time-to-live value")


class _NqaVplsMTraceHistoryIGMPVersion_Type(Integer32):
    """Custom type nqaVplsMTraceHistoryIGMPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1", 1),
          ("igmpv2", 2),
          ("igmpv3", 3))
    )


_NqaVplsMTraceHistoryIGMPVersion_Type.__name__ = "Integer32"
_NqaVplsMTraceHistoryIGMPVersion_Object = MibTableColumn
nqaVplsMTraceHistoryIGMPVersion = _NqaVplsMTraceHistoryIGMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 9),
    _NqaVplsMTraceHistoryIGMPVersion_Type()
)
nqaVplsMTraceHistoryIGMPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryIGMPVersion.setStatus("current")
_NqaVplsMTraceHistoryIGMPSnpgEnable_Type = EnableValue
_NqaVplsMTraceHistoryIGMPSnpgEnable_Object = MibTableColumn
nqaVplsMTraceHistoryIGMPSnpgEnable = _NqaVplsMTraceHistoryIGMPSnpgEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 10),
    _NqaVplsMTraceHistoryIGMPSnpgEnable_Type()
)
nqaVplsMTraceHistoryIGMPSnpgEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryIGMPSnpgEnable.setStatus("current")
_NqaVplsMTraceHistoryIGMPProxyEnable_Type = EnableValue
_NqaVplsMTraceHistoryIGMPProxyEnable_Object = MibTableColumn
nqaVplsMTraceHistoryIGMPProxyEnable = _NqaVplsMTraceHistoryIGMPProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 11),
    _NqaVplsMTraceHistoryIGMPProxyEnable_Type()
)
nqaVplsMTraceHistoryIGMPProxyEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryIGMPProxyEnable.setStatus("current")
_NqaVplsMTraceHistoryIGMPRouterPortLearningEnable_Type = EnableValue
_NqaVplsMTraceHistoryIGMPRouterPortLearningEnable_Object = MibTableColumn
nqaVplsMTraceHistoryIGMPRouterPortLearningEnable = _NqaVplsMTraceHistoryIGMPRouterPortLearningEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 12),
    _NqaVplsMTraceHistoryIGMPRouterPortLearningEnable_Type()
)
nqaVplsMTraceHistoryIGMPRouterPortLearningEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryIGMPRouterPortLearningEnable.setStatus("current")
_NqaVplsMTraceHistoryRequireRouterAlertEnable_Type = EnableValue
_NqaVplsMTraceHistoryRequireRouterAlertEnable_Object = MibTableColumn
nqaVplsMTraceHistoryRequireRouterAlertEnable = _NqaVplsMTraceHistoryRequireRouterAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 13),
    _NqaVplsMTraceHistoryRequireRouterAlertEnable_Type()
)
nqaVplsMTraceHistoryRequireRouterAlertEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryRequireRouterAlertEnable.setStatus("current")


class _NqaVplsMTraceHistoryForwardMode_Type(Integer32):
    """Custom type nqaVplsMTraceHistoryForwardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("mac", 1))
    )


_NqaVplsMTraceHistoryForwardMode_Type.__name__ = "Integer32"
_NqaVplsMTraceHistoryForwardMode_Object = MibTableColumn
nqaVplsMTraceHistoryForwardMode = _NqaVplsMTraceHistoryForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 14),
    _NqaVplsMTraceHistoryForwardMode_Type()
)
nqaVplsMTraceHistoryForwardMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryForwardMode.setStatus("current")
_NqaVplsMTraceHistoryHitFlag_Type = TruthValue
_NqaVplsMTraceHistoryHitFlag_Object = MibTableColumn
nqaVplsMTraceHistoryHitFlag = _NqaVplsMTraceHistoryHitFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 15),
    _NqaVplsMTraceHistoryHitFlag_Type()
)
nqaVplsMTraceHistoryHitFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryHitFlag.setStatus("current")
_NqaVplsMTraceHistoryPWExist_Type = TruthValue
_NqaVplsMTraceHistoryPWExist_Object = MibTableColumn
nqaVplsMTraceHistoryPWExist = _NqaVplsMTraceHistoryPWExist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 16),
    _NqaVplsMTraceHistoryPWExist_Type()
)
nqaVplsMTraceHistoryPWExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryPWExist.setStatus("current")


class _NqaVplsMTraceHistoryGroupPolicy_Type(Integer32):
    """Custom type nqaVplsMTraceHistoryGroupPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_NqaVplsMTraceHistoryGroupPolicy_Type.__name__ = "Integer32"
_NqaVplsMTraceHistoryGroupPolicy_Object = MibTableColumn
nqaVplsMTraceHistoryGroupPolicy = _NqaVplsMTraceHistoryGroupPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 17),
    _NqaVplsMTraceHistoryGroupPolicy_Type()
)
nqaVplsMTraceHistoryGroupPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryGroupPolicy.setStatus("current")


class _NqaVplsMTraceHistoryCACExist_Type(Integer32):
    """Custom type nqaVplsMTraceHistoryCACExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NqaVplsMTraceHistoryCACExist_Type.__name__ = "Integer32"
_NqaVplsMTraceHistoryCACExist_Object = MibTableColumn
nqaVplsMTraceHistoryCACExist = _NqaVplsMTraceHistoryCACExist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 18),
    _NqaVplsMTraceHistoryCACExist_Type()
)
nqaVplsMTraceHistoryCACExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryCACExist.setStatus("current")
_NqaVplsMTraceHistoryRcvQueryCount_Type = Gauge32
_NqaVplsMTraceHistoryRcvQueryCount_Object = MibTableColumn
nqaVplsMTraceHistoryRcvQueryCount = _NqaVplsMTraceHistoryRcvQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 19),
    _NqaVplsMTraceHistoryRcvQueryCount_Type()
)
nqaVplsMTraceHistoryRcvQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryRcvQueryCount.setStatus("current")
_NqaVplsMTraceHistoryRcvReportCount_Type = Gauge32
_NqaVplsMTraceHistoryRcvReportCount_Object = MibTableColumn
nqaVplsMTraceHistoryRcvReportCount = _NqaVplsMTraceHistoryRcvReportCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 20),
    _NqaVplsMTraceHistoryRcvReportCount_Type()
)
nqaVplsMTraceHistoryRcvReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryRcvReportCount.setStatus("current")
_NqaVplsMTraceHistoryRcvLeaveCount_Type = Gauge32
_NqaVplsMTraceHistoryRcvLeaveCount_Object = MibTableColumn
nqaVplsMTraceHistoryRcvLeaveCount = _NqaVplsMTraceHistoryRcvLeaveCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 21),
    _NqaVplsMTraceHistoryRcvLeaveCount_Type()
)
nqaVplsMTraceHistoryRcvLeaveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryRcvLeaveCount.setStatus("current")
_NqaVplsMTraceHistoryTimeStamp_Type = DateAndTime
_NqaVplsMTraceHistoryTimeStamp_Object = MibTableColumn
nqaVplsMTraceHistoryTimeStamp = _NqaVplsMTraceHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 22),
    _NqaVplsMTraceHistoryTimeStamp_Type()
)
nqaVplsMTraceHistoryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryTimeStamp.setStatus("current")
_NqaVplsMTraceHistoryCompletionTime_Type = Integer32
_NqaVplsMTraceHistoryCompletionTime_Object = MibTableColumn
nqaVplsMTraceHistoryCompletionTime = _NqaVplsMTraceHistoryCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 23),
    _NqaVplsMTraceHistoryCompletionTime_Type()
)
nqaVplsMTraceHistoryCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryCompletionTime.setUnits("milliseconds")
_NqaVplsMTraceHistoryLastRC_Type = Integer32
_NqaVplsMTraceHistoryLastRC_Object = MibTableColumn
nqaVplsMTraceHistoryLastRC = _NqaVplsMTraceHistoryLastRC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 24),
    _NqaVplsMTraceHistoryLastRC_Type()
)
nqaVplsMTraceHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryLastRC.setStatus("current")
_NqaVplsMTraceHistoryLastRSC_Type = Integer32
_NqaVplsMTraceHistoryLastRSC_Object = MibTableColumn
nqaVplsMTraceHistoryLastRSC = _NqaVplsMTraceHistoryLastRSC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 25),
    _NqaVplsMTraceHistoryLastRSC_Type()
)
nqaVplsMTraceHistoryLastRSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryLastRSC.setStatus("current")


class _NqaVplsMTraceHistoryFinishState_Type(Integer32):
    """Custom type nqaVplsMTraceHistoryFinishState based on Integer32"""
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
        *(("busy", 4),
          ("disconnected", 6),
          ("drop", 3),
          ("noConnected", 7),
          ("overThreshold", 5),
          ("success", 1),
          ("timeout", 2))
    )


_NqaVplsMTraceHistoryFinishState_Type.__name__ = "Integer32"
_NqaVplsMTraceHistoryFinishState_Object = MibTableColumn
nqaVplsMTraceHistoryFinishState = _NqaVplsMTraceHistoryFinishState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 26),
    _NqaVplsMTraceHistoryFinishState_Type()
)
nqaVplsMTraceHistoryFinishState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistoryFinishState.setStatus("current")


class _NqaVplsMTraceHistorySuccessPathNode_Type(Integer32):
    """Custom type nqaVplsMTraceHistorySuccessPathNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notonPath", 2),
          ("onPath", 1))
    )


_NqaVplsMTraceHistorySuccessPathNode_Type.__name__ = "Integer32"
_NqaVplsMTraceHistorySuccessPathNode_Object = MibTableColumn
nqaVplsMTraceHistorySuccessPathNode = _NqaVplsMTraceHistorySuccessPathNode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 6, 1, 27),
    _NqaVplsMTraceHistorySuccessPathNode_Type()
)
nqaVplsMTraceHistorySuccessPathNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaVplsMTraceHistorySuccessPathNode.setStatus("current")
_NqaMacTraceHistoryTable_Object = MibTable
nqaMacTraceHistoryTable = _NqaMacTraceHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7)
)
if mibBuilder.loadTexts:
    nqaMacTraceHistoryTable.setStatus("current")
_NqaMacTraceHistoryEntry_Object = MibTableRow
nqaMacTraceHistoryEntry = _NqaMacTraceHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1)
)
nqaMacTraceHistoryEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaMacTraceHistoryIndex"),
    (0, "NQA-MIB", "nqaMacTraceHistoryReceiveOrder"),
)
if mibBuilder.loadTexts:
    nqaMacTraceHistoryEntry.setStatus("current")


class _NqaMacTraceHistoryIndex_Type(Integer32):
    """Custom type nqaMacTraceHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMacTraceHistoryIndex_Type.__name__ = "Integer32"
_NqaMacTraceHistoryIndex_Object = MibTableColumn
nqaMacTraceHistoryIndex = _NqaMacTraceHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 1),
    _NqaMacTraceHistoryIndex_Type()
)
nqaMacTraceHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryIndex.setStatus("current")


class _NqaMacTraceHistoryReceiveOrder_Type(Integer32):
    """Custom type nqaMacTraceHistoryReceiveOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMacTraceHistoryReceiveOrder_Type.__name__ = "Integer32"
_NqaMacTraceHistoryReceiveOrder_Object = MibTableColumn
nqaMacTraceHistoryReceiveOrder = _NqaMacTraceHistoryReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 2),
    _NqaMacTraceHistoryReceiveOrder_Type()
)
nqaMacTraceHistoryReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryReceiveOrder.setStatus("current")


class _NqaMacTraceHistoryTTL_Type(Integer32):
    """Custom type nqaMacTraceHistoryTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NqaMacTraceHistoryTTL_Type.__name__ = "Integer32"
_NqaMacTraceHistoryTTL_Object = MibTableColumn
nqaMacTraceHistoryTTL = _NqaMacTraceHistoryTTL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 3),
    _NqaMacTraceHistoryTTL_Type()
)
nqaMacTraceHistoryTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryTTL.setStatus("current")
_NqaMacTraceHistorySeqNumber_Type = Unsigned32
_NqaMacTraceHistorySeqNumber_Object = MibTableColumn
nqaMacTraceHistorySeqNumber = _NqaMacTraceHistorySeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 4),
    _NqaMacTraceHistorySeqNumber_Type()
)
nqaMacTraceHistorySeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistorySeqNumber.setStatus("current")
_NqaMacTraceHistoryCompletionTime_Type = Integer32
_NqaMacTraceHistoryCompletionTime_Object = MibTableColumn
nqaMacTraceHistoryCompletionTime = _NqaMacTraceHistoryCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 5),
    _NqaMacTraceHistoryCompletionTime_Type()
)
nqaMacTraceHistoryCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryCompletionTime.setUnits("milliseconds")
_NqaMacTraceHistoryForwarded_Type = TruthValue
_NqaMacTraceHistoryForwarded_Object = MibTableColumn
nqaMacTraceHistoryForwarded = _NqaMacTraceHistoryForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 6),
    _NqaMacTraceHistoryForwarded_Type()
)
nqaMacTraceHistoryForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryForwarded.setStatus("current")
_NqaMacTraceHistoryTerminalMep_Type = TruthValue
_NqaMacTraceHistoryTerminalMep_Object = MibTableColumn
nqaMacTraceHistoryTerminalMep = _NqaMacTraceHistoryTerminalMep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 7),
    _NqaMacTraceHistoryTerminalMep_Type()
)
nqaMacTraceHistoryTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryTerminalMep.setStatus("current")
_NqaMacTraceHistoryRelayAction_Type = HWDot1agCfmRelayActionFieldValue
_NqaMacTraceHistoryRelayAction_Object = MibTableColumn
nqaMacTraceHistoryRelayAction = _NqaMacTraceHistoryRelayAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 8),
    _NqaMacTraceHistoryRelayAction_Type()
)
nqaMacTraceHistoryRelayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryRelayAction.setStatus("current")
_NqaMacTraceHistoryIngressAction_Type = HWDot1agCfmIngressActionFieldValue
_NqaMacTraceHistoryIngressAction_Object = MibTableColumn
nqaMacTraceHistoryIngressAction = _NqaMacTraceHistoryIngressAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 9),
    _NqaMacTraceHistoryIngressAction_Type()
)
nqaMacTraceHistoryIngressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryIngressAction.setStatus("current")
_NqaMacTraceHistoryIngressMac_Type = MacAddress
_NqaMacTraceHistoryIngressMac_Object = MibTableColumn
nqaMacTraceHistoryIngressMac = _NqaMacTraceHistoryIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 10),
    _NqaMacTraceHistoryIngressMac_Type()
)
nqaMacTraceHistoryIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryIngressMac.setStatus("current")
_NqaMacTraceHistoryIngressIfName_Type = OctetString
_NqaMacTraceHistoryIngressIfName_Object = MibTableColumn
nqaMacTraceHistoryIngressIfName = _NqaMacTraceHistoryIngressIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 11),
    _NqaMacTraceHistoryIngressIfName_Type()
)
nqaMacTraceHistoryIngressIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryIngressIfName.setStatus("current")
_NqaMacTraceHistoryEgressAction_Type = HWDot1agCfmEgressActionFieldValue
_NqaMacTraceHistoryEgressAction_Object = MibTableColumn
nqaMacTraceHistoryEgressAction = _NqaMacTraceHistoryEgressAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 12),
    _NqaMacTraceHistoryEgressAction_Type()
)
nqaMacTraceHistoryEgressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryEgressAction.setStatus("current")
_NqaMacTraceHistoryEgressMac_Type = MacAddress
_NqaMacTraceHistoryEgressMac_Object = MibTableColumn
nqaMacTraceHistoryEgressMac = _NqaMacTraceHistoryEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 13),
    _NqaMacTraceHistoryEgressMac_Type()
)
nqaMacTraceHistoryEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryEgressMac.setStatus("current")
_NqaMacTraceHistoryEgressIfName_Type = OctetString
_NqaMacTraceHistoryEgressIfName_Object = MibTableColumn
nqaMacTraceHistoryEgressIfName = _NqaMacTraceHistoryEgressIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 5, 7, 1, 14),
    _NqaMacTraceHistoryEgressIfName_Type()
)
nqaMacTraceHistoryEgressIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMacTraceHistoryEgressIfName.setStatus("current")
_NqaNotifications_ObjectIdentity = ObjectIdentity
nqaNotifications = _NqaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6)
)
_NqaConformance_ObjectIdentity = ObjectIdentity
nqaConformance = _NqaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7)
)
_NqaGroups_ObjectIdentity = ObjectIdentity
nqaGroups = _NqaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 1)
)
_NqaCompliances_ObjectIdentity = ObjectIdentity
nqaCompliances = _NqaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 2)
)
_NqaCollectStats_ObjectIdentity = ObjectIdentity
nqaCollectStats = _NqaCollectStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8)
)
_NqaJitterCollectStatsTable_Object = MibTable
nqaJitterCollectStatsTable = _NqaJitterCollectStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1)
)
if mibBuilder.loadTexts:
    nqaJitterCollectStatsTable.setStatus("current")
_NqaJitterCollectStatsEntry_Object = MibTableRow
nqaJitterCollectStatsEntry = _NqaJitterCollectStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1)
)
nqaJitterCollectStatsEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaJitterCollectStatsIndex"),
)
if mibBuilder.loadTexts:
    nqaJitterCollectStatsEntry.setStatus("current")


class _NqaJitterCollectStatsIndex_Type(Integer32):
    """Custom type nqaJitterCollectStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaJitterCollectStatsIndex_Type.__name__ = "Integer32"
_NqaJitterCollectStatsIndex_Object = MibTableColumn
nqaJitterCollectStatsIndex = _NqaJitterCollectStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 1),
    _NqaJitterCollectStatsIndex_Type()
)
nqaJitterCollectStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsIndex.setStatus("current")
_NqaJitterCollectStatsCompletions_Type = Counter32
_NqaJitterCollectStatsCompletions_Object = MibTableColumn
nqaJitterCollectStatsCompletions = _NqaJitterCollectStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 2),
    _NqaJitterCollectStatsCompletions_Type()
)
nqaJitterCollectStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsCompletions.setStatus("current")
_NqaJitterCollectStatsRTDOverThresholds_Type = Counter32
_NqaJitterCollectStatsRTDOverThresholds_Object = MibTableColumn
nqaJitterCollectStatsRTDOverThresholds = _NqaJitterCollectStatsRTDOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 3),
    _NqaJitterCollectStatsRTDOverThresholds_Type()
)
nqaJitterCollectStatsRTDOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsRTDOverThresholds.setStatus("current")
_NqaJitterCollectStatsOWDOverThresholdsSD_Type = Counter32
_NqaJitterCollectStatsOWDOverThresholdsSD_Object = MibTableColumn
nqaJitterCollectStatsOWDOverThresholdsSD = _NqaJitterCollectStatsOWDOverThresholdsSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 4),
    _NqaJitterCollectStatsOWDOverThresholdsSD_Type()
)
nqaJitterCollectStatsOWDOverThresholdsSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsOWDOverThresholdsSD.setStatus("current")
_NqaJitterCollectStatsOWDOverThresholdsDS_Type = Counter32
_NqaJitterCollectStatsOWDOverThresholdsDS_Object = MibTableColumn
nqaJitterCollectStatsOWDOverThresholdsDS = _NqaJitterCollectStatsOWDOverThresholdsDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 5),
    _NqaJitterCollectStatsOWDOverThresholdsDS_Type()
)
nqaJitterCollectStatsOWDOverThresholdsDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsOWDOverThresholdsDS.setStatus("current")
_NqaJitterCollectStatsNumOfRTT_Type = Counter32
_NqaJitterCollectStatsNumOfRTT_Object = MibTableColumn
nqaJitterCollectStatsNumOfRTT = _NqaJitterCollectStatsNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 6),
    _NqaJitterCollectStatsNumOfRTT_Type()
)
nqaJitterCollectStatsNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsNumOfRTT.setStatus("current")
_NqaJitterCollectStatsRTTSum_Type = Counter32
_NqaJitterCollectStatsRTTSum_Object = MibTableColumn
nqaJitterCollectStatsRTTSum = _NqaJitterCollectStatsRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 7),
    _NqaJitterCollectStatsRTTSum_Type()
)
nqaJitterCollectStatsRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsRTTSum.setStatus("current")
_NqaJitterCollectStatsRTTSum2Low_Type = Counter32
_NqaJitterCollectStatsRTTSum2Low_Object = MibTableColumn
nqaJitterCollectStatsRTTSum2Low = _NqaJitterCollectStatsRTTSum2Low_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 8),
    _NqaJitterCollectStatsRTTSum2Low_Type()
)
nqaJitterCollectStatsRTTSum2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsRTTSum2Low.setStatus("current")
_NqaJitterCollectStatsRTTSum2High_Type = Counter32
_NqaJitterCollectStatsRTTSum2High_Object = MibTableColumn
nqaJitterCollectStatsRTTSum2High = _NqaJitterCollectStatsRTTSum2High_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 9),
    _NqaJitterCollectStatsRTTSum2High_Type()
)
nqaJitterCollectStatsRTTSum2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsRTTSum2High.setStatus("current")
_NqaJitterCollectStatsRTTMin_Type = Gauge32
_NqaJitterCollectStatsRTTMin_Object = MibTableColumn
nqaJitterCollectStatsRTTMin = _NqaJitterCollectStatsRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 10),
    _NqaJitterCollectStatsRTTMin_Type()
)
nqaJitterCollectStatsRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsRTTMin.setStatus("current")
_NqaJitterCollectStatsRTTMax_Type = Gauge32
_NqaJitterCollectStatsRTTMax_Object = MibTableColumn
nqaJitterCollectStatsRTTMax = _NqaJitterCollectStatsRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 11),
    _NqaJitterCollectStatsRTTMax_Type()
)
nqaJitterCollectStatsRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsRTTMax.setStatus("current")
_NqaJitterCollectStatsMinOfPositivesSD_Type = Gauge32
_NqaJitterCollectStatsMinOfPositivesSD_Object = MibTableColumn
nqaJitterCollectStatsMinOfPositivesSD = _NqaJitterCollectStatsMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 12),
    _NqaJitterCollectStatsMinOfPositivesSD_Type()
)
nqaJitterCollectStatsMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMinOfPositivesSD.setStatus("current")
_NqaJitterCollectStatsMaxOfPositivesSD_Type = Gauge32
_NqaJitterCollectStatsMaxOfPositivesSD_Object = MibTableColumn
nqaJitterCollectStatsMaxOfPositivesSD = _NqaJitterCollectStatsMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 13),
    _NqaJitterCollectStatsMaxOfPositivesSD_Type()
)
nqaJitterCollectStatsMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMaxOfPositivesSD.setStatus("current")
_NqaJitterCollectStatsNumOfPositivesSD_Type = Counter32
_NqaJitterCollectStatsNumOfPositivesSD_Object = MibTableColumn
nqaJitterCollectStatsNumOfPositivesSD = _NqaJitterCollectStatsNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 14),
    _NqaJitterCollectStatsNumOfPositivesSD_Type()
)
nqaJitterCollectStatsNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsNumOfPositivesSD.setStatus("current")
_NqaJitterCollectStatsSumOfPositivesSD_Type = Counter32
_NqaJitterCollectStatsSumOfPositivesSD_Object = MibTableColumn
nqaJitterCollectStatsSumOfPositivesSD = _NqaJitterCollectStatsSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 15),
    _NqaJitterCollectStatsSumOfPositivesSD_Type()
)
nqaJitterCollectStatsSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSumOfPositivesSD.setStatus("current")
_NqaJitterCollectStatsSum2OfPositivesSDLow_Type = Counter32
_NqaJitterCollectStatsSum2OfPositivesSDLow_Object = MibTableColumn
nqaJitterCollectStatsSum2OfPositivesSDLow = _NqaJitterCollectStatsSum2OfPositivesSDLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 16),
    _NqaJitterCollectStatsSum2OfPositivesSDLow_Type()
)
nqaJitterCollectStatsSum2OfPositivesSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSum2OfPositivesSDLow.setStatus("current")
_NqaJitterCollectStatsSum2OfPositivesSDHigh_Type = Counter32
_NqaJitterCollectStatsSum2OfPositivesSDHigh_Object = MibTableColumn
nqaJitterCollectStatsSum2OfPositivesSDHigh = _NqaJitterCollectStatsSum2OfPositivesSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 17),
    _NqaJitterCollectStatsSum2OfPositivesSDHigh_Type()
)
nqaJitterCollectStatsSum2OfPositivesSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSum2OfPositivesSDHigh.setStatus("current")
_NqaJitterCollectStatsMinOfNegativesSD_Type = Gauge32
_NqaJitterCollectStatsMinOfNegativesSD_Object = MibTableColumn
nqaJitterCollectStatsMinOfNegativesSD = _NqaJitterCollectStatsMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 18),
    _NqaJitterCollectStatsMinOfNegativesSD_Type()
)
nqaJitterCollectStatsMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMinOfNegativesSD.setStatus("current")
_NqaJitterCollectStatsMaxOfNegativesSD_Type = Gauge32
_NqaJitterCollectStatsMaxOfNegativesSD_Object = MibTableColumn
nqaJitterCollectStatsMaxOfNegativesSD = _NqaJitterCollectStatsMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 19),
    _NqaJitterCollectStatsMaxOfNegativesSD_Type()
)
nqaJitterCollectStatsMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMaxOfNegativesSD.setStatus("current")
_NqaJitterCollectStatsNumOfNegativesSD_Type = Counter32
_NqaJitterCollectStatsNumOfNegativesSD_Object = MibTableColumn
nqaJitterCollectStatsNumOfNegativesSD = _NqaJitterCollectStatsNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 20),
    _NqaJitterCollectStatsNumOfNegativesSD_Type()
)
nqaJitterCollectStatsNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsNumOfNegativesSD.setStatus("current")
_NqaJitterCollectStatsSumOfNegativesSD_Type = Counter32
_NqaJitterCollectStatsSumOfNegativesSD_Object = MibTableColumn
nqaJitterCollectStatsSumOfNegativesSD = _NqaJitterCollectStatsSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 21),
    _NqaJitterCollectStatsSumOfNegativesSD_Type()
)
nqaJitterCollectStatsSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSumOfNegativesSD.setStatus("current")
_NqaJitterCollectStatsSum2OfNegativesSDLow_Type = Counter32
_NqaJitterCollectStatsSum2OfNegativesSDLow_Object = MibTableColumn
nqaJitterCollectStatsSum2OfNegativesSDLow = _NqaJitterCollectStatsSum2OfNegativesSDLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 22),
    _NqaJitterCollectStatsSum2OfNegativesSDLow_Type()
)
nqaJitterCollectStatsSum2OfNegativesSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSum2OfNegativesSDLow.setStatus("current")
_NqaJitterCollectStatsSum2OfNegativesSDHigh_Type = Counter32
_NqaJitterCollectStatsSum2OfNegativesSDHigh_Object = MibTableColumn
nqaJitterCollectStatsSum2OfNegativesSDHigh = _NqaJitterCollectStatsSum2OfNegativesSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 23),
    _NqaJitterCollectStatsSum2OfNegativesSDHigh_Type()
)
nqaJitterCollectStatsSum2OfNegativesSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSum2OfNegativesSDHigh.setStatus("current")
_NqaJitterCollectStatsMinOfPositivesDS_Type = Gauge32
_NqaJitterCollectStatsMinOfPositivesDS_Object = MibTableColumn
nqaJitterCollectStatsMinOfPositivesDS = _NqaJitterCollectStatsMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 24),
    _NqaJitterCollectStatsMinOfPositivesDS_Type()
)
nqaJitterCollectStatsMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMinOfPositivesDS.setStatus("current")
_NqaJitterCollectStatsMaxOfPositivesDS_Type = Gauge32
_NqaJitterCollectStatsMaxOfPositivesDS_Object = MibTableColumn
nqaJitterCollectStatsMaxOfPositivesDS = _NqaJitterCollectStatsMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 25),
    _NqaJitterCollectStatsMaxOfPositivesDS_Type()
)
nqaJitterCollectStatsMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMaxOfPositivesDS.setStatus("current")
_NqaJitterCollectStatsNumOfPositivesDS_Type = Counter32
_NqaJitterCollectStatsNumOfPositivesDS_Object = MibTableColumn
nqaJitterCollectStatsNumOfPositivesDS = _NqaJitterCollectStatsNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 26),
    _NqaJitterCollectStatsNumOfPositivesDS_Type()
)
nqaJitterCollectStatsNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsNumOfPositivesDS.setStatus("current")
_NqaJitterCollectStatsSumOfPositivesDS_Type = Counter32
_NqaJitterCollectStatsSumOfPositivesDS_Object = MibTableColumn
nqaJitterCollectStatsSumOfPositivesDS = _NqaJitterCollectStatsSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 27),
    _NqaJitterCollectStatsSumOfPositivesDS_Type()
)
nqaJitterCollectStatsSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSumOfPositivesDS.setStatus("current")
_NqaJitterCollectStatsSum2OfPositivesDSLow_Type = Counter32
_NqaJitterCollectStatsSum2OfPositivesDSLow_Object = MibTableColumn
nqaJitterCollectStatsSum2OfPositivesDSLow = _NqaJitterCollectStatsSum2OfPositivesDSLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 28),
    _NqaJitterCollectStatsSum2OfPositivesDSLow_Type()
)
nqaJitterCollectStatsSum2OfPositivesDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSum2OfPositivesDSLow.setStatus("current")
_NqaJitterCollectStatsSum2OfPositivesDSHigh_Type = Counter32
_NqaJitterCollectStatsSum2OfPositivesDSHigh_Object = MibTableColumn
nqaJitterCollectStatsSum2OfPositivesDSHigh = _NqaJitterCollectStatsSum2OfPositivesDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 29),
    _NqaJitterCollectStatsSum2OfPositivesDSHigh_Type()
)
nqaJitterCollectStatsSum2OfPositivesDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSum2OfPositivesDSHigh.setStatus("current")
_NqaJitterCollectStatsMinOfNegativesDS_Type = Gauge32
_NqaJitterCollectStatsMinOfNegativesDS_Object = MibTableColumn
nqaJitterCollectStatsMinOfNegativesDS = _NqaJitterCollectStatsMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 30),
    _NqaJitterCollectStatsMinOfNegativesDS_Type()
)
nqaJitterCollectStatsMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMinOfNegativesDS.setStatus("current")
_NqaJitterCollectStatsMaxOfNegativesDS_Type = Gauge32
_NqaJitterCollectStatsMaxOfNegativesDS_Object = MibTableColumn
nqaJitterCollectStatsMaxOfNegativesDS = _NqaJitterCollectStatsMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 31),
    _NqaJitterCollectStatsMaxOfNegativesDS_Type()
)
nqaJitterCollectStatsMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMaxOfNegativesDS.setStatus("current")
_NqaJitterCollectStatsNumOfNegativesDS_Type = Counter32
_NqaJitterCollectStatsNumOfNegativesDS_Object = MibTableColumn
nqaJitterCollectStatsNumOfNegativesDS = _NqaJitterCollectStatsNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 32),
    _NqaJitterCollectStatsNumOfNegativesDS_Type()
)
nqaJitterCollectStatsNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsNumOfNegativesDS.setStatus("current")
_NqaJitterCollectStatsSumOfNegativesDS_Type = Counter32
_NqaJitterCollectStatsSumOfNegativesDS_Object = MibTableColumn
nqaJitterCollectStatsSumOfNegativesDS = _NqaJitterCollectStatsSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 33),
    _NqaJitterCollectStatsSumOfNegativesDS_Type()
)
nqaJitterCollectStatsSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSumOfNegativesDS.setStatus("current")
_NqaJitterCollectStatsSum2OfNegativesDSLow_Type = Counter32
_NqaJitterCollectStatsSum2OfNegativesDSLow_Object = MibTableColumn
nqaJitterCollectStatsSum2OfNegativesDSLow = _NqaJitterCollectStatsSum2OfNegativesDSLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 34),
    _NqaJitterCollectStatsSum2OfNegativesDSLow_Type()
)
nqaJitterCollectStatsSum2OfNegativesDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSum2OfNegativesDSLow.setStatus("current")
_NqaJitterCollectStatsSum2OfNegativesDSHigh_Type = Counter32
_NqaJitterCollectStatsSum2OfNegativesDSHigh_Object = MibTableColumn
nqaJitterCollectStatsSum2OfNegativesDSHigh = _NqaJitterCollectStatsSum2OfNegativesDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 35),
    _NqaJitterCollectStatsSum2OfNegativesDSHigh_Type()
)
nqaJitterCollectStatsSum2OfNegativesDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSum2OfNegativesDSHigh.setStatus("current")
_NqaJitterCollectStatsMaxDelaySD_Type = Gauge32
_NqaJitterCollectStatsMaxDelaySD_Object = MibTableColumn
nqaJitterCollectStatsMaxDelaySD = _NqaJitterCollectStatsMaxDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 36),
    _NqaJitterCollectStatsMaxDelaySD_Type()
)
nqaJitterCollectStatsMaxDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMaxDelaySD.setStatus("current")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMaxDelaySD.setUnits("milliseconds")
_NqaJitterCollectStatsMaxDelayDS_Type = Gauge32
_NqaJitterCollectStatsMaxDelayDS_Object = MibTableColumn
nqaJitterCollectStatsMaxDelayDS = _NqaJitterCollectStatsMaxDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 37),
    _NqaJitterCollectStatsMaxDelayDS_Type()
)
nqaJitterCollectStatsMaxDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMaxDelayDS.setStatus("current")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMaxDelayDS.setUnits("milliseconds")
_NqaJitterCollectStatsNumOfOWD_Type = Counter32
_NqaJitterCollectStatsNumOfOWD_Object = MibTableColumn
nqaJitterCollectStatsNumOfOWD = _NqaJitterCollectStatsNumOfOWD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 38),
    _NqaJitterCollectStatsNumOfOWD_Type()
)
nqaJitterCollectStatsNumOfOWD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsNumOfOWD.setStatus("current")
_NqaJitterCollectStatsOWSumSD_Type = Counter32
_NqaJitterCollectStatsOWSumSD_Object = MibTableColumn
nqaJitterCollectStatsOWSumSD = _NqaJitterCollectStatsOWSumSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 39),
    _NqaJitterCollectStatsOWSumSD_Type()
)
nqaJitterCollectStatsOWSumSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsOWSumSD.setStatus("current")
_NqaJitterCollectStatsOWSumDS_Type = Counter32
_NqaJitterCollectStatsOWSumDS_Object = MibTableColumn
nqaJitterCollectStatsOWSumDS = _NqaJitterCollectStatsOWSumDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 40),
    _NqaJitterCollectStatsOWSumDS_Type()
)
nqaJitterCollectStatsOWSumDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsOWSumDS.setStatus("current")
_NqaJitterCollectStatsPacketLossSD_Type = Counter32
_NqaJitterCollectStatsPacketLossSD_Object = MibTableColumn
nqaJitterCollectStatsPacketLossSD = _NqaJitterCollectStatsPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 41),
    _NqaJitterCollectStatsPacketLossSD_Type()
)
nqaJitterCollectStatsPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsPacketLossSD.setStatus("current")
_NqaJitterCollectStatsPacketLossDS_Type = Counter32
_NqaJitterCollectStatsPacketLossDS_Object = MibTableColumn
nqaJitterCollectStatsPacketLossDS = _NqaJitterCollectStatsPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 42),
    _NqaJitterCollectStatsPacketLossDS_Type()
)
nqaJitterCollectStatsPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsPacketLossDS.setStatus("current")
_NqaJitterCollectStatsPacketLossUnknown_Type = Counter32
_NqaJitterCollectStatsPacketLossUnknown_Object = MibTableColumn
nqaJitterCollectStatsPacketLossUnknown = _NqaJitterCollectStatsPacketLossUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 43),
    _NqaJitterCollectStatsPacketLossUnknown_Type()
)
nqaJitterCollectStatsPacketLossUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsPacketLossUnknown.setStatus("current")
_NqaJitterCollectStatsPacketOutOfSequences_Type = Counter32
_NqaJitterCollectStatsPacketOutOfSequences_Object = MibTableColumn
nqaJitterCollectStatsPacketOutOfSequences = _NqaJitterCollectStatsPacketOutOfSequences_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 44),
    _NqaJitterCollectStatsPacketOutOfSequences_Type()
)
nqaJitterCollectStatsPacketOutOfSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsPacketOutOfSequences.setStatus("current")
_NqaJitterCollectStatsPacketLossRatio_Type = Gauge32
_NqaJitterCollectStatsPacketLossRatio_Object = MibTableColumn
nqaJitterCollectStatsPacketLossRatio = _NqaJitterCollectStatsPacketLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 45),
    _NqaJitterCollectStatsPacketLossRatio_Type()
)
nqaJitterCollectStatsPacketLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsPacketLossRatio.setStatus("current")
_NqaJitterCollectStatsErrors_Type = Counter32
_NqaJitterCollectStatsErrors_Object = MibTableColumn
nqaJitterCollectStatsErrors = _NqaJitterCollectStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 46),
    _NqaJitterCollectStatsErrors_Type()
)
nqaJitterCollectStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsErrors.setStatus("current")
_NqaJitterCollectStatsBusies_Type = Counter32
_NqaJitterCollectStatsBusies_Object = MibTableColumn
nqaJitterCollectStatsBusies = _NqaJitterCollectStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 47),
    _NqaJitterCollectStatsBusies_Type()
)
nqaJitterCollectStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsBusies.setStatus("current")
_NqaJitterCollectStatsTimeouts_Type = Counter32
_NqaJitterCollectStatsTimeouts_Object = MibTableColumn
nqaJitterCollectStatsTimeouts = _NqaJitterCollectStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 48),
    _NqaJitterCollectStatsTimeouts_Type()
)
nqaJitterCollectStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsTimeouts.setStatus("current")
_NqaJitterCollectStatsProbeResponses_Type = Counter32
_NqaJitterCollectStatsProbeResponses_Object = MibTableColumn
nqaJitterCollectStatsProbeResponses = _NqaJitterCollectStatsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 49),
    _NqaJitterCollectStatsProbeResponses_Type()
)
nqaJitterCollectStatsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsProbeResponses.setStatus("current")
_NqaJitterCollectStatsSentProbes_Type = Counter32
_NqaJitterCollectStatsSentProbes_Object = MibTableColumn
nqaJitterCollectStatsSentProbes = _NqaJitterCollectStatsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 50),
    _NqaJitterCollectStatsSentProbes_Type()
)
nqaJitterCollectStatsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsSentProbes.setStatus("current")
_NqaJitterCollectStatsDrops_Type = Counter32
_NqaJitterCollectStatsDrops_Object = MibTableColumn
nqaJitterCollectStatsDrops = _NqaJitterCollectStatsDrops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 51),
    _NqaJitterCollectStatsDrops_Type()
)
nqaJitterCollectStatsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsDrops.setStatus("current")
_NqaJitterCollectStatsRTTAvg_Type = Gauge32
_NqaJitterCollectStatsRTTAvg_Object = MibTableColumn
nqaJitterCollectStatsRTTAvg = _NqaJitterCollectStatsRTTAvg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 52),
    _NqaJitterCollectStatsRTTAvg_Type()
)
nqaJitterCollectStatsRTTAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsRTTAvg.setStatus("current")
_NqaJitterCollectStatsAvgJitter_Type = Gauge32
_NqaJitterCollectStatsAvgJitter_Object = MibTableColumn
nqaJitterCollectStatsAvgJitter = _NqaJitterCollectStatsAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 53),
    _NqaJitterCollectStatsAvgJitter_Type()
)
nqaJitterCollectStatsAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsAvgJitter.setStatus("current")
_NqaJitterCollectStatsAvgJitterSD_Type = Gauge32
_NqaJitterCollectStatsAvgJitterSD_Object = MibTableColumn
nqaJitterCollectStatsAvgJitterSD = _NqaJitterCollectStatsAvgJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 54),
    _NqaJitterCollectStatsAvgJitterSD_Type()
)
nqaJitterCollectStatsAvgJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsAvgJitterSD.setStatus("current")
_NqaJitterCollectStatsAvgJitterDS_Type = Gauge32
_NqaJitterCollectStatsAvgJitterDS_Object = MibTableColumn
nqaJitterCollectStatsAvgJitterDS = _NqaJitterCollectStatsAvgJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 55),
    _NqaJitterCollectStatsAvgJitterDS_Type()
)
nqaJitterCollectStatsAvgJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsAvgJitterDS.setStatus("current")
_NqaJitterCollectStatsJitterOut_Type = OctetString
_NqaJitterCollectStatsJitterOut_Object = MibTableColumn
nqaJitterCollectStatsJitterOut = _NqaJitterCollectStatsJitterOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 56),
    _NqaJitterCollectStatsJitterOut_Type()
)
nqaJitterCollectStatsJitterOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsJitterOut.setStatus("current")
_NqaJitterCollectStatsJitterIn_Type = OctetString
_NqaJitterCollectStatsJitterIn_Object = MibTableColumn
nqaJitterCollectStatsJitterIn = _NqaJitterCollectStatsJitterIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 57),
    _NqaJitterCollectStatsJitterIn_Type()
)
nqaJitterCollectStatsJitterIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsJitterIn.setStatus("current")
_NqaJitterCollectStatsMinDelaySD_Type = Gauge32
_NqaJitterCollectStatsMinDelaySD_Object = MibTableColumn
nqaJitterCollectStatsMinDelaySD = _NqaJitterCollectStatsMinDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 58),
    _NqaJitterCollectStatsMinDelaySD_Type()
)
nqaJitterCollectStatsMinDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMinDelaySD.setStatus("current")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMinDelaySD.setUnits("milliseconds")
_NqaJitterCollectStatsMinDelayDS_Type = Gauge32
_NqaJitterCollectStatsMinDelayDS_Object = MibTableColumn
nqaJitterCollectStatsMinDelayDS = _NqaJitterCollectStatsMinDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 59),
    _NqaJitterCollectStatsMinDelayDS_Type()
)
nqaJitterCollectStatsMinDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMinDelayDS.setStatus("current")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsMinDelayDS.setUnits("milliseconds")
_NqaJitterCollectStatsAvgDelaySD_Type = Gauge32
_NqaJitterCollectStatsAvgDelaySD_Object = MibTableColumn
nqaJitterCollectStatsAvgDelaySD = _NqaJitterCollectStatsAvgDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 60),
    _NqaJitterCollectStatsAvgDelaySD_Type()
)
nqaJitterCollectStatsAvgDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsAvgDelaySD.setStatus("current")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsAvgDelaySD.setUnits("milliseconds")
_NqaJitterCollectStatsAvgDelayDS_Type = Gauge32
_NqaJitterCollectStatsAvgDelayDS_Object = MibTableColumn
nqaJitterCollectStatsAvgDelayDS = _NqaJitterCollectStatsAvgDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 61),
    _NqaJitterCollectStatsAvgDelayDS_Type()
)
nqaJitterCollectStatsAvgDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsAvgDelayDS.setStatus("current")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsAvgDelayDS.setUnits("milliseconds")
_NqaJitterCollectStatsPktRewriteNum_Type = Counter32
_NqaJitterCollectStatsPktRewriteNum_Object = MibTableColumn
nqaJitterCollectStatsPktRewriteNum = _NqaJitterCollectStatsPktRewriteNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 62),
    _NqaJitterCollectStatsPktRewriteNum_Type()
)
nqaJitterCollectStatsPktRewriteNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsPktRewriteNum.setStatus("current")
_NqaJitterCollectStatsPktRewriteRatio_Type = Gauge32
_NqaJitterCollectStatsPktRewriteRatio_Object = MibTableColumn
nqaJitterCollectStatsPktRewriteRatio = _NqaJitterCollectStatsPktRewriteRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 63),
    _NqaJitterCollectStatsPktRewriteRatio_Type()
)
nqaJitterCollectStatsPktRewriteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsPktRewriteRatio.setStatus("current")
_NqaJitterCollectStatsPktDisorderNum_Type = Counter32
_NqaJitterCollectStatsPktDisorderNum_Object = MibTableColumn
nqaJitterCollectStatsPktDisorderNum = _NqaJitterCollectStatsPktDisorderNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 64),
    _NqaJitterCollectStatsPktDisorderNum_Type()
)
nqaJitterCollectStatsPktDisorderNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsPktDisorderNum.setStatus("current")
_NqaJitterCollectStatsPktDisorderRatio_Type = Gauge32
_NqaJitterCollectStatsPktDisorderRatio_Object = MibTableColumn
nqaJitterCollectStatsPktDisorderRatio = _NqaJitterCollectStatsPktDisorderRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 65),
    _NqaJitterCollectStatsPktDisorderRatio_Type()
)
nqaJitterCollectStatsPktDisorderRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsPktDisorderRatio.setStatus("current")
_NqaJitterCollectStatsFragPktDisorderNum_Type = Counter32
_NqaJitterCollectStatsFragPktDisorderNum_Object = MibTableColumn
nqaJitterCollectStatsFragPktDisorderNum = _NqaJitterCollectStatsFragPktDisorderNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 66),
    _NqaJitterCollectStatsFragPktDisorderNum_Type()
)
nqaJitterCollectStatsFragPktDisorderNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsFragPktDisorderNum.setStatus("current")
_NqaJitterCollectStatsFragPktDisorderRatio_Type = Gauge32
_NqaJitterCollectStatsFragPktDisorderRatio_Object = MibTableColumn
nqaJitterCollectStatsFragPktDisorderRatio = _NqaJitterCollectStatsFragPktDisorderRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 8, 1, 1, 67),
    _NqaJitterCollectStatsFragPktDisorderRatio_Type()
)
nqaJitterCollectStatsFragPktDisorderRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaJitterCollectStatsFragPktDisorderRatio.setStatus("current")
_NqaAlarm_ObjectIdentity = ObjectIdentity
nqaAlarm = _NqaAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9)
)


class _NqaMaxAlarmNum_Type(Integer32):
    """Custom type nqaMaxAlarmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMaxAlarmNum_Type.__name__ = "Integer32"
_NqaMaxAlarmNum_Object = MibScalar
nqaMaxAlarmNum = _NqaMaxAlarmNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 1),
    _NqaMaxAlarmNum_Type()
)
nqaMaxAlarmNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMaxAlarmNum.setStatus("current")


class _NqaMaxEventNum_Type(Integer32):
    """Custom type nqaMaxEventNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NqaMaxEventNum_Type.__name__ = "Integer32"
_NqaMaxEventNum_Object = MibScalar
nqaMaxEventNum = _NqaMaxEventNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 2),
    _NqaMaxEventNum_Type()
)
nqaMaxEventNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaMaxEventNum.setStatus("current")
_NqaAlarmTable_Object = MibTable
nqaAlarmTable = _NqaAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3)
)
if mibBuilder.loadTexts:
    nqaAlarmTable.setStatus("current")
_NqaAlarmEntry_Object = MibTableRow
nqaAlarmEntry = _NqaAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1)
)
nqaAlarmEntry.setIndexNames(
    (0, "NQA-MIB", "nqaAdminCtrlOwnerIndex"),
    (0, "NQA-MIB", "nqaAdminCtrlTestName"),
    (0, "NQA-MIB", "nqaAlarmIndex"),
)
if mibBuilder.loadTexts:
    nqaAlarmEntry.setStatus("current")


class _NqaAlarmIndex_Type(Integer32):
    """Custom type nqaAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NqaAlarmIndex_Type.__name__ = "Integer32"
_NqaAlarmIndex_Object = MibTableColumn
nqaAlarmIndex = _NqaAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 1),
    _NqaAlarmIndex_Type()
)
nqaAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaAlarmIndex.setStatus("current")


class _NqaAlarmVariable_Type(Integer32):
    """Custom type nqaAlarmVariable based on Integer32"""
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
        *(("jitterDsAvg", 7),
          ("jitterRavg", 5),
          ("jitterSdAvg", 6),
          ("lostPacketRatio", 2),
          ("packetLossDs", 4),
          ("packetLossSd", 3),
          ("rttAvg", 1))
    )


_NqaAlarmVariable_Type.__name__ = "Integer32"
_NqaAlarmVariable_Object = MibTableColumn
nqaAlarmVariable = _NqaAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 11),
    _NqaAlarmVariable_Type()
)
nqaAlarmVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAlarmVariable.setStatus("current")


class _NqaAlarmSampleType_Type(Integer32):
    """Custom type nqaAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 2),
          ("delta", 1))
    )


_NqaAlarmSampleType_Type.__name__ = "Integer32"
_NqaAlarmSampleType_Object = MibTableColumn
nqaAlarmSampleType = _NqaAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 12),
    _NqaAlarmSampleType_Type()
)
nqaAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAlarmSampleType.setStatus("current")


class _NqaAlarmValue_Type(Integer32):
    """Custom type nqaAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NqaAlarmValue_Type.__name__ = "Integer32"
_NqaAlarmValue_Object = MibTableColumn
nqaAlarmValue = _NqaAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 13),
    _NqaAlarmValue_Type()
)
nqaAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaAlarmValue.setStatus("current")


class _NqaAlarmStartUpNqaAlarm_Type(Integer32):
    """Custom type nqaAlarmStartUpNqaAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1),
          ("risingOrFallingAlarm", 3))
    )


_NqaAlarmStartUpNqaAlarm_Type.__name__ = "Integer32"
_NqaAlarmStartUpNqaAlarm_Object = MibTableColumn
nqaAlarmStartUpNqaAlarm = _NqaAlarmStartUpNqaAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 14),
    _NqaAlarmStartUpNqaAlarm_Type()
)
nqaAlarmStartUpNqaAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAlarmStartUpNqaAlarm.setStatus("current")


class _NqaAlarmRisingThreshold_Type(Integer32):
    """Custom type nqaAlarmRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NqaAlarmRisingThreshold_Type.__name__ = "Integer32"
_NqaAlarmRisingThreshold_Object = MibTableColumn
nqaAlarmRisingThreshold = _NqaAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 15),
    _NqaAlarmRisingThreshold_Type()
)
nqaAlarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAlarmRisingThreshold.setStatus("current")


class _NqaAlarmFallingThreshold_Type(Integer32):
    """Custom type nqaAlarmFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NqaAlarmFallingThreshold_Type.__name__ = "Integer32"
_NqaAlarmFallingThreshold_Object = MibTableColumn
nqaAlarmFallingThreshold = _NqaAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 16),
    _NqaAlarmFallingThreshold_Type()
)
nqaAlarmFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAlarmFallingThreshold.setStatus("current")


class _NqaAlarmRisingEventIndex_Type(Integer32):
    """Custom type nqaAlarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NqaAlarmRisingEventIndex_Type.__name__ = "Integer32"
_NqaAlarmRisingEventIndex_Object = MibTableColumn
nqaAlarmRisingEventIndex = _NqaAlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 17),
    _NqaAlarmRisingEventIndex_Type()
)
nqaAlarmRisingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAlarmRisingEventIndex.setStatus("current")


class _NqaAlarmFallingEventIndex_Type(Integer32):
    """Custom type nqaAlarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NqaAlarmFallingEventIndex_Type.__name__ = "Integer32"
_NqaAlarmFallingEventIndex_Object = MibTableColumn
nqaAlarmFallingEventIndex = _NqaAlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 18),
    _NqaAlarmFallingEventIndex_Type()
)
nqaAlarmFallingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAlarmFallingEventIndex.setStatus("current")


class _NqaAlarmDescription_Type(OctetString):
    """Custom type nqaAlarmDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NqaAlarmDescription_Type.__name__ = "OctetString"
_NqaAlarmDescription_Object = MibTableColumn
nqaAlarmDescription = _NqaAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 19),
    _NqaAlarmDescription_Type()
)
nqaAlarmDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAlarmDescription.setStatus("current")
_NqaAlarmStatus_Type = RowStatus
_NqaAlarmStatus_Object = MibTableColumn
nqaAlarmStatus = _NqaAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 3, 1, 51),
    _NqaAlarmStatus_Type()
)
nqaAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaAlarmStatus.setStatus("current")
_NqaEventTable_Object = MibTable
nqaEventTable = _NqaEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 4)
)
if mibBuilder.loadTexts:
    nqaEventTable.setStatus("current")
_NqaEventEntry_Object = MibTableRow
nqaEventEntry = _NqaEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 4, 1)
)
nqaEventEntry.setIndexNames(
    (0, "NQA-MIB", "nqaEventIndex"),
)
if mibBuilder.loadTexts:
    nqaEventEntry.setStatus("current")


class _NqaEventIndex_Type(Integer32):
    """Custom type nqaEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NqaEventIndex_Type.__name__ = "Integer32"
_NqaEventIndex_Object = MibTableColumn
nqaEventIndex = _NqaEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 4, 1, 1),
    _NqaEventIndex_Type()
)
nqaEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nqaEventIndex.setStatus("current")


class _NqaEventType_Type(Integer32):
    """Custom type nqaEventType based on Integer32"""
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
        *(("linkage", 5),
          ("log", 2),
          ("logAndTrap", 4),
          ("none", 1),
          ("trap", 3))
    )


_NqaEventType_Type.__name__ = "Integer32"
_NqaEventType_Object = MibTableColumn
nqaEventType = _NqaEventType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 4, 1, 11),
    _NqaEventType_Type()
)
nqaEventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaEventType.setStatus("current")


class _NqaEventDescription_Type(OctetString):
    """Custom type nqaEventDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NqaEventDescription_Type.__name__ = "OctetString"
_NqaEventDescription_Object = MibTableColumn
nqaEventDescription = _NqaEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 4, 1, 12),
    _NqaEventDescription_Type()
)
nqaEventDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaEventDescription.setStatus("current")


class _NqaEventAdminName_Type(OctetString):
    """Custom type nqaEventAdminName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NqaEventAdminName_Type.__name__ = "OctetString"
_NqaEventAdminName_Object = MibTableColumn
nqaEventAdminName = _NqaEventAdminName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 4, 1, 13),
    _NqaEventAdminName_Type()
)
nqaEventAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaEventAdminName.setStatus("current")


class _NqaEventOperationTag_Type(OctetString):
    """Custom type nqaEventOperationTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NqaEventOperationTag_Type.__name__ = "OctetString"
_NqaEventOperationTag_Object = MibTableColumn
nqaEventOperationTag = _NqaEventOperationTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 4, 1, 14),
    _NqaEventOperationTag_Type()
)
nqaEventOperationTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaEventOperationTag.setStatus("current")
_NqaEventStatus_Type = RowStatus
_NqaEventStatus_Object = MibTableColumn
nqaEventStatus = _NqaEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 9, 4, 1, 51),
    _NqaEventStatus_Type()
)
nqaEventStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nqaEventStatus.setStatus("current")
_NqaSaveRecord_ObjectIdentity = ObjectIdentity
nqaSaveRecord = _NqaSaveRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10)
)
_NqaFtpSaveRecordEnable_Type = EnabledStatus
_NqaFtpSaveRecordEnable_Object = MibScalar
nqaFtpSaveRecordEnable = _NqaFtpSaveRecordEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10, 1),
    _NqaFtpSaveRecordEnable_Type()
)
nqaFtpSaveRecordEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordEnable.setStatus("current")
_NqaFtpSaveRecordIpAddr_Type = InetAddress
_NqaFtpSaveRecordIpAddr_Object = MibScalar
nqaFtpSaveRecordIpAddr = _NqaFtpSaveRecordIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10, 2),
    _NqaFtpSaveRecordIpAddr_Type()
)
nqaFtpSaveRecordIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordIpAddr.setStatus("current")


class _NqaFtpSaveRecordVrfName_Type(OctetString):
    """Custom type nqaFtpSaveRecordVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NqaFtpSaveRecordVrfName_Type.__name__ = "OctetString"
_NqaFtpSaveRecordVrfName_Object = MibScalar
nqaFtpSaveRecordVrfName = _NqaFtpSaveRecordVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10, 3),
    _NqaFtpSaveRecordVrfName_Type()
)
nqaFtpSaveRecordVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordVrfName.setStatus("current")


class _NqaFtpSaveRecordUserName_Type(OctetString):
    """Custom type nqaFtpSaveRecordUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NqaFtpSaveRecordUserName_Type.__name__ = "OctetString"
_NqaFtpSaveRecordUserName_Object = MibScalar
nqaFtpSaveRecordUserName = _NqaFtpSaveRecordUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10, 4),
    _NqaFtpSaveRecordUserName_Type()
)
nqaFtpSaveRecordUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordUserName.setStatus("current")


class _NqaFtpSaveRecordPassword_Type(OctetString):
    """Custom type nqaFtpSaveRecordPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NqaFtpSaveRecordPassword_Type.__name__ = "OctetString"
_NqaFtpSaveRecordPassword_Object = MibScalar
nqaFtpSaveRecordPassword = _NqaFtpSaveRecordPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10, 5),
    _NqaFtpSaveRecordPassword_Type()
)
nqaFtpSaveRecordPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordPassword.setStatus("current")


class _NqaFtpSaveRecordFileName_Type(OctetString):
    """Custom type nqaFtpSaveRecordFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_NqaFtpSaveRecordFileName_Type.__name__ = "OctetString"
_NqaFtpSaveRecordFileName_Object = MibScalar
nqaFtpSaveRecordFileName = _NqaFtpSaveRecordFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10, 6),
    _NqaFtpSaveRecordFileName_Type()
)
nqaFtpSaveRecordFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordFileName.setStatus("current")


class _NqaFtpSaveRecordItemNum_Type(Integer32):
    """Custom type nqaFtpSaveRecordItemNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 2147483647),
    )


_NqaFtpSaveRecordItemNum_Type.__name__ = "Integer32"
_NqaFtpSaveRecordItemNum_Object = MibScalar
nqaFtpSaveRecordItemNum = _NqaFtpSaveRecordItemNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10, 7),
    _NqaFtpSaveRecordItemNum_Type()
)
nqaFtpSaveRecordItemNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordItemNum.setStatus("current")


class _NqaFtpSaveRecordTime_Type(Integer32):
    """Custom type nqaFtpSaveRecordTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 43200),
    )


_NqaFtpSaveRecordTime_Type.__name__ = "Integer32"
_NqaFtpSaveRecordTime_Object = MibScalar
nqaFtpSaveRecordTime = _NqaFtpSaveRecordTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10, 8),
    _NqaFtpSaveRecordTime_Type()
)
nqaFtpSaveRecordTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordTime.setStatus("current")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordTime.setUnits("minutes")
_NqaFtpSaveRecordNotificationEnable_Type = EnabledStatus
_NqaFtpSaveRecordNotificationEnable_Object = MibScalar
nqaFtpSaveRecordNotificationEnable = _NqaFtpSaveRecordNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10, 9),
    _NqaFtpSaveRecordNotificationEnable_Type()
)
nqaFtpSaveRecordNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordNotificationEnable.setStatus("current")


class _NqaFtpSaveRecordLastFileName_Type(OctetString):
    """Custom type nqaFtpSaveRecordLastFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 220),
    )


_NqaFtpSaveRecordLastFileName_Type.__name__ = "OctetString"
_NqaFtpSaveRecordLastFileName_Object = MibScalar
nqaFtpSaveRecordLastFileName = _NqaFtpSaveRecordLastFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 10, 10),
    _NqaFtpSaveRecordLastFileName_Type()
)
nqaFtpSaveRecordLastFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nqaFtpSaveRecordLastFileName.setStatus("current")

# Managed Objects groups

nqaBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 1, 1)
)
nqaBaseGroup.setObjects(
      *(("NQA-MIB", "nqaVersion"),
        ("NQA-MIB", "nqaReset"),
        ("NQA-MIB", "nqaTimeOfLastSetError"),
        ("NQA-MIB", "nqaLastSetError"),
        ("NQA-MIB", "nqaEnable"),
        ("NQA-MIB", "nqaNumOfCurrentCtrlEntry"),
        ("NQA-MIB", "nqaMaxConcurrentRequests"),
        ("NQA-MIB", "nqaMaxNumOfRequests"),
        ("NQA-MIB", "nqaJitterVersion"),
        ("NQA-MIB", "nqaSupportTestType"),
        ("NQA-MIB", "nqaSupportServerType"))
)
if mibBuilder.loadTexts:
    nqaBaseGroup.setStatus("current")

nqaAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 1, 2)
)
nqaAdminGroup.setObjects(
      *(("NQA-MIB", "nqaAdminCtrlTag"),
        ("NQA-MIB", "nqaAdminCtrlType"),
        ("NQA-MIB", "nqaAdminCtrlFrequency"),
        ("NQA-MIB", "nqaAdminCtrlTimeOut"),
        ("NQA-MIB", "nqaAdminCtrlThreshold1"),
        ("NQA-MIB", "nqaAdminCtrlThreshold2"),
        ("NQA-MIB", "nqaAdminCtrlThreshold3"),
        ("NQA-MIB", "nqaAdminCtrlStatus"),
        ("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaAdminParaTargetPort"),
        ("NQA-MIB", "nqaAdminParaSourceAddressType"),
        ("NQA-MIB", "nqaAdminParaSourceAddress"),
        ("NQA-MIB", "nqaAdminParaSourcePort"),
        ("NQA-MIB", "nqaAdminParaMaxTtl"),
        ("NQA-MIB", "nqaAdminParaInitialTtl"),
        ("NQA-MIB", "nqaAdminParaStorageType"),
        ("NQA-MIB", "nqaAdminParaMaxFailures"),
        ("NQA-MIB", "nqaAdminParaDontFragment"),
        ("NQA-MIB", "nqaAdminParaDataSize"),
        ("NQA-MIB", "nqaAdminParaDataFill"),
        ("NQA-MIB", "nqaAdminParaIfIndex"),
        ("NQA-MIB", "nqaAdminParaByPassRouteTable"),
        ("NQA-MIB", "nqaAdminParaMiscOptions"),
        ("NQA-MIB", "nqaAdminParaProbeCount"),
        ("NQA-MIB", "nqaAdminParaTrapGeneration"),
        ("NQA-MIB", "nqaAdminParaTrapProbeFailureFilter"),
        ("NQA-MIB", "nqaAdminParaTrapTestFailureFilter"),
        ("NQA-MIB", "nqaAdminParaDSField"),
        ("NQA-MIB", "nqaAdminParaDnsServerAddressType"),
        ("NQA-MIB", "nqaAdminParaDnsServerAddress"),
        ("NQA-MIB", "nqaAdminParaOperation"),
        ("NQA-MIB", "nqaAdminParaHttpVersion"),
        ("NQA-MIB", "nqaAdminParaHttpOperationString"),
        ("NQA-MIB", "nqaAdminParaTestFailurePercent"),
        ("NQA-MIB", "nqaAdminParaFtpUserName"),
        ("NQA-MIB", "nqaAdminParaFtpPassword"),
        ("NQA-MIB", "nqaAdminParaFtpFilePath"),
        ("NQA-MIB", "nqaAdminParaFtpFileSize"),
        ("NQA-MIB", "nqaAdminParaInterval"),
        ("NQA-MIB", "nqaAdminParaNumPackets"),
        ("NQA-MIB", "nqaAdminParaVrfName"),
        ("NQA-MIB", "nqaAdminParaLspAddressType"),
        ("NQA-MIB", "nqaAdminParaLspAddressMask"),
        ("NQA-MIB", "nqaAdminParaLspIpAddress"),
        ("NQA-MIB", "nqaAdminParaLspPWE3VcId"),
        ("NQA-MIB", "nqaAdminParaLspPWE3Type"),
        ("NQA-MIB", "nqaAdminParaLspPWE3Option"),
        ("NQA-MIB", "nqaAdminParaLspPWE3RemoteVcId"),
        ("NQA-MIB", "nqaAdminParaLspPWE3RemoteAddress"),
        ("NQA-MIB", "nqaAdminParaLspExp"),
        ("NQA-MIB", "nqaAdminParaLspReplyMode"),
        ("NQA-MIB", "nqaAdminParaResultRowMax"),
        ("NQA-MIB", "nqaAdminParaHistoryRowMax"),
        ("NQA-MIB", "nqaAdminParaCreateHopsEntries"),
        ("NQA-MIB", "nqaAdminParaLspVCType"),
        ("NQA-MIB", "nqaAdminParaMTraceLastHopAddress"),
        ("NQA-MIB", "nqaAdminParaMTraceSourceAddress"),
        ("NQA-MIB", "nqaAdminParaMTraceGroupAddress"),
        ("NQA-MIB", "nqaAdminParaMTraceMaxTtl"),
        ("NQA-MIB", "nqaAdminParaMTraceSendMode"),
        ("NQA-MIB", "nqaAdminParaMTraceResponseTtl"),
        ("NQA-MIB", "nqaAdminParaMTraceResponseAddressType"),
        ("NQA-MIB", "nqaAdminParaMTraceResponseAddress"),
        ("NQA-MIB", "nqaAdminParaDistanceNodeType"),
        ("NQA-MIB", "nqaAdminParaMacAddress"),
        ("NQA-MIB", "nqaAdminParaRMepID"),
        ("NQA-MIB", "nqaAdminParaMDName"),
        ("NQA-MIB", "nqaAdminParaMAName"),
        ("NQA-MIB", "nqaAdminParaMacTunnelName"),
        ("NQA-MIB", "nqaAdminParaCodecType"),
        ("NQA-MIB", "nqaAdminParaIcpifAdvFactor"),
        ("NQA-MIB", "nqaAdminParaFtpMode"),
        ("NQA-MIB", "nqaScheduleStartType"),
        ("NQA-MIB", "nqaScheduleStartTime"),
        ("NQA-MIB", "nqaScheduleEndType"),
        ("NQA-MIB", "nqaScheduleEndTime"),
        ("NQA-MIB", "nqaScheduleAgeTime"),
        ("NQA-MIB", "nqaScheduleNumOfInitiations"),
        ("NQA-MIB", "nqaAdminParaIcmpJitterMode"),
        ("NQA-MIB", "nqaAdminParaPathMtuDiscoveryPathMtuMax"),
        ("NQA-MIB", "nqaAdminParaPathMtuStep"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaScheduleElapsedTime"),
        ("NQA-MIB", "nqaScheduleLastFinishIndex"),
        ("NQA-MIB", "nqaScheduleLastCollectIndex"),
        ("NQA-MIB", "nqaGroupStatusType"),
        ("NQA-MIB", "nqaGroupPeriod"),
        ("NQA-MIB", "nqaGroupLeaderOwnerIndex"),
        ("NQA-MIB", "nqaGroupLeaderTestName"),
        ("NQA-MIB", "nqaGroupMemberNum"),
        ("NQA-MIB", "nqaGroupMemberFree"),
        ("NQA-MIB", "nqaAdminParaHardwareBased"),
        ("NQA-MIB", "nqaAdminParaPppoeUserName"),
        ("NQA-MIB", "nqaAdminParaPppoePassword"),
        ("NQA-MIB", "nqaAdminParaPppoeVlanIf"),
        ("NQA-MIB", "nqaAdminParaPppoeAuthenticationMode"),
        ("NQA-MIB", "nqaAdminParaPppoeRedialUpTimes"),
        ("NQA-MIB", "nqaAdminParaPppoeInterval"),
        ("NQA-MIB", "nqaAdminParaVsiName"),
        ("NQA-MIB", "nqaAdminParaVlanId"),
        ("NQA-MIB", "nqaAdminParaLspTunnelType"),
        ("NQA-MIB", "nqaAdminParaLspNextHopAddress"),
        ("NQA-MIB", "nqaAdminParaLspVersion"),
        ("NQA-MIB", "nqaAdminParaRemoteAddressType"),
        ("NQA-MIB", "nqaAdminParaRemoteAddress"),
        ("NQA-MIB", "nqaAdminParaTimeUnit"),
        ("NQA-MIB", "nqaAdminExtPara1"),
        ("NQA-MIB", "nqaAdminExtPara2"),
        ("NQA-MIB", "nqaAdminExtPara3"),
        ("NQA-MIB", "nqaAdminExtPara4"),
        ("NQA-MIB", "nqaAdminExtPara5"),
        ("NQA-MIB", "nqaAdminExtPara6"),
        ("NQA-MIB", "nqaAdminExtPara7"),
        ("NQA-MIB", "nqaAdminExtPara8"),
        ("NQA-MIB", "nqaAdminExtPara9"),
        ("NQA-MIB", "nqaAdminExtPara10"),
        ("NQA-MIB", "nqaAdminExtPara11"),
        ("NQA-MIB", "nqaAdminExtPara12"),
        ("NQA-MIB", "nqaAdminExtPara13"),
        ("NQA-MIB", "nqaAdminExtPara14"),
        ("NQA-MIB", "nqaAdminExtPara15"),
        ("NQA-MIB", "nqaAdminExtPara16"),
        ("NQA-MIB", "nqaAdminExtPara17"),
        ("NQA-MIB", "nqaAdminExtPara18"),
        ("NQA-MIB", "nqaAdminExtPara19"),
        ("NQA-MIB", "nqaAdminExtPara20"),
        ("NQA-MIB", "nqaAdminExtPara21"),
        ("NQA-MIB", "nqaAdminExtPara22"),
        ("NQA-MIB", "nqaAdminExtPara23"),
        ("NQA-MIB", "nqaAdminExtPara24"),
        ("NQA-MIB", "nqaAdminExtPara25"),
        ("NQA-MIB", "nqaAdminExtPara26"),
        ("NQA-MIB", "nqaAdminExtPara27"),
        ("NQA-MIB", "nqaAdminExtPara28"),
        ("NQA-MIB", "nqaAdminExtPara29"),
        ("NQA-MIB", "nqaAdminExtPara30"),
        ("NQA-MIB", "nqaAdminExtPara31"),
        ("NQA-MIB", "nqaAdminExtPara32"),
        ("NQA-MIB", "nqaAdminExtPara33"),
        ("NQA-MIB", "nqaAdminExtPara34"),
        ("NQA-MIB", "nqaAdminExtPara35"),
        ("NQA-MIB", "nqaAdminExtPara36"),
        ("NQA-MIB", "nqaAdminExtPara37"),
        ("NQA-MIB", "nqaAdminExtPara38"),
        ("NQA-MIB", "nqaAdminExtPara39"),
        ("NQA-MIB", "nqaAdminExtPara40"),
        ("NQA-MIB", "nqaAdminExtPara41"),
        ("NQA-MIB", "nqaAdminExtPara42"),
        ("NQA-MIB", "nqaAdminExtPara43"),
        ("NQA-MIB", "nqaAdminExtPara44"),
        ("NQA-MIB", "nqaAdminExtPara45"),
        ("NQA-MIB", "nqaAdminExtPara46"),
        ("NQA-MIB", "nqaAdminExtPara47"),
        ("NQA-MIB", "nqaAdminExtPara48"),
        ("NQA-MIB", "nqaAdminExtPara49"),
        ("NQA-MIB", "nqaAdminExtPara50"))
)
if mibBuilder.loadTexts:
    nqaAdminGroup.setStatus("current")

nqaServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 1, 3)
)
nqaServerGroup.setObjects(
      *(("NQA-MIB", "nqaTcpServerAddressType"),
        ("NQA-MIB", "nqaTcpServerStatus"),
        ("NQA-MIB", "nqaUdpServerAddressType"),
        ("NQA-MIB", "nqaUdpServerStatus"),
        ("NQA-MIB", "nqaIcmpServerAddressType"),
        ("NQA-MIB", "nqaIcmpServerStatus"),
        ("NQA-MIB", "nqaServerEnable"))
)
if mibBuilder.loadTexts:
    nqaServerGroup.setStatus("current")

nqaStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 1, 4)
)
nqaStatsGroup.setObjects(
      *(("NQA-MIB", "nqaResultsCompletions"),
        ("NQA-MIB", "nqaResultsTestAttempts"),
        ("NQA-MIB", "nqaResultsCurHopCount"),
        ("NQA-MIB", "nqaResultsCurProbeCount"),
        ("NQA-MIB", "nqaResultsRTDOverThresholds"),
        ("NQA-MIB", "nqaResultsCompletionTimeMin"),
        ("NQA-MIB", "nqaResultsCompletionTimeMax"),
        ("NQA-MIB", "nqaResultsDisconnects"),
        ("NQA-MIB", "nqaResultsTimeouts"),
        ("NQA-MIB", "nqaResultsBusies"),
        ("NQA-MIB", "nqaResultsNoConnections"),
        ("NQA-MIB", "nqaResultsSequenceErrors"),
        ("NQA-MIB", "nqaResultsDrops"),
        ("NQA-MIB", "nqaResultsAddressType"),
        ("NQA-MIB", "nqaResultsAddress"),
        ("NQA-MIB", "nqaResultsProbeResponses"),
        ("NQA-MIB", "nqaResultsSentProbes"),
        ("NQA-MIB", "nqaResultsLastGoodProbe"),
        ("NQA-MIB", "nqaResultsLastGoodPath"),
        ("NQA-MIB", "nqaResultsTestFinished"),
        ("NQA-MIB", "nqaHTTPStatsCompletions"),
        ("NQA-MIB", "nqaHTTPStatsRTDOverThresholds"),
        ("NQA-MIB", "nqaHTTPStatsRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsRTTMin"),
        ("NQA-MIB", "nqaHTTPStatsRTTMax"),
        ("NQA-MIB", "nqaHTTPStatsDNSRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsDNSRTTMin"),
        ("NQA-MIB", "nqaHTTPStatsDNSRTTMax"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectRTTMin"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectRTTMax"),
        ("NQA-MIB", "nqaHTTPStatsTransactionRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsTransactionRTTMin"),
        ("NQA-MIB", "nqaHTTPStatsTransactionRTTMax"),
        ("NQA-MIB", "nqaHTTPStatsMessageBodyOctetsSum"),
        ("NQA-MIB", "nqaHTTPStatsDNSServerTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsTransactionTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsDNSQueryErrors"),
        ("NQA-MIB", "nqaHTTPStatsErrors"),
        ("NQA-MIB", "nqaHTTPStatsTcpConnErrors"),
        ("NQA-MIB", "nqaHTTPStatsProbeResponses"),
        ("NQA-MIB", "nqaHTTPStatsSendProbes"),
        ("NQA-MIB", "nqaHTTPStatsBusies"),
        ("NQA-MIB", "nqaHTTPStatsTestFinished"),
        ("NQA-MIB", "nqaJitterStatsCompletions"),
        ("NQA-MIB", "nqaJitterStatsRTDOverThresholds"),
        ("NQA-MIB", "nqaJitterStatsNumOfRTT"),
        ("NQA-MIB", "nqaJitterStatsRTTSum"),
        ("NQA-MIB", "nqaJitterStatsRTTSum2Low"),
        ("NQA-MIB", "nqaJitterStatsRTTSum2High"),
        ("NQA-MIB", "nqaJitterStatsRTTMin"),
        ("NQA-MIB", "nqaJitterStatsRTTMax"),
        ("NQA-MIB", "nqaJitterStatsMinOfPositivesSD"),
        ("NQA-MIB", "nqaJitterStatsMaxOfPositivesSD"),
        ("NQA-MIB", "nqaJitterStatsNumOfPositivesSD"),
        ("NQA-MIB", "nqaJitterStatsSumOfPositivesSD"),
        ("NQA-MIB", "nqaJitterStatsSum2OfPositivesSDLow"),
        ("NQA-MIB", "nqaJitterStatsSum2OfPositivesSDHigh"),
        ("NQA-MIB", "nqaJitterStatsMinOfNegativesSD"),
        ("NQA-MIB", "nqaJitterStatsMaxOfNegativesSD"),
        ("NQA-MIB", "nqaJitterStatsNumOfNegativesSD"),
        ("NQA-MIB", "nqaJitterStatsSumOfNegativesSD"),
        ("NQA-MIB", "nqaJitterStatsSum2OfNegativesSDLow"),
        ("NQA-MIB", "nqaJitterStatsSum2OfNegativesSDHigh"),
        ("NQA-MIB", "nqaJitterStatsMinOfPositivesDS"),
        ("NQA-MIB", "nqaJitterStatsMaxOfPositivesDS"),
        ("NQA-MIB", "nqaJitterStatsNumOfPositivesDS"),
        ("NQA-MIB", "nqaJitterStatsSumOfPositivesDS"),
        ("NQA-MIB", "nqaJitterStatsSum2OfPositivesDSLow"),
        ("NQA-MIB", "nqaJitterStatsSum2OfPositivesDSHigh"),
        ("NQA-MIB", "nqaJitterStatsMinOfNegativesDS"),
        ("NQA-MIB", "nqaJitterStatsMaxOfNegativesDS"),
        ("NQA-MIB", "nqaJitterStatsNumOfNegativesDS"),
        ("NQA-MIB", "nqaJitterStatsSumOfNegativesDS"),
        ("NQA-MIB", "nqaJitterStatsSum2OfNegativesDSLow"),
        ("NQA-MIB", "nqaJitterStatsSum2OfNegativesDSHigh"),
        ("NQA-MIB", "nqaJitterStatsPacketLossSD"),
        ("NQA-MIB", "nqaJitterStatsPacketLossDS"),
        ("NQA-MIB", "nqaJitterStatsPacketOutOfSequences"),
        ("NQA-MIB", "nqaJitterStatsErrors"),
        ("NQA-MIB", "nqaJitterStatsBusies"),
        ("NQA-MIB", "nqaJitterStatsTimeouts"),
        ("NQA-MIB", "nqaJitterStatsProbeResponses"),
        ("NQA-MIB", "nqaJitterStatsSentProbes"),
        ("NQA-MIB", "nqaJitterStatsDrops"),
        ("NQA-MIB", "nqaJitterStatsTestFinished"),
        ("NQA-MIB", "nqaJitterStatsMaxDelaySD"),
        ("NQA-MIB", "nqaJitterStatsMaxDelayDS"),
        ("NQA-MIB", "nqaJitterStatsRTTAvg"),
        ("NQA-MIB", "nqaJitterStatsPacketLossRatio"),
        ("NQA-MIB", "nqaJitterStatsAvgJitter"),
        ("NQA-MIB", "nqaJitterStatsAvgJitterSD"),
        ("NQA-MIB", "nqaJitterStatsAvgJitterDS"),
        ("NQA-MIB", "nqaJitterStatsJitterOut"),
        ("NQA-MIB", "nqaJitterStatsJitterIn"),
        ("NQA-MIB", "nqaJitterStatsOWDOverThresholdsSD"),
        ("NQA-MIB", "nqaJitterStatsOWDOverThresholdsDS"),
        ("NQA-MIB", "nqaJitterStatsPktLossUnknown"),
        ("NQA-MIB", "nqaJitterStatsNumOfOWD"),
        ("NQA-MIB", "nqaJitterStatsOWSumSD"),
        ("NQA-MIB", "nqaPathJitterStatsCompletions"),
        ("NQA-MIB", "nqaPathJitterStatsAddressType"),
        ("NQA-MIB", "nqaPathJitterStatsAddress"),
        ("NQA-MIB", "nqaPathJitterStatsRtdOverThresholds"),
        ("NQA-MIB", "nqaPathJitterStatsNumOfRtt"),
        ("NQA-MIB", "nqaPathJitterStatsRttSum"),
        ("NQA-MIB", "nqaJitterStatsOperOfIcpif"),
        ("NQA-MIB", "nqaJitterStatsOperOfMos"),
        ("NQA-MIB", "nqaJitterStatsMinDelaySD"),
        ("NQA-MIB", "nqaJitterStatsSum2DelaySDLow"),
        ("NQA-MIB", "nqaJitterStatsSum2DelaySDHigh"),
        ("NQA-MIB", "nqaJitterStatsMinDelayDS"),
        ("NQA-MIB", "nqaJitterStatsSum2DelayDSLow"),
        ("NQA-MIB", "nqaJitterStatsSum2DelayDSHigh"),
        ("NQA-MIB", "nqaJitterStatsTimeUnit"),
        ("NQA-MIB", "nqaJitterStatsAvgDelaySD"),
        ("NQA-MIB", "nqaJitterStatsAvgDelayDS"),
        ("NQA-MIB", "nqaJitterStatsPktRewriteNum"),
        ("NQA-MIB", "nqaJitterStatsPktRewriteRatio"),
        ("NQA-MIB", "nqaJitterStatsPktDisorderNum"),
        ("NQA-MIB", "nqaJitterStatsPktDisorderRatio"),
        ("NQA-MIB", "nqaJitterStatsFragPktDisorderNum"),
        ("NQA-MIB", "nqaJitterStatsFragPktDisorderRatio"),
        ("NQA-MIB", "nqaPathJitterStatsRttSum2Low"),
        ("NQA-MIB", "nqaPathJitterStatsRttSum2High"),
        ("NQA-MIB", "nqaPathJitterStatsRttMin"),
        ("NQA-MIB", "nqaPathJitterStatsRttMax"),
        ("NQA-MIB", "nqaPathJitterStatsMinOfPositivesSD"),
        ("NQA-MIB", "nqaPathJitterStatsMaxOfPositivesSD"),
        ("NQA-MIB", "nqaPathJitterStatsNumOfPositivesSD"),
        ("NQA-MIB", "nqaPathJitterStatsSumOfPositivesSD"),
        ("NQA-MIB", "nqaPathJitterStatsSum2OfPositivesSDLow"),
        ("NQA-MIB", "nqaPathJitterStatsSum2OfPositivesSDHigh"),
        ("NQA-MIB", "nqaPathJitterStatsMinOfNegativesSD"),
        ("NQA-MIB", "nqaPathJitterStatsMaxOfNegativesSD"),
        ("NQA-MIB", "nqaPathJitterStatsNumOfNegativesSD"),
        ("NQA-MIB", "nqaPathJitterStatsSumOfNegativesSD"),
        ("NQA-MIB", "nqaPathJitterStatsSum2OfNegativesSDLow"),
        ("NQA-MIB", "nqaPathJitterStatsSum2OfNegativesSDHigh"),
        ("NQA-MIB", "nqaPathJitterStatsMinOfPositivesDS"),
        ("NQA-MIB", "nqaPathJitterStatsMaxOfPositivesDS"),
        ("NQA-MIB", "nqaPathJitterStatsNumOfPositivesDS"),
        ("NQA-MIB", "nqaPathJitterStatsSumOfPositivesDS"),
        ("NQA-MIB", "nqaPathJitterStatsSum2OfPositivesDSLow"),
        ("NQA-MIB", "nqaPathJitterStatsSum2OfPositivesDSHigh"),
        ("NQA-MIB", "nqaPathJitterStatsMinOfNegativesDS"),
        ("NQA-MIB", "nqaPathJitterStatsMaxOfNegativesDS"),
        ("NQA-MIB", "nqaPathJitterStatsNumOfNegativesDS"),
        ("NQA-MIB", "nqaPathJitterStatsSumOfNegativesDS"),
        ("NQA-MIB", "nqaPathJitterStatsSum2OfNegativesDSLow"),
        ("NQA-MIB", "nqaPathJitterStatsSum2OfNegativesDSHigh"),
        ("NQA-MIB", "nqaPathJitterStatsPacketLossSD"),
        ("NQA-MIB", "nqaPathJitterStatsPacketLossDS"),
        ("NQA-MIB", "nqaPathJitterStatsPacketOutOfSequences"),
        ("NQA-MIB", "nqaPathJitterStatsErrors"),
        ("NQA-MIB", "nqaPathJitterStatsBusies"),
        ("NQA-MIB", "nqaPathJitterStatsTimeouts"),
        ("NQA-MIB", "nqaPathJitterStatsProbeResponses"),
        ("NQA-MIB", "nqaPathJitterStatsSentProbes"),
        ("NQA-MIB", "nqaPathJitterStatsDrops"),
        ("NQA-MIB", "nqaPathJitterStatsTestFinished"),
        ("NQA-MIB", "nqaPathJitterStatsMaxDelaySD"),
        ("NQA-MIB", "nqaPathJitterStatsMaxDelayDS"),
        ("NQA-MIB", "nqaPathJitterStatsRttAvg"),
        ("NQA-MIB", "nqaPathJitterStatsPacketLossRatio"),
        ("NQA-MIB", "nqaPathJitterStatsAvgJitter"),
        ("NQA-MIB", "nqaPathJitterStatsAvgJitterSD"),
        ("NQA-MIB", "nqaPathJitterStatsAvgJitterDS"),
        ("NQA-MIB", "nqaPathJitterStatsJitterOut"),
        ("NQA-MIB", "nqaPathJitterStatsJitterIn"),
        ("NQA-MIB", "nqaPathJitterStatsOwdOverThresholdsSD"),
        ("NQA-MIB", "nqaPathJitterStatsPktLossUnknown"),
        ("NQA-MIB", "nqaPathJitterStatsNumOfOwd"),
        ("NQA-MIB", "nqaPathJitterStatsOwdSumSD"),
        ("NQA-MIB", "nqaPathJitterStatsOwdSumDS"),
        ("NQA-MIB", "nqaPathJitterStatsOwdOverThresholdsDS"),
        ("NQA-MIB", "nqaPathMtuStatsAddressType"),
        ("NQA-MIB", "nqaPathMtuStatsAddress"),
        ("NQA-MIB", "nqaPathMtuStatsCompletions"),
        ("NQA-MIB", "nqaPathMtuStatsSentProbes"),
        ("NQA-MIB", "nqaPathMtuStatsDiscoveryPathMtuMin"),
        ("NQA-MIB", "nqaPathMtuStatsDiscoveryPathMtuMax"),
        ("NQA-MIB", "nqaPathMtuStatsOptimumFirstStep"),
        ("NQA-MIB", "nqaPathMtuStatsBusies"),
        ("NQA-MIB", "nqaPathMtuStatsTimeouts"),
        ("NQA-MIB", "nqaPathMtuStatsDrops"),
        ("NQA-MIB", "nqaPathMtuStatsProbeResponses"),
        ("NQA-MIB", "nqaPathMtuStatsPathMtu"),
        ("NQA-MIB", "nqaPathMtuStatsTestFinished"),
        ("NQA-MIB", "nqaJitterStatsOWSumDS"),
        ("NQA-MIB", "nqaResultsSumCompletionTime"),
        ("NQA-MIB", "nqaResultsSumCompletionTime2Low"),
        ("NQA-MIB", "nqaResultsSumCompletionTime2High"),
        ("NQA-MIB", "nqaFTPStatsCompletions"),
        ("NQA-MIB", "nqaFTPStatsRTDOverThresholds"),
        ("NQA-MIB", "nqaFTPStatsCtrlConnMaxTime"),
        ("NQA-MIB", "nqaFTPStatsCtrlConnMinTime"),
        ("NQA-MIB", "nqaFTPStatsCtrlConnAveTime"),
        ("NQA-MIB", "nqaFTPStatsDataConnMaxTime"),
        ("NQA-MIB", "nqaFTPStatsDataConnMinTime"),
        ("NQA-MIB", "nqaFTPStatsDataConnAveTime"),
        ("NQA-MIB", "nqaFTPStatsConnectSumTimeMax"),
        ("NQA-MIB", "nqaFTPStatsConnectSumTimeMin"),
        ("NQA-MIB", "nqaFTPStatsConnectSumTimeAve"),
        ("NQA-MIB", "nqaFTPStatsMessageBodyOctetsSum"),
        ("NQA-MIB", "nqaFTPStatsErrors"),
        ("NQA-MIB", "nqaFTPStatsTimeouts"),
        ("NQA-MIB", "nqaFTPStatsDiscontinued"),
        ("NQA-MIB", "nqaFTPStatsProbeResponses"),
        ("NQA-MIB", "nqaFTPStatsSendProbes"),
        ("NQA-MIB", "nqaFTPStatsTestFinished"),
        ("NQA-MIB", "nqaMpingStatsTargetAddressType"),
        ("NQA-MIB", "nqaMpingStatsTargetAddress"),
        ("NQA-MIB", "nqaMpingStatsReceiverAddress"),
        ("NQA-MIB", "nqaMpingStatsCompletions"),
        ("NQA-MIB", "nqaMpingStatsRTDOverThresholds"),
        ("NQA-MIB", "nqaMpingStatsSumCompletionTime"),
        ("NQA-MIB", "nqaMpingStatsSumCompletionTime2Low"),
        ("NQA-MIB", "nqaMpingStatsSumCompletionTime2High"),
        ("NQA-MIB", "nqaMpingStatsCompletionTimeMin"),
        ("NQA-MIB", "nqaMpingStatsCompletionTimeMax"),
        ("NQA-MIB", "nqaMpingStatsTimeouts"),
        ("NQA-MIB", "nqaMpingStatsBusies"),
        ("NQA-MIB", "nqaMpingStatsSequenceErrors"),
        ("NQA-MIB", "nqaMpingStatsDrops"),
        ("NQA-MIB", "nqaMpingStatsProbeResponses"),
        ("NQA-MIB", "nqaMpingStatsSentProbes"),
        ("NQA-MIB", "nqaMpingStatsLastGoodProbe"),
        ("NQA-MIB", "nqaMpingStatsTestFinished"),
        ("NQA-MIB", "nqaMpingStatsReceiverCount"),
        ("NQA-MIB", "nqaMpingStatsLastFibHit"),
        ("NQA-MIB", "nqaMpingStatsRttAvg"),
        ("NQA-MIB", "nqaMpingStatsLostPacketRatio"),
        ("NQA-MIB", "nqaMtracertStatsAddressType"),
        ("NQA-MIB", "nqaMtracertStatsAddress"),
        ("NQA-MIB", "nqaMtracertStatsCompletions"),
        ("NQA-MIB", "nqaMtracertStatsCurHopCount"),
        ("NQA-MIB", "nqaMtracertStatsCurProbeCount"),
        ("NQA-MIB", "nqaMtracertStatsRTDOverThresholds"),
        ("NQA-MIB", "nqaMtracertStatsTimeouts"),
        ("NQA-MIB", "nqaMtracertStatsBusies"),
        ("NQA-MIB", "nqaMtracertStatsSequenceErrors"),
        ("NQA-MIB", "nqaMtracertStatsDrops"),
        ("NQA-MIB", "nqaMtracertStatsProbeResponses"),
        ("NQA-MIB", "nqaMtracertStatsSentProbes"),
        ("NQA-MIB", "nqaMtracertStatsLastGoodProbe"),
        ("NQA-MIB", "nqaMtracertStatsLastGoodPath"),
        ("NQA-MIB", "nqaMtracertStatsTestFinished"),
        ("NQA-MIB", "nqaMtracertStatsCurPathTTL"),
        ("NQA-MIB", "nqaMtracertStatsMaxPathTTL"),
        ("NQA-MIB", "nqaMtracertStatsInPkgLossRate"),
        ("NQA-MIB", "nqaMtracertStatsSGPkgLossRate"),
        ("NQA-MIB", "nqaMtracertStatsInPkgRate"),
        ("NQA-MIB", "nqaMtracertStatsOutPkgRate"),
        ("NQA-MIB", "nqaMtracertStatsTimeDelay"),
        ("NQA-MIB", "nqaResultsRttAvg"),
        ("NQA-MIB", "nqaResultsLostPacketRatio"),
        ("NQA-MIB", "nqaHTTPStatsRttAvg"),
        ("NQA-MIB", "nqaHTTPStatsLostPacketRatio"),
        ("NQA-MIB", "nqaFTPStatsRttAvg"),
        ("NQA-MIB", "nqaFTPStatsLostPacketRatio"),
        ("NQA-MIB", "nqaPppoeStatsCompletions"),
        ("NQA-MIB", "nqaPppoeStatsCurrentPhase"),
        ("NQA-MIB", "nqaPppoeStatsErrorMessage"),
        ("NQA-MIB", "nqaPppoeDiscoveryTimeout"),
        ("NQA-MIB", "nqaPppoeLcpTimeout"),
        ("NQA-MIB", "nqaPppoeAuthorizationTimeout"),
        ("NQA-MIB", "nqaPppoeNcpTimeout"),
        ("NQA-MIB", "nqaPppoeConnectionTime"),
        ("NQA-MIB", "nqaPppoeClientSessionId"),
        ("NQA-MIB", "nqaPppoeClientIpAddress"),
        ("NQA-MIB", "nqaPppoeGatewayIpAddress"))
)
if mibBuilder.loadTexts:
    nqaStatsGroup.setStatus("current")

nqaHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 1, 5)
)
nqaHistoryGroup.setObjects(
      *(("NQA-MIB", "nqaHistoryTimeStamp"),
        ("NQA-MIB", "nqaHistoryAddressType"),
        ("NQA-MIB", "nqaHistoryAddress"),
        ("NQA-MIB", "nqaHistoryCompletionTime"),
        ("NQA-MIB", "nqaHistoryFinishState"),
        ("NQA-MIB", "nqaHistoryLastRC"),
        ("NQA-MIB", "nqaMpingHistoryAddressType"),
        ("NQA-MIB", "nqaMpingHistoryAddress"),
        ("NQA-MIB", "nqaMpingHistoryReceiverAddress"),
        ("NQA-MIB", "nqaMpingHistoryTimeStamp"),
        ("NQA-MIB", "nqaMpingHistoryCompletionTime"),
        ("NQA-MIB", "nqaMpingHistoryFinishState"),
        ("NQA-MIB", "nqaMpingHistoryLastRC"),
        ("NQA-MIB", "nqaMpingHistoryFibHit"),
        ("NQA-MIB", "nqaMtracertHistoryAddressType"),
        ("NQA-MIB", "nqaMtracertHistoryAddress"),
        ("NQA-MIB", "nqaMtracertHistoryTimeStamp"),
        ("NQA-MIB", "nqaMtracertHistoryCompletionTime"),
        ("NQA-MIB", "nqaMtracertHistoryLastRC"),
        ("NQA-MIB", "nqaMtracertHistoryCurQueryMode"),
        ("NQA-MIB", "nqaMtracertHistoryQueryArrivalTime"),
        ("NQA-MIB", "nqaMtracertHistoryIncomingIfAddress"),
        ("NQA-MIB", "nqaMtracertHistoryOutgoingIfAddress"),
        ("NQA-MIB", "nqaMtracertHistoryPreHopRouterAddress"),
        ("NQA-MIB", "nqaMtracertHistoryInputPacketCount"),
        ("NQA-MIB", "nqaMtracertHistoryOutputPacketCount"),
        ("NQA-MIB", "nqaMtracertHistoryTotalSGPacketCount"),
        ("NQA-MIB", "nqaMtracertHistoryRtgProtocol"),
        ("NQA-MIB", "nqaMtracertHistoryFwdTTL"),
        ("NQA-MIB", "nqaMtracertHistoryFwdCode"),
        ("NQA-MIB", "nqaMtracertHistroyFinishState"),
        ("NQA-MIB", "nqaVplsMacTracertHistoryTimeStamp"),
        ("NQA-MIB", "nqaVplsMacTracertHistoryAddressType"),
        ("NQA-MIB", "nqaVplsMacTracertHistoryAddress"),
        ("NQA-MIB", "nqaVplsMacTracertHistoryCompletionTime"),
        ("NQA-MIB", "nqaVplsMacTracertHistoryFinishState"),
        ("NQA-MIB", "nqaVplsMacTracertHistoryHitFlag"),
        ("NQA-MIB", "nqaVplsMacTracertHistoryDSCount"),
        ("NQA-MIB", "nqaVplsMacTracertHistorySuccessPathNode"),
        ("NQA-MIB", "nqaVplsMacTracertHistoryDSAddress"),
        ("NQA-MIB", "nqaVplsMTraceHistoryResponserAddressType"),
        ("NQA-MIB", "nqaVplsMTraceHistoryResponserAddress"),
        ("NQA-MIB", "nqaVplsMTraceHistoryUpStreamAddressType"),
        ("NQA-MIB", "nqaVplsMTraceHistoryUpStreamAddress"),
        ("NQA-MIB", "nqaVplsMTraceHistoryReceivedTtl"),
        ("NQA-MIB", "nqaVplsMTraceHistoryIGMPVersion"),
        ("NQA-MIB", "nqaVplsMTraceHistoryIGMPSnpgEnable"),
        ("NQA-MIB", "nqaVplsMTraceHistoryIGMPProxyEnable"),
        ("NQA-MIB", "nqaVplsMTraceHistoryIGMPRouterPortLearningEnable"),
        ("NQA-MIB", "nqaVplsMTraceHistoryRequireRouterAlertEnable"),
        ("NQA-MIB", "nqaVplsMTraceHistoryForwardMode"),
        ("NQA-MIB", "nqaVplsMTraceHistoryHitFlag"),
        ("NQA-MIB", "nqaVplsMTraceHistoryPWExist"),
        ("NQA-MIB", "nqaVplsMTraceHistoryGroupPolicy"),
        ("NQA-MIB", "nqaVplsMTraceHistoryRcvQueryCount"),
        ("NQA-MIB", "nqaVplsMTraceHistoryRcvReportCount"),
        ("NQA-MIB", "nqaVplsMTraceHistoryRcvLeaveCount"),
        ("NQA-MIB", "nqaVplsMTraceHistoryTimeStamp"),
        ("NQA-MIB", "nqaVplsMTraceHistoryCompletionTime"),
        ("NQA-MIB", "nqaVplsMTraceHistoryLastRC"),
        ("NQA-MIB", "nqaVplsMTraceHistoryLastRSC"),
        ("NQA-MIB", "nqaVplsMTraceHistoryFinishState"),
        ("NQA-MIB", "nqaVplsMTraceHistorySuccessPathNode"),
        ("NQA-MIB", "nqaMacTraceHistoryTTL"),
        ("NQA-MIB", "nqaMacTraceHistorySeqNumber"),
        ("NQA-MIB", "nqaMacTraceHistoryForwarded"),
        ("NQA-MIB", "nqaMacTraceHistoryCompletionTime"),
        ("NQA-MIB", "nqaMacTraceHistoryTerminalMep"),
        ("NQA-MIB", "nqaMacTraceHistoryRelayAction"),
        ("NQA-MIB", "nqaMacTraceHistoryIngressAction"),
        ("NQA-MIB", "nqaMacTraceHistoryIngressMac"),
        ("NQA-MIB", "nqaMacTraceHistoryIngressIfName"),
        ("NQA-MIB", "nqaMacTraceHistoryEgressAction"),
        ("NQA-MIB", "nqaMacTraceHistoryEgressMac"),
        ("NQA-MIB", "nqaMacTraceHistoryEgressIfName"))
)
if mibBuilder.loadTexts:
    nqaHistoryGroup.setStatus("current")

nqaCollectStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 1, 7)
)
nqaCollectStatsGroup.setObjects(
      *(("NQA-MIB", "nqaJitterCollectStatsCompletions"),
        ("NQA-MIB", "nqaJitterCollectStatsRTDOverThresholds"),
        ("NQA-MIB", "nqaJitterCollectStatsOWDOverThresholdsSD"),
        ("NQA-MIB", "nqaJitterCollectStatsOWDOverThresholdsDS"),
        ("NQA-MIB", "nqaJitterCollectStatsNumOfRTT"),
        ("NQA-MIB", "nqaJitterCollectStatsRTTSum"),
        ("NQA-MIB", "nqaJitterCollectStatsRTTSum2Low"),
        ("NQA-MIB", "nqaJitterCollectStatsRTTSum2High"),
        ("NQA-MIB", "nqaJitterCollectStatsRTTMin"),
        ("NQA-MIB", "nqaJitterCollectStatsRTTMax"),
        ("NQA-MIB", "nqaJitterCollectStatsMinOfPositivesSD"),
        ("NQA-MIB", "nqaJitterCollectStatsMaxOfPositivesSD"),
        ("NQA-MIB", "nqaJitterCollectStatsNumOfPositivesSD"),
        ("NQA-MIB", "nqaJitterCollectStatsSumOfPositivesSD"),
        ("NQA-MIB", "nqaJitterCollectStatsSum2OfPositivesSDLow"),
        ("NQA-MIB", "nqaJitterCollectStatsSum2OfPositivesSDHigh"),
        ("NQA-MIB", "nqaJitterCollectStatsMinOfNegativesSD"),
        ("NQA-MIB", "nqaJitterCollectStatsMaxOfNegativesSD"),
        ("NQA-MIB", "nqaJitterCollectStatsNumOfNegativesSD"),
        ("NQA-MIB", "nqaJitterCollectStatsSumOfNegativesSD"),
        ("NQA-MIB", "nqaJitterCollectStatsSum2OfNegativesSDLow"),
        ("NQA-MIB", "nqaJitterCollectStatsSum2OfNegativesSDHigh"),
        ("NQA-MIB", "nqaJitterCollectStatsMinOfPositivesDS"),
        ("NQA-MIB", "nqaJitterCollectStatsMaxOfPositivesDS"),
        ("NQA-MIB", "nqaJitterCollectStatsNumOfPositivesDS"),
        ("NQA-MIB", "nqaJitterCollectStatsSumOfPositivesDS"),
        ("NQA-MIB", "nqaJitterCollectStatsSum2OfPositivesDSLow"),
        ("NQA-MIB", "nqaJitterCollectStatsSum2OfPositivesDSHigh"),
        ("NQA-MIB", "nqaJitterCollectStatsMinOfNegativesDS"),
        ("NQA-MIB", "nqaJitterCollectStatsMaxOfNegativesDS"),
        ("NQA-MIB", "nqaJitterCollectStatsNumOfNegativesDS"),
        ("NQA-MIB", "nqaJitterCollectStatsSumOfNegativesDS"),
        ("NQA-MIB", "nqaJitterCollectStatsSum2OfNegativesDSLow"),
        ("NQA-MIB", "nqaJitterCollectStatsSum2OfNegativesDSHigh"),
        ("NQA-MIB", "nqaJitterCollectStatsMaxDelaySD"),
        ("NQA-MIB", "nqaJitterCollectStatsMaxDelayDS"),
        ("NQA-MIB", "nqaJitterCollectStatsNumOfOWD"),
        ("NQA-MIB", "nqaJitterCollectStatsOWSumSD"),
        ("NQA-MIB", "nqaJitterCollectStatsOWSumDS"),
        ("NQA-MIB", "nqaJitterCollectStatsPacketLossSD"),
        ("NQA-MIB", "nqaJitterCollectStatsPacketLossDS"),
        ("NQA-MIB", "nqaJitterCollectStatsPacketLossUnknown"),
        ("NQA-MIB", "nqaJitterCollectStatsPacketOutOfSequences"),
        ("NQA-MIB", "nqaJitterCollectStatsPacketLossRatio"),
        ("NQA-MIB", "nqaJitterCollectStatsErrors"),
        ("NQA-MIB", "nqaJitterCollectStatsBusies"),
        ("NQA-MIB", "nqaJitterCollectStatsTimeouts"),
        ("NQA-MIB", "nqaJitterCollectStatsProbeResponses"),
        ("NQA-MIB", "nqaJitterCollectStatsSentProbes"),
        ("NQA-MIB", "nqaJitterCollectStatsDrops"),
        ("NQA-MIB", "nqaJitterCollectStatsRTTAvg"),
        ("NQA-MIB", "nqaJitterCollectStatsAvgJitter"),
        ("NQA-MIB", "nqaJitterCollectStatsAvgJitterSD"),
        ("NQA-MIB", "nqaJitterCollectStatsAvgJitterDS"),
        ("NQA-MIB", "nqaJitterCollectStatsJitterOut"),
        ("NQA-MIB", "nqaJitterCollectStatsJitterIn"),
        ("NQA-MIB", "nqaJitterCollectStatsMinDelaySD"),
        ("NQA-MIB", "nqaJitterCollectStatsMinDelayDS"),
        ("NQA-MIB", "nqaJitterCollectStatsAvgDelaySD"),
        ("NQA-MIB", "nqaJitterCollectStatsAvgDelayDS"),
        ("NQA-MIB", "nqaJitterCollectStatsPktRewriteNum"),
        ("NQA-MIB", "nqaJitterCollectStatsPktRewriteRatio"),
        ("NQA-MIB", "nqaJitterCollectStatsPktDisorderNum"),
        ("NQA-MIB", "nqaJitterCollectStatsPktDisorderRatio"),
        ("NQA-MIB", "nqaJitterCollectStatsFragPktDisorderNum"),
        ("NQA-MIB", "nqaJitterCollectStatsFragPktDisorderRatio"))
)
if mibBuilder.loadTexts:
    nqaCollectStatsGroup.setStatus("current")

nqaAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 1, 8)
)
nqaAlarmGroup.setObjects(
      *(("NQA-MIB", "nqaMaxAlarmNum"),
        ("NQA-MIB", "nqaMaxEventNum"),
        ("NQA-MIB", "nqaAlarmVariable"),
        ("NQA-MIB", "nqaAlarmSampleType"),
        ("NQA-MIB", "nqaAlarmValue"),
        ("NQA-MIB", "nqaAlarmStartUpNqaAlarm"),
        ("NQA-MIB", "nqaAlarmRisingThreshold"),
        ("NQA-MIB", "nqaAlarmDescription"),
        ("NQA-MIB", "nqaAlarmFallingThreshold"),
        ("NQA-MIB", "nqaAlarmRisingEventIndex"),
        ("NQA-MIB", "nqaAlarmFallingEventIndex"),
        ("NQA-MIB", "nqaAlarmStatus"),
        ("NQA-MIB", "nqaEventDescription"),
        ("NQA-MIB", "nqaEventAdminName"),
        ("NQA-MIB", "nqaEventOperationTag"),
        ("NQA-MIB", "nqaEventType"),
        ("NQA-MIB", "nqaEventStatus"))
)
if mibBuilder.loadTexts:
    nqaAlarmGroup.setStatus("current")

nqaFtpSaveRecordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 1, 9)
)
nqaFtpSaveRecordGroup.setObjects(
      *(("NQA-MIB", "nqaFtpSaveRecordEnable"),
        ("NQA-MIB", "nqaFtpSaveRecordIpAddr"),
        ("NQA-MIB", "nqaFtpSaveRecordVrfName"),
        ("NQA-MIB", "nqaFtpSaveRecordUserName"),
        ("NQA-MIB", "nqaFtpSaveRecordPassword"),
        ("NQA-MIB", "nqaFtpSaveRecordFileName"),
        ("NQA-MIB", "nqaFtpSaveRecordItemNum"),
        ("NQA-MIB", "nqaFtpSaveRecordTime"),
        ("NQA-MIB", "nqaFtpSaveRecordNotificationEnable"),
        ("NQA-MIB", "nqaFtpSaveRecordLastFileName"))
)
if mibBuilder.loadTexts:
    nqaFtpSaveRecordGroup.setStatus("current")


# Notification objects

nqaResultsProbeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 1)
)
nqaResultsProbeFailed.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaResultsAddressType"),
        ("NQA-MIB", "nqaResultsAddress"),
        ("NQA-MIB", "nqaResultsCompletionTimeMin"),
        ("NQA-MIB", "nqaResultsCompletionTimeMax"),
        ("NQA-MIB", "nqaResultsSumCompletionTime"),
        ("NQA-MIB", "nqaResultsProbeResponses"),
        ("NQA-MIB", "nqaResultsSentProbes"),
        ("NQA-MIB", "nqaResultsSumCompletionTime2Low"),
        ("NQA-MIB", "nqaResultsSumCompletionTime2High"),
        ("NQA-MIB", "nqaResultsLastGoodProbe"),
        ("NQA-MIB", "nqaResultsLastGoodPath"))
)
if mibBuilder.loadTexts:
    nqaResultsProbeFailed.setStatus(
        "current"
    )

nqaResultsTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 2)
)
nqaResultsTestFailed.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaResultsAddressType"),
        ("NQA-MIB", "nqaResultsAddress"),
        ("NQA-MIB", "nqaResultsCompletionTimeMin"),
        ("NQA-MIB", "nqaResultsCompletionTimeMax"),
        ("NQA-MIB", "nqaResultsSumCompletionTime"),
        ("NQA-MIB", "nqaResultsProbeResponses"),
        ("NQA-MIB", "nqaResultsSentProbes"),
        ("NQA-MIB", "nqaResultsSumCompletionTime2Low"),
        ("NQA-MIB", "nqaResultsSumCompletionTime2High"),
        ("NQA-MIB", "nqaResultsLastGoodProbe"),
        ("NQA-MIB", "nqaResultsLastGoodPath"))
)
if mibBuilder.loadTexts:
    nqaResultsTestFailed.setStatus(
        "current"
    )

nqaResultsTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 3)
)
nqaResultsTestCompleted.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaResultsAddressType"),
        ("NQA-MIB", "nqaResultsAddress"),
        ("NQA-MIB", "nqaResultsCompletionTimeMin"),
        ("NQA-MIB", "nqaResultsCompletionTimeMax"),
        ("NQA-MIB", "nqaResultsSumCompletionTime"),
        ("NQA-MIB", "nqaResultsProbeResponses"),
        ("NQA-MIB", "nqaResultsSentProbes"),
        ("NQA-MIB", "nqaResultsSumCompletionTime2Low"),
        ("NQA-MIB", "nqaResultsSumCompletionTime2High"),
        ("NQA-MIB", "nqaResultsLastGoodProbe"),
        ("NQA-MIB", "nqaResultsLastGoodPath"))
)
if mibBuilder.loadTexts:
    nqaResultsTestCompleted.setStatus(
        "current"
    )

nqaResultsThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 4)
)
nqaResultsThresholdNotification.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaResultsAddressType"),
        ("NQA-MIB", "nqaResultsAddress"),
        ("NQA-MIB", "nqaAdminCtrlThreshold1"),
        ("NQA-MIB", "nqaResultsCompletionTimeMax"),
        ("NQA-MIB", "nqaResultsRTDOverThresholds"))
)
if mibBuilder.loadTexts:
    nqaResultsThresholdNotification.setStatus(
        "current"
    )

nqaHTTPStatsProbeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 5)
)
nqaHTTPStatsProbeFailed.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaHTTPStatsDNSRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsTransactionRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsDNSServerTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsTransactionTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsDNSQueryErrors"),
        ("NQA-MIB", "nqaHTTPStatsTcpConnErrors"),
        ("NQA-MIB", "nqaHTTPStatsErrors"),
        ("NQA-MIB", "nqaHTTPStatsProbeResponses"),
        ("NQA-MIB", "nqaHTTPStatsSendProbes"))
)
if mibBuilder.loadTexts:
    nqaHTTPStatsProbeFailed.setStatus(
        "current"
    )

nqaHTTPStatsTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 6)
)
nqaHTTPStatsTestFailed.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaHTTPStatsDNSRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsTransactionRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsDNSServerTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsTransactionTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsDNSQueryErrors"),
        ("NQA-MIB", "nqaHTTPStatsTcpConnErrors"),
        ("NQA-MIB", "nqaHTTPStatsErrors"),
        ("NQA-MIB", "nqaHTTPStatsProbeResponses"),
        ("NQA-MIB", "nqaHTTPStatsSendProbes"))
)
if mibBuilder.loadTexts:
    nqaHTTPStatsTestFailed.setStatus(
        "current"
    )

nqaHTTPStatsTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 7)
)
nqaHTTPStatsTestCompleted.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaHTTPStatsDNSRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsTransactionRTTSum"),
        ("NQA-MIB", "nqaHTTPStatsDNSServerTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsTransactionTimeouts"),
        ("NQA-MIB", "nqaHTTPStatsDNSQueryErrors"),
        ("NQA-MIB", "nqaHTTPStatsTcpConnErrors"),
        ("NQA-MIB", "nqaHTTPStatsErrors"),
        ("NQA-MIB", "nqaHTTPStatsProbeResponses"),
        ("NQA-MIB", "nqaHTTPStatsSendProbes"))
)
if mibBuilder.loadTexts:
    nqaHTTPStatsTestCompleted.setStatus(
        "current"
    )

nqaHTTPStatsThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 8)
)
nqaHTTPStatsThresholdNotification.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaAdminCtrlThreshold1"),
        ("NQA-MIB", "nqaAdminCtrlThreshold2"),
        ("NQA-MIB", "nqaAdminCtrlThreshold3"),
        ("NQA-MIB", "nqaHTTPStatsDNSRTTMax"),
        ("NQA-MIB", "nqaHTTPStatsTCPConnectRTTMax"),
        ("NQA-MIB", "nqaHTTPStatsTransactionRTTMax"),
        ("NQA-MIB", "nqaHTTPStatsRTDOverThresholds"))
)
if mibBuilder.loadTexts:
    nqaHTTPStatsThresholdNotification.setStatus(
        "current"
    )

nqaJitterStatsProbeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 9)
)
nqaJitterStatsProbeFailed.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaJitterStatsRTTSum"),
        ("NQA-MIB", "nqaJitterStatsRTTSum2Low"),
        ("NQA-MIB", "nqaJitterStatsRTTSum2High"),
        ("NQA-MIB", "nqaJitterStatsRTTMin"),
        ("NQA-MIB", "nqaJitterStatsRTTMax"),
        ("NQA-MIB", "nqaJitterStatsPacketOutOfSequences"),
        ("NQA-MIB", "nqaJitterStatsErrors"),
        ("NQA-MIB", "nqaJitterStatsBusies"),
        ("NQA-MIB", "nqaJitterStatsTimeouts"),
        ("NQA-MIB", "nqaJitterStatsDrops"),
        ("NQA-MIB", "nqaJitterStatsProbeResponses"),
        ("NQA-MIB", "nqaJitterStatsSentProbes"),
        ("NQA-MIB", "nqaJitterStatsMaxDelaySD"),
        ("NQA-MIB", "nqaJitterStatsMaxDelayDS"),
        ("NQA-MIB", "nqaJitterStatsJitterOut"),
        ("NQA-MIB", "nqaJitterStatsJitterIn"),
        ("NQA-MIB", "nqaJitterStatsOWSumSD"),
        ("NQA-MIB", "nqaJitterStatsOWSumDS"))
)
if mibBuilder.loadTexts:
    nqaJitterStatsProbeFailed.setStatus(
        "current"
    )

nqaJitterStatsTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 10)
)
nqaJitterStatsTestFailed.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaJitterStatsRTTSum"),
        ("NQA-MIB", "nqaJitterStatsRTTSum2Low"),
        ("NQA-MIB", "nqaJitterStatsRTTSum2High"),
        ("NQA-MIB", "nqaJitterStatsRTTMin"),
        ("NQA-MIB", "nqaJitterStatsRTTMax"),
        ("NQA-MIB", "nqaJitterStatsPacketOutOfSequences"),
        ("NQA-MIB", "nqaJitterStatsErrors"),
        ("NQA-MIB", "nqaJitterStatsBusies"),
        ("NQA-MIB", "nqaJitterStatsTimeouts"),
        ("NQA-MIB", "nqaJitterStatsDrops"),
        ("NQA-MIB", "nqaJitterStatsProbeResponses"),
        ("NQA-MIB", "nqaJitterStatsSentProbes"),
        ("NQA-MIB", "nqaJitterStatsMaxDelaySD"),
        ("NQA-MIB", "nqaJitterStatsMaxDelayDS"),
        ("NQA-MIB", "nqaJitterStatsJitterOut"),
        ("NQA-MIB", "nqaJitterStatsJitterIn"),
        ("NQA-MIB", "nqaJitterStatsOWSumSD"),
        ("NQA-MIB", "nqaJitterStatsOWSumDS"))
)
if mibBuilder.loadTexts:
    nqaJitterStatsTestFailed.setStatus(
        "current"
    )

nqaJitterStatsTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 11)
)
nqaJitterStatsTestCompleted.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaJitterStatsRTTSum"),
        ("NQA-MIB", "nqaJitterStatsRTTSum2Low"),
        ("NQA-MIB", "nqaJitterStatsRTTSum2High"),
        ("NQA-MIB", "nqaJitterStatsRTTMin"),
        ("NQA-MIB", "nqaJitterStatsRTTMax"),
        ("NQA-MIB", "nqaJitterStatsPacketOutOfSequences"),
        ("NQA-MIB", "nqaJitterStatsErrors"),
        ("NQA-MIB", "nqaJitterStatsBusies"),
        ("NQA-MIB", "nqaJitterStatsTimeouts"),
        ("NQA-MIB", "nqaJitterStatsDrops"),
        ("NQA-MIB", "nqaJitterStatsProbeResponses"),
        ("NQA-MIB", "nqaJitterStatsSentProbes"),
        ("NQA-MIB", "nqaJitterStatsMaxDelaySD"),
        ("NQA-MIB", "nqaJitterStatsMaxDelayDS"),
        ("NQA-MIB", "nqaJitterStatsJitterOut"),
        ("NQA-MIB", "nqaJitterStatsJitterIn"),
        ("NQA-MIB", "nqaJitterStatsOWSumSD"),
        ("NQA-MIB", "nqaJitterStatsOWSumDS"))
)
if mibBuilder.loadTexts:
    nqaJitterStatsTestCompleted.setStatus(
        "current"
    )

nqaFTPStatsProbeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 12)
)
nqaFTPStatsProbeFailed.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaFTPStatsCtrlConnMaxTime"),
        ("NQA-MIB", "nqaFTPStatsDataConnMaxTime"),
        ("NQA-MIB", "nqaFTPStatsConnectSumTimeMax"),
        ("NQA-MIB", "nqaFTPStatsErrors"),
        ("NQA-MIB", "nqaFTPStatsTimeouts"),
        ("NQA-MIB", "nqaFTPStatsProbeResponses"),
        ("NQA-MIB", "nqaFTPStatsSendProbes"))
)
if mibBuilder.loadTexts:
    nqaFTPStatsProbeFailed.setStatus(
        "current"
    )

nqaFTPStatsTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 13)
)
nqaFTPStatsTestFailed.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaFTPStatsCtrlConnMaxTime"),
        ("NQA-MIB", "nqaFTPStatsDataConnMaxTime"),
        ("NQA-MIB", "nqaFTPStatsConnectSumTimeMax"),
        ("NQA-MIB", "nqaFTPStatsErrors"),
        ("NQA-MIB", "nqaFTPStatsTimeouts"),
        ("NQA-MIB", "nqaFTPStatsProbeResponses"),
        ("NQA-MIB", "nqaFTPStatsSendProbes"))
)
if mibBuilder.loadTexts:
    nqaFTPStatsTestFailed.setStatus(
        "current"
    )

nqaFTPStatsTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 14)
)
nqaFTPStatsTestCompleted.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaScheduleOperStatus"),
        ("NQA-MIB", "nqaFTPStatsCtrlConnMaxTime"),
        ("NQA-MIB", "nqaFTPStatsDataConnMaxTime"),
        ("NQA-MIB", "nqaFTPStatsConnectSumTimeMax"),
        ("NQA-MIB", "nqaFTPStatsErrors"),
        ("NQA-MIB", "nqaFTPStatsTimeouts"),
        ("NQA-MIB", "nqaFTPStatsProbeResponses"),
        ("NQA-MIB", "nqaFTPStatsSendProbes"))
)
if mibBuilder.loadTexts:
    nqaFTPStatsTestCompleted.setStatus(
        "current"
    )

nqaFTPStatsThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 15)
)
nqaFTPStatsThresholdNotification.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaAdminCtrlThreshold1"),
        ("NQA-MIB", "nqaAdminCtrlThreshold2"),
        ("NQA-MIB", "nqaFTPStatsCtrlConnMaxTime"),
        ("NQA-MIB", "nqaFTPStatsDataConnMaxTime"),
        ("NQA-MIB", "nqaFTPStatsRTDOverThresholds"))
)
if mibBuilder.loadTexts:
    nqaFTPStatsThresholdNotification.setStatus(
        "current"
    )

nqaJitterStatsRTDThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 16)
)
nqaJitterStatsRTDThresholdNotification.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaAdminCtrlThreshold1"),
        ("NQA-MIB", "nqaJitterStatsRTTMax"),
        ("NQA-MIB", "nqaJitterStatsMaxDelaySD"),
        ("NQA-MIB", "nqaJitterStatsMaxDelayDS"),
        ("NQA-MIB", "nqaJitterStatsRTDOverThresholds"))
)
if mibBuilder.loadTexts:
    nqaJitterStatsRTDThresholdNotification.setStatus(
        "current"
    )

nqaJitterStatsOWDThresholdNotificationSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 17)
)
nqaJitterStatsOWDThresholdNotificationSD.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaAdminCtrlThreshold2"),
        ("NQA-MIB", "nqaJitterStatsRTTMax"),
        ("NQA-MIB", "nqaJitterStatsMaxDelaySD"),
        ("NQA-MIB", "nqaJitterStatsMaxDelayDS"),
        ("NQA-MIB", "nqaJitterStatsOWDOverThresholdsSD"))
)
if mibBuilder.loadTexts:
    nqaJitterStatsOWDThresholdNotificationSD.setStatus(
        "current"
    )

nqaJitterStatsOWDThresholdNotificationDS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 18)
)
nqaJitterStatsOWDThresholdNotificationDS.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaAdminCtrlThreshold3"),
        ("NQA-MIB", "nqaJitterStatsRTTMax"),
        ("NQA-MIB", "nqaJitterStatsMaxDelaySD"),
        ("NQA-MIB", "nqaJitterStatsMaxDelayDS"),
        ("NQA-MIB", "nqaJitterStatsOWDOverThresholdsDS"))
)
if mibBuilder.loadTexts:
    nqaJitterStatsOWDThresholdNotificationDS.setStatus(
        "current"
    )

nqaNegotiateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 19)
)
nqaNegotiateFailed.setObjects(
      *(("NQA-MIB", "nqaAdminParaTargetAddressType"),
        ("NQA-MIB", "nqaAdminParaTargetAddress"),
        ("NQA-MIB", "nqaAdminParaTargetPort"),
        ("NQA-MIB", "nqaAdminParaVrfName"))
)
if mibBuilder.loadTexts:
    nqaNegotiateFailed.setStatus(
        "current"
    )

nqaRisingAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 20)
)
nqaRisingAlarmNotification.setObjects(
      *(("NQA-MIB", "nqaAlarmVariable"),
        ("NQA-MIB", "nqaAlarmSampleType"),
        ("NQA-MIB", "nqaAlarmValue"),
        ("NQA-MIB", "nqaAlarmRisingThreshold"),
        ("NQA-MIB", "nqaAlarmDescription"))
)
if mibBuilder.loadTexts:
    nqaRisingAlarmNotification.setStatus(
        "current"
    )

nqaFallingAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 21)
)
nqaFallingAlarmNotification.setObjects(
      *(("NQA-MIB", "nqaAlarmVariable"),
        ("NQA-MIB", "nqaAlarmSampleType"),
        ("NQA-MIB", "nqaAlarmValue"),
        ("NQA-MIB", "nqaAlarmFallingThreshold"),
        ("NQA-MIB", "nqaAlarmDescription"))
)
if mibBuilder.loadTexts:
    nqaFallingAlarmNotification.setStatus(
        "current"
    )

nqaFtpSaveRecordNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 22)
)
nqaFtpSaveRecordNotification.setObjects(
    ("NQA-MIB", "nqaFtpSaveRecordLastFileName")
)
if mibBuilder.loadTexts:
    nqaFtpSaveRecordNotification.setStatus(
        "current"
    )

nqaPppoeStatsTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 23)
)
nqaPppoeStatsTestFailed.setObjects(
      *(("NQA-MIB", "nqaPppoeStatsCompletions"),
        ("NQA-MIB", "nqaPppoeStatsCurrentPhase"),
        ("NQA-MIB", "nqaPppoeStatsErrorMessage"),
        ("NQA-MIB", "nqaPppoeDiscoveryTimeout"),
        ("NQA-MIB", "nqaPppoeLcpTimeout"),
        ("NQA-MIB", "nqaPppoeAuthorizationTimeout"),
        ("NQA-MIB", "nqaPppoeNcpTimeout"),
        ("NQA-MIB", "nqaPppoeConnectionTime"),
        ("NQA-MIB", "nqaPppoeClientSessionId"),
        ("NQA-MIB", "nqaPppoeClientIpAddress"),
        ("NQA-MIB", "nqaPppoeGatewayIpAddress"))
)
if mibBuilder.loadTexts:
    nqaPppoeStatsTestFailed.setStatus(
        "current"
    )

nqaPppoeStatsTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 6, 24)
)
nqaPppoeStatsTestCompleted.setObjects(
      *(("NQA-MIB", "nqaPppoeStatsCompletions"),
        ("NQA-MIB", "nqaPppoeStatsCurrentPhase"),
        ("NQA-MIB", "nqaPppoeStatsErrorMessage"),
        ("NQA-MIB", "nqaPppoeDiscoveryTimeout"),
        ("NQA-MIB", "nqaPppoeLcpTimeout"),
        ("NQA-MIB", "nqaPppoeAuthorizationTimeout"),
        ("NQA-MIB", "nqaPppoeNcpTimeout"),
        ("NQA-MIB", "nqaPppoeConnectionTime"),
        ("NQA-MIB", "nqaPppoeClientSessionId"),
        ("NQA-MIB", "nqaPppoeClientIpAddress"),
        ("NQA-MIB", "nqaPppoeGatewayIpAddress"))
)
if mibBuilder.loadTexts:
    nqaPppoeStatsTestCompleted.setStatus(
        "current"
    )


# Notifications groups

nqaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 1, 6)
)
nqaNotificationsGroup.setObjects(
      *(("NQA-MIB", "nqaResultsProbeFailed"),
        ("NQA-MIB", "nqaResultsTestFailed"),
        ("NQA-MIB", "nqaResultsTestCompleted"),
        ("NQA-MIB", "nqaResultsThresholdNotification"),
        ("NQA-MIB", "nqaHTTPStatsProbeFailed"),
        ("NQA-MIB", "nqaHTTPStatsTestFailed"),
        ("NQA-MIB", "nqaHTTPStatsTestCompleted"),
        ("NQA-MIB", "nqaHTTPStatsThresholdNotification"),
        ("NQA-MIB", "nqaJitterStatsProbeFailed"),
        ("NQA-MIB", "nqaJitterStatsTestFailed"),
        ("NQA-MIB", "nqaJitterStatsTestCompleted"),
        ("NQA-MIB", "nqaFTPStatsProbeFailed"),
        ("NQA-MIB", "nqaFTPStatsTestFailed"),
        ("NQA-MIB", "nqaFTPStatsTestCompleted"),
        ("NQA-MIB", "nqaFTPStatsThresholdNotification"),
        ("NQA-MIB", "nqaJitterStatsRTDThresholdNotification"),
        ("NQA-MIB", "nqaJitterStatsOWDThresholdNotificationSD"),
        ("NQA-MIB", "nqaJitterStatsOWDThresholdNotificationDS"),
        ("NQA-MIB", "nqaNegotiateFailed"),
        ("NQA-MIB", "nqaRisingAlarmNotification"),
        ("NQA-MIB", "nqaFallingAlarmNotification"),
        ("NQA-MIB", "nqaFtpSaveRecordNotification"),
        ("NQA-MIB", "nqaPppoeStatsTestFailed"),
        ("NQA-MIB", "nqaPppoeStatsTestCompleted"))
)
if mibBuilder.loadTexts:
    nqaNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nqaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 111, 7, 2, 1)
)
if mibBuilder.loadTexts:
    nqaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NQA-MIB",
    **{"NqaType": NqaType,
       "EnableValue": EnableValue,
       "NqaDistanceNodeType": NqaDistanceNodeType,
       "HWLldpPortIdSubtype": HWLldpPortIdSubtype,
       "HWLldpPortId": HWLldpPortId,
       "NqaOperation": NqaOperation,
       "nqa": nqa,
       "nqaBase": nqaBase,
       "nqaVersion": nqaVersion,
       "nqaEnable": nqaEnable,
       "nqaReset": nqaReset,
       "nqaTimeOfLastSetError": nqaTimeOfLastSetError,
       "nqaLastSetError": nqaLastSetError,
       "nqaNumOfCurrentCtrlEntry": nqaNumOfCurrentCtrlEntry,
       "nqaMaxConcurrentRequests": nqaMaxConcurrentRequests,
       "nqaMaxNumOfRequests": nqaMaxNumOfRequests,
       "nqaJitterVersion": nqaJitterVersion,
       "nqaSupportTestType": nqaSupportTestType,
       "nqaSupportServerType": nqaSupportServerType,
       "nqaCtrl": nqaCtrl,
       "nqaAdminCtrlTable": nqaAdminCtrlTable,
       "nqaAdminCtrlEntry": nqaAdminCtrlEntry,
       "nqaAdminCtrlOwnerIndex": nqaAdminCtrlOwnerIndex,
       "nqaAdminCtrlTestName": nqaAdminCtrlTestName,
       "nqaAdminCtrlTag": nqaAdminCtrlTag,
       "nqaAdminCtrlType": nqaAdminCtrlType,
       "nqaAdminCtrlFrequency": nqaAdminCtrlFrequency,
       "nqaAdminCtrlTimeOut": nqaAdminCtrlTimeOut,
       "nqaAdminCtrlThreshold1": nqaAdminCtrlThreshold1,
       "nqaAdminCtrlThreshold2": nqaAdminCtrlThreshold2,
       "nqaAdminCtrlThreshold3": nqaAdminCtrlThreshold3,
       "nqaAdminCtrlStatus": nqaAdminCtrlStatus,
       "nqaAdminParaTable": nqaAdminParaTable,
       "nqaAdminParaEntry": nqaAdminParaEntry,
       "nqaAdminParaTargetAddressType": nqaAdminParaTargetAddressType,
       "nqaAdminParaTargetAddress": nqaAdminParaTargetAddress,
       "nqaAdminParaTargetPort": nqaAdminParaTargetPort,
       "nqaAdminParaSourceAddressType": nqaAdminParaSourceAddressType,
       "nqaAdminParaSourceAddress": nqaAdminParaSourceAddress,
       "nqaAdminParaSourcePort": nqaAdminParaSourcePort,
       "nqaAdminParaMaxTtl": nqaAdminParaMaxTtl,
       "nqaAdminParaInitialTtl": nqaAdminParaInitialTtl,
       "nqaAdminParaStorageType": nqaAdminParaStorageType,
       "nqaAdminParaMaxFailures": nqaAdminParaMaxFailures,
       "nqaAdminParaDontFragment": nqaAdminParaDontFragment,
       "nqaAdminParaDataSize": nqaAdminParaDataSize,
       "nqaAdminParaDataFill": nqaAdminParaDataFill,
       "nqaAdminParaIfIndex": nqaAdminParaIfIndex,
       "nqaAdminParaByPassRouteTable": nqaAdminParaByPassRouteTable,
       "nqaAdminParaMiscOptions": nqaAdminParaMiscOptions,
       "nqaAdminParaProbeCount": nqaAdminParaProbeCount,
       "nqaAdminParaTrapGeneration": nqaAdminParaTrapGeneration,
       "nqaAdminParaTrapProbeFailureFilter": nqaAdminParaTrapProbeFailureFilter,
       "nqaAdminParaTrapTestFailureFilter": nqaAdminParaTrapTestFailureFilter,
       "nqaAdminParaDSField": nqaAdminParaDSField,
       "nqaAdminParaDnsServerAddressType": nqaAdminParaDnsServerAddressType,
       "nqaAdminParaDnsServerAddress": nqaAdminParaDnsServerAddress,
       "nqaAdminParaOperation": nqaAdminParaOperation,
       "nqaAdminParaHttpVersion": nqaAdminParaHttpVersion,
       "nqaAdminParaHttpOperationString": nqaAdminParaHttpOperationString,
       "nqaAdminParaTestFailurePercent": nqaAdminParaTestFailurePercent,
       "nqaAdminParaFtpUserName": nqaAdminParaFtpUserName,
       "nqaAdminParaFtpPassword": nqaAdminParaFtpPassword,
       "nqaAdminParaFtpFilePath": nqaAdminParaFtpFilePath,
       "nqaAdminParaFtpFileSize": nqaAdminParaFtpFileSize,
       "nqaAdminParaInterval": nqaAdminParaInterval,
       "nqaAdminParaNumPackets": nqaAdminParaNumPackets,
       "nqaAdminParaVrfName": nqaAdminParaVrfName,
       "nqaAdminParaLspAddressType": nqaAdminParaLspAddressType,
       "nqaAdminParaLspAddressMask": nqaAdminParaLspAddressMask,
       "nqaAdminParaLspIpAddress": nqaAdminParaLspIpAddress,
       "nqaAdminParaLspPWE3VcId": nqaAdminParaLspPWE3VcId,
       "nqaAdminParaLspPWE3Type": nqaAdminParaLspPWE3Type,
       "nqaAdminParaLspPWE3Option": nqaAdminParaLspPWE3Option,
       "nqaAdminParaLspPWE3RemoteVcId": nqaAdminParaLspPWE3RemoteVcId,
       "nqaAdminParaLspPWE3RemoteAddress": nqaAdminParaLspPWE3RemoteAddress,
       "nqaAdminParaLspExp": nqaAdminParaLspExp,
       "nqaAdminParaLspReplyMode": nqaAdminParaLspReplyMode,
       "nqaAdminParaResultRowMax": nqaAdminParaResultRowMax,
       "nqaAdminParaHistoryRowMax": nqaAdminParaHistoryRowMax,
       "nqaAdminParaCreateHopsEntries": nqaAdminParaCreateHopsEntries,
       "nqaAdminParaLspVCType": nqaAdminParaLspVCType,
       "nqaAdminParaMTraceLastHopAddress": nqaAdminParaMTraceLastHopAddress,
       "nqaAdminParaMTraceSourceAddress": nqaAdminParaMTraceSourceAddress,
       "nqaAdminParaMTraceGroupAddress": nqaAdminParaMTraceGroupAddress,
       "nqaAdminParaMTraceMaxTtl": nqaAdminParaMTraceMaxTtl,
       "nqaAdminParaMTraceSendMode": nqaAdminParaMTraceSendMode,
       "nqaAdminParaMTraceResponseTtl": nqaAdminParaMTraceResponseTtl,
       "nqaAdminParaMTraceResponseAddressType": nqaAdminParaMTraceResponseAddressType,
       "nqaAdminParaMTraceResponseAddress": nqaAdminParaMTraceResponseAddress,
       "nqaAdminParaDistanceNodeType": nqaAdminParaDistanceNodeType,
       "nqaAdminParaMacAddress": nqaAdminParaMacAddress,
       "nqaAdminParaRMepID": nqaAdminParaRMepID,
       "nqaAdminParaMDName": nqaAdminParaMDName,
       "nqaAdminParaMAName": nqaAdminParaMAName,
       "nqaAdminParaMacTunnelName": nqaAdminParaMacTunnelName,
       "nqaAdminParaPathMtuStep": nqaAdminParaPathMtuStep,
       "nqaAdminParaPathMtuDiscoveryPathMtuMax": nqaAdminParaPathMtuDiscoveryPathMtuMax,
       "nqaAdminParaIcmpJitterMode": nqaAdminParaIcmpJitterMode,
       "nqaAdminParaCodecType": nqaAdminParaCodecType,
       "nqaAdminParaIcpifAdvFactor": nqaAdminParaIcpifAdvFactor,
       "nqaAdminParaFtpMode": nqaAdminParaFtpMode,
       "nqaAdminParaHardwareBased": nqaAdminParaHardwareBased,
       "nqaAdminParaPppoeUserName": nqaAdminParaPppoeUserName,
       "nqaAdminParaPppoePassword": nqaAdminParaPppoePassword,
       "nqaAdminParaPppoeVlanIf": nqaAdminParaPppoeVlanIf,
       "nqaAdminParaPppoeAuthenticationMode": nqaAdminParaPppoeAuthenticationMode,
       "nqaAdminParaPppoeRedialUpTimes": nqaAdminParaPppoeRedialUpTimes,
       "nqaAdminParaPppoeInterval": nqaAdminParaPppoeInterval,
       "nqaAdminParaVsiName": nqaAdminParaVsiName,
       "nqaAdminParaVlanId": nqaAdminParaVlanId,
       "nqaAdminParaLspTunnelType": nqaAdminParaLspTunnelType,
       "nqaAdminParaLspNextHopAddress": nqaAdminParaLspNextHopAddress,
       "nqaAdminParaLspVersion": nqaAdminParaLspVersion,
       "nqaAdminParaRemoteAddressType": nqaAdminParaRemoteAddressType,
       "nqaAdminParaRemoteAddress": nqaAdminParaRemoteAddress,
       "nqaAdminParaTimeUnit": nqaAdminParaTimeUnit,
       "nqaScheduleTable": nqaScheduleTable,
       "nqaScheduleEntry": nqaScheduleEntry,
       "nqaScheduleStartType": nqaScheduleStartType,
       "nqaScheduleStartTime": nqaScheduleStartTime,
       "nqaScheduleEndType": nqaScheduleEndType,
       "nqaScheduleEndTime": nqaScheduleEndTime,
       "nqaScheduleAgeTime": nqaScheduleAgeTime,
       "nqaScheduleElapsedTime": nqaScheduleElapsedTime,
       "nqaScheduleNumOfInitiations": nqaScheduleNumOfInitiations,
       "nqaScheduleLastFinishIndex": nqaScheduleLastFinishIndex,
       "nqaScheduleOperStatus": nqaScheduleOperStatus,
       "nqaScheduleLastCollectIndex": nqaScheduleLastCollectIndex,
       "nqaGroupTable": nqaGroupTable,
       "nqaGroupEntry": nqaGroupEntry,
       "nqaGroupStatusType": nqaGroupStatusType,
       "nqaGroupPeriod": nqaGroupPeriod,
       "nqaGroupLeaderOwnerIndex": nqaGroupLeaderOwnerIndex,
       "nqaGroupLeaderTestName": nqaGroupLeaderTestName,
       "nqaGroupMemberNum": nqaGroupMemberNum,
       "nqaGroupMemberFree": nqaGroupMemberFree,
       "nqaAdminParaExtTable": nqaAdminParaExtTable,
       "nqaAdminParaExtEntry": nqaAdminParaExtEntry,
       "nqaAdminExtPara1": nqaAdminExtPara1,
       "nqaAdminExtPara2": nqaAdminExtPara2,
       "nqaAdminExtPara3": nqaAdminExtPara3,
       "nqaAdminExtPara4": nqaAdminExtPara4,
       "nqaAdminExtPara5": nqaAdminExtPara5,
       "nqaAdminExtPara6": nqaAdminExtPara6,
       "nqaAdminExtPara7": nqaAdminExtPara7,
       "nqaAdminExtPara8": nqaAdminExtPara8,
       "nqaAdminExtPara9": nqaAdminExtPara9,
       "nqaAdminExtPara10": nqaAdminExtPara10,
       "nqaAdminExtPara11": nqaAdminExtPara11,
       "nqaAdminExtPara12": nqaAdminExtPara12,
       "nqaAdminExtPara13": nqaAdminExtPara13,
       "nqaAdminExtPara14": nqaAdminExtPara14,
       "nqaAdminExtPara15": nqaAdminExtPara15,
       "nqaAdminExtPara16": nqaAdminExtPara16,
       "nqaAdminExtPara17": nqaAdminExtPara17,
       "nqaAdminExtPara18": nqaAdminExtPara18,
       "nqaAdminExtPara19": nqaAdminExtPara19,
       "nqaAdminExtPara20": nqaAdminExtPara20,
       "nqaAdminExtPara21": nqaAdminExtPara21,
       "nqaAdminExtPara22": nqaAdminExtPara22,
       "nqaAdminExtPara23": nqaAdminExtPara23,
       "nqaAdminExtPara24": nqaAdminExtPara24,
       "nqaAdminExtPara25": nqaAdminExtPara25,
       "nqaAdminExtPara26": nqaAdminExtPara26,
       "nqaAdminExtPara27": nqaAdminExtPara27,
       "nqaAdminExtPara28": nqaAdminExtPara28,
       "nqaAdminExtPara29": nqaAdminExtPara29,
       "nqaAdminExtPara30": nqaAdminExtPara30,
       "nqaAdminExtPara31": nqaAdminExtPara31,
       "nqaAdminExtPara32": nqaAdminExtPara32,
       "nqaAdminExtPara33": nqaAdminExtPara33,
       "nqaAdminExtPara34": nqaAdminExtPara34,
       "nqaAdminExtPara35": nqaAdminExtPara35,
       "nqaAdminExtPara36": nqaAdminExtPara36,
       "nqaAdminExtPara37": nqaAdminExtPara37,
       "nqaAdminExtPara38": nqaAdminExtPara38,
       "nqaAdminExtPara39": nqaAdminExtPara39,
       "nqaAdminExtPara40": nqaAdminExtPara40,
       "nqaAdminExtPara41": nqaAdminExtPara41,
       "nqaAdminExtPara42": nqaAdminExtPara42,
       "nqaAdminExtPara43": nqaAdminExtPara43,
       "nqaAdminExtPara44": nqaAdminExtPara44,
       "nqaAdminExtPara45": nqaAdminExtPara45,
       "nqaAdminExtPara46": nqaAdminExtPara46,
       "nqaAdminExtPara47": nqaAdminExtPara47,
       "nqaAdminExtPara48": nqaAdminExtPara48,
       "nqaAdminExtPara49": nqaAdminExtPara49,
       "nqaAdminExtPara50": nqaAdminExtPara50,
       "nqaServer": nqaServer,
       "nqaServerEnable": nqaServerEnable,
       "nqaTcpServerTable": nqaTcpServerTable,
       "nqaTcpServerEntry": nqaTcpServerEntry,
       "nqaTcpServerAddressType": nqaTcpServerAddressType,
       "nqaTcpServerAddress": nqaTcpServerAddress,
       "nqaTcpServerPort": nqaTcpServerPort,
       "nqaTcpServerVrfName": nqaTcpServerVrfName,
       "nqaTcpServerStatus": nqaTcpServerStatus,
       "nqaUdpServerTable": nqaUdpServerTable,
       "nqaUdpServerEntry": nqaUdpServerEntry,
       "nqaUdpServerAddressType": nqaUdpServerAddressType,
       "nqaUdpServerAddress": nqaUdpServerAddress,
       "nqaUdpServerPort": nqaUdpServerPort,
       "nqaUdpServerVrfName": nqaUdpServerVrfName,
       "nqaUdpServerStatus": nqaUdpServerStatus,
       "nqaIcmpServerTable": nqaIcmpServerTable,
       "nqaIcmpServerEntry": nqaIcmpServerEntry,
       "nqaIcmpServerAddress": nqaIcmpServerAddress,
       "nqaIcmpServerVrfName": nqaIcmpServerVrfName,
       "nqaIcmpServerAddressType": nqaIcmpServerAddressType,
       "nqaIcmpServerStatus": nqaIcmpServerStatus,
       "nqaStats": nqaStats,
       "nqaResultsTable": nqaResultsTable,
       "nqaResultsEntry": nqaResultsEntry,
       "nqaResultsIndex": nqaResultsIndex,
       "nqaResultsHopIndex": nqaResultsHopIndex,
       "nqaResultsCompletions": nqaResultsCompletions,
       "nqaResultsTestAttempts": nqaResultsTestAttempts,
       "nqaResultsCurHopCount": nqaResultsCurHopCount,
       "nqaResultsCurProbeCount": nqaResultsCurProbeCount,
       "nqaResultsRTDOverThresholds": nqaResultsRTDOverThresholds,
       "nqaResultsSumCompletionTime": nqaResultsSumCompletionTime,
       "nqaResultsSumCompletionTime2Low": nqaResultsSumCompletionTime2Low,
       "nqaResultsSumCompletionTime2High": nqaResultsSumCompletionTime2High,
       "nqaResultsCompletionTimeMin": nqaResultsCompletionTimeMin,
       "nqaResultsCompletionTimeMax": nqaResultsCompletionTimeMax,
       "nqaResultsDisconnects": nqaResultsDisconnects,
       "nqaResultsTimeouts": nqaResultsTimeouts,
       "nqaResultsBusies": nqaResultsBusies,
       "nqaResultsNoConnections": nqaResultsNoConnections,
       "nqaResultsSequenceErrors": nqaResultsSequenceErrors,
       "nqaResultsDrops": nqaResultsDrops,
       "nqaResultsAddressType": nqaResultsAddressType,
       "nqaResultsAddress": nqaResultsAddress,
       "nqaResultsProbeResponses": nqaResultsProbeResponses,
       "nqaResultsSentProbes": nqaResultsSentProbes,
       "nqaResultsLastGoodProbe": nqaResultsLastGoodProbe,
       "nqaResultsLastGoodPath": nqaResultsLastGoodPath,
       "nqaResultsTestFinished": nqaResultsTestFinished,
       "nqaResultsRttAvg": nqaResultsRttAvg,
       "nqaResultsLostPacketRatio": nqaResultsLostPacketRatio,
       "nqaHTTPStatsTable": nqaHTTPStatsTable,
       "nqaHTTPStatsEntry": nqaHTTPStatsEntry,
       "nqaHTTPStatsIndex": nqaHTTPStatsIndex,
       "nqaHTTPStatsCompletions": nqaHTTPStatsCompletions,
       "nqaHTTPStatsRTDOverThresholds": nqaHTTPStatsRTDOverThresholds,
       "nqaHTTPStatsRTTSum": nqaHTTPStatsRTTSum,
       "nqaHTTPStatsRTTMin": nqaHTTPStatsRTTMin,
       "nqaHTTPStatsRTTMax": nqaHTTPStatsRTTMax,
       "nqaHTTPStatsDNSRTTSum": nqaHTTPStatsDNSRTTSum,
       "nqaHTTPStatsDNSRTTMin": nqaHTTPStatsDNSRTTMin,
       "nqaHTTPStatsDNSRTTMax": nqaHTTPStatsDNSRTTMax,
       "nqaHTTPStatsTCPConnectRTTSum": nqaHTTPStatsTCPConnectRTTSum,
       "nqaHTTPStatsTCPConnectRTTMin": nqaHTTPStatsTCPConnectRTTMin,
       "nqaHTTPStatsTCPConnectRTTMax": nqaHTTPStatsTCPConnectRTTMax,
       "nqaHTTPStatsTransactionRTTSum": nqaHTTPStatsTransactionRTTSum,
       "nqaHTTPStatsTransactionRTTMin": nqaHTTPStatsTransactionRTTMin,
       "nqaHTTPStatsTransactionRTTMax": nqaHTTPStatsTransactionRTTMax,
       "nqaHTTPStatsMessageBodyOctetsSum": nqaHTTPStatsMessageBodyOctetsSum,
       "nqaHTTPStatsDNSServerTimeouts": nqaHTTPStatsDNSServerTimeouts,
       "nqaHTTPStatsTCPConnectTimeouts": nqaHTTPStatsTCPConnectTimeouts,
       "nqaHTTPStatsTransactionTimeouts": nqaHTTPStatsTransactionTimeouts,
       "nqaHTTPStatsDNSQueryErrors": nqaHTTPStatsDNSQueryErrors,
       "nqaHTTPStatsErrors": nqaHTTPStatsErrors,
       "nqaHTTPStatsTcpConnErrors": nqaHTTPStatsTcpConnErrors,
       "nqaHTTPStatsProbeResponses": nqaHTTPStatsProbeResponses,
       "nqaHTTPStatsSendProbes": nqaHTTPStatsSendProbes,
       "nqaHTTPStatsBusies": nqaHTTPStatsBusies,
       "nqaHTTPStatsTestFinished": nqaHTTPStatsTestFinished,
       "nqaHTTPStatsRttAvg": nqaHTTPStatsRttAvg,
       "nqaHTTPStatsLostPacketRatio": nqaHTTPStatsLostPacketRatio,
       "nqaJitterStatsTable": nqaJitterStatsTable,
       "nqaJitterStatsEntry": nqaJitterStatsEntry,
       "nqaJitterStatsIndex": nqaJitterStatsIndex,
       "nqaJitterStatsCompletions": nqaJitterStatsCompletions,
       "nqaJitterStatsRTDOverThresholds": nqaJitterStatsRTDOverThresholds,
       "nqaJitterStatsNumOfRTT": nqaJitterStatsNumOfRTT,
       "nqaJitterStatsRTTSum": nqaJitterStatsRTTSum,
       "nqaJitterStatsRTTSum2Low": nqaJitterStatsRTTSum2Low,
       "nqaJitterStatsRTTSum2High": nqaJitterStatsRTTSum2High,
       "nqaJitterStatsRTTMin": nqaJitterStatsRTTMin,
       "nqaJitterStatsRTTMax": nqaJitterStatsRTTMax,
       "nqaJitterStatsMinOfPositivesSD": nqaJitterStatsMinOfPositivesSD,
       "nqaJitterStatsMaxOfPositivesSD": nqaJitterStatsMaxOfPositivesSD,
       "nqaJitterStatsNumOfPositivesSD": nqaJitterStatsNumOfPositivesSD,
       "nqaJitterStatsSumOfPositivesSD": nqaJitterStatsSumOfPositivesSD,
       "nqaJitterStatsSum2OfPositivesSDLow": nqaJitterStatsSum2OfPositivesSDLow,
       "nqaJitterStatsSum2OfPositivesSDHigh": nqaJitterStatsSum2OfPositivesSDHigh,
       "nqaJitterStatsMinOfNegativesSD": nqaJitterStatsMinOfNegativesSD,
       "nqaJitterStatsMaxOfNegativesSD": nqaJitterStatsMaxOfNegativesSD,
       "nqaJitterStatsNumOfNegativesSD": nqaJitterStatsNumOfNegativesSD,
       "nqaJitterStatsSumOfNegativesSD": nqaJitterStatsSumOfNegativesSD,
       "nqaJitterStatsSum2OfNegativesSDLow": nqaJitterStatsSum2OfNegativesSDLow,
       "nqaJitterStatsSum2OfNegativesSDHigh": nqaJitterStatsSum2OfNegativesSDHigh,
       "nqaJitterStatsMinOfPositivesDS": nqaJitterStatsMinOfPositivesDS,
       "nqaJitterStatsMaxOfPositivesDS": nqaJitterStatsMaxOfPositivesDS,
       "nqaJitterStatsNumOfPositivesDS": nqaJitterStatsNumOfPositivesDS,
       "nqaJitterStatsSumOfPositivesDS": nqaJitterStatsSumOfPositivesDS,
       "nqaJitterStatsSum2OfPositivesDSLow": nqaJitterStatsSum2OfPositivesDSLow,
       "nqaJitterStatsSum2OfPositivesDSHigh": nqaJitterStatsSum2OfPositivesDSHigh,
       "nqaJitterStatsMinOfNegativesDS": nqaJitterStatsMinOfNegativesDS,
       "nqaJitterStatsMaxOfNegativesDS": nqaJitterStatsMaxOfNegativesDS,
       "nqaJitterStatsNumOfNegativesDS": nqaJitterStatsNumOfNegativesDS,
       "nqaJitterStatsSumOfNegativesDS": nqaJitterStatsSumOfNegativesDS,
       "nqaJitterStatsSum2OfNegativesDSLow": nqaJitterStatsSum2OfNegativesDSLow,
       "nqaJitterStatsSum2OfNegativesDSHigh": nqaJitterStatsSum2OfNegativesDSHigh,
       "nqaJitterStatsPacketLossSD": nqaJitterStatsPacketLossSD,
       "nqaJitterStatsPacketLossDS": nqaJitterStatsPacketLossDS,
       "nqaJitterStatsPacketOutOfSequences": nqaJitterStatsPacketOutOfSequences,
       "nqaJitterStatsErrors": nqaJitterStatsErrors,
       "nqaJitterStatsBusies": nqaJitterStatsBusies,
       "nqaJitterStatsTimeouts": nqaJitterStatsTimeouts,
       "nqaJitterStatsProbeResponses": nqaJitterStatsProbeResponses,
       "nqaJitterStatsSentProbes": nqaJitterStatsSentProbes,
       "nqaJitterStatsDrops": nqaJitterStatsDrops,
       "nqaJitterStatsTestFinished": nqaJitterStatsTestFinished,
       "nqaJitterStatsMaxDelaySD": nqaJitterStatsMaxDelaySD,
       "nqaJitterStatsMaxDelayDS": nqaJitterStatsMaxDelayDS,
       "nqaJitterStatsRTTAvg": nqaJitterStatsRTTAvg,
       "nqaJitterStatsPacketLossRatio": nqaJitterStatsPacketLossRatio,
       "nqaJitterStatsAvgJitter": nqaJitterStatsAvgJitter,
       "nqaJitterStatsAvgJitterSD": nqaJitterStatsAvgJitterSD,
       "nqaJitterStatsAvgJitterDS": nqaJitterStatsAvgJitterDS,
       "nqaJitterStatsJitterOut": nqaJitterStatsJitterOut,
       "nqaJitterStatsJitterIn": nqaJitterStatsJitterIn,
       "nqaJitterStatsOWDOverThresholdsSD": nqaJitterStatsOWDOverThresholdsSD,
       "nqaJitterStatsPktLossUnknown": nqaJitterStatsPktLossUnknown,
       "nqaJitterStatsNumOfOWD": nqaJitterStatsNumOfOWD,
       "nqaJitterStatsOWSumSD": nqaJitterStatsOWSumSD,
       "nqaJitterStatsOWSumDS": nqaJitterStatsOWSumDS,
       "nqaJitterStatsOWDOverThresholdsDS": nqaJitterStatsOWDOverThresholdsDS,
       "nqaJitterStatsOperOfIcpif": nqaJitterStatsOperOfIcpif,
       "nqaJitterStatsOperOfMos": nqaJitterStatsOperOfMos,
       "nqaJitterStatsMinDelaySD": nqaJitterStatsMinDelaySD,
       "nqaJitterStatsSum2DelaySDLow": nqaJitterStatsSum2DelaySDLow,
       "nqaJitterStatsSum2DelaySDHigh": nqaJitterStatsSum2DelaySDHigh,
       "nqaJitterStatsMinDelayDS": nqaJitterStatsMinDelayDS,
       "nqaJitterStatsSum2DelayDSLow": nqaJitterStatsSum2DelayDSLow,
       "nqaJitterStatsSum2DelayDSHigh": nqaJitterStatsSum2DelayDSHigh,
       "nqaJitterStatsTimeUnit": nqaJitterStatsTimeUnit,
       "nqaJitterStatsAvgDelaySD": nqaJitterStatsAvgDelaySD,
       "nqaJitterStatsAvgDelayDS": nqaJitterStatsAvgDelayDS,
       "nqaJitterStatsPktRewriteNum": nqaJitterStatsPktRewriteNum,
       "nqaJitterStatsPktRewriteRatio": nqaJitterStatsPktRewriteRatio,
       "nqaJitterStatsPktDisorderNum": nqaJitterStatsPktDisorderNum,
       "nqaJitterStatsPktDisorderRatio": nqaJitterStatsPktDisorderRatio,
       "nqaJitterStatsFragPktDisorderNum": nqaJitterStatsFragPktDisorderNum,
       "nqaJitterStatsFragPktDisorderRatio": nqaJitterStatsFragPktDisorderRatio,
       "nqaFTPStatsTable": nqaFTPStatsTable,
       "nqaFTPStatsEntry": nqaFTPStatsEntry,
       "nqaFTPStatsIndex": nqaFTPStatsIndex,
       "nqaFTPStatsCompletions": nqaFTPStatsCompletions,
       "nqaFTPStatsRTDOverThresholds": nqaFTPStatsRTDOverThresholds,
       "nqaFTPStatsCtrlConnMaxTime": nqaFTPStatsCtrlConnMaxTime,
       "nqaFTPStatsCtrlConnMinTime": nqaFTPStatsCtrlConnMinTime,
       "nqaFTPStatsCtrlConnAveTime": nqaFTPStatsCtrlConnAveTime,
       "nqaFTPStatsDataConnMaxTime": nqaFTPStatsDataConnMaxTime,
       "nqaFTPStatsDataConnMinTime": nqaFTPStatsDataConnMinTime,
       "nqaFTPStatsDataConnAveTime": nqaFTPStatsDataConnAveTime,
       "nqaFTPStatsConnectSumTimeMax": nqaFTPStatsConnectSumTimeMax,
       "nqaFTPStatsConnectSumTimeMin": nqaFTPStatsConnectSumTimeMin,
       "nqaFTPStatsConnectSumTimeAve": nqaFTPStatsConnectSumTimeAve,
       "nqaFTPStatsMessageBodyOctetsSum": nqaFTPStatsMessageBodyOctetsSum,
       "nqaFTPStatsErrors": nqaFTPStatsErrors,
       "nqaFTPStatsTimeouts": nqaFTPStatsTimeouts,
       "nqaFTPStatsDiscontinued": nqaFTPStatsDiscontinued,
       "nqaFTPStatsProbeResponses": nqaFTPStatsProbeResponses,
       "nqaFTPStatsSendProbes": nqaFTPStatsSendProbes,
       "nqaFTPStatsTestFinished": nqaFTPStatsTestFinished,
       "nqaFTPStatsRttAvg": nqaFTPStatsRttAvg,
       "nqaFTPStatsLostPacketRatio": nqaFTPStatsLostPacketRatio,
       "nqaMpingStatsTable": nqaMpingStatsTable,
       "nqaMpingStatsEntry": nqaMpingStatsEntry,
       "nqaMpingStatsIndex": nqaMpingStatsIndex,
       "nqaMpingStatsReceiverIndex": nqaMpingStatsReceiverIndex,
       "nqaMpingStatsTargetAddressType": nqaMpingStatsTargetAddressType,
       "nqaMpingStatsTargetAddress": nqaMpingStatsTargetAddress,
       "nqaMpingStatsReceiverAddress": nqaMpingStatsReceiverAddress,
       "nqaMpingStatsCompletions": nqaMpingStatsCompletions,
       "nqaMpingStatsRTDOverThresholds": nqaMpingStatsRTDOverThresholds,
       "nqaMpingStatsSumCompletionTime": nqaMpingStatsSumCompletionTime,
       "nqaMpingStatsSumCompletionTime2Low": nqaMpingStatsSumCompletionTime2Low,
       "nqaMpingStatsSumCompletionTime2High": nqaMpingStatsSumCompletionTime2High,
       "nqaMpingStatsCompletionTimeMin": nqaMpingStatsCompletionTimeMin,
       "nqaMpingStatsCompletionTimeMax": nqaMpingStatsCompletionTimeMax,
       "nqaMpingStatsTimeouts": nqaMpingStatsTimeouts,
       "nqaMpingStatsBusies": nqaMpingStatsBusies,
       "nqaMpingStatsSequenceErrors": nqaMpingStatsSequenceErrors,
       "nqaMpingStatsDrops": nqaMpingStatsDrops,
       "nqaMpingStatsProbeResponses": nqaMpingStatsProbeResponses,
       "nqaMpingStatsSentProbes": nqaMpingStatsSentProbes,
       "nqaMpingStatsLastGoodProbe": nqaMpingStatsLastGoodProbe,
       "nqaMpingStatsTestFinished": nqaMpingStatsTestFinished,
       "nqaMpingStatsReceiverCount": nqaMpingStatsReceiverCount,
       "nqaMpingStatsLastFibHit": nqaMpingStatsLastFibHit,
       "nqaMpingStatsRttAvg": nqaMpingStatsRttAvg,
       "nqaMpingStatsLostPacketRatio": nqaMpingStatsLostPacketRatio,
       "nqaMtracertStatsTable": nqaMtracertStatsTable,
       "nqaMtracertStatsEntry": nqaMtracertStatsEntry,
       "nqaMtracertStatsIndex": nqaMtracertStatsIndex,
       "nqaMtracertStatsHopIndex": nqaMtracertStatsHopIndex,
       "nqaMtracertStatsAddressType": nqaMtracertStatsAddressType,
       "nqaMtracertStatsAddress": nqaMtracertStatsAddress,
       "nqaMtracertStatsCompletions": nqaMtracertStatsCompletions,
       "nqaMtracertStatsCurHopCount": nqaMtracertStatsCurHopCount,
       "nqaMtracertStatsCurProbeCount": nqaMtracertStatsCurProbeCount,
       "nqaMtracertStatsRTDOverThresholds": nqaMtracertStatsRTDOverThresholds,
       "nqaMtracertStatsTimeouts": nqaMtracertStatsTimeouts,
       "nqaMtracertStatsBusies": nqaMtracertStatsBusies,
       "nqaMtracertStatsSequenceErrors": nqaMtracertStatsSequenceErrors,
       "nqaMtracertStatsDrops": nqaMtracertStatsDrops,
       "nqaMtracertStatsProbeResponses": nqaMtracertStatsProbeResponses,
       "nqaMtracertStatsSentProbes": nqaMtracertStatsSentProbes,
       "nqaMtracertStatsLastGoodProbe": nqaMtracertStatsLastGoodProbe,
       "nqaMtracertStatsLastGoodPath": nqaMtracertStatsLastGoodPath,
       "nqaMtracertStatsTestFinished": nqaMtracertStatsTestFinished,
       "nqaMtracertStatsCurPathTTL": nqaMtracertStatsCurPathTTL,
       "nqaMtracertStatsMaxPathTTL": nqaMtracertStatsMaxPathTTL,
       "nqaMtracertStatsInPkgLossRate": nqaMtracertStatsInPkgLossRate,
       "nqaMtracertStatsSGPkgLossRate": nqaMtracertStatsSGPkgLossRate,
       "nqaMtracertStatsInPkgRate": nqaMtracertStatsInPkgRate,
       "nqaMtracertStatsOutPkgRate": nqaMtracertStatsOutPkgRate,
       "nqaMtracertStatsTimeDelay": nqaMtracertStatsTimeDelay,
       "nqaPathMtuStatsTable": nqaPathMtuStatsTable,
       "nqaPathMtuStatsEntry": nqaPathMtuStatsEntry,
       "nqaPathMtuStatsIndex": nqaPathMtuStatsIndex,
       "nqaPathMtuStatsAddressType": nqaPathMtuStatsAddressType,
       "nqaPathMtuStatsAddress": nqaPathMtuStatsAddress,
       "nqaPathMtuStatsCompletions": nqaPathMtuStatsCompletions,
       "nqaPathMtuStatsSentProbes": nqaPathMtuStatsSentProbes,
       "nqaPathMtuStatsProbeResponses": nqaPathMtuStatsProbeResponses,
       "nqaPathMtuStatsDiscoveryPathMtuMin": nqaPathMtuStatsDiscoveryPathMtuMin,
       "nqaPathMtuStatsDiscoveryPathMtuMax": nqaPathMtuStatsDiscoveryPathMtuMax,
       "nqaPathMtuStatsOptimumFirstStep": nqaPathMtuStatsOptimumFirstStep,
       "nqaPathMtuStatsBusies": nqaPathMtuStatsBusies,
       "nqaPathMtuStatsTimeouts": nqaPathMtuStatsTimeouts,
       "nqaPathMtuStatsDrops": nqaPathMtuStatsDrops,
       "nqaPathMtuStatsPathMtu": nqaPathMtuStatsPathMtu,
       "nqaPathMtuStatsTestFinished": nqaPathMtuStatsTestFinished,
       "nqaPathJitterStatsTable": nqaPathJitterStatsTable,
       "nqaPathJitterStatsEntry": nqaPathJitterStatsEntry,
       "nqaPathJitterStatsIndex": nqaPathJitterStatsIndex,
       "nqaPathJitterStatsHopIndex": nqaPathJitterStatsHopIndex,
       "nqaPathJitterStatsCompletions": nqaPathJitterStatsCompletions,
       "nqaPathJitterStatsAddressType": nqaPathJitterStatsAddressType,
       "nqaPathJitterStatsAddress": nqaPathJitterStatsAddress,
       "nqaPathJitterStatsRtdOverThresholds": nqaPathJitterStatsRtdOverThresholds,
       "nqaPathJitterStatsNumOfRtt": nqaPathJitterStatsNumOfRtt,
       "nqaPathJitterStatsRttSum": nqaPathJitterStatsRttSum,
       "nqaPathJitterStatsRttSum2Low": nqaPathJitterStatsRttSum2Low,
       "nqaPathJitterStatsRttSum2High": nqaPathJitterStatsRttSum2High,
       "nqaPathJitterStatsRttMin": nqaPathJitterStatsRttMin,
       "nqaPathJitterStatsRttMax": nqaPathJitterStatsRttMax,
       "nqaPathJitterStatsMinOfPositivesSD": nqaPathJitterStatsMinOfPositivesSD,
       "nqaPathJitterStatsMaxOfPositivesSD": nqaPathJitterStatsMaxOfPositivesSD,
       "nqaPathJitterStatsNumOfPositivesSD": nqaPathJitterStatsNumOfPositivesSD,
       "nqaPathJitterStatsSumOfPositivesSD": nqaPathJitterStatsSumOfPositivesSD,
       "nqaPathJitterStatsSum2OfPositivesSDLow": nqaPathJitterStatsSum2OfPositivesSDLow,
       "nqaPathJitterStatsSum2OfPositivesSDHigh": nqaPathJitterStatsSum2OfPositivesSDHigh,
       "nqaPathJitterStatsMinOfNegativesSD": nqaPathJitterStatsMinOfNegativesSD,
       "nqaPathJitterStatsMaxOfNegativesSD": nqaPathJitterStatsMaxOfNegativesSD,
       "nqaPathJitterStatsNumOfNegativesSD": nqaPathJitterStatsNumOfNegativesSD,
       "nqaPathJitterStatsSumOfNegativesSD": nqaPathJitterStatsSumOfNegativesSD,
       "nqaPathJitterStatsSum2OfNegativesSDLow": nqaPathJitterStatsSum2OfNegativesSDLow,
       "nqaPathJitterStatsSum2OfNegativesSDHigh": nqaPathJitterStatsSum2OfNegativesSDHigh,
       "nqaPathJitterStatsMinOfPositivesDS": nqaPathJitterStatsMinOfPositivesDS,
       "nqaPathJitterStatsMaxOfPositivesDS": nqaPathJitterStatsMaxOfPositivesDS,
       "nqaPathJitterStatsNumOfPositivesDS": nqaPathJitterStatsNumOfPositivesDS,
       "nqaPathJitterStatsSumOfPositivesDS": nqaPathJitterStatsSumOfPositivesDS,
       "nqaPathJitterStatsSum2OfPositivesDSLow": nqaPathJitterStatsSum2OfPositivesDSLow,
       "nqaPathJitterStatsSum2OfPositivesDSHigh": nqaPathJitterStatsSum2OfPositivesDSHigh,
       "nqaPathJitterStatsMinOfNegativesDS": nqaPathJitterStatsMinOfNegativesDS,
       "nqaPathJitterStatsMaxOfNegativesDS": nqaPathJitterStatsMaxOfNegativesDS,
       "nqaPathJitterStatsNumOfNegativesDS": nqaPathJitterStatsNumOfNegativesDS,
       "nqaPathJitterStatsSumOfNegativesDS": nqaPathJitterStatsSumOfNegativesDS,
       "nqaPathJitterStatsSum2OfNegativesDSLow": nqaPathJitterStatsSum2OfNegativesDSLow,
       "nqaPathJitterStatsSum2OfNegativesDSHigh": nqaPathJitterStatsSum2OfNegativesDSHigh,
       "nqaPathJitterStatsPacketLossSD": nqaPathJitterStatsPacketLossSD,
       "nqaPathJitterStatsPacketLossDS": nqaPathJitterStatsPacketLossDS,
       "nqaPathJitterStatsPacketOutOfSequences": nqaPathJitterStatsPacketOutOfSequences,
       "nqaPathJitterStatsErrors": nqaPathJitterStatsErrors,
       "nqaPathJitterStatsBusies": nqaPathJitterStatsBusies,
       "nqaPathJitterStatsTimeouts": nqaPathJitterStatsTimeouts,
       "nqaPathJitterStatsProbeResponses": nqaPathJitterStatsProbeResponses,
       "nqaPathJitterStatsSentProbes": nqaPathJitterStatsSentProbes,
       "nqaPathJitterStatsDrops": nqaPathJitterStatsDrops,
       "nqaPathJitterStatsTestFinished": nqaPathJitterStatsTestFinished,
       "nqaPathJitterStatsMaxDelaySD": nqaPathJitterStatsMaxDelaySD,
       "nqaPathJitterStatsMaxDelayDS": nqaPathJitterStatsMaxDelayDS,
       "nqaPathJitterStatsRttAvg": nqaPathJitterStatsRttAvg,
       "nqaPathJitterStatsPacketLossRatio": nqaPathJitterStatsPacketLossRatio,
       "nqaPathJitterStatsAvgJitter": nqaPathJitterStatsAvgJitter,
       "nqaPathJitterStatsAvgJitterSD": nqaPathJitterStatsAvgJitterSD,
       "nqaPathJitterStatsAvgJitterDS": nqaPathJitterStatsAvgJitterDS,
       "nqaPathJitterStatsJitterOut": nqaPathJitterStatsJitterOut,
       "nqaPathJitterStatsJitterIn": nqaPathJitterStatsJitterIn,
       "nqaPathJitterStatsOwdOverThresholdsSD": nqaPathJitterStatsOwdOverThresholdsSD,
       "nqaPathJitterStatsPktLossUnknown": nqaPathJitterStatsPktLossUnknown,
       "nqaPathJitterStatsNumOfOwd": nqaPathJitterStatsNumOfOwd,
       "nqaPathJitterStatsOwdSumSD": nqaPathJitterStatsOwdSumSD,
       "nqaPathJitterStatsOwdSumDS": nqaPathJitterStatsOwdSumDS,
       "nqaPathJitterStatsOwdOverThresholdsDS": nqaPathJitterStatsOwdOverThresholdsDS,
       "nqaPppoeStatsTable": nqaPppoeStatsTable,
       "nqaPppoeStatsEntry": nqaPppoeStatsEntry,
       "nqaPppoeStatsIndex": nqaPppoeStatsIndex,
       "nqaPppoeRedialIndex": nqaPppoeRedialIndex,
       "nqaPppoeStatsCompletions": nqaPppoeStatsCompletions,
       "nqaPppoeStatsCurrentPhase": nqaPppoeStatsCurrentPhase,
       "nqaPppoeStatsErrorMessage": nqaPppoeStatsErrorMessage,
       "nqaPppoeDiscoveryTimeout": nqaPppoeDiscoveryTimeout,
       "nqaPppoeLcpTimeout": nqaPppoeLcpTimeout,
       "nqaPppoeAuthorizationTimeout": nqaPppoeAuthorizationTimeout,
       "nqaPppoeNcpTimeout": nqaPppoeNcpTimeout,
       "nqaPppoeConnectionTime": nqaPppoeConnectionTime,
       "nqaPppoeClientSessionId": nqaPppoeClientSessionId,
       "nqaPppoeClientIpAddress": nqaPppoeClientIpAddress,
       "nqaPppoeGatewayIpAddress": nqaPppoeGatewayIpAddress,
       "nqaHistory": nqaHistory,
       "nqaHistoryTable": nqaHistoryTable,
       "nqaHistoryEntry": nqaHistoryEntry,
       "nqaHistoryIndex": nqaHistoryIndex,
       "nqaHistoryHopIndex": nqaHistoryHopIndex,
       "nqaHistoryProbeIndex": nqaHistoryProbeIndex,
       "nqaHistoryTimeStamp": nqaHistoryTimeStamp,
       "nqaHistoryAddressType": nqaHistoryAddressType,
       "nqaHistoryAddress": nqaHistoryAddress,
       "nqaHistoryCompletionTime": nqaHistoryCompletionTime,
       "nqaHistoryFinishState": nqaHistoryFinishState,
       "nqaHistoryLastRC": nqaHistoryLastRC,
       "nqaMpingHistoryTable": nqaMpingHistoryTable,
       "nqaMpingHistoryEntry": nqaMpingHistoryEntry,
       "nqaMpingHistoryIndex": nqaMpingHistoryIndex,
       "nqaMpingHistoryReceiverIndex": nqaMpingHistoryReceiverIndex,
       "nqaMpingHistoryResponseIndex": nqaMpingHistoryResponseIndex,
       "nqaMpingHistoryAddressType": nqaMpingHistoryAddressType,
       "nqaMpingHistoryAddress": nqaMpingHistoryAddress,
       "nqaMpingHistoryReceiverAddress": nqaMpingHistoryReceiverAddress,
       "nqaMpingHistoryTimeStamp": nqaMpingHistoryTimeStamp,
       "nqaMpingHistoryCompletionTime": nqaMpingHistoryCompletionTime,
       "nqaMpingHistoryFinishState": nqaMpingHistoryFinishState,
       "nqaMpingHistoryLastRC": nqaMpingHistoryLastRC,
       "nqaMpingHistoryFibHit": nqaMpingHistoryFibHit,
       "nqaMtracertHistoryTable": nqaMtracertHistoryTable,
       "nqaMtracertHistoryEntry": nqaMtracertHistoryEntry,
       "nqaMtracertHistoryIndex": nqaMtracertHistoryIndex,
       "nqaMtracertHistoryHopIndex": nqaMtracertHistoryHopIndex,
       "nqaMtracertHistoryAddressType": nqaMtracertHistoryAddressType,
       "nqaMtracertHistoryAddress": nqaMtracertHistoryAddress,
       "nqaMtracertHistoryTimeStamp": nqaMtracertHistoryTimeStamp,
       "nqaMtracertHistoryCompletionTime": nqaMtracertHistoryCompletionTime,
       "nqaMtracertHistoryLastRC": nqaMtracertHistoryLastRC,
       "nqaMtracertHistoryCurQueryMode": nqaMtracertHistoryCurQueryMode,
       "nqaMtracertHistoryQueryArrivalTime": nqaMtracertHistoryQueryArrivalTime,
       "nqaMtracertHistoryIncomingIfAddress": nqaMtracertHistoryIncomingIfAddress,
       "nqaMtracertHistoryOutgoingIfAddress": nqaMtracertHistoryOutgoingIfAddress,
       "nqaMtracertHistoryPreHopRouterAddress": nqaMtracertHistoryPreHopRouterAddress,
       "nqaMtracertHistoryInputPacketCount": nqaMtracertHistoryInputPacketCount,
       "nqaMtracertHistoryOutputPacketCount": nqaMtracertHistoryOutputPacketCount,
       "nqaMtracertHistoryTotalSGPacketCount": nqaMtracertHistoryTotalSGPacketCount,
       "nqaMtracertHistoryRtgProtocol": nqaMtracertHistoryRtgProtocol,
       "nqaMtracertHistoryFwdTTL": nqaMtracertHistoryFwdTTL,
       "nqaMtracertHistoryFwdCode": nqaMtracertHistoryFwdCode,
       "nqaMtracertHistroyFinishState": nqaMtracertHistroyFinishState,
       "nqaVplsMacTracertHistoryTable": nqaVplsMacTracertHistoryTable,
       "nqaVplsMacTracertHistoryEntry": nqaVplsMacTracertHistoryEntry,
       "nqaVplsMacTracertHistoryIndex": nqaVplsMacTracertHistoryIndex,
       "nqaVplsMacTracertHistoryHopIndex": nqaVplsMacTracertHistoryHopIndex,
       "nqaVplsMacTracertHistoryResponseIndex": nqaVplsMacTracertHistoryResponseIndex,
       "nqaVplsMacTracertHistoryTimeStamp": nqaVplsMacTracertHistoryTimeStamp,
       "nqaVplsMacTracertHistoryAddressType": nqaVplsMacTracertHistoryAddressType,
       "nqaVplsMacTracertHistoryAddress": nqaVplsMacTracertHistoryAddress,
       "nqaVplsMacTracertHistoryCompletionTime": nqaVplsMacTracertHistoryCompletionTime,
       "nqaVplsMacTracertHistoryFinishState": nqaVplsMacTracertHistoryFinishState,
       "nqaVplsMacTracertHistoryHitFlag": nqaVplsMacTracertHistoryHitFlag,
       "nqaVplsMacTracertHistoryDSCount": nqaVplsMacTracertHistoryDSCount,
       "nqaVplsMacTracertHistorySuccessPathNode": nqaVplsMacTracertHistorySuccessPathNode,
       "nqaVplsMacTracertHistoryDSTable": nqaVplsMacTracertHistoryDSTable,
       "nqaVplsMacTracertHistoryDSEntry": nqaVplsMacTracertHistoryDSEntry,
       "nqaVplsMacTracertHistoryDSIndex": nqaVplsMacTracertHistoryDSIndex,
       "nqaVplsMacTracertHistoryDSAddress": nqaVplsMacTracertHistoryDSAddress,
       "nqaVplsMTraceHistoryTable": nqaVplsMTraceHistoryTable,
       "nqaVplsMTraceHistoryEntry": nqaVplsMTraceHistoryEntry,
       "nqaVplsMTraceHistoryIndex": nqaVplsMTraceHistoryIndex,
       "nqaVplsMTraceHistoryHopIndex": nqaVplsMTraceHistoryHopIndex,
       "nqaVplsMTraceHistoryResponseIndex": nqaVplsMTraceHistoryResponseIndex,
       "nqaVplsMTraceHistoryResponserAddressType": nqaVplsMTraceHistoryResponserAddressType,
       "nqaVplsMTraceHistoryResponserAddress": nqaVplsMTraceHistoryResponserAddress,
       "nqaVplsMTraceHistoryUpStreamAddressType": nqaVplsMTraceHistoryUpStreamAddressType,
       "nqaVplsMTraceHistoryUpStreamAddress": nqaVplsMTraceHistoryUpStreamAddress,
       "nqaVplsMTraceHistoryReceivedTtl": nqaVplsMTraceHistoryReceivedTtl,
       "nqaVplsMTraceHistoryIGMPVersion": nqaVplsMTraceHistoryIGMPVersion,
       "nqaVplsMTraceHistoryIGMPSnpgEnable": nqaVplsMTraceHistoryIGMPSnpgEnable,
       "nqaVplsMTraceHistoryIGMPProxyEnable": nqaVplsMTraceHistoryIGMPProxyEnable,
       "nqaVplsMTraceHistoryIGMPRouterPortLearningEnable": nqaVplsMTraceHistoryIGMPRouterPortLearningEnable,
       "nqaVplsMTraceHistoryRequireRouterAlertEnable": nqaVplsMTraceHistoryRequireRouterAlertEnable,
       "nqaVplsMTraceHistoryForwardMode": nqaVplsMTraceHistoryForwardMode,
       "nqaVplsMTraceHistoryHitFlag": nqaVplsMTraceHistoryHitFlag,
       "nqaVplsMTraceHistoryPWExist": nqaVplsMTraceHistoryPWExist,
       "nqaVplsMTraceHistoryGroupPolicy": nqaVplsMTraceHistoryGroupPolicy,
       "nqaVplsMTraceHistoryCACExist": nqaVplsMTraceHistoryCACExist,
       "nqaVplsMTraceHistoryRcvQueryCount": nqaVplsMTraceHistoryRcvQueryCount,
       "nqaVplsMTraceHistoryRcvReportCount": nqaVplsMTraceHistoryRcvReportCount,
       "nqaVplsMTraceHistoryRcvLeaveCount": nqaVplsMTraceHistoryRcvLeaveCount,
       "nqaVplsMTraceHistoryTimeStamp": nqaVplsMTraceHistoryTimeStamp,
       "nqaVplsMTraceHistoryCompletionTime": nqaVplsMTraceHistoryCompletionTime,
       "nqaVplsMTraceHistoryLastRC": nqaVplsMTraceHistoryLastRC,
       "nqaVplsMTraceHistoryLastRSC": nqaVplsMTraceHistoryLastRSC,
       "nqaVplsMTraceHistoryFinishState": nqaVplsMTraceHistoryFinishState,
       "nqaVplsMTraceHistorySuccessPathNode": nqaVplsMTraceHistorySuccessPathNode,
       "nqaMacTraceHistoryTable": nqaMacTraceHistoryTable,
       "nqaMacTraceHistoryEntry": nqaMacTraceHistoryEntry,
       "nqaMacTraceHistoryIndex": nqaMacTraceHistoryIndex,
       "nqaMacTraceHistoryReceiveOrder": nqaMacTraceHistoryReceiveOrder,
       "nqaMacTraceHistoryTTL": nqaMacTraceHistoryTTL,
       "nqaMacTraceHistorySeqNumber": nqaMacTraceHistorySeqNumber,
       "nqaMacTraceHistoryCompletionTime": nqaMacTraceHistoryCompletionTime,
       "nqaMacTraceHistoryForwarded": nqaMacTraceHistoryForwarded,
       "nqaMacTraceHistoryTerminalMep": nqaMacTraceHistoryTerminalMep,
       "nqaMacTraceHistoryRelayAction": nqaMacTraceHistoryRelayAction,
       "nqaMacTraceHistoryIngressAction": nqaMacTraceHistoryIngressAction,
       "nqaMacTraceHistoryIngressMac": nqaMacTraceHistoryIngressMac,
       "nqaMacTraceHistoryIngressIfName": nqaMacTraceHistoryIngressIfName,
       "nqaMacTraceHistoryEgressAction": nqaMacTraceHistoryEgressAction,
       "nqaMacTraceHistoryEgressMac": nqaMacTraceHistoryEgressMac,
       "nqaMacTraceHistoryEgressIfName": nqaMacTraceHistoryEgressIfName,
       "nqaNotifications": nqaNotifications,
       "nqaResultsProbeFailed": nqaResultsProbeFailed,
       "nqaResultsTestFailed": nqaResultsTestFailed,
       "nqaResultsTestCompleted": nqaResultsTestCompleted,
       "nqaResultsThresholdNotification": nqaResultsThresholdNotification,
       "nqaHTTPStatsProbeFailed": nqaHTTPStatsProbeFailed,
       "nqaHTTPStatsTestFailed": nqaHTTPStatsTestFailed,
       "nqaHTTPStatsTestCompleted": nqaHTTPStatsTestCompleted,
       "nqaHTTPStatsThresholdNotification": nqaHTTPStatsThresholdNotification,
       "nqaJitterStatsProbeFailed": nqaJitterStatsProbeFailed,
       "nqaJitterStatsTestFailed": nqaJitterStatsTestFailed,
       "nqaJitterStatsTestCompleted": nqaJitterStatsTestCompleted,
       "nqaFTPStatsProbeFailed": nqaFTPStatsProbeFailed,
       "nqaFTPStatsTestFailed": nqaFTPStatsTestFailed,
       "nqaFTPStatsTestCompleted": nqaFTPStatsTestCompleted,
       "nqaFTPStatsThresholdNotification": nqaFTPStatsThresholdNotification,
       "nqaJitterStatsRTDThresholdNotification": nqaJitterStatsRTDThresholdNotification,
       "nqaJitterStatsOWDThresholdNotificationSD": nqaJitterStatsOWDThresholdNotificationSD,
       "nqaJitterStatsOWDThresholdNotificationDS": nqaJitterStatsOWDThresholdNotificationDS,
       "nqaNegotiateFailed": nqaNegotiateFailed,
       "nqaRisingAlarmNotification": nqaRisingAlarmNotification,
       "nqaFallingAlarmNotification": nqaFallingAlarmNotification,
       "nqaFtpSaveRecordNotification": nqaFtpSaveRecordNotification,
       "nqaPppoeStatsTestFailed": nqaPppoeStatsTestFailed,
       "nqaPppoeStatsTestCompleted": nqaPppoeStatsTestCompleted,
       "nqaConformance": nqaConformance,
       "nqaGroups": nqaGroups,
       "nqaBaseGroup": nqaBaseGroup,
       "nqaAdminGroup": nqaAdminGroup,
       "nqaServerGroup": nqaServerGroup,
       "nqaStatsGroup": nqaStatsGroup,
       "nqaHistoryGroup": nqaHistoryGroup,
       "nqaNotificationsGroup": nqaNotificationsGroup,
       "nqaCollectStatsGroup": nqaCollectStatsGroup,
       "nqaAlarmGroup": nqaAlarmGroup,
       "nqaFtpSaveRecordGroup": nqaFtpSaveRecordGroup,
       "nqaCompliances": nqaCompliances,
       "nqaCompliance": nqaCompliance,
       "nqaCollectStats": nqaCollectStats,
       "nqaJitterCollectStatsTable": nqaJitterCollectStatsTable,
       "nqaJitterCollectStatsEntry": nqaJitterCollectStatsEntry,
       "nqaJitterCollectStatsIndex": nqaJitterCollectStatsIndex,
       "nqaJitterCollectStatsCompletions": nqaJitterCollectStatsCompletions,
       "nqaJitterCollectStatsRTDOverThresholds": nqaJitterCollectStatsRTDOverThresholds,
       "nqaJitterCollectStatsOWDOverThresholdsSD": nqaJitterCollectStatsOWDOverThresholdsSD,
       "nqaJitterCollectStatsOWDOverThresholdsDS": nqaJitterCollectStatsOWDOverThresholdsDS,
       "nqaJitterCollectStatsNumOfRTT": nqaJitterCollectStatsNumOfRTT,
       "nqaJitterCollectStatsRTTSum": nqaJitterCollectStatsRTTSum,
       "nqaJitterCollectStatsRTTSum2Low": nqaJitterCollectStatsRTTSum2Low,
       "nqaJitterCollectStatsRTTSum2High": nqaJitterCollectStatsRTTSum2High,
       "nqaJitterCollectStatsRTTMin": nqaJitterCollectStatsRTTMin,
       "nqaJitterCollectStatsRTTMax": nqaJitterCollectStatsRTTMax,
       "nqaJitterCollectStatsMinOfPositivesSD": nqaJitterCollectStatsMinOfPositivesSD,
       "nqaJitterCollectStatsMaxOfPositivesSD": nqaJitterCollectStatsMaxOfPositivesSD,
       "nqaJitterCollectStatsNumOfPositivesSD": nqaJitterCollectStatsNumOfPositivesSD,
       "nqaJitterCollectStatsSumOfPositivesSD": nqaJitterCollectStatsSumOfPositivesSD,
       "nqaJitterCollectStatsSum2OfPositivesSDLow": nqaJitterCollectStatsSum2OfPositivesSDLow,
       "nqaJitterCollectStatsSum2OfPositivesSDHigh": nqaJitterCollectStatsSum2OfPositivesSDHigh,
       "nqaJitterCollectStatsMinOfNegativesSD": nqaJitterCollectStatsMinOfNegativesSD,
       "nqaJitterCollectStatsMaxOfNegativesSD": nqaJitterCollectStatsMaxOfNegativesSD,
       "nqaJitterCollectStatsNumOfNegativesSD": nqaJitterCollectStatsNumOfNegativesSD,
       "nqaJitterCollectStatsSumOfNegativesSD": nqaJitterCollectStatsSumOfNegativesSD,
       "nqaJitterCollectStatsSum2OfNegativesSDLow": nqaJitterCollectStatsSum2OfNegativesSDLow,
       "nqaJitterCollectStatsSum2OfNegativesSDHigh": nqaJitterCollectStatsSum2OfNegativesSDHigh,
       "nqaJitterCollectStatsMinOfPositivesDS": nqaJitterCollectStatsMinOfPositivesDS,
       "nqaJitterCollectStatsMaxOfPositivesDS": nqaJitterCollectStatsMaxOfPositivesDS,
       "nqaJitterCollectStatsNumOfPositivesDS": nqaJitterCollectStatsNumOfPositivesDS,
       "nqaJitterCollectStatsSumOfPositivesDS": nqaJitterCollectStatsSumOfPositivesDS,
       "nqaJitterCollectStatsSum2OfPositivesDSLow": nqaJitterCollectStatsSum2OfPositivesDSLow,
       "nqaJitterCollectStatsSum2OfPositivesDSHigh": nqaJitterCollectStatsSum2OfPositivesDSHigh,
       "nqaJitterCollectStatsMinOfNegativesDS": nqaJitterCollectStatsMinOfNegativesDS,
       "nqaJitterCollectStatsMaxOfNegativesDS": nqaJitterCollectStatsMaxOfNegativesDS,
       "nqaJitterCollectStatsNumOfNegativesDS": nqaJitterCollectStatsNumOfNegativesDS,
       "nqaJitterCollectStatsSumOfNegativesDS": nqaJitterCollectStatsSumOfNegativesDS,
       "nqaJitterCollectStatsSum2OfNegativesDSLow": nqaJitterCollectStatsSum2OfNegativesDSLow,
       "nqaJitterCollectStatsSum2OfNegativesDSHigh": nqaJitterCollectStatsSum2OfNegativesDSHigh,
       "nqaJitterCollectStatsMaxDelaySD": nqaJitterCollectStatsMaxDelaySD,
       "nqaJitterCollectStatsMaxDelayDS": nqaJitterCollectStatsMaxDelayDS,
       "nqaJitterCollectStatsNumOfOWD": nqaJitterCollectStatsNumOfOWD,
       "nqaJitterCollectStatsOWSumSD": nqaJitterCollectStatsOWSumSD,
       "nqaJitterCollectStatsOWSumDS": nqaJitterCollectStatsOWSumDS,
       "nqaJitterCollectStatsPacketLossSD": nqaJitterCollectStatsPacketLossSD,
       "nqaJitterCollectStatsPacketLossDS": nqaJitterCollectStatsPacketLossDS,
       "nqaJitterCollectStatsPacketLossUnknown": nqaJitterCollectStatsPacketLossUnknown,
       "nqaJitterCollectStatsPacketOutOfSequences": nqaJitterCollectStatsPacketOutOfSequences,
       "nqaJitterCollectStatsPacketLossRatio": nqaJitterCollectStatsPacketLossRatio,
       "nqaJitterCollectStatsErrors": nqaJitterCollectStatsErrors,
       "nqaJitterCollectStatsBusies": nqaJitterCollectStatsBusies,
       "nqaJitterCollectStatsTimeouts": nqaJitterCollectStatsTimeouts,
       "nqaJitterCollectStatsProbeResponses": nqaJitterCollectStatsProbeResponses,
       "nqaJitterCollectStatsSentProbes": nqaJitterCollectStatsSentProbes,
       "nqaJitterCollectStatsDrops": nqaJitterCollectStatsDrops,
       "nqaJitterCollectStatsRTTAvg": nqaJitterCollectStatsRTTAvg,
       "nqaJitterCollectStatsAvgJitter": nqaJitterCollectStatsAvgJitter,
       "nqaJitterCollectStatsAvgJitterSD": nqaJitterCollectStatsAvgJitterSD,
       "nqaJitterCollectStatsAvgJitterDS": nqaJitterCollectStatsAvgJitterDS,
       "nqaJitterCollectStatsJitterOut": nqaJitterCollectStatsJitterOut,
       "nqaJitterCollectStatsJitterIn": nqaJitterCollectStatsJitterIn,
       "nqaJitterCollectStatsMinDelaySD": nqaJitterCollectStatsMinDelaySD,
       "nqaJitterCollectStatsMinDelayDS": nqaJitterCollectStatsMinDelayDS,
       "nqaJitterCollectStatsAvgDelaySD": nqaJitterCollectStatsAvgDelaySD,
       "nqaJitterCollectStatsAvgDelayDS": nqaJitterCollectStatsAvgDelayDS,
       "nqaJitterCollectStatsPktRewriteNum": nqaJitterCollectStatsPktRewriteNum,
       "nqaJitterCollectStatsPktRewriteRatio": nqaJitterCollectStatsPktRewriteRatio,
       "nqaJitterCollectStatsPktDisorderNum": nqaJitterCollectStatsPktDisorderNum,
       "nqaJitterCollectStatsPktDisorderRatio": nqaJitterCollectStatsPktDisorderRatio,
       "nqaJitterCollectStatsFragPktDisorderNum": nqaJitterCollectStatsFragPktDisorderNum,
       "nqaJitterCollectStatsFragPktDisorderRatio": nqaJitterCollectStatsFragPktDisorderRatio,
       "nqaAlarm": nqaAlarm,
       "nqaMaxAlarmNum": nqaMaxAlarmNum,
       "nqaMaxEventNum": nqaMaxEventNum,
       "nqaAlarmTable": nqaAlarmTable,
       "nqaAlarmEntry": nqaAlarmEntry,
       "nqaAlarmIndex": nqaAlarmIndex,
       "nqaAlarmVariable": nqaAlarmVariable,
       "nqaAlarmSampleType": nqaAlarmSampleType,
       "nqaAlarmValue": nqaAlarmValue,
       "nqaAlarmStartUpNqaAlarm": nqaAlarmStartUpNqaAlarm,
       "nqaAlarmRisingThreshold": nqaAlarmRisingThreshold,
       "nqaAlarmFallingThreshold": nqaAlarmFallingThreshold,
       "nqaAlarmRisingEventIndex": nqaAlarmRisingEventIndex,
       "nqaAlarmFallingEventIndex": nqaAlarmFallingEventIndex,
       "nqaAlarmDescription": nqaAlarmDescription,
       "nqaAlarmStatus": nqaAlarmStatus,
       "nqaEventTable": nqaEventTable,
       "nqaEventEntry": nqaEventEntry,
       "nqaEventIndex": nqaEventIndex,
       "nqaEventType": nqaEventType,
       "nqaEventDescription": nqaEventDescription,
       "nqaEventAdminName": nqaEventAdminName,
       "nqaEventOperationTag": nqaEventOperationTag,
       "nqaEventStatus": nqaEventStatus,
       "nqaSaveRecord": nqaSaveRecord,
       "nqaFtpSaveRecordEnable": nqaFtpSaveRecordEnable,
       "nqaFtpSaveRecordIpAddr": nqaFtpSaveRecordIpAddr,
       "nqaFtpSaveRecordVrfName": nqaFtpSaveRecordVrfName,
       "nqaFtpSaveRecordUserName": nqaFtpSaveRecordUserName,
       "nqaFtpSaveRecordPassword": nqaFtpSaveRecordPassword,
       "nqaFtpSaveRecordFileName": nqaFtpSaveRecordFileName,
       "nqaFtpSaveRecordItemNum": nqaFtpSaveRecordItemNum,
       "nqaFtpSaveRecordTime": nqaFtpSaveRecordTime,
       "nqaFtpSaveRecordNotificationEnable": nqaFtpSaveRecordNotificationEnable,
       "nqaFtpSaveRecordLastFileName": nqaFtpSaveRecordLastFileName}
)
