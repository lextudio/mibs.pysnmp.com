# SNMP MIB module (TIMETRA-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:33 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(timetraModules,) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraModules")


# MODULE-IDENTITY

timetraTCMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 2)
)
timetraTCMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-23 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1901-05-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class TmnxPortID(Unsigned32, TextualConvention):
    status = "current"


class TmnxEncapVal(Unsigned32, TextualConvention):
    status = "current"


class QTag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class QTagOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



class QTagFullRange(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class QTagFullRangeOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4095),
    )



class TmnxStrSapId(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class IpAddressPrefixLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )



class TmnxActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doAction", 1),
          ("notApplicable", 2))
    )



class TmnxAdminState(Integer32, TextualConvention):
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
        *(("inService", 2),
          ("noop", 1),
          ("outOfService", 3))
    )



class TmnxOperState(Integer32, TextualConvention):
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
        *(("inService", 2),
          ("outOfService", 3),
          ("transition", 4),
          ("unknown", 1))
    )



class TmnxStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )



class TmnxEnabledDisabled(Integer32, TextualConvention):
    status = "current"
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



class TmnxEnabledDisabledOrInherit(Integer32, TextualConvention):
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
        *(("disabled", 2),
          ("enabled", 1),
          ("inherit", 3))
    )



class TNamedItem(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TNamedItemOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )



class TLNamedItem(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class TLNamedItemOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )



class TItemDescription(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class TItemLongDescription(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )



class TmnxVRtrID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240),
    )



class TmnxVRtrIDOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240),
    )



class TmnxBgpAutonomousSystem(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxBgpLocalPreference(Unsigned32, TextualConvention):
    status = "current"


class TmnxBgpPreference(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxCustId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class BgpPeeringStatus(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("duplicatePeer", 10),
          ("genError", 12),
          ("hostInactive", 6),
          ("installed", 1),
          ("invalidRadiusAttr", 8),
          ("maxPeersReached", 11),
          ("noDualHomingSupport", 7),
          ("noDynamicPeerGroup", 9),
          ("noEnhancedSubmgt", 3),
          ("notApplicable", 0),
          ("notInstalled", 2),
          ("parentItfDown", 5),
          ("wrongAntiSpoof", 4))
    )



class TmnxServId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
        ValueRangeConstraint(2147483648, 2147483648),
        ValueRangeConstraint(2147483649, 2147483649),
        ValueRangeConstraint(2147483650, 2147483650),
    )



class ServiceAdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class ServiceOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class TPolicyID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
        ValueRangeConstraint(65536, 65536),
        ValueRangeConstraint(65537, 65537),
    )



class TTmplPolicyID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TSapIngressPolicyID(TPolicyID, TextualConvention):
    status = "current"


class TSapEgressPolicyID(TPolicyID, TextualConvention):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(65536, 65536),
        ValueRangeConstraint(65537, 65537),
    )



class TSdpIngressPolicyID(TPolicyID, TextualConvention):
    status = "current"


class TSdpEgressPolicyID(TPolicyID, TextualConvention):
    status = "current"


class TQosQGrpInstanceIDorZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxTransitIpPolicyId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxTransitIpPolicyIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxTransPrefPolicyId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxTransPrefPolicyIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxAarpId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxAarpIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TmnxBsxAarpServiceRefType(Integer32, TextualConvention):
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
        *(("dualHomed", 1),
          ("none", 0),
          ("shuntNetworkSide", 3),
          ("shuntSubscriberSide", 2))
    )



class TSapEgrEncapGrpQosPolicyIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TSapEgrEncapGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("isid", 1)
    )



class TSapEgrEncapGroupActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("destroy", 2))
    )



class TPerPacketOffset(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, 31),
    )



class TPerPacketOffsetOvr(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -128),
        ValueRangeConstraint(-32, 31),
    )



class TIngressHsmdaPerPacketOffset(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, 31),
    )



class TEgressQPerPacketOffset(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-64, 32),
    )



class TIngHsmdaPerPacketOffsetOvr(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -128),
        ValueRangeConstraint(-32, 31),
    )



class TEgressHsmdaPerPacketOffset(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, 31),
    )



class THsmdaCounterIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class THsmdaCounterIdOrZeroOrAll(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TEgrHsmdaPerPacketOffsetOvr(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -128),
        ValueRangeConstraint(-32, 31),
    )



class TIngressHsmdaCounterId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TIngressHsmdaCounterIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TEgressHsmdaCounterId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TEgressHsmdaCounterIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TEgrRateModType(Integer32, TextualConvention):
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
        *(("aggRateLimit", 2),
          ("namedScheduler", 3),
          ("none", 1))
    )



class TPolicyStatementNameOrEmpty(TNamedItemOrEmpty, TextualConvention):
    status = "current"


class TmnxVcType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10,
              11,
              17,
              18,
              19,
              20,
              21,
              23,
              25,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("atmCell", 3),
          ("atmSdu", 2),
          ("atmVccCell", 9),
          ("atmVpcCell", 10),
          ("cesopsn", 21),
          ("cesopsnCas", 23),
          ("ethernet", 5),
          ("ethernetVlan", 4),
          ("frDlci", 25),
          ("frDlciMartini", 1),
          ("ipipe", 11),
          ("mirrorDest", 4096),
          ("satopE1", 17),
          ("satopE3", 19),
          ("satopT1", 18),
          ("satopT3", 20))
    )



class TmnxVcId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxVcIdOrNone(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class Dot1PPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class Dot1PPriorityMask(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class ServiceAccessPoint(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TLspExpValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class TIpProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TIpOption(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TTcpUdpPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class TOperator(Integer32, TextualConvention):
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
        *(("eq", 1),
          ("gt", 4),
          ("lt", 3),
          ("none", 0),
          ("range", 2))
    )



class TTcpUdpPortOperator(TOperator, TextualConvention):
    status = "current"


class TFrameType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("atm", 5),
          ("e802dot2LLC", 1),
          ("e802dot2SNAP", 2),
          ("e802dot3", 0),
          ("ethernetII", 3))
    )



class TQueueId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TQueueIdOrAll(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TIngressQueueId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TIngressMeterId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TSapIngressMeterId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TNetworkIngressMeterId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )



class TEgressQueueId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TIngressHsmdaQueueId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TEgressHsmdaQueueId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class THsmdaSchedulerPolicyGroupId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2),
    )



class THsmdaPolicyIncludeQueues(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("q1to2", 1),
          ("q1to3", 2))
    )



class THsmdaPolicyScheduleClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



class TDSCPName(TNamedItem, TextualConvention):
    status = "current"


class TDSCPNameOrEmpty(TNamedItemOrEmpty, TextualConvention):
    status = "current"


class TDSCPValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class TDSCPValueOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )



class TDSCPFilterActionValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TFCName(TNamedItem, TextualConvention):
    status = "current"


class TFCNameOrEmpty(TNamedItemOrEmpty, TextualConvention):
    status = "current"


class TFCSet(Bits, TextualConvention):
    status = "current"


class TFCType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("af", 2),
          ("be", 0),
          ("ef", 5),
          ("h1", 6),
          ("h2", 4),
          ("l1", 3),
          ("l2", 1),
          ("nc", 7))
    )



class TmnxTunnelType(Integer32, TextualConvention):
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
        *(("bgp", 7),
          ("bypass", 5),
          ("gre", 4),
          ("invalid", 6),
          ("ldp", 2),
          ("rsvp", 3),
          ("sdp", 1))
    )



class TmnxTunnelID(Unsigned32, TextualConvention):
    status = "current"


class TmnxBgpRouteTarget(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxVPNRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class SdpBindId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class TmnxVRtrMplsLspID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TPortSchedulerPIR(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class TPortSchedulerPIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 400000000),
    )



class TPortSchedulerCIR(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 400000000),
    )



class TWeight(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TNonZeroWeight(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TPolicerWeight(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class THsmdaWeight(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class THsmdaWrrWeight(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class THsmdaWeightClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("class1", 1),
          ("class2", 2),
          ("class4", 4),
          ("class8", 8))
    )



class THsmdaWeightOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(1, 100),
    )



class THsmdaWrrWeightOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(1, 32),
    )



class TCIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class THPolCIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 20000000),
    )



class TRateType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("percent", 2))
    )



class TBWRateType(Integer32, TextualConvention):
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
        *(("kbps", 1),
          ("percentLocalLimit", 3),
          ("percentPortLimit", 2))
    )



class TPolicerRateType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("percentLocalLimit", 2))
    )



class TCIRRateOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class THPolCIRRateOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 20000000),
    )



class TCIRPercentOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 10000),
    )



class THsmdaCIRKRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class THsmdaCIRKRateOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class THsmdaCIRMRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000),
    )



class THsmdaCIRMRateOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000),
    )



class TPIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class THPolVirtualSchePIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 800000000),
    )



class THPolVirtualScheCIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 800000000),
    )



class TAdvCfgRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )



class TMaxDecRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100000000),
    )



class THPolPIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 20000000),
    )



class TSecondaryShaper10GPIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000),
    )



class TExpSecondaryShaperPIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )



class TExpSecondaryShaperClassRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )



class TPIRRateOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class THPolPIRRateOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 20000000),
    )



class TPIRPercentOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(1, 10000),
    )



class TPIRRateOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )



class THsmdaPIRKRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class THsmdaPIRKRateOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class THsmdaPIRMRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000),
    )



class THsmdaPIRMRateOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000),
    )



class TmnxDHCP6MsgType(Integer32, TextualConvention):
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("dhcp6MsgTypeAdvertise", 2),
          ("dhcp6MsgTypeConfirm", 4),
          ("dhcp6MsgTypeDecline", 9),
          ("dhcp6MsgTypeInfoRequest", 11),
          ("dhcp6MsgTypeMaxValue", 14),
          ("dhcp6MsgTypeRebind", 6),
          ("dhcp6MsgTypeReconfigure", 10),
          ("dhcp6MsgTypeRelayForw", 12),
          ("dhcp6MsgTypeRelayReply", 13),
          ("dhcp6MsgTypeRelease", 8),
          ("dhcp6MsgTypeRenew", 5),
          ("dhcp6MsgTypeReply", 7),
          ("dhcp6MsgTypeRequest", 3),
          ("dhcp6MsgTypeSolicit", 1))
    )



class TmnxOspfInstance(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )



class TmnxBGPFamilyType(Bits, TextualConvention):
    status = "current"


class TmnxIgmpGroupFilterMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )



class TmnxIgmpGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )



class TmnxIgmpVersion(Integer32, TextualConvention):
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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3))
    )



class TmnxMldGroupFilterMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )



class TmnxMldGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )



class TmnxMldVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )



class TmnxManagedRouteStatus(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("deprecated1", 9),
          ("enhancedSubMgmtRequired", 8),
          ("hostInactive", 7),
          ("installed", 0),
          ("l2AwNotSupported", 10),
          ("notYetInstalled", 1),
          ("outOfMemory", 3),
          ("parentInterfaceDown", 6),
          ("routeTableFull", 5),
          ("shadowed", 4),
          ("wrongAntiSpoofType", 2))
    )



class TmnxAncpString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class TmnxAncpStringOrZero(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class TmnxMulticastAddrFamily(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Multicast", 0),
          ("ipv6Multicast", 1))
    )



class TmnxAsciiSpecification(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TmnxMacSpecification(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )



class TmnxBinarySpecification(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TmnxDefSubIdSource(Integer32, TextualConvention):
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
        *(("useAutoId", 3),
          ("useSapId", 1),
          ("useString", 2))
    )



class TmnxSubIdentString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxSubIdentStringOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxSubRadServAlgorithm(Integer32, TextualConvention):
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
        *(("direct", 1),
          ("hashBased", 3),
          ("roundRobin", 2))
    )



class TmnxSubRadiusAttrType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxSubRadiusVendorId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class TmnxRadiusPendingReqLimit(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class TmnxRadiusServerOperState(Integer32, TextualConvention):
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
        *(("inService", 2),
          ("outOfService", 3),
          ("overloaded", 5),
          ("transition", 4),
          ("unknown", 1))
    )



class TmnxSubProfileString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TmnxSubProfileStringOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxSlaProfileString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TmnxSlaProfileStringOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxAppProfileString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class TmnxAppProfileStringOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxSubMgtIntDestIdOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxSubMgtIntDestId(TmnxSubMgtIntDestIdOrEmpty, TextualConvention):
    status = "current"
    subtypeSpec = TmnxSubMgtIntDestIdOrEmpty.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxDefInterDestIdSource(Integer32, TextualConvention):
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
        *(("useString", 1),
          ("useTopQTag", 2),
          ("useVpi", 3))
    )



class TmnxSubNasPortSuffixType(Integer32, TextualConvention):
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
        *(("circuitId", 1),
          ("none", 0),
          ("remoteId", 2))
    )



class TmnxSubNasPortPrefixType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("userString", 1))
    )



class TmnxSubNasPortTypeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("standard", 1))
    )



class TmnxSubMgtOrgStrOrZero(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxSubMgtOrgString(TmnxSubMgtOrgStrOrZero, TextualConvention):
    status = "current"
    subtypeSpec = TmnxSubMgtOrgStrOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class TmnxFilterProfileStringOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TmnxAccessLoopEncapDataLink(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 0),
          ("ethernet", 1))
    )



class TmnxAccessLoopEncaps1(Integer32, TextualConvention):
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
        *(("notAvailable", 0),
          ("singleTaggedEthernet", 2),
          ("untaggedEthernet", 1))
    )



class TmnxAccessLoopEncaps2(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernetOverAal5LlcFcs", 5),
          ("ethernetOverAal5LlcNoFcs", 6),
          ("ethernetOverAal5NullFcs", 7),
          ("ethernetOverAal5NullNoFcs", 8),
          ("ipoaLlc", 3),
          ("ipoaNull", 4),
          ("notAvailable", 0),
          ("pppoaLlc", 1),
          ("pppoaNull", 2))
    )



class TmnxSubAleOffsetMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("none", 0))
    )



class TmnxSubAleOffset(Integer32, TextualConvention):
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("ipoaLlc", 11),
          ("ipoaNull", 12),
          ("ipoe", 23),
          ("ipoeTagged", 24),
          ("ipoeoaLlc", 13),
          ("ipoeoaLlcFcs", 14),
          ("ipoeoaLlcTagged", 15),
          ("ipoeoaLlcTaggedFcs", 16),
          ("ipoeoaNull", 17),
          ("ipoeoaNullFcs", 18),
          ("ipoeoaNullTagged", 19),
          ("ipoeoaNullTaggedFcs", 20),
          ("none", 0),
          ("pppoaLlc", 1),
          ("pppoaNull", 2),
          ("pppoe", 21),
          ("pppoeTagged", 22),
          ("pppoeoaLlc", 3),
          ("pppoeoaLlcFcs", 4),
          ("pppoeoaLlcTagged", 5),
          ("pppoeoaLlcTaggedFcs", 6),
          ("pppoeoaNull", 7),
          ("pppoeoaNullFcs", 8),
          ("pppoeoaNullTagged", 9),
          ("pppoeoaNullTaggedFcs", 10))
    )



class TmnxDhcpOptionType(Integer32, TextualConvention):
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
        *(("ascii", 2),
          ("domain", 5),
          ("hex", 3),
          ("ipv4", 1),
          ("ipv6", 4))
    )



class TmnxPppoeUserName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class TmnxPppoeUserNameOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class TCpmProtPolicyID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TCpmProtPolicyIDOrDefault(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )



class TMlpppQoSProfileId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TMcFrQoSProfileId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxPppoeSessionId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxPppoePadoDelay(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 30),
    )



class TmnxPppoeSessionInfoOrigin(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("dhcp", 4),
          ("l2tp", 7),
          ("localUserDb", 3),
          ("midSessionChange", 5),
          ("none", 0),
          ("radius", 2),
          ("tags", 6))
    )



class TmnxPppoeSessionType(Integer32, TextualConvention):
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
        *(("l2tp", 4),
          ("local", 1),
          ("localRetail", 3),
          ("localWholesale", 2))
    )



class TmnxPppNcpProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipcp", 1),
          ("ipv6cp", 2))
    )



class TmnxMlpppEpClass(Integer32, TextualConvention):
    status = "current"
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
        *(("directoryNumber", 5),
          ("ipv4Address", 2),
          ("local", 1),
          ("macAddress", 3),
          ("magicNumber", 4),
          ("null", 0))
    )



class TNetworkPolicyID(TPolicyID, TextualConvention):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(65536, 65536),
        ValueRangeConstraint(65537, 65537),
    )



class TItemScope(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 1),
          ("template", 2))
    )



class TItemMatch(Integer32, TextualConvention):
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
        *(("false", 2),
          ("off", 1),
          ("true", 3))
    )



class TPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )



class TPriorityOrDefault(Integer32, TextualConvention):
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
        *(("default", 3),
          ("high", 2),
          ("low", 1))
    )



class TProfileUseDEOrNone(Integer32, TextualConvention):
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
        *(("de", 3),
          ("in", 1),
          ("none", 0),
          ("out", 2))
    )



class TPriorityOrUndefined(Integer32, TextualConvention):
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
        *(("high", 2),
          ("low", 1),
          ("undefined", 0))
    )



class TProfile(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )



class TProfileOrDei(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              13)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("use-dei", 13))
    )



class TDEProfile(Integer32, TextualConvention):
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
        *(("de", 3),
          ("in", 1),
          ("out", 2))
    )



class TDEProfileOrDei(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              13)
        )
    )
    namedValues = NamedValues(
        *(("de", 3),
          ("in", 1),
          ("out", 2),
          ("use-dei", 13))
    )



class TProfileOrNone(Integer32, TextualConvention):
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
        *(("in", 1),
          ("none", 0),
          ("out", 2))
    )



class TAdaptationRule(Integer32, TextualConvention):
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
        *(("closest", 3),
          ("max", 1),
          ("min", 2))
    )



