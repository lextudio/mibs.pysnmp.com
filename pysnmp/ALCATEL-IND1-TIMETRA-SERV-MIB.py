# SNMP MIB module (ALCATEL-IND1-TIMETRA-SERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-SERV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:13 2024
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

(TFilterID,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-FILTER-MIB",
    "TFilterID")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tSchedulerPolicyName,
 tVirtualSchedulerName) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-QOS-MIB",
    "tSchedulerPolicyName",
    "tVirtualSchedulerName")

(QTag,
 SdpBindId,
 ServiceAdminStatus,
 ServiceOperStatus,
 TCIRRate,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRRate,
 TPolicyStatementNameOrEmpty,
 TPortSchedulerPIR,
 TmnxActionType,
 TmnxAncpStringOrZero,
 TmnxCustId,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxManagedRouteStatus,
 TmnxPortID,
 TmnxServId,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "QTag",
    "SdpBindId",
    "ServiceAdminStatus",
    "ServiceOperStatus",
    "TCIRRate",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRRate",
    "TPolicyStatementNameOrEmpty",
    "TPortSchedulerPIR",
    "TmnxActionType",
    "TmnxAncpStringOrZero",
    "TmnxCustId",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxManagedRouteStatus",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrIDOrZero")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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


# MODULE-IDENTITY

timetraServicesMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 4)
)
timetraServicesMIBModule.setRevisions(
        ("1908-01-01 00:00",
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



class ServObjName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class ServObjDesc(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class ServObjLongDesc(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("apipe", 7),
          ("cpipe", 10),
          ("epipe", 1),
          ("fpipe", 8),
          ("ies", 5),
          ("ipipe", 9),
          ("mirror", 6),
          ("p3pipe", 2),
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



class SdpBindTlsBpduTranslation(Integer32, TextualConvention):
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
          ("cdp", 5),
          ("disabled", 2),
          ("pvst", 3),
          ("stp", 4),
          ("vtp", 6))
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 5),
          ("dhcp", 1),
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


class SvcISID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 16777215),
    )



class L2RouteOrigin(Integer32, TextualConvention):
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
        *(("bgp-l2vpn", 2),
          ("manual", 1),
          ("radius", 3))
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (1, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (1, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngQosSchedName"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (1, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrQosSchedName"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngQosPortIdSchedName"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngQosAssignmentPortId"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrQosPortIdSchedName"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrQosAssignmentPortId"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (1, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssIngQosSName"),
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


class _CustMssIngQosSPIR_Type(TPIRRate):
    """Custom type custMssIngQosSPIR based on TPIRRate"""
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


class _CustMssIngQosSCIR_Type(TCIRRate):
    """Custom type custMssIngQosSCIR based on TCIRRate"""
    defaultValue = -1


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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (1, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssEgrQosSName"),
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


class _CustMssEgrQosSPIR_Type(TPIRRate):
    """Custom type custMssEgrQosSPIR based on TPIRRate"""
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


class _CustMssEgrQosSCIR_Type(TCIRRate):
    """Custom type custMssEgrQosSCIR based on TCIRRate"""
    defaultValue = -1


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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (1, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (1, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngSchedPlcyPortStatsPort"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrSchedPlcyPortStatsPort"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("gre", 2),
          ("ldp", 3),
          ("none", 1))
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("bVpls", 2),
          ("iVpls", 3),
          ("none", 1))
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
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
        ValueRangeConstraint(1, 196607),
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
        ValueRangeConstraint(1, 10),
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
        ValueRangeConstraint(0, 16383),
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
        ValueRangeConstraint(1, 2048),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbMacAddr"),
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 4),
          ("host", 5),
          ("learned", 2),
          ("oam", 3),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfIndex"),
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
    iesIfVpnId.setStatus("current")
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("cem", 5),
          ("group", 3),
          ("ipMirror", 7),
          ("ipsec", 6),
          ("redundant", 4),
          ("service", 1),
          ("subscriber", 2))
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (1, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgName"),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm-only", 2),
          ("disable", 1))
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibInfoGrpAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibInfoSrcAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibInfoLocale"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibInfoPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibInfoEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibInfoSdpId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibInfoVcId"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibGrpSrcStatsGrpAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibGrpSrcStatsSrcAddr"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (1, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpName"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpName"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpMemberRemoteNodeAddrTp"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpMemberRemoteNodeAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpMemberIsSap"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpMemberPort"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpMemberEncap"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiInstanceId"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiInstanceId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiMvplsMinVlanTag"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiMvplsMaxVlanTag"),
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
    (1, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpName"),
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
    svcDhcpLeaseStateTable.setStatus("current")
_SvcDhcpLeaseStateEntry_Object = MibTableRow
svcDhcpLeaseStateEntry = _SvcDhcpLeaseStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1)
)
svcDhcpLeaseStateEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddr"),
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateEntry.setStatus("current")
_SvcDhcpLseStateCiAddrType_Type = InetAddressType
_SvcDhcpLseStateCiAddrType_Object = MibTableColumn
svcDhcpLseStateCiAddrType = _SvcDhcpLseStateCiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 1),
    _SvcDhcpLseStateCiAddrType_Type()
)
svcDhcpLseStateCiAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLseStateCiAddrType.setStatus("current")
_SvcDhcpLseStateCiAddr_Type = InetAddress
_SvcDhcpLseStateCiAddr_Object = MibTableColumn
svcDhcpLseStateCiAddr = _SvcDhcpLseStateCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 2),
    _SvcDhcpLseStateCiAddr_Type()
)
svcDhcpLseStateCiAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcDhcpLseStateCiAddr.setStatus("current")


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
    svcDhcpLseStateLocale.setStatus("current")
_SvcDhcpLseStatePortId_Type = TmnxPortID
_SvcDhcpLseStatePortId_Object = MibTableColumn
svcDhcpLseStatePortId = _SvcDhcpLseStatePortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 4),
    _SvcDhcpLseStatePortId_Type()
)
svcDhcpLseStatePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePortId.setStatus("current")
_SvcDhcpLseStateEncapValue_Type = TmnxEncapVal
_SvcDhcpLseStateEncapValue_Object = MibTableColumn
svcDhcpLseStateEncapValue = _SvcDhcpLseStateEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 5),
    _SvcDhcpLseStateEncapValue_Type()
)
svcDhcpLseStateEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateEncapValue.setStatus("current")
_SvcDhcpLseStateSdpId_Type = SdpId
_SvcDhcpLseStateSdpId_Object = MibTableColumn
svcDhcpLseStateSdpId = _SvcDhcpLseStateSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 6),
    _SvcDhcpLseStateSdpId_Type()
)
svcDhcpLseStateSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSdpId.setStatus("current")
_SvcDhcpLseStateVcId_Type = Unsigned32
_SvcDhcpLseStateVcId_Object = MibTableColumn
svcDhcpLseStateVcId = _SvcDhcpLseStateVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 7),
    _SvcDhcpLseStateVcId_Type()
)
svcDhcpLseStateVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateVcId.setStatus("current")
_SvcDhcpLseStateChAddr_Type = MacAddress
_SvcDhcpLseStateChAddr_Object = MibTableColumn
svcDhcpLseStateChAddr = _SvcDhcpLseStateChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 8),
    _SvcDhcpLseStateChAddr_Type()
)
svcDhcpLseStateChAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateChAddr.setStatus("current")
_SvcDhcpLseStateRemainLseTime_Type = Unsigned32
_SvcDhcpLseStateRemainLseTime_Object = MibTableColumn
svcDhcpLseStateRemainLseTime = _SvcDhcpLseStateRemainLseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 9),
    _SvcDhcpLseStateRemainLseTime_Type()
)
svcDhcpLseStateRemainLseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateRemainLseTime.setStatus("current")
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
    svcDhcpLseStateOption82.setStatus("current")
