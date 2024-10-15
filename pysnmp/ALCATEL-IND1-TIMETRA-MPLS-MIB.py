# SNMP MIB module (ALCATEL-IND1-TIMETRA-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:16 2024
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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxOperState,
 TmnxVRtrMplsLspID) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxOperState",
    "TmnxVRtrMplsLspID")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(MplsLSPID,
 MplsLabel,
 mplsXCLspId) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "MplsLSPID",
    "MplsLabel",
    "mplsXCLspId")

(mplsTunnelARHopEntry,
 mplsTunnelIndex,
 mplsTunnelIngressLSRId,
 mplsTunnelInstance) = mibBuilder.importSymbols(
    "MPLS-TE-MIB",
    "mplsTunnelARHopEntry",
    "mplsTunnelIndex",
    "mplsTunnelIngressLSRId",
    "mplsTunnelInstance")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

timetraMplsMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 6)
)
timetraMplsMIBModule.setRevisions(
        ("1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-23 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1900-09-07 00:00",
         "1900-08-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMplsLspFailCode(Integer32, TextualConvention):
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
              26)
        )
    )
    namedValues = NamedValues(
        *(("admissionControlError", 1),
          ("badL3PID", 9),
          ("badNode", 6),
          ("emptyPathInManualBypassLsp", 22),
          ("hopLimitExceeded", 20),
          ("labelAllocationError", 8),
          ("looseHopsInFRRLsp", 15),
          ("looseHopsInManualBypassLsp", 21),
          ("lspFlowControlled", 23),
          ("noCspfRouteOwner", 18),
          ("noCspfRouteToDestination", 19),
          ("noEgressMplsInterface", 13),
          ("noEgressRsvpInterface", 14),
          ("noError", 0),
          ("noResourcesAvailable", 5),
          ("noRouteToDestination", 2),
          ("retryExceeded", 17),
          ("routingError", 4),
          ("routingLoop", 7),
          ("srlgPrimaryCspfDisabled", 25),
          ("srlgPrimaryPathDown", 26),
          ("srlgSecondaryNotDisjoint", 24),
          ("trafficControlSystemError", 3),
          ("tunnelLocallyRepaired", 10),
          ("unknown", 16),
          ("unknownCType", 12),
          ("unknownObjectClass", 11))
    )



class TmnxMplsLabelOwner(Integer32, TextualConvention):
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
        *(("bgp", 5),
          ("ildp", 3),
          ("mirror", 6),
          ("none", 0),
          ("rsvp", 1),
          ("static", 7),
          ("svcmgr", 4),
          ("tldp", 2),
          ("vprn", 8))
    )



class TmnxMplsOperDownReasonCode(Integer32, TextualConvention):
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
        *(("adminDown", 1),
          ("clearDown", 5),
          ("iomFailure", 4),
          ("noResources", 2),
          ("operUp", 0),
          ("systemIpDown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxMplsConformance_ObjectIdentity = ObjectIdentity
tmnxMplsConformance = _TmnxMplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6)
)
_TmnxMplsCompliances_ObjectIdentity = ObjectIdentity
tmnxMplsCompliances = _TmnxMplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1)
)
_TmnxMplsGroups_ObjectIdentity = ObjectIdentity
tmnxMplsGroups = _TmnxMplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2)
)
_TmnxMplsObjs_ObjectIdentity = ObjectIdentity
tmnxMplsObjs = _TmnxMplsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6)
)
_VRtrMplsLspTable_Object = MibTable
vRtrMplsLspTable = _VRtrMplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTable.setStatus("current")
_VRtrMplsLspEntry_Object = MibTableRow
vRtrMplsLspEntry = _VRtrMplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1)
)
vRtrMplsLspEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspEntry.setStatus("current")
_VRtrMplsLspIndex_Type = TmnxVRtrMplsLspID
_VRtrMplsLspIndex_Object = MibTableColumn
vRtrMplsLspIndex = _VRtrMplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 1),
    _VRtrMplsLspIndex_Type()
)
vRtrMplsLspIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspIndex.setStatus("current")
_VRtrMplsLspRowStatus_Type = RowStatus
_VRtrMplsLspRowStatus_Object = MibTableColumn
vRtrMplsLspRowStatus = _VRtrMplsLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 2),
    _VRtrMplsLspRowStatus_Type()
)
vRtrMplsLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRowStatus.setStatus("current")
_VRtrMplsLspLastChange_Type = TimeStamp
_VRtrMplsLspLastChange_Object = MibTableColumn
vRtrMplsLspLastChange = _VRtrMplsLspLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 3),
    _VRtrMplsLspLastChange_Type()
)
vRtrMplsLspLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastChange.setStatus("current")
_VRtrMplsLspName_Type = TNamedItemOrEmpty
_VRtrMplsLspName_Object = MibTableColumn
vRtrMplsLspName = _VRtrMplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 4),
    _VRtrMplsLspName_Type()
)
vRtrMplsLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspName.setStatus("current")


class _VRtrMplsLspAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspAdminState based on TmnxAdminState"""


_VRtrMplsLspAdminState_Object = MibTableColumn
vRtrMplsLspAdminState = _VRtrMplsLspAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 5),
    _VRtrMplsLspAdminState_Type()
)
vRtrMplsLspAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminState.setStatus("current")
_VRtrMplsLspOperState_Type = TmnxOperState
_VRtrMplsLspOperState_Object = MibTableColumn
vRtrMplsLspOperState = _VRtrMplsLspOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 6),
    _VRtrMplsLspOperState_Type()
)
vRtrMplsLspOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperState.setStatus("current")
_VRtrMplsLspFromAddr_Type = IpAddress
_VRtrMplsLspFromAddr_Object = MibTableColumn
vRtrMplsLspFromAddr = _VRtrMplsLspFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 7),
    _VRtrMplsLspFromAddr_Type()
)
vRtrMplsLspFromAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFromAddr.setStatus("current")
_VRtrMplsLspToAddr_Type = IpAddress
_VRtrMplsLspToAddr_Object = MibTableColumn
vRtrMplsLspToAddr = _VRtrMplsLspToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 8),
    _VRtrMplsLspToAddr_Type()
)
vRtrMplsLspToAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspToAddr.setStatus("current")


class _VRtrMplsLspType_Type(Integer32):
    """Custom type vRtrMplsLspType based on Integer32"""
    defaultValue = 2

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
        *(("bypass-only", 4),
          ("dynamic", 2),
          ("static", 3),
          ("unknown", 1))
    )


_VRtrMplsLspType_Type.__name__ = "Integer32"
_VRtrMplsLspType_Object = MibTableColumn
vRtrMplsLspType = _VRtrMplsLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 9),
    _VRtrMplsLspType_Type()
)
vRtrMplsLspType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspType.setStatus("current")


class _VRtrMplsLspOutSegIndx_Type(Integer32):
    """Custom type vRtrMplsLspOutSegIndx based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMplsLspOutSegIndx_Type.__name__ = "Integer32"
_VRtrMplsLspOutSegIndx_Object = MibTableColumn
vRtrMplsLspOutSegIndx = _VRtrMplsLspOutSegIndx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 10),
    _VRtrMplsLspOutSegIndx_Type()
)
vRtrMplsLspOutSegIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspOutSegIndx.setStatus("current")


class _VRtrMplsLspRetryTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspRetryTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_VRtrMplsLspRetryTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspRetryTimer_Object = MibTableColumn
vRtrMplsLspRetryTimer = _VRtrMplsLspRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 11),
    _VRtrMplsLspRetryTimer_Type()
)
vRtrMplsLspRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryTimer.setUnits("seconds")


class _VRtrMplsLspRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspRetryLimit_Object = MibTableColumn
vRtrMplsLspRetryLimit = _VRtrMplsLspRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 12),
    _VRtrMplsLspRetryLimit_Type()
)
vRtrMplsLspRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryLimit.setStatus("current")


class _VRtrMplsLspMetric_Type(Unsigned32):
    """Custom type vRtrMplsLspMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrMplsLspMetric_Type.__name__ = "Unsigned32"
_VRtrMplsLspMetric_Object = MibTableColumn
vRtrMplsLspMetric = _VRtrMplsLspMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 13),
    _VRtrMplsLspMetric_Type()
)
vRtrMplsLspMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspMetric.setStatus("current")


class _VRtrMplsLspDecrementTtl_Type(TruthValue):
    """Custom type vRtrMplsLspDecrementTtl based on TruthValue"""


_VRtrMplsLspDecrementTtl_Object = MibTableColumn
vRtrMplsLspDecrementTtl = _VRtrMplsLspDecrementTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 14),
    _VRtrMplsLspDecrementTtl_Type()
)
vRtrMplsLspDecrementTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspDecrementTtl.setStatus("current")


class _VRtrMplsLspCspf_Type(TruthValue):
    """Custom type vRtrMplsLspCspf based on TruthValue"""


_VRtrMplsLspCspf_Object = MibTableColumn
vRtrMplsLspCspf = _VRtrMplsLspCspf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 15),
    _VRtrMplsLspCspf_Type()
)
vRtrMplsLspCspf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspf.setStatus("current")


class _VRtrMplsLspFastReroute_Type(TruthValue):
    """Custom type vRtrMplsLspFastReroute based on TruthValue"""


_VRtrMplsLspFastReroute_Object = MibTableColumn
vRtrMplsLspFastReroute = _VRtrMplsLspFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 16),
    _VRtrMplsLspFastReroute_Type()
)
vRtrMplsLspFastReroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFastReroute.setStatus("current")


class _VRtrMplsLspFRHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspFRHopLimit based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLspFRHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspFRHopLimit_Object = MibTableColumn
vRtrMplsLspFRHopLimit = _VRtrMplsLspFRHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 17),
    _VRtrMplsLspFRHopLimit_Type()
)
vRtrMplsLspFRHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRHopLimit.setStatus("current")


class _VRtrMplsLspFRBandwidth_Type(Unsigned32):
    """Custom type vRtrMplsLspFRBandwidth based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspFRBandwidth_Object = MibTableColumn
vRtrMplsLspFRBandwidth = _VRtrMplsLspFRBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 18),
    _VRtrMplsLspFRBandwidth_Type()
)
vRtrMplsLspFRBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspFRBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspClassOfService_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsLspClassOfService based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspClassOfService_Object = MibTableColumn
vRtrMplsLspClassOfService = _VRtrMplsLspClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 19),
    _VRtrMplsLspClassOfService_Type()
)
vRtrMplsLspClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspClassOfService.setStatus("current")


class _VRtrMplsLspSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspSetupPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspSetupPriority_Object = MibTableColumn
vRtrMplsLspSetupPriority = _VRtrMplsLspSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 20),
    _VRtrMplsLspSetupPriority_Type()
)
vRtrMplsLspSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSetupPriority.setStatus("current")


class _VRtrMplsLspHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspHoldPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspHoldPriority_Object = MibTableColumn
vRtrMplsLspHoldPriority = _VRtrMplsLspHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 21),
    _VRtrMplsLspHoldPriority_Type()
)
vRtrMplsLspHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldPriority.setStatus("current")


class _VRtrMplsLspRecord_Type(TruthValue):
    """Custom type vRtrMplsLspRecord based on TruthValue"""


_VRtrMplsLspRecord_Object = MibTableColumn
vRtrMplsLspRecord = _VRtrMplsLspRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 22),
    _VRtrMplsLspRecord_Type()
)
vRtrMplsLspRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRecord.setStatus("current")


class _VRtrMplsLspPreference_Type(Unsigned32):
    """Custom type vRtrMplsLspPreference based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsLspPreference_Type.__name__ = "Unsigned32"
_VRtrMplsLspPreference_Object = MibTableColumn
vRtrMplsLspPreference = _VRtrMplsLspPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 23),
    _VRtrMplsLspPreference_Type()
)
vRtrMplsLspPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPreference.setStatus("current")


class _VRtrMplsLspBandwidth_Type(Integer32):
    """Custom type vRtrMplsLspBandwidth based on Integer32"""
    defaultValue = 0


_VRtrMplsLspBandwidth_Object = MibTableColumn
vRtrMplsLspBandwidth = _VRtrMplsLspBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 24),
    _VRtrMplsLspBandwidth_Type()
)
vRtrMplsLspBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspBwProtect_Type(TruthValue):
    """Custom type vRtrMplsLspBwProtect based on TruthValue"""


_VRtrMplsLspBwProtect_Object = MibTableColumn
vRtrMplsLspBwProtect = _VRtrMplsLspBwProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 25),
    _VRtrMplsLspBwProtect_Type()
)
vRtrMplsLspBwProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBwProtect.setStatus("current")


class _VRtrMplsLspHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspHopLimit_Object = MibTableColumn
vRtrMplsLspHopLimit = _VRtrMplsLspHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 26),
    _VRtrMplsLspHopLimit_Type()
)
vRtrMplsLspHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspHopLimit.setStatus("current")


class _VRtrMplsLspNegotiatedMTU_Type(Unsigned32):
    """Custom type vRtrMplsLspNegotiatedMTU based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspNegotiatedMTU_Object = MibTableColumn
vRtrMplsLspNegotiatedMTU = _VRtrMplsLspNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 27),
    _VRtrMplsLspNegotiatedMTU_Type()
)
vRtrMplsLspNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspNegotiatedMTU.setStatus("current")


class _VRtrMplsLspRsvpResvStyle_Type(Integer32):
    """Custom type vRtrMplsLspRsvpResvStyle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ff", 2),
          ("se", 1))
    )


_VRtrMplsLspRsvpResvStyle_Type.__name__ = "Integer32"
_VRtrMplsLspRsvpResvStyle_Object = MibTableColumn
vRtrMplsLspRsvpResvStyle = _VRtrMplsLspRsvpResvStyle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 28),
    _VRtrMplsLspRsvpResvStyle_Type()
)
vRtrMplsLspRsvpResvStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRsvpResvStyle.setStatus("current")


class _VRtrMplsLspRsvpAdspec_Type(TruthValue):
    """Custom type vRtrMplsLspRsvpAdspec based on TruthValue"""


_VRtrMplsLspRsvpAdspec_Object = MibTableColumn
vRtrMplsLspRsvpAdspec = _VRtrMplsLspRsvpAdspec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 29),
    _VRtrMplsLspRsvpAdspec_Type()
)
vRtrMplsLspRsvpAdspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRsvpAdspec.setStatus("current")


class _VRtrMplsLspFRMethod_Type(Integer32):
    """Custom type vRtrMplsLspFRMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("facilityBackup", 2),
          ("oneToOneBackup", 1))
    )