class TAdaptationRuleOverride(Integer32, TextualConvention):
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
        *(("closest", 3),
          ("max", 1),
          ("min", 2),
          ("noOverride", 0))
    )



class TRemarkType(Integer32, TextualConvention):
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
        *(("dscp", 2),
          ("none", 1),
          ("precedence", 3))
    )



class TPrecValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TPrecValueOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class TBurstSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 131072),
    )



class TBurstSizeOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 131072),
    )



class TBurstPercent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TBurstHundredthsOfPercent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class TBurstPercentOrDefault(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )



class TBurstPercentOrDefaultOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )



class TRatePercent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TPIRRatePercent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TLevelOrDefault(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TQWeight(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )



class TMeterMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priority", 1),
          ("profile", 2))
    )



class TPlcyMode(Integer32, TextualConvention):
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
        *(("none", 0),
          ("roundRobin", 1),
          ("weightedDeficitRoundRobin", 3),
          ("weightedRoundRobin", 2))
    )



class TPlcyQuanta(Integer32, TextualConvention):
    status = "current"


class TQueueMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priority", 1),
          ("profile", 2))
    )



class TEntryIndicator(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TEntryId(TEntryIndicator, TextualConvention):
    status = "current"
    subtypeSpec = TEntryIndicator.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TMatchCriteria(Integer32, TextualConvention):
    status = "current"
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
        *(("dot1p", 5),
          ("dscp", 4),
          ("ip", 1),
          ("mac", 2),
          ("none", 3),
          ("prec", 6))
    )



class TmnxMdaQos(Integer32, TextualConvention):
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
        *(("hsmda1", 2),
          ("hsmda2", 3),
          ("mda", 1),
          ("unknown", 0))
    )



class TAtmTdpDescrType(Integer32, TextualConvention):
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
        *(("clp0And1pcr", 0),
          ("clp0And1pcrPlusClp0And1scr", 1),
          ("clp0And1pcrPlusClp0scr", 2),
          ("clp0And1pcrPlusClp0scrTag", 3))
    )



class TDEValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1),
    )



class TQGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("port", 0),
          ("vpls", 1))
    )



class TQosOverrideType(Integer32, TextualConvention):
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
        *(("aggRateLimit", 3),
          ("arbiter", 4),
          ("policer", 2),
          ("queue", 1),
          ("scheduler", 5))
    )



class TmnxIPsecTunnelTemplateId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )



class TmnxIPsecTunnelTemplateIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )



class TmnxIpSecIsaOperFlags(Bits, TextualConvention):
    status = "current"


class TmnxIkePolicyAuthMethod(Integer32, TextualConvention):
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
        *(("cert", 5),
          ("hybridX509XAuth", 2),
          ("plainPskXAuth", 4),
          ("plainX509XAuth", 3),
          ("psk", 1))
    )



class TmnxIkePolicyOwnAuthMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cert", 5),
          ("psk", 1),
          ("symmetric", 0))
    )



class TmnxRsvpDSTEClassType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TmnxAccPlcyQICounters(Bits, TextualConvention):
    status = "current"


class TmnxAccPlcyQECounters(Bits, TextualConvention):
    status = "current"


class TmnxAccPlcyOICounters(Bits, TextualConvention):
    status = "current"


class TmnxAccPlcyOECounters(Bits, TextualConvention):
    status = "current"


class TmnxAccPlcyAACounters(Bits, TextualConvention):
    status = "current"


class TmnxVdoGrpIdIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class TmnxVdoGrpId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class TmnxVdoGrpIdOrInherit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4),
    )



class TmnxVdoFccServerMode(Integer32, TextualConvention):
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
        *(("burst", 1),
          ("dent", 2),
          ("hybrid", 3),
          ("none", 0))
    )



class TmnxVdoPortNumber(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 5999),
        ValueRangeConstraint(6251, 65535),
    )



class TmnxVdoIfName(TNamedItem, TextualConvention):
    status = "current"


class TmnxTimeInSec(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )



class TmnxMobProfName(TNamedItem, TextualConvention):
    status = "current"


class TmnxMobProfNameOrEmpty(TNamedItemOrEmpty, TextualConvention):
    status = "current"


class TmnxMobProfIpTtl(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxMobDiaTransTimer(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )



class TmnxMobDiaRetryCount(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )



class TmnxMobDiaPeerHost(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class TmnxMobGwId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TmnxMobNode(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



class TmnxMobBufferLimit(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 12000),
    )



class TmnxMobQueueLimit(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 12000),
    )



class TmnxMobRtrAdvtInterval(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )



class TmnxMobRtrAdvtLifeTime(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )



class TmnxMobAddrScheme(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateful", 1),
          ("stateless", 2))
    )



class TmnxMobQciValue(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )



class TmnxMobQciValueOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )



class TmnxMobArpValue(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class TmnxMobArpValueOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class TmnxMobApn(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )



class TmnxMobApnOrZero(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class TmnxMobImsi(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class TmnxMobMsisdn(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )



class TmnxMobImei(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )



class TmnxMobNai(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 72),
    )



class TmnxMobMcc(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TmnxMobMnc(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(3, 3),
    )



class TmnxMobMccOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 3),
    )



class TmnxMobMncOrEmpty(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(3, 3),
    )



class TmnxMobUeState(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 2),
          ("ddnDamp", 6),
          ("idle", 1),
          ("init", 4),
          ("paging", 3),
          ("suspend", 5))
    )



class TmnxMobUeRat(Integer32, TextualConvention):
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
        *(("ehrpd", 7),
          ("eutran", 6),
          ("gan", 4),
          ("geran", 2),
          ("hrpd", 8),
          ("hspa", 5),
          ("oneXrtt", 9),
          ("umb", 10),
          ("utran", 1),
          ("wlan", 3))
    )



class TmnxMobUeSubType(Integer32, TextualConvention):
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
        *(("homer", 1),
          ("roamer", 2),
          ("visitor", 3))
    )



class TmnxMobPdnType(Integer32, TextualConvention):
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
        *(("ipv4", 1),
          ("ipv4v6", 3),
          ("ipv6", 2))
    )



class TmnxMobPgwSigProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gtp", 1),
          ("pmip", 2))
    )



class TmnxMobPdnSessionState(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("connected", 5),
          ("dlDelPending", 7),
          ("dlHandover", 10),
          ("idleMode", 8),
          ("incomingHandover", 11),
          ("init", 1),
          ("invalid", 0),
          ("outgoingHandover", 12),
          ("pageMode", 9),
          ("stateMax", 13),
          ("ulDelPending", 6),
          ("waitEnodebUpdate", 4),
          ("waitPcrfResponse", 2),
          ("waitPgwResponse", 3))
    )



class TmnxMobPdnSessionEvent(Integer32, TextualConvention):
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("dlPktNotificationAck", 13),
          ("dlPktNotificationFail", 14),
          ("dlPktRecvIndication", 12),
          ("eventMax", 22),
          ("gtpCreateSessReq", 1),
          ("gtpDeleteBearerResp", 4),
          ("gtpDeleteSessReq", 3),
          ("gtpModifyActiveToIdle", 6),
          ("gtpModifyQosCmd", 8),
          ("gtpResrcAllocCmd", 7),
          ("gtpS1CreateIndirectTunnel", 11),
          ("gtpUpdateBearerReq", 2),
          ("gtpUpdateBearerResp", 5),
          ("gtpX1eNodeBTeidUpdate", 9),
          ("gtpX2SrcSgwDeleteSessReq", 10),
          ("pcrfProvQosRules", 17),
          ("pcrfSessEstResp", 15),
          ("pcrfSessTerminateRsp", 16),
          ("pmipSessDeleteReq", 21),
          ("pmipSessDeleteRsp", 20),
          ("pmipSessResp", 18),
          ("pmipSessUpdate", 19),
          ("sessionInvalid", 0))
    )



class TmnxMobBearerId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class TmnxMobBearerType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 2),
          ("default", 1))
    )



class TmnxMobQci(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )



class TmnxMobArp(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class TmnxMobSdf(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxMobSdfFilter(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class TmnxMobSdfFilterNum(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class TmnxMobSdfRuleName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class TmnxMobSdfFilterDirection(Integer32, TextualConvention):
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
        *(("biDir", 3),
          ("downLink", 1),
          ("preRel7", 0),
          ("upLink", 2))
    )



class TmnxMobSdfFilterProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
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
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140)
        )
    )
    namedValues = NamedValues(
        *(("activeNet", 107),
          ("ah", 51),
          ("any", -1),
          ("any0hop", 114),
          ("anyDFS", 68),
          ("anyHostIntl", 61),
          ("anyLocalNet", 63),
          ("anyPEC", 99),
          ("argus", 13),
          ("aris", 104),
          ("ax25", 93),
          ("bbnRccMon", 10),
          ("bna", 49),
          ("brSatMon", 76),
          ("cbt", 7),
          ("cftp", 62),
          ("chaos", 16),
          ("compaqPeer", 110),
          ("cphb", 73),
          ("cpnx", 72),
          ("crtp", 126),
          ("crudp", 127),
          ("dccp", 33),
          ("dcnMeas", 19),
          ("ddp", 37),
          ("ddx", 116),
          ("dgp", 86),
          ("dsr", 48),
          ("egp", 8),
          ("eiGrp", 88),
          ("emcon", 14),
          ("encap", 98),
          ("esp", 50),
          ("etherIp", 97),
          ("fc", 133),
          ("fire", 125),
          ("ggp", 3),
          ("gmtp", 100),
          ("gre", 47),
          ("hip", 139),
          ("hmp", 20),
          ("iNlsp", 52),
          ("iatp", 117),
          ("icmp", 1),
          ("idpr", 35),
          ("idprCmtp", 38),
          ("idrp", 45),
          ("ifmp", 101),
          ("igmp", 2),
          ("igp", 9),
          ("il", 40),
          ("ip", 4),
          ("ipComp", 108),
          ("ipcv", 71),
          ("ipip", 94),
          ("iplt", 129),
          ("ippc", 67),
          ("ipv6", 41),
          ("ipv6Frag", 44),
          ("ipv6HopByOpOpt", 0),
          ("ipv6Icmp", 58),
          ("ipv6NoNxt", 59),
          ("ipv6Opts", 60),
          ("ipv6Route", 43),
          ("ipxInIp", 111),
          ("irdp", 28),
          ("isis", 124),
          ("isoIp", 80),
          ("isoTp4", 29),
          ("kryptolan", 65),
          ("l2tp", 115),
          ("larp", 91),
          ("leaf1", 25),
          ("leaf2", 26),
          ("manet", 138),
          ("meritInp", 32),
          ("mfeNsp", 31),
          ("micp", 95),
          ("mobHeader", 135),
          ("mobile", 55),
          ("mplsInIp", 137),
          ("mtp", 92),
          ("mux", 18),
          ("narp", 54),
          ("netblt", 30),
          ("nsfnetIgp", 85),
          ("nvp2", 11),
          ("ospfIgp", 89),
          ("pc3", 34),
          ("pgm", 113),
          ("pim", 103),
          ("pipe", 131),
          ("pnni", 102),
          ("prm", 21),
          ("ptp", 123),
          ("pup", 12),
          ("pvp", 75),
          ("qnx", 106),
          ("rdp", 27),
          ("rsvp", 46),
          ("rsvpE2eIgnore", 134),
          ("rvd", 66),
          ("satExpak", 64),
          ("satMon", 69),
          ("sccSp", 96),
          ("scps", 105),
          ("sctp", 132),
          ("sdrp", 42),
          ("secureVmpt", 82),
          ("shim6", 140),
          ("skip", 57),
          ("sm", 122),
          ("smp", 121),
          ("snp", 109),
          ("spriteRpc", 90),
          ("sps", 130),
          ("srp", 119),
          ("sscopmce", 128),
          ("st", 5),
          ("stp", 118),
          ("sunNd", 77),
          ("swipe", 53),
          ("tcf", 87),
          ("tcp", 6),
          ("tlsp", 56),
          ("tpplusplus", 39),
          ("trunk1", 23),
          ("trunk2", 24),
          ("ttp", 84),
          ("udp", 17),
          ("udpLite", 136),
          ("uti", 120),
          ("vines", 83),
          ("visa", 70),
          ("vmtp", 81),
          ("vrrp", 112),
          ("wbExpak", 79),
          ("wbMon", 78),
          ("wsn", 74),
          ("xnet", 15),
          ("xnsIdp", 22),
          ("xtp", 36))
    )



class TmnxMobPathMgmtState(Integer32, TextualConvention):
    status = "current"
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
        *(("disabled", 0),
          ("fault", 3),
          ("idle", 4),
          ("reqTimeOut", 2),
          ("restart", 5),
          ("up", 1))
    )



class TmnxMobDiaPathMgmtState(Integer32, TextualConvention):
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
        *(("active", 3),
          ("inactive", 2),
          ("shutDown", 0),
          ("shuttingDown", 1))
    )



class TmnxMobDiaDetailPathMgmtState(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("error", 0),
          ("idle", 1),
          ("localShutdown", 3),
          ("open", 7),
          ("openCoolingDown", 8),
          ("remoteClosing", 4),
          ("waitCea", 6),
          ("waitConnAck", 5),
          ("waitDns", 9))
    )



class TmnxMobGwType(Integer32, TextualConvention):
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
        *(("pgw", 2),
          ("sgw", 1),
          ("wlanGw", 3))
    )



class TmnxMobChargingProfile(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxMobChargingProfileOrInherit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )



class TmnxMobAuthType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diameter", 2),
          ("radius", 1))
    )



class TmnxMobAuthUserName(Integer32, TextualConvention):
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
        *(("imsi", 1),
          ("msisdn", 2),
          ("pco", 3))
    )



class TmnxMobProfGbrRate(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )



class TmnxMobProfMbrRate(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )



class TmnxMobPeerType(Integer32, TextualConvention):
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
        *(("hsgw", 3),
          ("pgw", 2),
          ("sgw", 1))
    )



class TmnxMobRfAcctLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pdnLevel", 1),
          ("qciLevel", 2))
    )



class TmnxMobProfPolReportingLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ratingGrp", 2),
          ("servId", 1))
    )



class TmnxMobProfPolChargingMethod(Integer32, TextualConvention):
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
        *(("both", 3),
          ("offline", 2),
          ("online", 1),
          ("profChargingMtd", 0))
    )



class TmnxMobProfPolMeteringMethod(Integer32, TextualConvention):
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
          ("timeBased", 1),
          ("volBased", 2))
    )



class TmnxMobServerState(Integer32, TextualConvention):
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
        *(("down", 2),
          ("na", 0),
          ("up", 1))
    )



class TmnxMobChargingBearerType(Integer32, TextualConvention):
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
        *(("home", 1),
          ("roaming", 3),
          ("visiting", 2))
    )



class TmnxMobChargingLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bearer", 2),
          ("pdn", 1))
    )



class TmnxMobIpCanType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("epc3gpp", 1),
          ("gprs3gpp", 2))
    )



class TmnxMobStaticPolPrecedence(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )



class TmnxMobStaticPolPrecedenceOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TmnxMobDualStackPref(Integer32, TextualConvention):
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("useCplane", 3))
    )



class TmnxMobDfPeerId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class TmnxMobLiTarget(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class TmnxMobLiTargetType(Integer32, TextualConvention):
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
        *(("imei", 3),
          ("imsi", 1),
          ("msisdn", 2))
    )



class TmnxReasContextVal(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )



class TmnxVdoStatInt(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("interval", 2))
    )



class TmnxVdoOutputFormat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtp-udp", 2),
          ("udp", 1))
    )



class TmnxVdoAnalyzerAlarm(Integer32, TextualConvention):
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
        *(("none", 0),
          ("poa", 3),
          ("qos", 2),
          ("tnc", 1))
    )



class TmnxVdoAnalyzerAlarmStates(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )



class SvcISID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16777215),
    )



class TIngPolicerId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class TIngPolicerIdOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )



class TEgrPolicerId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TEgrPolicerIdOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TFIRRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )



class TBurstSizeBytes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 134217728),
    )



class THSMDABurstSizeBytes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2688000),
    )



class THSMDAQueueBurstLimit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1000000),
    )



class TClassBurstLimit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 327680),
    )



class TPlcrBurstSizeBytes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4194304),
    )



class TBurstSizeBytesOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 134217728),
    )



class THSMDABurstSizeBytesOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2688000),
    )



class TPlcrBurstSizeBytesOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4194304),
    )



class TmnxBfdSessOperState(Integer32, TextualConvention):
    status = "current"
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
        *(("broken", 3),
          ("connected", 2),
          ("noResources", 6),
          ("notConfigured", 5),
          ("peerDetectsDown", 4),
          ("unknown", 1))
    )



class TmnxIngPolicerStatMode(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("minimal", 1),
          ("noStats", 0),
          ("offeredLimitedCapCIR", 9),
          ("offeredLimitedProfileCIR", 7),
          ("offeredPrioCIR", 6),
          ("offeredPrioNoCIR", 4),
          ("offeredProfileCIR", 5),
          ("offeredProfileCapCIR", 8),
          ("offeredProfileNoCIR", 2),
          ("offeredTotalCIR", 3))
    )



class TmnxIngPolicerStatModeOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("minimal", 1),
          ("noOverride", -1),
          ("noStats", 0),
          ("offeredLimitedCapCIR", 9),
          ("offeredLimitedProfileCIR", 7),
          ("offeredPrioCIR", 6),
          ("offeredPrioNoCIR", 4),
          ("offeredProfileCIR", 5),
          ("offeredProfileCapCIR", 8),
          ("offeredProfileNoCIR", 2),
          ("offeredTotalCIR", 3))
    )



class TmnxEgrPolicerStatMode(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("minimal", 1),
          ("noStats", 0),
          ("offeredLimitedCapCIR", 5),
          ("offeredProfileCIR", 4),
          ("offeredProfileCapCIR", 6),
          ("offeredProfileNoCIR", 2),
          ("offeredTotalCIR", 3))
    )