_SvcDhcpLseStatePersistKey_Type = Unsigned32
_SvcDhcpLseStatePersistKey_Object = MibTableColumn
svcDhcpLseStatePersistKey = _SvcDhcpLseStatePersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 11),
    _SvcDhcpLseStatePersistKey_Type()
)
svcDhcpLseStatePersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePersistKey.setStatus("current")
_SvcDhcpLseStateSubscrIdent_Type = DisplayString
_SvcDhcpLseStateSubscrIdent_Object = MibTableColumn
svcDhcpLseStateSubscrIdent = _SvcDhcpLseStateSubscrIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 12),
    _SvcDhcpLseStateSubscrIdent_Type()
)
svcDhcpLseStateSubscrIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSubscrIdent.setStatus("current")
_SvcDhcpLseStateSubProfString_Type = DisplayString
_SvcDhcpLseStateSubProfString_Object = MibTableColumn
svcDhcpLseStateSubProfString = _SvcDhcpLseStateSubProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 13),
    _SvcDhcpLseStateSubProfString_Type()
)
svcDhcpLseStateSubProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSubProfString.setStatus("current")
_SvcDhcpLseStateSlaProfString_Type = DisplayString
_SvcDhcpLseStateSlaProfString_Object = MibTableColumn
svcDhcpLseStateSlaProfString = _SvcDhcpLseStateSlaProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 14),
    _SvcDhcpLseStateSlaProfString_Type()
)
svcDhcpLseStateSlaProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSlaProfString.setStatus("current")


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
    svcDhcpLseStateShcvOperState.setStatus("current")
_SvcDhcpLseStateShcvChecks_Type = Unsigned32
_SvcDhcpLseStateShcvChecks_Object = MibTableColumn
svcDhcpLseStateShcvChecks = _SvcDhcpLseStateShcvChecks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 16),
    _SvcDhcpLseStateShcvChecks_Type()
)
svcDhcpLseStateShcvChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateShcvChecks.setStatus("current")
_SvcDhcpLseStateShcvReplies_Type = Unsigned32
_SvcDhcpLseStateShcvReplies_Object = MibTableColumn
svcDhcpLseStateShcvReplies = _SvcDhcpLseStateShcvReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 17),
    _SvcDhcpLseStateShcvReplies_Type()
)
svcDhcpLseStateShcvReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateShcvReplies.setStatus("current")
_SvcDhcpLseStateShcvReplyTime_Type = TimeStamp
_SvcDhcpLseStateShcvReplyTime_Object = MibTableColumn
svcDhcpLseStateShcvReplyTime = _SvcDhcpLseStateShcvReplyTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 18),
    _SvcDhcpLseStateShcvReplyTime_Type()
)
svcDhcpLseStateShcvReplyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateShcvReplyTime.setStatus("current")
_SvcDhcpLseStateClientId_Type = OctetString
_SvcDhcpLseStateClientId_Object = MibTableColumn
svcDhcpLseStateClientId = _SvcDhcpLseStateClientId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 19),
    _SvcDhcpLseStateClientId_Type()
)
svcDhcpLseStateClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateClientId.setStatus("current")
_SvcDhcpLseStateIAID_Type = Unsigned32
_SvcDhcpLseStateIAID_Object = MibTableColumn
svcDhcpLseStateIAID = _SvcDhcpLseStateIAID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 20),
    _SvcDhcpLseStateIAID_Type()
)
svcDhcpLseStateIAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateIAID.setStatus("current")
_SvcDhcpLseStateIAIDType_Type = IAIDType
_SvcDhcpLseStateIAIDType_Object = MibTableColumn
svcDhcpLseStateIAIDType = _SvcDhcpLseStateIAIDType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 21),
    _SvcDhcpLseStateIAIDType_Type()
)
svcDhcpLseStateIAIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateIAIDType.setStatus("current")


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
    svcDhcpLseStateCiAddrMaskLen.setStatus("current")
_SvcDhcpLseStateRetailerSvcId_Type = TmnxServId
_SvcDhcpLseStateRetailerSvcId_Object = MibTableColumn
svcDhcpLseStateRetailerSvcId = _SvcDhcpLseStateRetailerSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 23),
    _SvcDhcpLseStateRetailerSvcId_Type()
)
svcDhcpLseStateRetailerSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateRetailerSvcId.setStatus("current")
_SvcDhcpLseStateRetailerIf_Type = InterfaceIndexOrZero
_SvcDhcpLseStateRetailerIf_Object = MibTableColumn
svcDhcpLseStateRetailerIf = _SvcDhcpLseStateRetailerIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 24),
    _SvcDhcpLseStateRetailerIf_Type()
)
svcDhcpLseStateRetailerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateRetailerIf.setStatus("current")


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
    svcDhcpLseStateAncpString.setStatus("current")