_VRtrMplsLspFRMethod_Type.__name__ = "Integer32"
_VRtrMplsLspFRMethod_Object = MibTableColumn
vRtrMplsLspFRMethod = _VRtrMplsLspFRMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 30),
    _VRtrMplsLspFRMethod_Type()
)
vRtrMplsLspFRMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRMethod.setStatus("current")


class _VRtrMplsLspFRNodeProtect_Type(TruthValue):
    """Custom type vRtrMplsLspFRNodeProtect based on TruthValue"""


_VRtrMplsLspFRNodeProtect_Object = MibTableColumn
vRtrMplsLspFRNodeProtect = _VRtrMplsLspFRNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 31),
    _VRtrMplsLspFRNodeProtect_Type()
)
vRtrMplsLspFRNodeProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRNodeProtect.setStatus("current")


class _VRtrMplsLspAdminGroupInclude_Type(Unsigned32):
    """Custom type vRtrMplsLspAdminGroupInclude based on Unsigned32"""
    defaultHexValue = 0


_VRtrMplsLspAdminGroupInclude_Object = MibTableColumn
vRtrMplsLspAdminGroupInclude = _VRtrMplsLspAdminGroupInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 32),
    _VRtrMplsLspAdminGroupInclude_Type()
)
vRtrMplsLspAdminGroupInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminGroupInclude.setStatus("current")


class _VRtrMplsLspAdminGroupExclude_Type(Unsigned32):
    """Custom type vRtrMplsLspAdminGroupExclude based on Unsigned32"""
    defaultHexValue = 0


_VRtrMplsLspAdminGroupExclude_Object = MibTableColumn
vRtrMplsLspAdminGroupExclude = _VRtrMplsLspAdminGroupExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 33),
    _VRtrMplsLspAdminGroupExclude_Type()
)
vRtrMplsLspAdminGroupExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminGroupExclude.setStatus("current")


class _VRtrMplsLspAdaptive_Type(TruthValue):
    """Custom type vRtrMplsLspAdaptive based on TruthValue"""


_VRtrMplsLspAdaptive_Object = MibTableColumn
vRtrMplsLspAdaptive = _VRtrMplsLspAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 34),
    _VRtrMplsLspAdaptive_Type()
)
vRtrMplsLspAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdaptive.setStatus("current")


class _VRtrMplsLspInheritance_Type(Unsigned32):
    """Custom type vRtrMplsLspInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspInheritance_Object = MibTableColumn
vRtrMplsLspInheritance = _VRtrMplsLspInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 35),
    _VRtrMplsLspInheritance_Type()
)
vRtrMplsLspInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspInheritance.setStatus("current")


class _VRtrMplsLspOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspOptimizeTimer_Object = MibTableColumn
vRtrMplsLspOptimizeTimer = _VRtrMplsLspOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 36),
    _VRtrMplsLspOptimizeTimer_Type()
)
vRtrMplsLspOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspOptimizeTimer.setUnits("seconds")
_VRtrMplsLspOperFastReroute_Type = TruthValue
_VRtrMplsLspOperFastReroute_Object = MibTableColumn
vRtrMplsLspOperFastReroute = _VRtrMplsLspOperFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 37),
    _VRtrMplsLspOperFastReroute_Type()
)
vRtrMplsLspOperFastReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperFastReroute.setStatus("current")


class _VRtrMplsLspFRObject_Type(TruthValue):
    """Custom type vRtrMplsLspFRObject based on TruthValue"""


_VRtrMplsLspFRObject_Object = MibTableColumn
vRtrMplsLspFRObject = _VRtrMplsLspFRObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 38),
    _VRtrMplsLspFRObject_Type()
)
vRtrMplsLspFRObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRObject.setStatus("current")


class _VRtrMplsLspHoldTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspHoldTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsLspHoldTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspHoldTimer_Object = MibTableColumn
vRtrMplsLspHoldTimer = _VRtrMplsLspHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 39),
    _VRtrMplsLspHoldTimer_Type()
)
vRtrMplsLspHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldTimer.setUnits("seconds")


class _VRtrMplsLspCspfTeMetricEnabled_Type(TruthValue):
    """Custom type vRtrMplsLspCspfTeMetricEnabled based on TruthValue"""


_VRtrMplsLspCspfTeMetricEnabled_Object = MibTableColumn
vRtrMplsLspCspfTeMetricEnabled = _VRtrMplsLspCspfTeMetricEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 1, 1, 40),
    _VRtrMplsLspCspfTeMetricEnabled_Type()
)
vRtrMplsLspCspfTeMetricEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspfTeMetricEnabled.setStatus("current")
_VRtrMplsLspStatTable_Object = MibTable
vRtrMplsLspStatTable = _VRtrMplsLspStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatTable.setStatus("current")
_VRtrMplsLspStatEntry_Object = MibTableRow
vRtrMplsLspStatEntry = _VRtrMplsLspStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatEntry.setStatus("current")
_VRtrMplsLspOctets_Type = Counter64
_VRtrMplsLspOctets_Object = MibTableColumn
vRtrMplsLspOctets = _VRtrMplsLspOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 1),
    _VRtrMplsLspOctets_Type()
)
vRtrMplsLspOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOctets.setStatus("current")
_VRtrMplsLspPackets_Type = Counter64
_VRtrMplsLspPackets_Object = MibTableColumn
vRtrMplsLspPackets = _VRtrMplsLspPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 2),
    _VRtrMplsLspPackets_Type()
)
vRtrMplsLspPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPackets.setStatus("current")
_VRtrMplsLspAge_Type = TimeInterval
_VRtrMplsLspAge_Object = MibTableColumn
vRtrMplsLspAge = _VRtrMplsLspAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 3),
    _VRtrMplsLspAge_Type()
)
vRtrMplsLspAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAge.setStatus("current")
_VRtrMplsLspTimeUp_Type = TimeInterval
_VRtrMplsLspTimeUp_Object = MibTableColumn
vRtrMplsLspTimeUp = _VRtrMplsLspTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 4),
    _VRtrMplsLspTimeUp_Type()
)
vRtrMplsLspTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTimeUp.setStatus("current")
_VRtrMplsLspTimeDown_Type = TimeInterval
_VRtrMplsLspTimeDown_Object = MibTableColumn
vRtrMplsLspTimeDown = _VRtrMplsLspTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 5),
    _VRtrMplsLspTimeDown_Type()
)
vRtrMplsLspTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTimeDown.setStatus("current")
_VRtrMplsLspPrimaryTimeUp_Type = TimeInterval
_VRtrMplsLspPrimaryTimeUp_Object = MibTableColumn
vRtrMplsLspPrimaryTimeUp = _VRtrMplsLspPrimaryTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 6),
    _VRtrMplsLspPrimaryTimeUp_Type()
)
vRtrMplsLspPrimaryTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPrimaryTimeUp.setStatus("current")
_VRtrMplsLspTransitions_Type = Counter32
_VRtrMplsLspTransitions_Object = MibTableColumn
vRtrMplsLspTransitions = _VRtrMplsLspTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 7),
    _VRtrMplsLspTransitions_Type()
)
vRtrMplsLspTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTransitions.setStatus("current")
_VRtrMplsLspLastTransition_Type = TimeInterval
_VRtrMplsLspLastTransition_Object = MibTableColumn
vRtrMplsLspLastTransition = _VRtrMplsLspLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 8),
    _VRtrMplsLspLastTransition_Type()
)
vRtrMplsLspLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastTransition.setStatus("current")
_VRtrMplsLspPathChanges_Type = Counter32
_VRtrMplsLspPathChanges_Object = MibTableColumn
vRtrMplsLspPathChanges = _VRtrMplsLspPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 9),
    _VRtrMplsLspPathChanges_Type()
)
vRtrMplsLspPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathChanges.setStatus("current")
_VRtrMplsLspLastPathChange_Type = TimeInterval
_VRtrMplsLspLastPathChange_Object = MibTableColumn
vRtrMplsLspLastPathChange = _VRtrMplsLspLastPathChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 10),
    _VRtrMplsLspLastPathChange_Type()
)
vRtrMplsLspLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastPathChange.setStatus("current")
_VRtrMplsLspConfiguredPaths_Type = Integer32
_VRtrMplsLspConfiguredPaths_Object = MibTableColumn
vRtrMplsLspConfiguredPaths = _VRtrMplsLspConfiguredPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 11),
    _VRtrMplsLspConfiguredPaths_Type()
)
vRtrMplsLspConfiguredPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspConfiguredPaths.setStatus("current")
_VRtrMplsLspStandbyPaths_Type = Integer32
_VRtrMplsLspStandbyPaths_Object = MibTableColumn
vRtrMplsLspStandbyPaths = _VRtrMplsLspStandbyPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 12),
    _VRtrMplsLspStandbyPaths_Type()
)
vRtrMplsLspStandbyPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStandbyPaths.setStatus("current")
_VRtrMplsLspOperationalPaths_Type = Integer32
_VRtrMplsLspOperationalPaths_Object = MibTableColumn
vRtrMplsLspOperationalPaths = _VRtrMplsLspOperationalPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 2, 1, 13),
    _VRtrMplsLspOperationalPaths_Type()
)
vRtrMplsLspOperationalPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperationalPaths.setStatus("current")


class _VRtrMplsLspPathTableSpinlock_Type(TestAndIncr):
    """Custom type vRtrMplsLspPathTableSpinlock based on TestAndIncr"""
    defaultValue = 0


_VRtrMplsLspPathTableSpinlock_Object = MibScalar
vRtrMplsLspPathTableSpinlock = _VRtrMplsLspPathTableSpinlock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 3),
    _VRtrMplsLspPathTableSpinlock_Type()
)
vRtrMplsLspPathTableSpinlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTableSpinlock.setStatus("current")
_VRtrMplsLspPathTable_Object = MibTable
vRtrMplsLspPathTable = _VRtrMplsLspPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathTable.setStatus("current")
_VRtrMplsLspPathEntry_Object = MibTableRow
vRtrMplsLspPathEntry = _VRtrMplsLspPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1)
)
vRtrMplsLspPathEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathEntry.setStatus("current")
_VRtrMplsLspPathRowStatus_Type = RowStatus
_VRtrMplsLspPathRowStatus_Object = MibTableColumn
vRtrMplsLspPathRowStatus = _VRtrMplsLspPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 1),
    _VRtrMplsLspPathRowStatus_Type()
)
vRtrMplsLspPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRowStatus.setStatus("current")
_VRtrMplsLspPathLastChange_Type = TimeStamp
_VRtrMplsLspPathLastChange_Object = MibTableColumn
vRtrMplsLspPathLastChange = _VRtrMplsLspPathLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 2),
    _VRtrMplsLspPathLastChange_Type()
)
vRtrMplsLspPathLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLastChange.setStatus("current")


class _VRtrMplsLspPathType_Type(Integer32):
    """Custom type vRtrMplsLspPathType based on Integer32"""
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
        *(("other", 1),
          ("primary", 2),
          ("secondary", 4),
          ("standby", 3))
    )


_VRtrMplsLspPathType_Type.__name__ = "Integer32"
_VRtrMplsLspPathType_Object = MibTableColumn
vRtrMplsLspPathType = _VRtrMplsLspPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 3),
    _VRtrMplsLspPathType_Type()
)
vRtrMplsLspPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathType.setStatus("current")


class _VRtrMplsLspPathCos_Type(Integer32):
    """Custom type vRtrMplsLspPathCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_VRtrMplsLspPathCos_Type.__name__ = "Integer32"
_VRtrMplsLspPathCos_Object = MibTableColumn
vRtrMplsLspPathCos = _VRtrMplsLspPathCos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 4),
    _VRtrMplsLspPathCos_Type()
)
vRtrMplsLspPathCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCos.setStatus("current")


class _VRtrMplsLspPathProperties_Type(Bits):
    """Custom type vRtrMplsLspPathProperties based on Bits"""
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("cspf", 2),
          ("fast-reroute", 4),
          ("mergeable", 3),
          ("record-route", 0))
    )

_VRtrMplsLspPathProperties_Type.__name__ = "Bits"
_VRtrMplsLspPathProperties_Object = MibTableColumn
vRtrMplsLspPathProperties = _VRtrMplsLspPathProperties_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 5),
    _VRtrMplsLspPathProperties_Type()
)
vRtrMplsLspPathProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathProperties.setStatus("current")


class _VRtrMplsLspPathBandwidth_Type(Integer32):
    """Custom type vRtrMplsLspPathBandwidth based on Integer32"""
    defaultValue = 0


_VRtrMplsLspPathBandwidth_Object = MibTableColumn
vRtrMplsLspPathBandwidth = _VRtrMplsLspPathBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 6),
    _VRtrMplsLspPathBandwidth_Type()
)
vRtrMplsLspPathBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspPathBwProtect_Type(TruthValue):
    """Custom type vRtrMplsLspPathBwProtect based on TruthValue"""


_VRtrMplsLspPathBwProtect_Object = MibTableColumn
vRtrMplsLspPathBwProtect = _VRtrMplsLspPathBwProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 7),
    _VRtrMplsLspPathBwProtect_Type()
)
vRtrMplsLspPathBwProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathBwProtect.setStatus("current")


class _VRtrMplsLspPathState_Type(Integer32):
    """Custom type vRtrMplsLspPathState based on Integer32"""
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
        *(("active", 2),
          ("inactive", 3),
          ("unknown", 1))
    )


_VRtrMplsLspPathState_Type.__name__ = "Integer32"
_VRtrMplsLspPathState_Object = MibTableColumn
vRtrMplsLspPathState = _VRtrMplsLspPathState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 8),
    _VRtrMplsLspPathState_Type()
)
vRtrMplsLspPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathState.setStatus("current")