class TmnxEgrPolicerStatModeOverride(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("minimal", 1),
          ("noOverride", -1),
          ("noStats", 0),
          ("offeredLimitedCapCIR", 5),
          ("offeredProfileCIR", 4),
          ("offeredProfileCapCIR", 6),
          ("offeredProfileNoCIR", 2),
          ("offeredTotalCIR", 3))
    )



class TmnxTlsGroupId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class TSubHostId(Unsigned32, TextualConvention):
    status = "current"


class TDirection(Integer32, TextualConvention):
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
        *(("both", 0),
          ("egress", 2),
          ("ingress", 1))
    )



class TBurstLimit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 14000000),
    )



class TMacFilterType(Integer32, TextualConvention):
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
        *(("isid", 2),
          ("normal", 1),
          ("vid", 3))
    )



class TmnxPwGlobalId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxPwGlobalIdOrZero(Unsigned32, TextualConvention):
    status = "current"


class TmnxPwPathHopId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class TmnxPwPathHopIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class TmnxSpokeSdpId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxSpokeSdpIdOrZero(Unsigned32, TextualConvention):
    status = "current"


class TmnxMsPwPeSignaling(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("master", 2))
    )



class TmnxLdpFECType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              128,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("addrHost", 3),
          ("addrPrefix", 2),
          ("addrWildcard", 1),
          ("vll", 128),
          ("vpls", 130),
          ("vpws", 129))
    )



class TmnxSvcOperGrpCreationOrigin(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("mvrp", 2))
    )



class TmnxOperGrpHoldUpTime(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class TmnxOperGrpHoldDownTime(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class TmnxSrrpPriorityStep(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )



class TmnxAiiType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aiiType1", 1),
          ("aiiType2", 2))
    )



class ServObjDesc(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class TMplsLspExpProfMapID(TPolicyID, TextualConvention):
    status = "current"
    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TSysResource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 11),
    )



class TmnxSpbFid(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class TmnxSpbFidOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class TmnxSpbBridgePriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class TmnxSlopeMap(Integer32, TextualConvention):
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
        *(("high", 2),
          ("highLow", 3),
          ("low", 1),
          ("none", 0))
    )



class TmnxCdrType(Integer32, TextualConvention):
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
        *(("eGCdr", 3),
          ("gCdr", 2),
          ("pgwCdr", 1))
    )



class TmnxThresholdGroupType(Integer32, TextualConvention):
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
        *(("brMgmtCfFailure", 3),
          ("brMgmtCfSuccess", 2),
          ("brMgmtLimit", 1),
          ("brMgmtTraffic", 4),
          ("cpmSystem", 6),
          ("mgIsmSystem", 7),
          ("pathMgmt", 5))
    )



class TmnxMobUeId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class TmnxMobUeIdType(Integer32, TextualConvention):
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
        *(("imei", 1),
          ("imsi", 0),
          ("msisdn", 2))
    )



class TmnxMobImsiStr(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(9, 15),
    )



class TmnxVpnIpBackupFamily(Bits, TextualConvention):
    status = "current"


class TmnxTunnelGroupId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class TmnxTunnelGroupIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class TmnxMobRatingGrpState(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("allowFlow", 1),
          ("allowResRules", 4),
          ("creditsToppedUp", 7),
          ("dis1stPktTrigger", 6),
          ("disallowFlow", 2),
          ("iom1stPktTrigger", 5),
          ("redWebPortal", 3),
          ("waitForFpt", 8))
    )



class TmnxMobPresenceState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )



class TmnxMobPdnGyChrgTriggerType(Integer32, TextualConvention):
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("locCellIdRecvd", 22),
          ("locLacRecvd", 21),
          ("locMccRecvd", 18),
          ("locMncRecvd", 19),
          ("locRacRecvd", 20),
          ("locRecvd", 2),
          ("medCompRecvd", 23),
          ("partcNmbRecvd", 24),
          ("qosDlyClsRecvd", 6),
          ("qosGrtBtRtDllnkRecvd", 17),
          ("qosGrtBtRtUplnkRecvd", 16),
          ("qosMeanTrptRecvd", 9),
          ("qosMxBtRtDllnkRecvd", 11),
          ("qosMxBtRtUplnkRecvd", 10),
          ("qosPeakThrptRecvd", 7),
          ("qosPrcClsRecvd", 8),
          ("qosRecvd", 1),
          ("qosResBerRecvd", 12),
          ("qosRlbClsRecvd", 5),
          ("qosSduErrRatRecvd", 13),
          ("qosTransDelayRecvd", 14),
          ("qosTrfClsRecvd", 4),
          ("qosTrfHndPriRecvd", 15),
          ("ratRecvd", 3),
          ("servCondRecvd", 27),
          ("servNodeRecvd", 28),
          ("sgsnIpAddrRecvd", 0),
          ("thrldPartcNmbRecvd", 25),
          ("usrCsgInfoRecvd", 29),
          ("usrPartcTypeRecvd", 26))
    )



class TmnxMobPdnRefPointType(Integer32, TextualConvention):
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
        *(("gn", 3),
          ("gp", 5),
          ("s2a", 4),
          ("s5", 1),
          ("s8", 2))
    )



class TmnxQosBytesHex(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



class TSiteOperStatus(Integer32, TextualConvention):
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
        *(("down", 2),
          ("outOfResource", 3),
          ("up", 1))
    )



class TmnxSpbFdbLocale(Integer32, TextualConvention):
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
        *(("local", 1),
          ("sap", 2),
          ("sdp", 3),
          ("unknown", 4))
    )



class TmnxSpbFdbState(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("addModPending", 1),
          ("delPending", 2),
          ("noFateShared", 4),
          ("noUcast", 6),
          ("ok", 0),
          ("svcFdbLimit", 5),
          ("sysFdbLimit", 3))
    )



class TmnxMobServRefPointType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("s2a", 4),
          ("s5", 1),
          ("s8", 2))
    )



class TmnxMobAccessType(Integer32, TextualConvention):
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
        *(("eps", 1),
          ("gprs", 2),
          ("non3gpp", 3))
    )



class TmnxMobUeStrPrefix(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 15),
    )



class TmnxCdrDiagnosticAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )



class TmnxMplsTpGlobalID(Unsigned32, TextualConvention):
    status = "current"


class TmnxMplsTpNodeID(Unsigned32, TextualConvention):
    status = "current"


class TmnxMplsTpTunnelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mplsTpStatic", 1)
    )