_SvcDhcpLseStateFramedIpNetMaskTp_Type = InetAddressType
_SvcDhcpLseStateFramedIpNetMaskTp_Object = MibTableColumn
svcDhcpLseStateFramedIpNetMaskTp = _SvcDhcpLseStateFramedIpNetMaskTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 26),
    _SvcDhcpLseStateFramedIpNetMaskTp_Type()
)
svcDhcpLseStateFramedIpNetMaskTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateFramedIpNetMaskTp.setStatus("current")
_SvcDhcpLseStateFramedIpNetMask_Type = InetAddress
_SvcDhcpLseStateFramedIpNetMask_Object = MibTableColumn
svcDhcpLseStateFramedIpNetMask = _SvcDhcpLseStateFramedIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 27),
    _SvcDhcpLseStateFramedIpNetMask_Type()
)
svcDhcpLseStateFramedIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateFramedIpNetMask.setStatus("current")
_SvcDhcpLseStateBCastIpAddrType_Type = InetAddressType
_SvcDhcpLseStateBCastIpAddrType_Object = MibTableColumn
svcDhcpLseStateBCastIpAddrType = _SvcDhcpLseStateBCastIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 28),
    _SvcDhcpLseStateBCastIpAddrType_Type()
)
svcDhcpLseStateBCastIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBCastIpAddrType.setStatus("current")
_SvcDhcpLseStateBCastIpAddr_Type = InetAddress
_SvcDhcpLseStateBCastIpAddr_Object = MibTableColumn
svcDhcpLseStateBCastIpAddr = _SvcDhcpLseStateBCastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 29),
    _SvcDhcpLseStateBCastIpAddr_Type()
)
svcDhcpLseStateBCastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateBCastIpAddr.setStatus("current")
_SvcDhcpLseStateDefaultRouterTp_Type = InetAddressType
_SvcDhcpLseStateDefaultRouterTp_Object = MibTableColumn
svcDhcpLseStateDefaultRouterTp = _SvcDhcpLseStateDefaultRouterTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 30),
    _SvcDhcpLseStateDefaultRouterTp_Type()
)
svcDhcpLseStateDefaultRouterTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDefaultRouterTp.setStatus("current")
_SvcDhcpLseStateDefaultRouter_Type = InetAddress
_SvcDhcpLseStateDefaultRouter_Object = MibTableColumn
svcDhcpLseStateDefaultRouter = _SvcDhcpLseStateDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 31),
    _SvcDhcpLseStateDefaultRouter_Type()
)
svcDhcpLseStateDefaultRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDefaultRouter.setStatus("current")
_SvcDhcpLseStatePrimaryDnsType_Type = InetAddressType
_SvcDhcpLseStatePrimaryDnsType_Object = MibTableColumn
svcDhcpLseStatePrimaryDnsType = _SvcDhcpLseStatePrimaryDnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 32),
    _SvcDhcpLseStatePrimaryDnsType_Type()
)
svcDhcpLseStatePrimaryDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePrimaryDnsType.setStatus("current")
_SvcDhcpLseStatePrimaryDns_Type = InetAddress
_SvcDhcpLseStatePrimaryDns_Object = MibTableColumn
svcDhcpLseStatePrimaryDns = _SvcDhcpLseStatePrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 33),
    _SvcDhcpLseStatePrimaryDns_Type()
)
svcDhcpLseStatePrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePrimaryDns.setStatus("current")
_SvcDhcpLseStateSecondaryDnsType_Type = InetAddressType
_SvcDhcpLseStateSecondaryDnsType_Object = MibTableColumn
svcDhcpLseStateSecondaryDnsType = _SvcDhcpLseStateSecondaryDnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 34),
    _SvcDhcpLseStateSecondaryDnsType_Type()
)
svcDhcpLseStateSecondaryDnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSecondaryDnsType.setStatus("current")
_SvcDhcpLseStateSecondaryDns_Type = InetAddress
_SvcDhcpLseStateSecondaryDns_Object = MibTableColumn
svcDhcpLseStateSecondaryDns = _SvcDhcpLseStateSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 35),
    _SvcDhcpLseStateSecondaryDns_Type()
)
svcDhcpLseStateSecondaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSecondaryDns.setStatus("current")


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
    svcDhcpLseStateSessionTimeout.setStatus("current")
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
    svcDhcpLseStateServerLeaseStart.setStatus("current")
_SvcDhcpLseStateServerLastRenew_Type = DateAndTime
_SvcDhcpLseStateServerLastRenew_Object = MibTableColumn
svcDhcpLseStateServerLastRenew = _SvcDhcpLseStateServerLastRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 38),
    _SvcDhcpLseStateServerLastRenew_Type()
)
svcDhcpLseStateServerLastRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateServerLastRenew.setStatus("current")
_SvcDhcpLseStateServerLeaseEnd_Type = DateAndTime
_SvcDhcpLseStateServerLeaseEnd_Object = MibTableColumn
svcDhcpLseStateServerLeaseEnd = _SvcDhcpLseStateServerLeaseEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 39),
    _SvcDhcpLseStateServerLeaseEnd_Type()
)
svcDhcpLseStateServerLeaseEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateServerLeaseEnd.setStatus("current")
_SvcDhcpLseStateDhcpServerAddrType_Type = InetAddressType
_SvcDhcpLseStateDhcpServerAddrType_Object = MibTableColumn
svcDhcpLseStateDhcpServerAddrType = _SvcDhcpLseStateDhcpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 40),
    _SvcDhcpLseStateDhcpServerAddrType_Type()
)
svcDhcpLseStateDhcpServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDhcpServerAddrType.setStatus("current")
_SvcDhcpLseStateDhcpServerAddr_Type = InetAddress
_SvcDhcpLseStateDhcpServerAddr_Object = MibTableColumn
svcDhcpLseStateDhcpServerAddr = _SvcDhcpLseStateDhcpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 41),
    _SvcDhcpLseStateDhcpServerAddr_Type()
)
svcDhcpLseStateDhcpServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDhcpServerAddr.setStatus("current")
_SvcDhcpLseStateOriginSubscrId_Type = DhcpLseStateInfoOrigin
_SvcDhcpLseStateOriginSubscrId_Object = MibTableColumn
svcDhcpLseStateOriginSubscrId = _SvcDhcpLseStateOriginSubscrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 42),
    _SvcDhcpLseStateOriginSubscrId_Type()
)
svcDhcpLseStateOriginSubscrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateOriginSubscrId.setStatus("current")
_SvcDhcpLseStateOriginStrings_Type = DhcpLseStateInfoOrigin
_SvcDhcpLseStateOriginStrings_Object = MibTableColumn
svcDhcpLseStateOriginStrings = _SvcDhcpLseStateOriginStrings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 43),
    _SvcDhcpLseStateOriginStrings_Type()
)
svcDhcpLseStateOriginStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateOriginStrings.setStatus("current")
_SvcDhcpLseStateOriginLeaseInfo_Type = DhcpLseStateInfoOrigin
_SvcDhcpLseStateOriginLeaseInfo_Object = MibTableColumn
svcDhcpLseStateOriginLeaseInfo = _SvcDhcpLseStateOriginLeaseInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 44),
    _SvcDhcpLseStateOriginLeaseInfo_Type()
)
svcDhcpLseStateOriginLeaseInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateOriginLeaseInfo.setStatus("current")
_SvcDhcpLseStateDhcpClientAddrType_Type = InetAddressType
_SvcDhcpLseStateDhcpClientAddrType_Object = MibTableColumn
svcDhcpLseStateDhcpClientAddrType = _SvcDhcpLseStateDhcpClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 45),
    _SvcDhcpLseStateDhcpClientAddrType_Type()
)
svcDhcpLseStateDhcpClientAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDhcpClientAddrType.setStatus("current")
_SvcDhcpLseStateDhcpClientAddr_Type = InetAddress
_SvcDhcpLseStateDhcpClientAddr_Object = MibTableColumn
svcDhcpLseStateDhcpClientAddr = _SvcDhcpLseStateDhcpClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 46),
    _SvcDhcpLseStateDhcpClientAddr_Type()
)
svcDhcpLseStateDhcpClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateDhcpClientAddr.setStatus("current")
_SvcDhcpLseStateLeaseSplitActive_Type = TruthValue
_SvcDhcpLseStateLeaseSplitActive_Object = MibTableColumn
svcDhcpLseStateLeaseSplitActive = _SvcDhcpLseStateLeaseSplitActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 47),
    _SvcDhcpLseStateLeaseSplitActive_Type()
)
svcDhcpLseStateLeaseSplitActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateLeaseSplitActive.setStatus("current")


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
    svcDhcpLseStateInterDestId.setStatus("current")