class _VRtrMplsLspPathPreference_Type(Integer32):
    """Custom type vRtrMplsLspPathPreference based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsLspPathPreference_Type.__name__ = "Integer32"
_VRtrMplsLspPathPreference_Object = MibTableColumn
vRtrMplsLspPathPreference = _VRtrMplsLspPathPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 9),
    _VRtrMplsLspPathPreference_Type()
)
vRtrMplsLspPathPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathPreference.setStatus("current")


class _VRtrMplsLspPathCosSource_Type(TruthValue):
    """Custom type vRtrMplsLspPathCosSource based on TruthValue"""


_VRtrMplsLspPathCosSource_Object = MibTableColumn
vRtrMplsLspPathCosSource = _VRtrMplsLspPathCosSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 10),
    _VRtrMplsLspPathCosSource_Type()
)
vRtrMplsLspPathCosSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCosSource.setStatus("current")


class _VRtrMplsLspPathClassOfService_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsLspPathClassOfService based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspPathClassOfService_Object = MibTableColumn
vRtrMplsLspPathClassOfService = _VRtrMplsLspPathClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 11),
    _VRtrMplsLspPathClassOfService_Type()
)
vRtrMplsLspPathClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathClassOfService.setStatus("current")


class _VRtrMplsLspPathSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspPathSetupPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathSetupPriority_Object = MibTableColumn
vRtrMplsLspPathSetupPriority = _VRtrMplsLspPathSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 12),
    _VRtrMplsLspPathSetupPriority_Type()
)
vRtrMplsLspPathSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSetupPriority.setStatus("current")


class _VRtrMplsLspPathHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspPathHoldPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspPathHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathHoldPriority_Object = MibTableColumn
vRtrMplsLspPathHoldPriority = _VRtrMplsLspPathHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 13),
    _VRtrMplsLspPathHoldPriority_Type()
)
vRtrMplsLspPathHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathHoldPriority.setStatus("current")


class _VRtrMplsLspPathRecord_Type(Integer32):
    """Custom type vRtrMplsLspPathRecord based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRecord", 2),
          ("record", 1))
    )


_VRtrMplsLspPathRecord_Type.__name__ = "Integer32"
_VRtrMplsLspPathRecord_Object = MibTableColumn
vRtrMplsLspPathRecord = _VRtrMplsLspPathRecord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 14),
    _VRtrMplsLspPathRecord_Type()
)
vRtrMplsLspPathRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRecord.setStatus("current")


class _VRtrMplsLspPathHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspPathHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspPathHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathHopLimit_Object = MibTableColumn
vRtrMplsLspPathHopLimit = _VRtrMplsLspPathHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 15),
    _VRtrMplsLspPathHopLimit_Type()
)
vRtrMplsLspPathHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathHopLimit.setStatus("current")


class _VRtrMplsLspPathSharing_Type(TruthValue):
    """Custom type vRtrMplsLspPathSharing based on TruthValue"""


_VRtrMplsLspPathSharing_Object = MibTableColumn
vRtrMplsLspPathSharing = _VRtrMplsLspPathSharing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 16),
    _VRtrMplsLspPathSharing_Type()
)
vRtrMplsLspPathSharing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathSharing.setStatus("current")


class _VRtrMplsLspPathAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspPathAdminState based on TmnxAdminState"""


_VRtrMplsLspPathAdminState_Object = MibTableColumn
vRtrMplsLspPathAdminState = _VRtrMplsLspPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 17),
    _VRtrMplsLspPathAdminState_Type()
)
vRtrMplsLspPathAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdminState.setStatus("current")
_VRtrMplsLspPathOperState_Type = TmnxOperState
_VRtrMplsLspPathOperState_Object = MibTableColumn
vRtrMplsLspPathOperState = _VRtrMplsLspPathOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 18),
    _VRtrMplsLspPathOperState_Type()
)
vRtrMplsLspPathOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperState.setStatus("current")


class _VRtrMplsLspPathInheritance_Type(Unsigned32):
    """Custom type vRtrMplsLspPathInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspPathInheritance_Object = MibTableColumn
vRtrMplsLspPathInheritance = _VRtrMplsLspPathInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 19),
    _VRtrMplsLspPathInheritance_Type()
)
vRtrMplsLspPathInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathInheritance.setStatus("current")
_VRtrMplsLspPathLspId_Type = MplsLSPID
_VRtrMplsLspPathLspId_Object = MibTableColumn
vRtrMplsLspPathLspId = _VRtrMplsLspPathLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 20),
    _VRtrMplsLspPathLspId_Type()
)
vRtrMplsLspPathLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathLspId.setStatus("current")
_VRtrMplsLspPathRetryTimeRemaining_Type = Unsigned32
_VRtrMplsLspPathRetryTimeRemaining_Object = MibTableColumn
vRtrMplsLspPathRetryTimeRemaining = _VRtrMplsLspPathRetryTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 21),
    _VRtrMplsLspPathRetryTimeRemaining_Type()
)
vRtrMplsLspPathRetryTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRetryTimeRemaining.setStatus("current")


class _VRtrMplsLspPathTunnelARHopListIndex_Type(Integer32):
    """Custom type vRtrMplsLspPathTunnelARHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsLspPathTunnelARHopListIndex_Type.__name__ = "Integer32"
_VRtrMplsLspPathTunnelARHopListIndex_Object = MibTableColumn
vRtrMplsLspPathTunnelARHopListIndex = _VRtrMplsLspPathTunnelARHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 22),
    _VRtrMplsLspPathTunnelARHopListIndex_Type()
)
vRtrMplsLspPathTunnelARHopListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTunnelARHopListIndex.setStatus("current")


class _VRtrMplsLspPathNegotiatedMTU_Type(Unsigned32):
    """Custom type vRtrMplsLspPathNegotiatedMTU based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspPathNegotiatedMTU_Object = MibTableColumn
vRtrMplsLspPathNegotiatedMTU = _VRtrMplsLspPathNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 23),
    _VRtrMplsLspPathNegotiatedMTU_Type()
)
vRtrMplsLspPathNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNegotiatedMTU.setStatus("current")
_VRtrMplsLspPathFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathFailCode_Object = MibTableColumn
vRtrMplsLspPathFailCode = _VRtrMplsLspPathFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 24),
    _VRtrMplsLspPathFailCode_Type()
)
vRtrMplsLspPathFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathFailCode.setStatus("current")
_VRtrMplsLspPathFailNodeAddr_Type = IpAddress
_VRtrMplsLspPathFailNodeAddr_Object = MibTableColumn
vRtrMplsLspPathFailNodeAddr = _VRtrMplsLspPathFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 25),
    _VRtrMplsLspPathFailNodeAddr_Type()
)
vRtrMplsLspPathFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathFailNodeAddr.setStatus("current")


class _VRtrMplsLspPathAdminGroupInclude_Type(Unsigned32):
    """Custom type vRtrMplsLspPathAdminGroupInclude based on Unsigned32"""
    defaultHexValue = 0


_VRtrMplsLspPathAdminGroupInclude_Object = MibTableColumn
vRtrMplsLspPathAdminGroupInclude = _VRtrMplsLspPathAdminGroupInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 26),
    _VRtrMplsLspPathAdminGroupInclude_Type()
)
vRtrMplsLspPathAdminGroupInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdminGroupInclude.setStatus("current")


class _VRtrMplsLspPathAdminGroupExclude_Type(Unsigned32):
    """Custom type vRtrMplsLspPathAdminGroupExclude based on Unsigned32"""
    defaultHexValue = 0


_VRtrMplsLspPathAdminGroupExclude_Object = MibTableColumn
vRtrMplsLspPathAdminGroupExclude = _VRtrMplsLspPathAdminGroupExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 27),
    _VRtrMplsLspPathAdminGroupExclude_Type()
)
vRtrMplsLspPathAdminGroupExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdminGroupExclude.setStatus("current")


class _VRtrMplsLspPathAdaptive_Type(TruthValue):
    """Custom type vRtrMplsLspPathAdaptive based on TruthValue"""


_VRtrMplsLspPathAdaptive_Object = MibTableColumn
vRtrMplsLspPathAdaptive = _VRtrMplsLspPathAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 28),
    _VRtrMplsLspPathAdaptive_Type()
)
vRtrMplsLspPathAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathAdaptive.setStatus("current")


class _VRtrMplsLspPathOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspPathOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspPathOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathOptimizeTimer_Object = MibTableColumn
vRtrMplsLspPathOptimizeTimer = _VRtrMplsLspPathOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 29),
    _VRtrMplsLspPathOptimizeTimer_Type()
)
vRtrMplsLspPathOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOptimizeTimer.setUnits("seconds")


class _VRtrMplsLspPathNextOptimize_Type(Unsigned32):
    """Custom type vRtrMplsLspPathNextOptimize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspPathNextOptimize_Type.__name__ = "Unsigned32"
_VRtrMplsLspPathNextOptimize_Object = MibTableColumn
vRtrMplsLspPathNextOptimize = _VRtrMplsLspPathNextOptimize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 30),
    _VRtrMplsLspPathNextOptimize_Type()
)
vRtrMplsLspPathNextOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNextOptimize.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNextOptimize.setUnits("seconds")
_VRtrMplsLspPathOperBandwidth_Type = Integer32
_VRtrMplsLspPathOperBandwidth_Object = MibTableColumn
vRtrMplsLspPathOperBandwidth = _VRtrMplsLspPathOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 31),
    _VRtrMplsLspPathOperBandwidth_Type()
)
vRtrMplsLspPathOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspPathMBBState_Type(Integer32):
    """Custom type vRtrMplsLspPathMBBState based on Integer32"""
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
        *(("fail", 4),
          ("inProgress", 3),
          ("none", 1),
          ("success", 2))
    )


_VRtrMplsLspPathMBBState_Type.__name__ = "Integer32"
_VRtrMplsLspPathMBBState_Object = MibTableColumn
vRtrMplsLspPathMBBState = _VRtrMplsLspPathMBBState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 32),
    _VRtrMplsLspPathMBBState_Type()
)
vRtrMplsLspPathMBBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathMBBState.setStatus("current")
_VRtrMplsLspPathResignal_Type = TmnxActionType
_VRtrMplsLspPathResignal_Object = MibTableColumn
vRtrMplsLspPathResignal = _VRtrMplsLspPathResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 33),
    _VRtrMplsLspPathResignal_Type()
)
vRtrMplsLspPathResignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathResignal.setStatus("current")


class _VRtrMplsLspPathTunnelCRHopListIndex_Type(Integer32):
    """Custom type vRtrMplsLspPathTunnelCRHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsLspPathTunnelCRHopListIndex_Type.__name__ = "Integer32"
_VRtrMplsLspPathTunnelCRHopListIndex_Object = MibTableColumn
vRtrMplsLspPathTunnelCRHopListIndex = _VRtrMplsLspPathTunnelCRHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 34),
    _VRtrMplsLspPathTunnelCRHopListIndex_Type()
)
vRtrMplsLspPathTunnelCRHopListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTunnelCRHopListIndex.setStatus("current")
_VRtrMplsLspPathOperMTU_Type = Unsigned32
_VRtrMplsLspPathOperMTU_Object = MibTableColumn
vRtrMplsLspPathOperMTU = _VRtrMplsLspPathOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 35),
    _VRtrMplsLspPathOperMTU_Type()
)
vRtrMplsLspPathOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathOperMTU.setStatus("current")


class _VRtrMplsLspPathRecordLabel_Type(Integer32):
    """Custom type vRtrMplsLspPathRecordLabel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRecord", 2),
          ("record", 1))
    )


_VRtrMplsLspPathRecordLabel_Type.__name__ = "Integer32"
_VRtrMplsLspPathRecordLabel_Object = MibTableColumn
vRtrMplsLspPathRecordLabel = _VRtrMplsLspPathRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 4, 1, 36),
    _VRtrMplsLspPathRecordLabel_Type()
)
vRtrMplsLspPathRecordLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRecordLabel.setStatus("current")
_VRtrMplsLspPathStatTable_Object = MibTable
vRtrMplsLspPathStatTable = _VRtrMplsLspPathStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathStatTable.setStatus("current")
_VRtrMplsLspPathStatEntry_Object = MibTableRow
vRtrMplsLspPathStatEntry = _VRtrMplsLspPathStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathStatEntry.setStatus("current")
_VRtrMplsLspPathTimeUp_Type = TimeInterval
_VRtrMplsLspPathTimeUp_Object = MibTableColumn
vRtrMplsLspPathTimeUp = _VRtrMplsLspPathTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 1),
    _VRtrMplsLspPathTimeUp_Type()
)
vRtrMplsLspPathTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTimeUp.setStatus("current")
_VRtrMplsLspPathTimeDown_Type = TimeInterval
_VRtrMplsLspPathTimeDown_Object = MibTableColumn
vRtrMplsLspPathTimeDown = _VRtrMplsLspPathTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 2),
    _VRtrMplsLspPathTimeDown_Type()
)
vRtrMplsLspPathTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTimeDown.setStatus("current")
_VRtrMplsLspPathRetryAttempts_Type = Unsigned32
_VRtrMplsLspPathRetryAttempts_Object = MibTableColumn
vRtrMplsLspPathRetryAttempts = _VRtrMplsLspPathRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 3),
    _VRtrMplsLspPathRetryAttempts_Type()
)
vRtrMplsLspPathRetryAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathRetryAttempts.setStatus("current")
_VRtrMplsLspPathTransitionCount_Type = Counter32
_VRtrMplsLspPathTransitionCount_Object = MibTableColumn
vRtrMplsLspPathTransitionCount = _VRtrMplsLspPathTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 4),
    _VRtrMplsLspPathTransitionCount_Type()
)
vRtrMplsLspPathTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathTransitionCount.setStatus("current")
_VRtrMplsLspPathCspfQueries_Type = Counter32
_VRtrMplsLspPathCspfQueries_Object = MibTableColumn
vRtrMplsLspPathCspfQueries = _VRtrMplsLspPathCspfQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 5, 1, 5),
    _VRtrMplsLspPathCspfQueries_Type()
)
vRtrMplsLspPathCspfQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathCspfQueries.setStatus("current")
_VRtrMplsXCTable_Object = MibTable
vRtrMplsXCTable = _VRtrMplsXCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    vRtrMplsXCTable.setStatus("current")
_VRtrMplsXCEntry_Object = MibTableRow
vRtrMplsXCEntry = _VRtrMplsXCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1)
)
vRtrMplsXCEntry.setIndexNames(
    (0, "MPLS-LSR-MIB", "mplsXCLspId"),
)
if mibBuilder.loadTexts:
    vRtrMplsXCEntry.setStatus("current")


class _VRtrMplsXCIndex_Type(Integer32):
    """Custom type vRtrMplsXCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsXCIndex_Type.__name__ = "Integer32"
_VRtrMplsXCIndex_Object = MibTableColumn
vRtrMplsXCIndex = _VRtrMplsXCIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 1),
    _VRtrMplsXCIndex_Type()
)
vRtrMplsXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsXCIndex.setStatus("current")
_VRtrMplsInSegmentIfIndex_Type = InterfaceIndexOrZero
_VRtrMplsInSegmentIfIndex_Object = MibTableColumn
vRtrMplsInSegmentIfIndex = _VRtrMplsInSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 2),
    _VRtrMplsInSegmentIfIndex_Type()
)
vRtrMplsInSegmentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInSegmentIfIndex.setStatus("current")
_VRtrMplsInSegmentLabel_Type = MplsLabel
_VRtrMplsInSegmentLabel_Object = MibTableColumn
vRtrMplsInSegmentLabel = _VRtrMplsInSegmentLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 3),
    _VRtrMplsInSegmentLabel_Type()
)
vRtrMplsInSegmentLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsInSegmentLabel.setStatus("current")