class TmnxVwmCardType(Integer32, TextualConvention):
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
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("not-equipped", 1),
          ("not-provisioned", 0),
          ("sfc1A", 2),
          ("sfc1B", 3),
          ("sfc1C", 4),
          ("sfc1D", 5),
          ("sfc1E", 6),
          ("sfc1F", 7),
          ("sfc1G", 8),
          ("sfc1H", 9),
          ("sfc2AandB", 10),
          ("sfc2CandD", 11),
          ("sfc2EandF", 12),
          ("sfc2GandH", 13),
          ("sfc4A-D", 14),
          ("sfc4E-H", 15),
          ("sfc8", 16),
          ("sfd2A-R", 29),
          ("sfd2B-R", 30),
          ("sfd2C-R", 31),
          ("sfd2D-R", 32),
          ("sfd2E-R", 33),
          ("sfd2F-R", 34),
          ("sfd2G-R", 35),
          ("sfd2H-R", 36),
          ("sfd2I-R", 37),
          ("sfd2L-R", 38),
          ("sfd2M-R", 39),
          ("sfd2N-R", 40),
          ("sfd2O-R", 41),
          ("sfd2P-R", 42),
          ("sfd2Q-R", 43),
          ("sfd2R-R", 44),
          ("sfd4A-R", 21),
          ("sfd4B-R", 22),
          ("sfd4C-R", 23),
          ("sfd4D-R", 24),
          ("sfd4E-R", 25),
          ("sfd4F-R", 26),
          ("sfd4G-R", 27),
          ("sfd4H-R", 28),
          ("sfd8A-R", 17),
          ("sfd8B-R", 18),
          ("sfd8C-R", 19),
          ("sfd8D-R", 20))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-TC-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "TmnxPortID": TmnxPortID,
       "TmnxEncapVal": TmnxEncapVal,
       "QTag": QTag,
       "QTagOrZero": QTagOrZero,
       "QTagFullRange": QTagFullRange,
       "QTagFullRangeOrNone": QTagFullRangeOrNone,
       "TmnxStrSapId": TmnxStrSapId,
       "IpAddressPrefixLength": IpAddressPrefixLength,
       "TmnxActionType": TmnxActionType,
       "TmnxAdminState": TmnxAdminState,
       "TmnxOperState": TmnxOperState,
       "TmnxStatus": TmnxStatus,
       "TmnxEnabledDisabled": TmnxEnabledDisabled,
       "TmnxEnabledDisabledOrInherit": TmnxEnabledDisabledOrInherit,
       "TNamedItem": TNamedItem,
       "TNamedItemOrEmpty": TNamedItemOrEmpty,
       "TLNamedItem": TLNamedItem,
       "TLNamedItemOrEmpty": TLNamedItemOrEmpty,
       "TItemDescription": TItemDescription,
       "TItemLongDescription": TItemLongDescription,
       "TmnxVRtrID": TmnxVRtrID,
       "TmnxVRtrIDOrZero": TmnxVRtrIDOrZero,
       "TmnxBgpAutonomousSystem": TmnxBgpAutonomousSystem,
       "TmnxBgpLocalPreference": TmnxBgpLocalPreference,
       "TmnxBgpPreference": TmnxBgpPreference,
       "TmnxCustId": TmnxCustId,
       "BgpPeeringStatus": BgpPeeringStatus,
       "TmnxServId": TmnxServId,
       "ServiceAdminStatus": ServiceAdminStatus,
       "ServiceOperStatus": ServiceOperStatus,
       "TPolicyID": TPolicyID,
       "TTmplPolicyID": TTmplPolicyID,
       "TSapIngressPolicyID": TSapIngressPolicyID,
       "TSapEgressPolicyID": TSapEgressPolicyID,
       "TSdpIngressPolicyID": TSdpIngressPolicyID,
       "TSdpEgressPolicyID": TSdpEgressPolicyID,
       "TQosQGrpInstanceIDorZero": TQosQGrpInstanceIDorZero,
       "TmnxBsxTransitIpPolicyId": TmnxBsxTransitIpPolicyId,
       "TmnxBsxTransitIpPolicyIdOrZero": TmnxBsxTransitIpPolicyIdOrZero,
       "TmnxBsxTransPrefPolicyId": TmnxBsxTransPrefPolicyId,
       "TmnxBsxTransPrefPolicyIdOrZero": TmnxBsxTransPrefPolicyIdOrZero,
       "TmnxBsxAarpId": TmnxBsxAarpId,
       "TmnxBsxAarpIdOrZero": TmnxBsxAarpIdOrZero,
       "TmnxBsxAarpServiceRefType": TmnxBsxAarpServiceRefType,
       "TSapEgrEncapGrpQosPolicyIdOrZero": TSapEgrEncapGrpQosPolicyIdOrZero,
       "TSapEgrEncapGroupType": TSapEgrEncapGroupType,
       "TSapEgrEncapGroupActionType": TSapEgrEncapGroupActionType,
       "TPerPacketOffset": TPerPacketOffset,
       "TPerPacketOffsetOvr": TPerPacketOffsetOvr,
       "TIngressHsmdaPerPacketOffset": TIngressHsmdaPerPacketOffset,
       "TEgressQPerPacketOffset": TEgressQPerPacketOffset,
       "TIngHsmdaPerPacketOffsetOvr": TIngHsmdaPerPacketOffsetOvr,
       "TEgressHsmdaPerPacketOffset": TEgressHsmdaPerPacketOffset,
       "THsmdaCounterIdOrZero": THsmdaCounterIdOrZero,
       "THsmdaCounterIdOrZeroOrAll": THsmdaCounterIdOrZeroOrAll,
       "TEgrHsmdaPerPacketOffsetOvr": TEgrHsmdaPerPacketOffsetOvr,
       "TIngressHsmdaCounterId": TIngressHsmdaCounterId,
       "TIngressHsmdaCounterIdOrZero": TIngressHsmdaCounterIdOrZero,
       "TEgressHsmdaCounterId": TEgressHsmdaCounterId,
       "TEgressHsmdaCounterIdOrZero": TEgressHsmdaCounterIdOrZero,
       "TEgrRateModType": TEgrRateModType,
       "TPolicyStatementNameOrEmpty": TPolicyStatementNameOrEmpty,
       "TmnxVcType": TmnxVcType,
       "TmnxVcId": TmnxVcId,
       "TmnxVcIdOrNone": TmnxVcIdOrNone,
       "Dot1PPriority": Dot1PPriority,
       "Dot1PPriorityMask": Dot1PPriorityMask,
       "ServiceAccessPoint": ServiceAccessPoint,
       "TLspExpValue": TLspExpValue,
       "TIpProtocol": TIpProtocol,
       "TIpOption": TIpOption,
       "TTcpUdpPort": TTcpUdpPort,
       "TOperator": TOperator,
       "TTcpUdpPortOperator": TTcpUdpPortOperator,
       "TFrameType": TFrameType,
       "TQueueId": TQueueId,
       "TQueueIdOrAll": TQueueIdOrAll,
       "TIngressQueueId": TIngressQueueId,
       "TIngressMeterId": TIngressMeterId,
       "TSapIngressMeterId": TSapIngressMeterId,
       "TNetworkIngressMeterId": TNetworkIngressMeterId,
       "TEgressQueueId": TEgressQueueId,
       "TIngressHsmdaQueueId": TIngressHsmdaQueueId,
       "TEgressHsmdaQueueId": TEgressHsmdaQueueId,
       "THsmdaSchedulerPolicyGroupId": THsmdaSchedulerPolicyGroupId,
       "THsmdaPolicyIncludeQueues": THsmdaPolicyIncludeQueues,
       "THsmdaPolicyScheduleClass": THsmdaPolicyScheduleClass,
       "TDSCPName": TDSCPName,
       "TDSCPNameOrEmpty": TDSCPNameOrEmpty,
       "TDSCPValue": TDSCPValue,
       "TDSCPValueOrNone": TDSCPValueOrNone,
       "TDSCPFilterActionValue": TDSCPFilterActionValue,
       "TFCName": TFCName,
       "TFCNameOrEmpty": TFCNameOrEmpty,
       "TFCSet": TFCSet,
       "TFCType": TFCType,
       "TmnxTunnelType": TmnxTunnelType,
       "TmnxTunnelID": TmnxTunnelID,
       "TmnxBgpRouteTarget": TmnxBgpRouteTarget,
       "TmnxVPNRouteDistinguisher": TmnxVPNRouteDistinguisher,
       "SdpBindId": SdpBindId,
       "TmnxVRtrMplsLspID": TmnxVRtrMplsLspID,
       "TPortSchedulerPIR": TPortSchedulerPIR,
       "TPortSchedulerPIRRate": TPortSchedulerPIRRate,
       "TPortSchedulerCIR": TPortSchedulerCIR,
       "TWeight": TWeight,
       "TNonZeroWeight": TNonZeroWeight,
       "TPolicerWeight": TPolicerWeight,
       "THsmdaWeight": THsmdaWeight,
       "THsmdaWrrWeight": THsmdaWrrWeight,
       "THsmdaWeightClass": THsmdaWeightClass,
       "THsmdaWeightOverride": THsmdaWeightOverride,
       "THsmdaWrrWeightOverride": THsmdaWrrWeightOverride,
       "TCIRRate": TCIRRate,
       "THPolCIRRate": THPolCIRRate,
       "TRateType": TRateType,
       "TBWRateType": TBWRateType,
       "TPolicerRateType": TPolicerRateType,
       "TCIRRateOverride": TCIRRateOverride,
       "THPolCIRRateOverride": THPolCIRRateOverride,
       "TCIRPercentOverride": TCIRPercentOverride,
       "THsmdaCIRKRate": THsmdaCIRKRate,
       "THsmdaCIRKRateOverride": THsmdaCIRKRateOverride,
       "THsmdaCIRMRate": THsmdaCIRMRate,
       "THsmdaCIRMRateOverride": THsmdaCIRMRateOverride,
       "TPIRRate": TPIRRate,
       "THPolVirtualSchePIRRate": THPolVirtualSchePIRRate,
       "THPolVirtualScheCIRRate": THPolVirtualScheCIRRate,
       "TAdvCfgRate": TAdvCfgRate,
       "TMaxDecRate": TMaxDecRate,
       "THPolPIRRate": THPolPIRRate,
       "TSecondaryShaper10GPIRRate": TSecondaryShaper10GPIRRate,
       "TExpSecondaryShaperPIRRate": TExpSecondaryShaperPIRRate,
       "TExpSecondaryShaperClassRate": TExpSecondaryShaperClassRate,
       "TPIRRateOverride": TPIRRateOverride,
       "THPolPIRRateOverride": THPolPIRRateOverride,
       "TPIRPercentOverride": TPIRPercentOverride,
       "TPIRRateOrZero": TPIRRateOrZero,
       "THsmdaPIRKRate": THsmdaPIRKRate,
       "THsmdaPIRKRateOverride": THsmdaPIRKRateOverride,
       "THsmdaPIRMRate": THsmdaPIRMRate,
       "THsmdaPIRMRateOverride": THsmdaPIRMRateOverride,
       "TmnxDHCP6MsgType": TmnxDHCP6MsgType,
       "TmnxOspfInstance": TmnxOspfInstance,
       "TmnxBGPFamilyType": TmnxBGPFamilyType,
       "TmnxIgmpGroupFilterMode": TmnxIgmpGroupFilterMode,
       "TmnxIgmpGroupType": TmnxIgmpGroupType,
       "TmnxIgmpVersion": TmnxIgmpVersion,
       "TmnxMldGroupFilterMode": TmnxMldGroupFilterMode,
       "TmnxMldGroupType": TmnxMldGroupType,
       "TmnxMldVersion": TmnxMldVersion,
       "TmnxManagedRouteStatus": TmnxManagedRouteStatus,
       "TmnxAncpString": TmnxAncpString,
       "TmnxAncpStringOrZero": TmnxAncpStringOrZero,
       "TmnxMulticastAddrFamily": TmnxMulticastAddrFamily,
       "TmnxAsciiSpecification": TmnxAsciiSpecification,
       "TmnxMacSpecification": TmnxMacSpecification,
       "TmnxBinarySpecification": TmnxBinarySpecification,
       "TmnxDefSubIdSource": TmnxDefSubIdSource,
       "TmnxSubIdentString": TmnxSubIdentString,
       "TmnxSubIdentStringOrEmpty": TmnxSubIdentStringOrEmpty,
       "TmnxSubRadServAlgorithm": TmnxSubRadServAlgorithm,
       "TmnxSubRadiusAttrType": TmnxSubRadiusAttrType,
       "TmnxSubRadiusVendorId": TmnxSubRadiusVendorId,
       "TmnxRadiusPendingReqLimit": TmnxRadiusPendingReqLimit,
       "TmnxRadiusServerOperState": TmnxRadiusServerOperState,
       "TmnxSubProfileString": TmnxSubProfileString,
       "TmnxSubProfileStringOrEmpty": TmnxSubProfileStringOrEmpty,
       "TmnxSlaProfileString": TmnxSlaProfileString,
       "TmnxSlaProfileStringOrEmpty": TmnxSlaProfileStringOrEmpty,
       "TmnxAppProfileString": TmnxAppProfileString,
       "TmnxAppProfileStringOrEmpty": TmnxAppProfileStringOrEmpty,
       "TmnxSubMgtIntDestIdOrEmpty": TmnxSubMgtIntDestIdOrEmpty,
       "TmnxSubMgtIntDestId": TmnxSubMgtIntDestId,
       "TmnxDefInterDestIdSource": TmnxDefInterDestIdSource,
       "TmnxSubNasPortSuffixType": TmnxSubNasPortSuffixType,
       "TmnxSubNasPortPrefixType": TmnxSubNasPortPrefixType,
       "TmnxSubNasPortTypeType": TmnxSubNasPortTypeType,
       "TmnxSubMgtOrgStrOrZero": TmnxSubMgtOrgStrOrZero,
       "TmnxSubMgtOrgString": TmnxSubMgtOrgString,
       "TmnxFilterProfileStringOrEmpty": TmnxFilterProfileStringOrEmpty,
       "TmnxAccessLoopEncapDataLink": TmnxAccessLoopEncapDataLink,
       "TmnxAccessLoopEncaps1": TmnxAccessLoopEncaps1,
       "TmnxAccessLoopEncaps2": TmnxAccessLoopEncaps2,
       "TmnxSubAleOffsetMode": TmnxSubAleOffsetMode,
       "TmnxSubAleOffset": TmnxSubAleOffset,
       "TmnxDhcpOptionType": TmnxDhcpOptionType,
       "TmnxPppoeUserName": TmnxPppoeUserName,
       "TmnxPppoeUserNameOrEmpty": TmnxPppoeUserNameOrEmpty,
       "TCpmProtPolicyID": TCpmProtPolicyID,
       "TCpmProtPolicyIDOrDefault": TCpmProtPolicyIDOrDefault,
       "TMlpppQoSProfileId": TMlpppQoSProfileId,
       "TMcFrQoSProfileId": TMcFrQoSProfileId,
       "TmnxPppoeSessionId": TmnxPppoeSessionId,
       "TmnxPppoePadoDelay": TmnxPppoePadoDelay,
       "TmnxPppoeSessionInfoOrigin": TmnxPppoeSessionInfoOrigin,
       "TmnxPppoeSessionType": TmnxPppoeSessionType,
       "TmnxPppNcpProtocol": TmnxPppNcpProtocol,
       "TmnxMlpppEpClass": TmnxMlpppEpClass,
       "TNetworkPolicyID": TNetworkPolicyID,
       "TItemScope": TItemScope,
       "TItemMatch": TItemMatch,
       "TPriority": TPriority,
       "TPriorityOrDefault": TPriorityOrDefault,
       "TProfileUseDEOrNone": TProfileUseDEOrNone,
       "TPriorityOrUndefined": TPriorityOrUndefined,
       "TProfile": TProfile,
       "TProfileOrDei": TProfileOrDei,
       "TDEProfile": TDEProfile,
       "TDEProfileOrDei": TDEProfileOrDei,
       "TProfileOrNone": TProfileOrNone,
       "TAdaptationRule": TAdaptationRule,
       "TAdaptationRuleOverride": TAdaptationRuleOverride,
       "TRemarkType": TRemarkType,
       "TPrecValue": TPrecValue,
       "TPrecValueOrNone": TPrecValueOrNone,
       "TBurstSize": TBurstSize,
       "TBurstSizeOverride": TBurstSizeOverride,
       "TBurstPercent": TBurstPercent,
       "TBurstHundredthsOfPercent": TBurstHundredthsOfPercent,
       "TBurstPercentOrDefault": TBurstPercentOrDefault,
       "TBurstPercentOrDefaultOverride": TBurstPercentOrDefaultOverride,
       "TRatePercent": TRatePercent,
       "TPIRRatePercent": TPIRRatePercent,
       "TLevel": TLevel,
       "TLevelOrDefault": TLevelOrDefault,
       "TQWeight": TQWeight,
       "TMeterMode": TMeterMode,
       "TPlcyMode": TPlcyMode,
       "TPlcyQuanta": TPlcyQuanta,
       "TQueueMode": TQueueMode,
       "TEntryIndicator": TEntryIndicator,
       "TEntryId": TEntryId,
       "TMatchCriteria": TMatchCriteria,
       "TmnxMdaQos": TmnxMdaQos,
       "TAtmTdpDescrType": TAtmTdpDescrType,
       "TDEValue": TDEValue,
       "TQGroupType": TQGroupType,
       "TQosOverrideType": TQosOverrideType,
       "TmnxIPsecTunnelTemplateId": TmnxIPsecTunnelTemplateId,
       "TmnxIPsecTunnelTemplateIdOrZero": TmnxIPsecTunnelTemplateIdOrZero,
       "TmnxIpSecIsaOperFlags": TmnxIpSecIsaOperFlags,
       "TmnxIkePolicyAuthMethod": TmnxIkePolicyAuthMethod,
       "TmnxIkePolicyOwnAuthMethod": TmnxIkePolicyOwnAuthMethod,
       "TmnxRsvpDSTEClassType": TmnxRsvpDSTEClassType,
       "TmnxAccPlcyQICounters": TmnxAccPlcyQICounters,
       "TmnxAccPlcyQECounters": TmnxAccPlcyQECounters,
       "TmnxAccPlcyOICounters": TmnxAccPlcyOICounters,
       "TmnxAccPlcyOECounters": TmnxAccPlcyOECounters,
       "TmnxAccPlcyAACounters": TmnxAccPlcyAACounters,
       "TmnxVdoGrpIdIndex": TmnxVdoGrpIdIndex,
       "TmnxVdoGrpId": TmnxVdoGrpId,
       "TmnxVdoGrpIdOrInherit": TmnxVdoGrpIdOrInherit,
       "TmnxVdoFccServerMode": TmnxVdoFccServerMode,
       "TmnxVdoPortNumber": TmnxVdoPortNumber,
       "TmnxVdoIfName": TmnxVdoIfName,
       "TmnxTimeInSec": TmnxTimeInSec,
       "TmnxMobProfName": TmnxMobProfName,
       "TmnxMobProfNameOrEmpty": TmnxMobProfNameOrEmpty,
       "TmnxMobProfIpTtl": TmnxMobProfIpTtl,
       "TmnxMobDiaTransTimer": TmnxMobDiaTransTimer,
       "TmnxMobDiaRetryCount": TmnxMobDiaRetryCount,
       "TmnxMobDiaPeerHost": TmnxMobDiaPeerHost,
       "TmnxMobGwId": TmnxMobGwId,
       "TmnxMobNode": TmnxMobNode,
       "TmnxMobBufferLimit": TmnxMobBufferLimit,
       "TmnxMobQueueLimit": TmnxMobQueueLimit,
       "TmnxMobRtrAdvtInterval": TmnxMobRtrAdvtInterval,
       "TmnxMobRtrAdvtLifeTime": TmnxMobRtrAdvtLifeTime,
       "TmnxMobAddrScheme": TmnxMobAddrScheme,
       "TmnxMobQciValue": TmnxMobQciValue,
       "TmnxMobQciValueOrZero": TmnxMobQciValueOrZero,
       "TmnxMobArpValue": TmnxMobArpValue,
       "TmnxMobArpValueOrZero": TmnxMobArpValueOrZero,
       "TmnxMobApn": TmnxMobApn,
       "TmnxMobApnOrZero": TmnxMobApnOrZero,
       "TmnxMobImsi": TmnxMobImsi,
       "TmnxMobMsisdn": TmnxMobMsisdn,
       "TmnxMobImei": TmnxMobImei,
       "TmnxMobNai": TmnxMobNai,
       "TmnxMobMcc": TmnxMobMcc,
       "TmnxMobMnc": TmnxMobMnc,
       "TmnxMobMccOrEmpty": TmnxMobMccOrEmpty,
       "TmnxMobMncOrEmpty": TmnxMobMncOrEmpty,
       "TmnxMobUeState": TmnxMobUeState,
       "TmnxMobUeRat": TmnxMobUeRat,
       "TmnxMobUeSubType": TmnxMobUeSubType,
       "TmnxMobPdnType": TmnxMobPdnType,
       "TmnxMobPgwSigProtocol": TmnxMobPgwSigProtocol,
       "TmnxMobPdnSessionState": TmnxMobPdnSessionState,
       "TmnxMobPdnSessionEvent": TmnxMobPdnSessionEvent,
       "TmnxMobBearerId": TmnxMobBearerId,
       "TmnxMobBearerType": TmnxMobBearerType,
       "TmnxMobQci": TmnxMobQci,
       "TmnxMobArp": TmnxMobArp,
       "TmnxMobSdf": TmnxMobSdf,
       "TmnxMobSdfFilter": TmnxMobSdfFilter,
       "TmnxMobSdfFilterNum": TmnxMobSdfFilterNum,
       "TmnxMobSdfRuleName": TmnxMobSdfRuleName,
       "TmnxMobSdfFilterDirection": TmnxMobSdfFilterDirection,
       "TmnxMobSdfFilterProtocol": TmnxMobSdfFilterProtocol,
       "TmnxMobPathMgmtState": TmnxMobPathMgmtState,
       "TmnxMobDiaPathMgmtState": TmnxMobDiaPathMgmtState,
       "TmnxMobDiaDetailPathMgmtState": TmnxMobDiaDetailPathMgmtState,
       "TmnxMobGwType": TmnxMobGwType,
       "TmnxMobChargingProfile": TmnxMobChargingProfile,
       "TmnxMobChargingProfileOrInherit": TmnxMobChargingProfileOrInherit,
       "TmnxMobAuthType": TmnxMobAuthType,
       "TmnxMobAuthUserName": TmnxMobAuthUserName,
       "TmnxMobProfGbrRate": TmnxMobProfGbrRate,
       "TmnxMobProfMbrRate": TmnxMobProfMbrRate,
       "TmnxMobPeerType": TmnxMobPeerType,
       "TmnxMobRfAcctLevel": TmnxMobRfAcctLevel,
       "TmnxMobProfPolReportingLevel": TmnxMobProfPolReportingLevel,
       "TmnxMobProfPolChargingMethod": TmnxMobProfPolChargingMethod,
       "TmnxMobProfPolMeteringMethod": TmnxMobProfPolMeteringMethod,
       "TmnxMobServerState": TmnxMobServerState,
       "TmnxMobChargingBearerType": TmnxMobChargingBearerType,
       "TmnxMobChargingLevel": TmnxMobChargingLevel,
       "TmnxMobIpCanType": TmnxMobIpCanType,
       "TmnxMobStaticPolPrecedence": TmnxMobStaticPolPrecedence,
       "TmnxMobStaticPolPrecedenceOrZero": TmnxMobStaticPolPrecedenceOrZero,
       "TmnxMobDualStackPref": TmnxMobDualStackPref,
       "TmnxMobDfPeerId": TmnxMobDfPeerId,
       "TmnxMobLiTarget": TmnxMobLiTarget,
       "TmnxMobLiTargetType": TmnxMobLiTargetType,
       "TmnxReasContextVal": TmnxReasContextVal,
       "TmnxVdoStatInt": TmnxVdoStatInt,
       "TmnxVdoOutputFormat": TmnxVdoOutputFormat,
       "TmnxVdoAnalyzerAlarm": TmnxVdoAnalyzerAlarm,
       "TmnxVdoAnalyzerAlarmStates": TmnxVdoAnalyzerAlarmStates,
       "SvcISID": SvcISID,
       "TIngPolicerId": TIngPolicerId,
       "TIngPolicerIdOrNone": TIngPolicerIdOrNone,
       "TEgrPolicerId": TEgrPolicerId,
       "TEgrPolicerIdOrNone": TEgrPolicerIdOrNone,
       "TFIRRate": TFIRRate,
       "TBurstSizeBytes": TBurstSizeBytes,
       "THSMDABurstSizeBytes": THSMDABurstSizeBytes,
       "THSMDAQueueBurstLimit": THSMDAQueueBurstLimit,
       "TClassBurstLimit": TClassBurstLimit,
       "TPlcrBurstSizeBytes": TPlcrBurstSizeBytes,
       "TBurstSizeBytesOverride": TBurstSizeBytesOverride,
       "THSMDABurstSizeBytesOverride": THSMDABurstSizeBytesOverride,
       "TPlcrBurstSizeBytesOverride": TPlcrBurstSizeBytesOverride,
       "TmnxBfdSessOperState": TmnxBfdSessOperState,
       "TmnxIngPolicerStatMode": TmnxIngPolicerStatMode,
       "TmnxIngPolicerStatModeOverride": TmnxIngPolicerStatModeOverride,
       "TmnxEgrPolicerStatMode": TmnxEgrPolicerStatMode,
       "TmnxEgrPolicerStatModeOverride": TmnxEgrPolicerStatModeOverride,
       "TmnxTlsGroupId": TmnxTlsGroupId,
       "TSubHostId": TSubHostId,
       "TDirection": TDirection,
       "TBurstLimit": TBurstLimit,
       "TMacFilterType": TMacFilterType,
       "TmnxPwGlobalId": TmnxPwGlobalId,
       "TmnxPwGlobalIdOrZero": TmnxPwGlobalIdOrZero,
       "TmnxPwPathHopId": TmnxPwPathHopId,
       "TmnxPwPathHopIdOrZero": TmnxPwPathHopIdOrZero,
       "TmnxSpokeSdpId": TmnxSpokeSdpId,
       "TmnxSpokeSdpIdOrZero": TmnxSpokeSdpIdOrZero,
       "TmnxMsPwPeSignaling": TmnxMsPwPeSignaling,
       "TmnxLdpFECType": TmnxLdpFECType,
       "TmnxSvcOperGrpCreationOrigin": TmnxSvcOperGrpCreationOrigin,
       "TmnxOperGrpHoldUpTime": TmnxOperGrpHoldUpTime,
       "TmnxOperGrpHoldDownTime": TmnxOperGrpHoldDownTime,
       "TmnxSrrpPriorityStep": TmnxSrrpPriorityStep,
       "TmnxAiiType": TmnxAiiType,
       "ServObjDesc": ServObjDesc,
       "TMplsLspExpProfMapID": TMplsLspExpProfMapID,
       "TSysResource": TSysResource,
       "TmnxSpbFid": TmnxSpbFid,
       "TmnxSpbFidOrZero": TmnxSpbFidOrZero,
       "TmnxSpbBridgePriority": TmnxSpbBridgePriority,
       "TmnxSlopeMap": TmnxSlopeMap,
       "TmnxCdrType": TmnxCdrType,
       "TmnxThresholdGroupType": TmnxThresholdGroupType,
       "TmnxMobUeId": TmnxMobUeId,
       "TmnxMobUeIdType": TmnxMobUeIdType,
       "TmnxMobImsiStr": TmnxMobImsiStr,
       "TmnxVpnIpBackupFamily": TmnxVpnIpBackupFamily,
       "TmnxTunnelGroupId": TmnxTunnelGroupId,
       "TmnxTunnelGroupIdOrZero": TmnxTunnelGroupIdOrZero,
       "TmnxMobRatingGrpState": TmnxMobRatingGrpState,
       "TmnxMobPresenceState": TmnxMobPresenceState,
       "TmnxMobPdnGyChrgTriggerType": TmnxMobPdnGyChrgTriggerType,
       "TmnxMobPdnRefPointType": TmnxMobPdnRefPointType,
       "TmnxQosBytesHex": TmnxQosBytesHex,
       "TSiteOperStatus": TSiteOperStatus,
       "TmnxSpbFdbLocale": TmnxSpbFdbLocale,
       "TmnxSpbFdbState": TmnxSpbFdbState,
       "TmnxMobServRefPointType": TmnxMobServRefPointType,
       "TmnxMobAccessType": TmnxMobAccessType,
       "TmnxMobUeStrPrefix": TmnxMobUeStrPrefix,
       "TmnxCdrDiagnosticAction": TmnxCdrDiagnosticAction,
       "TmnxMplsTpGlobalID": TmnxMplsTpGlobalID,
       "TmnxMplsTpNodeID": TmnxMplsTpNodeID,
       "TmnxMplsTpTunnelType": TmnxMplsTpTunnelType,
       "TmnxVwmCardType": TmnxVwmCardType,
       "timetraTCMIBModule": timetraTCMIBModule}
)