_SvcDhcpLseStatePrimaryNbnsType_Type = InetAddressType
_SvcDhcpLseStatePrimaryNbnsType_Object = MibTableColumn
svcDhcpLseStatePrimaryNbnsType = _SvcDhcpLseStatePrimaryNbnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 49),
    _SvcDhcpLseStatePrimaryNbnsType_Type()
)
svcDhcpLseStatePrimaryNbnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePrimaryNbnsType.setStatus("current")
_SvcDhcpLseStatePrimaryNbns_Type = InetAddress
_SvcDhcpLseStatePrimaryNbns_Object = MibTableColumn
svcDhcpLseStatePrimaryNbns = _SvcDhcpLseStatePrimaryNbns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 50),
    _SvcDhcpLseStatePrimaryNbns_Type()
)
svcDhcpLseStatePrimaryNbns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStatePrimaryNbns.setStatus("current")
_SvcDhcpLseStateSecondaryNbnsType_Type = InetAddressType
_SvcDhcpLseStateSecondaryNbnsType_Object = MibTableColumn
svcDhcpLseStateSecondaryNbnsType = _SvcDhcpLseStateSecondaryNbnsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 51),
    _SvcDhcpLseStateSecondaryNbnsType_Type()
)
svcDhcpLseStateSecondaryNbnsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSecondaryNbnsType.setStatus("current")
_SvcDhcpLseStateSecondaryNbns_Type = InetAddress
_SvcDhcpLseStateSecondaryNbns_Object = MibTableColumn
svcDhcpLseStateSecondaryNbns = _SvcDhcpLseStateSecondaryNbns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 52),
    _SvcDhcpLseStateSecondaryNbns_Type()
)
svcDhcpLseStateSecondaryNbns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateSecondaryNbns.setStatus("current")
_SvcDhcpLseStateAppProfString_Type = DisplayString
_SvcDhcpLseStateAppProfString_Object = MibTableColumn
svcDhcpLseStateAppProfString = _SvcDhcpLseStateAppProfString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 53),
    _SvcDhcpLseStateAppProfString_Type()
)
svcDhcpLseStateAppProfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateAppProfString.setStatus("current")
_SvcDhcpLseStateNextHopMacAddr_Type = MacAddress
_SvcDhcpLseStateNextHopMacAddr_Object = MibTableColumn
svcDhcpLseStateNextHopMacAddr = _SvcDhcpLseStateNextHopMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 16, 1, 54),
    _SvcDhcpLseStateNextHopMacAddr_Type()
)
svcDhcpLseStateNextHopMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDhcpLseStateNextHopMacAddr.setStatus("current")
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsProtMacAddress"),
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
    svcDhcpLeaseStateModifyTable.setStatus("current")
_SvcDhcpLeaseStateModifyEntry_Object = MibTableRow
svcDhcpLeaseStateModifyEntry = _SvcDhcpLeaseStateModifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18, 1)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateModifyEntry.setStatus("current")


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
    svcDhcpLseStateModifySubIndent.setStatus("current")


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
    svcDhcpLseStateModifySubProfile.setStatus("current")


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
    svcDhcpLseStateModifySlaProfile.setStatus("current")


class _SvcDhcpLseStateEvaluateState_Type(TruthValue):
    """Custom type svcDhcpLseStateEvaluateState based on TruthValue"""


_SvcDhcpLseStateEvaluateState_Object = MibTableColumn
svcDhcpLseStateEvaluateState = _SvcDhcpLseStateEvaluateState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 18, 1, 4),
    _SvcDhcpLseStateEvaluateState_Type()
)
svcDhcpLseStateEvaluateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLseStateEvaluateState.setStatus("current")


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
    svcDhcpLseStateModInterDestId.setStatus("current")


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
    svcDhcpLseStateModifyAncpString.setStatus("current")


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
    svcDhcpLseStateModifyAppProfile.setStatus("current")
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointName"),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sap", 1),
          ("sdpBind", 2))
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
        ValueRangeConstraint(0, 196607),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfIndex"),
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
    (1, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyName"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscPolServerIndex"),
    (1, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyName"),
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


class _SvcPEDiscPolServerAddressType_Type(InetAddressType):
    """Custom type svcPEDiscPolServerAddressType based on InetAddressType"""


_SvcPEDiscPolServerAddressType_Object = MibTableColumn
svcPEDiscPolServerAddressType = _SvcPEDiscPolServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 23, 1, 3),
    _SvcPEDiscPolServerAddressType_Type()
)
svcPEDiscPolServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcPEDiscPolServerAddressType.setStatus("current")


class _SvcPEDiscPolServerAddress_Type(InetAddress):
    """Custom type svcPEDiscPolServerAddress based on InetAddress"""
    defaultHexValue = ""


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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcWholesalerID"),
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
_SvcDhcpLeaseStateActionTable_Object = MibTable
svcDhcpLeaseStateActionTable = _SvcDhcpLeaseStateActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 25)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateActionTable.setStatus("current")
_SvcDhcpLeaseStateActionEntry_Object = MibTableRow
svcDhcpLeaseStateActionEntry = _SvcDhcpLeaseStateActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 25, 1)
)
if mibBuilder.loadTexts:
    svcDhcpLeaseStateActionEntry.setStatus("current")


class _SvcDhcpLseStateForceRenew_Type(TruthValue):
    """Custom type svcDhcpLseStateForceRenew based on TruthValue"""


_SvcDhcpLseStateForceRenew_Object = MibTableColumn
svcDhcpLseStateForceRenew = _SvcDhcpLseStateForceRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 25, 1, 1),
    _SvcDhcpLseStateForceRenew_Type()
)
svcDhcpLseStateForceRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcDhcpLseStateForceRenew.setStatus("current")
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibEntryType"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibGrpMacAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibGrpInetAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibGrpInetAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibSrcInetAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibSrcInetAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibLocale"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibSdpId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibVcId"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibStatsEntryType"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibStatsGrpMacAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibStatsGrpInetAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibStatsGrpInetAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibStatsSrcInetAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibStatsSrcInetAddr"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
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
    svcTlsBgpADVsiRD.setStatus("current")
_SvcTlsBgpADExportRteTarget_Type = TNamedItemOrEmpty
_SvcTlsBgpADExportRteTarget_Object = MibTableColumn
svcTlsBgpADExportRteTarget = _SvcTlsBgpADExportRteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 6),
    _SvcTlsBgpADExportRteTarget_Type()
)
svcTlsBgpADExportRteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADExportRteTarget.setStatus("current")


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
    svcTlsBgpADVsiExportPolicy1.setStatus("current")


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
    svcTlsBgpADVsiExportPolicy2.setStatus("current")


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
    svcTlsBgpADVsiExportPolicy3.setStatus("current")


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
    svcTlsBgpADVsiExportPolicy4.setStatus("current")


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
    svcTlsBgpADVsiExportPolicy5.setStatus("current")