class _VRtrMplsOutSegmentIndex_Type(Integer32):
    """Custom type vRtrMplsOutSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMplsOutSegmentIndex_Type.__name__ = "Integer32"
_VRtrMplsOutSegmentIndex_Object = MibTableColumn
vRtrMplsOutSegmentIndex = _VRtrMplsOutSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 4),
    _VRtrMplsOutSegmentIndex_Type()
)
vRtrMplsOutSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsOutSegmentIndex.setStatus("current")
_VRtrMplsERHopTunnelIndex_Type = Integer32
_VRtrMplsERHopTunnelIndex_Object = MibTableColumn
vRtrMplsERHopTunnelIndex = _VRtrMplsERHopTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 5),
    _VRtrMplsERHopTunnelIndex_Type()
)
vRtrMplsERHopTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsERHopTunnelIndex.setStatus("current")
_VRtrMplsARHopTunnelIndex_Type = Integer32
_VRtrMplsARHopTunnelIndex_Object = MibTableColumn
vRtrMplsARHopTunnelIndex = _VRtrMplsARHopTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 6),
    _VRtrMplsARHopTunnelIndex_Type()
)
vRtrMplsARHopTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsARHopTunnelIndex.setStatus("current")
_VRtrMplsRsvpSessionIndex_Type = Unsigned32
_VRtrMplsRsvpSessionIndex_Object = MibTableColumn
vRtrMplsRsvpSessionIndex = _VRtrMplsRsvpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 7),
    _VRtrMplsRsvpSessionIndex_Type()
)
vRtrMplsRsvpSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsRsvpSessionIndex.setStatus("current")
_VRtrMplsXCFailCode_Type = TmnxMplsLspFailCode
_VRtrMplsXCFailCode_Object = MibTableColumn
vRtrMplsXCFailCode = _VRtrMplsXCFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 8),
    _VRtrMplsXCFailCode_Type()
)
vRtrMplsXCFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsXCFailCode.setStatus("current")
_VRtrMplsXCCHopTableIndex_Type = Integer32
_VRtrMplsXCCHopTableIndex_Object = MibTableColumn
vRtrMplsXCCHopTableIndex = _VRtrMplsXCCHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 6, 1, 9),
    _VRtrMplsXCCHopTableIndex_Type()
)
vRtrMplsXCCHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsXCCHopTableIndex.setStatus("current")
_VRtrMplsGeneralTable_Object = MibTable
vRtrMplsGeneralTable = _VRtrMplsGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7)
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralTable.setStatus("current")
_VRtrMplsGeneralEntry_Object = MibTableRow
vRtrMplsGeneralEntry = _VRtrMplsGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1)
)
vRtrMplsGeneralEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralEntry.setStatus("current")
_VRtrMplsGeneralLastChange_Type = TimeStamp
_VRtrMplsGeneralLastChange_Object = MibTableColumn
vRtrMplsGeneralLastChange = _VRtrMplsGeneralLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 1),
    _VRtrMplsGeneralLastChange_Type()
)
vRtrMplsGeneralLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLastChange.setStatus("current")


class _VRtrMplsGeneralAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsGeneralAdminState based on TmnxAdminState"""


_VRtrMplsGeneralAdminState_Object = MibTableColumn
vRtrMplsGeneralAdminState = _VRtrMplsGeneralAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 2),
    _VRtrMplsGeneralAdminState_Type()
)
vRtrMplsGeneralAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAdminState.setStatus("current")
_VRtrMplsGeneralOperState_Type = TmnxOperState
_VRtrMplsGeneralOperState_Object = MibTableColumn
vRtrMplsGeneralOperState = _VRtrMplsGeneralOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 3),
    _VRtrMplsGeneralOperState_Type()
)
vRtrMplsGeneralOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOperState.setStatus("current")


class _VRtrMplsGeneralPropagateTtl_Type(TruthValue):
    """Custom type vRtrMplsGeneralPropagateTtl based on TruthValue"""


_VRtrMplsGeneralPropagateTtl_Object = MibTableColumn
vRtrMplsGeneralPropagateTtl = _VRtrMplsGeneralPropagateTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 4),
    _VRtrMplsGeneralPropagateTtl_Type()
)
vRtrMplsGeneralPropagateTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralPropagateTtl.setStatus("current")


class _VRtrMplsGeneralTE_Type(Integer32):
    """Custom type vRtrMplsGeneralTE based on Integer32"""
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
        *(("bgp", 2),
          ("bgpigp", 3),
          ("none", 1))
    )


_VRtrMplsGeneralTE_Type.__name__ = "Integer32"
_VRtrMplsGeneralTE_Object = MibTableColumn
vRtrMplsGeneralTE = _VRtrMplsGeneralTE_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 5),
    _VRtrMplsGeneralTE_Type()
)
vRtrMplsGeneralTE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralTE.setStatus("current")
_VRtrMplsGeneralNewLspIndex_Type = TestAndIncr
_VRtrMplsGeneralNewLspIndex_Object = MibTableColumn
vRtrMplsGeneralNewLspIndex = _VRtrMplsGeneralNewLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 6),
    _VRtrMplsGeneralNewLspIndex_Type()
)
vRtrMplsGeneralNewLspIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNewLspIndex.setStatus("current")


class _VRtrMplsGeneralOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsGeneralOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralOptimizeTimer_Object = MibTableColumn
vRtrMplsGeneralOptimizeTimer = _VRtrMplsGeneralOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 7),
    _VRtrMplsGeneralOptimizeTimer_Type()
)
vRtrMplsGeneralOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOptimizeTimer.setUnits("seconds")


class _VRtrMplsGeneralFRObject_Type(TruthValue):
    """Custom type vRtrMplsGeneralFRObject based on TruthValue"""


_VRtrMplsGeneralFRObject_Object = MibTableColumn
vRtrMplsGeneralFRObject = _VRtrMplsGeneralFRObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 8),
    _VRtrMplsGeneralFRObject_Type()
)
vRtrMplsGeneralFRObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralFRObject.setStatus("current")


class _VRtrMplsGeneralResignalTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralResignalTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 10080),
    )


_VRtrMplsGeneralResignalTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralResignalTimer_Object = MibTableColumn
vRtrMplsGeneralResignalTimer = _VRtrMplsGeneralResignalTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 9),
    _VRtrMplsGeneralResignalTimer_Type()
)
vRtrMplsGeneralResignalTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralResignalTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralResignalTimer.setUnits("minutes")


class _VRtrMplsGeneralHoldTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralHoldTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGeneralHoldTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralHoldTimer_Object = MibTableColumn
vRtrMplsGeneralHoldTimer = _VRtrMplsGeneralHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 10),
    _VRtrMplsGeneralHoldTimer_Type()
)
vRtrMplsGeneralHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralHoldTimer.setUnits("seconds")


class _VRtrMplsGeneralDynamicBypass_Type(TruthValue):
    """Custom type vRtrMplsGeneralDynamicBypass based on TruthValue"""


_VRtrMplsGeneralDynamicBypass_Object = MibTableColumn
vRtrMplsGeneralDynamicBypass = _VRtrMplsGeneralDynamicBypass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 11),
    _VRtrMplsGeneralDynamicBypass_Type()
)
vRtrMplsGeneralDynamicBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicBypass.setStatus("current")
_VRtrMplsGeneralNextResignal_Type = Unsigned32
_VRtrMplsGeneralNextResignal_Object = MibTableColumn
vRtrMplsGeneralNextResignal = _VRtrMplsGeneralNextResignal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 12),
    _VRtrMplsGeneralNextResignal_Type()
)
vRtrMplsGeneralNextResignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNextResignal.setStatus("current")
_VRtrMplsGeneralOperDownReason_Type = TmnxMplsOperDownReasonCode
_VRtrMplsGeneralOperDownReason_Object = MibTableColumn
vRtrMplsGeneralOperDownReason = _VRtrMplsGeneralOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 13),
    _VRtrMplsGeneralOperDownReason_Type()
)
vRtrMplsGeneralOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOperDownReason.setStatus("current")


class _VRtrMplsGeneralSrlgFrr_Type(TruthValue):
    """Custom type vRtrMplsGeneralSrlgFrr based on TruthValue"""


_VRtrMplsGeneralSrlgFrr_Object = MibTableColumn
vRtrMplsGeneralSrlgFrr = _VRtrMplsGeneralSrlgFrr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 14),
    _VRtrMplsGeneralSrlgFrr_Type()
)
vRtrMplsGeneralSrlgFrr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSrlgFrr.setStatus("current")


class _VRtrMplsGeneralSrlgFrrStrict_Type(TruthValue):
    """Custom type vRtrMplsGeneralSrlgFrrStrict based on TruthValue"""


_VRtrMplsGeneralSrlgFrrStrict_Object = MibTableColumn
vRtrMplsGeneralSrlgFrrStrict = _VRtrMplsGeneralSrlgFrrStrict_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 7, 1, 15),
    _VRtrMplsGeneralSrlgFrrStrict_Type()
)
vRtrMplsGeneralSrlgFrrStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSrlgFrrStrict.setStatus("current")
_VRtrMplsGeneralStatTable_Object = MibTable
vRtrMplsGeneralStatTable = _VRtrMplsGeneralStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8)
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralStatTable.setStatus("current")
_VRtrMplsGeneralStatEntry_Object = MibTableRow
vRtrMplsGeneralStatEntry = _VRtrMplsGeneralStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralStatEntry.setStatus("current")
_VRtrMplsGeneralStaticLspOriginate_Type = Counter32
_VRtrMplsGeneralStaticLspOriginate_Object = MibTableColumn
vRtrMplsGeneralStaticLspOriginate = _VRtrMplsGeneralStaticLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 1),
    _VRtrMplsGeneralStaticLspOriginate_Type()
)
vRtrMplsGeneralStaticLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspOriginate.setStatus("current")
_VRtrMplsGeneralStaticLspTransit_Type = Counter32
_VRtrMplsGeneralStaticLspTransit_Object = MibTableColumn
vRtrMplsGeneralStaticLspTransit = _VRtrMplsGeneralStaticLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 2),
    _VRtrMplsGeneralStaticLspTransit_Type()
)
vRtrMplsGeneralStaticLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspTransit.setStatus("current")
_VRtrMplsGeneralStaticLspTerminate_Type = Counter32
_VRtrMplsGeneralStaticLspTerminate_Object = MibTableColumn
vRtrMplsGeneralStaticLspTerminate = _VRtrMplsGeneralStaticLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 3),
    _VRtrMplsGeneralStaticLspTerminate_Type()
)
vRtrMplsGeneralStaticLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspTerminate.setStatus("current")
_VRtrMplsGeneralDynamicLspOriginate_Type = Counter32
_VRtrMplsGeneralDynamicLspOriginate_Object = MibTableColumn
vRtrMplsGeneralDynamicLspOriginate = _VRtrMplsGeneralDynamicLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 4),
    _VRtrMplsGeneralDynamicLspOriginate_Type()
)
vRtrMplsGeneralDynamicLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicLspOriginate.setStatus("current")
_VRtrMplsGeneralDynamicLspTransit_Type = Counter32
_VRtrMplsGeneralDynamicLspTransit_Object = MibTableColumn
vRtrMplsGeneralDynamicLspTransit = _VRtrMplsGeneralDynamicLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 5),
    _VRtrMplsGeneralDynamicLspTransit_Type()
)
vRtrMplsGeneralDynamicLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicLspTransit.setStatus("current")
_VRtrMplsGeneralDynamicLspTerminate_Type = Counter32
_VRtrMplsGeneralDynamicLspTerminate_Object = MibTableColumn
vRtrMplsGeneralDynamicLspTerminate = _VRtrMplsGeneralDynamicLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 6),
    _VRtrMplsGeneralDynamicLspTerminate_Type()
)
vRtrMplsGeneralDynamicLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicLspTerminate.setStatus("current")
_VRtrMplsGeneralDetourLspOriginate_Type = Counter32
_VRtrMplsGeneralDetourLspOriginate_Object = MibTableColumn
vRtrMplsGeneralDetourLspOriginate = _VRtrMplsGeneralDetourLspOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 7),
    _VRtrMplsGeneralDetourLspOriginate_Type()
)
vRtrMplsGeneralDetourLspOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDetourLspOriginate.setStatus("current")
_VRtrMplsGeneralDetourLspTransit_Type = Counter32
_VRtrMplsGeneralDetourLspTransit_Object = MibTableColumn
vRtrMplsGeneralDetourLspTransit = _VRtrMplsGeneralDetourLspTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 8),
    _VRtrMplsGeneralDetourLspTransit_Type()
)
vRtrMplsGeneralDetourLspTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDetourLspTransit.setStatus("current")
_VRtrMplsGeneralDetourLspTerminate_Type = Counter32
_VRtrMplsGeneralDetourLspTerminate_Object = MibTableColumn
vRtrMplsGeneralDetourLspTerminate = _VRtrMplsGeneralDetourLspTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 8, 1, 9),
    _VRtrMplsGeneralDetourLspTerminate_Type()
)
vRtrMplsGeneralDetourLspTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDetourLspTerminate.setStatus("current")
_VRtrMplsIfTable_Object = MibTable
vRtrMplsIfTable = _VRtrMplsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9)
)
if mibBuilder.loadTexts:
    vRtrMplsIfTable.setStatus("current")
_VRtrMplsIfEntry_Object = MibTableRow
vRtrMplsIfEntry = _VRtrMplsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1)
)
vRtrMplsIfEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsIfEntry.setStatus("current")


class _VRtrMplsIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsIfAdminState based on TmnxAdminState"""


_VRtrMplsIfAdminState_Object = MibTableColumn
vRtrMplsIfAdminState = _VRtrMplsIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 1),
    _VRtrMplsIfAdminState_Type()
)
vRtrMplsIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfAdminState.setStatus("current")
_VRtrMplsIfOperState_Type = TmnxOperState
_VRtrMplsIfOperState_Object = MibTableColumn
vRtrMplsIfOperState = _VRtrMplsIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 2),
    _VRtrMplsIfOperState_Type()
)
vRtrMplsIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfOperState.setStatus("current")


class _VRtrMplsIfAdminGroup_Type(Unsigned32):
    """Custom type vRtrMplsIfAdminGroup based on Unsigned32"""
    defaultHexValue = 0


_VRtrMplsIfAdminGroup_Object = MibTableColumn
vRtrMplsIfAdminGroup = _VRtrMplsIfAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 3),
    _VRtrMplsIfAdminGroup_Type()
)
vRtrMplsIfAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfAdminGroup.setStatus("current")


class _VRtrMplsIfTeMetric_Type(Unsigned32):
    """Custom type vRtrMplsIfTeMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777215),
    )


