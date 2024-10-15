# SNMP MIB module (TIMETRA-BSX-NG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-BSX-NG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:02:00 2024
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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxHwIndexOrZero,
 TmnxSlotNumOrZero,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxHwIndexOrZero",
    "TmnxSlotNumOrZero",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(TEntryId,) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TEntryId")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxLogFileIdLogId,
 tmnxLogNotifyApInterval) = mibBuilder.importSymbols(
    "TIMETRA-LOG-MIB",
    "tmnxLogFileIdLogId",
    "tmnxLogNotifyApInterval")

(TmnxPortEncapType,) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "TmnxPortEncapType")

(tFCName,) = mibBuilder.importSymbols(
    "TIMETRA-QOS-MIB",
    "tFCName")

(SdpBindId,
 TAdaptationRule,
 TCIRRate,
 TDSCPNameOrEmpty,
 TFCNameOrEmpty,
 TIpProtocol,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRRate,
 TPriorityOrDefault,
 TQueueId,
 TTcpUdpPort,
 TmnxActionType,
 TmnxAdminState,
 TmnxBsxAarpId,
 TmnxBsxTransPrefPolicyId,
 TmnxBsxTransPrefPolicyIdOrZero,
 TmnxBsxTransitIpPolicyId,
 TmnxBsxTransitIpPolicyIdOrZero,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxSubRadServAlgorithm,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "SdpBindId",
    "TAdaptationRule",
    "TCIRRate",
    "TDSCPNameOrEmpty",
    "TFCNameOrEmpty",
    "TIpProtocol",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRRate",
    "TPriorityOrDefault",
    "TQueueId",
    "TTcpUdpPort",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxBsxAarpId",
    "TmnxBsxTransPrefPolicyId",
    "TmnxBsxTransPrefPolicyIdOrZero",
    "TmnxBsxTransitIpPolicyId",
    "TmnxBsxTransitIpPolicyIdOrZero",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxSubRadServAlgorithm",
    "TmnxVRtrIDOrZero")


# MODULE-IDENTITY

tmnxBsxNgMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 63)
)
tmnxBsxNgMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1908-12-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxBsxIsaAaGroupIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxBsxIsaAaGroupIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxBsxAaGrpPartIndex(Unsigned32, TextualConvention):
    status = "current"


class TmnxBsxFailToMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failToOpen", 1),
          ("failToWire", 0))
    )



class TmnxBsxPolicyVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("admin", 0),
          ("oper", 1))
    )



class TmnxBsxDirection(Integer32, TextualConvention):
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
        *(("both", 2),
          ("net2sub", 1),
          ("sub2net", 0))
    )



class TmnxBsxPolicerType(Integer32, TextualConvention):
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
        *(("dualBucketBandwidth", 2),
          ("flowCountLimit", 4),
          ("flowRateLimit", 3),
          ("none", 0),
          ("singleBucketBandwidth", 1))
    )



class TmnxBsxGranularity(Integer32, TextualConvention):
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
          ("subscriber", 2),
          ("system", 1))
    )



class TmnxBsxPolicerAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permitDeny", 0),
          ("priorityMark", 1))
    )



class TmnxBsxBurstSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )



class TmnxBsxOperator(Integer32, TextualConvention):
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
        *(("eq", 1),
          ("gt", 4),
          ("lt", 3),
          ("neq", 2),
          ("none", 0),
          ("range", 5))
    )



class TmnxBsxMdaRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("primary", 0))
    )



class TmnxBsxMdaActivityState(Integer32, TextualConvention):
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
        *(("active", 1),
          ("standby", 2),
          ("unavailable", 0))
    )



class TmnxBsxAaSubscriberType(Integer32, TextualConvention):
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
        *(("esm", 1),
          ("mobile", 5),
          ("sap", 2),
          ("spokeSdp", 3),
          ("transit", 4),
          ("unknown", 0))
    )



class TmnxBsxAaSubscriber(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TmnxBsxStatAaAcctCfgType(Integer32, TextualConvention):
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
        *(("aa-sub", 4),
          ("aa-sub-study-application", 6),
          ("aa-sub-study-protocol", 5),
          ("app-group", 3),
          ("application", 2),
          ("protocol", 1),
          ("unknown", 0))
    )



class TmnxBsxAaStatType(Integer32, TextualConvention):
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
        *(("app-group", 3),
          ("application", 2),
          ("chargingGroup", 4),
          ("protocol", 1),
          ("unknown", 0))
    )



class TmnxBsxAaStatExportMethod(Bits, TextualConvention):
    status = "current"


class TmnxBsxExprSubStringIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxBsxExprSubStringType(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("citrixApp", 7),
          ("h323ProductId", 9),
          ("httpHost", 1),
          ("httpReferrer", 3),
          ("httpUri", 2),
          ("httpUserAgent", 8),
          ("none", 0),
          ("sipMt", 6),
          ("sipUa", 4),
          ("sipUri", 5),
          ("tlsCsCommonName", 11),
          ("tlsCsOrgName", 10))
    )



class TmnxBsxExprSubString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TmnxBsxFirstPacketPolicy(Integer32, TextualConvention):
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
        *(("first-packet-trusted", 1),
          ("first-packet-validate", 2),
          ("none", 0))
    )



class TmnxBsxActionStatus(Integer32, TextualConvention):
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
          ("start", 1),
          ("stop", 2))
    )



class TmnxBsxAdminCtrl(Integer32, TextualConvention):
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
        *(("commit", 3),
          ("initialize", 2),
          ("none", 1))
    )



class TmnxBsxCustProtExprSubString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TmnxBsxProtocolDirection(Integer32, TextualConvention):
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
        *(("any", 3),
          ("client2server", 1),
          ("none", 0),
          ("server2client", 2))
    )



class TmnxBsxLoadBalanceStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("balancing", 0),
          ("complete", 1))
    )



class TmnxBsxCflowdExpType(Integer32, TextualConvention):
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
          ("rtpPerformance", 3),
          ("tcpPerformance", 2),
          ("volume", 1))
    )



class TmnxBsxCflowdPerfMeasType(Integer32, TextualConvention):
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
          ("rtp", 2),
          ("tcp", 1))
    )



class TmnxBsxAaSubStatsInterval(Integer32, TextualConvention):
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
        *(("realtime", 1),
          ("snapshot", 2),
          ("unknown", 0))
    )



class TmnxBsxAaSubAcctLossReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acctInvlExpiry", 1),
          ("noLoss", 0))
    )



class TmnxBsxAaSubAsoValDerivedFrom(Integer32, TextualConvention):
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
        *(("appProfile", 2),
          ("asoDefault", 1),
          ("none", 0),
          ("override", 3))
    )



class TmnxBsxAaSubPolicerResStatus(Integer32, TextualConvention):
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
        *(("exceeded", 3),
          ("none", 0),
          ("okay", 1),
          ("unknown", 2))
    )



class TmnxBsxStatIsaAaCfgType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aaPerformance", 1),
          ("unknown", 0))
    )



class TmnxBsxTransitSubOrigin(Bits, TextualConvention):
    status = "current"


class TmnxBsxTListAttribType(Integer32, TextualConvention):
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
          ("string", 2),
          ("uint", 1))
    )



class TmnxBsxTListAttribValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class TmnxBsxAqpHttpRedirFlowType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("droppedFlows", 1),
          ("none", 0))
    )



class TmnxBsxAarpInstState(Integer32, TextualConvention):
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
        *(("backup", 3),
          ("master", 2),
          ("remote", 1),
          ("standAlone", 0))
    )



class TmnxBsxAarpInstOperFlags(Bits, TextualConvention):
    status = "current"


class TmnxBsxAarpCommand(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forceEvaluate", 1),
          ("noCmd", 0))
    )



class TmnxBsxAarpServPointRole(Integer32, TextualConvention):
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
        *(("dualHomed", 1),
          ("interfaceShuntNet", 5),
          ("interfaceShuntSub", 4),
          ("none", 0),
          ("pipeShuntNet", 3),
          ("pipeShuntSub", 2))
    )



class TmnxBsxAarpServPointType(Integer32, TextualConvention):
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
        *(("sap", 1),
          ("spokeSdp", 2),
          ("unknown", 0))
    )



class TmnxBsxAarpServPoint(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxBsxConformance_ObjectIdentity = ObjectIdentity
tmnxBsxConformance = _TmnxBsxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63)
)
_TmnxBsxCompliances_ObjectIdentity = ObjectIdentity
tmnxBsxCompliances = _TmnxBsxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 1)
)
_TmnxBsxGroups_ObjectIdentity = ObjectIdentity
tmnxBsxGroups = _TmnxBsxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2)
)
_TmnxBsxMdaGroups_ObjectIdentity = ObjectIdentity
tmnxBsxMdaGroups = _TmnxBsxMdaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 6)
)
_TmnxBsxObsoleteGroups_ObjectIdentity = ObjectIdentity
tmnxBsxObsoleteGroups = _TmnxBsxObsoleteGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 7)
)
_TmnxBsxPolicyGroups_ObjectIdentity = ObjectIdentity
tmnxBsxPolicyGroups = _TmnxBsxPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 8)
)
_TmnxBsxNotificationGroups_ObjectIdentity = ObjectIdentity
tmnxBsxNotificationGroups = _TmnxBsxNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 10)
)
_TmnxBsxCflowdGroups_ObjectIdentity = ObjectIdentity
tmnxBsxCflowdGroups = _TmnxBsxCflowdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 11)
)
_TmnxBsxOvrdGroups_ObjectIdentity = ObjectIdentity
tmnxBsxOvrdGroups = _TmnxBsxOvrdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 12)
)
_TmnxBsxNotifyObjsGroups_ObjectIdentity = ObjectIdentity
tmnxBsxNotifyObjsGroups = _TmnxBsxNotifyObjsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 13)
)
_TmnxBsxTransitGroups_ObjectIdentity = ObjectIdentity
tmnxBsxTransitGroups = _TmnxBsxTransitGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 14)
)
_TmnxBsxStatsGroups_ObjectIdentity = ObjectIdentity
tmnxBsxStatsGroups = _TmnxBsxStatsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 15)
)
_TmnxBsxMobileGatewayGroups_ObjectIdentity = ObjectIdentity
tmnxBsxMobileGatewayGroups = _TmnxBsxMobileGatewayGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 16)
)
_TmnxBsxHttpRedirGroups_ObjectIdentity = ObjectIdentity
tmnxBsxHttpRedirGroups = _TmnxBsxHttpRedirGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 17)
)
_TmnxBsxStaticObjGroups_ObjectIdentity = ObjectIdentity
tmnxBsxStaticObjGroups = _TmnxBsxStaticObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 18)
)
_TmnxBsxRedundancyObjGroups_ObjectIdentity = ObjectIdentity
tmnxBsxRedundancyObjGroups = _TmnxBsxRedundancyObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 19)
)
_TmnxBsxHttpEnrichObjGroups_ObjectIdentity = ObjectIdentity
tmnxBsxHttpEnrichObjGroups = _TmnxBsxHttpEnrichObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 20)
)
_TmnxBsxRadiusAccountingGroups_ObjectIdentity = ObjectIdentity
tmnxBsxRadiusAccountingGroups = _TmnxBsxRadiusAccountingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 21)
)
_TmnxBsxObjs_ObjectIdentity = ObjectIdentity
tmnxBsxObjs = _TmnxBsxObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63)
)
_TmnxBsxMdaObjs_ObjectIdentity = ObjectIdentity
tmnxBsxMdaObjs = _TmnxBsxMdaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1)
)
_TmnxBsxMdaScalars_ObjectIdentity = ObjectIdentity
tmnxBsxMdaScalars = _TmnxBsxMdaScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 1)
)
_TmnxBsxIsaAaGrpLastChangeTime_Type = TimeStamp
_TmnxBsxIsaAaGrpLastChangeTime_Object = MibScalar
tmnxBsxIsaAaGrpLastChangeTime = _TmnxBsxIsaAaGrpLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 1, 1),
    _TmnxBsxIsaAaGrpLastChangeTime_Type()
)
tmnxBsxIsaAaGrpLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpLastChangeTime.setStatus("current")
_TmnxBsxIsaAaGrpFcLastChangeTime_Type = TimeStamp
_TmnxBsxIsaAaGrpFcLastChangeTime_Object = MibScalar
tmnxBsxIsaAaGrpFcLastChangeTime = _TmnxBsxIsaAaGrpFcLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 1, 2),
    _TmnxBsxIsaAaGrpFcLastChangeTime_Type()
)
tmnxBsxIsaAaGrpFcLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFcLastChangeTime.setStatus("current")
_TmnxBsxIsaAaGrpMdaLastChangeTime_Type = TimeStamp
_TmnxBsxIsaAaGrpMdaLastChangeTime_Object = MibScalar
tmnxBsxIsaAaGrpMdaLastChangeTime = _TmnxBsxIsaAaGrpMdaLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 1, 3),
    _TmnxBsxIsaAaGrpMdaLastChangeTime_Type()
)
tmnxBsxIsaAaGrpMdaLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpMdaLastChangeTime.setStatus("current")
_TmnxBsxAaGrpPartLastChangeTime_Type = TimeStamp
_TmnxBsxAaGrpPartLastChangeTime_Object = MibScalar
tmnxBsxAaGrpPartLastChangeTime = _TmnxBsxAaGrpPartLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 1, 4),
    _TmnxBsxAaGrpPartLastChangeTime_Type()
)
tmnxBsxAaGrpPartLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaGrpPartLastChangeTime.setStatus("current")
_TmnxBsxAaWap1xLastChangeTime_Type = TimeStamp
_TmnxBsxAaWap1xLastChangeTime_Object = MibScalar
tmnxBsxAaWap1xLastChangeTime = _TmnxBsxAaWap1xLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 1, 5),
    _TmnxBsxAaWap1xLastChangeTime_Type()
)
tmnxBsxAaWap1xLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaWap1xLastChangeTime.setStatus("current")
_TmnxBsxIsaAaGrpTable_Object = MibTable
tmnxBsxIsaAaGrpTable = _TmnxBsxIsaAaGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpTable.setStatus("current")
_TmnxBsxIsaAaGrpEntry_Object = MibTableRow
tmnxBsxIsaAaGrpEntry = _TmnxBsxIsaAaGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1)
)
tmnxBsxIsaAaGrpEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpEntry.setStatus("current")
_TmnxBsxIsaAaGroupIndex_Type = TmnxBsxIsaAaGroupIndex
_TmnxBsxIsaAaGroupIndex_Object = MibTableColumn
tmnxBsxIsaAaGroupIndex = _TmnxBsxIsaAaGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 1),
    _TmnxBsxIsaAaGroupIndex_Type()
)
tmnxBsxIsaAaGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGroupIndex.setStatus("current")
_TmnxBsxIsaAaGrpRowStatus_Type = RowStatus
_TmnxBsxIsaAaGrpRowStatus_Object = MibTableColumn
tmnxBsxIsaAaGrpRowStatus = _TmnxBsxIsaAaGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 2),
    _TmnxBsxIsaAaGrpRowStatus_Type()
)
tmnxBsxIsaAaGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpRowStatus.setStatus("current")
_TmnxBsxIsaAaGrpRowLastChange_Type = TimeStamp
_TmnxBsxIsaAaGrpRowLastChange_Object = MibTableColumn
tmnxBsxIsaAaGrpRowLastChange = _TmnxBsxIsaAaGrpRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 3),
    _TmnxBsxIsaAaGrpRowLastChange_Type()
)
tmnxBsxIsaAaGrpRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpRowLastChange.setStatus("current")
_TmnxBsxIsaAaGrpDescription_Type = TItemDescription
_TmnxBsxIsaAaGrpDescription_Object = MibTableColumn
tmnxBsxIsaAaGrpDescription = _TmnxBsxIsaAaGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 4),
    _TmnxBsxIsaAaGrpDescription_Type()
)
tmnxBsxIsaAaGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpDescription.setStatus("current")


class _TmnxBsxIsaAaGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxIsaAaGrpAdminState based on TmnxAdminState"""


_TmnxBsxIsaAaGrpAdminState_Object = MibTableColumn
tmnxBsxIsaAaGrpAdminState = _TmnxBsxIsaAaGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 5),
    _TmnxBsxIsaAaGrpAdminState_Type()
)
tmnxBsxIsaAaGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpAdminState.setStatus("current")


class _TmnxBsxIsaAaGrpOperState_Type(TmnxOperState):
    """Custom type tmnxBsxIsaAaGrpOperState based on TmnxOperState"""


_TmnxBsxIsaAaGrpOperState_Object = MibTableColumn
tmnxBsxIsaAaGrpOperState = _TmnxBsxIsaAaGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 6),
    _TmnxBsxIsaAaGrpOperState_Type()
)
tmnxBsxIsaAaGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpOperState.setStatus("current")


class _TmnxBsxIsaAaGrpFailToMode_Type(TmnxBsxFailToMode):
    """Custom type tmnxBsxIsaAaGrpFailToMode based on TmnxBsxFailToMode"""


_TmnxBsxIsaAaGrpFailToMode_Object = MibTableColumn
tmnxBsxIsaAaGrpFailToMode = _TmnxBsxIsaAaGrpFailToMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 7),
    _TmnxBsxIsaAaGrpFailToMode_Type()
)
tmnxBsxIsaAaGrpFailToMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFailToMode.setStatus("current")


class _TmnxBsxIsaAaGrpFromSubPool_Type(TNamedItem):
    """Custom type tmnxBsxIsaAaGrpFromSubPool based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxBsxIsaAaGrpFromSubPool_Object = MibTableColumn
tmnxBsxIsaAaGrpFromSubPool = _TmnxBsxIsaAaGrpFromSubPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 8),
    _TmnxBsxIsaAaGrpFromSubPool_Type()
)
tmnxBsxIsaAaGrpFromSubPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFromSubPool.setStatus("current")


class _TmnxBsxIsaAaGrpFromSubResvCbs_Type(Integer32):
    """Custom type tmnxBsxIsaAaGrpFromSubResvCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TmnxBsxIsaAaGrpFromSubResvCbs_Type.__name__ = "Integer32"
_TmnxBsxIsaAaGrpFromSubResvCbs_Object = MibTableColumn
tmnxBsxIsaAaGrpFromSubResvCbs = _TmnxBsxIsaAaGrpFromSubResvCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 9),
    _TmnxBsxIsaAaGrpFromSubResvCbs_Type()
)
tmnxBsxIsaAaGrpFromSubResvCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFromSubResvCbs.setStatus("current")


class _TmnxBsxIsaAaGrpFromSubSlpPolicy_Type(TNamedItem):
    """Custom type tmnxBsxIsaAaGrpFromSubSlpPolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxBsxIsaAaGrpFromSubSlpPolicy_Object = MibTableColumn
tmnxBsxIsaAaGrpFromSubSlpPolicy = _TmnxBsxIsaAaGrpFromSubSlpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 10),
    _TmnxBsxIsaAaGrpFromSubSlpPolicy_Type()
)
tmnxBsxIsaAaGrpFromSubSlpPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFromSubSlpPolicy.setStatus("current")


class _TmnxBsxIsaAaGrpFromSubQuePolicy_Type(TNamedItem):
    """Custom type tmnxBsxIsaAaGrpFromSubQuePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxBsxIsaAaGrpFromSubQuePolicy_Object = MibTableColumn
tmnxBsxIsaAaGrpFromSubQuePolicy = _TmnxBsxIsaAaGrpFromSubQuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 11),
    _TmnxBsxIsaAaGrpFromSubQuePolicy_Type()
)
tmnxBsxIsaAaGrpFromSubQuePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFromSubQuePolicy.setStatus("current")
_TmnxBsxIsaAaGrpFromSubSchPolicy_Type = TNamedItemOrEmpty
_TmnxBsxIsaAaGrpFromSubSchPolicy_Object = MibTableColumn
tmnxBsxIsaAaGrpFromSubSchPolicy = _TmnxBsxIsaAaGrpFromSubSchPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 12),
    _TmnxBsxIsaAaGrpFromSubSchPolicy_Type()
)
tmnxBsxIsaAaGrpFromSubSchPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFromSubSchPolicy.setStatus("current")


class _TmnxBsxIsaAaGrpToSubPool_Type(TNamedItem):
    """Custom type tmnxBsxIsaAaGrpToSubPool based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxBsxIsaAaGrpToSubPool_Object = MibTableColumn
tmnxBsxIsaAaGrpToSubPool = _TmnxBsxIsaAaGrpToSubPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 13),
    _TmnxBsxIsaAaGrpToSubPool_Type()
)
tmnxBsxIsaAaGrpToSubPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSubPool.setStatus("current")


class _TmnxBsxIsaAaGrpToSubResvCbs_Type(Integer32):
    """Custom type tmnxBsxIsaAaGrpToSubResvCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TmnxBsxIsaAaGrpToSubResvCbs_Type.__name__ = "Integer32"
_TmnxBsxIsaAaGrpToSubResvCbs_Object = MibTableColumn
tmnxBsxIsaAaGrpToSubResvCbs = _TmnxBsxIsaAaGrpToSubResvCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 14),
    _TmnxBsxIsaAaGrpToSubResvCbs_Type()
)
tmnxBsxIsaAaGrpToSubResvCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSubResvCbs.setStatus("current")


class _TmnxBsxIsaAaGrpToSubSlpPolicy_Type(TNamedItem):
    """Custom type tmnxBsxIsaAaGrpToSubSlpPolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxBsxIsaAaGrpToSubSlpPolicy_Object = MibTableColumn
tmnxBsxIsaAaGrpToSubSlpPolicy = _TmnxBsxIsaAaGrpToSubSlpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 15),
    _TmnxBsxIsaAaGrpToSubSlpPolicy_Type()
)
tmnxBsxIsaAaGrpToSubSlpPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSubSlpPolicy.setStatus("current")


class _TmnxBsxIsaAaGrpToSubQuePolicy_Type(TNamedItem):
    """Custom type tmnxBsxIsaAaGrpToSubQuePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxBsxIsaAaGrpToSubQuePolicy_Object = MibTableColumn
tmnxBsxIsaAaGrpToSubQuePolicy = _TmnxBsxIsaAaGrpToSubQuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 16),
    _TmnxBsxIsaAaGrpToSubQuePolicy_Type()
)
tmnxBsxIsaAaGrpToSubQuePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSubQuePolicy.setStatus("current")
_TmnxBsxIsaAaGrpToSubSchPolicy_Type = TNamedItemOrEmpty
_TmnxBsxIsaAaGrpToSubSchPolicy_Object = MibTableColumn
tmnxBsxIsaAaGrpToSubSchPolicy = _TmnxBsxIsaAaGrpToSubSchPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 17),
    _TmnxBsxIsaAaGrpToSubSchPolicy_Type()
)
tmnxBsxIsaAaGrpToSubSchPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSubSchPolicy.setStatus("current")


class _TmnxBsxIsaAaGrpIngressPool_Type(TNamedItem):
    """Custom type tmnxBsxIsaAaGrpIngressPool based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxBsxIsaAaGrpIngressPool_Object = MibTableColumn
tmnxBsxIsaAaGrpIngressPool = _TmnxBsxIsaAaGrpIngressPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 18),
    _TmnxBsxIsaAaGrpIngressPool_Type()
)
tmnxBsxIsaAaGrpIngressPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpIngressPool.setStatus("obsolete")


class _TmnxBsxIsaAaGrpIngressResvCbs_Type(Integer32):
    """Custom type tmnxBsxIsaAaGrpIngressResvCbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_TmnxBsxIsaAaGrpIngressResvCbs_Type.__name__ = "Integer32"
_TmnxBsxIsaAaGrpIngressResvCbs_Object = MibTableColumn
tmnxBsxIsaAaGrpIngressResvCbs = _TmnxBsxIsaAaGrpIngressResvCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 19),
    _TmnxBsxIsaAaGrpIngressResvCbs_Type()
)
tmnxBsxIsaAaGrpIngressResvCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpIngressResvCbs.setStatus("obsolete")


class _TmnxBsxIsaAaGrpIngressSlpPolicy_Type(TNamedItem):
    """Custom type tmnxBsxIsaAaGrpIngressSlpPolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxBsxIsaAaGrpIngressSlpPolicy_Object = MibTableColumn
tmnxBsxIsaAaGrpIngressSlpPolicy = _TmnxBsxIsaAaGrpIngressSlpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 20),
    _TmnxBsxIsaAaGrpIngressSlpPolicy_Type()
)
tmnxBsxIsaAaGrpIngressSlpPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpIngressSlpPolicy.setStatus("obsolete")


class _TmnxBsxIsaAaGrpIngressQuePolicy_Type(TNamedItem):
    """Custom type tmnxBsxIsaAaGrpIngressQuePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxBsxIsaAaGrpIngressQuePolicy_Object = MibTableColumn
tmnxBsxIsaAaGrpIngressQuePolicy = _TmnxBsxIsaAaGrpIngressQuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 21),
    _TmnxBsxIsaAaGrpIngressQuePolicy_Type()
)
tmnxBsxIsaAaGrpIngressQuePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpIngressQuePolicy.setStatus("obsolete")
_TmnxBsxIsaAaGrpActivityChange_Type = TimeStamp
_TmnxBsxIsaAaGrpActivityChange_Object = MibTableColumn
tmnxBsxIsaAaGrpActivityChange = _TmnxBsxIsaAaGrpActivityChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 22),
    _TmnxBsxIsaAaGrpActivityChange_Type()
)
tmnxBsxIsaAaGrpActivityChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpActivityChange.setStatus("current")


class _TmnxBsxIsaAaGrpPartitions_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxIsaAaGrpPartitions based on TmnxEnabledDisabled"""


_TmnxBsxIsaAaGrpPartitions_Object = MibTableColumn
tmnxBsxIsaAaGrpPartitions = _TmnxBsxIsaAaGrpPartitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 23),
    _TmnxBsxIsaAaGrpPartitions_Type()
)
tmnxBsxIsaAaGrpPartitions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpPartitions.setStatus("current")


class _TmnxBsxIsaAaGrpCapCostLowThres_Type(Unsigned32):
    """Custom type tmnxBsxIsaAaGrpCapCostLowThres based on Unsigned32"""
    defaultValue = 0


_TmnxBsxIsaAaGrpCapCostLowThres_Object = MibTableColumn
tmnxBsxIsaAaGrpCapCostLowThres = _TmnxBsxIsaAaGrpCapCostLowThres_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 24),
    _TmnxBsxIsaAaGrpCapCostLowThres_Type()
)
tmnxBsxIsaAaGrpCapCostLowThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpCapCostLowThres.setStatus("current")


class _TmnxBsxIsaAaGrpCapCostHighThres_Type(Unsigned32):
    """Custom type tmnxBsxIsaAaGrpCapCostHighThres based on Unsigned32"""
    defaultHexValue = 4294967295


_TmnxBsxIsaAaGrpCapCostHighThres_Object = MibTableColumn
tmnxBsxIsaAaGrpCapCostHighThres = _TmnxBsxIsaAaGrpCapCostHighThres_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 25),
    _TmnxBsxIsaAaGrpCapCostHighThres_Type()
)
tmnxBsxIsaAaGrpCapCostHighThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpCapCostHighThres.setStatus("current")
_TmnxBsxIsaAaGrpLoadBalanceStatus_Type = TmnxBsxLoadBalanceStatus
_TmnxBsxIsaAaGrpLoadBalanceStatus_Object = MibTableColumn
tmnxBsxIsaAaGrpLoadBalanceStatus = _TmnxBsxIsaAaGrpLoadBalanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 26),
    _TmnxBsxIsaAaGrpLoadBalanceStatus_Type()
)
tmnxBsxIsaAaGrpLoadBalanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpLoadBalanceStatus.setStatus("current")
_TmnxBsxIsaAaGrpUnassignedEsmSubs_Type = Gauge32
_TmnxBsxIsaAaGrpUnassignedEsmSubs_Object = MibTableColumn
tmnxBsxIsaAaGrpUnassignedEsmSubs = _TmnxBsxIsaAaGrpUnassignedEsmSubs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 27),
    _TmnxBsxIsaAaGrpUnassignedEsmSubs_Type()
)
tmnxBsxIsaAaGrpUnassignedEsmSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpUnassignedEsmSubs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpUnassignedEsmSubs.setUnits("subscribers")
_TmnxBsxIsaAaGrpUnassignedSapSubs_Type = Gauge32
_TmnxBsxIsaAaGrpUnassignedSapSubs_Object = MibTableColumn
tmnxBsxIsaAaGrpUnassignedSapSubs = _TmnxBsxIsaAaGrpUnassignedSapSubs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 28),
    _TmnxBsxIsaAaGrpUnassignedSapSubs_Type()
)
tmnxBsxIsaAaGrpUnassignedSapSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpUnassignedSapSubs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpUnassignedSapSubs.setUnits("subscribers")
_TmnxBsxIsaAaGrpUnassignedSpkSubs_Type = Gauge32
_TmnxBsxIsaAaGrpUnassignedSpkSubs_Object = MibTableColumn
tmnxBsxIsaAaGrpUnassignedSpkSubs = _TmnxBsxIsaAaGrpUnassignedSpkSubs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 29),
    _TmnxBsxIsaAaGrpUnassignedSpkSubs_Type()
)
tmnxBsxIsaAaGrpUnassignedSpkSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpUnassignedSpkSubs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpUnassignedSpkSubs.setUnits("subscribers")
_TmnxBsxIsaAaGrpUnassignedTIpSubs_Type = Gauge32
_TmnxBsxIsaAaGrpUnassignedTIpSubs_Object = MibTableColumn
tmnxBsxIsaAaGrpUnassignedTIpSubs = _TmnxBsxIsaAaGrpUnassignedTIpSubs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 30),
    _TmnxBsxIsaAaGrpUnassignedTIpSubs_Type()
)
tmnxBsxIsaAaGrpUnassignedTIpSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpUnassignedTIpSubs.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpUnassignedTIpSubs.setUnits("subscribers")


class _TmnxBsxIsaAaGrpAaSubScale_Type(Integer32):
    """Custom type tmnxBsxIsaAaGrpAaSubScale based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mobileGateway", 2),
          ("residential", 0),
          ("vpn", 1))
    )


_TmnxBsxIsaAaGrpAaSubScale_Type.__name__ = "Integer32"
_TmnxBsxIsaAaGrpAaSubScale_Object = MibTableColumn
tmnxBsxIsaAaGrpAaSubScale = _TmnxBsxIsaAaGrpAaSubScale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 31),
    _TmnxBsxIsaAaGrpAaSubScale_Type()
)
tmnxBsxIsaAaGrpAaSubScale.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpAaSubScale.setStatus("current")


class _TmnxBsxIsaAaGrpOverloadCutThru_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxIsaAaGrpOverloadCutThru based on TmnxEnabledDisabled"""


_TmnxBsxIsaAaGrpOverloadCutThru_Object = MibTableColumn
tmnxBsxIsaAaGrpOverloadCutThru = _TmnxBsxIsaAaGrpOverloadCutThru_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 32),
    _TmnxBsxIsaAaGrpOverloadCutThru_Type()
)
tmnxBsxIsaAaGrpOverloadCutThru.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpOverloadCutThru.setStatus("current")


class _TmnxBsxIsaAaGrpFromSubWaSBfHiWmk_Type(Integer32):
    """Custom type tmnxBsxIsaAaGrpFromSubWaSBfHiWmk based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100),
    )


_TmnxBsxIsaAaGrpFromSubWaSBfHiWmk_Type.__name__ = "Integer32"
_TmnxBsxIsaAaGrpFromSubWaSBfHiWmk_Object = MibTableColumn
tmnxBsxIsaAaGrpFromSubWaSBfHiWmk = _TmnxBsxIsaAaGrpFromSubWaSBfHiWmk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 33),
    _TmnxBsxIsaAaGrpFromSubWaSBfHiWmk_Type()
)
tmnxBsxIsaAaGrpFromSubWaSBfHiWmk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFromSubWaSBfHiWmk.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFromSubWaSBfHiWmk.setUnits("percent")


class _TmnxBsxIsaAaGrpFromSubWaSBfLoWmk_Type(Integer32):
    """Custom type tmnxBsxIsaAaGrpFromSubWaSBfLoWmk based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxBsxIsaAaGrpFromSubWaSBfLoWmk_Type.__name__ = "Integer32"
_TmnxBsxIsaAaGrpFromSubWaSBfLoWmk_Object = MibTableColumn
tmnxBsxIsaAaGrpFromSubWaSBfLoWmk = _TmnxBsxIsaAaGrpFromSubWaSBfLoWmk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 34),
    _TmnxBsxIsaAaGrpFromSubWaSBfLoWmk_Type()
)
tmnxBsxIsaAaGrpFromSubWaSBfLoWmk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFromSubWaSBfLoWmk.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFromSubWaSBfLoWmk.setUnits("percent")


class _TmnxBsxIsaAaGrpToSubWaSBfHiWmk_Type(Integer32):
    """Custom type tmnxBsxIsaAaGrpToSubWaSBfHiWmk based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100),
    )


_TmnxBsxIsaAaGrpToSubWaSBfHiWmk_Type.__name__ = "Integer32"
_TmnxBsxIsaAaGrpToSubWaSBfHiWmk_Object = MibTableColumn
tmnxBsxIsaAaGrpToSubWaSBfHiWmk = _TmnxBsxIsaAaGrpToSubWaSBfHiWmk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 35),
    _TmnxBsxIsaAaGrpToSubWaSBfHiWmk_Type()
)
tmnxBsxIsaAaGrpToSubWaSBfHiWmk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSubWaSBfHiWmk.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSubWaSBfHiWmk.setUnits("percent")


class _TmnxBsxIsaAaGrpToSubWaSBfLoWmk_Type(Integer32):
    """Custom type tmnxBsxIsaAaGrpToSubWaSBfLoWmk based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxBsxIsaAaGrpToSubWaSBfLoWmk_Type.__name__ = "Integer32"
_TmnxBsxIsaAaGrpToSubWaSBfLoWmk_Object = MibTableColumn
tmnxBsxIsaAaGrpToSubWaSBfLoWmk = _TmnxBsxIsaAaGrpToSubWaSBfLoWmk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 36),
    _TmnxBsxIsaAaGrpToSubWaSBfLoWmk_Type()
)
tmnxBsxIsaAaGrpToSubWaSBfLoWmk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSubWaSBfLoWmk.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSubWaSBfLoWmk.setUnits("percent")


class _TmnxBsxIsaAaGrpTransPrefV4NmEntr_Type(Unsigned32):
    """Custom type tmnxBsxIsaAaGrpTransPrefV4NmEntr based on Unsigned32"""
    defaultValue = 0


_TmnxBsxIsaAaGrpTransPrefV4NmEntr_Object = MibTableColumn
tmnxBsxIsaAaGrpTransPrefV4NmEntr = _TmnxBsxIsaAaGrpTransPrefV4NmEntr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 37),
    _TmnxBsxIsaAaGrpTransPrefV4NmEntr_Type()
)
tmnxBsxIsaAaGrpTransPrefV4NmEntr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpTransPrefV4NmEntr.setStatus("current")


class _TmnxBsxIsaAaGrpTransPrefV6NmEntr_Type(Unsigned32):
    """Custom type tmnxBsxIsaAaGrpTransPrefV6NmEntr based on Unsigned32"""
    defaultValue = 0


_TmnxBsxIsaAaGrpTransPrefV6NmEntr_Object = MibTableColumn
tmnxBsxIsaAaGrpTransPrefV6NmEntr = _TmnxBsxIsaAaGrpTransPrefV6NmEntr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 38),
    _TmnxBsxIsaAaGrpTransPrefV6NmEntr_Type()
)
tmnxBsxIsaAaGrpTransPrefV6NmEntr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpTransPrefV6NmEntr.setStatus("current")


class _TmnxBsxIsaAaGrpTransPrefV6RmEntr_Type(Unsigned32):
    """Custom type tmnxBsxIsaAaGrpTransPrefV6RmEntr based on Unsigned32"""
    defaultValue = 0


_TmnxBsxIsaAaGrpTransPrefV6RmEntr_Object = MibTableColumn
tmnxBsxIsaAaGrpTransPrefV6RmEntr = _TmnxBsxIsaAaGrpTransPrefV6RmEntr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 2, 1, 39),
    _TmnxBsxIsaAaGrpTransPrefV6RmEntr_Type()
)
tmnxBsxIsaAaGrpTransPrefV6RmEntr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpTransPrefV6RmEntr.setStatus("current")
_TmnxBsxIsaAaGrpFcTable_Object = MibTable
tmnxBsxIsaAaGrpFcTable = _TmnxBsxIsaAaGrpFcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFcTable.setStatus("current")
_TmnxBsxIsaAaGrpFcEntry_Object = MibTableRow
tmnxBsxIsaAaGrpFcEntry = _TmnxBsxIsaAaGrpFcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 3, 1)
)
tmnxBsxIsaAaGrpFcEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-QOS-MIB", "tFCName"),
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFcEntry.setStatus("current")
_TmnxBsxIsaAaGrpFcRowStatus_Type = RowStatus
_TmnxBsxIsaAaGrpFcRowStatus_Object = MibTableColumn
tmnxBsxIsaAaGrpFcRowStatus = _TmnxBsxIsaAaGrpFcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 3, 1, 1),
    _TmnxBsxIsaAaGrpFcRowStatus_Type()
)
tmnxBsxIsaAaGrpFcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFcRowStatus.setStatus("current")
_TmnxBsxIsaAaGrpFcRowLastChange_Type = TimeStamp
_TmnxBsxIsaAaGrpFcRowLastChange_Object = MibTableColumn
tmnxBsxIsaAaGrpFcRowLastChange = _TmnxBsxIsaAaGrpFcRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 3, 1, 2),
    _TmnxBsxIsaAaGrpFcRowLastChange_Type()
)
tmnxBsxIsaAaGrpFcRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFcRowLastChange.setStatus("current")
_TmnxBsxGrpMdaTable_Object = MibTable
tmnxBsxGrpMdaTable = _TmnxBsxGrpMdaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaTable.setStatus("current")
_TmnxBsxGrpMdaEntry_Object = MibTableRow
tmnxBsxGrpMdaEntry = _TmnxBsxGrpMdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1)
)
tmnxBsxGrpMdaEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaEntry.setStatus("current")
_TmnxBsxCardSlotNum_Type = TmnxSlotNumOrZero
_TmnxBsxCardSlotNum_Object = MibTableColumn
tmnxBsxCardSlotNum = _TmnxBsxCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 1),
    _TmnxBsxCardSlotNum_Type()
)
tmnxBsxCardSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxCardSlotNum.setStatus("current")
_TmnxBsxGrpMdaRowStatus_Type = RowStatus
_TmnxBsxGrpMdaRowStatus_Object = MibTableColumn
tmnxBsxGrpMdaRowStatus = _TmnxBsxGrpMdaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 2),
    _TmnxBsxGrpMdaRowStatus_Type()
)
tmnxBsxGrpMdaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaRowStatus.setStatus("current")
_TmnxBsxGrpMdaRowLastChange_Type = TimeStamp
_TmnxBsxGrpMdaRowLastChange_Object = MibTableColumn
tmnxBsxGrpMdaRowLastChange = _TmnxBsxGrpMdaRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 3),
    _TmnxBsxGrpMdaRowLastChange_Type()
)
tmnxBsxGrpMdaRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaRowLastChange.setStatus("current")


class _TmnxBsxGrpMdaRole_Type(TmnxBsxMdaRole):
    """Custom type tmnxBsxGrpMdaRole based on TmnxBsxMdaRole"""


_TmnxBsxGrpMdaRole_Object = MibTableColumn
tmnxBsxGrpMdaRole = _TmnxBsxGrpMdaRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 4),
    _TmnxBsxGrpMdaRole_Type()
)
tmnxBsxGrpMdaRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaRole.setStatus("current")


class _TmnxBsxGrpMdaActivityState_Type(TmnxBsxMdaActivityState):
    """Custom type tmnxBsxGrpMdaActivityState based on TmnxBsxMdaActivityState"""


_TmnxBsxGrpMdaActivityState_Object = MibTableColumn
tmnxBsxGrpMdaActivityState = _TmnxBsxGrpMdaActivityState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 5),
    _TmnxBsxGrpMdaActivityState_Type()
)
tmnxBsxGrpMdaActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaActivityState.setStatus("current")
_TmnxBsxGrpMdaActivityChange_Type = TimeStamp
_TmnxBsxGrpMdaActivityChange_Object = MibTableColumn
tmnxBsxGrpMdaActivityChange = _TmnxBsxGrpMdaActivityChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 6),
    _TmnxBsxGrpMdaActivityChange_Type()
)
tmnxBsxGrpMdaActivityChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaActivityChange.setStatus("current")
_TmnxBsxGrpMdaEsmSubscribers_Type = Gauge32
_TmnxBsxGrpMdaEsmSubscribers_Object = MibTableColumn
tmnxBsxGrpMdaEsmSubscribers = _TmnxBsxGrpMdaEsmSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 7),
    _TmnxBsxGrpMdaEsmSubscribers_Type()
)
tmnxBsxGrpMdaEsmSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaEsmSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaEsmSubscribers.setUnits("subscribers")
_TmnxBsxGrpMdaSapSubscribers_Type = Gauge32
_TmnxBsxGrpMdaSapSubscribers_Object = MibTableColumn
tmnxBsxGrpMdaSapSubscribers = _TmnxBsxGrpMdaSapSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 8),
    _TmnxBsxGrpMdaSapSubscribers_Type()
)
tmnxBsxGrpMdaSapSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaSapSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaSapSubscribers.setUnits("subscribers")
_TmnxBsxGrpMdaSpokeSdpSubscribers_Type = Gauge32
_TmnxBsxGrpMdaSpokeSdpSubscribers_Object = MibTableColumn
tmnxBsxGrpMdaSpokeSdpSubscribers = _TmnxBsxGrpMdaSpokeSdpSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 9),
    _TmnxBsxGrpMdaSpokeSdpSubscribers_Type()
)
tmnxBsxGrpMdaSpokeSdpSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaSpokeSdpSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaSpokeSdpSubscribers.setUnits("subscribers")
_TmnxBsxGrpMdaCapacityCost_Type = Gauge32
_TmnxBsxGrpMdaCapacityCost_Object = MibTableColumn
tmnxBsxGrpMdaCapacityCost = _TmnxBsxGrpMdaCapacityCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 10),
    _TmnxBsxGrpMdaCapacityCost_Type()
)
tmnxBsxGrpMdaCapacityCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaCapacityCost.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaCapacityCost.setUnits("cost")
_TmnxBsxGrpMdaStatsResourceCount_Type = Gauge32
_TmnxBsxGrpMdaStatsResourceCount_Object = MibTableColumn
tmnxBsxGrpMdaStatsResourceCount = _TmnxBsxGrpMdaStatsResourceCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 11),
    _TmnxBsxGrpMdaStatsResourceCount_Type()
)
tmnxBsxGrpMdaStatsResourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaStatsResourceCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaStatsResourceCount.setUnits("resources")
_TmnxBsxGrpMdaTransitIpSubs_Type = Gauge32
_TmnxBsxGrpMdaTransitIpSubs_Object = MibTableColumn
tmnxBsxGrpMdaTransitIpSubs = _TmnxBsxGrpMdaTransitIpSubs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 12),
    _TmnxBsxGrpMdaTransitIpSubs_Type()
)
tmnxBsxGrpMdaTransitIpSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaTransitIpSubs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaTransitIpSubs.setUnits("subscribers")
_TmnxBsxGrpMdaTransitIpAddrs_Type = Gauge32
_TmnxBsxGrpMdaTransitIpAddrs_Object = MibTableColumn
tmnxBsxGrpMdaTransitIpAddrs = _TmnxBsxGrpMdaTransitIpAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 13),
    _TmnxBsxGrpMdaTransitIpAddrs_Type()
)
tmnxBsxGrpMdaTransitIpAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaTransitIpAddrs.setStatus("current")
_TmnxBsxGrpMdaTransitSubs_Type = Gauge32
_TmnxBsxGrpMdaTransitSubs_Object = MibTableColumn
tmnxBsxGrpMdaTransitSubs = _TmnxBsxGrpMdaTransitSubs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 14),
    _TmnxBsxGrpMdaTransitSubs_Type()
)
tmnxBsxGrpMdaTransitSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaTransitSubs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaTransitSubs.setUnits("subscribers")
_TmnxBsxGrpMdaTransPrefEntries_Type = Gauge32
_TmnxBsxGrpMdaTransPrefEntries_Object = MibTableColumn
tmnxBsxGrpMdaTransPrefEntries = _TmnxBsxGrpMdaTransPrefEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 15),
    _TmnxBsxGrpMdaTransPrefEntries_Type()
)
tmnxBsxGrpMdaTransPrefEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaTransPrefEntries.setStatus("obsolete")
_TmnxBsxGrpMdaTransPrefV4Entr_Type = Gauge32
_TmnxBsxGrpMdaTransPrefV4Entr_Object = MibTableColumn
tmnxBsxGrpMdaTransPrefV4Entr = _TmnxBsxGrpMdaTransPrefV4Entr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 16),
    _TmnxBsxGrpMdaTransPrefV4Entr_Type()
)
tmnxBsxGrpMdaTransPrefV4Entr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaTransPrefV4Entr.setStatus("current")
_TmnxBsxGrpMdaTransPrefV6Entr_Type = Gauge32
_TmnxBsxGrpMdaTransPrefV6Entr_Object = MibTableColumn
tmnxBsxGrpMdaTransPrefV6Entr = _TmnxBsxGrpMdaTransPrefV6Entr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 17),
    _TmnxBsxGrpMdaTransPrefV6Entr_Type()
)
tmnxBsxGrpMdaTransPrefV6Entr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaTransPrefV6Entr.setStatus("current")
_TmnxBsxGrpMdaTransPrefV6RemEntr_Type = Gauge32
_TmnxBsxGrpMdaTransPrefV6RemEntr_Object = MibTableColumn
tmnxBsxGrpMdaTransPrefV6RemEntr = _TmnxBsxGrpMdaTransPrefV6RemEntr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 4, 1, 18),
    _TmnxBsxGrpMdaTransPrefV6RemEntr_Type()
)
tmnxBsxGrpMdaTransPrefV6RemEntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpMdaTransPrefV6RemEntr.setStatus("current")
_TmnxBsxGrpStatusTable_Object = MibTable
tmnxBsxGrpStatusTable = _TmnxBsxGrpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusTable.setStatus("current")
_TmnxBsxGrpStatusEntry_Object = MibTableRow
tmnxBsxGrpStatusEntry = _TmnxBsxGrpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1)
)
tmnxBsxGrpStatusEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEntry.setStatus("current")
_TmnxBsxGrpStatusDiscontTime_Type = TimeStamp
_TmnxBsxGrpStatusDiscontTime_Object = MibTableColumn
tmnxBsxGrpStatusDiscontTime = _TmnxBsxGrpStatusDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 1),
    _TmnxBsxGrpStatusDiscontTime_Type()
)
tmnxBsxGrpStatusDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusDiscontTime.setStatus("current")
_TmnxBsxGrpStatusOctsIn_Type = Counter32
_TmnxBsxGrpStatusOctsIn_Object = MibTableColumn
tmnxBsxGrpStatusOctsIn = _TmnxBsxGrpStatusOctsIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 2),
    _TmnxBsxGrpStatusOctsIn_Type()
)
tmnxBsxGrpStatusOctsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsIn.setUnits("bytes")
_TmnxBsxGrpStatusPktsIn_Type = Counter32
_TmnxBsxGrpStatusPktsIn_Object = MibTableColumn
tmnxBsxGrpStatusPktsIn = _TmnxBsxGrpStatusPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 3),
    _TmnxBsxGrpStatusPktsIn_Type()
)
tmnxBsxGrpStatusPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsIn.setUnits("packets")
_TmnxBsxGrpStatusPktsInPChipErs_Type = Counter32
_TmnxBsxGrpStatusPktsInPChipErs_Object = MibTableColumn
tmnxBsxGrpStatusPktsInPChipErs = _TmnxBsxGrpStatusPktsInPChipErs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 4),
    _TmnxBsxGrpStatusPktsInPChipErs_Type()
)
tmnxBsxGrpStatusPktsInPChipErs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsInPChipErs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsInPChipErs.setUnits("packets")
_TmnxBsxGrpStatusOctsDiscCongIn_Type = Counter32
_TmnxBsxGrpStatusOctsDiscCongIn_Object = MibTableColumn
tmnxBsxGrpStatusOctsDiscCongIn = _TmnxBsxGrpStatusOctsDiscCongIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 5),
    _TmnxBsxGrpStatusOctsDiscCongIn_Type()
)
tmnxBsxGrpStatusOctsDiscCongIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsDiscCongIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsDiscCongIn.setUnits("bytes")
_TmnxBsxGrpStatusPktsDiscCongIn_Type = Counter32
_TmnxBsxGrpStatusPktsDiscCongIn_Object = MibTableColumn
tmnxBsxGrpStatusPktsDiscCongIn = _TmnxBsxGrpStatusPktsDiscCongIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 6),
    _TmnxBsxGrpStatusPktsDiscCongIn_Type()
)
tmnxBsxGrpStatusPktsDiscCongIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsDiscCongIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsDiscCongIn.setUnits("packets")
_TmnxBsxGrpStatusOctsToMda_Type = Counter32
_TmnxBsxGrpStatusOctsToMda_Object = MibTableColumn
tmnxBsxGrpStatusOctsToMda = _TmnxBsxGrpStatusOctsToMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 7),
    _TmnxBsxGrpStatusOctsToMda_Type()
)
tmnxBsxGrpStatusOctsToMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsToMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsToMda.setUnits("bytes")
_TmnxBsxGrpStatusPktsToMda_Type = Counter32
_TmnxBsxGrpStatusPktsToMda_Object = MibTableColumn
tmnxBsxGrpStatusPktsToMda = _TmnxBsxGrpStatusPktsToMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 8),
    _TmnxBsxGrpStatusPktsToMda_Type()
)
tmnxBsxGrpStatusPktsToMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsToMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsToMda.setUnits("packets")
_TmnxBsxGrpStatusOctsDisCongMda_Type = Counter32
_TmnxBsxGrpStatusOctsDisCongMda_Object = MibTableColumn
tmnxBsxGrpStatusOctsDisCongMda = _TmnxBsxGrpStatusOctsDisCongMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 9),
    _TmnxBsxGrpStatusOctsDisCongMda_Type()
)
tmnxBsxGrpStatusOctsDisCongMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsDisCongMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsDisCongMda.setUnits("bytes")
_TmnxBsxGrpStatusPktsDisCongMda_Type = Counter32
_TmnxBsxGrpStatusPktsDisCongMda_Object = MibTableColumn
tmnxBsxGrpStatusPktsDisCongMda = _TmnxBsxGrpStatusPktsDisCongMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 10),
    _TmnxBsxGrpStatusPktsDisCongMda_Type()
)
tmnxBsxGrpStatusPktsDisCongMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsDisCongMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsDisCongMda.setUnits("packets")
_TmnxBsxGrpStatusOctsDiscErrors_Type = Counter32
_TmnxBsxGrpStatusOctsDiscErrors_Object = MibTableColumn
tmnxBsxGrpStatusOctsDiscErrors = _TmnxBsxGrpStatusOctsDiscErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 11),
    _TmnxBsxGrpStatusOctsDiscErrors_Type()
)
tmnxBsxGrpStatusOctsDiscErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsDiscErrors.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsDiscErrors.setUnits("bytes")
_TmnxBsxGrpStatusPktsDiscErrors_Type = Counter32
_TmnxBsxGrpStatusPktsDiscErrors_Object = MibTableColumn
tmnxBsxGrpStatusPktsDiscErrors = _TmnxBsxGrpStatusPktsDiscErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 12),
    _TmnxBsxGrpStatusPktsDiscErrors_Type()
)
tmnxBsxGrpStatusPktsDiscErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsDiscErrors.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsDiscErrors.setUnits("packets")
_TmnxBsxGrpStatusOctsPolicyByps_Type = Counter32
_TmnxBsxGrpStatusOctsPolicyByps_Object = MibTableColumn
tmnxBsxGrpStatusOctsPolicyByps = _TmnxBsxGrpStatusOctsPolicyByps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 13),
    _TmnxBsxGrpStatusOctsPolicyByps_Type()
)
tmnxBsxGrpStatusOctsPolicyByps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsPolicyByps.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsPolicyByps.setUnits("bytes")
_TmnxBsxGrpStatusPktsPolicyByps_Type = Counter32
_TmnxBsxGrpStatusPktsPolicyByps_Object = MibTableColumn
tmnxBsxGrpStatusPktsPolicyByps = _TmnxBsxGrpStatusPktsPolicyByps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 14),
    _TmnxBsxGrpStatusPktsPolicyByps_Type()
)
tmnxBsxGrpStatusPktsPolicyByps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsPolicyByps.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsPolicyByps.setUnits("packets")
_TmnxBsxGrpStatusOctsInspected_Type = Counter32
_TmnxBsxGrpStatusOctsInspected_Object = MibTableColumn
tmnxBsxGrpStatusOctsInspected = _TmnxBsxGrpStatusOctsInspected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 15),
    _TmnxBsxGrpStatusOctsInspected_Type()
)
tmnxBsxGrpStatusOctsInspected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsInspected.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsInspected.setUnits("bytes")
_TmnxBsxGrpStatusPktsInspected_Type = Counter32
_TmnxBsxGrpStatusPktsInspected_Object = MibTableColumn
tmnxBsxGrpStatusPktsInspected = _TmnxBsxGrpStatusPktsInspected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 16),
    _TmnxBsxGrpStatusPktsInspected_Type()
)
tmnxBsxGrpStatusPktsInspected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsInspected.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsInspected.setUnits("packets")
_TmnxBsxGrpStatusOctsDiscPolicy_Type = Counter32
_TmnxBsxGrpStatusOctsDiscPolicy_Object = MibTableColumn
tmnxBsxGrpStatusOctsDiscPolicy = _TmnxBsxGrpStatusOctsDiscPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 17),
    _TmnxBsxGrpStatusOctsDiscPolicy_Type()
)
tmnxBsxGrpStatusOctsDiscPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsDiscPolicy.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsDiscPolicy.setUnits("bytes")
_TmnxBsxGrpStatusPktsDiscPolicy_Type = Counter32
_TmnxBsxGrpStatusPktsDiscPolicy_Object = MibTableColumn
tmnxBsxGrpStatusPktsDiscPolicy = _TmnxBsxGrpStatusPktsDiscPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 18),
    _TmnxBsxGrpStatusPktsDiscPolicy_Type()
)
tmnxBsxGrpStatusPktsDiscPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsDiscPolicy.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsDiscPolicy.setUnits("packets")
_TmnxBsxGrpStatusOctsInMda_Type = Counter32
_TmnxBsxGrpStatusOctsInMda_Object = MibTableColumn
tmnxBsxGrpStatusOctsInMda = _TmnxBsxGrpStatusOctsInMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 19),
    _TmnxBsxGrpStatusOctsInMda_Type()
)
tmnxBsxGrpStatusOctsInMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsInMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsInMda.setUnits("bytes")
_TmnxBsxGrpStatusPktsInMda_Type = Counter32
_TmnxBsxGrpStatusPktsInMda_Object = MibTableColumn
tmnxBsxGrpStatusPktsInMda = _TmnxBsxGrpStatusPktsInMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 20),
    _TmnxBsxGrpStatusPktsInMda_Type()
)
tmnxBsxGrpStatusPktsInMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsInMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsInMda.setUnits("packets")
_TmnxBsxGrpStatusOctsFromMda_Type = Counter32
_TmnxBsxGrpStatusOctsFromMda_Object = MibTableColumn
tmnxBsxGrpStatusOctsFromMda = _TmnxBsxGrpStatusOctsFromMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 21),
    _TmnxBsxGrpStatusOctsFromMda_Type()
)
tmnxBsxGrpStatusOctsFromMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsFromMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsFromMda.setUnits("bytes")
_TmnxBsxGrpStatusPktsFromMda_Type = Counter32
_TmnxBsxGrpStatusPktsFromMda_Object = MibTableColumn
tmnxBsxGrpStatusPktsFromMda = _TmnxBsxGrpStatusPktsFromMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 22),
    _TmnxBsxGrpStatusPktsFromMda_Type()
)
tmnxBsxGrpStatusPktsFromMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsFromMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsFromMda.setUnits("packets")
_TmnxBsxGrpStatusPktsOutPChipEr_Type = Counter32
_TmnxBsxGrpStatusPktsOutPChipEr_Object = MibTableColumn
tmnxBsxGrpStatusPktsOutPChipEr = _TmnxBsxGrpStatusPktsOutPChipEr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 23),
    _TmnxBsxGrpStatusPktsOutPChipEr_Type()
)
tmnxBsxGrpStatusPktsOutPChipEr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsOutPChipEr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsOutPChipEr.setUnits("packets")
_TmnxBsxGrpStatusOctsDisCongOut_Type = Counter32
_TmnxBsxGrpStatusOctsDisCongOut_Object = MibTableColumn
tmnxBsxGrpStatusOctsDisCongOut = _TmnxBsxGrpStatusOctsDisCongOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 24),
    _TmnxBsxGrpStatusOctsDisCongOut_Type()
)
tmnxBsxGrpStatusOctsDisCongOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsDisCongOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsDisCongOut.setUnits("bytes")
_TmnxBsxGrpStatusPktsDisCongOut_Type = Counter32
_TmnxBsxGrpStatusPktsDisCongOut_Object = MibTableColumn
tmnxBsxGrpStatusPktsDisCongOut = _TmnxBsxGrpStatusPktsDisCongOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 25),
    _TmnxBsxGrpStatusPktsDisCongOut_Type()
)
tmnxBsxGrpStatusPktsDisCongOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsDisCongOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsDisCongOut.setUnits("packets")
_TmnxBsxGrpStatusOctsOut_Type = Counter32
_TmnxBsxGrpStatusOctsOut_Object = MibTableColumn
tmnxBsxGrpStatusOctsOut = _TmnxBsxGrpStatusOctsOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 26),
    _TmnxBsxGrpStatusOctsOut_Type()
)
tmnxBsxGrpStatusOctsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusOctsOut.setUnits("bytes")
_TmnxBsxGrpStatusPktsOut_Type = Counter32
_TmnxBsxGrpStatusPktsOut_Object = MibTableColumn
tmnxBsxGrpStatusPktsOut = _TmnxBsxGrpStatusPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 27),
    _TmnxBsxGrpStatusPktsOut_Type()
)
tmnxBsxGrpStatusPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktsOut.setUnits("packets")
_TmnxBsxGrpStatusFlows_Type = Counter32
_TmnxBsxGrpStatusFlows_Object = MibTableColumn
tmnxBsxGrpStatusFlows = _TmnxBsxGrpStatusFlows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 28),
    _TmnxBsxGrpStatusFlows_Type()
)
tmnxBsxGrpStatusFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlows.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlows.setUnits("flows")
_TmnxBsxGrpStatusFlowsCurrent_Type = Gauge32
_TmnxBsxGrpStatusFlowsCurrent_Object = MibTableColumn
tmnxBsxGrpStatusFlowsCurrent = _TmnxBsxGrpStatusFlowsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 29),
    _TmnxBsxGrpStatusFlowsCurrent_Type()
)
tmnxBsxGrpStatusFlowsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowsCurrent.setUnits("flows")
_TmnxBsxGrpStatusFlowSetupRate_Type = Gauge32
_TmnxBsxGrpStatusFlowSetupRate_Object = MibTableColumn
tmnxBsxGrpStatusFlowSetupRate = _TmnxBsxGrpStatusFlowSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 30),
    _TmnxBsxGrpStatusFlowSetupRate_Type()
)
tmnxBsxGrpStatusFlowSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowSetupRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowSetupRate.setUnits("flows per second")
_TmnxBsxGrpStatusSubsDiverted_Type = Gauge32
_TmnxBsxGrpStatusSubsDiverted_Object = MibTableColumn
tmnxBsxGrpStatusSubsDiverted = _TmnxBsxGrpStatusSubsDiverted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 31),
    _TmnxBsxGrpStatusSubsDiverted_Type()
)
tmnxBsxGrpStatusSubsDiverted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsDiverted.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsDiverted.setUnits("subscribers")
_TmnxBsxGrpStatusSubsCurrent_Type = Gauge32
_TmnxBsxGrpStatusSubsCurrent_Object = MibTableColumn
tmnxBsxGrpStatusSubsCurrent = _TmnxBsxGrpStatusSubsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 32),
    _TmnxBsxGrpStatusSubsCurrent_Type()
)
tmnxBsxGrpStatusSubsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsCurrent.setUnits("subscribers")
_TmnxBsxGrpStatusTrafficRate_Type = Gauge32
_TmnxBsxGrpStatusTrafficRate_Object = MibTableColumn
tmnxBsxGrpStatusTrafficRate = _TmnxBsxGrpStatusTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 33),
    _TmnxBsxGrpStatusTrafficRate_Type()
)
tmnxBsxGrpStatusTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusTrafficRate.setUnits("kbps")
_TmnxBsxGrpStatusHCOctsIn_Type = Counter64
_TmnxBsxGrpStatusHCOctsIn_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsIn = _TmnxBsxGrpStatusHCOctsIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 34),
    _TmnxBsxGrpStatusHCOctsIn_Type()
)
tmnxBsxGrpStatusHCOctsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsIn.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsIn_Type = Counter64
_TmnxBsxGrpStatusHCPktsIn_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsIn = _TmnxBsxGrpStatusHCPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 35),
    _TmnxBsxGrpStatusHCPktsIn_Type()
)
tmnxBsxGrpStatusHCPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsIn.setUnits("packets")
_TmnxBsxGrpStatusHCPktsInPChipErs_Type = Counter64
_TmnxBsxGrpStatusHCPktsInPChipErs_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsInPChipErs = _TmnxBsxGrpStatusHCPktsInPChipErs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 36),
    _TmnxBsxGrpStatusHCPktsInPChipErs_Type()
)
tmnxBsxGrpStatusHCPktsInPChipErs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsInPChipErs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsInPChipErs.setUnits("packets")
_TmnxBsxGrpStatusHCOctsDiscCongIn_Type = Counter64
_TmnxBsxGrpStatusHCOctsDiscCongIn_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsDiscCongIn = _TmnxBsxGrpStatusHCOctsDiscCongIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 37),
    _TmnxBsxGrpStatusHCOctsDiscCongIn_Type()
)
tmnxBsxGrpStatusHCOctsDiscCongIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsDiscCongIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsDiscCongIn.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsDiscCongIn_Type = Counter64
_TmnxBsxGrpStatusHCPktsDiscCongIn_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsDiscCongIn = _TmnxBsxGrpStatusHCPktsDiscCongIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 38),
    _TmnxBsxGrpStatusHCPktsDiscCongIn_Type()
)
tmnxBsxGrpStatusHCPktsDiscCongIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsDiscCongIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsDiscCongIn.setUnits("packets")
_TmnxBsxGrpStatusHCOctsToMda_Type = Counter64
_TmnxBsxGrpStatusHCOctsToMda_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsToMda = _TmnxBsxGrpStatusHCOctsToMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 39),
    _TmnxBsxGrpStatusHCOctsToMda_Type()
)
tmnxBsxGrpStatusHCOctsToMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsToMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsToMda.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsToMda_Type = Counter64
_TmnxBsxGrpStatusHCPktsToMda_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsToMda = _TmnxBsxGrpStatusHCPktsToMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 40),
    _TmnxBsxGrpStatusHCPktsToMda_Type()
)
tmnxBsxGrpStatusHCPktsToMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsToMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsToMda.setUnits("packets")
_TmnxBsxGrpStatusHCOctsDisCongMda_Type = Counter64
_TmnxBsxGrpStatusHCOctsDisCongMda_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsDisCongMda = _TmnxBsxGrpStatusHCOctsDisCongMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 41),
    _TmnxBsxGrpStatusHCOctsDisCongMda_Type()
)
tmnxBsxGrpStatusHCOctsDisCongMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsDisCongMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsDisCongMda.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsDisCongMda_Type = Counter64
_TmnxBsxGrpStatusHCPktsDisCongMda_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsDisCongMda = _TmnxBsxGrpStatusHCPktsDisCongMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 42),
    _TmnxBsxGrpStatusHCPktsDisCongMda_Type()
)
tmnxBsxGrpStatusHCPktsDisCongMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsDisCongMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsDisCongMda.setUnits("packets")
_TmnxBsxGrpStatusHCOctsDiscErrors_Type = Counter64
_TmnxBsxGrpStatusHCOctsDiscErrors_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsDiscErrors = _TmnxBsxGrpStatusHCOctsDiscErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 43),
    _TmnxBsxGrpStatusHCOctsDiscErrors_Type()
)
tmnxBsxGrpStatusHCOctsDiscErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsDiscErrors.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsDiscErrors.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsDiscErrors_Type = Counter64
_TmnxBsxGrpStatusHCPktsDiscErrors_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsDiscErrors = _TmnxBsxGrpStatusHCPktsDiscErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 44),
    _TmnxBsxGrpStatusHCPktsDiscErrors_Type()
)
tmnxBsxGrpStatusHCPktsDiscErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsDiscErrors.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsDiscErrors.setUnits("packets")
_TmnxBsxGrpStatusHCOctsPolicyByps_Type = Counter64
_TmnxBsxGrpStatusHCOctsPolicyByps_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsPolicyByps = _TmnxBsxGrpStatusHCOctsPolicyByps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 45),
    _TmnxBsxGrpStatusHCOctsPolicyByps_Type()
)
tmnxBsxGrpStatusHCOctsPolicyByps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsPolicyByps.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsPolicyByps.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsPolicyByps_Type = Counter64
_TmnxBsxGrpStatusHCPktsPolicyByps_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsPolicyByps = _TmnxBsxGrpStatusHCPktsPolicyByps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 46),
    _TmnxBsxGrpStatusHCPktsPolicyByps_Type()
)
tmnxBsxGrpStatusHCPktsPolicyByps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsPolicyByps.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsPolicyByps.setUnits("packets")
_TmnxBsxGrpStatusHCOctsInspected_Type = Counter64
_TmnxBsxGrpStatusHCOctsInspected_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsInspected = _TmnxBsxGrpStatusHCOctsInspected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 47),
    _TmnxBsxGrpStatusHCOctsInspected_Type()
)
tmnxBsxGrpStatusHCOctsInspected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsInspected.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsInspected.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsInspected_Type = Counter64
_TmnxBsxGrpStatusHCPktsInspected_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsInspected = _TmnxBsxGrpStatusHCPktsInspected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 48),
    _TmnxBsxGrpStatusHCPktsInspected_Type()
)
tmnxBsxGrpStatusHCPktsInspected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsInspected.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsInspected.setUnits("packets")
_TmnxBsxGrpStatusHCOctsDiscPolicy_Type = Counter64
_TmnxBsxGrpStatusHCOctsDiscPolicy_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsDiscPolicy = _TmnxBsxGrpStatusHCOctsDiscPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 49),
    _TmnxBsxGrpStatusHCOctsDiscPolicy_Type()
)
tmnxBsxGrpStatusHCOctsDiscPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsDiscPolicy.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsDiscPolicy.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsDiscPolicy_Type = Counter64
_TmnxBsxGrpStatusHCPktsDiscPolicy_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsDiscPolicy = _TmnxBsxGrpStatusHCPktsDiscPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 50),
    _TmnxBsxGrpStatusHCPktsDiscPolicy_Type()
)
tmnxBsxGrpStatusHCPktsDiscPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsDiscPolicy.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsDiscPolicy.setUnits("packets")
_TmnxBsxGrpStatusHCOctsInMda_Type = Counter64
_TmnxBsxGrpStatusHCOctsInMda_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsInMda = _TmnxBsxGrpStatusHCOctsInMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 51),
    _TmnxBsxGrpStatusHCOctsInMda_Type()
)
tmnxBsxGrpStatusHCOctsInMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsInMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsInMda.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsInMda_Type = Counter64
_TmnxBsxGrpStatusHCPktsInMda_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsInMda = _TmnxBsxGrpStatusHCPktsInMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 52),
    _TmnxBsxGrpStatusHCPktsInMda_Type()
)
tmnxBsxGrpStatusHCPktsInMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsInMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsInMda.setUnits("packets")
_TmnxBsxGrpStatusHCOctsFromMda_Type = Counter64
_TmnxBsxGrpStatusHCOctsFromMda_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsFromMda = _TmnxBsxGrpStatusHCOctsFromMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 53),
    _TmnxBsxGrpStatusHCOctsFromMda_Type()
)
tmnxBsxGrpStatusHCOctsFromMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsFromMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsFromMda.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsFromMda_Type = Counter64
_TmnxBsxGrpStatusHCPktsFromMda_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsFromMda = _TmnxBsxGrpStatusHCPktsFromMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 54),
    _TmnxBsxGrpStatusHCPktsFromMda_Type()
)
tmnxBsxGrpStatusHCPktsFromMda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsFromMda.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsFromMda.setUnits("packets")
_TmnxBsxGrpStatusHCPktsOutPChipEr_Type = Counter64
_TmnxBsxGrpStatusHCPktsOutPChipEr_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsOutPChipEr = _TmnxBsxGrpStatusHCPktsOutPChipEr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 55),
    _TmnxBsxGrpStatusHCPktsOutPChipEr_Type()
)
tmnxBsxGrpStatusHCPktsOutPChipEr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsOutPChipEr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsOutPChipEr.setUnits("packets")
_TmnxBsxGrpStatusHCOctsDisCongOut_Type = Counter64
_TmnxBsxGrpStatusHCOctsDisCongOut_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsDisCongOut = _TmnxBsxGrpStatusHCOctsDisCongOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 56),
    _TmnxBsxGrpStatusHCOctsDisCongOut_Type()
)
tmnxBsxGrpStatusHCOctsDisCongOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsDisCongOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsDisCongOut.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsDisCongOut_Type = Counter64
_TmnxBsxGrpStatusHCPktsDisCongOut_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsDisCongOut = _TmnxBsxGrpStatusHCPktsDisCongOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 57),
    _TmnxBsxGrpStatusHCPktsDisCongOut_Type()
)
tmnxBsxGrpStatusHCPktsDisCongOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsDisCongOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsDisCongOut.setUnits("packets")
_TmnxBsxGrpStatusHCOctsOut_Type = Counter64
_TmnxBsxGrpStatusHCOctsOut_Object = MibTableColumn
tmnxBsxGrpStatusHCOctsOut = _TmnxBsxGrpStatusHCOctsOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 58),
    _TmnxBsxGrpStatusHCOctsOut_Type()
)
tmnxBsxGrpStatusHCOctsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCOctsOut.setUnits("bytes")
_TmnxBsxGrpStatusHCPktsOut_Type = Counter64
_TmnxBsxGrpStatusHCPktsOut_Object = MibTableColumn
tmnxBsxGrpStatusHCPktsOut = _TmnxBsxGrpStatusHCPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 59),
    _TmnxBsxGrpStatusHCPktsOut_Type()
)
tmnxBsxGrpStatusHCPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktsOut.setUnits("packets")
_TmnxBsxGrpStatusHCFlows_Type = Counter64
_TmnxBsxGrpStatusHCFlows_Object = MibTableColumn
tmnxBsxGrpStatusHCFlows = _TmnxBsxGrpStatusHCFlows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 60),
    _TmnxBsxGrpStatusHCFlows_Type()
)
tmnxBsxGrpStatusHCFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCFlows.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCFlows.setUnits("flows")
_TmnxBsxGrpStatusFlowsAverage_Type = Gauge32
_TmnxBsxGrpStatusFlowsAverage_Object = MibTableColumn
tmnxBsxGrpStatusFlowsAverage = _TmnxBsxGrpStatusFlowsAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 61),
    _TmnxBsxGrpStatusFlowsAverage_Type()
)
tmnxBsxGrpStatusFlowsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowsAverage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowsAverage.setUnits("flows")
_TmnxBsxGrpStatusFlowsPeak_Type = Gauge32
_TmnxBsxGrpStatusFlowsPeak_Object = MibTableColumn
tmnxBsxGrpStatusFlowsPeak = _TmnxBsxGrpStatusFlowsPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 62),
    _TmnxBsxGrpStatusFlowsPeak_Type()
)
tmnxBsxGrpStatusFlowsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowsPeak.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowsPeak.setUnits("flows")
_TmnxBsxGrpStatusFlowSetupRateAvg_Type = Gauge32
_TmnxBsxGrpStatusFlowSetupRateAvg_Object = MibTableColumn
tmnxBsxGrpStatusFlowSetupRateAvg = _TmnxBsxGrpStatusFlowSetupRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 63),
    _TmnxBsxGrpStatusFlowSetupRateAvg_Type()
)
tmnxBsxGrpStatusFlowSetupRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowSetupRateAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowSetupRateAvg.setUnits("flows per second")
_TmnxBsxGrpStatusFlowSetupRatePk_Type = Gauge32
_TmnxBsxGrpStatusFlowSetupRatePk_Object = MibTableColumn
tmnxBsxGrpStatusFlowSetupRatePk = _TmnxBsxGrpStatusFlowSetupRatePk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 64),
    _TmnxBsxGrpStatusFlowSetupRatePk_Type()
)
tmnxBsxGrpStatusFlowSetupRatePk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowSetupRatePk.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowSetupRatePk.setUnits("flows per second")
_TmnxBsxGrpStatusSubsDivertedAvg_Type = Gauge32
_TmnxBsxGrpStatusSubsDivertedAvg_Object = MibTableColumn
tmnxBsxGrpStatusSubsDivertedAvg = _TmnxBsxGrpStatusSubsDivertedAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 65),
    _TmnxBsxGrpStatusSubsDivertedAvg_Type()
)
tmnxBsxGrpStatusSubsDivertedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsDivertedAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsDivertedAvg.setUnits("subscribers")
_TmnxBsxGrpStatusSubsDivertedPk_Type = Gauge32
_TmnxBsxGrpStatusSubsDivertedPk_Object = MibTableColumn
tmnxBsxGrpStatusSubsDivertedPk = _TmnxBsxGrpStatusSubsDivertedPk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 66),
    _TmnxBsxGrpStatusSubsDivertedPk_Type()
)
tmnxBsxGrpStatusSubsDivertedPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsDivertedPk.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsDivertedPk.setUnits("subscribers")
_TmnxBsxGrpStatusSubsAverage_Type = Gauge32
_TmnxBsxGrpStatusSubsAverage_Object = MibTableColumn
tmnxBsxGrpStatusSubsAverage = _TmnxBsxGrpStatusSubsAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 67),
    _TmnxBsxGrpStatusSubsAverage_Type()
)
tmnxBsxGrpStatusSubsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsAverage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsAverage.setUnits("subscribers")
_TmnxBsxGrpStatusSubsPeak_Type = Gauge32
_TmnxBsxGrpStatusSubsPeak_Object = MibTableColumn
tmnxBsxGrpStatusSubsPeak = _TmnxBsxGrpStatusSubsPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 68),
    _TmnxBsxGrpStatusSubsPeak_Type()
)
tmnxBsxGrpStatusSubsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsPeak.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusSubsPeak.setUnits("subscribers")
_TmnxBsxGrpStatusTrafficRateAvg_Type = Gauge32
_TmnxBsxGrpStatusTrafficRateAvg_Object = MibTableColumn
tmnxBsxGrpStatusTrafficRateAvg = _TmnxBsxGrpStatusTrafficRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 69),
    _TmnxBsxGrpStatusTrafficRateAvg_Type()
)
tmnxBsxGrpStatusTrafficRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusTrafficRateAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusTrafficRateAvg.setUnits("kbps")
_TmnxBsxGrpStatusTrafficRatePeak_Type = Gauge32
_TmnxBsxGrpStatusTrafficRatePeak_Object = MibTableColumn
tmnxBsxGrpStatusTrafficRatePeak = _TmnxBsxGrpStatusTrafficRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 70),
    _TmnxBsxGrpStatusTrafficRatePeak_Type()
)
tmnxBsxGrpStatusTrafficRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusTrafficRatePeak.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusTrafficRatePeak.setUnits("kbps")
_TmnxBsxGrpStatusPacketRate_Type = Gauge32
_TmnxBsxGrpStatusPacketRate_Object = MibTableColumn
tmnxBsxGrpStatusPacketRate = _TmnxBsxGrpStatusPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 71),
    _TmnxBsxGrpStatusPacketRate_Type()
)
tmnxBsxGrpStatusPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPacketRate.setUnits("packets per second")
_TmnxBsxGrpStatusPacketRateAvg_Type = Gauge32
_TmnxBsxGrpStatusPacketRateAvg_Object = MibTableColumn
tmnxBsxGrpStatusPacketRateAvg = _TmnxBsxGrpStatusPacketRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 72),
    _TmnxBsxGrpStatusPacketRateAvg_Type()
)
tmnxBsxGrpStatusPacketRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPacketRateAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPacketRateAvg.setUnits("packets per second")
_TmnxBsxGrpStatusPacketRatePeak_Type = Gauge32
_TmnxBsxGrpStatusPacketRatePeak_Object = MibTableColumn
tmnxBsxGrpStatusPacketRatePeak = _TmnxBsxGrpStatusPacketRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 73),
    _TmnxBsxGrpStatusPacketRatePeak_Type()
)
tmnxBsxGrpStatusPacketRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPacketRatePeak.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPacketRatePeak.setUnits("packets per second")
_TmnxBsxGrpStatusFlowResInUse_Type = Gauge32
_TmnxBsxGrpStatusFlowResInUse_Object = MibTableColumn
tmnxBsxGrpStatusFlowResInUse = _TmnxBsxGrpStatusFlowResInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 74),
    _TmnxBsxGrpStatusFlowResInUse_Type()
)
tmnxBsxGrpStatusFlowResInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowResInUse.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusFlowResInUse.setUnits("flow resources")
_TmnxBsxGrpStatusHCPktSzIncPk_Type = Counter64
_TmnxBsxGrpStatusHCPktSzIncPk_Object = MibTableColumn
tmnxBsxGrpStatusHCPktSzIncPk = _TmnxBsxGrpStatusHCPktSzIncPk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 75),
    _TmnxBsxGrpStatusHCPktSzIncPk_Type()
)
tmnxBsxGrpStatusHCPktSzIncPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktSzIncPk.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktSzIncPk.setUnits("packets")
_TmnxBsxGrpStatusPktSzIncPkLo_Type = Counter32
_TmnxBsxGrpStatusPktSzIncPkLo_Object = MibTableColumn
tmnxBsxGrpStatusPktSzIncPkLo = _TmnxBsxGrpStatusPktSzIncPkLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 76),
    _TmnxBsxGrpStatusPktSzIncPkLo_Type()
)
tmnxBsxGrpStatusPktSzIncPkLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzIncPkLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzIncPkLo.setUnits("packets")
_TmnxBsxGrpStatusPktSzIncPkHi_Type = Counter32
_TmnxBsxGrpStatusPktSzIncPkHi_Object = MibTableColumn
tmnxBsxGrpStatusPktSzIncPkHi = _TmnxBsxGrpStatusPktSzIncPkHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 77),
    _TmnxBsxGrpStatusPktSzIncPkHi_Type()
)
tmnxBsxGrpStatusPktSzIncPkHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzIncPkHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzIncPkHi.setUnits("packets")
_TmnxBsxGrpStatusHCPktSzDecPk_Type = Counter64
_TmnxBsxGrpStatusHCPktSzDecPk_Object = MibTableColumn
tmnxBsxGrpStatusHCPktSzDecPk = _TmnxBsxGrpStatusHCPktSzDecPk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 78),
    _TmnxBsxGrpStatusHCPktSzDecPk_Type()
)
tmnxBsxGrpStatusHCPktSzDecPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktSzDecPk.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktSzDecPk.setUnits("packets")
_TmnxBsxGrpStatusPktSzDecPkLo_Type = Counter32
_TmnxBsxGrpStatusPktSzDecPkLo_Object = MibTableColumn
tmnxBsxGrpStatusPktSzDecPkLo = _TmnxBsxGrpStatusPktSzDecPkLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 79),
    _TmnxBsxGrpStatusPktSzDecPkLo_Type()
)
tmnxBsxGrpStatusPktSzDecPkLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzDecPkLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzDecPkLo.setUnits("packets")
_TmnxBsxGrpStatusPktSzDecPkHi_Type = Counter32
_TmnxBsxGrpStatusPktSzDecPkHi_Object = MibTableColumn
tmnxBsxGrpStatusPktSzDecPkHi = _TmnxBsxGrpStatusPktSzDecPkHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 80),
    _TmnxBsxGrpStatusPktSzDecPkHi_Type()
)
tmnxBsxGrpStatusPktSzDecPkHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzDecPkHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzDecPkHi.setUnits("packets")
_TmnxBsxGrpStatusHCPktSzIncOc_Type = Counter64
_TmnxBsxGrpStatusHCPktSzIncOc_Object = MibTableColumn
tmnxBsxGrpStatusHCPktSzIncOc = _TmnxBsxGrpStatusHCPktSzIncOc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 81),
    _TmnxBsxGrpStatusHCPktSzIncOc_Type()
)
tmnxBsxGrpStatusHCPktSzIncOc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktSzIncOc.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktSzIncOc.setUnits("octets")
_TmnxBsxGrpStatusPktSzIncOcLo_Type = Counter32
_TmnxBsxGrpStatusPktSzIncOcLo_Object = MibTableColumn
tmnxBsxGrpStatusPktSzIncOcLo = _TmnxBsxGrpStatusPktSzIncOcLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 82),
    _TmnxBsxGrpStatusPktSzIncOcLo_Type()
)
tmnxBsxGrpStatusPktSzIncOcLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzIncOcLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzIncOcLo.setUnits("octets")
_TmnxBsxGrpStatusPktSzIncOcHi_Type = Counter32
_TmnxBsxGrpStatusPktSzIncOcHi_Object = MibTableColumn
tmnxBsxGrpStatusPktSzIncOcHi = _TmnxBsxGrpStatusPktSzIncOcHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 83),
    _TmnxBsxGrpStatusPktSzIncOcHi_Type()
)
tmnxBsxGrpStatusPktSzIncOcHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzIncOcHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzIncOcHi.setUnits("octets")
_TmnxBsxGrpStatusHCPktSzDecOc_Type = Counter64
_TmnxBsxGrpStatusHCPktSzDecOc_Object = MibTableColumn
tmnxBsxGrpStatusHCPktSzDecOc = _TmnxBsxGrpStatusHCPktSzDecOc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 84),
    _TmnxBsxGrpStatusHCPktSzDecOc_Type()
)
tmnxBsxGrpStatusHCPktSzDecOc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktSzDecOc.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusHCPktSzDecOc.setUnits("octets")
_TmnxBsxGrpStatusPktSzDecOcLo_Type = Counter32
_TmnxBsxGrpStatusPktSzDecOcLo_Object = MibTableColumn
tmnxBsxGrpStatusPktSzDecOcLo = _TmnxBsxGrpStatusPktSzDecOcLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 85),
    _TmnxBsxGrpStatusPktSzDecOcLo_Type()
)
tmnxBsxGrpStatusPktSzDecOcLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzDecOcLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzDecOcLo.setUnits("octets")
_TmnxBsxGrpStatusPktSzDecOcHi_Type = Counter32
_TmnxBsxGrpStatusPktSzDecOcHi_Object = MibTableColumn
tmnxBsxGrpStatusPktSzDecOcHi = _TmnxBsxGrpStatusPktSzDecOcHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 5, 1, 86),
    _TmnxBsxGrpStatusPktSzDecOcHi_Type()
)
tmnxBsxGrpStatusPktSzDecOcHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzDecOcHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusPktSzDecOcHi.setUnits("octets")
_TmnxBsxGrpStatusIngQTable_Object = MibTable
tmnxBsxGrpStatusIngQTable = _TmnxBsxGrpStatusIngQTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQTable.setStatus("current")
_TmnxBsxGrpStatusIngQEntry_Object = MibTableRow
tmnxBsxGrpStatusIngQEntry = _TmnxBsxGrpStatusIngQEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1)
)
tmnxBsxGrpStatusIngQEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusInQDirection"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusInQIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQEntry.setStatus("current")
_TmnxBsxGrpStatusInQDirection_Type = TmnxBsxDirection
_TmnxBsxGrpStatusInQDirection_Object = MibTableColumn
tmnxBsxGrpStatusInQDirection = _TmnxBsxGrpStatusInQDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 1),
    _TmnxBsxGrpStatusInQDirection_Type()
)
tmnxBsxGrpStatusInQDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusInQDirection.setStatus("current")
_TmnxBsxGrpStatusInQIndex_Type = TQueueId
_TmnxBsxGrpStatusInQIndex_Object = MibTableColumn
tmnxBsxGrpStatusInQIndex = _TmnxBsxGrpStatusInQIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 2),
    _TmnxBsxGrpStatusInQIndex_Type()
)
tmnxBsxGrpStatusInQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusInQIndex.setStatus("current")
_TmnxBsxGrpStatusIngQDiscontTime_Type = TimeStamp
_TmnxBsxGrpStatusIngQDiscontTime_Object = MibTableColumn
tmnxBsxGrpStatusIngQDiscontTime = _TmnxBsxGrpStatusIngQDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 3),
    _TmnxBsxGrpStatusIngQDiscontTime_Type()
)
tmnxBsxGrpStatusIngQDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQDiscontTime.setStatus("current")
_TmnxBsxGrpStatusIngQFwdInPPkts_Type = Counter32
_TmnxBsxGrpStatusIngQFwdInPPkts_Object = MibTableColumn
tmnxBsxGrpStatusIngQFwdInPPkts = _TmnxBsxGrpStatusIngQFwdInPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 4),
    _TmnxBsxGrpStatusIngQFwdInPPkts_Type()
)
tmnxBsxGrpStatusIngQFwdInPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQFwdInPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQFwdInPPkts.setUnits("packets")
_TmnxBsxGrpStatusIngQFwdOutPPkts_Type = Counter32
_TmnxBsxGrpStatusIngQFwdOutPPkts_Object = MibTableColumn
tmnxBsxGrpStatusIngQFwdOutPPkts = _TmnxBsxGrpStatusIngQFwdOutPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 5),
    _TmnxBsxGrpStatusIngQFwdOutPPkts_Type()
)
tmnxBsxGrpStatusIngQFwdOutPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQFwdOutPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQFwdOutPPkts.setUnits("packets")
_TmnxBsxGrpStatusIngQFwdInPOcts_Type = Counter32
_TmnxBsxGrpStatusIngQFwdInPOcts_Object = MibTableColumn
tmnxBsxGrpStatusIngQFwdInPOcts = _TmnxBsxGrpStatusIngQFwdInPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 6),
    _TmnxBsxGrpStatusIngQFwdInPOcts_Type()
)
tmnxBsxGrpStatusIngQFwdInPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQFwdInPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQFwdInPOcts.setUnits("bytes")
_TmnxBsxGrpStatusIngQFwdOutPOcts_Type = Counter32
_TmnxBsxGrpStatusIngQFwdOutPOcts_Object = MibTableColumn
tmnxBsxGrpStatusIngQFwdOutPOcts = _TmnxBsxGrpStatusIngQFwdOutPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 7),
    _TmnxBsxGrpStatusIngQFwdOutPOcts_Type()
)
tmnxBsxGrpStatusIngQFwdOutPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQFwdOutPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQFwdOutPOcts.setUnits("bytes")
_TmnxBsxGrpStatusIngQDroInPPkts_Type = Counter32
_TmnxBsxGrpStatusIngQDroInPPkts_Object = MibTableColumn
tmnxBsxGrpStatusIngQDroInPPkts = _TmnxBsxGrpStatusIngQDroInPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 8),
    _TmnxBsxGrpStatusIngQDroInPPkts_Type()
)
tmnxBsxGrpStatusIngQDroInPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQDroInPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQDroInPPkts.setUnits("packets")
_TmnxBsxGrpStatusIngQDroOutPPkts_Type = Counter32
_TmnxBsxGrpStatusIngQDroOutPPkts_Object = MibTableColumn
tmnxBsxGrpStatusIngQDroOutPPkts = _TmnxBsxGrpStatusIngQDroOutPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 9),
    _TmnxBsxGrpStatusIngQDroOutPPkts_Type()
)
tmnxBsxGrpStatusIngQDroOutPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQDroOutPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQDroOutPPkts.setUnits("packets")
_TmnxBsxGrpStatusIngQDroInPOcts_Type = Counter32
_TmnxBsxGrpStatusIngQDroInPOcts_Object = MibTableColumn
tmnxBsxGrpStatusIngQDroInPOcts = _TmnxBsxGrpStatusIngQDroInPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 10),
    _TmnxBsxGrpStatusIngQDroInPOcts_Type()
)
tmnxBsxGrpStatusIngQDroInPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQDroInPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQDroInPOcts.setUnits("bytes")
_TmnxBsxGrpStatusIngQDroOutPOcts_Type = Counter32
_TmnxBsxGrpStatusIngQDroOutPOcts_Object = MibTableColumn
tmnxBsxGrpStatusIngQDroOutPOcts = _TmnxBsxGrpStatusIngQDroOutPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 11),
    _TmnxBsxGrpStatusIngQDroOutPOcts_Type()
)
tmnxBsxGrpStatusIngQDroOutPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQDroOutPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQDroOutPOcts.setUnits("bytes")
_TmnxBsxGrpStatusIngQHCFwdInPPkts_Type = Counter64
_TmnxBsxGrpStatusIngQHCFwdInPPkts_Object = MibTableColumn
tmnxBsxGrpStatusIngQHCFwdInPPkts = _TmnxBsxGrpStatusIngQHCFwdInPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 12),
    _TmnxBsxGrpStatusIngQHCFwdInPPkts_Type()
)
tmnxBsxGrpStatusIngQHCFwdInPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCFwdInPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCFwdInPPkts.setUnits("packets")
_TmnxBsxGrpStatusIngQHCFwdOutPPkts_Type = Counter64
_TmnxBsxGrpStatusIngQHCFwdOutPPkts_Object = MibTableColumn
tmnxBsxGrpStatusIngQHCFwdOutPPkts = _TmnxBsxGrpStatusIngQHCFwdOutPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 13),
    _TmnxBsxGrpStatusIngQHCFwdOutPPkts_Type()
)
tmnxBsxGrpStatusIngQHCFwdOutPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCFwdOutPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCFwdOutPPkts.setUnits("packets")
_TmnxBsxGrpStatusIngQHCFwdInPOcts_Type = Counter64
_TmnxBsxGrpStatusIngQHCFwdInPOcts_Object = MibTableColumn
tmnxBsxGrpStatusIngQHCFwdInPOcts = _TmnxBsxGrpStatusIngQHCFwdInPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 14),
    _TmnxBsxGrpStatusIngQHCFwdInPOcts_Type()
)
tmnxBsxGrpStatusIngQHCFwdInPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCFwdInPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCFwdInPOcts.setUnits("bytes")
_TmnxBsxGrpStatusIngQHCFwdOutPOcts_Type = Counter64
_TmnxBsxGrpStatusIngQHCFwdOutPOcts_Object = MibTableColumn
tmnxBsxGrpStatusIngQHCFwdOutPOcts = _TmnxBsxGrpStatusIngQHCFwdOutPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 15),
    _TmnxBsxGrpStatusIngQHCFwdOutPOcts_Type()
)
tmnxBsxGrpStatusIngQHCFwdOutPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCFwdOutPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCFwdOutPOcts.setUnits("bytes")
_TmnxBsxGrpStatusIngQHCDroInPPkts_Type = Counter64
_TmnxBsxGrpStatusIngQHCDroInPPkts_Object = MibTableColumn
tmnxBsxGrpStatusIngQHCDroInPPkts = _TmnxBsxGrpStatusIngQHCDroInPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 16),
    _TmnxBsxGrpStatusIngQHCDroInPPkts_Type()
)
tmnxBsxGrpStatusIngQHCDroInPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCDroInPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCDroInPPkts.setUnits("packets")
_TmnxBsxGrpStatusIngQHCDroOutPPkts_Type = Counter64
_TmnxBsxGrpStatusIngQHCDroOutPPkts_Object = MibTableColumn
tmnxBsxGrpStatusIngQHCDroOutPPkts = _TmnxBsxGrpStatusIngQHCDroOutPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 17),
    _TmnxBsxGrpStatusIngQHCDroOutPPkts_Type()
)
tmnxBsxGrpStatusIngQHCDroOutPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCDroOutPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCDroOutPPkts.setUnits("packets")
_TmnxBsxGrpStatusIngQHCDroInPOcts_Type = Counter64
_TmnxBsxGrpStatusIngQHCDroInPOcts_Object = MibTableColumn
tmnxBsxGrpStatusIngQHCDroInPOcts = _TmnxBsxGrpStatusIngQHCDroInPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 18),
    _TmnxBsxGrpStatusIngQHCDroInPOcts_Type()
)
tmnxBsxGrpStatusIngQHCDroInPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCDroInPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCDroInPOcts.setUnits("bytes")
_TmnxBsxGrpStatusIngQHCDroOutPOcts_Type = Counter64
_TmnxBsxGrpStatusIngQHCDroOutPOcts_Object = MibTableColumn
tmnxBsxGrpStatusIngQHCDroOutPOcts = _TmnxBsxGrpStatusIngQHCDroOutPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 6, 1, 19),
    _TmnxBsxGrpStatusIngQHCDroOutPOcts_Type()
)
tmnxBsxGrpStatusIngQHCDroOutPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCDroOutPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusIngQHCDroOutPOcts.setUnits("bytes")
_TmnxBsxGrpStatusEgrQTable_Object = MibTable
tmnxBsxGrpStatusEgrQTable = _TmnxBsxGrpStatusEgrQTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQTable.setStatus("current")
_TmnxBsxGrpStatusEgrQEntry_Object = MibTableRow
tmnxBsxGrpStatusEgrQEntry = _TmnxBsxGrpStatusEgrQEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1)
)
tmnxBsxGrpStatusEgrQEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDirection"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQEntry.setStatus("current")
_TmnxBsxGrpStatusEgrQDirection_Type = TmnxBsxDirection
_TmnxBsxGrpStatusEgrQDirection_Object = MibTableColumn
tmnxBsxGrpStatusEgrQDirection = _TmnxBsxGrpStatusEgrQDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 1),
    _TmnxBsxGrpStatusEgrQDirection_Type()
)
tmnxBsxGrpStatusEgrQDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQDirection.setStatus("current")
_TmnxBsxGrpStatusEgrQIndex_Type = TQueueId
_TmnxBsxGrpStatusEgrQIndex_Object = MibTableColumn
tmnxBsxGrpStatusEgrQIndex = _TmnxBsxGrpStatusEgrQIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 2),
    _TmnxBsxGrpStatusEgrQIndex_Type()
)
tmnxBsxGrpStatusEgrQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQIndex.setStatus("current")
_TmnxBsxGrpStatusEgrQDiscontTime_Type = TimeStamp
_TmnxBsxGrpStatusEgrQDiscontTime_Object = MibTableColumn
tmnxBsxGrpStatusEgrQDiscontTime = _TmnxBsxGrpStatusEgrQDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 3),
    _TmnxBsxGrpStatusEgrQDiscontTime_Type()
)
tmnxBsxGrpStatusEgrQDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQDiscontTime.setStatus("current")
_TmnxBsxGrpStatusEgrQFwdInPPkts_Type = Counter32
_TmnxBsxGrpStatusEgrQFwdInPPkts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQFwdInPPkts = _TmnxBsxGrpStatusEgrQFwdInPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 4),
    _TmnxBsxGrpStatusEgrQFwdInPPkts_Type()
)
tmnxBsxGrpStatusEgrQFwdInPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQFwdInPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQFwdInPPkts.setUnits("packets")
_TmnxBsxGrpStatusEgrQFwdOutPPkts_Type = Counter32
_TmnxBsxGrpStatusEgrQFwdOutPPkts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQFwdOutPPkts = _TmnxBsxGrpStatusEgrQFwdOutPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 5),
    _TmnxBsxGrpStatusEgrQFwdOutPPkts_Type()
)
tmnxBsxGrpStatusEgrQFwdOutPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQFwdOutPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQFwdOutPPkts.setUnits("packets")
_TmnxBsxGrpStatusEgrQFwdInPOcts_Type = Counter32
_TmnxBsxGrpStatusEgrQFwdInPOcts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQFwdInPOcts = _TmnxBsxGrpStatusEgrQFwdInPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 6),
    _TmnxBsxGrpStatusEgrQFwdInPOcts_Type()
)
tmnxBsxGrpStatusEgrQFwdInPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQFwdInPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQFwdInPOcts.setUnits("bytes")
_TmnxBsxGrpStatusEgrQFwdOutPOcts_Type = Counter32
_TmnxBsxGrpStatusEgrQFwdOutPOcts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQFwdOutPOcts = _TmnxBsxGrpStatusEgrQFwdOutPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 7),
    _TmnxBsxGrpStatusEgrQFwdOutPOcts_Type()
)
tmnxBsxGrpStatusEgrQFwdOutPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQFwdOutPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQFwdOutPOcts.setUnits("bytes")
_TmnxBsxGrpStatusEgrQDroInPPkts_Type = Counter32
_TmnxBsxGrpStatusEgrQDroInPPkts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQDroInPPkts = _TmnxBsxGrpStatusEgrQDroInPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 8),
    _TmnxBsxGrpStatusEgrQDroInPPkts_Type()
)
tmnxBsxGrpStatusEgrQDroInPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQDroInPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQDroInPPkts.setUnits("packets")
_TmnxBsxGrpStatusEgrQDroOutPPkts_Type = Counter32
_TmnxBsxGrpStatusEgrQDroOutPPkts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQDroOutPPkts = _TmnxBsxGrpStatusEgrQDroOutPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 9),
    _TmnxBsxGrpStatusEgrQDroOutPPkts_Type()
)
tmnxBsxGrpStatusEgrQDroOutPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQDroOutPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQDroOutPPkts.setUnits("packets")
_TmnxBsxGrpStatusEgrQDroInPOcts_Type = Counter32
_TmnxBsxGrpStatusEgrQDroInPOcts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQDroInPOcts = _TmnxBsxGrpStatusEgrQDroInPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 10),
    _TmnxBsxGrpStatusEgrQDroInPOcts_Type()
)
tmnxBsxGrpStatusEgrQDroInPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQDroInPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQDroInPOcts.setUnits("bytes")
_TmnxBsxGrpStatusEgrQDroOutPOcts_Type = Counter32
_TmnxBsxGrpStatusEgrQDroOutPOcts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQDroOutPOcts = _TmnxBsxGrpStatusEgrQDroOutPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 11),
    _TmnxBsxGrpStatusEgrQDroOutPOcts_Type()
)
tmnxBsxGrpStatusEgrQDroOutPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQDroOutPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQDroOutPOcts.setUnits("bytes")
_TmnxBsxGrpStatusEgrQHCFwdInPPkts_Type = Counter64
_TmnxBsxGrpStatusEgrQHCFwdInPPkts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQHCFwdInPPkts = _TmnxBsxGrpStatusEgrQHCFwdInPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 12),
    _TmnxBsxGrpStatusEgrQHCFwdInPPkts_Type()
)
tmnxBsxGrpStatusEgrQHCFwdInPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCFwdInPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCFwdInPPkts.setUnits("packets")
_TmnxBsxGrpStatusEgrQHCFwdOutPPkts_Type = Counter64
_TmnxBsxGrpStatusEgrQHCFwdOutPPkts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQHCFwdOutPPkts = _TmnxBsxGrpStatusEgrQHCFwdOutPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 13),
    _TmnxBsxGrpStatusEgrQHCFwdOutPPkts_Type()
)
tmnxBsxGrpStatusEgrQHCFwdOutPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCFwdOutPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCFwdOutPPkts.setUnits("packets")
_TmnxBsxGrpStatusEgrQHCFwdInPOcts_Type = Counter64
_TmnxBsxGrpStatusEgrQHCFwdInPOcts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQHCFwdInPOcts = _TmnxBsxGrpStatusEgrQHCFwdInPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 14),
    _TmnxBsxGrpStatusEgrQHCFwdInPOcts_Type()
)
tmnxBsxGrpStatusEgrQHCFwdInPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCFwdInPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCFwdInPOcts.setUnits("bytes")
_TmnxBsxGrpStatusEgrQHCFwdOutPOcts_Type = Counter64
_TmnxBsxGrpStatusEgrQHCFwdOutPOcts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQHCFwdOutPOcts = _TmnxBsxGrpStatusEgrQHCFwdOutPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 15),
    _TmnxBsxGrpStatusEgrQHCFwdOutPOcts_Type()
)
tmnxBsxGrpStatusEgrQHCFwdOutPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCFwdOutPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCFwdOutPOcts.setUnits("bytes")
_TmnxBsxGrpStatusEgrQHCDroInPPkts_Type = Counter64
_TmnxBsxGrpStatusEgrQHCDroInPPkts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQHCDroInPPkts = _TmnxBsxGrpStatusEgrQHCDroInPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 16),
    _TmnxBsxGrpStatusEgrQHCDroInPPkts_Type()
)
tmnxBsxGrpStatusEgrQHCDroInPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCDroInPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCDroInPPkts.setUnits("packets")
_TmnxBsxGrpStatusEgrQHCDroOutPPkts_Type = Counter64
_TmnxBsxGrpStatusEgrQHCDroOutPPkts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQHCDroOutPPkts = _TmnxBsxGrpStatusEgrQHCDroOutPPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 17),
    _TmnxBsxGrpStatusEgrQHCDroOutPPkts_Type()
)
tmnxBsxGrpStatusEgrQHCDroOutPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCDroOutPPkts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCDroOutPPkts.setUnits("packets")
_TmnxBsxGrpStatusEgrQHCDroInPOcts_Type = Counter64
_TmnxBsxGrpStatusEgrQHCDroInPOcts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQHCDroInPOcts = _TmnxBsxGrpStatusEgrQHCDroInPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 18),
    _TmnxBsxGrpStatusEgrQHCDroInPOcts_Type()
)
tmnxBsxGrpStatusEgrQHCDroInPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCDroInPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCDroInPOcts.setUnits("bytes")
_TmnxBsxGrpStatusEgrQHCDroOutPOcts_Type = Counter64
_TmnxBsxGrpStatusEgrQHCDroOutPOcts_Object = MibTableColumn
tmnxBsxGrpStatusEgrQHCDroOutPOcts = _TmnxBsxGrpStatusEgrQHCDroOutPOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 7, 1, 19),
    _TmnxBsxGrpStatusEgrQHCDroOutPOcts_Type()
)
tmnxBsxGrpStatusEgrQHCDroOutPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCDroOutPOcts.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxGrpStatusEgrQHCDroOutPOcts.setUnits("bytes")
_TmnxBsxAaSubSumTable_Object = MibTable
tmnxBsxAaSubSumTable = _TmnxBsxAaSubSumTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumTable.setStatus("current")
_TmnxBsxAaSubSumEntry_Object = MibTableRow
tmnxBsxAaSubSumEntry = _TmnxBsxAaSubSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1)
)
tmnxBsxAaSubSumEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubStatsInterval"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriber"),
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumEntry.setStatus("current")
_TmnxBsxAaSubStatsInterval_Type = TmnxBsxAaSubStatsInterval
_TmnxBsxAaSubStatsInterval_Object = MibTableColumn
tmnxBsxAaSubStatsInterval = _TmnxBsxAaSubStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 1),
    _TmnxBsxAaSubStatsInterval_Type()
)
tmnxBsxAaSubStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAaSubStatsInterval.setStatus("current")
_TmnxBsxAaSubSumMdaSlotNum_Type = TmnxSlotNumOrZero
_TmnxBsxAaSubSumMdaSlotNum_Object = MibTableColumn
tmnxBsxAaSubSumMdaSlotNum = _TmnxBsxAaSubSumMdaSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 2),
    _TmnxBsxAaSubSumMdaSlotNum_Type()
)
tmnxBsxAaSubSumMdaSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumMdaSlotNum.setStatus("current")


class _TmnxBsxAaSubSumMdaMdaNum_Type(Unsigned32):
    """Custom type tmnxBsxAaSubSumMdaMdaNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TmnxBsxAaSubSumMdaMdaNum_Type.__name__ = "Unsigned32"
_TmnxBsxAaSubSumMdaMdaNum_Object = MibTableColumn
tmnxBsxAaSubSumMdaMdaNum = _TmnxBsxAaSubSumMdaMdaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 3),
    _TmnxBsxAaSubSumMdaMdaNum_Type()
)
tmnxBsxAaSubSumMdaMdaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumMdaMdaNum.setStatus("current")
_TmnxBsxAaSubSumAppProfName_Type = TNamedItem
_TmnxBsxAaSubSumAppProfName_Object = MibTableColumn
tmnxBsxAaSubSumAppProfName = _TmnxBsxAaSubSumAppProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 4),
    _TmnxBsxAaSubSumAppProfName_Type()
)
tmnxBsxAaSubSumAppProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumAppProfName.setStatus("current")
_TmnxBsxAaSubSumDiscontTime_Type = TimeStamp
_TmnxBsxAaSubSumDiscontTime_Object = MibTableColumn
tmnxBsxAaSubSumDiscontTime = _TmnxBsxAaSubSumDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 5),
    _TmnxBsxAaSubSumDiscontTime_Type()
)
tmnxBsxAaSubSumDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumDiscontTime.setStatus("current")
_TmnxBsxAaSubSumOctsAdmFmSb_Type = Counter32
_TmnxBsxAaSubSumOctsAdmFmSb_Object = MibTableColumn
tmnxBsxAaSubSumOctsAdmFmSb = _TmnxBsxAaSubSumOctsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 6),
    _TmnxBsxAaSubSumOctsAdmFmSb_Type()
)
tmnxBsxAaSubSumOctsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumOctsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumOctsAdmFmSb.setUnits("bytes")
_TmnxBsxAaSubSumPktsAdmFmSb_Type = Counter32
_TmnxBsxAaSubSumPktsAdmFmSb_Object = MibTableColumn
tmnxBsxAaSubSumPktsAdmFmSb = _TmnxBsxAaSubSumPktsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 7),
    _TmnxBsxAaSubSumPktsAdmFmSb_Type()
)
tmnxBsxAaSubSumPktsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumPktsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumPktsAdmFmSb.setUnits("packets")
_TmnxBsxAaSubSumFlwsAdmFmSb_Type = Counter32
_TmnxBsxAaSubSumFlwsAdmFmSb_Object = MibTableColumn
tmnxBsxAaSubSumFlwsAdmFmSb = _TmnxBsxAaSubSumFlwsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 8),
    _TmnxBsxAaSubSumFlwsAdmFmSb_Type()
)
tmnxBsxAaSubSumFlwsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumFlwsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumFlwsAdmFmSb.setUnits("flows")
_TmnxBsxAaSubSumOctsDnyFmSb_Type = Counter32
_TmnxBsxAaSubSumOctsDnyFmSb_Object = MibTableColumn
tmnxBsxAaSubSumOctsDnyFmSb = _TmnxBsxAaSubSumOctsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 9),
    _TmnxBsxAaSubSumOctsDnyFmSb_Type()
)
tmnxBsxAaSubSumOctsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumOctsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumOctsDnyFmSb.setUnits("bytes")
_TmnxBsxAaSubSumPktsDnyFmSb_Type = Counter32
_TmnxBsxAaSubSumPktsDnyFmSb_Object = MibTableColumn
tmnxBsxAaSubSumPktsDnyFmSb = _TmnxBsxAaSubSumPktsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 10),
    _TmnxBsxAaSubSumPktsDnyFmSb_Type()
)
tmnxBsxAaSubSumPktsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumPktsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumPktsDnyFmSb.setUnits("packets")
_TmnxBsxAaSubSumFlwsDnyFmSb_Type = Counter32
_TmnxBsxAaSubSumFlwsDnyFmSb_Object = MibTableColumn
tmnxBsxAaSubSumFlwsDnyFmSb = _TmnxBsxAaSubSumFlwsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 11),
    _TmnxBsxAaSubSumFlwsDnyFmSb_Type()
)
tmnxBsxAaSubSumFlwsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumFlwsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumFlwsDnyFmSb.setUnits("flows")
_TmnxBsxAaSubSumOctsAdmToSb_Type = Counter32
_TmnxBsxAaSubSumOctsAdmToSb_Object = MibTableColumn
tmnxBsxAaSubSumOctsAdmToSb = _TmnxBsxAaSubSumOctsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 12),
    _TmnxBsxAaSubSumOctsAdmToSb_Type()
)
tmnxBsxAaSubSumOctsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumOctsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumOctsAdmToSb.setUnits("bytes")
_TmnxBsxAaSubSumPktsAdmToSb_Type = Counter32
_TmnxBsxAaSubSumPktsAdmToSb_Object = MibTableColumn
tmnxBsxAaSubSumPktsAdmToSb = _TmnxBsxAaSubSumPktsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 13),
    _TmnxBsxAaSubSumPktsAdmToSb_Type()
)
tmnxBsxAaSubSumPktsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumPktsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumPktsAdmToSb.setUnits("packets")
_TmnxBsxAaSubSumFlwsAdmToSb_Type = Counter32
_TmnxBsxAaSubSumFlwsAdmToSb_Object = MibTableColumn
tmnxBsxAaSubSumFlwsAdmToSb = _TmnxBsxAaSubSumFlwsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 14),
    _TmnxBsxAaSubSumFlwsAdmToSb_Type()
)
tmnxBsxAaSubSumFlwsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumFlwsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumFlwsAdmToSb.setUnits("flows")
_TmnxBsxAaSubSumOctsDnyToSb_Type = Counter32
_TmnxBsxAaSubSumOctsDnyToSb_Object = MibTableColumn
tmnxBsxAaSubSumOctsDnyToSb = _TmnxBsxAaSubSumOctsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 15),
    _TmnxBsxAaSubSumOctsDnyToSb_Type()
)
tmnxBsxAaSubSumOctsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumOctsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumOctsDnyToSb.setUnits("bytes")
_TmnxBsxAaSubSumPktsDnyToSb_Type = Counter32
_TmnxBsxAaSubSumPktsDnyToSb_Object = MibTableColumn
tmnxBsxAaSubSumPktsDnyToSb = _TmnxBsxAaSubSumPktsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 16),
    _TmnxBsxAaSubSumPktsDnyToSb_Type()
)
tmnxBsxAaSubSumPktsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumPktsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumPktsDnyToSb.setUnits("packets")
_TmnxBsxAaSubSumFlwsDnyToSb_Type = Counter32
_TmnxBsxAaSubSumFlwsDnyToSb_Object = MibTableColumn
tmnxBsxAaSubSumFlwsDnyToSb = _TmnxBsxAaSubSumFlwsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 17),
    _TmnxBsxAaSubSumFlwsDnyToSb_Type()
)
tmnxBsxAaSubSumFlwsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumFlwsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumFlwsDnyToSb.setUnits("flows")
_TmnxBsxAaSubSumTermFlwDur_Type = Counter32
_TmnxBsxAaSubSumTermFlwDur_Object = MibTableColumn
tmnxBsxAaSubSumTermFlwDur = _TmnxBsxAaSubSumTermFlwDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 18),
    _TmnxBsxAaSubSumTermFlwDur_Type()
)
tmnxBsxAaSubSumTermFlwDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumTermFlwDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumTermFlwDur.setUnits("seconds")
_TmnxBsxAaSubSumTermFlws_Type = Counter32
_TmnxBsxAaSubSumTermFlws_Object = MibTableColumn
tmnxBsxAaSubSumTermFlws = _TmnxBsxAaSubSumTermFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 19),
    _TmnxBsxAaSubSumTermFlws_Type()
)
tmnxBsxAaSubSumTermFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumTermFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumTermFlws.setUnits("flows")
_TmnxBsxAaSubSumShrtDurFlws_Type = Counter32
_TmnxBsxAaSubSumShrtDurFlws_Object = MibTableColumn
tmnxBsxAaSubSumShrtDurFlws = _TmnxBsxAaSubSumShrtDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 20),
    _TmnxBsxAaSubSumShrtDurFlws_Type()
)
tmnxBsxAaSubSumShrtDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumShrtDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumShrtDurFlws.setUnits("flows")
_TmnxBsxAaSubSumMedDurFlws_Type = Counter32
_TmnxBsxAaSubSumMedDurFlws_Object = MibTableColumn
tmnxBsxAaSubSumMedDurFlws = _TmnxBsxAaSubSumMedDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 21),
    _TmnxBsxAaSubSumMedDurFlws_Type()
)
tmnxBsxAaSubSumMedDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumMedDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumMedDurFlws.setUnits("flows")
_TmnxBsxAaSubSumLngDurFlws_Type = Counter32
_TmnxBsxAaSubSumLngDurFlws_Object = MibTableColumn
tmnxBsxAaSubSumLngDurFlws = _TmnxBsxAaSubSumLngDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 22),
    _TmnxBsxAaSubSumLngDurFlws_Type()
)
tmnxBsxAaSubSumLngDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumLngDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumLngDurFlws.setUnits("flows")
_TmnxBsxAaSubSumActFlwsFmSb_Type = Gauge32
_TmnxBsxAaSubSumActFlwsFmSb_Object = MibTableColumn
tmnxBsxAaSubSumActFlwsFmSb = _TmnxBsxAaSubSumActFlwsFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 23),
    _TmnxBsxAaSubSumActFlwsFmSb_Type()
)
tmnxBsxAaSubSumActFlwsFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumActFlwsFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumActFlwsFmSb.setUnits("flows")
_TmnxBsxAaSubSumActFlwsToSb_Type = Gauge32
_TmnxBsxAaSubSumActFlwsToSb_Object = MibTableColumn
tmnxBsxAaSubSumActFlwsToSb = _TmnxBsxAaSubSumActFlwsToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 24),
    _TmnxBsxAaSubSumActFlwsToSb_Type()
)
tmnxBsxAaSubSumActFlwsToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumActFlwsToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumActFlwsToSb.setUnits("flows")
_TmnxBsxAaSubSumHCOctsAdmFmSb_Type = Counter64
_TmnxBsxAaSubSumHCOctsAdmFmSb_Object = MibTableColumn
tmnxBsxAaSubSumHCOctsAdmFmSb = _TmnxBsxAaSubSumHCOctsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 25),
    _TmnxBsxAaSubSumHCOctsAdmFmSb_Type()
)
tmnxBsxAaSubSumHCOctsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCOctsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCOctsAdmFmSb.setUnits("bytes")
_TmnxBsxAaSubSumHCPktsAdmFmSb_Type = Counter64
_TmnxBsxAaSubSumHCPktsAdmFmSb_Object = MibTableColumn
tmnxBsxAaSubSumHCPktsAdmFmSb = _TmnxBsxAaSubSumHCPktsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 26),
    _TmnxBsxAaSubSumHCPktsAdmFmSb_Type()
)
tmnxBsxAaSubSumHCPktsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCPktsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCPktsAdmFmSb.setUnits("packets")
_TmnxBsxAaSubSumHCFlwsAdmFmSb_Type = Counter64
_TmnxBsxAaSubSumHCFlwsAdmFmSb_Object = MibTableColumn
tmnxBsxAaSubSumHCFlwsAdmFmSb = _TmnxBsxAaSubSumHCFlwsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 27),
    _TmnxBsxAaSubSumHCFlwsAdmFmSb_Type()
)
tmnxBsxAaSubSumHCFlwsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCFlwsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCFlwsAdmFmSb.setUnits("flows")
_TmnxBsxAaSubSumHCOctsDnyFmSb_Type = Counter64
_TmnxBsxAaSubSumHCOctsDnyFmSb_Object = MibTableColumn
tmnxBsxAaSubSumHCOctsDnyFmSb = _TmnxBsxAaSubSumHCOctsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 28),
    _TmnxBsxAaSubSumHCOctsDnyFmSb_Type()
)
tmnxBsxAaSubSumHCOctsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCOctsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCOctsDnyFmSb.setUnits("bytes")
_TmnxBsxAaSubSumHCPktsDnyFmSb_Type = Counter64
_TmnxBsxAaSubSumHCPktsDnyFmSb_Object = MibTableColumn
tmnxBsxAaSubSumHCPktsDnyFmSb = _TmnxBsxAaSubSumHCPktsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 29),
    _TmnxBsxAaSubSumHCPktsDnyFmSb_Type()
)
tmnxBsxAaSubSumHCPktsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCPktsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCPktsDnyFmSb.setUnits("packets")
_TmnxBsxAaSubSumHCFlwsDnyFmSb_Type = Counter64
_TmnxBsxAaSubSumHCFlwsDnyFmSb_Object = MibTableColumn
tmnxBsxAaSubSumHCFlwsDnyFmSb = _TmnxBsxAaSubSumHCFlwsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 30),
    _TmnxBsxAaSubSumHCFlwsDnyFmSb_Type()
)
tmnxBsxAaSubSumHCFlwsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCFlwsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCFlwsDnyFmSb.setUnits("flows")
_TmnxBsxAaSubSumHCOctsAdmToSb_Type = Counter64
_TmnxBsxAaSubSumHCOctsAdmToSb_Object = MibTableColumn
tmnxBsxAaSubSumHCOctsAdmToSb = _TmnxBsxAaSubSumHCOctsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 31),
    _TmnxBsxAaSubSumHCOctsAdmToSb_Type()
)
tmnxBsxAaSubSumHCOctsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCOctsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCOctsAdmToSb.setUnits("bytes")
_TmnxBsxAaSubSumHCPktsAdmToSb_Type = Counter64
_TmnxBsxAaSubSumHCPktsAdmToSb_Object = MibTableColumn
tmnxBsxAaSubSumHCPktsAdmToSb = _TmnxBsxAaSubSumHCPktsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 32),
    _TmnxBsxAaSubSumHCPktsAdmToSb_Type()
)
tmnxBsxAaSubSumHCPktsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCPktsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCPktsAdmToSb.setUnits("packets")
_TmnxBsxAaSubSumHCFlwsAdmToSb_Type = Counter64
_TmnxBsxAaSubSumHCFlwsAdmToSb_Object = MibTableColumn
tmnxBsxAaSubSumHCFlwsAdmToSb = _TmnxBsxAaSubSumHCFlwsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 33),
    _TmnxBsxAaSubSumHCFlwsAdmToSb_Type()
)
tmnxBsxAaSubSumHCFlwsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCFlwsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCFlwsAdmToSb.setUnits("flows")
_TmnxBsxAaSubSumHCOctsDnyToSb_Type = Counter64
_TmnxBsxAaSubSumHCOctsDnyToSb_Object = MibTableColumn
tmnxBsxAaSubSumHCOctsDnyToSb = _TmnxBsxAaSubSumHCOctsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 34),
    _TmnxBsxAaSubSumHCOctsDnyToSb_Type()
)
tmnxBsxAaSubSumHCOctsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCOctsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCOctsDnyToSb.setUnits("bytes")
_TmnxBsxAaSubSumHCPktsDnyToSb_Type = Counter64
_TmnxBsxAaSubSumHCPktsDnyToSb_Object = MibTableColumn
tmnxBsxAaSubSumHCPktsDnyToSb = _TmnxBsxAaSubSumHCPktsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 35),
    _TmnxBsxAaSubSumHCPktsDnyToSb_Type()
)
tmnxBsxAaSubSumHCPktsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCPktsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCPktsDnyToSb.setUnits("packets")
_TmnxBsxAaSubSumHCFlwsDnyToSb_Type = Counter64
_TmnxBsxAaSubSumHCFlwsDnyToSb_Object = MibTableColumn
tmnxBsxAaSubSumHCFlwsDnyToSb = _TmnxBsxAaSubSumHCFlwsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 36),
    _TmnxBsxAaSubSumHCFlwsDnyToSb_Type()
)
tmnxBsxAaSubSumHCFlwsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCFlwsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCFlwsDnyToSb.setUnits("flows")
_TmnxBsxAaSubSumHCTermFlwDur_Type = Counter64
_TmnxBsxAaSubSumHCTermFlwDur_Object = MibTableColumn
tmnxBsxAaSubSumHCTermFlwDur = _TmnxBsxAaSubSumHCTermFlwDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 37),
    _TmnxBsxAaSubSumHCTermFlwDur_Type()
)
tmnxBsxAaSubSumHCTermFlwDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCTermFlwDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCTermFlwDur.setUnits("seconds")
_TmnxBsxAaSubSumHCTermFlws_Type = Counter64
_TmnxBsxAaSubSumHCTermFlws_Object = MibTableColumn
tmnxBsxAaSubSumHCTermFlws = _TmnxBsxAaSubSumHCTermFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 38),
    _TmnxBsxAaSubSumHCTermFlws_Type()
)
tmnxBsxAaSubSumHCTermFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCTermFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCTermFlws.setUnits("flows")
_TmnxBsxAaSubSumHCShrtDurFlws_Type = Counter64
_TmnxBsxAaSubSumHCShrtDurFlws_Object = MibTableColumn
tmnxBsxAaSubSumHCShrtDurFlws = _TmnxBsxAaSubSumHCShrtDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 39),
    _TmnxBsxAaSubSumHCShrtDurFlws_Type()
)
tmnxBsxAaSubSumHCShrtDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCShrtDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCShrtDurFlws.setUnits("flows")
_TmnxBsxAaSubSumHCMedDurFlws_Type = Counter64
_TmnxBsxAaSubSumHCMedDurFlws_Object = MibTableColumn
tmnxBsxAaSubSumHCMedDurFlws = _TmnxBsxAaSubSumHCMedDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 40),
    _TmnxBsxAaSubSumHCMedDurFlws_Type()
)
tmnxBsxAaSubSumHCMedDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCMedDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCMedDurFlws.setUnits("flows")
_TmnxBsxAaSubSumHCLngDurFlws_Type = Counter64
_TmnxBsxAaSubSumHCLngDurFlws_Object = MibTableColumn
tmnxBsxAaSubSumHCLngDurFlws = _TmnxBsxAaSubSumHCLngDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 8, 1, 41),
    _TmnxBsxAaSubSumHCLngDurFlws_Type()
)
tmnxBsxAaSubSumHCLngDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCLngDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxAaSubSumHCLngDurFlws.setUnits("flows")
_TmnxBsxAaGrpPartTable_Object = MibTable
tmnxBsxAaGrpPartTable = _TmnxBsxAaGrpPartTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxBsxAaGrpPartTable.setStatus("current")
_TmnxBsxAaGrpPartEntry_Object = MibTableRow
tmnxBsxAaGrpPartEntry = _TmnxBsxAaGrpPartEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 9, 1)
)
tmnxBsxAaGrpPartEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxAaGrpPartEntry.setStatus("current")
_TmnxBsxAaGrpPartIndex_Type = TmnxBsxAaGrpPartIndex
_TmnxBsxAaGrpPartIndex_Object = MibTableColumn
tmnxBsxAaGrpPartIndex = _TmnxBsxAaGrpPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 9, 1, 1),
    _TmnxBsxAaGrpPartIndex_Type()
)
tmnxBsxAaGrpPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAaGrpPartIndex.setStatus("current")
_TmnxBsxAaGrpPartRowStatus_Type = RowStatus
_TmnxBsxAaGrpPartRowStatus_Object = MibTableColumn
tmnxBsxAaGrpPartRowStatus = _TmnxBsxAaGrpPartRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 9, 1, 2),
    _TmnxBsxAaGrpPartRowStatus_Type()
)
tmnxBsxAaGrpPartRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAaGrpPartRowStatus.setStatus("current")
_TmnxBsxAaGrpPartRowLastChange_Type = TimeStamp
_TmnxBsxAaGrpPartRowLastChange_Object = MibTableColumn
tmnxBsxAaGrpPartRowLastChange = _TmnxBsxAaGrpPartRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 9, 1, 3),
    _TmnxBsxAaGrpPartRowLastChange_Type()
)
tmnxBsxAaGrpPartRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaGrpPartRowLastChange.setStatus("current")
_TmnxBsxAaGrpPartDescription_Type = TItemDescription
_TmnxBsxAaGrpPartDescription_Object = MibTableColumn
tmnxBsxAaGrpPartDescription = _TmnxBsxAaGrpPartDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 9, 1, 4),
    _TmnxBsxAaGrpPartDescription_Type()
)
tmnxBsxAaGrpPartDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAaGrpPartDescription.setStatus("current")


class _TmnxBsxAaGrpPartXOnlineHost_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxAaGrpPartXOnlineHost based on TmnxEnabledDisabled"""


_TmnxBsxAaGrpPartXOnlineHost_Object = MibTableColumn
tmnxBsxAaGrpPartXOnlineHost = _TmnxBsxAaGrpPartXOnlineHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 9, 1, 5),
    _TmnxBsxAaGrpPartXOnlineHost_Type()
)
tmnxBsxAaGrpPartXOnlineHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAaGrpPartXOnlineHost.setStatus("current")


class _TmnxBsxAaGrpPartHttpMatchAllReq_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxAaGrpPartHttpMatchAllReq based on TmnxEnabledDisabled"""


_TmnxBsxAaGrpPartHttpMatchAllReq_Object = MibTableColumn
tmnxBsxAaGrpPartHttpMatchAllReq = _TmnxBsxAaGrpPartHttpMatchAllReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 9, 1, 6),
    _TmnxBsxAaGrpPartHttpMatchAllReq_Type()
)
tmnxBsxAaGrpPartHttpMatchAllReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAaGrpPartHttpMatchAllReq.setStatus("current")


class _TmnxBsxAaGrpPartAaSubRemote_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxAaGrpPartAaSubRemote based on TmnxEnabledDisabled"""


_TmnxBsxAaGrpPartAaSubRemote_Object = MibTableColumn
tmnxBsxAaGrpPartAaSubRemote = _TmnxBsxAaGrpPartAaSubRemote_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 9, 1, 7),
    _TmnxBsxAaGrpPartAaSubRemote_Type()
)
tmnxBsxAaGrpPartAaSubRemote.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAaGrpPartAaSubRemote.setStatus("current")
_TmnxBsxIsaLoadBalUnSubTable_Object = MibTable
tmnxBsxIsaLoadBalUnSubTable = _TmnxBsxIsaLoadBalUnSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxBsxIsaLoadBalUnSubTable.setStatus("current")
_TmnxBsxIsaLoadBalUnSubEntry_Object = MibTableRow
tmnxBsxIsaLoadBalUnSubEntry = _TmnxBsxIsaLoadBalUnSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 10, 1)
)
tmnxBsxIsaLoadBalUnSubEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaLoadBalUnSub"),
)
if mibBuilder.loadTexts:
    tmnxBsxIsaLoadBalUnSubEntry.setStatus("current")
_TmnxBsxIsaLoadBalUnSub_Type = TmnxBsxAaSubscriber
_TmnxBsxIsaLoadBalUnSub_Object = MibTableColumn
tmnxBsxIsaLoadBalUnSub = _TmnxBsxIsaLoadBalUnSub_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 10, 1, 1),
    _TmnxBsxIsaLoadBalUnSub_Type()
)
tmnxBsxIsaLoadBalUnSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaLoadBalUnSub.setStatus("current")
_TmnxBsxIsaLoadBalUnSubTransit_Type = Gauge32
_TmnxBsxIsaLoadBalUnSubTransit_Object = MibTableColumn
tmnxBsxIsaLoadBalUnSubTransit = _TmnxBsxIsaLoadBalUnSubTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 10, 1, 2),
    _TmnxBsxIsaLoadBalUnSubTransit_Type()
)
tmnxBsxIsaLoadBalUnSubTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxIsaLoadBalUnSubTransit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxIsaLoadBalUnSubTransit.setUnits("subscribers")
_TmnxBsxAaSubTable_Object = MibTable
tmnxBsxAaSubTable = _TmnxBsxAaSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubTable.setStatus("current")
_TmnxBsxAaSubEntry_Object = MibTableRow
tmnxBsxAaSubEntry = _TmnxBsxAaSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 11, 1)
)
tmnxBsxAaSubEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriber"),
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubEntry.setStatus("current")
_TmnxBsxAaSubMdaSlotNum_Type = TmnxSlotNumOrZero
_TmnxBsxAaSubMdaSlotNum_Object = MibTableColumn
tmnxBsxAaSubMdaSlotNum = _TmnxBsxAaSubMdaSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 11, 1, 1),
    _TmnxBsxAaSubMdaSlotNum_Type()
)
tmnxBsxAaSubMdaSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubMdaSlotNum.setStatus("current")


class _TmnxBsxAaSubMdaMdaNum_Type(Unsigned32):
    """Custom type tmnxBsxAaSubMdaMdaNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TmnxBsxAaSubMdaMdaNum_Type.__name__ = "Unsigned32"
_TmnxBsxAaSubMdaMdaNum_Object = MibTableColumn
tmnxBsxAaSubMdaMdaNum = _TmnxBsxAaSubMdaMdaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 11, 1, 2),
    _TmnxBsxAaSubMdaMdaNum_Type()
)
tmnxBsxAaSubMdaMdaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubMdaMdaNum.setStatus("current")
_TmnxBsxAaSubAppProfName_Type = TNamedItem
_TmnxBsxAaSubAppProfName_Object = MibTableColumn
tmnxBsxAaSubAppProfName = _TmnxBsxAaSubAppProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 11, 1, 3),
    _TmnxBsxAaSubAppProfName_Type()
)
tmnxBsxAaSubAppProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubAppProfName.setStatus("current")
_TmnxBsxAaSubHasOverrides_Type = TruthValue
_TmnxBsxAaSubHasOverrides_Object = MibTableColumn
tmnxBsxAaSubHasOverrides = _TmnxBsxAaSubHasOverrides_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 11, 1, 4),
    _TmnxBsxAaSubHasOverrides_Type()
)
tmnxBsxAaSubHasOverrides.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubHasOverrides.setStatus("current")
_TmnxBsxAaSubTransitIpPolicyId_Type = TmnxBsxTransitIpPolicyIdOrZero
_TmnxBsxAaSubTransitIpPolicyId_Object = MibTableColumn
tmnxBsxAaSubTransitIpPolicyId = _TmnxBsxAaSubTransitIpPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 11, 1, 5),
    _TmnxBsxAaSubTransitIpPolicyId_Type()
)
tmnxBsxAaSubTransitIpPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubTransitIpPolicyId.setStatus("current")
_TmnxBsxAaSubTransPrefPolicyId_Type = TmnxBsxTransPrefPolicyIdOrZero
_TmnxBsxAaSubTransPrefPolicyId_Object = MibTableColumn
tmnxBsxAaSubTransPrefPolicyId = _TmnxBsxAaSubTransPrefPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 11, 1, 6),
    _TmnxBsxAaSubTransPrefPolicyId_Type()
)
tmnxBsxAaSubTransPrefPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubTransPrefPolicyId.setStatus("current")
_TmnxBsxAaWap1xTable_Object = MibTable
tmnxBsxAaWap1xTable = _TmnxBsxAaWap1xTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxBsxAaWap1xTable.setStatus("current")
_TmnxBsxAaWap1xEntry_Object = MibTableRow
tmnxBsxAaWap1xEntry = _TmnxBsxAaWap1xEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxBsxAaWap1xEntry.setStatus("current")
_TmnxBsxAaWap1xRowLastChange_Type = TimeStamp
_TmnxBsxAaWap1xRowLastChange_Object = MibTableColumn
tmnxBsxAaWap1xRowLastChange = _TmnxBsxAaWap1xRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 12, 1, 1),
    _TmnxBsxAaWap1xRowLastChange_Type()
)
tmnxBsxAaWap1xRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaWap1xRowLastChange.setStatus("current")


class _TmnxBsxAaWap1xAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxAaWap1xAdminState based on TmnxAdminState"""


_TmnxBsxAaWap1xAdminState_Object = MibTableColumn
tmnxBsxAaWap1xAdminState = _TmnxBsxAaWap1xAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 1, 12, 1, 2),
    _TmnxBsxAaWap1xAdminState_Type()
)
tmnxBsxAaWap1xAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAaWap1xAdminState.setStatus("current")
_TmnxBsxPolicyObjs_ObjectIdentity = ObjectIdentity
tmnxBsxPolicyObjs = _TmnxBsxPolicyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2)
)
_TmnxBsxProtTable_Object = MibTable
tmnxBsxProtTable = _TmnxBsxProtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxBsxProtTable.setStatus("current")
_TmnxBsxProtEntry_Object = MibTableRow
tmnxBsxProtEntry = _TmnxBsxProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 1, 1)
)
tmnxBsxProtEntry.setIndexNames(
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxProtName"),
)
if mibBuilder.loadTexts:
    tmnxBsxProtEntry.setStatus("current")
_TmnxBsxProtName_Type = TNamedItem
_TmnxBsxProtName_Object = MibTableColumn
tmnxBsxProtName = _TmnxBsxProtName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 1, 1, 1),
    _TmnxBsxProtName_Type()
)
tmnxBsxProtName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxProtName.setStatus("current")
_TmnxBsxProtDescription_Type = TItemDescription
_TmnxBsxProtDescription_Object = MibTableColumn
tmnxBsxProtDescription = _TmnxBsxProtDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 1, 1, 2),
    _TmnxBsxProtDescription_Type()
)
tmnxBsxProtDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxProtDescription.setStatus("current")
_TmnxBsxProtParentName_Type = TNamedItemOrEmpty
_TmnxBsxProtParentName_Object = MibTableColumn
tmnxBsxProtParentName = _TmnxBsxProtParentName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 1, 1, 3),
    _TmnxBsxProtParentName_Type()
)
tmnxBsxProtParentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxProtParentName.setStatus("current")


class _TmnxBsxProtAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxProtAdminState based on TmnxAdminState"""


_TmnxBsxProtAdminState_Object = MibTableColumn
tmnxBsxProtAdminState = _TmnxBsxProtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 1, 1, 4),
    _TmnxBsxProtAdminState_Type()
)
tmnxBsxProtAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxProtAdminState.setStatus("current")
_TmnxBsxProtObsolete_Type = TruthValue
_TmnxBsxProtObsolete_Object = MibTableColumn
tmnxBsxProtObsolete = _TmnxBsxProtObsolete_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 1, 1, 5),
    _TmnxBsxProtObsolete_Type()
)
tmnxBsxProtObsolete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxProtObsolete.setStatus("current")
_TmnxBsxAppGrpCfgTable_Object = MibTable
tmnxBsxAppGrpCfgTable = _TmnxBsxAppGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxAppGrpCfgTable.setStatus("current")
_TmnxBsxAppGrpCfgEntry_Object = MibTableRow
tmnxBsxAppGrpCfgEntry = _TmnxBsxAppGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 2, 1)
)
tmnxBsxAppGrpCfgEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpName"),
)
if mibBuilder.loadTexts:
    tmnxBsxAppGrpCfgEntry.setStatus("current")
_TmnxBsxAppGrpPolicyVersion_Type = TmnxBsxPolicyVersion
_TmnxBsxAppGrpPolicyVersion_Object = MibTableColumn
tmnxBsxAppGrpPolicyVersion = _TmnxBsxAppGrpPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 2, 1, 1),
    _TmnxBsxAppGrpPolicyVersion_Type()
)
tmnxBsxAppGrpPolicyVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppGrpPolicyVersion.setStatus("current")
_TmnxBsxAppGrpName_Type = TNamedItem
_TmnxBsxAppGrpName_Object = MibTableColumn
tmnxBsxAppGrpName = _TmnxBsxAppGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 2, 1, 2),
    _TmnxBsxAppGrpName_Type()
)
tmnxBsxAppGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppGrpName.setStatus("current")
_TmnxBsxAppGrpRowStatus_Type = RowStatus
_TmnxBsxAppGrpRowStatus_Object = MibTableColumn
tmnxBsxAppGrpRowStatus = _TmnxBsxAppGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 2, 1, 3),
    _TmnxBsxAppGrpRowStatus_Type()
)
tmnxBsxAppGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppGrpRowStatus.setStatus("current")


class _TmnxBsxAppGrpStorageType_Type(StorageType):
    """Custom type tmnxBsxAppGrpStorageType based on StorageType"""


_TmnxBsxAppGrpStorageType_Object = MibTableColumn
tmnxBsxAppGrpStorageType = _TmnxBsxAppGrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 2, 1, 4),
    _TmnxBsxAppGrpStorageType_Type()
)
tmnxBsxAppGrpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppGrpStorageType.setStatus("current")
_TmnxBsxAppGrpDescription_Type = TItemDescription
_TmnxBsxAppGrpDescription_Object = MibTableColumn
tmnxBsxAppGrpDescription = _TmnxBsxAppGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 2, 1, 5),
    _TmnxBsxAppGrpDescription_Type()
)
tmnxBsxAppGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppGrpDescription.setStatus("current")


class _TmnxBsxAppGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxAppGrpAdminState based on TmnxAdminState"""


_TmnxBsxAppGrpAdminState_Object = MibTableColumn
tmnxBsxAppGrpAdminState = _TmnxBsxAppGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 2, 1, 6),
    _TmnxBsxAppGrpAdminState_Type()
)
tmnxBsxAppGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppGrpAdminState.setStatus("obsolete")
_TmnxBsxAppGrpChargeGrp_Type = TNamedItemOrEmpty
_TmnxBsxAppGrpChargeGrp_Object = MibTableColumn
tmnxBsxAppGrpChargeGrp = _TmnxBsxAppGrpChargeGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 2, 1, 7),
    _TmnxBsxAppGrpChargeGrp_Type()
)
tmnxBsxAppGrpChargeGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppGrpChargeGrp.setStatus("current")
_TmnxBsxAppCfgTable_Object = MibTable
tmnxBsxAppCfgTable = _TmnxBsxAppCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxAppCfgTable.setStatus("current")
_TmnxBsxAppCfgEntry_Object = MibTableRow
tmnxBsxAppCfgEntry = _TmnxBsxAppCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 3, 1)
)
tmnxBsxAppCfgEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppName"),
)
if mibBuilder.loadTexts:
    tmnxBsxAppCfgEntry.setStatus("current")
_TmnxBsxAppPolicyVersion_Type = TmnxBsxPolicyVersion
_TmnxBsxAppPolicyVersion_Object = MibTableColumn
tmnxBsxAppPolicyVersion = _TmnxBsxAppPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 3, 1, 1),
    _TmnxBsxAppPolicyVersion_Type()
)
tmnxBsxAppPolicyVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppPolicyVersion.setStatus("current")
_TmnxBsxAppName_Type = TNamedItem
_TmnxBsxAppName_Object = MibTableColumn
tmnxBsxAppName = _TmnxBsxAppName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 3, 1, 2),
    _TmnxBsxAppName_Type()
)
tmnxBsxAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppName.setStatus("current")
_TmnxBsxAppRowStatus_Type = RowStatus
_TmnxBsxAppRowStatus_Object = MibTableColumn
tmnxBsxAppRowStatus = _TmnxBsxAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 3, 1, 3),
    _TmnxBsxAppRowStatus_Type()
)
tmnxBsxAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppRowStatus.setStatus("current")


class _TmnxBsxAppStorageType_Type(StorageType):
    """Custom type tmnxBsxAppStorageType based on StorageType"""


_TmnxBsxAppStorageType_Object = MibTableColumn
tmnxBsxAppStorageType = _TmnxBsxAppStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 3, 1, 4),
    _TmnxBsxAppStorageType_Type()
)
tmnxBsxAppStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppStorageType.setStatus("current")
_TmnxBsxAppDescription_Type = TItemDescription
_TmnxBsxAppDescription_Object = MibTableColumn
tmnxBsxAppDescription = _TmnxBsxAppDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 3, 1, 5),
    _TmnxBsxAppDescription_Type()
)
tmnxBsxAppDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppDescription.setStatus("current")


class _TmnxBsxAppAppGroup_Type(TNamedItem):
    """Custom type tmnxBsxAppAppGroup based on TNamedItem"""
    defaultValue = OctetString("Unknown")


_TmnxBsxAppAppGroup_Object = MibTableColumn
tmnxBsxAppAppGroup = _TmnxBsxAppAppGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 3, 1, 6),
    _TmnxBsxAppAppGroup_Type()
)
tmnxBsxAppAppGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppAppGroup.setStatus("current")
_TmnxBsxAppChargeGrp_Type = TNamedItemOrEmpty
_TmnxBsxAppChargeGrp_Object = MibTableColumn
tmnxBsxAppChargeGrp = _TmnxBsxAppChargeGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 3, 1, 7),
    _TmnxBsxAppChargeGrp_Type()
)
tmnxBsxAppChargeGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppChargeGrp.setStatus("current")
_TmnxBsxAppFilterTable_Object = MibTable
tmnxBsxAppFilterTable = _TmnxBsxAppFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxAppFilterTable.setStatus("current")
_TmnxBsxAppFilterEntry_Object = MibTableRow
tmnxBsxAppFilterEntry = _TmnxBsxAppFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1)
)
tmnxBsxAppFilterEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterEntryId"),
)
if mibBuilder.loadTexts:
    tmnxBsxAppFilterEntry.setStatus("current")
_TmnxBsxAppFilterPolicyVersion_Type = TmnxBsxPolicyVersion
_TmnxBsxAppFilterPolicyVersion_Object = MibTableColumn
tmnxBsxAppFilterPolicyVersion = _TmnxBsxAppFilterPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 1),
    _TmnxBsxAppFilterPolicyVersion_Type()
)
tmnxBsxAppFilterPolicyVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterPolicyVersion.setStatus("current")
_TmnxBsxAppFilterEntryId_Type = TEntryId
_TmnxBsxAppFilterEntryId_Object = MibTableColumn
tmnxBsxAppFilterEntryId = _TmnxBsxAppFilterEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 2),
    _TmnxBsxAppFilterEntryId_Type()
)
tmnxBsxAppFilterEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterEntryId.setStatus("current")
_TmnxBsxAppFilterRowStatus_Type = RowStatus
_TmnxBsxAppFilterRowStatus_Object = MibTableColumn
tmnxBsxAppFilterRowStatus = _TmnxBsxAppFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 3),
    _TmnxBsxAppFilterRowStatus_Type()
)
tmnxBsxAppFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterRowStatus.setStatus("current")
_TmnxBsxAppFilterDescription_Type = TItemDescription
_TmnxBsxAppFilterDescription_Object = MibTableColumn
tmnxBsxAppFilterDescription = _TmnxBsxAppFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 4),
    _TmnxBsxAppFilterDescription_Type()
)
tmnxBsxAppFilterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterDescription.setStatus("current")


class _TmnxBsxAppFilterAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxAppFilterAdminState based on TmnxAdminState"""


_TmnxBsxAppFilterAdminState_Object = MibTableColumn
tmnxBsxAppFilterAdminState = _TmnxBsxAppFilterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 5),
    _TmnxBsxAppFilterAdminState_Type()
)
tmnxBsxAppFilterAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterAdminState.setStatus("current")
_TmnxBsxAppFilterProtocol_Type = TNamedItemOrEmpty
_TmnxBsxAppFilterProtocol_Object = MibTableColumn
tmnxBsxAppFilterProtocol = _TmnxBsxAppFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 6),
    _TmnxBsxAppFilterProtocol_Type()
)
tmnxBsxAppFilterProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterProtocol.setStatus("current")


class _TmnxBsxAppFilterProtocolOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAppFilterProtocolOp based on TmnxBsxOperator"""


_TmnxBsxAppFilterProtocolOp_Object = MibTableColumn
tmnxBsxAppFilterProtocolOp = _TmnxBsxAppFilterProtocolOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 7),
    _TmnxBsxAppFilterProtocolOp_Type()
)
tmnxBsxAppFilterProtocolOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterProtocolOp.setStatus("current")


class _TmnxBsxAppFilterFlowSetupDir_Type(TmnxBsxDirection):
    """Custom type tmnxBsxAppFilterFlowSetupDir based on TmnxBsxDirection"""


_TmnxBsxAppFilterFlowSetupDir_Object = MibTableColumn
tmnxBsxAppFilterFlowSetupDir = _TmnxBsxAppFilterFlowSetupDir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 8),
    _TmnxBsxAppFilterFlowSetupDir_Type()
)
tmnxBsxAppFilterFlowSetupDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterFlowSetupDir.setStatus("current")


class _TmnxBsxAppFilterIpProtocolNum_Type(TIpProtocol):
    """Custom type tmnxBsxAppFilterIpProtocolNum based on TIpProtocol"""
    defaultValue = -1


_TmnxBsxAppFilterIpProtocolNum_Object = MibTableColumn
tmnxBsxAppFilterIpProtocolNum = _TmnxBsxAppFilterIpProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 9),
    _TmnxBsxAppFilterIpProtocolNum_Type()
)
tmnxBsxAppFilterIpProtocolNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterIpProtocolNum.setStatus("current")


class _TmnxBsxAppFilterIpProtocolNumOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAppFilterIpProtocolNumOp based on TmnxBsxOperator"""


_TmnxBsxAppFilterIpProtocolNumOp_Object = MibTableColumn
tmnxBsxAppFilterIpProtocolNumOp = _TmnxBsxAppFilterIpProtocolNumOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 10),
    _TmnxBsxAppFilterIpProtocolNumOp_Type()
)
tmnxBsxAppFilterIpProtocolNumOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterIpProtocolNumOp.setStatus("current")


class _TmnxBsxAppFilterServerAddrType_Type(InetAddressType):
    """Custom type tmnxBsxAppFilterServerAddrType based on InetAddressType"""


_TmnxBsxAppFilterServerAddrType_Object = MibTableColumn
tmnxBsxAppFilterServerAddrType = _TmnxBsxAppFilterServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 11),
    _TmnxBsxAppFilterServerAddrType_Type()
)
tmnxBsxAppFilterServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterServerAddrType.setStatus("current")


class _TmnxBsxAppFilterServerAddr_Type(InetAddress):
    """Custom type tmnxBsxAppFilterServerAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxAppFilterServerAddr_Type.__name__ = "InetAddress"
_TmnxBsxAppFilterServerAddr_Object = MibTableColumn
tmnxBsxAppFilterServerAddr = _TmnxBsxAppFilterServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 12),
    _TmnxBsxAppFilterServerAddr_Type()
)
tmnxBsxAppFilterServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterServerAddr.setStatus("current")


class _TmnxBsxAppFilterServerAddrLen_Type(InetAddressPrefixLength):
    """Custom type tmnxBsxAppFilterServerAddrLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxBsxAppFilterServerAddrLen_Object = MibTableColumn
tmnxBsxAppFilterServerAddrLen = _TmnxBsxAppFilterServerAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 13),
    _TmnxBsxAppFilterServerAddrLen_Type()
)
tmnxBsxAppFilterServerAddrLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterServerAddrLen.setStatus("current")


class _TmnxBsxAppFilterServerAddrOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAppFilterServerAddrOp based on TmnxBsxOperator"""


_TmnxBsxAppFilterServerAddrOp_Object = MibTableColumn
tmnxBsxAppFilterServerAddrOp = _TmnxBsxAppFilterServerAddrOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 14),
    _TmnxBsxAppFilterServerAddrOp_Type()
)
tmnxBsxAppFilterServerAddrOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterServerAddrOp.setStatus("current")


class _TmnxBsxAppFilterServerPort_Type(TTcpUdpPort):
    """Custom type tmnxBsxAppFilterServerPort based on TTcpUdpPort"""
    defaultValue = 0


_TmnxBsxAppFilterServerPort_Object = MibTableColumn
tmnxBsxAppFilterServerPort = _TmnxBsxAppFilterServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 15),
    _TmnxBsxAppFilterServerPort_Type()
)
tmnxBsxAppFilterServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterServerPort.setStatus("obsolete")


class _TmnxBsxAppFilterServerPortOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAppFilterServerPortOp based on TmnxBsxOperator"""


_TmnxBsxAppFilterServerPortOp_Object = MibTableColumn
tmnxBsxAppFilterServerPortOp = _TmnxBsxAppFilterServerPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 16),
    _TmnxBsxAppFilterServerPortOp_Type()
)
tmnxBsxAppFilterServerPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterServerPortOp.setStatus("current")


class _TmnxBsxAppFilterServerPortFpp_Type(TmnxBsxFirstPacketPolicy):
    """Custom type tmnxBsxAppFilterServerPortFpp based on TmnxBsxFirstPacketPolicy"""


_TmnxBsxAppFilterServerPortFpp_Object = MibTableColumn
tmnxBsxAppFilterServerPortFpp = _TmnxBsxAppFilterServerPortFpp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 17),
    _TmnxBsxAppFilterServerPortFpp_Type()
)
tmnxBsxAppFilterServerPortFpp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterServerPortFpp.setStatus("current")


class _TmnxBsxAppFilterServerPortLow_Type(TTcpUdpPort):
    """Custom type tmnxBsxAppFilterServerPortLow based on TTcpUdpPort"""
    defaultValue = 0


_TmnxBsxAppFilterServerPortLow_Object = MibTableColumn
tmnxBsxAppFilterServerPortLow = _TmnxBsxAppFilterServerPortLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 18),
    _TmnxBsxAppFilterServerPortLow_Type()
)
tmnxBsxAppFilterServerPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterServerPortLow.setStatus("current")


class _TmnxBsxAppFilterServerPortHigh_Type(TTcpUdpPort):
    """Custom type tmnxBsxAppFilterServerPortHigh based on TTcpUdpPort"""
    defaultValue = 0


_TmnxBsxAppFilterServerPortHigh_Object = MibTableColumn
tmnxBsxAppFilterServerPortHigh = _TmnxBsxAppFilterServerPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 19),
    _TmnxBsxAppFilterServerPortHigh_Type()
)
tmnxBsxAppFilterServerPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterServerPortHigh.setStatus("current")


class _TmnxBsxAppFilterApplication_Type(TNamedItem):
    """Custom type tmnxBsxAppFilterApplication based on TNamedItem"""
    defaultValue = OctetString("Unknown")


_TmnxBsxAppFilterApplication_Object = MibTableColumn
tmnxBsxAppFilterApplication = _TmnxBsxAppFilterApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 4, 1, 99),
    _TmnxBsxAppFilterApplication_Type()
)
tmnxBsxAppFilterApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterApplication.setStatus("current")
_TmnxBsxAsoTable_Object = MibTable
tmnxBsxAsoTable = _TmnxBsxAsoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxBsxAsoTable.setStatus("current")
_TmnxBsxAsoEntry_Object = MibTableRow
tmnxBsxAsoEntry = _TmnxBsxAsoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 5, 1)
)
tmnxBsxAsoEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAsoPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAsoCharName"),
)
if mibBuilder.loadTexts:
    tmnxBsxAsoEntry.setStatus("current")
_TmnxBsxAsoPolicyVersion_Type = TmnxBsxPolicyVersion
_TmnxBsxAsoPolicyVersion_Object = MibTableColumn
tmnxBsxAsoPolicyVersion = _TmnxBsxAsoPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 5, 1, 1),
    _TmnxBsxAsoPolicyVersion_Type()
)
tmnxBsxAsoPolicyVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAsoPolicyVersion.setStatus("current")
_TmnxBsxAsoCharName_Type = TNamedItem
_TmnxBsxAsoCharName_Object = MibTableColumn
tmnxBsxAsoCharName = _TmnxBsxAsoCharName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 5, 1, 2),
    _TmnxBsxAsoCharName_Type()
)
tmnxBsxAsoCharName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAsoCharName.setStatus("current")
_TmnxBsxAsoRowStatus_Type = RowStatus
_TmnxBsxAsoRowStatus_Object = MibTableColumn
tmnxBsxAsoRowStatus = _TmnxBsxAsoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 5, 1, 3),
    _TmnxBsxAsoRowStatus_Type()
)
tmnxBsxAsoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAsoRowStatus.setStatus("current")
_TmnxBsxAsoDefValName_Type = TNamedItemOrEmpty
_TmnxBsxAsoDefValName_Object = MibTableColumn
tmnxBsxAsoDefValName = _TmnxBsxAsoDefValName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 5, 1, 4),
    _TmnxBsxAsoDefValName_Type()
)
tmnxBsxAsoDefValName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAsoDefValName.setStatus("current")
_TmnxBsxAsoValTable_Object = MibTable
tmnxBsxAsoValTable = _TmnxBsxAsoValTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxBsxAsoValTable.setStatus("current")
_TmnxBsxAsoValEntry_Object = MibTableRow
tmnxBsxAsoValEntry = _TmnxBsxAsoValEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 6, 1)
)
tmnxBsxAsoValEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAsoValPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAsoValCharName"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxAsoValValName"),
)
if mibBuilder.loadTexts:
    tmnxBsxAsoValEntry.setStatus("current")
_TmnxBsxAsoValPolicyVersion_Type = TmnxBsxPolicyVersion
_TmnxBsxAsoValPolicyVersion_Object = MibTableColumn
tmnxBsxAsoValPolicyVersion = _TmnxBsxAsoValPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 6, 1, 1),
    _TmnxBsxAsoValPolicyVersion_Type()
)
tmnxBsxAsoValPolicyVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAsoValPolicyVersion.setStatus("current")
_TmnxBsxAsoValCharName_Type = TNamedItem
_TmnxBsxAsoValCharName_Object = MibTableColumn
tmnxBsxAsoValCharName = _TmnxBsxAsoValCharName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 6, 1, 2),
    _TmnxBsxAsoValCharName_Type()
)
tmnxBsxAsoValCharName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAsoValCharName.setStatus("current")
_TmnxBsxAsoValValName_Type = TNamedItem
_TmnxBsxAsoValValName_Object = MibTableColumn
tmnxBsxAsoValValName = _TmnxBsxAsoValValName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 6, 1, 3),
    _TmnxBsxAsoValValName_Type()
)
tmnxBsxAsoValValName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAsoValValName.setStatus("current")
_TmnxBsxAsoValRowStatus_Type = RowStatus
_TmnxBsxAsoValRowStatus_Object = MibTableColumn
tmnxBsxAsoValRowStatus = _TmnxBsxAsoValRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 6, 1, 4),
    _TmnxBsxAsoValRowStatus_Type()
)
tmnxBsxAsoValRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAsoValRowStatus.setStatus("current")
_TmnxBsxAppProfTable_Object = MibTable
tmnxBsxAppProfTable = _TmnxBsxAppProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxBsxAppProfTable.setStatus("current")
_TmnxBsxAppProfEntry_Object = MibTableRow
tmnxBsxAppProfEntry = _TmnxBsxAppProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 7, 1)
)
tmnxBsxAppProfEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfName"),
)
if mibBuilder.loadTexts:
    tmnxBsxAppProfEntry.setStatus("current")
_TmnxBsxAppProfName_Type = TNamedItem
_TmnxBsxAppProfName_Object = MibTableColumn
tmnxBsxAppProfName = _TmnxBsxAppProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 7, 1, 1),
    _TmnxBsxAppProfName_Type()
)
tmnxBsxAppProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppProfName.setStatus("current")
_TmnxBsxAppProfRowStatus_Type = RowStatus
_TmnxBsxAppProfRowStatus_Object = MibTableColumn
tmnxBsxAppProfRowStatus = _TmnxBsxAppProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 7, 1, 2),
    _TmnxBsxAppProfRowStatus_Type()
)
tmnxBsxAppProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppProfRowStatus.setStatus("current")
_TmnxBsxAppProfDescription_Type = TItemDescription
_TmnxBsxAppProfDescription_Object = MibTableColumn
tmnxBsxAppProfDescription = _TmnxBsxAppProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 7, 1, 3),
    _TmnxBsxAppProfDescription_Type()
)
tmnxBsxAppProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppProfDescription.setStatus("current")


class _TmnxBsxAppProfDivert_Type(TruthValue):
    """Custom type tmnxBsxAppProfDivert based on TruthValue"""


_TmnxBsxAppProfDivert_Object = MibTableColumn
tmnxBsxAppProfDivert = _TmnxBsxAppProfDivert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 7, 1, 4),
    _TmnxBsxAppProfDivert_Type()
)
tmnxBsxAppProfDivert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppProfDivert.setStatus("current")


class _TmnxBsxAppProfCapacityCost_Type(Unsigned32):
    """Custom type tmnxBsxAppProfCapacityCost based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxBsxAppProfCapacityCost_Type.__name__ = "Unsigned32"
_TmnxBsxAppProfCapacityCost_Object = MibTableColumn
tmnxBsxAppProfCapacityCost = _TmnxBsxAppProfCapacityCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 7, 1, 5),
    _TmnxBsxAppProfCapacityCost_Type()
)
tmnxBsxAppProfCapacityCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppProfCapacityCost.setStatus("current")
_TmnxBsxAppProfCharTable_Object = MibTable
tmnxBsxAppProfCharTable = _TmnxBsxAppProfCharTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxBsxAppProfCharTable.setStatus("current")
_TmnxBsxAppProfCharEntry_Object = MibTableRow
tmnxBsxAppProfCharEntry = _TmnxBsxAppProfCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 8, 1)
)
tmnxBsxAppProfCharEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharProfName"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharCharName"),
)
if mibBuilder.loadTexts:
    tmnxBsxAppProfCharEntry.setStatus("current")
_TmnxBsxAppProfCharPolicyVersion_Type = TmnxBsxPolicyVersion
_TmnxBsxAppProfCharPolicyVersion_Object = MibTableColumn
tmnxBsxAppProfCharPolicyVersion = _TmnxBsxAppProfCharPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 8, 1, 1),
    _TmnxBsxAppProfCharPolicyVersion_Type()
)
tmnxBsxAppProfCharPolicyVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppProfCharPolicyVersion.setStatus("current")
_TmnxBsxAppProfCharProfName_Type = TNamedItem
_TmnxBsxAppProfCharProfName_Object = MibTableColumn
tmnxBsxAppProfCharProfName = _TmnxBsxAppProfCharProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 8, 1, 2),
    _TmnxBsxAppProfCharProfName_Type()
)
tmnxBsxAppProfCharProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppProfCharProfName.setStatus("current")
_TmnxBsxAppProfCharCharName_Type = TNamedItem
_TmnxBsxAppProfCharCharName_Object = MibTableColumn
tmnxBsxAppProfCharCharName = _TmnxBsxAppProfCharCharName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 8, 1, 3),
    _TmnxBsxAppProfCharCharName_Type()
)
tmnxBsxAppProfCharCharName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppProfCharCharName.setStatus("current")
_TmnxBsxAppProfCharRowStatus_Type = RowStatus
_TmnxBsxAppProfCharRowStatus_Object = MibTableColumn
tmnxBsxAppProfCharRowStatus = _TmnxBsxAppProfCharRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 8, 1, 4),
    _TmnxBsxAppProfCharRowStatus_Type()
)
tmnxBsxAppProfCharRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppProfCharRowStatus.setStatus("current")
_TmnxBsxAppProfCharValName_Type = TNamedItem
_TmnxBsxAppProfCharValName_Object = MibTableColumn
tmnxBsxAppProfCharValName = _TmnxBsxAppProfCharValName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 8, 1, 5),
    _TmnxBsxAppProfCharValName_Type()
)
tmnxBsxAppProfCharValName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppProfCharValName.setStatus("current")
_TmnxBsxAqpTable_Object = MibTable
tmnxBsxAqpTable = _TmnxBsxAqpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9)
)
if mibBuilder.loadTexts:
    tmnxBsxAqpTable.setStatus("current")
_TmnxBsxAqpEntry_Object = MibTableRow
tmnxBsxAqpEntry = _TmnxBsxAqpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1)
)
tmnxBsxAqpEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAqpPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAqpEntryId"),
)
if mibBuilder.loadTexts:
    tmnxBsxAqpEntry.setStatus("current")
_TmnxBsxAqpPolicyVersion_Type = TmnxBsxPolicyVersion
_TmnxBsxAqpPolicyVersion_Object = MibTableColumn
tmnxBsxAqpPolicyVersion = _TmnxBsxAqpPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 1),
    _TmnxBsxAqpPolicyVersion_Type()
)
tmnxBsxAqpPolicyVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAqpPolicyVersion.setStatus("current")
_TmnxBsxAqpEntryId_Type = TEntryId
_TmnxBsxAqpEntryId_Object = MibTableColumn
tmnxBsxAqpEntryId = _TmnxBsxAqpEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 2),
    _TmnxBsxAqpEntryId_Type()
)
tmnxBsxAqpEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAqpEntryId.setStatus("current")
_TmnxBsxAqpRowStatus_Type = RowStatus
_TmnxBsxAqpRowStatus_Object = MibTableColumn
tmnxBsxAqpRowStatus = _TmnxBsxAqpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 3),
    _TmnxBsxAqpRowStatus_Type()
)
tmnxBsxAqpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpRowStatus.setStatus("current")
_TmnxBsxAqpDescription_Type = TItemDescription
_TmnxBsxAqpDescription_Object = MibTableColumn
tmnxBsxAqpDescription = _TmnxBsxAqpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 4),
    _TmnxBsxAqpDescription_Type()
)
tmnxBsxAqpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDescription.setStatus("current")


class _TmnxBsxAqpAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxAqpAdminState based on TmnxAdminState"""


_TmnxBsxAqpAdminState_Object = MibTableColumn
tmnxBsxAqpAdminState = _TmnxBsxAqpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 5),
    _TmnxBsxAqpAdminState_Type()
)
tmnxBsxAqpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpAdminState.setStatus("current")
_TmnxBsxAqpApplication_Type = TNamedItemOrEmpty
_TmnxBsxAqpApplication_Object = MibTableColumn
tmnxBsxAqpApplication = _TmnxBsxAqpApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 6),
    _TmnxBsxAqpApplication_Type()
)
tmnxBsxAqpApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpApplication.setStatus("current")


class _TmnxBsxAqpApplicationOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpApplicationOp based on TmnxBsxOperator"""


_TmnxBsxAqpApplicationOp_Object = MibTableColumn
tmnxBsxAqpApplicationOp = _TmnxBsxAqpApplicationOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 7),
    _TmnxBsxAqpApplicationOp_Type()
)
tmnxBsxAqpApplicationOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpApplicationOp.setStatus("current")
_TmnxBsxAqpAppGroup_Type = TNamedItemOrEmpty
_TmnxBsxAqpAppGroup_Object = MibTableColumn
tmnxBsxAqpAppGroup = _TmnxBsxAqpAppGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 8),
    _TmnxBsxAqpAppGroup_Type()
)
tmnxBsxAqpAppGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpAppGroup.setStatus("current")


class _TmnxBsxAqpAppGroupOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpAppGroupOp based on TmnxBsxOperator"""


_TmnxBsxAqpAppGroupOp_Object = MibTableColumn
tmnxBsxAqpAppGroupOp = _TmnxBsxAqpAppGroupOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 9),
    _TmnxBsxAqpAppGroupOp_Type()
)
tmnxBsxAqpAppGroupOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpAppGroupOp.setStatus("current")


class _TmnxBsxAqpTrafficDir_Type(TmnxBsxDirection):
    """Custom type tmnxBsxAqpTrafficDir based on TmnxBsxDirection"""


_TmnxBsxAqpTrafficDir_Object = MibTableColumn
tmnxBsxAqpTrafficDir = _TmnxBsxAqpTrafficDir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 10),
    _TmnxBsxAqpTrafficDir_Type()
)
tmnxBsxAqpTrafficDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpTrafficDir.setStatus("current")
_TmnxBsxAqpSubscriber_Type = TNamedItemOrEmpty
_TmnxBsxAqpSubscriber_Object = MibTableColumn
tmnxBsxAqpSubscriber = _TmnxBsxAqpSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 11),
    _TmnxBsxAqpSubscriber_Type()
)
tmnxBsxAqpSubscriber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSubscriber.setStatus("obsolete")


class _TmnxBsxAqpSubscriberOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpSubscriberOp based on TmnxBsxOperator"""


_TmnxBsxAqpSubscriberOp_Object = MibTableColumn
tmnxBsxAqpSubscriberOp = _TmnxBsxAqpSubscriberOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 12),
    _TmnxBsxAqpSubscriberOp_Type()
)
tmnxBsxAqpSubscriberOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSubscriberOp.setStatus("obsolete")
_TmnxBsxAqpDscp_Type = TDSCPNameOrEmpty
_TmnxBsxAqpDscp_Object = MibTableColumn
tmnxBsxAqpDscp = _TmnxBsxAqpDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 13),
    _TmnxBsxAqpDscp_Type()
)
tmnxBsxAqpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDscp.setStatus("current")


class _TmnxBsxAqpDscpOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpDscpOp based on TmnxBsxOperator"""


_TmnxBsxAqpDscpOp_Object = MibTableColumn
tmnxBsxAqpDscpOp = _TmnxBsxAqpDscpOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 14),
    _TmnxBsxAqpDscpOp_Type()
)
tmnxBsxAqpDscpOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDscpOp.setStatus("current")


class _TmnxBsxAqpSapSubscrPortId_Type(TmnxPortID):
    """Custom type tmnxBsxAqpSapSubscrPortId based on TmnxPortID"""
    defaultValue = 0


_TmnxBsxAqpSapSubscrPortId_Object = MibTableColumn
tmnxBsxAqpSapSubscrPortId = _TmnxBsxAqpSapSubscrPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 15),
    _TmnxBsxAqpSapSubscrPortId_Type()
)
tmnxBsxAqpSapSubscrPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSapSubscrPortId.setStatus("obsolete")


class _TmnxBsxAqpSapSubscrEncapValue_Type(TmnxEncapVal):
    """Custom type tmnxBsxAqpSapSubscrEncapValue based on TmnxEncapVal"""
    defaultValue = 0


_TmnxBsxAqpSapSubscrEncapValue_Object = MibTableColumn
tmnxBsxAqpSapSubscrEncapValue = _TmnxBsxAqpSapSubscrEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 16),
    _TmnxBsxAqpSapSubscrEncapValue_Type()
)
tmnxBsxAqpSapSubscrEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSapSubscrEncapValue.setStatus("obsolete")


class _TmnxBsxAqpSapSubscrOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpSapSubscrOp based on TmnxBsxOperator"""


_TmnxBsxAqpSapSubscrOp_Object = MibTableColumn
tmnxBsxAqpSapSubscrOp = _TmnxBsxAqpSapSubscrOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 17),
    _TmnxBsxAqpSapSubscrOp_Type()
)
tmnxBsxAqpSapSubscrOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSapSubscrOp.setStatus("obsolete")


class _TmnxBsxAqpSrcAddressType_Type(InetAddressType):
    """Custom type tmnxBsxAqpSrcAddressType based on InetAddressType"""


_TmnxBsxAqpSrcAddressType_Object = MibTableColumn
tmnxBsxAqpSrcAddressType = _TmnxBsxAqpSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 18),
    _TmnxBsxAqpSrcAddressType_Type()
)
tmnxBsxAqpSrcAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSrcAddressType.setStatus("current")


class _TmnxBsxAqpSrcAddress_Type(InetAddress):
    """Custom type tmnxBsxAqpSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxAqpSrcAddress_Type.__name__ = "InetAddress"
_TmnxBsxAqpSrcAddress_Object = MibTableColumn
tmnxBsxAqpSrcAddress = _TmnxBsxAqpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 19),
    _TmnxBsxAqpSrcAddress_Type()
)
tmnxBsxAqpSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSrcAddress.setStatus("current")


class _TmnxBsxAqpSrcAddressLength_Type(InetAddressPrefixLength):
    """Custom type tmnxBsxAqpSrcAddressLength based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxBsxAqpSrcAddressLength_Object = MibTableColumn
tmnxBsxAqpSrcAddressLength = _TmnxBsxAqpSrcAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 20),
    _TmnxBsxAqpSrcAddressLength_Type()
)
tmnxBsxAqpSrcAddressLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSrcAddressLength.setStatus("current")


class _TmnxBsxAqpSrcAddressOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpSrcAddressOp based on TmnxBsxOperator"""


_TmnxBsxAqpSrcAddressOp_Object = MibTableColumn
tmnxBsxAqpSrcAddressOp = _TmnxBsxAqpSrcAddressOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 21),
    _TmnxBsxAqpSrcAddressOp_Type()
)
tmnxBsxAqpSrcAddressOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSrcAddressOp.setStatus("current")


class _TmnxBsxAqpSrcPortOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpSrcPortOp based on TmnxBsxOperator"""


_TmnxBsxAqpSrcPortOp_Object = MibTableColumn
tmnxBsxAqpSrcPortOp = _TmnxBsxAqpSrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 22),
    _TmnxBsxAqpSrcPortOp_Type()
)
tmnxBsxAqpSrcPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSrcPortOp.setStatus("current")


class _TmnxBsxAqpSrcPortLowValue_Type(TTcpUdpPort):
    """Custom type tmnxBsxAqpSrcPortLowValue based on TTcpUdpPort"""
    defaultValue = 0


_TmnxBsxAqpSrcPortLowValue_Object = MibTableColumn
tmnxBsxAqpSrcPortLowValue = _TmnxBsxAqpSrcPortLowValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 23),
    _TmnxBsxAqpSrcPortLowValue_Type()
)
tmnxBsxAqpSrcPortLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSrcPortLowValue.setStatus("current")


class _TmnxBsxAqpSrcPortHighValue_Type(TTcpUdpPort):
    """Custom type tmnxBsxAqpSrcPortHighValue based on TTcpUdpPort"""
    defaultValue = 0


_TmnxBsxAqpSrcPortHighValue_Object = MibTableColumn
tmnxBsxAqpSrcPortHighValue = _TmnxBsxAqpSrcPortHighValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 24),
    _TmnxBsxAqpSrcPortHighValue_Type()
)
tmnxBsxAqpSrcPortHighValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSrcPortHighValue.setStatus("current")


class _TmnxBsxAqpDstAddressType_Type(InetAddressType):
    """Custom type tmnxBsxAqpDstAddressType based on InetAddressType"""


_TmnxBsxAqpDstAddressType_Object = MibTableColumn
tmnxBsxAqpDstAddressType = _TmnxBsxAqpDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 25),
    _TmnxBsxAqpDstAddressType_Type()
)
tmnxBsxAqpDstAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDstAddressType.setStatus("current")


class _TmnxBsxAqpDstAddress_Type(InetAddress):
    """Custom type tmnxBsxAqpDstAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxAqpDstAddress_Type.__name__ = "InetAddress"
_TmnxBsxAqpDstAddress_Object = MibTableColumn
tmnxBsxAqpDstAddress = _TmnxBsxAqpDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 26),
    _TmnxBsxAqpDstAddress_Type()
)
tmnxBsxAqpDstAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDstAddress.setStatus("current")


class _TmnxBsxAqpDstAddressLength_Type(InetAddressPrefixLength):
    """Custom type tmnxBsxAqpDstAddressLength based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxBsxAqpDstAddressLength_Object = MibTableColumn
tmnxBsxAqpDstAddressLength = _TmnxBsxAqpDstAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 27),
    _TmnxBsxAqpDstAddressLength_Type()
)
tmnxBsxAqpDstAddressLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDstAddressLength.setStatus("current")


class _TmnxBsxAqpDstAddressOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpDstAddressOp based on TmnxBsxOperator"""


_TmnxBsxAqpDstAddressOp_Object = MibTableColumn
tmnxBsxAqpDstAddressOp = _TmnxBsxAqpDstAddressOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 28),
    _TmnxBsxAqpDstAddressOp_Type()
)
tmnxBsxAqpDstAddressOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDstAddressOp.setStatus("current")


class _TmnxBsxAqpDstPortOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpDstPortOp based on TmnxBsxOperator"""


_TmnxBsxAqpDstPortOp_Object = MibTableColumn
tmnxBsxAqpDstPortOp = _TmnxBsxAqpDstPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 29),
    _TmnxBsxAqpDstPortOp_Type()
)
tmnxBsxAqpDstPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDstPortOp.setStatus("current")


class _TmnxBsxAqpDstPortLowValue_Type(TTcpUdpPort):
    """Custom type tmnxBsxAqpDstPortLowValue based on TTcpUdpPort"""
    defaultValue = 0


_TmnxBsxAqpDstPortLowValue_Object = MibTableColumn
tmnxBsxAqpDstPortLowValue = _TmnxBsxAqpDstPortLowValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 30),
    _TmnxBsxAqpDstPortLowValue_Type()
)
tmnxBsxAqpDstPortLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDstPortLowValue.setStatus("current")


class _TmnxBsxAqpDstPortHighValue_Type(TTcpUdpPort):
    """Custom type tmnxBsxAqpDstPortHighValue based on TTcpUdpPort"""
    defaultValue = 0


_TmnxBsxAqpDstPortHighValue_Object = MibTableColumn
tmnxBsxAqpDstPortHighValue = _TmnxBsxAqpDstPortHighValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 31),
    _TmnxBsxAqpDstPortHighValue_Type()
)
tmnxBsxAqpDstPortHighValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDstPortHighValue.setStatus("current")


class _TmnxBsxAqpSpokeSdpSubscr_Type(SdpBindId):
    """Custom type tmnxBsxAqpSpokeSdpSubscr based on SdpBindId"""
    defaultHexValue = "0"


_TmnxBsxAqpSpokeSdpSubscr_Object = MibTableColumn
tmnxBsxAqpSpokeSdpSubscr = _TmnxBsxAqpSpokeSdpSubscr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 32),
    _TmnxBsxAqpSpokeSdpSubscr_Type()
)
tmnxBsxAqpSpokeSdpSubscr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSpokeSdpSubscr.setStatus("obsolete")


class _TmnxBsxAqpSpokeSdpSubscrOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpSpokeSdpSubscrOp based on TmnxBsxOperator"""


_TmnxBsxAqpSpokeSdpSubscrOp_Object = MibTableColumn
tmnxBsxAqpSpokeSdpSubscrOp = _TmnxBsxAqpSpokeSdpSubscrOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 33),
    _TmnxBsxAqpSpokeSdpSubscrOp_Type()
)
tmnxBsxAqpSpokeSdpSubscrOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpSpokeSdpSubscrOp.setStatus("obsolete")


class _TmnxBsxAqpAaSubscriberType_Type(TmnxBsxAaSubscriberType):
    """Custom type tmnxBsxAqpAaSubscriberType based on TmnxBsxAaSubscriberType"""


_TmnxBsxAqpAaSubscriberType_Object = MibTableColumn
tmnxBsxAqpAaSubscriberType = _TmnxBsxAqpAaSubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 34),
    _TmnxBsxAqpAaSubscriberType_Type()
)
tmnxBsxAqpAaSubscriberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpAaSubscriberType.setStatus("current")
_TmnxBsxAqpAaSubscriber_Type = TmnxBsxAaSubscriber
_TmnxBsxAqpAaSubscriber_Object = MibTableColumn
tmnxBsxAqpAaSubscriber = _TmnxBsxAqpAaSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 35),
    _TmnxBsxAqpAaSubscriber_Type()
)
tmnxBsxAqpAaSubscriber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpAaSubscriber.setStatus("current")


class _TmnxBsxAqpAaSubscriberOp_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpAaSubscriberOp based on TmnxBsxOperator"""


_TmnxBsxAqpAaSubscriberOp_Object = MibTableColumn
tmnxBsxAqpAaSubscriberOp = _TmnxBsxAqpAaSubscriberOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 36),
    _TmnxBsxAqpAaSubscriberOp_Type()
)
tmnxBsxAqpAaSubscriberOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpAaSubscriberOp.setStatus("current")


class _TmnxBsxAqpDrop_Type(TruthValue):
    """Custom type tmnxBsxAqpDrop based on TruthValue"""


_TmnxBsxAqpDrop_Object = MibTableColumn
tmnxBsxAqpDrop = _TmnxBsxAqpDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 50),
    _TmnxBsxAqpDrop_Type()
)
tmnxBsxAqpDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpDrop.setStatus("current")
_TmnxBsxAqpBwLimitPolicer_Type = TNamedItemOrEmpty
_TmnxBsxAqpBwLimitPolicer_Object = MibTableColumn
tmnxBsxAqpBwLimitPolicer = _TmnxBsxAqpBwLimitPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 51),
    _TmnxBsxAqpBwLimitPolicer_Type()
)
tmnxBsxAqpBwLimitPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpBwLimitPolicer.setStatus("current")
_TmnxBsxAqpFlowRatePolicer_Type = TNamedItemOrEmpty
_TmnxBsxAqpFlowRatePolicer_Object = MibTableColumn
tmnxBsxAqpFlowRatePolicer = _TmnxBsxAqpFlowRatePolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 52),
    _TmnxBsxAqpFlowRatePolicer_Type()
)
tmnxBsxAqpFlowRatePolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpFlowRatePolicer.setStatus("current")
_TmnxBsxAqpFlowCountPolicer_Type = TNamedItemOrEmpty
_TmnxBsxAqpFlowCountPolicer_Object = MibTableColumn
tmnxBsxAqpFlowCountPolicer = _TmnxBsxAqpFlowCountPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 53),
    _TmnxBsxAqpFlowCountPolicer_Type()
)
tmnxBsxAqpFlowCountPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpFlowCountPolicer.setStatus("current")


class _TmnxBsxAqpRemarkFc_Type(TFCNameOrEmpty):
    """Custom type tmnxBsxAqpRemarkFc based on TFCNameOrEmpty"""
    defaultHexValue = ""


_TmnxBsxAqpRemarkFc_Object = MibTableColumn
tmnxBsxAqpRemarkFc = _TmnxBsxAqpRemarkFc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 54),
    _TmnxBsxAqpRemarkFc_Type()
)
tmnxBsxAqpRemarkFc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpRemarkFc.setStatus("current")


class _TmnxBsxAqpRemarkPriority_Type(TPriorityOrDefault):
    """Custom type tmnxBsxAqpRemarkPriority based on TPriorityOrDefault"""


_TmnxBsxAqpRemarkPriority_Object = MibTableColumn
tmnxBsxAqpRemarkPriority = _TmnxBsxAqpRemarkPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 55),
    _TmnxBsxAqpRemarkPriority_Type()
)
tmnxBsxAqpRemarkPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpRemarkPriority.setStatus("current")


class _TmnxBsxAqpRemarkDscpInProfile_Type(TDSCPNameOrEmpty):
    """Custom type tmnxBsxAqpRemarkDscpInProfile based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TmnxBsxAqpRemarkDscpInProfile_Object = MibTableColumn
tmnxBsxAqpRemarkDscpInProfile = _TmnxBsxAqpRemarkDscpInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 56),
    _TmnxBsxAqpRemarkDscpInProfile_Type()
)
tmnxBsxAqpRemarkDscpInProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpRemarkDscpInProfile.setStatus("current")


class _TmnxBsxAqpRemarkDscpOutProfile_Type(TDSCPNameOrEmpty):
    """Custom type tmnxBsxAqpRemarkDscpOutProfile based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TmnxBsxAqpRemarkDscpOutProfile_Object = MibTableColumn
tmnxBsxAqpRemarkDscpOutProfile = _TmnxBsxAqpRemarkDscpOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 57),
    _TmnxBsxAqpRemarkDscpOutProfile_Type()
)
tmnxBsxAqpRemarkDscpOutProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpRemarkDscpOutProfile.setStatus("current")


class _TmnxBsxAqpMirrorSource_Type(TmnxServId):
    """Custom type tmnxBsxAqpMirrorSource based on TmnxServId"""
    defaultValue = 0


_TmnxBsxAqpMirrorSource_Object = MibTableColumn
tmnxBsxAqpMirrorSource = _TmnxBsxAqpMirrorSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 58),
    _TmnxBsxAqpMirrorSource_Type()
)
tmnxBsxAqpMirrorSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpMirrorSource.setStatus("current")


class _TmnxBsxAqpMirrorSourceAllIncl_Type(TruthValue):
    """Custom type tmnxBsxAqpMirrorSourceAllIncl based on TruthValue"""


_TmnxBsxAqpMirrorSourceAllIncl_Object = MibTableColumn
tmnxBsxAqpMirrorSourceAllIncl = _TmnxBsxAqpMirrorSourceAllIncl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 59),
    _TmnxBsxAqpMirrorSourceAllIncl_Type()
)
tmnxBsxAqpMirrorSourceAllIncl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpMirrorSourceAllIncl.setStatus("current")
_TmnxBsxAqpHttpErrRedirName_Type = TNamedItemOrEmpty
_TmnxBsxAqpHttpErrRedirName_Object = MibTableColumn
tmnxBsxAqpHttpErrRedirName = _TmnxBsxAqpHttpErrRedirName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 60),
    _TmnxBsxAqpHttpErrRedirName_Type()
)
tmnxBsxAqpHttpErrRedirName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpHttpErrRedirName.setStatus("current")
_TmnxBsxAqpHttpRedirName_Type = TNamedItemOrEmpty
_TmnxBsxAqpHttpRedirName_Object = MibTableColumn
tmnxBsxAqpHttpRedirName = _TmnxBsxAqpHttpRedirName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 61),
    _TmnxBsxAqpHttpRedirName_Type()
)
tmnxBsxAqpHttpRedirName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpHttpRedirName.setStatus("current")


class _TmnxBsxAqpHttpRedirFlowType_Type(TmnxBsxAqpHttpRedirFlowType):
    """Custom type tmnxBsxAqpHttpRedirFlowType based on TmnxBsxAqpHttpRedirFlowType"""


_TmnxBsxAqpHttpRedirFlowType_Object = MibTableColumn
tmnxBsxAqpHttpRedirFlowType = _TmnxBsxAqpHttpRedirFlowType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 62),
    _TmnxBsxAqpHttpRedirFlowType_Type()
)
tmnxBsxAqpHttpRedirFlowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpHttpRedirFlowType.setStatus("current")
_TmnxBsxAqpHttpEnrichName_Type = TNamedItemOrEmpty
_TmnxBsxAqpHttpEnrichName_Object = MibTableColumn
tmnxBsxAqpHttpEnrichName = _TmnxBsxAqpHttpEnrichName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 9, 1, 63),
    _TmnxBsxAqpHttpEnrichName_Type()
)
tmnxBsxAqpHttpEnrichName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpHttpEnrichName.setStatus("current")
_TmnxBsxAdminControl_ObjectIdentity = ObjectIdentity
tmnxBsxAdminControl = _TmnxBsxAdminControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 10)
)
_TmnxBsxAdminOwner_Type = TNamedItemOrEmpty
_TmnxBsxAdminOwner_Object = MibScalar
tmnxBsxAdminOwner = _TmnxBsxAdminOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 10, 1),
    _TmnxBsxAdminOwner_Type()
)
tmnxBsxAdminOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxAdminOwner.setStatus("obsolete")


class _TmnxBsxAdminControlApply_Type(Integer32):
    """Custom type tmnxBsxAdminControlApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commit", 3),
          ("initialize", 2),
          ("none", 1))
    )


_TmnxBsxAdminControlApply_Type.__name__ = "Integer32"
_TmnxBsxAdminControlApply_Object = MibScalar
tmnxBsxAdminControlApply = _TmnxBsxAdminControlApply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 10, 2),
    _TmnxBsxAdminControlApply_Type()
)
tmnxBsxAdminControlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxAdminControlApply.setStatus("obsolete")
_TmnxBsxAdminLastChangeTime_Type = TimeStamp
_TmnxBsxAdminLastChangeTime_Object = MibScalar
tmnxBsxAdminLastChangeTime = _TmnxBsxAdminLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 10, 3),
    _TmnxBsxAdminLastChangeTime_Type()
)
tmnxBsxAdminLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAdminLastChangeTime.setStatus("obsolete")
_TmnxBsxAdminCtrlTable_Object = MibTable
tmnxBsxAdminCtrlTable = _TmnxBsxAdminCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 10, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxAdminCtrlTable.setStatus("current")
_TmnxBsxAdminCtrlEntry_Object = MibTableRow
tmnxBsxAdminCtrlEntry = _TmnxBsxAdminCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 10, 4, 1)
)
tmnxBsxAdminCtrlEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxAdminCtrlEntry.setStatus("current")
_TmnxBsxAdminCtrlLastChTime_Type = TimeStamp
_TmnxBsxAdminCtrlLastChTime_Object = MibTableColumn
tmnxBsxAdminCtrlLastChTime = _TmnxBsxAdminCtrlLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 10, 4, 1, 1),
    _TmnxBsxAdminCtrlLastChTime_Type()
)
tmnxBsxAdminCtrlLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAdminCtrlLastChTime.setStatus("current")
_TmnxBsxAdminCtrlConfigOwner_Type = TNamedItemOrEmpty
_TmnxBsxAdminCtrlConfigOwner_Object = MibTableColumn
tmnxBsxAdminCtrlConfigOwner = _TmnxBsxAdminCtrlConfigOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 10, 4, 1, 2),
    _TmnxBsxAdminCtrlConfigOwner_Type()
)
tmnxBsxAdminCtrlConfigOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxAdminCtrlConfigOwner.setStatus("current")
_TmnxBsxAdminCtrlApply_Type = TmnxBsxAdminCtrl
_TmnxBsxAdminCtrlApply_Object = MibTableColumn
tmnxBsxAdminCtrlApply = _TmnxBsxAdminCtrlApply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 10, 4, 1, 3),
    _TmnxBsxAdminCtrlApply_Type()
)
tmnxBsxAdminCtrlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxAdminCtrlApply.setStatus("current")
_TmnxBsxPolicerTable_Object = MibTable
tmnxBsxPolicerTable = _TmnxBsxPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11)
)
if mibBuilder.loadTexts:
    tmnxBsxPolicerTable.setStatus("current")
_TmnxBsxPolicerEntry_Object = MibTableRow
tmnxBsxPolicerEntry = _TmnxBsxPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1)
)
tmnxBsxPolicerEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerName"),
)
if mibBuilder.loadTexts:
    tmnxBsxPolicerEntry.setStatus("current")
_TmnxBsxPolicerName_Type = TNamedItem
_TmnxBsxPolicerName_Object = MibTableColumn
tmnxBsxPolicerName = _TmnxBsxPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 1),
    _TmnxBsxPolicerName_Type()
)
tmnxBsxPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxPolicerName.setStatus("current")
_TmnxBsxPolicerRowStatus_Type = RowStatus
_TmnxBsxPolicerRowStatus_Object = MibTableColumn
tmnxBsxPolicerRowStatus = _TmnxBsxPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 2),
    _TmnxBsxPolicerRowStatus_Type()
)
tmnxBsxPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerRowStatus.setStatus("current")
_TmnxBsxPolicerDescription_Type = TItemDescription
_TmnxBsxPolicerDescription_Object = MibTableColumn
tmnxBsxPolicerDescription = _TmnxBsxPolicerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 3),
    _TmnxBsxPolicerDescription_Type()
)
tmnxBsxPolicerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerDescription.setStatus("current")


class _TmnxBsxPolicerType_Type(TmnxBsxPolicerType):
    """Custom type tmnxBsxPolicerType based on TmnxBsxPolicerType"""


_TmnxBsxPolicerType_Object = MibTableColumn
tmnxBsxPolicerType = _TmnxBsxPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 4),
    _TmnxBsxPolicerType_Type()
)
tmnxBsxPolicerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerType.setStatus("current")


class _TmnxBsxPolicerGranularity_Type(TmnxBsxGranularity):
    """Custom type tmnxBsxPolicerGranularity based on TmnxBsxGranularity"""


_TmnxBsxPolicerGranularity_Object = MibTableColumn
tmnxBsxPolicerGranularity = _TmnxBsxPolicerGranularity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 5),
    _TmnxBsxPolicerGranularity_Type()
)
tmnxBsxPolicerGranularity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerGranularity.setStatus("current")


class _TmnxBsxPolicerAction_Type(TmnxBsxPolicerAction):
    """Custom type tmnxBsxPolicerAction based on TmnxBsxPolicerAction"""


_TmnxBsxPolicerAction_Object = MibTableColumn
tmnxBsxPolicerAction = _TmnxBsxPolicerAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 6),
    _TmnxBsxPolicerAction_Type()
)
tmnxBsxPolicerAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerAction.setStatus("current")


class _TmnxBsxPolicerAdminPIR_Type(TPIRRate):
    """Custom type tmnxBsxPolicerAdminPIR based on TPIRRate"""
    defaultValue = -1


_TmnxBsxPolicerAdminPIR_Object = MibTableColumn
tmnxBsxPolicerAdminPIR = _TmnxBsxPolicerAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 7),
    _TmnxBsxPolicerAdminPIR_Type()
)
tmnxBsxPolicerAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxPolicerAdminPIR.setUnits("kbps or flows")


class _TmnxBsxPolicerAdminCIR_Type(TCIRRate):
    """Custom type tmnxBsxPolicerAdminCIR based on TCIRRate"""
    defaultValue = 0


_TmnxBsxPolicerAdminCIR_Object = MibTableColumn
tmnxBsxPolicerAdminCIR = _TmnxBsxPolicerAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 8),
    _TmnxBsxPolicerAdminCIR_Type()
)
tmnxBsxPolicerAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxPolicerAdminCIR.setUnits("kbps or flows")


class _TmnxBsxPolicerMBS_Type(TmnxBsxBurstSize):
    """Custom type tmnxBsxPolicerMBS based on TmnxBsxBurstSize"""
    defaultValue = 0


_TmnxBsxPolicerMBS_Object = MibTableColumn
tmnxBsxPolicerMBS = _TmnxBsxPolicerMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 9),
    _TmnxBsxPolicerMBS_Type()
)
tmnxBsxPolicerMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerMBS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxPolicerMBS.setUnits("KB or flows")


class _TmnxBsxPolicerCBS_Type(TmnxBsxBurstSize):
    """Custom type tmnxBsxPolicerCBS based on TmnxBsxBurstSize"""
    defaultValue = 0


_TmnxBsxPolicerCBS_Object = MibTableColumn
tmnxBsxPolicerCBS = _TmnxBsxPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 10),
    _TmnxBsxPolicerCBS_Type()
)
tmnxBsxPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerCBS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxPolicerCBS.setUnits("KB or flows")


class _TmnxBsxPolicerPIRAdaptation_Type(TAdaptationRule):
    """Custom type tmnxBsxPolicerPIRAdaptation based on TAdaptationRule"""


_TmnxBsxPolicerPIRAdaptation_Object = MibTableColumn
tmnxBsxPolicerPIRAdaptation = _TmnxBsxPolicerPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 11),
    _TmnxBsxPolicerPIRAdaptation_Type()
)
tmnxBsxPolicerPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerPIRAdaptation.setStatus("current")


class _TmnxBsxPolicerCIRAdaptation_Type(TAdaptationRule):
    """Custom type tmnxBsxPolicerCIRAdaptation based on TAdaptationRule"""


_TmnxBsxPolicerCIRAdaptation_Object = MibTableColumn
tmnxBsxPolicerCIRAdaptation = _TmnxBsxPolicerCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 11, 1, 12),
    _TmnxBsxPolicerCIRAdaptation_Type()
)
tmnxBsxPolicerCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPolicerCIRAdaptation.setStatus("current")
_TmnxBsxIsaAaTim_ObjectIdentity = ObjectIdentity
tmnxBsxIsaAaTim = _TmnxBsxIsaAaTim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 12)
)
_TmnxBsxUpgrade_Type = TmnxActionType
_TmnxBsxUpgrade_Object = MibScalar
tmnxBsxUpgrade = _TmnxBsxUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 12, 1),
    _TmnxBsxUpgrade_Type()
)
tmnxBsxUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxUpgrade.setStatus("current")
_TmnxBsxVersion_Type = DisplayString
_TmnxBsxVersion_Object = MibScalar
tmnxBsxVersion = _TmnxBsxVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 12, 2),
    _TmnxBsxVersion_Type()
)
tmnxBsxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxVersion.setStatus("current")
_TmnxBsxAqpStatsTable_Object = MibTable
tmnxBsxAqpStatsTable = _TmnxBsxAqpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 13)
)
if mibBuilder.loadTexts:
    tmnxBsxAqpStatsTable.setStatus("current")
_TmnxBsxAqpStatsEntry_Object = MibTableRow
tmnxBsxAqpStatsEntry = _TmnxBsxAqpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 13, 1)
)
tmnxBsxAqpStatsEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAqpEntryId"),
)
if mibBuilder.loadTexts:
    tmnxBsxAqpStatsEntry.setStatus("current")
_TmnxBsxAqpStatsFlows_Type = Counter32
_TmnxBsxAqpStatsFlows_Object = MibTableColumn
tmnxBsxAqpStatsFlows = _TmnxBsxAqpStatsFlows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 13, 1, 1),
    _TmnxBsxAqpStatsFlows_Type()
)
tmnxBsxAqpStatsFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAqpStatsFlows.setStatus("obsolete")
_TmnxBsxAqpStatsConflicts_Type = Counter32
_TmnxBsxAqpStatsConflicts_Object = MibTableColumn
tmnxBsxAqpStatsConflicts = _TmnxBsxAqpStatsConflicts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 13, 1, 2),
    _TmnxBsxAqpStatsConflicts_Type()
)
tmnxBsxAqpStatsConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAqpStatsConflicts.setStatus("obsolete")
_TmnxBsxAqpStatsHCFlows_Type = Counter64
_TmnxBsxAqpStatsHCFlows_Object = MibTableColumn
tmnxBsxAqpStatsHCFlows = _TmnxBsxAqpStatsHCFlows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 13, 1, 3),
    _TmnxBsxAqpStatsHCFlows_Type()
)
tmnxBsxAqpStatsHCFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAqpStatsHCFlows.setStatus("current")
_TmnxBsxAqpStatsFlowsLo_Type = Counter32
_TmnxBsxAqpStatsFlowsLo_Object = MibTableColumn
tmnxBsxAqpStatsFlowsLo = _TmnxBsxAqpStatsFlowsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 13, 1, 4),
    _TmnxBsxAqpStatsFlowsLo_Type()
)
tmnxBsxAqpStatsFlowsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAqpStatsFlowsLo.setStatus("current")
_TmnxBsxAqpStatsFlowsHi_Type = Counter32
_TmnxBsxAqpStatsFlowsHi_Object = MibTableColumn
tmnxBsxAqpStatsFlowsHi = _TmnxBsxAqpStatsFlowsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 13, 1, 5),
    _TmnxBsxAqpStatsFlowsHi_Type()
)
tmnxBsxAqpStatsFlowsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAqpStatsFlowsHi.setStatus("current")
_TmnxBsxAqpStatsHCConflicts_Type = Counter64
_TmnxBsxAqpStatsHCConflicts_Object = MibTableColumn
tmnxBsxAqpStatsHCConflicts = _TmnxBsxAqpStatsHCConflicts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 13, 1, 6),
    _TmnxBsxAqpStatsHCConflicts_Type()
)
tmnxBsxAqpStatsHCConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAqpStatsHCConflicts.setStatus("current")
_TmnxBsxAqpStatsConflictsLo_Type = Counter32
_TmnxBsxAqpStatsConflictsLo_Object = MibTableColumn
tmnxBsxAqpStatsConflictsLo = _TmnxBsxAqpStatsConflictsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 13, 1, 7),
    _TmnxBsxAqpStatsConflictsLo_Type()
)
tmnxBsxAqpStatsConflictsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAqpStatsConflictsLo.setStatus("current")
_TmnxBsxAqpStatsConflictsHi_Type = Counter32
_TmnxBsxAqpStatsConflictsHi_Object = MibTableColumn
tmnxBsxAqpStatsConflictsHi = _TmnxBsxAqpStatsConflictsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 13, 1, 8),
    _TmnxBsxAqpStatsConflictsHi_Type()
)
tmnxBsxAqpStatsConflictsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAqpStatsConflictsHi.setStatus("current")
_TmnxBsxInfo_ObjectIdentity = ObjectIdentity
tmnxBsxInfo = _TmnxBsxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 14)
)


class _TmnxBsxFlowFullHighWatermark_Type(Integer32):
    """Custom type tmnxBsxFlowFullHighWatermark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxBsxFlowFullHighWatermark_Type.__name__ = "Integer32"
_TmnxBsxFlowFullHighWatermark_Object = MibScalar
tmnxBsxFlowFullHighWatermark = _TmnxBsxFlowFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 14, 1),
    _TmnxBsxFlowFullHighWatermark_Type()
)
tmnxBsxFlowFullHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxFlowFullHighWatermark.setStatus("current")


class _TmnxBsxFlowFullLowWatermark_Type(Integer32):
    """Custom type tmnxBsxFlowFullLowWatermark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxBsxFlowFullLowWatermark_Type.__name__ = "Integer32"
_TmnxBsxFlowFullLowWatermark_Object = MibScalar
tmnxBsxFlowFullLowWatermark = _TmnxBsxFlowFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 14, 2),
    _TmnxBsxFlowFullLowWatermark_Type()
)
tmnxBsxFlowFullLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxFlowFullLowWatermark.setStatus("current")


class _TmnxBsxFlowSetupHighWatermark_Type(Integer32):
    """Custom type tmnxBsxFlowSetupHighWatermark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_TmnxBsxFlowSetupHighWatermark_Type.__name__ = "Integer32"
_TmnxBsxFlowSetupHighWatermark_Object = MibScalar
tmnxBsxFlowSetupHighWatermark = _TmnxBsxFlowSetupHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 14, 3),
    _TmnxBsxFlowSetupHighWatermark_Type()
)
tmnxBsxFlowSetupHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxFlowSetupHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxFlowSetupHighWatermark.setUnits("flows per second")


class _TmnxBsxFlowSetupLowWatermark_Type(Integer32):
    """Custom type tmnxBsxFlowSetupLowWatermark based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxBsxFlowSetupLowWatermark_Type.__name__ = "Integer32"
_TmnxBsxFlowSetupLowWatermark_Object = MibScalar
tmnxBsxFlowSetupLowWatermark = _TmnxBsxFlowSetupLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 14, 4),
    _TmnxBsxFlowSetupLowWatermark_Type()
)
tmnxBsxFlowSetupLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxFlowSetupLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxFlowSetupLowWatermark.setUnits("flows per second")


class _TmnxBsxPacketRateHighWatermark_Type(Integer32):
    """Custom type tmnxBsxPacketRateHighWatermark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_TmnxBsxPacketRateHighWatermark_Type.__name__ = "Integer32"
_TmnxBsxPacketRateHighWatermark_Object = MibScalar
tmnxBsxPacketRateHighWatermark = _TmnxBsxPacketRateHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 14, 5),
    _TmnxBsxPacketRateHighWatermark_Type()
)
tmnxBsxPacketRateHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxPacketRateHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxPacketRateHighWatermark.setUnits("packets per second")


class _TmnxBsxPacketRateLowWatermark_Type(Integer32):
    """Custom type tmnxBsxPacketRateLowWatermark based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxBsxPacketRateLowWatermark_Type.__name__ = "Integer32"
_TmnxBsxPacketRateLowWatermark_Object = MibScalar
tmnxBsxPacketRateLowWatermark = _TmnxBsxPacketRateLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 14, 6),
    _TmnxBsxPacketRateLowWatermark_Type()
)
tmnxBsxPacketRateLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxPacketRateLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxPacketRateLowWatermark.setUnits("packets per second")


class _TmnxBsxBitRateHighWatermark_Type(Integer32):
    """Custom type tmnxBsxBitRateHighWatermark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_TmnxBsxBitRateHighWatermark_Type.__name__ = "Integer32"
_TmnxBsxBitRateHighWatermark_Object = MibScalar
tmnxBsxBitRateHighWatermark = _TmnxBsxBitRateHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 14, 7),
    _TmnxBsxBitRateHighWatermark_Type()
)
tmnxBsxBitRateHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxBitRateHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxBitRateHighWatermark.setUnits("megabits per second")


class _TmnxBsxBitRateLowWatermark_Type(Integer32):
    """Custom type tmnxBsxBitRateLowWatermark based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxBsxBitRateLowWatermark_Type.__name__ = "Integer32"
_TmnxBsxBitRateLowWatermark_Object = MibScalar
tmnxBsxBitRateLowWatermark = _TmnxBsxBitRateLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 14, 8),
    _TmnxBsxBitRateLowWatermark_Type()
)
tmnxBsxBitRateLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxBitRateLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxBitRateLowWatermark.setUnits("megabits per second")
_TmnxBsxAqpCharTable_Object = MibTable
tmnxBsxAqpCharTable = _TmnxBsxAqpCharTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 15)
)
if mibBuilder.loadTexts:
    tmnxBsxAqpCharTable.setStatus("current")
_TmnxBsxAqpCharEntry_Object = MibTableRow
tmnxBsxAqpCharEntry = _TmnxBsxAqpCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 15, 1)
)
tmnxBsxAqpCharEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAqpPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAqpEntryId"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAsoCharName"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxAsoValValName"),
)
if mibBuilder.loadTexts:
    tmnxBsxAqpCharEntry.setStatus("current")
_TmnxBsxAqpCharRowStatus_Type = RowStatus
_TmnxBsxAqpCharRowStatus_Object = MibTableColumn
tmnxBsxAqpCharRowStatus = _TmnxBsxAqpCharRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 15, 1, 1),
    _TmnxBsxAqpCharRowStatus_Type()
)
tmnxBsxAqpCharRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpCharRowStatus.setStatus("current")


class _TmnxBsxAqpCharOperator_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAqpCharOperator based on TmnxBsxOperator"""


_TmnxBsxAqpCharOperator_Object = MibTableColumn
tmnxBsxAqpCharOperator = _TmnxBsxAqpCharOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 15, 1, 2),
    _TmnxBsxAqpCharOperator_Type()
)
tmnxBsxAqpCharOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAqpCharOperator.setStatus("current")
_TmnxBsxAppFilterExprTable_Object = MibTable
tmnxBsxAppFilterExprTable = _TmnxBsxAppFilterExprTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 16)
)
if mibBuilder.loadTexts:
    tmnxBsxAppFilterExprTable.setStatus("current")
_TmnxBsxAppFilterExprEntry_Object = MibTableRow
tmnxBsxAppFilterExprEntry = _TmnxBsxAppFilterExprEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 16, 1)
)
tmnxBsxAppFilterExprEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterEntryId"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxAppFilterExprEntry.setStatus("current")
_TmnxBsxAppFilterExprIndex_Type = TmnxBsxExprSubStringIndex
_TmnxBsxAppFilterExprIndex_Object = MibTableColumn
tmnxBsxAppFilterExprIndex = _TmnxBsxAppFilterExprIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 16, 1, 1),
    _TmnxBsxAppFilterExprIndex_Type()
)
tmnxBsxAppFilterExprIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterExprIndex.setStatus("current")
_TmnxBsxAppFilterExprRowStatus_Type = RowStatus
_TmnxBsxAppFilterExprRowStatus_Object = MibTableColumn
tmnxBsxAppFilterExprRowStatus = _TmnxBsxAppFilterExprRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 16, 1, 2),
    _TmnxBsxAppFilterExprRowStatus_Type()
)
tmnxBsxAppFilterExprRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterExprRowStatus.setStatus("current")


class _TmnxBsxAppFilterExprType_Type(TmnxBsxExprSubStringType):
    """Custom type tmnxBsxAppFilterExprType based on TmnxBsxExprSubStringType"""


_TmnxBsxAppFilterExprType_Object = MibTableColumn
tmnxBsxAppFilterExprType = _TmnxBsxAppFilterExprType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 16, 1, 3),
    _TmnxBsxAppFilterExprType_Type()
)
tmnxBsxAppFilterExprType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterExprType.setStatus("current")


class _TmnxBsxAppFilterExprOperator_Type(TmnxBsxOperator):
    """Custom type tmnxBsxAppFilterExprOperator based on TmnxBsxOperator"""


_TmnxBsxAppFilterExprOperator_Object = MibTableColumn
tmnxBsxAppFilterExprOperator = _TmnxBsxAppFilterExprOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 16, 1, 4),
    _TmnxBsxAppFilterExprOperator_Type()
)
tmnxBsxAppFilterExprOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterExprOperator.setStatus("current")
_TmnxBsxAppFilterExprStr_Type = TmnxBsxExprSubString
_TmnxBsxAppFilterExprStr_Object = MibTableColumn
tmnxBsxAppFilterExprStr = _TmnxBsxAppFilterExprStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 16, 1, 5),
    _TmnxBsxAppFilterExprStr_Type()
)
tmnxBsxAppFilterExprStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAppFilterExprStr.setStatus("current")
_TmnxBsxCustProtTable_Object = MibTable
tmnxBsxCustProtTable = _TmnxBsxCustProtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 17)
)
if mibBuilder.loadTexts:
    tmnxBsxCustProtTable.setStatus("current")
_TmnxBsxCustProtEntry_Object = MibTableRow
tmnxBsxCustProtEntry = _TmnxBsxCustProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 17, 1)
)
tmnxBsxCustProtEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtEntryId"),
)
if mibBuilder.loadTexts:
    tmnxBsxCustProtEntry.setStatus("current")
_TmnxBsxCustProtPolicyVersion_Type = TmnxBsxPolicyVersion
_TmnxBsxCustProtPolicyVersion_Object = MibTableColumn
tmnxBsxCustProtPolicyVersion = _TmnxBsxCustProtPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 17, 1, 1),
    _TmnxBsxCustProtPolicyVersion_Type()
)
tmnxBsxCustProtPolicyVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxCustProtPolicyVersion.setStatus("current")
_TmnxBsxCustProtEntryId_Type = TEntryId
_TmnxBsxCustProtEntryId_Object = MibTableColumn
tmnxBsxCustProtEntryId = _TmnxBsxCustProtEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 17, 1, 2),
    _TmnxBsxCustProtEntryId_Type()
)
tmnxBsxCustProtEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxCustProtEntryId.setStatus("current")
_TmnxBsxCustProtRowStatus_Type = RowStatus
_TmnxBsxCustProtRowStatus_Object = MibTableColumn
tmnxBsxCustProtRowStatus = _TmnxBsxCustProtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 17, 1, 3),
    _TmnxBsxCustProtRowStatus_Type()
)
tmnxBsxCustProtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCustProtRowStatus.setStatus("current")
_TmnxBsxCustProtRowLastChange_Type = TimeStamp
_TmnxBsxCustProtRowLastChange_Object = MibTableColumn
tmnxBsxCustProtRowLastChange = _TmnxBsxCustProtRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 17, 1, 4),
    _TmnxBsxCustProtRowLastChange_Type()
)
tmnxBsxCustProtRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCustProtRowLastChange.setStatus("current")


class _TmnxBsxCustProtIpProtocolNum_Type(TIpProtocol):
    """Custom type tmnxBsxCustProtIpProtocolNum based on TIpProtocol"""
    defaultValue = -1


_TmnxBsxCustProtIpProtocolNum_Object = MibTableColumn
tmnxBsxCustProtIpProtocolNum = _TmnxBsxCustProtIpProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 17, 1, 5),
    _TmnxBsxCustProtIpProtocolNum_Type()
)
tmnxBsxCustProtIpProtocolNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCustProtIpProtocolNum.setStatus("current")
_TmnxBsxCustProtDescription_Type = TItemDescription
_TmnxBsxCustProtDescription_Object = MibTableColumn
tmnxBsxCustProtDescription = _TmnxBsxCustProtDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 17, 1, 6),
    _TmnxBsxCustProtDescription_Type()
)
tmnxBsxCustProtDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCustProtDescription.setStatus("current")


class _TmnxBsxCustProtAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxCustProtAdminState based on TmnxAdminState"""


_TmnxBsxCustProtAdminState_Object = MibTableColumn
tmnxBsxCustProtAdminState = _TmnxBsxCustProtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 17, 1, 7),
    _TmnxBsxCustProtAdminState_Type()
)
tmnxBsxCustProtAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCustProtAdminState.setStatus("current")
_TmnxBsxCustProtExprTable_Object = MibTable
tmnxBsxCustProtExprTable = _TmnxBsxCustProtExprTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 18)
)
if mibBuilder.loadTexts:
    tmnxBsxCustProtExprTable.setStatus("current")
_TmnxBsxCustProtExprEntry_Object = MibTableRow
tmnxBsxCustProtExprEntry = _TmnxBsxCustProtExprEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 18, 1)
)
tmnxBsxCustProtExprEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtEntryId"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxCustProtExprEntry.setStatus("current")
_TmnxBsxCustProtExprIndex_Type = TmnxBsxExprSubStringIndex
_TmnxBsxCustProtExprIndex_Object = MibTableColumn
tmnxBsxCustProtExprIndex = _TmnxBsxCustProtExprIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 18, 1, 1),
    _TmnxBsxCustProtExprIndex_Type()
)
tmnxBsxCustProtExprIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxCustProtExprIndex.setStatus("current")
_TmnxBsxCustProtExprRowStatus_Type = RowStatus
_TmnxBsxCustProtExprRowStatus_Object = MibTableColumn
tmnxBsxCustProtExprRowStatus = _TmnxBsxCustProtExprRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 18, 1, 2),
    _TmnxBsxCustProtExprRowStatus_Type()
)
tmnxBsxCustProtExprRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCustProtExprRowStatus.setStatus("current")
_TmnxBsxCustProtExprRowLastChange_Type = TimeStamp
_TmnxBsxCustProtExprRowLastChange_Object = MibTableColumn
tmnxBsxCustProtExprRowLastChange = _TmnxBsxCustProtExprRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 18, 1, 3),
    _TmnxBsxCustProtExprRowLastChange_Type()
)
tmnxBsxCustProtExprRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCustProtExprRowLastChange.setStatus("current")


class _TmnxBsxCustProtExprOffset_Type(Unsigned32):
    """Custom type tmnxBsxCustProtExprOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxBsxCustProtExprOffset_Type.__name__ = "Unsigned32"
_TmnxBsxCustProtExprOffset_Object = MibTableColumn
tmnxBsxCustProtExprOffset = _TmnxBsxCustProtExprOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 18, 1, 4),
    _TmnxBsxCustProtExprOffset_Type()
)
tmnxBsxCustProtExprOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCustProtExprOffset.setStatus("current")


class _TmnxBsxCustProtExprDirection_Type(TmnxBsxProtocolDirection):
    """Custom type tmnxBsxCustProtExprDirection based on TmnxBsxProtocolDirection"""


_TmnxBsxCustProtExprDirection_Object = MibTableColumn
tmnxBsxCustProtExprDirection = _TmnxBsxCustProtExprDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 18, 1, 5),
    _TmnxBsxCustProtExprDirection_Type()
)
tmnxBsxCustProtExprDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCustProtExprDirection.setStatus("current")


class _TmnxBsxCustProtExprOperator_Type(TmnxBsxOperator):
    """Custom type tmnxBsxCustProtExprOperator based on TmnxBsxOperator"""


_TmnxBsxCustProtExprOperator_Object = MibTableColumn
tmnxBsxCustProtExprOperator = _TmnxBsxCustProtExprOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 18, 1, 6),
    _TmnxBsxCustProtExprOperator_Type()
)
tmnxBsxCustProtExprOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCustProtExprOperator.setStatus("current")
_TmnxBsxCustProtExprStr_Type = TmnxBsxCustProtExprSubString
_TmnxBsxCustProtExprStr_Object = MibTableColumn
tmnxBsxCustProtExprStr = _TmnxBsxCustProtExprStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 18, 1, 7),
    _TmnxBsxCustProtExprStr_Type()
)
tmnxBsxCustProtExprStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCustProtExprStr.setStatus("current")
_TmnxBsxAaSubAsoValTable_Object = MibTable
tmnxBsxAaSubAsoValTable = _TmnxBsxAaSubAsoValTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 19)
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubAsoValTable.setStatus("current")
_TmnxBsxAaSubAsoValEntry_Object = MibTableRow
tmnxBsxAaSubAsoValEntry = _TmnxBsxAaSubAsoValEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 19, 1)
)
tmnxBsxAaSubAsoValEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriber"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAsoValCharName"),
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubAsoValEntry.setStatus("current")
_TmnxBsxAaSubAsoValName_Type = TNamedItem
_TmnxBsxAaSubAsoValName_Object = MibTableColumn
tmnxBsxAaSubAsoValName = _TmnxBsxAaSubAsoValName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 19, 1, 1),
    _TmnxBsxAaSubAsoValName_Type()
)
tmnxBsxAaSubAsoValName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubAsoValName.setStatus("current")
_TmnxBsxAaSubAsoValDerivedFrom_Type = TmnxBsxAaSubAsoValDerivedFrom
_TmnxBsxAaSubAsoValDerivedFrom_Object = MibTableColumn
tmnxBsxAaSubAsoValDerivedFrom = _TmnxBsxAaSubAsoValDerivedFrom_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 19, 1, 2),
    _TmnxBsxAaSubAsoValDerivedFrom_Type()
)
tmnxBsxAaSubAsoValDerivedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubAsoValDerivedFrom.setStatus("current")
_TmnxBsxAaSubPolicerTable_Object = MibTable
tmnxBsxAaSubPolicerTable = _TmnxBsxAaSubPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 20)
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolicerTable.setStatus("current")
_TmnxBsxAaSubPolicerEntry_Object = MibTableRow
tmnxBsxAaSubPolicerEntry = _TmnxBsxAaSubPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 20, 1)
)
tmnxBsxAaSubPolicerEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriber"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolicerType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolicerDirection"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolicerIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolicerEntry.setStatus("current")
_TmnxBsxAaSubPolicerType_Type = TmnxBsxPolicerType
_TmnxBsxAaSubPolicerType_Object = MibTableColumn
tmnxBsxAaSubPolicerType = _TmnxBsxAaSubPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 20, 1, 1),
    _TmnxBsxAaSubPolicerType_Type()
)
tmnxBsxAaSubPolicerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolicerType.setStatus("current")
_TmnxBsxAaSubPolicerDirection_Type = TmnxBsxDirection
_TmnxBsxAaSubPolicerDirection_Object = MibTableColumn
tmnxBsxAaSubPolicerDirection = _TmnxBsxAaSubPolicerDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 20, 1, 2),
    _TmnxBsxAaSubPolicerDirection_Type()
)
tmnxBsxAaSubPolicerDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolicerDirection.setStatus("current")


class _TmnxBsxAaSubPolicerIndex_Type(Integer32):
    """Custom type tmnxBsxAaSubPolicerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_TmnxBsxAaSubPolicerIndex_Type.__name__ = "Integer32"
_TmnxBsxAaSubPolicerIndex_Object = MibTableColumn
tmnxBsxAaSubPolicerIndex = _TmnxBsxAaSubPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 20, 1, 3),
    _TmnxBsxAaSubPolicerIndex_Type()
)
tmnxBsxAaSubPolicerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolicerIndex.setStatus("current")
_TmnxBsxAaSubPolicerAqpEntryId_Type = TEntryId
_TmnxBsxAaSubPolicerAqpEntryId_Object = MibTableColumn
tmnxBsxAaSubPolicerAqpEntryId = _TmnxBsxAaSubPolicerAqpEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 20, 1, 4),
    _TmnxBsxAaSubPolicerAqpEntryId_Type()
)
tmnxBsxAaSubPolicerAqpEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolicerAqpEntryId.setStatus("current")
_TmnxBsxAaSubPolicerName_Type = TNamedItem
_TmnxBsxAaSubPolicerName_Object = MibTableColumn
tmnxBsxAaSubPolicerName = _TmnxBsxAaSubPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 20, 1, 5),
    _TmnxBsxAaSubPolicerName_Type()
)
tmnxBsxAaSubPolicerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolicerName.setStatus("current")
_TmnxBsxAaSubPolResExTable_Object = MibTable
tmnxBsxAaSubPolResExTable = _TmnxBsxAaSubPolResExTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 21)
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolResExTable.setStatus("current")
_TmnxBsxAaSubPolResExEntry_Object = MibTableRow
tmnxBsxAaSubPolResExEntry = _TmnxBsxAaSubPolResExEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 21, 1)
)
tmnxBsxAaSubPolResExEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriber"),
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolResExEntry.setStatus("current")
_TmnxBsxAaSubPolResExStatus_Type = TmnxBsxAaSubPolicerResStatus
_TmnxBsxAaSubPolResExStatus_Object = MibTableColumn
tmnxBsxAaSubPolResExStatus = _TmnxBsxAaSubPolResExStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 21, 1, 1),
    _TmnxBsxAaSubPolResExStatus_Type()
)
tmnxBsxAaSubPolResExStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolResExStatus.setStatus("current")
_TmnxBsxPolicyScalars_ObjectIdentity = ObjectIdentity
tmnxBsxPolicyScalars = _TmnxBsxPolicyScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 22)
)
_TmnxBsxPlcyCfgLastChTime_Type = TimeStamp
_TmnxBsxPlcyCfgLastChTime_Object = MibScalar
tmnxBsxPlcyCfgLastChTime = _TmnxBsxPlcyCfgLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 22, 1),
    _TmnxBsxPlcyCfgLastChTime_Type()
)
tmnxBsxPlcyCfgLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxPlcyCfgLastChTime.setStatus("current")
_TmnxBsxChargeGrpLastChTime_Type = TimeStamp
_TmnxBsxChargeGrpLastChTime_Object = MibScalar
tmnxBsxChargeGrpLastChTime = _TmnxBsxChargeGrpLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 22, 2),
    _TmnxBsxChargeGrpLastChTime_Type()
)
tmnxBsxChargeGrpLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxChargeGrpLastChTime.setStatus("current")
_TmnxBsxChargeGrpCfgTable_Object = MibTable
tmnxBsxChargeGrpCfgTable = _TmnxBsxChargeGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 23)
)
if mibBuilder.loadTexts:
    tmnxBsxChargeGrpCfgTable.setStatus("current")
_TmnxBsxChargeGrpCfgEntry_Object = MibTableRow
tmnxBsxChargeGrpCfgEntry = _TmnxBsxChargeGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 23, 1)
)
tmnxBsxChargeGrpCfgEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxChargeGrpPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxChargeGrpName"),
)
if mibBuilder.loadTexts:
    tmnxBsxChargeGrpCfgEntry.setStatus("current")
_TmnxBsxChargeGrpPolicyVersion_Type = TmnxBsxPolicyVersion
_TmnxBsxChargeGrpPolicyVersion_Object = MibTableColumn
tmnxBsxChargeGrpPolicyVersion = _TmnxBsxChargeGrpPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 23, 1, 1),
    _TmnxBsxChargeGrpPolicyVersion_Type()
)
tmnxBsxChargeGrpPolicyVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxChargeGrpPolicyVersion.setStatus("current")
_TmnxBsxChargeGrpName_Type = TNamedItem
_TmnxBsxChargeGrpName_Object = MibTableColumn
tmnxBsxChargeGrpName = _TmnxBsxChargeGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 23, 1, 2),
    _TmnxBsxChargeGrpName_Type()
)
tmnxBsxChargeGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxChargeGrpName.setStatus("current")
_TmnxBsxChargeGrpRowStatus_Type = RowStatus
_TmnxBsxChargeGrpRowStatus_Object = MibTableColumn
tmnxBsxChargeGrpRowStatus = _TmnxBsxChargeGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 23, 1, 3),
    _TmnxBsxChargeGrpRowStatus_Type()
)
tmnxBsxChargeGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxChargeGrpRowStatus.setStatus("current")
_TmnxBsxChargeGrpRowLastCh_Type = TimeStamp
_TmnxBsxChargeGrpRowLastCh_Object = MibTableColumn
tmnxBsxChargeGrpRowLastCh = _TmnxBsxChargeGrpRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 23, 1, 4),
    _TmnxBsxChargeGrpRowLastCh_Type()
)
tmnxBsxChargeGrpRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxChargeGrpRowLastCh.setStatus("current")
_TmnxBsxChargeGrpDescription_Type = TItemDescription
_TmnxBsxChargeGrpDescription_Object = MibTableColumn
tmnxBsxChargeGrpDescription = _TmnxBsxChargeGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 23, 1, 5),
    _TmnxBsxChargeGrpDescription_Type()
)
tmnxBsxChargeGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxChargeGrpDescription.setStatus("current")


class _TmnxBsxChargeGrpExportId_Type(Unsigned32):
    """Custom type tmnxBsxChargeGrpExportId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxBsxChargeGrpExportId_Type.__name__ = "Unsigned32"
_TmnxBsxChargeGrpExportId_Object = MibTableColumn
tmnxBsxChargeGrpExportId = _TmnxBsxChargeGrpExportId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 23, 1, 6),
    _TmnxBsxChargeGrpExportId_Type()
)
tmnxBsxChargeGrpExportId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxChargeGrpExportId.setStatus("current")
_TmnxBsxPlcyCfgTable_Object = MibTable
tmnxBsxPlcyCfgTable = _TmnxBsxPlcyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 24)
)
if mibBuilder.loadTexts:
    tmnxBsxPlcyCfgTable.setStatus("current")
_TmnxBsxPlcyCfgEntry_Object = MibTableRow
tmnxBsxPlcyCfgEntry = _TmnxBsxPlcyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 24, 1)
)
tmnxBsxPlcyCfgEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxPlcyPolicyVersion"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxPlcyCfgEntry.setStatus("current")
_TmnxBsxPlcyPolicyVersion_Type = TmnxBsxPolicyVersion
_TmnxBsxPlcyPolicyVersion_Object = MibTableColumn
tmnxBsxPlcyPolicyVersion = _TmnxBsxPlcyPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 24, 1, 1),
    _TmnxBsxPlcyPolicyVersion_Type()
)
tmnxBsxPlcyPolicyVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxPlcyPolicyVersion.setStatus("current")
_TmnxBsxPlcyRowLastCh_Type = TimeStamp
_TmnxBsxPlcyRowLastCh_Object = MibTableColumn
tmnxBsxPlcyRowLastCh = _TmnxBsxPlcyRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 24, 1, 2),
    _TmnxBsxPlcyRowLastCh_Type()
)
tmnxBsxPlcyRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxPlcyRowLastCh.setStatus("current")
_TmnxBsxPlcyDefChargeGrp_Type = TNamedItemOrEmpty
_TmnxBsxPlcyDefChargeGrp_Object = MibTableColumn
tmnxBsxPlcyDefChargeGrp = _TmnxBsxPlcyDefChargeGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 2, 24, 1, 3),
    _TmnxBsxPlcyDefChargeGrp_Type()
)
tmnxBsxPlcyDefChargeGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxPlcyDefChargeGrp.setStatus("current")
_TmnxBsxStatsObjs_ObjectIdentity = ObjectIdentity
tmnxBsxStatsObjs = _TmnxBsxStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3)
)
_TmnxBsxStatsAccounting_ObjectIdentity = ObjectIdentity
tmnxBsxStatsAccounting = _TmnxBsxStatsAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 1)
)
_TmnxBsxStatAaAcctLastChTime_Type = TimeStamp
_TmnxBsxStatAaAcctLastChTime_Object = MibScalar
tmnxBsxStatAaAcctLastChTime = _TmnxBsxStatAaAcctLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 1, 1),
    _TmnxBsxStatAaAcctLastChTime_Type()
)
tmnxBsxStatAaAcctLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAcctLastChTime.setStatus("current")
_TmnxBsxStatAaSubLastChTime_Type = TimeStamp
_TmnxBsxStatAaSubLastChTime_Object = MibScalar
tmnxBsxStatAaSubLastChTime = _TmnxBsxStatAaSubLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 1, 2),
    _TmnxBsxStatAaSubLastChTime_Type()
)
tmnxBsxStatAaSubLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubLastChTime.setStatus("current")
_TmnxBsxStatAaSubSdyLastChTime_Type = TimeStamp
_TmnxBsxStatAaSubSdyLastChTime_Object = MibScalar
tmnxBsxStatAaSubSdyLastChTime = _TmnxBsxStatAaSubSdyLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 1, 3),
    _TmnxBsxStatAaSubSdyLastChTime_Type()
)
tmnxBsxStatAaSubSdyLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyLastChTime.setStatus("current")
_TmnxBsxStatIsaAaCfgLastChTime_Type = TimeStamp
_TmnxBsxStatIsaAaCfgLastChTime_Object = MibScalar
tmnxBsxStatIsaAaCfgLastChTime = _TmnxBsxStatIsaAaCfgLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 1, 4),
    _TmnxBsxStatIsaAaCfgLastChTime_Type()
)
tmnxBsxStatIsaAaCfgLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatIsaAaCfgLastChTime.setStatus("current")
_TmnxBsxStatAaAcctCfgTable_Object = MibTable
tmnxBsxStatAaAcctCfgTable = _TmnxBsxStatAaAcctCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaAcctCfgTable.setStatus("current")
_TmnxBsxStatAaAcctCfgEntry_Object = MibTableRow
tmnxBsxStatAaAcctCfgEntry = _TmnxBsxStatAaAcctCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 2, 1)
)
tmnxBsxStatAaAcctCfgEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAcctCfgType"),
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaAcctCfgEntry.setStatus("current")
_TmnxBsxStatAaAcctCfgType_Type = TmnxBsxStatAaAcctCfgType
_TmnxBsxStatAaAcctCfgType_Object = MibTableColumn
tmnxBsxStatAaAcctCfgType = _TmnxBsxStatAaAcctCfgType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 2, 1, 1),
    _TmnxBsxStatAaAcctCfgType_Type()
)
tmnxBsxStatAaAcctCfgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAcctCfgType.setStatus("current")


class _TmnxBsxStatAaAcctCfgCollStats_Type(TruthValue):
    """Custom type tmnxBsxStatAaAcctCfgCollStats based on TruthValue"""


_TmnxBsxStatAaAcctCfgCollStats_Object = MibTableColumn
tmnxBsxStatAaAcctCfgCollStats = _TmnxBsxStatAaAcctCfgCollStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 2, 1, 2),
    _TmnxBsxStatAaAcctCfgCollStats_Type()
)
tmnxBsxStatAaAcctCfgCollStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAcctCfgCollStats.setStatus("current")


class _TmnxBsxStatAaAcctCfgPolicy_Type(Unsigned32):
    """Custom type tmnxBsxStatAaAcctCfgPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxBsxStatAaAcctCfgPolicy_Type.__name__ = "Unsigned32"
_TmnxBsxStatAaAcctCfgPolicy_Object = MibTableColumn
tmnxBsxStatAaAcctCfgPolicy = _TmnxBsxStatAaAcctCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 2, 1, 3),
    _TmnxBsxStatAaAcctCfgPolicy_Type()
)
tmnxBsxStatAaAcctCfgPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAcctCfgPolicy.setStatus("current")


class _TmnxBsxStatAaAcctCfgAggrStats_Type(TruthValue):
    """Custom type tmnxBsxStatAaAcctCfgAggrStats based on TruthValue"""


_TmnxBsxStatAaAcctCfgAggrStats_Object = MibTableColumn
tmnxBsxStatAaAcctCfgAggrStats = _TmnxBsxStatAaAcctCfgAggrStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 2, 1, 4),
    _TmnxBsxStatAaAcctCfgAggrStats_Type()
)
tmnxBsxStatAaAcctCfgAggrStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAcctCfgAggrStats.setStatus("current")


class _TmnxBsxStatAaAcctCfgAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxStatAaAcctCfgAdminState based on TmnxAdminState"""


_TmnxBsxStatAaAcctCfgAdminState_Object = MibTableColumn
tmnxBsxStatAaAcctCfgAdminState = _TmnxBsxStatAaAcctCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 2, 1, 5),
    _TmnxBsxStatAaAcctCfgAdminState_Type()
)
tmnxBsxStatAaAcctCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAcctCfgAdminState.setStatus("current")


class _TmnxBsxStatAaAcctCfgMaxThruStats_Type(TruthValue):
    """Custom type tmnxBsxStatAaAcctCfgMaxThruStats based on TruthValue"""


_TmnxBsxStatAaAcctCfgMaxThruStats_Object = MibTableColumn
tmnxBsxStatAaAcctCfgMaxThruStats = _TmnxBsxStatAaAcctCfgMaxThruStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 2, 1, 6),
    _TmnxBsxStatAaAcctCfgMaxThruStats_Type()
)
tmnxBsxStatAaAcctCfgMaxThruStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAcctCfgMaxThruStats.setStatus("current")
_TmnxBsxStatAaAcctCfgRadiusPlcy_Type = TNamedItemOrEmpty
_TmnxBsxStatAaAcctCfgRadiusPlcy_Object = MibTableColumn
tmnxBsxStatAaAcctCfgRadiusPlcy = _TmnxBsxStatAaAcctCfgRadiusPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 2, 1, 7),
    _TmnxBsxStatAaAcctCfgRadiusPlcy_Type()
)
tmnxBsxStatAaAcctCfgRadiusPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAcctCfgRadiusPlcy.setStatus("current")
_TmnxBsxStatAaSubTable_Object = MibTable
tmnxBsxStatAaSubTable = _TmnxBsxStatAaSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubTable.setStatus("current")
_TmnxBsxStatAaSubEntry_Object = MibTableRow
tmnxBsxStatAaSubEntry = _TmnxBsxStatAaSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1)
)
tmnxBsxStatAaSubEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubStatsInterval"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriber"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaType"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaName"),
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubEntry.setStatus("current")
_TmnxBsxAaSubscriberType_Type = TmnxBsxAaSubscriberType
_TmnxBsxAaSubscriberType_Object = MibTableColumn
tmnxBsxAaSubscriberType = _TmnxBsxAaSubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 1),
    _TmnxBsxAaSubscriberType_Type()
)
tmnxBsxAaSubscriberType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAaSubscriberType.setStatus("current")
_TmnxBsxAaSubscriber_Type = TmnxBsxAaSubscriber
_TmnxBsxAaSubscriber_Object = MibTableColumn
tmnxBsxAaSubscriber = _TmnxBsxAaSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 2),
    _TmnxBsxAaSubscriber_Type()
)
tmnxBsxAaSubscriber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAaSubscriber.setStatus("current")
_TmnxBsxStatAaType_Type = TmnxBsxAaStatType
_TmnxBsxStatAaType_Object = MibTableColumn
tmnxBsxStatAaType = _TmnxBsxStatAaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 3),
    _TmnxBsxStatAaType_Type()
)
tmnxBsxStatAaType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxStatAaType.setStatus("current")
_TmnxBsxStatAaName_Type = TNamedItem
_TmnxBsxStatAaName_Object = MibTableColumn
tmnxBsxStatAaName = _TmnxBsxStatAaName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 4),
    _TmnxBsxStatAaName_Type()
)
tmnxBsxStatAaName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxStatAaName.setStatus("current")
_TmnxBsxStatAaSubDiscontTime_Type = TimeStamp
_TmnxBsxStatAaSubDiscontTime_Object = MibTableColumn
tmnxBsxStatAaSubDiscontTime = _TmnxBsxStatAaSubDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 5),
    _TmnxBsxStatAaSubDiscontTime_Type()
)
tmnxBsxStatAaSubDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubDiscontTime.setStatus("current")
_TmnxBsxStatAaSubOctsAdmFmSb_Type = Counter32
_TmnxBsxStatAaSubOctsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubOctsAdmFmSb = _TmnxBsxStatAaSubOctsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 6),
    _TmnxBsxStatAaSubOctsAdmFmSb_Type()
)
tmnxBsxStatAaSubOctsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubOctsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubOctsAdmFmSb.setUnits("bytes")
_TmnxBsxStatAaSubPktsAdmFmSb_Type = Counter32
_TmnxBsxStatAaSubPktsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubPktsAdmFmSb = _TmnxBsxStatAaSubPktsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 7),
    _TmnxBsxStatAaSubPktsAdmFmSb_Type()
)
tmnxBsxStatAaSubPktsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubPktsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubPktsAdmFmSb.setUnits("packets")
_TmnxBsxStatAaSubFlwsAdmFmSb_Type = Counter32
_TmnxBsxStatAaSubFlwsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubFlwsAdmFmSb = _TmnxBsxStatAaSubFlwsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 8),
    _TmnxBsxStatAaSubFlwsAdmFmSb_Type()
)
tmnxBsxStatAaSubFlwsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubFlwsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubFlwsAdmFmSb.setUnits("flows")
_TmnxBsxStatAaSubOctsDnyFmSb_Type = Counter32
_TmnxBsxStatAaSubOctsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubOctsDnyFmSb = _TmnxBsxStatAaSubOctsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 9),
    _TmnxBsxStatAaSubOctsDnyFmSb_Type()
)
tmnxBsxStatAaSubOctsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubOctsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubOctsDnyFmSb.setUnits("bytes")
_TmnxBsxStatAaSubPktsDnyFmSb_Type = Counter32
_TmnxBsxStatAaSubPktsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubPktsDnyFmSb = _TmnxBsxStatAaSubPktsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 10),
    _TmnxBsxStatAaSubPktsDnyFmSb_Type()
)
tmnxBsxStatAaSubPktsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubPktsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubPktsDnyFmSb.setUnits("packets")
_TmnxBsxStatAaSubFlwsDnyFmSb_Type = Counter32
_TmnxBsxStatAaSubFlwsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubFlwsDnyFmSb = _TmnxBsxStatAaSubFlwsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 11),
    _TmnxBsxStatAaSubFlwsDnyFmSb_Type()
)
tmnxBsxStatAaSubFlwsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubFlwsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubFlwsDnyFmSb.setUnits("flows")
_TmnxBsxStatAaSubOctsAdmToSb_Type = Counter32
_TmnxBsxStatAaSubOctsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubOctsAdmToSb = _TmnxBsxStatAaSubOctsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 12),
    _TmnxBsxStatAaSubOctsAdmToSb_Type()
)
tmnxBsxStatAaSubOctsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubOctsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubOctsAdmToSb.setUnits("bytes")
_TmnxBsxStatAaSubPktsAdmToSb_Type = Counter32
_TmnxBsxStatAaSubPktsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubPktsAdmToSb = _TmnxBsxStatAaSubPktsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 13),
    _TmnxBsxStatAaSubPktsAdmToSb_Type()
)
tmnxBsxStatAaSubPktsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubPktsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubPktsAdmToSb.setUnits("packets")
_TmnxBsxStatAaSubFlwsAdmToSb_Type = Counter32
_TmnxBsxStatAaSubFlwsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubFlwsAdmToSb = _TmnxBsxStatAaSubFlwsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 14),
    _TmnxBsxStatAaSubFlwsAdmToSb_Type()
)
tmnxBsxStatAaSubFlwsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubFlwsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubFlwsAdmToSb.setUnits("flows")
_TmnxBsxStatAaSubOctsDnyToSb_Type = Counter32
_TmnxBsxStatAaSubOctsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubOctsDnyToSb = _TmnxBsxStatAaSubOctsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 15),
    _TmnxBsxStatAaSubOctsDnyToSb_Type()
)
tmnxBsxStatAaSubOctsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubOctsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubOctsDnyToSb.setUnits("bytes")
_TmnxBsxStatAaSubPktsDnyToSb_Type = Counter32
_TmnxBsxStatAaSubPktsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubPktsDnyToSb = _TmnxBsxStatAaSubPktsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 16),
    _TmnxBsxStatAaSubPktsDnyToSb_Type()
)
tmnxBsxStatAaSubPktsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubPktsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubPktsDnyToSb.setUnits("packets")
_TmnxBsxStatAaSubFlwsDnyToSb_Type = Counter32
_TmnxBsxStatAaSubFlwsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubFlwsDnyToSb = _TmnxBsxStatAaSubFlwsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 17),
    _TmnxBsxStatAaSubFlwsDnyToSb_Type()
)
tmnxBsxStatAaSubFlwsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubFlwsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubFlwsDnyToSb.setUnits("flows")
_TmnxBsxStatAaSubTermFlwDur_Type = Counter32
_TmnxBsxStatAaSubTermFlwDur_Object = MibTableColumn
tmnxBsxStatAaSubTermFlwDur = _TmnxBsxStatAaSubTermFlwDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 18),
    _TmnxBsxStatAaSubTermFlwDur_Type()
)
tmnxBsxStatAaSubTermFlwDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubTermFlwDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubTermFlwDur.setUnits("seconds")
_TmnxBsxStatAaSubTermFlws_Type = Counter32
_TmnxBsxStatAaSubTermFlws_Object = MibTableColumn
tmnxBsxStatAaSubTermFlws = _TmnxBsxStatAaSubTermFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 19),
    _TmnxBsxStatAaSubTermFlws_Type()
)
tmnxBsxStatAaSubTermFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubTermFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubTermFlws.setUnits("flows")
_TmnxBsxStatAaSubShrtDurFlws_Type = Counter32
_TmnxBsxStatAaSubShrtDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubShrtDurFlws = _TmnxBsxStatAaSubShrtDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 20),
    _TmnxBsxStatAaSubShrtDurFlws_Type()
)
tmnxBsxStatAaSubShrtDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubShrtDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubShrtDurFlws.setUnits("flows")
_TmnxBsxStatAaSubMedDurFlws_Type = Counter32
_TmnxBsxStatAaSubMedDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubMedDurFlws = _TmnxBsxStatAaSubMedDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 21),
    _TmnxBsxStatAaSubMedDurFlws_Type()
)
tmnxBsxStatAaSubMedDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubMedDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubMedDurFlws.setUnits("flows")
_TmnxBsxStatAaSubLngDurFlws_Type = Counter32
_TmnxBsxStatAaSubLngDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubLngDurFlws = _TmnxBsxStatAaSubLngDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 22),
    _TmnxBsxStatAaSubLngDurFlws_Type()
)
tmnxBsxStatAaSubLngDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubLngDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubLngDurFlws.setUnits("flows")
_TmnxBsxStatAaSubActFlwsFmSb_Type = Gauge32
_TmnxBsxStatAaSubActFlwsFmSb_Object = MibTableColumn
tmnxBsxStatAaSubActFlwsFmSb = _TmnxBsxStatAaSubActFlwsFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 23),
    _TmnxBsxStatAaSubActFlwsFmSb_Type()
)
tmnxBsxStatAaSubActFlwsFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubActFlwsFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubActFlwsFmSb.setUnits("flows")
_TmnxBsxStatAaSubActFlwsToSb_Type = Gauge32
_TmnxBsxStatAaSubActFlwsToSb_Object = MibTableColumn
tmnxBsxStatAaSubActFlwsToSb = _TmnxBsxStatAaSubActFlwsToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 24),
    _TmnxBsxStatAaSubActFlwsToSb_Type()
)
tmnxBsxStatAaSubActFlwsToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubActFlwsToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubActFlwsToSb.setUnits("flows")
_TmnxBsxStatAaSubHCOctsAdmFmSb_Type = Counter64
_TmnxBsxStatAaSubHCOctsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubHCOctsAdmFmSb = _TmnxBsxStatAaSubHCOctsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 25),
    _TmnxBsxStatAaSubHCOctsAdmFmSb_Type()
)
tmnxBsxStatAaSubHCOctsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCOctsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCOctsAdmFmSb.setUnits("bytes")
_TmnxBsxStatAaSubHCPktsAdmFmSb_Type = Counter64
_TmnxBsxStatAaSubHCPktsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubHCPktsAdmFmSb = _TmnxBsxStatAaSubHCPktsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 26),
    _TmnxBsxStatAaSubHCPktsAdmFmSb_Type()
)
tmnxBsxStatAaSubHCPktsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCPktsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCPktsAdmFmSb.setUnits("packets")
_TmnxBsxStatAaSubHCFlwsAdmFmSb_Type = Counter64
_TmnxBsxStatAaSubHCFlwsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubHCFlwsAdmFmSb = _TmnxBsxStatAaSubHCFlwsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 27),
    _TmnxBsxStatAaSubHCFlwsAdmFmSb_Type()
)
tmnxBsxStatAaSubHCFlwsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCFlwsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCFlwsAdmFmSb.setUnits("flows")
_TmnxBsxStatAaSubHCOctsDnyFmSb_Type = Counter64
_TmnxBsxStatAaSubHCOctsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubHCOctsDnyFmSb = _TmnxBsxStatAaSubHCOctsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 28),
    _TmnxBsxStatAaSubHCOctsDnyFmSb_Type()
)
tmnxBsxStatAaSubHCOctsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCOctsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCOctsDnyFmSb.setUnits("bytes")
_TmnxBsxStatAaSubHCPktsDnyFmSb_Type = Counter64
_TmnxBsxStatAaSubHCPktsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubHCPktsDnyFmSb = _TmnxBsxStatAaSubHCPktsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 29),
    _TmnxBsxStatAaSubHCPktsDnyFmSb_Type()
)
tmnxBsxStatAaSubHCPktsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCPktsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCPktsDnyFmSb.setUnits("packets")
_TmnxBsxStatAaSubHCFlwsDnyFmSb_Type = Counter64
_TmnxBsxStatAaSubHCFlwsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubHCFlwsDnyFmSb = _TmnxBsxStatAaSubHCFlwsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 30),
    _TmnxBsxStatAaSubHCFlwsDnyFmSb_Type()
)
tmnxBsxStatAaSubHCFlwsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCFlwsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCFlwsDnyFmSb.setUnits("flows")
_TmnxBsxStatAaSubHCOctsAdmToSb_Type = Counter64
_TmnxBsxStatAaSubHCOctsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubHCOctsAdmToSb = _TmnxBsxStatAaSubHCOctsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 31),
    _TmnxBsxStatAaSubHCOctsAdmToSb_Type()
)
tmnxBsxStatAaSubHCOctsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCOctsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCOctsAdmToSb.setUnits("bytes")
_TmnxBsxStatAaSubHCPktsAdmToSb_Type = Counter64
_TmnxBsxStatAaSubHCPktsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubHCPktsAdmToSb = _TmnxBsxStatAaSubHCPktsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 32),
    _TmnxBsxStatAaSubHCPktsAdmToSb_Type()
)
tmnxBsxStatAaSubHCPktsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCPktsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCPktsAdmToSb.setUnits("packets")
_TmnxBsxStatAaSubHCFlwsAdmToSb_Type = Counter64
_TmnxBsxStatAaSubHCFlwsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubHCFlwsAdmToSb = _TmnxBsxStatAaSubHCFlwsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 33),
    _TmnxBsxStatAaSubHCFlwsAdmToSb_Type()
)
tmnxBsxStatAaSubHCFlwsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCFlwsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCFlwsAdmToSb.setUnits("flows")
_TmnxBsxStatAaSubHCOctsDnyToSb_Type = Counter64
_TmnxBsxStatAaSubHCOctsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubHCOctsDnyToSb = _TmnxBsxStatAaSubHCOctsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 34),
    _TmnxBsxStatAaSubHCOctsDnyToSb_Type()
)
tmnxBsxStatAaSubHCOctsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCOctsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCOctsDnyToSb.setUnits("bytes")
_TmnxBsxStatAaSubHCPktsDnyToSb_Type = Counter64
_TmnxBsxStatAaSubHCPktsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubHCPktsDnyToSb = _TmnxBsxStatAaSubHCPktsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 35),
    _TmnxBsxStatAaSubHCPktsDnyToSb_Type()
)
tmnxBsxStatAaSubHCPktsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCPktsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCPktsDnyToSb.setUnits("packets")
_TmnxBsxStatAaSubHCFlwsDnyToSb_Type = Counter64
_TmnxBsxStatAaSubHCFlwsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubHCFlwsDnyToSb = _TmnxBsxStatAaSubHCFlwsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 36),
    _TmnxBsxStatAaSubHCFlwsDnyToSb_Type()
)
tmnxBsxStatAaSubHCFlwsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCFlwsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCFlwsDnyToSb.setUnits("flows")
_TmnxBsxStatAaSubHCTermFlwDur_Type = Counter64
_TmnxBsxStatAaSubHCTermFlwDur_Object = MibTableColumn
tmnxBsxStatAaSubHCTermFlwDur = _TmnxBsxStatAaSubHCTermFlwDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 37),
    _TmnxBsxStatAaSubHCTermFlwDur_Type()
)
tmnxBsxStatAaSubHCTermFlwDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCTermFlwDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCTermFlwDur.setUnits("seconds")
_TmnxBsxStatAaSubHCTermFlws_Type = Counter64
_TmnxBsxStatAaSubHCTermFlws_Object = MibTableColumn
tmnxBsxStatAaSubHCTermFlws = _TmnxBsxStatAaSubHCTermFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 38),
    _TmnxBsxStatAaSubHCTermFlws_Type()
)
tmnxBsxStatAaSubHCTermFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCTermFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCTermFlws.setUnits("flows")
_TmnxBsxStatAaSubHCShrtDurFlws_Type = Counter64
_TmnxBsxStatAaSubHCShrtDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubHCShrtDurFlws = _TmnxBsxStatAaSubHCShrtDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 39),
    _TmnxBsxStatAaSubHCShrtDurFlws_Type()
)
tmnxBsxStatAaSubHCShrtDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCShrtDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCShrtDurFlws.setUnits("flows")
_TmnxBsxStatAaSubHCMedDurFlws_Type = Counter64
_TmnxBsxStatAaSubHCMedDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubHCMedDurFlws = _TmnxBsxStatAaSubHCMedDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 40),
    _TmnxBsxStatAaSubHCMedDurFlws_Type()
)
tmnxBsxStatAaSubHCMedDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCMedDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCMedDurFlws.setUnits("flows")
_TmnxBsxStatAaSubHCLngDurFlws_Type = Counter64
_TmnxBsxStatAaSubHCLngDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubHCLngDurFlws = _TmnxBsxStatAaSubHCLngDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 3, 1, 41),
    _TmnxBsxStatAaSubHCLngDurFlws_Type()
)
tmnxBsxStatAaSubHCLngDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCLngDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubHCLngDurFlws.setUnits("flows")
_TmnxBsxStatAaSubSdyTable_Object = MibTable
tmnxBsxStatAaSubSdyTable = _TmnxBsxStatAaSubSdyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyTable.setStatus("current")
_TmnxBsxStatAaSubSdyEntry_Object = MibTableRow
tmnxBsxStatAaSubSdyEntry = _TmnxBsxStatAaSubSdyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1)
)
tmnxBsxStatAaSubSdyEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubStatsInterval"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriber"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaName"),
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyEntry.setStatus("current")
_TmnxBsxStatAaSubSdyDiscontTime_Type = TimeStamp
_TmnxBsxStatAaSubSdyDiscontTime_Object = MibTableColumn
tmnxBsxStatAaSubSdyDiscontTime = _TmnxBsxStatAaSubSdyDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 1),
    _TmnxBsxStatAaSubSdyDiscontTime_Type()
)
tmnxBsxStatAaSubSdyDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyDiscontTime.setStatus("current")
_TmnxBsxStatAaSubSdyOctsAdmFmSb_Type = Counter32
_TmnxBsxStatAaSubSdyOctsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyOctsAdmFmSb = _TmnxBsxStatAaSubSdyOctsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 2),
    _TmnxBsxStatAaSubSdyOctsAdmFmSb_Type()
)
tmnxBsxStatAaSubSdyOctsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyOctsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyOctsAdmFmSb.setUnits("bytes")
_TmnxBsxStatAaSubSdyPktsAdmFmSb_Type = Counter32
_TmnxBsxStatAaSubSdyPktsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyPktsAdmFmSb = _TmnxBsxStatAaSubSdyPktsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 3),
    _TmnxBsxStatAaSubSdyPktsAdmFmSb_Type()
)
tmnxBsxStatAaSubSdyPktsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyPktsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyPktsAdmFmSb.setUnits("packets")
_TmnxBsxStatAaSubSdyFlwsAdmFmSb_Type = Counter32
_TmnxBsxStatAaSubSdyFlwsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyFlwsAdmFmSb = _TmnxBsxStatAaSubSdyFlwsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 4),
    _TmnxBsxStatAaSubSdyFlwsAdmFmSb_Type()
)
tmnxBsxStatAaSubSdyFlwsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyFlwsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyFlwsAdmFmSb.setUnits("flows")
_TmnxBsxStatAaSubSdyOctsDnyFmSb_Type = Counter32
_TmnxBsxStatAaSubSdyOctsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyOctsDnyFmSb = _TmnxBsxStatAaSubSdyOctsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 5),
    _TmnxBsxStatAaSubSdyOctsDnyFmSb_Type()
)
tmnxBsxStatAaSubSdyOctsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyOctsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyOctsDnyFmSb.setUnits("bytes")
_TmnxBsxStatAaSubSdyPktsDnyFmSb_Type = Counter32
_TmnxBsxStatAaSubSdyPktsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyPktsDnyFmSb = _TmnxBsxStatAaSubSdyPktsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 6),
    _TmnxBsxStatAaSubSdyPktsDnyFmSb_Type()
)
tmnxBsxStatAaSubSdyPktsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyPktsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyPktsDnyFmSb.setUnits("packets")
_TmnxBsxStatAaSubSdyFlwsDnyFmSb_Type = Counter32
_TmnxBsxStatAaSubSdyFlwsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyFlwsDnyFmSb = _TmnxBsxStatAaSubSdyFlwsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 7),
    _TmnxBsxStatAaSubSdyFlwsDnyFmSb_Type()
)
tmnxBsxStatAaSubSdyFlwsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyFlwsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyFlwsDnyFmSb.setUnits("flows")
_TmnxBsxStatAaSubSdyOctsAdmToSb_Type = Counter32
_TmnxBsxStatAaSubSdyOctsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyOctsAdmToSb = _TmnxBsxStatAaSubSdyOctsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 8),
    _TmnxBsxStatAaSubSdyOctsAdmToSb_Type()
)
tmnxBsxStatAaSubSdyOctsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyOctsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyOctsAdmToSb.setUnits("bytes")
_TmnxBsxStatAaSubSdyPktsAdmToSb_Type = Counter32
_TmnxBsxStatAaSubSdyPktsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyPktsAdmToSb = _TmnxBsxStatAaSubSdyPktsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 9),
    _TmnxBsxStatAaSubSdyPktsAdmToSb_Type()
)
tmnxBsxStatAaSubSdyPktsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyPktsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyPktsAdmToSb.setUnits("packets")
_TmnxBsxStatAaSubSdyFlwsAdmToSb_Type = Counter32
_TmnxBsxStatAaSubSdyFlwsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyFlwsAdmToSb = _TmnxBsxStatAaSubSdyFlwsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 10),
    _TmnxBsxStatAaSubSdyFlwsAdmToSb_Type()
)
tmnxBsxStatAaSubSdyFlwsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyFlwsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyFlwsAdmToSb.setUnits("flows")
_TmnxBsxStatAaSubSdyOctsDnyToSb_Type = Counter32
_TmnxBsxStatAaSubSdyOctsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyOctsDnyToSb = _TmnxBsxStatAaSubSdyOctsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 11),
    _TmnxBsxStatAaSubSdyOctsDnyToSb_Type()
)
tmnxBsxStatAaSubSdyOctsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyOctsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyOctsDnyToSb.setUnits("bytes")
_TmnxBsxStatAaSubSdyPktsDnyToSb_Type = Counter32
_TmnxBsxStatAaSubSdyPktsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyPktsDnyToSb = _TmnxBsxStatAaSubSdyPktsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 12),
    _TmnxBsxStatAaSubSdyPktsDnyToSb_Type()
)
tmnxBsxStatAaSubSdyPktsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyPktsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyPktsDnyToSb.setUnits("packets")
_TmnxBsxStatAaSubSdyFlwsDnyToSb_Type = Counter32
_TmnxBsxStatAaSubSdyFlwsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyFlwsDnyToSb = _TmnxBsxStatAaSubSdyFlwsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 13),
    _TmnxBsxStatAaSubSdyFlwsDnyToSb_Type()
)
tmnxBsxStatAaSubSdyFlwsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyFlwsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyFlwsDnyToSb.setUnits("flows")
_TmnxBsxStatAaSubSdyTermFlwDur_Type = Counter32
_TmnxBsxStatAaSubSdyTermFlwDur_Object = MibTableColumn
tmnxBsxStatAaSubSdyTermFlwDur = _TmnxBsxStatAaSubSdyTermFlwDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 14),
    _TmnxBsxStatAaSubSdyTermFlwDur_Type()
)
tmnxBsxStatAaSubSdyTermFlwDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyTermFlwDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyTermFlwDur.setUnits("seconds")
_TmnxBsxStatAaSubSdyTermFlws_Type = Counter32
_TmnxBsxStatAaSubSdyTermFlws_Object = MibTableColumn
tmnxBsxStatAaSubSdyTermFlws = _TmnxBsxStatAaSubSdyTermFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 15),
    _TmnxBsxStatAaSubSdyTermFlws_Type()
)
tmnxBsxStatAaSubSdyTermFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyTermFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyTermFlws.setUnits("flows")
_TmnxBsxStatAaSubSdyShrtDurFlws_Type = Counter32
_TmnxBsxStatAaSubSdyShrtDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubSdyShrtDurFlws = _TmnxBsxStatAaSubSdyShrtDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 16),
    _TmnxBsxStatAaSubSdyShrtDurFlws_Type()
)
tmnxBsxStatAaSubSdyShrtDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyShrtDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyShrtDurFlws.setUnits("flows")
_TmnxBsxStatAaSubSdyMedDurFlws_Type = Counter32
_TmnxBsxStatAaSubSdyMedDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubSdyMedDurFlws = _TmnxBsxStatAaSubSdyMedDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 17),
    _TmnxBsxStatAaSubSdyMedDurFlws_Type()
)
tmnxBsxStatAaSubSdyMedDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyMedDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyMedDurFlws.setUnits("flows")
_TmnxBsxStatAaSubSdyLngDurFlws_Type = Counter32
_TmnxBsxStatAaSubSdyLngDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubSdyLngDurFlws = _TmnxBsxStatAaSubSdyLngDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 18),
    _TmnxBsxStatAaSubSdyLngDurFlws_Type()
)
tmnxBsxStatAaSubSdyLngDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyLngDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyLngDurFlws.setUnits("flows")
_TmnxBsxStatAaSubSdyActFlwsFmSb_Type = Gauge32
_TmnxBsxStatAaSubSdyActFlwsFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyActFlwsFmSb = _TmnxBsxStatAaSubSdyActFlwsFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 19),
    _TmnxBsxStatAaSubSdyActFlwsFmSb_Type()
)
tmnxBsxStatAaSubSdyActFlwsFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyActFlwsFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyActFlwsFmSb.setUnits("flows")
_TmnxBsxStatAaSubSdyActFlwsToSb_Type = Gauge32
_TmnxBsxStatAaSubSdyActFlwsToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyActFlwsToSb = _TmnxBsxStatAaSubSdyActFlwsToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 20),
    _TmnxBsxStatAaSubSdyActFlwsToSb_Type()
)
tmnxBsxStatAaSubSdyActFlwsToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyActFlwsToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyActFlwsToSb.setUnits("flows")
_TmnxBsxStatAaSubSdyHCOctsAdmFmSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCOctsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCOctsAdmFmSb = _TmnxBsxStatAaSubSdyHCOctsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 21),
    _TmnxBsxStatAaSubSdyHCOctsAdmFmSb_Type()
)
tmnxBsxStatAaSubSdyHCOctsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCOctsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCOctsAdmFmSb.setUnits("bytes")
_TmnxBsxStatAaSubSdyHCPktsAdmFmSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCPktsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCPktsAdmFmSb = _TmnxBsxStatAaSubSdyHCPktsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 22),
    _TmnxBsxStatAaSubSdyHCPktsAdmFmSb_Type()
)
tmnxBsxStatAaSubSdyHCPktsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCPktsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCPktsAdmFmSb.setUnits("packets")
_TmnxBsxStatAaSubSdyHCFlwsAdmFmSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCFlwsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCFlwsAdmFmSb = _TmnxBsxStatAaSubSdyHCFlwsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 23),
    _TmnxBsxStatAaSubSdyHCFlwsAdmFmSb_Type()
)
tmnxBsxStatAaSubSdyHCFlwsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCFlwsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCFlwsAdmFmSb.setUnits("flows")
_TmnxBsxStatAaSubSdyHCOctsDnyFmSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCOctsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCOctsDnyFmSb = _TmnxBsxStatAaSubSdyHCOctsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 24),
    _TmnxBsxStatAaSubSdyHCOctsDnyFmSb_Type()
)
tmnxBsxStatAaSubSdyHCOctsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCOctsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCOctsDnyFmSb.setUnits("bytes")
_TmnxBsxStatAaSubSdyHCPktsDnyFmSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCPktsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCPktsDnyFmSb = _TmnxBsxStatAaSubSdyHCPktsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 25),
    _TmnxBsxStatAaSubSdyHCPktsDnyFmSb_Type()
)
tmnxBsxStatAaSubSdyHCPktsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCPktsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCPktsDnyFmSb.setUnits("packets")
_TmnxBsxStatAaSubSdyHCFlwsDnyFmSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCFlwsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCFlwsDnyFmSb = _TmnxBsxStatAaSubSdyHCFlwsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 26),
    _TmnxBsxStatAaSubSdyHCFlwsDnyFmSb_Type()
)
tmnxBsxStatAaSubSdyHCFlwsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCFlwsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCFlwsDnyFmSb.setUnits("flows")
_TmnxBsxStatAaSubSdyHCOctsAdmToSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCOctsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCOctsAdmToSb = _TmnxBsxStatAaSubSdyHCOctsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 27),
    _TmnxBsxStatAaSubSdyHCOctsAdmToSb_Type()
)
tmnxBsxStatAaSubSdyHCOctsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCOctsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCOctsAdmToSb.setUnits("bytes")
_TmnxBsxStatAaSubSdyHCPktsAdmToSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCPktsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCPktsAdmToSb = _TmnxBsxStatAaSubSdyHCPktsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 28),
    _TmnxBsxStatAaSubSdyHCPktsAdmToSb_Type()
)
tmnxBsxStatAaSubSdyHCPktsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCPktsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCPktsAdmToSb.setUnits("packets")
_TmnxBsxStatAaSubSdyHCFlwsAdmToSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCFlwsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCFlwsAdmToSb = _TmnxBsxStatAaSubSdyHCFlwsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 29),
    _TmnxBsxStatAaSubSdyHCFlwsAdmToSb_Type()
)
tmnxBsxStatAaSubSdyHCFlwsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCFlwsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCFlwsAdmToSb.setUnits("flows")
_TmnxBsxStatAaSubSdyHCOctsDnyToSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCOctsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCOctsDnyToSb = _TmnxBsxStatAaSubSdyHCOctsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 30),
    _TmnxBsxStatAaSubSdyHCOctsDnyToSb_Type()
)
tmnxBsxStatAaSubSdyHCOctsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCOctsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCOctsDnyToSb.setUnits("bytes")
_TmnxBsxStatAaSubSdyHCPktsDnyToSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCPktsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCPktsDnyToSb = _TmnxBsxStatAaSubSdyHCPktsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 31),
    _TmnxBsxStatAaSubSdyHCPktsDnyToSb_Type()
)
tmnxBsxStatAaSubSdyHCPktsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCPktsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCPktsDnyToSb.setUnits("packets")
_TmnxBsxStatAaSubSdyHCFlwsDnyToSb_Type = Counter64
_TmnxBsxStatAaSubSdyHCFlwsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCFlwsDnyToSb = _TmnxBsxStatAaSubSdyHCFlwsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 32),
    _TmnxBsxStatAaSubSdyHCFlwsDnyToSb_Type()
)
tmnxBsxStatAaSubSdyHCFlwsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCFlwsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCFlwsDnyToSb.setUnits("flows")
_TmnxBsxStatAaSubSdyHCTermFlwDur_Type = Counter64
_TmnxBsxStatAaSubSdyHCTermFlwDur_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCTermFlwDur = _TmnxBsxStatAaSubSdyHCTermFlwDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 33),
    _TmnxBsxStatAaSubSdyHCTermFlwDur_Type()
)
tmnxBsxStatAaSubSdyHCTermFlwDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCTermFlwDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCTermFlwDur.setUnits("seconds")
_TmnxBsxStatAaSubSdyHCTermFlws_Type = Counter64
_TmnxBsxStatAaSubSdyHCTermFlws_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCTermFlws = _TmnxBsxStatAaSubSdyHCTermFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 34),
    _TmnxBsxStatAaSubSdyHCTermFlws_Type()
)
tmnxBsxStatAaSubSdyHCTermFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCTermFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCTermFlws.setUnits("flows")
_TmnxBsxStatAaSubSdyHCShrtDurFlws_Type = Counter64
_TmnxBsxStatAaSubSdyHCShrtDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCShrtDurFlws = _TmnxBsxStatAaSubSdyHCShrtDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 35),
    _TmnxBsxStatAaSubSdyHCShrtDurFlws_Type()
)
tmnxBsxStatAaSubSdyHCShrtDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCShrtDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCShrtDurFlws.setUnits("flows")
_TmnxBsxStatAaSubSdyHCMedDurFlws_Type = Counter64
_TmnxBsxStatAaSubSdyHCMedDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCMedDurFlws = _TmnxBsxStatAaSubSdyHCMedDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 36),
    _TmnxBsxStatAaSubSdyHCMedDurFlws_Type()
)
tmnxBsxStatAaSubSdyHCMedDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCMedDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCMedDurFlws.setUnits("flows")
_TmnxBsxStatAaSubSdyHCLngDurFlws_Type = Counter64
_TmnxBsxStatAaSubSdyHCLngDurFlws_Object = MibTableColumn
tmnxBsxStatAaSubSdyHCLngDurFlws = _TmnxBsxStatAaSubSdyHCLngDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 4, 1, 37),
    _TmnxBsxStatAaSubSdyHCLngDurFlws_Type()
)
tmnxBsxStatAaSubSdyHCLngDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCLngDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyHCLngDurFlws.setUnits("flows")
_TmnxBsxStatAaSubCfgTable_Object = MibTable
tmnxBsxStatAaSubCfgTable = _TmnxBsxStatAaSubCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubCfgTable.setStatus("current")
_TmnxBsxStatAaSubCfgEntry_Object = MibTableRow
tmnxBsxStatAaSubCfgEntry = _TmnxBsxStatAaSubCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 5, 1)
)
tmnxBsxStatAaSubCfgEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaType"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaName"),
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubCfgEntry.setStatus("current")
_TmnxBsxStatAaSubCfgRowStatus_Type = RowStatus
_TmnxBsxStatAaSubCfgRowStatus_Object = MibTableColumn
tmnxBsxStatAaSubCfgRowStatus = _TmnxBsxStatAaSubCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 5, 1, 1),
    _TmnxBsxStatAaSubCfgRowStatus_Type()
)
tmnxBsxStatAaSubCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubCfgRowStatus.setStatus("current")
_TmnxBsxStatAaSubCfgExportMethod_Type = TmnxBsxAaStatExportMethod
_TmnxBsxStatAaSubCfgExportMethod_Object = MibTableColumn
tmnxBsxStatAaSubCfgExportMethod = _TmnxBsxStatAaSubCfgExportMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 5, 1, 2),
    _TmnxBsxStatAaSubCfgExportMethod_Type()
)
tmnxBsxStatAaSubCfgExportMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubCfgExportMethod.setStatus("current")
_TmnxBsxStatAaSubSdyCfgTable_Object = MibTable
tmnxBsxStatAaSubSdyCfgTable = _TmnxBsxStatAaSubSdyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyCfgTable.setStatus("current")
_TmnxBsxStatAaSubSdyCfgEntry_Object = MibTableRow
tmnxBsxStatAaSubSdyCfgEntry = _TmnxBsxStatAaSubSdyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 6, 1)
)
tmnxBsxStatAaSubSdyCfgEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriber"),
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyCfgEntry.setStatus("current")
_TmnxBsxStatAaSubSdyRowStatus_Type = RowStatus
_TmnxBsxStatAaSubSdyRowStatus_Object = MibTableColumn
tmnxBsxStatAaSubSdyRowStatus = _TmnxBsxStatAaSubSdyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 6, 1, 1),
    _TmnxBsxStatAaSubSdyRowStatus_Type()
)
tmnxBsxStatAaSubSdyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxStatAaSubSdyRowStatus.setStatus("current")
_TmnxBsxStatAaTable_Object = MibTable
tmnxBsxStatAaTable = _TmnxBsxStatAaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaTable.setStatus("current")
_TmnxBsxStatAaEntry_Object = MibTableRow
tmnxBsxStatAaEntry = _TmnxBsxStatAaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1)
)
tmnxBsxStatAaEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaType"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaName"),
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaEntry.setStatus("current")
_TmnxBsxStatAaDiscontTime_Type = TimeStamp
_TmnxBsxStatAaDiscontTime_Object = MibTableColumn
tmnxBsxStatAaDiscontTime = _TmnxBsxStatAaDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 1),
    _TmnxBsxStatAaDiscontTime_Type()
)
tmnxBsxStatAaDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaDiscontTime.setStatus("current")
_TmnxBsxStatAaOctsAdmFmSb_Type = Counter32
_TmnxBsxStatAaOctsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaOctsAdmFmSb = _TmnxBsxStatAaOctsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 2),
    _TmnxBsxStatAaOctsAdmFmSb_Type()
)
tmnxBsxStatAaOctsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaOctsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaOctsAdmFmSb.setUnits("bytes")
_TmnxBsxStatAaPktsAdmFmSb_Type = Counter32
_TmnxBsxStatAaPktsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaPktsAdmFmSb = _TmnxBsxStatAaPktsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 3),
    _TmnxBsxStatAaPktsAdmFmSb_Type()
)
tmnxBsxStatAaPktsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaPktsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaPktsAdmFmSb.setUnits("packets")
_TmnxBsxStatAaFlwsAdmFmSb_Type = Counter32
_TmnxBsxStatAaFlwsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaFlwsAdmFmSb = _TmnxBsxStatAaFlwsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 4),
    _TmnxBsxStatAaFlwsAdmFmSb_Type()
)
tmnxBsxStatAaFlwsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaFlwsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaFlwsAdmFmSb.setUnits("flows")
_TmnxBsxStatAaOctsDnyFmSb_Type = Counter32
_TmnxBsxStatAaOctsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaOctsDnyFmSb = _TmnxBsxStatAaOctsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 5),
    _TmnxBsxStatAaOctsDnyFmSb_Type()
)
tmnxBsxStatAaOctsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaOctsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaOctsDnyFmSb.setUnits("bytes")
_TmnxBsxStatAaPktsDnyFmSb_Type = Counter32
_TmnxBsxStatAaPktsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaPktsDnyFmSb = _TmnxBsxStatAaPktsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 6),
    _TmnxBsxStatAaPktsDnyFmSb_Type()
)
tmnxBsxStatAaPktsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaPktsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaPktsDnyFmSb.setUnits("packets")
_TmnxBsxStatAaFlwsDnyFmSb_Type = Counter32
_TmnxBsxStatAaFlwsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaFlwsDnyFmSb = _TmnxBsxStatAaFlwsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 7),
    _TmnxBsxStatAaFlwsDnyFmSb_Type()
)
tmnxBsxStatAaFlwsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaFlwsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaFlwsDnyFmSb.setUnits("flows")
_TmnxBsxStatAaOctsAdmToSb_Type = Counter32
_TmnxBsxStatAaOctsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaOctsAdmToSb = _TmnxBsxStatAaOctsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 8),
    _TmnxBsxStatAaOctsAdmToSb_Type()
)
tmnxBsxStatAaOctsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaOctsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaOctsAdmToSb.setUnits("bytes")
_TmnxBsxStatAaPktsAdmToSb_Type = Counter32
_TmnxBsxStatAaPktsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaPktsAdmToSb = _TmnxBsxStatAaPktsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 9),
    _TmnxBsxStatAaPktsAdmToSb_Type()
)
tmnxBsxStatAaPktsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaPktsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaPktsAdmToSb.setUnits("packets")
_TmnxBsxStatAaFlwsAdmToSb_Type = Counter32
_TmnxBsxStatAaFlwsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaFlwsAdmToSb = _TmnxBsxStatAaFlwsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 10),
    _TmnxBsxStatAaFlwsAdmToSb_Type()
)
tmnxBsxStatAaFlwsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaFlwsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaFlwsAdmToSb.setUnits("flows")
_TmnxBsxStatAaOctsDnyToSb_Type = Counter32
_TmnxBsxStatAaOctsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaOctsDnyToSb = _TmnxBsxStatAaOctsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 11),
    _TmnxBsxStatAaOctsDnyToSb_Type()
)
tmnxBsxStatAaOctsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaOctsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaOctsDnyToSb.setUnits("bytes")
_TmnxBsxStatAaPktsDnyToSb_Type = Counter32
_TmnxBsxStatAaPktsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaPktsDnyToSb = _TmnxBsxStatAaPktsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 12),
    _TmnxBsxStatAaPktsDnyToSb_Type()
)
tmnxBsxStatAaPktsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaPktsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaPktsDnyToSb.setUnits("packets")
_TmnxBsxStatAaFlwsDnyToSb_Type = Counter32
_TmnxBsxStatAaFlwsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaFlwsDnyToSb = _TmnxBsxStatAaFlwsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 13),
    _TmnxBsxStatAaFlwsDnyToSb_Type()
)
tmnxBsxStatAaFlwsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaFlwsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaFlwsDnyToSb.setUnits("flows")
_TmnxBsxStatAaTermFlwDur_Type = Counter32
_TmnxBsxStatAaTermFlwDur_Object = MibTableColumn
tmnxBsxStatAaTermFlwDur = _TmnxBsxStatAaTermFlwDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 14),
    _TmnxBsxStatAaTermFlwDur_Type()
)
tmnxBsxStatAaTermFlwDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaTermFlwDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaTermFlwDur.setUnits("seconds")
_TmnxBsxStatAaTermFlws_Type = Counter32
_TmnxBsxStatAaTermFlws_Object = MibTableColumn
tmnxBsxStatAaTermFlws = _TmnxBsxStatAaTermFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 15),
    _TmnxBsxStatAaTermFlws_Type()
)
tmnxBsxStatAaTermFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaTermFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaTermFlws.setUnits("flows")
_TmnxBsxStatAaShrtDurFlws_Type = Counter32
_TmnxBsxStatAaShrtDurFlws_Object = MibTableColumn
tmnxBsxStatAaShrtDurFlws = _TmnxBsxStatAaShrtDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 16),
    _TmnxBsxStatAaShrtDurFlws_Type()
)
tmnxBsxStatAaShrtDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaShrtDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaShrtDurFlws.setUnits("flows")
_TmnxBsxStatAaMedDurFlws_Type = Counter32
_TmnxBsxStatAaMedDurFlws_Object = MibTableColumn
tmnxBsxStatAaMedDurFlws = _TmnxBsxStatAaMedDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 17),
    _TmnxBsxStatAaMedDurFlws_Type()
)
tmnxBsxStatAaMedDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaMedDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaMedDurFlws.setUnits("flows")
_TmnxBsxStatAaLngDurFlws_Type = Counter32
_TmnxBsxStatAaLngDurFlws_Object = MibTableColumn
tmnxBsxStatAaLngDurFlws = _TmnxBsxStatAaLngDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 18),
    _TmnxBsxStatAaLngDurFlws_Type()
)
tmnxBsxStatAaLngDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaLngDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaLngDurFlws.setUnits("flows")
_TmnxBsxStatAaActFlwsFmSb_Type = Gauge32
_TmnxBsxStatAaActFlwsFmSb_Object = MibTableColumn
tmnxBsxStatAaActFlwsFmSb = _TmnxBsxStatAaActFlwsFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 19),
    _TmnxBsxStatAaActFlwsFmSb_Type()
)
tmnxBsxStatAaActFlwsFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaActFlwsFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaActFlwsFmSb.setUnits("flows")
_TmnxBsxStatAaActFlwsToSb_Type = Gauge32
_TmnxBsxStatAaActFlwsToSb_Object = MibTableColumn
tmnxBsxStatAaActFlwsToSb = _TmnxBsxStatAaActFlwsToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 20),
    _TmnxBsxStatAaActFlwsToSb_Type()
)
tmnxBsxStatAaActFlwsToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaActFlwsToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaActFlwsToSb.setUnits("flows")
_TmnxBsxStatAaNumSubscribers_Type = Gauge32
_TmnxBsxStatAaNumSubscribers_Object = MibTableColumn
tmnxBsxStatAaNumSubscribers = _TmnxBsxStatAaNumSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 21),
    _TmnxBsxStatAaNumSubscribers_Type()
)
tmnxBsxStatAaNumSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaNumSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaNumSubscribers.setUnits("subscribers")
_TmnxBsxStatAaHCOctsAdmFmSb_Type = Counter64
_TmnxBsxStatAaHCOctsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaHCOctsAdmFmSb = _TmnxBsxStatAaHCOctsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 22),
    _TmnxBsxStatAaHCOctsAdmFmSb_Type()
)
tmnxBsxStatAaHCOctsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCOctsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCOctsAdmFmSb.setUnits("bytes")
_TmnxBsxStatAaHCPktsAdmFmSb_Type = Counter64
_TmnxBsxStatAaHCPktsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaHCPktsAdmFmSb = _TmnxBsxStatAaHCPktsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 23),
    _TmnxBsxStatAaHCPktsAdmFmSb_Type()
)
tmnxBsxStatAaHCPktsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCPktsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCPktsAdmFmSb.setUnits("packets")
_TmnxBsxStatAaHCFlwsAdmFmSb_Type = Counter64
_TmnxBsxStatAaHCFlwsAdmFmSb_Object = MibTableColumn
tmnxBsxStatAaHCFlwsAdmFmSb = _TmnxBsxStatAaHCFlwsAdmFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 24),
    _TmnxBsxStatAaHCFlwsAdmFmSb_Type()
)
tmnxBsxStatAaHCFlwsAdmFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCFlwsAdmFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCFlwsAdmFmSb.setUnits("flows")
_TmnxBsxStatAaHCOctsDnyFmSb_Type = Counter64
_TmnxBsxStatAaHCOctsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaHCOctsDnyFmSb = _TmnxBsxStatAaHCOctsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 25),
    _TmnxBsxStatAaHCOctsDnyFmSb_Type()
)
tmnxBsxStatAaHCOctsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCOctsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCOctsDnyFmSb.setUnits("bytes")
_TmnxBsxStatAaHCPktsDnyFmSb_Type = Counter64
_TmnxBsxStatAaHCPktsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaHCPktsDnyFmSb = _TmnxBsxStatAaHCPktsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 26),
    _TmnxBsxStatAaHCPktsDnyFmSb_Type()
)
tmnxBsxStatAaHCPktsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCPktsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCPktsDnyFmSb.setUnits("packets")
_TmnxBsxStatAaHCFlwsDnyFmSb_Type = Counter64
_TmnxBsxStatAaHCFlwsDnyFmSb_Object = MibTableColumn
tmnxBsxStatAaHCFlwsDnyFmSb = _TmnxBsxStatAaHCFlwsDnyFmSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 27),
    _TmnxBsxStatAaHCFlwsDnyFmSb_Type()
)
tmnxBsxStatAaHCFlwsDnyFmSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCFlwsDnyFmSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCFlwsDnyFmSb.setUnits("flows")
_TmnxBsxStatAaHCOctsAdmToSb_Type = Counter64
_TmnxBsxStatAaHCOctsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaHCOctsAdmToSb = _TmnxBsxStatAaHCOctsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 28),
    _TmnxBsxStatAaHCOctsAdmToSb_Type()
)
tmnxBsxStatAaHCOctsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCOctsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCOctsAdmToSb.setUnits("bytes")
_TmnxBsxStatAaHCPktsAdmToSb_Type = Counter64
_TmnxBsxStatAaHCPktsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaHCPktsAdmToSb = _TmnxBsxStatAaHCPktsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 29),
    _TmnxBsxStatAaHCPktsAdmToSb_Type()
)
tmnxBsxStatAaHCPktsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCPktsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCPktsAdmToSb.setUnits("packets")
_TmnxBsxStatAaHCFlwsAdmToSb_Type = Counter64
_TmnxBsxStatAaHCFlwsAdmToSb_Object = MibTableColumn
tmnxBsxStatAaHCFlwsAdmToSb = _TmnxBsxStatAaHCFlwsAdmToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 30),
    _TmnxBsxStatAaHCFlwsAdmToSb_Type()
)
tmnxBsxStatAaHCFlwsAdmToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCFlwsAdmToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCFlwsAdmToSb.setUnits("flows")
_TmnxBsxStatAaHCOctsDnyToSb_Type = Counter64
_TmnxBsxStatAaHCOctsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaHCOctsDnyToSb = _TmnxBsxStatAaHCOctsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 31),
    _TmnxBsxStatAaHCOctsDnyToSb_Type()
)
tmnxBsxStatAaHCOctsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCOctsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCOctsDnyToSb.setUnits("bytes")
_TmnxBsxStatAaHCPktsDnyToSb_Type = Counter64
_TmnxBsxStatAaHCPktsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaHCPktsDnyToSb = _TmnxBsxStatAaHCPktsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 32),
    _TmnxBsxStatAaHCPktsDnyToSb_Type()
)
tmnxBsxStatAaHCPktsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCPktsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCPktsDnyToSb.setUnits("packets")
_TmnxBsxStatAaHCFlwsDnyToSb_Type = Counter64
_TmnxBsxStatAaHCFlwsDnyToSb_Object = MibTableColumn
tmnxBsxStatAaHCFlwsDnyToSb = _TmnxBsxStatAaHCFlwsDnyToSb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 33),
    _TmnxBsxStatAaHCFlwsDnyToSb_Type()
)
tmnxBsxStatAaHCFlwsDnyToSb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCFlwsDnyToSb.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCFlwsDnyToSb.setUnits("flows")
_TmnxBsxStatAaHCTermFlwDur_Type = Counter64
_TmnxBsxStatAaHCTermFlwDur_Object = MibTableColumn
tmnxBsxStatAaHCTermFlwDur = _TmnxBsxStatAaHCTermFlwDur_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 34),
    _TmnxBsxStatAaHCTermFlwDur_Type()
)
tmnxBsxStatAaHCTermFlwDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCTermFlwDur.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCTermFlwDur.setUnits("seconds")
_TmnxBsxStatAaHCTermFlws_Type = Counter64
_TmnxBsxStatAaHCTermFlws_Object = MibTableColumn
tmnxBsxStatAaHCTermFlws = _TmnxBsxStatAaHCTermFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 35),
    _TmnxBsxStatAaHCTermFlws_Type()
)
tmnxBsxStatAaHCTermFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCTermFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCTermFlws.setUnits("flows")
_TmnxBsxStatAaHCShrtDurFlws_Type = Counter64
_TmnxBsxStatAaHCShrtDurFlws_Object = MibTableColumn
tmnxBsxStatAaHCShrtDurFlws = _TmnxBsxStatAaHCShrtDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 36),
    _TmnxBsxStatAaHCShrtDurFlws_Type()
)
tmnxBsxStatAaHCShrtDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCShrtDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCShrtDurFlws.setUnits("flows")
_TmnxBsxStatAaHCMedDurFlws_Type = Counter64
_TmnxBsxStatAaHCMedDurFlws_Object = MibTableColumn
tmnxBsxStatAaHCMedDurFlws = _TmnxBsxStatAaHCMedDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 37),
    _TmnxBsxStatAaHCMedDurFlws_Type()
)
tmnxBsxStatAaHCMedDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCMedDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCMedDurFlws.setUnits("flows")
_TmnxBsxStatAaHCLngDurFlws_Type = Counter64
_TmnxBsxStatAaHCLngDurFlws_Object = MibTableColumn
tmnxBsxStatAaHCLngDurFlws = _TmnxBsxStatAaHCLngDurFlws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 7, 1, 38),
    _TmnxBsxStatAaHCLngDurFlws_Type()
)
tmnxBsxStatAaHCLngDurFlws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCLngDurFlws.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaHCLngDurFlws.setUnits("flows")
_TmnxBsxStatAaAppFilterTable_Object = MibTable
tmnxBsxStatAaAppFilterTable = _TmnxBsxStatAaAppFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterTable.setStatus("current")
_TmnxBsxStatAaAppFilterEntry_Object = MibTableRow
tmnxBsxStatAaAppFilterEntry = _TmnxBsxStatAaAppFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 8, 1)
)
tmnxBsxStatAaAppFilterEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterEntryId"),
)
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterEntry.setStatus("current")
_TmnxBsxStatAaAppFilterHCFlows_Type = Counter64
_TmnxBsxStatAaAppFilterHCFlows_Object = MibTableColumn
tmnxBsxStatAaAppFilterHCFlows = _TmnxBsxStatAaAppFilterHCFlows_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 8, 1, 1),
    _TmnxBsxStatAaAppFilterHCFlows_Type()
)
tmnxBsxStatAaAppFilterHCFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterHCFlows.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterHCFlows.setUnits("flows")
_TmnxBsxStatAaAppFilterFlowsLo_Type = Counter32
_TmnxBsxStatAaAppFilterFlowsLo_Object = MibTableColumn
tmnxBsxStatAaAppFilterFlowsLo = _TmnxBsxStatAaAppFilterFlowsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 8, 1, 2),
    _TmnxBsxStatAaAppFilterFlowsLo_Type()
)
tmnxBsxStatAaAppFilterFlowsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterFlowsLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterFlowsLo.setUnits("flows")
_TmnxBsxStatAaAppFilterFlowsHi_Type = Counter32
_TmnxBsxStatAaAppFilterFlowsHi_Object = MibTableColumn
tmnxBsxStatAaAppFilterFlowsHi = _TmnxBsxStatAaAppFilterFlowsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 8, 1, 3),
    _TmnxBsxStatAaAppFilterFlowsHi_Type()
)
tmnxBsxStatAaAppFilterFlowsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterFlowsHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterFlowsHi.setUnits("flows")
_TmnxBsxStatAaAppFilterFlowHCOctC_Type = Counter64
_TmnxBsxStatAaAppFilterFlowHCOctC_Object = MibTableColumn
tmnxBsxStatAaAppFilterFlowHCOctC = _TmnxBsxStatAaAppFilterFlowHCOctC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 8, 1, 4),
    _TmnxBsxStatAaAppFilterFlowHCOctC_Type()
)
tmnxBsxStatAaAppFilterFlowHCOctC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterFlowHCOctC.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterFlowHCOctC.setUnits("octets")
_TmnxBsxStatAaAppFilterFlowOctCLo_Type = Counter32
_TmnxBsxStatAaAppFilterFlowOctCLo_Object = MibTableColumn
tmnxBsxStatAaAppFilterFlowOctCLo = _TmnxBsxStatAaAppFilterFlowOctCLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 8, 1, 5),
    _TmnxBsxStatAaAppFilterFlowOctCLo_Type()
)
tmnxBsxStatAaAppFilterFlowOctCLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterFlowOctCLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterFlowOctCLo.setUnits("octets")
_TmnxBsxStatAaAppFilterFlowOctCHi_Type = Counter32
_TmnxBsxStatAaAppFilterFlowOctCHi_Object = MibTableColumn
tmnxBsxStatAaAppFilterFlowOctCHi = _TmnxBsxStatAaAppFilterFlowOctCHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 8, 1, 6),
    _TmnxBsxStatAaAppFilterFlowOctCHi_Type()
)
tmnxBsxStatAaAppFilterFlowOctCHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterFlowOctCHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxStatAaAppFilterFlowOctCHi.setUnits("octets")
_TmnxBsxStatIsaAaCfgTable_Object = MibTable
tmnxBsxStatIsaAaCfgTable = _TmnxBsxStatIsaAaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 9)
)
if mibBuilder.loadTexts:
    tmnxBsxStatIsaAaCfgTable.setStatus("current")
_TmnxBsxStatIsaAaCfgEntry_Object = MibTableRow
tmnxBsxStatIsaAaCfgEntry = _TmnxBsxStatIsaAaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 9, 1)
)
tmnxBsxStatIsaAaCfgEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatIsaAaCfgType"),
)
if mibBuilder.loadTexts:
    tmnxBsxStatIsaAaCfgEntry.setStatus("current")
_TmnxBsxStatIsaAaCfgType_Type = TmnxBsxStatIsaAaCfgType
_TmnxBsxStatIsaAaCfgType_Object = MibTableColumn
tmnxBsxStatIsaAaCfgType = _TmnxBsxStatIsaAaCfgType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 9, 1, 1),
    _TmnxBsxStatIsaAaCfgType_Type()
)
tmnxBsxStatIsaAaCfgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxStatIsaAaCfgType.setStatus("current")


class _TmnxBsxStatIsaAaCfgCollStats_Type(TruthValue):
    """Custom type tmnxBsxStatIsaAaCfgCollStats based on TruthValue"""


_TmnxBsxStatIsaAaCfgCollStats_Object = MibTableColumn
tmnxBsxStatIsaAaCfgCollStats = _TmnxBsxStatIsaAaCfgCollStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 9, 1, 2),
    _TmnxBsxStatIsaAaCfgCollStats_Type()
)
tmnxBsxStatIsaAaCfgCollStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxStatIsaAaCfgCollStats.setStatus("current")


class _TmnxBsxStatIsaAaCfgPolicy_Type(Unsigned32):
    """Custom type tmnxBsxStatIsaAaCfgPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxBsxStatIsaAaCfgPolicy_Type.__name__ = "Unsigned32"
_TmnxBsxStatIsaAaCfgPolicy_Object = MibTableColumn
tmnxBsxStatIsaAaCfgPolicy = _TmnxBsxStatIsaAaCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 3, 9, 1, 3),
    _TmnxBsxStatIsaAaCfgPolicy_Type()
)
tmnxBsxStatIsaAaCfgPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxStatIsaAaCfgPolicy.setStatus("current")
_TmnxBsxNotifObjs_ObjectIdentity = ObjectIdentity
tmnxBsxNotifObjs = _TmnxBsxNotifObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4)
)
_TmnxBsxNotifyIsaAaGroupIndex_Type = TmnxBsxIsaAaGroupIndex
_TmnxBsxNotifyIsaAaGroupIndex_Object = MibScalar
tmnxBsxNotifyIsaAaGroupIndex = _TmnxBsxNotifyIsaAaGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4, 1),
    _TmnxBsxNotifyIsaAaGroupIndex_Type()
)
tmnxBsxNotifyIsaAaGroupIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBsxNotifyIsaAaGroupIndex.setStatus("current")
_TmnxBsxNotifyActiveMda_Type = TmnxHwIndexOrZero
_TmnxBsxNotifyActiveMda_Object = MibScalar
tmnxBsxNotifyActiveMda = _TmnxBsxNotifyActiveMda_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4, 2),
    _TmnxBsxNotifyActiveMda_Type()
)
tmnxBsxNotifyActiveMda.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBsxNotifyActiveMda.setStatus("current")
_TmnxBsxNotifyActionStatus_Type = TmnxBsxActionStatus
_TmnxBsxNotifyActionStatus_Object = MibScalar
tmnxBsxNotifyActionStatus = _TmnxBsxNotifyActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4, 3),
    _TmnxBsxNotifyActionStatus_Type()
)
tmnxBsxNotifyActionStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBsxNotifyActionStatus.setStatus("current")
_TmnxBsxNotifyAaSubscriberType_Type = TmnxBsxAaSubscriberType
_TmnxBsxNotifyAaSubscriberType_Object = MibScalar
tmnxBsxNotifyAaSubscriberType = _TmnxBsxNotifyAaSubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4, 4),
    _TmnxBsxNotifyAaSubscriberType_Type()
)
tmnxBsxNotifyAaSubscriberType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBsxNotifyAaSubscriberType.setStatus("current")
_TmnxBsxNotifyAaSubscriberName_Type = TmnxBsxAaSubscriber
_TmnxBsxNotifyAaSubscriberName_Object = MibScalar
tmnxBsxNotifyAaSubscriberName = _TmnxBsxNotifyAaSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4, 5),
    _TmnxBsxNotifyAaSubscriberName_Type()
)
tmnxBsxNotifyAaSubscriberName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBsxNotifyAaSubscriberName.setStatus("current")
_TmnxBsxNotifyAaSubAcctLossReason_Type = TmnxBsxAaSubAcctLossReason
_TmnxBsxNotifyAaSubAcctLossReason_Object = MibScalar
tmnxBsxNotifyAaSubAcctLossReason = _TmnxBsxNotifyAaSubAcctLossReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4, 6),
    _TmnxBsxNotifyAaSubAcctLossReason_Type()
)
tmnxBsxNotifyAaSubAcctLossReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBsxNotifyAaSubAcctLossReason.setStatus("current")
_TmnxBsxNotifyAaGrpPartIndex_Type = TmnxBsxAaGrpPartIndex
_TmnxBsxNotifyAaGrpPartIndex_Object = MibScalar
tmnxBsxNotifyAaGrpPartIndex = _TmnxBsxNotifyAaGrpPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4, 7),
    _TmnxBsxNotifyAaGrpPartIndex_Type()
)
tmnxBsxNotifyAaGrpPartIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBsxNotifyAaGrpPartIndex.setStatus("current")
_TmnxBsxNotifyTransitIpPolicyId_Type = TmnxBsxTransitIpPolicyId
_TmnxBsxNotifyTransitIpPolicyId_Object = MibScalar
tmnxBsxNotifyTransitIpPolicyId = _TmnxBsxNotifyTransitIpPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4, 8),
    _TmnxBsxNotifyTransitIpPolicyId_Type()
)
tmnxBsxNotifyTransitIpPolicyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBsxNotifyTransitIpPolicyId.setStatus("current")


class _TmnxBsxNotifyRadiusCoAAuditState_Type(Integer32):
    """Custom type tmnxBsxNotifyRadiusCoAAuditState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end", 2),
          ("start", 1))
    )


_TmnxBsxNotifyRadiusCoAAuditState_Type.__name__ = "Integer32"
_TmnxBsxNotifyRadiusCoAAuditState_Object = MibScalar
tmnxBsxNotifyRadiusCoAAuditState = _TmnxBsxNotifyRadiusCoAAuditState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4, 9),
    _TmnxBsxNotifyRadiusCoAAuditState_Type()
)
tmnxBsxNotifyRadiusCoAAuditState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBsxNotifyRadiusCoAAuditState.setStatus("current")
_TmnxBsxNotifyReason_Type = DisplayString
_TmnxBsxNotifyReason_Object = MibScalar
tmnxBsxNotifyReason = _TmnxBsxNotifyReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 4, 10),
    _TmnxBsxNotifyReason_Type()
)
tmnxBsxNotifyReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBsxNotifyReason.setStatus("current")
_TmnxBsxCflowdObjs_ObjectIdentity = ObjectIdentity
tmnxBsxCflowdObjs = _TmnxBsxCflowdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5)
)
_TmnxBsxCflowdScalars_ObjectIdentity = ObjectIdentity
tmnxBsxCflowdScalars = _TmnxBsxCflowdScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 1)
)
_TmnxBsxCflowdLastChangeTime_Type = TimeStamp
_TmnxBsxCflowdLastChangeTime_Object = MibScalar
tmnxBsxCflowdLastChangeTime = _TmnxBsxCflowdLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 1, 1),
    _TmnxBsxCflowdLastChangeTime_Type()
)
tmnxBsxCflowdLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdLastChangeTime.setStatus("current")
_TmnxBsxCflowdCollLastChangeTime_Type = TimeStamp
_TmnxBsxCflowdCollLastChangeTime_Object = MibScalar
tmnxBsxCflowdCollLastChangeTime = _TmnxBsxCflowdCollLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 1, 2),
    _TmnxBsxCflowdCollLastChangeTime_Type()
)
tmnxBsxCflowdCollLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollLastChangeTime.setStatus("current")
_TmnxBsxCflowdPerfLastChangeTime_Type = TimeStamp
_TmnxBsxCflowdPerfLastChangeTime_Object = MibScalar
tmnxBsxCflowdPerfLastChangeTime = _TmnxBsxCflowdPerfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 1, 3),
    _TmnxBsxCflowdPerfLastChangeTime_Type()
)
tmnxBsxCflowdPerfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfLastChangeTime.setStatus("current")
_TmnxBsxCflowdExpLastChangeTime_Type = TimeStamp
_TmnxBsxCflowdExpLastChangeTime_Object = MibScalar
tmnxBsxCflowdExpLastChangeTime = _TmnxBsxCflowdExpLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 1, 4),
    _TmnxBsxCflowdExpLastChangeTime_Type()
)
tmnxBsxCflowdExpLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpLastChangeTime.setStatus("current")
_TmnxBsxCflowdPerfExpLastChTime_Type = TimeStamp
_TmnxBsxCflowdPerfExpLastChTime_Object = MibScalar
tmnxBsxCflowdPerfExpLastChTime = _TmnxBsxCflowdPerfExpLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 1, 5),
    _TmnxBsxCflowdPerfExpLastChTime_Type()
)
tmnxBsxCflowdPerfExpLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfExpLastChTime.setStatus("current")
_TmnxBsxCflowdTable_Object = MibTable
tmnxBsxCflowdTable = _TmnxBsxCflowdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdTable.setStatus("current")
_TmnxBsxCflowdEntry_Object = MibTableRow
tmnxBsxCflowdEntry = _TmnxBsxCflowdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 2, 1)
)
tmnxBsxCflowdEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdEntry.setStatus("current")
_TmnxBsxCflowdRowLastChange_Type = TimeStamp
_TmnxBsxCflowdRowLastChange_Object = MibTableColumn
tmnxBsxCflowdRowLastChange = _TmnxBsxCflowdRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 2, 1, 1),
    _TmnxBsxCflowdRowLastChange_Type()
)
tmnxBsxCflowdRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdRowLastChange.setStatus("current")


class _TmnxBsxCflowdAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxCflowdAdminState based on TmnxAdminState"""


_TmnxBsxCflowdAdminState_Object = MibTableColumn
tmnxBsxCflowdAdminState = _TmnxBsxCflowdAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 2, 1, 2),
    _TmnxBsxCflowdAdminState_Type()
)
tmnxBsxCflowdAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxCflowdAdminState.setStatus("current")


class _TmnxBsxCflowdVolRate_Type(Unsigned32):
    """Custom type tmnxBsxCflowdVolRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxBsxCflowdVolRate_Type.__name__ = "Unsigned32"
_TmnxBsxCflowdVolRate_Object = MibTableColumn
tmnxBsxCflowdVolRate = _TmnxBsxCflowdVolRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 2, 1, 3),
    _TmnxBsxCflowdVolRate_Type()
)
tmnxBsxCflowdVolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxCflowdVolRate.setStatus("current")


class _TmnxBsxCflowdTemplateRetransmit_Type(Unsigned32):
    """Custom type tmnxBsxCflowdTemplateRetransmit based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_TmnxBsxCflowdTemplateRetransmit_Type.__name__ = "Unsigned32"
_TmnxBsxCflowdTemplateRetransmit_Object = MibTableColumn
tmnxBsxCflowdTemplateRetransmit = _TmnxBsxCflowdTemplateRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 2, 1, 4),
    _TmnxBsxCflowdTemplateRetransmit_Type()
)
tmnxBsxCflowdTemplateRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxCflowdTemplateRetransmit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdTemplateRetransmit.setUnits("seconds")
_TmnxBsxCflowdCollTable_Object = MibTable
tmnxBsxCflowdCollTable = _TmnxBsxCflowdCollTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollTable.setStatus("current")
_TmnxBsxCflowdCollEntry_Object = MibTableRow
tmnxBsxCflowdCollEntry = _TmnxBsxCflowdCollEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3, 1)
)
tmnxBsxCflowdCollEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollAddressType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollAddress"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollPort"),
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollEntry.setStatus("current")
_TmnxBsxCflowdCollAddressType_Type = InetAddressType
_TmnxBsxCflowdCollAddressType_Object = MibTableColumn
tmnxBsxCflowdCollAddressType = _TmnxBsxCflowdCollAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3, 1, 1),
    _TmnxBsxCflowdCollAddressType_Type()
)
tmnxBsxCflowdCollAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollAddressType.setStatus("current")


class _TmnxBsxCflowdCollAddress_Type(InetAddress):
    """Custom type tmnxBsxCflowdCollAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxCflowdCollAddress_Type.__name__ = "InetAddress"
_TmnxBsxCflowdCollAddress_Object = MibTableColumn
tmnxBsxCflowdCollAddress = _TmnxBsxCflowdCollAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3, 1, 2),
    _TmnxBsxCflowdCollAddress_Type()
)
tmnxBsxCflowdCollAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollAddress.setStatus("current")


class _TmnxBsxCflowdCollPort_Type(TTcpUdpPort):
    """Custom type tmnxBsxCflowdCollPort based on TTcpUdpPort"""
    subtypeSpec = TTcpUdpPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxBsxCflowdCollPort_Type.__name__ = "TTcpUdpPort"
_TmnxBsxCflowdCollPort_Object = MibTableColumn
tmnxBsxCflowdCollPort = _TmnxBsxCflowdCollPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3, 1, 3),
    _TmnxBsxCflowdCollPort_Type()
)
tmnxBsxCflowdCollPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollPort.setStatus("current")
_TmnxBsxCflowdCollRowStatus_Type = RowStatus
_TmnxBsxCflowdCollRowStatus_Object = MibTableColumn
tmnxBsxCflowdCollRowStatus = _TmnxBsxCflowdCollRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3, 1, 4),
    _TmnxBsxCflowdCollRowStatus_Type()
)
tmnxBsxCflowdCollRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollRowStatus.setStatus("current")
_TmnxBsxCflowdCollRowLastChange_Type = TimeStamp
_TmnxBsxCflowdCollRowLastChange_Object = MibTableColumn
tmnxBsxCflowdCollRowLastChange = _TmnxBsxCflowdCollRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3, 1, 5),
    _TmnxBsxCflowdCollRowLastChange_Type()
)
tmnxBsxCflowdCollRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollRowLastChange.setStatus("current")
_TmnxBsxCflowdCollDescription_Type = TItemDescription
_TmnxBsxCflowdCollDescription_Object = MibTableColumn
tmnxBsxCflowdCollDescription = _TmnxBsxCflowdCollDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3, 1, 6),
    _TmnxBsxCflowdCollDescription_Type()
)
tmnxBsxCflowdCollDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollDescription.setStatus("current")


class _TmnxBsxCflowdCollAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxCflowdCollAdminState based on TmnxAdminState"""


_TmnxBsxCflowdCollAdminState_Object = MibTableColumn
tmnxBsxCflowdCollAdminState = _TmnxBsxCflowdCollAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3, 1, 7),
    _TmnxBsxCflowdCollAdminState_Type()
)
tmnxBsxCflowdCollAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollAdminState.setStatus("current")


class _TmnxBsxCflowdCollOperState_Type(TmnxOperState):
    """Custom type tmnxBsxCflowdCollOperState based on TmnxOperState"""


_TmnxBsxCflowdCollOperState_Object = MibTableColumn
tmnxBsxCflowdCollOperState = _TmnxBsxCflowdCollOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3, 1, 8),
    _TmnxBsxCflowdCollOperState_Type()
)
tmnxBsxCflowdCollOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollOperState.setStatus("current")


class _TmnxBsxCflowdCollVersion_Type(Unsigned32):
    """Custom type tmnxBsxCflowdCollVersion based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
    )


_TmnxBsxCflowdCollVersion_Type.__name__ = "Unsigned32"
_TmnxBsxCflowdCollVersion_Object = MibTableColumn
tmnxBsxCflowdCollVersion = _TmnxBsxCflowdCollVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 3, 1, 9),
    _TmnxBsxCflowdCollVersion_Type()
)
tmnxBsxCflowdCollVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollVersion.setStatus("current")
_TmnxBsxCflowdPerfTable_Object = MibTable
tmnxBsxCflowdPerfTable = _TmnxBsxCflowdPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfTable.setStatus("current")
_TmnxBsxCflowdPerfEntry_Object = MibTableRow
tmnxBsxCflowdPerfEntry = _TmnxBsxCflowdPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 4, 1)
)
tmnxBsxCflowdPerfEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdPerfMeasType"),
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfEntry.setStatus("current")
_TmnxBsxCflowdPerfMeasType_Type = TmnxBsxCflowdPerfMeasType
_TmnxBsxCflowdPerfMeasType_Object = MibTableColumn
tmnxBsxCflowdPerfMeasType = _TmnxBsxCflowdPerfMeasType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 4, 1, 1),
    _TmnxBsxCflowdPerfMeasType_Type()
)
tmnxBsxCflowdPerfMeasType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfMeasType.setStatus("current")
_TmnxBsxCflowdPerfRowLastChange_Type = TimeStamp
_TmnxBsxCflowdPerfRowLastChange_Object = MibTableColumn
tmnxBsxCflowdPerfRowLastChange = _TmnxBsxCflowdPerfRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 4, 1, 2),
    _TmnxBsxCflowdPerfRowLastChange_Type()
)
tmnxBsxCflowdPerfRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfRowLastChange.setStatus("current")


class _TmnxBsxCflowdPerfFlowRate_Type(Unsigned32):
    """Custom type tmnxBsxCflowdPerfFlowRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxBsxCflowdPerfFlowRate_Type.__name__ = "Unsigned32"
_TmnxBsxCflowdPerfFlowRate_Object = MibTableColumn
tmnxBsxCflowdPerfFlowRate = _TmnxBsxCflowdPerfFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 4, 1, 3),
    _TmnxBsxCflowdPerfFlowRate_Type()
)
tmnxBsxCflowdPerfFlowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfFlowRate.setStatus("current")


class _TmnxBsxCflowdPerfFlowRate2_Type(Unsigned32):
    """Custom type tmnxBsxCflowdPerfFlowRate2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxBsxCflowdPerfFlowRate2_Type.__name__ = "Unsigned32"
_TmnxBsxCflowdPerfFlowRate2_Object = MibTableColumn
tmnxBsxCflowdPerfFlowRate2 = _TmnxBsxCflowdPerfFlowRate2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 4, 1, 4),
    _TmnxBsxCflowdPerfFlowRate2_Type()
)
tmnxBsxCflowdPerfFlowRate2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfFlowRate2.setStatus("current")
_TmnxBsxCflowdExpTable_Object = MibTable
tmnxBsxCflowdExpTable = _TmnxBsxCflowdExpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 5)
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpTable.setStatus("current")
_TmnxBsxCflowdExpEntry_Object = MibTableRow
tmnxBsxCflowdExpEntry = _TmnxBsxCflowdExpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 5, 1)
)
tmnxBsxCflowdExpEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpType"),
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpEntry.setStatus("current")
_TmnxBsxCflowdExpType_Type = TmnxBsxCflowdExpType
_TmnxBsxCflowdExpType_Object = MibTableColumn
tmnxBsxCflowdExpType = _TmnxBsxCflowdExpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 5, 1, 1),
    _TmnxBsxCflowdExpType_Type()
)
tmnxBsxCflowdExpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpType.setStatus("current")
_TmnxBsxCflowdExpRowLastChange_Type = TimeStamp
_TmnxBsxCflowdExpRowLastChange_Object = MibTableColumn
tmnxBsxCflowdExpRowLastChange = _TmnxBsxCflowdExpRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 5, 1, 2),
    _TmnxBsxCflowdExpRowLastChange_Type()
)
tmnxBsxCflowdExpRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpRowLastChange.setStatus("current")


class _TmnxBsxCflowdExpAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxCflowdExpAdminState based on TmnxAdminState"""


_TmnxBsxCflowdExpAdminState_Object = MibTableColumn
tmnxBsxCflowdExpAdminState = _TmnxBsxCflowdExpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 5, 1, 3),
    _TmnxBsxCflowdExpAdminState_Type()
)
tmnxBsxCflowdExpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpAdminState.setStatus("current")
_TmnxBsxCflowdPerfExpTable_Object = MibTable
tmnxBsxCflowdPerfExpTable = _TmnxBsxCflowdPerfExpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 6)
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfExpTable.setStatus("current")
_TmnxBsxCflowdPerfExpEntry_Object = MibTableRow
tmnxBsxCflowdPerfExpEntry = _TmnxBsxCflowdPerfExpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 6, 1)
)
tmnxBsxCflowdPerfExpEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaName"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdPerfMeasType"),
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfExpEntry.setStatus("current")
_TmnxBsxCflowdPerfExpRowStatus_Type = RowStatus
_TmnxBsxCflowdPerfExpRowStatus_Object = MibTableColumn
tmnxBsxCflowdPerfExpRowStatus = _TmnxBsxCflowdPerfExpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 6, 1, 1),
    _TmnxBsxCflowdPerfExpRowStatus_Type()
)
tmnxBsxCflowdPerfExpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfExpRowStatus.setStatus("current")
_TmnxBsxCflowdPerfExpRowLastChnge_Type = TimeStamp
_TmnxBsxCflowdPerfExpRowLastChnge_Object = MibTableColumn
tmnxBsxCflowdPerfExpRowLastChnge = _TmnxBsxCflowdPerfExpRowLastChnge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 6, 1, 2),
    _TmnxBsxCflowdPerfExpRowLastChnge_Type()
)
tmnxBsxCflowdPerfExpRowLastChnge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfExpRowLastChnge.setStatus("current")


class _TmnxBsxCflowdPerfExpRateNum_Type(Unsigned32):
    """Custom type tmnxBsxCflowdPerfExpRateNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxBsxCflowdPerfExpRateNum_Type.__name__ = "Unsigned32"
_TmnxBsxCflowdPerfExpRateNum_Object = MibTableColumn
tmnxBsxCflowdPerfExpRateNum = _TmnxBsxCflowdPerfExpRateNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 6, 1, 3),
    _TmnxBsxCflowdPerfExpRateNum_Type()
)
tmnxBsxCflowdPerfExpRateNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxCflowdPerfExpRateNum.setStatus("current")
_TmnxBsxCflowdStatusTable_Object = MibTable
tmnxBsxCflowdStatusTable = _TmnxBsxCflowdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7)
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusTable.setStatus("current")
_TmnxBsxCflowdStatusEntry_Object = MibTableRow
tmnxBsxCflowdStatusEntry = _TmnxBsxCflowdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1)
)
tmnxBsxCflowdStatusEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpType"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusEntry.setStatus("current")
_TmnxBsxCflowdStatusDiscontTime_Type = TimeStamp
_TmnxBsxCflowdStatusDiscontTime_Object = MibTableColumn
tmnxBsxCflowdStatusDiscontTime = _TmnxBsxCflowdStatusDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 1),
    _TmnxBsxCflowdStatusDiscontTime_Type()
)
tmnxBsxCflowdStatusDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusDiscontTime.setStatus("current")
_TmnxBsxCflowdStatusActFlowsCurr_Type = Gauge32
_TmnxBsxCflowdStatusActFlowsCurr_Object = MibTableColumn
tmnxBsxCflowdStatusActFlowsCurr = _TmnxBsxCflowdStatusActFlowsCurr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 2),
    _TmnxBsxCflowdStatusActFlowsCurr_Type()
)
tmnxBsxCflowdStatusActFlowsCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusActFlowsCurr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusActFlowsCurr.setUnits("flows")
_TmnxBsxCflowdStatusRecRateCurr_Type = Gauge32
_TmnxBsxCflowdStatusRecRateCurr_Object = MibTableColumn
tmnxBsxCflowdStatusRecRateCurr = _TmnxBsxCflowdStatusRecRateCurr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 3),
    _TmnxBsxCflowdStatusRecRateCurr_Type()
)
tmnxBsxCflowdStatusRecRateCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusRecRateCurr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusRecRateCurr.setUnits("records per second")
_TmnxBsxCflowdStatusPktRateCurr_Type = Gauge32
_TmnxBsxCflowdStatusPktRateCurr_Object = MibTableColumn
tmnxBsxCflowdStatusPktRateCurr = _TmnxBsxCflowdStatusPktRateCurr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 4),
    _TmnxBsxCflowdStatusPktRateCurr_Type()
)
tmnxBsxCflowdStatusPktRateCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusPktRateCurr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusPktRateCurr.setUnits("packets per second")
_TmnxBsxCflowdStatusRecReported_Type = Counter32
_TmnxBsxCflowdStatusRecReported_Object = MibTableColumn
tmnxBsxCflowdStatusRecReported = _TmnxBsxCflowdStatusRecReported_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 5),
    _TmnxBsxCflowdStatusRecReported_Type()
)
tmnxBsxCflowdStatusRecReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusRecReported.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusRecReported.setUnits("records")
_TmnxBsxCflowdStatusHCRecReported_Type = Counter64
_TmnxBsxCflowdStatusHCRecReported_Object = MibTableColumn
tmnxBsxCflowdStatusHCRecReported = _TmnxBsxCflowdStatusHCRecReported_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 6),
    _TmnxBsxCflowdStatusHCRecReported_Type()
)
tmnxBsxCflowdStatusHCRecReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusHCRecReported.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusHCRecReported.setUnits("records")
_TmnxBsxCflowdStatusRecDropped_Type = Counter32
_TmnxBsxCflowdStatusRecDropped_Object = MibTableColumn
tmnxBsxCflowdStatusRecDropped = _TmnxBsxCflowdStatusRecDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 7),
    _TmnxBsxCflowdStatusRecDropped_Type()
)
tmnxBsxCflowdStatusRecDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusRecDropped.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusRecDropped.setUnits("records")
_TmnxBsxCflowdStatusHCRecDropped_Type = Counter64
_TmnxBsxCflowdStatusHCRecDropped_Object = MibTableColumn
tmnxBsxCflowdStatusHCRecDropped = _TmnxBsxCflowdStatusHCRecDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 8),
    _TmnxBsxCflowdStatusHCRecDropped_Type()
)
tmnxBsxCflowdStatusHCRecDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusHCRecDropped.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusHCRecDropped.setUnits("records")
_TmnxBsxCflowdStatusPktsSent_Type = Counter32
_TmnxBsxCflowdStatusPktsSent_Object = MibTableColumn
tmnxBsxCflowdStatusPktsSent = _TmnxBsxCflowdStatusPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 9),
    _TmnxBsxCflowdStatusPktsSent_Type()
)
tmnxBsxCflowdStatusPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusPktsSent.setUnits("packets")
_TmnxBsxCflowdStatusHCPktsSent_Type = Counter64
_TmnxBsxCflowdStatusHCPktsSent_Object = MibTableColumn
tmnxBsxCflowdStatusHCPktsSent = _TmnxBsxCflowdStatusHCPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 10),
    _TmnxBsxCflowdStatusHCPktsSent_Type()
)
tmnxBsxCflowdStatusHCPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusHCPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusHCPktsSent.setUnits("packets")
_TmnxBsxCflowdStatusFlowsNoRes_Type = Counter32
_TmnxBsxCflowdStatusFlowsNoRes_Object = MibTableColumn
tmnxBsxCflowdStatusFlowsNoRes = _TmnxBsxCflowdStatusFlowsNoRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 11),
    _TmnxBsxCflowdStatusFlowsNoRes_Type()
)
tmnxBsxCflowdStatusFlowsNoRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusFlowsNoRes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusFlowsNoRes.setUnits("flows")
_TmnxBsxCflowdStatusHCFlowsNoRes_Type = Counter64
_TmnxBsxCflowdStatusHCFlowsNoRes_Object = MibTableColumn
tmnxBsxCflowdStatusHCFlowsNoRes = _TmnxBsxCflowdStatusHCFlowsNoRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 12),
    _TmnxBsxCflowdStatusHCFlowsNoRes_Type()
)
tmnxBsxCflowdStatusHCFlowsNoRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusHCFlowsNoRes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusHCFlowsNoRes.setUnits("flows")
_TmnxBsxCflowdStatusHCUSupSSRCSt_Type = Counter64
_TmnxBsxCflowdStatusHCUSupSSRCSt_Object = MibTableColumn
tmnxBsxCflowdStatusHCUSupSSRCSt = _TmnxBsxCflowdStatusHCUSupSSRCSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 13),
    _TmnxBsxCflowdStatusHCUSupSSRCSt_Type()
)
tmnxBsxCflowdStatusHCUSupSSRCSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusHCUSupSSRCSt.setStatus("current")
_TmnxBsxCflowdStatusUSupSSRCStLo_Type = Counter32
_TmnxBsxCflowdStatusUSupSSRCStLo_Object = MibTableColumn
tmnxBsxCflowdStatusUSupSSRCStLo = _TmnxBsxCflowdStatusUSupSSRCStLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 14),
    _TmnxBsxCflowdStatusUSupSSRCStLo_Type()
)
tmnxBsxCflowdStatusUSupSSRCStLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusUSupSSRCStLo.setStatus("current")
_TmnxBsxCflowdStatusUSupSSRCStHi_Type = Counter32
_TmnxBsxCflowdStatusUSupSSRCStHi_Object = MibTableColumn
tmnxBsxCflowdStatusUSupSSRCStHi = _TmnxBsxCflowdStatusUSupSSRCStHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 7, 1, 15),
    _TmnxBsxCflowdStatusUSupSSRCStHi_Type()
)
tmnxBsxCflowdStatusUSupSSRCStHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdStatusUSupSSRCStHi.setStatus("current")
_TmnxBsxCflowdCollStatTable_Object = MibTable
tmnxBsxCflowdCollStatTable = _TmnxBsxCflowdCollStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 8)
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollStatTable.setStatus("current")
_TmnxBsxCflowdCollStatEntry_Object = MibTableRow
tmnxBsxCflowdCollStatEntry = _TmnxBsxCflowdCollStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 8, 1)
)
tmnxBsxCflowdCollStatEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollAddressType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollAddress"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollPort"),
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollStatEntry.setStatus("current")
_TmnxBsxCflowdCollStatDiscontTime_Type = TimeStamp
_TmnxBsxCflowdCollStatDiscontTime_Object = MibTableColumn
tmnxBsxCflowdCollStatDiscontTime = _TmnxBsxCflowdCollStatDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 8, 1, 1),
    _TmnxBsxCflowdCollStatDiscontTime_Type()
)
tmnxBsxCflowdCollStatDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollStatDiscontTime.setStatus("current")
_TmnxBsxCflowdCollStatRecSent_Type = Counter32
_TmnxBsxCflowdCollStatRecSent_Object = MibTableColumn
tmnxBsxCflowdCollStatRecSent = _TmnxBsxCflowdCollStatRecSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 8, 1, 2),
    _TmnxBsxCflowdCollStatRecSent_Type()
)
tmnxBsxCflowdCollStatRecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollStatRecSent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollStatRecSent.setUnits("records")
_TmnxBsxCflowdCollStatHCRecSent_Type = Counter64
_TmnxBsxCflowdCollStatHCRecSent_Object = MibTableColumn
tmnxBsxCflowdCollStatHCRecSent = _TmnxBsxCflowdCollStatHCRecSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 8, 1, 3),
    _TmnxBsxCflowdCollStatHCRecSent_Type()
)
tmnxBsxCflowdCollStatHCRecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollStatHCRecSent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdCollStatHCRecSent.setUnits("records")
_TmnxBsxCflowdExpStatTable_Object = MibTable
tmnxBsxCflowdExpStatTable = _TmnxBsxCflowdExpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9)
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatTable.setStatus("current")
_TmnxBsxCflowdExpStatEntry_Object = MibTableRow
tmnxBsxCflowdExpStatEntry = _TmnxBsxCflowdExpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1)
)
tmnxBsxCflowdExpStatEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpType"),
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatEntry.setStatus("current")
_TmnxBsxCflowdExpStatDiscontTime_Type = TimeStamp
_TmnxBsxCflowdExpStatDiscontTime_Object = MibTableColumn
tmnxBsxCflowdExpStatDiscontTime = _TmnxBsxCflowdExpStatDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1, 1),
    _TmnxBsxCflowdExpStatDiscontTime_Type()
)
tmnxBsxCflowdExpStatDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatDiscontTime.setStatus("current")
_TmnxBsxCflowdExpStatRecReport_Type = Counter32
_TmnxBsxCflowdExpStatRecReport_Object = MibTableColumn
tmnxBsxCflowdExpStatRecReport = _TmnxBsxCflowdExpStatRecReport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1, 2),
    _TmnxBsxCflowdExpStatRecReport_Type()
)
tmnxBsxCflowdExpStatRecReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatRecReport.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatRecReport.setUnits("records")
_TmnxBsxCflowdExpStatHCRecReport_Type = Counter64
_TmnxBsxCflowdExpStatHCRecReport_Object = MibTableColumn
tmnxBsxCflowdExpStatHCRecReport = _TmnxBsxCflowdExpStatHCRecReport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1, 3),
    _TmnxBsxCflowdExpStatHCRecReport_Type()
)
tmnxBsxCflowdExpStatHCRecReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatHCRecReport.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatHCRecReport.setUnits("records")
_TmnxBsxCflowdExpStatRecDropped_Type = Counter32
_TmnxBsxCflowdExpStatRecDropped_Object = MibTableColumn
tmnxBsxCflowdExpStatRecDropped = _TmnxBsxCflowdExpStatRecDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1, 4),
    _TmnxBsxCflowdExpStatRecDropped_Type()
)
tmnxBsxCflowdExpStatRecDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatRecDropped.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatRecDropped.setUnits("records")
_TmnxBsxCflowdExpStatHCRecDropped_Type = Counter64
_TmnxBsxCflowdExpStatHCRecDropped_Object = MibTableColumn
tmnxBsxCflowdExpStatHCRecDropped = _TmnxBsxCflowdExpStatHCRecDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1, 5),
    _TmnxBsxCflowdExpStatHCRecDropped_Type()
)
tmnxBsxCflowdExpStatHCRecDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatHCRecDropped.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatHCRecDropped.setUnits("records")
_TmnxBsxCflowdExpStatFlowsNoRes_Type = Counter32
_TmnxBsxCflowdExpStatFlowsNoRes_Object = MibTableColumn
tmnxBsxCflowdExpStatFlowsNoRes = _TmnxBsxCflowdExpStatFlowsNoRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1, 6),
    _TmnxBsxCflowdExpStatFlowsNoRes_Type()
)
tmnxBsxCflowdExpStatFlowsNoRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatFlowsNoRes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatFlowsNoRes.setUnits("flows")
_TmnxBsxCflowdExpStatHCFlowsNoRes_Type = Counter64
_TmnxBsxCflowdExpStatHCFlowsNoRes_Object = MibTableColumn
tmnxBsxCflowdExpStatHCFlowsNoRes = _TmnxBsxCflowdExpStatHCFlowsNoRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1, 7),
    _TmnxBsxCflowdExpStatHCFlowsNoRes_Type()
)
tmnxBsxCflowdExpStatHCFlowsNoRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatHCFlowsNoRes.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatHCFlowsNoRes.setUnits("flows")
_TmnxBsxCflowdExpStatHCUSupSSRCSt_Type = Counter64
_TmnxBsxCflowdExpStatHCUSupSSRCSt_Object = MibTableColumn
tmnxBsxCflowdExpStatHCUSupSSRCSt = _TmnxBsxCflowdExpStatHCUSupSSRCSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1, 8),
    _TmnxBsxCflowdExpStatHCUSupSSRCSt_Type()
)
tmnxBsxCflowdExpStatHCUSupSSRCSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatHCUSupSSRCSt.setStatus("current")
_TmnxBsxCflowdExpStatUSupSSRCStLo_Type = Counter32
_TmnxBsxCflowdExpStatUSupSSRCStLo_Object = MibTableColumn
tmnxBsxCflowdExpStatUSupSSRCStLo = _TmnxBsxCflowdExpStatUSupSSRCStLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1, 9),
    _TmnxBsxCflowdExpStatUSupSSRCStLo_Type()
)
tmnxBsxCflowdExpStatUSupSSRCStLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatUSupSSRCStLo.setStatus("current")
_TmnxBsxCflowdExpStatUSupSSRCStHi_Type = Counter32
_TmnxBsxCflowdExpStatUSupSSRCStHi_Object = MibTableColumn
tmnxBsxCflowdExpStatUSupSSRCStHi = _TmnxBsxCflowdExpStatUSupSSRCStHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 5, 9, 1, 10),
    _TmnxBsxCflowdExpStatUSupSSRCStHi_Type()
)
tmnxBsxCflowdExpStatUSupSSRCStHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxCflowdExpStatUSupSSRCStHi.setStatus("current")
_TmnxBsxOvrdObjs_ObjectIdentity = ObjectIdentity
tmnxBsxOvrdObjs = _TmnxBsxOvrdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6)
)
_TmnxBsxOvrdScalars_ObjectIdentity = ObjectIdentity
tmnxBsxOvrdScalars = _TmnxBsxOvrdScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 1)
)
_TmnxBsxOvrdAaSubLastChTime_Type = TimeStamp
_TmnxBsxOvrdAaSubLastChTime_Object = MibScalar
tmnxBsxOvrdAaSubLastChTime = _TmnxBsxOvrdAaSubLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 1, 1),
    _TmnxBsxOvrdAaSubLastChTime_Type()
)
tmnxBsxOvrdAaSubLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubLastChTime.setStatus("current")
_TmnxBsxOvrdAaSubCharLastChTm_Type = TimeStamp
_TmnxBsxOvrdAaSubCharLastChTm_Object = MibScalar
tmnxBsxOvrdAaSubCharLastChTm = _TmnxBsxOvrdAaSubCharLastChTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 1, 2),
    _TmnxBsxOvrdAaSubCharLastChTm_Type()
)
tmnxBsxOvrdAaSubCharLastChTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubCharLastChTm.setStatus("current")
_TmnxBsxOvrdAaSubTable_Object = MibTable
tmnxBsxOvrdAaSubTable = _TmnxBsxOvrdAaSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubTable.setStatus("current")
_TmnxBsxOvrdAaSubEntry_Object = MibTableRow
tmnxBsxOvrdAaSubEntry = _TmnxBsxOvrdAaSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 2, 1)
)
tmnxBsxOvrdAaSubEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriber"),
)
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubEntry.setStatus("current")
_TmnxBsxOvrdAaSubRowStatus_Type = RowStatus
_TmnxBsxOvrdAaSubRowStatus_Object = MibTableColumn
tmnxBsxOvrdAaSubRowStatus = _TmnxBsxOvrdAaSubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 2, 1, 1),
    _TmnxBsxOvrdAaSubRowStatus_Type()
)
tmnxBsxOvrdAaSubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubRowStatus.setStatus("current")
_TmnxBsxOvrdAaSubRowLastCh_Type = TimeStamp
_TmnxBsxOvrdAaSubRowLastCh_Object = MibTableColumn
tmnxBsxOvrdAaSubRowLastCh = _TmnxBsxOvrdAaSubRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 2, 1, 2),
    _TmnxBsxOvrdAaSubRowLastCh_Type()
)
tmnxBsxOvrdAaSubRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubRowLastCh.setStatus("current")
_TmnxBsxOvrdAaSubCharTable_Object = MibTable
tmnxBsxOvrdAaSubCharTable = _TmnxBsxOvrdAaSubCharTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubCharTable.setStatus("current")
_TmnxBsxOvrdAaSubCharEntry_Object = MibTableRow
tmnxBsxOvrdAaSubCharEntry = _TmnxBsxOvrdAaSubCharEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 3, 1)
)
tmnxBsxOvrdAaSubCharEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriber"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxAsoCharName"),
)
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubCharEntry.setStatus("current")
_TmnxBsxOvrdAaSubCharRowStatus_Type = RowStatus
_TmnxBsxOvrdAaSubCharRowStatus_Object = MibTableColumn
tmnxBsxOvrdAaSubCharRowStatus = _TmnxBsxOvrdAaSubCharRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 3, 1, 1),
    _TmnxBsxOvrdAaSubCharRowStatus_Type()
)
tmnxBsxOvrdAaSubCharRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubCharRowStatus.setStatus("current")
_TmnxBsxOvrdAaSubCharRowLastCh_Type = TimeStamp
_TmnxBsxOvrdAaSubCharRowLastCh_Object = MibTableColumn
tmnxBsxOvrdAaSubCharRowLastCh = _TmnxBsxOvrdAaSubCharRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 3, 1, 2),
    _TmnxBsxOvrdAaSubCharRowLastCh_Type()
)
tmnxBsxOvrdAaSubCharRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubCharRowLastCh.setStatus("current")
_TmnxBsxOvrdAaSubCharValName_Type = TNamedItem
_TmnxBsxOvrdAaSubCharValName_Object = MibTableColumn
tmnxBsxOvrdAaSubCharValName = _TmnxBsxOvrdAaSubCharValName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 6, 3, 1, 3),
    _TmnxBsxOvrdAaSubCharValName_Type()
)
tmnxBsxOvrdAaSubCharValName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxOvrdAaSubCharValName.setStatus("current")
_TmnxBsxTransitObjs_ObjectIdentity = ObjectIdentity
tmnxBsxTransitObjs = _TmnxBsxTransitObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7)
)
_TmnxBsxTransitScalars_ObjectIdentity = ObjectIdentity
tmnxBsxTransitScalars = _TmnxBsxTransitScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 1)
)
_TmnxBsxTransitIpPolicyLastChTime_Type = TimeStamp
_TmnxBsxTransitIpPolicyLastChTime_Object = MibScalar
tmnxBsxTransitIpPolicyLastChTime = _TmnxBsxTransitIpPolicyLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 1, 1),
    _TmnxBsxTransitIpPolicyLastChTime_Type()
)
tmnxBsxTransitIpPolicyLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyLastChTime.setStatus("current")
_TmnxBsxTransIpPlcySubLastChTime_Type = TimeStamp
_TmnxBsxTransIpPlcySubLastChTime_Object = MibScalar
tmnxBsxTransIpPlcySubLastChTime = _TmnxBsxTransIpPlcySubLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 1, 2),
    _TmnxBsxTransIpPlcySubLastChTime_Type()
)
tmnxBsxTransIpPlcySubLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransIpPlcySubLastChTime.setStatus("current")
_TmnxBsxTransIpPlcyAddrLastChTime_Type = TimeStamp
_TmnxBsxTransIpPlcyAddrLastChTime_Object = MibScalar
tmnxBsxTransIpPlcyAddrLastChTime = _TmnxBsxTransIpPlcyAddrLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 1, 3),
    _TmnxBsxTransIpPlcyAddrLastChTime_Type()
)
tmnxBsxTransIpPlcyAddrLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransIpPlcyAddrLastChTime.setStatus("current")
_TmnxBsxTransPrefPlcyLastChTime_Type = TimeStamp
_TmnxBsxTransPrefPlcyLastChTime_Object = MibScalar
tmnxBsxTransPrefPlcyLastChTime = _TmnxBsxTransPrefPlcyLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 1, 4),
    _TmnxBsxTransPrefPlcyLastChTime_Type()
)
tmnxBsxTransPrefPlcyLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPlcyLastChTime.setStatus("current")
_TmnxBsxTransPrefSubLastChTime_Type = TimeStamp
_TmnxBsxTransPrefSubLastChTime_Object = MibScalar
tmnxBsxTransPrefSubLastChTime = _TmnxBsxTransPrefSubLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 1, 5),
    _TmnxBsxTransPrefSubLastChTime_Type()
)
tmnxBsxTransPrefSubLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSubLastChTime.setStatus("current")
_TmnxBsxTransPrefEntryLastChTime_Type = TimeStamp
_TmnxBsxTransPrefEntryLastChTime_Object = MibScalar
tmnxBsxTransPrefEntryLastChTime = _TmnxBsxTransPrefEntryLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 1, 6),
    _TmnxBsxTransPrefEntryLastChTime_Type()
)
tmnxBsxTransPrefEntryLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntryLastChTime.setStatus("current")
_TmnxBsxTransitIpPolicyTable_Object = MibTable
tmnxBsxTransitIpPolicyTable = _TmnxBsxTransitIpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyTable.setStatus("current")
_TmnxBsxTransitIpPolicyEntry_Object = MibTableRow
tmnxBsxTransitIpPolicyEntry = _TmnxBsxTransitIpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1)
)
tmnxBsxTransitIpPolicyEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyEntry.setStatus("current")
_TmnxBsxTransitIpPolicyId_Type = TmnxBsxTransitIpPolicyId
_TmnxBsxTransitIpPolicyId_Object = MibTableColumn
tmnxBsxTransitIpPolicyId = _TmnxBsxTransitIpPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 1),
    _TmnxBsxTransitIpPolicyId_Type()
)
tmnxBsxTransitIpPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyId.setStatus("current")
_TmnxBsxTransitIpPolicyRowStatus_Type = RowStatus
_TmnxBsxTransitIpPolicyRowStatus_Object = MibTableColumn
tmnxBsxTransitIpPolicyRowStatus = _TmnxBsxTransitIpPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 2),
    _TmnxBsxTransitIpPolicyRowStatus_Type()
)
tmnxBsxTransitIpPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyRowStatus.setStatus("current")
_TmnxBsxTransitIpPolicyRowLastCh_Type = TimeStamp
_TmnxBsxTransitIpPolicyRowLastCh_Object = MibTableColumn
tmnxBsxTransitIpPolicyRowLastCh = _TmnxBsxTransitIpPolicyRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 3),
    _TmnxBsxTransitIpPolicyRowLastCh_Type()
)
tmnxBsxTransitIpPolicyRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyRowLastCh.setStatus("current")
_TmnxBsxTransitIpPolicyDesc_Type = TItemDescription
_TmnxBsxTransitIpPolicyDesc_Object = MibTableColumn
tmnxBsxTransitIpPolicyDesc = _TmnxBsxTransitIpPolicyDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 4),
    _TmnxBsxTransitIpPolicyDesc_Type()
)
tmnxBsxTransitIpPolicyDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyDesc.setStatus("current")
_TmnxBsxTransitIpPolicyDefAppProf_Type = TNamedItemOrEmpty
_TmnxBsxTransitIpPolicyDefAppProf_Object = MibTableColumn
tmnxBsxTransitIpPolicyDefAppProf = _TmnxBsxTransitIpPolicyDefAppProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 5),
    _TmnxBsxTransitIpPolicyDefAppProf_Type()
)
tmnxBsxTransitIpPolicyDefAppProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyDefAppProf.setStatus("current")
_TmnxBsxTransitIpPolicySubIdPlcy_Type = TNamedItemOrEmpty
_TmnxBsxTransitIpPolicySubIdPlcy_Object = MibTableColumn
tmnxBsxTransitIpPolicySubIdPlcy = _TmnxBsxTransitIpPolicySubIdPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 6),
    _TmnxBsxTransitIpPolicySubIdPlcy_Type()
)
tmnxBsxTransitIpPolicySubIdPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicySubIdPlcy.setStatus("current")


class _TmnxBsxTransitIpPolicyRadius_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxTransitIpPolicyRadius based on TmnxEnabledDisabled"""


_TmnxBsxTransitIpPolicyRadius_Object = MibTableColumn
tmnxBsxTransitIpPolicyRadius = _TmnxBsxTransitIpPolicyRadius_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 7),
    _TmnxBsxTransitIpPolicyRadius_Type()
)
tmnxBsxTransitIpPolicyRadius.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyRadius.setStatus("current")
_TmnxBsxTransitIpPolicyRadAuthPlc_Type = TNamedItemOrEmpty
_TmnxBsxTransitIpPolicyRadAuthPlc_Object = MibTableColumn
tmnxBsxTransitIpPolicyRadAuthPlc = _TmnxBsxTransitIpPolicyRadAuthPlc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 8),
    _TmnxBsxTransitIpPolicyRadAuthPlc_Type()
)
tmnxBsxTransitIpPolicyRadAuthPlc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyRadAuthPlc.setStatus("current")


class _TmnxBsxTransitIpPolicyDhcp_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxTransitIpPolicyDhcp based on TmnxEnabledDisabled"""


_TmnxBsxTransitIpPolicyDhcp_Object = MibTableColumn
tmnxBsxTransitIpPolicyDhcp = _TmnxBsxTransitIpPolicyDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 9),
    _TmnxBsxTransitIpPolicyDhcp_Type()
)
tmnxBsxTransitIpPolicyDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyDhcp.setStatus("current")


class _TmnxBsxTransitIpPolicyIPv6PfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxBsxTransitIpPolicyIPv6PfxLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxBsxTransitIpPolicyIPv6PfxLen_Object = MibTableColumn
tmnxBsxTransitIpPolicyIPv6PfxLen = _TmnxBsxTransitIpPolicyIPv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 10),
    _TmnxBsxTransitIpPolicyIPv6PfxLen_Type()
)
tmnxBsxTransitIpPolicyIPv6PfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyIPv6PfxLen.setStatus("current")
_TmnxBsxTransitIpPolicySubsCount_Type = Counter32
_TmnxBsxTransitIpPolicySubsCount_Object = MibTableColumn
tmnxBsxTransitIpPolicySubsCount = _TmnxBsxTransitIpPolicySubsCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 11),
    _TmnxBsxTransitIpPolicySubsCount_Type()
)
tmnxBsxTransitIpPolicySubsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicySubsCount.setStatus("current")
_TmnxBsxTransitIpPolicyIPv4EntCnt_Type = Counter32
_TmnxBsxTransitIpPolicyIPv4EntCnt_Object = MibTableColumn
tmnxBsxTransitIpPolicyIPv4EntCnt = _TmnxBsxTransitIpPolicyIPv4EntCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 12),
    _TmnxBsxTransitIpPolicyIPv4EntCnt_Type()
)
tmnxBsxTransitIpPolicyIPv4EntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyIPv4EntCnt.setStatus("current")
_TmnxBsxTransitIpPolicyIPv6EntCnt_Type = Counter32
_TmnxBsxTransitIpPolicyIPv6EntCnt_Object = MibTableColumn
tmnxBsxTransitIpPolicyIPv6EntCnt = _TmnxBsxTransitIpPolicyIPv6EntCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 13),
    _TmnxBsxTransitIpPolicyIPv6EntCnt_Type()
)
tmnxBsxTransitIpPolicyIPv6EntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyIPv6EntCnt.setStatus("current")


class _TmnxBsxTransitIpPolicySeenIp_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxTransitIpPolicySeenIp based on TmnxEnabledDisabled"""


_TmnxBsxTransitIpPolicySeenIp_Object = MibTableColumn
tmnxBsxTransitIpPolicySeenIp = _TmnxBsxTransitIpPolicySeenIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 14),
    _TmnxBsxTransitIpPolicySeenIp_Type()
)
tmnxBsxTransitIpPolicySeenIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicySeenIp.setStatus("current")


class _TmnxBsxTransitIpPolicyAutoCreate_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxTransitIpPolicyAutoCreate based on TmnxEnabledDisabled"""


_TmnxBsxTransitIpPolicyAutoCreate_Object = MibTableColumn
tmnxBsxTransitIpPolicyAutoCreate = _TmnxBsxTransitIpPolicyAutoCreate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 15),
    _TmnxBsxTransitIpPolicyAutoCreate_Type()
)
tmnxBsxTransitIpPolicyAutoCreate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyAutoCreate.setStatus("current")
_TmnxBsxTransitIpPolicySeenIpRad_Type = TNamedItemOrEmpty
_TmnxBsxTransitIpPolicySeenIpRad_Object = MibTableColumn
tmnxBsxTransitIpPolicySeenIpRad = _TmnxBsxTransitIpPolicySeenIpRad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 2, 1, 16),
    _TmnxBsxTransitIpPolicySeenIpRad_Type()
)
tmnxBsxTransitIpPolicySeenIpRad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicySeenIpRad.setStatus("current")
_TmnxBsxTransitIpPolicySubTable_Object = MibTable
tmnxBsxTransitIpPolicySubTable = _TmnxBsxTransitIpPolicySubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicySubTable.setStatus("current")
_TmnxBsxTransitIpPolicySubEntry_Object = MibTableRow
tmnxBsxTransitIpPolicySubEntry = _TmnxBsxTransitIpPolicySubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 3, 1)
)
tmnxBsxTransitIpPolicySubEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyId"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicySubscriber"),
)
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicySubEntry.setStatus("current")
_TmnxBsxTransitIpPolicySubscriber_Type = TNamedItem
_TmnxBsxTransitIpPolicySubscriber_Object = MibTableColumn
tmnxBsxTransitIpPolicySubscriber = _TmnxBsxTransitIpPolicySubscriber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 3, 1, 1),
    _TmnxBsxTransitIpPolicySubscriber_Type()
)
tmnxBsxTransitIpPolicySubscriber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicySubscriber.setStatus("current")
_TmnxBsxTransIpPlcySubRowStatus_Type = RowStatus
_TmnxBsxTransIpPlcySubRowStatus_Object = MibTableColumn
tmnxBsxTransIpPlcySubRowStatus = _TmnxBsxTransIpPlcySubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 3, 1, 2),
    _TmnxBsxTransIpPlcySubRowStatus_Type()
)
tmnxBsxTransIpPlcySubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransIpPlcySubRowStatus.setStatus("current")
_TmnxBsxTransIpPlcySubRowLastCh_Type = TimeStamp
_TmnxBsxTransIpPlcySubRowLastCh_Object = MibTableColumn
tmnxBsxTransIpPlcySubRowLastCh = _TmnxBsxTransIpPlcySubRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 3, 1, 3),
    _TmnxBsxTransIpPlcySubRowLastCh_Type()
)
tmnxBsxTransIpPlcySubRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransIpPlcySubRowLastCh.setStatus("current")
_TmnxBsxTransIpPlcySubAppProfNm_Type = TNamedItem
_TmnxBsxTransIpPlcySubAppProfNm_Object = MibTableColumn
tmnxBsxTransIpPlcySubAppProfNm = _TmnxBsxTransIpPlcySubAppProfNm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 3, 1, 4),
    _TmnxBsxTransIpPlcySubAppProfNm_Type()
)
tmnxBsxTransIpPlcySubAppProfNm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransIpPlcySubAppProfNm.setStatus("current")


class _TmnxBsxTransIpPlcySubRefCount_Type(Unsigned32):
    """Custom type tmnxBsxTransIpPlcySubRefCount based on Unsigned32"""
    defaultValue = 0


_TmnxBsxTransIpPlcySubRefCount_Object = MibTableColumn
tmnxBsxTransIpPlcySubRefCount = _TmnxBsxTransIpPlcySubRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 3, 1, 5),
    _TmnxBsxTransIpPlcySubRefCount_Type()
)
tmnxBsxTransIpPlcySubRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransIpPlcySubRefCount.setStatus("current")
_TmnxBsxTransitIpPolicyAddrTable_Object = MibTable
tmnxBsxTransitIpPolicyAddrTable = _TmnxBsxTransitIpPolicyAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyAddrTable.setStatus("current")
_TmnxBsxTransitIpPolicyAddrEntry_Object = MibTableRow
tmnxBsxTransitIpPolicyAddrEntry = _TmnxBsxTransitIpPolicyAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 4, 1)
)
tmnxBsxTransitIpPolicyAddrEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyId"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyAddrType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyAddr"),
)
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyAddrEntry.setStatus("current")
_TmnxBsxTransitIpPolicyAddrType_Type = InetAddressType
_TmnxBsxTransitIpPolicyAddrType_Object = MibTableColumn
tmnxBsxTransitIpPolicyAddrType = _TmnxBsxTransitIpPolicyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 4, 1, 1),
    _TmnxBsxTransitIpPolicyAddrType_Type()
)
tmnxBsxTransitIpPolicyAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyAddrType.setStatus("current")


class _TmnxBsxTransitIpPolicyAddr_Type(InetAddress):
    """Custom type tmnxBsxTransitIpPolicyAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxTransitIpPolicyAddr_Type.__name__ = "InetAddress"
_TmnxBsxTransitIpPolicyAddr_Object = MibTableColumn
tmnxBsxTransitIpPolicyAddr = _TmnxBsxTransitIpPolicyAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 4, 1, 2),
    _TmnxBsxTransitIpPolicyAddr_Type()
)
tmnxBsxTransitIpPolicyAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPolicyAddr.setStatus("current")
_TmnxBsxTransIpPlcyAddrRowStatus_Type = RowStatus
_TmnxBsxTransIpPlcyAddrRowStatus_Object = MibTableColumn
tmnxBsxTransIpPlcyAddrRowStatus = _TmnxBsxTransIpPlcyAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 4, 1, 3),
    _TmnxBsxTransIpPlcyAddrRowStatus_Type()
)
tmnxBsxTransIpPlcyAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransIpPlcyAddrRowStatus.setStatus("current")
_TmnxBsxTransIpPlcyAddrRowLastCh_Type = TimeStamp
_TmnxBsxTransIpPlcyAddrRowLastCh_Object = MibTableColumn
tmnxBsxTransIpPlcyAddrRowLastCh = _TmnxBsxTransIpPlcyAddrRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 4, 1, 4),
    _TmnxBsxTransIpPlcyAddrRowLastCh_Type()
)
tmnxBsxTransIpPlcyAddrRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransIpPlcyAddrRowLastCh.setStatus("current")
_TmnxBsxTransIpPlcyAddrSubscriber_Type = TNamedItem
_TmnxBsxTransIpPlcyAddrSubscriber_Object = MibTableColumn
tmnxBsxTransIpPlcyAddrSubscriber = _TmnxBsxTransIpPlcyAddrSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 4, 1, 5),
    _TmnxBsxTransIpPlcyAddrSubscriber_Type()
)
tmnxBsxTransIpPlcyAddrSubscriber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransIpPlcyAddrSubscriber.setStatus("current")
_TmnxBsxTransitIpSumTable_Object = MibTable
tmnxBsxTransitIpSumTable = _TmnxBsxTransitIpSumTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 5)
)
if mibBuilder.loadTexts:
    tmnxBsxTransitIpSumTable.setStatus("current")
_TmnxBsxTransitIpSumEntry_Object = MibTableRow
tmnxBsxTransitIpSumEntry = _TmnxBsxTransitIpSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 5, 1)
)
tmnxBsxTransitIpSumEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyId"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicySubscriber"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyAddrType"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyAddr"),
)
if mibBuilder.loadTexts:
    tmnxBsxTransitIpSumEntry.setStatus("current")
_TmnxBsxTransitIpSumUpdateTime_Type = TimeStamp
_TmnxBsxTransitIpSumUpdateTime_Object = MibTableColumn
tmnxBsxTransitIpSumUpdateTime = _TmnxBsxTransitIpSumUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 5, 1, 1),
    _TmnxBsxTransitIpSumUpdateTime_Type()
)
tmnxBsxTransitIpSumUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpSumUpdateTime.setStatus("current")
_TmnxBsxTransitIpSumParentSubType_Type = TmnxBsxAaSubscriberType
_TmnxBsxTransitIpSumParentSubType_Object = MibTableColumn
tmnxBsxTransitIpSumParentSubType = _TmnxBsxTransitIpSumParentSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 5, 1, 2),
    _TmnxBsxTransitIpSumParentSubType_Type()
)
tmnxBsxTransitIpSumParentSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpSumParentSubType.setStatus("current")
_TmnxBsxTransitIpSumParentSub_Type = TmnxBsxAaSubscriber
_TmnxBsxTransitIpSumParentSub_Object = MibTableColumn
tmnxBsxTransitIpSumParentSub = _TmnxBsxTransitIpSumParentSub_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 5, 1, 3),
    _TmnxBsxTransitIpSumParentSub_Type()
)
tmnxBsxTransitIpSumParentSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpSumParentSub.setStatus("current")
_TmnxBsxTransitIpSumAppProfNm_Type = TNamedItem
_TmnxBsxTransitIpSumAppProfNm_Object = MibTableColumn
tmnxBsxTransitIpSumAppProfNm = _TmnxBsxTransitIpSumAppProfNm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 5, 1, 4),
    _TmnxBsxTransitIpSumAppProfNm_Type()
)
tmnxBsxTransitIpSumAppProfNm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpSumAppProfNm.setStatus("current")
_TmnxBsxTransitIpSumIpOriginMask_Type = TmnxBsxTransitSubOrigin
_TmnxBsxTransitIpSumIpOriginMask_Object = MibTableColumn
tmnxBsxTransitIpSumIpOriginMask = _TmnxBsxTransitIpSumIpOriginMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 5, 1, 5),
    _TmnxBsxTransitIpSumIpOriginMask_Type()
)
tmnxBsxTransitIpSumIpOriginMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransitIpSumIpOriginMask.setStatus("current")
_TmnxBsxTransPrefPolicyTable_Object = MibTable
tmnxBsxTransPrefPolicyTable = _TmnxBsxTransPrefPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 6)
)
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPolicyTable.setStatus("current")
_TmnxBsxTransPrefPolicyEntry_Object = MibTableRow
tmnxBsxTransPrefPolicyEntry = _TmnxBsxTransPrefPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 6, 1)
)
tmnxBsxTransPrefPolicyEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPolicyEntry.setStatus("current")
_TmnxBsxTransPrefPolicyId_Type = TmnxBsxTransPrefPolicyId
_TmnxBsxTransPrefPolicyId_Object = MibTableColumn
tmnxBsxTransPrefPolicyId = _TmnxBsxTransPrefPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 6, 1, 1),
    _TmnxBsxTransPrefPolicyId_Type()
)
tmnxBsxTransPrefPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPolicyId.setStatus("current")
_TmnxBsxTransPrefPolicyRowStatus_Type = RowStatus
_TmnxBsxTransPrefPolicyRowStatus_Object = MibTableColumn
tmnxBsxTransPrefPolicyRowStatus = _TmnxBsxTransPrefPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 6, 1, 2),
    _TmnxBsxTransPrefPolicyRowStatus_Type()
)
tmnxBsxTransPrefPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPolicyRowStatus.setStatus("current")
_TmnxBsxTransPrefPolicyRowLastCh_Type = TimeStamp
_TmnxBsxTransPrefPolicyRowLastCh_Object = MibTableColumn
tmnxBsxTransPrefPolicyRowLastCh = _TmnxBsxTransPrefPolicyRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 6, 1, 3),
    _TmnxBsxTransPrefPolicyRowLastCh_Type()
)
tmnxBsxTransPrefPolicyRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPolicyRowLastCh.setStatus("current")
_TmnxBsxTransPrefPolicyDesc_Type = TItemDescription
_TmnxBsxTransPrefPolicyDesc_Object = MibTableColumn
tmnxBsxTransPrefPolicyDesc = _TmnxBsxTransPrefPolicyDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 6, 1, 4),
    _TmnxBsxTransPrefPolicyDesc_Type()
)
tmnxBsxTransPrefPolicyDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPolicyDesc.setStatus("current")
_TmnxBsxTransPrefPolicySubsCount_Type = Counter32
_TmnxBsxTransPrefPolicySubsCount_Object = MibTableColumn
tmnxBsxTransPrefPolicySubsCount = _TmnxBsxTransPrefPolicySubsCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 6, 1, 5),
    _TmnxBsxTransPrefPolicySubsCount_Type()
)
tmnxBsxTransPrefPolicySubsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPolicySubsCount.setStatus("current")
_TmnxBsxTransPrefPolicyEntCount_Type = Counter32
_TmnxBsxTransPrefPolicyEntCount_Object = MibTableColumn
tmnxBsxTransPrefPolicyEntCount = _TmnxBsxTransPrefPolicyEntCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 6, 1, 6),
    _TmnxBsxTransPrefPolicyEntCount_Type()
)
tmnxBsxTransPrefPolicyEntCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPolicyEntCount.setStatus("current")
_TmnxBsxTransPrefPolicyIPv4EntCnt_Type = Counter32
_TmnxBsxTransPrefPolicyIPv4EntCnt_Object = MibTableColumn
tmnxBsxTransPrefPolicyIPv4EntCnt = _TmnxBsxTransPrefPolicyIPv4EntCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 6, 1, 7),
    _TmnxBsxTransPrefPolicyIPv4EntCnt_Type()
)
tmnxBsxTransPrefPolicyIPv4EntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPolicyIPv4EntCnt.setStatus("current")
_TmnxBsxTransPrefPolicyIPv6EntCnt_Type = Counter32
_TmnxBsxTransPrefPolicyIPv6EntCnt_Object = MibTableColumn
tmnxBsxTransPrefPolicyIPv6EntCnt = _TmnxBsxTransPrefPolicyIPv6EntCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 6, 1, 8),
    _TmnxBsxTransPrefPolicyIPv6EntCnt_Type()
)
tmnxBsxTransPrefPolicyIPv6EntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefPolicyIPv6EntCnt.setStatus("current")
_TmnxBsxTransPrefSubTable_Object = MibTable
tmnxBsxTransPrefSubTable = _TmnxBsxTransPrefSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 7)
)
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSubTable.setStatus("current")
_TmnxBsxTransPrefSubEntry_Object = MibTableRow
tmnxBsxTransPrefSubEntry = _TmnxBsxTransPrefSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 7, 1)
)
tmnxBsxTransPrefSubEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicyId"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSubscriber"),
)
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSubEntry.setStatus("current")
_TmnxBsxTransPrefSubscriber_Type = TNamedItem
_TmnxBsxTransPrefSubscriber_Object = MibTableColumn
tmnxBsxTransPrefSubscriber = _TmnxBsxTransPrefSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 7, 1, 1),
    _TmnxBsxTransPrefSubscriber_Type()
)
tmnxBsxTransPrefSubscriber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSubscriber.setStatus("current")
_TmnxBsxTransPrefSubRowStatus_Type = RowStatus
_TmnxBsxTransPrefSubRowStatus_Object = MibTableColumn
tmnxBsxTransPrefSubRowStatus = _TmnxBsxTransPrefSubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 7, 1, 2),
    _TmnxBsxTransPrefSubRowStatus_Type()
)
tmnxBsxTransPrefSubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSubRowStatus.setStatus("current")
_TmnxBsxTransPrefSubRowLastCh_Type = TimeStamp
_TmnxBsxTransPrefSubRowLastCh_Object = MibTableColumn
tmnxBsxTransPrefSubRowLastCh = _TmnxBsxTransPrefSubRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 7, 1, 3),
    _TmnxBsxTransPrefSubRowLastCh_Type()
)
tmnxBsxTransPrefSubRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSubRowLastCh.setStatus("current")


class _TmnxBsxTransPrefSubIsRemote_Type(TruthValue):
    """Custom type tmnxBsxTransPrefSubIsRemote based on TruthValue"""


_TmnxBsxTransPrefSubIsRemote_Object = MibTableColumn
tmnxBsxTransPrefSubIsRemote = _TmnxBsxTransPrefSubIsRemote_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 7, 1, 4),
    _TmnxBsxTransPrefSubIsRemote_Type()
)
tmnxBsxTransPrefSubIsRemote.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSubIsRemote.setStatus("current")
_TmnxBsxTransPrefSubAppProfNm_Type = TNamedItem
_TmnxBsxTransPrefSubAppProfNm_Object = MibTableColumn
tmnxBsxTransPrefSubAppProfNm = _TmnxBsxTransPrefSubAppProfNm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 7, 1, 5),
    _TmnxBsxTransPrefSubAppProfNm_Type()
)
tmnxBsxTransPrefSubAppProfNm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSubAppProfNm.setStatus("current")
_TmnxBsxTransPrefSubRefCount_Type = Unsigned32
_TmnxBsxTransPrefSubRefCount_Object = MibTableColumn
tmnxBsxTransPrefSubRefCount = _TmnxBsxTransPrefSubRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 7, 1, 6),
    _TmnxBsxTransPrefSubRefCount_Type()
)
tmnxBsxTransPrefSubRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSubRefCount.setStatus("current")
_TmnxBsxTransPrefTable_Object = MibTable
tmnxBsxTransPrefTable = _TmnxBsxTransPrefTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8)
)
if mibBuilder.loadTexts:
    tmnxBsxTransPrefTable.setStatus("current")
_TmnxBsxTransPrefEntry_Object = MibTableRow
tmnxBsxTransPrefEntry = _TmnxBsxTransPrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1)
)
tmnxBsxTransPrefEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicyId"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntryId"),
)
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntry.setStatus("current")


class _TmnxBsxTransPrefEntryId_Type(Unsigned32):
    """Custom type tmnxBsxTransPrefEntryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxBsxTransPrefEntryId_Type.__name__ = "Unsigned32"
_TmnxBsxTransPrefEntryId_Object = MibTableColumn
tmnxBsxTransPrefEntryId = _TmnxBsxTransPrefEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1, 1),
    _TmnxBsxTransPrefEntryId_Type()
)
tmnxBsxTransPrefEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntryId.setStatus("current")
_TmnxBsxTransPrefEntryRowStatus_Type = RowStatus
_TmnxBsxTransPrefEntryRowStatus_Object = MibTableColumn
tmnxBsxTransPrefEntryRowStatus = _TmnxBsxTransPrefEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1, 2),
    _TmnxBsxTransPrefEntryRowStatus_Type()
)
tmnxBsxTransPrefEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntryRowStatus.setStatus("current")
_TmnxBsxTransPrefEntryRowLastCh_Type = TimeStamp
_TmnxBsxTransPrefEntryRowLastCh_Object = MibTableColumn
tmnxBsxTransPrefEntryRowLastCh = _TmnxBsxTransPrefEntryRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1, 3),
    _TmnxBsxTransPrefEntryRowLastCh_Type()
)
tmnxBsxTransPrefEntryRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntryRowLastCh.setStatus("current")


class _TmnxBsxTransPrefEntrySubAddrType_Type(InetAddressType):
    """Custom type tmnxBsxTransPrefEntrySubAddrType based on InetAddressType"""


_TmnxBsxTransPrefEntrySubAddrType_Object = MibTableColumn
tmnxBsxTransPrefEntrySubAddrType = _TmnxBsxTransPrefEntrySubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1, 4),
    _TmnxBsxTransPrefEntrySubAddrType_Type()
)
tmnxBsxTransPrefEntrySubAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntrySubAddrType.setStatus("current")


class _TmnxBsxTransPrefEntrySubAddr_Type(InetAddress):
    """Custom type tmnxBsxTransPrefEntrySubAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxTransPrefEntrySubAddr_Type.__name__ = "InetAddress"
_TmnxBsxTransPrefEntrySubAddr_Object = MibTableColumn
tmnxBsxTransPrefEntrySubAddr = _TmnxBsxTransPrefEntrySubAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1, 5),
    _TmnxBsxTransPrefEntrySubAddr_Type()
)
tmnxBsxTransPrefEntrySubAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntrySubAddr.setStatus("current")


class _TmnxBsxTransPrefEntrySubAddrLen_Type(InetAddressPrefixLength):
    """Custom type tmnxBsxTransPrefEntrySubAddrLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxBsxTransPrefEntrySubAddrLen_Object = MibTableColumn
tmnxBsxTransPrefEntrySubAddrLen = _TmnxBsxTransPrefEntrySubAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1, 6),
    _TmnxBsxTransPrefEntrySubAddrLen_Type()
)
tmnxBsxTransPrefEntrySubAddrLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntrySubAddrLen.setStatus("current")


class _TmnxBsxTransPrefEntryNetAddrType_Type(InetAddressType):
    """Custom type tmnxBsxTransPrefEntryNetAddrType based on InetAddressType"""


_TmnxBsxTransPrefEntryNetAddrType_Object = MibTableColumn
tmnxBsxTransPrefEntryNetAddrType = _TmnxBsxTransPrefEntryNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1, 7),
    _TmnxBsxTransPrefEntryNetAddrType_Type()
)
tmnxBsxTransPrefEntryNetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntryNetAddrType.setStatus("current")


class _TmnxBsxTransPrefEntryNetAddr_Type(InetAddress):
    """Custom type tmnxBsxTransPrefEntryNetAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxTransPrefEntryNetAddr_Type.__name__ = "InetAddress"
_TmnxBsxTransPrefEntryNetAddr_Object = MibTableColumn
tmnxBsxTransPrefEntryNetAddr = _TmnxBsxTransPrefEntryNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1, 8),
    _TmnxBsxTransPrefEntryNetAddr_Type()
)
tmnxBsxTransPrefEntryNetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntryNetAddr.setStatus("current")


class _TmnxBsxTransPrefEntryNetAddrLen_Type(InetAddressPrefixLength):
    """Custom type tmnxBsxTransPrefEntryNetAddrLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxBsxTransPrefEntryNetAddrLen_Object = MibTableColumn
tmnxBsxTransPrefEntryNetAddrLen = _TmnxBsxTransPrefEntryNetAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1, 9),
    _TmnxBsxTransPrefEntryNetAddrLen_Type()
)
tmnxBsxTransPrefEntryNetAddrLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntryNetAddrLen.setStatus("current")
_TmnxBsxTransPrefEntrySubscriber_Type = TNamedItemOrEmpty
_TmnxBsxTransPrefEntrySubscriber_Object = MibTableColumn
tmnxBsxTransPrefEntrySubscriber = _TmnxBsxTransPrefEntrySubscriber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 8, 1, 10),
    _TmnxBsxTransPrefEntrySubscriber_Type()
)
tmnxBsxTransPrefEntrySubscriber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefEntrySubscriber.setStatus("current")
_TmnxBsxTransPrefSumTable_Object = MibTable
tmnxBsxTransPrefSumTable = _TmnxBsxTransPrefSumTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9)
)
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumTable.setStatus("current")
_TmnxBsxTransPrefSumEntry_Object = MibTableRow
tmnxBsxTransPrefSumEntry = _TmnxBsxTransPrefSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1)
)
tmnxBsxTransPrefSumEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicyId"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSubscriber"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntryId"),
)
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumEntry.setStatus("current")
_TmnxBsxTransPrefSumUpdateTime_Type = TimeStamp
_TmnxBsxTransPrefSumUpdateTime_Object = MibTableColumn
tmnxBsxTransPrefSumUpdateTime = _TmnxBsxTransPrefSumUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1, 1),
    _TmnxBsxTransPrefSumUpdateTime_Type()
)
tmnxBsxTransPrefSumUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumUpdateTime.setStatus("current")
_TmnxBsxTransPrefSumSubAddrType_Type = InetAddressType
_TmnxBsxTransPrefSumSubAddrType_Object = MibTableColumn
tmnxBsxTransPrefSumSubAddrType = _TmnxBsxTransPrefSumSubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1, 2),
    _TmnxBsxTransPrefSumSubAddrType_Type()
)
tmnxBsxTransPrefSumSubAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumSubAddrType.setStatus("current")


class _TmnxBsxTransPrefSumSubAddr_Type(InetAddress):
    """Custom type tmnxBsxTransPrefSumSubAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxTransPrefSumSubAddr_Type.__name__ = "InetAddress"
_TmnxBsxTransPrefSumSubAddr_Object = MibTableColumn
tmnxBsxTransPrefSumSubAddr = _TmnxBsxTransPrefSumSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1, 3),
    _TmnxBsxTransPrefSumSubAddr_Type()
)
tmnxBsxTransPrefSumSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumSubAddr.setStatus("current")
_TmnxBsxTransPrefSumSubAddrLen_Type = InetAddressPrefixLength
_TmnxBsxTransPrefSumSubAddrLen_Object = MibTableColumn
tmnxBsxTransPrefSumSubAddrLen = _TmnxBsxTransPrefSumSubAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1, 4),
    _TmnxBsxTransPrefSumSubAddrLen_Type()
)
tmnxBsxTransPrefSumSubAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumSubAddrLen.setStatus("current")
_TmnxBsxTransPrefSumNetAddrType_Type = InetAddressType
_TmnxBsxTransPrefSumNetAddrType_Object = MibTableColumn
tmnxBsxTransPrefSumNetAddrType = _TmnxBsxTransPrefSumNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1, 5),
    _TmnxBsxTransPrefSumNetAddrType_Type()
)
tmnxBsxTransPrefSumNetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumNetAddrType.setStatus("current")


class _TmnxBsxTransPrefSumNetAddr_Type(InetAddress):
    """Custom type tmnxBsxTransPrefSumNetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxTransPrefSumNetAddr_Type.__name__ = "InetAddress"
_TmnxBsxTransPrefSumNetAddr_Object = MibTableColumn
tmnxBsxTransPrefSumNetAddr = _TmnxBsxTransPrefSumNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1, 6),
    _TmnxBsxTransPrefSumNetAddr_Type()
)
tmnxBsxTransPrefSumNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumNetAddr.setStatus("current")
_TmnxBsxTransPrefSumNetAddrLen_Type = InetAddressPrefixLength
_TmnxBsxTransPrefSumNetAddrLen_Object = MibTableColumn
tmnxBsxTransPrefSumNetAddrLen = _TmnxBsxTransPrefSumNetAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1, 7),
    _TmnxBsxTransPrefSumNetAddrLen_Type()
)
tmnxBsxTransPrefSumNetAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumNetAddrLen.setStatus("current")
_TmnxBsxTransPrefSumParentSubType_Type = TmnxBsxAaSubscriberType
_TmnxBsxTransPrefSumParentSubType_Object = MibTableColumn
tmnxBsxTransPrefSumParentSubType = _TmnxBsxTransPrefSumParentSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1, 8),
    _TmnxBsxTransPrefSumParentSubType_Type()
)
tmnxBsxTransPrefSumParentSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumParentSubType.setStatus("current")
_TmnxBsxTransPrefSumParentSub_Type = TmnxBsxAaSubscriber
_TmnxBsxTransPrefSumParentSub_Object = MibTableColumn
tmnxBsxTransPrefSumParentSub = _TmnxBsxTransPrefSumParentSub_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1, 9),
    _TmnxBsxTransPrefSumParentSub_Type()
)
tmnxBsxTransPrefSumParentSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumParentSub.setStatus("current")
_TmnxBsxTransPrefSumAppProfNm_Type = TNamedItem
_TmnxBsxTransPrefSumAppProfNm_Object = MibTableColumn
tmnxBsxTransPrefSumAppProfNm = _TmnxBsxTransPrefSumAppProfNm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 7, 9, 1, 10),
    _TmnxBsxTransPrefSumAppProfNm_Type()
)
tmnxBsxTransPrefSumAppProfNm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTransPrefSumAppProfNm.setStatus("current")
_TmnxBsxHttpRedirObjs_ObjectIdentity = ObjectIdentity
tmnxBsxHttpRedirObjs = _TmnxBsxHttpRedirObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8)
)
_TmnxBsxHttpRedirScalars_ObjectIdentity = ObjectIdentity
tmnxBsxHttpRedirScalars = _TmnxBsxHttpRedirScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 1)
)
_TmnxBsxHttpRedirErrLastChTime_Type = TimeStamp
_TmnxBsxHttpRedirErrLastChTime_Object = MibScalar
tmnxBsxHttpRedirErrLastChTime = _TmnxBsxHttpRedirErrLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 1, 1),
    _TmnxBsxHttpRedirErrLastChTime_Type()
)
tmnxBsxHttpRedirErrLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrLastChTime.setStatus("current")
_TmnxBsxHttpRedirErrCodeLastCh_Type = TimeStamp
_TmnxBsxHttpRedirErrCodeLastCh_Object = MibScalar
tmnxBsxHttpRedirErrCodeLastCh = _TmnxBsxHttpRedirErrCodeLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 1, 2),
    _TmnxBsxHttpRedirErrCodeLastCh_Type()
)
tmnxBsxHttpRedirErrCodeLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrCodeLastCh.setStatus("current")
_TmnxBsxHttpRedirLastCh_Type = TimeStamp
_TmnxBsxHttpRedirLastCh_Object = MibScalar
tmnxBsxHttpRedirLastCh = _TmnxBsxHttpRedirLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 1, 3),
    _TmnxBsxHttpRedirLastCh_Type()
)
tmnxBsxHttpRedirLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirLastCh.setStatus("current")
_TmnxBsxHttpRedirErrTable_Object = MibTable
tmnxBsxHttpRedirErrTable = _TmnxBsxHttpRedirErrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrTable.setStatus("current")
_TmnxBsxHttpRedirErrEntry_Object = MibTableRow
tmnxBsxHttpRedirErrEntry = _TmnxBsxHttpRedirErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 2, 1)
)
tmnxBsxHttpRedirErrEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrName"),
)
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrEntry.setStatus("current")
_TmnxBsxHttpRedirErrName_Type = TNamedItem
_TmnxBsxHttpRedirErrName_Object = MibTableColumn
tmnxBsxHttpRedirErrName = _TmnxBsxHttpRedirErrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 2, 1, 1),
    _TmnxBsxHttpRedirErrName_Type()
)
tmnxBsxHttpRedirErrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrName.setStatus("current")
_TmnxBsxHttpRedirErrRowStatus_Type = RowStatus
_TmnxBsxHttpRedirErrRowStatus_Object = MibTableColumn
tmnxBsxHttpRedirErrRowStatus = _TmnxBsxHttpRedirErrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 2, 1, 2),
    _TmnxBsxHttpRedirErrRowStatus_Type()
)
tmnxBsxHttpRedirErrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrRowStatus.setStatus("current")
_TmnxBsxHttpRedirErrRowLastCh_Type = TimeStamp
_TmnxBsxHttpRedirErrRowLastCh_Object = MibTableColumn
tmnxBsxHttpRedirErrRowLastCh = _TmnxBsxHttpRedirErrRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 2, 1, 3),
    _TmnxBsxHttpRedirErrRowLastCh_Type()
)
tmnxBsxHttpRedirErrRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrRowLastCh.setStatus("current")


class _TmnxBsxHttpRedirErrEnabled_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxHttpRedirErrEnabled based on TmnxEnabledDisabled"""


_TmnxBsxHttpRedirErrEnabled_Object = MibTableColumn
tmnxBsxHttpRedirErrEnabled = _TmnxBsxHttpRedirErrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 2, 1, 4),
    _TmnxBsxHttpRedirErrEnabled_Type()
)
tmnxBsxHttpRedirErrEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrEnabled.setStatus("current")
_TmnxBsxHttpRedirErrDescription_Type = TItemDescription
_TmnxBsxHttpRedirErrDescription_Object = MibTableColumn
tmnxBsxHttpRedirErrDescription = _TmnxBsxHttpRedirErrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 2, 1, 5),
    _TmnxBsxHttpRedirErrDescription_Type()
)
tmnxBsxHttpRedirErrDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrDescription.setStatus("current")


class _TmnxBsxHttpRedirErrTemplateId_Type(Unsigned32):
    """Custom type tmnxBsxHttpRedirErrTemplateId based on Unsigned32"""
    defaultValue = 0


_TmnxBsxHttpRedirErrTemplateId_Object = MibTableColumn
tmnxBsxHttpRedirErrTemplateId = _TmnxBsxHttpRedirErrTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 2, 1, 6),
    _TmnxBsxHttpRedirErrTemplateId_Type()
)
tmnxBsxHttpRedirErrTemplateId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrTemplateId.setStatus("current")
_TmnxBsxHttpRedirErrHttpHost_Type = SnmpAdminString
_TmnxBsxHttpRedirErrHttpHost_Object = MibTableColumn
tmnxBsxHttpRedirErrHttpHost = _TmnxBsxHttpRedirErrHttpHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 2, 1, 7),
    _TmnxBsxHttpRedirErrHttpHost_Type()
)
tmnxBsxHttpRedirErrHttpHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrHttpHost.setStatus("current")


class _TmnxBsxHttpRedirErrParticipantId_Type(SnmpAdminString):
    """Custom type tmnxBsxHttpRedirErrParticipantId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxBsxHttpRedirErrParticipantId_Type.__name__ = "SnmpAdminString"
_TmnxBsxHttpRedirErrParticipantId_Object = MibTableColumn
tmnxBsxHttpRedirErrParticipantId = _TmnxBsxHttpRedirErrParticipantId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 2, 1, 8),
    _TmnxBsxHttpRedirErrParticipantId_Type()
)
tmnxBsxHttpRedirErrParticipantId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrParticipantId.setStatus("current")
_TmnxBsxHttpRedirErrCodeTable_Object = MibTable
tmnxBsxHttpRedirErrCodeTable = _TmnxBsxHttpRedirErrCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrCodeTable.setStatus("current")
_TmnxBsxHttpRedirErrCodeEntry_Object = MibTableRow
tmnxBsxHttpRedirErrCodeEntry = _TmnxBsxHttpRedirErrCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 3, 1)
)
tmnxBsxHttpRedirErrCodeEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrName"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrCode"),
)
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrCodeEntry.setStatus("current")
_TmnxBsxHttpRedirErrCode_Type = Unsigned32
_TmnxBsxHttpRedirErrCode_Object = MibTableColumn
tmnxBsxHttpRedirErrCode = _TmnxBsxHttpRedirErrCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 3, 1, 1),
    _TmnxBsxHttpRedirErrCode_Type()
)
tmnxBsxHttpRedirErrCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrCode.setStatus("current")
_TmnxBsxHttpRedirErrCodeRowStatus_Type = RowStatus
_TmnxBsxHttpRedirErrCodeRowStatus_Object = MibTableColumn
tmnxBsxHttpRedirErrCodeRowStatus = _TmnxBsxHttpRedirErrCodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 3, 1, 2),
    _TmnxBsxHttpRedirErrCodeRowStatus_Type()
)
tmnxBsxHttpRedirErrCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrCodeRowStatus.setStatus("current")
_TmnxBsxHttpRedirErrCodeRowLastCh_Type = TimeStamp
_TmnxBsxHttpRedirErrCodeRowLastCh_Object = MibTableColumn
tmnxBsxHttpRedirErrCodeRowLastCh = _TmnxBsxHttpRedirErrCodeRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 3, 1, 3),
    _TmnxBsxHttpRedirErrCodeRowLastCh_Type()
)
tmnxBsxHttpRedirErrCodeRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrCodeRowLastCh.setStatus("current")


class _TmnxBsxHttpRedirErrorCodeMsgSize_Type(Unsigned32):
    """Custom type tmnxBsxHttpRedirErrorCodeMsgSize based on Unsigned32"""
    defaultValue = 1024


_TmnxBsxHttpRedirErrorCodeMsgSize_Object = MibTableColumn
tmnxBsxHttpRedirErrorCodeMsgSize = _TmnxBsxHttpRedirErrorCodeMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 3, 1, 4),
    _TmnxBsxHttpRedirErrorCodeMsgSize_Type()
)
tmnxBsxHttpRedirErrorCodeMsgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrorCodeMsgSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrorCodeMsgSize.setUnits("octets")
_TmnxBsxHttpRdStatTable_Object = MibTable
tmnxBsxHttpRdStatTable = _TmnxBsxHttpRdStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatTable.setStatus("current")
_TmnxBsxHttpRdStatEntry_Object = MibTableRow
tmnxBsxHttpRdStatEntry = _TmnxBsxHttpRdStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1)
)
tmnxBsxHttpRdStatEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrName"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrCode"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatEntry.setStatus("current")
_TmnxBsxHttpRdStatDiscontTime_Type = TimeStamp
_TmnxBsxHttpRdStatDiscontTime_Object = MibTableColumn
tmnxBsxHttpRdStatDiscontTime = _TmnxBsxHttpRdStatDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 1),
    _TmnxBsxHttpRdStatDiscontTime_Type()
)
tmnxBsxHttpRdStatDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatDiscontTime.setStatus("current")
_TmnxBsxHttpRdStatHCRedir_Type = Counter64
_TmnxBsxHttpRdStatHCRedir_Object = MibTableColumn
tmnxBsxHttpRdStatHCRedir = _TmnxBsxHttpRdStatHCRedir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 2),
    _TmnxBsxHttpRdStatHCRedir_Type()
)
tmnxBsxHttpRdStatHCRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatHCRedir.setStatus("current")
_TmnxBsxHttpRdStatRedirLo_Type = Counter32
_TmnxBsxHttpRdStatRedirLo_Object = MibTableColumn
tmnxBsxHttpRdStatRedirLo = _TmnxBsxHttpRdStatRedirLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 3),
    _TmnxBsxHttpRdStatRedirLo_Type()
)
tmnxBsxHttpRdStatRedirLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatRedirLo.setStatus("current")
_TmnxBsxHttpRdStatRedirHi_Type = Counter32
_TmnxBsxHttpRdStatRedirHi_Object = MibTableColumn
tmnxBsxHttpRdStatRedirHi = _TmnxBsxHttpRdStatRedirHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 4),
    _TmnxBsxHttpRdStatRedirHi_Type()
)
tmnxBsxHttpRdStatRedirHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatRedirHi.setStatus("current")
_TmnxBsxHttpRdStatHCSizeExceeded_Type = Counter64
_TmnxBsxHttpRdStatHCSizeExceeded_Object = MibTableColumn
tmnxBsxHttpRdStatHCSizeExceeded = _TmnxBsxHttpRdStatHCSizeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 5),
    _TmnxBsxHttpRdStatHCSizeExceeded_Type()
)
tmnxBsxHttpRdStatHCSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatHCSizeExceeded.setStatus("current")
_TmnxBsxHttpRdStatSizeExceededLo_Type = Counter32
_TmnxBsxHttpRdStatSizeExceededLo_Object = MibTableColumn
tmnxBsxHttpRdStatSizeExceededLo = _TmnxBsxHttpRdStatSizeExceededLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 6),
    _TmnxBsxHttpRdStatSizeExceededLo_Type()
)
tmnxBsxHttpRdStatSizeExceededLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatSizeExceededLo.setStatus("current")
_TmnxBsxHttpRdStatSizeExceededHi_Type = Counter32
_TmnxBsxHttpRdStatSizeExceededHi_Object = MibTableColumn
tmnxBsxHttpRdStatSizeExceededHi = _TmnxBsxHttpRdStatSizeExceededHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 7),
    _TmnxBsxHttpRdStatSizeExceededHi_Type()
)
tmnxBsxHttpRdStatSizeExceededHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatSizeExceededHi.setStatus("current")
_TmnxBsxHttpRdStatHCOutOfResource_Type = Counter64
_TmnxBsxHttpRdStatHCOutOfResource_Object = MibTableColumn
tmnxBsxHttpRdStatHCOutOfResource = _TmnxBsxHttpRdStatHCOutOfResource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 8),
    _TmnxBsxHttpRdStatHCOutOfResource_Type()
)
tmnxBsxHttpRdStatHCOutOfResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatHCOutOfResource.setStatus("current")
_TmnxBsxHttpRdStatOutOfResourceLo_Type = Counter32
_TmnxBsxHttpRdStatOutOfResourceLo_Object = MibTableColumn
tmnxBsxHttpRdStatOutOfResourceLo = _TmnxBsxHttpRdStatOutOfResourceLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 9),
    _TmnxBsxHttpRdStatOutOfResourceLo_Type()
)
tmnxBsxHttpRdStatOutOfResourceLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatOutOfResourceLo.setStatus("current")
_TmnxBsxHttpRdStatOutOfResourceHi_Type = Counter32
_TmnxBsxHttpRdStatOutOfResourceHi_Object = MibTableColumn
tmnxBsxHttpRdStatOutOfResourceHi = _TmnxBsxHttpRdStatOutOfResourceHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 10),
    _TmnxBsxHttpRdStatOutOfResourceHi_Type()
)
tmnxBsxHttpRdStatOutOfResourceHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatOutOfResourceHi.setStatus("current")
_TmnxBsxHttpRdStatHCNotRedirFType_Type = Counter64
_TmnxBsxHttpRdStatHCNotRedirFType_Object = MibTableColumn
tmnxBsxHttpRdStatHCNotRedirFType = _TmnxBsxHttpRdStatHCNotRedirFType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 11),
    _TmnxBsxHttpRdStatHCNotRedirFType_Type()
)
tmnxBsxHttpRdStatHCNotRedirFType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatHCNotRedirFType.setStatus("current")
_TmnxBsxHttpRdStatNotRedirFTypeLo_Type = Counter32
_TmnxBsxHttpRdStatNotRedirFTypeLo_Object = MibTableColumn
tmnxBsxHttpRdStatNotRedirFTypeLo = _TmnxBsxHttpRdStatNotRedirFTypeLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 12),
    _TmnxBsxHttpRdStatNotRedirFTypeLo_Type()
)
tmnxBsxHttpRdStatNotRedirFTypeLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatNotRedirFTypeLo.setStatus("current")
_TmnxBsxHttpRdStatNotRedirFTypeHi_Type = Counter32
_TmnxBsxHttpRdStatNotRedirFTypeHi_Object = MibTableColumn
tmnxBsxHttpRdStatNotRedirFTypeHi = _TmnxBsxHttpRdStatNotRedirFTypeHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 13),
    _TmnxBsxHttpRdStatNotRedirFTypeHi_Type()
)
tmnxBsxHttpRdStatNotRedirFTypeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatNotRedirFTypeHi.setStatus("current")
_TmnxBsxHttpRdStatHCNotRedir_Type = Counter64
_TmnxBsxHttpRdStatHCNotRedir_Object = MibTableColumn
tmnxBsxHttpRdStatHCNotRedir = _TmnxBsxHttpRdStatHCNotRedir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 14),
    _TmnxBsxHttpRdStatHCNotRedir_Type()
)
tmnxBsxHttpRdStatHCNotRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatHCNotRedir.setStatus("current")
_TmnxBsxHttpRdStatNotRedirLo_Type = Counter32
_TmnxBsxHttpRdStatNotRedirLo_Object = MibTableColumn
tmnxBsxHttpRdStatNotRedirLo = _TmnxBsxHttpRdStatNotRedirLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 15),
    _TmnxBsxHttpRdStatNotRedirLo_Type()
)
tmnxBsxHttpRdStatNotRedirLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatNotRedirLo.setStatus("current")
_TmnxBsxHttpRdStatNotRedirHi_Type = Counter32
_TmnxBsxHttpRdStatNotRedirHi_Object = MibTableColumn
tmnxBsxHttpRdStatNotRedirHi = _TmnxBsxHttpRdStatNotRedirHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 4, 1, 16),
    _TmnxBsxHttpRdStatNotRedirHi_Type()
)
tmnxBsxHttpRdStatNotRedirHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRdStatNotRedirHi.setStatus("current")
_TmnxBsxHttpRedirTable_Object = MibTable
tmnxBsxHttpRedirTable = _TmnxBsxHttpRedirTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 5)
)
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirTable.setStatus("current")
_TmnxBsxHttpRedirEntry_Object = MibTableRow
tmnxBsxHttpRedirEntry = _TmnxBsxHttpRedirEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 5, 1)
)
tmnxBsxHttpRedirEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirName"),
)
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirEntry.setStatus("current")
_TmnxBsxHttpRedirName_Type = TNamedItem
_TmnxBsxHttpRedirName_Object = MibTableColumn
tmnxBsxHttpRedirName = _TmnxBsxHttpRedirName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 5, 1, 1),
    _TmnxBsxHttpRedirName_Type()
)
tmnxBsxHttpRedirName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirName.setStatus("current")
_TmnxBsxHttpRedirRowStatus_Type = RowStatus
_TmnxBsxHttpRedirRowStatus_Object = MibTableColumn
tmnxBsxHttpRedirRowStatus = _TmnxBsxHttpRedirRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 5, 1, 2),
    _TmnxBsxHttpRedirRowStatus_Type()
)
tmnxBsxHttpRedirRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirRowStatus.setStatus("current")
_TmnxBsxHttpRedirRowLastCh_Type = TimeStamp
_TmnxBsxHttpRedirRowLastCh_Object = MibTableColumn
tmnxBsxHttpRedirRowLastCh = _TmnxBsxHttpRedirRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 5, 1, 3),
    _TmnxBsxHttpRedirRowLastCh_Type()
)
tmnxBsxHttpRedirRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirRowLastCh.setStatus("current")


class _TmnxBsxHttpRedirEnabled_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxHttpRedirEnabled based on TmnxEnabledDisabled"""


_TmnxBsxHttpRedirEnabled_Object = MibTableColumn
tmnxBsxHttpRedirEnabled = _TmnxBsxHttpRedirEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 5, 1, 4),
    _TmnxBsxHttpRedirEnabled_Type()
)
tmnxBsxHttpRedirEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirEnabled.setStatus("current")
_TmnxBsxHttpRedirDescription_Type = TItemDescription
_TmnxBsxHttpRedirDescription_Object = MibTableColumn
tmnxBsxHttpRedirDescription = _TmnxBsxHttpRedirDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 5, 1, 5),
    _TmnxBsxHttpRedirDescription_Type()
)
tmnxBsxHttpRedirDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirDescription.setStatus("current")


class _TmnxBsxHttpRedirTemplateId_Type(Unsigned32):
    """Custom type tmnxBsxHttpRedirTemplateId based on Unsigned32"""
    defaultValue = 0


_TmnxBsxHttpRedirTemplateId_Object = MibTableColumn
tmnxBsxHttpRedirTemplateId = _TmnxBsxHttpRedirTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 5, 1, 6),
    _TmnxBsxHttpRedirTemplateId_Type()
)
tmnxBsxHttpRedirTemplateId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirTemplateId.setStatus("current")
_TmnxBsxHttpRedirHttpHost_Type = SnmpAdminString
_TmnxBsxHttpRedirHttpHost_Object = MibTableColumn
tmnxBsxHttpRedirHttpHost = _TmnxBsxHttpRedirHttpHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 5, 1, 7),
    _TmnxBsxHttpRedirHttpHost_Type()
)
tmnxBsxHttpRedirHttpHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirHttpHost.setStatus("current")
_TmnxBsxHttpPcyRdStatTable_Object = MibTable
tmnxBsxHttpPcyRdStatTable = _TmnxBsxHttpPcyRdStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6)
)
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatTable.setStatus("current")
_TmnxBsxHttpPcyRdStatEntry_Object = MibTableRow
tmnxBsxHttpPcyRdStatEntry = _TmnxBsxHttpPcyRdStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1)
)
tmnxBsxHttpPcyRdStatEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatEntry.setStatus("current")
_TmnxBsxHttpPcyRdStatDiscontTime_Type = TimeStamp
_TmnxBsxHttpPcyRdStatDiscontTime_Object = MibTableColumn
tmnxBsxHttpPcyRdStatDiscontTime = _TmnxBsxHttpPcyRdStatDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1, 1),
    _TmnxBsxHttpPcyRdStatDiscontTime_Type()
)
tmnxBsxHttpPcyRdStatDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatDiscontTime.setStatus("current")
_TmnxBsxHttpPcyRdStatHCRedir_Type = Counter64
_TmnxBsxHttpPcyRdStatHCRedir_Object = MibTableColumn
tmnxBsxHttpPcyRdStatHCRedir = _TmnxBsxHttpPcyRdStatHCRedir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1, 2),
    _TmnxBsxHttpPcyRdStatHCRedir_Type()
)
tmnxBsxHttpPcyRdStatHCRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatHCRedir.setStatus("current")
_TmnxBsxHttpPcyRdStatRedirLo_Type = Counter32
_TmnxBsxHttpPcyRdStatRedirLo_Object = MibTableColumn
tmnxBsxHttpPcyRdStatRedirLo = _TmnxBsxHttpPcyRdStatRedirLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1, 3),
    _TmnxBsxHttpPcyRdStatRedirLo_Type()
)
tmnxBsxHttpPcyRdStatRedirLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatRedirLo.setStatus("current")
_TmnxBsxHttpPcyRdStatRedirHi_Type = Counter32
_TmnxBsxHttpPcyRdStatRedirHi_Object = MibTableColumn
tmnxBsxHttpPcyRdStatRedirHi = _TmnxBsxHttpPcyRdStatRedirHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1, 4),
    _TmnxBsxHttpPcyRdStatRedirHi_Type()
)
tmnxBsxHttpPcyRdStatRedirHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatRedirHi.setStatus("current")
_TmnxBsxHttpPcyRdStatHCOutOfRes_Type = Counter64
_TmnxBsxHttpPcyRdStatHCOutOfRes_Object = MibTableColumn
tmnxBsxHttpPcyRdStatHCOutOfRes = _TmnxBsxHttpPcyRdStatHCOutOfRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1, 5),
    _TmnxBsxHttpPcyRdStatHCOutOfRes_Type()
)
tmnxBsxHttpPcyRdStatHCOutOfRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatHCOutOfRes.setStatus("current")
_TmnxBsxHttpPcyRdStatOutOfResLo_Type = Counter32
_TmnxBsxHttpPcyRdStatOutOfResLo_Object = MibTableColumn
tmnxBsxHttpPcyRdStatOutOfResLo = _TmnxBsxHttpPcyRdStatOutOfResLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1, 6),
    _TmnxBsxHttpPcyRdStatOutOfResLo_Type()
)
tmnxBsxHttpPcyRdStatOutOfResLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatOutOfResLo.setStatus("current")
_TmnxBsxHttpPcyRdStatOutOfResHi_Type = Counter32
_TmnxBsxHttpPcyRdStatOutOfResHi_Object = MibTableColumn
tmnxBsxHttpPcyRdStatOutOfResHi = _TmnxBsxHttpPcyRdStatOutOfResHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1, 7),
    _TmnxBsxHttpPcyRdStatOutOfResHi_Type()
)
tmnxBsxHttpPcyRdStatOutOfResHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatOutOfResHi.setStatus("current")
_TmnxBsxHttpPcyRdStatHCNotRedir_Type = Counter64
_TmnxBsxHttpPcyRdStatHCNotRedir_Object = MibTableColumn
tmnxBsxHttpPcyRdStatHCNotRedir = _TmnxBsxHttpPcyRdStatHCNotRedir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1, 8),
    _TmnxBsxHttpPcyRdStatHCNotRedir_Type()
)
tmnxBsxHttpPcyRdStatHCNotRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatHCNotRedir.setStatus("current")
_TmnxBsxHttpPcyRdStatNotRedirLo_Type = Counter32
_TmnxBsxHttpPcyRdStatNotRedirLo_Object = MibTableColumn
tmnxBsxHttpPcyRdStatNotRedirLo = _TmnxBsxHttpPcyRdStatNotRedirLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1, 9),
    _TmnxBsxHttpPcyRdStatNotRedirLo_Type()
)
tmnxBsxHttpPcyRdStatNotRedirLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatNotRedirLo.setStatus("current")
_TmnxBsxHttpPcyRdStatNotRedirHi_Type = Counter32
_TmnxBsxHttpPcyRdStatNotRedirHi_Object = MibTableColumn
tmnxBsxHttpPcyRdStatNotRedirHi = _TmnxBsxHttpPcyRdStatNotRedirHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 8, 6, 1, 10),
    _TmnxBsxHttpPcyRdStatNotRedirHi_Type()
)
tmnxBsxHttpPcyRdStatNotRedirHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpPcyRdStatNotRedirHi.setStatus("current")
_TmnxBsxStaticDataObjs_ObjectIdentity = ObjectIdentity
tmnxBsxStaticDataObjs = _TmnxBsxStaticDataObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9)
)
_TmnxBsxStaticObjScalars_ObjectIdentity = ObjectIdentity
tmnxBsxStaticObjScalars = _TmnxBsxStaticObjScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 1)
)
_TmnxBsxTListTableLastUpdateT_Type = TimeStamp
_TmnxBsxTListTableLastUpdateT_Object = MibScalar
tmnxBsxTListTableLastUpdateT = _TmnxBsxTListTableLastUpdateT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 1, 1),
    _TmnxBsxTListTableLastUpdateT_Type()
)
tmnxBsxTListTableLastUpdateT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTListTableLastUpdateT.setStatus("current")
_TmnxBsxTListAttribTableLUpdateT_Type = TimeStamp
_TmnxBsxTListAttribTableLUpdateT_Object = MibScalar
tmnxBsxTListAttribTableLUpdateT = _TmnxBsxTListAttribTableLUpdateT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 1, 2),
    _TmnxBsxTListAttribTableLUpdateT_Type()
)
tmnxBsxTListAttribTableLUpdateT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTListAttribTableLUpdateT.setStatus("current")
_TmnxBsxTListTable_Object = MibTable
tmnxBsxTListTable = _TmnxBsxTListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxTListTable.setStatus("current")
_TmnxBsxTListEntry_Object = MibTableRow
tmnxBsxTListEntry = _TmnxBsxTListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 2, 1)
)
tmnxBsxTListEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTListName"),
)
if mibBuilder.loadTexts:
    tmnxBsxTListEntry.setStatus("current")
_TmnxBsxTListName_Type = TNamedItem
_TmnxBsxTListName_Object = MibTableColumn
tmnxBsxTListName = _TmnxBsxTListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 2, 1, 1),
    _TmnxBsxTListName_Type()
)
tmnxBsxTListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxTListName.setStatus("current")
_TmnxBsxTListRowLastUpdateT_Type = TimeStamp
_TmnxBsxTListRowLastUpdateT_Object = MibTableColumn
tmnxBsxTListRowLastUpdateT = _TmnxBsxTListRowLastUpdateT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 2, 1, 2),
    _TmnxBsxTListRowLastUpdateT_Type()
)
tmnxBsxTListRowLastUpdateT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTListRowLastUpdateT.setStatus("current")
_TmnxBsxTListDescription_Type = TItemDescription
_TmnxBsxTListDescription_Object = MibTableColumn
tmnxBsxTListDescription = _TmnxBsxTListDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 2, 1, 3),
    _TmnxBsxTListDescription_Type()
)
tmnxBsxTListDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTListDescription.setStatus("current")
_TmnxBsxTListAttribTable_Object = MibTable
tmnxBsxTListAttribTable = _TmnxBsxTListAttribTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxTListAttribTable.setStatus("current")
_TmnxBsxTListAttribEntry_Object = MibTableRow
tmnxBsxTListAttribEntry = _TmnxBsxTListAttribEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 3, 1)
)
tmnxBsxTListAttribEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTListName"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTListAttribName"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxTListAttribSet"),
)
if mibBuilder.loadTexts:
    tmnxBsxTListAttribEntry.setStatus("current")
_TmnxBsxTListAttribName_Type = TNamedItem
_TmnxBsxTListAttribName_Object = MibTableColumn
tmnxBsxTListAttribName = _TmnxBsxTListAttribName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 3, 1, 1),
    _TmnxBsxTListAttribName_Type()
)
tmnxBsxTListAttribName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxTListAttribName.setStatus("current")
_TmnxBsxTListAttribSet_Type = Unsigned32
_TmnxBsxTListAttribSet_Object = MibTableColumn
tmnxBsxTListAttribSet = _TmnxBsxTListAttribSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 3, 1, 2),
    _TmnxBsxTListAttribSet_Type()
)
tmnxBsxTListAttribSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxTListAttribSet.setStatus("current")
_TmnxBsxTListAttribRowLastUpdateT_Type = TimeStamp
_TmnxBsxTListAttribRowLastUpdateT_Object = MibTableColumn
tmnxBsxTListAttribRowLastUpdateT = _TmnxBsxTListAttribRowLastUpdateT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 3, 1, 3),
    _TmnxBsxTListAttribRowLastUpdateT_Type()
)
tmnxBsxTListAttribRowLastUpdateT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTListAttribRowLastUpdateT.setStatus("current")
_TmnxBsxTListAttribType_Type = TmnxBsxTListAttribType
_TmnxBsxTListAttribType_Object = MibTableColumn
tmnxBsxTListAttribType = _TmnxBsxTListAttribType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 3, 1, 4),
    _TmnxBsxTListAttribType_Type()
)
tmnxBsxTListAttribType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTListAttribType.setStatus("current")
_TmnxBsxTListAttribValue_Type = TmnxBsxTListAttribValue
_TmnxBsxTListAttribValue_Object = MibTableColumn
tmnxBsxTListAttribValue = _TmnxBsxTListAttribValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 9, 3, 1, 5),
    _TmnxBsxTListAttribValue_Type()
)
tmnxBsxTListAttribValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxTListAttribValue.setStatus("current")
_TmnxBsxRedundancyObjs_ObjectIdentity = ObjectIdentity
tmnxBsxRedundancyObjs = _TmnxBsxRedundancyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10)
)
_TmnxBsxRedundancyObjScalars_ObjectIdentity = ObjectIdentity
tmnxBsxRedundancyObjScalars = _TmnxBsxRedundancyObjScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 1)
)
_TmnxBsxAarpTableLastChTime_Type = TimeStamp
_TmnxBsxAarpTableLastChTime_Object = MibScalar
tmnxBsxAarpTableLastChTime = _TmnxBsxAarpTableLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 1, 1),
    _TmnxBsxAarpTableLastChTime_Type()
)
tmnxBsxAarpTableLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpTableLastChTime.setStatus("current")
_TmnxBsxAarpInstTable_Object = MibTable
tmnxBsxAarpInstTable = _TmnxBsxAarpInstTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxAarpInstTable.setStatus("current")
_TmnxBsxAarpInstEntry_Object = MibTableRow
tmnxBsxAarpInstEntry = _TmnxBsxAarpInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1)
)
tmnxBsxAarpInstEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstId"),
)
if mibBuilder.loadTexts:
    tmnxBsxAarpInstEntry.setStatus("current")
_TmnxBsxAarpInstId_Type = TmnxBsxAarpId
_TmnxBsxAarpInstId_Object = MibTableColumn
tmnxBsxAarpInstId = _TmnxBsxAarpInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 1),
    _TmnxBsxAarpInstId_Type()
)
tmnxBsxAarpInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstId.setStatus("current")
_TmnxBsxAarpInstRowStatus_Type = RowStatus
_TmnxBsxAarpInstRowStatus_Object = MibTableColumn
tmnxBsxAarpInstRowStatus = _TmnxBsxAarpInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 2),
    _TmnxBsxAarpInstRowStatus_Type()
)
tmnxBsxAarpInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstRowStatus.setStatus("current")
_TmnxBsxAarpInstLastCh_Type = TimeStamp
_TmnxBsxAarpInstLastCh_Object = MibTableColumn
tmnxBsxAarpInstLastCh = _TmnxBsxAarpInstLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 3),
    _TmnxBsxAarpInstLastCh_Type()
)
tmnxBsxAarpInstLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstLastCh.setStatus("current")
_TmnxBsxAarpInstDescription_Type = TItemDescription
_TmnxBsxAarpInstDescription_Object = MibTableColumn
tmnxBsxAarpInstDescription = _TmnxBsxAarpInstDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 4),
    _TmnxBsxAarpInstDescription_Type()
)
tmnxBsxAarpInstDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstDescription.setStatus("current")


class _TmnxBsxAarpInstPeerIpType_Type(InetAddressType):
    """Custom type tmnxBsxAarpInstPeerIpType based on InetAddressType"""


_TmnxBsxAarpInstPeerIpType_Object = MibTableColumn
tmnxBsxAarpInstPeerIpType = _TmnxBsxAarpInstPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 5),
    _TmnxBsxAarpInstPeerIpType_Type()
)
tmnxBsxAarpInstPeerIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPeerIpType.setStatus("current")


class _TmnxBsxAarpInstPeerIpAddr_Type(InetAddress):
    """Custom type tmnxBsxAarpInstPeerIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxAarpInstPeerIpAddr_Type.__name__ = "InetAddress"
_TmnxBsxAarpInstPeerIpAddr_Object = MibTableColumn
tmnxBsxAarpInstPeerIpAddr = _TmnxBsxAarpInstPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 6),
    _TmnxBsxAarpInstPeerIpAddr_Type()
)
tmnxBsxAarpInstPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPeerIpAddr.setStatus("current")


class _TmnxBsxAarpInstPriority_Type(Unsigned32):
    """Custom type tmnxBsxAarpInstPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxBsxAarpInstPriority_Type.__name__ = "Unsigned32"
_TmnxBsxAarpInstPriority_Object = MibTableColumn
tmnxBsxAarpInstPriority = _TmnxBsxAarpInstPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 7),
    _TmnxBsxAarpInstPriority_Type()
)
tmnxBsxAarpInstPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPriority.setStatus("current")


class _TmnxBsxAarpInstAdminState_Type(TmnxAdminState):
    """Custom type tmnxBsxAarpInstAdminState based on TmnxAdminState"""


_TmnxBsxAarpInstAdminState_Object = MibTableColumn
tmnxBsxAarpInstAdminState = _TmnxBsxAarpInstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 8),
    _TmnxBsxAarpInstAdminState_Type()
)
tmnxBsxAarpInstAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstAdminState.setStatus("current")
_TmnxBsxAarpInstOperState_Type = TmnxOperState
_TmnxBsxAarpInstOperState_Object = MibTableColumn
tmnxBsxAarpInstOperState = _TmnxBsxAarpInstOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 9),
    _TmnxBsxAarpInstOperState_Type()
)
tmnxBsxAarpInstOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstOperState.setStatus("current")
_TmnxBsxAarpInstState_Type = TmnxBsxAarpInstState
_TmnxBsxAarpInstState_Object = MibTableColumn
tmnxBsxAarpInstState = _TmnxBsxAarpInstState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 10),
    _TmnxBsxAarpInstState_Type()
)
tmnxBsxAarpInstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstState.setStatus("current")
_TmnxBsxAarpInstOperFlags_Type = TmnxBsxAarpInstOperFlags
_TmnxBsxAarpInstOperFlags_Object = MibTableColumn
tmnxBsxAarpInstOperFlags = _TmnxBsxAarpInstOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 11),
    _TmnxBsxAarpInstOperFlags_Type()
)
tmnxBsxAarpInstOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstOperFlags.setStatus("current")
_TmnxBsxAarpInstPeerPriority_Type = Unsigned32
_TmnxBsxAarpInstPeerPriority_Object = MibTableColumn
tmnxBsxAarpInstPeerPriority = _TmnxBsxAarpInstPeerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 12),
    _TmnxBsxAarpInstPeerPriority_Type()
)
tmnxBsxAarpInstPeerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPeerPriority.setStatus("current")
_TmnxBsxAarpInstPeerState_Type = TmnxBsxAarpInstState
_TmnxBsxAarpInstPeerState_Object = MibTableColumn
tmnxBsxAarpInstPeerState = _TmnxBsxAarpInstPeerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 13),
    _TmnxBsxAarpInstPeerState_Type()
)
tmnxBsxAarpInstPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPeerState.setStatus("current")
_TmnxBsxAarpInstPeerOperFlags_Type = TmnxBsxAarpInstOperFlags
_TmnxBsxAarpInstPeerOperFlags_Object = MibTableColumn
tmnxBsxAarpInstPeerOperFlags = _TmnxBsxAarpInstPeerOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 14),
    _TmnxBsxAarpInstPeerOperFlags_Type()
)
tmnxBsxAarpInstPeerOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPeerOperFlags.setStatus("current")
_TmnxBsxAarpInstPeerSubRefType_Type = TmnxBsxAaSubscriberType
_TmnxBsxAarpInstPeerSubRefType_Object = MibTableColumn
tmnxBsxAarpInstPeerSubRefType = _TmnxBsxAarpInstPeerSubRefType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 15),
    _TmnxBsxAarpInstPeerSubRefType_Type()
)
tmnxBsxAarpInstPeerSubRefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPeerSubRefType.setStatus("current")


class _TmnxBsxAarpInstPeerEPSapPortId_Type(TmnxPortID):
    """Custom type tmnxBsxAarpInstPeerEPSapPortId based on TmnxPortID"""
    defaultHexValue = 503316480


_TmnxBsxAarpInstPeerEPSapPortId_Object = MibTableColumn
tmnxBsxAarpInstPeerEPSapPortId = _TmnxBsxAarpInstPeerEPSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 16),
    _TmnxBsxAarpInstPeerEPSapPortId_Type()
)
tmnxBsxAarpInstPeerEPSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPeerEPSapPortId.setStatus("current")


class _TmnxBsxAarpInstPeerEPSapEncap_Type(TmnxEncapVal):
    """Custom type tmnxBsxAarpInstPeerEPSapEncap based on TmnxEncapVal"""
    defaultValue = 0


_TmnxBsxAarpInstPeerEPSapEncap_Object = MibTableColumn
tmnxBsxAarpInstPeerEPSapEncap = _TmnxBsxAarpInstPeerEPSapEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 17),
    _TmnxBsxAarpInstPeerEPSapEncap_Type()
)
tmnxBsxAarpInstPeerEPSapEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPeerEPSapEncap.setStatus("current")


class _TmnxBsxAarpInstPeerEPSapEncType_Type(TmnxPortEncapType):
    """Custom type tmnxBsxAarpInstPeerEPSapEncType based on TmnxPortEncapType"""


_TmnxBsxAarpInstPeerEPSapEncType_Object = MibTableColumn
tmnxBsxAarpInstPeerEPSapEncType = _TmnxBsxAarpInstPeerEPSapEncType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 18),
    _TmnxBsxAarpInstPeerEPSapEncType_Type()
)
tmnxBsxAarpInstPeerEPSapEncType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPeerEPSapEncType.setStatus("current")


class _TmnxBsxAarpInstPeerEPSdpBindId_Type(SdpBindId):
    """Custom type tmnxBsxAarpInstPeerEPSdpBindId based on SdpBindId"""
    defaultHexValue = "0"


_TmnxBsxAarpInstPeerEPSdpBindId_Object = MibTableColumn
tmnxBsxAarpInstPeerEPSdpBindId = _TmnxBsxAarpInstPeerEPSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 2, 1, 19),
    _TmnxBsxAarpInstPeerEPSdpBindId_Type()
)
tmnxBsxAarpInstPeerEPSdpBindId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpInstPeerEPSdpBindId.setStatus("current")
_TmnxBsxAarpCommandTable_Object = MibTable
tmnxBsxAarpCommandTable = _TmnxBsxAarpCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxAarpCommandTable.setStatus("current")
_TmnxBsxAarpCommandEntry_Object = MibTableRow
tmnxBsxAarpCommandEntry = _TmnxBsxAarpCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxBsxAarpCommandEntry.setStatus("current")


class _TmnxBsxAarpCommandControl_Type(TmnxBsxAarpCommand):
    """Custom type tmnxBsxAarpCommandControl based on TmnxBsxAarpCommand"""


_TmnxBsxAarpCommandControl_Object = MibTableColumn
tmnxBsxAarpCommandControl = _TmnxBsxAarpCommandControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 3, 1, 1),
    _TmnxBsxAarpCommandControl_Type()
)
tmnxBsxAarpCommandControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxAarpCommandControl.setStatus("current")
_TmnxBsxAarpServPointTable_Object = MibTable
tmnxBsxAarpServPointTable = _TmnxBsxAarpServPointTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxAarpServPointTable.setStatus("current")
_TmnxBsxAarpServPointEntry_Object = MibTableRow
tmnxBsxAarpServPointEntry = _TmnxBsxAarpServPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 4, 1)
)
tmnxBsxAarpServPointEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstId"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAarpServPointRole"),
)
if mibBuilder.loadTexts:
    tmnxBsxAarpServPointEntry.setStatus("current")
_TmnxBsxAarpServPointRole_Type = TmnxBsxAarpServPointRole
_TmnxBsxAarpServPointRole_Object = MibTableColumn
tmnxBsxAarpServPointRole = _TmnxBsxAarpServPointRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 4, 1, 1),
    _TmnxBsxAarpServPointRole_Type()
)
tmnxBsxAarpServPointRole.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxAarpServPointRole.setStatus("current")
_TmnxBsxAarpServPointType_Type = TmnxBsxAarpServPointType
_TmnxBsxAarpServPointType_Object = MibTableColumn
tmnxBsxAarpServPointType = _TmnxBsxAarpServPointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 4, 1, 2),
    _TmnxBsxAarpServPointType_Type()
)
tmnxBsxAarpServPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpServPointType.setStatus("current")
_TmnxBsxAarpServPoint_Type = TmnxBsxAarpServPoint
_TmnxBsxAarpServPoint_Object = MibTableColumn
tmnxBsxAarpServPoint = _TmnxBsxAarpServPoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 10, 4, 1, 3),
    _TmnxBsxAarpServPoint_Type()
)
tmnxBsxAarpServPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxAarpServPoint.setStatus("current")
_TmnxBsxHttpEnrichObjs_ObjectIdentity = ObjectIdentity
tmnxBsxHttpEnrichObjs = _TmnxBsxHttpEnrichObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11)
)
_TmnxBsxHttpEnrichScalars_ObjectIdentity = ObjectIdentity
tmnxBsxHttpEnrichScalars = _TmnxBsxHttpEnrichScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 1)
)
_TmnxBsxHttpEnrichLastChTime_Type = TimeStamp
_TmnxBsxHttpEnrichLastChTime_Object = MibScalar
tmnxBsxHttpEnrichLastChTime = _TmnxBsxHttpEnrichLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 1, 1),
    _TmnxBsxHttpEnrichLastChTime_Type()
)
tmnxBsxHttpEnrichLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichLastChTime.setStatus("current")
_TmnxBsxHttpEnrichFieldLastChTime_Type = TimeStamp
_TmnxBsxHttpEnrichFieldLastChTime_Object = MibScalar
tmnxBsxHttpEnrichFieldLastChTime = _TmnxBsxHttpEnrichFieldLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 1, 2),
    _TmnxBsxHttpEnrichFieldLastChTime_Type()
)
tmnxBsxHttpEnrichFieldLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichFieldLastChTime.setStatus("current")
_TmnxBsxHttpEnrichTable_Object = MibTable
tmnxBsxHttpEnrichTable = _TmnxBsxHttpEnrichTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichTable.setStatus("current")
_TmnxBsxHttpEnrichEntry_Object = MibTableRow
tmnxBsxHttpEnrichEntry = _TmnxBsxHttpEnrichEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 2, 1)
)
tmnxBsxHttpEnrichEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichName"),
)
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichEntry.setStatus("current")
_TmnxBsxHttpEnrichName_Type = TNamedItem
_TmnxBsxHttpEnrichName_Object = MibTableColumn
tmnxBsxHttpEnrichName = _TmnxBsxHttpEnrichName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 2, 1, 1),
    _TmnxBsxHttpEnrichName_Type()
)
tmnxBsxHttpEnrichName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichName.setStatus("current")
_TmnxBsxHttpEnrichRowStatus_Type = RowStatus
_TmnxBsxHttpEnrichRowStatus_Object = MibTableColumn
tmnxBsxHttpEnrichRowStatus = _TmnxBsxHttpEnrichRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 2, 1, 2),
    _TmnxBsxHttpEnrichRowStatus_Type()
)
tmnxBsxHttpEnrichRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichRowStatus.setStatus("current")
_TmnxBsxHttpEnrichRowLastCh_Type = TimeStamp
_TmnxBsxHttpEnrichRowLastCh_Object = MibTableColumn
tmnxBsxHttpEnrichRowLastCh = _TmnxBsxHttpEnrichRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 2, 1, 3),
    _TmnxBsxHttpEnrichRowLastCh_Type()
)
tmnxBsxHttpEnrichRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichRowLastCh.setStatus("current")


class _TmnxBsxHttpEnrichEnabled_Type(TmnxEnabledDisabled):
    """Custom type tmnxBsxHttpEnrichEnabled based on TmnxEnabledDisabled"""


_TmnxBsxHttpEnrichEnabled_Object = MibTableColumn
tmnxBsxHttpEnrichEnabled = _TmnxBsxHttpEnrichEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 2, 1, 4),
    _TmnxBsxHttpEnrichEnabled_Type()
)
tmnxBsxHttpEnrichEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichEnabled.setStatus("current")
_TmnxBsxHttpEnrichDescription_Type = TItemDescription
_TmnxBsxHttpEnrichDescription_Object = MibTableColumn
tmnxBsxHttpEnrichDescription = _TmnxBsxHttpEnrichDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 2, 1, 5),
    _TmnxBsxHttpEnrichDescription_Type()
)
tmnxBsxHttpEnrichDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichDescription.setStatus("current")
_TmnxBsxHttpEnrichFieldTable_Object = MibTable
tmnxBsxHttpEnrichFieldTable = _TmnxBsxHttpEnrichFieldTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichFieldTable.setStatus("current")
_TmnxBsxHttpEnrichFieldEntry_Object = MibTableRow
tmnxBsxHttpEnrichFieldEntry = _TmnxBsxHttpEnrichFieldEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 3, 1)
)
tmnxBsxHttpEnrichFieldEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGroupIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichName"),
    (1, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichFieldName"),
)
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichFieldEntry.setStatus("current")
_TmnxBsxHttpEnrichFieldName_Type = TNamedItem
_TmnxBsxHttpEnrichFieldName_Object = MibTableColumn
tmnxBsxHttpEnrichFieldName = _TmnxBsxHttpEnrichFieldName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 3, 1, 1),
    _TmnxBsxHttpEnrichFieldName_Type()
)
tmnxBsxHttpEnrichFieldName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichFieldName.setStatus("current")
_TmnxBsxHttpEnrichFieldRowStatus_Type = RowStatus
_TmnxBsxHttpEnrichFieldRowStatus_Object = MibTableColumn
tmnxBsxHttpEnrichFieldRowStatus = _TmnxBsxHttpEnrichFieldRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 3, 1, 2),
    _TmnxBsxHttpEnrichFieldRowStatus_Type()
)
tmnxBsxHttpEnrichFieldRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichFieldRowStatus.setStatus("current")
_TmnxBsxHttpEnrichFieldRowLastCh_Type = TimeStamp
_TmnxBsxHttpEnrichFieldRowLastCh_Object = MibTableColumn
tmnxBsxHttpEnrichFieldRowLastCh = _TmnxBsxHttpEnrichFieldRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 3, 1, 3),
    _TmnxBsxHttpEnrichFieldRowLastCh_Type()
)
tmnxBsxHttpEnrichFieldRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichFieldRowLastCh.setStatus("current")


class _TmnxBsxHttpEnrichFieldHeaderName_Type(SnmpAdminString):
    """Custom type tmnxBsxHttpEnrichFieldHeaderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxBsxHttpEnrichFieldHeaderName_Type.__name__ = "SnmpAdminString"
_TmnxBsxHttpEnrichFieldHeaderName_Object = MibTableColumn
tmnxBsxHttpEnrichFieldHeaderName = _TmnxBsxHttpEnrichFieldHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 3, 1, 4),
    _TmnxBsxHttpEnrichFieldHeaderName_Type()
)
tmnxBsxHttpEnrichFieldHeaderName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichFieldHeaderName.setStatus("current")
_TmnxBsxHttpEnrichStatTable_Object = MibTable
tmnxBsxHttpEnrichStatTable = _TmnxBsxHttpEnrichStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichStatTable.setStatus("current")
_TmnxBsxHttpEnrichStatEntry_Object = MibTableRow
tmnxBsxHttpEnrichStatEntry = _TmnxBsxHttpEnrichStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1)
)
tmnxBsxHttpEnrichStatEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichStatEntry.setStatus("current")
_TmnxBsxHttpEnrichStatDiscontTime_Type = TimeStamp
_TmnxBsxHttpEnrichStatDiscontTime_Object = MibTableColumn
tmnxBsxHttpEnrichStatDiscontTime = _TmnxBsxHttpEnrichStatDiscontTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 1),
    _TmnxBsxHttpEnrichStatDiscontTime_Type()
)
tmnxBsxHttpEnrichStatDiscontTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichStatDiscontTime.setStatus("current")
_TmnxBsxHttpEnrichHCNumEnriched_Type = Counter64
_TmnxBsxHttpEnrichHCNumEnriched_Object = MibTableColumn
tmnxBsxHttpEnrichHCNumEnriched = _TmnxBsxHttpEnrichHCNumEnriched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 2),
    _TmnxBsxHttpEnrichHCNumEnriched_Type()
)
tmnxBsxHttpEnrichHCNumEnriched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichHCNumEnriched.setStatus("current")
_TmnxBsxHttpEnrichNumEnrichedLo_Type = Counter32
_TmnxBsxHttpEnrichNumEnrichedLo_Object = MibTableColumn
tmnxBsxHttpEnrichNumEnrichedLo = _TmnxBsxHttpEnrichNumEnrichedLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 3),
    _TmnxBsxHttpEnrichNumEnrichedLo_Type()
)
tmnxBsxHttpEnrichNumEnrichedLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichNumEnrichedLo.setStatus("current")
_TmnxBsxHttpEnrichNumEnrichedHi_Type = Counter32
_TmnxBsxHttpEnrichNumEnrichedHi_Object = MibTableColumn
tmnxBsxHttpEnrichNumEnrichedHi = _TmnxBsxHttpEnrichNumEnrichedHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 4),
    _TmnxBsxHttpEnrichNumEnrichedHi_Type()
)
tmnxBsxHttpEnrichNumEnrichedHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichNumEnrichedHi.setStatus("current")
_TmnxBsxHttpEnrichHCNumNoResource_Type = Counter64
_TmnxBsxHttpEnrichHCNumNoResource_Object = MibTableColumn
tmnxBsxHttpEnrichHCNumNoResource = _TmnxBsxHttpEnrichHCNumNoResource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 5),
    _TmnxBsxHttpEnrichHCNumNoResource_Type()
)
tmnxBsxHttpEnrichHCNumNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichHCNumNoResource.setStatus("current")
_TmnxBsxHttpEnrichNumNoResourceLo_Type = Counter32
_TmnxBsxHttpEnrichNumNoResourceLo_Object = MibTableColumn
tmnxBsxHttpEnrichNumNoResourceLo = _TmnxBsxHttpEnrichNumNoResourceLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 6),
    _TmnxBsxHttpEnrichNumNoResourceLo_Type()
)
tmnxBsxHttpEnrichNumNoResourceLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichNumNoResourceLo.setStatus("current")
_TmnxBsxHttpEnrichNumNoResourceHi_Type = Counter32
_TmnxBsxHttpEnrichNumNoResourceHi_Object = MibTableColumn
tmnxBsxHttpEnrichNumNoResourceHi = _TmnxBsxHttpEnrichNumNoResourceHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 7),
    _TmnxBsxHttpEnrichNumNoResourceHi_Type()
)
tmnxBsxHttpEnrichNumNoResourceHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichNumNoResourceHi.setStatus("current")
_TmnxBsxHttpEnrichHCMissngSubData_Type = Counter64
_TmnxBsxHttpEnrichHCMissngSubData_Object = MibTableColumn
tmnxBsxHttpEnrichHCMissngSubData = _TmnxBsxHttpEnrichHCMissngSubData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 8),
    _TmnxBsxHttpEnrichHCMissngSubData_Type()
)
tmnxBsxHttpEnrichHCMissngSubData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichHCMissngSubData.setStatus("current")
_TmnxBsxHttpEnrichMissngSubDataLo_Type = Counter32
_TmnxBsxHttpEnrichMissngSubDataLo_Object = MibTableColumn
tmnxBsxHttpEnrichMissngSubDataLo = _TmnxBsxHttpEnrichMissngSubDataLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 9),
    _TmnxBsxHttpEnrichMissngSubDataLo_Type()
)
tmnxBsxHttpEnrichMissngSubDataLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichMissngSubDataLo.setStatus("current")
_TmnxBsxHttpEnrichMissngSubDataHi_Type = Counter32
_TmnxBsxHttpEnrichMissngSubDataHi_Object = MibTableColumn
tmnxBsxHttpEnrichMissngSubDataHi = _TmnxBsxHttpEnrichMissngSubDataHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 10),
    _TmnxBsxHttpEnrichMissngSubDataHi_Type()
)
tmnxBsxHttpEnrichMissngSubDataHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichMissngSubDataHi.setStatus("current")
_TmnxBsxHttpEnrichHCTplNotEnabled_Type = Counter64
_TmnxBsxHttpEnrichHCTplNotEnabled_Object = MibTableColumn
tmnxBsxHttpEnrichHCTplNotEnabled = _TmnxBsxHttpEnrichHCTplNotEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 11),
    _TmnxBsxHttpEnrichHCTplNotEnabled_Type()
)
tmnxBsxHttpEnrichHCTplNotEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichHCTplNotEnabled.setStatus("current")
_TmnxBsxHttpEnrichTplNotEnabledLo_Type = Counter32
_TmnxBsxHttpEnrichTplNotEnabledLo_Object = MibTableColumn
tmnxBsxHttpEnrichTplNotEnabledLo = _TmnxBsxHttpEnrichTplNotEnabledLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 12),
    _TmnxBsxHttpEnrichTplNotEnabledLo_Type()
)
tmnxBsxHttpEnrichTplNotEnabledLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichTplNotEnabledLo.setStatus("current")
_TmnxBsxHttpEnrichTplNotEnabledHi_Type = Counter32
_TmnxBsxHttpEnrichTplNotEnabledHi_Object = MibTableColumn
tmnxBsxHttpEnrichTplNotEnabledHi = _TmnxBsxHttpEnrichTplNotEnabledHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 13),
    _TmnxBsxHttpEnrichTplNotEnabledHi_Type()
)
tmnxBsxHttpEnrichTplNotEnabledHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichTplNotEnabledHi.setStatus("current")
_TmnxBsxHttpEnrichHCTrafficChar_Type = Counter64
_TmnxBsxHttpEnrichHCTrafficChar_Object = MibTableColumn
tmnxBsxHttpEnrichHCTrafficChar = _TmnxBsxHttpEnrichHCTrafficChar_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 14),
    _TmnxBsxHttpEnrichHCTrafficChar_Type()
)
tmnxBsxHttpEnrichHCTrafficChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichHCTrafficChar.setStatus("current")
_TmnxBsxHttpEnrichTrafficCharLo_Type = Counter32
_TmnxBsxHttpEnrichTrafficCharLo_Object = MibTableColumn
tmnxBsxHttpEnrichTrafficCharLo = _TmnxBsxHttpEnrichTrafficCharLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 15),
    _TmnxBsxHttpEnrichTrafficCharLo_Type()
)
tmnxBsxHttpEnrichTrafficCharLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichTrafficCharLo.setStatus("current")
_TmnxBsxHttpEnrichTrafficCharHi_Type = Counter32
_TmnxBsxHttpEnrichTrafficCharHi_Object = MibTableColumn
tmnxBsxHttpEnrichTrafficCharHi = _TmnxBsxHttpEnrichTrafficCharHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 11, 4, 1, 16),
    _TmnxBsxHttpEnrichTrafficCharHi_Type()
)
tmnxBsxHttpEnrichTrafficCharHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichTrafficCharHi.setStatus("current")
_TmnxBsxRadApObjs_ObjectIdentity = ObjectIdentity
tmnxBsxRadApObjs = _TmnxBsxRadApObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12)
)
_TmnxBsxRadApScalars_ObjectIdentity = ObjectIdentity
tmnxBsxRadApScalars = _TmnxBsxRadApScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 1)
)
_TmnxBsxRadApLastChTime_Type = TimeStamp
_TmnxBsxRadApLastChTime_Object = MibScalar
tmnxBsxRadApLastChTime = _TmnxBsxRadApLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 1, 1),
    _TmnxBsxRadApLastChTime_Type()
)
tmnxBsxRadApLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApLastChTime.setStatus("current")
_TmnxBsxRadApServLastChTime_Type = TimeStamp
_TmnxBsxRadApServLastChTime_Object = MibScalar
tmnxBsxRadApServLastChTime = _TmnxBsxRadApServLastChTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 1, 2),
    _TmnxBsxRadApServLastChTime_Type()
)
tmnxBsxRadApServLastChTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApServLastChTime.setStatus("current")
_TmnxBsxRadApTable_Object = MibTable
tmnxBsxRadApTable = _TmnxBsxRadApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxRadApTable.setStatus("current")
_TmnxBsxRadApEntry_Object = MibTableRow
tmnxBsxRadApEntry = _TmnxBsxRadApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1)
)
tmnxBsxRadApEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxRadApName"),
)
if mibBuilder.loadTexts:
    tmnxBsxRadApEntry.setStatus("current")
_TmnxBsxRadApName_Type = TNamedItem
_TmnxBsxRadApName_Object = MibTableColumn
tmnxBsxRadApName = _TmnxBsxRadApName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 1),
    _TmnxBsxRadApName_Type()
)
tmnxBsxRadApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxRadApName.setStatus("current")
_TmnxBsxRadApRowStatus_Type = RowStatus
_TmnxBsxRadApRowStatus_Object = MibTableColumn
tmnxBsxRadApRowStatus = _TmnxBsxRadApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 2),
    _TmnxBsxRadApRowStatus_Type()
)
tmnxBsxRadApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApRowStatus.setStatus("current")
_TmnxBsxRadApRowLastChange_Type = TimeStamp
_TmnxBsxRadApRowLastChange_Object = MibTableColumn
tmnxBsxRadApRowLastChange = _TmnxBsxRadApRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 3),
    _TmnxBsxRadApRowLastChange_Type()
)
tmnxBsxRadApRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApRowLastChange.setStatus("current")
_TmnxBsxRadApDescription_Type = TItemDescription
_TmnxBsxRadApDescription_Object = MibTableColumn
tmnxBsxRadApDescription = _TmnxBsxRadApDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 4),
    _TmnxBsxRadApDescription_Type()
)
tmnxBsxRadApDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApDescription.setStatus("current")


class _TmnxBsxRadApServerRetry_Type(Unsigned32):
    """Custom type tmnxBsxRadApServerRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxBsxRadApServerRetry_Type.__name__ = "Unsigned32"
_TmnxBsxRadApServerRetry_Object = MibTableColumn
tmnxBsxRadApServerRetry = _TmnxBsxRadApServerRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 5),
    _TmnxBsxRadApServerRetry_Type()
)
tmnxBsxRadApServerRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServerRetry.setStatus("current")


class _TmnxBsxRadApServerTimeout_Type(Unsigned32):
    """Custom type tmnxBsxRadApServerTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_TmnxBsxRadApServerTimeout_Type.__name__ = "Unsigned32"
_TmnxBsxRadApServerTimeout_Object = MibTableColumn
tmnxBsxRadApServerTimeout = _TmnxBsxRadApServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 6),
    _TmnxBsxRadApServerTimeout_Type()
)
tmnxBsxRadApServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxRadApServerTimeout.setUnits("seconds")


class _TmnxBsxRadApServerVRtrID_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxBsxRadApServerVRtrID based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxBsxRadApServerVRtrID_Object = MibTableColumn
tmnxBsxRadApServerVRtrID = _TmnxBsxRadApServerVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 7),
    _TmnxBsxRadApServerVRtrID_Type()
)
tmnxBsxRadApServerVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServerVRtrID.setStatus("current")


class _TmnxBsxRadApServerSrcAddrType_Type(InetAddressType):
    """Custom type tmnxBsxRadApServerSrcAddrType based on InetAddressType"""


_TmnxBsxRadApServerSrcAddrType_Object = MibTableColumn
tmnxBsxRadApServerSrcAddrType = _TmnxBsxRadApServerSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 8),
    _TmnxBsxRadApServerSrcAddrType_Type()
)
tmnxBsxRadApServerSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServerSrcAddrType.setStatus("current")


class _TmnxBsxRadApServerSrcAddr_Type(InetAddress):
    """Custom type tmnxBsxRadApServerSrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxRadApServerSrcAddr_Type.__name__ = "InetAddress"
_TmnxBsxRadApServerSrcAddr_Object = MibTableColumn
tmnxBsxRadApServerSrcAddr = _TmnxBsxRadApServerSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 9),
    _TmnxBsxRadApServerSrcAddr_Type()
)
tmnxBsxRadApServerSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServerSrcAddr.setStatus("current")


class _TmnxBsxRadApServerAlgorithm_Type(TmnxSubRadServAlgorithm):
    """Custom type tmnxBsxRadApServerAlgorithm based on TmnxSubRadServAlgorithm"""


_TmnxBsxRadApServerAlgorithm_Object = MibTableColumn
tmnxBsxRadApServerAlgorithm = _TmnxBsxRadApServerAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 10),
    _TmnxBsxRadApServerAlgorithm_Type()
)
tmnxBsxRadApServerAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServerAlgorithm.setStatus("current")


class _TmnxBsxRadApIntrmUpdateInterval_Type(Unsigned32):
    """Custom type tmnxBsxRadApIntrmUpdateInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 1080),
    )


_TmnxBsxRadApIntrmUpdateInterval_Type.__name__ = "Unsigned32"
_TmnxBsxRadApIntrmUpdateInterval_Object = MibTableColumn
tmnxBsxRadApIntrmUpdateInterval = _TmnxBsxRadApIntrmUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 11),
    _TmnxBsxRadApIntrmUpdateInterval_Type()
)
tmnxBsxRadApIntrmUpdateInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApIntrmUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBsxRadApIntrmUpdateInterval.setUnits("minutes")


class _TmnxBsxRadApSignfcntChangeDelta_Type(Unsigned32):
    """Custom type tmnxBsxRadApSignfcntChangeDelta based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TmnxBsxRadApSignfcntChangeDelta_Type.__name__ = "Unsigned32"
_TmnxBsxRadApSignfcntChangeDelta_Object = MibTableColumn
tmnxBsxRadApSignfcntChangeDelta = _TmnxBsxRadApSignfcntChangeDelta_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 2, 1, 12),
    _TmnxBsxRadApSignfcntChangeDelta_Type()
)
tmnxBsxRadApSignfcntChangeDelta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApSignfcntChangeDelta.setStatus("current")
_TmnxBsxRadApServTable_Object = MibTable
tmnxBsxRadApServTable = _TmnxBsxRadApServTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxRadApServTable.setStatus("current")
_TmnxBsxRadApServEntry_Object = MibTableRow
tmnxBsxRadApServEntry = _TmnxBsxRadApServEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 3, 1)
)
tmnxBsxRadApServEntry.setIndexNames(
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxRadApName"),
    (0, "TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServIndex"),
)
if mibBuilder.loadTexts:
    tmnxBsxRadApServEntry.setStatus("current")


class _TmnxBsxRadApServIndex_Type(Unsigned32):
    """Custom type tmnxBsxRadApServIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxBsxRadApServIndex_Type.__name__ = "Unsigned32"
_TmnxBsxRadApServIndex_Object = MibTableColumn
tmnxBsxRadApServIndex = _TmnxBsxRadApServIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 3, 1, 1),
    _TmnxBsxRadApServIndex_Type()
)
tmnxBsxRadApServIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBsxRadApServIndex.setStatus("current")
_TmnxBsxRadApServRowStatus_Type = RowStatus
_TmnxBsxRadApServRowStatus_Object = MibTableColumn
tmnxBsxRadApServRowStatus = _TmnxBsxRadApServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 3, 1, 2),
    _TmnxBsxRadApServRowStatus_Type()
)
tmnxBsxRadApServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServRowStatus.setStatus("current")
_TmnxBsxRadApServRowLastChange_Type = TimeStamp
_TmnxBsxRadApServRowLastChange_Object = MibTableColumn
tmnxBsxRadApServRowLastChange = _TmnxBsxRadApServRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 3, 1, 3),
    _TmnxBsxRadApServRowLastChange_Type()
)
tmnxBsxRadApServRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApServRowLastChange.setStatus("current")
_TmnxBsxRadApServAddrType_Type = InetAddressType
_TmnxBsxRadApServAddrType_Object = MibTableColumn
tmnxBsxRadApServAddrType = _TmnxBsxRadApServAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 3, 1, 4),
    _TmnxBsxRadApServAddrType_Type()
)
tmnxBsxRadApServAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServAddrType.setStatus("current")


class _TmnxBsxRadApServAddr_Type(InetAddress):
    """Custom type tmnxBsxRadApServAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBsxRadApServAddr_Type.__name__ = "InetAddress"
_TmnxBsxRadApServAddr_Object = MibTableColumn
tmnxBsxRadApServAddr = _TmnxBsxRadApServAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 3, 1, 5),
    _TmnxBsxRadApServAddr_Type()
)
tmnxBsxRadApServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServAddr.setStatus("current")


class _TmnxBsxRadApServSecret_Type(DisplayString):
    """Custom type tmnxBsxRadApServSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 20),
    )


_TmnxBsxRadApServSecret_Type.__name__ = "DisplayString"
_TmnxBsxRadApServSecret_Object = MibTableColumn
tmnxBsxRadApServSecret = _TmnxBsxRadApServSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 3, 1, 6),
    _TmnxBsxRadApServSecret_Type()
)
tmnxBsxRadApServSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServSecret.setStatus("current")


class _TmnxBsxRadApServAcctPort_Type(Unsigned32):
    """Custom type tmnxBsxRadApServAcctPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxBsxRadApServAcctPort_Type.__name__ = "Unsigned32"
_TmnxBsxRadApServAcctPort_Object = MibTableColumn
tmnxBsxRadApServAcctPort = _TmnxBsxRadApServAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 3, 1, 7),
    _TmnxBsxRadApServAcctPort_Type()
)
tmnxBsxRadApServAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBsxRadApServAcctPort.setStatus("current")
_TmnxBsxRadApServOperState_Type = TmnxOperState
_TmnxBsxRadApServOperState_Object = MibTableColumn
tmnxBsxRadApServOperState = _TmnxBsxRadApServOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 3, 1, 8),
    _TmnxBsxRadApServOperState_Type()
)
tmnxBsxRadApServOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApServOperState.setStatus("current")
_TmnxBsxRadApStatTable_Object = MibTable
tmnxBsxRadApStatTable = _TmnxBsxRadApStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxRadApStatTable.setStatus("current")
_TmnxBsxRadApStatEntry_Object = MibTableRow
tmnxBsxRadApStatEntry = _TmnxBsxRadApStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxBsxRadApStatEntry.setStatus("current")
_TmnxBsxRadApTxRequests_Type = Counter32
_TmnxBsxRadApTxRequests_Object = MibTableColumn
tmnxBsxRadApTxRequests = _TmnxBsxRadApTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 4, 1, 1),
    _TmnxBsxRadApTxRequests_Type()
)
tmnxBsxRadApTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApTxRequests.setStatus("current")
_TmnxBsxRadApRxResponses_Type = Counter32
_TmnxBsxRadApRxResponses_Object = MibTableColumn
tmnxBsxRadApRxResponses = _TmnxBsxRadApRxResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 4, 1, 2),
    _TmnxBsxRadApRxResponses_Type()
)
tmnxBsxRadApRxResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApRxResponses.setStatus("current")
_TmnxBsxRadApReqTimeouts_Type = Counter32
_TmnxBsxRadApReqTimeouts_Object = MibTableColumn
tmnxBsxRadApReqTimeouts = _TmnxBsxRadApReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 4, 1, 3),
    _TmnxBsxRadApReqTimeouts_Type()
)
tmnxBsxRadApReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApReqTimeouts.setStatus("current")
_TmnxBsxRadApSendRetries_Type = Counter32
_TmnxBsxRadApSendRetries_Object = MibTableColumn
tmnxBsxRadApSendRetries = _TmnxBsxRadApSendRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 4, 1, 4),
    _TmnxBsxRadApSendRetries_Type()
)
tmnxBsxRadApSendRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApSendRetries.setStatus("current")
_TmnxBsxRadApSendFail_Type = Counter32
_TmnxBsxRadApSendFail_Object = MibTableColumn
tmnxBsxRadApSendFail = _TmnxBsxRadApSendFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 4, 1, 5),
    _TmnxBsxRadApSendFail_Type()
)
tmnxBsxRadApSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApSendFail.setStatus("current")
_TmnxBsxRadApServStatTable_Object = MibTable
tmnxBsxRadApServStatTable = _TmnxBsxRadApServStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 5)
)
if mibBuilder.loadTexts:
    tmnxBsxRadApServStatTable.setStatus("current")
_TmnxBsxRadApServStatEntry_Object = MibTableRow
tmnxBsxRadApServStatEntry = _TmnxBsxRadApServStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxBsxRadApServStatEntry.setStatus("current")
_TmnxBsxRadApServTxRequests_Type = Counter32
_TmnxBsxRadApServTxRequests_Object = MibTableColumn
tmnxBsxRadApServTxRequests = _TmnxBsxRadApServTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 5, 1, 1),
    _TmnxBsxRadApServTxRequests_Type()
)
tmnxBsxRadApServTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApServTxRequests.setStatus("current")
_TmnxBsxRadApServRxResponses_Type = Counter32
_TmnxBsxRadApServRxResponses_Object = MibTableColumn
tmnxBsxRadApServRxResponses = _TmnxBsxRadApServRxResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 5, 1, 2),
    _TmnxBsxRadApServRxResponses_Type()
)
tmnxBsxRadApServRxResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApServRxResponses.setStatus("current")
_TmnxBsxRadApServReqTimeouts_Type = Counter32
_TmnxBsxRadApServReqTimeouts_Object = MibTableColumn
tmnxBsxRadApServReqTimeouts = _TmnxBsxRadApServReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 5, 1, 3),
    _TmnxBsxRadApServReqTimeouts_Type()
)
tmnxBsxRadApServReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApServReqTimeouts.setStatus("current")
_TmnxBsxRadApServReqSendFail_Type = Counter32
_TmnxBsxRadApServReqSendFail_Object = MibTableColumn
tmnxBsxRadApServReqSendFail = _TmnxBsxRadApServReqSendFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 63, 12, 5, 1, 4),
    _TmnxBsxRadApServReqSendFail_Type()
)
tmnxBsxRadApServReqSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBsxRadApServReqSendFail.setStatus("current")
_TmnxBsxNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxBsxNotifyPrefix = _TmnxBsxNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63)
)
_TmnxBsxNotifications_ObjectIdentity = ObjectIdentity
tmnxBsxNotifications = _TmnxBsxNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0)
)
tmnxBsxAaGrpPartEntry.registerAugmentions(
    ("TIMETRA-BSX-NG-MIB",
     "tmnxBsxAaWap1xEntry")
)
tmnxBsxAaWap1xEntry.setIndexNames(*tmnxBsxAaGrpPartEntry.getIndexNames())
tmnxBsxAarpInstEntry.registerAugmentions(
    ("TIMETRA-BSX-NG-MIB",
     "tmnxBsxAarpCommandEntry")
)
tmnxBsxAarpCommandEntry.setIndexNames(*tmnxBsxAarpInstEntry.getIndexNames())
tmnxBsxRadApEntry.registerAugmentions(
    ("TIMETRA-BSX-NG-MIB",
     "tmnxBsxRadApStatEntry")
)
tmnxBsxRadApStatEntry.setIndexNames(*tmnxBsxRadApEntry.getIndexNames())
tmnxBsxRadApServEntry.registerAugmentions(
    ("TIMETRA-BSX-NG-MIB",
     "tmnxBsxRadApServStatEntry")
)
tmnxBsxRadApServStatEntry.setIndexNames(*tmnxBsxRadApServEntry.getIndexNames())

# Managed Objects groups

tmnxBsxMdaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 1)
)
tmnxBsxMdaGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFcLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpMdaLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpOperState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFailToMode"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubPool"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubResvCbs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubSlpPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubQuePolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubSchPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubPool"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubResvCbs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubSlpPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubQuePolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubSchPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpIngressPool"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpIngressResvCbs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpIngressSlpPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpIngressQuePolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFcRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFcRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaActivityState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaActivityChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaRole"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpActivityChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsInPChipErs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsDiscCongIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsDiscCongIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsToMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsToMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsDisCongMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsDisCongMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsDiscErrors"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsDiscErrors"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsPolicyByps"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsPolicyByps"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsInspected"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsInspected"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsDiscPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsDiscPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsInMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsInMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsFromMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsFromMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsOutPChipEr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsDisCongOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsDisCongOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlows"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlowsCurrent"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlowSetupRate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusSubsDiverted"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusSubsCurrent"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusTrafficRate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsInPChipErs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsDiscCongIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsDiscCongIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsToMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsToMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsDisCongMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsDisCongMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsDiscErrors"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsDiscErrors"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsPolicyByps"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsPolicyByps"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsInspected"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsInspected"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsDiscPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsDiscPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsInMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsInMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsFromMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsFromMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsOutPChipEr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsDisCongOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsDisCongOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCFlows"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQFwdInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQFwdOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQFwdInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQFwdOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQDroInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQDroOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQDroInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQDroOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCFwdInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCFwdOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCFwdInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCFwdOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCDroInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCDroOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCDroInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCDroOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQFwdInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQFwdOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQFwdInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQFwdOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDroInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDroOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDroInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDroOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCFwdInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCFwdOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCFwdInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCFwdOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCDroInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCDroOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCDroInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCDroOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaEsmSubscribers"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaSapSubscribers"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumMdaSlotNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumMdaMdaNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumAppProfName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumOctsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumPktsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumFlwsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumOctsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumPktsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumFlwsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumOctsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumPktsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumFlwsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumOctsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumPktsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumFlwsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumTermFlwDur"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumTermFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumShrtDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumMedDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumLngDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumActFlwsFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumActFlwsToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCOctsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCPktsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCFlwsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCOctsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCPktsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCFlwsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCOctsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCPktsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCFlwsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCOctsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCPktsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCFlwsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCTermFlwDur"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCTermFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCShrtDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCMedDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCLngDurFlws"))
)
if mibBuilder.loadTexts:
    tmnxBsxMdaGroup.setStatus("obsolete")

tmnxBsxPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 2)
)
tmnxBsxPolicyGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxProtDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpStorageType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppStorageType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppAppGroup"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterProtocol"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterProtocolOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterFlowSetupDir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterIpProtocolNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterIpProtocolNumOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrLen"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPort"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortFpp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterApplication"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprStr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoDefValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoValRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfDivert"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerGranularity"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAction"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAdminPIR"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAdminCIR"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerCBS"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerMBS"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerCIRAdaptation"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerPIRAdaptation"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpApplication"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpApplicationOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAppGroup"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAppGroupOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpTrafficDir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSubscriber"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSubscriberOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDscp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDscpOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDrop"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpBwLimitPolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpFlowRatePolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpFlowCountPolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminOwner"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminControlApply"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxUpgrade"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxVersion"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsFlows"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowFullHighWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowFullLowWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpCharRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpCharOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsConflicts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSapSubscrPortId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSapSubscrEncapValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSapSubscrOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddress"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressLength"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortLowValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortHighValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddress"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressLength"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortLowValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortHighValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkFc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkPriority"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkDscpInProfile"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkDscpOutProfile"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpMirrorSource"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpMirrorSourceAllIncl"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlConfigOwner"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlApply"))
)
if mibBuilder.loadTexts:
    tmnxBsxPolicyGroup.setStatus("obsolete")

tmnxBsxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 3)
)
tmnxBsxStatsGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAcctLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAcctCfgCollStats"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAcctCfgPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubOctsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubPktsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubFlwsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubOctsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubPktsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubFlwsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubOctsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubPktsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubFlwsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubOctsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubPktsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubFlwsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubTermFlwDur"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubTermFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubShrtDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubMedDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubLngDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubActFlwsFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubActFlwsToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCOctsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCPktsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCFlwsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCOctsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCPktsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCFlwsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCOctsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCPktsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCFlwsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCOctsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCPktsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCFlwsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCTermFlwDur"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCTermFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCShrtDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCMedDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubHCLngDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyOctsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyPktsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyFlwsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyOctsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyPktsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyFlwsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyOctsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyPktsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyFlwsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyOctsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyPktsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyFlwsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyTermFlwDur"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyTermFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyShrtDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyMedDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyLngDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyActFlwsFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyActFlwsToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCOctsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCPktsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCFlwsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCOctsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCPktsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCFlwsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCOctsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCPktsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCFlwsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCOctsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCPktsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCFlwsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCTermFlwDur"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCTermFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCShrtDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCMedDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyHCLngDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubCfgRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubSdyRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaOctsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaPktsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaFlwsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaOctsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaPktsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaFlwsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaOctsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaPktsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaFlwsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaOctsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaPktsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaFlwsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaTermFlwDur"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaTermFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaShrtDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaMedDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaLngDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaActFlwsFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaActFlwsToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaNumSubscribers"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCOctsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCPktsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCFlwsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCOctsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCPktsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCFlwsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCOctsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCPktsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCFlwsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCOctsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCPktsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCFlwsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCTermFlwDur"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCTermFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCShrtDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCMedDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaHCLngDurFlws"))
)
if mibBuilder.loadTexts:
    tmnxBsxStatsGroup.setStatus("current")

tmnxBsxNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 4)
)
tmnxBsxNotifyObjsGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActionStatus"))
)
if mibBuilder.loadTexts:
    tmnxBsxNotifyObjsGroup.setStatus("current")

tmnxBsxMdaGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 6, 1)
)
tmnxBsxMdaGroupV7v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFcLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpMdaLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpOperState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFailToMode"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubPool"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubResvCbs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubSlpPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubQuePolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubSchPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubPool"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubResvCbs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubSlpPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubQuePolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubSchPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFcRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFcRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaActivityState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaActivityChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaRole"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpActivityChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsInPChipErs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsDiscCongIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsDiscCongIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsToMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsToMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsDisCongMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsDisCongMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsDiscErrors"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsDiscErrors"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsPolicyByps"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsPolicyByps"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsInspected"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsInspected"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsDiscPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsDiscPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsInMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsInMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsFromMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsFromMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsOutPChipEr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsDisCongOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsDisCongOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusOctsOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktsOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlows"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlowsCurrent"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlowSetupRate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusSubsDiverted"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusSubsCurrent"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusTrafficRate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsInPChipErs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsDiscCongIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsDiscCongIn"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsToMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsToMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsDisCongMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsDisCongMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsDiscErrors"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsDiscErrors"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsPolicyByps"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsPolicyByps"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsInspected"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsInspected"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsDiscPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsDiscPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsInMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsInMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsFromMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsFromMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsOutPChipEr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsDisCongOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsDisCongOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCOctsOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktsOut"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCFlows"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQFwdInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQFwdOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQFwdInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQFwdOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQDroInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQDroOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQDroInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQDroOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCFwdInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCFwdOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCFwdInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCFwdOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCDroInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCDroOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCDroInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusIngQHCDroOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQFwdInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQFwdOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQFwdInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQFwdOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDroInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDroOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDroInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQDroOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCFwdInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCFwdOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCFwdInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCFwdOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCDroInPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCDroOutPPkts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCDroInPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusEgrQHCDroOutPOcts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaEsmSubscribers"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaSapSubscribers"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumMdaSlotNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumMdaMdaNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumAppProfName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumOctsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumPktsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumFlwsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumOctsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumPktsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumFlwsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumOctsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumPktsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumFlwsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumOctsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumPktsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumFlwsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumTermFlwDur"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumTermFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumShrtDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumMedDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumLngDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumActFlwsFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumActFlwsToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCOctsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCPktsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCFlwsAdmFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCOctsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCPktsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCFlwsDnyFmSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCOctsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCPktsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCFlwsAdmToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCOctsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCPktsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCFlwsDnyToSb"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCTermFlwDur"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCTermFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCShrtDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCMedDurFlws"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubSumHCLngDurFlws"))
)
if mibBuilder.loadTexts:
    tmnxBsxMdaGroupV7v0.setStatus("current")

tmnxBsxMdaGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 6, 2)
)
tmnxBsxMdaGroupV8v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpPartitions"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpCapCostLowThres"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpCapCostHighThres"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpLoadBalanceStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpUnassignedEsmSubs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpUnassignedSapSubs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpUnassignedSpkSubs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpAaSubScale"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpOverloadCutThru"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaSpokeSdpSubscribers"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaCapacityCost"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaStatsResourceCount"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlowsAverage"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlowsPeak"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlowSetupRateAvg"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlowSetupRatePk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusSubsDivertedAvg"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusSubsDivertedPk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusSubsAverage"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusSubsPeak"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusTrafficRateAvg"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusTrafficRatePeak"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaLoadBalUnSub"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubMdaSlotNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubMdaMdaNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubAppProfName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubHasOverrides"))
)
if mibBuilder.loadTexts:
    tmnxBsxMdaGroupV8v0.setStatus("current")

tmnxBsxMdaGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 6, 3)
)
tmnxBsxMdaGroupV9v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPacketRate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPacketRateAvg"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPacketRatePeak"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlowResInUse"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransitIpSubs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransitIpAddrs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransitSubs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransPrefEntries"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubWaSBfHiWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubWaSBfLoWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubWaSBfHiWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubWaSBfLoWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubTransitIpPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubTransPrefPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpTransPrefV4NmEntr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaLoadBalUnSubTransit"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartXOnlineHost"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartHttpMatchAllReq"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktSzIncPk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzIncPkLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzIncPkHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktSzDecPk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzDecPkLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzDecPkHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktSzIncOc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzIncOcLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzIncOcHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktSzDecOc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzDecOcLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzDecOcHi"))
)
if mibBuilder.loadTexts:
    tmnxBsxMdaGroupV9v0.setStatus("obsolete")

tmnxBsxMdaGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 6, 4)
)
tmnxBsxMdaGroupV10v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPacketRate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPacketRateAvg"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPacketRatePeak"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusFlowResInUse"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransitIpSubs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransitIpAddrs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransitSubs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubWaSBfHiWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubWaSBfLoWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubWaSBfHiWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubWaSBfLoWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubTransitIpPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubTransPrefPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpTransPrefV4NmEntr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaLoadBalUnSubTransit"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartXOnlineHost"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartHttpMatchAllReq"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartAaSubRemote"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktSzIncPk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzIncPkLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzIncPkHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktSzDecPk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzDecPkLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzDecPkHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktSzIncOc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzIncOcLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzIncOcHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusHCPktSzDecOc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzDecOcLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpStatusPktSzDecOcHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpTransPrefV6NmEntr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpTransPrefV6RmEntr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransPrefV4Entr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransPrefV6Entr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransPrefV6RemEntr"))
)
if mibBuilder.loadTexts:
    tmnxBsxMdaGroupV10v0.setStatus("current")

tmnxBsxMdaGroupMG3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 6, 5)
)
tmnxBsxMdaGroupMG3v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartXOnlineHost"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaGrpPartHttpMatchAllReq"))
)
if mibBuilder.loadTexts:
    tmnxBsxMdaGroupMG3v0.setStatus("obsolete")

tmnxBsxObsoleteGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 7, 1)
)
tmnxBsxObsoleteGroupV7v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpIngressPool"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpIngressResvCbs"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpIngressSlpPolicy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpIngressQuePolicy"))
)
if mibBuilder.loadTexts:
    tmnxBsxObsoleteGroupV7v0.setStatus("current")

tmnxBsxObsoleteGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 7, 2)
)
tmnxBsxObsoleteGroupV8v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminOwner"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminControlApply"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPort"))
)
if mibBuilder.loadTexts:
    tmnxBsxObsoleteGroupV8v0.setStatus("current")

tmnxBsxObsoleteGroupsV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 7, 3)
)
tmnxBsxObsoleteGroupsV9v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsFlows"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsConflicts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSubscriber"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSubscriberOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSapSubscrPortId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSapSubscrEncapValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSapSubscrOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSpokeSdpSubscr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSpokeSdpSubscrOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpUnassignedTIpSubs"))
)
if mibBuilder.loadTexts:
    tmnxBsxObsoleteGroupsV9v0.setStatus("current")

tmnxBsxObsoleteGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 7, 4)
)
tmnxBsxObsoleteGroupV10v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxGrpMdaTransPrefEntries"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpAdminState"))
)
if mibBuilder.loadTexts:
    tmnxBsxObsoleteGroupV10v0.setStatus("current")

tmnxBsxPolicyGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 8, 1)
)
tmnxBsxPolicyGroupV8v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxProtDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxProtParentName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxProtAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpStorageType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppStorageType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppAppGroup"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterProtocol"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterProtocolOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterFlowSetupDir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterIpProtocolNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterIpProtocolNumOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrLen"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortFpp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortLow"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortHigh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterApplication"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprStr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoDefValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoValRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfDivert"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCapacityCost"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerGranularity"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAction"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAdminPIR"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAdminCIR"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerCBS"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerMBS"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerCIRAdaptation"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerPIRAdaptation"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpApplication"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpApplicationOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAppGroup"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAppGroupOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpTrafficDir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSubscriber"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSubscriberOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDscp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDscpOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDrop"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpBwLimitPolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpFlowRatePolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpFlowCountPolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxUpgrade"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxVersion"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsFlows"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowFullHighWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowFullLowWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpCharRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpCharOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsConflicts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSapSubscrPortId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSapSubscrEncapValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSapSubscrOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddress"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressLength"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortLowValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortHighValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddress"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressLength"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortLowValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortHighValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSpokeSdpSubscr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSpokeSdpSubscrOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkFc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkPriority"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkDscpInProfile"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkDscpOutProfile"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpMirrorSource"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpMirrorSourceAllIncl"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlConfigOwner"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlApply"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtIpProtocolNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprOffset"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprDirection"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprStr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubAsoValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubAsoValDerivedFrom"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolicerAqpEntryId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolicerName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolResExStatus"))
)
if mibBuilder.loadTexts:
    tmnxBsxPolicyGroupV8v0.setStatus("obsolete")

tmnxBsxPolicyGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 8, 2)
)
tmnxBsxPolicyGroupV9v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxProtDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxProtParentName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxProtAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpStorageType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppStorageType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppAppGroup"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterProtocol"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterProtocolOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterFlowSetupDir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterIpProtocolNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterIpProtocolNumOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrLen"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortFpp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortLow"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortHigh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterApplication"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprStr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoDefValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoValRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfDivert"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCapacityCost"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerGranularity"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAction"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAdminPIR"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAdminCIR"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerCBS"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerMBS"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerCIRAdaptation"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerPIRAdaptation"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpApplication"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpApplicationOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAppGroup"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAppGroupOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpTrafficDir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDscp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDscpOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDrop"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpBwLimitPolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpFlowRatePolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpFlowCountPolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxUpgrade"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxVersion"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowFullHighWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowFullLowWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpCharRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpCharOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddress"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressLength"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortLowValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortHighValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddress"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressLength"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortLowValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortHighValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkFc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkPriority"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkDscpInProfile"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkDscpOutProfile"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpMirrorSource"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpMirrorSourceAllIncl"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlConfigOwner"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlApply"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtIpProtocolNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprOffset"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprDirection"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprStr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubAsoValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubAsoValDerivedFrom"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolicerAqpEntryId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolicerName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolResExStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAaSubscriberType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAaSubscriber"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAaSubscriberOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowSetupHighWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowSetupLowWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPacketRateHighWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPacketRateLowWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxBitRateHighWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxBitRateLowWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsHCFlows"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsFlowsLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsFlowsHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsHCConflicts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsConflictsLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsConflictsHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpHttpErrRedirName"))
)
if mibBuilder.loadTexts:
    tmnxBsxPolicyGroupV9v0.setStatus("obsolete")

tmnxBsxPolicyGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 8, 3)
)
tmnxBsxPolicyGroupV10v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxProtDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxProtParentName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxProtAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxProtObsolete"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpStorageType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppStorageType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppAppGroup"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterProtocol"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterProtocolOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterFlowSetupDir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterIpProtocolNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterIpProtocolNumOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrLen"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerAddrOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortFpp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortLow"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterServerPortHigh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterApplication"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppFilterExprStr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoDefValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAsoValRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfDivert"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCapacityCost"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppProfCharValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerGranularity"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAction"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAdminPIR"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerAdminCIR"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerCBS"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerMBS"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerCIRAdaptation"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPolicerPIRAdaptation"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpApplication"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpApplicationOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAppGroup"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAppGroupOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpTrafficDir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDscp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDscpOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDrop"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpBwLimitPolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpFlowRatePolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpFlowCountPolicer"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxUpgrade"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxVersion"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowFullHighWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowFullLowWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpCharRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpCharOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddress"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressLength"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcAddressOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortLowValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpSrcPortHighValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddress"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressLength"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstAddressOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortLowValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpDstPortHighValue"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkFc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkPriority"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkDscpInProfile"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpRemarkDscpOutProfile"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpMirrorSource"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpMirrorSourceAllIncl"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlConfigOwner"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAdminCtrlApply"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtIpProtocolNum"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprOffset"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprDirection"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprOperator"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCustProtExprStr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubAsoValName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubAsoValDerivedFrom"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolicerAqpEntryId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolicerName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolResExStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAaSubscriberType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAaSubscriber"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpAaSubscriberOp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowSetupHighWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowSetupLowWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPacketRateHighWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPacketRateLowWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxBitRateHighWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxBitRateLowWatermark"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsHCFlows"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsFlowsLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsFlowsHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsHCConflicts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsConflictsLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpStatsConflictsHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpHttpErrRedirName"))
)
if mibBuilder.loadTexts:
    tmnxBsxPolicyGroupV10v0.setStatus("current")

tmnxBsxCflowdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 11, 1)
)
tmnxBsxCflowdGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdPerfLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdPerfExpLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdVolRate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdTemplateRetransmit"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollOperState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollVersion"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdPerfRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdPerfFlowRate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdPerfExpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdPerfExpRowLastChnge"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusRecReported"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusRecDropped"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusPktsSent"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusFlowsNoRes"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusActFlowsCurr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusRecRateCurr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusPktRateCurr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusHCRecReported"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusHCRecDropped"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusHCPktsSent"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusHCFlowsNoRes"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollStatDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollStatRecSent"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdCollStatHCRecSent"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpStatDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpStatRecReport"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpStatHCRecReport"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpStatRecDropped"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpStatHCRecDropped"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpStatFlowsNoRes"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpStatHCFlowsNoRes"))
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdGroup.setStatus("current")

tmnxBsxCflowdGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 11, 2)
)
tmnxBsxCflowdGroupV9v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusHCUSupSSRCSt"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusUSupSSRCStLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdStatusUSupSSRCStHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpStatHCUSupSSRCSt"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpStatUSupSSRCStLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdExpStatUSupSSRCStHi"))
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdGroupV9v0.setStatus("current")

tmnxBsxCflowdGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 11, 3)
)
tmnxBsxCflowdGroupV10v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdPerfFlowRate2"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxCflowdPerfExpRateNum"))
)
if mibBuilder.loadTexts:
    tmnxBsxCflowdGroupV10v0.setStatus("current")

tmnxBsxOvrdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 12, 1)
)
tmnxBsxOvrdGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxOvrdAaSubLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxOvrdAaSubCharLastChTm"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxOvrdAaSubRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxOvrdAaSubRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxOvrdAaSubCharRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxOvrdAaSubCharRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxOvrdAaSubCharValName"))
)
if mibBuilder.loadTexts:
    tmnxBsxOvrdGroup.setStatus("current")

tmnxBsxNotifyObjsGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 13, 1)
)
tmnxBsxNotifyObjsGroupV7v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaSubscriberType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaSubscriberName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaSubAcctLossReason"))
)
if mibBuilder.loadTexts:
    tmnxBsxNotifyObjsGroupV7v0.setStatus("current")

tmnxBsxNotifyObjsGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 13, 2)
)
tmnxBsxNotifyObjsGroupV8v0.setObjects(
    ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex")
)
if mibBuilder.loadTexts:
    tmnxBsxNotifyObjsGroupV8v0.setStatus("current")

tmnxBsxNotifyObjsGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 13, 3)
)
tmnxBsxNotifyObjsGroupV9v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyRadiusCoAAuditState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyReason"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyTransitIpPolicyId"))
)
if mibBuilder.loadTexts:
    tmnxBsxNotifyObjsGroupV9v0.setStatus("current")

tmnxBsxTransitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 14, 1)
)
tmnxBsxTransitGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPlcySubLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPlcyAddrLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyDesc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyDefAppProf"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicySubIdPlcy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyRadius"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyRadAuthPlc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyDhcp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPlcySubRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPlcySubRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPlcySubAppProfNm"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPlcySubRefCount"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPlcyAddrRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPlcyAddrRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPlcyAddrSubscriber"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpSumParentSubType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpSumParentSub"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpSumAppProfNm"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpSumIpOriginMask"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpSumUpdateTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPlcyLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSubLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntryLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicyRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicyRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicyDesc"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSubRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSubRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSubIsRemote"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSubAppProfNm"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSubRefCount"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntryRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntryRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntrySubAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntrySubAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntrySubAddrLen"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntryNetAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntryNetAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntryNetAddrLen"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefEntrySubscriber"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSumSubAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSumSubAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSumSubAddrLen"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSumNetAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSumNetAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSumNetAddrLen"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSumUpdateTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSumParentSubType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSumParentSub"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefSumAppProfNm"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicySubsCount"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyIPv4EntCnt"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicySubsCount"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicyEntCount"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicyIPv4EntCnt"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransitGroup.setStatus("current")

tmnxBsxTransitGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 14, 2)
)
tmnxBsxTransitGroupV10v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyIPv6PfxLen"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyIPv6EntCnt"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransPrefPolicyIPv6EntCnt"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransitGroupV10v0.setStatus("current")

tmnxBsxTransitSeenIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 14, 3)
)
tmnxBsxTransitSeenIpGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicySeenIp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicyAutoCreate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPolicySeenIpRad"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPeerEPSapPortId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPeerEPSapEncap"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPeerEPSapEncType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPeerEPSdpBindId"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransitSeenIpGroup.setStatus("current")

tmnxBsxStatsGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 15, 1)
)
tmnxBsxStatsGroupV9v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAcctCfgAggrStats"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAppFilterHCFlows"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAppFilterFlowsLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAppFilterFlowsHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAppFilterFlowHCOctC"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAppFilterFlowOctCLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAppFilterFlowOctCHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAcctCfgAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAcctCfgMaxThruStats"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatIsaAaCfgLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatIsaAaCfgCollStats"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatIsaAaCfgPolicy"))
)
if mibBuilder.loadTexts:
    tmnxBsxStatsGroupV9v0.setStatus("current")

tmnxBsxMobileGatewayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 16, 1)
)
tmnxBsxMobileGatewayGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxAaWap1xLastChangeTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaWap1xRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaWap1xAdminState"))
)
if mibBuilder.loadTexts:
    tmnxBsxMobileGatewayGroup.setStatus("current")

tmnxBsxHttpRedirErrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 17, 1)
)
tmnxBsxHttpRedirErrGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrCodeLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrEnabled"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrTemplateId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrHttpHost"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrParticipantId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrCodeRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrCodeRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirErrorCodeMsgSize"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatHCRedir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatRedirLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatRedirHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatHCSizeExceeded"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatSizeExceededLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatSizeExceededHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatHCOutOfResource"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatOutOfResourceLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatOutOfResourceHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatHCNotRedirFType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatNotRedirFTypeLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatNotRedirFTypeHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatHCNotRedir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatNotRedirLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRdStatNotRedirHi"))
)
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirErrGroup.setStatus("current")

tmnxBsxHttpRedirGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 17, 2)
)
tmnxBsxHttpRedirGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirEnabled"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirTemplateId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpRedirHttpHost"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpHttpRedirName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpHttpRedirFlowType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpPcyRdStatDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpPcyRdStatHCRedir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpPcyRdStatRedirLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpPcyRdStatRedirHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpPcyRdStatHCOutOfRes"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpPcyRdStatOutOfResLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpPcyRdStatOutOfResHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpPcyRdStatHCNotRedir"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpPcyRdStatNotRedirLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpPcyRdStatNotRedirHi"))
)
if mibBuilder.loadTexts:
    tmnxBsxHttpRedirGroup.setStatus("current")

tmnxBsxStaticObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 18, 1)
)
tmnxBsxStaticObjGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxTListTableLastUpdateT"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTListAttribTableLUpdateT"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTListRowLastUpdateT"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTListDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTListAttribRowLastUpdateT"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTListAttribType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTListAttribValue"))
)
if mibBuilder.loadTexts:
    tmnxBsxStaticObjGroup.setStatus("current")

tmnxBsxRedundancyObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 19, 1)
)
tmnxBsxRedundancyObjGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpTableLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPeerIpType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPeerIpAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPriority"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstAdminState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstOperState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstOperFlags"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPeerPriority"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPeerState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPeerOperFlags"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstPeerSubRefType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpCommandControl"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpServPointType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpServPoint"))
)
if mibBuilder.loadTexts:
    tmnxBsxRedundancyObjGroup.setStatus("current")

tmnxBsxHttpEnrichObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 20, 1)
)
tmnxBsxHttpEnrichObjGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichFieldLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichEnabled"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichFieldRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichFieldRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichFieldHeaderName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAqpHttpEnrichName"))
)
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichObjGroup.setStatus("current")

tmnxBsxHttpEnrichStatObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 20, 2)
)
tmnxBsxHttpEnrichStatObjGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichStatDiscontTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichHCNumEnriched"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichNumEnrichedLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichNumEnrichedHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichHCNumNoResource"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichNumNoResourceLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichNumNoResourceHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichHCMissngSubData"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichMissngSubDataLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichMissngSubDataHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichHCTplNotEnabled"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichTplNotEnabledLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichTplNotEnabledHi"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichHCTrafficChar"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichTrafficCharLo"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxHttpEnrichTrafficCharHi"))
)
if mibBuilder.loadTexts:
    tmnxBsxHttpEnrichStatObjGroup.setStatus("current")

tmnxBsxRadiusAccountingObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 21, 1)
)
tmnxBsxRadiusAccountingObjGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxAppChargeGrp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAppGrpChargeGrp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxChargeGrpRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxChargeGrpDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxChargeGrpExportId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxChargeGrpLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxChargeGrpRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPlcyCfgLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPlcyDefChargeGrp"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPlcyRowLastCh"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaAcctCfgRadiusPlcy"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxStatAaSubCfgExportMethod"))
)
if mibBuilder.loadTexts:
    tmnxBsxRadiusAccountingObjGroup.setStatus("current")

tmnxBsxRadApObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 21, 2)
)
tmnxBsxRadApObjGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServLastChTime"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServerRetry"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServerTimeout"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServerVRtrID"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServerSrcAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServerSrcAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServerAlgorithm"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApIntrmUpdateInterval"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApSignfcntChangeDelta"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServRowStatus"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServRowLastChange"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServSecret"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServAcctPort"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServOperState"))
)
if mibBuilder.loadTexts:
    tmnxBsxRadApObjGroup.setStatus("current")

tmnxBsxRadApStatObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 21, 3)
)
tmnxBsxRadApStatObjGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApTxRequests"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApRxResponses"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApReqTimeouts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApSendRetries"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApSendFail"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServTxRequests"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServRxResponses"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServReqTimeouts"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServReqSendFail"))
)
if mibBuilder.loadTexts:
    tmnxBsxRadApStatObjGroup.setStatus("current")


# Notification objects

tmnxBsxIsaAaGrpNonRedundantClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 1)
)
tmnxBsxIsaAaGrpNonRedundantClear.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpNonRedundantClear.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 2)
)
tmnxBsxIsaAaGrpSwitchover.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpSwitchover.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpFlowFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 3)
)
tmnxBsxIsaAaGrpFlowFull.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFlowFull.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpFlowFullClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 4)
)
tmnxBsxIsaAaGrpFlowFullClear.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFlowFullClear.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpFailureV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 5)
)
tmnxBsxIsaAaGrpFailureV2.setObjects(
    ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex")
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFailureV2.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpFailureClearV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 6)
)
tmnxBsxIsaAaGrpFailureClearV2.setObjects(
    ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex")
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFailureClearV2.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpNonRedundantV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 7)
)
tmnxBsxIsaAaGrpNonRedundantV2.setObjects(
    ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex")
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpNonRedundantV2.setStatus(
        "current"
    )

tmnxBsxIsaAaSubLoadBalance = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 8)
)
tmnxBsxIsaAaSubLoadBalance.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActionStatus"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaSubLoadBalance.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpCapCostThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 9)
)
tmnxBsxIsaAaGrpCapCostThres.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpCapCostHighThres"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpCapCostThres.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpCapCostThresClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 10)
)
tmnxBsxIsaAaGrpCapCostThresClear.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpCapCostLowThres"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpCapCostThresClear.setStatus(
        "current"
    )

tmnxBsxAaSubscribersUnassigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 11)
)
tmnxBsxAaSubscribersUnassigned.setObjects(
    ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex")
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubscribersUnassigned.setStatus(
        "current"
    )

tmnxBsxAaSubscriberAcctDataLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 12)
)
tmnxBsxAaSubscriberAcctDataLoss.setObjects(
      *(("TIMETRA-LOG-MIB", "tmnxLogFileIdLogId"),
        ("TIMETRA-LOG-MIB", "tmnxLogNotifyApInterval"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaSubscriberType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaSubscriberName"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaSubAcctLossReason"))
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubscriberAcctDataLoss.setStatus(
        "current"
    )

tmnxBsxAaSubPolResExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 13)
)
tmnxBsxAaSubPolResExceeded.setObjects(
    ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex")
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolResExceeded.setStatus(
        "current"
    )

tmnxBsxAaSubPolResExceededClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 14)
)
tmnxBsxAaSubPolResExceededClear.setObjects(
    ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex")
)
if mibBuilder.loadTexts:
    tmnxBsxAaSubPolResExceededClear.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpFlowSetup = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 15)
)
tmnxBsxIsaAaGrpFlowSetup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowSetupHighWatermark"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFlowSetup.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpFlowSetupClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 16)
)
tmnxBsxIsaAaGrpFlowSetupClear.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxFlowSetupLowWatermark"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFlowSetupClear.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpPacketRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 17)
)
tmnxBsxIsaAaGrpPacketRate.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPacketRateHighWatermark"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpPacketRate.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpPacketRateClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 18)
)
tmnxBsxIsaAaGrpPacketRateClear.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxPacketRateLowWatermark"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpPacketRateClear.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpBitRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 19)
)
tmnxBsxIsaAaGrpBitRate.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxBitRateHighWatermark"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpBitRate.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpBitRateClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 20)
)
tmnxBsxIsaAaGrpBitRateClear.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxBitRateLowWatermark"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpBitRateClear.setStatus(
        "current"
    )

tmnxBsxTransIpPolAaSubCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 21)
)
tmnxBsxTransIpPolAaSubCreated.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyTransitIpPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaSubscriberName"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransIpPolAaSubCreated.setStatus(
        "current"
    )

tmnxBsxTransIpPolAaSubDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 22)
)
tmnxBsxTransIpPolAaSubDeleted.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyTransitIpPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaSubscriberName"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransIpPolAaSubDeleted.setStatus(
        "current"
    )

tmnxBsxTransIpPolRadCoAAudit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 23)
)
tmnxBsxTransIpPolRadCoAAudit.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyTransitIpPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyRadiusCoAAuditState"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransIpPolRadCoAAudit.setStatus(
        "current"
    )

tmnxBsxTransIpPolRadCoAError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 24)
)
tmnxBsxTransIpPolRadCoAError.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyTransitIpPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyReason"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransIpPolRadCoAError.setStatus(
        "current"
    )

tmnxBsxTransIpPolRadDiscError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 25)
)
tmnxBsxTransIpPolRadDiscError.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyTransitIpPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyReason"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransIpPolRadDiscError.setStatus(
        "current"
    )

tmnxBsxTransIpPolDhcpAddWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 26)
)
tmnxBsxTransIpPolDhcpAddWarning.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyTransitIpPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyReason"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransIpPolDhcpAddWarning.setStatus(
        "current"
    )

tmnxBsxTransIpPolDhcpDelWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 27)
)
tmnxBsxTransIpPolDhcpDelWarning.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyTransitIpPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyReason"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransIpPolDhcpDelWarning.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpFmSbWaSBufOvld = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 28)
)
tmnxBsxIsaAaGrpFmSbWaSBufOvld.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubWaSBfHiWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFmSbWaSBufOvld.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpFmSbWaSBufOvldClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 29)
)
tmnxBsxIsaAaGrpFmSbWaSBufOvldClr.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFromSubWaSBfLoWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpFmSbWaSBufOvldClr.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpToSbWaSBufOvld = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 30)
)
tmnxBsxIsaAaGrpToSbWaSBufOvld.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubWaSBfHiWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSbWaSBufOvld.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpToSbWaSBufOvldClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 31)
)
tmnxBsxIsaAaGrpToSbWaSBufOvldClr.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSubWaSBfLoWmk"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpToSbWaSBufOvldClr.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpOvrldCutthru = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 32)
)
tmnxBsxIsaAaGrpOvrldCutthru.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpOvrldCutthru.setStatus(
        "current"
    )

tmnxBsxIsaAaGrpOvrldCutthruClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 33)
)
tmnxBsxIsaAaGrpOvrldCutthruClr.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyIsaAaGroupIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyActiveMda"))
)
if mibBuilder.loadTexts:
    tmnxBsxIsaAaGrpOvrldCutthruClr.setStatus(
        "current"
    )

tmnxBsxTransitIpPersistenceWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 34)
)
tmnxBsxTransitIpPersistenceWarn.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyAaGrpPartIndex"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyTransitIpPolicyId"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyReason"))
)
if mibBuilder.loadTexts:
    tmnxBsxTransitIpPersistenceWarn.setStatus(
        "current"
    )

tmnxBsxAarpInstOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 35)
)
tmnxBsxAarpInstOperStateChanged.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstOperState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxBsxAarpInstOperStateChanged.setStatus(
        "current"
    )

tmnxBsxAarpInstStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 36)
)
tmnxBsxAarpInstStateChanged.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstState"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxBsxAarpInstStateChanged.setStatus(
        "current"
    )

tmnxBsxRadApFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 37)
)
tmnxBsxRadApFailure.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApDescription"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxNotifyReason"))
)
if mibBuilder.loadTexts:
    tmnxBsxRadApFailure.setStatus(
        "current"
    )

tmnxBsxRadApServOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 63, 0, 38)
)
tmnxBsxRadApServOperStateChange.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServAddrType"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServAddr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServOperState"))
)
if mibBuilder.loadTexts:
    tmnxBsxRadApServOperStateChange.setStatus(
        "current"
    )


# Notifications groups

tmnxBsxNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 5)
)
tmnxBsxNotificationGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFailureV2"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFailureClearV2"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpNonRedundantV2"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpNonRedundantClear"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpSwitchover"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFlowFull"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFlowFullClear"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaSubLoadBalance"))
)
if mibBuilder.loadTexts:
    tmnxBsxNotificationGroup.setStatus(
        "current"
    )

tmnxBsxNotificationGroupV8v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 10, 1)
)
tmnxBsxNotificationGroupV8v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpCapCostThres"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpCapCostThresClear"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscribersUnassigned"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolResExceeded"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubPolResExceededClear"))
)
if mibBuilder.loadTexts:
    tmnxBsxNotificationGroupV8v0.setStatus(
        "current"
    )

tmnxBsxNotificationGroupV7v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 10, 2)
)
tmnxBsxNotificationGroupV7v0.setObjects(
    ("TIMETRA-BSX-NG-MIB", "tmnxBsxAaSubscriberAcctDataLoss")
)
if mibBuilder.loadTexts:
    tmnxBsxNotificationGroupV7v0.setStatus(
        "current"
    )

tmnxBsxNotificationGroupV9v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 10, 3)
)
tmnxBsxNotificationGroupV9v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpBitRate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpBitRateClear"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFlowSetup"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFlowSetupClear"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpPacketRate"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpPacketRateClear"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPolAaSubCreated"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPolAaSubDeleted"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPolRadCoAAudit"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPolRadCoAError"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPolRadDiscError"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPolDhcpAddWarning"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransIpPolDhcpDelWarning"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFmSbWaSBufOvld"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpFmSbWaSBufOvldClr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSbWaSBufOvld"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpToSbWaSBufOvldClr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpOvrldCutthru"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxIsaAaGrpOvrldCutthruClr"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxTransitIpPersistenceWarn"))
)
if mibBuilder.loadTexts:
    tmnxBsxNotificationGroupV9v0.setStatus(
        "current"
    )

tmnxBsxNotificationGroupV10v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 10, 4)
)
tmnxBsxNotificationGroupV10v0.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstOperStateChanged"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxAarpInstStateChanged"))
)
if mibBuilder.loadTexts:
    tmnxBsxNotificationGroupV10v0.setStatus(
        "current"
    )

tmnxBsxRadApNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 2, 10, 5)
)
tmnxBsxRadApNotificationGroup.setObjects(
      *(("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApFailure"),
        ("TIMETRA-BSX-NG-MIB", "tmnxBsxRadApServOperStateChange"))
)
if mibBuilder.loadTexts:
    tmnxBsxRadApNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxBsxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxBsxCompliance.setStatus(
        "obsolete"
    )

tmnxBsxComplianceV7v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxBsxComplianceV7v0.setStatus(
        "obsolete"
    )

tmnxBsxComplianceV8v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxBsxComplianceV8v0.setStatus(
        "obsolete"
    )

tmnxBsxComplianceV9v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxBsxComplianceV9v0.setStatus(
        "obsolete"
    )

tmnxBsxComplianceV10v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 63, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxBsxComplianceV10v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-BSX-NG-MIB",
    **{"TmnxBsxIsaAaGroupIndex": TmnxBsxIsaAaGroupIndex,
       "TmnxBsxIsaAaGroupIndexOrZero": TmnxBsxIsaAaGroupIndexOrZero,
       "TmnxBsxAaGrpPartIndex": TmnxBsxAaGrpPartIndex,
       "TmnxBsxFailToMode": TmnxBsxFailToMode,
       "TmnxBsxPolicyVersion": TmnxBsxPolicyVersion,
       "TmnxBsxDirection": TmnxBsxDirection,
       "TmnxBsxPolicerType": TmnxBsxPolicerType,
       "TmnxBsxGranularity": TmnxBsxGranularity,
       "TmnxBsxPolicerAction": TmnxBsxPolicerAction,
       "TmnxBsxBurstSize": TmnxBsxBurstSize,
       "TmnxBsxOperator": TmnxBsxOperator,
       "TmnxBsxMdaRole": TmnxBsxMdaRole,
       "TmnxBsxMdaActivityState": TmnxBsxMdaActivityState,
       "TmnxBsxAaSubscriberType": TmnxBsxAaSubscriberType,
       "TmnxBsxAaSubscriber": TmnxBsxAaSubscriber,
       "TmnxBsxStatAaAcctCfgType": TmnxBsxStatAaAcctCfgType,
       "TmnxBsxAaStatType": TmnxBsxAaStatType,
       "TmnxBsxAaStatExportMethod": TmnxBsxAaStatExportMethod,
       "TmnxBsxExprSubStringIndex": TmnxBsxExprSubStringIndex,
       "TmnxBsxExprSubStringType": TmnxBsxExprSubStringType,
       "TmnxBsxExprSubString": TmnxBsxExprSubString,
       "TmnxBsxFirstPacketPolicy": TmnxBsxFirstPacketPolicy,
       "TmnxBsxActionStatus": TmnxBsxActionStatus,
       "TmnxBsxAdminCtrl": TmnxBsxAdminCtrl,
       "TmnxBsxCustProtExprSubString": TmnxBsxCustProtExprSubString,
       "TmnxBsxProtocolDirection": TmnxBsxProtocolDirection,
       "TmnxBsxLoadBalanceStatus": TmnxBsxLoadBalanceStatus,
       "TmnxBsxCflowdExpType": TmnxBsxCflowdExpType,
       "TmnxBsxCflowdPerfMeasType": TmnxBsxCflowdPerfMeasType,
       "TmnxBsxAaSubStatsInterval": TmnxBsxAaSubStatsInterval,
       "TmnxBsxAaSubAcctLossReason": TmnxBsxAaSubAcctLossReason,
       "TmnxBsxAaSubAsoValDerivedFrom": TmnxBsxAaSubAsoValDerivedFrom,
       "TmnxBsxAaSubPolicerResStatus": TmnxBsxAaSubPolicerResStatus,
       "TmnxBsxStatIsaAaCfgType": TmnxBsxStatIsaAaCfgType,
       "TmnxBsxTransitSubOrigin": TmnxBsxTransitSubOrigin,
       "TmnxBsxTListAttribType": TmnxBsxTListAttribType,
       "TmnxBsxTListAttribValue": TmnxBsxTListAttribValue,
       "TmnxBsxAqpHttpRedirFlowType": TmnxBsxAqpHttpRedirFlowType,
       "TmnxBsxAarpInstState": TmnxBsxAarpInstState,
       "TmnxBsxAarpInstOperFlags": TmnxBsxAarpInstOperFlags,
       "TmnxBsxAarpCommand": TmnxBsxAarpCommand,
       "TmnxBsxAarpServPointRole": TmnxBsxAarpServPointRole,
       "TmnxBsxAarpServPointType": TmnxBsxAarpServPointType,
       "TmnxBsxAarpServPoint": TmnxBsxAarpServPoint,
       "tmnxBsxNgMIBModule": tmnxBsxNgMIBModule,
       "tmnxBsxConformance": tmnxBsxConformance,
       "tmnxBsxCompliances": tmnxBsxCompliances,
       "tmnxBsxCompliance": tmnxBsxCompliance,
       "tmnxBsxComplianceV7v0": tmnxBsxComplianceV7v0,
       "tmnxBsxComplianceV8v0": tmnxBsxComplianceV8v0,
       "tmnxBsxComplianceV9v0": tmnxBsxComplianceV9v0,
       "tmnxBsxComplianceV10v0": tmnxBsxComplianceV10v0,
       "tmnxBsxGroups": tmnxBsxGroups,
       "tmnxBsxMdaGroup": tmnxBsxMdaGroup,
       "tmnxBsxPolicyGroup": tmnxBsxPolicyGroup,
       "tmnxBsxStatsGroup": tmnxBsxStatsGroup,
       "tmnxBsxNotifyObjsGroup": tmnxBsxNotifyObjsGroup,
       "tmnxBsxNotificationGroup": tmnxBsxNotificationGroup,
       "tmnxBsxMdaGroups": tmnxBsxMdaGroups,
       "tmnxBsxMdaGroupV7v0": tmnxBsxMdaGroupV7v0,
       "tmnxBsxMdaGroupV8v0": tmnxBsxMdaGroupV8v0,
       "tmnxBsxMdaGroupV9v0": tmnxBsxMdaGroupV9v0,
       "tmnxBsxMdaGroupV10v0": tmnxBsxMdaGroupV10v0,
       "tmnxBsxMdaGroupMG3v0": tmnxBsxMdaGroupMG3v0,
       "tmnxBsxObsoleteGroups": tmnxBsxObsoleteGroups,
       "tmnxBsxObsoleteGroupV7v0": tmnxBsxObsoleteGroupV7v0,
       "tmnxBsxObsoleteGroupV8v0": tmnxBsxObsoleteGroupV8v0,
       "tmnxBsxObsoleteGroupsV9v0": tmnxBsxObsoleteGroupsV9v0,
       "tmnxBsxObsoleteGroupV10v0": tmnxBsxObsoleteGroupV10v0,
       "tmnxBsxPolicyGroups": tmnxBsxPolicyGroups,
       "tmnxBsxPolicyGroupV8v0": tmnxBsxPolicyGroupV8v0,
       "tmnxBsxPolicyGroupV9v0": tmnxBsxPolicyGroupV9v0,
       "tmnxBsxPolicyGroupV10v0": tmnxBsxPolicyGroupV10v0,
       "tmnxBsxNotificationGroups": tmnxBsxNotificationGroups,
       "tmnxBsxNotificationGroupV8v0": tmnxBsxNotificationGroupV8v0,
       "tmnxBsxNotificationGroupV7v0": tmnxBsxNotificationGroupV7v0,
       "tmnxBsxNotificationGroupV9v0": tmnxBsxNotificationGroupV9v0,
       "tmnxBsxNotificationGroupV10v0": tmnxBsxNotificationGroupV10v0,
       "tmnxBsxRadApNotificationGroup": tmnxBsxRadApNotificationGroup,
       "tmnxBsxCflowdGroups": tmnxBsxCflowdGroups,
       "tmnxBsxCflowdGroup": tmnxBsxCflowdGroup,
       "tmnxBsxCflowdGroupV9v0": tmnxBsxCflowdGroupV9v0,
       "tmnxBsxCflowdGroupV10v0": tmnxBsxCflowdGroupV10v0,
       "tmnxBsxOvrdGroups": tmnxBsxOvrdGroups,
       "tmnxBsxOvrdGroup": tmnxBsxOvrdGroup,
       "tmnxBsxNotifyObjsGroups": tmnxBsxNotifyObjsGroups,
       "tmnxBsxNotifyObjsGroupV7v0": tmnxBsxNotifyObjsGroupV7v0,
       "tmnxBsxNotifyObjsGroupV8v0": tmnxBsxNotifyObjsGroupV8v0,
       "tmnxBsxNotifyObjsGroupV9v0": tmnxBsxNotifyObjsGroupV9v0,
       "tmnxBsxTransitGroups": tmnxBsxTransitGroups,
       "tmnxBsxTransitGroup": tmnxBsxTransitGroup,
       "tmnxBsxTransitGroupV10v0": tmnxBsxTransitGroupV10v0,
       "tmnxBsxTransitSeenIpGroup": tmnxBsxTransitSeenIpGroup,
       "tmnxBsxStatsGroups": tmnxBsxStatsGroups,
       "tmnxBsxStatsGroupV9v0": tmnxBsxStatsGroupV9v0,
       "tmnxBsxMobileGatewayGroups": tmnxBsxMobileGatewayGroups,
       "tmnxBsxMobileGatewayGroup": tmnxBsxMobileGatewayGroup,
       "tmnxBsxHttpRedirGroups": tmnxBsxHttpRedirGroups,
       "tmnxBsxHttpRedirErrGroup": tmnxBsxHttpRedirErrGroup,
       "tmnxBsxHttpRedirGroup": tmnxBsxHttpRedirGroup,
       "tmnxBsxStaticObjGroups": tmnxBsxStaticObjGroups,
       "tmnxBsxStaticObjGroup": tmnxBsxStaticObjGroup,
       "tmnxBsxRedundancyObjGroups": tmnxBsxRedundancyObjGroups,
       "tmnxBsxRedundancyObjGroup": tmnxBsxRedundancyObjGroup,
       "tmnxBsxHttpEnrichObjGroups": tmnxBsxHttpEnrichObjGroups,
       "tmnxBsxHttpEnrichObjGroup": tmnxBsxHttpEnrichObjGroup,
       "tmnxBsxHttpEnrichStatObjGroup": tmnxBsxHttpEnrichStatObjGroup,
       "tmnxBsxRadiusAccountingGroups": tmnxBsxRadiusAccountingGroups,
       "tmnxBsxRadiusAccountingObjGroup": tmnxBsxRadiusAccountingObjGroup,
       "tmnxBsxRadApObjGroup": tmnxBsxRadApObjGroup,
       "tmnxBsxRadApStatObjGroup": tmnxBsxRadApStatObjGroup,
       "tmnxBsxObjs": tmnxBsxObjs,
       "tmnxBsxMdaObjs": tmnxBsxMdaObjs,
       "tmnxBsxMdaScalars": tmnxBsxMdaScalars,
       "tmnxBsxIsaAaGrpLastChangeTime": tmnxBsxIsaAaGrpLastChangeTime,
       "tmnxBsxIsaAaGrpFcLastChangeTime": tmnxBsxIsaAaGrpFcLastChangeTime,
       "tmnxBsxIsaAaGrpMdaLastChangeTime": tmnxBsxIsaAaGrpMdaLastChangeTime,
       "tmnxBsxAaGrpPartLastChangeTime": tmnxBsxAaGrpPartLastChangeTime,
       "tmnxBsxAaWap1xLastChangeTime": tmnxBsxAaWap1xLastChangeTime,
       "tmnxBsxIsaAaGrpTable": tmnxBsxIsaAaGrpTable,
       "tmnxBsxIsaAaGrpEntry": tmnxBsxIsaAaGrpEntry,
       "tmnxBsxIsaAaGroupIndex": tmnxBsxIsaAaGroupIndex,
       "tmnxBsxIsaAaGrpRowStatus": tmnxBsxIsaAaGrpRowStatus,
       "tmnxBsxIsaAaGrpRowLastChange": tmnxBsxIsaAaGrpRowLastChange,
       "tmnxBsxIsaAaGrpDescription": tmnxBsxIsaAaGrpDescription,
       "tmnxBsxIsaAaGrpAdminState": tmnxBsxIsaAaGrpAdminState,
       "tmnxBsxIsaAaGrpOperState": tmnxBsxIsaAaGrpOperState,
       "tmnxBsxIsaAaGrpFailToMode": tmnxBsxIsaAaGrpFailToMode,
       "tmnxBsxIsaAaGrpFromSubPool": tmnxBsxIsaAaGrpFromSubPool,
       "tmnxBsxIsaAaGrpFromSubResvCbs": tmnxBsxIsaAaGrpFromSubResvCbs,
       "tmnxBsxIsaAaGrpFromSubSlpPolicy": tmnxBsxIsaAaGrpFromSubSlpPolicy,
       "tmnxBsxIsaAaGrpFromSubQuePolicy": tmnxBsxIsaAaGrpFromSubQuePolicy,
       "tmnxBsxIsaAaGrpFromSubSchPolicy": tmnxBsxIsaAaGrpFromSubSchPolicy,
       "tmnxBsxIsaAaGrpToSubPool": tmnxBsxIsaAaGrpToSubPool,
       "tmnxBsxIsaAaGrpToSubResvCbs": tmnxBsxIsaAaGrpToSubResvCbs,
       "tmnxBsxIsaAaGrpToSubSlpPolicy": tmnxBsxIsaAaGrpToSubSlpPolicy,
       "tmnxBsxIsaAaGrpToSubQuePolicy": tmnxBsxIsaAaGrpToSubQuePolicy,
       "tmnxBsxIsaAaGrpToSubSchPolicy": tmnxBsxIsaAaGrpToSubSchPolicy,
       "tmnxBsxIsaAaGrpIngressPool": tmnxBsxIsaAaGrpIngressPool,
       "tmnxBsxIsaAaGrpIngressResvCbs": tmnxBsxIsaAaGrpIngressResvCbs,
       "tmnxBsxIsaAaGrpIngressSlpPolicy": tmnxBsxIsaAaGrpIngressSlpPolicy,
       "tmnxBsxIsaAaGrpIngressQuePolicy": tmnxBsxIsaAaGrpIngressQuePolicy,
       "tmnxBsxIsaAaGrpActivityChange": tmnxBsxIsaAaGrpActivityChange,
       "tmnxBsxIsaAaGrpPartitions": tmnxBsxIsaAaGrpPartitions,
       "tmnxBsxIsaAaGrpCapCostLowThres": tmnxBsxIsaAaGrpCapCostLowThres,
       "tmnxBsxIsaAaGrpCapCostHighThres": tmnxBsxIsaAaGrpCapCostHighThres,
       "tmnxBsxIsaAaGrpLoadBalanceStatus": tmnxBsxIsaAaGrpLoadBalanceStatus,
       "tmnxBsxIsaAaGrpUnassignedEsmSubs": tmnxBsxIsaAaGrpUnassignedEsmSubs,
       "tmnxBsxIsaAaGrpUnassignedSapSubs": tmnxBsxIsaAaGrpUnassignedSapSubs,
       "tmnxBsxIsaAaGrpUnassignedSpkSubs": tmnxBsxIsaAaGrpUnassignedSpkSubs,
       "tmnxBsxIsaAaGrpUnassignedTIpSubs": tmnxBsxIsaAaGrpUnassignedTIpSubs,
       "tmnxBsxIsaAaGrpAaSubScale": tmnxBsxIsaAaGrpAaSubScale,
       "tmnxBsxIsaAaGrpOverloadCutThru": tmnxBsxIsaAaGrpOverloadCutThru,
       "tmnxBsxIsaAaGrpFromSubWaSBfHiWmk": tmnxBsxIsaAaGrpFromSubWaSBfHiWmk,
       "tmnxBsxIsaAaGrpFromSubWaSBfLoWmk": tmnxBsxIsaAaGrpFromSubWaSBfLoWmk,
       "tmnxBsxIsaAaGrpToSubWaSBfHiWmk": tmnxBsxIsaAaGrpToSubWaSBfHiWmk,
       "tmnxBsxIsaAaGrpToSubWaSBfLoWmk": tmnxBsxIsaAaGrpToSubWaSBfLoWmk,
       "tmnxBsxIsaAaGrpTransPrefV4NmEntr": tmnxBsxIsaAaGrpTransPrefV4NmEntr,
       "tmnxBsxIsaAaGrpTransPrefV6NmEntr": tmnxBsxIsaAaGrpTransPrefV6NmEntr,
       "tmnxBsxIsaAaGrpTransPrefV6RmEntr": tmnxBsxIsaAaGrpTransPrefV6RmEntr,
       "tmnxBsxIsaAaGrpFcTable": tmnxBsxIsaAaGrpFcTable,
       "tmnxBsxIsaAaGrpFcEntry": tmnxBsxIsaAaGrpFcEntry,
       "tmnxBsxIsaAaGrpFcRowStatus": tmnxBsxIsaAaGrpFcRowStatus,
       "tmnxBsxIsaAaGrpFcRowLastChange": tmnxBsxIsaAaGrpFcRowLastChange,
       "tmnxBsxGrpMdaTable": tmnxBsxGrpMdaTable,
       "tmnxBsxGrpMdaEntry": tmnxBsxGrpMdaEntry,
       "tmnxBsxCardSlotNum": tmnxBsxCardSlotNum,
       "tmnxBsxGrpMdaRowStatus": tmnxBsxGrpMdaRowStatus,
       "tmnxBsxGrpMdaRowLastChange": tmnxBsxGrpMdaRowLastChange,
       "tmnxBsxGrpMdaRole": tmnxBsxGrpMdaRole,
       "tmnxBsxGrpMdaActivityState": tmnxBsxGrpMdaActivityState,
       "tmnxBsxGrpMdaActivityChange": tmnxBsxGrpMdaActivityChange,
       "tmnxBsxGrpMdaEsmSubscribers": tmnxBsxGrpMdaEsmSubscribers,
       "tmnxBsxGrpMdaSapSubscribers": tmnxBsxGrpMdaSapSubscribers,
       "tmnxBsxGrpMdaSpokeSdpSubscribers": tmnxBsxGrpMdaSpokeSdpSubscribers,
       "tmnxBsxGrpMdaCapacityCost": tmnxBsxGrpMdaCapacityCost,
       "tmnxBsxGrpMdaStatsResourceCount": tmnxBsxGrpMdaStatsResourceCount,
       "tmnxBsxGrpMdaTransitIpSubs": tmnxBsxGrpMdaTransitIpSubs,
       "tmnxBsxGrpMdaTransitIpAddrs": tmnxBsxGrpMdaTransitIpAddrs,
       "tmnxBsxGrpMdaTransitSubs": tmnxBsxGrpMdaTransitSubs,
       "tmnxBsxGrpMdaTransPrefEntries": tmnxBsxGrpMdaTransPrefEntries,
       "tmnxBsxGrpMdaTransPrefV4Entr": tmnxBsxGrpMdaTransPrefV4Entr,
       "tmnxBsxGrpMdaTransPrefV6Entr": tmnxBsxGrpMdaTransPrefV6Entr,
       "tmnxBsxGrpMdaTransPrefV6RemEntr": tmnxBsxGrpMdaTransPrefV6RemEntr,
       "tmnxBsxGrpStatusTable": tmnxBsxGrpStatusTable,
       "tmnxBsxGrpStatusEntry": tmnxBsxGrpStatusEntry,
       "tmnxBsxGrpStatusDiscontTime": tmnxBsxGrpStatusDiscontTime,
       "tmnxBsxGrpStatusOctsIn": tmnxBsxGrpStatusOctsIn,
       "tmnxBsxGrpStatusPktsIn": tmnxBsxGrpStatusPktsIn,
       "tmnxBsxGrpStatusPktsInPChipErs": tmnxBsxGrpStatusPktsInPChipErs,
       "tmnxBsxGrpStatusOctsDiscCongIn": tmnxBsxGrpStatusOctsDiscCongIn,
       "tmnxBsxGrpStatusPktsDiscCongIn": tmnxBsxGrpStatusPktsDiscCongIn,
       "tmnxBsxGrpStatusOctsToMda": tmnxBsxGrpStatusOctsToMda,
       "tmnxBsxGrpStatusPktsToMda": tmnxBsxGrpStatusPktsToMda,
       "tmnxBsxGrpStatusOctsDisCongMda": tmnxBsxGrpStatusOctsDisCongMda,
       "tmnxBsxGrpStatusPktsDisCongMda": tmnxBsxGrpStatusPktsDisCongMda,
       "tmnxBsxGrpStatusOctsDiscErrors": tmnxBsxGrpStatusOctsDiscErrors,
       "tmnxBsxGrpStatusPktsDiscErrors": tmnxBsxGrpStatusPktsDiscErrors,
       "tmnxBsxGrpStatusOctsPolicyByps": tmnxBsxGrpStatusOctsPolicyByps,
       "tmnxBsxGrpStatusPktsPolicyByps": tmnxBsxGrpStatusPktsPolicyByps,
       "tmnxBsxGrpStatusOctsInspected": tmnxBsxGrpStatusOctsInspected,
       "tmnxBsxGrpStatusPktsInspected": tmnxBsxGrpStatusPktsInspected,
       "tmnxBsxGrpStatusOctsDiscPolicy": tmnxBsxGrpStatusOctsDiscPolicy,
       "tmnxBsxGrpStatusPktsDiscPolicy": tmnxBsxGrpStatusPktsDiscPolicy,
       "tmnxBsxGrpStatusOctsInMda": tmnxBsxGrpStatusOctsInMda,
       "tmnxBsxGrpStatusPktsInMda": tmnxBsxGrpStatusPktsInMda,
       "tmnxBsxGrpStatusOctsFromMda": tmnxBsxGrpStatusOctsFromMda,
       "tmnxBsxGrpStatusPktsFromMda": tmnxBsxGrpStatusPktsFromMda,
       "tmnxBsxGrpStatusPktsOutPChipEr": tmnxBsxGrpStatusPktsOutPChipEr,
       "tmnxBsxGrpStatusOctsDisCongOut": tmnxBsxGrpStatusOctsDisCongOut,
       "tmnxBsxGrpStatusPktsDisCongOut": tmnxBsxGrpStatusPktsDisCongOut,
       "tmnxBsxGrpStatusOctsOut": tmnxBsxGrpStatusOctsOut,
       "tmnxBsxGrpStatusPktsOut": tmnxBsxGrpStatusPktsOut,
       "tmnxBsxGrpStatusFlows": tmnxBsxGrpStatusFlows,
       "tmnxBsxGrpStatusFlowsCurrent": tmnxBsxGrpStatusFlowsCurrent,
       "tmnxBsxGrpStatusFlowSetupRate": tmnxBsxGrpStatusFlowSetupRate,
       "tmnxBsxGrpStatusSubsDiverted": tmnxBsxGrpStatusSubsDiverted,
       "tmnxBsxGrpStatusSubsCurrent": tmnxBsxGrpStatusSubsCurrent,
       "tmnxBsxGrpStatusTrafficRate": tmnxBsxGrpStatusTrafficRate,
       "tmnxBsxGrpStatusHCOctsIn": tmnxBsxGrpStatusHCOctsIn,
       "tmnxBsxGrpStatusHCPktsIn": tmnxBsxGrpStatusHCPktsIn,
       "tmnxBsxGrpStatusHCPktsInPChipErs": tmnxBsxGrpStatusHCPktsInPChipErs,
       "tmnxBsxGrpStatusHCOctsDiscCongIn": tmnxBsxGrpStatusHCOctsDiscCongIn,
       "tmnxBsxGrpStatusHCPktsDiscCongIn": tmnxBsxGrpStatusHCPktsDiscCongIn,
       "tmnxBsxGrpStatusHCOctsToMda": tmnxBsxGrpStatusHCOctsToMda,
       "tmnxBsxGrpStatusHCPktsToMda": tmnxBsxGrpStatusHCPktsToMda,
       "tmnxBsxGrpStatusHCOctsDisCongMda": tmnxBsxGrpStatusHCOctsDisCongMda,
       "tmnxBsxGrpStatusHCPktsDisCongMda": tmnxBsxGrpStatusHCPktsDisCongMda,
       "tmnxBsxGrpStatusHCOctsDiscErrors": tmnxBsxGrpStatusHCOctsDiscErrors,
       "tmnxBsxGrpStatusHCPktsDiscErrors": tmnxBsxGrpStatusHCPktsDiscErrors,
       "tmnxBsxGrpStatusHCOctsPolicyByps": tmnxBsxGrpStatusHCOctsPolicyByps,
       "tmnxBsxGrpStatusHCPktsPolicyByps": tmnxBsxGrpStatusHCPktsPolicyByps,
       "tmnxBsxGrpStatusHCOctsInspected": tmnxBsxGrpStatusHCOctsInspected,
       "tmnxBsxGrpStatusHCPktsInspected": tmnxBsxGrpStatusHCPktsInspected,
       "tmnxBsxGrpStatusHCOctsDiscPolicy": tmnxBsxGrpStatusHCOctsDiscPolicy,
       "tmnxBsxGrpStatusHCPktsDiscPolicy": tmnxBsxGrpStatusHCPktsDiscPolicy,
       "tmnxBsxGrpStatusHCOctsInMda": tmnxBsxGrpStatusHCOctsInMda,
       "tmnxBsxGrpStatusHCPktsInMda": tmnxBsxGrpStatusHCPktsInMda,
       "tmnxBsxGrpStatusHCOctsFromMda": tmnxBsxGrpStatusHCOctsFromMda,
       "tmnxBsxGrpStatusHCPktsFromMda": tmnxBsxGrpStatusHCPktsFromMda,
       "tmnxBsxGrpStatusHCPktsOutPChipEr": tmnxBsxGrpStatusHCPktsOutPChipEr,
       "tmnxBsxGrpStatusHCOctsDisCongOut": tmnxBsxGrpStatusHCOctsDisCongOut,
       "tmnxBsxGrpStatusHCPktsDisCongOut": tmnxBsxGrpStatusHCPktsDisCongOut,
       "tmnxBsxGrpStatusHCOctsOut": tmnxBsxGrpStatusHCOctsOut,
       "tmnxBsxGrpStatusHCPktsOut": tmnxBsxGrpStatusHCPktsOut,
       "tmnxBsxGrpStatusHCFlows": tmnxBsxGrpStatusHCFlows,
       "tmnxBsxGrpStatusFlowsAverage": tmnxBsxGrpStatusFlowsAverage,
       "tmnxBsxGrpStatusFlowsPeak": tmnxBsxGrpStatusFlowsPeak,
       "tmnxBsxGrpStatusFlowSetupRateAvg": tmnxBsxGrpStatusFlowSetupRateAvg,
       "tmnxBsxGrpStatusFlowSetupRatePk": tmnxBsxGrpStatusFlowSetupRatePk,
       "tmnxBsxGrpStatusSubsDivertedAvg": tmnxBsxGrpStatusSubsDivertedAvg,
       "tmnxBsxGrpStatusSubsDivertedPk": tmnxBsxGrpStatusSubsDivertedPk,
       "tmnxBsxGrpStatusSubsAverage": tmnxBsxGrpStatusSubsAverage,
       "tmnxBsxGrpStatusSubsPeak": tmnxBsxGrpStatusSubsPeak,
       "tmnxBsxGrpStatusTrafficRateAvg": tmnxBsxGrpStatusTrafficRateAvg,
       "tmnxBsxGrpStatusTrafficRatePeak": tmnxBsxGrpStatusTrafficRatePeak,
       "tmnxBsxGrpStatusPacketRate": tmnxBsxGrpStatusPacketRate,
       "tmnxBsxGrpStatusPacketRateAvg": tmnxBsxGrpStatusPacketRateAvg,
       "tmnxBsxGrpStatusPacketRatePeak": tmnxBsxGrpStatusPacketRatePeak,
       "tmnxBsxGrpStatusFlowResInUse": tmnxBsxGrpStatusFlowResInUse,
       "tmnxBsxGrpStatusHCPktSzIncPk": tmnxBsxGrpStatusHCPktSzIncPk,
       "tmnxBsxGrpStatusPktSzIncPkLo": tmnxBsxGrpStatusPktSzIncPkLo,
       "tmnxBsxGrpStatusPktSzIncPkHi": tmnxBsxGrpStatusPktSzIncPkHi,
       "tmnxBsxGrpStatusHCPktSzDecPk": tmnxBsxGrpStatusHCPktSzDecPk,
       "tmnxBsxGrpStatusPktSzDecPkLo": tmnxBsxGrpStatusPktSzDecPkLo,
       "tmnxBsxGrpStatusPktSzDecPkHi": tmnxBsxGrpStatusPktSzDecPkHi,
       "tmnxBsxGrpStatusHCPktSzIncOc": tmnxBsxGrpStatusHCPktSzIncOc,
       "tmnxBsxGrpStatusPktSzIncOcLo": tmnxBsxGrpStatusPktSzIncOcLo,
       "tmnxBsxGrpStatusPktSzIncOcHi": tmnxBsxGrpStatusPktSzIncOcHi,
       "tmnxBsxGrpStatusHCPktSzDecOc": tmnxBsxGrpStatusHCPktSzDecOc,
       "tmnxBsxGrpStatusPktSzDecOcLo": tmnxBsxGrpStatusPktSzDecOcLo,
       "tmnxBsxGrpStatusPktSzDecOcHi": tmnxBsxGrpStatusPktSzDecOcHi,
       "tmnxBsxGrpStatusIngQTable": tmnxBsxGrpStatusIngQTable,
       "tmnxBsxGrpStatusIngQEntry": tmnxBsxGrpStatusIngQEntry,
       "tmnxBsxGrpStatusInQDirection": tmnxBsxGrpStatusInQDirection,
       "tmnxBsxGrpStatusInQIndex": tmnxBsxGrpStatusInQIndex,
       "tmnxBsxGrpStatusIngQDiscontTime": tmnxBsxGrpStatusIngQDiscontTime,
       "tmnxBsxGrpStatusIngQFwdInPPkts": tmnxBsxGrpStatusIngQFwdInPPkts,
       "tmnxBsxGrpStatusIngQFwdOutPPkts": tmnxBsxGrpStatusIngQFwdOutPPkts,
       "tmnxBsxGrpStatusIngQFwdInPOcts": tmnxBsxGrpStatusIngQFwdInPOcts,
       "tmnxBsxGrpStatusIngQFwdOutPOcts": tmnxBsxGrpStatusIngQFwdOutPOcts,
       "tmnxBsxGrpStatusIngQDroInPPkts": tmnxBsxGrpStatusIngQDroInPPkts,
       "tmnxBsxGrpStatusIngQDroOutPPkts": tmnxBsxGrpStatusIngQDroOutPPkts,
       "tmnxBsxGrpStatusIngQDroInPOcts": tmnxBsxGrpStatusIngQDroInPOcts,
       "tmnxBsxGrpStatusIngQDroOutPOcts": tmnxBsxGrpStatusIngQDroOutPOcts,
       "tmnxBsxGrpStatusIngQHCFwdInPPkts": tmnxBsxGrpStatusIngQHCFwdInPPkts,
       "tmnxBsxGrpStatusIngQHCFwdOutPPkts": tmnxBsxGrpStatusIngQHCFwdOutPPkts,
       "tmnxBsxGrpStatusIngQHCFwdInPOcts": tmnxBsxGrpStatusIngQHCFwdInPOcts,
       "tmnxBsxGrpStatusIngQHCFwdOutPOcts": tmnxBsxGrpStatusIngQHCFwdOutPOcts,
       "tmnxBsxGrpStatusIngQHCDroInPPkts": tmnxBsxGrpStatusIngQHCDroInPPkts,
       "tmnxBsxGrpStatusIngQHCDroOutPPkts": tmnxBsxGrpStatusIngQHCDroOutPPkts,
       "tmnxBsxGrpStatusIngQHCDroInPOcts": tmnxBsxGrpStatusIngQHCDroInPOcts,
       "tmnxBsxGrpStatusIngQHCDroOutPOcts": tmnxBsxGrpStatusIngQHCDroOutPOcts,
       "tmnxBsxGrpStatusEgrQTable": tmnxBsxGrpStatusEgrQTable,
       "tmnxBsxGrpStatusEgrQEntry": tmnxBsxGrpStatusEgrQEntry,
       "tmnxBsxGrpStatusEgrQDirection": tmnxBsxGrpStatusEgrQDirection,
       "tmnxBsxGrpStatusEgrQIndex": tmnxBsxGrpStatusEgrQIndex,
       "tmnxBsxGrpStatusEgrQDiscontTime": tmnxBsxGrpStatusEgrQDiscontTime,
       "tmnxBsxGrpStatusEgrQFwdInPPkts": tmnxBsxGrpStatusEgrQFwdInPPkts,
       "tmnxBsxGrpStatusEgrQFwdOutPPkts": tmnxBsxGrpStatusEgrQFwdOutPPkts,
       "tmnxBsxGrpStatusEgrQFwdInPOcts": tmnxBsxGrpStatusEgrQFwdInPOcts,
       "tmnxBsxGrpStatusEgrQFwdOutPOcts": tmnxBsxGrpStatusEgrQFwdOutPOcts,
       "tmnxBsxGrpStatusEgrQDroInPPkts": tmnxBsxGrpStatusEgrQDroInPPkts,
       "tmnxBsxGrpStatusEgrQDroOutPPkts": tmnxBsxGrpStatusEgrQDroOutPPkts,
       "tmnxBsxGrpStatusEgrQDroInPOcts": tmnxBsxGrpStatusEgrQDroInPOcts,
       "tmnxBsxGrpStatusEgrQDroOutPOcts": tmnxBsxGrpStatusEgrQDroOutPOcts,
       "tmnxBsxGrpStatusEgrQHCFwdInPPkts": tmnxBsxGrpStatusEgrQHCFwdInPPkts,
       "tmnxBsxGrpStatusEgrQHCFwdOutPPkts": tmnxBsxGrpStatusEgrQHCFwdOutPPkts,
       "tmnxBsxGrpStatusEgrQHCFwdInPOcts": tmnxBsxGrpStatusEgrQHCFwdInPOcts,
       "tmnxBsxGrpStatusEgrQHCFwdOutPOcts": tmnxBsxGrpStatusEgrQHCFwdOutPOcts,
       "tmnxBsxGrpStatusEgrQHCDroInPPkts": tmnxBsxGrpStatusEgrQHCDroInPPkts,
       "tmnxBsxGrpStatusEgrQHCDroOutPPkts": tmnxBsxGrpStatusEgrQHCDroOutPPkts,
       "tmnxBsxGrpStatusEgrQHCDroInPOcts": tmnxBsxGrpStatusEgrQHCDroInPOcts,
       "tmnxBsxGrpStatusEgrQHCDroOutPOcts": tmnxBsxGrpStatusEgrQHCDroOutPOcts,
       "tmnxBsxAaSubSumTable": tmnxBsxAaSubSumTable,
       "tmnxBsxAaSubSumEntry": tmnxBsxAaSubSumEntry,
       "tmnxBsxAaSubStatsInterval": tmnxBsxAaSubStatsInterval,
       "tmnxBsxAaSubSumMdaSlotNum": tmnxBsxAaSubSumMdaSlotNum,
       "tmnxBsxAaSubSumMdaMdaNum": tmnxBsxAaSubSumMdaMdaNum,
       "tmnxBsxAaSubSumAppProfName": tmnxBsxAaSubSumAppProfName,
       "tmnxBsxAaSubSumDiscontTime": tmnxBsxAaSubSumDiscontTime,
       "tmnxBsxAaSubSumOctsAdmFmSb": tmnxBsxAaSubSumOctsAdmFmSb,
       "tmnxBsxAaSubSumPktsAdmFmSb": tmnxBsxAaSubSumPktsAdmFmSb,
       "tmnxBsxAaSubSumFlwsAdmFmSb": tmnxBsxAaSubSumFlwsAdmFmSb,
       "tmnxBsxAaSubSumOctsDnyFmSb": tmnxBsxAaSubSumOctsDnyFmSb,
       "tmnxBsxAaSubSumPktsDnyFmSb": tmnxBsxAaSubSumPktsDnyFmSb,
       "tmnxBsxAaSubSumFlwsDnyFmSb": tmnxBsxAaSubSumFlwsDnyFmSb,
       "tmnxBsxAaSubSumOctsAdmToSb": tmnxBsxAaSubSumOctsAdmToSb,
       "tmnxBsxAaSubSumPktsAdmToSb": tmnxBsxAaSubSumPktsAdmToSb,
       "tmnxBsxAaSubSumFlwsAdmToSb": tmnxBsxAaSubSumFlwsAdmToSb,
       "tmnxBsxAaSubSumOctsDnyToSb": tmnxBsxAaSubSumOctsDnyToSb,
       "tmnxBsxAaSubSumPktsDnyToSb": tmnxBsxAaSubSumPktsDnyToSb,
       "tmnxBsxAaSubSumFlwsDnyToSb": tmnxBsxAaSubSumFlwsDnyToSb,
       "tmnxBsxAaSubSumTermFlwDur": tmnxBsxAaSubSumTermFlwDur,
       "tmnxBsxAaSubSumTermFlws": tmnxBsxAaSubSumTermFlws,
       "tmnxBsxAaSubSumShrtDurFlws": tmnxBsxAaSubSumShrtDurFlws,
       "tmnxBsxAaSubSumMedDurFlws": tmnxBsxAaSubSumMedDurFlws,
       "tmnxBsxAaSubSumLngDurFlws": tmnxBsxAaSubSumLngDurFlws,
       "tmnxBsxAaSubSumActFlwsFmSb": tmnxBsxAaSubSumActFlwsFmSb,
       "tmnxBsxAaSubSumActFlwsToSb": tmnxBsxAaSubSumActFlwsToSb,
       "tmnxBsxAaSubSumHCOctsAdmFmSb": tmnxBsxAaSubSumHCOctsAdmFmSb,
       "tmnxBsxAaSubSumHCPktsAdmFmSb": tmnxBsxAaSubSumHCPktsAdmFmSb,
       "tmnxBsxAaSubSumHCFlwsAdmFmSb": tmnxBsxAaSubSumHCFlwsAdmFmSb,
       "tmnxBsxAaSubSumHCOctsDnyFmSb": tmnxBsxAaSubSumHCOctsDnyFmSb,
       "tmnxBsxAaSubSumHCPktsDnyFmSb": tmnxBsxAaSubSumHCPktsDnyFmSb,
       "tmnxBsxAaSubSumHCFlwsDnyFmSb": tmnxBsxAaSubSumHCFlwsDnyFmSb,
       "tmnxBsxAaSubSumHCOctsAdmToSb": tmnxBsxAaSubSumHCOctsAdmToSb,
       "tmnxBsxAaSubSumHCPktsAdmToSb": tmnxBsxAaSubSumHCPktsAdmToSb,
       "tmnxBsxAaSubSumHCFlwsAdmToSb": tmnxBsxAaSubSumHCFlwsAdmToSb,
       "tmnxBsxAaSubSumHCOctsDnyToSb": tmnxBsxAaSubSumHCOctsDnyToSb,
       "tmnxBsxAaSubSumHCPktsDnyToSb": tmnxBsxAaSubSumHCPktsDnyToSb,
       "tmnxBsxAaSubSumHCFlwsDnyToSb": tmnxBsxAaSubSumHCFlwsDnyToSb,
       "tmnxBsxAaSubSumHCTermFlwDur": tmnxBsxAaSubSumHCTermFlwDur,
       "tmnxBsxAaSubSumHCTermFlws": tmnxBsxAaSubSumHCTermFlws,
       "tmnxBsxAaSubSumHCShrtDurFlws": tmnxBsxAaSubSumHCShrtDurFlws,
       "tmnxBsxAaSubSumHCMedDurFlws": tmnxBsxAaSubSumHCMedDurFlws,
       "tmnxBsxAaSubSumHCLngDurFlws": tmnxBsxAaSubSumHCLngDurFlws,
       "tmnxBsxAaGrpPartTable": tmnxBsxAaGrpPartTable,
       "tmnxBsxAaGrpPartEntry": tmnxBsxAaGrpPartEntry,
       "tmnxBsxAaGrpPartIndex": tmnxBsxAaGrpPartIndex,
       "tmnxBsxAaGrpPartRowStatus": tmnxBsxAaGrpPartRowStatus,
       "tmnxBsxAaGrpPartRowLastChange": tmnxBsxAaGrpPartRowLastChange,
       "tmnxBsxAaGrpPartDescription": tmnxBsxAaGrpPartDescription,
       "tmnxBsxAaGrpPartXOnlineHost": tmnxBsxAaGrpPartXOnlineHost,
       "tmnxBsxAaGrpPartHttpMatchAllReq": tmnxBsxAaGrpPartHttpMatchAllReq,
       "tmnxBsxAaGrpPartAaSubRemote": tmnxBsxAaGrpPartAaSubRemote,
       "tmnxBsxIsaLoadBalUnSubTable": tmnxBsxIsaLoadBalUnSubTable,
       "tmnxBsxIsaLoadBalUnSubEntry": tmnxBsxIsaLoadBalUnSubEntry,
       "tmnxBsxIsaLoadBalUnSub": tmnxBsxIsaLoadBalUnSub,
       "tmnxBsxIsaLoadBalUnSubTransit": tmnxBsxIsaLoadBalUnSubTransit,
       "tmnxBsxAaSubTable": tmnxBsxAaSubTable,
       "tmnxBsxAaSubEntry": tmnxBsxAaSubEntry,
       "tmnxBsxAaSubMdaSlotNum": tmnxBsxAaSubMdaSlotNum,
       "tmnxBsxAaSubMdaMdaNum": tmnxBsxAaSubMdaMdaNum,
       "tmnxBsxAaSubAppProfName": tmnxBsxAaSubAppProfName,
       "tmnxBsxAaSubHasOverrides": tmnxBsxAaSubHasOverrides,
       "tmnxBsxAaSubTransitIpPolicyId": tmnxBsxAaSubTransitIpPolicyId,
       "tmnxBsxAaSubTransPrefPolicyId": tmnxBsxAaSubTransPrefPolicyId,
       "tmnxBsxAaWap1xTable": tmnxBsxAaWap1xTable,
       "tmnxBsxAaWap1xEntry": tmnxBsxAaWap1xEntry,
       "tmnxBsxAaWap1xRowLastChange": tmnxBsxAaWap1xRowLastChange,
       "tmnxBsxAaWap1xAdminState": tmnxBsxAaWap1xAdminState,
       "tmnxBsxPolicyObjs": tmnxBsxPolicyObjs,
       "tmnxBsxProtTable": tmnxBsxProtTable,
       "tmnxBsxProtEntry": tmnxBsxProtEntry,
       "tmnxBsxProtName": tmnxBsxProtName,
       "tmnxBsxProtDescription": tmnxBsxProtDescription,
       "tmnxBsxProtParentName": tmnxBsxProtParentName,
       "tmnxBsxProtAdminState": tmnxBsxProtAdminState,
       "tmnxBsxProtObsolete": tmnxBsxProtObsolete,
       "tmnxBsxAppGrpCfgTable": tmnxBsxAppGrpCfgTable,
       "tmnxBsxAppGrpCfgEntry": tmnxBsxAppGrpCfgEntry,
       "tmnxBsxAppGrpPolicyVersion": tmnxBsxAppGrpPolicyVersion,
       "tmnxBsxAppGrpName": tmnxBsxAppGrpName,
       "tmnxBsxAppGrpRowStatus": tmnxBsxAppGrpRowStatus,
       "tmnxBsxAppGrpStorageType": tmnxBsxAppGrpStorageType,
       "tmnxBsxAppGrpDescription": tmnxBsxAppGrpDescription,
       "tmnxBsxAppGrpAdminState": tmnxBsxAppGrpAdminState,
       "tmnxBsxAppGrpChargeGrp": tmnxBsxAppGrpChargeGrp,
       "tmnxBsxAppCfgTable": tmnxBsxAppCfgTable,
       "tmnxBsxAppCfgEntry": tmnxBsxAppCfgEntry,
       "tmnxBsxAppPolicyVersion": tmnxBsxAppPolicyVersion,
       "tmnxBsxAppName": tmnxBsxAppName,
       "tmnxBsxAppRowStatus": tmnxBsxAppRowStatus,
       "tmnxBsxAppStorageType": tmnxBsxAppStorageType,
       "tmnxBsxAppDescription": tmnxBsxAppDescription,
       "tmnxBsxAppAppGroup": tmnxBsxAppAppGroup,
       "tmnxBsxAppChargeGrp": tmnxBsxAppChargeGrp,
       "tmnxBsxAppFilterTable": tmnxBsxAppFilterTable,
       "tmnxBsxAppFilterEntry": tmnxBsxAppFilterEntry,
       "tmnxBsxAppFilterPolicyVersion": tmnxBsxAppFilterPolicyVersion,
       "tmnxBsxAppFilterEntryId": tmnxBsxAppFilterEntryId,
       "tmnxBsxAppFilterRowStatus": tmnxBsxAppFilterRowStatus,
       "tmnxBsxAppFilterDescription": tmnxBsxAppFilterDescription,
       "tmnxBsxAppFilterAdminState": tmnxBsxAppFilterAdminState,
       "tmnxBsxAppFilterProtocol": tmnxBsxAppFilterProtocol,
       "tmnxBsxAppFilterProtocolOp": tmnxBsxAppFilterProtocolOp,
       "tmnxBsxAppFilterFlowSetupDir": tmnxBsxAppFilterFlowSetupDir,
       "tmnxBsxAppFilterIpProtocolNum": tmnxBsxAppFilterIpProtocolNum,
       "tmnxBsxAppFilterIpProtocolNumOp": tmnxBsxAppFilterIpProtocolNumOp,
       "tmnxBsxAppFilterServerAddrType": tmnxBsxAppFilterServerAddrType,
       "tmnxBsxAppFilterServerAddr": tmnxBsxAppFilterServerAddr,
       "tmnxBsxAppFilterServerAddrLen": tmnxBsxAppFilterServerAddrLen,
       "tmnxBsxAppFilterServerAddrOp": tmnxBsxAppFilterServerAddrOp,
       "tmnxBsxAppFilterServerPort": tmnxBsxAppFilterServerPort,
       "tmnxBsxAppFilterServerPortOp": tmnxBsxAppFilterServerPortOp,
       "tmnxBsxAppFilterServerPortFpp": tmnxBsxAppFilterServerPortFpp,
       "tmnxBsxAppFilterServerPortLow": tmnxBsxAppFilterServerPortLow,
       "tmnxBsxAppFilterServerPortHigh": tmnxBsxAppFilterServerPortHigh,
       "tmnxBsxAppFilterApplication": tmnxBsxAppFilterApplication,
       "tmnxBsxAsoTable": tmnxBsxAsoTable,
       "tmnxBsxAsoEntry": tmnxBsxAsoEntry,
       "tmnxBsxAsoPolicyVersion": tmnxBsxAsoPolicyVersion,
       "tmnxBsxAsoCharName": tmnxBsxAsoCharName,
       "tmnxBsxAsoRowStatus": tmnxBsxAsoRowStatus,
       "tmnxBsxAsoDefValName": tmnxBsxAsoDefValName,
       "tmnxBsxAsoValTable": tmnxBsxAsoValTable,
       "tmnxBsxAsoValEntry": tmnxBsxAsoValEntry,
       "tmnxBsxAsoValPolicyVersion": tmnxBsxAsoValPolicyVersion,
       "tmnxBsxAsoValCharName": tmnxBsxAsoValCharName,
       "tmnxBsxAsoValValName": tmnxBsxAsoValValName,
       "tmnxBsxAsoValRowStatus": tmnxBsxAsoValRowStatus,
       "tmnxBsxAppProfTable": tmnxBsxAppProfTable,
       "tmnxBsxAppProfEntry": tmnxBsxAppProfEntry,
       "tmnxBsxAppProfName": tmnxBsxAppProfName,
       "tmnxBsxAppProfRowStatus": tmnxBsxAppProfRowStatus,
       "tmnxBsxAppProfDescription": tmnxBsxAppProfDescription,
       "tmnxBsxAppProfDivert": tmnxBsxAppProfDivert,
       "tmnxBsxAppProfCapacityCost": tmnxBsxAppProfCapacityCost,
       "tmnxBsxAppProfCharTable": tmnxBsxAppProfCharTable,
       "tmnxBsxAppProfCharEntry": tmnxBsxAppProfCharEntry,
       "tmnxBsxAppProfCharPolicyVersion": tmnxBsxAppProfCharPolicyVersion,
       "tmnxBsxAppProfCharProfName": tmnxBsxAppProfCharProfName,
       "tmnxBsxAppProfCharCharName": tmnxBsxAppProfCharCharName,
       "tmnxBsxAppProfCharRowStatus": tmnxBsxAppProfCharRowStatus,
       "tmnxBsxAppProfCharValName": tmnxBsxAppProfCharValName,
       "tmnxBsxAqpTable": tmnxBsxAqpTable,
       "tmnxBsxAqpEntry": tmnxBsxAqpEntry,
       "tmnxBsxAqpPolicyVersion": tmnxBsxAqpPolicyVersion,
       "tmnxBsxAqpEntryId": tmnxBsxAqpEntryId,
       "tmnxBsxAqpRowStatus": tmnxBsxAqpRowStatus,
       "tmnxBsxAqpDescription": tmnxBsxAqpDescription,
       "tmnxBsxAqpAdminState": tmnxBsxAqpAdminState,
       "tmnxBsxAqpApplication": tmnxBsxAqpApplication,
       "tmnxBsxAqpApplicationOp": tmnxBsxAqpApplicationOp,
       "tmnxBsxAqpAppGroup": tmnxBsxAqpAppGroup,
       "tmnxBsxAqpAppGroupOp": tmnxBsxAqpAppGroupOp,
       "tmnxBsxAqpTrafficDir": tmnxBsxAqpTrafficDir,
       "tmnxBsxAqpSubscriber": tmnxBsxAqpSubscriber,
       "tmnxBsxAqpSubscriberOp": tmnxBsxAqpSubscriberOp,
       "tmnxBsxAqpDscp": tmnxBsxAqpDscp,
       "tmnxBsxAqpDscpOp": tmnxBsxAqpDscpOp,
       "tmnxBsxAqpSapSubscrPortId": tmnxBsxAqpSapSubscrPortId,
       "tmnxBsxAqpSapSubscrEncapValue": tmnxBsxAqpSapSubscrEncapValue,
       "tmnxBsxAqpSapSubscrOp": tmnxBsxAqpSapSubscrOp,
       "tmnxBsxAqpSrcAddressType": tmnxBsxAqpSrcAddressType,
       "tmnxBsxAqpSrcAddress": tmnxBsxAqpSrcAddress,
       "tmnxBsxAqpSrcAddressLength": tmnxBsxAqpSrcAddressLength,
       "tmnxBsxAqpSrcAddressOp": tmnxBsxAqpSrcAddressOp,
       "tmnxBsxAqpSrcPortOp": tmnxBsxAqpSrcPortOp,
       "tmnxBsxAqpSrcPortLowValue": tmnxBsxAqpSrcPortLowValue,
       "tmnxBsxAqpSrcPortHighValue": tmnxBsxAqpSrcPortHighValue,
       "tmnxBsxAqpDstAddressType": tmnxBsxAqpDstAddressType,
       "tmnxBsxAqpDstAddress": tmnxBsxAqpDstAddress,
       "tmnxBsxAqpDstAddressLength": tmnxBsxAqpDstAddressLength,
       "tmnxBsxAqpDstAddressOp": tmnxBsxAqpDstAddressOp,
       "tmnxBsxAqpDstPortOp": tmnxBsxAqpDstPortOp,
       "tmnxBsxAqpDstPortLowValue": tmnxBsxAqpDstPortLowValue,
       "tmnxBsxAqpDstPortHighValue": tmnxBsxAqpDstPortHighValue,
       "tmnxBsxAqpSpokeSdpSubscr": tmnxBsxAqpSpokeSdpSubscr,
       "tmnxBsxAqpSpokeSdpSubscrOp": tmnxBsxAqpSpokeSdpSubscrOp,
       "tmnxBsxAqpAaSubscriberType": tmnxBsxAqpAaSubscriberType,
       "tmnxBsxAqpAaSubscriber": tmnxBsxAqpAaSubscriber,
       "tmnxBsxAqpAaSubscriberOp": tmnxBsxAqpAaSubscriberOp,
       "tmnxBsxAqpDrop": tmnxBsxAqpDrop,
       "tmnxBsxAqpBwLimitPolicer": tmnxBsxAqpBwLimitPolicer,
       "tmnxBsxAqpFlowRatePolicer": tmnxBsxAqpFlowRatePolicer,
       "tmnxBsxAqpFlowCountPolicer": tmnxBsxAqpFlowCountPolicer,
       "tmnxBsxAqpRemarkFc": tmnxBsxAqpRemarkFc,
       "tmnxBsxAqpRemarkPriority": tmnxBsxAqpRemarkPriority,
       "tmnxBsxAqpRemarkDscpInProfile": tmnxBsxAqpRemarkDscpInProfile,
       "tmnxBsxAqpRemarkDscpOutProfile": tmnxBsxAqpRemarkDscpOutProfile,
       "tmnxBsxAqpMirrorSource": tmnxBsxAqpMirrorSource,
       "tmnxBsxAqpMirrorSourceAllIncl": tmnxBsxAqpMirrorSourceAllIncl,
       "tmnxBsxAqpHttpErrRedirName": tmnxBsxAqpHttpErrRedirName,
       "tmnxBsxAqpHttpRedirName": tmnxBsxAqpHttpRedirName,
       "tmnxBsxAqpHttpRedirFlowType": tmnxBsxAqpHttpRedirFlowType,
       "tmnxBsxAqpHttpEnrichName": tmnxBsxAqpHttpEnrichName,
       "tmnxBsxAdminControl": tmnxBsxAdminControl,
       "tmnxBsxAdminOwner": tmnxBsxAdminOwner,
       "tmnxBsxAdminControlApply": tmnxBsxAdminControlApply,
       "tmnxBsxAdminLastChangeTime": tmnxBsxAdminLastChangeTime,
       "tmnxBsxAdminCtrlTable": tmnxBsxAdminCtrlTable,
       "tmnxBsxAdminCtrlEntry": tmnxBsxAdminCtrlEntry,
       "tmnxBsxAdminCtrlLastChTime": tmnxBsxAdminCtrlLastChTime,
       "tmnxBsxAdminCtrlConfigOwner": tmnxBsxAdminCtrlConfigOwner,
       "tmnxBsxAdminCtrlApply": tmnxBsxAdminCtrlApply,
       "tmnxBsxPolicerTable": tmnxBsxPolicerTable,
       "tmnxBsxPolicerEntry": tmnxBsxPolicerEntry,
       "tmnxBsxPolicerName": tmnxBsxPolicerName,
       "tmnxBsxPolicerRowStatus": tmnxBsxPolicerRowStatus,
       "tmnxBsxPolicerDescription": tmnxBsxPolicerDescription,
       "tmnxBsxPolicerType": tmnxBsxPolicerType,
       "tmnxBsxPolicerGranularity": tmnxBsxPolicerGranularity,
       "tmnxBsxPolicerAction": tmnxBsxPolicerAction,
       "tmnxBsxPolicerAdminPIR": tmnxBsxPolicerAdminPIR,
       "tmnxBsxPolicerAdminCIR": tmnxBsxPolicerAdminCIR,
       "tmnxBsxPolicerMBS": tmnxBsxPolicerMBS,
       "tmnxBsxPolicerCBS": tmnxBsxPolicerCBS,
       "tmnxBsxPolicerPIRAdaptation": tmnxBsxPolicerPIRAdaptation,
       "tmnxBsxPolicerCIRAdaptation": tmnxBsxPolicerCIRAdaptation,
       "tmnxBsxIsaAaTim": tmnxBsxIsaAaTim,
       "tmnxBsxUpgrade": tmnxBsxUpgrade,
       "tmnxBsxVersion": tmnxBsxVersion,
       "tmnxBsxAqpStatsTable": tmnxBsxAqpStatsTable,
       "tmnxBsxAqpStatsEntry": tmnxBsxAqpStatsEntry,
       "tmnxBsxAqpStatsFlows": tmnxBsxAqpStatsFlows,
       "tmnxBsxAqpStatsConflicts": tmnxBsxAqpStatsConflicts,
       "tmnxBsxAqpStatsHCFlows": tmnxBsxAqpStatsHCFlows,
       "tmnxBsxAqpStatsFlowsLo": tmnxBsxAqpStatsFlowsLo,
       "tmnxBsxAqpStatsFlowsHi": tmnxBsxAqpStatsFlowsHi,
       "tmnxBsxAqpStatsHCConflicts": tmnxBsxAqpStatsHCConflicts,
       "tmnxBsxAqpStatsConflictsLo": tmnxBsxAqpStatsConflictsLo,
       "tmnxBsxAqpStatsConflictsHi": tmnxBsxAqpStatsConflictsHi,
       "tmnxBsxInfo": tmnxBsxInfo,
       "tmnxBsxFlowFullHighWatermark": tmnxBsxFlowFullHighWatermark,
       "tmnxBsxFlowFullLowWatermark": tmnxBsxFlowFullLowWatermark,
       "tmnxBsxFlowSetupHighWatermark": tmnxBsxFlowSetupHighWatermark,
       "tmnxBsxFlowSetupLowWatermark": tmnxBsxFlowSetupLowWatermark,
       "tmnxBsxPacketRateHighWatermark": tmnxBsxPacketRateHighWatermark,
       "tmnxBsxPacketRateLowWatermark": tmnxBsxPacketRateLowWatermark,
       "tmnxBsxBitRateHighWatermark": tmnxBsxBitRateHighWatermark,
       "tmnxBsxBitRateLowWatermark": tmnxBsxBitRateLowWatermark,
       "tmnxBsxAqpCharTable": tmnxBsxAqpCharTable,
       "tmnxBsxAqpCharEntry": tmnxBsxAqpCharEntry,
       "tmnxBsxAqpCharRowStatus": tmnxBsxAqpCharRowStatus,
       "tmnxBsxAqpCharOperator": tmnxBsxAqpCharOperator,
       "tmnxBsxAppFilterExprTable": tmnxBsxAppFilterExprTable,
       "tmnxBsxAppFilterExprEntry": tmnxBsxAppFilterExprEntry,
       "tmnxBsxAppFilterExprIndex": tmnxBsxAppFilterExprIndex,
       "tmnxBsxAppFilterExprRowStatus": tmnxBsxAppFilterExprRowStatus,
       "tmnxBsxAppFilterExprType": tmnxBsxAppFilterExprType,
       "tmnxBsxAppFilterExprOperator": tmnxBsxAppFilterExprOperator,
       "tmnxBsxAppFilterExprStr": tmnxBsxAppFilterExprStr,
       "tmnxBsxCustProtTable": tmnxBsxCustProtTable,
       "tmnxBsxCustProtEntry": tmnxBsxCustProtEntry,
       "tmnxBsxCustProtPolicyVersion": tmnxBsxCustProtPolicyVersion,
       "tmnxBsxCustProtEntryId": tmnxBsxCustProtEntryId,
       "tmnxBsxCustProtRowStatus": tmnxBsxCustProtRowStatus,
       "tmnxBsxCustProtRowLastChange": tmnxBsxCustProtRowLastChange,
       "tmnxBsxCustProtIpProtocolNum": tmnxBsxCustProtIpProtocolNum,
       "tmnxBsxCustProtDescription": tmnxBsxCustProtDescription,
       "tmnxBsxCustProtAdminState": tmnxBsxCustProtAdminState,
       "tmnxBsxCustProtExprTable": tmnxBsxCustProtExprTable,
       "tmnxBsxCustProtExprEntry": tmnxBsxCustProtExprEntry,
       "tmnxBsxCustProtExprIndex": tmnxBsxCustProtExprIndex,
       "tmnxBsxCustProtExprRowStatus": tmnxBsxCustProtExprRowStatus,
       "tmnxBsxCustProtExprRowLastChange": tmnxBsxCustProtExprRowLastChange,
       "tmnxBsxCustProtExprOffset": tmnxBsxCustProtExprOffset,
       "tmnxBsxCustProtExprDirection": tmnxBsxCustProtExprDirection,
       "tmnxBsxCustProtExprOperator": tmnxBsxCustProtExprOperator,
       "tmnxBsxCustProtExprStr": tmnxBsxCustProtExprStr,
       "tmnxBsxAaSubAsoValTable": tmnxBsxAaSubAsoValTable,
       "tmnxBsxAaSubAsoValEntry": tmnxBsxAaSubAsoValEntry,
       "tmnxBsxAaSubAsoValName": tmnxBsxAaSubAsoValName,
       "tmnxBsxAaSubAsoValDerivedFrom": tmnxBsxAaSubAsoValDerivedFrom,
       "tmnxBsxAaSubPolicerTable": tmnxBsxAaSubPolicerTable,
       "tmnxBsxAaSubPolicerEntry": tmnxBsxAaSubPolicerEntry,
       "tmnxBsxAaSubPolicerType": tmnxBsxAaSubPolicerType,
       "tmnxBsxAaSubPolicerDirection": tmnxBsxAaSubPolicerDirection,
       "tmnxBsxAaSubPolicerIndex": tmnxBsxAaSubPolicerIndex,
       "tmnxBsxAaSubPolicerAqpEntryId": tmnxBsxAaSubPolicerAqpEntryId,
       "tmnxBsxAaSubPolicerName": tmnxBsxAaSubPolicerName,
       "tmnxBsxAaSubPolResExTable": tmnxBsxAaSubPolResExTable,
       "tmnxBsxAaSubPolResExEntry": tmnxBsxAaSubPolResExEntry,
       "tmnxBsxAaSubPolResExStatus": tmnxBsxAaSubPolResExStatus,
       "tmnxBsxPolicyScalars": tmnxBsxPolicyScalars,
       "tmnxBsxPlcyCfgLastChTime": tmnxBsxPlcyCfgLastChTime,
       "tmnxBsxChargeGrpLastChTime": tmnxBsxChargeGrpLastChTime,
       "tmnxBsxChargeGrpCfgTable": tmnxBsxChargeGrpCfgTable,
       "tmnxBsxChargeGrpCfgEntry": tmnxBsxChargeGrpCfgEntry,
       "tmnxBsxChargeGrpPolicyVersion": tmnxBsxChargeGrpPolicyVersion,
       "tmnxBsxChargeGrpName": tmnxBsxChargeGrpName,
       "tmnxBsxChargeGrpRowStatus": tmnxBsxChargeGrpRowStatus,
       "tmnxBsxChargeGrpRowLastCh": tmnxBsxChargeGrpRowLastCh,
       "tmnxBsxChargeGrpDescription": tmnxBsxChargeGrpDescription,
       "tmnxBsxChargeGrpExportId": tmnxBsxChargeGrpExportId,
       "tmnxBsxPlcyCfgTable": tmnxBsxPlcyCfgTable,
       "tmnxBsxPlcyCfgEntry": tmnxBsxPlcyCfgEntry,
       "tmnxBsxPlcyPolicyVersion": tmnxBsxPlcyPolicyVersion,
       "tmnxBsxPlcyRowLastCh": tmnxBsxPlcyRowLastCh,
       "tmnxBsxPlcyDefChargeGrp": tmnxBsxPlcyDefChargeGrp,
       "tmnxBsxStatsObjs": tmnxBsxStatsObjs,
       "tmnxBsxStatsAccounting": tmnxBsxStatsAccounting,
       "tmnxBsxStatAaAcctLastChTime": tmnxBsxStatAaAcctLastChTime,
       "tmnxBsxStatAaSubLastChTime": tmnxBsxStatAaSubLastChTime,
       "tmnxBsxStatAaSubSdyLastChTime": tmnxBsxStatAaSubSdyLastChTime,
       "tmnxBsxStatIsaAaCfgLastChTime": tmnxBsxStatIsaAaCfgLastChTime,
       "tmnxBsxStatAaAcctCfgTable": tmnxBsxStatAaAcctCfgTable,
       "tmnxBsxStatAaAcctCfgEntry": tmnxBsxStatAaAcctCfgEntry,
       "tmnxBsxStatAaAcctCfgType": tmnxBsxStatAaAcctCfgType,
       "tmnxBsxStatAaAcctCfgCollStats": tmnxBsxStatAaAcctCfgCollStats,
       "tmnxBsxStatAaAcctCfgPolicy": tmnxBsxStatAaAcctCfgPolicy,
       "tmnxBsxStatAaAcctCfgAggrStats": tmnxBsxStatAaAcctCfgAggrStats,
       "tmnxBsxStatAaAcctCfgAdminState": tmnxBsxStatAaAcctCfgAdminState,
       "tmnxBsxStatAaAcctCfgMaxThruStats": tmnxBsxStatAaAcctCfgMaxThruStats,
       "tmnxBsxStatAaAcctCfgRadiusPlcy": tmnxBsxStatAaAcctCfgRadiusPlcy,
       "tmnxBsxStatAaSubTable": tmnxBsxStatAaSubTable,
       "tmnxBsxStatAaSubEntry": tmnxBsxStatAaSubEntry,
       "tmnxBsxAaSubscriberType": tmnxBsxAaSubscriberType,
       "tmnxBsxAaSubscriber": tmnxBsxAaSubscriber,
       "tmnxBsxStatAaType": tmnxBsxStatAaType,
       "tmnxBsxStatAaName": tmnxBsxStatAaName,
       "tmnxBsxStatAaSubDiscontTime": tmnxBsxStatAaSubDiscontTime,
       "tmnxBsxStatAaSubOctsAdmFmSb": tmnxBsxStatAaSubOctsAdmFmSb,
       "tmnxBsxStatAaSubPktsAdmFmSb": tmnxBsxStatAaSubPktsAdmFmSb,
       "tmnxBsxStatAaSubFlwsAdmFmSb": tmnxBsxStatAaSubFlwsAdmFmSb,
       "tmnxBsxStatAaSubOctsDnyFmSb": tmnxBsxStatAaSubOctsDnyFmSb,
       "tmnxBsxStatAaSubPktsDnyFmSb": tmnxBsxStatAaSubPktsDnyFmSb,
       "tmnxBsxStatAaSubFlwsDnyFmSb": tmnxBsxStatAaSubFlwsDnyFmSb,
       "tmnxBsxStatAaSubOctsAdmToSb": tmnxBsxStatAaSubOctsAdmToSb,
       "tmnxBsxStatAaSubPktsAdmToSb": tmnxBsxStatAaSubPktsAdmToSb,
       "tmnxBsxStatAaSubFlwsAdmToSb": tmnxBsxStatAaSubFlwsAdmToSb,
       "tmnxBsxStatAaSubOctsDnyToSb": tmnxBsxStatAaSubOctsDnyToSb,
       "tmnxBsxStatAaSubPktsDnyToSb": tmnxBsxStatAaSubPktsDnyToSb,
       "tmnxBsxStatAaSubFlwsDnyToSb": tmnxBsxStatAaSubFlwsDnyToSb,
       "tmnxBsxStatAaSubTermFlwDur": tmnxBsxStatAaSubTermFlwDur,
       "tmnxBsxStatAaSubTermFlws": tmnxBsxStatAaSubTermFlws,
       "tmnxBsxStatAaSubShrtDurFlws": tmnxBsxStatAaSubShrtDurFlws,
       "tmnxBsxStatAaSubMedDurFlws": tmnxBsxStatAaSubMedDurFlws,
       "tmnxBsxStatAaSubLngDurFlws": tmnxBsxStatAaSubLngDurFlws,
       "tmnxBsxStatAaSubActFlwsFmSb": tmnxBsxStatAaSubActFlwsFmSb,
       "tmnxBsxStatAaSubActFlwsToSb": tmnxBsxStatAaSubActFlwsToSb,
       "tmnxBsxStatAaSubHCOctsAdmFmSb": tmnxBsxStatAaSubHCOctsAdmFmSb,
       "tmnxBsxStatAaSubHCPktsAdmFmSb": tmnxBsxStatAaSubHCPktsAdmFmSb,
       "tmnxBsxStatAaSubHCFlwsAdmFmSb": tmnxBsxStatAaSubHCFlwsAdmFmSb,
       "tmnxBsxStatAaSubHCOctsDnyFmSb": tmnxBsxStatAaSubHCOctsDnyFmSb,
       "tmnxBsxStatAaSubHCPktsDnyFmSb": tmnxBsxStatAaSubHCPktsDnyFmSb,
       "tmnxBsxStatAaSubHCFlwsDnyFmSb": tmnxBsxStatAaSubHCFlwsDnyFmSb,
       "tmnxBsxStatAaSubHCOctsAdmToSb": tmnxBsxStatAaSubHCOctsAdmToSb,
       "tmnxBsxStatAaSubHCPktsAdmToSb": tmnxBsxStatAaSubHCPktsAdmToSb,
       "tmnxBsxStatAaSubHCFlwsAdmToSb": tmnxBsxStatAaSubHCFlwsAdmToSb,
       "tmnxBsxStatAaSubHCOctsDnyToSb": tmnxBsxStatAaSubHCOctsDnyToSb,
       "tmnxBsxStatAaSubHCPktsDnyToSb": tmnxBsxStatAaSubHCPktsDnyToSb,
       "tmnxBsxStatAaSubHCFlwsDnyToSb": tmnxBsxStatAaSubHCFlwsDnyToSb,
       "tmnxBsxStatAaSubHCTermFlwDur": tmnxBsxStatAaSubHCTermFlwDur,
       "tmnxBsxStatAaSubHCTermFlws": tmnxBsxStatAaSubHCTermFlws,
       "tmnxBsxStatAaSubHCShrtDurFlws": tmnxBsxStatAaSubHCShrtDurFlws,
       "tmnxBsxStatAaSubHCMedDurFlws": tmnxBsxStatAaSubHCMedDurFlws,
       "tmnxBsxStatAaSubHCLngDurFlws": tmnxBsxStatAaSubHCLngDurFlws,
       "tmnxBsxStatAaSubSdyTable": tmnxBsxStatAaSubSdyTable,
       "tmnxBsxStatAaSubSdyEntry": tmnxBsxStatAaSubSdyEntry,
       "tmnxBsxStatAaSubSdyDiscontTime": tmnxBsxStatAaSubSdyDiscontTime,
       "tmnxBsxStatAaSubSdyOctsAdmFmSb": tmnxBsxStatAaSubSdyOctsAdmFmSb,
       "tmnxBsxStatAaSubSdyPktsAdmFmSb": tmnxBsxStatAaSubSdyPktsAdmFmSb,
       "tmnxBsxStatAaSubSdyFlwsAdmFmSb": tmnxBsxStatAaSubSdyFlwsAdmFmSb,
       "tmnxBsxStatAaSubSdyOctsDnyFmSb": tmnxBsxStatAaSubSdyOctsDnyFmSb,
       "tmnxBsxStatAaSubSdyPktsDnyFmSb": tmnxBsxStatAaSubSdyPktsDnyFmSb,
       "tmnxBsxStatAaSubSdyFlwsDnyFmSb": tmnxBsxStatAaSubSdyFlwsDnyFmSb,
       "tmnxBsxStatAaSubSdyOctsAdmToSb": tmnxBsxStatAaSubSdyOctsAdmToSb,
       "tmnxBsxStatAaSubSdyPktsAdmToSb": tmnxBsxStatAaSubSdyPktsAdmToSb,
       "tmnxBsxStatAaSubSdyFlwsAdmToSb": tmnxBsxStatAaSubSdyFlwsAdmToSb,
       "tmnxBsxStatAaSubSdyOctsDnyToSb": tmnxBsxStatAaSubSdyOctsDnyToSb,
       "tmnxBsxStatAaSubSdyPktsDnyToSb": tmnxBsxStatAaSubSdyPktsDnyToSb,
       "tmnxBsxStatAaSubSdyFlwsDnyToSb": tmnxBsxStatAaSubSdyFlwsDnyToSb,
       "tmnxBsxStatAaSubSdyTermFlwDur": tmnxBsxStatAaSubSdyTermFlwDur,
       "tmnxBsxStatAaSubSdyTermFlws": tmnxBsxStatAaSubSdyTermFlws,
       "tmnxBsxStatAaSubSdyShrtDurFlws": tmnxBsxStatAaSubSdyShrtDurFlws,
       "tmnxBsxStatAaSubSdyMedDurFlws": tmnxBsxStatAaSubSdyMedDurFlws,
       "tmnxBsxStatAaSubSdyLngDurFlws": tmnxBsxStatAaSubSdyLngDurFlws,
       "tmnxBsxStatAaSubSdyActFlwsFmSb": tmnxBsxStatAaSubSdyActFlwsFmSb,
       "tmnxBsxStatAaSubSdyActFlwsToSb": tmnxBsxStatAaSubSdyActFlwsToSb,
       "tmnxBsxStatAaSubSdyHCOctsAdmFmSb": tmnxBsxStatAaSubSdyHCOctsAdmFmSb,
       "tmnxBsxStatAaSubSdyHCPktsAdmFmSb": tmnxBsxStatAaSubSdyHCPktsAdmFmSb,
       "tmnxBsxStatAaSubSdyHCFlwsAdmFmSb": tmnxBsxStatAaSubSdyHCFlwsAdmFmSb,
       "tmnxBsxStatAaSubSdyHCOctsDnyFmSb": tmnxBsxStatAaSubSdyHCOctsDnyFmSb,
       "tmnxBsxStatAaSubSdyHCPktsDnyFmSb": tmnxBsxStatAaSubSdyHCPktsDnyFmSb,
       "tmnxBsxStatAaSubSdyHCFlwsDnyFmSb": tmnxBsxStatAaSubSdyHCFlwsDnyFmSb,
       "tmnxBsxStatAaSubSdyHCOctsAdmToSb": tmnxBsxStatAaSubSdyHCOctsAdmToSb,
       "tmnxBsxStatAaSubSdyHCPktsAdmToSb": tmnxBsxStatAaSubSdyHCPktsAdmToSb,
       "tmnxBsxStatAaSubSdyHCFlwsAdmToSb": tmnxBsxStatAaSubSdyHCFlwsAdmToSb,
       "tmnxBsxStatAaSubSdyHCOctsDnyToSb": tmnxBsxStatAaSubSdyHCOctsDnyToSb,
       "tmnxBsxStatAaSubSdyHCPktsDnyToSb": tmnxBsxStatAaSubSdyHCPktsDnyToSb,
       "tmnxBsxStatAaSubSdyHCFlwsDnyToSb": tmnxBsxStatAaSubSdyHCFlwsDnyToSb,
       "tmnxBsxStatAaSubSdyHCTermFlwDur": tmnxBsxStatAaSubSdyHCTermFlwDur,
       "tmnxBsxStatAaSubSdyHCTermFlws": tmnxBsxStatAaSubSdyHCTermFlws,
       "tmnxBsxStatAaSubSdyHCShrtDurFlws": tmnxBsxStatAaSubSdyHCShrtDurFlws,
       "tmnxBsxStatAaSubSdyHCMedDurFlws": tmnxBsxStatAaSubSdyHCMedDurFlws,
       "tmnxBsxStatAaSubSdyHCLngDurFlws": tmnxBsxStatAaSubSdyHCLngDurFlws,
       "tmnxBsxStatAaSubCfgTable": tmnxBsxStatAaSubCfgTable,
       "tmnxBsxStatAaSubCfgEntry": tmnxBsxStatAaSubCfgEntry,
       "tmnxBsxStatAaSubCfgRowStatus": tmnxBsxStatAaSubCfgRowStatus,
       "tmnxBsxStatAaSubCfgExportMethod": tmnxBsxStatAaSubCfgExportMethod,
       "tmnxBsxStatAaSubSdyCfgTable": tmnxBsxStatAaSubSdyCfgTable,
       "tmnxBsxStatAaSubSdyCfgEntry": tmnxBsxStatAaSubSdyCfgEntry,
       "tmnxBsxStatAaSubSdyRowStatus": tmnxBsxStatAaSubSdyRowStatus,
       "tmnxBsxStatAaTable": tmnxBsxStatAaTable,
       "tmnxBsxStatAaEntry": tmnxBsxStatAaEntry,
       "tmnxBsxStatAaDiscontTime": tmnxBsxStatAaDiscontTime,
       "tmnxBsxStatAaOctsAdmFmSb": tmnxBsxStatAaOctsAdmFmSb,
       "tmnxBsxStatAaPktsAdmFmSb": tmnxBsxStatAaPktsAdmFmSb,
       "tmnxBsxStatAaFlwsAdmFmSb": tmnxBsxStatAaFlwsAdmFmSb,
       "tmnxBsxStatAaOctsDnyFmSb": tmnxBsxStatAaOctsDnyFmSb,
       "tmnxBsxStatAaPktsDnyFmSb": tmnxBsxStatAaPktsDnyFmSb,
       "tmnxBsxStatAaFlwsDnyFmSb": tmnxBsxStatAaFlwsDnyFmSb,
       "tmnxBsxStatAaOctsAdmToSb": tmnxBsxStatAaOctsAdmToSb,
       "tmnxBsxStatAaPktsAdmToSb": tmnxBsxStatAaPktsAdmToSb,
       "tmnxBsxStatAaFlwsAdmToSb": tmnxBsxStatAaFlwsAdmToSb,
       "tmnxBsxStatAaOctsDnyToSb": tmnxBsxStatAaOctsDnyToSb,
       "tmnxBsxStatAaPktsDnyToSb": tmnxBsxStatAaPktsDnyToSb,
       "tmnxBsxStatAaFlwsDnyToSb": tmnxBsxStatAaFlwsDnyToSb,
       "tmnxBsxStatAaTermFlwDur": tmnxBsxStatAaTermFlwDur,
       "tmnxBsxStatAaTermFlws": tmnxBsxStatAaTermFlws,
       "tmnxBsxStatAaShrtDurFlws": tmnxBsxStatAaShrtDurFlws,
       "tmnxBsxStatAaMedDurFlws": tmnxBsxStatAaMedDurFlws,
       "tmnxBsxStatAaLngDurFlws": tmnxBsxStatAaLngDurFlws,
       "tmnxBsxStatAaActFlwsFmSb": tmnxBsxStatAaActFlwsFmSb,
       "tmnxBsxStatAaActFlwsToSb": tmnxBsxStatAaActFlwsToSb,
       "tmnxBsxStatAaNumSubscribers": tmnxBsxStatAaNumSubscribers,
       "tmnxBsxStatAaHCOctsAdmFmSb": tmnxBsxStatAaHCOctsAdmFmSb,
       "tmnxBsxStatAaHCPktsAdmFmSb": tmnxBsxStatAaHCPktsAdmFmSb,
       "tmnxBsxStatAaHCFlwsAdmFmSb": tmnxBsxStatAaHCFlwsAdmFmSb,
       "tmnxBsxStatAaHCOctsDnyFmSb": tmnxBsxStatAaHCOctsDnyFmSb,
       "tmnxBsxStatAaHCPktsDnyFmSb": tmnxBsxStatAaHCPktsDnyFmSb,
       "tmnxBsxStatAaHCFlwsDnyFmSb": tmnxBsxStatAaHCFlwsDnyFmSb,
       "tmnxBsxStatAaHCOctsAdmToSb": tmnxBsxStatAaHCOctsAdmToSb,
       "tmnxBsxStatAaHCPktsAdmToSb": tmnxBsxStatAaHCPktsAdmToSb,
       "tmnxBsxStatAaHCFlwsAdmToSb": tmnxBsxStatAaHCFlwsAdmToSb,
       "tmnxBsxStatAaHCOctsDnyToSb": tmnxBsxStatAaHCOctsDnyToSb,
       "tmnxBsxStatAaHCPktsDnyToSb": tmnxBsxStatAaHCPktsDnyToSb,
       "tmnxBsxStatAaHCFlwsDnyToSb": tmnxBsxStatAaHCFlwsDnyToSb,
       "tmnxBsxStatAaHCTermFlwDur": tmnxBsxStatAaHCTermFlwDur,
       "tmnxBsxStatAaHCTermFlws": tmnxBsxStatAaHCTermFlws,
       "tmnxBsxStatAaHCShrtDurFlws": tmnxBsxStatAaHCShrtDurFlws,
       "tmnxBsxStatAaHCMedDurFlws": tmnxBsxStatAaHCMedDurFlws,
       "tmnxBsxStatAaHCLngDurFlws": tmnxBsxStatAaHCLngDurFlws,
       "tmnxBsxStatAaAppFilterTable": tmnxBsxStatAaAppFilterTable,
       "tmnxBsxStatAaAppFilterEntry": tmnxBsxStatAaAppFilterEntry,
       "tmnxBsxStatAaAppFilterHCFlows": tmnxBsxStatAaAppFilterHCFlows,
       "tmnxBsxStatAaAppFilterFlowsLo": tmnxBsxStatAaAppFilterFlowsLo,
       "tmnxBsxStatAaAppFilterFlowsHi": tmnxBsxStatAaAppFilterFlowsHi,
       "tmnxBsxStatAaAppFilterFlowHCOctC": tmnxBsxStatAaAppFilterFlowHCOctC,
       "tmnxBsxStatAaAppFilterFlowOctCLo": tmnxBsxStatAaAppFilterFlowOctCLo,
       "tmnxBsxStatAaAppFilterFlowOctCHi": tmnxBsxStatAaAppFilterFlowOctCHi,
       "tmnxBsxStatIsaAaCfgTable": tmnxBsxStatIsaAaCfgTable,
       "tmnxBsxStatIsaAaCfgEntry": tmnxBsxStatIsaAaCfgEntry,
       "tmnxBsxStatIsaAaCfgType": tmnxBsxStatIsaAaCfgType,
       "tmnxBsxStatIsaAaCfgCollStats": tmnxBsxStatIsaAaCfgCollStats,
       "tmnxBsxStatIsaAaCfgPolicy": tmnxBsxStatIsaAaCfgPolicy,
       "tmnxBsxNotifObjs": tmnxBsxNotifObjs,
       "tmnxBsxNotifyIsaAaGroupIndex": tmnxBsxNotifyIsaAaGroupIndex,
       "tmnxBsxNotifyActiveMda": tmnxBsxNotifyActiveMda,
       "tmnxBsxNotifyActionStatus": tmnxBsxNotifyActionStatus,
       "tmnxBsxNotifyAaSubscriberType": tmnxBsxNotifyAaSubscriberType,
       "tmnxBsxNotifyAaSubscriberName": tmnxBsxNotifyAaSubscriberName,
       "tmnxBsxNotifyAaSubAcctLossReason": tmnxBsxNotifyAaSubAcctLossReason,
       "tmnxBsxNotifyAaGrpPartIndex": tmnxBsxNotifyAaGrpPartIndex,
       "tmnxBsxNotifyTransitIpPolicyId": tmnxBsxNotifyTransitIpPolicyId,
       "tmnxBsxNotifyRadiusCoAAuditState": tmnxBsxNotifyRadiusCoAAuditState,
       "tmnxBsxNotifyReason": tmnxBsxNotifyReason,
       "tmnxBsxCflowdObjs": tmnxBsxCflowdObjs,
       "tmnxBsxCflowdScalars": tmnxBsxCflowdScalars,
       "tmnxBsxCflowdLastChangeTime": tmnxBsxCflowdLastChangeTime,
       "tmnxBsxCflowdCollLastChangeTime": tmnxBsxCflowdCollLastChangeTime,
       "tmnxBsxCflowdPerfLastChangeTime": tmnxBsxCflowdPerfLastChangeTime,
       "tmnxBsxCflowdExpLastChangeTime": tmnxBsxCflowdExpLastChangeTime,
       "tmnxBsxCflowdPerfExpLastChTime": tmnxBsxCflowdPerfExpLastChTime,
       "tmnxBsxCflowdTable": tmnxBsxCflowdTable,
       "tmnxBsxCflowdEntry": tmnxBsxCflowdEntry,
       "tmnxBsxCflowdRowLastChange": tmnxBsxCflowdRowLastChange,
       "tmnxBsxCflowdAdminState": tmnxBsxCflowdAdminState,
       "tmnxBsxCflowdVolRate": tmnxBsxCflowdVolRate,
       "tmnxBsxCflowdTemplateRetransmit": tmnxBsxCflowdTemplateRetransmit,
       "tmnxBsxCflowdCollTable": tmnxBsxCflowdCollTable,
       "tmnxBsxCflowdCollEntry": tmnxBsxCflowdCollEntry,
       "tmnxBsxCflowdCollAddressType": tmnxBsxCflowdCollAddressType,
       "tmnxBsxCflowdCollAddress": tmnxBsxCflowdCollAddress,
       "tmnxBsxCflowdCollPort": tmnxBsxCflowdCollPort,
       "tmnxBsxCflowdCollRowStatus": tmnxBsxCflowdCollRowStatus,
       "tmnxBsxCflowdCollRowLastChange": tmnxBsxCflowdCollRowLastChange,
       "tmnxBsxCflowdCollDescription": tmnxBsxCflowdCollDescription,
       "tmnxBsxCflowdCollAdminState": tmnxBsxCflowdCollAdminState,
       "tmnxBsxCflowdCollOperState": tmnxBsxCflowdCollOperState,
       "tmnxBsxCflowdCollVersion": tmnxBsxCflowdCollVersion,
       "tmnxBsxCflowdPerfTable": tmnxBsxCflowdPerfTable,
       "tmnxBsxCflowdPerfEntry": tmnxBsxCflowdPerfEntry,
       "tmnxBsxCflowdPerfMeasType": tmnxBsxCflowdPerfMeasType,
       "tmnxBsxCflowdPerfRowLastChange": tmnxBsxCflowdPerfRowLastChange,
       "tmnxBsxCflowdPerfFlowRate": tmnxBsxCflowdPerfFlowRate,
       "tmnxBsxCflowdPerfFlowRate2": tmnxBsxCflowdPerfFlowRate2,
       "tmnxBsxCflowdExpTable": tmnxBsxCflowdExpTable,
       "tmnxBsxCflowdExpEntry": tmnxBsxCflowdExpEntry,
       "tmnxBsxCflowdExpType": tmnxBsxCflowdExpType,
       "tmnxBsxCflowdExpRowLastChange": tmnxBsxCflowdExpRowLastChange,
       "tmnxBsxCflowdExpAdminState": tmnxBsxCflowdExpAdminState,
       "tmnxBsxCflowdPerfExpTable": tmnxBsxCflowdPerfExpTable,
       "tmnxBsxCflowdPerfExpEntry": tmnxBsxCflowdPerfExpEntry,
       "tmnxBsxCflowdPerfExpRowStatus": tmnxBsxCflowdPerfExpRowStatus,
       "tmnxBsxCflowdPerfExpRowLastChnge": tmnxBsxCflowdPerfExpRowLastChnge,
       "tmnxBsxCflowdPerfExpRateNum": tmnxBsxCflowdPerfExpRateNum,
       "tmnxBsxCflowdStatusTable": tmnxBsxCflowdStatusTable,
       "tmnxBsxCflowdStatusEntry": tmnxBsxCflowdStatusEntry,
       "tmnxBsxCflowdStatusDiscontTime": tmnxBsxCflowdStatusDiscontTime,
       "tmnxBsxCflowdStatusActFlowsCurr": tmnxBsxCflowdStatusActFlowsCurr,
       "tmnxBsxCflowdStatusRecRateCurr": tmnxBsxCflowdStatusRecRateCurr,
       "tmnxBsxCflowdStatusPktRateCurr": tmnxBsxCflowdStatusPktRateCurr,
       "tmnxBsxCflowdStatusRecReported": tmnxBsxCflowdStatusRecReported,
       "tmnxBsxCflowdStatusHCRecReported": tmnxBsxCflowdStatusHCRecReported,
       "tmnxBsxCflowdStatusRecDropped": tmnxBsxCflowdStatusRecDropped,
       "tmnxBsxCflowdStatusHCRecDropped": tmnxBsxCflowdStatusHCRecDropped,
       "tmnxBsxCflowdStatusPktsSent": tmnxBsxCflowdStatusPktsSent,
       "tmnxBsxCflowdStatusHCPktsSent": tmnxBsxCflowdStatusHCPktsSent,
       "tmnxBsxCflowdStatusFlowsNoRes": tmnxBsxCflowdStatusFlowsNoRes,
       "tmnxBsxCflowdStatusHCFlowsNoRes": tmnxBsxCflowdStatusHCFlowsNoRes,
       "tmnxBsxCflowdStatusHCUSupSSRCSt": tmnxBsxCflowdStatusHCUSupSSRCSt,
       "tmnxBsxCflowdStatusUSupSSRCStLo": tmnxBsxCflowdStatusUSupSSRCStLo,
       "tmnxBsxCflowdStatusUSupSSRCStHi": tmnxBsxCflowdStatusUSupSSRCStHi,
       "tmnxBsxCflowdCollStatTable": tmnxBsxCflowdCollStatTable,
       "tmnxBsxCflowdCollStatEntry": tmnxBsxCflowdCollStatEntry,
       "tmnxBsxCflowdCollStatDiscontTime": tmnxBsxCflowdCollStatDiscontTime,
       "tmnxBsxCflowdCollStatRecSent": tmnxBsxCflowdCollStatRecSent,
       "tmnxBsxCflowdCollStatHCRecSent": tmnxBsxCflowdCollStatHCRecSent,
       "tmnxBsxCflowdExpStatTable": tmnxBsxCflowdExpStatTable,
       "tmnxBsxCflowdExpStatEntry": tmnxBsxCflowdExpStatEntry,
       "tmnxBsxCflowdExpStatDiscontTime": tmnxBsxCflowdExpStatDiscontTime,
       "tmnxBsxCflowdExpStatRecReport": tmnxBsxCflowdExpStatRecReport,
       "tmnxBsxCflowdExpStatHCRecReport": tmnxBsxCflowdExpStatHCRecReport,
       "tmnxBsxCflowdExpStatRecDropped": tmnxBsxCflowdExpStatRecDropped,
       "tmnxBsxCflowdExpStatHCRecDropped": tmnxBsxCflowdExpStatHCRecDropped,
       "tmnxBsxCflowdExpStatFlowsNoRes": tmnxBsxCflowdExpStatFlowsNoRes,
       "tmnxBsxCflowdExpStatHCFlowsNoRes": tmnxBsxCflowdExpStatHCFlowsNoRes,
       "tmnxBsxCflowdExpStatHCUSupSSRCSt": tmnxBsxCflowdExpStatHCUSupSSRCSt,
       "tmnxBsxCflowdExpStatUSupSSRCStLo": tmnxBsxCflowdExpStatUSupSSRCStLo,
       "tmnxBsxCflowdExpStatUSupSSRCStHi": tmnxBsxCflowdExpStatUSupSSRCStHi,
       "tmnxBsxOvrdObjs": tmnxBsxOvrdObjs,
       "tmnxBsxOvrdScalars": tmnxBsxOvrdScalars,
       "tmnxBsxOvrdAaSubLastChTime": tmnxBsxOvrdAaSubLastChTime,
       "tmnxBsxOvrdAaSubCharLastChTm": tmnxBsxOvrdAaSubCharLastChTm,
       "tmnxBsxOvrdAaSubTable": tmnxBsxOvrdAaSubTable,
       "tmnxBsxOvrdAaSubEntry": tmnxBsxOvrdAaSubEntry,
       "tmnxBsxOvrdAaSubRowStatus": tmnxBsxOvrdAaSubRowStatus,
       "tmnxBsxOvrdAaSubRowLastCh": tmnxBsxOvrdAaSubRowLastCh,
       "tmnxBsxOvrdAaSubCharTable": tmnxBsxOvrdAaSubCharTable,
       "tmnxBsxOvrdAaSubCharEntry": tmnxBsxOvrdAaSubCharEntry,
       "tmnxBsxOvrdAaSubCharRowStatus": tmnxBsxOvrdAaSubCharRowStatus,
       "tmnxBsxOvrdAaSubCharRowLastCh": tmnxBsxOvrdAaSubCharRowLastCh,
       "tmnxBsxOvrdAaSubCharValName": tmnxBsxOvrdAaSubCharValName,
       "tmnxBsxTransitObjs": tmnxBsxTransitObjs,
       "tmnxBsxTransitScalars": tmnxBsxTransitScalars,
       "tmnxBsxTransitIpPolicyLastChTime": tmnxBsxTransitIpPolicyLastChTime,
       "tmnxBsxTransIpPlcySubLastChTime": tmnxBsxTransIpPlcySubLastChTime,
       "tmnxBsxTransIpPlcyAddrLastChTime": tmnxBsxTransIpPlcyAddrLastChTime,
       "tmnxBsxTransPrefPlcyLastChTime": tmnxBsxTransPrefPlcyLastChTime,
       "tmnxBsxTransPrefSubLastChTime": tmnxBsxTransPrefSubLastChTime,
       "tmnxBsxTransPrefEntryLastChTime": tmnxBsxTransPrefEntryLastChTime,
       "tmnxBsxTransitIpPolicyTable": tmnxBsxTransitIpPolicyTable,
       "tmnxBsxTransitIpPolicyEntry": tmnxBsxTransitIpPolicyEntry,
       "tmnxBsxTransitIpPolicyId": tmnxBsxTransitIpPolicyId,
       "tmnxBsxTransitIpPolicyRowStatus": tmnxBsxTransitIpPolicyRowStatus,
       "tmnxBsxTransitIpPolicyRowLastCh": tmnxBsxTransitIpPolicyRowLastCh,
       "tmnxBsxTransitIpPolicyDesc": tmnxBsxTransitIpPolicyDesc,
       "tmnxBsxTransitIpPolicyDefAppProf": tmnxBsxTransitIpPolicyDefAppProf,
       "tmnxBsxTransitIpPolicySubIdPlcy": tmnxBsxTransitIpPolicySubIdPlcy,
       "tmnxBsxTransitIpPolicyRadius": tmnxBsxTransitIpPolicyRadius,
       "tmnxBsxTransitIpPolicyRadAuthPlc": tmnxBsxTransitIpPolicyRadAuthPlc,
       "tmnxBsxTransitIpPolicyDhcp": tmnxBsxTransitIpPolicyDhcp,
       "tmnxBsxTransitIpPolicyIPv6PfxLen": tmnxBsxTransitIpPolicyIPv6PfxLen,
       "tmnxBsxTransitIpPolicySubsCount": tmnxBsxTransitIpPolicySubsCount,
       "tmnxBsxTransitIpPolicyIPv4EntCnt": tmnxBsxTransitIpPolicyIPv4EntCnt,
       "tmnxBsxTransitIpPolicyIPv6EntCnt": tmnxBsxTransitIpPolicyIPv6EntCnt,
       "tmnxBsxTransitIpPolicySeenIp": tmnxBsxTransitIpPolicySeenIp,
       "tmnxBsxTransitIpPolicyAutoCreate": tmnxBsxTransitIpPolicyAutoCreate,
       "tmnxBsxTransitIpPolicySeenIpRad": tmnxBsxTransitIpPolicySeenIpRad,
       "tmnxBsxTransitIpPolicySubTable": tmnxBsxTransitIpPolicySubTable,
       "tmnxBsxTransitIpPolicySubEntry": tmnxBsxTransitIpPolicySubEntry,
       "tmnxBsxTransitIpPolicySubscriber": tmnxBsxTransitIpPolicySubscriber,
       "tmnxBsxTransIpPlcySubRowStatus": tmnxBsxTransIpPlcySubRowStatus,
       "tmnxBsxTransIpPlcySubRowLastCh": tmnxBsxTransIpPlcySubRowLastCh,
       "tmnxBsxTransIpPlcySubAppProfNm": tmnxBsxTransIpPlcySubAppProfNm,
       "tmnxBsxTransIpPlcySubRefCount": tmnxBsxTransIpPlcySubRefCount,
       "tmnxBsxTransitIpPolicyAddrTable": tmnxBsxTransitIpPolicyAddrTable,
       "tmnxBsxTransitIpPolicyAddrEntry": tmnxBsxTransitIpPolicyAddrEntry,
       "tmnxBsxTransitIpPolicyAddrType": tmnxBsxTransitIpPolicyAddrType,
       "tmnxBsxTransitIpPolicyAddr": tmnxBsxTransitIpPolicyAddr,
       "tmnxBsxTransIpPlcyAddrRowStatus": tmnxBsxTransIpPlcyAddrRowStatus,
       "tmnxBsxTransIpPlcyAddrRowLastCh": tmnxBsxTransIpPlcyAddrRowLastCh,
       "tmnxBsxTransIpPlcyAddrSubscriber": tmnxBsxTransIpPlcyAddrSubscriber,
       "tmnxBsxTransitIpSumTable": tmnxBsxTransitIpSumTable,
       "tmnxBsxTransitIpSumEntry": tmnxBsxTransitIpSumEntry,
       "tmnxBsxTransitIpSumUpdateTime": tmnxBsxTransitIpSumUpdateTime,
       "tmnxBsxTransitIpSumParentSubType": tmnxBsxTransitIpSumParentSubType,
       "tmnxBsxTransitIpSumParentSub": tmnxBsxTransitIpSumParentSub,
       "tmnxBsxTransitIpSumAppProfNm": tmnxBsxTransitIpSumAppProfNm,
       "tmnxBsxTransitIpSumIpOriginMask": tmnxBsxTransitIpSumIpOriginMask,
       "tmnxBsxTransPrefPolicyTable": tmnxBsxTransPrefPolicyTable,
       "tmnxBsxTransPrefPolicyEntry": tmnxBsxTransPrefPolicyEntry,
       "tmnxBsxTransPrefPolicyId": tmnxBsxTransPrefPolicyId,
       "tmnxBsxTransPrefPolicyRowStatus": tmnxBsxTransPrefPolicyRowStatus,
       "tmnxBsxTransPrefPolicyRowLastCh": tmnxBsxTransPrefPolicyRowLastCh,
       "tmnxBsxTransPrefPolicyDesc": tmnxBsxTransPrefPolicyDesc,
       "tmnxBsxTransPrefPolicySubsCount": tmnxBsxTransPrefPolicySubsCount,
       "tmnxBsxTransPrefPolicyEntCount": tmnxBsxTransPrefPolicyEntCount,
       "tmnxBsxTransPrefPolicyIPv4EntCnt": tmnxBsxTransPrefPolicyIPv4EntCnt,
       "tmnxBsxTransPrefPolicyIPv6EntCnt": tmnxBsxTransPrefPolicyIPv6EntCnt,
       "tmnxBsxTransPrefSubTable": tmnxBsxTransPrefSubTable,
       "tmnxBsxTransPrefSubEntry": tmnxBsxTransPrefSubEntry,
       "tmnxBsxTransPrefSubscriber": tmnxBsxTransPrefSubscriber,
       "tmnxBsxTransPrefSubRowStatus": tmnxBsxTransPrefSubRowStatus,
       "tmnxBsxTransPrefSubRowLastCh": tmnxBsxTransPrefSubRowLastCh,
       "tmnxBsxTransPrefSubIsRemote": tmnxBsxTransPrefSubIsRemote,
       "tmnxBsxTransPrefSubAppProfNm": tmnxBsxTransPrefSubAppProfNm,
       "tmnxBsxTransPrefSubRefCount": tmnxBsxTransPrefSubRefCount,
       "tmnxBsxTransPrefTable": tmnxBsxTransPrefTable,
       "tmnxBsxTransPrefEntry": tmnxBsxTransPrefEntry,
       "tmnxBsxTransPrefEntryId": tmnxBsxTransPrefEntryId,
       "tmnxBsxTransPrefEntryRowStatus": tmnxBsxTransPrefEntryRowStatus,
       "tmnxBsxTransPrefEntryRowLastCh": tmnxBsxTransPrefEntryRowLastCh,
       "tmnxBsxTransPrefEntrySubAddrType": tmnxBsxTransPrefEntrySubAddrType,
       "tmnxBsxTransPrefEntrySubAddr": tmnxBsxTransPrefEntrySubAddr,
       "tmnxBsxTransPrefEntrySubAddrLen": tmnxBsxTransPrefEntrySubAddrLen,
       "tmnxBsxTransPrefEntryNetAddrType": tmnxBsxTransPrefEntryNetAddrType,
       "tmnxBsxTransPrefEntryNetAddr": tmnxBsxTransPrefEntryNetAddr,
       "tmnxBsxTransPrefEntryNetAddrLen": tmnxBsxTransPrefEntryNetAddrLen,
       "tmnxBsxTransPrefEntrySubscriber": tmnxBsxTransPrefEntrySubscriber,
       "tmnxBsxTransPrefSumTable": tmnxBsxTransPrefSumTable,
       "tmnxBsxTransPrefSumEntry": tmnxBsxTransPrefSumEntry,
       "tmnxBsxTransPrefSumUpdateTime": tmnxBsxTransPrefSumUpdateTime,
       "tmnxBsxTransPrefSumSubAddrType": tmnxBsxTransPrefSumSubAddrType,
       "tmnxBsxTransPrefSumSubAddr": tmnxBsxTransPrefSumSubAddr,
       "tmnxBsxTransPrefSumSubAddrLen": tmnxBsxTransPrefSumSubAddrLen,
       "tmnxBsxTransPrefSumNetAddrType": tmnxBsxTransPrefSumNetAddrType,
       "tmnxBsxTransPrefSumNetAddr": tmnxBsxTransPrefSumNetAddr,
       "tmnxBsxTransPrefSumNetAddrLen": tmnxBsxTransPrefSumNetAddrLen,
       "tmnxBsxTransPrefSumParentSubType": tmnxBsxTransPrefSumParentSubType,
       "tmnxBsxTransPrefSumParentSub": tmnxBsxTransPrefSumParentSub,
       "tmnxBsxTransPrefSumAppProfNm": tmnxBsxTransPrefSumAppProfNm,
       "tmnxBsxHttpRedirObjs": tmnxBsxHttpRedirObjs,
       "tmnxBsxHttpRedirScalars": tmnxBsxHttpRedirScalars,
       "tmnxBsxHttpRedirErrLastChTime": tmnxBsxHttpRedirErrLastChTime,
       "tmnxBsxHttpRedirErrCodeLastCh": tmnxBsxHttpRedirErrCodeLastCh,
       "tmnxBsxHttpRedirLastCh": tmnxBsxHttpRedirLastCh,
       "tmnxBsxHttpRedirErrTable": tmnxBsxHttpRedirErrTable,
       "tmnxBsxHttpRedirErrEntry": tmnxBsxHttpRedirErrEntry,
       "tmnxBsxHttpRedirErrName": tmnxBsxHttpRedirErrName,
       "tmnxBsxHttpRedirErrRowStatus": tmnxBsxHttpRedirErrRowStatus,
       "tmnxBsxHttpRedirErrRowLastCh": tmnxBsxHttpRedirErrRowLastCh,
       "tmnxBsxHttpRedirErrEnabled": tmnxBsxHttpRedirErrEnabled,
       "tmnxBsxHttpRedirErrDescription": tmnxBsxHttpRedirErrDescription,
       "tmnxBsxHttpRedirErrTemplateId": tmnxBsxHttpRedirErrTemplateId,
       "tmnxBsxHttpRedirErrHttpHost": tmnxBsxHttpRedirErrHttpHost,
       "tmnxBsxHttpRedirErrParticipantId": tmnxBsxHttpRedirErrParticipantId,
       "tmnxBsxHttpRedirErrCodeTable": tmnxBsxHttpRedirErrCodeTable,
       "tmnxBsxHttpRedirErrCodeEntry": tmnxBsxHttpRedirErrCodeEntry,
       "tmnxBsxHttpRedirErrCode": tmnxBsxHttpRedirErrCode,
       "tmnxBsxHttpRedirErrCodeRowStatus": tmnxBsxHttpRedirErrCodeRowStatus,
       "tmnxBsxHttpRedirErrCodeRowLastCh": tmnxBsxHttpRedirErrCodeRowLastCh,
       "tmnxBsxHttpRedirErrorCodeMsgSize": tmnxBsxHttpRedirErrorCodeMsgSize,
       "tmnxBsxHttpRdStatTable": tmnxBsxHttpRdStatTable,
       "tmnxBsxHttpRdStatEntry": tmnxBsxHttpRdStatEntry,
       "tmnxBsxHttpRdStatDiscontTime": tmnxBsxHttpRdStatDiscontTime,
       "tmnxBsxHttpRdStatHCRedir": tmnxBsxHttpRdStatHCRedir,
       "tmnxBsxHttpRdStatRedirLo": tmnxBsxHttpRdStatRedirLo,
       "tmnxBsxHttpRdStatRedirHi": tmnxBsxHttpRdStatRedirHi,
       "tmnxBsxHttpRdStatHCSizeExceeded": tmnxBsxHttpRdStatHCSizeExceeded,
       "tmnxBsxHttpRdStatSizeExceededLo": tmnxBsxHttpRdStatSizeExceededLo,
       "tmnxBsxHttpRdStatSizeExceededHi": tmnxBsxHttpRdStatSizeExceededHi,
       "tmnxBsxHttpRdStatHCOutOfResource": tmnxBsxHttpRdStatHCOutOfResource,
       "tmnxBsxHttpRdStatOutOfResourceLo": tmnxBsxHttpRdStatOutOfResourceLo,
       "tmnxBsxHttpRdStatOutOfResourceHi": tmnxBsxHttpRdStatOutOfResourceHi,
       "tmnxBsxHttpRdStatHCNotRedirFType": tmnxBsxHttpRdStatHCNotRedirFType,
       "tmnxBsxHttpRdStatNotRedirFTypeLo": tmnxBsxHttpRdStatNotRedirFTypeLo,
       "tmnxBsxHttpRdStatNotRedirFTypeHi": tmnxBsxHttpRdStatNotRedirFTypeHi,
       "tmnxBsxHttpRdStatHCNotRedir": tmnxBsxHttpRdStatHCNotRedir,
       "tmnxBsxHttpRdStatNotRedirLo": tmnxBsxHttpRdStatNotRedirLo,
       "tmnxBsxHttpRdStatNotRedirHi": tmnxBsxHttpRdStatNotRedirHi,
       "tmnxBsxHttpRedirTable": tmnxBsxHttpRedirTable,
       "tmnxBsxHttpRedirEntry": tmnxBsxHttpRedirEntry,
       "tmnxBsxHttpRedirName": tmnxBsxHttpRedirName,
       "tmnxBsxHttpRedirRowStatus": tmnxBsxHttpRedirRowStatus,
       "tmnxBsxHttpRedirRowLastCh": tmnxBsxHttpRedirRowLastCh,
       "tmnxBsxHttpRedirEnabled": tmnxBsxHttpRedirEnabled,
       "tmnxBsxHttpRedirDescription": tmnxBsxHttpRedirDescription,
       "tmnxBsxHttpRedirTemplateId": tmnxBsxHttpRedirTemplateId,
       "tmnxBsxHttpRedirHttpHost": tmnxBsxHttpRedirHttpHost,
       "tmnxBsxHttpPcyRdStatTable": tmnxBsxHttpPcyRdStatTable,
       "tmnxBsxHttpPcyRdStatEntry": tmnxBsxHttpPcyRdStatEntry,
       "tmnxBsxHttpPcyRdStatDiscontTime": tmnxBsxHttpPcyRdStatDiscontTime,
       "tmnxBsxHttpPcyRdStatHCRedir": tmnxBsxHttpPcyRdStatHCRedir,
       "tmnxBsxHttpPcyRdStatRedirLo": tmnxBsxHttpPcyRdStatRedirLo,
       "tmnxBsxHttpPcyRdStatRedirHi": tmnxBsxHttpPcyRdStatRedirHi,
       "tmnxBsxHttpPcyRdStatHCOutOfRes": tmnxBsxHttpPcyRdStatHCOutOfRes,
       "tmnxBsxHttpPcyRdStatOutOfResLo": tmnxBsxHttpPcyRdStatOutOfResLo,
       "tmnxBsxHttpPcyRdStatOutOfResHi": tmnxBsxHttpPcyRdStatOutOfResHi,
       "tmnxBsxHttpPcyRdStatHCNotRedir": tmnxBsxHttpPcyRdStatHCNotRedir,
       "tmnxBsxHttpPcyRdStatNotRedirLo": tmnxBsxHttpPcyRdStatNotRedirLo,
       "tmnxBsxHttpPcyRdStatNotRedirHi": tmnxBsxHttpPcyRdStatNotRedirHi,
       "tmnxBsxStaticDataObjs": tmnxBsxStaticDataObjs,
       "tmnxBsxStaticObjScalars": tmnxBsxStaticObjScalars,
       "tmnxBsxTListTableLastUpdateT": tmnxBsxTListTableLastUpdateT,
       "tmnxBsxTListAttribTableLUpdateT": tmnxBsxTListAttribTableLUpdateT,
       "tmnxBsxTListTable": tmnxBsxTListTable,
       "tmnxBsxTListEntry": tmnxBsxTListEntry,
       "tmnxBsxTListName": tmnxBsxTListName,
       "tmnxBsxTListRowLastUpdateT": tmnxBsxTListRowLastUpdateT,
       "tmnxBsxTListDescription": tmnxBsxTListDescription,
       "tmnxBsxTListAttribTable": tmnxBsxTListAttribTable,
       "tmnxBsxTListAttribEntry": tmnxBsxTListAttribEntry,
       "tmnxBsxTListAttribName": tmnxBsxTListAttribName,
       "tmnxBsxTListAttribSet": tmnxBsxTListAttribSet,
       "tmnxBsxTListAttribRowLastUpdateT": tmnxBsxTListAttribRowLastUpdateT,
       "tmnxBsxTListAttribType": tmnxBsxTListAttribType,
       "tmnxBsxTListAttribValue": tmnxBsxTListAttribValue,
       "tmnxBsxRedundancyObjs": tmnxBsxRedundancyObjs,
       "tmnxBsxRedundancyObjScalars": tmnxBsxRedundancyObjScalars,
       "tmnxBsxAarpTableLastChTime": tmnxBsxAarpTableLastChTime,
       "tmnxBsxAarpInstTable": tmnxBsxAarpInstTable,
       "tmnxBsxAarpInstEntry": tmnxBsxAarpInstEntry,
       "tmnxBsxAarpInstId": tmnxBsxAarpInstId,
       "tmnxBsxAarpInstRowStatus": tmnxBsxAarpInstRowStatus,
       "tmnxBsxAarpInstLastCh": tmnxBsxAarpInstLastCh,
       "tmnxBsxAarpInstDescription": tmnxBsxAarpInstDescription,
       "tmnxBsxAarpInstPeerIpType": tmnxBsxAarpInstPeerIpType,
       "tmnxBsxAarpInstPeerIpAddr": tmnxBsxAarpInstPeerIpAddr,
       "tmnxBsxAarpInstPriority": tmnxBsxAarpInstPriority,
       "tmnxBsxAarpInstAdminState": tmnxBsxAarpInstAdminState,
       "tmnxBsxAarpInstOperState": tmnxBsxAarpInstOperState,
       "tmnxBsxAarpInstState": tmnxBsxAarpInstState,
       "tmnxBsxAarpInstOperFlags": tmnxBsxAarpInstOperFlags,
       "tmnxBsxAarpInstPeerPriority": tmnxBsxAarpInstPeerPriority,
       "tmnxBsxAarpInstPeerState": tmnxBsxAarpInstPeerState,
       "tmnxBsxAarpInstPeerOperFlags": tmnxBsxAarpInstPeerOperFlags,
       "tmnxBsxAarpInstPeerSubRefType": tmnxBsxAarpInstPeerSubRefType,
       "tmnxBsxAarpInstPeerEPSapPortId": tmnxBsxAarpInstPeerEPSapPortId,
       "tmnxBsxAarpInstPeerEPSapEncap": tmnxBsxAarpInstPeerEPSapEncap,
       "tmnxBsxAarpInstPeerEPSapEncType": tmnxBsxAarpInstPeerEPSapEncType,
       "tmnxBsxAarpInstPeerEPSdpBindId": tmnxBsxAarpInstPeerEPSdpBindId,
       "tmnxBsxAarpCommandTable": tmnxBsxAarpCommandTable,
       "tmnxBsxAarpCommandEntry": tmnxBsxAarpCommandEntry,
       "tmnxBsxAarpCommandControl": tmnxBsxAarpCommandControl,
       "tmnxBsxAarpServPointTable": tmnxBsxAarpServPointTable,
       "tmnxBsxAarpServPointEntry": tmnxBsxAarpServPointEntry,
       "tmnxBsxAarpServPointRole": tmnxBsxAarpServPointRole,
       "tmnxBsxAarpServPointType": tmnxBsxAarpServPointType,
       "tmnxBsxAarpServPoint": tmnxBsxAarpServPoint,
       "tmnxBsxHttpEnrichObjs": tmnxBsxHttpEnrichObjs,
       "tmnxBsxHttpEnrichScalars": tmnxBsxHttpEnrichScalars,
       "tmnxBsxHttpEnrichLastChTime": tmnxBsxHttpEnrichLastChTime,
       "tmnxBsxHttpEnrichFieldLastChTime": tmnxBsxHttpEnrichFieldLastChTime,
       "tmnxBsxHttpEnrichTable": tmnxBsxHttpEnrichTable,
       "tmnxBsxHttpEnrichEntry": tmnxBsxHttpEnrichEntry,
       "tmnxBsxHttpEnrichName": tmnxBsxHttpEnrichName,
       "tmnxBsxHttpEnrichRowStatus": tmnxBsxHttpEnrichRowStatus,
       "tmnxBsxHttpEnrichRowLastCh": tmnxBsxHttpEnrichRowLastCh,
       "tmnxBsxHttpEnrichEnabled": tmnxBsxHttpEnrichEnabled,
       "tmnxBsxHttpEnrichDescription": tmnxBsxHttpEnrichDescription,
       "tmnxBsxHttpEnrichFieldTable": tmnxBsxHttpEnrichFieldTable,
       "tmnxBsxHttpEnrichFieldEntry": tmnxBsxHttpEnrichFieldEntry,
       "tmnxBsxHttpEnrichFieldName": tmnxBsxHttpEnrichFieldName,
       "tmnxBsxHttpEnrichFieldRowStatus": tmnxBsxHttpEnrichFieldRowStatus,
       "tmnxBsxHttpEnrichFieldRowLastCh": tmnxBsxHttpEnrichFieldRowLastCh,
       "tmnxBsxHttpEnrichFieldHeaderName": tmnxBsxHttpEnrichFieldHeaderName,
       "tmnxBsxHttpEnrichStatTable": tmnxBsxHttpEnrichStatTable,
       "tmnxBsxHttpEnrichStatEntry": tmnxBsxHttpEnrichStatEntry,
       "tmnxBsxHttpEnrichStatDiscontTime": tmnxBsxHttpEnrichStatDiscontTime,
       "tmnxBsxHttpEnrichHCNumEnriched": tmnxBsxHttpEnrichHCNumEnriched,
       "tmnxBsxHttpEnrichNumEnrichedLo": tmnxBsxHttpEnrichNumEnrichedLo,
       "tmnxBsxHttpEnrichNumEnrichedHi": tmnxBsxHttpEnrichNumEnrichedHi,
       "tmnxBsxHttpEnrichHCNumNoResource": tmnxBsxHttpEnrichHCNumNoResource,
       "tmnxBsxHttpEnrichNumNoResourceLo": tmnxBsxHttpEnrichNumNoResourceLo,
       "tmnxBsxHttpEnrichNumNoResourceHi": tmnxBsxHttpEnrichNumNoResourceHi,
       "tmnxBsxHttpEnrichHCMissngSubData": tmnxBsxHttpEnrichHCMissngSubData,
       "tmnxBsxHttpEnrichMissngSubDataLo": tmnxBsxHttpEnrichMissngSubDataLo,
       "tmnxBsxHttpEnrichMissngSubDataHi": tmnxBsxHttpEnrichMissngSubDataHi,
       "tmnxBsxHttpEnrichHCTplNotEnabled": tmnxBsxHttpEnrichHCTplNotEnabled,
       "tmnxBsxHttpEnrichTplNotEnabledLo": tmnxBsxHttpEnrichTplNotEnabledLo,
       "tmnxBsxHttpEnrichTplNotEnabledHi": tmnxBsxHttpEnrichTplNotEnabledHi,
       "tmnxBsxHttpEnrichHCTrafficChar": tmnxBsxHttpEnrichHCTrafficChar,
       "tmnxBsxHttpEnrichTrafficCharLo": tmnxBsxHttpEnrichTrafficCharLo,
       "tmnxBsxHttpEnrichTrafficCharHi": tmnxBsxHttpEnrichTrafficCharHi,
       "tmnxBsxRadApObjs": tmnxBsxRadApObjs,
       "tmnxBsxRadApScalars": tmnxBsxRadApScalars,
       "tmnxBsxRadApLastChTime": tmnxBsxRadApLastChTime,
       "tmnxBsxRadApServLastChTime": tmnxBsxRadApServLastChTime,
       "tmnxBsxRadApTable": tmnxBsxRadApTable,
       "tmnxBsxRadApEntry": tmnxBsxRadApEntry,
       "tmnxBsxRadApName": tmnxBsxRadApName,
       "tmnxBsxRadApRowStatus": tmnxBsxRadApRowStatus,
       "tmnxBsxRadApRowLastChange": tmnxBsxRadApRowLastChange,
       "tmnxBsxRadApDescription": tmnxBsxRadApDescription,
       "tmnxBsxRadApServerRetry": tmnxBsxRadApServerRetry,
       "tmnxBsxRadApServerTimeout": tmnxBsxRadApServerTimeout,
       "tmnxBsxRadApServerVRtrID": tmnxBsxRadApServerVRtrID,
       "tmnxBsxRadApServerSrcAddrType": tmnxBsxRadApServerSrcAddrType,
       "tmnxBsxRadApServerSrcAddr": tmnxBsxRadApServerSrcAddr,
       "tmnxBsxRadApServerAlgorithm": tmnxBsxRadApServerAlgorithm,
       "tmnxBsxRadApIntrmUpdateInterval": tmnxBsxRadApIntrmUpdateInterval,
       "tmnxBsxRadApSignfcntChangeDelta": tmnxBsxRadApSignfcntChangeDelta,
       "tmnxBsxRadApServTable": tmnxBsxRadApServTable,
       "tmnxBsxRadApServEntry": tmnxBsxRadApServEntry,
       "tmnxBsxRadApServIndex": tmnxBsxRadApServIndex,
       "tmnxBsxRadApServRowStatus": tmnxBsxRadApServRowStatus,
       "tmnxBsxRadApServRowLastChange": tmnxBsxRadApServRowLastChange,
       "tmnxBsxRadApServAddrType": tmnxBsxRadApServAddrType,
       "tmnxBsxRadApServAddr": tmnxBsxRadApServAddr,
       "tmnxBsxRadApServSecret": tmnxBsxRadApServSecret,
       "tmnxBsxRadApServAcctPort": tmnxBsxRadApServAcctPort,
       "tmnxBsxRadApServOperState": tmnxBsxRadApServOperState,
       "tmnxBsxRadApStatTable": tmnxBsxRadApStatTable,
       "tmnxBsxRadApStatEntry": tmnxBsxRadApStatEntry,
       "tmnxBsxRadApTxRequests": tmnxBsxRadApTxRequests,
       "tmnxBsxRadApRxResponses": tmnxBsxRadApRxResponses,
       "tmnxBsxRadApReqTimeouts": tmnxBsxRadApReqTimeouts,
       "tmnxBsxRadApSendRetries": tmnxBsxRadApSendRetries,
       "tmnxBsxRadApSendFail": tmnxBsxRadApSendFail,
       "tmnxBsxRadApServStatTable": tmnxBsxRadApServStatTable,
       "tmnxBsxRadApServStatEntry": tmnxBsxRadApServStatEntry,
       "tmnxBsxRadApServTxRequests": tmnxBsxRadApServTxRequests,
       "tmnxBsxRadApServRxResponses": tmnxBsxRadApServRxResponses,
       "tmnxBsxRadApServReqTimeouts": tmnxBsxRadApServReqTimeouts,
       "tmnxBsxRadApServReqSendFail": tmnxBsxRadApServReqSendFail,
       "tmnxBsxNotifyPrefix": tmnxBsxNotifyPrefix,
       "tmnxBsxNotifications": tmnxBsxNotifications,
       "tmnxBsxIsaAaGrpNonRedundantClear": tmnxBsxIsaAaGrpNonRedundantClear,
       "tmnxBsxIsaAaGrpSwitchover": tmnxBsxIsaAaGrpSwitchover,
       "tmnxBsxIsaAaGrpFlowFull": tmnxBsxIsaAaGrpFlowFull,
       "tmnxBsxIsaAaGrpFlowFullClear": tmnxBsxIsaAaGrpFlowFullClear,
       "tmnxBsxIsaAaGrpFailureV2": tmnxBsxIsaAaGrpFailureV2,
       "tmnxBsxIsaAaGrpFailureClearV2": tmnxBsxIsaAaGrpFailureClearV2,
       "tmnxBsxIsaAaGrpNonRedundantV2": tmnxBsxIsaAaGrpNonRedundantV2,
       "tmnxBsxIsaAaSubLoadBalance": tmnxBsxIsaAaSubLoadBalance,
       "tmnxBsxIsaAaGrpCapCostThres": tmnxBsxIsaAaGrpCapCostThres,
       "tmnxBsxIsaAaGrpCapCostThresClear": tmnxBsxIsaAaGrpCapCostThresClear,
       "tmnxBsxAaSubscribersUnassigned": tmnxBsxAaSubscribersUnassigned,
       "tmnxBsxAaSubscriberAcctDataLoss": tmnxBsxAaSubscriberAcctDataLoss,
       "tmnxBsxAaSubPolResExceeded": tmnxBsxAaSubPolResExceeded,
       "tmnxBsxAaSubPolResExceededClear": tmnxBsxAaSubPolResExceededClear,
       "tmnxBsxIsaAaGrpFlowSetup": tmnxBsxIsaAaGrpFlowSetup,
       "tmnxBsxIsaAaGrpFlowSetupClear": tmnxBsxIsaAaGrpFlowSetupClear,
       "tmnxBsxIsaAaGrpPacketRate": tmnxBsxIsaAaGrpPacketRate,
       "tmnxBsxIsaAaGrpPacketRateClear": tmnxBsxIsaAaGrpPacketRateClear,
       "tmnxBsxIsaAaGrpBitRate": tmnxBsxIsaAaGrpBitRate,
       "tmnxBsxIsaAaGrpBitRateClear": tmnxBsxIsaAaGrpBitRateClear,
       "tmnxBsxTransIpPolAaSubCreated": tmnxBsxTransIpPolAaSubCreated,
       "tmnxBsxTransIpPolAaSubDeleted": tmnxBsxTransIpPolAaSubDeleted,
       "tmnxBsxTransIpPolRadCoAAudit": tmnxBsxTransIpPolRadCoAAudit,
       "tmnxBsxTransIpPolRadCoAError": tmnxBsxTransIpPolRadCoAError,
       "tmnxBsxTransIpPolRadDiscError": tmnxBsxTransIpPolRadDiscError,
       "tmnxBsxTransIpPolDhcpAddWarning": tmnxBsxTransIpPolDhcpAddWarning,
       "tmnxBsxTransIpPolDhcpDelWarning": tmnxBsxTransIpPolDhcpDelWarning,
       "tmnxBsxIsaAaGrpFmSbWaSBufOvld": tmnxBsxIsaAaGrpFmSbWaSBufOvld,
       "tmnxBsxIsaAaGrpFmSbWaSBufOvldClr": tmnxBsxIsaAaGrpFmSbWaSBufOvldClr,
       "tmnxBsxIsaAaGrpToSbWaSBufOvld": tmnxBsxIsaAaGrpToSbWaSBufOvld,
       "tmnxBsxIsaAaGrpToSbWaSBufOvldClr": tmnxBsxIsaAaGrpToSbWaSBufOvldClr,
       "tmnxBsxIsaAaGrpOvrldCutthru": tmnxBsxIsaAaGrpOvrldCutthru,
       "tmnxBsxIsaAaGrpOvrldCutthruClr": tmnxBsxIsaAaGrpOvrldCutthruClr,
       "tmnxBsxTransitIpPersistenceWarn": tmnxBsxTransitIpPersistenceWarn,
       "tmnxBsxAarpInstOperStateChanged": tmnxBsxAarpInstOperStateChanged,
       "tmnxBsxAarpInstStateChanged": tmnxBsxAarpInstStateChanged,
       "tmnxBsxRadApFailure": tmnxBsxRadApFailure,
       "tmnxBsxRadApServOperStateChange": tmnxBsxRadApServOperStateChange}
)