_SvcTlsBgpADImportRteTarget_Type = TNamedItemOrEmpty
_SvcTlsBgpADImportRteTarget_Object = MibTableColumn
svcTlsBgpADImportRteTarget = _SvcTlsBgpADImportRteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 31, 1, 12),
    _SvcTlsBgpADImportRteTarget_Type()
)
svcTlsBgpADImportRteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADImportRteTarget.setStatus("current")


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
    svcTlsBgpADVsiImportPolicy1.setStatus("current")


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
    svcTlsBgpADVsiImportPolicy2.setStatus("current")


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
    svcTlsBgpADVsiImportPolicy3.setStatus("current")


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
    svcTlsBgpADVsiImportPolicy4.setStatus("current")


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
    svcTlsBgpADVsiImportPolicy5.setStatus("current")


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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
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
_SvcEpipePbbBvplsDstMac_Type = MacAddress
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiInstanceId"),
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
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpManagedRouteInetAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpManagedRouteInetAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpManagedRoutePrefixLen"),
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
    ("ALCATEL-IND1-TIMETRA-SERV-MIB",
     "svcDhcpLeaseStateModifyEntry")
)
svcDhcpLeaseStateModifyEntry.setIndexNames(*svcDhcpLeaseStateEntry.getIndexNames())
svcDhcpLeaseStateEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-SERV-MIB",
     "svcDhcpLeaseStateActionEntry")
)
svcDhcpLeaseStateActionEntry.setIndexNames(*svcDhcpLeaseStateEntry.getIndexNames())
svcTlsInfoEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-SERV-MIB",
     "svcTlsBackboneInfoEntry")
)
svcTlsBackboneInfoEntry.setIndexNames(*svcTlsInfoEntry.getIndexNames())

# Managed Objects groups

tmnxCustV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1, 2, 100)
)
tmnxCustV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custNumEntries"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custNextFreeId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custDescription"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custContact"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custPhone"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteDescription"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteScope"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteAssignment"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteIngressSchedulerPolicy"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteEgressSchedulerPolicy"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteTodSuite"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteCurrentIngrSchedPlcy"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteCurrentEgrSchedPlcy"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteEgressAggRateLimit"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteIntendedIngrSchedPlcy"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteIntendedEgrSchedPlcy"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteFrameBasedAccnt"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngQosSchedStatsForwardedPackets"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngQosSchedStatsForwardedOctets"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrQosSchedStatsForwardedPackets"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrQosSchedStatsForwardedOctets"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngQosPortSchedFwdPkts"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngQosPortSchedFwdOctets"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrQosPortSchedFwdPkts"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrQosPortSchedFwdOctets"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssIngQosSRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssIngQosSLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssIngQosSOverrideFlags"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssIngQosSPIR"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssIngQosSCIR"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssIngQosSSummedCIR"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssEgrQosSRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssEgrQosSLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssEgrQosSOverrideFlags"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssEgrQosSPIR"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssEgrQosSCIR"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMssEgrQosSSummedCIR"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngSchedPlcyStatsFwdPkt"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngSchedPlcyStatsFwdOct"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrSchedPlcyStatsFwdPkt"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrSchedPlcyStatsFwdOct"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngSchedPlcyPortStatsFwdPkt"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custIngSchedPlcyPortStatsFwdOct"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrSchedPlcyPortStatsFwdPkt"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custEgrSchedPlcyPortStatsFwdOct"))
)
if mibBuilder.loadTexts:
    tmnxCustV6v0Group.setStatus("current")

tmnxSvcV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 101)
)
tmnxSvcV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcNumEntries"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcCustId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcIpRouting"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDescription"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcMtu"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcNumSaps"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcNumSdps"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDefMeshVcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVRouterId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcAutoBind"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcLastStatusChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVllType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcMgmtVpls"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcRadiusDiscovery"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcRadiusUserName"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcRadiusUserNameType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVcSwitching"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcRadiusPEDiscPolicy"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcRadiusDiscoveryShutdown"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVplsType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTotalFdbMimDestIdxEntries"))
)
if mibBuilder.loadTexts:
    tmnxSvcV6v0Group.setStatus("current")

tmnxSvcTlsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 102)
)
tmnxSvcTlsV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMacLearning"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsDiscardUnknownDest"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbTableSize"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbNumEntries"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbNumStaticEntries"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbLocalAgeTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbRemoteAgeTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpPriority"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpBridgeAddress"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpTimeSinceTopologyChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpTopologyChanges"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpDesignatedRoot"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpRootCost"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpRootPort"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpMaxAge"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpHelloTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpForwardDelay"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpBridgeMaxAge"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpBridgeHelloTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpBridgeForwardDelay"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpVirtualRootBridgeStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMacAgeing"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpTopologyChangeActive"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbTableFullHighWatermark"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbTableFullLowWatermark"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsCustId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpVersion"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpHoldCount"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpPrimaryBridge"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpBridgeInstanceId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpVcpOperProtocol"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMacMoveMaxRate"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMacMoveRetryTimeout"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMacMoveAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMacRelearnOnly"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMfibTableSize"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMfibTableFullHighWatermark"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMfibTableFullLowWatermark"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMacFlushOnFail"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpRegionName"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpRegionRevision"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpBridgeMaxHops"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpCistRegionalRoot"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpCistIntRootCost"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpCistRemainingHopCount"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpCistRegionalRootPort"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbNumLearnedEntries"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbNumOamEntries"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbNumDhcpEntries"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbNumHostEntries"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsShcvAction"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsShcvSrcIp"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsShcvSrcMac"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsShcvInterval"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsPriPortsCumulativeFactor"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsSecPortsCumulativeFactor"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsL2ptTermEnabled"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsPropagateMacFlush"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpMaxAttributes"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttributeCount"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpFailedRegisterCount"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpFloodTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrTblHighWatermark"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrTblLowWatermark"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMcPathMgmtPlcyName"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpAdminQinqFixedTagVal"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsV6v0Group.setStatus("current")

tmnxSvcTlsFdbV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 103)
)
tmnxSvcTlsFdbV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbMacAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbLocale"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbPortId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbSdpId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbVcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbCustId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbLastStateChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbProtected"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbBackboneDstMac"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbNumIVplsMac"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbEndPointName"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbEPMacOperSdpId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbEPMacOperVcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsFdbPbbNumEpipes"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsProtMacRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsProtMacLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsFdbV6v0Group.setStatus("current")

tmnxSvcIesIfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 104)
)
tmnxSvcIesIfV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfIndex"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfName"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfDescription"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfCustId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfLoopback"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfLastStatusChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfShcvSource"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfShcvAction"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfShcvInterval"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesGrpIfOperUpWhileEmpty"))
)
if mibBuilder.loadTexts:
    tmnxSvcIesIfV6v0Group.setStatus("current")

tmnxSvcTlsShgV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 105)
)
tmnxSvcTlsShgV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgCustId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgInstanceId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgDescription"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgResidential"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgRestProtSrcMac"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgRestUnprotDstMac"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgRestProtSrcMacAction"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsShgCreationOrigin"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsShgV6v0Group.setStatus("current")

tmnxSvcTlsMFibV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 106)
)
tmnxSvcTlsMFibV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibFwdOrBlk"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibSvcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibStatsForwardedPkts"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibStatsForwardedOctets"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsMFibV6v0Group.setStatus("current")