_VRtrMplsIfTeMetric_Type.__name__ = "Unsigned32"
_VRtrMplsIfTeMetric_Object = MibTableColumn
vRtrMplsIfTeMetric = _VRtrMplsIfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 9, 1, 4),
    _VRtrMplsIfTeMetric_Type()
)
vRtrMplsIfTeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfTeMetric.setStatus("current")
_VRtrMplsIfStatTable_Object = MibTable
vRtrMplsIfStatTable = _VRtrMplsIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10)
)
if mibBuilder.loadTexts:
    vRtrMplsIfStatTable.setStatus("current")
_VRtrMplsIfStatEntry_Object = MibTableRow
vRtrMplsIfStatEntry = _VRtrMplsIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsIfStatEntry.setStatus("current")
_VRtrMplsIfTxPktCount_Type = Counter64
_VRtrMplsIfTxPktCount_Object = MibTableColumn
vRtrMplsIfTxPktCount = _VRtrMplsIfTxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 1),
    _VRtrMplsIfTxPktCount_Type()
)
vRtrMplsIfTxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfTxPktCount.setStatus("current")
_VRtrMplsIfRxPktCount_Type = Counter64
_VRtrMplsIfRxPktCount_Object = MibTableColumn
vRtrMplsIfRxPktCount = _VRtrMplsIfRxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 2),
    _VRtrMplsIfRxPktCount_Type()
)
vRtrMplsIfRxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfRxPktCount.setStatus("current")
_VRtrMplsIfTxOctetCount_Type = Counter64
_VRtrMplsIfTxOctetCount_Object = MibTableColumn
vRtrMplsIfTxOctetCount = _VRtrMplsIfTxOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 3),
    _VRtrMplsIfTxOctetCount_Type()
)
vRtrMplsIfTxOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfTxOctetCount.setStatus("current")
_VRtrMplsIfRxOctetCount_Type = Counter64
_VRtrMplsIfRxOctetCount_Object = MibTableColumn
vRtrMplsIfRxOctetCount = _VRtrMplsIfRxOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 10, 1, 4),
    _VRtrMplsIfRxOctetCount_Type()
)
vRtrMplsIfRxOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfRxOctetCount.setStatus("current")
_VRtrMplsTunnelARHopTable_Object = MibTable
vRtrMplsTunnelARHopTable = _VRtrMplsTunnelARHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11)
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopTable.setStatus("current")
_VRtrMplsTunnelARHopEntry_Object = MibTableRow
vRtrMplsTunnelARHopEntry = _VRtrMplsTunnelARHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopEntry.setStatus("current")


class _VRtrMplsTunnelARHopProtection_Type(Bits):
    """Custom type vRtrMplsTunnelARHopProtection based on Bits"""
    namedValues = NamedValues(
        *(("bandwidthProtected", 2),
          ("localAvailable", 0),
          ("localInUse", 1),
          ("nodeProtected", 3))
    )

_VRtrMplsTunnelARHopProtection_Type.__name__ = "Bits"
_VRtrMplsTunnelARHopProtection_Object = MibTableColumn
vRtrMplsTunnelARHopProtection = _VRtrMplsTunnelARHopProtection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 1),
    _VRtrMplsTunnelARHopProtection_Type()
)
vRtrMplsTunnelARHopProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopProtection.setStatus("current")
_VRtrMplsTunnelARHopRecordLabel_Type = MplsLabel
_VRtrMplsTunnelARHopRecordLabel_Object = MibTableColumn
vRtrMplsTunnelARHopRecordLabel = _VRtrMplsTunnelARHopRecordLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 2),
    _VRtrMplsTunnelARHopRecordLabel_Type()
)
vRtrMplsTunnelARHopRecordLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopRecordLabel.setStatus("current")
_VRtrMplsTunnelARHopRouterId_Type = IpAddress
_VRtrMplsTunnelARHopRouterId_Object = MibTableColumn
vRtrMplsTunnelARHopRouterId = _VRtrMplsTunnelARHopRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 11, 1, 3),
    _VRtrMplsTunnelARHopRouterId_Type()
)
vRtrMplsTunnelARHopRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelARHopRouterId.setStatus("current")
_VRtrMplsTunnelCHopTable_Object = MibTable
vRtrMplsTunnelCHopTable = _VRtrMplsTunnelCHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12)
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopTable.setStatus("current")
_VRtrMplsTunnelCHopEntry_Object = MibTableRow
vRtrMplsTunnelCHopEntry = _VRtrMplsTunnelCHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1)
)
vRtrMplsTunnelCHopEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopListIndex"),
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopEntry.setStatus("current")


class _VRtrMplsTunnelCHopListIndex_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsTunnelCHopListIndex_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopListIndex_Object = MibTableColumn
vRtrMplsTunnelCHopListIndex = _VRtrMplsTunnelCHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 1),
    _VRtrMplsTunnelCHopListIndex_Type()
)
vRtrMplsTunnelCHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopListIndex.setStatus("current")


class _VRtrMplsTunnelCHopIndex_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrMplsTunnelCHopIndex_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopIndex_Object = MibTableColumn
vRtrMplsTunnelCHopIndex = _VRtrMplsTunnelCHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 2),
    _VRtrMplsTunnelCHopIndex_Type()
)
vRtrMplsTunnelCHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIndex.setStatus("current")


class _VRtrMplsTunnelCHopAddrType_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopAddrType based on Integer32"""
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
        *(("asNumber", 3),
          ("ipV4", 1),
          ("ipV6", 2),
          ("lspid", 4))
    )


_VRtrMplsTunnelCHopAddrType_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopAddrType_Object = MibTableColumn
vRtrMplsTunnelCHopAddrType = _VRtrMplsTunnelCHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 3),
    _VRtrMplsTunnelCHopAddrType_Type()
)
vRtrMplsTunnelCHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopAddrType.setStatus("current")
_VRtrMplsTunnelCHopIpv4Addr_Type = IpAddress
_VRtrMplsTunnelCHopIpv4Addr_Object = MibTableColumn
vRtrMplsTunnelCHopIpv4Addr = _VRtrMplsTunnelCHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 4),
    _VRtrMplsTunnelCHopIpv4Addr_Type()
)
vRtrMplsTunnelCHopIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv4Addr.setStatus("current")


class _VRtrMplsTunnelCHopIpv4PrefixLen_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopIpv4PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VRtrMplsTunnelCHopIpv4PrefixLen_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopIpv4PrefixLen_Object = MibTableColumn
vRtrMplsTunnelCHopIpv4PrefixLen = _VRtrMplsTunnelCHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 5),
    _VRtrMplsTunnelCHopIpv4PrefixLen_Type()
)
vRtrMplsTunnelCHopIpv4PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv4PrefixLen.setStatus("current")
_VRtrMplsTunnelCHopIpv6Addr_Type = InetAddressIPv6
_VRtrMplsTunnelCHopIpv6Addr_Object = MibTableColumn
vRtrMplsTunnelCHopIpv6Addr = _VRtrMplsTunnelCHopIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 6),
    _VRtrMplsTunnelCHopIpv6Addr_Type()
)
vRtrMplsTunnelCHopIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv6Addr.setStatus("current")


class _VRtrMplsTunnelCHopIpv6PrefixLen_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VRtrMplsTunnelCHopIpv6PrefixLen_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopIpv6PrefixLen_Object = MibTableColumn
vRtrMplsTunnelCHopIpv6PrefixLen = _VRtrMplsTunnelCHopIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 7),
    _VRtrMplsTunnelCHopIpv6PrefixLen_Type()
)
vRtrMplsTunnelCHopIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopIpv6PrefixLen.setStatus("current")


class _VRtrMplsTunnelCHopAsNumber_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopAsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsTunnelCHopAsNumber_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopAsNumber_Object = MibTableColumn
vRtrMplsTunnelCHopAsNumber = _VRtrMplsTunnelCHopAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 8),
    _VRtrMplsTunnelCHopAsNumber_Type()
)
vRtrMplsTunnelCHopAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopAsNumber.setStatus("current")
_VRtrMplsTunnelCHopLspId_Type = MplsLSPID
_VRtrMplsTunnelCHopLspId_Object = MibTableColumn
vRtrMplsTunnelCHopLspId = _VRtrMplsTunnelCHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 9),
    _VRtrMplsTunnelCHopLspId_Type()
)
vRtrMplsTunnelCHopLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopLspId.setStatus("current")


class _VRtrMplsTunnelCHopStrictOrLoose_Type(Integer32):
    """Custom type vRtrMplsTunnelCHopStrictOrLoose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )


_VRtrMplsTunnelCHopStrictOrLoose_Type.__name__ = "Integer32"
_VRtrMplsTunnelCHopStrictOrLoose_Object = MibTableColumn
vRtrMplsTunnelCHopStrictOrLoose = _VRtrMplsTunnelCHopStrictOrLoose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 12, 1, 10),
    _VRtrMplsTunnelCHopStrictOrLoose_Type()
)
vRtrMplsTunnelCHopStrictOrLoose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTunnelCHopStrictOrLoose.setStatus("current")
_VRtrMplsAdminGroupTable_Object = MibTable
vRtrMplsAdminGroupTable = _VRtrMplsAdminGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13)
)
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupTable.setStatus("current")
_VRtrMplsAdminGroupEntry_Object = MibTableRow
vRtrMplsAdminGroupEntry = _VRtrMplsAdminGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1)
)
vRtrMplsAdminGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupName"),
)
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupEntry.setStatus("current")
_VRtrMplsAdminGroupName_Type = TNamedItem
_VRtrMplsAdminGroupName_Object = MibTableColumn
vRtrMplsAdminGroupName = _VRtrMplsAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1, 1),
    _VRtrMplsAdminGroupName_Type()
)
vRtrMplsAdminGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupName.setStatus("current")
_VRtrMplsAdminGroupRowStatus_Type = RowStatus
_VRtrMplsAdminGroupRowStatus_Object = MibTableColumn
vRtrMplsAdminGroupRowStatus = _VRtrMplsAdminGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1, 2),
    _VRtrMplsAdminGroupRowStatus_Type()
)
vRtrMplsAdminGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupRowStatus.setStatus("current")


class _VRtrMplsAdminGroupValue_Type(Integer32):
    """Custom type vRtrMplsAdminGroupValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31),
    )


_VRtrMplsAdminGroupValue_Type.__name__ = "Integer32"
_VRtrMplsAdminGroupValue_Object = MibTableColumn
vRtrMplsAdminGroupValue = _VRtrMplsAdminGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 13, 1, 3),
    _VRtrMplsAdminGroupValue_Type()
)
vRtrMplsAdminGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsAdminGroupValue.setStatus("current")
_VRtrMplsFSGroupTable_Object = MibTable
vRtrMplsFSGroupTable = _VRtrMplsFSGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14)
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupTable.setStatus("current")
_VRtrMplsFSGroupEntry_Object = MibTableRow
vRtrMplsFSGroupEntry = _VRtrMplsFSGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1)
)
vRtrMplsFSGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsFSGroupName"),
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupEntry.setStatus("current")
_VRtrMplsFSGroupName_Type = TNamedItem
_VRtrMplsFSGroupName_Object = MibTableColumn
vRtrMplsFSGroupName = _VRtrMplsFSGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1, 1),
    _VRtrMplsFSGroupName_Type()
)
vRtrMplsFSGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupName.setStatus("current")
_VRtrMplsFSGroupRowStatus_Type = RowStatus
_VRtrMplsFSGroupRowStatus_Object = MibTableColumn
vRtrMplsFSGroupRowStatus = _VRtrMplsFSGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1, 2),
    _VRtrMplsFSGroupRowStatus_Type()
)
vRtrMplsFSGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupRowStatus.setStatus("current")


class _VRtrMplsFSGroupCost_Type(Unsigned32):
    """Custom type vRtrMplsFSGroupCost based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrMplsFSGroupCost_Type.__name__ = "Unsigned32"
_VRtrMplsFSGroupCost_Object = MibTableColumn
vRtrMplsFSGroupCost = _VRtrMplsFSGroupCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 14, 1, 3),
    _VRtrMplsFSGroupCost_Type()
)
vRtrMplsFSGroupCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupCost.setStatus("current")
_VRtrMplsFSGroupParamsTable_Object = MibTable
vRtrMplsFSGroupParamsTable = _VRtrMplsFSGroupParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15)
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsTable.setStatus("current")
_VRtrMplsFSGroupParamsEntry_Object = MibTableRow
vRtrMplsFSGroupParamsEntry = _VRtrMplsFSGroupParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1)
)
vRtrMplsFSGroupParamsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsFSGroupName"),
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsFromAddr"),
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsToAddr"),
)
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsEntry.setStatus("current")
_VRtrMplsFSGroupParamsFromAddr_Type = IpAddress
_VRtrMplsFSGroupParamsFromAddr_Object = MibTableColumn
vRtrMplsFSGroupParamsFromAddr = _VRtrMplsFSGroupParamsFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1, 1),
    _VRtrMplsFSGroupParamsFromAddr_Type()
)
vRtrMplsFSGroupParamsFromAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsFromAddr.setStatus("current")
_VRtrMplsFSGroupParamsToAddr_Type = IpAddress
_VRtrMplsFSGroupParamsToAddr_Object = MibTableColumn
vRtrMplsFSGroupParamsToAddr = _VRtrMplsFSGroupParamsToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1, 2),
    _VRtrMplsFSGroupParamsToAddr_Type()
)
vRtrMplsFSGroupParamsToAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsToAddr.setStatus("current")
_VRtrMplsFSGroupParamsRowStatus_Type = RowStatus
_VRtrMplsFSGroupParamsRowStatus_Object = MibTableColumn
vRtrMplsFSGroupParamsRowStatus = _VRtrMplsFSGroupParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 15, 1, 3),
    _VRtrMplsFSGroupParamsRowStatus_Type()
)
vRtrMplsFSGroupParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsFSGroupParamsRowStatus.setStatus("current")
_TmnxMplsNotificationlObjects_ObjectIdentity = ObjectIdentity
tmnxMplsNotificationlObjects = _TmnxMplsNotificationlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16)
)


