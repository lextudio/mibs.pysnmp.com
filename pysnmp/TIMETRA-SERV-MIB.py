# SNMP MIB module (TIMETRA-SERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-SERV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:04:59 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxCardSlotNum,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxMDASlotNum")

(TEntryId,
 TFilterID,
 TItemScope) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TEntryId",
    "TFilterID",
    "TItemScope")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tQosIngQGroupName,
 tSchedulerPolicyName,
 tVirtualSchedulerName) = mibBuilder.importSymbols(
    "TIMETRA-QOS-MIB",
    "tQosIngQGroupName",
    "tSchedulerPolicyName",
    "tVirtualSchedulerName")

(BgpPeeringStatus,
 QTag,
 QTagOrZero,
 SdpBindId,
 ServiceAdminStatus,
 ServiceOperStatus,
 SvcISID,
 TBurstPercentOrDefault,
 TBurstSize,
 TBurstSizeBytesOverride,
 TCIRRate,
 TCIRRateOverride,
 TDirection,
 THPolVirtualScheCIRRate,
 THPolVirtualSchePIRRate,
 THsmdaWrrWeightOverride,
 TIngressQueueId,
 TItemDescription,
 TLNamedItem,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRRate,
 TPIRRateOverride,
 TPolicyID,
 TPolicyStatementNameOrEmpty,
 TPortSchedulerPIR,
 TQosOverrideType,
 TSiteOperStatus,
 TmnxAccessLoopEncapDataLink,
 TmnxAccessLoopEncaps1,
 TmnxAccessLoopEncaps2,
 TmnxActionType,
 TmnxAdminState,
 TmnxAiiType,
 TmnxAncpStringOrZero,
 TmnxAppProfileStringOrEmpty,
 TmnxBgpAutonomousSystem,
 TmnxCustId,
 TmnxDefSubIdSource,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxLdpFECType,
 TmnxManagedRouteStatus,
 TmnxMsPwPeSignaling,
 TmnxOperGrpHoldDownTime,
 TmnxOperGrpHoldUpTime,
 TmnxPortID,
 TmnxPwGlobalId,
 TmnxPwGlobalIdOrZero,
 TmnxPwPathHopId,
 TmnxServId,
 TmnxSlaProfileStringOrEmpty,
 TmnxSpbBridgePriority,
 TmnxSpbFdbLocale,
 TmnxSpbFdbState,
 TmnxSpbFid,
 TmnxSpbFidOrZero,
 TmnxSpokeSdpId,
 TmnxSpokeSdpIdOrZero,
 TmnxSubIdentStringOrEmpty,
 TmnxSubMgtIntDestIdOrEmpty,
 TmnxSubProfileStringOrEmpty,
 TmnxSvcOperGrpCreationOrigin,
 TmnxTlsGroupId,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "BgpPeeringStatus",
    "QTag",
    "QTagOrZero",
    "SdpBindId",
    "ServiceAdminStatus",
    "ServiceOperStatus",
    "SvcISID",
    "TBurstPercentOrDefault",
    "TBurstSize",
    "TBurstSizeBytesOverride",
    "TCIRRate",
    "TCIRRateOverride",
    "TDirection",
    "THPolVirtualScheCIRRate",
    "THPolVirtualSchePIRRate",
    "THsmdaWrrWeightOverride",
    "TIngressQueueId",
    "TItemDescription",
    "TLNamedItem",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRRate",
    "TPIRRateOverride",
    "TPolicyID",
    "TPolicyStatementNameOrEmpty",
    "TPortSchedulerPIR",
    "TQosOverrideType",
    "TSiteOperStatus",
    "TmnxAccessLoopEncapDataLink",
    "TmnxAccessLoopEncaps1",
    "TmnxAccessLoopEncaps2",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxAiiType",
    "TmnxAncpStringOrZero",
    "TmnxAppProfileStringOrEmpty",
    "TmnxBgpAutonomousSystem",
    "TmnxCustId",
    "TmnxDefSubIdSource",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxLdpFECType",
    "TmnxManagedRouteStatus",
    "TmnxMsPwPeSignaling",
    "TmnxOperGrpHoldDownTime",
    "TmnxOperGrpHoldUpTime",
    "TmnxPortID",
    "TmnxPwGlobalId",
    "TmnxPwGlobalIdOrZero",
    "TmnxPwPathHopId",
    "TmnxServId",
    "TmnxSlaProfileStringOrEmpty",
    "TmnxSpbBridgePriority",
    "TmnxSpbFdbLocale",
    "TmnxSpbFdbState",
    "TmnxSpbFid",
    "TmnxSpbFidOrZero",
    "TmnxSpokeSdpId",
    "TmnxSpokeSdpIdOrZero",
    "TmnxSubIdentStringOrEmpty",
    "TmnxSubMgtIntDestIdOrEmpty",
    "TmnxSubProfileStringOrEmpty",
    "TmnxSvcOperGrpCreationOrigin",
    "TmnxTlsGroupId",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrIDOrZero")


# MODULE-IDENTITY

timetraServicesMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 4)
)
timetraServicesMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1909-02-28 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-02-28 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1900-08-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ArpHostInfoOrigin(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 5),
          ("none", 0),
          ("radius", 2))
    )



class ServObjName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class ServObjDesc(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class ServObjLongDesc(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )



class ServType(Integer32, TextualConvention):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("apipe", 7),
          ("cpipe", 10),
          ("epipe", 1),
          ("fpipe", 8),
          ("ies", 5),
          ("intTls", 11),
          ("ipipe", 9),
          ("mirror", 6),
          ("p3pipe", 2),
          ("rvpls", 15),
          ("tls", 3),
          ("unknown", 0),
          ("vprn", 4))
    )



class VpnId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class SdpId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 17407),
    )



class SdpTemplateId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class PWTemplateId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class TlsBpduTranslation(Integer32, TextualConvention):
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
        *(("auto", 1),
          ("auto-rw", 6),
          ("disabled", 2),
          ("pvst", 3),
          ("pvst-rw", 5),
          ("stp", 4))
    )



class TlsLimitMacMoveLevel(Integer32, TextualConvention):
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
        *(("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )



class TlsLimitMacMove(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blockable", 1),
          ("nonBlockable", 2))
    )



class SdpBindVcType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("atmCell", 7),
          ("atmSdu", 6),
          ("atmVcc", 8),
          ("atmVpc", 9),
          ("cesopsn", 16),
          ("cesopsnCas", 17),
          ("ether", 2),
          ("frDlci", 10),
          ("ipipe", 11),
          ("mirror", 5),
          ("satopE1", 12),
          ("satopE3", 14),
          ("satopT1", 13),
          ("satopT3", 15),
          ("undef", 1),
          ("vlan", 4))
    )



class StpExceptionCondition(Integer32, TextualConvention):
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
        *(("downstreamLoopDetected", 3),
          ("none", 1),
          ("oneWayCommuniation", 2))
    )



class LspIdList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )



class BridgeId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class TSapIngQueueId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class TSapEgrQueueId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TStpPortState(Integer32, TextualConvention):
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("discarding", 7),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )



class StpPortRole(Integer32, TextualConvention):
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
        *(("alternate", 3),
          ("backup", 4),
          ("designated", 2),
          ("disabled", 5),
          ("master", 0),
          ("root", 1))
    )



class StpProtocol(Integer32, TextualConvention):
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
        *(("mstp", 3),
          ("notApplicable", 0),
          ("rstp", 2),
          ("stp", 1))
    )



class MfibLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("sdp", 2))
    )



class MfibGrpSrcFwdOrBlk(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("forward", 1))
    )



class MvplsPruneState(Integer32, TextualConvention):
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
        *(("notApplicable", 1),
          ("notPruned", 2),
          ("pruned", 3))
    )



class TQosQueueAttribute(Bits, TextualConvention):
    status = "current"


class TVirtSchedAttribute(Bits, TextualConvention):
    status = "current"


class MstiInstanceId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class MstiInstanceIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



class DhcpLseStateInfoOrigin(Integer32, TextualConvention):
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
        *(("default", 5),
          ("dhcp", 1),
          ("gtp", 7),
          ("localUserDb", 6),
          ("none", 0),
          ("radius", 2),
          ("retailerDhcp", 4),
          ("retailerRadius", 3))
    )



class IAIDType(Integer32, TextualConvention):
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
        *(("non-temporary", 2),
          ("prefix", 3),
          ("temporary", 1),
          ("undefined", 0))
    )



class TdmOptionsSigPkts(Integer32, TextualConvention):
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
        *(("dataAndSigPkts", 3),
          ("dataPkts", 1),
          ("noSigPkts", 0),
          ("sigPkts", 2))
    )



class TdmOptionsCasTrunkFraming(Integer32, TextualConvention):
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
        *(("e1Trunk", 1),
          ("noCas", 0),
          ("t1EsfTrunk", 2),
          ("t1SfTrunk", 3))
    )



class CemSapReportAlarm(Bits, TextualConvention):
    status = "current"


class CemSapEcid(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )



class SdpBFHundredthsOfPercent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )



class SdpBindBandwidth(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )



class L2ptProtocols(Bits, TextualConvention):
    status = "current"


class L2RouteOrigin(Integer32, TextualConvention):
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
        *(("bgp-l2vpn", 2),
          ("bgpSignalL2vpn", 4),
          ("manual", 1),
          ("multiSegmentPW", 5),
          ("radius", 3),
          ("vplsPmsi", 6))
    )



class ConfigStatus(Integer32, TextualConvention):
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
        *(("created", 1),
          ("deleted", 3),
          ("modified", 2))
    )



class ServAccessLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("spoke", 2))
    )



class ServShcvOperState(Integer32, TextualConvention):
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
        *(("disabled", 1),
          ("down", 3),
          ("undefined", 2),
          ("up", 4))
    )



class TMrpPolicyDefaultAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("block", 1))
    )



class TMrpPolicyAction(Integer32, TextualConvention):
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
        *(("allow", 2),
          ("block", 1),
          ("end-station", 3),
          ("none", 0))
    )



class TmnxSiteId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxServConformance_ObjectIdentity = ObjectIdentity
tmnxServConformance = _TmnxServConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4)
)
_TmnxCustConformance_ObjectIdentity = ObjectIdentity
tmnxCustConformance = _TmnxCustConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1)
)
_TmnxCustCompliances_ObjectIdentity = ObjectIdentity
tmnxCustCompliances = _TmnxCustCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1, 1)
)
_TmnxCustGroups_ObjectIdentity = ObjectIdentity
tmnxCustGroups = _TmnxCustGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1, 2)
)
_TmnxSvcConformance_ObjectIdentity = ObjectIdentity
tmnxSvcConformance = _TmnxSvcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2)
)
_TmnxSvcCompliances_ObjectIdentity = ObjectIdentity
tmnxSvcCompliances = _TmnxSvcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1)
)
_TmnxSvcGroups_ObjectIdentity = ObjectIdentity
tmnxSvcGroups = _TmnxSvcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2)
)
_TmnxTstpConformance_ObjectIdentity = ObjectIdentity
tmnxTstpConformance = _TmnxTstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 5)
)
_TmnxTstpCompliances_ObjectIdentity = ObjectIdentity
tmnxTstpCompliances = _TmnxTstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 5, 1)
)
_TmnxTstpGroups_ObjectIdentity = ObjectIdentity
tmnxTstpGroups = _TmnxTstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 5, 2)
)
_TmnxServObjs_ObjectIdentity = ObjectIdentity
tmnxServObjs = _TmnxServObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4)
)
_TmnxCustObjs_ObjectIdentity = ObjectIdentity
tmnxCustObjs = _TmnxCustObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1)
)
_CustNumEntries_Type = Integer32
_CustNumEntries_Object = MibScalar
custNumEntries = _CustNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 1),
    _CustNumEntries_Type()
)
custNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custNumEntries.setStatus("current")
_CustNextFreeId_Type = TmnxCustId
_CustNextFreeId_Object = MibScalar
custNextFreeId = _CustNextFreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 2),
    _CustNextFreeId_Type()
)
custNextFreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custNextFreeId.setStatus("current")
_CustInfoTable_Object = MibTable
custInfoTable = _CustInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    custInfoTable.setStatus("current")
_CustInfoEntry_Object = MibTableRow
custInfoEntry = _CustInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 3, 1)
)
custInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
)
if mibBuilder.loadTexts:
    custInfoEntry.setStatus("current")
_CustId_Type = TmnxCustId
_CustId_Object = MibTableColumn
custId = _CustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 3, 1, 1),
    _CustId_Type()
)
custId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custId.setStatus("current")
_CustRowStatus_Type = RowStatus
_CustRowStatus_Object = MibTableColumn
custRowStatus = _CustRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 3, 1, 2),
    _CustRowStatus_Type()
)
custRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custRowStatus.setStatus("current")
_CustDescription_Type = ServObjDesc
_CustDescription_Object = MibTableColumn
custDescription = _CustDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 3, 1, 3),
    _CustDescription_Type()
)
custDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custDescription.setStatus("current")
_CustContact_Type = ServObjDesc
_CustContact_Object = MibTableColumn
custContact = _CustContact_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 3, 1, 4),
    _CustContact_Type()
)
custContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custContact.setStatus("current")
_CustPhone_Type = ServObjDesc
_CustPhone_Object = MibTableColumn
custPhone = _CustPhone_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 3, 1, 5),
    _CustPhone_Type()
)
custPhone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custPhone.setStatus("current")
_CustLastMgmtChange_Type = TimeStamp
_CustLastMgmtChange_Object = MibTableColumn
custLastMgmtChange = _CustLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 3, 1, 6),
    _CustLastMgmtChange_Type()
)
custLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custLastMgmtChange.setStatus("current")
_CustMultiServiceSiteTable_Object = MibTable
custMultiServiceSiteTable = _CustMultiServiceSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    custMultiServiceSiteTable.setStatus("current")
_CustMultiServiceSiteEntry_Object = MibTableRow
custMultiServiceSiteEntry = _CustMultiServiceSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1)
)
custMultiServiceSiteEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (1, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
)
if mibBuilder.loadTexts:
    custMultiServiceSiteEntry.setStatus("current")
_CustMultSvcSiteName_Type = TNamedItem
_CustMultSvcSiteName_Object = MibTableColumn
custMultSvcSiteName = _CustMultSvcSiteName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 1),
    _CustMultSvcSiteName_Type()
)
custMultSvcSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMultSvcSiteName.setStatus("current")
_CustMultSvcSiteRowStatus_Type = RowStatus
_CustMultSvcSiteRowStatus_Object = MibTableColumn
custMultSvcSiteRowStatus = _CustMultSvcSiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 2),
    _CustMultSvcSiteRowStatus_Type()
)
custMultSvcSiteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteRowStatus.setStatus("current")
_CustMultSvcSiteDescription_Type = ServObjDesc
_CustMultSvcSiteDescription_Object = MibTableColumn
custMultSvcSiteDescription = _CustMultSvcSiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 3),
    _CustMultSvcSiteDescription_Type()
)
custMultSvcSiteDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteDescription.setStatus("current")


class _CustMultSvcSiteScope_Type(Integer32):
    """Custom type custMultSvcSiteScope based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("card", 2),
          ("port", 1))
    )


_CustMultSvcSiteScope_Type.__name__ = "Integer32"
_CustMultSvcSiteScope_Object = MibTableColumn
custMultSvcSiteScope = _CustMultSvcSiteScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 4),
    _CustMultSvcSiteScope_Type()
)
custMultSvcSiteScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteScope.setStatus("current")


class _CustMultSvcSiteAssignment_Type(Unsigned32):
    """Custom type custMultSvcSiteAssignment based on Unsigned32"""
    defaultValue = 0


_CustMultSvcSiteAssignment_Object = MibTableColumn
custMultSvcSiteAssignment = _CustMultSvcSiteAssignment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 5),
    _CustMultSvcSiteAssignment_Type()
)
custMultSvcSiteAssignment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteAssignment.setStatus("current")
_CustMultSvcSiteIngressSchedulerPolicy_Type = ServObjName
_CustMultSvcSiteIngressSchedulerPolicy_Object = MibTableColumn
custMultSvcSiteIngressSchedulerPolicy = _CustMultSvcSiteIngressSchedulerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 6),
    _CustMultSvcSiteIngressSchedulerPolicy_Type()
)
custMultSvcSiteIngressSchedulerPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteIngressSchedulerPolicy.setStatus("current")
_CustMultSvcSiteEgressSchedulerPolicy_Type = ServObjName
_CustMultSvcSiteEgressSchedulerPolicy_Object = MibTableColumn
custMultSvcSiteEgressSchedulerPolicy = _CustMultSvcSiteEgressSchedulerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 7),
    _CustMultSvcSiteEgressSchedulerPolicy_Type()
)
custMultSvcSiteEgressSchedulerPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteEgressSchedulerPolicy.setStatus("current")
_CustMultSvcSiteLastMgmtChange_Type = TimeStamp
_CustMultSvcSiteLastMgmtChange_Object = MibTableColumn
custMultSvcSiteLastMgmtChange = _CustMultSvcSiteLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 8),
    _CustMultSvcSiteLastMgmtChange_Type()
)
custMultSvcSiteLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMultSvcSiteLastMgmtChange.setStatus("current")


class _CustMultSvcSiteTodSuite_Type(TNamedItemOrEmpty):
    """Custom type custMultSvcSiteTodSuite based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_CustMultSvcSiteTodSuite_Object = MibTableColumn
custMultSvcSiteTodSuite = _CustMultSvcSiteTodSuite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 9),
    _CustMultSvcSiteTodSuite_Type()
)
custMultSvcSiteTodSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteTodSuite.setStatus("current")
_CustMultSvcSiteCurrentIngrSchedPlcy_Type = ServObjName
_CustMultSvcSiteCurrentIngrSchedPlcy_Object = MibTableColumn
custMultSvcSiteCurrentIngrSchedPlcy = _CustMultSvcSiteCurrentIngrSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 10),
    _CustMultSvcSiteCurrentIngrSchedPlcy_Type()
)
custMultSvcSiteCurrentIngrSchedPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMultSvcSiteCurrentIngrSchedPlcy.setStatus("current")
_CustMultSvcSiteCurrentEgrSchedPlcy_Type = ServObjName
_CustMultSvcSiteCurrentEgrSchedPlcy_Object = MibTableColumn
custMultSvcSiteCurrentEgrSchedPlcy = _CustMultSvcSiteCurrentEgrSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 11),
    _CustMultSvcSiteCurrentEgrSchedPlcy_Type()
)
custMultSvcSiteCurrentEgrSchedPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMultSvcSiteCurrentEgrSchedPlcy.setStatus("current")


class _CustMultSvcSiteEgressAggRateLimit_Type(TPortSchedulerPIR):
    """Custom type custMultSvcSiteEgressAggRateLimit based on TPortSchedulerPIR"""
    defaultValue = -1


_CustMultSvcSiteEgressAggRateLimit_Object = MibTableColumn
custMultSvcSiteEgressAggRateLimit = _CustMultSvcSiteEgressAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 12),
    _CustMultSvcSiteEgressAggRateLimit_Type()
)
custMultSvcSiteEgressAggRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteEgressAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    custMultSvcSiteEgressAggRateLimit.setUnits("kbps")
_CustMultSvcSiteIntendedIngrSchedPlcy_Type = ServObjName
_CustMultSvcSiteIntendedIngrSchedPlcy_Object = MibTableColumn
custMultSvcSiteIntendedIngrSchedPlcy = _CustMultSvcSiteIntendedIngrSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 13),
    _CustMultSvcSiteIntendedIngrSchedPlcy_Type()
)
custMultSvcSiteIntendedIngrSchedPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMultSvcSiteIntendedIngrSchedPlcy.setStatus("current")
_CustMultSvcSiteIntendedEgrSchedPlcy_Type = ServObjName
_CustMultSvcSiteIntendedEgrSchedPlcy_Object = MibTableColumn
custMultSvcSiteIntendedEgrSchedPlcy = _CustMultSvcSiteIntendedEgrSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 14),
    _CustMultSvcSiteIntendedEgrSchedPlcy_Type()
)
custMultSvcSiteIntendedEgrSchedPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMultSvcSiteIntendedEgrSchedPlcy.setStatus("current")


class _CustMultSvcSiteFrameBasedAccnt_Type(TruthValue):
    """Custom type custMultSvcSiteFrameBasedAccnt based on TruthValue"""


_CustMultSvcSiteFrameBasedAccnt_Object = MibTableColumn
custMultSvcSiteFrameBasedAccnt = _CustMultSvcSiteFrameBasedAccnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 15),
    _CustMultSvcSiteFrameBasedAccnt_Type()
)
custMultSvcSiteFrameBasedAccnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteFrameBasedAccnt.setStatus("current")


class _CustMultSvcSiteSubscriberMss_Type(TruthValue):
    """Custom type custMultSvcSiteSubscriberMss based on TruthValue"""


_CustMultSvcSiteSubscriberMss_Object = MibTableColumn
custMultSvcSiteSubscriberMss = _CustMultSvcSiteSubscriberMss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 16),
    _CustMultSvcSiteSubscriberMss_Type()
)
custMultSvcSiteSubscriberMss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteSubscriberMss.setStatus("current")
_CustMultSvcSiteIngPolcrCtrlPolcy_Type = TNamedItemOrEmpty
_CustMultSvcSiteIngPolcrCtrlPolcy_Object = MibTableColumn
custMultSvcSiteIngPolcrCtrlPolcy = _CustMultSvcSiteIngPolcrCtrlPolcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 17),
    _CustMultSvcSiteIngPolcrCtrlPolcy_Type()
)
custMultSvcSiteIngPolcrCtrlPolcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteIngPolcrCtrlPolcy.setStatus("current")
_CustMultSvcSiteEgrPolcrCtrlPolcy_Type = TNamedItemOrEmpty
_CustMultSvcSiteEgrPolcrCtrlPolcy_Object = MibTableColumn
custMultSvcSiteEgrPolcrCtrlPolcy = _CustMultSvcSiteEgrPolcrCtrlPolcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 4, 1, 18),
    _CustMultSvcSiteEgrPolcrCtrlPolcy_Type()
)
custMultSvcSiteEgrPolcrCtrlPolcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMultSvcSiteEgrPolcrCtrlPolcy.setStatus("current")
_CustMultiSvcSiteIngStatsTable_Object = MibTable
custMultiSvcSiteIngStatsTable = _CustMultiSvcSiteIngStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    custMultiSvcSiteIngStatsTable.setStatus("current")
_CustMultiSvcSiteIngStatsEntry_Object = MibTableRow
custMultiSvcSiteIngStatsEntry = _CustMultiSvcSiteIngStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 5, 1)
)
custMultiSvcSiteIngStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (1, "TIMETRA-SERV-MIB", "custIngQosSchedName"),
)
if mibBuilder.loadTexts:
    custMultiSvcSiteIngStatsEntry.setStatus("current")
_CustIngQosSchedName_Type = TNamedItem
_CustIngQosSchedName_Object = MibTableColumn
custIngQosSchedName = _CustIngQosSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 5, 1, 1),
    _CustIngQosSchedName_Type()
)
custIngQosSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custIngQosSchedName.setStatus("current")
_CustIngQosSchedStatsForwardedPackets_Type = Counter64
_CustIngQosSchedStatsForwardedPackets_Object = MibTableColumn
custIngQosSchedStatsForwardedPackets = _CustIngQosSchedStatsForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 5, 1, 2),
    _CustIngQosSchedStatsForwardedPackets_Type()
)
custIngQosSchedStatsForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosSchedStatsForwardedPackets.setStatus("current")
_CustIngQosSchedStatsForwardedOctets_Type = Counter64
_CustIngQosSchedStatsForwardedOctets_Object = MibTableColumn
custIngQosSchedStatsForwardedOctets = _CustIngQosSchedStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 5, 1, 3),
    _CustIngQosSchedStatsForwardedOctets_Type()
)
custIngQosSchedStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosSchedStatsForwardedOctets.setStatus("current")
_CustMultiSvcSiteEgrStatsTable_Object = MibTable
custMultiSvcSiteEgrStatsTable = _CustMultiSvcSiteEgrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    custMultiSvcSiteEgrStatsTable.setStatus("current")
_CustMultiSvcSiteEgrStatsEntry_Object = MibTableRow
custMultiSvcSiteEgrStatsEntry = _CustMultiSvcSiteEgrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 6, 1)
)
custMultiSvcSiteEgrStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (1, "TIMETRA-SERV-MIB", "custEgrQosSchedName"),
)
if mibBuilder.loadTexts:
    custMultiSvcSiteEgrStatsEntry.setStatus("current")
_CustEgrQosSchedName_Type = TNamedItem
_CustEgrQosSchedName_Object = MibTableColumn
custEgrQosSchedName = _CustEgrQosSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 6, 1, 1),
    _CustEgrQosSchedName_Type()
)
custEgrQosSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custEgrQosSchedName.setStatus("current")
_CustEgrQosSchedStatsForwardedPackets_Type = Counter64
_CustEgrQosSchedStatsForwardedPackets_Object = MibTableColumn
custEgrQosSchedStatsForwardedPackets = _CustEgrQosSchedStatsForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 6, 1, 2),
    _CustEgrQosSchedStatsForwardedPackets_Type()
)
custEgrQosSchedStatsForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosSchedStatsForwardedPackets.setStatus("current")
_CustEgrQosSchedStatsForwardedOctets_Type = Counter64
_CustEgrQosSchedStatsForwardedOctets_Object = MibTableColumn
custEgrQosSchedStatsForwardedOctets = _CustEgrQosSchedStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 6, 1, 3),
    _CustEgrQosSchedStatsForwardedOctets_Type()
)
custEgrQosSchedStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosSchedStatsForwardedOctets.setStatus("current")
_CustIngQosPortIdSchedStatsTable_Object = MibTable
custIngQosPortIdSchedStatsTable = _CustIngQosPortIdSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 7)
)
if mibBuilder.loadTexts:
    custIngQosPortIdSchedStatsTable.setStatus("current")
_CustIngQosPortIdSchedStatsEntry_Object = MibTableRow
custIngQosPortIdSchedStatsEntry = _CustIngQosPortIdSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 7, 1)
)
custIngQosPortIdSchedStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-SERV-MIB", "custIngQosPortIdSchedName"),
    (0, "TIMETRA-SERV-MIB", "custIngQosAssignmentPortId"),
)
if mibBuilder.loadTexts:
    custIngQosPortIdSchedStatsEntry.setStatus("current")
_CustIngQosPortIdSchedName_Type = TNamedItem
_CustIngQosPortIdSchedName_Object = MibTableColumn
custIngQosPortIdSchedName = _CustIngQosPortIdSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 7, 1, 1),
    _CustIngQosPortIdSchedName_Type()
)
custIngQosPortIdSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custIngQosPortIdSchedName.setStatus("current")
_CustIngQosAssignmentPortId_Type = TmnxPortID
_CustIngQosAssignmentPortId_Object = MibTableColumn
custIngQosAssignmentPortId = _CustIngQosAssignmentPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 7, 1, 2),
    _CustIngQosAssignmentPortId_Type()
)
custIngQosAssignmentPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custIngQosAssignmentPortId.setStatus("current")
_CustIngQosPortSchedFwdPkts_Type = Counter64
_CustIngQosPortSchedFwdPkts_Object = MibTableColumn
custIngQosPortSchedFwdPkts = _CustIngQosPortSchedFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 7, 1, 3),
    _CustIngQosPortSchedFwdPkts_Type()
)
custIngQosPortSchedFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosPortSchedFwdPkts.setStatus("current")
_CustIngQosPortSchedFwdOctets_Type = Counter64
_CustIngQosPortSchedFwdOctets_Object = MibTableColumn
custIngQosPortSchedFwdOctets = _CustIngQosPortSchedFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 7, 1, 4),
    _CustIngQosPortSchedFwdOctets_Type()
)
custIngQosPortSchedFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosPortSchedFwdOctets.setStatus("current")
_CustEgrQosPortIdSchedStatsTable_Object = MibTable
custEgrQosPortIdSchedStatsTable = _CustEgrQosPortIdSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 8)
)
if mibBuilder.loadTexts:
    custEgrQosPortIdSchedStatsTable.setStatus("current")
_CustEgrQosPortIdSchedStatsEntry_Object = MibTableRow
custEgrQosPortIdSchedStatsEntry = _CustEgrQosPortIdSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 8, 1)
)
custEgrQosPortIdSchedStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-SERV-MIB", "custEgrQosPortIdSchedName"),
    (0, "TIMETRA-SERV-MIB", "custEgrQosAssignmentPortId"),
)
if mibBuilder.loadTexts:
    custEgrQosPortIdSchedStatsEntry.setStatus("current")
_CustEgrQosPortIdSchedName_Type = TNamedItem
_CustEgrQosPortIdSchedName_Object = MibTableColumn
custEgrQosPortIdSchedName = _CustEgrQosPortIdSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 8, 1, 1),
    _CustEgrQosPortIdSchedName_Type()
)
custEgrQosPortIdSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custEgrQosPortIdSchedName.setStatus("current")
_CustEgrQosAssignmentPortId_Type = TmnxPortID
_CustEgrQosAssignmentPortId_Object = MibTableColumn
custEgrQosAssignmentPortId = _CustEgrQosAssignmentPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 8, 1, 2),
    _CustEgrQosAssignmentPortId_Type()
)
custEgrQosAssignmentPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custEgrQosAssignmentPortId.setStatus("current")
_CustEgrQosPortSchedFwdPkts_Type = Counter64
_CustEgrQosPortSchedFwdPkts_Object = MibTableColumn
custEgrQosPortSchedFwdPkts = _CustEgrQosPortSchedFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 8, 1, 3),
    _CustEgrQosPortSchedFwdPkts_Type()
)
custEgrQosPortSchedFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosPortSchedFwdPkts.setStatus("current")
_CustEgrQosPortSchedFwdOctets_Type = Counter64
_CustEgrQosPortSchedFwdOctets_Object = MibTableColumn
custEgrQosPortSchedFwdOctets = _CustEgrQosPortSchedFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 8, 1, 4),
    _CustEgrQosPortSchedFwdOctets_Type()
)
custEgrQosPortSchedFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosPortSchedFwdOctets.setStatus("current")
_CustMssIngQosSchedInfoTable_Object = MibTable
custMssIngQosSchedInfoTable = _CustMssIngQosSchedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 9)
)
if mibBuilder.loadTexts:
    custMssIngQosSchedInfoTable.setStatus("current")
_CustMssIngQosSchedInfoEntry_Object = MibTableRow
custMssIngQosSchedInfoEntry = _CustMssIngQosSchedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 9, 1)
)
custMssIngQosSchedInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (1, "TIMETRA-SERV-MIB", "custMssIngQosSName"),
)
if mibBuilder.loadTexts:
    custMssIngQosSchedInfoEntry.setStatus("current")
_CustMssIngQosSName_Type = TNamedItem
_CustMssIngQosSName_Object = MibTableColumn
custMssIngQosSName = _CustMssIngQosSName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 9, 1, 1),
    _CustMssIngQosSName_Type()
)
custMssIngQosSName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custMssIngQosSName.setStatus("current")
_CustMssIngQosSRowStatus_Type = RowStatus
_CustMssIngQosSRowStatus_Object = MibTableColumn
custMssIngQosSRowStatus = _CustMssIngQosSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 9, 1, 2),
    _CustMssIngQosSRowStatus_Type()
)
custMssIngQosSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMssIngQosSRowStatus.setStatus("current")
_CustMssIngQosSLastMgmtChange_Type = TimeStamp
_CustMssIngQosSLastMgmtChange_Object = MibTableColumn
custMssIngQosSLastMgmtChange = _CustMssIngQosSLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 9, 1, 3),
    _CustMssIngQosSLastMgmtChange_Type()
)
custMssIngQosSLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssIngQosSLastMgmtChange.setStatus("current")
_CustMssIngQosSOverrideFlags_Type = TVirtSchedAttribute
_CustMssIngQosSOverrideFlags_Object = MibTableColumn
custMssIngQosSOverrideFlags = _CustMssIngQosSOverrideFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 9, 1, 4),
    _CustMssIngQosSOverrideFlags_Type()
)
custMssIngQosSOverrideFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMssIngQosSOverrideFlags.setStatus("current")


class _CustMssIngQosSPIR_Type(THPolVirtualSchePIRRate):
    """Custom type custMssIngQosSPIR based on THPolVirtualSchePIRRate"""
    defaultValue = -1


_CustMssIngQosSPIR_Object = MibTableColumn
custMssIngQosSPIR = _CustMssIngQosSPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 9, 1, 5),
    _CustMssIngQosSPIR_Type()
)
custMssIngQosSPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMssIngQosSPIR.setStatus("current")
if mibBuilder.loadTexts:
    custMssIngQosSPIR.setUnits("kilo bits per second")


class _CustMssIngQosSCIR_Type(THPolVirtualScheCIRRate):
    """Custom type custMssIngQosSCIR based on THPolVirtualScheCIRRate"""
    defaultValue = 0


_CustMssIngQosSCIR_Object = MibTableColumn
custMssIngQosSCIR = _CustMssIngQosSCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 9, 1, 6),
    _CustMssIngQosSCIR_Type()
)
custMssIngQosSCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMssIngQosSCIR.setStatus("current")
if mibBuilder.loadTexts:
    custMssIngQosSCIR.setUnits("kilo bits per second")


class _CustMssIngQosSSummedCIR_Type(TruthValue):
    """Custom type custMssIngQosSSummedCIR based on TruthValue"""


_CustMssIngQosSSummedCIR_Object = MibTableColumn
custMssIngQosSSummedCIR = _CustMssIngQosSSummedCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 9, 1, 7),
    _CustMssIngQosSSummedCIR_Type()
)
custMssIngQosSSummedCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMssIngQosSSummedCIR.setStatus("current")
_CustMssEgrQosSchedInfoTable_Object = MibTable
custMssEgrQosSchedInfoTable = _CustMssEgrQosSchedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 10)
)
if mibBuilder.loadTexts:
    custMssEgrQosSchedInfoTable.setStatus("current")
_CustMssEgrQosSchedInfoEntry_Object = MibTableRow
custMssEgrQosSchedInfoEntry = _CustMssEgrQosSchedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 10, 1)
)
custMssEgrQosSchedInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (1, "TIMETRA-SERV-MIB", "custMssEgrQosSName"),
)
if mibBuilder.loadTexts:
    custMssEgrQosSchedInfoEntry.setStatus("current")
_CustMssEgrQosSName_Type = TNamedItem
_CustMssEgrQosSName_Object = MibTableColumn
custMssEgrQosSName = _CustMssEgrQosSName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 10, 1, 1),
    _CustMssEgrQosSName_Type()
)
custMssEgrQosSName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custMssEgrQosSName.setStatus("current")
_CustMssEgrQosSRowStatus_Type = RowStatus
_CustMssEgrQosSRowStatus_Object = MibTableColumn
custMssEgrQosSRowStatus = _CustMssEgrQosSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 10, 1, 2),
    _CustMssEgrQosSRowStatus_Type()
)
custMssEgrQosSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMssEgrQosSRowStatus.setStatus("current")
_CustMssEgrQosSLastMgmtChange_Type = TimeStamp
_CustMssEgrQosSLastMgmtChange_Object = MibTableColumn
custMssEgrQosSLastMgmtChange = _CustMssEgrQosSLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 10, 1, 3),
    _CustMssEgrQosSLastMgmtChange_Type()
)
custMssEgrQosSLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssEgrQosSLastMgmtChange.setStatus("current")
_CustMssEgrQosSOverrideFlags_Type = TVirtSchedAttribute
_CustMssEgrQosSOverrideFlags_Object = MibTableColumn
custMssEgrQosSOverrideFlags = _CustMssEgrQosSOverrideFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 10, 1, 4),
    _CustMssEgrQosSOverrideFlags_Type()
)
custMssEgrQosSOverrideFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMssEgrQosSOverrideFlags.setStatus("current")


class _CustMssEgrQosSPIR_Type(THPolVirtualSchePIRRate):
    """Custom type custMssEgrQosSPIR based on THPolVirtualSchePIRRate"""
    defaultValue = -1


_CustMssEgrQosSPIR_Object = MibTableColumn
custMssEgrQosSPIR = _CustMssEgrQosSPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 10, 1, 5),
    _CustMssEgrQosSPIR_Type()
)
custMssEgrQosSPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMssEgrQosSPIR.setStatus("current")
if mibBuilder.loadTexts:
    custMssEgrQosSPIR.setUnits("kilo bits per second")


class _CustMssEgrQosSCIR_Type(THPolVirtualScheCIRRate):
    """Custom type custMssEgrQosSCIR based on THPolVirtualScheCIRRate"""
    defaultValue = 0


_CustMssEgrQosSCIR_Object = MibTableColumn
custMssEgrQosSCIR = _CustMssEgrQosSCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 10, 1, 6),
    _CustMssEgrQosSCIR_Type()
)
custMssEgrQosSCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMssEgrQosSCIR.setStatus("current")
if mibBuilder.loadTexts:
    custMssEgrQosSCIR.setUnits("kilo bits per second")


class _CustMssEgrQosSSummedCIR_Type(TruthValue):
    """Custom type custMssEgrQosSSummedCIR based on TruthValue"""


_CustMssEgrQosSSummedCIR_Object = MibTableColumn
custMssEgrQosSSummedCIR = _CustMssEgrQosSSummedCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 10, 1, 7),
    _CustMssEgrQosSSummedCIR_Type()
)
custMssEgrQosSSummedCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    custMssEgrQosSSummedCIR.setStatus("current")
_CustMultiSvcSiteIngSchedPlcyStatsTable_Object = MibTable
custMultiSvcSiteIngSchedPlcyStatsTable = _CustMultiSvcSiteIngSchedPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 11)
)
if mibBuilder.loadTexts:
    custMultiSvcSiteIngSchedPlcyStatsTable.setStatus("current")
_CustMultiSvcSiteIngSchedPlcyStatsEntry_Object = MibTableRow
custMultiSvcSiteIngSchedPlcyStatsEntry = _CustMultiSvcSiteIngSchedPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 11, 1)
)
custMultiSvcSiteIngSchedPlcyStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (1, "TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
)
if mibBuilder.loadTexts:
    custMultiSvcSiteIngSchedPlcyStatsEntry.setStatus("current")
_CustIngSchedPlcyStatsFwdPkt_Type = Counter64
_CustIngSchedPlcyStatsFwdPkt_Object = MibTableColumn
custIngSchedPlcyStatsFwdPkt = _CustIngSchedPlcyStatsFwdPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 11, 1, 1),
    _CustIngSchedPlcyStatsFwdPkt_Type()
)
custIngSchedPlcyStatsFwdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngSchedPlcyStatsFwdPkt.setStatus("current")
_CustIngSchedPlcyStatsFwdOct_Type = Counter64
_CustIngSchedPlcyStatsFwdOct_Object = MibTableColumn
custIngSchedPlcyStatsFwdOct = _CustIngSchedPlcyStatsFwdOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 11, 1, 2),
    _CustIngSchedPlcyStatsFwdOct_Type()
)
custIngSchedPlcyStatsFwdOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngSchedPlcyStatsFwdOct.setStatus("current")
_CustMultiSvcSiteEgrSchedPlcyStatsTable_Object = MibTable
custMultiSvcSiteEgrSchedPlcyStatsTable = _CustMultiSvcSiteEgrSchedPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 12)
)
if mibBuilder.loadTexts:
    custMultiSvcSiteEgrSchedPlcyStatsTable.setStatus("current")
_CustMultiSvcSiteEgrSchedPlcyStatsEntry_Object = MibTableRow
custMultiSvcSiteEgrSchedPlcyStatsEntry = _CustMultiSvcSiteEgrSchedPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 12, 1)
)
custMultiSvcSiteEgrSchedPlcyStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (1, "TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
)
if mibBuilder.loadTexts:
    custMultiSvcSiteEgrSchedPlcyStatsEntry.setStatus("current")
_CustEgrSchedPlcyStatsFwdPkt_Type = Counter64
_CustEgrSchedPlcyStatsFwdPkt_Object = MibTableColumn
custEgrSchedPlcyStatsFwdPkt = _CustEgrSchedPlcyStatsFwdPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 12, 1, 1),
    _CustEgrSchedPlcyStatsFwdPkt_Type()
)
custEgrSchedPlcyStatsFwdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrSchedPlcyStatsFwdPkt.setStatus("current")
_CustEgrSchedPlcyStatsFwdOct_Type = Counter64
_CustEgrSchedPlcyStatsFwdOct_Object = MibTableColumn
custEgrSchedPlcyStatsFwdOct = _CustEgrSchedPlcyStatsFwdOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 12, 1, 2),
    _CustEgrSchedPlcyStatsFwdOct_Type()
)
custEgrSchedPlcyStatsFwdOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrSchedPlcyStatsFwdOct.setStatus("current")
_CustMultiSvcSiteIngSchedPlcyPortStatsTable_Object = MibTable
custMultiSvcSiteIngSchedPlcyPortStatsTable = _CustMultiSvcSiteIngSchedPlcyPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 13)
)
if mibBuilder.loadTexts:
    custMultiSvcSiteIngSchedPlcyPortStatsTable.setStatus("current")
_CustMultiSvcSiteIngSchedPlcyPortStatsEntry_Object = MibTableRow
custMultiSvcSiteIngSchedPlcyPortStatsEntry = _CustMultiSvcSiteIngSchedPlcyPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 13, 1)
)
custMultiSvcSiteIngSchedPlcyPortStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (0, "TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
    (0, "TIMETRA-SERV-MIB", "custIngSchedPlcyPortStatsPort"),
)
if mibBuilder.loadTexts:
    custMultiSvcSiteIngSchedPlcyPortStatsEntry.setStatus("current")
_CustIngSchedPlcyPortStatsPort_Type = TmnxPortID
_CustIngSchedPlcyPortStatsPort_Object = MibTableColumn
custIngSchedPlcyPortStatsPort = _CustIngSchedPlcyPortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 13, 1, 1),
    _CustIngSchedPlcyPortStatsPort_Type()
)
custIngSchedPlcyPortStatsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custIngSchedPlcyPortStatsPort.setStatus("current")
_CustIngSchedPlcyPortStatsFwdPkt_Type = Counter64
_CustIngSchedPlcyPortStatsFwdPkt_Object = MibTableColumn
custIngSchedPlcyPortStatsFwdPkt = _CustIngSchedPlcyPortStatsFwdPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 13, 1, 2),
    _CustIngSchedPlcyPortStatsFwdPkt_Type()
)
custIngSchedPlcyPortStatsFwdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngSchedPlcyPortStatsFwdPkt.setStatus("current")
_CustIngSchedPlcyPortStatsFwdOct_Type = Counter64
_CustIngSchedPlcyPortStatsFwdOct_Object = MibTableColumn
custIngSchedPlcyPortStatsFwdOct = _CustIngSchedPlcyPortStatsFwdOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 13, 1, 3),
    _CustIngSchedPlcyPortStatsFwdOct_Type()
)
custIngSchedPlcyPortStatsFwdOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngSchedPlcyPortStatsFwdOct.setStatus("current")
_CustMultiSvcSiteEgrSchedPlcyPortStatsTable_Object = MibTable
custMultiSvcSiteEgrSchedPlcyPortStatsTable = _CustMultiSvcSiteEgrSchedPlcyPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 14)
)
if mibBuilder.loadTexts:
    custMultiSvcSiteEgrSchedPlcyPortStatsTable.setStatus("current")
_CustMultiSvcSiteEgrSchedPlcyPortStatsEntry_Object = MibTableRow
custMultiSvcSiteEgrSchedPlcyPortStatsEntry = _CustMultiSvcSiteEgrSchedPlcyPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 14, 1)
)
custMultiSvcSiteEgrSchedPlcyPortStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (0, "TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
    (0, "TIMETRA-SERV-MIB", "custEgrSchedPlcyPortStatsPort"),
)
if mibBuilder.loadTexts:
    custMultiSvcSiteEgrSchedPlcyPortStatsEntry.setStatus("current")
_CustEgrSchedPlcyPortStatsPort_Type = TmnxPortID
_CustEgrSchedPlcyPortStatsPort_Object = MibTableColumn
custEgrSchedPlcyPortStatsPort = _CustEgrSchedPlcyPortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 14, 1, 1),
    _CustEgrSchedPlcyPortStatsPort_Type()
)
custEgrSchedPlcyPortStatsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custEgrSchedPlcyPortStatsPort.setStatus("current")
_CustEgrSchedPlcyPortStatsFwdPkt_Type = Counter64
_CustEgrSchedPlcyPortStatsFwdPkt_Object = MibTableColumn
custEgrSchedPlcyPortStatsFwdPkt = _CustEgrSchedPlcyPortStatsFwdPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 14, 1, 2),
    _CustEgrSchedPlcyPortStatsFwdPkt_Type()
)
custEgrSchedPlcyPortStatsFwdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrSchedPlcyPortStatsFwdPkt.setStatus("current")
_CustEgrSchedPlcyPortStatsFwdOct_Type = Counter64
_CustEgrSchedPlcyPortStatsFwdOct_Object = MibTableColumn
custEgrSchedPlcyPortStatsFwdOct = _CustEgrSchedPlcyPortStatsFwdOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 14, 1, 3),
    _CustEgrSchedPlcyPortStatsFwdOct_Type()
)
custEgrSchedPlcyPortStatsFwdOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrSchedPlcyPortStatsFwdOct.setStatus("current")
_CustMssIngQosArbitStatsTable_Object = MibTable
custMssIngQosArbitStatsTable = _CustMssIngQosArbitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 15)
)
if mibBuilder.loadTexts:
    custMssIngQosArbitStatsTable.setStatus("current")
_CustMssIngQosArbitStatsEntry_Object = MibTableRow
custMssIngQosArbitStatsEntry = _CustMssIngQosArbitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 15, 1)
)
custMssIngQosArbitStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-SERV-MIB", "custMssIngQosArbitName"),
)
if mibBuilder.loadTexts:
    custMssIngQosArbitStatsEntry.setStatus("current")
_CustMssIngQosArbitName_Type = TNamedItem
_CustMssIngQosArbitName_Object = MibTableColumn
custMssIngQosArbitName = _CustMssIngQosArbitName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 15, 1, 1),
    _CustMssIngQosArbitName_Type()
)
custMssIngQosArbitName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custMssIngQosArbitName.setStatus("current")
_CustMssIngQosArbitStatsFwdPkts_Type = Counter64
_CustMssIngQosArbitStatsFwdPkts_Object = MibTableColumn
custMssIngQosArbitStatsFwdPkts = _CustMssIngQosArbitStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 15, 1, 2),
    _CustMssIngQosArbitStatsFwdPkts_Type()
)
custMssIngQosArbitStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssIngQosArbitStatsFwdPkts.setStatus("current")
_CustMssIngQosArbitStatsFwdPktsLo_Type = Counter32
_CustMssIngQosArbitStatsFwdPktsLo_Object = MibTableColumn
custMssIngQosArbitStatsFwdPktsLo = _CustMssIngQosArbitStatsFwdPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 15, 1, 3),
    _CustMssIngQosArbitStatsFwdPktsLo_Type()
)
custMssIngQosArbitStatsFwdPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssIngQosArbitStatsFwdPktsLo.setStatus("current")
_CustMssIngQosArbitStatsFwdPktsHi_Type = Counter32
_CustMssIngQosArbitStatsFwdPktsHi_Object = MibTableColumn
custMssIngQosArbitStatsFwdPktsHi = _CustMssIngQosArbitStatsFwdPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 15, 1, 4),
    _CustMssIngQosArbitStatsFwdPktsHi_Type()
)
custMssIngQosArbitStatsFwdPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssIngQosArbitStatsFwdPktsHi.setStatus("current")
_CustMssIngQosArbitStatsFwdOcts_Type = Counter64
_CustMssIngQosArbitStatsFwdOcts_Object = MibTableColumn
custMssIngQosArbitStatsFwdOcts = _CustMssIngQosArbitStatsFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 15, 1, 5),
    _CustMssIngQosArbitStatsFwdOcts_Type()
)
custMssIngQosArbitStatsFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssIngQosArbitStatsFwdOcts.setStatus("current")
_CustMssIngQosArbitStatsFwdOctsLo_Type = Counter32
_CustMssIngQosArbitStatsFwdOctsLo_Object = MibTableColumn
custMssIngQosArbitStatsFwdOctsLo = _CustMssIngQosArbitStatsFwdOctsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 15, 1, 6),
    _CustMssIngQosArbitStatsFwdOctsLo_Type()
)
custMssIngQosArbitStatsFwdOctsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssIngQosArbitStatsFwdOctsLo.setStatus("current")
_CustMssIngQosArbitStatsFwdOctsHi_Type = Counter32
_CustMssIngQosArbitStatsFwdOctsHi_Object = MibTableColumn
custMssIngQosArbitStatsFwdOctsHi = _CustMssIngQosArbitStatsFwdOctsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 15, 1, 7),
    _CustMssIngQosArbitStatsFwdOctsHi_Type()
)
custMssIngQosArbitStatsFwdOctsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssIngQosArbitStatsFwdOctsHi.setStatus("current")
_CustMssEgrQosArbitStatsTable_Object = MibTable
custMssEgrQosArbitStatsTable = _CustMssEgrQosArbitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 16)
)
if mibBuilder.loadTexts:
    custMssEgrQosArbitStatsTable.setStatus("current")
_CustMssEgrQosArbitStatsEntry_Object = MibTableRow
custMssEgrQosArbitStatsEntry = _CustMssEgrQosArbitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 16, 1)
)
custMssEgrQosArbitStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-SERV-MIB", "custMssEgrQosArbitName"),
)
if mibBuilder.loadTexts:
    custMssEgrQosArbitStatsEntry.setStatus("current")
_CustMssEgrQosArbitName_Type = TNamedItem
_CustMssEgrQosArbitName_Object = MibTableColumn
custMssEgrQosArbitName = _CustMssEgrQosArbitName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 16, 1, 1),
    _CustMssEgrQosArbitName_Type()
)
custMssEgrQosArbitName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custMssEgrQosArbitName.setStatus("current")
_CustMssEgrQosArbitStatsFwdPkts_Type = Counter64
_CustMssEgrQosArbitStatsFwdPkts_Object = MibTableColumn
custMssEgrQosArbitStatsFwdPkts = _CustMssEgrQosArbitStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 16, 1, 2),
    _CustMssEgrQosArbitStatsFwdPkts_Type()
)
custMssEgrQosArbitStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssEgrQosArbitStatsFwdPkts.setStatus("current")
_CustMssEgrQosArbitStatsFwdPktsLo_Type = Counter32
_CustMssEgrQosArbitStatsFwdPktsLo_Object = MibTableColumn
custMssEgrQosArbitStatsFwdPktsLo = _CustMssEgrQosArbitStatsFwdPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 16, 1, 3),
    _CustMssEgrQosArbitStatsFwdPktsLo_Type()
)
custMssEgrQosArbitStatsFwdPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssEgrQosArbitStatsFwdPktsLo.setStatus("current")
_CustMssEgrQosArbitStatsFwdPktsHi_Type = Counter32
_CustMssEgrQosArbitStatsFwdPktsHi_Object = MibTableColumn
custMssEgrQosArbitStatsFwdPktsHi = _CustMssEgrQosArbitStatsFwdPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 16, 1, 4),
    _CustMssEgrQosArbitStatsFwdPktsHi_Type()
)
custMssEgrQosArbitStatsFwdPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssEgrQosArbitStatsFwdPktsHi.setStatus("current")
_CustMssEgrQosArbitStatsFwdOcts_Type = Counter64
_CustMssEgrQosArbitStatsFwdOcts_Object = MibTableColumn
custMssEgrQosArbitStatsFwdOcts = _CustMssEgrQosArbitStatsFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 16, 1, 5),
    _CustMssEgrQosArbitStatsFwdOcts_Type()
)
custMssEgrQosArbitStatsFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssEgrQosArbitStatsFwdOcts.setStatus("current")
_CustMssEgrQosArbitStatsFwdOctsLo_Type = Counter32
_CustMssEgrQosArbitStatsFwdOctsLo_Object = MibTableColumn
custMssEgrQosArbitStatsFwdOctsLo = _CustMssEgrQosArbitStatsFwdOctsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 16, 1, 6),
    _CustMssEgrQosArbitStatsFwdOctsLo_Type()
)
custMssEgrQosArbitStatsFwdOctsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssEgrQosArbitStatsFwdOctsLo.setStatus("current")
_CustMssEgrQosArbitStatsFwdOctsHi_Type = Counter32
_CustMssEgrQosArbitStatsFwdOctsHi_Object = MibTableColumn
custMssEgrQosArbitStatsFwdOctsHi = _CustMssEgrQosArbitStatsFwdOctsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 16, 1, 7),
    _CustMssEgrQosArbitStatsFwdOctsHi_Type()
)
custMssEgrQosArbitStatsFwdOctsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custMssEgrQosArbitStatsFwdOctsHi.setStatus("current")
_CustIngQosPortIdArbitStatsTable_Object = MibTable
custIngQosPortIdArbitStatsTable = _CustIngQosPortIdArbitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 17)
)
if mibBuilder.loadTexts:
    custIngQosPortIdArbitStatsTable.setStatus("current")
_CustIngQosPortIdArbitStatsEntry_Object = MibTableRow
custIngQosPortIdArbitStatsEntry = _CustIngQosPortIdArbitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 17, 1)
)
custIngQosPortIdArbitStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-SERV-MIB", "custIngQosPortIdArbitName"),
    (0, "TIMETRA-SERV-MIB", "custIngQosAssignmentPortId"),
)
if mibBuilder.loadTexts:
    custIngQosPortIdArbitStatsEntry.setStatus("current")
_CustIngQosPortIdArbitName_Type = TNamedItem
_CustIngQosPortIdArbitName_Object = MibTableColumn
custIngQosPortIdArbitName = _CustIngQosPortIdArbitName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 17, 1, 1),
    _CustIngQosPortIdArbitName_Type()
)
custIngQosPortIdArbitName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custIngQosPortIdArbitName.setStatus("current")
_CustIngQosPortIdArbitFwdPkts_Type = Counter64
_CustIngQosPortIdArbitFwdPkts_Object = MibTableColumn
custIngQosPortIdArbitFwdPkts = _CustIngQosPortIdArbitFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 17, 1, 2),
    _CustIngQosPortIdArbitFwdPkts_Type()
)
custIngQosPortIdArbitFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosPortIdArbitFwdPkts.setStatus("current")
_CustIngQosPortIdArbitFwdPktsLo_Type = Counter32
_CustIngQosPortIdArbitFwdPktsLo_Object = MibTableColumn
custIngQosPortIdArbitFwdPktsLo = _CustIngQosPortIdArbitFwdPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 17, 1, 3),
    _CustIngQosPortIdArbitFwdPktsLo_Type()
)
custIngQosPortIdArbitFwdPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosPortIdArbitFwdPktsLo.setStatus("current")
_CustIngQosPortIdArbitFwdPktsHi_Type = Counter32
_CustIngQosPortIdArbitFwdPktsHi_Object = MibTableColumn
custIngQosPortIdArbitFwdPktsHi = _CustIngQosPortIdArbitFwdPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 17, 1, 4),
    _CustIngQosPortIdArbitFwdPktsHi_Type()
)
custIngQosPortIdArbitFwdPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosPortIdArbitFwdPktsHi.setStatus("current")
_CustIngQosPortIdArbitFwdOcts_Type = Counter64
_CustIngQosPortIdArbitFwdOcts_Object = MibTableColumn
custIngQosPortIdArbitFwdOcts = _CustIngQosPortIdArbitFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 17, 1, 5),
    _CustIngQosPortIdArbitFwdOcts_Type()
)
custIngQosPortIdArbitFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosPortIdArbitFwdOcts.setStatus("current")
_CustIngQosPortIdArbitFwdOctsLo_Type = Counter32
_CustIngQosPortIdArbitFwdOctsLo_Object = MibTableColumn
custIngQosPortIdArbitFwdOctsLo = _CustIngQosPortIdArbitFwdOctsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 17, 1, 6),
    _CustIngQosPortIdArbitFwdOctsLo_Type()
)
custIngQosPortIdArbitFwdOctsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosPortIdArbitFwdOctsLo.setStatus("current")
_CustIngQosPortIdArbitFwdOctsHi_Type = Counter32
_CustIngQosPortIdArbitFwdOctsHi_Object = MibTableColumn
custIngQosPortIdArbitFwdOctsHi = _CustIngQosPortIdArbitFwdOctsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 17, 1, 7),
    _CustIngQosPortIdArbitFwdOctsHi_Type()
)
custIngQosPortIdArbitFwdOctsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custIngQosPortIdArbitFwdOctsHi.setStatus("current")
_CustEgrQosPortIdArbitStatsTable_Object = MibTable
custEgrQosPortIdArbitStatsTable = _CustEgrQosPortIdArbitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 18)
)
if mibBuilder.loadTexts:
    custEgrQosPortIdArbitStatsTable.setStatus("current")
_CustEgrQosPortIdArbitStatsEntry_Object = MibTableRow
custEgrQosPortIdArbitStatsEntry = _CustEgrQosPortIdArbitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 18, 1)
)
custEgrQosPortIdArbitStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "custId"),
    (0, "TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "TIMETRA-SERV-MIB", "custEgrQosPortIdArbitName"),
    (0, "TIMETRA-SERV-MIB", "custEgrQosAssignmentPortId"),
)
if mibBuilder.loadTexts:
    custEgrQosPortIdArbitStatsEntry.setStatus("current")
_CustEgrQosPortIdArbitName_Type = TNamedItem
_CustEgrQosPortIdArbitName_Object = MibTableColumn
custEgrQosPortIdArbitName = _CustEgrQosPortIdArbitName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 18, 1, 1),
    _CustEgrQosPortIdArbitName_Type()
)
custEgrQosPortIdArbitName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    custEgrQosPortIdArbitName.setStatus("current")
_CustEgrQosPortIdArbitFwdPkts_Type = Counter64
_CustEgrQosPortIdArbitFwdPkts_Object = MibTableColumn
custEgrQosPortIdArbitFwdPkts = _CustEgrQosPortIdArbitFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 18, 1, 2),
    _CustEgrQosPortIdArbitFwdPkts_Type()
)
custEgrQosPortIdArbitFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosPortIdArbitFwdPkts.setStatus("current")
_CustEgrQosPortIdArbitFwdPktsLo_Type = Counter32
_CustEgrQosPortIdArbitFwdPktsLo_Object = MibTableColumn
custEgrQosPortIdArbitFwdPktsLo = _CustEgrQosPortIdArbitFwdPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 18, 1, 3),
    _CustEgrQosPortIdArbitFwdPktsLo_Type()
)
custEgrQosPortIdArbitFwdPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosPortIdArbitFwdPktsLo.setStatus("current")
_CustEgrQosPortIdArbitFwdPktsHi_Type = Counter32
_CustEgrQosPortIdArbitFwdPktsHi_Object = MibTableColumn
custEgrQosPortIdArbitFwdPktsHi = _CustEgrQosPortIdArbitFwdPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 18, 1, 4),
    _CustEgrQosPortIdArbitFwdPktsHi_Type()
)
custEgrQosPortIdArbitFwdPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosPortIdArbitFwdPktsHi.setStatus("current")
_CustEgrQosPortIdArbitFwdOcts_Type = Counter64
_CustEgrQosPortIdArbitFwdOcts_Object = MibTableColumn
custEgrQosPortIdArbitFwdOcts = _CustEgrQosPortIdArbitFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 18, 1, 5),
    _CustEgrQosPortIdArbitFwdOcts_Type()
)
custEgrQosPortIdArbitFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosPortIdArbitFwdOcts.setStatus("current")
_CustEgrQosPortIdArbitFwdOctsLo_Type = Counter32
_CustEgrQosPortIdArbitFwdOctsLo_Object = MibTableColumn
custEgrQosPortIdArbitFwdOctsLo = _CustEgrQosPortIdArbitFwdOctsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 18, 1, 6),
    _CustEgrQosPortIdArbitFwdOctsLo_Type()
)
custEgrQosPortIdArbitFwdOctsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosPortIdArbitFwdOctsLo.setStatus("current")
_CustEgrQosPortIdArbitFwdOctsHi_Type = Counter32
_CustEgrQosPortIdArbitFwdOctsHi_Object = MibTableColumn
custEgrQosPortIdArbitFwdOctsHi = _CustEgrQosPortIdArbitFwdOctsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 1, 18, 1, 7),
    _CustEgrQosPortIdArbitFwdOctsHi_Type()
)
custEgrQosPortIdArbitFwdOctsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    custEgrQosPortIdArbitFwdOctsHi.setStatus("current")
_TmnxSvcObjs_ObjectIdentity = ObjectIdentity
tmnxSvcObjs = _TmnxSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2)
)
_SvcNumEntries_Type = Integer32
_SvcNumEntries_Object = MibScalar
svcNumEntries = _SvcNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 1),
    _SvcNumEntries_Type()
)
svcNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNumEntries.setStatus("current")
_SvcBaseInfoTable_Object = MibTable
svcBaseInfoTable = _SvcBaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    svcBaseInfoTable.setStatus("current")
_SvcBaseInfoEntry_Object = MibTableRow
svcBaseInfoEntry = _SvcBaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1)
)
svcBaseInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcBaseInfoEntry.setStatus("current")
_SvcId_Type = TmnxServId
_SvcId_Object = MibTableColumn
svcId = _SvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 1),
    _SvcId_Type()
)
svcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcId.setStatus("current")
_SvcRowStatus_Type = RowStatus
_SvcRowStatus_Object = MibTableColumn
svcRowStatus = _SvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 2),
    _SvcRowStatus_Type()
)
svcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcRowStatus.setStatus("current")
_SvcType_Type = ServType
_SvcType_Object = MibTableColumn
svcType = _SvcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 3),
    _SvcType_Type()
)
svcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcType.setStatus("current")
_SvcCustId_Type = TmnxCustId
_SvcCustId_Object = MibTableColumn
svcCustId = _SvcCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 4),
    _SvcCustId_Type()
)
svcCustId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcCustId.setStatus("current")
_SvcIpRouting_Type = TmnxEnabledDisabled
_SvcIpRouting_Object = MibTableColumn
svcIpRouting = _SvcIpRouting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 5),
    _SvcIpRouting_Type()
)
svcIpRouting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcIpRouting.setStatus("current")
_SvcDescription_Type = ServObjDesc
_SvcDescription_Object = MibTableColumn
svcDescription = _SvcDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 6),
    _SvcDescription_Type()
)
svcDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcDescription.setStatus("current")


class _SvcMtu_Type(Integer32):
    """Custom type svcMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9194),
    )


_SvcMtu_Type.__name__ = "Integer32"
_SvcMtu_Object = MibTableColumn
svcMtu = _SvcMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 7),
    _SvcMtu_Type()
)
svcMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMtu.setStatus("current")


class _SvcAdminStatus_Type(ServiceAdminStatus):
    """Custom type svcAdminStatus based on ServiceAdminStatus"""


_SvcAdminStatus_Object = MibTableColumn
svcAdminStatus = _SvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 8),
    _SvcAdminStatus_Type()
)
svcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcAdminStatus.setStatus("current")
_SvcOperStatus_Type = ServiceOperStatus
_SvcOperStatus_Object = MibTableColumn
svcOperStatus = _SvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 9),
    _SvcOperStatus_Type()
)
svcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcOperStatus.setStatus("current")
_SvcNumSaps_Type = Integer32
_SvcNumSaps_Object = MibTableColumn
svcNumSaps = _SvcNumSaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 10),
    _SvcNumSaps_Type()
)
svcNumSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNumSaps.setStatus("current")
_SvcNumSdps_Type = Integer32
_SvcNumSdps_Object = MibTableColumn
svcNumSdps = _SvcNumSdps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 11),
    _SvcNumSdps_Type()
)
svcNumSdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNumSdps.setStatus("current")
_SvcLastMgmtChange_Type = TimeStamp
_SvcLastMgmtChange_Object = MibTableColumn
svcLastMgmtChange = _SvcLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 12),
    _SvcLastMgmtChange_Type()
)
svcLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcLastMgmtChange.setStatus("current")
_SvcDefMeshVcId_Type = Unsigned32
_SvcDefMeshVcId_Object = MibTableColumn
svcDefMeshVcId = _SvcDefMeshVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 13),
    _SvcDefMeshVcId_Type()
)
svcDefMeshVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcDefMeshVcId.setStatus("current")


class _SvcVpnId_Type(VpnId):
    """Custom type svcVpnId based on VpnId"""
    defaultValue = 0


_SvcVpnId_Object = MibTableColumn
svcVpnId = _SvcVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 14),
    _SvcVpnId_Type()
)
svcVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVpnId.setStatus("current")


class _SvcVRouterId_Type(TmnxVRtrIDOrZero):
    """Custom type svcVRouterId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_SvcVRouterId_Object = MibTableColumn
svcVRouterId = _SvcVRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 15),
    _SvcVRouterId_Type()
)
svcVRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVRouterId.setStatus("current")


class _SvcAutoBind_Type(Integer32):
    """Custom type svcAutoBind based on Integer32"""
    defaultValue = 1

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
        *(("gre", 2),
          ("ldp", 3),
          ("mpls", 5),
          ("none", 1),
          ("rsvp-te", 4))
    )


_SvcAutoBind_Type.__name__ = "Integer32"
_SvcAutoBind_Object = MibTableColumn
svcAutoBind = _SvcAutoBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 16),
    _SvcAutoBind_Type()
)
svcAutoBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcAutoBind.setStatus("current")
_SvcLastStatusChange_Type = TimeStamp
_SvcLastStatusChange_Object = MibTableColumn
svcLastStatusChange = _SvcLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 17),
    _SvcLastStatusChange_Type()
)
svcLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcLastStatusChange.setStatus("current")


class _SvcVllType_Type(Integer32):
    """Custom type svcVllType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              8,
              9,
              10,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("atmCell", 7),
          ("atmSdu", 6),
          ("atmVcc", 8),
          ("atmVpc", 9),
          ("cesopsn", 16),
          ("cesopsnCas", 17),
          ("frDlci", 10),
          ("satopE1", 12),
          ("satopE3", 14),
          ("satopT1", 13),
          ("satopT3", 15),
          ("undef", 1))
    )


_SvcVllType_Type.__name__ = "Integer32"
_SvcVllType_Object = MibTableColumn
svcVllType = _SvcVllType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 18),
    _SvcVllType_Type()
)
svcVllType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllType.setStatus("current")


class _SvcMgmtVpls_Type(TruthValue):
    """Custom type svcMgmtVpls based on TruthValue"""


_SvcMgmtVpls_Object = MibTableColumn
svcMgmtVpls = _SvcMgmtVpls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 19),
    _SvcMgmtVpls_Type()
)
svcMgmtVpls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMgmtVpls.setStatus("current")


class _SvcRadiusDiscovery_Type(TruthValue):
    """Custom type svcRadiusDiscovery based on TruthValue"""


_SvcRadiusDiscovery_Object = MibTableColumn
svcRadiusDiscovery = _SvcRadiusDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 20),
    _SvcRadiusDiscovery_Type()
)
svcRadiusDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcRadiusDiscovery.setStatus("current")


class _SvcRadiusUserNameType_Type(Integer32):
    """Custom type svcRadiusUserNameType based on Integer32"""
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
        *(("none", 0),
          ("router-distinguisher", 2),
          ("vpn-id", 1))
    )


_SvcRadiusUserNameType_Type.__name__ = "Integer32"
_SvcRadiusUserNameType_Object = MibTableColumn
svcRadiusUserNameType = _SvcRadiusUserNameType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 21),
    _SvcRadiusUserNameType_Type()
)
svcRadiusUserNameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcRadiusUserNameType.setStatus("current")


class _SvcRadiusUserName_Type(DisplayString):
    """Custom type svcRadiusUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcRadiusUserName_Type.__name__ = "DisplayString"
_SvcRadiusUserName_Object = MibTableColumn
svcRadiusUserName = _SvcRadiusUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 22),
    _SvcRadiusUserName_Type()
)
svcRadiusUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcRadiusUserName.setStatus("current")


class _SvcVcSwitching_Type(TruthValue):
    """Custom type svcVcSwitching based on TruthValue"""


_SvcVcSwitching_Object = MibTableColumn
svcVcSwitching = _SvcVcSwitching_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 23),
    _SvcVcSwitching_Type()
)
svcVcSwitching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVcSwitching.setStatus("current")
_SvcRadiusPEDiscPolicy_Type = TNamedItemOrEmpty
_SvcRadiusPEDiscPolicy_Object = MibTableColumn
svcRadiusPEDiscPolicy = _SvcRadiusPEDiscPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 24),
    _SvcRadiusPEDiscPolicy_Type()
)
svcRadiusPEDiscPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcRadiusPEDiscPolicy.setStatus("current")


class _SvcRadiusDiscoveryShutdown_Type(ServiceAdminStatus):
    """Custom type svcRadiusDiscoveryShutdown based on ServiceAdminStatus"""


_SvcRadiusDiscoveryShutdown_Object = MibTableColumn
svcRadiusDiscoveryShutdown = _SvcRadiusDiscoveryShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 25),
    _SvcRadiusDiscoveryShutdown_Type()
)
svcRadiusDiscoveryShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcRadiusDiscoveryShutdown.setStatus("current")


class _SvcVplsType_Type(Integer32):
    """Custom type svcVplsType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bVpls", 2),
          ("iVpls", 3),
          ("none", 1),
          ("rVpls", 10))
    )


_SvcVplsType_Type.__name__ = "Integer32"
_SvcVplsType_Object = MibTableColumn
svcVplsType = _SvcVplsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 26),
    _SvcVplsType_Type()
)
svcVplsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVplsType.setStatus("current")
_SvcNumMcStandbySaps_Type = Integer32
_SvcNumMcStandbySaps_Object = MibTableColumn
svcNumMcStandbySaps = _SvcNumMcStandbySaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 27),
    _SvcNumMcStandbySaps_Type()
)
svcNumMcStandbySaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNumMcStandbySaps.setStatus("current")


class _SvcName_Type(TLNamedItemOrEmpty):
    """Custom type svcName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_SvcName_Object = MibTableColumn
svcName = _SvcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 29),
    _SvcName_Type()
)
svcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcName.setStatus("current")


class _SvcInterASMvpn_Type(TruthValue):
    """Custom type svcInterASMvpn based on TruthValue"""


_SvcInterASMvpn_Object = MibTableColumn
svcInterASMvpn = _SvcInterASMvpn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 30),
    _SvcInterASMvpn_Type()
)
svcInterASMvpn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcInterASMvpn.setStatus("current")


class _SvcHashLabel_Type(TruthValue):
    """Custom type svcHashLabel based on TruthValue"""


_SvcHashLabel_Object = MibTableColumn
svcHashLabel = _SvcHashLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 31),
    _SvcHashLabel_Type()
)
svcHashLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcHashLabel.setStatus("current")
_SvcTmplUsed_Type = TNamedItemOrEmpty
_SvcTmplUsed_Object = MibTableColumn
svcTmplUsed = _SvcTmplUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 32),
    _SvcTmplUsed_Type()
)
svcTmplUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTmplUsed.setStatus("current")
_SvcCtrlSvcId_Type = TmnxServId
_SvcCtrlSvcId_Object = MibTableColumn
svcCtrlSvcId = _SvcCtrlSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 33),
    _SvcCtrlSvcId_Type()
)
svcCtrlSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcCtrlSvcId.setStatus("current")
_SvcCreationOrigin_Type = L2RouteOrigin
_SvcCreationOrigin_Object = MibTableColumn
svcCreationOrigin = _SvcCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 2, 1, 34),
    _SvcCreationOrigin_Type()
)
svcCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcCreationOrigin.setStatus("current")
_SvcTlsInfoTable_Object = MibTable
svcTlsInfoTable = _SvcTlsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    svcTlsInfoTable.setStatus("current")
_SvcTlsInfoEntry_Object = MibTableRow
svcTlsInfoEntry = _SvcTlsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1)
)
svcTlsInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcTlsInfoEntry.setStatus("current")


class _SvcTlsMacLearning_Type(TmnxEnabledDisabled):
    """Custom type svcTlsMacLearning based on TmnxEnabledDisabled"""


_SvcTlsMacLearning_Object = MibTableColumn
svcTlsMacLearning = _SvcTlsMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 1),
    _SvcTlsMacLearning_Type()
)
svcTlsMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacLearning.setStatus("current")


class _SvcTlsDiscardUnknownDest_Type(TmnxEnabledDisabled):
    """Custom type svcTlsDiscardUnknownDest based on TmnxEnabledDisabled"""


_SvcTlsDiscardUnknownDest_Object = MibTableColumn
svcTlsDiscardUnknownDest = _SvcTlsDiscardUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 2),
    _SvcTlsDiscardUnknownDest_Type()
)
svcTlsDiscardUnknownDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsDiscardUnknownDest.setStatus("current")


class _SvcTlsFdbTableSize_Type(Integer32):
    """Custom type svcTlsFdbTableSize based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511999),
    )


_SvcTlsFdbTableSize_Type.__name__ = "Integer32"
_SvcTlsFdbTableSize_Object = MibTableColumn
svcTlsFdbTableSize = _SvcTlsFdbTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 3),
    _SvcTlsFdbTableSize_Type()
)
svcTlsFdbTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsFdbTableSize.setStatus("current")
_SvcTlsFdbNumEntries_Type = Integer32
_SvcTlsFdbNumEntries_Object = MibTableColumn
svcTlsFdbNumEntries = _SvcTlsFdbNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 4),
    _SvcTlsFdbNumEntries_Type()
)
svcTlsFdbNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsFdbNumEntries.setStatus("current")
_SvcTlsFdbNumStaticEntries_Type = Integer32
_SvcTlsFdbNumStaticEntries_Object = MibTableColumn
svcTlsFdbNumStaticEntries = _SvcTlsFdbNumStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 5),
    _SvcTlsFdbNumStaticEntries_Type()
)
svcTlsFdbNumStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsFdbNumStaticEntries.setStatus("current")


class _SvcTlsFdbLocalAgeTime_Type(Integer32):
    """Custom type svcTlsFdbLocalAgeTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_SvcTlsFdbLocalAgeTime_Type.__name__ = "Integer32"
_SvcTlsFdbLocalAgeTime_Object = MibTableColumn
svcTlsFdbLocalAgeTime = _SvcTlsFdbLocalAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 6),
    _SvcTlsFdbLocalAgeTime_Type()
)
svcTlsFdbLocalAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsFdbLocalAgeTime.setStatus("current")


class _SvcTlsFdbRemoteAgeTime_Type(Integer32):
    """Custom type svcTlsFdbRemoteAgeTime based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_SvcTlsFdbRemoteAgeTime_Type.__name__ = "Integer32"
_SvcTlsFdbRemoteAgeTime_Object = MibTableColumn
svcTlsFdbRemoteAgeTime = _SvcTlsFdbRemoteAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 7),
    _SvcTlsFdbRemoteAgeTime_Type()
)
svcTlsFdbRemoteAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsFdbRemoteAgeTime.setStatus("current")


class _SvcTlsStpAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type svcTlsStpAdminStatus based on TmnxEnabledDisabled"""


_SvcTlsStpAdminStatus_Object = MibTableColumn
svcTlsStpAdminStatus = _SvcTlsStpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 8),
    _SvcTlsStpAdminStatus_Type()
)
svcTlsStpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsStpAdminStatus.setStatus("current")


class _SvcTlsStpPriority_Type(Integer32):
    """Custom type svcTlsStpPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SvcTlsStpPriority_Type.__name__ = "Integer32"
_SvcTlsStpPriority_Object = MibTableColumn
svcTlsStpPriority = _SvcTlsStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 9),
    _SvcTlsStpPriority_Type()
)
svcTlsStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsStpPriority.setStatus("current")
_SvcTlsStpBridgeAddress_Type = MacAddress
_SvcTlsStpBridgeAddress_Object = MibTableColumn
svcTlsStpBridgeAddress = _SvcTlsStpBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 10),
    _SvcTlsStpBridgeAddress_Type()
)
svcTlsStpBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpBridgeAddress.setStatus("current")
_SvcTlsStpTimeSinceTopologyChange_Type = TimeTicks
_SvcTlsStpTimeSinceTopologyChange_Object = MibTableColumn
svcTlsStpTimeSinceTopologyChange = _SvcTlsStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 11),
    _SvcTlsStpTimeSinceTopologyChange_Type()
)
svcTlsStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpTimeSinceTopologyChange.setStatus("current")
_SvcTlsStpTopologyChanges_Type = Integer32
_SvcTlsStpTopologyChanges_Object = MibTableColumn
svcTlsStpTopologyChanges = _SvcTlsStpTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 12),
    _SvcTlsStpTopologyChanges_Type()
)
svcTlsStpTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpTopologyChanges.setStatus("current")
_SvcTlsStpDesignatedRoot_Type = BridgeId
_SvcTlsStpDesignatedRoot_Object = MibTableColumn
svcTlsStpDesignatedRoot = _SvcTlsStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 13),
    _SvcTlsStpDesignatedRoot_Type()
)
svcTlsStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpDesignatedRoot.setStatus("current")
_SvcTlsStpRootCost_Type = Integer32
_SvcTlsStpRootCost_Object = MibTableColumn
svcTlsStpRootCost = _SvcTlsStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 14),
    _SvcTlsStpRootCost_Type()
)
svcTlsStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpRootCost.setStatus("current")
_SvcTlsStpRootPort_Type = Integer32
_SvcTlsStpRootPort_Object = MibTableColumn
svcTlsStpRootPort = _SvcTlsStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 15),
    _SvcTlsStpRootPort_Type()
)
svcTlsStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpRootPort.setStatus("current")
_SvcTlsStpMaxAge_Type = Integer32
_SvcTlsStpMaxAge_Object = MibTableColumn
svcTlsStpMaxAge = _SvcTlsStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 16),
    _SvcTlsStpMaxAge_Type()
)
svcTlsStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpMaxAge.setStatus("current")
_SvcTlsStpHelloTime_Type = Integer32
_SvcTlsStpHelloTime_Object = MibTableColumn
svcTlsStpHelloTime = _SvcTlsStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 17),
    _SvcTlsStpHelloTime_Type()
)
svcTlsStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpHelloTime.setStatus("current")
_SvcTlsStpHoldTime_Type = Integer32
_SvcTlsStpHoldTime_Object = MibTableColumn
svcTlsStpHoldTime = _SvcTlsStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 18),
    _SvcTlsStpHoldTime_Type()
)
svcTlsStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpHoldTime.setStatus("obsolete")
_SvcTlsStpForwardDelay_Type = Integer32
_SvcTlsStpForwardDelay_Object = MibTableColumn
svcTlsStpForwardDelay = _SvcTlsStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 19),
    _SvcTlsStpForwardDelay_Type()
)
svcTlsStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpForwardDelay.setStatus("current")


class _SvcTlsStpBridgeMaxAge_Type(Integer32):
    """Custom type svcTlsStpBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_SvcTlsStpBridgeMaxAge_Type.__name__ = "Integer32"
_SvcTlsStpBridgeMaxAge_Object = MibTableColumn
svcTlsStpBridgeMaxAge = _SvcTlsStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 20),
    _SvcTlsStpBridgeMaxAge_Type()
)
svcTlsStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsStpBridgeMaxAge.setStatus("current")


class _SvcTlsStpBridgeHelloTime_Type(Integer32):
    """Custom type svcTlsStpBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvcTlsStpBridgeHelloTime_Type.__name__ = "Integer32"
_SvcTlsStpBridgeHelloTime_Object = MibTableColumn
svcTlsStpBridgeHelloTime = _SvcTlsStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 21),
    _SvcTlsStpBridgeHelloTime_Type()
)
svcTlsStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsStpBridgeHelloTime.setStatus("current")


class _SvcTlsStpBridgeForwardDelay_Type(Integer32):
    """Custom type svcTlsStpBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_SvcTlsStpBridgeForwardDelay_Type.__name__ = "Integer32"
_SvcTlsStpBridgeForwardDelay_Object = MibTableColumn
svcTlsStpBridgeForwardDelay = _SvcTlsStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 22),
    _SvcTlsStpBridgeForwardDelay_Type()
)
svcTlsStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsStpBridgeForwardDelay.setStatus("current")


class _SvcTlsStpOperStatus_Type(Integer32):
    """Custom type svcTlsStpOperStatus based on Integer32"""
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


_SvcTlsStpOperStatus_Type.__name__ = "Integer32"
_SvcTlsStpOperStatus_Object = MibTableColumn
svcTlsStpOperStatus = _SvcTlsStpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 30),
    _SvcTlsStpOperStatus_Type()
)
svcTlsStpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpOperStatus.setStatus("current")


class _SvcTlsStpVirtualRootBridgeStatus_Type(Integer32):
    """Custom type svcTlsStpVirtualRootBridgeStatus based on Integer32"""
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


_SvcTlsStpVirtualRootBridgeStatus_Type.__name__ = "Integer32"
_SvcTlsStpVirtualRootBridgeStatus_Object = MibTableColumn
svcTlsStpVirtualRootBridgeStatus = _SvcTlsStpVirtualRootBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 31),
    _SvcTlsStpVirtualRootBridgeStatus_Type()
)
svcTlsStpVirtualRootBridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpVirtualRootBridgeStatus.setStatus("current")


class _SvcTlsMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type svcTlsMacAgeing based on TmnxEnabledDisabled"""


_SvcTlsMacAgeing_Object = MibTableColumn
svcTlsMacAgeing = _SvcTlsMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 32),
    _SvcTlsMacAgeing_Type()
)
svcTlsMacAgeing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacAgeing.setStatus("current")
_SvcTlsStpTopologyChangeActive_Type = TruthValue
_SvcTlsStpTopologyChangeActive_Object = MibTableColumn
svcTlsStpTopologyChangeActive = _SvcTlsStpTopologyChangeActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 33),
    _SvcTlsStpTopologyChangeActive_Type()
)
svcTlsStpTopologyChangeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpTopologyChangeActive.setStatus("current")


class _SvcTlsFdbTableFullHighWatermark_Type(Integer32):
    """Custom type svcTlsFdbTableFullHighWatermark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTlsFdbTableFullHighWatermark_Type.__name__ = "Integer32"
_SvcTlsFdbTableFullHighWatermark_Object = MibTableColumn
svcTlsFdbTableFullHighWatermark = _SvcTlsFdbTableFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 34),
    _SvcTlsFdbTableFullHighWatermark_Type()
)
svcTlsFdbTableFullHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsFdbTableFullHighWatermark.setStatus("current")


class _SvcTlsFdbTableFullLowWatermark_Type(Integer32):
    """Custom type svcTlsFdbTableFullLowWatermark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTlsFdbTableFullLowWatermark_Type.__name__ = "Integer32"
_SvcTlsFdbTableFullLowWatermark_Object = MibTableColumn
svcTlsFdbTableFullLowWatermark = _SvcTlsFdbTableFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 35),
    _SvcTlsFdbTableFullLowWatermark_Type()
)
svcTlsFdbTableFullLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsFdbTableFullLowWatermark.setStatus("current")
_SvcTlsVpnId_Type = VpnId
_SvcTlsVpnId_Object = MibTableColumn
svcTlsVpnId = _SvcTlsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 36),
    _SvcTlsVpnId_Type()
)
svcTlsVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsVpnId.setStatus("current")
_SvcTlsCustId_Type = TmnxCustId
_SvcTlsCustId_Object = MibTableColumn
svcTlsCustId = _SvcTlsCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 37),
    _SvcTlsCustId_Type()
)
svcTlsCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsCustId.setStatus("current")


class _SvcTlsStpVersion_Type(Integer32):
    """Custom type svcTlsStpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("compDot1w", 3),
          ("dot1w", 4),
          ("mstp", 5),
          ("pmstp", 6),
          ("rstp", 2))
    )


_SvcTlsStpVersion_Type.__name__ = "Integer32"
_SvcTlsStpVersion_Object = MibTableColumn
svcTlsStpVersion = _SvcTlsStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 38),
    _SvcTlsStpVersion_Type()
)
svcTlsStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsStpVersion.setStatus("current")


class _SvcTlsStpHoldCount_Type(Integer32):
    """Custom type svcTlsStpHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SvcTlsStpHoldCount_Type.__name__ = "Integer32"
_SvcTlsStpHoldCount_Object = MibTableColumn
svcTlsStpHoldCount = _SvcTlsStpHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 39),
    _SvcTlsStpHoldCount_Type()
)
svcTlsStpHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsStpHoldCount.setStatus("current")
_SvcTlsStpPrimaryBridge_Type = BridgeId
_SvcTlsStpPrimaryBridge_Object = MibTableColumn
svcTlsStpPrimaryBridge = _SvcTlsStpPrimaryBridge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 40),
    _SvcTlsStpPrimaryBridge_Type()
)
svcTlsStpPrimaryBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpPrimaryBridge.setStatus("current")


class _SvcTlsStpBridgeInstanceId_Type(Integer32):
    """Custom type svcTlsStpBridgeInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SvcTlsStpBridgeInstanceId_Type.__name__ = "Integer32"
_SvcTlsStpBridgeInstanceId_Object = MibTableColumn
svcTlsStpBridgeInstanceId = _SvcTlsStpBridgeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 41),
    _SvcTlsStpBridgeInstanceId_Type()
)
svcTlsStpBridgeInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpBridgeInstanceId.setStatus("current")
_SvcTlsStpVcpOperProtocol_Type = StpProtocol
_SvcTlsStpVcpOperProtocol_Object = MibTableColumn
svcTlsStpVcpOperProtocol = _SvcTlsStpVcpOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 42),
    _SvcTlsStpVcpOperProtocol_Type()
)
svcTlsStpVcpOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpVcpOperProtocol.setStatus("current")


class _SvcTlsMacMoveMaxRate_Type(Unsigned32):
    """Custom type svcTlsMacMoveMaxRate based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvcTlsMacMoveMaxRate_Type.__name__ = "Unsigned32"
_SvcTlsMacMoveMaxRate_Object = MibTableColumn
svcTlsMacMoveMaxRate = _SvcTlsMacMoveMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 43),
    _SvcTlsMacMoveMaxRate_Type()
)
svcTlsMacMoveMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacMoveMaxRate.setStatus("current")


class _SvcTlsMacMoveRetryTimeout_Type(Unsigned32):
    """Custom type svcTlsMacMoveRetryTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SvcTlsMacMoveRetryTimeout_Type.__name__ = "Unsigned32"
_SvcTlsMacMoveRetryTimeout_Object = MibTableColumn
svcTlsMacMoveRetryTimeout = _SvcTlsMacMoveRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 44),
    _SvcTlsMacMoveRetryTimeout_Type()
)
svcTlsMacMoveRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacMoveRetryTimeout.setStatus("current")


class _SvcTlsMacMoveAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type svcTlsMacMoveAdminStatus based on TmnxEnabledDisabled"""


_SvcTlsMacMoveAdminStatus_Object = MibTableColumn
svcTlsMacMoveAdminStatus = _SvcTlsMacMoveAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 45),
    _SvcTlsMacMoveAdminStatus_Type()
)
svcTlsMacMoveAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacMoveAdminStatus.setStatus("current")
_SvcTlsMacRelearnOnly_Type = TruthValue
_SvcTlsMacRelearnOnly_Object = MibTableColumn
svcTlsMacRelearnOnly = _SvcTlsMacRelearnOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 46),
    _SvcTlsMacRelearnOnly_Type()
)
svcTlsMacRelearnOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsMacRelearnOnly.setStatus("current")


class _SvcTlsMfibTableSize_Type(Integer32):
    """Custom type svcTlsMfibTableSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40959),
    )


_SvcTlsMfibTableSize_Type.__name__ = "Integer32"
_SvcTlsMfibTableSize_Object = MibTableColumn
svcTlsMfibTableSize = _SvcTlsMfibTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 47),
    _SvcTlsMfibTableSize_Type()
)
svcTlsMfibTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMfibTableSize.setStatus("current")


class _SvcTlsMfibTableFullHighWatermark_Type(Integer32):
    """Custom type svcTlsMfibTableFullHighWatermark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTlsMfibTableFullHighWatermark_Type.__name__ = "Integer32"
_SvcTlsMfibTableFullHighWatermark_Object = MibTableColumn
svcTlsMfibTableFullHighWatermark = _SvcTlsMfibTableFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 48),
    _SvcTlsMfibTableFullHighWatermark_Type()
)
svcTlsMfibTableFullHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMfibTableFullHighWatermark.setStatus("current")


class _SvcTlsMfibTableFullLowWatermark_Type(Integer32):
    """Custom type svcTlsMfibTableFullLowWatermark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTlsMfibTableFullLowWatermark_Type.__name__ = "Integer32"
_SvcTlsMfibTableFullLowWatermark_Object = MibTableColumn
svcTlsMfibTableFullLowWatermark = _SvcTlsMfibTableFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 49),
    _SvcTlsMfibTableFullLowWatermark_Type()
)
svcTlsMfibTableFullLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMfibTableFullLowWatermark.setStatus("current")


class _SvcTlsMacFlushOnFail_Type(TmnxEnabledDisabled):
    """Custom type svcTlsMacFlushOnFail based on TmnxEnabledDisabled"""


_SvcTlsMacFlushOnFail_Object = MibTableColumn
svcTlsMacFlushOnFail = _SvcTlsMacFlushOnFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 50),
    _SvcTlsMacFlushOnFail_Type()
)
svcTlsMacFlushOnFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacFlushOnFail.setStatus("current")


class _SvcTlsStpRegionName_Type(DisplayString):
    """Custom type svcTlsStpRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SvcTlsStpRegionName_Type.__name__ = "DisplayString"
_SvcTlsStpRegionName_Object = MibTableColumn
svcTlsStpRegionName = _SvcTlsStpRegionName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 51),
    _SvcTlsStpRegionName_Type()
)
svcTlsStpRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsStpRegionName.setStatus("current")


class _SvcTlsStpRegionRevision_Type(Integer32):
    """Custom type svcTlsStpRegionRevision based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SvcTlsStpRegionRevision_Type.__name__ = "Integer32"
_SvcTlsStpRegionRevision_Object = MibTableColumn
svcTlsStpRegionRevision = _SvcTlsStpRegionRevision_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 52),
    _SvcTlsStpRegionRevision_Type()
)
svcTlsStpRegionRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsStpRegionRevision.setStatus("current")


class _SvcTlsStpBridgeMaxHops_Type(Integer32):
    """Custom type svcTlsStpBridgeMaxHops based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_SvcTlsStpBridgeMaxHops_Type.__name__ = "Integer32"
_SvcTlsStpBridgeMaxHops_Object = MibTableColumn
svcTlsStpBridgeMaxHops = _SvcTlsStpBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 53),
    _SvcTlsStpBridgeMaxHops_Type()
)
svcTlsStpBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsStpBridgeMaxHops.setStatus("current")
_SvcTlsStpCistRegionalRoot_Type = BridgeId
_SvcTlsStpCistRegionalRoot_Object = MibTableColumn
svcTlsStpCistRegionalRoot = _SvcTlsStpCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 54),
    _SvcTlsStpCistRegionalRoot_Type()
)
svcTlsStpCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpCistRegionalRoot.setStatus("current")
_SvcTlsStpCistIntRootCost_Type = Integer32
_SvcTlsStpCistIntRootCost_Object = MibTableColumn
svcTlsStpCistIntRootCost = _SvcTlsStpCistIntRootCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 55),
    _SvcTlsStpCistIntRootCost_Type()
)
svcTlsStpCistIntRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpCistIntRootCost.setStatus("current")
_SvcTlsStpCistRemainingHopCount_Type = Integer32
_SvcTlsStpCistRemainingHopCount_Object = MibTableColumn
svcTlsStpCistRemainingHopCount = _SvcTlsStpCistRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 56),
    _SvcTlsStpCistRemainingHopCount_Type()
)
svcTlsStpCistRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpCistRemainingHopCount.setStatus("current")
_SvcTlsStpCistRegionalRootPort_Type = Integer32
_SvcTlsStpCistRegionalRootPort_Object = MibTableColumn
svcTlsStpCistRegionalRootPort = _SvcTlsStpCistRegionalRootPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 57),
    _SvcTlsStpCistRegionalRootPort_Type()
)
svcTlsStpCistRegionalRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsStpCistRegionalRootPort.setStatus("current")
_SvcTlsFdbNumLearnedEntries_Type = Integer32
_SvcTlsFdbNumLearnedEntries_Object = MibTableColumn
svcTlsFdbNumLearnedEntries = _SvcTlsFdbNumLearnedEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 58),
    _SvcTlsFdbNumLearnedEntries_Type()
)
svcTlsFdbNumLearnedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsFdbNumLearnedEntries.setStatus("current")
_SvcTlsFdbNumOamEntries_Type = Integer32
_SvcTlsFdbNumOamEntries_Object = MibTableColumn
svcTlsFdbNumOamEntries = _SvcTlsFdbNumOamEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 59),
    _SvcTlsFdbNumOamEntries_Type()
)
svcTlsFdbNumOamEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsFdbNumOamEntries.setStatus("current")
_SvcTlsFdbNumDhcpEntries_Type = Integer32
_SvcTlsFdbNumDhcpEntries_Object = MibTableColumn
svcTlsFdbNumDhcpEntries = _SvcTlsFdbNumDhcpEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 60),
    _SvcTlsFdbNumDhcpEntries_Type()
)
svcTlsFdbNumDhcpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsFdbNumDhcpEntries.setStatus("current")
_SvcTlsFdbNumHostEntries_Type = Integer32
_SvcTlsFdbNumHostEntries_Object = MibTableColumn
svcTlsFdbNumHostEntries = _SvcTlsFdbNumHostEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 61),
    _SvcTlsFdbNumHostEntries_Type()
)
svcTlsFdbNumHostEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsFdbNumHostEntries.setStatus("current")


class _SvcTlsShcvAction_Type(Integer32):
    """Custom type svcTlsShcvAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("remove", 2))
    )


_SvcTlsShcvAction_Type.__name__ = "Integer32"
_SvcTlsShcvAction_Object = MibTableColumn
svcTlsShcvAction = _SvcTlsShcvAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 62),
    _SvcTlsShcvAction_Type()
)
svcTlsShcvAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsShcvAction.setStatus("current")
_SvcTlsShcvSrcIp_Type = IpAddress
_SvcTlsShcvSrcIp_Object = MibTableColumn
svcTlsShcvSrcIp = _SvcTlsShcvSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 63),
    _SvcTlsShcvSrcIp_Type()
)
svcTlsShcvSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsShcvSrcIp.setStatus("current")
_SvcTlsShcvSrcMac_Type = MacAddress
_SvcTlsShcvSrcMac_Object = MibTableColumn
svcTlsShcvSrcMac = _SvcTlsShcvSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 64),
    _SvcTlsShcvSrcMac_Type()
)
svcTlsShcvSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsShcvSrcMac.setStatus("current")


class _SvcTlsShcvInterval_Type(Unsigned32):
    """Custom type svcTlsShcvInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_SvcTlsShcvInterval_Type.__name__ = "Unsigned32"
_SvcTlsShcvInterval_Object = MibTableColumn
svcTlsShcvInterval = _SvcTlsShcvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 65),
    _SvcTlsShcvInterval_Type()
)
svcTlsShcvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsShcvInterval.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsShcvInterval.setUnits("minutes")


class _SvcTlsPriPortsCumulativeFactor_Type(Unsigned32):
    """Custom type svcTlsPriPortsCumulativeFactor based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_SvcTlsPriPortsCumulativeFactor_Type.__name__ = "Unsigned32"
_SvcTlsPriPortsCumulativeFactor_Object = MibTableColumn
svcTlsPriPortsCumulativeFactor = _SvcTlsPriPortsCumulativeFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 66),
    _SvcTlsPriPortsCumulativeFactor_Type()
)
svcTlsPriPortsCumulativeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsPriPortsCumulativeFactor.setStatus("current")


class _SvcTlsSecPortsCumulativeFactor_Type(Unsigned32):
    """Custom type svcTlsSecPortsCumulativeFactor based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 9),
    )


_SvcTlsSecPortsCumulativeFactor_Type.__name__ = "Unsigned32"
_SvcTlsSecPortsCumulativeFactor_Object = MibTableColumn
svcTlsSecPortsCumulativeFactor = _SvcTlsSecPortsCumulativeFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 67),
    _SvcTlsSecPortsCumulativeFactor_Type()
)
svcTlsSecPortsCumulativeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsSecPortsCumulativeFactor.setStatus("current")
_SvcTlsL2ptTermEnabled_Type = TruthValue
_SvcTlsL2ptTermEnabled_Object = MibTableColumn
svcTlsL2ptTermEnabled = _SvcTlsL2ptTermEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 68),
    _SvcTlsL2ptTermEnabled_Type()
)
svcTlsL2ptTermEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsL2ptTermEnabled.setStatus("current")


class _SvcTlsPropagateMacFlush_Type(TruthValue):
    """Custom type svcTlsPropagateMacFlush based on TruthValue"""


_SvcTlsPropagateMacFlush_Object = MibTableColumn
svcTlsPropagateMacFlush = _SvcTlsPropagateMacFlush_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 69),
    _SvcTlsPropagateMacFlush_Type()
)
svcTlsPropagateMacFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsPropagateMacFlush.setStatus("current")


class _SvcTlsMrpAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type svcTlsMrpAdminStatus based on TmnxEnabledDisabled"""


_SvcTlsMrpAdminStatus_Object = MibTableColumn
svcTlsMrpAdminStatus = _SvcTlsMrpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 70),
    _SvcTlsMrpAdminStatus_Type()
)
svcTlsMrpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMrpAdminStatus.setStatus("current")


class _SvcTlsMrpMaxAttributes_Type(Unsigned32):
    """Custom type svcTlsMrpMaxAttributes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_SvcTlsMrpMaxAttributes_Type.__name__ = "Unsigned32"
_SvcTlsMrpMaxAttributes_Object = MibTableColumn
svcTlsMrpMaxAttributes = _SvcTlsMrpMaxAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 71),
    _SvcTlsMrpMaxAttributes_Type()
)
svcTlsMrpMaxAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMrpMaxAttributes.setStatus("current")
_SvcTlsMrpAttributeCount_Type = Unsigned32
_SvcTlsMrpAttributeCount_Object = MibTableColumn
svcTlsMrpAttributeCount = _SvcTlsMrpAttributeCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 72),
    _SvcTlsMrpAttributeCount_Type()
)
svcTlsMrpAttributeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsMrpAttributeCount.setStatus("current")
_SvcTlsMrpFailedRegisterCount_Type = Unsigned32
_SvcTlsMrpFailedRegisterCount_Object = MibTableColumn
svcTlsMrpFailedRegisterCount = _SvcTlsMrpFailedRegisterCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 73),
    _SvcTlsMrpFailedRegisterCount_Type()
)
svcTlsMrpFailedRegisterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsMrpFailedRegisterCount.setStatus("current")


class _SvcTlsMcPathMgmtPlcyName_Type(TNamedItem):
    """Custom type svcTlsMcPathMgmtPlcyName based on TNamedItem"""
    defaultValue = OctetString("default")


_SvcTlsMcPathMgmtPlcyName_Object = MibTableColumn
svcTlsMcPathMgmtPlcyName = _SvcTlsMcPathMgmtPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 74),
    _SvcTlsMcPathMgmtPlcyName_Type()
)
svcTlsMcPathMgmtPlcyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMcPathMgmtPlcyName.setStatus("current")


class _SvcTlsMrpFloodTime_Type(Unsigned32):
    """Custom type svcTlsMrpFloodTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 600),
    )


_SvcTlsMrpFloodTime_Type.__name__ = "Unsigned32"
_SvcTlsMrpFloodTime_Object = MibTableColumn
svcTlsMrpFloodTime = _SvcTlsMrpFloodTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 75),
    _SvcTlsMrpFloodTime_Type()
)
svcTlsMrpFloodTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMrpFloodTime.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsMrpFloodTime.setUnits("seconds")


class _SvcTlsMrpAttrTblHighWatermark_Type(Integer32):
    """Custom type svcTlsMrpAttrTblHighWatermark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTlsMrpAttrTblHighWatermark_Type.__name__ = "Integer32"
_SvcTlsMrpAttrTblHighWatermark_Object = MibTableColumn
svcTlsMrpAttrTblHighWatermark = _SvcTlsMrpAttrTblHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 76),
    _SvcTlsMrpAttrTblHighWatermark_Type()
)
svcTlsMrpAttrTblHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMrpAttrTblHighWatermark.setStatus("current")


class _SvcTlsMrpAttrTblLowWatermark_Type(Integer32):
    """Custom type svcTlsMrpAttrTblLowWatermark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTlsMrpAttrTblLowWatermark_Type.__name__ = "Integer32"
_SvcTlsMrpAttrTblLowWatermark_Object = MibTableColumn
svcTlsMrpAttrTblLowWatermark = _SvcTlsMrpAttrTblLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 77),
    _SvcTlsMrpAttrTblLowWatermark_Type()
)
svcTlsMrpAttrTblLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMrpAttrTblLowWatermark.setStatus("current")


class _SvcTlsMacMoveNumRetries_Type(Unsigned32):
    """Custom type svcTlsMacMoveNumRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SvcTlsMacMoveNumRetries_Type.__name__ = "Unsigned32"
_SvcTlsMacMoveNumRetries_Object = MibTableColumn
svcTlsMacMoveNumRetries = _SvcTlsMacMoveNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 78),
    _SvcTlsMacMoveNumRetries_Type()
)
svcTlsMacMoveNumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacMoveNumRetries.setStatus("current")


class _SvcTlsMacSubNetLen_Type(Integer32):
    """Custom type svcTlsMacSubNetLen based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 48),
    )


_SvcTlsMacSubNetLen_Type.__name__ = "Integer32"
_SvcTlsMacSubNetLen_Object = MibTableColumn
svcTlsMacSubNetLen = _SvcTlsMacSubNetLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 79),
    _SvcTlsMacSubNetLen_Type()
)
svcTlsMacSubNetLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacSubNetLen.setStatus("current")


class _SvcTlsSendFlushOnBVplsFail_Type(TruthValue):
    """Custom type svcTlsSendFlushOnBVplsFail based on TruthValue"""


_SvcTlsSendFlushOnBVplsFail_Object = MibTableColumn
svcTlsSendFlushOnBVplsFail = _SvcTlsSendFlushOnBVplsFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 80),
    _SvcTlsSendFlushOnBVplsFail_Type()
)
svcTlsSendFlushOnBVplsFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsSendFlushOnBVplsFail.setStatus("current")


class _SvcTlsPropMacFlushFromBVpls_Type(TruthValue):
    """Custom type svcTlsPropMacFlushFromBVpls based on TruthValue"""


_SvcTlsPropMacFlushFromBVpls_Object = MibTableColumn
svcTlsPropMacFlushFromBVpls = _SvcTlsPropMacFlushFromBVpls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 81),
    _SvcTlsPropMacFlushFromBVpls_Type()
)
svcTlsPropMacFlushFromBVpls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsPropMacFlushFromBVpls.setStatus("current")


class _SvcTlsMacNotifInterval_Type(Unsigned32):
    """Custom type svcTlsMacNotifInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTlsMacNotifInterval_Type.__name__ = "Unsigned32"
_SvcTlsMacNotifInterval_Object = MibTableColumn
svcTlsMacNotifInterval = _SvcTlsMacNotifInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 82),
    _SvcTlsMacNotifInterval_Type()
)
svcTlsMacNotifInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacNotifInterval.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsMacNotifInterval.setUnits("deci-seconds")


class _SvcTlsMacNotifCount_Type(Unsigned32):
    """Custom type svcTlsMacNotifCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SvcTlsMacNotifCount_Type.__name__ = "Unsigned32"
_SvcTlsMacNotifCount_Object = MibTableColumn
svcTlsMacNotifCount = _SvcTlsMacNotifCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 83),
    _SvcTlsMacNotifCount_Type()
)
svcTlsMacNotifCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacNotifCount.setStatus("current")


class _SvcTlsMacNotifAdminState_Type(TmnxEnabledDisabled):
    """Custom type svcTlsMacNotifAdminState based on TmnxEnabledDisabled"""


_SvcTlsMacNotifAdminState_Object = MibTableColumn
svcTlsMacNotifAdminState = _SvcTlsMacNotifAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 84),
    _SvcTlsMacNotifAdminState_Type()
)
svcTlsMacNotifAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsMacNotifAdminState.setStatus("current")


class _SvcTlsPerSvcHashing_Type(TmnxEnabledDisabled):
    """Custom type svcTlsPerSvcHashing based on TmnxEnabledDisabled"""


_SvcTlsPerSvcHashing_Object = MibTableColumn
svcTlsPerSvcHashing = _SvcTlsPerSvcHashing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 85),
    _SvcTlsPerSvcHashing_Type()
)
svcTlsPerSvcHashing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsPerSvcHashing.setStatus("current")


class _SvcTlsAllowIpIfBinding_Type(TruthValue):
    """Custom type svcTlsAllowIpIfBinding based on TruthValue"""


_SvcTlsAllowIpIfBinding_Object = MibTableColumn
svcTlsAllowIpIfBinding = _SvcTlsAllowIpIfBinding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 86),
    _SvcTlsAllowIpIfBinding_Type()
)
svcTlsAllowIpIfBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsAllowIpIfBinding.setStatus("current")


class _SvcTlsShcvRetryTimeout_Type(Unsigned32):
    """Custom type svcTlsShcvRetryTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_SvcTlsShcvRetryTimeout_Type.__name__ = "Unsigned32"
_SvcTlsShcvRetryTimeout_Object = MibTableColumn
svcTlsShcvRetryTimeout = _SvcTlsShcvRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 87),
    _SvcTlsShcvRetryTimeout_Type()
)
svcTlsShcvRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsShcvRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsShcvRetryTimeout.setUnits("seconds")


class _SvcTlsShcvRetryCount_Type(Unsigned32):
    """Custom type svcTlsShcvRetryCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 29),
    )


_SvcTlsShcvRetryCount_Type.__name__ = "Unsigned32"
_SvcTlsShcvRetryCount_Object = MibTableColumn
svcTlsShcvRetryCount = _SvcTlsShcvRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 88),
    _SvcTlsShcvRetryCount_Type()
)
svcTlsShcvRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsShcvRetryCount.setStatus("current")


class _SvcTlsTempFloodTime_Type(Integer32):
    """Custom type svcTlsTempFloodTime based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(3, 600),
    )


_SvcTlsTempFloodTime_Type.__name__ = "Integer32"
_SvcTlsTempFloodTime_Object = MibTableColumn
svcTlsTempFloodTime = _SvcTlsTempFloodTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 89),
    _SvcTlsTempFloodTime_Type()
)
svcTlsTempFloodTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsTempFloodTime.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsTempFloodTime.setUnits("seconds")
_SvcTlsTempFloodActive_Type = TruthValue
_SvcTlsTempFloodActive_Object = MibTableColumn
svcTlsTempFloodActive = _SvcTlsTempFloodActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 90),
    _SvcTlsTempFloodActive_Type()
)
svcTlsTempFloodActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsTempFloodActive.setStatus("current")
_SvcTlsTempFloodChangeCount_Type = Integer32
_SvcTlsTempFloodChangeCount_Object = MibTableColumn
svcTlsTempFloodChangeCount = _SvcTlsTempFloodChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 3, 1, 91),
    _SvcTlsTempFloodChangeCount_Type()
)
svcTlsTempFloodChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsTempFloodChangeCount.setStatus("current")
_TlsFdbInfoTable_Object = MibTable
tlsFdbInfoTable = _TlsFdbInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    tlsFdbInfoTable.setStatus("current")
_TlsFdbInfoEntry_Object = MibTableRow
tlsFdbInfoEntry = _TlsFdbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1)
)
tlsFdbInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsFdbMacAddr"),
)
if mibBuilder.loadTexts:
    tlsFdbInfoEntry.setStatus("current")
_TlsFdbMacAddr_Type = MacAddress
_TlsFdbMacAddr_Object = MibTableColumn
tlsFdbMacAddr = _TlsFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 1),
    _TlsFdbMacAddr_Type()
)
tlsFdbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsFdbMacAddr.setStatus("current")
_TlsFdbRowStatus_Type = RowStatus
_TlsFdbRowStatus_Object = MibTableColumn
tlsFdbRowStatus = _TlsFdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 2),
    _TlsFdbRowStatus_Type()
)
tlsFdbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsFdbRowStatus.setStatus("current")


class _TlsFdbType_Type(Integer32):
    """Custom type tlsFdbType based on Integer32"""
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
        *(("dhcp", 4),
          ("host", 5),
          ("intf", 6),
          ("learned", 2),
          ("oam", 3),
          ("spb", 7),
          ("static", 1))
    )


_TlsFdbType_Type.__name__ = "Integer32"
_TlsFdbType_Object = MibTableColumn
tlsFdbType = _TlsFdbType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 3),
    _TlsFdbType_Type()
)
tlsFdbType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsFdbType.setStatus("current")


class _TlsFdbLocale_Type(Integer32):
    """Custom type tlsFdbLocale based on Integer32"""
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
        *(("cpm", 3),
          ("endpoint", 4),
          ("sap", 1),
          ("sdp", 2))
    )


_TlsFdbLocale_Type.__name__ = "Integer32"
_TlsFdbLocale_Object = MibTableColumn
tlsFdbLocale = _TlsFdbLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 4),
    _TlsFdbLocale_Type()
)
tlsFdbLocale.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsFdbLocale.setStatus("current")
_TlsFdbPortId_Type = TmnxPortID
_TlsFdbPortId_Object = MibTableColumn
tlsFdbPortId = _TlsFdbPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 5),
    _TlsFdbPortId_Type()
)
tlsFdbPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsFdbPortId.setStatus("current")
_TlsFdbEncapValue_Type = TmnxEncapVal
_TlsFdbEncapValue_Object = MibTableColumn
tlsFdbEncapValue = _TlsFdbEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 6),
    _TlsFdbEncapValue_Type()
)
tlsFdbEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsFdbEncapValue.setStatus("current")
_TlsFdbSdpId_Type = SdpId
_TlsFdbSdpId_Object = MibTableColumn
tlsFdbSdpId = _TlsFdbSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 7),
    _TlsFdbSdpId_Type()
)
tlsFdbSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsFdbSdpId.setStatus("current")
_TlsFdbVcId_Type = Unsigned32
_TlsFdbVcId_Object = MibTableColumn
tlsFdbVcId = _TlsFdbVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 8),
    _TlsFdbVcId_Type()
)
tlsFdbVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsFdbVcId.setStatus("current")
_TlsFdbVpnId_Type = VpnId
_TlsFdbVpnId_Object = MibTableColumn
tlsFdbVpnId = _TlsFdbVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 9),
    _TlsFdbVpnId_Type()
)
tlsFdbVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsFdbVpnId.setStatus("current")
_TlsFdbCustId_Type = TmnxCustId
_TlsFdbCustId_Object = MibTableColumn
tlsFdbCustId = _TlsFdbCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 10),
    _TlsFdbCustId_Type()
)
tlsFdbCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsFdbCustId.setStatus("current")
_TlsFdbLastStateChange_Type = TimeStamp
_TlsFdbLastStateChange_Object = MibTableColumn
tlsFdbLastStateChange = _TlsFdbLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 11),
    _TlsFdbLastStateChange_Type()
)
tlsFdbLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsFdbLastStateChange.setStatus("current")
_TlsFdbProtected_Type = TruthValue
_TlsFdbProtected_Object = MibTableColumn
tlsFdbProtected = _TlsFdbProtected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 12),
    _TlsFdbProtected_Type()
)
tlsFdbProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsFdbProtected.setStatus("current")
_TlsFdbBackboneDstMac_Type = MacAddress
_TlsFdbBackboneDstMac_Object = MibTableColumn
tlsFdbBackboneDstMac = _TlsFdbBackboneDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 13),
    _TlsFdbBackboneDstMac_Type()
)
tlsFdbBackboneDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsFdbBackboneDstMac.setStatus("current")
_TlsFdbNumIVplsMac_Type = Unsigned32
_TlsFdbNumIVplsMac_Object = MibTableColumn
tlsFdbNumIVplsMac = _TlsFdbNumIVplsMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 14),
    _TlsFdbNumIVplsMac_Type()
)
tlsFdbNumIVplsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsFdbNumIVplsMac.setStatus("current")
_TlsFdbEndPointName_Type = TNamedItemOrEmpty
_TlsFdbEndPointName_Object = MibTableColumn
tlsFdbEndPointName = _TlsFdbEndPointName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 15),
    _TlsFdbEndPointName_Type()
)
tlsFdbEndPointName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsFdbEndPointName.setStatus("current")
_TlsFdbEPMacOperSdpId_Type = SdpId
_TlsFdbEPMacOperSdpId_Object = MibTableColumn
tlsFdbEPMacOperSdpId = _TlsFdbEPMacOperSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 16),
    _TlsFdbEPMacOperSdpId_Type()
)
tlsFdbEPMacOperSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsFdbEPMacOperSdpId.setStatus("current")
_TlsFdbEPMacOperVcId_Type = Unsigned32
_TlsFdbEPMacOperVcId_Object = MibTableColumn
tlsFdbEPMacOperVcId = _TlsFdbEPMacOperVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 17),
    _TlsFdbEPMacOperVcId_Type()
)
tlsFdbEPMacOperVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsFdbEPMacOperVcId.setStatus("current")
_TlsFdbPbbNumEpipes_Type = Unsigned32
_TlsFdbPbbNumEpipes_Object = MibTableColumn
tlsFdbPbbNumEpipes = _TlsFdbPbbNumEpipes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 4, 1, 18),
    _TlsFdbPbbNumEpipes_Type()
)
tlsFdbPbbNumEpipes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsFdbPbbNumEpipes.setStatus("current")
_IesIfTable_Object = MibTable
iesIfTable = _IesIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    iesIfTable.setStatus("current")
_IesIfEntry_Object = MibTableRow
iesIfEntry = _IesIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1)
)
iesIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    iesIfEntry.setStatus("current")
_IesIfIndex_Type = InterfaceIndex
_IesIfIndex_Object = MibTableColumn
iesIfIndex = _IesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 1),
    _IesIfIndex_Type()
)
iesIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIfIndex.setStatus("current")
_IesIfRowStatus_Type = RowStatus
_IesIfRowStatus_Object = MibTableColumn
iesIfRowStatus = _IesIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 2),
    _IesIfRowStatus_Type()
)
iesIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfRowStatus.setStatus("current")
_IesIfName_Type = TNamedItem
_IesIfName_Object = MibTableColumn
iesIfName = _IesIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 3),
    _IesIfName_Type()
)
iesIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfName.setStatus("current")
_IesIfDescription_Type = ServObjLongDesc
_IesIfDescription_Object = MibTableColumn
iesIfDescription = _IesIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 4),
    _IesIfDescription_Type()
)
iesIfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfDescription.setStatus("current")


class _IesIfAdminStatus_Type(ServiceAdminStatus):
    """Custom type iesIfAdminStatus based on ServiceAdminStatus"""


_IesIfAdminStatus_Object = MibTableColumn
iesIfAdminStatus = _IesIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 5),
    _IesIfAdminStatus_Type()
)
iesIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfAdminStatus.setStatus("current")
_IesIfOperStatus_Type = ServiceOperStatus
_IesIfOperStatus_Object = MibTableColumn
iesIfOperStatus = _IesIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 6),
    _IesIfOperStatus_Type()
)
iesIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIfOperStatus.setStatus("current")
_IesIfLastMgmtChange_Type = TimeStamp
_IesIfLastMgmtChange_Object = MibTableColumn
iesIfLastMgmtChange = _IesIfLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 7),
    _IesIfLastMgmtChange_Type()
)
iesIfLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIfLastMgmtChange.setStatus("current")
_IesIfVpnId_Type = VpnId
_IesIfVpnId_Object = MibTableColumn
iesIfVpnId = _IesIfVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 8),
    _IesIfVpnId_Type()
)
iesIfVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIfVpnId.setStatus("obsolete")
_IesIfCustId_Type = TmnxCustId
_IesIfCustId_Object = MibTableColumn
iesIfCustId = _IesIfCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 9),
    _IesIfCustId_Type()
)
iesIfCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIfCustId.setStatus("current")
_IesIfLoopback_Type = TruthValue
_IesIfLoopback_Object = MibTableColumn
iesIfLoopback = _IesIfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 10),
    _IesIfLoopback_Type()
)
iesIfLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfLoopback.setStatus("current")
_IesIfLastStatusChange_Type = TimeStamp
_IesIfLastStatusChange_Object = MibTableColumn
iesIfLastStatusChange = _IesIfLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 11),
    _IesIfLastStatusChange_Type()
)
iesIfLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIfLastStatusChange.setStatus("current")


class _IesIfType_Type(Integer32):
    """Custom type iesIfType based on Integer32"""
    defaultValue = 1

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
        *(("aarp", 10),
          ("cem", 5),
          ("group", 3),
          ("ipMirror", 7),
          ("ipsec", 6),
          ("redundant", 4),
          ("reserved9", 9),
          ("service", 1),
          ("subscriber", 2),
          ("video", 8))
    )


_IesIfType_Type.__name__ = "Integer32"
_IesIfType_Object = MibTableColumn
iesIfType = _IesIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 12),
    _IesIfType_Type()
)
iesIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfType.setStatus("current")


class _IesIfParentIf_Type(InterfaceIndexOrZero):
    """Custom type iesIfParentIf based on InterfaceIndexOrZero"""
    defaultValue = 0


_IesIfParentIf_Object = MibTableColumn
iesIfParentIf = _IesIfParentIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 13),
    _IesIfParentIf_Type()
)
iesIfParentIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfParentIf.setStatus("current")


class _IesIfShcvSource_Type(Integer32):
    """Custom type iesIfShcvSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vrrp", 2))
    )


_IesIfShcvSource_Type.__name__ = "Integer32"
_IesIfShcvSource_Object = MibTableColumn
iesIfShcvSource = _IesIfShcvSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 14),
    _IesIfShcvSource_Type()
)
iesIfShcvSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfShcvSource.setStatus("current")


class _IesIfShcvAction_Type(Integer32):
    """Custom type iesIfShcvAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("remove", 2))
    )


_IesIfShcvAction_Type.__name__ = "Integer32"
_IesIfShcvAction_Object = MibTableColumn
iesIfShcvAction = _IesIfShcvAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 15),
    _IesIfShcvAction_Type()
)
iesIfShcvAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfShcvAction.setStatus("current")


class _IesIfShcvInterval_Type(Unsigned32):
    """Custom type iesIfShcvInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_IesIfShcvInterval_Type.__name__ = "Unsigned32"
_IesIfShcvInterval_Object = MibTableColumn
iesIfShcvInterval = _IesIfShcvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 16),
    _IesIfShcvInterval_Type()
)
iesIfShcvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfShcvInterval.setStatus("current")
if mibBuilder.loadTexts:
    iesIfShcvInterval.setUnits("minutes")


class _IesIfFwdServId_Type(TmnxServId):
    """Custom type iesIfFwdServId based on TmnxServId"""
    defaultValue = 0


_IesIfFwdServId_Object = MibTableColumn
iesIfFwdServId = _IesIfFwdServId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 17),
    _IesIfFwdServId_Type()
)
iesIfFwdServId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfFwdServId.setStatus("current")


class _IesIfFwdSubIf_Type(InterfaceIndexOrZero):
    """Custom type iesIfFwdSubIf based on InterfaceIndexOrZero"""
    defaultValue = 0


_IesIfFwdSubIf_Object = MibTableColumn
iesIfFwdSubIf = _IesIfFwdSubIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 18),
    _IesIfFwdSubIf_Type()
)
iesIfFwdSubIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfFwdSubIf.setStatus("current")
_IesIfPrivateRetailSubnets_Type = TruthValue
_IesIfPrivateRetailSubnets_Object = MibTableColumn
iesIfPrivateRetailSubnets = _IesIfPrivateRetailSubnets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 19),
    _IesIfPrivateRetailSubnets_Type()
)
iesIfPrivateRetailSubnets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfPrivateRetailSubnets.setStatus("current")


class _IesIfDelegatedPrefixLen_Type(Unsigned32):
    """Custom type iesIfDelegatedPrefixLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48, 64),
    )


_IesIfDelegatedPrefixLen_Type.__name__ = "Unsigned32"
_IesIfDelegatedPrefixLen_Object = MibTableColumn
iesIfDelegatedPrefixLen = _IesIfDelegatedPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 20),
    _IesIfDelegatedPrefixLen_Type()
)
iesIfDelegatedPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfDelegatedPrefixLen.setStatus("current")


class _IesIfLns_Type(TruthValue):
    """Custom type iesIfLns based on TruthValue"""


_IesIfLns_Object = MibTableColumn
iesIfLns = _IesIfLns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 21),
    _IesIfLns_Type()
)
iesIfLns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfLns.setStatus("current")


class _IesIfVplsName_Type(TLNamedItemOrEmpty):
    """Custom type iesIfVplsName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_IesIfVplsName_Object = MibTableColumn
iesIfVplsName = _IesIfVplsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 22),
    _IesIfVplsName_Type()
)
iesIfVplsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfVplsName.setStatus("current")
_IesIfVplsStatus_Type = ServiceOperStatus
_IesIfVplsStatus_Object = MibTableColumn
iesIfVplsStatus = _IesIfVplsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 23),
    _IesIfVplsStatus_Type()
)
iesIfVplsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIfVplsStatus.setStatus("current")
_IesIfVplsFailedReason_Type = DisplayString
_IesIfVplsFailedReason_Object = MibTableColumn
iesIfVplsFailedReason = _IesIfVplsFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 24),
    _IesIfVplsFailedReason_Type()
)
iesIfVplsFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIfVplsFailedReason.setStatus("current")


class _IesIfShcvRetryTimeout_Type(Unsigned32):
    """Custom type iesIfShcvRetryTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_IesIfShcvRetryTimeout_Type.__name__ = "Unsigned32"
_IesIfShcvRetryTimeout_Object = MibTableColumn
iesIfShcvRetryTimeout = _IesIfShcvRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 25),
    _IesIfShcvRetryTimeout_Type()
)
iesIfShcvRetryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfShcvRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    iesIfShcvRetryTimeout.setUnits("seconds")


class _IesIfShcvRetryCount_Type(Unsigned32):
    """Custom type iesIfShcvRetryCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 29),
    )


_IesIfShcvRetryCount_Type.__name__ = "Unsigned32"
_IesIfShcvRetryCount_Object = MibTableColumn
iesIfShcvRetryCount = _IesIfShcvRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 26),
    _IesIfShcvRetryCount_Type()
)
iesIfShcvRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfShcvRetryCount.setStatus("current")


class _IesIfSapEgressQosId_Type(TPolicyID):
    """Custom type iesIfSapEgressQosId based on TPolicyID"""
    defaultValue = 0


_IesIfSapEgressQosId_Object = MibTableColumn
iesIfSapEgressQosId = _IesIfSapEgressQosId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 27),
    _IesIfSapEgressQosId_Type()
)
iesIfSapEgressQosId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfSapEgressQosId.setStatus("current")


class _IesIfDefaultPrimaryDnsIPv4Addr_Type(InetAddressIPv4):
    """Custom type iesIfDefaultPrimaryDnsIPv4Addr based on InetAddressIPv4"""
    defaultHexValue = ""


_IesIfDefaultPrimaryDnsIPv4Addr_Object = MibTableColumn
iesIfDefaultPrimaryDnsIPv4Addr = _IesIfDefaultPrimaryDnsIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 28),
    _IesIfDefaultPrimaryDnsIPv4Addr_Type()
)
iesIfDefaultPrimaryDnsIPv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfDefaultPrimaryDnsIPv4Addr.setStatus("current")


class _IesIfDefaultSecondaryDnsIPv4Addr_Type(InetAddressIPv4):
    """Custom type iesIfDefaultSecondaryDnsIPv4Addr based on InetAddressIPv4"""
    defaultHexValue = ""


_IesIfDefaultSecondaryDnsIPv4Addr_Object = MibTableColumn
iesIfDefaultSecondaryDnsIPv4Addr = _IesIfDefaultSecondaryDnsIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 29),
    _IesIfDefaultSecondaryDnsIPv4Addr_Type()
)
iesIfDefaultSecondaryDnsIPv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfDefaultSecondaryDnsIPv4Addr.setStatus("current")


class _IesIfDefaultPrimaryDnsIPv6Addr_Type(InetAddressIPv6):
    """Custom type iesIfDefaultPrimaryDnsIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = ""


_IesIfDefaultPrimaryDnsIPv6Addr_Object = MibTableColumn
iesIfDefaultPrimaryDnsIPv6Addr = _IesIfDefaultPrimaryDnsIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 30),
    _IesIfDefaultPrimaryDnsIPv6Addr_Type()
)
iesIfDefaultPrimaryDnsIPv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfDefaultPrimaryDnsIPv6Addr.setStatus("current")


class _IesIfDefaultSecondaryDnsIPv6Addr_Type(InetAddressIPv6):
    """Custom type iesIfDefaultSecondaryDnsIPv6Addr based on InetAddressIPv6"""
    defaultHexValue = ""


_IesIfDefaultSecondaryDnsIPv6Addr_Object = MibTableColumn
iesIfDefaultSecondaryDnsIPv6Addr = _IesIfDefaultSecondaryDnsIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 31),
    _IesIfDefaultSecondaryDnsIPv6Addr_Type()
)
iesIfDefaultSecondaryDnsIPv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfDefaultSecondaryDnsIPv6Addr.setStatus("current")


class _IesIfIPv6ConfigAllowed_Type(TruthValue):
    """Custom type iesIfIPv6ConfigAllowed based on TruthValue"""


_IesIfIPv6ConfigAllowed_Object = MibTableColumn
iesIfIPv6ConfigAllowed = _IesIfIPv6ConfigAllowed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 32),
    _IesIfIPv6ConfigAllowed_Type()
)
iesIfIPv6ConfigAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfIPv6ConfigAllowed.setStatus("current")


class _IesIfSrrpRoutingEnabled_Type(TruthValue):
    """Custom type iesIfSrrpRoutingEnabled based on TruthValue"""


_IesIfSrrpRoutingEnabled_Object = MibTableColumn
iesIfSrrpRoutingEnabled = _IesIfSrrpRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 33),
    _IesIfSrrpRoutingEnabled_Type()
)
iesIfSrrpRoutingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfSrrpRoutingEnabled.setStatus("current")


class _IesIfSrrpRoutingHoldTime_Type(Unsigned32):
    """Custom type iesIfSrrpRoutingHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_IesIfSrrpRoutingHoldTime_Type.__name__ = "Unsigned32"
_IesIfSrrpRoutingHoldTime_Object = MibTableColumn
iesIfSrrpRoutingHoldTime = _IesIfSrrpRoutingHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 34),
    _IesIfSrrpRoutingHoldTime_Type()
)
iesIfSrrpRoutingHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfSrrpRoutingHoldTime.setStatus("current")
_IesIfMonitorOperGrp_Type = TNamedItemOrEmpty
_IesIfMonitorOperGrp_Object = MibTableColumn
iesIfMonitorOperGrp = _IesIfMonitorOperGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 35),
    _IesIfMonitorOperGrp_Type()
)
iesIfMonitorOperGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfMonitorOperGrp.setStatus("current")


class _IesIfAllowUnmatchingSubnets_Type(TruthValue):
    """Custom type iesIfAllowUnmatchingSubnets based on TruthValue"""


_IesIfAllowUnmatchingSubnets_Object = MibTableColumn
iesIfAllowUnmatchingSubnets = _IesIfAllowUnmatchingSubnets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 36),
    _IesIfAllowUnmatchingSubnets_Type()
)
iesIfAllowUnmatchingSubnets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfAllowUnmatchingSubnets.setStatus("current")


class _IesIfGroupInterfaceType_Type(Integer32):
    """Custom type iesIfGroupInterfaceType based on Integer32"""
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
        *(("lns", 2),
          ("none", 0),
          ("plain", 1),
          ("softGre", 3))
    )


_IesIfGroupInterfaceType_Type.__name__ = "Integer32"
_IesIfGroupInterfaceType_Object = MibTableColumn
iesIfGroupInterfaceType = _IesIfGroupInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 37),
    _IesIfGroupInterfaceType_Type()
)
iesIfGroupInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfGroupInterfaceType.setStatus("current")


class _IesIfShcvFamily_Type(Integer32):
    """Custom type iesIfShcvFamily based on Integer32"""
    defaultValue = 1

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
          ("ipv4", 1),
          ("ipv6", 2))
    )


_IesIfShcvFamily_Type.__name__ = "Integer32"
_IesIfShcvFamily_Object = MibTableColumn
iesIfShcvFamily = _IesIfShcvFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 38),
    _IesIfShcvFamily_Type()
)
iesIfShcvFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfShcvFamily.setStatus("current")


class _IesIfIPv6IpoeBridgedModeEnabled_Type(TruthValue):
    """Custom type iesIfIPv6IpoeBridgedModeEnabled based on TruthValue"""


_IesIfIPv6IpoeBridgedModeEnabled_Object = MibTableColumn
iesIfIPv6IpoeBridgedModeEnabled = _IesIfIPv6IpoeBridgedModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 39),
    _IesIfIPv6IpoeBridgedModeEnabled_Type()
)
iesIfIPv6IpoeBridgedModeEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfIPv6IpoeBridgedModeEnabled.setStatus("current")


class _IesIfIPv6AllowUnmatchingPfxs_Type(TruthValue):
    """Custom type iesIfIPv6AllowUnmatchingPfxs based on TruthValue"""


_IesIfIPv6AllowUnmatchingPfxs_Object = MibTableColumn
iesIfIPv6AllowUnmatchingPfxs = _IesIfIPv6AllowUnmatchingPfxs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 5, 1, 40),
    _IesIfIPv6AllowUnmatchingPfxs_Type()
)
iesIfIPv6AllowUnmatchingPfxs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIfIPv6AllowUnmatchingPfxs.setStatus("current")
_TlsShgInfoTable_Object = MibTable
tlsShgInfoTable = _TlsShgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6)
)
if mibBuilder.loadTexts:
    tlsShgInfoTable.setStatus("current")
_TlsShgInfoEntry_Object = MibTableRow
tlsShgInfoEntry = _TlsShgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1)
)
tlsShgInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (1, "TIMETRA-SERV-MIB", "tlsShgName"),
)
if mibBuilder.loadTexts:
    tlsShgInfoEntry.setStatus("current")
_TlsShgName_Type = TNamedItem
_TlsShgName_Object = MibTableColumn
tlsShgName = _TlsShgName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 1),
    _TlsShgName_Type()
)
tlsShgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsShgName.setStatus("current")
_TlsShgRowStatus_Type = RowStatus
_TlsShgRowStatus_Object = MibTableColumn
tlsShgRowStatus = _TlsShgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 2),
    _TlsShgRowStatus_Type()
)
tlsShgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsShgRowStatus.setStatus("current")
_TlsShgCustId_Type = TmnxCustId
_TlsShgCustId_Object = MibTableColumn
tlsShgCustId = _TlsShgCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 3),
    _TlsShgCustId_Type()
)
tlsShgCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsShgCustId.setStatus("current")
_TlsShgInstanceId_Type = Unsigned32
_TlsShgInstanceId_Object = MibTableColumn
tlsShgInstanceId = _TlsShgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 4),
    _TlsShgInstanceId_Type()
)
tlsShgInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsShgInstanceId.setStatus("current")
_TlsShgDescription_Type = ServObjDesc
_TlsShgDescription_Object = MibTableColumn
tlsShgDescription = _TlsShgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 5),
    _TlsShgDescription_Type()
)
tlsShgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsShgDescription.setStatus("current")
_TlsShgLastMgmtChange_Type = TimeStamp
_TlsShgLastMgmtChange_Object = MibTableColumn
tlsShgLastMgmtChange = _TlsShgLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 6),
    _TlsShgLastMgmtChange_Type()
)
tlsShgLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsShgLastMgmtChange.setStatus("current")


class _TlsShgResidential_Type(TruthValue):
    """Custom type tlsShgResidential based on TruthValue"""


_TlsShgResidential_Object = MibTableColumn
tlsShgResidential = _TlsShgResidential_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 7),
    _TlsShgResidential_Type()
)
tlsShgResidential.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsShgResidential.setStatus("current")


class _TlsShgRestProtSrcMac_Type(TruthValue):
    """Custom type tlsShgRestProtSrcMac based on TruthValue"""


_TlsShgRestProtSrcMac_Object = MibTableColumn
tlsShgRestProtSrcMac = _TlsShgRestProtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 8),
    _TlsShgRestProtSrcMac_Type()
)
tlsShgRestProtSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsShgRestProtSrcMac.setStatus("current")


class _TlsShgRestUnprotDstMac_Type(TruthValue):
    """Custom type tlsShgRestUnprotDstMac based on TruthValue"""


_TlsShgRestUnprotDstMac_Object = MibTableColumn
tlsShgRestUnprotDstMac = _TlsShgRestUnprotDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 9),
    _TlsShgRestUnprotDstMac_Type()
)
tlsShgRestUnprotDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsShgRestUnprotDstMac.setStatus("current")


class _TlsShgRestProtSrcMacAction_Type(Integer32):
    """Custom type tlsShgRestProtSrcMacAction based on Integer32"""
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
        *(("alarm-only", 2),
          ("disable", 1),
          ("discardFrame", 3))
    )


_TlsShgRestProtSrcMacAction_Type.__name__ = "Integer32"
_TlsShgRestProtSrcMacAction_Object = MibTableColumn
tlsShgRestProtSrcMacAction = _TlsShgRestProtSrcMacAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 10),
    _TlsShgRestProtSrcMacAction_Type()
)
tlsShgRestProtSrcMacAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsShgRestProtSrcMacAction.setStatus("current")
_TlsShgCreationOrigin_Type = L2RouteOrigin
_TlsShgCreationOrigin_Object = MibTableColumn
tlsShgCreationOrigin = _TlsShgCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 11),
    _TlsShgCreationOrigin_Type()
)
tlsShgCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsShgCreationOrigin.setStatus("current")
_TlsShgSiteName_Type = TNamedItemOrEmpty
_TlsShgSiteName_Object = MibTableColumn
tlsShgSiteName = _TlsShgSiteName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 12),
    _TlsShgSiteName_Type()
)
tlsShgSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsShgSiteName.setStatus("current")


class _TlsShgAutoLearnMacProtect_Type(TruthValue):
    """Custom type tlsShgAutoLearnMacProtect based on TruthValue"""


_TlsShgAutoLearnMacProtect_Object = MibTableColumn
tlsShgAutoLearnMacProtect = _TlsShgAutoLearnMacProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 6, 1, 13),
    _TlsShgAutoLearnMacProtect_Type()
)
tlsShgAutoLearnMacProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsShgAutoLearnMacProtect.setStatus("current")
_SvcApipeInfoTable_Object = MibTable
svcApipeInfoTable = _SvcApipeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 7)
)
if mibBuilder.loadTexts:
    svcApipeInfoTable.setStatus("current")
_SvcApipeInfoEntry_Object = MibTableRow
svcApipeInfoEntry = _SvcApipeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 7, 1)
)
svcApipeInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcApipeInfoEntry.setStatus("current")


class _SvcApipeInterworking_Type(Integer32):
    """Custom type svcApipeInterworking based on Integer32"""
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
        *(("frf-5", 2),
          ("frf-8-2-translate", 3),
          ("none", 1))
    )


_SvcApipeInterworking_Type.__name__ = "Integer32"
_SvcApipeInterworking_Object = MibTableColumn
svcApipeInterworking = _SvcApipeInterworking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 7, 1, 1),
    _SvcApipeInterworking_Type()
)
svcApipeInterworking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcApipeInterworking.setStatus("current")


class _SvcApipeSignaledVllTypeOverride_Type(Integer32):
    """Custom type svcApipeSignaledVllTypeOverride based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("atmVcc", 8),
          ("none", 0))
    )


_SvcApipeSignaledVllTypeOverride_Type.__name__ = "Integer32"
_SvcApipeSignaledVllTypeOverride_Object = MibTableColumn
svcApipeSignaledVllTypeOverride = _SvcApipeSignaledVllTypeOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 7, 1, 2),
    _SvcApipeSignaledVllTypeOverride_Type()
)
svcApipeSignaledVllTypeOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcApipeSignaledVllTypeOverride.setStatus("current")
_TlsMFibInfoTable_Object = MibTable
tlsMFibInfoTable = _TlsMFibInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8)
)
if mibBuilder.loadTexts:
    tlsMFibInfoTable.setStatus("obsolete")
_TlsMFibInfoEntry_Object = MibTableRow
tlsMFibInfoEntry = _TlsMFibInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8, 1)
)
tlsMFibInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibInfoGrpAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibInfoSrcAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibInfoLocale"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibInfoPortId"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibInfoEncapValue"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibInfoSdpId"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibInfoVcId"),
)
if mibBuilder.loadTexts:
    tlsMFibInfoEntry.setStatus("obsolete")
_TlsMFibInfoGrpAddr_Type = IpAddress
_TlsMFibInfoGrpAddr_Object = MibTableColumn
tlsMFibInfoGrpAddr = _TlsMFibInfoGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8, 1, 1),
    _TlsMFibInfoGrpAddr_Type()
)
tlsMFibInfoGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibInfoGrpAddr.setStatus("obsolete")
_TlsMFibInfoSrcAddr_Type = IpAddress
_TlsMFibInfoSrcAddr_Object = MibTableColumn
tlsMFibInfoSrcAddr = _TlsMFibInfoSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8, 1, 2),
    _TlsMFibInfoSrcAddr_Type()
)
tlsMFibInfoSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibInfoSrcAddr.setStatus("obsolete")
_TlsMFibInfoLocale_Type = MfibLocation
_TlsMFibInfoLocale_Object = MibTableColumn
tlsMFibInfoLocale = _TlsMFibInfoLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8, 1, 3),
    _TlsMFibInfoLocale_Type()
)
tlsMFibInfoLocale.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibInfoLocale.setStatus("obsolete")
_TlsMFibInfoPortId_Type = TmnxPortID
_TlsMFibInfoPortId_Object = MibTableColumn
tlsMFibInfoPortId = _TlsMFibInfoPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8, 1, 4),
    _TlsMFibInfoPortId_Type()
)
tlsMFibInfoPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibInfoPortId.setStatus("obsolete")
_TlsMFibInfoEncapValue_Type = TmnxEncapVal
_TlsMFibInfoEncapValue_Object = MibTableColumn
tlsMFibInfoEncapValue = _TlsMFibInfoEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8, 1, 5),
    _TlsMFibInfoEncapValue_Type()
)
tlsMFibInfoEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibInfoEncapValue.setStatus("obsolete")
_TlsMFibInfoSdpId_Type = SdpId
_TlsMFibInfoSdpId_Object = MibTableColumn
tlsMFibInfoSdpId = _TlsMFibInfoSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8, 1, 6),
    _TlsMFibInfoSdpId_Type()
)
tlsMFibInfoSdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibInfoSdpId.setStatus("obsolete")
_TlsMFibInfoVcId_Type = Unsigned32
_TlsMFibInfoVcId_Object = MibTableColumn
tlsMFibInfoVcId = _TlsMFibInfoVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8, 1, 7),
    _TlsMFibInfoVcId_Type()
)
tlsMFibInfoVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibInfoVcId.setStatus("obsolete")
_TlsMFibInfoFwdOrBlk_Type = MfibGrpSrcFwdOrBlk
_TlsMFibInfoFwdOrBlk_Object = MibTableColumn
tlsMFibInfoFwdOrBlk = _TlsMFibInfoFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8, 1, 8),
    _TlsMFibInfoFwdOrBlk_Type()
)
tlsMFibInfoFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMFibInfoFwdOrBlk.setStatus("obsolete")
_TlsMFibInfoSvcId_Type = TmnxServId
_TlsMFibInfoSvcId_Object = MibTableColumn
tlsMFibInfoSvcId = _TlsMFibInfoSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 8, 1, 9),
    _TlsMFibInfoSvcId_Type()
)
tlsMFibInfoSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMFibInfoSvcId.setStatus("obsolete")
_TlsMFibGrpSrcStatsTable_Object = MibTable
tlsMFibGrpSrcStatsTable = _TlsMFibGrpSrcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 9)
)
if mibBuilder.loadTexts:
    tlsMFibGrpSrcStatsTable.setStatus("obsolete")
_TlsMFibGrpSrcStatsEntry_Object = MibTableRow
tlsMFibGrpSrcStatsEntry = _TlsMFibGrpSrcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 9, 1)
)
tlsMFibGrpSrcStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibGrpSrcStatsGrpAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibGrpSrcStatsSrcAddr"),
)
if mibBuilder.loadTexts:
    tlsMFibGrpSrcStatsEntry.setStatus("obsolete")
_TlsMFibGrpSrcStatsGrpAddr_Type = IpAddress
_TlsMFibGrpSrcStatsGrpAddr_Object = MibTableColumn
tlsMFibGrpSrcStatsGrpAddr = _TlsMFibGrpSrcStatsGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 9, 1, 1),
    _TlsMFibGrpSrcStatsGrpAddr_Type()
)
tlsMFibGrpSrcStatsGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibGrpSrcStatsGrpAddr.setStatus("obsolete")
_TlsMFibGrpSrcStatsSrcAddr_Type = IpAddress
_TlsMFibGrpSrcStatsSrcAddr_Object = MibTableColumn
tlsMFibGrpSrcStatsSrcAddr = _TlsMFibGrpSrcStatsSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 9, 1, 2),
    _TlsMFibGrpSrcStatsSrcAddr_Type()
)
tlsMFibGrpSrcStatsSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibGrpSrcStatsSrcAddr.setStatus("obsolete")
_TlsMFibGrpSrcStatsForwardedPkts_Type = Counter64
_TlsMFibGrpSrcStatsForwardedPkts_Object = MibTableColumn
tlsMFibGrpSrcStatsForwardedPkts = _TlsMFibGrpSrcStatsForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 9, 1, 3),
    _TlsMFibGrpSrcStatsForwardedPkts_Type()
)
tlsMFibGrpSrcStatsForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMFibGrpSrcStatsForwardedPkts.setStatus("obsolete")
_TlsMFibGrpSrcStatsForwardedOctets_Type = Counter64
_TlsMFibGrpSrcStatsForwardedOctets_Object = MibTableColumn
tlsMFibGrpSrcStatsForwardedOctets = _TlsMFibGrpSrcStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 9, 1, 4),
    _TlsMFibGrpSrcStatsForwardedOctets_Type()
)
tlsMFibGrpSrcStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMFibGrpSrcStatsForwardedOctets.setStatus("obsolete")
_TlsRdntGrpTable_Object = MibTable
tlsRdntGrpTable = _TlsRdntGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 10)
)
if mibBuilder.loadTexts:
    tlsRdntGrpTable.setStatus("current")
_TlsRdntGrpEntry_Object = MibTableRow
tlsRdntGrpEntry = _TlsRdntGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 10, 1)
)
tlsRdntGrpEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (1, "TIMETRA-SERV-MIB", "tlsRdntGrpName"),
)
if mibBuilder.loadTexts:
    tlsRdntGrpEntry.setStatus("current")
_TlsRdntGrpName_Type = TNamedItem
_TlsRdntGrpName_Object = MibTableColumn
tlsRdntGrpName = _TlsRdntGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 10, 1, 1),
    _TlsRdntGrpName_Type()
)
tlsRdntGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsRdntGrpName.setStatus("current")
_TlsRdntGrpRowStatus_Type = RowStatus
_TlsRdntGrpRowStatus_Object = MibTableColumn
tlsRdntGrpRowStatus = _TlsRdntGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 10, 1, 2),
    _TlsRdntGrpRowStatus_Type()
)
tlsRdntGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsRdntGrpRowStatus.setStatus("current")


class _TlsRdntGrpDescription_Type(ServObjDesc):
    """Custom type tlsRdntGrpDescription based on ServObjDesc"""
    defaultHexValue = ""


_TlsRdntGrpDescription_Object = MibTableColumn
tlsRdntGrpDescription = _TlsRdntGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 10, 1, 3),
    _TlsRdntGrpDescription_Type()
)
tlsRdntGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsRdntGrpDescription.setStatus("current")
_TlsRdntGrpLastMgmtChange_Type = TimeStamp
_TlsRdntGrpLastMgmtChange_Object = MibTableColumn
tlsRdntGrpLastMgmtChange = _TlsRdntGrpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 10, 1, 4),
    _TlsRdntGrpLastMgmtChange_Type()
)
tlsRdntGrpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsRdntGrpLastMgmtChange.setStatus("current")
_TlsRdntGrpMemberTable_Object = MibTable
tlsRdntGrpMemberTable = _TlsRdntGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 11)
)
if mibBuilder.loadTexts:
    tlsRdntGrpMemberTable.setStatus("current")
_TlsRdntGrpMemberEntry_Object = MibTableRow
tlsRdntGrpMemberEntry = _TlsRdntGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 11, 1)
)
tlsRdntGrpMemberEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "tlsRdntGrpName"),
    (0, "TIMETRA-SERV-MIB", "tlsRdntGrpMemberRemoteNodeAddrTp"),
    (0, "TIMETRA-SERV-MIB", "tlsRdntGrpMemberRemoteNodeAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsRdntGrpMemberIsSap"),
    (0, "TIMETRA-SERV-MIB", "tlsRdntGrpMemberPort"),
    (0, "TIMETRA-SERV-MIB", "tlsRdntGrpMemberEncap"),
)
if mibBuilder.loadTexts:
    tlsRdntGrpMemberEntry.setStatus("current")
_TlsRdntGrpMemberRemoteNodeAddrTp_Type = InetAddressType
_TlsRdntGrpMemberRemoteNodeAddrTp_Object = MibTableColumn
tlsRdntGrpMemberRemoteNodeAddrTp = _TlsRdntGrpMemberRemoteNodeAddrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 11, 1, 1),
    _TlsRdntGrpMemberRemoteNodeAddrTp_Type()
)
tlsRdntGrpMemberRemoteNodeAddrTp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsRdntGrpMemberRemoteNodeAddrTp.setStatus("current")
_TlsRdntGrpMemberRemoteNodeAddr_Type = InetAddress
_TlsRdntGrpMemberRemoteNodeAddr_Object = MibTableColumn
tlsRdntGrpMemberRemoteNodeAddr = _TlsRdntGrpMemberRemoteNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 11, 1, 2),
    _TlsRdntGrpMemberRemoteNodeAddr_Type()
)
tlsRdntGrpMemberRemoteNodeAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsRdntGrpMemberRemoteNodeAddr.setStatus("current")
_TlsRdntGrpMemberIsSap_Type = TruthValue
_TlsRdntGrpMemberIsSap_Object = MibTableColumn
tlsRdntGrpMemberIsSap = _TlsRdntGrpMemberIsSap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 11, 1, 3),
    _TlsRdntGrpMemberIsSap_Type()
)
tlsRdntGrpMemberIsSap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsRdntGrpMemberIsSap.setStatus("current")
_TlsRdntGrpMemberPort_Type = TmnxPortID
_TlsRdntGrpMemberPort_Object = MibTableColumn
tlsRdntGrpMemberPort = _TlsRdntGrpMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 11, 1, 4),
    _TlsRdntGrpMemberPort_Type()
)
tlsRdntGrpMemberPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsRdntGrpMemberPort.setStatus("current")
_TlsRdntGrpMemberEncap_Type = TmnxEncapVal
_TlsRdntGrpMemberEncap_Object = MibTableColumn
tlsRdntGrpMemberEncap = _TlsRdntGrpMemberEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 11, 1, 5),
    _TlsRdntGrpMemberEncap_Type()
)
tlsRdntGrpMemberEncap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsRdntGrpMemberEncap.setStatus("current")
_TlsRdntGrpMemberRowStatus_Type = RowStatus
_TlsRdntGrpMemberRowStatus_Object = MibTableColumn
tlsRdntGrpMemberRowStatus = _TlsRdntGrpMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 11, 1, 6),
    _TlsRdntGrpMemberRowStatus_Type()
)
tlsRdntGrpMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsRdntGrpMemberRowStatus.setStatus("current")
_TlsRdntGrpMemberLastMgmtChange_Type = TimeStamp
_TlsRdntGrpMemberLastMgmtChange_Object = MibTableColumn
tlsRdntGrpMemberLastMgmtChange = _TlsRdntGrpMemberLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 11, 1, 7),
    _TlsRdntGrpMemberLastMgmtChange_Type()
)
tlsRdntGrpMemberLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsRdntGrpMemberLastMgmtChange.setStatus("current")
_TlsMstiTable_Object = MibTable
tlsMstiTable = _TlsMstiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 12)
)
if mibBuilder.loadTexts:
    tlsMstiTable.setStatus("current")
_TlsMstiEntry_Object = MibTableRow
tlsMstiEntry = _TlsMstiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 12, 1)
)
tlsMstiEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsMstiInstanceId"),
)
if mibBuilder.loadTexts:
    tlsMstiEntry.setStatus("current")
_TlsMstiInstanceId_Type = MstiInstanceId
_TlsMstiInstanceId_Object = MibTableColumn
tlsMstiInstanceId = _TlsMstiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 12, 1, 1),
    _TlsMstiInstanceId_Type()
)
tlsMstiInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMstiInstanceId.setStatus("current")
_TlsMstiRowStatus_Type = RowStatus
_TlsMstiRowStatus_Object = MibTableColumn
tlsMstiRowStatus = _TlsMstiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 12, 1, 2),
    _TlsMstiRowStatus_Type()
)
tlsMstiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsMstiRowStatus.setStatus("current")


class _TlsMstiPriority_Type(Integer32):
    """Custom type tlsMstiPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TlsMstiPriority_Type.__name__ = "Integer32"
_TlsMstiPriority_Object = MibTableColumn
tlsMstiPriority = _TlsMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 12, 1, 3),
    _TlsMstiPriority_Type()
)
tlsMstiPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsMstiPriority.setStatus("current")
_TlsMstiLastMgmtChange_Type = TimeStamp
_TlsMstiLastMgmtChange_Object = MibTableColumn
tlsMstiLastMgmtChange = _TlsMstiLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 12, 1, 4),
    _TlsMstiLastMgmtChange_Type()
)
tlsMstiLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMstiLastMgmtChange.setStatus("current")
_TlsMstiRegionalRoot_Type = BridgeId
_TlsMstiRegionalRoot_Object = MibTableColumn
tlsMstiRegionalRoot = _TlsMstiRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 12, 1, 5),
    _TlsMstiRegionalRoot_Type()
)
tlsMstiRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMstiRegionalRoot.setStatus("current")
_TlsMstiIntRootCost_Type = Integer32
_TlsMstiIntRootCost_Object = MibTableColumn
tlsMstiIntRootCost = _TlsMstiIntRootCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 12, 1, 6),
    _TlsMstiIntRootCost_Type()
)
tlsMstiIntRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMstiIntRootCost.setStatus("current")
_TlsMstiRemainingHopCount_Type = Integer32
_TlsMstiRemainingHopCount_Object = MibTableColumn
tlsMstiRemainingHopCount = _TlsMstiRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 12, 1, 7),
    _TlsMstiRemainingHopCount_Type()
)
tlsMstiRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMstiRemainingHopCount.setStatus("current")
_TlsMstiRegionalRootPort_Type = Integer32
_TlsMstiRegionalRootPort_Object = MibTableColumn
tlsMstiRegionalRootPort = _TlsMstiRegionalRootPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 12, 1, 8),
    _TlsMstiRegionalRootPort_Type()
)
tlsMstiRegionalRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMstiRegionalRootPort.setStatus("current")
_TlsMstiManagedVlanListTable_Object = MibTable
tlsMstiManagedVlanListTable = _TlsMstiManagedVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 13)
)
if mibBuilder.loadTexts:
    tlsMstiManagedVlanListTable.setStatus("current")
_TlsMstiManagedVlanListEntry_Object = MibTableRow
tlsMstiManagedVlanListEntry = _TlsMstiManagedVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 13, 1)
)
tlsMstiManagedVlanListEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsMstiInstanceId"),
    (0, "TIMETRA-SERV-MIB", "tlsMstiMvplsMinVlanTag"),
    (0, "TIMETRA-SERV-MIB", "tlsMstiMvplsMaxVlanTag"),
)
if mibBuilder.loadTexts:
    tlsMstiManagedVlanListEntry.setStatus("current")
_TlsMstiMvplsMinVlanTag_Type = QTag
_TlsMstiMvplsMinVlanTag_Object = MibTableColumn
tlsMstiMvplsMinVlanTag = _TlsMstiMvplsMinVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 13, 1, 1),
    _TlsMstiMvplsMinVlanTag_Type()
)
tlsMstiMvplsMinVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMstiMvplsMinVlanTag.setStatus("current")
_TlsMstiMvplsMaxVlanTag_Type = QTag
_TlsMstiMvplsMaxVlanTag_Object = MibTableColumn
tlsMstiMvplsMaxVlanTag = _TlsMstiMvplsMaxVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 13, 1, 2),
    _TlsMstiMvplsMaxVlanTag_Type()
)
tlsMstiMvplsMaxVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMstiMvplsMaxVlanTag.setStatus("current")
_TlsMstiMvplsRowStatus_Type = RowStatus
_TlsMstiMvplsRowStatus_Object = MibTableColumn
tlsMstiMvplsRowStatus = _TlsMstiMvplsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 13, 1, 3),
    _TlsMstiMvplsRowStatus_Type()
)
tlsMstiMvplsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsMstiMvplsRowStatus.setStatus("current")
_TlsEgressMulticastGroupTable_Object = MibTable
tlsEgressMulticastGroupTable = _TlsEgressMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14)
)
if mibBuilder.loadTexts:
    tlsEgressMulticastGroupTable.setStatus("current")
_TlsEgressMulticastGroupEntry_Object = MibTableRow
tlsEgressMulticastGroupEntry = _TlsEgressMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1)
)
tlsEgressMulticastGroupEntry.setIndexNames(
    (1, "TIMETRA-SERV-MIB", "tlsEgrMcGrpName"),
)
if mibBuilder.loadTexts:
    tlsEgressMulticastGroupEntry.setStatus("current")
_TlsEgrMcGrpName_Type = TNamedItem
_TlsEgrMcGrpName_Object = MibTableColumn
tlsEgrMcGrpName = _TlsEgrMcGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 1),
    _TlsEgrMcGrpName_Type()
)
tlsEgrMcGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsEgrMcGrpName.setStatus("current")
_TlsEgrMcGrpRowStatus_Type = RowStatus
_TlsEgrMcGrpRowStatus_Object = MibTableColumn
tlsEgrMcGrpRowStatus = _TlsEgrMcGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 2),
    _TlsEgrMcGrpRowStatus_Type()
)
tlsEgrMcGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpRowStatus.setStatus("current")
_TlsEgrMcGrpLastMgmtChange_Type = TimeStamp
_TlsEgrMcGrpLastMgmtChange_Object = MibTableColumn
tlsEgrMcGrpLastMgmtChange = _TlsEgrMcGrpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 3),
    _TlsEgrMcGrpLastMgmtChange_Type()
)
tlsEgrMcGrpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsEgrMcGrpLastMgmtChange.setStatus("current")
_TlsEgrMcGrpDescription_Type = ServObjDesc
_TlsEgrMcGrpDescription_Object = MibTableColumn
tlsEgrMcGrpDescription = _TlsEgrMcGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 4),
    _TlsEgrMcGrpDescription_Type()
)
tlsEgrMcGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpDescription.setStatus("current")


class _TlsEgrMcGrpChainLimit_Type(Unsigned32):
    """Custom type tlsEgrMcGrpChainLimit based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TlsEgrMcGrpChainLimit_Type.__name__ = "Unsigned32"
_TlsEgrMcGrpChainLimit_Object = MibTableColumn
tlsEgrMcGrpChainLimit = _TlsEgrMcGrpChainLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 5),
    _TlsEgrMcGrpChainLimit_Type()
)
tlsEgrMcGrpChainLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpChainLimit.setStatus("current")


class _TlsEgrMcGrpEncapType_Type(Integer32):
    """Custom type tlsEgrMcGrpEncapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("nullEncap", 1),
          ("qEncap", 2),
          ("qinqEncap", 10),
          ("unknown", 0))
    )


_TlsEgrMcGrpEncapType_Type.__name__ = "Integer32"
_TlsEgrMcGrpEncapType_Object = MibTableColumn
tlsEgrMcGrpEncapType = _TlsEgrMcGrpEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 6),
    _TlsEgrMcGrpEncapType_Type()
)
tlsEgrMcGrpEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpEncapType.setStatus("current")


class _TlsEgrMcGrpDot1qEtherType_Type(Unsigned32):
    """Custom type tlsEgrMcGrpDot1qEtherType based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TlsEgrMcGrpDot1qEtherType_Type.__name__ = "Unsigned32"
_TlsEgrMcGrpDot1qEtherType_Object = MibTableColumn
tlsEgrMcGrpDot1qEtherType = _TlsEgrMcGrpDot1qEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 7),
    _TlsEgrMcGrpDot1qEtherType_Type()
)
tlsEgrMcGrpDot1qEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpDot1qEtherType.setStatus("current")


class _TlsEgrMcGrpMacFilterId_Type(TFilterID):
    """Custom type tlsEgrMcGrpMacFilterId based on TFilterID"""
    defaultValue = 0


_TlsEgrMcGrpMacFilterId_Object = MibTableColumn
tlsEgrMcGrpMacFilterId = _TlsEgrMcGrpMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 8),
    _TlsEgrMcGrpMacFilterId_Type()
)
tlsEgrMcGrpMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpMacFilterId.setStatus("current")


class _TlsEgrMcGrpIpFilterId_Type(TFilterID):
    """Custom type tlsEgrMcGrpIpFilterId based on TFilterID"""
    defaultValue = 0


_TlsEgrMcGrpIpFilterId_Object = MibTableColumn
tlsEgrMcGrpIpFilterId = _TlsEgrMcGrpIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 9),
    _TlsEgrMcGrpIpFilterId_Type()
)
tlsEgrMcGrpIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpIpFilterId.setStatus("current")


class _TlsEgrMcGrpIpv6FilterId_Type(TFilterID):
    """Custom type tlsEgrMcGrpIpv6FilterId based on TFilterID"""
    defaultValue = 0


_TlsEgrMcGrpIpv6FilterId_Object = MibTableColumn
tlsEgrMcGrpIpv6FilterId = _TlsEgrMcGrpIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 10),
    _TlsEgrMcGrpIpv6FilterId_Type()
)
tlsEgrMcGrpIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpIpv6FilterId.setStatus("current")


class _TlsEgrMcGrpQinqEtherType_Type(Unsigned32):
    """Custom type tlsEgrMcGrpQinqEtherType based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TlsEgrMcGrpQinqEtherType_Type.__name__ = "Unsigned32"
_TlsEgrMcGrpQinqEtherType_Object = MibTableColumn
tlsEgrMcGrpQinqEtherType = _TlsEgrMcGrpQinqEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 11),
    _TlsEgrMcGrpQinqEtherType_Type()
)
tlsEgrMcGrpQinqEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpQinqEtherType.setStatus("current")


class _TlsEgrMcGrpQinqFixedTagPosition_Type(Integer32):
    """Custom type tlsEgrMcGrpQinqFixedTagPosition based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bottomTag", 3),
          ("topTag", 2))
    )


_TlsEgrMcGrpQinqFixedTagPosition_Type.__name__ = "Integer32"
_TlsEgrMcGrpQinqFixedTagPosition_Object = MibTableColumn
tlsEgrMcGrpQinqFixedTagPosition = _TlsEgrMcGrpQinqFixedTagPosition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 12),
    _TlsEgrMcGrpQinqFixedTagPosition_Type()
)
tlsEgrMcGrpQinqFixedTagPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpQinqFixedTagPosition.setStatus("current")


class _TlsEgrMcGrpAdminQinqFixedTagVal_Type(Unsigned32):
    """Custom type tlsEgrMcGrpAdminQinqFixedTagVal based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_TlsEgrMcGrpAdminQinqFixedTagVal_Type.__name__ = "Unsigned32"
_TlsEgrMcGrpAdminQinqFixedTagVal_Object = MibTableColumn
tlsEgrMcGrpAdminQinqFixedTagVal = _TlsEgrMcGrpAdminQinqFixedTagVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 13),
    _TlsEgrMcGrpAdminQinqFixedTagVal_Type()
)
tlsEgrMcGrpAdminQinqFixedTagVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsEgrMcGrpAdminQinqFixedTagVal.setStatus("current")
_TlsEgrMcGrpOperQinqFixedTagVal_Type = Unsigned32
_TlsEgrMcGrpOperQinqFixedTagVal_Object = MibTableColumn
tlsEgrMcGrpOperQinqFixedTagVal = _TlsEgrMcGrpOperQinqFixedTagVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 14, 1, 14),
    _TlsEgrMcGrpOperQinqFixedTagVal_Type()
)
tlsEgrMcGrpOperQinqFixedTagVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsEgrMcGrpOperQinqFixedTagVal.setStatus("current")
_SvcDhcpLeaseStateTable_Object = MibTable
svcDhcpLeaseStateTable = _SvcDhcpLeaseStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateTable.setStatus("obsolete")
_SvcDhcpLeaseStateEntry_Object = MibTableRow
svcDhcpLeaseStateEntry = _SvcDhcpLeaseStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1)
)
svcDhcpLeaseStateEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddr"),
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateEntry.setStatus("obsolete")
_SvcDhcpLseStateCiAddrType_Type = InetAddressType
_SvcDhcpLseStateCiAddrType_Object = MibTableColumn
svcDhcpLseStateCiAddrType = _SvcDhcpLseStateCiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 1),
    _SvcDhcpLseStateCiAddrType_Type()
)
svcDhcpLseStateCiAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLseStateCiAddrType.setStatus("obsolete")
_SvcDhcpLseStateCiAddr_Type = InetAddress
_SvcDhcpLseStateCiAddr_Object = MibTableColumn
svcDhcpLseStateCiAddr = _SvcDhcpLseStateCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 2),
    _SvcDhcpLseStateCiAddr_Type()
)
svcDhcpLseStateCiAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLseStateCiAddr.setStatus("obsolete")


class _SvcDhcpLseStateLocale_Type(Integer32):
    """Custom type svcDhcpLseStateLocale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("sdp", 2))
    )


_SvcDhcpLseStateLocale_Type.__name__ = "Integer32"
_SvcDhcpLseStateLocale_Object = MibTableColumn
svcDhcpLseStateLocale = _SvcDhcpLseStateLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 3),
    _SvcDhcpLseStateLocale_Type()
)
svcDhcpLseStateLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateLocale.setStatus("obsolete")
_SvcDhcpLseStatePortId_Type = TmnxPortID
_SvcDhcpLseStatePortId_Object = MibTableColumn
svcDhcpLseStatePortId = _SvcDhcpLseStatePortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 4),
    _SvcDhcpLseStatePortId_Type()
)
svcDhcpLseStatePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePortId.setStatus("obsolete")
_SvcDhcpLseStateEncapValue_Type = TmnxEncapVal
_SvcDhcpLseStateEncapValue_Object = MibTableColumn
svcDhcpLseStateEncapValue = _SvcDhcpLseStateEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 5),
    _SvcDhcpLseStateEncapValue_Type()
)
svcDhcpLseStateEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateEncapValue.setStatus("obsolete")
_SvcDhcpLseStateSdpId_Type = SdpId
_SvcDhcpLseStateSdpId_Object = MibTableColumn
svcDhcpLseStateSdpId = _SvcDhcpLseStateSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 6),
    _SvcDhcpLseStateSdpId_Type()
)
svcDhcpLseStateSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSdpId.setStatus("obsolete")
_SvcDhcpLseStateVcId_Type = Unsigned32
_SvcDhcpLseStateVcId_Object = MibTableColumn
svcDhcpLseStateVcId = _SvcDhcpLseStateVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 7),
    _SvcDhcpLseStateVcId_Type()
)
svcDhcpLseStateVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateVcId.setStatus("obsolete")
_SvcDhcpLseStateChAddr_Type = MacAddress
_SvcDhcpLseStateChAddr_Object = MibTableColumn
svcDhcpLseStateChAddr = _SvcDhcpLseStateChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 8),
    _SvcDhcpLseStateChAddr_Type()
)
svcDhcpLseStateChAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateChAddr.setStatus("obsolete")
_SvcDhcpLseStateRemainLseTime_Type = Unsigned32
_SvcDhcpLseStateRemainLseTime_Object = MibTableColumn
svcDhcpLseStateRemainLseTime = _SvcDhcpLseStateRemainLseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 9),
    _SvcDhcpLseStateRemainLseTime_Type()
)
svcDhcpLseStateRemainLseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateRemainLseTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    svcDhcpLseStateRemainLseTime.setUnits("seconds")
_SvcDhcpLseStateOption82_Type = OctetString
_SvcDhcpLseStateOption82_Object = MibTableColumn
svcDhcpLseStateOption82 = _SvcDhcpLseStateOption82_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 10),
    _SvcDhcpLseStateOption82_Type()
)
svcDhcpLseStateOption82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateOption82.setStatus("obsolete")
_SvcDhcpLseStatePersistKey_Type = Unsigned32
_SvcDhcpLseStatePersistKey_Object = MibTableColumn
svcDhcpLseStatePersistKey = _SvcDhcpLseStatePersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 11),
    _SvcDhcpLseStatePersistKey_Type()
)
svcDhcpLseStatePersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePersistKey.setStatus("obsolete")
_SvcDhcpLseStateSubscrIdent_Type = DisplayString
_SvcDhcpLseStateSubscrIdent_Object = MibTableColumn
svcDhcpLseStateSubscrIdent = _SvcDhcpLseStateSubscrIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 12),
    _SvcDhcpLseStateSubscrIdent_Type()
)
svcDhcpLseStateSubscrIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSubscrIdent.setStatus("obsolete")
_SvcDhcpLseStateSubProfString_Type = DisplayString
_SvcDhcpLseStateSubProfString_Object = MibTableColumn
svcDhcpLseStateSubProfString = _SvcDhcpLseStateSubProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 13),
    _SvcDhcpLseStateSubProfString_Type()
)
svcDhcpLseStateSubProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSubProfString.setStatus("obsolete")
_SvcDhcpLseStateSlaProfString_Type = DisplayString
_SvcDhcpLseStateSlaProfString_Object = MibTableColumn
svcDhcpLseStateSlaProfString = _SvcDhcpLseStateSlaProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 14),
    _SvcDhcpLseStateSlaProfString_Type()
)
svcDhcpLseStateSlaProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSlaProfString.setStatus("obsolete")


class _SvcDhcpLseStateShcvOperState_Type(Integer32):
    """Custom type svcDhcpLseStateShcvOperState based on Integer32"""
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
        *(("disabled", 1),
          ("down", 3),
          ("undefined", 2),
          ("up", 4))
    )


_SvcDhcpLseStateShcvOperState_Type.__name__ = "Integer32"
_SvcDhcpLseStateShcvOperState_Object = MibTableColumn
svcDhcpLseStateShcvOperState = _SvcDhcpLseStateShcvOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 15),
    _SvcDhcpLseStateShcvOperState_Type()
)
svcDhcpLseStateShcvOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateShcvOperState.setStatus("obsolete")
_SvcDhcpLseStateShcvChecks_Type = Unsigned32
_SvcDhcpLseStateShcvChecks_Object = MibTableColumn
svcDhcpLseStateShcvChecks = _SvcDhcpLseStateShcvChecks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 16),
    _SvcDhcpLseStateShcvChecks_Type()
)
svcDhcpLseStateShcvChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateShcvChecks.setStatus("obsolete")
_SvcDhcpLseStateShcvReplies_Type = Unsigned32
_SvcDhcpLseStateShcvReplies_Object = MibTableColumn
svcDhcpLseStateShcvReplies = _SvcDhcpLseStateShcvReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 17),
    _SvcDhcpLseStateShcvReplies_Type()
)
svcDhcpLseStateShcvReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateShcvReplies.setStatus("obsolete")
_SvcDhcpLseStateShcvReplyTime_Type = TimeStamp
_SvcDhcpLseStateShcvReplyTime_Object = MibTableColumn
svcDhcpLseStateShcvReplyTime = _SvcDhcpLseStateShcvReplyTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 18),
    _SvcDhcpLseStateShcvReplyTime_Type()
)
svcDhcpLseStateShcvReplyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateShcvReplyTime.setStatus("obsolete")
_SvcDhcpLseStateClientId_Type = OctetString
_SvcDhcpLseStateClientId_Object = MibTableColumn
svcDhcpLseStateClientId = _SvcDhcpLseStateClientId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 19),
    _SvcDhcpLseStateClientId_Type()
)
svcDhcpLseStateClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateClientId.setStatus("obsolete")
_SvcDhcpLseStateIAID_Type = Unsigned32
_SvcDhcpLseStateIAID_Object = MibTableColumn
svcDhcpLseStateIAID = _SvcDhcpLseStateIAID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 20),
    _SvcDhcpLseStateIAID_Type()
)
svcDhcpLseStateIAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateIAID.setStatus("obsolete")
_SvcDhcpLseStateIAIDType_Type = IAIDType
_SvcDhcpLseStateIAIDType_Object = MibTableColumn
svcDhcpLseStateIAIDType = _SvcDhcpLseStateIAIDType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 21),
    _SvcDhcpLseStateIAIDType_Type()
)
svcDhcpLseStateIAIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateIAIDType.setStatus("obsolete")


class _SvcDhcpLseStateCiAddrMaskLen_Type(Unsigned32):
    """Custom type svcDhcpLseStateCiAddrMaskLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SvcDhcpLseStateCiAddrMaskLen_Type.__name__ = "Unsigned32"
_SvcDhcpLseStateCiAddrMaskLen_Object = MibTableColumn
svcDhcpLseStateCiAddrMaskLen = _SvcDhcpLseStateCiAddrMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 22),
    _SvcDhcpLseStateCiAddrMaskLen_Type()
)
svcDhcpLseStateCiAddrMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateCiAddrMaskLen.setStatus("obsolete")
_SvcDhcpLseStateRetailerSvcId_Type = TmnxServId
_SvcDhcpLseStateRetailerSvcId_Object = MibTableColumn
svcDhcpLseStateRetailerSvcId = _SvcDhcpLseStateRetailerSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 23),
    _SvcDhcpLseStateRetailerSvcId_Type()
)
svcDhcpLseStateRetailerSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateRetailerSvcId.setStatus("obsolete")
_SvcDhcpLseStateRetailerIf_Type = InterfaceIndexOrZero
_SvcDhcpLseStateRetailerIf_Object = MibTableColumn
svcDhcpLseStateRetailerIf = _SvcDhcpLseStateRetailerIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 24),
    _SvcDhcpLseStateRetailerIf_Type()
)
svcDhcpLseStateRetailerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateRetailerIf.setStatus("obsolete")


class _SvcDhcpLseStateAncpString_Type(DisplayString):
    """Custom type svcDhcpLseStateAncpString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_SvcDhcpLseStateAncpString_Type.__name__ = "DisplayString"
_SvcDhcpLseStateAncpString_Object = MibTableColumn
svcDhcpLseStateAncpString = _SvcDhcpLseStateAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 25),
    _SvcDhcpLseStateAncpString_Type()
)
svcDhcpLseStateAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateAncpString.setStatus("obsolete")
_SvcDhcpLseStateFramedIpNetMaskTp_Type = InetAddressType
_SvcDhcpLseStateFramedIpNetMaskTp_Object = MibTableColumn
svcDhcpLseStateFramedIpNetMaskTp = _SvcDhcpLseStateFramedIpNetMaskTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 26),
    _SvcDhcpLseStateFramedIpNetMaskTp_Type()
)
svcDhcpLseStateFramedIpNetMaskTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateFramedIpNetMaskTp.setStatus("obsolete")
_SvcDhcpLseStateFramedIpNetMask_Type = InetAddress
_SvcDhcpLseStateFramedIpNetMask_Object = MibTableColumn
svcDhcpLseStateFramedIpNetMask = _SvcDhcpLseStateFramedIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 27),
    _SvcDhcpLseStateFramedIpNetMask_Type()
)
svcDhcpLseStateFramedIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateFramedIpNetMask.setStatus("obsolete")
_SvcDhcpLseStateBCastIpAddrType_Type = InetAddressType
_SvcDhcpLseStateBCastIpAddrType_Object = MibTableColumn
svcDhcpLseStateBCastIpAddrType = _SvcDhcpLseStateBCastIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 28),
    _SvcDhcpLseStateBCastIpAddrType_Type()
)
svcDhcpLseStateBCastIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBCastIpAddrType.setStatus("obsolete")
_SvcDhcpLseStateBCastIpAddr_Type = InetAddress
_SvcDhcpLseStateBCastIpAddr_Object = MibTableColumn
svcDhcpLseStateBCastIpAddr = _SvcDhcpLseStateBCastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 29),
    _SvcDhcpLseStateBCastIpAddr_Type()
)
svcDhcpLseStateBCastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBCastIpAddr.setStatus("obsolete")
_SvcDhcpLseStateDefaultRouterTp_Type = InetAddressType
_SvcDhcpLseStateDefaultRouterTp_Object = MibTableColumn
svcDhcpLseStateDefaultRouterTp = _SvcDhcpLseStateDefaultRouterTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 30),
    _SvcDhcpLseStateDefaultRouterTp_Type()
)
svcDhcpLseStateDefaultRouterTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDefaultRouterTp.setStatus("obsolete")
_SvcDhcpLseStateDefaultRouter_Type = InetAddress
_SvcDhcpLseStateDefaultRouter_Object = MibTableColumn
svcDhcpLseStateDefaultRouter = _SvcDhcpLseStateDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 31),
    _SvcDhcpLseStateDefaultRouter_Type()
)
svcDhcpLseStateDefaultRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDefaultRouter.setStatus("obsolete")
_SvcDhcpLseStatePrimaryDnsType_Type = InetAddressType
_SvcDhcpLseStatePrimaryDnsType_Object = MibTableColumn
svcDhcpLseStatePrimaryDnsType = _SvcDhcpLseStatePrimaryDnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 32),
    _SvcDhcpLseStatePrimaryDnsType_Type()
)
svcDhcpLseStatePrimaryDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePrimaryDnsType.setStatus("obsolete")
_SvcDhcpLseStatePrimaryDns_Type = InetAddress
_SvcDhcpLseStatePrimaryDns_Object = MibTableColumn
svcDhcpLseStatePrimaryDns = _SvcDhcpLseStatePrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 33),
    _SvcDhcpLseStatePrimaryDns_Type()
)
svcDhcpLseStatePrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePrimaryDns.setStatus("obsolete")
_SvcDhcpLseStateSecondaryDnsType_Type = InetAddressType
_SvcDhcpLseStateSecondaryDnsType_Object = MibTableColumn
svcDhcpLseStateSecondaryDnsType = _SvcDhcpLseStateSecondaryDnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 34),
    _SvcDhcpLseStateSecondaryDnsType_Type()
)
svcDhcpLseStateSecondaryDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSecondaryDnsType.setStatus("obsolete")
_SvcDhcpLseStateSecondaryDns_Type = InetAddress
_SvcDhcpLseStateSecondaryDns_Object = MibTableColumn
svcDhcpLseStateSecondaryDns = _SvcDhcpLseStateSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 35),
    _SvcDhcpLseStateSecondaryDns_Type()
)
svcDhcpLseStateSecondaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSecondaryDns.setStatus("obsolete")


class _SvcDhcpLseStateSessionTimeout_Type(Unsigned32):
    """Custom type svcDhcpLseStateSessionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SvcDhcpLseStateSessionTimeout_Type.__name__ = "Unsigned32"
_SvcDhcpLseStateSessionTimeout_Object = MibTableColumn
svcDhcpLseStateSessionTimeout = _SvcDhcpLseStateSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 36),
    _SvcDhcpLseStateSessionTimeout_Type()
)
svcDhcpLseStateSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSessionTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    svcDhcpLseStateSessionTimeout.setUnits("seconds")
_SvcDhcpLseStateServerLeaseStart_Type = DateAndTime
_SvcDhcpLseStateServerLeaseStart_Object = MibTableColumn
svcDhcpLseStateServerLeaseStart = _SvcDhcpLseStateServerLeaseStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 37),
    _SvcDhcpLseStateServerLeaseStart_Type()
)
svcDhcpLseStateServerLeaseStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateServerLeaseStart.setStatus("obsolete")
_SvcDhcpLseStateServerLastRenew_Type = DateAndTime
_SvcDhcpLseStateServerLastRenew_Object = MibTableColumn
svcDhcpLseStateServerLastRenew = _SvcDhcpLseStateServerLastRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 38),
    _SvcDhcpLseStateServerLastRenew_Type()
)
svcDhcpLseStateServerLastRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateServerLastRenew.setStatus("obsolete")
_SvcDhcpLseStateServerLeaseEnd_Type = DateAndTime
_SvcDhcpLseStateServerLeaseEnd_Object = MibTableColumn
svcDhcpLseStateServerLeaseEnd = _SvcDhcpLseStateServerLeaseEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 39),
    _SvcDhcpLseStateServerLeaseEnd_Type()
)
svcDhcpLseStateServerLeaseEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateServerLeaseEnd.setStatus("obsolete")
_SvcDhcpLseStateDhcpServerAddrType_Type = InetAddressType
_SvcDhcpLseStateDhcpServerAddrType_Object = MibTableColumn
svcDhcpLseStateDhcpServerAddrType = _SvcDhcpLseStateDhcpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 40),
    _SvcDhcpLseStateDhcpServerAddrType_Type()
)
svcDhcpLseStateDhcpServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDhcpServerAddrType.setStatus("obsolete")
_SvcDhcpLseStateDhcpServerAddr_Type = InetAddress
_SvcDhcpLseStateDhcpServerAddr_Object = MibTableColumn
svcDhcpLseStateDhcpServerAddr = _SvcDhcpLseStateDhcpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 41),
    _SvcDhcpLseStateDhcpServerAddr_Type()
)
svcDhcpLseStateDhcpServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDhcpServerAddr.setStatus("obsolete")
_SvcDhcpLseStateOriginSubscrId_Type = DhcpLseStateInfoOrigin
_SvcDhcpLseStateOriginSubscrId_Object = MibTableColumn
svcDhcpLseStateOriginSubscrId = _SvcDhcpLseStateOriginSubscrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 42),
    _SvcDhcpLseStateOriginSubscrId_Type()
)
svcDhcpLseStateOriginSubscrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateOriginSubscrId.setStatus("obsolete")
_SvcDhcpLseStateOriginStrings_Type = DhcpLseStateInfoOrigin
_SvcDhcpLseStateOriginStrings_Object = MibTableColumn
svcDhcpLseStateOriginStrings = _SvcDhcpLseStateOriginStrings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 43),
    _SvcDhcpLseStateOriginStrings_Type()
)
svcDhcpLseStateOriginStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateOriginStrings.setStatus("obsolete")
_SvcDhcpLseStateOriginLeaseInfo_Type = DhcpLseStateInfoOrigin
_SvcDhcpLseStateOriginLeaseInfo_Object = MibTableColumn
svcDhcpLseStateOriginLeaseInfo = _SvcDhcpLseStateOriginLeaseInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 44),
    _SvcDhcpLseStateOriginLeaseInfo_Type()
)
svcDhcpLseStateOriginLeaseInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateOriginLeaseInfo.setStatus("obsolete")
_SvcDhcpLseStateDhcpClientAddrType_Type = InetAddressType
_SvcDhcpLseStateDhcpClientAddrType_Object = MibTableColumn
svcDhcpLseStateDhcpClientAddrType = _SvcDhcpLseStateDhcpClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 45),
    _SvcDhcpLseStateDhcpClientAddrType_Type()
)
svcDhcpLseStateDhcpClientAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDhcpClientAddrType.setStatus("obsolete")
_SvcDhcpLseStateDhcpClientAddr_Type = InetAddress
_SvcDhcpLseStateDhcpClientAddr_Object = MibTableColumn
svcDhcpLseStateDhcpClientAddr = _SvcDhcpLseStateDhcpClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 46),
    _SvcDhcpLseStateDhcpClientAddr_Type()
)
svcDhcpLseStateDhcpClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDhcpClientAddr.setStatus("obsolete")
_SvcDhcpLseStateLeaseSplitActive_Type = TruthValue
_SvcDhcpLseStateLeaseSplitActive_Object = MibTableColumn
svcDhcpLseStateLeaseSplitActive = _SvcDhcpLseStateLeaseSplitActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 47),
    _SvcDhcpLseStateLeaseSplitActive_Type()
)
svcDhcpLseStateLeaseSplitActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateLeaseSplitActive.setStatus("obsolete")


class _SvcDhcpLseStateInterDestId_Type(DisplayString):
    """Custom type svcDhcpLseStateInterDestId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SvcDhcpLseStateInterDestId_Type.__name__ = "DisplayString"
_SvcDhcpLseStateInterDestId_Object = MibTableColumn
svcDhcpLseStateInterDestId = _SvcDhcpLseStateInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 48),
    _SvcDhcpLseStateInterDestId_Type()
)
svcDhcpLseStateInterDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateInterDestId.setStatus("obsolete")
_SvcDhcpLseStatePrimaryNbnsType_Type = InetAddressType
_SvcDhcpLseStatePrimaryNbnsType_Object = MibTableColumn
svcDhcpLseStatePrimaryNbnsType = _SvcDhcpLseStatePrimaryNbnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 49),
    _SvcDhcpLseStatePrimaryNbnsType_Type()
)
svcDhcpLseStatePrimaryNbnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePrimaryNbnsType.setStatus("obsolete")
_SvcDhcpLseStatePrimaryNbns_Type = InetAddress
_SvcDhcpLseStatePrimaryNbns_Object = MibTableColumn
svcDhcpLseStatePrimaryNbns = _SvcDhcpLseStatePrimaryNbns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 50),
    _SvcDhcpLseStatePrimaryNbns_Type()
)
svcDhcpLseStatePrimaryNbns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePrimaryNbns.setStatus("obsolete")
_SvcDhcpLseStateSecondaryNbnsType_Type = InetAddressType
_SvcDhcpLseStateSecondaryNbnsType_Object = MibTableColumn
svcDhcpLseStateSecondaryNbnsType = _SvcDhcpLseStateSecondaryNbnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 51),
    _SvcDhcpLseStateSecondaryNbnsType_Type()
)
svcDhcpLseStateSecondaryNbnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSecondaryNbnsType.setStatus("obsolete")
_SvcDhcpLseStateSecondaryNbns_Type = InetAddress
_SvcDhcpLseStateSecondaryNbns_Object = MibTableColumn
svcDhcpLseStateSecondaryNbns = _SvcDhcpLseStateSecondaryNbns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 52),
    _SvcDhcpLseStateSecondaryNbns_Type()
)
svcDhcpLseStateSecondaryNbns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSecondaryNbns.setStatus("obsolete")
_SvcDhcpLseStateAppProfString_Type = DisplayString
_SvcDhcpLseStateAppProfString_Object = MibTableColumn
svcDhcpLseStateAppProfString = _SvcDhcpLseStateAppProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 53),
    _SvcDhcpLseStateAppProfString_Type()
)
svcDhcpLseStateAppProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateAppProfString.setStatus("obsolete")
_SvcDhcpLseStateNextHopMacAddr_Type = MacAddress
_SvcDhcpLseStateNextHopMacAddr_Object = MibTableColumn
svcDhcpLseStateNextHopMacAddr = _SvcDhcpLseStateNextHopMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 54),
    _SvcDhcpLseStateNextHopMacAddr_Type()
)
svcDhcpLseStateNextHopMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateNextHopMacAddr.setStatus("obsolete")
_SvcDhcpLseStateCategoryMapName_Type = TNamedItemOrEmpty
_SvcDhcpLseStateCategoryMapName_Object = MibTableColumn
svcDhcpLseStateCategoryMapName = _SvcDhcpLseStateCategoryMapName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 55),
    _SvcDhcpLseStateCategoryMapName_Type()
)
svcDhcpLseStateCategoryMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateCategoryMapName.setStatus("obsolete")
_SvcDhcpLseStateNakNextRenew_Type = TruthValue
_SvcDhcpLseStateNakNextRenew_Object = MibTableColumn
svcDhcpLseStateNakNextRenew = _SvcDhcpLseStateNakNextRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 56),
    _SvcDhcpLseStateNakNextRenew_Type()
)
svcDhcpLseStateNakNextRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateNakNextRenew.setStatus("obsolete")


class _SvcDhcpLseStateRadiusClassAttr_Type(OctetString):
    """Custom type svcDhcpLseStateRadiusClassAttr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcDhcpLseStateRadiusClassAttr_Type.__name__ = "OctetString"
_SvcDhcpLseStateRadiusClassAttr_Object = MibTableColumn
svcDhcpLseStateRadiusClassAttr = _SvcDhcpLseStateRadiusClassAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 57),
    _SvcDhcpLseStateRadiusClassAttr_Type()
)
svcDhcpLseStateRadiusClassAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateRadiusClassAttr.setStatus("obsolete")


class _SvcDhcpLseStateRadiusUserName_Type(DisplayString):
    """Custom type svcDhcpLseStateRadiusUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SvcDhcpLseStateRadiusUserName_Type.__name__ = "DisplayString"
_SvcDhcpLseStateRadiusUserName_Object = MibTableColumn
svcDhcpLseStateRadiusUserName = _SvcDhcpLseStateRadiusUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 58),
    _SvcDhcpLseStateRadiusUserName_Type()
)
svcDhcpLseStateRadiusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateRadiusUserName.setStatus("obsolete")
_TlsProtectedMacTable_Object = MibTable
tlsProtectedMacTable = _TlsProtectedMacTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 17)
)
if mibBuilder.loadTexts:
    tlsProtectedMacTable.setStatus("current")
_TlsProtectedMacEntry_Object = MibTableRow
tlsProtectedMacEntry = _TlsProtectedMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 17, 1)
)
tlsProtectedMacEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsProtMacAddress"),
)
if mibBuilder.loadTexts:
    tlsProtectedMacEntry.setStatus("current")
_TlsProtMacAddress_Type = MacAddress
_TlsProtMacAddress_Object = MibTableColumn
tlsProtMacAddress = _TlsProtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 17, 1, 1),
    _TlsProtMacAddress_Type()
)
tlsProtMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsProtMacAddress.setStatus("current")
_TlsProtMacRowStatus_Type = RowStatus
_TlsProtMacRowStatus_Object = MibTableColumn
tlsProtMacRowStatus = _TlsProtMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 17, 1, 2),
    _TlsProtMacRowStatus_Type()
)
tlsProtMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tlsProtMacRowStatus.setStatus("current")
_TlsProtMacLastMgmtChange_Type = TimeStamp
_TlsProtMacLastMgmtChange_Object = MibTableColumn
tlsProtMacLastMgmtChange = _TlsProtMacLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 17, 1, 3),
    _TlsProtMacLastMgmtChange_Type()
)
tlsProtMacLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsProtMacLastMgmtChange.setStatus("current")
_SvcDhcpLeaseStateModifyTable_Object = MibTable
svcDhcpLeaseStateModifyTable = _SvcDhcpLeaseStateModifyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateModifyTable.setStatus("obsolete")
_SvcDhcpLeaseStateModifyEntry_Object = MibTableRow
svcDhcpLeaseStateModifyEntry = _SvcDhcpLeaseStateModifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18, 1)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateModifyEntry.setStatus("obsolete")


class _SvcDhcpLseStateModifySubIndent_Type(DisplayString):
    """Custom type svcDhcpLseStateModifySubIndent based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SvcDhcpLseStateModifySubIndent_Type.__name__ = "DisplayString"
_SvcDhcpLseStateModifySubIndent_Object = MibTableColumn
svcDhcpLseStateModifySubIndent = _SvcDhcpLseStateModifySubIndent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18, 1, 1),
    _SvcDhcpLseStateModifySubIndent_Type()
)
svcDhcpLseStateModifySubIndent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLseStateModifySubIndent.setStatus("obsolete")


class _SvcDhcpLseStateModifySubProfile_Type(DisplayString):
    """Custom type svcDhcpLseStateModifySubProfile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SvcDhcpLseStateModifySubProfile_Type.__name__ = "DisplayString"
_SvcDhcpLseStateModifySubProfile_Object = MibTableColumn
svcDhcpLseStateModifySubProfile = _SvcDhcpLseStateModifySubProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18, 1, 2),
    _SvcDhcpLseStateModifySubProfile_Type()
)
svcDhcpLseStateModifySubProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLseStateModifySubProfile.setStatus("obsolete")


class _SvcDhcpLseStateModifySlaProfile_Type(DisplayString):
    """Custom type svcDhcpLseStateModifySlaProfile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SvcDhcpLseStateModifySlaProfile_Type.__name__ = "DisplayString"
_SvcDhcpLseStateModifySlaProfile_Object = MibTableColumn
svcDhcpLseStateModifySlaProfile = _SvcDhcpLseStateModifySlaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18, 1, 3),
    _SvcDhcpLseStateModifySlaProfile_Type()
)
svcDhcpLseStateModifySlaProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLseStateModifySlaProfile.setStatus("obsolete")


class _SvcDhcpLseStateEvaluateState_Type(TruthValue):
    """Custom type svcDhcpLseStateEvaluateState based on TruthValue"""


_SvcDhcpLseStateEvaluateState_Object = MibTableColumn
svcDhcpLseStateEvaluateState = _SvcDhcpLseStateEvaluateState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18, 1, 4),
    _SvcDhcpLseStateEvaluateState_Type()
)
svcDhcpLseStateEvaluateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLseStateEvaluateState.setStatus("obsolete")


class _SvcDhcpLseStateModInterDestId_Type(DisplayString):
    """Custom type svcDhcpLseStateModInterDestId based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SvcDhcpLseStateModInterDestId_Type.__name__ = "DisplayString"
_SvcDhcpLseStateModInterDestId_Object = MibTableColumn
svcDhcpLseStateModInterDestId = _SvcDhcpLseStateModInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18, 1, 5),
    _SvcDhcpLseStateModInterDestId_Type()
)
svcDhcpLseStateModInterDestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLseStateModInterDestId.setStatus("obsolete")


class _SvcDhcpLseStateModifyAncpString_Type(TmnxAncpStringOrZero):
    """Custom type svcDhcpLseStateModifyAncpString based on TmnxAncpStringOrZero"""
    defaultHexValue = ""


_SvcDhcpLseStateModifyAncpString_Object = MibTableColumn
svcDhcpLseStateModifyAncpString = _SvcDhcpLseStateModifyAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18, 1, 6),
    _SvcDhcpLseStateModifyAncpString_Type()
)
svcDhcpLseStateModifyAncpString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLseStateModifyAncpString.setStatus("obsolete")


class _SvcDhcpLseStateModifyAppProfile_Type(DisplayString):
    """Custom type svcDhcpLseStateModifyAppProfile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SvcDhcpLseStateModifyAppProfile_Type.__name__ = "DisplayString"
_SvcDhcpLseStateModifyAppProfile_Object = MibTableColumn
svcDhcpLseStateModifyAppProfile = _SvcDhcpLseStateModifyAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18, 1, 7),
    _SvcDhcpLseStateModifyAppProfile_Type()
)
svcDhcpLseStateModifyAppProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLseStateModifyAppProfile.setStatus("obsolete")
_SvcEndPointTable_Object = MibTable
svcEndPointTable = _SvcEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19)
)
if mibBuilder.loadTexts:
    svcEndPointTable.setStatus("current")
_SvcEndPointEntry_Object = MibTableRow
svcEndPointEntry = _SvcEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1)
)
svcEndPointEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcEndPointName"),
)
if mibBuilder.loadTexts:
    svcEndPointEntry.setStatus("current")
_SvcEndPointName_Type = TNamedItem
_SvcEndPointName_Object = MibTableColumn
svcEndPointName = _SvcEndPointName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 1),
    _SvcEndPointName_Type()
)
svcEndPointName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcEndPointName.setStatus("current")
_SvcEndPointRowStatus_Type = RowStatus
_SvcEndPointRowStatus_Object = MibTableColumn
svcEndPointRowStatus = _SvcEndPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 2),
    _SvcEndPointRowStatus_Type()
)
svcEndPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointRowStatus.setStatus("current")
_SvcEndPointDescription_Type = ServObjDesc
_SvcEndPointDescription_Object = MibTableColumn
svcEndPointDescription = _SvcEndPointDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 3),
    _SvcEndPointDescription_Type()
)
svcEndPointDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointDescription.setStatus("current")


class _SvcEndPointRevertTime_Type(Integer32):
    """Custom type svcEndPointRevertTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 600),
    )


_SvcEndPointRevertTime_Type.__name__ = "Integer32"
_SvcEndPointRevertTime_Object = MibTableColumn
svcEndPointRevertTime = _SvcEndPointRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 4),
    _SvcEndPointRevertTime_Type()
)
svcEndPointRevertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointRevertTime.setStatus("current")
if mibBuilder.loadTexts:
    svcEndPointRevertTime.setUnits("seconds")


class _SvcEndPointTxActiveType_Type(Integer32):
    """Custom type svcEndPointTxActiveType based on Integer32"""
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
          ("sap", 1),
          ("sdpBind", 2),
          ("sdpFec", 3))
    )


_SvcEndPointTxActiveType_Type.__name__ = "Integer32"
_SvcEndPointTxActiveType_Object = MibTableColumn
svcEndPointTxActiveType = _SvcEndPointTxActiveType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 5),
    _SvcEndPointTxActiveType_Type()
)
svcEndPointTxActiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEndPointTxActiveType.setStatus("current")
_SvcEndPointTxActivePortId_Type = TmnxPortID
_SvcEndPointTxActivePortId_Object = MibTableColumn
svcEndPointTxActivePortId = _SvcEndPointTxActivePortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 6),
    _SvcEndPointTxActivePortId_Type()
)
svcEndPointTxActivePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEndPointTxActivePortId.setStatus("current")
_SvcEndPointTxActiveEncap_Type = TmnxEncapVal
_SvcEndPointTxActiveEncap_Object = MibTableColumn
svcEndPointTxActiveEncap = _SvcEndPointTxActiveEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 7),
    _SvcEndPointTxActiveEncap_Type()
)
svcEndPointTxActiveEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEndPointTxActiveEncap.setStatus("current")
_SvcEndPointTxActiveSdpId_Type = SdpBindId
_SvcEndPointTxActiveSdpId_Object = MibTableColumn
svcEndPointTxActiveSdpId = _SvcEndPointTxActiveSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 8),
    _SvcEndPointTxActiveSdpId_Type()
)
svcEndPointTxActiveSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEndPointTxActiveSdpId.setStatus("current")


class _SvcEndPointForceSwitchOver_Type(TmnxActionType):
    """Custom type svcEndPointForceSwitchOver based on TmnxActionType"""


_SvcEndPointForceSwitchOver_Object = MibTableColumn
svcEndPointForceSwitchOver = _SvcEndPointForceSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 9),
    _SvcEndPointForceSwitchOver_Type()
)
svcEndPointForceSwitchOver.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointForceSwitchOver.setStatus("current")


class _SvcEndPointForceSwitchOverSdpId_Type(SdpBindId):
    """Custom type svcEndPointForceSwitchOverSdpId based on SdpBindId"""
    defaultHexValue = "0000000000000000"


_SvcEndPointForceSwitchOverSdpId_Object = MibTableColumn
svcEndPointForceSwitchOverSdpId = _SvcEndPointForceSwitchOverSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 10),
    _SvcEndPointForceSwitchOverSdpId_Type()
)
svcEndPointForceSwitchOverSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointForceSwitchOverSdpId.setStatus("current")


class _SvcEndPointActiveHoldDelay_Type(Unsigned32):
    """Custom type svcEndPointActiveHoldDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SvcEndPointActiveHoldDelay_Type.__name__ = "Unsigned32"
_SvcEndPointActiveHoldDelay_Object = MibTableColumn
svcEndPointActiveHoldDelay = _SvcEndPointActiveHoldDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 11),
    _SvcEndPointActiveHoldDelay_Type()
)
svcEndPointActiveHoldDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointActiveHoldDelay.setStatus("current")
if mibBuilder.loadTexts:
    svcEndPointActiveHoldDelay.setUnits("deci-seconds")


class _SvcEndPointIgnoreStandbySig_Type(TruthValue):
    """Custom type svcEndPointIgnoreStandbySig based on TruthValue"""


_SvcEndPointIgnoreStandbySig_Object = MibTableColumn
svcEndPointIgnoreStandbySig = _SvcEndPointIgnoreStandbySig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 12),
    _SvcEndPointIgnoreStandbySig_Type()
)
svcEndPointIgnoreStandbySig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointIgnoreStandbySig.setStatus("current")


class _SvcEndPointMacPinning_Type(TmnxEnabledDisabled):
    """Custom type svcEndPointMacPinning based on TmnxEnabledDisabled"""


_SvcEndPointMacPinning_Object = MibTableColumn
svcEndPointMacPinning = _SvcEndPointMacPinning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 13),
    _SvcEndPointMacPinning_Type()
)
svcEndPointMacPinning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointMacPinning.setStatus("current")


class _SvcEndPointMacLimit_Type(Integer32):
    """Custom type svcEndPointMacLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511999),
    )


_SvcEndPointMacLimit_Type.__name__ = "Integer32"
_SvcEndPointMacLimit_Object = MibTableColumn
svcEndPointMacLimit = _SvcEndPointMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 14),
    _SvcEndPointMacLimit_Type()
)
svcEndPointMacLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointMacLimit.setStatus("current")


class _SvcEndPointSuppressStandbySig_Type(TruthValue):
    """Custom type svcEndPointSuppressStandbySig based on TruthValue"""


_SvcEndPointSuppressStandbySig_Object = MibTableColumn
svcEndPointSuppressStandbySig = _SvcEndPointSuppressStandbySig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 15),
    _SvcEndPointSuppressStandbySig_Type()
)
svcEndPointSuppressStandbySig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointSuppressStandbySig.setStatus("current")


class _SvcEndPointRevertTimeCountDn_Type(Integer32):
    """Custom type svcEndPointRevertTimeCountDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 600),
    )


_SvcEndPointRevertTimeCountDn_Type.__name__ = "Integer32"
_SvcEndPointRevertTimeCountDn_Object = MibTableColumn
svcEndPointRevertTimeCountDn = _SvcEndPointRevertTimeCountDn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 16),
    _SvcEndPointRevertTimeCountDn_Type()
)
svcEndPointRevertTimeCountDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEndPointRevertTimeCountDn.setStatus("current")
if mibBuilder.loadTexts:
    svcEndPointRevertTimeCountDn.setUnits("seconds")
_SvcEndPointTxActiveChangeCount_Type = Counter32
_SvcEndPointTxActiveChangeCount_Object = MibTableColumn
svcEndPointTxActiveChangeCount = _SvcEndPointTxActiveChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 17),
    _SvcEndPointTxActiveChangeCount_Type()
)
svcEndPointTxActiveChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEndPointTxActiveChangeCount.setStatus("current")
_SvcEndPointTxActiveLastChange_Type = TimeStamp
_SvcEndPointTxActiveLastChange_Object = MibTableColumn
svcEndPointTxActiveLastChange = _SvcEndPointTxActiveLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 18),
    _SvcEndPointTxActiveLastChange_Type()
)
svcEndPointTxActiveLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEndPointTxActiveLastChange.setStatus("current")
_SvcEndPointTxActiveUpTime_Type = TimeTicks
_SvcEndPointTxActiveUpTime_Object = MibTableColumn
svcEndPointTxActiveUpTime = _SvcEndPointTxActiveUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 19),
    _SvcEndPointTxActiveUpTime_Type()
)
svcEndPointTxActiveUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEndPointTxActiveUpTime.setStatus("current")


class _SvcEndPointMCEPId_Type(Unsigned32):
    """Custom type svcEndPointMCEPId based on Unsigned32"""
    defaultValue = 0


_SvcEndPointMCEPId_Object = MibTableColumn
svcEndPointMCEPId = _SvcEndPointMCEPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 20),
    _SvcEndPointMCEPId_Type()
)
svcEndPointMCEPId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointMCEPId.setStatus("current")


class _SvcEndPointMCEPPeerAddrType_Type(InetAddressType):
    """Custom type svcEndPointMCEPPeerAddrType based on InetAddressType"""


_SvcEndPointMCEPPeerAddrType_Object = MibTableColumn
svcEndPointMCEPPeerAddrType = _SvcEndPointMCEPPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 21),
    _SvcEndPointMCEPPeerAddrType_Type()
)
svcEndPointMCEPPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointMCEPPeerAddrType.setStatus("current")


class _SvcEndPointMCEPPeerAddr_Type(InetAddress):
    """Custom type svcEndPointMCEPPeerAddr based on InetAddress"""
    defaultHexValue = ""


_SvcEndPointMCEPPeerAddr_Object = MibTableColumn
svcEndPointMCEPPeerAddr = _SvcEndPointMCEPPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 22),
    _SvcEndPointMCEPPeerAddr_Type()
)
svcEndPointMCEPPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointMCEPPeerAddr.setStatus("current")


class _SvcEndPointMCEPPeerName_Type(TNamedItemOrEmpty):
    """Custom type svcEndPointMCEPPeerName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SvcEndPointMCEPPeerName_Object = MibTableColumn
svcEndPointMCEPPeerName = _SvcEndPointMCEPPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 23),
    _SvcEndPointMCEPPeerName_Type()
)
svcEndPointMCEPPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointMCEPPeerName.setStatus("current")


class _SvcEndPointBlockOnMeshFail_Type(TruthValue):
    """Custom type svcEndPointBlockOnMeshFail based on TruthValue"""


_SvcEndPointBlockOnMeshFail_Object = MibTableColumn
svcEndPointBlockOnMeshFail = _SvcEndPointBlockOnMeshFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 24),
    _SvcEndPointBlockOnMeshFail_Type()
)
svcEndPointBlockOnMeshFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointBlockOnMeshFail.setStatus("current")
_SvcEndPointMCEPPsvModeActive_Type = TruthValue
_SvcEndPointMCEPPsvModeActive_Object = MibTableColumn
svcEndPointMCEPPsvModeActive = _SvcEndPointMCEPPsvModeActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 25),
    _SvcEndPointMCEPPsvModeActive_Type()
)
svcEndPointMCEPPsvModeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEndPointMCEPPsvModeActive.setStatus("current")


class _SvcEndPointStandbySigMaster_Type(TruthValue):
    """Custom type svcEndPointStandbySigMaster based on TruthValue"""


_SvcEndPointStandbySigMaster_Object = MibTableColumn
svcEndPointStandbySigMaster = _SvcEndPointStandbySigMaster_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 26),
    _SvcEndPointStandbySigMaster_Type()
)
svcEndPointStandbySigMaster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointStandbySigMaster.setStatus("current")


class _SvcEndPointStandbySigSlave_Type(TruthValue):
    """Custom type svcEndPointStandbySigSlave based on TruthValue"""


_SvcEndPointStandbySigSlave_Object = MibTableColumn
svcEndPointStandbySigSlave = _SvcEndPointStandbySigSlave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 27),
    _SvcEndPointStandbySigSlave_Type()
)
svcEndPointStandbySigSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointStandbySigSlave.setStatus("current")


class _SvcEndPointForceSwitchOvrSdpFec_Type(TmnxSpokeSdpIdOrZero):
    """Custom type svcEndPointForceSwitchOvrSdpFec based on TmnxSpokeSdpIdOrZero"""
    defaultValue = 0


_SvcEndPointForceSwitchOvrSdpFec_Object = MibTableColumn
svcEndPointForceSwitchOvrSdpFec = _SvcEndPointForceSwitchOvrSdpFec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 28),
    _SvcEndPointForceSwitchOvrSdpFec_Type()
)
svcEndPointForceSwitchOvrSdpFec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointForceSwitchOvrSdpFec.setStatus("current")
_SvcEndPointTxActiveSdpFec_Type = TmnxSpokeSdpIdOrZero
_SvcEndPointTxActiveSdpFec_Object = MibTableColumn
svcEndPointTxActiveSdpFec = _SvcEndPointTxActiveSdpFec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 29),
    _SvcEndPointTxActiveSdpFec_Type()
)
svcEndPointTxActiveSdpFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEndPointTxActiveSdpFec.setStatus("current")


class _SvcEndPointRestProtSrcMac_Type(TruthValue):
    """Custom type svcEndPointRestProtSrcMac based on TruthValue"""


_SvcEndPointRestProtSrcMac_Object = MibTableColumn
svcEndPointRestProtSrcMac = _SvcEndPointRestProtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 30),
    _SvcEndPointRestProtSrcMac_Type()
)
svcEndPointRestProtSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointRestProtSrcMac.setStatus("current")


class _SvcEndPointRestProtSrcMacAction_Type(Integer32):
    """Custom type svcEndPointRestProtSrcMacAction based on Integer32"""
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
        *(("alarmOnly", 2),
          ("disable", 1),
          ("discardFrame", 3))
    )


_SvcEndPointRestProtSrcMacAction_Type.__name__ = "Integer32"
_SvcEndPointRestProtSrcMacAction_Object = MibTableColumn
svcEndPointRestProtSrcMacAction = _SvcEndPointRestProtSrcMacAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 31),
    _SvcEndPointRestProtSrcMacAction_Type()
)
svcEndPointRestProtSrcMacAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointRestProtSrcMacAction.setStatus("current")


class _SvcEndPointAutoLearnMacProtect_Type(TruthValue):
    """Custom type svcEndPointAutoLearnMacProtect based on TruthValue"""


_SvcEndPointAutoLearnMacProtect_Object = MibTableColumn
svcEndPointAutoLearnMacProtect = _SvcEndPointAutoLearnMacProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 19, 1, 32),
    _SvcEndPointAutoLearnMacProtect_Type()
)
svcEndPointAutoLearnMacProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEndPointAutoLearnMacProtect.setStatus("current")
_IesGrpIfTable_Object = MibTable
iesGrpIfTable = _IesGrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 21)
)
if mibBuilder.loadTexts:
    iesGrpIfTable.setStatus("current")
_IesGrpIfEntry_Object = MibTableRow
iesGrpIfEntry = _IesGrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 21, 1)
)
iesGrpIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    iesGrpIfEntry.setStatus("current")


class _IesGrpIfRedInterface_Type(InterfaceIndexOrZero):
    """Custom type iesGrpIfRedInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_IesGrpIfRedInterface_Object = MibTableColumn
iesGrpIfRedInterface = _IesGrpIfRedInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 21, 1, 1),
    _IesGrpIfRedInterface_Type()
)
iesGrpIfRedInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesGrpIfRedInterface.setStatus("current")


class _IesGrpIfOperUpWhileEmpty_Type(TruthValue):
    """Custom type iesGrpIfOperUpWhileEmpty based on TruthValue"""


_IesGrpIfOperUpWhileEmpty_Object = MibTableColumn
iesGrpIfOperUpWhileEmpty = _IesGrpIfOperUpWhileEmpty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 21, 1, 2),
    _IesGrpIfOperUpWhileEmpty_Type()
)
iesGrpIfOperUpWhileEmpty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesGrpIfOperUpWhileEmpty.setStatus("current")
_IesGrpIfPolicyControl_Type = TNamedItemOrEmpty
_IesGrpIfPolicyControl_Object = MibTableColumn
iesGrpIfPolicyControl = _IesGrpIfPolicyControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 21, 1, 3),
    _IesGrpIfPolicyControl_Type()
)
iesGrpIfPolicyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesGrpIfPolicyControl.setStatus("current")
_SvcPEDiscoveryPolicyTable_Object = MibTable
svcPEDiscoveryPolicyTable = _SvcPEDiscoveryPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 22)
)
if mibBuilder.loadTexts:
    svcPEDiscoveryPolicyTable.setStatus("current")
_SvcPEDiscoveryPolicyEntry_Object = MibTableRow
svcPEDiscoveryPolicyEntry = _SvcPEDiscoveryPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 22, 1)
)
svcPEDiscoveryPolicyEntry.setIndexNames(
    (1, "TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyName"),
)
if mibBuilder.loadTexts:
    svcPEDiscoveryPolicyEntry.setStatus("current")
_SvcPEDiscoveryPolicyName_Type = TNamedItem
_SvcPEDiscoveryPolicyName_Object = MibTableColumn
svcPEDiscoveryPolicyName = _SvcPEDiscoveryPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 22, 1, 1),
    _SvcPEDiscoveryPolicyName_Type()
)
svcPEDiscoveryPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPEDiscoveryPolicyName.setStatus("current")
_SvcPEDiscoveryPolicyRowStatus_Type = RowStatus
_SvcPEDiscoveryPolicyRowStatus_Object = MibTableColumn
svcPEDiscoveryPolicyRowStatus = _SvcPEDiscoveryPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 22, 1, 2),
    _SvcPEDiscoveryPolicyRowStatus_Type()
)
svcPEDiscoveryPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPEDiscoveryPolicyRowStatus.setStatus("current")


class _SvcPEDiscoveryPolicyPassword_Type(OctetString):
    """Custom type svcPEDiscoveryPolicyPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SvcPEDiscoveryPolicyPassword_Type.__name__ = "OctetString"
_SvcPEDiscoveryPolicyPassword_Object = MibTableColumn
svcPEDiscoveryPolicyPassword = _SvcPEDiscoveryPolicyPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 22, 1, 3),
    _SvcPEDiscoveryPolicyPassword_Type()
)
svcPEDiscoveryPolicyPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPEDiscoveryPolicyPassword.setStatus("current")


class _SvcPEDiscoveryPolicyInterval_Type(Unsigned32):
    """Custom type svcPEDiscoveryPolicyInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SvcPEDiscoveryPolicyInterval_Type.__name__ = "Unsigned32"
_SvcPEDiscoveryPolicyInterval_Object = MibTableColumn
svcPEDiscoveryPolicyInterval = _SvcPEDiscoveryPolicyInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 22, 1, 4),
    _SvcPEDiscoveryPolicyInterval_Type()
)
svcPEDiscoveryPolicyInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPEDiscoveryPolicyInterval.setStatus("current")
if mibBuilder.loadTexts:
    svcPEDiscoveryPolicyInterval.setUnits("minutes")


class _SvcPEDiscoveryPolicyTimeout_Type(Unsigned32):
    """Custom type svcPEDiscoveryPolicyTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_SvcPEDiscoveryPolicyTimeout_Type.__name__ = "Unsigned32"
_SvcPEDiscoveryPolicyTimeout_Object = MibTableColumn
svcPEDiscoveryPolicyTimeout = _SvcPEDiscoveryPolicyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 22, 1, 5),
    _SvcPEDiscoveryPolicyTimeout_Type()
)
svcPEDiscoveryPolicyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPEDiscoveryPolicyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    svcPEDiscoveryPolicyTimeout.setUnits("seconds")
_SvcPEDiscPolServerTable_Object = MibTable
svcPEDiscPolServerTable = _SvcPEDiscPolServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 23)
)
if mibBuilder.loadTexts:
    svcPEDiscPolServerTable.setStatus("current")
_SvcPEDiscPolServerEntry_Object = MibTableRow
svcPEDiscPolServerEntry = _SvcPEDiscPolServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 23, 1)
)
svcPEDiscPolServerEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcPEDiscPolServerIndex"),
    (1, "TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyName"),
)
if mibBuilder.loadTexts:
    svcPEDiscPolServerEntry.setStatus("current")


class _SvcPEDiscPolServerIndex_Type(Unsigned32):
    """Custom type svcPEDiscPolServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SvcPEDiscPolServerIndex_Type.__name__ = "Unsigned32"
_SvcPEDiscPolServerIndex_Object = MibTableColumn
svcPEDiscPolServerIndex = _SvcPEDiscPolServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 23, 1, 1),
    _SvcPEDiscPolServerIndex_Type()
)
svcPEDiscPolServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPEDiscPolServerIndex.setStatus("current")
_SvcPEDiscPolServerRowStatus_Type = RowStatus
_SvcPEDiscPolServerRowStatus_Object = MibTableColumn
svcPEDiscPolServerRowStatus = _SvcPEDiscPolServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 23, 1, 2),
    _SvcPEDiscPolServerRowStatus_Type()
)
svcPEDiscPolServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPEDiscPolServerRowStatus.setStatus("current")
_SvcPEDiscPolServerAddressType_Type = InetAddressType
_SvcPEDiscPolServerAddressType_Object = MibTableColumn
svcPEDiscPolServerAddressType = _SvcPEDiscPolServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 23, 1, 3),
    _SvcPEDiscPolServerAddressType_Type()
)
svcPEDiscPolServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPEDiscPolServerAddressType.setStatus("current")
_SvcPEDiscPolServerAddress_Type = InetAddress
_SvcPEDiscPolServerAddress_Object = MibTableColumn
svcPEDiscPolServerAddress = _SvcPEDiscPolServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 23, 1, 4),
    _SvcPEDiscPolServerAddress_Type()
)
svcPEDiscPolServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPEDiscPolServerAddress.setStatus("current")


class _SvcPEDiscPolServerSecret_Type(OctetString):
    """Custom type svcPEDiscPolServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SvcPEDiscPolServerSecret_Type.__name__ = "OctetString"
_SvcPEDiscPolServerSecret_Object = MibTableColumn
svcPEDiscPolServerSecret = _SvcPEDiscPolServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 23, 1, 5),
    _SvcPEDiscPolServerSecret_Type()
)
svcPEDiscPolServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPEDiscPolServerSecret.setStatus("current")
_SvcPEDiscPolServerOperStatus_Type = ServiceOperStatus
_SvcPEDiscPolServerOperStatus_Object = MibTableColumn
svcPEDiscPolServerOperStatus = _SvcPEDiscPolServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 23, 1, 6),
    _SvcPEDiscPolServerOperStatus_Type()
)
svcPEDiscPolServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPEDiscPolServerOperStatus.setStatus("current")


class _SvcPEDiscPolServerPort_Type(Unsigned32):
    """Custom type svcPEDiscPolServerPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SvcPEDiscPolServerPort_Type.__name__ = "Unsigned32"
_SvcPEDiscPolServerPort_Object = MibTableColumn
svcPEDiscPolServerPort = _SvcPEDiscPolServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 23, 1, 7),
    _SvcPEDiscPolServerPort_Type()
)
svcPEDiscPolServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPEDiscPolServerPort.setStatus("current")
_SvcWholesalerInfoTable_Object = MibTable
svcWholesalerInfoTable = _SvcWholesalerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 24)
)
if mibBuilder.loadTexts:
    svcWholesalerInfoTable.setStatus("current")
_SvcWholesalerInfoEntry_Object = MibTableRow
svcWholesalerInfoEntry = _SvcWholesalerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 24, 1)
)
svcWholesalerInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcWholesalerID"),
)
if mibBuilder.loadTexts:
    svcWholesalerInfoEntry.setStatus("current")
_SvcWholesalerID_Type = TmnxServId
_SvcWholesalerID_Object = MibTableColumn
svcWholesalerID = _SvcWholesalerID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 24, 1, 1),
    _SvcWholesalerID_Type()
)
svcWholesalerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcWholesalerID.setStatus("current")
_SvcWholesalerNumStaticHosts_Type = Unsigned32
_SvcWholesalerNumStaticHosts_Object = MibTableColumn
svcWholesalerNumStaticHosts = _SvcWholesalerNumStaticHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 24, 1, 2),
    _SvcWholesalerNumStaticHosts_Type()
)
svcWholesalerNumStaticHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcWholesalerNumStaticHosts.setStatus("current")
_SvcWholesalerNumDynamicHosts_Type = Unsigned32
_SvcWholesalerNumDynamicHosts_Object = MibTableColumn
svcWholesalerNumDynamicHosts = _SvcWholesalerNumDynamicHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 24, 1, 3),
    _SvcWholesalerNumDynamicHosts_Type()
)
svcWholesalerNumDynamicHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcWholesalerNumDynamicHosts.setStatus("current")
_SvcWholesalerNumDhcpLeaseStates_Type = Unsigned32
_SvcWholesalerNumDhcpLeaseStates_Object = MibTableColumn
svcWholesalerNumDhcpLeaseStates = _SvcWholesalerNumDhcpLeaseStates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 24, 1, 4),
    _SvcWholesalerNumDhcpLeaseStates_Type()
)
svcWholesalerNumDhcpLeaseStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcWholesalerNumDhcpLeaseStates.setStatus("current")
_SvcWholesalerNumPppoeSessions_Type = Unsigned32
_SvcWholesalerNumPppoeSessions_Object = MibTableColumn
svcWholesalerNumPppoeSessions = _SvcWholesalerNumPppoeSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 24, 1, 5),
    _SvcWholesalerNumPppoeSessions_Type()
)
svcWholesalerNumPppoeSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcWholesalerNumPppoeSessions.setStatus("current")
_SvcWholesalerNumArpHosts_Type = Unsigned32
_SvcWholesalerNumArpHosts_Object = MibTableColumn
svcWholesalerNumArpHosts = _SvcWholesalerNumArpHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 24, 1, 6),
    _SvcWholesalerNumArpHosts_Type()
)
svcWholesalerNumArpHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcWholesalerNumArpHosts.setStatus("current")
_SvcDhcpLeaseStateActionTable_Object = MibTable
svcDhcpLeaseStateActionTable = _SvcDhcpLeaseStateActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 25)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateActionTable.setStatus("obsolete")
_SvcDhcpLeaseStateActionEntry_Object = MibTableRow
svcDhcpLeaseStateActionEntry = _SvcDhcpLeaseStateActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 25, 1)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateActionEntry.setStatus("obsolete")


class _SvcDhcpLseStateForceRenew_Type(TruthValue):
    """Custom type svcDhcpLseStateForceRenew based on TruthValue"""


_SvcDhcpLseStateForceRenew_Object = MibTableColumn
svcDhcpLseStateForceRenew = _SvcDhcpLseStateForceRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 25, 1, 1),
    _SvcDhcpLseStateForceRenew_Type()
)
svcDhcpLseStateForceRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLseStateForceRenew.setStatus("obsolete")
_SvcIfDHCP6MsgStatTable_Object = MibTable
svcIfDHCP6MsgStatTable = _SvcIfDHCP6MsgStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 26)
)
if mibBuilder.loadTexts:
    svcIfDHCP6MsgStatTable.setStatus("current")
_SvcIfDHCP6MsgStatEntry_Object = MibTableRow
svcIfDHCP6MsgStatEntry = _SvcIfDHCP6MsgStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 26, 1)
)
svcIfDHCP6MsgStatEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    svcIfDHCP6MsgStatEntry.setStatus("current")
_SvcIfDHCP6MsgStatsLstClrd_Type = TimeStamp
_SvcIfDHCP6MsgStatsLstClrd_Object = MibTableColumn
svcIfDHCP6MsgStatsLstClrd = _SvcIfDHCP6MsgStatsLstClrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 26, 1, 1),
    _SvcIfDHCP6MsgStatsLstClrd_Type()
)
svcIfDHCP6MsgStatsLstClrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIfDHCP6MsgStatsLstClrd.setStatus("current")
_SvcIfDHCP6MsgStatsRcvd_Type = Gauge32
_SvcIfDHCP6MsgStatsRcvd_Object = MibTableColumn
svcIfDHCP6MsgStatsRcvd = _SvcIfDHCP6MsgStatsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 26, 1, 2),
    _SvcIfDHCP6MsgStatsRcvd_Type()
)
svcIfDHCP6MsgStatsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIfDHCP6MsgStatsRcvd.setStatus("current")
_SvcIfDHCP6MsgStatsSent_Type = Gauge32
_SvcIfDHCP6MsgStatsSent_Object = MibTableColumn
svcIfDHCP6MsgStatsSent = _SvcIfDHCP6MsgStatsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 26, 1, 3),
    _SvcIfDHCP6MsgStatsSent_Type()
)
svcIfDHCP6MsgStatsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIfDHCP6MsgStatsSent.setStatus("current")
_SvcIfDHCP6MsgStatsDropped_Type = Gauge32
_SvcIfDHCP6MsgStatsDropped_Object = MibTableColumn
svcIfDHCP6MsgStatsDropped = _SvcIfDHCP6MsgStatsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 26, 1, 4),
    _SvcIfDHCP6MsgStatsDropped_Type()
)
svcIfDHCP6MsgStatsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIfDHCP6MsgStatsDropped.setStatus("current")
_SvcTlsBackboneInfoTable_Object = MibTable
svcTlsBackboneInfoTable = _SvcTlsBackboneInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27)
)
if mibBuilder.loadTexts:
    svcTlsBackboneInfoTable.setStatus("current")
_SvcTlsBackboneInfoEntry_Object = MibTableRow
svcTlsBackboneInfoEntry = _SvcTlsBackboneInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1)
)
if mibBuilder.loadTexts:
    svcTlsBackboneInfoEntry.setStatus("current")


class _SvcTlsBackboneSrcMac_Type(MacAddress):
    """Custom type svcTlsBackboneSrcMac based on MacAddress"""
    defaultHexValue = "000000000000"


_SvcTlsBackboneSrcMac_Object = MibTableColumn
svcTlsBackboneSrcMac = _SvcTlsBackboneSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1, 1),
    _SvcTlsBackboneSrcMac_Type()
)
svcTlsBackboneSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsBackboneSrcMac.setStatus("current")


class _SvcTlsBackboneVplsSvcId_Type(TmnxServId):
    """Custom type svcTlsBackboneVplsSvcId based on TmnxServId"""
    defaultValue = 0


_SvcTlsBackboneVplsSvcId_Object = MibTableColumn
svcTlsBackboneVplsSvcId = _SvcTlsBackboneVplsSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1, 2),
    _SvcTlsBackboneVplsSvcId_Type()
)
svcTlsBackboneVplsSvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsBackboneVplsSvcId.setStatus("current")


class _SvcTlsBackboneVplsSvcISID_Type(SvcISID):
    """Custom type svcTlsBackboneVplsSvcISID based on SvcISID"""
    defaultValue = -1


_SvcTlsBackboneVplsSvcISID_Object = MibTableColumn
svcTlsBackboneVplsSvcISID = _SvcTlsBackboneVplsSvcISID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1, 3),
    _SvcTlsBackboneVplsSvcISID_Type()
)
svcTlsBackboneVplsSvcISID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsBackboneVplsSvcISID.setStatus("current")
_SvcTlsBackboneOperSrcMac_Type = MacAddress
_SvcTlsBackboneOperSrcMac_Object = MibTableColumn
svcTlsBackboneOperSrcMac = _SvcTlsBackboneOperSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1, 4),
    _SvcTlsBackboneOperSrcMac_Type()
)
svcTlsBackboneOperSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBackboneOperSrcMac.setStatus("current")
_SvcTlsBackboneOperVplsSvcISID_Type = SvcISID
_SvcTlsBackboneOperVplsSvcISID_Object = MibTableColumn
svcTlsBackboneOperVplsSvcISID = _SvcTlsBackboneOperVplsSvcISID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1, 5),
    _SvcTlsBackboneOperVplsSvcISID_Type()
)
svcTlsBackboneOperVplsSvcISID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBackboneOperVplsSvcISID.setStatus("current")


class _SvcTlsBackboneLDPMacFlush_Type(TruthValue):
    """Custom type svcTlsBackboneLDPMacFlush based on TruthValue"""


_SvcTlsBackboneLDPMacFlush_Object = MibTableColumn
svcTlsBackboneLDPMacFlush = _SvcTlsBackboneLDPMacFlush_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1, 6),
    _SvcTlsBackboneLDPMacFlush_Type()
)
svcTlsBackboneLDPMacFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsBackboneLDPMacFlush.setStatus("current")


class _SvcTlsBackboneVplsStp_Type(TmnxEnabledDisabled):
    """Custom type svcTlsBackboneVplsStp based on TmnxEnabledDisabled"""


_SvcTlsBackboneVplsStp_Object = MibTableColumn
svcTlsBackboneVplsStp = _SvcTlsBackboneVplsStp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1, 7),
    _SvcTlsBackboneVplsStp_Type()
)
svcTlsBackboneVplsStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsBackboneVplsStp.setStatus("current")


class _SvcTlsBackboneLDPMacFlushNotMine_Type(TruthValue):
    """Custom type svcTlsBackboneLDPMacFlushNotMine based on TruthValue"""


_SvcTlsBackboneLDPMacFlushNotMine_Object = MibTableColumn
svcTlsBackboneLDPMacFlushNotMine = _SvcTlsBackboneLDPMacFlushNotMine_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1, 8),
    _SvcTlsBackboneLDPMacFlushNotMine_Type()
)
svcTlsBackboneLDPMacFlushNotMine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsBackboneLDPMacFlushNotMine.setStatus("current")


class _SvcTlsBackboneUseSapBMac_Type(TruthValue):
    """Custom type svcTlsBackboneUseSapBMac based on TruthValue"""


_SvcTlsBackboneUseSapBMac_Object = MibTableColumn
svcTlsBackboneUseSapBMac = _SvcTlsBackboneUseSapBMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1, 9),
    _SvcTlsBackboneUseSapBMac_Type()
)
svcTlsBackboneUseSapBMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsBackboneUseSapBMac.setStatus("current")


class _SvcTlsBackboneForceQTagFwd_Type(TruthValue):
    """Custom type svcTlsBackboneForceQTagFwd based on TruthValue"""


_SvcTlsBackboneForceQTagFwd_Object = MibTableColumn
svcTlsBackboneForceQTagFwd = _SvcTlsBackboneForceQTagFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 27, 1, 10),
    _SvcTlsBackboneForceQTagFwd_Type()
)
svcTlsBackboneForceQTagFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsBackboneForceQTagFwd.setStatus("current")
_TlsMFibTable_Object = MibTable
tlsMFibTable = _TlsMFibTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28)
)
if mibBuilder.loadTexts:
    tlsMFibTable.setStatus("current")
_TlsMFibEntry_Object = MibTableRow
tlsMFibEntry = _TlsMFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1)
)
tlsMFibEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibEntryType"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibGrpMacAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibGrpInetAddrType"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibGrpInetAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibSrcInetAddrType"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibSrcInetAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibLocale"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibPortId"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibEncapValue"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibSdpId"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibVcId"),
)
if mibBuilder.loadTexts:
    tlsMFibEntry.setStatus("current")


class _TlsMFibEntryType_Type(Integer32):
    """Custom type tlsMFibEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipBased", 1),
          ("macBased", 2))
    )


_TlsMFibEntryType_Type.__name__ = "Integer32"
_TlsMFibEntryType_Object = MibTableColumn
tlsMFibEntryType = _TlsMFibEntryType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 1),
    _TlsMFibEntryType_Type()
)
tlsMFibEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibEntryType.setStatus("current")
_TlsMFibGrpMacAddr_Type = MacAddress
_TlsMFibGrpMacAddr_Object = MibTableColumn
tlsMFibGrpMacAddr = _TlsMFibGrpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 2),
    _TlsMFibGrpMacAddr_Type()
)
tlsMFibGrpMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibGrpMacAddr.setStatus("current")
_TlsMFibGrpInetAddrType_Type = InetAddressType
_TlsMFibGrpInetAddrType_Object = MibTableColumn
tlsMFibGrpInetAddrType = _TlsMFibGrpInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 3),
    _TlsMFibGrpInetAddrType_Type()
)
tlsMFibGrpInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibGrpInetAddrType.setStatus("current")


class _TlsMFibGrpInetAddr_Type(InetAddress):
    """Custom type tlsMFibGrpInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMFibGrpInetAddr_Type.__name__ = "InetAddress"
_TlsMFibGrpInetAddr_Object = MibTableColumn
tlsMFibGrpInetAddr = _TlsMFibGrpInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 4),
    _TlsMFibGrpInetAddr_Type()
)
tlsMFibGrpInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibGrpInetAddr.setStatus("current")
_TlsMFibSrcInetAddrType_Type = InetAddressType
_TlsMFibSrcInetAddrType_Object = MibTableColumn
tlsMFibSrcInetAddrType = _TlsMFibSrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 5),
    _TlsMFibSrcInetAddrType_Type()
)
tlsMFibSrcInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibSrcInetAddrType.setStatus("current")


class _TlsMFibSrcInetAddr_Type(InetAddress):
    """Custom type tlsMFibSrcInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMFibSrcInetAddr_Type.__name__ = "InetAddress"
_TlsMFibSrcInetAddr_Object = MibTableColumn
tlsMFibSrcInetAddr = _TlsMFibSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 6),
    _TlsMFibSrcInetAddr_Type()
)
tlsMFibSrcInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibSrcInetAddr.setStatus("current")
_TlsMFibLocale_Type = MfibLocation
_TlsMFibLocale_Object = MibTableColumn
tlsMFibLocale = _TlsMFibLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 7),
    _TlsMFibLocale_Type()
)
tlsMFibLocale.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibLocale.setStatus("current")
_TlsMFibPortId_Type = TmnxPortID
_TlsMFibPortId_Object = MibTableColumn
tlsMFibPortId = _TlsMFibPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 8),
    _TlsMFibPortId_Type()
)
tlsMFibPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibPortId.setStatus("current")
_TlsMFibEncapValue_Type = TmnxEncapVal
_TlsMFibEncapValue_Object = MibTableColumn
tlsMFibEncapValue = _TlsMFibEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 9),
    _TlsMFibEncapValue_Type()
)
tlsMFibEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibEncapValue.setStatus("current")
_TlsMFibSdpId_Type = SdpId
_TlsMFibSdpId_Object = MibTableColumn
tlsMFibSdpId = _TlsMFibSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 10),
    _TlsMFibSdpId_Type()
)
tlsMFibSdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibSdpId.setStatus("current")
_TlsMFibVcId_Type = Unsigned32
_TlsMFibVcId_Object = MibTableColumn
tlsMFibVcId = _TlsMFibVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 11),
    _TlsMFibVcId_Type()
)
tlsMFibVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibVcId.setStatus("current")
_TlsMFibFwdOrBlk_Type = MfibGrpSrcFwdOrBlk
_TlsMFibFwdOrBlk_Object = MibTableColumn
tlsMFibFwdOrBlk = _TlsMFibFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 12),
    _TlsMFibFwdOrBlk_Type()
)
tlsMFibFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMFibFwdOrBlk.setStatus("current")
_TlsMFibSvcId_Type = TmnxServId
_TlsMFibSvcId_Object = MibTableColumn
tlsMFibSvcId = _TlsMFibSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 28, 1, 13),
    _TlsMFibSvcId_Type()
)
tlsMFibSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMFibSvcId.setStatus("current")
_TlsMFibStatsTable_Object = MibTable
tlsMFibStatsTable = _TlsMFibStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 29)
)
if mibBuilder.loadTexts:
    tlsMFibStatsTable.setStatus("current")
_TlsMFibStatsEntry_Object = MibTableRow
tlsMFibStatsEntry = _TlsMFibStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 29, 1)
)
tlsMFibStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibStatsEntryType"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibStatsGrpMacAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibStatsGrpInetAddrType"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibStatsGrpInetAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibStatsSrcInetAddrType"),
    (0, "TIMETRA-SERV-MIB", "tlsMFibStatsSrcInetAddr"),
)
if mibBuilder.loadTexts:
    tlsMFibStatsEntry.setStatus("current")


class _TlsMFibStatsEntryType_Type(Integer32):
    """Custom type tlsMFibStatsEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipBased", 1),
          ("macBased", 2))
    )


_TlsMFibStatsEntryType_Type.__name__ = "Integer32"
_TlsMFibStatsEntryType_Object = MibTableColumn
tlsMFibStatsEntryType = _TlsMFibStatsEntryType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 29, 1, 1),
    _TlsMFibStatsEntryType_Type()
)
tlsMFibStatsEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibStatsEntryType.setStatus("current")
_TlsMFibStatsGrpMacAddr_Type = MacAddress
_TlsMFibStatsGrpMacAddr_Object = MibTableColumn
tlsMFibStatsGrpMacAddr = _TlsMFibStatsGrpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 29, 1, 2),
    _TlsMFibStatsGrpMacAddr_Type()
)
tlsMFibStatsGrpMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibStatsGrpMacAddr.setStatus("current")
_TlsMFibStatsGrpInetAddrType_Type = InetAddressType
_TlsMFibStatsGrpInetAddrType_Object = MibTableColumn
tlsMFibStatsGrpInetAddrType = _TlsMFibStatsGrpInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 29, 1, 3),
    _TlsMFibStatsGrpInetAddrType_Type()
)
tlsMFibStatsGrpInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibStatsGrpInetAddrType.setStatus("current")


class _TlsMFibStatsGrpInetAddr_Type(InetAddress):
    """Custom type tlsMFibStatsGrpInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMFibStatsGrpInetAddr_Type.__name__ = "InetAddress"
_TlsMFibStatsGrpInetAddr_Object = MibTableColumn
tlsMFibStatsGrpInetAddr = _TlsMFibStatsGrpInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 29, 1, 4),
    _TlsMFibStatsGrpInetAddr_Type()
)
tlsMFibStatsGrpInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibStatsGrpInetAddr.setStatus("current")
_TlsMFibStatsSrcInetAddrType_Type = InetAddressType
_TlsMFibStatsSrcInetAddrType_Object = MibTableColumn
tlsMFibStatsSrcInetAddrType = _TlsMFibStatsSrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 29, 1, 5),
    _TlsMFibStatsSrcInetAddrType_Type()
)
tlsMFibStatsSrcInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibStatsSrcInetAddrType.setStatus("current")


class _TlsMFibStatsSrcInetAddr_Type(InetAddress):
    """Custom type tlsMFibStatsSrcInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMFibStatsSrcInetAddr_Type.__name__ = "InetAddress"
_TlsMFibStatsSrcInetAddr_Object = MibTableColumn
tlsMFibStatsSrcInetAddr = _TlsMFibStatsSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 29, 1, 6),
    _TlsMFibStatsSrcInetAddr_Type()
)
tlsMFibStatsSrcInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMFibStatsSrcInetAddr.setStatus("current")
_TlsMFibStatsForwardedPkts_Type = Counter64
_TlsMFibStatsForwardedPkts_Object = MibTableColumn
tlsMFibStatsForwardedPkts = _TlsMFibStatsForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 29, 1, 7),
    _TlsMFibStatsForwardedPkts_Type()
)
tlsMFibStatsForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMFibStatsForwardedPkts.setStatus("current")
_TlsMFibStatsForwardedOctets_Type = Counter64
_TlsMFibStatsForwardedOctets_Object = MibTableColumn
tlsMFibStatsForwardedOctets = _TlsMFibStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 29, 1, 8),
    _TlsMFibStatsForwardedOctets_Type()
)
tlsMFibStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMFibStatsForwardedOctets.setStatus("current")
_SvcTlsBgpADTableLastChanged_Type = TimeStamp
_SvcTlsBgpADTableLastChanged_Object = MibScalar
svcTlsBgpADTableLastChanged = _SvcTlsBgpADTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 30),
    _SvcTlsBgpADTableLastChanged_Type()
)
svcTlsBgpADTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpADTableLastChanged.setStatus("current")
_SvcTlsBgpADTable_Object = MibTable
svcTlsBgpADTable = _SvcTlsBgpADTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31)
)
if mibBuilder.loadTexts:
    svcTlsBgpADTable.setStatus("current")
_SvcTlsBgpADEntry_Object = MibTableRow
svcTlsBgpADEntry = _SvcTlsBgpADEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1)
)
svcTlsBgpADEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcTlsBgpADEntry.setStatus("current")
_SvcTlsBgpADRowStatus_Type = RowStatus
_SvcTlsBgpADRowStatus_Object = MibTableColumn
svcTlsBgpADRowStatus = _SvcTlsBgpADRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 1),
    _SvcTlsBgpADRowStatus_Type()
)
svcTlsBgpADRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADRowStatus.setStatus("current")
_SvcTlsBgpADLastChanged_Type = TimeStamp
_SvcTlsBgpADLastChanged_Object = MibTableColumn
svcTlsBgpADLastChanged = _SvcTlsBgpADLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 2),
    _SvcTlsBgpADLastChanged_Type()
)
svcTlsBgpADLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpADLastChanged.setStatus("current")


class _SvcTlsBgpADVplsId_Type(TmnxVPNRouteDistinguisher):
    """Custom type svcTlsBgpADVplsId based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_SvcTlsBgpADVplsId_Object = MibTableColumn
svcTlsBgpADVplsId = _SvcTlsBgpADVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 3),
    _SvcTlsBgpADVplsId_Type()
)
svcTlsBgpADVplsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVplsId.setStatus("current")


class _SvcTlsBgpADVsiPrefix_Type(Unsigned32):
    """Custom type svcTlsBgpADVsiPrefix based on Unsigned32"""
    defaultValue = 0


_SvcTlsBgpADVsiPrefix_Object = MibTableColumn
svcTlsBgpADVsiPrefix = _SvcTlsBgpADVsiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 4),
    _SvcTlsBgpADVsiPrefix_Type()
)
svcTlsBgpADVsiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiPrefix.setStatus("current")


class _SvcTlsBgpADVsiRD_Type(TmnxVPNRouteDistinguisher):
    """Custom type svcTlsBgpADVsiRD based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_SvcTlsBgpADVsiRD_Object = MibTableColumn
svcTlsBgpADVsiRD = _SvcTlsBgpADVsiRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 5),
    _SvcTlsBgpADVsiRD_Type()
)
svcTlsBgpADVsiRD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiRD.setStatus("obsolete")
_SvcTlsBgpADExportRteTarget_Type = TNamedItemOrEmpty
_SvcTlsBgpADExportRteTarget_Object = MibTableColumn
svcTlsBgpADExportRteTarget = _SvcTlsBgpADExportRteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 6),
    _SvcTlsBgpADExportRteTarget_Type()
)
svcTlsBgpADExportRteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADExportRteTarget.setStatus("obsolete")


class _SvcTlsBgpADVsiExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpADVsiExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpADVsiExportPolicy1_Object = MibTableColumn
svcTlsBgpADVsiExportPolicy1 = _SvcTlsBgpADVsiExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 7),
    _SvcTlsBgpADVsiExportPolicy1_Type()
)
svcTlsBgpADVsiExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiExportPolicy1.setStatus("obsolete")


class _SvcTlsBgpADVsiExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpADVsiExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpADVsiExportPolicy2_Object = MibTableColumn
svcTlsBgpADVsiExportPolicy2 = _SvcTlsBgpADVsiExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 8),
    _SvcTlsBgpADVsiExportPolicy2_Type()
)
svcTlsBgpADVsiExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiExportPolicy2.setStatus("obsolete")


class _SvcTlsBgpADVsiExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpADVsiExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpADVsiExportPolicy3_Object = MibTableColumn
svcTlsBgpADVsiExportPolicy3 = _SvcTlsBgpADVsiExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 9),
    _SvcTlsBgpADVsiExportPolicy3_Type()
)
svcTlsBgpADVsiExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiExportPolicy3.setStatus("obsolete")


class _SvcTlsBgpADVsiExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpADVsiExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpADVsiExportPolicy4_Object = MibTableColumn
svcTlsBgpADVsiExportPolicy4 = _SvcTlsBgpADVsiExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 10),
    _SvcTlsBgpADVsiExportPolicy4_Type()
)
svcTlsBgpADVsiExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiExportPolicy4.setStatus("obsolete")


class _SvcTlsBgpADVsiExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpADVsiExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpADVsiExportPolicy5_Object = MibTableColumn
svcTlsBgpADVsiExportPolicy5 = _SvcTlsBgpADVsiExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 11),
    _SvcTlsBgpADVsiExportPolicy5_Type()
)
svcTlsBgpADVsiExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiExportPolicy5.setStatus("obsolete")
_SvcTlsBgpADImportRteTarget_Type = TNamedItemOrEmpty
_SvcTlsBgpADImportRteTarget_Object = MibTableColumn
svcTlsBgpADImportRteTarget = _SvcTlsBgpADImportRteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 12),
    _SvcTlsBgpADImportRteTarget_Type()
)
svcTlsBgpADImportRteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADImportRteTarget.setStatus("obsolete")


class _SvcTlsBgpADVsiImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpADVsiImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpADVsiImportPolicy1_Object = MibTableColumn
svcTlsBgpADVsiImportPolicy1 = _SvcTlsBgpADVsiImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 13),
    _SvcTlsBgpADVsiImportPolicy1_Type()
)
svcTlsBgpADVsiImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiImportPolicy1.setStatus("obsolete")


class _SvcTlsBgpADVsiImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpADVsiImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpADVsiImportPolicy2_Object = MibTableColumn
svcTlsBgpADVsiImportPolicy2 = _SvcTlsBgpADVsiImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 14),
    _SvcTlsBgpADVsiImportPolicy2_Type()
)
svcTlsBgpADVsiImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiImportPolicy2.setStatus("obsolete")


class _SvcTlsBgpADVsiImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpADVsiImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpADVsiImportPolicy3_Object = MibTableColumn
svcTlsBgpADVsiImportPolicy3 = _SvcTlsBgpADVsiImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 15),
    _SvcTlsBgpADVsiImportPolicy3_Type()
)
svcTlsBgpADVsiImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiImportPolicy3.setStatus("obsolete")


class _SvcTlsBgpADVsiImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpADVsiImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpADVsiImportPolicy4_Object = MibTableColumn
svcTlsBgpADVsiImportPolicy4 = _SvcTlsBgpADVsiImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 16),
    _SvcTlsBgpADVsiImportPolicy4_Type()
)
svcTlsBgpADVsiImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiImportPolicy4.setStatus("obsolete")


class _SvcTlsBgpADVsiImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpADVsiImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpADVsiImportPolicy5_Object = MibTableColumn
svcTlsBgpADVsiImportPolicy5 = _SvcTlsBgpADVsiImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 17),
    _SvcTlsBgpADVsiImportPolicy5_Type()
)
svcTlsBgpADVsiImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADVsiImportPolicy5.setStatus("obsolete")


class _SvcTlsBgpADAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type svcTlsBgpADAdminStatus based on TmnxEnabledDisabled"""


_SvcTlsBgpADAdminStatus_Object = MibTableColumn
svcTlsBgpADAdminStatus = _SvcTlsBgpADAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 18),
    _SvcTlsBgpADAdminStatus_Type()
)
svcTlsBgpADAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADAdminStatus.setStatus("current")
_SvcEpipePbbTableLastChanged_Type = TimeStamp
_SvcEpipePbbTableLastChanged_Object = MibScalar
svcEpipePbbTableLastChanged = _SvcEpipePbbTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 36),
    _SvcEpipePbbTableLastChanged_Type()
)
svcEpipePbbTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpipePbbTableLastChanged.setStatus("current")
_SvcEpipePbbTable_Object = MibTable
svcEpipePbbTable = _SvcEpipePbbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37)
)
if mibBuilder.loadTexts:
    svcEpipePbbTable.setStatus("current")
_SvcEpipePbbEntry_Object = MibTableRow
svcEpipePbbEntry = _SvcEpipePbbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1)
)
svcEpipePbbEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcEpipePbbEntry.setStatus("current")
_SvcEpipePbbRowStatus_Type = RowStatus
_SvcEpipePbbRowStatus_Object = MibTableColumn
svcEpipePbbRowStatus = _SvcEpipePbbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1, 1),
    _SvcEpipePbbRowStatus_Type()
)
svcEpipePbbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEpipePbbRowStatus.setStatus("current")
_SvcEpipePbbLastChngd_Type = TimeStamp
_SvcEpipePbbLastChngd_Object = MibTableColumn
svcEpipePbbLastChngd = _SvcEpipePbbLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1, 2),
    _SvcEpipePbbLastChngd_Type()
)
svcEpipePbbLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpipePbbLastChngd.setStatus("current")
_SvcEpipePbbBvplsSvcId_Type = TmnxServId
_SvcEpipePbbBvplsSvcId_Object = MibTableColumn
svcEpipePbbBvplsSvcId = _SvcEpipePbbBvplsSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1, 3),
    _SvcEpipePbbBvplsSvcId_Type()
)
svcEpipePbbBvplsSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEpipePbbBvplsSvcId.setStatus("current")


class _SvcEpipePbbBvplsDstMac_Type(MacAddress):
    """Custom type svcEpipePbbBvplsDstMac based on MacAddress"""
    defaultHexValue = "000000000000"


_SvcEpipePbbBvplsDstMac_Object = MibTableColumn
svcEpipePbbBvplsDstMac = _SvcEpipePbbBvplsDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1, 4),
    _SvcEpipePbbBvplsDstMac_Type()
)
svcEpipePbbBvplsDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEpipePbbBvplsDstMac.setStatus("current")
_SvcEpipePbbSvcISID_Type = SvcISID
_SvcEpipePbbSvcISID_Object = MibTableColumn
svcEpipePbbSvcISID = _SvcEpipePbbSvcISID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1, 5),
    _SvcEpipePbbSvcISID_Type()
)
svcEpipePbbSvcISID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEpipePbbSvcISID.setStatus("current")
_SvcEpipePbbOperState_Type = ServiceOperStatus
_SvcEpipePbbOperState_Object = MibTableColumn
svcEpipePbbOperState = _SvcEpipePbbOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1, 6),
    _SvcEpipePbbOperState_Type()
)
svcEpipePbbOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpipePbbOperState.setStatus("current")
_SvcEpipePbbFlooding_Type = TruthValue
_SvcEpipePbbFlooding_Object = MibTableColumn
svcEpipePbbFlooding = _SvcEpipePbbFlooding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1, 7),
    _SvcEpipePbbFlooding_Type()
)
svcEpipePbbFlooding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpipePbbFlooding.setStatus("current")
_SvcEpipePbbLastStatusChange_Type = TimeStamp
_SvcEpipePbbLastStatusChange_Object = MibTableColumn
svcEpipePbbLastStatusChange = _SvcEpipePbbLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1, 8),
    _SvcEpipePbbLastStatusChange_Type()
)
svcEpipePbbLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpipePbbLastStatusChange.setStatus("current")
_SvcEpipePbbBvplsOperDstMac_Type = MacAddress
_SvcEpipePbbBvplsOperDstMac_Object = MibTableColumn
svcEpipePbbBvplsOperDstMac = _SvcEpipePbbBvplsOperDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1, 9),
    _SvcEpipePbbBvplsOperDstMac_Type()
)
svcEpipePbbBvplsOperDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpipePbbBvplsOperDstMac.setStatus("current")


class _SvcEpipePbbBvplsDstMacName_Type(TNamedItemOrEmpty):
    """Custom type svcEpipePbbBvplsDstMacName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SvcEpipePbbBvplsDstMacName_Object = MibTableColumn
svcEpipePbbBvplsDstMacName = _SvcEpipePbbBvplsDstMacName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 37, 1, 10),
    _SvcEpipePbbBvplsDstMacName_Type()
)
svcEpipePbbBvplsDstMacName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEpipePbbBvplsDstMacName.setStatus("current")
_TlsPipInfoTable_Object = MibTable
tlsPipInfoTable = _TlsPipInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40)
)
if mibBuilder.loadTexts:
    tlsPipInfoTable.setStatus("current")
_TlsPipInfoEntry_Object = MibTableRow
tlsPipInfoEntry = _TlsPipInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1)
)
tlsPipInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tlsPipInfoEntry.setStatus("current")
_TlsPipStpPortState_Type = TStpPortState
_TlsPipStpPortState_Object = MibTableColumn
tlsPipStpPortState = _TlsPipStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 1),
    _TlsPipStpPortState_Type()
)
tlsPipStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpPortState.setStatus("current")
_TlsPipStpPortRole_Type = StpPortRole
_TlsPipStpPortRole_Object = MibTableColumn
tlsPipStpPortRole = _TlsPipStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 2),
    _TlsPipStpPortRole_Type()
)
tlsPipStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpPortRole.setStatus("current")
_TlsPipStpDesignatedBridge_Type = BridgeId
_TlsPipStpDesignatedBridge_Object = MibTableColumn
tlsPipStpDesignatedBridge = _TlsPipStpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 3),
    _TlsPipStpDesignatedBridge_Type()
)
tlsPipStpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpDesignatedBridge.setStatus("current")
_TlsPipStpDesignatedPort_Type = Integer32
_TlsPipStpDesignatedPort_Object = MibTableColumn
tlsPipStpDesignatedPort = _TlsPipStpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 4),
    _TlsPipStpDesignatedPort_Type()
)
tlsPipStpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpDesignatedPort.setStatus("current")
_TlsPipStpException_Type = StpExceptionCondition
_TlsPipStpException_Object = MibTableColumn
tlsPipStpException = _TlsPipStpException_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 5),
    _TlsPipStpException_Type()
)
tlsPipStpException.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpException.setStatus("current")
_TlsPipStpForwardTransitions_Type = Counter32
_TlsPipStpForwardTransitions_Object = MibTableColumn
tlsPipStpForwardTransitions = _TlsPipStpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 6),
    _TlsPipStpForwardTransitions_Type()
)
tlsPipStpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpForwardTransitions.setStatus("current")
_TlsPipStpInConfigBpdus_Type = Counter32
_TlsPipStpInConfigBpdus_Object = MibTableColumn
tlsPipStpInConfigBpdus = _TlsPipStpInConfigBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 7),
    _TlsPipStpInConfigBpdus_Type()
)
tlsPipStpInConfigBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpInConfigBpdus.setStatus("current")
_TlsPipStpInTcnBpdus_Type = Counter32
_TlsPipStpInTcnBpdus_Object = MibTableColumn
tlsPipStpInTcnBpdus = _TlsPipStpInTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 8),
    _TlsPipStpInTcnBpdus_Type()
)
tlsPipStpInTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpInTcnBpdus.setStatus("current")
_TlsPipStpInRstBpdus_Type = Counter32
_TlsPipStpInRstBpdus_Object = MibTableColumn
tlsPipStpInRstBpdus = _TlsPipStpInRstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 9),
    _TlsPipStpInRstBpdus_Type()
)
tlsPipStpInRstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpInRstBpdus.setStatus("current")
_TlsPipStpInMstBpdus_Type = Counter32
_TlsPipStpInMstBpdus_Object = MibTableColumn
tlsPipStpInMstBpdus = _TlsPipStpInMstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 10),
    _TlsPipStpInMstBpdus_Type()
)
tlsPipStpInMstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpInMstBpdus.setStatus("current")
_TlsPipStpInBadBpdus_Type = Counter32
_TlsPipStpInBadBpdus_Object = MibTableColumn
tlsPipStpInBadBpdus = _TlsPipStpInBadBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 11),
    _TlsPipStpInBadBpdus_Type()
)
tlsPipStpInBadBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpInBadBpdus.setStatus("current")
_TlsPipStpOutConfigBpdus_Type = Counter32
_TlsPipStpOutConfigBpdus_Object = MibTableColumn
tlsPipStpOutConfigBpdus = _TlsPipStpOutConfigBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 12),
    _TlsPipStpOutConfigBpdus_Type()
)
tlsPipStpOutConfigBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpOutConfigBpdus.setStatus("current")
_TlsPipStpOutTcnBpdus_Type = Counter32
_TlsPipStpOutTcnBpdus_Object = MibTableColumn
tlsPipStpOutTcnBpdus = _TlsPipStpOutTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 13),
    _TlsPipStpOutTcnBpdus_Type()
)
tlsPipStpOutTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpOutTcnBpdus.setStatus("current")
_TlsPipStpOutRstBpdus_Type = Counter32
_TlsPipStpOutRstBpdus_Object = MibTableColumn
tlsPipStpOutRstBpdus = _TlsPipStpOutRstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 14),
    _TlsPipStpOutRstBpdus_Type()
)
tlsPipStpOutRstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpOutRstBpdus.setStatus("current")
_TlsPipStpOutMstBpdus_Type = Counter32
_TlsPipStpOutMstBpdus_Object = MibTableColumn
tlsPipStpOutMstBpdus = _TlsPipStpOutMstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 15),
    _TlsPipStpOutMstBpdus_Type()
)
tlsPipStpOutMstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpOutMstBpdus.setStatus("current")
_TlsPipStpOperStatus_Type = ServiceOperStatus
_TlsPipStpOperStatus_Object = MibTableColumn
tlsPipStpOperStatus = _TlsPipStpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 16),
    _TlsPipStpOperStatus_Type()
)
tlsPipStpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpOperStatus.setStatus("current")
_TlsPipStpMvplsPruneState_Type = MvplsPruneState
_TlsPipStpMvplsPruneState_Object = MibTableColumn
tlsPipStpMvplsPruneState = _TlsPipStpMvplsPruneState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 17),
    _TlsPipStpMvplsPruneState_Type()
)
tlsPipStpMvplsPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpMvplsPruneState.setStatus("current")
_TlsPipStpOperProtocol_Type = StpProtocol
_TlsPipStpOperProtocol_Object = MibTableColumn
tlsPipStpOperProtocol = _TlsPipStpOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 18),
    _TlsPipStpOperProtocol_Type()
)
tlsPipStpOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpOperProtocol.setStatus("current")


class _TlsPipStpPortNum_Type(Unsigned32):
    """Custom type tlsPipStpPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TlsPipStpPortNum_Type.__name__ = "Unsigned32"
_TlsPipStpPortNum_Object = MibTableColumn
tlsPipStpPortNum = _TlsPipStpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 19),
    _TlsPipStpPortNum_Type()
)
tlsPipStpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpPortNum.setStatus("current")
_TlsPipStpInsideRegion_Type = TruthValue
_TlsPipStpInsideRegion_Object = MibTableColumn
tlsPipStpInsideRegion = _TlsPipStpInsideRegion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 20),
    _TlsPipStpInsideRegion_Type()
)
tlsPipStpInsideRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipStpInsideRegion.setStatus("current")
_TlsPipInTcBitBpdus_Type = Counter32
_TlsPipInTcBitBpdus_Object = MibTableColumn
tlsPipInTcBitBpdus = _TlsPipInTcBitBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 21),
    _TlsPipInTcBitBpdus_Type()
)
tlsPipInTcBitBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipInTcBitBpdus.setStatus("current")
_TlsPipOutTcBitBpdus_Type = Counter32
_TlsPipOutTcBitBpdus_Object = MibTableColumn
tlsPipOutTcBitBpdus = _TlsPipOutTcBitBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 40, 1, 22),
    _TlsPipOutTcBitBpdus_Type()
)
tlsPipOutTcBitBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipOutTcBitBpdus.setStatus("current")
_TlsPipMstiTable_Object = MibTable
tlsPipMstiTable = _TlsPipMstiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 41)
)
if mibBuilder.loadTexts:
    tlsPipMstiTable.setStatus("current")
_TlsPipMstiEntry_Object = MibTableRow
tlsPipMstiEntry = _TlsPipMstiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 41, 1)
)
tlsPipMstiEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsMstiInstanceId"),
)
if mibBuilder.loadTexts:
    tlsPipMstiEntry.setStatus("current")
_TlsPipMstiPortRole_Type = StpPortRole
_TlsPipMstiPortRole_Object = MibTableColumn
tlsPipMstiPortRole = _TlsPipMstiPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 41, 1, 1),
    _TlsPipMstiPortRole_Type()
)
tlsPipMstiPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipMstiPortRole.setStatus("current")
_TlsPipMstiPortState_Type = TStpPortState
_TlsPipMstiPortState_Object = MibTableColumn
tlsPipMstiPortState = _TlsPipMstiPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 41, 1, 2),
    _TlsPipMstiPortState_Type()
)
tlsPipMstiPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipMstiPortState.setStatus("current")
_TlsPipMstiDesignatedBridge_Type = BridgeId
_TlsPipMstiDesignatedBridge_Object = MibTableColumn
tlsPipMstiDesignatedBridge = _TlsPipMstiDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 41, 1, 3),
    _TlsPipMstiDesignatedBridge_Type()
)
tlsPipMstiDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipMstiDesignatedBridge.setStatus("current")
_TlsPipMstiDesignatedPort_Type = Integer32
_TlsPipMstiDesignatedPort_Object = MibTableColumn
tlsPipMstiDesignatedPort = _TlsPipMstiDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 41, 1, 4),
    _TlsPipMstiDesignatedPort_Type()
)
tlsPipMstiDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPipMstiDesignatedPort.setStatus("current")
_SvcTotalFdbMimDestIdxEntries_Type = Unsigned32
_SvcTotalFdbMimDestIdxEntries_Object = MibScalar
svcTotalFdbMimDestIdxEntries = _SvcTotalFdbMimDestIdxEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 42),
    _SvcTotalFdbMimDestIdxEntries_Type()
)
svcTotalFdbMimDestIdxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotalFdbMimDestIdxEntries.setStatus("current")
_SvcDhcpManagedRouteTable_Object = MibTable
svcDhcpManagedRouteTable = _SvcDhcpManagedRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 43)
)
if mibBuilder.loadTexts:
    svcDhcpManagedRouteTable.setStatus("current")
_SvcDhcpManagedRouteEntry_Object = MibTableRow
svcDhcpManagedRouteEntry = _SvcDhcpManagedRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 43, 1)
)
svcDhcpManagedRouteEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddr"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpManagedRouteInetAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpManagedRouteInetAddr"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpManagedRoutePrefixLen"),
)
if mibBuilder.loadTexts:
    svcDhcpManagedRouteEntry.setStatus("current")
_SvcDhcpManagedRouteInetAddrType_Type = InetAddressType
_SvcDhcpManagedRouteInetAddrType_Object = MibTableColumn
svcDhcpManagedRouteInetAddrType = _SvcDhcpManagedRouteInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 43, 1, 1),
    _SvcDhcpManagedRouteInetAddrType_Type()
)
svcDhcpManagedRouteInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpManagedRouteInetAddrType.setStatus("current")
_SvcDhcpManagedRouteInetAddr_Type = InetAddress
_SvcDhcpManagedRouteInetAddr_Object = MibTableColumn
svcDhcpManagedRouteInetAddr = _SvcDhcpManagedRouteInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 43, 1, 2),
    _SvcDhcpManagedRouteInetAddr_Type()
)
svcDhcpManagedRouteInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpManagedRouteInetAddr.setStatus("current")


class _SvcDhcpManagedRoutePrefixLen_Type(InetAddressPrefixLength):
    """Custom type svcDhcpManagedRoutePrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SvcDhcpManagedRoutePrefixLen_Type.__name__ = "InetAddressPrefixLength"
_SvcDhcpManagedRoutePrefixLen_Object = MibTableColumn
svcDhcpManagedRoutePrefixLen = _SvcDhcpManagedRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 43, 1, 3),
    _SvcDhcpManagedRoutePrefixLen_Type()
)
svcDhcpManagedRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpManagedRoutePrefixLen.setStatus("current")
_SvcDhcpManagedRouteStatus_Type = TmnxManagedRouteStatus
_SvcDhcpManagedRouteStatus_Object = MibTableColumn
svcDhcpManagedRouteStatus = _SvcDhcpManagedRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 43, 1, 4),
    _SvcDhcpManagedRouteStatus_Type()
)
svcDhcpManagedRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpManagedRouteStatus.setStatus("current")
_SvcArpHostTableLastChanged_Type = TimeStamp
_SvcArpHostTableLastChanged_Object = MibScalar
svcArpHostTableLastChanged = _SvcArpHostTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 44),
    _SvcArpHostTableLastChanged_Type()
)
svcArpHostTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostTableLastChanged.setStatus("current")
_SvcArpHostTable_Object = MibTable
svcArpHostTable = _SvcArpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45)
)
if mibBuilder.loadTexts:
    svcArpHostTable.setStatus("current")
_SvcArpHostEntry_Object = MibTableRow
svcArpHostEntry = _SvcArpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1)
)
svcArpHostEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostIpAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostIpAddr"),
)
if mibBuilder.loadTexts:
    svcArpHostEntry.setStatus("current")
_SvcArpHostIpAddrType_Type = InetAddressType
_SvcArpHostIpAddrType_Object = MibTableColumn
svcArpHostIpAddrType = _SvcArpHostIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 1),
    _SvcArpHostIpAddrType_Type()
)
svcArpHostIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcArpHostIpAddrType.setStatus("current")


class _SvcArpHostIpAddr_Type(InetAddress):
    """Custom type svcArpHostIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_SvcArpHostIpAddr_Type.__name__ = "InetAddress"
_SvcArpHostIpAddr_Object = MibTableColumn
svcArpHostIpAddr = _SvcArpHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 2),
    _SvcArpHostIpAddr_Type()
)
svcArpHostIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcArpHostIpAddr.setStatus("current")
_SvcArpHostLocale_Type = ServAccessLocation
_SvcArpHostLocale_Object = MibTableColumn
svcArpHostLocale = _SvcArpHostLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 3),
    _SvcArpHostLocale_Type()
)
svcArpHostLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostLocale.setStatus("current")
_SvcArpHostSapPortId_Type = TmnxPortID
_SvcArpHostSapPortId_Object = MibTableColumn
svcArpHostSapPortId = _SvcArpHostSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 4),
    _SvcArpHostSapPortId_Type()
)
svcArpHostSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostSapPortId.setStatus("current")
_SvcArpHostSapEncapValue_Type = TmnxEncapVal
_SvcArpHostSapEncapValue_Object = MibTableColumn
svcArpHostSapEncapValue = _SvcArpHostSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 5),
    _SvcArpHostSapEncapValue_Type()
)
svcArpHostSapEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostSapEncapValue.setStatus("current")
_SvcArpHostSdpId_Type = SdpId
_SvcArpHostSdpId_Object = MibTableColumn
svcArpHostSdpId = _SvcArpHostSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 6),
    _SvcArpHostSdpId_Type()
)
svcArpHostSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostSdpId.setStatus("current")
_SvcArpHostVcId_Type = Unsigned32
_SvcArpHostVcId_Object = MibTableColumn
svcArpHostVcId = _SvcArpHostVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 7),
    _SvcArpHostVcId_Type()
)
svcArpHostVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostVcId.setStatus("current")
_SvcArpHostSessionTimeout_Type = Unsigned32
_SvcArpHostSessionTimeout_Object = MibTableColumn
svcArpHostSessionTimeout = _SvcArpHostSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 8),
    _SvcArpHostSessionTimeout_Type()
)
svcArpHostSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostSessionTimeout.setStatus("current")


class _SvcArpHostStart_Type(DateAndTime):
    """Custom type svcArpHostStart based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_SvcArpHostStart_Type.__name__ = "DateAndTime"
_SvcArpHostStart_Object = MibTableColumn
svcArpHostStart = _SvcArpHostStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 9),
    _SvcArpHostStart_Type()
)
svcArpHostStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostStart.setStatus("current")


class _SvcArpHostLastAuth_Type(DateAndTime):
    """Custom type svcArpHostLastAuth based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_SvcArpHostLastAuth_Type.__name__ = "DateAndTime"
_SvcArpHostLastAuth_Object = MibTableColumn
svcArpHostLastAuth = _SvcArpHostLastAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 10),
    _SvcArpHostLastAuth_Type()
)
svcArpHostLastAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostLastAuth.setStatus("current")


class _SvcArpHostRefresh_Type(DateAndTime):
    """Custom type svcArpHostRefresh based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_SvcArpHostRefresh_Type.__name__ = "DateAndTime"
_SvcArpHostRefresh_Object = MibTableColumn
svcArpHostRefresh = _SvcArpHostRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 11),
    _SvcArpHostRefresh_Type()
)
svcArpHostRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostRefresh.setStatus("current")
_SvcArpHostRemainingTime_Type = Unsigned32
_SvcArpHostRemainingTime_Object = MibTableColumn
svcArpHostRemainingTime = _SvcArpHostRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 12),
    _SvcArpHostRemainingTime_Type()
)
svcArpHostRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    svcArpHostRemainingTime.setUnits("seconds")
_SvcArpHostShcvOperState_Type = ServShcvOperState
_SvcArpHostShcvOperState_Object = MibTableColumn
svcArpHostShcvOperState = _SvcArpHostShcvOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 13),
    _SvcArpHostShcvOperState_Type()
)
svcArpHostShcvOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostShcvOperState.setStatus("current")
_SvcArpHostShcvChecks_Type = Unsigned32
_SvcArpHostShcvChecks_Object = MibTableColumn
svcArpHostShcvChecks = _SvcArpHostShcvChecks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 14),
    _SvcArpHostShcvChecks_Type()
)
svcArpHostShcvChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostShcvChecks.setStatus("current")
_SvcArpHostShcvReplies_Type = Unsigned32
_SvcArpHostShcvReplies_Object = MibTableColumn
svcArpHostShcvReplies = _SvcArpHostShcvReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 15),
    _SvcArpHostShcvReplies_Type()
)
svcArpHostShcvReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostShcvReplies.setStatus("current")
_SvcArpHostShcvReplyTime_Type = TimeStamp
_SvcArpHostShcvReplyTime_Object = MibTableColumn
svcArpHostShcvReplyTime = _SvcArpHostShcvReplyTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 16),
    _SvcArpHostShcvReplyTime_Type()
)
svcArpHostShcvReplyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostShcvReplyTime.setStatus("current")
_SvcArpHostSubscrIdent_Type = TmnxSubIdentStringOrEmpty
_SvcArpHostSubscrIdent_Object = MibTableColumn
svcArpHostSubscrIdent = _SvcArpHostSubscrIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 17),
    _SvcArpHostSubscrIdent_Type()
)
svcArpHostSubscrIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostSubscrIdent.setStatus("current")
_SvcArpHostSubProfString_Type = TmnxSubProfileStringOrEmpty
_SvcArpHostSubProfString_Object = MibTableColumn
svcArpHostSubProfString = _SvcArpHostSubProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 18),
    _SvcArpHostSubProfString_Type()
)
svcArpHostSubProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostSubProfString.setStatus("current")
_SvcArpHostSlaProfString_Type = TmnxSlaProfileStringOrEmpty
_SvcArpHostSlaProfString_Object = MibTableColumn
svcArpHostSlaProfString = _SvcArpHostSlaProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 19),
    _SvcArpHostSlaProfString_Type()
)
svcArpHostSlaProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostSlaProfString.setStatus("current")
_SvcArpHostAppProfString_Type = TmnxAppProfileStringOrEmpty
_SvcArpHostAppProfString_Object = MibTableColumn
svcArpHostAppProfString = _SvcArpHostAppProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 20),
    _SvcArpHostAppProfString_Type()
)
svcArpHostAppProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostAppProfString.setStatus("current")
_SvcArpHostAncpString_Type = TmnxAncpStringOrZero
_SvcArpHostAncpString_Object = MibTableColumn
svcArpHostAncpString = _SvcArpHostAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 21),
    _SvcArpHostAncpString_Type()
)
svcArpHostAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostAncpString.setStatus("current")
_SvcArpHostInterDestId_Type = TmnxSubMgtIntDestIdOrEmpty
_SvcArpHostInterDestId_Object = MibTableColumn
svcArpHostInterDestId = _SvcArpHostInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 22),
    _SvcArpHostInterDestId_Type()
)
svcArpHostInterDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostInterDestId.setStatus("current")
_SvcArpHostRetailerSvcId_Type = TmnxServId
_SvcArpHostRetailerSvcId_Object = MibTableColumn
svcArpHostRetailerSvcId = _SvcArpHostRetailerSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 23),
    _SvcArpHostRetailerSvcId_Type()
)
svcArpHostRetailerSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostRetailerSvcId.setStatus("current")
_SvcArpHostRetailerIf_Type = InterfaceIndexOrZero
_SvcArpHostRetailerIf_Object = MibTableColumn
svcArpHostRetailerIf = _SvcArpHostRetailerIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 24),
    _SvcArpHostRetailerIf_Type()
)
svcArpHostRetailerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostRetailerIf.setStatus("current")
_SvcArpHostMacAddr_Type = MacAddress
_SvcArpHostMacAddr_Object = MibTableColumn
svcArpHostMacAddr = _SvcArpHostMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 25),
    _SvcArpHostMacAddr_Type()
)
svcArpHostMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostMacAddr.setStatus("current")
_SvcArpHostPersistKey_Type = Unsigned32
_SvcArpHostPersistKey_Object = MibTableColumn
svcArpHostPersistKey = _SvcArpHostPersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 26),
    _SvcArpHostPersistKey_Type()
)
svcArpHostPersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostPersistKey.setStatus("current")
_SvcArpHostCategoryMapName_Type = TNamedItemOrEmpty
_SvcArpHostCategoryMapName_Object = MibTableColumn
svcArpHostCategoryMapName = _SvcArpHostCategoryMapName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 27),
    _SvcArpHostCategoryMapName_Type()
)
svcArpHostCategoryMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostCategoryMapName.setStatus("current")


class _SvcArpHostRadiusClassAttr_Type(OctetString):
    """Custom type svcArpHostRadiusClassAttr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_SvcArpHostRadiusClassAttr_Type.__name__ = "OctetString"
_SvcArpHostRadiusClassAttr_Object = MibTableColumn
svcArpHostRadiusClassAttr = _SvcArpHostRadiusClassAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 28),
    _SvcArpHostRadiusClassAttr_Type()
)
svcArpHostRadiusClassAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostRadiusClassAttr.setStatus("current")


class _SvcArpHostRadiusUserName_Type(DisplayString):
    """Custom type svcArpHostRadiusUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SvcArpHostRadiusUserName_Type.__name__ = "DisplayString"
_SvcArpHostRadiusUserName_Object = MibTableColumn
svcArpHostRadiusUserName = _SvcArpHostRadiusUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 29),
    _SvcArpHostRadiusUserName_Type()
)
svcArpHostRadiusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostRadiusUserName.setStatus("current")
_SvcArpHostOriginSubscrId_Type = ArpHostInfoOrigin
_SvcArpHostOriginSubscrId_Object = MibTableColumn
svcArpHostOriginSubscrId = _SvcArpHostOriginSubscrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 30),
    _SvcArpHostOriginSubscrId_Type()
)
svcArpHostOriginSubscrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostOriginSubscrId.setStatus("current")
_SvcArpHostOriginStrings_Type = ArpHostInfoOrigin
_SvcArpHostOriginStrings_Object = MibTableColumn
svcArpHostOriginStrings = _SvcArpHostOriginStrings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 45, 1, 31),
    _SvcArpHostOriginStrings_Type()
)
svcArpHostOriginStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostOriginStrings.setStatus("current")
_SvcArpHostIfTableLastMgmtChange_Type = TimeStamp
_SvcArpHostIfTableLastMgmtChange_Object = MibScalar
svcArpHostIfTableLastMgmtChange = _SvcArpHostIfTableLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 46),
    _SvcArpHostIfTableLastMgmtChange_Type()
)
svcArpHostIfTableLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostIfTableLastMgmtChange.setStatus("current")
_SvcArpHostIfTable_Object = MibTable
svcArpHostIfTable = _SvcArpHostIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 47)
)
if mibBuilder.loadTexts:
    svcArpHostIfTable.setStatus("current")
_SvcArpHostIfEntry_Object = MibTableRow
svcArpHostIfEntry = _SvcArpHostIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 47, 1)
)
svcArpHostIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    svcArpHostIfEntry.setStatus("current")
_SvcArpHostIfLastMgmtChange_Type = TimeStamp
_SvcArpHostIfLastMgmtChange_Object = MibTableColumn
svcArpHostIfLastMgmtChange = _SvcArpHostIfLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 47, 1, 1),
    _SvcArpHostIfLastMgmtChange_Type()
)
svcArpHostIfLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostIfLastMgmtChange.setStatus("current")
_SvcArpHostIfAdminState_Type = TmnxAdminState
_SvcArpHostIfAdminState_Object = MibTableColumn
svcArpHostIfAdminState = _SvcArpHostIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 47, 1, 2),
    _SvcArpHostIfAdminState_Type()
)
svcArpHostIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcArpHostIfAdminState.setStatus("current")


class _SvcArpHostIfMaxNumHosts_Type(Unsigned32):
    """Custom type svcArpHostIfMaxNumHosts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SvcArpHostIfMaxNumHosts_Type.__name__ = "Unsigned32"
_SvcArpHostIfMaxNumHosts_Object = MibTableColumn
svcArpHostIfMaxNumHosts = _SvcArpHostIfMaxNumHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 47, 1, 3),
    _SvcArpHostIfMaxNumHosts_Type()
)
svcArpHostIfMaxNumHosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcArpHostIfMaxNumHosts.setStatus("current")


class _SvcArpHostIfMaxNumHostsSap_Type(Unsigned32):
    """Custom type svcArpHostIfMaxNumHostsSap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SvcArpHostIfMaxNumHostsSap_Type.__name__ = "Unsigned32"
_SvcArpHostIfMaxNumHostsSap_Object = MibTableColumn
svcArpHostIfMaxNumHostsSap = _SvcArpHostIfMaxNumHostsSap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 47, 1, 4),
    _SvcArpHostIfMaxNumHostsSap_Type()
)
svcArpHostIfMaxNumHostsSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcArpHostIfMaxNumHostsSap.setStatus("current")


class _SvcArpHostIfMinAuthInterval_Type(Unsigned32):
    """Custom type svcArpHostIfMinAuthInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_SvcArpHostIfMinAuthInterval_Type.__name__ = "Unsigned32"
_SvcArpHostIfMinAuthInterval_Object = MibTableColumn
svcArpHostIfMinAuthInterval = _SvcArpHostIfMinAuthInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 47, 1, 5),
    _SvcArpHostIfMinAuthInterval_Type()
)
svcArpHostIfMinAuthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcArpHostIfMinAuthInterval.setStatus("current")
if mibBuilder.loadTexts:
    svcArpHostIfMinAuthInterval.setUnits("minutes")
_SvcArpHostIfNumHosts_Type = Gauge32
_SvcArpHostIfNumHosts_Object = MibTableColumn
svcArpHostIfNumHosts = _SvcArpHostIfNumHosts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 47, 1, 6),
    _SvcArpHostIfNumHosts_Type()
)
svcArpHostIfNumHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostIfNumHosts.setStatus("current")
_SvcArpHostDefaultSessionTimeout_Type = Unsigned32
_SvcArpHostDefaultSessionTimeout_Object = MibScalar
svcArpHostDefaultSessionTimeout = _SvcArpHostDefaultSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 48),
    _SvcArpHostDefaultSessionTimeout_Type()
)
svcArpHostDefaultSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostDefaultSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    svcArpHostDefaultSessionTimeout.setUnits("seconds")
_SvcIgmpTrkTableLastMgmtChange_Type = TimeStamp
_SvcIgmpTrkTableLastMgmtChange_Object = MibScalar
svcIgmpTrkTableLastMgmtChange = _SvcIgmpTrkTableLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 49),
    _SvcIgmpTrkTableLastMgmtChange_Type()
)
svcIgmpTrkTableLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIgmpTrkTableLastMgmtChange.setStatus("current")
_SvcIgmpTrkTable_Object = MibTable
svcIgmpTrkTable = _SvcIgmpTrkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 50)
)
if mibBuilder.loadTexts:
    svcIgmpTrkTable.setStatus("current")
_SvcIgmpTrkEntry_Object = MibTableRow
svcIgmpTrkEntry = _SvcIgmpTrkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 50, 1)
)
svcIgmpTrkEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcIgmpTrkEntry.setStatus("current")
_SvcIgmpTrkLastMgmtChange_Type = TimeStamp
_SvcIgmpTrkLastMgmtChange_Object = MibTableColumn
svcIgmpTrkLastMgmtChange = _SvcIgmpTrkLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 50, 1, 1),
    _SvcIgmpTrkLastMgmtChange_Type()
)
svcIgmpTrkLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIgmpTrkLastMgmtChange.setStatus("current")


class _SvcIgmpTrkAdminState_Type(TmnxAdminState):
    """Custom type svcIgmpTrkAdminState based on TmnxAdminState"""


_SvcIgmpTrkAdminState_Object = MibTableColumn
svcIgmpTrkAdminState = _SvcIgmpTrkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 50, 1, 2),
    _SvcIgmpTrkAdminState_Type()
)
svcIgmpTrkAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcIgmpTrkAdminState.setStatus("current")


class _SvcIgmpTrkExpiryTime_Type(Unsigned32):
    """Custom type svcIgmpTrkExpiryTime based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SvcIgmpTrkExpiryTime_Type.__name__ = "Unsigned32"
_SvcIgmpTrkExpiryTime_Object = MibTableColumn
svcIgmpTrkExpiryTime = _SvcIgmpTrkExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 50, 1, 3),
    _SvcIgmpTrkExpiryTime_Type()
)
svcIgmpTrkExpiryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcIgmpTrkExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    svcIgmpTrkExpiryTime.setUnits("seconds")
_SvcIpipeInfoTableLastMgmtChange_Type = TimeStamp
_SvcIpipeInfoTableLastMgmtChange_Object = MibScalar
svcIpipeInfoTableLastMgmtChange = _SvcIpipeInfoTableLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 51),
    _SvcIpipeInfoTableLastMgmtChange_Type()
)
svcIpipeInfoTableLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIpipeInfoTableLastMgmtChange.setStatus("current")
_SvcIpipeInfoTable_Object = MibTable
svcIpipeInfoTable = _SvcIpipeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 52)
)
if mibBuilder.loadTexts:
    svcIpipeInfoTable.setStatus("current")
_SvcIpipeInfoEntry_Object = MibTableRow
svcIpipeInfoEntry = _SvcIpipeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 52, 1)
)
svcIpipeInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcIpipeInfoEntry.setStatus("current")
_SvcIpipeInfoLastMgmtChange_Type = TimeStamp
_SvcIpipeInfoLastMgmtChange_Object = MibTableColumn
svcIpipeInfoLastMgmtChange = _SvcIpipeInfoLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 52, 1, 1),
    _SvcIpipeInfoLastMgmtChange_Type()
)
svcIpipeInfoLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIpipeInfoLastMgmtChange.setStatus("current")


class _SvcIpipeCeAddressDiscovery_Type(TmnxEnabledDisabled):
    """Custom type svcIpipeCeAddressDiscovery based on TmnxEnabledDisabled"""


_SvcIpipeCeAddressDiscovery_Object = MibTableColumn
svcIpipeCeAddressDiscovery = _SvcIpipeCeAddressDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 52, 1, 2),
    _SvcIpipeCeAddressDiscovery_Type()
)
svcIpipeCeAddressDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcIpipeCeAddressDiscovery.setStatus("current")


class _SvcIpipeIpv6CeAddressDiscovery_Type(TmnxEnabledDisabled):
    """Custom type svcIpipeIpv6CeAddressDiscovery based on TmnxEnabledDisabled"""


_SvcIpipeIpv6CeAddressDiscovery_Object = MibTableColumn
svcIpipeIpv6CeAddressDiscovery = _SvcIpipeIpv6CeAddressDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 52, 1, 3),
    _SvcIpipeIpv6CeAddressDiscovery_Type()
)
svcIpipeIpv6CeAddressDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcIpipeIpv6CeAddressDiscovery.setStatus("current")


class _SvcIpipeStackCapabilitySignaling_Type(TmnxEnabledDisabled):
    """Custom type svcIpipeStackCapabilitySignaling based on TmnxEnabledDisabled"""


_SvcIpipeStackCapabilitySignaling_Object = MibTableColumn
svcIpipeStackCapabilitySignaling = _SvcIpipeStackCapabilitySignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 52, 1, 4),
    _SvcIpipeStackCapabilitySignaling_Type()
)
svcIpipeStackCapabilitySignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcIpipeStackCapabilitySignaling.setStatus("current")
_SvcDhcpLeaseStateBgpTable_Object = MibTable
svcDhcpLeaseStateBgpTable = _SvcDhcpLeaseStateBgpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 53)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateBgpTable.setStatus("obsolete")
_SvcDhcpLeaseStateBgpEntry_Object = MibTableRow
svcDhcpLeaseStateBgpEntry = _SvcDhcpLeaseStateBgpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 53, 1)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateBgpEntry.setStatus("current")
_SvcDhcpLseStateBgpPrngPlcyName_Type = TNamedItemOrEmpty
_SvcDhcpLseStateBgpPrngPlcyName_Object = MibTableColumn
svcDhcpLseStateBgpPrngPlcyName = _SvcDhcpLseStateBgpPrngPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 53, 1, 1),
    _SvcDhcpLseStateBgpPrngPlcyName_Type()
)
svcDhcpLseStateBgpPrngPlcyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBgpPrngPlcyName.setStatus("obsolete")
_SvcDhcpLseStateBgpAuthKeyChain_Type = TNamedItemOrEmpty
_SvcDhcpLseStateBgpAuthKeyChain_Object = MibTableColumn
svcDhcpLseStateBgpAuthKeyChain = _SvcDhcpLseStateBgpAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 53, 1, 2),
    _SvcDhcpLseStateBgpAuthKeyChain_Type()
)
svcDhcpLseStateBgpAuthKeyChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBgpAuthKeyChain.setStatus("obsolete")


class _SvcDhcpLseStateBgpMD5AuthKey_Type(OctetString):
    """Custom type svcDhcpLseStateBgpMD5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvcDhcpLseStateBgpMD5AuthKey_Type.__name__ = "OctetString"
_SvcDhcpLseStateBgpMD5AuthKey_Object = MibTableColumn
svcDhcpLseStateBgpMD5AuthKey = _SvcDhcpLseStateBgpMD5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 53, 1, 3),
    _SvcDhcpLseStateBgpMD5AuthKey_Type()
)
svcDhcpLseStateBgpMD5AuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBgpMD5AuthKey.setStatus("obsolete")
_SvcDhcpLseStateBgpImportPolicy_Type = TPolicyStatementNameOrEmpty
_SvcDhcpLseStateBgpImportPolicy_Object = MibTableColumn
svcDhcpLseStateBgpImportPolicy = _SvcDhcpLseStateBgpImportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 53, 1, 4),
    _SvcDhcpLseStateBgpImportPolicy_Type()
)
svcDhcpLseStateBgpImportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBgpImportPolicy.setStatus("obsolete")
_SvcDhcpLseStateBgpExportPolicy_Type = TPolicyStatementNameOrEmpty
_SvcDhcpLseStateBgpExportPolicy_Object = MibTableColumn
svcDhcpLseStateBgpExportPolicy = _SvcDhcpLseStateBgpExportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 53, 1, 5),
    _SvcDhcpLseStateBgpExportPolicy_Type()
)
svcDhcpLseStateBgpExportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBgpExportPolicy.setStatus("obsolete")
_SvcDhcpLseStateBgpPeerAS_Type = InetAutonomousSystemNumber
_SvcDhcpLseStateBgpPeerAS_Object = MibTableColumn
svcDhcpLseStateBgpPeerAS = _SvcDhcpLseStateBgpPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 53, 1, 6),
    _SvcDhcpLseStateBgpPeerAS_Type()
)
svcDhcpLseStateBgpPeerAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBgpPeerAS.setStatus("obsolete")
_SvcDhcpLseStateBgpPeeringStatus_Type = BgpPeeringStatus
_SvcDhcpLseStateBgpPeeringStatus_Object = MibTableColumn
svcDhcpLseStateBgpPeeringStatus = _SvcDhcpLseStateBgpPeeringStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 53, 1, 7),
    _SvcDhcpLseStateBgpPeeringStatus_Type()
)
svcDhcpLseStateBgpPeeringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBgpPeeringStatus.setStatus("obsolete")
_SvcArpHostMRtTable_Object = MibTable
svcArpHostMRtTable = _SvcArpHostMRtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 54)
)
if mibBuilder.loadTexts:
    svcArpHostMRtTable.setStatus("current")
_SvcArpHostMRtEntry_Object = MibTableRow
svcArpHostMRtEntry = _SvcArpHostMRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 54, 1)
)
svcArpHostMRtEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostIpAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostIpAddr"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostMRtAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostMRtAddr"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostMRtPrefixLen"),
)
if mibBuilder.loadTexts:
    svcArpHostMRtEntry.setStatus("current")
_SvcArpHostMRtAddrType_Type = InetAddressType
_SvcArpHostMRtAddrType_Object = MibTableColumn
svcArpHostMRtAddrType = _SvcArpHostMRtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 54, 1, 1),
    _SvcArpHostMRtAddrType_Type()
)
svcArpHostMRtAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcArpHostMRtAddrType.setStatus("current")


class _SvcArpHostMRtAddr_Type(InetAddress):
    """Custom type svcArpHostMRtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SvcArpHostMRtAddr_Type.__name__ = "InetAddress"
_SvcArpHostMRtAddr_Object = MibTableColumn
svcArpHostMRtAddr = _SvcArpHostMRtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 54, 1, 2),
    _SvcArpHostMRtAddr_Type()
)
svcArpHostMRtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcArpHostMRtAddr.setStatus("current")
_SvcArpHostMRtPrefixLen_Type = InetAddressPrefixLength
_SvcArpHostMRtPrefixLen_Object = MibTableColumn
svcArpHostMRtPrefixLen = _SvcArpHostMRtPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 54, 1, 3),
    _SvcArpHostMRtPrefixLen_Type()
)
svcArpHostMRtPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcArpHostMRtPrefixLen.setStatus("current")
_SvcArpHostMRtStatus_Type = TmnxManagedRouteStatus
_SvcArpHostMRtStatus_Object = MibTableColumn
svcArpHostMRtStatus = _SvcArpHostMRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 54, 1, 4),
    _SvcArpHostMRtStatus_Type()
)
svcArpHostMRtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostMRtStatus.setStatus("current")
_SvcArpHostBgpTable_Object = MibTable
svcArpHostBgpTable = _SvcArpHostBgpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 55)
)
if mibBuilder.loadTexts:
    svcArpHostBgpTable.setStatus("current")
_SvcArpHostBgpEntry_Object = MibTableRow
svcArpHostBgpEntry = _SvcArpHostBgpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 55, 1)
)
if mibBuilder.loadTexts:
    svcArpHostBgpEntry.setStatus("current")
_SvcArpHostBgpPrngPlcyName_Type = TNamedItemOrEmpty
_SvcArpHostBgpPrngPlcyName_Object = MibTableColumn
svcArpHostBgpPrngPlcyName = _SvcArpHostBgpPrngPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 55, 1, 1),
    _SvcArpHostBgpPrngPlcyName_Type()
)
svcArpHostBgpPrngPlcyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostBgpPrngPlcyName.setStatus("current")
_SvcArpHostBgpAuthKeyChain_Type = TNamedItemOrEmpty
_SvcArpHostBgpAuthKeyChain_Object = MibTableColumn
svcArpHostBgpAuthKeyChain = _SvcArpHostBgpAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 55, 1, 2),
    _SvcArpHostBgpAuthKeyChain_Type()
)
svcArpHostBgpAuthKeyChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostBgpAuthKeyChain.setStatus("current")


class _SvcArpHostBgpMD5AuthKey_Type(OctetString):
    """Custom type svcArpHostBgpMD5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvcArpHostBgpMD5AuthKey_Type.__name__ = "OctetString"
_SvcArpHostBgpMD5AuthKey_Object = MibTableColumn
svcArpHostBgpMD5AuthKey = _SvcArpHostBgpMD5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 55, 1, 3),
    _SvcArpHostBgpMD5AuthKey_Type()
)
svcArpHostBgpMD5AuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostBgpMD5AuthKey.setStatus("current")
_SvcArpHostBgpImportPolicy_Type = TPolicyStatementNameOrEmpty
_SvcArpHostBgpImportPolicy_Object = MibTableColumn
svcArpHostBgpImportPolicy = _SvcArpHostBgpImportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 55, 1, 4),
    _SvcArpHostBgpImportPolicy_Type()
)
svcArpHostBgpImportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostBgpImportPolicy.setStatus("current")
_SvcArpHostBgpExportPolicy_Type = TPolicyStatementNameOrEmpty
_SvcArpHostBgpExportPolicy_Object = MibTableColumn
svcArpHostBgpExportPolicy = _SvcArpHostBgpExportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 55, 1, 5),
    _SvcArpHostBgpExportPolicy_Type()
)
svcArpHostBgpExportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostBgpExportPolicy.setStatus("current")
_SvcArpHostBgpPeerAS_Type = InetAutonomousSystemNumber
_SvcArpHostBgpPeerAS_Object = MibTableColumn
svcArpHostBgpPeerAS = _SvcArpHostBgpPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 55, 1, 6),
    _SvcArpHostBgpPeerAS_Type()
)
svcArpHostBgpPeerAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostBgpPeerAS.setStatus("current")
_SvcArpHostBgpPeeringStatus_Type = BgpPeeringStatus
_SvcArpHostBgpPeeringStatus_Object = MibTableColumn
svcArpHostBgpPeeringStatus = _SvcArpHostBgpPeeringStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 55, 1, 7),
    _SvcArpHostBgpPeeringStatus_Type()
)
svcArpHostBgpPeeringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostBgpPeeringStatus.setStatus("current")
_SvcEpMcEpStatsTable_Object = MibTable
svcEpMcEpStatsTable = _SvcEpMcEpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 56)
)
if mibBuilder.loadTexts:
    svcEpMcEpStatsTable.setStatus("current")
_SvcEpMcEpStatsEntry_Object = MibTableRow
svcEpMcEpStatsEntry = _SvcEpMcEpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 56, 1)
)
svcEpMcEpStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcEndPointMCEPId"),
)
if mibBuilder.loadTexts:
    svcEpMcEpStatsEntry.setStatus("current")
_SvcEpMcEpStatsPktsRxConfig_Type = Counter32
_SvcEpMcEpStatsPktsRxConfig_Object = MibTableColumn
svcEpMcEpStatsPktsRxConfig = _SvcEpMcEpStatsPktsRxConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 56, 1, 1),
    _SvcEpMcEpStatsPktsRxConfig_Type()
)
svcEpMcEpStatsPktsRxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpMcEpStatsPktsRxConfig.setStatus("current")
_SvcEpMcEpStatsPktsRxState_Type = Counter32
_SvcEpMcEpStatsPktsRxState_Object = MibTableColumn
svcEpMcEpStatsPktsRxState = _SvcEpMcEpStatsPktsRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 56, 1, 2),
    _SvcEpMcEpStatsPktsRxState_Type()
)
svcEpMcEpStatsPktsRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpMcEpStatsPktsRxState.setStatus("current")
_SvcEpMcEpStatsPktsTxConfig_Type = Counter32
_SvcEpMcEpStatsPktsTxConfig_Object = MibTableColumn
svcEpMcEpStatsPktsTxConfig = _SvcEpMcEpStatsPktsTxConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 56, 1, 3),
    _SvcEpMcEpStatsPktsTxConfig_Type()
)
svcEpMcEpStatsPktsTxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpMcEpStatsPktsTxConfig.setStatus("current")
_SvcEpMcEpStatsPktsTxState_Type = Counter32
_SvcEpMcEpStatsPktsTxState_Object = MibTableColumn
svcEpMcEpStatsPktsTxState = _SvcEpMcEpStatsPktsTxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 56, 1, 4),
    _SvcEpMcEpStatsPktsTxState_Type()
)
svcEpMcEpStatsPktsTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpMcEpStatsPktsTxState.setStatus("current")
_SvcEpMcEpStatsPktsTxFailed_Type = Counter32
_SvcEpMcEpStatsPktsTxFailed_Object = MibTableColumn
svcEpMcEpStatsPktsTxFailed = _SvcEpMcEpStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 56, 1, 5),
    _SvcEpMcEpStatsPktsTxFailed_Type()
)
svcEpMcEpStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpMcEpStatsPktsTxFailed.setStatus("current")


class _SvcPbbSrcBVplsMacAddr_Type(MacAddress):
    """Custom type svcPbbSrcBVplsMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_SvcPbbSrcBVplsMacAddr_Object = MibScalar
svcPbbSrcBVplsMacAddr = _SvcPbbSrcBVplsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 57),
    _SvcPbbSrcBVplsMacAddr_Type()
)
svcPbbSrcBVplsMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPbbSrcBVplsMacAddr.setStatus("current")
_SvcMacNameTableLastChanged_Type = TimeStamp
_SvcMacNameTableLastChanged_Object = MibScalar
svcMacNameTableLastChanged = _SvcMacNameTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 58),
    _SvcMacNameTableLastChanged_Type()
)
svcMacNameTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMacNameTableLastChanged.setStatus("current")
_SvcMacNameTable_Object = MibTable
svcMacNameTable = _SvcMacNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 59)
)
if mibBuilder.loadTexts:
    svcMacNameTable.setStatus("current")
_SvcMacNameEntry_Object = MibTableRow
svcMacNameEntry = _SvcMacNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 59, 1)
)
svcMacNameEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcMacName"),
)
if mibBuilder.loadTexts:
    svcMacNameEntry.setStatus("current")
_SvcMacName_Type = TNamedItem
_SvcMacName_Object = MibTableColumn
svcMacName = _SvcMacName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 59, 1, 1),
    _SvcMacName_Type()
)
svcMacName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcMacName.setStatus("current")
_SvcMacNameRowStatus_Type = RowStatus
_SvcMacNameRowStatus_Object = MibTableColumn
svcMacNameRowStatus = _SvcMacNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 59, 1, 2),
    _SvcMacNameRowStatus_Type()
)
svcMacNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMacNameRowStatus.setStatus("current")
_SvcMacNameLastChngd_Type = TimeStamp
_SvcMacNameLastChngd_Object = MibTableColumn
svcMacNameLastChngd = _SvcMacNameLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 59, 1, 3),
    _SvcMacNameLastChngd_Type()
)
svcMacNameLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMacNameLastChngd.setStatus("current")
_SvcMacNameAddr_Type = MacAddress
_SvcMacNameAddr_Object = MibTableColumn
svcMacNameAddr = _SvcMacNameAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 59, 1, 4),
    _SvcMacNameAddr_Type()
)
svcMacNameAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMacNameAddr.setStatus("current")
_SvcMacNotificationGroup_ObjectIdentity = ObjectIdentity
svcMacNotificationGroup = _SvcMacNotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 60)
)


class _SvcMacNotifInterval_Type(Unsigned32):
    """Custom type svcMacNotifInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SvcMacNotifInterval_Type.__name__ = "Unsigned32"
_SvcMacNotifInterval_Object = MibScalar
svcMacNotifInterval = _SvcMacNotifInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 60, 1),
    _SvcMacNotifInterval_Type()
)
svcMacNotifInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcMacNotifInterval.setStatus("current")
if mibBuilder.loadTexts:
    svcMacNotifInterval.setUnits("deci-seconds")


class _SvcMacNotifCount_Type(Unsigned32):
    """Custom type svcMacNotifCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvcMacNotifCount_Type.__name__ = "Unsigned32"
_SvcMacNotifCount_Object = MibScalar
svcMacNotifCount = _SvcMacNotifCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 60, 2),
    _SvcMacNotifCount_Type()
)
svcMacNotifCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcMacNotifCount.setStatus("current")
_TlsProtMacImplTable_Object = MibTable
tlsProtMacImplTable = _TlsProtMacImplTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 61)
)
if mibBuilder.loadTexts:
    tlsProtMacImplTable.setStatus("current")
_TlsProtMacImplEntry_Object = MibTableRow
tlsProtMacImplEntry = _TlsProtMacImplEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 61, 1)
)
tlsProtMacImplEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsProtMacImplMacAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsProtMacImplLocale"),
    (0, "TIMETRA-SERV-MIB", "tlsProtMacImplPortId"),
    (0, "TIMETRA-SERV-MIB", "tlsProtMacImplEncapValue"),
    (0, "TIMETRA-SERV-MIB", "tlsProtMacImplSdpBindId"),
)
if mibBuilder.loadTexts:
    tlsProtMacImplEntry.setStatus("current")
_TlsProtMacImplMacAddr_Type = MacAddress
_TlsProtMacImplMacAddr_Object = MibTableColumn
tlsProtMacImplMacAddr = _TlsProtMacImplMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 61, 1, 1),
    _TlsProtMacImplMacAddr_Type()
)
tlsProtMacImplMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsProtMacImplMacAddr.setStatus("current")


class _TlsProtMacImplLocale_Type(Integer32):
    """Custom type tlsProtMacImplLocale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("sap", 1),
          ("sdp", 2))
    )


_TlsProtMacImplLocale_Type.__name__ = "Integer32"
_TlsProtMacImplLocale_Object = MibTableColumn
tlsProtMacImplLocale = _TlsProtMacImplLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 61, 1, 2),
    _TlsProtMacImplLocale_Type()
)
tlsProtMacImplLocale.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsProtMacImplLocale.setStatus("current")
_TlsProtMacImplPortId_Type = TmnxPortID
_TlsProtMacImplPortId_Object = MibTableColumn
tlsProtMacImplPortId = _TlsProtMacImplPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 61, 1, 3),
    _TlsProtMacImplPortId_Type()
)
tlsProtMacImplPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsProtMacImplPortId.setStatus("current")
_TlsProtMacImplEncapValue_Type = TmnxEncapVal
_TlsProtMacImplEncapValue_Object = MibTableColumn
tlsProtMacImplEncapValue = _TlsProtMacImplEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 61, 1, 4),
    _TlsProtMacImplEncapValue_Type()
)
tlsProtMacImplEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsProtMacImplEncapValue.setStatus("current")
_TlsProtMacImplSdpBindId_Type = SdpBindId
_TlsProtMacImplSdpBindId_Object = MibTableColumn
tlsProtMacImplSdpBindId = _TlsProtMacImplSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 61, 1, 5),
    _TlsProtMacImplSdpBindId_Type()
)
tlsProtMacImplSdpBindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsProtMacImplSdpBindId.setStatus("current")
_TlsProtMacImplCount_Type = Counter32
_TlsProtMacImplCount_Object = MibTableColumn
tlsProtMacImplCount = _TlsProtMacImplCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 61, 1, 6),
    _TlsProtMacImplCount_Type()
)
tlsProtMacImplCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsProtMacImplCount.setStatus("current")
_SvcNameTableLastChanged_Type = TimeStamp
_SvcNameTableLastChanged_Object = MibScalar
svcNameTableLastChanged = _SvcNameTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 62),
    _SvcNameTableLastChanged_Type()
)
svcNameTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNameTableLastChanged.setStatus("current")
_SvcNameTable_Object = MibTable
svcNameTable = _SvcNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 63)
)
if mibBuilder.loadTexts:
    svcNameTable.setStatus("current")
_SvcNameEntry_Object = MibTableRow
svcNameEntry = _SvcNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 63, 1)
)
svcNameEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcName"),
)
if mibBuilder.loadTexts:
    svcNameEntry.setStatus("current")


class _SvcNameId_Type(TmnxServId):
    """Custom type svcNameId based on TmnxServId"""
    defaultValue = 0


_SvcNameId_Object = MibTableColumn
svcNameId = _SvcNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 63, 1, 1),
    _SvcNameId_Type()
)
svcNameId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcNameId.setStatus("current")
_SvcNameRowStatus_Type = RowStatus
_SvcNameRowStatus_Object = MibTableColumn
svcNameRowStatus = _SvcNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 63, 1, 2),
    _SvcNameRowStatus_Type()
)
svcNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcNameRowStatus.setStatus("current")
_SvcNameLastChanged_Type = TimeStamp
_SvcNameLastChanged_Object = MibTableColumn
svcNameLastChanged = _SvcNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 63, 1, 3),
    _SvcNameLastChanged_Type()
)
svcNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNameLastChanged.setStatus("current")


class _SvcNameType_Type(ServType):
    """Custom type svcNameType based on ServType"""


_SvcNameType_Object = MibTableColumn
svcNameType = _SvcNameType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 63, 1, 4),
    _SvcNameType_Type()
)
svcNameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcNameType.setStatus("current")
_SvcMrpPlcyTableLastChgd_Type = TimeStamp
_SvcMrpPlcyTableLastChgd_Object = MibScalar
svcMrpPlcyTableLastChgd = _SvcMrpPlcyTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 64),
    _SvcMrpPlcyTableLastChgd_Type()
)
svcMrpPlcyTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMrpPlcyTableLastChgd.setStatus("current")
_SvcMrpPolicyTable_Object = MibTable
svcMrpPolicyTable = _SvcMrpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 65)
)
if mibBuilder.loadTexts:
    svcMrpPolicyTable.setStatus("current")
_SvcMrpPolicyEntry_Object = MibTableRow
svcMrpPolicyEntry = _SvcMrpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 65, 1)
)
svcMrpPolicyEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcMrpPolicyName"),
)
if mibBuilder.loadTexts:
    svcMrpPolicyEntry.setStatus("current")
_SvcMrpPolicyName_Type = TNamedItem
_SvcMrpPolicyName_Object = MibTableColumn
svcMrpPolicyName = _SvcMrpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 65, 1, 1),
    _SvcMrpPolicyName_Type()
)
svcMrpPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcMrpPolicyName.setStatus("current")
_SvcMrpPolicyRowStatus_Type = RowStatus
_SvcMrpPolicyRowStatus_Object = MibTableColumn
svcMrpPolicyRowStatus = _SvcMrpPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 65, 1, 2),
    _SvcMrpPolicyRowStatus_Type()
)
svcMrpPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMrpPolicyRowStatus.setStatus("current")
_SvcMrpPolicyLastChanged_Type = TimeStamp
_SvcMrpPolicyLastChanged_Object = MibTableColumn
svcMrpPolicyLastChanged = _SvcMrpPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 65, 1, 3),
    _SvcMrpPolicyLastChanged_Type()
)
svcMrpPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMrpPolicyLastChanged.setStatus("current")
_SvcMrpPolicyDescription_Type = TItemDescription
_SvcMrpPolicyDescription_Object = MibTableColumn
svcMrpPolicyDescription = _SvcMrpPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 65, 1, 4),
    _SvcMrpPolicyDescription_Type()
)
svcMrpPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMrpPolicyDescription.setStatus("current")


class _SvcMrpPolicyScope_Type(TItemScope):
    """Custom type svcMrpPolicyScope based on TItemScope"""


_SvcMrpPolicyScope_Object = MibTableColumn
svcMrpPolicyScope = _SvcMrpPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 65, 1, 5),
    _SvcMrpPolicyScope_Type()
)
svcMrpPolicyScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMrpPolicyScope.setStatus("current")


class _SvcMrpPolicyDefaultAction_Type(TMrpPolicyDefaultAction):
    """Custom type svcMrpPolicyDefaultAction based on TMrpPolicyDefaultAction"""


_SvcMrpPolicyDefaultAction_Object = MibTableColumn
svcMrpPolicyDefaultAction = _SvcMrpPolicyDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 65, 1, 6),
    _SvcMrpPolicyDefaultAction_Type()
)
svcMrpPolicyDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMrpPolicyDefaultAction.setStatus("current")
_SvcMrpPlcyParamsTblLastChgd_Type = TimeStamp
_SvcMrpPlcyParamsTblLastChgd_Object = MibScalar
svcMrpPlcyParamsTblLastChgd = _SvcMrpPlcyParamsTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 66),
    _SvcMrpPlcyParamsTblLastChgd_Type()
)
svcMrpPlcyParamsTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMrpPlcyParamsTblLastChgd.setStatus("current")
_SvcMrpPolicyParamsTable_Object = MibTable
svcMrpPolicyParamsTable = _SvcMrpPolicyParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 67)
)
if mibBuilder.loadTexts:
    svcMrpPolicyParamsTable.setStatus("current")
_SvcMrpPolicyParamsEntry_Object = MibTableRow
svcMrpPolicyParamsEntry = _SvcMrpPolicyParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 67, 1)
)
svcMrpPolicyParamsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcMrpPolicyName"),
    (0, "TIMETRA-SERV-MIB", "svcMrpPolicyParamsEntryId"),
)
if mibBuilder.loadTexts:
    svcMrpPolicyParamsEntry.setStatus("current")
_SvcMrpPolicyParamsEntryId_Type = TEntryId
_SvcMrpPolicyParamsEntryId_Object = MibTableColumn
svcMrpPolicyParamsEntryId = _SvcMrpPolicyParamsEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 67, 1, 1),
    _SvcMrpPolicyParamsEntryId_Type()
)
svcMrpPolicyParamsEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcMrpPolicyParamsEntryId.setStatus("current")
_SvcMrpPolicyParamsRowStatus_Type = RowStatus
_SvcMrpPolicyParamsRowStatus_Object = MibTableColumn
svcMrpPolicyParamsRowStatus = _SvcMrpPolicyParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 67, 1, 2),
    _SvcMrpPolicyParamsRowStatus_Type()
)
svcMrpPolicyParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMrpPolicyParamsRowStatus.setStatus("current")
_SvcMrpPolicyParamsLastChanged_Type = TimeStamp
_SvcMrpPolicyParamsLastChanged_Object = MibTableColumn
svcMrpPolicyParamsLastChanged = _SvcMrpPolicyParamsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 67, 1, 3),
    _SvcMrpPolicyParamsLastChanged_Type()
)
svcMrpPolicyParamsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMrpPolicyParamsLastChanged.setStatus("current")
_SvcMrpPolicyParamsDescription_Type = TItemDescription
_SvcMrpPolicyParamsDescription_Object = MibTableColumn
svcMrpPolicyParamsDescription = _SvcMrpPolicyParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 67, 1, 4),
    _SvcMrpPolicyParamsDescription_Type()
)
svcMrpPolicyParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMrpPolicyParamsDescription.setStatus("current")


class _SvcMrpPolicyParamsAction_Type(TMrpPolicyAction):
    """Custom type svcMrpPolicyParamsAction based on TMrpPolicyAction"""


_SvcMrpPolicyParamsAction_Object = MibTableColumn
svcMrpPolicyParamsAction = _SvcMrpPolicyParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 67, 1, 5),
    _SvcMrpPolicyParamsAction_Type()
)
svcMrpPolicyParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMrpPolicyParamsAction.setStatus("current")
_SvcMrpPlcyParamsISIDTblLastChgd_Type = TimeStamp
_SvcMrpPlcyParamsISIDTblLastChgd_Object = MibScalar
svcMrpPlcyParamsISIDTblLastChgd = _SvcMrpPlcyParamsISIDTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 68),
    _SvcMrpPlcyParamsISIDTblLastChgd_Type()
)
svcMrpPlcyParamsISIDTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMrpPlcyParamsISIDTblLastChgd.setStatus("current")
_SvcMrpPolicyParamsISIDTable_Object = MibTable
svcMrpPolicyParamsISIDTable = _SvcMrpPolicyParamsISIDTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 69)
)
if mibBuilder.loadTexts:
    svcMrpPolicyParamsISIDTable.setStatus("current")
_SvcMrpPolicyParamsISIDEntry_Object = MibTableRow
svcMrpPolicyParamsISIDEntry = _SvcMrpPolicyParamsISIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 69, 1)
)
svcMrpPolicyParamsISIDEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcMrpPolicyName"),
    (0, "TIMETRA-SERV-MIB", "svcMrpPolicyParamsEntryId"),
    (0, "TIMETRA-SERV-MIB", "svcMrpPolicyParamsISIDLow"),
)
if mibBuilder.loadTexts:
    svcMrpPolicyParamsISIDEntry.setStatus("current")


class _SvcMrpPolicyParamsISIDLow_Type(SvcISID):
    """Custom type svcMrpPolicyParamsISIDLow based on SvcISID"""
    subtypeSpec = SvcISID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SvcMrpPolicyParamsISIDLow_Type.__name__ = "SvcISID"
_SvcMrpPolicyParamsISIDLow_Object = MibTableColumn
svcMrpPolicyParamsISIDLow = _SvcMrpPolicyParamsISIDLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 69, 1, 1),
    _SvcMrpPolicyParamsISIDLow_Type()
)
svcMrpPolicyParamsISIDLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcMrpPolicyParamsISIDLow.setStatus("current")


class _SvcMrpPolicyParamsISIDHigh_Type(SvcISID):
    """Custom type svcMrpPolicyParamsISIDHigh based on SvcISID"""
    subtypeSpec = SvcISID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_SvcMrpPolicyParamsISIDHigh_Type.__name__ = "SvcISID"
_SvcMrpPolicyParamsISIDHigh_Object = MibTableColumn
svcMrpPolicyParamsISIDHigh = _SvcMrpPolicyParamsISIDHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 69, 1, 2),
    _SvcMrpPolicyParamsISIDHigh_Type()
)
svcMrpPolicyParamsISIDHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMrpPolicyParamsISIDHigh.setStatus("current")
_SvcMrpPolicyParamsISIDRowStatus_Type = RowStatus
_SvcMrpPolicyParamsISIDRowStatus_Object = MibTableColumn
svcMrpPolicyParamsISIDRowStatus = _SvcMrpPolicyParamsISIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 69, 1, 3),
    _SvcMrpPolicyParamsISIDRowStatus_Type()
)
svcMrpPolicyParamsISIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMrpPolicyParamsISIDRowStatus.setStatus("current")
_SvcMrpPolicyParamsISIDLastChgd_Type = TimeStamp
_SvcMrpPolicyParamsISIDLastChgd_Object = MibTableColumn
svcMrpPolicyParamsISIDLastChgd = _SvcMrpPolicyParamsISIDLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 69, 1, 4),
    _SvcMrpPolicyParamsISIDLastChgd_Type()
)
svcMrpPolicyParamsISIDLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMrpPolicyParamsISIDLastChgd.setStatus("current")
_SvcEpipeTableLastChanged_Type = TimeStamp
_SvcEpipeTableLastChanged_Object = MibScalar
svcEpipeTableLastChanged = _SvcEpipeTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 70),
    _SvcEpipeTableLastChanged_Type()
)
svcEpipeTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpipeTableLastChanged.setStatus("current")
_SvcEpipeTable_Object = MibTable
svcEpipeTable = _SvcEpipeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 71)
)
if mibBuilder.loadTexts:
    svcEpipeTable.setStatus("current")
_SvcEpipeEntry_Object = MibTableRow
svcEpipeEntry = _SvcEpipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 71, 1)
)
svcEpipeEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcEpipeEntry.setStatus("current")
_SvcEpipeLastChngd_Type = TimeStamp
_SvcEpipeLastChngd_Object = MibTableColumn
svcEpipeLastChngd = _SvcEpipeLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 71, 1, 1),
    _SvcEpipeLastChngd_Type()
)
svcEpipeLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpipeLastChngd.setStatus("current")


class _SvcEpipePerSvcHashing_Type(TmnxEnabledDisabled):
    """Custom type svcEpipePerSvcHashing based on TmnxEnabledDisabled"""


_SvcEpipePerSvcHashing_Object = MibTableColumn
svcEpipePerSvcHashing = _SvcEpipePerSvcHashing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 71, 1, 2),
    _SvcEpipePerSvcHashing_Type()
)
svcEpipePerSvcHashing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcEpipePerSvcHashing.setStatus("current")
_SvcEpipeBackboneTableLastChanged_Type = TimeStamp
_SvcEpipeBackboneTableLastChanged_Object = MibScalar
svcEpipeBackboneTableLastChanged = _SvcEpipeBackboneTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 72),
    _SvcEpipeBackboneTableLastChanged_Type()
)
svcEpipeBackboneTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpipeBackboneTableLastChanged.setStatus("current")
_SvcEpipeBackboneTable_Object = MibTable
svcEpipeBackboneTable = _SvcEpipeBackboneTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 73)
)
if mibBuilder.loadTexts:
    svcEpipeBackboneTable.setStatus("current")
_SvcEpipeBackboneEntry_Object = MibTableRow
svcEpipeBackboneEntry = _SvcEpipeBackboneEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 73, 1)
)
svcEpipeBackboneEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcEpipeBackboneEntry.setStatus("current")
_SvcEpipeBackboneLastChngd_Type = TimeStamp
_SvcEpipeBackboneLastChngd_Object = MibTableColumn
svcEpipeBackboneLastChngd = _SvcEpipeBackboneLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 73, 1, 1),
    _SvcEpipeBackboneLastChngd_Type()
)
svcEpipeBackboneLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEpipeBackboneLastChngd.setStatus("current")


class _SvcEpipeBackboneForceQTagFwd_Type(TruthValue):
    """Custom type svcEpipeBackboneForceQTagFwd based on TruthValue"""


_SvcEpipeBackboneForceQTagFwd_Object = MibTableColumn
svcEpipeBackboneForceQTagFwd = _SvcEpipeBackboneForceQTagFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 73, 1, 2),
    _SvcEpipeBackboneForceQTagFwd_Type()
)
svcEpipeBackboneForceQTagFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcEpipeBackboneForceQTagFwd.setStatus("current")
_SvcTlsSiteIdTblLastChanged_Type = TimeStamp
_SvcTlsSiteIdTblLastChanged_Object = MibScalar
svcTlsSiteIdTblLastChanged = _SvcTlsSiteIdTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 74),
    _SvcTlsSiteIdTblLastChanged_Type()
)
svcTlsSiteIdTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSiteIdTblLastChanged.setStatus("current")
_SvcTlsSiteIdTable_Object = MibTable
svcTlsSiteIdTable = _SvcTlsSiteIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75)
)
if mibBuilder.loadTexts:
    svcTlsSiteIdTable.setStatus("current")
_SvcTlsSiteIdEntry_Object = MibTableRow
svcTlsSiteIdEntry = _SvcTlsSiteIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1)
)
svcTlsSiteIdEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcTlsSiteIdName"),
)
if mibBuilder.loadTexts:
    svcTlsSiteIdEntry.setStatus("current")
_SvcTlsSiteIdName_Type = TNamedItem
_SvcTlsSiteIdName_Object = MibTableColumn
svcTlsSiteIdName = _SvcTlsSiteIdName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 1),
    _SvcTlsSiteIdName_Type()
)
svcTlsSiteIdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcTlsSiteIdName.setStatus("current")
_SvcTlsSiteIdRowStatus_Type = RowStatus
_SvcTlsSiteIdRowStatus_Object = MibTableColumn
svcTlsSiteIdRowStatus = _SvcTlsSiteIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 2),
    _SvcTlsSiteIdRowStatus_Type()
)
svcTlsSiteIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdRowStatus.setStatus("current")
_SvcTlsSiteIdLastChanged_Type = TimeStamp
_SvcTlsSiteIdLastChanged_Object = MibTableColumn
svcTlsSiteIdLastChanged = _SvcTlsSiteIdLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 3),
    _SvcTlsSiteIdLastChanged_Type()
)
svcTlsSiteIdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSiteIdLastChanged.setStatus("current")


class _SvcTlsSiteIdAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type svcTlsSiteIdAdminStatus based on TmnxEnabledDisabled"""


_SvcTlsSiteIdAdminStatus_Object = MibTableColumn
svcTlsSiteIdAdminStatus = _SvcTlsSiteIdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 4),
    _SvcTlsSiteIdAdminStatus_Type()
)
svcTlsSiteIdAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdAdminStatus.setStatus("current")


class _SvcTlsSiteIdSiteId_Type(TmnxSiteId):
    """Custom type svcTlsSiteIdSiteId based on TmnxSiteId"""
    defaultValue = -1


_SvcTlsSiteIdSiteId_Object = MibTableColumn
svcTlsSiteIdSiteId = _SvcTlsSiteIdSiteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 5),
    _SvcTlsSiteIdSiteId_Type()
)
svcTlsSiteIdSiteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdSiteId.setStatus("current")


class _SvcTlsSiteIdPortId_Type(TmnxPortID):
    """Custom type svcTlsSiteIdPortId based on TmnxPortID"""
    defaultHexValue = 503316480


_SvcTlsSiteIdPortId_Object = MibTableColumn
svcTlsSiteIdPortId = _SvcTlsSiteIdPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 6),
    _SvcTlsSiteIdPortId_Type()
)
svcTlsSiteIdPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdPortId.setStatus("current")


class _SvcTlsSiteIdEncapValue_Type(TmnxEncapVal):
    """Custom type svcTlsSiteIdEncapValue based on TmnxEncapVal"""
    defaultValue = 0


_SvcTlsSiteIdEncapValue_Object = MibTableColumn
svcTlsSiteIdEncapValue = _SvcTlsSiteIdEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 7),
    _SvcTlsSiteIdEncapValue_Type()
)
svcTlsSiteIdEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdEncapValue.setStatus("current")


class _SvcTlsSiteIdSdpBindId_Type(SdpBindId):
    """Custom type svcTlsSiteIdSdpBindId based on SdpBindId"""
    defaultHexValue = ""


_SvcTlsSiteIdSdpBindId_Object = MibTableColumn
svcTlsSiteIdSdpBindId = _SvcTlsSiteIdSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 8),
    _SvcTlsSiteIdSdpBindId_Type()
)
svcTlsSiteIdSdpBindId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdSdpBindId.setStatus("current")


class _SvcTlsSiteIdShgName_Type(TNamedItemOrEmpty):
    """Custom type svcTlsSiteIdShgName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SvcTlsSiteIdShgName_Object = MibTableColumn
svcTlsSiteIdShgName = _SvcTlsSiteIdShgName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 9),
    _SvcTlsSiteIdShgName_Type()
)
svcTlsSiteIdShgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdShgName.setStatus("current")


class _SvcTlsSiteIdShgMeshSdp_Type(TruthValue):
    """Custom type svcTlsSiteIdShgMeshSdp based on TruthValue"""


_SvcTlsSiteIdShgMeshSdp_Object = MibTableColumn
svcTlsSiteIdShgMeshSdp = _SvcTlsSiteIdShgMeshSdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 10),
    _SvcTlsSiteIdShgMeshSdp_Type()
)
svcTlsSiteIdShgMeshSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdShgMeshSdp.setStatus("current")


class _SvcTlsSiteIdFailedThresh_Type(Integer32):
    """Custom type svcTlsSiteIdFailedThresh based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1000),
    )


_SvcTlsSiteIdFailedThresh_Type.__name__ = "Integer32"
_SvcTlsSiteIdFailedThresh_Object = MibTableColumn
svcTlsSiteIdFailedThresh = _SvcTlsSiteIdFailedThresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 11),
    _SvcTlsSiteIdFailedThresh_Type()
)
svcTlsSiteIdFailedThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdFailedThresh.setStatus("current")
_SvcTlsSiteIdOperStatus_Type = TSiteOperStatus
_SvcTlsSiteIdOperStatus_Object = MibTableColumn
svcTlsSiteIdOperStatus = _SvcTlsSiteIdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 12),
    _SvcTlsSiteIdOperStatus_Type()
)
svcTlsSiteIdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSiteIdOperStatus.setStatus("current")
_SvcTlsSiteIdDesignatedFwdr_Type = TruthValue
_SvcTlsSiteIdDesignatedFwdr_Object = MibTableColumn
svcTlsSiteIdDesignatedFwdr = _SvcTlsSiteIdDesignatedFwdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 13),
    _SvcTlsSiteIdDesignatedFwdr_Type()
)
svcTlsSiteIdDesignatedFwdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSiteIdDesignatedFwdr.setStatus("current")


class _SvcTlsSiteIdBootTimer_Type(Integer32):
    """Custom type svcTlsSiteIdBootTimer based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 600),
    )


_SvcTlsSiteIdBootTimer_Type.__name__ = "Integer32"
_SvcTlsSiteIdBootTimer_Object = MibTableColumn
svcTlsSiteIdBootTimer = _SvcTlsSiteIdBootTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 14),
    _SvcTlsSiteIdBootTimer_Type()
)
svcTlsSiteIdBootTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdBootTimer.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsSiteIdBootTimer.setUnits("seconds")


class _SvcTlsSiteIdSiteActTimer_Type(Integer32):
    """Custom type svcTlsSiteIdSiteActTimer based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_SvcTlsSiteIdSiteActTimer_Type.__name__ = "Integer32"
_SvcTlsSiteIdSiteActTimer_Object = MibTableColumn
svcTlsSiteIdSiteActTimer = _SvcTlsSiteIdSiteActTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 15),
    _SvcTlsSiteIdSiteActTimer_Type()
)
svcTlsSiteIdSiteActTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdSiteActTimer.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsSiteIdSiteActTimer.setUnits("seconds")
_SvcTlsSiteIdDfUpTime_Type = Unsigned32
_SvcTlsSiteIdDfUpTime_Object = MibTableColumn
svcTlsSiteIdDfUpTime = _SvcTlsSiteIdDfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 16),
    _SvcTlsSiteIdDfUpTime_Type()
)
svcTlsSiteIdDfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSiteIdDfUpTime.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsSiteIdDfUpTime.setUnits("seconds")
_SvcTlsSiteIdDfChgCnt_Type = Unsigned32
_SvcTlsSiteIdDfChgCnt_Object = MibTableColumn
svcTlsSiteIdDfChgCnt = _SvcTlsSiteIdDfChgCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 17),
    _SvcTlsSiteIdDfChgCnt_Type()
)
svcTlsSiteIdDfChgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSiteIdDfChgCnt.setStatus("current")
_SvcTlsSiteIdTimerRemain_Type = Unsigned32
_SvcTlsSiteIdTimerRemain_Object = MibTableColumn
svcTlsSiteIdTimerRemain = _SvcTlsSiteIdTimerRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 18),
    _SvcTlsSiteIdTimerRemain_Type()
)
svcTlsSiteIdTimerRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSiteIdTimerRemain.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsSiteIdTimerRemain.setUnits("seconds")
_SvcTlsSiteIdMonitorOperGrp_Type = TNamedItemOrEmpty
_SvcTlsSiteIdMonitorOperGrp_Object = MibTableColumn
svcTlsSiteIdMonitorOperGrp = _SvcTlsSiteIdMonitorOperGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 75, 1, 19),
    _SvcTlsSiteIdMonitorOperGrp_Type()
)
svcTlsSiteIdMonitorOperGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSiteIdMonitorOperGrp.setStatus("current")
_SvcBgpVplsTblLastChanged_Type = TimeStamp
_SvcBgpVplsTblLastChanged_Object = MibScalar
svcBgpVplsTblLastChanged = _SvcBgpVplsTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 78),
    _SvcBgpVplsTblLastChanged_Type()
)
svcBgpVplsTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcBgpVplsTblLastChanged.setStatus("current")
_SvcBgpVplsTable_Object = MibTable
svcBgpVplsTable = _SvcBgpVplsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 79)
)
if mibBuilder.loadTexts:
    svcBgpVplsTable.setStatus("current")
_SvcBgpVplsEntry_Object = MibTableRow
svcBgpVplsEntry = _SvcBgpVplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 79, 1)
)
svcBgpVplsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcBgpVplsEntry.setStatus("current")
_SvcBgpVplsRowStatus_Type = RowStatus
_SvcBgpVplsRowStatus_Object = MibTableColumn
svcBgpVplsRowStatus = _SvcBgpVplsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 79, 1, 1),
    _SvcBgpVplsRowStatus_Type()
)
svcBgpVplsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcBgpVplsRowStatus.setStatus("current")
_SvcBgpVplsLastChanged_Type = TimeStamp
_SvcBgpVplsLastChanged_Object = MibTableColumn
svcBgpVplsLastChanged = _SvcBgpVplsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 79, 1, 2),
    _SvcBgpVplsLastChanged_Type()
)
svcBgpVplsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcBgpVplsLastChanged.setStatus("current")


class _SvcBgpVplsMaxVeId_Type(Integer32):
    """Custom type svcBgpVplsMaxVeId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65535),
    )


_SvcBgpVplsMaxVeId_Type.__name__ = "Integer32"
_SvcBgpVplsMaxVeId_Object = MibTableColumn
svcBgpVplsMaxVeId = _SvcBgpVplsMaxVeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 79, 1, 3),
    _SvcBgpVplsMaxVeId_Type()
)
svcBgpVplsMaxVeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcBgpVplsMaxVeId.setStatus("current")


class _SvcBgpVplsAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type svcBgpVplsAdminStatus based on TmnxEnabledDisabled"""


_SvcBgpVplsAdminStatus_Object = MibTableColumn
svcBgpVplsAdminStatus = _SvcBgpVplsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 79, 1, 4),
    _SvcBgpVplsAdminStatus_Type()
)
svcBgpVplsAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcBgpVplsAdminStatus.setStatus("current")


class _SvcBgpVplsVeName_Type(TNamedItemOrEmpty):
    """Custom type svcBgpVplsVeName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SvcBgpVplsVeName_Object = MibTableColumn
svcBgpVplsVeName = _SvcBgpVplsVeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 79, 1, 5),
    _SvcBgpVplsVeName_Type()
)
svcBgpVplsVeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcBgpVplsVeName.setStatus("current")


class _SvcBgpVplsVeId_Type(TmnxSiteId):
    """Custom type svcBgpVplsVeId based on TmnxSiteId"""
    defaultValue = -1


_SvcBgpVplsVeId_Object = MibTableColumn
svcBgpVplsVeId = _SvcBgpVplsVeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 79, 1, 6),
    _SvcBgpVplsVeId_Type()
)
svcBgpVplsVeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcBgpVplsVeId.setStatus("current")
_SvcTlsBgpTableLastChanged_Type = TimeStamp
_SvcTlsBgpTableLastChanged_Object = MibScalar
svcTlsBgpTableLastChanged = _SvcTlsBgpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 80),
    _SvcTlsBgpTableLastChanged_Type()
)
svcTlsBgpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpTableLastChanged.setStatus("current")
_SvcTlsBgpTable_Object = MibTable
svcTlsBgpTable = _SvcTlsBgpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81)
)
if mibBuilder.loadTexts:
    svcTlsBgpTable.setStatus("current")
_SvcTlsBgpEntry_Object = MibTableRow
svcTlsBgpEntry = _SvcTlsBgpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1)
)
svcTlsBgpEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcTlsBgpEntry.setStatus("current")
_SvcTlsBgpLastChanged_Type = TimeStamp
_SvcTlsBgpLastChanged_Object = MibTableColumn
svcTlsBgpLastChanged = _SvcTlsBgpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 1),
    _SvcTlsBgpLastChanged_Type()
)
svcTlsBgpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpLastChanged.setStatus("current")


class _SvcTlsBgpVsiRD_Type(TmnxVPNRouteDistinguisher):
    """Custom type svcTlsBgpVsiRD based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_SvcTlsBgpVsiRD_Object = MibTableColumn
svcTlsBgpVsiRD = _SvcTlsBgpVsiRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 2),
    _SvcTlsBgpVsiRD_Type()
)
svcTlsBgpVsiRD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiRD.setStatus("current")
_SvcTlsBgpExportRteTarget_Type = TNamedItemOrEmpty
_SvcTlsBgpExportRteTarget_Object = MibTableColumn
svcTlsBgpExportRteTarget = _SvcTlsBgpExportRteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 3),
    _SvcTlsBgpExportRteTarget_Type()
)
svcTlsBgpExportRteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpExportRteTarget.setStatus("current")


class _SvcTlsBgpVsiExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpVsiExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpVsiExportPolicy1_Object = MibTableColumn
svcTlsBgpVsiExportPolicy1 = _SvcTlsBgpVsiExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 4),
    _SvcTlsBgpVsiExportPolicy1_Type()
)
svcTlsBgpVsiExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiExportPolicy1.setStatus("current")


class _SvcTlsBgpVsiExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpVsiExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpVsiExportPolicy2_Object = MibTableColumn
svcTlsBgpVsiExportPolicy2 = _SvcTlsBgpVsiExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 5),
    _SvcTlsBgpVsiExportPolicy2_Type()
)
svcTlsBgpVsiExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiExportPolicy2.setStatus("current")


class _SvcTlsBgpVsiExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpVsiExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpVsiExportPolicy3_Object = MibTableColumn
svcTlsBgpVsiExportPolicy3 = _SvcTlsBgpVsiExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 6),
    _SvcTlsBgpVsiExportPolicy3_Type()
)
svcTlsBgpVsiExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiExportPolicy3.setStatus("current")


class _SvcTlsBgpVsiExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpVsiExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpVsiExportPolicy4_Object = MibTableColumn
svcTlsBgpVsiExportPolicy4 = _SvcTlsBgpVsiExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 7),
    _SvcTlsBgpVsiExportPolicy4_Type()
)
svcTlsBgpVsiExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiExportPolicy4.setStatus("current")


class _SvcTlsBgpVsiExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpVsiExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpVsiExportPolicy5_Object = MibTableColumn
svcTlsBgpVsiExportPolicy5 = _SvcTlsBgpVsiExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 8),
    _SvcTlsBgpVsiExportPolicy5_Type()
)
svcTlsBgpVsiExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiExportPolicy5.setStatus("current")
_SvcTlsBgpImportRteTarget_Type = TNamedItemOrEmpty
_SvcTlsBgpImportRteTarget_Object = MibTableColumn
svcTlsBgpImportRteTarget = _SvcTlsBgpImportRteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 9),
    _SvcTlsBgpImportRteTarget_Type()
)
svcTlsBgpImportRteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpImportRteTarget.setStatus("current")


class _SvcTlsBgpVsiImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpVsiImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpVsiImportPolicy1_Object = MibTableColumn
svcTlsBgpVsiImportPolicy1 = _SvcTlsBgpVsiImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 10),
    _SvcTlsBgpVsiImportPolicy1_Type()
)
svcTlsBgpVsiImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiImportPolicy1.setStatus("current")


class _SvcTlsBgpVsiImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpVsiImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpVsiImportPolicy2_Object = MibTableColumn
svcTlsBgpVsiImportPolicy2 = _SvcTlsBgpVsiImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 11),
    _SvcTlsBgpVsiImportPolicy2_Type()
)
svcTlsBgpVsiImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiImportPolicy2.setStatus("current")


class _SvcTlsBgpVsiImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpVsiImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpVsiImportPolicy3_Object = MibTableColumn
svcTlsBgpVsiImportPolicy3 = _SvcTlsBgpVsiImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 12),
    _SvcTlsBgpVsiImportPolicy3_Type()
)
svcTlsBgpVsiImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiImportPolicy3.setStatus("current")


class _SvcTlsBgpVsiImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpVsiImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpVsiImportPolicy4_Object = MibTableColumn
svcTlsBgpVsiImportPolicy4 = _SvcTlsBgpVsiImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 13),
    _SvcTlsBgpVsiImportPolicy4_Type()
)
svcTlsBgpVsiImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiImportPolicy4.setStatus("current")


class _SvcTlsBgpVsiImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type svcTlsBgpVsiImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SvcTlsBgpVsiImportPolicy5_Object = MibTableColumn
svcTlsBgpVsiImportPolicy5 = _SvcTlsBgpVsiImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 14),
    _SvcTlsBgpVsiImportPolicy5_Type()
)
svcTlsBgpVsiImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpVsiImportPolicy5.setStatus("current")
_SvcTlsBgpRowStatus_Type = RowStatus
_SvcTlsBgpRowStatus_Object = MibTableColumn
svcTlsBgpRowStatus = _SvcTlsBgpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 81, 1, 15),
    _SvcTlsBgpRowStatus_Type()
)
svcTlsBgpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpRowStatus.setStatus("current")
_SvcTlsPbbIgmpSnpgMRtrTable_Object = MibTable
svcTlsPbbIgmpSnpgMRtrTable = _SvcTlsPbbIgmpSnpgMRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 82)
)
if mibBuilder.loadTexts:
    svcTlsPbbIgmpSnpgMRtrTable.setStatus("current")
_SvcTlsPbbIgmpSnpgMRtrEntry_Object = MibTableRow
svcTlsPbbIgmpSnpgMRtrEntry = _SvcTlsPbbIgmpSnpgMRtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 82, 1)
)
svcTlsPbbIgmpSnpgMRtrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcTlsPbbIgmpSnpgMRtrSvcIdIVpls"),
    (0, "TIMETRA-SERV-MIB", "svcTlsPbbIgmpSnpgMRtrSvcIdBVpls"),
    (1, "TIMETRA-SERV-MIB", "svcTlsPbbIgmpSnpgMRtrMacName"),
)
if mibBuilder.loadTexts:
    svcTlsPbbIgmpSnpgMRtrEntry.setStatus("current")
_SvcTlsPbbIgmpSnpgMRtrSvcIdIVpls_Type = TmnxServId
_SvcTlsPbbIgmpSnpgMRtrSvcIdIVpls_Object = MibTableColumn
svcTlsPbbIgmpSnpgMRtrSvcIdIVpls = _SvcTlsPbbIgmpSnpgMRtrSvcIdIVpls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 82, 1, 1),
    _SvcTlsPbbIgmpSnpgMRtrSvcIdIVpls_Type()
)
svcTlsPbbIgmpSnpgMRtrSvcIdIVpls.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcTlsPbbIgmpSnpgMRtrSvcIdIVpls.setStatus("current")
_SvcTlsPbbIgmpSnpgMRtrSvcIdBVpls_Type = TmnxServId
_SvcTlsPbbIgmpSnpgMRtrSvcIdBVpls_Object = MibTableColumn
svcTlsPbbIgmpSnpgMRtrSvcIdBVpls = _SvcTlsPbbIgmpSnpgMRtrSvcIdBVpls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 82, 1, 2),
    _SvcTlsPbbIgmpSnpgMRtrSvcIdBVpls_Type()
)
svcTlsPbbIgmpSnpgMRtrSvcIdBVpls.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcTlsPbbIgmpSnpgMRtrSvcIdBVpls.setStatus("current")
_SvcTlsPbbIgmpSnpgMRtrMacName_Type = TNamedItem
_SvcTlsPbbIgmpSnpgMRtrMacName_Object = MibTableColumn
svcTlsPbbIgmpSnpgMRtrMacName = _SvcTlsPbbIgmpSnpgMRtrMacName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 82, 1, 3),
    _SvcTlsPbbIgmpSnpgMRtrMacName_Type()
)
svcTlsPbbIgmpSnpgMRtrMacName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcTlsPbbIgmpSnpgMRtrMacName.setStatus("current")
_SvcTlsPbbIgmpSnpgMRtrRowStatus_Type = RowStatus
_SvcTlsPbbIgmpSnpgMRtrRowStatus_Object = MibTableColumn
svcTlsPbbIgmpSnpgMRtrRowStatus = _SvcTlsPbbIgmpSnpgMRtrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 82, 1, 4),
    _SvcTlsPbbIgmpSnpgMRtrRowStatus_Type()
)
svcTlsPbbIgmpSnpgMRtrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsPbbIgmpSnpgMRtrRowStatus.setStatus("current")
_SvcTlsPbbIgmpSnpgMRtrLastCh_Type = TimeStamp
_SvcTlsPbbIgmpSnpgMRtrLastCh_Object = MibTableColumn
svcTlsPbbIgmpSnpgMRtrLastCh = _SvcTlsPbbIgmpSnpgMRtrLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 82, 1, 5),
    _SvcTlsPbbIgmpSnpgMRtrLastCh_Type()
)
svcTlsPbbIgmpSnpgMRtrLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsPbbIgmpSnpgMRtrLastCh.setStatus("current")
_SvcL2MhRteTable_Object = MibTable
svcL2MhRteTable = _SvcL2MhRteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 83)
)
if mibBuilder.loadTexts:
    svcL2MhRteTable.setStatus("current")
_SvcL2MhRteEntry_Object = MibTableRow
svcL2MhRteEntry = _SvcL2MhRteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 83, 1)
)
svcL2MhRteEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcL2MhRteSiteId"),
    (0, "TIMETRA-SERV-MIB", "svcL2MhRteRouteDistinguisher"),
    (0, "TIMETRA-SERV-MIB", "svcL2MhRteNextHopType"),
    (0, "TIMETRA-SERV-MIB", "svcL2MhRteNextHop"),
)
if mibBuilder.loadTexts:
    svcL2MhRteEntry.setStatus("current")
_SvcL2MhRteSiteId_Type = TmnxSiteId
_SvcL2MhRteSiteId_Object = MibTableColumn
svcL2MhRteSiteId = _SvcL2MhRteSiteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 83, 1, 1),
    _SvcL2MhRteSiteId_Type()
)
svcL2MhRteSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2MhRteSiteId.setStatus("current")
_SvcL2MhRteRouteDistinguisher_Type = TmnxVPNRouteDistinguisher
_SvcL2MhRteRouteDistinguisher_Object = MibTableColumn
svcL2MhRteRouteDistinguisher = _SvcL2MhRteRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 83, 1, 2),
    _SvcL2MhRteRouteDistinguisher_Type()
)
svcL2MhRteRouteDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2MhRteRouteDistinguisher.setStatus("current")
_SvcL2MhRteNextHopType_Type = InetAddressType
_SvcL2MhRteNextHopType_Object = MibTableColumn
svcL2MhRteNextHopType = _SvcL2MhRteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 83, 1, 3),
    _SvcL2MhRteNextHopType_Type()
)
svcL2MhRteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2MhRteNextHopType.setStatus("current")
_SvcL2MhRteNextHop_Type = InetAddress
_SvcL2MhRteNextHop_Object = MibTableColumn
svcL2MhRteNextHop = _SvcL2MhRteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 83, 1, 4),
    _SvcL2MhRteNextHop_Type()
)
svcL2MhRteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2MhRteNextHop.setStatus("current")


class _SvcL2MhRteState_Type(Integer32):
    """Custom type svcL2MhRteState based on Integer32"""
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


_SvcL2MhRteState_Type.__name__ = "Integer32"
_SvcL2MhRteState_Object = MibTableColumn
svcL2MhRteState = _SvcL2MhRteState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 83, 1, 5),
    _SvcL2MhRteState_Type()
)
svcL2MhRteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2MhRteState.setStatus("current")
_SvcL2MhRteDf_Type = TruthValue
_SvcL2MhRteDf_Object = MibTableColumn
svcL2MhRteDf = _SvcL2MhRteDf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 83, 1, 6),
    _SvcL2MhRteDf_Type()
)
svcL2MhRteDf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2MhRteDf.setStatus("current")
_SvcTmplTblLastChanged_Type = TimeStamp
_SvcTmplTblLastChanged_Object = MibScalar
svcTmplTblLastChanged = _SvcTmplTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 85),
    _SvcTmplTblLastChanged_Type()
)
svcTmplTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTmplTblLastChanged.setStatus("current")
_SvcTmplTable_Object = MibTable
svcTmplTable = _SvcTmplTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 86)
)
if mibBuilder.loadTexts:
    svcTmplTable.setStatus("current")
_SvcTmplEntry_Object = MibTableRow
svcTmplEntry = _SvcTmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 86, 1)
)
svcTmplEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcTmplName"),
)
if mibBuilder.loadTexts:
    svcTmplEntry.setStatus("current")
_SvcTmplName_Type = TNamedItem
_SvcTmplName_Object = MibTableColumn
svcTmplName = _SvcTmplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 86, 1, 1),
    _SvcTmplName_Type()
)
svcTmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcTmplName.setStatus("current")
_SvcTmplRowStatus_Type = RowStatus
_SvcTmplRowStatus_Object = MibTableColumn
svcTmplRowStatus = _SvcTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 86, 1, 2),
    _SvcTmplRowStatus_Type()
)
svcTmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTmplRowStatus.setStatus("current")
_SvcTmplLastChanged_Type = TimeStamp
_SvcTmplLastChanged_Object = MibTableColumn
svcTmplLastChanged = _SvcTmplLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 86, 1, 3),
    _SvcTmplLastChanged_Type()
)
svcTmplLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTmplLastChanged.setStatus("current")
_SvcTmplSvcCount_Type = Unsigned32
_SvcTmplSvcCount_Object = MibTableColumn
svcTmplSvcCount = _SvcTmplSvcCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 86, 1, 4),
    _SvcTmplSvcCount_Type()
)
svcTmplSvcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTmplSvcCount.setStatus("current")
_SvcTmplType_Type = ServType
_SvcTmplType_Object = MibTableColumn
svcTmplType = _SvcTmplType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 86, 1, 5),
    _SvcTmplType_Type()
)
svcTmplType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTmplType.setStatus("current")


class _SvcTmplMtu_Type(Integer32):
    """Custom type svcTmplMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9194),
    )


_SvcTmplMtu_Type.__name__ = "Integer32"
_SvcTmplMtu_Object = MibTableColumn
svcTmplMtu = _SvcTmplMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 86, 1, 6),
    _SvcTmplMtu_Type()
)
svcTmplMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTmplMtu.setStatus("current")


class _SvcTmplCustId_Type(TmnxCustId):
    """Custom type svcTmplCustId based on TmnxCustId"""
    defaultValue = 0


_SvcTmplCustId_Object = MibTableColumn
svcTmplCustId = _SvcTmplCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 86, 1, 7),
    _SvcTmplCustId_Type()
)
svcTmplCustId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTmplCustId.setStatus("current")
_SvcTlsGroupTblLastChanged_Type = TimeStamp
_SvcTlsGroupTblLastChanged_Object = MibScalar
svcTlsGroupTblLastChanged = _SvcTlsGroupTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 87),
    _SvcTlsGroupTblLastChanged_Type()
)
svcTlsGroupTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsGroupTblLastChanged.setStatus("current")
_SvcTlsGroupTable_Object = MibTable
svcTlsGroupTable = _SvcTlsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88)
)
if mibBuilder.loadTexts:
    svcTlsGroupTable.setStatus("current")
_SvcTlsGroupEntry_Object = MibTableRow
svcTlsGroupEntry = _SvcTlsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1)
)
svcTlsGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcTlsGroupId"),
)
if mibBuilder.loadTexts:
    svcTlsGroupEntry.setStatus("current")
_SvcTlsGroupId_Type = TmnxTlsGroupId
_SvcTlsGroupId_Object = MibTableColumn
svcTlsGroupId = _SvcTlsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 1),
    _SvcTlsGroupId_Type()
)
svcTlsGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcTlsGroupId.setStatus("current")
_SvcTlsGroupRowStatus_Type = RowStatus
_SvcTlsGroupRowStatus_Object = MibTableColumn
svcTlsGroupRowStatus = _SvcTlsGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 2),
    _SvcTlsGroupRowStatus_Type()
)
svcTlsGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsGroupRowStatus.setStatus("current")
_SvcTlsGroupLastChanged_Type = TimeStamp
_SvcTlsGroupLastChanged_Object = MibTableColumn
svcTlsGroupLastChanged = _SvcTlsGroupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 3),
    _SvcTlsGroupLastChanged_Type()
)
svcTlsGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsGroupLastChanged.setStatus("current")


class _SvcTlsGroupAdminStatus_Type(ServiceAdminStatus):
    """Custom type svcTlsGroupAdminStatus based on ServiceAdminStatus"""


_SvcTlsGroupAdminStatus_Object = MibTableColumn
svcTlsGroupAdminStatus = _SvcTlsGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 4),
    _SvcTlsGroupAdminStatus_Type()
)
svcTlsGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsGroupAdminStatus.setStatus("current")


class _SvcTlsGroupStart_Type(TmnxServId):
    """Custom type svcTlsGroupStart based on TmnxServId"""
    defaultValue = 0


_SvcTlsGroupStart_Object = MibTableColumn
svcTlsGroupStart = _SvcTlsGroupStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 5),
    _SvcTlsGroupStart_Type()
)
svcTlsGroupStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsGroupStart.setStatus("current")


class _SvcTlsGroupEnd_Type(TmnxServId):
    """Custom type svcTlsGroupEnd based on TmnxServId"""
    defaultValue = 0


_SvcTlsGroupEnd_Object = MibTableColumn
svcTlsGroupEnd = _SvcTlsGroupEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 6),
    _SvcTlsGroupEnd_Type()
)
svcTlsGroupEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsGroupEnd.setStatus("current")


class _SvcTlsGroupStartVlanTag_Type(QTagOrZero):
    """Custom type svcTlsGroupStartVlanTag based on QTagOrZero"""
    defaultValue = 0


_SvcTlsGroupStartVlanTag_Object = MibTableColumn
svcTlsGroupStartVlanTag = _SvcTlsGroupStartVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 7),
    _SvcTlsGroupStartVlanTag_Type()
)
svcTlsGroupStartVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsGroupStartVlanTag.setStatus("current")


class _SvcTlsGroupSvcTmplName_Type(TNamedItemOrEmpty):
    """Custom type svcTlsGroupSvcTmplName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SvcTlsGroupSvcTmplName_Object = MibTableColumn
svcTlsGroupSvcTmplName = _SvcTlsGroupSvcTmplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 8),
    _SvcTlsGroupSvcTmplName_Type()
)
svcTlsGroupSvcTmplName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsGroupSvcTmplName.setStatus("current")


class _SvcTlsGroupSapTmplName_Type(TNamedItemOrEmpty):
    """Custom type svcTlsGroupSapTmplName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SvcTlsGroupSapTmplName_Object = MibTableColumn
svcTlsGroupSapTmplName = _SvcTlsGroupSapTmplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 9),
    _SvcTlsGroupSapTmplName_Type()
)
svcTlsGroupSapTmplName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsGroupSapTmplName.setStatus("current")


class _SvcTlsGroupMvrpControl_Type(TruthValue):
    """Custom type svcTlsGroupMvrpControl based on TruthValue"""


_SvcTlsGroupMvrpControl_Object = MibTableColumn
svcTlsGroupMvrpControl = _SvcTlsGroupMvrpControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 10),
    _SvcTlsGroupMvrpControl_Type()
)
svcTlsGroupMvrpControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsGroupMvrpControl.setStatus("current")


class _SvcTlsGroupOperStatus_Type(Integer32):
    """Custom type svcTlsGroupOperStatus based on Integer32"""
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
          ("inProgress", 3),
          ("up", 1))
    )


_SvcTlsGroupOperStatus_Type.__name__ = "Integer32"
_SvcTlsGroupOperStatus_Object = MibTableColumn
svcTlsGroupOperStatus = _SvcTlsGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 11),
    _SvcTlsGroupOperStatus_Type()
)
svcTlsGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsGroupOperStatus.setStatus("current")
_SvcTlsGroupLastError_Type = DisplayString
_SvcTlsGroupLastError_Object = MibTableColumn
svcTlsGroupLastError = _SvcTlsGroupLastError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 88, 1, 12),
    _SvcTlsGroupLastError_Type()
)
svcTlsGroupLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsGroupLastError.setStatus("current")
_SvcDhcpLeaseTable_Object = MibTable
svcDhcpLeaseTable = _SvcDhcpLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseTable.setStatus("current")
_SvcDhcpLeaseEntry_Object = MibTableRow
svcDhcpLeaseEntry = _SvcDhcpLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1)
)
svcDhcpLeaseEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseCiAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseCiAddr"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseNextHopMacAddr"),
)
if mibBuilder.loadTexts:
    svcDhcpLeaseEntry.setStatus("current")
_SvcDhcpLeaseCiAddrType_Type = InetAddressType
_SvcDhcpLeaseCiAddrType_Object = MibTableColumn
svcDhcpLeaseCiAddrType = _SvcDhcpLeaseCiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 1),
    _SvcDhcpLeaseCiAddrType_Type()
)
svcDhcpLeaseCiAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLeaseCiAddrType.setStatus("current")


class _SvcDhcpLeaseCiAddr_Type(InetAddress):
    """Custom type svcDhcpLeaseCiAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SvcDhcpLeaseCiAddr_Type.__name__ = "InetAddress"
_SvcDhcpLeaseCiAddr_Object = MibTableColumn
svcDhcpLeaseCiAddr = _SvcDhcpLeaseCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 2),
    _SvcDhcpLeaseCiAddr_Type()
)
svcDhcpLeaseCiAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLeaseCiAddr.setStatus("current")
_SvcDhcpLeaseNextHopMacAddr_Type = MacAddress
_SvcDhcpLeaseNextHopMacAddr_Object = MibTableColumn
svcDhcpLeaseNextHopMacAddr = _SvcDhcpLeaseNextHopMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 3),
    _SvcDhcpLeaseNextHopMacAddr_Type()
)
svcDhcpLeaseNextHopMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLeaseNextHopMacAddr.setStatus("current")
_SvcDhcpLeaseChAddr_Type = MacAddress
_SvcDhcpLeaseChAddr_Object = MibTableColumn
svcDhcpLeaseChAddr = _SvcDhcpLeaseChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 4),
    _SvcDhcpLeaseChAddr_Type()
)
svcDhcpLeaseChAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseChAddr.setStatus("current")


class _SvcDhcpLeaseLocale_Type(Integer32):
    """Custom type svcDhcpLeaseLocale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("sdp", 2))
    )


_SvcDhcpLeaseLocale_Type.__name__ = "Integer32"
_SvcDhcpLeaseLocale_Object = MibTableColumn
svcDhcpLeaseLocale = _SvcDhcpLeaseLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 5),
    _SvcDhcpLeaseLocale_Type()
)
svcDhcpLeaseLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseLocale.setStatus("current")
_SvcDhcpLeasePortId_Type = TmnxPortID
_SvcDhcpLeasePortId_Object = MibTableColumn
svcDhcpLeasePortId = _SvcDhcpLeasePortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 6),
    _SvcDhcpLeasePortId_Type()
)
svcDhcpLeasePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeasePortId.setStatus("current")
_SvcDhcpLeaseEncapValue_Type = TmnxEncapVal
_SvcDhcpLeaseEncapValue_Object = MibTableColumn
svcDhcpLeaseEncapValue = _SvcDhcpLeaseEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 7),
    _SvcDhcpLeaseEncapValue_Type()
)
svcDhcpLeaseEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseEncapValue.setStatus("current")
_SvcDhcpLeaseSdpId_Type = SdpId
_SvcDhcpLeaseSdpId_Object = MibTableColumn
svcDhcpLeaseSdpId = _SvcDhcpLeaseSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 8),
    _SvcDhcpLeaseSdpId_Type()
)
svcDhcpLeaseSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseSdpId.setStatus("current")
_SvcDhcpLeaseVcId_Type = Unsigned32
_SvcDhcpLeaseVcId_Object = MibTableColumn
svcDhcpLeaseVcId = _SvcDhcpLeaseVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 9),
    _SvcDhcpLeaseVcId_Type()
)
svcDhcpLeaseVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseVcId.setStatus("current")
_SvcDhcpLeaseRemainLseTime_Type = Unsigned32
_SvcDhcpLeaseRemainLseTime_Object = MibTableColumn
svcDhcpLeaseRemainLseTime = _SvcDhcpLeaseRemainLseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 10),
    _SvcDhcpLeaseRemainLseTime_Type()
)
svcDhcpLeaseRemainLseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseRemainLseTime.setStatus("current")
if mibBuilder.loadTexts:
    svcDhcpLeaseRemainLseTime.setUnits("seconds")
_SvcDhcpLeaseOption82_Type = OctetString
_SvcDhcpLeaseOption82_Object = MibTableColumn
svcDhcpLeaseOption82 = _SvcDhcpLeaseOption82_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 11),
    _SvcDhcpLeaseOption82_Type()
)
svcDhcpLeaseOption82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseOption82.setStatus("current")
_SvcDhcpLeasePersistKey_Type = Unsigned32
_SvcDhcpLeasePersistKey_Object = MibTableColumn
svcDhcpLeasePersistKey = _SvcDhcpLeasePersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 12),
    _SvcDhcpLeasePersistKey_Type()
)
svcDhcpLeasePersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeasePersistKey.setStatus("current")
_SvcDhcpLeaseSubscrIdent_Type = DisplayString
_SvcDhcpLeaseSubscrIdent_Object = MibTableColumn
svcDhcpLeaseSubscrIdent = _SvcDhcpLeaseSubscrIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 13),
    _SvcDhcpLeaseSubscrIdent_Type()
)
svcDhcpLeaseSubscrIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseSubscrIdent.setStatus("current")
_SvcDhcpLeaseSubProfString_Type = DisplayString
_SvcDhcpLeaseSubProfString_Object = MibTableColumn
svcDhcpLeaseSubProfString = _SvcDhcpLeaseSubProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 14),
    _SvcDhcpLeaseSubProfString_Type()
)
svcDhcpLeaseSubProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseSubProfString.setStatus("current")
_SvcDhcpLeaseSlaProfString_Type = DisplayString
_SvcDhcpLeaseSlaProfString_Object = MibTableColumn
svcDhcpLeaseSlaProfString = _SvcDhcpLeaseSlaProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 15),
    _SvcDhcpLeaseSlaProfString_Type()
)
svcDhcpLeaseSlaProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseSlaProfString.setStatus("current")
_SvcDhcpLeaseShcvOperState_Type = ServShcvOperState
_SvcDhcpLeaseShcvOperState_Object = MibTableColumn
svcDhcpLeaseShcvOperState = _SvcDhcpLeaseShcvOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 16),
    _SvcDhcpLeaseShcvOperState_Type()
)
svcDhcpLeaseShcvOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseShcvOperState.setStatus("current")
_SvcDhcpLeaseShcvChecks_Type = Unsigned32
_SvcDhcpLeaseShcvChecks_Object = MibTableColumn
svcDhcpLeaseShcvChecks = _SvcDhcpLeaseShcvChecks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 17),
    _SvcDhcpLeaseShcvChecks_Type()
)
svcDhcpLeaseShcvChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseShcvChecks.setStatus("current")
_SvcDhcpLeaseShcvReplies_Type = Unsigned32
_SvcDhcpLeaseShcvReplies_Object = MibTableColumn
svcDhcpLeaseShcvReplies = _SvcDhcpLeaseShcvReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 18),
    _SvcDhcpLeaseShcvReplies_Type()
)
svcDhcpLeaseShcvReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseShcvReplies.setStatus("current")
_SvcDhcpLeaseShcvReplyTime_Type = TimeStamp
_SvcDhcpLeaseShcvReplyTime_Object = MibTableColumn
svcDhcpLeaseShcvReplyTime = _SvcDhcpLeaseShcvReplyTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 19),
    _SvcDhcpLeaseShcvReplyTime_Type()
)
svcDhcpLeaseShcvReplyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseShcvReplyTime.setStatus("current")


class _SvcDhcpLeaseClientId_Type(OctetString):
    """Custom type svcDhcpLeaseClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvcDhcpLeaseClientId_Type.__name__ = "OctetString"
_SvcDhcpLeaseClientId_Object = MibTableColumn
svcDhcpLeaseClientId = _SvcDhcpLeaseClientId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 20),
    _SvcDhcpLeaseClientId_Type()
)
svcDhcpLeaseClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseClientId.setStatus("current")
_SvcDhcpLeaseIAID_Type = Unsigned32
_SvcDhcpLeaseIAID_Object = MibTableColumn
svcDhcpLeaseIAID = _SvcDhcpLeaseIAID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 21),
    _SvcDhcpLeaseIAID_Type()
)
svcDhcpLeaseIAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseIAID.setStatus("current")
_SvcDhcpLeaseIAIDType_Type = IAIDType
_SvcDhcpLeaseIAIDType_Object = MibTableColumn
svcDhcpLeaseIAIDType = _SvcDhcpLeaseIAIDType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 22),
    _SvcDhcpLeaseIAIDType_Type()
)
svcDhcpLeaseIAIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseIAIDType.setStatus("current")


class _SvcDhcpLeaseCiAddrMaskLen_Type(Unsigned32):
    """Custom type svcDhcpLeaseCiAddrMaskLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SvcDhcpLeaseCiAddrMaskLen_Type.__name__ = "Unsigned32"
_SvcDhcpLeaseCiAddrMaskLen_Object = MibTableColumn
svcDhcpLeaseCiAddrMaskLen = _SvcDhcpLeaseCiAddrMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 23),
    _SvcDhcpLeaseCiAddrMaskLen_Type()
)
svcDhcpLeaseCiAddrMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseCiAddrMaskLen.setStatus("current")
_SvcDhcpLeaseRetailerSvcId_Type = TmnxServId
_SvcDhcpLeaseRetailerSvcId_Object = MibTableColumn
svcDhcpLeaseRetailerSvcId = _SvcDhcpLeaseRetailerSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 24),
    _SvcDhcpLeaseRetailerSvcId_Type()
)
svcDhcpLeaseRetailerSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseRetailerSvcId.setStatus("current")
_SvcDhcpLeaseRetailerIf_Type = InterfaceIndexOrZero
_SvcDhcpLeaseRetailerIf_Object = MibTableColumn
svcDhcpLeaseRetailerIf = _SvcDhcpLeaseRetailerIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 25),
    _SvcDhcpLeaseRetailerIf_Type()
)
svcDhcpLeaseRetailerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseRetailerIf.setStatus("current")
_SvcDhcpLeaseAncpString_Type = TmnxAncpStringOrZero
_SvcDhcpLeaseAncpString_Object = MibTableColumn
svcDhcpLeaseAncpString = _SvcDhcpLeaseAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 26),
    _SvcDhcpLeaseAncpString_Type()
)
svcDhcpLeaseAncpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseAncpString.setStatus("current")
_SvcDhcpLeaseFramedIpNetMaskTp_Type = InetAddressType
_SvcDhcpLeaseFramedIpNetMaskTp_Object = MibTableColumn
svcDhcpLeaseFramedIpNetMaskTp = _SvcDhcpLeaseFramedIpNetMaskTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 27),
    _SvcDhcpLeaseFramedIpNetMaskTp_Type()
)
svcDhcpLeaseFramedIpNetMaskTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseFramedIpNetMaskTp.setStatus("current")
_SvcDhcpLeaseFramedIpNetMask_Type = InetAddress
_SvcDhcpLeaseFramedIpNetMask_Object = MibTableColumn
svcDhcpLeaseFramedIpNetMask = _SvcDhcpLeaseFramedIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 28),
    _SvcDhcpLeaseFramedIpNetMask_Type()
)
svcDhcpLeaseFramedIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseFramedIpNetMask.setStatus("current")
_SvcDhcpLeaseBCastIpAddrType_Type = InetAddressType
_SvcDhcpLeaseBCastIpAddrType_Object = MibTableColumn
svcDhcpLeaseBCastIpAddrType = _SvcDhcpLeaseBCastIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 29),
    _SvcDhcpLeaseBCastIpAddrType_Type()
)
svcDhcpLeaseBCastIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseBCastIpAddrType.setStatus("current")
_SvcDhcpLeaseBCastIpAddr_Type = InetAddress
_SvcDhcpLeaseBCastIpAddr_Object = MibTableColumn
svcDhcpLeaseBCastIpAddr = _SvcDhcpLeaseBCastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 30),
    _SvcDhcpLeaseBCastIpAddr_Type()
)
svcDhcpLeaseBCastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseBCastIpAddr.setStatus("current")
_SvcDhcpLeaseDefaultRouterTp_Type = InetAddressType
_SvcDhcpLeaseDefaultRouterTp_Object = MibTableColumn
svcDhcpLeaseDefaultRouterTp = _SvcDhcpLeaseDefaultRouterTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 31),
    _SvcDhcpLeaseDefaultRouterTp_Type()
)
svcDhcpLeaseDefaultRouterTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseDefaultRouterTp.setStatus("current")
_SvcDhcpLeaseDefaultRouter_Type = InetAddress
_SvcDhcpLeaseDefaultRouter_Object = MibTableColumn
svcDhcpLeaseDefaultRouter = _SvcDhcpLeaseDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 32),
    _SvcDhcpLeaseDefaultRouter_Type()
)
svcDhcpLeaseDefaultRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseDefaultRouter.setStatus("current")
_SvcDhcpLeasePrimaryDnsType_Type = InetAddressType
_SvcDhcpLeasePrimaryDnsType_Object = MibTableColumn
svcDhcpLeasePrimaryDnsType = _SvcDhcpLeasePrimaryDnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 33),
    _SvcDhcpLeasePrimaryDnsType_Type()
)
svcDhcpLeasePrimaryDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeasePrimaryDnsType.setStatus("current")
_SvcDhcpLeasePrimaryDns_Type = InetAddress
_SvcDhcpLeasePrimaryDns_Object = MibTableColumn
svcDhcpLeasePrimaryDns = _SvcDhcpLeasePrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 34),
    _SvcDhcpLeasePrimaryDns_Type()
)
svcDhcpLeasePrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeasePrimaryDns.setStatus("current")
_SvcDhcpLeaseSecondaryDnsType_Type = InetAddressType
_SvcDhcpLeaseSecondaryDnsType_Object = MibTableColumn
svcDhcpLeaseSecondaryDnsType = _SvcDhcpLeaseSecondaryDnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 35),
    _SvcDhcpLeaseSecondaryDnsType_Type()
)
svcDhcpLeaseSecondaryDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseSecondaryDnsType.setStatus("current")
_SvcDhcpLeaseSecondaryDns_Type = InetAddress
_SvcDhcpLeaseSecondaryDns_Object = MibTableColumn
svcDhcpLeaseSecondaryDns = _SvcDhcpLeaseSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 36),
    _SvcDhcpLeaseSecondaryDns_Type()
)
svcDhcpLeaseSecondaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseSecondaryDns.setStatus("current")


class _SvcDhcpLeaseSessionTimeout_Type(Unsigned32):
    """Custom type svcDhcpLeaseSessionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SvcDhcpLeaseSessionTimeout_Type.__name__ = "Unsigned32"
_SvcDhcpLeaseSessionTimeout_Object = MibTableColumn
svcDhcpLeaseSessionTimeout = _SvcDhcpLeaseSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 37),
    _SvcDhcpLeaseSessionTimeout_Type()
)
svcDhcpLeaseSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    svcDhcpLeaseSessionTimeout.setUnits("seconds")
_SvcDhcpLeaseServerLeaseStart_Type = DateAndTime
_SvcDhcpLeaseServerLeaseStart_Object = MibTableColumn
svcDhcpLeaseServerLeaseStart = _SvcDhcpLeaseServerLeaseStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 38),
    _SvcDhcpLeaseServerLeaseStart_Type()
)
svcDhcpLeaseServerLeaseStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseServerLeaseStart.setStatus("current")
_SvcDhcpLeaseServerLastRenew_Type = DateAndTime
_SvcDhcpLeaseServerLastRenew_Object = MibTableColumn
svcDhcpLeaseServerLastRenew = _SvcDhcpLeaseServerLastRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 39),
    _SvcDhcpLeaseServerLastRenew_Type()
)
svcDhcpLeaseServerLastRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseServerLastRenew.setStatus("current")
_SvcDhcpLeaseServerLeaseEnd_Type = DateAndTime
_SvcDhcpLeaseServerLeaseEnd_Object = MibTableColumn
svcDhcpLeaseServerLeaseEnd = _SvcDhcpLeaseServerLeaseEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 40),
    _SvcDhcpLeaseServerLeaseEnd_Type()
)
svcDhcpLeaseServerLeaseEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseServerLeaseEnd.setStatus("current")
_SvcDhcpLeaseDhcpServerAddrType_Type = InetAddressType
_SvcDhcpLeaseDhcpServerAddrType_Object = MibTableColumn
svcDhcpLeaseDhcpServerAddrType = _SvcDhcpLeaseDhcpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 41),
    _SvcDhcpLeaseDhcpServerAddrType_Type()
)
svcDhcpLeaseDhcpServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseDhcpServerAddrType.setStatus("current")
_SvcDhcpLeaseDhcpServerAddr_Type = InetAddress
_SvcDhcpLeaseDhcpServerAddr_Object = MibTableColumn
svcDhcpLeaseDhcpServerAddr = _SvcDhcpLeaseDhcpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 42),
    _SvcDhcpLeaseDhcpServerAddr_Type()
)
svcDhcpLeaseDhcpServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseDhcpServerAddr.setStatus("current")
_SvcDhcpLeaseOriginSubscrId_Type = DhcpLseStateInfoOrigin
_SvcDhcpLeaseOriginSubscrId_Object = MibTableColumn
svcDhcpLeaseOriginSubscrId = _SvcDhcpLeaseOriginSubscrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 43),
    _SvcDhcpLeaseOriginSubscrId_Type()
)
svcDhcpLeaseOriginSubscrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseOriginSubscrId.setStatus("current")
_SvcDhcpLeaseOriginStrings_Type = DhcpLseStateInfoOrigin
_SvcDhcpLeaseOriginStrings_Object = MibTableColumn
svcDhcpLeaseOriginStrings = _SvcDhcpLeaseOriginStrings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 44),
    _SvcDhcpLeaseOriginStrings_Type()
)
svcDhcpLeaseOriginStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseOriginStrings.setStatus("current")
_SvcDhcpLeaseOriginLeaseInfo_Type = DhcpLseStateInfoOrigin
_SvcDhcpLeaseOriginLeaseInfo_Object = MibTableColumn
svcDhcpLeaseOriginLeaseInfo = _SvcDhcpLeaseOriginLeaseInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 45),
    _SvcDhcpLeaseOriginLeaseInfo_Type()
)
svcDhcpLeaseOriginLeaseInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseOriginLeaseInfo.setStatus("current")
_SvcDhcpLeaseDhcpClientAddrType_Type = InetAddressType
_SvcDhcpLeaseDhcpClientAddrType_Object = MibTableColumn
svcDhcpLeaseDhcpClientAddrType = _SvcDhcpLeaseDhcpClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 46),
    _SvcDhcpLeaseDhcpClientAddrType_Type()
)
svcDhcpLeaseDhcpClientAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseDhcpClientAddrType.setStatus("current")
_SvcDhcpLeaseDhcpClientAddr_Type = InetAddress
_SvcDhcpLeaseDhcpClientAddr_Object = MibTableColumn
svcDhcpLeaseDhcpClientAddr = _SvcDhcpLeaseDhcpClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 47),
    _SvcDhcpLeaseDhcpClientAddr_Type()
)
svcDhcpLeaseDhcpClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseDhcpClientAddr.setStatus("current")
_SvcDhcpLeaseLeaseSplitActive_Type = TruthValue
_SvcDhcpLeaseLeaseSplitActive_Object = MibTableColumn
svcDhcpLeaseLeaseSplitActive = _SvcDhcpLeaseLeaseSplitActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 48),
    _SvcDhcpLeaseLeaseSplitActive_Type()
)
svcDhcpLeaseLeaseSplitActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseLeaseSplitActive.setStatus("current")


class _SvcDhcpLeaseInterDestId_Type(DisplayString):
    """Custom type svcDhcpLeaseInterDestId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SvcDhcpLeaseInterDestId_Type.__name__ = "DisplayString"
_SvcDhcpLeaseInterDestId_Object = MibTableColumn
svcDhcpLeaseInterDestId = _SvcDhcpLeaseInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 49),
    _SvcDhcpLeaseInterDestId_Type()
)
svcDhcpLeaseInterDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseInterDestId.setStatus("current")
_SvcDhcpLeasePrimaryNbnsType_Type = InetAddressType
_SvcDhcpLeasePrimaryNbnsType_Object = MibTableColumn
svcDhcpLeasePrimaryNbnsType = _SvcDhcpLeasePrimaryNbnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 50),
    _SvcDhcpLeasePrimaryNbnsType_Type()
)
svcDhcpLeasePrimaryNbnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeasePrimaryNbnsType.setStatus("current")
_SvcDhcpLeasePrimaryNbns_Type = InetAddress
_SvcDhcpLeasePrimaryNbns_Object = MibTableColumn
svcDhcpLeasePrimaryNbns = _SvcDhcpLeasePrimaryNbns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 51),
    _SvcDhcpLeasePrimaryNbns_Type()
)
svcDhcpLeasePrimaryNbns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeasePrimaryNbns.setStatus("current")
_SvcDhcpLeaseSecondaryNbnsType_Type = InetAddressType
_SvcDhcpLeaseSecondaryNbnsType_Object = MibTableColumn
svcDhcpLeaseSecondaryNbnsType = _SvcDhcpLeaseSecondaryNbnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 52),
    _SvcDhcpLeaseSecondaryNbnsType_Type()
)
svcDhcpLeaseSecondaryNbnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseSecondaryNbnsType.setStatus("current")
_SvcDhcpLeaseSecondaryNbns_Type = InetAddress
_SvcDhcpLeaseSecondaryNbns_Object = MibTableColumn
svcDhcpLeaseSecondaryNbns = _SvcDhcpLeaseSecondaryNbns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 53),
    _SvcDhcpLeaseSecondaryNbns_Type()
)
svcDhcpLeaseSecondaryNbns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseSecondaryNbns.setStatus("current")
_SvcDhcpLeaseAppProfString_Type = DisplayString
_SvcDhcpLeaseAppProfString_Object = MibTableColumn
svcDhcpLeaseAppProfString = _SvcDhcpLeaseAppProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 54),
    _SvcDhcpLeaseAppProfString_Type()
)
svcDhcpLeaseAppProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseAppProfString.setStatus("current")
_SvcDhcpLeaseCategoryMapName_Type = TNamedItemOrEmpty
_SvcDhcpLeaseCategoryMapName_Object = MibTableColumn
svcDhcpLeaseCategoryMapName = _SvcDhcpLeaseCategoryMapName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 55),
    _SvcDhcpLeaseCategoryMapName_Type()
)
svcDhcpLeaseCategoryMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseCategoryMapName.setStatus("current")
_SvcDhcpLeaseNakNextRenew_Type = TruthValue
_SvcDhcpLeaseNakNextRenew_Object = MibTableColumn
svcDhcpLeaseNakNextRenew = _SvcDhcpLeaseNakNextRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 56),
    _SvcDhcpLeaseNakNextRenew_Type()
)
svcDhcpLeaseNakNextRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseNakNextRenew.setStatus("current")


class _SvcDhcpLeaseRadiusClassAttr_Type(OctetString):
    """Custom type svcDhcpLeaseRadiusClassAttr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_SvcDhcpLeaseRadiusClassAttr_Type.__name__ = "OctetString"
_SvcDhcpLeaseRadiusClassAttr_Object = MibTableColumn
svcDhcpLeaseRadiusClassAttr = _SvcDhcpLeaseRadiusClassAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 57),
    _SvcDhcpLeaseRadiusClassAttr_Type()
)
svcDhcpLeaseRadiusClassAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseRadiusClassAttr.setStatus("current")


class _SvcDhcpLeaseRadiusUserName_Type(DisplayString):
    """Custom type svcDhcpLeaseRadiusUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SvcDhcpLeaseRadiusUserName_Type.__name__ = "DisplayString"
_SvcDhcpLeaseRadiusUserName_Object = MibTableColumn
svcDhcpLeaseRadiusUserName = _SvcDhcpLeaseRadiusUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 58),
    _SvcDhcpLeaseRadiusUserName_Type()
)
svcDhcpLeaseRadiusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseRadiusUserName.setStatus("current")
_SvcDhcpLeasePoolName_Type = TNamedItem
_SvcDhcpLeasePoolName_Object = MibTableColumn
svcDhcpLeasePoolName = _SvcDhcpLeasePoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 59),
    _SvcDhcpLeasePoolName_Type()
)
svcDhcpLeasePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeasePoolName.setStatus("current")


class _SvcDhcpLeaseServerId_Type(OctetString):
    """Custom type svcDhcpLeaseServerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvcDhcpLeaseServerId_Type.__name__ = "OctetString"
_SvcDhcpLeaseServerId_Object = MibTableColumn
svcDhcpLeaseServerId = _SvcDhcpLeaseServerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 60),
    _SvcDhcpLeaseServerId_Type()
)
svcDhcpLeaseServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseServerId.setStatus("current")


class _SvcDhcpLeaseInterfaceId_Type(OctetString):
    """Custom type svcDhcpLeaseInterfaceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvcDhcpLeaseInterfaceId_Type.__name__ = "OctetString"
_SvcDhcpLeaseInterfaceId_Object = MibTableColumn
svcDhcpLeaseInterfaceId = _SvcDhcpLeaseInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 61),
    _SvcDhcpLeaseInterfaceId_Type()
)
svcDhcpLeaseInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseInterfaceId.setStatus("current")


class _SvcDhcpLeaseRemoteId_Type(OctetString):
    """Custom type svcDhcpLeaseRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvcDhcpLeaseRemoteId_Type.__name__ = "OctetString"
_SvcDhcpLeaseRemoteId_Object = MibTableColumn
svcDhcpLeaseRemoteId = _SvcDhcpLeaseRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 62),
    _SvcDhcpLeaseRemoteId_Type()
)
svcDhcpLeaseRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseRemoteId.setStatus("current")


class _SvcDhcpLeaseOption60_Type(OctetString):
    """Custom type svcDhcpLeaseOption60 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvcDhcpLeaseOption60_Type.__name__ = "OctetString"
_SvcDhcpLeaseOption60_Object = MibTableColumn
svcDhcpLeaseOption60 = _SvcDhcpLeaseOption60_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 63),
    _SvcDhcpLeaseOption60_Type()
)
svcDhcpLeaseOption60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseOption60.setStatus("current")


class _SvcDhcpLeaseRadCalledStationId_Type(OctetString):
    """Custom type svcDhcpLeaseRadCalledStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SvcDhcpLeaseRadCalledStationId_Type.__name__ = "OctetString"
_SvcDhcpLeaseRadCalledStationId_Object = MibTableColumn
svcDhcpLeaseRadCalledStationId = _SvcDhcpLeaseRadCalledStationId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 90, 1, 64),
    _SvcDhcpLeaseRadCalledStationId_Type()
)
svcDhcpLeaseRadCalledStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseRadCalledStationId.setStatus("current")
_SvcDhcpLeaseModifyTable_Object = MibTable
svcDhcpLeaseModifyTable = _SvcDhcpLeaseModifyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 91)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseModifyTable.setStatus("current")
_SvcDhcpLeaseModifyEntry_Object = MibTableRow
svcDhcpLeaseModifyEntry = _SvcDhcpLeaseModifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 91, 1)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseModifyEntry.setStatus("current")


class _SvcDhcpLeaseModifySubIndent_Type(DisplayString):
    """Custom type svcDhcpLeaseModifySubIndent based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SvcDhcpLeaseModifySubIndent_Type.__name__ = "DisplayString"
_SvcDhcpLeaseModifySubIndent_Object = MibTableColumn
svcDhcpLeaseModifySubIndent = _SvcDhcpLeaseModifySubIndent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 91, 1, 1),
    _SvcDhcpLeaseModifySubIndent_Type()
)
svcDhcpLeaseModifySubIndent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLeaseModifySubIndent.setStatus("current")


class _SvcDhcpLeaseModifySubProfile_Type(DisplayString):
    """Custom type svcDhcpLeaseModifySubProfile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SvcDhcpLeaseModifySubProfile_Type.__name__ = "DisplayString"
_SvcDhcpLeaseModifySubProfile_Object = MibTableColumn
svcDhcpLeaseModifySubProfile = _SvcDhcpLeaseModifySubProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 91, 1, 2),
    _SvcDhcpLeaseModifySubProfile_Type()
)
svcDhcpLeaseModifySubProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLeaseModifySubProfile.setStatus("current")


class _SvcDhcpLeaseModifySlaProfile_Type(DisplayString):
    """Custom type svcDhcpLeaseModifySlaProfile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SvcDhcpLeaseModifySlaProfile_Type.__name__ = "DisplayString"
_SvcDhcpLeaseModifySlaProfile_Object = MibTableColumn
svcDhcpLeaseModifySlaProfile = _SvcDhcpLeaseModifySlaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 91, 1, 3),
    _SvcDhcpLeaseModifySlaProfile_Type()
)
svcDhcpLeaseModifySlaProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLeaseModifySlaProfile.setStatus("current")


class _SvcDhcpLeaseEvaluateState_Type(TruthValue):
    """Custom type svcDhcpLeaseEvaluateState based on TruthValue"""


_SvcDhcpLeaseEvaluateState_Object = MibTableColumn
svcDhcpLeaseEvaluateState = _SvcDhcpLeaseEvaluateState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 91, 1, 4),
    _SvcDhcpLeaseEvaluateState_Type()
)
svcDhcpLeaseEvaluateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLeaseEvaluateState.setStatus("current")


class _SvcDhcpLeaseModInterDestId_Type(DisplayString):
    """Custom type svcDhcpLeaseModInterDestId based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SvcDhcpLeaseModInterDestId_Type.__name__ = "DisplayString"
_SvcDhcpLeaseModInterDestId_Object = MibTableColumn
svcDhcpLeaseModInterDestId = _SvcDhcpLeaseModInterDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 91, 1, 5),
    _SvcDhcpLeaseModInterDestId_Type()
)
svcDhcpLeaseModInterDestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLeaseModInterDestId.setStatus("current")


class _SvcDhcpLeaseModifyAncpString_Type(TmnxAncpStringOrZero):
    """Custom type svcDhcpLeaseModifyAncpString based on TmnxAncpStringOrZero"""
    defaultHexValue = ""


_SvcDhcpLeaseModifyAncpString_Object = MibTableColumn
svcDhcpLeaseModifyAncpString = _SvcDhcpLeaseModifyAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 91, 1, 6),
    _SvcDhcpLeaseModifyAncpString_Type()
)
svcDhcpLeaseModifyAncpString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLeaseModifyAncpString.setStatus("current")


class _SvcDhcpLeaseModifyAppProfile_Type(DisplayString):
    """Custom type svcDhcpLeaseModifyAppProfile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SvcDhcpLeaseModifyAppProfile_Type.__name__ = "DisplayString"
_SvcDhcpLeaseModifyAppProfile_Object = MibTableColumn
svcDhcpLeaseModifyAppProfile = _SvcDhcpLeaseModifyAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 91, 1, 7),
    _SvcDhcpLeaseModifyAppProfile_Type()
)
svcDhcpLeaseModifyAppProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLeaseModifyAppProfile.setStatus("current")
_SvcDhcpLeaseActionTable_Object = MibTable
svcDhcpLeaseActionTable = _SvcDhcpLeaseActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 92)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseActionTable.setStatus("current")
_SvcDhcpLeaseActionEntry_Object = MibTableRow
svcDhcpLeaseActionEntry = _SvcDhcpLeaseActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 92, 1)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseActionEntry.setStatus("current")


class _SvcDhcpLeaseForceRenew_Type(TruthValue):
    """Custom type svcDhcpLeaseForceRenew based on TruthValue"""


_SvcDhcpLeaseForceRenew_Object = MibTableColumn
svcDhcpLeaseForceRenew = _SvcDhcpLeaseForceRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 92, 1, 1),
    _SvcDhcpLeaseForceRenew_Type()
)
svcDhcpLeaseForceRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLeaseForceRenew.setStatus("current")
_SvcDhcpLeaseBgpTable_Object = MibTable
svcDhcpLeaseBgpTable = _SvcDhcpLeaseBgpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 93)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseBgpTable.setStatus("current")
_SvcDhcpLeaseBgpEntry_Object = MibTableRow
svcDhcpLeaseBgpEntry = _SvcDhcpLeaseBgpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 93, 1)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseBgpEntry.setStatus("current")
_SvcDhcpLeaseBgpPrngPlcyName_Type = TNamedItemOrEmpty
_SvcDhcpLeaseBgpPrngPlcyName_Object = MibTableColumn
svcDhcpLeaseBgpPrngPlcyName = _SvcDhcpLeaseBgpPrngPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 93, 1, 1),
    _SvcDhcpLeaseBgpPrngPlcyName_Type()
)
svcDhcpLeaseBgpPrngPlcyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseBgpPrngPlcyName.setStatus("current")
_SvcDhcpLeaseBgpAuthKeyChain_Type = TNamedItemOrEmpty
_SvcDhcpLeaseBgpAuthKeyChain_Object = MibTableColumn
svcDhcpLeaseBgpAuthKeyChain = _SvcDhcpLeaseBgpAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 93, 1, 2),
    _SvcDhcpLeaseBgpAuthKeyChain_Type()
)
svcDhcpLeaseBgpAuthKeyChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseBgpAuthKeyChain.setStatus("current")


class _SvcDhcpLeaseBgpMD5AuthKey_Type(OctetString):
    """Custom type svcDhcpLeaseBgpMD5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvcDhcpLeaseBgpMD5AuthKey_Type.__name__ = "OctetString"
_SvcDhcpLeaseBgpMD5AuthKey_Object = MibTableColumn
svcDhcpLeaseBgpMD5AuthKey = _SvcDhcpLeaseBgpMD5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 93, 1, 3),
    _SvcDhcpLeaseBgpMD5AuthKey_Type()
)
svcDhcpLeaseBgpMD5AuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseBgpMD5AuthKey.setStatus("current")
_SvcDhcpLeaseBgpImportPolicy_Type = TPolicyStatementNameOrEmpty
_SvcDhcpLeaseBgpImportPolicy_Object = MibTableColumn
svcDhcpLeaseBgpImportPolicy = _SvcDhcpLeaseBgpImportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 93, 1, 4),
    _SvcDhcpLeaseBgpImportPolicy_Type()
)
svcDhcpLeaseBgpImportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseBgpImportPolicy.setStatus("current")
_SvcDhcpLeaseBgpExportPolicy_Type = TPolicyStatementNameOrEmpty
_SvcDhcpLeaseBgpExportPolicy_Object = MibTableColumn
svcDhcpLeaseBgpExportPolicy = _SvcDhcpLeaseBgpExportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 93, 1, 5),
    _SvcDhcpLeaseBgpExportPolicy_Type()
)
svcDhcpLeaseBgpExportPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseBgpExportPolicy.setStatus("current")
_SvcDhcpLeaseBgpPeerAS_Type = InetAutonomousSystemNumber
_SvcDhcpLeaseBgpPeerAS_Object = MibTableColumn
svcDhcpLeaseBgpPeerAS = _SvcDhcpLeaseBgpPeerAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 93, 1, 6),
    _SvcDhcpLeaseBgpPeerAS_Type()
)
svcDhcpLeaseBgpPeerAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseBgpPeerAS.setStatus("current")
_SvcDhcpLeaseBgpPeeringStatus_Type = BgpPeeringStatus
_SvcDhcpLeaseBgpPeeringStatus_Object = MibTableColumn
svcDhcpLeaseBgpPeeringStatus = _SvcDhcpLeaseBgpPeeringStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 93, 1, 7),
    _SvcDhcpLeaseBgpPeeringStatus_Type()
)
svcDhcpLeaseBgpPeeringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseBgpPeeringStatus.setStatus("current")
_SvcTmplTlsTblLastChanged_Type = TimeStamp
_SvcTmplTlsTblLastChanged_Object = MibScalar
svcTmplTlsTblLastChanged = _SvcTmplTlsTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 94),
    _SvcTmplTlsTblLastChanged_Type()
)
svcTmplTlsTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTmplTlsTblLastChanged.setStatus("current")
_SvcTmplTlsTable_Object = MibTable
svcTmplTlsTable = _SvcTmplTlsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95)
)
if mibBuilder.loadTexts:
    svcTmplTlsTable.setStatus("current")
_SvcTmplTlsEntry_Object = MibTableRow
svcTmplTlsEntry = _SvcTmplTlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1)
)
svcTmplTlsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcTmplName"),
)
if mibBuilder.loadTexts:
    svcTmplTlsEntry.setStatus("current")
_SvcTmplTlsLastChanged_Type = TimeStamp
_SvcTmplTlsLastChanged_Object = MibTableColumn
svcTmplTlsLastChanged = _SvcTmplTlsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 1),
    _SvcTmplTlsLastChanged_Type()
)
svcTmplTlsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTmplTlsLastChanged.setStatus("current")


class _SvcTmplTlsMacLearning_Type(TmnxEnabledDisabled):
    """Custom type svcTmplTlsMacLearning based on TmnxEnabledDisabled"""


_SvcTmplTlsMacLearning_Object = MibTableColumn
svcTmplTlsMacLearning = _SvcTmplTlsMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 2),
    _SvcTmplTlsMacLearning_Type()
)
svcTmplTlsMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsMacLearning.setStatus("current")


class _SvcTmplTlsDiscardUnknownDest_Type(TmnxEnabledDisabled):
    """Custom type svcTmplTlsDiscardUnknownDest based on TmnxEnabledDisabled"""


_SvcTmplTlsDiscardUnknownDest_Object = MibTableColumn
svcTmplTlsDiscardUnknownDest = _SvcTmplTlsDiscardUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 3),
    _SvcTmplTlsDiscardUnknownDest_Type()
)
svcTmplTlsDiscardUnknownDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsDiscardUnknownDest.setStatus("current")


class _SvcTmplTlsFdbTableSize_Type(Integer32):
    """Custom type svcTmplTlsFdbTableSize based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511999),
    )


_SvcTmplTlsFdbTableSize_Type.__name__ = "Integer32"
_SvcTmplTlsFdbTableSize_Object = MibTableColumn
svcTmplTlsFdbTableSize = _SvcTmplTlsFdbTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 4),
    _SvcTmplTlsFdbTableSize_Type()
)
svcTmplTlsFdbTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsFdbTableSize.setStatus("current")


class _SvcTmplTlsFdbLocalAgeTime_Type(Integer32):
    """Custom type svcTmplTlsFdbLocalAgeTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_SvcTmplTlsFdbLocalAgeTime_Type.__name__ = "Integer32"
_SvcTmplTlsFdbLocalAgeTime_Object = MibTableColumn
svcTmplTlsFdbLocalAgeTime = _SvcTmplTlsFdbLocalAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 5),
    _SvcTmplTlsFdbLocalAgeTime_Type()
)
svcTmplTlsFdbLocalAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsFdbLocalAgeTime.setStatus("current")
if mibBuilder.loadTexts:
    svcTmplTlsFdbLocalAgeTime.setUnits("seconds")


class _SvcTmplTlsFdbRemoteAgeTime_Type(Integer32):
    """Custom type svcTmplTlsFdbRemoteAgeTime based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_SvcTmplTlsFdbRemoteAgeTime_Type.__name__ = "Integer32"
_SvcTmplTlsFdbRemoteAgeTime_Object = MibTableColumn
svcTmplTlsFdbRemoteAgeTime = _SvcTmplTlsFdbRemoteAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 6),
    _SvcTmplTlsFdbRemoteAgeTime_Type()
)
svcTmplTlsFdbRemoteAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsFdbRemoteAgeTime.setStatus("current")
if mibBuilder.loadTexts:
    svcTmplTlsFdbRemoteAgeTime.setUnits("seconds")


class _SvcTmplTlsStpAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type svcTmplTlsStpAdminStatus based on TmnxEnabledDisabled"""


_SvcTmplTlsStpAdminStatus_Object = MibTableColumn
svcTmplTlsStpAdminStatus = _SvcTmplTlsStpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 7),
    _SvcTmplTlsStpAdminStatus_Type()
)
svcTmplTlsStpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsStpAdminStatus.setStatus("current")


class _SvcTmplTlsStpPriority_Type(Integer32):
    """Custom type svcTmplTlsStpPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SvcTmplTlsStpPriority_Type.__name__ = "Integer32"
_SvcTmplTlsStpPriority_Object = MibTableColumn
svcTmplTlsStpPriority = _SvcTmplTlsStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 8),
    _SvcTmplTlsStpPriority_Type()
)
svcTmplTlsStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsStpPriority.setStatus("current")


class _SvcTmplTlsStpBridgeMaxAge_Type(Integer32):
    """Custom type svcTmplTlsStpBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_SvcTmplTlsStpBridgeMaxAge_Type.__name__ = "Integer32"
_SvcTmplTlsStpBridgeMaxAge_Object = MibTableColumn
svcTmplTlsStpBridgeMaxAge = _SvcTmplTlsStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 9),
    _SvcTmplTlsStpBridgeMaxAge_Type()
)
svcTmplTlsStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsStpBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    svcTmplTlsStpBridgeMaxAge.setUnits("seconds")


class _SvcTmplTlsStpBridgeHelloTime_Type(Integer32):
    """Custom type svcTmplTlsStpBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvcTmplTlsStpBridgeHelloTime_Type.__name__ = "Integer32"
_SvcTmplTlsStpBridgeHelloTime_Object = MibTableColumn
svcTmplTlsStpBridgeHelloTime = _SvcTmplTlsStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 10),
    _SvcTmplTlsStpBridgeHelloTime_Type()
)
svcTmplTlsStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsStpBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    svcTmplTlsStpBridgeHelloTime.setUnits("seconds")


class _SvcTmplTlsStpBridgeForwardDelay_Type(Integer32):
    """Custom type svcTmplTlsStpBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_SvcTmplTlsStpBridgeForwardDelay_Type.__name__ = "Integer32"
_SvcTmplTlsStpBridgeForwardDelay_Object = MibTableColumn
svcTmplTlsStpBridgeForwardDelay = _SvcTmplTlsStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 11),
    _SvcTmplTlsStpBridgeForwardDelay_Type()
)
svcTmplTlsStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsStpBridgeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    svcTmplTlsStpBridgeForwardDelay.setUnits("seconds")


class _SvcTmplTlsMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type svcTmplTlsMacAgeing based on TmnxEnabledDisabled"""


_SvcTmplTlsMacAgeing_Object = MibTableColumn
svcTmplTlsMacAgeing = _SvcTmplTlsMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 12),
    _SvcTmplTlsMacAgeing_Type()
)
svcTmplTlsMacAgeing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsMacAgeing.setStatus("current")


class _SvcTmplTlsFdbTableFullHighWMark_Type(Integer32):
    """Custom type svcTmplTlsFdbTableFullHighWMark based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTmplTlsFdbTableFullHighWMark_Type.__name__ = "Integer32"
_SvcTmplTlsFdbTableFullHighWMark_Object = MibTableColumn
svcTmplTlsFdbTableFullHighWMark = _SvcTmplTlsFdbTableFullHighWMark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 13),
    _SvcTmplTlsFdbTableFullHighWMark_Type()
)
svcTmplTlsFdbTableFullHighWMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsFdbTableFullHighWMark.setStatus("current")


class _SvcTmplTlsFdbTableFullLowWMark_Type(Integer32):
    """Custom type svcTmplTlsFdbTableFullLowWMark based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTmplTlsFdbTableFullLowWMark_Type.__name__ = "Integer32"
_SvcTmplTlsFdbTableFullLowWMark_Object = MibTableColumn
svcTmplTlsFdbTableFullLowWMark = _SvcTmplTlsFdbTableFullLowWMark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 14),
    _SvcTmplTlsFdbTableFullLowWMark_Type()
)
svcTmplTlsFdbTableFullLowWMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsFdbTableFullLowWMark.setStatus("current")


class _SvcTmplTlsStpVersion_Type(Integer32):
    """Custom type svcTmplTlsStpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("compDot1w", 3),
          ("dot1w", 4),
          ("mstp", 5),
          ("pmstp", 6),
          ("rstp", 2))
    )


_SvcTmplTlsStpVersion_Type.__name__ = "Integer32"
_SvcTmplTlsStpVersion_Object = MibTableColumn
svcTmplTlsStpVersion = _SvcTmplTlsStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 15),
    _SvcTmplTlsStpVersion_Type()
)
svcTmplTlsStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsStpVersion.setStatus("current")


class _SvcTmplTlsStpHoldCount_Type(Integer32):
    """Custom type svcTmplTlsStpHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SvcTmplTlsStpHoldCount_Type.__name__ = "Integer32"
_SvcTmplTlsStpHoldCount_Object = MibTableColumn
svcTmplTlsStpHoldCount = _SvcTmplTlsStpHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 16),
    _SvcTmplTlsStpHoldCount_Type()
)
svcTmplTlsStpHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsStpHoldCount.setStatus("current")


class _SvcTmplTlsPerSvcHashing_Type(TmnxEnabledDisabled):
    """Custom type svcTmplTlsPerSvcHashing based on TmnxEnabledDisabled"""


_SvcTmplTlsPerSvcHashing_Object = MibTableColumn
svcTmplTlsPerSvcHashing = _SvcTmplTlsPerSvcHashing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 17),
    _SvcTmplTlsPerSvcHashing_Type()
)
svcTmplTlsPerSvcHashing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsPerSvcHashing.setStatus("current")


class _SvcTmplTlsTempFloodTime_Type(Integer32):
    """Custom type svcTmplTlsTempFloodTime based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(3, 600),
    )


_SvcTmplTlsTempFloodTime_Type.__name__ = "Integer32"
_SvcTmplTlsTempFloodTime_Object = MibTableColumn
svcTmplTlsTempFloodTime = _SvcTmplTlsTempFloodTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 18),
    _SvcTmplTlsTempFloodTime_Type()
)
svcTmplTlsTempFloodTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsTempFloodTime.setStatus("current")
if mibBuilder.loadTexts:
    svcTmplTlsTempFloodTime.setUnits("seconds")


class _SvcTmplTlsMacMoveMaxRate_Type(Unsigned32):
    """Custom type svcTmplTlsMacMoveMaxRate based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SvcTmplTlsMacMoveMaxRate_Type.__name__ = "Unsigned32"
_SvcTmplTlsMacMoveMaxRate_Object = MibTableColumn
svcTmplTlsMacMoveMaxRate = _SvcTmplTlsMacMoveMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 19),
    _SvcTmplTlsMacMoveMaxRate_Type()
)
svcTmplTlsMacMoveMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsMacMoveMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    svcTmplTlsMacMoveMaxRate.setUnits("per-second")


class _SvcTmplTlsMacMoveRetryTimeout_Type(Unsigned32):
    """Custom type svcTmplTlsMacMoveRetryTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SvcTmplTlsMacMoveRetryTimeout_Type.__name__ = "Unsigned32"
_SvcTmplTlsMacMoveRetryTimeout_Object = MibTableColumn
svcTmplTlsMacMoveRetryTimeout = _SvcTmplTlsMacMoveRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 20),
    _SvcTmplTlsMacMoveRetryTimeout_Type()
)
svcTmplTlsMacMoveRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsMacMoveRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    svcTmplTlsMacMoveRetryTimeout.setUnits("seconds")


class _SvcTmplTlsMacMoveAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type svcTmplTlsMacMoveAdminStatus based on TmnxEnabledDisabled"""


_SvcTmplTlsMacMoveAdminStatus_Object = MibTableColumn
svcTmplTlsMacMoveAdminStatus = _SvcTmplTlsMacMoveAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 21),
    _SvcTmplTlsMacMoveAdminStatus_Type()
)
svcTmplTlsMacMoveAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsMacMoveAdminStatus.setStatus("current")


class _SvcTmplTlsPriPortsCumFactor_Type(Unsigned32):
    """Custom type svcTmplTlsPriPortsCumFactor based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_SvcTmplTlsPriPortsCumFactor_Type.__name__ = "Unsigned32"
_SvcTmplTlsPriPortsCumFactor_Object = MibTableColumn
svcTmplTlsPriPortsCumFactor = _SvcTmplTlsPriPortsCumFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 22),
    _SvcTmplTlsPriPortsCumFactor_Type()
)
svcTmplTlsPriPortsCumFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsPriPortsCumFactor.setStatus("current")


class _SvcTmplTlsSecPortsCumFactor_Type(Unsigned32):
    """Custom type svcTmplTlsSecPortsCumFactor based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 9),
    )


_SvcTmplTlsSecPortsCumFactor_Type.__name__ = "Unsigned32"
_SvcTmplTlsSecPortsCumFactor_Object = MibTableColumn
svcTmplTlsSecPortsCumFactor = _SvcTmplTlsSecPortsCumFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 23),
    _SvcTmplTlsSecPortsCumFactor_Type()
)
svcTmplTlsSecPortsCumFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsSecPortsCumFactor.setStatus("current")


class _SvcTmplTlsMacMoveNumRetries_Type(Unsigned32):
    """Custom type svcTmplTlsMacMoveNumRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SvcTmplTlsMacMoveNumRetries_Type.__name__ = "Unsigned32"
_SvcTmplTlsMacMoveNumRetries_Object = MibTableColumn
svcTmplTlsMacMoveNumRetries = _SvcTmplTlsMacMoveNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 95, 1, 24),
    _SvcTmplTlsMacMoveNumRetries_Type()
)
svcTmplTlsMacMoveNumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTmplTlsMacMoveNumRetries.setStatus("current")
_SvcTmplUserTable_Object = MibTable
svcTmplUserTable = _SvcTmplUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 96)
)
if mibBuilder.loadTexts:
    svcTmplUserTable.setStatus("current")
_SvcTmplUserEntry_Object = MibTableRow
svcTmplUserEntry = _SvcTmplUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 96, 1)
)
svcTmplUserEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcTmplName"),
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcTmplUserEntry.setStatus("current")


class _SvcTmplUserCreationOrigin_Type(Integer32):
    """Custom type svcTmplUserCreationOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mVpls", 1)
    )


_SvcTmplUserCreationOrigin_Type.__name__ = "Integer32"
_SvcTmplUserCreationOrigin_Object = MibTableColumn
svcTmplUserCreationOrigin = _SvcTmplUserCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 96, 1, 1),
    _SvcTmplUserCreationOrigin_Type()
)
svcTmplUserCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTmplUserCreationOrigin.setStatus("current")
_SvcTmplUserCreatorSvcId_Type = TmnxServId
_SvcTmplUserCreatorSvcId_Object = MibTableColumn
svcTmplUserCreatorSvcId = _SvcTmplUserCreatorSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 96, 1, 2),
    _SvcTmplUserCreatorSvcId_Type()
)
svcTmplUserCreatorSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTmplUserCreatorSvcId.setStatus("current")
_SvcTlsExtTable_Object = MibTable
svcTlsExtTable = _SvcTlsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97)
)
if mibBuilder.loadTexts:
    svcTlsExtTable.setStatus("current")
_SvcTlsExtEntry_Object = MibTableRow
svcTlsExtEntry = _SvcTlsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1)
)
if mibBuilder.loadTexts:
    svcTlsExtEntry.setStatus("current")


class _SvcTlsExtMvrpMaxAttributes_Type(Unsigned32):
    """Custom type svcTlsExtMvrpMaxAttributes based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SvcTlsExtMvrpMaxAttributes_Type.__name__ = "Unsigned32"
_SvcTlsExtMvrpMaxAttributes_Object = MibTableColumn
svcTlsExtMvrpMaxAttributes = _SvcTlsExtMvrpMaxAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 1),
    _SvcTlsExtMvrpMaxAttributes_Type()
)
svcTlsExtMvrpMaxAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsExtMvrpMaxAttributes.setStatus("current")
_SvcTlsExtMvrpRegAttrCnt_Type = Unsigned32
_SvcTlsExtMvrpRegAttrCnt_Object = MibTableColumn
svcTlsExtMvrpRegAttrCnt = _SvcTlsExtMvrpRegAttrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 2),
    _SvcTlsExtMvrpRegAttrCnt_Type()
)
svcTlsExtMvrpRegAttrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsExtMvrpRegAttrCnt.setStatus("current")
_SvcTlsExtMvrpDeclaredAttrCnt_Type = Unsigned32
_SvcTlsExtMvrpDeclaredAttrCnt_Object = MibTableColumn
svcTlsExtMvrpDeclaredAttrCnt = _SvcTlsExtMvrpDeclaredAttrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 3),
    _SvcTlsExtMvrpDeclaredAttrCnt_Type()
)
svcTlsExtMvrpDeclaredAttrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsExtMvrpDeclaredAttrCnt.setStatus("current")
_SvcTlsExtMvrpFailedRegCnt_Type = Unsigned32
_SvcTlsExtMvrpFailedRegCnt_Object = MibTableColumn
svcTlsExtMvrpFailedRegCnt = _SvcTlsExtMvrpFailedRegCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 4),
    _SvcTlsExtMvrpFailedRegCnt_Type()
)
svcTlsExtMvrpFailedRegCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsExtMvrpFailedRegCnt.setStatus("current")


class _SvcTlsExtMvrpAttrTblHighWM_Type(Integer32):
    """Custom type svcTlsExtMvrpAttrTblHighWM based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTlsExtMvrpAttrTblHighWM_Type.__name__ = "Integer32"
_SvcTlsExtMvrpAttrTblHighWM_Object = MibTableColumn
svcTlsExtMvrpAttrTblHighWM = _SvcTlsExtMvrpAttrTblHighWM_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 5),
    _SvcTlsExtMvrpAttrTblHighWM_Type()
)
svcTlsExtMvrpAttrTblHighWM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsExtMvrpAttrTblHighWM.setStatus("current")


class _SvcTlsExtMvrpAttrTblLowWM_Type(Integer32):
    """Custom type svcTlsExtMvrpAttrTblLowWM based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SvcTlsExtMvrpAttrTblLowWM_Type.__name__ = "Integer32"
_SvcTlsExtMvrpAttrTblLowWM_Object = MibTableColumn
svcTlsExtMvrpAttrTblLowWM = _SvcTlsExtMvrpAttrTblLowWM_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 6),
    _SvcTlsExtMvrpAttrTblLowWM_Type()
)
svcTlsExtMvrpAttrTblLowWM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsExtMvrpAttrTblLowWM.setStatus("current")


class _SvcTlsExtMvrpHoldTime_Type(Unsigned32):
    """Custom type svcTlsExtMvrpHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 30),
    )


_SvcTlsExtMvrpHoldTime_Type.__name__ = "Unsigned32"
_SvcTlsExtMvrpHoldTime_Object = MibTableColumn
svcTlsExtMvrpHoldTime = _SvcTlsExtMvrpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 7),
    _SvcTlsExtMvrpHoldTime_Type()
)
svcTlsExtMvrpHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsExtMvrpHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsExtMvrpHoldTime.setUnits("minutes")


class _SvcTlsExtMvrpAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type svcTlsExtMvrpAdminStatus based on TmnxEnabledDisabled"""


_SvcTlsExtMvrpAdminStatus_Object = MibTableColumn
svcTlsExtMvrpAdminStatus = _SvcTlsExtMvrpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 8),
    _SvcTlsExtMvrpAdminStatus_Type()
)
svcTlsExtMvrpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsExtMvrpAdminStatus.setStatus("current")


class _SvcTlsExtMvrpOperStatus_Type(Integer32):
    """Custom type svcTlsExtMvrpOperStatus based on Integer32"""
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


_SvcTlsExtMvrpOperStatus_Type.__name__ = "Integer32"
_SvcTlsExtMvrpOperStatus_Object = MibTableColumn
svcTlsExtMvrpOperStatus = _SvcTlsExtMvrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 9),
    _SvcTlsExtMvrpOperStatus_Type()
)
svcTlsExtMvrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsExtMvrpOperStatus.setStatus("current")
_SvcTlsExtMmrpAdminStatus_Type = TmnxEnabledDisabled
_SvcTlsExtMmrpAdminStatus_Object = MibTableColumn
svcTlsExtMmrpAdminStatus = _SvcTlsExtMmrpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 10),
    _SvcTlsExtMmrpAdminStatus_Type()
)
svcTlsExtMmrpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsExtMmrpAdminStatus.setStatus("current")


class _SvcTlsExtMmrpOperStatus_Type(Integer32):
    """Custom type svcTlsExtMmrpOperStatus based on Integer32"""
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


_SvcTlsExtMmrpOperStatus_Type.__name__ = "Integer32"
_SvcTlsExtMmrpOperStatus_Object = MibTableColumn
svcTlsExtMmrpOperStatus = _SvcTlsExtMmrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 11),
    _SvcTlsExtMmrpOperStatus_Type()
)
svcTlsExtMmrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsExtMmrpOperStatus.setStatus("current")
_SvcTlsExtMmrpRegAttrCnt_Type = Unsigned32
_SvcTlsExtMmrpRegAttrCnt_Object = MibTableColumn
svcTlsExtMmrpRegAttrCnt = _SvcTlsExtMmrpRegAttrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 12),
    _SvcTlsExtMmrpRegAttrCnt_Type()
)
svcTlsExtMmrpRegAttrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsExtMmrpRegAttrCnt.setStatus("current")
_SvcTlsExtMmrpDeclaredAttrCnt_Type = Unsigned32
_SvcTlsExtMmrpDeclaredAttrCnt_Object = MibTableColumn
svcTlsExtMmrpDeclaredAttrCnt = _SvcTlsExtMmrpDeclaredAttrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 13),
    _SvcTlsExtMmrpDeclaredAttrCnt_Type()
)
svcTlsExtMmrpDeclaredAttrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsExtMmrpDeclaredAttrCnt.setStatus("current")
_SvcTlsExtMmrpFailedRegCnt_Type = Unsigned32
_SvcTlsExtMmrpFailedRegCnt_Object = MibTableColumn
svcTlsExtMmrpFailedRegCnt = _SvcTlsExtMmrpFailedRegCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 14),
    _SvcTlsExtMmrpFailedRegCnt_Type()
)
svcTlsExtMmrpFailedRegCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsExtMmrpFailedRegCnt.setStatus("current")
_SvcTlsExtMvrpAttributeCount_Type = Unsigned32
_SvcTlsExtMvrpAttributeCount_Object = MibTableColumn
svcTlsExtMvrpAttributeCount = _SvcTlsExtMvrpAttributeCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 15),
    _SvcTlsExtMvrpAttributeCount_Type()
)
svcTlsExtMvrpAttributeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsExtMvrpAttributeCount.setStatus("current")


class _SvcTlsExtMmrpEndStationOnly_Type(TruthValue):
    """Custom type svcTlsExtMmrpEndStationOnly based on TruthValue"""


_SvcTlsExtMmrpEndStationOnly_Object = MibTableColumn
svcTlsExtMmrpEndStationOnly = _SvcTlsExtMmrpEndStationOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 16),
    _SvcTlsExtMmrpEndStationOnly_Type()
)
svcTlsExtMmrpEndStationOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsExtMmrpEndStationOnly.setStatus("current")


class _SvcTlsExtMacReNotifInterval_Type(Unsigned32):
    """Custom type svcTlsExtMacReNotifInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(240, 840),
    )


_SvcTlsExtMacReNotifInterval_Type.__name__ = "Unsigned32"
_SvcTlsExtMacReNotifInterval_Object = MibTableColumn
svcTlsExtMacReNotifInterval = _SvcTlsExtMacReNotifInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 17),
    _SvcTlsExtMacReNotifInterval_Type()
)
svcTlsExtMacReNotifInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsExtMacReNotifInterval.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsExtMacReNotifInterval.setUnits("seconds")


class _SvcTlsExtSpbmCtrlVpls_Type(TmnxServId):
    """Custom type svcTlsExtSpbmCtrlVpls based on TmnxServId"""
    defaultValue = 0


_SvcTlsExtSpbmCtrlVpls_Object = MibTableColumn
svcTlsExtSpbmCtrlVpls = _SvcTlsExtSpbmCtrlVpls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 18),
    _SvcTlsExtSpbmCtrlVpls_Type()
)
svcTlsExtSpbmCtrlVpls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsExtSpbmCtrlVpls.setStatus("current")


class _SvcTlsExtSpbmFid_Type(TmnxSpbFidOrZero):
    """Custom type svcTlsExtSpbmFid based on TmnxSpbFidOrZero"""
    defaultValue = 0


_SvcTlsExtSpbmFid_Object = MibTableColumn
svcTlsExtSpbmFid = _SvcTlsExtSpbmFid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 97, 1, 19),
    _SvcTlsExtSpbmFid_Type()
)
svcTlsExtSpbmFid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcTlsExtSpbmFid.setStatus("current")
_SvcPwRtLclPrefixTblLastChanged_Type = TimeStamp
_SvcPwRtLclPrefixTblLastChanged_Object = MibScalar
svcPwRtLclPrefixTblLastChanged = _SvcPwRtLclPrefixTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 98),
    _SvcPwRtLclPrefixTblLastChanged_Type()
)
svcPwRtLclPrefixTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtLclPrefixTblLastChanged.setStatus("current")
_SvcPwRtLclPrefixTable_Object = MibTable
svcPwRtLclPrefixTable = _SvcPwRtLclPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 99)
)
if mibBuilder.loadTexts:
    svcPwRtLclPrefixTable.setStatus("current")
_SvcPwRtLclPrefixEntry_Object = MibTableRow
svcPwRtLclPrefixEntry = _SvcPwRtLclPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 99, 1)
)
svcPwRtLclPrefixEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcPwRtLclPrefixGlobalId"),
    (0, "TIMETRA-SERV-MIB", "svcPwRtLclPrefix"),
)
if mibBuilder.loadTexts:
    svcPwRtLclPrefixEntry.setStatus("current")
_SvcPwRtLclPrefixGlobalId_Type = TmnxPwGlobalId
_SvcPwRtLclPrefixGlobalId_Object = MibTableColumn
svcPwRtLclPrefixGlobalId = _SvcPwRtLclPrefixGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 99, 1, 1),
    _SvcPwRtLclPrefixGlobalId_Type()
)
svcPwRtLclPrefixGlobalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPwRtLclPrefixGlobalId.setStatus("current")


class _SvcPwRtLclPrefix_Type(Unsigned32):
    """Custom type svcPwRtLclPrefix based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SvcPwRtLclPrefix_Type.__name__ = "Unsigned32"
_SvcPwRtLclPrefix_Object = MibTableColumn
svcPwRtLclPrefix = _SvcPwRtLclPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 99, 1, 2),
    _SvcPwRtLclPrefix_Type()
)
svcPwRtLclPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPwRtLclPrefix.setStatus("current")
_SvcPwRtLclPrefixRowStatus_Type = RowStatus
_SvcPwRtLclPrefixRowStatus_Object = MibTableColumn
svcPwRtLclPrefixRowStatus = _SvcPwRtLclPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 99, 1, 3),
    _SvcPwRtLclPrefixRowStatus_Type()
)
svcPwRtLclPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPwRtLclPrefixRowStatus.setStatus("current")
_SvcPwRtLclPrefixLastChange_Type = TimeStamp
_SvcPwRtLclPrefixLastChange_Object = MibTableColumn
svcPwRtLclPrefixLastChange = _SvcPwRtLclPrefixLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 99, 1, 4),
    _SvcPwRtLclPrefixLastChange_Type()
)
svcPwRtLclPrefixLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtLclPrefixLastChange.setStatus("current")
_SvcPwRtPathTblLastChanged_Type = TimeStamp
_SvcPwRtPathTblLastChanged_Object = MibScalar
svcPwRtPathTblLastChanged = _SvcPwRtPathTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 100),
    _SvcPwRtPathTblLastChanged_Type()
)
svcPwRtPathTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtPathTblLastChanged.setStatus("current")
_SvcPwRtPathTable_Object = MibTable
svcPwRtPathTable = _SvcPwRtPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 101)
)
if mibBuilder.loadTexts:
    svcPwRtPathTable.setStatus("current")
_SvcPwRtPathEntry_Object = MibTableRow
svcPwRtPathEntry = _SvcPwRtPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 101, 1)
)
svcPwRtPathEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcPwRtPathName"),
)
if mibBuilder.loadTexts:
    svcPwRtPathEntry.setStatus("current")
_SvcPwRtPathName_Type = TNamedItem
_SvcPwRtPathName_Object = MibTableColumn
svcPwRtPathName = _SvcPwRtPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 101, 1, 1),
    _SvcPwRtPathName_Type()
)
svcPwRtPathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPwRtPathName.setStatus("current")
_SvcPwRtPathRowStatus_Type = RowStatus
_SvcPwRtPathRowStatus_Object = MibTableColumn
svcPwRtPathRowStatus = _SvcPwRtPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 101, 1, 2),
    _SvcPwRtPathRowStatus_Type()
)
svcPwRtPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPwRtPathRowStatus.setStatus("current")
_SvcPwRtPathLastChange_Type = TimeStamp
_SvcPwRtPathLastChange_Object = MibTableColumn
svcPwRtPathLastChange = _SvcPwRtPathLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 101, 1, 3),
    _SvcPwRtPathLastChange_Type()
)
svcPwRtPathLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtPathLastChange.setStatus("current")


class _SvcPwRtPathAdminStatus_Type(ServiceAdminStatus):
    """Custom type svcPwRtPathAdminStatus based on ServiceAdminStatus"""


_SvcPwRtPathAdminStatus_Object = MibTableColumn
svcPwRtPathAdminStatus = _SvcPwRtPathAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 101, 1, 4),
    _SvcPwRtPathAdminStatus_Type()
)
svcPwRtPathAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPwRtPathAdminStatus.setStatus("current")
_SvcPwRtPathHopTblLastChgd_Type = TimeStamp
_SvcPwRtPathHopTblLastChgd_Object = MibScalar
svcPwRtPathHopTblLastChgd = _SvcPwRtPathHopTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 102),
    _SvcPwRtPathHopTblLastChgd_Type()
)
svcPwRtPathHopTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtPathHopTblLastChgd.setStatus("current")
_SvcPwRtPathHopTable_Object = MibTable
svcPwRtPathHopTable = _SvcPwRtPathHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 103)
)
if mibBuilder.loadTexts:
    svcPwRtPathHopTable.setStatus("current")
_SvcPwRtPathHopEntry_Object = MibTableRow
svcPwRtPathHopEntry = _SvcPwRtPathHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 103, 1)
)
svcPwRtPathHopEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcPwRtPathName"),
    (0, "TIMETRA-SERV-MIB", "svcPwRtPathHopIndex"),
)
if mibBuilder.loadTexts:
    svcPwRtPathHopEntry.setStatus("current")
_SvcPwRtPathHopIndex_Type = TmnxPwPathHopId
_SvcPwRtPathHopIndex_Object = MibTableColumn
svcPwRtPathHopIndex = _SvcPwRtPathHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 103, 1, 1),
    _SvcPwRtPathHopIndex_Type()
)
svcPwRtPathHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPwRtPathHopIndex.setStatus("current")
_SvcPwRtPathHopRowStatus_Type = RowStatus
_SvcPwRtPathHopRowStatus_Object = MibTableColumn
svcPwRtPathHopRowStatus = _SvcPwRtPathHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 103, 1, 2),
    _SvcPwRtPathHopRowStatus_Type()
)
svcPwRtPathHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPwRtPathHopRowStatus.setStatus("current")
_SvcPwRtPathHopLastChange_Type = TimeStamp
_SvcPwRtPathHopLastChange_Object = MibTableColumn
svcPwRtPathHopLastChange = _SvcPwRtPathHopLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 103, 1, 3),
    _SvcPwRtPathHopLastChange_Type()
)
svcPwRtPathHopLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtPathHopLastChange.setStatus("current")


class _SvcPwRtPathHopAddrType_Type(InetAddressType):
    """Custom type svcPwRtPathHopAddrType based on InetAddressType"""


_SvcPwRtPathHopAddrType_Object = MibTableColumn
svcPwRtPathHopAddrType = _SvcPwRtPathHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 103, 1, 4),
    _SvcPwRtPathHopAddrType_Type()
)
svcPwRtPathHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPwRtPathHopAddrType.setStatus("current")


class _SvcPwRtPathHopAddr_Type(InetAddress):
    """Custom type svcPwRtPathHopAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SvcPwRtPathHopAddr_Type.__name__ = "InetAddress"
_SvcPwRtPathHopAddr_Object = MibTableColumn
svcPwRtPathHopAddr = _SvcPwRtPathHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 103, 1, 5),
    _SvcPwRtPathHopAddr_Type()
)
svcPwRtPathHopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPwRtPathHopAddr.setStatus("current")
_SvcPwRtStaticRtTblLastChgd_Type = TimeStamp
_SvcPwRtStaticRtTblLastChgd_Object = MibScalar
svcPwRtStaticRtTblLastChgd = _SvcPwRtStaticRtTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 104),
    _SvcPwRtStaticRtTblLastChgd_Type()
)
svcPwRtStaticRtTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtStaticRtTblLastChgd.setStatus("current")
_SvcPwRtStaticRtTable_Object = MibTable
svcPwRtStaticRtTable = _SvcPwRtStaticRtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 105)
)
if mibBuilder.loadTexts:
    svcPwRtStaticRtTable.setStatus("current")
_SvcPwRtStaticRtEntry_Object = MibTableRow
svcPwRtStaticRtEntry = _SvcPwRtStaticRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 105, 1)
)
svcPwRtStaticRtEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcPwRtStaticRtDstGlobalId"),
    (0, "TIMETRA-SERV-MIB", "svcPwRtStaticRtDstPrefix"),
    (0, "TIMETRA-SERV-MIB", "svcPwRtStaticRtDstAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcPwRtStaticRtDstAddr"),
)
if mibBuilder.loadTexts:
    svcPwRtStaticRtEntry.setStatus("current")
_SvcPwRtStaticRtDstGlobalId_Type = TmnxPwGlobalIdOrZero
_SvcPwRtStaticRtDstGlobalId_Object = MibTableColumn
svcPwRtStaticRtDstGlobalId = _SvcPwRtStaticRtDstGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 105, 1, 1),
    _SvcPwRtStaticRtDstGlobalId_Type()
)
svcPwRtStaticRtDstGlobalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPwRtStaticRtDstGlobalId.setStatus("current")
_SvcPwRtStaticRtDstPrefix_Type = Unsigned32
_SvcPwRtStaticRtDstPrefix_Object = MibTableColumn
svcPwRtStaticRtDstPrefix = _SvcPwRtStaticRtDstPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 105, 1, 2),
    _SvcPwRtStaticRtDstPrefix_Type()
)
svcPwRtStaticRtDstPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPwRtStaticRtDstPrefix.setStatus("current")
_SvcPwRtStaticRtDstAddrType_Type = InetAddressType
_SvcPwRtStaticRtDstAddrType_Object = MibTableColumn
svcPwRtStaticRtDstAddrType = _SvcPwRtStaticRtDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 105, 1, 3),
    _SvcPwRtStaticRtDstAddrType_Type()
)
svcPwRtStaticRtDstAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPwRtStaticRtDstAddrType.setStatus("current")


class _SvcPwRtStaticRtDstAddr_Type(InetAddress):
    """Custom type svcPwRtStaticRtDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SvcPwRtStaticRtDstAddr_Type.__name__ = "InetAddress"
_SvcPwRtStaticRtDstAddr_Object = MibTableColumn
svcPwRtStaticRtDstAddr = _SvcPwRtStaticRtDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 105, 1, 4),
    _SvcPwRtStaticRtDstAddr_Type()
)
svcPwRtStaticRtDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPwRtStaticRtDstAddr.setStatus("current")
_SvcPwRtStaticRtRowStatus_Type = RowStatus
_SvcPwRtStaticRtRowStatus_Object = MibTableColumn
svcPwRtStaticRtRowStatus = _SvcPwRtStaticRtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 105, 1, 5),
    _SvcPwRtStaticRtRowStatus_Type()
)
svcPwRtStaticRtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPwRtStaticRtRowStatus.setStatus("current")
_SvcPwRtStaticRtLastChange_Type = TimeStamp
_SvcPwRtStaticRtLastChange_Object = MibTableColumn
svcPwRtStaticRtLastChange = _SvcPwRtStaticRtLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 105, 1, 6),
    _SvcPwRtStaticRtLastChange_Type()
)
svcPwRtStaticRtLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtStaticRtLastChange.setStatus("current")
_SvcMSPwPeTblLastChanged_Type = TimeStamp
_SvcMSPwPeTblLastChanged_Object = MibScalar
svcMSPwPeTblLastChanged = _SvcMSPwPeTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 106),
    _SvcMSPwPeTblLastChanged_Type()
)
svcMSPwPeTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMSPwPeTblLastChanged.setStatus("current")
_SvcMSPwPeTable_Object = MibTable
svcMSPwPeTable = _SvcMSPwPeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107)
)
if mibBuilder.loadTexts:
    svcMSPwPeTable.setStatus("current")
_SvcMSPwPeEntry_Object = MibTableRow
svcMSPwPeEntry = _SvcMSPwPeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1)
)
svcMSPwPeEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcMSPwPeId"),
)
if mibBuilder.loadTexts:
    svcMSPwPeEntry.setStatus("current")
_SvcMSPwPeId_Type = TmnxSpokeSdpId
_SvcMSPwPeId_Object = MibTableColumn
svcMSPwPeId = _SvcMSPwPeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 1),
    _SvcMSPwPeId_Type()
)
svcMSPwPeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcMSPwPeId.setStatus("current")
_SvcMSPwPeRowStatus_Type = RowStatus
_SvcMSPwPeRowStatus_Object = MibTableColumn
svcMSPwPeRowStatus = _SvcMSPwPeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 2),
    _SvcMSPwPeRowStatus_Type()
)
svcMSPwPeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeRowStatus.setStatus("current")
_SvcMSPwPeLastChange_Type = TimeStamp
_SvcMSPwPeLastChange_Object = MibTableColumn
svcMSPwPeLastChange = _SvcMSPwPeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 3),
    _SvcMSPwPeLastChange_Type()
)
svcMSPwPeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMSPwPeLastChange.setStatus("current")


class _SvcMSPwPeAdminStatus_Type(ServiceAdminStatus):
    """Custom type svcMSPwPeAdminStatus based on ServiceAdminStatus"""


_SvcMSPwPeAdminStatus_Object = MibTableColumn
svcMSPwPeAdminStatus = _SvcMSPwPeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 4),
    _SvcMSPwPeAdminStatus_Type()
)
svcMSPwPeAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeAdminStatus.setStatus("current")


class _SvcMSPwPeFecType_Type(TmnxLdpFECType):
    """Custom type svcMSPwPeFecType based on TmnxLdpFECType"""


_SvcMSPwPeFecType_Object = MibTableColumn
svcMSPwPeFecType = _SvcMSPwPeFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 5),
    _SvcMSPwPeFecType_Type()
)
svcMSPwPeFecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeFecType.setStatus("current")


class _SvcMSPwPeAiiType_Type(TmnxAiiType):
    """Custom type svcMSPwPeAiiType based on TmnxAiiType"""


_SvcMSPwPeAiiType_Object = MibTableColumn
svcMSPwPeAiiType = _SvcMSPwPeAiiType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 6),
    _SvcMSPwPeAiiType_Type()
)
svcMSPwPeAiiType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeAiiType.setStatus("current")


class _SvcMSPwPeSignaling_Type(TmnxMsPwPeSignaling):
    """Custom type svcMSPwPeSignaling based on TmnxMsPwPeSignaling"""


_SvcMSPwPeSignaling_Object = MibTableColumn
svcMSPwPeSignaling = _SvcMSPwPeSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 7),
    _SvcMSPwPeSignaling_Type()
)
svcMSPwPeSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeSignaling.setStatus("current")


class _SvcMSPwPeAutoConfig_Type(TruthValue):
    """Custom type svcMSPwPeAutoConfig based on TruthValue"""


_SvcMSPwPeAutoConfig_Object = MibTableColumn
svcMSPwPeAutoConfig = _SvcMSPwPeAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 8),
    _SvcMSPwPeAutoConfig_Type()
)
svcMSPwPeAutoConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeAutoConfig.setStatus("current")


class _SvcMSPwPeAgi_Type(TmnxVPNRouteDistinguisher):
    """Custom type svcMSPwPeAgi based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_SvcMSPwPeAgi_Object = MibTableColumn
svcMSPwPeAgi = _SvcMSPwPeAgi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 9),
    _SvcMSPwPeAgi_Type()
)
svcMSPwPeAgi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeAgi.setStatus("current")


class _SvcMSPwPePolicyId_Type(PWTemplateId):
    """Custom type svcMSPwPePolicyId based on PWTemplateId"""
    defaultValue = 0


_SvcMSPwPePolicyId_Object = MibTableColumn
svcMSPwPePolicyId = _SvcMSPwPePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 10),
    _SvcMSPwPePolicyId_Type()
)
svcMSPwPePolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPePolicyId.setStatus("current")


class _SvcMSPwPePrecedence_Type(Unsigned32):
    """Custom type svcMSPwPePrecedence based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SvcMSPwPePrecedence_Type.__name__ = "Unsigned32"
_SvcMSPwPePrecedence_Object = MibTableColumn
svcMSPwPePrecedence = _SvcMSPwPePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 11),
    _SvcMSPwPePrecedence_Type()
)
svcMSPwPePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPePrecedence.setStatus("current")


class _SvcMSPwPeRetryTimer_Type(Unsigned32):
    """Custom type svcMSPwPeRetryTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 480),
    )


_SvcMSPwPeRetryTimer_Type.__name__ = "Unsigned32"
_SvcMSPwPeRetryTimer_Object = MibTableColumn
svcMSPwPeRetryTimer = _SvcMSPwPeRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 12),
    _SvcMSPwPeRetryTimer_Type()
)
svcMSPwPeRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    svcMSPwPeRetryTimer.setUnits("seconds")


class _SvcMSPwPeRetryCount_Type(Unsigned32):
    """Custom type svcMSPwPeRetryCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10000),
    )


_SvcMSPwPeRetryCount_Type.__name__ = "Unsigned32"
_SvcMSPwPeRetryCount_Object = MibTableColumn
svcMSPwPeRetryCount = _SvcMSPwPeRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 13),
    _SvcMSPwPeRetryCount_Type()
)
svcMSPwPeRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeRetryCount.setStatus("current")


class _SvcMSPwPeSaiiGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type svcMSPwPeSaiiGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_SvcMSPwPeSaiiGlobalId_Object = MibTableColumn
svcMSPwPeSaiiGlobalId = _SvcMSPwPeSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 14),
    _SvcMSPwPeSaiiGlobalId_Type()
)
svcMSPwPeSaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeSaiiGlobalId.setStatus("current")


class _SvcMSPwPeSaiiPrefix_Type(Unsigned32):
    """Custom type svcMSPwPeSaiiPrefix based on Unsigned32"""
    defaultValue = 0


_SvcMSPwPeSaiiPrefix_Object = MibTableColumn
svcMSPwPeSaiiPrefix = _SvcMSPwPeSaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 15),
    _SvcMSPwPeSaiiPrefix_Type()
)
svcMSPwPeSaiiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeSaiiPrefix.setStatus("current")


class _SvcMSPwPeSaiiAcId_Type(Unsigned32):
    """Custom type svcMSPwPeSaiiAcId based on Unsigned32"""
    defaultValue = 0


_SvcMSPwPeSaiiAcId_Object = MibTableColumn
svcMSPwPeSaiiAcId = _SvcMSPwPeSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 16),
    _SvcMSPwPeSaiiAcId_Type()
)
svcMSPwPeSaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeSaiiAcId.setStatus("current")


class _SvcMSPwPeTaiiGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type svcMSPwPeTaiiGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_SvcMSPwPeTaiiGlobalId_Object = MibTableColumn
svcMSPwPeTaiiGlobalId = _SvcMSPwPeTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 17),
    _SvcMSPwPeTaiiGlobalId_Type()
)
svcMSPwPeTaiiGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeTaiiGlobalId.setStatus("current")


class _SvcMSPwPeTaiiPrefix_Type(Unsigned32):
    """Custom type svcMSPwPeTaiiPrefix based on Unsigned32"""
    defaultValue = 0


_SvcMSPwPeTaiiPrefix_Object = MibTableColumn
svcMSPwPeTaiiPrefix = _SvcMSPwPeTaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 18),
    _SvcMSPwPeTaiiPrefix_Type()
)
svcMSPwPeTaiiPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeTaiiPrefix.setStatus("current")


class _SvcMSPwPeTaiiAcId_Type(Unsigned32):
    """Custom type svcMSPwPeTaiiAcId based on Unsigned32"""
    defaultValue = 0


_SvcMSPwPeTaiiAcId_Object = MibTableColumn
svcMSPwPeTaiiAcId = _SvcMSPwPeTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 19),
    _SvcMSPwPeTaiiAcId_Type()
)
svcMSPwPeTaiiAcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeTaiiAcId.setStatus("current")


class _SvcMSPwPePathName_Type(TNamedItemOrEmpty):
    """Custom type svcMSPwPePathName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SvcMSPwPePathName_Object = MibTableColumn
svcMSPwPePathName = _SvcMSPwPePathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 20),
    _SvcMSPwPePathName_Type()
)
svcMSPwPePathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPePathName.setStatus("current")


class _SvcMSPwPeEndPoint_Type(TNamedItemOrEmpty):
    """Custom type svcMSPwPeEndPoint based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SvcMSPwPeEndPoint_Object = MibTableColumn
svcMSPwPeEndPoint = _SvcMSPwPeEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 21),
    _SvcMSPwPeEndPoint_Type()
)
svcMSPwPeEndPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeEndPoint.setStatus("current")


class _SvcMSPwPeStandbySigSlave_Type(TruthValue):
    """Custom type svcMSPwPeStandbySigSlave based on TruthValue"""


_SvcMSPwPeStandbySigSlave_Object = MibTableColumn
svcMSPwPeStandbySigSlave = _SvcMSPwPeStandbySigSlave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 22),
    _SvcMSPwPeStandbySigSlave_Type()
)
svcMSPwPeStandbySigSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeStandbySigSlave.setStatus("current")


class _SvcMSPwPeIsICB_Type(TruthValue):
    """Custom type svcMSPwPeIsICB based on TruthValue"""


_SvcMSPwPeIsICB_Object = MibTableColumn
svcMSPwPeIsICB = _SvcMSPwPeIsICB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 23),
    _SvcMSPwPeIsICB_Type()
)
svcMSPwPeIsICB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcMSPwPeIsICB.setStatus("current")
_SvcMSPwPeTimeRemain_Type = Unsigned32
_SvcMSPwPeTimeRemain_Object = MibTableColumn
svcMSPwPeTimeRemain = _SvcMSPwPeTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 24),
    _SvcMSPwPeTimeRemain_Type()
)
svcMSPwPeTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMSPwPeTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    svcMSPwPeTimeRemain.setUnits("seconds")
_SvcMSPwPeRetryRemain_Type = Unsigned32
_SvcMSPwPeRetryRemain_Object = MibTableColumn
svcMSPwPeRetryRemain = _SvcMSPwPeRetryRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 25),
    _SvcMSPwPeRetryRemain_Type()
)
svcMSPwPeRetryRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMSPwPeRetryRemain.setStatus("current")
_SvcMSPwPeOperSdpBind_Type = SdpBindId
_SvcMSPwPeOperSdpBind_Object = MibTableColumn
svcMSPwPeOperSdpBind = _SvcMSPwPeOperSdpBind_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 26),
    _SvcMSPwPeOperSdpBind_Type()
)
svcMSPwPeOperSdpBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMSPwPeOperSdpBind.setStatus("current")
_SvcMSPwPeRetryExpired_Type = TruthValue
_SvcMSPwPeRetryExpired_Object = MibTableColumn
svcMSPwPeRetryExpired = _SvcMSPwPeRetryExpired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 27),
    _SvcMSPwPeRetryExpired_Type()
)
svcMSPwPeRetryExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMSPwPeRetryExpired.setStatus("current")
_SvcMSPwPeLastError_Type = DisplayString
_SvcMSPwPeLastError_Object = MibTableColumn
svcMSPwPeLastError = _SvcMSPwPeLastError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 107, 1, 28),
    _SvcMSPwPeLastError_Type()
)
svcMSPwPeLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMSPwPeLastError.setStatus("current")
_SvcOperGrpTblLastChanged_Type = TimeStamp
_SvcOperGrpTblLastChanged_Object = MibScalar
svcOperGrpTblLastChanged = _SvcOperGrpTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 108),
    _SvcOperGrpTblLastChanged_Type()
)
svcOperGrpTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcOperGrpTblLastChanged.setStatus("current")
_SvcOperGrpTable_Object = MibTable
svcOperGrpTable = _SvcOperGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109)
)
if mibBuilder.loadTexts:
    svcOperGrpTable.setStatus("current")
_SvcOperGrpEntry_Object = MibTableRow
svcOperGrpEntry = _SvcOperGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1)
)
svcOperGrpEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcOperGrpName"),
)
if mibBuilder.loadTexts:
    svcOperGrpEntry.setStatus("current")
_SvcOperGrpName_Type = TNamedItem
_SvcOperGrpName_Object = MibTableColumn
svcOperGrpName = _SvcOperGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 1),
    _SvcOperGrpName_Type()
)
svcOperGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcOperGrpName.setStatus("current")
_SvcOperGrpRowStatus_Type = RowStatus
_SvcOperGrpRowStatus_Object = MibTableColumn
svcOperGrpRowStatus = _SvcOperGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 2),
    _SvcOperGrpRowStatus_Type()
)
svcOperGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcOperGrpRowStatus.setStatus("current")
_SvcOperGrpLastChange_Type = TimeStamp
_SvcOperGrpLastChange_Object = MibTableColumn
svcOperGrpLastChange = _SvcOperGrpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 3),
    _SvcOperGrpLastChange_Type()
)
svcOperGrpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcOperGrpLastChange.setStatus("current")
_SvcOperGrpOperStatus_Type = ServiceOperStatus
_SvcOperGrpOperStatus_Object = MibTableColumn
svcOperGrpOperStatus = _SvcOperGrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 4),
    _SvcOperGrpOperStatus_Type()
)
svcOperGrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcOperGrpOperStatus.setStatus("current")


class _SvcOperGrpHoldDownTime_Type(TmnxOperGrpHoldDownTime):
    """Custom type svcOperGrpHoldDownTime based on TmnxOperGrpHoldDownTime"""
    defaultValue = 0


_SvcOperGrpHoldDownTime_Object = MibTableColumn
svcOperGrpHoldDownTime = _SvcOperGrpHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 5),
    _SvcOperGrpHoldDownTime_Type()
)
svcOperGrpHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcOperGrpHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    svcOperGrpHoldDownTime.setUnits("seconds")
_SvcOperGrpCreationOrigin_Type = TmnxSvcOperGrpCreationOrigin
_SvcOperGrpCreationOrigin_Object = MibTableColumn
svcOperGrpCreationOrigin = _SvcOperGrpCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 6),
    _SvcOperGrpCreationOrigin_Type()
)
svcOperGrpCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcOperGrpCreationOrigin.setStatus("current")


class _SvcOperGrpHoldUpTime_Type(TmnxOperGrpHoldUpTime):
    """Custom type svcOperGrpHoldUpTime based on TmnxOperGrpHoldUpTime"""
    defaultValue = 4


_SvcOperGrpHoldUpTime_Object = MibTableColumn
svcOperGrpHoldUpTime = _SvcOperGrpHoldUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 7),
    _SvcOperGrpHoldUpTime_Type()
)
svcOperGrpHoldUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcOperGrpHoldUpTime.setStatus("current")
if mibBuilder.loadTexts:
    svcOperGrpHoldUpTime.setUnits("seconds")
_SvcOperGrpHoldUpTimeRemain_Type = TmnxOperGrpHoldUpTime
_SvcOperGrpHoldUpTimeRemain_Object = MibTableColumn
svcOperGrpHoldUpTimeRemain = _SvcOperGrpHoldUpTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 8),
    _SvcOperGrpHoldUpTimeRemain_Type()
)
svcOperGrpHoldUpTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcOperGrpHoldUpTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    svcOperGrpHoldUpTimeRemain.setUnits("seconds")
_SvcOperGrpHoldDownTimeRemain_Type = TmnxOperGrpHoldDownTime
_SvcOperGrpHoldDownTimeRemain_Object = MibTableColumn
svcOperGrpHoldDownTimeRemain = _SvcOperGrpHoldDownTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 9),
    _SvcOperGrpHoldDownTimeRemain_Type()
)
svcOperGrpHoldDownTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcOperGrpHoldDownTimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    svcOperGrpHoldDownTimeRemain.setUnits("seconds")
_SvcOperGrpNumMembers_Type = Gauge32
_SvcOperGrpNumMembers_Object = MibTableColumn
svcOperGrpNumMembers = _SvcOperGrpNumMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 10),
    _SvcOperGrpNumMembers_Type()
)
svcOperGrpNumMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcOperGrpNumMembers.setStatus("current")
_SvcOperGrpNumMonitoring_Type = Gauge32
_SvcOperGrpNumMonitoring_Object = MibTableColumn
svcOperGrpNumMonitoring = _SvcOperGrpNumMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 109, 1, 11),
    _SvcOperGrpNumMonitoring_Type()
)
svcOperGrpNumMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcOperGrpNumMonitoring.setStatus("current")
_SvcDhcpLeaseAleTable_Object = MibTable
svcDhcpLeaseAleTable = _SvcDhcpLeaseAleTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 110)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseAleTable.setStatus("current")
_SvcDhcpLeaseAleEntry_Object = MibTableRow
svcDhcpLeaseAleEntry = _SvcDhcpLeaseAleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 110, 1)
)
svcDhcpLeaseAleEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseCiAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseCiAddr"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseNextHopMacAddr"),
)
if mibBuilder.loadTexts:
    svcDhcpLeaseAleEntry.setStatus("current")
_SvcDhcpLeaseAleDatalink_Type = TmnxAccessLoopEncapDataLink
_SvcDhcpLeaseAleDatalink_Object = MibTableColumn
svcDhcpLeaseAleDatalink = _SvcDhcpLeaseAleDatalink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 110, 1, 1),
    _SvcDhcpLeaseAleDatalink_Type()
)
svcDhcpLeaseAleDatalink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseAleDatalink.setStatus("current")
_SvcDhcpLeaseAleEncaps1_Type = TmnxAccessLoopEncaps1
_SvcDhcpLeaseAleEncaps1_Object = MibTableColumn
svcDhcpLeaseAleEncaps1 = _SvcDhcpLeaseAleEncaps1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 110, 1, 2),
    _SvcDhcpLeaseAleEncaps1_Type()
)
svcDhcpLeaseAleEncaps1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseAleEncaps1.setStatus("current")
_SvcDhcpLeaseAleEncaps2_Type = TmnxAccessLoopEncaps2
_SvcDhcpLeaseAleEncaps2_Object = MibTableColumn
svcDhcpLeaseAleEncaps2 = _SvcDhcpLeaseAleEncaps2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 110, 1, 3),
    _SvcDhcpLeaseAleEncaps2_Type()
)
svcDhcpLeaseAleEncaps2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseAleEncaps2.setStatus("current")
_SvcEthCfmTblLastChanged_Type = TimeStamp
_SvcEthCfmTblLastChanged_Object = MibScalar
svcEthCfmTblLastChanged = _SvcEthCfmTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 111),
    _SvcEthCfmTblLastChanged_Type()
)
svcEthCfmTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcEthCfmTblLastChanged.setStatus("current")
_SvcEthCfmTable_Object = MibTable
svcEthCfmTable = _SvcEthCfmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 112)
)
if mibBuilder.loadTexts:
    svcEthCfmTable.setStatus("current")
_SvcEthCfmEntry_Object = MibTableRow
svcEthCfmEntry = _SvcEthCfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 112, 1)
)
svcEthCfmEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcEthCfmEntry.setStatus("current")


class _SvcEthCfmTunnelFaultNotification_Type(Integer32):
    """Custom type svcEthCfmTunnelFaultNotification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 2))
    )


_SvcEthCfmTunnelFaultNotification_Type.__name__ = "Integer32"
_SvcEthCfmTunnelFaultNotification_Object = MibTableColumn
svcEthCfmTunnelFaultNotification = _SvcEthCfmTunnelFaultNotification_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 112, 1, 1),
    _SvcEthCfmTunnelFaultNotification_Type()
)
svcEthCfmTunnelFaultNotification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEthCfmTunnelFaultNotification.setStatus("current")


class _SvcEthCfmVMepExtensions_Type(TmnxEnabledDisabled):
    """Custom type svcEthCfmVMepExtensions based on TmnxEnabledDisabled"""


_SvcEthCfmVMepExtensions_Object = MibTableColumn
svcEthCfmVMepExtensions = _SvcEthCfmVMepExtensions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 112, 1, 2),
    _SvcEthCfmVMepExtensions_Type()
)
svcEthCfmVMepExtensions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcEthCfmVMepExtensions.setStatus("current")
_TmnxSvcGrpObjs_ObjectIdentity = ObjectIdentity
tmnxSvcGrpObjs = _TmnxSvcGrpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113)
)
_SvcMacFdbRecords_Type = Unsigned32
_SvcMacFdbRecords_Object = MibScalar
svcMacFdbRecords = _SvcMacFdbRecords_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 1),
    _SvcMacFdbRecords_Type()
)
svcMacFdbRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMacFdbRecords.setStatus("current")


class _SvcPwRtSpeAddrGlobalId_Type(TmnxPwGlobalIdOrZero):
    """Custom type svcPwRtSpeAddrGlobalId based on TmnxPwGlobalIdOrZero"""
    defaultValue = 0


_SvcPwRtSpeAddrGlobalId_Object = MibScalar
svcPwRtSpeAddrGlobalId = _SvcPwRtSpeAddrGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 2),
    _SvcPwRtSpeAddrGlobalId_Type()
)
svcPwRtSpeAddrGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPwRtSpeAddrGlobalId.setStatus("current")


class _SvcPwRtSpeAddrPrefix_Type(Unsigned32):
    """Custom type svcPwRtSpeAddrPrefix based on Unsigned32"""
    defaultValue = 0


_SvcPwRtSpeAddrPrefix_Object = MibScalar
svcPwRtSpeAddrPrefix = _SvcPwRtSpeAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 3),
    _SvcPwRtSpeAddrPrefix_Type()
)
svcPwRtSpeAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPwRtSpeAddrPrefix.setStatus("current")


class _SvcPwRtBootTimer_Type(Integer32):
    """Custom type svcPwRtBootTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SvcPwRtBootTimer_Type.__name__ = "Integer32"
_SvcPwRtBootTimer_Object = MibScalar
svcPwRtBootTimer = _SvcPwRtBootTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 4),
    _SvcPwRtBootTimer_Type()
)
svcPwRtBootTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPwRtBootTimer.setStatus("current")
if mibBuilder.loadTexts:
    svcPwRtBootTimer.setUnits("seconds")


class _SvcPwRtRetryTimer_Type(Unsigned32):
    """Custom type svcPwRtRetryTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 480),
    )


_SvcPwRtRetryTimer_Type.__name__ = "Unsigned32"
_SvcPwRtRetryTimer_Object = MibScalar
svcPwRtRetryTimer = _SvcPwRtRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 5),
    _SvcPwRtRetryTimer_Type()
)
svcPwRtRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPwRtRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    svcPwRtRetryTimer.setUnits("seconds")


class _SvcPwRtRetryCount_Type(Unsigned32):
    """Custom type svcPwRtRetryCount based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_SvcPwRtRetryCount_Type.__name__ = "Unsigned32"
_SvcPwRtRetryCount_Object = MibScalar
svcPwRtRetryCount = _SvcPwRtRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 6),
    _SvcPwRtRetryCount_Type()
)
svcPwRtRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcPwRtRetryCount.setStatus("current")
_SvcPwRtBgpRoutes_Type = Gauge32
_SvcPwRtBgpRoutes_Object = MibScalar
svcPwRtBgpRoutes = _SvcPwRtBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 7),
    _SvcPwRtBgpRoutes_Type()
)
svcPwRtBgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtBgpRoutes.setStatus("current")
_SvcPwRtStaticRoutes_Type = Gauge32
_SvcPwRtStaticRoutes_Object = MibScalar
svcPwRtStaticRoutes = _SvcPwRtStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 8),
    _SvcPwRtStaticRoutes_Type()
)
svcPwRtStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtStaticRoutes.setStatus("current")
_SvcPwRtLocalRoutes_Type = Gauge32
_SvcPwRtLocalRoutes_Object = MibScalar
svcPwRtLocalRoutes = _SvcPwRtLocalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 9),
    _SvcPwRtLocalRoutes_Type()
)
svcPwRtLocalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtLocalRoutes.setStatus("current")
_SvcPwRtHostRoutes_Type = Gauge32
_SvcPwRtHostRoutes_Object = MibScalar
svcPwRtHostRoutes = _SvcPwRtHostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 10),
    _SvcPwRtHostRoutes_Type()
)
svcPwRtHostRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtHostRoutes.setStatus("current")


class _SvcPwRtBootTimerRemain_Type(Integer32):
    """Custom type svcPwRtBootTimerRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SvcPwRtBootTimerRemain_Type.__name__ = "Integer32"
_SvcPwRtBootTimerRemain_Object = MibScalar
svcPwRtBootTimerRemain = _SvcPwRtBootTimerRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 113, 11),
    _SvcPwRtBootTimerRemain_Type()
)
svcPwRtBootTimerRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtBootTimerRemain.setStatus("current")
if mibBuilder.loadTexts:
    svcPwRtBootTimerRemain.setUnits("seconds")
_SvcPwRtLclPfxRDTblLastChanged_Type = TimeStamp
_SvcPwRtLclPfxRDTblLastChanged_Object = MibScalar
svcPwRtLclPfxRDTblLastChanged = _SvcPwRtLclPfxRDTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 114),
    _SvcPwRtLclPfxRDTblLastChanged_Type()
)
svcPwRtLclPfxRDTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtLclPfxRDTblLastChanged.setStatus("current")
_SvcPwRtLclPfxRDTable_Object = MibTable
svcPwRtLclPfxRDTable = _SvcPwRtLclPfxRDTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 115)
)
if mibBuilder.loadTexts:
    svcPwRtLclPfxRDTable.setStatus("current")
_SvcPwRtLclPfxRDEntry_Object = MibTableRow
svcPwRtLclPfxRDEntry = _SvcPwRtLclPfxRDEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 115, 1)
)
svcPwRtLclPfxRDEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcPwRtLclPrefixGlobalId"),
    (0, "TIMETRA-SERV-MIB", "svcPwRtLclPrefix"),
    (0, "TIMETRA-SERV-MIB", "svcPwRtLclPfxRD"),
)
if mibBuilder.loadTexts:
    svcPwRtLclPfxRDEntry.setStatus("current")
_SvcPwRtLclPfxRD_Type = TmnxVPNRouteDistinguisher
_SvcPwRtLclPfxRD_Object = MibTableColumn
svcPwRtLclPfxRD = _SvcPwRtLclPfxRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 115, 1, 1),
    _SvcPwRtLclPfxRD_Type()
)
svcPwRtLclPfxRD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcPwRtLclPfxRD.setStatus("current")
_SvcPwRtLclPfxRDRowStatus_Type = RowStatus
_SvcPwRtLclPfxRDRowStatus_Object = MibTableColumn
svcPwRtLclPfxRDRowStatus = _SvcPwRtLclPfxRDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 115, 1, 2),
    _SvcPwRtLclPfxRDRowStatus_Type()
)
svcPwRtLclPfxRDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPwRtLclPfxRDRowStatus.setStatus("current")
_SvcPwRtLclPfxRDLastChange_Type = TimeStamp
_SvcPwRtLclPfxRDLastChange_Object = MibTableColumn
svcPwRtLclPfxRDLastChange = _SvcPwRtLclPfxRDLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 115, 1, 3),
    _SvcPwRtLclPfxRDLastChange_Type()
)
svcPwRtLclPfxRDLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwRtLclPfxRDLastChange.setStatus("current")


class _SvcPwRtLclPfxRDCommunity_Type(Unsigned32):
    """Custom type svcPwRtLclPfxRDCommunity based on Unsigned32"""
    defaultValue = 0


_SvcPwRtLclPfxRDCommunity_Object = MibTableColumn
svcPwRtLclPfxRDCommunity = _SvcPwRtLclPfxRDCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 115, 1, 4),
    _SvcPwRtLclPfxRDCommunity_Type()
)
svcPwRtLclPfxRDCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPwRtLclPfxRDCommunity.setStatus("current")
_SvcPwSpeSaiiTable_Object = MibTable
svcPwSpeSaiiTable = _SvcPwSpeSaiiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 116)
)
if mibBuilder.loadTexts:
    svcPwSpeSaiiTable.setStatus("current")
_SvcPwSpeSaiiEntry_Object = MibTableRow
svcPwSpeSaiiEntry = _SvcPwSpeSaiiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 116, 1)
)
svcPwSpeSaiiEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcMSPwPeSaiiGlobalId"),
    (0, "TIMETRA-SERV-MIB", "svcMSPwPeSaiiPrefix"),
    (0, "TIMETRA-SERV-MIB", "svcMSPwPeSaiiAcId"),
)
if mibBuilder.loadTexts:
    svcPwSpeSaiiEntry.setStatus("current")
_SvcPwSpeSaiiTaiiGlobalId_Type = TmnxPwGlobalIdOrZero
_SvcPwSpeSaiiTaiiGlobalId_Object = MibTableColumn
svcPwSpeSaiiTaiiGlobalId = _SvcPwSpeSaiiTaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 116, 1, 1),
    _SvcPwSpeSaiiTaiiGlobalId_Type()
)
svcPwSpeSaiiTaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeSaiiTaiiGlobalId.setStatus("current")
_SvcPwSpeSaiiTaiiPrefix_Type = Unsigned32
_SvcPwSpeSaiiTaiiPrefix_Object = MibTableColumn
svcPwSpeSaiiTaiiPrefix = _SvcPwSpeSaiiTaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 116, 1, 2),
    _SvcPwSpeSaiiTaiiPrefix_Type()
)
svcPwSpeSaiiTaiiPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeSaiiTaiiPrefix.setStatus("current")
_SvcPwSpeSaiiTaiiAcId_Type = Unsigned32
_SvcPwSpeSaiiTaiiAcId_Object = MibTableColumn
svcPwSpeSaiiTaiiAcId = _SvcPwSpeSaiiTaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 116, 1, 3),
    _SvcPwSpeSaiiTaiiAcId_Type()
)
svcPwSpeSaiiTaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeSaiiTaiiAcId.setStatus("current")
_SvcPwSpeSaiiSvcId_Type = TmnxServId
_SvcPwSpeSaiiSvcId_Object = MibTableColumn
svcPwSpeSaiiSvcId = _SvcPwSpeSaiiSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 116, 1, 4),
    _SvcPwSpeSaiiSvcId_Type()
)
svcPwSpeSaiiSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeSaiiSvcId.setStatus("current")
_SvcPwSpeSaiiOperSdpBind1_Type = SdpBindId
_SvcPwSpeSaiiOperSdpBind1_Object = MibTableColumn
svcPwSpeSaiiOperSdpBind1 = _SvcPwSpeSaiiOperSdpBind1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 116, 1, 5),
    _SvcPwSpeSaiiOperSdpBind1_Type()
)
svcPwSpeSaiiOperSdpBind1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeSaiiOperSdpBind1.setStatus("current")
_SvcPwSpeSaiiOperSdpBind2_Type = SdpBindId
_SvcPwSpeSaiiOperSdpBind2_Object = MibTableColumn
svcPwSpeSaiiOperSdpBind2 = _SvcPwSpeSaiiOperSdpBind2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 116, 1, 6),
    _SvcPwSpeSaiiOperSdpBind2_Type()
)
svcPwSpeSaiiOperSdpBind2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeSaiiOperSdpBind2.setStatus("current")
_SvcPwSpeTaiiTable_Object = MibTable
svcPwSpeTaiiTable = _SvcPwSpeTaiiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 117)
)
if mibBuilder.loadTexts:
    svcPwSpeTaiiTable.setStatus("current")
_SvcPwSpeTaiiEntry_Object = MibTableRow
svcPwSpeTaiiEntry = _SvcPwSpeTaiiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 117, 1)
)
svcPwSpeTaiiEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcMSPwPeTaiiGlobalId"),
    (0, "TIMETRA-SERV-MIB", "svcMSPwPeTaiiPrefix"),
    (0, "TIMETRA-SERV-MIB", "svcMSPwPeTaiiAcId"),
)
if mibBuilder.loadTexts:
    svcPwSpeTaiiEntry.setStatus("current")
_SvcPwSpeTaiiSaiiGlobalId_Type = TmnxPwGlobalIdOrZero
_SvcPwSpeTaiiSaiiGlobalId_Object = MibTableColumn
svcPwSpeTaiiSaiiGlobalId = _SvcPwSpeTaiiSaiiGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 117, 1, 1),
    _SvcPwSpeTaiiSaiiGlobalId_Type()
)
svcPwSpeTaiiSaiiGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeTaiiSaiiGlobalId.setStatus("current")
_SvcPwSpeTaiiSaiiPrefix_Type = Unsigned32
_SvcPwSpeTaiiSaiiPrefix_Object = MibTableColumn
svcPwSpeTaiiSaiiPrefix = _SvcPwSpeTaiiSaiiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 117, 1, 2),
    _SvcPwSpeTaiiSaiiPrefix_Type()
)
svcPwSpeTaiiSaiiPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeTaiiSaiiPrefix.setStatus("current")
_SvcPwSpeTaiiSaiiAcId_Type = Unsigned32
_SvcPwSpeTaiiSaiiAcId_Object = MibTableColumn
svcPwSpeTaiiSaiiAcId = _SvcPwSpeTaiiSaiiAcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 117, 1, 3),
    _SvcPwSpeTaiiSaiiAcId_Type()
)
svcPwSpeTaiiSaiiAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeTaiiSaiiAcId.setStatus("current")
_SvcPwSpeTaiiSvcId_Type = TmnxServId
_SvcPwSpeTaiiSvcId_Object = MibTableColumn
svcPwSpeTaiiSvcId = _SvcPwSpeTaiiSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 117, 1, 4),
    _SvcPwSpeTaiiSvcId_Type()
)
svcPwSpeTaiiSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeTaiiSvcId.setStatus("current")
_SvcPwSpeTaiiOperSdpBind1_Type = SdpBindId
_SvcPwSpeTaiiOperSdpBind1_Object = MibTableColumn
svcPwSpeTaiiOperSdpBind1 = _SvcPwSpeTaiiOperSdpBind1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 117, 1, 5),
    _SvcPwSpeTaiiOperSdpBind1_Type()
)
svcPwSpeTaiiOperSdpBind1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeTaiiOperSdpBind1.setStatus("current")
_SvcPwSpeTaiiOperSdpBind2_Type = SdpBindId
_SvcPwSpeTaiiOperSdpBind2_Object = MibTableColumn
svcPwSpeTaiiOperSdpBind2 = _SvcPwSpeTaiiOperSdpBind2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 117, 1, 6),
    _SvcPwSpeTaiiOperSdpBind2_Type()
)
svcPwSpeTaiiOperSdpBind2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcPwSpeTaiiOperSdpBind2.setStatus("current")
_SvcDhcpLeaseOvrTable_Object = MibTable
svcDhcpLeaseOvrTable = _SvcDhcpLeaseOvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrTable.setStatus("current")
_SvcDhcpLeaseOvrEntry_Object = MibTableRow
svcDhcpLeaseOvrEntry = _SvcDhcpLeaseOvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118, 1)
)
svcDhcpLeaseOvrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseCiAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseCiAddr"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseNextHopMacAddr"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseOvrDirection"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseOvrType"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseOvrTypeId"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseOvrTypeName"),
)
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrEntry.setStatus("current")


class _SvcDhcpLeaseOvrDirection_Type(TDirection):
    """Custom type svcDhcpLeaseOvrDirection based on TDirection"""
    subtypeSpec = TDirection.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_SvcDhcpLeaseOvrDirection_Type.__name__ = "TDirection"
_SvcDhcpLeaseOvrDirection_Object = MibTableColumn
svcDhcpLeaseOvrDirection = _SvcDhcpLeaseOvrDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118, 1, 1),
    _SvcDhcpLeaseOvrDirection_Type()
)
svcDhcpLeaseOvrDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrDirection.setStatus("current")
_SvcDhcpLeaseOvrType_Type = TQosOverrideType
_SvcDhcpLeaseOvrType_Object = MibTableColumn
svcDhcpLeaseOvrType = _SvcDhcpLeaseOvrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118, 1, 2),
    _SvcDhcpLeaseOvrType_Type()
)
svcDhcpLeaseOvrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrType.setStatus("current")
_SvcDhcpLeaseOvrTypeId_Type = Integer32
_SvcDhcpLeaseOvrTypeId_Object = MibTableColumn
svcDhcpLeaseOvrTypeId = _SvcDhcpLeaseOvrTypeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118, 1, 3),
    _SvcDhcpLeaseOvrTypeId_Type()
)
svcDhcpLeaseOvrTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrTypeId.setStatus("current")
_SvcDhcpLeaseOvrTypeName_Type = TNamedItemOrEmpty
_SvcDhcpLeaseOvrTypeName_Object = MibTableColumn
svcDhcpLeaseOvrTypeName = _SvcDhcpLeaseOvrTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118, 1, 4),
    _SvcDhcpLeaseOvrTypeName_Type()
)
svcDhcpLeaseOvrTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrTypeName.setStatus("current")
_SvcDhcpLeaseOvrPIR_Type = TPIRRateOverride
_SvcDhcpLeaseOvrPIR_Object = MibTableColumn
svcDhcpLeaseOvrPIR = _SvcDhcpLeaseOvrPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118, 1, 5),
    _SvcDhcpLeaseOvrPIR_Type()
)
svcDhcpLeaseOvrPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrPIR.setStatus("current")
_SvcDhcpLeaseOvrCIR_Type = TCIRRateOverride
_SvcDhcpLeaseOvrCIR_Object = MibTableColumn
svcDhcpLeaseOvrCIR = _SvcDhcpLeaseOvrCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118, 1, 6),
    _SvcDhcpLeaseOvrCIR_Type()
)
svcDhcpLeaseOvrCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrCIR.setStatus("current")
_SvcDhcpLeaseOvrCBS_Type = TBurstSizeBytesOverride
_SvcDhcpLeaseOvrCBS_Object = MibTableColumn
svcDhcpLeaseOvrCBS = _SvcDhcpLeaseOvrCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118, 1, 7),
    _SvcDhcpLeaseOvrCBS_Type()
)
svcDhcpLeaseOvrCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrCBS.setStatus("current")
_SvcDhcpLeaseOvrMBS_Type = TBurstSizeBytesOverride
_SvcDhcpLeaseOvrMBS_Object = MibTableColumn
svcDhcpLeaseOvrMBS = _SvcDhcpLeaseOvrMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118, 1, 8),
    _SvcDhcpLeaseOvrMBS_Type()
)
svcDhcpLeaseOvrMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrMBS.setStatus("current")
_SvcDhcpLeaseOvrWrrWeight_Type = THsmdaWrrWeightOverride
_SvcDhcpLeaseOvrWrrWeight_Object = MibTableColumn
svcDhcpLeaseOvrWrrWeight = _SvcDhcpLeaseOvrWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 118, 1, 9),
    _SvcDhcpLeaseOvrWrrWeight_Type()
)
svcDhcpLeaseOvrWrrWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseOvrWrrWeight.setStatus("current")
_SvcTlsSpbTableLastChanged_Type = TimeStamp
_SvcTlsSpbTableLastChanged_Object = MibScalar
svcTlsSpbTableLastChanged = _SvcTlsSpbTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 119),
    _SvcTlsSpbTableLastChanged_Type()
)
svcTlsSpbTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSpbTableLastChanged.setStatus("current")
_SvcTlsSpbTable_Object = MibTable
svcTlsSpbTable = _SvcTlsSpbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120)
)
if mibBuilder.loadTexts:
    svcTlsSpbTable.setStatus("current")
_SvcTlsSpbEntry_Object = MibTableRow
svcTlsSpbEntry = _SvcTlsSpbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1)
)
svcTlsSpbEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcTlsSpbEntry.setStatus("current")
_SvcTlsSpbRowStatus_Type = RowStatus
_SvcTlsSpbRowStatus_Object = MibTableColumn
svcTlsSpbRowStatus = _SvcTlsSpbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1, 1),
    _SvcTlsSpbRowStatus_Type()
)
svcTlsSpbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSpbRowStatus.setStatus("current")
_SvcTlsSpbLastChanged_Type = TimeStamp
_SvcTlsSpbLastChanged_Object = MibTableColumn
svcTlsSpbLastChanged = _SvcTlsSpbLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1, 2),
    _SvcTlsSpbLastChanged_Type()
)
svcTlsSpbLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSpbLastChanged.setStatus("current")


class _SvcTlsSpbIsisInstance_Type(Integer32):
    """Custom type svcTlsSpbIsisInstance based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 2047),
    )


_SvcTlsSpbIsisInstance_Type.__name__ = "Integer32"
_SvcTlsSpbIsisInstance_Object = MibTableColumn
svcTlsSpbIsisInstance = _SvcTlsSpbIsisInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1, 3),
    _SvcTlsSpbIsisInstance_Type()
)
svcTlsSpbIsisInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSpbIsisInstance.setStatus("current")


class _SvcTlsSpbFid_Type(TmnxSpbFid):
    """Custom type svcTlsSpbFid based on TmnxSpbFid"""
    defaultValue = 1


_SvcTlsSpbFid_Object = MibTableColumn
svcTlsSpbFid = _SvcTlsSpbFid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1, 4),
    _SvcTlsSpbFid_Type()
)
svcTlsSpbFid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSpbFid.setStatus("current")


class _SvcTlsSpbL1BridgePriority_Type(TmnxSpbBridgePriority):
    """Custom type svcTlsSpbL1BridgePriority based on TmnxSpbBridgePriority"""
    defaultValue = 8


_SvcTlsSpbL1BridgePriority_Object = MibTableColumn
svcTlsSpbL1BridgePriority = _SvcTlsSpbL1BridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1, 5),
    _SvcTlsSpbL1BridgePriority_Type()
)
svcTlsSpbL1BridgePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSpbL1BridgePriority.setStatus("current")


class _SvcTlsSpbL1FwdTreeTopoUcast_Type(Integer32):
    """Custom type svcTlsSpbL1FwdTreeTopoUcast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("spf", 0),
          ("st", 1))
    )


_SvcTlsSpbL1FwdTreeTopoUcast_Type.__name__ = "Integer32"
_SvcTlsSpbL1FwdTreeTopoUcast_Object = MibTableColumn
svcTlsSpbL1FwdTreeTopoUcast = _SvcTlsSpbL1FwdTreeTopoUcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1, 6),
    _SvcTlsSpbL1FwdTreeTopoUcast_Type()
)
svcTlsSpbL1FwdTreeTopoUcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSpbL1FwdTreeTopoUcast.setStatus("current")


class _SvcTlsSpbAdminState_Type(TmnxAdminState):
    """Custom type svcTlsSpbAdminState based on TmnxAdminState"""


_SvcTlsSpbAdminState_Object = MibTableColumn
svcTlsSpbAdminState = _SvcTlsSpbAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1, 7),
    _SvcTlsSpbAdminState_Type()
)
svcTlsSpbAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsSpbAdminState.setStatus("current")


class _SvcTlsSpbL1FwdTreeTopoMcast_Type(Integer32):
    """Custom type svcTlsSpbL1FwdTreeTopoMcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("spf", 0),
          ("st", 1))
    )


_SvcTlsSpbL1FwdTreeTopoMcast_Type.__name__ = "Integer32"
_SvcTlsSpbL1FwdTreeTopoMcast_Object = MibTableColumn
svcTlsSpbL1FwdTreeTopoMcast = _SvcTlsSpbL1FwdTreeTopoMcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1, 8),
    _SvcTlsSpbL1FwdTreeTopoMcast_Type()
)
svcTlsSpbL1FwdTreeTopoMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSpbL1FwdTreeTopoMcast.setStatus("current")
_SvcTlsSpbL1BridgeId_Type = BridgeId
_SvcTlsSpbL1BridgeId_Object = MibTableColumn
svcTlsSpbL1BridgeId = _SvcTlsSpbL1BridgeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1, 9),
    _SvcTlsSpbL1BridgeId_Type()
)
svcTlsSpbL1BridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSpbL1BridgeId.setStatus("current")
_SvcTlsSpbL1McastDesigBridgeId_Type = BridgeId
_SvcTlsSpbL1McastDesigBridgeId_Object = MibTableColumn
svcTlsSpbL1McastDesigBridgeId = _SvcTlsSpbL1McastDesigBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 120, 1, 10),
    _SvcTlsSpbL1McastDesigBridgeId_Type()
)
svcTlsSpbL1McastDesigBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSpbL1McastDesigBridgeId.setStatus("current")
_SvcVllBgpTableLastChanged_Type = TimeStamp
_SvcVllBgpTableLastChanged_Object = MibScalar
svcVllBgpTableLastChanged = _SvcVllBgpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 121),
    _SvcVllBgpTableLastChanged_Type()
)
svcVllBgpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllBgpTableLastChanged.setStatus("current")
_SvcVllBgpTable_Object = MibTable
svcVllBgpTable = _SvcVllBgpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 122)
)
if mibBuilder.loadTexts:
    svcVllBgpTable.setStatus("current")
_SvcVllBgpEntry_Object = MibTableRow
svcVllBgpEntry = _SvcVllBgpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 122, 1)
)
svcVllBgpEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcVllBgpEntry.setStatus("current")
_SvcVllBgpRowStatus_Type = RowStatus
_SvcVllBgpRowStatus_Object = MibTableColumn
svcVllBgpRowStatus = _SvcVllBgpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 122, 1, 1),
    _SvcVllBgpRowStatus_Type()
)
svcVllBgpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllBgpRowStatus.setStatus("current")
_SvcVllBgpLastChanged_Type = TimeStamp
_SvcVllBgpLastChanged_Object = MibTableColumn
svcVllBgpLastChanged = _SvcVllBgpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 122, 1, 2),
    _SvcVllBgpLastChanged_Type()
)
svcVllBgpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllBgpLastChanged.setStatus("current")


class _SvcVllBgpVsiRD_Type(TmnxVPNRouteDistinguisher):
    """Custom type svcVllBgpVsiRD based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_SvcVllBgpVsiRD_Object = MibTableColumn
svcVllBgpVsiRD = _SvcVllBgpVsiRD_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 122, 1, 3),
    _SvcVllBgpVsiRD_Type()
)
svcVllBgpVsiRD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllBgpVsiRD.setStatus("current")
_SvcVllBgpExportRteTarget_Type = TNamedItemOrEmpty
_SvcVllBgpExportRteTarget_Object = MibTableColumn
svcVllBgpExportRteTarget = _SvcVllBgpExportRteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 122, 1, 4),
    _SvcVllBgpExportRteTarget_Type()
)
svcVllBgpExportRteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllBgpExportRteTarget.setStatus("current")
_SvcVllBgpImportRteTarget_Type = TNamedItemOrEmpty
_SvcVllBgpImportRteTarget_Object = MibTableColumn
svcVllBgpImportRteTarget = _SvcVllBgpImportRteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 122, 1, 5),
    _SvcVllBgpImportRteTarget_Type()
)
svcVllBgpImportRteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllBgpImportRteTarget.setStatus("current")
_SvcVllSiteIdTblLastChanged_Type = TimeStamp
_SvcVllSiteIdTblLastChanged_Object = MibScalar
svcVllSiteIdTblLastChanged = _SvcVllSiteIdTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 123),
    _SvcVllSiteIdTblLastChanged_Type()
)
svcVllSiteIdTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllSiteIdTblLastChanged.setStatus("current")
_SvcVllSiteIdTable_Object = MibTable
svcVllSiteIdTable = _SvcVllSiteIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124)
)
if mibBuilder.loadTexts:
    svcVllSiteIdTable.setStatus("current")
_SvcVllSiteIdEntry_Object = MibTableRow
svcVllSiteIdEntry = _SvcVllSiteIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1)
)
svcVllSiteIdEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcVllSiteIdName"),
)
if mibBuilder.loadTexts:
    svcVllSiteIdEntry.setStatus("current")
_SvcVllSiteIdName_Type = TNamedItem
_SvcVllSiteIdName_Object = MibTableColumn
svcVllSiteIdName = _SvcVllSiteIdName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 1),
    _SvcVllSiteIdName_Type()
)
svcVllSiteIdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcVllSiteIdName.setStatus("current")
_SvcVllSiteIdRowStatus_Type = RowStatus
_SvcVllSiteIdRowStatus_Object = MibTableColumn
svcVllSiteIdRowStatus = _SvcVllSiteIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 2),
    _SvcVllSiteIdRowStatus_Type()
)
svcVllSiteIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllSiteIdRowStatus.setStatus("current")
_SvcVllSiteIdLastChanged_Type = TimeStamp
_SvcVllSiteIdLastChanged_Object = MibTableColumn
svcVllSiteIdLastChanged = _SvcVllSiteIdLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 3),
    _SvcVllSiteIdLastChanged_Type()
)
svcVllSiteIdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllSiteIdLastChanged.setStatus("current")


class _SvcVllSiteIdAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type svcVllSiteIdAdminStatus based on TmnxEnabledDisabled"""


_SvcVllSiteIdAdminStatus_Object = MibTableColumn
svcVllSiteIdAdminStatus = _SvcVllSiteIdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 4),
    _SvcVllSiteIdAdminStatus_Type()
)
svcVllSiteIdAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllSiteIdAdminStatus.setStatus("current")


class _SvcVllSiteIdSiteId_Type(TmnxSiteId):
    """Custom type svcVllSiteIdSiteId based on TmnxSiteId"""
    defaultValue = -1


_SvcVllSiteIdSiteId_Object = MibTableColumn
svcVllSiteIdSiteId = _SvcVllSiteIdSiteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 5),
    _SvcVllSiteIdSiteId_Type()
)
svcVllSiteIdSiteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllSiteIdSiteId.setStatus("current")


class _SvcVllSiteIdPortId_Type(TmnxPortID):
    """Custom type svcVllSiteIdPortId based on TmnxPortID"""
    defaultHexValue = 503316480


_SvcVllSiteIdPortId_Object = MibTableColumn
svcVllSiteIdPortId = _SvcVllSiteIdPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 6),
    _SvcVllSiteIdPortId_Type()
)
svcVllSiteIdPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllSiteIdPortId.setStatus("current")


class _SvcVllSiteIdEncapValue_Type(TmnxEncapVal):
    """Custom type svcVllSiteIdEncapValue based on TmnxEncapVal"""
    defaultValue = 0


_SvcVllSiteIdEncapValue_Object = MibTableColumn
svcVllSiteIdEncapValue = _SvcVllSiteIdEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 7),
    _SvcVllSiteIdEncapValue_Type()
)
svcVllSiteIdEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllSiteIdEncapValue.setStatus("current")
_SvcVllSiteIdOperStatus_Type = TSiteOperStatus
_SvcVllSiteIdOperStatus_Object = MibTableColumn
svcVllSiteIdOperStatus = _SvcVllSiteIdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 8),
    _SvcVllSiteIdOperStatus_Type()
)
svcVllSiteIdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllSiteIdOperStatus.setStatus("current")
_SvcVllSiteIdDesignatedFwdr_Type = TruthValue
_SvcVllSiteIdDesignatedFwdr_Object = MibTableColumn
svcVllSiteIdDesignatedFwdr = _SvcVllSiteIdDesignatedFwdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 9),
    _SvcVllSiteIdDesignatedFwdr_Type()
)
svcVllSiteIdDesignatedFwdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllSiteIdDesignatedFwdr.setStatus("current")


class _SvcVllSiteIdBootTimer_Type(Integer32):
    """Custom type svcVllSiteIdBootTimer based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 600),
    )


_SvcVllSiteIdBootTimer_Type.__name__ = "Integer32"
_SvcVllSiteIdBootTimer_Object = MibTableColumn
svcVllSiteIdBootTimer = _SvcVllSiteIdBootTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 10),
    _SvcVllSiteIdBootTimer_Type()
)
svcVllSiteIdBootTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllSiteIdBootTimer.setStatus("current")
if mibBuilder.loadTexts:
    svcVllSiteIdBootTimer.setUnits("seconds")


class _SvcVllSiteIdSiteActTimer_Type(Integer32):
    """Custom type svcVllSiteIdSiteActTimer based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_SvcVllSiteIdSiteActTimer_Type.__name__ = "Integer32"
_SvcVllSiteIdSiteActTimer_Object = MibTableColumn
svcVllSiteIdSiteActTimer = _SvcVllSiteIdSiteActTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 11),
    _SvcVllSiteIdSiteActTimer_Type()
)
svcVllSiteIdSiteActTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcVllSiteIdSiteActTimer.setStatus("current")
if mibBuilder.loadTexts:
    svcVllSiteIdSiteActTimer.setUnits("seconds")
_SvcVllSiteIdDfUpTime_Type = Unsigned32
_SvcVllSiteIdDfUpTime_Object = MibTableColumn
svcVllSiteIdDfUpTime = _SvcVllSiteIdDfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 12),
    _SvcVllSiteIdDfUpTime_Type()
)
svcVllSiteIdDfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllSiteIdDfUpTime.setStatus("current")
if mibBuilder.loadTexts:
    svcVllSiteIdDfUpTime.setUnits("seconds")
_SvcVllSiteIdDfChgCnt_Type = Unsigned32
_SvcVllSiteIdDfChgCnt_Object = MibTableColumn
svcVllSiteIdDfChgCnt = _SvcVllSiteIdDfChgCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 13),
    _SvcVllSiteIdDfChgCnt_Type()
)
svcVllSiteIdDfChgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllSiteIdDfChgCnt.setStatus("current")
_SvcVllSiteIdTimerRemain_Type = Unsigned32
_SvcVllSiteIdTimerRemain_Object = MibTableColumn
svcVllSiteIdTimerRemain = _SvcVllSiteIdTimerRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 124, 1, 14),
    _SvcVllSiteIdTimerRemain_Type()
)
svcVllSiteIdTimerRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcVllSiteIdTimerRemain.setStatus("current")
if mibBuilder.loadTexts:
    svcVllSiteIdTimerRemain.setUnits("seconds")
_SvcTlsPmsiTableLastChanged_Type = TimeStamp
_SvcTlsPmsiTableLastChanged_Object = MibScalar
svcTlsPmsiTableLastChanged = _SvcTlsPmsiTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 125),
    _SvcTlsPmsiTableLastChanged_Type()
)
svcTlsPmsiTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsPmsiTableLastChanged.setStatus("current")
_SvcTlsPmsiTable_Object = MibTable
svcTlsPmsiTable = _SvcTlsPmsiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126)
)
if mibBuilder.loadTexts:
    svcTlsPmsiTable.setStatus("current")
_SvcTlsPmsiEntry_Object = MibTableRow
svcTlsPmsiEntry = _SvcTlsPmsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126, 1)
)
svcTlsPmsiEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    svcTlsPmsiEntry.setStatus("current")
_SvcTlsPmsiRowStatus_Type = RowStatus
_SvcTlsPmsiRowStatus_Object = MibTableColumn
svcTlsPmsiRowStatus = _SvcTlsPmsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126, 1, 1),
    _SvcTlsPmsiRowStatus_Type()
)
svcTlsPmsiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsPmsiRowStatus.setStatus("current")
_SvcTlsPmsiLastChanged_Type = TimeStamp
_SvcTlsPmsiLastChanged_Object = MibTableColumn
svcTlsPmsiLastChanged = _SvcTlsPmsiLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126, 1, 2),
    _SvcTlsPmsiLastChanged_Type()
)
svcTlsPmsiLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsPmsiLastChanged.setStatus("current")


class _SvcTlsIPmsiAdminState_Type(TmnxAdminState):
    """Custom type svcTlsIPmsiAdminState based on TmnxAdminState"""


_SvcTlsIPmsiAdminState_Object = MibTableColumn
svcTlsIPmsiAdminState = _SvcTlsIPmsiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126, 1, 3),
    _SvcTlsIPmsiAdminState_Type()
)
svcTlsIPmsiAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsIPmsiAdminState.setStatus("current")


class _SvcTlsIPmsiDataDelayIntvl_Type(Integer32):
    """Custom type svcTlsIPmsiDataDelayIntvl based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 180),
    )


_SvcTlsIPmsiDataDelayIntvl_Type.__name__ = "Integer32"
_SvcTlsIPmsiDataDelayIntvl_Object = MibTableColumn
svcTlsIPmsiDataDelayIntvl = _SvcTlsIPmsiDataDelayIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126, 1, 4),
    _SvcTlsIPmsiDataDelayIntvl_Type()
)
svcTlsIPmsiDataDelayIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsIPmsiDataDelayIntvl.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsIPmsiDataDelayIntvl.setUnits("seconds")


class _SvcTlsIPmsiType_Type(Integer32):
    """Custom type svcTlsIPmsiType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rsvp", 1))
    )


_SvcTlsIPmsiType_Type.__name__ = "Integer32"
_SvcTlsIPmsiType_Object = MibTableColumn
svcTlsIPmsiType = _SvcTlsIPmsiType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126, 1, 5),
    _SvcTlsIPmsiType_Type()
)
svcTlsIPmsiType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsIPmsiType.setStatus("current")


class _SvcTlsIPmsiLspTmpl_Type(TNamedItemOrEmpty):
    """Custom type svcTlsIPmsiLspTmpl based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SvcTlsIPmsiLspTmpl_Object = MibTableColumn
svcTlsIPmsiLspTmpl = _SvcTlsIPmsiLspTmpl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126, 1, 6),
    _SvcTlsIPmsiLspTmpl_Type()
)
svcTlsIPmsiLspTmpl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsIPmsiLspTmpl.setStatus("current")


class _SvcTlsIPmsiRootAndLeaf_Type(TruthValue):
    """Custom type svcTlsIPmsiRootAndLeaf based on TruthValue"""


_SvcTlsIPmsiRootAndLeaf_Object = MibTableColumn
svcTlsIPmsiRootAndLeaf = _SvcTlsIPmsiRootAndLeaf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126, 1, 7),
    _SvcTlsIPmsiRootAndLeaf_Type()
)
svcTlsIPmsiRootAndLeaf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsIPmsiRootAndLeaf.setStatus("current")
_SvcTlsIPmsiRemainDataDelayIntvl_Type = Integer32
_SvcTlsIPmsiRemainDataDelayIntvl_Object = MibTableColumn
svcTlsIPmsiRemainDataDelayIntvl = _SvcTlsIPmsiRemainDataDelayIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126, 1, 8),
    _SvcTlsIPmsiRemainDataDelayIntvl_Type()
)
svcTlsIPmsiRemainDataDelayIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsIPmsiRemainDataDelayIntvl.setStatus("current")
if mibBuilder.loadTexts:
    svcTlsIPmsiRemainDataDelayIntvl.setUnits("seconds")
_SvcTlsIPmsiLspName_Type = TNamedItemOrEmpty
_SvcTlsIPmsiLspName_Object = MibTableColumn
svcTlsIPmsiLspName = _SvcTlsIPmsiLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 126, 1, 9),
    _SvcTlsIPmsiLspName_Type()
)
svcTlsIPmsiLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsIPmsiLspName.setStatus("current")
_SvcDhcpLeaseWppTable_Object = MibTable
svcDhcpLeaseWppTable = _SvcDhcpLeaseWppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 127)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseWppTable.setStatus("current")
_SvcDhcpLeaseWppEntry_Object = MibTableRow
svcDhcpLeaseWppEntry = _SvcDhcpLeaseWppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 127, 1)
)
svcDhcpLeaseWppEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseCiAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseCiAddr"),
    (0, "TIMETRA-SERV-MIB", "svcDhcpLeaseNextHopMacAddr"),
)
if mibBuilder.loadTexts:
    svcDhcpLeaseWppEntry.setStatus("current")


class _SvcDhcpLeaseWppState_Type(Integer32):
    """Custom type svcDhcpLeaseWppState based on Integer32"""
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
        *(("authenticated", 5),
          ("authenticating", 4),
          ("initial", 1),
          ("registered", 3),
          ("registering", 2))
    )


_SvcDhcpLeaseWppState_Type.__name__ = "Integer32"
_SvcDhcpLeaseWppState_Object = MibTableColumn
svcDhcpLeaseWppState = _SvcDhcpLeaseWppState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 127, 1, 1),
    _SvcDhcpLeaseWppState_Type()
)
svcDhcpLeaseWppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseWppState.setStatus("current")
_SvcDhcpLeaseWppPortalRouter_Type = TmnxVRtrIDOrZero
_SvcDhcpLeaseWppPortalRouter_Object = MibTableColumn
svcDhcpLeaseWppPortalRouter = _SvcDhcpLeaseWppPortalRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 127, 1, 2),
    _SvcDhcpLeaseWppPortalRouter_Type()
)
svcDhcpLeaseWppPortalRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseWppPortalRouter.setStatus("current")
_SvcDhcpLeaseWppPortalName_Type = TNamedItemOrEmpty
_SvcDhcpLeaseWppPortalName_Object = MibTableColumn
svcDhcpLeaseWppPortalName = _SvcDhcpLeaseWppPortalName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 127, 1, 3),
    _SvcDhcpLeaseWppPortalName_Type()
)
svcDhcpLeaseWppPortalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLeaseWppPortalName.setStatus("current")
_SvcIfSapCfgTableLastChanged_Type = TimeStamp
_SvcIfSapCfgTableLastChanged_Object = MibScalar
svcIfSapCfgTableLastChanged = _SvcIfSapCfgTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 128),
    _SvcIfSapCfgTableLastChanged_Type()
)
svcIfSapCfgTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIfSapCfgTableLastChanged.setStatus("current")
_SvcIfSapCfgTable_Object = MibTable
svcIfSapCfgTable = _SvcIfSapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129)
)
if mibBuilder.loadTexts:
    svcIfSapCfgTable.setStatus("current")
_SvcIfSapCfgEntry_Object = MibTableRow
svcIfSapCfgEntry = _SvcIfSapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129, 1)
)
svcIfSapCfgEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    svcIfSapCfgEntry.setStatus("current")
_SvcIfSapCfgLastMgmtChange_Type = TimeStamp
_SvcIfSapCfgLastMgmtChange_Object = MibTableColumn
svcIfSapCfgLastMgmtChange = _SvcIfSapCfgLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129, 1, 1),
    _SvcIfSapCfgLastMgmtChange_Type()
)
svcIfSapCfgLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIfSapCfgLastMgmtChange.setStatus("current")
_SvcIfSapCfgDescription_Type = TItemDescription
_SvcIfSapCfgDescription_Object = MibTableColumn
svcIfSapCfgDescription = _SvcIfSapCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129, 1, 2),
    _SvcIfSapCfgDescription_Type()
)
svcIfSapCfgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcIfSapCfgDescription.setStatus("current")
_SvcIfSapCfgDefSubProfile_Type = TNamedItemOrEmpty
_SvcIfSapCfgDefSubProfile_Object = MibTableColumn
svcIfSapCfgDefSubProfile = _SvcIfSapCfgDefSubProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129, 1, 3),
    _SvcIfSapCfgDefSubProfile_Type()
)
svcIfSapCfgDefSubProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcIfSapCfgDefSubProfile.setStatus("current")
_SvcIfSapCfgDefSlaProfile_Type = TNamedItemOrEmpty
_SvcIfSapCfgDefSlaProfile_Object = MibTableColumn
svcIfSapCfgDefSlaProfile = _SvcIfSapCfgDefSlaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129, 1, 4),
    _SvcIfSapCfgDefSlaProfile_Type()
)
svcIfSapCfgDefSlaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcIfSapCfgDefSlaProfile.setStatus("current")
_SvcIfSapCfgDefAppProfile_Type = TNamedItemOrEmpty
_SvcIfSapCfgDefAppProfile_Object = MibTableColumn
svcIfSapCfgDefAppProfile = _SvcIfSapCfgDefAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129, 1, 5),
    _SvcIfSapCfgDefAppProfile_Type()
)
svcIfSapCfgDefAppProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcIfSapCfgDefAppProfile.setStatus("current")
_SvcIfSapCfgSubIdentPolicy_Type = TNamedItemOrEmpty
_SvcIfSapCfgSubIdentPolicy_Object = MibTableColumn
svcIfSapCfgSubIdentPolicy = _SvcIfSapCfgSubIdentPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129, 1, 6),
    _SvcIfSapCfgSubIdentPolicy_Type()
)
svcIfSapCfgSubIdentPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcIfSapCfgSubIdentPolicy.setStatus("current")


class _SvcIfSapCfgDefSubIdent_Type(TmnxDefSubIdSource):
    """Custom type svcIfSapCfgDefSubIdent based on TmnxDefSubIdSource"""


_SvcIfSapCfgDefSubIdent_Object = MibTableColumn
svcIfSapCfgDefSubIdent = _SvcIfSapCfgDefSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129, 1, 7),
    _SvcIfSapCfgDefSubIdent_Type()
)
svcIfSapCfgDefSubIdent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcIfSapCfgDefSubIdent.setStatus("current")


class _SvcIfSapCfgDefSubIdentString_Type(DisplayString):
    """Custom type svcIfSapCfgDefSubIdentString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SvcIfSapCfgDefSubIdentString_Type.__name__ = "DisplayString"
_SvcIfSapCfgDefSubIdentString_Object = MibTableColumn
svcIfSapCfgDefSubIdentString = _SvcIfSapCfgDefSubIdentString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129, 1, 8),
    _SvcIfSapCfgDefSubIdentString_Type()
)
svcIfSapCfgDefSubIdentString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcIfSapCfgDefSubIdentString.setStatus("current")
_SvcIfSapCfgDefFilterProfile_Type = TNamedItemOrEmpty
_SvcIfSapCfgDefFilterProfile_Object = MibTableColumn
svcIfSapCfgDefFilterProfile = _SvcIfSapCfgDefFilterProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 129, 1, 9),
    _SvcIfSapCfgDefFilterProfile_Type()
)
svcIfSapCfgDefFilterProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcIfSapCfgDefFilterProfile.setStatus("current")
_SvcTlsSpbUserSvcTable_Object = MibTable
svcTlsSpbUserSvcTable = _SvcTlsSpbUserSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 130)
)
if mibBuilder.loadTexts:
    svcTlsSpbUserSvcTable.setStatus("current")
_SvcTlsSpbUserSvcEntry_Object = MibTableRow
svcTlsSpbUserSvcEntry = _SvcTlsSpbUserSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 130, 1)
)
svcTlsSpbUserSvcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcTlsSpbFid"),
    (0, "TIMETRA-SERV-MIB", "svcTlsSpbUserSvcId"),
)
if mibBuilder.loadTexts:
    svcTlsSpbUserSvcEntry.setStatus("current")
_SvcTlsSpbUserSvcId_Type = TmnxServId
_SvcTlsSpbUserSvcId_Object = MibTableColumn
svcTlsSpbUserSvcId = _SvcTlsSpbUserSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 130, 1, 1),
    _SvcTlsSpbUserSvcId_Type()
)
svcTlsSpbUserSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcTlsSpbUserSvcId.setStatus("current")
_SvcTlsSpbUserSvcLastUpdate_Type = TimeStamp
_SvcTlsSpbUserSvcLastUpdate_Object = MibTableColumn
svcTlsSpbUserSvcLastUpdate = _SvcTlsSpbUserSvcLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 130, 1, 2),
    _SvcTlsSpbUserSvcLastUpdate_Type()
)
svcTlsSpbUserSvcLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsSpbUserSvcLastUpdate.setStatus("current")
_TlsSpbFdbTable_Object = MibTable
tlsSpbFdbTable = _TlsSpbFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131)
)
if mibBuilder.loadTexts:
    tlsSpbFdbTable.setStatus("current")
_TlsSpbFdbEntry_Object = MibTableRow
tlsSpbFdbEntry = _TlsSpbFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1)
)
tlsSpbFdbEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsSpbFdbMacAddr"),
)
if mibBuilder.loadTexts:
    tlsSpbFdbEntry.setStatus("current")
_TlsSpbFdbMacAddr_Type = MacAddress
_TlsSpbFdbMacAddr_Object = MibTableColumn
tlsSpbFdbMacAddr = _TlsSpbFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 1),
    _TlsSpbFdbMacAddr_Type()
)
tlsSpbFdbMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsSpbFdbMacAddr.setStatus("current")
_TlsSpbFdbLocale_Type = TmnxSpbFdbLocale
_TlsSpbFdbLocale_Object = MibTableColumn
tlsSpbFdbLocale = _TlsSpbFdbLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 4),
    _TlsSpbFdbLocale_Type()
)
tlsSpbFdbLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbLocale.setStatus("current")
_TlsSpbFdbPortId_Type = TmnxPortID
_TlsSpbFdbPortId_Object = MibTableColumn
tlsSpbFdbPortId = _TlsSpbFdbPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 5),
    _TlsSpbFdbPortId_Type()
)
tlsSpbFdbPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbPortId.setStatus("current")
_TlsSpbFdbEncapValue_Type = TmnxEncapVal
_TlsSpbFdbEncapValue_Object = MibTableColumn
tlsSpbFdbEncapValue = _TlsSpbFdbEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 6),
    _TlsSpbFdbEncapValue_Type()
)
tlsSpbFdbEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbEncapValue.setStatus("current")
_TlsSpbFdbSdpId_Type = SdpId
_TlsSpbFdbSdpId_Object = MibTableColumn
tlsSpbFdbSdpId = _TlsSpbFdbSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 7),
    _TlsSpbFdbSdpId_Type()
)
tlsSpbFdbSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbSdpId.setStatus("current")
_TlsSpbFdbVcId_Type = Unsigned32
_TlsSpbFdbVcId_Object = MibTableColumn
tlsSpbFdbVcId = _TlsSpbFdbVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 8),
    _TlsSpbFdbVcId_Type()
)
tlsSpbFdbVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbVcId.setStatus("current")
_TlsSpbFdbState_Type = TmnxSpbFdbState
_TlsSpbFdbState_Object = MibTableColumn
tlsSpbFdbState = _TlsSpbFdbState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 9),
    _TlsSpbFdbState_Type()
)
tlsSpbFdbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbState.setStatus("current")
_TlsSpbFdbMLocale_Type = TmnxSpbFdbLocale
_TlsSpbFdbMLocale_Object = MibTableColumn
tlsSpbFdbMLocale = _TlsSpbFdbMLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 10),
    _TlsSpbFdbMLocale_Type()
)
tlsSpbFdbMLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbMLocale.setStatus("current")
_TlsSpbFdbMPortId_Type = TmnxPortID
_TlsSpbFdbMPortId_Object = MibTableColumn
tlsSpbFdbMPortId = _TlsSpbFdbMPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 11),
    _TlsSpbFdbMPortId_Type()
)
tlsSpbFdbMPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbMPortId.setStatus("current")
_TlsSpbFdbMEncapValue_Type = TmnxEncapVal
_TlsSpbFdbMEncapValue_Object = MibTableColumn
tlsSpbFdbMEncapValue = _TlsSpbFdbMEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 12),
    _TlsSpbFdbMEncapValue_Type()
)
tlsSpbFdbMEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbMEncapValue.setStatus("current")
_TlsSpbFdbMSdpId_Type = SdpId
_TlsSpbFdbMSdpId_Object = MibTableColumn
tlsSpbFdbMSdpId = _TlsSpbFdbMSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 13),
    _TlsSpbFdbMSdpId_Type()
)
tlsSpbFdbMSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbMSdpId.setStatus("current")
_TlsSpbFdbMVcId_Type = Unsigned32
_TlsSpbFdbMVcId_Object = MibTableColumn
tlsSpbFdbMVcId = _TlsSpbFdbMVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 14),
    _TlsSpbFdbMVcId_Type()
)
tlsSpbFdbMVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbMVcId.setStatus("current")
_TlsSpbFdbMState_Type = TmnxSpbFdbState
_TlsSpbFdbMState_Object = MibTableColumn
tlsSpbFdbMState = _TlsSpbFdbMState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 131, 1, 15),
    _TlsSpbFdbMState_Type()
)
tlsSpbFdbMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFdbMState.setStatus("current")
_TlsSpbFidFdbTable_Object = MibTable
tlsSpbFidFdbTable = _TlsSpbFidFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132)
)
if mibBuilder.loadTexts:
    tlsSpbFidFdbTable.setStatus("current")
_TlsSpbFidFdbEntry_Object = MibTableRow
tlsSpbFidFdbEntry = _TlsSpbFidFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1)
)
tlsSpbFidFdbEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcTlsSpbFid"),
    (0, "TIMETRA-SERV-MIB", "tlsSpbFidFdbMacAddr"),
)
if mibBuilder.loadTexts:
    tlsSpbFidFdbEntry.setStatus("current")
_TlsSpbFidFdbMacAddr_Type = MacAddress
_TlsSpbFidFdbMacAddr_Object = MibTableColumn
tlsSpbFidFdbMacAddr = _TlsSpbFidFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 1),
    _TlsSpbFidFdbMacAddr_Type()
)
tlsSpbFidFdbMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsSpbFidFdbMacAddr.setStatus("current")
_TlsSpbFidFdbLocale_Type = TmnxSpbFdbLocale
_TlsSpbFidFdbLocale_Object = MibTableColumn
tlsSpbFidFdbLocale = _TlsSpbFidFdbLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 4),
    _TlsSpbFidFdbLocale_Type()
)
tlsSpbFidFdbLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbLocale.setStatus("current")
_TlsSpbFidFdbPortId_Type = TmnxPortID
_TlsSpbFidFdbPortId_Object = MibTableColumn
tlsSpbFidFdbPortId = _TlsSpbFidFdbPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 5),
    _TlsSpbFidFdbPortId_Type()
)
tlsSpbFidFdbPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbPortId.setStatus("current")
_TlsSpbFidFdbEncapValue_Type = TmnxEncapVal
_TlsSpbFidFdbEncapValue_Object = MibTableColumn
tlsSpbFidFdbEncapValue = _TlsSpbFidFdbEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 6),
    _TlsSpbFidFdbEncapValue_Type()
)
tlsSpbFidFdbEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbEncapValue.setStatus("current")
_TlsSpbFidFdbSdpId_Type = SdpId
_TlsSpbFidFdbSdpId_Object = MibTableColumn
tlsSpbFidFdbSdpId = _TlsSpbFidFdbSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 7),
    _TlsSpbFidFdbSdpId_Type()
)
tlsSpbFidFdbSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbSdpId.setStatus("current")
_TlsSpbFidFdbVcId_Type = Unsigned32
_TlsSpbFidFdbVcId_Object = MibTableColumn
tlsSpbFidFdbVcId = _TlsSpbFidFdbVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 8),
    _TlsSpbFidFdbVcId_Type()
)
tlsSpbFidFdbVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbVcId.setStatus("current")
_TlsSpbFidFdbMLocale_Type = TmnxSpbFdbLocale
_TlsSpbFidFdbMLocale_Object = MibTableColumn
tlsSpbFidFdbMLocale = _TlsSpbFidFdbMLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 9),
    _TlsSpbFidFdbMLocale_Type()
)
tlsSpbFidFdbMLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbMLocale.setStatus("current")
_TlsSpbFidFdbMPortId_Type = TmnxPortID
_TlsSpbFidFdbMPortId_Object = MibTableColumn
tlsSpbFidFdbMPortId = _TlsSpbFidFdbMPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 10),
    _TlsSpbFidFdbMPortId_Type()
)
tlsSpbFidFdbMPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbMPortId.setStatus("current")
_TlsSpbFidFdbMEncapValue_Type = TmnxEncapVal
_TlsSpbFidFdbMEncapValue_Object = MibTableColumn
tlsSpbFidFdbMEncapValue = _TlsSpbFidFdbMEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 11),
    _TlsSpbFidFdbMEncapValue_Type()
)
tlsSpbFidFdbMEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbMEncapValue.setStatus("current")
_TlsSpbFidFdbMSdpId_Type = SdpId
_TlsSpbFidFdbMSdpId_Object = MibTableColumn
tlsSpbFidFdbMSdpId = _TlsSpbFidFdbMSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 12),
    _TlsSpbFidFdbMSdpId_Type()
)
tlsSpbFidFdbMSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbMSdpId.setStatus("current")
_TlsSpbFidFdbMVcId_Type = Unsigned32
_TlsSpbFidFdbMVcId_Object = MibTableColumn
tlsSpbFidFdbMVcId = _TlsSpbFidFdbMVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 13),
    _TlsSpbFidFdbMVcId_Type()
)
tlsSpbFidFdbMVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbMVcId.setStatus("current")
_TlsSpbFidFdbLastUpdate_Type = TimeStamp
_TlsSpbFidFdbLastUpdate_Object = MibTableColumn
tlsSpbFidFdbLastUpdate = _TlsSpbFidFdbLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 14),
    _TlsSpbFidFdbLastUpdate_Type()
)
tlsSpbFidFdbLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbLastUpdate.setStatus("current")
_TlsSpbFidFdbMLastUpdate_Type = TimeStamp
_TlsSpbFidFdbMLastUpdate_Object = MibTableColumn
tlsSpbFidFdbMLastUpdate = _TlsSpbFidFdbMLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 132, 1, 15),
    _TlsSpbFidFdbMLastUpdate_Type()
)
tlsSpbFidFdbMLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidFdbMLastUpdate.setStatus("current")
_TlsSpbMFibTable_Object = MibTable
tlsSpbMFibTable = _TlsSpbMFibTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 133)
)
if mibBuilder.loadTexts:
    tlsSpbMFibTable.setStatus("current")
_TlsSpbMFibEntry_Object = MibTableRow
tlsSpbMFibEntry = _TlsSpbMFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 133, 1)
)
tlsSpbMFibEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "tlsSpbMFibMacAddr"),
)
if mibBuilder.loadTexts:
    tlsSpbMFibEntry.setStatus("current")
_TlsSpbMFibMacAddr_Type = MacAddress
_TlsSpbMFibMacAddr_Object = MibTableColumn
tlsSpbMFibMacAddr = _TlsSpbMFibMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 133, 1, 1),
    _TlsSpbMFibMacAddr_Type()
)
tlsSpbMFibMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsSpbMFibMacAddr.setStatus("current")
_TlsSpbMFibIsid_Type = Unsigned32
_TlsSpbMFibIsid_Object = MibTableColumn
tlsSpbMFibIsid = _TlsSpbMFibIsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 133, 1, 2),
    _TlsSpbMFibIsid_Type()
)
tlsSpbMFibIsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbMFibIsid.setStatus("current")


class _TlsSpbMFibState_Type(Bits):
    """Custom type tlsSpbMFibState based on Bits"""
    namedValues = NamedValues(
        *(("addModPending", 1),
          ("delPending", 2),
          ("noFateShared", 4),
          ("ok", 0),
          ("spbMFibLimit", 5),
          ("sysMFibLimit", 3))
    )

_TlsSpbMFibState_Type.__name__ = "Bits"
_TlsSpbMFibState_Object = MibTableColumn
tlsSpbMFibState = _TlsSpbMFibState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 133, 1, 3),
    _TlsSpbMFibState_Type()
)
tlsSpbMFibState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbMFibState.setStatus("current")
_TlsSpbFidMFibTable_Object = MibTable
tlsSpbFidMFibTable = _TlsSpbFidMFibTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 134)
)
if mibBuilder.loadTexts:
    tlsSpbFidMFibTable.setStatus("current")
_TlsSpbFidMFibEntry_Object = MibTableRow
tlsSpbFidMFibEntry = _TlsSpbFidMFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 134, 1)
)
tlsSpbFidMFibEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcTlsSpbFid"),
    (0, "TIMETRA-SERV-MIB", "tlsSpbFidMFibMacAddr"),
    (0, "TIMETRA-SERV-MIB", "tlsSpbFidMFibLocale"),
    (0, "TIMETRA-SERV-MIB", "tlsSpbFidMFibPortId"),
    (0, "TIMETRA-SERV-MIB", "tlsSpbFidMFibEncapValue"),
    (0, "TIMETRA-SERV-MIB", "tlsSpbFidMFibSdpId"),
    (0, "TIMETRA-SERV-MIB", "tlsSpbFidMFibVcId"),
)
if mibBuilder.loadTexts:
    tlsSpbFidMFibEntry.setStatus("current")
_TlsSpbFidMFibMacAddr_Type = MacAddress
_TlsSpbFidMFibMacAddr_Object = MibTableColumn
tlsSpbFidMFibMacAddr = _TlsSpbFidMFibMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 134, 1, 1),
    _TlsSpbFidMFibMacAddr_Type()
)
tlsSpbFidMFibMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsSpbFidMFibMacAddr.setStatus("current")
_TlsSpbFidMFibLocale_Type = TmnxSpbFdbLocale
_TlsSpbFidMFibLocale_Object = MibTableColumn
tlsSpbFidMFibLocale = _TlsSpbFidMFibLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 134, 1, 2),
    _TlsSpbFidMFibLocale_Type()
)
tlsSpbFidMFibLocale.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsSpbFidMFibLocale.setStatus("current")
_TlsSpbFidMFibPortId_Type = TmnxPortID
_TlsSpbFidMFibPortId_Object = MibTableColumn
tlsSpbFidMFibPortId = _TlsSpbFidMFibPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 134, 1, 3),
    _TlsSpbFidMFibPortId_Type()
)
tlsSpbFidMFibPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsSpbFidMFibPortId.setStatus("current")
_TlsSpbFidMFibEncapValue_Type = TmnxEncapVal
_TlsSpbFidMFibEncapValue_Object = MibTableColumn
tlsSpbFidMFibEncapValue = _TlsSpbFidMFibEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 134, 1, 4),
    _TlsSpbFidMFibEncapValue_Type()
)
tlsSpbFidMFibEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsSpbFidMFibEncapValue.setStatus("current")
_TlsSpbFidMFibSdpId_Type = SdpId
_TlsSpbFidMFibSdpId_Object = MibTableColumn
tlsSpbFidMFibSdpId = _TlsSpbFidMFibSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 134, 1, 5),
    _TlsSpbFidMFibSdpId_Type()
)
tlsSpbFidMFibSdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsSpbFidMFibSdpId.setStatus("current")
_TlsSpbFidMFibVcId_Type = Unsigned32
_TlsSpbFidMFibVcId_Object = MibTableColumn
tlsSpbFidMFibVcId = _TlsSpbFidMFibVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 134, 1, 6),
    _TlsSpbFidMFibVcId_Type()
)
tlsSpbFidMFibVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsSpbFidMFibVcId.setStatus("current")
_TlsSpbFidMFibIsid_Type = Unsigned32
_TlsSpbFidMFibIsid_Object = MibTableColumn
tlsSpbFidMFibIsid = _TlsSpbFidMFibIsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 134, 1, 7),
    _TlsSpbFidMFibIsid_Type()
)
tlsSpbFidMFibIsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidMFibIsid.setStatus("current")
_TlsSpbFidMFibLastUpdate_Type = TimeStamp
_TlsSpbFidMFibLastUpdate_Object = MibTableColumn
tlsSpbFidMFibLastUpdate = _TlsSpbFidMFibLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 134, 1, 8),
    _TlsSpbFidMFibLastUpdate_Type()
)
tlsSpbFidMFibLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsSpbFidMFibLastUpdate.setStatus("current")
_SvcSpbIfTable_Object = MibTable
svcSpbIfTable = _SvcSpbIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 135)
)
if mibBuilder.loadTexts:
    svcSpbIfTable.setStatus("current")
_SvcSpbIfEntry_Object = MibTableRow
svcSpbIfEntry = _SvcSpbIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 135, 1)
)
svcSpbIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcSpbIfIndex"),
)
if mibBuilder.loadTexts:
    svcSpbIfEntry.setStatus("current")
_SvcSpbIfIndex_Type = InterfaceIndex
_SvcSpbIfIndex_Object = MibTableColumn
svcSpbIfIndex = _SvcSpbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 135, 1, 1),
    _SvcSpbIfIndex_Type()
)
svcSpbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcSpbIfIndex.setStatus("current")
_SvcSpbIfLocale_Type = TmnxSpbFdbLocale
_SvcSpbIfLocale_Object = MibTableColumn
svcSpbIfLocale = _SvcSpbIfLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 135, 1, 4),
    _SvcSpbIfLocale_Type()
)
svcSpbIfLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSpbIfLocale.setStatus("current")
_SvcSpbIfPortId_Type = TmnxPortID
_SvcSpbIfPortId_Object = MibTableColumn
svcSpbIfPortId = _SvcSpbIfPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 135, 1, 5),
    _SvcSpbIfPortId_Type()
)
svcSpbIfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSpbIfPortId.setStatus("current")
_SvcSpbIfEncapValue_Type = TmnxEncapVal
_SvcSpbIfEncapValue_Object = MibTableColumn
svcSpbIfEncapValue = _SvcSpbIfEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 135, 1, 6),
    _SvcSpbIfEncapValue_Type()
)
svcSpbIfEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSpbIfEncapValue.setStatus("current")
_SvcSpbIfSdpId_Type = SdpId
_SvcSpbIfSdpId_Object = MibTableColumn
svcSpbIfSdpId = _SvcSpbIfSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 135, 1, 7),
    _SvcSpbIfSdpId_Type()
)
svcSpbIfSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSpbIfSdpId.setStatus("current")
_SvcSpbIfVcId_Type = Unsigned32
_SvcSpbIfVcId_Object = MibTableColumn
svcSpbIfVcId = _SvcSpbIfVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 135, 1, 8),
    _SvcSpbIfVcId_Type()
)
svcSpbIfVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSpbIfVcId.setStatus("current")
_SvcSpbIfSvcId_Type = TmnxServId
_SvcSpbIfSvcId_Object = MibTableColumn
svcSpbIfSvcId = _SvcSpbIfSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 135, 1, 9),
    _SvcSpbIfSvcId_Type()
)
svcSpbIfSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSpbIfSvcId.setStatus("current")
_SvcSpbIfIsisInstance_Type = Integer32
_SvcSpbIfIsisInstance_Object = MibTableColumn
svcSpbIfIsisInstance = _SvcSpbIfIsisInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 135, 1, 10),
    _SvcSpbIfIsisInstance_Type()
)
svcSpbIfIsisInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSpbIfIsisInstance.setStatus("current")
_SvcArpHostOvrTable_Object = MibTable
svcArpHostOvrTable = _SvcArpHostOvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136)
)
if mibBuilder.loadTexts:
    svcArpHostOvrTable.setStatus("current")
_SvcArpHostOvrEntry_Object = MibTableRow
svcArpHostOvrEntry = _SvcArpHostOvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136, 1)
)
svcArpHostOvrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostIpAddrType"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostIpAddr"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostOvrDirection"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostOvrType"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostOvrTypeId"),
    (0, "TIMETRA-SERV-MIB", "svcArpHostOvrTypeName"),
)
if mibBuilder.loadTexts:
    svcArpHostOvrEntry.setStatus("current")


class _SvcArpHostOvrDirection_Type(TDirection):
    """Custom type svcArpHostOvrDirection based on TDirection"""
    subtypeSpec = TDirection.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_SvcArpHostOvrDirection_Type.__name__ = "TDirection"
_SvcArpHostOvrDirection_Object = MibTableColumn
svcArpHostOvrDirection = _SvcArpHostOvrDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136, 1, 1),
    _SvcArpHostOvrDirection_Type()
)
svcArpHostOvrDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcArpHostOvrDirection.setStatus("current")
_SvcArpHostOvrType_Type = TQosOverrideType
_SvcArpHostOvrType_Object = MibTableColumn
svcArpHostOvrType = _SvcArpHostOvrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136, 1, 2),
    _SvcArpHostOvrType_Type()
)
svcArpHostOvrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcArpHostOvrType.setStatus("current")
_SvcArpHostOvrTypeId_Type = Integer32
_SvcArpHostOvrTypeId_Object = MibTableColumn
svcArpHostOvrTypeId = _SvcArpHostOvrTypeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136, 1, 3),
    _SvcArpHostOvrTypeId_Type()
)
svcArpHostOvrTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcArpHostOvrTypeId.setStatus("current")
_SvcArpHostOvrTypeName_Type = TNamedItemOrEmpty
_SvcArpHostOvrTypeName_Object = MibTableColumn
svcArpHostOvrTypeName = _SvcArpHostOvrTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136, 1, 4),
    _SvcArpHostOvrTypeName_Type()
)
svcArpHostOvrTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcArpHostOvrTypeName.setStatus("current")
_SvcArpHostOvrPIR_Type = TPIRRateOverride
_SvcArpHostOvrPIR_Object = MibTableColumn
svcArpHostOvrPIR = _SvcArpHostOvrPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136, 1, 5),
    _SvcArpHostOvrPIR_Type()
)
svcArpHostOvrPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostOvrPIR.setStatus("current")
_SvcArpHostOvrCIR_Type = TCIRRateOverride
_SvcArpHostOvrCIR_Object = MibTableColumn
svcArpHostOvrCIR = _SvcArpHostOvrCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136, 1, 6),
    _SvcArpHostOvrCIR_Type()
)
svcArpHostOvrCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostOvrCIR.setStatus("current")
_SvcArpHostOvrCBS_Type = TBurstSizeBytesOverride
_SvcArpHostOvrCBS_Object = MibTableColumn
svcArpHostOvrCBS = _SvcArpHostOvrCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136, 1, 7),
    _SvcArpHostOvrCBS_Type()
)
svcArpHostOvrCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostOvrCBS.setStatus("current")
_SvcArpHostOvrMBS_Type = TBurstSizeBytesOverride
_SvcArpHostOvrMBS_Object = MibTableColumn
svcArpHostOvrMBS = _SvcArpHostOvrMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136, 1, 8),
    _SvcArpHostOvrMBS_Type()
)
svcArpHostOvrMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostOvrMBS.setStatus("current")
_SvcArpHostOvrWrrWeight_Type = THsmdaWrrWeightOverride
_SvcArpHostOvrWrrWeight_Object = MibTableColumn
svcArpHostOvrWrrWeight = _SvcArpHostOvrWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 136, 1, 9),
    _SvcArpHostOvrWrrWeight_Type()
)
svcArpHostOvrWrrWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcArpHostOvrWrrWeight.setStatus("current")
_IesIfIsaTnlNHTableLastChanged_Type = TimeStamp
_IesIfIsaTnlNHTableLastChanged_Object = MibScalar
iesIfIsaTnlNHTableLastChanged = _IesIfIsaTnlNHTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 137),
    _IesIfIsaTnlNHTableLastChanged_Type()
)
iesIfIsaTnlNHTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIfIsaTnlNHTableLastChanged.setStatus("current")
_IesIfIsaTnlNHTable_Object = MibTable
iesIfIsaTnlNHTable = _IesIfIsaTnlNHTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 138)
)
if mibBuilder.loadTexts:
    iesIfIsaTnlNHTable.setStatus("current")
_IesIfIsaTnlNHEntry_Object = MibTableRow
iesIfIsaTnlNHEntry = _IesIfIsaTnlNHEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 138, 1)
)
if mibBuilder.loadTexts:
    iesIfIsaTnlNHEntry.setStatus("current")
_IesIfIsaTnlNHLastChanged_Type = TimeStamp
_IesIfIsaTnlNHLastChanged_Object = MibTableColumn
iesIfIsaTnlNHLastChanged = _IesIfIsaTnlNHLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 138, 1, 1),
    _IesIfIsaTnlNHLastChanged_Type()
)
iesIfIsaTnlNHLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIfIsaTnlNHLastChanged.setStatus("current")


class _IesIfIsaTnlNHStaticAddrType_Type(InetAddressType):
    """Custom type iesIfIsaTnlNHStaticAddrType based on InetAddressType"""


_IesIfIsaTnlNHStaticAddrType_Object = MibTableColumn
iesIfIsaTnlNHStaticAddrType = _IesIfIsaTnlNHStaticAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 138, 1, 2),
    _IesIfIsaTnlNHStaticAddrType_Type()
)
iesIfIsaTnlNHStaticAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesIfIsaTnlNHStaticAddrType.setStatus("current")


class _IesIfIsaTnlNHStaticAddr_Type(InetAddress):
    """Custom type iesIfIsaTnlNHStaticAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_IesIfIsaTnlNHStaticAddr_Type.__name__ = "InetAddress"
_IesIfIsaTnlNHStaticAddr_Object = MibTableColumn
iesIfIsaTnlNHStaticAddr = _IesIfIsaTnlNHStaticAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 138, 1, 3),
    _IesIfIsaTnlNHStaticAddr_Type()
)
iesIfIsaTnlNHStaticAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesIfIsaTnlNHStaticAddr.setStatus("current")


class _IesIfIsaTnlNHDynAddrType_Type(InetAddressType):
    """Custom type iesIfIsaTnlNHDynAddrType based on InetAddressType"""


_IesIfIsaTnlNHDynAddrType_Object = MibTableColumn
iesIfIsaTnlNHDynAddrType = _IesIfIsaTnlNHDynAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 138, 1, 4),
    _IesIfIsaTnlNHDynAddrType_Type()
)
iesIfIsaTnlNHDynAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesIfIsaTnlNHDynAddrType.setStatus("current")


class _IesIfIsaTnlNHDynAddr_Type(InetAddress):
    """Custom type iesIfIsaTnlNHDynAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_IesIfIsaTnlNHDynAddr_Type.__name__ = "InetAddress"
_IesIfIsaTnlNHDynAddr_Object = MibTableColumn
iesIfIsaTnlNHDynAddr = _IesIfIsaTnlNHDynAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 138, 1, 5),
    _IesIfIsaTnlNHDynAddr_Type()
)
iesIfIsaTnlNHDynAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesIfIsaTnlNHDynAddr.setStatus("current")
_TmnxTstpNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxTstpNotifyObjs = _TmnxTstpNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 5)
)
_TmnxCustomerBridgeId_Type = BridgeId
_TmnxCustomerBridgeId_Object = MibScalar
tmnxCustomerBridgeId = _TmnxCustomerBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 5, 1),
    _TmnxCustomerBridgeId_Type()
)
tmnxCustomerBridgeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCustomerBridgeId.setStatus("current")
_TmnxCustomerRootBridgeId_Type = BridgeId
_TmnxCustomerRootBridgeId_Object = MibScalar
tmnxCustomerRootBridgeId = _TmnxCustomerRootBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 5, 2),
    _TmnxCustomerRootBridgeId_Type()
)
tmnxCustomerRootBridgeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCustomerRootBridgeId.setStatus("current")
_TmnxOtherBridgeId_Type = BridgeId
_TmnxOtherBridgeId_Object = MibScalar
tmnxOtherBridgeId = _TmnxOtherBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 5, 3),
    _TmnxOtherBridgeId_Type()
)
tmnxOtherBridgeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOtherBridgeId.setStatus("current")
_TmnxOldSdpBindTlsStpPortState_Type = TStpPortState
_TmnxOldSdpBindTlsStpPortState_Object = MibScalar
tmnxOldSdpBindTlsStpPortState = _TmnxOldSdpBindTlsStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 5, 4),
    _TmnxOldSdpBindTlsStpPortState_Type()
)
tmnxOldSdpBindTlsStpPortState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOldSdpBindTlsStpPortState.setStatus("current")
_TmnxVcpState_Type = TStpPortState
_TmnxVcpState_Object = MibScalar
tmnxVcpState = _TmnxVcpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 5, 5),
    _TmnxVcpState_Type()
)
tmnxVcpState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVcpState.setStatus("current")
_TmnxSvcNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxSvcNotifyObjs = _TmnxSvcNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6)
)
_MacPinningMacAddress_Type = MacAddress
_MacPinningMacAddress_Object = MibScalar
macPinningMacAddress = _MacPinningMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 1),
    _MacPinningMacAddress_Type()
)
macPinningMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    macPinningMacAddress.setStatus("current")
_MacPinningPinnedRow_Type = RowPointer
_MacPinningPinnedRow_Object = MibScalar
macPinningPinnedRow = _MacPinningPinnedRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 2),
    _MacPinningPinnedRow_Type()
)
macPinningPinnedRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    macPinningPinnedRow.setStatus("current")
_MacPinningPinnedRowDescr_Type = DisplayString
_MacPinningPinnedRowDescr_Object = MibScalar
macPinningPinnedRowDescr = _MacPinningPinnedRowDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 3),
    _MacPinningPinnedRowDescr_Type()
)
macPinningPinnedRowDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    macPinningPinnedRowDescr.setStatus("current")
_MacPinningViolatingRow_Type = RowPointer
_MacPinningViolatingRow_Object = MibScalar
macPinningViolatingRow = _MacPinningViolatingRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 4),
    _MacPinningViolatingRow_Type()
)
macPinningViolatingRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    macPinningViolatingRow.setStatus("current")
_MacPinningViolatingRowDescr_Type = DisplayString
_MacPinningViolatingRowDescr_Object = MibScalar
macPinningViolatingRowDescr = _MacPinningViolatingRowDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 5),
    _MacPinningViolatingRowDescr_Type()
)
macPinningViolatingRowDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    macPinningViolatingRowDescr.setStatus("current")
_TlsDHCPClientLease_Type = Integer32
_TlsDHCPClientLease_Object = MibScalar
tlsDHCPClientLease = _TlsDHCPClientLease_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 6),
    _TlsDHCPClientLease_Type()
)
tlsDHCPClientLease.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDHCPClientLease.setStatus("obsolete")
_TlsDhcpLseStateOldCiAddr_Type = IpAddress
_TlsDhcpLseStateOldCiAddr_Object = MibScalar
tlsDhcpLseStateOldCiAddr = _TlsDhcpLseStateOldCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 7),
    _TlsDhcpLseStateOldCiAddr_Type()
)
tlsDhcpLseStateOldCiAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpLseStateOldCiAddr.setStatus("obsolete")
_TlsDhcpLseStateOldChAddr_Type = MacAddress
_TlsDhcpLseStateOldChAddr_Object = MibScalar
tlsDhcpLseStateOldChAddr = _TlsDhcpLseStateOldChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 8),
    _TlsDhcpLseStateOldChAddr_Type()
)
tlsDhcpLseStateOldChAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpLseStateOldChAddr.setStatus("obsolete")
_TlsDhcpLseStateNewCiAddr_Type = IpAddress
_TlsDhcpLseStateNewCiAddr_Object = MibScalar
tlsDhcpLseStateNewCiAddr = _TlsDhcpLseStateNewCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 9),
    _TlsDhcpLseStateNewCiAddr_Type()
)
tlsDhcpLseStateNewCiAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpLseStateNewCiAddr.setStatus("obsolete")
_TlsDhcpLseStateNewChAddr_Type = MacAddress
_TlsDhcpLseStateNewChAddr_Object = MibScalar
tlsDhcpLseStateNewChAddr = _TlsDhcpLseStateNewChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 10),
    _TlsDhcpLseStateNewChAddr_Type()
)
tlsDhcpLseStateNewChAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpLseStateNewChAddr.setStatus("obsolete")
_TlsDhcpRestoreLseStateCiAddr_Type = IpAddress
_TlsDhcpRestoreLseStateCiAddr_Object = MibScalar
tlsDhcpRestoreLseStateCiAddr = _TlsDhcpRestoreLseStateCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 11),
    _TlsDhcpRestoreLseStateCiAddr_Type()
)
tlsDhcpRestoreLseStateCiAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpRestoreLseStateCiAddr.setStatus("obsolete")
_TlsDhcpRestoreLseStateSvcId_Type = TmnxServId
_TlsDhcpRestoreLseStateSvcId_Object = MibScalar
tlsDhcpRestoreLseStateSvcId = _TlsDhcpRestoreLseStateSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 12),
    _TlsDhcpRestoreLseStateSvcId_Type()
)
tlsDhcpRestoreLseStateSvcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpRestoreLseStateSvcId.setStatus("obsolete")
_TlsDhcpRestoreLseStatePortId_Type = TmnxPortID
_TlsDhcpRestoreLseStatePortId_Object = MibScalar
tlsDhcpRestoreLseStatePortId = _TlsDhcpRestoreLseStatePortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 13),
    _TlsDhcpRestoreLseStatePortId_Type()
)
tlsDhcpRestoreLseStatePortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpRestoreLseStatePortId.setStatus("obsolete")
_TlsDhcpRestoreLseStateEncapVal_Type = TmnxEncapVal
_TlsDhcpRestoreLseStateEncapVal_Object = MibScalar
tlsDhcpRestoreLseStateEncapVal = _TlsDhcpRestoreLseStateEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 14),
    _TlsDhcpRestoreLseStateEncapVal_Type()
)
tlsDhcpRestoreLseStateEncapVal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpRestoreLseStateEncapVal.setStatus("obsolete")
_TlsDhcpRestoreLseStateProblem_Type = DisplayString
_TlsDhcpRestoreLseStateProblem_Object = MibScalar
tlsDhcpRestoreLseStateProblem = _TlsDhcpRestoreLseStateProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 15),
    _TlsDhcpRestoreLseStateProblem_Type()
)
tlsDhcpRestoreLseStateProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpRestoreLseStateProblem.setStatus("obsolete")
_TlsDhcpPacketProblem_Type = DisplayString
_TlsDhcpPacketProblem_Object = MibScalar
tlsDhcpPacketProblem = _TlsDhcpPacketProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 16),
    _TlsDhcpPacketProblem_Type()
)
tlsDhcpPacketProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpPacketProblem.setStatus("obsolete")
_TlsDhcpLseStatePopulateError_Type = DisplayString
_TlsDhcpLseStatePopulateError_Object = MibScalar
tlsDhcpLseStatePopulateError = _TlsDhcpLseStatePopulateError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 17),
    _TlsDhcpLseStatePopulateError_Type()
)
tlsDhcpLseStatePopulateError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tlsDhcpLseStatePopulateError.setStatus("obsolete")
_SvcDhcpRestoreLseStateCiAddr_Type = IpAddress
_SvcDhcpRestoreLseStateCiAddr_Object = MibScalar
svcDhcpRestoreLseStateCiAddr = _SvcDhcpRestoreLseStateCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 18),
    _SvcDhcpRestoreLseStateCiAddr_Type()
)
svcDhcpRestoreLseStateCiAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpRestoreLseStateCiAddr.setStatus("current")
_SvcDhcpRestoreLseStateProblem_Type = DisplayString
_SvcDhcpRestoreLseStateProblem_Object = MibScalar
svcDhcpRestoreLseStateProblem = _SvcDhcpRestoreLseStateProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 19),
    _SvcDhcpRestoreLseStateProblem_Type()
)
svcDhcpRestoreLseStateProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpRestoreLseStateProblem.setStatus("current")
_SvcDhcpLseStateOldCiAddr_Type = IpAddress
_SvcDhcpLseStateOldCiAddr_Object = MibScalar
svcDhcpLseStateOldCiAddr = _SvcDhcpLseStateOldCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 20),
    _SvcDhcpLseStateOldCiAddr_Type()
)
svcDhcpLseStateOldCiAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpLseStateOldCiAddr.setStatus("current")
_SvcDhcpLseStateOldChAddr_Type = MacAddress
_SvcDhcpLseStateOldChAddr_Object = MibScalar
svcDhcpLseStateOldChAddr = _SvcDhcpLseStateOldChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 21),
    _SvcDhcpLseStateOldChAddr_Type()
)
svcDhcpLseStateOldChAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpLseStateOldChAddr.setStatus("current")
_SvcDhcpLseStateNewCiAddr_Type = IpAddress
_SvcDhcpLseStateNewCiAddr_Object = MibScalar
svcDhcpLseStateNewCiAddr = _SvcDhcpLseStateNewCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 22),
    _SvcDhcpLseStateNewCiAddr_Type()
)
svcDhcpLseStateNewCiAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpLseStateNewCiAddr.setStatus("current")
_SvcDhcpLseStateNewChAddr_Type = MacAddress
_SvcDhcpLseStateNewChAddr_Object = MibScalar
svcDhcpLseStateNewChAddr = _SvcDhcpLseStateNewChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 23),
    _SvcDhcpLseStateNewChAddr_Type()
)
svcDhcpLseStateNewChAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpLseStateNewChAddr.setStatus("current")
_SvcDhcpClientLease_Type = Integer32
_SvcDhcpClientLease_Object = MibScalar
svcDhcpClientLease = _SvcDhcpClientLease_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 24),
    _SvcDhcpClientLease_Type()
)
svcDhcpClientLease.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpClientLease.setStatus("current")
_SvcDhcpPacketProblem_Type = DisplayString
_SvcDhcpPacketProblem_Object = MibScalar
svcDhcpPacketProblem = _SvcDhcpPacketProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 25),
    _SvcDhcpPacketProblem_Type()
)
svcDhcpPacketProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpPacketProblem.setStatus("current")
_SvcDhcpLseStatePopulateError_Type = DisplayString
_SvcDhcpLseStatePopulateError_Object = MibScalar
svcDhcpLseStatePopulateError = _SvcDhcpLseStatePopulateError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 26),
    _SvcDhcpLseStatePopulateError_Type()
)
svcDhcpLseStatePopulateError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpLseStatePopulateError.setStatus("current")
_HostConnectivityCiAddrType_Type = InetAddressType
_HostConnectivityCiAddrType_Object = MibScalar
hostConnectivityCiAddrType = _HostConnectivityCiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 27),
    _HostConnectivityCiAddrType_Type()
)
hostConnectivityCiAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hostConnectivityCiAddrType.setStatus("current")
_HostConnectivityCiAddr_Type = InetAddress
_HostConnectivityCiAddr_Object = MibScalar
hostConnectivityCiAddr = _HostConnectivityCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 28),
    _HostConnectivityCiAddr_Type()
)
hostConnectivityCiAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hostConnectivityCiAddr.setStatus("current")
_HostConnectivityChAddr_Type = MacAddress
_HostConnectivityChAddr_Object = MibScalar
hostConnectivityChAddr = _HostConnectivityChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 29),
    _HostConnectivityChAddr_Type()
)
hostConnectivityChAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hostConnectivityChAddr.setStatus("current")
_ProtectedMacForNotify_Type = MacAddress
_ProtectedMacForNotify_Object = MibScalar
protectedMacForNotify = _ProtectedMacForNotify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 30),
    _ProtectedMacForNotify_Type()
)
protectedMacForNotify.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    protectedMacForNotify.setStatus("current")
_StaticHostDynamicMacIpAddress_Type = IpAddress
_StaticHostDynamicMacIpAddress_Object = MibScalar
staticHostDynamicMacIpAddress = _StaticHostDynamicMacIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 31),
    _StaticHostDynamicMacIpAddress_Type()
)
staticHostDynamicMacIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    staticHostDynamicMacIpAddress.setStatus("current")
_StaticHostDynamicMacConflict_Type = DisplayString
_StaticHostDynamicMacConflict_Object = MibScalar
staticHostDynamicMacConflict = _StaticHostDynamicMacConflict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 32),
    _StaticHostDynamicMacConflict_Type()
)
staticHostDynamicMacConflict.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    staticHostDynamicMacConflict.setStatus("current")
_TmnxSvcObjRow_Type = RowPointer
_TmnxSvcObjRow_Object = MibScalar
tmnxSvcObjRow = _TmnxSvcObjRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 33),
    _TmnxSvcObjRow_Type()
)
tmnxSvcObjRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSvcObjRow.setStatus("current")
_TmnxSvcObjRowDescr_Type = DisplayString
_TmnxSvcObjRowDescr_Object = MibScalar
tmnxSvcObjRowDescr = _TmnxSvcObjRowDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 34),
    _TmnxSvcObjRowDescr_Type()
)
tmnxSvcObjRowDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSvcObjRowDescr.setStatus("current")
_TmnxSvcObjTodSuite_Type = DisplayString
_TmnxSvcObjTodSuite_Object = MibScalar
tmnxSvcObjTodSuite = _TmnxSvcObjTodSuite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 35),
    _TmnxSvcObjTodSuite_Type()
)
tmnxSvcObjTodSuite.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSvcObjTodSuite.setStatus("current")
_TmnxFailureDescription_Type = DisplayString
_TmnxFailureDescription_Object = MibScalar
tmnxFailureDescription = _TmnxFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 36),
    _TmnxFailureDescription_Type()
)
tmnxFailureDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxFailureDescription.setStatus("current")
_SvcDhcpProxyError_Type = DisplayString
_SvcDhcpProxyError_Object = MibScalar
svcDhcpProxyError = _SvcDhcpProxyError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 37),
    _SvcDhcpProxyError_Type()
)
svcDhcpProxyError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpProxyError.setStatus("current")
_SvcDhcpCoAError_Type = DisplayString
_SvcDhcpCoAError_Object = MibScalar
svcDhcpCoAError = _SvcDhcpCoAError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 38),
    _SvcDhcpCoAError_Type()
)
svcDhcpCoAError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpCoAError.setStatus("current")
_SvcDhcpSubAuthError_Type = DisplayString
_SvcDhcpSubAuthError_Object = MibScalar
svcDhcpSubAuthError = _SvcDhcpSubAuthError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 39),
    _SvcDhcpSubAuthError_Type()
)
svcDhcpSubAuthError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcDhcpSubAuthError.setStatus("current")


class _SvcTlsMrpAttrRegFailedReason_Type(Integer32):
    """Custom type svcTlsMrpAttrRegFailedReason based on Integer32"""
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
        *(("attribute-limit-reached", 2),
          ("mfib-entry-create-failed", 5),
          ("system-attr-limit-reached", 3),
          ("unknown", 1),
          ("unsupported-attribute", 4))
    )


_SvcTlsMrpAttrRegFailedReason_Type.__name__ = "Integer32"
_SvcTlsMrpAttrRegFailedReason_Object = MibScalar
svcTlsMrpAttrRegFailedReason = _SvcTlsMrpAttrRegFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 40),
    _SvcTlsMrpAttrRegFailedReason_Type()
)
svcTlsMrpAttrRegFailedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcTlsMrpAttrRegFailedReason.setStatus("current")


class _SvcTlsMrpAttrType_Type(Unsigned32):
    """Custom type svcTlsMrpAttrType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SvcTlsMrpAttrType_Type.__name__ = "Unsigned32"
_SvcTlsMrpAttrType_Object = MibScalar
svcTlsMrpAttrType = _SvcTlsMrpAttrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 41),
    _SvcTlsMrpAttrType_Type()
)
svcTlsMrpAttrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcTlsMrpAttrType.setStatus("current")


class _SvcTlsMrpAttrValue_Type(OctetString):
    """Custom type svcTlsMrpAttrValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvcTlsMrpAttrValue_Type.__name__ = "OctetString"
_SvcTlsMrpAttrValue_Object = MibScalar
svcTlsMrpAttrValue = _SvcTlsMrpAttrValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 42),
    _SvcTlsMrpAttrValue_Type()
)
svcTlsMrpAttrValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcTlsMrpAttrValue.setStatus("current")
_SvcMstiInstanceId_Type = MstiInstanceId
_SvcMstiInstanceId_Object = MibScalar
svcMstiInstanceId = _SvcMstiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 43),
    _SvcMstiInstanceId_Type()
)
svcMstiInstanceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcMstiInstanceId.setStatus("current")
_SvcNotifSapPortId_Type = TmnxPortID
_SvcNotifSapPortId_Object = MibScalar
svcNotifSapPortId = _SvcNotifSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 44),
    _SvcNotifSapPortId_Type()
)
svcNotifSapPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcNotifSapPortId.setStatus("current")
_SvcNotifSapEncapValue_Type = TmnxEncapVal
_SvcNotifSapEncapValue_Object = MibScalar
svcNotifSapEncapValue = _SvcNotifSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 45),
    _SvcNotifSapEncapValue_Type()
)
svcNotifSapEncapValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcNotifSapEncapValue.setStatus("current")
_SvcArpHostPopulateError_Type = DisplayString
_SvcArpHostPopulateError_Object = MibScalar
svcArpHostPopulateError = _SvcArpHostPopulateError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 46),
    _SvcArpHostPopulateError_Type()
)
svcArpHostPopulateError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcArpHostPopulateError.setStatus("current")
_SvcHostAddrType_Type = InetAddressType
_SvcHostAddrType_Object = MibScalar
svcHostAddrType = _SvcHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 47),
    _SvcHostAddrType_Type()
)
svcHostAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcHostAddrType.setStatus("current")


class _SvcHostAddr_Type(InetAddress):
    """Custom type svcHostAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SvcHostAddr_Type.__name__ = "InetAddress"
_SvcHostAddr_Object = MibScalar
svcHostAddr = _SvcHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 6, 48),
    _SvcHostAddr_Type()
)
svcHostAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcHostAddr.setStatus("current")
_TmnxServNotifications_ObjectIdentity = ObjectIdentity
tmnxServNotifications = _TmnxServNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4)
)
_CustTrapsPrefix_ObjectIdentity = ObjectIdentity
custTrapsPrefix = _CustTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 1)
)
_CustTraps_ObjectIdentity = ObjectIdentity
custTraps = _CustTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 1, 0)
)
_SvcTrapsPrefix_ObjectIdentity = ObjectIdentity
svcTrapsPrefix = _SvcTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2)
)
_SvcTraps_ObjectIdentity = ObjectIdentity
svcTraps = _SvcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0)
)
_TstpTrapsPrefix_ObjectIdentity = ObjectIdentity
tstpTrapsPrefix = _TstpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5)
)
_TstpTraps_ObjectIdentity = ObjectIdentity
tstpTraps = _TstpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0)
)
svcDhcpLeaseStateEntry.registerAugmentions(
    ("TIMETRA-SERV-MIB",
     "svcDhcpLeaseStateModifyEntry")
)
svcDhcpLeaseStateModifyEntry.setIndexNames(*svcDhcpLeaseStateEntry.getIndexNames())
svcDhcpLeaseStateEntry.registerAugmentions(
    ("TIMETRA-SERV-MIB",
     "svcDhcpLeaseStateActionEntry")
)
svcDhcpLeaseStateActionEntry.setIndexNames(*svcDhcpLeaseStateEntry.getIndexNames())
svcTlsInfoEntry.registerAugmentions(
    ("TIMETRA-SERV-MIB",
     "svcTlsBackboneInfoEntry")
)
svcTlsBackboneInfoEntry.setIndexNames(*svcTlsInfoEntry.getIndexNames())
svcDhcpLeaseStateEntry.registerAugmentions(
    ("TIMETRA-SERV-MIB",
     "svcDhcpLeaseStateBgpEntry")
)
svcDhcpLeaseStateBgpEntry.setIndexNames(*svcDhcpLeaseStateEntry.getIndexNames())
svcArpHostEntry.registerAugmentions(
    ("TIMETRA-SERV-MIB",
     "svcArpHostBgpEntry")
)
svcArpHostBgpEntry.setIndexNames(*svcArpHostEntry.getIndexNames())
svcDhcpLeaseEntry.registerAugmentions(
    ("TIMETRA-SERV-MIB",
     "svcDhcpLeaseModifyEntry")
)
svcDhcpLeaseModifyEntry.setIndexNames(*svcDhcpLeaseEntry.getIndexNames())
svcDhcpLeaseEntry.registerAugmentions(
    ("TIMETRA-SERV-MIB",
     "svcDhcpLeaseActionEntry")
)
svcDhcpLeaseActionEntry.setIndexNames(*svcDhcpLeaseEntry.getIndexNames())
svcDhcpLeaseEntry.registerAugmentions(
    ("TIMETRA-SERV-MIB",
     "svcDhcpLeaseBgpEntry")
)
svcDhcpLeaseBgpEntry.setIndexNames(*svcDhcpLeaseEntry.getIndexNames())
svcTlsInfoEntry.registerAugmentions(
    ("TIMETRA-SERV-MIB",
     "svcTlsExtEntry")
)
svcTlsExtEntry.setIndexNames(*svcTlsInfoEntry.getIndexNames())
iesIfEntry.registerAugmentions(
    ("TIMETRA-SERV-MIB",
     "iesIfIsaTnlNHEntry")
)
iesIfIsaTnlNHEntry.setIndexNames(*iesIfEntry.getIndexNames())

# Managed Objects groups

tmnxCustV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1, 2, 100)
)
tmnxCustV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "custNumEntries"),
        ("TIMETRA-SERV-MIB", "custNextFreeId"),
        ("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "custRowStatus"),
        ("TIMETRA-SERV-MIB", "custDescription"),
        ("TIMETRA-SERV-MIB", "custContact"),
        ("TIMETRA-SERV-MIB", "custPhone"),
        ("TIMETRA-SERV-MIB", "custLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteName"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteRowStatus"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteDescription"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteScope"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteAssignment"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteIngressSchedulerPolicy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteEgressSchedulerPolicy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteTodSuite"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteCurrentIngrSchedPlcy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteCurrentEgrSchedPlcy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteEgressAggRateLimit"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteIntendedIngrSchedPlcy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteIntendedEgrSchedPlcy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteFrameBasedAccnt"),
        ("TIMETRA-SERV-MIB", "custIngQosSchedStatsForwardedPackets"),
        ("TIMETRA-SERV-MIB", "custIngQosSchedStatsForwardedOctets"),
        ("TIMETRA-SERV-MIB", "custEgrQosSchedStatsForwardedPackets"),
        ("TIMETRA-SERV-MIB", "custEgrQosSchedStatsForwardedOctets"),
        ("TIMETRA-SERV-MIB", "custIngQosPortSchedFwdPkts"),
        ("TIMETRA-SERV-MIB", "custIngQosPortSchedFwdOctets"),
        ("TIMETRA-SERV-MIB", "custEgrQosPortSchedFwdPkts"),
        ("TIMETRA-SERV-MIB", "custEgrQosPortSchedFwdOctets"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSRowStatus"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSOverrideFlags"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSPIR"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSCIR"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSSummedCIR"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSRowStatus"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSOverrideFlags"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSPIR"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSCIR"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSSummedCIR"),
        ("TIMETRA-SERV-MIB", "custIngSchedPlcyStatsFwdPkt"),
        ("TIMETRA-SERV-MIB", "custIngSchedPlcyStatsFwdOct"),
        ("TIMETRA-SERV-MIB", "custEgrSchedPlcyStatsFwdPkt"),
        ("TIMETRA-SERV-MIB", "custEgrSchedPlcyStatsFwdOct"),
        ("TIMETRA-SERV-MIB", "custIngSchedPlcyPortStatsFwdPkt"),
        ("TIMETRA-SERV-MIB", "custIngSchedPlcyPortStatsFwdOct"),
        ("TIMETRA-SERV-MIB", "custEgrSchedPlcyPortStatsFwdPkt"),
        ("TIMETRA-SERV-MIB", "custEgrSchedPlcyPortStatsFwdOct"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteFrameBasedAccnt"))
)
if mibBuilder.loadTexts:
    tmnxCustV6v0Group.setStatus("obsolete")

tmnxCustV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1, 2, 102)
)
tmnxCustV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "custNumEntries"),
        ("TIMETRA-SERV-MIB", "custNextFreeId"),
        ("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "custRowStatus"),
        ("TIMETRA-SERV-MIB", "custDescription"),
        ("TIMETRA-SERV-MIB", "custContact"),
        ("TIMETRA-SERV-MIB", "custPhone"),
        ("TIMETRA-SERV-MIB", "custLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteName"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteRowStatus"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteDescription"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteScope"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteAssignment"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteIngressSchedulerPolicy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteEgressSchedulerPolicy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteTodSuite"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteCurrentIngrSchedPlcy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteCurrentEgrSchedPlcy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteEgressAggRateLimit"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteIntendedIngrSchedPlcy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteIntendedEgrSchedPlcy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteFrameBasedAccnt"),
        ("TIMETRA-SERV-MIB", "custIngQosSchedStatsForwardedPackets"),
        ("TIMETRA-SERV-MIB", "custIngQosSchedStatsForwardedOctets"),
        ("TIMETRA-SERV-MIB", "custEgrQosSchedStatsForwardedPackets"),
        ("TIMETRA-SERV-MIB", "custEgrQosSchedStatsForwardedOctets"),
        ("TIMETRA-SERV-MIB", "custIngQosPortSchedFwdPkts"),
        ("TIMETRA-SERV-MIB", "custIngQosPortSchedFwdOctets"),
        ("TIMETRA-SERV-MIB", "custEgrQosPortSchedFwdPkts"),
        ("TIMETRA-SERV-MIB", "custEgrQosPortSchedFwdOctets"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSRowStatus"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSOverrideFlags"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSPIR"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSCIR"),
        ("TIMETRA-SERV-MIB", "custMssIngQosSSummedCIR"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSRowStatus"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSOverrideFlags"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSPIR"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSCIR"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosSSummedCIR"),
        ("TIMETRA-SERV-MIB", "custIngSchedPlcyStatsFwdPkt"),
        ("TIMETRA-SERV-MIB", "custIngSchedPlcyStatsFwdOct"),
        ("TIMETRA-SERV-MIB", "custEgrSchedPlcyStatsFwdPkt"),
        ("TIMETRA-SERV-MIB", "custEgrSchedPlcyStatsFwdOct"),
        ("TIMETRA-SERV-MIB", "custIngSchedPlcyPortStatsFwdPkt"),
        ("TIMETRA-SERV-MIB", "custIngSchedPlcyPortStatsFwdOct"),
        ("TIMETRA-SERV-MIB", "custEgrSchedPlcyPortStatsFwdPkt"),
        ("TIMETRA-SERV-MIB", "custEgrSchedPlcyPortStatsFwdOct"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteFrameBasedAccnt"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteSubscriberMss"))
)
if mibBuilder.loadTexts:
    tmnxCustV8v0Group.setStatus("current")

tmnxCustV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1, 2, 103)
)
tmnxCustV9v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "custMultSvcSiteIngPolcrCtrlPolcy"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteEgrPolcrCtrlPolcy"))
)
if mibBuilder.loadTexts:
    tmnxCustV9v0Group.setStatus("current")

tmnxSvcV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 101)
)
tmnxSvcV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcNumEntries"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcRowStatus"),
        ("TIMETRA-SERV-MIB", "svcType"),
        ("TIMETRA-SERV-MIB", "svcCustId"),
        ("TIMETRA-SERV-MIB", "svcIpRouting"),
        ("TIMETRA-SERV-MIB", "svcDescription"),
        ("TIMETRA-SERV-MIB", "svcMtu"),
        ("TIMETRA-SERV-MIB", "svcAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcOperStatus"),
        ("TIMETRA-SERV-MIB", "svcNumSaps"),
        ("TIMETRA-SERV-MIB", "svcNumSdps"),
        ("TIMETRA-SERV-MIB", "svcLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcDefMeshVcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SERV-MIB", "svcVRouterId"),
        ("TIMETRA-SERV-MIB", "svcAutoBind"),
        ("TIMETRA-SERV-MIB", "svcLastStatusChange"),
        ("TIMETRA-SERV-MIB", "svcVllType"),
        ("TIMETRA-SERV-MIB", "svcMgmtVpls"),
        ("TIMETRA-SERV-MIB", "svcRadiusDiscovery"),
        ("TIMETRA-SERV-MIB", "svcRadiusUserName"),
        ("TIMETRA-SERV-MIB", "svcRadiusUserNameType"),
        ("TIMETRA-SERV-MIB", "svcVcSwitching"),
        ("TIMETRA-SERV-MIB", "svcRadiusPEDiscPolicy"),
        ("TIMETRA-SERV-MIB", "svcRadiusDiscoveryShutdown"),
        ("TIMETRA-SERV-MIB", "svcVplsType"),
        ("TIMETRA-SERV-MIB", "svcTotalFdbMimDestIdxEntries"))
)
if mibBuilder.loadTexts:
    tmnxSvcV6v0Group.setStatus("current")

tmnxSvcTlsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 102)
)
tmnxSvcTlsV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsMacLearning"),
        ("TIMETRA-SERV-MIB", "svcTlsDiscardUnknownDest"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbTableSize"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbNumEntries"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbNumStaticEntries"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbLocalAgeTime"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbRemoteAgeTime"),
        ("TIMETRA-SERV-MIB", "svcTlsStpAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsStpPriority"),
        ("TIMETRA-SERV-MIB", "svcTlsStpBridgeAddress"),
        ("TIMETRA-SERV-MIB", "svcTlsStpTimeSinceTopologyChange"),
        ("TIMETRA-SERV-MIB", "svcTlsStpTopologyChanges"),
        ("TIMETRA-SERV-MIB", "svcTlsStpDesignatedRoot"),
        ("TIMETRA-SERV-MIB", "svcTlsStpRootCost"),
        ("TIMETRA-SERV-MIB", "svcTlsStpRootPort"),
        ("TIMETRA-SERV-MIB", "svcTlsStpMaxAge"),
        ("TIMETRA-SERV-MIB", "svcTlsStpHelloTime"),
        ("TIMETRA-SERV-MIB", "svcTlsStpForwardDelay"),
        ("TIMETRA-SERV-MIB", "svcTlsStpBridgeMaxAge"),
        ("TIMETRA-SERV-MIB", "svcTlsStpBridgeHelloTime"),
        ("TIMETRA-SERV-MIB", "svcTlsStpBridgeForwardDelay"),
        ("TIMETRA-SERV-MIB", "svcTlsStpOperStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsStpVirtualRootBridgeStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsMacAgeing"),
        ("TIMETRA-SERV-MIB", "svcTlsStpTopologyChangeActive"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbTableFullHighWatermark"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbTableFullLowWatermark"),
        ("TIMETRA-SERV-MIB", "svcTlsVpnId"),
        ("TIMETRA-SERV-MIB", "svcTlsCustId"),
        ("TIMETRA-SERV-MIB", "svcTlsStpVersion"),
        ("TIMETRA-SERV-MIB", "svcTlsStpHoldCount"),
        ("TIMETRA-SERV-MIB", "svcTlsStpPrimaryBridge"),
        ("TIMETRA-SERV-MIB", "svcTlsStpBridgeInstanceId"),
        ("TIMETRA-SERV-MIB", "svcTlsStpVcpOperProtocol"),
        ("TIMETRA-SERV-MIB", "svcTlsMacMoveMaxRate"),
        ("TIMETRA-SERV-MIB", "svcTlsMacMoveRetryTimeout"),
        ("TIMETRA-SERV-MIB", "svcTlsMacMoveAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsMacRelearnOnly"),
        ("TIMETRA-SERV-MIB", "svcTlsMfibTableSize"),
        ("TIMETRA-SERV-MIB", "svcTlsMfibTableFullHighWatermark"),
        ("TIMETRA-SERV-MIB", "svcTlsMfibTableFullLowWatermark"),
        ("TIMETRA-SERV-MIB", "svcTlsMacFlushOnFail"),
        ("TIMETRA-SERV-MIB", "svcTlsStpRegionName"),
        ("TIMETRA-SERV-MIB", "svcTlsStpRegionRevision"),
        ("TIMETRA-SERV-MIB", "svcTlsStpBridgeMaxHops"),
        ("TIMETRA-SERV-MIB", "svcTlsStpCistRegionalRoot"),
        ("TIMETRA-SERV-MIB", "svcTlsStpCistIntRootCost"),
        ("TIMETRA-SERV-MIB", "svcTlsStpCistRemainingHopCount"),
        ("TIMETRA-SERV-MIB", "svcTlsStpCistRegionalRootPort"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbNumLearnedEntries"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbNumOamEntries"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbNumDhcpEntries"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbNumHostEntries"),
        ("TIMETRA-SERV-MIB", "svcTlsShcvAction"),
        ("TIMETRA-SERV-MIB", "svcTlsShcvSrcIp"),
        ("TIMETRA-SERV-MIB", "svcTlsShcvSrcMac"),
        ("TIMETRA-SERV-MIB", "svcTlsShcvInterval"),
        ("TIMETRA-SERV-MIB", "svcTlsPriPortsCumulativeFactor"),
        ("TIMETRA-SERV-MIB", "svcTlsSecPortsCumulativeFactor"),
        ("TIMETRA-SERV-MIB", "svcTlsL2ptTermEnabled"),
        ("TIMETRA-SERV-MIB", "svcTlsPropagateMacFlush"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpMaxAttributes"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttributeCount"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpFailedRegisterCount"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpFloodTime"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrTblHighWatermark"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrTblLowWatermark"),
        ("TIMETRA-SERV-MIB", "svcTlsMcPathMgmtPlcyName"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpAdminQinqFixedTagVal"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsV6v0Group.setStatus("current")

tmnxSvcTlsFdbV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 103)
)
tmnxSvcTlsFdbV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsFdbMacAddr"),
        ("TIMETRA-SERV-MIB", "tlsFdbRowStatus"),
        ("TIMETRA-SERV-MIB", "tlsFdbType"),
        ("TIMETRA-SERV-MIB", "tlsFdbLocale"),
        ("TIMETRA-SERV-MIB", "tlsFdbPortId"),
        ("TIMETRA-SERV-MIB", "tlsFdbEncapValue"),
        ("TIMETRA-SERV-MIB", "tlsFdbSdpId"),
        ("TIMETRA-SERV-MIB", "tlsFdbVcId"),
        ("TIMETRA-SERV-MIB", "tlsFdbVpnId"),
        ("TIMETRA-SERV-MIB", "tlsFdbCustId"),
        ("TIMETRA-SERV-MIB", "tlsFdbLastStateChange"),
        ("TIMETRA-SERV-MIB", "tlsFdbProtected"),
        ("TIMETRA-SERV-MIB", "tlsFdbBackboneDstMac"),
        ("TIMETRA-SERV-MIB", "tlsFdbNumIVplsMac"),
        ("TIMETRA-SERV-MIB", "tlsFdbEndPointName"),
        ("TIMETRA-SERV-MIB", "tlsFdbEPMacOperSdpId"),
        ("TIMETRA-SERV-MIB", "tlsFdbEPMacOperVcId"),
        ("TIMETRA-SERV-MIB", "tlsFdbPbbNumEpipes"),
        ("TIMETRA-SERV-MIB", "tlsProtMacRowStatus"),
        ("TIMETRA-SERV-MIB", "tlsProtMacLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsFdbV6v0Group.setStatus("obsolete")

tmnxSvcIesIfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 104)
)
tmnxSvcIesIfV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "iesIfIndex"),
        ("TIMETRA-SERV-MIB", "iesIfRowStatus"),
        ("TIMETRA-SERV-MIB", "iesIfName"),
        ("TIMETRA-SERV-MIB", "iesIfDescription"),
        ("TIMETRA-SERV-MIB", "iesIfAdminStatus"),
        ("TIMETRA-SERV-MIB", "iesIfOperStatus"),
        ("TIMETRA-SERV-MIB", "iesIfLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "iesIfVpnId"),
        ("TIMETRA-SERV-MIB", "iesIfCustId"),
        ("TIMETRA-SERV-MIB", "iesIfLoopback"),
        ("TIMETRA-SERV-MIB", "iesIfLastStatusChange"),
        ("TIMETRA-SERV-MIB", "iesIfType"),
        ("TIMETRA-SERV-MIB", "iesIfShcvSource"),
        ("TIMETRA-SERV-MIB", "iesIfShcvAction"),
        ("TIMETRA-SERV-MIB", "iesIfShcvInterval"),
        ("TIMETRA-SERV-MIB", "iesGrpIfOperUpWhileEmpty"))
)
if mibBuilder.loadTexts:
    tmnxSvcIesIfV6v0Group.setStatus("current")

tmnxSvcTlsShgV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 105)
)
tmnxSvcTlsShgV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsShgRowStatus"),
        ("TIMETRA-SERV-MIB", "tlsShgCustId"),
        ("TIMETRA-SERV-MIB", "tlsShgInstanceId"),
        ("TIMETRA-SERV-MIB", "tlsShgDescription"),
        ("TIMETRA-SERV-MIB", "tlsShgLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "tlsShgResidential"),
        ("TIMETRA-SERV-MIB", "tlsShgRestProtSrcMac"),
        ("TIMETRA-SERV-MIB", "tlsShgRestUnprotDstMac"),
        ("TIMETRA-SERV-MIB", "tlsShgCreationOrigin"),
        ("TIMETRA-SERV-MIB", "tlsShgRestProtSrcMacAction"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsShgV6v0Group.setStatus("current")

tmnxSvcTlsMFibV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 106)
)
tmnxSvcTlsMFibV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsMFibFwdOrBlk"),
        ("TIMETRA-SERV-MIB", "tlsMFibSvcId"),
        ("TIMETRA-SERV-MIB", "tlsMFibStatsForwardedPkts"),
        ("TIMETRA-SERV-MIB", "tlsMFibStatsForwardedOctets"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsMFibV6v0Group.setStatus("current")

tmnxSvcRdntV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 107)
)
tmnxSvcRdntV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsRdntGrpRowStatus"),
        ("TIMETRA-SERV-MIB", "tlsRdntGrpDescription"),
        ("TIMETRA-SERV-MIB", "tlsRdntGrpLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "tlsRdntGrpMemberRowStatus"),
        ("TIMETRA-SERV-MIB", "tlsRdntGrpMemberLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxSvcRdntV6v0Group.setStatus("current")

tmnxSvcTlsMstiV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 108)
)
tmnxSvcTlsMstiV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsMstiRowStatus"),
        ("TIMETRA-SERV-MIB", "tlsMstiPriority"),
        ("TIMETRA-SERV-MIB", "tlsMstiLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "tlsMstiRegionalRoot"),
        ("TIMETRA-SERV-MIB", "tlsMstiIntRootCost"),
        ("TIMETRA-SERV-MIB", "tlsMstiRemainingHopCount"),
        ("TIMETRA-SERV-MIB", "tlsMstiRegionalRootPort"),
        ("TIMETRA-SERV-MIB", "tlsMstiMvplsRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsMstiV6v0Group.setStatus("current")

tmnxSvcTlsEgrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 109)
)
tmnxSvcTlsEgrV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsEgrMcGrpRowStatus"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpDescription"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpChainLimit"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpEncapType"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpDot1qEtherType"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpQinqEtherType"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpMacFilterId"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpIpFilterId"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpIpv6FilterId"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpQinqFixedTagPosition"),
        ("TIMETRA-SERV-MIB", "tlsEgrMcGrpOperQinqFixedTagVal"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsEgrV6v0Group.setStatus("current")

tmnxSvcDhcpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 110)
)
tmnxSvcDhcpV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpLseStateLocale"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePortId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateEncapValue"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSdpId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateVcId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateChAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRemainLseTime"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOption82"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePersistKey"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSubscrIdent"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSubProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSlaProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvOperState"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvChecks"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvReplies"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvReplyTime"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateClientId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateIAID"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateIAIDType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddrMaskLen"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRetailerSvcId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRetailerIf"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateAncpString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateFramedIpNetMaskTp"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateFramedIpNetMask"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBCastIpAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBCastIpAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDefaultRouterTp"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDefaultRouter"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryDnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryDns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryDnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryDns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSessionTimeout"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateServerLeaseStart"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateServerLastRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateServerLeaseEnd"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpServerAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpServerAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOriginSubscrId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOriginStrings"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOriginLeaseInfo"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpClientAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpClientAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateLeaseSplitActive"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateInterDestId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryNbnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryNbns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryNbnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryNbns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNextHopMacAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifySubIndent"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifySubProfile"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifySlaProfile"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateEvaluateState"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModInterDestId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifyAncpString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateForceRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpManagedRouteStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcDhcpV6v0Group.setStatus("obsolete")

tmnxSvcEndPointV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 111)
)
tmnxSvcEndPointV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcEndPointRowStatus"),
        ("TIMETRA-SERV-MIB", "svcEndPointDescription"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActiveType"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActivePortId"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActiveEncap"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActiveSdpId"),
        ("TIMETRA-SERV-MIB", "svcEndPointForceSwitchOver"),
        ("TIMETRA-SERV-MIB", "svcEndPointForceSwitchOverSdpId"),
        ("TIMETRA-SERV-MIB", "svcEndPointActiveHoldDelay"),
        ("TIMETRA-SERV-MIB", "svcEndPointIgnoreStandbySig"),
        ("TIMETRA-SERV-MIB", "svcEndPointMacPinning"),
        ("TIMETRA-SERV-MIB", "svcEndPointMacLimit"),
        ("TIMETRA-SERV-MIB", "svcEndPointSuppressStandbySig"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActiveChangeCount"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActiveLastChange"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActiveUpTime"),
        ("TIMETRA-SERV-MIB", "svcEndPointRevertTime"),
        ("TIMETRA-SERV-MIB", "svcEndPointRevertTimeCountDn"))
)
if mibBuilder.loadTexts:
    tmnxSvcEndPointV6v0Group.setStatus("current")

tmnxSvcPEV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 112)
)
tmnxSvcPEV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyRowStatus"),
        ("TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyPassword"),
        ("TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyInterval"),
        ("TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyTimeout"),
        ("TIMETRA-SERV-MIB", "svcPEDiscPolServerRowStatus"),
        ("TIMETRA-SERV-MIB", "svcPEDiscPolServerAddressType"),
        ("TIMETRA-SERV-MIB", "svcPEDiscPolServerAddress"),
        ("TIMETRA-SERV-MIB", "svcPEDiscPolServerSecret"),
        ("TIMETRA-SERV-MIB", "svcPEDiscPolServerOperStatus"),
        ("TIMETRA-SERV-MIB", "svcPEDiscPolServerPort"))
)
if mibBuilder.loadTexts:
    tmnxSvcPEV6v0Group.setStatus("current")

tmnxSvcIfDHCP6V6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 114)
)
tmnxSvcIfDHCP6V6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcIfDHCP6MsgStatsLstClrd"),
        ("TIMETRA-SERV-MIB", "svcIfDHCP6MsgStatsRcvd"),
        ("TIMETRA-SERV-MIB", "svcIfDHCP6MsgStatsSent"),
        ("TIMETRA-SERV-MIB", "svcIfDHCP6MsgStatsDropped"))
)
if mibBuilder.loadTexts:
    tmnxSvcIfDHCP6V6v0Group.setStatus("current")

tmnxSvcTlsBackbone6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 115)
)
tmnxSvcTlsBackbone6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsBackboneSrcMac"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneVplsSvcId"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneVplsSvcISID"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneOperSrcMac"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneOperVplsSvcISID"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneLDPMacFlush"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneVplsStp"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsBackbone6v0Group.setStatus("obsolete")

tmnxSvcTlsBgpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 116)
)
tmnxSvcTlsBgpV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsBgpADTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADRowStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVplsId"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiPrefix"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiRD"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADExportRteTarget"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy1"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy2"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy3"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy4"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy5"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADImportRteTarget"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy1"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy2"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy3"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy4"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy5"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADAdminStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsBgpV6v0Group.setStatus("obsolete")

tmnxSvcEpipeV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 117)
)
tmnxSvcEpipeV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcEpipePbbTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbRowStatus"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbLastChngd"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbBvplsSvcId"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbBvplsDstMac"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbSvcISID"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbOperState"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbFlooding"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbLastStatusChange"))
)
if mibBuilder.loadTexts:
    tmnxSvcEpipeV6v0Group.setStatus("current")

tmnxSvcTlsPipV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 118)
)
tmnxSvcTlsPipV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsPipStpPortState"),
        ("TIMETRA-SERV-MIB", "tlsPipStpPortRole"),
        ("TIMETRA-SERV-MIB", "tlsPipStpDesignatedBridge"),
        ("TIMETRA-SERV-MIB", "tlsPipStpDesignatedPort"),
        ("TIMETRA-SERV-MIB", "tlsPipStpException"),
        ("TIMETRA-SERV-MIB", "tlsPipStpForwardTransitions"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInConfigBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInTcnBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInRstBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInMstBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInBadBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOutConfigBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOutTcnBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOutRstBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOutMstBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOperStatus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpMvplsPruneState"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOperProtocol"),
        ("TIMETRA-SERV-MIB", "tlsPipStpPortNum"),
        ("TIMETRA-SERV-MIB", "tlsPipMstiPortRole"),
        ("TIMETRA-SERV-MIB", "tlsPipMstiPortState"),
        ("TIMETRA-SERV-MIB", "tlsPipMstiDesignatedBridge"),
        ("TIMETRA-SERV-MIB", "tlsPipMstiDesignatedPort"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsPipV6v0Group.setStatus("obsolete")

tmnxApipeV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 119)
)
tmnxApipeV3v0Group.setObjects(
    ("TIMETRA-SERV-MIB", "svcApipeInterworking")
)
if mibBuilder.loadTexts:
    tmnxApipeV3v0Group.setStatus("current")

tmnxSvcRoutedCOV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 120)
)
tmnxSvcRoutedCOV5v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "iesIfParentIf"),
        ("TIMETRA-SERV-MIB", "iesIfFwdServId"),
        ("TIMETRA-SERV-MIB", "iesIfFwdSubIf"),
        ("TIMETRA-SERV-MIB", "iesGrpIfRedInterface"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumStaticHosts"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumDynamicHosts"))
)
if mibBuilder.loadTexts:
    tmnxSvcRoutedCOV5v0Group.setStatus("obsolete")

tmnxSvcBsxV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 121)
)
tmnxSvcBsxV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpLseStateAppProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifyAppProfile"))
)
if mibBuilder.loadTexts:
    tmnxSvcBsxV6v0Group.setStatus("obsolete")

tmnxSvcTlsBackbone6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 122)
)
tmnxSvcTlsBackbone6v1Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsBackboneSrcMac"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneVplsSvcId"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneVplsSvcISID"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneOperSrcMac"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneOperVplsSvcISID"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneLDPMacFlush"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneLDPMacFlushNotMine"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneVplsStp"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsBackbone6v1Group.setStatus("current")

tmnxArpHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 130)
)
tmnxArpHostGroup.setObjects(
      *(("TIMETRA-SERV-MIB", "svcArpHostTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcArpHostLocale"),
        ("TIMETRA-SERV-MIB", "svcArpHostSapPortId"),
        ("TIMETRA-SERV-MIB", "svcArpHostSapEncapValue"),
        ("TIMETRA-SERV-MIB", "svcArpHostSdpId"),
        ("TIMETRA-SERV-MIB", "svcArpHostVcId"),
        ("TIMETRA-SERV-MIB", "svcArpHostSessionTimeout"),
        ("TIMETRA-SERV-MIB", "svcArpHostStart"),
        ("TIMETRA-SERV-MIB", "svcArpHostLastAuth"),
        ("TIMETRA-SERV-MIB", "svcArpHostRefresh"),
        ("TIMETRA-SERV-MIB", "svcArpHostRemainingTime"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvOperState"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvChecks"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvReplies"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvReplyTime"),
        ("TIMETRA-SERV-MIB", "svcArpHostSubscrIdent"),
        ("TIMETRA-SERV-MIB", "svcArpHostSubProfString"),
        ("TIMETRA-SERV-MIB", "svcArpHostSlaProfString"),
        ("TIMETRA-SERV-MIB", "svcArpHostAppProfString"),
        ("TIMETRA-SERV-MIB", "svcArpHostAncpString"),
        ("TIMETRA-SERV-MIB", "svcArpHostInterDestId"),
        ("TIMETRA-SERV-MIB", "svcArpHostRetailerSvcId"),
        ("TIMETRA-SERV-MIB", "svcArpHostRetailerIf"),
        ("TIMETRA-SERV-MIB", "svcArpHostMacAddr"),
        ("TIMETRA-SERV-MIB", "svcArpHostPersistKey"),
        ("TIMETRA-SERV-MIB", "svcArpHostCategoryMapName"),
        ("TIMETRA-SERV-MIB", "svcArpHostRadiusClassAttr"),
        ("TIMETRA-SERV-MIB", "svcArpHostRadiusUserName"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfTableLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfAdminState"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfMaxNumHosts"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfMaxNumHostsSap"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfMinAuthInterval"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfNumHosts"),
        ("TIMETRA-SERV-MIB", "svcArpHostDefaultSessionTimeout"),
        ("TIMETRA-SERV-MIB", "svcArpHostMRtStatus"))
)
if mibBuilder.loadTexts:
    tmnxArpHostGroup.setStatus("obsolete")

svcIgmpTrkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 131)
)
svcIgmpTrkGroup.setObjects(
      *(("TIMETRA-SERV-MIB", "svcIgmpTrkTableLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcIgmpTrkLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcIgmpTrkAdminState"),
        ("TIMETRA-SERV-MIB", "svcIgmpTrkExpiryTime"))
)
if mibBuilder.loadTexts:
    svcIgmpTrkGroup.setStatus("current")

svcTlsMacV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 132)
)
svcTlsMacV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsMacMoveNumRetries"),
        ("TIMETRA-SERV-MIB", "svcTlsMacSubNetLen"),
        ("TIMETRA-SERV-MIB", "svcTlsSendFlushOnBVplsFail"),
        ("TIMETRA-SERV-MIB", "svcTlsPropMacFlushFromBVpls"))
)
if mibBuilder.loadTexts:
    svcTlsMacV7v0Group.setStatus("current")

tmnxSvcRoutedCOV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 133)
)
tmnxSvcRoutedCOV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "iesIfParentIf"),
        ("TIMETRA-SERV-MIB", "iesIfFwdServId"),
        ("TIMETRA-SERV-MIB", "iesIfFwdSubIf"),
        ("TIMETRA-SERV-MIB", "iesGrpIfRedInterface"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumStaticHosts"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumDynamicHosts"),
        ("TIMETRA-SERV-MIB", "iesIfPrivateRetailSubnets"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumDhcpLeaseStates"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumPppoeSessions"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumArpHosts"))
)
if mibBuilder.loadTexts:
    tmnxSvcRoutedCOV7v0Group.setStatus("obsolete")

svcTlsEndPointV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 134)
)
svcTlsEndPointV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcEndPointMCEPId"),
        ("TIMETRA-SERV-MIB", "svcEndPointMCEPPeerAddr"),
        ("TIMETRA-SERV-MIB", "svcEndPointMCEPPeerAddrType"),
        ("TIMETRA-SERV-MIB", "svcEndPointMCEPPeerName"),
        ("TIMETRA-SERV-MIB", "svcEndPointMCEPPsvModeActive"),
        ("TIMETRA-SERV-MIB", "svcEndPointBlockOnMeshFail"),
        ("TIMETRA-SERV-MIB", "svcEpMcEpStatsPktsRxConfig"),
        ("TIMETRA-SERV-MIB", "svcEpMcEpStatsPktsRxState"),
        ("TIMETRA-SERV-MIB", "svcEpMcEpStatsPktsTxConfig"),
        ("TIMETRA-SERV-MIB", "svcEpMcEpStatsPktsTxFailed"),
        ("TIMETRA-SERV-MIB", "svcEpMcEpStatsPktsTxState"))
)
if mibBuilder.loadTexts:
    svcTlsEndPointV7v0Group.setStatus("current")

tmnxSvcIpipeV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 135)
)
tmnxSvcIpipeV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcIpipeInfoLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcIpipeCeAddressDiscovery"),
        ("TIMETRA-SERV-MIB", "svcIpipeInfoTableLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxSvcIpipeV7v0Group.setStatus("obsolete")

tmnxSvcDhcpBgpV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 136)
)
tmnxSvcDhcpBgpV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpPrngPlcyName"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpAuthKeyChain"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpMD5AuthKey"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpImportPolicy"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpExportPolicy"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpPeerAS"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpPeeringStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcDhcpBgpV7v0Group.setStatus("current")

tmnxSvcTlsPipV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 137)
)
tmnxSvcTlsPipV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsPipStpPortState"),
        ("TIMETRA-SERV-MIB", "tlsPipStpPortRole"),
        ("TIMETRA-SERV-MIB", "tlsPipStpDesignatedBridge"),
        ("TIMETRA-SERV-MIB", "tlsPipStpDesignatedPort"),
        ("TIMETRA-SERV-MIB", "tlsPipStpException"),
        ("TIMETRA-SERV-MIB", "tlsPipStpForwardTransitions"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInConfigBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInTcnBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInRstBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInMstBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInBadBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOutConfigBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOutTcnBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOutRstBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOutMstBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOperStatus"),
        ("TIMETRA-SERV-MIB", "tlsPipStpMvplsPruneState"),
        ("TIMETRA-SERV-MIB", "tlsPipStpOperProtocol"),
        ("TIMETRA-SERV-MIB", "tlsPipStpPortNum"),
        ("TIMETRA-SERV-MIB", "tlsPipMstiPortRole"),
        ("TIMETRA-SERV-MIB", "tlsPipMstiPortState"),
        ("TIMETRA-SERV-MIB", "tlsPipMstiDesignatedBridge"),
        ("TIMETRA-SERV-MIB", "tlsPipMstiDesignatedPort"),
        ("TIMETRA-SERV-MIB", "tlsPipStpInsideRegion"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsPipV7v0Group.setStatus("current")

tmnxArpHostBgpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 138)
)
tmnxArpHostBgpGroup.setObjects(
      *(("TIMETRA-SERV-MIB", "svcArpHostBgpPrngPlcyName"),
        ("TIMETRA-SERV-MIB", "svcArpHostBgpAuthKeyChain"),
        ("TIMETRA-SERV-MIB", "svcArpHostBgpMD5AuthKey"),
        ("TIMETRA-SERV-MIB", "svcArpHostBgpImportPolicy"),
        ("TIMETRA-SERV-MIB", "svcArpHostBgpExportPolicy"),
        ("TIMETRA-SERV-MIB", "svcArpHostBgpPeerAS"),
        ("TIMETRA-SERV-MIB", "svcArpHostBgpPeeringStatus"))
)
if mibBuilder.loadTexts:
    tmnxArpHostBgpGroup.setStatus("current")

tmnxSvcDhcpV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 139)
)
tmnxSvcDhcpV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpLseStateLocale"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePortId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateEncapValue"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSdpId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateVcId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateChAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRemainLseTime"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOption82"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePersistKey"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSubscrIdent"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSubProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSlaProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvOperState"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvChecks"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvReplies"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvReplyTime"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateClientId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateIAID"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateIAIDType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddrMaskLen"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRetailerSvcId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRetailerIf"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateAncpString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateFramedIpNetMaskTp"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateFramedIpNetMask"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBCastIpAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBCastIpAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDefaultRouterTp"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDefaultRouter"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryDnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryDns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryDnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryDns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSessionTimeout"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateServerLeaseStart"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateServerLastRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateServerLeaseEnd"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpServerAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpServerAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOriginSubscrId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOriginStrings"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOriginLeaseInfo"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpClientAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpClientAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateLeaseSplitActive"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateInterDestId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryNbnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryNbns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryNbnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryNbns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNextHopMacAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateCategoryMapName"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNakNextRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRadiusClassAttr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRadiusUserName"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifySubIndent"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifySubProfile"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifySlaProfile"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateEvaluateState"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModInterDestId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifyAncpString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateForceRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpManagedRouteStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcDhcpV7v0Group.setStatus("obsolete")

tmnxSvcPbbMacV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 140)
)
tmnxSvcPbbMacV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcEpipePbbBvplsDstMacName"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbBvplsOperDstMac"),
        ("TIMETRA-SERV-MIB", "svcMacNameAddr"),
        ("TIMETRA-SERV-MIB", "svcMacNameLastChngd"),
        ("TIMETRA-SERV-MIB", "svcMacNameRowStatus"),
        ("TIMETRA-SERV-MIB", "svcMacNameTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcPbbSrcBVplsMacAddr"),
        ("TIMETRA-SERV-MIB", "svcMacNotifCount"),
        ("TIMETRA-SERV-MIB", "svcMacNotifInterval"),
        ("TIMETRA-SERV-MIB", "svcTlsMacNotifAdminState"),
        ("TIMETRA-SERV-MIB", "svcTlsMacNotifCount"),
        ("TIMETRA-SERV-MIB", "svcTlsMacNotifInterval"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneUseSapBMac"),
        ("TIMETRA-SERV-MIB", "svcTlsPbbIgmpSnpgMRtrRowStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsPbbIgmpSnpgMRtrLastCh"))
)
if mibBuilder.loadTexts:
    tmnxSvcPbbMacV7v0Group.setStatus("current")

tmnxSvcTlsFdbV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 141)
)
tmnxSvcTlsFdbV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsFdbMacAddr"),
        ("TIMETRA-SERV-MIB", "tlsFdbRowStatus"),
        ("TIMETRA-SERV-MIB", "tlsFdbType"),
        ("TIMETRA-SERV-MIB", "tlsFdbLocale"),
        ("TIMETRA-SERV-MIB", "tlsFdbPortId"),
        ("TIMETRA-SERV-MIB", "tlsFdbEncapValue"),
        ("TIMETRA-SERV-MIB", "tlsFdbSdpId"),
        ("TIMETRA-SERV-MIB", "tlsFdbVcId"),
        ("TIMETRA-SERV-MIB", "tlsFdbVpnId"),
        ("TIMETRA-SERV-MIB", "tlsFdbCustId"),
        ("TIMETRA-SERV-MIB", "tlsFdbLastStateChange"),
        ("TIMETRA-SERV-MIB", "tlsFdbProtected"),
        ("TIMETRA-SERV-MIB", "tlsFdbBackboneDstMac"),
        ("TIMETRA-SERV-MIB", "tlsFdbNumIVplsMac"),
        ("TIMETRA-SERV-MIB", "tlsFdbEndPointName"),
        ("TIMETRA-SERV-MIB", "tlsFdbEPMacOperSdpId"),
        ("TIMETRA-SERV-MIB", "tlsFdbEPMacOperVcId"),
        ("TIMETRA-SERV-MIB", "tlsFdbPbbNumEpipes"),
        ("TIMETRA-SERV-MIB", "tlsProtMacRowStatus"),
        ("TIMETRA-SERV-MIB", "tlsProtMacLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "tlsProtMacImplCount"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsFdbV7v0Group.setStatus("current")

tmnxSvcV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 142)
)
tmnxSvcV7v0Group.setObjects(
    ("TIMETRA-SERV-MIB", "svcNumMcStandbySaps")
)
if mibBuilder.loadTexts:
    tmnxSvcV7v0Group.setStatus("current")

tmnxSvcV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 143)
)
tmnxSvcV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcName"),
        ("TIMETRA-SERV-MIB", "svcNameId"),
        ("TIMETRA-SERV-MIB", "svcNameRowStatus"),
        ("TIMETRA-SERV-MIB", "svcNameLastChanged"),
        ("TIMETRA-SERV-MIB", "svcNameTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcNameType"),
        ("TIMETRA-SERV-MIB", "svcEndPointStandbySigMaster"),
        ("TIMETRA-SERV-MIB", "svcTlsPerSvcHashing"),
        ("TIMETRA-SERV-MIB", "svcEpipePerSvcHashing"),
        ("TIMETRA-SERV-MIB", "svcTlsBackboneForceQTagFwd"),
        ("TIMETRA-SERV-MIB", "svcEpipeBackboneForceQTagFwd"),
        ("TIMETRA-SERV-MIB", "svcEpipeBackboneLastChngd"),
        ("TIMETRA-SERV-MIB", "svcEpipeBackboneTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcEpipeLastChngd"),
        ("TIMETRA-SERV-MIB", "svcEpipeTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcHashLabel"))
)
if mibBuilder.loadTexts:
    tmnxSvcV8v0Group.setStatus("current")

tmnxSvcMrpPolicyV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 144)
)
tmnxSvcMrpPolicyV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcMrpPlcyTableLastChgd"),
        ("TIMETRA-SERV-MIB", "svcMrpPlcyParamsTblLastChgd"),
        ("TIMETRA-SERV-MIB", "svcMrpPlcyParamsISIDTblLastChgd"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyRowStatus"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyLastChanged"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyDescription"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyScope"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyDefaultAction"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyParamsRowStatus"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyParamsLastChanged"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyParamsDescription"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyParamsAction"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyParamsISIDHigh"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyParamsISIDRowStatus"),
        ("TIMETRA-SERV-MIB", "svcMrpPolicyParamsISIDLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxSvcMrpPolicyV8v0Group.setStatus("current")

tmnxSvcSiteV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 145)
)
tmnxSvcSiteV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsSiteIdAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdEncapValue"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdPortId"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdRowStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdSdpBindId"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdShgMeshSdp"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdShgName"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdSiteId"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdFailedThresh"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdOperStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdDesignatedFwdr"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdDfUpTime"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdDfChgCnt"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcBgpVplsVeId"),
        ("TIMETRA-SERV-MIB", "svcBgpVplsVeName"),
        ("TIMETRA-SERV-MIB", "svcBgpVplsMaxVeId"),
        ("TIMETRA-SERV-MIB", "svcBgpVplsAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcBgpVplsLastChanged"),
        ("TIMETRA-SERV-MIB", "svcBgpVplsRowStatus"),
        ("TIMETRA-SERV-MIB", "svcBgpVplsTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpExportRteTarget"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpImportRteTarget"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiExportPolicy1"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiExportPolicy2"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiExportPolicy3"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiExportPolicy4"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiExportPolicy5"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiImportPolicy1"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiImportPolicy2"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiImportPolicy3"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiImportPolicy4"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiImportPolicy5"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpVsiRD"),
        ("TIMETRA-SERV-MIB", "tlsShgSiteName"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdBootTimer"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdSiteActTimer"),
        ("TIMETRA-SERV-MIB", "svcTlsSiteIdTimerRemain"))
)
if mibBuilder.loadTexts:
    tmnxSvcSiteV8v0Group.setStatus("current")

tmnxSvcRoutedCOV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 146)
)
tmnxSvcRoutedCOV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "iesIfParentIf"),
        ("TIMETRA-SERV-MIB", "iesIfFwdServId"),
        ("TIMETRA-SERV-MIB", "iesIfFwdSubIf"),
        ("TIMETRA-SERV-MIB", "iesGrpIfRedInterface"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumStaticHosts"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumDynamicHosts"),
        ("TIMETRA-SERV-MIB", "iesIfPrivateRetailSubnets"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumDhcpLeaseStates"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumPppoeSessions"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumArpHosts"),
        ("TIMETRA-SERV-MIB", "iesIfDelegatedPrefixLen"),
        ("TIMETRA-SERV-MIB", "iesIfLns"),
        ("TIMETRA-SERV-MIB", "iesIfDefaultPrimaryDnsIPv4Addr"),
        ("TIMETRA-SERV-MIB", "iesIfDefaultSecondaryDnsIPv4Addr"),
        ("TIMETRA-SERV-MIB", "iesIfDefaultPrimaryDnsIPv6Addr"),
        ("TIMETRA-SERV-MIB", "iesIfDefaultSecondaryDnsIPv6Addr"),
        ("TIMETRA-SERV-MIB", "iesIfIPv6ConfigAllowed"))
)
if mibBuilder.loadTexts:
    tmnxSvcRoutedCOV8v0Group.setStatus("obsolete")

tmnxArpHostV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 147)
)
tmnxArpHostV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcArpHostTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcArpHostLocale"),
        ("TIMETRA-SERV-MIB", "svcArpHostSapPortId"),
        ("TIMETRA-SERV-MIB", "svcArpHostSapEncapValue"),
        ("TIMETRA-SERV-MIB", "svcArpHostSdpId"),
        ("TIMETRA-SERV-MIB", "svcArpHostVcId"),
        ("TIMETRA-SERV-MIB", "svcArpHostSessionTimeout"),
        ("TIMETRA-SERV-MIB", "svcArpHostStart"),
        ("TIMETRA-SERV-MIB", "svcArpHostLastAuth"),
        ("TIMETRA-SERV-MIB", "svcArpHostRefresh"),
        ("TIMETRA-SERV-MIB", "svcArpHostRemainingTime"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvOperState"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvChecks"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvReplies"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvReplyTime"),
        ("TIMETRA-SERV-MIB", "svcArpHostSubscrIdent"),
        ("TIMETRA-SERV-MIB", "svcArpHostSubProfString"),
        ("TIMETRA-SERV-MIB", "svcArpHostSlaProfString"),
        ("TIMETRA-SERV-MIB", "svcArpHostAppProfString"),
        ("TIMETRA-SERV-MIB", "svcArpHostAncpString"),
        ("TIMETRA-SERV-MIB", "svcArpHostInterDestId"),
        ("TIMETRA-SERV-MIB", "svcArpHostRetailerSvcId"),
        ("TIMETRA-SERV-MIB", "svcArpHostRetailerIf"),
        ("TIMETRA-SERV-MIB", "svcArpHostMacAddr"),
        ("TIMETRA-SERV-MIB", "svcArpHostPersistKey"),
        ("TIMETRA-SERV-MIB", "svcArpHostCategoryMapName"),
        ("TIMETRA-SERV-MIB", "svcArpHostRadiusClassAttr"),
        ("TIMETRA-SERV-MIB", "svcArpHostRadiusUserName"),
        ("TIMETRA-SERV-MIB", "svcArpHostOriginSubscrId"),
        ("TIMETRA-SERV-MIB", "svcArpHostOriginStrings"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfTableLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfAdminState"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfMaxNumHosts"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfMaxNumHostsSap"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfMinAuthInterval"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfNumHosts"),
        ("TIMETRA-SERV-MIB", "svcArpHostDefaultSessionTimeout"),
        ("TIMETRA-SERV-MIB", "svcArpHostMRtStatus"))
)
if mibBuilder.loadTexts:
    tmnxArpHostV8v0Group.setStatus("obsolete")

tmnxSvcTlsBgpV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 148)
)
tmnxSvcTlsBgpV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsBgpADTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADRowStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVplsId"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiPrefix"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcL2MhRteDf"),
        ("TIMETRA-SERV-MIB", "svcL2MhRteState"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsBgpV8v0Group.setStatus("current")

tmnxSvcDhcpV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 150)
)
tmnxSvcDhcpV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpLeaseChAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseLocale"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeasePortId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseEncapValue"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseSdpId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseVcId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseRemainLseTime"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseOption82"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeasePersistKey"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseSubscrIdent"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseSubProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseSlaProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseShcvOperState"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseShcvChecks"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseShcvReplies"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseShcvReplyTime"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseClientId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseIAID"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseIAIDType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseCiAddrMaskLen"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseRetailerSvcId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseRetailerIf"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseAncpString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseFramedIpNetMaskTp"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseFramedIpNetMask"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseBCastIpAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseBCastIpAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseDefaultRouterTp"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseDefaultRouter"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeasePrimaryDnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeasePrimaryDns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseSecondaryDnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseSecondaryDns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseSessionTimeout"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseServerLeaseStart"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseServerLastRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseServerLeaseEnd"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseDhcpServerAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseDhcpServerAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseOriginSubscrId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseOriginStrings"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseOriginLeaseInfo"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseDhcpClientAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseDhcpClientAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseLeaseSplitActive"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseInterDestId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeasePrimaryNbnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeasePrimaryNbns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseSecondaryNbnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseSecondaryNbns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseCategoryMapName"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseNakNextRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseRadiusClassAttr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseRadiusUserName"),
        ("TIMETRA-SERV-MIB", "svcDhcpManagedRouteStatus"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseModifySubIndent"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseModifySubIndent"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseModifySubProfile"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseModifySlaProfile"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseEvaluateState"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseModInterDestId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseModifyAncpString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseForceRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseBgpPrngPlcyName"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseBgpAuthKeyChain"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseBgpMD5AuthKey"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseBgpImportPolicy"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseBgpExportPolicy"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseBgpPeerAS"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseBgpPeeringStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcDhcpV8v0Group.setStatus("current")

tmnxSvcBsxV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 151)
)
tmnxSvcBsxV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpLeaseAppProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseModifyAppProfile"))
)
if mibBuilder.loadTexts:
    tmnxSvcBsxV8v0Group.setStatus("current")

tmnxSvcTlsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 152)
)
tmnxSvcTlsV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsShcvRetryTimeout"),
        ("TIMETRA-SERV-MIB", "svcTlsShcvRetryCount"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsV7v0Group.setStatus("current")

tmnxSvcIesIfV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 153)
)
tmnxSvcIesIfV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "iesIfShcvRetryTimeout"),
        ("TIMETRA-SERV-MIB", "iesIfShcvRetryCount"))
)
if mibBuilder.loadTexts:
    tmnxSvcIesIfV7v0Group.setStatus("current")

tmnxSvcRoutedVplsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 154)
)
tmnxSvcRoutedVplsV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsAllowIpIfBinding"),
        ("TIMETRA-SERV-MIB", "iesIfVplsName"),
        ("TIMETRA-SERV-MIB", "iesIfVplsStatus"),
        ("TIMETRA-SERV-MIB", "iesIfVplsFailedReason"),
        ("TIMETRA-SERV-MIB", "iesIfSapEgressQosId"))
)
if mibBuilder.loadTexts:
    tmnxSvcRoutedVplsV8v0Group.setStatus("current")

tmnxSvcMvrpV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 155)
)
tmnxSvcMvrpV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTmplLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTmplMtu"),
        ("TIMETRA-SERV-MIB", "svcTmplRowStatus"),
        ("TIMETRA-SERV-MIB", "svcTmplTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTmplType"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupEnd"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupRowStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupSapTmplName"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupStart"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupSvcTmplName"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupMvrpControl"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupStartVlanTag"),
        ("TIMETRA-SERV-MIB", "svcTlsTempFloodTime"),
        ("TIMETRA-SERV-MIB", "svcTlsTempFloodActive"),
        ("TIMETRA-SERV-MIB", "svcTlsTempFloodChangeCount"),
        ("TIMETRA-SERV-MIB", "svcTmplSvcCount"),
        ("TIMETRA-SERV-MIB", "svcTmplUsed"),
        ("TIMETRA-SERV-MIB", "svcCtrlSvcId"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMvrpAttributeCount"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMmrpAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMmrpOperStatus"),
        ("TIMETRA-SERV-MIB", "svcTmplUserCreationOrigin"),
        ("TIMETRA-SERV-MIB", "svcTmplUserCreatorSvcId"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsDiscardUnknownDest"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsFdbLocalAgeTime"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsFdbRemoteAgeTime"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsFdbTableFullHighWMark"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsFdbTableFullLowWMark"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsFdbTableSize"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsMacAgeing"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsMacLearning"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsMacMoveAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsMacMoveMaxRate"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsMacMoveNumRetries"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsMacMoveRetryTimeout"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsPerSvcHashing"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsPriPortsCumFactor"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsSecPortsCumFactor"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsStpAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsStpBridgeForwardDelay"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsStpBridgeHelloTime"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsStpBridgeMaxAge"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsStpHoldCount"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsStpPriority"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsStpVersion"),
        ("TIMETRA-SERV-MIB", "svcTmplTlsTempFloodTime"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMvrpAttrTblHighWM"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMvrpAttrTblLowWM"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMvrpHoldTime"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMvrpMaxAttributes"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMvrpAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMvrpOperStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupOperStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupLastError"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMmrpDeclaredAttrCnt"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMmrpFailedRegCnt"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMmrpRegAttrCnt"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMvrpDeclaredAttrCnt"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMvrpFailedRegCnt"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMvrpRegAttrCnt"),
        ("TIMETRA-SERV-MIB", "svcTmplCustId"))
)
if mibBuilder.loadTexts:
    tmnxSvcMvrpV8v0Group.setStatus("current")

tmnxSvcIpipeV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 156)
)
tmnxSvcIpipeV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcIpipeInfoLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcIpipeCeAddressDiscovery"),
        ("TIMETRA-SERV-MIB", "svcIpipeInfoTableLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcIpipeIpv6CeAddressDiscovery"),
        ("TIMETRA-SERV-MIB", "svcIpipeStackCapabilitySignaling"))
)
if mibBuilder.loadTexts:
    tmnxSvcIpipeV8v0Group.setStatus("current")

tmnxSvcInterAsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 157)
)
tmnxSvcInterAsV8v0Group.setObjects(
    ("TIMETRA-SERV-MIB", "svcInterASMvpn")
)
if mibBuilder.loadTexts:
    tmnxSvcInterAsV8v0Group.setStatus("current")

tmnxSvcPwV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 158)
)
tmnxSvcPwV8v0Group.setObjects(
    ("TIMETRA-SERV-MIB", "svcEndPointStandbySigSlave")
)
if mibBuilder.loadTexts:
    tmnxSvcPwV8v0Group.setStatus("current")

tmnxSvcTlsPipV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 159)
)
tmnxSvcTlsPipV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsPipInTcBitBpdus"),
        ("TIMETRA-SERV-MIB", "tlsPipOutTcBitBpdus"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsPipV8v0Group.setStatus("current")

tmnxSvcIesIfV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 160)
)
tmnxSvcIesIfV8v0Group.setObjects(
    ("TIMETRA-SERV-MIB", "iesGrpIfPolicyControl")
)
if mibBuilder.loadTexts:
    tmnxSvcIesIfV8v0Group.setStatus("current")

tmnxSvcV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 161)
)
tmnxSvcV9v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcCreationOrigin"),
        ("TIMETRA-SERV-MIB", "svcMacFdbRecords"))
)
if mibBuilder.loadTexts:
    tmnxSvcV9v0Group.setStatus("current")

tmnxSvcMSPwPeV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 162)
)
tmnxSvcMSPwPeV9v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcMSPwPeAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeLastChange"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeRowStatus"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeFecType"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeAiiType"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeAgi"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeAutoConfig"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeEndPoint"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeStandbySigSlave"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeIsICB"),
        ("TIMETRA-SERV-MIB", "svcMSPwPePathName"),
        ("TIMETRA-SERV-MIB", "svcMSPwPePolicyId"),
        ("TIMETRA-SERV-MIB", "svcMSPwPePrecedence"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeRetryCount"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeRetryTimer"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeSaiiAcId"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeSaiiGlobalId"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeSaiiPrefix"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeSignaling"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeTaiiAcId"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeTaiiGlobalId"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeTaiiPrefix"),
        ("TIMETRA-SERV-MIB", "svcPwRtPathAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcPwRtPathHopAddr"),
        ("TIMETRA-SERV-MIB", "svcPwRtPathHopAddrType"),
        ("TIMETRA-SERV-MIB", "svcPwRtPathHopLastChange"),
        ("TIMETRA-SERV-MIB", "svcPwRtPathHopRowStatus"),
        ("TIMETRA-SERV-MIB", "svcPwRtPathHopTblLastChgd"),
        ("TIMETRA-SERV-MIB", "svcPwRtPathLastChange"),
        ("TIMETRA-SERV-MIB", "svcPwRtPathRowStatus"),
        ("TIMETRA-SERV-MIB", "svcPwRtPathTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcPwRtLclPrefixLastChange"),
        ("TIMETRA-SERV-MIB", "svcPwRtLclPrefixRowStatus"),
        ("TIMETRA-SERV-MIB", "svcPwRtLclPrefixTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcPwRtStaticRtLastChange"),
        ("TIMETRA-SERV-MIB", "svcPwRtStaticRtRowStatus"),
        ("TIMETRA-SERV-MIB", "svcPwRtStaticRtTblLastChgd"),
        ("TIMETRA-SERV-MIB", "svcPwSpeTaiiOperSdpBind1"),
        ("TIMETRA-SERV-MIB", "svcPwSpeTaiiOperSdpBind2"),
        ("TIMETRA-SERV-MIB", "svcPwSpeTaiiSvcId"),
        ("TIMETRA-SERV-MIB", "svcPwSpeTaiiSaiiAcId"),
        ("TIMETRA-SERV-MIB", "svcPwSpeTaiiSaiiGlobalId"),
        ("TIMETRA-SERV-MIB", "svcPwSpeTaiiSaiiPrefix"),
        ("TIMETRA-SERV-MIB", "svcPwSpeSaiiOperSdpBind1"),
        ("TIMETRA-SERV-MIB", "svcPwSpeSaiiOperSdpBind2"),
        ("TIMETRA-SERV-MIB", "svcPwSpeSaiiSvcId"),
        ("TIMETRA-SERV-MIB", "svcPwSpeSaiiTaiiAcId"),
        ("TIMETRA-SERV-MIB", "svcPwSpeSaiiTaiiGlobalId"),
        ("TIMETRA-SERV-MIB", "svcPwSpeSaiiTaiiPrefix"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeRetryRemain"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeTimeRemain"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeOperSdpBind"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActiveSdpFec"),
        ("TIMETRA-SERV-MIB", "svcPwRtSpeAddrGlobalId"),
        ("TIMETRA-SERV-MIB", "svcPwRtSpeAddrPrefix"),
        ("TIMETRA-SERV-MIB", "svcEndPointForceSwitchOvrSdpFec"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeRetryExpired"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeLastError"),
        ("TIMETRA-SERV-MIB", "svcPwRtBgpRoutes"),
        ("TIMETRA-SERV-MIB", "svcPwRtBootTimer"),
        ("TIMETRA-SERV-MIB", "svcPwRtHostRoutes"),
        ("TIMETRA-SERV-MIB", "svcPwRtLocalRoutes"),
        ("TIMETRA-SERV-MIB", "svcPwRtRetryCount"),
        ("TIMETRA-SERV-MIB", "svcPwRtRetryTimer"),
        ("TIMETRA-SERV-MIB", "svcPwRtStaticRoutes"),
        ("TIMETRA-SERV-MIB", "svcPwRtLclPfxRDCommunity"),
        ("TIMETRA-SERV-MIB", "svcPwRtLclPfxRDLastChange"),
        ("TIMETRA-SERV-MIB", "svcPwRtLclPfxRDRowStatus"),
        ("TIMETRA-SERV-MIB", "svcPwRtLclPfxRDTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcPwRtBootTimerRemain"))
)
if mibBuilder.loadTexts:
    tmnxSvcMSPwPeV9v0Group.setStatus("current")

tmnxSvcOperGrpV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 163)
)
tmnxSvcOperGrpV9v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsSiteIdMonitorOperGrp"),
        ("TIMETRA-SERV-MIB", "svcOperGrpCreationOrigin"),
        ("TIMETRA-SERV-MIB", "svcOperGrpHoldUpTime"),
        ("TIMETRA-SERV-MIB", "svcOperGrpHoldDownTime"),
        ("TIMETRA-SERV-MIB", "svcOperGrpNumMembers"),
        ("TIMETRA-SERV-MIB", "svcOperGrpNumMonitoring"),
        ("TIMETRA-SERV-MIB", "svcOperGrpLastChange"),
        ("TIMETRA-SERV-MIB", "svcOperGrpOperStatus"),
        ("TIMETRA-SERV-MIB", "svcOperGrpRowStatus"),
        ("TIMETRA-SERV-MIB", "svcOperGrpTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcOperGrpHoldUpTimeRemain"),
        ("TIMETRA-SERV-MIB", "svcOperGrpHoldDownTimeRemain"))
)
if mibBuilder.loadTexts:
    tmnxSvcOperGrpV9v0Group.setStatus("current")

tmnxSvcDhcpV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 164)
)
tmnxSvcDhcpV9v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpLeaseAleDatalink"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseAleEncaps1"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseAleEncaps2"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseOvrPIR"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseOvrCIR"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseOvrCBS"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseOvrMBS"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseOvrWrrWeight"))
)
if mibBuilder.loadTexts:
    tmnxSvcDhcpV9v0Group.setStatus("current")

tmnxSvcRoutedCOV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 165)
)
tmnxSvcRoutedCOV9v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "iesIfParentIf"),
        ("TIMETRA-SERV-MIB", "iesIfFwdServId"),
        ("TIMETRA-SERV-MIB", "iesIfFwdSubIf"),
        ("TIMETRA-SERV-MIB", "iesGrpIfRedInterface"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumStaticHosts"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumDynamicHosts"),
        ("TIMETRA-SERV-MIB", "iesIfPrivateRetailSubnets"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumDhcpLeaseStates"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumPppoeSessions"),
        ("TIMETRA-SERV-MIB", "svcWholesalerNumArpHosts"),
        ("TIMETRA-SERV-MIB", "iesIfDelegatedPrefixLen"),
        ("TIMETRA-SERV-MIB", "iesIfLns"),
        ("TIMETRA-SERV-MIB", "iesIfDefaultPrimaryDnsIPv4Addr"),
        ("TIMETRA-SERV-MIB", "iesIfDefaultSecondaryDnsIPv4Addr"),
        ("TIMETRA-SERV-MIB", "iesIfDefaultPrimaryDnsIPv6Addr"),
        ("TIMETRA-SERV-MIB", "iesIfDefaultSecondaryDnsIPv6Addr"),
        ("TIMETRA-SERV-MIB", "iesIfIPv6ConfigAllowed"),
        ("TIMETRA-SERV-MIB", "iesIfSrrpRoutingEnabled"),
        ("TIMETRA-SERV-MIB", "iesIfSrrpRoutingHoldTime"),
        ("TIMETRA-SERV-MIB", "iesIfAllowUnmatchingSubnets"))
)
if mibBuilder.loadTexts:
    tmnxSvcRoutedCOV9v0Group.setStatus("current")

tmnxSvcV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 166)
)
tmnxSvcV9v0R4Group.setObjects(
      *(("TIMETRA-SERV-MIB", "iesIfMonitorOperGrp"),
        ("TIMETRA-SERV-MIB", "svcTlsExtMmrpEndStationOnly"))
)
if mibBuilder.loadTexts:
    tmnxSvcV9v0R4Group.setStatus("current")

tmnxSvcMacReNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 167)
)
tmnxSvcMacReNotifyGroup.setObjects(
    ("TIMETRA-SERV-MIB", "svcTlsExtMacReNotifInterval")
)
if mibBuilder.loadTexts:
    tmnxSvcMacReNotifyGroup.setStatus("current")

tmnxSvcDhcpV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 170)
)
tmnxSvcDhcpV10v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpLeaseWppState"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseWppPortalRouter"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseWppPortalName"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeasePoolName"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseServerId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseInterfaceId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseRemoteId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseOption60"),
        ("TIMETRA-SERV-MIB", "svcDhcpLeaseRadCalledStationId"))
)
if mibBuilder.loadTexts:
    tmnxSvcDhcpV10v0Group.setStatus("current")

tmnxSvcRoutedCOV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 171)
)
tmnxSvcRoutedCOV10v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "iesIfGroupInterfaceType"),
        ("TIMETRA-SERV-MIB", "svcIfSapCfgTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcIfSapCfgLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcIfSapCfgDescription"),
        ("TIMETRA-SERV-MIB", "svcIfSapCfgDefSubProfile"),
        ("TIMETRA-SERV-MIB", "svcIfSapCfgDefSlaProfile"),
        ("TIMETRA-SERV-MIB", "svcIfSapCfgDefAppProfile"),
        ("TIMETRA-SERV-MIB", "svcIfSapCfgSubIdentPolicy"),
        ("TIMETRA-SERV-MIB", "svcIfSapCfgDefSubIdent"),
        ("TIMETRA-SERV-MIB", "svcIfSapCfgDefSubIdentString"),
        ("TIMETRA-SERV-MIB", "svcIfSapCfgDefFilterProfile"))
)
if mibBuilder.loadTexts:
    tmnxSvcRoutedCOV10v0Group.setStatus("current")

tmnxSvcV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 172)
)
tmnxSvcV10v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcEndPointRestProtSrcMac"),
        ("TIMETRA-SERV-MIB", "svcEndPointRestProtSrcMacAction"),
        ("TIMETRA-SERV-MIB", "svcEndPointAutoLearnMacProtect"),
        ("TIMETRA-SERV-MIB", "tlsShgAutoLearnMacProtect"),
        ("TIMETRA-SERV-MIB", "custMssIngQosArbitStatsFwdPkts"),
        ("TIMETRA-SERV-MIB", "custMssIngQosArbitStatsFwdPktsLo"),
        ("TIMETRA-SERV-MIB", "custMssIngQosArbitStatsFwdPktsHi"),
        ("TIMETRA-SERV-MIB", "custMssIngQosArbitStatsFwdOcts"),
        ("TIMETRA-SERV-MIB", "custMssIngQosArbitStatsFwdOctsLo"),
        ("TIMETRA-SERV-MIB", "custMssIngQosArbitStatsFwdOctsHi"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosArbitStatsFwdPkts"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosArbitStatsFwdPktsLo"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosArbitStatsFwdPktsHi"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosArbitStatsFwdOcts"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosArbitStatsFwdOctsLo"),
        ("TIMETRA-SERV-MIB", "custMssEgrQosArbitStatsFwdOctsHi"),
        ("TIMETRA-SERV-MIB", "custIngQosPortIdArbitFwdPkts"),
        ("TIMETRA-SERV-MIB", "custIngQosPortIdArbitFwdPktsLo"),
        ("TIMETRA-SERV-MIB", "custIngQosPortIdArbitFwdPktsHi"),
        ("TIMETRA-SERV-MIB", "custIngQosPortIdArbitFwdOcts"),
        ("TIMETRA-SERV-MIB", "custIngQosPortIdArbitFwdOctsLo"),
        ("TIMETRA-SERV-MIB", "custIngQosPortIdArbitFwdOctsHi"),
        ("TIMETRA-SERV-MIB", "custEgrQosPortIdArbitFwdPkts"),
        ("TIMETRA-SERV-MIB", "custEgrQosPortIdArbitFwdPktsLo"),
        ("TIMETRA-SERV-MIB", "custEgrQosPortIdArbitFwdPktsHi"),
        ("TIMETRA-SERV-MIB", "custEgrQosPortIdArbitFwdOcts"),
        ("TIMETRA-SERV-MIB", "custEgrQosPortIdArbitFwdOctsLo"),
        ("TIMETRA-SERV-MIB", "custEgrQosPortIdArbitFwdOctsHi"))
)
if mibBuilder.loadTexts:
    tmnxSvcV10v0Group.setStatus("current")

tmnxSvcIesIfV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 173)
)
tmnxSvcIesIfV10v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "iesIfShcvFamily"),
        ("TIMETRA-SERV-MIB", "iesIfIPv6IpoeBridgedModeEnabled"),
        ("TIMETRA-SERV-MIB", "iesIfIPv6AllowUnmatchingPfxs"))
)
if mibBuilder.loadTexts:
    tmnxSvcIesIfV10v0Group.setStatus("current")

tmnxArpHostV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 174)
)
tmnxArpHostV10v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcArpHostTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcArpHostLocale"),
        ("TIMETRA-SERV-MIB", "svcArpHostSapPortId"),
        ("TIMETRA-SERV-MIB", "svcArpHostSapEncapValue"),
        ("TIMETRA-SERV-MIB", "svcArpHostSdpId"),
        ("TIMETRA-SERV-MIB", "svcArpHostVcId"),
        ("TIMETRA-SERV-MIB", "svcArpHostSessionTimeout"),
        ("TIMETRA-SERV-MIB", "svcArpHostStart"),
        ("TIMETRA-SERV-MIB", "svcArpHostLastAuth"),
        ("TIMETRA-SERV-MIB", "svcArpHostRefresh"),
        ("TIMETRA-SERV-MIB", "svcArpHostRemainingTime"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvOperState"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvChecks"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvReplies"),
        ("TIMETRA-SERV-MIB", "svcArpHostShcvReplyTime"),
        ("TIMETRA-SERV-MIB", "svcArpHostSubscrIdent"),
        ("TIMETRA-SERV-MIB", "svcArpHostSubProfString"),
        ("TIMETRA-SERV-MIB", "svcArpHostSlaProfString"),
        ("TIMETRA-SERV-MIB", "svcArpHostAppProfString"),
        ("TIMETRA-SERV-MIB", "svcArpHostAncpString"),
        ("TIMETRA-SERV-MIB", "svcArpHostInterDestId"),
        ("TIMETRA-SERV-MIB", "svcArpHostRetailerSvcId"),
        ("TIMETRA-SERV-MIB", "svcArpHostRetailerIf"),
        ("TIMETRA-SERV-MIB", "svcArpHostMacAddr"),
        ("TIMETRA-SERV-MIB", "svcArpHostPersistKey"),
        ("TIMETRA-SERV-MIB", "svcArpHostCategoryMapName"),
        ("TIMETRA-SERV-MIB", "svcArpHostRadiusClassAttr"),
        ("TIMETRA-SERV-MIB", "svcArpHostRadiusUserName"),
        ("TIMETRA-SERV-MIB", "svcArpHostOriginSubscrId"),
        ("TIMETRA-SERV-MIB", "svcArpHostOriginStrings"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfTableLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfLastMgmtChange"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfAdminState"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfMaxNumHosts"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfMaxNumHostsSap"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfMinAuthInterval"),
        ("TIMETRA-SERV-MIB", "svcArpHostIfNumHosts"),
        ("TIMETRA-SERV-MIB", "svcArpHostDefaultSessionTimeout"),
        ("TIMETRA-SERV-MIB", "svcArpHostMRtStatus"),
        ("TIMETRA-SERV-MIB", "svcArpHostOvrPIR"),
        ("TIMETRA-SERV-MIB", "svcArpHostOvrCIR"),
        ("TIMETRA-SERV-MIB", "svcArpHostOvrCBS"),
        ("TIMETRA-SERV-MIB", "svcArpHostOvrMBS"),
        ("TIMETRA-SERV-MIB", "svcArpHostOvrWrrWeight"))
)
if mibBuilder.loadTexts:
    tmnxArpHostV10v0Group.setStatus("current")

tmnxSvcIesIfNHV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 176)
)
tmnxSvcIesIfNHV10v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "iesIfIsaTnlNHTableLastChanged"),
        ("TIMETRA-SERV-MIB", "iesIfIsaTnlNHLastChanged"),
        ("TIMETRA-SERV-MIB", "iesIfIsaTnlNHStaticAddrType"),
        ("TIMETRA-SERV-MIB", "iesIfIsaTnlNHStaticAddr"),
        ("TIMETRA-SERV-MIB", "iesIfIsaTnlNHDynAddrType"),
        ("TIMETRA-SERV-MIB", "iesIfIsaTnlNHDynAddr"))
)
if mibBuilder.loadTexts:
    tmnxSvcIesIfNHV10v0Group.setStatus("current")

tmnxSvcNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 200)
)
tmnxSvcNotifyObjsV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpRestoreLseStateCiAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpRestoreLseStateProblem"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOldCiAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOldChAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNewCiAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNewChAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpClientLease"),
        ("TIMETRA-SERV-MIB", "svcDhcpPacketProblem"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePopulateError"),
        ("TIMETRA-SERV-MIB", "hostConnectivityCiAddrType"),
        ("TIMETRA-SERV-MIB", "hostConnectivityCiAddr"),
        ("TIMETRA-SERV-MIB", "hostConnectivityChAddr"),
        ("TIMETRA-SERV-MIB", "protectedMacForNotify"),
        ("TIMETRA-SERV-MIB", "staticHostDynamicMacIpAddress"),
        ("TIMETRA-SERV-MIB", "staticHostDynamicMacConflict"),
        ("TIMETRA-SERV-MIB", "tmnxSvcObjRow"),
        ("TIMETRA-SERV-MIB", "tmnxSvcObjRowDescr"),
        ("TIMETRA-SERV-MIB", "tmnxSvcObjTodSuite"),
        ("TIMETRA-SERV-MIB", "tmnxFailureDescription"),
        ("TIMETRA-SERV-MIB", "svcDhcpProxyError"),
        ("TIMETRA-SERV-MIB", "svcDhcpCoAError"),
        ("TIMETRA-SERV-MIB", "svcDhcpSubAuthError"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrRegFailedReason"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrType"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrValue"),
        ("TIMETRA-SERV-MIB", "svcMstiInstanceId"),
        ("TIMETRA-SERV-MIB", "tmnxCustomerBridgeId"),
        ("TIMETRA-SERV-MIB", "tmnxCustomerRootBridgeId"),
        ("TIMETRA-SERV-MIB", "tmnxOtherBridgeId"),
        ("TIMETRA-SERV-MIB", "tmnxOldSdpBindTlsStpPortState"),
        ("TIMETRA-SERV-MIB", "tmnxVcpState"),
        ("TIMETRA-SERV-MIB", "macPinningMacAddress"),
        ("TIMETRA-SERV-MIB", "macPinningPinnedRow"),
        ("TIMETRA-SERV-MIB", "macPinningPinnedRowDescr"),
        ("TIMETRA-SERV-MIB", "macPinningViolatingRow"),
        ("TIMETRA-SERV-MIB", "macPinningViolatingRowDescr"))
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyObjsV6v0Group.setStatus("obsolete")

tmnxArpHostNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 201)
)
tmnxArpHostNotifyObjsGroup.setObjects(
      *(("TIMETRA-SERV-MIB", "svcNotifSapPortId"),
        ("TIMETRA-SERV-MIB", "svcNotifSapEncapValue"),
        ("TIMETRA-SERV-MIB", "svcArpHostPopulateError"))
)
if mibBuilder.loadTexts:
    tmnxArpHostNotifyObjsGroup.setStatus("current")

tmnxSvcNotifyObjsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 202)
)
tmnxSvcNotifyObjsV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpRestoreLseStateCiAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpRestoreLseStateProblem"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOldCiAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOldChAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNewCiAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNewChAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpClientLease"),
        ("TIMETRA-SERV-MIB", "svcDhcpPacketProblem"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePopulateError"),
        ("TIMETRA-SERV-MIB", "hostConnectivityCiAddrType"),
        ("TIMETRA-SERV-MIB", "hostConnectivityCiAddr"),
        ("TIMETRA-SERV-MIB", "hostConnectivityChAddr"),
        ("TIMETRA-SERV-MIB", "protectedMacForNotify"),
        ("TIMETRA-SERV-MIB", "staticHostDynamicMacIpAddress"),
        ("TIMETRA-SERV-MIB", "staticHostDynamicMacConflict"),
        ("TIMETRA-SERV-MIB", "tmnxSvcObjRow"),
        ("TIMETRA-SERV-MIB", "tmnxSvcObjRowDescr"),
        ("TIMETRA-SERV-MIB", "tmnxSvcObjTodSuite"),
        ("TIMETRA-SERV-MIB", "tmnxFailureDescription"),
        ("TIMETRA-SERV-MIB", "svcDhcpProxyError"),
        ("TIMETRA-SERV-MIB", "svcDhcpCoAError"),
        ("TIMETRA-SERV-MIB", "svcDhcpSubAuthError"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrRegFailedReason"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrType"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrValue"),
        ("TIMETRA-SERV-MIB", "svcMstiInstanceId"),
        ("TIMETRA-SERV-MIB", "tmnxCustomerBridgeId"),
        ("TIMETRA-SERV-MIB", "tmnxCustomerRootBridgeId"),
        ("TIMETRA-SERV-MIB", "tmnxOtherBridgeId"),
        ("TIMETRA-SERV-MIB", "tmnxOldSdpBindTlsStpPortState"),
        ("TIMETRA-SERV-MIB", "tmnxVcpState"),
        ("TIMETRA-SERV-MIB", "macPinningMacAddress"),
        ("TIMETRA-SERV-MIB", "macPinningPinnedRow"),
        ("TIMETRA-SERV-MIB", "macPinningPinnedRowDescr"),
        ("TIMETRA-SERV-MIB", "macPinningViolatingRow"),
        ("TIMETRA-SERV-MIB", "macPinningViolatingRowDescr"),
        ("TIMETRA-SERV-MIB", "svcHostAddrType"),
        ("TIMETRA-SERV-MIB", "svcHostAddr"))
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyObjsV7v0Group.setStatus("current")

tmnxSvcObsoletedV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 300)
)
tmnxSvcObsoletedV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsStpHoldTime"),
        ("TIMETRA-SERV-MIB", "tlsMFibInfoFwdOrBlk"),
        ("TIMETRA-SERV-MIB", "tlsMFibInfoSvcId"),
        ("TIMETRA-SERV-MIB", "tlsMFibGrpSrcStatsForwardedPkts"),
        ("TIMETRA-SERV-MIB", "tlsMFibGrpSrcStatsForwardedOctets"),
        ("TIMETRA-SERV-MIB", "tlsDHCPClientLease"),
        ("TIMETRA-SERV-MIB", "tlsDhcpLseStateOldCiAddr"),
        ("TIMETRA-SERV-MIB", "tlsDhcpLseStateOldChAddr"),
        ("TIMETRA-SERV-MIB", "tlsDhcpLseStateNewCiAddr"),
        ("TIMETRA-SERV-MIB", "tlsDhcpLseStateNewChAddr"),
        ("TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateCiAddr"),
        ("TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateSvcId"),
        ("TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStatePortId"),
        ("TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateEncapVal"),
        ("TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateProblem"),
        ("TIMETRA-SERV-MIB", "tlsDhcpPacketProblem"),
        ("TIMETRA-SERV-MIB", "tlsDhcpLseStatePopulateError"))
)
if mibBuilder.loadTexts:
    tmnxSvcObsoletedV6v0Group.setStatus("current")

tmnxSvcObsoletedV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 301)
)
tmnxSvcObsoletedV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsBgpADVsiRD"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADExportRteTarget"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy1"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy2"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy3"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy4"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy5"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADImportRteTarget"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy1"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy2"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy3"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy4"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy5"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateLocale"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePortId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateEncapValue"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSdpId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateVcId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateChAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRemainLseTime"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOption82"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePersistKey"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSubscrIdent"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSubProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSlaProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvOperState"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvChecks"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvReplies"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateShcvReplyTime"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateClientId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateIAID"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateIAIDType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddrMaskLen"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRetailerSvcId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRetailerIf"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateAncpString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateFramedIpNetMaskTp"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateFramedIpNetMask"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBCastIpAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBCastIpAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDefaultRouterTp"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDefaultRouter"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryDnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryDns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryDnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryDns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSessionTimeout"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateServerLeaseStart"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateServerLastRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateServerLeaseEnd"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpServerAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpServerAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOriginSubscrId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOriginStrings"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateOriginLeaseInfo"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpClientAddrType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpClientAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateLeaseSplitActive"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateInterDestId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryNbnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryNbns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryNbnsType"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryNbns"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNextHopMacAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateCategoryMapName"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateNakNextRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRadiusClassAttr"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateRadiusUserName"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifySubIndent"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifySubProfile"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifySlaProfile"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateEvaluateState"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModInterDestId"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifyAncpString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateForceRenew"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateAppProfString"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateModifyAppProfile"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpPrngPlcyName"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpAuthKeyChain"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpMD5AuthKey"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpImportPolicy"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpExportPolicy"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpPeerAS"),
        ("TIMETRA-SERV-MIB", "svcDhcpLseStateBgpPeeringStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcObsoletedV8v0Group.setStatus("current")

tmnxSvcObsoletedV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 302)
)
tmnxSvcObsoletedV9v0Group.setObjects(
    ("TIMETRA-SERV-MIB", "iesIfVpnId")
)
if mibBuilder.loadTexts:
    tmnxSvcObsoletedV9v0Group.setStatus("current")

tmnxSvcEthCfmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 407)
)
tmnxSvcEthCfmGroup.setObjects(
      *(("TIMETRA-SERV-MIB", "svcEthCfmTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcEthCfmTunnelFaultNotification"),
        ("TIMETRA-SERV-MIB", "svcEthCfmVMepExtensions"))
)
if mibBuilder.loadTexts:
    tmnxSvcEthCfmGroup.setStatus("current")

tmnxSvcApipeInfoV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 409)
)
tmnxSvcApipeInfoV9v0Group.setObjects(
    ("TIMETRA-SERV-MIB", "svcApipeSignaledVllTypeOverride")
)
if mibBuilder.loadTexts:
    tmnxSvcApipeInfoV9v0Group.setStatus("current")

tmnxSvcSpbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 410)
)
tmnxSvcSpbGroup.setObjects(
      *(("TIMETRA-SERV-MIB", "svcSpbIfEncapValue"),
        ("TIMETRA-SERV-MIB", "svcSpbIfLocale"),
        ("TIMETRA-SERV-MIB", "svcSpbIfPortId"),
        ("TIMETRA-SERV-MIB", "svcSpbIfSdpId"),
        ("TIMETRA-SERV-MIB", "svcSpbIfVcId"),
        ("TIMETRA-SERV-MIB", "svcSpbIfSvcId"),
        ("TIMETRA-SERV-MIB", "svcSpbIfIsisInstance"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbMEncapValue"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbMLocale"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbMPortId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbMSdpId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbMState"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbMVcId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbMEncapValue"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbMLocale"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbMPortId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbMSdpId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbMVcId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidMFibIsid"),
        ("TIMETRA-SERV-MIB", "tlsSpbMFibState"),
        ("TIMETRA-SERV-MIB", "tlsSpbMFibIsid"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbEncapValue"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbLocale"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbPortId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbSdpId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbState"),
        ("TIMETRA-SERV-MIB", "tlsSpbFdbVcId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbEncapValue"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbLocale"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbPortId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbSdpId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbVcId"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbLastUpdate"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidFdbMLastUpdate"),
        ("TIMETRA-SERV-MIB", "tlsSpbFidMFibLastUpdate"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbUserSvcLastUpdate"),
        ("TIMETRA-SERV-MIB", "svcTlsExtSpbmCtrlVpls"),
        ("TIMETRA-SERV-MIB", "svcTlsExtSpbmFid"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbFid"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbIsisInstance"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbRowStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbL1BridgePriority"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbL1FwdTreeTopoUcast"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbL1FwdTreeTopoMcast"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbL1BridgeId"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbL1McastDesigBridgeId"),
        ("TIMETRA-SERV-MIB", "svcTlsSpbAdminState"))
)
if mibBuilder.loadTexts:
    tmnxSvcSpbGroup.setStatus("current")

tmnxSvcVllBgpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 411)
)
tmnxSvcVllBgpGroup.setObjects(
      *(("TIMETRA-SERV-MIB", "svcVllBgpExportRteTarget"),
        ("TIMETRA-SERV-MIB", "svcVllBgpImportRteTarget"),
        ("TIMETRA-SERV-MIB", "svcVllBgpLastChanged"),
        ("TIMETRA-SERV-MIB", "svcVllBgpTableLastChanged"),
        ("TIMETRA-SERV-MIB", "svcVllBgpVsiRD"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdBootTimer"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdDesignatedFwdr"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdDfChgCnt"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdDfUpTime"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdEncapValue"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdLastChanged"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdOperStatus"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdPortId"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdRowStatus"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdSiteActTimer"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdSiteId"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdTblLastChanged"),
        ("TIMETRA-SERV-MIB", "svcVllSiteIdTimerRemain"),
        ("TIMETRA-SERV-MIB", "svcVllBgpRowStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsBgpRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcVllBgpGroup.setStatus("current")

tmnxSvcP2mpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 412)
)
tmnxSvcP2mpGroup.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsIPmsiAdminState"),
        ("TIMETRA-SERV-MIB", "svcTlsIPmsiDataDelayIntvl"),
        ("TIMETRA-SERV-MIB", "svcTlsIPmsiRemainDataDelayIntvl"),
        ("TIMETRA-SERV-MIB", "svcTlsIPmsiType"),
        ("TIMETRA-SERV-MIB", "svcTlsIPmsiRootAndLeaf"),
        ("TIMETRA-SERV-MIB", "svcTlsIPmsiLspTmpl"),
        ("TIMETRA-SERV-MIB", "svcTlsIPmsiLspName"),
        ("TIMETRA-SERV-MIB", "svcTlsPmsiLastChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsPmsiRowStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsPmsiTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxSvcP2mpGroup.setStatus("current")


# Notification objects

custCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 1, 0, 1)
)
custCreated.setObjects(
    ("TIMETRA-SERV-MIB", "custId")
)
if mibBuilder.loadTexts:
    custCreated.setStatus(
        "obsolete"
    )

custDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 1, 0, 2)
)
custDeleted.setObjects(
    ("TIMETRA-SERV-MIB", "custId")
)
if mibBuilder.loadTexts:
    custDeleted.setStatus(
        "obsolete"
    )

custMultSvcSiteCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 1, 0, 3)
)
custMultSvcSiteCreated.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteName"))
)
if mibBuilder.loadTexts:
    custMultSvcSiteCreated.setStatus(
        "obsolete"
    )

custMultSvcSiteDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 1, 0, 4)
)
custMultSvcSiteDeleted.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteName"))
)
if mibBuilder.loadTexts:
    custMultSvcSiteDeleted.setStatus(
        "obsolete"
    )

svcCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 1)
)
svcCreated.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SERV-MIB", "svcType"))
)
if mibBuilder.loadTexts:
    svcCreated.setStatus(
        "obsolete"
    )

svcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 2)
)
svcDeleted.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcDeleted.setStatus(
        "obsolete"
    )

svcStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 3)
)
svcStatusChanged.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SERV-MIB", "svcAdminStatus"),
        ("TIMETRA-SERV-MIB", "svcOperStatus"))
)
if mibBuilder.loadTexts:
    svcStatusChanged.setStatus(
        "current"
    )

svcTlsFdbTableFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 4)
)
svcTlsFdbTableFullAlarmRaised.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsFdbTableFullAlarmRaised.setStatus(
        "current"
    )

svcTlsFdbTableFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 5)
)
svcTlsFdbTableFullAlarmCleared.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsFdbTableFullAlarmCleared.setStatus(
        "current"
    )

iesIfCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 6)
)
iesIfCreated.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SERV-MIB", "iesIfIndex"))
)
if mibBuilder.loadTexts:
    iesIfCreated.setStatus(
        "obsolete"
    )

iesIfDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 7)
)
iesIfDeleted.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SERV-MIB", "iesIfIndex"))
)
if mibBuilder.loadTexts:
    iesIfDeleted.setStatus(
        "obsolete"
    )

iesIfStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 8)
)
iesIfStatusChanged.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SERV-MIB", "iesIfIndex"),
        ("TIMETRA-SERV-MIB", "iesIfAdminStatus"),
        ("TIMETRA-SERV-MIB", "iesIfOperStatus"))
)
if mibBuilder.loadTexts:
    iesIfStatusChanged.setStatus(
        "current"
    )

svcTlsMfibTableFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 9)
)
svcTlsMfibTableFullAlarmRaised.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsMfibTableFullAlarmRaised.setStatus(
        "current"
    )

svcTlsMfibTableFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 10)
)
svcTlsMfibTableFullAlarmCleared.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsMfibTableFullAlarmCleared.setStatus(
        "current"
    )

svcTlsMacPinningViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 11)
)
svcTlsMacPinningViolation.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SERV-MIB", "macPinningMacAddress"),
        ("TIMETRA-SERV-MIB", "macPinningPinnedRow"),
        ("TIMETRA-SERV-MIB", "macPinningPinnedRowDescr"),
        ("TIMETRA-SERV-MIB", "macPinningViolatingRow"),
        ("TIMETRA-SERV-MIB", "macPinningViolatingRowDescr"))
)
if mibBuilder.loadTexts:
    svcTlsMacPinningViolation.setStatus(
        "current"
    )

svcTlsDHCPLseStRestoreProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 12)
)
svcTlsDHCPLseStRestoreProblem.setObjects(
      *(("TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateSvcId"),
        ("TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStatePortId"),
        ("TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateEncapVal"),
        ("TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateCiAddr"),
        ("TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateProblem"))
)
if mibBuilder.loadTexts:
    svcTlsDHCPLseStRestoreProblem.setStatus(
        "obsolete"
    )

svcTlsDHCPLseStatePopulateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 13)
)
svcTlsDHCPLseStatePopulateErr.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "tlsDhcpLseStatePopulateError"))
)
if mibBuilder.loadTexts:
    svcTlsDHCPLseStatePopulateErr.setStatus(
        "obsolete"
    )

svcDHCPLseStateRestoreProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 14)
)
svcDHCPLseStateRestoreProblem.setObjects(
      *(("TIMETRA-SERV-MIB", "svcDhcpRestoreLseStateCiAddr"),
        ("TIMETRA-SERV-MIB", "svcDhcpRestoreLseStateProblem"))
)
if mibBuilder.loadTexts:
    svcDHCPLseStateRestoreProblem.setStatus(
        "current"
    )

tmnxSvcObjTodSuiteApplicFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 15)
)
tmnxSvcObjTodSuiteApplicFailed.setObjects(
      *(("TIMETRA-SERV-MIB", "tmnxSvcObjRow"),
        ("TIMETRA-SERV-MIB", "tmnxSvcObjRowDescr"),
        ("TIMETRA-SERV-MIB", "tmnxSvcObjTodSuite"),
        ("TIMETRA-SERV-MIB", "tmnxFailureDescription"))
)
if mibBuilder.loadTexts:
    tmnxSvcObjTodSuiteApplicFailed.setStatus(
        "current"
    )

tmnxEndPointTxActiveChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 16)
)
tmnxEndPointTxActiveChanged.setObjects(
      *(("TIMETRA-SERV-MIB", "svcEndPointTxActiveType"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActivePortId"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActiveEncap"),
        ("TIMETRA-SERV-MIB", "svcEndPointTxActiveSdpId"))
)
if mibBuilder.loadTexts:
    tmnxEndPointTxActiveChanged.setStatus(
        "current"
    )

tmnxSvcPEDiscPolServOperStatChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 17)
)
tmnxSvcPEDiscPolServOperStatChg.setObjects(
      *(("TIMETRA-SERV-MIB", "svcPEDiscPolServerAddressType"),
        ("TIMETRA-SERV-MIB", "svcPEDiscPolServerAddress"),
        ("TIMETRA-SERV-MIB", "svcPEDiscPolServerOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcPEDiscPolServOperStatChg.setStatus(
        "current"
    )

svcEndPointMacLimitAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 18)
)
svcEndPointMacLimitAlarmRaised.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SERV-MIB", "svcEndPointMacLimit"))
)
if mibBuilder.loadTexts:
    svcEndPointMacLimitAlarmRaised.setStatus(
        "current"
    )

svcEndPointMacLimitAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 19)
)
svcEndPointMacLimitAlarmCleared.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"),
        ("TIMETRA-SERV-MIB", "svcEndPointMacLimit"))
)
if mibBuilder.loadTexts:
    svcEndPointMacLimitAlarmCleared.setStatus(
        "current"
    )

svcTlsMrpAttrRegistrationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 20)
)
svcTlsMrpAttrRegistrationFailed.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrRegFailedReason"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrType"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrValue"))
)
if mibBuilder.loadTexts:
    svcTlsMrpAttrRegistrationFailed.setStatus(
        "current"
    )

svcFdbMimDestTblFullAlrm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 21)
)
svcFdbMimDestTblFullAlrm.setObjects(
    ("TIMETRA-SERV-MIB", "svcTotalFdbMimDestIdxEntries")
)
if mibBuilder.loadTexts:
    svcFdbMimDestTblFullAlrm.setStatus(
        "current"
    )

svcFdbMimDestTblFullAlrmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 22)
)
svcFdbMimDestTblFullAlrmCleared.setObjects(
    ("TIMETRA-SERV-MIB", "svcTotalFdbMimDestIdxEntries")
)
if mibBuilder.loadTexts:
    svcFdbMimDestTblFullAlrmCleared.setStatus(
        "current"
    )

svcDHCPMiscellaneousProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 23)
)
svcDHCPMiscellaneousProblem.setObjects(
    ("TIMETRA-SERV-MIB", "tmnxFailureDescription")
)
if mibBuilder.loadTexts:
    svcDHCPMiscellaneousProblem.setStatus(
        "current"
    )

svcPersistencyProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 24)
)
svcPersistencyProblem.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "tmnxFailureDescription"))
)
if mibBuilder.loadTexts:
    svcPersistencyProblem.setStatus(
        "current"
    )

svcTlsMrpAttrTblFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 25)
)
svcTlsMrpAttrTblFullAlarmRaised.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsMrpAttrTblFullAlarmRaised.setStatus(
        "current"
    )

svcTlsMrpAttrTblFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 26)
)
svcTlsMrpAttrTblFullAlarmCleared.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsMrpAttrTblFullAlarmCleared.setStatus(
        "current"
    )

svcArpHostPopulateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 27)
)
svcArpHostPopulateErr.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcNotifSapPortId"),
        ("TIMETRA-SERV-MIB", "svcNotifSapEncapValue"),
        ("TIMETRA-SERV-MIB", "svcArpHostPopulateError"))
)
if mibBuilder.loadTexts:
    svcArpHostPopulateErr.setStatus(
        "current"
    )

svcEpipePbbOperStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 28)
)
svcEpipePbbOperStatusChanged.setObjects(
    ("TIMETRA-SERV-MIB", "svcEpipePbbOperState")
)
if mibBuilder.loadTexts:
    svcEpipePbbOperStatusChanged.setStatus(
        "current"
    )

svcEPMCEPConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 29)
)
svcEPMCEPConfigMismatch.setObjects(
    ("TIMETRA-SERV-MIB", "svcEndPointMCEPId")
)
if mibBuilder.loadTexts:
    svcEPMCEPConfigMismatch.setStatus(
        "current"
    )

svcEPMCEPConfigMismatchResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 30)
)
svcEPMCEPConfigMismatchResolved.setObjects(
    ("TIMETRA-SERV-MIB", "svcEndPointMCEPId")
)
if mibBuilder.loadTexts:
    svcEPMCEPConfigMismatchResolved.setStatus(
        "current"
    )

svcEPMCEPPassiveModeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 31)
)
svcEPMCEPPassiveModeActive.setObjects(
    ("TIMETRA-SERV-MIB", "svcEndPointMCEPId")
)
if mibBuilder.loadTexts:
    svcEPMCEPPassiveModeActive.setStatus(
        "current"
    )

svcEPMCEPPassiveModePassive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 32)
)
svcEPMCEPPassiveModePassive.setObjects(
    ("TIMETRA-SERV-MIB", "svcEndPointMCEPId")
)
if mibBuilder.loadTexts:
    svcEPMCEPPassiveModePassive.setStatus(
        "current"
    )

svcRestoreHostProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 33)
)
svcRestoreHostProblem.setObjects(
      *(("TIMETRA-SERV-MIB", "svcHostAddrType"),
        ("TIMETRA-SERV-MIB", "svcHostAddr"),
        ("TIMETRA-SERV-MIB", "tmnxFailureDescription"))
)
if mibBuilder.loadTexts:
    svcRestoreHostProblem.setStatus(
        "current"
    )

svcTlsSiteDesigFwdrChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 34)
)
svcTlsSiteDesigFwdrChg.setObjects(
    ("TIMETRA-SERV-MIB", "svcTlsSiteIdDesignatedFwdr")
)
if mibBuilder.loadTexts:
    svcTlsSiteDesigFwdrChg.setStatus(
        "current"
    )

svcTlsGroupOperStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 35)
)
svcTlsGroupOperStatusChanged.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsGroupOperStatus"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupLastError"))
)
if mibBuilder.loadTexts:
    svcTlsGroupOperStatusChanged.setStatus(
        "current"
    )

svcMacFdbTblFullAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 36)
)
svcMacFdbTblFullAlarm.setObjects(
    ("TIMETRA-SERV-MIB", "svcMacFdbRecords")
)
if mibBuilder.loadTexts:
    svcMacFdbTblFullAlarm.setStatus(
        "current"
    )

svcMacFdbTblFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 37)
)
svcMacFdbTblFullAlarmCleared.setObjects(
    ("TIMETRA-SERV-MIB", "svcMacFdbRecords")
)
if mibBuilder.loadTexts:
    svcMacFdbTblFullAlarmCleared.setStatus(
        "current"
    )

svcMSPwRtMisconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 38)
)
svcMSPwRtMisconfig.setObjects(
      *(("TIMETRA-SERV-MIB", "svcMSPwPeSaiiGlobalId"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeSaiiPrefix"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeSaiiAcId"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeTaiiGlobalId"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeTaiiPrefix"),
        ("TIMETRA-SERV-MIB", "svcMSPwPeTaiiAcId"))
)
if mibBuilder.loadTexts:
    svcMSPwRtMisconfig.setStatus(
        "current"
    )

svcOperGrpOperStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 39)
)
svcOperGrpOperStatusChanged.setObjects(
    ("TIMETRA-SERV-MIB", "svcOperGrpOperStatus")
)
if mibBuilder.loadTexts:
    svcOperGrpOperStatusChanged.setStatus(
        "current"
    )

svcMSPwRetryExpiredNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 40)
)
svcMSPwRetryExpiredNotif.setObjects(
    ("TIMETRA-SERV-MIB", "svcMSPwPeRetryExpired")
)
if mibBuilder.loadTexts:
    svcMSPwRetryExpiredNotif.setStatus(
        "current"
    )

svcVllSiteDesigFwdrChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 41)
)
svcVllSiteDesigFwdrChg.setObjects(
    ("TIMETRA-SERV-MIB", "svcVllSiteIdDesignatedFwdr")
)
if mibBuilder.loadTexts:
    svcVllSiteDesigFwdrChg.setStatus(
        "current"
    )

topologyChangeVcpState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 3)
)
topologyChangeVcpState.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "tmnxVcpState"))
)
if mibBuilder.loadTexts:
    topologyChangeVcpState.setStatus(
        "current"
    )

newRootVcpState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 4)
)
newRootVcpState.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"))
)
if mibBuilder.loadTexts:
    newRootVcpState.setStatus(
        "current"
    )

newRootBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 7)
)
newRootBridge.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"))
)
if mibBuilder.loadTexts:
    newRootBridge.setStatus(
        "current"
    )

vcpActiveProtocolChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 32)
)
vcpActiveProtocolChange.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcTlsStpVcpOperProtocol"))
)
if mibBuilder.loadTexts:
    vcpActiveProtocolChange.setStatus(
        "current"
    )

tmnxNewCistRegionalRootBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 33)
)
tmnxNewCistRegionalRootBridge.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcTlsStpCistRegionalRoot"))
)
if mibBuilder.loadTexts:
    tmnxNewCistRegionalRootBridge.setStatus(
        "current"
    )

tmnxNewMstiRegionalRootBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 34)
)
tmnxNewMstiRegionalRootBridge.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "svcMstiInstanceId"),
        ("TIMETRA-SERV-MIB", "tlsMstiRegionalRoot"))
)
if mibBuilder.loadTexts:
    tmnxNewMstiRegionalRootBridge.setStatus(
        "current"
    )

topologyChangePipMajorState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 39)
)
topologyChangePipMajorState.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"))
)
if mibBuilder.loadTexts:
    topologyChangePipMajorState.setStatus(
        "current"
    )

topologyChangePipState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 40)
)
topologyChangePipState.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"))
)
if mibBuilder.loadTexts:
    topologyChangePipState.setStatus(
        "current"
    )

tmnxPipStpExcepCondStateChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 41)
)
tmnxPipStpExcepCondStateChng.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SERV-MIB", "tlsPipStpException"))
)
if mibBuilder.loadTexts:
    tmnxPipStpExcepCondStateChng.setStatus(
        "current"
    )

pipActiveProtocolChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 42)
)
pipActiveProtocolChange.setObjects(
      *(("TIMETRA-SERV-MIB", "custId"),
        ("TIMETRA-SERV-MIB", "svcId"))
)
if mibBuilder.loadTexts:
    pipActiveProtocolChange.setStatus(
        "current"
    )


# Notifications groups

tmnxSvcNotifyV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 401)
)
tmnxSvcNotifyV6v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcStatusChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbTableFullAlarmRaised"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbTableFullAlarmCleared"),
        ("TIMETRA-SERV-MIB", "iesIfStatusChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsMfibTableFullAlarmRaised"),
        ("TIMETRA-SERV-MIB", "svcTlsMfibTableFullAlarmCleared"),
        ("TIMETRA-SERV-MIB", "svcTlsMacPinningViolation"),
        ("TIMETRA-SERV-MIB", "svcDHCPLseStateRestoreProblem"),
        ("TIMETRA-SERV-MIB", "tmnxSvcObjTodSuiteApplicFailed"),
        ("TIMETRA-SERV-MIB", "tmnxEndPointTxActiveChanged"),
        ("TIMETRA-SERV-MIB", "tmnxSvcPEDiscPolServOperStatChg"),
        ("TIMETRA-SERV-MIB", "svcEndPointMacLimitAlarmRaised"),
        ("TIMETRA-SERV-MIB", "svcEndPointMacLimitAlarmCleared"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrRegistrationFailed"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrTblFullAlarmRaised"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrTblFullAlarmCleared"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbOperStatusChanged"),
        ("TIMETRA-SERV-MIB", "topologyChangeVcpState"),
        ("TIMETRA-SERV-MIB", "newRootVcpState"),
        ("TIMETRA-SERV-MIB", "newRootBridge"),
        ("TIMETRA-SERV-MIB", "vcpActiveProtocolChange"),
        ("TIMETRA-SERV-MIB", "tmnxNewCistRegionalRootBridge"),
        ("TIMETRA-SERV-MIB", "tmnxNewMstiRegionalRootBridge"),
        ("TIMETRA-SERV-MIB", "topologyChangePipMajorState"),
        ("TIMETRA-SERV-MIB", "topologyChangePipState"),
        ("TIMETRA-SERV-MIB", "tmnxPipStpExcepCondStateChng"),
        ("TIMETRA-SERV-MIB", "pipActiveProtocolChange"),
        ("TIMETRA-SERV-MIB", "svcFdbMimDestTblFullAlrm"),
        ("TIMETRA-SERV-MIB", "svcFdbMimDestTblFullAlrmCleared"),
        ("TIMETRA-SERV-MIB", "svcDHCPMiscellaneousProblem"),
        ("TIMETRA-SERV-MIB", "svcPersistencyProblem"))
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyV6v0Group.setStatus(
        "obsolete"
    )

tmnxSvcNotifyObsoletedGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 402)
)
tmnxSvcNotifyObsoletedGroup.setObjects(
      *(("TIMETRA-SERV-MIB", "custCreated"),
        ("TIMETRA-SERV-MIB", "custDeleted"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteCreated"),
        ("TIMETRA-SERV-MIB", "custMultSvcSiteDeleted"),
        ("TIMETRA-SERV-MIB", "svcCreated"),
        ("TIMETRA-SERV-MIB", "svcDeleted"),
        ("TIMETRA-SERV-MIB", "iesIfCreated"),
        ("TIMETRA-SERV-MIB", "iesIfDeleted"),
        ("TIMETRA-SERV-MIB", "svcTlsDHCPLseStRestoreProblem"),
        ("TIMETRA-SERV-MIB", "svcTlsDHCPLseStatePopulateErr"))
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyObsoletedGroup.setStatus(
        "current"
    )

tmnxArpHostNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 403)
)
tmnxArpHostNotifyGroup.setObjects(
    ("TIMETRA-SERV-MIB", "svcArpHostPopulateErr")
)
if mibBuilder.loadTexts:
    tmnxArpHostNotifyGroup.setStatus(
        "current"
    )

tmnxSvcMCEPNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 404)
)
tmnxSvcMCEPNotifyGroup.setObjects(
      *(("TIMETRA-SERV-MIB", "svcEPMCEPConfigMismatch"),
        ("TIMETRA-SERV-MIB", "svcEPMCEPConfigMismatchResolved"),
        ("TIMETRA-SERV-MIB", "svcEPMCEPPassiveModeActive"),
        ("TIMETRA-SERV-MIB", "svcEPMCEPPassiveModePassive"))
)
if mibBuilder.loadTexts:
    tmnxSvcMCEPNotifyGroup.setStatus(
        "current"
    )

tmnxSvcNotifyV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 405)
)
tmnxSvcNotifyV7v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcStatusChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbTableFullAlarmRaised"),
        ("TIMETRA-SERV-MIB", "svcTlsFdbTableFullAlarmCleared"),
        ("TIMETRA-SERV-MIB", "iesIfStatusChanged"),
        ("TIMETRA-SERV-MIB", "svcTlsMfibTableFullAlarmRaised"),
        ("TIMETRA-SERV-MIB", "svcTlsMfibTableFullAlarmCleared"),
        ("TIMETRA-SERV-MIB", "svcTlsMacPinningViolation"),
        ("TIMETRA-SERV-MIB", "svcDHCPLseStateRestoreProblem"),
        ("TIMETRA-SERV-MIB", "tmnxSvcObjTodSuiteApplicFailed"),
        ("TIMETRA-SERV-MIB", "tmnxEndPointTxActiveChanged"),
        ("TIMETRA-SERV-MIB", "tmnxSvcPEDiscPolServOperStatChg"),
        ("TIMETRA-SERV-MIB", "svcEndPointMacLimitAlarmRaised"),
        ("TIMETRA-SERV-MIB", "svcEndPointMacLimitAlarmCleared"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrRegistrationFailed"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrTblFullAlarmRaised"),
        ("TIMETRA-SERV-MIB", "svcTlsMrpAttrTblFullAlarmCleared"),
        ("TIMETRA-SERV-MIB", "svcEpipePbbOperStatusChanged"),
        ("TIMETRA-SERV-MIB", "topologyChangeVcpState"),
        ("TIMETRA-SERV-MIB", "newRootVcpState"),
        ("TIMETRA-SERV-MIB", "newRootBridge"),
        ("TIMETRA-SERV-MIB", "vcpActiveProtocolChange"),
        ("TIMETRA-SERV-MIB", "tmnxNewCistRegionalRootBridge"),
        ("TIMETRA-SERV-MIB", "tmnxNewMstiRegionalRootBridge"),
        ("TIMETRA-SERV-MIB", "topologyChangePipMajorState"),
        ("TIMETRA-SERV-MIB", "topologyChangePipState"),
        ("TIMETRA-SERV-MIB", "tmnxPipStpExcepCondStateChng"),
        ("TIMETRA-SERV-MIB", "pipActiveProtocolChange"),
        ("TIMETRA-SERV-MIB", "svcFdbMimDestTblFullAlrm"),
        ("TIMETRA-SERV-MIB", "svcFdbMimDestTblFullAlrmCleared"),
        ("TIMETRA-SERV-MIB", "svcDHCPMiscellaneousProblem"),
        ("TIMETRA-SERV-MIB", "svcPersistencyProblem"),
        ("TIMETRA-SERV-MIB", "svcRestoreHostProblem"))
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyV7v0Group.setStatus(
        "current"
    )

tmnxSvcNotifyV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 406)
)
tmnxSvcNotifyV8v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcTlsSiteDesigFwdrChg"),
        ("TIMETRA-SERV-MIB", "svcTlsGroupOperStatusChanged"))
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyV8v0Group.setStatus(
        "current"
    )

tmnxSvcNotifyV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 408)
)
tmnxSvcNotifyV9v0Group.setObjects(
      *(("TIMETRA-SERV-MIB", "svcMSPwRtMisconfig"),
        ("TIMETRA-SERV-MIB", "svcMSPwRetryExpiredNotif"),
        ("TIMETRA-SERV-MIB", "svcMacFdbTblFullAlarm"),
        ("TIMETRA-SERV-MIB", "svcMacFdbTblFullAlarmCleared"),
        ("TIMETRA-SERV-MIB", "svcOperGrpOperStatusChanged"))
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyV9v0Group.setStatus(
        "current"
    )

tmnxSvcNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 413)
)
tmnxSvcNotifyV10v0Group.setObjects(
    ("TIMETRA-SERV-MIB", "svcVllSiteDesigFwdrChg")
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyV10v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxCustCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1, 1, 100)
)
if mibBuilder.loadTexts:
    tmnxCustCompliance.setStatus(
        "obsolete"
    )

tmnxCustV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1, 1, 101)
)
if mibBuilder.loadTexts:
    tmnxCustV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxCustV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1, 1, 102)
)
if mibBuilder.loadTexts:
    tmnxCustV9v0Compliance.setStatus(
        "current"
    )

tmnxSvc7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 100)
)
if mibBuilder.loadTexts:
    tmnxSvc7450V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7750V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 101)
)
if mibBuilder.loadTexts:
    tmnxSvc7750V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7710V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 102)
)
if mibBuilder.loadTexts:
    tmnxSvc7710V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7450V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 103)
)
if mibBuilder.loadTexts:
    tmnxSvc7450V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7750V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 104)
)
if mibBuilder.loadTexts:
    tmnxSvc7750V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7710V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 105)
)
if mibBuilder.loadTexts:
    tmnxSvc7710V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 106)
)
if mibBuilder.loadTexts:
    tmnxSvc7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7750V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 107)
)
if mibBuilder.loadTexts:
    tmnxSvc7750V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7710V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 108)
)
if mibBuilder.loadTexts:
    tmnxSvc7710V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7450V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 109)
)
if mibBuilder.loadTexts:
    tmnxSvc7450V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7750V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 110)
)
if mibBuilder.loadTexts:
    tmnxSvc7750V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7710V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 111)
)
if mibBuilder.loadTexts:
    tmnxSvc7710V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7450V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 112)
)
if mibBuilder.loadTexts:
    tmnxSvc7450V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7750V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 113)
)
if mibBuilder.loadTexts:
    tmnxSvc7750V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7710V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 114)
)
if mibBuilder.loadTexts:
    tmnxSvc7710V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxSvc7450V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 115)
)
if mibBuilder.loadTexts:
    tmnxSvc7450V10v0Compliance.setStatus(
        "current"
    )

tmnxSvc7750V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 116)
)
if mibBuilder.loadTexts:
    tmnxSvc7750V10v0Compliance.setStatus(
        "current"
    )

tmnxSvc7710V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 117)
)
if mibBuilder.loadTexts:
    tmnxSvc7710V10v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SERV-MIB",
    **{"ArpHostInfoOrigin": ArpHostInfoOrigin,
       "ServObjName": ServObjName,
       "ServObjDesc": ServObjDesc,
       "ServObjLongDesc": ServObjLongDesc,
       "ServType": ServType,
       "VpnId": VpnId,
       "SdpId": SdpId,
       "SdpTemplateId": SdpTemplateId,
       "PWTemplateId": PWTemplateId,
       "TlsBpduTranslation": TlsBpduTranslation,
       "TlsLimitMacMoveLevel": TlsLimitMacMoveLevel,
       "TlsLimitMacMove": TlsLimitMacMove,
       "SdpBindVcType": SdpBindVcType,
       "StpExceptionCondition": StpExceptionCondition,
       "LspIdList": LspIdList,
       "BridgeId": BridgeId,
       "TSapIngQueueId": TSapIngQueueId,
       "TSapEgrQueueId": TSapEgrQueueId,
       "TStpPortState": TStpPortState,
       "StpPortRole": StpPortRole,
       "StpProtocol": StpProtocol,
       "MfibLocation": MfibLocation,
       "MfibGrpSrcFwdOrBlk": MfibGrpSrcFwdOrBlk,
       "MvplsPruneState": MvplsPruneState,
       "TQosQueueAttribute": TQosQueueAttribute,
       "TVirtSchedAttribute": TVirtSchedAttribute,
       "MstiInstanceId": MstiInstanceId,
       "MstiInstanceIdOrZero": MstiInstanceIdOrZero,
       "DhcpLseStateInfoOrigin": DhcpLseStateInfoOrigin,
       "IAIDType": IAIDType,
       "TdmOptionsSigPkts": TdmOptionsSigPkts,
       "TdmOptionsCasTrunkFraming": TdmOptionsCasTrunkFraming,
       "CemSapReportAlarm": CemSapReportAlarm,
       "CemSapEcid": CemSapEcid,
       "SdpBFHundredthsOfPercent": SdpBFHundredthsOfPercent,
       "SdpBindBandwidth": SdpBindBandwidth,
       "L2ptProtocols": L2ptProtocols,
       "L2RouteOrigin": L2RouteOrigin,
       "ConfigStatus": ConfigStatus,
       "ServAccessLocation": ServAccessLocation,
       "ServShcvOperState": ServShcvOperState,
       "TMrpPolicyDefaultAction": TMrpPolicyDefaultAction,
       "TMrpPolicyAction": TMrpPolicyAction,
       "TmnxSiteId": TmnxSiteId,
       "timetraServicesMIBModule": timetraServicesMIBModule,
       "tmnxServConformance": tmnxServConformance,
       "tmnxCustConformance": tmnxCustConformance,
       "tmnxCustCompliances": tmnxCustCompliances,
       "tmnxCustCompliance": tmnxCustCompliance,
       "tmnxCustV8v0Compliance": tmnxCustV8v0Compliance,
       "tmnxCustV9v0Compliance": tmnxCustV9v0Compliance,
       "tmnxCustGroups": tmnxCustGroups,
       "tmnxCustV6v0Group": tmnxCustV6v0Group,
       "tmnxCustV8v0Group": tmnxCustV8v0Group,
       "tmnxCustV9v0Group": tmnxCustV9v0Group,
       "tmnxSvcConformance": tmnxSvcConformance,
       "tmnxSvcCompliances": tmnxSvcCompliances,
       "tmnxSvc7450V6v0Compliance": tmnxSvc7450V6v0Compliance,
       "tmnxSvc7750V6v0Compliance": tmnxSvc7750V6v0Compliance,
       "tmnxSvc7710V6v0Compliance": tmnxSvc7710V6v0Compliance,
       "tmnxSvc7450V6v1Compliance": tmnxSvc7450V6v1Compliance,
       "tmnxSvc7750V6v1Compliance": tmnxSvc7750V6v1Compliance,
       "tmnxSvc7710V6v1Compliance": tmnxSvc7710V6v1Compliance,
       "tmnxSvc7450V7v0Compliance": tmnxSvc7450V7v0Compliance,
       "tmnxSvc7750V7v0Compliance": tmnxSvc7750V7v0Compliance,
       "tmnxSvc7710V7v0Compliance": tmnxSvc7710V7v0Compliance,
       "tmnxSvc7450V8v0Compliance": tmnxSvc7450V8v0Compliance,
       "tmnxSvc7750V8v0Compliance": tmnxSvc7750V8v0Compliance,
       "tmnxSvc7710V8v0Compliance": tmnxSvc7710V8v0Compliance,
       "tmnxSvc7450V9v0Compliance": tmnxSvc7450V9v0Compliance,
       "tmnxSvc7750V9v0Compliance": tmnxSvc7750V9v0Compliance,
       "tmnxSvc7710V9v0Compliance": tmnxSvc7710V9v0Compliance,
       "tmnxSvc7450V10v0Compliance": tmnxSvc7450V10v0Compliance,
       "tmnxSvc7750V10v0Compliance": tmnxSvc7750V10v0Compliance,
       "tmnxSvc7710V10v0Compliance": tmnxSvc7710V10v0Compliance,
       "tmnxSvcGroups": tmnxSvcGroups,
       "tmnxSvcV6v0Group": tmnxSvcV6v0Group,
       "tmnxSvcTlsV6v0Group": tmnxSvcTlsV6v0Group,
       "tmnxSvcTlsFdbV6v0Group": tmnxSvcTlsFdbV6v0Group,
       "tmnxSvcIesIfV6v0Group": tmnxSvcIesIfV6v0Group,
       "tmnxSvcTlsShgV6v0Group": tmnxSvcTlsShgV6v0Group,
       "tmnxSvcTlsMFibV6v0Group": tmnxSvcTlsMFibV6v0Group,
       "tmnxSvcRdntV6v0Group": tmnxSvcRdntV6v0Group,
       "tmnxSvcTlsMstiV6v0Group": tmnxSvcTlsMstiV6v0Group,
       "tmnxSvcTlsEgrV6v0Group": tmnxSvcTlsEgrV6v0Group,
       "tmnxSvcDhcpV6v0Group": tmnxSvcDhcpV6v0Group,
       "tmnxSvcEndPointV6v0Group": tmnxSvcEndPointV6v0Group,
       "tmnxSvcPEV6v0Group": tmnxSvcPEV6v0Group,
       "tmnxSvcIfDHCP6V6v0Group": tmnxSvcIfDHCP6V6v0Group,
       "tmnxSvcTlsBackbone6v0Group": tmnxSvcTlsBackbone6v0Group,
       "tmnxSvcTlsBgpV6v0Group": tmnxSvcTlsBgpV6v0Group,
       "tmnxSvcEpipeV6v0Group": tmnxSvcEpipeV6v0Group,
       "tmnxSvcTlsPipV6v0Group": tmnxSvcTlsPipV6v0Group,
       "tmnxApipeV3v0Group": tmnxApipeV3v0Group,
       "tmnxSvcRoutedCOV5v0Group": tmnxSvcRoutedCOV5v0Group,
       "tmnxSvcBsxV6v0Group": tmnxSvcBsxV6v0Group,
       "tmnxSvcTlsBackbone6v1Group": tmnxSvcTlsBackbone6v1Group,
       "tmnxArpHostGroup": tmnxArpHostGroup,
       "svcIgmpTrkGroup": svcIgmpTrkGroup,
       "svcTlsMacV7v0Group": svcTlsMacV7v0Group,
       "tmnxSvcRoutedCOV7v0Group": tmnxSvcRoutedCOV7v0Group,
       "svcTlsEndPointV7v0Group": svcTlsEndPointV7v0Group,
       "tmnxSvcIpipeV7v0Group": tmnxSvcIpipeV7v0Group,
       "tmnxSvcDhcpBgpV7v0Group": tmnxSvcDhcpBgpV7v0Group,
       "tmnxSvcTlsPipV7v0Group": tmnxSvcTlsPipV7v0Group,
       "tmnxArpHostBgpGroup": tmnxArpHostBgpGroup,
       "tmnxSvcDhcpV7v0Group": tmnxSvcDhcpV7v0Group,
       "tmnxSvcPbbMacV7v0Group": tmnxSvcPbbMacV7v0Group,
       "tmnxSvcTlsFdbV7v0Group": tmnxSvcTlsFdbV7v0Group,
       "tmnxSvcV7v0Group": tmnxSvcV7v0Group,
       "tmnxSvcV8v0Group": tmnxSvcV8v0Group,
       "tmnxSvcMrpPolicyV8v0Group": tmnxSvcMrpPolicyV8v0Group,
       "tmnxSvcSiteV8v0Group": tmnxSvcSiteV8v0Group,
       "tmnxSvcRoutedCOV8v0Group": tmnxSvcRoutedCOV8v0Group,
       "tmnxArpHostV8v0Group": tmnxArpHostV8v0Group,
       "tmnxSvcTlsBgpV8v0Group": tmnxSvcTlsBgpV8v0Group,
       "tmnxSvcDhcpV8v0Group": tmnxSvcDhcpV8v0Group,
       "tmnxSvcBsxV8v0Group": tmnxSvcBsxV8v0Group,
       "tmnxSvcTlsV7v0Group": tmnxSvcTlsV7v0Group,
       "tmnxSvcIesIfV7v0Group": tmnxSvcIesIfV7v0Group,
       "tmnxSvcRoutedVplsV8v0Group": tmnxSvcRoutedVplsV8v0Group,
       "tmnxSvcMvrpV8v0Group": tmnxSvcMvrpV8v0Group,
       "tmnxSvcIpipeV8v0Group": tmnxSvcIpipeV8v0Group,
       "tmnxSvcInterAsV8v0Group": tmnxSvcInterAsV8v0Group,
       "tmnxSvcPwV8v0Group": tmnxSvcPwV8v0Group,
       "tmnxSvcTlsPipV8v0Group": tmnxSvcTlsPipV8v0Group,
       "tmnxSvcIesIfV8v0Group": tmnxSvcIesIfV8v0Group,
       "tmnxSvcV9v0Group": tmnxSvcV9v0Group,
       "tmnxSvcMSPwPeV9v0Group": tmnxSvcMSPwPeV9v0Group,
       "tmnxSvcOperGrpV9v0Group": tmnxSvcOperGrpV9v0Group,
       "tmnxSvcDhcpV9v0Group": tmnxSvcDhcpV9v0Group,
       "tmnxSvcRoutedCOV9v0Group": tmnxSvcRoutedCOV9v0Group,
       "tmnxSvcV9v0R4Group": tmnxSvcV9v0R4Group,
       "tmnxSvcMacReNotifyGroup": tmnxSvcMacReNotifyGroup,
       "tmnxSvcDhcpV10v0Group": tmnxSvcDhcpV10v0Group,
       "tmnxSvcRoutedCOV10v0Group": tmnxSvcRoutedCOV10v0Group,
       "tmnxSvcV10v0Group": tmnxSvcV10v0Group,
       "tmnxSvcIesIfV10v0Group": tmnxSvcIesIfV10v0Group,
       "tmnxArpHostV10v0Group": tmnxArpHostV10v0Group,
       "tmnxSvcIesIfNHV10v0Group": tmnxSvcIesIfNHV10v0Group,
       "tmnxSvcNotifyObjsV6v0Group": tmnxSvcNotifyObjsV6v0Group,
       "tmnxArpHostNotifyObjsGroup": tmnxArpHostNotifyObjsGroup,
       "tmnxSvcNotifyObjsV7v0Group": tmnxSvcNotifyObjsV7v0Group,
       "tmnxSvcObsoletedV6v0Group": tmnxSvcObsoletedV6v0Group,
       "tmnxSvcObsoletedV8v0Group": tmnxSvcObsoletedV8v0Group,
       "tmnxSvcObsoletedV9v0Group": tmnxSvcObsoletedV9v0Group,
       "tmnxSvcNotifyV6v0Group": tmnxSvcNotifyV6v0Group,
       "tmnxSvcNotifyObsoletedGroup": tmnxSvcNotifyObsoletedGroup,
       "tmnxArpHostNotifyGroup": tmnxArpHostNotifyGroup,
       "tmnxSvcMCEPNotifyGroup": tmnxSvcMCEPNotifyGroup,
       "tmnxSvcNotifyV7v0Group": tmnxSvcNotifyV7v0Group,
       "tmnxSvcNotifyV8v0Group": tmnxSvcNotifyV8v0Group,
       "tmnxSvcEthCfmGroup": tmnxSvcEthCfmGroup,
       "tmnxSvcNotifyV9v0Group": tmnxSvcNotifyV9v0Group,
       "tmnxSvcApipeInfoV9v0Group": tmnxSvcApipeInfoV9v0Group,
       "tmnxSvcSpbGroup": tmnxSvcSpbGroup,
       "tmnxSvcVllBgpGroup": tmnxSvcVllBgpGroup,
       "tmnxSvcP2mpGroup": tmnxSvcP2mpGroup,
       "tmnxSvcNotifyV10v0Group": tmnxSvcNotifyV10v0Group,
       "tmnxTstpConformance": tmnxTstpConformance,
       "tmnxTstpCompliances": tmnxTstpCompliances,
       "tmnxTstpGroups": tmnxTstpGroups,
       "tmnxServObjs": tmnxServObjs,
       "tmnxCustObjs": tmnxCustObjs,
       "custNumEntries": custNumEntries,
       "custNextFreeId": custNextFreeId,
       "custInfoTable": custInfoTable,
       "custInfoEntry": custInfoEntry,
       "custId": custId,
       "custRowStatus": custRowStatus,
       "custDescription": custDescription,
       "custContact": custContact,
       "custPhone": custPhone,
       "custLastMgmtChange": custLastMgmtChange,
       "custMultiServiceSiteTable": custMultiServiceSiteTable,
       "custMultiServiceSiteEntry": custMultiServiceSiteEntry,
       "custMultSvcSiteName": custMultSvcSiteName,
       "custMultSvcSiteRowStatus": custMultSvcSiteRowStatus,
       "custMultSvcSiteDescription": custMultSvcSiteDescription,
       "custMultSvcSiteScope": custMultSvcSiteScope,
       "custMultSvcSiteAssignment": custMultSvcSiteAssignment,
       "custMultSvcSiteIngressSchedulerPolicy": custMultSvcSiteIngressSchedulerPolicy,
       "custMultSvcSiteEgressSchedulerPolicy": custMultSvcSiteEgressSchedulerPolicy,
       "custMultSvcSiteLastMgmtChange": custMultSvcSiteLastMgmtChange,
       "custMultSvcSiteTodSuite": custMultSvcSiteTodSuite,
       "custMultSvcSiteCurrentIngrSchedPlcy": custMultSvcSiteCurrentIngrSchedPlcy,
       "custMultSvcSiteCurrentEgrSchedPlcy": custMultSvcSiteCurrentEgrSchedPlcy,
       "custMultSvcSiteEgressAggRateLimit": custMultSvcSiteEgressAggRateLimit,
       "custMultSvcSiteIntendedIngrSchedPlcy": custMultSvcSiteIntendedIngrSchedPlcy,
       "custMultSvcSiteIntendedEgrSchedPlcy": custMultSvcSiteIntendedEgrSchedPlcy,
       "custMultSvcSiteFrameBasedAccnt": custMultSvcSiteFrameBasedAccnt,
       "custMultSvcSiteSubscriberMss": custMultSvcSiteSubscriberMss,
       "custMultSvcSiteIngPolcrCtrlPolcy": custMultSvcSiteIngPolcrCtrlPolcy,
       "custMultSvcSiteEgrPolcrCtrlPolcy": custMultSvcSiteEgrPolcrCtrlPolcy,
       "custMultiSvcSiteIngStatsTable": custMultiSvcSiteIngStatsTable,
       "custMultiSvcSiteIngStatsEntry": custMultiSvcSiteIngStatsEntry,
       "custIngQosSchedName": custIngQosSchedName,
       "custIngQosSchedStatsForwardedPackets": custIngQosSchedStatsForwardedPackets,
       "custIngQosSchedStatsForwardedOctets": custIngQosSchedStatsForwardedOctets,
       "custMultiSvcSiteEgrStatsTable": custMultiSvcSiteEgrStatsTable,
       "custMultiSvcSiteEgrStatsEntry": custMultiSvcSiteEgrStatsEntry,
       "custEgrQosSchedName": custEgrQosSchedName,
       "custEgrQosSchedStatsForwardedPackets": custEgrQosSchedStatsForwardedPackets,
       "custEgrQosSchedStatsForwardedOctets": custEgrQosSchedStatsForwardedOctets,
       "custIngQosPortIdSchedStatsTable": custIngQosPortIdSchedStatsTable,
       "custIngQosPortIdSchedStatsEntry": custIngQosPortIdSchedStatsEntry,
       "custIngQosPortIdSchedName": custIngQosPortIdSchedName,
       "custIngQosAssignmentPortId": custIngQosAssignmentPortId,
       "custIngQosPortSchedFwdPkts": custIngQosPortSchedFwdPkts,
       "custIngQosPortSchedFwdOctets": custIngQosPortSchedFwdOctets,
       "custEgrQosPortIdSchedStatsTable": custEgrQosPortIdSchedStatsTable,
       "custEgrQosPortIdSchedStatsEntry": custEgrQosPortIdSchedStatsEntry,
       "custEgrQosPortIdSchedName": custEgrQosPortIdSchedName,
       "custEgrQosAssignmentPortId": custEgrQosAssignmentPortId,
       "custEgrQosPortSchedFwdPkts": custEgrQosPortSchedFwdPkts,
       "custEgrQosPortSchedFwdOctets": custEgrQosPortSchedFwdOctets,
       "custMssIngQosSchedInfoTable": custMssIngQosSchedInfoTable,
       "custMssIngQosSchedInfoEntry": custMssIngQosSchedInfoEntry,
       "custMssIngQosSName": custMssIngQosSName,
       "custMssIngQosSRowStatus": custMssIngQosSRowStatus,
       "custMssIngQosSLastMgmtChange": custMssIngQosSLastMgmtChange,
       "custMssIngQosSOverrideFlags": custMssIngQosSOverrideFlags,
       "custMssIngQosSPIR": custMssIngQosSPIR,
       "custMssIngQosSCIR": custMssIngQosSCIR,
       "custMssIngQosSSummedCIR": custMssIngQosSSummedCIR,
       "custMssEgrQosSchedInfoTable": custMssEgrQosSchedInfoTable,
       "custMssEgrQosSchedInfoEntry": custMssEgrQosSchedInfoEntry,
       "custMssEgrQosSName": custMssEgrQosSName,
       "custMssEgrQosSRowStatus": custMssEgrQosSRowStatus,
       "custMssEgrQosSLastMgmtChange": custMssEgrQosSLastMgmtChange,
       "custMssEgrQosSOverrideFlags": custMssEgrQosSOverrideFlags,
       "custMssEgrQosSPIR": custMssEgrQosSPIR,
       "custMssEgrQosSCIR": custMssEgrQosSCIR,
       "custMssEgrQosSSummedCIR": custMssEgrQosSSummedCIR,
       "custMultiSvcSiteIngSchedPlcyStatsTable": custMultiSvcSiteIngSchedPlcyStatsTable,
       "custMultiSvcSiteIngSchedPlcyStatsEntry": custMultiSvcSiteIngSchedPlcyStatsEntry,
       "custIngSchedPlcyStatsFwdPkt": custIngSchedPlcyStatsFwdPkt,
       "custIngSchedPlcyStatsFwdOct": custIngSchedPlcyStatsFwdOct,
       "custMultiSvcSiteEgrSchedPlcyStatsTable": custMultiSvcSiteEgrSchedPlcyStatsTable,
       "custMultiSvcSiteEgrSchedPlcyStatsEntry": custMultiSvcSiteEgrSchedPlcyStatsEntry,
       "custEgrSchedPlcyStatsFwdPkt": custEgrSchedPlcyStatsFwdPkt,
       "custEgrSchedPlcyStatsFwdOct": custEgrSchedPlcyStatsFwdOct,
       "custMultiSvcSiteIngSchedPlcyPortStatsTable": custMultiSvcSiteIngSchedPlcyPortStatsTable,
       "custMultiSvcSiteIngSchedPlcyPortStatsEntry": custMultiSvcSiteIngSchedPlcyPortStatsEntry,
       "custIngSchedPlcyPortStatsPort": custIngSchedPlcyPortStatsPort,
       "custIngSchedPlcyPortStatsFwdPkt": custIngSchedPlcyPortStatsFwdPkt,
       "custIngSchedPlcyPortStatsFwdOct": custIngSchedPlcyPortStatsFwdOct,
       "custMultiSvcSiteEgrSchedPlcyPortStatsTable": custMultiSvcSiteEgrSchedPlcyPortStatsTable,
       "custMultiSvcSiteEgrSchedPlcyPortStatsEntry": custMultiSvcSiteEgrSchedPlcyPortStatsEntry,
       "custEgrSchedPlcyPortStatsPort": custEgrSchedPlcyPortStatsPort,
       "custEgrSchedPlcyPortStatsFwdPkt": custEgrSchedPlcyPortStatsFwdPkt,
       "custEgrSchedPlcyPortStatsFwdOct": custEgrSchedPlcyPortStatsFwdOct,
       "custMssIngQosArbitStatsTable": custMssIngQosArbitStatsTable,
       "custMssIngQosArbitStatsEntry": custMssIngQosArbitStatsEntry,
       "custMssIngQosArbitName": custMssIngQosArbitName,
       "custMssIngQosArbitStatsFwdPkts": custMssIngQosArbitStatsFwdPkts,
       "custMssIngQosArbitStatsFwdPktsLo": custMssIngQosArbitStatsFwdPktsLo,
       "custMssIngQosArbitStatsFwdPktsHi": custMssIngQosArbitStatsFwdPktsHi,
       "custMssIngQosArbitStatsFwdOcts": custMssIngQosArbitStatsFwdOcts,
       "custMssIngQosArbitStatsFwdOctsLo": custMssIngQosArbitStatsFwdOctsLo,
       "custMssIngQosArbitStatsFwdOctsHi": custMssIngQosArbitStatsFwdOctsHi,
       "custMssEgrQosArbitStatsTable": custMssEgrQosArbitStatsTable,
       "custMssEgrQosArbitStatsEntry": custMssEgrQosArbitStatsEntry,
       "custMssEgrQosArbitName": custMssEgrQosArbitName,
       "custMssEgrQosArbitStatsFwdPkts": custMssEgrQosArbitStatsFwdPkts,
       "custMssEgrQosArbitStatsFwdPktsLo": custMssEgrQosArbitStatsFwdPktsLo,
       "custMssEgrQosArbitStatsFwdPktsHi": custMssEgrQosArbitStatsFwdPktsHi,
       "custMssEgrQosArbitStatsFwdOcts": custMssEgrQosArbitStatsFwdOcts,
       "custMssEgrQosArbitStatsFwdOctsLo": custMssEgrQosArbitStatsFwdOctsLo,
       "custMssEgrQosArbitStatsFwdOctsHi": custMssEgrQosArbitStatsFwdOctsHi,
       "custIngQosPortIdArbitStatsTable": custIngQosPortIdArbitStatsTable,
       "custIngQosPortIdArbitStatsEntry": custIngQosPortIdArbitStatsEntry,
       "custIngQosPortIdArbitName": custIngQosPortIdArbitName,
       "custIngQosPortIdArbitFwdPkts": custIngQosPortIdArbitFwdPkts,
       "custIngQosPortIdArbitFwdPktsLo": custIngQosPortIdArbitFwdPktsLo,
       "custIngQosPortIdArbitFwdPktsHi": custIngQosPortIdArbitFwdPktsHi,
       "custIngQosPortIdArbitFwdOcts": custIngQosPortIdArbitFwdOcts,
       "custIngQosPortIdArbitFwdOctsLo": custIngQosPortIdArbitFwdOctsLo,
       "custIngQosPortIdArbitFwdOctsHi": custIngQosPortIdArbitFwdOctsHi,
       "custEgrQosPortIdArbitStatsTable": custEgrQosPortIdArbitStatsTable,
       "custEgrQosPortIdArbitStatsEntry": custEgrQosPortIdArbitStatsEntry,
       "custEgrQosPortIdArbitName": custEgrQosPortIdArbitName,
       "custEgrQosPortIdArbitFwdPkts": custEgrQosPortIdArbitFwdPkts,
       "custEgrQosPortIdArbitFwdPktsLo": custEgrQosPortIdArbitFwdPktsLo,
       "custEgrQosPortIdArbitFwdPktsHi": custEgrQosPortIdArbitFwdPktsHi,
       "custEgrQosPortIdArbitFwdOcts": custEgrQosPortIdArbitFwdOcts,
       "custEgrQosPortIdArbitFwdOctsLo": custEgrQosPortIdArbitFwdOctsLo,
       "custEgrQosPortIdArbitFwdOctsHi": custEgrQosPortIdArbitFwdOctsHi,
       "tmnxSvcObjs": tmnxSvcObjs,
       "svcNumEntries": svcNumEntries,
       "svcBaseInfoTable": svcBaseInfoTable,
       "svcBaseInfoEntry": svcBaseInfoEntry,
       "svcId": svcId,
       "svcRowStatus": svcRowStatus,
       "svcType": svcType,
       "svcCustId": svcCustId,
       "svcIpRouting": svcIpRouting,
       "svcDescription": svcDescription,
       "svcMtu": svcMtu,
       "svcAdminStatus": svcAdminStatus,
       "svcOperStatus": svcOperStatus,
       "svcNumSaps": svcNumSaps,
       "svcNumSdps": svcNumSdps,
       "svcLastMgmtChange": svcLastMgmtChange,
       "svcDefMeshVcId": svcDefMeshVcId,
       "svcVpnId": svcVpnId,
       "svcVRouterId": svcVRouterId,
       "svcAutoBind": svcAutoBind,
       "svcLastStatusChange": svcLastStatusChange,
       "svcVllType": svcVllType,
       "svcMgmtVpls": svcMgmtVpls,
       "svcRadiusDiscovery": svcRadiusDiscovery,
       "svcRadiusUserNameType": svcRadiusUserNameType,
       "svcRadiusUserName": svcRadiusUserName,
       "svcVcSwitching": svcVcSwitching,
       "svcRadiusPEDiscPolicy": svcRadiusPEDiscPolicy,
       "svcRadiusDiscoveryShutdown": svcRadiusDiscoveryShutdown,
       "svcVplsType": svcVplsType,
       "svcNumMcStandbySaps": svcNumMcStandbySaps,
       "svcName": svcName,
       "svcInterASMvpn": svcInterASMvpn,
       "svcHashLabel": svcHashLabel,
       "svcTmplUsed": svcTmplUsed,
       "svcCtrlSvcId": svcCtrlSvcId,
       "svcCreationOrigin": svcCreationOrigin,
       "svcTlsInfoTable": svcTlsInfoTable,
       "svcTlsInfoEntry": svcTlsInfoEntry,
       "svcTlsMacLearning": svcTlsMacLearning,
       "svcTlsDiscardUnknownDest": svcTlsDiscardUnknownDest,
       "svcTlsFdbTableSize": svcTlsFdbTableSize,
       "svcTlsFdbNumEntries": svcTlsFdbNumEntries,
       "svcTlsFdbNumStaticEntries": svcTlsFdbNumStaticEntries,
       "svcTlsFdbLocalAgeTime": svcTlsFdbLocalAgeTime,
       "svcTlsFdbRemoteAgeTime": svcTlsFdbRemoteAgeTime,
       "svcTlsStpAdminStatus": svcTlsStpAdminStatus,
       "svcTlsStpPriority": svcTlsStpPriority,
       "svcTlsStpBridgeAddress": svcTlsStpBridgeAddress,
       "svcTlsStpTimeSinceTopologyChange": svcTlsStpTimeSinceTopologyChange,
       "svcTlsStpTopologyChanges": svcTlsStpTopologyChanges,
       "svcTlsStpDesignatedRoot": svcTlsStpDesignatedRoot,
       "svcTlsStpRootCost": svcTlsStpRootCost,
       "svcTlsStpRootPort": svcTlsStpRootPort,
       "svcTlsStpMaxAge": svcTlsStpMaxAge,
       "svcTlsStpHelloTime": svcTlsStpHelloTime,
       "svcTlsStpHoldTime": svcTlsStpHoldTime,
       "svcTlsStpForwardDelay": svcTlsStpForwardDelay,
       "svcTlsStpBridgeMaxAge": svcTlsStpBridgeMaxAge,
       "svcTlsStpBridgeHelloTime": svcTlsStpBridgeHelloTime,
       "svcTlsStpBridgeForwardDelay": svcTlsStpBridgeForwardDelay,
       "svcTlsStpOperStatus": svcTlsStpOperStatus,
       "svcTlsStpVirtualRootBridgeStatus": svcTlsStpVirtualRootBridgeStatus,
       "svcTlsMacAgeing": svcTlsMacAgeing,
       "svcTlsStpTopologyChangeActive": svcTlsStpTopologyChangeActive,
       "svcTlsFdbTableFullHighWatermark": svcTlsFdbTableFullHighWatermark,
       "svcTlsFdbTableFullLowWatermark": svcTlsFdbTableFullLowWatermark,
       "svcTlsVpnId": svcTlsVpnId,
       "svcTlsCustId": svcTlsCustId,
       "svcTlsStpVersion": svcTlsStpVersion,
       "svcTlsStpHoldCount": svcTlsStpHoldCount,
       "svcTlsStpPrimaryBridge": svcTlsStpPrimaryBridge,
       "svcTlsStpBridgeInstanceId": svcTlsStpBridgeInstanceId,
       "svcTlsStpVcpOperProtocol": svcTlsStpVcpOperProtocol,
       "svcTlsMacMoveMaxRate": svcTlsMacMoveMaxRate,
       "svcTlsMacMoveRetryTimeout": svcTlsMacMoveRetryTimeout,
       "svcTlsMacMoveAdminStatus": svcTlsMacMoveAdminStatus,
       "svcTlsMacRelearnOnly": svcTlsMacRelearnOnly,
       "svcTlsMfibTableSize": svcTlsMfibTableSize,
       "svcTlsMfibTableFullHighWatermark": svcTlsMfibTableFullHighWatermark,
       "svcTlsMfibTableFullLowWatermark": svcTlsMfibTableFullLowWatermark,
       "svcTlsMacFlushOnFail": svcTlsMacFlushOnFail,
       "svcTlsStpRegionName": svcTlsStpRegionName,
       "svcTlsStpRegionRevision": svcTlsStpRegionRevision,
       "svcTlsStpBridgeMaxHops": svcTlsStpBridgeMaxHops,
       "svcTlsStpCistRegionalRoot": svcTlsStpCistRegionalRoot,
       "svcTlsStpCistIntRootCost": svcTlsStpCistIntRootCost,
       "svcTlsStpCistRemainingHopCount": svcTlsStpCistRemainingHopCount,
       "svcTlsStpCistRegionalRootPort": svcTlsStpCistRegionalRootPort,
       "svcTlsFdbNumLearnedEntries": svcTlsFdbNumLearnedEntries,
       "svcTlsFdbNumOamEntries": svcTlsFdbNumOamEntries,
       "svcTlsFdbNumDhcpEntries": svcTlsFdbNumDhcpEntries,
       "svcTlsFdbNumHostEntries": svcTlsFdbNumHostEntries,
       "svcTlsShcvAction": svcTlsShcvAction,
       "svcTlsShcvSrcIp": svcTlsShcvSrcIp,
       "svcTlsShcvSrcMac": svcTlsShcvSrcMac,
       "svcTlsShcvInterval": svcTlsShcvInterval,
       "svcTlsPriPortsCumulativeFactor": svcTlsPriPortsCumulativeFactor,
       "svcTlsSecPortsCumulativeFactor": svcTlsSecPortsCumulativeFactor,
       "svcTlsL2ptTermEnabled": svcTlsL2ptTermEnabled,
       "svcTlsPropagateMacFlush": svcTlsPropagateMacFlush,
       "svcTlsMrpAdminStatus": svcTlsMrpAdminStatus,
       "svcTlsMrpMaxAttributes": svcTlsMrpMaxAttributes,
       "svcTlsMrpAttributeCount": svcTlsMrpAttributeCount,
       "svcTlsMrpFailedRegisterCount": svcTlsMrpFailedRegisterCount,
       "svcTlsMcPathMgmtPlcyName": svcTlsMcPathMgmtPlcyName,
       "svcTlsMrpFloodTime": svcTlsMrpFloodTime,
       "svcTlsMrpAttrTblHighWatermark": svcTlsMrpAttrTblHighWatermark,
       "svcTlsMrpAttrTblLowWatermark": svcTlsMrpAttrTblLowWatermark,
       "svcTlsMacMoveNumRetries": svcTlsMacMoveNumRetries,
       "svcTlsMacSubNetLen": svcTlsMacSubNetLen,
       "svcTlsSendFlushOnBVplsFail": svcTlsSendFlushOnBVplsFail,
       "svcTlsPropMacFlushFromBVpls": svcTlsPropMacFlushFromBVpls,
       "svcTlsMacNotifInterval": svcTlsMacNotifInterval,
       "svcTlsMacNotifCount": svcTlsMacNotifCount,
       "svcTlsMacNotifAdminState": svcTlsMacNotifAdminState,
       "svcTlsPerSvcHashing": svcTlsPerSvcHashing,
       "svcTlsAllowIpIfBinding": svcTlsAllowIpIfBinding,
       "svcTlsShcvRetryTimeout": svcTlsShcvRetryTimeout,
       "svcTlsShcvRetryCount": svcTlsShcvRetryCount,
       "svcTlsTempFloodTime": svcTlsTempFloodTime,
       "svcTlsTempFloodActive": svcTlsTempFloodActive,
       "svcTlsTempFloodChangeCount": svcTlsTempFloodChangeCount,
       "tlsFdbInfoTable": tlsFdbInfoTable,
       "tlsFdbInfoEntry": tlsFdbInfoEntry,
       "tlsFdbMacAddr": tlsFdbMacAddr,
       "tlsFdbRowStatus": tlsFdbRowStatus,
       "tlsFdbType": tlsFdbType,
       "tlsFdbLocale": tlsFdbLocale,
       "tlsFdbPortId": tlsFdbPortId,
       "tlsFdbEncapValue": tlsFdbEncapValue,
       "tlsFdbSdpId": tlsFdbSdpId,
       "tlsFdbVcId": tlsFdbVcId,
       "tlsFdbVpnId": tlsFdbVpnId,
       "tlsFdbCustId": tlsFdbCustId,
       "tlsFdbLastStateChange": tlsFdbLastStateChange,
       "tlsFdbProtected": tlsFdbProtected,
       "tlsFdbBackboneDstMac": tlsFdbBackboneDstMac,
       "tlsFdbNumIVplsMac": tlsFdbNumIVplsMac,
       "tlsFdbEndPointName": tlsFdbEndPointName,
       "tlsFdbEPMacOperSdpId": tlsFdbEPMacOperSdpId,
       "tlsFdbEPMacOperVcId": tlsFdbEPMacOperVcId,
       "tlsFdbPbbNumEpipes": tlsFdbPbbNumEpipes,
       "iesIfTable": iesIfTable,
       "iesIfEntry": iesIfEntry,
       "iesIfIndex": iesIfIndex,
       "iesIfRowStatus": iesIfRowStatus,
       "iesIfName": iesIfName,
       "iesIfDescription": iesIfDescription,
       "iesIfAdminStatus": iesIfAdminStatus,
       "iesIfOperStatus": iesIfOperStatus,
       "iesIfLastMgmtChange": iesIfLastMgmtChange,
       "iesIfVpnId": iesIfVpnId,
       "iesIfCustId": iesIfCustId,
       "iesIfLoopback": iesIfLoopback,
       "iesIfLastStatusChange": iesIfLastStatusChange,
       "iesIfType": iesIfType,
       "iesIfParentIf": iesIfParentIf,
       "iesIfShcvSource": iesIfShcvSource,
       "iesIfShcvAction": iesIfShcvAction,
       "iesIfShcvInterval": iesIfShcvInterval,
       "iesIfFwdServId": iesIfFwdServId,
       "iesIfFwdSubIf": iesIfFwdSubIf,
       "iesIfPrivateRetailSubnets": iesIfPrivateRetailSubnets,
       "iesIfDelegatedPrefixLen": iesIfDelegatedPrefixLen,
       "iesIfLns": iesIfLns,
       "iesIfVplsName": iesIfVplsName,
       "iesIfVplsStatus": iesIfVplsStatus,
       "iesIfVplsFailedReason": iesIfVplsFailedReason,
       "iesIfShcvRetryTimeout": iesIfShcvRetryTimeout,
       "iesIfShcvRetryCount": iesIfShcvRetryCount,
       "iesIfSapEgressQosId": iesIfSapEgressQosId,
       "iesIfDefaultPrimaryDnsIPv4Addr": iesIfDefaultPrimaryDnsIPv4Addr,
       "iesIfDefaultSecondaryDnsIPv4Addr": iesIfDefaultSecondaryDnsIPv4Addr,
       "iesIfDefaultPrimaryDnsIPv6Addr": iesIfDefaultPrimaryDnsIPv6Addr,
       "iesIfDefaultSecondaryDnsIPv6Addr": iesIfDefaultSecondaryDnsIPv6Addr,
       "iesIfIPv6ConfigAllowed": iesIfIPv6ConfigAllowed,
       "iesIfSrrpRoutingEnabled": iesIfSrrpRoutingEnabled,
       "iesIfSrrpRoutingHoldTime": iesIfSrrpRoutingHoldTime,
       "iesIfMonitorOperGrp": iesIfMonitorOperGrp,
       "iesIfAllowUnmatchingSubnets": iesIfAllowUnmatchingSubnets,
       "iesIfGroupInterfaceType": iesIfGroupInterfaceType,
       "iesIfShcvFamily": iesIfShcvFamily,
       "iesIfIPv6IpoeBridgedModeEnabled": iesIfIPv6IpoeBridgedModeEnabled,
       "iesIfIPv6AllowUnmatchingPfxs": iesIfIPv6AllowUnmatchingPfxs,
       "tlsShgInfoTable": tlsShgInfoTable,
       "tlsShgInfoEntry": tlsShgInfoEntry,
       "tlsShgName": tlsShgName,
       "tlsShgRowStatus": tlsShgRowStatus,
       "tlsShgCustId": tlsShgCustId,
       "tlsShgInstanceId": tlsShgInstanceId,
       "tlsShgDescription": tlsShgDescription,
       "tlsShgLastMgmtChange": tlsShgLastMgmtChange,
       "tlsShgResidential": tlsShgResidential,
       "tlsShgRestProtSrcMac": tlsShgRestProtSrcMac,
       "tlsShgRestUnprotDstMac": tlsShgRestUnprotDstMac,
       "tlsShgRestProtSrcMacAction": tlsShgRestProtSrcMacAction,
       "tlsShgCreationOrigin": tlsShgCreationOrigin,
       "tlsShgSiteName": tlsShgSiteName,
       "tlsShgAutoLearnMacProtect": tlsShgAutoLearnMacProtect,
       "svcApipeInfoTable": svcApipeInfoTable,
       "svcApipeInfoEntry": svcApipeInfoEntry,
       "svcApipeInterworking": svcApipeInterworking,
       "svcApipeSignaledVllTypeOverride": svcApipeSignaledVllTypeOverride,
       "tlsMFibInfoTable": tlsMFibInfoTable,
       "tlsMFibInfoEntry": tlsMFibInfoEntry,
       "tlsMFibInfoGrpAddr": tlsMFibInfoGrpAddr,
       "tlsMFibInfoSrcAddr": tlsMFibInfoSrcAddr,
       "tlsMFibInfoLocale": tlsMFibInfoLocale,
       "tlsMFibInfoPortId": tlsMFibInfoPortId,
       "tlsMFibInfoEncapValue": tlsMFibInfoEncapValue,
       "tlsMFibInfoSdpId": tlsMFibInfoSdpId,
       "tlsMFibInfoVcId": tlsMFibInfoVcId,
       "tlsMFibInfoFwdOrBlk": tlsMFibInfoFwdOrBlk,
       "tlsMFibInfoSvcId": tlsMFibInfoSvcId,
       "tlsMFibGrpSrcStatsTable": tlsMFibGrpSrcStatsTable,
       "tlsMFibGrpSrcStatsEntry": tlsMFibGrpSrcStatsEntry,
       "tlsMFibGrpSrcStatsGrpAddr": tlsMFibGrpSrcStatsGrpAddr,
       "tlsMFibGrpSrcStatsSrcAddr": tlsMFibGrpSrcStatsSrcAddr,
       "tlsMFibGrpSrcStatsForwardedPkts": tlsMFibGrpSrcStatsForwardedPkts,
       "tlsMFibGrpSrcStatsForwardedOctets": tlsMFibGrpSrcStatsForwardedOctets,
       "tlsRdntGrpTable": tlsRdntGrpTable,
       "tlsRdntGrpEntry": tlsRdntGrpEntry,
       "tlsRdntGrpName": tlsRdntGrpName,
       "tlsRdntGrpRowStatus": tlsRdntGrpRowStatus,
       "tlsRdntGrpDescription": tlsRdntGrpDescription,
       "tlsRdntGrpLastMgmtChange": tlsRdntGrpLastMgmtChange,
       "tlsRdntGrpMemberTable": tlsRdntGrpMemberTable,
       "tlsRdntGrpMemberEntry": tlsRdntGrpMemberEntry,
       "tlsRdntGrpMemberRemoteNodeAddrTp": tlsRdntGrpMemberRemoteNodeAddrTp,
       "tlsRdntGrpMemberRemoteNodeAddr": tlsRdntGrpMemberRemoteNodeAddr,
       "tlsRdntGrpMemberIsSap": tlsRdntGrpMemberIsSap,
       "tlsRdntGrpMemberPort": tlsRdntGrpMemberPort,
       "tlsRdntGrpMemberEncap": tlsRdntGrpMemberEncap,
       "tlsRdntGrpMemberRowStatus": tlsRdntGrpMemberRowStatus,
       "tlsRdntGrpMemberLastMgmtChange": tlsRdntGrpMemberLastMgmtChange,
       "tlsMstiTable": tlsMstiTable,
       "tlsMstiEntry": tlsMstiEntry,
       "tlsMstiInstanceId": tlsMstiInstanceId,
       "tlsMstiRowStatus": tlsMstiRowStatus,
       "tlsMstiPriority": tlsMstiPriority,
       "tlsMstiLastMgmtChange": tlsMstiLastMgmtChange,
       "tlsMstiRegionalRoot": tlsMstiRegionalRoot,
       "tlsMstiIntRootCost": tlsMstiIntRootCost,
       "tlsMstiRemainingHopCount": tlsMstiRemainingHopCount,
       "tlsMstiRegionalRootPort": tlsMstiRegionalRootPort,
       "tlsMstiManagedVlanListTable": tlsMstiManagedVlanListTable,
       "tlsMstiManagedVlanListEntry": tlsMstiManagedVlanListEntry,
       "tlsMstiMvplsMinVlanTag": tlsMstiMvplsMinVlanTag,
       "tlsMstiMvplsMaxVlanTag": tlsMstiMvplsMaxVlanTag,
       "tlsMstiMvplsRowStatus": tlsMstiMvplsRowStatus,
       "tlsEgressMulticastGroupTable": tlsEgressMulticastGroupTable,
       "tlsEgressMulticastGroupEntry": tlsEgressMulticastGroupEntry,
       "tlsEgrMcGrpName": tlsEgrMcGrpName,
       "tlsEgrMcGrpRowStatus": tlsEgrMcGrpRowStatus,
       "tlsEgrMcGrpLastMgmtChange": tlsEgrMcGrpLastMgmtChange,
       "tlsEgrMcGrpDescription": tlsEgrMcGrpDescription,
       "tlsEgrMcGrpChainLimit": tlsEgrMcGrpChainLimit,
       "tlsEgrMcGrpEncapType": tlsEgrMcGrpEncapType,
       "tlsEgrMcGrpDot1qEtherType": tlsEgrMcGrpDot1qEtherType,
       "tlsEgrMcGrpMacFilterId": tlsEgrMcGrpMacFilterId,
       "tlsEgrMcGrpIpFilterId": tlsEgrMcGrpIpFilterId,
       "tlsEgrMcGrpIpv6FilterId": tlsEgrMcGrpIpv6FilterId,
       "tlsEgrMcGrpQinqEtherType": tlsEgrMcGrpQinqEtherType,
       "tlsEgrMcGrpQinqFixedTagPosition": tlsEgrMcGrpQinqFixedTagPosition,
       "tlsEgrMcGrpAdminQinqFixedTagVal": tlsEgrMcGrpAdminQinqFixedTagVal,
       "tlsEgrMcGrpOperQinqFixedTagVal": tlsEgrMcGrpOperQinqFixedTagVal,
       "svcDhcpLeaseStateTable": svcDhcpLeaseStateTable,
       "svcDhcpLeaseStateEntry": svcDhcpLeaseStateEntry,
       "svcDhcpLseStateCiAddrType": svcDhcpLseStateCiAddrType,
       "svcDhcpLseStateCiAddr": svcDhcpLseStateCiAddr,
       "svcDhcpLseStateLocale": svcDhcpLseStateLocale,
       "svcDhcpLseStatePortId": svcDhcpLseStatePortId,
       "svcDhcpLseStateEncapValue": svcDhcpLseStateEncapValue,
       "svcDhcpLseStateSdpId": svcDhcpLseStateSdpId,
       "svcDhcpLseStateVcId": svcDhcpLseStateVcId,
       "svcDhcpLseStateChAddr": svcDhcpLseStateChAddr,
       "svcDhcpLseStateRemainLseTime": svcDhcpLseStateRemainLseTime,
       "svcDhcpLseStateOption82": svcDhcpLseStateOption82,
       "svcDhcpLseStatePersistKey": svcDhcpLseStatePersistKey,
       "svcDhcpLseStateSubscrIdent": svcDhcpLseStateSubscrIdent,
       "svcDhcpLseStateSubProfString": svcDhcpLseStateSubProfString,
       "svcDhcpLseStateSlaProfString": svcDhcpLseStateSlaProfString,
       "svcDhcpLseStateShcvOperState": svcDhcpLseStateShcvOperState,
       "svcDhcpLseStateShcvChecks": svcDhcpLseStateShcvChecks,
       "svcDhcpLseStateShcvReplies": svcDhcpLseStateShcvReplies,
       "svcDhcpLseStateShcvReplyTime": svcDhcpLseStateShcvReplyTime,
       "svcDhcpLseStateClientId": svcDhcpLseStateClientId,
       "svcDhcpLseStateIAID": svcDhcpLseStateIAID,
       "svcDhcpLseStateIAIDType": svcDhcpLseStateIAIDType,
       "svcDhcpLseStateCiAddrMaskLen": svcDhcpLseStateCiAddrMaskLen,
       "svcDhcpLseStateRetailerSvcId": svcDhcpLseStateRetailerSvcId,
       "svcDhcpLseStateRetailerIf": svcDhcpLseStateRetailerIf,
       "svcDhcpLseStateAncpString": svcDhcpLseStateAncpString,
       "svcDhcpLseStateFramedIpNetMaskTp": svcDhcpLseStateFramedIpNetMaskTp,
       "svcDhcpLseStateFramedIpNetMask": svcDhcpLseStateFramedIpNetMask,
       "svcDhcpLseStateBCastIpAddrType": svcDhcpLseStateBCastIpAddrType,
       "svcDhcpLseStateBCastIpAddr": svcDhcpLseStateBCastIpAddr,
       "svcDhcpLseStateDefaultRouterTp": svcDhcpLseStateDefaultRouterTp,
       "svcDhcpLseStateDefaultRouter": svcDhcpLseStateDefaultRouter,
       "svcDhcpLseStatePrimaryDnsType": svcDhcpLseStatePrimaryDnsType,
       "svcDhcpLseStatePrimaryDns": svcDhcpLseStatePrimaryDns,
       "svcDhcpLseStateSecondaryDnsType": svcDhcpLseStateSecondaryDnsType,
       "svcDhcpLseStateSecondaryDns": svcDhcpLseStateSecondaryDns,
       "svcDhcpLseStateSessionTimeout": svcDhcpLseStateSessionTimeout,
       "svcDhcpLseStateServerLeaseStart": svcDhcpLseStateServerLeaseStart,
       "svcDhcpLseStateServerLastRenew": svcDhcpLseStateServerLastRenew,
       "svcDhcpLseStateServerLeaseEnd": svcDhcpLseStateServerLeaseEnd,
       "svcDhcpLseStateDhcpServerAddrType": svcDhcpLseStateDhcpServerAddrType,
       "svcDhcpLseStateDhcpServerAddr": svcDhcpLseStateDhcpServerAddr,
       "svcDhcpLseStateOriginSubscrId": svcDhcpLseStateOriginSubscrId,
       "svcDhcpLseStateOriginStrings": svcDhcpLseStateOriginStrings,
       "svcDhcpLseStateOriginLeaseInfo": svcDhcpLseStateOriginLeaseInfo,
       "svcDhcpLseStateDhcpClientAddrType": svcDhcpLseStateDhcpClientAddrType,
       "svcDhcpLseStateDhcpClientAddr": svcDhcpLseStateDhcpClientAddr,
       "svcDhcpLseStateLeaseSplitActive": svcDhcpLseStateLeaseSplitActive,
       "svcDhcpLseStateInterDestId": svcDhcpLseStateInterDestId,
       "svcDhcpLseStatePrimaryNbnsType": svcDhcpLseStatePrimaryNbnsType,
       "svcDhcpLseStatePrimaryNbns": svcDhcpLseStatePrimaryNbns,
       "svcDhcpLseStateSecondaryNbnsType": svcDhcpLseStateSecondaryNbnsType,
       "svcDhcpLseStateSecondaryNbns": svcDhcpLseStateSecondaryNbns,
       "svcDhcpLseStateAppProfString": svcDhcpLseStateAppProfString,
       "svcDhcpLseStateNextHopMacAddr": svcDhcpLseStateNextHopMacAddr,
       "svcDhcpLseStateCategoryMapName": svcDhcpLseStateCategoryMapName,
       "svcDhcpLseStateNakNextRenew": svcDhcpLseStateNakNextRenew,
       "svcDhcpLseStateRadiusClassAttr": svcDhcpLseStateRadiusClassAttr,
       "svcDhcpLseStateRadiusUserName": svcDhcpLseStateRadiusUserName,
       "tlsProtectedMacTable": tlsProtectedMacTable,
       "tlsProtectedMacEntry": tlsProtectedMacEntry,
       "tlsProtMacAddress": tlsProtMacAddress,
       "tlsProtMacRowStatus": tlsProtMacRowStatus,
       "tlsProtMacLastMgmtChange": tlsProtMacLastMgmtChange,
       "svcDhcpLeaseStateModifyTable": svcDhcpLeaseStateModifyTable,
       "svcDhcpLeaseStateModifyEntry": svcDhcpLeaseStateModifyEntry,
       "svcDhcpLseStateModifySubIndent": svcDhcpLseStateModifySubIndent,
       "svcDhcpLseStateModifySubProfile": svcDhcpLseStateModifySubProfile,
       "svcDhcpLseStateModifySlaProfile": svcDhcpLseStateModifySlaProfile,
       "svcDhcpLseStateEvaluateState": svcDhcpLseStateEvaluateState,
       "svcDhcpLseStateModInterDestId": svcDhcpLseStateModInterDestId,
       "svcDhcpLseStateModifyAncpString": svcDhcpLseStateModifyAncpString,
       "svcDhcpLseStateModifyAppProfile": svcDhcpLseStateModifyAppProfile,
       "svcEndPointTable": svcEndPointTable,
       "svcEndPointEntry": svcEndPointEntry,
       "svcEndPointName": svcEndPointName,
       "svcEndPointRowStatus": svcEndPointRowStatus,
       "svcEndPointDescription": svcEndPointDescription,
       "svcEndPointRevertTime": svcEndPointRevertTime,
       "svcEndPointTxActiveType": svcEndPointTxActiveType,
       "svcEndPointTxActivePortId": svcEndPointTxActivePortId,
       "svcEndPointTxActiveEncap": svcEndPointTxActiveEncap,
       "svcEndPointTxActiveSdpId": svcEndPointTxActiveSdpId,
       "svcEndPointForceSwitchOver": svcEndPointForceSwitchOver,
       "svcEndPointForceSwitchOverSdpId": svcEndPointForceSwitchOverSdpId,
       "svcEndPointActiveHoldDelay": svcEndPointActiveHoldDelay,
       "svcEndPointIgnoreStandbySig": svcEndPointIgnoreStandbySig,
       "svcEndPointMacPinning": svcEndPointMacPinning,
       "svcEndPointMacLimit": svcEndPointMacLimit,
       "svcEndPointSuppressStandbySig": svcEndPointSuppressStandbySig,
       "svcEndPointRevertTimeCountDn": svcEndPointRevertTimeCountDn,
       "svcEndPointTxActiveChangeCount": svcEndPointTxActiveChangeCount,
       "svcEndPointTxActiveLastChange": svcEndPointTxActiveLastChange,
       "svcEndPointTxActiveUpTime": svcEndPointTxActiveUpTime,
       "svcEndPointMCEPId": svcEndPointMCEPId,
       "svcEndPointMCEPPeerAddrType": svcEndPointMCEPPeerAddrType,
       "svcEndPointMCEPPeerAddr": svcEndPointMCEPPeerAddr,
       "svcEndPointMCEPPeerName": svcEndPointMCEPPeerName,
       "svcEndPointBlockOnMeshFail": svcEndPointBlockOnMeshFail,
       "svcEndPointMCEPPsvModeActive": svcEndPointMCEPPsvModeActive,
       "svcEndPointStandbySigMaster": svcEndPointStandbySigMaster,
       "svcEndPointStandbySigSlave": svcEndPointStandbySigSlave,
       "svcEndPointForceSwitchOvrSdpFec": svcEndPointForceSwitchOvrSdpFec,
       "svcEndPointTxActiveSdpFec": svcEndPointTxActiveSdpFec,
       "svcEndPointRestProtSrcMac": svcEndPointRestProtSrcMac,
       "svcEndPointRestProtSrcMacAction": svcEndPointRestProtSrcMacAction,
       "svcEndPointAutoLearnMacProtect": svcEndPointAutoLearnMacProtect,
       "iesGrpIfTable": iesGrpIfTable,
       "iesGrpIfEntry": iesGrpIfEntry,
       "iesGrpIfRedInterface": iesGrpIfRedInterface,
       "iesGrpIfOperUpWhileEmpty": iesGrpIfOperUpWhileEmpty,
       "iesGrpIfPolicyControl": iesGrpIfPolicyControl,
       "svcPEDiscoveryPolicyTable": svcPEDiscoveryPolicyTable,
       "svcPEDiscoveryPolicyEntry": svcPEDiscoveryPolicyEntry,
       "svcPEDiscoveryPolicyName": svcPEDiscoveryPolicyName,
       "svcPEDiscoveryPolicyRowStatus": svcPEDiscoveryPolicyRowStatus,
       "svcPEDiscoveryPolicyPassword": svcPEDiscoveryPolicyPassword,
       "svcPEDiscoveryPolicyInterval": svcPEDiscoveryPolicyInterval,
       "svcPEDiscoveryPolicyTimeout": svcPEDiscoveryPolicyTimeout,
       "svcPEDiscPolServerTable": svcPEDiscPolServerTable,
       "svcPEDiscPolServerEntry": svcPEDiscPolServerEntry,
       "svcPEDiscPolServerIndex": svcPEDiscPolServerIndex,
       "svcPEDiscPolServerRowStatus": svcPEDiscPolServerRowStatus,
       "svcPEDiscPolServerAddressType": svcPEDiscPolServerAddressType,
       "svcPEDiscPolServerAddress": svcPEDiscPolServerAddress,
       "svcPEDiscPolServerSecret": svcPEDiscPolServerSecret,
       "svcPEDiscPolServerOperStatus": svcPEDiscPolServerOperStatus,
       "svcPEDiscPolServerPort": svcPEDiscPolServerPort,
       "svcWholesalerInfoTable": svcWholesalerInfoTable,
       "svcWholesalerInfoEntry": svcWholesalerInfoEntry,
       "svcWholesalerID": svcWholesalerID,
       "svcWholesalerNumStaticHosts": svcWholesalerNumStaticHosts,
       "svcWholesalerNumDynamicHosts": svcWholesalerNumDynamicHosts,
       "svcWholesalerNumDhcpLeaseStates": svcWholesalerNumDhcpLeaseStates,
       "svcWholesalerNumPppoeSessions": svcWholesalerNumPppoeSessions,
       "svcWholesalerNumArpHosts": svcWholesalerNumArpHosts,
       "svcDhcpLeaseStateActionTable": svcDhcpLeaseStateActionTable,
       "svcDhcpLeaseStateActionEntry": svcDhcpLeaseStateActionEntry,
       "svcDhcpLseStateForceRenew": svcDhcpLseStateForceRenew,
       "svcIfDHCP6MsgStatTable": svcIfDHCP6MsgStatTable,
       "svcIfDHCP6MsgStatEntry": svcIfDHCP6MsgStatEntry,
       "svcIfDHCP6MsgStatsLstClrd": svcIfDHCP6MsgStatsLstClrd,
       "svcIfDHCP6MsgStatsRcvd": svcIfDHCP6MsgStatsRcvd,
       "svcIfDHCP6MsgStatsSent": svcIfDHCP6MsgStatsSent,
       "svcIfDHCP6MsgStatsDropped": svcIfDHCP6MsgStatsDropped,
       "svcTlsBackboneInfoTable": svcTlsBackboneInfoTable,
       "svcTlsBackboneInfoEntry": svcTlsBackboneInfoEntry,
       "svcTlsBackboneSrcMac": svcTlsBackboneSrcMac,
       "svcTlsBackboneVplsSvcId": svcTlsBackboneVplsSvcId,
       "svcTlsBackboneVplsSvcISID": svcTlsBackboneVplsSvcISID,
       "svcTlsBackboneOperSrcMac": svcTlsBackboneOperSrcMac,
       "svcTlsBackboneOperVplsSvcISID": svcTlsBackboneOperVplsSvcISID,
       "svcTlsBackboneLDPMacFlush": svcTlsBackboneLDPMacFlush,
       "svcTlsBackboneVplsStp": svcTlsBackboneVplsStp,
       "svcTlsBackboneLDPMacFlushNotMine": svcTlsBackboneLDPMacFlushNotMine,
       "svcTlsBackboneUseSapBMac": svcTlsBackboneUseSapBMac,
       "svcTlsBackboneForceQTagFwd": svcTlsBackboneForceQTagFwd,
       "tlsMFibTable": tlsMFibTable,
       "tlsMFibEntry": tlsMFibEntry,
       "tlsMFibEntryType": tlsMFibEntryType,
       "tlsMFibGrpMacAddr": tlsMFibGrpMacAddr,
       "tlsMFibGrpInetAddrType": tlsMFibGrpInetAddrType,
       "tlsMFibGrpInetAddr": tlsMFibGrpInetAddr,
       "tlsMFibSrcInetAddrType": tlsMFibSrcInetAddrType,
       "tlsMFibSrcInetAddr": tlsMFibSrcInetAddr,
       "tlsMFibLocale": tlsMFibLocale,
       "tlsMFibPortId": tlsMFibPortId,
       "tlsMFibEncapValue": tlsMFibEncapValue,
       "tlsMFibSdpId": tlsMFibSdpId,
       "tlsMFibVcId": tlsMFibVcId,
       "tlsMFibFwdOrBlk": tlsMFibFwdOrBlk,
       "tlsMFibSvcId": tlsMFibSvcId,
       "tlsMFibStatsTable": tlsMFibStatsTable,
       "tlsMFibStatsEntry": tlsMFibStatsEntry,
       "tlsMFibStatsEntryType": tlsMFibStatsEntryType,
       "tlsMFibStatsGrpMacAddr": tlsMFibStatsGrpMacAddr,
       "tlsMFibStatsGrpInetAddrType": tlsMFibStatsGrpInetAddrType,
       "tlsMFibStatsGrpInetAddr": tlsMFibStatsGrpInetAddr,
       "tlsMFibStatsSrcInetAddrType": tlsMFibStatsSrcInetAddrType,
       "tlsMFibStatsSrcInetAddr": tlsMFibStatsSrcInetAddr,
       "tlsMFibStatsForwardedPkts": tlsMFibStatsForwardedPkts,
       "tlsMFibStatsForwardedOctets": tlsMFibStatsForwardedOctets,
       "svcTlsBgpADTableLastChanged": svcTlsBgpADTableLastChanged,
       "svcTlsBgpADTable": svcTlsBgpADTable,
       "svcTlsBgpADEntry": svcTlsBgpADEntry,
       "svcTlsBgpADRowStatus": svcTlsBgpADRowStatus,
       "svcTlsBgpADLastChanged": svcTlsBgpADLastChanged,
       "svcTlsBgpADVplsId": svcTlsBgpADVplsId,
       "svcTlsBgpADVsiPrefix": svcTlsBgpADVsiPrefix,
       "svcTlsBgpADVsiRD": svcTlsBgpADVsiRD,
       "svcTlsBgpADExportRteTarget": svcTlsBgpADExportRteTarget,
       "svcTlsBgpADVsiExportPolicy1": svcTlsBgpADVsiExportPolicy1,
       "svcTlsBgpADVsiExportPolicy2": svcTlsBgpADVsiExportPolicy2,
       "svcTlsBgpADVsiExportPolicy3": svcTlsBgpADVsiExportPolicy3,
       "svcTlsBgpADVsiExportPolicy4": svcTlsBgpADVsiExportPolicy4,
       "svcTlsBgpADVsiExportPolicy5": svcTlsBgpADVsiExportPolicy5,
       "svcTlsBgpADImportRteTarget": svcTlsBgpADImportRteTarget,
       "svcTlsBgpADVsiImportPolicy1": svcTlsBgpADVsiImportPolicy1,
       "svcTlsBgpADVsiImportPolicy2": svcTlsBgpADVsiImportPolicy2,
       "svcTlsBgpADVsiImportPolicy3": svcTlsBgpADVsiImportPolicy3,
       "svcTlsBgpADVsiImportPolicy4": svcTlsBgpADVsiImportPolicy4,
       "svcTlsBgpADVsiImportPolicy5": svcTlsBgpADVsiImportPolicy5,
       "svcTlsBgpADAdminStatus": svcTlsBgpADAdminStatus,
       "svcEpipePbbTableLastChanged": svcEpipePbbTableLastChanged,
       "svcEpipePbbTable": svcEpipePbbTable,
       "svcEpipePbbEntry": svcEpipePbbEntry,
       "svcEpipePbbRowStatus": svcEpipePbbRowStatus,
       "svcEpipePbbLastChngd": svcEpipePbbLastChngd,
       "svcEpipePbbBvplsSvcId": svcEpipePbbBvplsSvcId,
       "svcEpipePbbBvplsDstMac": svcEpipePbbBvplsDstMac,
       "svcEpipePbbSvcISID": svcEpipePbbSvcISID,
       "svcEpipePbbOperState": svcEpipePbbOperState,
       "svcEpipePbbFlooding": svcEpipePbbFlooding,
       "svcEpipePbbLastStatusChange": svcEpipePbbLastStatusChange,
       "svcEpipePbbBvplsOperDstMac": svcEpipePbbBvplsOperDstMac,
       "svcEpipePbbBvplsDstMacName": svcEpipePbbBvplsDstMacName,
       "tlsPipInfoTable": tlsPipInfoTable,
       "tlsPipInfoEntry": tlsPipInfoEntry,
       "tlsPipStpPortState": tlsPipStpPortState,
       "tlsPipStpPortRole": tlsPipStpPortRole,
       "tlsPipStpDesignatedBridge": tlsPipStpDesignatedBridge,
       "tlsPipStpDesignatedPort": tlsPipStpDesignatedPort,
       "tlsPipStpException": tlsPipStpException,
       "tlsPipStpForwardTransitions": tlsPipStpForwardTransitions,
       "tlsPipStpInConfigBpdus": tlsPipStpInConfigBpdus,
       "tlsPipStpInTcnBpdus": tlsPipStpInTcnBpdus,
       "tlsPipStpInRstBpdus": tlsPipStpInRstBpdus,
       "tlsPipStpInMstBpdus": tlsPipStpInMstBpdus,
       "tlsPipStpInBadBpdus": tlsPipStpInBadBpdus,
       "tlsPipStpOutConfigBpdus": tlsPipStpOutConfigBpdus,
       "tlsPipStpOutTcnBpdus": tlsPipStpOutTcnBpdus,
       "tlsPipStpOutRstBpdus": tlsPipStpOutRstBpdus,
       "tlsPipStpOutMstBpdus": tlsPipStpOutMstBpdus,
       "tlsPipStpOperStatus": tlsPipStpOperStatus,
       "tlsPipStpMvplsPruneState": tlsPipStpMvplsPruneState,
       "tlsPipStpOperProtocol": tlsPipStpOperProtocol,
       "tlsPipStpPortNum": tlsPipStpPortNum,
       "tlsPipStpInsideRegion": tlsPipStpInsideRegion,
       "tlsPipInTcBitBpdus": tlsPipInTcBitBpdus,
       "tlsPipOutTcBitBpdus": tlsPipOutTcBitBpdus,
       "tlsPipMstiTable": tlsPipMstiTable,
       "tlsPipMstiEntry": tlsPipMstiEntry,
       "tlsPipMstiPortRole": tlsPipMstiPortRole,
       "tlsPipMstiPortState": tlsPipMstiPortState,
       "tlsPipMstiDesignatedBridge": tlsPipMstiDesignatedBridge,
       "tlsPipMstiDesignatedPort": tlsPipMstiDesignatedPort,
       "svcTotalFdbMimDestIdxEntries": svcTotalFdbMimDestIdxEntries,
       "svcDhcpManagedRouteTable": svcDhcpManagedRouteTable,
       "svcDhcpManagedRouteEntry": svcDhcpManagedRouteEntry,
       "svcDhcpManagedRouteInetAddrType": svcDhcpManagedRouteInetAddrType,
       "svcDhcpManagedRouteInetAddr": svcDhcpManagedRouteInetAddr,
       "svcDhcpManagedRoutePrefixLen": svcDhcpManagedRoutePrefixLen,
       "svcDhcpManagedRouteStatus": svcDhcpManagedRouteStatus,
       "svcArpHostTableLastChanged": svcArpHostTableLastChanged,
       "svcArpHostTable": svcArpHostTable,
       "svcArpHostEntry": svcArpHostEntry,
       "svcArpHostIpAddrType": svcArpHostIpAddrType,
       "svcArpHostIpAddr": svcArpHostIpAddr,
       "svcArpHostLocale": svcArpHostLocale,
       "svcArpHostSapPortId": svcArpHostSapPortId,
       "svcArpHostSapEncapValue": svcArpHostSapEncapValue,
       "svcArpHostSdpId": svcArpHostSdpId,
       "svcArpHostVcId": svcArpHostVcId,
       "svcArpHostSessionTimeout": svcArpHostSessionTimeout,
       "svcArpHostStart": svcArpHostStart,
       "svcArpHostLastAuth": svcArpHostLastAuth,
       "svcArpHostRefresh": svcArpHostRefresh,
       "svcArpHostRemainingTime": svcArpHostRemainingTime,
       "svcArpHostShcvOperState": svcArpHostShcvOperState,
       "svcArpHostShcvChecks": svcArpHostShcvChecks,
       "svcArpHostShcvReplies": svcArpHostShcvReplies,
       "svcArpHostShcvReplyTime": svcArpHostShcvReplyTime,
       "svcArpHostSubscrIdent": svcArpHostSubscrIdent,
       "svcArpHostSubProfString": svcArpHostSubProfString,
       "svcArpHostSlaProfString": svcArpHostSlaProfString,
       "svcArpHostAppProfString": svcArpHostAppProfString,
       "svcArpHostAncpString": svcArpHostAncpString,
       "svcArpHostInterDestId": svcArpHostInterDestId,
       "svcArpHostRetailerSvcId": svcArpHostRetailerSvcId,
       "svcArpHostRetailerIf": svcArpHostRetailerIf,
       "svcArpHostMacAddr": svcArpHostMacAddr,
       "svcArpHostPersistKey": svcArpHostPersistKey,
       "svcArpHostCategoryMapName": svcArpHostCategoryMapName,
       "svcArpHostRadiusClassAttr": svcArpHostRadiusClassAttr,
       "svcArpHostRadiusUserName": svcArpHostRadiusUserName,
       "svcArpHostOriginSubscrId": svcArpHostOriginSubscrId,
       "svcArpHostOriginStrings": svcArpHostOriginStrings,
       "svcArpHostIfTableLastMgmtChange": svcArpHostIfTableLastMgmtChange,
       "svcArpHostIfTable": svcArpHostIfTable,
       "svcArpHostIfEntry": svcArpHostIfEntry,
       "svcArpHostIfLastMgmtChange": svcArpHostIfLastMgmtChange,
       "svcArpHostIfAdminState": svcArpHostIfAdminState,
       "svcArpHostIfMaxNumHosts": svcArpHostIfMaxNumHosts,
       "svcArpHostIfMaxNumHostsSap": svcArpHostIfMaxNumHostsSap,
       "svcArpHostIfMinAuthInterval": svcArpHostIfMinAuthInterval,
       "svcArpHostIfNumHosts": svcArpHostIfNumHosts,
       "svcArpHostDefaultSessionTimeout": svcArpHostDefaultSessionTimeout,
       "svcIgmpTrkTableLastMgmtChange": svcIgmpTrkTableLastMgmtChange,
       "svcIgmpTrkTable": svcIgmpTrkTable,
       "svcIgmpTrkEntry": svcIgmpTrkEntry,
       "svcIgmpTrkLastMgmtChange": svcIgmpTrkLastMgmtChange,
       "svcIgmpTrkAdminState": svcIgmpTrkAdminState,
       "svcIgmpTrkExpiryTime": svcIgmpTrkExpiryTime,
       "svcIpipeInfoTableLastMgmtChange": svcIpipeInfoTableLastMgmtChange,
       "svcIpipeInfoTable": svcIpipeInfoTable,
       "svcIpipeInfoEntry": svcIpipeInfoEntry,
       "svcIpipeInfoLastMgmtChange": svcIpipeInfoLastMgmtChange,
       "svcIpipeCeAddressDiscovery": svcIpipeCeAddressDiscovery,
       "svcIpipeIpv6CeAddressDiscovery": svcIpipeIpv6CeAddressDiscovery,
       "svcIpipeStackCapabilitySignaling": svcIpipeStackCapabilitySignaling,
       "svcDhcpLeaseStateBgpTable": svcDhcpLeaseStateBgpTable,
       "svcDhcpLeaseStateBgpEntry": svcDhcpLeaseStateBgpEntry,
       "svcDhcpLseStateBgpPrngPlcyName": svcDhcpLseStateBgpPrngPlcyName,
       "svcDhcpLseStateBgpAuthKeyChain": svcDhcpLseStateBgpAuthKeyChain,
       "svcDhcpLseStateBgpMD5AuthKey": svcDhcpLseStateBgpMD5AuthKey,
       "svcDhcpLseStateBgpImportPolicy": svcDhcpLseStateBgpImportPolicy,
       "svcDhcpLseStateBgpExportPolicy": svcDhcpLseStateBgpExportPolicy,
       "svcDhcpLseStateBgpPeerAS": svcDhcpLseStateBgpPeerAS,
       "svcDhcpLseStateBgpPeeringStatus": svcDhcpLseStateBgpPeeringStatus,
       "svcArpHostMRtTable": svcArpHostMRtTable,
       "svcArpHostMRtEntry": svcArpHostMRtEntry,
       "svcArpHostMRtAddrType": svcArpHostMRtAddrType,
       "svcArpHostMRtAddr": svcArpHostMRtAddr,
       "svcArpHostMRtPrefixLen": svcArpHostMRtPrefixLen,
       "svcArpHostMRtStatus": svcArpHostMRtStatus,
       "svcArpHostBgpTable": svcArpHostBgpTable,
       "svcArpHostBgpEntry": svcArpHostBgpEntry,
       "svcArpHostBgpPrngPlcyName": svcArpHostBgpPrngPlcyName,
       "svcArpHostBgpAuthKeyChain": svcArpHostBgpAuthKeyChain,
       "svcArpHostBgpMD5AuthKey": svcArpHostBgpMD5AuthKey,
       "svcArpHostBgpImportPolicy": svcArpHostBgpImportPolicy,
       "svcArpHostBgpExportPolicy": svcArpHostBgpExportPolicy,
       "svcArpHostBgpPeerAS": svcArpHostBgpPeerAS,
       "svcArpHostBgpPeeringStatus": svcArpHostBgpPeeringStatus,
       "svcEpMcEpStatsTable": svcEpMcEpStatsTable,
       "svcEpMcEpStatsEntry": svcEpMcEpStatsEntry,
       "svcEpMcEpStatsPktsRxConfig": svcEpMcEpStatsPktsRxConfig,
       "svcEpMcEpStatsPktsRxState": svcEpMcEpStatsPktsRxState,
       "svcEpMcEpStatsPktsTxConfig": svcEpMcEpStatsPktsTxConfig,
       "svcEpMcEpStatsPktsTxState": svcEpMcEpStatsPktsTxState,
       "svcEpMcEpStatsPktsTxFailed": svcEpMcEpStatsPktsTxFailed,
       "svcPbbSrcBVplsMacAddr": svcPbbSrcBVplsMacAddr,
       "svcMacNameTableLastChanged": svcMacNameTableLastChanged,
       "svcMacNameTable": svcMacNameTable,
       "svcMacNameEntry": svcMacNameEntry,
       "svcMacName": svcMacName,
       "svcMacNameRowStatus": svcMacNameRowStatus,
       "svcMacNameLastChngd": svcMacNameLastChngd,
       "svcMacNameAddr": svcMacNameAddr,
       "svcMacNotificationGroup": svcMacNotificationGroup,
       "svcMacNotifInterval": svcMacNotifInterval,
       "svcMacNotifCount": svcMacNotifCount,
       "tlsProtMacImplTable": tlsProtMacImplTable,
       "tlsProtMacImplEntry": tlsProtMacImplEntry,
       "tlsProtMacImplMacAddr": tlsProtMacImplMacAddr,
       "tlsProtMacImplLocale": tlsProtMacImplLocale,
       "tlsProtMacImplPortId": tlsProtMacImplPortId,
       "tlsProtMacImplEncapValue": tlsProtMacImplEncapValue,
       "tlsProtMacImplSdpBindId": tlsProtMacImplSdpBindId,
       "tlsProtMacImplCount": tlsProtMacImplCount,
       "svcNameTableLastChanged": svcNameTableLastChanged,
       "svcNameTable": svcNameTable,
       "svcNameEntry": svcNameEntry,
       "svcNameId": svcNameId,
       "svcNameRowStatus": svcNameRowStatus,
       "svcNameLastChanged": svcNameLastChanged,
       "svcNameType": svcNameType,
       "svcMrpPlcyTableLastChgd": svcMrpPlcyTableLastChgd,
       "svcMrpPolicyTable": svcMrpPolicyTable,
       "svcMrpPolicyEntry": svcMrpPolicyEntry,
       "svcMrpPolicyName": svcMrpPolicyName,
       "svcMrpPolicyRowStatus": svcMrpPolicyRowStatus,
       "svcMrpPolicyLastChanged": svcMrpPolicyLastChanged,
       "svcMrpPolicyDescription": svcMrpPolicyDescription,
       "svcMrpPolicyScope": svcMrpPolicyScope,
       "svcMrpPolicyDefaultAction": svcMrpPolicyDefaultAction,
       "svcMrpPlcyParamsTblLastChgd": svcMrpPlcyParamsTblLastChgd,
       "svcMrpPolicyParamsTable": svcMrpPolicyParamsTable,
       "svcMrpPolicyParamsEntry": svcMrpPolicyParamsEntry,
       "svcMrpPolicyParamsEntryId": svcMrpPolicyParamsEntryId,
       "svcMrpPolicyParamsRowStatus": svcMrpPolicyParamsRowStatus,
       "svcMrpPolicyParamsLastChanged": svcMrpPolicyParamsLastChanged,
       "svcMrpPolicyParamsDescription": svcMrpPolicyParamsDescription,
       "svcMrpPolicyParamsAction": svcMrpPolicyParamsAction,
       "svcMrpPlcyParamsISIDTblLastChgd": svcMrpPlcyParamsISIDTblLastChgd,
       "svcMrpPolicyParamsISIDTable": svcMrpPolicyParamsISIDTable,
       "svcMrpPolicyParamsISIDEntry": svcMrpPolicyParamsISIDEntry,
       "svcMrpPolicyParamsISIDLow": svcMrpPolicyParamsISIDLow,
       "svcMrpPolicyParamsISIDHigh": svcMrpPolicyParamsISIDHigh,
       "svcMrpPolicyParamsISIDRowStatus": svcMrpPolicyParamsISIDRowStatus,
       "svcMrpPolicyParamsISIDLastChgd": svcMrpPolicyParamsISIDLastChgd,
       "svcEpipeTableLastChanged": svcEpipeTableLastChanged,
       "svcEpipeTable": svcEpipeTable,
       "svcEpipeEntry": svcEpipeEntry,
       "svcEpipeLastChngd": svcEpipeLastChngd,
       "svcEpipePerSvcHashing": svcEpipePerSvcHashing,
       "svcEpipeBackboneTableLastChanged": svcEpipeBackboneTableLastChanged,
       "svcEpipeBackboneTable": svcEpipeBackboneTable,
       "svcEpipeBackboneEntry": svcEpipeBackboneEntry,
       "svcEpipeBackboneLastChngd": svcEpipeBackboneLastChngd,
       "svcEpipeBackboneForceQTagFwd": svcEpipeBackboneForceQTagFwd,
       "svcTlsSiteIdTblLastChanged": svcTlsSiteIdTblLastChanged,
       "svcTlsSiteIdTable": svcTlsSiteIdTable,
       "svcTlsSiteIdEntry": svcTlsSiteIdEntry,
       "svcTlsSiteIdName": svcTlsSiteIdName,
       "svcTlsSiteIdRowStatus": svcTlsSiteIdRowStatus,
       "svcTlsSiteIdLastChanged": svcTlsSiteIdLastChanged,
       "svcTlsSiteIdAdminStatus": svcTlsSiteIdAdminStatus,
       "svcTlsSiteIdSiteId": svcTlsSiteIdSiteId,
       "svcTlsSiteIdPortId": svcTlsSiteIdPortId,
       "svcTlsSiteIdEncapValue": svcTlsSiteIdEncapValue,
       "svcTlsSiteIdSdpBindId": svcTlsSiteIdSdpBindId,
       "svcTlsSiteIdShgName": svcTlsSiteIdShgName,
       "svcTlsSiteIdShgMeshSdp": svcTlsSiteIdShgMeshSdp,
       "svcTlsSiteIdFailedThresh": svcTlsSiteIdFailedThresh,
       "svcTlsSiteIdOperStatus": svcTlsSiteIdOperStatus,
       "svcTlsSiteIdDesignatedFwdr": svcTlsSiteIdDesignatedFwdr,
       "svcTlsSiteIdBootTimer": svcTlsSiteIdBootTimer,
       "svcTlsSiteIdSiteActTimer": svcTlsSiteIdSiteActTimer,
       "svcTlsSiteIdDfUpTime": svcTlsSiteIdDfUpTime,
       "svcTlsSiteIdDfChgCnt": svcTlsSiteIdDfChgCnt,
       "svcTlsSiteIdTimerRemain": svcTlsSiteIdTimerRemain,
       "svcTlsSiteIdMonitorOperGrp": svcTlsSiteIdMonitorOperGrp,
       "svcBgpVplsTblLastChanged": svcBgpVplsTblLastChanged,
       "svcBgpVplsTable": svcBgpVplsTable,
       "svcBgpVplsEntry": svcBgpVplsEntry,
       "svcBgpVplsRowStatus": svcBgpVplsRowStatus,
       "svcBgpVplsLastChanged": svcBgpVplsLastChanged,
       "svcBgpVplsMaxVeId": svcBgpVplsMaxVeId,
       "svcBgpVplsAdminStatus": svcBgpVplsAdminStatus,
       "svcBgpVplsVeName": svcBgpVplsVeName,
       "svcBgpVplsVeId": svcBgpVplsVeId,
       "svcTlsBgpTableLastChanged": svcTlsBgpTableLastChanged,
       "svcTlsBgpTable": svcTlsBgpTable,
       "svcTlsBgpEntry": svcTlsBgpEntry,
       "svcTlsBgpLastChanged": svcTlsBgpLastChanged,
       "svcTlsBgpVsiRD": svcTlsBgpVsiRD,
       "svcTlsBgpExportRteTarget": svcTlsBgpExportRteTarget,
       "svcTlsBgpVsiExportPolicy1": svcTlsBgpVsiExportPolicy1,
       "svcTlsBgpVsiExportPolicy2": svcTlsBgpVsiExportPolicy2,
       "svcTlsBgpVsiExportPolicy3": svcTlsBgpVsiExportPolicy3,
       "svcTlsBgpVsiExportPolicy4": svcTlsBgpVsiExportPolicy4,
       "svcTlsBgpVsiExportPolicy5": svcTlsBgpVsiExportPolicy5,
       "svcTlsBgpImportRteTarget": svcTlsBgpImportRteTarget,
       "svcTlsBgpVsiImportPolicy1": svcTlsBgpVsiImportPolicy1,
       "svcTlsBgpVsiImportPolicy2": svcTlsBgpVsiImportPolicy2,
       "svcTlsBgpVsiImportPolicy3": svcTlsBgpVsiImportPolicy3,
       "svcTlsBgpVsiImportPolicy4": svcTlsBgpVsiImportPolicy4,
       "svcTlsBgpVsiImportPolicy5": svcTlsBgpVsiImportPolicy5,
       "svcTlsBgpRowStatus": svcTlsBgpRowStatus,
       "svcTlsPbbIgmpSnpgMRtrTable": svcTlsPbbIgmpSnpgMRtrTable,
       "svcTlsPbbIgmpSnpgMRtrEntry": svcTlsPbbIgmpSnpgMRtrEntry,
       "svcTlsPbbIgmpSnpgMRtrSvcIdIVpls": svcTlsPbbIgmpSnpgMRtrSvcIdIVpls,
       "svcTlsPbbIgmpSnpgMRtrSvcIdBVpls": svcTlsPbbIgmpSnpgMRtrSvcIdBVpls,
       "svcTlsPbbIgmpSnpgMRtrMacName": svcTlsPbbIgmpSnpgMRtrMacName,
       "svcTlsPbbIgmpSnpgMRtrRowStatus": svcTlsPbbIgmpSnpgMRtrRowStatus,
       "svcTlsPbbIgmpSnpgMRtrLastCh": svcTlsPbbIgmpSnpgMRtrLastCh,
       "svcL2MhRteTable": svcL2MhRteTable,
       "svcL2MhRteEntry": svcL2MhRteEntry,
       "svcL2MhRteSiteId": svcL2MhRteSiteId,
       "svcL2MhRteRouteDistinguisher": svcL2MhRteRouteDistinguisher,
       "svcL2MhRteNextHopType": svcL2MhRteNextHopType,
       "svcL2MhRteNextHop": svcL2MhRteNextHop,
       "svcL2MhRteState": svcL2MhRteState,
       "svcL2MhRteDf": svcL2MhRteDf,
       "svcTmplTblLastChanged": svcTmplTblLastChanged,
       "svcTmplTable": svcTmplTable,
       "svcTmplEntry": svcTmplEntry,
       "svcTmplName": svcTmplName,
       "svcTmplRowStatus": svcTmplRowStatus,
       "svcTmplLastChanged": svcTmplLastChanged,
       "svcTmplSvcCount": svcTmplSvcCount,
       "svcTmplType": svcTmplType,
       "svcTmplMtu": svcTmplMtu,
       "svcTmplCustId": svcTmplCustId,
       "svcTlsGroupTblLastChanged": svcTlsGroupTblLastChanged,
       "svcTlsGroupTable": svcTlsGroupTable,
       "svcTlsGroupEntry": svcTlsGroupEntry,
       "svcTlsGroupId": svcTlsGroupId,
       "svcTlsGroupRowStatus": svcTlsGroupRowStatus,
       "svcTlsGroupLastChanged": svcTlsGroupLastChanged,
       "svcTlsGroupAdminStatus": svcTlsGroupAdminStatus,
       "svcTlsGroupStart": svcTlsGroupStart,
       "svcTlsGroupEnd": svcTlsGroupEnd,
       "svcTlsGroupStartVlanTag": svcTlsGroupStartVlanTag,
       "svcTlsGroupSvcTmplName": svcTlsGroupSvcTmplName,
       "svcTlsGroupSapTmplName": svcTlsGroupSapTmplName,
       "svcTlsGroupMvrpControl": svcTlsGroupMvrpControl,
       "svcTlsGroupOperStatus": svcTlsGroupOperStatus,
       "svcTlsGroupLastError": svcTlsGroupLastError,
       "svcDhcpLeaseTable": svcDhcpLeaseTable,
       "svcDhcpLeaseEntry": svcDhcpLeaseEntry,
       "svcDhcpLeaseCiAddrType": svcDhcpLeaseCiAddrType,
       "svcDhcpLeaseCiAddr": svcDhcpLeaseCiAddr,
       "svcDhcpLeaseNextHopMacAddr": svcDhcpLeaseNextHopMacAddr,
       "svcDhcpLeaseChAddr": svcDhcpLeaseChAddr,
       "svcDhcpLeaseLocale": svcDhcpLeaseLocale,
       "svcDhcpLeasePortId": svcDhcpLeasePortId,
       "svcDhcpLeaseEncapValue": svcDhcpLeaseEncapValue,
       "svcDhcpLeaseSdpId": svcDhcpLeaseSdpId,
       "svcDhcpLeaseVcId": svcDhcpLeaseVcId,
       "svcDhcpLeaseRemainLseTime": svcDhcpLeaseRemainLseTime,
       "svcDhcpLeaseOption82": svcDhcpLeaseOption82,
       "svcDhcpLeasePersistKey": svcDhcpLeasePersistKey,
       "svcDhcpLeaseSubscrIdent": svcDhcpLeaseSubscrIdent,
       "svcDhcpLeaseSubProfString": svcDhcpLeaseSubProfString,
       "svcDhcpLeaseSlaProfString": svcDhcpLeaseSlaProfString,
       "svcDhcpLeaseShcvOperState": svcDhcpLeaseShcvOperState,
       "svcDhcpLeaseShcvChecks": svcDhcpLeaseShcvChecks,
       "svcDhcpLeaseShcvReplies": svcDhcpLeaseShcvReplies,
       "svcDhcpLeaseShcvReplyTime": svcDhcpLeaseShcvReplyTime,
       "svcDhcpLeaseClientId": svcDhcpLeaseClientId,
       "svcDhcpLeaseIAID": svcDhcpLeaseIAID,
       "svcDhcpLeaseIAIDType": svcDhcpLeaseIAIDType,
       "svcDhcpLeaseCiAddrMaskLen": svcDhcpLeaseCiAddrMaskLen,
       "svcDhcpLeaseRetailerSvcId": svcDhcpLeaseRetailerSvcId,
       "svcDhcpLeaseRetailerIf": svcDhcpLeaseRetailerIf,
       "svcDhcpLeaseAncpString": svcDhcpLeaseAncpString,
       "svcDhcpLeaseFramedIpNetMaskTp": svcDhcpLeaseFramedIpNetMaskTp,
       "svcDhcpLeaseFramedIpNetMask": svcDhcpLeaseFramedIpNetMask,
       "svcDhcpLeaseBCastIpAddrType": svcDhcpLeaseBCastIpAddrType,
       "svcDhcpLeaseBCastIpAddr": svcDhcpLeaseBCastIpAddr,
       "svcDhcpLeaseDefaultRouterTp": svcDhcpLeaseDefaultRouterTp,
       "svcDhcpLeaseDefaultRouter": svcDhcpLeaseDefaultRouter,
       "svcDhcpLeasePrimaryDnsType": svcDhcpLeasePrimaryDnsType,
       "svcDhcpLeasePrimaryDns": svcDhcpLeasePrimaryDns,
       "svcDhcpLeaseSecondaryDnsType": svcDhcpLeaseSecondaryDnsType,
       "svcDhcpLeaseSecondaryDns": svcDhcpLeaseSecondaryDns,
       "svcDhcpLeaseSessionTimeout": svcDhcpLeaseSessionTimeout,
       "svcDhcpLeaseServerLeaseStart": svcDhcpLeaseServerLeaseStart,
       "svcDhcpLeaseServerLastRenew": svcDhcpLeaseServerLastRenew,
       "svcDhcpLeaseServerLeaseEnd": svcDhcpLeaseServerLeaseEnd,
       "svcDhcpLeaseDhcpServerAddrType": svcDhcpLeaseDhcpServerAddrType,
       "svcDhcpLeaseDhcpServerAddr": svcDhcpLeaseDhcpServerAddr,
       "svcDhcpLeaseOriginSubscrId": svcDhcpLeaseOriginSubscrId,
       "svcDhcpLeaseOriginStrings": svcDhcpLeaseOriginStrings,
       "svcDhcpLeaseOriginLeaseInfo": svcDhcpLeaseOriginLeaseInfo,
       "svcDhcpLeaseDhcpClientAddrType": svcDhcpLeaseDhcpClientAddrType,
       "svcDhcpLeaseDhcpClientAddr": svcDhcpLeaseDhcpClientAddr,
       "svcDhcpLeaseLeaseSplitActive": svcDhcpLeaseLeaseSplitActive,
       "svcDhcpLeaseInterDestId": svcDhcpLeaseInterDestId,
       "svcDhcpLeasePrimaryNbnsType": svcDhcpLeasePrimaryNbnsType,
       "svcDhcpLeasePrimaryNbns": svcDhcpLeasePrimaryNbns,
       "svcDhcpLeaseSecondaryNbnsType": svcDhcpLeaseSecondaryNbnsType,
       "svcDhcpLeaseSecondaryNbns": svcDhcpLeaseSecondaryNbns,
       "svcDhcpLeaseAppProfString": svcDhcpLeaseAppProfString,
       "svcDhcpLeaseCategoryMapName": svcDhcpLeaseCategoryMapName,
       "svcDhcpLeaseNakNextRenew": svcDhcpLeaseNakNextRenew,
       "svcDhcpLeaseRadiusClassAttr": svcDhcpLeaseRadiusClassAttr,
       "svcDhcpLeaseRadiusUserName": svcDhcpLeaseRadiusUserName,
       "svcDhcpLeasePoolName": svcDhcpLeasePoolName,
       "svcDhcpLeaseServerId": svcDhcpLeaseServerId,
       "svcDhcpLeaseInterfaceId": svcDhcpLeaseInterfaceId,
       "svcDhcpLeaseRemoteId": svcDhcpLeaseRemoteId,
       "svcDhcpLeaseOption60": svcDhcpLeaseOption60,
       "svcDhcpLeaseRadCalledStationId": svcDhcpLeaseRadCalledStationId,
       "svcDhcpLeaseModifyTable": svcDhcpLeaseModifyTable,
       "svcDhcpLeaseModifyEntry": svcDhcpLeaseModifyEntry,
       "svcDhcpLeaseModifySubIndent": svcDhcpLeaseModifySubIndent,
       "svcDhcpLeaseModifySubProfile": svcDhcpLeaseModifySubProfile,
       "svcDhcpLeaseModifySlaProfile": svcDhcpLeaseModifySlaProfile,
       "svcDhcpLeaseEvaluateState": svcDhcpLeaseEvaluateState,
       "svcDhcpLeaseModInterDestId": svcDhcpLeaseModInterDestId,
       "svcDhcpLeaseModifyAncpString": svcDhcpLeaseModifyAncpString,
       "svcDhcpLeaseModifyAppProfile": svcDhcpLeaseModifyAppProfile,
       "svcDhcpLeaseActionTable": svcDhcpLeaseActionTable,
       "svcDhcpLeaseActionEntry": svcDhcpLeaseActionEntry,
       "svcDhcpLeaseForceRenew": svcDhcpLeaseForceRenew,
       "svcDhcpLeaseBgpTable": svcDhcpLeaseBgpTable,
       "svcDhcpLeaseBgpEntry": svcDhcpLeaseBgpEntry,
       "svcDhcpLeaseBgpPrngPlcyName": svcDhcpLeaseBgpPrngPlcyName,
       "svcDhcpLeaseBgpAuthKeyChain": svcDhcpLeaseBgpAuthKeyChain,
       "svcDhcpLeaseBgpMD5AuthKey": svcDhcpLeaseBgpMD5AuthKey,
       "svcDhcpLeaseBgpImportPolicy": svcDhcpLeaseBgpImportPolicy,
       "svcDhcpLeaseBgpExportPolicy": svcDhcpLeaseBgpExportPolicy,
       "svcDhcpLeaseBgpPeerAS": svcDhcpLeaseBgpPeerAS,
       "svcDhcpLeaseBgpPeeringStatus": svcDhcpLeaseBgpPeeringStatus,
       "svcTmplTlsTblLastChanged": svcTmplTlsTblLastChanged,
       "svcTmplTlsTable": svcTmplTlsTable,
       "svcTmplTlsEntry": svcTmplTlsEntry,
       "svcTmplTlsLastChanged": svcTmplTlsLastChanged,
       "svcTmplTlsMacLearning": svcTmplTlsMacLearning,
       "svcTmplTlsDiscardUnknownDest": svcTmplTlsDiscardUnknownDest,
       "svcTmplTlsFdbTableSize": svcTmplTlsFdbTableSize,
       "svcTmplTlsFdbLocalAgeTime": svcTmplTlsFdbLocalAgeTime,
       "svcTmplTlsFdbRemoteAgeTime": svcTmplTlsFdbRemoteAgeTime,
       "svcTmplTlsStpAdminStatus": svcTmplTlsStpAdminStatus,
       "svcTmplTlsStpPriority": svcTmplTlsStpPriority,
       "svcTmplTlsStpBridgeMaxAge": svcTmplTlsStpBridgeMaxAge,
       "svcTmplTlsStpBridgeHelloTime": svcTmplTlsStpBridgeHelloTime,
       "svcTmplTlsStpBridgeForwardDelay": svcTmplTlsStpBridgeForwardDelay,
       "svcTmplTlsMacAgeing": svcTmplTlsMacAgeing,
       "svcTmplTlsFdbTableFullHighWMark": svcTmplTlsFdbTableFullHighWMark,
       "svcTmplTlsFdbTableFullLowWMark": svcTmplTlsFdbTableFullLowWMark,
       "svcTmplTlsStpVersion": svcTmplTlsStpVersion,
       "svcTmplTlsStpHoldCount": svcTmplTlsStpHoldCount,
       "svcTmplTlsPerSvcHashing": svcTmplTlsPerSvcHashing,
       "svcTmplTlsTempFloodTime": svcTmplTlsTempFloodTime,
       "svcTmplTlsMacMoveMaxRate": svcTmplTlsMacMoveMaxRate,
       "svcTmplTlsMacMoveRetryTimeout": svcTmplTlsMacMoveRetryTimeout,
       "svcTmplTlsMacMoveAdminStatus": svcTmplTlsMacMoveAdminStatus,
       "svcTmplTlsPriPortsCumFactor": svcTmplTlsPriPortsCumFactor,
       "svcTmplTlsSecPortsCumFactor": svcTmplTlsSecPortsCumFactor,
       "svcTmplTlsMacMoveNumRetries": svcTmplTlsMacMoveNumRetries,
       "svcTmplUserTable": svcTmplUserTable,
       "svcTmplUserEntry": svcTmplUserEntry,
       "svcTmplUserCreationOrigin": svcTmplUserCreationOrigin,
       "svcTmplUserCreatorSvcId": svcTmplUserCreatorSvcId,
       "svcTlsExtTable": svcTlsExtTable,
       "svcTlsExtEntry": svcTlsExtEntry,
       "svcTlsExtMvrpMaxAttributes": svcTlsExtMvrpMaxAttributes,
       "svcTlsExtMvrpRegAttrCnt": svcTlsExtMvrpRegAttrCnt,
       "svcTlsExtMvrpDeclaredAttrCnt": svcTlsExtMvrpDeclaredAttrCnt,
       "svcTlsExtMvrpFailedRegCnt": svcTlsExtMvrpFailedRegCnt,
       "svcTlsExtMvrpAttrTblHighWM": svcTlsExtMvrpAttrTblHighWM,
       "svcTlsExtMvrpAttrTblLowWM": svcTlsExtMvrpAttrTblLowWM,
       "svcTlsExtMvrpHoldTime": svcTlsExtMvrpHoldTime,
       "svcTlsExtMvrpAdminStatus": svcTlsExtMvrpAdminStatus,
       "svcTlsExtMvrpOperStatus": svcTlsExtMvrpOperStatus,
       "svcTlsExtMmrpAdminStatus": svcTlsExtMmrpAdminStatus,
       "svcTlsExtMmrpOperStatus": svcTlsExtMmrpOperStatus,
       "svcTlsExtMmrpRegAttrCnt": svcTlsExtMmrpRegAttrCnt,
       "svcTlsExtMmrpDeclaredAttrCnt": svcTlsExtMmrpDeclaredAttrCnt,
       "svcTlsExtMmrpFailedRegCnt": svcTlsExtMmrpFailedRegCnt,
       "svcTlsExtMvrpAttributeCount": svcTlsExtMvrpAttributeCount,
       "svcTlsExtMmrpEndStationOnly": svcTlsExtMmrpEndStationOnly,
       "svcTlsExtMacReNotifInterval": svcTlsExtMacReNotifInterval,
       "svcTlsExtSpbmCtrlVpls": svcTlsExtSpbmCtrlVpls,
       "svcTlsExtSpbmFid": svcTlsExtSpbmFid,
       "svcPwRtLclPrefixTblLastChanged": svcPwRtLclPrefixTblLastChanged,
       "svcPwRtLclPrefixTable": svcPwRtLclPrefixTable,
       "svcPwRtLclPrefixEntry": svcPwRtLclPrefixEntry,
       "svcPwRtLclPrefixGlobalId": svcPwRtLclPrefixGlobalId,
       "svcPwRtLclPrefix": svcPwRtLclPrefix,
       "svcPwRtLclPrefixRowStatus": svcPwRtLclPrefixRowStatus,
       "svcPwRtLclPrefixLastChange": svcPwRtLclPrefixLastChange,
       "svcPwRtPathTblLastChanged": svcPwRtPathTblLastChanged,
       "svcPwRtPathTable": svcPwRtPathTable,
       "svcPwRtPathEntry": svcPwRtPathEntry,
       "svcPwRtPathName": svcPwRtPathName,
       "svcPwRtPathRowStatus": svcPwRtPathRowStatus,
       "svcPwRtPathLastChange": svcPwRtPathLastChange,
       "svcPwRtPathAdminStatus": svcPwRtPathAdminStatus,
       "svcPwRtPathHopTblLastChgd": svcPwRtPathHopTblLastChgd,
       "svcPwRtPathHopTable": svcPwRtPathHopTable,
       "svcPwRtPathHopEntry": svcPwRtPathHopEntry,
       "svcPwRtPathHopIndex": svcPwRtPathHopIndex,
       "svcPwRtPathHopRowStatus": svcPwRtPathHopRowStatus,
       "svcPwRtPathHopLastChange": svcPwRtPathHopLastChange,
       "svcPwRtPathHopAddrType": svcPwRtPathHopAddrType,
       "svcPwRtPathHopAddr": svcPwRtPathHopAddr,
       "svcPwRtStaticRtTblLastChgd": svcPwRtStaticRtTblLastChgd,
       "svcPwRtStaticRtTable": svcPwRtStaticRtTable,
       "svcPwRtStaticRtEntry": svcPwRtStaticRtEntry,
       "svcPwRtStaticRtDstGlobalId": svcPwRtStaticRtDstGlobalId,
       "svcPwRtStaticRtDstPrefix": svcPwRtStaticRtDstPrefix,
       "svcPwRtStaticRtDstAddrType": svcPwRtStaticRtDstAddrType,
       "svcPwRtStaticRtDstAddr": svcPwRtStaticRtDstAddr,
       "svcPwRtStaticRtRowStatus": svcPwRtStaticRtRowStatus,
       "svcPwRtStaticRtLastChange": svcPwRtStaticRtLastChange,
       "svcMSPwPeTblLastChanged": svcMSPwPeTblLastChanged,
       "svcMSPwPeTable": svcMSPwPeTable,
       "svcMSPwPeEntry": svcMSPwPeEntry,
       "svcMSPwPeId": svcMSPwPeId,
       "svcMSPwPeRowStatus": svcMSPwPeRowStatus,
       "svcMSPwPeLastChange": svcMSPwPeLastChange,
       "svcMSPwPeAdminStatus": svcMSPwPeAdminStatus,
       "svcMSPwPeFecType": svcMSPwPeFecType,
       "svcMSPwPeAiiType": svcMSPwPeAiiType,
       "svcMSPwPeSignaling": svcMSPwPeSignaling,
       "svcMSPwPeAutoConfig": svcMSPwPeAutoConfig,
       "svcMSPwPeAgi": svcMSPwPeAgi,
       "svcMSPwPePolicyId": svcMSPwPePolicyId,
       "svcMSPwPePrecedence": svcMSPwPePrecedence,
       "svcMSPwPeRetryTimer": svcMSPwPeRetryTimer,
       "svcMSPwPeRetryCount": svcMSPwPeRetryCount,
       "svcMSPwPeSaiiGlobalId": svcMSPwPeSaiiGlobalId,
       "svcMSPwPeSaiiPrefix": svcMSPwPeSaiiPrefix,
       "svcMSPwPeSaiiAcId": svcMSPwPeSaiiAcId,
       "svcMSPwPeTaiiGlobalId": svcMSPwPeTaiiGlobalId,
       "svcMSPwPeTaiiPrefix": svcMSPwPeTaiiPrefix,
       "svcMSPwPeTaiiAcId": svcMSPwPeTaiiAcId,
       "svcMSPwPePathName": svcMSPwPePathName,
       "svcMSPwPeEndPoint": svcMSPwPeEndPoint,
       "svcMSPwPeStandbySigSlave": svcMSPwPeStandbySigSlave,
       "svcMSPwPeIsICB": svcMSPwPeIsICB,
       "svcMSPwPeTimeRemain": svcMSPwPeTimeRemain,
       "svcMSPwPeRetryRemain": svcMSPwPeRetryRemain,
       "svcMSPwPeOperSdpBind": svcMSPwPeOperSdpBind,
       "svcMSPwPeRetryExpired": svcMSPwPeRetryExpired,
       "svcMSPwPeLastError": svcMSPwPeLastError,
       "svcOperGrpTblLastChanged": svcOperGrpTblLastChanged,
       "svcOperGrpTable": svcOperGrpTable,
       "svcOperGrpEntry": svcOperGrpEntry,
       "svcOperGrpName": svcOperGrpName,
       "svcOperGrpRowStatus": svcOperGrpRowStatus,
       "svcOperGrpLastChange": svcOperGrpLastChange,
       "svcOperGrpOperStatus": svcOperGrpOperStatus,
       "svcOperGrpHoldDownTime": svcOperGrpHoldDownTime,
       "svcOperGrpCreationOrigin": svcOperGrpCreationOrigin,
       "svcOperGrpHoldUpTime": svcOperGrpHoldUpTime,
       "svcOperGrpHoldUpTimeRemain": svcOperGrpHoldUpTimeRemain,
       "svcOperGrpHoldDownTimeRemain": svcOperGrpHoldDownTimeRemain,
       "svcOperGrpNumMembers": svcOperGrpNumMembers,
       "svcOperGrpNumMonitoring": svcOperGrpNumMonitoring,
       "svcDhcpLeaseAleTable": svcDhcpLeaseAleTable,
       "svcDhcpLeaseAleEntry": svcDhcpLeaseAleEntry,
       "svcDhcpLeaseAleDatalink": svcDhcpLeaseAleDatalink,
       "svcDhcpLeaseAleEncaps1": svcDhcpLeaseAleEncaps1,
       "svcDhcpLeaseAleEncaps2": svcDhcpLeaseAleEncaps2,
       "svcEthCfmTblLastChanged": svcEthCfmTblLastChanged,
       "svcEthCfmTable": svcEthCfmTable,
       "svcEthCfmEntry": svcEthCfmEntry,
       "svcEthCfmTunnelFaultNotification": svcEthCfmTunnelFaultNotification,
       "svcEthCfmVMepExtensions": svcEthCfmVMepExtensions,
       "tmnxSvcGrpObjs": tmnxSvcGrpObjs,
       "svcMacFdbRecords": svcMacFdbRecords,
       "svcPwRtSpeAddrGlobalId": svcPwRtSpeAddrGlobalId,
       "svcPwRtSpeAddrPrefix": svcPwRtSpeAddrPrefix,
       "svcPwRtBootTimer": svcPwRtBootTimer,
       "svcPwRtRetryTimer": svcPwRtRetryTimer,
       "svcPwRtRetryCount": svcPwRtRetryCount,
       "svcPwRtBgpRoutes": svcPwRtBgpRoutes,
       "svcPwRtStaticRoutes": svcPwRtStaticRoutes,
       "svcPwRtLocalRoutes": svcPwRtLocalRoutes,
       "svcPwRtHostRoutes": svcPwRtHostRoutes,
       "svcPwRtBootTimerRemain": svcPwRtBootTimerRemain,
       "svcPwRtLclPfxRDTblLastChanged": svcPwRtLclPfxRDTblLastChanged,
       "svcPwRtLclPfxRDTable": svcPwRtLclPfxRDTable,
       "svcPwRtLclPfxRDEntry": svcPwRtLclPfxRDEntry,
       "svcPwRtLclPfxRD": svcPwRtLclPfxRD,
       "svcPwRtLclPfxRDRowStatus": svcPwRtLclPfxRDRowStatus,
       "svcPwRtLclPfxRDLastChange": svcPwRtLclPfxRDLastChange,
       "svcPwRtLclPfxRDCommunity": svcPwRtLclPfxRDCommunity,
       "svcPwSpeSaiiTable": svcPwSpeSaiiTable,
       "svcPwSpeSaiiEntry": svcPwSpeSaiiEntry,
       "svcPwSpeSaiiTaiiGlobalId": svcPwSpeSaiiTaiiGlobalId,
       "svcPwSpeSaiiTaiiPrefix": svcPwSpeSaiiTaiiPrefix,
       "svcPwSpeSaiiTaiiAcId": svcPwSpeSaiiTaiiAcId,
       "svcPwSpeSaiiSvcId": svcPwSpeSaiiSvcId,
       "svcPwSpeSaiiOperSdpBind1": svcPwSpeSaiiOperSdpBind1,
       "svcPwSpeSaiiOperSdpBind2": svcPwSpeSaiiOperSdpBind2,
       "svcPwSpeTaiiTable": svcPwSpeTaiiTable,
       "svcPwSpeTaiiEntry": svcPwSpeTaiiEntry,
       "svcPwSpeTaiiSaiiGlobalId": svcPwSpeTaiiSaiiGlobalId,
       "svcPwSpeTaiiSaiiPrefix": svcPwSpeTaiiSaiiPrefix,
       "svcPwSpeTaiiSaiiAcId": svcPwSpeTaiiSaiiAcId,
       "svcPwSpeTaiiSvcId": svcPwSpeTaiiSvcId,
       "svcPwSpeTaiiOperSdpBind1": svcPwSpeTaiiOperSdpBind1,
       "svcPwSpeTaiiOperSdpBind2": svcPwSpeTaiiOperSdpBind2,
       "svcDhcpLeaseOvrTable": svcDhcpLeaseOvrTable,
       "svcDhcpLeaseOvrEntry": svcDhcpLeaseOvrEntry,
       "svcDhcpLeaseOvrDirection": svcDhcpLeaseOvrDirection,
       "svcDhcpLeaseOvrType": svcDhcpLeaseOvrType,
       "svcDhcpLeaseOvrTypeId": svcDhcpLeaseOvrTypeId,
       "svcDhcpLeaseOvrTypeName": svcDhcpLeaseOvrTypeName,
       "svcDhcpLeaseOvrPIR": svcDhcpLeaseOvrPIR,
       "svcDhcpLeaseOvrCIR": svcDhcpLeaseOvrCIR,
       "svcDhcpLeaseOvrCBS": svcDhcpLeaseOvrCBS,
       "svcDhcpLeaseOvrMBS": svcDhcpLeaseOvrMBS,
       "svcDhcpLeaseOvrWrrWeight": svcDhcpLeaseOvrWrrWeight,
       "svcTlsSpbTableLastChanged": svcTlsSpbTableLastChanged,
       "svcTlsSpbTable": svcTlsSpbTable,
       "svcTlsSpbEntry": svcTlsSpbEntry,
       "svcTlsSpbRowStatus": svcTlsSpbRowStatus,
       "svcTlsSpbLastChanged": svcTlsSpbLastChanged,
       "svcTlsSpbIsisInstance": svcTlsSpbIsisInstance,
       "svcTlsSpbFid": svcTlsSpbFid,
       "svcTlsSpbL1BridgePriority": svcTlsSpbL1BridgePriority,
       "svcTlsSpbL1FwdTreeTopoUcast": svcTlsSpbL1FwdTreeTopoUcast,
       "svcTlsSpbAdminState": svcTlsSpbAdminState,
       "svcTlsSpbL1FwdTreeTopoMcast": svcTlsSpbL1FwdTreeTopoMcast,
       "svcTlsSpbL1BridgeId": svcTlsSpbL1BridgeId,
       "svcTlsSpbL1McastDesigBridgeId": svcTlsSpbL1McastDesigBridgeId,
       "svcVllBgpTableLastChanged": svcVllBgpTableLastChanged,
       "svcVllBgpTable": svcVllBgpTable,
       "svcVllBgpEntry": svcVllBgpEntry,
       "svcVllBgpRowStatus": svcVllBgpRowStatus,
       "svcVllBgpLastChanged": svcVllBgpLastChanged,
       "svcVllBgpVsiRD": svcVllBgpVsiRD,
       "svcVllBgpExportRteTarget": svcVllBgpExportRteTarget,
       "svcVllBgpImportRteTarget": svcVllBgpImportRteTarget,
       "svcVllSiteIdTblLastChanged": svcVllSiteIdTblLastChanged,
       "svcVllSiteIdTable": svcVllSiteIdTable,
       "svcVllSiteIdEntry": svcVllSiteIdEntry,
       "svcVllSiteIdName": svcVllSiteIdName,
       "svcVllSiteIdRowStatus": svcVllSiteIdRowStatus,
       "svcVllSiteIdLastChanged": svcVllSiteIdLastChanged,
       "svcVllSiteIdAdminStatus": svcVllSiteIdAdminStatus,
       "svcVllSiteIdSiteId": svcVllSiteIdSiteId,
       "svcVllSiteIdPortId": svcVllSiteIdPortId,
       "svcVllSiteIdEncapValue": svcVllSiteIdEncapValue,
       "svcVllSiteIdOperStatus": svcVllSiteIdOperStatus,
       "svcVllSiteIdDesignatedFwdr": svcVllSiteIdDesignatedFwdr,
       "svcVllSiteIdBootTimer": svcVllSiteIdBootTimer,
       "svcVllSiteIdSiteActTimer": svcVllSiteIdSiteActTimer,
       "svcVllSiteIdDfUpTime": svcVllSiteIdDfUpTime,
       "svcVllSiteIdDfChgCnt": svcVllSiteIdDfChgCnt,
       "svcVllSiteIdTimerRemain": svcVllSiteIdTimerRemain,
       "svcTlsPmsiTableLastChanged": svcTlsPmsiTableLastChanged,
       "svcTlsPmsiTable": svcTlsPmsiTable,
       "svcTlsPmsiEntry": svcTlsPmsiEntry,
       "svcTlsPmsiRowStatus": svcTlsPmsiRowStatus,
       "svcTlsPmsiLastChanged": svcTlsPmsiLastChanged,
       "svcTlsIPmsiAdminState": svcTlsIPmsiAdminState,
       "svcTlsIPmsiDataDelayIntvl": svcTlsIPmsiDataDelayIntvl,
       "svcTlsIPmsiType": svcTlsIPmsiType,
       "svcTlsIPmsiLspTmpl": svcTlsIPmsiLspTmpl,
       "svcTlsIPmsiRootAndLeaf": svcTlsIPmsiRootAndLeaf,
       "svcTlsIPmsiRemainDataDelayIntvl": svcTlsIPmsiRemainDataDelayIntvl,
       "svcTlsIPmsiLspName": svcTlsIPmsiLspName,
       "svcDhcpLeaseWppTable": svcDhcpLeaseWppTable,
       "svcDhcpLeaseWppEntry": svcDhcpLeaseWppEntry,
       "svcDhcpLeaseWppState": svcDhcpLeaseWppState,
       "svcDhcpLeaseWppPortalRouter": svcDhcpLeaseWppPortalRouter,
       "svcDhcpLeaseWppPortalName": svcDhcpLeaseWppPortalName,
       "svcIfSapCfgTableLastChanged": svcIfSapCfgTableLastChanged,
       "svcIfSapCfgTable": svcIfSapCfgTable,
       "svcIfSapCfgEntry": svcIfSapCfgEntry,
       "svcIfSapCfgLastMgmtChange": svcIfSapCfgLastMgmtChange,
       "svcIfSapCfgDescription": svcIfSapCfgDescription,
       "svcIfSapCfgDefSubProfile": svcIfSapCfgDefSubProfile,
       "svcIfSapCfgDefSlaProfile": svcIfSapCfgDefSlaProfile,
       "svcIfSapCfgDefAppProfile": svcIfSapCfgDefAppProfile,
       "svcIfSapCfgSubIdentPolicy": svcIfSapCfgSubIdentPolicy,
       "svcIfSapCfgDefSubIdent": svcIfSapCfgDefSubIdent,
       "svcIfSapCfgDefSubIdentString": svcIfSapCfgDefSubIdentString,
       "svcIfSapCfgDefFilterProfile": svcIfSapCfgDefFilterProfile,
       "svcTlsSpbUserSvcTable": svcTlsSpbUserSvcTable,
       "svcTlsSpbUserSvcEntry": svcTlsSpbUserSvcEntry,
       "svcTlsSpbUserSvcId": svcTlsSpbUserSvcId,
       "svcTlsSpbUserSvcLastUpdate": svcTlsSpbUserSvcLastUpdate,
       "tlsSpbFdbTable": tlsSpbFdbTable,
       "tlsSpbFdbEntry": tlsSpbFdbEntry,
       "tlsSpbFdbMacAddr": tlsSpbFdbMacAddr,
       "tlsSpbFdbLocale": tlsSpbFdbLocale,
       "tlsSpbFdbPortId": tlsSpbFdbPortId,
       "tlsSpbFdbEncapValue": tlsSpbFdbEncapValue,
       "tlsSpbFdbSdpId": tlsSpbFdbSdpId,
       "tlsSpbFdbVcId": tlsSpbFdbVcId,
       "tlsSpbFdbState": tlsSpbFdbState,
       "tlsSpbFdbMLocale": tlsSpbFdbMLocale,
       "tlsSpbFdbMPortId": tlsSpbFdbMPortId,
       "tlsSpbFdbMEncapValue": tlsSpbFdbMEncapValue,
       "tlsSpbFdbMSdpId": tlsSpbFdbMSdpId,
       "tlsSpbFdbMVcId": tlsSpbFdbMVcId,
       "tlsSpbFdbMState": tlsSpbFdbMState,
       "tlsSpbFidFdbTable": tlsSpbFidFdbTable,
       "tlsSpbFidFdbEntry": tlsSpbFidFdbEntry,
       "tlsSpbFidFdbMacAddr": tlsSpbFidFdbMacAddr,
       "tlsSpbFidFdbLocale": tlsSpbFidFdbLocale,
       "tlsSpbFidFdbPortId": tlsSpbFidFdbPortId,
       "tlsSpbFidFdbEncapValue": tlsSpbFidFdbEncapValue,
       "tlsSpbFidFdbSdpId": tlsSpbFidFdbSdpId,
       "tlsSpbFidFdbVcId": tlsSpbFidFdbVcId,
       "tlsSpbFidFdbMLocale": tlsSpbFidFdbMLocale,
       "tlsSpbFidFdbMPortId": tlsSpbFidFdbMPortId,
       "tlsSpbFidFdbMEncapValue": tlsSpbFidFdbMEncapValue,
       "tlsSpbFidFdbMSdpId": tlsSpbFidFdbMSdpId,
       "tlsSpbFidFdbMVcId": tlsSpbFidFdbMVcId,
       "tlsSpbFidFdbLastUpdate": tlsSpbFidFdbLastUpdate,
       "tlsSpbFidFdbMLastUpdate": tlsSpbFidFdbMLastUpdate,
       "tlsSpbMFibTable": tlsSpbMFibTable,
       "tlsSpbMFibEntry": tlsSpbMFibEntry,
       "tlsSpbMFibMacAddr": tlsSpbMFibMacAddr,
       "tlsSpbMFibIsid": tlsSpbMFibIsid,
       "tlsSpbMFibState": tlsSpbMFibState,
       "tlsSpbFidMFibTable": tlsSpbFidMFibTable,
       "tlsSpbFidMFibEntry": tlsSpbFidMFibEntry,
       "tlsSpbFidMFibMacAddr": tlsSpbFidMFibMacAddr,
       "tlsSpbFidMFibLocale": tlsSpbFidMFibLocale,
       "tlsSpbFidMFibPortId": tlsSpbFidMFibPortId,
       "tlsSpbFidMFibEncapValue": tlsSpbFidMFibEncapValue,
       "tlsSpbFidMFibSdpId": tlsSpbFidMFibSdpId,
       "tlsSpbFidMFibVcId": tlsSpbFidMFibVcId,
       "tlsSpbFidMFibIsid": tlsSpbFidMFibIsid,
       "tlsSpbFidMFibLastUpdate": tlsSpbFidMFibLastUpdate,
       "svcSpbIfTable": svcSpbIfTable,
       "svcSpbIfEntry": svcSpbIfEntry,
       "svcSpbIfIndex": svcSpbIfIndex,
       "svcSpbIfLocale": svcSpbIfLocale,
       "svcSpbIfPortId": svcSpbIfPortId,
       "svcSpbIfEncapValue": svcSpbIfEncapValue,
       "svcSpbIfSdpId": svcSpbIfSdpId,
       "svcSpbIfVcId": svcSpbIfVcId,
       "svcSpbIfSvcId": svcSpbIfSvcId,
       "svcSpbIfIsisInstance": svcSpbIfIsisInstance,
       "svcArpHostOvrTable": svcArpHostOvrTable,
       "svcArpHostOvrEntry": svcArpHostOvrEntry,
       "svcArpHostOvrDirection": svcArpHostOvrDirection,
       "svcArpHostOvrType": svcArpHostOvrType,
       "svcArpHostOvrTypeId": svcArpHostOvrTypeId,
       "svcArpHostOvrTypeName": svcArpHostOvrTypeName,
       "svcArpHostOvrPIR": svcArpHostOvrPIR,
       "svcArpHostOvrCIR": svcArpHostOvrCIR,
       "svcArpHostOvrCBS": svcArpHostOvrCBS,
       "svcArpHostOvrMBS": svcArpHostOvrMBS,
       "svcArpHostOvrWrrWeight": svcArpHostOvrWrrWeight,
       "iesIfIsaTnlNHTableLastChanged": iesIfIsaTnlNHTableLastChanged,
       "iesIfIsaTnlNHTable": iesIfIsaTnlNHTable,
       "iesIfIsaTnlNHEntry": iesIfIsaTnlNHEntry,
       "iesIfIsaTnlNHLastChanged": iesIfIsaTnlNHLastChanged,
       "iesIfIsaTnlNHStaticAddrType": iesIfIsaTnlNHStaticAddrType,
       "iesIfIsaTnlNHStaticAddr": iesIfIsaTnlNHStaticAddr,
       "iesIfIsaTnlNHDynAddrType": iesIfIsaTnlNHDynAddrType,
       "iesIfIsaTnlNHDynAddr": iesIfIsaTnlNHDynAddr,
       "tmnxTstpNotifyObjs": tmnxTstpNotifyObjs,
       "tmnxCustomerBridgeId": tmnxCustomerBridgeId,
       "tmnxCustomerRootBridgeId": tmnxCustomerRootBridgeId,
       "tmnxOtherBridgeId": tmnxOtherBridgeId,
       "tmnxOldSdpBindTlsStpPortState": tmnxOldSdpBindTlsStpPortState,
       "tmnxVcpState": tmnxVcpState,
       "tmnxSvcNotifyObjs": tmnxSvcNotifyObjs,
       "macPinningMacAddress": macPinningMacAddress,
       "macPinningPinnedRow": macPinningPinnedRow,
       "macPinningPinnedRowDescr": macPinningPinnedRowDescr,
       "macPinningViolatingRow": macPinningViolatingRow,
       "macPinningViolatingRowDescr": macPinningViolatingRowDescr,
       "tlsDHCPClientLease": tlsDHCPClientLease,
       "tlsDhcpLseStateOldCiAddr": tlsDhcpLseStateOldCiAddr,
       "tlsDhcpLseStateOldChAddr": tlsDhcpLseStateOldChAddr,
       "tlsDhcpLseStateNewCiAddr": tlsDhcpLseStateNewCiAddr,
       "tlsDhcpLseStateNewChAddr": tlsDhcpLseStateNewChAddr,
       "tlsDhcpRestoreLseStateCiAddr": tlsDhcpRestoreLseStateCiAddr,
       "tlsDhcpRestoreLseStateSvcId": tlsDhcpRestoreLseStateSvcId,
       "tlsDhcpRestoreLseStatePortId": tlsDhcpRestoreLseStatePortId,
       "tlsDhcpRestoreLseStateEncapVal": tlsDhcpRestoreLseStateEncapVal,
       "tlsDhcpRestoreLseStateProblem": tlsDhcpRestoreLseStateProblem,
       "tlsDhcpPacketProblem": tlsDhcpPacketProblem,
       "tlsDhcpLseStatePopulateError": tlsDhcpLseStatePopulateError,
       "svcDhcpRestoreLseStateCiAddr": svcDhcpRestoreLseStateCiAddr,
       "svcDhcpRestoreLseStateProblem": svcDhcpRestoreLseStateProblem,
       "svcDhcpLseStateOldCiAddr": svcDhcpLseStateOldCiAddr,
       "svcDhcpLseStateOldChAddr": svcDhcpLseStateOldChAddr,
       "svcDhcpLseStateNewCiAddr": svcDhcpLseStateNewCiAddr,
       "svcDhcpLseStateNewChAddr": svcDhcpLseStateNewChAddr,
       "svcDhcpClientLease": svcDhcpClientLease,
       "svcDhcpPacketProblem": svcDhcpPacketProblem,
       "svcDhcpLseStatePopulateError": svcDhcpLseStatePopulateError,
       "hostConnectivityCiAddrType": hostConnectivityCiAddrType,
       "hostConnectivityCiAddr": hostConnectivityCiAddr,
       "hostConnectivityChAddr": hostConnectivityChAddr,
       "protectedMacForNotify": protectedMacForNotify,
       "staticHostDynamicMacIpAddress": staticHostDynamicMacIpAddress,
       "staticHostDynamicMacConflict": staticHostDynamicMacConflict,
       "tmnxSvcObjRow": tmnxSvcObjRow,
       "tmnxSvcObjRowDescr": tmnxSvcObjRowDescr,
       "tmnxSvcObjTodSuite": tmnxSvcObjTodSuite,
       "tmnxFailureDescription": tmnxFailureDescription,
       "svcDhcpProxyError": svcDhcpProxyError,
       "svcDhcpCoAError": svcDhcpCoAError,
       "svcDhcpSubAuthError": svcDhcpSubAuthError,
       "svcTlsMrpAttrRegFailedReason": svcTlsMrpAttrRegFailedReason,
       "svcTlsMrpAttrType": svcTlsMrpAttrType,
       "svcTlsMrpAttrValue": svcTlsMrpAttrValue,
       "svcMstiInstanceId": svcMstiInstanceId,
       "svcNotifSapPortId": svcNotifSapPortId,
       "svcNotifSapEncapValue": svcNotifSapEncapValue,
       "svcArpHostPopulateError": svcArpHostPopulateError,
       "svcHostAddrType": svcHostAddrType,
       "svcHostAddr": svcHostAddr,
       "tmnxServNotifications": tmnxServNotifications,
       "custTrapsPrefix": custTrapsPrefix,
       "custTraps": custTraps,
       "custCreated": custCreated,
       "custDeleted": custDeleted,
       "custMultSvcSiteCreated": custMultSvcSiteCreated,
       "custMultSvcSiteDeleted": custMultSvcSiteDeleted,
       "svcTrapsPrefix": svcTrapsPrefix,
       "svcTraps": svcTraps,
       "svcCreated": svcCreated,
       "svcDeleted": svcDeleted,
       "svcStatusChanged": svcStatusChanged,
       "svcTlsFdbTableFullAlarmRaised": svcTlsFdbTableFullAlarmRaised,
       "svcTlsFdbTableFullAlarmCleared": svcTlsFdbTableFullAlarmCleared,
       "iesIfCreated": iesIfCreated,
       "iesIfDeleted": iesIfDeleted,
       "iesIfStatusChanged": iesIfStatusChanged,
       "svcTlsMfibTableFullAlarmRaised": svcTlsMfibTableFullAlarmRaised,
       "svcTlsMfibTableFullAlarmCleared": svcTlsMfibTableFullAlarmCleared,
       "svcTlsMacPinningViolation": svcTlsMacPinningViolation,
       "svcTlsDHCPLseStRestoreProblem": svcTlsDHCPLseStRestoreProblem,
       "svcTlsDHCPLseStatePopulateErr": svcTlsDHCPLseStatePopulateErr,
       "svcDHCPLseStateRestoreProblem": svcDHCPLseStateRestoreProblem,
       "tmnxSvcObjTodSuiteApplicFailed": tmnxSvcObjTodSuiteApplicFailed,
       "tmnxEndPointTxActiveChanged": tmnxEndPointTxActiveChanged,
       "tmnxSvcPEDiscPolServOperStatChg": tmnxSvcPEDiscPolServOperStatChg,
       "svcEndPointMacLimitAlarmRaised": svcEndPointMacLimitAlarmRaised,
       "svcEndPointMacLimitAlarmCleared": svcEndPointMacLimitAlarmCleared,
       "svcTlsMrpAttrRegistrationFailed": svcTlsMrpAttrRegistrationFailed,
       "svcFdbMimDestTblFullAlrm": svcFdbMimDestTblFullAlrm,
       "svcFdbMimDestTblFullAlrmCleared": svcFdbMimDestTblFullAlrmCleared,
       "svcDHCPMiscellaneousProblem": svcDHCPMiscellaneousProblem,
       "svcPersistencyProblem": svcPersistencyProblem,
       "svcTlsMrpAttrTblFullAlarmRaised": svcTlsMrpAttrTblFullAlarmRaised,
       "svcTlsMrpAttrTblFullAlarmCleared": svcTlsMrpAttrTblFullAlarmCleared,
       "svcArpHostPopulateErr": svcArpHostPopulateErr,
       "svcEpipePbbOperStatusChanged": svcEpipePbbOperStatusChanged,
       "svcEPMCEPConfigMismatch": svcEPMCEPConfigMismatch,
       "svcEPMCEPConfigMismatchResolved": svcEPMCEPConfigMismatchResolved,
       "svcEPMCEPPassiveModeActive": svcEPMCEPPassiveModeActive,
       "svcEPMCEPPassiveModePassive": svcEPMCEPPassiveModePassive,
       "svcRestoreHostProblem": svcRestoreHostProblem,
       "svcTlsSiteDesigFwdrChg": svcTlsSiteDesigFwdrChg,
       "svcTlsGroupOperStatusChanged": svcTlsGroupOperStatusChanged,
       "svcMacFdbTblFullAlarm": svcMacFdbTblFullAlarm,
       "svcMacFdbTblFullAlarmCleared": svcMacFdbTblFullAlarmCleared,
       "svcMSPwRtMisconfig": svcMSPwRtMisconfig,
       "svcOperGrpOperStatusChanged": svcOperGrpOperStatusChanged,
       "svcMSPwRetryExpiredNotif": svcMSPwRetryExpiredNotif,
       "svcVllSiteDesigFwdrChg": svcVllSiteDesigFwdrChg,
       "tstpTrapsPrefix": tstpTrapsPrefix,
       "tstpTraps": tstpTraps,
       "topologyChangeVcpState": topologyChangeVcpState,
       "newRootVcpState": newRootVcpState,
       "newRootBridge": newRootBridge,
       "vcpActiveProtocolChange": vcpActiveProtocolChange,
       "tmnxNewCistRegionalRootBridge": tmnxNewCistRegionalRootBridge,
       "tmnxNewMstiRegionalRootBridge": tmnxNewMstiRegionalRootBridge,
       "topologyChangePipMajorState": topologyChangePipMajorState,
       "topologyChangePipState": topologyChangePipState,
       "tmnxPipStpExcepCondStateChng": tmnxPipStpExcepCondStateChng,
       "pipActiveProtocolChange": pipActiveProtocolChange}
)