tmnxSvcRdntV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 107)
)
tmnxSvcRdntV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpDescription"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpMemberRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsRdntGrpMemberLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxSvcRdntV6v0Group.setStatus("current")

tmnxSvcTlsMstiV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 108)
)
tmnxSvcTlsMstiV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiPriority"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiRegionalRoot"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiIntRootCost"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiRemainingHopCount"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiRegionalRootPort"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiMvplsRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsMstiV6v0Group.setStatus("current")

tmnxSvcTlsEgrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 109)
)
tmnxSvcTlsEgrV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpDescription"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpChainLimit"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpEncapType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpDot1qEtherType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpQinqEtherType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpIpv6FilterId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpQinqFixedTagPosition"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsEgrMcGrpOperQinqFixedTagVal"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsEgrV6v0Group.setStatus("current")

tmnxSvcDhcpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 110)
)
tmnxSvcDhcpV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateLocale"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStatePortId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateSdpId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateVcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateRemainLseTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateOption82"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStatePersistKey"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateSubscrIdent"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateSubProfString"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateSlaProfString"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateShcvOperState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateShcvChecks"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateShcvReplies"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateShcvReplyTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateClientId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateIAID"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateIAIDType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateCiAddrMaskLen"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateRetailerSvcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateRetailerIf"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateAncpString"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateFramedIpNetMaskTp"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateFramedIpNetMask"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateBCastIpAddrType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateBCastIpAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateDefaultRouterTp"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateDefaultRouter"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryDnsType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryDns"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryDnsType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryDns"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateSessionTimeout"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateServerLeaseStart"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateServerLastRenew"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateServerLeaseEnd"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpServerAddrType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpServerAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateOriginSubscrId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateOriginStrings"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateOriginLeaseInfo"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpClientAddrType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateDhcpClientAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateLeaseSplitActive"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateInterDestId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryNbnsType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStatePrimaryNbns"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryNbnsType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateSecondaryNbns"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNextHopMacAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateModifySubIndent"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateModifySubProfile"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateModifySlaProfile"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateEvaluateState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateModInterDestId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateModifyAncpString"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateForceRenew"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpManagedRouteStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcDhcpV6v0Group.setStatus("current")

tmnxSvcEndPointV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 111)
)
tmnxSvcEndPointV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointDescription"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActiveType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActivePortId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActiveEncap"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActiveSdpId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointForceSwitchOver"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointForceSwitchOverSdpId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointActiveHoldDelay"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointIgnoreStandbySig"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointMacPinning"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointMacLimit"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointSuppressStandbySig"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActiveChangeCount"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActiveLastChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActiveUpTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointRevertTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointRevertTimeCountDn"))
)
if mibBuilder.loadTexts:
    tmnxSvcEndPointV6v0Group.setStatus("current")

tmnxSvcPEV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 112)
)
tmnxSvcPEV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyPassword"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyInterval"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscoveryPolicyTimeout"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscPolServerRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscPolServerAddressType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscPolServerAddress"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscPolServerSecret"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscPolServerOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscPolServerPort"))
)
if mibBuilder.loadTexts:
    tmnxSvcPEV6v0Group.setStatus("current")

tmnxSvcIfDHCP6V6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 114)
)
tmnxSvcIfDHCP6V6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcIfDHCP6MsgStatsLstClrd"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcIfDHCP6MsgStatsRcvd"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcIfDHCP6MsgStatsSent"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcIfDHCP6MsgStatsDropped"))
)
if mibBuilder.loadTexts:
    tmnxSvcIfDHCP6V6v0Group.setStatus("current")

tmnxSvcTlsBackbone6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 115)
)
tmnxSvcTlsBackbone6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBackboneSrcMac"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBackboneVplsSvcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBackboneVplsSvcISID"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBackboneOperSrcMac"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBackboneOperVplsSvcISID"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBackboneLDPMacFlush"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBackboneVplsStp"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsBackbone6v0Group.setStatus("current")

tmnxSvcTlsBgpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 116)
)
tmnxSvcTlsBgpV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVplsId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiPrefix"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiRD"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADExportRteTarget"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiExportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADImportRteTarget"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADVsiImportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsBgpADAdminStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsBgpV6v0Group.setStatus("current")

tmnxSvcEpipeV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 117)
)
tmnxSvcEpipeV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEpipePbbTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEpipePbbRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEpipePbbLastChngd"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEpipePbbBvplsSvcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEpipePbbBvplsDstMac"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEpipePbbSvcISID"))
)
if mibBuilder.loadTexts:
    tmnxSvcEpipeV6v0Group.setStatus("current")

tmnxSvcTlsPipV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 118)
)
tmnxSvcTlsPipV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpPortState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpPortRole"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpDesignatedBridge"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpDesignatedPort"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpException"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpForwardTransitions"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpInConfigBpdus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpInTcnBpdus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpInRstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpInMstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpInBadBpdus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpOutConfigBpdus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpOutTcnBpdus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpOutRstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpOutMstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpMvplsPruneState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpOperProtocol"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpPortNum"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipMstiPortRole"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipMstiPortState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipMstiDesignatedBridge"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipMstiDesignatedPort"))
)
if mibBuilder.loadTexts:
    tmnxSvcTlsPipV6v0Group.setStatus("current")

tmnxApipeV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 119)
)
tmnxApipeV3v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcApipeInterworking")
)
if mibBuilder.loadTexts:
    tmnxApipeV3v0Group.setStatus("current")

tmnxSvcRoutedCOV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 120)
)
tmnxSvcRoutedCOV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfParentIf"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfFwdServId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfFwdSubIf"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesGrpIfRedInterface"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcWholesalerNumStaticHosts"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcWholesalerNumDynamicHosts"))
)
if mibBuilder.loadTexts:
    tmnxSvcRoutedCOV5v0Group.setStatus("current")

tmnxSvcBsxV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 121)
)
tmnxSvcBsxV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateAppProfString"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateModifyAppProfile"))
)
if mibBuilder.loadTexts:
    tmnxSvcBsxV6v0Group.setStatus("current")

tmnxSvcNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 200)
)
tmnxSvcNotifyObjsV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpRestoreLseStateCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpRestoreLseStateProblem"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateOldCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateOldChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpClientLease"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpPacketProblem"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStatePopulateError"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "hostConnectivityCiAddrType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "hostConnectivityCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "hostConnectivityChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "protectedMacForNotify"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "staticHostDynamicMacIpAddress"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "staticHostDynamicMacConflict"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxSvcObjRow"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxSvcObjRowDescr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxSvcObjTodSuite"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxFailureDescription"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpProxyError"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpCoAError"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpSubAuthError"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrRegFailedReason"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcMstiInstanceId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxCustomerBridgeId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxCustomerRootBridgeId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxOtherBridgeId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxOldSdpBindTlsStpPortState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxVcpState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "macPinningMacAddress"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "macPinningPinnedRow"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "macPinningPinnedRowDescr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "macPinningViolatingRow"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "macPinningViolatingRowDescr"))
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyObjsV6v0Group.setStatus("current")