class _VRtrMplsLspNotificationReasonCode_Type(Integer32):
    """Custom type vRtrMplsLspNotificationReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("noPathIsOperational", 1))
    )


_VRtrMplsLspNotificationReasonCode_Type.__name__ = "Integer32"
_VRtrMplsLspNotificationReasonCode_Object = MibScalar
vRtrMplsLspNotificationReasonCode = _VRtrMplsLspNotificationReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 1),
    _VRtrMplsLspNotificationReasonCode_Type()
)
vRtrMplsLspNotificationReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspNotificationReasonCode.setStatus("current")
_VRtrMplsLspPathNotificationReasonCode_Type = TmnxMplsLspFailCode
_VRtrMplsLspPathNotificationReasonCode_Object = MibScalar
vRtrMplsLspPathNotificationReasonCode = _VRtrMplsLspPathNotificationReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 2),
    _VRtrMplsLspPathNotificationReasonCode_Type()
)
vRtrMplsLspPathNotificationReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspPathNotificationReasonCode.setStatus("current")
_VRtrMplsNotifyRow_Type = RowPointer
_VRtrMplsNotifyRow_Object = MibScalar
vRtrMplsNotifyRow = _VRtrMplsNotifyRow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 16, 3),
    _VRtrMplsNotifyRow_Type()
)
vRtrMplsNotifyRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsNotifyRow.setStatus("current")
_VRtrMplsLabelRangeTable_Object = MibTable
vRtrMplsLabelRangeTable = _VRtrMplsLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17)
)
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeTable.setStatus("current")
_VRtrMplsLabelRangeEntry_Object = MibTableRow
vRtrMplsLabelRangeEntry = _VRtrMplsLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1)
)
vRtrMplsLabelRangeEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLabelType"),
)
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeEntry.setStatus("current")


class _VRtrMplsLabelType_Type(Integer32):
    """Custom type vRtrMplsLabelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("staticLsp", 1),
          ("staticSvc", 2))
    )


_VRtrMplsLabelType_Type.__name__ = "Integer32"
_VRtrMplsLabelType_Object = MibTableColumn
vRtrMplsLabelType = _VRtrMplsLabelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 1),
    _VRtrMplsLabelType_Type()
)
vRtrMplsLabelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLabelType.setStatus("current")
_VRtrMplsLabelRangeMin_Type = Unsigned32
_VRtrMplsLabelRangeMin_Object = MibTableColumn
vRtrMplsLabelRangeMin = _VRtrMplsLabelRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 2),
    _VRtrMplsLabelRangeMin_Type()
)
vRtrMplsLabelRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeMin.setStatus("current")
_VRtrMplsLabelRangeMax_Type = Unsigned32
_VRtrMplsLabelRangeMax_Object = MibTableColumn
vRtrMplsLabelRangeMax = _VRtrMplsLabelRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 3),
    _VRtrMplsLabelRangeMax_Type()
)
vRtrMplsLabelRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeMax.setStatus("current")
_VRtrMplsLabelRangeAging_Type = Unsigned32
_VRtrMplsLabelRangeAging_Object = MibTableColumn
vRtrMplsLabelRangeAging = _VRtrMplsLabelRangeAging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 4),
    _VRtrMplsLabelRangeAging_Type()
)
vRtrMplsLabelRangeAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeAging.setStatus("current")
_VRtrMplsLabelRangeAvailable_Type = Unsigned32
_VRtrMplsLabelRangeAvailable_Object = MibTableColumn
vRtrMplsLabelRangeAvailable = _VRtrMplsLabelRangeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 17, 1, 5),
    _VRtrMplsLabelRangeAvailable_Type()
)
vRtrMplsLabelRangeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeAvailable.setStatus("current")
_VRtrMplsStaticLSPLabelTable_Object = MibTable
vRtrMplsStaticLSPLabelTable = _VRtrMplsStaticLSPLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18)
)
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelTable.setStatus("current")
_VRtrMplsStaticLSPLabelEntry_Object = MibTableRow
vRtrMplsStaticLSPLabelEntry = _VRtrMplsStaticLSPLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18, 1)
)
vRtrMplsStaticLSPLabelEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsStaticLSPLabel"),
)
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelEntry.setStatus("current")


class _VRtrMplsStaticLSPLabel_Type(MplsLabel):
    """Custom type vRtrMplsStaticLSPLabel based on MplsLabel"""
    subtypeSpec = MplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1023),
    )


_VRtrMplsStaticLSPLabel_Type.__name__ = "MplsLabel"
_VRtrMplsStaticLSPLabel_Object = MibTableColumn
vRtrMplsStaticLSPLabel = _VRtrMplsStaticLSPLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18, 1, 1),
    _VRtrMplsStaticLSPLabel_Type()
)
vRtrMplsStaticLSPLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabel.setStatus("current")
_VRtrMplsStaticLSPLabelOwner_Type = TmnxMplsLabelOwner
_VRtrMplsStaticLSPLabelOwner_Object = MibTableColumn
vRtrMplsStaticLSPLabelOwner = _VRtrMplsStaticLSPLabelOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 18, 1, 2),
    _VRtrMplsStaticLSPLabelOwner_Type()
)
vRtrMplsStaticLSPLabelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelOwner.setStatus("current")
_VRtrMplsStaticSvcLabelTable_Object = MibTable
vRtrMplsStaticSvcLabelTable = _VRtrMplsStaticSvcLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19)
)
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelTable.setStatus("current")
_VRtrMplsStaticSvcLabelEntry_Object = MibTableRow
vRtrMplsStaticSvcLabelEntry = _VRtrMplsStaticSvcLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19, 1)
)
vRtrMplsStaticSvcLabelEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsStaticSvcLabel"),
)
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelEntry.setStatus("current")


class _VRtrMplsStaticSvcLabel_Type(MplsLabel):
    """Custom type vRtrMplsStaticSvcLabel based on MplsLabel"""
    subtypeSpec = MplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 18431),
    )


_VRtrMplsStaticSvcLabel_Type.__name__ = "MplsLabel"
_VRtrMplsStaticSvcLabel_Object = MibTableColumn
vRtrMplsStaticSvcLabel = _VRtrMplsStaticSvcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19, 1, 1),
    _VRtrMplsStaticSvcLabel_Type()
)
vRtrMplsStaticSvcLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabel.setStatus("current")


class _VRtrMplsStaticSvcLabelOwner_Type(TmnxMplsLabelOwner):
    """Custom type vRtrMplsStaticSvcLabelOwner based on TmnxMplsLabelOwner"""


_VRtrMplsStaticSvcLabelOwner_Object = MibTableColumn
vRtrMplsStaticSvcLabelOwner = _VRtrMplsStaticSvcLabelOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 19, 1, 2),
    _VRtrMplsStaticSvcLabelOwner_Type()
)
vRtrMplsStaticSvcLabelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelOwner.setStatus("current")
_VRtrMplsSrlgGrpTableLastChanged_Type = TimeStamp
_VRtrMplsSrlgGrpTableLastChanged_Object = MibScalar
vRtrMplsSrlgGrpTableLastChanged = _VRtrMplsSrlgGrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 20),
    _VRtrMplsSrlgGrpTableLastChanged_Type()
)
vRtrMplsSrlgGrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpTableLastChanged.setStatus("current")
_VRtrMplsSrlgGrpTable_Object = MibTable
vRtrMplsSrlgGrpTable = _VRtrMplsSrlgGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21)
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpTable.setStatus("current")
_VRtrMplsSrlgGrpEntry_Object = MibTableRow
vRtrMplsSrlgGrpEntry = _VRtrMplsSrlgGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1)
)
vRtrMplsSrlgGrpEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpName"),
)
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpEntry.setStatus("current")
_VRtrMplsSrlgGrpName_Type = TNamedItem
_VRtrMplsSrlgGrpName_Object = MibTableColumn
vRtrMplsSrlgGrpName = _VRtrMplsSrlgGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 1),
    _VRtrMplsSrlgGrpName_Type()
)
vRtrMplsSrlgGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpName.setStatus("current")
_VRtrMplsSrlgGrpRowStatus_Type = RowStatus
_VRtrMplsSrlgGrpRowStatus_Object = MibTableColumn
vRtrMplsSrlgGrpRowStatus = _VRtrMplsSrlgGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 2),
    _VRtrMplsSrlgGrpRowStatus_Type()
)
vRtrMplsSrlgGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpRowStatus.setStatus("current")
_VRtrMplsSrlgGrpLastChanged_Type = TimeStamp
_VRtrMplsSrlgGrpLastChanged_Object = MibTableColumn
vRtrMplsSrlgGrpLastChanged = _VRtrMplsSrlgGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 3),
    _VRtrMplsSrlgGrpLastChanged_Type()
)
vRtrMplsSrlgGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpLastChanged.setStatus("current")
_VRtrMplsSrlgGrpValue_Type = Unsigned32
_VRtrMplsSrlgGrpValue_Object = MibTableColumn
vRtrMplsSrlgGrpValue = _VRtrMplsSrlgGrpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 21, 1, 4),
    _VRtrMplsSrlgGrpValue_Type()
)
vRtrMplsSrlgGrpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsSrlgGrpValue.setStatus("current")
_VRtrMplsIfSrlgGrpTblLastChanged_Type = TimeStamp
_VRtrMplsIfSrlgGrpTblLastChanged_Object = MibScalar
vRtrMplsIfSrlgGrpTblLastChanged = _VRtrMplsIfSrlgGrpTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 22),
    _VRtrMplsIfSrlgGrpTblLastChanged_Type()
)
vRtrMplsIfSrlgGrpTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpTblLastChanged.setStatus("current")
_VRtrMplsIfSrlgGrpTable_Object = MibTable
vRtrMplsIfSrlgGrpTable = _VRtrMplsIfSrlgGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23)
)
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpTable.setStatus("current")
_VRtrMplsIfSrlgGrpEntry_Object = MibTableRow
vRtrMplsIfSrlgGrpEntry = _VRtrMplsIfSrlgGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1)
)
vRtrMplsIfSrlgGrpEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (1, "ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpName"),
)
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpEntry.setStatus("current")
_VRtrMplsIfSrlgGrpName_Type = TNamedItem
_VRtrMplsIfSrlgGrpName_Object = MibTableColumn
vRtrMplsIfSrlgGrpName = _VRtrMplsIfSrlgGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1, 1),
    _VRtrMplsIfSrlgGrpName_Type()
)
vRtrMplsIfSrlgGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpName.setStatus("current")
_VRtrMplsIfSrlgGrpRowStatus_Type = RowStatus
_VRtrMplsIfSrlgGrpRowStatus_Object = MibTableColumn
vRtrMplsIfSrlgGrpRowStatus = _VRtrMplsIfSrlgGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1, 2),
    _VRtrMplsIfSrlgGrpRowStatus_Type()
)
vRtrMplsIfSrlgGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpRowStatus.setStatus("current")
_VRtrMplsIfSrlgGrpLastChanged_Type = TimeStamp
_VRtrMplsIfSrlgGrpLastChanged_Object = MibTableColumn
vRtrMplsIfSrlgGrpLastChanged = _VRtrMplsIfSrlgGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 6, 23, 1, 3),
    _VRtrMplsIfSrlgGrpLastChanged_Type()
)
vRtrMplsIfSrlgGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfSrlgGrpLastChanged.setStatus("current")
_TmnxMplsNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMplsNotifyPrefix = _TmnxMplsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6)
)
_TmnxMplsNotifications_ObjectIdentity = ObjectIdentity
tmnxMplsNotifications = _TmnxMplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0)
)
vRtrMplsLspEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-MPLS-MIB",
     "vRtrMplsLspStatEntry")
)
vRtrMplsLspStatEntry.setIndexNames(*vRtrMplsLspEntry.getIndexNames())
vRtrMplsLspPathEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-MPLS-MIB",
     "vRtrMplsLspPathStatEntry")
)
vRtrMplsLspPathStatEntry.setIndexNames(*vRtrMplsLspPathEntry.getIndexNames())
vRtrMplsGeneralEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-MPLS-MIB",
     "vRtrMplsGeneralStatEntry")
)
vRtrMplsGeneralStatEntry.setIndexNames(*vRtrMplsGeneralEntry.getIndexNames())
vRtrMplsIfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-MPLS-MIB",
     "vRtrMplsIfStatEntry")
)
vRtrMplsIfStatEntry.setIndexNames(*vRtrMplsIfEntry.getIndexNames())
mplsTunnelARHopEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-MPLS-MIB",
     "vRtrMplsTunnelARHopEntry")
)
vRtrMplsTunnelARHopEntry.setIndexNames(*mplsTunnelARHopEntry.getIndexNames())

# Managed Objects groups

tmnxMplsLspPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 3)
)
tmnxMplsLspPathGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathTableSpinlock"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathRowStatus"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathLastChange"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathType"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathCos"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathProperties"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathBandwidth"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathBwProtect"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathPreference"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathCosSource"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathClassOfService"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathSetupPriority"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathHoldPriority"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecord"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathHopLimit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathSharing"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathInheritance"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathLspId"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryTimeRemaining"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelARHopListIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathNegotiatedMTU"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailCode"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathFailNodeAddr"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupInclude"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminGroupExclude"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdaptive"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathOptimizeTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathNextOptimize"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperBandwidth"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathMBBState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignal"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathTunnelCRHopListIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperMTU"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathRecordLabel"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeUp"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathTimeDown"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathRetryAttempts"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathTransitionCount"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathCspfQueries"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspPathGroup.setStatus("current")

tmnxMplsXCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 4)
)
tmnxMplsXCGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsXCIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsInSegmentIfIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsInSegmentLabel"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsOutSegmentIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsERHopTunnelIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsARHopTunnelIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsRsvpSessionIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsXCFailCode"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsXCCHopTableIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsXCGroup.setStatus("current")

tmnxMplsIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 5)
)
tmnxMplsIfGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfOperState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfAdminGroup"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfTxPktCount"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfRxPktCount"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfTxOctetCount"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfRxOctetCount"))
)
if mibBuilder.loadTexts:
    tmnxMplsIfGroup.setStatus("current")

tmnxMplsTunnelARHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 6)
)
tmnxMplsTunnelARHopGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopProtection"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopRecordLabel"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelARHopRouterId"))
)
if mibBuilder.loadTexts:
    tmnxMplsTunnelARHopGroup.setStatus("current")

tmnxMplsTunnelCHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 7)
)
tmnxMplsTunnelCHopGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopAddrType"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv4Addr"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv4PrefixLen"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv6Addr"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopIpv6PrefixLen"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopAsNumber"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopLspId"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsTunnelCHopStrictOrLoose"))
)
if mibBuilder.loadTexts:
    tmnxMplsTunnelCHopGroup.setStatus("current")

tmnxMplsAdminGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 8)
)
tmnxMplsAdminGroupGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupRowStatus"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsAdminGroupValue"))
)
if mibBuilder.loadTexts:
    tmnxMplsAdminGroupGroup.setStatus("current")

tmnxMplsFSGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 9)
)
tmnxMplsFSGroupGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsFSGroupRowStatus"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsFSGroupCost"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsFSGroupParamsRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxMplsFSGroupGroup.setStatus("current")

tmnxMplsNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 10)
)
tmnxMplsNotifyObjsGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspNotificationReasonCode"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathNotificationReasonCode"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsNotifyRow"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotifyObjsGroup.setStatus("current")

tmnxMplsGlobalR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 12)
)
tmnxMplsGlobalR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalR2r1Group.setStatus("obsolete")

tmnxMplsLspR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 13)
)
tmnxMplsLspR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspDecrementTtl"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspClassOfService"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPreference"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspBandwidth"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspBwProtect"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspR2r1Group.setStatus("obsolete")

tmnxMplsLabelRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 15)
)
tmnxMplsLabelRangeGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeMin"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeMax"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeAging"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLabelRangeAvailable"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsStaticLSPLabelOwner"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsStaticSvcLabelOwner"))
)
if mibBuilder.loadTexts:
    tmnxMplsLabelRangeGroup.setStatus("current")

tmnxMplsGlobalV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 16)
)
tmnxMplsGlobalV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralHoldTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicBypass"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV5v0Group.setStatus("obsolete")

tmnxMplsLspV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 17)
)
tmnxMplsLspV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRowStatus"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspLastChange"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspName"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFromAddr"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspToAddr"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspType"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOutSegIndx"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRetryTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRetryLimit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspMetric"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspDecrementTtl"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspCspf"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFastReroute"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFRHopLimit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFRBandwidth"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspClassOfService"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspSetupPriority"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspHoldPriority"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRecord"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPreference"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspBandwidth"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspBwProtect"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspHopLimit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspNegotiatedMTU"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpResvStyle"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspRsvpAdspec"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFRMethod"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFRNodeProtect"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupInclude"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAdminGroupExclude"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAdaptive"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspInheritance"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOptimizeTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOperFastReroute"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspFRObject"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOctets"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPackets"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAge"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspTimeUp"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspTimeDown"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPrimaryTimeUp"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspTransitions"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspLastTransition"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathChanges"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspLastPathChange"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspConfiguredPaths"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspStandbyPaths"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOperationalPaths"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspHoldTimer"))
)
if mibBuilder.loadTexts:
    tmnxMplsLspV5v0Group.setStatus("current")

tmnxMplsGlobalV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 18)
)
tmnxMplsGlobalV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralLastChange"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralPropagateTtl"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralTE"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralNewLspIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralOptimizeTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralFRObject"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralResignalTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspOriginate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTransit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralStaticLspTerminate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspOriginate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTransit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicLspTerminate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspOriginate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTransit"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDetourLspTerminate"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralHoldTimer"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralDynamicBypass"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralNextResignal"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperDownReason"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrr"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralSrlgFrrStrict"))
)
if mibBuilder.loadTexts:
    tmnxMplsGlobalV6v0Group.setStatus("current")

tmnxMplsSrlgV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 19)
)
tmnxMplsSrlgV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpRowStatus"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpLastChanged"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsSrlgGrpValue"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpTblLastChanged"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpRowStatus"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfSrlgGrpLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMplsSrlgV6v0Group.setStatus("current")

tmnxMplsIfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 21)
)
tmnxMplsIfV6v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfTeMetric")
)
if mibBuilder.loadTexts:
    tmnxMplsIfV6v0Group.setStatus("current")

tmnxMplsLspV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 22)
)
tmnxMplsLspV6v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspCspfTeMetricEnabled")
)
if mibBuilder.loadTexts:
    tmnxMplsLspV6v0Group.setStatus("current")


# Notification objects

vRtrMplsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 1)
)
vRtrMplsStateChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsGeneralOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsStateChange.setStatus(
        "current"
    )

vRtrMplsIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 2)
)
vRtrMplsIfStateChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsIfStateChange.setStatus(
        "current"
    )

vRtrMplsLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 3)
)
vRtrMplsLspUp.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspUp.setStatus(
        "current"
    )

vRtrMplsLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 4)
)
vRtrMplsLspDown.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspOperState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspNotificationReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspDown.setStatus(
        "current"
    )

vRtrMplsLspPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 5)
)
vRtrMplsLspPathUp.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathUp.setStatus(
        "current"
    )

vRtrMplsLspPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 6)
)
vRtrMplsLspPathDown.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
        ("MPLS-TE-MIB", "mplsTunnelIndex"),
        ("MPLS-TE-MIB", "mplsTunnelInstance"),
        ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathNotificationReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathDown.setStatus(
        "current"
    )

vRtrMplsLspPathRerouted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 7)
)
vRtrMplsLspPathRerouted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathRerouted.setStatus(
        "current"
    )

vRtrMplsLspPathResignaled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 6, 0, 8)
)
vRtrMplsLspPathResignaled.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathAdminState"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathOperState"))
)
if mibBuilder.loadTexts:
    vRtrMplsLspPathResignaled.setStatus(
        "current"
    )


# Notifications groups