tmnxSvcObsoletedV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 300)
)
tmnxSvcObsoletedV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpHoldTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibInfoFwdOrBlk"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibInfoSvcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibGrpSrcStatsForwardedPkts"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMFibGrpSrcStatsForwardedOctets"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDHCPClientLease"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStateOldCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStateOldChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateSvcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStatePortId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateEncapVal"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateProblem"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpPacketProblem"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStatePopulateError"))
)
if mibBuilder.loadTexts:
    tmnxSvcObsoletedV6v0Group.setStatus("current")


# Notification objects

custCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 1, 0, 1)
)
custCreated.setObjects(
    ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId")
)
if mibBuilder.loadTexts:
    custCreated.setStatus(
        "obsolete"
    )

custDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 1, 0, 2)
)
custDeleted.setObjects(
    ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId")
)
if mibBuilder.loadTexts:
    custDeleted.setStatus(
        "obsolete"
    )

custMultSvcSiteCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 1, 0, 3)
)
custMultSvcSiteCreated.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"))
)
if mibBuilder.loadTexts:
    custMultSvcSiteCreated.setStatus(
        "obsolete"
    )

custMultSvcSiteDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 1, 0, 4)
)
custMultSvcSiteDeleted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteName"))
)
if mibBuilder.loadTexts:
    custMultSvcSiteDeleted.setStatus(
        "obsolete"
    )

svcCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 1)
)
svcCreated.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcType"))
)
if mibBuilder.loadTexts:
    svcCreated.setStatus(
        "obsolete"
    )

svcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 2)
)
svcDeleted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcDeleted.setStatus(
        "obsolete"
    )

svcStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 3)
)
svcStatusChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcOperStatus"))
)
if mibBuilder.loadTexts:
    svcStatusChanged.setStatus(
        "current"
    )

svcTlsFdbTableFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 4)
)
svcTlsFdbTableFullAlarmRaised.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsFdbTableFullAlarmRaised.setStatus(
        "current"
    )

svcTlsFdbTableFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 5)
)
svcTlsFdbTableFullAlarmCleared.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsFdbTableFullAlarmCleared.setStatus(
        "current"
    )

iesIfCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 6)
)
iesIfCreated.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfIndex"))
)
if mibBuilder.loadTexts:
    iesIfCreated.setStatus(
        "obsolete"
    )

iesIfDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 7)
)
iesIfDeleted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfIndex"))
)
if mibBuilder.loadTexts:
    iesIfDeleted.setStatus(
        "obsolete"
    )

iesIfStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 8)
)
iesIfStatusChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfIndex"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfOperStatus"))
)
if mibBuilder.loadTexts:
    iesIfStatusChanged.setStatus(
        "current"
    )

svcTlsMfibTableFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 9)
)
svcTlsMfibTableFullAlarmRaised.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsMfibTableFullAlarmRaised.setStatus(
        "current"
    )

svcTlsMfibTableFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 10)
)
svcTlsMfibTableFullAlarmCleared.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsMfibTableFullAlarmCleared.setStatus(
        "current"
    )

svcTlsMacPinningViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 11)
)
svcTlsMacPinningViolation.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "macPinningMacAddress"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "macPinningPinnedRow"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "macPinningPinnedRowDescr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "macPinningViolatingRow"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "macPinningViolatingRowDescr"))
)
if mibBuilder.loadTexts:
    svcTlsMacPinningViolation.setStatus(
        "current"
    )

svcTlsDHCPLseStRestoreProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 12)
)
svcTlsDHCPLseStRestoreProblem.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateSvcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStatePortId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateEncapVal"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpRestoreLseStateProblem"))
)
if mibBuilder.loadTexts:
    svcTlsDHCPLseStRestoreProblem.setStatus(
        "obsolete"
    )

svcTlsDHCPLseStatePopulateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 13)
)
svcTlsDHCPLseStatePopulateErr.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStatePopulateError"))
)
if mibBuilder.loadTexts:
    svcTlsDHCPLseStatePopulateErr.setStatus(
        "obsolete"
    )

svcDHCPLseStateRestoreProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 14)
)
svcDHCPLseStateRestoreProblem.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpRestoreLseStateCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpRestoreLseStateProblem"))
)
if mibBuilder.loadTexts:
    svcDHCPLseStateRestoreProblem.setStatus(
        "current"
    )

tmnxSvcObjTodSuiteApplicFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 15)
)
tmnxSvcObjTodSuiteApplicFailed.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxSvcObjRow"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxSvcObjRowDescr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxSvcObjTodSuite"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxFailureDescription"))
)
if mibBuilder.loadTexts:
    tmnxSvcObjTodSuiteApplicFailed.setStatus(
        "current"
    )

tmnxEndPointTxActiveChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 16)
)
tmnxEndPointTxActiveChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActiveType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActivePortId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActiveEncap"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointTxActiveSdpId"))
)
if mibBuilder.loadTexts:
    tmnxEndPointTxActiveChanged.setStatus(
        "current"
    )

tmnxSvcPEDiscPolServOperStatChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 17)
)
tmnxSvcPEDiscPolServOperStatChg.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscPolServerAddressType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscPolServerAddress"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPEDiscPolServerOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSvcPEDiscPolServOperStatChg.setStatus(
        "current"
    )

svcEndPointMacLimitAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 18)
)
svcEndPointMacLimitAlarmRaised.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointMacLimit"))
)
if mibBuilder.loadTexts:
    svcEndPointMacLimitAlarmRaised.setStatus(
        "current"
    )

svcEndPointMacLimitAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 19)
)
svcEndPointMacLimitAlarmCleared.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointMacLimit"))
)
if mibBuilder.loadTexts:
    svcEndPointMacLimitAlarmCleared.setStatus(
        "current"
    )

svcTlsMrpAttrRegistrationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 20)
)
svcTlsMrpAttrRegistrationFailed.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrRegFailedReason"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrValue"))
)
if mibBuilder.loadTexts:
    svcTlsMrpAttrRegistrationFailed.setStatus(
        "current"
    )

svcFdbMimDestTblFullAlrm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 21)
)
svcFdbMimDestTblFullAlrm.setObjects(
    ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTotalFdbMimDestIdxEntries")
)
if mibBuilder.loadTexts:
    svcFdbMimDestTblFullAlrm.setStatus(
        "current"
    )

svcFdbMimDestTblFullAlrmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 22)
)
svcFdbMimDestTblFullAlrmCleared.setObjects(
    ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTotalFdbMimDestIdxEntries")
)
if mibBuilder.loadTexts:
    svcFdbMimDestTblFullAlrmCleared.setStatus(
        "current"
    )

svcDHCPMiscellaneousProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 23)
)
svcDHCPMiscellaneousProblem.setObjects(
    ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxFailureDescription")
)
if mibBuilder.loadTexts:
    svcDHCPMiscellaneousProblem.setStatus(
        "current"
    )

svcPersistencyProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 24)
)
svcPersistencyProblem.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxFailureDescription"))
)
if mibBuilder.loadTexts:
    svcPersistencyProblem.setStatus(
        "current"
    )

svcTlsMrpAttrTblFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 25)
)
svcTlsMrpAttrTblFullAlarmRaised.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsMrpAttrTblFullAlarmRaised.setStatus(
        "current"
    )

svcTlsMrpAttrTblFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 2, 0, 26)
)
svcTlsMrpAttrTblFullAlarmCleared.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"))
)
if mibBuilder.loadTexts:
    svcTlsMrpAttrTblFullAlarmCleared.setStatus(
        "current"
    )

topologyChangeVcpState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 3)
)
topologyChangeVcpState.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxVcpState"))
)
if mibBuilder.loadTexts:
    topologyChangeVcpState.setStatus(
        "current"
    )

newRootVcpState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 4)
)
newRootVcpState.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"))
)
if mibBuilder.loadTexts:
    newRootVcpState.setStatus(
        "current"
    )

newRootBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 7)
)
newRootBridge.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"))
)
if mibBuilder.loadTexts:
    newRootBridge.setStatus(
        "current"
    )

vcpActiveProtocolChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 32)
)
vcpActiveProtocolChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpVcpOperProtocol"))
)
if mibBuilder.loadTexts:
    vcpActiveProtocolChange.setStatus(
        "current"
    )

tmnxNewCistRegionalRootBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 33)
)
tmnxNewCistRegionalRootBridge.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpCistRegionalRoot"))
)
if mibBuilder.loadTexts:
    tmnxNewCistRegionalRootBridge.setStatus(
        "current"
    )

tmnxNewMstiRegionalRootBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 34)
)
tmnxNewMstiRegionalRootBridge.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcMstiInstanceId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiRegionalRoot"))
)
if mibBuilder.loadTexts:
    tmnxNewMstiRegionalRootBridge.setStatus(
        "current"
    )

topologyChangePipMajorState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 39)
)
topologyChangePipMajorState.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"))
)
if mibBuilder.loadTexts:
    topologyChangePipMajorState.setStatus(
        "current"
    )

topologyChangePipState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 40)
)
topologyChangePipState.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"))
)
if mibBuilder.loadTexts:
    topologyChangePipState.setStatus(
        "current"
    )

tmnxPipStpExcepCondStateChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 41)
)
tmnxPipStpExcepCondStateChng.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsPipStpException"))
)
if mibBuilder.loadTexts:
    tmnxPipStpExcepCondStateChng.setStatus(
        "current"
    )

pipActiveProtocolChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 42)
)
pipActiveProtocolChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"))
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
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcStatusChanged"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbTableFullAlarmRaised"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsFdbTableFullAlarmCleared"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfStatusChanged"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMfibTableFullAlarmRaised"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMfibTableFullAlarmCleared"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMacPinningViolation"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDHCPLseStateRestoreProblem"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxSvcObjTodSuiteApplicFailed"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxEndPointTxActiveChanged"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxSvcPEDiscPolServOperStatChg"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointMacLimitAlarmRaised"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcEndPointMacLimitAlarmCleared"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrRegistrationFailed"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrTblFullAlarmRaised"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMrpAttrTblFullAlarmCleared"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "topologyChangeVcpState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "newRootVcpState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "newRootBridge"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "vcpActiveProtocolChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxNewCistRegionalRootBridge"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxNewMstiRegionalRootBridge"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "topologyChangePipMajorState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "topologyChangePipState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxPipStpExcepCondStateChng"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "pipActiveProtocolChange"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcFdbMimDestTblFullAlrm"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcFdbMimDestTblFullAlrmCleared"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDHCPMiscellaneousProblem"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcPersistencyProblem"))
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyV6v0Group.setStatus(
        "current"
    )

tmnxSvcNotifyObsoletedGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 2, 402)
)
tmnxSvcNotifyObsoletedGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custCreated"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custDeleted"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteCreated"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "custMultSvcSiteDeleted"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcCreated"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDeleted"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfCreated"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "iesIfDeleted"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsDHCPLseStRestoreProblem"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsDHCPLseStatePopulateErr"))
)
if mibBuilder.loadTexts:
    tmnxSvcNotifyObsoletedGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxCustCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 1, 1, 100)
)
if mibBuilder.loadTexts:
    tmnxCustCompliance.setStatus(
        "current"
    )

tmnxSvc7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 100)
)
if mibBuilder.loadTexts:
    tmnxSvc7450V6v0Compliance.setStatus(
        "current"
    )

tmnxSvc7750V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 101)
)
if mibBuilder.loadTexts:
    tmnxSvc7750V6v0Compliance.setStatus(
        "current"
    )

tmnxSvc7710V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 2, 1, 102)
)
if mibBuilder.loadTexts:
    tmnxSvc7710V6v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-SERV-MIB",
    **{"ServObjName": ServObjName,
       "ServObjDesc": ServObjDesc,
       "ServObjLongDesc": ServObjLongDesc,
       "ServType": ServType,
       "VpnId": VpnId,
       "SdpId": SdpId,
       "SdpTemplateId": SdpTemplateId,
       "PWTemplateId": PWTemplateId,
       "SdpBindTlsBpduTranslation": SdpBindTlsBpduTranslation,
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
       "SvcISID": SvcISID,
       "L2RouteOrigin": L2RouteOrigin,
       "ConfigStatus": ConfigStatus,
       "timetraServicesMIBModule": timetraServicesMIBModule,
       "tmnxServConformance": tmnxServConformance,
       "tmnxCustConformance": tmnxCustConformance,
       "tmnxCustCompliances": tmnxCustCompliances,
       "tmnxCustCompliance": tmnxCustCompliance,
       "tmnxCustGroups": tmnxCustGroups,
       "tmnxCustV6v0Group": tmnxCustV6v0Group,
       "tmnxSvcConformance": tmnxSvcConformance,
       "tmnxSvcCompliances": tmnxSvcCompliances,
       "tmnxSvc7450V6v0Compliance": tmnxSvc7450V6v0Compliance,
       "tmnxSvc7750V6v0Compliance": tmnxSvc7750V6v0Compliance,
       "tmnxSvc7710V6v0Compliance": tmnxSvc7710V6v0Compliance,
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
       "tmnxSvcNotifyObjsV6v0Group": tmnxSvcNotifyObjsV6v0Group,
       "tmnxSvcObsoletedV6v0Group": tmnxSvcObsoletedV6v0Group,
       "tmnxSvcNotifyV6v0Group": tmnxSvcNotifyV6v0Group,
       "tmnxSvcNotifyObsoletedGroup": tmnxSvcNotifyObsoletedGroup,
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
       "svcApipeInfoTable": svcApipeInfoTable,
       "svcApipeInfoEntry": svcApipeInfoEntry,
       "svcApipeInterworking": svcApipeInterworking,
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
       "iesGrpIfTable": iesGrpIfTable,
       "iesGrpIfEntry": iesGrpIfEntry,
       "iesGrpIfRedInterface": iesGrpIfRedInterface,
       "iesGrpIfOperUpWhileEmpty": iesGrpIfOperUpWhileEmpty,
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