tmnxMplsNotificationR2r1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 2, 14)
)
tmnxMplsNotificationR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsStateChange"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsIfStateChange"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspUp"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspDown"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathUp"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathDown"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathRerouted"),
        ("ALCATEL-IND1-TIMETRA-MPLS-MIB", "vRtrMplsLspPathResignaled"))
)
if mibBuilder.loadTexts:
    tmnxMplsNotificationR2r1Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMplsV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxMplsV3v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxMplsV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxMplsV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxMplsV6v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-MPLS-MIB",
    **{"TmnxMplsLspFailCode": TmnxMplsLspFailCode,
       "TmnxMplsLabelOwner": TmnxMplsLabelOwner,
       "TmnxMplsOperDownReasonCode": TmnxMplsOperDownReasonCode,
       "timetraMplsMIBModule": timetraMplsMIBModule,
       "tmnxMplsConformance": tmnxMplsConformance,
       "tmnxMplsCompliances": tmnxMplsCompliances,
       "tmnxMplsV3v0Compliance": tmnxMplsV3v0Compliance,
       "tmnxMplsV5v0Compliance": tmnxMplsV5v0Compliance,
       "tmnxMplsV6v0Compliance": tmnxMplsV6v0Compliance,
       "tmnxMplsGroups": tmnxMplsGroups,
       "tmnxMplsLspPathGroup": tmnxMplsLspPathGroup,
       "tmnxMplsXCGroup": tmnxMplsXCGroup,
       "tmnxMplsIfGroup": tmnxMplsIfGroup,
       "tmnxMplsTunnelARHopGroup": tmnxMplsTunnelARHopGroup,
       "tmnxMplsTunnelCHopGroup": tmnxMplsTunnelCHopGroup,
       "tmnxMplsAdminGroupGroup": tmnxMplsAdminGroupGroup,
       "tmnxMplsFSGroupGroup": tmnxMplsFSGroupGroup,
       "tmnxMplsNotifyObjsGroup": tmnxMplsNotifyObjsGroup,
       "tmnxMplsGlobalR2r1Group": tmnxMplsGlobalR2r1Group,
       "tmnxMplsLspR2r1Group": tmnxMplsLspR2r1Group,
       "tmnxMplsNotificationR2r1Group": tmnxMplsNotificationR2r1Group,
       "tmnxMplsLabelRangeGroup": tmnxMplsLabelRangeGroup,
       "tmnxMplsGlobalV5v0Group": tmnxMplsGlobalV5v0Group,
       "tmnxMplsLspV5v0Group": tmnxMplsLspV5v0Group,
       "tmnxMplsGlobalV6v0Group": tmnxMplsGlobalV6v0Group,
       "tmnxMplsSrlgV6v0Group": tmnxMplsSrlgV6v0Group,
       "tmnxMplsIfV6v0Group": tmnxMplsIfV6v0Group,
       "tmnxMplsLspV6v0Group": tmnxMplsLspV6v0Group,
       "tmnxMplsObjs": tmnxMplsObjs,
       "vRtrMplsLspTable": vRtrMplsLspTable,
       "vRtrMplsLspEntry": vRtrMplsLspEntry,
       "vRtrMplsLspIndex": vRtrMplsLspIndex,
       "vRtrMplsLspRowStatus": vRtrMplsLspRowStatus,
       "vRtrMplsLspLastChange": vRtrMplsLspLastChange,
       "vRtrMplsLspName": vRtrMplsLspName,
       "vRtrMplsLspAdminState": vRtrMplsLspAdminState,
       "vRtrMplsLspOperState": vRtrMplsLspOperState,
       "vRtrMplsLspFromAddr": vRtrMplsLspFromAddr,
       "vRtrMplsLspToAddr": vRtrMplsLspToAddr,
       "vRtrMplsLspType": vRtrMplsLspType,
       "vRtrMplsLspOutSegIndx": vRtrMplsLspOutSegIndx,
       "vRtrMplsLspRetryTimer": vRtrMplsLspRetryTimer,
       "vRtrMplsLspRetryLimit": vRtrMplsLspRetryLimit,
       "vRtrMplsLspMetric": vRtrMplsLspMetric,
       "vRtrMplsLspDecrementTtl": vRtrMplsLspDecrementTtl,
       "vRtrMplsLspCspf": vRtrMplsLspCspf,
       "vRtrMplsLspFastReroute": vRtrMplsLspFastReroute,
       "vRtrMplsLspFRHopLimit": vRtrMplsLspFRHopLimit,
       "vRtrMplsLspFRBandwidth": vRtrMplsLspFRBandwidth,
       "vRtrMplsLspClassOfService": vRtrMplsLspClassOfService,
       "vRtrMplsLspSetupPriority": vRtrMplsLspSetupPriority,
       "vRtrMplsLspHoldPriority": vRtrMplsLspHoldPriority,
       "vRtrMplsLspRecord": vRtrMplsLspRecord,
       "vRtrMplsLspPreference": vRtrMplsLspPreference,
       "vRtrMplsLspBandwidth": vRtrMplsLspBandwidth,
       "vRtrMplsLspBwProtect": vRtrMplsLspBwProtect,
       "vRtrMplsLspHopLimit": vRtrMplsLspHopLimit,
       "vRtrMplsLspNegotiatedMTU": vRtrMplsLspNegotiatedMTU,
       "vRtrMplsLspRsvpResvStyle": vRtrMplsLspRsvpResvStyle,
       "vRtrMplsLspRsvpAdspec": vRtrMplsLspRsvpAdspec,
       "vRtrMplsLspFRMethod": vRtrMplsLspFRMethod,
       "vRtrMplsLspFRNodeProtect": vRtrMplsLspFRNodeProtect,
       "vRtrMplsLspAdminGroupInclude": vRtrMplsLspAdminGroupInclude,
       "vRtrMplsLspAdminGroupExclude": vRtrMplsLspAdminGroupExclude,
       "vRtrMplsLspAdaptive": vRtrMplsLspAdaptive,
       "vRtrMplsLspInheritance": vRtrMplsLspInheritance,
       "vRtrMplsLspOptimizeTimer": vRtrMplsLspOptimizeTimer,
       "vRtrMplsLspOperFastReroute": vRtrMplsLspOperFastReroute,
       "vRtrMplsLspFRObject": vRtrMplsLspFRObject,
       "vRtrMplsLspHoldTimer": vRtrMplsLspHoldTimer,
       "vRtrMplsLspCspfTeMetricEnabled": vRtrMplsLspCspfTeMetricEnabled,
       "vRtrMplsLspStatTable": vRtrMplsLspStatTable,
       "vRtrMplsLspStatEntry": vRtrMplsLspStatEntry,
       "vRtrMplsLspOctets": vRtrMplsLspOctets,
       "vRtrMplsLspPackets": vRtrMplsLspPackets,
       "vRtrMplsLspAge": vRtrMplsLspAge,
       "vRtrMplsLspTimeUp": vRtrMplsLspTimeUp,
       "vRtrMplsLspTimeDown": vRtrMplsLspTimeDown,
       "vRtrMplsLspPrimaryTimeUp": vRtrMplsLspPrimaryTimeUp,
       "vRtrMplsLspTransitions": vRtrMplsLspTransitions,
       "vRtrMplsLspLastTransition": vRtrMplsLspLastTransition,
       "vRtrMplsLspPathChanges": vRtrMplsLspPathChanges,
       "vRtrMplsLspLastPathChange": vRtrMplsLspLastPathChange,
       "vRtrMplsLspConfiguredPaths": vRtrMplsLspConfiguredPaths,
       "vRtrMplsLspStandbyPaths": vRtrMplsLspStandbyPaths,
       "vRtrMplsLspOperationalPaths": vRtrMplsLspOperationalPaths,
       "vRtrMplsLspPathTableSpinlock": vRtrMplsLspPathTableSpinlock,
       "vRtrMplsLspPathTable": vRtrMplsLspPathTable,
       "vRtrMplsLspPathEntry": vRtrMplsLspPathEntry,
       "vRtrMplsLspPathRowStatus": vRtrMplsLspPathRowStatus,
       "vRtrMplsLspPathLastChange": vRtrMplsLspPathLastChange,
       "vRtrMplsLspPathType": vRtrMplsLspPathType,
       "vRtrMplsLspPathCos": vRtrMplsLspPathCos,
       "vRtrMplsLspPathProperties": vRtrMplsLspPathProperties,
       "vRtrMplsLspPathBandwidth": vRtrMplsLspPathBandwidth,
       "vRtrMplsLspPathBwProtect": vRtrMplsLspPathBwProtect,
       "vRtrMplsLspPathState": vRtrMplsLspPathState,
       "vRtrMplsLspPathPreference": vRtrMplsLspPathPreference,
       "vRtrMplsLspPathCosSource": vRtrMplsLspPathCosSource,
       "vRtrMplsLspPathClassOfService": vRtrMplsLspPathClassOfService,
       "vRtrMplsLspPathSetupPriority": vRtrMplsLspPathSetupPriority,
       "vRtrMplsLspPathHoldPriority": vRtrMplsLspPathHoldPriority,
       "vRtrMplsLspPathRecord": vRtrMplsLspPathRecord,
       "vRtrMplsLspPathHopLimit": vRtrMplsLspPathHopLimit,
       "vRtrMplsLspPathSharing": vRtrMplsLspPathSharing,
       "vRtrMplsLspPathAdminState": vRtrMplsLspPathAdminState,
       "vRtrMplsLspPathOperState": vRtrMplsLspPathOperState,
       "vRtrMplsLspPathInheritance": vRtrMplsLspPathInheritance,
       "vRtrMplsLspPathLspId": vRtrMplsLspPathLspId,
       "vRtrMplsLspPathRetryTimeRemaining": vRtrMplsLspPathRetryTimeRemaining,
       "vRtrMplsLspPathTunnelARHopListIndex": vRtrMplsLspPathTunnelARHopListIndex,
       "vRtrMplsLspPathNegotiatedMTU": vRtrMplsLspPathNegotiatedMTU,
       "vRtrMplsLspPathFailCode": vRtrMplsLspPathFailCode,
       "vRtrMplsLspPathFailNodeAddr": vRtrMplsLspPathFailNodeAddr,
       "vRtrMplsLspPathAdminGroupInclude": vRtrMplsLspPathAdminGroupInclude,
       "vRtrMplsLspPathAdminGroupExclude": vRtrMplsLspPathAdminGroupExclude,
       "vRtrMplsLspPathAdaptive": vRtrMplsLspPathAdaptive,
       "vRtrMplsLspPathOptimizeTimer": vRtrMplsLspPathOptimizeTimer,
       "vRtrMplsLspPathNextOptimize": vRtrMplsLspPathNextOptimize,
       "vRtrMplsLspPathOperBandwidth": vRtrMplsLspPathOperBandwidth,
       "vRtrMplsLspPathMBBState": vRtrMplsLspPathMBBState,
       "vRtrMplsLspPathResignal": vRtrMplsLspPathResignal,
       "vRtrMplsLspPathTunnelCRHopListIndex": vRtrMplsLspPathTunnelCRHopListIndex,
       "vRtrMplsLspPathOperMTU": vRtrMplsLspPathOperMTU,
       "vRtrMplsLspPathRecordLabel": vRtrMplsLspPathRecordLabel,
       "vRtrMplsLspPathStatTable": vRtrMplsLspPathStatTable,
       "vRtrMplsLspPathStatEntry": vRtrMplsLspPathStatEntry,
       "vRtrMplsLspPathTimeUp": vRtrMplsLspPathTimeUp,
       "vRtrMplsLspPathTimeDown": vRtrMplsLspPathTimeDown,
       "vRtrMplsLspPathRetryAttempts": vRtrMplsLspPathRetryAttempts,
       "vRtrMplsLspPathTransitionCount": vRtrMplsLspPathTransitionCount,
       "vRtrMplsLspPathCspfQueries": vRtrMplsLspPathCspfQueries,
       "vRtrMplsXCTable": vRtrMplsXCTable,
       "vRtrMplsXCEntry": vRtrMplsXCEntry,
       "vRtrMplsXCIndex": vRtrMplsXCIndex,
       "vRtrMplsInSegmentIfIndex": vRtrMplsInSegmentIfIndex,
       "vRtrMplsInSegmentLabel": vRtrMplsInSegmentLabel,
       "vRtrMplsOutSegmentIndex": vRtrMplsOutSegmentIndex,
       "vRtrMplsERHopTunnelIndex": vRtrMplsERHopTunnelIndex,
       "vRtrMplsARHopTunnelIndex": vRtrMplsARHopTunnelIndex,
       "vRtrMplsRsvpSessionIndex": vRtrMplsRsvpSessionIndex,
       "vRtrMplsXCFailCode": vRtrMplsXCFailCode,
       "vRtrMplsXCCHopTableIndex": vRtrMplsXCCHopTableIndex,
       "vRtrMplsGeneralTable": vRtrMplsGeneralTable,
       "vRtrMplsGeneralEntry": vRtrMplsGeneralEntry,
       "vRtrMplsGeneralLastChange": vRtrMplsGeneralLastChange,
       "vRtrMplsGeneralAdminState": vRtrMplsGeneralAdminState,
       "vRtrMplsGeneralOperState": vRtrMplsGeneralOperState,
       "vRtrMplsGeneralPropagateTtl": vRtrMplsGeneralPropagateTtl,
       "vRtrMplsGeneralTE": vRtrMplsGeneralTE,
       "vRtrMplsGeneralNewLspIndex": vRtrMplsGeneralNewLspIndex,
       "vRtrMplsGeneralOptimizeTimer": vRtrMplsGeneralOptimizeTimer,
       "vRtrMplsGeneralFRObject": vRtrMplsGeneralFRObject,
       "vRtrMplsGeneralResignalTimer": vRtrMplsGeneralResignalTimer,
       "vRtrMplsGeneralHoldTimer": vRtrMplsGeneralHoldTimer,
       "vRtrMplsGeneralDynamicBypass": vRtrMplsGeneralDynamicBypass,
       "vRtrMplsGeneralNextResignal": vRtrMplsGeneralNextResignal,
       "vRtrMplsGeneralOperDownReason": vRtrMplsGeneralOperDownReason,
       "vRtrMplsGeneralSrlgFrr": vRtrMplsGeneralSrlgFrr,
       "vRtrMplsGeneralSrlgFrrStrict": vRtrMplsGeneralSrlgFrrStrict,
       "vRtrMplsGeneralStatTable": vRtrMplsGeneralStatTable,
       "vRtrMplsGeneralStatEntry": vRtrMplsGeneralStatEntry,
       "vRtrMplsGeneralStaticLspOriginate": vRtrMplsGeneralStaticLspOriginate,
       "vRtrMplsGeneralStaticLspTransit": vRtrMplsGeneralStaticLspTransit,
       "vRtrMplsGeneralStaticLspTerminate": vRtrMplsGeneralStaticLspTerminate,
       "vRtrMplsGeneralDynamicLspOriginate": vRtrMplsGeneralDynamicLspOriginate,
       "vRtrMplsGeneralDynamicLspTransit": vRtrMplsGeneralDynamicLspTransit,
       "vRtrMplsGeneralDynamicLspTerminate": vRtrMplsGeneralDynamicLspTerminate,
       "vRtrMplsGeneralDetourLspOriginate": vRtrMplsGeneralDetourLspOriginate,
       "vRtrMplsGeneralDetourLspTransit": vRtrMplsGeneralDetourLspTransit,
       "vRtrMplsGeneralDetourLspTerminate": vRtrMplsGeneralDetourLspTerminate,
       "vRtrMplsIfTable": vRtrMplsIfTable,
       "vRtrMplsIfEntry": vRtrMplsIfEntry,
       "vRtrMplsIfAdminState": vRtrMplsIfAdminState,
       "vRtrMplsIfOperState": vRtrMplsIfOperState,
       "vRtrMplsIfAdminGroup": vRtrMplsIfAdminGroup,
       "vRtrMplsIfTeMetric": vRtrMplsIfTeMetric,
       "vRtrMplsIfStatTable": vRtrMplsIfStatTable,
       "vRtrMplsIfStatEntry": vRtrMplsIfStatEntry,
       "vRtrMplsIfTxPktCount": vRtrMplsIfTxPktCount,
       "vRtrMplsIfRxPktCount": vRtrMplsIfRxPktCount,
       "vRtrMplsIfTxOctetCount": vRtrMplsIfTxOctetCount,
       "vRtrMplsIfRxOctetCount": vRtrMplsIfRxOctetCount,
       "vRtrMplsTunnelARHopTable": vRtrMplsTunnelARHopTable,
       "vRtrMplsTunnelARHopEntry": vRtrMplsTunnelARHopEntry,
       "vRtrMplsTunnelARHopProtection": vRtrMplsTunnelARHopProtection,
       "vRtrMplsTunnelARHopRecordLabel": vRtrMplsTunnelARHopRecordLabel,
       "vRtrMplsTunnelARHopRouterId": vRtrMplsTunnelARHopRouterId,
       "vRtrMplsTunnelCHopTable": vRtrMplsTunnelCHopTable,
       "vRtrMplsTunnelCHopEntry": vRtrMplsTunnelCHopEntry,
       "vRtrMplsTunnelCHopListIndex": vRtrMplsTunnelCHopListIndex,
       "vRtrMplsTunnelCHopIndex": vRtrMplsTunnelCHopIndex,
       "vRtrMplsTunnelCHopAddrType": vRtrMplsTunnelCHopAddrType,
       "vRtrMplsTunnelCHopIpv4Addr": vRtrMplsTunnelCHopIpv4Addr,
       "vRtrMplsTunnelCHopIpv4PrefixLen": vRtrMplsTunnelCHopIpv4PrefixLen,
       "vRtrMplsTunnelCHopIpv6Addr": vRtrMplsTunnelCHopIpv6Addr,
       "vRtrMplsTunnelCHopIpv6PrefixLen": vRtrMplsTunnelCHopIpv6PrefixLen,
       "vRtrMplsTunnelCHopAsNumber": vRtrMplsTunnelCHopAsNumber,
       "vRtrMplsTunnelCHopLspId": vRtrMplsTunnelCHopLspId,
       "vRtrMplsTunnelCHopStrictOrLoose": vRtrMplsTunnelCHopStrictOrLoose,
       "vRtrMplsAdminGroupTable": vRtrMplsAdminGroupTable,
       "vRtrMplsAdminGroupEntry": vRtrMplsAdminGroupEntry,
       "vRtrMplsAdminGroupName": vRtrMplsAdminGroupName,
       "vRtrMplsAdminGroupRowStatus": vRtrMplsAdminGroupRowStatus,
       "vRtrMplsAdminGroupValue": vRtrMplsAdminGroupValue,
       "vRtrMplsFSGroupTable": vRtrMplsFSGroupTable,
       "vRtrMplsFSGroupEntry": vRtrMplsFSGroupEntry,
       "vRtrMplsFSGroupName": vRtrMplsFSGroupName,
       "vRtrMplsFSGroupRowStatus": vRtrMplsFSGroupRowStatus,
       "vRtrMplsFSGroupCost": vRtrMplsFSGroupCost,
       "vRtrMplsFSGroupParamsTable": vRtrMplsFSGroupParamsTable,
       "vRtrMplsFSGroupParamsEntry": vRtrMplsFSGroupParamsEntry,
       "vRtrMplsFSGroupParamsFromAddr": vRtrMplsFSGroupParamsFromAddr,
       "vRtrMplsFSGroupParamsToAddr": vRtrMplsFSGroupParamsToAddr,
       "vRtrMplsFSGroupParamsRowStatus": vRtrMplsFSGroupParamsRowStatus,
       "tmnxMplsNotificationlObjects": tmnxMplsNotificationlObjects,
       "vRtrMplsLspNotificationReasonCode": vRtrMplsLspNotificationReasonCode,
       "vRtrMplsLspPathNotificationReasonCode": vRtrMplsLspPathNotificationReasonCode,
       "vRtrMplsNotifyRow": vRtrMplsNotifyRow,
       "vRtrMplsLabelRangeTable": vRtrMplsLabelRangeTable,
       "vRtrMplsLabelRangeEntry": vRtrMplsLabelRangeEntry,
       "vRtrMplsLabelType": vRtrMplsLabelType,
       "vRtrMplsLabelRangeMin": vRtrMplsLabelRangeMin,
       "vRtrMplsLabelRangeMax": vRtrMplsLabelRangeMax,
       "vRtrMplsLabelRangeAging": vRtrMplsLabelRangeAging,
       "vRtrMplsLabelRangeAvailable": vRtrMplsLabelRangeAvailable,
       "vRtrMplsStaticLSPLabelTable": vRtrMplsStaticLSPLabelTable,
       "vRtrMplsStaticLSPLabelEntry": vRtrMplsStaticLSPLabelEntry,
       "vRtrMplsStaticLSPLabel": vRtrMplsStaticLSPLabel,
       "vRtrMplsStaticLSPLabelOwner": vRtrMplsStaticLSPLabelOwner,
       "vRtrMplsStaticSvcLabelTable": vRtrMplsStaticSvcLabelTable,
       "vRtrMplsStaticSvcLabelEntry": vRtrMplsStaticSvcLabelEntry,
       "vRtrMplsStaticSvcLabel": vRtrMplsStaticSvcLabel,
       "vRtrMplsStaticSvcLabelOwner": vRtrMplsStaticSvcLabelOwner,
       "vRtrMplsSrlgGrpTableLastChanged": vRtrMplsSrlgGrpTableLastChanged,
       "vRtrMplsSrlgGrpTable": vRtrMplsSrlgGrpTable,
       "vRtrMplsSrlgGrpEntry": vRtrMplsSrlgGrpEntry,
       "vRtrMplsSrlgGrpName": vRtrMplsSrlgGrpName,
       "vRtrMplsSrlgGrpRowStatus": vRtrMplsSrlgGrpRowStatus,
       "vRtrMplsSrlgGrpLastChanged": vRtrMplsSrlgGrpLastChanged,
       "vRtrMplsSrlgGrpValue": vRtrMplsSrlgGrpValue,
       "vRtrMplsIfSrlgGrpTblLastChanged": vRtrMplsIfSrlgGrpTblLastChanged,
       "vRtrMplsIfSrlgGrpTable": vRtrMplsIfSrlgGrpTable,
       "vRtrMplsIfSrlgGrpEntry": vRtrMplsIfSrlgGrpEntry,
       "vRtrMplsIfSrlgGrpName": vRtrMplsIfSrlgGrpName,
       "vRtrMplsIfSrlgGrpRowStatus": vRtrMplsIfSrlgGrpRowStatus,
       "vRtrMplsIfSrlgGrpLastChanged": vRtrMplsIfSrlgGrpLastChanged,
       "tmnxMplsNotifyPrefix": tmnxMplsNotifyPrefix,
       "tmnxMplsNotifications": tmnxMplsNotifications,
       "vRtrMplsStateChange": vRtrMplsStateChange,
       "vRtrMplsIfStateChange": vRtrMplsIfStateChange,
       "vRtrMplsLspUp": vRtrMplsLspUp,
       "vRtrMplsLspDown": vRtrMplsLspDown,
       "vRtrMplsLspPathUp": vRtrMplsLspPathUp,
       "vRtrMplsLspPathDown": vRtrMplsLspPathDown,
       "vRtrMplsLspPathRerouted": vRtrMplsLspPathRerouted,
       "vRtrMplsLspPathResignaled": vRtrMplsLspPathResignaled}
)
